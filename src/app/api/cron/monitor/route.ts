import { NextRequest, NextResponse } from "next/server";
import { sendSlackMessage } from "@/lib/slack";

export const dynamic = "force-dynamic";
export const maxDuration = 30;

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://findmy.ai.kr";
const MAX_RETRIES = 2;
const HEALTH_TIMEOUT = 15000;

interface MonitorResult {
  healthy: boolean;
  attempts: number;
  lastError?: string;
  redeploy?: { triggered: boolean; success?: boolean; error?: string };
  slackNotified?: boolean;
}

async function checkHealth(): Promise<{ ok: boolean; error?: string }> {
  try {
    const res = await fetch(`${SITE_URL}/api/health`, {
      signal: AbortSignal.timeout(HEALTH_TIMEOUT),
      cache: "no-store",
    });
    if (!res.ok) {
      return { ok: false, error: `HTTP ${res.status}` };
    }
    const data = await res.json();
    return { ok: data.status === "healthy", error: data.status !== "healthy" ? "Unhealthy status" : undefined };
  } catch (err) {
    return {
      ok: false,
      error: err instanceof Error ? err.message : "Health check failed",
    };
  }
}

async function triggerRedeploy(): Promise<{ success: boolean; error?: string }> {
  const deployHook = process.env.VERCEL_DEPLOY_HOOK;
  if (!deployHook) {
    return { success: false, error: "VERCEL_DEPLOY_HOOK not configured" };
  }

  try {
    const res = await fetch(deployHook, {
      method: "POST",
      signal: AbortSignal.timeout(10000),
    });
    if (res.ok) {
      return { success: true };
    }
    return { success: false, error: `Deploy hook returned ${res.status}` };
  } catch (err) {
    return {
      success: false,
      error: err instanceof Error ? err.message : "Deploy hook failed",
    };
  }
}

export async function GET(request: NextRequest) {
  try {
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const result: MonitorResult = { healthy: false, attempts: 0 };

    for (let i = 0; i <= MAX_RETRIES; i++) {
      result.attempts = i + 1;
      const health = await checkHealth();

      if (health.ok) {
        result.healthy = true;
        break;
      }

      result.lastError = health.error;

      if (i < MAX_RETRIES) {
        await new Promise((r) => setTimeout(r, 3000));
      }
    }

    if (result.healthy) {
      console.log(`[Monitor] Health check passed (${result.attempts} attempt(s))`);
      return NextResponse.json({
        success: true,
        ...result,
        timestamp: new Date().toISOString(),
      });
    }

    // 서비스 다운 감지 — Slack 알림
    console.error(`[Monitor] Service DOWN after ${result.attempts} attempts: ${result.lastError}`);

    result.slackNotified = await sendSlackMessage({
      text: `🚨 FindMyAI 서비스 다운 감지!\n에러: ${result.lastError}\n시도 횟수: ${result.attempts}`,
    });

    // Vercel 재배포 트리거
    const redeployResult = await triggerRedeploy();
    result.redeploy = { triggered: true, ...redeployResult };

    if (redeployResult.success) {
      await sendSlackMessage({
        text: "🔄 FindMyAI 자동 재배포가 트리거되었습니다. 잠시 후 서비스가 복구될 예정입니다.",
      });
    } else {
      await sendSlackMessage({
        text: `⚠️ FindMyAI 자동 재배포 실패: ${redeployResult.error}\n수동 확인이 필요합니다.`,
      });
    }

    return NextResponse.json(
      {
        success: false,
        ...result,
        timestamp: new Date().toISOString(),
      },
      { status: 503 }
    );
  } catch (error) {
    console.error("[Monitor] Fatal error:", error);
    return NextResponse.json(
      { error: "Monitor execution failed" },
      { status: 500 }
    );
  }
}
