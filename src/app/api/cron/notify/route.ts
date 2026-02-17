import { NextRequest, NextResponse } from "next/server";
import { sendSlackMessage } from "@/lib/slack";

export const dynamic = "force-dynamic";

export async function POST(request: NextRequest) {
  try {
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const { message } = await request.json();
    if (!message) {
      return NextResponse.json({ error: "message required" }, { status: 400 });
    }

    const sent = await sendSlackMessage({ text: message });

    return NextResponse.json({ success: sent });
  } catch (error) {
    console.error("[Notify] Error:", error);
    return NextResponse.json({ error: "Failed" }, { status: 500 });
  }
}
