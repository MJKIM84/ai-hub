import { prisma } from "@/lib/prisma";
import { notFound } from "next/navigation";
import { Header } from "@/components/layout/Header";
import { Footer } from "@/components/layout/Footer";
import { CATEGORIES, PRICING_MODELS } from "@/constants/categories";
import { formatDate, formatNumber } from "@/lib/utils";
import {
  ArrowLeft, ExternalLink, ThumbsUp, Eye, Calendar, Flag, Tag
} from "lucide-react";
import Link from "next/link";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  const services = await prisma.service.findMany({ select: { slug: true } });
  return services.map((s) => ({ slug: s.slug }));
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
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-2">
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

            {service.description && (
              <div className="mb-6 pb-6 border-b dark:border-white/10 border-black/10">
                <p className="dark:text-zinc-300 text-zinc-600 leading-relaxed">
                  {service.description}
                </p>
              </div>
            )}

            <div className="grid grid-cols-3 gap-4 mb-6">
              <div className="text-center p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <Eye className="w-5 h-5 mx-auto mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-lg font-semibold dark:text-white text-zinc-900">
                  {formatNumber(service.clicks)}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">조회</p>
              </div>
              <div className="text-center p-4 rounded-xl dark:bg-white/5 bg-black/5">
                <ThumbsUp className="w-5 h-5 mx-auto mb-2 dark:text-zinc-400 text-zinc-500" />
                <p className="text-lg font-semibold dark:text-white text-zinc-900">
                  {formatNumber(service.upvotes)}
                </p>
                <p className="text-xs dark:text-zinc-500 text-zinc-400">추천</p>
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

            <a
              href={service.url}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full flex items-center justify-center gap-2 py-3.5 rounded-xl text-sm font-medium
                bg-gradient-to-r from-neon-blue to-neon-purple text-white
                hover:opacity-90 transition-all duration-200
                shadow-lg shadow-neon-blue/20"
            >
              <ExternalLink className="w-4 h-4" />
              서비스 방문하기
            </a>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}
