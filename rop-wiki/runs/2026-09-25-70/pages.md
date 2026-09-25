# 스토리텔러 산출 2026-09-25-70

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | draft | q3-04 답함(3절 q3-04 소절 신설), 2절 질문 목록 갱신과 q3-11 추가, 4·5·7절 추가, 6절 시뮬레이션 초기값 행 충족·전환 미승인, 8절 출처 추가, 9절 이력 행 추가 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0.8 → v0.9: 층 '높이 기준'에 층 고도 값 후보 병기, 문 '여닫는 방식' 값 후보(Open-RMF 문 유형)와 '동작 범위' 속성 추가, 엘리베이터 '칸 치수' 속성 추가, 6절 질문 3건 추가, H1 버전 표기(v0.7) 오류를 v0.9로 수정 |
| update | docs/ideas/floorplan-recognition.md | draft | 5절 '핵심 구성 요소'에 '시뮬레이션 초기값' 소절 신설(설계·도입 검토용과 운영 중 예측용 초기화 구분), '아직 조사되지 않은 구성 요소'에서 q3-04 제거, 새 각주 3건 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 스키마 초안 현재 버전 v0.9와 실행 2026-09-25-70 변경, 아이디어 페이지 5절 시뮬레이션 초기값, 백로그 후속 질문 21건·q3-04 답함 반영 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 3 | q3-04 답함(시뮬레이션 초기값에 더 필요한 정보 여섯 묶음, 종합은 추정), 공간 그래프 스키마 초안 v0.8 → v0.9, 후속 질문 2건 | run 2026-09-25-70
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 3: q3-04 답함(도면 기반 층별 지도를 시뮬레이션 초기값으로 쓰기 위해 더 필요한 정보 여섯 묶음, 추정), 공간 그래프 스키마 초안 v0.9
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 건축 도면 자동 인식 트랙 단계 3 q3-04 답함(시뮬레이션 초기값, 설계용·운영 예측용 초기화 구분), 세부영역 반영 제안 제출
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 q3-04 답(도면이 채우는 몫과 도면 밖 원천, 추정)을 6·8절 반영 제안으로 제출

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 핵심 제조 시뮬레이션 데이터 | Core Manufacturing Simulation Data (CMSD) | 제조 분야 시뮬레이션과 정보 시스템 사이 데이터 교환을 위한 SISO 표준 중립 정보 모델이다. | 22, 28 | ref-647 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/simulation.html |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-441 | Open Robotics (open-rmf) | rmf_traffic_editor — README | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_traffic_editor |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-081 | Vega-Torres, M. A. 외 | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 논문 | medium | https://arxiv.org/abs/2308.05443 |
| ref-644 | Lee, H.-C., Woo, H.-M., & Shin, S. (International Journal of Precision Engineering and Manufacturing) | Digital Twin-based Sensor-Free Virtual Mapping for Autonomous Mobile Robot Localization | 논문 | medium | https://link.springer.com/article/10.1007/s12541-026-01598-2 |
| ref-645 | Rinciog, A. 외 (malerinc/slapstack GitHub) | slapstack — README (SLAPStack: storage location assignment simulation for block-stacking warehouses) | 오픈소스 문서 | medium | https://github.com/malerinc/slapstack |
| ref-646 | Skoogh, A., & Johansson, B. | Time-consumption analysis of input data activities in discrete event simulation projects | 논문 | medium | https://www.researchgate.net/publication/235719405_TIME-CONSUMPTION_ANALYSIS_OF_INPUT_DATA_ACTIVITIES_IN_DISCRETE_EVENT_SIMULATION_PROJECTS |
| ref-647 | Lee, Y.-T. T. (NIST, Journal of Research of NIST) | A Journey in Standard Development: The Core Manufacturing Simulation Data (CMSD) Information Model | 정부·연구기관 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC4730674/ |
| ref-648 | IFAC-PapersOnLine 게재 논문 저자(미확인) | Initialization of Simulation-Based Digital Twins for Internal Transport Systems | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2405896324015374 |
| ref-649 | Oyediran, H., Turner, W., Kim, K., & Barrows, M. | Integration of 4D BIM and Robot Task Planning: Creation and Flow of Construction-Related Information for Action-Level Simulation of Indoor Wall Frame Installation | 논문 | medium | https://arxiv.org/abs/2402.03602 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? | 22, 28 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값 |
| 출하 | 수행 자원 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값 |
| 출하 | 제약 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값 |
| 출하 | 완료·인계 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값 |
| 출하 | 예외·성과 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04 | 단계 3. 구현 가설 설계 — q3-04 시뮬레이션 초기값 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| SISO CMSD (Core Manufacturing Simulation Data, SISO-STD-008-2010·SISO-STD-008-01-2012) | 표준 | SISO(Simulation Interoperability Standards Organization) | 22, 28 | ref-647 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4730674/ |
| SLAPStack (블록 적재 창고 저장 위치 배정 시뮬레이션) | 오픈소스 | Rinciog, A. 외 (malerinc/slapstack GitHub) | 22, 3 | ref-645 | https://github.com/malerinc/slapstack |

## 추가 조사 요청

- 단계 3 페이지 H1 아래 상태 줄(> 단계 상태: … 답한 질문: 2건)은 H2 절 밖이라 patches 로 고칠 수 없어 이번 실행에서 갱신하지 못했다(현재 값: 열린 질문 7건 · 답한 질문 4건이 맞음). pipeline 담당에게 H1 아래 상태 줄을 patch 로 바꿀 수 있는 방법(또는 퍼블리셔 자동 갱신)을 요청한다. 같은 이유로 공간 그래프 스키마 초안은 H1 버전 표기를 고치기 위해 content 전체로 보냈다.
- 단계 3 완료 조건 '사용자에게 제안하는 실험 계획'을 채우려면 다음 트랙 실행에서 실험 계획(예: 도면 기반 Open-RMF 시뮬레이션 월드와 현장 측정 비교)의 근거가 되는 측정 항목·공개 데이터 자료가 필요하다(q5-06 과 연결).
- 22. 시뮬레이션·예측용 디지털 트윈 반영에 앞서, 물류센터 시뮬레이션 입력을 중립 형식으로 표준화하거나 물류 대상 입력 데이터 준비 시간을 측정한 자료(국내 포함)가 필요하다 — 이번 근거(31%, CMSD)는 제조 대상이다.
- slotcar 단순화 모델의 회전 속도·가속 파라미터 명칭은 1차 검증 요약 응답에 직접 나오지 않았으므로 rmf_simulation 원문에서 파라미터 이름을 재확인할 필요가 있다.

## 이행한 수정 지시

- f12 강등 — 단계 3 페이지 q3-04 소절의 4D BIM 문장을 [추정]으로 쓰고 SDF 분할·FBX·URDF→SDF 세부를 '원문 미열람으로 미확인'으로 적었으며, ref-649 기관 칸을 'Oyediran, H., Turner, W., Kim, K., & Barrows, M.'로 고치고 각주 제목·reference_updates 요약에 ITcon 2025 게재판을 병기했다.
- f7 수정 — 단계 3 페이지·아이디어 페이지·스키마 초안 6절에서 '별도 파라미터로 설정' 표현을 빼고 '레이아웃 코드에는 충전 설비·차량 사양이 없다(설정 위치는 README 에서 미확인)'로 쓰고, 초기 충전 수준은 README 가 WEPAStacks 사용 사례에 한정한다는 조건을 병기했다.
- f6 필드명 — 단계 3 페이지와 아이디어 페이지에서 physicalParameters 의 minimumSpeed·maximumSpeed·minimumHeight·maximumHeight·width·length 와 typeSpecification 의 maximumLoadMass 원문 이름을 썼다.
- f9·f18 문구 — '입력 데이터 관련 활동이 평균 전체 프로젝트 시간의 31%'로 고치고 '제조 시뮬레이션 대상, 표본 규모 미확인, 2007 발행'을 병기했으며 f18 종합 문장과 4절 불확실성에도 같은 문구를 반영했다.
- ref-647 — 각주와 reference_updates 의 발행일을 2015, 기관 칸을 'Lee, Y.-T. T. (NIST, Journal of Research of NIST)'로 적었다.
- f1·f4 중복 방지 — q3-04 소절에서 building_map_generator 는 'q3-01 소절에서 본 것처럼'으로 가리키며 같은 각주(ref-441)와 ref-406 으로 한 문장만 재서술했고, 시뮬레이션 이점(f4)은 한 문장으로 짧게 두었다.
- 각주 — ref-644·ref-646·ref-647·ref-648·ref-649 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-081 은 기존 각주 줄을 그대로 썼고 ref-406·ref-079·ref-645 는 원문 열람 출처로 표기했다.
- 용어집 — '워밍업 기간'은 glossary_updates 에서 뺐고, 'CMSD'는 '제조 분야 시뮬레이션과 정보 시스템 사이 데이터 교환을 위한 SISO 표준 중립 정보 모델' 범위로만 등록했다.
- 온톨로지 층 — 새 속성을 두지 않고 기존 '높이 기준(단계 4에서 확정)'에 값 후보 'Open-RMF traffic-editor 층 고도(elevation, 미터)'를 병기하고 근거 칸에 f2(실행 2026-09-25-70)를 적었다.
- 온톨로지 문 — 새 속성 '구동 유형'을 두지 않고 기존 '여닫는 방식'의 값 후보로 Open-RMF 문 유형(hinged·double_hinged·sliding·double_sliding)을 더하고 '동작 범위(motion_degrees·motion_direction)' 속성을 추가했으며 근거 칸에 f2·f3 을 적었다.
- 온톨로지 엘리베이터·버전 — '칸 치수(Open-RMF 승강기 칸 폭·깊이, 미터)' 속성을 추가하고, 프런트매터 ontology_version·H1 제목 '공간 그래프 스키마 초안 (v0.9)'·출력 ontology_draft_version 을 0.9 로 맞췄다. H1 은 H2 절 밖이라 patches 로 고칠 수 없어 이 페이지만 content 전체로 보냈다.
- 단계 3 페이지 6절 — 시뮬레이션 초기값 행을 충족(q3-04, 결론은 추정)·'충족 · 전환 미승인'으로 바꾸고, 실험 계획 행은 미충족 유지, 아래 줄을 '다음 단계로 전환: 아니오(완료 조건 미충족: 실험 계획; 막힌 질문 q3-05·q3-06·q3-07·q3-08·q3-09·q3-10)'로 썼다.
- 아이디어 페이지 5절 — '아직 조사되지 않은 구성 요소'에서 q3-04 를 빼고, 새 '시뮬레이션 초기값' 소절에서 설계·도입 검토용 정적 초기값과 운영 중 예측용 현재 상태 초기화를 f16 대로 나누어 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈에 각각 연결했다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.9
- 트랙 로그 항목: 답한 질문: q3-04(시뮬레이션 초기값에 더 필요한 정보 — 3차원·층, 설비 동작, 로봇 모델, 운영 요소, 업무 부하, 현재 상태의 여섯 묶음, 근거 f1~f19, 종합은 추정) / 새 질문: q3-11(f7, 단계 3), q5-06(f14, 단계 5) / 온톨로지 변경: v0.8 → v0.9(2026-09-25, 근거 실행 2026-09-25-70): 층 '높이 기준'에 값 후보 층 고도(elevation) 병기(f2), 문 '여닫는 방식' 값 후보에 Open-RMF 문 유형 추가·'동작 범위' 속성 추가(f2·f3), 엘리베이터 '칸 치수' 속성 추가(f2); 거부 없음; H1 버전 표기 오류(v0.7) 수정 / 완료 조건 평가: 미충족(부족: 사용자에게 제안하는 실험 계획; 막힌 질문 q3-05·q3-06·q3-07·q3-08·q3-09·q3-10, 시뮬레이션 초기값 행은 충족) / 세부영역 반영 제안: 22. 시뮬레이션·예측용 디지털 트윈 2건, 6. 지도·공간·위치 모델 2건, 8. 실시간 세계 상태·데이터 일관성 1건 / 다음 실행 제안: 실험 페이지에 단계 3 실험 계획 제안, 이어서 q3-07 또는 q3-09 / 비고: 단계 3 페이지 H1 아래 상태 줄은 patches 로 갱신하지 못함
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 7, 답함 4, 완료 조건 미충족(실험 계획 없음)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-04 | 답함 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-04 | — | — | — |
| q3-11 | 열림 | — | 시뮬레이션 초기값에 필요한 주문 흐름·초기 재고를 창고 관리 시스템의 로케이션 코드로 받아 공간 그래프의 저장 위치·스테이션 노드에 붙이려면 어떤 대응 규칙과 식별자가 필요한가? (q3-04 에서 파생) | 3 | f7 |
| q5-06 | 열림 | — | 도면 기반으로 만든 시뮬레이션 월드로 예측한 처리량·혼잡 지점을 실제 현장 측정과 비교해, 가설 3 의 '시뮬레이션 초기값으로 쓸 수 있다'를 판정하는 지표와 허용 오차는 무엇인가? (q3-04 에서 파생) | 5 | f14 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 22 | 6. 대표 접근법과 기술 | 도면 주석에서 Open-RMF building_map_generator 로 시뮬레이션 월드를 만드는 방식(바닥·벽·층 고도·문·승강기·스폰 주석, slotcar 등 플러그인)과 추가로 필요한 입력(로봇 모델·주문 흐름·초기 재고·현재 상태), 설계·도입 검토용과 운영 중 예측용 초기화의 구분(추정, 8. 실시간 세계 상태·데이터 일관성과의 경계) |
| 22 | 8. 대표 연구와 자료 | SLAPStack(레이아웃·주문 흐름·초기 충전 수준), SISO CMSD(제조 대상 중립 정보 모델), Skoogh·Johansson 2007(입력 데이터 관련 활동 평균 31%, 제조 대상), IFAC 2024 사내 운송 디지털 트윈 초기화 연구 |
| 6 | 8. 대표 연구와 자료 | 연계 대상: Lee·Woo·Shin(IJPEM 2026) 2D 건축 CAD 도면 기반 가상 환경·점유 격자 지도 자동 생성과 위치추정 오차(저자 보고), 4D BIM 을 로봇 시뮬레이션 월드로 변환한 건설 로봇 연구(추정, 세부 미확인) |
| 6 | 6. 대표 접근법과 기술 | 도면 인식이 채우는 것은 평면 형상과 문·승강기·계단 위치 정도이고 층 고도·벽 높이·설비 동작·로봇 모델·업무 부하는 도면 밖 원천에서 와야 하며 비구조 요소는 빠질 수 있다는 정리(추정, BIM 기반 지도 한계 f13) |
| 8 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 운영 중 예측 시뮬레이션은 실제 부하 상태로 초기화해야 한다는 연구(IFAC 2024)와, 8. 실시간 세계 상태·데이터 일관성이 22. 시뮬레이션·예측용 디지털 트윈에 현재 상태 초기값을 공급하는 쪽이라는 구분(추정) |
