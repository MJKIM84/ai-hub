import { NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";
export const maxDuration = 30;

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://aihub.example.com";
const MAX_RETRIES = 2;
const HEALTH_TIMEOUT = 15000; // 15초

interface MonitorResult {
  healthy: boolean;
  attempts: number;
  lastError?: string;
  redeploy?: { triggered: boolean; success?: boolean; error?: string };
  notification?: { sent: boolean; method?: string; error?: string };
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

async function sendNotification(
  message: string,
  isRecovery: boolean = false
): Promise<{ sent: boolean; method?: string; error?: string }> {
  // 1. Discord 웹훅 (우선)
  const discordWebhook = process.env.DISCORD_WEBHOOK_URL;
  if (discordWebhook) {
    try {
      const emoji = isRecovery ? "✅" : "🚨";
      const res = await fetch(discordWebhook, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          content: `${emoji} **AI HUB 모니터링**\n${message}\n\n🕐 ${new Date().toLocaleString("ko-KR", { timeZone: "Asia/Seoul" })}`,
        }),
        signal: AbortSignal.timeout(10000),
      });
      if (res.ok) return { sent: true, method: "discord" };
    } catch {}
  }

  // 2. Slack 웹훅
  const slackWebhook = process.env.SLACK_WEBHOOK_URL;
  if (slackWebhook) {
    try {
      const res = await fetch(slackWebhook, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: `${isRecovery ? "✅" : "🚨"} AI HUB: ${message}`,
        }),
        signal: AbortSignal.timeout(10000),
      });
      if (res.ok) return { sent: true, method: "slack" };
    } catch {}
  }

  // 3. 이메일 (향후 확장 — 현재는 로그만)
  const alertEmail = process.env.ALERT_EMAIL;
  if (alertEmail) {
    console.warn(`[Monitor] 이메일 알림 대상: ${alertEmail}, 메시지: ${message}`);
    // 향후 SendGrid/Resend 등 연동 시 구현
  }

  // 웹훅이 설정되지 않았으면 콘솔 로그만
  console.error(`[Monitor] ALERT: ${message}`);
  return { sent: false, error: "No notification channel configured" };
}

export async function GET(request: NextRequest) {
  try {
    // Vercel Cron 인증
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const result: MonitorResult = { healthy: false, attempts: 0 };

    // 재시도 포함 헬스 체크
    for (let i = 0; i <= MAX_RETRIES; i++) {
      result.attempts = i + 1;
      const health = await checkHealth();

      if (health.ok) {
        result.healthy = true;
        break;
      }

      result.lastError = health.error;

      // 마지막 시도가 아니면 3초 대기 후 재시도
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

    // 서비스 다운 감지
    console.error(`[Monitor] Service DOWN after ${result.attempts} attempts: ${result.lastError}`);

    // 알림 전송
    const notifMsg = `서비스 다운 감지!\n에러: ${result.lastError}\n시도 횟수: ${result.attempts}`;
    result.notification = await sendNotification(notifMsg);

    // Vercel 재배포 트리거
    const redeployResult = await triggerRedeploy();
    result.redeploy = { triggered: true, ...redeployResult };

    if (redeployResult.success) {
      await sendNotification("자동 재배포가 트리거되었습니다. 잠시 후 서비스가 복구될 예정입니다.", false);
    } else {
      await sendNotification(`⚠️ 자동 재배포 실패: ${redeployResult.error}\n수동 확인이 필요합니다.`, false);
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
