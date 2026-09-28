import React from "react";
import { initializeVisitorSession } from "./visitorSession";
import ReactDOM from "react-dom/client";
import App from "./App";
import "@fontsource/noto-sans-kr/400.css";
import "@fontsource/noto-sans-kr/500.css";
import "@fontsource/noto-sans-kr/600.css";
import "@fontsource/space-grotesk/500.css";
import "@fontsource/space-grotesk/600.css";
import "./styles.css";
const root = ReactDOM.createRoot(document.getElementById("root")!);
root.render(<p role="status">작업 공간을 여는 중…</p>);
initializeVisitorSession()
  .then((session) =>
    root.render(
      <React.StrictMode>
        {session.mode === "personal_api" && (
          <aside className="visitor-banner" aria-label="개인 체험 공간">
            <strong>내 체험 공간</strong> · 다른 방문자와 작업·API 키가
            분리됩니다.
            <span>
              {" "}
              {new Date(session.expires_at! * 1000).toLocaleTimeString(
                "ko-KR",
                { hour: "2-digit", minute: "2-digit" },
              )}
              까지 사용 · 필요한 결과는 내려받아 보관하세요.
            </span>
          </aside>
        )}
        <App />
      </React.StrictMode>,
    ),
  )
  .catch((error) =>
    root.render(
      <main className="session-error">
        <h1>체험 공간을 열지 못했습니다</h1>
        <p role="alert">{error.message}</p>
        <button onClick={() => location.reload()}>다시 시도</button>
      </main>,
    ),
  );
