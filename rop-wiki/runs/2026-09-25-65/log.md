# 실행 로그 2026-09-25-65

- 2026-09-25 15:56:03 KST [준비] 실행 시작 (date=2026-09-25 run_id=2026-09-25-65 resume=없음 step=전체 run_type=track area=자동 track=floorplan-recognition)
- 2026-09-25 15:56:03 KST [준비] 웹 도구 점검 생략(--skip-probe): 기존 probe.json 사용
- 2026-09-25 15:56:03 KST [준비] 웹 도구 점검: web_search_available: true · web_fetch_available: false
- 2026-09-25 15:56:03 KST [준비] 부분 열람 모드: 일반 웹 페이지 열람은 차단, GitHub 공식 저장소 원문(raw.githubusercontent.com)과 inbox 원문만 열람 — 출처별 원문 열람 표시·신뢰도 상한 적용
- 2026-09-25 15:56:04 KST [준비] 결과: 성공 · 소요 1초 · web_search_available: true · web_fetch_available: false · 부분 열람 모드(fetch_mode: mirror_only)
- 2026-09-25 15:56:04 KST [대상 선정] 결과: 성공 · 소요 0초 · track · 6. 지도·공간·위치 모델
- 2026-09-25 15:56:15 KST [리서치 에이전트] 프롬프트 저장: runs/2026-09-25-65/prompts/research.md (484,916자, 규칙은 시스템 프롬프트 researcher-061e717d5a1d.md)
- 2026-09-25 16:04:01 KST [리서치 에이전트] 호출 완료(시도 1): 턴 33 · 7분 47초 · 비용 $6.0042 · subtype success
- 2026-09-25 16:04:01 KST [리서치 에이전트] 저장: runs/2026-09-25-65/research.json
- 2026-09-25 16:04:02 KST [형식 검증] 리서치 산출물 검사: 출처 24건 중 원문 열람 7건 · 신뢰도 상한 적용 2건
- 2026-09-25 16:04:02 KST [형식 검증]   - 출처 ref-031: data/source_texts 의 원문 텍스트(data/source_texts/ref-031.txt)가 있어 fetched true(github_raw)(에이전트 표시는 인정하지 않음 — inbox 열람 표시가 있으나 data/source_texts 에 원문 텍스트가 없다)
- 2026-09-25 16:04:02 KST [형식 검증]   - 출처 ref-651: 원문 열람 표시를 인정하지 않음 — 연 파일(https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Capability%20Description/1/0/README.md)은 공식 산출물(정본 페이지 본문 아님)이다 — 정본 문서의 원문 열람으로 치지 않는다. 연 파일을 github.com/…/blob/… URL 의 별도 출처로 인용하면 원문 열람으로 인정된다. fetched false 로 둔다
- 2026-09-25 16:04:02 KST [리서치] 예산 점검: 예산 안
- 2026-09-25 16:04:02 KST [리서치] 결과: 성공 · 소요 7분 58초 · 예산 안
- 2026-09-25 16:04:02 KST [내용 검증 에이전트] 프롬프트 저장: runs/2026-09-25-65/prompts/verification1.md (536,267자, 규칙은 시스템 프롬프트 verifier-e64d9bdc3472.md)
