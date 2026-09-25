# 스토리텔러 산출 2026-09-25-07

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | draft | corr-001 반영: 7절 VDA 5050 행을 현행판 3.0.0·2.0.0 병기로 고치고 열람 표시 수정, 3.0.0 pick·drop 완료 정의와 loads 필드 설명 추가. 11절 oq-007 보강(열림 유지). 13절 각주 ref-031·ref-032·ref-051·ref-052 추가. corr-002 거절(분류원문 보호, 1절 변경 없음) |
| create | docs/topics/2026/2026-09-25-area07-s7.md | draft | 자동 분리: 7. 화물·재고·자산 식별과 추적 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,570자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 7. 화물·재고·자산 식별과 추적 | corr-001 반영(7절 VDA 5050 현행판 3.0.0·2.0.0 병기, 두 판 모두 loads·loadId 정의, 열람 표시 수정), corr-002 거절(사유: 분류원문 보호), 11절 oq-007 보강(열림 유지), 용어집 VDA 5050 정의 수정 | run 2026-09-25-07
- 홈 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: corr-001 반영(VDA 5050 현행판 3.0.0 병기, 적재물 식별 보고가 두 판 모두에 있음), corr-002 거절(분류원문 보호)
- 대분류 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 7절 VDA 5050 행을 3.0.0(현행판)·2.0.0 병기와 공식 저장소 원문 확인 표시로 갱신(corr-001), 11절 oq-007 보강. corr-002 거절(분류원문 보호)
- 세부영역 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 7절 VDA 5050 3.0.0·2.0.0 병기와 열람 표시 수정(corr-001), 11절 oq-007 보강, 각주 4건 추가. corr-002 거절(분류원문 보호)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| update | VDA 5050 | VDA 5050 | 독일자동차산업협회(VDA)와 VDMA가 정한 이동로봇(AGV·AMR)과 상위 관제(fleet control) 사이의 통신 인터페이스 권고안이며 현행판은 3.0.0이다. | 5, 7, 9 | ref-031, ref-052 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 표준 | medium | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 표준 | medium | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-052 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/README.md |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 11절 oq-007: VDA 5050 3.0.0 명세 7장(메시지 명세) 이후를 열람해 loadId 형식 규정과 식별 결과가 지시한 loadId와 다를 때의 보고 규칙이 있는지 확인해야 한다(이번 열람 응답이 7장 앞에서 잘림).
- 11절 oq-007: 이전 실행 2026-09-25-03 f12의 3.0.0 loadId 문구('Set by fleet control or mobile robot …')가 명세의 어느 위치(action 파라미터 설명 등)에 있는지 확인이 필요하다.
- 7절 VDA 5050 행: 공식 저장소 2.0.0 태그 마크다운(RELEASE CANDIDATE)과 VDA 게시 PDF(ref-022)의 글자 단위 일치를 확인해야 열람 표시를 더 정리할 수 있다.
- 7절 현행판 표기·oq-005: VDA 5050 3.0.0의 정확한 발행일(2026-03-19 대 2026-04 보도자료)을 발행 기관 원문으로 확인해야 한다.
- 표준 목록의 VDA 5050 (3.0.0) 행 관련 영역에 7. 화물·재고·자산 식별과 추적을 더하고 참고문헌을 공식 저장소(ref-031)로 보강할지 다음 실행에서 판단이 필요하다.

## 이행한 수정 지시

- 7절 VDA 5050 행(corr-001) — 이름 칸을 'VDA 5050 3.0.0(현행판)·2.0.0'으로, 관계 칸을 '적재물 식별 보고(state 메시지의 loads·loadId, 두 판 모두 정의) [사실][^ref-031][^ref-051][^ref-022]'로 고쳤다.
- 7절 VDA 5050 행 출처 칸 — '원문 미열람'을 지시 문구('공식 저장소 main 원문 확인(ref-031·ref-051·ref-052). 2.0.0은 공식 저장소 태그 마크다운(RELEASE CANDIDATE 문구) 확인, VDA 게시 PDF(ref-022)는 원문 미열람·일치 미확인')로 바꿨다.
- f4 — 7절 표 아래 문단에 '3.0.0 명세 기준'임을 밝혀 pick·drop 완료 정의와 선택 파라미터를 [사실][^ref-031]로 썼고, 3·5·9절의 기존 ref-022 문장은 고치지 않았다.
- f5 — 7절에 '2026년 발행이며 정확한 날짜는 미확인(oq-005)'까지만 쓰고, 구역(zone) 개념 문장은 [사실][^ref-031][^ref-032]로 썼다.
- f6·f8 — [의견] 문장으로 본문에 싣지 않고 7절 편집과 corr-002 거절의 근거로만 썼다.
- 11절 oq-007 — 상태 '열림'을 유지하고 지시 문구대로 f7 보강 문장을 [추정][^ref-051]로 덧붙였으며 해결로 바꾸지 않았다(open_question_updates 없음).
- 1절 한 줄 정의 — 바꾸지 않았다(corr-002 거절, 1절 패치 없음).
- 13절 각주 — ref-031·ref-051·ref-052를 '기관, 제목, 미확인, URL, 접근일 2026-09-25' 형식으로, ref-032를 발행일 2026-04와 ' (원문 미열람)'으로 추가했고 ref-022의 ' (원문 미열람)'을 유지했으며, 프런트매터 sources에 ref-031·ref-032·ref-051·ref-052를 더했다.
- reference_updates — ref-051·ref-052를 source_unopened: false로 신규 등록하고, ref-032·ref-022는 source_unopened: true를 유지했으며 본문에서 쓰지 않은 ref-018·ref-021은 넣지 않았다.
- 용어집 VDA 5050 — glossary_updates(action: update)로 한 줄 정의를 지시 문구로 바로잡고 팩트시트는 규격 안의 한 메시지로 설명에서 구분했다(근거 ref-031·ref-052).
- 변경 이력·페이지 갱신 요약 — changelog_entry, diff_summary, index_updates에 corr-001 반영과 corr-002 거절(사유: 분류원문 보호)을 적었다.
- 분량 초과 자동 분리: 7. 화물·재고·자산 식별과 추적 본문 4,922자 > 기준 4,000자 → 1개 절을 주제 페이지로 옮김, 남은 본문 3,641자
