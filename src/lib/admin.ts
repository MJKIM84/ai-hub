import { NextRequest } from "next/server";

/**
 * 어드민 인증 — ADMIN_SECRET 환경변수로 간단 인증
 * 헤더: Authorization: Bearer <token>
 * 쿼리: ?token=<token>
 */
export function verifyAdminToken(request: NextRequest): boolean {
  const adminSecret = process.env.ADMIN_SECRET;
  if (!adminSecret) return false;

  // 헤더 인증
  const authHeader = request.headers.get("authorization");
  if (authHeader === `Bearer ${adminSecret}`) return true;

  // 쿼리 파라미터 인증
  const { searchParams } = new URL(request.url);
  const token = searchParams.get("token");
  if (token === adminSecret) return true;

  return false;
}
