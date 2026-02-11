import { NextRequest, NextResponse } from "next/server";
import { verifyAdminToken } from "@/lib/admin";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  const isAuthenticated = verifyAdminToken(request);
  return NextResponse.json({ authenticated: isAuthenticated });
}
