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
    const limit = parseInt(searchParams.get("limit") || "20");
    const onlyHidden = searchParams.get("hidden") === "true";

    // 신고가 1건 이상인 댓글 조회
    const where: Record<string, unknown> = {
      reports: { gt: 0 },
    };
    if (onlyHidden) {
      where.isHidden = true;
    }

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
          createdAt: true,
          serviceId: true,
          service: { select: { id: true, name: true, slug: true } },
          commentReports: {
            select: {
              id: true,
              reporterIp: true,
              reason: true,
              createdAt: true,
            },
            orderBy: { createdAt: "desc" as const },
            take: 10,
          },
        },
        orderBy: { reports: "desc" },
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
      commentReports: item.commentReports.map((r) => ({
        ...r,
        reporterIp: r.reporterIp
          ? r.reporterIp.split(".").slice(0, 2).join(".") + ".*.*"
          : "",
      })),
    }));

    return NextResponse.json({
      items: maskedItems,
      total,
      page,
      totalPages: Math.ceil(total / limit),
    });
  } catch (error) {
    console.error("GET /api/admin/reports error:", error);
    return NextResponse.json({ error: "Failed to fetch reports" }, { status: 500 });
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
        data: { isHidden: false, reports: 0 },
      });
      // 신고 기록 초기화
      await prisma.commentReport.deleteMany({
        where: { commentId },
      });
    } else if (action === "delete") {
      // 소프트 삭제
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
    console.error("PATCH /api/admin/reports error:", error);
    return NextResponse.json({ error: "Failed to process action" }, { status: 500 });
  }
}
