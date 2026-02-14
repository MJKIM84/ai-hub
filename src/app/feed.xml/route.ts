import { prisma } from "@/lib/prisma";
import { CATEGORIES } from "@/constants/categories";

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://findmy.ai.kr";
const SITE_NAME = "FindMyAI";

export const dynamic = "force-dynamic";

function escapeXml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

export async function GET() {
  let services: {
    name: string;
    slug: string;
    description: string | null;
    tagline: string | null;
    category: string;
    url: string;
    logoUrl: string | null;
    createdAt: Date;
    updatedAt: Date;
  }[] = [];

  try {
    services = await prisma.service.findMany({
      select: {
        name: true,
        slug: true,
        description: true,
        tagline: true,
        category: true,
        url: true,
        logoUrl: true,
        createdAt: true,
        updatedAt: true,
      },
      orderBy: { createdAt: "desc" },
      take: 100,
    });
  } catch {
    // DB 연결 실패 시 빈 피드
  }

  const lastBuildDate = services.length > 0
    ? services[0].createdAt.toUTCString()
    : new Date().toUTCString();

  const items = services.map((s) => {
    const category = CATEGORIES.find((c) => c.id === s.category);
    const desc = s.description || s.tagline || `${s.name} - AI 서비스`;
    return `    <item>
      <title>${escapeXml(s.name)}</title>
      <link>${SITE_URL}/service/${s.slug}</link>
      <guid isPermaLink="true">${SITE_URL}/service/${s.slug}</guid>
      <description>${escapeXml(desc)}</description>
      <category>${escapeXml(category?.nameKo || "AI 서비스")}</category>
      <pubDate>${s.createdAt.toUTCString()}</pubDate>
    </item>`;
  });

  const rss = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>${SITE_NAME} - AI 도구 디렉토리</title>
    <link>${SITE_URL}</link>
    <description>나에게 맞는 AI를 찾아보세요. ChatGPT, Claude, Midjourney 등 수백 개의 AI 도구를 카테고리별로 탐색하세요.</description>
    <language>ko</language>
    <lastBuildDate>${lastBuildDate}</lastBuildDate>
    <atom:link href="${SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
${items.join("\n")}
  </channel>
</rss>`;

  return new Response(rss, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8",
      "Cache-Control": "public, max-age=3600, s-maxage=3600",
    },
  });
}
