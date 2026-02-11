"use client";

import { Sparkles, ArrowDown } from "lucide-react";

export function HeroSection() {
  return (
    <section className="relative pt-32 pb-12 px-4 hero-gradient overflow-hidden">
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-20 left-1/4 w-72 h-72 bg-neon-blue/10 rounded-full blur-3xl animate-float" />
        <div className="absolute top-40 right-1/4 w-96 h-96 bg-neon-purple/8 rounded-full blur-3xl animate-float" style={{ animationDelay: '-3s' }} />
      </div>

      <div className="relative max-w-4xl mx-auto text-center">
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full
          dark:bg-white/5 bg-black/5
          dark:border-white/10 border-black/10 border
          text-sm mb-6">
          <Sparkles className="w-4 h-4 text-neon-blue" />
          <span className="dark:text-zinc-300 text-zinc-600">
            AI 서비스를 한곳에서 발견하세요
          </span>
        </div>

        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight mb-6">
          <span className="dark:text-white text-zinc-900">나에게 맞는</span>
          <br />
          <span className="bg-gradient-to-r from-neon-blue via-neon-purple to-neon-pink bg-clip-text text-transparent">
            AI 도구를 발견하세요
          </span>
        </h1>

        <p className="text-lg sm:text-xl dark:text-zinc-400 text-zinc-500 max-w-2xl mx-auto mb-10 leading-relaxed">
          수만 개의 AI 서비스 중에서 당신에게 딱 맞는 도구를 찾아보세요.
          <br className="hidden sm:block" />
          개발자는 자신의 서비스를 1분 안에 등록할 수 있습니다.
        </p>

        <div className="flex items-center justify-center">
          <ArrowDown className="w-5 h-5 dark:text-zinc-500 text-zinc-400 animate-bounce" />
        </div>
      </div>
    </section>
  );
}
