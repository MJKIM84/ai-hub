# 스토리텔러 산출 2026-09-25-61

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | draft | 영역 심화: seed → draft, 섹션 3~11 신규 작성(버전·지도·배터리·배포 복구·재평가, 가상 시나리오 2건), 페이지 상태 자동 영역 추가 |
| create | docs/topics/2026/2026-09-25-area24-s4.md | draft | 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "4. 핵심 개념과 용어" 절(1,365자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area24-s6.md | draft | 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "6. 대표 접근법과 기술" 절(1,327자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area24-s3.md | draft | 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "3. 왜 중요한가" 절(1,019자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area24-s7.md | draft | 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(982자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area24-s10.md | draft | 자동 분리: 24. 자산·소프트웨어 수명주기 관리 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(731자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 24. 자산·소프트웨어 수명주기 관리 | 영역 심화: 3~11절 신규 작성(버전·지도·배터리 열화·배포 복구·변경 후 재평가, 적치·출하 가상 시나리오) | run 2026-09-25-61
- 홈 최근 업데이트: 2026-09-25 — 24. 자산·소프트웨어 수명주기 관리: 영역 심화로 3~11절 첫 작성(펌웨어·지도 버전, 배터리 건강 상태, 배포·복구, 변경 후 재평가)
- 대분류 최근 업데이트: 2026-09-25 — 24. 자산·소프트웨어 수명주기 관리: 영역 심화로 3~11절 첫 작성, 열린 질문 4건 등록
- 세부영역 최근 업데이트: 2026-09-25 — 24. 자산·소프트웨어 수명주기 관리: 3~11절 신규 작성(실행 2026-09-25-61)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 상태 기반 정비 | Condition-Based Maintenance (CBM) | 정해진 주기 대신 상태 감시로 확인한 설비 상태에 따라 정비 여부와 시점을 정하는 정비 방식이다. | 24, 19 | ref-757, ref-754 |
| new | 배터리 건강 상태 | State of Health (SOH) | 배터리의 현재 용량·성능을 새 배터리 대비 비율로 나타낸 값으로, VDA 5050 상태 메시지의 batteryHealth 가 이에 해당한다. | 24, 16 | ref-051 |
| new | 소프트웨어 명판 | Software Nameplate (IDTA 02007) | 자산관리셸에서 소프트웨어 제품과 설치 인스턴스의 식별·버전·설치 정보를 통일된 형태로 기술하는 서브모델이다. | 24, 28 | ref-753 |
| new | 무선 업데이트 | Over-the-Air Update (OTA) | 기기를 회수하지 않고 네트워크로 소프트웨어·펌웨어를 내려받아 갱신하는 방식이다. | 24 | ref-760, ref-761 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-668 | Open Robotics (open-rmf) | rmf_simulation — README | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_simulation |
| ref-751 | Open Robotics (ROS 2 Design) | Managed nodes (ROS 2 Design: node_lifecycle) | 오픈소스 문서 | medium | https://design.ros2.org/articles/node_lifecycle.html |
| ref-752 | Open Robotics (ROS REP) | REP 2000 -- ROS 2 Releases and Target Platforms | 오픈소스 문서 | medium | https://www.ros.org/reps/rep-2000.html |
| ref-753 | IDTA (admin-shell-io/id GitHub) | IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing) | 표준 | medium | https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md |
| ref-754 | ISO | ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines | 표준 | medium | https://www.iso.org/standard/71194.html |
| ref-755 | ISO | ISO 55000:2024 - Asset management — Vocabulary, overview and principles | 표준 | medium | https://www.iso.org/standard/83053.html |
| ref-756 | arXiv (저자 미확인) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2603.22731 |
| ref-757 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 논문 | medium | https://link.springer.com/article/10.1007/s11431-024-2810-2 |
| ref-758 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 표준 | medium | https://webstore.iec.ch/en/publication/22811 |
| ref-759 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 정부·연구기관 | medium | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng |
| ref-760 | Amazon Web Services (aws-samples GitHub) | ros2-ota-firmware-updates — README | 벤더 문서 | low | https://github.com/aws-samples/ros2-ota-firmware-updates |
| ref-761 | 네이트 뉴스(원 매체 미확인) | 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장 | 기사 | low | https://m.news.nate.com/view/20260723n24828 |
| ref-762 | 한국로봇사용자협회 | 협동로봇 설치 작업장 안전인증 안내 | 업계 보고서 | medium | https://www.korua.or.kr/inspect/inspectInfo.do |
| ref-763 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 벤더 문서 | low | https://doc.safetics.io/insight-risk-assessment/ |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가? | 24, 23 | 열림 | — |
| new | — | VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? | 24, 9, 28 | 열림 | — |
| new | — | 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? | 24, 25 | 열림 | — |
| new | — | EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? | 24, 25 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 적치 | 시작 조건 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 적치 | 작업 대상 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 적치 | 수행 자원 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 적치 | 제약 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 적치 | 완료·인계 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 적치 | 예외·성과 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 출하 | 시작 조건 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 출하 | 작업 대상 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 출하 | 수행 자원 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |
| 출하 | 제약 | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 24. 자산·소프트웨어 수명주기 관리 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0) | 표준 | IDTA(Industrial Digital Twin Association) | 24, 28 | ref-753 | https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md |
| ISO 17359:2018 기계 상태 감시·진단 일반 지침 | 표준 | ISO | 24, 19 | ref-754 | https://www.iso.org/standard/71194.html |
| ISO 55000:2024 자산 관리 — 용어·개요·원칙 | 표준 | ISO (ISO/TC 251) | 24 | ref-755 | https://www.iso.org/standard/83053.html |
| IEC TR 62443-2-3:2015 IACS 환경의 패치 관리 | 표준 | IEC | 24, 26 | ref-758 | https://webstore.iec.ch/en/publication/22811 |
| REP 2000 ROS 2 Releases and Target Platforms | 프레임워크 | Open Robotics (ROS REP) | 24 | ref-752 | https://www.ros.org/reps/rep-2000.html |
| rmf_simulation (Open-RMF 시뮬레이션 플러그인) | 오픈소스 | Open Robotics (open-rmf) | 22, 24 | ref-668 | https://github.com/open-rmf/rmf_simulation |
| 협동로봇 설치 작업장 안전인증 | 평가 프로그램 | 한국로봇사용자협회 | 25, 24 | ref-762 | https://www.korua.or.kr/inspect/inspectInfo.do |

## 추가 조사 요청

- 4절: 예지보전(Predictive Maintenance) 정의를 뒷받침할 출처가 브리프에 없어 본문·용어집에 넣지 못했다 — 표준·검토 논문 출처로 정의를 확인해 달라.
- 전 절: 모든 핵심 주장이 단일 출처이므로 교차 확인이 필요하다(특히 REP 2000 지원 기간, VDA 5050 버전·지도 규칙, IDTA 02007 속성). 페이지 신뢰도를 높이려면 독립 출처가 필요하다.
- 3절·11절: EU 기계 규정에서 제조사가 예견한 소프트웨어 업데이트의 취급(실질적 변경 제외 여부)을 조문 원문이나 EU 공식 지침으로 확인해 달라 — 브리프에는 정의 조건만 있다.
- 3절·11절: 국내 협동로봇 설치 작업장 안전인증에서 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정 원문 확인이 필요하다.
- 6절·7절: 신규 출처 예산 도달로 빠진 ISO 13374, ISO 10218-1:2025 사이버보안 요구, CISA SBOM, 카나리 배포 연구를 다음 실행에서 조사해 달라.
- 참고문헌: ref-751 의 URL(https://design.ros2.org/articles/node_lifecycle.html)이 표준 목록의 기존 ref-364 와 같다 — 1차 검증 지시가 없어 브리프 id 를 그대로 썼으므로 퍼블리셔 병합 또는 다음 갱신에서 ref-364 로 통일할지 확인해 달라.
- 9절: '업데이트를 운영 시간대·일부 로봇 단위로 나눠 배포'하는 방식의 근거(단계적 배포·카나리 배포의 로봇 플릿 적용 사례)가 없어 구축자 추론으로만 남겼다.

## 이행한 수정 지시

- ref-749·ref-750 재사용 지시 — 본문 각주와 13절 정의, sources, reference_updates 에서 ref-749 를 ref-031(VDA5050_EN.md)로, ref-750 을 ref-051(state.schema)로 바꾸고 ref-749·ref-750 은 등록하지 않았다.
- f13 축소 지시 — 4절 '자산 관리' 항목에 제2판·2024-07·ISO/TC 251·2014판 대체·용어·개요·원칙·모든 유형의 자산 적용만 [사실]로 쓰고 '하드웨어·소프트웨어·설비 포함'과 '수명주기 단계별 평가' 구절은 넣지 않았다.
- f17 분리 지시 — 3절에 '제조사가 예견·계획하지 않은' 조건을 넣은 실질적 변경 정의를 [사실]로, 소프트웨어 업데이트가 판단 대상이 될 수 있다는 부분을 별도 문장 [추정]으로 썼다.
- f18 문구 수정 지시 — 6절·8절에서 'aws-samples 저장소의 시연용 샘플'로 쓰고 자동 롤백은 README 가 이점으로 나열할 뿐 구현 절차는 보이지 않는다고 밝혔으며 [추정]과 '벤더 주장'을 유지했다.
- f19 강등 지시 — 6절·8절에서 [추정]으로 쓰고 주관 조직명을 'KIST 휴머노이드연구단'으로 고쳤으며 원 매체 미확인을 병기했다.
- f27 의견 주체 표시 지시 — 10절 첫 문장에 '구축자 의견'임을 밝히고 각 연결 항목을 [의견]으로 두었다.
- f23 추론 표시 지시 — 9절 표 아래에 '운영 시간대·일부 로봇 단위 분할 배포'가 확인한 출처에 직접 근거가 없는 구축자 추론이라고 밝히고 [추정]을 유지했다.
- f15 프리프린트 표시 지시 — 6절과 8절에 arXiv 프리프린트(동료 심사 전)이며 저자 미확인임을 적었다.
- f9 기준일 지시 — 3절에 Kilted 지원 종료(2026-11)가 기준일 2026-09-25 에서 약 2개월 뒤라는 문장을 더했다.
- 원문 미열람 표시 지시 — ref-754·ref-755·ref-756·ref-757·ref-758·ref-759·ref-761·ref-762·ref-763·ref-668 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.
- 신뢰도·태그 지시 — 프런트매터 confidence 를 medium 으로 두고 각 finding 의 태그를 1차 판정 처분(f13·f17 부분 강등, f19 강등, 나머지 유지)대로 썼다.
- 분량 초과 자동 분리: 24. 자산·소프트웨어 수명주기 관리 본문 8,444자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,733자
