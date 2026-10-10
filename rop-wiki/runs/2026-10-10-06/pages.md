# 스토리텔러 산출 2026-10-10-06

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/integration/robot-and-vendor-fleet-manager-integration.md | draft | 차등 갱신: 3절 IO-AMRs 범위 한정 추가, 5절 연동 위치·제어 수준 기록 기준과 상업 시설·기타 사례 추가, 6절 단절 시 상태 분리·신호등 연동 전제·상태 변환 사례, 7절 VDA 5050 3.0.0 날짜 병기·공개 구현 판 정보, 8절 Lopes·Franke 서지·범위 보강, 10절 21·47·12·2·64·67번 연결, 11절 부분 근거와 새 질문 5건, 6·7·8·10·11절에 2026-09-25 분리 페이지 링크 유지, 13절 각주 갱신(Franke 외 기존 id ref-1430 의 URL·발행일·열람 반영, ref-258 열람 반영, ref-031·ref-251·ref-256 접근일, 신규 각주) |
| create | docs/topics/2026/2026-10-10-area20-s7.md | draft | 자동 분리: 20. 로봇·제조사 관제 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,938자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area20-s6.md | draft | 자동 분리: 20. 로봇·제조사 관제 연동 의 "6. 대표 접근법과 기술" 절(1,684자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area20-s11.md | draft | 자동 분리: 20. 로봇·제조사 관제 연동 의 "11. 열린 질문" 절(1,604자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area20-s8.md | draft | 자동 분리: 20. 로봇·제조사 관제 연동 의 "8. 대표 연구와 자료" 절(1,251자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area20-s10.md | draft | 자동 분리: 20. 로봇·제조사 관제 연동 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,088자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area20-s3.md | draft | 자동 분리: 20. 로봇·제조사 관제 연동 의 "3. 왜 중요한가" 절(915자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-10 | 20. 로봇·제조사 관제 연동 | 차등 갱신: VDA 5050 3.0.0 공식 자료 날짜 차이 병기, 단절 시 상태 분리·신호등 연동 전제·상태 변환 사례, 상업 시설·기타 사례 추가, Lopes·Franke(ref-1430)·IO-AMRs 서지·범위 보강, 새 열린 질문 5건 | run 2026-10-10-06
- 홈 최근 업데이트: 2026-10-10 — 20. 로봇·제조사 관제 연동: VDA 5050 3.0.0 공식 자료의 날짜 차이(카탈로그 2026-03-17·보도자료 2026-04-20) 병기, 신호등 연동 전제와 단절 시 상태 분리, 상업 시설·기타 현장 사례 추가
- 대분류 최근 업데이트: 2026-10-10 — 20. 로봇·제조사 관제 연동: 3·5·6·7·8·10·11절 차등 갱신(VDA 5050 3.0.0 날짜 병기, Open-RMF 신호등 연동 전제, ros_amr_interop 상태 매핑, Lopes·Franke 서지 보강)
- 세부영역 최근 업데이트: 2026-10-10 — 20. 로봇·제조사 관제 연동: 연동 위치·제어 수준 기록 기준과 호텔(상업 시설)·전시 시연(기타) 사례, 단절 시 상태 분리, 공개 구현 판 정보, 21·47·12번 연결과 새 열린 질문 5건 추가

## 용어집 갱신

- 없음

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 표준 | medium | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN |
| ref-1423 | VDA(Verband der Automobilindustrie) | VDA 5050 | 표준 | medium | https://www.vda.de/en/news/publications/publication/vda-5050 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-1029 | InOrbit | Contents — InOrbit Developer Portal | 벤더 문서 | medium | https://developer.inorbit.ai/docs |
| ref-1424 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp |
| ref-1398 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst |
| ref-136 | Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명) (Polytechnic University of Coimbra 등; Applied Sciences, MDPI) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 논문 | medium | https://www.mdpi.com/2076-3417/15/13/7235 |
| ref-1430 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 논문 | medium | https://proc.logistics-journal.de/article/download/1067/1036/8465 |
| ref-258 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 정부·연구기관 | medium | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ |
| ref-1426 | Open Robotics Discourse (OSRA Interop SIG) | Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490 |
| ref-255 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 오픈소스 문서 | high | https://github.com/inorbit-ai/ros_amr_interop |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 오픈소스 문서 | high | https://github.com/open-rmf/free_fleet |
| ref-742 | coatyio (vda-5050-lib.js GitHub) | vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README) | 오픈소스 문서 | medium | https://github.com/coatyio/vda-5050-lib.js |
| ref-1427 | InOrbit.AI | 10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026 | 벤더 문서 | low | https://www.inorbit.ai/automate-2026 |
| ref-1428 | 카카오모빌리티 | 카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속 | 벤더 문서 | low | https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 표준 | medium | https://www.iso.org/standard/86749.html |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | Lopes 외 논문 초록의 작업 상태 갱신 평균 지연 120 ms 와 본문 §6.2 의 로봇 상태 평균 갱신 간격 약 120 ms 는 같은 측정인가, 그리고 이 값과 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점(타임스탬프 정의)으로 측정했는가? | 20, 37 | 열림 | — |
| new | — | ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가? | 20 | 열림 | — |
| new | — | zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가? | 20, 42 | 열림 | — |
| new | — | InOrbit 의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가? | 20 | 열림 | — |
| new | — | 카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API 와 로봇 대수·운영 기간은 공개됐는가? | 20, 64 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 기타 | 수행 자원 | docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#5-적용-사례-현장-유형-명시 | 20. 로봇·제조사 관제 연동 |
| 상업 시설 | 수행 자원 | docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#5-적용-사례-현장-유형-명시 | 20. 로봇·제조사 관제 연동 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 분리 주제 페이지 topics/2026/2026-09-25-area09-s7.md·s8.md·s11.md 의 본문이 이번 입력에 없어 직접 고치지 못했다. 다음 갱신에서 그 페이지들을 입력으로 넣어 (1) s7 표 VDA 5050 3.0.0 행의 '정확한 발행일 미확인'을 카탈로그 2026-03-17·보도자료 2026-04-20 병기로, (2) s8 의 ref-136 저자 '미확인'을 'Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명)'으로, (3) s11 의 '신규' 세 질문을 oq-031·oq-032·oq-033 으로 바꾸도록 요청한다(이번에는 세부영역 페이지 7·8·11절과 reference_updates 로만 반영).
- 트랙 반영 제안(실행 2026-09-25-23): VDA 5050 팩트시트 2.1.0 태그와 3.0.0 의 필드 이름 변화(agvGeometry→mobileRobotGeometry 등)와 추가 필드를 7절에 넣으려면 이번 브리프에 없는 원문 대조 finding 이 필요하다.
- 트랙 반영 제안(실행 2026-09-25-35): MassRobotics 운용 상태 9종·적재 여유 비율·화물 최대 중량·부피의 형식·단위 정규화를 7절에 넣으려면 ref-230 원문 대조 finding 이 필요하다.
- 3절·8절: IO-AMRs 과제의 완료 여부·결과 보고서, Lopes 외 논문 본문 §6.2·§5.3 수치(PDF 판독)와 Franke 외(ref-1430) p.5 워크숍 구성의 원문 대조가 필요하다(현재 [추정]).
- 7절·10절: VDA 5050 3.0.0 GitHub 릴리스 설명의 날짜와 ISO 21423 카탈로그 단계(60.00)를 원문으로 확인해 oq-005·21. 상호운용 표준·적합성 쪽에 반영할 근거가 필요하다.
- 7절: Open-RMF 구역(zones) 기능이 배포판(태그)에 병합됐는지 확인할 원문 근거가 필요하다(rmf_ros2 PR #516 은 실재 미확인으로 제외).
- 실행 스크립트 담당: 자동 분리가 기존 절의 '자세한 내용은 주제 페이지 […2026-09-25-area09-sN.md]에 있다' 줄을 새 분리 페이지 링크로 덮어쓰며 옮기지 않았다. 이번에는 append 패치 첫머리에 옛 분리 페이지 링크 줄을 넣어 대응했으나, 재분리 시 기존 링크 줄을 보존하거나 새 분리 페이지 본문으로 옮기도록 분리 코드를 고쳐 달라고 요청한다.
- 실행 스크립트 담당: 참고문헌 id 치환 처리(ref-1430·ref-1429·ref-1430) 점검을 요청한다. 같은 Franke 외 논문이 리서치 브리프에서는 ref-1429, 이전 스토리텔러 입력에서는 ref-1430, 이번 입력(기존 페이지 9절·13절·auto:area-recent 와 참고문헌 색인 ResearchGate URL 행)에서는 ref-1430 로 보였고, 이전 초안 렌더링에서는 패치하지 않은 9절과 auto:area-recent 안의 ref-1430 가 ref-1430 으로 바뀌어 있었다. URL 이 바뀐 출처(ResearchGate → 학술지 PDF)를 새 id 로 치환하는 처리가 있는지 확인하고, 이번 reference_updates 의 ref-1430(URL 변경)가 새 id 로 분리되지 않게 해 달라.

## 이행한 수정 지시

- f3 강등 — 7절에서 PDF 표지의 판 표기(2026년 3월)를 '보고됐으나 검증 단계에서 대조하지 못했다' [추정]으로 쓰고 각주를 ref-1423 으로 달았다.
- f4 분리 — 7절에서 카탈로그 2026-03-17 과 보도자료 2026-04-20 의 날짜 차이는 [사실](ref-1423·ref-032)로, PDF 표지의 월은 별도 [추정] 문장으로 나눠 썼다.
- f5 — 7절에 '이 위키는 … 맞다고 본다' 형식의 [의견]으로 썼고, 13절 ref-031 각주 발행일은 '미확인' 그대로 두었다.
- oq-005 — 7절과 11절에 부분 근거(f1·f2·f4 분리형, f5 의견)만 덧붙이고 상태는 열림으로 유지했다(open_question_updates 에 해결 변경 없음).
- f15 — 8절에서 초록의 작업 상태 갱신(task status updates) 평균 지연 120 ms·화면 갱신 1초 미만은 [사실], 본문 §6.2 의 로봇 상태 평균 갱신 간격은 [추정](검증 단계 미대조)으로 병기했다.
- f18 — 기존 '작업 상태 갱신 평균 지연 120 ms' 표현을 교체하지 않고 8절에 두 표현을 병기했으며, 실험실 감시 결과라는 한정만 [의견]으로 남기고 표현 차이는 Lopes 새 열린 질문 문장에 합쳤다.
- f16·f17 — 8절에서 20대·99.5%·약 500 m²·측정 장소 미명시를 '논문 본문 §6.2·§5.3 은 … 보고한다(검증 단계 미대조)' [추정]으로 썼다.
- ref-136 기관 — reference_updates 와 13절 각주의 기관을 'Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명)'으로 고쳤다. 분리 페이지(2026-09-25-area09-s8)의 본문은 입력에 없어 직접 패치하지 못했고, 참고문헌 갱신으로 반영되도록 하고 additional_research_requests 에 후속 갱신을 요청했다.
- f19 — 8절에서 저자 4명·2023-10-11·DOI·Proceedings Nr. 19·워크숍 참여 주체는 [사실], 2·3·1 여섯 회사·2023년 봄은 [추정](본문 p.5, 검증 단계 미대조)으로 썼다(각주는 기존 id ref-1430).
- ref-1429 각주 — 기존 Franke 각주(입력 기존 페이지의 ref-1430)를 고치라는 뜻으로 이행해 13절에서 URL 을 학술지 PDF 로, 발행일 2023-10-11, 접근일 2026-10-10 으로 바꾸고 '(원문 미열람)'을 뗐으며, 8절의 주변 설비 인터페이스 문장은 건드리지 않았다.
- ref-258 각주 — 13절에서 접근일을 2026-10-10 으로 바꾸고 '(원문 미열람)'을 뗐으며, 3절에 f21·f22 와 성과 근거로 쓰지 않는다는 f23 범위 한정만 덧붙였다.
- f24 — 본문·표·열린 질문 어디에도 넣지 않았고 ref-1425 를 reference_updates 에서 뺐으며, 7절 구역 기능의 의견(f26)은 ref-1426 하나만 각주로 달았다.
- f12 — 참고문헌 색인에 있는 ref-1398 하나만 각주로 쓰고(ref-1513 미사용), 7절에 패키지 판을 기록한다는 평가 관점만 [의견]으로 쓰며 수정 내용은 27. 다중 로봇 경로·교통 관리 — MAPF 로 넘겼다.
- f6 — 6절에서 새 사실 문장을 만들지 않고 F. 연동 대분류 페이지를 가리키며 같은 번역어 '마지막으로 해제된 노드'와 같은 각주 ref-031 을 썼고, 중심은 f8 의 상태 분리 [의견]으로 두었다.
- f13·f34·f36 — 5절의 해당 문장 모두 [추정]에 '벤더 주장'을 병기했고, ref-1200 은 인용·교차 확인에 쓰지 않았다.
- 5절 새 사례 — 기타(전시 시연)와 상업 시설(호텔) 사례의 근거 없는 칸은 '미확인'으로 두고 로봇 대수·위임 방식·성과 수치를 채우지 않았으며, site_matrix_updates 에는 근거로 채운 '수행 자원' 칸 두 개만 냈다.
- f38 — 10절에서 '연계 대상: ' 서술과 [추정]을 유지해 21. 상호운용 표준·적합성으로 연결만 했고, 13절 ref-159 각주에 '(원문 미열람)'을 두었다.
- f39·f40 — 10절에서 47. AI·학습·적응과 모델 운영, 12. 채팅으로 업무 지시·오케스트레이션과 잇는 연결 문장으로만 쓰고 시뮬레이션 시연임을 밝혔으며 승인 관문 문제는 oq-141 로 넘겼다.
- 직접 인용 — 출처 원문 인용은 ref-136 의 'task status updates' 한 구절뿐이며, ref-031·ref-1424·ref-1427·ref-258 은 모두 재서술했다('muti-map' 오탈자는 쓰지 않음).
- 트랙 반영 제안 — 실행 2026-09-25-23 제안(팩트시트 필드 이름 변화)은 반영하지 않고 제안 상태로 두었고, 실행 2026-09-25-35 제안은 7절에 f28(statusReport 필수 필드) 범위만 반영했다.
- open_questions_new — 다섯 질문을 open_question_updates 에 new 로 냈고 Lopes 질문에 초록·본문 표현 차이를 묻는 문장을 합쳤으며, oq-005·oq-031·oq-032·oq-033 은 상태 변경 없이 11절에 부분 근거(oq-032 f9~f11, oq-033 f27~f29, oq-031 f14·f20·f37)만 달았다.
- 2차: 2026-09-25 분리 페이지 링크 복원 — 6·7·8·10·11절 append 패치 첫머리에 각각 2026-09-25-area09-s6·s7·s8·s10·s11.md 로 가는 링크 줄을 넣어, 재분리돼도 새 분리 페이지 본문에 남게 했다. 분리 코드가 기존 링크 줄을 덮어쓰는 동작 자체는 패치로 고칠 수 없어 additional_research_requests 에 실행 스크립트 담당 요청으로 적었다.
- 2차: 절 번호만 쓴 참조 — 6절·10절·11절에서 '7절'·'5절' 같은 번호만 쓴 참조를 '20. 로봇·제조사 관제 연동의 「7. 관련 표준·프레임워크·오픈소스」 절' 형식의 원 페이지 절 이름으로 바꿨다.
- 2차: 각주 접근일 — 13절의 ref-031·ref-251·ref-256 각주 접근일을 reference_updates 의 accessed 와 같은 2026-10-10 으로 고쳤다.
- 2차: Franke 외 논문 id 통일 — 입력 기존 페이지 9절 표와 참고문헌 색인의 ResearchGate URL 행에 붙은 id 인 ref-1430 를 3절 VDA 5050 문장(replace 패치), 8절 append 패치의 Franke 항목 세 곳, 13절 각주 정의, 세부영역 페이지 프런트매터 sources, reference_updates 항목 id 에 똑같이 썼다. reference_updates 의 ref-1430 는 URL 을 학술지 PDF(https://proc.logistics-journal.de/article/download/1067/1036/8465)로, 발행일 2023-10-11, 접근일 2026-10-10, source_unopened false 로 바꿨고, 예약 구간 id(ref-1429·ref-1430)는 어디에도 쓰지 않았다. 분리 페이지 s3·s8 의 본문·출처·sources 는 이 패치와 13절 각주에서 생성되므로 같은 ref-1430 가 된다.
- 2차: 9절·auto:area-recent 미패치 — 두 곳은 패치하지 않았다. 이번 입력에서 기존 페이지 9절 표의 Franke 논문 id 는 ref-1430, 참고문헌 색인의 ResearchGate URL 행 id 도 ref-1430 로 서로 같았다(차이 없음). 다만 이전 초안 렌더링(runs/2026-10-10-06/pages/…)에서는 9절과 auto:area-recent 안이 ref-1430 으로 보였고 리서치 브리프는 같은 논문을 ref-1429 로 적었으므로, '참고문헌 id 치환 처리(ref-1430·ref-1429·ref-1430) 점검'을 additional_research_requests 에 실행 스크립트 담당 요청으로 남겼다.
- 분량 초과 자동 분리: 20. 로봇·제조사 관제 연동 본문 12,637자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 5,097자
