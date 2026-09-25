# 스토리텔러 산출 2026-09-25-19

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | q1-03 답함(3절 소제목 신설), 상태 줄 열린 3·답함 3으로 갱신, 4절 결론·불확실성, 5절 q2-06 등록·중복 폐기 기록, 6절 전환 아니오(q1-04·q1-05·q1-06), 7·8·9절 갱신 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0.2 → v0.3: 개념 '작업 스테이션' 추가(확정), '충전 위치' 접근 지점 속성 추가·확정, '엘리베이터' BIM 대응 클래스 속성 추가·확정, 다이어그램에 작업 스테이션 노드, 6절 질문 4건 추가·q1-03 항목 근거 보강 |
| update | docs/ideas/floorplan-recognition.md | draft | 3절에 운영 시설(충전소·작업 스테이션) 보완 사례 소절 추가, 4절에 단계 2 전 선행 근거(IFC 4.3·VDMA LIF·VDA 5050 시설 표현) 작성 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 초안 v0.3, 아이디어 3·4절 갱신, 백로그 q1-03 답함·중복 3건 폐기 반영 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 1 | q1-03 답함(충전 위치·작업 스테이션 보완 사례), 공간 그래프 스키마 초안 v0.2→v0.3, 백로그 중복 3건 폐기·q2-06 등록, 신규 출처 id ref-241~ref-250로 재부여 | run 2026-09-25-19
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1: q1-03 답함(운영 시설을 도면에서 자동 인식한 사례는 검색 범위에서 찾지 못했고 주석·현장 감지·레이아웃 교환·설비 계획으로 보완), 공간 그래프 스키마 초안 v0.3
- 대분류 최근 업데이트: 2026-09-25 — B. 공통 정보·환경 모델: 건축 도면 자동 인식 트랙 단계 1 q1-03 답함, 6. 지도·공간·위치 모델에 반영 제안 2건(대표 접근법, 관련 표준)
- 세부영역 최근 업데이트: —

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 레이아웃 교환 형식 | Layout Interchange Format (LIF) | VDMA가 정한, 무인운반 차량 통합사업자가 노드·엣지·스테이션으로 된 주행 레이아웃을 상위 관제 시스템에 넘기기 위한 교환 형식이다. | 28, 6, 9, 16 | ref-241, ref-031 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-085 | Braga, R. G., Tahir, M. O., Karimi, S., Dah-Achinanon, U., Iordanova, I., & St-Onge, D. | Intuitive BIM-aided robotic navigation and assets localization with semantic user interfaces | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1548684/full |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 논문 | medium | https://arxiv.org/abs/2406.17003 |
| ref-241 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 표준 | high | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-242 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 오픈소스 문서 | medium | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json |
| ref-243 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElement (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md |
| ref-244 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md |
| ref-245 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricApplianceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricApplianceTypeEnum.md |
| ref-246 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 오픈소스 문서 | high | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md |
| ref-247 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 |
| ref-248 | Digani, V., Sabattini, L., Secchi, C., & Fantuzzi, C. | An automatic approach for the generation of the roadmap for multi-AGV systems in an industrial environment | 논문 | medium | https://www.researchgate.net/publication/286354583_An_automatic_approach_for_the_generation_of_the_roadmap_for_multi-AGV_systems_in_an_industrial_environment |
| ref-249 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 벤더 문서 | low | https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23 |
| ref-250 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? | 28, 6 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| VDMA LIF (Layout Interchange Format) | 표준 | VDMA | 28, 6, 9 | ref-241 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) | 표준 | buildingSMART | 6, 28 | ref-243 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md |
| Nav2 Docking Framework (nav2_docking) | 오픈소스 | ROS Navigation (Open Navigation) | 16, 6 | ref-246 | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md |

## 추가 조사 요청

- 단계 2 q2-01·q2-06: VDMA LIF 공식 지침 본문(PDF)과 공식 저장소 스키마에서 스테이션 유형 필드 유무와 판·발행일(1.0.0 2023-09 대 VDMA 2024-03)을 확인해야 한다 — 현재 근거는 제3자 스키마와 README 뿐이다.
- 단계 2 q2-06: IFC 4.3 게시판(ADD2)과 다른 클래스(IfcElectricFlowStorageDevice, IfcFurniture 등)·속성 세트·IDS 에서 로봇 충전소·작업대를 표현하는 방법이나 관례가 있는지 확인이 필요하다.
- 공간 그래프 스키마 초안 6절(q3-02): 작업 스테이션을 공용 자원에 포함할지 판단할 근거(16. 공용 자원·충전·에너지 최적화 정의와 제조사 관제의 작업대·스테이션 예약 사례)가 필요하다.
- 단계 1 q1-03 보강: Digani 외(2014)의 입력 조건과 작업 지점 입력 방식, Beinschob 외(2017)의 병목 목록을 원문으로 확인해야 한다.
- oq-022 관련: 국내 물류센터에서 도면·레이아웃 자료로 충전소·작업대 위치를 로봇 관제에 등록한 공공·학술 사례를 한국어로 더 찾아야 한다.
- 퍼블리셔 확인 요청: ref-241(LIF README)은 실행 2026-09-25-17 브리프가 ref-160 으로 제안한 URL 과 같으므로 URL 중복을 확인해야 한다.

## 이행한 수정 지시

- 출처 id 충돌 — brief 의 ref-318~ref-327 을 ref-241~ref-250 으로 순서대로 일괄 교체해 모든 페이지 각주·프런트매터 sources·reference_updates 에 적용했고 기존 ref-318~ref-327 은 건드리지 않았다.
- f3 — 단계 1 페이지 q1-03 과 아이디어 4절에서 startCharging·stopCharging 을 '즉시 동작(instantAction) 또는 노드 동작'으로 고치고 엣지 언급을 뺐으며, 'charging spot·charging lane' 을 stationType 예로 쓰지 않고 stationType 은 pick·drop 파라미터로만 적었다.
- f4·f5 — 'VDA 5050 3.0.0 은 LIF 를 VDMA 2024-03 으로 인용'과 'LIF README 는 1.0.0 판을 2023-09 로 적음'을 각각 [사실]로 병기하고 열린 질문(출처 충돌)을 open_question_updates 에 등록했으며, 용어집 정의에는 판·날짜를 넣지 않았다.
- f6 — 단계 1 페이지·아이디어 4절·초안에 'VDMA 공식 산출물이 아닌 제3자(continua-systems) 스키마 기준'을 밝히고 LIF 표준 구조로 확정하지 못했다고 적었으며, 일반화는 f7 [추정] 문장으로만 썼다.
- f7 — '레이아웃은 통합사업자가 만든다'를 'LIF 는 통합사업자가 관제에 레이아웃을 넘기는 교환 형식으로 정의된다'로 좁혀 [추정]으로 썼다.
- f13·f18·f20 — MiR 충전기 마커(ref-249)를 쓴 모든 문장에 '[추정] 벤더 주장' 또는 '벤더 주장' 병기를 하고 매뉴얼 게재 사이트 사본임을 본문과 각주 제목에 적었다.
- f17 — 논문 요지(창고 충전소 최적 위치를 페이지랭크형 그래프로 정함)만 [사실]로 쓰고 '도면에서 읽는 대상이 아니라' 해석은 뺐으며, 16. 공용 자원·충전·에너지 최적화 6절 반영 제안에서 f17 을 빼고 3. 처리능력·거점·설비 계획으로 연결만 제안했다.
- f2 — 'manually annotated' 직접 인용을 쓰지 않고 '문서에 자동 인식 설명이 없고 속성은 편집기에서 사람이 입력한다'로 재서술했다.
- f8·f9·f10 — IFC 근거가 개발 브랜치(ifc4.3-main) 원본이며 게시판 IFC 4.3 ADD2 와 문구가 다를 수 있음을 본문과 각주 제목(ref-243~ref-245)에 적고, f9 에 같은 발행 주체라 독립 교차가 아님을 유지했다.
- f12 — '의미 지도에서 얻은 자유 공간 지도를 바탕으로'를 빼고 '(입력 조건과 작업 지점 입력 방식은 미확인)'을 붙였다.
- 원문 미열람 — ref-085·ref-109·ref-247·ref-248·ref-249·ref-250 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 와 '원문 미열람. ' 요약 시작을 넣었다.
- 온톨로지 — 작업 스테이션을 확정으로 추가(f1·f3·f6), 충전 위치에 접근 지점 속성 추가·확정(f1·f6·f14), 엘리베이터에 BIM 대응 클래스 속성 추가·확정(f8)했고, 정보 출처 속성과 공용 자원 포함 여부는 6절 질문으로 두었으며, 버전을 0.3 으로 H1·프런트매터·JSON 에 맞추고 다이어그램에 작업 스테이션을 관계 없는 노드로 넣었다(상태 줄은 auto 마커라 퍼블리셔가 갱신).
- 초안 6절 기존 q1-03 항목에 f18 [추정] 근거 문장과 각주를 붙이고 'q1-03 은 실행 2026-09-25-19 에서 답함'을 적었다.
- 백로그 — q1-07·q2-05·q4-06 을 폐기로 backlog_updates 에 냈고, 단계 1 페이지 5절에 폐기 사유와 f19→q2-01·q2-03, f17(실행 2026-09-25-11)→q4-02 연결을 적었으며 2절 표에는 넣지 않았다.
- 단계 3 새 질문(f7)은 backlog_updates 에 넣지 않고 단계 1 페이지 5절과 q1-03 본문에서 단계 4. 지도 변환 보정과 현장 정합의 q4-03 관련 근거로 연결했다.
- 단계 2 새 질문(f10)을 q2-06 으로 backlog_updates 에 등록하고 단계 1 페이지 5절 표에 추가했다(q2-05 id 는 재사용하지 않음).
- 단계 1 페이지 — 2절 q1-03 을 답함·2026-09-25-19·[3절 q1-03](#q1-03) 으로 바꾸고 3절에 '### q1-03 … {#q1-03}' 소제목을 두었으며, 6절 검증 판정을 '충족 · 미승인', 표 아래 줄을 '다음 단계로 전환: 아니오(막힌 질문 q1-04·q1-05·q1-06)'로 쓰고 상태 줄을 열린 질문 3건·답한 질문 3건으로 맞췄다(상태 줄 갱신을 위해 이 페이지는 전체 content 로 보냄).
- q1-03 결론 — '이번 검색 범위(한·영 검색 15회)에서 찾지 못했다'로 범위를 적고 없다고 단정하지 않았으며 중심 주장(f18)을 [추정]으로 두었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.3
- 트랙 로그 항목: 답한 질문: q1-03(f1~f20, 결론 f18 은 검색 범위 기준 [추정]) / 새 질문: q2-06(f10); 단계 3 질문(f7)은 q4-03 중복으로 미등록, f7 은 q4-03 근거로 연결; 폐기: q1-07(q1-06 중복)·q2-05(q2-01·q2-03 중복)·q4-06(q4-02 중복), 실행 2026-09-25-11 중복 등록 / 온톨로지 변경: v0.2 → v0.3(2026-09-25, 근거 실행 2026-09-25-19): 개념 '작업 스테이션' 추가·확정(f1·f3·f6), '충전 위치' 속성 접근 지점 추가·확정(f1·f6·f14), '엘리베이터' 속성 BIM 대응 클래스(IfcTransportElement, 개발 브랜치 기준) 추가·확정(f8). 거부: 충전 위치·작업 스테이션의 정보 출처 속성(f18·f19 추정)과 작업 스테이션의 공용 자원 포함 여부 → 6절 질문(q3-02) / 완료 조건 평가: 충족(검증 stage_complete), 단계 전환 미승인(막힌 질문 q1-04·q1-05·q1-06) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건, 16. 공용 자원·충전·에너지 최적화 3건, 28. 표준·상호운용성·다사업자 거버넌스 1건, 3. 처리능력·거점·설비 계획 1건, 21. 온보딩·설정·현장 시운전 1건, 22. 시뮬레이션·예측용 디지털 트윈 1건 / 출처: 신규 출처 id 를 ref-241~ref-250 으로 재부여(기존 id 충돌) / 다음 실행 제안: q1-04, 이어서 q1-05·q1-06
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 3, 답함 3, 완료 조건 충족(검증 판정 충족), 단계 전환 미승인(막힌 질문 q1-04·q1-05·q1-06)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-03 | 답함 | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-03 | — | — | — |
| q1-07 | 폐기 | — | — | — | — |
| q2-05 | 폐기 | — | — | — | — |
| q4-06 | 폐기 | — | — | — | — |
| q2-06 | 열림 | — | 로봇 충전소·작업 스테이션처럼 IFC 4.3 표준 유형 값에 없는 운영 시설을 BIM 에 담으려면 사용자 정의 유형·속성 세트로 표현해야 하는가, 이를 정한 IDS·속성 세트 관례나 사례가 있는가? (q1-03 에서 파생) | 2 | f10 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 운영 시설(충전소·작업 스테이션) 위치는 도면 자동 인식 사례가 검색 범위에서 확인되지 않았고 사람의 주석(Open-RMF traffic-editor 경유점 속성), 현장 감지(Nav2 도크 보정, 3D 스캔 의미 지도 기반 경로망 자동 설계), 레이아웃 교환(LIF)으로 채우는 것으로 보인다는 [추정]과 근거 사실(ref-079, ref-246, ref-247, ref-241, 실행 2026-09-25-19). |
| 6 | 7. 관련 표준·프레임워크·오픈소스 | VDMA LIF(통합사업자→관제 레이아웃 교환 형식, 판·발행일 출처 충돌, 스테이션 구조는 제3자 스키마 기준), IFC 4.3 IfcTransportElement(엘리베이터, 개발 브랜치 기준), VDA 5050 3.0.0 지도 식별·배포(mapId·mapVersion, downloadMap·enableMap) (ref-241, ref-242, ref-243, ref-031). |
| 16 | 6. 대표 접근법과 기술 | 충전소 위치 정보의 출처: traffic-editor is_charger·dock_name 수동 주석(ref-079), Nav2 도크 데이터베이스와 검출 보정(연계 대상, ref-246), MiR 충전기 마커 감지(벤더 주장, ref-249). 시설 위치와 접근 지점을 분리해야 할 것으로 보인다는 [추정](f19). 정밀 도킹은 로봇 자체 지능·제어 쪽 연계 대상. |
| 16 | 7. 관련 표준·프레임워크·오픈소스 | VDA 5050 3.0.0 은 충전을 즉시 동작 또는 노드 동작으로 쓰는 startCharging·stopCharging 으로 표현하고 구역 유형에 충전소를 두지 않는다(ref-031). Nav2 도킹 프레임워크(ref-246). |
| 16 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 창고 충전소 배치 최적화(Stark 외 2024, ref-109)는 3. 처리능력·거점·설비 계획의 충전기 배치로 연결한다. |
| 3 | 8. 대표 연구와 자료 | Stark 외(2024-06 프리프린트, 원문 미열람): 전동 산업용 트럭 플릿 창고의 충전소 최적 위치를 페이지랭크형 그래프 모델로 정하는 방법(ref-109). |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | VDMA LIF(README 1.0.0·2023-09 대 VDA 5050 3.0.0 의 'VDMA 2024-03' 인용 충돌, 열린 질문), VDA 5050 의 LIF 경로 가져오기 규정, IFC 4.3 운송 요소 클래스와 콘센트·전기기기 유형 열거에 로봇 충전 설비 값 부재(개발 브랜치 기준) (ref-241, ref-031, ref-243, ref-244, ref-245). |
| 21 | 6. 대표 접근법과 기술 | 다중 AGV 도입 병목(정밀 지도, 픽업·하역 위치 좌표, 경로망 설계)을 3D 스캔 의미 지도로 줄이는 반자동 방법(Beinschob 외 2017, ref-247)과 충전기 앞으로 로봇을 몰고 가 마커로 위치를 등록하는 절차(벤더 주장, ref-249). |
| 22 | 8. 대표 연구와 자료 | 현장 스캔과 객체 인식으로 공장 계획용 건조 환경 디지털 트윈을 자동 생성하는 방법(Sommer 외 2023, 원문 미열람, ref-250). 계획용 트윈이므로 8. 실시간 세계 상태·데이터 일관성과 구분한다. |
