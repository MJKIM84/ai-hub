# 대상 선정 규칙 검증(운영 전환 1-7) — 시뮬레이션 기록

- 일시: 2026-09-25
- 방법: 위키 전체를 작업용 복사본(scratchpad/selsim)에 복사한 뒤 상태를 조작하고 `python3 pipeline/select_target.py --date <날짜> --run-id <id> --stdout --no-side-effects` 로 선정 결과만 확인했다. 실제 위키와 실행 이력은 바꾸지 않았다.
- 조작한 상태: 28개 세부영역을 모두 `published` 로 바꿈. 세부영역 3번에 가짜 보류 실행 3건(runs/parked/2026-09-20-01·21-01·22-01, area_deep_dive)을 둠.

| # | 날짜(요일) | 추가 조작 | 선정 결과 | 확인한 규칙 |
|---|---|---|---|---|
| 1 | 2026-09-26(토) | 없음 | track · nl-task-chatbot · 질문 q1-01~q1-03 · 제외 영역 3 | 트랙 실행일(화·목·토), 트랙 가중 순환(실행이 가장 적은 트랙), 3회 연속 보류 영역 제외 |
| 2 | 2026-09-29(화) | 없음 | track | 트랙 실행일 |
| 3 | 2026-09-30(수) | 없음 | weekly_review(7번째 실행) | 매 7번째 실행 주간 정리 |
| 4 | 2026-09-28(월) | 가짜 weekly_review 게시 실행 1건 추가(8번째 실행이 되게) | category_link · 대분류 A · 제외 영역 3 | 소속 세부영역 4개가 모두 채워진 첫 대분류의 연결 절 채우기(cycle1 다음, cycle2 앞) |
| 5 | 2026-09-28(월) | 대분류 7개 페이지를 published 로 | topic · 세부영역 9 · 점수 48 = 경과일 4 + 열린 질문 2 + 빈 매트릭스 칸 42 + 우선 가중치 0 − 최근 감점 0 · 제외 영역 3 | 2주기 점수식 선정 |

- 3회 연속 보류 제외는 1·4·5번 모두에서 `excluded_areas: [3]` 과 근거 문장 "3회 연속 보류로 제외한 영역: 3. 처리능력·거점·설비 계획" 으로 확인했다.
- 트랙 단계 전환은 실제 실행에서 단계 완료가 아직 나오지 않아 퍼블리셔 함수 단위 테스트로 확인했다(`pipeline/checks/test_pipeline_ops.py` 의 `test_stage_transition_advances_and_records`, `test_stage_transition_last_stage_marks_done`). 확인한 것: current_stage 갱신, 이전 단계 "완료", 새 단계 "진행 중", 마지막 단계 뒤 트랙 status done, 변경 이력 1건.
