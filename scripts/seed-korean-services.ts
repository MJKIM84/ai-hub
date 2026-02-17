/**
 * 국내 AI 서비스 일괄 등록 스크립트
 *
 * 사용법:
 *   npx tsx scripts/seed-korean-services.ts
 */

import pg from "pg";
import slugify from "slugify";
import * as dotenv from "dotenv";

dotenv.config({ path: ".env.production.local" });
if (!process.env.DATABASE_URL || process.env.DATABASE_URL.startsWith("file:")) {
  dotenv.config({ path: ".env.local", override: true });
}

function createSlug(name: string): string {
  return slugify(name, { lower: true, strict: true, trim: true });
}

const connectionString = process.env.DATABASE_URL!;
const pool = new pg.Pool({ connectionString, ssl: { rejectUnauthorized: false } });

interface ServiceSeed {
  url: string;
  name: string;
  nameKo: string;
  description: string;
  descriptionKo: string;
  category: string;
  pricingModel: "free" | "freemium" | "paid";
  tags: string[];
  isKorean: boolean;
}

const SERVICES: ServiceSeed[] = [
  // ──────────── 대화형 AI / 챗봇 ────────────
  {
    url: "https://clova-x.naver.com",
    name: "CLOVA X",
    nameKo: "클로바X",
    description: "Naver's conversational AI powered by HyperCLOVA X, optimized for Korean language understanding.",
    descriptionKo: "네이버의 HyperCLOVA X 기반 대화형 AI로 한국어 이해에 최적화되어 있습니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["네이버", "한국어 AI", "HyperCLOVA", "대화형"],
    isKorean: true,
  },
  {
    url: "https://kanana.kakao.com",
    name: "Kanana",
    nameKo: "카나나",
    description: "Kakao's AI mate service integrated with KakaoTalk, providing personalized AI assistance in conversations.",
    descriptionKo: "카카오톡과 연동되어 대화 속에서 개인 맞춤형 AI 도움을 제공하는 카카오의 AI 메이트 서비스입니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["카카오", "카카오톡", "AI 메이트", "한국어"],
    isKorean: true,
  },
  {
    url: "https://adot.ai",
    name: "A.dot (에이닷)",
    nameKo: "에이닷",
    description: "SKT's AI personal assistant with multi-LLM search, real-time notes, and everyday life assistance.",
    descriptionKo: "멀티 LLM 검색, 실시간 노트, 일상 생활 도우미를 제공하는 SKT의 AI 개인 비서입니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["SKT", "AI 비서", "검색", "일상 도우미"],
    isKorean: true,
  },
  {
    url: "https://alan.estsoft.ai",
    name: "Alan AI",
    nameKo: "앨런",
    description: "Korean AI search engine by ESTsoft comparing ChatGPT, Claude, Gemini, and EXAONE models side by side.",
    descriptionKo: "ChatGPT, Claude, Gemini, EXAONE 4개 모델을 비교할 수 있는 이스트소프트의 한국어 AI 검색엔진입니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["AI 검색", "모델 비교", "이스트소프트", "한국어"],
    isKorean: true,
  },
  {
    url: "https://zeta-ai.io",
    name: "Zeta",
    nameKo: "제타",
    description: "Social AI companion platform where users create and interact with various AI characters and stories.",
    descriptionKo: "다양한 AI 캐릭터와 대화하고 스토리를 만들 수 있는 소셜 AI 컴패니언 플랫폼입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["AI 캐릭터", "소셜", "스토리", "엔터테인먼트"],
    isKorean: true,
  },
  {
    url: "https://luda.ai",
    name: "이루다",
    nameKo: "이루다",
    description: "Korea's popular AI chatbot companion by Scatter Lab, featuring natural Korean conversation capabilities.",
    descriptionKo: "스캐터랩의 대표 AI 챗봇으로 자연스러운 한국어 대화 능력을 갖춘 AI 친구입니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["챗봇", "대화형", "스캐터랩", "AI 친구"],
    isKorean: true,
  },

  // ──────────── AI 검색 ────────────
  {
    url: "https://liner.com",
    name: "Liner",
    nameKo: "라이너",
    description: "AI search engine trusted by 13M+ users, ranking #2 globally in AI search web traffic with 95% overseas users.",
    descriptionKo: "1,300만 명 이상이 사용하는 AI 검색엔진으로, AI 검색 웹 트래픽 세계 2위입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["AI 검색", "글로벌", "리서치", "웹 검색"],
    isKorean: true,
  },

  // ──────────── 음성/노트 ────────────
  {
    url: "https://clovanote.naver.com",
    name: "CLOVA Note",
    nameKo: "클로바노트",
    description: "Naver's AI-powered meeting note service that automatically records, transcribes, and summarizes meetings in Korean.",
    descriptionKo: "회의를 자동으로 녹음, 전사, 요약하는 네이버의 AI 회의록 서비스입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["회의록", "음성 인식", "네이버", "한국어 STT"],
    isKorean: true,
  },
  {
    url: "https://daglo.ai",
    name: "Daglo",
    nameKo: "다글로",
    description: "AI meeting notes service providing automatic transcription and summarization for Korean business meetings.",
    descriptionKo: "한국어 비즈니스 회의의 자동 전사 및 요약을 제공하는 AI 회의록 서비스입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["회의록", "전사", "요약", "비즈니스"],
    isKorean: true,
  },
  {
    url: "https://tiro.ooo",
    name: "Tiro",
    nameKo: "티로",
    description: "AI note-taking service for meetings with automatic transcription and smart summarization for Korean users.",
    descriptionKo: "자동 전사 및 스마트 요약을 제공하는 AI 노트테이킹 서비스입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["노트테이킹", "전사", "요약", "회의록"],
    isKorean: true,
  },

  // ──────────── 음성 합성 / TTS ────────────
  {
    url: "https://typecast.ai",
    name: "Typecast",
    nameKo: "타입캐스트",
    description: "AI voice generator and virtual human platform offering natural-sounding Korean and multilingual TTS.",
    descriptionKo: "자연스러운 한국어 및 다국어 TTS를 제공하는 AI 음성 생성 및 가상인간 플랫폼입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["TTS", "음성 합성", "가상인간", "한국어"],
    isKorean: true,
  },

  // ──────────── AI LLM / 플랫폼 ────────────
  {
    url: "https://www.upstage.ai",
    name: "Upstage",
    nameKo: "업스테이지",
    description: "Korean AI company behind Solar LLM, recognized as a frontier model outperforming GPT-4.1 and DeepSeek V3.",
    descriptionKo: "GPT-4.1과 DeepSeek V3를 능가하는 프론티어 모델 Solar LLM을 개발한 한국 AI 기업입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["Solar LLM", "프론티어 모델", "엔터프라이즈", "한국 AI"],
    isKorean: true,
  },
  {
    url: "https://www.saltlux.com",
    name: "Saltlux",
    nameKo: "솔트룩스",
    description: "Korea's representative AI chatbot and enterprise AI platform provider with natural language processing expertise.",
    descriptionKo: "자연어 처리 전문 기술을 보유한 대한민국 대표 AI 챗봇 및 엔터프라이즈 AI 플랫폼 기업입니다.",
    category: "text-generation",
    pricingModel: "paid",
    tags: ["엔터프라이즈", "챗봇", "NLP", "한국 AI"],
    isKorean: true,
  },

  // ──────────── 교육 AI ────────────
  {
    url: "https://qanda.ai",
    name: "QANDA",
    nameKo: "콴다",
    description: "AI-powered math and study assistant used by 8M+ students monthly across 70+ countries.",
    descriptionKo: "70개 이상 국가에서 월 800만 명의 학생이 사용하는 AI 기반 수학 및 학습 어시스턴트입니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["수학", "교육", "학습", "글로벌"],
    isKorean: true,
  },
  {
    url: "https://www.milktpt.com",
    name: "밀당PT",
    nameKo: "밀당PT",
    description: "AI-based online tutoring service for middle and high school English and Math by iHateFlying Bugs.",
    descriptionKo: "아이헤이트플라잉버그스의 중고등 영어·수학 AI 온택트 과외 서비스입니다.",
    category: "education",
    pricingModel: "paid",
    tags: ["교육", "과외", "영어", "수학"],
    isKorean: true,
  },

  // ──────────── 의료 AI ────────────
  {
    url: "https://www.lunit.io",
    name: "Lunit",
    nameKo: "루닛",
    description: "World-leading medical AI company specializing in cancer detection and precision oncology solutions.",
    descriptionKo: "암 검출 및 정밀 종양학 솔루션에 특화된 세계적 의료 AI 기업입니다.",
    category: "healthcare",
    pricingModel: "paid",
    tags: ["의료 AI", "암 검출", "정밀 의료", "영상 판독"],
    isKorean: true,
  },
  {
    url: "https://www.vuno.co",
    name: "VUNO",
    nameKo: "뷰노",
    description: "Medical AI company offering FDA-approved diagnostic solutions for chest X-ray and bone age analysis.",
    descriptionKo: "흉부 엑스레이 및 골연령 분석을 위한 FDA 승인 AI 진단 솔루션을 제공하는 의료 AI 기업입니다.",
    category: "healthcare",
    pricingModel: "paid",
    tags: ["의료 AI", "FDA 승인", "영상 진단", "헬스케어"],
    isKorean: true,
  },

  // ──────────── 번역 / 데이터 ────────────
  {
    url: "https://www.flitto.com",
    name: "Flitto",
    nameKo: "플리토",
    description: "Multilingual data platform for AI and real-time AI interpretation solution, serving 170+ languages.",
    descriptionKo: "170개 이상의 언어를 지원하는 AI용 다국어 데이터 플랫폼 및 실시간 AI 통역 솔루션입니다.",
    category: "translation",
    pricingModel: "freemium",
    tags: ["번역", "다국어 데이터", "AI 통역", "실시간"],
    isKorean: true,
  },

  // ──────────── 디자인 / 크리에이티브 ────────────
  {
    url: "https://www.designovel.com",
    name: "Designovel",
    nameKo: "디자이노블",
    description: "AI fashion advisory and trend analysis platform selected by Korea's Ministry of Science and ICT.",
    descriptionKo: "과학기술정보통신부에 선정된 AI 패션 자문 및 트렌드 분석 플랫폼입니다.",
    category: "productivity",
    pricingModel: "paid",
    tags: ["패션", "트렌드 분석", "디자인", "AI 자문"],
    isKorean: true,
  },

  // ──────────── 생산성 / 비즈니스 ────────────
  {
    url: "https://callabo.ai",
    name: "Callabo",
    nameKo: "콜라보",
    description: "Korea's #1 AI meeting notes service for business with automatic recording, transcription, and summarization.",
    descriptionKo: "자동 녹음, 전사, 요약 기능을 제공하는 국내 1위 비즈니스 AI 회의록 서비스입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["회의록", "비즈니스", "전사", "요약"],
    isKorean: true,
  },
  {
    url: "https://selectstar.ai",
    name: "Select Star",
    nameKo: "셀렉트스타",
    description: "AI data ops platform providing data collection, labeling, and LLM reliability verification solutions.",
    descriptionKo: "데이터 수집, 라벨링, LLM 신뢰성 검증 솔루션을 제공하는 AI 데이터옵스 플랫폼입니다.",
    category: "data-analysis",
    pricingModel: "paid",
    tags: ["데이터 라벨링", "DataOps", "LLM", "AI 데이터"],
    isKorean: true,
  },

  // ──────────── AI 인프라 / 반도체 ────────────
  {
    url: "https://www.furiosa.ai",
    name: "FuriosaAI",
    nameKo: "퓨리오사AI",
    description: "Korean AI semiconductor startup developing high-performance NPU chips, valued at ~$1.3B after Meta acquisition offer.",
    descriptionKo: "고성능 NPU 칩을 개발하는 한국 AI 반도체 스타트업으로, 메타의 인수 제안을 받았습니다.",
    category: "data-analysis",
    pricingModel: "paid",
    tags: ["AI 반도체", "NPU", "칩셋", "인프라"],
    isKorean: true,
  },

  // ──────────── 콘텐츠 생성 ────────────
  {
    url: "https://carat.im",
    name: "Carat",
    nameKo: "캐럿",
    description: "AI content creation agent trusted by 2.6M users for generating marketing content and creative materials.",
    descriptionKo: "260만 사용자가 선택한 마케팅 콘텐츠 및 크리에이티브 자료 생성 AI 에이전트입니다.",
    category: "writing",
    pricingModel: "freemium",
    tags: ["콘텐츠 생성", "마케팅", "크리에이티브", "AI 에이전트"],
    isKorean: true,
  },

  // ──────────── 기타 유명 한국 AI ────────────
  {
    url: "https://www.returnzero.com",
    name: "Return Zero",
    nameKo: "리턴제로",
    description: "Korean AI voice technology company developing next-gen conversational voice AI and speech recognition.",
    descriptionKo: "차세대 대화형 음성 AI 및 음성 인식 기술을 개발하는 한국 AI 음성 기술 기업입니다.",
    category: "voice-speech",
    pricingModel: "paid",
    tags: ["음성 AI", "음성 인식", "STT", "대화형"],
    isKorean: true,
  },
  {
    url: "https://www.twelvelabs.io",
    name: "Twelve Labs",
    nameKo: "트웰브랩스",
    description: "Video understanding AI platform backed by NVIDIA, Intel, and Samsung, enabling semantic video search and analysis.",
    descriptionKo: "NVIDIA, 인텔, 삼성이 투자한 비디오 이해 AI 플랫폼으로, 시맨틱 비디오 검색 및 분석을 제공합니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 AI", "영상 분석", "시맨틱 검색", "비디오 이해"],
    isKorean: true,
  },
  {
    url: "https://www.makinarocks.ai",
    name: "MakinaRocks",
    nameKo: "마키나락스",
    description: "Industrial AI solution provider listed in CB Insights' Global AI 100, specializing in manufacturing optimization.",
    descriptionKo: "CB인사이트 세계 100대 AI 기업에 선정된 산업 특화 AI 솔루션 기업으로, 제조 최적화에 특화되어 있습니다.",
    category: "data-analysis",
    pricingModel: "paid",
    tags: ["산업 AI", "제조", "최적화", "CB인사이트 100"],
    isKorean: true,
  },
  {
    url: "https://www.marqvision.com",
    name: "MarqVision",
    nameKo: "마크비전",
    description: "AI-powered brand protection platform, founder selected in Forbes '33 Best AI Founders to Watch 2025'.",
    descriptionKo: "AI 기반 브랜드 보호 플랫폼으로, 대표가 포브스 '2025 주목해야 할 AI 창업자 33인'에 선정됐습니다.",
    category: "productivity",
    pricingModel: "paid",
    tags: ["브랜드 보호", "지적 재산", "AI 탐지", "포브스"],
    isKorean: true,
  },
  {
    url: "https://nuvilab.com",
    name: "Nuvilab",
    nameKo: "누비랩",
    description: "AI food scanner developer selected by Korea's MSIT for global expansion support program.",
    descriptionKo: "과학기술정보통신부 글로벌 진출 지원 프로그램에 선정된 AI 푸드 스캐너 개발 기업입니다.",
    category: "healthcare",
    pricingModel: "paid",
    tags: ["푸드 스캐너", "식품 AI", "건강", "분석"],
    isKorean: true,
  },
  {
    url: "https://www.rebellions.ai",
    name: "Rebellions",
    nameKo: "리벨리온",
    description: "AI chip company merged with SK's Sapeon, creating a ~$1.3T won valued AI semiconductor powerhouse.",
    descriptionKo: "SK 사피온과 합병하여 기업가치 약 1.3조 원의 AI 반도체 기업으로 재탄생했습니다.",
    category: "data-analysis",
    pricingModel: "paid",
    tags: ["AI 칩", "반도체", "SK", "NPU"],
    isKorean: true,
  },
];

async function main() {
  console.log(`📦 한국 AI 서비스 ${SERVICES.length}개 등록 시작...\n`);

  const client = await pool.connect();
  try {
    await client.query("SELECT 1 as test");
    console.log("✅ DB 연결 성공\n");
  } catch (e) {
    console.error("❌ DB 연결 실패:", e);
    client.release();
    return;
  }

  let created = 0;
  let updated = 0;
  let skipped = 0;
  let errors = 0;

  for (const svc of SERVICES) {
    try {
      const existing = await client.query(
        `SELECT id, "nameKo", "descriptionKo"
         FROM "Service"
         WHERE url = $1 OR url = $2 OR url = $3 OR name = $4
         LIMIT 1`,
        [svc.url, svc.url.replace(/\/$/, ""), svc.url + "/", svc.name]
      );

      if (existing.rows.length > 0) {
        const ex = existing.rows[0];
        if ((svc.nameKo && !ex.nameKo) || (svc.descriptionKo && !ex.descriptionKo) || !ex.nameKo) {
          await client.query(
            `UPDATE "Service"
             SET "nameKo" = COALESCE($1, "nameKo"),
                 "descriptionKo" = COALESCE($2, "descriptionKo"),
                 "isKorean" = true
             WHERE id = $3`,
            [svc.nameKo, svc.descriptionKo, ex.id]
          );
          console.log(`  ✏️  [업데이트] ${svc.nameKo} (${svc.name}) — 한국어 정보 추가`);
          updated++;
        } else {
          console.log(`  ⏭️  [건너뜀] ${svc.nameKo} (${svc.name}) — 이미 등록됨`);
          skipped++;
        }
        continue;
      }

      const slug = createSlug(svc.name);
      const slugCheck = await client.query(
        `SELECT id FROM "Service" WHERE slug = $1 LIMIT 1`,
        [slug]
      );
      const finalSlug = slugCheck.rows.length > 0 ? `${slug}-${Date.now()}` : slug;
      const domain = new URL(svc.url).hostname;
      const id = `cuid_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;

      await client.query(
        `INSERT INTO "Service" (
          id, slug, url, name, "nameKo", description, "descriptionKo",
          tagline, category, "pricingModel", tags, "isKorean",
          "logoUrl", "faviconUrl", "ogImageUrl", source, score,
          clicks, upvotes, downvotes, "isVerified",
          "createdAt", "updatedAt"
        ) VALUES (
          $1, $2, $3, $4, $5, $6, $7,
          $8, $9, $10, $11, $12,
          $13, $14, $15, $16, $17,
          $18, $19, $20, $21,
          NOW(), NOW()
        )`,
        [
          id, finalSlug, svc.url, svc.name, svc.nameKo,
          svc.description, svc.descriptionKo,
          null, svc.category, svc.pricingModel,
          JSON.stringify(svc.tags), svc.isKorean,
          null,
          `https://www.google.com/s2/favicons?domain=${domain}&sz=128`,
          null, "auto", 0.5,
          0, 0, 0, false,
        ]
      );

      console.log(`  ✅ [등록] ${svc.nameKo} (${svc.name}) — ${svc.category}`);
      created++;
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      if (message.includes("unique") || message.includes("duplicate")) {
        console.log(`  ⏭️  [건너뜀] ${svc.nameKo} — unique constraint`);
        skipped++;
      } else {
        console.error(`  ❌ [에러] ${svc.nameKo}: ${message}`);
        errors++;
      }
    }
  }

  console.log(`\n✨ 완료!`);
  console.log(`   ✅ 신규 등록: ${created}개`);
  console.log(`   ✏️  업데이트: ${updated}개`);
  console.log(`   ⏭️  건너뜀: ${skipped}개`);
  console.log(`   ❌ 에러: ${errors}개`);

  client.release();
  await pool.end();
}

main().catch((e) => {
  console.error(e);
  pool.end();
  process.exit(1);
});
