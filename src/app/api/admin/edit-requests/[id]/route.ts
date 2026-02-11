import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";

interface RouteParams {
  params: Promise<{ id: string }>;
}

export async function PATCH(request: NextRequest, { params }: RouteParams) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const { id } = await params;
    const body = await request.json();
    const { action, adminNote } = body; // action: "approve" | "reject"

    const editRequest = await prisma.editRequest.findUnique({
      where: { id },
      include: { service: true },
    });

    if (!editRequest) {
      return NextResponse.json({ error: "Not found" }, { status: 404 });
    }

    if (action === "approve") {
      // 변경 사항 적용
      const changes = JSON.parse(editRequest.changes) as Record<string, unknown>;
      const updateData: Record<string, unknown> = {};

      if (changes.name) updateData.name = changes.name;
      if (changes.description) updateData.description = changes.description;
      if (changes.category) updateData.category = changes.category;
      if (changes.pricingModel) updateData.pricingModel = changes.pricingModel;

      // 클레임 요청인 경우 source를 developer로 변경
      if (editRequest.requestType === "claim") {
        updateData.source = "developer";
        updateData.isVerified = true;
      }

      if (Object.keys(updateData).length > 0) {
        await prisma.service.update({
          where: { id: editRequest.serviceId },
          data: updateData as never,
        });
      }

      await prisma.editRequest.update({
        where: { id },
        data: { status: "approved", adminNote },
      });

      return NextResponse.json({ success: true, message: "요청이 승인되었습니다" });
    } else if (action === "reject") {
      await prisma.editRequest.update({
        where: { id },
        data: { status: "rejected", adminNote },
      });

      return NextResponse.json({ success: true, message: "요청이 거절되었습니다" });
    }

    return NextResponse.json({ error: "Invalid action" }, { status: 400 });
  } catch (error) {
    console.error("PATCH /api/admin/edit-requests/[id] error:", error);
    return NextResponse.json({ error: "Failed to update edit request" }, { status: 500 });
  }
}
