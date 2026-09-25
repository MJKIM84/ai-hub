# 리서치 브리프 2026-09-25-56

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-56 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 22. 시뮬레이션·예측용 디지털 트윈 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(디지털 모델·섀도·트윈 구분, 8. 실시간 세계 상태·데이터 일관성과의 경계)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음(트랙 floorplan-recognition 반영 제안 1건: Sommer 외 2023, ref-241)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 0건)

## 조사 질문

1. 성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]
2. 디지털 트윈·시뮬레이션의 정의와 표준(ISO 23247, KS X ISO 23247)은 무엇이며, 디지털 모델·디지털 섀도·디지털 트윈 구분으로 8. 실시간 세계 상태·데이터 일관성과 어떻게 경계를 긋는가? (섹션 3·4·7 겨냥)
3. 물류센터 로봇 운영 정책·배치·수요 변화의 효과를 예측하는 대표 접근법(이산 사건 시뮬레이션, 물리 기반 로봇 시뮬레이터, 데이터 기반 모델 생성)은 무엇인가? (섹션 6 겨냥)
4. 오픈소스 도구(Open-RMF 시뮬레이션, RAWSim-O, OFacT)는 무엇을 재현하고 어떤 결정을 실험하게 하는가? (섹션 7 겨냥)
5. 시뮬레이션 모델의 검증·타당성 확인 방법과 실데이터 검증 부족 문제는 연구에서 어떻게 다뤄지는가? (섹션 8·11 겨냥)
6. ROP 가 직접 맡을 시뮬레이션 범위와 외부에 맡길 범위(센서·물리 시뮬레이션, 로봇 로컬 주행, 수요예측)는 어떻게 나뉘는가? (섹션 9·10 겨냥)
7. 국내 물류센터 디지털 트윈 사례와 트랙 floorplan-recognition 반영 제안(스캔·객체 인식 기반 계획용 트윈, Sommer 외 2023)은 무엇을 보여 주는가? (섹션 5·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO 23247(제조를 위한 디지털 트윈 프레임워크)은 국내에 KS X ISO 23247 로 부합화되어 있으며 제1부 개요 및 일반 원리, 제2부 참조 구조, 제4부 정보 교환 등 부로 나뉜다. | ref-659 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | ISO 는 2026년에 ISO 23247-5(디지털 트윈을 위한 디지털 스레드)와 ISO 23247-6(디지털 트윈 결합)을 발간했고, 국가기술표준원은 2026-07-28 이 두 표준이 한국(ETRI) 제안으로 발간되었다고 알렸다. | ref-661, ref-662 | 예 | medium | 2026-07-28 | — | 원문 미열람 |
| f3 | [사실] | ISO 23247-6 은 목적에 따라 여러 디지털 트윈을 골라 결합하는 방법을 정해, 제품·설비·공정의 개별 트윈을 묶어 생산 라인·공장 전체의 복합 트윈을 구성하게 한다. | ref-661, ref-662 | 아니오 | medium | 2026-07-28 | — | 원문 미열람 |
| f4 | [사실] | NIST 의 제조용 디지털 트윈 과제는 디지털 트윈을 신뢰할 수 있고 상호운용 가능하게 만드는 측정 과학과 표준 개발을 목표로 둔다. | ref-660 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f5 | [사실] | Kritzinger 외(2018)는 제조 분야 문헌을 디지털 모델·디지털 섀도·디지털 트윈으로 구분해 분류했고, 가장 높은 단계인 디지털 트윈을 다룬 문헌은 드물고 모델·섀도 문헌이 더 많다고 보고했다. | ref-291 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f6 | [의견] | 분류 원문의 구분(8. 실시간 세계 상태·데이터 일관성은 현재 상태 표현, 22. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험)에 문헌의 모델·섀도·트윈 구분을 맞추면, '디지털 트윈'이라는 이름이 실시간 동기화 수준을 가리키는 경우와 시나리오 실험 기능을 가리키는 경우가 섞여 쓰이므로 이 위키는 용도(현재 표현/미래 실험)로 나눠 적는 것이 맞아 보인다. | ref-291, ref-664 | 아니오 | low | 2020 | — | 원문 미열람 |
| f7 | [사실] | Agalianos 외(2020)는 물류 4.0 에서 이산 사건 시뮬레이션(DES)이 사물인터넷 장치의 실시간 데이터를 질의하며 디지털 트윈의 한 부분으로 진화하고, 이를 통해 창고 계획·관리·의사결정을 지원한다고 정리했다. | ref-664 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f8 | [사실] | Le·Fan(2024)의 물류·공급망 디지털 트윈 문헌 검토는 실제 데이터로 검증한 논문은 소수이고 대다수가 생성 데이터를 쓴다고 보고해, 실무 적용의 부족을 지적했다. | ref-665 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | Le·Fan(2024)은 COVID-19 이후 공급망 위험·교란 관리에서 디지털 트윈의 이점이 뚜렷해졌다고 보고, 물류·공급망 디지털 트윈 개념 틀을 제안했다. | ref-665 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f10 | [사실] | Coelho 외(2021)는 Simio 로 만든 사내 물류 시뮬레이션 의사결정 지원 도구를 제안하고, 이 모델이 현실을 대표하여 실제 운영을 방해하지 않고 개선안을 시험하는 디지털 트윈화 도구로 쓰일 수 있다고 보고했다. | ref-666 | 아니오 | medium | 2021 | — | 원문 미열람 |
| f11 | [사실] | Open-RMF 문서는 Gazebo·Ignition 물리 시뮬레이터를 ROS 2 와 연결해 시뮬레이션에 쓴 코드를 수정 없이 실제 시스템에서도 실행하고, 시나리오 반복·예외 상황 탐색·장시간 검증을 현장 배치 전에 할 수 있다고 설명한다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [사실] | Open-RMF 의 building_map_generator 는 traffic_editor 로 주석한 .building.yaml 에서 Gazebo·Ignition 월드(바닥·벽 메시)와 플릿 어댑터용 주행 그래프를 함께 생성하므로, 레이아웃이 바뀌면 주석을 고쳐 시뮬레이션 월드를 다시 만들 수 있다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [사실] | Open-RMF 시뮬레이션은 로봇용 slotcar 플러그인(레일식 주행과 가감속), 문·승강기 플러그인, 작업셀 적재·하역을 흉내 내는 TeleportDispenser·TeleportIngestor, Menge 기반 보행자 군중 시뮬레이션(CrowdSim), 배터리·충전기 동작 전환 도구를 제공한다. | ref-406, ref-668 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f14 | [추정] | 연계 대상: Open-RMF 시뮬레이션의 로봇 모델은 레일식 주행을 흉내 내는 단순화 모델이므로, 센서 인식·로컬 회피 같은 로봇 자체 거동의 충실도는 제조사·물리 시뮬레이터 쪽에 맡기고 ROP 시뮬레이션은 플릿 조율·설비 상호작용을 실험하는 데 초점이 맞는 것으로 보인다. | ref-406, ref-668 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [사실] | rmf_simulation 저장소는 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 지원 대상으로 적어, 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리가 필요하다. | ref-668 | 아니오 | medium | 2026-09-25 | — | — |
| f16 | [사실] | RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS)의 이산 사건 시뮬레이션 프레임워크로, 운영 중 생기는 여러 결정 문제의 효과를 연구하고 새 결정 방법을 끼워 넣을 수 있게 하며 2D·3D 화면과 로봇 위치 히트맵을 제공한다(C#, GPL v3). | ref-101 | 아니오 | medium | 2026-09-25 | 피킹 | — |
| f17 | [사실] | Merschformann 외(2019)의 RMFS 결정 규칙 연구는 이산 사건 시뮬레이션으로 배정 규칙을 가정한 미래에서 실험했고, 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-398 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f18 | [사실] | 국내 연구로 시뮬레이션과 메타모델을 결합해 자동물류센터 설계를 최적화한 연구가 있다. | ref-402 | 아니오 | medium | 2006 | — | 원문 미열람 |
| f19 | [사실] | 다중 AGV 시스템의 경로망을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있어, 경로망 배치안 평가가 시뮬레이션으로 이루어진다. | ref-267 | 아니오 | medium | 2024 | 제약 | 원문 미열람 |
| f20 | [사실] | OFacT(Open Factory Twin)는 Fraunhofer ISST 등이 개발한 생산·물류용 오픈소스 디지털 트윈 프레임워크로, 주문·자원·부품·공정으로 공장 상태를 기술하는 상태 모델, 주문·자원 에이전트 제어, 일관성 검사를 포함한 데이터 통합, 시나리오 평가·예측용 시뮬레이션, KPI 비교 계획 서비스를 갖춘다(Apache 2.0). | ref-670 | 아니오 | medium | 2026-09-25 | — | — |
| f21 | [추정] | OFacT 가 현재 상태를 담는 상태 모델·데이터 통합과 시나리오를 돌리는 시뮬레이션·계획 서비스를 별도 구성요소로 두는 것은, 8. 실시간 세계 상태·데이터 일관성(현재 표현)과 22. 시뮬레이션·예측용 디지털 트윈(미래 실험)을 나누는 분류 원문의 구분과 같은 방향의 설계로 보인다. | ref-670 | 아니오 | low | 2026-09-25 | — | — |
| f22 | [사실] | Sargent 의 시뮬레이션 모델 검증·타당성 확인(V&V) 틀은 개념 모델 타당성, 모델 검증, 운영 타당성, 데이터 타당성을 나누어 확인하고 결과 문서화와 모델 인가(accreditation)를 다룬다. | ref-671 | 아니오 | medium | 2008 | — | 원문 미열람 |
| f23 | [추정] | CJ대한통운은 2021년 11월 현실 물류센터와 같은 가상 물류센터를 구축해 작업 동선·재고 배치·설비 효율을 최적화하고 장비 고장·피킹 오류·상품 파손 원인을 사전에 파악하며, AI 가 시나리오를 학습해 몇 시간 걸릴 일을 수초~수분에 해결한다고 발표했다. | ref-672 | 아니오 | low | 2021-11 | 피킹 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f24 | [추정] | NVIDIA 는 'Mega' Omniverse 블루프린트를 공장·창고 디지털 트윈에서 로봇 플릿과 물리 AI 를 배치 전에 개발·시험·최적화하는 참조 작업 흐름(센서 시뮬레이션·합성 데이터 생성 결합)으로 소개하고, KION·Accenture 가 창고·유통 공정 최적화에 쓴다고 밝혔다. | ref-673 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f25 | [추정] | 분류 원문 질문 '성수기 주문량이 늘면 어디가 먼저 막힐까?'에 대해, 확인한 DES 연구·도구는 주문 도착량과 배정 규칙·자원 수(로봇·작업대)를 바꿔 처리량과 대기를 비교하는 방식으로 답하며, ROP 오케스트레이션 정책 자체를 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사에서 찾지 못했다. | ref-398, ref-101, ref-666, ref-664 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f26 | [사실] | Sommer 외(2023)는 레이저 스캔과 객체 인식으로 공장의 건조 환경(built environment) 디지털 트윈을 자동 생성해 생산 계획의 입력으로 쓰는 방법을 제안했다. | ref-241 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f27 | [추정] | Sommer 외(2023)의 트윈은 생산 계획을 위한 배치·공간 모델이므로 22. 시뮬레이션·예측용 디지털 트윈의 초기 모델 생성(계획용)에 해당하고, 운영 중 현재 상태를 동기화하는 8. 실시간 세계 상태·데이터 일관성과는 구분되는 것으로 보인다. | ref-241, ref-406 | 아니오 | low | 2023 | — | — |
| f28 | [추정] | ROP 가 직접 맡을 시뮬레이션 몫은 자신의 작업 배정·교통·충전 정책과 설비 요청(문·승강기)을 시뮬레이션된 플릿·설비에 대해 그대로 실행해 보는 것으로 보이며, Open-RMF 처럼 같은 코드를 시뮬레이션과 실제에 쓰는 구조가 그 근거가 된다. | ref-406, ref-668 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f29 | [추정] | 연계 대상: 센서 시뮬레이션·합성 데이터 생성·물리 기반 로봇 거동 재현은 시뮬레이터 제공자와 로봇 제조사 영역이고, 시나리오의 주문·물동량 전망은 상위 업무 시스템의 수요예측에서 받는 입력으로 보인다. | ref-673, ref-665 | 아니오 | low | 2026-09-25 | 시작 조건 | 원문 미열람 |
| f30 | [의견] | Open-RMF 시뮬레이션이 강조하는 시나리오 반복·예외 상황 탐색은 23. 시험·형식 검증·벤치마크의 회귀·장애 시험과 환경을 공유하므로, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인이라는 목적으로 나누는 것이 분류 원문 정의에 맞아 보인다. | ref-406 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: KSSN 표준 상세 목록: KS X ISO 23247-1 '개요 및 일반 원리', -2 '참조 구조', -4 '정보 교환' (제3부 목록은 이번 검색에서 확인하지 못함) (발행일 미확인, 확인일 기준)
- **f2**: ISO 카탈로그에 ISO 23247-6:2026 'Digital twin composition' 등재. 기사: 국표원이 디지털 쓰레드(23247-5)·디지털 트윈 결합(23247-6) 국제표준 2건 발간을 밝힘(2026-07-28)
- **f3**: 개별 트윈을 블록처럼 결합해 라인·공장 전체를 덮는 복합 디지털 트윈을 구현한다는 설명(기사 요약 중심, ISO 본문 미열람)
- **f4**: 과제 목표: 디지털 트윈을 reliable, interoperable, trustworthy 하게 만드는 측정 과학·표준 개발 (발행일 미확인, 확인일 기준)
- **f5**: Digital Model(DM), Digital Shadow(DS), Digital Twin 구분; DT 문헌은 scarce, DM·DS 문헌이 더 많음. 향후 과제로 충실도 수준·데이터 소유권 등 7개 제시
- **f6**: Kritzinger 외는 데이터 연결 수준으로 DM·DS·DT 를 구분하고, Agalianos 외는 DES 가 실시간 데이터를 질의하며 DT 의 일부로 진화한다고 서술 — 두 축(동기화 수준, 실험 용도)이 다름
- **f7**: Procedia Manufacturing 51, 1636–1641. DES 와 DT 통합 문헌을 검토하고 물류의 추세·과제를 식별
- **f8**: only a few papers employ actual data sets for validation whereas the majority utilize generative data sets (Computers & Industrial Engineering 187)
- **f9**: 팬데믹 이후 risk and disruption management 에서 DT 의 이점이 부각; LSCS 용 개념 프레임워크 제안
- **f10**: 유통 시설과 생산 시설의 사내 물류 활동 분석; 지능형 객체 기반 Simio 모델이 operations improvement without disrupting real sets 에 쓰일 수 있음
- **f11**: "the exact same code used to run the simulations will also be run on the physical system as well without any changes" — 배터리 소모·충돌 비용 없이 반복 시험
- **f12**: 두 모드: .world·model.sdf 생성, 경로 계획용 YAML 주행 그래프 내보내기; 설비 레이아웃 변경 시 주석 수정 후 재생성
- **f13**: slotcar 는 /robot_path_requests 를 구독해 rail-like navigation 구현; rmf_simulation README 에 Toggle charging(배터리·충전기), Crowd simulation(Menge) 항목 (두 출처 모두 Open Robotics 계열)
- **f14**: slotcar 는 'simple robot navigation stack'으로 경로 요청을 받아 레일식으로 이동하고 업데이트를 보냄 — 로컬 주행 알고리즘을 재현하지 않음
- **f15**: README: Gazebo Classic 11 (support ending January 2025), Gazebo Fortress; ros_gz 지원 판에 맞춤(예: ROS Humble–Fortress)
- **f16**: "a discrete event-based simulation for Robotic Mobile Fulfillment Systems"; 결정 문제별 새 방법 구현 확장성, 히트맵·경로 계획 시각화, GNU GPL v3
- **f17**: RMFS 결정 규칙 조합을 시뮬레이션으로 비교, 피킹 주문 배정 규칙의 처리량 영향이 큼 (재인용: 2026-09-25-55)
- **f18**: KISTI ScienceON 수록 '시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화' (재인용: 2026-09-25-55)
- **f19**: Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (재인용: 2026-09-25-55)
- **f20**: "Open source Digital Twin Framework for Production and Logistics"; Simulation 은 evaluate different scenarios or produce forecasts; 창고·공급망도 대상
- **f21**: README 구성요소: State Model / Data Integration(실데이터·일관성 검사) 와 Simulation / Planning Services(시나리오·KPI) 분리
- **f22**: conceptual model validity, model verification, operational validity, data validity 및 권장 검증 절차·인가 논의(WSC 논문, 검색 요약 기준)
- **f23**: 벤더 주장: 보도자료 — 운영 현황 모니터링·재현, 작업동선·재고배치·설비효율 최적화, 이듬해 택배 네트워크(허브·서브터미널)로 확대 계획
- **f24**: 벤더 주장: reference workflow for combining sensor simulation and synthetic data generation ... verify performance of autonomous systems in industrial digital twins (발행일 미확인, 확인일 기준)
- **f25**: RAWSim-O·RMFS 결정 규칙 연구는 결정 규칙별 처리량 비교, Coelho 외는 개선안 시험, Agalianos 외는 창고 계획 지원 — 성수기 병목 위치를 직접 보고한 ROP 사례 없음
- **f26**: Journal of Industrial Information Integration 33, 100462 (2023). 스캔·객체 검출로 공장 레이아웃 모델링과 객체 인식을 자동화해 계획 입력으로 제공
- **f27**: 계획 입력용 자동 생성(ref-241)과, 주석한 평면도에서 시뮬레이션 월드를 만드는 Open-RMF 흐름(ref-406)이 모두 실험용 모델의 초기값 생성 단계
- **f28**: 문·승강기 플러그인이 /door_requests·/lift_requests 에 응답하고 slotcar 가 경로 요청을 받음 — 오케스트레이션 계층의 요청이 시뮬레이션 대상
- **f29**: Mega 블루프린트는 센서 시뮬레이션·합성 데이터를 제공 기능으로 둠; 물류·공급망 DT 틀은 수요·교란 시나리오를 상위 계획 입력으로 다룸(분류 원문 9장 경계 적용)
- **f30**: RMF 문서: scenario repeatability, edge case exploration, long-running validation before facility deployment

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-659 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 예 |
| ref-660 | NIST | Digital Twins for Advanced Manufacturing | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing | 예 |
| ref-661 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/87426.html | 예 |
| ref-662 | 머니투데이 | 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간 | 2026-07-28 | 기사 | medium | 2026-09-25 | https://www.mt.co.kr/economy/2026/07/28/2026072809211448284 | 예 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-664 | Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G. | Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics | 2020 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2351978920320990 | 예 |
| ref-665 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 예 |
| ref-666 | Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P. | Simulation-based decision support tool for in-house logistics: the basis for a digital twin | 2021 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646 | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-668 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_simulation | 아니오 |
| ref-101 | Merschformann, M. (merschformann GitHub) | RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/merschformann/RAWSim-O | 아니오 |
| ref-670 | OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) | ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/OpenFactoryTwin/ofact | 아니오 |
| ref-671 | Sargent, R. G. | Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation) | 2008 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/abs/10.5555/1516744.1516780 | 예 |
| ref-672 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 2021-11 | 벤더 문서 | low | 2026-09-25 | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 | 예 |
| ref-673 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 미확인 | 벤더 문서 | low | 2026-09-25 | https://blogs.nvidia.com/blog/mega-omniverse-blueprint | 예 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | 논문 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |

### 출처 요약

- **ref-659**: 원문 미열람. ISO 23247 을 부합화한 KS X ISO 23247 시리즈의 제1부 표준 상세 페이지. 검색 결과에서 제2부(참조 구조)·제4부(정보 교환) 항목도 확인.
- **ref-660**: 원문 미열람. 제조 디지털 트윈을 신뢰·상호운용 가능하게 하는 측정 과학과 표준 개발을 목표로 하는 NIST 과제 페이지.
- **ref-661**: 원문 미열람. 여러 디지털 트윈을 목적에 따라 결합하는 방법을 다루는 ISO 23247 제6부 카탈로그 페이지.
- **ref-662**: 원문 미열람. 국가기술표준원이 한국 제안 ISO 23247-5(디지털 쓰레드)·23247-6(디지털 트윈 결합) 발간을 알린 내용을 보도.
- **ref-291**: 원문 미열람. IFAC-PapersOnLine 게재. 디지털 모델·디지털 섀도·디지털 트윈을 구분해 제조 분야 문헌을 분류하고 연구 공백 7가지를 제시.
- **ref-664**: 원문 미열람. Procedia Manufacturing 51. 물류에서 DES 와 디지털 트윈 통합 문헌을 검토하고 추세·과제를 정리.
- **ref-665**: 원문 미열람. Computers & Industrial Engineering 187. 물류·공급망 디지털 트윈 문헌 검토와 개념 틀 제안, 실데이터 검증 논문이 소수라고 보고.
- **ref-666**: 원문 미열람. Computers & Industrial Engineering 153. Simio 기반 사내 물류 시뮬레이션 의사결정 지원 도구를 디지털 트윈의 기초로 제안.
- **ref-406**: Open-RMF 시뮬레이션 장: Gazebo·Ignition 연동, building_map_generator 의 월드·주행 그래프 생성, slotcar·문·승강기·작업셀·군중 플러그인.
- **ref-668**: Open-RMF 시뮬레이션 플러그인 저장소: 문·승강기·군중·충전 전환·slotcar·읽기 전용·텔레포트 디스펜서/인제스터, 지원 Gazebo 판.
- **ref-101**: RMFS 이산 사건 시뮬레이션 프레임워크 README: 결정 문제별 방법 확장, 2D·3D 화면·히트맵, C#, GPL v3.
- **ref-670**: 생산·물류용 오픈소스 디지털 트윈 프레임워크 README: 상태 모델, 에이전트 제어, 데이터 통합, 시뮬레이션, 계획 서비스, 환경 인터페이스. Apache 2.0.
- **ref-671**: 원문 미열람. 시뮬레이션 모델의 개념 모델 타당성·모델 검증·운영 타당성·데이터 타당성과 검증 절차·인가를 다룬 WSC 튜토리얼 논문.
- **ref-672**: 원문 미열람. 물류센터 디지털 트윈 구축 계획과 기대 효과를 알린 기업 보도자료(국내 사례).
- **ref-673**: 원문 미열람. 산업 시설 디지털 트윈에서 로봇 플릿을 배치 전에 시험하는 참조 작업 흐름을 소개한 벤더 블로그.
- **ref-241**: 원문 미열람. Journal of Industrial Information Integration 33. 스캔과 객체 인식으로 공장 건조 환경 디지털 트윈을 자동 생성해 생산 계획 입력으로 쓰는 방법.
- **ref-398**: 원문 미열람. RMFS 결정 규칙을 시뮬레이션으로 비교한 연구.
- **ref-402**: 원문 미열람. 시뮬레이션과 메타모델로 자동물류센터 설계를 최적화한 국내 연구.
- **ref-267**: 원문 미열람. 다중 AGV 경로망을 시뮬레이션 기반으로 자동 설계하는 연구.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f7·f9·f10·f11(배치 전 반복 시험·운영 방해 없는 개선안 시험), f8(실데이터 검증 부족) / 4절 핵심 개념: f5(디지털 모델·섀도·트윈), f6 의견·f21 추정(8. 실시간 세계 상태·데이터 일관성과의 구분: 현재 표현 vs 가정한 미래 실험), f3(디지털 트윈 결합) / 5절 현장 시나리오: f25(피킹·제약, 분류 원문 질문 — 추정), f17(피킹·예외·성과), f23(국내 사례, 벤더 주장 병기) / 6절 대표 접근법: f7(DES 와 실시간 데이터), f10(DES 의사결정 지원), f11·f13(물리 시뮬레이터·플러그인), f12·f26·f27(평면도·스캔에서 초기 모델 생성), f24(벤더 주장) / 7절 표준·오픈소스: f1·f2·f3·f4(ISO 23247·KS X ISO 23247·NIST), f11~f13·f15(Open-RMF 시뮬레이션), f16(RAWSim-O), f20(OFacT) / 8절 대표 연구: f5·f7·f8·f9·f10·f17·f18·f19·f22, 트랙 floorplan-recognition 단계 1 반영 제안(2026-09-25-19) 검토 결과 f26(사실)·f27(추정, 계획용 트윈이므로 8. 실시간 세계 상태·데이터 일관성과 구분) / 9절 경계: f28(ROP 직접: 자기 정책을 시뮬레이션된 플릿·설비에 실행), f14·f29('연계 대상': 로봇 자체 거동·센서 시뮬레이션·수요예측) / 10절 연결: 8. 실시간 세계 상태·데이터 일관성(f6·f21), 23. 시험·형식 검증·벤치마크(f30), 24. 자산·소프트웨어 수명주기 관리(f15), 21. 온보딩·설정·현장 시운전과 6. 지도·공간·위치 모델(f12·f26), 13. 작업 배정 — MRTA·15. 다중 로봇 경로·교통 관리 — MAPF(f17·f19), 27. AI·학습·적응과 모델 운영(f23·f24 벤더 주장, 학습 환경으로서 트윈), 28. 표준·상호운용성·다사업자 거버넌스(f1~f3), 20. 예외 복구·재계획·업무 연속성(f9) / 11절 열린 질문: open_questions_new 3건과 f25 의 미확인 사항. 벤더 주장 f23·f24 는 [추정]+'벤더 주장' 병기. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 디지털 스레드 | Digital Thread | 제품 수명주기 전반의 설계·생산·운영 데이터를 연결해 디지털 트윈을 만들고 유지하게 하는 데이터 연결 체계로, ISO 23247-5 가 제조 디지털 트윈용 틀을 정한다. |
| 디지털 트윈 결합 | Digital Twin Composition | 제품·설비·공정의 개별 디지털 트윈을 목적에 맞게 골라 묶어 라인·공장 단위의 복합 트윈을 만드는 방법으로, ISO 23247-6 이 다룬다. |
| 시뮬레이션 모델 검증·타당성 확인 | Verification and Validation (V&V) of Simulation Models | 시뮬레이션 모델이 설계대로 구현되었는지(검증)와 목적에 비추어 현실을 충분히 대표하는지(타당성 확인)를 개념 모델·운영·데이터 측면에서 확인하는 절차다. |

## 열린 질문

새로 생긴 질문:

- 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 4. 성과·경제성·프로세스 개선 | 근거: f8 | 종류: 일반
- 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f3 | 종류: 일반
- 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 9. 로봇·제조사 관제 연동 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 1
- 예산 사용량: 검색 23회 · 신규 출처 15건
- 미확인 항목:
    - f1: KS X ISO 23247 제3부 목록과 각 부의 KS 제정일 미확인
    - f2·f3: ISO 23247-6 본문 미열람, 결합 방법 설명은 기사 요약 중심
    - f4: NIST 과제 페이지 원문 미열람, 발행일 미확인
    - f22: Sargent 논문의 정확한 판(2008 WSC 외 여러 판 존재) 원문 미확인
    - f23·f24: 벤더 주장, 독립 출처로 효과 수치 확인 못 함
    - f25: ROP 정책을 성수기 시나리오로 시험한 공개 물류센터 사례 찾지 못함
    - ref-241: 참고문헌 목록의 기존 값을 입력으로 받지 못해 검색 결과로 기관·제목·URL 을 채움(퍼블리셔 대조 필요)
    - ref-673 발행일 미확인
- 범위 경계 위반 의심:
    - f14·f29: 센서 인식·로컬 주행·센서 시뮬레이션과 수요예측은 분류 원문 9장 외부 연계 영역이므로 '연계 대상:'으로 표시
    - f24: 물리 AI 학습·센서 시뮬레이션은 ROP 직접 범위가 아님(벤더 주장으로만 서술)
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처는 ref-406(Open-RMF 시뮬레이션 장, 미러 목록 경로), ref-668(rmf_simulation), ref-101(RAWSim-O), ref-670(OFacT) 4건이며 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 23회/30, 신규 출처 15건/15(ref-659~ref-673, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 23247-1 정의 원문, 물류 디지털 트윈 대규모 사례(Ashrafian·Pedersen 2023), 데이터 기반 시뮬레이션 모델 자동 생성 검토 논문은 출처로 넣지 않음. 재사용 4건: ref-398·ref-402·ref-267(2026-09-25-55 브리프 값 사용), ref-241(입력에 참고문헌 목록 값이 없어 검색으로 확인한 값으로 기재). 트랙 반영 제안 1건(2026-09-25-19, floorplan-recognition 단계 1, 8절)은 f26(사실)·f27(추정)으로 조사해 반영을 제안. 교차 확인은 f2 1건뿐. 한국 자료: KS X ISO 23247(ref-659), 국표원 발표 기사(ref-662), 국내 연구(ref-402), CJ대한통운 보도자료(ref-672, 벤더 주장). 한국어 검색에서 나온 업체 블로그는 출처로 쓰지 않음. 27. AI·학습·적응과 모델 운영 연결은 f23·f24 벤더 주장뿐이라 교차 규칙 대상(5·21·6·13·19)에 직접 해당하는 근거는 없음. 정정 요청 없음, 대상 영역 열린 질문 0건, 해결 제안 없음.
