import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { z } from "zod";
import { getClientIp } from "@/lib/utils";

const feedbackSchema = z.object({
  type: z.enum(["partnership", "feedback"]),
  email: z.string().email().optional(),
  message: z.string().min(1, "메시지를 입력해주세요").max(2000),
});

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const data = feedbackSchema.parse(body);
    const ip = getClientIp(request.headers);

    // IP당 5분 내 중복 방지
    const recent = await prisma.feedback.findFirst({
      where: {
        senderIp: ip,
        createdAt: { gte: new Date(Date.now() - 5 * 60 * 1000) },
      },
    });

    if (recent) {
      return NextResponse.json(
        { error: "잠시 후 다시 시도해주세요." },
        { status: 429 }
      );
    }

    await prisma.feedback.create({
      data: {
        type: data.type,
        email: data.email || null,
        message: data.message,
        senderIp: ip,
      },
    });

    return NextResponse.json({ success: true }, { status: 201 });
  } catch (error) {
    console.error("POST /api/feedback error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다" },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "전송에 실패했습니다" },
      { status: 500 }
    );
  }
}
