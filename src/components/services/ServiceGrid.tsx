"use client";

import { useState, useEffect, useRef } from "react";
import { useSearchParams } from "next/navigation";
import { Loader2, ChevronDown } from "lucide-react";
import { ServiceCard } from "./ServiceCard";
import { SortSelector } from "../filters/SortSelector";
import type { Service } from "@/types/service";

interface ServiceGridProps {
  initialServices: Service[];
  totalCount: number;
  currentPage: number;
  hasMore: boolean;
  currentSort?: string;
}

export function ServiceGrid({
  initialServices,
  totalCount,
  currentPage,
  hasMore,
  currentSort,
}: ServiceGridProps) {
  const [services, setServices] = useState<Service[]>(initialServices);
  const [page, setPage] = useState(currentPage);
  const [loading, setLoading] = useState(false);
  const [canLoadMore, setCanLoadMore] = useState(hasMore);
  const searchParams = useSearchParams();
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
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex items-center justify-between mb-6">
        <p className="text-sm dark:text-zinc-500 text-zinc-400">
          총 <span className="dark:text-white text-zinc-900 font-semibold">{totalCount}</span>개의 서비스
        </p>
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
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
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
