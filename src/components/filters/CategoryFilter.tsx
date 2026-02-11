"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { CATEGORIES } from "@/constants/categories";
import {
  LayoutGrid, MessageSquare, Image, Palette, Code2, Zap, Mic,
  GraduationCap, Video, BarChart3, PenTool, Languages, Heart, Globe, Rocket
} from "lucide-react";

const iconMap: Record<string, React.ComponentType<{ className?: string }>> = {
  LayoutGrid, MessageSquare, Image, Palette, Code2, Zap, Mic,
  GraduationCap, Video, BarChart3, PenTool, Languages, Heart, Globe, Rocket,
};

const INDIE_DEV_ID = "indie-dev";

interface CategoryFilterProps {
  activeCategory?: string;
  categoryCounts?: Record<string, number>;
}

export function CategoryFilter({ activeCategory, categoryCounts }: CategoryFilterProps) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const setCategory = (categoryId: string) => {
    const params = new URLSearchParams(searchParams.toString());
    if (categoryId === "all") {
      params.delete("category");
    } else {
      params.set("category", categoryId);
    }
    params.delete("page");
    router.replace(`/?${params.toString()}`, { scroll: false });
  };

  const current = activeCategory || "all";

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8">
      <div className="flex gap-2 overflow-x-auto no-scrollbar pb-2">
        {CATEGORIES.map((cat) => {
          const Icon = iconMap[cat.icon];
          const isActive = current === cat.id;
          const isIndieDev = cat.id === INDIE_DEV_ID;
          const count = cat.id === 'all' ? undefined : categoryCounts?.[cat.id];

          // 개인개발 카테고리: 항상 눈에 띄는 특별 스타일
          if (isIndieDev) {
            return (
              <button
                key={cat.id}
                onClick={() => setCategory(cat.id)}
                className={`indie-dev-btn flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-bold whitespace-nowrap
                  transition-all duration-200 shrink-0 relative overflow-hidden
                  ${isActive
                    ? "indie-dev-btn-active shadow-lg"
                    : "indie-dev-btn-inactive"
                  }`}
              >
                {Icon && <Icon className="w-4 h-4 relative z-10" />}
                <span className="relative z-10">{cat.nameKo}</span>
                {count !== undefined && count > 0 && (
                  <span className={`text-xs relative z-10 ${isActive ? "text-white/80" : "opacity-70"}`}>
                    {count}
                  </span>
                )}
              </button>
            );
          }

          return (
            <button
              key={cat.id}
              onClick={() => setCategory(cat.id)}
              className={`flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium whitespace-nowrap
                transition-all duration-200 shrink-0
                ${isActive
                  ? "bg-gradient-to-r from-neon-blue to-neon-purple text-white shadow-lg shadow-neon-blue/20"
                  : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-600 dark:hover:bg-white/10 hover:bg-black/10"
                }`}
            >
              {Icon && <Icon className="w-4 h-4" />}
              <span>{cat.nameKo}</span>
              {count !== undefined && count > 0 && (
                <span className={`text-xs ${isActive ? "text-white/70" : "dark:text-zinc-500 text-zinc-400"}`}>
                  {count}
                </span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
