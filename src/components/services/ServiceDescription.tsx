"use client";

import { useState } from "react";
import { LanguageToggle } from "./LanguageToggle";

interface ServiceDescriptionProps {
  name: string;
  nameKo?: string | null;
  description?: string | null;
  descriptionKo?: string | null;
  tagline?: string | null;
}

export function ServiceDescription({
  name,
  nameKo,
  description,
  descriptionKo,
  tagline,
}: ServiceDescriptionProps) {
  const hasKorean = !!(nameKo || descriptionKo);
  const [lang, setLang] = useState<"ko" | "en">(hasKorean ? "ko" : "en");

  const displayName = lang === "ko" && nameKo ? nameKo : name;
  const displayDescription =
    lang === "ko" && descriptionKo
      ? descriptionKo
      : description || tagline || null;

  return (
    <div>
      {/* 언어 토글 */}
      {hasKorean && (
        <div className="flex items-center justify-between mb-3">
          <span className="text-xs dark:text-zinc-500 text-zinc-400">설명</span>
          <LanguageToggle lang={lang} onToggle={setLang} hasKorean={hasKorean} />
        </div>
      )}

      {/* 한국어 이름 (원문과 다를 때만 표시) */}
      {lang === "ko" && nameKo && nameKo !== name && (
        <p className="text-sm font-medium dark:text-zinc-400 text-zinc-500 mb-2">
          {displayName}
        </p>
      )}

      {/* 설명 본문 */}
      {displayDescription && (
        <p className="dark:text-zinc-300 text-zinc-600 leading-relaxed whitespace-pre-wrap">
          {displayDescription}
        </p>
      )}

      {/* 원문 참고 (한국어 모드일 때) */}
      {lang === "ko" && descriptionKo && description && (
        <p className="text-xs dark:text-zinc-600 text-zinc-400 mt-2">
          원문: {description.length > 100 ? description.substring(0, 100) + "..." : description}
        </p>
      )}
    </div>
  );
}
