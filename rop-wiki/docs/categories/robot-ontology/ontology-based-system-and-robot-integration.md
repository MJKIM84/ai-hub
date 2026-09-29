---
title: "6. 온톨로지 기반 시스템·로봇 연동"
type: area
category: "B. 로봇 온톨로지"
area_no: 6
related_areas: [4, 5, 7, 18, 20, 21, 22, 25, 29, 45, 47, 63]
tags: [능력·스킬·서비스 모델, 스킬 인터페이스, 능력 매칭, 플릿 어댑터, 전제조건 검사, 자산관리셸]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-038, ref-201, ref-037, ref-249, ref-876, ref-877, ref-878, ref-879, ref-229, ref-880, ref-881, ref-882, ref-883, ref-884, ref-885, ref-153, ref-869, ref-465]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [B. 로봇 온톨로지](index.md) › 6. 온톨로지 기반 시스템·로봇 연동

# 6. 온톨로지 기반 시스템·로봇 연동

!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-29 · 마지막 실행: 2026-09-29
<!-- auto:page-status:end -->

## 1. 한 줄 정의

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]

## 3. 왜 중요한가

이 영역이 없으면 로봇을 한 대 더 들이거나 새 업무 시스템을 붙일 때마다 사람이 능력 목록을 다시 읽고 어댑터를 손으로 맞추는 일이 반복된다. Vieira da Silva·Köcher·Fay(2022, 2023 개정)는 이기종 자율 로봇 팀에서 각 로봇이 제공하는 기능을 일관되게 기술하는 방법이 없다고 지적하고, 제조업의 능력·스킬 모델링 접근을 자율 로봇에 적용한 능력 모델을 제안했다. [사실][^ref-038]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 왜 중요한가](../../topics/2026/2026-09-29-area06-s3.md)에 있다.

## 4. 핵심 개념과 용어

**능력·스킬·서비스(Capability, Skill, Service, CSS)** — Plattform Industrie 4.0 의 [능력·스킬·서비스 모델](../../glossary/capabilities-skills-services.md)을 구현한 CSS 온톨로지는 능력을 산업 생산에서 효과를 내는 기능의 구현 독립적 명세로, [스킬](../../glossary/skill.md)을 능력을 구현한 실행 가능한 자동화 기능으로, 서비스를 제공 능력의 상업적 측면 기술로 정의한다(2026-09-29 확인). [사실][^ref-878]
- **스킬 인터페이스(Skill Interface)** — 같은 온톨로지는 스킬마다 외부 제어를 위한 스킬 인터페이스(예: OPC UA 서버)를 가져야 한다고 둔다.

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area06-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인된 현장 사례는 병원 둘과 기타(오피스 빌딩) 하나다. 제조 공장·물류창고의 현장 사례는 확인되지 않았으며, 제조 관련 자료(탐페레대학교의 능력 매치메이킹, 자산관리셸에서 계획 문제 생성)는 생산 시스템 설계와 실험실 수준의 검증이다. [사실][^ref-885][^ref-201]

**현장 유형:** 병원

**사례:** 의료센터 물류 운반과 다중 로봇 플릿 조정을 온톨로지로 검사하는 시뮬레이션(HERON)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 의료센터 안의 물류 운반 요청과 다중 로봇 플릿 조정 시나리오. 임상 배치가 아니라 시뮬레이션이다. [사실][^ref-880] |
| 작업 대상 | 의료센터 안에서 운반되는 물품과 그 운반 작업 정보 [사실][^ref-880] |
| 수행 자원 | 다중 로봇 플릿과 온톨로지 추론기(SPARQL 질의·SHACL 형상) [사실][^ref-880] |
| 제약 | 특정 작업에 대한 에이전트 자격과 전제조건(SPARQL 검사), 역할 기반 권한·오버라이드 승인 같은 기관 정책(SHACL 검증) [사실][^ref-880] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(임상 배치 없이 시뮬레이션으로 시연했으므로 처리량·시간 성과가 없다) [사실][^ref-880] |

Ioannidou 외(Healthcare, 2025)의 의료 로봇 상위 온톨로지 HERON 은 SPARQL 질의로 특정 작업에 대한 에이전트 자격과 전제조건을 검사하고 [형상 제약 언어](../../glossary/shacl.md)(Shapes Constraint Language, SHACL) 형상으로 역할 기반 권한·오버라이드 승인 같은 기관 정책 준수를 검증하며, 임상 배치 없이 Fundació Ave Maria 의료센터의 물류 운반·다중 로봇 플릿 조정 시뮬레이션 시나리오로 시연했다. [사실][^ref-880] 이 영역 관점에서 이 사례는 제약 항목의 실행 시점 조건 판단에 관여한다. 역할 기반 권한·오버라이드 정책 자체는 48. 안전·위험 관리와 51. 인증·권한·격리의 범위와 겹치므로 여기서는 조건 검사 사례로만 다룬다. 배터리·문·승강기 같은 구체 상태 조건은 이 사례에서 확인되지 않았다.

**현장 유형:** 병원

**사례:** 타르투대학교병원 이기종 플릿 현장 시험에서 프로그램 제어가 없는 문 통과

| 항목 | 내용 |
|---|---|
| 시작 조건 | [Open-RMF](../../glossary/open-rmf.md) 로 등록·운용한 이기종 이동로봇 플릿의 병원 내 작업 [사실][^ref-869] |
| 작업 대상 | 미확인 |
| 수행 자원 | PAL Robotics TIAGo 로봇, FreeFleet 클라이언트·서버와 RMF 어댑터 파일, 카드 인식·근접 센서를 대신 작동시키는 서보 장치 [사실][^ref-869] |
| 제약 | 프로그램 제어가 없는 병원 문 [사실][^ref-869] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

Valner 외(2022)의 현장 시험은 로봇 쪽 등록은 어댑터 파일로 처리했지만, 프로그램 제어가 없는 문은 서보 장치를 만들어 지나야 했다. [사실][^ref-869] 온톨로지·설정 기반 연동이 닿지 않는 설비가 현장에 남는다는 점에서 이 영역의 한계를 보여주는 사례다. 이 근거는 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md)에서도 같은 각주로 쓴다.

**현장 유형:** 기타

**사례:** 싱가포르 Galen 오피스 빌딩에서 개방 API 승강기와 RMF 로 로봇이 여러 층을 오가는 시험 환경

| 항목 | 내용 |
|---|---|
| 시작 조건 | 청소·보안·배송·컨시어지 등 여러 층에 걸친 로봇 작업이 층 이동을 요구할 때 [사실][^ref-884] |
| 작업 대상 | 건물의 층간 공간(승강기와 각 층) [사실][^ref-884] |
| 수행 자원 | 자율이동로봇, 개방 API 를 가진 KONE DX 급 승강기, RMF. 창이종합병원 CHART·KONE·Smart Urban Co-Innovation Lab·AWS·CapitaLand 가 참여 [사실][^ref-884] |
| 제약 | 승강기가 개방 API 로 현대화되어 있어야 한다 [사실][^ref-884] |
| 완료·인계 | 미확인 |
| 예외·성과 | 업체 수와 정량 결과는 공개 페이지에 없다(2026-09-29 확인) [사실][^ref-884] |

창이종합병원 CHART 는 캐피털랜드 Galen 오피스 빌딩을 로봇–승강기 연동의 실환경 시험장으로 두고, 여러 업체 로봇으로 시험을 확대할 계획을 밝혔다. [사실][^ref-884] 승강기 개방 API 연동 자체는 22. 설비·건물 시스템 연동의 범위이며, 이 영역에서는 플랫폼 기반 이기종 로봇의 층간 이동 시험 환경 사례로만 둔다.

## 6. 대표 접근법과 기술

작업·요구에 맞는 로봇·자원 후보를 능력 기술을 근거로 찾는 접근은 서로 다른 세 연구 그룹(LAAS 의 구성요소 기반 능력 추론, 탐페레대학교의 능력 매치메이킹, 헬무트 슈미트 대학의 이기종 로봇 능력 모델)에서 확인된다. [사실][^ref-249][^ref-885][^ref-038] Dussard 외는 구성요소에서 추론한 능력으로 로봇이 배정될 수 있는 작업과 없는 작업을 정한다. [사실][^ref-249]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area06-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준·오픈소스 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다. 용어는 [스킬](../../glossary/skill.md), [능력 기술 서브모델](../../glossary/capability-description-submodel.md), [플릿 어댑터](../../glossary/fleet-adapter.md), [VDA 5050 팩트시트](../../glossary/vda-5050-factsheet.md)를 참고한다.

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area06-s7.md)에 있다.

## 8. 대표 연구와 자료

Vieira da Silva, L. M., Köcher, A., & Fay, A., A Capability and Skill Model for Heterogeneous Autonomous Robots(2022, 2023 개정) — 이기종 자율 로봇의 기능을 일관되게 기술할 방법이 없다는 문제에서 출발해 제조업 능력·스킬 모델링을 자율 로봇에 확장했다. 이 영역의 문제 정의를 주는 자료다. [사실][^ref-038]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 대표 연구와 자료](../../topics/2026/2026-09-29-area06-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 능력 온톨로지 질의로 후보 로봇을 찾는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안, 스킬 인터페이스 호출과 상태·실패·완료 확인 | 스킬의 내부 구현과 상태 기계 실행(OPC UA 서버·로봇 SDK 쪽), 실행 성능 |
| 시설·설비 제어 | 실행 전 문·승강기 상태 확인, 승강기 사용 요청과 인계 | 승강기 제조사의 개방 API 와 설비 제어 자체 |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 능력 온톨로지 질의로 후보 로봇을 찾아 근거와 함께 돌려주는 기능, 능력→스킬→인터페이스 매핑표와 그 검토·승인 기록, 어댑터 설정·핸들러 초안 생성, 실행 전 전제조건·정책 검사(배터리·문·승강기 상태)다. 근거를 함께 돌려주는 설명 기능과 검토되지 않은 연결의 실행 차단은 확인한 출처 어디에도 명시되지 않아 ROP 가 따로 설계해야 할 요구로 보이며, Open-RMF 의 consider 콜백과 HERON 의 SHACL 정책 검사가 승인 관문의 부분 선례다. [추정][^ref-878][^ref-876][^ref-881][^ref-880]

연계 대상: 스킬의 내부 구현과 상태 기계 실행, 승강기 제조사의 개방 API 자체는 분류 원문 19장의 "로봇 자체 지능·제어"와 "시설·설비 제어" 경계 쪽이다. 이종 제조사를 잇는 ROP 는 스킬 인터페이스 호출·상태 확인·완료 판정과 승강기 사용 요청·인계만 맡고 구현 성능은 제조사·설비 측에 맡겨야 할 것으로 보인다. [추정][^ref-882][^ref-884][^ref-878] 이 경계는 제품 전략에 따라 이동할 수 있으며, 기준은 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 능력 표현을 주는 5. 로봇 능력·작업 표현과 등록 데이터를 주는 4. 이기종 로봇 등록, 매핑·제약을 검증하는 7. 온톨로지 검증·변경 관리를 앞뒤로 두고, 연동·배정·실행 영역으로 이어진다. [추정][^ref-876][^ref-229][^ref-880][^ref-465]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area06-s10.md)에 있다.

## 11. 열린 질문

**oq-150** (상태: 열림 · 실행 2026-09-29-08 부분 진전) 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? — Open-RMF 의 task_capabilities·action_categories 로 청소·수동 제어 같은 팩트시트에 없는 능력을 선언하는 방법은 공식 문서로 확인되지만, 문 열기·승강기 사용은 사용자 정의 동작이 아니라 플랫폼 기능이라 그 경로로 등록하지 않으며, 자산관리셸 능력 기술 서브모델을 로봇 현장에서 실제로 썼다는 사례는 확인되지 않아 미해결로 남는다. [추정][^ref-876][^ref-229][^ref-153]

자세한 내용은 주제 페이지 [6. 온톨로지 기반 시스템·로봇 연동 — 열린 질문](../../topics/2026/2026-09-29-area06-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-29 · 갱신 · [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md) — 영역 심화: 섹션 3~11 신규 작성(finding 28건 반영, 1차 조건부 승인 수정 13건·2차 수정 2건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2 (실행 2026-09-29-08)
- 2026-09-29 · 생성 · [6. 온톨로지 기반 시스템·로봇 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area06-s6.md) — 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "6. 대표 접근법과 기술" 절(3,102자)을 옮겼다 (실행 2026-09-29-08)
- 2026-09-29 · 생성 · [6. 온톨로지 기반 시스템·로봇 연동 — 대표 연구와 자료](../../topics/2026/2026-09-29-area06-s8.md) — 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "8. 대표 연구와 자료" 절(1,873자)을 옮겼다 (실행 2026-09-29-08)
- 2026-09-29 · 생성 · [6. 온톨로지 기반 시스템·로봇 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area06-s4.md) — 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "4. 핵심 개념과 용어" 절(1,115자)을 옮겼다 (실행 2026-09-29-08)
- 2026-09-29 · 생성 · [6. 온톨로지 기반 시스템·로봇 연동 — 열린 질문](../../topics/2026/2026-09-29-area06-s11.md) — 자동 분리: 6. 온톨로지 기반 시스템·로봇 연동 의 "11. 열린 질문" 절(1,074자)을 옮겼다 (실행 2026-09-29-08)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-038]: Vieira da Silva, L. M., Köcher, A., & Fay, A. (Helmut Schmidt University), A Capability and Skill Model for Heterogeneous Autonomous Robots, 2023-02-09, https://arxiv.org/abs/2209.10900, 접근일 2026-09-29
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. (IEEE CASE 2026 채택), From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06-01, https://arxiv.org/abs/2606.02167, 접근일 2026-09-29
[^ref-249]: Dussard, B., Sarthou, G., & Clodic, A. (LAAS-CNRS), Ontological Component-based Description of Robot Capabilities, 2025-09-10, https://arxiv.org/abs/2306.07569, 접근일 2026-09-29
[^ref-876]: Open Robotics (Programming Multiple Robots with ROS 2), User-defined Tasks - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task_userdefined.html, 접근일 2026-09-29
[^ref-878]: CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) GitHub 공식 저장소, CSS — An ontology for the Capability, Skill and Service model of Plattform Industrie 4.0 (README), 미확인, https://github.com/CaSkade-Automation/CSS, 접근일 2026-09-29
[^ref-229]: Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소, IDTA 02020 Submodel Template: Capability Description — README (published/Capability Description/1/0), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description, 접근일 2026-09-29 (원문 미열람)
[^ref-880]: Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics, 2025-04-30, https://pmc.ncbi.nlm.nih.gov/articles/PMC12071619/, 접근일 2026-09-29
[^ref-881]: ROS Index (InOrbit ros_amr_interop, 유지관리자 Leandro Pineda), vda5050_connector - ROS Package Overview, 미확인, https://index.ros.org/p/vda5050_connector/, 접근일 2026-09-29
[^ref-882]: Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. (FAIM 2021, Zenodo), An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell, 2021-11-03, https://zenodo.org/records/5648095, 접근일 2026-09-29
[^ref-884]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CGH-CHART), Robot-Lift Integration Challenge - Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h/robot-lift-integration-challenge, 접근일 2026-09-29
[^ref-885]: Järvenpää, E., Siltala, N., Hylli, O., & Lanz, M. (Tampere University, Procedia CIRP 97), Capability matchmaking software for rapid production system design and reconfiguration planning, 2021, https://researchportal.tuni.fi/en/publications/capability-matchmaking-software-for-rapid-production-system-desig/, 접근일 2026-09-29
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-29 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-10-18, https://arxiv.org/abs/2406.07962, 접근일 2026-09-29 (원문 미열람)
