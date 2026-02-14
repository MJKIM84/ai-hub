"use client";

import { useState, useEffect, useCallback } from "react";
import { Workflow, Rocket, ArrowDown } from "lucide-react";

const HERO_SLIDES = [
  {
    badge: "AI를 파이프라인으로 연결하세요",
    badgeIcon: "workflow" as const,
    titleTop: "나만의",
    titleBottom: "AI 워크플로를 설계하세요",
    gradient: "from-neon-blue via-neon-purple to-neon-pink",
    desc1: "수백 개의 AI 서비스를 탐색하고, 파이프라인으로 조합하세요.",
    desc2: "업무에 딱 맞는 AI 워크플로를 만들어보세요.",
  },
  {
    badge: "내가 만든 AI 서비스를 무료로 홍보하세요",
    badgeIcon: "rocket" as const,
    titleTop: "개발자를 위한",
    titleBottom: "무료 AI 홍보 플랫폼",
    gradient: "from-neon-orange via-neon-pink to-neon-purple",
    desc1: "URL 하나만 입력하면 서비스 정보가 자동으로 등록됩니다.",
    desc2: "개인개발자도 1분 안에 무료로 홍보를 시작할 수 있습니다.",
  },
] as const;

const INTERVAL = 5000;

export function HeroSection() {
  const [current, setCurrent] = useState(0);
  const [fade, setFade] = useState(true);

  const goTo = useCallback((index: number) => {
    setFade(false);
    setTimeout(() => {
      setCurrent(index);
      setFade(true);
    }, 300);
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      goTo(current === 0 ? 1 : 0);
    }, INTERVAL);
    return () => clearInterval(timer);
  }, [current, goTo]);

  const slide = HERO_SLIDES[current];

  return (
    <section className="relative pt-32 pb-12 px-4 hero-gradient overflow-hidden">
      {/* Pipeline network lines */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <svg className="absolute inset-0 w-full h-full opacity-[0.06] dark:opacity-[0.08]" xmlns="http://www.w3.org/2000/svg">
          <line x1="10%" y1="20%" x2="40%" y2="50%" stroke="currentColor" strokeWidth="1" className="text-neon-blue" />
          <line x1="40%" y1="50%" x2="70%" y2="30%" stroke="currentColor" strokeWidth="1" className="text-neon-blue" />
          <line x1="70%" y1="30%" x2="90%" y2="60%" stroke="currentColor" strokeWidth="1" className="text-neon-purple" />
          <line x1="30%" y1="70%" x2="60%" y2="80%" stroke="currentColor" strokeWidth="1" className="text-neon-purple" />
          <line x1="20%" y1="40%" x2="50%" y2="20%" stroke="currentColor" strokeWidth="1" className="text-neon-blue" />
          <circle cx="10%" cy="20%" r="3" className="fill-neon-blue" />
          <circle cx="40%" cy="50%" r="4" className="fill-neon-blue" />
          <circle cx="70%" cy="30%" r="3" className="fill-neon-purple" />
          <circle cx="90%" cy="60%" r="3" className="fill-neon-purple" />
          <circle cx="30%" cy="70%" r="3" className="fill-neon-purple" />
          <circle cx="60%" cy="80%" r="3" className="fill-neon-blue" />
        </svg>
        <div className="absolute top-20 left-1/4 w-72 h-72 bg-neon-blue/10 rounded-full blur-3xl animate-float" />
        <div className="absolute top-40 right-1/4 w-96 h-96 bg-neon-purple/8 rounded-full blur-3xl animate-float" style={{ animationDelay: '-3s' }} />
      </div>

      <div className="relative max-w-4xl mx-auto text-center">
        <div
          className={`transition-all duration-300 ease-in-out ${
            fade ? "opacity-100 translate-y-0" : "opacity-0 -translate-y-2"
          }`}
        >
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full
            dark:bg-white/5 bg-black/5
            dark:border-white/10 border-black/10 border
            text-sm mb-6">
            {slide.badgeIcon === "workflow" ? (
              <Workflow className="w-4 h-4 text-neon-blue" />
            ) : (
              <Rocket className="w-4 h-4 text-neon-orange" />
            )}
            <span className="dark:text-zinc-300 text-zinc-600">
              {slide.badge}
            </span>
          </div>

          {/* Title */}
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight mb-6">
            <span className="dark:text-white text-zinc-900">{slide.titleTop}</span>
            <br />
            <span className={`bg-gradient-to-r ${slide.gradient} bg-clip-text text-transparent`}>
              {slide.titleBottom}
            </span>
          </h1>

          {/* Description */}
          <p className="text-lg sm:text-xl dark:text-zinc-400 text-zinc-500 max-w-2xl mx-auto mb-10 leading-relaxed">
            {slide.desc1}
            <br className="hidden sm:block" />
            {slide.desc2}
          </p>
        </div>

        {/* Slide indicators */}
        <div className="flex items-center justify-center gap-2 mb-6">
          {HERO_SLIDES.map((_, i) => (
            <button
              key={i}
              onClick={() => goTo(i)}
              className={`h-1.5 rounded-full transition-all duration-300
                ${i === current
                  ? "w-8 bg-gradient-to-r from-neon-blue to-neon-purple"
                  : "w-1.5 dark:bg-white/20 bg-black/15 dark:hover:bg-white/30 hover:bg-black/25"
                }`}
            />
          ))}
        </div>

        <div className="flex items-center justify-center">
          <ArrowDown className="w-5 h-5 dark:text-zinc-500 text-zinc-400 animate-bounce" />
        </div>
      </div>
    </section>
  );
}
