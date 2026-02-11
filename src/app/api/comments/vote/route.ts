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

    // 기존 투표 확인 (unique: commentId + voterIp)
    const existingVote = await prisma.commentVote.findUnique({
      where: {
        commentId_voterIp: { commentId, voterIp: ip },
      },
    });

    if (existingVote) {
      if (existingVote.type === type) {
        // 같은 타입 클릭 → 투표 취소
        await prisma.commentVote.delete({
          where: { id: existingVote.id },
        });

        const updateData = type === "like"
          ? { likes: { decrement: 1 } }
          : { dislikes: { decrement: 1 } };

        const updatedComment = await prisma.comment.update({
          where: { id: commentId },
          data: updateData,
        });

        return NextResponse.json({
          success: true,
          action: "cancelled",
          likes: updatedComment.likes,
          dislikes: updatedComment.dislikes,
        });
      } else {
        // 다른 타입 → 투표 변경
        await prisma.commentVote.update({
          where: { id: existingVote.id },
          data: { type },
        });

        // 기존 타입 감소 + 새 타입 증가
        const updateData = type === "like"
          ? { likes: { increment: 1 }, dislikes: { decrement: 1 } }
          : { dislikes: { increment: 1 }, likes: { decrement: 1 } };

        const updatedComment = await prisma.comment.update({
          where: { id: commentId },
          data: updateData,
        });

        return NextResponse.json({
          success: true,
          action: "switched",
          likes: updatedComment.likes,
          dislikes: updatedComment.dislikes,
        });
      }
    }

    // 신규 투표
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
      action: "voted",
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
