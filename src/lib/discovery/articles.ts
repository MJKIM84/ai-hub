import * as cheerio from "cheerio";
import { prisma } from "@/lib/prisma";
import { translateToKorean, isEnglishText } from "@/lib/translator";

interface ArticleItem {
  title: string;
  url: string;
  sourceName: string;
  publishedAt?: Date;
}

/**
 * Google News RSS에서 서비스 관련 기사 검색
 */
async function fetchGoogleNewsRSS(
  query: string
): Promise<ArticleItem[]> {
  const items: ArticleItem[] = [];
  try {
    const encodedQuery = encodeURIComponent(`${query} AI`);
    const rssUrl = `https://news.google.com/rss/search?q=${encodedQuery}&hl=en&gl=US&ceid=US:en`;

    const res = await fetch(rssUrl, {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
        Accept: "application/rss+xml, text/xml, application/xml",
      },
      signal: AbortSignal.timeout(5000),
    });

    if (!res.ok) return items;

    const xml = await res.text();
    const $ = cheerio.load(xml, { xml: true });

    $("item").each((i, el) => {
      if (i >= 3) return false; // 서비스당 최대 3건

      const title = $(el).find("title").text().trim();
      const link = $(el).find("link").text().trim();
      const pubDate = $(el).find("pubDate").text().trim();
      const source = $(el).find("source").text().trim();

      if (!title || !link) return;

      // 최근 7일 기사만
      if (pubDate) {
        const published = new Date(pubDate);
        const sevenDaysAgo = new Date();
        sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7);
        if (published < sevenDaysAgo) return;
      }

      items.push({
        title,
        url: link,
        sourceName: source || "Google News",
        publishedAt: pubDate ? new Date(pubDate) : undefined,
      });
    });
  } catch (err) {
    console.error(`[Articles] RSS fetch error for "${query}":`, err);
  }
  return items;
}

/**
 * 관련 기사 크롤링 메인 오케스트레이터
 * 모든 서비스에 대해 Google News RSS로 기사 검색 후 DB에 저장
 */
export async function runArticleCrawl(offset = 0, limit = 15): Promise<{
  servicesChecked: number;
  articlesCreated: number;
  errors: string[];
  totalServices: number;
}> {
  const result = {
    servicesChecked: 0,
    articlesCreated: 0,
    errors: [] as string[],
    totalServices: 0,
  };

  try {
    result.totalServices = await prisma.service.count();

    // 서비스 조회 (offset/limit으로 배치 처리, Vercel 60초 제한 고려)
    const services = await prisma.service.findMany({
      select: { id: true, name: true },
      orderBy: { score: "desc" },
      skip: offset,
      take: limit,
    });

    console.log(`[Articles] ${services.length}개 서비스 기사 크롤 시작`);

    for (const service of services) {
      result.servicesChecked++;

      try {
        const articles = await fetchGoogleNewsRSS(service.name);

        for (const article of articles) {
          try {
            // 제목 한글 번역 (영어인 경우만)
            let titleKo: string | null = null;
            if (isEnglishText(article.title)) {
              titleKo = await translateToKorean(article.title);
            }

            // upsert (중복 방지: serviceId + url 유니크 제약)
            await prisma.article.upsert({
              where: {
                serviceId_url: {
                  serviceId: service.id,
                  url: article.url,
                },
              },
              update: {
                titleKo: titleKo || undefined,
              },
              create: {
                serviceId: service.id,
                title: article.title,
                titleKo,
                url: article.url,
                sourceName: article.sourceName,
                publishedAt: article.publishedAt,
              },
            });

            result.articlesCreated++;
          } catch (err) {
            // 개별 기사 저장 에러 (중복 등) — 무시
            const msg = err instanceof Error ? err.message : String(err);
            if (!msg.includes("Unique constraint")) {
              result.errors.push(`[${service.name}] ${article.url}: ${msg}`);
            }
          }
        }

        // Rate limit 방지 (서비스 간 간격)
        await new Promise((r) => setTimeout(r, 300));
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        result.errors.push(`[${service.name}] ${msg}`);
      }
    }

    // 7일 이상 된 기사 정리
    const weekAgo = new Date();
    weekAgo.setDate(weekAgo.getDate() - 14); // 2주 넘은 기사 삭제
    await prisma.article.deleteMany({
      where: { createdAt: { lt: weekAgo } },
    });
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    result.errors.push(`Fatal: ${msg}`);
  }

  console.log(
    `[Articles] 완료: ${result.servicesChecked}개 서비스 확인, ${result.articlesCreated}개 기사 저장, ${result.errors.length}개 에러`
  );

  return result;
}
