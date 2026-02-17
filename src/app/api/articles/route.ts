import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  try {
    const serviceId = request.nextUrl.searchParams.get("serviceId");

    if (!serviceId) {
      return NextResponse.json(
        { error: "serviceId 파라미터가 필요합니다" },
        { status: 400 }
      );
    }

    const articles = await prisma.article.findMany({
      where: { serviceId },
      orderBy: { publishedAt: "desc" },
      take: 10,
    });

    return NextResponse.json({ items: articles });
  } catch (error) {
    console.error("[API:Articles] Error:", error);
    return NextResponse.json(
      { error: "기사 조회 중 오류가 발생했습니다" },
      { status: 500 }
    );
  }
}
