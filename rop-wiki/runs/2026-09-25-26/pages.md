# 스토리텔러 산출 2026-09-25-26

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md | draft | q1-03 답함(3절 소제목 신설, 신뢰도 low), 4절 결론·불확실성(f22 이번 실행에서도 미확인), 후속 질문 q4-06, 완료 조건 표·이력 갱신, 상태 줄 갱신(상태 줄이 절 밖에 있어 patches 대신 전체 content로 보냄) |
| update | docs/ideas/nl-task-chatbot.md | draft | 3절: q1-03 미조사 문장 두 곳을 채팅·음성 지시의 확인·승인 방식 비교(작업자 대상 동작 단위 확인 대 로봇 대상 확인 절차 미확인)로 교체 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6절 아이디어 2 항목의 'q1-03 미조사' 문구를 이번 실행 결과로 교체(상태 줄은 마지막 트랙 실행 2026-09-25·현재 단계 단계 1 그대로라 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 1 | q1-03 답함(채팅·음성 지시 제품의 확인·승인 방식, 신뢰도 low), 후속 질문 q4-06 등록, 아이디어 2 3절 갱신 | run 2026-09-25-26
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 1: 채팅·음성 지시 제품의 확인·승인 방식(q1-03)을 조사했다. 작업자 대상 음성 피킹은 체크 디지트·수량 응답으로 동작을 확인하지만, 로봇 대상 자연어 지시 제품의 실행 전 확인 절차는 공개 자료에서 확인되지 않았다.
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA(자연어 업무 지시 챗봇 트랙 단계 1): 채팅·음성 지시 제품의 확인·승인 방식 비교와 후속 질문 q4-06 등록.
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 트랙 단계 1에서 채팅·음성 지시 제품의 확인·승인 방식(q1-03)을 조사했다. 반영 제안은 18. 사람–로봇 협업·운영 인터페이스 대상이다.

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 음성 피킹 | Voice-Directed Picking (Voice Picking) | 시스템이 작업자에게 갈 위치와 피킹할 수량을 음성으로 지시하고 작업자가 짧은 음성 응답으로 동작을 확인하는 창고 피킹 방식이다. | 18 | ref-438, ref-439 |
| new | 위치 체크 디지트 | Location Check Digit | 보관 위치 라벨에 붙은 짧은 확인용 숫자로, 작업자가 이를 말하거나 입력해 올바른 위치에 있음을 시스템에 확인시키는 데 쓰인다. GS1 식별 키(SSCC·GTIN 등)의 끝자리 검증 숫자(체크 디지트)와는 다른 뜻이다. | 18 | ref-438, ref-439 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-438 | Lucas Systems | Voice-Directed Warehousing - Solutions \| Lucas Systems | 벤더 문서 | low | https://www.lucasware.com/voice-directed-warehousing/ |
| ref-439 | USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.) | System and method for generating and updating location check digits (US 8868519) | 정부·연구기관 | medium | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519 |
| ref-440 | Amazon | Amazon unveils next-gen Proteus robot as part of €10 billion European investment in its fulfillment network | 벤더 문서 | low | https://www.aboutamazon.com/news/operations/amazon-proteus-robot-europe-investment-employee-support |
| ref-441 | The Robot Report | Proteus gets natural-language ability as Amazon expands European robot deployments | 기사 | low | https://www.therobotreport.com/proteus-gets-natural-language-ability-amazon-expands-europe-robot-deployments/ |
| ref-442 | InOrbit.AI | InOrbit RobOps Copilot - Bring AI power to robot operations | 벤더 문서 | low | https://www.inorbit.ai/robopscopilot |
| ref-443 | Locus Robotics | Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface) | 벤더 문서 | low | https://locusrobotics.com/locusone/automated-warehouse-software/user-interface |
| ref-444 | Aila Technologies | Locus Robotics leverages Aila's scanning to increase productivity (case study) | 벤더 문서 | low | https://www.ailatech.com/blog/case-study-locus-robotics/ |
| ref-445 | 뉴스핌 | 현대로템, 무인로봇 국책과제 2건 수주 | 기사 | low | https://www.newspim.com/news/view/20260526000361 |
| ref-177 | InOrbit.AI (RoboticsTomorrow 게재 보도자료) | InOrbit.AI Demonstrates the Future of Multi-Vendor Robot Orchestration and Physical AI at Automate 2026 | 벤더 문서 | low | https://www.roboticstomorrow.com/news/2026/06/22/inorbitai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai-at-automate-2026/26757/ |
| ref-178 | Formant (Business Wire 보도자료) | Formant F3 Brings Generative AI and Agentic Reasoning to Robot Ops | 벤더 문서 | low | https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 1 페이지 4절·아이디어 2 페이지 3절: 로봇 대상 자연어 지시 제품(Amazon 차세대 Proteus, InOrbit RobOps Copilot, Formant F3)의 해석 결과 실행 전 확인·승인 절차와 명령 권한 장치를 원문(제품 문서·기술 자료)으로 확인할 필요가 있다. 이번 결론은 검색 요약 범위의 관찰이라 신뢰도 low 에 머문다(q1-02 의 f22 와 함께).
- 특허 US 8868519 의 등록일과 발행 정보를 확인해 참고문헌 ref-439 의 발행일(현재 미확인)을 채울 필요가 있다.
- 국내 물류 현장에서 로봇·작업자에게 채팅·음성으로 일을 지시하는 제품과 그 확인 방식(한국 자료 우선 규칙). 이번 실행에서는 국방 과제(연계 대상)만 확인했다.
- 백로그 정리: q1-05 와 q1-06 이 같은 질문으로 중복 등록되어 있어 하나를 폐기 또는 병합해야 한다(검증 지적, 트랙 백로그 담당 요청).
- 단계 1 완료 조건: 지시 분해 접근의 유형 목록을 업무 분해·배정 설계 초안에 반영하려면 검증이 승인할 수 있는 초안 변경 제안(근거 finding 포함)이 다음 트랙 실행에서 필요하다.

## 이행한 수정 지시

- ref-439 기관·출원일 — reference_updates 의 기관을 'USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.)'로 고치고 발행일은 null(각주 '미확인')로 두었으며, 요약과 단계 1 페이지 3절·아이디어 2 페이지 3절 본문에 '출원 2011-05-27(검색 요약 기준)'을 적었다.
- f1 주장 범위 — 단계 1 페이지 3절 q1-03, 4절 결론, 아이디어 2 페이지 3절에서 [사실] 문장을 음성 피킹 일반 관행(위치·할 일 음성 지시, 체크 디지트·수량 응답 확인)으로 한정하고, Lucas Systems Jennifer 는 별도 문장에 [추정] 벤더 주장으로 썼다.
- f3·f4·f6 벤더 주장 병기 — 단계 1 페이지 3절 q1-03 과 아이디어 2 페이지 3절의 Locus·Amazon·InOrbit 문장 모두에 [추정] 벤더 주장을 붙이고, 18. 사람–로봇 협업·운영 인터페이스 반영 제안 요약에도 벤더 주장임을 적었다. InOrbit Connect 미션 연계는 '제품 페이지 요약 기준'으로 밝혔다.
- f4 기준일 — 두 페이지 모두 '2026-06-04(발표일, 검색 요약 기준)'로 적고 실험실 파일럿 단계·유럽 2027년 상반기 계획을 같은 문장에 두었다. 각주 발행일 2026-06 과 모순되지 않는다.
- f5·f7 부재 표현 — 확인·승인 절차를 찾지 못했다는 문장마다 '검색 요약 범위의 관찰이며 부재의 확인이 아니다'를 함께 썼다. 단계 1 페이지에서 f7 은 3절에 쓰지 않고 4절 남은 불확실성의 기존 f22 항목을 '이번 실행(2026-09-25-26)에서도 확인되지 않음'으로 갱신하는 데만 썼다.
- f8 연계 대상 — 단계 1 페이지 3절 '국내 사례' 한 줄로만 두고 문장 첫머리 '연계 대상:'과 국방 무인로봇 과제(산업통상부·국방과학연구소 발주)임을 밝혔다. 물류 제품 사례·아이디어 2 페이지·18. 사람–로봇 협업·운영 인터페이스 반영 제안에는 넣지 않았다.
- 원문 미열람 표시 — ref-438~ref-445 와 ref-177·ref-178 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙였고, reference_updates 의 신규 8건(재사용 2건 포함)에 source_unopened: true 를 넣었다.
- 용어집 — '체크 디지트'를 '위치 체크 디지트(Location Check Digit)'로 등록하고 GS1 식별 키 끝자리 검증 숫자와 다른 뜻이라는 문장을 정의에 덧붙였다. '음성 피킹(Voice-Directed Picking)'은 그대로 등록했다.
- 18. 사람–로봇 협업·운영 인터페이스 반영 제안 — area_reflection_proposals 의 절을 '6. 대표 접근법과 기술'과 '8. 대표 연구와 자료'로 냈고 세부영역 페이지는 고치지 않았다.
- 단계 1 페이지 2절·3절·상태 줄 — q1-03 행을 답함·2026-09-25-26·[#q1-03](#q1-03)으로 바꾸고, 3절에 '### q1-03 … {#q1-03}' 소제목을 두어 첫 단락에 답 신뢰도 low 와 그 이유를 밝혔으며, 상태 줄을 '열린 질문: 3건 · 답한 질문: 3건'으로 고쳤다(상태 줄이 절 밖이라 이 페이지는 전체 content 로 보냈다).
- 단계 1 페이지 6절 — 첫 행 '충족'·'충족(1차 예비, 2차에서 확정)', 둘째 행 '미충족'·'미충족 · 미승인', 표 아래 줄을 지시 문구 그대로 썼고 상태 줄의 완료 조건은 '미충족'을 유지했다.
- 아이디어 2 페이지 3절 — 첫 단락의 q1-03 미조사 문장과 절 끝의 '아직 조사되지 않음' 문장을 모두 없애고 f1·f2·f3·f4·f6·f7·f9 기반 소절 '채팅·음성 지시의 확인·승인 방식'과 이 위키가 직접 구성한 비교표를 두었다.
- 트랙 개요 6절 — 아이디어 2 항목의 q1-03 미조사 문구를 '작업자 대상 확인 방식 확인, 로봇 대상 제품의 확인 절차는 공개 자료에서 미확인'으로 고쳤다. 상태 줄(마지막 트랙 실행 2026-09-25, 현재 단계 단계 1. 선행 연구·제품 사례 조사)은 이미 지시 값과 같아 그대로 두었다.
- 새 질문 — backlog_updates 에 q4-06(단계 4, origin f9, 열림)을 등록하고 단계 1 페이지 5절 후속 질문 표에 추가했으며, 표 아래에 q4-01·q4-02 와 이어지지만 중복이 아니라는 메모를 붙였다.
- 업무 분해·배정 설계 초안 — pages 에 넣지 않고 ontology_draft_version 을 '0.2'로 유지했다. 확인(승인) 개념 질문은 초안을 고치지 않고 단계 1 페이지 4절 결론에서 f9 근거로 초안 6절 미해결 모델링 질문에 링크만 했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.2
- 트랙 로그 항목: 답한 질문: q1-03(f1·f2·f3·f4·f5·f6·f7·f8·f9, 답 신뢰도 low — 작업자 대상 동작 단위 확인은 확인, 로봇 대상 자연어 지시 제품의 실행 전 확인 절차는 공개 자료 검색 요약 범위에서 미확인) / 새 질문: q4-06(단계 4. 오해석 방지와 확인 절차, 근거 f9 — 두 확인 방식의 오류·부담 비교, q4-01·q4-02와 연결되나 중복 아님) / 온톨로지 변경: 없음(업무 분해·배정 설계 초안 v0.2 유지, 제안 없음) / 완료 조건 평가: 미충족(부족: 지시 분해 접근 유형 목록이 업무 분해·배정 설계 초안에 미반영; 아이디어 2 3절 비교는 1차 예비 충족) / 세부영역 반영 제안: 18. 사람–로봇 협업·운영 인터페이스 2건(6. 대표 접근법과 기술, 8. 대표 연구와 자료) / 다음 실행 제안: q1-04, q1-05·q1-06 중복 정리 후 하나
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 3, 답함 3, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-03 | 답함 | docs/tracks/nl-task-chatbot/stage-1-prior-work-and-products.md#q1-03 | — | — | — |
| q4-06 | 열림 | — | 작업자 음성 피킹의 체크 디지트·스캔처럼 동작 하나하나를 현장에서 확인받는 방식과, 자연어 지시의 해석 결과(작업·대상·로봇)를 배정 전에 요약해 확인받는 방식을 함께 둘 때 각각 어떤 오류를 잡고 확인 부담은 얼마나 늘어나는가? (q1-03 에서 파생) | 4 | f9 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 18 | 6. 대표 접근법과 기술 | 작업자에게 일을 지시하는 운영 인터페이스의 확인 방식: 음성 피킹은 체크 디지트·수량 같은 짧은 음성 응답으로 동작마다 확인한다([사실], ref-438·ref-439). 협업 피킹 로봇(Locus)은 화면으로 품목·위치·수량을 보여 주고 선택 기능으로 위치·용기 바코드 스캔 뒤 화면 확인을 받는다([추정] 벤더 주장, ref-443·ref-444). 로봇 대상 자연어 지시 제품은 해석 결과의 실행 전 확인 절차가 공개 자료에서 드러나지 않아(검색 요약 범위의 관찰, 부재의 확인 아님) 동작 확인과 지시 확인은 대상·시점이 다른 것으로 보인다([추정], 이 위키의 정리). |
| 18 | 8. 대표 연구와 자료 | 음성 지시 창고 작업 자료(Lucas Systems, 벤더 문서), 위치 체크 디지트 불일치 경고를 기술한 미국 특허 공보 US 8868519(양수인 VOCOLLECT, INC., 출원 2011-05-27), Locus Robotics 사용자 인터페이스와 Aila 사례(벤더 주장), 자연어 지시 로봇 사례로 Amazon 차세대 Proteus(2026-06-04 발표, 실험실 파일럿, 벤더 주장)와 InOrbit RobOps Copilot 제품 페이지(벤더 주장). 모두 원문 미열람. |
