import { NextResponse } from "next/server";
import { clearAdminSession } from "@/lib/admin";

export async function POST() {
  try {
    await clearAdminSession();
    return NextResponse.json({ success: true });
  } catch {
    return NextResponse.json(
      { error: "로그아웃 처리 중 오류가 발생했습니다" },
      { status: 500 }
    );
  }
}
