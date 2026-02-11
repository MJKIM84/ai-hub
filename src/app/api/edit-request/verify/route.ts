import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const token = searchParams.get("token");

    if (!token) {
      return NextResponse.json(
        { error: "인증 토큰이 필요합니다" },
        { status: 400 }
      );
    }

    const editRequest = await prisma.editRequest.findUnique({
      where: { verifyToken: token },
      include: { service: true },
    });

    if (!editRequest) {
      return NextResponse.json(
        { error: "유효하지 않은 토큰입니다" },
        { status: 404 }
      );
    }

    if (editRequest.isVerified) {
      return NextResponse.json({
        message: "이미 인증되었습니다",
        requestId: editRequest.id,
        status: editRequest.status,
      });
    }

    // 이메일 인증 처리
    await prisma.editRequest.update({
      where: { id: editRequest.id },
      data: { isVerified: true },
    });

    return NextResponse.json({
      success: true,
      message: "이메일 인증이 완료되었습니다. 관리자 검토 후 반영됩니다.",
      requestId: editRequest.id,
      serviceName: editRequest.service.name,
    });
  } catch (error) {
    console.error("GET /api/edit-request/verify error:", error);
    return NextResponse.json(
      { error: "인증 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
