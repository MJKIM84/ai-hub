import { NextRequest, NextResponse } from "next/server";
import { runArticleCrawl } from "@/lib/discovery/articles";
import { sendSlackMessage } from "@/lib/slack";

export const dynamic = "force-dynamic";
export const maxDuration = 60; // Vercel Pro: 최대 60초

const BATCH_SIZE = 15;

export async function GET(request: NextRequest) {
  try {
    // Vercel Cron 인증
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const offset = parseInt(request.nextUrl.searchParams.get("offset") || "0", 10);
    const limit = parseInt(request.nextUrl.searchParams.get("limit") || String(BATCH_SIZE), 10);

    console.log(`[Cron:Articles] Starting article crawl (offset=${offset}, limit=${limit})...`);
    const result = await runArticleCrawl(offset, limit);
    console.log("[Cron:Articles] Completed:", JSON.stringify(result));

    // 다음 배치가 남아있으면 자동으로 다음 호출 트리거
    const nextOffset = offset + limit;
    let nextBatchTriggered = false;

    if (nextOffset < result.totalServices) {
      try {
        const baseUrl = process.env.NEXT_PUBLIC_APP_URL || "https://findmy.ai.kr";
        // fire-and-forget: 다음 배치를 비동기로 호출
        fetch(`${baseUrl}/api/cron/articles?offset=${nextOffset}&limit=${BATCH_SIZE}`, {
          headers: { Authorization: `Bearer ${cronSecret}` },
        }).catch(() => {}); // 에러 무시 — 다음 크론에서 재시도
        nextBatchTriggered = true;
        console.log(`[Cron:Articles] Next batch triggered: offset=${nextOffset}`);
      } catch {
        // 다음 배치 트리거 실패 — 다음 크론 실행 시 처리
      }
    }

    // 전체 완료 시에만 Slack 알림 (마지막 배치)
    if (!nextBatchTriggered && result.articlesCreated > 0) {
      await sendSlackMessage({
        text: [
          "📰 기사 크롤링 전체 완료",
          `서비스 확인: ${result.totalServices}개`,
          `이번 배치 기사 저장: ${result.articlesCreated}개`,
          result.errors.length > 0
            ? `에러: ${result.errors.length}개`
            : "",
        ]
          .filter(Boolean)
          .join("\n"),
      });
    }

    return NextResponse.json({
      success: true,
      ...result,
      nextBatchTriggered,
      nextOffset: nextBatchTriggered ? nextOffset : null,
    });
  } catch (error) {
    console.error("[Cron:Articles] Fatal error:", error);

    await sendSlackMessage({
      text: `🚨 기사 크롤링 실패: ${error instanceof Error ? error.message : "알 수 없는 오류"}`,
    });

    return NextResponse.json(
      { error: "기사 크롤링 중 오류가 발생했습니다" },
      { status: 500 }
    );
  }
}
