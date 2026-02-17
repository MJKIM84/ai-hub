import { prisma } from "@/lib/prisma";
import { suggestCategory } from "@/lib/categorizer";
import { calculateNameSimilarity, extractDomain } from "./dedup";

export interface ValidationWarning {
  serviceId: string;
  serviceName: string;
  serviceUrl: string;
  type: "url_dead" | "missing_description" | "name_is_domain" | "wrong_category" | "possible_duplicate" | "bad_name";
  message: string;
  severity: "error" | "warning";
}

export interface ValidationReport {
  totalChecked: number;
  passed: number;
  warnings: ValidationWarning[];
}

/**
 * URL 생존 확인 — HEAD 요청으로 응답 코드 체크
 */
async function checkUrlAlive(url: string): Promise<{ alive: boolean; status: number | null }> {
  try {
    const res = await fetch(url, {
      method: "HEAD",
      headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
      },
      redirect: "follow",
      signal: AbortSignal.timeout(8000),
    });
    // 403은 봇 차단이지 URL이 죽은 건 아님 (ChatGPT, Claude 등 대형 서비스)
    const isAlive = res.ok || [301, 302, 308, 403].includes(res.status);
    return { alive: isAlive, status: res.status };
  } catch {
    // HEAD 실패 시 GET으로 재시도 (일부 서버가 HEAD를 거부)
    try {
      const res = await fetch(url, {
        method: "GET",
        headers: {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
        redirect: "follow",
        signal: AbortSignal.timeout(8000),
      });
      const isAlive = res.ok || res.status === 403;
      return { alive: isAlive, status: res.status };
    } catch {
      return { alive: false, status: null };
    }
  }
}

/**
 * name이 도메인명과 같은지 체크
 */
function isNameJustDomain(name: string, url: string): boolean {
  try {
    const domain = extractDomain(url);
    const hostname = new URL(url).hostname.replace(/^www\./, "").toLowerCase();
    const nameLower = name.toLowerCase().trim();

    return nameLower === domain || nameLower === hostname || nameLower === hostname.split(".")[0];
  } catch {
    return false;
  }
}

/**
 * 크롤링된 서비스 데이터 검증
 * @param serviceIds 검증할 서비스 ID 목록 (비어있으면 최근 24시간 auto 서비스)
 */
export async function validateCrawledServices(
  serviceIds?: string[]
): Promise<ValidationReport> {
  const report: ValidationReport = {
    totalChecked: 0,
    passed: 0,
    warnings: [],
  };

  // 검증 대상 서비스 조회
  let services;
  if (serviceIds && serviceIds.length > 0) {
    services = await prisma.service.findMany({
      where: { id: { in: serviceIds } },
      select: { id: true, name: true, url: true, description: true, category: true },
    });
  } else {
    // 최근 24시간 내 자동 등록된 서비스
    const oneDayAgo = new Date();
    oneDayAgo.setDate(oneDayAgo.getDate() - 1);
    services = await prisma.service.findMany({
      where: {
        source: "auto",
        createdAt: { gte: oneDayAgo },
      },
      select: { id: true, name: true, url: true, description: true, category: true },
    });
  }

  if (services.length === 0) {
    return report;
  }

  // 전체 서비스 목록 (중복 검사용)
  const allServices = await prisma.service.findMany({
    select: { id: true, name: true, url: true },
  });

  for (const service of services) {
    report.totalChecked++;
    const serviceWarnings: ValidationWarning[] = [];

    // 1. URL 생존 확인
    const urlCheck = await checkUrlAlive(service.url);
    if (!urlCheck.alive) {
      serviceWarnings.push({
        serviceId: service.id,
        serviceName: service.name,
        serviceUrl: service.url,
        type: "url_dead",
        message: `URL 응답 없음 (status: ${urlCheck.status ?? "timeout"})`,
        severity: "error",
      });
    }

    // 2. 필수 필드 체크
    if (!service.description) {
      serviceWarnings.push({
        serviceId: service.id,
        serviceName: service.name,
        serviceUrl: service.url,
        type: "missing_description",
        message: "설명(description)이 없음",
        severity: "warning",
      });
    }

    if (isNameJustDomain(service.name, service.url)) {
      serviceWarnings.push({
        serviceId: service.id,
        serviceName: service.name,
        serviceUrl: service.url,
        type: "name_is_domain",
        message: `이름이 도메인명과 동일 ("${service.name}")`,
        severity: "warning",
      });
    }

    // 3. 이름 품질 검증
    if (service.name.startsWith("GitHub -")) {
      serviceWarnings.push({
        serviceId: service.id,
        serviceName: service.name,
        serviceUrl: service.url,
        type: "bad_name",
        message: `GitHub 레포 제목 형태 — 정리 필요`,
        severity: "warning",
      });
    } else if (service.name.includes(" | ") || service.name.length > 60) {
      serviceWarnings.push({
        serviceId: service.id,
        serviceName: service.name,
        serviceUrl: service.url,
        type: "bad_name",
        message: `이름이 너무 길거나 파이프(|) 포함 (${service.name.length}자)`,
        severity: "warning",
      });
    }

    // 4. 카테고리 정확도 재검증
    const text = `${service.name} ${service.description || ""}`;
    const categoryCheck = suggestCategory(text);
    if (categoryCheck.confidence < 0.5 && categoryCheck.primary !== service.category) {
      serviceWarnings.push({
        serviceId: service.id,
        serviceName: service.name,
        serviceUrl: service.url,
        type: "wrong_category",
        message: `카테고리 불일치 — 현재: ${service.category}, 추천: ${categoryCheck.primary} (confidence: ${categoryCheck.confidence})`,
        severity: "warning",
      });
    }

    // 5. 중복 재검사 (다른 서비스와 이름 유사도 0.7+)
    for (const other of allServices) {
      if (other.id === service.id) continue;
      const similarity = calculateNameSimilarity(service.name, other.name);
      if (similarity >= 0.7) {
        serviceWarnings.push({
          serviceId: service.id,
          serviceName: service.name,
          serviceUrl: service.url,
          type: "possible_duplicate",
          message: `"${other.name}"과(와) 유사 (유사도: ${(similarity * 100).toFixed(0)}%)`,
          severity: similarity >= 0.85 ? "error" : "warning",
        });
        break; // 하나만 보고
      }
    }

    if (serviceWarnings.length === 0) {
      report.passed++;
    } else {
      report.warnings.push(...serviceWarnings);
    }

    // Rate limit 방지
    await new Promise((r) => setTimeout(r, 200));
  }

  return report;
}
