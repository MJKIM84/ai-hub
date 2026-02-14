import { prisma } from "@/lib/prisma";
import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { WorkflowBuilder } from "@/components/workflow/WorkflowBuilder";
import type { Metadata } from "next";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "AI 워크플로 빌더",
  description:
    "AI 서비스를 드래그&드롭으로 연결하여 나만의 AI 파이프라인을 설계하세요.",
  openGraph: {
    title: "AI 워크플로 빌더 | pipeAI",
    description:
      "AI 서비스를 드래그&드롭으로 연결하여 나만의 AI 파이프라인을 설계하세요.",
  },
};

export default async function WorkflowPage() {
  const services = await prisma.service.findMany({
    select: {
      id: true,
      name: true,
      category: true,
      logoUrl: true,
      faviconUrl: true,
      ogImageUrl: true,
    },
    orderBy: { name: "asc" },
  });

  return (
    <>
      <Header />
      <main className="min-h-screen pt-20">
        <WorkflowBuilder services={services} />
      </main>
      <Footer />
    </>
  );
}
