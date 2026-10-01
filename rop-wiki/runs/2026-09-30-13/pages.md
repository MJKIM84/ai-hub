# 스토리텔러 산출 2026-09-30-13

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md | draft | 영역 심화: 3~11절 신규 작성, 13절 각주 정의 15건, 프런트매터 related_areas·tags·confidence·sources·last_run 채움(1차 조건부 승인 수정 15건 반영). 2차: 3절 첫 문장을 태그 없는 연결 문장으로, 4절 도입 문장의 [사실] 태그 제거, 9절 '상용 예로'를 '6절에서 예로'로 고침 |
| create | docs/topics/2026/2026-09-30-area37-s6.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차: '국내 상용 예로'를 '국내 예로(연구 과제 페이지 기준)'로 고침 |
| create | docs/topics/2026/2026-09-30-area37-s8.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "8. 대표 연구와 자료" 절을 옮겼다(2차 재실행에서 변경 없음) |
| create | docs/topics/2026/2026-09-30-area37-s4.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "4. 핵심 개념과 용어" 절을 옮겼다. 2차: 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 뗀 연결 문장으로 바꿈 |
| create | docs/topics/2026/2026-09-30-area37-s10.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다. 2차: 짝 엔진을 번호와 이름으로 표기, 39. 운영 성과 측정·개선 항목의 '실제 소요 시간' 드리프트 수정 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 37. 관제 화면·실행 기록 | 영역 심화: 3~11절 신규 작성(Open-RMF 시각화·작업 상태·로그 스키마, VDA 5050 시각화 토픽, MCAP, ISA-101, 설명 가능한 표시 연구, 병원 사례), 1차 조건부 승인 수정 15건과 2차 수정 6건 반영 | run 2026-09-30-13
- 홈 최근 업데이트: 2026-09-30 — 37. 관제 화면·실행 기록: 영역 심화로 3~11절을 처음 작성(지도 위 통합 상태 표시, 작업 상태·로그 스키마와 기록 재생, 설명 가능한 표시 연구, 병원 배송 이력 사례)
- 대분류 최근 업데이트: 2026-09-30 — 37. 관제 화면·실행 기록: 영역 심화 초안(Open-RMF·VDA 5050·MCAP·ISA-101 정리, 설명 가능한 표시는 연구 단계, 현장 사례는 병원 협약 1건)
- 세부영역 최근 업데이트: 2026-09-30 — 37. 관제 화면·실행 기록: 3~11절 신규 작성, 새 열린 질문 4건, 신뢰도 low

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 설명 가능한 다중 에이전트 경로 찾기 | Explainable Multi-Agent Path Finding (Explainable MAPF) | 여러 에이전트의 충돌 없는 경로를 찾으면서, 궤적이 서로 겹치지 않는 시간 구간 이미지 몇 장만으로 사람이 계획의 안전을 눈으로 확인할 수 있게 하는 경로 계획 문제다. | 37, 27 | ref-1173 |
| new | HMI 철학 | HMI Philosophy (ISA-TR101.01) | ISA-101 계열이 기술 보고서 ISA-TR101.01-2022로 다루는 HMI 설계 원칙 문서다. | 37, 38 | ref-1176 |
| new | 로그 재생 | Log Playback | 타임스탬프가 붙은 기록 데이터를 기록 시각 순서대로 다시 흘려 보내며 시간축을 탐색·가감속해 과거 시점의 상태를 다시 보는 기능이다. | 37, 36, 43 | ref-1172, ref-1171 |
| new | 상황 인식 | Situation Awareness (SA) | 운영자가 임무 환경의 상황을 파악하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다. | 37, 31 | ref-1175 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1165 | Open Robotics (open-rmf/rmf_visualization) | rmf_visualization — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_visualization |
| ref-302 | Open Robotics (open-rmf/rmf-web) | rmf-web — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web |
| ref-111 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-1168 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_log.json (Task Event Log) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json |
| ref-1169 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json |
| ref-031 | VDA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0) | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-1171 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 오픈소스 문서 | high | https://mcap.dev/spec |
| ref-1172 | Foxglove | Playback — Foxglove Documentation | 벤더 문서 | medium | https://docs.foxglove.dev/docs/visualization/playback |
| ref-1173 | Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022) | Conflict-Based Search for Explainable Multi-Agent Path Finding | 논문 | medium | https://arxiv.org/abs/2202.09930 |
| ref-477 | Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 |
| ref-1175 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ |
| ref-1176 | ISA (International Society of Automation) | ISA-101 Series of Standards | 표준 | medium | https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards |
| ref-1177 | 현대자동차그룹 로보틱스랩 | PROJECTS — Robot Fleet Management (NARCHON) | 벤더 문서 | medium | https://robotics.hyundai.com/projects/research/view.do?seq=102 |
| ref-1178 | 네이버클라우드 | ARC brain 개요 - 사용 가이드 | 벤더 문서 | medium | https://guide.ncloud-docs.com/docs/arc-brain-overview |
| ref-1179 | 아주경제 | 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 | 기사 | low | https://www.ajunews.com/view/20250407084333272 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? | 37, 21 | 열림 | — |
| new | — | 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가? | 37, 31 | 열림 | — |
| new | — | 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? | 37, 59 | 열림 | — |
| new | — | 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? | 37, 38 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 작업 대상 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 병원 | 수행 자원 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 병원 | 완료·인계 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) | 표준 | ISA(International Society of Automation) | 37, 38 | ref-1176 | https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards |
| Open-RMF rmf_visualization | 오픈소스 | Open Robotics (open-rmf) | 37, 15, 22 | ref-1165 | https://github.com/open-rmf/rmf_visualization |
| Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) | 오픈소스 | Open Robotics (open-rmf) | 37, 38, 43 | ref-1168 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json |

## 추가 조사 요청

- 5절: 물류창고·제조 공장·상업 시설·가정·실외·기타 현장에서 로봇 관제 화면·실행 기록을 운영에 쓴 사례(여섯 항목을 채울 근거) — 현재 병원 1건(협약 단계 보도)뿐이다.
- 5절: 한림대학교의료원 병원 배송 사례의 시작 조건·제약·예외·성과와 실제 운영 여부 — 2025-04-07 보도 이후 운영 결과 자료가 필요하다.
- 7절: ISO 11064(관제실 인간공학 설계) 각 부의 범위 — 발행 기관 원문을 열지 못해 넣지 못했다.
- 8절: Chen 외(2018) SAT 논문 원문 열람 — 실험 시스템(IMPACT 등)과 투명성 수준별 수행 결과를 확인해야 [사실]로 쓸 수 있다.
- 11절 oq-131: RoboCup Logistics League 경기 기록을 객체 중심 이벤트 로그(OCEL)로 만든 연구 등 플릿 실행 기록을 시나리오로 바꾸는 공개 형식 근거.
- 10절: 작업 실제 소요 시간(시작·완료 시각) 기록 필드와 성과 지표 산출 방식을 담은 자료 — 39. 운영 성과 측정·개선 연결을 구체화하려면 필요하다.
- 전반: 핵심 사실(Open-RMF 스키마, VDA 5050 토픽, Roldán 외 결과)이 모두 단일 출처라 독립 교차 확인 자료가 필요하다.

## 이행한 수정 지시

- f8 강등·재서술 — 4절·8절에서 [추정]으로 쓰고 'NP-난해임을 보인 뒤'를 빼고 '선행 연구가 제안한 시간 구간 이미지 설명 개념을 받아 CBS의 제약 트리와 A* 탐색에 설명 가능성 제약을 더한 XG-CBS를 제안하고 계획 시간과 설명 가능성의 절충을 분석했다'로 고쳤다.
- f9 강등·축약 — 4절·8절에서 [추정]으로 쓰고 'SAT 모델을 세 연구 프로그램(자율 분대원, 사람과 여러 하위 로봇의 중재자, 계획 추천 에이전트)에 적용했고 공유 이해와 신뢰 보정에 효과적이라고 정리했다'로 줄였으며 IMPACT·두 시스템·수행 향상 문구는 넣지 않았다.
- ref-477 원문 미열람 표시 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 항목에 source_unopened: true 를 넣었다.
- f10 수치 제외 — 8절에 SAGAT·NASA-TLX 수치를 쓰지 않고 상황 인식·부하 순서, 가상현실 묶음 차이 p=0.042, 예측 요소 효과 비유의와 기존 인터페이스 부하의 수치상 증가만 썼다.
- f12 재서술 — 6절에서 '적용처로 건물·상업 시설' 구절을 빼고 연동 설비를 '엘리베이터·자동문·스크린도어 등', 운영 환경을 '실내외 환경의 층별·존별 트래픽 관리'로 적었으며 [추정] 벤더 주장을 병기했다.
- 5절 상업 시설 제외 — f12를 적용 사례로 쓰지 않고 6절·9절 벤더 예로만 썼으며 site_matrix_updates 에 상업 시설 칸을 넣지 않았다.
- 5절 병원 사례 — 2025-04-07 보도 기준 협약·개발 계획 단계이고 운영 결과가 확인되지 않았음을 밝히고, 시작 조건·제약·예외·성과 칸을 '미확인'으로 두었으며, 물류창고·제조 공장·상업 시설·가정·실외·기타 사례는 찾지 못했다고 적었다.
- f16 재서술 — 3절에서 f9 근거의 '투명할수록 수행이 나아진다' 구절을 빼고, f10 구절을 'Roldán 외가 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었다'로 바꾸었으며 [추정]을 유지했다.
- f19 연결 수정 — 10절과 프런트매터 related_areas 에서 64. 상업 시설을 뺐다.
- 벤더 주장 병기 — f7(Foxglove)·f12(나콘)·f13(ARC brain)을 쓴 6·7·9절의 모든 문장·표 칸에 [추정] 벤더 주장을 함께 적었다.
- ref-031 재사용 확인 — 입력의 참고문헌 목록(docs_tree 기준)에 ref-1079가 등록돼 있지 않아 재사용할 수 없으므로 각주·sources 에 브리프 id ref-031을 쓰고 reference_updates 에 넣었으며, summary 에 이전 실행 ref-1079 와 같은 URL 임을 적어 퍼블리셔가 합칠 수 있게 했다.
- 용어 '상황 인식' 축약 — 지각·이해·예측 3단계 설명을 빼고 '운영자가 임무 환경의 상황을 파악하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다'로 glossary_updates 와 4절에 썼다.
- 용어 'HMI 철학' 축약 — 정의를 'ISA-101 계열이 기술 보고서 ISA-TR101.01-2022로 다루는 HMI 설계 원칙 문서'로 줄이고 내용 설명을 뺐다.
- ref-1179 제목 수정 — '(제목은 검색 결과 기준)'을 지우고 '현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다'로 각주와 reference_updates 에 썼다.
- 11절 열린 질문 — oq-131은 열림으로 유지하고(open_question_updates 에 상태 변경을 내지 않음), open_questions_new 4건을 open_question_updates 에 new 로 등록하고 11절에 적었다.
- 2차: 짝 엔진 표기 — 분리 페이지 s10 의 11. 채팅으로 실제 상황 시뮬레이션 재현 항목에서 '짝 엔진은 33·36번 영역이다'를 '짝 엔진은 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현이다'로 고쳤다.
- 2차: '상용' 표현 삭제 — 분리 페이지 s6 의 '국내 상용 예로'를 '국내 예로(연구 과제 페이지 기준)'로, 세부영역 9절의 '상용 예로 든 나콘·ARC brain·Foxglove'를 '6절에서 예로 든 나콘·ARC brain·Foxglove'로 고쳤고 [추정]과 '벤더 주장' 병기는 그대로 두었다.
- 2차: 39. 운영 성과 측정·개선 연결 드리프트 — 분리 페이지 s10 의 해당 항목을 '작업 상태 값, 처음·현재 추정 소요 시간, 로그 항목의 시각 기록이 성과 지표의 원자료가 될 수 있다'로 고쳤다.
- 2차: 3절 첫 문장 — '좌우한다' 단정과 [의견] 태그를 빼고 태그 없는 연결 문장 '관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.'로 바꿨다(outline 요약도 함께 고침).
- 2차: 4절 도입 문장 — 세부영역 4절 첫 문장과 분리 페이지 s4 의 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 떼고 태그 없는 연결 문장 '관제 화면과 실행 기록에 관련된 개념을 정리한다.'로 바꿨다.
- 2차: ref-031 요약·보고 문구 — reference_updates 의 ref-031 summary 에서 '참고문헌 목록에 ref-1079 가 없어 새 id 로 낸다' 구절을 지우고 '이전 실행 2026-09-30-10 의 ref-1079 와 같은 URL 이다.'만 남겼으며, fixes_applied 의 ref-031 항목을 실제로 쓴 id(ref-031)로 고쳤다.
