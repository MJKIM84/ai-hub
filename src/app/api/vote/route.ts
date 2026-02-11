import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { voteRequestSchema } from "@/lib/validators";
import { calculateGravityScore, calculatePoints } from "@/lib/ranking";
import { getClientIp } from "@/lib/utils";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { serviceId, type } = voteRequestSchema.parse(body);

    const ip = getClientIp(request.headers);

    const service = await prisma.service.findUnique({
      where: { id: serviceId },
    });

    if (!service) {
      return NextResponse.json(
        { error: "서비스를 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    // 클릭은 단순 카운트 증가 (Vote 레코드 없이)
    if (type === "click") {
      await prisma.service.update({
        where: { id: serviceId },
        data: { clicks: { increment: 1 } },
      });

      return NextResponse.json({
        success: true,
        upvotes: service.upvotes,
        downvotes: service.downvotes,
      });
    }

    // 추천/비추천 처리 — unique(serviceId, voterIp)로 1인 1표
    const existingVote = await prisma.vote.findUnique({
      where: {
        serviceId_voterIp: { serviceId, voterIp: ip },
      },
    });

    let updateData: Record<string, unknown> = {};
    let action = "voted";

    if (existingVote) {
      if (existingVote.type === type) {
        // 같은 타입 재클릭 → 투표 취소
        await prisma.vote.delete({
          where: { id: existingVote.id },
        });

        updateData = type === "upvote"
          ? { upvotes: { decrement: 1 } }
          : { downvotes: { decrement: 1 } };
        action = "cancelled";
      } else {
        // 다른 타입 → 투표 변경 (upvote ↔ downvote)
        await prisma.vote.update({
          where: { id: existingVote.id },
          data: { type },
        });

        updateData = type === "upvote"
          ? { upvotes: { increment: 1 }, downvotes: { decrement: 1 } }
          : { downvotes: { increment: 1 }, upvotes: { decrement: 1 } };
        action = "switched";
      }
    } else {
      // 신규 투표
      await prisma.vote.create({
        data: { serviceId, voterIp: ip, type },
      });

      updateData = type === "upvote"
        ? { upvotes: { increment: 1 } }
        : { downvotes: { increment: 1 } };
      action = "voted";
    }

    const updatedService = await prisma.service.update({
      where: { id: serviceId },
      data: updateData as never,
    });

    const points = calculatePoints(updatedService.clicks, updatedService.upvotes, updatedService.downvotes);
    const newScore = calculateGravityScore(points, updatedService.createdAt);

    await prisma.service.update({
      where: { id: serviceId },
      data: { score: newScore },
    });

    return NextResponse.json({
      success: true,
      action,
      upvotes: updatedService.upvotes,
      downvotes: updatedService.downvotes,
    });
  } catch (error) {
    console.error("POST /api/vote error:", error);
    return NextResponse.json(
      { error: "투표 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
