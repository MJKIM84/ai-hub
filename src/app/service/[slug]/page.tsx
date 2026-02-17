import { prisma } from "@/lib/prisma";
import { notFound } from "next/navigation";
import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { CATEGORIES, PRICING_MODELS } from "@/constants/categories";
import { formatDate, formatNumber, maskIp } from "@/lib/utils";
import {
  ExternalLink, Eye, Calendar, Flag, Tag, Bot, UserCheck, MessageSquare
} from "lucide-react";
import type { Metadata } from "next";
import { EditRequestButton } from "@/components/services/EditRequestButton";
import { ServiceVotePanel } from "@/components/services/ServiceVotePanel";
import { RelatedArticles } from "@/components/services/RelatedArticles";
import { CommentSection } from "@/components/services/CommentSection";
import { BackButton } from "@/components/services/BackButton";
import { ServiceDescription } from "@/components/services/ServiceDescription";
import { ServiceDetailLogo } from "@/components/services/ServiceDetailLogo";

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
  const pricing = PRICING_MODELS.find((p) => p.id === service.pricingModel);

  // 한국어 이름 우선 사용
  const displayName = service.nameKo || service.name;
  const categoryName = category?.nameKo || "AI 서비스";
  const pricingName = pricing?.nameKo || "";

  // 한국어 description 우선, 없으면 영어 + 한국어 보조 설명 생성
  const koDesc = service.descriptionKo;
  const enDesc = service.description || service.tagline;
  const richDescription = koDesc
    ? `${koDesc} ${displayName}은(는) ${categoryName} 카테고리의 ${pricingName ? pricingName + " " : ""}AI 서비스입니다.`
    : enDesc
    ? `${displayName} - ${enDesc}. ${categoryName} 분야 AI 도구로 FindMyAI에서 리뷰, 가격, 대안 정보를 확인하세요.`
    : `${displayName}은(는) ${categoryName} 카테고리의 ${pricingName ? pricingName + " " : ""}AI 서비스입니다. 사용자 리뷰, 가격 정보, 대안 비교를 FindMyAI에서 확인하세요.`;

  // SEO에 최적화된 title
  const title = `${displayName} - ${categoryName} | 가격, 리뷰, 대안 비교`;
  const ogTitle = `${displayName} - ${categoryName} AI 도구 | FindMyAI`;
  const ogImage = service.ogImageUrl || service.logoUrl || service.faviconUrl;

  // 풍부한 키워드: 서비스명 변형 + 카테고리 + 태그 + 한국어 검색어
  const parsedTags: string[] = (() => { try { return JSON.parse(service.tags) as string[]; } catch { return []; } })();
  const tagCategories = parsedTags
    .map((t) => CATEGORIES.find((c) => c.id === t)?.nameKo)
    .filter(Boolean) as string[];

  const keywords = [
    service.name,
    displayName,
    `${service.name} 사용법`,
    `${service.name} 가격`,
    `${service.name} 후기`,
    `${service.name} 대안`,
    `${service.name} 한국어`,
    `${displayName} 리뷰`,
    categoryName,
    category?.name || "",
    ...tagCategories,
    ...parsedTags,
    pricingName,
    "AI 서비스",
    "AI 도구",
    "인공지능",
    ...(service.isKorean ? ["한국 AI", "국산 AI", "한국어 AI"] : []),
  ].filter(Boolean);

  return {
    title: `${displayName} - ${categoryName}`,
    description: richDescription,
    keywords,
    alternates: {
      canonical: `/service/${slug}`,
    },
    openGraph: {
      title: ogTitle,
      description: richDescription,
      url: `${SITE_URL}/service/${slug}`,
      type: "article",
      locale: "ko_KR",
      siteName: "FindMyAI",
      ...(ogImage && {
        images: [{ url: ogImage, width: 1200, height: 630, alt: displayName }],
      }),
    },
    twitter: {
      card: "summary_large_image",
      title: ogTitle,
      description: richDescription,
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

  // 한국어 이름/설명 우선
  const displayName = service.nameKo || service.name;
  const displayDesc = service.descriptionKo || service.description || service.tagline || "";
  const parsedTags: string[] = (() => { try { return JSON.parse(service.tags) as string[]; } catch { return []; } })();

  // JSON-LD — SoftwareApplication + BreadcrumbList + FAQPage + WebPage
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "SoftwareApplication",
        name: service.name,
        ...(service.nameKo && { alternateName: service.nameKo }),
        description: displayDesc,
        url: service.url,
        applicationCategory: category?.name || "AI",
        applicationSubCategory: category?.nameKo || "AI 도구",
        operatingSystem: "Web",
        inLanguage: service.isKorean ? "ko" : "en",
        ...(logoSrc && { image: logoSrc }),
        ...(pricing && {
          offers: {
            "@type": "Offer",
            price: pricing.id === "free" ? "0" : undefined,
            priceCurrency: "KRW",
            availability: "https://schema.org/InStock",
            category: pricing.nameKo,
          },
        }),
        aggregateRating: {
          "@type": "AggregateRating",
          ratingValue: Math.min(5, Math.max(1, (service.upvotes / Math.max(service.clicks, 1)) * 5 + 2.5)).toFixed(1),
          ratingCount: Math.max(1, service.upvotes + service.clicks),
          bestRating: "5",
          worstRating: "1",
        },
        ...(parsedTags.length > 0 && {
          keywords: parsedTags.map((t) => {
            const tagCat = CATEGORIES.find((c) => c.id === t);
            return tagCat ? tagCat.nameKo : t;
          }).join(", "),
        }),
      },
      {
        "@type": "WebPage",
        "@id": `${SITE_URL}/service/${slug}`,
        url: `${SITE_URL}/service/${slug}`,
        name: `${displayName} - ${category?.nameKo || "AI 서비스"} | FindMyAI`,
        description: displayDesc,
        inLanguage: "ko-KR",
        isPartOf: { "@id": `${SITE_URL}/#website` },
        about: {
          "@type": "SoftwareApplication",
          name: service.name,
        },
        datePublished: service.createdAt.toISOString(),
        dateModified: service.updatedAt.toISOString(),
      },
      {
        "@type": "BreadcrumbList",
        itemListElement: [
          {
            "@type": "ListItem",
            position: 1,
            name: "홈",
            item: SITE_URL,
          },
          ...(category ? [{
            "@type": "ListItem",
            position: 2,
            name: category.nameKo,
            item: `${SITE_URL}/?category=${service.category}`,
          }] : []),
          {
            "@type": "ListItem",
            position: category ? 3 : 2,
            name: displayName,
            item: `${SITE_URL}/service/${slug}`,
          },
        ],
      },
      // FAQ 구조화 데이터 — 서비스별 자동 생성 (구글 리치 스니펫)
      {
        "@type": "FAQPage",
        mainEntity: [
          {
            "@type": "Question",
            name: `${displayName}은(는) 무료인가요?`,
            acceptedAnswer: {
              "@type": "Answer",
              text: pricing?.id === "free"
                ? `네, ${displayName}은(는) 무료로 사용할 수 있는 AI 서비스입니다.`
                : pricing?.id === "freemium"
                ? `${displayName}은(는) 기본 기능을 무료로 제공하며, 추가 기능은 유료입니다 (프리미엄 모델).`
                : `${displayName}은(는) 유료 AI 서비스입니다. 자세한 가격은 공식 사이트에서 확인해주세요.`,
            },
          },
          {
            "@type": "Question",
            name: `${displayName}은(는) 어떤 AI 서비스인가요?`,
            acceptedAnswer: {
              "@type": "Answer",
              text: displayDesc || `${displayName}은(는) ${category?.nameKo || "AI"} 카테고리의 서비스입니다. FindMyAI에서 자세한 정보를 확인하세요.`,
            },
          },
          {
            "@type": "Question",
            name: `${displayName}의 대안은 무엇인가요?`,
            acceptedAnswer: {
              "@type": "Answer",
              text: `FindMyAI에서 ${category?.nameKo || "AI"} 카테고리의 다른 서비스들을 비교해보세요. 다양한 대안과 리뷰를 확인할 수 있습니다.`,
            },
          },
        ],
      },
    ],
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
          <BackButton />

          {/* 서비스 정보 카드 */}
          <div className="glass p-4 sm:p-8">
            {/* 모바일: 세로 배치 / 데스크톱: 가로 배치 */}
            <div className="flex flex-col sm:flex-row sm:items-start gap-3 sm:gap-5 mb-4 sm:mb-6">
              <div className="flex items-center gap-3 sm:block">
                <ServiceDetailLogo
                  logoUrl={service.logoUrl}
                  faviconUrl={service.faviconUrl}
                  ogImageUrl={service.ogImageUrl}
                  serviceUrl={service.url}
                  name={service.name}
                />
                {/* 모바일에서 로고 옆에 이름 표시 */}
                <div className="sm:hidden flex-1 min-w-0">
                  <h1 className="text-xl font-bold dark:text-white text-zinc-900">
                    {service.name}
                  </h1>
                  <div className="flex items-center gap-1.5 mt-1 flex-wrap">
                    {service.isKorean && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-lg text-xs font-medium
                        dark:bg-neon-blue/15 bg-neon-blue/10 dark:text-neon-blue text-blue-600">
                        <Flag className="w-3 h-3" />
                        한국
                      </span>
                    )}
                    {service.source === "auto" && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-lg text-xs font-medium
                        dark:bg-orange-500/15 bg-orange-500/10 dark:text-orange-400 text-orange-600">
                        <Bot className="w-3 h-3" />
                        Auto
                      </span>
                    )}
                    {service.source === "developer" && (
                      <span className="flex items-center gap-1 px-2 py-0.5 rounded-lg text-xs font-medium
                        dark:bg-emerald-500/15 bg-emerald-500/10 dark:text-emerald-400 text-emerald-600">
                        <UserCheck className="w-3 h-3" />
                        인증됨
                      </span>
                    )}
                  </div>
                </div>
              </div>
              <div className="flex-1 min-w-0">
                <div className="mb-2">
                  {/* 데스크톱에서만 이름 표시 (모바일은 위에서 로고 옆에 표시) */}
                  <div className="hidden sm:flex items-center gap-3 flex-wrap min-w-0 mb-2">
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
                  {/* 서비스 방문 + 정보 수정 버튼 */}
                  <div className="flex items-center gap-2">
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
                      className="flex items-center gap-1.5 px-3 py-2 sm:px-4 sm:py-2 rounded-xl text-xs font-medium
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

            {/* 상세 설명 (한국어/영어 토글) */}
            {(service.description || service.descriptionKo) && (
              <div className="mb-6 pb-6 border-b dark:border-white/10 border-black/10">
                <ServiceDescription
                  name={service.name}
                  nameKo={service.nameKo}
                  description={service.description}
                  descriptionKo={service.descriptionKo}
                  tagline={service.tagline}
                />
              </div>
            )}

            {/* 통계 */}
            <div className="grid grid-cols-3 gap-2 sm:gap-4 mb-6">
              <div className="text-center p-2.5 sm:p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <Eye className="w-4 h-4 sm:w-5 sm:h-5 mx-auto mb-1.5 sm:mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-base sm:text-lg font-semibold dark:text-white text-zinc-900">
                  {formatNumber(service.clicks)}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">조회</p>
              </div>
              <div className="text-center p-2.5 sm:p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <MessageSquare className="w-4 h-4 sm:w-5 sm:h-5 mx-auto mb-1.5 sm:mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-base sm:text-lg font-semibold dark:text-white text-zinc-900">
                  {commentTotal}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">댓글</p>
              </div>
              <div className="text-center p-2.5 sm:p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <Calendar className="w-4 h-4 sm:w-5 sm:h-5 mx-auto mb-1.5 sm:mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-xs sm:text-sm font-semibold dark:text-white text-zinc-900">
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

          {/* 관련 기사 섹션 */}
          <RelatedArticles serviceId={service.id} />

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
