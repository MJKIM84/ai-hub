import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { voteRequestSchema } from "@/lib/validators";
import { calculateGravityScore, calculatePoints } from "@/lib/ranking";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { serviceId, type } = voteRequestSchema.parse(body);

    const ip = request.headers.get("x-forwarded-for") ||
      request.headers.get("x-real-ip") ||
      "anonymous";

    const service = await prisma.service.findUnique({
      where: { id: serviceId },
    });

    if (!service) {
      return NextResponse.json(
        { error: "서비스를 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    try {
      await prisma.vote.create({
        data: { serviceId, voterIp: ip, type },
      });
    } catch {
      // Duplicate vote - silently ignore
    }

    const updateData: Record<string, unknown> = {};
    if (type === "click") {
      updateData.clicks = { increment: 1 };
    } else {
      updateData.upvotes = { increment: 1 };
    }

    const updatedService = await prisma.service.update({
      where: { id: serviceId },
      data: updateData as never,
    });

    const points = calculatePoints(updatedService.clicks, updatedService.upvotes);
    const newScore = calculateGravityScore(points, updatedService.createdAt);

    await prisma.service.update({
      where: { id: serviceId },
      data: { score: newScore },
    });

    return NextResponse.json({
      success: true,
      newCount: type === "click" ? updatedService.clicks : updatedService.upvotes,
    });
  } catch (error) {
    console.error("POST /api/vote error:", error);
    return NextResponse.json(
      { error: "투표 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
