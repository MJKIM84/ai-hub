# 결정 기록 (DECISIONS)

운영 전환 작업(2026-09-25~)에서 사람 확인 없이 내린 결정과 이유를 한 줄씩 남긴다. 사람이 다시 검토할 만한 것은 [BUILD_ASSUMPTIONS.md](BUILD_ASSUMPTIONS.md) 에도 [가정]으로 추가한다.

| # | 날짜 | 분류 | 결정 | 이유 |
|---|---|---|---|---|
| D-001 | 2026-09-25 | 1-1 원문 열람 진단 | 외부 열람 차단은 셸 스크립트만이 아니라 에이전트 웹 조회 도구(WebFetch)까지 같은 이그레스 프록시에서 막힌다고 판정했다 | curl 과 헤드리스 `claude -p` WebFetch 가 ref.gs1.org·arxiv.org·nist.gov·design.ros2.org·doi.org·crossref·openalex·wikipedia 등에서 같은 CONNECT 403(프록시 거부)을 냈다 |
| D-002 | 2026-09-25 | 1-1 원문 열람 진단 | raw.githubusercontent.com 은 셸과 에이전트 WebFetch 모두 열리고, github.com 페이지와 API 는 세션 저장소 범위 밖이라 막힌다. 웹 검색(WebSearch)은 서버 측이라 동작한다 | VDA5050 원문(raw) 200·208KB, gs1/EPCIS README 200, 헤드리스 WebFetch 가 VDA 5050 첫 제목을 읽음. github.com/VDA5050 은 403 |
| D-003 | 2026-09-25 | 1-1 원문 열람 | 원문 열람은 스크립트가 아니라 에이전트 WebFetch 로 하고, 공식 문서가 GitHub 에 있는 출처는 raw.githubusercontent.com 경로로 연다. 그 밖의 출처는 사람이 inbox/sources/ 에 넣은 파일로 연다 | 에이전트 도구가 열 수 있는 유일한 경로이며, 공식 저장소 원문이므로 원문 열람으로 인정할 수 있다 |
| D-004 | 2026-09-25 | 비용 | 비용 증가의 주원인은 호출마다 새로 쓰는 프롬프트 캐시(10만~27만 토큰)와 스토리텔러의 전체 페이지 재출력(최대 8.6만 출력 토큰)으로 판단했다 | 드라이런 응답의 usage: cache_read 는 Claude Code 기본 시스템 프롬프트(약 5~9천 토큰)만 적중했다 |
