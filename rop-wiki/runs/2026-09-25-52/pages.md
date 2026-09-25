# 스토리텔러 산출 2026-09-25-52

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | draft | 영역 심화: 3~11절 신규 작성, 13절 각주 19건, page-status 마커 추가, 트랙 반영 제안 중 재확인된 5건 반영 |
| create | docs/topics/2026/2026-09-25-area21-s6.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "6. 대표 접근법과 기술" 절(1,742자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area21-s7.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "7. 관련 표준·프레임워크·오픈소스" 절(936자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area21-s4.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "4. 핵심 개념과 용어" 절(914자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area21-s8.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "8. 대표 연구와 자료" 절(871자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 21. 온보딩·설정·현장 시운전 | 영역 심화: 3~11절 신규 작성(표준 등록 메시지·어댑터 설정·평면도 주석·반자동 지도 작성·가상 시운전, 적치 시나리오) | run 2026-09-25-52
- 홈 최근 업데이트: 2026-09-25 — 21. 온보딩·설정·현장 시운전: 영역 심화 초안 작성(등록 표준 메시지, 지도 정합, 반자동 지도 작성, 가상 시운전)
- 대분류 최근 업데이트: 2026-09-25 — 21. 온보딩·설정·현장 시운전: 3~11절 초안 작성, 적치 단계 새 제조사 AMR 시운전 시나리오
- 세부영역 최근 업데이트: 2026-09-25 — 21. 온보딩·설정·현장 시운전: 3~11절 신규 작성, 트랙 반영 제안 가운데 재확인된 5건 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 가상 시운전 | Virtual Commissioning | 제어 로직·로봇 프로그램·관제 설정을 현장 설치 전에 가상 모델과 연결해 시험함으로써 현장 시운전의 시간과 위험을 줄이려는 방법이다. | 21, 22 | ref-640 |
| new | 플러그 앤 프로듀스 | Plug and Produce | 새 설비나 자원을 연결하면 기술된 능력 정보를 바탕으로 최소한의 설정만으로 생산·작업에 투입되게 하려는 통합 방식이다. | 21, 5 | ref-636 |
| new | 신원 보고 | Identity Report (MassRobotics identityReport) | MassRobotics AMR 상호운용 표준에서 로봇이 제조사·모델·일련번호·외곽 치수와 선택적으로 속도·화물 한계·문서 위치를 알리는 메시지다. | 21, 9 | ref-601 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-569 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-601 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-629 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-630 | Open Robotics | Programming Multiple Robots with ROS 2 — traffic-editor | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-631 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-632 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020 Submodel Capability Description 1.0 — README | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-633 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-634 | Beinschob, P. 외 | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 |
| ref-635 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 논문 | medium | https://arxiv.org/abs/2404.13499 |
| ref-636 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 논문 | medium | https://arxiv.org/abs/2307.00827 |
| ref-637 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 논문 | medium | https://arxiv.org/abs/2406.07962 |
| ref-638 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-639 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 기사 | low | https://www.busan.com/view/busan/view.php?code=2026072420194685883 |
| ref-640 | Siemens Digital Industries Software | Virtual commissioning with Siemens solutions reduces launch time by three weeks | 벤더 문서 | low | https://resources.sw.siemens.com/en-US/case-study-idc/ |
| ref-641 | European Commission CORDIS | PAN-ROBOTS: Automating logistics for the factory of the future | 정부·연구기관 | medium | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future |
| ref-642 | 노주형, 강규리, 김연찬, 심현철 (한국로봇학회) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 |
| ref-643 | Open Robotics (open-rmf/rmf_site) | rmf_site — README (RMF Site Editor) | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_site |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? | 21, 9 | 열림 | — |
| new | — | 제조사 로봇 지도와 공통 관제 지도 사이 좌표 대응(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? | 21, 6, 23 | 열림 | — |
| new | — | 출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? | 21, 6 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 적치 | 시작 조건 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 작업 대상 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 수행 자원 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 제약 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 완료·인계 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 예외·성과 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| RMF Site Editor (rmf_site) | 오픈소스 | Open Robotics (open-rmf) | 21, 6 | ref-643 | https://github.com/open-rmf/rmf_site |

## 추가 조사 요청

- 트랙 반영 제안 가운데 이번 실행에서 다시 확인하지 않은 항목(MiR 평면도 업로드·축척 요건 벤더 주장 ref-271 등, 충전기 마커 등록 절차 ref-219, OTTO 설정 복제·부분 재지도화, Boniardi 외 2019, Beinschob·Reinke 2015 ref-266, 다중 AGV 경로망 자동 설계 IEEE T-ASE 2024 ref-267, Rüdt 외 2025 ref-268, 국내 건설로봇 문헌고찰)을 다음 21. 온보딩·설정·현장 시운전 실행에서 검증해 6·8절에 반영할지 판단해야 한다.
- 중복 id 병합 확인: ref-634↔ref-217(Beinschob 외 2017), ref-641↔ref-265(PAN-Robots CORDIS), ref-635↔ref-269(Heselden·Das 2024), ref-630↔ref-079(traffic-editor, 같은 URL), ref-633↔ref-046(LIF, 같은 URL), ref-638↔ref-470(ISO 3691-4, 같은 URL), ref-632↔ref-229(IDTA 02020, 같은 URL), ref-631↔ref-105 여부 — 퍼블리셔가 같은 URL 이면 기존 id 로 합쳐야 한다.
- 3절·5절의 설치 기간 단축 수치(PAN-Robots 6→2개월, Siemens 3주)를 독립 출처로 교차 확인할 자료가 필요하다(현재 과제·벤더 측 보고값뿐).
- 5절 완료·인계 칸: 현장 시운전의 합격 기준(지도 정합 오차, 위치 정확도 시험 방법)에 관한 표준·지침 근거가 필요하다(ISO 3691-4 시운전 절차 원문 또는 공인 해설).
- 7절: KTL–KILA 협약(2026-07-23)의 기관 보도자료 원문과 이후 실증 실적 확인이 필요하다.
- 11절 oq-022: 국내 물류센터의 CAD·BIM 도면 활용 사례를 추가 한국어 검색으로 찾아야 한다.

## 이행한 수정 지시

- f2 필수 절 정정 — 6절 '표준 메시지로 로봇 등록 정보 받기'에서 필수 여섯 절(과 헤더 필드)·선택 mobileRobotConfiguration 으로 고쳐 쓰고 [추정][^ref-629]로 강등했으며 7절 표 행도 [추정]으로 표기했다.
- f22 표현 정정 — 5절 제약 칸을 '팩트시트의 필수·선택 최상위 절과 신원 보고 필드'로 고쳐 쓰고 [추정]을 유지했다.
- f10 분리 — 6절에서 Full Control·Traffic Light 문장에 [사실][^ref-569], Read Only 문장에 [사실][^ref-004]를 붙이고 '온보딩 때 연동 수준이 선택 사항'은 별도 [추정] 문장으로 분리했으며 ref-004 각주는 공통 참고문헌 형식 줄을 그대로 옮겼다.
- f14 구절 삭제 — '사물인터넷 장치 개조나 외부 시스템 연동 없이'를 빼고 8절 연구 사례로만 두었으며 로봇 자체 기능 연구(연계 대상)임을 밝혔다.
- f20 비교 기준 — 4·5·6절에서 [추정] 벤더 주장을 유지하고 6절에 '현장 시운전만 한 유사 업그레이드 프로젝트(8주) 대비 3주 단축, 고속 분류기, Tecnomatix Plant Simulation'으로 적었으며 '코드를 설계와 대조 검증해 큰 변경 불필요' 구절은 뺐다.
- f4·f5 LIF 기준일 — 7절 표 아래에 'VDMA 2024-03 인용[^ref-031]'과 '1.0.0, 2023-09[^ref-633]'을 둘 다 제시하고, 11절과 open_question_updates 에 출처 충돌 질문을 올렸다.
- f12 — 3·5절에서 [추정]과 '과제 측 보고값, 비교 조건 미확인'을 유지하고, 6절에서 원인 설명은 'PAN-Robots 과제 측은 … 서술한다'로 과제 측 서술로만 적었다.
- 4절 용어 — '좌표 대응·좌표 정합'을 용어집 '지도 정합 (Map Alignment)'으로 통일하고 대응점 설정을 그 방법으로 설명했으며, 팩트시트·LIF·경로망·플릿 어댑터는 기존 용어집 링크만 걸고 glossary_updates 는 가상 시운전·플러그 앤 프로듀스·신원 보고 3건만 냈다.
- 각주 — ref-569·ref-632·ref-634~ref-642 각주 정의에 ' (원문 미열람)'을 붙이고 reference_updates 의 source_unopened 를 true 로 두었으며, ref-004 는 공통 참고문헌 각주 형식 줄을 그대로 복사했다.
- 10절 연결 — f17 을 5. 로봇 능력·작업 온톨로지와 27. AI·학습·적응과 모델 운영 양쪽에 연결했고, 22. 시뮬레이션·예측용 디지털 트윈 연결은 가상 시운전·팩트시트의 시뮬레이션 용도로 한정했으며 8. 실시간 세계 상태·데이터 일관성은 연결하지 않았다.
- 트랙 반영 제안 — traffic-editor(f8), 플릿 어댑터 설정(f7), Beinschob 외(f11), Heselden·Das(f13), PAN-Robots(f12)만 반영하고 MiR·OTTO 벤더 주장, Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 본문에서 빼고 additional_research_requests 에 다음 실행 후보로 적었다.
- f1 인용 위치 — 6절에서 'VDA 5050 3.0.0 표 2(4.3절)'로 적고 ref-031 직접 인용은 그 한 곳에서만 했다.
- 분량 초과 자동 분리: 21. 온보딩·설정·현장 시운전 본문 7,666자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,676자
