/**
 * 세계적으로 유명한 AI 서비스 일괄 등록 스크립트
 * 실행: npx tsx scripts/seed-services.ts
 */

import { PrismaClient } from "../src/generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";
import { config } from "dotenv";

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

function slugify(name: string): string {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9가-힣]+/g, "-")
    .replace(/(^-|-$)/g, "")
    .substring(0, 80);
}

interface ServiceSeed {
  name: string;
  url: string;
  description: string;
  descriptionKo: string;
  category: string;
  pricingModel: string;
  tags: string[];
}

const services: ServiceSeed[] = [
  // ===== 텍스트 생성 / LLM =====
  {
    name: "Google Gemini",
    url: "https://gemini.google.com",
    description: "Google's most capable AI model. Chat, create, explore with multimodal AI.",
    descriptionKo: "구글의 가장 강력한 AI 모델. 멀티모달 AI로 대화, 생성, 탐색을 지원합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation", "productivity"],
  },
  {
    name: "Microsoft Copilot",
    url: "https://copilot.microsoft.com",
    description: "Your everyday AI companion by Microsoft. Powered by GPT-4, integrated with Microsoft 365.",
    descriptionKo: "마이크로소프트의 일상 AI 도우미. GPT-4 기반으로 Microsoft 365와 통합됩니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation", "productivity"],
  },
  {
    name: "Llama (Meta)",
    url: "https://llama.meta.com",
    description: "Meta's open-source large language model. Free to use for research and commercial applications.",
    descriptionKo: "메타의 오픈소스 대규모 언어 모델. 연구 및 상업적 용도로 무료 사용 가능합니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["text-generation"],
  },
  {
    name: "Mistral AI",
    url: "https://mistral.ai",
    description: "Open and portable generative AI for devs and businesses. Building the best open-source models.",
    descriptionKo: "개발자와 기업을 위한 오픈 생성형 AI. 최고의 오픈소스 모델을 구축합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation"],
  },
  {
    name: "Cohere",
    url: "https://cohere.com",
    description: "Enterprise AI platform for search, generation, and classification. Build with LLMs at scale.",
    descriptionKo: "검색, 생성, 분류를 위한 엔터프라이즈 AI 플랫폼. 대규모 LLM을 활용합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation", "data-analysis"],
  },
  {
    name: "Pi by Inflection",
    url: "https://pi.ai",
    description: "A personal AI assistant designed to be kind, helpful, and curious. Built by Inflection AI.",
    descriptionKo: "친절하고 도움이 되며 호기심 많은 개인 AI 어시스턴트. Inflection AI가 개발했습니다.",
    category: "text-generation",
    pricingModel: "free",
    tags: ["text-generation"],
  },
  {
    name: "Poe",
    url: "https://poe.com",
    description: "Access multiple AI chatbots in one platform. Chat with GPT-4, Claude, Gemini, and more.",
    descriptionKo: "하나의 플랫폼에서 여러 AI 챗봇을 이용. GPT-4, Claude, Gemini 등과 대화할 수 있습니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation"],
  },
  {
    name: "Character.AI",
    url: "https://character.ai",
    description: "Chat with AI characters. Create and interact with intelligent agents powered by neural language models.",
    descriptionKo: "AI 캐릭터와 대화하세요. 신경 언어 모델로 구동되는 지능형 에이전트를 만들고 상호작용합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation"],
  },
  {
    name: "xAI Grok",
    url: "https://grok.x.ai",
    description: "AI assistant by xAI with real-time knowledge and witty personality. Integrated with X (Twitter).",
    descriptionKo: "xAI의 AI 어시스턴트. 실시간 지식과 위트 있는 성격을 갖추고 X(트위터)와 통합됩니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation"],
  },

  // ===== 이미지 생성 =====
  {
    name: "DALL-E 3",
    url: "https://openai.com/dall-e-3",
    description: "OpenAI's text-to-image model. Create realistic images and art from natural language descriptions.",
    descriptionKo: "OpenAI의 텍스트-이미지 변환 모델. 자연어 설명으로 사실적인 이미지와 예술 작품을 생성합니다.",
    category: "image-generation",
    pricingModel: "paid",
    tags: ["image-generation"],
  },
  {
    name: "Adobe Firefly",
    url: "https://www.adobe.com/products/firefly.html",
    description: "Adobe's generative AI for creative professionals. Safe for commercial use with training on licensed content.",
    descriptionKo: "크리에이티브 전문가를 위한 어도비의 생성형 AI. 라이선스 콘텐츠로 학습되어 상업적 사용이 안전합니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["image-generation", "image-editing"],
  },
  {
    name: "Leonardo.AI",
    url: "https://leonardo.ai",
    description: "AI-powered creative platform for generating production-quality visual assets with speed and style.",
    descriptionKo: "프로덕션 품질의 시각 자산을 빠르고 스타일리시하게 생성하는 AI 크리에이티브 플랫폼입니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["image-generation"],
  },
  {
    name: "Ideogram",
    url: "https://ideogram.ai",
    description: "AI image generator that excels at text rendering within images. Create logos, posters, and more.",
    descriptionKo: "이미지 내 텍스트 렌더링에 뛰어난 AI 이미지 생성기. 로고, 포스터 등을 만들 수 있습니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["image-generation"],
  },
  {
    name: "Flux AI",
    url: "https://flux1.ai",
    description: "State-of-the-art open-source image generation model by Black Forest Labs.",
    descriptionKo: "Black Forest Labs의 최첨단 오픈소스 이미지 생성 모델입니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["image-generation"],
  },

  // ===== 비디오 =====
  {
    name: "Sora",
    url: "https://openai.com/sora",
    description: "OpenAI's text-to-video model. Generate realistic and imaginative videos from text instructions.",
    descriptionKo: "OpenAI의 텍스트-비디오 변환 모델. 텍스트 지시로 사실적이고 상상력 넘치는 비디오를 생성합니다.",
    category: "video",
    pricingModel: "paid",
    tags: ["video"],
  },
  {
    name: "Pika",
    url: "https://pika.art",
    description: "AI video generation platform. Create and edit videos with AI in creative new ways.",
    descriptionKo: "AI 비디오 생성 플랫폼. 창의적인 방식으로 AI를 활용해 비디오를 만들고 편집합니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["video"],
  },
  {
    name: "Luma Dream Machine",
    url: "https://lumalabs.ai/dream-machine",
    description: "AI model that generates high-quality, realistic videos from text and images.",
    descriptionKo: "텍스트와 이미지로 고품질의 사실적인 비디오를 생성하는 AI 모델입니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["video"],
  },
  {
    name: "HeyGen",
    url: "https://www.heygen.com",
    description: "AI video generator with realistic AI avatars. Create professional videos in minutes.",
    descriptionKo: "현실적인 AI 아바타를 활용한 AI 비디오 생성기. 몇 분 만에 전문적인 비디오를 만듭니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["video"],
  },
  {
    name: "Synthesia",
    url: "https://www.synthesia.io",
    description: "AI video creation platform. Turn text into professional videos with AI avatars in 130+ languages.",
    descriptionKo: "AI 비디오 제작 플랫폼. 130개 이상 언어의 AI 아바타로 텍스트를 전문 비디오로 변환합니다.",
    category: "video",
    pricingModel: "paid",
    tags: ["video"],
  },
  {
    name: "Kling AI",
    url: "https://klingai.com",
    description: "Kuaishou's AI video generation model. Create high-quality videos with advanced motion capabilities.",
    descriptionKo: "콰이서우의 AI 비디오 생성 모델. 고급 모션 기능으로 고품질 비디오를 생성합니다.",
    category: "video",
    pricingModel: "freemium",
    tags: ["video"],
  },

  // ===== 음성/음악 =====
  {
    name: "Whisper (OpenAI)",
    url: "https://openai.com/research/whisper",
    description: "OpenAI's open-source speech recognition model. Robust multilingual speech-to-text.",
    descriptionKo: "OpenAI의 오픈소스 음성 인식 모델. 강력한 다국어 음성-텍스트 변환을 지원합니다.",
    category: "voice-speech",
    pricingModel: "free",
    tags: ["voice-speech"],
  },
  {
    name: "Murf AI",
    url: "https://murf.ai",
    description: "AI voice generator with natural-sounding text-to-speech. Create studio-quality voiceovers.",
    descriptionKo: "자연스러운 텍스트-음성 변환 AI 음성 생성기. 스튜디오 품질의 보이스오버를 제작합니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["voice-speech"],
  },
  {
    name: "Udio",
    url: "https://www.udio.com",
    description: "AI music generation platform. Create full songs with vocals, instruments and production from text.",
    descriptionKo: "AI 음악 생성 플랫폼. 텍스트로 보컬, 악기, 프로덕션이 포함된 완전한 노래를 만듭니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["voice-speech"],
  },
  {
    name: "AIVA",
    url: "https://www.aiva.ai",
    description: "AI music composer. Create original music for films, games, commercials, and more.",
    descriptionKo: "AI 음악 작곡가. 영화, 게임, 광고 등을 위한 오리지널 음악을 만듭니다.",
    category: "voice-speech",
    pricingModel: "freemium",
    tags: ["voice-speech"],
  },

  // ===== 코드 어시스턴트 =====
  {
    name: "Replit AI",
    url: "https://replit.com/ai",
    description: "AI-powered coding platform. Build software faster with AI assistance in the browser.",
    descriptionKo: "AI 기반 코딩 플랫폼. 브라우저에서 AI 지원으로 더 빠르게 소프트웨어를 개발합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant"],
  },
  {
    name: "Tabnine",
    url: "https://www.tabnine.com",
    description: "AI code assistant for software developers. Whole-line and full-function code completions.",
    descriptionKo: "소프트웨어 개발자를 위한 AI 코드 어시스턴트. 전체 라인 및 전체 함수 코드 완성을 제공합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant"],
  },
  {
    name: "Codeium (Windsurf)",
    url: "https://codeium.com",
    description: "Free AI-powered code acceleration toolkit. Autocomplete, search, and chat for 70+ languages.",
    descriptionKo: "무료 AI 코드 가속 툴킷. 70개 이상 언어에 대한 자동완성, 검색, 채팅을 지원합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant"],
  },
  {
    name: "v0 by Vercel",
    url: "https://v0.dev",
    description: "AI-powered UI generation tool by Vercel. Generate React components from text descriptions.",
    descriptionKo: "Vercel의 AI 기반 UI 생성 도구. 텍스트 설명으로 React 컴포넌트를 생성합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant"],
  },
  {
    name: "Bolt.new",
    url: "https://bolt.new",
    description: "AI full-stack web development platform. Build, run, and deploy full-stack apps from prompts.",
    descriptionKo: "AI 풀스택 웹 개발 플랫폼. 프롬프트로 풀스택 앱을 빌드, 실행, 배포합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant"],
  },
  {
    name: "Lovable",
    url: "https://lovable.dev",
    description: "AI-powered software engineer. Build full-stack web apps from natural language descriptions.",
    descriptionKo: "AI 기반 소프트웨어 엔지니어. 자연어 설명으로 풀스택 웹 앱을 구축합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant"],
  },

  // ===== 생산성 도구 =====
  {
    name: "Jasper",
    url: "https://www.jasper.ai",
    description: "AI copilot for enterprise marketing teams. Create on-brand content at scale.",
    descriptionKo: "엔터프라이즈 마케팅 팀을 위한 AI 코파일럿. 브랜드에 맞는 콘텐츠를 대규모로 생성합니다.",
    category: "productivity",
    pricingModel: "paid",
    tags: ["productivity", "writing"],
  },
  {
    name: "Copy.ai",
    url: "https://www.copy.ai",
    description: "AI-powered copywriting and content creation platform for marketing and sales teams.",
    descriptionKo: "마케팅 및 세일즈 팀을 위한 AI 기반 카피라이팅 및 콘텐츠 제작 플랫폼입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity", "writing"],
  },
  {
    name: "Otter.ai",
    url: "https://otter.ai",
    description: "AI meeting assistant for transcription, notes, and summaries. Real-time meeting capture.",
    descriptionKo: "전사, 노트, 요약을 위한 AI 회의 어시스턴트. 실시간 회의 기록을 지원합니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity", "voice-speech"],
  },
  {
    name: "Tome",
    url: "https://tome.app",
    description: "AI-powered presentation and storytelling tool. Create compelling narratives with AI.",
    descriptionKo: "AI 기반 프레젠테이션 및 스토리텔링 도구. AI로 설득력 있는 내러티브를 만듭니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity"],
  },
  {
    name: "Beautiful.ai",
    url: "https://www.beautiful.ai",
    description: "AI-powered presentation software that designs slides for you. Smart templates and formatting.",
    descriptionKo: "슬라이드를 자동으로 디자인해주는 AI 프레젠테이션 소프트웨어. 스마트 템플릿과 포맷팅을 제공합니다.",
    category: "productivity",
    pricingModel: "paid",
    tags: ["productivity"],
  },
  {
    name: "Mem.ai",
    url: "https://mem.ai",
    description: "AI-powered note-taking and knowledge management. Self-organizing workspace with AI search.",
    descriptionKo: "AI 기반 노트 작성 및 지식 관리. AI 검색이 포함된 자가 정리 워크스페이스입니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity"],
  },

  // ===== 글쓰기 =====
  {
    name: "Writesonic",
    url: "https://writesonic.com",
    description: "AI writing platform for creating SEO-optimized content, blogs, ads, and marketing copy.",
    descriptionKo: "SEO 최적화 콘텐츠, 블로그, 광고, 마케팅 카피를 작성하는 AI 글쓰기 플랫폼입니다.",
    category: "writing",
    pricingModel: "freemium",
    tags: ["writing"],
  },
  {
    name: "QuillBot",
    url: "https://quillbot.com",
    description: "AI paraphrasing and writing tool. Rewrite sentences, check grammar, and improve writing.",
    descriptionKo: "AI 패러프레이징 및 글쓰기 도구. 문장 재작성, 문법 검사, 글쓰기 개선을 지원합니다.",
    category: "writing",
    pricingModel: "freemium",
    tags: ["writing"],
  },
  {
    name: "Sudowrite",
    url: "https://www.sudowrite.com",
    description: "AI writing assistant for fiction authors. Generate prose, brainstorm ideas, and overcome writer's block.",
    descriptionKo: "소설 작가를 위한 AI 글쓰기 어시스턴트. 산문 생성, 아이디어 브레인스토밍, 작가의 슬럼프 극복을 돕습니다.",
    category: "writing",
    pricingModel: "paid",
    tags: ["writing"],
  },

  // ===== 번역 =====
  {
    name: "Papago",
    url: "https://papago.naver.com",
    description: "Naver's AI-powered translation service. Supports 13 languages with context-aware translation.",
    descriptionKo: "네이버의 AI 기반 번역 서비스. 13개 언어를 지원하며 문맥 인식 번역을 제공합니다.",
    category: "translation",
    pricingModel: "free",
    tags: ["translation"],
  },

  // ===== 이미지 편집 =====
  {
    name: "Photoroom",
    url: "https://www.photoroom.com",
    description: "AI photo editor for product and portrait photography. Remove backgrounds, create studio-quality images.",
    descriptionKo: "제품 및 인물 사진을 위한 AI 포토 에디터. 배경 제거, 스튜디오 품질 이미지를 생성합니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["image-editing"],
  },
  {
    name: "Clipdrop",
    url: "https://clipdrop.co",
    description: "AI-powered image editing suite by Stability AI. Remove backgrounds, upscale, relight photos.",
    descriptionKo: "Stability AI의 AI 기반 이미지 편집 도구. 배경 제거, 업스케일, 사진 재조명을 지원합니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["image-editing"],
  },
  {
    name: "Lensa AI",
    url: "https://prisma-ai.com/lensa",
    description: "AI-powered photo and video editor. Create magic avatars and enhance selfies with AI.",
    descriptionKo: "AI 기반 사진 및 비디오 편집기. AI로 매직 아바타를 만들고 셀피를 보정합니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["image-editing"],
  },

  // ===== 데이터 분석 =====
  {
    name: "Julius AI",
    url: "https://julius.ai",
    description: "AI data analyst. Analyze data, create visualizations, and get insights with natural language.",
    descriptionKo: "AI 데이터 분석가. 자연어로 데이터를 분석하고 시각화를 생성하며 인사이트를 얻습니다.",
    category: "data-analysis",
    pricingModel: "freemium",
    tags: ["data-analysis"],
  },
  {
    name: "MonkeyLearn",
    url: "https://monkeylearn.com",
    description: "No-code text analytics platform powered by AI. Classify and extract data from text.",
    descriptionKo: "AI 기반 노코드 텍스트 분석 플랫폼. 텍스트에서 데이터를 분류하고 추출합니다.",
    category: "data-analysis",
    pricingModel: "freemium",
    tags: ["data-analysis"],
  },

  // ===== 교육 =====
  {
    name: "Khan Academy Khanmigo",
    url: "https://www.khanacademy.org/khan-labs",
    description: "AI-powered tutor by Khan Academy. Personalized learning assistance powered by GPT-4.",
    descriptionKo: "칸아카데미의 AI 튜터. GPT-4 기반의 개인 맞춤형 학습 지원을 제공합니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["education"],
  },
  {
    name: "Duolingo Max",
    url: "https://www.duolingo.com",
    description: "AI-enhanced language learning app. Practice conversations with AI and get explanations.",
    descriptionKo: "AI가 강화된 언어 학습 앱. AI와 대화를 연습하고 설명을 받을 수 있습니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["education"],
  },
  {
    name: "Socratic by Google",
    url: "https://socratic.org",
    description: "AI-powered homework help app by Google. Get visual explanations for any subject.",
    descriptionKo: "구글의 AI 기반 숙제 도우미 앱. 모든 과목에 대한 시각적 설명을 제공합니다.",
    category: "education",
    pricingModel: "free",
    tags: ["education"],
  },

  // ===== 디자인 =====
  {
    name: "Figma AI",
    url: "https://www.figma.com/ai",
    description: "AI-powered design features in Figma. Generate designs, rename layers, and remove backgrounds.",
    descriptionKo: "Figma의 AI 디자인 기능. 디자인 생성, 레이어 이름 변경, 배경 제거를 지원합니다.",
    category: "image-editing",
    pricingModel: "freemium",
    tags: ["image-editing", "productivity"],
  },
  {
    name: "Framer AI",
    url: "https://www.framer.com",
    description: "AI website builder. Generate and publish websites from text descriptions in seconds.",
    descriptionKo: "AI 웹사이트 빌더. 텍스트 설명으로 몇 초 만에 웹사이트를 생성하고 퍼블리시합니다.",
    category: "code-assistant",
    pricingModel: "freemium",
    tags: ["code-assistant", "productivity"],
  },

  // ===== 검색/리서치 =====
  {
    name: "You.com",
    url: "https://you.com",
    description: "AI-powered search engine. Get summarized answers with cited sources from across the web.",
    descriptionKo: "AI 기반 검색 엔진. 웹 전체에서 출처가 인용된 요약 답변을 제공합니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation"],
  },
  {
    name: "Elicit",
    url: "https://elicit.com",
    description: "AI research assistant. Automate literature reviews and find relevant research papers.",
    descriptionKo: "AI 연구 어시스턴트. 문헌 검토를 자동화하고 관련 연구 논문을 찾아줍니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity", "education"],
  },
  {
    name: "Consensus",
    url: "https://consensus.app",
    description: "AI-powered academic search engine. Find answers in scientific research papers.",
    descriptionKo: "AI 기반 학술 검색 엔진. 과학 연구 논문에서 답변을 찾아줍니다.",
    category: "education",
    pricingModel: "freemium",
    tags: ["education"],
  },

  // ===== 자동화 =====
  {
    name: "Zapier AI",
    url: "https://zapier.com/ai",
    description: "AI-powered workflow automation. Connect apps and automate tasks with natural language.",
    descriptionKo: "AI 기반 워크플로우 자동화. 자연어로 앱을 연결하고 작업을 자동화합니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity"],
  },
  {
    name: "Make (Integromat)",
    url: "https://www.make.com",
    description: "Visual platform for workflow automation with AI capabilities. Connect 1000+ apps.",
    descriptionKo: "AI 기능을 갖춘 시각적 워크플로우 자동화 플랫폼. 1000개 이상의 앱을 연결합니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity"],
  },

  // ===== 마케팅/SEO =====
  {
    name: "Surfer SEO",
    url: "https://surferseo.com",
    description: "AI-powered SEO tool for content optimization. Write and optimize content that ranks.",
    descriptionKo: "콘텐츠 최적화를 위한 AI 기반 SEO 도구. 검색 순위에 오르는 콘텐츠를 작성하고 최적화합니다.",
    category: "writing",
    pricingModel: "paid",
    tags: ["writing", "productivity"],
  },

  // ===== 고객 서비스 =====
  {
    name: "Intercom Fin",
    url: "https://www.intercom.com/fin",
    description: "AI customer service agent by Intercom. Resolve customer issues instantly with AI.",
    descriptionKo: "Intercom의 AI 고객 서비스 에이전트. AI로 고객 문제를 즉시 해결합니다.",
    category: "productivity",
    pricingModel: "paid",
    tags: ["productivity"],
  },
  {
    name: "Tidio",
    url: "https://www.tidio.com",
    description: "AI chatbot and live chat platform for customer support. Automate up to 70% of queries.",
    descriptionKo: "고객 지원을 위한 AI 챗봇 및 실시간 채팅 플랫폼. 문의의 최대 70%를 자동화합니다.",
    category: "productivity",
    pricingModel: "freemium",
    tags: ["productivity"],
  },

  // ===== 3D / 게임 =====
  {
    name: "Meshy",
    url: "https://www.meshy.ai",
    description: "AI 3D model generator. Create 3D assets from text or images for games and design.",
    descriptionKo: "AI 3D 모델 생성기. 텍스트나 이미지로 게임 및 디자인용 3D 자산을 만듭니다.",
    category: "image-generation",
    pricingModel: "freemium",
    tags: ["image-generation"],
  },

  // ===== 한국 서비스 추가 =====
  {
    name: "AskUp",
    url: "https://askup.co",
    description: "Korean AI chatbot service on KakaoTalk. GPT-based Korean language AI assistant.",
    descriptionKo: "카카오톡 기반 한국어 AI 챗봇 서비스. GPT 기반 한국어 AI 어시스턴트입니다.",
    category: "text-generation",
    pricingModel: "freemium",
    tags: ["text-generation", "korean-llm"],
  },
  {
    name: "Toss AI",
    url: "https://toss.im",
    description: "AI-powered financial services by Toss. Smart financial insights and automation.",
    descriptionKo: "토스의 AI 기반 금융 서비스. 스마트한 금융 인사이트와 자동화를 제공합니다.",
    category: "data-analysis",
    pricingModel: "free",
    tags: ["data-analysis"],
  },
];

async function main() {
  console.log(`🚀 ${services.length}개의 AI 서비스 등록을 시작합니다...\n`);

  let created = 0;
  let skipped = 0;
  const errors: string[] = [];

  for (const svc of services) {
    try {
      // URL 중복 체크
      const existing = await prisma.service.findUnique({
        where: { url: svc.url },
      });

      if (existing) {
        console.log(`⏭️  ${svc.name} (이미 등록됨)`);
        skipped++;
        continue;
      }

      const slug = slugify(svc.name);

      // slug 중복 체크
      const slugExists = await prisma.service.findUnique({
        where: { slug },
      });

      const finalSlug = slugExists
        ? `${slug}-${Date.now().toString(36)}`
        : slug;

      await prisma.service.create({
        data: {
          slug: finalSlug,
          url: svc.url,
          name: svc.name,
          description: svc.description,
          descriptionKo: svc.descriptionKo,
          nameKo: svc.name, // 브랜드명 유지
          category: svc.category,
          tags: JSON.stringify(svc.tags),
          pricingModel: svc.pricingModel,
          source: "user",
          isVerified: true,
          isKorean: svc.url.includes(".kr") || svc.url.includes("naver") || svc.url.includes("kakao") || svc.url.includes("toss"),
        },
      });

      console.log(`✅ ${svc.name} (${svc.category})`);
      created++;
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      errors.push(`${svc.name}: ${msg}`);
      console.error(`❌ ${svc.name}: ${msg}`);
    }
  }

  console.log(`\n📊 결과:`);
  console.log(`  등록됨: ${created}개`);
  console.log(`  스킵됨: ${skipped}개`);
  console.log(`  에러: ${errors.length}개`);

  if (errors.length > 0) {
    console.log(`\n에러 목록:`);
    errors.forEach((e) => console.log(`  - ${e}`));
  }

  // 전체 서비스 수 확인
  const total = await prisma.service.count();
  console.log(`\n🎯 총 서비스 수: ${total}개`);

  await prisma.$disconnect();
}

main().catch((err) => {
  console.error("Fatal:", err);
  process.exit(1);
});
