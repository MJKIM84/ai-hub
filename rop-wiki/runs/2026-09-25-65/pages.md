# 스토리텔러 산출 2026-09-25-65

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | draft | q3-03 답함(3절 소제목 신설), 후속 질문 q3-10·q5-05, 4·5·6·8·9절 갱신, 7절 반영 제안 추가. H1 아래 단계 상태 줄(답한 질문 2건 → 3건)은 H2 절 밖이라 패치로 보낼 수 없으므로 코드에서 맞춰야 한다 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0.7 → v0.8: 문에 자동 구동 여부·장애인 접근 가능 속성(f8), 계단에 단 높이·디딤판 길이·단 수 속성(f9) 추가(두 행 확정 유지). 개념 '통과 요구 조건'은 6절 질문으로. H1 의 (v0.7) 표기는 H2 절 밖이라 패치로 보낼 수 없어 프런트매터 ontology_version 0.8 에 맞춰 코드가 (v0.8)로 바꿔야 한다 |
| update | docs/ideas/floorplan-recognition.md | draft | 5절: 핵심 구성 요소에 '능력 대조' 소절 신설, '다른 아이디어와의 연결' 작성(아이디어 1·13. 작업 배정 — MRTA 연결, 추정), 새 각주 정의 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절 살아있는 산출물 링크: 스키마 초안 v0.8, 아이디어 페이지 5절 능력 대조·다른 아이디어와의 연결, 백로그 후속 질문 수와 답한 질문(q3-03) 갱신. 상태 줄은 단계·날짜 변동이 없어 그대로 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 3 | q3-03 답함(요구–제공 능력 매칭·설비 연동 선택 조건·로봇별 통행 가능 부분 그래프, 추정), 공간 그래프 스키마 초안 v0.7 → v0.8, 후속 질문 q3-10·q5-05 | run 2026-09-25-65
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 3. 구현 가설 설계: q3-03 답함(공간 요소 통과 조건과 로봇 능력의 대조, 추정), 공간 그래프 스키마 초안 v0.8
- 대분류 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 3(중심 영역 6. 지도·공간·위치 모델): 로봇 능력과 문·계단·승강기 통과 조건의 대조 방식(추정)과 IFC 문·계단 속성을 스키마 초안에 반영
- 세부영역 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 트랙 단계 3: q3-03 에서 공간 그래프의 통과 조건과 로봇 능력 대조, 로봇별 통행 가능 부분 그래프 파생(추정)을 확인하고 6. 대표 접근법과 기술 반영을 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 통과 가능성 | Traversability | 특정 로봇이 공간 그래프의 구역·차선·문·계단·승강기를 지나갈 수 있는지를 로봇 능력(정적 조건)으로 판정하는 통과 가능 여부이며, 문 닫힘 같은 현재 상태는 8. 실시간 세계 상태·데이터 일관성 쪽에서 따로 다룬다. | 6, 5, 8, 13 | ref-649, ref-650, ref-461, ref-651 |
| new | 차선 폐쇄 | Lane Closure | 관제가 실행 중에 주행 그래프의 특정 차선을 일시적으로 쓰지 못하게 닫는 조치로, Open-RMF 에서는 플릿 이름과 닫을 차선 번호 목록을 담은 요청 메시지(LaneRequest)로 한다. | 15, 8, 6 | ref-645 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-348 | ISPRS International Journal of Geo-Information(MDPI) 게재 논문 저자(미확인) | Data Model for IndoorGML Extension to Support Indoor Navigation of People with Mobility Disabilities | 논문 | medium | https://www.mdpi.com/2220-9964/9/2/66 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema |
| ref-419 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcDoor (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcDoor.md |
| ref-461 | Buildings(MDPI) 게재 논문 저자(Concordia University, 목록 미확인) | Ontology for BIM-Based Robotic Navigation and Inspection Tasks | 논문 | medium | https://www.mdpi.com/2075-5309/14/8/2274 |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp |
| ref-644 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-645 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg |
| ref-646 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_route — README (Nav2 Route Server) | 오픈소스 문서 | medium | https://github.com/ros-navigation/navigation2/blob/main/nav2_route/README.md |
| ref-647 | de Vos, K., van den Brandt, G., Senden, J., Pauwels, P., van de Molengraft, R., & Torta, E. | Generation of skill-specific maps from graph world models for robotic systems | 논문 | medium | https://arxiv.org/abs/2402.18174 |
| ref-648 | Omer 외(Omer, de Vos, Pauwels, Torta, Monteriù; RoboCup 2024 심포지엄 논문집) | Semantic Path Planning for Heterogeneous Robots from Building Digital Twin Data | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-031-85859-8_5 |
| ref-649 | buildingSMART International | Pset_DoorCommon - IFC 4.3.2 Documentation | 표준 | medium | https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_DoorCommon.htm |
| ref-650 | buildingSMART International | Pset_StairCommon - IFC4.3.2.0 Documentation | 표준 | medium | https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_StairCommon.htm |
| ref-651 | IDTA (admin-shell-io/submodel-templates GitHub) | IDTA 02020 Capability Description — README (Submodel Template, Version 1.0) | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-652 | Vieira da Silva, L. M. 외 | A Capability and Skill Model for Heterogeneous Autonomous Robots | 논문 | medium | https://arxiv.org/abs/2209.10900 |
| ref-653 | Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau) | On realizing autonomous transport services in multi story buildings with doors and elevators | 논문 | medium | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full |
| ref-654 | Morilla-Cabello, D., & Montijano, E. | CHORAL: Traversal-Aware Planning for Safe and Efficient Heterogeneous Multi-Robot Routing | 논문 | medium | https://arxiv.org/abs/2601.10340 |
| ref-655 | Halilovic, A., Hasic, V., & Krivic, S. | Ontology-Guided Reasoning for Affordance-Based Explanations of Robot Navigation | 논문 | medium | https://arxiv.org/abs/2606.00117 |
| ref-656 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 정부·연구기관 | medium | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 |
| ref-657 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 |
| ref-658 | 이관용, 구한민, 이윤서, 정민승, 윤동근, 김갑성(지적과 국토정보 52(2), 17-34) | 로봇 친화형 건축물 인증 지표 개발: 초점집단면접(FGI)과 분석적 계층화 과정(AHP)의 활용 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002903574 |
| ref-659 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_doors.html |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | KS B 7317 이 정한 이동 로봇의 승강기 탑승 단차·틈새 기준값은 무엇이며, 국내 물류센터의 화물용 승강기와 이종 제조사 로봇에 그대로 적용되는가? | 10, 6 | 열림 | — |

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Nav2 Route Server (nav2_route) | 오픈소스 | ROS Navigation (ros-navigation/navigation2) | 15, 6 | ref-646 | https://github.com/ros-navigation/navigation2/blob/main/nav2_route/README.md |

## 추가 조사 요청

- 단계 3 페이지 q3-03·아이디어 페이지 5절: 로봇 충전 능력(충전 방식·커넥터·도킹 조건)과 충전 위치 속성을 대조하는 근거가 이번 브리프에 없어 답을 계단·문·승강기 중심으로 썼다. 충전 능력 표현(VDA 5050·Open-RMF·능력 모델)의 근거가 필요하다.
- 아이디어 페이지 5절 '다른 아이디어와의 연결': 매뉴얼 기반 로봇 기능 온톨로지 트랙 온톨로지 초안의 능력 개념(계단·도어 조작·충전, 작업 요구·제약·실행 조건) 이름과 공간 그래프 쪽 통과 조건의 대응을 확인하려면 그 초안 페이지를 입력으로 받아야 한다(q3-10 과 연결).
- 단계 3 페이지 q3-03: IFC 4.3.2 Pset_DoorCommon·Pset_StairCommon 속성 정의 원문(공식 문서)을 열어 검색 요약 기준 확인을 보강할 필요가 있다.
- 단계 3 페이지 q3-03·열린 질문: KS B 7317 의 단차·틈새 수치 기준과 로봇 친화형 건축물 인증 지표의 세부 항목(출입문 폭·단차 등)이 필요하다.
- 아이디어 페이지 5절 '다른 아이디어와의 연결': 아이디어 2(자연어 업무 지시 챗봇)가 공간 그래프를 질의해 장소를 해석하는 지점의 근거가 브리프에 없다.

## 이행한 수정 지시

- f5 파일 범위 한정 — 단계 3 페이지 3절 q3-03 에 'rmf_traffic 의 Graph.hpp 파일에 정의된 차선 속성에는 … 없다'로 쓰고 4절 불확실성에 Graph.hpp 범위 한정을 적었으며, LaneClosure.hpp 는 본문에 서술하지 않았다.
- f7 동적 엣지 서술 — 단계 3 페이지 q3-03 에 '외부 요청 값에 따라 막힌 엣지를 닫고 다시 여는 동적 엣지 채점기'로 썼고 ref-646 참고문헌 요약도 같게 고쳤다.
- f9 사실·추정 분리 — Pset_StairCommon 세 속성 문장은 [사실], '통과 난이도를 수치로 담을 수 있다'는 별도 문장 [추정]으로 나눴다.
- f11 사람 대상 명시 — q3-03 의 교통약자 IndoorGML 확장 문장에 '대상은 로봇이 아니라 사람'을 밝혔고, 로봇 판정으로 옮기는 부분은 종합(f21) [추정] 문장과 종합 표 머리 설명에서만 다뤘다.
- f19 환경 조건 — '실외'를 빼고 '점검 임무 대상, 환경 조건 미확인'으로 썼고, 단계 3 페이지·아이디어 페이지 각주 ref-654 기관 칸과 reference_updates org 를 'Morilla-Cabello, D., & Montijano, E.'로 썼다.
- ref-655 발행일 — 본문 'Halilovic 외(2026-06)', 각주 발행일, reference_updates published 를 모두 2026-06 으로 고쳤다.
- ref-658 기관 — 단계 3 페이지 각주와 reference_updates org 를 '이관용, 구한민, 이윤서, 정민승, 윤동근, 김갑성(지적과 국토정보 52(2), 17-34)'로 고쳤다.
- ref-031 열람 경로 — reference_updates 에는 fetched_via 필드가 없으므로 summary 에 '입력 원문 텍스트(inbox, data/source_texts)로 열람'을 적고 source_unopened false 로 두었다.
- 원문 미열람 표기 — 이번 실행이 쓴 각주 정의(단계 3 페이지 8절 전체 교체, 아이디어 페이지 5절, 스키마 초안 6절 추가분)의 ref-079·ref-348·ref-413·ref-419·ref-461·ref-647~ref-658 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다(ref-651 포함). 스키마 초안 7절 끝과 아이디어 페이지 3·4절에 있는 이전 실행의 ref-079·ref-413·ref-419 정의는 이번 패치 범위 밖(자동 영역 인접 절·미변경 절)이라 고치지 않았다.
- 기존 문장 재사용 — f2 의 관제 보유 통행 제한, f4 의 graph_idx 플릿별 그래프, f10 의 OBRNIT 네 개념 묶음, f23 의 기본 그래프 분리는 q3-01·q3-02 문장을 가리키고 새로 쓰지 않았으며, 도입 단계 로봇 그룹별 경로 제한·INVALID_ORDER_ACTION·플릿 설정의 문·승강기 필드 부재·OBRNIT 최대 단 높이만 덧붙였다. 4절 결론은 기존 분리 문장을 확장하는 형태로 바꿨다.
- f21 용어 — 단계 3 페이지(../../glossary/…)와 아이디어 페이지(../glossary/…)에서 '요구 능력·제공 능력'과 '능력 매칭' 용어집 항목에 링크해 같은 용어로 썼다.
- 용어 '통과 가능성' 정의 — '로봇 능력(정적 조건)으로 판정하는 통과 가능 여부이며, 문 닫힘 같은 현재 상태는 8. 실시간 세계 상태·데이터 일관성 쪽에서 따로 다룬다'로 고쳐 glossary_updates 에 냈다.
- 온톨로지 승인 변경 — 스키마 초안 2절에서 문에 자동 구동 여부(Pset_DoorCommon.HasDrive)·장애인 접근 가능(HandicapAccessible) 속성(f8), 계단에 단 높이·디딤판 길이·단 수(Pset_StairCommon) 속성(f9)을 더하고 두 행 상태 '확정'을 유지했으며, 프런트매터 ontology_version·ontology_draft_version 을 0.8 로 맞췄다. H1 의 (v0.8) 표기는 H2 절 밖이라 패치로 보낼 수 없어 diff_summary 에 코드 갱신 필요를 적었고, 상태 줄은 자동 영역이다.
- '통과 요구 조건' 미반영 — 개념 표에 넣지 않고 스키마 초안 6절 미해결 모델링 질문에 이유(정의 밖 개념, 관계 미정, 매뉴얼 트랙 개념과 중복 미확인, 근거 f11·f14 이전은 추정)와 함께 두고 q3-03 항목 근거를 f21 [추정]으로 보강했다(해결로 바꾸지 않음).
- 10. 설비·건물 시스템 연동 반영 제안 — KS B 7317 은 표준명·제정 사실만 적고 단차·틈새 수치는 '미확인', 승강기 탑승 안전 제어는 '연계 대상'으로 짧게 적는다고 area_reflection_proposals 요약에 명시했다.
- 단계 3 페이지 6절 — 능력 대조·다른 아이디어와의 연결 행을 충족으로, 시뮬레이션 초기값·실험 계획 행을 미충족으로 두고 '다음 단계로 전환: 아니오(완료 조건 미충족: 시뮬레이션 초기값, 실험 계획; 막힌 질문 q3-04·q3-05·q3-06·q3-07·q3-08·q3-09)'로 썼다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.8
- 트랙 로그 항목: 답한 질문: q3-03(공간 요소 통과 조건과 로봇 제공 능력의 요구–제공 능력 매칭, 문·승강기의 로봇 능력 또는 설비 연동 선택 조건, 로봇별 통행 가능 부분 그래프와 현재 상태 층 분리 — 결론은 추정, 근거 f1~f24) / 새 질문: q3-10(f23), q5-05(f21) / 온톨로지 변경: v0.7 → v0.8: 문 속성 '자동 구동 여부'·'장애인 접근 가능' 추가(f8), 계단 속성 '단 높이·디딤판 길이·단 수' 추가(f9), 두 행 확정 유지; 거부: 개념 '통과 요구 조건'(f8·f9·f11·f14 → 6절 미해결 모델링 질문); 근거 실행 2026-09-25-65 / 완료 조건 평가: 미충족(부족: 아이디어 3 5절 핵심 구성 요소 중 시뮬레이션 초기값, 사용자에게 제안하는 실험 계획) / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 10. 설비·건물 시스템 연동, 13. 작업 배정 — MRTA, 8. 실시간 세계 상태·데이터 일관성 5건 / 다음 실행 제안: q3-04(시뮬레이션 초기값), 이어서 q3-10
- 개요 진행 현황: 단계 3 진행 중 — 열린 질문 7, 답함 3, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-03 | 답함 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-03 | — | — | — |
| q3-10 | 열림 | — | VDA 5050 팩트시트·Open-RMF 플릿 설정에 계단·문·승강기 능력 필드가 없을 때, 로봇별 최대 단 높이·문 조작·승강기 이용 가능 여부 같은 능력 속성 값을 매뉴얼이나 현장 시험에서 어떻게 얻어 공간 그래프의 통과 요구 조건과 같은 단위로 맞추는가? (q3-03 에서 파생, 매뉴얼 기반 로봇 기능 온톨로지 트랙과 연결) | 3 | f23 |
| q5-05 | 열림 | — | 요구–제공 능력 매칭으로 만든 로봇별 통행 가능 판정이 실제 주행에서 틀리는 경우(통과 가능 판정 후 실패, 불가 판정의 과잉 제한)를 시뮬레이션·실기체 시험으로 어떻게 측정하고 임계값을 보정하는가? (q3-03 에서 파생) | 5 | f21 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 6. 대표 접근법과 기술 | 로봇 능력 속성(최대 단 높이·폭·높이·문 조작·승강기 이용)을 공간 요소의 통과 조건과 요구–제공 능력 매칭으로 대조하는 접근(추정, f21)과, VDA 5050 팩트시트·Open-RMF 플릿 설정에 계단·문·승강기 능력 필드가 없다는 사실(f1·f4, ref-644·ref-105), IDTA 02020 요구·제공 능력(f14)·이종 로봇 능력 모델(f15). |
| 6 | 6. 대표 접근법과 기술 | BIM·건물 디지털 트윈에서 로봇 스킬별 지도·경로를 만드는 연구(f12·f13), Nav2 경로 서버의 엣지 메타데이터·동적 엣지 폐쇄(f7), IFC 문·계단 속성 세트(f8·f9), 플릿 중립 공간 그래프에서 로봇별 통행 가능 부분 그래프 파생(추정, f23). |
| 10 | 6. 대표 접근법과 기술 | 문·승강기 통과를 설비 연동(Open-RMF 문 어댑터 DoorRequest·DoorState, IFC 자동 구동 문 HasDrive)으로 충족하는 방식(f6·f8), 로봇 조작과 설비 연동의 선택 조건(추정, f22). KS B 7317 은 표준명·2021-11-11 제정 사실만 [사실]로 쓰고 단차·틈새 수치는 '미확인'으로 두며, 승강기 탑승 안전 제어 자체는 '연계 대상'으로 짧게 적는다(f17). |
| 13 | 6. 대표 접근법과 기술 | 능력별 통행 가능 경로를 먼저 구해 배정 후보를 거르거나 이종 차량 경로·배정 문제에 넣는 접근(연계 대상 사례 CHORAL, 점검 임무 대상·환경 조건 미확인, f19)과 ‘3층 출하 대기장’ 배정 후보를 로봇별 통행 가능 부분 그래프로 거르는 방식(추정, f24). |
| 8 | 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) | 정적 능력 대조(6. 지도·공간·위치 모델, 5. 로봇 능력·작업 온톨로지)와 현재 상태 층(문 상태, Open-RMF LaneRequest 차선 폐쇄)을 분리해야 한다는 점(추정, f23)과 어포던스 상태로 막힌 경로를 설명하는 연구(f20). |
