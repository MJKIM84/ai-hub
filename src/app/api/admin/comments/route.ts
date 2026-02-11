import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get("page") || "1");
    const limit = parseInt(searchParams.get("limit") || "30");
    const filter = searchParams.get("filter"); // "hidden", "deleted", "all"

    const where: Record<string, unknown> = {};
    if (filter === "hidden") {
      where.isHidden = true;
      where.isDeleted = false;
    } else if (filter === "deleted") {
      where.isDeleted = true;
    }
    // "all" = no filter

    const [items, total] = await Promise.all([
      prisma.comment.findMany({
        where: where as never,
        select: {
          id: true,
          content: true,
          authorName: true,
          authorIp: true,
          reports: true,
          isHidden: true,
          isDeleted: true,
          likes: true,
          dislikes: true,
          parentId: true,
          createdAt: true,
          service: { select: { id: true, name: true, slug: true } },
        },
        orderBy: { createdAt: "desc" },
        skip: (page - 1) * limit,
        take: limit,
      }),
      prisma.comment.count({ where: where as never }),
    ]);

    // IP 마스킹
    const maskedItems = items.map((item) => ({
      ...item,
      authorIp: item.authorIp
        ? item.authorIp.split(".").slice(0, 2).join(".") + ".*.*"
        : "",
    }));

    return NextResponse.json({
      items: maskedItems,
      total,
      page,
      totalPages: Math.ceil(total / limit),
    });
  } catch (error) {
    console.error("GET /api/admin/comments error:", error);
    return NextResponse.json({ error: "Failed to fetch comments" }, { status: 500 });
  }
}

export async function PATCH(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const body = await request.json();
    const { commentId, action } = body;

    if (!commentId || !action) {
      return NextResponse.json({ error: "commentId and action required" }, { status: 400 });
    }

    if (action === "hide") {
      await prisma.comment.update({
        where: { id: commentId },
        data: { isHidden: true },
      });
    } else if (action === "unhide") {
      await prisma.comment.update({
        where: { id: commentId },
        data: { isHidden: false },
      });
    } else if (action === "delete") {
      await prisma.comment.update({
        where: { id: commentId },
        data: {
          isDeleted: true,
          content: "",
          authorName: "삭제됨",
          authorIp: "",
          password: "",
        },
      });
    } else {
      return NextResponse.json({ error: "Invalid action" }, { status: 400 });
    }

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("PATCH /api/admin/comments error:", error);
    return NextResponse.json({ error: "Failed to process action" }, { status: 500 });
  }
}
