"use client";

import { Search, X } from "lucide-react";
import { useState, useCallback, useEffect, useRef } from "react";
import { useRouter, useSearchParams } from "next/navigation";

export function SearchBar({ initialQuery }: { initialQuery?: string }) {
  const [query, setQuery] = useState(initialQuery || "");
  const router = useRouter();
  const searchParams = useSearchParams();
  const hasScrolled = useRef(false);
  const searchWrapperRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const isTypingRef = useRef(false);

  const updateSearch = useCallback(
    (value: string) => {
      const params = new URLSearchParams(searchParams.toString());
      if (value) {
        params.set("q", value);
      } else {
        params.delete("q");
      }
      params.delete("page");
      // replace + scroll:false로 타이핑 중 스크롤 위치 유지
      router.replace(`/?${params.toString()}`, { scroll: false });
    },
    [router, searchParams]
  );

  useEffect(() => {
    const timer = setTimeout(() => {
      updateSearch(query);
    }, 300);
    return () => clearTimeout(timer);
  }, [query, updateSearch]);

  // 서버 데이터가 바뀌어도 포커스 + 스크롤 위치 복원
  useEffect(() => {
    if (isTypingRef.current && inputRef.current) {
      // 타이핑 중이면 포커스를 다시 잡아줌
      inputRef.current.focus();
    }
  });

  const handleFocus = () => {
    if (hasScrolled.current) return;
    hasScrolled.current = true;

    // 검색바 자체를 화면 상단 근처로 스크롤 → 검색바 + 서비스 카드 동시에 보임
    if (searchWrapperRef.current) {
      const offset = 20; // 상단 여백
      const top = searchWrapperRef.current.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: "smooth" });
    }
  };

  return (
    <div ref={searchWrapperRef} className="max-w-2xl mx-auto px-4 -mt-2 mb-8">
      <div className="relative neon-border rounded-2xl">
        <div className="glass flex items-center px-5 py-4">
          <Search className="w-5 h-5 dark:text-zinc-400 text-zinc-500 shrink-0" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => {
              isTypingRef.current = true;
              setQuery(e.target.value);
            }}
            onFocus={handleFocus}
            onBlur={() => { isTypingRef.current = false; }}
            placeholder="어떤 AI 도구를 찾고 계신가요?"
            className="w-full ml-3 bg-transparent outline-none text-base
              dark:text-white text-zinc-900
              dark:placeholder-zinc-500 placeholder-zinc-400"
          />
          {query && (
            <button
              onClick={() => setQuery("")}
              className="ml-2 p-1 rounded-lg dark:hover:bg-white/10 hover:bg-black/5 transition-colors"
            >
              <X className="w-4 h-4 dark:text-zinc-400 text-zinc-500" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
