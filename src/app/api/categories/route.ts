import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { CATEGORIES } from "@/constants/categories";

export async function GET() {
  try {
    const counts = await prisma.service.groupBy({
      by: ["category"],
      _count: { id: true },
    });

    const countMap: Record<string, number> = {};
    for (const c of counts) {
      countMap[c.category] = c._count.id;
    }

    const categories = CATEGORIES.filter((c) => c.id !== "all").map((c) => ({
      ...c,
      count: countMap[c.id] || 0,
    }));

    return NextResponse.json({ categories });
  } catch (error) {
    console.error("GET /api/categories error:", error);
    return NextResponse.json(
      { error: "카테고리 목록을 불러올 수 없습니다" },
      { status: 500 }
    );
  }
}
