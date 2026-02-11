import { NextRequest, NextResponse } from "next/server";
import { runDailyCrawl } from "@/lib/discovery/crawler";

export const dynamic = "force-dynamic";
export const maxDuration = 60; // Vercel Pro: 최대 60초

export async function GET(request: NextRequest) {
  try {
    // Vercel Cron 인증 (CRON_SECRET은 Vercel이 자동 설정)
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    console.log("[Cron] Starting daily AI service discovery...");
    const result = await runDailyCrawl();
    console.log("[Cron] Completed:", JSON.stringify(result));

    return NextResponse.json({
      success: true,
      ...result,
    });
  } catch (error) {
    console.error("[Cron] Fatal error:", error);
    return NextResponse.json(
      {
        error: "크롤링 실행 중 오류가 발생했습니다",
      },
      { status: 500 }
    );
  }
}
