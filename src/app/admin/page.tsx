"use client";

import { useState, useEffect, useCallback, Suspense } from "react";
import {
  Globe, FileEdit, Database, Activity, MessageSquare, AlertTriangle, Mail,
  Check, X, ExternalLink, Loader2, RefreshCw, Eye, EyeOff, Trash2, ThumbsUp, ThumbsDown,
  LogOut, Lock,
} from "lucide-react";

type Tab = "discoveries" | "edit-requests" | "sources" | "crawl-runs" | "feedback" | "reports" | "comments";

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

interface FeedbackItem {
  id: string;
  type: string;
  email: string | null;
  message: string;
  senderIp: string;
  status: string;
  createdAt: string;
}

interface ReportedComment {
  id: string;
  content: string;
  authorName: string;
  authorIp: string;
  reports: number;
  isHidden: boolean;
  isDeleted: boolean;
  createdAt: string;
  service: { id: string; name: string; slug: string };
  commentReports: { id: string; reporterIp: string; reason: string | null; createdAt: string }[];
}

interface AdminComment {
  id: string;
  content: string;
  authorName: string;
  authorIp: string;
  reports: number;
  isHidden: boolean;
  isDeleted: boolean;
  likes: number;
  dislikes: number;
  parentId: string | null;
  createdAt: string;
  service: { id: string; name: string; slug: string };
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

/* ============================
   로그인 화면
   ============================ */
function LoginForm({ onLogin }: { onLogin: () => void }) {
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await fetch("/api/admin/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, password }),
      });
      const data = await res.json();

      if (res.ok && data.success) {
        onLogin();
      } else {
        setError(data.error || "로그인에 실패했습니다");
      }
    } catch {
      setError("서버에 연결할 수 없습니다");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center dark:bg-zinc-950 bg-zinc-50">
      <div className="glass p-8 w-full max-w-sm">
        <div className="flex items-center justify-center gap-2 mb-6">
          <Lock className="w-6 h-6 text-neon-blue" />
          <h1 className="text-xl font-bold dark:text-white text-zinc-900">Admin Login</h1>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium dark:text-zinc-300 text-zinc-700 mb-1">
              아이디
            </label>
            <input
              type="text"
              value={id}
              onChange={(e) => setId(e.target.value)}
              className="w-full px-4 py-2.5 rounded-xl text-sm
                dark:bg-white/5 bg-black/5
                dark:text-white text-zinc-900
                dark:border-white/10 border-black/10 border
                focus:outline-none focus:ring-2 focus:ring-neon-blue/50"
              placeholder="관리자 ID"
              autoComplete="username"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium dark:text-zinc-300 text-zinc-700 mb-1">
              비밀번호
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-2.5 rounded-xl text-sm
                dark:bg-white/5 bg-black/5
                dark:text-white text-zinc-900
                dark:border-white/10 border-black/10 border
                focus:outline-none focus:ring-2 focus:ring-neon-blue/50"
              placeholder="비밀번호"
              autoComplete="current-password"
              required
            />
          </div>

          {error && (
            <p className="text-sm text-red-400 text-center">{error}</p>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2.5 rounded-xl text-sm font-medium
              bg-gradient-to-r from-neon-blue to-neon-purple text-white
              hover:opacity-90 transition-opacity
              disabled:opacity-50 flex items-center justify-center gap-2"
          >
            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : null}
            {loading ? "로그인 중..." : "로그인"}
          </button>
        </form>
      </div>
    </div>
  );
}

/* ============================
   메인 어드민 페이지
   ============================ */
function AdminPage() {
  const [authenticated, setAuthenticated] = useState<boolean | null>(null);
  const [activeTab, setActiveTab] = useState<Tab>("feedback");
  const [loading, setLoading] = useState(false);

  // Data — 기존
  const [discoveries, setDiscoveries] = useState<DiscoveryLog[]>([]);
  const [editRequests, setEditRequests] = useState<EditRequestItem[]>([]);
  const [sources, setSources] = useState<SourceItem[]>([]);
  const [crawlRuns, setCrawlRuns] = useState<CrawlRunItem[]>([]);
  const [statusFilter, setStatusFilter] = useState<string>("");

  // Data — 신규
  const [feedbackList, setFeedbackList] = useState<FeedbackItem[]>([]);
  const [reportedComments, setReportedComments] = useState<ReportedComment[]>([]);
  const [adminComments, setAdminComments] = useState<AdminComment[]>([]);
  const [commentFilter, setCommentFilter] = useState<string>("");
  const [reportHiddenOnly, setReportHiddenOnly] = useState(false);

  // 세션 확인
  useEffect(() => {
    fetch("/api/admin/session")
      .then((r) => r.json())
      .then((data) => setAuthenticated(data.authenticated))
      .catch(() => setAuthenticated(false));
  }, []);

  const fetchData = useCallback(async () => {
    if (!authenticated) return;
    setLoading(true);
    try {
      const statusParam = statusFilter ? `&status=${statusFilter}` : "";
      switch (activeTab) {
        case "discoveries": {
          const res = await fetch(`/api/admin/discoveries?${statusParam}`);
          const data = await res.json();
          setDiscoveries(data.items || []);
          break;
        }
        case "edit-requests": {
          const res = await fetch(`/api/admin/edit-requests?${statusParam}`);
          const data = await res.json();
          setEditRequests(data.items || []);
          break;
        }
        case "sources": {
          const res = await fetch(`/api/admin/sources`);
          const data = await res.json();
          setSources(data.items || []);
          break;
        }
        case "crawl-runs": {
          const res = await fetch(`/api/admin/crawl-runs`);
          const data = await res.json();
          setCrawlRuns(data.items || []);
          break;
        }
        case "feedback": {
          const res = await fetch(`/api/admin/feedback?${statusParam}`);
          const data = await res.json();
          setFeedbackList(data.items || []);
          break;
        }
        case "reports": {
          const hiddenParam = reportHiddenOnly ? "hidden=true" : "";
          const res = await fetch(`/api/admin/reports?${hiddenParam}`);
          const data = await res.json();
          setReportedComments(data.items || []);
          break;
        }
        case "comments": {
          const filterParam = commentFilter ? `filter=${commentFilter}` : "";
          const res = await fetch(`/api/admin/comments?${filterParam}`);
          const data = await res.json();
          setAdminComments(data.items || []);
          break;
        }
      }
    } catch (err) {
      console.error("Fetch error:", err);
    } finally {
      setLoading(false);
    }
  }, [authenticated, activeTab, statusFilter, reportHiddenOnly, commentFilter]);

  useEffect(() => { fetchData(); }, [fetchData]);

  // Actions
  const handleDiscoveryAction = async (id: string, action: "approve" | "reject") => {
    try {
      await fetch(`/api/admin/discoveries/${id}`, {
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
      await fetch(`/api/admin/edit-requests/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action }),
      });
      fetchData();
    } catch (err) {
      console.error("Action error:", err);
    }
  };

  const handleFeedbackStatus = async (id: string, status: string) => {
    try {
      await fetch(`/api/admin/feedback`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, status }),
      });
      fetchData();
    } catch (err) {
      console.error("Feedback action error:", err);
    }
  };

  const handleCommentAction = async (api: string, commentId: string, action: string) => {
    try {
      await fetch(`/api/admin/${api}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ commentId, action }),
      });
      fetchData();
    } catch (err) {
      console.error("Comment action error:", err);
    }
  };

  const handleLogout = async () => {
    await fetch("/api/admin/logout", { method: "POST" });
    setAuthenticated(false);
  };

  // 로딩 중
  if (authenticated === null) {
    return (
      <div className="min-h-screen flex items-center justify-center dark:bg-zinc-950 bg-zinc-50">
        <Loader2 className="w-8 h-8 animate-spin dark:text-zinc-400 text-zinc-500" />
      </div>
    );
  }

  // 로그인 필요
  if (!authenticated) {
    return <LoginForm onLogin={() => setAuthenticated(true)} />;
  }

  const tabs: { id: Tab; label: string; icon: React.ReactNode }[] = [
    { id: "feedback", label: "문의/의견", icon: <Mail className="w-4 h-4" /> },
    { id: "reports", label: "댓글 신고", icon: <AlertTriangle className="w-4 h-4" /> },
    { id: "comments", label: "댓글 관리", icon: <MessageSquare className="w-4 h-4" /> },
    { id: "edit-requests", label: "수정 요청", icon: <FileEdit className="w-4 h-4" /> },
    { id: "discoveries", label: "발견 목록", icon: <Globe className="w-4 h-4" /> },
    { id: "sources", label: "소스 관리", icon: <Database className="w-4 h-4" /> },
    { id: "crawl-runs", label: "크롤링 이력", icon: <Activity className="w-4 h-4" /> },
  ];

  const statusBadge = (status: string) => {
    const colors: Record<string, string> = {
      pending: "dark:bg-yellow-500/15 bg-yellow-500/10 dark:text-yellow-400 text-yellow-600",
      approved: "dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600",
      rejected: "dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600",
      reviewed: "dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600",
      resolved: "dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600",
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

  const formatDate = (dateStr: string) => {
    return new Date(dateStr).toLocaleString("ko-KR", {
      year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit",
    });
  };

  return (
    <div className="min-h-screen dark:bg-zinc-950 bg-zinc-50 p-4 md:p-8">
      <div className="max-w-6xl mx-auto">
        <div className="flex items-center justify-between mb-8">
          <h1 className="text-2xl font-bold dark:text-white text-zinc-900">Admin Dashboard</h1>
          <div className="flex items-center gap-2">
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
            <button
              onClick={handleLogout}
              className="flex items-center gap-2 px-4 py-2 rounded-xl text-sm
                dark:bg-red-500/10 bg-red-500/5
                dark:text-red-400 text-red-600
                dark:hover:bg-red-500/20 hover:bg-red-500/10
                transition-all"
            >
              <LogOut className="w-4 h-4" />
              로그아웃
            </button>
          </div>
        </div>

        {/* Tabs */}
        <div className="flex gap-2 mb-6 overflow-x-auto pb-1">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => { setActiveTab(tab.id); setStatusFilter(""); setCommentFilter(""); setReportHiddenOnly(false); }}
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

        {/* Status filter — 기존 탭들 */}
        {(activeTab === "discoveries" || activeTab === "edit-requests") && (
          <div className="flex gap-2 mb-4 flex-wrap">
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

        {/* Feedback 필터 */}
        {activeTab === "feedback" && (
          <div className="flex gap-2 mb-4 flex-wrap">
            {["", "pending", "reviewed", "resolved"].map((s) => (
              <button
                key={s}
                onClick={() => setStatusFilter(s)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all
                  ${statusFilter === s
                    ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
                    : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500"
                  }`}
              >
                {s === "" ? "전체" : s === "pending" ? "대기" : s === "reviewed" ? "확인됨" : "해결됨"}
              </button>
            ))}
          </div>
        )}

        {/* Reports 필터 */}
        {activeTab === "reports" && (
          <div className="flex gap-2 mb-4">
            <button
              onClick={() => setReportHiddenOnly(false)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all
                ${!reportHiddenOnly
                  ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
                  : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500"
                }`}
            >
              전체 신고
            </button>
            <button
              onClick={() => setReportHiddenOnly(true)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all
                ${reportHiddenOnly
                  ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
                  : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500"
                }`}
            >
              숨김된 댓글만
            </button>
          </div>
        )}

        {/* Comments 필터 */}
        {activeTab === "comments" && (
          <div className="flex gap-2 mb-4 flex-wrap">
            {[
              { value: "", label: "전체" },
              { value: "hidden", label: "숨김" },
              { value: "deleted", label: "삭제됨" },
            ].map((f) => (
              <button
                key={f.value}
                onClick={() => setCommentFilter(f.value)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all
                  ${commentFilter === f.value
                    ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-blue-600"
                    : "dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500"
                  }`}
              >
                {f.label}
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
              {/* ===== 문의/의견 (Feedback) ===== */}
              {activeTab === "feedback" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {feedbackList.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">문의/의견이 없습니다</p>
                  ) : (
                    feedbackList.map((f) => (
                      <div key={f.id} className="p-4 flex items-start gap-4">
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-2 mb-1">
                            <span className={`px-2 py-0.5 rounded-md text-xs font-medium
                              ${f.type === "partnership"
                                ? "dark:bg-purple-500/15 bg-purple-500/10 dark:text-purple-400 text-purple-600"
                                : "dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600"
                              }`}
                            >
                              {f.type === "partnership" ? "제휴" : "의견"}
                            </span>
                            {statusBadge(f.status)}
                            <span className="text-xs dark:text-zinc-500 text-zinc-400">
                              {formatDate(f.createdAt)}
                            </span>
                          </div>
                          {f.email && (
                            <p className="text-xs dark:text-zinc-400 text-zinc-500 mb-1">{f.email}</p>
                          )}
                          <p className="text-sm dark:text-zinc-300 text-zinc-700 whitespace-pre-wrap">{f.message}</p>
                        </div>
                        {f.status === "pending" && (
                          <div className="flex gap-2 shrink-0">
                            <button
                              onClick={() => handleFeedbackStatus(f.id, "reviewed")}
                              className="px-3 py-1.5 rounded-lg text-xs font-medium
                                dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600 hover:opacity-80"
                            >
                              확인
                            </button>
                            <button
                              onClick={() => handleFeedbackStatus(f.id, "resolved")}
                              className="px-3 py-1.5 rounded-lg text-xs font-medium
                                dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600 hover:opacity-80"
                            >
                              해결
                            </button>
                          </div>
                        )}
                        {f.status === "reviewed" && (
                          <button
                            onClick={() => handleFeedbackStatus(f.id, "resolved")}
                            className="px-3 py-1.5 rounded-lg text-xs font-medium shrink-0
                              dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600 hover:opacity-80"
                          >
                            해결 완료
                          </button>
                        )}
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* ===== 댓글 신고 (Reports) ===== */}
              {activeTab === "reports" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {reportedComments.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">신고된 댓글이 없습니다</p>
                  ) : (
                    reportedComments.map((c) => (
                      <div key={c.id} className="p-4">
                        <div className="flex items-start gap-4">
                          <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2 mb-1 flex-wrap">
                              <span className="text-sm font-medium dark:text-white text-zinc-900">
                                {c.authorName}
                              </span>
                              <span className="text-xs dark:text-zinc-500 text-zinc-400">
                                {c.authorIp}
                              </span>
                              <span className="px-2 py-0.5 rounded-md text-xs font-medium dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600">
                                신고 {c.reports}건
                              </span>
                              {c.isHidden && (
                                <span className="px-2 py-0.5 rounded-md text-xs font-medium dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600">
                                  숨김
                                </span>
                              )}
                              {c.isDeleted && (
                                <span className="px-2 py-0.5 rounded-md text-xs font-medium dark:bg-zinc-500/15 bg-zinc-500/10 dark:text-zinc-400 text-zinc-500">
                                  삭제됨
                                </span>
                              )}
                            </div>
                            <p className="text-xs dark:text-zinc-400 text-zinc-500 mb-1">
                              서비스: <a href={`/service/${c.service.slug}`} target="_blank" rel="noopener noreferrer" className="text-neon-blue hover:underline">{c.service.name}</a>
                              {" · "}{formatDate(c.createdAt)}
                            </p>
                            {!c.isDeleted && (
                              <p className="text-sm dark:text-zinc-300 text-zinc-700 mb-2 whitespace-pre-wrap">{c.content}</p>
                            )}
                            {c.commentReports.length > 0 && (
                              <div className="mt-2 space-y-1">
                                <p className="text-xs font-medium dark:text-zinc-400 text-zinc-500">신고 사유:</p>
                                {c.commentReports.map((r) => (
                                  <p key={r.id} className="text-xs dark:text-zinc-500 text-zinc-400 pl-2 border-l-2 dark:border-zinc-700 border-zinc-300">
                                    {r.reporterIp} · {r.reason || "사유 없음"} · {formatDate(r.createdAt)}
                                  </p>
                                ))}
                              </div>
                            )}
                          </div>
                          {!c.isDeleted && (
                            <div className="flex flex-col gap-2 shrink-0">
                              {c.isHidden ? (
                                <button
                                  onClick={() => handleCommentAction("reports", c.id, "unhide")}
                                  className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                                    dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600 hover:opacity-80"
                                >
                                  <Eye className="w-3 h-3" /> 숨김 해제
                                </button>
                              ) : (
                                <button
                                  onClick={() => handleCommentAction("reports", c.id, "hide")}
                                  className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                                    dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600 hover:opacity-80"
                                >
                                  <EyeOff className="w-3 h-3" /> 숨김
                                </button>
                              )}
                              <button
                                onClick={() => handleCommentAction("reports", c.id, "delete")}
                                className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                                  dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600 hover:opacity-80"
                              >
                                <Trash2 className="w-3 h-3" /> 삭제
                              </button>
                            </div>
                          )}
                        </div>
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* ===== 댓글 관리 (Comments) ===== */}
              {activeTab === "comments" && (
                <div className="divide-y dark:divide-white/5 divide-black/5">
                  {adminComments.length === 0 ? (
                    <p className="p-8 text-center text-sm dark:text-zinc-500 text-zinc-400">댓글이 없습니다</p>
                  ) : (
                    adminComments.map((c) => (
                      <div key={c.id} className="p-4 flex items-start gap-4">
                        <div className="flex-1 min-w-0">
                          <div className="flex items-center gap-2 mb-1 flex-wrap">
                            <span className="text-sm font-medium dark:text-white text-zinc-900">
                              {c.authorName || "삭제됨"}
                            </span>
                            <span className="text-xs dark:text-zinc-500 text-zinc-400">
                              {c.authorIp}
                            </span>
                            {c.isHidden && (
                              <span className="px-2 py-0.5 rounded-md text-xs font-medium dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600">
                                숨김
                              </span>
                            )}
                            {c.isDeleted && (
                              <span className="px-2 py-0.5 rounded-md text-xs font-medium dark:bg-zinc-500/15 bg-zinc-500/10 dark:text-zinc-400 text-zinc-500">
                                삭제됨
                              </span>
                            )}
                            {c.reports > 0 && (
                              <span className="px-2 py-0.5 rounded-md text-xs font-medium dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600">
                                신고 {c.reports}
                              </span>
                            )}
                            {c.parentId && (
                              <span className="px-2 py-0.5 rounded-md text-xs dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500">
                                답글
                              </span>
                            )}
                          </div>
                          <p className="text-xs dark:text-zinc-400 text-zinc-500 mb-1">
                            <a href={`/service/${c.service.slug}`} target="_blank" rel="noopener noreferrer" className="text-neon-blue hover:underline">{c.service.name}</a>
                            {" · "}{formatDate(c.createdAt)}
                            {" · "}
                            <span className="inline-flex items-center gap-0.5"><ThumbsUp className="w-3 h-3" /> {c.likes}</span>
                            {" "}
                            <span className="inline-flex items-center gap-0.5"><ThumbsDown className="w-3 h-3" /> {c.dislikes}</span>
                          </p>
                          {!c.isDeleted && (
                            <p className="text-sm dark:text-zinc-300 text-zinc-700 whitespace-pre-wrap">{c.content}</p>
                          )}
                        </div>
                        {!c.isDeleted && (
                          <div className="flex flex-col gap-2 shrink-0">
                            {c.isHidden ? (
                              <button
                                onClick={() => handleCommentAction("comments", c.id, "unhide")}
                                className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                                  dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600 hover:opacity-80"
                              >
                                <Eye className="w-3 h-3" /> 해제
                              </button>
                            ) : (
                              <button
                                onClick={() => handleCommentAction("comments", c.id, "hide")}
                                className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                                  dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600 hover:opacity-80"
                              >
                                <EyeOff className="w-3 h-3" /> 숨김
                              </button>
                            )}
                            <button
                              onClick={() => handleCommentAction("comments", c.id, "delete")}
                              className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                                dark:bg-red-500/15 bg-red-500/10 dark:text-red-400 text-red-600 hover:opacity-80"
                            >
                              <Trash2 className="w-3 h-3" /> 삭제
                            </button>
                          </div>
                        )}
                      </div>
                    ))
                  )}
                </div>
              )}

              {/* ===== 기존 탭들 ===== */}

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
