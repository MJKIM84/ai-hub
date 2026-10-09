---
title: "N. 보안·개인정보"
type: category
status: draft
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-009, ref-010, ref-031, ref-405, ref-494, ref-579, ref-588, ref-589, ref-700, ref-854, ref-857, ref-863, ref-969, ref-1076, ref-1105, ref-1106, ref-1107, ref-1109, ref-1110, ref-1111, ref-1112, ref-1113, ref-1114, ref-1116, ref-1136, ref-1138, ref-1141, ref-1145, ref-1146, ref-1173, ref-1299, ref-1301, ref-1242, ref-1263, ref-1228, ref-1264, ref-1265, ref-1266, ref-1267, ref-1268, ref-1269, ref-1272, ref-1273, ref-1274, ref-1260]
---

[홈](../../index.md) › N. 보안·개인정보

# N. 보안·개인정보

## 핵심 질문

누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

## 개요

인증·권한·격리, 통신 보호, 위협 관리와 감사 기록, 문서·대화 입력 보안, 개인정보·영상 데이터 보호. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **51. 인증·권한·격리** | 장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? | [51. 인증·권한·격리](authentication-authorization-and-isolation.md) | published |
| **52. 통신 보호·위협 관리·감사** | 통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 | 통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? | [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md) | published |
| **53. 개인정보·영상 데이터** | 영상·작업자·거주자 데이터 보호, 최소 수집·익명화 | 로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? | [53. 개인정보·영상 데이터](privacy-and-video-data.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문]

## 다른 대분류와의 연결

이 절은 게시된 [51. 인증·권한·격리](authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md) 페이지와 다른 대분류 페이지의 검증된 주장을 근거로, N. 보안·개인정보의 세 세부영역이 다른 대분류의 어느 세부영역과 무엇으로 이어지는지 정리한다. 연결의 절반 가까이가 추정이고 근거 대부분이 단일 출처의 재인용이므로, 문장마다 붙은 태그로 확인된 사실과 추정을 나눠 읽는다. 본문의 oq 번호는 [열린 질문](../../open-questions.md) 페이지의 항목이다.

범위 경계는 분류 원문 19장을 따른다. 로봇 제어기·운영체제·펌웨어 보안은 '로봇 자체 지능·제어' 경계의 제조사 몫, 현장 망의 방화벽·VPN과 승강기 조작은 '시설·설비 제어' 경계의 연계 대상, 앱·기기 쪽 보안과 얼굴 가림·잠금 칸 인증은 제조사 기능에 속하는 연계 대상이다. 법령·규정이 실제로 적용되는지의 판단은 운영 사업자·법무가 맡는 연계 대상이며, 아래 연결에서 ROP 몫은 기록·통보·데이터 흐름 규칙을 제공하는 데까지로 본다. [의견]

### A. 기획·사업

대분류 페이지: [A. 기획·사업](../planning-and-business/index.md)

- **[1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md) ↔ 52. 통신 보호·위협 관리·감사.** 과학기술정보통신부와 한국인터넷진흥원(Korea Internet & Security Agency, KISA)은 2026-03-05 로봇 보안모델 고도화판과 로봇 보안요구사항 해설서를 공개했고, 피지컬 AI 확산과 유럽·북미 사이버보안 규제 강화를 반영해 기업이 개발·수출 과정의 보안 요구를 파악하게 하는 것을 목적으로 밝혔다. [사실][^ref-1269][^ref-1111] 두 근거는 같은 정부 발표를 옮긴 기사라 독립 교차 확인이 아니며, 보안모델·해설서의 구체 요구 항목은 미확인이다(oq-250).
- **[2. 사용 사례·요구·책임 범위](../planning-and-business/use-cases-requirements-and-scope.md) ↔ 52. 통신 보호·위협 관리·감사.** 52. 통신 보호·위협 관리·감사 페이지는 ROP가 자신이 여는 연결의 보안과 전체 연결 구조의 위협 모델을 맡고 로봇 제어기·펌웨어와 현장 망 보안은 제조사·시설 IT/OT(정보기술/운영기술) 쪽 연계 대상으로 두므로, 이 보안 책임 경계가 2. 사용 사례·요구·책임 범위의 책임 범위 정의에 들어가야 할 것으로 보인다. [추정][^ref-1114][^ref-1107][^ref-009]
- **[3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md) ↔ 51. 인증·권한·격리.** KUKA는 iiQKA.OS2 운영체제와 KR C5-2 제어기 플랫폼이 IEC 62443-4-2 보안 수준 2(SL2) 인증을 받았고 로봇 제조사 가운데 처음이라고 2026-09-02 발표했는데, 인증 사실과 '최초'는 모두 KUKA 보도자료의 주장이고 발표문에 인증 기관은 적혀 있지 않으며 제어기 보안 인증 자체는 로봇 제조사 쪽 연계 대상이다. [추정] 벤더 주장[^ref-1273] IEC 62443이 보안 수준을 정하고 로봇 제어기 단위의 인증 발표가 나오고 있으므로 로봇·플랫폼 조달 요구에 구성요소 보안 인증 여부와 목표 보안 수준을 넣는 일이 3. 경제성·조달·사업 모델로 넘어갈 것으로 보이나, 플릿 관리 소프트웨어 단위의 인증 사례는 확인하지 못했다. [추정][^ref-1105][^ref-1273]

### B. 로봇 온톨로지

대분류 페이지: [B. 로봇 온톨로지](../robot-ontology/index.md)

- **[4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md) ↔ 51. 인증·권한·격리.** VDA 5050 3.0.0은 로봇이 새 인증서 묶음을 내려받아 활성화하게 하는 즉시 동작 updateCertificate를 두며, 키 내려받기 링크와 인증서 내려받기 링크는 필수 매개변수이고 인증 기관 내려받기 링크만 선택 매개변수다. [사실][^ref-031] 명세는 이 내려받기도 전송 계층 보안(Transport Layer Security, TLS)으로 보호해야 하고 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고 적는다(3.0.0 판, 발행일 미확인, 2026-10-09 확인). [사실][^ref-031]
- **4. 이기종 로봇 등록·[7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md), O. 검증·도입·수명주기의 [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) ↔ 51. 인증·권한·격리.** 로봇마다 인증서 교체 지원 여부와 인증서 판·만료를 등록 정보로 두고 교체 이력을 판 관리와 함께 다루면 인증서 교체 대상과 시점을 추적할 수 있을 것으로 보이나, 이를 등록 항목·판 관리로 다룬 공개 구현은 확인하지 못했다. [추정][^ref-031] 교체 승인과 실패 때 되돌림 책임은 oq-113으로 남아 있다.
- **4. 이기종 로봇 등록 ↔ 53. 개인정보·영상 데이터.** 53. 개인정보·영상 데이터 페이지가 카메라 유무·촬영 사실 표시 수단·영상 전송 경로 기록과 로봇 인지 출력 필드 축소를 ROP 직접 범위로 보므로, 이런 개인정보 관련 속성이 4. 이기종 로봇 등록의 등록 항목으로 넘어갈 것으로 보인다. [추정][^ref-1145][^ref-588]
- **[6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md) ↔ 51. 인증·권한·격리.** ROS 2 접근 제어 정책은 인클레이브별로 토픽·서비스·액션 단위의 허용·거부를 두므로, '진단은 허용하고 이동은 막는' 명령 단위 권한을 걸려면 6. 온톨로지 기반 시스템·로봇 연동이 능력을 실제 명령에 묶을 때 권한 정책과 같은 명령 식별자를 공유해야 할 것으로 보인다. [추정][^ref-579][^ref-405] 능력 모델과 권한 정책을 잇는 공개 사례는 확인하지 못했다.

### C. 채팅 기반 구성·운영

대분류 페이지: [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md). 분류 원문의 C. 채팅 기반 구성·운영 주석은 대화 결과를 실행 명령이 아니라 계획으로 보고 사람이 확인·승인한 계획만 실행하게 하므로, 아래 보안 연결은 이 원칙과 함께 읽는다. 업무 지시 대화가 부르는 엔진은 G. 계획·최적화의 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링이다.

- **[13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md) ↔ 52. 통신 보호·위협 관리·감사.** OWASP(Open Worldwide Application Security Project) LLM01:2025는 프롬프트 주입을 사용자가 직접 넣는 직접 주입과 문서·웹 같은 외부 내용에 숨은 지시가 들어오는 간접 주입으로 나누고 완화책을 정리한다. [사실][^ref-1106]
- **[12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) ↔ 52. 통신 보호·위협 관리·감사.** 대규모 언어 모델(Large Language Model, LLM)을 통합한 이동로봇 시스템에 대한 프롬프트 주입 공격 연구(Zhang 외, 2024-08)와 다중 에이전트 로봇 시스템에서 프롬프트가 로봇을 제어할 때의 프롬프트 주입 공격 연구(Nagaraja 외, 2026-08)가 있다. [사실][^ref-1113][^ref-1112]
- **13. 대화형 기능의 신뢰·기반, L. AI·학습 기술의 [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md) ↔ 52. 통신 보호·위협 관리·감사.** Robey 외는 언어 모델이 제어하는 로봇에서 탈옥 알고리즘 RoboPAIR의 공격 성공률이 자주 100%에 이르렀다고 보고했고, Ravichandran 외의 RoboGuard는 arXiv 개정판 v2(2026-03-03) 기준으로 최악의 탈옥 공격에서 위험 계획 실행을 92% 초과에서 3% 미만으로 줄였다고 보고했다. [사실][^ref-857][^ref-700] v1은 다른 수치를 보고했고, 두 수치 모두 저자 보고값이며 독립 재현은 확인되지 않았다.
- **12. 채팅으로 업무 지시·오케스트레이션 ↔ 51. 인증·권한·격리.** Open-RMF REST API를 언어 모델 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버(Nayantra) 같은 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근 통제가 '사람이 확인·승인한 계획만 실행' 원칙과 함께 두 대분류의 경계가 될 것으로 보인다. [추정][^ref-854][^ref-857] 발표 안내문에는 권한 제한 구성이 나오지 않는다.
- **12. 채팅으로 업무 지시·오케스트레이션 ↔ 52. 통신 보호·위협 관리·감사.** '사람이 확인·승인한 계획만 실행'이 지켜졌음을 사후에 보이려면 누가 어떤 계획을 언제 승인했는지를 변조 탐지가 가능한 감사 기록으로 남겨야 할 것으로 보이며, 자율 에이전트 행동을 블록체인 기록과 언어 모델 설명으로 추적하는 구조 연구(2024-03)가 그 후보다. [추정][^ref-1110] 대화 승인 기록에 적용한 사례는 확인하지 못했다(oq-248).

### D. 공간·지도 모델

대분류 페이지: [D. 공간·지도 모델](../space-and-map-model/index.md)

- **[16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md) ↔ 53. 개인정보·영상 데이터.** 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 브랜드(2025-03 기준 최신 모델) 점검에서 집 내부 구조를 나타내는 지도 정보는 모든 제품이 기기에 저장하고 스마트폰에는 저장하지 않았으며 일부 제품은 서버에도 저장했고, 일부 사업자는 로봇청소기 접근통제와 개인정보 전송 암호화가 미흡했다. [사실][^ref-1268][^ref-1141] 위원회는 특별한 개인정보 침해 위험은 확인되지 않았다고 밝혔고, 지도 저장 위치는 기사 한 건에서만 확인했다. [사실][^ref-1268] 앱 인증·기기 저장은 제조사 기능의 연계 대상이다.
- **[15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)·16. 장소 의미·지도 관리 ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 건물 내부 지도가 개인정보 점검 대상 정보로 다뤄지고 VDA 5050이 지도를 관제가 지정한 링크에서 내려받게 하므로, ROP가 보관·배포하는 지도의 저장 위치·전송 암호화·접근 권한을 정하는 일이 두 대분류를 잇는 지점이 될 것으로 보인다. [추정][^ref-1268][^ref-031] 업무 시설 지도의 접근 통제를 다룬 기관 자료는 찾지 못했으며, 이 연결은 D. 공간·지도 모델 페이지가 근거 없음으로 남긴 자리를 채운다.

### E. 사물·사람·실시간 상태

대분류 페이지: [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)

- **[18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ 52. 통신 보호·위협 관리·감사.** Shen 외(2026-09, 프리프린트)는 ROS 2에서 환경 변수 하나를 바꾸면 사전 빌드된 훅이 텔레메트리·제어 신호를 발행 전에 가로채고 주입할 수 있음을 보였고, Secure ROS 2를 쓴 실제 Franka 로봇팔에서 약 3 ms 지터로 위조 텔레메트리를 넣어 AI 기반 탐지기 상대로도 87% 성공했다고 보고했다. [사실][^ref-1272] 87%와 약 3 ms는 저자 보고값이고 독립 재현은 확인되지 않았다.
- **18. 실시간 세계 상태·데이터 일관성, J. 현장 운영·관제의 [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ 52. 통신 보호·위협 관리·감사.** 로봇이 보고하는 상태가 통신 보호 이전 단계에서 위조될 수 있고, 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 배정·경로 계획의 비용 개선을 없앨 수 있다는 연구(GPS 스푸핑·택시 수요 실험, 물류센터 적용 미확인)가 있으므로, 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 판단과 38. 모니터링·이상 탐지·원인 분석은 암호화된 보고만 믿지 말고 설비 센서·다른 로봇 관측과 교차 확인해야 할 것으로 보인다. [추정][^ref-1272][^ref-494] 이는 현재 상태를 표현하는 쪽의 문제이며(oq-082), I. 설계·시뮬레이션의 가정한 미래 실험과는 구분한다.
- **[17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 병원 운반 로봇 Zena RX는 생체 인식과 직원 PIN으로 잠금 칸을 연다고 제조사 보도자료(2024-04-29)가 밝히고, 공동주택 배달 로봇은 2020-07 계획 단계 보도에서 비밀번호로 적재함을 열게 했으므로, '누구에게 넘겼는가' 기록은 인증 수단과 생체·전화번호 처리 규칙에 기댈 것으로 보인다. [추정] 벤더 주장[^ref-1299][^ref-1301] 잠금 칸·생체 인증은 제조사 기능의 연계 대상이다(oq-293).
- **[19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md) ↔ 53. 개인정보·영상 데이터.** ROS 규약 제안 REP-155(Draft 상태, 2022-01-11 작성)는 사람마다 영속 ID를 두고 얼굴·몸·음성 ID를 후보 대응으로 연결하며, 개인정보·동의는 다루지 않는다. [사실][^ref-1173]

### F. 연동

대분류 페이지: [F. 연동](../integration/index.md)

- **[20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) ↔ 51. 인증·권한·격리.** 2025-08 한 보안 연구자는 Pudu Robotics 로봇 관리 소프트웨어가 유효한 인증 토큰만 확인하고 그 뒤 권한을 검사하지 않아, 교차 사이트 스크립팅(Cross-Site Scripting, XSS)이나 체험 계정으로 얻은 토큰으로 주문을 바꾸고 로봇을 다른 위치로 보내고 이름을 바꿀 수 있었다고 공개했다. [사실][^ref-1264][^ref-1265] 근거 두 기사는 같은 연구자 공개를 옮긴 것이라 교차 확인이 아니며, 실제 악용 사례는 보도되지 않았다.
- **20. 로봇·제조사 관제 연동 ↔ 52. 통신 보호·위협 관리·감사.** 미국 사이버보안·기반시설보안청(Cybersecurity and Infrastructure Security Agency, CISA) 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇 TUG를 제어하는 Home Base Server에서 인증 없이 웹소켓으로 로봇을 제어할 수 있는 취약점(공통 취약점 식별 번호(Common Vulnerabilities and Exposures, CVE) CVE-2022-1070, 공통 취약점 점수 체계(Common Vulnerability Scoring System, CVSS) 9.8)과 인가 누락 취약점을 공개했다. [사실][^ref-1107] 권고가 드는 방화벽·VPN 같은 망 조치는 시설 IT/OT 쪽 연계 대상이다.
- **20. 로봇·제조사 관제 연동 ↔ 51. 인증·권한·격리.** 식당 서빙 로봇과 병원 운반 로봇 사례 모두 제조사 플릿 서버·관리 API의 인증·인가 결함이 로봇 제어로 이어졌으므로, ROP가 제조사 관제를 연결할 때 연결 계정의 권한 범위와 인가 확인을 연동 승인 조건으로 둬야 할 것으로 보인다. [추정][^ref-1264][^ref-1107] 그런 인가 시험을 정한 공개 기준은 확인하지 못했다(oq-100).
- **[21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ 52. 통신 보호·위협 관리·감사.** VDA 5050 3.0.0은 범위 절에서 보안 통신·데이터 보호의 메커니즘·기술·절차를 정하지 않는다고 밝히고, 프로토콜 보안은 브로커 구성으로 다뤄야 하며 이 지침에서는 다루지 않는다고 적는다. [사실][^ref-031] 상호운용 규격이 통신 보안을 범위 밖 브로커 구성에 맡기므로 21. 상호운용 표준·적합성의 적합성 시험과 브로커·API의 상호 인증·TLS 설정 확인은 별도 경로로 관리해야 할 것으로 보이며, 그 최소 요구를 정한 공개 보안 프로파일은 확인하지 못했다. [추정][^ref-031][^ref-1105] 관련 질문은 oq-246이다.
- **[22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md) ↔ 51. 인증·권한·격리.** 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)도 같은 관리 API 결함의 대상이 될 수 있다고 보도되었으므로, 로봇 관제·설비 어댑터 구성요소를 SROS 2(Secure ROS 2) 인클레이브처럼 별도 신원·접근 규칙으로 나눠 설비 명령 권한을 제한하는 설계가 두 대분류의 경계가 될 것으로 보인다. [추정][^ref-1265][^ref-405] 승강기 제어 자체는 시설·설비 제어 경계의 연계 대상이다(oq-056).

### G. 계획·최적화

대분류 페이지: [G. 계획·최적화](../planning-and-optimization/index.md)

- **[25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md) ↔ 51. 인증·권한·격리.** Francos 외(2026-08, 프리프린트)는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했다. [사실][^ref-494] 실험은 GPS 스푸핑 데이터와 택시 수요로 했으며 물류센터 적용은 확인되지 않았다.
- **25. 작업 배정 — MRTA·[27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) ↔ 51. 인증·권한·격리.** 제조사 관리 API를 거쳐 주문을 바꾸거나 로봇 위치를 옮길 수 있었던 사례가 있으므로, ROP의 배정·교통 계획은 자신이 내리지 않은 임무 변경·이동을 로봇 상태에서 감지해 해당 로봇을 계획에서 보류하는 규칙이 필요할 것으로 보인다. [추정][^ref-1264] 계획 쪽 감지 규칙을 다룬 자료는 확인하지 못했다.

### H. 실행·협업·예외 복구

대분류 페이지: [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)

- **[29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) ↔ 51. 인증·권한·격리.** VDA 5050 3.0.0에서 updateCertificate 동작은 실행 중에는 인증서를 내려받아 설치하고 있다는 상태로, 실패하면 내려받기 또는 설치 실패로 보고되므로, 보안 명령도 일반 명령처럼 실행 확인·실패 처리 대상이 된다. [사실][^ref-031]
- **[32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) ↔ 52. 통신 보호·위협 관리·감사.** 식당 서빙 로봇 관리 API 결함으로 영업 중 플릿 전체 작업을 취소하거나 멈출 수 있었다는 보도는 연구자·매체의 가능성 평가이고 실제 사고는 보도되지 않았지만, 보안 사고로 플릿 일부·전체를 격리하고 수동 운영으로 넘어가는 시나리오가 32. 예외 복구·재계획·업무 연속성의 복구 절차에 들어가야 할 것으로 보인다. [추정][^ref-1264][^ref-1265]

### I. 설계·시뮬레이션

대분류 페이지: [I. 설계·시뮬레이션](../design-and-simulation/index.md)

- **[34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md) ↔ 52. 통신 보호·위협 관리·감사.** Carr 외(2022)는 ROS로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. [사실][^ref-1242]
- **34. 시뮬레이션·예측용 디지털 트윈·[36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md) ↔ 52. 통신 보호·위협 관리·감사·53. 개인정보·영상 데이터.** 가정한 미래를 실험하는 시뮬레이션과 실제 상황 재현에 운영 기록·영상을 입력으로 쓰면 그 기록의 무결성과 '재현' 목적의 이용 범위를 함께 정해야 할 것으로 보이며, 이는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 문제와 구분된다. [추정][^ref-1242][^ref-588] 관련 질문은 oq-306·oq-308이다.

### J. 현장 운영·관제

대분류 페이지: [J. 현장 운영·관제](../field-operations-and-monitoring/index.md)

- **[37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md) ↔ 52. 통신 보호·위협 관리·감사.** Fernández-Becerra 외(2024-03)는 자율 에이전트의 행동을 블록체인 기반 기록과 대규모 언어 모델 설명으로 남겨 책임 추적성과 설명 가능성을 높이는 구조를 제안했다. [사실][^ref-1110] 수백 대 규모의 지연·저장 비용은 oq-248로 열려 있다.
- **37. 관제 화면·실행 기록 ↔ 52. 통신 보호·위협 관리·감사.** 업계 해설에 따르면 EU 기계류 규정 (EU) 2023/1230은 변조 보호, 개입 증거 기록, 안전 소프트웨어 판 추적 로그를 요구하며 2027-01-20 전면 적용된다. [사실][^ref-1109] 규정 원문은 열지 못했고, 이 요구가 오케스트레이션 플랫폼에 미치는지는 oq-249로 열려 있다.
- **38. 모니터링·이상 탐지·원인 분석 ↔ 52. 통신 보호·위협 관리·감사.** 위 E. 사물·사람·실시간 상태 항목의 상태 교차 확인 추정이 38. 모니터링·이상 탐지·원인 분석에도 걸린다.
- **[40. 운영 절차·요청 창구](../field-operations-and-monitoring/operating-procedures-and-request-channels.md) ↔ 52. 통신 보호·위협 관리·감사.** Pudu 사례에서 연구자의 신고(2025-08-12 시작)는 응답을 받지 못하다가 고객사(Skylark Holdings·Zensho)에 알린 뒤에야 처리되었고, 제조사는 이후 취약점을 고치고 보안 대응 센터와 신고 주소를 만들었다. [사실][^ref-1264][^ref-1265] 지연 이유에 대해 The Register는 제조사가 보안 신고 창구가 없어 대응이 늦었다고 인정했다고 전하고, Hackmag은 제조사가 다른 경로로 보고를 받았다고 설명했다고 전한다. [사실][^ref-1264][^ref-1265] 두 기사는 같은 연구자 공개를 옮긴 것이라 교차 확인이 아니다.
- **40. 운영 절차·요청 창구, O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리, P. 거버넌스·법규·사회의 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md) ↔ 52. 통신 보호·위협 관리·감사.** EU 사이버복원력법(Cyber Resilience Act, CRA)에 따라 2026-09-11부터 디지털 요소 제품 제조자는 적극 악용되는 취약점과 중대 사고를 유럽연합 사이버보안청(ENISA) 단일 보고 플랫폼을 통해 주 사업장 국가의 컴퓨터 보안 사고 대응팀(Computer Security Incident Response Team, CSIRT)에 알려야 하며, 인지 후 24시간 안에 조기 경보와 72시간 안에 통지를 내고, 최종 보고는 취약점이면 시정 조치가 나온 뒤 14일 안에, 중대 사고면 72시간 통지 뒤 한 달 안에 낸다. [사실][^ref-1228] 이 내용은 집행위원회 안내 페이지 기준이며 규정 원문은 열지 않았다.
- **40. 운영 절차·요청 창구 ↔ 52. 통신 보호·위협 관리·감사.** 신고 창구가 없던 제조사 사례와 24·72시간 보고 시한을 함께 보면, 여러 제조사 로봇을 운영하는 현장의 요청 창구에 보안 취약점·사고 접수와 제조사·ROP 사업자 사이 통보 경로를 두는 일이 40. 운영 절차·요청 창구로 넘어갈 것으로 보인다. [추정][^ref-1228][^ref-1264] 보고 의무는 제조자에 걸리며, 플랫폼 사업자의 해당 여부는 oq-291로 열려 있다.

### K. 플랫폼 아키텍처·인프라

대분류 페이지: [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)

- **[41. 플랫폼 아키텍처·외부 API](../platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) ↔ 51. 인증·권한·격리.** Open-RMF 문서는 웹 대시보드를 TLS로 제공하고 OpenID Connect(OIDC)로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용하며, ROS 2 쪽 구성요소는 SROS 2 인클레이브로 권한을 나눈다고 설명한다. [사실][^ref-405]
- **[42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) ↔ 52. 통신 보호·위협 관리·감사.** ROS 2는 데이터 분산 서비스(Data Distribution Service, DDS) 보안 규격의 인증·접근 통제·암호화 플러그인을 쓰고, ROS 2 위협 모델 초안은 보안이 꺼진 시스템에서는 어떤 노드든 어떤 토픽에나 발행할 수 있어 신원 위조와 명령 가로채기가 가능하다고 정리한다. [사실][^ref-009][^ref-010]
- **[43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md) ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 2026-09-14 로봇청소기 점검 보도에 따르면 개인정보보호위원회는 점검 후속 조치로 접근권한 부여 내역 보관 기간을 200일에서 3년으로, 접속기록 보관 기간을 90일에서 2년 이상으로 늘리도록 했다. [사실][^ref-1268] 이 조치가 점검 사업자에만 해당하는지와 근거 조항은 기사에 없어 미확인이다(oq-214).

### L. AI·학습 기술

대분류 페이지: [L. AI·학습 기술](../ai-and-learning/index.md)

- **[45. 문서·도면·장면 이해](../ai-and-learning/document-drawing-and-scene-understanding.md)·[47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ 53. 개인정보·영상 데이터.** 개인정보보호위원회는 2023-11 자율주행차·이동형 로봇 개발에 영상데이터 원본 활용을 허용하는 방향을 밝혔고, 2026-05-06 ICT 규제샌드박스 심의위원회는 배달로봇 카메라 원본 영상을 AI 학습에 쓰는 과제에 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지 등을 조건으로 실증특례를 승인했다. [사실][^ref-1138][^ref-1263] 현장 유형으로는 Q. 현장 유형별 적용의 66. 실외 사례다.
- **47. AI·학습·적응과 모델 운영 ↔ 52. 통신 보호·위협 관리·감사.** EU AI Act 제12조는 고위험 AI 시스템이 수명 기간 동안 사건 기록(로그)을 자동으로 남길 수 있어야 하고, 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다. [사실][^ref-863] ROP의 AI 구성요소, 특히 13. 대화형 기능의 신뢰·기반이 다루는 대화 기능이 고위험에 해당하는지는 oq-106·oq-143으로 열려 있다.
- **44. 로봇 기반 모델·언어 모델 계획 ↔ 52. 통신 보호·위협 관리·감사.** 탈옥·가드레일 연구는 위 C. 채팅 기반 구성·운영 항목에 적용 대상 영역과 함께 적었다.

### M. 안전

대분류 페이지: [M. 안전](../safety/index.md)

- **[50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md) ↔ 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사.** 산업용 로봇 안전 표준 ISO 10218-1/-2의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. [사실][^ref-1116][^ref-1076] 업계 해설과 판 비교 논문이 같은 내용을 전하지만 조항 번호는 미확인이다(oq-102).
- **50. 안전 표준·인증·사고 조사 ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 서비스 로봇 안전 표준 ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 사이버보안과 데이터 보호 절을 새로 넣었다. [사실][^ref-1260] 최종판에 남았는지는 미확인이다(oq-254).
- **[48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ 52. 통신 보호·위협 관리·감사.** Quarta 외(IEEE S&P 2017)는 널리 쓰이는 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 것으로 보이며(검색 결과 요약 기준), 제어기 보안은 로봇 제조사 쪽 연계 대상이다. [추정][^ref-1114]
- **48. 안전·위험 관리 ↔ 51. 인증·권한·격리.** 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제가 안전 평가 대상이 될 것으로 보인다. [추정][^ref-1116][^ref-1260] 로봇 자체 안전 기능은 연계 대상이다.

### O. 검증·도입·수명주기

대분류 페이지: [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)

- **[54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) ↔ 52. 통신 보호·위협 관리·감사.** 2025년 한국인터넷진흥원·한국소비자원의 로봇청소기 6종 점검은 모바일앱 보안·정책 관리·기기 보안 3개 영역 40개 항목으로 이루어졌다고 보도되어, 로봇 보안 시험 항목의 국내 참고 틀이 될 것으로 보인다. [추정][^ref-969] 다중 로봇 관제 플랫폼에 같은 틀을 쓴 사례는 확인하지 못했다.
- **[55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) ↔ 52. 통신 보호·위협 관리·감사.** ROS 2 위협 모델 초안이 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 들므로, 설치·시운전 점검 항목에 기본 자격증명 변경과 원격 접속 범위 확인이 들어가야 할 것으로 보인다. [추정][^ref-010]
- **57. 자산·소프트웨어 수명주기 관리 ↔ 52. 통신 보호·위협 관리·감사.** ROS 2 위협 모델 초안은 빌드 팜과 서드파티 구성요소를 통한 공급망 위협을 주요 위협으로 들고, Shen 외(2026-09)는 제3자 Docker 컨테이너·보조 도구에 대한 폭넓은 의존을 이용해 악성 훅이 든 패키지를 퍼뜨릴 수 있다고 적는다. [사실][^ref-010][^ref-1272] 위 B. 로봇 온톨로지 항목의 인증서 교체 이력과 J. 현장 운영·관제 항목의 사이버복원력법 보고 의무도 57. 자산·소프트웨어 수명주기 관리로 이어진다.

### P. 거버넌스·법규·사회

대분류 페이지: [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)

- **[58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md) ↔ 53. 개인정보·영상 데이터.** EU 데이터법은 2025-09-12부터 적용되며, 로봇·산업 기계 같은 연결 제품의 사용자가 사용으로 생긴 데이터에 접근해 직접 쓰거나 제3자와 공유할 수 있게 하고, 데이터 보유자는 사용자와 계약을 두고 생성 데이터 종류·양·수집 빈도를 알려야 한다. [사실][^ref-1274] 여러 제조사 로봇의 데이터를 모아 관제하는 ROP 사업자가 데이터법상 사용자·제3자 가운데 어느 쪽이고 개인정보 처리에서 운영자·수탁자 가운데 어느 쪽인지가 계약으로 정해야 할 쟁점이 될 것으로 보인다. [추정][^ref-1274][^ref-588] 플랫폼 사업자 지위를 다룬 해석은 확인하지 못했다(oq-259).
- **59. 법·규제·보험·라이선스 ↔ 53. 개인정보·영상 데이터.** 개인정보보호위원회 이동형 영상정보처리기기 안내서 공개 보도와 법률사무소 해설은 카메라를 단 자율주행차·배달로봇이 외부에 촬영 사실을 표시하고 명확히 거부하는 사람의 의사를 받아들여야 한다고 전한다. [사실][^ref-1136][^ref-588] 두 출처는 같은 안내서 발표를 옮긴 것이라 독립 교차 확인이 아니며, 위 J. 현장 운영·관제 항목의 사이버복원력법 보고 의무도 59. 법·규제·보험·라이선스와 이어진다.
- **[60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md) ↔ 53. 개인정보·영상 데이터.** 프랑스 개인정보 감독기관 CNIL은 2023-12-27 결정(2024-01-23 공표)으로 Amazon France Logistique에 3,200만 유로 과징금을 부과했는데, 물류창고 작업자 스캐너 기록으로 10분 넘는 비활동을 실시간 경보하고 1.25초 안의 빠른 스캔을 표시하는 지표와 모든 데이터·지표의 31일 보관을 과도하다고 보았다. [사실][^ref-1266][^ref-1267] 이 사례는 로봇이 아니라 작업자 휴대 스캐너 기록에 관한 것이며, Amazon은 사실과 다르다며 이의 제기 권리를 유보했다. [사실][^ref-1266]
- **60. 노동·수용성·접근성, J. 현장 운영·관제의 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ 53. 개인정보·영상 데이터.** 작업자 스캐너 기록의 개인별 비활동·속도 지표가 과도한 감시로 판단된 사례가 있으므로, ROP가 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록할 때 39. 운영 성과 측정·개선의 지표를 집계 단위로 두고 보존 기간을 줄이는 설계가 필요할 것으로 보인다. [추정][^ref-1266][^ref-589] 로봇 연동 지표에 이 판단이 적용된 사례는 확인하지 못했다(oq-285).
- **60. 노동·수용성·접근성 ↔ 53. 개인정보·영상 데이터.** 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 둔다. [사실][^ref-589] 카메라 로봇이 감시 설비에 해당하는지는 oq-099로 열려 있다.

### Q. 현장 유형별 적용

대분류 페이지: [Q. 현장 유형별 적용](../site-type-applications/index.md). 현장마다 다른 요구는 Q. 현장 유형별 적용에 모으고 공통 기능은 위 대분류에 두므로, 위 사례를 현장 유형별로 다시 묶는다.

- **[61. 물류창고](../site-type-applications/warehouse.md):** 위 P. 거버넌스·법규·사회 항목의 CNIL 사례는 물류창고에서 일어났지만 로봇이 아닌 작업자 스캐너 기록 사례라 ROP 적용 사례로 보지 않는다.
- **[62. 제조 공장](../site-type-applications/manufacturing-plant.md):** 산업용 로봇 제어기 취약점 실험(M. 안전 항목).
- **[63. 병원·의료](../site-type-applications/hospital-and-healthcare.md):** TUG 플릿 서버 취약점(F. 연동 항목)과 Zena RX 잠금 칸 인증(E. 사물·사람·실시간 상태 항목, 벤더 주장)이 있다. 진료실을 흉내 낸 모의 시나리오에서 의사·환자를 알아보도록 학습한 서비스 로봇은 대상이 아닌 사람의 얼굴을 안정적으로 가렸지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮췄다. [사실][^ref-1146] 실제 병원 도입이 아닌 모의 실험이며, 기기 쪽 얼굴 가림은 제조사 기능의 연계 대상이다.
- **[64. 상업 시설](../site-type-applications/commercial-facilities.md):** Pudu 식당 서빙 로봇의 관리 API 결함과 신고 지연(F. 연동, H. 실행·협업·예외 복구, J. 현장 운영·관제 항목).
- **[65. 가정·공동주택](../site-type-applications/home-and-apartment.md):** 로봇청소기 지도 저장 위치(D. 공간·지도 모델 항목), 접근권한 내역·접속기록 보관 기간(K. 플랫폼 아키텍처·인프라 항목), 보안 점검 40개 항목(O. 검증·도입·수명주기 항목).
- **[66. 실외](../site-type-applications/outdoor.md):** 배달로봇 원본 영상 실증특례(L. AI·학습 기술 항목), 촬영 사실 표시·거부 수용(P. 거버넌스·법규·사회 항목).
- **[67. 기타 현장](../site-type-applications/other-sites.md):** 같은 Pudu 결함 보도는 사무실에서 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)이 사무실 시스템을 망가뜨리거나 지식재산을 빼내는 데 쓰일 수 있다고 평가했는데, 이는 연구자·매체의 가능성 평가이며 확인된 사고는 아니다. [추정][^ref-1265][^ref-1264]

### 아직 다루지 않은 연결

이번 근거로는 N. 보안·개인정보와의 연결을 찾지 못한 세부영역이다. 다음 대분류 연결 실행이나 해당 영역 실행에서 다룬다.

- B. 로봇 온톨로지: 5. 로봇 능력·작업 표현
- C. 채팅 기반 구성·운영: 8. 채팅으로 맵 작성, 9. 채팅으로 시나리오 구성, 10. 채팅으로 로봇 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현
- F. 연동: 23. 업무 시스템 연동
- G. 계획·최적화: 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화
- H. 실행·협업·예외 복구: 30. 로봇 간 협업·물리적 인계
- I. 설계·시뮬레이션: 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계
- L. AI·학습 기술: 46. 예측·학습 기반 최적화
- M. 안전: 49. 사람 근접 안전
- O. 검증·도입·수명주기: 56. 운영 이관·확대·교육

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 45건이다(논문 13건 · 기사·보고서 11건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 21건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1145](../../references/ref-1145.md) — Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports (발행 2026-09-02)
- [ref-1112](../../references/ref-1112.md) — Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems (발행 2026-08)
- [ref-1144](../../references/ref-1144.md) — Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences (발행 2026-04-07)
- [ref-1146](../../references/ref-1146.md) — Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting (발행 2026-03-16)
- [ref-585](../../references/ref-585.md) — Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52), Security Aspects of Zones and Conduits in IEC 62443 (발행 2026)
- [ref-1108](../../references/ref-1108.md) — Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot (발행 2025-09-17)
- [ref-1143](../../references/ref-1143.md) — Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception (발행 2025-05-08)
- [ref-700](../../references/ref-700.md) — Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots (발행 2025-03)
- [ref-857](../../references/ref-857.md) — Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots (발행 2024-11-09)
- [ref-1113](../../references/ref-1113.md) — Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems (발행 2024-08)
- 그 밖에 3건

**기사·보고서**

- [ref-1141](../../references/ref-1141.md) — 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) (발행 2026-09-14)
- [ref-1109](../../references/ref-1109.md) — IES (Integrated Equipment Services), Machinery Regulation Guide (발행 2026-08-27)
- [ref-1111](../../references/ref-1111.md) — 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시 (발행 2026-03-06)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-1140](../../references/ref-1140.md) — 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인) (발행 2025-09-02)
- [ref-1136](../../references/ref-1136.md) — 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" (발행 2024-10-14)
- [ref-1139](../../references/ref-1139.md) — 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터) (발행 2024-02-08)
- [ref-968](../../references/ref-968.md) — MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? (발행 2022-12-19)
- [ref-588](../../references/ref-588.md) — 김·장 법률사무소, '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 (발행 미확인)
- [ref-471](../../references/ref-471.md) — A3(Association for Advancing Automation), Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) (발행 미확인)
- 그 밖에 1건

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-1135](../../references/ref-1135.md) — 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.) (발행 2024-10-14)
- [ref-1138](../../references/ref-1138.md) — 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용 (발행 2023-11-15)
- [ref-582](../../references/ref-582.md) — NIST, NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (발행 2023-09)
- [ref-555](../../references/ref-555.md) — European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery (발행 2023-06)
- [ref-1107](../../references/ref-1107.md) — CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05) (발행 2022-04-12)
- [ref-580](../../references/ref-580.md) — Open Robotics (ROS 2 Design), ROS 2 Security Enclaves (발행 2020-05)
- [ref-1147](../../references/ref-1147.md) — European Data Protection Board (EDPB), Guidelines 3/2019 on processing of personal data through video devices (발행 2020-01)
- [ref-579](../../references/ref-579.md) — Open Robotics (ROS 2 Design), ROS 2 Access Control Policies (발행 2019-08)
- [ref-584](../../references/ref-584.md) — CSA / IEC (ANSI Webstore), CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) (발행 2013-08)
- [ref-591](../../references/ref-591.md) — European Commission (Shaping Europe's digital future), The Cyber Resilience Act - Summary of the legislative text (발행 미확인)
- 그 밖에 11건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [53. 개인정보·영상 데이터](privacy-and-video-data.md) — seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계, 연결 16개 영역, 열린 질문 11건), 13절 각주, 1차 수정 15건·2차 수정 4건 반영 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area53-s6.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "6. 대표 접근법과 기술" 절(1,883자)을 옮겼다 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 열린 질문](../../topics/2026/2026-09-30-area53-s11.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "11. 열린 질문" 절을 옮겼다. 2차 수정: 기존 질문 7건을 등록 문장 그대로 옮기고 부분 근거 메모 2건에 [추정]·각주, EDPB 풀어쓰기 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 대표 연구와 자료](../../topics/2026/2026-09-30-area53-s8.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Xu·Ayday 항목의 플랫폼 필드 설계 연결 문장을 [추정]으로 분리 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area53-s4.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "4. 핵심 개념과 용어" 절(1,008자)을 옮겼다 (실행 2026-09-30-16)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [9]는 참고문헌 [ref-009](../../references/ref-009.md)에 해당한다.[^ref-009] 원문의 [10]은 참고문헌 [ref-010](../../references/ref-010.md)에 해당한다.[^ref-010]

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-10-09
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-10-09 (원문 미열람)
[^ref-579]: Open Robotics (ROS 2 Design), ROS 2 Access Control Policies, 2019-08, https://design.ros2.org/articles/ros2_access_control_policies.html, 접근일 2026-10-09
[^ref-588]: 김·장 법률사무소, '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트, 미확인, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-10-09 (원문 미열람)
[^ref-589]: 법제처 국가법령정보센터, 근로자참여 및 협력증진에 관한 법률, 미확인, https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636, 접근일 2026-10-09 (원문 미열람)
[^ref-700]: Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09 (원문 미열람)
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-10-09 (원문 미열람)
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-10-09 (원문 미열람)
[^ref-969]: 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은?, 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-10-09 (원문 미열람)
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-10-09 (원문 미열람)
[^ref-1105]: IEC (SyC Smart Energy), IEC 62443, 미확인, https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/, 접근일 2026-10-09 (원문 미열람)
[^ref-1106]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-10-09 (원문 미열람)
[^ref-1107]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-10-09 (원문 미열람)
[^ref-1109]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-10-09 (원문 미열람)
[^ref-1110]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-10-09 (원문 미열람)
[^ref-1111]: 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시, 2026-03-06, https://www.mstoday.co.kr/news/articleView.html?idxno=100755, 접근일 2026-10-09 (원문 미열람)
[^ref-1112]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-10-09 (원문 미열람)
[^ref-1113]: Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems, 2024-08, https://arxiv.org/abs/2408.03515, 접근일 2026-10-09 (원문 미열람)
[^ref-1114]: Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017), An Experimental Security Analysis of an Industrial Robot Controller, 2017, https://files01.core.ac.uk/download/pdf/84891817.pdf, 접근일 2026-10-09 (원문 미열람)
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-10-09 (원문 미열람)
[^ref-1136]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-10-09 (원문 미열람)
[^ref-1138]: 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용, 2023-11-15, https://www.korea.kr/news/policyNewsView.do?newsId=148922669, 접근일 2026-10-09 (원문 미열람)
[^ref-1141]: 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인), 2026-09-14, https://view.asiae.co.kr/article/2026091410054053414, 접근일 2026-10-09 (원문 미열람)
[^ref-1145]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-10-09 (원문 미열람)
[^ref-1146]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-10-09 (원문 미열람)
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09 (원문 미열람)
[^ref-1299]: ST Engineering Aethon (Newswire 게재 보도자료), ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals, 2024-04-29, https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264, 접근일 2026-10-09 (원문 미열람)
[^ref-1301]: 경향신문 (곽희양), 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다, 2020-07-03, https://www.khan.co.kr/article/202007031130001, 접근일 2026-10-09 (원문 미열람)
[^ref-1242]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09 (원문 미열람)
[^ref-1263]: 메트로신문, AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원, 2026-05-06, https://www.metroseoul.co.kr/article/20260506500296, 접근일 2026-10-09 (원문 미열람)
[^ref-1228]: European Commission (Shaping Europe's digital future), CRA reporting, 미확인(페이지 최종 갱신 2026-09-11), https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-10-09
[^ref-1264]: The Register, Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots, 2025-08-29, https://www.theregister.com/2025/08/29/pudu_robots_hackable/, 접근일 2026-10-09
[^ref-1265]: Hackmag, Researcher finds a way to hack Chinese Pudu service robots, 2025-09-05, https://hackmag.com/news/pudu-bugs, 접근일 2026-10-09
[^ref-1266]: Silicon UK, France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance, 2024-01-23, https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858, 접근일 2026-10-09
[^ref-1267]: CNIL (Commission nationale de l'informatique et des libertés), Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million, 2024-01-23, https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million, 접근일 2026-10-09 (원문 미열람)
[^ref-1268]: 바이라인네트워크 (곽중희), 개인정보위 "로봇청소기 5개 브랜드, 특별한 침해 위험 없어", 2026-09-14, https://byline.network/2026/09/14-623/, 접근일 2026-10-09
[^ref-1269]: 바이라인네트워크, 과기정통부, 선박·우주·로봇 보안 매뉴얼 공개, 2026-03-06, https://byline.network/2026/03/6-340/, 접근일 2026-10-09
[^ref-1272]: Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv), Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics, 2026-09-08, https://arxiv.org/abs/2609.08280, 접근일 2026-10-09
[^ref-1273]: KUKA (Robotics Tomorrow 게재 보도자료), KUKA is First to Achieve Security Level 2 Certification for Robotics Industry, 2026-09-02, https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/, 접근일 2026-10-09
[^ref-1274]: European Commission (Shaping Europe's digital future), Data Act explained, 미확인(페이지 최종 갱신 2025-12-15), https://digital-strategy.ec.europa.eu/en/policies/data-act-explained, 접근일 2026-10-09
[^ref-1260]: DIN Media, DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024), 2024-10, https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303, 접근일 2026-10-09 (원문 미열람)
