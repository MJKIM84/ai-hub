# 스토리텔러 산출 2026-09-30-06

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md | draft | 섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건 |
| create | docs/topics/2026/2026-09-30-area43-s6.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,750자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area43-s10.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,115자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area43-s7.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,055자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area43-s4.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "4. 핵심 개념과 용어" 절(975자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area43-s11.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "11. 열린 질문" 절(889자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area43-s3.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "3. 왜 중요한가" 절(743자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 43. 데이터·관측성·배포 | 섹션 3~11 신규 작성(seed → draft): 기록·관측성·배포·비용 접근법, 병원·물류창고 적용 사례, 책임 경계, 열린 질문 6건. 1차 조건부 승인 수정 15건 이행 | run 2026-09-30-06
- 홈 최근 업데이트: 2026-09-30 — 43. 데이터·관측성·배포: 섹션 3~11 신규 작성(MCAP·OpenTelemetry·A/B 롤백·FinOps 접근법, 병원·물류창고 적용 사례, 책임 경계, 열린 질문 6건)
- 대분류 최근 업데이트: 2026-09-30 — 43. 데이터·관측성·배포: 섹션 3~11 신규 작성(seed → draft). 기록 형식·플랫폼 관찰·배포 롤백·비용 계측과 책임 경계 정리
- 세부영역 최근 업데이트: 2026-09-30 — 43. 데이터·관측성·배포: 섹션 3~11 신규 작성, 1차 조건부 승인 수정 15건 이행 (실행 2026-09-30-06)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 관측성 | Observability | 시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다. | 43, 37, 38 | ref-1042 |
| new | 오픈텔레메트리 | OpenTelemetry (OTel) | 추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다. | 43, 38, 47 | ref-1042, ref-1043 |
| new | MCAP | MCAP | 여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다. | 43, 37, 38 | ref-1040, ref-1041 |
| new | 핀옵스 | FinOps | 클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다. | 43, 3 | ref-1048 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md |
| ref-1038 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 논문 | medium | https://arxiv.org/abs/2201.00393 |
| ref-1039 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 논문 | medium | https://arxiv.org/abs/2606.10746 |
| ref-1040 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 오픈소스 문서 | high | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html |
| ref-1041 | Foxglove | MCAP as the ROS 2 Default Bag Format | 벤더 문서 | medium | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format |
| ref-1042 | OpenTelemetry (CNCF) | Specification Status Summary | 오픈소스 문서 | high | https://opentelemetry.io/docs/specs/status/ |
| ref-1043 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 오픈소스 문서 | high | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md |
| ref-1044 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 오픈소스 문서 | medium | https://github.com/szobov/ros-opentelemetry |
| ref-1045 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ |
| ref-1046 | Northern.tech (mendersoftware) | mender — README | 오픈소스 문서 | high | https://github.com/mendersoftware/mender |
| ref-766 | 개인정보보호위원회 (국가법령정보센터) | 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호) | 정부·연구기관 | medium | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 |
| ref-1048 | FinOps Foundation | FinOps Phases | 업계 보고서 | medium | https://www.finops.org/framework/phases/ |
| ref-1049 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 표준 | medium | https://www.finops.org/insights/focus-1-2-available/ |
| ref-943 | Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-1051 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 논문 | medium | https://arxiv.org/abs/2609.29043 |
| ref-1052 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies and innovation at scale | 벤더 문서 | medium | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? | 43, 38 | 열림 | — |
| new | — | 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? | 43, 53 | 열림 | — |
| new | — | 개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? | 43, 13 | 열림 | — |
| new | — | 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? | 43, 57 | 열림 | — |
| new | — | 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? | 43, 53 | 열림 | — |
| new | — | 구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가? | 43, 63 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |
| 병원 | 작업 대상 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |
| 병원 | 완료·인계 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |
| 병원 | 예외·성과 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |
| 물류창고 | 예외·성과 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) | 오픈소스 | Foxglove (ROS 2 채택: Open Robotics) | 43, 37, 38 | ref-1041 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format |
| OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 | 오픈소스 | OpenTelemetry (CNCF) | 43, 13, 47 | ref-1043 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md |
| ros-opentelemetry | 오픈소스 | szobov (GitHub, 개인 저장소) | 43, 38 | ref-1044 | https://github.com/szobov/ros-opentelemetry |
| Mender (OTA 업데이트 관리자) | 오픈소스 | Northern.tech (mendersoftware) | 43, 57 | ref-1046 | https://github.com/mendersoftware/mender |
| FinOps 프레임워크 (FinOps Phases) | 프레임워크 | FinOps Foundation | 43, 3 | ref-1048 | https://www.finops.org/framework/phases/ |
| FOCUS 1.2 (FinOps 청구 데이터 명세) | 표준 | FinOps Foundation | 43, 3 | ref-1049 | https://www.finops.org/insights/focus-1-2-available/ |

## 추가 조사 요청

- 3·7·9·11절: 개인정보보호위원회고시 제2025-9호 제8조와 부칙 시행일 확인 — 현행 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은지 알아야 강등된 보존 의무 서술을 [사실]로 바로잡을 수 있다.
- 5절 병원 사례: 구로병원 약품 배송 로봇 실증의 수행 자원(로봇·간호사·승강기 역할 분담)과 제약(승강기·시간·구역 제약) — 여섯 항목 가운데 두 칸이 미확인이다. 수령인(간호사) 확인 여부와 성공률 분모도 원문에서 재확인이 필요하다.
- 5절 물류창고 사례: Ocado 또는 다른 창고의 배포 전 검증 사례에서 시작 조건·작업 대상·수행 자원·제약·완료·인계 — 벤더 글 외 독립 출처가 없고 다섯 칸이 미확인이다.
- 5절: 제조 공장·상업 시설·가정·실외·기타 현장에서 운영 데이터 수집·관측성·소프트웨어 배포(롤백 포함)를 다룬 사례 — 이번 조사에서 찾지 못했다.
- 6·11절: OpenTelemetry 생성형 AI 토큰 지표의 이전 이름(gen_ai.client.token.usage)과 현재 이름(gen_ai.client.inference.usage.*)의 관계와 변경 시점.
- 6·7절: FOCUS 1.2 명세 본문(PDF) 열람 — 발표 글만 근거로 했다.
- 6·11절: 이종 제조사 로봇 기록과 플랫폼 분산 추적을 한 작업 식별자로 잇는 공개 사례·표준, 운행 중 로봇 작업을 끊지 않는 순차 배포·롤백 기준을 공개한 관제 제품·연구.
- 6·8절: ros2_tracing·ros2probe·LLM 연쇄 계획 논문의 본문 실험 조건(초록 기준 서술을 보강하기 위해).
- 다음 실행 제안: 38. 모니터링·이상 탐지·원인 분석 페이지에 ros2_tracing·ros2probe·구로병원 로그 분석 결과 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 Mender A/B 업데이트 반영.

## 이행한 수정 지시

- f11 강등 — 3·7·9·10절의 접속기록 문장을 모두 [추정]으로 쓰고 7절에 '제2023-6호(2023-09-22 시행 판) 기준이며 이후 개정 여부와 현행 조문(점검 주기 포함)은 미확인'을 밝혔으며 '월 1회 이상 점검'은 본문에서 뺐다.
- ref-766 원문 미열람 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-766 에 source_unopened: true 와 신뢰도 medium 을 넣었다.
- 현행 고시 열린 질문 — 11절과 open_question_updates 에 현행 「개인정보의 안전성 확보조치 기준」 접속기록 조항 질문(관련 영역 43·53)을 더하고 additional_research_requests 에 '개인정보보호위원회고시 제2025-9호 제8조와 부칙 시행일 확인'을 넣었다.
- f22 한정 — 3절 다섯째 까닭을 '2023-09-22 시행 판 기준 접속기록 보관 의무가 있었다(현행 조문 미확인)'로 한정해 [추정]으로 썼다.
- f16 — 5절 병원 사례 완료·인계 칸을 '로봇이 사람 개입 없이 전체 경로를 마치고 약품을 인계'로 쓰고 간호사 수령은 정의에 넣지 않았다.
- f17 — 로봇·승강기 로그와 관찰 기록지를 병원 사례의 예외·성과 칸과 서술에 두고 작업 대상 칸은 약품으로 썼으며 site_matrix_updates 도 시작 조건·작업 대상·완료·인계·예외·성과로 맞췄다.
- f18 — 성공률·실패 건수를 '저자 보고'로만 옮기고 분모를 계산해 덧붙이지 않았으며, 11절과 open_question_updates 에 성공률 분모 질문(관련 영역 43·63)을 지시 문구대로 올렸다.
- 5절 미확인 — 병원 사례의 수행 자원·제약과 물류창고 사례의 시작 조건·작업 대상·수행 자원·제약·완료·인계를 '미확인'으로 두고, 제조 공장·상업 시설·가정·실외 사례를 찾지 못했음을 밝혔으며 K3s 실험실 연구와 LLM 계획 평가 실험은 적용 사례로 쓰지 않았다.
- f5·f19 벤더 주장 — MCAP 장점과 Ocado 문장을 모두 '[추정] 벤더 주장'으로 쓰고, 6절 첫머리 종합 추정에서 배포 전 시뮬레이션 검증이 벤더 주장 근거임을 별도 문장으로 밝혔다(9·10절에도 같은 한정).
- f10 — 6절에서 'Mender README 는 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있다고 설명한다'처럼 출처의 설명으로 서술하고 '연계 대상:'으로 시작했다.
- f3·f14 — 3·6·8절에서 ros2probe 와 LLM 연쇄 계획 연구를 '동료 심사 전 arXiv 프리프린트'로 밝혔다.
- ref-1049 — reference_updates 의 발행일을 2025-06-03 으로 적고 본문 기준일은 비준일 2025-05-29 로 유지했으며, 각주에 '발행 기관의 발표 글, 명세 본문 미열람'을 밝혔다.
- ref-1052 — 참고문헌과 각주의 제목을 'Ocado's digital twins and simulations: driving efficiencies and innovation at scale' 로 고쳤다.
- 11절 셋째 질문 — '개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데'로 고쳐 이름 변경 단정을 없앴고 open_question_updates 에도 같은 문구로 냈다.
- 10절 교차 규칙 — 토큰 지표·LLM 호출 비용을 44. 로봇 기반 모델·언어 모델 계획, 47. AI·학습·적응과 모델 운영, 13. 대화형 기능의 신뢰·기반에 번호와 이름으로 연결하고, Ocado 사례는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)에만 연결했으며 18. 실시간 세계 상태·데이터 일관성은 연결하지 않았다.
- 분량 초과 자동 분리: 43. 데이터·관측성·배포 본문 10,414자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,745자
