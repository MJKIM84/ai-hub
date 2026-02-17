/**
 * 인기 AI 서비스 일괄 등록 스크립트
 *
 * 사용법:
 *   npx tsx scripts/seed-popular-services.ts
 *
 * 환경변수:
 *   API_URL - API 엔드포인트 (기본: http://localhost:3000)
 *   또는 직접 DB에 접근하여 등록
 */

import pg from "pg";
import slugify from "slugify";
import * as dotenv from "dotenv";

// 프로덕션 DB에 연결 (.env.production.local 또는 .env.local)
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
  nameKo?: string;
  description: string;
  descriptionKo?: string;
  tagline?: string;
  category: string;
  pricingModel: "free" | "freemium" | "paid";
  tags: string[];
  isKorean?: boolean;
  logoUrl?: string;
  faviconUrl?: string;
}

// ============================================================
// 유명 AI 서비스 목록 — 카테고리별로 정리
// ============================================================
const SERVICES: ServiceSeed[] = [
  // ──────────── 텍스트 생성 (text-generation) ────────────
  {
    url: "https://chat.openai.com",
    name: "ChatGPT",
    nameKo: "챗GPT",
    description: "OpenAI's AI chatbot powered by GPT-4o, capable of text generation, analysis, coding, and multimodal interactions.",
    descriptionKo: "OpenAI의 AI 챗봇으로 GPT-4o 기반의 텍스트 생성, 분석, 코딩, 멀티모달 대화를 지원합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["chatbot", "GPT-4", "OpenAI", "대화형 AI"],
  },
  {
    url: "https://claude.ai",
    name: "Claude",
    nameKo: "클로드",
    description: "Anthropic's AI assistant known for safety, helpfulness, and long-context understanding.",
    descriptionKo: "Anthropic의 AI 어시스턴트로 안전성, 유용성, 긴 문맥 이해 능력이 뛰어납니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["chatbot", "Anthropic", "Claude", "안전한 AI"],
  },
  {
    url: "https://gemini.google.com",
    name: "Google Gemini",
    nameKo: "구글 제미나이",
    description: "Google's multimodal AI model with search integration, code generation, and image understanding.",
    descriptionKo: "구글의 멀티모달 AI 모델로 검색 통합, 코드 생성, 이미지 이해 기능을 제공합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["Google", "멀티모달", "검색", "Gemini"],
  },
  {
    url: "https://www.perplexity.ai",
    name: "Perplexity AI",
    nameKo: "퍼플렉시티",
    description: "AI-powered search engine that provides direct, cited answers to complex questions.",
    descriptionKo: "복잡한 질문에 출처가 포함된 직접적인 답변을 제공하는 AI 기반 검색 엔진입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["AI 검색", "research", "출처 기반", "답변"],
  },
  {
    url: "https://copilot.microsoft.com",
    name: "Microsoft Copilot",
    nameKo: "마이크로소프트 코파일럿",
    description: "Microsoft's AI companion integrated with Bing search, Office apps, and Windows.",
    descriptionKo: "Bing 검색, Office, Windows와 통합된 마이크로소프트의 AI 어시스턴트입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["Microsoft", "Bing", "Office", "Windows"],
  },
  {
    url: "https://grok.com",
    name: "Grok",
    nameKo: "그록",
    description: "xAI's conversational AI with real-time X/Twitter data access and witty personality.",
    descriptionKo: "실시간 X/트위터 데이터 접근과 위트있는 성격을 가진 xAI의 대화형 AI입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["xAI", "Elon Musk", "실시간", "트위터"],
  },
  {
    url: "https://deepseek.com",
    name: "DeepSeek",
    nameKo: "딥시크",
    description: "Chinese AI lab offering powerful open-source language models with strong reasoning capabilities.",
    descriptionKo: "강력한 추론 능력을 갖춘 오픈소스 언어 모델을 제공하는 중국 AI 연구소입니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["오픈소스", "중국 AI", "추론", "DeepSeek-R1"],
  },
  {
    url: "https://chat.mistral.ai",
    name: "Mistral AI",
    nameKo: "미스트랄",
    description: "European AI company offering efficient, open-weight language models with multilingual support.",
    descriptionKo: "다국어 지원이 뛰어난 효율적인 오픈 가중치 언어 모델을 제공하는 유럽 AI 기업입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["오픈소스", "유럽 AI", "다국어", "효율적"],
  },
  {
    url: "https://poe.com",
    name: "Poe",
    nameKo: "포",
    description: "Platform by Quora offering access to multiple AI models including GPT-4, Claude, and custom bots.",
    descriptionKo: "GPT-4, Claude 등 여러 AI 모델에 접근할 수 있는 Quora의 AI 플랫폼입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["멀티모델", "Quora", "봇 생성", "AI 플랫폼"],
  },
  {
    url: "https://character.ai",
    name: "Character.AI",
    nameKo: "캐릭터AI",
    description: "Create and chat with AI characters with unique personalities and knowledge.",
    descriptionKo: "고유한 성격과 지식을 가진 AI 캐릭터를 만들고 대화할 수 있는 서비스입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["캐릭터", "롤플레이", "대화", "엔터테인먼트"],
  },

  // ──────────── 이미지 생성 (image-generation) ────────────
  {
    url: "https://www.midjourney.com",
    name: "Midjourney",
    nameKo: "미드저니",
    description: "Leading AI image generator known for artistic, photorealistic outputs via Discord and web interface.",
    descriptionKo: "예술적이고 사실적인 이미지를 생성하는 최고의 AI 이미지 생성기입니다.",
    category: "image-generation",
    pricingModel: "paid",
    tags: ["이미지 생성", "아트", "Discord", "포토리얼"],
  },
  {
    url: "https://openai.com/dall-e-3",
    name: "DALL-E 3",
    nameKo: "달리 3",
    description: "OpenAI's text-to-image model with precise prompt following and high-quality output.",
    descriptionKo: "정확한 프롬프트 반영과 고품질 출력을 제공하는 OpenAI의 텍스트-이미지 생성 모델입니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["OpenAI", "텍스트to이미지", "DALL-E", "이미지 생성"],
  },
  {
    url: "https://stability.ai",
    name: "Stable Diffusion",
    nameKo: "스테이블 디퓨전",
    description: "Open-source AI image generation model by Stability AI, widely used for local and cloud deployment.",
    descriptionKo: "Stability AI의 오픈소스 이미지 생성 모델로 로컬 및 클라우드 배포에 널리 사용됩니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["오픈소스", "이미지 생성", "로컬 실행", "Stable Diffusion"],
  },
  {
    url: "https://ideogram.ai",
    name: "Ideogram",
    nameKo: "아이디오그램",
    description: "AI image generator known for exceptional text rendering within images and creative typography.",
    descriptionKo: "이미지 내 텍스트 렌더링과 창의적 타이포그래피에 뛰어난 AI 이미지 생성기입니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["텍스트 렌더링", "타이포그래피", "이미지 생성", "디자인"],
  },
  {
    url: "https://www.flux1.ai",
    name: "Flux",
    nameKo: "플럭스",
    description: "Fast, high-quality AI image generation model by Black Forest Labs with open-source options.",
    descriptionKo: "Black Forest Labs의 빠르고 고품질 AI 이미지 생성 모델로 오픈소스 옵션도 제공합니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["이미지 생성", "빠른 생성", "오픈소스", "고품질"],
  },
  {
    url: "https://leonardo.ai",
    name: "Leonardo AI",
    nameKo: "레오나르도 AI",
    description: "AI-powered creative platform for generating and editing game assets, art, and design elements.",
    descriptionKo: "게임 에셋, 아트, 디자인 요소를 생성하고 편집하는 AI 크리에이티브 플랫폼입니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["게임 에셋", "디자인", "아트", "크리에이티브"],
  },

  // ──────────── 이미지 편집 (image-editing) ────────────
  {
    url: "https://www.canva.com",
    name: "Canva",
    nameKo: "캔바",
    description: "All-in-one design platform with AI-powered image editing, templates, and graphic design tools.",
    descriptionKo: "AI 기반 이미지 편집, 템플릿, 그래픽 디자인 도구를 제공하는 올인원 디자인 플랫폼입니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["디자인", "템플릿", "그래픽", "편집"],
  },
  {
    url: "https://www.adobe.com/products/firefly.html",
    name: "Adobe Firefly",
    nameKo: "어도비 파이어플라이",
    description: "Adobe's generative AI for image creation, editing, and creative design within Adobe ecosystem.",
    descriptionKo: "Adobe 생태계에서 이미지 생성, 편집, 크리에이티브 디자인을 지원하는 생성형 AI입니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["Adobe", "이미지 편집", "생성형 AI", "포토샵"],
  },
  {
    url: "https://clipdrop.co",
    name: "Clipdrop",
    nameKo: "클립드롭",
    description: "AI-powered image editing tools including background removal, upscaling, and object removal.",
    descriptionKo: "배경 제거, 업스케일링, 객체 제거 등 AI 기반 이미지 편집 도구 모음입니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["배경 제거", "업스케일링", "이미지 편집", "객체 제거"],
  },
  {
    url: "https://remove.bg",
    name: "remove.bg",
    nameKo: "리무브비지",
    description: "Automatic AI-powered background removal for images in seconds.",
    descriptionKo: "몇 초 만에 이미지 배경을 자동으로 제거하는 AI 서비스입니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["배경 제거", "자동", "이미지", "편집"],
  },

  // ──────────── 코드 어시스턴트 (code-assistant) ────────────
  {
    url: "https://github.com/features/copilot",
    name: "GitHub Copilot",
    nameKo: "깃허브 코파일럿",
    description: "AI pair programmer powered by OpenAI Codex, providing code suggestions in your IDE.",
    descriptionKo: "IDE에서 코드 제안을 제공하는 OpenAI Codex 기반의 AI 페어 프로그래머입니다.",
    category: "code-assistant",
    pricingModel: "paid",
    tags: ["코딩", "GitHub", "IDE", "코드 완성"],
  },
  {
    url: "https://cursor.com",
    name: "Cursor",
    nameKo: "커서",
    description: "AI-first code editor built on VS Code with intelligent code completion, editing, and chat.",
    descriptionKo: "VS Code 기반의 AI 우선 코드 에디터로 지능형 코드 완성, 편집, 채팅 기능을 제공합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["코드 에디터", "VS Code", "AI 코딩", "코드 완성"],
  },
  {
    url: "https://www.tabnine.com",
    name: "Tabnine",
    nameKo: "탭나인",
    description: "AI code assistant with privacy-focused, enterprise-ready code completion for all major IDEs.",
    descriptionKo: "프라이버시 중심의 엔터프라이즈급 AI 코드 완성 도구로 모든 주요 IDE를 지원합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["코드 완성", "프라이버시", "엔터프라이즈", "IDE"],
  },
  {
    url: "https://codeium.com",
    name: "Codeium",
    nameKo: "코디움",
    description: "Free AI code completion and search tool supporting 70+ languages in major IDEs.",
    descriptionKo: "70개 이상의 언어를 지원하는 무료 AI 코드 완성 및 검색 도구입니다.",
    category: "code-assistant",
    pricingModel: "free",
    tags: ["코드 완성", "무료", "다국어", "IDE"],
  },
  {
    url: "https://replit.com",
    name: "Replit",
    nameKo: "리플릿",
    description: "Online IDE with AI assistant for building, deploying, and collaborating on software projects.",
    descriptionKo: "소프트웨어 프로젝트를 빌드, 배포, 협업할 수 있는 AI 어시스턴트가 포함된 온라인 IDE입니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["온라인 IDE", "배포", "협업", "AI 코딩"],
  },
  {
    url: "https://v0.dev",
    name: "v0 by Vercel",
    nameKo: "v0",
    description: "AI-powered UI component generator by Vercel using shadcn/ui and Tailwind CSS.",
    descriptionKo: "shadcn/ui와 Tailwind CSS를 사용하는 Vercel의 AI 기반 UI 컴포넌트 생성기입니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["UI 생성", "React", "Vercel", "프론트엔드"],
  },
  {
    url: "https://bolt.new",
    name: "Bolt.new",
    nameKo: "볼트",
    description: "AI-powered full-stack web app builder that generates and deploys apps from natural language.",
    descriptionKo: "자연어로 풀스택 웹 앱을 생성하고 배포하는 AI 기반 앱 빌더입니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["풀스택", "앱 빌더", "배포", "노코드"],
  },
  {
    url: "https://lovable.dev",
    name: "Lovable",
    nameKo: "러버블",
    description: "AI-powered full-stack app builder that turns natural language into production-ready applications.",
    descriptionKo: "자연어를 프로덕션 수준의 앱으로 변환하는 AI 기반 풀스택 앱 빌더입니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["앱 빌더", "풀스택", "프로덕션", "AI 개발"],
  },

  // ──────────── 비디오 (video) ────────────
  {
    url: "https://openai.com/sora",
    name: "Sora",
    nameKo: "소라",
    description: "OpenAI's text-to-video AI model generating realistic and creative videos from text descriptions.",
    descriptionKo: "텍스트 설명에서 사실적이고 창의적인 비디오를 생성하는 OpenAI의 텍스트-비디오 AI 모델입니다.",
    category: "video",
    pricingModel: "paid",
    tags: ["비디오 생성", "OpenAI", "텍스트to비디오", "소라"],
  },
  {
    url: "https://runwayml.com",
    name: "Runway",
    nameKo: "런웨이",
    description: "AI-powered video creation and editing platform with Gen-3 Alpha for text/image-to-video.",
    descriptionKo: "Gen-3 Alpha를 통한 텍스트/이미지-비디오 변환을 지원하는 AI 비디오 생성 및 편집 플랫폼입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 생성", "편집", "Gen-3", "크리에이티브"],
  },
  {
    url: "https://pika.art",
    name: "Pika",
    nameKo: "피카",
    description: "AI video generation platform creating short videos from text and image prompts.",
    descriptionKo: "텍스트와 이미지 프롬프트에서 짧은 비디오를 생성하는 AI 비디오 생성 플랫폼입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 생성", "짧은 영상", "프롬프트", "크리에이티브"],
  },
  {
    url: "https://www.hedra.com",
    name: "Hedra",
    nameKo: "헤드라",
    description: "AI avatar video generator creating talking head videos from audio and a single photo.",
    descriptionKo: "오디오와 사진 한 장으로 토킹 헤드 비디오를 생성하는 AI 아바타 비디오 생성기입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["아바타", "토킹 헤드", "비디오 생성", "립싱크"],
  },
  {
    url: "https://www.capcut.com",
    name: "CapCut",
    nameKo: "캡컷",
    description: "Free video editor by ByteDance with AI-powered editing, captions, and effects.",
    descriptionKo: "AI 기반 편집, 자막, 효과를 제공하는 ByteDance의 무료 비디오 편집기입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 편집", "자막", "ByteDance", "무료"],
  },
  {
    url: "https://www.descript.com",
    name: "Descript",
    nameKo: "디스크립트",
    description: "AI video/audio editor that lets you edit media by editing text transcript.",
    descriptionKo: "텍스트 트랜스크립트를 편집하여 미디어를 편집할 수 있는 AI 비디오/오디오 편집기입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 편집", "오디오 편집", "트랜스크립트", "팟캐스트"],
  },
  {
    url: "https://hailuoai.video",
    name: "Hailuo AI",
    nameKo: "하이루오",
    description: "MiniMax's AI video generator creating high-quality videos with natural motion and coherent scenes.",
    descriptionKo: "자연스러운 동작과 일관된 장면으로 고품질 비디오를 생성하는 MiniMax의 AI 비디오 생성기입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 생성", "MiniMax", "고품질", "자연스러운 동작"],
  },
  {
    url: "https://klingai.com",
    name: "Kling AI",
    nameKo: "클링",
    description: "Kuaishou's AI video generation model with impressive motion quality and lip sync capabilities.",
    descriptionKo: "뛰어난 동작 품질과 립싱크 기능을 갖춘 콰이쇼우의 AI 비디오 생성 모델입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 생성", "립싱크", "동작", "Kuaishou"],
  },
  {
    url: "https://www.seedance.ai",
    name: "Seedance",
    nameKo: "시댄스",
    description: "ByteDance's AI video and dance generation model for creating dynamic, choreographed video content.",
    descriptionKo: "역동적인 안무 비디오 콘텐츠를 생성하는 ByteDance의 AI 비디오 및 댄스 생성 모델입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 생성", "댄스", "ByteDance", "안무"],
  },
  {
    url: "https://www.veed.io",
    name: "VEED.io",
    nameKo: "비드",
    description: "Online video editor with AI subtitles, translations, avatars, and screen recording.",
    descriptionKo: "AI 자막, 번역, 아바타, 화면 녹화 기능을 갖춘 온라인 비디오 편집기입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 편집", "자막", "번역", "온라인"],
  },
  {
    url: "https://luma.ai",
    name: "Luma AI",
    nameKo: "루마 AI",
    description: "AI-powered 3D capture and video generation platform using Dream Machine technology.",
    descriptionKo: "Dream Machine 기술을 사용하는 AI 기반 3D 캡처 및 비디오 생성 플랫폼입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["3D", "비디오 생성", "Dream Machine", "3D 캡처"],
  },

  // ──────────── 음성/스피치 (voice-speech) ────────────
  {
    url: "https://elevenlabs.io",
    name: "ElevenLabs",
    nameKo: "일레븐랩스",
    description: "Industry-leading AI voice synthesis platform with natural-sounding text-to-speech and voice cloning.",
    descriptionKo: "자연스러운 텍스트-음성 변환과 음성 클로닝을 제공하는 업계 최고의 AI 음성 합성 플랫폼입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["TTS", "음성 합성", "음성 클로닝", "자연스러운"],
  },
  {
    url: "https://murf.ai",
    name: "Murf AI",
    nameKo: "머프 AI",
    description: "AI voiceover platform with 120+ realistic voices in 20+ languages for professional content.",
    descriptionKo: "전문 콘텐츠를 위한 20개 이상 언어의 120개 이상 리얼한 목소리를 제공하는 AI 보이스오버 플랫폼입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["보이스오버", "TTS", "다국어", "전문 콘텐츠"],
  },
  {
    url: "https://www.assemblyai.com",
    name: "AssemblyAI",
    nameKo: "어셈블리AI",
    description: "AI-powered speech-to-text API with speaker diarization, sentiment analysis, and summarization.",
    descriptionKo: "화자 분리, 감정 분석, 요약 기능이 포함된 AI 기반 음성-텍스트 변환 API입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["STT", "음성 인식", "API", "화자 분리"],
  },
  {
    url: "https://otter.ai",
    name: "Otter.ai",
    nameKo: "오터",
    description: "AI meeting assistant that records, transcribes, and summarizes meetings in real-time.",
    descriptionKo: "실시간으로 회의를 녹음, 전사, 요약하는 AI 미팅 어시스턴트입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["회의 녹음", "전사", "요약", "실시간"],
  },
  {
    url: "https://suno.com",
    name: "Suno",
    nameKo: "수노",
    description: "AI music generation platform that creates complete songs with vocals from text prompts.",
    descriptionKo: "텍스트 프롬프트에서 보컬이 포함된 완전한 노래를 생성하는 AI 음악 생성 플랫폼입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["음악 생성", "AI 음악", "보컬", "작곡"],
  },
  {
    url: "https://www.udio.com",
    name: "Udio",
    nameKo: "유디오",
    description: "AI music creation tool generating high-quality, diverse music from text descriptions.",
    descriptionKo: "텍스트 설명에서 고품질의 다양한 음악을 생성하는 AI 음악 제작 도구입니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["음악 생성", "AI 음악", "다양한 장르", "텍스트to음악"],
  },

  // ──────────── 생산성 도구 (productivity) ────────────
  {
    url: "https://notion.so",
    name: "Notion AI",
    nameKo: "노션 AI",
    description: "AI assistant integrated into Notion workspace for writing, summarizing, and organizing information.",
    descriptionKo: "글쓰기, 요약, 정보 정리를 위해 Notion 워크스페이스에 통합된 AI 어시스턴트입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["Notion", "워크스페이스", "요약", "정리"],
  },
  {
    url: "https://zapier.com",
    name: "Zapier",
    nameKo: "재피어",
    description: "Automation platform connecting 6000+ apps with AI-powered workflow creation and task management.",
    descriptionKo: "AI 기반 워크플로우 생성과 작업 관리로 6000개 이상의 앱을 연결하는 자동화 플랫폼입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["자동화", "워크플로우", "앱 연결", "생산성"],
  },
  {
    url: "https://gamma.app",
    name: "Gamma",
    nameKo: "감마",
    description: "AI-powered presentation and document builder creating beautiful slides from text prompts.",
    descriptionKo: "텍스트 프롬프트에서 아름다운 슬라이드를 생성하는 AI 기반 프레젠테이션 빌더입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["프레젠테이션", "슬라이드", "문서", "AI 빌더"],
  },
  {
    url: "https://fireflies.ai",
    name: "Fireflies.ai",
    nameKo: "파이어플라이즈",
    description: "AI meeting assistant that automatically transcribes, summarizes, and searches voice conversations.",
    descriptionKo: "음성 대화를 자동으로 전사, 요약, 검색하는 AI 미팅 어시스턴트입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["미팅", "전사", "요약", "검색"],
  },

  // ──────────── 글쓰기 보조 (writing) ────────────
  {
    url: "https://jasper.ai",
    name: "Jasper",
    nameKo: "재스퍼",
    description: "Enterprise AI writing platform for marketing, sales, and content creation at scale.",
    descriptionKo: "마케팅, 영업, 대규모 콘텐츠 제작을 위한 엔터프라이즈 AI 글쓰기 플랫폼입니다.",
    category: "writing",
    pricingModel: "paid",
    tags: ["마케팅", "콘텐츠", "엔터프라이즈", "글쓰기"],
  },
  {
    url: "https://www.copy.ai",
    name: "Copy.ai",
    nameKo: "카피AI",
    description: "AI copywriting tool for generating marketing copy, product descriptions, and social media content.",
    descriptionKo: "마케팅 카피, 제품 설명, 소셜 미디어 콘텐츠를 생성하는 AI 카피라이팅 도구입니다.",
    category: "writing",
    pricingModel: "freemium",
    tags: ["카피라이팅", "마케팅", "소셜미디어", "콘텐츠"],
  },
  {
    url: "https://grammarly.com",
    name: "Grammarly",
    nameKo: "그래머리",
    description: "AI writing assistant for grammar checking, style improvement, and tone detection across platforms.",
    descriptionKo: "문법 검사, 스타일 개선, 톤 감지를 제공하는 AI 글쓰기 어시스턴트입니다.",
    category: "writing",
    pricingModel: "freemium",
    tags: ["문법 검사", "교정", "스타일", "글쓰기"],
  },
  {
    url: "https://quillbot.com",
    name: "QuillBot",
    nameKo: "퀼봇",
    description: "AI paraphrasing tool with grammar checking, summarization, and citation generation.",
    descriptionKo: "문법 검사, 요약, 인용 생성 기능이 포함된 AI 패러프레이징 도구입니다.",
    category: "writing",
    pricingModel: "freemium",
    tags: ["패러프레이징", "문법 검사", "요약", "인용"],
  },

  // ──────────── 번역 (translation) ────────────
  {
    url: "https://www.deepl.com",
    name: "DeepL",
    nameKo: "딥엘",
    description: "AI translation service known for high accuracy and natural-sounding translations in 30+ languages.",
    descriptionKo: "30개 이상의 언어에서 높은 정확도와 자연스러운 번역을 제공하는 AI 번역 서비스입니다.",
    category: "translation",
    pricingModel: "freemium",
    tags: ["번역", "고정확도", "다국어", "자연스러운"],
  },
  {
    url: "https://papago.naver.com",
    name: "Papago",
    nameKo: "파파고",
    description: "Naver's AI translation service specializing in Korean, Japanese, Chinese, and other Asian languages.",
    descriptionKo: "한국어, 일본어, 중국어 등 아시아 언어에 특화된 네이버의 AI 번역 서비스입니다.",
    category: "translation",
    pricingModel: "free",
    tags: ["번역", "한국어", "아시아 언어", "네이버"],
    isKorean: true,
  },

  // ──────────── 교육 (education) ────────────
  {
    url: "https://www.khanacademy.org/khan-labs",
    name: "Khanmigo",
    nameKo: "칸미고",
    description: "Khan Academy's AI tutor providing personalized learning assistance across subjects.",
    descriptionKo: "다양한 과목에 걸쳐 개인화된 학습 도움을 제공하는 Khan Academy의 AI 튜터입니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["교육", "튜터", "개인화 학습", "Khan Academy"],
  },
  {
    url: "https://www.duolingo.com",
    name: "Duolingo",
    nameKo: "듀오링고",
    description: "AI-powered language learning app with personalized lessons, gamification, and conversation practice.",
    descriptionKo: "개인화된 레슨, 게이미피케이션, 대화 연습을 제공하는 AI 기반 언어 학습 앱입니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["언어 학습", "게이미피케이션", "대화 연습", "앱"],
  },
  {
    url: "https://photomath.com",
    name: "Photomath",
    nameKo: "포토매스",
    description: "AI math solver that scans and solves math problems with step-by-step explanations.",
    descriptionKo: "수학 문제를 스캔하고 단계별 설명과 함께 풀어주는 AI 수학 풀이기입니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["수학", "풀이", "단계별 설명", "스캔"],
  },

  // ──────────── 데이터 분석 (data-analysis) ────────────
  {
    url: "https://julius.ai",
    name: "Julius AI",
    nameKo: "줄리어스",
    description: "AI data analysis platform that lets you chat with your data, create visualizations, and generate reports.",
    descriptionKo: "데이터와 대화하고 시각화를 만들고 보고서를 생성할 수 있는 AI 데이터 분석 플랫폼입니다.",
    category: "data-analysis",
    pricingModel: "freemium",
    tags: ["데이터 분석", "시각화", "보고서", "대화형"],
  },
  {
    url: "https://www.tableau.com",
    name: "Tableau",
    nameKo: "태블로",
    description: "Leading data visualization platform with AI-powered analytics and natural language queries.",
    descriptionKo: "AI 기반 분석과 자연어 쿼리를 지원하는 선도적 데이터 시각화 플랫폼입니다.",
    category: "data-analysis",
    pricingModel: "paid",
    tags: ["데이터 시각화", "분석", "BI", "대시보드"],
  },

  // ──────────── 한국어 LLM / 한국 서비스 (korean-llm) ────────────
  {
    url: "https://clova.ai",
    name: "NAVER CLOVA",
    nameKo: "네이버 클로바",
    description: "Naver's AI platform offering HyperCLOVA X for Korean language understanding and generation.",
    descriptionKo: "한국어 이해와 생성을 위한 HyperCLOVA X를 제공하는 네이버의 AI 플랫폼입니다.",
    category: "korean-llm",
    pricingModel: "freemium",
    tags: ["네이버", "HyperCLOVA", "한국어 AI", "LLM"],
    isKorean: true,
  },
  {
    url: "https://wrtn.ai",
    name: "Wrtn",
    nameKo: "뤼튼",
    description: "Korean AI platform offering free access to GPT-4, Claude, and other models with Korean optimization.",
    descriptionKo: "GPT-4, Claude 등 다양한 AI 모델에 무료로 접근할 수 있는 한국어 최적화 AI 플랫폼입니다.",
    category: "korean-llm",
    pricingModel: "free",
    tags: ["뤼튼", "한국어", "무료", "멀티모델"],
    isKorean: true,
  },
  {
    url: "https://ask.adobe.com",
    name: "Adobe Ask",
    nameKo: "어도비 애스크",
    description: "Adobe's AI assistant for creative tools, answering questions and providing guidance.",
    descriptionKo: "크리에이티브 도구에 대한 질문에 답하고 가이드를 제공하는 Adobe의 AI 어시스턴트입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["Adobe", "크리에이티브", "가이드", "어시스턴트"],
  },
  {
    url: "https://www.maltbot.com",
    name: "Maltbot",
    nameKo: "몰트봇",
    description: "AI-powered chatbot platform for creating and deploying conversational AI agents.",
    descriptionKo: "대화형 AI 에이전트를 만들고 배포할 수 있는 AI 기반 챗봇 플랫폼입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["챗봇", "에이전트", "대화형 AI", "배포"],
  },

  // ──────────── 의료/헬스케어 (healthcare) ────────────
  {
    url: "https://www.ada.com",
    name: "Ada Health",
    nameKo: "에이다 헬스",
    description: "AI-powered symptom assessment and health guidance platform used by millions worldwide.",
    descriptionKo: "전 세계 수백만 명이 사용하는 AI 기반 증상 평가 및 건강 가이드 플랫폼입니다.",
    category: "healthcare",
    pricingModel: "free",
    tags: ["증상 평가", "건강", "의료 AI", "가이드"],
  },

  // ──────────── 추가 유명 서비스들 ────────────
  {
    url: "https://www.anthropic.com/claude-code",
    name: "Claude Code",
    nameKo: "클로드 코드",
    description: "Anthropic's agentic coding tool that operates in the terminal for autonomous software development.",
    descriptionKo: "자율적 소프트웨어 개발을 위해 터미널에서 작동하는 Anthropic의 에이전틱 코딩 도구입니다.",
    category: "code-assistant",
    pricingModel: "paid",
    tags: ["Anthropic", "터미널", "에이전틱", "코딩"],
  },
  {
    url: "https://openai.com/o1",
    name: "OpenAI o1",
    nameKo: "OpenAI o1",
    description: "OpenAI's reasoning-focused model with chain-of-thought capabilities for complex problem solving.",
    descriptionKo: "복잡한 문제 해결을 위한 사고 체인 기능을 갖춘 OpenAI의 추론 중심 모델입니다.",
    category: "text-generation",
    pricingModel: "paid",
    tags: ["추론", "OpenAI", "문제 해결", "사고 체인"],
  },
  {
    url: "https://www.notion.so",
    name: "Notion",
    nameKo: "노션",
    description: "All-in-one workspace combining notes, docs, databases, and project management with AI features.",
    descriptionKo: "노트, 문서, 데이터베이스, 프로젝트 관리를 AI 기능과 결합한 올인원 워크스페이스입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["워크스페이스", "노트", "프로젝트 관리", "데이터베이스"],
  },
  {
    url: "https://www.beautiful.ai",
    name: "Beautiful.ai",
    nameKo: "뷰티풀AI",
    description: "AI-powered presentation maker that automatically designs beautiful slides.",
    descriptionKo: "아름다운 슬라이드를 자동으로 디자인하는 AI 프레젠테이션 메이커입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["프레젠테이션", "슬라이드", "자동 디자인", "비즈니스"],
  },
  {
    url: "https://www.loom.com",
    name: "Loom",
    nameKo: "룸",
    description: "Video messaging platform with AI-powered summaries, chapters, and task generation.",
    descriptionKo: "AI 기반 요약, 챕터, 작업 생성 기능을 갖춘 비디오 메시징 플랫폼입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["비디오 메시지", "요약", "협업", "비동기"],
  },
  {
    url: "https://www.synthesia.io",
    name: "Synthesia",
    nameKo: "신세시아",
    description: "AI video generation platform creating professional videos with AI avatars in 120+ languages.",
    descriptionKo: "120개 이상의 언어로 AI 아바타를 활용한 전문 비디오를 생성하는 AI 비디오 생성 플랫폼입니다.",
    category: "video",
    pricingModel: "paid",
    tags: ["AI 아바타", "비디오 생성", "다국어", "전문적"],
  },
  {
    url: "https://huggingface.co",
    name: "Hugging Face",
    nameKo: "허깅페이스",
    description: "The AI community platform hosting 500K+ models, datasets, and ML apps for open-source AI.",
    descriptionKo: "50만 개 이상의 모델, 데이터셋, ML 앱을 호스팅하는 오픈소스 AI 커뮤니티 플랫폼입니다.",
    category: "data-analysis",
    pricingModel: "freemium",
    tags: ["오픈소스", "모델 허브", "커뮤니티", "ML"],
  },
  {
    url: "https://www.invideo.io",
    name: "InVideo AI",
    nameKo: "인비디오",
    description: "AI video generator that creates publish-ready videos from text prompts in minutes.",
    descriptionKo: "텍스트 프롬프트에서 몇 분 만에 퍼블리시 가능한 비디오를 생성하는 AI 비디오 생성기입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["비디오 생성", "텍스트to비디오", "빠른 생성", "퍼블리시"],
  },
  {
    url: "https://www.opus.pro",
    name: "Opus Clip",
    nameKo: "오푸스 클립",
    description: "AI-powered video repurposing tool that turns long videos into viral short clips.",
    descriptionKo: "긴 영상을 바이럴 숏클립으로 변환하는 AI 기반 비디오 리퍼포징 도구입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["숏클립", "리퍼포징", "바이럴", "비디오 편집"],
  },
  {
    url: "https://www.d-id.com",
    name: "D-ID",
    nameKo: "디아이디",
    description: "AI-powered platform for creating talking avatar videos from a single photo and audio.",
    descriptionKo: "사진 한 장과 오디오에서 토킹 아바타 비디오를 생성하는 AI 플랫폼입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["토킹 아바타", "비디오 생성", "사진to비디오", "AI 아바타"],
  },
];

async function main() {
  console.log(`📦 ${SERVICES.length}개의 AI 서비스 등록 시작...\n`);

  // DB 연결 테스트
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
  let skipped = 0;
  let errors = 0;

  for (const svc of SERVICES) {
    try {
      // URL or name 중복 체크
      const existing = await client.query(
        `SELECT id, "nameKo", "descriptionKo"
         FROM "Service"
         WHERE url = $1 OR url = $2 OR url = $3 OR name = $4
         LIMIT 1`,
        [svc.url, svc.url.replace(/\/$/, ""), svc.url + "/", svc.name]
      );

      if (existing.rows.length > 0) {
        const ex = existing.rows[0];
        // 기존 서비스에 한국어 정보 업데이트
        if ((svc.nameKo && !ex.nameKo) || (svc.descriptionKo && !ex.descriptionKo)) {
          await client.query(
            `UPDATE "Service"
             SET "nameKo" = COALESCE("nameKo", $1),
                 "descriptionKo" = COALESCE("descriptionKo", $2),
                 "isKorean" = CASE WHEN $3 = true THEN true ELSE "isKorean" END
             WHERE id = $4`,
            [svc.nameKo || null, svc.descriptionKo || null, svc.isKorean || false, ex.id]
          );
          console.log(`  ✏️  [업데이트] ${svc.name} — 한국어 정보 추가`);
        } else {
          console.log(`  ⏭️  [건너뜀] ${svc.name} — 이미 등록됨`);
        }
        skipped++;
        continue;
      }

      const slug = createSlug(svc.name);

      // 슬러그 중복 체크
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
          id, finalSlug, svc.url, svc.name, svc.nameKo || null,
          svc.description, svc.descriptionKo || null,
          svc.tagline || null, svc.category, svc.pricingModel,
          JSON.stringify(svc.tags), svc.isKorean || false,
          svc.logoUrl || null,
          svc.faviconUrl || `https://www.google.com/s2/favicons?domain=${domain}&sz=128`,
          null, "auto", 0.5,
          0, 0, 0, false,
        ]
      );

      console.log(`  ✅ [등록] ${svc.name} (${svc.category})`);
      created++;
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      if (message.includes("unique") || message.includes("duplicate") || message.includes("Unique")) {
        console.log(`  ⏭️  [건너뜀] ${svc.name} — 이미 등록됨 (unique constraint)`);
        skipped++;
      } else {
        console.error(`  ❌ [에러] ${svc.name}: ${message}`);
        errors++;
      }
    }
  }

  console.log(`\n✨ 완료!`);
  console.log(`   ✅ 등록: ${created}개`);
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
