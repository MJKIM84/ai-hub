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
          position: "relative",
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
        </svg>
        <div
          style={{
            position: "absolute",
            top: "6px",
            left: "3px",
            fontSize: "7px",
            fontWeight: 800,
            color: "white",
            width: "18px",
            textAlign: "center",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          AI
        </div>
      </div>
    ),
    { ...size }
  );
}
