import type { PrismaClient } from "@/generated/prisma/client";

/**
 * URL 정규화 — 프로토콜, www, 트레일링 슬래시, 쿼리 파라미터, 해시 제거
 */
export function normalizeUrl(rawUrl: string): string {
  try {
    const url = new URL(rawUrl.trim());
    // 프로토콜 통일
    let normalized = url.hostname.replace(/^www\./, "").toLowerCase();
    // 경로: 트레일링 슬래시 제거
    let pathname = url.pathname.replace(/\/+$/, "");
    if (!pathname) pathname = "";
    normalized += pathname;
    return normalized;
  } catch {
    // 파싱 실패 시 원본 그대로 소문자 처리
    return rawUrl.trim().toLowerCase();
  }
}

/**
 * 루트 도메인 추출 — chat.openai.com → openai.com
 */
export function extractDomain(rawUrl: string): string {
  try {
    const url = new URL(rawUrl.trim());
    const hostname = url.hostname.replace(/^www\./, "").toLowerCase();
    const parts = hostname.split(".");
    // IP 주소거나 단순 도메인이면 그대로
    if (parts.length <= 2) return hostname;
    // 마지막 2부분만 (co.kr, com.au 등은 단순화)
    return parts.slice(-2).join(".");
  } catch {
    return rawUrl.trim().toLowerCase();
  }
}

/**
 * Levenshtein 거리 기반 이름 유사도 (0~1)
 */
export function calculateNameSimilarity(a: string, b: string): number {
  const s1 = a.toLowerCase().trim();
  const s2 = b.toLowerCase().trim();

  if (s1 === s2) return 1;
  if (s1.length === 0 || s2.length === 0) return 0;

  const len1 = s1.length;
  const len2 = s2.length;

  // DP 테이블
  const dp: number[][] = Array.from({ length: len1 + 1 }, () =>
    Array(len2 + 1).fill(0)
  );

  for (let i = 0; i <= len1; i++) dp[i][0] = i;
  for (let j = 0; j <= len2; j++) dp[0][j] = j;

  for (let i = 1; i <= len1; i++) {
    for (let j = 1; j <= len2; j++) {
      const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
      dp[i][j] = Math.min(
        dp[i - 1][j] + 1,
        dp[i][j - 1] + 1,
        dp[i - 1][j - 1] + cost
      );
    }
  }

  const distance = dp[len1][len2];
  const maxLen = Math.max(len1, len2);
  return 1 - distance / maxLen;
}

export interface DuplicateCheckResult {
  isDuplicate: boolean;
  matchType: "exact_url" | "domain" | "name" | null;
  matchedServiceId: string | null;
  matchedServiceName: string | null;
  similarityScore: number;
}

/**
 * 3단계 중복 검사:
 * 1. 정규화된 URL 정확 매칭
 * 2. 루트 도메인 매칭
 * 3. 이름 유사도 > 0.85
 */
export async function checkDuplicate(
  url: string,
  name: string,
  prisma: PrismaClient
): Promise<DuplicateCheckResult> {
  const normalized = normalizeUrl(url);
  const domain = extractDomain(url);

  // 1단계: 정규화된 URL로 기존 DiscoveryLog 검사
  const existingLog = await prisma.discoveryLog.findUnique({
    where: { normalizedUrl: normalized },
  });
  if (existingLog) {
    return {
      isDuplicate: true,
      matchType: "exact_url",
      matchedServiceId: existingLog.duplicateOfId || existingLog.serviceId,
      matchedServiceName: existingLog.title,
      similarityScore: 1,
    };
  }

  // 1-b: 기존 Service 테이블의 URL과도 비교
  const allServices = await prisma.service.findMany({
    select: { id: true, url: true, name: true },
  });

  for (const svc of allServices) {
    if (normalizeUrl(svc.url) === normalized) {
      return {
        isDuplicate: true,
        matchType: "exact_url",
        matchedServiceId: svc.id,
        matchedServiceName: svc.name,
        similarityScore: 1,
      };
    }
  }

  // 2단계: 도메인 매칭 (같은 루트 도메인의 서비스)
  for (const svc of allServices) {
    if (extractDomain(svc.url) === domain) {
      return {
        isDuplicate: false, // 같은 도메인이지만 다른 서비스일 수 있음 — 경고만
        matchType: "domain",
        matchedServiceId: svc.id,
        matchedServiceName: svc.name,
        similarityScore: 0.7,
      };
    }
  }

  // 3단계: 이름 유사도
  if (name) {
    for (const svc of allServices) {
      const similarity = calculateNameSimilarity(name, svc.name);
      if (similarity > 0.85) {
        return {
          isDuplicate: true,
          matchType: "name",
          matchedServiceId: svc.id,
          matchedServiceName: svc.name,
          similarityScore: similarity,
        };
      }
    }
  }

  return {
    isDuplicate: false,
    matchType: null,
    matchedServiceId: null,
    matchedServiceName: null,
    similarityScore: 0,
  };
}
