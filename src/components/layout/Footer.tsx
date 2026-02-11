import { Sparkles } from "lucide-react";

export function Footer() {
  return (
    <footer className="mt-20 py-8 border-t dark:border-white/10 border-black/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 rounded-md bg-gradient-to-br from-neon-blue to-neon-purple flex items-center justify-center">
              <Sparkles className="w-3 h-3 text-white" />
            </div>
            <span className="text-sm font-semibold bg-gradient-to-r from-neon-blue to-neon-purple bg-clip-text text-transparent">
              AI HUB
            </span>
          </div>
          <p className="text-sm dark:text-zinc-500 text-zinc-400">
            AI 서비스의 파편화를 해소하고, 개발자와 사용자를 연결합니다.
          </p>
        </div>
      </div>
    </footer>
  );
}
