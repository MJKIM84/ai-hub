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
        onClick={() => setShowModal(true)}
        className="w-full flex items-center justify-center gap-2 py-3 rounded-xl text-sm font-medium
          dark:bg-white/5 bg-black/5
          dark:text-zinc-400 text-zinc-500
          dark:hover:bg-white/10 hover:bg-black/10
          transition-all duration-200 mt-3"
      >
        <PenLine className="w-4 h-4" />
        정보 수정 요청
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
