import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export const dynamic = "force-dynamic";

export async function GET() {
  const start = Date.now();
  const checks: Record<string, { status: string; latency?: number; error?: string }> = {};

  // 1. 기본 서버 체크
  checks.server = { status: "ok", latency: 0 };

  // 2. DB 연결 체크
  try {
    const dbStart = Date.now();
    await prisma.$queryRawUnsafe("SELECT 1");
    checks.database = { status: "ok", latency: Date.now() - dbStart };
  } catch (err) {
    checks.database = {
      status: "error",
      error: err instanceof Error ? err.message : "DB connection failed",
    };
  }

  // 3. 메모리 체크
  const memUsage = process.memoryUsage();
  const heapUsedMB = Math.round(memUsage.heapUsed / 1024 / 1024);
  const heapTotalMB = Math.round(memUsage.heapTotal / 1024 / 1024);
  checks.memory = {
    status: heapUsedMB > 450 ? "warning" : "ok",
    latency: heapUsedMB,
  };

  const totalLatency = Date.now() - start;
  const overallStatus = Object.values(checks).every((c) => c.status !== "error")
    ? "healthy"
    : "unhealthy";

  const statusCode = overallStatus === "healthy" ? 200 : 503;

  return NextResponse.json(
    {
      status: overallStatus,
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
      latency: totalLatency,
      checks,
      memory: {
        heapUsed: `${heapUsedMB}MB`,
        heapTotal: `${heapTotalMB}MB`,
      },
    },
    { status: statusCode }
  );
}
