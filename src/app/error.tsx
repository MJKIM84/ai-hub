"use client";

import { useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("Application error:", error);
  }, [error]);

  return (
    <div className="min-h-screen flex items-center justify-center dark:bg-[#0a0a0f] bg-gray-50">
      <div className="text-center px-6">
        <div className="text-6xl mb-4">⚠️</div>
        <h1 className="text-2xl font-bold dark:text-white text-zinc-900 mb-2">
          오류가 발생했습니다
        </h1>
        <p className="dark:text-zinc-400 text-zinc-500 mb-8 max-w-md">
          일시적인 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.
        </p>
        <div className="flex items-center justify-center gap-4">
          <button
            onClick={reset}
            className="inline-flex items-center gap-2 px-6 py-3 rounded-xl font-medium
              bg-gradient-to-r from-neon-blue to-neon-purple text-white
              hover:opacity-90 transition-opacity"
          >
            다시 시도
          </button>
          <a
            href="/"
            className="inline-flex items-center gap-2 px-6 py-3 rounded-xl font-medium
              dark:bg-white/10 bg-black/5 dark:text-white text-zinc-900
              hover:opacity-80 transition-opacity"
          >
            홈으로
          </a>
        </div>
      </div>
    </div>
  );
}
