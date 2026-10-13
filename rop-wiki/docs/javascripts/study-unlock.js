// 스터디 잠금 해제 뒤 mkdocs-material 의 본문 구성 요소(mermaid 다이어그램, 코드 복사 단추 등)를 다시 붙인다.
// mkdocs-encryptcontent-plugin 은 복호화가 끝나면 window 에 "encryptcontent_event" 를 보낸다.
window.addEventListener("encryptcontent_event", function () {
  if (window.document$ && typeof window.document$.next === "function") {
    window.document$.next(document);
  }
});
