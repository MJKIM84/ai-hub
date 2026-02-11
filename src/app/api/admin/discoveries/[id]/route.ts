import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";
import { scrapeServiceMetadata } from "@/lib/scraper";
import { calculateGravityScore } from "@/lib/ranking";
import { createSlug } from "@/lib/utils";

interface RouteParams {
  params: Promise<{ id: string }>;
}

export async function PATCH(request: NextRequest, { params }: RouteParams) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const { id } = await params;
    const body = await request.json();
    const { action } = body; // "approve" | "reject"

    const log = await prisma.discoveryLog.findUnique({ where: { id } });
    if (!log) {
      return NextResponse.json({ error: "Not found" }, { status: 404 });
    }

    if (action === "approve") {
      // 메타데이터 추출 후 서비스 생성
      try {
        const metadata = await scrapeServiceMetadata(log.discoveredUrl);
        let slug = createSlug(metadata.name);
        const existingSlug = await prisma.service.findUnique({ where: { slug } });
        if (existingSlug) {
          slug = `${slug}-${Date.now().toString(36)}`;
        }

        const service = await prisma.service.create({
          data: {
            slug,
            url: log.discoveredUrl,
            name: metadata.name,
            description: metadata.description,
            category: log.title ? metadata.suggestedCategory : "productivity",
            tags: JSON.stringify(metadata.suggestedTags),
            pricingModel: "free",
            faviconUrl: metadata.faviconUrl || undefined,
            ogImageUrl: metadata.ogImageUrl || undefined,
            source: "auto",
            score: calculateGravityScore(0, new Date()),
          },
        });

        await prisma.discoveryLog.update({
          where: { id },
          data: { status: "approved", serviceId: service.id },
        });

        return NextResponse.json({ success: true, service });
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        return NextResponse.json({ error: `승인 실패: ${msg}` }, { status: 500 });
      }
    } else if (action === "reject") {
      await prisma.discoveryLog.update({
        where: { id },
        data: { status: "rejected" },
      });
      return NextResponse.json({ success: true });
    }

    return NextResponse.json({ error: "Invalid action" }, { status: 400 });
  } catch (error) {
    console.error("PATCH /api/admin/discoveries/[id] error:", error);
    return NextResponse.json({ error: "Failed to update discovery" }, { status: 500 });
  }
}
