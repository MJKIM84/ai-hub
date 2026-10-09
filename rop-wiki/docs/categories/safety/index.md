---
title: "M. 안전"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-004, ref-031, ref-104, ref-159, ref-161, ref-286, ref-406, ref-417, ref-470, ref-472, ref-562, ref-563, ref-565, ref-567, ref-621, ref-945, ref-980, ref-1076, ref-1079, ref-1080, ref-1081, ref-1083, ref-1084, ref-1116, ref-1117, ref-1118, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-1180, ref-1181, ref-1214, ref-1241, ref-1242, ref-1249, ref-857, ref-700, ref-1253, ref-1254, ref-1255, ref-1256, ref-1257, ref-1258, ref-1259, ref-1260, ref-1261]
---

[홈](../../index.md) › M. 안전

# M. 안전

## 핵심 질문

여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

## 개요

위험성 평가, 안전 기능과 정지·재개, 사람 근접 안전, 비상 대응, 안전 표준·인증, 사고 조사. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **48. 안전·위험 관리** | 위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? | [48. 안전·위험 관리](safety-and-risk-management.md) | published |
| **49. 사람 근접 안전** | 사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 | 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? | [49. 사람 근접 안전](human-proximity-safety.md) | published |
| **50. 안전 표준·인증·사고 조사** | 안전 표준 적합성·인증, 사고 기록과 사후 조사 | 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? | [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

여러 장비가 각각 안전해도 함께 움직일 때 새로운 위험이 생길 수 있다. **로봇·사람·설비의 상호작용 전체**를 위험성 평가의 대상으로 삼아야 한다. [분류원문]

## 다른 대분류와의 연결

M. 안전의 세 세부영역 [48. 안전·위험 관리](safety-and-risk-management.md), [49. 사람 근접 안전](human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md)이 다른 16개 대분류와 어디서 만나는지를 대분류별로 정리한다. 근거는 게시된 세부영역·대분류 페이지의 검증된 주장과 이번 실행에서 확인한 출처이며, 다른 대분류 페이지에 이미 있는 연결은 같은 각주를 다시 쓰고 그 사실을 밝힌다.

이 절에서 비상정지 회로·보호 필드·무선 안전 정지 같은 안전 기능 자체는 로봇 제조사·통합자 몫의 연계 대상으로 적는다. ROP 몫은 안전 상태를 받아 작업을 보류·재배정하고 재개를 지시하는 범위로 한정한다. 승강기 모드 제어, 동시적 위치추정·지도작성(SLAM) 같은 로봇 자체 기능, 법령 해석과 적용 판단도 연계 대상이다.

### A. 기획·사업

[A. 기획·사업](../planning-and-business/index.md)과는 안전 책임의 분담, 표준 개정 일정, 실외 로봇의 보험 비용으로 만난다.

책임 분담에서는 48. 안전·위험 관리가 2. 사용 사례·요구·책임 범위와 만난다. ANSI/A3 R15.08 시리즈는 로봇 자체(1부), 산업용 이동로봇 시스템·적용의 통합(2부, 2023), 사용자의 산업용 이동로봇 적용 사용(3부, 2026)으로 나뉘어 제조사·통합자·사용자의 안전 책임을 부별로 다룬다. [사실][^ref-1254][^ref-1084] 통합자와 사용자의 의무가 따로 있으므로, 여러 제조사 로봇을 묶는 ROP 사업자가 현장마다 통합자 역할을 맡는지 사용자의 위험성평가를 지원하는 데 머무는지가 책임 범위 정의에 들어가야 할 것으로 보인다(열린 질문 oq-096). [추정][^ref-1254][^ref-1084][^ref-472]

표준 개정 일정에서는 50. 안전 표준·인증·사고 조사가 1. 기술·시장·업체 동향과 만난다. ISO 10218-1/-2 개정판은 2025-02에 나왔고, EN ISO 판의 참조는 2026-09-07 EU 관보에 실렸다. [사실][^ref-1116] ANSI/A3 R15.08-3 의 발행일은 A3 판매 페이지 기준 2026-04-23이고, 공개 발표 보도는 2026-10-04(Robotics 24/7)이다. [사실][^ref-1255][^ref-1256] ISO 13482 개정판은 2026-09-15 기준 최종 국제표준안(FDIS) 단계다(근거 페이지 원문은 열람하지 않았다). [사실][^ref-1117] 이를 종합하면 주요 로봇 안전 표준의 개정이 2025~2026년에 몰려 있는 것으로 보인다. [추정][^ref-1116][^ref-1255][^ref-1117]

비용·조달에서는 50. 안전 표준·인증·사고 조사가 3. 경제성·조달·사업 모델과 만난다. 2023-11-17 시행된 개정 지능형로봇법에 따라 보도에서 실외이동로봇을 운영하는 자는 보험(또는 공제)에 의무 가입해야 하고, 산업통상자원부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정해 보험상품 출시를 지원한다(기사 1건, 2023-11-16 보도 기준). [사실][^ref-1259] 실외 로봇 도입에서는 보험 가입과 인증 유지가 운영비 항목이 될 것으로 보인다. [추정][^ref-1259] 인증 단위가 로봇과 관제장치의 조합이므로, 관제를 맡는 ROP 사업자가 운영자 의무 범위에 드는지가 조달·계약 단계의 쟁점이 될 것으로 보인다. [추정][^ref-1259][^ref-980]

### B. 로봇 온톨로지

[B. 로봇 온톨로지](../robot-ontology/index.md)와는 로봇이 지금 관제를 받을 수 있는 상태인지, 어떤 안전 표준·인증을 지니는지를 표현하는 일로 만난다.

VDA 5050 3.0.0 의 운용 모드 가운데 관제가 로봇을 제어하는 것은 AUTOMATIC(관제가 완전히 제어)과 SEMIAUTOMATIC(관제가 제어하되 주행 속도는 사람–기계 인터페이스(Human-Machine Interface, HMI)가 조정)이고, INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 로봇을 제어하지 않는다. [사실][^ref-031] 따라서 6. 온톨로지 기반 시스템·로봇 연동의 실행 시점 조건 판단에 배터리·적재 상태와 함께 운용 모드와 안전 상태(비상정지·보호 필드 침범)를 넣어야, 관제가 제어권이 없는 로봇에 작업을 내리지 않을 것으로 보인다. [추정][^ref-031]

등록 정보 쪽에서는 로봇마다 R15.08 유형(A·B·C), 적용 안전 표준과 판, 인증 상태를 4. 이기종 로봇 등록의 등록 정보로 두면 표준 개정과 인증 범위를 배정·경로 제약으로 추적할 수 있을 것으로 보인다. [추정][^ref-1254][^ref-1116][^ref-980]

### C. 채팅 기반 구성·운영

[C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)과는 대화 지시가 로봇 동작으로 이어지기 전의 안전 검사로 만나며, 12. 채팅으로 업무 지시·오케스트레이션과 13. 대화형 기능의 신뢰·기반에 걸친다. 분류 원문 C. 채팅 기반 구성·운영 주석은 대화 결과를 실행 명령이 아니라 계획으로 보고 '사람이 확인·승인한 계획만 실행'하게 한다. 12. 채팅으로 업무 지시·오케스트레이션은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링을 대화로 쓰게 하는 기능이므로(분류 원문 C 주석), 아래 G. 계획·최적화 연결과 짝으로 읽는다.

Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트(SafeGate)와 작업 안전 계약을 두는 방법을 제안했다. [사실][^ref-417] Ravichandran 외의 RoboGuard 에서는 악성 프롬프트와 격리한 신뢰 기점 대규모 언어 모델(Large Language Model, LLM)이 미리 정한 안전 규칙을 시간 논리 제약으로 바꾸고, 제어 합성으로 계획과의 충돌을 푼다(2026-03 개정판 기준). [사실][^ref-700] 저자들은 최악의 탈옥 공격에서 위험 계획 실행이 92% 이상에서 3% 미만으로 줄었다고 보고했다(저자 보고값, 독립 재현 미확인). [사실][^ref-700] 반대로 Robey 외(2024-10)는 언어 모델이 제어하는 로봇이 해로운 물리 행동을 하도록 만드는 탈옥 알고리즘 RoboPAIR 를 제시했고, GPT-4o 계획기를 쓴 Clearpath Jackal 과 GPT-3.5 를 연동한 Unitree Go2 등에서 공격 성공률이 자주 100%에 이르렀다고 보고했다(저자 보고값, 독립 재현 미확인). [사실][^ref-857]

이 연구들을 보면, '사람이 확인·승인한 계획만 실행' 원칙에 실행 전 안전 게이트·가드레일 같은 자동 검사를 더할 때 대화 지시에서 로봇 동작까지 이어지는 경로가 48. 안전·위험 관리의 위험성평가 대상이 될 것으로 보이며, 로봇 자체 안전 기능은 연계 대상으로 남는다. [추정][^ref-417][^ref-700] 관련 열린 질문은 oq-144·oq-302 다.

### D. 공간·지도 모델

[D. 공간·지도 모델](../space-and-map-model/index.md)과는 지도에 붙은 구역 규칙이 안전 조치로 인정받을 수 있는지, 운용 구역을 어떻게 정의하는지로 만난다. 같은 연결은 D. 공간·지도 모델 페이지의 연결 절에도 있다.

VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 여기거나 적용해서는 안 된다고 범위 절에 적는다. [사실][^ref-031] 구역 규칙(16. 장소 의미·지도 관리)을 보면, BLOCKED 구역에는 로봇이 들어가서는 안 되고 구역 안에 있는 로봇은 멈춘 뒤 BLOCKED_ZONE_VIOLATION 오류를 CRITICAL 수준으로 보고하며, SPEED_LIMIT 구역에서는 구역에 들어설 때 이미 최대 속도(m/s) 이하여야 한다. [사실][^ref-031] 따라서 지도에 붙은 진입 금지·속도 제한 구역은 교통 관리 규칙이지 안전 기능이 아니며, 49. 사람 근접 안전의 위험성평가에서 이를 위험 감소 조치로 인정받으려면 ISO 3691-4 의 운용 구역 준비와 로봇의 안전 등급 보호 필드 설정에 맞춰야 할 것으로 보인다(oq-229). [추정][^ref-031][^ref-470]

48. 안전·위험 관리와 15. 지도·공간·위치 모델은 운용 구역 정의로도 이어진다. ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다(2023-06 발행, 표준 본문 미열람, oq-170). [사실][^ref-470] 연계 대상으로, SLAM 위치추정의 안전성을 무결성 위험 지표로 정량화한 연구(IJRR, 2025-05)는 데이터 연관 오류와 지나치게 높은 랜드마크 밀도가 안전성을 떨어뜨릴 수 있다고 보고했으나 위치추정 자체는 로봇 자체 지능·제어 경계에 속한다. [사실][^ref-161]

### E. 사물·사람·실시간 상태

[E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)와는 설비·사람의 현재 상태를 안전 판단에 쓰는 일로 만난다. 이 연결은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이며, 아래 I. 설계·시뮬레이션의 가정한 미래 실험과 구분한다. 같은 연결은 E. 사물·사람·실시간 상태 페이지의 연결 절에도 있다.

Open-RMF 승강기 상태(LiftState)의 현재 모드에는 알 수 없음·사람·무인 운반 차량(Automated Guided Vehicle, AGV)·화재·오프라인·비상이 있고, 이 가운데 사람·AGV 모드만 설정할 수 있으며 나머지는 읽기 전용이다. [사실][^ref-286] 승강기의 화재·비상 모드 제어는 시설·설비 제어 경계의 연계 대상이고, ROP 는 탑승을 확정하기 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다(모드 정보를 몇 초까지 믿을지는 oq-034). [추정][^ref-286]

사람 흐름 쪽에서는 49. 사람 근접 안전이 19. 사람·보행자 모델과 만난다. 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다(기사 1건, 2024-07-12 기준). [사실][^ref-1181] 병원의 사람·휠체어 대기 규칙이나 창고의 학습된 사람 흐름처럼 사람 흐름 정보는 구역·시간대별 대기·속도 규칙으로 49. 사람 근접 안전과 이어질 것으로 보이며, 이때 사람 검출·안전 정지는 로봇이 맡는 연계 대상이다. [추정][^ref-1181][^ref-1180]

### F. 연동

[F. 연동](../integration/index.md)과는 상호운용 규격과 안전 표준의 경계, 비상 신호 전달, 승강기 탑승 안전으로 만난다.

상호운용 표준 쪽에서는 50. 안전 표준·인증·사고 조사가 21. 상호운용 표준·적합성과 만난다. 앞의 D. 공간·지도 모델 항목에서 본 VDA 5050 의 범위 선언에 더해, ISO 21423(산업용 이동로봇 통신·상호운용성)의 범위는 여러 제조사 자율이동로봇(Autonomous Mobile Robot, AMR)·플릿 관리 장비·기업 자원 사이의 통신 프로토콜이며 안전 요구와 공공 도로 이동 기계는 범위에서 뺀다(2026-10-09 확인, 발행 진행 중 단계). [사실][^ref-159] 따라서 연동 적합성 시험(21. 상호운용 표준·적합성)과 안전 표준 적합성·인증(50. 안전 표준·인증·사고 조사)은 별도 경로로 관리해야 할 것으로 보인다. [추정][^ref-031][^ref-159]

비상 신호 쪽에서는 48. 안전·위험 관리가 20. 로봇·제조사 관제 연동과 만난다. Open-RMF 기능 요청 이슈 #658 은 화재경보가 울리면 로봇들이 주차 위치로 이동하지만 비상 신호가 대상 플릿을 구분하지 않는 불리언 값이라고 지적한다(2025-04-04 이슈 작성 기준, 이후 구현 여부 미확인). [사실][^ref-567]

승강기 탑승 쪽에서는 50. 안전 표준·인증·사고 조사가 22. 설비·건물 시스템 연동과 만난다. 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했다. [사실][^ref-945] ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 구성을 로봇 유형별로 바꾸고 탑승형 로봇 절을 뺐으며, 사이버보안·데이터 보호·승강기와 협동하는 로봇(참고 부속서 H) 절을 새로 넣었다(초안 기준). [사실][^ref-1260] 탑승 안전 요구가 국내 KS 와 서비스 로봇 안전 표준 개정 초안 양쪽에 들어오므로, ROP 는 승강기 연동 요청·운영 모드 확인을 맡고 탑승 안전의 적합성은 로봇·승강기 쪽 표준에 맡기는 경계가 될 것으로 보인다(초안 내용이 최종판에 남았는지는 oq-254 에서 확인한다). [추정][^ref-945][^ref-1260][^ref-1117]

### G. 계획·최적화

[G. 계획·최적화](../planning-and-optimization/index.md)와는 배정·경로·대피 동작에 안전을 반영하는 일로 만난다. 비상 경보 때의 주차 동작은 G. 계획·최적화 페이지의 연결 절에도 있다.

배정 쪽에서 49. 사람 근접 안전은 25. 작업 배정 — MRTA와 만난다. Kazemi Eskeri 외(IROS 2025)는 사람과 함께 쓰는 환경에서 사람을 고려하는 다중 로봇 작업 배정 방법을 다뤘다. [사실][^ref-1083]

경로 쪽에서 48. 안전·위험 관리는 27. 다중 로봇 경로·교통 관리 — MAPF와 만난다. Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004] Reliability Engineering & System Safety 게재 연구(2023, 저자 미확인)는 다중 이동로봇 운반 작업의 충돌 위험원을 시스템 이론적 프로세스 분석(System-Theoretic Process Analysis, STPA)과 확률 페트리넷(SPN)으로 모델링·분석했다. [사실][^ref-565]

공용 자원 쪽에서 48. 안전·위험 관리는 28. 공용 자원·충전·에너지 최적화와 만난다. Open-RMF 데모에서는 비상 경보가 켜지면 로봇들을 가장 가까운 주차 위치로 보낸다. [사실][^ref-104]

### H. 실행·협업·예외 복구

[H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)와는 정지 뒤 재개 판단, 통신 단절 때의 동작, 비정상 작업 중 사고로 만난다.

재개 판단 쪽에서 48. 안전·위험 관리는 29. 명령·작업 실행의 신뢰성·31. 사람–로봇 협업과 만난다. VDA 5050 3.0.0 의 안전 상태(safetyState)는 activeEmergencyStop 을 MANUAL(로봇에서 수동 확인), REMOTE(시설 비상정지를 원격 확인), NONE 으로 보고하고, fieldViolation 으로 레이저·범퍼 같은 보호 필드 침범 여부를 보고한다. [사실][^ref-031] 앞의 B. 로봇 온톨로지 항목의 운용 모드 구분과 함께 보면, ROP 의 재개 지시는 비상정지가 NONE 이고 운용 모드가 AUTOMATIC 으로 돌아온 것을 확인한 뒤에 내려야 할 것으로 보인다. [추정][^ref-031] MANUAL 비상정지는 로봇에서 사람이 확인해야 하므로 현장 인력 출동이 복구 절차에 들어갈 것으로 보인다(oq-095). [추정][^ref-031]

통신 단절 쪽에서는 32. 예외 복구·재계획·업무 연속성과 만난다. VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다. [사실][^ref-031]

비정상 작업 중 사고에서는 50. 안전 표준·인증·사고 조사가 32. 예외 복구·재계획·업무 연속성과 J. 현장 운영·관제의 40. 운영 절차·요청 창구와 만난다. 2026-09 식품 제조 공장에서 멈춘 제품 적재 로봇을 점검하던 노동자가 끼여 숨진 사고에 대해, 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(Lockout/Tagout, LOTO)가 실시되지 않았다고 지적했다(2026-09-29 보도 기준, 원인 미확정). [사실][^ref-1125] 2023-11 농산물유통센터에서는 상자를 팔레트로 옮기는 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌다(2023-11-08 보도 기준). [사실][^ref-1124] 두 사망 사고가 모두 점검·작동 확인 같은 비정상 작업 중에 났으므로, ROP 가 정지 뒤 재가동·재개를 지시하기 전에 작업 중인 사람과 잠금 상태를 확인하는 절차가 복구 절차와 운영 절차의 접점이 될 것으로 보인다. [추정][^ref-1124][^ref-1125][^ref-031]

### I. 설계·시뮬레이션

[I. 설계·시뮬레이션](../design-and-simulation/index.md)과는 위험을 현장 투입 전에 가상으로 찾는 일로 만난다. 이 연결은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현 쪽이며, 앞의 E. 사물·사람·실시간 상태 항목에서 다룬 현재 상태 표현(18. 실시간 세계 상태·데이터 일관성)과 섞지 않는다.

48. 안전·위험 관리 쪽에서, Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 만들어 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. [사실][^ref-1241]

49. 사람 근접 안전 쪽에서는 34. 시뮬레이션·예측용 디지털 트윈과 19. 사람·보행자 모델이 함께 쓰인다. Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션에 쓴다(현장 사례가 아니라 시뮬레이션 예제다). [사실][^ref-406] Rondoni 외(Scientific Reports, 2024-08)는 모의 병원 환경의 시뮬레이션 평가에서 병원 물류 로봇 HOSBOT 과 TIAGo 를 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 7개 지표로 비교했고, 최고 속도에서는 방향 오차가 커졌다. [사실][^ref-1081]

연계 대상으로, IEC 61508-7 이 시뮬레이션을 시험 목적의 설비 거동 모사로 정의한다고 인용한 업체 인터뷰(2014)는 기능안전 표준이 안전 확인에 시뮬레이션을 권고한다고 해석했으나 이동로봇 안전 인증이 시뮬레이션 결과를 근거로 받아들이는 절차는 찾지 못했다. [추정][^ref-1249]

### J. 현장 운영·관제

[J. 현장 운영·관제](../field-operations-and-monitoring/index.md)와는 사고 조사용 기록, 실행 중 감시, 사용자 운영 절차로 만난다.

기록 쪽에서 50. 안전 표준·인증·사고 조사는 37. 관제 화면·실행 기록과 만난다. Winfield 외(2022-05)는 사회적 로봇의 사고 조사를 위한 윤리적 블랙박스(Ethical Black Box) 개방 표준 초안을 제안했다. [사실][^ref-1120] 플릿 수준에서 명령·정지·재가동·운용 모드 전환·안전 상태 보고를 시각과 함께 남기는 실행 기록이 사고·아차 사고 조사의 입력이 될 것으로 보이나, 그 최소 항목을 정한 표준은 확인하지 못했다(oq-252). [추정][^ref-1120][^ref-1122][^ref-031]

감시 쪽에서는 38. 모니터링·이상 탐지·원인 분석과 만난다. Sanders·Sener·Chen(Applied Ergonomics, 2024)은 미국 산업안전보건청(OSHA) 중대 부상 보고(Severe Injury Reports)에서 작업장 로봇 관련 부상을 분석했다. [사실][^ref-1122] Ferrando 외(2020)의 ROSMonitoring 은 로봇 운영체제(Robot Operating System, ROS) 응용의 형식 속성을 ROS 바깥에서 명세해 실행 중에 검증하는 런타임 검증 틀이며, 여러 ROS 배포판에 옮겨 쓸 수 있고 특정 명세 형식에 묶이지 않는다. [사실][^ref-1261] 진입 금지 구역 위반이나 정지 지시 뒤 응답처럼 안전과 관련된 운영 규칙을 실행 중에 감시하는 런타임 검증이 38. 모니터링·이상 탐지·원인 분석과 48. 안전·위험 관리를 잇는 방법이 될 것으로 보이나, 제조사가 다른 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-1261][^ref-031]

운영 절차 쪽에서는 40. 운영 절차·요청 창구와 만난다. ANSI/A3 R15.08-3-2026 은 산업용 이동로봇을 운영하는 사용자에게 위험성평가와 직원 교육을 요구한다. [사실][^ref-1254][^ref-1256] ANSI 블로그(2026-09-17)는 여기에 위험 감소 조치의 유지와 안전 작업 절차를 든다. [사실][^ref-1254] Robotics 24/7(2026-10-04)과 A3 판매 페이지는 변경 관리를 사용자 의무로 든다. [사실][^ref-1256][^ref-1255] 이 내용은 ANSI 블로그·Robotics 24/7·A3 판매 페이지의 요약 기준이며 표준 본문은 열람하지 않았다. R15.08-3 의 사용자 교육·안전 작업 절차 요구는 40. 운영 절차·요청 창구의 현장 절차와 O. 검증·도입·수명주기의 56. 운영 이관·확대·교육의 교육 계획으로 넘어갈 것으로 보이나, 여러 제조사 로봇이 섞인 현장에서 누가 이를 이행하는지는 확인하지 못했다(oq-265). [추정][^ref-1254][^ref-1256] 점검 중 사고와 잠금 확인 절차는 앞의 H. 실행·협업·예외 복구 항목에 적었다.

### K. 플랫폼 아키텍처·인프라

[K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)와는 플릿 일괄 정지 신호를 어떤 통신 경로에 둘지로 만나며, 48. 안전·위험 관리와 42. 분산 시스템·통신·컴퓨팅 구조가 맞닿는다.

FORT Robotics 사례 소개에 따르면, 한 창고의 울타리 친 AMR 구역에서 문에 단 주 제어기가 문이 열리면 구역의 로봇들에 무선 안전 비상정지를 보내며 이 시스템은 ISO 13849 범주 3·PLd 로 설계됐다고 한다(2023-05-18 게재). [추정] 벤더 주장[^ref-1257] 이 사례는 소규모 시범 운영 단계이고, 플릿 관리 시스템·창고 관리 시스템(WMS) 연동은 언급하지 않는다. [추정] 벤더 주장[^ref-1257] VDA 5050 은 안전 표준이 아니고 연결이 끊긴 로봇은 받은 주문을 이어 수행하므로, 플릿 일괄 정지는 관제 메시지 경로가 아니라 그와 독립된 안전 등급 정지 경로에 맡기고 ROP 는 정지 결과를 상태로 받아 작업을 보류·재배정하는 구조가 두 대분류의 경계가 될 것으로 보인다(oq-095). [추정][^ref-031][^ref-1257]

### L. AI·학습 기술

[L. AI·학습 기술](../ai-and-learning/index.md)과는 AI 가 정지·경로·구역 결정에 관여할 때의 규제 분류와 채택 검사로 만난다. 교차 규칙에 따라 이 내용은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과, 적용 대상인 48. 안전·위험 관리 양쪽에 연결한다.

EU AI Act(Regulation (EU) 2024/1689)는 부속서 I 의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이면서 제3자 적합성 평가를 받는 AI 시스템을 고위험 AI 로 분류한다. [사실][^ref-621] 법무법인 태평양 해설에 따르면, 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을 정하게 하고 운영 단계에서 성능 저하·오류의 정기 점검과 관리자 교육을 요구한다(2025-09 초안 기준 해설). [사실][^ref-1253] AI 가 정지·경로·구역 결정에 관여하면 실행 전 안전 게이트 같은 채택 검사는 47. AI·학습·적응과 모델 운영의 채택 기준과 48. 안전·위험 관리의 위험성평가 양쪽에 걸칠 것으로 보이며, 이런 AI 가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106). [추정][^ref-621][^ref-417]

### N. 보안·개인정보

[N. 보안·개인정보](../security-and-privacy/index.md)와는 안전 표준에 들어온 사이버보안·데이터 보호 요구와, 공격이 안전 사고로 번지는 경로로 만난다.

산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다(조항 번호 미확인, oq-102). [사실][^ref-1116][^ref-1076] 서비스 로봇 쪽에서도 앞의 F. 연동 항목의 ISO 13482 개정 초안이 사이버보안·데이터 보호 절을 새로 넣었다(초안 기준). [사실][^ref-1260] 이렇게 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제(51. 인증·권한·격리)와 사람 위치·영상 데이터 처리(53. 개인정보·영상 데이터)도 안전 평가 대상이 될 것으로 보인다. [추정][^ref-1116][^ref-1260]

52. 통신 보호·위협 관리·감사 쪽에서는 공격이 안전 문제로 번진다. Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. [사실][^ref-1242] 언어 모델 제어 로봇의 탈옥 공격(RoboPAIR)은 앞의 C. 채팅 기반 구성·운영 항목에 적었으며, 같은 내용이 52. 통신 보호·위협 관리·감사와도 이어진다.

### O. 검증·도입·수명주기

[O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)와는 안전 시험, 배치 전 위험성평가, 법정 교육, 배치 후 변경 관리로 만난다.

시험 쪽에서는 54. 시험·형식 검증·벤치마크와 만난다. 앞의 J. 현장 운영·관제 항목의 런타임 검증 틀(ROSMonitoring)이 이 영역에도 걸치며, 49. 사람 근접 안전의 평가 기준과 관련해 Francis 외(2023)는 사회적 로봇 내비게이션 알고리즘의 평가 원칙과 지침을 정리했다. [사실][^ref-1079]

배치 전 평가 쪽에서는 55. 현장 조사·설치·시운전과 만난다. Belzile 외(2025-02)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과 이동로봇 전용이면서 여러 배치 상황에 적용할 수 있는 표준이 없다고 보고, 건설 현장 이동로봇 배치 전에 쓸 위험성평가 틀을 제안했다(프리프린트). [사실][^ref-563]

법정 교육 쪽에서는 56. 운영 이관·확대·교육과 만난다. 법제처 법령해석 23-0872(2023-11-21)는 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 '산업용 로봇'을 쓰는 작업으로 한정되지 않는다고 회답했고, KS B ISO 8373 의 '로봇'이 산업용·서비스용·의료용을 포괄한다는 점을 근거로 들었다(제3자 게재본 기준, 법원 판결 같은 기속력은 없음). [사실][^ref-1258] 따라서 서비스·이동 로봇을 쓰는 작업도 로봇작업 특별교육 대상이 될 수 있으므로, ROP 를 들인 현장의 운영 이관 교육 계획에 법정 특별교육 해당 여부 판단이 들어가야 할 것으로 보이나 고용노동부의 적용 지침은 확인하지 못했다(oq-275). [추정][^ref-1258] 앞의 L. AI·학습 기술 항목의 관리자 교육 요구(초안 기준 해설)와 J. 현장 운영·관제 항목의 R15.08-3 교육 요구도 56. 운영 이관·확대·교육과 이어진다.

배치 후 변경 쪽에서는 57. 자산·소프트웨어 수명주기 관리와 만난다. R15.08-3 은 공급자가 배치한 뒤 사용자가 산업용 이동로봇이나 그 적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다고 한다(ANSI 블로그 2026-09-17 요약 기준, 표준 본문 미열람). [사실][^ref-1254] ROP 에서 구역·속도 제한·경로망·운영 정책을 바꾸는 일이 사용자 쪽 변경 관리와 위험성 재평가의 계기가 될 수 있으므로, 설정 변경 이력을 판 단위로 남기고 재평가 필요 여부를 표시하는 기능이 48. 안전·위험 관리와 57. 자산·소프트웨어 수명주기 관리를 잇는 것으로 보인다(oq-093, oq-282). [추정][^ref-1254][^ref-031]

### P. 거버넌스·법규·사회

[P. 거버넌스·법규·사회](../governance-law-and-society/index.md)와는 다사업자 책임, 법령·인증·보험, 사회적 수용으로 만난다.

다사업자 책임 쪽에서 48. 안전·위험 관리는 58. 다사업자 책임·계약·데이터와 만난다. ANSI/A3 R15.08-2 는 2023-10 산업용 이동로봇 시스템과 적용의 안전 요구를 다루는 2부로 발표됐다. [사실][^ref-472][^ref-1084] 통합자와 ROP 사업자의 역할 분담은 이 발행 사실만으로 정해지지 않으며, 앞의 A. 기획·사업 항목의 추정과 열린 질문 oq-096 으로 이어진다.

법령·인증 쪽에서 50. 안전 표준·인증·사고 조사는 59. 법·규제·보험·라이선스와 만난다. EN ISO 10218-1:2025·-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015 로 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다. [사실][^ref-1116] 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 미확인이다. 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거하며, 인증 절차와 기준은 산업통상자원부 고시(2023-11-17)로 정해졌다. [사실][^ref-980][^ref-1118] 심사 항목 수는 출처마다 달라 열린 질문 oq-186·oq-230 에서 다룬다. 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 산업용 로봇의 운전 중 위험 방지 조치를 정하고, 한국산업표준이나 국제 안전기준에 맞는 경우 방책 같은 조치를 생략할 수 있게 한다(2023-07-01 시행본 기준, 물류센터 AMR 플릿 적용 여부는 oq-097). [사실][^ref-562] 실외이동로봇 운영자의 보험 의무는 앞의 A. 기획·사업 항목에 적었다.

사회적 수용 쪽에서 49. 사람 근접 안전은 60. 노동·수용성·접근성과 만난다. Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명을 면담하고 공동설계 워크숍을 연 결과, 이동장애인이 보도 로봇과 보도 공간을 두고 경쟁한다고 느끼고 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. [사실][^ref-1214]

### Q. 현장 유형별 적용

[Q. 현장 유형별 적용](../site-type-applications/index.md)은 현장마다 다른 요구를 모으고, 위 연결 가운데 모든 현장에 공통인 기능은 A~P 의 대분류에 둔다. 아래는 M. 안전의 근거가 있는 현장 유형이다.

- **61. 물류창고**: 상자를 팔레트로 옮기는 로봇의 점검 중 사망 사고가 있다(2023-11-08 보도 기준, 앞의 H. 실행·협업·예외 복구 항목). [사실][^ref-1124] 울타리 구역의 무선 안전 비상정지 사례도 있으나 업체 소개 기준이다(앞의 K. 플랫폼 아키텍처·인프라 항목). [추정] 벤더 주장[^ref-1257] 아마존은 자사 풀필먼트 센터에서 직원이 로보틱스 테크 조끼를 켜고 로봇 구역에 들어가면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명하며, 감속 속도·거리 값은 공개되지 않았다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1080]
- **62. 제조 공장**: 식품 제조 공장의 적재 로봇 점검 중 끼임 사망 사고와 잠금·표지 미실시 지적이 있다(2026-09-29 보도 기준, 원인 미확정, 앞의 H. 실행·협업·예외 복구 항목). [사실][^ref-1125]
- **63. 병원·의료**: 병원의 로봇 통행 경로·작업 정지 지점 표시(기사 1건, 앞의 E. 사물·사람·실시간 상태 항목)와 모의 병원 환경의 주행 속도 시뮬레이션 평가(앞의 I. 설계·시뮬레이션 항목)가 있다. [사실][^ref-1181][^ref-1081]
- **65. 가정·공동주택**: Webb 외(2021)는 지원 주거 아파트에서 넘어진 거주자를 보조 로봇이 직원에게 알리지 못한 모의 사고를 역할극 증언 면담과 윤리적 블랙박스 기록으로 조사하는 방법을 시험했다(실제 사고가 아닌 모의 사고 시나리오). [사실][^ref-1121]
- **66. 실외**: 한국로봇산업진흥원은 실외이동로봇 운행안전인증 대상을 최고 속도 15km/h 이하·최대 질량 500kg 이하로 두고 주변 인식과 비상정지를 심사하며, 인증 뒤 2년 주기 정기점검을 둔다(확인일 2026-09-30). [사실][^ref-980] 운영자 보험 의무(앞의 A. 기획·사업 항목)와 보도 접근성 연구(앞의 P. 거버넌스·법규·사회 항목)도 실외 현장의 요구다. [사실][^ref-1259][^ref-1214]
- **67. 기타 현장**: 건설 현장 이동로봇 배치 전 위험성평가 틀 제안이 있다(프리프린트, 앞의 O. 검증·도입·수명주기 항목). [사실][^ref-563]
- **64. 상업 시설**: 실제 현장의 사람 근접 안전 사례는 아직 다루지 않았다. 앞의 I. 설계·시뮬레이션 항목의 공항 터미널 군중 시뮬레이션은 시뮬레이션 예제이므로 현장 사례로 세지 않는다.

### 아직 다루지 않은 연결

다음 연결은 이번 실행의 근거가 없어 내용을 채우지 않았다: 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 그리고 64. 상업 시설의 실제 사람 근접 안전 사례.

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-10-09 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-10-09 (원문 미열람)
[^ref-161]: Abdul Hafez, O., Joerger, M., & Spenko, M., Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach, 2025-05, https://journals.sagepub.com/doi/10.1177/02783649241287797, 접근일 2026-10-09 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09
[^ref-417]: Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-09 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-10-09 (원문 미열람)
[^ref-472]: A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-10-09 (원문 미열람)
[^ref-562]: 국가법령정보센터(고용노동부), 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지), 2023-07-01, https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0, 접근일 2026-10-09 (원문 미열람)
[^ref-563]: Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02, https://arxiv.org/abs/2502.20693, 접근일 2026-10-09 (원문 미열람)
[^ref-565]: Reliability Engineering & System Safety (저자 미확인), Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN, 2023, https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534, 접근일 2026-10-09 (원문 미열람)
[^ref-567]: Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf, 2025-04-04, https://github.com/open-rmf/rmf/issues/658, 접근일 2026-10-09 (원문 미열람)
[^ref-621]: European Commission, AI Act | Shaping Europe's digital future, 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-10-09 (원문 미열람)
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-10-09 (원문 미열람)
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-09 (원문 미열람)
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-10-09 (원문 미열람)
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-06-29, https://arxiv.org/abs/2306.16740, 접근일 2026-10-09 (원문 미열람)
[^ref-1080]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-10-09 (원문 미열람)
[^ref-1081]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-10-09 (원문 미열람)
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-09 (원문 미열람)
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-10-09 (원문 미열람)
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-10-09
[^ref-1117]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-10-09 (원문 미열람)
[^ref-1118]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-10-09 (원문 미열람)
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09 (원문 미열람)
[^ref-1121]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-10-09 (원문 미열람)
[^ref-1122]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-10-09 (원문 미열람)
[^ref-1124]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-10-09 (원문 미열람)
[^ref-1125]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-10-09 (원문 미열람)
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-10-09 (원문 미열람)
[^ref-1181]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-10-09 (원문 미열람)
[^ref-1214]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-10-09 (원문 미열람)
[^ref-1241]: Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020), Simulation-based Testing for Early Safety-Validation of Robot Systems, 2020-11-20, https://arxiv.org/abs/2011.10294, 접근일 2026-10-09 (원문 미열람)
[^ref-1242]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09 (원문 미열람)
[^ref-1249]: Wind River (Engblom, J. 인터뷰, Buchwieser, A.), Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser, 2014-11-20, https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser, 접근일 2026-10-09 (원문 미열람)
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv), Jailbreaking LLM-Controlled Robots, 2024-10-17, https://arxiv.org/abs/2410.13691, 접근일 2026-10-09 (원문 미열람)
[^ref-700]: Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03-10, https://arxiv.org/abs/2503.07885, 접근일 2026-10-09 (원문 미열람)
[^ref-1253]: 법무법인 태평양(BKL) AI팀, AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인, 2025-09-30, https://www.bkl.co.kr/law/insight/newsletter/6248, 접근일 2026-10-09 (원문 미열람)
[^ref-1254]: ANSI (American National Standards Institute) Blog, ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 2026-09-17, https://blog.ansi.org/?p=190868, 접근일 2026-10-09
[^ref-1255]: A3(Association for Advancing Automation), ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications, 2026-04-23, https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download, 접근일 2026-10-09
[^ref-1256]: Robotics 24/7, A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available, 2026-10-04, https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available, 접근일 2026-10-09
[^ref-1257]: FORT Robotics (A3 Case Studies 게재), Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs, 2023-05-18, https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs, 접근일 2026-10-09
[^ref-1258]: 법제처 (네플라 위키 게재본, 법제처 원문 미열람), [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련), 2023-11-21, https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k, 접근일 2026-10-09
[^ref-1259]: 메트로신문 (한용수), 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막, 2023-11-16, https://www.metroseoul.co.kr/article/20231116500208, 접근일 2026-10-09
[^ref-1260]: DIN Media, DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024), 2024-10, https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303, 접근일 2026-10-09
[^ref-1261]: Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS), ROSMonitoring: A Runtime Verification Framework for ROS, 2020-12-03, https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/, 접근일 2026-10-09

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 72건이다(논문 22건 · 기사·보고서 14건 · 업체 발표 3건 · 표준·오픈소스·기관 자료 33건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1085](../../references/ref-1085.md) — Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters (발행 2026-04-15)
- [ref-417](../../references/ref-417.md) — Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems (발행 2026-04)
- [ref-1076](../../references/ref-1076.md) — Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 (발행 2026-02-19)
- [ref-1083](../../references/ref-1083.md) — Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments (발행 2025-08-27)
- [ref-161](../../references/ref-161.md) — Abdul Hafez, O., Joerger, M., & Spenko, M., Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach (발행 2025-05)
- [ref-1082](../../references/ref-1082.md) — Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario (발행 2025-03-27)
- [ref-700](../../references/ref-700.md) — Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots (발행 2025-03)
- [ref-563](../../references/ref-563.md) — Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment (발행 2025-02)
- [ref-857](../../references/ref-857.md) — Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots (발행 2024-11-09)
- [ref-1081](../../references/ref-1081.md) — Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments (발행 2024-08-07)
- 그 밖에 12건

**기사·보고서**

- [ref-1256](../../references/ref-1256.md) — Robotics 24/7, A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available (발행 2026-10-04)
- [ref-1125](../../references/ref-1125.md) — 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 (발행 2026-09-29)
- [ref-1116](../../references/ref-1116.md) — IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2 (발행 2026-09-18)
- [ref-791](../../references/ref-791.md) — Intertek, Machines Got Smarter, Now ISO 12100 has to Catch Up (발행 2025-12-11)
- [ref-1253](../../references/ref-1253.md) — 법무법인 태평양(BKL) AI팀, AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인 (발행 2025-09-30)
- [ref-1115](../../references/ref-1115.md) — The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul (발행 2025-02)
- [ref-1181](../../references/ref-1181.md) — 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 (발행 2024-07-12)
- [ref-1078](../../references/ref-1078.md) — 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠" (발행 2024-03-09)
- [ref-1259](../../references/ref-1259.md) — 메트로신문 (한용수), 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막 (발행 2023-11-16)
- [ref-1124](../../references/ref-1124.md) — 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 (발행 2023-11-08)
- 그 밖에 4건

**업체 발표**

- [ref-1257](../../references/ref-1257.md) — FORT Robotics (A3 Case Studies 게재), Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs (발행 2023-05-18)
- [ref-1249](../../references/ref-1249.md) — Wind River (Engblom, J. 인터뷰, Buchwieser, A.), Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser (발행 2014-11-20)
- [ref-1080](../../references/ref-1080.md) — Amazon, Ever wonder how people and robots team up on your Amazon order? (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-1254](../../references/ref-1254.md) — ANSI (American National Standards Institute) Blog, ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications (발행 2026-09-17)
- [ref-1255](../../references/ref-1255.md) — A3(Association for Advancing Automation), ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications (발행 2026-04-23)
- [ref-567](../../references/ref-567.md) — Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf (발행 2025-04-04)
- [ref-560](../../references/ref-560.md) — ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells (발행 2025-02)
- [ref-790](../../references/ref-790.md) — DIN Media, DIN EN ISO 12100 - 2025-01 (Draft standard) (발행 2025-01)
- [ref-561](../../references/ref-561.md) — 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 (발행 2024-11-03)
- [ref-1260](../../references/ref-1260.md) — DIN Media, DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) (발행 2024-10)
- [ref-1258](../../references/ref-1258.md) — 법제처 (네플라 위키 게재본, 법제처 원문 미열람), [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련) (발행 2023-11-21)
- [ref-1118](../../references/ref-1118.md) — 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (발행 2023-11-17)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- 그 밖에 23건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [M. 안전](index.md) — '다른 대분류와의 연결' 절 첫 작성: 16개 대분류와의 연결(주장 70건 근거), Q. 현장 유형별 적용 현장별 정리, 아직 다루지 않은 연결 7건, 각주 정의 48건 (실행 2026-10-09-09)
- 2026-10-09 · 요약 · [M. 안전](index.md) — M. 안전: 다른 대분류와의 연결 절 첫 작성(16개 대분류와의 연결, 현장 유형별 근거, 아직 다루지 않은 연결 7건) (실행 2026-10-09-09)
- 2026-09-30 · 갱신 · [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) — seed → draft: 3~11절 첫 작성(표준·인증 개정 현황, 제조 공장·물류창고·실외·가정·기타 사례, 사고 기록·조사 방법, 책임 경계, 연결 17건, 열린 질문 7건). 2차 수정: 7절 머리 문장을 f1·f3 의 구체 사실로 교체, 프런트매터 sources 를 각주 정의와 일치 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 머리 문장을 f1·f3 의 구체 사실로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "4. 핵심 개념과 용어" 절(1,007자)을 옮겼다 (실행 2026-09-30-15)
<!-- auto:category-recent:end -->
