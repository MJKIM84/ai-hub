/**
 * 브랜드명 번역 수정 — 서비스 이름은 고유명사이므로 원문 유지
 * 실행: npx tsx scripts/fix-brand-names.ts
 */

import { PrismaClient } from "../src/generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";
import { config } from "dotenv";

config({ path: ".env.production.local" });
config({ path: ".env.local" });
config({ path: ".env" });

const connectionString = process.env.DATABASE_URL!;
const adapter = new PrismaPg({ connectionString });
const prisma = new PrismaClient({ adapter });

async function main() {
  console.log("🔧 서비스 이름을 원문으로 복원합니다...\n");

  // nameKo가 원래 name과 다른 서비스 조회
  const services = await prisma.service.findMany({
    where: { nameKo: { not: null } },
    select: { id: true, name: true, nameKo: true },
  });

  let fixed = 0;
  for (const svc of services) {
    if (svc.nameKo && svc.nameKo !== svc.name) {
      // 서비스 이름은 브랜드명이므로 원문 유지
      await prisma.service.update({
        where: { id: svc.id },
        data: { nameKo: svc.name },
      });
      console.log(`✅ "${svc.nameKo}" → "${svc.name}"`);
      fixed++;
    }
  }

  console.log(`\n📊 ${fixed}개 서비스 이름 복원 완료`);
  await prisma.$disconnect();
}

main().catch((err) => {
  console.error("Fatal:", err);
  process.exit(1);
});
