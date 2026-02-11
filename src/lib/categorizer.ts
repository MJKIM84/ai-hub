const CATEGORY_KEYWORDS: Record<string, string[]> = {
  'indie-dev': [
    'indie', 'side project', 'solo developer', 'personal project', 'hobby project',
    '개인개발', '사이드 프로젝트', '1인 개발', '인디 개발', '솔로 개발자',
    'maker', 'bootstrapped', 'open source', 'pet project',
  ],
  'text-generation': [
    'gpt', 'llm', 'chatbot', 'chat', 'language model', 'conversational',
    '챗봇', '대화', '언어 모델', 'ai assistant', 'copilot',
  ],
  'image-generation': [
    'image generat', 'text to image', 'diffusion', 'dall-e', 'midjourney',
    'stable diffusion', '이미지 생성', 'art generat', 'ai art',
  ],
  'image-editing': [
    'image edit', 'photo edit', 'enhance', 'upscale', 'remove background',
    '이미지 편집', '사진 편집', 'retouch',
  ],
  'code-assistant': [
    'code', 'programming', 'ide', 'developer tool', 'coding', 'github copilot',
    '코딩', '개발', 'debug', 'software development',
  ],
  'productivity': [
    'productivity', 'workflow', 'automation', 'project management', 'notion',
    '생산성', '자동화', '업무', 'task management', 'scheduling',
  ],
  'voice-speech': [
    'speech', 'voice', 'tts', 'stt', 'text to speech', 'speech to text',
    '음성', '목소리', 'audio', 'transcription', 'dictation',
  ],
  'education': [
    'education', 'learning', 'tutor', 'course', 'study', 'quiz',
    '교육', '학습', '튜터', 'e-learning', 'training',
  ],
  'video': [
    'video', 'animation', 'motion', 'film', 'editing video',
    '영상', '비디오', '애니메이션',
  ],
  'data-analysis': [
    'analytics', 'data', 'visualization', 'dashboard', 'insight', 'report',
    '분석', '데이터', '시각화', 'chart', 'statistics',
  ],
  'writing': [
    'writing', 'grammar', 'copywriting', 'content creation', 'blog',
    '글쓰기', '작문', '교정', 'proofreading', 'essay',
  ],
  'translation': [
    'translat', 'multilingual', 'localization', 'interpret',
    '번역', '통역', '다국어',
  ],
  'healthcare': [
    'medical', 'health', 'diagnosis', 'clinical', 'patient', 'biomedical',
    '의료', '건강', '진단', '헬스케어',
  ],
  'korean-llm': [
    'clova', 'hyperclova', '한국어', 'korean language', '뤼튼', 'wrtn',
    'upstage', 'solar',
  ],
};

export function suggestCategory(text: string): {
  primary: string;
  confidence: number;
  alternatives: string[];
} {
  const lowerText = text.toLowerCase();
  const scores: Record<string, number> = {};

  for (const [category, keywords] of Object.entries(CATEGORY_KEYWORDS)) {
    let score = 0;
    for (const keyword of keywords) {
      if (lowerText.includes(keyword.toLowerCase())) {
        score += 1;
      }
    }
    if (score > 0) {
      scores[category] = score;
    }
  }

  const sorted = Object.entries(scores).sort(([, a], [, b]) => b - a);

  if (sorted.length === 0) {
    return { primary: 'productivity', confidence: 0, alternatives: [] };
  }

  const maxScore = sorted[0][1];
  const totalKeywords = CATEGORY_KEYWORDS[sorted[0][0]].length;

  return {
    primary: sorted[0][0],
    confidence: Math.min(maxScore / totalKeywords, 1),
    alternatives: sorted.slice(1, 4).map(([cat]) => cat),
  };
}
