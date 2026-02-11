"use client";

import { useState, useEffect } from "react";
import { MessageSquare, ThumbsUp, ThumbsDown, Send, Loader2, ChevronDown } from "lucide-react";
import { formatRelativeTime } from "@/lib/utils";
import type { Comment } from "@/types/service";

interface CommentSectionProps {
  serviceId: string;
  initialComments: Comment[];
  initialTotal: number;
}

export function CommentSection({ serviceId, initialComments, initialTotal }: CommentSectionProps) {
  const [comments, setComments] = useState<Comment[]>(initialComments);
  const [total, setTotal] = useState(initialTotal);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(initialTotal > 20);
  const [loadingMore, setLoadingMore] = useState(false);

  // 댓글 작성 상태
  const [nickname, setNickname] = useState("");
  const [content, setContent] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  // 투표 상태 (commentId → "like" | "dislike")
  const [votedComments, setVotedComments] = useState<Record<string, string>>({});

  // localStorage에서 닉네임 복원
  useEffect(() => {
    const saved = localStorage.getItem("aihub_nickname");
    if (saved) setNickname(saved);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    if (!nickname.trim() || !content.trim()) {
      setError("닉네임과 댓글 내용을 입력해주세요.");
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
      setComments((prev) => [newComment, ...prev]);
      setTotal((prev) => prev + 1);
      setContent("");
      localStorage.setItem("aihub_nickname", nickname.trim());
    } catch {
      setError("댓글 작성에 실패했습니다.");
    } finally {
      setSubmitting(false);
    }
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
    } catch {
      // ignore
    } finally {
      setLoadingMore(false);
    }
  };

  const handleCommentVote = async (commentId: string, type: "like" | "dislike") => {
    if (votedComments[commentId]) return;

    try {
      const res = await fetch("/api/comments/vote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ commentId, type }),
      });
      const data = await res.json();

      if (data.alreadyVoted || res.ok) {
        setVotedComments((prev) => ({ ...prev, [commentId]: type }));
      }
      if (res.ok && !data.alreadyVoted) {
        setComments((prev) =>
          prev.map((c) =>
            c.id === commentId
              ? { ...c, likes: data.likes, dislikes: data.dislikes }
              : c
          )
        );
      }
    } catch {}
  };

  return (
    <div className="mt-8">
      <h2 className="flex items-center gap-2 text-lg font-bold dark:text-white text-zinc-900 mb-6">
        <MessageSquare className="w-5 h-5" />
        댓글 {total > 0 && <span className="text-sm font-normal dark:text-zinc-500 text-zinc-400">{total}개</span>}
      </h2>

      {/* 댓글 작성 폼 */}
      <form onSubmit={handleSubmit} className="mb-8">
        <div className="glass rounded-xl p-4">
          <div className="flex gap-3 mb-3">
            <input
              type="text"
              value={nickname}
              onChange={(e) => setNickname(e.target.value)}
              placeholder="닉네임"
              maxLength={50}
              className="w-32 sm:w-40 px-3 py-2 rounded-lg text-sm bg-transparent
                dark:bg-white/5 bg-black/5
                dark:text-white text-zinc-900
                dark:placeholder-zinc-500 placeholder-zinc-400
                outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30"
            />
          </div>
          <div className="flex gap-3">
            <textarea
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="댓글을 작성해주세요..."
              maxLength={1000}
              rows={3}
              className="flex-1 px-3 py-2 rounded-lg text-sm bg-transparent resize-none
                dark:bg-white/5 bg-black/5
                dark:text-white text-zinc-900
                dark:placeholder-zinc-500 placeholder-zinc-400
                outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30"
            />
          </div>
          <div className="flex items-center justify-between mt-3">
            <span className="text-xs dark:text-zinc-500 text-zinc-400">
              {content.length}/1000
            </span>
            <button
              type="submit"
              disabled={submitting || !nickname.trim() || !content.trim()}
              className="flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium
                bg-gradient-to-r from-neon-blue to-neon-purple text-white
                hover:opacity-90 transition-all duration-200
                disabled:opacity-40 disabled:cursor-not-allowed"
            >
              {submitting ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
              등록
            </button>
          </div>
          {error && (
            <p className="text-xs text-red-400 mt-2">{error}</p>
          )}
        </div>
      </form>

      {/* 댓글 목록 */}
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
            <div key={comment.id} className="rounded-xl p-4 dark:bg-white/5 bg-black/5">
              <div className="flex items-center justify-between mb-2">
                <span className="text-sm font-medium dark:text-white text-zinc-900">
                  {comment.authorName}
                </span>
                <span className="text-xs dark:text-zinc-500 text-zinc-400">
                  {formatRelativeTime(comment.createdAt)}
                </span>
              </div>
              <p className="text-sm dark:text-zinc-300 text-zinc-600 leading-relaxed mb-3 whitespace-pre-wrap">
                {comment.content}
              </p>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => handleCommentVote(comment.id, "like")}
                  disabled={!!votedComments[comment.id]}
                  className={`flex items-center gap-1 text-xs transition-colors
                    ${votedComments[comment.id] === "like"
                      ? "dark:text-neon-green text-emerald-600"
                      : "dark:text-zinc-500 text-zinc-400 dark:hover:text-neon-green hover:text-emerald-600"
                    }
                    disabled:cursor-default`}
                >
                  <ThumbsUp className="w-3.5 h-3.5" />
                  {comment.likes > 0 && comment.likes}
                </button>
                <button
                  onClick={() => handleCommentVote(comment.id, "dislike")}
                  disabled={!!votedComments[comment.id]}
                  className={`flex items-center gap-1 text-xs transition-colors
                    ${votedComments[comment.id] === "dislike"
                      ? "dark:text-pink-400 text-pink-600"
                      : "dark:text-zinc-500 text-zinc-400 dark:hover:text-pink-400 hover:text-pink-600"
                    }
                    disabled:cursor-default`}
                >
                  <ThumbsDown className="w-3.5 h-3.5" />
                  {comment.dislikes > 0 && comment.dislikes}
                </button>
              </div>
            </div>
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
    </div>
  );
}
