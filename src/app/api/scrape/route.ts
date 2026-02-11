import { NextRequest, NextResponse } from "next/server";
import { scrapeServiceMetadata } from "@/lib/scraper";
import { scrapeRequestSchema } from "@/lib/validators";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { url } = scrapeRequestSchema.parse(body);

    const data = await scrapeServiceMetadata(url);

    return NextResponse.json(data);
  } catch (error) {
    console.error("POST /api/scrape error:", error);

    if (error instanceof Error) {
      if (error.name === "ZodError") {
        return NextResponse.json(
          { error: "올바른 URL을 입력해주세요" },
          { status: 400 }
        );
      }
      if (error.message.includes("Failed to fetch")) {
        return NextResponse.json(
          { error: "해당 URL에 접근할 수 없습니다" },
          { status: 422 }
        );
      }
    }

    return NextResponse.json(
      { error: "URL을 분석할 수 없습니다" },
      { status: 500 }
    );
  }
}
