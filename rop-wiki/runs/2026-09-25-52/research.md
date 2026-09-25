# 리서치 브리프 2026-09-25-52

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-52 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 21. 온보딩·설정·현장 시운전 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음 (트랙 반영 제안: 도입 설치 시간의 원인)
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 새 제조사 로봇을 적치 운반에 추가하는 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음 (트랙 반영 제안 3건 대상)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음 (트랙 반영 제안 2건 대상)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-022 관련

## 조사 질문

1. 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]
2. 새 로봇을 관제에 등록할 때 로봇 신원·기능·제약을 어떤 표준 메시지나 설정으로 받는가(VDA 5050 팩트시트, MassRobotics 신원 보고, Open-RMF 플릿 어댑터 설정)? (섹션 4·6·7 겨냥)
3. 지도·레이아웃·경로망은 새 현장에서 어떻게 만들고 관제에 넘기며, 이를 자동화·반자동화하는 연구는 무엇인가? (섹션 3·6·8 겨냥, 트랙 반영 제안 검토)
4. 제조사별 로봇 지도와 공통 지도 사이의 좌표 대응과 다층 정렬은 어떻게 설정하는가? (섹션 6 겨냥, 6. 지도·공간·위치 모델 연결)
5. 능력 기술 표준과 문서(매뉴얼) 해석 AI 는 로봇 등록·능력 매칭 작업을 어떻게 줄이려 하는가? (섹션 6·8 겨냥, 교차 규칙: 27. AI·학습·적응과 모델 운영 → 5·21)
6. 현장 시운전 전 안전 준비·가상 시운전·국내 시험·실증 체계는 무엇이 있는가? (섹션 7·9·10 겨냥, 한국 자료 우선)
7. oq-022 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 활용한 사례가 있는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세는 팩트시트(factsheet) 토픽을 관제(fleet control)에서 이동로봇 설정을 돕는 파라미터·제조사 정보 전달 수단으로 두고, 관제가 즉시 동작 factsheetRequest 로 로봇에 팩트시트 전송을 요청할 수 있게 한다. | ref-031, ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 팩트시트 스키마는 유형 사양(typeSpecification), 물리 파라미터, 프로토콜 한계, 지원 프로토콜 기능·동작(protocolFeatures), 로봇 기하, 적재 사양(loadSpecification), 하드웨어·소프트웨어 버전과 충전 파라미터를 담는 로봇 구성(mobileRobotConfiguration)의 일곱 절을 필수로 두며, 스키마 설명은 이 정보가 관제 통합에 필요하고 시스템 계획·규모 산정·시뮬레이션에도 쓸 수 있다고 적는다. | ref-228 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f3 | [사실] | VDA 5050 3.0.0 은 지도 배포를 위해 즉시 동작 downloadMap(지도 id·버전·내려받기 링크)·enableMap·deleteMap 을 두고, 관제가 내려받기를 지시하면 로봇이 지도 서버에서 지도를 받아 특정 버전을 활성화하는 흐름을 설명한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | VDA 5050 3.0.0 은 도입(implementation) 단계에서 경로 정의·스테이션 설정·로봇 속성 저장이 이루어진다고 설명하되 경로 설정 자체는 명세 범위 밖으로 두며, 경로망은 레이아웃 교환 형식(LIF)으로 관제에 가져올 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합사업자가 간선·노드·스테이션으로 이루어진 주행 레이아웃을 제3자 중앙 관제 시스템에 처음 넘겨주기 위한 비구속적 교환 형식이다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f6 | [사실] | MassRobotics AMR 상호운용 표준의 신원 보고(identityReport)는 uuid·시각·제조사명·모델·일련번호·기본 외곽 치수를 필수로, 최고 속도·예상 가동 시간·충전기 형식·지원 업체·제품 문서 URI·화물 종류·최대 화물 부피·최대 화물 무게를 선택으로 둔다. | ref-230 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f7 | [사실] | Open-RMF 플릿 어댑터 설정 파일은 새 플릿마다 속도·가속 한계, 외곽 반경, 배터리·기계 파라미터, 후진 가능 여부, 수행 가능한 작업 유형(순회·배송·청소), 작업 종료 후 동작, 로봇 좌표계와 RMF 좌표계를 대응점 쌍으로 변환하는 reference_coordinates, 제조사 관제 API 연결 정보를 채우게 한다. | ref-153 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | Open-RMF traffic-editor 는 기존 건축 도면·평면도를 배경 이미지로 불러오고, 알려진 두 점 사이 거리 측정으로 축척을 맞춘 뒤 정점·벽·문·승강기·주행 차선·충전기를 사람이 주석하게 하며, 층 사이 정렬은 수직으로 맞춘 기준점(fiducial) 쌍으로 변환을 계산한다. | ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | Open-RMF 는 대규모 RMF 배치 현장을 시각화·편집하는 실험적 도구 RMF Site Editor(rmf_site)를 공개하며, 이 도구의 프로젝트에서 시뮬레이션과 주행 그래프를 생성할 수 있다고 설명한다. | ref-643 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 연동 수준 가운데 전체 제어(Full Control)는 경로를 언제든 새 경로로 바꿀 수 있고, 신호등 제어(Traffic Light)는 일시정지·재개만 허용하며, 읽기 전용(Read Only) 플릿은 제어권 없이 상태만 보고하므로, 새 플릿 온보딩 때 어느 수준으로 연동할지가 선택 사항이 된다. | ref-251 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f11 | [사실] | Beinschob 외(Robotics and Autonomous Systems 87권, 2017)는 다중 AGV 도입의 긴 설치 시간 원인으로 공장의 정밀 2D 지도 작성, 픽업·하역 위치의 3D 좌표 지정, 전문가의 수작업 경로망 설계를 들고, 레이저 스캐너 시스템으로 3D 의미 지도를 얻어 이를 반자동화하는 통합 시스템을 제안한다. | ref-217 | 아니오 | medium | 2017 | — | 원문 미열람 |
| f12 | [추정] | EU CORDIS 의 PAN-Robots 과제 소개는 기존 표지를 활용한 위치 추정과 반자동 공장 탐사로 시스템 설치 기간을 6개월에서 2개월로 줄일 수 있다고 적지만, 이는 과제 측 보고값이며 비교 조건은 확인되지 않았다. | ref-265 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | Heselden·Das(arXiv 2404.13499, 2024)는 지도 작성이 새 환경에 로봇을 배치할 때 시간이 많이 드는 과정이라고 보고, 전역 위치·물체 위치·위상·점유 정보 중심의 표준화된 지도 처리 방식과 빠진 데이터를 틀·절차적으로 생성하는 관리 스크립트를 제안한다. | ref-269 | 아니오 | medium | 2024-04 | — | 원문 미열람 |
| f14 | [사실] | 노주형 외(한국로봇학회 논문지 21권 1호, 2026)는 3D 라이다–관성 센서 기반 SLAM 탐사와 로봇팔로 승강기 버튼을 누르는 기능을 결합해 사물인터넷 장치 개조나 외부 시스템 연동 없이 다층 실내 지도를 처음부터 끝까지 자율로 구축하는 시스템을 제안한다. | ref-163 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f15 | [사실] | IDTA 02020 능력 기술(Capability Description) 서브모델 1.0 은 공정·제품 요구와 자원 능력을 함께 모델링해 요구 능력과 제공 능력을 비교하고 생산 공정의 계획·오케스트레이션을 지원하도록 만든 자산관리셸 서브모델 명세다. | ref-229 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [사실] | Vieira da Silva 외(arXiv 2307.00827, ETFA 2023)는 새 자원과 기능의 통합 공수를 줄이려는 플러그 앤 프로듀스(Plug and Produce)를 위해 능력·스킬을 기술하는 두 접근(온톨로지 기반 형식 기술, 자산관리셸 서브모델 표준화)이 서로 호환되지 않는다고 보고 둘 사이의 대응을 제안한다. | ref-037 | 아니오 | medium | 2023-07 | — | 원문 미열람 |
| f17 | [사실] | Vieira da Silva 외(arXiv 2406.07962, 2024)는 능력의 자연어 설명을 소수 예시 프롬프트에 넣어 LLM(Large Language Model, 대규모 언어 모델)으로 능력 온톨로지를 생성하고, 구문 검사·모순 검사·환각과 누락 요소 검사를 LLM 과 반복하는 방식으로 결과를 자동 검증하는 방법을 제안한다. | ref-637 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f18 | [사실] | 연계 대상: ISO 3691-4:2023 은 무인 산업용 트럭과 그 시스템의 안전 요구사항과 검증 수단을 정하고, 트럭이 안전하게 운행하도록 운행 구역을 준비하는 요구를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f19 | [사실] | 한국산업기술시험원(KTL)과 한국통합물류협회(KILA)는 2026-07-23 물류로봇·자동화 설비의 시험·인증과 표준화 협력 업무협약을 맺고, AMR·AGV·팔레타이징 로봇·모바일 매니퓰레이터·자율주행 지게차의 성능·안전성 검증을 KTL 테스트베드와 회원사 물류센터를 잇는 연구개발–시험평가–현장 실증 체계로 지원하겠다고 밝혔다. | ref-639 | 아니오 | low | 2026-07-24 | — | 원문 미열람 |
| f20 | [추정] | Siemens 는 고객사례에서 IDC 가 가상 시운전(virtual commissioning)으로 코드를 시스템 설계와 대조 검증해 현장에서 큰 변경이 필요 없었고 가동 개시를 3주 앞당겼다고 설명한다. | ref-640 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람, 벤더 주장 |
| f21 | [추정] | f1~f8·f11·f13 을 종합하면 새 제조사 로봇이나 새 현장을 추가할 때 반복되는 작업은 로봇 신원·기능·제약 등록(팩트시트·신원 보고·어댑터 설정), 지도·레이아웃·경로망 작성과 가져오기, 제조사 지도와 공통 지도의 좌표 대응, 연동 수준 선택으로 나눌 수 있고, 앞의 등록 항목은 표준 메시지로 받을 수 있으나 경로망 설계와 좌표 대응은 여전히 사람의 설정 작업으로 남는 것으로 보인다. | ref-031, ref-228, ref-230, ref-153, ref-079, ref-217, ref-269 | 아니오 | low | 2026-09-25 | 적치 / 수행 자원 | — |
| f22 | [추정] | 이번에 확인한 범위의 팩트시트 스키마 최상위 절과 신원 보고 필드에는 제조사 지도와 공통(관제) 지도 사이의 좌표 대응을 담는 항목이 보이지 않고, Open-RMF 는 이를 현장별 어댑터 설정(reference_coordinates)으로 두므로, 좌표 정합은 현장 시운전의 설정·검증 항목으로 남는 것으로 보인다. | ref-228, ref-230, ref-153 | 아니오 | low | 2026-09-25 | 적치 / 제약 | — |
| f23 | [추정] | 연계 대상: 로봇 자체의 SLAM 지도 작성·위치 추정·센서 교정은 제조사 몫이고, 관제 인터페이스가 제공하는 것(팩트시트 요청, 지도 배포 지시, 레이아웃 가져오기, 어댑터 설정)을 보면 이종 로봇을 연결하는 ROP 는 로봇 등록 정보의 수집·검증, 레이아웃·좌표 대응 설정, 연동 수준 결정과 그 설정의 버전 관리를 맡는 경계가 될 것으로 보인다. | ref-031, ref-153, ref-251 | 아니오 | low | 2026-09-25 | 수행 자원 | — |

### 근거 발췌

- **f1**: 6.10절: 팩트시트는 "Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control"를 전달한다. 표 4에 factsheetRequest 즉시 동작. (두 출처는 같은 저장소라 독립 아님)
- **f2**: factsheet.schema 최상위 필수 절 7개. 설명문: 로봇 유형 계열을 VDA 5050 준수 관제에 통합하는 데 필요하며 계획·규모 산정·시뮬레이션에 적용 가능. (발행일 미확인, 확인일 기준)
- **f3**: 표 4: downloadMap 은 새 지도 내려받기를 트리거(mapId, version, 링크), enableMap·deleteMap. 그림 13: 관제 트리거 → 로봇이 지도 서버에서 받음 → 버전 활성화.
- **f4**: 5.2절: 경로 수동 정의, 스테이션 설정, 로봇 속성 저장을 도입 단계 활동으로 서술하고 경로 설정은 이 문서의 대상이 아니라고 적음. LIF(VDMA 2024-03)로 경로를 관제에 가져올 수 있다고 언급.
- **f5**: README: 통합사업자가 "initially transfer a track layout to a central (third-party) master control system" 할 수 있게 함. 레이아웃은 edges·nodes·stations 모음. 1.0.0, 2023-09, 비구속적 접근.
- **f6**: AMR_Interop_Standard.json identityReport required: uuid, timestamp, manufacturerName, robotModel, robotSerialNumber, baseRobotEnvelope. optional: maxSpeed, maxRunTime, chargerType, productDocumentation, cargoType, cargoMaxVolume, cargoMaxWeight 등.
- **f7**: config.yaml 의 rmf_fleet(limits, profile, battery_system, mechanical_system, reversible, task_capabilities, finishing_request), 선택 reference_coordinates, fleet_manager(prefix, 인증). 필드와 어댑터 코드가 맞지 않으면 가져오기 오류.
- **f8**: 목적: 여러 플릿의 의도를 "standardized, vendor neutral manner through a graphical interface"로 표현. 측정선으로 축척(기본 1픽셀=5cm), 충전기는 정점 속성, 기준점 쌍으로 층간 이동·회전·축척 계산.
- **f9**: README: "an experimental approach to visualizing and editing large RMF deployment sites". Rust·Bevy 기반, 데스크톱·웹, 프로젝트에서 시뮬레이션·주행 그래프 생성, 웹판은 JSON 내보내기. (발행일 미확인, 확인일 기준)
- **f10**: integration_fleets: Full Control·Traffic Light·Read Only 세 연동 수준과 각 수준의 제어 범위. (재인용: 2026-09-25-50)
- **f11**: 초록 요약: 긴 도입 시간은 정밀 2D 지도, 픽업·하역 위치의 3D 지리 참조, 경로망 수작업 설계에서 비롯. 혁신적 레이저 스캐너로 3D 의미 지도 획득. (PAN-Robots 과제)
- **f12**: 검색 요약: 설치를 6개월 대신 2개월에 할 수 있어 공장 중단 시간을 줄인다; 반자동 공장 탐사와 기존 랜드마크 활용 위치 추정 덕분. 비교 기준·현장 수 미확인. (발행일 미확인, 확인일 기준)
- **f13**: 초록 요약: 지도 작성은 새 환경 배치의 시간 소모 과정. 전역 위치·물체 위치·위상·점유 중심 표준 처리, 빠진 데이터의 템플릿·절차적 생성으로 효율적 배치와 플랫폼 간 상호운용 향상. ICRA 2024 워크숍.
- **f14**: 검색 요약: 3D LiDAR–IMU SLAM 기반 프런티어 생성, 다중 센서 융합 비용 지도, RGB-D 카메라와 4자유도 매니퓰레이터로 승강기 버튼 조작, 완전 자율 다층 지도 구축. 48–57쪽.
- **f15**: README: "enables reliable comparison between required and provided capabilities and supports efficient planning and orchestration of production processes." 버전 1.0(IDTA 첫 공식 발행). 시운전 공수는 언급 없음.
- **f16**: 검색 요약: 플러그 앤 프로듀스의 핵심은 새 자원과 기능 통합 공수 감소; 능력·스킬 모델링에 온톨로지와 AAS 서브모델이라는 호환되지 않는 두 접근이 있음.
- **f17**: 검색 요약: 자연어 능력 설명 → few-shot 프롬프트 → 능력 온톨로지 생성 → 구문 검사, 모순 검사, 환각·누락 요소 검사의 검증 루프. 2024-10 개정.
- **f18**: 검색 요약(ISO 소개): 무인 산업용 트럭과 시스템의 안전 요구와 검증; 운행 구역 상태가 안전 운행에 큰 영향을 주며 구역 준비는 부속서 A 에 규정.
- **f19**: 기사 요약: 2026-07-23 MOU, KILA 168개 회원사, 대상 로봇 5종, KTL 테스트베드와 실제 물류창고 연계. 협약 단계이며 실적은 미확인.
- **f20**: 벤더 주장: 가상 시운전으로 launch time 3주 단축, 현장에서 큰 변경 불필요. 비교 기준·현장 조건 미확인. (발행일 미확인, 확인일 기준)
- **f21**: 팩트시트·identityReport 는 등록 정보를 표준화(f1·f2·f6), 경로 설정은 VDA 5050 범위 밖(f4), traffic-editor 는 사람 주석(f8), 경로망 수작업은 도입 병목(f11·f13). 이 위키의 종합 추론.
- **f22**: factsheet.schema 7개 절, identityReport 필드 목록에 좌표 대응 항목 없음(부재 확인 아닌 관찰), Open-RMF 는 대응점 쌍 설정으로 변환.
- **f23**: VDA 5050 은 지도 배포 동작과 팩트시트만 정하고 경로 설정은 범위 밖(f3·f4), Open-RMF 는 어댑터 설정·연동 수준을 통합 측에 둠(f7·f10). 분류 원문 9장 '로봇 자체 지능·제어' 경계 적용.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-251 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-079 | Open Robotics | Programming Multiple Robots with ROS 2 — traffic-editor | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-153 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-229 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020 Submodel Capability Description 1.0 — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA | 2023-09 | 표준 | medium | 2026-09-25 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-217 | Beinschob, P. 외 | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 예 |
| ref-269 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 2024-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2404.13499 | 예 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.00827 | 예 |
| ref-637 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.07962 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-639 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | 기사 | low | 2026-09-25 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 예 |
| ref-640 | Siemens Digital Industries Software | Virtual commissioning with Siemens solutions reduces launch time by three weeks | 미확인 | 벤더 문서 | low | 2026-09-25 | https://resources.sw.siemens.com/en-US/case-study-idc/ | 예 |
| ref-265 | European Commission CORDIS | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 예 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철 (한국로봇학회) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | 논문 | medium | 2026-09-25 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 예 |
| ref-643 | Open Robotics (open-rmf/rmf_site) | rmf_site — README (RMF Site Editor) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_site | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 최신판(3.0.0) 명세 원문. 팩트시트, 지도 배포 동작, 도입 단계, LIF 언급을 확인.
- **ref-230**: MassRobotics AMR 상호운용 표준의 JSON 스키마. 신원 보고(identityReport)와 상태 보고 필드 정의.
- **ref-251**: 원문 미열람. Open-RMF 플릿 어댑터 연동 수준(Full Control·Traffic Light·Read Only) 설명. 이번 실행에서는 다시 열지 않고 이전 실행(2026-09-25-50) 확인 내용을 재인용.
- **ref-228**: VDA 5050 팩트시트 JSON 스키마. 로봇 유형 사양·물리 파라미터·프로토콜 한계·기능·기하·적재·구성 절을 정의하고 관제 통합 용도를 설명.
- **ref-079**: Open-RMF traffic-editor 사용법. 평면도 배경, 측정으로 축척 설정, 벽·문·승강기·차선·충전기 주석, 기준점으로 층 정렬.
- **ref-153**: Open-RMF 플릿 어댑터 튜토리얼. 설정 파일의 로봇 사양·작업 능력·좌표 변환 대응점·제조사 관제 연결 항목 설명.
- **ref-229**: 자산관리셸 능력 기술 서브모델 1.0 소개. 요구 능력과 제공 능력의 비교, 생산 계획·오케스트레이션 지원.
- **ref-046**: VDMA LIF 1.0.0 공식 저장소 README. 통합사업자가 간선·노드·스테이션 레이아웃을 제3자 관제에 넘기는 교환 형식.
- **ref-217**: 원문 미열람. Robotics and Autonomous Systems 87권. 다중 AGV 도입 병목(정밀 지도, 픽업·하역 위치, 경로망 설계)을 3D 의미 지도로 반자동화.
- **ref-269**: 원문 미열람. 새 환경 배치의 지도 작성 부담을 줄이는 표준화된 지도 처리 방식과 관리 스크립트 제안(ICRA 2024 워크숍).
- **ref-037**: 원문 미열람. 플러그 앤 프로듀스를 위한 능력·스킬 모델의 온톨로지 방식과 자산관리셸 방식 사이 대응 제안.
- **ref-637**: 원문 미열람. LLM 으로 자연어 능력 설명에서 능력 온톨로지를 생성하고 구문·모순·환각 검사로 검증하는 방법.
- **ref-470**: 원문 미열람. 무인 산업용 트럭과 시스템의 안전 요구·검증, 운행 구역 준비(부속서 A).
- **ref-639**: 원문 미열람. KTL 과 한국통합물류협회의 물류로봇 시험·인증·표준화 업무협약(2026-07-23) 보도.
- **ref-640**: 원문 미열람. IDC 고객사례: 가상 시운전으로 가동 개시 3주 단축(벤더 주장).
- **ref-265**: 원문 미열람. EU FP7 PAN-Robots 과제 결과 소개. 반자동 공장 탐사로 설치 기간 6개월→2개월(과제 측 보고).
- **ref-163**: 원문 미열람. 한국로봇학회 논문지 21권 1호. 자율 탐사와 로봇팔 승강기 조작으로 다층 실내 지도를 자율 구축.
- **ref-643**: 대규모 RMF 배치 현장을 시각화·편집하는 실험적 도구 RMF Site Editor 소개.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절 왜 중요한가: f11·f13(설치 시간 원인, 트랙 반영 제안 2026-09-25-22 재확인), f12(PAN-Robots 6→2개월, 추정), f21(SCM 질문 연결) / 4절 용어: 팩트시트(f1·f2, 기존 용어), 신원 보고(f6), LIF(f5, 기존 용어), 기준점(f8), 가상 시운전(f20), 플러그 앤 프로듀스(f16) / 5절 시나리오: 적치 단계에 새 제조사 AMR 추가 — 수행 자원 f6·f7·f21, 제약 f22·f18, 예외·성과 f12·f20 / 6절 접근법: 표준 등록 메시지 f1·f2·f6, 어댑터 설정 f7, 평면도 주석·측정 축척 f8·f9(트랙 반영 제안 2026-09-25-11 재확인), 연동 수준 선택 f10, 반자동·자율 지도 작성 f11·f13·f14(트랙 반영 제안 2026-09-25-19 재확인), 능력 기술·매칭 f15·f16, 문서 해석 AI f17 / 7절 표준·오픈소스: VDA 5050(f1~f4), LIF(f5), MassRobotics(f6), Open-RMF(f7~f10), IDTA 02020(f15), ISO 3691-4(f18, 연계 대상), 국내 KTL–KILA 체계(f19) / 8절 연구: f11·f13·f14·f16·f17 / 9절 범위: f23(로봇 자체 SLAM·교정은 연계 대상), f18 / 10절 연결: 5. 로봇 능력·작업 온톨로지(f15~f17), 6. 지도·공간·위치 모델(f8·f13·f22), 9. 로봇·제조사 관제 연동(f1·f6·f7·f10), 10. 설비·건물 시스템 연동(f14 승강기), 22. 시뮬레이션·예측용 디지털 트윈(f2·f20), 23. 시험·형식 검증·벤치마크(f19), 24. 자산·소프트웨어 수명주기 관리(f3 지도 버전), 25. 안전·위험 관리(f18), 27. AI·학습·적응과 모델 운영(f17, 교차 규칙) / 11절 열린 질문: oq-022(미해결)와 새 질문 2건. 트랙 반영 제안 가운데 MiR·OTTO 벤더 주장(ref-271 등), Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 이번에 다시 확인하지 않아 다음 실행 후보로 남긴다 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 가상 시운전 | Virtual Commissioning | 제어 로직·로봇 프로그램·관제 설정을 현장 설치 전에 가상 모델과 연결해 시험함으로써 현장 시운전의 시간과 위험을 줄이려는 방법이다. |
| 플러그 앤 프로듀스 | Plug and Produce | 새 설비나 자원을 연결하면 기술된 능력 정보를 바탕으로 최소한의 설정만으로 생산·작업에 투입되게 하려는 통합 방식이다. |
| 신원 보고 | Identity Report (MassRobotics identityReport) | MassRobotics AMR 상호운용 표준에서 로봇이 제조사·모델·일련번호·외곽 치수와 선택적으로 속도·화물 한계·문서 위치를 알리는 메시지다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 9. 로봇·제조사 관제 연동 | 근거: f21 | 종류: 일반
- 제조사 로봇 지도와 공통 관제 지도 사이 좌표 대응(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 23. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 항목마다 단일 출처(f1 의 두 출처는 같은 저장소라 독립 아님)
    - f11·f13·f14·f16·f17·f18: 원문 미열람, 검색 요약 범위
    - f12 PAN-Robots 6→2개월: 과제 측 보고값, 비교 조건 미확인
    - f19 KTL–KILA 협약: 기사만 확인, 기관 보도자료 원문 미확인
    - f20 Siemens 가상 시운전 3주 단축: 벤더 주장, 독립 확인 없음
    - f22: 팩트시트 최상위 절과 신원 보고 필드 범위의 부재 관찰이며 하위 필드 전체 확인 아님
    - ISO 3691-4 의 시운전 절차·통합사업자 책임 구분은 제3자 해설에서만 보여 finding 으로 내지 않음
    - oq-022: 국내 물류센터의 CAD·BIM 도면 활용 사례를 한국어 검색 2회에서 찾지 못함
- 범위 경계 위반 의심:
    - f18: ISO 3691-4 는 설비·차량 안전 영역(25. 안전·위험 관리, 분류 원문 9장 연계)이라 '연계 대상: '으로 표시하고 운행 구역 준비 요구만 시운전 제약으로 연결
    - f23: 로봇 자체 SLAM·위치 추정·센서 교정은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역으로 구분
    - f14: 로봇팔 승강기 조작 자율 지도 작성은 로봇 자체 기능 연구이므로 8절 연구 사례로만 두고 ROP 직접 범위로 서술하지 않도록 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-031·ref-230(재사용), ref-228·ref-079·ref-153·ref-229·ref-046·ref-643(신규). 그 밖의 신규 출처(ref-217~ref-163)와 재사용 ref-251 는 원문 미열람(신뢰도 상한 medium, 모든 finding medium 이하). 검색 18회/30, 신규 출처 15건/15(ref-228~ref-643, 예약 구간 안) — 신규 출처 상한 도달로 MiR·OTTO 벤더 문서, Boniardi 외 2019, 다중 AGV 경로망 자동 설계(IEEE T-ASE 2024), Rüdt 외 2025, 문서 해석 LLM(기술 매뉴얼 지식 추출) 논문은 추가하지 않았다. 입력의 참고문헌 목록이 요약본(0건 표시)이라 트랙 반영 제안이 인용한 ref-217·ref-265·ref-269 등의 서지 정보를 몰라 재사용하지 못하고, 같은 문헌(Beinschob 외 2017, PAN-Robots CORDIS, Heselden·Das 2024)을 새 id(ref-217·ref-265·ref-269)로 다시 적었다 — 같은 URL 이면 퍼블리셔가 기존 id 로 합쳐야 한다. ref-251 는 이전 브리프(2026-09-25-50) 값을 재인용. 트랙 반영 제안 6건 가운데 traffic-editor(f8), 플릿 어댑터 설정(f7), Beinschob 외(f11), Heselden·Das(f13), PAN-Robots(f12)는 이번 finding 으로 재확인했고, 나머지는 페이지 제안 rationale 에 다음 실행 후보로 적었다. 한국 자료: KTL–KILA 협약(f19, 기사), 한국로봇학회 논문(f14). 한국어 검색에서 나온 블로그·업체 홍보 글은 쓰지 않았다. 교차 규칙: 문서 해석 AI(f17)는 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 연구 방법으로 27. AI·학습·적응과 모델 운영 연결을 제안. 8. 실시간 세계 상태·데이터 일관성 관련 주장 없음, 22. 시뮬레이션·예측용 디지털 트윈은 가상 시운전(f20)·팩트시트의 시뮬레이션 용도(f2) 연결로만 제안. 정정 요청 없음. oq-022 는 해결하지 못함.
