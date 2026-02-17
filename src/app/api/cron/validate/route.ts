import { NextRequest, NextResponse } from "next/server";
import { validateCrawledServices } from "@/lib/discovery/validator";
import { sendValidationReport, sendSlackMessage } from "@/lib/slack";

export const dynamic = "force-dynamic";
export const maxDuration = 60;

export async function GET(request: NextRequest) {
  try {
    // Vercel Cron 인증
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    console.log("[Cron:Validate] Starting validation...");

    // 최근 24시간 auto 서비스 검증 (serviceIds 없으면 자동으로 최근 24시간)
    const report = await validateCrawledServices();

    console.log(
      `[Cron:Validate] 완료: ${report.totalChecked}개 검증, ${report.passed}개 통과, ${report.warnings.length}개 이슈`
    );

    // Slack 리포트 전송
    await sendValidationReport(report);

    return NextResponse.json({
      success: true,
      ...report,
    });
  } catch (error) {
    console.error("[Cron:Validate] Fatal error:", error);

    await sendSlackMessage({
      text: `🚨 데이터 검증 실패: ${error instanceof Error ? error.message : "알 수 없는 오류"}`,
    });

    return NextResponse.json(
      { error: "검증 중 오류가 발생했습니다" },
      { status: 500 }
    );
  }
}
