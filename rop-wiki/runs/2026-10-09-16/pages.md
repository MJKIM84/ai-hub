# 스토리텔러 산출 2026-10-09-16

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md | draft | 3절 둘째 문단을 현재 원문 질문에 맞추고 심각도·시각 형식·통신 신호·사람 개입 근거 보강, 5절 현장 유형별 사례(병원·상업 시설·실외·기타) 추가와 물류창고 사례 재확인, 7절 표준 필드 표 추가와 2026-09-25 목록 링크 유지, 9절 내부 진단·승강기·실외 인증 경계와 직접 범위 후보 추가, 11절 2026-09-25 목록 링크 유지·부분 근거·새 질문 2건, 13절 각주 접근일·기관 표기 갱신(2차 수정 3건 반영) |
| create | docs/topics/2026/2026-10-09-area38-s7.md | draft | 자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 "7. 관련 표준·프레임워크·오픈소스" 절(2,049자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area38-s3.md | draft | 자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 "3. 왜 중요한가" 절(1,297자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area38-s11.md | draft | 자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 "11. 열린 질문" 절(1,010자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area38-s10.md | draft | 자동 분리: 38. 모니터링·이상 탐지·원인 분석 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(648자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 38. 모니터링·이상 탐지·원인 분석 | 3절 심각도·시각 형식·통신 신호·사람 개입 근거 보강과 원문 질문 표현 정정, 5절 병원·상업 시설·실외·기타 사례 추가, 7절 VDA 5050·MassRobotics·Open-RMF·OpenTelemetry 필드 표, 9절 내부 진단·승강기·실외 인증 경계, 11절 부분 근거·새 질문 2건, 각주 갱신(1차 조건부 승인 수정 16건·2차 수정 3건 반영) | run 2026-10-09-16
- 홈 최근 업데이트: 2026-10-09 — 38. 모니터링·이상 탐지·원인 분석: 표준별 심각도·시각 형식·연결 상태 차이와 병원·상업 시설·실외·기타 현장 사례를 더하고 책임 경계를 보강했다
- 대분류 최근 업데이트: 2026-10-09 — 38. 모니터링·이상 탐지·원인 분석: 3·5·7·9·11절 갱신(현장 유형별 사례 4건 추가, VDA 5050·MassRobotics·Open-RMF 필드 정리, 새 열린 질문 2건)
- 세부영역 최근 업데이트: 2026-10-09 — 38. 모니터링·이상 탐지·원인 분석: 3절 원문 질문 표현 정정과 근거 보강, 5절 병원·상업 시설·실외·기타 사례, 7절 표준 필드 표, 9절 경계 보강, 11절 부분 근거·새 질문 2건, 13절 각주 접근일 갱신

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 연결 상태 | Connection State (VDA 5050 connectionState) | VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다. | 38, 20 | ref-449 |
| new | 경보 등급 | Alert Tier (Open-RMF Alert) | Open-RMF 경보 메시지가 운영자에게 보내는 경보의 심각도를 INFO·WARNING·ERROR 세 단계로 나타내는 필드다. | 38, 32 | ref-448 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_doors.html |
| ref-445 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 오픈소스 문서 | high | https://github.com/ros/diagnostics/blob/ros2/README.md |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 오픈소스 문서 | high | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 기사 | low | http://www.irobotnews.com/news/articleView.html?idxno=34601 |
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones | 기사 | low | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 정부·연구기관 | medium | https://www.kiria.org/portal/cert/portalCertEstiSafe.do |
| ref-961 | Responsible AI Collaborative (AI Incident Database) | Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks | 기사 | low | https://incidentdatabase.ai/cite/346/ |
| ref-962 | Hotel Technology News | Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce | 기사 | low | https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/ |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? (관련: oq-033, oq-073) | 38, 21 | 열림 | — |
| new | — | VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가? | 38, 42 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 시작 조건 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 물류창고 | 작업 대상 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 물류창고 | 수행 자원 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 물류창고 | 제약 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 물류창고 | 완료·인계 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 물류창고 | 예외·성과 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 병원 | 작업 대상 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 병원 | 수행 자원 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 병원 | 예외·성과 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 상업 시설 | 작업 대상 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 상업 시설 | 수행 자원 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 상업 시설 | 예외·성과 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 실외 | 제약 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 기타 | 시작 조건 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 기타 | 작업 대상 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |
| 기타 | 수행 자원 | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md#5-적용-사례-현장-유형-명시 | 38. 모니터링·이상 탐지·원인 분석 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 구로병원 논문(ref-943)의 실패 유형별 분류(복도 자율주행·통신·승강기 막힘)와 전체 성공률·분모를 원문 기준으로 재조사해 38. 모니터링·이상 탐지·원인 분석 5절 병원 사례와 oq-074에 반영
- 5절 병원·상업 시설·실외·기타 사례의 '미확인' 칸(시작 조건·제약·완료·인계 등)을 채울 근거 — 이번 브리프의 finding 이 한두 항목에만 걸려 있어 여섯 항목을 채우지 못했다
- 5절 제조 공장 현장의 이상 탐지·원인 분석 적용 사례 — 이번 브리프에 근거가 없어 '이번 조사에서 찾지 못했다'로 두었다
- 한림대학교성심병원 보도(ref-944)의 세부 분류 합계(8종 76대)와 7종 73대가 맞지 않는 점을 다른 출처로 확인 — 5절 병원 사례의 '보도 기준' 표기를 해소하기 위해
- 실외이동로봇 운행안전인증 심사 항목 수가 한국로봇산업진흥원 안내 페이지(8개)와 이전 실행 2026-10-09-15 의 기사(16개)에서 다른 점과 관제장치 항목의 세부 요건 — 5절 실외 사례와 9절 업종별 조건 행의 근거 보강 및 출처 충돌 여부 판단을 위해
- ref-031 출처 항목의 표기 불일치(summary 는 '원문 미열람.'으로 시작하나 fetched true·source_unopened false) 정리 — 참고문헌 페이지 표기를 바로잡기 위해
- 10절(분리 주제 페이지)의 '분류 개정 전 원문 8장의 교차 규칙' 표현을 원문 13장(L. AI·학습 기술 주석) 기준으로 다시 확인 — 이번 갱신 절 밖이라 고치지 않았다
- 파이프라인 담당: 자동 분리가 기존 '자세한 내용은 주제 페이지 …' 줄을 지우는 문제와, 3절 분리 뒤 세부영역 페이지 프런트매터 sources 에 본문 인용이 없는 ref-451 이 남는 문제 확인 — 2차 검증 노트의 지적

## 이행한 수정 지시

- f2 분리 — 7절 VDA 5050 state 스키마 행에서 information 배열의 시각화·디버깅 전용 규정만 [사실][^ref-051]로 쓰고, '원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다'는 별도 문장 [추정][^ref-051]으로 썼다.
- f3 각주 — 7절 VDA 5050 3.0.0 명세 행의 오류 수준 4단계와 errorDescription·errorHint(번역 포함) 문장에 [사실][^ref-031][^ref-051] 두 각주를 달았다.
- f6 분리·표현 — 7절 Open-RMF 작업 상태 행에서 상태 12값·배차 상태(failed_to_assign)·배차 오류 배열·일시정지/재개/취소/강제 종료 요청의 시각·라벨 기록까지 [사실][^ref-111]로, 지연 구분 가능성은 [추정][^ref-111]으로 쓰고 '사람 개입' 대신 '개입 요청(라벨로 출처 표시)'으로 썼다.
- f10 분리 — 9절 본문에서 ROS 2 diagnostics 의 /diagnostics·aggregator·원격 기록(InfluxDB) 설명만 [사실][^ref-445]로, 'ROP 는 결과를 원인 범주 판정의 입력으로 받는다'는 '연계 대상:' 표시와 함께 [추정][^ref-445]로 썼고 표의 연계 대상 칸도 유지했다.
- f15 표현 — 3절에서 'Open-RMF 작업 기록이 일시정지·재개 요청과 그 요청 출처 라벨을 남긴다'로 바꾸고 waitingHumanEvent 를 '사람 사건 대기'로 썼으며 [추정] 태그를 유지했다.
- f16 강등 — 5절 병원 사례를 [추정][^ref-943]으로 쓰고 '승강기 가동률 59.01% 미만 구간의 성공률은 95.52%였고 실패는 승강기 가동률이 높은 구간에 몰렸다'로 고쳤으며 '90% 초과' 표현을 쓰지 않았다. 설비(승강기) 혼잡 원인은 해석이라고 밝히고, 승강기 운행 제어는 연계 대상이며 ROP 몫은 승강기 상태를 원인 범주에 반영하는 데까지라고 5절 서술과 9절 표에 썼다.
- f17 한정 — 5절 병원 사례에서 '7종 73대'를 '보도 기준'으로 쓰고 '이 보도에는 이상 탐지·원인 분석 방식이나 원인별 장애 통계가 나오지 않는다'로 한정했다.
- f18 표현 — 5절 기타 사례의 시설을 '노르웨이 Northern Lights 시설'로 쓰고, 계기 판독·가스(누출) 탐지는 로봇 인식 기능인 연계 대상으로 짧게 두었으며 ROP 쪽은 점검 결과를 설비 이상 판정의 입력으로 받는 부분만 [추정]으로 서술했다.
- f19 분리 — 5절 실외 사례에서 '운행안전인증은 로봇과 관제장치의 조합을 대상으로 한다'만 [사실][^ref-980]로, '관제장치의 감시 기능이 운행 조건의 하나가 된다'는 [추정][^ref-980]으로 쓰고 인증 판단은 인증 기관·운영자 쪽 연계 대상이라고 5절 서술과 9절 표에 밝혔다.
- f20 표현 — 5절 상업 시설 사례에서 '사람 개입 없이는 처리하지 못해 사람의 일을 늘렸고', 철수 규모를 '로봇 일부(보도 기준 절반가량)'로 쓰고 기준일 2019-01 보도를 유지했다.
- f21 제외 — 본문에 쓰지 않고 additional_research_requests 에 구로병원 논문의 실패 유형별 분류와 전체 성공률·분모 재조사 요청을 넣었다.
- 5절 현장 유형별 분리 — 병원(f16·f17)·상업 시설(f20)·실외(f19)·기타(f18) 사례를 현장 유형마다 나누고 finding 이 없는 칸은 '미확인'으로 두었으며, site_matrix_updates 에는 실제로 채운 칸만 넣었다. 제조 공장은 이번 조사에서 찾지 못했다고 두었다.
- 3절 원문 질문 표현 — 둘째 문단을 '지연의 원인이 로봇인지 설비인지 통신인지 앞 작업인지'로 고쳐 [분류원문] 태그 없이 풀어 썼다.
- 열린 질문 1번 — 질문 끝에 '(관련: oq-033, oq-073)'를 붙여 open_question_updates 와 11절에 등록했고, 관련 영역 38·21 과 종류 일반(접두어 없음)을 유지했다.
- 각주 접근일·표기 — ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447·ref-031 의 접근일을 2026-10-09 로 갱신하고, ref-111·ref-283·ref-230·ref-313 의 기관·제목을 참고문헌 색인 줄과 같게 고쳤다.
- 원문 미열람 표시 — ref-943·ref-944·ref-995·ref-980·ref-961·ref-962 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- 2차: 7절·11절 기존 목록 링크 복원 — 7절 replace 본문의 첫 문단 뒤에 '2026-09-25에 정리한 표준·오픈소스 목록은 [38. 모니터링·이상 탐지·원인 분석 — 관련 표준·프레임워크·오픈소스(2026-09-25)](../../topics/2026/2026-09-25-area19-s7.md)에 있다.'를, 11절 append 본문의 '### 2026-10-09 갱신' 소제목 앞에 '2026-09-25에 정리한 열린 질문은 [38. 모니터링·이상 탐지·원인 분석 — 열린 질문(2026-09-25)](../../topics/2026/2026-09-25-area19-s11.md)에 있다.'를 지시된 형식 그대로 넣었다.
- 2차: 5절 병원 사례 표 정리 — 수행 자원 칸에서 한림대학교성심병원 문장을 빼고 의약품 배송 로봇의 승강기 호출·탑승 문장과 승강기 운행 제어 연계 대상 문장만 남겼으며, 한림대학교성심병원 문장('다른 병원 사례로, … [사실][^ref-944]')은 표 아래 '한림대학교성심병원 보도에는 …' 문장 앞에 별도 언급으로 옮겼다. site_matrix_updates 의 병원 3칸은 그대로 두었다.
- 2차: 5절 문체 — 도입 문단 끝과 '### 제조 공장' 아래의 '찾지 못함.'을 '…이번 조사에서 찾지 못했다.'로 고쳤고 표 칸의 '미확인'은 그대로 두었다.
- 분량 초과 자동 분리: 38. 모니터링·이상 탐지·원인 분석 본문 9,770자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 5,370자
