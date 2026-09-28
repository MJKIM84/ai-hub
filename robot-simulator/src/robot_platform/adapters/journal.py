"""Durable at-most-once dispatch journal, not an exactly-once physical execution claim."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import sqlite3
from threading import RLock

from .contracts import CommandFeedback, CommandStatus, RobotCommand


def fingerprint(command: RobotCommand) -> str:
    return json.dumps(asdict(command), sort_keys=True, separators=(",", ":"), allow_nan=False)


@dataclass(frozen=True)
class JournalClaim:
    dispatch: bool
    feedback: CommandFeedback


class CommandJournal:
    def __init__(self, path: str | Path = ":memory:"):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(str(path), timeout=10, isolation_level=None, check_same_thread=False)
        self._db.row_factory = sqlite3.Row
        self._lock = RLock()
        self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute("PRAGMA synchronous=FULL")
        self._db.executescript("""
            CREATE TABLE IF NOT EXISTS adapter_sessions (
                scope TEXT PRIMARY KEY, epoch INTEGER NOT NULL, last_sequence INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS adapter_commands (
                scope TEXT NOT NULL, command_id TEXT NOT NULL, fingerprint TEXT NOT NULL,
                epoch INTEGER NOT NULL, feedback_json TEXT NOT NULL,
                PRIMARY KEY(scope, command_id)
            );
        """)

    @staticmethod
    def _encode(feedback: CommandFeedback) -> str:
        return json.dumps(asdict(feedback), sort_keys=True, allow_nan=False)

    @staticmethod
    def _decode(value: str) -> CommandFeedback:
        data = json.loads(value)
        data["status"] = CommandStatus(data["status"])
        return CommandFeedback(**data)

    def new_epoch(self, scope: str, observed_at: float) -> int:
        """Invalidates outstanding outcomes before any new connection can dispatch."""
        with self._lock:
            self._db.execute("BEGIN IMMEDIATE")
            try:
                session = self._db.execute("SELECT epoch FROM adapter_sessions WHERE scope=?", (scope,)).fetchone()
                epoch = session["epoch"] + 1 if session else 1
                self._db.execute("""INSERT INTO adapter_sessions VALUES(?, ?, -1)
                    ON CONFLICT(scope) DO UPDATE SET epoch=excluded.epoch""", (scope, epoch))
                rows = self._db.execute("SELECT command_id,feedback_json FROM adapter_commands WHERE scope=?", (scope,)).fetchall()
                for row in rows:
                    f = self._decode(row["feedback_json"])
                    if f.status in (CommandStatus.ACCEPTED, CommandStatus.RUNNING):
                        replacement = CommandFeedback(f.command_id, CommandStatus.UNKNOWN, observed_at,
                            "new_session_previous_outcome_unconfirmed", f.vendor_command_id, f.connection_epoch)
                        self._db.execute("UPDATE adapter_commands SET feedback_json=? WHERE scope=? AND command_id=?",
                                         (self._encode(replacement), scope, f.command_id))
                self._db.execute("COMMIT")
                return epoch
            except Exception:
                self._db.execute("ROLLBACK")
                raise

    def lookup(self, scope: str, command_id: str) -> CommandFeedback | None:
        with self._lock:
            row = self._db.execute("SELECT feedback_json FROM adapter_commands WHERE scope=? AND command_id=?",
                                   (scope, command_id)).fetchone()
            return self._decode(row[0]) if row else None

    def duplicate(self, scope: str, command: RobotCommand, now: float) -> CommandFeedback | None:
        value = fingerprint(command)
        with self._lock:
            row = self._db.execute("SELECT fingerprint,feedback_json FROM adapter_commands WHERE scope=? AND command_id=?",
                                   (scope, command.command_id)).fetchone()
            if not row:
                return None
            if row["fingerprint"] != value:
                return CommandFeedback(command.command_id, CommandStatus.REJECTED, now,
                                       "command_id_payload_conflict", connection_epoch=command.connection_epoch)
            return self._decode(row["feedback_json"])

    def reserve(self, scope: str, command: RobotCommand, now: float) -> JournalClaim:
        """Commit before the side effect, accepting possible UNKNOWN after a crash."""
        value = fingerprint(command)
        with self._lock:
            self._db.execute("BEGIN IMMEDIATE")
            try:
                duplicate = self.duplicate(scope, command, now)
                if duplicate:
                    self._db.execute("COMMIT")
                    return JournalClaim(False, duplicate)
                session = self._db.execute("SELECT epoch,last_sequence FROM adapter_sessions WHERE scope=?", (scope,)).fetchone()
                reason = None
                if session is None or command.connection_epoch != session["epoch"]:
                    reason = "stale_connection_epoch"
                elif command.sequence <= session["last_sequence"]:
                    reason = "out_of_order_sequence"
                if reason:
                    feedback = CommandFeedback(command.command_id, CommandStatus.REJECTED, now,
                                               reason, connection_epoch=command.connection_epoch)
                    self._db.execute("COMMIT")
                    return JournalClaim(False, feedback)
                feedback = CommandFeedback(command.command_id, CommandStatus.ACCEPTED, now,
                                           "dispatch_reserved_result_unconfirmed", connection_epoch=command.connection_epoch)
                self._db.execute("INSERT INTO adapter_commands VALUES(?,?,?,?,?)",
                    (scope, command.command_id, value, command.connection_epoch, self._encode(feedback)))
                self._db.execute("UPDATE adapter_sessions SET last_sequence=? WHERE scope=?", (command.sequence, scope))
                self._db.execute("COMMIT")
                return JournalClaim(True, feedback)
            except Exception:
                self._db.execute("ROLLBACK")
                raise

    def update(self, scope: str, feedback: CommandFeedback) -> CommandFeedback:
        with self._lock:
            self._db.execute("BEGIN IMMEDIATE")
            try:
                row = self._db.execute("""SELECT c.epoch,c.feedback_json,s.epoch AS current_epoch
                    FROM adapter_commands c JOIN adapter_sessions s ON c.scope=s.scope
                    WHERE c.scope=? AND c.command_id=?""", (scope, feedback.command_id)).fetchone()
                if row is None:
                    raise KeyError(feedback.command_id)
                if row["epoch"] != row["current_epoch"] or row["epoch"] != feedback.connection_epoch:
                    result = self._decode(row["feedback_json"])
                else:
                    self._db.execute("UPDATE adapter_commands SET feedback_json=? WHERE scope=? AND command_id=?",
                                     (self._encode(feedback), scope, feedback.command_id))
                    result = feedback
                self._db.execute("COMMIT")
                return result
            except Exception:
                self._db.execute("ROLLBACK")
                raise

    def close(self) -> None:
        with self._lock:
            self._db.close()
