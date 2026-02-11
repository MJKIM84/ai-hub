import { NextRequest, NextResponse } from "next/server";
import { verifyAdminCredentials, setAdminSession } from "@/lib/admin";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { id, password } = body;

    if (!id || !password) {
      return NextResponse.json(
        { error: "ID와 비밀번호를 입력해주세요" },
        { status: 400 }
      );
    }

    if (!verifyAdminCredentials(id, password)) {
      // 브루트포스 방지용 지연
      await new Promise((r) => setTimeout(r, 1000));
      return NextResponse.json(
        { error: "ID 또는 비밀번호가 올바르지 않습니다" },
        { status: 401 }
      );
    }

    await setAdminSession();

    return NextResponse.json({ success: true });
  } catch {
    return NextResponse.json(
      { error: "로그인 처리 중 오류가 발생했습니다" },
      { status: 500 }
    );
  }
}
