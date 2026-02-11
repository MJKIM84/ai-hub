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

    // 중복 투표 확인
    const existingVote = await prisma.vote.findUnique({
      where: {
        serviceId_voterIp_type: { serviceId, voterIp: ip, type },
      },
    });

    if (existingVote && (type === "upvote" || type === "downvote")) {
      return NextResponse.json(
        {
          error: type === "upvote" ? "이미 추천한 서비스입니다" : "이미 비추천한 서비스입니다",
          alreadyVoted: true,
        },
        { status: 409 }
      );
    }

    // 클릭은 중복 기록만 안 하고 카운트는 올림 (조회수 성격)
    if (!existingVote) {
      await prisma.vote.create({
        data: { serviceId, voterIp: ip, type },
      });
    }

    const updateData: Record<string, unknown> = {};
    if (type === "click") {
      updateData.clicks = { increment: 1 };
    } else if (type === "upvote" && !existingVote) {
      updateData.upvotes = { increment: 1 };
    } else if (type === "downvote" && !existingVote) {
      updateData.downvotes = { increment: 1 };
    }

    if (Object.keys(updateData).length > 0) {
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
        upvotes: updatedService.upvotes,
        downvotes: updatedService.downvotes,
      });
    }

    return NextResponse.json({
      success: true,
      upvotes: service.upvotes,
      downvotes: service.downvotes,
    });
  } catch (error) {
    console.error("POST /api/vote error:", error);
    return NextResponse.json(
      { error: "투표 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
