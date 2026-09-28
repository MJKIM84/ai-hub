"""Atomic cooperative reservations and observation-evidenced item custody.

The ledger never reads simulator truth or moves objects. Its trusted caller
supplies workflow observations and performs physical placement checks upstream.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import hashlib
import json
import math
from threading import RLock

from .loading_workflow import LoadingWorkflow
from .transport_workflow import TransportWorkflow


class ResourceConflict(ValueError):
    """The complete bundle or expected custody version is unavailable."""


def _id(value, label):
    if not isinstance(value, str) or not value:
        raise ValueError(label+' must be a nonempty string')
    return value


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(label+' must be finite and nonnegative')
    return float(value)


def _mapping(value, label):
    if not isinstance(value, Mapping):
        raise ValueError(label+' must be a mapping')
    return value


def _vector(value, label):
    if (not isinstance(value, (list, tuple)) or len(value) != 3
            or any(isinstance(component, bool) or not isinstance(component, (int, float))
                   or not math.isfinite(component) for component in value)):
        raise ValueError(label+' must be a finite three-dimensional vector')
    return tuple(value)


def _fingerprint(proof):
    # The transport payload cannot be reused simply by replacing the execution
    # envelope. This is replay detection, not cryptographic sender authentication.
    body = {key: value for key, value in proof.items() if key != 'execution_id'}
    try:
        canonical = json.dumps(body, sort_keys=True, allow_nan=False, separators=(',', ':'))
    except (TypeError, ValueError) as error:
        raise ValueError('evidence must contain finite JSON values') from error
    return hashlib.sha256(canonical.encode()).hexdigest()


class CooperativeResources:
    VERSION = 'observed-cooperative-resources-0.3'
    FRESH_AGE = TransportWorkflow.FRESH_AGE
    MAX_PEER_SKEW = TransportWorkflow.MAX_PEER_SKEW

    def __init__(self):
        self._lock = RLock()
        self._executions = {}
        self._resource_owners = {}
        self._items = {}
        self._proof_uses = {}
        self._recovery_requests = {}

    def _execution(self, execution_id, item_id=None):
        _id(execution_id, 'execution_id')
        if execution_id not in self._executions:
            raise ValueError('unknown execution')
        execution = self._executions[execution_id]
        if item_id is not None and item_id != execution['item_id']:
            raise ValueError('item does not belong to execution')
        return execution

    def _receipt(self, execution, *, idempotent=False, action=None, applied_version=None):
        item = self._items[execution['item_id']]
        return deepcopy(dict(execution_id=execution['execution_id'], task_id=execution['task_id'],
            participants=execution['participants'], item_id=execution['item_id'], workspace_id=execution['workspace_id'],
            status=execution['status'], resources=[key for key in execution['bundle'] if self._resource_owners.get(key)==execution['execution_id']],
            owner=item['owner'], version=item['version'], idempotent=idempotent,
            action=action, applied_version=applied_version, reason=execution['reason'],
            terminal_status=execution.get('terminal_status'), terminal_reason=execution.get('terminal_reason'),
            recovery=execution.get('recovery')))

    def acquire(self, execution_id, task_id, participants, item_id, workspace_id):
        execution_id, task_id, item_id, workspace_id = (_id(value, label) for value, label in
            ((execution_id, 'execution_id'), (task_id, 'task_id'), (item_id, 'item_id'), (workspace_id, 'workspace_id')))
        _mapping(participants, 'participants')
        if not participants:
            raise ValueError('at least one role is required')
        roles = {_id(role, 'role'): _id(rid, 'robot_id') for role, rid in participants.items()}
        if len(set(roles.values())) != len(roles):
            raise ValueError('different roles cannot use the same robot')
        identity = dict(task_id=task_id, participants=roles, item_id=item_id, workspace_id=workspace_id)
        bundle = sorted(['task:'+task_id, 'item:'+item_id, 'workspace:'+workspace_id, *('robot:'+rid for rid in roles.values())])
        with self._lock:
            if execution_id in self._executions:
                existing = self._executions[execution_id]
                if any(existing[key]!=value for key, value in identity.items()):
                    raise ResourceConflict('execution id already identifies a different bundle')
                return self._receipt(existing, idempotent=True, action='acquire')
            conflicts = {key: self._resource_owners[key] for key in bundle if key in self._resource_owners}
            if conflicts:
                raise ResourceConflict('bundle acquisition conflict: '+json.dumps(conflicts, sort_keys=True))
            execution = dict(identity, execution_id=execution_id, bundle=bundle, status='active',
                             reason=None, last_action_at=None, retained_at=None)
            self._executions[execution_id] = execution
            self._items.setdefault(item_id, dict(owner=None, version=0, last_evidence_at=None))
            self._resource_owners.update({key: execution_id for key in bundle})
            return self._receipt(execution, action='acquire')

    def _bound(self, execution, item_id, proof):
        _mapping(proof, 'evidence')
        if (proof.get('execution_id') != execution['execution_id'] or proof.get('task_id') != execution['task_id']
                or proof.get('item_id') != item_id):
            raise ValueError('evidence execution/task/item identity mismatch')
        if proof.get('workspace_id', execution['workspace_id']) != execution['workspace_id']:
            raise ValueError('evidence workspace identity mismatch')
        return _fingerprint(proof)

    def _replay(self, execution, key, operation):
        previous = self._proof_uses.get(key)
        if previous is None:
            return None
        if previous['execution_id'] != execution['execution_id'] or previous['operation'] != operation:
            raise ValueError('evidence already belongs to another execution or operation')
        # Return CURRENT custody. An old successful retry must not tell an
        # adapter to rewind an item that has since been transferred/released.
        return self._receipt(execution, idempotent=True, action=operation[0], applied_version=previous['version'])

    def _now(self, execution, now):
        now = _number(now, 'now')
        if execution['last_action_at'] is not None and now < execution['last_action_at']:
            raise ValueError('operation time cannot move backwards')
        return now

    def _fresh(self, stamp, now, label):
        stamp = _number(stamp, label)
        if stamp > now+1e-9 or now-stamp > self.FRESH_AGE+1e-9:
            raise ValueError(label+' is future or stale')
        return stamp

    def _fence(self, execution, stamp):
        previous = self._items[execution['item_id']]['last_evidence_at']
        if previous is not None and stamp <= previous:
            raise ValueError('evidence is reordered or an altered duplicate sample')
        retained = execution['retained_at']
        if retained is not None and stamp <= retained:
            raise ValueError('recovery needs observations after the retained failure/cancellation')

    def _workflow(self, execution, proof):
        evidence = _mapping(proof.get('evidence'), 'workflow evidence')
        if evidence.get('source') != 'observations' or evidence.get('workflow_version') != TransportWorkflow.VERSION:
            raise ValueError('identified TransportWorkflow observation evidence required')
        carrier, receiver = proof.get('carrier_id'), proof.get('receiver_id')
        participants = set(execution['participants'].values())
        if (not isinstance(carrier, str) or not isinstance(receiver, str)
                or carrier not in participants or receiver not in participants or carrier == receiver):
            raise ValueError('workflow carrier/receiver must be distinct reserved participants')
        for role, rid in (('carrier', carrier), ('receiver', receiver)):
            if role in execution['participants'] and execution['participants'][role] != rid:
                raise ValueError('workflow does not match reserved '+role+' role')
        if evidence.get('carrier_id') != carrier:
            raise ValueError('carrier evidence identity mismatch')
        intent = _mapping(proof.get('resource_intent'), 'resource_intent')
        if not isinstance(intent.get('retain'), list) or 'item:'+execution['item_id'] not in intent['retain'] or intent.get('release') != []:
            raise ValueError('workflow must retain the item and request no implicit release')
        return evidence, intent

    @staticmethod
    def _event(evidence, name, at_most):
        events = evidence.get('events')
        if not isinstance(events, list):
            raise ValueError('workflow event history is missing')
        matching = [row for row in events if isinstance(row, Mapping) and row.get('event')==name]
        if not matching or not any(_number(row.get('sampled_at'), name+' sample') <= at_most+1e-9 for row in matching):
            raise ValueError(name+' observed event is missing or future')

    def _accept(self, execution, key, operation, now, stamp):
        item = self._items[execution['item_id']]
        item['last_evidence_at'] = stamp
        execution['last_action_at'] = now
        self._proof_uses[key] = dict(execution_id=execution['execution_id'], operation=operation, version=item['version'])
        return self._receipt(execution, action=operation[0], applied_version=item['version'])

    def _loading_workflow(self, execution, proof, action, now):
        evidence = _mapping(proof.get('evidence'), 'loading evidence')
        if evidence.get('source') != 'observations' or evidence.get('workflow_version') != LoadingWorkflow.VERSION:
            raise ValueError('identified LoadingWorkflow observation evidence required')
        donor, carrier = proof.get('donor_id'), proof.get('carrier_id')
        participants = execution['participants']
        if (not isinstance(donor, str) or not isinstance(carrier, str) or donor == carrier
                or donor not in participants.values() or carrier not in participants.values()):
            raise ValueError('loading donor/carrier must be distinct reserved participants')
        if (participants.get('carrier') != carrier
                or not any(participants.get(role) == donor for role in ('donor', 'loader'))):
            raise ValueError('loading requires explicitly reserved donor/loader and carrier roles')
        for role, rid in (('donor', donor), ('loader', donor), ('carrier', carrier)):
            if role in participants and participants[role] != rid:
                raise ValueError('loading workflow does not match reserved '+role+' role')
        identity = dict(task_id=execution['task_id'], item_id=execution['item_id'], donor_id=donor, carrier_id=carrier)
        if any(evidence.get(key) != value for key, value in identity.items()):
            raise ValueError('loading evidence identity mismatch')
        intent = _mapping(proof.get('resource_intent'), 'resource_intent')
        retained = intent.get('retain')
        if not isinstance(retained, list) or 'item:'+execution['item_id'] not in retained or intent.get('release') != []:
            raise ValueError('loading must retain the item and request no implicit release')
        proposal = _mapping(intent.get(action), action)
        measured = _mapping(evidence.get('donor_grip' if action == 'donor_custody' else 'loaded'), action+' observations')
        for row in (proposal, measured):
            if any(row.get(key) != value for key, value in identity.items()):
                raise ValueError('loading proposal or observation identity mismatch')
        if (measured.get('source') != 'observations' or measured.get('workflow_version') != LoadingWorkflow.VERSION
                or (action == 'donor_custody' and measured.get('robot_id') != donor)):
            raise ValueError('identified donor loading observations required')
        donor_stamp = self._fresh(evidence.get('donor_sampled_at'), now, 'donor sample')
        carrier_stamp = self._fresh(evidence.get('carrier_sampled_at'), now, 'carrier sample')
        if abs(donor_stamp-carrier_stamp) > LoadingWorkflow.PEER_SKEW+1e-9:
            raise ValueError('loading peer observations are not synchronized')
        stamp = min(donor_stamp, carrier_stamp)
        for row in (proposal, measured):
            for field, expected in (('donor_sampled_at', donor_stamp), ('carrier_sampled_at', carrier_stamp),
                                    ('confirmed_at', stamp)):
                if self._fresh(row.get(field), now, field) != expected:
                    raise ValueError('loading proposal and observation timestamps mismatch')
        if self._fresh(measured.get('sampled_at'), now, 'loading confirmation sample') != stamp:
            raise ValueError('loading confirmation must match the current peer samples')
        return evidence, proposal, measured, (donor_stamp, carrier_stamp)

    @staticmethod
    def _loading_dwell(measured, stamp, minimum):
        since = _number(measured.get('stable_since'), 'stable since')
        duration = _number(measured.get('stable_duration_s'), 'stable duration')
        declared = _number(measured.get('minimum_stable_duration_s'), 'minimum stable duration')
        if (since > stamp or declared != minimum or duration < minimum-1e-9
                or not math.isclose(duration, stamp-since, abs_tol=1e-9)):
            raise ValueError('observed loading stability dwell is incomplete or inconsistent')

    def _loading_fence(self, execution, samples):
        self._fence(execution, min(samples))
        previous = execution.get('loading_samples')
        if previous is not None and any(current <= old for current, old in zip(samples, previous)):
            raise ValueError('loading participant evidence is reordered or an altered duplicate sample')

    def observe_donor_custody(self, execution_id, item_id, owner, evidence, *, now):
        """Record an initially unowned item only after an observed donor grasp/lift."""
        _id(owner, 'owner');_number(now, 'now')
        operation = ('observe_donor_custody', item_id, owner)
        with self._lock:
            execution = self._execution(execution_id, item_id)
            key = self._bound(execution, item_id, evidence)
            replay = self._replay(execution, key, operation)
            if replay is not None:return replay
            now = self._now(execution, now)
            if execution['status'] != 'active':raise ResourceConflict('execution is retained or closed')
            observed, proposal, measured, samples = self._loading_workflow(execution, evidence, 'donor_custody', now)
            if (evidence.get('donor_id') != owner or evidence.get('status') != 'running'
                    or 'from_robot' not in proposal or proposal['from_robot'] is not None or proposal.get('to_robot') != owner):
                raise ValueError('running donor custody proposal required')
            if (measured.get('bilateral_contact') is not True or measured.get('finger_contacts') != ['left', 'right']
                    or measured.get('lifted') is not True or observed.get('donor_released') is not False
                    or observed.get('carrier_released') is not True):
                raise ValueError('current donor bilateral contact and lifted item evidence required')
            source = _vector(measured.get('source_item_position'), 'source item position')
            current = _vector(measured.get('item_position'), 'item position')
            lift = _number(measured.get('lift_height_m'), 'lift height')
            speed = _number(measured.get('item_speed_m_s'), 'item speed')
            error = _number(measured.get('tool_error_m'), 'tool error')
            if (measured.get('minimum_lift_height_m') != LoadingWorkflow.DONOR_LIFT_MIN or lift < LoadingWorkflow.DONOR_LIFT_MIN-1e-9
                    or not math.isclose(lift, current[2]-source[2], abs_tol=1e-9)
                    or measured.get('maximum_item_speed_m_s') != LoadingWorkflow.DONOR_SETTLED_SPEED or speed > LoadingWorkflow.DONOR_SETTLED_SPEED+1e-9
                    or measured.get('maximum_tool_error_m') != LoadingWorkflow.DONOR_TOOL_TOLERANCE or error > LoadingWorkflow.DONOR_TOOL_TOLERANCE+1e-9):
                raise ValueError('verified donor lift and settled grasp evidence required')
            self._loading_dwell(measured, min(samples), LoadingWorkflow.DONOR_DWELL)
            self._event(observed, 'donor_grip_verified', min(samples))
            self._loading_fence(execution, samples)
            item = self._items[item_id]
            if item['owner'] not in (None, owner):raise ResourceConflict('item already has another observed owner')
            if item['owner'] is None:item.update(owner=owner, version=item['version']+1)
            execution['loading_samples'] = samples
            return self._accept(execution, key, operation, now, min(samples))

    def commit_loading_transfer(self, execution_id, item_id, expected_owner, new_owner, now, proof, *, expected_version=None):
        """CAS donor to carrier after observed support, release, and clearance."""
        _id(expected_owner, 'expected_owner');_id(new_owner, 'new_owner');_number(now, 'now')
        if expected_owner == new_owner:raise ValueError('loading requires distinct owners')
        if expected_version is not None and (type(expected_version) is not int or expected_version < 0):
            raise ValueError('expected_version must be a nonnegative integer')
        operation = ('commit_loading_transfer', item_id, expected_owner, new_owner)
        with self._lock:
            execution = self._execution(execution_id, item_id)
            key = self._bound(execution, item_id, proof)
            replay = self._replay(execution, key, operation)
            if replay is not None:return replay
            now = self._now(execution, now)
            if execution['status'] != 'active':raise ResourceConflict('execution is retained or closed')
            observed, proposal, measured, samples = self._loading_workflow(execution, proof, 'loading_commit', now)
            if (proof.get('donor_id') != expected_owner or proof.get('carrier_id') != new_owner
                    or proposal.get('from_robot') != expected_owner or proposal.get('to_robot') != new_owner
                    or proof.get('status') != 'completed' or proof.get('phase') != 'loaded'
                    or proof.get('code') != 'loading_verified'):
                raise ValueError('completed physical donor-to-carrier loading required')
            for row in (observed, measured):
                if (row.get('supported') is not True or row.get('donor_released') is not True
                        or row.get('carrier_released') is not True or row.get('donor_contact') is not False):
                    raise ValueError('carrier support and fully released donor observations required')
            if (measured.get('donor_bilateral_contact') is not False or measured.get('carrier_bilateral_contact') is not False
                    or measured.get('donor_finger_contacts') != [] or measured.get('carrier_finger_contacts') != []
                    or measured.get('footprint_inside') is not True or measured.get('height_good') is not True):
                raise ValueError('released fingers and supported footprint evidence required')
            geom = measured.get('support_geom')
            if not isinstance(geom, str) or not geom.startswith(new_owner+'/'):
                raise ValueError('support geometry must belong to the carrier')
            mass = _number(measured.get('item_mass_kg'), 'item mass')
            minimum = _number(measured.get('minimum_support_force_N'), 'minimum support force')
            upward = _number(measured.get('upward_support_force_N'), 'upward support force')
            relative = _number(measured.get('item_relative_speed'), 'item relative speed')
            height = _number(measured.get('height_error_m'), 'support height error')
            retreat = _number(measured.get('retreat_error_m'), 'retreat error')
            target = _vector(measured.get('retreat_target'), 'retreat target')
            tool = _vector(measured.get('donor_tool_position'), 'donor tool position')
            if (mass <= 0 or not math.isclose(minimum, LoadingWorkflow.SUPPORT_FRACTION*mass*9.81, abs_tol=1e-9)
                    or upward < minimum or measured.get('maximum_relative_speed') != LoadingWorkflow.MAX_RELATIVE_SPEED or relative > LoadingWorkflow.MAX_RELATIVE_SPEED+1e-9
                    or measured.get('maximum_height_error_m') != LoadingWorkflow.MAX_HEIGHT_ERROR or height > LoadingWorkflow.MAX_HEIGHT_ERROR+1e-9
                    or measured.get('maximum_retreat_error_m') != LoadingWorkflow.RETREAT_TOLERANCE or retreat > LoadingWorkflow.RETREAT_TOLERANCE+1e-9
                    or not math.isclose(retreat, math.dist(target, tool), abs_tol=1e-9)):
                raise ValueError('stable carrier support and observed donor retreat required')
            for field in ('upward_support_force_N', 'minimum_support_force_N', 'item_relative_speed'):
                if observed.get(field) != measured[field]:
                    raise ValueError('loading summary and support evidence mismatch')
            self._loading_dwell(measured, min(samples), LoadingWorkflow.CLEARANCE_DWELL)
            report = _mapping(proof.get('report'), 'loading report')
            expected = dict(task_id=execution['task_id'], item_id=item_id, donor_id=expected_owner,
                            carrier_id=new_owner, state='loaded', sampled_at=min(samples))
            if any(report.get(field) != value for field, value in expected.items()):
                raise ValueError('loading report identity or timestamp mismatch')
            self._event(observed, 'loading_verified', min(samples))
            self._loading_fence(execution, samples)
            item = self._items[item_id]
            if item['owner'] != expected_owner or (expected_version is not None and item['version'] != expected_version):
                raise ResourceConflict('custody compare-and-swap owner/version mismatch')
            item.update(owner=new_owner, version=item['version']+1)
            execution['loading_samples'] = samples
            return self._accept(execution, key, operation, now, min(samples))

    def observe_custody(self, execution_id, item_id, owner, evidence, *, now):
        _id(owner, 'owner');_number(now, 'now')
        operation = ('observe_custody', item_id, owner)
        with self._lock:
            execution = self._execution(execution_id, item_id)
            key = self._bound(execution, item_id, evidence)
            replay = self._replay(execution, key, operation)
            if replay is not None:return replay
            now = self._now(execution, now)
            if execution['status'] != 'active':raise ResourceConflict('execution is retained or closed')
            measured, _ = self._workflow(execution, evidence)
            if evidence.get('carrier_id') != owner or evidence.get('status') != 'running' or evidence.get('supported') is not True:
                raise ValueError('fresh supported carrier result required')
            stamp = self._fresh(measured.get('sampled_at'), now, 'carrier sample')
            minimum = _number(measured.get('minimum_support_force_N'), 'minimum support force')
            upward = _number(measured.get('upward_support_force_N'), 'upward support force')
            relative = _number(measured.get('item_relative_speed'), 'item relative speed')
            if minimum<=0 or upward<minimum or relative>TransportWorkflow.RELATIVE_SPEED or measured.get('carrier_item_contact') is not True:
                raise ValueError('upward support and settled item evidence required')
            self._event(measured, 'load_supported', stamp)
            self._fence(execution, stamp)
            item = self._items[item_id]
            if item['owner'] is None and any(role in execution['participants'] for role in ('donor', 'loader')):
                raise ResourceConflict('reserved donor requires initial donor custody and an explicit loading transfer')
            if item['owner'] not in (None, owner):raise ResourceConflict('item already has another observed owner')
            if item['owner'] is None:item.update(owner=owner, version=item['version']+1)
            return self._accept(execution, key, operation, now, stamp)

    def commit_transfer(self, execution_id, item_id, expected_owner, new_owner, now, proof, *, expected_version=None):
        _id(expected_owner, 'expected_owner');_id(new_owner, 'new_owner');_number(now, 'now')
        if expected_owner == new_owner:raise ValueError('handoff requires distinct owners')
        if expected_version is not None and (type(expected_version) is not int or expected_version<0):
            raise ValueError('expected_version must be a nonnegative integer')
        operation = ('commit_transfer', item_id, expected_owner, new_owner)
        with self._lock:
            execution = self._execution(execution_id, item_id)
            key = self._bound(execution, item_id, proof)
            replay = self._replay(execution, key, operation)
            if replay is not None:return replay
            now = self._now(execution, now)
            if execution['status'] != 'active':raise ResourceConflict('execution is retained or closed')
            evidence, intent = self._workflow(execution, proof)
            proposal = _mapping(intent.get('handoff_commit'), 'handoff_commit')
            expected = dict(task_id=execution['task_id'], item_id=item_id, from_robot=expected_owner, to_robot=new_owner)
            if any(proposal.get(key)!=value for key,value in expected.items()):
                raise ValueError('handoff proposal identity mismatch')
            if (proof.get('carrier_id')!=expected_owner or proof.get('receiver_id')!=new_owner
                    or proof.get('status')!='completed' or proof.get('code')!='handoff_verified'
                    or proof.get('phase')!='confirm_handoff' or proof.get('supported') is not False):
                raise ValueError('completed physical handoff workflow required')
            carrier = self._fresh(proposal.get('carrier_sampled_at'), now, 'carrier sample')
            receiver = self._fresh(proposal.get('receiver_sampled_at'), now, 'receiver sample')
            ack = self._fresh(proposal.get('receiver_ack_at'), now, 'receiver acknowledgement')
            separated = _number(proposal.get('separated_at'), 'separation time')
            if abs(carrier-receiver)>self.MAX_PEER_SKEW+1e-9 or not separated<ack<=receiver+1e-9 or separated>carrier+1e-9:
                raise ValueError('fresh peer samples and a post-separation acknowledgement required')
            self._fresh(evidence.get('sampled_at'), now, 'carrier evidence sample')
            self._fresh(evidence.get('receiver_sampled_at'), now, 'receiver evidence sample')
            if (evidence.get('sampled_at')!=carrier or evidence.get('receiver_sampled_at')!=receiver
                    or evidence.get('carrier_item_contact') is not False or evidence.get('receiver_bilateral_contact') is not True):
                raise ValueError('matching released sender and bilateral receiver evidence required')
            sender = _mapping(evidence.get('sender_confirmation'), 'sender_confirmation')
            receiver_ack = _mapping(evidence.get('receiver_confirmation'), 'receiver_confirmation')
            self._fresh(sender.get('sampled_at'), now, 'sender confirmation sample')
            self._fresh(receiver_ack.get('sampled_at'), now, 'receiver confirmation sample')
            sender_expected = dict(task_id=execution['task_id'], item_id=item_id, robot_id=expected_owner,
                                   receiver_id=new_owner, state='observed_released', sampled_at=carrier)
            ack_expected = dict(task_id=execution['task_id'], item_id=item_id, carrier_id=expected_owner,
                                state='received', sampled_at=ack)
            if any(sender.get(key)!=value for key,value in sender_expected.items()) or any(receiver_ack.get(key)!=value for key,value in ack_expected.items()):
                raise ValueError('sender/receiver confirmation identity or timestamps mismatch')
            self._event(evidence, 'physical_separation_confirmed', separated)
            self._event(evidence, 'handoff_verified', carrier)
            self._fence(execution, min(carrier, receiver))
            item = self._items[item_id]
            if item['owner']!=expected_owner or (expected_version is not None and item['version']!=expected_version):
                raise ResourceConflict('custody compare-and-swap owner/version mismatch')
            item.update(owner=new_owner, version=item['version']+1)
            return self._accept(execution, key, operation, now, min(carrier, receiver))

    def begin_recovery(self, execution_id, recovery_id, actor_id, now, *, expected_version):
        """Authorize one recovery attempt without releasing leases or moving custody."""
        _id(recovery_id, 'recovery_id');_id(actor_id, 'actor_id');_number(now, 'now')
        if type(expected_version) is not int or expected_version < 0:
            raise ValueError('expected_version must be a nonnegative integer')
        identity = (execution_id, actor_id, expected_version)
        with self._lock:
            execution = self._execution(execution_id)
            current = execution.get('recovery')
            previous = self._recovery_requests.get(recovery_id)
            if previous is not None:
                if previous != identity:
                    raise ResourceConflict('recovery id already identifies another attempt')
                if not current or current['recovery_id'] != recovery_id:
                    raise ResourceConflict('retired recovery id cannot restart or control another attempt')
                return self._receipt(execution, idempotent=True, action='begin_recovery')
            if execution['status'] not in ('failed', 'cancelled'):
                raise ResourceConflict('recovery requires a retained failed or cancelled execution')
            if actor_id not in execution['participants'].values():
                raise ValueError('recovery actor must be a reserved participant')
            now = self._now(execution, now)
            if self._items[execution['item_id']]['version'] != expected_version:
                raise ResourceConflict('recovery custody version mismatch')
            if any(self._resource_owners.get(resource) != execution_id for resource in execution['bundle']):
                raise ResourceConflict('recovery requires the entire retained resource bundle')
            recovery = dict(recovery_id=recovery_id, actor_id=actor_id, status='recovering',
                started_at=now, expected_version=expected_version, reason=None)
            execution.setdefault('terminal_status', execution['status'])
            execution.setdefault('terminal_reason', execution['reason'])
            execution.update(status='recovering', recovery=recovery, last_action_at=now)
            self._recovery_requests[recovery_id] = identity
            return self._receipt(execution, action='begin_recovery')

    @staticmethod
    def _recovery_attempt(execution, recovery_id, actor_id=None):
        _id(recovery_id, 'recovery_id')
        recovery = execution.get('recovery')
        if recovery is None or recovery['recovery_id'] != recovery_id:
            raise ResourceConflict('unknown or retired recovery id')
        if actor_id is not None and recovery['actor_id'] != actor_id:
            raise ValueError('recovery actor identity mismatch')
        return recovery

    def _end_recovery(self, execution_id, recovery_id, reason, now, *, cancelled):
        _id(reason, 'reason');_number(now, 'now')
        with self._lock:
            execution = self._execution(execution_id)
            recovery = self._recovery_attempt(execution, recovery_id)
            action = 'cancel_recovery' if cancelled else 'fail_recovery'
            if recovery['status'] in ('failed', 'cancelled'):
                return self._receipt(execution, idempotent=True, action=action)
            if execution['status'] != 'recovering':
                raise ResourceConflict('recovery is already closed')
            now = self._now(execution, now)
            recovery.update(status='cancelled' if cancelled else 'failed', reason=reason, ended_at=now)
            execution.update(status='failed', reason=reason, retained_at=now, last_action_at=now)
            return self._receipt(execution, action=action)

    def fail_recovery(self, execution_id, recovery_id, reason='recovery_failed', *, now):
        return self._end_recovery(execution_id, recovery_id, reason, now, cancelled=False)

    def cancel_recovery(self, execution_id, recovery_id, reason='recovery_cancelled', *, now):
        return self._end_recovery(execution_id, recovery_id, reason, now, cancelled=True)

    @staticmethod
    def _recovery_contacts(rows, item_id):
        if not isinstance(rows, list):
            raise ValueError('raw recovery contact wrench observations are required')
        contacts = []
        item_geom = item_id+'/shape'
        for row in rows:
            _mapping(row, 'contact wrench')
            a, b = row.get('geom_a'), row.get('geom_b')
            if a == b or item_geom not in (a, b):
                raise ValueError('recovery contact does not identify this item')
            other = a if b == item_geom else b
            _id(other, 'contact geometry')
            force = _number(row.get('force'), 'contact force')
            vector = _vector(row.get('force_on_b_world'), 'contact force vector')
            _vector(row.get('position'), 'contact position')
            if force > .1 and math.sqrt(sum(x*x for x in vector)) <= .1:
                raise ValueError('nonzero recovery contact requires a nonzero force vector')
            contacts.append((other, force))
        return contacts

    def observe_recovery_custody(self, execution_id, item_id, expected_owner, actor_id, now, proof,
                                 *, recovery_id, expected_version):
        """CAS custody using current raw grasp contacts from a recovery workflow."""
        from .recovery_workflow import RecoveryPlacement

        _id(actor_id, 'actor_id');_number(now, 'now')
        _mapping(proof, 'recovery proof')
        if expected_owner is not None:_id(expected_owner, 'expected_owner')
        if type(expected_version) is not int or expected_version < 0:
            raise ValueError('expected_version must be a nonnegative integer')
        operation = ('observe_recovery_custody', item_id, recovery_id, expected_owner, actor_id)
        with self._lock:
            execution = self._execution(execution_id, item_id)
            attempt = self._recovery_attempt(execution, recovery_id, actor_id)
            if proof.get('recovery_id') != recovery_id:
                raise ValueError('recovery evidence request identity mismatch')
            key = self._bound(execution, item_id, proof)
            replay = self._replay(execution, key, operation)
            if replay is not None:return replay
            now = self._now(execution, now)
            if execution['status'] != 'recovering' or attempt['status'] != 'recovering':
                raise ResourceConflict('custody observations require the current active recovery')
            observed = _mapping(proof.get('evidence'), 'recovery evidence')
            measured = _mapping(observed.get('grasp_verified'), 'recovery grasp evidence')
            intent = _mapping(proof.get('resource_intent'), 'resource_intent')
            proposal = _mapping(intent.get('recovery_custody'), 'recovery custody proposal')
            carrier = proof.get('carrier_id')
            if (not isinstance(carrier, str) or execution['participants'].get('carrier') != carrier
                    or carrier == actor_id or proof.get('actor_id') != actor_id):
                raise ValueError('recovery actor and reserved carrier identities must match')
            identity = dict(task_id=execution['task_id'], item_id=item_id, actor_id=actor_id, carrier_id=carrier)
            for row in (observed, measured, proposal):
                if any(row.get(k) != v for k, v in identity.items()):
                    raise ValueError('recovery observation or proposal identity mismatch')
            for row in (observed, measured):
                if row.get('source') != 'observations' or row.get('workflow_version') != RecoveryPlacement.VERSION:
                    raise ValueError('identified RecoveryPlacement observation evidence required')
            retained = intent.get('retain')
            if not isinstance(retained, list) or 'item:'+item_id not in retained or intent.get('release') != []:
                raise ValueError('recovery custody must retain the item and all leases')
            mode = proof.get('mode')
            if (proof.get('status') != 'running' or mode not in ('held', 'pickup')
                    or observed.get('mode') != mode or measured.get('mode') != mode or proposal.get('to_robot') != actor_id
                    or measured.get('robot_id') != actor_id):
                raise ValueError('current identified recovery grasp proposal required')
            if (mode == 'held' and expected_owner not in (None, actor_id)) or (mode == 'pickup' and expected_owner != carrier):
                raise ResourceConflict('recovery mode does not match current source ownership')
            samples = tuple(self._fresh(observed.get(name), now, name)
                            for name in ('actor_sampled_at', 'carrier_sampled_at'))
            stamp = min(samples)
            if abs(samples[0]-samples[1]) > RecoveryPlacement.MAX_PEER_SKEW+1e-9:
                raise ValueError('recovery peer observations are not synchronized')
            for row in (measured, proposal):
                for field, expected in (('actor_sampled_at', samples[0]), ('carrier_sampled_at', samples[1]), ('confirmed_at', stamp)):
                    if self._fresh(row.get(field), now, field) != expected:
                        raise ValueError('recovery confirmation timestamps mismatch')
            if self._fresh(measured.get('sampled_at'), now, 'grasp sample') != stamp:
                raise ValueError('recovery grasp sample must match the current peer observations')
            if stamp <= attempt['started_at']:
                raise ValueError('recovery needs observations after this recovery request')
            previous = attempt.get('samples')
            if previous is not None and any(a <= b for a, b in zip(samples, previous)):
                raise ValueError('recovery participant evidence is reordered or an altered duplicate sample')
            self._fence(execution, stamp)
            if (measured.get('bilateral_contact') is not True or measured.get('finger_contacts') != ['left', 'right']
                    or measured.get('source_separated') is not True or measured.get('carrier_contact') is not False
                    or measured.get('external_contact') is not False):
                raise ValueError('bilateral grasp and physical source separation are required')
            contacts = self._recovery_contacts(measured.get('item_contact_wrenches'), item_id)
            carrier_contacts = self._recovery_contacts(measured.get('carrier_contact_wrenches'), item_id)
            expected_fingers = {actor_id+'/finger-shape-left', actor_id+'/finger-shape-right'}
            touched = {geom for geom, force in contacts if force > .1}
            if not expected_fingers <= touched:
                raise ValueError('both actual actor finger contact wrenches are required')
            if (any(not geom.startswith(actor_id+'/') and force > .1 for geom, force in contacts)
                    or any(geom.startswith(carrier+'/') and force > .1 for geom, force in carrier_contacts)):
                raise ValueError('raw contacts still show external or carrier support')
            speed = _number(measured.get('item_speed_m_s'), 'item speed')
            tool_error = _number(measured.get('tool_error_m'), 'tool error')
            tool = _vector(measured.get('tool_position'), 'tool position')
            target = _vector(measured.get('tool_target'), 'tool target')
            _vector(measured.get('item_position'), 'item position')
            if (measured.get('maximum_item_speed_m_s') != RecoveryPlacement.SETTLED_SPEED or speed > RecoveryPlacement.SETTLED_SPEED+1e-9
                    or measured.get('maximum_tool_error_m') != RecoveryPlacement.TOOL_TOLERANCE or tool_error > RecoveryPlacement.TOOL_TOLERANCE+1e-9
                    or not math.isclose(tool_error, math.dist(tool, target), abs_tol=1e-9)):
                raise ValueError('observed recovery grasp must be settled')
            self._loading_dwell(measured, stamp, RecoveryPlacement.GRASP_DWELL)
            if mode == 'held':
                if measured.get('already_held') is not True:
                    raise ValueError('held recovery must explicitly observe the existing grasp')
            else:
                source = _vector(measured.get('source_item_position'), 'source item position')
                item_position = _vector(measured.get('item_position'), 'item position')
                lift = _number(measured.get('lift_height_m'), 'lift height')
                if (measured.get('lifted') is not True or measured.get('already_held') is not False
                        or measured.get('minimum_lift_height_m') != RecoveryPlacement.MIN_LIFT or lift < RecoveryPlacement.MIN_LIFT-1e-9
                        or not math.isclose(lift, item_position[2]-source[2], abs_tol=1e-9)):
                    raise ValueError('pickup recovery needs the observed lift from its source')
            item = self._items[item_id]
            if item['owner'] != expected_owner or item['version'] != expected_version:
                raise ResourceConflict('recovery custody compare-and-swap owner/version mismatch')
            if item['owner'] != actor_id:item.update(owner=actor_id, version=item['version']+1)
            attempt.update(samples=samples, custody_version=item['version'])
            return self._accept(execution, key, operation, now, stamp)

    def _retain(self, execution_id, status, reason, now):
        _id(reason, 'reason')
        with self._lock:
            execution = self._execution(execution_id)
            if execution['status'] in ('released', 'recovered'):raise ResourceConflict('execution is already closed')
            if execution['status'] == 'recovering':
                raise ResourceConflict('recovery failure/cancellation requires the current recovery id')
            if execution['status'] in ('failed', 'cancelled'):
                return self._receipt(execution, idempotent=True, action=status)
            stamp = execution['last_action_at'] if now is None else self._now(execution, now)
            execution.setdefault('terminal_status', status)
            execution.setdefault('terminal_reason', reason)
            execution.update(status=status, reason=reason, retained_at=stamp, last_action_at=stamp)
            return self._receipt(execution, action=status)

    def fail(self, execution_id, reason='cooperative_operation_failed', *, now=None):
        return self._retain(execution_id, 'failed', reason, now)

    def cancel(self, execution_id, reason='operator_cancelled', *, now=None):
        return self._retain(execution_id, 'cancelled', reason, now)

    def _finish(self, execution_id, now, evidence, recovery):
        _number(now, 'now')
        action = 'recover' if recovery else 'release'
        with self._lock:
            execution = self._execution(execution_id)
            item_id = execution['item_id'];operation = (action, item_id)
            key = self._bound(execution, item_id, evidence)
            attempt = None
            if recovery and execution.get('recovery') is not None:
                attempt = self._recovery_attempt(execution, evidence.get('recovery_id'), evidence.get('actor_id'))
                if evidence.get('actor_id') != attempt['actor_id']:
                    raise ValueError('recovery actor identity is required')
                operation = (action, item_id, attempt['recovery_id'])
            replay = self._replay(execution, key, operation)
            if replay is not None:return replay
            now = self._now(execution, now)
            allowed = (('recovering',) if attempt is not None else ('failed', 'cancelled')) if recovery else ('active',)
            if execution['status'] not in allowed:raise ResourceConflict('explicit '+action+' is invalid for this execution status')
            placement = _mapping(evidence.get('placement'), 'placement')
            peers = _mapping(evidence.get('participants'), 'participant release observations')
            if evidence.get('source')!='observations' or evidence.get('final_placed') is not True:
                raise ValueError('observed final placement required; success claims cannot release resources')
            if (placement.get('item_id')!=item_id or placement.get('support_confirmed') is not True
                    or placement.get('stable') is not True or placement.get('holders')!=[]):
                raise ValueError('stable supported final placement and no holders required')
            if set(peers)!=set(execution['participants'].values()):
                raise ValueError('fresh no-holder observations required from every reserved participant')
            stamps = [self._fresh(placement.get('sampled_at'), now, 'placement sample')]
            for rid, observation in peers.items():
                _mapping(observation, 'participant observation')
                if observation.get('robot_id')!=rid or observation.get('item_id')!=item_id or observation.get('holding') is not False:
                    raise ValueError('participant identity or no-holder observation mismatch')
                stamps.append(self._fresh(observation.get('sampled_at'), now, rid+' sample'))
            if max(stamps)-min(stamps)>self.MAX_PEER_SKEW+1e-9:
                raise ValueError('placement and participant observations are not synchronized')
            if attempt is not None and attempt.get('samples') is not None:
                for rid, previous in zip((attempt['actor_id'], execution['participants']['carrier']), attempt['samples']):
                    if peers[rid]['sampled_at'] <= previous:
                        raise ValueError('recovery final participant observation is reordered or duplicated')
            self._fence(execution, min(stamps))
            if attempt is not None and min(stamps) <= attempt['started_at']:
                raise ValueError('recovery completion needs observations after this recovery request')
            item = self._items[item_id]
            if item['owner'] is not None:item.update(owner=None, version=item['version']+1)
            for resource in execution['bundle']:
                del self._resource_owners[resource]
            execution.update(status='recovered' if recovery else 'released', reason='observed_final_placement_no_holders')
            if attempt is not None:
                attempt.update(status='recovered', ended_at=now, reason='observed_final_placement_no_holders')
            return self._accept(execution, key, operation, now, min(stamps))

    def release(self, execution_id, now, evidence):
        return self._finish(execution_id, now, evidence, recovery=False)

    def recover(self, execution_id, now, evidence):
        return self._finish(execution_id, now, evidence, recovery=True)

    def snapshot(self):
        with self._lock:
            return deepcopy(dict(version=self.VERSION,
                executions={eid:self._receipt(execution) for eid,execution in self._executions.items()},
                resource_owners=self._resource_owners, items=self._items))
