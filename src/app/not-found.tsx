import Link from "next/link";

export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center dark:bg-[#0a0a0f] bg-gray-50">
      <div className="text-center px-6">
        <div className="text-8xl font-bold bg-gradient-to-r from-neon-blue to-neon-purple bg-clip-text text-transparent mb-4">
          404
        </div>
        <h1 className="text-2xl font-bold dark:text-white text-zinc-900 mb-2">
          페이지를 찾을 수 없습니다
        </h1>
        <p className="dark:text-zinc-400 text-zinc-500 mb-8 max-w-md">
          요청하신 페이지가 존재하지 않거나, 이동되었거나, 삭제되었을 수 있습니다.
        </p>
        <Link
          href="/"
          className="inline-flex items-center gap-2 px-6 py-3 rounded-xl font-medium
            bg-gradient-to-r from-neon-blue to-neon-purple text-white
            hover:opacity-90 transition-opacity"
        >
          홈으로 돌아가기
        </Link>
      </div>
    </div>
  );
}
