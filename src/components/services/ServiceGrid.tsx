"use client";

import { useState, useEffect, useRef } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { Loader2, ChevronDown } from "lucide-react";
import { ServiceCard } from "./ServiceCard";
import { SortSelector } from "../filters/SortSelector";
import type { Service } from "@/types/service";

interface ServiceGridProps {
  initialServices: Service[];
  totalCount: number;
  todayCount?: number;
  currentPage: number;
  hasMore: boolean;
  currentSort?: string;
  currentFilter?: string;
}

export function ServiceGrid({
  initialServices,
  totalCount,
  todayCount,
  currentPage,
  hasMore,
  currentSort,
  currentFilter,
}: ServiceGridProps) {
  const [services, setServices] = useState<Service[]>(initialServices);
  const [page, setPage] = useState(currentPage);
  const [loading, setLoading] = useState(false);
  const [canLoadMore, setCanLoadMore] = useState(hasMore);
  const searchParams = useSearchParams();
  const router = useRouter();
  const prevInitialRef = useRef(initialServices);

  // Reset when server data changes (search/filter/sort)
  useEffect(() => {
    const prevIds = prevInitialRef.current.map(s => s.id).join(',');
    const newIds = initialServices.map(s => s.id).join(',');
    if (prevIds !== newIds) {
      setServices(initialServices);
      setPage(1);
      setCanLoadMore(hasMore);
      prevInitialRef.current = initialServices;
    }
  }, [initialServices, hasMore]);

  // 스크롤 위치 복원
  useEffect(() => {
    const savedY = sessionStorage.getItem("scrollY");
    if (savedY) {
      const y = parseInt(savedY, 10);
      requestAnimationFrame(() => {
        window.scrollTo(0, y);
      });
      sessionStorage.removeItem("scrollY");
    }
  }, []);

  const loadMore = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams(searchParams.toString());
      params.set("page", String(page + 1));
      const res = await fetch(`/api/services?${params.toString()}`);
      const data = await res.json();
      setServices((prev) => [...prev, ...data.items]);
      setPage(page + 1);
      setCanLoadMore(data.hasMore);
    } catch (error) {
      console.error("Failed to load more:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleVote = (serviceId: string) => {
    setServices((prev) =>
      prev.map((s) =>
        s.id === serviceId ? { ...s, upvotes: s.upvotes + 1 } : s
      )
    );
  };

  return (
    <div id="service-grid" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between mb-4 sm:mb-6">
        <div className="flex items-center gap-2 sm:gap-3">
          {currentFilter === "today" ? (
            <button
              onClick={() => {
                const params = new URLSearchParams(searchParams.toString());
                params.delete("filter");
                router.push(`/?${params.toString()}`);
              }}
              className="text-sm dark:text-zinc-400 text-zinc-500 hover:text-neon-blue transition-colors cursor-pointer"
            >
              ← 전체 <span className="dark:text-white text-zinc-900 font-semibold">{totalCount}</span>개 보기
            </button>
          ) : (
            <p className="text-sm dark:text-zinc-500 text-zinc-400 whitespace-nowrap">
              총 <span className="dark:text-white text-zinc-900 font-semibold">{totalCount}</span>개의 서비스
            </p>
          )}
          {todayCount != null && todayCount > 0 && (
            <button
              onClick={() => {
                const params = new URLSearchParams(searchParams.toString());
                if (currentFilter === "today") {
                  params.delete("filter");
                } else {
                  params.set("filter", "today");
                }
                router.push(`/?${params.toString()}`);
              }}
              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium whitespace-nowrap
                transition-all duration-200 cursor-pointer
                ${currentFilter === "today"
                  ? "bg-emerald-500/25 text-emerald-400 ring-1 ring-emerald-500/40"
                  : "bg-emerald-500/15 text-emerald-500 hover:bg-emerald-500/25 animate-pulse"
                }`}
            >
              🆕 오늘 {todayCount}개 등록
            </button>
          )}
        </div>
        <SortSelector currentSort={currentSort} />
      </div>

      {services.length === 0 ? (
        <div className="text-center py-20">
          <p className="text-lg dark:text-zinc-400 text-zinc-500 mb-2">
            검색 결과가 없습니다
          </p>
          <p className="text-sm dark:text-zinc-500 text-zinc-400">
            다른 키워드로 검색해보세요
          </p>
        </div>
      ) : (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3 sm:gap-5">
            {services.map((service) => (
              <ServiceCard
                key={service.id}
                service={service}
                onVote={handleVote}
              />
            ))}
          </div>

          {canLoadMore && (
            <div className="flex justify-center mt-10">
              <button
                onClick={loadMore}
                disabled={loading}
                className="flex items-center gap-2 px-6 py-3 rounded-xl text-sm font-medium
                  glass dark:hover:bg-white/10 hover:bg-black/10
                  dark:text-zinc-300 text-zinc-600
                  disabled:opacity-50 transition-all duration-200"
              >
                {loading ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <ChevronDown className="w-4 h-4" />
                )}
                {loading ? "불러오는 중..." : "더 보기"}
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
}
