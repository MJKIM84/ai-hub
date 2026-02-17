import { ImageResponse } from "next/og";

export const runtime = "edge";
export const alt = "FindMyAI - 나에게 맞는 AI를 찾아보세요";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function OGImage() {
  return new ImageResponse(
    (
      <div
        style={{
          background: "linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%)",
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: "sans-serif",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Background grid pattern */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundImage:
              "linear-gradient(rgba(99,102,241,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(99,102,241,0.1) 1px, transparent 1px)",
            backgroundSize: "60px 60px",
            display: "flex",
          }}
        />

        {/* Glow effect */}
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: "600px",
            height: "600px",
            borderRadius: "50%",
            background: "radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%)",
            display: "flex",
          }}
        />

        {/* Logo / Icon */}
        <div
          style={{
            fontSize: "72px",
            marginBottom: "20px",
            display: "flex",
          }}
        >
          🔍
        </div>

        {/* Title */}
        <div
          style={{
            fontSize: "64px",
            fontWeight: 800,
            color: "white",
            letterSpacing: "-2px",
            display: "flex",
            alignItems: "center",
            gap: "12px",
          }}
        >
          <span style={{ color: "#818cf8" }}>Find</span>
          <span>My</span>
          <span style={{ color: "#6366f1" }}>AI</span>
        </div>

        {/* Subtitle */}
        <div
          style={{
            fontSize: "28px",
            color: "#94a3b8",
            marginTop: "16px",
            display: "flex",
          }}
        >
          나에게 맞는 AI를 찾아보세요
        </div>

        {/* Tags */}
        <div
          style={{
            display: "flex",
            gap: "12px",
            marginTop: "32px",
          }}
        >
          {["AI 도구 비교", "무료 등록", "카테고리별 탐색"].map((tag) => (
            <div
              key={tag}
              style={{
                background: "rgba(99,102,241,0.2)",
                border: "1px solid rgba(99,102,241,0.3)",
                borderRadius: "20px",
                padding: "8px 20px",
                color: "#a5b4fc",
                fontSize: "18px",
                display: "flex",
              }}
            >
              {tag}
            </div>
          ))}
        </div>

        {/* URL */}
        <div
          style={{
            position: "absolute",
            bottom: "32px",
            fontSize: "20px",
            color: "#475569",
            display: "flex",
          }}
        >
          findmy.ai.kr
        </div>
      </div>
    ),
    { ...size }
  );
}
