import type { Metadata } from "next";
import { ThemeProvider } from "@/components/ThemeProvider";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI HUB - AI 서비스 허브 포털",
  description: "AI 서비스를 한눈에 발견하고 비교하세요. 개발자와 사용자를 연결하는 미니멀리스트 AI 도구 디렉토리.",
  keywords: ["AI", "인공지능", "AI 도구", "AI 서비스", "AI 허브", "AI 디렉토리"],
  openGraph: {
    title: "AI HUB - AI 서비스 허브 포털",
    description: "AI 서비스를 한눈에 발견하고 비교하세요.",
    type: "website",
    locale: "ko_KR",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ko" suppressHydrationWarning>
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
