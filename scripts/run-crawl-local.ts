/**
 * 로컬에서 크롤링 직접 실행 (CRON_SECRET 불필요)
 * Usage: npx tsx scripts/run-crawl-local.ts [discover|articles|both]
 */
import { config } from "dotenv";
config({ path: ".env.production.local" });
config({ path: ".env.local" });
config({ path: ".env" });

import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client.js";
import pg from "pg";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
const adapter = new PrismaPg(pool);
const prisma = new PrismaClient({ adapter }) as any;

// prisma를 글로벌로 설정하여 lib 코드가 사용할 수 있도록
(globalThis as any).__prisma = prisma;

const mode = process.argv[2] || "both";

async function runDiscover() {
  console.log("\n=== 서비스 크롤링 시작 ===\n");

  // 동적 임포트
  const { runDailyCrawl } = await import("../src/lib/discovery/crawler.js");
  const result = await runDailyCrawl();

  console.log("\n=== 서비스 크롤링 결과 ===");
  console.log(`소스 확인: ${result.sourcesChecked}개`);
  console.log(`URL 발견: ${result.urlsDiscovered}개`);
  console.log(`신규 URL: ${result.urlsNew}개`);
  console.log(`중복 URL: ${result.urlsDuplicate}개`);
  console.log(`서비스 생성: ${result.servicesCreated}개`);
  if (result.errors.length > 0) {
    console.log(`에러: ${result.errors.length}개`);
    result.errors.slice(0, 5).forEach((e: string) => console.log(`  - ${e.substring(0, 100)}`));
  }
  return result;
}

async function runArticles() {
  console.log("\n=== 기사 크롤링 시작 ===\n");

  const { runArticleCrawl } = await import("../src/lib/discovery/articles.js");
  const result = await runArticleCrawl();

  console.log("\n=== 기사 크롤링 결과 ===");
  console.log(`서비스 확인: ${result.servicesChecked}개`);
  console.log(`기사 저장: ${result.articlesCreated}개`);
  if (result.errors.length > 0) {
    console.log(`에러: ${result.errors.length}개`);
    result.errors.slice(0, 5).forEach((e: string) => console.log(`  - ${e.substring(0, 100)}`));
  }
  return result;
}

async function main() {
  try {
    if (mode === "discover" || mode === "both") {
      await runDiscover();
    }
    if (mode === "articles" || mode === "both") {
      await runArticles();
    }
  } catch (err) {
    console.error("Fatal error:", err);
  } finally {
    await prisma.$disconnect();
    await pool.end();
    process.exit(0);
  }
}

main();
