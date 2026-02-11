import type { MetadataRoute } from "next";

const SITE_URL = process.env.NEXT_PUBLIC_APP_URL || "https://aihub.example.com";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/api/", "/admin"],
      },
      {
        // 네이버 검색봇
        userAgent: "Yeti",
        allow: "/",
        disallow: ["/api/", "/admin"],
      },
      {
        // 구글 검색봇
        userAgent: "Googlebot",
        allow: "/",
        disallow: ["/api/", "/admin"],
      },
    ],
    sitemap: `${SITE_URL}/sitemap.xml`,
    host: SITE_URL,
  };
}
