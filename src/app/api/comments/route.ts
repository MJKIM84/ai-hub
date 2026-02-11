import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { commentCreateSchema, commentUpdateSchema, commentDeleteSchema } from "@/lib/validators";
import { getClientIp, maskIp, hashPassword } from "@/lib/utils";

const COMMENTS_PER_PAGE = 20;

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const serviceId = searchParams.get("serviceId");
    const page = Math.max(1, parseInt(searchParams.get("page") || "1", 10));
    const parentId = searchParams.get("parentId"); // null = top-level only

    if (!serviceId) {
      return NextResponse.json(
        { error: "serviceId가 필요합니다" },
        { status: 400 }
      );
    }

    const where = parentId
      ? { serviceId, parentId }
      : { serviceId, parentId: null }; // top-level comments only

    const [items, total] = await Promise.all([
      prisma.comment.findMany({
        where,
        orderBy: { createdAt: "desc" },
        skip: (page - 1) * COMMENTS_PER_PAGE,
        take: COMMENTS_PER_PAGE,
        select: {
          id: true,
          content: true,
          authorName: true,
          authorIp: true,
          likes: true,
          dislikes: true,
          parentId: true,
          createdAt: true,
          _count: { select: { replies: true } },
        },
      }),
      prisma.comment.count({ where }),
    ]);

    // Mask IPs before sending to client
    const maskedItems = items.map((item) => ({
      id: item.id,
      content: item.content,
      authorName: item.authorName,
      maskedIp: maskIp(item.authorIp),
      likes: item.likes,
      dislikes: item.dislikes,
      parentId: item.parentId,
      replyCount: item._count.replies,
      createdAt: item.createdAt,
    }));

    return NextResponse.json({
      items: maskedItems,
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

    // parentId 유효성 확인
    if (data.parentId) {
      const parentComment = await prisma.comment.findUnique({
        where: { id: data.parentId },
      });
      if (!parentComment || parentComment.serviceId !== data.serviceId) {
        return NextResponse.json(
          { error: "부모 댓글을 찾을 수 없습니다" },
          { status: 404 }
        );
      }
    }

    const hashedPw = await hashPassword(data.password);

    const comment = await prisma.comment.create({
      data: {
        serviceId: data.serviceId,
        content: data.content,
        authorName: data.authorName,
        authorIp: ip,
        password: hashedPw,
        parentId: data.parentId || null,
      },
      select: {
        id: true,
        content: true,
        authorName: true,
        authorIp: true,
        likes: true,
        dislikes: true,
        parentId: true,
        createdAt: true,
      },
    });

    return NextResponse.json({
      ...comment,
      maskedIp: maskIp(comment.authorIp),
      authorIp: undefined,
      replyCount: 0,
    }, { status: 201 });
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

export async function PATCH(request: NextRequest) {
  try {
    const body = await request.json();
    const data = commentUpdateSchema.parse(body);

    const comment = await prisma.comment.findUnique({
      where: { id: data.commentId },
    });

    if (!comment) {
      return NextResponse.json(
        { error: "댓글을 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    const hashedPw = await hashPassword(data.password);
    if (hashedPw !== comment.password) {
      return NextResponse.json(
        { error: "비밀번호가 일치하지 않습니다" },
        { status: 403 }
      );
    }

    const updated = await prisma.comment.update({
      where: { id: data.commentId },
      data: { content: data.content },
      select: {
        id: true,
        content: true,
        authorName: true,
        authorIp: true,
        likes: true,
        dislikes: true,
        parentId: true,
        createdAt: true,
        _count: { select: { replies: true } },
      },
    });

    return NextResponse.json({
      id: updated.id,
      content: updated.content,
      authorName: updated.authorName,
      maskedIp: maskIp(updated.authorIp),
      likes: updated.likes,
      dislikes: updated.dislikes,
      parentId: updated.parentId,
      replyCount: updated._count.replies,
      createdAt: updated.createdAt,
    });
  } catch (error) {
    console.error("PATCH /api/comments error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다" },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "댓글 수정에 실패했습니다" },
      { status: 500 }
    );
  }
}

export async function DELETE(request: NextRequest) {
  try {
    const body = await request.json();
    const data = commentDeleteSchema.parse(body);

    const comment = await prisma.comment.findUnique({
      where: { id: data.commentId },
    });

    if (!comment) {
      return NextResponse.json(
        { error: "댓글을 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    const hashedPw = await hashPassword(data.password);
    if (hashedPw !== comment.password) {
      return NextResponse.json(
        { error: "비밀번호가 일치하지 않습니다" },
        { status: 403 }
      );
    }

    // Cascade delete will handle replies and votes
    await prisma.comment.delete({
      where: { id: data.commentId },
    });

    return NextResponse.json({ success: true, deletedId: data.commentId });
  } catch (error) {
    console.error("DELETE /api/comments error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다" },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "댓글 삭제에 실패했습니다" },
      { status: 500 }
    );
  }
}
