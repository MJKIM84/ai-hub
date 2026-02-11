import * as cheerio from 'cheerio';
import { suggestCategory } from './categorizer';

export interface ScrapeResult {
  name: string;
  description: string | null;
  ogImageUrl: string | null;
  faviconUrl: string;
  suggestedCategory: string;
  suggestedTags: string[];
}

function isPrivateHost(hostname: string): boolean {
  const blocked = [
    /^localhost$/i,
    /^127\.\d+\.\d+\.\d+$/,
    /^10\.\d+\.\d+\.\d+$/,
    /^172\.(1[6-9]|2\d|3[01])\.\d+\.\d+$/,
    /^192\.168\.\d+\.\d+$/,
    /^0\.0\.0\.0$/,
    /^::1$/,
    /^\[::1\]$/,
    /^metadata\.google\.internal$/i,
    /^169\.254\.\d+\.\d+$/,
  ];
  return blocked.some((re) => re.test(hostname));
}

export async function scrapeServiceMetadata(url: string): Promise<ScrapeResult> {
  const parsedUrl = new URL(url);
  const domain = parsedUrl.hostname;

  if (isPrivateHost(domain)) {
    throw new Error("내부 네트워크 주소는 허용되지 않습니다");
  }

  const response = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (compatible; AI-Hub-Bot/1.0)',
      'Accept': 'text/html,application/xhtml+xml',
    },
    signal: AbortSignal.timeout(10000),
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: ${response.status}`);
  }

  const html = await response.text();
  const $ = cheerio.load(html);

  const name =
    $('meta[property="og:title"]').attr('content') ||
    $('meta[name="twitter:title"]').attr('content') ||
    $('title').text().trim() ||
    domain;

  const description =
    $('meta[property="og:description"]').attr('content') ||
    $('meta[name="description"]').attr('content') ||
    $('meta[name="twitter:description"]').attr('content') ||
    null;

  const ogImageUrl =
    $('meta[property="og:image"]').attr('content') ||
    $('meta[name="twitter:image"]').attr('content') ||
    null;

  let faviconUrl = '';
  const iconLink =
    $('link[rel="icon"]').attr('href') ||
    $('link[rel="shortcut icon"]').attr('href') ||
    $('link[rel="apple-touch-icon"]').attr('href');

  if (iconLink) {
    faviconUrl = iconLink.startsWith('http')
      ? iconLink
      : new URL(iconLink, url).toString();
  } else {
    faviconUrl = `https://www.google.com/s2/favicons?domain=${domain}&sz=128`;
  }

  const fullText = `${name} ${description || ''} ${$('h1').text()} ${$('h2').text()}`;
  const { primary, alternatives } = suggestCategory(fullText);

  return {
    name: name.length > 100 ? name.substring(0, 100) : name,
    description: description ? (description.length > 300 ? description.substring(0, 300) : description) : null,
    ogImageUrl: ogImageUrl && ogImageUrl.startsWith('http') ? ogImageUrl : ogImageUrl ? new URL(ogImageUrl, url).toString() : null,
    faviconUrl,
    suggestedCategory: primary,
    suggestedTags: [primary, ...alternatives],
  };
}
