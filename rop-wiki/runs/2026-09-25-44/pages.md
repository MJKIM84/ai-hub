# 스토리텔러 산출 2026-09-25-44

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md | draft | q2-03 답함(3절 소제목 신설: VDA 5050 지도 배포·구역 집합, LIF, Open-RMF, Nav2 격자 지도, 제조사 PNG 평면도, 수용 형식 3분류), 상태 줄·4·5·6·8·9절 갱신, 후속 질문 q4-07·q3-06 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | v0.5 → v0.6: 층별 지도에 교환 형식(후보) 속성 추가(f1·f5·f7·f8), H1 버전 표기 오류(v0.4) 수정, 6절에 지도 판 근거 보강·VDA 5050 구역 집합·공용 자원 목록 형식·층·장소 식별자 대응 질문 추가 |
| update | docs/ideas/floorplan-recognition.md | draft | 4절: '관제·ROP 수용 형식' 소절 신설(이 위키가 구성한 비교표, 3분류 종합 [추정], VDA 5050 구역 집합·경로망 설정, Nav2 격자 지도, building.yaml), 첫 단락과 q2-01 소절의 q2-03 안내 문구 갱신 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 스키마 초안 v0.6, 아이디어 페이지 4절 관제 수용 형식(q2-03), 백로그 수치 갱신 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 2 | q2-03 답함(관제·ROP 수용 형식: 격자 지도·레이아웃 교환·구역 집합), 공간 그래프 스키마 초안 v0.5 → v0.6, 후속 질문 q4-07·q3-06 등록 | run 2026-09-25-44
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2: q2-03 답함(로봇 관제·ROP가 받아들이는 지도·레이아웃·구역 형식 정리), 공간 그래프 스키마 초안 v0.6
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 2에서 VDA 5050 지도 배포·구역 집합, VDMA LIF, Open-RMF building.yaml, Nav2 격자 지도를 수용 형식으로 정리(세부영역 반영 제안 3건)
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 2(q2-03)에서 관제가 받는 지도·구역·레이아웃 형식을 정리했고, 7절과 9절 반영을 제안했다

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 구역 집합 | Zone Set (VDA 5050 zoneSet) | 하나의 지도(mapId)에 붙는 다각형 구역들의 묶음으로, 구역마다 통행 금지·진입 허가·속도 제한·우선·벌점·방향 같은 유형과 파라미터를 둔다. | 6, 15, 28 | ref-980, ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-978 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_map_server — README | 오픈소스 문서 | high | https://github.com/ros-navigation/navigation2/blob/main/nav2_map_server/README.md |
| ref-979 | Open Robotics (open-rmf) | rmf_traffic_editor — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_traffic_editor |
| ref-980 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/zoneSet.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/zoneSet.schema |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-212 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 오픈소스 문서 | medium | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json |
| ref-227 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 벤더 문서 | low | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 |
| ref-346 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Level.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Level.msg |
| ref-349 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Graph.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Graph.msg |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) | 오픈소스 | ROS Navigation (ros-navigation/navigation2) | 6, 9 | ref-978 | https://github.com/ros-navigation/navigation2/blob/main/nav2_map_server/README.md |

## 추가 조사 요청

- 단계 2 완료 조건 2: 공간 그래프 스키마 초안 3절에 넣을 관계(엣지) 유형의 표준 대응(IndoorGML 2.0 Edge·레이어 간 연결, IFC 공간 경계 A 유형, BOT adjacentZone 등)을 확인하는 조사가 필요하다 — 단계 전환의 막힌 조건이다.
- q2-03 보강: ABB·KUKA·OTTO 등 물류 로봇 관제 제품과 국내 관제 제품이 도면·지도 파일을 어떤 형식으로 가져오는지 공개 매뉴얼로 확인한 자료가 없다(현재 벤더 주장 1건). 단계 페이지 3절 q2-03 '격자 지도' 소제목에 필요하다.
- q2-03 보강: VDA 5050 3.0.0 명세 전체(6.3절 이후, factsheet 포함)를 대조해 지도 파일 내용 형식을 정하는지 확인해야 f4(추정)의 부재 관찰을 확정하거나 고칠 수 있다.
- q3-06 관련: 충전소·승강기·작업 스테이션 같은 공용 자원 목록을 관제 사이에 교환하는 형식(검색 2회 범위에서 찾지 못함)을 한·영으로 더 검색할 필요가 있다.
- oq-025: LIF 판·발행일(VDA 5050 인용 2024-03 대 README 1.0.0·2023-09) 충돌을 VDMA 공식 발행 정보로 확인할 필요가 있다.
- 퍼블리셔 담당 요청: 이번 형식 검사 실패(logs/daily/2026-09-25.md 의 깨진 링크 ../glossary/hierarchical-task-network.md)는 이 실행의 스토리텔러 산출 페이지가 아니라 퍼블리셔가 쓰는 일일 로그에 있다. 이 실행의 페이지에는 그 링크가 없으며, 용어집에 hierarchical-task-network 항목이 없으므로(다른 트랙 실행의 용어 후보로 보임) 일일 로그 생성 시 존재하지 않는 용어집 페이지에는 링크하지 않거나 해당 용어 항목을 먼저 만들도록 확인이 필요하다. 스토리텔러는 브리프 근거 없이 그 용어를 등록할 수 없다.

## 이행한 수정 지시

- 인용 — 단계 2 페이지와 아이디어 페이지 모두 ref-031(VDA 5050 명세) 원문 직접 인용을 0회로 두고 f1(6.3.1)·f3(5.2) 구절을 모두 재서술했다.
- f3·f5 LIF 판·발행일 — 단계 페이지 q2-03 VDA 5050 소제목에 'VDA 5050 3.0.0 은 LIF 를 VDMA 2024-03 으로 인용하고, LIF 공식 README 는 1.0.0 판을 2023-09 로 적는다'로 둘 다 제시하고 열린 질문 oq-025 링크를 달았으며, 아이디어 페이지는 기존 LIF 소절의 같은 문장을 가리켰다.
- f4 — [추정]을 유지하고 '이번에 읽은 명세 범위(6.3절)에서는'과 '부재 확정은 아니다'를 단계 페이지·아이디어 페이지 문장 안에 남겼으며, 28. 표준·상호운용성·다사업자 거버넌스 반영 제안에서도 지도 파일 형식 미규정을 [추정]으로 제안했다.
- f12 — 3분류 문장에 '이 위키의 분류'와 '공용 자원 목록 전용 교환 형식은 이번 검색 범위(검색 2회)에서 찾지 못했다(부재 확인 아님)'를 밝히고, VDA 5050 주문은 레이아웃 교환 형식과 같은 칸에 두지 않고 '주문마다 보내는 주행 구간 그래프'로 따로 적었다(비교표에서도 제외).
- f7·f14 — Nav2 map_server 격자 지도 YAML 을 로봇 쪽 내비게이션 스택의 입력 형식으로 밝히고 '연계 대상:' 표시를 유지했으며, 격자 지도 생성·위치추정을 로봇 자체 지능·제어 쪽 연계 대상으로만 썼다.
- f8 — .building.yaml 에서 시뮬레이션 월드를 생성한다는 내용은 형식 설명으로만 쓰고 22. 시뮬레이션·예측용 디지털 트윈에는 연결 링크만 두었으며, 8. 실시간 세계 상태·데이터 일관성과 섞지 않았다.
- f5·f6·f9·f10·f11·f13·f14 — 이미 게시된 주장은 새 문장으로 반복하지 않고 아이디어 3 페이지 3·4절, 단계 2 페이지 q2-01 대조 사례, 단계 1 q1-03 답, 6. 지도·공간·위치 모델 3·9절을 가리키는 문장으로 쓰고 기존 각주(ref-046, ref-212, ref-346, ref-349, ref-079, ref-105, ref-227, ref-031)를 재사용했다.
- f13 — 단계 페이지 q2-03 '분류 원문 질문과의 관계'와 스키마 초안 6절 새 항목에서 층·장소 식별자 대응 문제를 열린 질문 oq-027·oq-045(단계 페이지)와 q4-03·q4-07(스키마 초안)에 연결해 적었다.
- f11 — '[추정] 벤더 주장' 병기와 유통사 게재본 표시를 유지하고 각주 정의에 ' (원문 미열람)'을 붙였다.
- 원문 미열람 표시 — ref-978·ref-979·ref-980 은 표시 없이 쓰고 reference_updates 에 source_unopened: false 로 냈으며, ref-046 은 기존 각주 줄을 그대로 썼다. 단계 페이지에 새로 정의한 ref-079·ref-105·ref-212·ref-227 과 스키마 초안에 새로 정의한 ref-346 에는 ' (원문 미열람)'을 붙이고, 이미 정의가 있던 ref-346·ref-349(단계 페이지)와 ref-079·ref-212(스키마 초안) 정의 줄은 유지했다.
- 온톨로지 변경 '층별 지도' — 속성 '교환 형식(후보: … 이 파일의 내용 형식은 명세 6.3절 범위에서 정해지지 않은 것으로 보임)'을 지시 문구 그대로 f1·f5·f7·f8 각주(ref-031·ref-046·ref-978·ref-979)와 함께 더하고 상태는 확정을 유지했다. '지도 판' 속성은 넣지 않고 6절 지도 버전 항목에 'VDA 5050은 mapId·mapVersion으로, 제3자 LIF 스키마는 layoutVersion으로 판을 식별한다'를 [사실][^ref-031][^ref-212]로 보강했다.
- 온톨로지 변경 '제한 구역' — 개념으로 넣지 않고 6절에 지시 문구대로 VDA 5050 구역 집합을 공간 그래프 개념으로 둘지 묻는 새 항목([사실][^ref-980][^ref-031])과 '구역 집합은 도면이 아니라 관제가 만들어 배포하는 설정이다' 문장을 두었다.
- 초안 버전 — ontology_version 을 '0.5' → '0.6'으로 올리고 H1 을 '공간 그래프 스키마 초안 (v0.6)'으로 고쳤으며, 프런트매터·page-status 표기·track_updates.ontology_draft_version 을 0.6 으로 맞추고 2절 끝 버전 설명 단락에 v0.6(교환 형식 후보 추가, 지도 판 속성·구역 개념 미반영)을 더했다. H1·상태 줄은 H2 절 밖이라 patches 로 고칠 수 없어 이 페이지는 전체 content 로 보냈다.
- 단계 2 페이지 — 2절 q2-03 을 답함(2026-09-25-44, [답](#q2-03))으로 바꾸고 3절에 지시된 소제목 '### q2-03 … {#q2-03}'을 두었으며, 6절 완료 조건 1은 충족·검증 판정 '미승인', 완료 조건 2는 미충족, 표 아래 줄은 '다음 단계로 전환: 아니오(관계(엣지) 쪽 표준 대응 없음; 열린 질문 q2-04·q2-06·q2-07·q2-08·q2-09)', 상태 줄은 '열린 질문: 5건 · 답한 질문: 3건 · 완료 조건: 미충족'으로 썼다. 상태 줄이 H2 절 밖이라 이 페이지도 전체 content 로 보냈다.
- 아이디어 3 페이지 4절 — '관제·ROP 수용 형식' 소절에 비교가 이 위키가 구성한 것이며 출처 표를 옮기지 않았음을 밝히고 3분류 종합을 [추정]으로 두었으며, 4절 첫 단락과 q2-01 소절의 'q2-03은 단계 2 실행이 채운다'·'아직 조사하지 않아 이 절에 없다' 문구를 새 소절을 가리키도록 고쳤다.
- 새 질문 — f4 파생 질문을 q4-07(단계 4, origin f4), f12 파생 질문을 q3-06(단계 3, origin f12)으로 backlog_updates 에 등록하고, 단계 페이지 5절에 q4-07 과 q4-03·q4-04, q3-06 과 q3-02 의 관계를 한 줄씩 적었다.
- 용어집 — '구역 집합(Zone Set, VDA 5050 zoneSet)'을 근거 f2(ref-980, ref-031)로 등록하되 정의를 지시 문구대로 고치고, 설명에 해제 구역·VDA 5050·레이아웃 교환 형식·점유 격자 지도 페이지 링크를 두었다.
- 세부영역 반영 제안 — 6. 지도·공간·위치 모델과 28. 표준·상호운용성·다사업자 거버넌스 페이지는 고치지 않고 area_reflection_proposals 로만 냈으며, 6. 지도·공간·위치 모델 9절 제안은 기존 경계 문장·각주(ref-031, ref-153) 재사용으로 적고 f14 를 새 문장으로 반복하지 않도록 했다.
- 형식: 퍼블리셔 사전 검사의 깨진 링크(logs/daily/2026-09-25.md → ../glossary/hierarchical-task-network.md)를 확인했다. 이 링크는 이번 실행이 낸 네 페이지(단계 2 페이지, 공간 그래프 스키마 초안, 아이디어 3 페이지 4절 패치, 트랙 개요 6절 패치)와 용어집 갱신 어디에도 없고 퍼블리셔가 쓰는 일일 로그에 있어 스토리텔러 산출물에서 고칠 부분이 없다. 내용은 바꾸지 않고 같은 산출물을 다시 냈으며, 이번 실행 페이지의 링크 대상(용어집 vda-5050·release-zone·layout-interchange-format·occupancy-grid-map, 세부영역·열린 질문·단계 페이지)은 모두 docs_tree 에 있음을 재확인했다. 일일 로그 쪽 조치는 additional_research_requests 에 퍼블리셔 담당 요청으로 적었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.6
- 트랙 로그 항목: 답한 질문: q2-03(f1~f14, 관제·ROP 수용 형식 3분류는 이 위키의 추정) / 새 질문: q4-07(단계 4. 지도 변환 보정과 현장 정합, f4), q3-06(단계 3. 구현 가설 설계, f12) / 온톨로지 변경: v0.5 → v0.6: 개념 '층별 지도'에 속성 '교환 형식(후보)' 추가(f1·f5·f7·f8, 근거 실행 2026-09-25-44); 거부: '지도 판' 속성(6절 지도 버전 질문 q4-02·q4-03·q4-04 근거 보강, f1·f6), 개념 '제한 구역'(6절 VDA 5050 구역 집합 질문, f2); H1 버전 표기 오류(v0.4) 수정 / 완료 조건 평가: 미충족(부족: 표준과 대응시킨 관계(엣지) 유형이 스키마 초안에 없음; 열린 질문 q2-04·q2-06·q2-07·q2-08·q2-09. 완료 조건 1(아이디어 4절)은 q2-03 소절로 자체 평가 충족, 검증 미승인) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건(7절, 9절), 28. 표준·상호운용성·다사업자 거버넌스 1건(7절) / 다음 실행 제안: 엣지 표준 대응 조사와 q2-07(IndoorGML 2.0 연결 표현), 이어서 q2-04·q2-06. 참고: 트랙 개요 H1 아래 상태 줄의 '현재 단계: 단계 1. 선행 연구·제품 사례 조사'가 트랙 설정 current_stage 와 실제 진행(단계 2)과 맞는지 트랙 담당의 확인이 필요하다(이 실행은 단계 전환을 내지 않아 줄을 고치지 않았다). 형식 재작성: 일일 로그의 깨진 용어집 링크(hierarchical-task-network)는 이 실행 산출물 밖의 문제로 퍼블리셔 담당에게 넘겼다.
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 5, 답함 3, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-03 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-03 | — | — | — |
| q4-07 | 열림 | — | VDA 5050 downloadMap 으로 배포하는 지도 파일의 내용 형식이 제조사마다 다를 때, 도면에서 만든 층별 지도를 제조사별 지도 파일로 변환·배포하고 mapVersion 을 맞추는 책임과 절차를 ROP 가 어떻게 둘 수 있는가? (q2-03 에서 파생) | 4 | f4 |
| q3-06 | 열림 | — | 충전소·승강기·작업 스테이션 같은 공용 자원 목록을 관제 사이에 교환하는 전용 형식이 없을 때, LIF 스테이션·Open-RMF 경유점 속성·VDA 5050 경로망 설정 가운데 무엇을 기준으로 공용 자원 목록을 내보낼 수 있는가? (q2-03 에서 파생) | 3 | f12 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 7. 관련 표준·프레임워크·오픈소스 | 주제 페이지로 분리된 7절(area06-s7)에 로봇 관제가 받는 지도·구역·레이아웃 형식을 더한다: VDA 5050 3.0.0 의 지도 식별(mapId·mapVersion)과 downloadMap·enableMap·deleteMap 배포, 구역 집합(zoneSet, 10종 유형) [사실][^ref-031][^ref-980]; VDMA LIF 레이아웃 교환 [사실][^ref-046]; Nav2 map_server 격자 지도 YAML(로봇 쪽 입력, 연계 대상) [사실][^ref-978]; Open-RMF .building.yaml 과 주행 그래프 파일 생성 [사실][^ref-979]; 수용 형식 3분류와 공용 자원 목록 전용 형식 부재는 이 위키의 추정 [추정]. |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 기존 경계 표 문장과 각주(ref-031, ref-153)를 재사용해, 로봇 자체 지능·제어 행의 'ROP가 직접 맡는 것'에 도면 기반 결과를 제조사·관제 수용 형식(레이아웃·구역·공용 자원 설정)으로 변환·전달하는 일을 지도 판 관리와 함께 적는 것을 제안한다. 격자 지도 생성·위치추정은 연계 대상으로 유지하며 f14 를 새 문장으로 반복하지 않는다 [추정]. |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | VDA 5050 3.0.0 의 지도 식별·배포 동작과 구역 집합(zoneSet) 스키마 [사실][^ref-031][^ref-980], 이번에 읽은 명세 범위(6.3절)에서는 지도 파일 내용 형식이 정해지지 않은 것으로 보인다는 관찰(부재 확정 아님) [추정][^ref-031], VDMA LIF 레이아웃 교환과 판·발행일 충돌(oq-025) [사실][^ref-046][^ref-031]을 반영한다. |
