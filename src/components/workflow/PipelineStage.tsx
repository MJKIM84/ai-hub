"use client";

import { X } from "lucide-react";
import { CATEGORIES } from "@/constants/categories";
import type { WorkflowStage } from "@/lib/workflows";

interface PipelineStageProps {
  stage: WorkflowStage;
  index: number;
  onRemove: (index: number) => void;
  onDragStart: (e: React.DragEvent, index: number) => void;
  onDragOver: (e: React.DragEvent) => void;
  onDrop: (e: React.DragEvent, index: number) => void;
}

export function PipelineStage({
  stage,
  index,
  onRemove,
  onDragStart,
  onDragOver,
  onDrop,
}: PipelineStageProps) {
  const category = CATEGORIES.find((c) => c.id === stage.serviceCategory);

  return (
    <div
      draggable
      onDragStart={(e) => onDragStart(e, index)}
      onDragOver={onDragOver}
      onDrop={(e) => onDrop(e, index)}
      className="pipe-node p-4 cursor-grab active:cursor-grabbing
        flex items-center gap-3 group relative min-w-[160px]"
    >
      {/* 좌측 연결 포트 */}
      {index > 0 && (
        <div className="absolute -left-[5px] top-1/2 -translate-y-1/2 w-2.5 h-2.5
          rounded-full dark:bg-pipe-cyan bg-neon-blue border-2 dark:border-surface-dark border-surface-light z-10" />
      )}

      {/* 로고 */}
      <div className="w-10 h-10 rounded-lg overflow-hidden shrink-0
        dark:bg-white/10 bg-black/5 flex items-center justify-center">
        {stage.serviceLogo ? (
          <img src={stage.serviceLogo} alt={stage.serviceName} className="w-full h-full object-cover" />
        ) : (
          <span className="text-sm font-bold dark:text-zinc-400 text-zinc-500">
            {stage.serviceName[0]}
          </span>
        )}
      </div>

      {/* 정보 */}
      <div className="flex-1 min-w-0">
        <p className="text-sm font-medium dark:text-white text-zinc-900 truncate">
          {stage.serviceName}
        </p>
        {category && (
          <p className="text-xs dark:text-zinc-500 text-zinc-400 truncate">
            {category.nameKo}
          </p>
        )}
      </div>

      {/* 삭제 버튼 */}
      <button
        onClick={(e) => { e.stopPropagation(); onRemove(index); }}
        className="opacity-0 group-hover:opacity-100 transition-opacity
          p-1 rounded-md dark:hover:bg-white/10 hover:bg-black/10"
      >
        <X className="w-3.5 h-3.5 dark:text-zinc-400 text-zinc-500" />
      </button>

      {/* 우측 연결 포트 */}
      <div className="absolute -right-[5px] top-1/2 -translate-y-1/2 w-2.5 h-2.5
        rounded-full dark:bg-pipe-cyan bg-neon-blue border-2 dark:border-surface-dark border-surface-light z-10" />
    </div>
  );
}
