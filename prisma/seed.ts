import Database from "better-sqlite3";
import path from "path";
import { randomBytes } from "crypto";

const dbPath = path.join(__dirname, "..", "dev.db");
const db = new Database(dbPath);

function cuid() {
  return "c" + Date.now().toString(36) + randomBytes(4).toString("hex");
}

const services = [
  { slug: "chatgpt", url: "https://chat.openai.com", name: "ChatGPT", description: "OpenAI의 대화형 AI 모델. 텍스트 생성, 코드 작성, 분석 등 다양한 작업을 수행합니다.", tagline: "AI와 대화하며 모든 것을 해결하세요", category: "text-generation", tags: '["text-generation","code-assistant","productivity"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=chat.openai.com&sz=128", clicks: 1520, upvotes: 340, isKorean: 0 },
  { slug: "claude", url: "https://claude.ai", name: "Claude", description: "Anthropic의 AI 어시스턴트. 안전하고 유용한 대화형 AI로 긴 문서 분석과 코딩에 특화되어 있습니다.", tagline: "안전하고 유용한 AI 어시스턴트", category: "text-generation", tags: '["text-generation","code-assistant","writing"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=claude.ai&sz=128", clicks: 980, upvotes: 275, isKorean: 0 },
  { slug: "midjourney", url: "https://www.midjourney.com", name: "Midjourney", description: "텍스트 프롬프트로 고품질 이미지를 생성하는 AI 도구. 예술적이고 창의적인 이미지 생성에 최적화되어 있습니다.", tagline: "상상을 이미지로 만드는 AI", category: "image-generation", tags: '["image-generation"]', pricingModel: "paid", faviconUrl: "https://www.google.com/s2/favicons?domain=midjourney.com&sz=128", clicks: 870, upvotes: 210, isKorean: 0 },
  { slug: "cursor", url: "https://cursor.sh", name: "Cursor", description: "AI 기반 코드 에디터. VS Code를 기반으로 AI 자동완성과 코드 생성 기능을 제공합니다.", tagline: "AI 기반 차세대 코드 에디터", category: "code-assistant", tags: '["code-assistant","productivity"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=cursor.sh&sz=128", clicks: 1230, upvotes: 320, isKorean: 0 },
  { slug: "perplexity", url: "https://www.perplexity.ai", name: "Perplexity", description: "AI 기반 검색 엔진. 웹 검색 결과를 분석하여 정확한 답변을 제공합니다.", tagline: "AI가 찾아주는 정확한 답변", category: "text-generation", tags: '["text-generation","data-analysis"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=perplexity.ai&sz=128", clicks: 650, upvotes: 180, isKorean: 0 },
  { slug: "notion-ai", url: "https://www.notion.so/product/ai", name: "Notion AI", description: "Notion에 통합된 AI 기능. 문서 요약, 글쓰기 보조, 브레인스토밍 등을 지원합니다.", tagline: "업무 생산성을 높이는 AI", category: "productivity", tags: '["productivity","writing"]', pricingModel: "paid", faviconUrl: "https://www.google.com/s2/favicons?domain=notion.so&sz=128", clicks: 540, upvotes: 145, isKorean: 0 },
  { slug: "elevenlabs", url: "https://elevenlabs.io", name: "ElevenLabs", description: "고품질 AI 음성 합성 플랫폼. 자연스러운 음성 생성과 음성 복제를 지원합니다.", tagline: "가장 자연스러운 AI 음성", category: "voice-speech", tags: '["voice-speech"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=elevenlabs.io&sz=128", clicks: 420, upvotes: 130, isKorean: 0 },
  { slug: "runway", url: "https://runwayml.com", name: "Runway", description: "AI 기반 비디오 생성 및 편집 도구. 텍스트나 이미지에서 비디오를 생성할 수 있습니다.", tagline: "AI로 만드는 영상 제작", category: "video", tags: '["video","image-editing"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=runwayml.com&sz=128", clicks: 380, upvotes: 95, isKorean: 0 },
  { slug: "grammarly", url: "https://www.grammarly.com", name: "Grammarly", description: "AI 기반 영문 교정 도구. 문법, 맞춤법, 스타일을 자동으로 교정합니다.", tagline: "완벽한 영문 글쓰기를 위한 AI", category: "writing", tags: '["writing"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=grammarly.com&sz=128", clicks: 310, upvotes: 85, isKorean: 0 },
  { slug: "deepl", url: "https://www.deepl.com", name: "DeepL", description: "AI 기반 번역 서비스. 자연스럽고 정확한 번역을 제공하며 30개 이상의 언어를 지원합니다.", tagline: "세계에서 가장 정확한 번역기", category: "translation", tags: '["translation"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=deepl.com&sz=128", clicks: 480, upvotes: 160, isKorean: 0 },
  { slug: "github-copilot", url: "https://github.com/features/copilot", name: "GitHub Copilot", description: "AI 기반 코드 자동완성 도구. 코드 컨텍스트를 분석하여 자동으로 코드를 제안합니다.", tagline: "AI 페어 프로그래머", category: "code-assistant", tags: '["code-assistant"]', pricingModel: "paid", faviconUrl: "https://www.google.com/s2/favicons?domain=github.com&sz=128", clicks: 920, upvotes: 250, isKorean: 0 },
  { slug: "stable-diffusion", url: "https://stability.ai", name: "Stable Diffusion", description: "오픈소스 이미지 생성 AI. 텍스트 프롬프트를 기반으로 다양한 스타일의 이미지를 생성합니다.", tagline: "오픈소스 이미지 생성 AI", category: "image-generation", tags: '["image-generation"]', pricingModel: "free", faviconUrl: "https://www.google.com/s2/favicons?domain=stability.ai&sz=128", clicks: 690, upvotes: 195, isKorean: 0 },
  { slug: "wrtn", url: "https://wrtn.ai", name: "뤼튼 (Wrtn)", description: "한국의 대표적인 AI 플랫폼. 다양한 AI 도구와 서비스를 하나의 플랫폼에서 제공합니다.", tagline: "모든 AI를 하나의 플랫폼에서", category: "text-generation", tags: '["text-generation","korean-llm","productivity"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=wrtn.ai&sz=128", clicks: 780, upvotes: 230, isKorean: 1 },
  { slug: "naver-clova", url: "https://clova.ai", name: "NAVER CLOVA", description: "네이버의 AI 플랫폼. HyperCLOVA X를 기반으로 한국어에 특화된 AI 서비스를 제공합니다.", tagline: "한국어에 특화된 AI 플랫폼", category: "korean-llm", tags: '["korean-llm","text-generation","voice-speech"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=clova.ai&sz=128", clicks: 620, upvotes: 185, isKorean: 1 },
  { slug: "upstage", url: "https://www.upstage.ai", name: "Upstage", description: "Solar LLM을 개발한 한국 AI 기업. 문서 AI와 언어 모델 서비스를 제공합니다.", tagline: "한국의 AI 유니콘", category: "korean-llm", tags: '["korean-llm","text-generation","education"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=upstage.ai&sz=128", clicks: 340, upvotes: 120, isKorean: 1 },
  { slug: "riiid", url: "https://riiid.com", name: "Riiid (산타)", description: "AI 튜터 산타를 운영하는 한국 에듀테크 기업. TOEIC 등 시험 대비 AI 학습을 제공합니다.", tagline: "AI 튜터링의 선두주자", category: "education", tags: '["education","korean-llm"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=riiid.com&sz=128", clicks: 280, upvotes: 95, isKorean: 1 },
  { slug: "vuno", url: "https://www.vuno.co", name: "VUNO", description: "의료 AI 전문 기업. 영상의학, 병리학 등에서 AI 기반 진단 보조 솔루션을 제공합니다.", tagline: "AI로 더 나은 의료를 만들다", category: "healthcare", tags: '["healthcare"]', pricingModel: "paid", faviconUrl: "https://www.google.com/s2/favicons?domain=vuno.co&sz=128", clicks: 150, upvotes: 65, isKorean: 1 },
  { slug: "lunit", url: "https://www.lunit.io", name: "Lunit", description: "AI 기반 의료 영상 분석 기업. 암 진단 보조 AI 솔루션을 글로벌 시장에 제공합니다.", tagline: "AI로 암을 정복하다", category: "healthcare", tags: '["healthcare"]', pricingModel: "paid", faviconUrl: "https://www.google.com/s2/favicons?domain=lunit.io&sz=128", clicks: 180, upvotes: 72, isKorean: 1 },
  { slug: "clova-note", url: "https://clovanote.naver.com", name: "Clova Note", description: "네이버의 AI 음성 기록 서비스. 회의, 강의, 인터뷰 등을 자동으로 텍스트로 변환합니다.", tagline: "AI가 받아쓰는 음성 기록", category: "voice-speech", tags: '["voice-speech","productivity"]', pricingModel: "free", faviconUrl: "https://www.google.com/s2/favicons?domain=clovanote.naver.com&sz=128", clicks: 430, upvotes: 155, isKorean: 1 },
  { slug: "lionrocket", url: "https://lionrocket.ai", name: "LionRocket", description: "한국의 AI 이미지 생성 스타트업. K-콘텐츠에 특화된 이미지와 웹툰 생성 AI를 제공합니다.", tagline: "K-콘텐츠 생성 AI", category: "image-generation", tags: '["image-generation","korean-llm"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=lionrocket.ai&sz=128", clicks: 210, upvotes: 78, isKorean: 1 },
  { slug: "suno-ai", url: "https://suno.com", name: "Suno", description: "AI 음악 생성 플랫폼. 텍스트 프롬프트로 노래와 음악을 자동으로 작곡합니다.", tagline: "AI로 음악을 만드세요", category: "voice-speech", tags: '["voice-speech"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=suno.com&sz=128", clicks: 560, upvotes: 190, isKorean: 0 },
  { slug: "canva-ai", url: "https://www.canva.com", name: "Canva AI", description: "디자인 플랫폼 Canva의 AI 기능. 이미지 생성, 배경 제거, 디자인 자동 생성 등을 제공합니다.", tagline: "누구나 쉽게 디자인하는 AI", category: "image-editing", tags: '["image-editing","productivity"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=canva.com&sz=128", clicks: 470, upvotes: 140, isKorean: 0 },
  { slug: "gamma", url: "https://gamma.app", name: "Gamma", description: "AI 기반 프레젠테이션 생성 도구. 텍스트를 입력하면 전문적인 슬라이드를 자동으로 생성합니다.", tagline: "AI가 만드는 프레젠테이션", category: "productivity", tags: '["productivity","writing"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=gamma.app&sz=128", clicks: 350, upvotes: 110, isKorean: 0 },
  { slug: "remove-bg", url: "https://www.remove.bg", name: "Remove.bg", description: "AI 기반 이미지 배경 제거 도구. 클릭 한 번으로 이미지 배경을 자동으로 제거합니다.", tagline: "원클릭 배경 제거", category: "image-editing", tags: '["image-editing"]', pricingModel: "freemium", faviconUrl: "https://www.google.com/s2/favicons?domain=remove.bg&sz=128", clicks: 290, upvotes: 88, isKorean: 0 },
  { slug: "tableau-ai", url: "https://www.tableau.com", name: "Tableau AI", description: "데이터 시각화 플랫폼의 AI 기능. 자연어 질문으로 데이터 분석과 시각화를 수행합니다.", tagline: "AI 기반 데이터 시각화", category: "data-analysis", tags: '["data-analysis"]', pricingModel: "paid", faviconUrl: "https://www.google.com/s2/favicons?domain=tableau.com&sz=128", clicks: 220, upvotes: 70, isKorean: 0 },
];

const insert = db.prepare(`
  INSERT OR IGNORE INTO Service (id, slug, url, name, description, tagline, logoUrl, faviconUrl, ogImageUrl, category, tags, pricingModel, clicks, upvotes, score, isVerified, isKorean, submittedBy, createdAt, updatedAt)
  VALUES (?, ?, ?, ?, ?, ?, NULL, ?, NULL, ?, ?, ?, ?, ?, ?, 0, ?, NULL, ?, ?)
`);

const now = new Date();
let seeded = 0;

for (const s of services) {
  const createdAt = new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000);
  const points = s.clicks + s.upvotes * 2;
  const hoursAge = (now.getTime() - createdAt.getTime()) / (1000 * 60 * 60);
  const score = (points - 1) / Math.pow(hoursAge + 2, 1.8);

  const result = insert.run(
    cuid(), s.slug, s.url, s.name, s.description, s.tagline,
    s.faviconUrl, s.category, s.tags, s.pricingModel,
    s.clicks, s.upvotes, score, s.isKorean,
    createdAt.toISOString(), now.toISOString()
  );
  if (result.changes > 0) seeded++;
}

console.log(`Seeded ${seeded} services (${services.length - seeded} already existed).`);
db.close();
