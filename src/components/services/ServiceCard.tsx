"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { ThumbsUp, Eye, Flag, Bot, UserCheck, ArrowRight } from "lucide-react";
import type { Service } from "@/types/service";
import { CATEGORIES, PRICING_MODELS } from "@/constants/categories";
import { formatNumber } from "@/lib/utils";

interface ServiceCardProps {
  service: Service;
  onVote?: (serviceId: string) => void;
}

// 카테고리별 파이프 컬러 매핑
function getPipeColorClass(categoryId: string): string {
  const colorMap: Record<string, string> = {
    "text-generation": "",
    "image-generation": "pipe-node-purple",
    "image-editing": "pipe-node-pink",
    "code-assistant": "pipe-node-green",
    "productivity": "",
    "voice-speech": "pipe-node-orange",
    "education": "pipe-node-purple",
    "video": "pipe-node-pink",
    "data-analysis": "pipe-node-green",
    "writing": "pipe-node-purple",
    "translation": "",
    "healthcare": "pipe-node-pink",
    "korean-llm": "",
    "indie-dev": "pipe-node-orange",
  };
  return colorMap[categoryId] || "";
}

export function ServiceCard({ service, onVote }: ServiceCardProps) {
  const [voted, setVoted] = useState(false);
  const router = useRouter();
  const category = CATEGORIES.find((c) => c.id === service.category);
  const pricing = PRICING_MODELS.find((p) => p.id === service.pricingModel);

  const handleClick = () => {
    router.push(`/service/${service.slug}`);
  };

  const handleVote = async (e: React.MouseEvent) => {
    e.stopPropagation();
    try {
      const res = await fetch("/api/vote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ serviceId: service.id, type: "upvote" }),
      });
      const data = await res.json();
      if (res.ok) {
        if (data.action === "cancelled") {
          setVoted(false);
        } else {
          setVoted(true);
        }
        onVote?.(service.id);
      }
    } catch {}
  };

  const logoSrc = service.logoUrl || service.faviconUrl || service.ogImageUrl;
  const pipeColor = getPipeColorClass(service.category);

  return (
    <div
      onClick={handleClick}
      className={`pipe-node ${pipeColor} p-5 cursor-pointer group relative flex flex-col h-full`}
    >
      <div className="flex items-start gap-4 mb-3">
        <div className="w-12 h-12 rounded-xl overflow-hidden shrink-0
          dark:bg-white/10 bg-black/5 flex items-center justify-center">
          {logoSrc ? (
            <img
              src={logoSrc}
              alt={service.name}
              className="w-full h-full object-cover"
              onError={(e) => {
                const img = e.target as HTMLImageElement;
                img.style.display = 'none';
                const fallback = document.createElement('span');
                fallback.className = 'text-lg font-bold dark:text-zinc-400 text-zinc-500';
                fallback.textContent = service.name[0] || '?';
                img.parentElement?.appendChild(fallback);
              }}
            />
          ) : (
            <span className="text-lg font-bold dark:text-zinc-400 text-zinc-500">
              {service.name[0]}
            </span>
          )}
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2">
            <h3 className="font-semibold dark:text-white text-zinc-900 truncate text-base">
              {service.name}
            </h3>
            {service.isKorean && (
              <span title="한국 서비스"><Flag className="w-3.5 h-3.5 text-neon-blue shrink-0" /></span>
            )}
            {service.source === "auto" && (
              <span title="자동 수집"><Bot className="w-3.5 h-3.5 text-orange-400 shrink-0" /></span>
            )}
            {service.source === "developer" && (
              <span title="개발자 인증"><UserCheck className="w-3.5 h-3.5 text-emerald-400 shrink-0" /></span>
            )}
          </div>
          <p className="text-sm dark:text-zinc-400 text-zinc-500 line-clamp-2 mt-1 leading-relaxed">
            {service.description || service.tagline || "설명이 없습니다."}
          </p>
        </div>
      </div>

      <div className="flex items-center gap-2 flex-wrap mt-auto pt-3">
        {category && (
          <span className="px-2.5 py-1 rounded-lg text-xs font-medium
            dark:bg-neon-purple/15 bg-neon-purple/10
            dark:text-neon-purple text-purple-600">
            {category.nameKo}
          </span>
        )}
        {pricing && (
          <span className={`px-2.5 py-1 rounded-lg text-xs font-medium
            ${pricing.id === 'free'
              ? 'dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600'
              : pricing.id === 'freemium'
              ? 'dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600'
              : 'dark:bg-amber-500/15 bg-amber-500/10 dark:text-amber-400 text-amber-600'
            }`}>
            {pricing.nameKo}
          </span>
        )}
      </div>

      <div className="flex items-center justify-between mt-3 pt-3 border-t dark:border-white/5 border-black/5">
        <div className="flex items-center gap-3 text-xs dark:text-zinc-500 text-zinc-400">
          <span className="flex items-center gap-1">
            <Eye className="w-3.5 h-3.5" />
            {formatNumber(service.clicks)}
          </span>
          <span className="flex items-center gap-1">
            <ThumbsUp className="w-3.5 h-3.5" />
            {formatNumber(service.upvotes)}
          </span>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={handleVote}
            className={`flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-medium
              transition-all duration-200
              ${voted
                ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-neon-blue"
                : "dark:bg-white/5 bg-black/5 dark:hover:bg-neon-blue/20 hover:bg-neon-blue/10 dark:text-zinc-400 text-zinc-500 dark:hover:text-neon-blue hover:text-neon-blue"
              }`}
          >
            <ThumbsUp className={`w-3 h-3 ${voted ? "fill-current" : ""}`} />
            {voted ? "추천됨" : "추천"}
          </button>
          <ArrowRight className="w-4 h-4 dark:text-zinc-500 text-zinc-400
            group-hover:text-neon-blue group-hover:translate-x-0.5 transition-all" />
        </div>
      </div>
    </div>
  );
}
