"use client";

import { useState } from "react";
import { Search, Mail, Send, Loader2, Check, Handshake, MessageSquareText } from "lucide-react";
import Link from "next/link";

export function Footer() {
  const [type, setType] = useState<"partnership" | "feedback">("feedback");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;

    setSubmitting(true);
    setError("");
    try {
      const res = await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          type,
          email: email.trim() || undefined,
          message: message.trim(),
        }),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || "전송에 실패했습니다.");
      }

      setSubmitted(true);
      setMessage("");
      setEmail("");
      setTimeout(() => setSubmitted(false), 3000);
    } catch (err) {
      setError(err instanceof Error ? err.message : "오류가 발생했습니다.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <footer className="mt-20 border-t dark:border-white/10 border-black/10">
      {/* 제휴 & 의견 영역 */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="max-w-2xl mx-auto">
          <div className="text-center mb-8">
            <h3 className="text-lg font-bold dark:text-white text-zinc-900 mb-2">
              FindMyAI와 함께하기
            </h3>
            <p className="text-sm dark:text-zinc-400 text-zinc-500">
              제휴 문의, 기능 제안, 서비스 개선 의견 등 무엇이든 환영합니다.
            </p>
          </div>

          {/* 유형 선택 탭 */}
          <div className="flex justify-center gap-2 mb-6">
            <button
              type="button"
              onClick={() => setType("feedback")}
              className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200
                ${type === "feedback"
                  ? "dark:bg-neon-blue/15 bg-neon-blue/10 dark:text-neon-blue text-blue-600 ring-1 dark:ring-neon-blue/30 ring-neon-blue/20"
                  : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500 dark:hover:bg-white/10 hover:bg-black/10"
                }`}
            >
              <MessageSquareText className="w-4 h-4" />
              의견/제안
            </button>
            <button
              type="button"
              onClick={() => setType("partnership")}
              className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200
                ${type === "partnership"
                  ? "dark:bg-neon-purple/15 bg-neon-purple/10 dark:text-neon-purple text-purple-600 ring-1 dark:ring-neon-purple/30 ring-neon-purple/20"
                  : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500 dark:hover:bg-white/10 hover:bg-black/10"
                }`}
            >
              <Handshake className="w-4 h-4" />
              제휴 문의
            </button>
          </div>

          {/* 폼 */}
          <form onSubmit={handleSubmit} className="glass rounded-xl p-5">
            <div className="flex items-center gap-2 mb-3">
              <div className="flex items-center gap-2 px-3 py-2 rounded-lg flex-1
                dark:bg-white/5 bg-black/5 border dark:border-white/5 border-black/5">
                <Mail className="w-4 h-4 dark:text-zinc-500 text-zinc-400 shrink-0" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="이메일 (선택사항 — 답변을 원하시면 입력해주세요)"
                  className="w-full bg-transparent outline-none text-sm
                    dark:text-white text-zinc-900
                    dark:placeholder-zinc-500 placeholder-zinc-400"
                />
              </div>
            </div>
            <textarea
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder={
                type === "partnership"
                  ? "제휴 내용을 알려주세요. (회사명, 제안 내용 등)"
                  : "서비스 개선 의견, 기능 제안, 버그 제보 등 자유롭게 작성해주세요."
              }
              rows={3}
              maxLength={2000}
              className="w-full px-3 py-2 rounded-lg text-sm bg-transparent resize-none mb-3
                dark:bg-white/5 bg-black/5
                dark:text-white text-zinc-900
                dark:placeholder-zinc-500 placeholder-zinc-400
                outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30
                border dark:border-white/5 border-black/5"
            />
            {error && <p className="text-xs text-red-400 mb-2">{error}</p>}
            <div className="flex items-center justify-between">
              <span className="text-xs dark:text-zinc-500 text-zinc-400">
                {message.length}/2000
              </span>
              <button
                type="submit"
                disabled={submitting || !message.trim() || submitted}
                className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-medium
                  transition-all duration-200 disabled:opacity-40 disabled:cursor-not-allowed
                  ${submitted
                    ? "bg-emerald-500/20 text-emerald-400"
                    : "bg-gradient-to-r from-neon-blue to-neon-purple text-white hover:opacity-90"
                  }`}
              >
                {submitted ? (
                  <>
                    <Check className="w-4 h-4" />
                    전송 완료!
                  </>
                ) : submitting ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    전송 중...
                  </>
                ) : (
                  <>
                    <Send className="w-4 h-4" />
                    전송하기
                  </>
                )}
              </button>
            </div>
          </form>
        </div>
      </div>

      {/* 기존 하단 바 */}
      <div className="border-t dark:border-white/5 border-black/5 py-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <div className="w-6 h-6 rounded-md bg-gradient-to-br from-neon-blue to-neon-purple flex items-center justify-center">
                <Search className="w-3 h-3 text-white" />
              </div>
              <span className="text-sm font-semibold bg-gradient-to-r from-neon-blue to-neon-purple bg-clip-text text-transparent">
                FindMyAI
              </span>
            </div>
            <div className="flex items-center gap-4">
              <Link
                href="/policy"
                className="text-sm dark:text-zinc-500 text-zinc-400 hover:dark:text-zinc-300 hover:text-zinc-600 transition-colors"
              >
                운영정책
              </Link>
              <span className="dark:text-zinc-700 text-zinc-300">|</span>
              <p className="text-sm dark:text-zinc-500 text-zinc-400">
                나에게 맞는 AI를 찾아보세요.
              </p>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
