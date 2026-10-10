# 스토리텔러 산출 2026-10-10-05

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md | draft | 3절 충전 값 의미·단위 구분과 호텔 연구 수치(Han 외 2025) 보강, 5절 제약 행 권고 표현 정정·상업 시설(호텔 수치 실험) 사례 추가, 6·7·8·11절 갱신 요약과 새 주제 페이지·2026-09-25 분리 페이지 링크(문단 안 문장으로 둠), 13절 각주 갱신(ref-031·ref-103 등) |
| create | docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md | draft | 신규 작성: 충전 하한 값 구분, 충전소 is_charger 지정(oq-069 해결), 승강기 메시지 범위, Open-RMF 판 기록, 공용 충전기·열화 MILP, 항만 물류–에너지 후보 자료(2차 수정: 세 줄 요약 둘째 줄 범위 조정, 연계 범위 의견 주체 명시) |
| update | docs/topics/2026/2026-09-25-area16-s6.md | draft | 3. 본문 끝에 충전소 속성 충돌 문장 정정 소제목 추가(문서 is_parking_spot·구현 is_charger 병기, 구현 기준 판단은 의견), 8. 출처에 ref-1543 정의 추가, 10. 이력에 2026-10-10 행 추가, 프런트매터 sources·last_run 갱신 |
| create | docs/topics/2026/2026-10-10-area28-s11.md | draft | 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "11. 열린 질문" 절(1,185자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area28-s3.md | draft | 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "3. 왜 중요한가" 절(770자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area28-s10.md | draft | 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(637자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area28-s7.md | draft | 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "7. 관련 표준·프레임워크·오픈소스" 절(633자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area28-s6.md | draft | 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절(607자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area28-s8.md | draft | 자동 분리: 28. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절(534자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-10 | 28. 공용 자원·충전·에너지 최적화 | 5절 제약 행을 VDA 5050 권고 표현으로 정정하고 상업 시설(호텔 수치 실험) 사례 추가, 3절 충전 값 구분·호텔 수치 보강, 충전소 is_charger 정리(oq-069 해결), 공용 충전기·승강기 메시지 확인 주제 페이지 신설, 6·7·8·11절에 기존 분리 페이지 링크 유지 | run 2026-10-10-05
- 홈 최근 업데이트: 2026-10-10 — 28. 공용 자원·충전·에너지 최적화: 충전 하한 권고 표현 정정, 충전소 is_charger 정리(oq-069 해결), 상업 시설 사례와 공용 충전기·열화 연구 추가
- 대분류 최근 업데이트: 2026-10-10 — 28. 공용 자원·충전·에너지 최적화: 5절 제약 행 정정·상업 시설 사례 추가, 6·7·8·11절 갱신과 주제 페이지 '충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가' 신설
- 세부영역 최근 업데이트: 2026-10-10 — 28. 공용 자원·충전·에너지 최적화: 3·5절 정정·보강, 6·7·8·11절에 갱신 요약과 새 주제 페이지·2026-09-25 분리 페이지 링크, 6절 분리 페이지에 충전소 속성 정정 추가

## 용어집 갱신

- 없음

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | high | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp |
| ref-1543 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp (2.14.0) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/parse_graph.cpp |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg |
| ref-103 | Han, L., Ding, J., Liu, S., & Meng, M.(Sensors 25(6) 1783, doi:10.3390/s25061783) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2603.22731 |
| ref-1544 | Song Yang, Sichen Yue, Xiao Wang, Kaiyu Wang, Xin Tian, Xiao Wang (Processes, MDPI) | A Two-Stage Logistics–Energy Coordinated Optimization Framework for AGV Scheduling and Charging Under Reefer Container Temperature Constraints | 논문 | medium | https://www.mdpi.com/2227-9717/14/15/2424 |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| update | oq-069 | 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? | 15, 28 | 해결 | docs/topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md |
| new | — | 공용 충전기 예약 시간이 끝났는데 로봇이 충전기 앞을 떠나지 못할 때 다음 예약의 시작을 어떻게 조정하는가? | 28, 27 | 열림 | — |
| new | — | 충전 상태(SOC) 추정 오차와 충전소까지의 이동·대기 에너지를 반영해 운영 하한에 더할 여유를 어떻게 검증하는가? | 28, 5 | 열림 | — |
| new | — | 배터리 열화 최적화 모델의 예시 결과를 실제 셀·충전기·장기 운용 데이터로 검증한 공개 재현 자료가 있는가? | 28, 57 | 열림 | — |
| new | — | 승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가? | 28, 22 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 상업 시설 | 시작 조건 | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시 | 28. 공용 자원·충전·에너지 최적화 |
| 상업 시설 | 작업 대상 | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시 | 28. 공용 자원·충전·에너지 최적화 |
| 상업 시설 | 수행 자원 | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시 | 28. 공용 자원·충전·에너지 최적화 |
| 상업 시설 | 제약 | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시 | 28. 공용 자원·충전·에너지 최적화 |
| 상업 시설 | 예외·성과 | docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md#5-적용-사례-현장-유형-명시 | 28. 공용 자원·충전·에너지 최적화 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 6절 분리 페이지(docs/topics/2026/2026-09-25-area16-s6.md)의 is_parking_spot/is_charger 충돌 문장 자체는 페이지 본문이 입력에 없어 교체하지 못하고 3. 본문 끝에 정정 소제목만 덧붙였다 — 다음 갱신 실행에서 이 페이지를 입력으로 넣어 해당 문장을 정정 문장으로 바꿔야 한다
- 7·8·11절 분리 페이지(2026-09-25-area16-s7·s8·s11)는 입력에 없고 하루 갱신 상한(2)도 찼으므로 고치지 않았다. 세부영역 6·7·8·11절 append 문단 안에 이 페이지들로 가는 링크 문장을 넣어 자동 재분리 뒤에도 남게 했다 — 다음 갱신에서 분리 페이지 내용에도 반영할지 정해야 한다(파이프라인 담당: 재분리 코드가 '자세한 내용은 주제 페이지' 로 시작하는 독립 문단을 버리는지 확인 요청)
- 트랙 반영 제안 4건(IDTA 02047 충전 요소 2건, IDTA 디지털 배터리 여권 1건, rmf_traffic 문·승강기·VDA 해제 구역 1건)은 이번 브리프가 다루지 않아 반영하지 않았다 — 7·6절 반영을 위해 IDTA 02047 템플릿 원문(oq-060)과 배터리 여권 템플릿 본문, rmf_traffic 문·승강기 표현 원문 조사가 필요하다
- 11절 oq-066: 물류센터 로봇의 시간대별 전기 요금·최대 수요 전력 기준 충전 계획 연구와 국내 사례(한국어 자료)가 필요하다. Yang 외(ref-1544)는 원문 미열람이라 수치를 쓸 수 없다
- 11절 oq-067: Open-RMF 승강기 감독(lift supervisor) 등 메시지 밖 구성요소의 타임아웃·대기열 구현 조사가 필요하다
- 5절: 물류창고·상업 시설 밖 현장 유형(병원·제조 공장 등)의 충전·승강기 공용 자원 사례와 상업 시설 사례의 완료·인계 항목 근거가 필요하다

## 이행한 수정 지시

- 5절 제약 행 정정 — '보내야 한다' 문장을 'VDA 5050 은 팩트시트의 임계 충전 수준(백분율, 로봇 유형별 선언값) 이하에서는 관제가 충전소로 가는 주문만 보내는 것이 좋다고 권고(should)한다(3.0.0 판 기준, 발행일 미확인)'로 바꾸고 각주를 [^ref-031][^ref-228]로 두었다(corr id 없음).
- 3절 첫 문장 — 같은 '충전 임계값'으로 묶던 괄호를 'VDA 5050 의 임계 충전 수준(관제의 주문 제한 기준, 백분율)이나 Open-RMF 의 recharge_threshold(운행 하한, 0~1 비율)'로 의미·단위를 구분해 고쳤고 태그는 [추정] 그대로 두었다.
- 3절 호텔 연구 문장 — 새 문장을 더하지 않고 기존 문장을 Han 외(2025), 고객 노드 60개·40→100초·약 225→500초로 고쳤으며 '거의 두 배'는 틀렸다는 서술 없이 뺐고, 모델 수치 실험이라는 [의견](이 위키는 본다)을 덧붙였다.
- [^ref-103] 각주 — 세부영역 13절에서 지시된 저자·Sensors 서지·doi·발행일 2025-03-13·접근일 2026-10-10 형식으로 바꾸고 '(원문 미열람)'을 뺐으며, reference_updates 의 ref-103 에도 저자·발행일을 반영했다.
- 용어 표기 — MTVRP 는 5절 상업 시설 사례에서 '다중 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)'(용어집 링크)로, MILP 는 주제 페이지 3절에서 '혼합 정수 계획(Mixed Integer Linear Programming, MILP)'으로 썼다.
- 5절 상업 시설 사례 — '현장 유형: 상업 시설'과 '다층 호텔 배송을 모델링한 수치 실험(실제 배치 아님)'을 사례 머리에 밝히고, 완료·인계와 수행 자원의 설비 쪽 분담·복구 주체는 '미확인'으로 두었으며, 물류창고 머리 문장을 상업 시설 사례 추가에 맞게 고쳤다. site_matrix_updates 는 상업 시설에 해당하는 항목만 냈고 물류창고·실외는 내지 않았다(주제 페이지 4절의 가상 창고 수치 실험도 이 지시에 따라 매트릭스에 내지 않음).
- Yang 외(ref-1544) — 5절 적용 사례에 쓰지 않고 원문 미열람 후보 자료로만 주제 페이지 3절과 세부영역 8절 요약에 [추정]·[의견]으로 두었으며, 각주 접근일 뒤에 '(원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. 항만 마이크로그리드 운영은 주제 페이지 5절 연계 범위에 연계 대상으로 짧게 적었다.
- 6절 분리 페이지 충돌 문장 — 해당 페이지 본문이 입력에 없어 원 문장을 직접 바꾸지 못했으므로, 그 페이지 '3. 본문' 끝에 '2026-10-10 정정' 소제목을 덧붙여 정정 대상 문장을 밝히고 '지원 작업 문서(ref-039)는 is_parking_spot, 현재 구현 그래프 API(ref-536)·rmf_fleet_adapter 2.14.0 파서(ref-1543)는 별도 속성·is_charger' 를 둘 다 제시한 뒤 구현 기준 판단을 [의견]으로 적었다. 같은 내용을 세부영역 6절과 주제 페이지 3절에도 실었고, 원 문장 교체는 additional_research_requests 에 올렸다. Graph.hpp 주석 복사 오류는 언급하지 않았다.
- 6·7절 분리 페이지 내용(VDA 백분율 선언과 Open-RMF 비율 설정의 단위·의미 구분, f7 우선순위 규칙 부재와 조사 범위 한정, 0.10·1.0 이 템플릿 예시값임) — 분리 페이지가 입력에 없고 하루 갱신 상한이 차서, 새 주제 페이지 3절 '충전 하한' 소제목과 세부영역 6절 요약에 넣었다.
- 7절 분리 페이지 내용(승강기 메시지 필드와 점유 시간·시간창·다중 목적층 필드 부재를 [사실], 배분 정책 부재로 넓히지 않는다는 [의견], rmf_fleet_adapter 2.12.0·2.13.0 수정 이력 [사실]과 판 기록 권고 [의견]) — 같은 이유로 주제 페이지 3절과 세부영역 7절 요약에 넣었다.
- ref-1398 — 입력의 참고문헌 색인에 같은 URL(ref-1487·ref-1513)이 아직 등록돼 있지 않아 각주·프런트매터에 ref-1398 를 쓰고 reference_updates 에 URL 을 그대로 두어 퍼블리셔가 기존 id 로 합치게 했다.
- Li 외(ref-403) — 주제 페이지 3절에 프리프린트(arXiv v1, 2026-03-24, 동료심사 미확인)를 밝히고 같은 로봇의 세션 쌍은 세션 집합이 모든 로봇의 세션을 포함하도록 정의된 데서 따라 나온다(논문이 따로 명시하지 않음)고 적었으며, 최대 54% 열화 감소는 대표 사례 하나의 예시적 기대 평균임을 같은 문장(주제 4절 예외·성과, 세부영역 8절)에 붙이고 f22 를 [의견]으로 두었다.
- [의견] 주체 명시 — f3·f6·f10·f13·f16·f22·f24·f27 의 의견 문장을 모두 '이 위키는 … 본다/쓰지 않는다' 형식으로 썼다.
- [^ref-031] — 세부영역·주제 페이지 각주 접근일을 2026-10-10 으로 갱신하고, batteryCharging·임계 충전 수준을 인용한 곳(세부영역 5·6절, 주제 3절)에 '3.0.0 판 기준(발행일 미확인)'을 밝혔다.
- 11절·열린 질문 — oq-069 를 해결(link: 새 주제 페이지)로 open_question_updates 에 내고 해결 근거를 f8·f9 와 문서(ref-039) 서술 차이로 적었으며, oq-066·oq-067·oq-068 은 세부영역 11절에 부분 근거만 적고 열림을 유지했다. 새 질문 4건은 브리프 형식대로 new 로 등록했다.
- 트랙 반영 제안 4건 — 근거 finding 이 없어 6·7절에 반영하지 않고 제안 상태로 두었으며 oq-060 도 건드리지 않았다(추가 조사 요청에 기록).
- 직접 인용 — ref-031 은 세부영역 5절의 '(should)' 한 단어만 인용하고 주제 페이지에서는 재서술했으며, ref-403·ref-103 은 원문 구절을 인용하지 않고 모두 재서술했다.
- 2차: 세부영역 6·7·8·11절 append 패치 content 마다 '2026-09-25 까지 정리한 내용은 주제 페이지 [28. 공용 자원·충전·에너지 최적화 — <절 이름>](../../topics/2026/2026-09-25-area16-s<n>.md)에 있다.' 링크 문장을 넣었다. 이전 초안에서 독립 문단으로 둔 '자세한 내용은 주제 페이지 …' 줄이 재분리 때 빠졌으므로, 링크 문장을 모두 문단 끝의 문장으로 넣어 자동 분리 뒤 새 분리 페이지(2026-10-10-area28-s6·s7·s8·s11)에도 남게 했다(8절 세 줄 요약이 가리키는 대기행렬·충전 최적화·승강기 병목 연구도 이 링크로 닿는다).
- 2차: 6·7절 append 끝에 '자세한 확인 결과는 주제 페이지 [충전 하한과 충전소 지정, 승강기 세션 점유는 무엇이 확인됐는가](../../topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md)에 있다.' 문장을 문단 안에 넣었고(8절에도 같은 문장으로 맞춤), 세부영역 diff_summary 를 '새 주제 페이지·2026-09-25 분리 페이지 링크'로 고쳤다.
- 2차: docs/topics/2026/2026-09-25-area16-s6.md — (1) '8. 출처' replace 패치의 frontmatter 로 sources 에 ref-1543 을 더하고 last_run 을 2026-10-10 으로 고쳤다. (2) [^ref-1543] 정의를 8. 출처 절 안(목록 끝)에 넣어 이력 표 뒤에 붙지 않게 했다. (3) 10. 이력 replace 패치로 '| 2026-10-10 | 2026-10-10-05 | 3. 본문 끝에 충전소 경유점 속성 정정 소제목 추가 |' 행을 기존 행 위에 더했다.
- 2차: 새 주제 페이지 1. 세 줄 요약 둘째 줄에서 별도 정책 항목을 f6 범위(운행 하한·충전 시작 판단·충전 목표)로 좁히고, 충전소 지정은 '충전소 지정은 구현 기준(is_charger)으로 확인하며' 라는 별도 구절(f10)로 썼다(이전 초안의 '기대는' 오탈자도 함께 지움).
- 2차: 새 주제 페이지 5. ROP 관점의 시사점 연계 범위의 항만 항목을 '이 위키는 항만 마이크로그리드(태양광·풍력·ESS) 운영을 ROP 직접 범위가 아닌 에너지 설비 쪽 연계 대상으로 본다. [의견][^ref-1544]' 로 고쳐 의견 주체를 밝혔다.
- 분량 초과 자동 분리: 28. 공용 자원·충전·에너지 최적화 본문 7,323자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 4,052자
