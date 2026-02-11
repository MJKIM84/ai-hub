"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { ArrowUpDown } from "lucide-react";

const SORT_OPTIONS = [
  { id: "gravity", label: "추천순" },
  { id: "newest", label: "최신순" },
  { id: "popular", label: "인기순" },
  { id: "name", label: "이름순" },
] as const;

export function SortSelector({ currentSort }: { currentSort?: string }) {
  const router = useRouter();
  const searchParams = useSearchParams();

  const setSort = (sortId: string) => {
    const params = new URLSearchParams(searchParams.toString());
    if (sortId === "gravity") {
      params.delete("sort");
    } else {
      params.set("sort", sortId);
    }
    params.delete("page");
    router.push(`/?${params.toString()}`);
  };

  const active = currentSort || "gravity";

  return (
    <div className="flex items-center gap-2">
      <ArrowUpDown className="w-4 h-4 dark:text-zinc-500 text-zinc-400" />
      <div className="flex gap-1">
        {SORT_OPTIONS.map((opt) => (
          <button
            key={opt.id}
            onClick={() => setSort(opt.id)}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-200
              ${active === opt.id
                ? "dark:bg-white/10 bg-black/10 dark:text-white text-zinc-900"
                : "dark:text-zinc-500 text-zinc-400 dark:hover:text-zinc-300 hover:text-zinc-600"
              }`}
          >
            {opt.label}
          </button>
        ))}
      </div>
    </div>
  );
}
