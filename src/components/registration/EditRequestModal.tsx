"use client";

import { useState } from "react";
import { X, Mail, Loader2, Check, PenLine, UserCheck } from "lucide-react";
import { CATEGORIES, PRICING_MODELS } from "@/constants/categories";

interface EditRequestModalProps {
  serviceId: string;
  serviceName: string;
  currentData: {
    name: string;
    description: string | null;
    category: string;
    pricingModel: string;
  };
  onClose: () => void;
}

type Step = "type" | "form" | "success";

export function EditRequestModal({
  serviceId,
  serviceName,
  currentData,
  onClose,
}: EditRequestModalProps) {
  const [step, setStep] = useState<Step>("type");
  const [requestType, setRequestType] = useState<"claim" | "edit">("edit");
  const [email, setEmail] = useState("");
  const [reason, setReason] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // 수정 요청 필드
  const [newName, setNewName] = useState(currentData.name);
  const [newDescription, setNewDescription] = useState(
    currentData.description || ""
  );
  const [newCategory, setNewCategory] = useState(currentData.category);
  const [newPricingModel, setNewPricingModel] = useState(
    currentData.pricingModel
  );

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    try {
      const changes: Record<string, unknown> = {};
      if (newName !== currentData.name) changes.name = newName;
      if (newDescription !== (currentData.description || ""))
        changes.description = newDescription;
      if (newCategory !== currentData.category) changes.category = newCategory;
      if (newPricingModel !== currentData.pricingModel)
        changes.pricingModel = newPricingModel;

      const res = await fetch("/api/edit-request", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          serviceId,
          requestType,
          contactEmail: email,
          changes,
          reason,
        }),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || "요청에 실패했습니다");
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
      <div
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
      />

      <div className="relative w-full max-w-lg glass dark:bg-zinc-900/90 bg-white/95 rounded-2xl overflow-hidden">
        <div className="flex items-center justify-between p-5 border-b dark:border-white/10 border-black/10">
          <h2 className="text-lg font-semibold dark:text-white text-zinc-900">
            {step === "type" && "요청 유형 선택"}
            {step === "form" &&
              (requestType === "claim"
                ? "서비스 클레임"
                : "정보 수정 요청")}
            {step === "success" && "요청 접수 완료!"}
          </h2>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-lg dark:hover:bg-white/10 hover:bg-black/5 flex items-center justify-center transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        <div className="p-5">
          {/* 스텝 1: 요청 유형 선택 */}
          {step === "type" && (
            <div className="space-y-4">
              <p className="text-sm dark:text-zinc-400 text-zinc-500">
                <strong>{serviceName}</strong>에 대한 요청 유형을 선택해주세요.
              </p>

              <button
                onClick={() => {
                  setRequestType("claim");
                  setStep("form");
                }}
                className="w-full flex items-center gap-4 p-4 rounded-xl border
                  dark:border-white/10 border-black/10
                  dark:hover:bg-white/5 hover:bg-black/5
                  transition-all group text-left"
              >
                <div className="w-10 h-10 rounded-xl dark:bg-neon-blue/15 bg-neon-blue/10 flex items-center justify-center shrink-0">
                  <UserCheck className="w-5 h-5 dark:text-neon-blue text-blue-600" />
                </div>
                <div>
                  <p className="font-medium dark:text-white text-zinc-900 text-sm">
                    서비스 클레임
                  </p>
                  <p className="text-xs dark:text-zinc-500 text-zinc-400 mt-0.5">
                    이 서비스의 개발자/소유자임을 인증합니다
                  </p>
                </div>
              </button>

              <button
                onClick={() => {
                  setRequestType("edit");
                  setStep("form");
                }}
                className="w-full flex items-center gap-4 p-4 rounded-xl border
                  dark:border-white/10 border-black/10
                  dark:hover:bg-white/5 hover:bg-black/5
                  transition-all group text-left"
              >
                <div className="w-10 h-10 rounded-xl dark:bg-neon-purple/15 bg-neon-purple/10 flex items-center justify-center shrink-0">
                  <PenLine className="w-5 h-5 dark:text-neon-purple text-purple-600" />
                </div>
                <div>
                  <p className="font-medium dark:text-white text-zinc-900 text-sm">
                    정보 수정 요청
                  </p>
                  <p className="text-xs dark:text-zinc-500 text-zinc-400 mt-0.5">
                    잘못된 정보를 수정 요청합니다
                  </p>
                </div>
              </button>
            </div>
          )}

          {/* 스텝 2: 폼 입력 */}
          {step === "form" && (
            <div className="space-y-4">
              <div>
                <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">
                  이메일
                </label>
                <div className="flex items-center gap-2 px-3 py-2.5 rounded-xl
                  dark:bg-white/5 bg-black/5
                  dark:border-white/10 border-black/10 border">
                  <Mail className="w-4 h-4 dark:text-zinc-500 text-zinc-400 shrink-0" />
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="email@example.com"
                    className="w-full bg-transparent outline-none text-sm
                      dark:text-white text-zinc-900
                      dark:placeholder-zinc-500 placeholder-zinc-400"
                  />
                </div>
              </div>

              {requestType === "edit" && (
                <div className="space-y-3">
                  <div>
                    <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">
                      서비스 이름
                    </label>
                    <input
                      type="text"
                      value={newName}
                      onChange={(e) => setNewName(e.target.value)}
                      className="w-full px-3 py-2.5 rounded-xl text-sm
                        dark:bg-white/5 bg-black/5
                        dark:border-white/10 border-black/10 border
                        dark:text-white text-zinc-900 outline-none
                        focus:border-neon-blue/50 transition-colors"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">
                      설명
                    </label>
                    <textarea
                      value={newDescription}
                      onChange={(e) => setNewDescription(e.target.value)}
                      rows={3}
                      className="w-full px-3 py-2.5 rounded-xl text-sm resize-none
                        dark:bg-white/5 bg-black/5
                        dark:border-white/10 border-black/10 border
                        dark:text-white text-zinc-900 outline-none
                        focus:border-neon-blue/50 transition-colors"
                    />
                  </div>

                  <div className="grid grid-cols-2 gap-3">
                    <div>
                      <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">
                        카테고리
                      </label>
                      <select
                        value={newCategory}
                        onChange={(e) => setNewCategory(e.target.value)}
                        className="w-full px-3 py-2.5 rounded-xl text-sm
                          dark:bg-white/5 bg-black/5
                          dark:border-white/10 border-black/10 border
                          dark:text-white text-zinc-900 outline-none
                          focus:border-neon-blue/50 transition-colors"
                      >
                        {CATEGORIES.filter((c) => c.id !== "all").map((c) => (
                          <option key={c.id} value={c.id}>
                            {c.nameKo}
                          </option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">
                        가격 모델
                      </label>
                      <select
                        value={newPricingModel}
                        onChange={(e) => setNewPricingModel(e.target.value)}
                        className="w-full px-3 py-2.5 rounded-xl text-sm
                          dark:bg-white/5 bg-black/5
                          dark:border-white/10 border-black/10 border
                          dark:text-white text-zinc-900 outline-none
                          focus:border-neon-blue/50 transition-colors"
                      >
                        {PRICING_MODELS.map((p) => (
                          <option key={p.id} value={p.id}>
                            {p.nameKo}
                          </option>
                        ))}
                      </select>
                    </div>
                  </div>
                </div>
              )}

              <div>
                <label className="block text-xs font-medium dark:text-zinc-400 text-zinc-500 mb-1.5">
                  {requestType === "claim" ? "클레임 사유" : "수정 사유"}
                </label>
                <textarea
                  value={reason}
                  onChange={(e) => setReason(e.target.value)}
                  rows={2}
                  placeholder={
                    requestType === "claim"
                      ? "이 서비스의 개발자임을 증명할 수 있는 정보를 입력해주세요"
                      : "수정이 필요한 이유를 알려주세요"
                  }
                  className="w-full px-3 py-2.5 rounded-xl text-sm resize-none
                    dark:bg-white/5 bg-black/5
                    dark:border-white/10 border-black/10 border
                    dark:text-white text-zinc-900 outline-none
                    focus:border-neon-blue/50 transition-colors
                    dark:placeholder-zinc-500 placeholder-zinc-400"
                />
              </div>

              {error && <p className="text-sm text-red-400">{error}</p>}

              <div className="flex gap-3">
                <button
                  onClick={() => setStep("type")}
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
                  disabled={!email || loading}
                  className="flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-sm font-medium
                    bg-gradient-to-r from-neon-blue to-neon-purple text-white
                    hover:opacity-90 disabled:opacity-40
                    transition-all duration-200"
                >
                  {loading ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <Check className="w-4 h-4" />
                  )}
                  {loading ? "제출 중..." : "제출하기"}
                </button>
              </div>
            </div>
          )}

          {/* 스텝 3: 완료 */}
          {step === "success" && (
            <div className="text-center py-6">
              <div className="w-16 h-16 mx-auto mb-4 rounded-full
                bg-gradient-to-br from-neon-green/20 to-neon-blue/20
                flex items-center justify-center">
                <Check className="w-8 h-8 text-neon-green" />
              </div>
              <h3 className="text-lg font-semibold dark:text-white text-zinc-900 mb-2">
                요청이 접수되었습니다!
              </h3>
              <p className="text-sm dark:text-zinc-400 text-zinc-500 mb-6">
                {requestType === "claim"
                  ? "관리자 검토 후 서비스 소유권이 인증됩니다."
                  : "관리자 검토 후 수정 사항이 반영됩니다."}
              </p>
              <button
                onClick={onClose}
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
