import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { ArrowLeft, Shield } from "lucide-react";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "운영정책",
  description: "FindMyAI 서비스 이용 제한 사유 및 댓글 운영정책 안내",
};

export default function PolicyPage() {
  return (
    <>
      <Header />
      <main className="min-h-screen pt-24 pb-12 px-4">
        <div className="max-w-3xl mx-auto">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm dark:text-zinc-400 text-zinc-500 hover:text-neon-blue transition-colors mb-8"
          >
            <ArrowLeft className="w-4 h-4" />
            목록으로 돌아가기
          </Link>

          <div className="glass p-8">
            <div className="flex items-center gap-3 mb-8">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-neon-blue to-neon-purple flex items-center justify-center">
                <Shield className="w-5 h-5 text-white" />
              </div>
              <h1 className="text-2xl font-bold dark:text-white text-zinc-900">
                운영정책
              </h1>
            </div>

            {/* 1. 서비스 이용 제한 사유 */}
            <section className="mb-10">
              <h2 className="text-lg font-semibold dark:text-white text-zinc-900 mb-4 pb-2 border-b dark:border-white/10 border-black/10">
                1. 서비스 이용 제한 사유
              </h2>
              <ul className="space-y-2.5 dark:text-zinc-300 text-zinc-600 text-sm leading-relaxed">
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">1.</span>
                  <span>회사 또는 제3자의 명예를 훼손하는 경우</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">2.</span>
                  <span>회사 또는 제3자의 저작권 등 기타 권리를 침해하는 경우</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">3.</span>
                  <span>외설 또는 폭력적인 메시지, 기타 관계법령 및 공서양속에 반하는 경우</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">4.</span>
                  <span>제3자에게 피해가 발생하였거나 피해가 예상되는 경우</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">5.</span>
                  <span>댓글 도배 등 부정한 용도로 서비스를 이용하는 경우</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">6.</span>
                  <span>범죄행위를 목적으로 하거나 범죄행위를 교사한다고 판단되는 경우</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">7.</span>
                  <span>기타 관계 법령을 위배한다고 판단되는 경우</span>
                </li>
              </ul>
            </section>

            {/* 2. 댓글 기능 */}
            <section className="mb-10">
              <h2 className="text-lg font-semibold dark:text-white text-zinc-900 mb-4 pb-2 border-b dark:border-white/10 border-black/10">
                2. 댓글 기능
              </h2>

              {/* 가. 댓글 신고 */}
              <div className="mb-6">
                <h3 className="text-sm font-semibold dark:text-white text-zinc-800 mb-3">
                  가. 댓글 신고
                </h3>
                <ul className="space-y-2 dark:text-zinc-300 text-zinc-600 text-sm leading-relaxed">
                  <li className="flex gap-2">
                    <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                    <span>사용자는 다른 사용자의 댓글을 신고할 수 있습니다. 신고된 댓글은 신고한 사용자에 한해서 숨김 처리되며 이는 복구할 수 없습니다.</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                    <span>신고된 댓글은 이용약관 및 운영정책에 따라 처리됩니다.</span>
                  </li>
                </ul>
              </div>

              {/* 나. 댓글 삭제 */}
              <div>
                <h3 className="text-sm font-semibold dark:text-white text-zinc-800 mb-3">
                  나. 댓글 삭제
                </h3>
                <ul className="space-y-2 dark:text-zinc-300 text-zinc-600 text-sm leading-relaxed">
                  <li className="flex gap-2">
                    <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                    <span>사용자는 본인이 작성한 댓글을 삭제할 수 있습니다.</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                    <span>삭제된 댓글의 답글은 작성자 또는 회사가 별도로 삭제하기 전까지 삭제되지 않습니다.</span>
                  </li>
                </ul>
              </div>
            </section>

            {/* 3. 서비스 이용 제한 */}
            <section>
              <h2 className="text-lg font-semibold dark:text-white text-zinc-900 mb-4 pb-2 border-b dark:border-white/10 border-black/10">
                3. 서비스 이용 제한
              </h2>
              <ul className="space-y-2 dark:text-zinc-300 text-zinc-600 text-sm leading-relaxed">
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                  <span>회사는 비방 및 욕설, 광고 등 댓글에 부적합한 단어의 이용을 금지하고 있습니다.</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                  <span>서비스 이용 제한은 누적 위반 횟수를 우선하여 처리하나 사안의 심각성에 따라 처리 기준이 달라질 수 있습니다.</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                  <span>회사는 사용자의 IP 및 ID를 일시 또는 영구적으로 차단하여 서비스 이용을 제한할 수 있습니다.</span>
                </li>
                <li className="flex gap-2">
                  <span className="dark:text-zinc-500 text-zinc-400 shrink-0">-</span>
                  <span>회사는 사용자의 댓글을 삭제하여 게재된 댓글의 이용을 제한할 수 있습니다.</span>
                </li>
              </ul>
            </section>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}
