import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { verifyAdminToken, verifyPassword, hashPassword } from "@/lib/admin";

export async function POST(request: NextRequest) {
  if (!verifyAdminToken(request)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  try {
    const { currentPassword, newPassword } = await request.json();

    if (!currentPassword || !newPassword) {
      return NextResponse.json(
        { error: "현재 비밀번호와 새 비밀번호를 입력해주세요" },
        { status: 400 }
      );
    }

    if (newPassword.length < 4) {
      return NextResponse.json(
        { error: "비밀번호는 4자 이상이어야 합니다" },
        { status: 400 }
      );
    }

    // 현재 관리자 계정 가져오기 (첫 번째 계정)
    const admin = await prisma.adminUser.findFirst();
    if (!admin) {
      return NextResponse.json({ error: "관리자 계정이 없습니다" }, { status: 404 });
    }

    // 현재 비밀번호 확인
    if (!verifyPassword(currentPassword, admin.password)) {
      return NextResponse.json(
        { error: "현재 비밀번호가 올바르지 않습니다" },
        { status: 401 }
      );
    }

    // 새 비밀번호로 업데이트
    await prisma.adminUser.update({
      where: { id: admin.id },
      data: { password: hashPassword(newPassword) },
    });

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error("Change password error:", error);
    return NextResponse.json(
      { error: "비밀번호 변경 중 오류가 발생했습니다" },
      { status: 500 }
    );
  }
}
