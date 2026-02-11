export const CATEGORIES = [
  { id: 'all', name: 'All', nameKo: '전체', icon: 'LayoutGrid' },
  { id: 'indie-dev', name: 'Indie Dev', nameKo: '개인개발', icon: 'Rocket' },
  { id: 'text-generation', name: 'Text Generation', nameKo: '텍스트 생성', icon: 'MessageSquare' },
  { id: 'image-generation', name: 'Image Generation', nameKo: '이미지 생성', icon: 'Image' },
  { id: 'image-editing', name: 'Image Editing', nameKo: '이미지 편집', icon: 'Palette' },
  { id: 'code-assistant', name: 'Code Assistant', nameKo: '코드 어시스턴트', icon: 'Code2' },
  { id: 'productivity', name: 'Productivity', nameKo: '생산성 도구', icon: 'Zap' },
  { id: 'voice-speech', name: 'Voice & Speech', nameKo: '음성 인식', icon: 'Mic' },
  { id: 'education', name: 'Education', nameKo: '교육/튜터링', icon: 'GraduationCap' },
  { id: 'video', name: 'Video', nameKo: '비디오', icon: 'Video' },
  { id: 'data-analysis', name: 'Data Analysis', nameKo: '데이터 분석', icon: 'BarChart3' },
  { id: 'writing', name: 'Writing', nameKo: '글쓰기 보조', icon: 'PenTool' },
  { id: 'translation', name: 'Translation', nameKo: '번역', icon: 'Languages' },
  { id: 'healthcare', name: 'Healthcare', nameKo: '의료/헬스케어', icon: 'Heart' },
  { id: 'korean-llm', name: 'Korean LLM', nameKo: '한국어 LLM', icon: 'Globe' },
] as const;

export type CategoryId = (typeof CATEGORIES)[number]['id'];

export const PRICING_MODELS = [
  { id: 'free', name: 'Free', nameKo: '무료', color: 'emerald' },
  { id: 'freemium', name: 'Freemium', nameKo: '프리미엄', color: 'blue' },
  { id: 'paid', name: 'Paid', nameKo: '유료', color: 'amber' },
] as const;

export type PricingModel = (typeof PRICING_MODELS)[number]['id'];
