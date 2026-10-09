# 스토리텔러 산출 2026-10-09-23

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-2-document-types.md | draft | q2-02·q2-03·q2-05 답함(신뢰도 낮음), 3절 q2-03의 AMR 샘플 미발견 문장을 MiR·Clearpath 샘플로 대체, q2-05 소제목 신설, 4~6·9절 갱신, 7절 반영 제안 추가, 후속 질문 q3-10. 2차: 단계 상태 줄을 열린 질문 2건·답한 질문 5건으로 고치고, 새 각주 정의를 8절로 옮기고 ref-1408 기관 표기를 참고문헌과 맞췄다 |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | draft | v0.4 → v0.5: 근거 문서 속성 '언어(원본 / 번역 구분)' 추가(f16·f17·f20), 속성 '적용 구성'은 6절 질문에 합침. 2차: H1·머리 단락·4절 도식·3절·5절을 v0.5와 샘플 11건에 맞추고 ref-1408 기관 표기를 참고문헌과 맞췄다 |
| update | docs/tracks/manual-capability-ontology/document-type-matrix.md | draft | 4절 공개 문서 샘플 4건 → 11건(AMR 4건 포함), 'AMR 샘플 미발견' 문장 대체, 3절에 두산 웹 매뉴얼 사양 표·UR 별도 오류 코드 문서 메모, 8절 이력. 2차: 머리 상태 줄을 '공개 문서 샘플: 11건'으로 고치고, 3절 메모의 추론 문장에 태그를 붙이고, 새 각주 정의를 7절로 옮겼다 |
| update | docs/tracks/manual-capability-ontology/index.md | draft | 6절 살아있는 산출물 링크: 온톨로지 초안 v0.5, 문서 유형 매트릭스 샘플 11건, 백로그 q2-02·q2-03·q2-05 답함·q3-10 등록, 아이디어 페이지 갱신 반영. 2차: 머리 상태 줄의 현재 단계를 단계 2. 로봇 문서 유형과 정보 구조 조사로 고쳤다 |
| update | docs/ideas/robot-capability-ontology.md | draft | 3절에 근거 형태별 문서 이해·데이터시트 추출·매뉴얼 질의응답 측정 자료, 4절에 AMR 공개 문서 접근·재사용 조건과 근거 문서의 언어·판 기록 필요(실행 2026-10-09-23) 추가. 2차: 3절 끝 추론 문장에 태그를 붙이고 ref-1408 기관 표기를 참고문헌과 맞췄다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 매뉴얼 기반 로봇 기능 온톨로지 단계 2 | q2-02·q2-03·q2-05 답함(신뢰도 낮음), AMR 등 공개 문서 샘플 7건 추가, 온톨로지 v0.4 → v0.5(근거 문서 속성 언어), 후속 질문 q3-10 | run 2026-10-09-23
- 홈 최근 업데이트: 2026-10-09 — 매뉴얼 기반 로봇 기능 온톨로지 단계 2: 기능 정보 형태별 추출 난이도·공개 문서 샘플(AMR 포함)·언어·판에 따른 정보 차이 질문에 답하고 능력 온톨로지 초안을 v0.5로 올림
- 대분류 최근 업데이트: 2026-10-09 — 5. 로봇 능력·작업 표현(트랙 단계 2): 제조사 문서의 접근·재사용 조건과 언어·판·구성에 따른 정보 차이 정리, 근거 문서에 언어(원본 / 번역 구분) 속성 추가
- 세부영역 최근 업데이트: 2026-10-09 — 5. 로봇 능력·작업 표현: 트랙 단계 2 실행 2026-10-09-23이 근거 문서의 언어·판 기록 필요를 확인(능력 온톨로지 초안 v0.5), 4. 이기종 로봇 등록·45. 문서·도면·장면 이해·57. 자산·소프트웨어 수명주기 관리 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 원본 설명서 | Original Instructions | 제조자 또는 그 대리인이 내용을 확인한 언어판 설명서로, EU 기계류 지침은 이 판에 'Original instructions'를, 다른 언어로 옮긴 판에 'Translation of the original instructions'를 표기하게 한다. | 4, 5, 59 | ref-1408 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-1397 | Mobile Industrial Robots (MiR) | MiR250 HW 2.0 SW 2.x — Product documents | 벤더 문서 | medium | https://mobile-industrial-robots.com/product-documents/mir250-hw-20-sw-2-v1 |
| ref-1398 | Mobile Industrial Robots (MiR) | MiR1350 Pallet Lift HW 1.0 SW 2.x — Product documents | 벤더 문서 | medium | https://mobile-industrial-robots.com/product-documents/mir1350-pallet-lift-hw-10-sw-2-v1 |
| ref-1399 | Universal Robots A/S | User Manuals (PolyScope X 10.13 landing page) | 벤더 문서 | medium | https://www.universal-robots.com/manuals/EN/HTML/SW10_13/Content/Landingpages/WebPolyX/Usermanual.htm |
| ref-1400 | Universal Robots A/S | Copyright and disclaimers (SW 5.26 manual) | 벤더 문서 | medium | https://www.universal-robots.com/manuals/EN/HTML/SW5_26/Content/prod-fu-tp/fu-tp-copyright-and-disclaimers.htm |
| ref-1401 | Clearpath Robotics by Rockwell Automation | IndoorNav User Manual — Getting Started | 벤더 문서 | medium | https://docs.clearpathrobotics.com/docs_indoornav_user_manual/getting_started |
| ref-1402 | Clearpath Robotics by Rockwell Automation | IndoorNav User Manual — Appendix A: IndoorNav ROS 2 API | 벤더 문서 | medium | https://docs.clearpathrobotics.com/docs_indoornav_user_manual/api |
| ref-1403 | Clearpath Robotics by Rockwell Automation | OutdoorNav User Manual 1.0.0 — API Overview | 벤더 문서 | medium | https://docs.clearpathrobotics.com/docs_outdoornav_user_manual/1.0.0/api/api_overview |
| ref-1404 | OMRON Robotics | Download center | 벤더 문서 | medium | https://robotics.omron.com/browse-documents/?dir_id=125 |
| ref-1405 | Boston Dynamics | Spot SDK Release Notes | 벤더 문서 | medium | https://dev.bostondynamics.com/docs/release_notes |
| ref-1406 | 두산로보틱스 | Doosan Robotics User Manual 3.2.1 — Manipulator (M/H Series) | 벤더 문서 | medium | https://manual.doosanrobotics.com/en/user-manual/3.2.1/1-m-h-series/manipulator |
| ref-1407 | 두산로보틱스 | 두산로보틱스 사용자 매뉴얼 3.2.1 — M1013 | 벤더 문서 | medium | https://manual.doosanrobotics.com/ko/user-manual/3.2.1/1-m-h-series/m1013 |
| ref-1408 | European Parliament and Council (legislation.gov.uk 게재본, EUR-Lex 원문 미열람) | Directive 2006/42/EC on machinery — Annex I | 정부·연구기관 | high | https://www.legislation.gov.uk/eudr/2006/42/annex/I |
| ref-1409 | Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks) | MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations | 논문 | high | https://arxiv.org/abs/2407.01523 |
| ref-1410 | Riedler, M., & Langer, S. | Beyond Text: Optimizing RAG with Multimodal Inputs for Industrial Applications | 논문 | medium | https://arxiv.org/abs/2410.21943 |
| ref-1411 | Gun, J., & Oksanen, T. (Technical University of Munich) | Agri-Query: A Case Study on RAG vs. Long-Context LLMs for Cross-Lingual Technical Question Answering | 논문 | medium | https://arxiv.org/abs/2508.18093 |
| ref-1412 | Singh, R. 외 | A Multimodal Manufacturing Safety Chatbot: Knowledge Base Design, Benchmark Development, and Evaluation of Multiple RAG Approaches | 논문 | medium | https://arxiv.org/abs/2511.11847 |
| ref-1072 | Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access) | Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0 | 논문 | medium | https://arxiv.org/abs/2403.17209 |
| ref-1071 | Groß, J., & Heidrich, J. | AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning | 논문 | medium | https://arxiv.org/abs/2609.07334 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내에서 판매·설치되는 산업용 로봇·이동로봇의 사용설명서를 한국어로 제공해야 한다는 규정이 자율안전확인 고시나 다른 법령에 있으며, 원본과 한국어 번역판의 판이 다를 때 어느 쪽을 근거로 삼는가? | 59, 4 | 열림 | — |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| EU 기계류 지침 2006/42/EC 부속서 I 1.7.4.1 (설명서 언어·원본·번역 표기) | 프레임워크 | European Parliament and Council (legislation.gov.uk 게재본) | 4, 59 | ref-1408 | https://www.legislation.gov.uk/eudr/2006/42/annex/I |
| MMLongBench-Doc (긴 문서 이해 벤치마크) | 평가 프로그램 | Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks) | 45, 54 | ref-1409 | https://arxiv.org/abs/2407.01523 |

## 추가 조사 요청

- 단계 2 페이지 3절 q2-02: 로봇 매뉴얼(사양 표·오류 코드표·작업 영역 도면·코드 예제)을 대상으로 근거 형태별 추출 정확도를 측정한 자료 — 현재 답은 범용 문서 벤치마크 유추이며 코드 예제 형태는 측정 자료가 없다(q3-01·q5-01·oq-226과 함께 조사).
- 단계 2 페이지 3절 q2-05: 규정 (EU) 2023/1230 의 설명서 언어·디지털 제공 조항 원문(EUR-Lex) — 이번에 열지 못해 대체 규정 기준의 원본·번역 요건이 미확인이다.
- 단계 2 페이지 3절 q2-05: 같은 기종의 언어판·판 사이 실제 사양 값 차이를 문서끼리 대조한 근거(MiR250 포르투갈어판 1.4·1.5 판 파일 대조 등) — 현재 판 불일치는 링크 경로 관찰뿐이다.
- 문서 유형 매트릭스 4절·단계 2 q2-07: 국내 AMR 제조사의 공개 매뉴얼·API 문서와 이용 조건 — 한국어 검색 2회에서 찾지 못했다.
- 문서 유형 매트릭스 3절: 사용자 매뉴얼·오류 코드표(Universal Robots Error Codes 문서 내부 형태 포함)·치수도·도면 행 — 단계 2 완료 조건 충족에 필요하다.
- 파이프라인 담당 요청: config/tracks/manual-capability-ontology.yaml 의 current_stage 가 1로 남아 있어 트랙 개요 5절 자동 단계 진행 표가 단계 2를 '대기'로 보여 준다. 이번 실행의 대상 단계(2)와 맞추어야 한다(2차 검증 참고 사항). 이번 재실행에서는 절 밖 머리 줄(단계 상태 줄·매트릭스 상태 줄·초안 H1·트랙 개요 현재 단계)을 고치기 위해 다섯 페이지를 모두 페이지 전문(content)으로 보냈다.

## 이행한 수정 지시

- f9 — 단계 2 페이지 3절 q2-02의 종합 문장에서 HTML 을 난이도 순위 근거로 쓰지 않고, GPT-4o 의 근거 형태 사이 정확도가 44~50으로 고르고 표(50.0)가 가장 높으며 차트·이미지 저하는 공개 모델·OCR 파이프라인에서 크다는 문장으로 고쳐 썼다.
- q2-02 답의 한계 — 3절 {#q2-02} 본문과 4절 남은 불확실성에 측정 자료가 범용 문서 벤치마크(로봇 매뉴얼 미포함)이고 코드 예제 형태는 측정 자료에 없다는 점을 명시했다.
- f12 — '승인을 받게 한다'를 '양식 제출을 요구하며, 제출 즉시 접근을 안내하면서도 검토 중·거절 상태 메시지를 둔다'로 고쳐 3절 q2-03과 매트릭스 4절 OMRON 행에 썼고 [추정] 벤더 주장을 유지했다.
- f21 — 'UR20 에도 두 계열 매뉴얼을 따로 둔다'를 빼고, 모델별(UR Series·e-Series) 매뉴얼 나열·시리즈마다 두 소프트웨어 계열 사용 가능·주소에 SW5_26·SW10_13 판과 언어가 들어 있다는 축소 문장([추정] 벤더 주장)으로 3절 q2-05에 썼다.
- f20 — 'V2 판 매뉴얼은 별도의 레거시 사이트(v2-manual)로 분리한다'로 고쳐 3절 q2-05에 썼다.
- f16 — 'Original instructions' 표기 대상을 '제조자 또는 그 대리인이 확인한 언어판'으로 고쳐 3·4절, 온톨로지 초안 2절, 아이디어 페이지, 용어집에 썼고, 본문에 legislation.gov.uk 게재본·EUR-Lex 원문 미열람을 밝히고 참고문헌 기관 표기에도 같은 사실을 넣었다.
- f15 — 통합 수준 문서를 계정 뒤에 두는 경향에 두산로보틱스의 ROS 2·API 문서 공개 예외를 병기하고, 명시적 허락 확인 결론은 q2-03 답이 아니라 백로그 q6-07의 부분 근거로 넘긴다고 3절 q2-03과 아이디어 페이지에 썼다.
- f22·f11·f23 — 계단 사용 금지 같은 주행 동작과 IndoorNav·OutdoorNav 자율주행 API 를 분류 원문 19장 '로봇 자체 지능·제어'의 연계 대상으로 짧게 적고 문서 판·접근 조건 사례로만 썼다([의견] 문장 두 곳).
- 단계 5 새 질문(근거 형태별 평가 세트) — backlog_updates 에 넣지 않았고, 3절 q2-02 끝 남은 부분에 q3-01·q5-01·oq-226을 연결했으며 5절에 미등록 이유를 적었다.
- 온톨로지 초안 — 근거 문서 속성 '언어(원본 / 번역 구분)'만 2절에 반영(근거 f16·f17·f20)하고 프런트매터 ontology_version 과 track_updates.ontology_draft_version 을 0.5로 맞췄다. '적용 구성'은 6절에 근거 f17·f18·f22·f24·f26과 함께 '근거 문서의 단위와 버전'·q6-02 질문에 합쳤다. H1·auto 상태 줄은 절 밖이라 프런트매터 값으로 동기화되도록 요청을 남겼다.
- AMR 샘플 대체 — 단계 2 페이지 3절 q2-03과 매트릭스 4절의 'AMR 제조사의 공개 매뉴얼 샘플은 찾지 못했다' 문장을 MiR·Clearpath 샘플(벤더 주장)로 대체하고, 4절 표에 MiR250·MiR1350 Pallet Lift·Clearpath IndoorNav·OutdoorNav·Universal Robots·OMRON·두산 웹 매뉴얼 7행을 이용 조건과 함께 더했다.
- q2-07 — 상태를 바꾸지 않았다. 단계 2 페이지 2절 표의 q2-07은 '열림' 그대로이고 backlog_updates 에 넣지 않았다.
- 단계 2 페이지 4절 — 실행 2026-10-09-22에서 미확인으로 남긴 VDA 5050 팩트시트 뒷부분(versions·batteryCharging·loadPositions)을 이번 raw 원문 열람으로 확인했다는 결론 항목을 넣고 옛 미확인 항목을 뺐다.
- f6 — 3절 q2-02 본문과 아이디어 페이지에 arXiv 2511.11847 의 v1 2025-11-14 제출·v2 2026-02-10 개정판을 기준판 표기로 남기고 참고문헌 요약에도 적었다.
- 2차: 단계 2 페이지 상태 줄 — 페이지 전문(content)으로 보내며 H1 아래 줄을 '열린 질문: 2건 · 답한 질문: 5건'으로 고쳤다(2절 표의 답함 5건·열림 2건과 일치).
- 2차: 온톨로지 초안 v0.5 표기 — 페이지 전문으로 보내며 H1 을 '능력 온톨로지 초안 (v0.5)'로 고치고, 머리 단락 앞에 v0.5 문장(실행 2026-10-09-23, 근거 문서 속성 언어(원본 / 번역 구분) 추가, 적용 구성은 6절에 합침)을 더했다. 4절 mermaid 하위 그룹 표시 이름을 'v0.5 개념'으로, 도식 아래 문장을 '근거 문서의 속성(문서 유형·이용 조건·언어)'로, 3절을 'v0.3·v0.4·v0.5에서는 관계 변경이 없다'로, 5절을 '샘플 4건을 올렸고 실행 2026-10-09-23에서 11건으로 늘렸으나'로 고쳤다. 6절 첫 문장에도 v0.5를 넣었다. auto 상태 줄 마커 안은 퍼블리셔 영역이라 손대지 않았다.
- 2차: 문서 유형 매트릭스 머리 상태 줄 — 페이지 전문으로 보내며 '공개 문서 샘플: 11건'으로 고쳤다(4절 표 11행과 일치). 8절 이력의 이번 실행 행에도 머리 줄 샘플 수 갱신을 적었다.
- 2차: 트랙 개요 머리 상태 줄 — 페이지 전문으로 보내며 '현재 단계: 단계 2. 로봇 문서 유형과 정보 구조 조사'로 고쳤다. 단계 전환은 미승인이라 stage_transition 은 넣지 않았다.
- 2차: index_updates.area_recent — '4·45·57번 영역'을 '4. 이기종 로봇 등록·45. 문서·도면·장면 이해·57. 자산·소프트웨어 수명주기 관리 반영 제안'으로 고쳤다.
- 2차: ref-1408 각주 기관 표기 — 단계 2 페이지·온톨로지 초안·아이디어 페이지의 각주 정의를 'European Parliament and Council (legislation.gov.uk 게재본, EUR-Lex 원문 미열람)'으로 고쳐 reference_updates 의 org 와 같은 문자열로 맞췄다. 단계 2 페이지와 매트릭스의 새 각주 정의는 페이지 끝에서 각 페이지의 출처 절(8절·7절) 안으로 옮겼다.
- 2차: 태그 누락 2곳 — 매트릭스 3절 '실행 2026-10-09-23 메모'의 추론 문장을 '…별도 문서에 있는 것으로 보인다. [추정][^ref-1399]'로 끊어 태그를 붙이고 이어지는 미조사 처리 문장은 따로 두었다. 아이디어 페이지 3절 끝 문장 '…아직 유추 수준이다'에 [추정][^ref-1409][^ref-1412][^ref-1072]를 붙였다.

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-2-document-types.md
- 온톨로지 초안 버전: 0.5
- 트랙 로그 항목: 답한 질문: q2-02(근거 형태별 측정은 범용 문서 벤치마크 유추, 코드 예제 미측정), q2-03(AMR 샘플 MiR·Clearpath와 접근·재사용 조건, 법적 판단 아님), q2-05(언어판·문서 판·하드웨어/상위 모듈 구성 세 축) — 셋 다 신뢰도 낮은 답 / 새 질문: q3-10(f19, 언어판 선택·차이 검출, 단계 3). 근거 형태별 평가 세트 질문(단계 5)은 q2-02·q3-01·q5-01·oq-226 중복으로 등록하지 않음 / 온톨로지 변경: v0.4 → v0.5: 근거 문서 속성 '언어(원본 / 번역 구분)' 추가(f16·f17·f20, 실행 2026-10-09-23). 속성 '적용 구성(하드웨어·소프트웨어 판, 상위 모듈·옵션 장비)'은 거부 — 6절 '근거 문서의 단위와 버전'·q6-02 질문에 합침 / 완료 조건 평가: 미충족(부족: 문서 유형 매트릭스 사용자 매뉴얼·오류 코드표·치수도·도면 행과 대부분 칸 미조사, 국내 AMR 샘플 없음, 막힌 질문 q2-06·q2-07) / 세부영역 반영 제안: 45. 문서·도면·장면 이해, 4. 이기종 로봇 등록, 57. 자산·소프트웨어 수명주기 관리 3건 / 다음 실행 제안: q2-06, q2-07(매트릭스 사용자 매뉴얼·오류 코드표 행과 함께). 참고: 트랙 정의 current_stage 가 1로 남아 있어 개요 자동 표와 맞지 않음(파이프라인 담당)
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 2(q2-06·q2-07), 답함 5, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-02 | 답함 | docs/tracks/manual-capability-ontology/stage-2-document-types.md#q2-02 | — | — | — |
| q2-03 | 답함 | docs/tracks/manual-capability-ontology/stage-2-document-types.md#q2-03 | — | — | — |
| q2-05 | 답함 | docs/tracks/manual-capability-ontology/stage-2-document-types.md#q2-05 | — | — | — |
| q3-10 | 열림 | — | 제조사 매뉴얼의 언어판 사이에 판 번호·내용이 어긋날 때(번역판이 원본보다 오래된 판인 경우) 능력 정의 초안의 추출 근거로 어느 언어판을 고르고, 언어판 사이 차이를 어떻게 검출하는가? (q2-05 에서 파생) | 3 | f19 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 45 | 8. 대표 연구와 자료 | 근거 형태별 문서 이해 정확도(MMLongBench-Doc, GPT-4o 텍스트 46.3·표 50.0·이미지 44.1, 공개 모델·OCR 파이프라인의 차트·이미지 저하), 산업 문서 다중 모달 RAG(Riedler·Langer 2024), 데이터시트→자산관리셸 추출(Xia 외 2024 유효 생성률 62~79%, AAS-RAIL 30.4~52.4% 상대 개선), 매뉴얼 질의응답(Singh 외, UR5e 포함 86.66%)과 교차 언어 기술 질의응답(Agri-Query). 매뉴얼 해석은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에 적용되는 방법으로 연결(근거: 실행 2026-10-09-23 f1~f6·f25). |
| 4 | 6. 대표 접근법과 기술 | 등록 때 확보할 제조사 문서의 접근 조건(MiR·Clearpath 통합 문서 로그인, OMRON 양식 제출, 두산 ROS 2·API 공개 예외)과 재사용 표기(UR 서면 승인 없는 복제 금지 등, 벤더 주장), 근거 문서에 언어·원본 여부·적용 판을 함께 기록할 필요(이 위키의 종합, 근거: 실행 2026-10-09-23 f10~f15·f26). 재가공 허용 여부는 트랙 q6-07로 연결. |
| 57 | 6. 대표 접근법과 기술 | 소프트웨어 판에 따라 기능이 추가·폐기되는 사례(Spot SDK 릴리스 노트, 벤더 주장)와 문서 판의 유지 중단 표시(Clearpath OutdoorNav 1.0.0), VDA 5050 팩트시트 구성 블록의 하드웨어·소프트웨어 판 키-값 배열(versions) — 능력 정의를 적용 판과 함께 관리할 필요(근거: 실행 2026-10-09-23 f22·f23·f24·f26). |
