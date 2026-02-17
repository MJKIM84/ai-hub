import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { sendSlackMessage } from "@/lib/slack";

export const dynamic = "force-dynamic";
export const maxDuration = 60;

export async function GET(request: NextRequest) {
  try {
    // CRON_SECRET 인증
    const authHeader = request.headers.get("authorization");
    const cronSecret = process.env.CRON_SECRET;

    if (!cronSecret || authHeader !== `Bearer ${cronSecret}`) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const results: string[] = [];

    // 1. 이름에 " | " 포함된 서비스 정리 (파이프 앞부분만 유지)
    const pipeServices = await prisma.service.findMany({
      where: {
        name: { contains: " | " },
      },
      select: { id: true, name: true },
    });

    for (const s of pipeServices) {
      const cleanName = s.name.split(" | ")[0].split(" — ")[0].trim();
      if (cleanName !== s.name && cleanName.length > 2) {
        await prisma.service.update({
          where: { id: s.id },
          data: { name: cleanName },
        });
        results.push(`이름 수정: "${s.name.substring(0, 40)}" → "${cleanName}"`);
      }
    }

    // 2. GitHub "GitHub -" 서비스 — 스타 100개 이상은 이름만 정리, 미만은 삭제
    const githubServices = await prisma.service.findMany({
      where: {
        name: { startsWith: "GitHub -" },
      },
      select: { id: true, name: true, url: true },
    });

    for (const s of githubServices) {
      // GitHub API로 스타 수 확인
      const repoMatch = s.url.match(/github\.com\/([^/]+\/[^/]+)/);
      let stars = 0;
      if (repoMatch) {
        try {
          const ghRes = await fetch(`https://api.github.com/repos/${repoMatch[1]}`, {
            headers: { "User-Agent": "AI-Hub-Bot/1.0" },
            signal: AbortSignal.timeout(5000),
          });
          if (ghRes.ok) {
            const ghData = await ghRes.json();
            stars = ghData.stargazers_count || 0;
          }
        } catch {
          // API 실패 시 삭제
        }
      }

      if (stars >= 100) {
        // 이름 정리 (레포명만 추출)
        const repoName = repoMatch ? repoMatch[1].split("/")[1] : s.name;
        const cleanName = repoName.charAt(0).toUpperCase() + repoName.slice(1);
        await prisma.service.update({
          where: { id: s.id },
          data: { name: cleanName },
        });
        results.push(`이름 정리 (⭐${stars}): "${s.name.substring(0, 40)}" → "${cleanName}"`);
      } else {
        await prisma.service.delete({ where: { id: s.id } });
        results.push(`삭제 (⭐${stars}): ${s.name.substring(0, 50)}`);
      }

      // Rate limit
      await new Promise((r) => setTimeout(r, 300));
    }

    // 3. 디렉토리/랭킹 사이트 삭제
    const directoryKeywords = ["AI Revenue Ranking", "Top Earning AI Tools"];
    for (const keyword of directoryKeywords) {
      const dirServices = await prisma.service.findMany({
        where: { name: { contains: keyword } },
        select: { id: true, name: true },
      });
      for (const s of dirServices) {
        await prisma.service.delete({ where: { id: s.id } });
        results.push(`삭제 (디렉토리): ${s.name.substring(0, 50)}`);
      }
    }

    // 4. 블로그 포스트 URL (/blob/) 삭제
    const blogServices = await prisma.service.findMany({
      where: {
        url: { contains: "/blob/" },
      },
      select: { id: true, name: true, url: true },
    });

    for (const s of blogServices) {
      await prisma.service.delete({ where: { id: s.id } });
      results.push(`삭제 (블로그): ${s.name.substring(0, 50)}`);
    }

    // 5. 설명 없는 서비스에 설명 추가 시도
    const noDescServices = await prisma.service.findMany({
      where: {
        description: null,
        source: "auto",
      },
      select: { id: true, name: true, url: true },
    });

    for (const s of noDescServices) {
      try {
        const res = await fetch(s.url, {
          headers: { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" },
          redirect: "follow",
          signal: AbortSignal.timeout(5000),
        });
        if (res.ok) {
          const html = await res.text();
          const descMatch = html.match(/<meta\s+(?:name|property)=["'](?:description|og:description)["']\s+content=["']([^"']+)["']/i)
            || html.match(/content=["']([^"']+)["']\s+(?:name|property)=["'](?:description|og:description)["']/i);
          if (descMatch && descMatch[1].length > 10) {
            await prisma.service.update({
              where: { id: s.id },
              data: { description: descMatch[1].substring(0, 500) },
            });
            results.push(`설명 추가: ${s.name} → "${descMatch[1].substring(0, 40)}..."`);
          } else {
            // meta description 없으면 <h1> + <h2> 조합으로 설명 생성
            const h1Match = html.match(/<h1[^>]*>([^<]+)<\/h1>/i);
            const h2Match = html.match(/<h2[^>]*>([^<]+)<\/h2>/i);
            if (h1Match) {
              const fallbackDesc = h2Match
                ? `${h1Match[1].trim()}. ${h2Match[1].trim()}`
                : h1Match[1].trim();
              if (fallbackDesc.length > 10) {
                await prisma.service.update({
                  where: { id: s.id },
                  data: { description: fallbackDesc.substring(0, 500) },
                });
                results.push(`설명 추가 (h1): ${s.name} → "${fallbackDesc.substring(0, 40)}..."`);
              }
            }
          }
        }
      } catch {
        // 실패 시 무시
      }
      await new Promise((r) => setTimeout(r, 300));
    }

    // Slack 알림
    if (results.length > 0) {
      await sendSlackMessage({
        text: `🧹 데이터 정리 완료: ${results.length}건 처리\n${results.join("\n")}`,
      });
    }

    return NextResponse.json({
      success: true,
      actionsPerformed: results.length,
      details: results,
    });
  } catch (error) {
    console.error("[Cleanup] Error:", error);
    return NextResponse.json(
      { error: "정리 중 오류 발생" },
      { status: 500 }
    );
  }
}
