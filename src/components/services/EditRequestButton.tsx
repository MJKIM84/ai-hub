"use client";

import { useState } from "react";
import { PenLine } from "lucide-react";
import { EditRequestModal } from "@/components/registration/EditRequestModal";

interface EditRequestButtonProps {
  serviceId: string;
  serviceName: string;
  currentData: {
    name: string;
    description: string | null;
    category: string;
    pricingModel: string;
  };
}

export function EditRequestButton({
  serviceId,
  serviceName,
  currentData,
}: EditRequestButtonProps) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button
        onClick={(e) => { e.stopPropagation(); setShowModal(true); }}
        className="flex items-center gap-1.5 px-2.5 py-2 sm:px-4 sm:py-2 rounded-xl text-xs font-medium whitespace-nowrap
          dark:bg-white/5 bg-black/5
          dark:text-zinc-400 text-zinc-500
          dark:hover:bg-white/10 hover:bg-black/10
          transition-all duration-200"
      >
        <PenLine className="w-3.5 h-3.5" />
        <span className="hidden sm:inline">정보 수정 요청</span>
        <span className="sm:hidden">수정</span>
      </button>

      {showModal && (
        <EditRequestModal
          serviceId={serviceId}
          serviceName={serviceName}
          currentData={currentData}
          onClose={() => setShowModal(false)}
        />
      )}
    </>
  );
}
