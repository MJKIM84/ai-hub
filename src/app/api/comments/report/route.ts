import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { commentReportSchema } from "@/lib/validators";
import { getClientIp } from "@/lib/utils";

const AUTO_HIDE_THRESHOLD = 5;

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const data = commentReportSchema.parse(body);
    const ip = getClientIp(request.headers);

    // 댓글 존재 확인
    const comment = await prisma.comment.findUnique({
      where: { id: data.commentId },
    });

    if (!comment) {
      return NextResponse.json(
        { error: "댓글을 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    // 이미 신고했는지 확인
    const existing = await prisma.commentReport.findUnique({
      where: {
        commentId_reporterIp: {
          commentId: data.commentId,
          reporterIp: ip,
        },
      },
    });

    if (existing) {
      return NextResponse.json(
        { error: "이미 신고한 댓글입니다" },
        { status: 409 }
      );
    }

    // 신고 생성 + 카운트 증가를 트랜잭션으로
    const result = await prisma.$transaction(async (tx) => {
      await tx.commentReport.create({
        data: {
          commentId: data.commentId,
          reporterIp: ip,
          reason: data.reason || null,
        },
      });

      const updated = await tx.comment.update({
        where: { id: data.commentId },
        data: {
          reports: { increment: 1 },
          // 5개 이상이면 자동 숨김
          ...(comment.reports + 1 >= AUTO_HIDE_THRESHOLD && {
            isHidden: true,
          }),
        },
        select: {
          reports: true,
          isHidden: true,
        },
      });

      return updated;
    });

    return NextResponse.json({
      success: true,
      reports: result.reports,
      isHidden: result.isHidden,
    });
  } catch (error) {
    console.error("POST /api/comments/report error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다" },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "신고 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
