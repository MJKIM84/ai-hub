import { prisma } from "@/lib/prisma";
import { notFound } from "next/navigation";
import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { CATEGORIES, PRICING_MODELS } from "@/constants/categories";
import { formatDate, formatNumber, maskIp } from "@/lib/utils";
import {
  ArrowLeft, ExternalLink, Eye, Calendar, Flag, Tag, Bot, UserCheck, MessageSquare
} from "lucide-react";
import Link from "next/link";
import type { Metadata } from "next";
import { EditRequestButton } from "@/components/services/EditRequestButton";
import { ServiceVotePanel } from "@/components/services/ServiceVotePanel";
import { CommentSection } from "@/components/services/CommentSection";

export const dynamic = "force-dynamic";

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://findmy.ai.kr";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  try {
    const services = await prisma.service.findMany({ select: { slug: true } });
    return services.map((s) => ({ slug: s.slug }));
  } catch {
    return [];
  }
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const service = await prisma.service.findUnique({ where: { slug } });

  if (!service) {
    return { title: "서비스를 찾을 수 없습니다" };
  }

  const category = CATEGORIES.find((c) => c.id === service.category);
  const title = `${service.name} - ${category?.nameKo || "AI 서비스"} | FindMyAI`;
  const description =
    service.description ||
    service.tagline ||
    `${service.name}은(는) ${category?.nameKo || "AI"} 카테고리의 서비스입니다. FindMyAI에서 자세한 정보를 확인하세요.`;
  const ogImage = service.ogImageUrl || service.logoUrl || service.faviconUrl;

  return {
    title: `${service.name} - ${category?.nameKo || "AI 서비스"}`,
    description,
    keywords: [
      service.name,
      category?.nameKo || "",
      category?.name || "",
      "AI 서비스",
      "AI 도구",
      ...((() => { try { return JSON.parse(service.tags) as string[]; } catch { return []; } })()),
    ].filter(Boolean),
    alternates: {
      canonical: `/service/${slug}`,
    },
    openGraph: {
      title,
      description,
      url: `${SITE_URL}/service/${slug}`,
      type: "article",
      locale: "ko_KR",
      siteName: "FindMyAI",
      ...(ogImage && {
        images: [{ url: ogImage, width: 1200, height: 630, alt: service.name }],
      }),
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
      ...(ogImage && { images: [ogImage] }),
    },
  };
}

export default async function ServiceDetailPage({ params }: PageProps) {
  const { slug } = await params;
  const service = await prisma.service.findUnique({ where: { slug } });

  if (!service) notFound();

  const category = CATEGORIES.find((c) => c.id === service.category);
  const pricing = PRICING_MODELS.find((p) => p.id === service.pricingModel);
  const tags: string[] = (() => {
    try { return JSON.parse(service.tags); } catch { return []; }
  })();

  const logoSrc = service.logoUrl || service.ogImageUrl || service.faviconUrl;

  // 초기 댓글 데이터 서버사이드 fetch (플랫 — 시간순)
  const [rawComments, commentTotal] = await Promise.all([
    prisma.comment.findMany({
      where: { serviceId: service.id },
      orderBy: { createdAt: "asc" },
      take: 20,
      select: {
        id: true,
        content: true,
        authorName: true,
        authorIp: true,
        likes: true,
        dislikes: true,
        parentId: true,
        parent: { select: { authorName: true } },
        isDeleted: true,
        reports: true,
        isHidden: true,
        createdAt: true,
        _count: { select: { replies: true } },
      },
    }),
    prisma.comment.count({ where: { serviceId: service.id } }),
  ]);

  const initialComments = rawComments.map((c) => ({
    id: c.id,
    content: c.content,
    authorName: c.authorName,
    maskedIp: maskIp(c.authorIp),
    likes: c.likes,
    dislikes: c.dislikes,
    parentId: c.parentId,
    replyToAuthorName: c.parent?.authorName || undefined,
    replyCount: c._count.replies,
    isDeleted: c.isDeleted,
    reports: c.reports,
    isHidden: c.isHidden,
    createdAt: c.createdAt,
  }));

  // JSON-LD
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    name: service.name,
    description: service.description || service.tagline || "",
    url: service.url,
    applicationCategory: "AI",
    operatingSystem: "Web",
    ...(logoSrc && { image: logoSrc }),
    ...(pricing && {
      offers: {
        "@type": "Offer",
        price: pricing.id === "free" ? "0" : undefined,
        priceCurrency: "KRW",
        availability: "https://schema.org/InStock",
      },
    }),
    aggregateRating: {
      "@type": "AggregateRating",
      ratingValue: Math.min(5, Math.max(1, (service.upvotes / Math.max(service.clicks, 1)) * 5 + 2.5)).toFixed(1),
      ratingCount: service.upvotes + service.clicks,
      bestRating: "5",
      worstRating: "1",
    },
  };

  return (
    <>
      <Header />
      <main className="min-h-screen pt-24 pb-12 px-4">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />

        <div className="max-w-3xl mx-auto">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-sm dark:text-zinc-400 text-zinc-500 hover:text-neon-blue transition-colors mb-8"
          >
            <ArrowLeft className="w-4 h-4" />
            목록으로 돌아가기
          </Link>

          {/* 서비스 정보 카드 */}
          <div className="glass p-8">
            <div className="flex items-start gap-5 mb-6">
              <div className="w-20 h-20 rounded-2xl overflow-hidden shrink-0
                dark:bg-white/10 bg-black/5 flex items-center justify-center">
                {logoSrc ? (
                  <img src={logoSrc} alt={service.name} className="w-full h-full object-cover"
                    onError={undefined} />
                ) : (
                  <span className="text-3xl font-bold dark:text-zinc-400 text-zinc-500">
                    {service.name[0]}
                  </span>
                )}
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex items-start justify-between gap-3 mb-2">
                  <div className="flex items-center gap-3 flex-wrap min-w-0">
                    <h1 className="text-2xl font-bold dark:text-white text-zinc-900">
                      {service.name}
                    </h1>
                    {service.isKorean && (
                      <span className="flex items-center gap-1 px-2 py-1 rounded-lg text-xs font-medium
                        dark:bg-neon-blue/15 bg-neon-blue/10 dark:text-neon-blue text-blue-600">
                        <Flag className="w-3 h-3" />
                        한국
                      </span>
                    )}
                    {service.source === "auto" && (
                      <span className="flex items-center gap-1 px-2 py-1 rounded-lg text-xs font-medium
                        dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600">
                        <Bot className="w-3 h-3" />
                        Auto
                      </span>
                    )}
                    {service.source === "developer" && (
                      <span className="flex items-center gap-1 px-2 py-1 rounded-lg text-xs font-medium
                        dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600">
                        <UserCheck className="w-3 h-3" />
                        인증됨
                      </span>
                    )}
                  </div>
                  {/* 서비스 방문 + 정보 수정 버튼 (우측 상단) */}
                  <div className="flex items-center gap-2 shrink-0">
                    <EditRequestButton
                      serviceId={service.id}
                      serviceName={service.name}
                      currentData={{
                        name: service.name,
                        description: service.description,
                        category: service.category,
                        pricingModel: service.pricingModel,
                      }}
                    />
                    <a
                      href={service.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-medium
                        bg-gradient-to-r from-neon-blue to-neon-purple text-white
                        hover:opacity-90 transition-all duration-200 whitespace-nowrap
                        shadow-lg shadow-neon-blue/20"
                    >
                      <ExternalLink className="w-3.5 h-3.5" />
                      서비스 방문하기
                    </a>
                  </div>
                </div>
                {service.tagline && (
                  <p className="text-base dark:text-zinc-400 text-zinc-500 mb-3">
                    {service.tagline}
                  </p>
                )}
                <div className="flex items-center gap-3 flex-wrap">
                  {category && (
                    <span className="px-3 py-1.5 rounded-lg text-xs font-medium
                      dark:bg-neon-purple/15 bg-neon-purple/10
                      dark:text-neon-purple text-purple-600">
                      {category.nameKo}
                    </span>
                  )}
                  {pricing && (
                    <span className={`px-3 py-1.5 rounded-lg text-xs font-medium
                      ${pricing.id === 'free'
                        ? 'dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600'
                        : pricing.id === 'freemium'
                        ? 'dark:bg-blue-500/15 bg-blue-500/10 dark:text-blue-400 text-blue-600'
                        : 'dark:bg-amber-500/15 bg-amber-500/10 dark:text-amber-400 text-amber-600'
                      }`}>
                      {pricing.nameKo}
                    </span>
                  )}
                </div>
              </div>
            </div>

            {/* 상세 설명 (잘림 없이 전체 표시) */}
            {service.description && (
              <div className="mb-6 pb-6 border-b dark:border-white/10 border-black/10">
                <p className="dark:text-zinc-300 text-zinc-600 leading-relaxed whitespace-pre-wrap">
                  {service.description}
                </p>
              </div>
            )}

            {/* 통계 */}
            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className="text-center p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <Eye className="w-5 h-5 mx-auto mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-lg font-semibold dark:text-white text-zinc-900">
                  {formatNumber(service.clicks)}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">조회</p>
              </div>
              <div className="text-center p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <MessageSquare className="w-5 h-5 mx-auto mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-lg font-semibold dark:text-white text-zinc-900">
                  {commentTotal}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">댓글</p>
              </div>
              <div className="text-center p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <Calendar className="w-5 h-5 mx-auto mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-sm font-semibold dark:text-white text-zinc-900">
                  {formatDate(service.createdAt)}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">등록일</p>
              </div>
            </div>

            {tags.length > 0 && (
              <div className="flex items-center gap-2 flex-wrap mb-6">
                <Tag className="w-4 h-4 dark:text-zinc-500 text-zinc-400" />
                {tags.map((tag) => {
                  const tagCat = CATEGORIES.find((c) => c.id === tag);
                  return (
                    <span key={tag} className="px-2.5 py-1 rounded-lg text-xs
                      dark:bg-white/5 bg-black/5 dark:text-zinc-400 text-zinc-500">
                      {tagCat ? tagCat.nameKo : tag}
                    </span>
                  );
                })}
              </div>
            )}

            {/* 추천 / 비추천 */}
            <ServiceVotePanel
              serviceId={service.id}
              initialUpvotes={service.upvotes}
              initialDownvotes={service.downvotes}
            />
          </div>

          {/* 커뮤니티 댓글 섹션 */}
          <CommentSection
            serviceId={service.id}
            initialComments={JSON.parse(JSON.stringify(initialComments))}
            initialTotal={commentTotal}
          />
        </div>
      </main>
      <Footer />
    </>
  );
}
