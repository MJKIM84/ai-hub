# 스토리텔러 산출 2026-09-25-75

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md | draft | q4-02 답함(3절 소제목 신설), 후속 질문 q4-11·q5-07, 4·5·6·7·8절 갱신. H1 아래 상태 줄(패치 범위 밖)은 열린 질문 8건·답한 질문 2건으로 바뀌어야 한다 |
| update | docs/ideas/floorplan-recognition.md | draft | 5절에 '도면–현장 차이 탐지와 반영' 소절 신설(q4-02, 실행 2026-09-25-75, 추정 중심) |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 6절 정렬 정보·도면–현장 차이·지도 버전 항목에 근거 보강(f12·f13·f15·f16, 실행 2026-09-25-75). 개념·관계 변경 없음, 초안 버전 v1.0 유지 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절 살아있는 산출물에 실행 2026-09-25-75(단계 4, q4-02) 반영 내용 한 단락 추가. 상태 줄(현재 단계 단계 4 유지, 마지막 트랙 실행 2026-09-25)은 변경 없음 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 4 | q4-02 답함(도면–현장 차이의 지속성별 탐지·반영 경로와 ROP 경계, 추정 중심), 후속 질문 q4-11·q5-07, 스키마 초안 변경 없음(v1.0) | run 2026-09-25-75
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 4. 지도 변환 보정과 현장 정합: q4-02 답함(도면–현장 차이를 구조 변경·반정적 배치·임시 장애물로 나눈 탐지·반영 경로, 추정), 후속 질문 2건
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 건축 도면 자동 인식 트랙 단계 4에서 도면–현장 차이 탐지와 반영 경로(q4-02)를 정리하고 6절·9절 반영을 제안
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 4 q4-02(도면–현장 차이 탐지·반영) 결과를 6. 대표 접근법과 기술, 9. ROP가 직접 맡는 것과 외부와 연계하는 것 절에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 스캔 대 BIM 비교 | Scan-vs-BIM | 설계 BIM·3D 모델을 현장 레이저 스캔 점군에 정합해 모델 객체의 시공 상태와 설계 대비 편차를 찾는 방법이다. | 6, 21 | ref-745 |
| new | 반정적 객체 | Semi-static Object | 팔레트·랙·가구처럼 로봇이 관측하는 동안은 움직이지 않지만 시간이 지나면 위치가 바뀌거나 나타나고 사라져 정적 지도를 낡게 만드는 물체다. | 6, 8 | ref-748, ref-747 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-743 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_costmap_2d — include/nav2_costmap_2d/obstacle_layer.hpp | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/include/nav2_costmap_2d/obstacle_layer.hpp |
| ref-744 | Vega-Torres, M. A. (MigVega GitHub) | SLAM2REF — README (연계 논문 Construction Robotics 8(2), 2024-07, DOI 10.1007/s41693-024-00126-w) | 오픈소스 문서 | medium | https://github.com/MigVega/SLAM2REF |
| ref-745 | Bosché, F. (Advanced Engineering Informatics) | Automated recognition of 3D CAD model objects in laser scans and calculation of as-built dimensions for dimensional compliance control in construction (Advanced Engineering Informatics 24(1), 107-118) | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1474034609000482 |
| ref-746 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 논문 | medium | https://www.mdpi.com/1424-8220/23/13/6066 |
| ref-747 | Shaik, N., Liebig, T., Kirsch, C., & Müller, H. (KI 2017) | Dynamic Map Update of Non-static Facility Logistics Environment with a Multi-robot System | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-319-67190-1_19 |
| ref-748 | Qian, J. 외 (RSS 2023) | POV-SLAM: Probabilistic Object-Aware Variational SLAM in Semi-Static Environments | 논문 | medium | https://arxiv.org/abs/2307.00488 |
| ref-749 | 윤동희, 백주미, 심지수, 이동근, 송두삼(설비공학 논문집 36(5), 251-261) | 노후건축물에서 모바일기기를 이용한 Scan-to-BIM 역설계 도면생성 방안 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003077202 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-160 | Prakhya, S. M., Yang, L., & Liu, Z. | Lifelong 3D Mapping Framework for Hand-held & Robot-mounted LiDAR Mapping Systems | 논문 | medium | https://arxiv.org/abs/2501.18110 |
| ref-221 | Vega Torres, M. A., Braun, A., & Borrmann, A. | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 논문 | medium | https://arxiv.org/abs/2408.15870 |
| ref-224 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 논문 | medium | https://arxiv.org/abs/2408.01737 |
| ref-270 | Macenski, S. (SteveMacenski GitHub) | slam_toolbox — README (Slam Toolbox for lifelong mapping and localization in potentially massive maps with ROS) | 오픈소스 문서 | medium | https://github.com/SteveMacenski/slam_toolbox |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg |
| ref-644 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_costmap_2d — README | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/README.md |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 제약 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-02 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 예외·성과 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-02 | 단계 4. 지도 변환 보정과 현장 정합 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| SLAM2REF (라이다 데이터의 기준 지도 다중 세션 정렬 도구) | 오픈소스 | Vega-Torres, M. A. (MigVega GitHub) | 6, 21 | ref-744 | https://github.com/MigVega/SLAM2REF |

## 추가 조사 요청

- 단계 4 페이지 3절 q4-11: 도달 불가 보고·변화 탐지 결과를 임시 막힘과 반정적 배치 변화로 가르는 판정 기준(지속 시간, 반복 횟수, 여러 로봇의 일치)을 제시한 연구·현장 자료가 필요하다 — f18 이 근거 없음으로 남겼다.
- 6. 지도·공간·위치 모델 11절 oq-022: 국내 물류센터에서 도면–현장 차이를 확인한 사례가 여전히 없다(f19). 한국어 자료 추가 조사가 필요하다.
- scan-vs-BIM 명칭과 물류 시설 적용 사례를 원문으로 확인할 출처가 필요하다(ref-745 스니펫에 명칭 없음).
- H1 아래 단계 상태 줄은 패치 범위(H2 절) 밖이라 이번 출력으로 갱신하지 못했다. 퍼블리셔가 '열린 질문: 8건 · 답한 질문: 2건'으로 맞추도록 pipeline 담당에게 요청한다.

## 이행한 수정 지시

- f1 명칭 분리 — 단계 페이지·아이디어 페이지에서 Bosché(2010) 제안 문장은 [사실]로 두고, 'scan-vs-BIM 으로 불린다'는 별도 [추정] 문장으로 떼었으며 건설 시공 품질 관리 대상·물류 적용 미확인을 함께 적었다.
- f2 병기 — 오차율 문장에 '저자 보고, 단일 출처, 원문 미열람'과 비교 기준(BIM 결과의 실 폭·깊이 대 기존 건축도면)을 적고, 좁은 공간·장애물 조건의 오차 증가 문장에 '검색 요약 기준'을 붙였다.
- f14 분리 — 단계 페이지·아이디어 페이지에서 '현장의 예기치 않은 막힘이 관제 쪽 신호로 올라온다'를 별도 [추정] 문장으로 떼었다.
- f15 분리 — '그래프 자체를 고치지 않고 반영'을 별도 [추정] 문장으로 두고 메시지 정의가 그래프 수정 여부를 말하지 않는다고 적었다(단계 페이지·아이디어 페이지·스키마 초안).
- f3·f4·f11 출처 독립성 — 단계 페이지 3절과 4절 불확실성에 ref-221·ref-744 가 같은 TUM 저자 그룹, ref-743·ref-644 가 같은 Nav2 프로젝트임을 적고 교차 확인으로 쓰지 않았다.
- f4 디지털 트윈 — README 의 시설 디지털 트윈 갱신을 '시설의 현재 상태를 나타내는 지도 갱신'으로만 옮기고 22. 시뮬레이션·예측용 디지털 트윈에는 연결하지 않았다.
- f3~f11 범위 — 각 문장 앞에 '연계 대상:'을 유지하고, 절 머리에 SLAM·다중 세션 정렬·변화 탐지·비용 지도가 분류 원문 9장 로봇 자체 지능·제어 쪽 연계 대상임을 적었다(관제 규격 f12~f15 는 연계 대상 표시 없이 ROP 반영 수단으로 둠).
- f16~f19 — 모두 [추정]으로 두고 '이 위키의 종합이며 단일 출처 없음'을 밝혔으며, f18 시나리오는 '다음은 설명을 위한 가상의 시나리오이다.'로 시작하고 수치를 넣지 않았고, mermaid 도식 아래에 이 위키의 추정 구조임을 적었다.
- 인용 — ref-270·ref-031 은 직접 인용 없이 모두 재서술했다.
- 각주 미열람 표시 — ref-745·746·747·748·749·160·221·224 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-031·270·569·644·743·744 는 원문 연 출처로 두었다.
- ref-747 — 기관 칸을 'Shaik, N., Liebig, T., Kirsch, C., & Müller, H. (KI 2017)'로, 발행일을 2017-09 로 고쳐 각주와 reference_updates 에 반영했다.
- ref-745 — 발행일을 2010-01 로, 제목 뒤 서지 'Advanced Engineering Informatics 24(1), 107-118'을 보강했다.
- ref-744 — 제목에 연계 논문 'Construction Robotics 8(2), 2024-07, DOI 10.1007/s41693-024-00126-w'를 병기하고 발행일은 미확인으로 두었다.
- 기존 id 재사용 — ref-224·270·644·031·160·221·569 는 새 id 를 만들지 않고 기존 각주 문자열 그대로 썼다.
- 단계 페이지 6절 — 두 번째 행을 '미충족'(검증 판정 '미충족 · 미승인')으로 두고 표 아래 줄을 지시 문구 그대로 썼으며, 트랙 개요 상태 줄의 현재 단계는 단계 4 로 유지했다(개요 상태 줄 변경 없음).
- q4-02 — 단계 페이지 2절에서 답함(2026-09-25-75, #q4-02)으로 바꾸고 3절에 '### q4-02 … {#q4-02}' 소제목을 두었으며, backlog_updates 에 답함과 새 질문 q4-11(단계 4, origin f17)·q5-07(단계 5, origin f8)을 등록했다.
- oq-022 — 해결로 바꾸지 않았다(open_question_updates 없음, 불확실성에 미해결로 명시).
- 스키마 초안 — ontology_version '1.0' 유지, 6절 정렬 정보·도면–현장 차이·지도 버전 항목의 근거 보강으로 f12·f13·f15·f16(추정)만 덧붙이고 개념·관계 표는 바꾸지 않았다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
- 온톨로지 초안 버전: 1.0
- 트랙 로그 항목: 답한 질문: q4-02(도면–현장 차이의 지속성별 탐지·반영 경로와 ROP 경계, 근거 f1~f19, 종합은 추정) / 새 질문: q4-11(단계 4, f17), q5-07(단계 5, f8) / 온톨로지 변경: 없음(공간 그래프 스키마 초안 v1.0 유지, 6절 정렬 정보·도면–현장 차이·지도 버전 항목에 f12·f13·f15·f16 근거 보강만) / 완료 조건 평가: 미충족(부족: 도면–현장 정합 절차 초안 — q4-03 미답) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건, 21. 온보딩·설정·현장 시운전 1건, 24. 자산·소프트웨어 수명주기 관리 1건 / 다음 실행 제안: q4-03
- 개요 진행 현황: 단계 4 진행 중 — 열린 질문 8, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-02 | 답함 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-02 | — | — | — |
| q4-11 | 열림 | — | 로봇이 보고한 도달 불가(VDA 5050 NODE_UNREACHABLE)나 제조사 SLAM 의 변화 탐지 결과를 임시 막힘과 반정적 배치 변화로 가르고, 구역 집합·차선 폐쇄로 처리할지 지도 판을 올릴지 정하는 기준(지속 시간, 반복 횟수, 여러 로봇의 일치)은 무엇인가? (q4-02 에서 파생) | 4 | f17 |
| q5-07 | 열림 | — | 도면–현장 차이 탐지 방법(재측량 대조, 다중 세션 변화 탐지)의 성능을 물류 현장에서 놓친 변화·잘못 탐지한 변화와 지도 갱신 지연으로 측정하려면 어떤 지표와 시험 절차가 필요한가? (q4-02 에서 파생) | 5 | f8 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 도면–현장 차이 탐지 방법(scan-vs-BIM 재측량 대조, BIM 기반 다중 세션 정렬·변화 탐지 — 연계 대상)과 지속성별 반영 경로(구조 변경·반정적 배치·임시 장애물, 추정). 근거 ref-745·ref-221·ref-747·ref-743·ref-031·ref-569. |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 변화 탐지 계산·SLAM·비용 지도는 로봇·제조사 쪽 연계 대상이고, 탐지된 차이를 구역 집합(새 zoneSetId)·차선 폐쇄·지도 판으로 반영하고 도면 변경 이력을 관리하는 것은 ROP 쪽이라는 경계(추정). 근거 ref-031·ref-569·ref-270. |
| 21 | 6. 대표 접근법과 기술 | 시운전 전 재측량으로 도면과 현장을 대조하는 방법(Bosché 2010 scan-vs-BIM, 국내 노후 건축물 Scan-to-BIM 연구의 저자 보고 오차율)과 기준 지도 정렬 도구 SLAM2REF(연계 대상). 근거 ref-745·ref-749·ref-744. |
| 24 | 6. 대표 접근법과 기술 | 현장 변화에 따른 지도 판(mapVersion) 갱신·사전 적재 후 활성화와 구역 집합 교체(내용 불변, 새 zoneSetId) 규칙, 임시 적치 대응을 판 갱신과 구역·차선 처리로 나누는 흐름(추정). 근거 ref-031. |
