import { ImageResponse } from "next/og";

export const size = { width: 32, height: 32 };
export const contentType = "image/png";

export default function Icon() {
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
          borderRadius: "7px",
        }}
      >
        <svg
          width="22"
          height="22"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="10.5" cy="10.5" r="6" stroke="white" strokeWidth="2.5" fill="none" />
          <line x1="15" y1="15" x2="20" y2="20" stroke="white" strokeWidth="2.5" strokeLinecap="round" />
          <text x="10.5" y="13" textAnchor="middle" fontFamily="sans-serif" fontWeight="800" fontSize="7" fill="white">AI</text>
        </svg>
      </div>
    ),
    { ...size }
  );
}
