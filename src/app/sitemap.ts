import type { MetadataRoute } from "next";
import { prisma } from "@/lib/prisma";

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://findmy.ai.kr";

export const dynamic = "force-dynamic";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  // 모든 서비스 슬러그와 수정일 가져오기
  let services: { slug: string; updatedAt: Date }[] = [];
  try {
    services = await prisma.service.findMany({
      select: { slug: true, updatedAt: true },
      orderBy: { updatedAt: "desc" },
    });
  } catch {
    // DB 연결 실패 시 빈 배열로 폴백
  }

  const serviceUrls: MetadataRoute.Sitemap = services.map((service) => ({
    url: `${SITE_URL}/service/${service.slug}`,
    lastModified: service.updatedAt,
    changeFrequency: "weekly",
    priority: 0.7,
  }));

  // 카테고리 페이지들
  const categories = [
    "indie-dev", "text-generation", "image-generation", "image-editing",
    "code-assistant", "productivity", "voice-speech", "education",
    "video", "data-analysis", "writing", "translation", "healthcare", "korean-llm",
  ];

  const categoryUrls: MetadataRoute.Sitemap = categories.map((cat) => ({
    url: `${SITE_URL}/?category=${cat}`,
    lastModified: new Date(),
    changeFrequency: "daily",
    priority: 0.6,
  }));

  // 정적 페이지들
  const staticPages: MetadataRoute.Sitemap = [
    {
      url: SITE_URL,
      lastModified: new Date(),
      changeFrequency: "daily",
      priority: 1.0,
    },
    {
      url: `${SITE_URL}/policy`,
      lastModified: new Date("2025-01-01"),
      changeFrequency: "yearly",
      priority: 0.3,
    },
    {
      url: `${SITE_URL}/status`,
      lastModified: new Date(),
      changeFrequency: "always",
      priority: 0.2,
    },
  ];

  return [
    ...staticPages,
    ...categoryUrls,
    ...serviceUrls,
  ];
}
