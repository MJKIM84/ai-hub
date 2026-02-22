import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";

export async function GET(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    // KST 기준 오늘 시작
    const todayStart = new Date();
    todayStart.setHours(todayStart.getHours() + 9);
    todayStart.setHours(0, 0, 0, 0);
    todayStart.setHours(todayStart.getHours() - 9);

    const [
      totalServices,
      todayServices,
      pendingFeedback,
      pendingEditRequests,
      pendingDiscoveries,
      reportedComments,
      totalComments,
      totalClicks,
    ] = await Promise.all([
      prisma.service.count(),
      prisma.service.count({ where: { createdAt: { gte: todayStart } } }),
      prisma.feedback.count({ where: { status: "pending" } }),
      prisma.editRequest.count({ where: { status: "pending" } }),
      prisma.discoveryLog.count({ where: { status: "pending" } }),
      prisma.comment.count({ where: { reports: { gt: 0 }, isHidden: false, isDeleted: false } }),
      prisma.comment.count(),
      prisma.service.aggregate({ _sum: { clicks: true } }),
    ]);

    return NextResponse.json({
      totalServices,
      todayServices,
      pendingFeedback,
      pendingEditRequests,
      pendingDiscoveries,
      reportedComments,
      totalComments,
      totalClicks: totalClicks._sum.clicks || 0,
    });
  } catch (error) {
    console.error("GET /api/admin/dashboard error:", error);
    return NextResponse.json({ error: "Failed to fetch dashboard data" }, { status: 500 });
  }
}
