"use client";

import { Search, X } from "lucide-react";
import { useState, useCallback, useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";

export function SearchBar({ initialQuery }: { initialQuery?: string }) {
  const [query, setQuery] = useState(initialQuery || "");
  const router = useRouter();
  const searchParams = useSearchParams();

  const updateSearch = useCallback(
    (value: string) => {
      const params = new URLSearchParams(searchParams.toString());
      if (value) {
        params.set("q", value);
      } else {
        params.delete("q");
      }
      params.delete("page");
      router.push(`/?${params.toString()}`);
    },
    [router, searchParams]
  );

  useEffect(() => {
    const timer = setTimeout(() => {
      updateSearch(query);
    }, 300);
    return () => clearTimeout(timer);
  }, [query, updateSearch]);

  return (
    <div className="max-w-2xl mx-auto px-4 -mt-2 mb-8">
      <div className="relative neon-border rounded-2xl">
        <div className="glass flex items-center px-5 py-4">
          <Search className="w-5 h-5 dark:text-zinc-400 text-zinc-500 shrink-0" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
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
