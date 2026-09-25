# 스토리텔러 산출 2026-09-25-58

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | draft | q3-02 답함(3절 소제목 신설), 후속 질문 2건(q3-09·q4-08), 4·5·6·7·8·9절 갱신. H1 아래 단계 상태 줄(답한 질문 1건→2건)은 H2 밖이라 패치로 보내지 못함 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | v0.6 → v0.7: 개념 '경유점'·'주행 차선' 추가·확정, '공용 자원' 속성 '상호 배제 여부' 추가·확정, 다이어그램에 두 개념 추가(연결선 없음), 6절 질문 3건 추가. H1 버전 표기는 H2 밖이라 패치로 보내지 못함(프런트매터 ontology_version 으로 동기화 요청) |
| update | docs/ideas/floorplan-recognition.md | draft | 5절 '핵심 구성 요소' 소절 첫 작성(q3-02: 공간 그래프 두 층위·자원 예약 단위·통과 조건 분리·경로망 초안, 모두 추정과 근거 사실), 새 각주 4건 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크 갱신(스키마 초안 v0.7, 아이디어 5절 핵심 구성 요소, 백로그 후속 질문 17건·q3-02 답함). H1 아래 트랙 상태 줄(현재 단계)은 H2 밖이라 패치로 보내지 못함 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 3 | q3-02 답함(공간 그래프 구역·차선 두 층위, 공용 자원 예약 단위, 로봇별 통행 가능 여부 분리 — 모두 추정), 공간 그래프 스키마 초안 v0.6 → v0.7(경유점·주행 차선 추가, 공용 자원 확정), 후속 질문 2건 | run 2026-09-25-58
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 3: q3-02 답함(공간 그래프를 구역 수준·차선 수준 두 층위로 두는 구현 가설, 추정), 공간 그래프 스키마 초안 v0.7
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 3에서 공간 그래프의 노드·엣지 단위(구역 수준·차선 수준)와 관제 형식의 경유점·차선 속성 정리, 6절 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 q3-02(공간 그래프 두 층위, 공간 세분화 연구)를 6. 대표 접근법과 기술·8. 대표 연구와 자료에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 상호 배제 그룹 | Mutex Group (Open-RMF) | Open-RMF 주행 그래프에서 한 번에 로봇 한 대만 점유할 수 있도록 묶은 경유점·차선의 집합이다. | 15, 16, 6 | ref-689 |
| new | 공간 세분화 | Subspacing (Indoor Space Subdivision) | 실내 공간을 여러 상세 수준의 하위 공간으로 나누고 수준 사이 위계를 노드–관계 구조로 유지해 서로 다른 상세 수준의 네트워크를 만드는 방법이다. | 6, 28 | ref-694 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-689 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp |
| ref-690 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphEdge.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphEdge.msg |
| ref-691 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphNode.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphNode.msg |
| ref-692 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema |
| ref-693 | Henkel, C., & Toussaint, M. | Optimized Directed Roadmap Graph for Multi-Agent Path Finding Using Stochastic Gradient Descent | 논문 | medium | https://arxiv.org/abs/2003.12924 |
| ref-694 | Claridades, A. R. C., Choi, H.-S., & Lee, J. | An Indoor Space Subspacing Framework for Implementing a 3D Hierarchical Network-Based Topological Data Model | 논문 | medium | https://doi.org/10.3390/ijgi11020076 |
| ref-695 | Ray, A., Bradley, C., Carlone, L., & Roy, N. | Task and Motion Planning in Hierarchical 3D Scene Graphs (ISRR 2024) | 논문 | medium | https://arxiv.org/abs/2403.08094 |
| ref-347 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 논문 | medium | https://arxiv.org/abs/2305.07154 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html |
| ref-212 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 오픈소스 문서 | medium | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json |
| ref-268 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 논문 | medium | https://arxiv.org/abs/2511.07175 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 형식 동기화 요청(조사 아님): 단계 3 페이지 H1 아래 단계 상태 줄(답한 질문 1건 → 2건, 열린 질문 7건), 공간 그래프 스키마 초안 H1 버전 표기(v0.6 → v0.7), 트랙 개요 상태 줄(현재 단계가 단계 1로 남아 있음 → 단계 3. 구현 가설 설계)은 H2 절 밖이라 patches 로 보낼 수 없다. pipeline 담당이 프런트매터(ontology_version 등)와 백로그 값으로 동기화하거나 H1 앞 머리 영역 패치를 허용해야 한다.
- 단계 3 페이지 3절 q3-02·스키마 초안 6절: 구역 수준 노드와 차선 수준 경유점·차선을 두 층위로 두고 포함 관계로 잇는 구조를 제시한 독립 출처(교차 확인용)가 필요하다. 현재는 이 위키의 종합(추정)뿐이다.
- 스키마 초안 6절(문·연결 표현): IndoorGML 2.0 JSON 인코딩 초안(26-043)의 Node·Edge·InterLayerConnection 속성을 원문으로 확인해야 한다(이번 실행에서 미러 HTML 이 머리말 위주로 읽혀 확인하지 못함).
- q3-09·q4-08 대비: 구역 수준 노드와 제조사 플릿별 경유점·스테이션의 포함 관계를 자동 생성하거나 검수한 사례, 플릿 중립 그래프에서 플릿별 주행 그래프를 파생·동기화한 공개 구현이 필요하다.
- 참고문헌 표기 확인: ref-031 의 fetched_via 가 github_raw 로 적혀 있으나 fetch_url 이 없고 한계 항목은 입력 원문(inbox)으로 적어 서로 맞지 않는다. 다음 실행에서 열람 경로를 바로잡아야 한다.

## 이행한 수정 지시

- f2: 문구 수정 — 단계 3 페이지 3절 q3-02 '관제 형식의 경유점·차선 속성' 소절에서 문은 차선 이벤트(DoorOpen·DoorClose)와 문 속성(DoorProperties)으로, 승강기는 차선 이벤트(LiftSessionBegin 등)와 경유점의 승강기 안 여부 속성(in_lift, LiftProperties)으로 표현한다고 고쳐 [사실]을 유지했다.
- f4: 그래프 개수를 '기본 9개 그래프, 9개 플릿'으로 쓰고 문은 '정점 사이에 따로 추가한다'까지만 썼다(단계 3 페이지 3절, 아이디어 페이지 5절).
- f3: '같은 상호 배제 그룹에 속한 경유점·차선은 한 번에 로봇 한 대만 점유한다'까지만 [사실]로 쓰고, 점유 예약 표현이라는 해석은 f15 의 [추정] 문장에만 넣었다.
- f13: [추정]으로 강등하고 '연계 대상:' 표시를 유지했다. 장면 그래프의 장소·방 층과 층 사이 포함 관계 설명은 [^ref-347]로, ref-695 는 계층형 3D 장면 그래프로 희소한 계획 문제를 만들어 대규모 환경의 작업·동작 계획을 확장한 연구라는 문장에만 달았다.
- ref-695: reference_updates 의 기관을 'Ray, A., Bradley, C., Carlone, L., & Roy, N.'으로, 제목에 'ISRR 2024'를 병기하고 발행일 2024-03, 각주 접근일 뒤 ' (원문 미열람)'을 붙였다.
- ref-693·ref-694·ref-695·ref-212·ref-268: 이번 실행이 새로 쓴 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다(ref-347 도 같게 처리). 아이디어 페이지의 기존 ref-212·ref-268 정의는 중복 정의를 피하려 새로 쓰지 않았다.
- f12: '산업용 AGV 대상'은 어느 페이지에도 쓰지 않았다.
- f9·f15: 'RELEASE 구역'을 '해제 구역'으로 바꾸고 단계 3 페이지 첫 등장에 '해제 구역(RELEASE)'으로 영문을 병기하며 용어집 항목에 링크했다(아이디어 페이지 첫 등장도 '해제 구역(RELEASE)').
- 인용: ref-031 의 영어 원문 직접 인용은 한 곳도 두지 않고 f8·f10 모두 한국어로 재서술했다(출처당 1회 이하 충족). ref-689 의 상호 배제 그룹 문구도 재서술했다.
- 온톨로지 초안: 2절 개념 목록 표에 '경유점 (Waypoint)'(f1·f5·f6·f7)과 '주행 차선 (Lane)'(f2·f4·f5·f7)을 상태 '확정'으로 추가했다. 정의는 좌표 지점과 두 경유점을 잇는 주행 엣지로만 두고, 속성은 지시한 목록(층·지도 식별자·미터 좌표·대기·통과·주차·충전 여부·허용 편차·승강기 안 여부 / 방향·속도 제한·높이 조건·주행 방향 제약·이벤트·상호 배제 그룹·플릿 그래프 번호)만 넣었다.
- 온톨로지 초안: '공용 자원'에 속성 '상호 배제 여부(Open-RMF 상호 배제 그룹 근거)'만 추가하고(f3·f9·f10) 상태를 초안 → 확정으로 바꿨다. '점유 요소' 속성은 반영하지 않고 6절 미해결 모델링 질문(q3-02·q3-06 관련, [추정])으로 두었다.
- 온톨로지 초안: 3절 관계 행은 추가하지 않고 그 사실을 3절에 한 문장으로 덧붙였다. 경유점·주행 차선과 공간 노드의 관계와 개념 구분은 6절 질문으로 두고 f14 를 [추정] 근거로 달았으며, 4절 다이어그램에는 두 개념을 연결선 없이 추가했다.
- 온톨로지 초안 버전: 프런트매터 ontology_version 과 track_updates.ontology_draft_version 을 '0.7'로 맞췄다. H1 의 '(v0.6)' 표기는 H2 절 밖이라 patches 로 바꿀 수 없어 diff_summary 와 additional_research_requests 에 동기화를 요청했다.
- 단계 3 페이지 6절: 스키마 갱신 완료 조건을 '충족'(검증 판정 '충족 후보(1차 검증) · 미승인')으로 적고, 핵심 구성 요소 조건은 행을 나눴으며, 표 아래를 '다음 단계로 전환: 아니오(… 막힌 질문 q3-03·q3-04·q3-05·q3-06·q3-07·q3-08)'로 두었다. stage_transition 은 넣지 않았다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.7
- 트랙 로그 항목: 답한 질문: q3-02(공간 그래프를 구역 수준·차선 수준 두 층위로 두고 포함 관계로 잇는 구조, 공용 자원 예약 단위, 로봇별 통행 가능 여부 분리 — 종합은 추정, 근거 f1~f18) / 새 질문: q3-09(f14, 단계 3), q4-08(f16, 단계 4) / 온톨로지 변경: v0.6 → v0.7(2026-09-25, 근거 실행 2026-09-25-58): 개념 '경유점' 추가·확정(f1·f5·f6·f7), '주행 차선' 추가·확정(f2·f4·f5·f7), '공용 자원' 속성 '상호 배제 여부' 추가와 확정(f3·f9·f10); 거부: 공용 자원 '점유 요소'(f15 추정 → 6절 질문), 관계 추가 없음(경유점·주행 차선–공간 노드 관계 → 6절 질문, f14) / 완료 조건 평가: 미충족(부족: 아이디어 3 5절 핵심 구성 요소 중 능력 대조·시뮬레이션 초기값, 다른 아이디어와의 연결, 실험 계획; 스키마 단계 3 근거 갱신은 충족 후보) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건, 15. 다중 로봇 경로·교통 관리 — MAPF 1건, 16. 공용 자원·충전·에너지 최적화 1건 / 다음 실행 제안: q3-03(능력 대조), q3-09
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 7, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-02 | 답함 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-02 | — | — | — |
| q3-09 | 열림 | — | 도면 인식은 방·구역 같은 구역 수준 노드를 주지만 주행 경유점·차선은 주지 않을 때, 구역 수준 노드와 제조사 플릿별 차선 수준 경유점·스테이션 사이의 포함 관계를 자동으로 만들거나 사람이 확인하는 규칙은 무엇인가? (q3-02 에서 파생) | 3 | f14 |
| q4-08 | 열림 | — | 플릿 중립의 기본 공간 그래프에서 제조사 플릿별 주행 그래프(Open-RMF graph_idx)나 VDA 5050 관제 보유 통행 제한을 파생·동기화할 때, 로봇별 통행 가능 여부를 어디에 저장하고 도면·지도 판이 바뀌면 어떻게 다시 맞추는가? (q3-02 에서 파생) | 4 | f16 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 공간 그래프를 구역 수준 노드(방·구역·업무 장소)와 차선 수준 경유점·차선의 두 층위로 두고 포함 관계로 잇는 접근(추정, f14), ‘3층 출하 대기장’을 구역 노드 하나로 두고 플릿별 경유점·스테이션을 대응시키는 방식(추정, f17). 트랙 건축 도면 자동 인식 실행 2026-09-25-58. |
| 6 | 8. 대표 연구와 자료 | Claridades·Choi·Lee(2022)의 IndoorGML 공간 세분화(subspacing) 틀(f11, 원문 미열람)과 계층형 3D 장면 그래프 연구(연계 대상, f13 추정). |
| 16 | 6. 대표 접근법과 기술 | rmf_traffic 의 문·승강기 표현(차선 이벤트·경유점 승강기 안 여부)과 상호 배제 그룹(f2·f3), VDA 5050 해제 구역 접근 허가와 startCharging 의 위치(f9·f10), 공용 자원 개체가 걸친 경유점·차선·구역을 가리키는 예약 단위(추정, f15). |
| 15 | 6. 대표 접근법과 기술 | traffic-editor 플릿별 주행 그래프(기본 9개)와 VDA 5050 엣지 통과 조건·관제 보유 통행 제한(f4·f7·f8), 방향 경로망 최적화 ODRM(f12), 도면 차선 그래프를 경로망 자동 생성의 입력 초안으로 두는 관점(추정, f18). |
