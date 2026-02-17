import * as cheerio from "cheerio";

export interface DiscoveredItem {
  url: string;
  title?: string;
  description?: string;
}

const MIN_GITHUB_STARS = 1000;

/**
 * GitHub 스타 수 문자열을 숫자로 변환 (e.g. "1.2k" → 1200, "500" → 500)
 */
function parseStarCount(text: string): number {
  const cleaned = text.trim().replace(/,/g, "").toLowerCase();
  if (cleaned.endsWith("k")) {
    return Math.round(parseFloat(cleaned.replace("k", "")) * 1000);
  }
  return parseInt(cleaned, 10) || 0;
}

/**
 * GitHub API로 레포 상세 정보 조회 (스타 수 + 홈페이지 URL)
 */
async function fetchGitHubRepoInfo(
  owner: string,
  repo: string
): Promise<{ stars: number; homepage: string | null } | null> {
  try {
    const headers: Record<string, string> = {
      Accept: "application/vnd.github.v3+json",
      "User-Agent": "AI-Hub-Bot/1.0",
    };
    const token = process.env.GITHUB_TOKEN;
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }

    const res = await fetch(`https://api.github.com/repos/${owner}/${repo}`, {
      headers,
      signal: AbortSignal.timeout(8000),
    });
    if (!res.ok) return null;

    const data = await res.json();
    return {
      stars: data.stargazers_count || 0,
      homepage: data.homepage || null,
    };
  } catch {
    return null;
  }
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
 * 1000+ 스타만 필터링, 홈페이지 URL이 있으면 해당 URL 사용
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
      "agent", "copilot", "openai", "anthropic", "langchain",
    ];

    // 후보 수집
    const candidates: { owner: string; repo: string; desc: string; pageStars: number }[] = [];

    $("article.Box-row").each((_, el) => {
      const repoLink = $(el).find("h2 a").attr("href");
      const desc = $(el).find("p").text().trim().toLowerCase();
      const repoName = repoLink?.toLowerCase() || "";

      // AI 관련 필터
      const isAI =
        aiKeywords.some((kw) => desc.includes(kw)) ||
        aiKeywords.some((kw) => repoName.includes(kw));

      if (!isAI || !repoLink) return;

      // 페이지에서 스타 수 파싱 (초기 필터)
      const starEl = $(el).find('a[href$="/stargazers"]').text().trim() ||
                     $(el).find('svg[aria-label="star"]').parent().text().trim();
      const pageStars = parseStarCount(starEl);

      // 페이지에서 보이는 스타 수로 1차 필터 (명확히 적은 건 스킵)
      if (pageStars > 0 && pageStars < MIN_GITHUB_STARS) return;

      const parts = repoLink.replace(/^\//, "").split("/");
      if (parts.length >= 2) {
        candidates.push({
          owner: parts[0],
          repo: parts[1],
          desc: $(el).find("p").text().trim(),
          pageStars,
        });
      }
    });

    // GitHub API로 정확한 스타 수 + 홈페이지 URL 조회
    for (const cand of candidates.slice(0, 10)) {
      const info = await fetchGitHubRepoInfo(cand.owner, cand.repo);

      if (info && info.stars >= MIN_GITHUB_STARS) {
        // 홈페이지 URL이 있으면 실제 서비스 URL 사용, 없으면 GitHub URL
        const serviceUrl = info.homepage && info.homepage.startsWith("http")
          ? info.homepage
          : `https://github.com/${cand.owner}/${cand.repo}`;

        items.push({
          url: serviceUrl,
          title: `${cand.owner}/${cand.repo}`,
          description: cand.desc || undefined,
        });

        console.log(`[Source:GitHub] ✅ ${cand.owner}/${cand.repo} (⭐${info.stars}) → ${serviceUrl}`);
      } else {
        console.log(`[Source:GitHub] ⏭️ ${cand.owner}/${cand.repo} (⭐${info?.stars || cand.pageStars}) — 스킵`);
      }

      // Rate limit 방지
      await new Promise((r) => setTimeout(r, 200));
    }
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

/**
 * Futurepedia — AI 툴 디렉토리에서 최신 서비스 추출
 */
export async function fetchFuturepediaAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const res = await fetch("https://www.futurepedia.io/ai-tools", {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
        Accept: "text/html",
      },
      signal: AbortSignal.timeout(10000),
    });
    if (!res.ok) return items;

    const html = await res.text();
    const $ = cheerio.load(html);

    // 외부 서비스 링크 추출
    $('a[href*="http"]').each((_, el) => {
      const href = $(el).attr("href");
      if (!href || href.includes("futurepedia.io") || href.includes("google.com") ||
          href.includes("twitter.com") || href.includes("facebook.com") ||
          href.includes("linkedin.com") || href.includes("youtube.com")) return;
      const title = $(el).text().trim();
      if (title.length > 1 && title.length < 100 && !items.some((i) => i.url === href)) {
        items.push({ url: href, title: title || undefined });
      }
    });

    // 내부 AI 툴 페이지 링크도 추출
    $('a[href*="/tool/"]').each((_, el) => {
      const href = $(el).attr("href");
      if (!href) return;
      const fullUrl = href.startsWith("http") ? href : `https://www.futurepedia.io${href}`;
      const title = $(el).text().trim();
      if (!items.some((i) => i.url === fullUrl)) {
        items.push({ url: fullUrl, title: title || undefined });
      }
    });
  } catch (err) {
    console.error("[Source:Futurepedia] Error:", err);
  }
  return items.slice(0, 10);
}

/**
 * Toolify — AI 툴 디렉토리에서 최신 서비스 추출
 */
export async function fetchToolifyAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const res = await fetch("https://www.toolify.ai/", {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
        Accept: "text/html",
      },
      signal: AbortSignal.timeout(10000),
    });
    if (!res.ok) return items;

    const html = await res.text();
    const $ = cheerio.load(html);

    // 외부 서비스 링크 추출
    $('a[href*="http"]').each((_, el) => {
      const href = $(el).attr("href");
      if (!href || href.includes("toolify.ai") || href.includes("google.com") ||
          href.includes("twitter.com") || href.includes("facebook.com") ||
          href.includes("linkedin.com")) return;
      const title = $(el).text().trim();
      if (title.length > 1 && title.length < 100 && !items.some((i) => i.url === href)) {
        items.push({ url: href, title: title || undefined });
      }
    });

    // 내부 AI 툴 페이지 링크 추출
    $('a[href*="/tool/"], a[href*="/ai/"]').each((_, el) => {
      const href = $(el).attr("href");
      if (!href) return;
      const fullUrl = href.startsWith("http") ? href : `https://www.toolify.ai${href}`;
      const title = $(el).text().trim();
      if (!items.some((i) => i.url === fullUrl)) {
        items.push({ url: fullUrl, title: title || undefined });
      }
    });
  } catch (err) {
    console.error("[Source:Toolify] Error:", err);
  }
  return items.slice(0, 10);
}

/**
 * BensBites — AI 뉴스/서비스 디렉토리에서 최신 서비스 추출
 */
export async function fetchBensBitesAI(): Promise<DiscoveredItem[]> {
  const items: DiscoveredItem[] = [];
  try {
    const res = await fetch("https://bensbites.com/trending", {
      headers: {
        "User-Agent": "Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)",
        Accept: "text/html",
      },
      signal: AbortSignal.timeout(10000),
    });
    if (!res.ok) return items;

    const html = await res.text();
    const $ = cheerio.load(html);

    // 외부 서비스 링크 추출
    $('a[href*="http"]').each((_, el) => {
      const href = $(el).attr("href");
      if (!href || href.includes("bensbites.com") || href.includes("google.com") ||
          href.includes("twitter.com") || href.includes("facebook.com") ||
          href.includes("linkedin.com") || href.includes("substack.com")) return;
      const title = $(el).text().trim();
      if (title.length > 1 && title.length < 100 && !items.some((i) => i.url === href)) {
        items.push({ url: href, title: title || undefined });
      }
    });
  } catch (err) {
    console.error("[Source:BensBites] Error:", err);
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
  futurepedia: fetchFuturepediaAI,
  toolify: fetchToolifyAI,
  bensbites: fetchBensBitesAI,
};
