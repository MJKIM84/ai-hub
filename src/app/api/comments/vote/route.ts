import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { commentVoteSchema } from "@/lib/validators";
import { getClientIp } from "@/lib/utils";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { commentId, type } = commentVoteSchema.parse(body);

    const ip = getClientIp(request.headers);

    // 댓글 존재 확인
    const comment = await prisma.comment.findUnique({
      where: { id: commentId },
    });

    if (!comment) {
      return NextResponse.json(
        { error: "댓글을 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    // 중복 투표 확인
    const existingVote = await prisma.commentVote.findUnique({
      where: {
        commentId_voterIp_type: { commentId, voterIp: ip, type },
      },
    });

    if (existingVote) {
      return NextResponse.json(
        { error: "이미 투표했습니다", alreadyVoted: true },
        { status: 409 }
      );
    }

    // 투표 생성 + 카운트 업데이트
    await prisma.commentVote.create({
      data: { commentId, voterIp: ip, type },
    });

    const updateData = type === "like"
      ? { likes: { increment: 1 } }
      : { dislikes: { increment: 1 } };

    const updatedComment = await prisma.comment.update({
      where: { id: commentId },
      data: updateData,
    });

    return NextResponse.json({
      success: true,
      likes: updatedComment.likes,
      dislikes: updatedComment.dislikes,
    });
  } catch (error) {
    console.error("POST /api/comments/vote error:", error);
    return NextResponse.json(
      { error: "투표 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
