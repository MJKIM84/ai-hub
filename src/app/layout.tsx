import type { Metadata } from "next";
import Script from "next/script";
import { ThemeProvider } from "@/components/ThemeProvider";
import "./globals.css";

const GA_ID = process.env.NEXT_PUBLIC_GA_ID;
const CLARITY_ID = process.env.NEXT_PUBLIC_CLARITY_ID;

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://findmy.ai.kr";
const SITE_NAME = "FindMyAI";
const SITE_DESCRIPTION =
  "나에게 맞는 AI를 찾아보세요. ChatGPT, Claude, Midjourney 등 수백 개의 AI 도구를 카테고리별로 탐색하고, 개인 개발자도 무료로 AI 서비스를 등록·홍보할 수 있는 AI 디렉토리입니다.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "FindMyAI - 나에게 맞는 AI를 찾아보세요 | AI 도구 비교·발견·등록",
    template: "%s | FindMyAI",
  },
  description: SITE_DESCRIPTION,
  keywords: [
    "AI", "인공지능", "AI 도구", "AI 서비스", "FindMyAI", "AI 디렉토리",
    "ChatGPT", "Claude", "Midjourney", "AI 비교", "AI 추천",
    "개인개발", "사이드 프로젝트", "AI 홍보", "무료 등록",
    "인공지능 서비스 모음", "AI tool directory", "find my AI",
  ],
  authors: [{ name: "FindMyAI" }],
  creator: "FindMyAI",
  publisher: "FindMyAI",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "FindMyAI - 나에게 맞는 AI를 찾아보세요",
    description: SITE_DESCRIPTION,
    url: SITE_URL,
    siteName: SITE_NAME,
    type: "website",
    locale: "ko_KR",
    images: [
      {
        url: "/opengraph-image",
        width: 1200,
        height: 630,
        alt: "FindMyAI - 나에게 맞는 AI를 찾아보세요",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "FindMyAI - 나에게 맞는 AI를 찾아보세요",
    description: SITE_DESCRIPTION,
    images: ["/opengraph-image"],
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
    ...(process.env.NEXT_PUBLIC_GOOGLE_VERIFICATION
      ? { google: process.env.NEXT_PUBLIC_GOOGLE_VERIFICATION }
      : {}),
    ...(process.env.NEXT_PUBLIC_NAVER_VERIFICATION
      ? { other: { "naver-site-verification": process.env.NEXT_PUBLIC_NAVER_VERIFICATION } }
      : {}),
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // JSON-LD 구조화 데이터 — 웹사이트 + 검색 액션 + 조직 + FAQ
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": `${SITE_URL}/#website`,
        url: SITE_URL,
        name: SITE_NAME,
        alternateName: ["FindMyAI", "파인드마이AI", "find my ai"],
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
          url: `${SITE_URL}/opengraph-image`,
        },
        sameAs: [],
      },
      {
        "@type": "CollectionPage",
        "@id": `${SITE_URL}/#collection`,
        url: SITE_URL,
        name: "AI 도구 디렉토리",
        description: "ChatGPT, Claude, Midjourney 등 AI 도구를 카테고리별로 탐색하세요.",
        isPartOf: { "@id": `${SITE_URL}/#website` },
        inLanguage: "ko-KR",
      },
      {
        "@type": "FAQPage",
        mainEntity: [
          {
            "@type": "Question",
            name: "FindMyAI는 무엇인가요?",
            acceptedAnswer: {
              "@type": "Answer",
              text: "FindMyAI는 ChatGPT, Claude, Midjourney 등 수백 개의 AI 도구를 카테고리별로 탐색하고 비교할 수 있는 AI 디렉토리 서비스입니다.",
            },
          },
          {
            "@type": "Question",
            name: "AI 서비스를 무료로 등록할 수 있나요?",
            acceptedAnswer: {
              "@type": "Answer",
              text: "네, 개인 개발자도 URL 하나만 입력하면 1분 안에 무료로 AI 서비스를 등록하고 홍보할 수 있습니다.",
            },
          },
          {
            "@type": "Question",
            name: "어떤 카테고리의 AI 도구를 찾을 수 있나요?",
            acceptedAnswer: {
              "@type": "Answer",
              text: "텍스트 생성, 이미지 생성, 코드 어시스턴트, 음성/스피치, 번역, 교육, 데이터 분석, 영상 편집 등 다양한 카테고리를 제공합니다.",
            },
          },
        ],
      },
    ],
  };

  return (
    <html lang="ko" suppressHydrationWarning>
      <head>
        <link
          rel="alternate"
          type="application/rss+xml"
          title="FindMyAI - AI 도구 피드"
          href={`${SITE_URL}/feed.xml`}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="antialiased min-h-screen transition-colors duration-300">
        {/* Google Analytics */}
        {GA_ID && (
          <>
            <Script
              src={`https://www.googletagmanager.com/gtag/js?id=${GA_ID}`}
              strategy="afterInteractive"
            />
            <Script id="google-analytics" strategy="afterInteractive">
              {`
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());
                gtag('config', '${GA_ID}', {
                  page_path: window.location.pathname,
                });
              `}
            </Script>
          </>
        )}
        {/* Microsoft Clarity */}
        {CLARITY_ID && (
          <Script id="microsoft-clarity" strategy="afterInteractive">
            {`
              (function(c,l,a,r,i,t,y){
                c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
                t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
                y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
              })(window, document, "clarity", "script", "${CLARITY_ID}");
            `}
          </Script>
        )}
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
