"use client";

import { Search, X, Loader2 } from "lucide-react";
import { useState, useRef } from "react";
import { useRouter, useSearchParams } from "next/navigation";

export function SearchBar({ initialQuery }: { initialQuery?: string }) {
  const [query, setQuery] = useState(initialQuery || "");
  const [isSearching, setIsSearching] = useState(false);
  const router = useRouter();
  const searchParams = useSearchParams();
  const hasScrolled = useRef(false);
  const searchWrapperRef = useRef<HTMLDivElement>(null);
  const debounceTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  // searchParams를 ref로 최신 상태 유지
  const searchParamsRef = useRef(searchParams);
  searchParamsRef.current = searchParams;

  const executeSearch = (value: string) => {
    const params = new URLSearchParams(searchParamsRef.current.toString());
    if (value.trim()) {
      params.set("q", value.trim());
    } else {
      params.delete("q");
    }
    params.delete("page");
    router.push(`/?${params.toString()}`, { scroll: false });
    setTimeout(() => setIsSearching(false), 500);
  };

  // 키 입력 핸들러 — 디바운스 검색
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setQuery(value);

    if (debounceTimer.current) {
      clearTimeout(debounceTimer.current);
    }

    setIsSearching(true);
    debounceTimer.current = setTimeout(() => {
      executeSearch(value);
    }, 300);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (debounceTimer.current) {
      clearTimeout(debounceTimer.current);
    }
    setIsSearching(true);
    executeSearch(query);
  };

  const handleClear = () => {
    setQuery("");
    if (debounceTimer.current) {
      clearTimeout(debounceTimer.current);
    }
    setIsSearching(true);
    executeSearch("");
  };

  const handleFocus = () => {
    if (hasScrolled.current) return;
    hasScrolled.current = true;

    if (searchWrapperRef.current) {
      const offset = 20;
      const top = searchWrapperRef.current.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: "smooth" });
    }
  };

  return (
    <div ref={searchWrapperRef} className="max-w-2xl mx-auto px-4 -mt-2 mb-8">
      <form onSubmit={handleSubmit} className="relative neon-border rounded-2xl">
        <div className="glass flex items-center px-3 py-3 sm:px-5 sm:py-4">
          {isSearching ? (
            <Loader2 className="w-5 h-5 text-neon-blue shrink-0 animate-spin" />
          ) : (
            <Search className="w-5 h-5 dark:text-zinc-400 text-zinc-500 shrink-0" />
          )}
          <input
            type="text"
            value={query}
            onChange={handleChange}
            onFocus={handleFocus}
            placeholder="어떤 AI 도구를 찾고 계신가요?"
            className="w-full ml-3 bg-transparent outline-none text-base
              dark:text-white text-zinc-900
              dark:placeholder-zinc-500 placeholder-zinc-400"
          />
          {query && (
            <button
              type="button"
              onClick={handleClear}
              className="ml-2 p-1 rounded-lg dark:hover:bg-white/10 hover:bg-black/5 transition-colors"
            >
              <X className="w-4 h-4 dark:text-zinc-400 text-zinc-500" />
            </button>
          )}
        </div>
      </form>
    </div>
  );
}
