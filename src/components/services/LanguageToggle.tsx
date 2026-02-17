"use client";

interface LanguageToggleProps {
  lang: "ko" | "en";
  onToggle: (lang: "ko" | "en") => void;
  hasKorean: boolean;
}

export function LanguageToggle({ lang, onToggle, hasKorean }: LanguageToggleProps) {
  if (!hasKorean) return null;

  return (
    <div className="inline-flex items-center rounded-lg dark:bg-white/5 bg-black/5 p-0.5">
      <button
        onClick={() => onToggle("ko")}
        className={`px-3 py-1 rounded-md text-xs font-medium transition-all duration-200
          ${lang === "ko"
            ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
            : "dark:text-zinc-400 text-zinc-500 dark:hover:text-zinc-300 hover:text-zinc-600"
          }`}
      >
        한국어
      </button>
      <button
        onClick={() => onToggle("en")}
        className={`px-3 py-1 rounded-md text-xs font-medium transition-all duration-200
          ${lang === "en"
            ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
            : "dark:text-zinc-400 text-zinc-500 dark:hover:text-zinc-300 hover:text-zinc-600"
          }`}
      >
        English
      </button>
    </div>
  );
}
