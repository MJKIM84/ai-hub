import { NextRequest } from "next/server";
import { cookies } from "next/headers";

const SESSION_COOKIE_NAME = "admin_session";
const SESSION_MAX_AGE = 60 * 60 * 24; // 24시간

/**
 * 세션 토큰 생성 — HMAC 기반 간단 서명
 */
function generateSessionToken(): string {
  const secret = process.env.ADMIN_SECRET || "fallback-secret";
  const timestamp = Date.now().toString();
  const payload = `${timestamp}:${secret}`;

  // Web Crypto 없이 간단한 해시 생성
  let hash = 0;
  for (let i = 0; i < payload.length; i++) {
    const char = payload.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash |= 0;
  }
  return `${timestamp}:${Math.abs(hash).toString(36)}`;
}

/**
 * 세션 토큰 검증 — 24시간 이내 생성된 토큰인지 확인
 */
function isValidSessionToken(token: string): boolean {
  const parts = token.split(":");
  if (parts.length !== 2) return false;

  const timestamp = parseInt(parts[0]);
  if (isNaN(timestamp)) return false;

  const age = Date.now() - timestamp;
  return age >= 0 && age < SESSION_MAX_AGE * 1000;
}

/**
 * 어드민 인증 — ID/비밀번호 검증
 */
export function verifyAdminCredentials(id: string, password: string): boolean {
  const adminId = process.env.ADMIN_ID;
  const adminPassword = process.env.ADMIN_PASSWORD;

  if (!adminId || !adminPassword) return false;
  return id === adminId && password === adminPassword;
}

/**
 * 세션 쿠키 설정
 */
export async function setAdminSession(): Promise<string> {
  const token = generateSessionToken();
  const cookieStore = await cookies();
  cookieStore.set(SESSION_COOKIE_NAME, token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: SESSION_MAX_AGE,
    path: "/",
  });
  return token;
}

/**
 * 세션 쿠키 삭제
 */
export async function clearAdminSession(): Promise<void> {
  const cookieStore = await cookies();
  cookieStore.delete(SESSION_COOKIE_NAME);
}

/**
 * 어드민 인증 확인 (3가지 방식 지원)
 * 1. 세션 쿠키 (로그인 기반)
 * 2. Authorization 헤더 (Bearer token)
 * 3. 쿼리 파라미터 (?token=) — 하위 호환
 */
export function verifyAdminToken(request: NextRequest): boolean {
  // 1. 세션 쿠키 확인
  const sessionCookie = request.cookies.get(SESSION_COOKIE_NAME);
  if (sessionCookie && isValidSessionToken(sessionCookie.value)) {
    return true;
  }

  const adminSecret = process.env.ADMIN_SECRET;
  if (!adminSecret) return false;

  // 2. Authorization 헤더
  const authHeader = request.headers.get("authorization");
  if (authHeader === `Bearer ${adminSecret}`) return true;

  // 3. 쿼리 파라미터 (하위 호환)
  const { searchParams } = new URL(request.url);
  const token = searchParams.get("token");
  if (token === adminSecret) return true;

  return false;
}
