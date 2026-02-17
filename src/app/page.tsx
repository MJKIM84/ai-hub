import { prisma } from "@/lib/prisma";
import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { HeroSection } from "@/components/hero/HeroSection";
import { SearchBar } from "@/components/hero/SearchBar";
import { CategoryFilter } from "@/components/filters/CategoryFilter";
import { ServiceGrid } from "@/components/services/ServiceGrid";
import { calculateRelevanceScore } from "@/lib/search";

export const dynamic = "force-dynamic";

const ITEMS_PER_PAGE = 12;

interface PageProps {
  searchParams: Promise<{
    q?: string;
    category?: string;
    sort?: string;
    page?: string;
    filter?: string;
  }>;
}

export default async function HomePage({ searchParams }: PageProps) {
  const params = await searchParams;
  const page = Math.max(1, parseInt(params.page || "1", 10));
  const sort = params.sort || "gravity";

  // 오늘 자정(KST) 기준 시작 시각 계산
  const todayStart = new Date();
  todayStart.setHours(todayStart.getHours() + 9); // UTC → KST
  todayStart.setHours(0, 0, 0, 0);
  todayStart.setHours(todayStart.getHours() - 9); // KST → UTC

  const where: Record<string, unknown> = {};
  if (params.category) where.category = params.category;
  if (params.filter === "today") {
    where.createdAt = { gte: todayStart };
  }
  if (params.q) {
    where.OR = [
      { name: { contains: params.q, mode: "insensitive" } },
      { nameKo: { contains: params.q, mode: "insensitive" } },
      { description: { contains: params.q, mode: "insensitive" } },
      { descriptionKo: { contains: params.q, mode: "insensitive" } },
      { tagline: { contains: params.q, mode: "insensitive" } },
      { tags: { contains: params.q, mode: "insensitive" } },
      { category: { contains: params.q, mode: "insensitive" } },
    ];
  }

  let orderBy: Record<string, string> = {};
  switch (sort) {
    case "newest": orderBy = { createdAt: "desc" }; break;
    case "popular": orderBy = { clicks: "desc" }; break;
    case "name": orderBy = { name: "asc" }; break;
    default: orderBy = { score: "desc" };
  }

  const [items, total, categoryCounts, todayCount] = await Promise.all([
    prisma.service.findMany({
      where: where as never,
      orderBy: orderBy as never,
      skip: (page - 1) * ITEMS_PER_PAGE,
      take: ITEMS_PER_PAGE,
    }),
    prisma.service.count({ where: where as never }),
    prisma.service.groupBy({
      by: ["category"],
      _count: { id: true },
    }),
    prisma.service.count({
      where: { createdAt: { gte: todayStart } },
    }),
  ]);

  let sortedItems = items;
  if (params.q && items.length > 0) {
    sortedItems = [...items].sort((a, b) => {
      const scoreA = calculateRelevanceScore(params.q!, a);
      const scoreB = calculateRelevanceScore(params.q!, b);
      return scoreB - scoreA;
    });
  }

  const countMap: Record<string, number> = {};
  for (const c of categoryCounts) {
    countMap[c.category] = c._count.id;
  }

  const totalPages = Math.ceil(total / ITEMS_PER_PAGE);

  return (
    <>
      <Header />
      <main className="min-h-screen">
        <HeroSection />
        <SearchBar initialQuery={params.q} />
        <CategoryFilter activeCategory={params.category} categoryCounts={countMap} />
        <ServiceGrid
          initialServices={JSON.parse(JSON.stringify(sortedItems))}
          totalCount={total}
          todayCount={todayCount}
          currentPage={page}
          hasMore={page < totalPages}
          currentSort={sort}
          currentFilter={params.filter}
        />
      </main>
      <Footer />
    </>
  );
}
