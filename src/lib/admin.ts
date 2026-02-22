import { NextRequest } from "next/server";
import { cookies } from "next/headers";
import { scryptSync, randomBytes, timingSafeEqual } from "crypto";
import { prisma } from "@/lib/prisma";

const SESSION_COOKIE_NAME = "admin_session";
const SESSION_MAX_AGE = 60 * 60 * 24; // 24시간

// ─── 비밀번호 해싱 ───

export function hashPassword(password: string): string {
  const salt = randomBytes(16).toString("hex");
  const hash = scryptSync(password, salt, 64).toString("hex");
  return `${salt}:${hash}`;
}

export function verifyPassword(password: string, stored: string): boolean {
  const [salt, hash] = stored.split(":");
  if (!salt || !hash) return false;
  const hashBuffer = Buffer.from(hash, "hex");
  const derivedKey = scryptSync(password, salt, 64);
  return timingSafeEqual(hashBuffer, derivedKey);
}

// ─── 세션 관리 ───

function generateSessionToken(): string {
  const secret = process.env.ADMIN_SECRET || "fallback-secret";
  const timestamp = Date.now().toString();
  const payload = `${timestamp}:${secret}`;

  let hash = 0;
  for (let i = 0; i < payload.length; i++) {
    const char = payload.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash |= 0;
  }
  return `${timestamp}:${Math.abs(hash).toString(36)}`;
}

function isValidSessionToken(token: string): boolean {
  const parts = token.split(":");
  if (parts.length !== 2) return false;

  const timestamp = parseInt(parts[0]);
  if (isNaN(timestamp)) return false;

  const age = Date.now() - timestamp;
  return age >= 0 && age < SESSION_MAX_AGE * 1000;
}

// ─── 인증 ───

/**
 * DB 기반 관리자 인증 — 초기 계정 자동 생성 포함
 */
export async function verifyAdminCredentials(id: string, password: string): Promise<boolean> {
  // DB에서 관리자 계정 확인
  let admin = await prisma.adminUser.findUnique({ where: { username: id } });

  // 계정이 없고, DB에 관리자 레코드가 하나도 없으면 초기 계정 생성
  if (!admin) {
    const count = await prisma.adminUser.count();
    if (count === 0) {
      const defaultId = process.env.ADMIN_ID || "mang84";
      const defaultPw = process.env.ADMIN_PASSWORD || "0000";
      admin = await prisma.adminUser.create({
        data: {
          username: defaultId,
          password: hashPassword(defaultPw),
        },
      });
    }
  }

  if (!admin) return false;
  if (admin.username !== id) return false;

  return verifyPassword(password, admin.password);
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
 * 어드민 인증 확인 (3가지 방식)
 */
export function verifyAdminToken(request: NextRequest): boolean {
  // 1. 세션 쿠키
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
