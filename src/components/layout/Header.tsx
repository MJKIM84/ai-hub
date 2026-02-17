"use client";

import { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { Plus } from "lucide-react";
import { ThemeToggle } from "./ThemeToggle";
import { RegisterModal } from "../registration/RegisterModal";

export function Header() {
  const [showRegister, setShowRegister] = useState(false);

  return (
    <>
      <header className="fixed top-0 left-0 right-0 z-50 glass">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <Link href="/" className="flex items-center gap-2 group">
              <Image src="/logo.svg" alt="FindMyAI" width={32} height={32} className="rounded-lg" priority />
              <span className="text-lg font-bold bg-gradient-to-r from-neon-blue to-neon-purple bg-clip-text text-transparent">
                FindMyAI
              </span>
            </Link>

            <div className="flex items-center gap-3">
              <button
                onClick={() => setShowRegister(true)}
                className="flex items-center gap-2 px-3 py-2.5 sm:px-4 sm:py-2 rounded-xl text-sm font-medium
                  bg-gradient-to-r from-neon-blue to-neon-purple text-white
                  hover:opacity-90 transition-all duration-200 active:scale-95 sm:hover:scale-105
                  shadow-lg shadow-neon-blue/20 min-h-[44px]"
              >
                <Plus className="w-4 h-4" />
                <span className="hidden sm:inline">서비스 등록</span>
              </button>
              <ThemeToggle />
            </div>
          </div>
        </div>
      </header>
      {showRegister && (
        <RegisterModal onClose={() => setShowRegister(false)} />
      )}
    </>
  );
}
