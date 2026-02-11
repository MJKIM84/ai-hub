import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { commentCreateSchema } from "@/lib/validators";
import { getClientIp } from "@/lib/utils";

const COMMENTS_PER_PAGE = 20;

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const serviceId = searchParams.get("serviceId");
    const page = Math.max(1, parseInt(searchParams.get("page") || "1", 10));

    if (!serviceId) {
      return NextResponse.json(
        { error: "serviceId가 필요합니다" },
        { status: 400 }
      );
    }

    const [items, total] = await Promise.all([
      prisma.comment.findMany({
        where: { serviceId },
        orderBy: { createdAt: "desc" },
        skip: (page - 1) * COMMENTS_PER_PAGE,
        take: COMMENTS_PER_PAGE,
        select: {
          id: true,
          content: true,
          authorName: true,
          likes: true,
          dislikes: true,
          createdAt: true,
        },
      }),
      prisma.comment.count({ where: { serviceId } }),
    ]);

    return NextResponse.json({
      items,
      total,
      page,
      hasMore: page * COMMENTS_PER_PAGE < total,
    });
  } catch (error) {
    console.error("GET /api/comments error:", error);
    return NextResponse.json(
      { error: "댓글을 불러올 수 없습니다" },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const data = commentCreateSchema.parse(body);

    const ip = getClientIp(request.headers);

    // 같은 IP로 같은 서비스에 1분 내 중복 댓글 방지
    const recentComment = await prisma.comment.findFirst({
      where: {
        serviceId: data.serviceId,
        authorIp: ip,
        createdAt: { gte: new Date(Date.now() - 60 * 1000) },
      },
    });

    if (recentComment) {
      return NextResponse.json(
        { error: "잠시 후 다시 시도해주세요" },
        { status: 429 }
      );
    }

    // 서비스 존재 확인
    const service = await prisma.service.findUnique({
      where: { id: data.serviceId },
    });

    if (!service) {
      return NextResponse.json(
        { error: "서비스를 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    const comment = await prisma.comment.create({
      data: {
        serviceId: data.serviceId,
        content: data.content,
        authorName: data.authorName,
        authorIp: ip,
      },
      select: {
        id: true,
        content: true,
        authorName: true,
        likes: true,
        dislikes: true,
        createdAt: true,
      },
    });

    return NextResponse.json(comment, { status: 201 });
  } catch (error) {
    console.error("POST /api/comments error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다", details: error },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "댓글 작성에 실패했습니다" },
      { status: 500 }
    );
  }
}
