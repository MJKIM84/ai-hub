"use client";

import { useState, useCallback } from "react";

interface ServiceLogoProps {
  logoUrl: string | null;
  faviconUrl: string | null;
  ogImageUrl: string | null;
  serviceUrl: string;
  name: string;
  size?: "sm" | "md" | "lg";
}

// 서비스 URL에서 도메인 추출
function getDomain(url: string): string {
  try {
    return new URL(url).hostname;
  } catch {
    return "";
  }
}

// Google Favicon API (항상 작동하는 최후 fallback)
function getGoogleFavicon(domain: string, size: number = 128): string {
  return `https://www.google.com/s2/favicons?domain=${domain}&sz=${size}`;
}

// 배경색을 이름 해시로 생성 (일관된 색상)
function getHashColor(name: string): string {
  const colors = [
    "from-blue-500 to-blue-600",
    "from-purple-500 to-purple-600",
    "from-pink-500 to-pink-600",
    "from-indigo-500 to-indigo-600",
    "from-cyan-500 to-cyan-600",
    "from-teal-500 to-teal-600",
    "from-emerald-500 to-emerald-600",
    "from-orange-500 to-orange-600",
    "from-rose-500 to-rose-600",
    "from-violet-500 to-violet-600",
  ];
  let hash = 0;
  for (let i = 0; i < name.length; i++) {
    hash = name.charCodeAt(i) + ((hash << 5) - hash);
  }
  return colors[Math.abs(hash) % colors.length];
}

const sizeClasses = {
  sm: "w-10 h-10 rounded-lg text-sm",
  md: "w-12 h-12 rounded-xl text-lg",
  lg: "w-14 h-14 sm:w-20 sm:h-20 rounded-xl sm:rounded-2xl text-2xl sm:text-3xl",
};

export function ServiceLogo({
  logoUrl,
  faviconUrl,
  ogImageUrl,
  serviceUrl,
  name,
  size = "md",
}: ServiceLogoProps) {
  // fallback 단계: logoUrl → faviconUrl → ogImageUrl → Google Favicon → 이니셜
  const domain = getDomain(serviceUrl);

  const sources = [
    logoUrl,
    faviconUrl,
    ogImageUrl,
    domain ? getGoogleFavicon(domain) : null,
  ].filter(Boolean) as string[];

  const [currentIndex, setCurrentIndex] = useState(0);
  const [showInitial, setShowInitial] = useState(sources.length === 0);

  const handleError = useCallback(() => {
    if (currentIndex < sources.length - 1) {
      // 다음 fallback 소스로 전환
      setCurrentIndex((prev) => prev + 1);
    } else {
      // 모든 소스 실패 → 이니셜 표시
      setShowInitial(true);
    }
  }, [currentIndex, sources.length]);

  const hashColor = getHashColor(name);
  const initial = name.charAt(0).toUpperCase();

  if (showInitial) {
    return (
      <div
        className={`${sizeClasses[size]} shrink-0 bg-gradient-to-br ${hashColor}
          flex items-center justify-center font-bold text-white`}
      >
        {initial}
      </div>
    );
  }

  return (
    <div
      className={`${sizeClasses[size]} shrink-0 overflow-hidden
        dark:bg-white/10 bg-black/5 flex items-center justify-center`}
    >
      <img
        src={sources[currentIndex]}
        alt={name}
        className="w-full h-full object-cover"
        loading="lazy"
        referrerPolicy="no-referrer"
        onError={handleError}
      />
    </div>
  );
}
