"use client";

import { useState, useEffect } from "react";
import {
  MessageSquare, ThumbsUp, ThumbsDown, Send, Loader2,
  ChevronDown, Pencil, Trash2, X, Check,
  Lock, Reply,
} from "lucide-react";
import { formatRelativeTime } from "@/lib/utils";
import type { Comment } from "@/types/service";

interface CommentSectionProps {
  serviceId: string;
  initialComments: Comment[];
  initialTotal: number;
}

// ─── Comment Form ───
interface CommentFormProps {
  serviceId: string;
  parentId?: string;
  replyToName?: string;
  onSubmitted: (comment: Comment) => void;
  onCancel?: () => void;
  compact?: boolean;
}

function CommentForm({ serviceId, parentId, replyToName, onSubmitted, onCancel, compact }: CommentFormProps) {
  const [nickname, setNickname] = useState("");
  const [password, setPassword] = useState("");
  const [content, setContent] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const saved = localStorage.getItem("aihub_nickname");
    if (saved) setNickname(saved);
    const savedPw = localStorage.getItem("aihub_comment_pw");
    if (savedPw) setPassword(savedPw);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    if (!nickname.trim() || !content.trim() || !password.trim()) {
      setError("닉네임, 비밀번호, 댓글 내용을 모두 입력해주세요.");
      return;
    }

    setSubmitting(true);
    try {
      const res = await fetch("/api/comments", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          serviceId,
          content: content.trim(),
          authorName: nickname.trim(),
          password: password.trim(),
          parentId: parentId || undefined,
        }),
      });

      if (res.status === 429) {
        setError("잠시 후 다시 시도해주세요.");
        return;
      }

      if (!res.ok) {
        const data = await res.json();
        setError(data.error || "댓글 작성에 실패했습니다.");
        return;
      }

      const newComment = await res.json();
      onSubmitted(newComment);
      setContent("");
      localStorage.setItem("aihub_nickname", nickname.trim());
      localStorage.setItem("aihub_comment_pw", password.trim());
    } catch {
      setError("댓글 작성에 실패했습니다.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className={compact ? "mb-3" : "mb-8"}>
      <div className={`${compact ? "rounded-lg p-3 dark:bg-white/3 bg-black/3 border dark:border-white/5 border-black/5" : "glass rounded-xl p-4"}`}>
        {replyToName && (
          <div className="flex items-center gap-1.5 mb-2 text-xs dark:text-neon-blue text-blue-600">
            <Reply className="w-3 h-3" />
            <span className="font-medium">@{replyToName}</span>
            <span className="dark:text-zinc-500 text-zinc-400">에게 답글</span>
          </div>
        )}
        <div className="flex gap-2 mb-2 flex-wrap">
          <input
            type="text"
            value={nickname}
            onChange={(e) => setNickname(e.target.value)}
            placeholder="닉네임"
            maxLength={50}
            className={`${compact ? "w-24" : "w-32 sm:w-40"} px-3 py-2 rounded-lg text-sm bg-transparent
              dark:bg-white/5 bg-black/5
              dark:text-white text-zinc-900
              dark:placeholder-zinc-500 placeholder-zinc-400
              outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30`}
          />
          <div className="relative">
            <Lock className="absolute left-2.5 top-1/2 -translate-y-1/2 w-3 h-3 dark:text-zinc-500 text-zinc-400" />
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="비밀번호"
              maxLength={100}
              className={`${compact ? "w-24" : "w-28 sm:w-36"} pl-7 pr-3 py-2 rounded-lg text-sm bg-transparent
                dark:bg-white/5 bg-black/5
                dark:text-white text-zinc-900
                dark:placeholder-zinc-500 placeholder-zinc-400
                outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30`}
            />
          </div>
        </div>
        <div className="flex gap-2">
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder={parentId ? "답글을 작성해주세요..." : "댓글을 작성해주세요..."}
            maxLength={1000}
            rows={compact ? 2 : 3}
            className="flex-1 px-3 py-2 rounded-lg text-sm bg-transparent resize-none
              dark:bg-white/5 bg-black/5
              dark:text-white text-zinc-900
              dark:placeholder-zinc-500 placeholder-zinc-400
              outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30"
          />
        </div>
        <div className="flex items-center justify-between mt-2">
          <span className="text-xs dark:text-zinc-500 text-zinc-400">
            {content.length}/1000
          </span>
          <div className="flex items-center gap-2">
            <button
              type="submit"
              disabled={submitting || !nickname.trim() || !content.trim() || !password.trim()}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium
                bg-gradient-to-r from-neon-blue to-neon-purple text-white
                hover:opacity-90 transition-all duration-200
                disabled:opacity-40 disabled:cursor-not-allowed"
            >
              {submitting ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Send className="w-3.5 h-3.5" />}
              등록
            </button>
            {onCancel && (
              <button
                type="button"
                onClick={onCancel}
                className="px-3 py-1.5 rounded-lg text-xs font-medium
                  dark:text-zinc-400 text-zinc-500 hover:dark:text-zinc-300 hover:text-zinc-700 transition-colors"
              >
                취소
              </button>
            )}
          </div>
        </div>
        {error && (
          <p className="text-xs text-red-400 mt-1">{error}</p>
        )}
      </div>
    </form>
  );
}

// ─── Single Comment Item (flat — no nesting) ───
interface CommentItemProps {
  comment: Comment;
  serviceId: string;
  onDeleted: (commentId: string) => void;
  onUpdated: (comment: Comment) => void;
  onReply: (commentId: string, authorName: string) => void;
}

function CommentItem({ comment, serviceId, onDeleted, onUpdated, onReply }: CommentItemProps) {
  // Vote state
  const [likes, setLikes] = useState(comment.likes);
  const [dislikes, setDislikes] = useState(comment.dislikes);
  const [votedType, setVotedType] = useState<"like" | "dislike" | null>(null);

  // Edit/Delete state
  const [editing, setEditing] = useState(false);
  const [editContent, setEditContent] = useState(comment.content);
  const [editPassword, setEditPassword] = useState("");
  const [editError, setEditError] = useState("");
  const [editLoading, setEditLoading] = useState(false);

  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);
  const [deletePassword, setDeletePassword] = useState("");
  const [deleteError, setDeleteError] = useState("");
  const [deleteLoading, setDeleteLoading] = useState(false);

  const handleVote = async (type: "like" | "dislike") => {
    try {
      const res = await fetch("/api/comments/vote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ commentId: comment.id, type }),
      });
      const data = await res.json();
      if (res.ok) {
        setLikes(data.likes);
        setDislikes(data.dislikes);
        if (data.action === "cancelled") {
          setVotedType(null);
        } else {
          setVotedType(type);
        }
      }
    } catch {}
  };

  const handleEdit = async () => {
    if (!editPassword.trim() || !editContent.trim()) {
      setEditError("비밀번호와 내용을 입력해주세요.");
      return;
    }
    setEditLoading(true);
    setEditError("");
    try {
      const res = await fetch("/api/comments", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          commentId: comment.id,
          content: editContent.trim(),
          password: editPassword.trim(),
        }),
      });
      const data = await res.json();
      if (res.ok) {
        onUpdated(data);
        setEditing(false);
        setEditPassword("");
      } else {
        setEditError(data.error || "수정에 실패했습니다.");
      }
    } catch {
      setEditError("수정에 실패했습니다.");
    } finally {
      setEditLoading(false);
    }
  };

  const handleDelete = async () => {
    if (!deletePassword.trim()) {
      setDeleteError("비밀번호를 입력해주세요.");
      return;
    }
    setDeleteLoading(true);
    setDeleteError("");
    try {
      const res = await fetch("/api/comments", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          commentId: comment.id,
          password: deletePassword.trim(),
        }),
      });
      const data = await res.json();
      if (res.ok) {
        onDeleted(data.deletedId);
      } else {
        setDeleteError(data.error || "삭제에 실패했습니다.");
      }
    } catch {
      setDeleteError("삭제에 실패했습니다.");
    } finally {
      setDeleteLoading(false);
    }
  };

  const isReply = !!comment.parentId;

  return (
    <div className={isReply ? "ml-8" : ""}>
      <div className={`rounded-xl p-4 ${isReply
        ? "dark:bg-white/[0.02] bg-black/[0.02] border-l-2 dark:border-neon-blue/20 border-blue-200"
        : "dark:bg-white/5 bg-black/5"}`}
      >
        {/* Reply indicator — @닉네임 */}
        {isReply && comment.replyToAuthorName && (
          <div className="flex items-center gap-1.5 mb-1.5 text-xs">
            <Reply className="w-3 h-3 dark:text-neon-blue text-blue-500" />
            <span className="dark:text-neon-blue text-blue-600 font-medium">@{comment.replyToAuthorName}</span>
          </div>
        )}

        {/* Header */}
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          <span className="text-sm font-medium dark:text-white text-zinc-900">
            {comment.authorName}
          </span>
          <span className="text-xs dark:text-zinc-600 text-zinc-400">
            ({comment.maskedIp})
          </span>
        </div>
        <span className="text-xs dark:text-zinc-500 text-zinc-400">
          {formatRelativeTime(comment.createdAt)}
        </span>
      </div>

      {/* Content / Edit mode */}
      {editing ? (
        <div className="mb-3">
          <textarea
            value={editContent}
            onChange={(e) => setEditContent(e.target.value)}
            maxLength={1000}
            rows={3}
            className="w-full px-3 py-2 rounded-lg text-sm bg-transparent resize-none
              dark:bg-white/5 bg-black/5 dark:text-white text-zinc-900
              outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30"
          />
          <div className="flex items-center gap-2 mt-2">
            <div className="relative">
              <Lock className="absolute left-2 top-1/2 -translate-y-1/2 w-3 h-3 dark:text-zinc-500 text-zinc-400" />
              <input
                type="password"
                value={editPassword}
                onChange={(e) => setEditPassword(e.target.value)}
                placeholder="비밀번호 확인"
                className="w-28 pl-6 pr-2 py-1.5 rounded-lg text-xs bg-transparent
                  dark:bg-white/5 bg-black/5 dark:text-white text-zinc-900
                  dark:placeholder-zinc-500 placeholder-zinc-400
                  outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30"
              />
            </div>
            <button
              onClick={handleEdit}
              disabled={editLoading}
              className="flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-medium
                bg-gradient-to-r from-neon-blue to-neon-purple text-white
                hover:opacity-90 transition-all disabled:opacity-40"
            >
              {editLoading ? <Loader2 className="w-3 h-3 animate-spin" /> : <Check className="w-3 h-3" />}
              수정
            </button>
            <button
              onClick={() => { setEditing(false); setEditContent(comment.content); setEditError(""); }}
              className="flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs
                dark:text-zinc-400 text-zinc-500 hover:dark:text-zinc-300"
            >
              <X className="w-3 h-3" /> 취소
            </button>
          </div>
          {editError && <p className="text-xs text-red-400 mt-1">{editError}</p>}
        </div>
      ) : (
        <p className="text-sm dark:text-zinc-300 text-zinc-600 leading-relaxed mb-3 whitespace-pre-wrap">
          {comment.content}
        </p>
      )}

      {/* Delete confirm */}
      {showDeleteConfirm && (
        <div className="mb-3 p-3 rounded-lg dark:bg-red-500/10 bg-red-50 border dark:border-red-500/20 border-red-200">
          <p className="text-xs dark:text-red-300 text-red-600 mb-2">정말 삭제하시겠습니까?</p>
          <div className="flex items-center gap-2">
            <div className="relative">
              <Lock className="absolute left-2 top-1/2 -translate-y-1/2 w-3 h-3 dark:text-red-400 text-red-500" />
              <input
                type="password"
                value={deletePassword}
                onChange={(e) => setDeletePassword(e.target.value)}
                placeholder="비밀번호"
                className="w-28 pl-6 pr-2 py-1.5 rounded-lg text-xs bg-transparent
                  dark:bg-white/5 bg-black/5 dark:text-white text-zinc-900
                  dark:placeholder-zinc-500 placeholder-zinc-400
                  outline-none focus:ring-1 dark:focus:ring-red-500/50 focus:ring-red-500/30"
              />
            </div>
            <button
              onClick={handleDelete}
              disabled={deleteLoading}
              className="flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-medium
                bg-red-500 text-white hover:bg-red-600 transition-all disabled:opacity-40"
            >
              {deleteLoading ? <Loader2 className="w-3 h-3 animate-spin" /> : <Trash2 className="w-3 h-3" />}
              삭제
            </button>
            <button
              onClick={() => { setShowDeleteConfirm(false); setDeletePassword(""); setDeleteError(""); }}
              className="text-xs dark:text-zinc-400 text-zinc-500"
            >
              취소
            </button>
          </div>
          {deleteError && <p className="text-xs text-red-400 mt-1">{deleteError}</p>}
        </div>
      )}

      {/* Actions: vote, reply, edit, delete */}
      {!editing && !showDeleteConfirm && (
        <div className="flex items-center gap-3 flex-wrap">
          <button
            onClick={() => handleVote("like")}
            className={`flex items-center gap-1 text-xs transition-colors
              ${votedType === "like"
                ? "dark:text-neon-green text-emerald-600"
                : "dark:text-zinc-500 text-zinc-400 dark:hover:text-neon-green hover:text-emerald-600"
              }`}
          >
            <ThumbsUp className={`w-3.5 h-3.5 ${votedType === "like" ? "fill-current" : ""}`} />
            {likes > 0 && likes}
          </button>
          <button
            onClick={() => handleVote("dislike")}
            className={`flex items-center gap-1 text-xs transition-colors
              ${votedType === "dislike"
                ? "dark:text-pink-400 text-pink-600"
                : "dark:text-zinc-500 text-zinc-400 dark:hover:text-pink-400 hover:text-pink-600"
              }`}
          >
            <ThumbsDown className={`w-3.5 h-3.5 ${votedType === "dislike" ? "fill-current" : ""}`} />
            {dislikes > 0 && dislikes}
          </button>

          <button
            onClick={() => onReply(comment.id, comment.authorName)}
            className="flex items-center gap-1 text-xs dark:text-zinc-500 text-zinc-400
              dark:hover:text-neon-blue hover:text-neon-blue transition-colors"
          >
            <Reply className="w-3.5 h-3.5" />
            답글
          </button>

          <button
            onClick={() => setEditing(true)}
            className="flex items-center gap-1 text-xs dark:text-zinc-500 text-zinc-400
              dark:hover:text-zinc-300 hover:text-zinc-600 transition-colors"
          >
            <Pencil className="w-3 h-3" />
            수정
          </button>

          <button
            onClick={() => setShowDeleteConfirm(true)}
            className="flex items-center gap-1 text-xs dark:text-zinc-500 text-zinc-400
              dark:hover:text-red-400 hover:text-red-600 transition-colors"
          >
            <Trash2 className="w-3 h-3" />
            삭제
          </button>
        </div>
      )}
      </div>
    </div>
  );
}

// ─── Main CommentSection (flat layout) ───
export function CommentSection({ serviceId, initialComments, initialTotal }: CommentSectionProps) {
  const [comments, setComments] = useState<Comment[]>(initialComments);
  const [total, setTotal] = useState(initialTotal);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(initialTotal > 20);
  const [loadingMore, setLoadingMore] = useState(false);

  // Reply state — which comment are we replying to?
  const [replyTo, setReplyTo] = useState<{ commentId: string; authorName: string } | null>(null);

  const handleNewComment = (comment: Comment) => {
    setComments((prev) => [...prev, comment]); // 시간순이므로 끝에 추가
    setTotal((prev) => prev + 1);
    setReplyTo(null);
  };

  const handleLoadMore = async () => {
    setLoadingMore(true);
    try {
      const nextPage = page + 1;
      const res = await fetch(`/api/comments?serviceId=${serviceId}&page=${nextPage}`);
      const data = await res.json();
      setComments((prev) => [...prev, ...data.items]);
      setPage(nextPage);
      setHasMore(data.hasMore);
    } catch {} finally {
      setLoadingMore(false);
    }
  };

  const handleDeleted = (commentId: string) => {
    setComments((prev) => prev.filter((c) => c.id !== commentId));
    setTotal((prev) => prev - 1);
  };

  const handleUpdated = (updated: Comment) => {
    setComments((prev) => prev.map((c) => c.id === updated.id ? { ...c, ...updated } : c));
  };

  const handleReply = (commentId: string, authorName: string) => {
    setReplyTo({ commentId, authorName });
    // 스크롤 to form
    setTimeout(() => {
      document.getElementById("comment-reply-form")?.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 100);
  };

  return (
    <div className="mt-8">
      <h2 className="flex items-center gap-2 text-lg font-bold dark:text-white text-zinc-900 mb-6">
        <MessageSquare className="w-5 h-5" />
        댓글 {total > 0 && <span className="text-sm font-normal dark:text-zinc-500 text-zinc-400">{total}개</span>}
      </h2>

      {/* Top-level comment form */}
      {!replyTo && (
        <CommentForm serviceId={serviceId} onSubmitted={handleNewComment} />
      )}

      {/* Comment list — flat, all at the same level */}
      {comments.length === 0 ? (
        <div className="text-center py-12">
          <MessageSquare className="w-8 h-8 mx-auto mb-3 dark:text-zinc-600 text-zinc-300" />
          <p className="text-sm dark:text-zinc-500 text-zinc-400">
            첫 번째 댓글을 작성해보세요!
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {comments.map((comment) => (
            <CommentItem
              key={comment.id}
              comment={comment}
              serviceId={serviceId}
              onDeleted={handleDeleted}
              onUpdated={handleUpdated}
              onReply={handleReply}
            />
          ))}

          {hasMore && (
            <div className="flex justify-center pt-4">
              <button
                onClick={handleLoadMore}
                disabled={loadingMore}
                className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-medium
                  dark:bg-white/5 bg-black/5
                  dark:hover:bg-white/10 hover:bg-black/10
                  dark:text-zinc-400 text-zinc-500
                  disabled:opacity-50 transition-all duration-200"
              >
                {loadingMore ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <ChevronDown className="w-4 h-4" />
                )}
                {loadingMore ? "불러오는 중..." : "더보기"}
              </button>
            </div>
          )}
        </div>
      )}

      {/* Reply form — appears at the bottom when replying */}
      {replyTo && (
        <div id="comment-reply-form" className="mt-4">
          <CommentForm
            serviceId={serviceId}
            parentId={replyTo.commentId}
            replyToName={replyTo.authorName}
            onSubmitted={handleNewComment}
            onCancel={() => setReplyTo(null)}
            compact
          />
        </div>
      )}
    </div>
  );
}
