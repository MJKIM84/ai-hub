/**
 * 기존 영어 서비스 일괄 번역 스크립트
 * 실행: npx tsx scripts/batch-translate.ts
 */

import { PrismaClient } from "../src/generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";
import { config } from "dotenv";

// production env 우선 로드
config({ path: ".env.production.local" });
config({ path: ".env.local" });
config({ path: ".env" });

const connectionString = process.env.DATABASE_URL!;
if (!connectionString) {
  console.error("❌ DATABASE_URL 환경변수가 없습니다.");
  process.exit(1);
}

const adapter = new PrismaPg({ connectionString });
const prisma = new PrismaClient({ adapter });

function isEnglishText(text: string): boolean {
  const latinChars = text.replace(/[\s\d\p{P}\p{S}]/gu, "");
  if (latinChars.length === 0) return false;
  const latinCount = (latinChars.match(/[a-zA-Z]/g) || []).length;
  return latinCount / latinChars.length > 0.7;
}

async function translateToKorean(text: string): Promise<string | null> {
  try {
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ko&dt=t&q=${encodeURIComponent(text)}`;
    const res = await fetch(url);
    if (!res.ok) return null;
    const data = await res.json();
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const translated = data[0]?.map((s: any) => s[0]).join("") || null;
    return translated;
  } catch {
    return null;
  }
}

async function main() {
  console.log("🔄 기존 영어 서비스 일괄 번역 시작...\n");

  const services = await prisma.service.findMany({
    where: { nameKo: null },
    select: { id: true, name: true, description: true },
  });

  console.log(`📋 번역 대상: ${services.length}개 서비스\n`);

  let translated = 0;
  let skipped = 0;
  const errors: string[] = [];

  for (const svc of services) {
    try {
      let nameKo: string | null = null;
      let descriptionKo: string | null = null;

      // 이름 번역 (영어인 경우만)
      if (isEnglishText(svc.name)) {
        nameKo = await translateToKorean(svc.name);
      }

      // 설명 번역 (영어인 경우만)
      if (svc.description && isEnglishText(svc.description)) {
        descriptionKo = await translateToKorean(svc.description);
      }

      if (nameKo || descriptionKo) {
        await prisma.service.update({
          where: { id: svc.id },
          data: {
            nameKo: nameKo || svc.name,
            descriptionKo: descriptionKo || svc.description,
          },
        });
        translated++;
        console.log(`✅ ${svc.name} → ${nameKo || "(한국어)"}`);
      } else {
        // 이미 한국어이거나 번역 불필요
        await prisma.service.update({
          where: { id: svc.id },
          data: {
            nameKo: svc.name,
            descriptionKo: svc.description,
          },
        });
        skipped++;
        console.log(`⏭️ ${svc.name} (이미 한국어)`);
      }

      // Rate limit 방지
      await new Promise((r) => setTimeout(r, 300));
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      errors.push(`${svc.name}: ${msg}`);
      console.error(`❌ ${svc.name}: ${msg}`);
    }
  }

  console.log(`\n📊 결과:`);
  console.log(`  번역됨: ${translated}개`);
  console.log(`  스킵됨: ${skipped}개`);
  console.log(`  에러: ${errors.length}개`);

  if (errors.length > 0) {
    console.log(`\n에러 목록:`);
    errors.forEach((e) => console.log(`  - ${e}`));
  }

  await prisma.$disconnect();
}

main().catch((err) => {
  console.error("Fatal:", err);
  process.exit(1);
});
