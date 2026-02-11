"use client";

import { useState, useEffect, useCallback } from "react";
import Link from "next/link";
import {
  Activity,
  Database,
  Server,
  MemoryStick,
  RefreshCw,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  ArrowLeft,
} from "lucide-react";

interface HealthData {
  status: "healthy" | "unhealthy";
  timestamp: string;
  uptime: number;
  latency: number;
  checks: Record<string, { status: string; latency?: number; error?: string }>;
  memory: { heapUsed: string; heapTotal: string };
}

function StatusIcon({ status }: { status: string }) {
  if (status === "ok" || status === "healthy")
    return <CheckCircle2 className="w-5 h-5 text-emerald-400" />;
  if (status === "warning")
    return <AlertTriangle className="w-5 h-5 text-amber-400" />;
  return <XCircle className="w-5 h-5 text-red-400" />;
}

function formatUptime(seconds: number): string {
  const d = Math.floor(seconds / 86400);
  const h = Math.floor((seconds % 86400) / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = Math.floor(seconds % 60);

  const parts: string[] = [];
  if (d > 0) parts.push(`${d}일`);
  if (h > 0) parts.push(`${h}시간`);
  if (m > 0) parts.push(`${m}분`);
  parts.push(`${s}초`);
  return parts.join(" ");
}

const CHECK_ICONS: Record<string, typeof Server> = {
  server: Server,
  database: Database,
  memory: MemoryStick,
};

const CHECK_NAMES: Record<string, string> = {
  server: "서버",
  database: "데이터베이스",
  memory: "메모리",
};

export default function StatusPage() {
  const [health, setHealth] = useState<HealthData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastChecked, setLastChecked] = useState<Date | null>(null);

  const fetchHealth = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/health", { cache: "no-store" });
      const data = await res.json();
      setHealth(data);
      setLastChecked(new Date());
    } catch {
      setError("서버에 연결할 수 없습니다");
      setHealth(null);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchHealth();
    const interval = setInterval(fetchHealth, 30000); // 30초마다 갱신
    return () => clearInterval(interval);
  }, [fetchHealth]);

  const overallStatus = error
    ? "down"
    : health?.status === "healthy"
    ? "operational"
    : "degraded";

  return (
    <div className="min-h-screen dark:bg-[#0a0a0f] bg-gray-50">
      <div className="max-w-2xl mx-auto px-4 py-12">
        {/* 헤더 */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/"
            className="p-2 rounded-lg dark:bg-white/5 bg-black/5 dark:hover:bg-white/10 hover:bg-black/10 transition-colors"
          >
            <ArrowLeft className="w-5 h-5 dark:text-zinc-400 text-zinc-500" />
          </Link>
          <div className="flex items-center gap-2">
            <Activity className="w-6 h-6 text-neon-blue" />
            <h1 className="text-2xl font-bold dark:text-white text-zinc-900">
              서비스 상태
            </h1>
          </div>
          <button
            onClick={fetchHealth}
            disabled={loading}
            className="ml-auto p-2 rounded-lg dark:bg-white/5 bg-black/5
              dark:hover:bg-white/10 hover:bg-black/10 transition-colors
              disabled:opacity-50"
          >
            <RefreshCw
              className={`w-5 h-5 dark:text-zinc-400 text-zinc-500 ${
                loading ? "animate-spin" : ""
              }`}
            />
          </button>
        </div>

        {/* 전체 상태 배너 */}
        <div
          className={`glass-card p-6 mb-6 border-l-4 ${
            overallStatus === "operational"
              ? "border-l-emerald-400"
              : overallStatus === "degraded"
              ? "border-l-amber-400"
              : "border-l-red-400"
          }`}
        >
          <div className="flex items-center gap-3">
            {overallStatus === "operational" ? (
              <CheckCircle2 className="w-8 h-8 text-emerald-400" />
            ) : overallStatus === "degraded" ? (
              <AlertTriangle className="w-8 h-8 text-amber-400" />
            ) : (
              <XCircle className="w-8 h-8 text-red-400" />
            )}
            <div>
              <h2 className="text-lg font-semibold dark:text-white text-zinc-900">
                {overallStatus === "operational"
                  ? "모든 시스템이 정상 작동 중입니다"
                  : overallStatus === "degraded"
                  ? "일부 시스템에 문제가 감지되었습니다"
                  : "서비스에 연결할 수 없습니다"}
              </h2>
              {lastChecked && (
                <p className="text-sm dark:text-zinc-400 text-zinc-500 mt-1">
                  마지막 확인: {lastChecked.toLocaleTimeString("ko-KR")}
                </p>
              )}
            </div>
          </div>
        </div>

        {/* 상세 체크 항목들 */}
        {health && (
          <div className="space-y-3 mb-6">
            {Object.entries(health.checks).map(([key, check]) => {
              const Icon = CHECK_ICONS[key] || Server;
              const name = CHECK_NAMES[key] || key;

              return (
                <div
                  key={key}
                  className="glass-card p-4 flex items-center justify-between"
                >
                  <div className="flex items-center gap-3">
                    <Icon className="w-5 h-5 dark:text-zinc-400 text-zinc-500" />
                    <span className="font-medium dark:text-white text-zinc-900">
                      {name}
                    </span>
                  </div>
                  <div className="flex items-center gap-3">
                    {check.latency !== undefined && check.status !== "error" && (
                      <span className="text-sm dark:text-zinc-500 text-zinc-400">
                        {key === "memory"
                          ? `${check.latency}MB`
                          : `${check.latency}ms`}
                      </span>
                    )}
                    {check.error && (
                      <span className="text-sm text-red-400">{check.error}</span>
                    )}
                    <StatusIcon status={check.status} />
                  </div>
                </div>
              );
            })}
          </div>
        )}

        {/* 시스템 정보 */}
        {health && (
          <div className="glass-card p-4">
            <h3 className="text-sm font-semibold dark:text-zinc-300 text-zinc-700 mb-3">
              시스템 정보
            </h3>
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span className="dark:text-zinc-500 text-zinc-400">응답 시간</span>
                <p className="dark:text-white text-zinc-900 font-medium">
                  {health.latency}ms
                </p>
              </div>
              <div>
                <span className="dark:text-zinc-500 text-zinc-400">업타임</span>
                <p className="dark:text-white text-zinc-900 font-medium">
                  {formatUptime(health.uptime)}
                </p>
              </div>
              <div>
                <span className="dark:text-zinc-500 text-zinc-400">힙 메모리</span>
                <p className="dark:text-white text-zinc-900 font-medium">
                  {health.memory.heapUsed} / {health.memory.heapTotal}
                </p>
              </div>
              <div>
                <span className="dark:text-zinc-500 text-zinc-400">상태 확인</span>
                <p className="dark:text-white text-zinc-900 font-medium">
                  {health.timestamp
                    ? new Date(health.timestamp).toLocaleTimeString("ko-KR")
                    : "-"}
                </p>
              </div>
            </div>
          </div>
        )}

        {/* 에러 표시 */}
        {error && !health && (
          <div className="glass-card p-6 text-center">
            <XCircle className="w-12 h-12 text-red-400 mx-auto mb-3" />
            <p className="dark:text-zinc-300 text-zinc-700 mb-2">{error}</p>
            <p className="text-sm dark:text-zinc-500 text-zinc-400">
              서비스가 일시적으로 중단되었을 수 있습니다. 잠시 후 다시 확인해 주세요.
            </p>
          </div>
        )}

        {/* 푸터 */}
        <p className="text-center text-sm dark:text-zinc-600 text-zinc-400 mt-8">
          30초마다 자동으로 상태를 확인합니다
        </p>
      </div>
    </div>
  );
}
