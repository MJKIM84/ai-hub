import * as cheerio from "cheerio";

export interface DiscoveredItem {
  url: string;
  title?: string;
  description?: string;
}

/**
 * Product Hunt — AI 태그 제품 페이지에서 링크 추출
 */
export async function fetchProductHuntAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const res = await fetch("https://www.producthunt.com/topics/artificial-intelligence", {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
        Accept: "text/html",
      },
      signal: AbortSignal.timeout(10000),
    });
    if (!res.ok) return items;

    const html = await res.text();
    const $ = cheerio.load(html);

    // Product Hunt 제품 링크 추출
    $('a[href*="/posts/"]').each((_, el) => {
      const href = $(el).attr("href");
      if (!href) return;
      const fullUrl = href.startsWith("http")
        ? href
        : `https://www.producthunt.com${href}`;
      const title = $(el).text().trim();
      if (fullUrl && !items.some((i) => i.url === fullUrl)) {
        items.push({ url: fullUrl, title: title || undefined });
      }
    });

    // 외부 서비스 URL 추출 시도
    $('a[rel="nofollow"]').each((_, el) => {
      const href = $(el).attr("href");
      if (
        href &&
        href.startsWith("http") &&
        !href.includes("producthunt.com")
      ) {
        const title = $(el).text().trim();
        if (!items.some((i) => i.url === href)) {
          items.push({ url: href, title: title || undefined });
        }
      }
    });
  } catch (err) {
    console.error("[Source:ProductHunt] Error:", err);
  }
  return items.slice(0, 10);
}

/**
 * Hacker News — Algolia API로 AI 관련 "Show HN" 검색
 */
export async function fetchHackerNewsAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const query = encodeURIComponent("Show HN AI");
    const res = await fetch(
      `https://hn.algolia.com/api/v1/search_by_date?query=${query}&tags=show_hn&hitsPerPage=10`,
      { signal: AbortSignal.timeout(10000) }
    );
    if (!res.ok) return items;

    const data = await res.json();
    for (const hit of data.hits || []) {
      const url = hit.url;
      if (url && url.startsWith("http")) {
        items.push({
          url,
          title: hit.title || undefined,
          description: hit.story_text?.substring(0, 300) || undefined,
        });
      }
    }
  } catch (err) {
    console.error("[Source:HackerNews] Error:", err);
  }
  return items.slice(0, 10);
}

/**
 * GitHub Trending — AI/ML 카테고리 트렌딩 리포에서 홈페이지 URL 추출
 */
export async function fetchGitHubTrendingAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const res = await fetch(
      "https://github.com/trending?since=daily&spoken_language_code=en",
      {
        headers: {
          "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
          Accept: "text/html",
        },
        signal: AbortSignal.timeout(10000),
      }
    );
    if (!res.ok) return items;

    const html = await res.text();
    const $ = cheerio.load(html);

    const aiKeywords = [
      "ai", "ml", "llm", "gpt", "neural", "deep-learning",
      "machine-learning", "transformer", "diffusion", "chatbot",
    ];

    $("article.Box-row").each((_, el) => {
      const repoLink = $(el).find("h2 a").attr("href");
      const desc = $(el).find("p").text().trim().toLowerCase();
      const repoName = repoLink?.toLowerCase() || "";

      // AI 관련 필터
      const isAI =
        aiKeywords.some((kw) => desc.includes(kw)) ||
        aiKeywords.some((kw) => repoName.includes(kw));

      if (isAI && repoLink) {
        const fullUrl = `https://github.com${repoLink}`;
        items.push({
          url: fullUrl,
          title: repoLink.replace(/^\//, ""),
          description: $(el).find("p").text().trim() || undefined,
        });
      }
    });
  } catch (err) {
    console.error("[Source:GitHub] Error:", err);
  }
  return items.slice(0, 5);
}

/**
 * There Is An AI For That — AI 툴 디렉토리에서 링크 추출
 */
export async function fetchTheresAnAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const res = await fetch("https://theresanaiforthat.com/new/", {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
        Accept: "text/html",
      },
      signal: AbortSignal.timeout(10000),
    });
    if (!res.ok) return items;

    const html = await res.text();
    const $ = cheerio.load(html);

    // 최근 추가된 AI 툴 링크 추출
    $("a.ai_link, a[href*='/ai/']").each((_, el) => {
      const href = $(el).attr("href");
      if (!href) return;
      const fullUrl = href.startsWith("http")
        ? href
        : `https://theresanaiforthat.com${href}`;
      const title = $(el).text().trim();
      if (!items.some((i) => i.url === fullUrl)) {
        items.push({ url: fullUrl, title: title || undefined });
      }
    });

    // 외부 링크 (실제 서비스 URL)
    $('a[target="_blank"][rel*="nofollow"]').each((_, el) => {
      const href = $(el).attr("href");
      if (
        href &&
        href.startsWith("http") &&
        !href.includes("theresanaiforthat.com")
      ) {
        const title = $(el).text().trim();
        if (!items.some((i) => i.url === href)) {
          items.push({ url: href, title: title || undefined });
        }
      }
    });
  } catch (err) {
    console.error("[Source:TheresAnAI] Error:", err);
  }
  return items.slice(0, 10);
}

// 소스 타입과 함수 매핑
export const SOURCE_FETCHERS: Record<
  string,
  () => Promise<DiscoveredItem[]>
> = {
  producthunt: fetchProductHuntAI,
  hackernews: fetchHackerNewsAI,
  github: fetchGitHubTrendingAI,
  theresanai: fetchTheresAnAI,
};
