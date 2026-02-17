"use client";

import { useState, useEffect } from "react";
import { Newspaper, ExternalLink, Loader2 } from "lucide-react";

interface Article {
  id: string;
  title: string;
  titleKo: string | null;
  url: string;
  sourceName: string;
  publishedAt: string | null;
}

interface RelatedArticlesProps {
  serviceId: string;
}

function formatArticleDate(dateStr: string | null): string {
  if (!dateStr) return "";
  const d = new Date(dateStr);
  const now = new Date();
  const diff = now.getTime() - d.getTime();
  const hours = Math.floor(diff / (1000 * 60 * 60));
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));

  if (hours < 1) return "방금 전";
  if (hours < 24) return `${hours}시간 전`;
  if (days < 7) return `${days}일 전`;
  return d.toLocaleDateString("ko-KR", { month: "short", day: "numeric" });
}

export function RelatedArticles({ serviceId }: RelatedArticlesProps) {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchArticles() {
      try {
        const res = await fetch(`/api/articles?serviceId=${serviceId}`);
        if (!res.ok) return;
        const data = await res.json();
        setArticles(data.items || []);
      } catch {
        // 무시
      } finally {
        setLoading(false);
      }
    }
    fetchArticles();
  }, [serviceId]);

  // 로딩 중이거나 기사 없으면 숨김
  if (loading) {
    return (
      <div className="glass p-6 mt-6">
        <div className="flex items-center gap-2 mb-4">
          <Newspaper className="w-5 h-5 dark:text-zinc-400 text-zinc-500" />
          <h3 className="text-lg font-semibold dark:text-white text-zinc-900">
            관련 기사
          </h3>
        </div>
        <div className="flex items-center justify-center py-4">
          <Loader2 className="w-5 h-5 animate-spin dark:text-zinc-500 text-zinc-400" />
        </div>
      </div>
    );
  }

  if (articles.length === 0) return null;

  return (
    <div className="glass p-6 mt-6">
      <div className="flex items-center gap-2 mb-4">
        <Newspaper className="w-5 h-5 dark:text-neon-blue text-blue-500" />
        <h3 className="text-lg font-semibold dark:text-white text-zinc-900">
          관련 기사
        </h3>
        <span className="text-xs dark:text-zinc-500 text-zinc-400">
          {articles.length}건
        </span>
      </div>

      <div className="space-y-3">
        {articles.map((article) => (
          <a
            key={article.id}
            href={article.url}
            target="_blank"
            rel="noopener noreferrer"
            className="block p-3 rounded-xl
              dark:bg-white/5 bg-black/5
              dark:hover:bg-white/10 hover:bg-black/10
              transition-all duration-200 group"
          >
            <div className="flex items-start justify-between gap-3">
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium dark:text-white text-zinc-900
                  group-hover:text-neon-blue transition-colors line-clamp-2">
                  {article.titleKo || article.title}
                </p>
                {article.titleKo && (
                  <p className="text-xs dark:text-zinc-500 text-zinc-400 mt-1 line-clamp-1">
                    {article.title}
                  </p>
                )}
                <div className="flex items-center gap-2 mt-1.5">
                  <span className="text-xs dark:text-zinc-500 text-zinc-400">
                    {article.sourceName}
                  </span>
                  {article.publishedAt && (
                    <>
                      <span className="text-xs dark:text-zinc-600 text-zinc-300">·</span>
                      <span className="text-xs dark:text-zinc-500 text-zinc-400">
                        {formatArticleDate(article.publishedAt)}
                      </span>
                    </>
                  )}
                </div>
              </div>
              <ExternalLink className="w-4 h-4 shrink-0 dark:text-zinc-600 text-zinc-400
                group-hover:text-neon-blue transition-colors mt-0.5" />
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}
