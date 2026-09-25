# 스토리텔러 산출 2026-09-25-37

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | draft | q2-01 답함(2·3·4·5·6·8·9절 작성), 후속 질문 2건(q2-05·q2-06), q2-04 행 추가, 상태 줄 갱신. seed 단계 페이지를 처음 채우고 H1 아래 상태 줄을 바꿔야 해서(1차 수정 지시) patches 대신 content 로 보냄 |
| update | docs/tracks/nl-task-chatbot/task-model-draft.md | draft | 초안 v0.3 → v0.4: 상황 속성에 공간 노드 참조 추가(확정 유지), 업무 기한·우선순위 값 원천과 기한 필드 부재 메모(초안 → 확정), 작업 요구 수정 거부를 6절 질문으로. H1 버전 표기를 바꿔야 해서 content 로 보냄 |
| update | docs/ideas/nl-task-chatbot.md | draft | 4절에 '필요한 데이터 항목과 원천' 소절 작성(q2-01), 표준·형식 목록·평가 데이터는 미조사로 명시 |
| update | docs/tracks/nl-task-chatbot/index.md | draft | 6. 살아있는 산출물 링크: 초안 v0.4, 아이디어 페이지 4절 작성 반영(현재 단계는 트랙 정의 current_stage 1 그대로라 상태 줄 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 자연어 업무 지시 챗봇 단계 2 | q2-01 답함(로봇 인터페이스·업무 시스템 필드와 정보 항목 원천 대응), 초안 v0.3 → v0.4, 후속 질문 2건 | run 2026-09-25-37
- 홈 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 단계 2: 채팅 지시에 필요한 정보 항목을 Open-RMF·VDA 5050·ISA-95·EPCIS 필드에 대응(로봇 인터페이스에 기한 필드 없음), 초안 v0.4
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 자연어 업무 지시 챗봇 트랙이 배정 입력이 될 작업 요청 필드(기한 필드 없음)와 팩트시트 적재 명세를 정리하고 7. 관련 표준·프레임워크·오픈소스 반영을 제안
- 세부영역 최근 업데이트: 2026-09-25 — 자연어 업무 지시 챗봇 트랙 단계 2(q2-01): Open-RMF 작업 요청·배송 기술과 VDA 5050 팩트시트 필드를 7. 관련 표준·프레임워크·오픈소스에 반영 제안

## 용어집 갱신

- 없음

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-768 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__delivery.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__delivery.json |
| ref-769 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__payload_transfer.json |
| ref-770 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/place.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json |
| ref-771 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema |
| ref-772 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphNode.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphNode.msg |
| ref-773 | Martins, P. H., Custódio, L., & Ventura, R. | A deep learning approach for understanding natural language commands for mobile service robots | 논문 | medium | https://arxiv.org/abs/1807.03053 |
| ref-774 | Rana, K. 외 | SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning | 논문 | medium | https://arxiv.org/abs/2307.06135 |
| ref-775 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 논문 | medium | https://arxiv.org/abs/2604.05427 |
| ref-776 | Mecalux | Mecalux integrates generative AI into Easy WMS | 벤더 문서 | low | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 표준 | medium | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL |
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 표준 | medium | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf |
| ref-360 | arXiv 2508.19114 저자(미확인) | DELIVER: A System for LLM-Guided Coordinated Multi-Robot Pickup and Delivery using Voronoi-Based Relay Planning | 논문 | medium | https://arxiv.org/abs/2508.19114 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 단계 2 페이지 3절 q2-01·초안 업무 개념의 완료 조건: Open-RMF 작업 상태 스키마(ref-111)와 EPCIS 이벤트로 업무 완료 조건을 어떻게 표현할 수 있는지 원문 확인이 필요하다(이번 실행에서 미재확인).
- 단계 2 페이지 3절: VDA 5050 3.0.0 상태 메시지의 적재물(loads) 필드 세부가 필요하다(대상 화물 식별 단위 비교, q2-06).
- 아이디어 2 4절 완료 조건: 분해한 작업·배정 결과를 표현하는 표준·형식 목록 비교(q2-02)와 지시–정답 작업 쌍 평가 데이터(q2-03)를 조사해야 한다.
- 용어집: '사람 확인 루프(Human-in-the-Loop)'의 정의를 뒷받침할 출처가 필요하다(이번 실행은 정의 출처가 없어 등록 보류).
- 국내 자료: 자연어 물류 작업 지시의 정보 항목을 정리한 한국어 자료를 추가 검색해야 한다(이번 한국어 검색 1회).
- 파이프라인 담당 요청: 차등 갱신(patches)으로는 H1 제목(초안 버전 표기)과 H1 아래 단계 상태 줄을 바꿀 수 없어, 이번 실행은 단계 2 페이지(seed)와 업무 분해·배정 설계 초안을 content 로 보냈다. 트랙 초안 H1 버전·단계 상태 줄을 patches 로 갱신할 방법(예: 프런트매터 값에서 코드가 생성)을 정해 주기 바란다.

## 이행한 수정 지시

- f10 분리 — 단계 2 페이지 3절에서 'DELIVER 는 경량 LLaMA3 로 픽업·배송 위치를 뽑아 다중 로봇 픽업·배송에 넘긴다'만 [사실]로, '검색 요약 범위에서 화물 식별·기한 추출은 확인되지 않았다(원문 미열람)'를 별도 [추정] 문장으로 썼다.
- VDA 5050 기준판 — f4·f5·f6 을 쓴 단계 2 페이지·초안·아이디어 페이지 문장마다 '3.0.0(공식 저장소 main 브랜치, 확인일 2026-09-25)'을 같은 문장에 적었다.
- f7 일부 열거 — 자재 데이터형을 '자재 정의 id·로트 id·수량·단위 등(자재 클래스·하위 로트 id 도 있음, 모두 선택)'으로 쓰고 기준일을 노드셋 모델 발행일 2024-01-31 로 적었다.
- f13 — 단계 2 페이지와 아이디어 4절에서 [추정]·'벤더 주장'을 병기하고 발행일 미확인으로 두었으며, WMS(상위 업무 시스템) 제품 기능이자 ROP 의 연계 대상 사례로 서술했고, 1. 주문·업무 시스템 연계·18. 사람–로봇 협업·운영 인터페이스 반영 제안도 같은 틀로 냈다.
- f12 — ISO 13482 가 개인 돌봄 로봇 안전 표준이고 230개 과업·AI2-THOR 30개 시나리오 평가가 저자 보고이며 물류 현장 대상이 아님을 같은 문단에 적고, 25. 안전·위험 관리와 27. AI·학습·적응과 모델 운영 양쪽에 7절 연결과 반영 제안을 냈다.
- f14·f16 대리 원천 — 단계 2 페이지 3절 q2-01 답 첫 단락과 4절 불확실성에 VDA 5050 팩트시트·Open-RMF 건물 지도 그래프를 대리 원천으로 썼다고 적고, 완료 조건 표현 원천(작업 상태 스키마·EPCIS 이벤트) 미확인을 4절 불확실성에 적었다.
- 기존 열린 질문 연결 — 단계 2 페이지 3절에서 f15 를 oq-019, f16 을 oq-029, f17 을 oq-007·oq-023 에 링크로 연결했고 새 일반 열린 질문은 만들지 않았다(open_question_updates 빈 배열).
- 원문 미열람 표시 — ref-015·ref-360·ref-773·ref-774·ref-775·ref-776 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, 원문을 연 ref-125·ref-031·ref-228·ref-130·ref-768~ref-772 에는 붙이지 않았다.
- 기관·저자 — reference_updates 와 각주에서 ref-773 을 'Martins, P. H., Custódio, L., & Ventura, R.', ref-775 를 'Obi, I., … & Min, B.-C.(Purdue University SMART Lab)', ref-774 를 'Rana, K. 외'로 적었다.
- 용어 보류 — '사람 확인 루프(Human-in-the-Loop)'를 glossary_updates 에 넣지 않고 정의 출처 확보를 additional_research_requests 에 적었다.
- 상황 수정 승인 — 초안 상황 행의 주요 속성에 '장소 표현과 그 해석 결과인 공간 노드 참조(지도 id, 경유점 이름 또는 번호)'를 짝으로 더하고 근거 칸에 finding f3·f4 (실행 2026-09-25-37)와 ref-770·ref-772·ref-771 을 달았으며 상태 확정을 유지하고, 이름 대응 규칙은 6절 질문(q2-01, q2-05, oq-029)으로 두었다.
- 업무 수정 승인 — 기한·우선순위의 '(단계 2에서 확정)'을 지우고 값 원천 후보 '채팅 지시 / 업무 시스템 작업 지시(ISA-95 EndTime·Priority)'(f7, ref-130)를 적었으며, 로봇 인터페이스 기한 필드 부재를 [사실](ref-125·ref-771), 작업 모델의 기한 보유를 f15 근거 [추정]으로 쓰고, 완료 조건의 '(단계 2에서 확정)'은 유지하고 상태를 초안 → 확정으로 바꿨다.
- 작업 요구 수정 거부 — 개념 목록 표에 반영하지 않고 6절에 '작업 요구에 적재물 식별과 적재물 유형·치수·중량을 더해 팩트시트 loadSets 와 대조할 것인가 — 능력 온톨로지 초안과 대조 후 결정(근거 f2·f5·f6·f17, 관련 q2-01)' 질문을 두었다.
- 버전 0.4 — 초안 H1 '(v0.4)', 프런트매터 ontology_version '0.4', track_updates.ontology_draft_version "0.4" 를 맞추고 1절 버전 요약 문단에 v0.4 변경(상황·업무 승인, 작업 요구 거부)을 적었다. H1 변경을 위해 초안은 content 로 보냈다.
- q3-01 중복 — 기한 변환 규칙 질문을 backlog_updates 에 새 id 로 넣지 않고 단계 2 페이지 5절 표 아래에 'q3-01 에 근거 f15 로 연결'로 적었다.
- 새 질문 두 건 — 장소 이름 사전(q2-05, origin f16)과 화물 식별 단위(q2-06, origin f17)를 단계 2 로 backlog_updates 에 등록하고 단계 2 페이지 2절·5절에 적었다.
- 단계 2 페이지 2·3·4절 — q2-01 을 상태 답함, 답한 실행 id 2026-09-25-37, 답 위치 '#q2-01' 로 적고 3절에 '### q2-01 필요한 정보 항목과 그 원천 {#q2-01}' 소제목을 두었으며, 4절에 핵심 답(f14 등)이 이 위키의 추론(신뢰도 low)이고 교차 확인이 0건임을 명시했다.
- 단계 2 페이지 6절·상태 줄 — 완료 조건 두 행을 '미충족', 검증 판정 '미충족 · 미승인'으로 두고 표 아래를 '다음 단계로 전환: 아니오(아이디어 2 4절의 표준·형식 목록(q2-02) 미조사, 작업 모델 정보 항목 일부만 반영, 열린 질문 q2-02·q2-03·q2-04)'로 썼으며, 상태 줄을 '단계 상태: 진행 중 … 완료 조건: 미충족'으로 바꿨다(상태 줄 변경을 위해 seed 단계 페이지를 content 로 보냈다).
- 아이디어 4절 — '필요한 데이터 항목과 원천' 소절만 쓰고 표준·형식 목록 비교(q2-02)와 평가 데이터(q2-03)가 미조사임을 명시했으며, 항목–원천 대응 표 앞 문장에 이 위키가 구성한 표이며 [추정]임을 적었다.
- 세부영역 직접 수정 금지 — 13. 작업 배정 — MRTA, 1. 주문·업무 시스템 연계, 18. 사람–로봇 협업·운영 인터페이스 페이지는 pages 에 넣지 않고 area_reflection_proposals 로만 냈으며, 1. 주문·업무 시스템 연계 제안에서 f13 은 7절이 아닌 6. 대표 접근법과 기술의 제품 사례로 표시했다.
- docs/ideas/nl-task-chatbot.md: 각주 정의 8개를 참고문헌에서 만들어 붙임: ref-015, ref-031, ref-125, ref-130, ref-228, ref-769, ref-771, ref-776

## 트랙 갱신

- 단계 페이지: docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.4
- 트랙 로그 항목: 답한 질문: q2-01(f1~f18; 로봇 인터페이스 필드 f1~f5, 로봇 능력 대리 원천 f6, 업무 시스템 f7·f8, 지시 해석 연구 f9~f12, WMS 채팅 제품 f13(벤더 주장), 항목–원천 대응 f14, 기한 공백 f15, 장소 이름 대응 f16, 화물 식별 단위 f17, 13. 작업 배정 — MRTA 질문 연결 f18) / 새 질문: q2-05(f16), q2-06(f17); 기한 변환 규칙 분담은 q3-01 과 중복이라 등록하지 않고 근거 f15 로 연결 / 온톨로지 변경: v0.3 → v0.4: 개념 '상황 (Situation)' 장소 표현에 해석 결과 '공간 노드 참조(지도 id, 경유점 이름 또는 번호)' 짝 추가(f3·f4, 상태 확정 유지), 개념 '업무 (Job)' 기한·우선순위 값 원천 후보(채팅 지시 / ISA-95 EndTime·Priority)와 로봇 인터페이스 기한 필드 부재 메모(f1·f4·f7·f15, 초안 → 확정); 거부: '작업 요구 (Task Requirement)' 적재물 속성 추가(능력 온톨로지 초안과 충돌 여부 미확인, 6절 질문) / 완료 조건 평가: 미충족(부족: 아이디어 2 4절의 표준·형식 목록(q2-02) 미조사, 작업 모델 정보 항목 일부 반영, 열린 질문 q2-02·q2-03·q2-04) / 세부영역 반영 제안: 13. 작업 배정 — MRTA, 1. 주문·업무 시스템 연계(2건), 6. 지도·공간·위치 모델, 18. 사람–로봇 협업·운영 인터페이스, 25. 안전·위험 관리, 27. AI·학습·적응과 모델 운영 7건 / 다음 실행 제안: q2-02, q2-04, q2-05
- 개요 진행 현황: 단계 1 진행 중(트랙 정의의 현재 단계) — 이번 실행은 CLI 지정으로 단계 2 질문 q2-01 에 답함. 단계 2: 열린 질문 5, 답함 1, 완료 조건 미충족. 단계 전환 없음

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-01 | 답함 | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md#q2-01 | — | — | — |
| q2-05 | 열림 | — | 지시 속 현장 장소 용어(예: 3층 출하 대기장, 2번 도크)와 공간 그래프 경유점 이름·지도 id·WMS 로케이션 코드를 대응시키는 이름 사전은 어떤 형식으로 두고 누가 관리하는가? (q2-01 에서 파생) | 2 | f16 |
| q2-06 | 열림 | — | 채팅 지시의 '대상 화물'을 품목 단위(sku·수량)로 받을지 적재 단위(loadId·SSCC)로 받을지, 둘 사이 대응은 어느 시스템에서 가져오는가? (q2-01 에서 파생) | 2 | f17 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 13 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF 작업 요청 스키마(필수 category·description, 선택 가장 이른 시작 시각·우선순위, 기한 필드 없음)와 배송 작업 기술(픽업·하역 사건의 장소·적재물 sku·수량), VDA 5050 3.0.0 팩트시트 적재 명세·지원 동작이 배정 입력이 되는 구조(단계 2 실행 2026-09-25-37, f1·f2·f6). 채팅 지시만으로는 기한·우선순위·화물 제약이 비기 쉬워 업무 시스템과 팩트시트에서 보완해야 한다는 추론(f15·f18, [추정])을 SCM 질문과 연결. |
| 1 | 7. 관련 표준·프레임워크·오픈소스 | OPC UA for ISA-95 작업 제어 노드셋(2024-01-31)의 작업 지시는 작업 지시 id 만 필수이고 종료 시각·우선순위·자재 요구가 선택 필드여서, 채팅 지시의 기한·대상 화물 원천 후보가 된다(f7). 로봇 인터페이스에는 기한 필드가 없어 작업 모델이 기한을 보유해야 한다는 추론(f15, [추정], oq-019 연결). |
| 1 | 6. 대표 접근법과 기술 | 상위 업무 시스템(WMS) 쪽 제품 사례: Mecalux Easy WMS 의 대화형 비서가 긴급 주문 출고·통로 잠금 해제를 채팅 요청으로 실행하되 실행 전 요약·확인을 받는다([추정] 벤더 주장, f13). ROP 기능이 아니라 연계 대상의 사례로만 서술. |
| 6 | 7. 관련 표준·프레임워크·오픈소스 | Open-RMF 장소 스키마(경유점 이름·번호 또는 경유점·방향 객체)와 건물 지도 그래프 노드(x·y, 이름, 파라미터), VDA 5050 3.0.0 노드 위치의 mapId(f3·f4). 지시 속 현장 장소 용어를 이 식별자로 옮기려면 이름 대응 정보가 필요하다는 추론(f16, [추정], oq-029·트랙 질문 q2-05). |
| 18 | 6. 대표 접근법과 기술 | 채팅 지시 실행 전 확인 방식 두 가지: WMS 대화형 비서의 동작·영향 항목 요약 후 채팅 확인(Mecalux, [추정] 벤더 주장, WMS 쪽 연계 대상 사례, f13)과 자연어 명령의 안전 속성 추출 뒤 결정적 승인·거부 게이트(SafeGate, ISO 13482 개인 돌봄 로봇 표준 기반, 저자 보고·물류 현장 미평가, f12). 27. AI·학습·적응과 모델 운영과 함께 연결. |
| 25 | 6. 대표 접근법과 기술 | SafeGate(arXiv 2604.05427, 2026-04)는 자연어 명령에서 안전 관련 속성을 뽑아 ISO 13482 기반 결정적 판정으로 실행을 승인·거부하고 불변 조건·가드·중단 조건의 작업 안전 계약으로 분해한다(f12). ISO 13482 는 개인 돌봄 로봇 표준이고 평가는 저자 보고이며 물류 현장 대상이 아님을 병기. |
| 27 | 6. 대표 접근법과 기술 | LLM 지시 해석이 뽑는 인자와 접지 방법: DELIVER 는 픽업·배송 위치 추출(화물·기한 추출은 요약 범위에서 미확인, f10), SayPlan 은 3D 장면 그래프 의미 탐색으로 계획을 접지(f11, 저자 보고), SafeGate 는 안전 속성 추출·결정적 게이트(f12). 적용 대상인 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결. |
