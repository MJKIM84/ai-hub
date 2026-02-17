import { ImageResponse } from "next/og";

export const size = { width: 180, height: 180 };
export const contentType = "image/png";

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          background: "linear-gradient(135deg, #6366f1 0%, #a855f7 100%)",
          borderRadius: "38px",
        }}
      >
        {/* 돋보기 + AI 텍스트 */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            position: "relative",
          }}
        >
          <svg
            width="120"
            height="120"
            viewBox="0 0 120 120"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle cx="50" cy="50" r="28" stroke="white" strokeWidth="8" fill="none" opacity="0.95" />
            <line x1="70" y1="70" x2="98" y2="98" stroke="white" strokeWidth="8" strokeLinecap="round" opacity="0.95" />
            <text x="50" y="56" textAnchor="middle" fontFamily="system-ui, sans-serif" fontWeight="800" fontSize="28" fill="white">AI</text>
          </svg>
        </div>
      </div>
    ),
    { ...size }
  );
}
