"use client";

import { useState } from "react";
import { X, Globe, Loader2, Check, ChevronRight, Sparkles, AlertTriangle } from "lucide-react";
import { CATEGORIES, PRICING_MODELS } from "@/constants/categories";

interface RegisterModalProps {
  onClose: () => void;
}

type Step = "url" | "preview" | "success";

interface ExtractedData {
  name: string;
  description: string | null;
  ogImageUrl: string | null;
  faviconUrl: string;
  suggestedCategory: string;
  suggestedTags: string[];
}

export function RegisterModal({ onClose }: RegisterModalProps) {
  const [step, setStep] = useState<Step>("url");
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [extracted, setExtracted] = useState<ExtractedData | null>(null);

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("");
  const [pricingModel, setPricingModel] = useState("free");
  const [isKorean, setIsKorean] = useState(false);
  const [duplicateWarning, setDuplicateWarning] = useState<string | null>(null);

  const handleExtract = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/scrape", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || "URL을 분석할 수 없습니다");
      }
      const data: ExtractedData = await res.json();
      setExtracted(data);
      setName(data.name);
      setDescription(data.description || "");
      setCategory(data.suggestedCategory);
      setStep("preview");
    } catch (err) {
      setError(err instanceof Error ? err.message : "오류가 발생했습니다");
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setDuplicateWarning(null);
    try {
      const res = await fetch("/api/services", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          url,
          name,
          description,
          category,
          pricingModel,
          isKorean,
          tags: extracted?.suggestedTags || [],
          faviconUrl: extracted?.faviconUrl,
          ogImageUrl: extracted?.ogImageUrl,
          logoUrl: extracted?.ogImageUrl || extracted?.faviconUrl,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        // 중복 감지 시 상세 정보 표시
        if (res.status === 409 && data.duplicate) {
          const dupInfo = data.duplicate;
          setError(
            `유사한 서비스가 이미 존재합니다: "${dupInfo.matchedServiceName}" (유사도: ${Math.round(dupInfo.similarityScore * 100)}%)`
          );
        } else {
          throw new Error(data.error || "등록에 실패했습니다");
        }
        return;
      }
      // 경고가 있으면 표시
      if (data.warning) {
        setDuplicateWarning(data.warning.message);
      }
      setStep("success");
    } catch (err) {
      setError(err instanceof Error ? err.message : "오류가 발생했습니다");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-[60] flex items-center justify-center p-4">
      <div className="absolute inset-0 bg-black/60 backdrop-blur-sm" />

      <div className="relative w-full max-w-lg glass dark:bg-zinc-900/90 bg-white/95 rounded-2xl overflow-hidden max-h-[90vh] overflow-y-auto">
        <div className="flex items-center justify-between p-5 border-b dark:border-white/10 border-black/10">
          <h2 className="text-lg font-semibold dark:text-white text-zinc-900">
            {step === "url" && "AI 서비스 등록"}
            {step === "preview" && "정보 확인"}
            {step === "success" && "등록 완료!"}
          </h2>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-lg dark:hover:bg-white/10 hover:bg-black/5 flex items-center justify-center transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        <div className="p-5">
          {step === "url" && (
            <div className="space-y-4">
              <p className="text-sm dark:text-zinc-400 text-zinc-500">
                서비스 URL만 입력하면 나머지 정보는 자동으로 추출됩니다.
              </p>
              <div className="neon-border rounded-xl">
                <div className="flex items-center gap-3 glass px-4 py-3">
                  <Globe className="w-5 h-5 dark:text-zinc-400 text-zinc-500 shrink-0" />
                  <input
                    type="url"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="https://example.com"
                    className="w-full bg-transparent outline-none text-sm
                      dark:text-white text-zinc-900
                      dark:placeholder-zinc-500 placeholder-zinc-400"
                    onKeyDown={(e) => e.key === "Enter" && url && handleExtract()}
                  />
                </div>
              </div>
              {error && (
                <p className="text-sm text-red-400">{error}</p>
              )}
              <button
                onClick={handleExtract}
                disabled={!url || loading}
                className="w-full flex items-center justify-center gap-2 py-3 rounded-xl text-sm font-medium
                  bg-gradient-to-r from-neon-blue to-neon-purple text-white
                  hover:opacity-90 disabled:opacity-40
                  transition-all duration-200"
              >
                {loading ? (
                  <Loader2 className="w-4 h-4 animate-spin" />
                ) : (
                  <Sparkles className="w-4 h-4" />
                )}
                {loading ? "분석 중..." : "URL 분석하기"}
              </button>
            </div>
          )}

          {step === "preview" && (
            <div className="space-y-4">
              <div className="flex items-center gap-3 p-3 rounded-xl dark:bg-white/5 bg-black/5">
                {extracted?.faviconUrl && (
                  <img
                    src={extracted.faviconUrl}
                    alt=""
                    className="w-10 h-10 rounded-lg"
                    onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }}
                  />
                )}
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium dark:text-white text-zinc-900 truncate">{url}</p>
                  <p className="text-xs dark:text-zinc-500 text-zinc-400">자동 추출된 정보를 확인해주세요</p>
                </div>
              </div>

              <div className="space-y-3">
                <div>
                  <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">서비스 이름</label>
                  <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full px-3 py-2.5 rounded-xl text-sm
                      dark:bg-white/5 bg-black/5
                      dark:border-white/10 border-black/10 border
                      dark:text-white text-zinc-900 outline-none
                      focus:border-neon-blue/50 transition-colors"
                  />
                </div>

                <div>
                  <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">설명</label>
                  <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    rows={3}
                    className="w-full px-3 py-2.5 rounded-xl text-sm resize-none
                      dark:bg-white/5 bg-black/5
                      dark:border-white/10 border-black/10 border
                      dark:text-white text-zinc-900 outline-none
                      focus:border-neon-blue/50 transition-colors"
                  />
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">카테고리</label>
                    <select
                      value={category}
                      onChange={(e) => setCategory(e.target.value)}
                      className="w-full px-3 py-2.5 rounded-xl text-sm
                        dark:bg-white/5 bg-black/5
                        dark:border-white/10 border-black/10 border
                        dark:text-white text-zinc-900 outline-none
                        focus:border-neon-blue/50 transition-colors"
                    >
                      {CATEGORIES.filter((c) => c.id !== "all").map((c) => (
                        <option key={c.id} value={c.id}>{c.nameKo}</option>
                      ))}
                    </select>
                  </div>

                  <div>
                    <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">가격 모델</label>
                    <select
                      value={pricingModel}
                      onChange={(e) => setPricingModel(e.target.value)}
                      className="w-full px-3 py-2.5 rounded-xl text-sm
                        dark:bg-white/5 bg-black/5
                        dark:border-white/10 border-black/10 border
                        dark:text-white text-zinc-900 outline-none
                        focus:border-neon-blue/50 transition-colors"
                    >
                      {PRICING_MODELS.map((p) => (
                        <option key={p.id} value={p.id}>{p.nameKo}</option>
                      ))}
                    </select>
                  </div>
                </div>

                <label className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={isKorean}
                    onChange={(e) => setIsKorean(e.target.checked)}
                    className="w-4 h-4 rounded accent-neon-blue"
                  />
                  <span className="text-sm dark:text-zinc-300 text-zinc-600">한국 서비스</span>
                </label>
              </div>

              {error && <p className="text-sm text-red-400">{error}</p>}

              <div className="flex gap-3">
                <button
                  onClick={() => setStep("url")}
                  className="flex-1 py-3 rounded-xl text-sm font-medium
                    dark:bg-white/5 bg-black/5
                    dark:text-zinc-300 text-zinc-600
                    dark:hover:bg-white/10 hover:bg-black/10
                    transition-all duration-200"
                >
                  뒤로
                </button>
                <button
                  onClick={handleSubmit}
                  disabled={!name || !category || loading}
                  className="flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-sm font-medium
                    bg-gradient-to-r from-neon-blue to-neon-purple text-white
                    hover:opacity-90 disabled:opacity-40
                    transition-all duration-200"
                >
                  {loading ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <ChevronRight className="w-4 h-4" />
                  )}
                  {loading ? "등록 중..." : "등록하기"}
                </button>
              </div>
            </div>
          )}

          {step === "success" && (
            <div className="text-center py-6">
              <div className="w-16 h-16 mx-auto mb-4 rounded-full
                bg-gradient-to-br from-neon-green/20 to-neon-blue/20
                flex items-center justify-center">
                <Check className="w-8 h-8 text-neon-green" />
              </div>
              <h3 className="text-lg font-semibold dark:text-white text-zinc-900 mb-2">
                등록이 완료되었습니다!
              </h3>
              <p className="text-sm dark:text-zinc-400 text-zinc-500 mb-4">
                서비스가 성공적으로 등록되었습니다.
              </p>
              {duplicateWarning && (
                <div className="flex items-start gap-2 p-3 rounded-xl dark:bg-orange-500/10 bg-orange-500/5 mb-4">
                  <AlertTriangle className="w-4 h-4 text-orange-400 shrink-0 mt-0.5" />
                  <p className="text-xs dark:text-orange-300 text-orange-600">{duplicateWarning}</p>
                </div>
              )}
              <button
                onClick={() => { onClose(); window.location.reload(); }}
                className="px-6 py-3 rounded-xl text-sm font-medium
                  bg-gradient-to-r from-neon-blue to-neon-purple text-white
                  hover:opacity-90 transition-all duration-200"
              >
                확인
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
