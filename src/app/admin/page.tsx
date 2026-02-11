"use client";

import { useState, useEffect, useCallback, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import {
  Globe, FileEdit, Database, Activity,
  Check, X, ExternalLink, Loader2, RefreshCw
} from "lucide-react";

type Tab = "discoveries" | "edit-requests" | "sources" | "crawl-runs";

interface DiscoveryLog {
  id: string;
  discoveredUrl: string;
  normalizedUrl: string;
  domain: string;
  title: string | null;
  description: string | null;
  status: string;
  similarityScore: number | null;
  errorMessage: string | null;
  createdAt: string;
  source: { name: string; type: string };
  duplicateOf: { id: string; name: string; slug: string } | null;
}

interface EditRequestItem {
  id: string;
  requestType: string;
  contactEmail: string;
  isVerified: boolean;
  changes: string;
  reason: string | null;
  status: string;
  adminNote: string | null;
  createdAt: string;
  service: { id: string; name: string; slug: string; url: string };
}

interface SourceItem {
  id: string;
  name: string;
  type: string;
  url: string;
  isActive: boolean;
  priority: number;
  lastCrawled: string | null;
}

interface CrawlRunItem {
  id: string;
  startedAt: string;
  completedAt: string | null;
  status: string;
  sourcesChecked: number;
  urlsDiscovered: number;
  urlsNew: number;
  urlsDuplicate: number;
  servicesCreated: number;
  errorMessage: string | null;
}

export default function AdminPageWrapper() {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center dark:bg-zinc-950 bg-zinc-50">
        <Loader2 className="w-8 h-8 animate-spin dark:text-zinc-400 text-zinc-500" />
      </div>
    }>
      <AdminPage />
    </Suspense>
  );
}

function AdminPage() {
  const searchParams = useSearchParams();
  const token = searchParams.get("token") || "";
  const [activeTab, setActiveTab] = useState<Tab>("discoveries");
  const [loading, setLoading] = useState(false);

  // Data
  const [discoveries, setDiscoveries] = useState<DiscoveryLog[]>([]);
  const [editRequests, setEditRequests] = useState<EditRequestItem[]>([]);
  const [sources, setSources] = useState<SourceItem[]>([]);
  const [crawlRuns, setCrawlRuns] = useState<CrawlRunItem[]>([]);
  const [statusFilter, setStatusFilter] = useState<string>("");

  const fetchData = useCallback(async () => {
    if (!token) return;
    setLoading(true);
    try {
      const statusParam = statusFilter ? `&status=${statusFilter}` : "";
      switch (activeTab) {
        case "discoveries": {
          const res = await fetch(`/api/admin/discoveries?token=${token}${statusParam}`);
          const data = await res.json();
          setDiscoveries(data.items || []);
          break;
        }
        case "edit-requests": {
          const res = await fetch(`/api/admin/edit-requests?token=${token}${statusParam}`);
          const data = await res.json();
          setEditRequests(data.items || []);
          break;
        }
        case "sources": {
          const res = await fetch(`/api/admin/sources?token=${token}`);
          const data = await res.json();
          setSources(data.items || []);
          break;
        }
        case "crawl-runs": {
          const res = await fetch(`/api/admin/crawl-runs?token=${token}`);
          const data = await res.json();
          setCrawlRuns(data.items || []);
          break;
        }
      }
    } catch (err) {
      console.error("Fetch error:", err);
    } finally {
      setLoading(false);
    }
  }, [token, activeTab, statusFilter]);

  useEffect(() => { fetchData(); }, [fetchData]);

  const handleDiscoveryAction = async (id: string, action: "approve" | "reject") => {
    try {
      await fetch(`/api/admin/discoveries/${id}?token=${token}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action }),
      });
      fetchData();
    } catch (err) {
      console.error("Action error:", err);
    }
  };

  const handleEditRequestAction = async (id: string, action: "approve" | "reject") => {
    try {
      await fetch(`/api/admin/edit-requests/${id}?token=${token}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action }),
      });
      fetchData();
    } catch (err) {
      console.error("Action error:", err);
    }
  };

  if (!token) {
    return (
      <div className="min-h-screen flex items-center justify-center dark:bg-zinc-950 bg-zinc-50">
        <div className="glass p-8 text-center max-w-md">
          <h1 className="text-xl font-bold dark:text-white text-zinc-900 mb-4">Admin Access Required</h1>
          <p className="text-sm dark:text-zinc-400 text-zinc-500">
            관리자 인증이 필요합니다.
          </p>
        </div>
      </div>
    );
  }

  const tabs: { id: Tab; label: string; icon: React.ReactNode }[] = [
    { id: "discoveries", label: "발견 목록", icon: <Globe className="w-4 h-4" /> },
    { id: "edit-requests", label: "수정 요청", icon: <FileEdit className="w-4 h-4" /> },
    { id: "sources", label: "소스 관리", icon: <Database className="w-4 h-4" /> },
    { id: "crawl-runs", label: "크롤링 이력", icon: <Activity className="w-4 h-4" /> },
  ];

  const statusBadge = (status: string) => {
    const colors: Record<string, string> = {
      pending: "dark:bg-yellow-500/15 bg-yellow-500/10 dark:text-yellow-400 text-yellow-600",
      approved: "dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600",
      rejected: "dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600",
      duplicate: "dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600",
      error: "dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600",
      running: "dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600",
      completed: "dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600",
      failed: "dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600",
    };
    return (
      <span className={`px-2 py-0.5 rounded-md text-xs font-medium ${colors[status] || "dark:bg-zinc-500/15 bg-zinc-500/10 dark:text-zinc-400 text-zinc-500"}`}>
        {status}
      </span>
    );
  };

  return (
    <div className="min-h-screen dark:bg-zinc-950 bg-zinc-50 p-4 md:p-8">
      <div className="max-w-6xl mx-auto">
        <div className="flex items-center justify-between mb-8">
          <h1 className="text-2xl font-bold dark:text-white text-zinc-900">Admin Dashboard</h1>
          <button
            onClick={fetchData}
            disabled={loading}
            className="flex items-center gap-2 px-4 py-2 rounded-xl text-sm
              dark:bg-white/5 bg-black/5
              dark:text-zinc-300 text-zinc-600
              dark:hover:bg-white/10 hover:bg-black/10
              transition-all"
          >
            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <RefreshCw className="w-4 h-4" />}
            새로고침
          </button>
        </div>

        {/* Tabs */}
        <div className="flex gap-2 mb-6 overflow-x-auto">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => { setActiveTab(tab.id); setStatusFilter(""); }}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-medium whitespace-nowrap transition-all
                ${activeTab === tab.id
                  ? "bg-gradient-to-r from-neon-blue to-neon-purple text-white"
                  : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500 dark:hover:bg-white/10 hover:bg-black/10"
                }`}
            >
              {tab.icon}
              {tab.label}
            </button>
          ))}
        </div>

        {/* Status filter */}
        {(activeTab === "discoveries" || activeTab === "edit-requests") && (
          <div className="flex gap-2 mb-4">
            {["", "pending", "approved", "rejected", ...(activeTab === "discoveries" ? ["duplicate", "error"] : [])].map((s) => (
              <button
                key={s}
                onClick={() => setStatusFilter(s)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all
                  ${statusFilter === s
                    ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
                    : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500"
                  }`}
              >
                {s || "전체"}
              </button>
            ))}
          </div>
        )}

        {/* Content */}
        <div className="glass rounded-2xl overflow-hidden">
          {loading ? (
            <div className="flex items-center justify-center p-12">
              <Loader2 className="w-8 h-8 animate-spin dark:text-zinc-400 text-zinc-500" />
            </div>
          ) : (
            <>
              {/* Discoveries */}
              {activeTab === "discoveries" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {discoveries.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">데이터가 없습니다</p>
                  ) : (
                    discoveries.map((d) => (
                      <div key={d.id} className="p-4 flex items-start gap-4">
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-2 mb-1">
                            <p className="text-sm font-medium dark:text-white text-zinc-900 truncate">
                              {d.title || d.domain}
                            </p>
                            {statusBadge(d.status)}
                            <span className="text-xs dark:text-zinc-500 text-zinc-400">
                              via {d.source?.name}
                            </span>
                          </div>
                          <a href={d.discoveredUrl} target="_blank" rel="noopener noreferrer"
                            className="text-xs dark:text-zinc-400 text-zinc-500 hover:text-neon-blue flex items-center gap-1 truncate">
                            <ExternalLink className="w-3 h-3 shrink-0" />
                            {d.discoveredUrl}
                          </a>
                          {d.description && (
                            <p className="text-xs dark:text-zinc-500 text-zinc-400 mt-1 line-clamp-2">{d.description}</p>
                          )}
                          {d.duplicateOf && (
                            <p className="text-xs text-orange-400 mt-1">
                              중복: {d.duplicateOf.name} (score: {d.similarityScore?.toFixed(2)})
                            </p>
                          )}
                          {d.errorMessage && (
                            <p className="text-xs text-red-400 mt-1 truncate">{d.errorMessage}</p>
                          )}
                        </div>
                        {d.status === "pending" && (
                          <div className="flex gap-2 shrink-0">
                            <button
                              onClick={() => handleDiscoveryAction(d.id, "approve")}
                              className="p-2 rounded-lg dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600 hover:opacity-80"
                            >
                              <Check className="w-4 h-4" />
                            </button>
                            <button
                              onClick={() => handleDiscoveryAction(d.id, "reject")}
                              className="p-2 rounded-lg dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600 hover:opacity-80"
                            >
                              <X className="w-4 h-4" />
                            </button>
                          </div>
                        )}
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* Edit Requests */}
              {activeTab === "edit-requests" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {editRequests.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">데이터가 없습니다</p>
                  ) : (
                    editRequests.map((r) => (
                      <div key={r.id} className="p-4 flex items-start gap-4">
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-2 mb-1">
                            <p className="text-sm font-medium dark:text-white text-zinc-900">
                              {r.service.name}
                            </p>
                            {statusBadge(r.status)}
                            <span className={`px-2 py-0.5 rounded-md text-xs font-medium
                              ${r.requestType === "claim"
                                ? "dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600"
                                : "dark:bg-purple-500/15 bg-purple-500/10 dark:text-purple-400 text-purple-600"
                              }`}>
                              {r.requestType === "claim" ? "클레임" : "수정"}
                            </span>
                            {r.isVerified && (
                              <span className="text-xs dark:text-emerald-400 text-emerald-600">인증됨</span>
                            )}
                          </div>
                          <p className="text-xs dark:text-zinc-400 text-zinc-500">{r.contactEmail}</p>
                          {r.reason && (
                            <p className="text-xs dark:text-zinc-500 text-zinc-400 mt-1">{r.reason}</p>
                          )}
                          {r.changes && r.changes !== "{}" && (
                            <p className="text-xs dark:text-zinc-500 text-zinc-400 mt-1 font-mono">
                              변경: {r.changes}
                            </p>
                          )}
                        </div>
                        {r.status === "pending" && (
                          <div className="flex gap-2 shrink-0">
                            <button
                              onClick={() => handleEditRequestAction(r.id, "approve")}
                              className="p-2 rounded-lg dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600 hover:opacity-80"
                            >
                              <Check className="w-4 h-4" />
                            </button>
                            <button
                              onClick={() => handleEditRequestAction(r.id, "reject")}
                              className="p-2 rounded-lg dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600 hover:opacity-80"
                            >
                              <X className="w-4 h-4" />
                            </button>
                          </div>
                        )}
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* Sources */}
              {activeTab === "sources" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {sources.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">소스가 없습니다. 크롤링 시 자동 생성됩니다.</p>
                  ) : (
                    sources.map((s) => (
                      <div key={s.id} className="p-4 flex items-center gap-4">
                        <div className="flex-1">
                          <div className="flex items-center gap-2 mb-1">
                            <p className="text-sm font-medium dark:text-white text-zinc-900">{s.name}</p>
                            <span className="px-2 py-0.5 rounded-md text-xs dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500">
                              {s.type}
                            </span>
                            <span className={`px-2 py-0.5 rounded-md text-xs font-medium
                              ${s.isActive
                                ? "dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600"
                                : "dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600"
                              }`}>
                              {s.isActive ? "활성" : "비활성"}
                            </span>
                          </div>
                          <p className="text-xs dark:text-zinc-500 text-zinc-400">
                            우선순위: {s.priority} | 마지막 크롤링: {s.lastCrawled ? new Date(s.lastCrawled).toLocaleString("ko-KR") : "없음"}
                          </p>
                        </div>
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* Crawl Runs */}
              {activeTab === "crawl-runs" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {crawlRuns.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">크롤링 이력이 없습니다</p>
                  ) : (
                    crawlRuns.map((r) => (
                      <div key={r.id} className="p-4">
                        <div className="flex items-center gap-2 mb-2">
                          {statusBadge(r.status)}
                          <span className="text-xs dark:text-zinc-400 text-zinc-500">
                            {new Date(r.startedAt).toLocaleString("ko-KR")}
                            {r.completedAt && ` ~ ${new Date(r.completedAt).toLocaleString("ko-KR")}`}
                          </span>
                        </div>
                        <div className="grid grid-cols-5 gap-3 text-center">
                          <div>
                            <p className="text-lg font-semibold dark:text-white text-zinc-900">{r.sourcesChecked}</p>
                            <p className="text-xs dark:text-zinc-500 text-zinc-400">소스</p>
                          </div>
                          <div>
                            <p className="text-lg font-semibold dark:text-white text-zinc-900">{r.urlsDiscovered}</p>
                            <p className="text-xs dark:text-zinc-500 text-zinc-400">발견</p>
                          </div>
                          <div>
                            <p className="text-lg font-semibold dark:text-white text-zinc-900">{r.urlsNew}</p>
                            <p className="text-xs dark:text-zinc-500 text-zinc-400">신규</p>
                          </div>
                          <div>
                            <p className="text-lg font-semibold dark:text-white text-zinc-900">{r.urlsDuplicate}</p>
                            <p className="text-xs dark:text-zinc-500 text-zinc-400">중복</p>
                          </div>
                          <div>
                            <p className="text-lg font-semibold text-neon-green">{r.servicesCreated}</p>
                            <p className="text-xs dark:text-zinc-500 text-zinc-400">등록</p>
                          </div>
                        </div>
                        {r.errorMessage && (
                          <p className="text-xs text-red-400 mt-2 line-clamp-2">{r.errorMessage}</p>
                        )}
                      </div>
                    ))
                  )}
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
