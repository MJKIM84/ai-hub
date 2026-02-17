"use client";

import { useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react";

export function BackButton() {
  const router = useRouter();

  const handleBack = () => {
    router.back();
  };

  return (
    <button
      onClick={handleBack}
      className="inline-flex items-center gap-2 text-sm dark:text-zinc-400 text-zinc-500 hover:text-neon-blue transition-colors mb-6 sm:mb-8 py-2 active:scale-95"
    >
      <ArrowLeft className="w-4 h-4" />
      목록으로 돌아가기
    </button>
  );
}
