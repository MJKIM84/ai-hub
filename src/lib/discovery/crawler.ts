import { prisma } from "@/lib/prisma";
import { scrapeServiceMetadata } from "@/lib/scraper";
import { suggestCategory } from "@/lib/categorizer";
import { calculateGravityScore } from "@/lib/ranking";
import { createSlug } from "@/lib/utils";
import { translateService } from "@/lib/translator";
import { normalizeUrl, extractDomain, checkDuplicate } from "./dedup";
import { SOURCE_FETCHERS, type DiscoveredItem } from "./sources";
import { validateCrawledServices, type ValidationReport } from "./validator";

interface CrawlResult {
  crawlRunId: string;
  sourcesChecked: number;
  urlsDiscovered: number;
  urlsNew: number;
  urlsDuplicate: number;
  servicesCreated: number;
  createdServiceIds: string[];
  validation: ValidationReport | null;
  errors: string[];
}

/**
 * 매일 크롤링 실행 오케스트레이터
 * - 활성 소스를 priority 순으로 조회
 * - 소스별 URL 추출 → 중복 확인 → 신규면 메타데이터 추출 → 자동 승인
 */
export async function runDailyCrawl(): Promise<CrawlResult> {
  // 1. CrawlRun 레코드 생성
  const crawlRun = await prisma.crawlRun.create({
    data: { status: "running" },
  });

  const result: CrawlResult = {
    crawlRunId: crawlRun.id,
    sourcesChecked: 0,
    urlsDiscovered: 0,
    urlsNew: 0,
    urlsDuplicate: 0,
    servicesCreated: 0,
    createdServiceIds: [],
    validation: null,
    errors: [],
  };

  try {
    // 2. 활성 소스 조회 (priority 내림차순, 최대 5개 — 웹 소스 우선)
    const sources = await prisma.discoverySource.findMany({
      where: { isActive: true },
      orderBy: { priority: "desc" },
      take: 5,
    });

    // 소스가 없으면 기본 소스 시드
    if (sources.length === 0) {
      await seedDefaultSources();
      const seeded = await prisma.discoverySource.findMany({
        where: { isActive: true },
        orderBy: { priority: "desc" },
        take: 5,
      });
      sources.push(...seeded);
    }

    // 3. 소스별 처리
    for (const source of sources) {
      result.sourcesChecked++;

      try {
        const fetcher = SOURCE_FETCHERS[source.type];
        if (!fetcher) {
          result.errors.push(`Unknown source type: ${source.type}`);
          continue;
        }

        const discovered: DiscoveredItem[] = await fetcher();
        result.urlsDiscovered += discovered.length;

        // 각 URL 처리
        for (const item of discovered) {
          try {
            await processDiscoveredUrl(item, source.id, result);
          } catch (err) {
            const msg = err instanceof Error ? err.message : String(err);
            result.errors.push(`[${source.name}] ${item.url}: ${msg}`);
          }
        }

        // 소스의 lastCrawled 갱신
        await prisma.discoverySource.update({
          where: { id: source.id },
          data: { lastCrawled: new Date() },
        });
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        result.errors.push(`[${source.name}] Source error: ${msg}`);
      }
    }

    // 4. 새로 생성된 서비스 검증
    if (result.createdServiceIds.length > 0) {
      try {
        console.log(`[Crawl] ${result.createdServiceIds.length}개 신규 서비스 검증 시작...`);
        result.validation = await validateCrawledServices(result.createdServiceIds);
        console.log(`[Crawl] 검증 완료: ${result.validation.passed}/${result.validation.totalChecked} 통과, ${result.validation.warnings.length}건 경고`);
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        result.errors.push(`[Validation] ${msg}`);
      }
    }

    // 5. CrawlRun 완료 처리
    await prisma.crawlRun.update({
      where: { id: crawlRun.id },
      data: {
        status: "completed",
        completedAt: new Date(),
        sourcesChecked: result.sourcesChecked,
        urlsDiscovered: result.urlsDiscovered,
        urlsNew: result.urlsNew,
        urlsDuplicate: result.urlsDuplicate,
        servicesCreated: result.servicesCreated,
        errorMessage: result.errors.length > 0
          ? result.errors.join("\n").substring(0, 2000)
          : null,
      },
    });
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    result.errors.push(`Fatal: ${msg}`);

    await prisma.crawlRun.update({
      where: { id: crawlRun.id },
      data: {
        status: "failed",
        completedAt: new Date(),
        errorMessage: msg.substring(0, 2000),
      },
    });
  }

  return result;
}

/**
 * 발견된 URL 처리
 */
async function processDiscoveredUrl(
  item: DiscoveredItem,
  sourceId: string,
  result: CrawlResult
): Promise<void> {
  const normalized = normalizeUrl(item.url);
  const domain = extractDomain(item.url);

  // 이미 처리된 URL인지 확인
  const existingLog = await prisma.discoveryLog.findUnique({
    where: { normalizedUrl: normalized },
  });
  if (existingLog) {
    result.urlsDuplicate++;
    return;
  }

  // 중복 검사
  const dupCheck = await checkDuplicate(
    item.url,
    item.title || "",
    prisma
  );

  if (dupCheck.isDuplicate) {
    result.urlsDuplicate++;
    await prisma.discoveryLog.create({
      data: {
        sourceId,
        discoveredUrl: item.url,
        normalizedUrl: normalized,
        domain,
        title: item.title,
        description: item.description,
        status: "duplicate",
        duplicateOfId: dupCheck.matchedServiceId,
        similarityScore: dupCheck.similarityScore,
      },
    });
    return;
  }

  // 신규 URL — 메타데이터 추출 시도
  result.urlsNew++;

  try {
    const metadata = await scrapeServiceMetadata(item.url);
    const categoryResult = suggestCategory(
      `${metadata.name} ${metadata.description || ""}`
    );

    // 자동 승인 조건: 메타데이터 추출 성공 + 카테고리 매칭됨 (confidence > 0)
    // 이미 AI 관련 소스에서 발견된 URL이므로 키워드 1개만 매칭돼도 승인
    const autoApprove = categoryResult.confidence >= 0.3;

    if (autoApprove) {
      // 서비스 생성
      let slug = createSlug(metadata.name);
      const existingSlug = await prisma.service.findUnique({
        where: { slug },
      });
      if (existingSlug) {
        slug = `${slug}-${Date.now().toString(36)}`;
      }

      // 영어 서비스면 한글 번역
      const translation = await translateService(metadata.name, metadata.description);

      const service = await prisma.service.create({
        data: {
          slug,
          url: item.url,
          name: metadata.name,
          description: metadata.description,
          nameKo: translation.nameKo,
          descriptionKo: translation.descriptionKo,
          category: categoryResult.primary,
          tags: JSON.stringify(metadata.suggestedTags),
          pricingModel: "free",
          faviconUrl: metadata.faviconUrl || undefined,
          ogImageUrl: metadata.ogImageUrl || undefined,
          source: "auto",
          score: calculateGravityScore(0, new Date()),
        },
      });

      result.servicesCreated++;
      result.createdServiceIds.push(service.id);

      await prisma.discoveryLog.create({
        data: {
          sourceId,
          discoveredUrl: item.url,
          normalizedUrl: normalized,
          domain,
          title: metadata.name,
          description: metadata.description,
          status: "approved",
          serviceId: service.id,
          duplicateOfId: dupCheck.matchedServiceId,
          similarityScore: dupCheck.similarityScore,
        },
      });
    } else {
      // 수동 승인 대기
      await prisma.discoveryLog.create({
        data: {
          sourceId,
          discoveredUrl: item.url,
          normalizedUrl: normalized,
          domain,
          title: metadata.name,
          description: metadata.description,
          status: "pending",
          duplicateOfId: dupCheck.matchedServiceId,
          similarityScore: dupCheck.similarityScore,
        },
      });
    }
  } catch (err) {
    // 메타데이터 추출 실패
    const msg = err instanceof Error ? err.message : String(err);
    await prisma.discoveryLog.create({
      data: {
        sourceId,
        discoveredUrl: item.url,
        normalizedUrl: normalized,
        domain,
        title: item.title,
        description: item.description,
        status: "error",
        errorMessage: msg.substring(0, 500),
      },
    });
  }
}

/**
 * 기본 소스 시드
 * 웹 AI 디렉토리 소스를 높은 priority로, GitHub은 낮은 priority로 설정
 */
async function seedDefaultSources() {
  const defaults = [
    // 웹 AI 디렉토리 (높은 priority — 우선 크롤)
    {
      name: "Futurepedia",
      type: "futurepedia",
      url: "https://www.futurepedia.io/ai-tools",
      priority: 9,
    },
    {
      name: "Toolify AI",
      type: "toolify",
      url: "https://www.toolify.ai/",
      priority: 9,
    },
    {
      name: "BensBites",
      type: "bensbites",
      url: "https://bensbites.com/trending",
      priority: 8,
    },
    {
      name: "Product Hunt AI",
      type: "producthunt",
      url: "https://www.producthunt.com/topics/artificial-intelligence",
      priority: 8,
    },
    {
      name: "Hacker News (Show HN)",
      type: "hackernews",
      url: "https://hn.algolia.com/api/v1/search_by_date",
      priority: 7,
    },
    {
      name: "There Is An AI For That",
      type: "theresanai",
      url: "https://theresanaiforthat.com/new/",
      priority: 7,
    },
    // GitHub — 낮은 priority (1000+ 스타만 필터)
    {
      name: "GitHub Trending",
      type: "github",
      url: "https://github.com/trending",
      priority: 3,
    },
  ];

  for (const source of defaults) {
    await prisma.discoverySource.upsert({
      where: { url: source.url },
      update: { priority: source.priority },
      create: source,
    });
  }
}
