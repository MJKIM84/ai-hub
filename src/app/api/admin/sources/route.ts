import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const sources = await prisma.discoverySource.findMany({
      orderBy: { priority: "desc" },
    });

    return NextResponse.json({ items: sources });
  } catch (error) {
    console.error("GET /api/admin/sources error:", error);
    return NextResponse.json({ error: "Failed to fetch sources" }, { status: 500 });
  }
}

export async function POST(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const body = await request.json();
    const { name, type, url, priority, isActive } = body;

    if (!name || !type || !url) {
      return NextResponse.json({ error: "name, type, url are required" }, { status: 400 });
    }

    const source = await prisma.discoverySource.upsert({
      where: { url },
      update: { name, type, priority: priority || 0, isActive: isActive ?? true },
      create: { name, type, url, priority: priority || 0, isActive: isActive ?? true },
    });

    return NextResponse.json({ success: true, source }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/sources error:", error);
    return NextResponse.json({ error: "Failed to create/update source" }, { status: 500 });
  }
}
