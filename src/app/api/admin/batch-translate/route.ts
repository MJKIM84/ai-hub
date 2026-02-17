import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken } from "@/lib/admin";
import { translateService } from "@/lib/translator";

export const dynamic = "force-dynamic";
export const maxDuration = 60;

/**
 * 기존 영어 서비스 일괄 번역 (nameKo, descriptionKo가 없는 서비스 대상)
 * POST /api/admin/batch-translate
 */
export async function POST(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    // nameKo가 null인 서비스 조회
    const services = await prisma.service.findMany({
      where: {
        nameKo: null,
      },
      select: {
        id: true,
        name: true,
        description: true,
      },
      take: 50, // 한 번에 최대 50개
    });

    if (services.length === 0) {
      return NextResponse.json({
        message: "번역할 서비스가 없습니다.",
        translated: 0,
        errors: [],
      });
    }

    let translated = 0;
    const errors: string[] = [];

    for (const svc of services) {
      try {
        const result = await translateService(svc.name, svc.description);

        await prisma.service.update({
          where: { id: svc.id },
          data: {
            nameKo: result.nameKo,
            descriptionKo: result.descriptionKo,
          },
        });

        translated++;

        // Google Translate 레이트 리밋 방지
        await new Promise((r) => setTimeout(r, 500));
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        errors.push(`${svc.name}: ${msg}`);
      }
    }

    return NextResponse.json({
      message: `${translated}개 서비스 번역 완료`,
      translated,
      remaining: services.length - translated,
      errors,
    });
  } catch (error) {
    console.error("Batch translate error:", error);
    return NextResponse.json(
      { error: "번역 실패" },
      { status: 500 }
    );
  }
}
