import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { serviceCreateSchema, serviceQuerySchema } from "@/lib/validators";
import { calculateGravityScore } from "@/lib/ranking";
import { calculateRelevanceScore } from "@/lib/search";
import { createSlug } from "@/lib/utils";
import { checkDuplicate } from "@/lib/discovery/dedup";

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const params = serviceQuerySchema.parse(Object.fromEntries(searchParams));

    const where: Record<string, unknown> = {};
    if (params.category) where.category = params.category;
    if (params.pricing) where.pricingModel = params.pricing;
    if (params.korean) where.isKorean = true;

    if (params.q) {
      where.OR = [
        { name: { contains: params.q, mode: "insensitive" } },
        { description: { contains: params.q, mode: "insensitive" } },
        { tagline: { contains: params.q, mode: "insensitive" } },
        { tags: { contains: params.q, mode: "insensitive" } },
        { category: { contains: params.q, mode: "insensitive" } },
      ];
    }

    let orderBy: Record<string, string> = {};
    switch (params.sort) {
      case "newest": orderBy = { createdAt: "desc" }; break;
      case "popular": orderBy = { clicks: "desc" }; break;
      case "name": orderBy = { name: "asc" }; break;
      default: orderBy = { score: "desc" };
    }

    const skip = (params.page - 1) * params.limit;

    const [items, total] = await Promise.all([
      prisma.service.findMany({
        where: where as never,
        orderBy: orderBy as never,
        skip,
        take: params.limit,
      }),
      prisma.service.count({ where: where as never }),
    ]);

    let sortedItems = items;
    if (params.q && items.length > 0) {
      sortedItems = [...items].sort((a, b) => {
        const scoreA = calculateRelevanceScore(params.q!, a);
        const scoreB = calculateRelevanceScore(params.q!, b);
        return scoreB - scoreA;
      });
    }

    const totalPages = Math.ceil(total / params.limit);

    return NextResponse.json({
      items: sortedItems,
      total,
      page: params.page,
      totalPages,
      hasMore: params.page < totalPages,
    });
  } catch (error) {
    console.error("GET /api/services error:", error);
    return NextResponse.json(
      { error: "서비스 목록을 불러올 수 없습니다" },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const data = serviceCreateSchema.parse(body);

    // 기존 URL 중복 검사
    const existing = await prisma.service.findUnique({
      where: { url: data.url },
    });
    if (existing) {
      return NextResponse.json(
        { error: "이미 등록된 URL입니다" },
        { status: 409 }
      );
    }

    // 3단계 중복 검사 (URL 정규화 + 도메인 + 이름 유사도)
    const dupCheck = await checkDuplicate(data.url, data.name, prisma);
    if (dupCheck.isDuplicate) {
      return NextResponse.json(
        {
          error: "유사한 서비스가 이미 등록되어 있습니다",
          duplicate: {
            matchType: dupCheck.matchType,
            matchedServiceName: dupCheck.matchedServiceName,
            similarityScore: dupCheck.similarityScore,
          },
        },
        { status: 409 }
      );
    }

    // 도메인 매칭 경고 (중복은 아니지만 같은 도메인)
    let duplicateWarning = null;
    if (dupCheck.matchType === "domain") {
      duplicateWarning = {
        message: `같은 도메인의 서비스가 이미 존재합니다: ${dupCheck.matchedServiceName}`,
        matchedServiceName: dupCheck.matchedServiceName,
      };
    }

    let slug = createSlug(data.name);
    const existingSlug = await prisma.service.findUnique({ where: { slug } });
    if (existingSlug) {
      slug = `${slug}-${Date.now().toString(36)}`;
    }

    const service = await prisma.service.create({
      data: {
        slug,
        url: data.url,
        name: data.name,
        description: data.description,
        tagline: data.tagline,
        category: data.category,
        tags: JSON.stringify(data.tags || []),
        pricingModel: data.pricingModel,
        logoUrl: data.logoUrl || undefined,
        faviconUrl: data.faviconUrl || undefined,
        ogImageUrl: data.ogImageUrl || undefined,
        isKorean: data.isKorean,
        source: data.source || "user",
        score: calculateGravityScore(0, new Date()),
      },
    });

    return NextResponse.json(
      {
        service,
        message: "서비스가 등록되었습니다",
        ...(duplicateWarning && { warning: duplicateWarning }),
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("POST /api/services error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다", details: error },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "서비스 등록에 실패했습니다" },
      { status: 500 }
    );
  }
}
