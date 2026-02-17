/**
 * Google Translate 무료 API를 활용한 영→한 번역 유틸리티
 */

const TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single";

/**
 * 텍스트가 주로 영어(라틴 문자)인지 판단
 */
export function isEnglishText(text: string): boolean {
  if (!text) return false;
  const ascii = text.replace(/[\s\d\W]/g, "");
  if (ascii.length === 0) return false;
  const latinCount = (ascii.match(/[a-zA-Z]/g) || []).length;
  return latinCount / ascii.length > 0.7;
}

/**
 * Google Translate 무료 API로 영→한 번역
 */
export async function translateToKorean(text: string): Promise<string | null> {
  if (!text || !isEnglishText(text)) return null;

  try {
    const params = new URLSearchParams({
      client: "gtx",
      sl: "en",
      tl: "ko",
      dt: "t",
      q: text.substring(0, 1000), // 최대 1000자
    });

    const res = await fetch(`${TRANSLATE_URL}?${params}`, {
      signal: AbortSignal.timeout(8000),
    });

    if (!res.ok) return null;

    const data = await res.json();
    // 응답 구조: [[["번역된 텍스트","원문",...],...],...]
    if (Array.isArray(data) && Array.isArray(data[0])) {
      const translated = data[0]
        .filter((segment: unknown[]) => segment && segment[0])
        .map((segment: unknown[]) => segment[0])
        .join("");
      return translated || null;
    }

    return null;
  } catch (err) {
    console.error("[Translator] Error:", err);
    return null;
  }
}

/**
 * 서비스 설명을 한국어로 번역 (이름은 브랜드/고유명사이므로 번역하지 않음)
 */
export async function translateService(
  name: string,
  description: string | null
): Promise<{ nameKo: string | null; descriptionKo: string | null }> {
  const descriptionKo = description
    ? await translateToKorean(description)
    : null;

  return { nameKo: name, descriptionKo };
}
