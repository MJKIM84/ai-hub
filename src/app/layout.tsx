import type { Metadata } from "next";
import { ThemeProvider } from "@/components/ThemeProvider";
import "./globals.css";

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://aihub.example.com";
const SITE_NAME = "pipeAI";
const SITE_DESCRIPTION =
  "AI 서비스를 파이프라인으로 연결하세요. 수백 개의 AI 도구를 탐색하고, 나만의 AI 워크플로를 설계할 수 있는 플랫폼입니다. 개인 개발자도 무료로 AI 서비스를 등록·홍보할 수 있습니다.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "pipeAI - AI 파이프라인 플랫폼 | AI 워크플로·비교·발견",
    template: "%s | pipeAI",
  },
  description: SITE_DESCRIPTION,
  keywords: [
    "AI", "인공지능", "AI 도구", "AI 서비스", "AI 파이프라인", "AI 워크플로",
    "ChatGPT", "Claude", "Midjourney", "AI 비교", "AI 추천",
    "개인개발", "사이드 프로젝트", "AI 홍보", "무료 등록",
    "인공지능 서비스 모음", "AI tool directory", "AI workflow builder",
  ],
  authors: [{ name: "pipeAI" }],
  creator: "pipeAI",
  publisher: "pipeAI",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "pipeAI - AI 파이프라인 플랫폼",
    description: SITE_DESCRIPTION,
    url: SITE_URL,
    siteName: SITE_NAME,
    type: "website",
    locale: "ko_KR",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "pipeAI - AI 파이프라인 플랫폼",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "pipeAI - AI 파이프라인 플랫폼",
    description: SITE_DESCRIPTION,
    images: ["/og-image.png"],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  verification: {
    // 네이버 웹마스터 도구 인증 (실제 인증 코드로 교체 필요)
    // other: { "naver-site-verification": "YOUR_NAVER_CODE" },
    // 구글 서치 콘솔 인증 (실제 인증 코드로 교체 필요)
    // google: "YOUR_GOOGLE_CODE",
  },
  ...(process.env.NEXT_PUBLIC_NAVER_VERIFICATION || process.env.NEXT_PUBLIC_GOOGLE_VERIFICATION
    ? {
        other: {
          ...(process.env.NEXT_PUBLIC_NAVER_VERIFICATION
            ? { "naver-site-verification": process.env.NEXT_PUBLIC_NAVER_VERIFICATION }
            : {}),
          ...(process.env.NEXT_PUBLIC_GOOGLE_VERIFICATION
            ? { "google-site-verification": process.env.NEXT_PUBLIC_GOOGLE_VERIFICATION }
            : {}),
        },
      }
    : {}),
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // JSON-LD 구조화 데이터 — 웹사이트 + 검색 액션
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": `${SITE_URL}/#website`,
        url: SITE_URL,
        name: SITE_NAME,
        description: SITE_DESCRIPTION,
        inLanguage: "ko-KR",
        potentialAction: {
          "@type": "SearchAction",
          target: {
            "@type": "EntryPoint",
            urlTemplate: `${SITE_URL}/?q={search_term_string}`,
          },
          "query-input": "required name=search_term_string",
        },
      },
      {
        "@type": "Organization",
        "@id": `${SITE_URL}/#organization`,
        name: SITE_NAME,
        url: SITE_URL,
        logo: {
          "@type": "ImageObject",
          url: `${SITE_URL}/og-image.png`,
        },
      },
    ],
  };

  return (
    <html lang="ko" suppressHydrationWarning>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="antialiased min-h-screen transition-colors duration-300">
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange={false}
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
