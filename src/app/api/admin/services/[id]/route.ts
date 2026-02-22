import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";

interface RouteParams {
  params: Promise<{ id: string }>;
}

/** 서비스 수정 */
export async function PATCH(request: NextRequest, { params }: RouteParams) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const { id } = await params;
    const body = await request.json();

    const service = await prisma.service.findUnique({ where: { id } });
    if (!service) {
      return NextResponse.json({ error: "Service not found" }, { status: 404 });
    }

    const allowedFields = [
      "name", "nameKo", "description", "descriptionKo", "tagline",
      "url", "category", "tags", "pricingModel",
      "isVerified", "isKorean", "logoUrl", "faviconUrl", "ogImageUrl",
    ];

    const updateData: Record<string, unknown> = {};
    for (const field of allowedFields) {
      if (body[field] !== undefined) {
        updateData[field] = body[field];
      }
    }

    const updated = await prisma.service.update({
      where: { id },
      data: updateData,
    });

    return NextResponse.json({ success: true, service: updated });
  } catch (error) {
    console.error("PATCH /api/admin/services/[id] error:", error);
    return NextResponse.json({ error: "Failed to update service" }, { status: 500 });
  }
}

/** 서비스 삭제 */
export async function DELETE(request: NextRequest, { params }: RouteParams) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const { id } = await params;

    const service = await prisma.service.findUnique({ where: { id } });
    if (!service) {
      return NextResponse.json({ error: "Service not found" }, { status: 404 });
    }

    await prisma.service.delete({ where: { id } });

    return NextResponse.json({ success: true, deleted: service.name });
  } catch (error) {
    console.error("DELETE /api/admin/services/[id] error:", error);
    return NextResponse.json({ error: "Failed to delete service" }, { status: 500 });
  }
}
