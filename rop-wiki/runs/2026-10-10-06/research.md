# 리서치 브리프 2026-10-10-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-10-06 |
| 날짜 | 2026-10-10 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 20. 로봇·제조사 관제 연동 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — IO-AMRs 과제 문장(ref-258)이 원문 미열람이고 주관 기관·과제 단계(계획인지 완료인지)가 없음
- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 출하 시나리오 하나뿐이고 '수행 자원' 행이 추정이며 직접 제어·위임 비교 자료 없음(oq-031). 연동 위치와 제어 수준을 나눠 보는 기준, 상업 시설·전시 시연 사례 없음
- 섹션 6. 대표 접근법과 기술 — 연결 단절 시 실행 의미와 상태 분리, 신호등 수준 연동의 정지 시간 전제·교착 시 사람 개입(oq-032), 상태·오류 변환의 실제 필드 매핑 사례(oq-033) 근거가 약함
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 3.0.0 발행일 미확인(oq-005), 공개 구현(free_fleet·ros_amr_interop·vda-5050-lib.js)의 판별 지원 범위와 Open-RMF 구역 기능의 개발 상태 미반영
- 섹션 8. 대표 연구와 자료 — Lopes 외 논문(ref-136) 저자 미확인·120 ms 지표 명칭과 측정 조건 미확인, Franke 외(ref-1429) 원문 미열람·워크숍 구성 미기재
- 섹션 10. 다른 연구영역과의 연결 — 21. 상호운용 표준·적합성(ISO 21423 단계), 47. AI·학습·적응과 모델 운영(MCP 연동)과의 연결 없음
- 섹션 11. 열린 질문 — oq-005·oq-031·oq-032·oq-033 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
2. oq-005 VDA 5050 3.0.0 의 발행일은 공식 자료에서 무엇으로 표시되는가? (섹션 7·11 겨냥)
3. oq-032 제조사 관제가 일시정지·재개만 허용하는 신호등 수준 연동에서 정지·교착 처리의 전제는 무엇인가? (섹션 6·11 겨냥)
4. oq-033 공개 구현은 로봇 상태·오류를 표준 필드로 어떻게 옮기는가? (섹션 6·11 겨냥)
5. oq-031 직접 제어와 제조사 관제 위임을 고르는 기준이나 비교 자료가 있는가? (섹션 5·11 겨냥)
6. 기존 8절·3절 연구 자료(Lopes 외, Franke 외, IO-AMRs)의 서지·측정 조건·단계는 원문에서 무엇으로 확인되는가? (섹션 3·8 겨냥)
7. VDA 5050·Open-RMF 공개 구현의 판별 지원 범위와 개발 중 기능은 무엇인가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 보도자료 'Version 3.0 of VDA 5050 released'의 본문 날짜는 2026-04-20(Berlin, April 20, 2026)이며, 보도자료 URL 은 260421 계열이다. | ref-032 | 아니오 | medium | 2026-10-10 | — | — |
| f2 | [사실] | VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목은 날짜를 2026-03-17(March 17, 2026)로 표시한다. | ref-1423 | 아니오 | medium | 2026-10-10 | — | — |
| f3 | [사실] | VDA 가 배포하는 VDA 5050 3.0.0 공식 PDF 의 표지는 판 표기를 'Version 3.0.0, March 2026'으로 적어 월 단위(2026-03)까지만 밝힌다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f4 | [사실] | VDA 의 공식 자료 세 가지가 VDA 5050 3.0.0 의 날짜를 서로 다르게 표시한다: 카탈로그 2026-03-17, 보도자료 본문 2026-04-20, 명세 표지 2026-03. | ref-1423, ref-032, ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f5 | [의견] | VDA 5050 3.0.0 의 발행일은 하나로 확정하지 않고 서지에는 판 표기의 월(2026-03)을 적으며, 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)는 주석으로 함께 남기는 것이 맞아 보인다(oq-005 부분 답변). | ref-031, ref-032, ref-1423 | 아니오 | low | 2026-10-10 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 §4.1 은 로봇이 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다고 정한다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 주문에 딸린 동작·즉시 동작·구역 동작의 상태를 상태 메시지의 actionStates·instantActionStates·zoneActionStates 세 배열로 나눠 보고하게 하며, 구역 동작의 예정 상태 보고는 선택 사항이다. | ref-031 | 아니오 | medium | 2026-10-10 | — | — |
| f8 | [의견] | 로봇이 단절 중에도 해제된 노드까지 주행을 이어 가므로(f6) ROP 어댑터는 연결 단절(connection 상태)을 곧 정지로 해석하지 말고, 연결 상태와 동작 실패(동작 상태 배열의 FAILED)를 별도 상태로 보존해 단절 시 실행 의미와 상태를 분리하는 것이 좋아 보인다. | ref-031 | 아니오 | low | 2026-10-10 | — | — |
| f9 | [사실] | Open-RMF EasyTrafficLight API(rmf_fleet_adapter 2.14.0)의 moving_from() 경고는 로봇이 다음 체크포인트에서 멈출 시간이 있을 때만, 곧 정지 명령의 통신 지연과 로봇 최대 감속을 감안해 호출하라고 하며, 이를 어기면 MovingError·WaitingError 가 나고 교통 흐름이 끊기거나 교착될 수 있다고 적는다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f10 | [사실] | 같은 헤더의 Blocker 설명은 해결할 수 없는 충돌로 교착이 생기면 RMF 교통 협상 시스템이 충돌 참여자를 충분히 제어하지 못하므로 사람 개입이 필요할 수 있다고 적는다. | ref-1424 | 아니오 | medium | 2026-10-10 | — | — |
| f11 | [의견] | 신호등 수준으로 붙는 제조사 플릿의 연동 계약에는 정지 명령의 유무만이 아니라 정지 가능 시간(통신 지연·최대 감속)과 정지 확인 응답, 교착 시 사람 개입 경로를 함께 적는 것이 좋아 보이며, 제어 수준별 교통 성능을 같은 조건에서 비교한 자료는 여전히 찾지 못했다(oq-032 부분 근거). | ref-1424 | 아니오 | low | 2026-10-10 | — | — |
| f12 | [의견] | 신호등 연동을 평가·재현할 때는 쓰는 rmf_fleet_adapter 패키지 판을 함께 기록하는 것이 좋아 보인다. 2.14.0(2026-09-26) 변경 이력에 EasyTrafficLight 의 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 들어 있기 때문이다. | ref-1398 | 아니오 | low | 2026-10-10 | — | — |
| f13 | [추정] | InOrbit 개발자 문서는 InOrbit 이 제어하는 로봇 플릿을 RMF core 에 잇는 오픈소스 전체 제어(full control) 플릿 어댑터를 제공해 여러 제조사 로봇의 중앙 교통 조정을 가능하게 한다고 밝힌다. | ref-1029 | 아니오 | low | 2026-10-10 | — | 벤더 주장 |
| f14 | [의견] | 연동 위치(제조사 관제 API 를 거치는지, 로봇에 직접 붙는지)와 제어 수준(전체 제어인지)은 따로 판단해 별도 항목으로 기록하고, 제어 권한은 경로 지정·교체, 정지, 진행 상태 반환으로 나눠 적는 것이 좋아 보인다(oq-031 판단 기준 보강). | ref-251, ref-1029 | 아니오 | low | 2026-10-10 | — | — |
| f15 | [사실] | Lopes 외(Applied Sciences 2025, 15(13), 7235, 2025-06-27) 논문은 본문 §6.2 에서 로봇 상태의 평균 갱신 간격(average update interval)을 약 120 ms, 사용자 화면 지연을 1초 미만으로 보고하며, 초록은 같은 값을 'average latency'로 표현한다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f16 | [사실] | 같은 논문은 실험 시험 중 AMR·AGV 를 포함해 최대 20대를 화면·서버 성능의 큰 저하 없이 동시에 감시할 수 있었고 시험 기간 서버 가동률이 99.5% 이상이었다고 보고한다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f17 | [사실] | 같은 논문의 §5.3(로봇 지도 작성·연결) 시험은 코임브라 공학연구소 기계공학과의 약 500 m² 실험실에서 수행됐으며, 120 ms·20대 결과를 어디서 측정했는지는 논문에 명시돼 있지 않다. | ref-136 | 아니오 | medium | 2026-10-10 | — | — |
| f18 | [의견] | Lopes 외의 결과는 자동차 공장 적용을 목표로 한 실험실 연구의 감시 성능이므로, 자동차 공장의 장기 운영 지연이나 20대 동시 주행 제어 성능으로 인용하지 않고, 기존 '작업 상태 갱신 평균 지연 120 ms' 표현은 '로봇 상태 평균 갱신 간격 약 120 ms'로 고치는 것이 맞아 보인다. | ref-136 | 아니오 | low | 2026-10-10 | — | — |
| f19 | [사실] | Franke 외(Logistics Journal: Proceedings No.19, 2023-10-11) 연구는 2023년 봄 소프트웨어 기업 2곳·하드웨어 제조사 3곳·창고 사용자 1곳 등 여섯 회사가 참여한 워크숍으로 VDA 5050 개념에 기반한 새 표준 인터페이스 요구를 수집했다. | ref-1429 | 아니오 | medium | 2026-10-10 | — | — |
| f20 | [의견] | Franke 외 연구는 연동 요구 분석 자료로 분류하고, 실물 플릿을 비교한 실험이 아니므로 직접 제어와 제조사 관제 위임의 처리량 비교 근거로 쓰지 않는 것이 맞아 보인다. | ref-1429 | 아니오 | low | 2026-10-10 | — | — |
| f21 | [사실] | ARM Institute 의 IO-AMRs 과제 소개는 주관 기관을 Siemens Technology 로, 협력 기관을 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 로 적는다. | ref-258 | 아니오 | medium | 2026-10-10 | — | — |
| f22 | [사실] | IO-AMRs 과제 소개는 다중 지도 관리자·연결 계층·전역 플릿 관리자를 이전 ARM 지원 과제의 산출물을 활용해 만들 '계획'으로 서술해, 이 과제가 소개 시점에 계획 단계였음을 보여 준다. | ref-258 | 아니오 | medium | 2026-10-10 | — | — |
| f23 | [의견] | IO-AMRs 소개는 과제 목표의 근거로만 쓰고 달성한 운영 성과의 근거로 쓰지 않으며, 3절의 목표 문장에는 주관 기관과 계획 단계라는 범위만 보태는 것이 맞아 보인다. | ref-258 | 아니오 | low | 2026-10-10 | — | — |
| f24 | [추정] | Open-RMF rmf_ros2 PR #516 'Add GoToZone feature'는 구역 이름을 받아 구역 안 경유점을 예약하는 기능을 제안하며 2026-10-10 기준 미병합 상태인 것으로 보이나, 이번 환경에서 PR 원문과 상태를 직접 확인하지 못했다. | ref-1425 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f25 | [사실] | Open Robotics Discourse 의 2026-05-04 Interop SIG 공지는 CHART 가 RMF-2.0 프로젝트로 개발한 새 기능을 단계적으로 공개하며 첫 단계가 시설 '구역(zones)' 관리 기능이고, 공지 시점에 이 기능이 검토 중(currently undergoing review)이라고 밝힌다. | ref-1426 | 아니오 | medium | 2026-10-10 | — | — |
| f26 | [의견] | 어댑터 기능 목록을 정리할 때는 배포판(태그)에 든 기능과 검토 중인 기능(예: Open-RMF 구역 기능)을 구분해 적는 것이 좋아 보인다. | ref-1426, ref-1425 | 아니오 | low | 2026-10-10 | — | — |
| f27 | [사실] | ros_amr_interop 1.1.1 의 MassRobotics 송신 예제 설정은 ROS 토픽 /we_b_robots/mode(std_msgs/String)를 operationalState 에, /troubleshooting/errorcodes 를 errorCodes 에 연결하고, 오류 코드는 쉼표로 구분한 문자열로 받아 MassRobotics 표준이 요구하는 배열로 바꾼다고 주석에 적는다. | ref-255 | 아니오 | medium | 2026-10-10 | — | — |
| f28 | [사실] | MassRobotics AMR 상호운용 표준 1.0 태그의 JSON 스키마는 상태 보고(statusReport)의 필수 필드를 uuid·timestamp·operationalState·location 넷으로 둔다. | ref-230 | 아니오 | medium | 2026-10-10 | — | — |
| f29 | [의견] | ros_amr_interop 예제는 ROS→MassRobotics 한 방향의 운용 상태·오류 매핑 사례일 뿐이므로 Open-RMF·VDA 5050·MassRobotics 세 체계의 공통 상태·오류 어휘 표준으로 일반화하지 않는 것이 맞아 보이며, 세 체계를 함께 다루는 표준 매핑은 이번에도 확인하지 못했다(oq-033 부분 근거). | ref-255, ref-230 | 아니오 | low | 2026-10-10 | — | — |
| f30 | [사실] | free_fleet 1.3.0 태그의 README 는 메시지를 CycloneDDS 의 dds_idlc 로 FleetMessages.idl 에서 생성한다고 설명하고, ROS 1·ROS 2 양쪽의 cyclonedds 판을 같게 맞춰야 한다고 권고하며, DDS 를 쓰지 않는 새 판을 준비 중이라고 적는다. | ref-256 | 아니오 | medium | 2026-10-10 | — | — |
| f31 | [의견] | 위키의 free_fleet 설명(현재 기본 브랜치의 zenoh 기반 Nav2·Nav1 어댑터)과 과거 태그 1.3.0 의 CycloneDDS 기반 설치 절차는 섞지 않고 판을 밝혀 적는 것이 좋아 보인다. | ref-256 | 아니오 | low | 2026-10-10 | — | — |
| f32 | [사실] | vda-5050-lib.js 의 v1.7.0(2026-04-29) 변경 이력은 VDA 5050 3.0 지원을 추가하며 새 Topic.ZoneSet·Topic.Responses 토픽, VdaVersion 의 '3.0.0', 3.0 용 사전 컴파일 검증기와 타입을 넣었다고 적는다. | ref-742 | 아니오 | medium | 2026-10-10 | — | — |
| f33 | [의견] | 어댑터에 VDA 5050 라이브러리를 쓸 때는 라이브러리 판과 지원 규격 판을 함께 고정하는 것이 좋아 보이며, 라이브러리가 선언한 3.0 지원은 제조사 로봇과의 적합성·실물 호환성 검증으로 세지 않는 것이 맞아 보인다. | ref-742 | 아니오 | low | 2026-10-10 | — | — |
| f34 | [추정] | InOrbit 은 Automate 2026 시연에서 Ati Robotics·Kärcher·Neura Robotics·Omron·Peer Robotics·Quasi Robotics·Unitree 7개사 로봇이 공유 공간에서 함께 임무를 수행하고, Slamcore·Guide Robotics 의 실시간 위치 추적(RTLS)으로 수동 차량까지 묶어 InOrbit 을 포함해 10개사가 협업했다고 밝힌다. | ref-1427 | 아니오 | low | 2026-10-10 | 기타 | 벤더 주장 |
| f35 | [의견] | Automate 2026 시연의 '10개사'는 참여 기업 수(로봇 7·위치 추적 2·InOrbit 1)이지 로봇 대수나 AMR 제조사 수가 아니므로, 상용 운영 사례가 아닌 전시 시연으로 분류하는 것이 맞아 보인다. | ref-1427 | 아니오 | low | 2026-10-10 | 기타 | — |
| f36 | [추정] | 카카오모빌리티는 2024년 로보티즈와 업무협약을 맺고 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용해 왔다고 발표했다(2026-03-16). | ref-1428, ref-1200 | 아니오 | low | 2026-10-10 | 상업 시설 | 벤더 주장 |
| f37 | [의견] | 카카오모빌리티–로보티즈 호텔 사례는 국내 플랫폼–로봇 제조사 연동 사례로 분류하되, 제어 위임 방식·API·로봇 대수가 공개되지 않아 한 현장에서 여러 제조사 플릿을 함께 운영한 증거나 직접 제어·위임 비교 근거(oq-031)로는 쓰지 않는 것이 맞아 보인다. | ref-1428, ref-1200 | 아니오 | low | 2026-10-10 | 상업 시설 | — |
| f38 | [추정] | 연계 대상: ISO 21423(산업용 이동로봇 통신·상호운용) 공식 카탈로그가 2026-10-10 기준 '60.00 Under publication' 단계를 표시한다는 외부 메모의 기록이 있으나, iso.org 가 403 으로 막혀 이번에 직접 확인하지 못했다. | ref-159 | 아니오 | low | 2026-10-10 | — | 원문 미열람 |
| f39 | [사실] | Open Robotics Discourse 의 Interop SIG 2026-07-02 세션 공지는 Open-RMF REST API 를 언어 모델이 호출할 수 있는 MCP 도구로 노출하는 서버와, 영어 명령을 다단계 RMF 임무로 바꿔 NVIDIA Isaac Sim 창고의 로봇이 Nav2 로 실행하는 에이전트(Nayantra)를 발표한다고 알린다. | ref-854 | 아니오 | medium | 2026-10-10 | — | — |
| f40 | [의견] | MCP 로 Open-RMF REST API 를 노출하는 시연은 47. AI·학습·적응과 모델 운영(및 12. 채팅으로 업무 지시·오케스트레이션)과의 연결 지점으로 제안할 만하나, 시뮬레이션 창고 시연이므로 실물 다사업자 플릿의 안정성 근거로 쓰지 않는 것이 맞아 보인다. | ref-854 | 아니오 | low | 2026-10-10 | — | — |

### 근거 발췌

- **f1**: 보도자료 제목 아래 "Berlin" · "April 20, 2026". URL 경로 260421_PM_VDA_5050_EN 의 숫자를 본문 날짜로 대체하지 않음. oq-005 관련
- **f2**: 카탈로그 제목 'VDA 5050' 아래 "March 17, 2026", VDA-Recommendations PDF 3,38 MB, 'VDA 5050 Version 3.0.0 Mobile Robot Communication Interface'. 카탈로그 표시일이 문서 발행일인지는 페이지에 설명 없음
- **f3**: 공식 PDF(https://www.vda.de/dam/jcr%3A09f03b91-13e2-4db3-bf30-4f221710071b/VDA5050-V3.0.0-2025-03.pdf) 표지 "Version 3.0.0, March 2026". 파일 이름의 2025 는 발행연도로 쓰지 않음. ref-031 과 같은 명세의 PDF 판
- **f4**: f1·f2·f3 의 원문 표시를 나란히 둔 것. 세 자료 모두 VDA 계열이라 독립 교차 확인이 아니다. 일자 차이의 원인(업무 단계)은 어느 자료에도 설명이 없다
- **f5**: f4 에서 도출. 저장소 릴리스 설명에 있다는 2026-03-19 와 게시 시각은 이번 환경에서 원문을 확인하지 못해 근거로 쓰지 않음
- **f6**: §4.1 Connection handling, security and QoS: "it keeps all the order information and fulfills the order up to the last released node". 대분류 F 개요(42↔32 연결)에 같은 번역어 '마지막으로 해제된 노드'로 이미 있음
- **f7**: §6.6.9 Action states, §7.8 state 메시지 표. actionStates 는 새 주문 수락 시 비우고, instantActionStates·zoneActionStates 는 clearInstantActions·clearZoneActions 실행 때까지 유지(목록이 길면 *_STATES_FULL 오류 가능). 구역 동작 지원 시 zoneActionStates 필수
- **f8**: f6·f7 에서 도출한 설계 판단. 단절 뒤 복구 절차는 32. 예외 복구·재계획·업무 연속성 연결로 한정. 명세 3.0.0 범위
- **f9**: EasyTrafficLight.hpp \warning: "accounting for the network latency of sending out the stop command and the maximum deceleration of the robot". API 계약의 전제이며 실험 수치가 아님
- **f10**: deadlock_callback 에 넘기는 Blocker 클래스 주석: "Human intervention may be required at this point, because the RMF traffic negotiation system does not have a high enough level of control"
- **f11**: f9·f10 에서 도출. 단일 프로젝트 API 문서 근거이며 제한 제어가 모든 교착을 해결한다는 보장으로 넓히지 않음
- **f12**: CHANGELOG 2.14.0: "Fix EasyTrafficLight publish fleet state"(#525), "Fix cumulative delay calculation in EasyTrafficLight"(#524). 이 수정 사실은 27. 다중 로봇 경로·교통 관리 — MAPF 주제 페이지에 이미 있어 영역 20 에는 평가 관점만 더함. 수정 이력은 성능 향상을 증명하지 않음
- **f13**: 벤더 주장: Open-RMF 절 "InOrbit provides an open source full control fleet adapter for RMF". 제조사 관제 API 경유 전체 제어 조건은 5절 '제약' 행(ref-251)에 이미 있어 보강 근거로만 씀 (발행일 미확인, 확인일 기준)
- **f14**: Open-RMF 책은 전체 제어 조건을 '제조사 관제가 명시 경로를 지정·중단·교체할 수 있고 위치를 갱신'으로 둠("fleet manager allows us to specify explicit paths"). InOrbit 문서는 관제 플랫폼 경유 전체 제어 어댑터를 밝힘. 국내 물류센터 비중·비용·처리량 비교는 미확인
- **f15**: p.21 §6.2 "The average update interval for the robot status was approximately 120 ms". p.1 초록 "average latency of 120 ms". 측정 지점·타임스탬프 정의는 논문에 없음
- **f16**: p.21 §6.2 "simultaneously monitor up to 20 robots, including AMRs ... and AGVs". 20대의 기종 구성·시험 기간·표본 수는 밝히지 않음. 감시·감독 중심 결과이며 주행 제어 성능이 아님
- **f17**: p.12 §5.3 Mapping and Interconnection of Robots: "within a laboratory covering an area of approximately 500 m2", 시제품이 설치될 공장 조건을 대략 모사. 기존 위키의 ref-136 저자 '미확인'은 17명 저자로 정정
- **f18**: f15~f17 에서 도출. 단일 연구팀 결과이며 독립 재현 미확인
- **f19**: p.5 §3.1: "two software enterprises, three hardware manufacturers and one end-user from warehousing", "six participating", "in spring 2023". DOI 10.2195/lj_proc_franke_en_202310_01
- **f20**: f19 에서 도출. 워크숍 기반 요구 수집 연구. 기존 8절의 '주변 설비 인터페이스 미포함' 문장은 반복하지 않음
- **f21**: Participants: "Lead: Siemens Technology", "Partners: FedEx, Yaskawa Motoman, Waypoint Robotics, University of Memphis" (발행일 미확인, 확인일 기준)
- **f22**: Technical Approach: "will leverage outputs from a prior ARM-funded project to create a muti-map manager[원문 철자], connectivity layer, and global fleet manager". 운영자 면담으로 인력·기술 전환 계획도 만든다고 함. 완료일·공개 코드·실물 결과는 페이지에 없음 (발행일 미확인, 확인일 기준)
- **f23**: f21·f22 에서 도출. 과제 발주 기관의 1차 자료이나 독립 성능 평가가 아님
- **f24**: 외부 조사 메모의 PR 설명('zone booking system')·상태 Open·merged_at null 기록에 의존. GitHub API 접근이 막혀 대조 실패
- **f25**: 공지(2026-05-04 게시, 확인일 2026-10-10): "this new zone feature which is currently undergoing review". 발표 예시로 환자 중심 목적지 선택과 승강기 공유를 듦. 2026-07-08 녹화 링크 게시. 병합 여부는 이 공지로 알 수 없음
- **f26**: f24·f25 에서 도출. CHART 의 하드웨어 시험 주장을 업스트림 배포판 검증으로 바꾸지 않음
- **f27**: massrobotics_amr_sender_py/params/sample_config.yaml(태그 1.1.1): operationalState.valueFrom.rosTopic, errorCodes.valueFrom.rosTopic, 주석 "Error codes are expected to be comma-separated strings" (발행일 미확인, 확인일 기준)
- **f28**: AMR_Interop_Standard.json(태그 1.0) statusReport.required = [uuid, timestamp, operationalState, location]. errorCodes 는 필수가 아님 (발행일 미확인, 확인일 기준)
- **f29**: f27·f28 에서 도출. 1.1.1·1.0 은 고정된 과거 태그이며 최신 지원 범위를 뜻하지 않음
- **f30**: README(태그 1.3.0) Message Generation: "dds_idlc from CycloneDDS". Prerequisites: "the version of cyclonedds used/built should be the same". 태그 커밋일은 확인하지 못해 발행일 미확인 (발행일 미확인, 확인일 기준)
- **f31**: f30 과 기존 7절(ref-256 기본 브랜치 README, zenoh) 비교에서 도출. zenoh 판에 대응하는 배포 태그는 확인하지 못함
- **f32**: CHANGELOG.md 1.7.0 (2026-04-29) 'VDA5050 V3.0 Support': "new Topic.ZoneSet and Topic.Responses topics, extended VdaVersion type with \"3.0.0\", V3.0 pre-compiled validators"
- **f33**: f32 에서 도출. 규격 원문과 별개 프로젝트의 구현 이력
- **f34**: 벤더 주장: "Robots from Ati Robotics, Kärcher, Neura Robotics, Omron, Peer Robotics, Quasi Robotics, and Unitree ... execute complex missions together", "ten companies in total, including InOrbit.AI". 현장 유형은 전시 시연 (발행일 미확인, 확인일 기준)
- **f35**: f34 에서 도출. 로봇 대수·성능·가동률·실패 기록은 페이지에 없음
- **f36**: 벤더 주장: 보도자료 "신라스테이 서초, 반얀트리 클럽 앤 스파 서울 등 프리미엄 호텔에서 상용 로봇 배송 서비스를 적용". 아시아경제 기사(ref-1200)는 보도자료를 옮긴 것이라 독립 확인 아님. 2. 사용 사례·요구·책임 범위에 같은 사례 있음
- **f37**: f36 에서 도출. 가동률 8배·배송 성공률 100% 는 분모·기간 미확인이라 새로 넣지 않음. 다수 제조사 협력은 사업 계획으로만 언급됨
- **f38**: 외부 조사 메모 기록에 의존(카탈로그 Life cycle 60.00). 규격 본문 미열람. 공통 좌표계 등 내용은 oq-027(21. 상호운용 표준·적합성)에서 다룸
- **f39**: 2026-06-25 공지: "an MCP server that exposes the Open-RMF REST API as LLM-callable tools", "executed by a robot in an NVIDIA Isaac Sim warehouse". 영상 전체·실물 대수는 확인하지 않음
- **f40**: f39 에서 도출. 승인 관문 위치는 기존 oq-141 이 다룸. 코드 태그·실패 처리 시험은 확인하지 않음

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-10 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04-20 | 표준 | medium | 2026-10-10 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-1423 | VDA(Verband der Automobilindustrie) | VDA 5050 | 2026-03-17 | 표준 | medium | 2026-10-10 | https://www.vda.de/en/news/publications/publication/vda-5050 | 아니오 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 아니오 |
| ref-1029 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | 벤더 문서 | medium | 2026-10-10 | https://developer.inorbit.ai/docs | 아니오 |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp | 아니오 |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 2026-09-26 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-136 | Lopes, D., Pereira, T., Gonçalves, A. 외 17명 (Polytechnic University of Coimbra 등; Applied Sciences, MDPI) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025-06-27 | 논문 | medium | 2026-10-10 | https://www.mdpi.com/2076-3417/15/13/7235 | 아니오 |
| ref-1429 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 2023-10-11 | 논문 | medium | 2026-10-10 | https://proc.logistics-journal.de/article/download/1067/1036/8465 | 아니오 |
| ref-258 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 미확인 | 정부·연구기관 | medium | 2026-10-10 | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ | 아니오 |
| ref-1425 | chart-singapore / CHART (open-rmf/rmf_ros2 GitHub) | Add GoToZone feature (rmf_ros2 pull request #516) | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/open-rmf/rmf_ros2/pull/516 | 예 |
| ref-1426 | Open Robotics Discourse (OSRA Interop SIG) | Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature | 2026-05-04 | 오픈소스 문서 | medium | 2026-10-10 | https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490 | 아니오 |
| ref-255 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/inorbit-ai/ros_amr_interop | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-10 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | 오픈소스 문서 | high | 2026-10-10 | https://github.com/open-rmf/free_fleet | 아니오 |
| ref-742 | coatyio (vda-5050-lib.js GitHub) | vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-10 | https://github.com/coatyio/vda-5050-lib.js | 아니오 |
| ref-1427 | InOrbit.AI | 10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026 | 미확인 | 벤더 문서 | low | 2026-10-10 | https://www.inorbit.ai/automate-2026 | 아니오 |
| ref-1428 | 카카오모빌리티 | 카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속 | 2026-03-16 | 벤더 문서 | low | 2026-10-10 | https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361 | 아니오 |
| ref-1200 | 아시아경제 | 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인) | 2026-03-16 | 기사 | low | 2026-10-10 | https://view.asiae.co.kr/article/2026031610244491183 | 아니오 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-10-10 | https://www.iso.org/standard/86749.html | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-10 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문. 이번에는 3.0.0 태그판의 §4.1(단절 시 마지막으로 해제된 노드까지 수행)·§6.6.9·§7.8(세 동작 상태 배열)을 대조했고, VDA 공식 PDF 표지의 판 표기 'Version 3.0.0, March 2026'을 확인했다.
- **ref-032**: VDA 5050 3.0 판 공개를 알리는 VDA 보도자료. 본문 날짜는 'Berlin, April 20, 2026'이다(URL 은 260421 계열).
- **ref-1423**: VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0(Interface for the Communication between Mobile Robots and a Fleet Control) 항목. 표시 날짜는 2026-03-17이며 PDF(3.38 MB) 내려받기를 제공한다. 발행일은 카탈로그 표시일 기준이다.
- **ref-251**: Open-RMF 책의 플릿 통합 장. 전체 제어·신호등·읽기 전용 수준과, 전체 제어에 필요한 조건(제조사 관제가 명시 경로를 지정·중단·교체)을 설명한다.
- **ref-1029**: 로봇 운영 플랫폼의 API·SDK·커넥터를 설명하는 개발자 문서. 이번에는 Open-RMF 절의 오픈소스 전체 제어 플릿 어댑터 언급을 확인했다.
- **ref-1424**: Open-RMF 신호등 수준 연동 API 헤더(2.14.0 태그). moving_from() 호출 전제(정지 시간·통신 지연·최대 감속)와 교착 시 사람 개입 가능성(Blocker)을 적는다. 발행일은 2.14.0 패키지판 날짜다.
- **ref-1398**: rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그). 2.14.0(2026-09-26)에 EasyTrafficLight 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 기록돼 있다.
- **ref-136**: Applied Sciences 15(13) 7235, DOI 10.3390/app15137235. 자동차 공장 적용을 목표로 여러 제조사 AGV·AMR 을 하나의 웹 플랫폼으로 감시하는 플릿 관리 소프트웨어를 실험실에서 시험했다. 기존 ref-136 저자 '미확인' 정정(출판 PDF 첫 원문 열람, 저자 17명 확인).
- **ref-1429**: Logistics Journal: Proceedings No.19, DOI 10.2195/lj_proc_franke_en_202310_01. 2023년 봄 여섯 회사 워크숍으로 VDA 5050 개념 기반 새 표준 인터페이스 요구를 정리했다. 기존 ResearchGate URL 대신 학술지 원문 PDF 를 처음 열람했다.
- **ref-258**: ARM Institute 과제 소개. 주관 기관 Siemens Technology, 협력 기관 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 이며 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만들 계획을 적는다. 이번이 첫 원문 열람이다.
- **ref-1425**: 원문 미열람. 구역 이름을 받아 구역 안 경유점을 예약하는 GoToZone 기능을 제안하는 풀 리퀘스트로 외부 조사 메모가 미병합이라 기록했으나, 이번 환경에서 GitHub 접근이 막혀 상태를 확인하지 못했다.
- **ref-1426**: CHART 가 RMF-2.0 프로젝트로 개발한 Open-RMF 구역(zones) 기능을 소개하는 2026-05-07 SIG 세션 공지. 공지 시점에 기능이 검토 중이라고 밝히고, 2026-07-08 녹화 링크가 덧붙었다.
- **ref-255**: InOrbit 의 AMR 상호운용 ROS 패키지 저장소. 이번에는 1.1.1 태그의 MassRobotics 송신 예제 설정(operationalState·errorCodes 토픽 매핑)을 확인했다.
- **ref-230**: MassRobotics AMR 상호운용 표준 JSON 스키마. 이번에는 1.0 태그에서 statusReport 필수 필드(uuid·timestamp·operationalState·location)를 확인했다.
- **ref-256**: Open-RMF free_fleet README. 이번에는 과거 태그 1.3.0 의 README(CycloneDDS dds_idlc 메시지 생성, ROS 1·2 cyclonedds 판 일치 권고)를 확인했다. 태그 커밋일은 확인하지 못했다.
- **ref-742**: Node.js·브라우저용 VDA 5050 라이브러리. 이번에는 v1.7.0(2026-04-29) 변경 이력의 VDA 5050 3.0 지원(ZoneSet·Responses 토픽, 3.0 검증기)을 확인했다.
- **ref-1427**: InOrbit 의 Automate 2026 다중 제조사 로봇 오케스트레이션 시연 페이지. 로봇 7개사·위치 추적 2개사·InOrbit 을 합쳐 10개사 협업이라고 밝힌다.
- **ref-1428**: 카카오모빌리티 보도자료. 로보티즈와 협력해 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용했고 가동률·성공률 개선을 주장한다. 같은 내용을 옮긴 기사는 기존 ref-1200 이다.
- **ref-1200**: 카카오모빌리티·로보티즈의 호텔 룸서비스 로봇 배송 사례(신라스테이 서초·반얀트리 클럽 앤 스파 서울)와 회사가 밝힌 가동률·성공률·매출 수치를 전한 기사. 카카오모빌리티 보도자료(ref-1428)를 옮긴 것이다.
- **ref-159**: 원문 미열람. 서로 다른 공급사의 산업용 이동로봇·플릿 관리자 사이 통신·상호운용을 다루는 ISO 규격 페이지. 외부 메모는 2026-10-10 단계 60.00(발행 중)을 기록했으나 이번 환경에서 iso.org 가 403 으로 막혀 확인하지 못했다.
- **ref-854**: OSRA 상호운용 SIG 2026-07-02 세션 공지(2026-06-25 게시). Open-RMF REST API 를 MCP 도구로 노출하는 서버와 NVIDIA Isaac Sim 창고 로봇을 움직이는 에이전트(Nayantra)를 다룬다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/robot-and-vendor-fleet-manager-integration.md | 3, 5, 6, 7, 8, 10, 11 | 갱신(차등): 섹션 3 — IO-AMRs 목표 문장(기존 내용 확인)에 주관 기관 Siemens Technology·협력 기관과 '계획 단계' 범위만 보탬(f21·f22·f23). / 섹션 5 — 연동 위치와 제어 수준을 따로 기록하는 기준(f14, InOrbit 문서 f13 은 벤더 주장 보강 근거로만; 제조사 관제 API 경유 전체 제어 조건은 '제약' 행 ref-251 에 이미 있어 중복 추가 안 함), 새 사례 두 개: 전시 시연(현장 유형 기타, f34·f35, 벤더 주장), 국내 호텔(현장 유형 상업 시설, f36·f37, 벤더 주장; 2. 사용 사례·요구·책임 범위의 ref-1200 사례와 같은 건이므로 '플랫폼–제조사 연동 사례' 분류 관점만 짧게). / 섹션 6(주제 페이지 2026-09-25-area09-s6 요약) — VDA 연결 단절 시 실행 의미와 상태 분리(f6~f8; '마지막으로 해제된 노드' 번역어는 대분류 개요와 같게, f6 사실은 개요에 이미 있으므로 영역 20 에는 상태 분리 관점으로), 신호등 연동의 정지 시간 전제·교착 시 사람 개입(f9~f11), 상태·오류 변환표 절에 ros_amr_interop→MassRobotics 필드 매핑 사례(f27~f29). / 섹션 7(주제 페이지 2026-09-25-area09-s7 표) — VDA 5050 3.0.0 행의 '정확한 발행일 미확인'을 공식 자료 세 날짜 표시로 교체(f1~f5), Open-RMF 신호등 연동 평가 시 패키지 판 기록(f12; 2.14.0 수정 사실은 27. 다중 로봇 경로·교통 관리 — MAPF 에 이미 있음), Open-RMF 구역 기능 개발 상태(f24 추정·f25·f26), free_fleet 1.3.0 판 구분(f30·f31), vda-5050-lib.js v1.7.0 3.0 지원(f32·f33). / 섹션 8(주제 페이지 2026-09-25-area09-s8) — Lopes 외 항목의 저자 '미확인'을 17명 저자·DOI 로, '작업 상태 갱신 평균 지연 120 ms'를 '로봇 상태 평균 갱신 간격 약 120 ms'로 정정하고 20대 감시·§5.3 실험실 범위 추가(f15~f18), Franke 외 항목에 워크숍 구성과 서지 보강(f19·f20). / 섹션 10(주제 페이지 2026-09-25-area09-s10) — 21. 상호운용 표준·적합성: ISO 21423 단계 기록은 추정으로 연결 제안 수준(f38, oq-027 과 겹치므로 링크만), 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션: MCP 로 Open-RMF REST API 노출 시연(f39·f40, oq-141 관련). / 섹션 11(주제 페이지 2026-09-25-area09-s11) — 분리 페이지의 '신규' 세 질문을 실제 id 로 표기(oq-031·oq-032·oq-033), 부분 근거: oq-005 ← f1~f5, oq-032 ← f9~f11, oq-033 ← f27~f29, oq-031 ← f14·f20·f37(답 아님, 판단 기준만). 모두 열림 유지. 새 질문 5건. 다음 실행 후보: 21. 상호운용 표준·적합성(ISO 21423 발행 확인, f38), 27. 다중 로봇 경로·교통 관리 — MAPF(신호등 연동 교착, f9~f11). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- Lopes 외 논문이 보고한 로봇 상태 평균 갱신 간격 약 120 ms 와 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점(타임스탬프 정의)으로 측정했는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 37. 관제 화면·실행 기록 | 근거: f15 | 종류: 일반
- ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f22 | 종류: 일반
- zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가? | 관련 영역: 20. 로봇·제조사 관제 연동, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f30 | 종류: 일반
- InOrbit 의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f34 | 종류: 일반
- 카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API 와 로봇 대수·운영 기간은 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 64. 상업 시설 | 근거: f36 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 6건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-06/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.
    - VDA 5050 3.0.0 GitHub 릴리스 설명의 'March 19th, 2026'과 게시 시각(published_at)은 이 환경에서 확인하지 못해 출처로 넣지 않았다(발행일 null 유지).
    - f24: GoToZone PR #516(ref-1425)의 설명·미병합 상태는 GitHub 접근 차단으로 원문 대조 실패. 간접 근거로 2026-05-04 SIG 공지(ref-1426, f25)만 사실로 둠
    - f38: ISO 21423 카탈로그의 '60.00 Under publication' 단계는 iso.org 403 으로 확인 실패(ref-159 원문 미열람)
    - f15~f17: Lopes 외 120 ms·20대 결과의 측정 장소·로봇 구성·시험 기간은 논문에 명시돼 있지 않음
    - f30: free_fleet 1.3.0 태그 커밋일 미확인(published null)
    - f34·f36: Automate 2026 시연과 카카오모빌리티 호텔 사례는 벤더 발표만 있고 독립 확인 없음(ref-1200 은 보도자료를 옮긴 기사)
    - oq-031: 국내 물류센터의 직접 제어·위임 비중·비용·처리량 비교 자료는 이번에도 찾지 못함
- 범위 경계 위반 의심:
    - f38: ISO 21423 은 21. 상호운용 표준·적합성 쪽 내용이므로 claim 을 '연계 대상: '으로 시작하고 10절 연결 제안 수준으로만 씀
    - f9~f11: 신호등 연동의 교착 처리는 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 영역 20 에는 연동 계약 관점으로 한정
    - f39·f40: MCP·언어 모델 연동은 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션 쪽 내용이라 연결 제안으로만 씀
    - f36·f37: 호텔 사례의 업무 범위는 2. 사용 사례·요구·책임 범위·64. 상업 시설에 이미 있으므로 영역 20 에는 연동 사례 분류만
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 6건(ref-1423, ref-1424, ref-1425, ref-1426, ref-1427, ref-1428, 예약 구간 ref-1423~ref-1452 안), 재사용 15건. 메모 출처 매핑: n1·VDA 공식 PDF→ref-031, n3→ref-032, n4→ref-1423(신규), n5→ref-251, n6→ref-1424(신규, 위키에 EasyTrafficLight.hpp 출처 없음), n7→ref-136, n8→ref-1429, n9→ref-258, n10→ref-1398, n11→ref-1425(신규, 미열람), n12→ref-742, n13→ref-255, n14→ref-230, n15→ref-256, n16→ref-1427(신규; 기존 ref-177 은 RoboticsTomorrow 게재 보도자료라 다른 문서), n17→ref-1428(신규, 카카오모빌리티 보도자료 원문)+ref-1200(같은 내용을 옮긴 아시아경제 기사, 이번에 재열람해 호텔 이름 확인), n18→ref-854, n19→ref-159, n20→ref-1029. n2(GitHub 릴리스)는 넣지 않음. 간접 근거로 SIG 공지 ref-1426(신규) 추가. 검증 수정 반영: VDA 날짜는 세 공식 표시가 다르다는 것을 사실로, 하나로 확정하지 않는 것은 의견으로(f4·f5); 상태 배열 근거를 §6.6.9·§7.8 로(§7.7 아님, f7); '마지막으로 해제된 노드' 번역어를 대분류 개요와 맞춤(f6); Lopes 120 ms 를 '평균 갱신 간격'으로, 실험실 범위를 §5.3 지도 작성·연결 작업으로 좁힘(f15~f17); Franke 근거 쪽수 p.5(f19); IO-AMRs 는 주관 기관·계획 단계만 새로(f21·f22); 제조사 관제 API 경유 전체 제어는 5절 '제약' 행 기존 내용이라 중복 추가 안 함(f13 은 보강); EasyTrafficLight 2.14.0 수정은 의견으로만(f12); GoToZone PR·ISO 21423 단계는 추정·미열람(f24·f38); Automate·호텔은 벤더 주장·추정 유지. 교차 확인 0건: VDA 날짜 세 자료는 모두 VDA 계열, Open-RMF 헤더·변경 이력은 같은 프로젝트, ref-1200 은 ref-1428 을 옮긴 기사라 독립 출처가 아니다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-005 근거 f1~f5, oq-032 근거 f9~f11, oq-033 근거 f27~f29, oq-031 판단 기준 f14·f20·f37. 분리 페이지 11절의 '신규' 세 질문은 oq-031·oq-032·oq-033 이다. 메모의 새 질문 U1~U11 가운데 기존 질문과 겹치는 U1(oq-005)·U2(oq-031)·U3(oq-032)·U4(oq-033)·U11(oq-141 과 겹침)과 본문 근거가 없는 U6 은 빼고 U5·U7·U8·U9·U10 을 다듬어 5건을 올렸다. 현장 유형 사례 finding: 상업 시설(호텔, f36·f37), 기타(전시 시연, f34·f35). 용어 후보 없음(플릿 어댑터·VDA 5050·오픈 RMF 는 용어집에 있음). 입력 누락 없음. 우선 지정 질문 없음.
