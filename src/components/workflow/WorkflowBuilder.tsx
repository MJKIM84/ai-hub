"use client";

import { useState, useEffect, useCallback } from "react";
import {
  Search, Save, FolderOpen, Trash2, Share2,
  ChevronDown, ChevronRight, Plus, Workflow,
} from "lucide-react";
import { PipelineStage } from "./PipelineStage";
import { PipeConnector } from "./PipeConnector";
import { CATEGORIES } from "@/constants/categories";
import {
  saveWorkflow, loadWorkflows, deleteWorkflow, encodeWorkflow,
  MAX_STAGES,
} from "@/lib/workflows";
import type { WorkflowStage, SavedWorkflow } from "@/lib/workflows";

interface ServiceItem {
  id: string;
  name: string;
  category: string;
  logoUrl: string | null;
  faviconUrl: string | null;
  ogImageUrl: string | null;
}

interface WorkflowBuilderProps {
  services: ServiceItem[];
}

export function WorkflowBuilder({ services }: WorkflowBuilderProps) {
  const [stages, setStages] = useState<WorkflowStage[]>([]);
  const [search, setSearch] = useState("");
  const [expandedCats, setExpandedCats] = useState<Set<string>>(new Set());
  const [savedList, setSavedList] = useState<SavedWorkflow[]>([]);
  const [showSaved, setShowSaved] = useState(false);
  const [saveName, setSaveName] = useState("");
  const [showSaveInput, setShowSaveInput] = useState(false);
  const [shareUrl, setShareUrl] = useState("");
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    setSavedList(loadWorkflows());
    setIsMobile(window.innerWidth < 768);
    const handleResize = () => setIsMobile(window.innerWidth < 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // 카테고리별 서비스 그룹핑
  const grouped = CATEGORIES.filter((c) => c.id !== "all").map((cat) => ({
    ...cat,
    services: services.filter((s) => s.category === cat.id),
  })).filter((g) => g.services.length > 0);

  // 검색 필터
  const filteredGroups = search.trim()
    ? grouped.map((g) => ({
        ...g,
        services: g.services.filter((s) =>
          s.name.toLowerCase().includes(search.toLowerCase())
        ),
      })).filter((g) => g.services.length > 0)
    : grouped;

  const toggleCat = (catId: string) => {
    setExpandedCats((prev) => {
      const next = new Set(prev);
      if (next.has(catId)) next.delete(catId);
      else next.add(catId);
      return next;
    });
  };

  // 서비스 → 파이프라인에 추가
  const addStage = useCallback((service: ServiceItem) => {
    if (stages.length >= MAX_STAGES) return;
    setStages((prev) => [
      ...prev,
      {
        serviceId: service.id,
        serviceName: service.name,
        serviceCategory: service.category,
        serviceLogo: service.logoUrl || service.faviconUrl || service.ogImageUrl || undefined,
      },
    ]);
  }, [stages.length]);

  const removeStage = (index: number) => {
    setStages((prev) => prev.filter((_, i) => i !== index));
  };

  // 드래그 & 드롭 재정렬
  const [dragIdx, setDragIdx] = useState<number | null>(null);

  const handleDragStart = (_e: React.DragEvent, index: number) => {
    setDragIdx(index);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
  };

  const handleDrop = (_e: React.DragEvent, targetIndex: number) => {
    if (dragIdx === null || dragIdx === targetIndex) return;
    setStages((prev) => {
      const next = [...prev];
      const [moved] = next.splice(dragIdx, 1);
      next.splice(targetIndex, 0, moved);
      return next;
    });
    setDragIdx(null);
  };

  // 좌측 패널 → 캔버스 드롭
  const handleCanvasDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "copy";
  };

  const handleCanvasDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const serviceId = e.dataTransfer.getData("text/service-id");
    if (!serviceId) return;
    const service = services.find((s) => s.id === serviceId);
    if (service) addStage(service);
  };

  // 서비스 아이템 드래그
  const handleServiceDragStart = (e: React.DragEvent, service: ServiceItem) => {
    e.dataTransfer.setData("text/service-id", service.id);
    e.dataTransfer.effectAllowed = "copy";
  };

  // 저장/불러오기
  const handleSave = () => {
    if (!saveName.trim() || stages.length === 0) return;
    saveWorkflow(saveName.trim(), stages);
    setSavedList(loadWorkflows());
    setShowSaveInput(false);
    setSaveName("");
  };

  const handleLoad = (wf: SavedWorkflow) => {
    setStages(wf.stages);
    setShowSaved(false);
  };

  const handleDelete = (name: string) => {
    deleteWorkflow(name);
    setSavedList(loadWorkflows());
  };

  const handleShare = () => {
    if (stages.length === 0) return;
    const hash = encodeWorkflow(stages);
    const url = `${window.location.origin}/workflow#${hash}`;
    setShareUrl(url);
    navigator.clipboard?.writeText(url);
  };

  const handleClear = () => {
    setStages([]);
    setShareUrl("");
  };

  return (
    <div className="flex flex-col md:flex-row gap-6 max-w-7xl mx-auto">
      {/* 좌측 패널 — 서비스 목록 */}
      <div className="w-full md:w-72 shrink-0">
        <div className="glass rounded-xl p-4 md:sticky md:top-20 md:max-h-[calc(100vh-6rem)] md:overflow-y-auto">
          <div className="flex items-center gap-2 px-3 py-2 rounded-lg mb-3
            dark:bg-white/5 bg-black/5 border dark:border-white/5 border-black/5">
            <Search className="w-4 h-4 dark:text-zinc-500 text-zinc-400 shrink-0" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="AI 서비스 검색..."
              className="w-full bg-transparent outline-none text-sm
                dark:text-white text-zinc-900 dark:placeholder-zinc-500 placeholder-zinc-400"
            />
          </div>

          <div className="space-y-1">
            {filteredGroups.map((group) => (
              <div key={group.id}>
                <button
                  onClick={() => toggleCat(group.id)}
                  className="flex items-center justify-between w-full px-3 py-2 rounded-lg text-sm
                    dark:text-zinc-300 text-zinc-700 dark:hover:bg-white/5 hover:bg-black/5 transition-colors"
                >
                  <span className="font-medium">{group.nameKo} ({group.services.length})</span>
                  {expandedCats.has(group.id) ? (
                    <ChevronDown className="w-4 h-4 dark:text-zinc-500 text-zinc-400" />
                  ) : (
                    <ChevronRight className="w-4 h-4 dark:text-zinc-500 text-zinc-400" />
                  )}
                </button>
                {expandedCats.has(group.id) && (
                  <div className="ml-2 space-y-0.5 mb-2">
                    {group.services.map((service) => {
                      const logo = service.logoUrl || service.faviconUrl || service.ogImageUrl;
                      return (
                        <div
                          key={service.id}
                          draggable
                          onDragStart={(e) => handleServiceDragStart(e, service)}
                          onClick={() => addStage(service)}
                          className="flex items-center gap-2 px-3 py-1.5 rounded-lg cursor-pointer
                            dark:hover:bg-white/5 hover:bg-black/5 transition-colors group/item"
                        >
                          <div className="w-6 h-6 rounded overflow-hidden shrink-0
                            dark:bg-white/10 bg-black/5 flex items-center justify-center">
                            {logo ? (
                              <img src={logo} alt="" className="w-full h-full object-cover" />
                            ) : (
                              <span className="text-[10px] font-bold dark:text-zinc-500 text-zinc-400">
                                {service.name[0]}
                              </span>
                            )}
                          </div>
                          <span className="text-xs dark:text-zinc-400 text-zinc-500 truncate flex-1">
                            {service.name}
                          </span>
                          <Plus className="w-3 h-3 dark:text-zinc-600 text-zinc-300
                            group-hover/item:dark:text-neon-blue group-hover/item:text-neon-blue
                            transition-colors shrink-0" />
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* 우측 — 캔버스 + 하단바 */}
      <div className="flex-1 min-w-0">
        {/* 캔버스 */}
        <div
          onDragOver={handleCanvasDragOver}
          onDrop={handleCanvasDrop}
          className="glass rounded-xl p-6 min-h-[300px] md:min-h-[400px] flex items-center justify-center"
        >
          {stages.length === 0 ? (
            <div className="text-center py-10">
              <Workflow className="w-12 h-12 mx-auto mb-4 dark:text-zinc-600 text-zinc-300" />
              <p className="text-sm dark:text-zinc-500 text-zinc-400 mb-1">
                좌측에서 AI 서비스를 드래그하거나 클릭하여 추가하세요
              </p>
              <p className="text-xs dark:text-zinc-600 text-zinc-400">
                최대 {MAX_STAGES}개까지 추가할 수 있습니다
              </p>
            </div>
          ) : (
            <div className={`flex ${isMobile ? "flex-col items-center" : "flex-row items-center"} flex-wrap gap-2`}>
              {stages.map((stage, i) => (
                <div key={`${stage.serviceId}-${i}`} className={`flex ${isMobile ? "flex-col" : "flex-row"} items-center`}>
                  {i > 0 && <PipeConnector direction={isMobile ? "vertical" : "horizontal"} />}
                  <PipelineStage
                    stage={stage}
                    index={i}
                    onRemove={removeStage}
                    onDragStart={handleDragStart}
                    onDragOver={handleDragOver}
                    onDrop={handleDrop}
                  />
                </div>
              ))}
            </div>
          )}
        </div>

        {/* 하단 바 */}
        <div className="flex items-center justify-between mt-4 flex-wrap gap-3">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs dark:text-zinc-500 text-zinc-400">
              {stages.length}/{MAX_STAGES} 노드
            </span>
            {stages.length > 0 && (
              <button
                onClick={handleClear}
                className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs
                  dark:text-zinc-400 text-zinc-500 dark:hover:bg-white/5 hover:bg-black/5 transition-colors"
              >
                <Trash2 className="w-3 h-3" />
                초기화
              </button>
            )}
          </div>
          <div className="flex items-center gap-2 flex-wrap">
            {/* 저장 */}
            {showSaveInput ? (
              <div className="flex items-center gap-1">
                <input
                  type="text"
                  value={saveName}
                  onChange={(e) => setSaveName(e.target.value)}
                  placeholder="워크플로 이름"
                  maxLength={50}
                  className="w-36 px-3 py-1.5 rounded-lg text-xs bg-transparent
                    dark:bg-white/5 bg-black/5 dark:text-white text-zinc-900
                    dark:placeholder-zinc-500 placeholder-zinc-400
                    outline-none focus:ring-1 dark:focus:ring-neon-blue/50 focus:ring-neon-blue/30"
                  onKeyDown={(e) => e.key === "Enter" && handleSave()}
                />
                <button
                  onClick={handleSave}
                  disabled={!saveName.trim() || stages.length === 0}
                  className="px-3 py-1.5 rounded-lg text-xs font-medium
                    bg-gradient-to-r from-neon-blue to-neon-purple text-white
                    hover:opacity-90 disabled:opacity-40 transition-all"
                >
                  저장
                </button>
                <button
                  onClick={() => setShowSaveInput(false)}
                  className="px-2 py-1.5 text-xs dark:text-zinc-400 text-zinc-500"
                >
                  취소
                </button>
              </div>
            ) : (
              <button
                onClick={() => setShowSaveInput(true)}
                disabled={stages.length === 0}
                className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                  dark:bg-white/5 bg-black/5 dark:text-zinc-300 text-zinc-600
                  dark:hover:bg-white/10 hover:bg-black/10 disabled:opacity-40 transition-all"
              >
                <Save className="w-3 h-3" />
                저장
              </button>
            )}

            {/* 불러오기 */}
            <div className="relative">
              <button
                onClick={() => setShowSaved(!showSaved)}
                className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                  dark:bg-white/5 bg-black/5 dark:text-zinc-300 text-zinc-600
                  dark:hover:bg-white/10 hover:bg-black/10 transition-all"
              >
                <FolderOpen className="w-3 h-3" />
                불러오기 {savedList.length > 0 && `(${savedList.length})`}
              </button>
              {showSaved && savedList.length > 0 && (
                <div className="absolute right-0 top-full mt-2 w-64 rounded-xl p-2 z-50
                  dark:bg-zinc-800 bg-white shadow-lg border dark:border-white/10 border-black/10">
                  {savedList.map((wf) => (
                    <div key={wf.name} className="flex items-center justify-between px-3 py-2 rounded-lg
                      dark:hover:bg-white/5 hover:bg-black/5 transition-colors">
                      <button
                        onClick={() => handleLoad(wf)}
                        className="flex-1 text-left min-w-0"
                      >
                        <p className="text-xs font-medium dark:text-white text-zinc-900 truncate">
                          {wf.name}
                        </p>
                        <p className="text-[10px] dark:text-zinc-500 text-zinc-400">
                          {wf.stages.length}개 노드
                        </p>
                      </button>
                      <button
                        onClick={() => handleDelete(wf.name)}
                        className="p-1 ml-2 dark:text-zinc-500 text-zinc-400
                          dark:hover:text-red-400 hover:text-red-500 transition-colors"
                      >
                        <Trash2 className="w-3 h-3" />
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* 공유 */}
            <button
              onClick={handleShare}
              disabled={stages.length === 0}
              className="flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-medium
                dark:bg-white/5 bg-black/5 dark:text-zinc-300 text-zinc-600
                dark:hover:bg-white/10 hover:bg-black/10 disabled:opacity-40 transition-all"
            >
              <Share2 className="w-3 h-3" />
              공유
            </button>
          </div>
        </div>

        {/* 공유 URL */}
        {shareUrl && (
          <div className="mt-3 flex items-center gap-2 px-3 py-2 rounded-lg
            dark:bg-emerald-500/10 bg-emerald-50 border dark:border-emerald-500/20 border-emerald-200">
            <p className="text-xs dark:text-emerald-400 text-emerald-600 truncate flex-1">
              클립보드에 복사됨: {shareUrl}
            </p>
            <button
              onClick={() => setShareUrl("")}
              className="text-xs dark:text-zinc-400 text-zinc-500 shrink-0"
            >
              닫기
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
