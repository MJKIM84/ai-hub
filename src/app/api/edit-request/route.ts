import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { editRequestSchema } from "@/lib/validators";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const data = editRequestSchema.parse(body);

    // 서비스 존재 확인
    const service = await prisma.service.findUnique({
      where: { id: data.serviceId },
    });
    if (!service) {
      return NextResponse.json(
        { error: "서비스를 찾을 수 없습니다" },
        { status: 404 }
      );
    }

    // 같은 이메일로 동일 서비스에 대한 대기중 요청이 있는지 확인
    const existingRequest = await prisma.editRequest.findFirst({
      where: {
        serviceId: data.serviceId,
        contactEmail: data.contactEmail,
        status: "pending",
      },
    });
    if (existingRequest) {
      return NextResponse.json(
        { error: "이미 대기 중인 요청이 있습니다" },
        { status: 409 }
      );
    }

    const editRequest = await prisma.editRequest.create({
      data: {
        serviceId: data.serviceId,
        requestType: data.requestType,
        contactEmail: data.contactEmail,
        changes: JSON.stringify(data.changes || {}),
        reason: data.reason,
      },
    });

    return NextResponse.json(
      {
        success: true,
        requestId: editRequest.id,
        verifyToken: editRequest.verifyToken,
        message:
          data.requestType === "claim"
            ? "클레임 요청이 접수되었습니다. 인증 토큰을 확인해주세요."
            : "수정 요청이 접수되었습니다.",
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("POST /api/edit-request error:", error);
    if (error instanceof Error && error.name === "ZodError") {
      return NextResponse.json(
        { error: "입력 데이터가 유효하지 않습니다", details: error },
        { status: 400 }
      );
    }
    return NextResponse.json(
      { error: "요청 처리에 실패했습니다" },
      { status: 500 }
    );
  }
}
