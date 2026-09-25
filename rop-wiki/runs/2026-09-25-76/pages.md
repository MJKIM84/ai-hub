# 스토리텔러 산출 2026-09-25-76

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md | draft | q4-03 답함(3절 {#q4-03} 신설, 추정 중심), 후속 질문 q4-12·q4-13, 완료 조건 2행 충족(1차 예비)·전환 미승인, 출처 16건 추가, 이력 행 추가; 2차 수정: 상태 줄 수치·완료 조건 갱신, 7절에 10. 설비·건물 시스템 연동 추가 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | v1.0 → v1.1: 층 속성 '시스템별 층 식별자(별칭)' 추가(MassRobotics planarDatum 제외), 개념 '좌표계 정렬'은 반영하지 않고 6절 근거 보강, 6절에 층·장소 식별자 대응 근거와 도면–현장 정합 절차 초안(추정) 추가; 2차 수정: H1 을 v1.1 로, 프런트매터 sources 에서 미인용 ref-159·ref-745·ref-750 제거 |
| update | docs/ideas/floorplan-recognition.md | draft | 5절에 '좌표 정렬과 층·목적지 이름 맞춤' 소절(q4-03, 추정 중심)과 q4-02·q4-03 을 합친 '도면–현장 정합 절차 초안(추정)' 소절 추가; 2차 수정: 5절을 replace 로 보내 기존 소절의 'q4-03 미조사·정합 절차 미완성' 문장을 이번 결과로 고치고 메타 문장 삭제 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절: 공간 그래프 스키마 초안 현재 버전을 v1.1 로 고치고 실행 2026-09-25-76 산출물 변화 단락 추가(2차 수정: replace 로 보내 괄호 문장 삭제) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 4 | q4-03 답함(좌표 정렬 절차·층/목적지 대응표, 추정 중심), 공간 그래프 스키마 초안 v1.1(층 속성 '시스템별 층 식별자' 추가), 도면–현장 정합 절차 초안(추정) 반영 | run 2026-09-25-76
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 4: q4-03 답함(도면–로봇 지도 좌표 정렬과 층·목적지 대응표, 추정 중심), 공간 그래프 스키마 초안 v1.1, 도면–현장 정합 절차 초안(추정)
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델(건축 도면 자동 인식 트랙 단계 4): 좌표 정렬과 층·목적지 이름 맞춤 조사, 세부영역 반영 제안 6건(6. 지도·공간·위치 모델 4건, 21. 온보딩·설정·현장 시운전 1건, 10. 설비·건물 시스템 연동 1건)
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 q4-03 에서 좌표 정렬·층/목적지 대응표 조사(추정 중심), 6·7·9·11절 반영 제안(실행 2026-09-25-76)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 유사 변환 | Similarity Transformation | 회전·이동·균일 축척만으로 한 좌표계의 점을 다른 좌표계로 옮기는 변환으로, 대응점 쌍에서 최소제곱으로 추정해 도면·관제 지도와 제조사 로봇 지도를 맞추는 데 쓴다. | 6, 21, 9 | ref-153, ref-744, ref-745 |
| new | 공통 좌표계 | Common Coordinate System (CCS, ISO 21423) | ISO 21423 이 시설 안의 한 점을 원점으로 정해 여러 제조사 이동로봇이 위치를 미터 단위로 함께 표현하게 하는 시설 공통 좌표계다(최종안 요약 기준). | 6, 28, 9 | ref-746, ref-159 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-346 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Level.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Level.msg |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-338 | OGC (Open Geospatial Consortium) / Apple | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 표준 | medium | https://docs.ogc.org/cs/20-094/ |
| ref-162 | GS1 | Identifying a physical location - GLN | 표준 | medium | https://www.gs1.org/standards/id-keys/gln/physical-location |
| ref-345 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 정부·연구기관 | medium | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 |
| ref-224 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 논문 | medium | https://arxiv.org/abs/2408.01737 |
| ref-743 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Lift.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Lift.msg |
| ref-744 | Palonen, A. (axelpale/nudged GitHub) | nudged — README (Affine transformation estimator e.g. for multi-touch gestures and calibration) | 오픈소스 문서 | medium | https://github.com/axelpale/nudged |
| ref-745 | Umeyama, S. (IEEE Transactions on Pattern Analysis and Machine Intelligence 13(4), 376-380) | Least-Squares Estimation of Transformation Parameters Between Two Point Patterns | 논문 | medium | https://ieeexplore.ieee.org/document/88573/ |
| ref-746 | ISO (iTeh Standards 미리보기) | ISO/FDIS 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://standards.iteh.ai/catalog/standards/iso/f772b16e-582a-4ed4-9f79-0a80ad376f40/iso-fdis-21423 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://www.iso.org/standard/86749.html |
| ref-747 | Carpin, S. (Autonomous Robots) | Fast and accurate map merging for multi-robot systems | 논문 | medium | https://link.springer.com/article/10.1007/s10514-008-9097-4 |
| ref-748 | Kakuma, D., Tsuichihara, S., Garcia Ricardez, G. A., Takamatsu, J., & Ogasawara, T. | Alignment of Occupancy Grid and Floor Maps Using Graph Matching | 논문 | medium | https://ieeexplore.ieee.org/document/7889504/ |
| ref-749 | Hou, J., Kuang, H., & Schwertfeger, S. (ROBIO 2019) | Fast 2D Map Matching Based on Area Graphs | 논문 | medium | https://arxiv.org/abs/1911.07432 |
| ref-750 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보구축작업규정 (고시 제2021-1445호, 2021-12-24) | 정부·연구기관 | medium | https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/%EC%8B%A4%EB%82%B4%EA%B3%B5%EA%B0%84%EC%A0%95%EB%B3%B4%EA%B5%AC%EC%B6%95%EC%9E%91%EC%97%85%EA%B7%9C%EC%A0%95/(2021-1445,20211224) |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 수행 자원 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 제약 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 완료·인계 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03 | 단계 4. 지도 변환 보정과 현장 정합 |
| 출하 | 예외·성과 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03 | 단계 4. 지도 변환 보정과 현장 정합 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| nudged (2D 유사 변환 추정 라이브러리) | 오픈소스 | Palonen, A. (axelpale/nudged GitHub) | 6, 21 | ref-744 | https://github.com/axelpale/nudged |

## 추가 조사 요청

- 단계 4 페이지 3절·스키마 6절: IMDF 1.0.0 에서 층 표기 관례가 다른 층을 같은 순번의 여러 Level 로 모델링할 수 있는지(f11 의 검증 미확인 부분이라 본문에서 뺐다) 원문으로 확인 필요 — q4-13 의 층 대응표 기준 키 판단 근거가 된다.
- 단계 4 페이지 3절: ISO 21423 발행판의 공통 좌표계(CCS) 정의(층별 원점 여부, 기준점 개수, 미터 단위 문구)를 발행 기관 자료로 확인 필요 — 현재 FDIS 미리보기 검색 요약에만 기대며 oq-027 해결 근거가 되지 못한다.
- 단계 4 페이지 3절: 실내공간정보 구축 작업규정 현행(2021-12-24 개정 이후) 조문의 기준점 선정·절대좌표 부여 규정 확인 필요 — 제정판 기준으로만 검색됐다.

## 이행한 수정 지시

- f11 부분 강등 — 단계 4 페이지 3절 q4-03 에서 ordinal 0·지하층 음수·short_name 분리만 [사실][^ref-338](각주에 원문 미열람)로 두고 '같은 순번의 여러 Level' 절은 삭제했으며, 4절 불확실성에 확인하지 못해 싣지 않았음을 적었다.
- f7 — ISO 21423 CCS 문장에 'FDIS 미리보기(iTeh Standards) 검색 요약 기준, 발행판 문구·층별 원점 여부·기준점 개수 미확인'을 병기하고 ref-746 과 함께 ref-159 각주를 두었으며(단계 페이지·아이디어 페이지), oq-027 은 근거 보강으로만 적고 해결로 바꾸지 않았다.
- f19 — MassRobotics planarDatum 을 단계 페이지·스키마 6절·아이디어 5절에서 '층 구분에 쓰일 수 있는 기준면 식별자로 보이는' 값으로 쓰고 층 식별자로 단정하지 않았으며, Lift.msg 의 층 이름 목록과 LiftState 의 주석 없는 문자열을 구분해 적었다.
- f1·f5 — 단계 페이지 3절에 '제조사 지도와 공통 좌표의 변환'(대응 경유점 4쌍 권장, 플릿 어댑터)과 '도면 축척과 층–기준층 변환'(기준점 2쌍 이상, traffic-editor)을 별도 소제목으로 나누고 서로 다른 변환임을 밝히는 문장을 넣었으며, 아이디어 5절과 스키마 6절에도 같은 구분을 적었다. MSE 는 '변환 오차 추정값(평균제곱오차)'으로 썼다.
- f3 — nudged README 문장에 JavaScript 2.x 기준이며 Open-RMF 튜토리얼의 Python 판과의 구현 동일성은 미확인임을 병기했다(단계 페이지 3절, 4절 불확실성, 표준 목록 요약).
- f16·f17 — 실내공간정보 구축 작업규정 문장을 '2018-03-05 제정판 기준으로 검색됨, 현행 조문 미확인, 2021-12-24 개정판(고시 제2021-1445호) 존재(개정 내용 미확인)'로 쓰고 ref-345·ref-750 각주를 달았다.
- f18 — 좌표 정렬 절차 초안을 [추정](이 위키의 종합, 단일 출처 없음, 신뢰도 low)으로 표기하고 mermaid 절차도를 직접 그렸으며, 스키마 초안 6절과 아이디어 3 5절에 q4-02 답과 합친 '도면–현장 정합 절차 초안(추정)'을 실었다.
- f22 — 시나리오 예외·성과 칸에 '설명용 가정 사례'임을 밝히고 국내 층 표기('1층'이 지상 출입층)와 IMDF ordinal 의 대응은 출처로 확인하지 않은 가정이라고 적었다.
- f13·f14·f15 — 자동 정합 연구 소제목 앞에 지도 작성·위치추정은 분류 원문 9장 '로봇 자체 지능·제어'의 연계 대상이고 알고리즘은 제조사 SLAM 지도를 입력으로 하는 시운전 보조 도구 후보로만 다룬다고 적었으며, f14 는 '대략적 정렬 수준으로 보고됐다'고 썼다.
- f21 — 목적지 대응표 문장에 GLN·WMS 로케이션 코드의 부여·관리는 상위 업무 시스템 쪽 연계 대상이고 ROP 는 대응표만 둔다는 경계를 넣고, WMS 로케이션 코드–경유점 대응 사례를 찾지 못했음(oq-029 미해결)을 적었다.
- 온톨로지 변경 '층' 속성 승인 — 스키마 2절 층 행에 '시스템별 층 식별자(별칭: Open-RMF 건물 지도 층 이름·승강기 층 이름 문자열, VDA 5050 mapId, IMDF 순번(ordinal)·약칭(short_name))'을 더하고 근거 f6·f9·f10·f11(실행 2026-09-25-76)을 적었으며 상태는 확정 유지, MassRobotics planarDatum 은 6절 메모로만 두었다. 프런트매터 ontology_version 과 JSON ontology_draft_version 을 '1.1'로 올렸고 상태 표시는 자동 영역이 프런트매터 값으로 채운다. H1 '(v1.0)'은 H2 절 밖이라 부록 R-3 패치로는 바꿀 수 없어, 패치 적용 코드가 프런트매터 ontology_version 으로 H1 을 '(v1.1)'로 맞추도록 요청한다.
- 온톨로지 변경 '좌표계 정렬' 거부 — 개념 표에 넣지 않고 스키마 6절 정렬 정보 항목의 근거 보강으로 두었으며, 거부 근거(f1·f2 층 키 아래 플릿별 대응점은 별도 개념 쪽 논거, VDA 5050 은 공유 좌표계라 근거 아님, '층간 정렬 기준점'·용어집 '지도 정합'과의 범위 미정)를 적었다.
- 단계 4 페이지 6절 — 완료 조건 2행 충족 여부를 '충족(1차 예비, 2차 확인)', 검증 판정을 '충족 · 미승인'으로 쓰고 아래 줄을 '다음 단계로 전환: 아니오(막힌 질문 q4-04·q4-05·q4-07·q4-08·q4-09·q4-10·q4-11 및 이번 새 질문 q4-12·q4-13)'로 두었다. 상태 줄은 입력의 '진행 중'을 유지하고 track_updates.stage_transition 은 넣지 않았다.
- q4-03 — 백로그를 답함(answer_link #q4-03)으로, 단계 페이지 2절을 답함·실행 2026-09-25-76·#q4-03 으로 바꾸고, 3절에 '### q4-03 … {#q4-03}' 소제목을 두었으며 첫 문단에 핵심 종합이 추정이라 종합 신뢰도 low 임을 밝혔다.
- 원문 미열람 표기 — 단계 페이지 8절에 추가한 ref-745·ref-746·ref-747·ref-748·ref-749·ref-750·ref-338·ref-162·ref-345(와 ref-159) 각주 정의 끝에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었으며, raw 로 연 ref-153·ref-105·ref-079·ref-230·ref-346·ref-286·ref-743·ref-744 와 입력 원문 ref-031 에는 붙이지 않았다(ref-224 기존 각주는 원래대로 미열람 표기 유지).
- 세부영역 반영 제안 — 6. 지도·공간·위치 모델, 21. 온보딩·설정·현장 시운전, 10. 설비·건물 시스템 연동 페이지는 pages 에 넣지 않고 area_reflection_proposals 와 트랙 로그·단계 페이지 7절에만 남겼으며, oq-027·oq-045·oq-029 는 open_question_updates 에 넣지 않아 해결로 바꾸지 않았다.
- docs/tracks/floorplan-recognition/space-graph-schema-draft.md: 각주 정의 8개를 참고문헌에서 만들어 붙임: ref-105, ref-162, ref-230, ref-286, ref-345, ref-743, ref-744, ref-746
- docs/ideas/floorplan-recognition.md: 각주 정의 11개를 참고문헌에서 만들어 붙임: ref-159, ref-162, ref-230, ref-286, ref-346, ref-743, ref-744, ref-746, ref-747, ref-748, ring ref-749
- 2차: 아이디어 페이지 5절 — 패치를 replace 로 보내 '내비게이션 지도 변환 보정' 소절 끝 문장을 'q4-02는 실행 2026-09-25-75, q4-03은 실행 2026-09-25-76에서 답했고 합친 정합 절차 초안(추정)은 아래 소절에 있다'로, '도면–현장 차이 탐지와 반영' 소절 끝 문장을 'q4-03은 실행 2026-09-25-76에서 답했고 정합 절차 초안은 아래 소절에 있다, 실행 2026-09-25-75에서는 스키마 v1.0 유지'로 고쳤으며, 새 소절의 메타 문장 '위 소절 끝의 … 갱신된다'를 지웠다. 새 출처 각주 정의 11건은 5절 끝에 함께 넣었다.
- 2차: 스키마 초안 H1 — 패치로는 H1 을 바꿀 수 없어 이 페이지를 전체 content 로 보내고 H1 을 '공간 그래프 스키마 초안 (v1.1)'로 고쳤다. 프런트매터 ontology_version·JSON ontology_draft_version 과 함께 '1.1'로 맞췄고, auto:page-status 마커 안은 퍼블리셔가 채우므로 손대지 않았다.
- 2차: 스키마 초안 프런트매터 sources 에서 본문 미인용·각주 미정의인 ref-159·ref-745·ref-750 을 뺐고, reference_updates 의 ref-745·ref-750 cited_by 에서 space-graph-schema-draft.md 를 뺐다.
- 2차: 단계 4 페이지 상태 줄 — 패치로는 H1 아래 줄을 바꿀 수 없어 이 페이지를 전체 content 로 보내고 '> 단계 상태: 진행 중 · 열린 질문: 9건 · 답한 질문: 3건 · 완료 조건: 충족 · 마지막 실행: 2026-09-25'로 고쳤다.
- 2차: 단계 4 페이지 7. 관련 세부영역 목록에 [10. 설비·건물 시스템 연동] 항목(승강기 상태 층이 주석 없는 문자열이라 지도 층 이름과의 층 대응표가 필요할 것으로 보이는 지점, [추정][^ref-286][^ref-743], oq-045)을 9. 로봇·제조사 관제 연동 다음에 더해 프런트매터 related_areas 와 맞췄다.
- 2차: 트랙 개요 6절 — 패치를 replace 로 보내 공간 그래프 스키마 초안 항목의 '현재 버전 v1.0'을 'v1.1'로 고치고, 덧붙인 단락의 괄호 '(위 목록의 '현재 버전 v1.0'은 v1.1 로 읽는다)'를 지웠다.
- 2차: index_updates.category_recent 의 반영 제안 건수를 '세부영역 반영 제안 6건(6. 지도·공간·위치 모델 4건, 21. 온보딩·설정·현장 시운전 1건, 10. 설비·건물 시스템 연동 1건)'으로 고쳤다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
- 온톨로지 초안 버전: 1.1
- 트랙 로그 항목: 답한 질문: q4-03(좌표 정렬 절차와 층·목적지 대응표, 근거 f1~f23, 핵심 종합 f18~f23 은 추정, 종합 신뢰도 low) / 새 질문: q4-12(f20, 국소 왜곡과 목적지별 잔차 판정), q4-13(f19, 층 대응표 기준 키와 겹치는 층) / 온톨로지 변경: v1.0 → v1.1: 층 속성 '시스템별 층 식별자(별칭)' 추가(f6·f9·f10·f11, MassRobotics planarDatum 제외 — 6절 메모); 거부: 개념 '좌표계 정렬'(f1·f2·f5·f6·f8 → 6절 정렬 정보 항목 근거 보강). 버전 이력 행: 1.1 | 2026-09-25 | 층 속성 '시스템별 층 식별자(별칭)' 추가(f6·f9·f10·f11), 거부: 개념 '좌표계 정렬'(6절 근거 보강) | 2026-09-25-76 / 완료 조건 평가: 보정 항목 목록 충족(2차 확인), 도면–현장 정합 절차 초안 충족(2차 확인 — q4-02·q4-03 답을 스키마 초안 6절과 아이디어 3. 건축 도면 자동 인식 5절에 반영), 단계 전환 미승인(열린 질문 q4-04·q4-05·q4-07·q4-08·q4-09·q4-10·q4-11·q4-12·q4-13) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 4건(6·7·9·11절), 21. 온보딩·설정·현장 시운전 1건(6절), 10. 설비·건물 시스템 연동 1건(6절) / 다음 실행 제안: q4-04(도면·지도 버전 관리와 재검증), 이어서 q4-07(지도 파일 배포와 mapVersion)
- 개요 진행 현황: 단계 4 진행 중 — 열린 질문 9, 답함 3(q4-01·q4-02·q4-03), 완료 조건 충족, 단계 전환 미승인

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-03 | 답함 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-03 | — | — | — |
| q4-12 | 열림 | — | 제조사 SLAM 지도에 국소 왜곡이 있어 층당 유사 변환 하나의 목적지별 잔차가 노드 허용 편차(VDA 5050 allowedDeviationXY 등)를 넘을 때, 구역별 분할 변환이나 목적지별 보정점을 어떻게 두고 시운전 합격 기준을 무엇으로 정하는가? (q4-03 에서 파생) | 4 | f20 |
| q4-13 | 열림 | — | 메자닌·중층·지하층·다른 건물 동이 섞인 물류센터에서 물리적 층 순번(IMDF ordinal 등)을 층 대응표의 기준 키로 쓰고 Open-RMF 층·승강기 층 이름, VDA 5050 mapId, 그리고 층 구분에 쓰일 수 있는 기준면 식별자로 보이는 MassRobotics planarDatum 을 별칭으로 매달 때, 같은 순번에 여러 표기가 있거나 층이 부분적으로 겹치는 경우를 어떻게 표현하는가? (q4-03 에서 파생) | 4 | f19 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 층별·플릿별 대응 경유점(최소 4쌍 권장)으로 유사 변환을 최소제곱 추정하고 변환 오차 추정값을 확인하는 방법(사실, ref-153·ref-105·ref-744·ref-745)과 traffic-editor 의 층–기준층 변환(기준점 2쌍 이상, ref-079)이 서로 다른 변환이라는 점, 정합 절차 초안과 목적지 대응점별 잔차 판정(추정). |
| 6 | 7. 관련 표준·프레임워크·오픈소스 | ISO/FDIS 21423 공통 좌표계 원점 정의(FDIS 미리보기 검색 요약 기준, 발행판 미확인, ref-746·ref-159), MassRobotics location 의 planarDatum(층 필드 없음, ref-230), IMDF 층 순번·약칭(ref-338), Open-RMF Level·Lift 층 이름(ref-346·ref-743), nudged 라이브러리(ref-744). |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 공통 좌표계 원점·층 대응표·목적지 대응표·제조사별 변환과 잔차 확인은 ROP, 제조사 지도 작성·위치추정과 격자 지도–도면 자동 정합 알고리즘은 로봇 쪽 연계 대상(시운전 보조 도구 후보), GLN·WMS 로케이션 코드 부여는 상위 업무 시스템 연계 대상이라는 경계(추정). |
| 6 | 11. 열린 질문 | oq-027(ISO 21423 CCS)·oq-045(지도 층 이름–승강기 층 이름)·oq-029(GLN·WMS 로케이션–경유점)의 근거 보강. 모두 해결 아님. |
| 21 | 6. 대표 접근법과 기술 | 시운전에서 층별 대응점 4쌍 이상과 목적지 대응점별 잔차로 정렬을 합격 판정하는 방법(추정), 국내 실내공간정보 구축 작업규정의 기준점 선정(2018 제정판 기준 검색, 현행 미확인), 격자 지도–도면 자동 정합 연구(Carpin 2008, Kakuma 외 2017 대략적 정렬, Hou 외 2019). oq-077 근거 보강. |
| 10 | 6. 대표 접근법과 기술 | Open-RMF 승강기 상태의 층이 주석 없는 문자열(ref-286)이고 승강기 메시지는 운행 층을 층 이름 목록으로 두므로(ref-743), 지도 층 이름과의 층 대응표가 필요할 것으로 보인다(추정, oq-045). |
