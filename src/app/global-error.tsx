"use client";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <html lang="ko">
      <body style={{ margin: 0, backgroundColor: "#0a0a0f", color: "#fff", fontFamily: "system-ui, sans-serif" }}>
        <div style={{
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}>
          <div style={{ textAlign: "center", padding: "24px" }}>
            <div style={{ fontSize: "48px", marginBottom: "16px" }}>🚨</div>
            <h1 style={{ fontSize: "24px", fontWeight: "bold", marginBottom: "8px" }}>
              심각한 오류가 발생했습니다
            </h1>
            <p style={{ color: "#a1a1aa", marginBottom: "32px", maxWidth: "400px" }}>
              서비스에 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.
            </p>
            <button
              onClick={reset}
              style={{
                padding: "12px 24px",
                borderRadius: "12px",
                border: "none",
                background: "linear-gradient(to right, #00D4FF, #A855F7)",
                color: "#fff",
                fontWeight: 600,
                fontSize: "16px",
                cursor: "pointer",
              }}
            >
              다시 시도
            </button>
          </div>
        </div>
      </body>
    </html>
  );
}
