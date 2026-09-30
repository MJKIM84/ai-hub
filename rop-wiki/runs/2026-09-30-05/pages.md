# 스토리텔러 산출 2026-09-30-05

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md | draft | 섹션 3~11 신규 작성(seed → draft): 판단 배치 혼합 구조, 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건. 1차 조건부 승인 수정 17건과 2차 수정 5건(3절 일반화 2건 좁힘, 4절 도입 단락, [의견] 주체 표시, 약어 풀이) 이행 |
| create | docs/topics/2026/2026-09-30-area41-s6.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "6. 대표 접근법과 기술" 절(3,254자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area41-s4.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "4. 핵심 개념과 용어" 절(1,132자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area41-s7.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "7. 관련 표준·프레임워크·오픈소스" 절(962자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area41-s10.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(879자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area41-s3.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "3. 왜 중요한가" 절(844자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area41-s8.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "8. 대표 연구와 자료" 절(832자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area41-s11.md | draft | 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "11. 열린 질문" 절(571자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 41. 플랫폼 아키텍처·외부 API | 섹션 3~11 신규 작성(로봇·현장 서버·클라우드 혼합 배치, REST·이벤트·웹훅·SDK 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건), 1차 조건부 승인 수정 17건·2차 수정 5건 이행 | run 2026-09-30-05
- 홈 최근 업데이트: 2026-09-30 — 41. 플랫폼 아키텍처·외부 API: 판단 배치(로봇·현장 서버·클라우드)와 외부 API 조합(REST·이벤트·웹훅·SDK), 병원·제조 공장·물류창고·기타 적용 사례로 3~11절 신규 작성
- 대분류 최근 업데이트: 2026-09-30 — 41. 플랫폼 아키텍처·외부 API: 섹션 3~11 신규 작성(혼합 배치·계산 오프로딩·다중 클라우드 장애 대응·제조사 어댑터 계층·외부 API 와 인증·권한, 적용 사례 4건)
- 세부영역 최근 업데이트: 2026-09-30 — 41. 플랫폼 아키텍처·외부 API: 영역 심화로 섹션 3~11 신규 작성, 신뢰도 low(핵심 결론은 종합 추정, 제품·국내 사례는 벤더 주장)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | OpenAPI 명세 | OpenAPI Specification (OAS) | HTTP API 의 경로·요청·응답·보안 방식을 사람과 컴퓨터가 함께 읽을 수 있게 기술하는 언어 중립 표준 형식으로, 3.1.0 은 웹훅도 기술한다. | 41, 23 | ref-1028 |
| new | AsyncAPI 명세 | AsyncAPI Specification | MQTT·AMQP·WebSocket·Kafka 같은 메시지 기반 API 의 채널·동작·메시지·브로커를 기계가독 형식으로 기술하는 프로토콜 중립 명세다. | 41, 21 | ref-1027 |
| new | 웹훅 | Webhook | 어떤 사건이 일어났을 때 서비스가 미리 등록된 외부 URL 로 HTTP 요청을 보내 알리는 방식의 이벤트 전달 인터페이스다. | 41, 37 | ref-1028, ref-1034 |
| new | 클라우드 로보틱스 | Cloud Robotics | 로봇이 인터넷으로 연결된 원격 계산·저장 자원에 계산이나 데이터를 맡겨 온보드 능력의 한계를 보완하는 구조와 연구 분야다. | 41, 42 | ref-304, ref-1032 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md |
| ref-304 | Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 논문 | medium | https://arxiv.org/abs/2205.09778 |
| ref-1025 | NAVER Corp. | 로보틱스 l NAVER Corp. | 벤더 문서 | medium | https://www.navercorp.com/tech/robotics |
| ref-937 | Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology) | ROMI-H | 정부·연구기관 | medium | https://www.cgh.com.sg/chart/projects/romi-h |
| ref-1027 | AsyncAPI Initiative | AsyncAPI Specification 3.1.0 | 표준 | high | https://www.asyncapi.com/docs/reference/specification/v3.1.0 |
| ref-1028 | OpenAPI Initiative | OpenAPI Specification v3.1.0 | 표준 | high | https://spec.openapis.org/oas/v3.1.0 |
| ref-1029 | 뉴스핌 | 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다 | 기사 | low | https://www.newspim.com/news/view/20260512001077 |
| ref-870 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막 | 기사 | low | https://www.irobotnews.com/news/articleView.html?idxno=43274 |
| ref-308 | Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv) | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 논문 | medium | https://arxiv.org/abs/2512.15215 |
| ref-1032 | Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv) | Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform | 논문 | medium | https://arxiv.org/abs/1706.08931 |
| ref-1033 | Open Robotics (open-rmf) | rmf_api_msgs — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs |
| ref-1034 | InOrbit | Contents — InOrbit Developer Portal | 벤더 문서 | medium | https://developer.inorbit.ai/docs |
| ref-774 | Mobile Industrial Robots (MiR) | MiR Fleet | 벤더 문서 | medium | https://mobile-industrial-robots.com/products/software/mir-fleet |
| ref-1036 | Locus Robotics | Seamless Integrations with LocusOne Robotics | 벤더 문서 | medium | https://locusrobotics.com/locusone/automated-warehouse-software/integrations |
| ref-1037 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 논문 | medium | https://arxiv.org/abs/2412.05408 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? | 41, 42 | 열림 | — |
| new | — | 로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가? | 41, 57 | 열림 | — |
| new | — | 로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가? | 41, 29 | 열림 | — |
| new | — | 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? | 41, 21 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 제조 공장 | 작업 대상 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 제조 공장 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 물류창고 | 시작 조건 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 물류창고 | 작업 대상 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 물류창고 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 물류창고 | 제약 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 물류창고 | 완료·인계 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 물류창고 | 예외·성과 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |
| 기타 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시 | 41. 플랫폼 아키텍처·외부 API |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| OpenAPI Specification 3.1.0 | 표준 | OpenAPI Initiative | 41, 23 | ref-1028 | https://spec.openapis.org/oas/v3.1.0 |
| AsyncAPI Specification 3.1.0 | 표준 | AsyncAPI Initiative | 41, 21 | ref-1027 | https://www.asyncapi.com/docs/reference/specification/v3.1.0 |
| FogROS2 (클라우드·포그 로보틱스 플랫폼) | 오픈소스 | Ichnowski, J., Chen, K., Dharmarajan, K. 외 | 41, 42 | ref-304 | https://arxiv.org/abs/2205.09778 |

## 추가 조사 요청

- 5. 적용 사례 (현장 유형 명시): 병원(RoMi-H)·제조 공장(RAIL)·기타(네이버 1784) 사례의 시작 조건·제약·완료·인계·예외·성과 칸 근거가 없어 미확인으로 두었다 — 실제 배치 보고서나 논문 본문에서 확인이 필요하다. 상업 시설·가정·실외 현장의 플랫폼 배치·외부 API 사례도 없다.
- 6. 대표 접근법과 기술: FogROS2 모션 계획 가속 배수가 arXiv v3 초록(45배)과 ICRA 2023 판 서술(28배)로 다를 수 있어 미확인으로 병기했다 — ICRA 카메라 레디 판 확인이 필요하다.
- 5·6절: 네이버 1784 의 클라우드 제어 로봇 대수(회사 페이지 100여 대, 기사 문구 40여 대)의 기준 시점 차이를 기사 원문으로 확인해야 한다.
- 7. 관련 표준·프레임워크·오픈소스: 국내 클라우드 로봇·이기종 로봇 통합관제의 참조 구조·외부 API 표준(TTA·KS)을 찾지 못했다(열린 질문으로 올림).
- 13. 참고 자료 (각주): ref-004·ref-031 은 기존 id 를 재사용했으나 기존 참고문헌 페이지(docs/references/ref-004.md, ref-031.md)의 '각주 형식' 줄이 입력에 없어 브리프 출처 값으로 적었다 — 퍼블리셔가 기존 줄과 대조해 맞춰 주기를 요청한다.
- 참고문헌 id 충돌(1차·2차 검증 지적): 이번 브리프의 신규 id 가운데 같은 날 이전 브리프(2026-09-30-03·04)의 다른 출처 id 와 겹치는 것이 있다 — 게시 전 id 재배정·병합을 pipeline 담당에게 요청한다. 참고로 입력 대분류 페이지(K. 플랫폼 아키텍처·인프라)의 '이 대분류의 자료' 목록에는 ref-304 가 FogROS2, ref-308 이 Brorsson 외 논문으로 같은 제목으로 이미 올라 있어, 이 두 id 는 기존 참고문헌과 같은 출처일 가능성이 있다(URL 은 입력에서 확인하지 못함).
- 42. 분산 시스템·통신·컴퓨팅 구조 페이지와의 중복: 역할 분담·장애 대응(FogROS2-FT·RAIL) 내용이 겹칠 수 있어 다음 해당 영역 실행에서 기존 각주와 대조가 필요하다.

## 이행한 수정 지시

- f1 강등 — 6절 '외부 API' 소절과 7절 표 rmf-web 행을 [추정]으로 쓰고 'REST'·'OpenAPI 형식' 표현을 빼, 웹 대시보드가 쓰는 API 엔드포인트, /docs 경로와 공개 문서 사이트의 API 정의, TortoiseORM 기반 PostgreSQL·SQLite·MySQL·MariaDB 와 기본 메모리 SQLite 로만 서술했다.
- f2 — 6절 인증·권한 문단의 권한 구조를 '역할·동작·권한 그룹 세 값으로 권한을 정하는 구조'로 고쳤고 7절 표에도 같은 표현을 썼다.
- f3 — 6절에서 README 가 이름으로 드는 스키마는 작업 상태(task_state)이고 작업 요청·플릿 상태 스키마는 저장소 스키마 파일 기준이라는 문장을 따로 두었다(reference_updates ref-1033 요약도 같게 고침).
- f5 — 6절에서 주제 계층을 '로컬 브로커용으로 제안한 것이고 클라우드 브로커에서는 조정될 수 있으며 주제 이름은 정해진 대로 써야 한다'로 고치고 visualization·zoneSet·responses 가 선택 주제임과 기준 판 3.0.0 을 밝혔다. 7절 표도 '제안'으로 썼다.
- f7 — 4절·7절에서 '3.1.0 에는 수신 웹훅을 기술하는 webhooks 필드가 있다'로 고쳤고, 용어집 'OpenAPI 명세' 정의의 '3.1.0 부터'를 '3.1.0 은'으로 고쳤다(reference_updates ref-1028 요약도 수정).
- f9 — 6절 FogROS2 문장에 'arXiv v3(2023-04-24) 초록 기준 저자 보고'를 적고 모션 계획 가속 배수는 판에 따라 다를 수 있어 미확인이라고 병기했다. 8절에도 v3 2023-04-24 를 적었다.
- f11 — 6절 역할 분담 문장의 로봇 쪽 역할을 '온보드 실행·자율 기능(범위는 연구마다 다름)'으로 좁혀 썼다.
- f12 — 4절·5절·6절·8절에서 현장 클라우드 앞의 '지연·연결 문제를 다루는' 수식어를 쓰지 않았고, f21 종합 문장의 '지연·연결에 민감한' 수식도 함께 뺐다.
- f19·ref-1029 — 6절 본문의 보도일과 각주·reference_updates 의 발행일을 2026-05-13 으로, 제목을 "카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다"로 고치고 '(제목 일부만 확인)'을 뗐다.
- f20·ref-870 — 제목을 "[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막"으로, 발행일·기준일을 2025-11-09 로 고치고, 6절에서 '50대 이상 로봇 동시 제어·승강기 연동' 문장과 '국내 첫 이기종 로봇 통합관제 솔루션이라는 주장' 문장을 나눠 썼다.
- f15 — 지원 대수는 본문에 쓰지 않았다(두 표현 가운데 한쪽을 고르지 않기 위해 수치 자체를 넣지 않음). MiR 내용은 모두 [추정] 벤더 주장으로 썼다.
- f21 — 3절·6절의 REST(OpenAPI 로 기술) 부분 근거를 ref-1028·ref-774·ref-1034(f7·f15·f16)로 한정하고 f1(rmf-web API 엔드포인트)을 근거로 쓰지 않았다. 6절 종합 문장의 ref-762 은 인증·권한(f2) 근거로만 남겼다.
- f24 — 9절에서 42. 분산 시스템·통신·컴퓨팅 구조를 외부 연계 대상으로 쓰지 않고, '클라우드 제공자 인프라는 외부 연계 대상, 현장 네트워크 설계는 ROP 의 다른 세부영역인 42. 분산 시스템·통신·컴퓨팅 구조에서 다룬다'로 나눠 썼다.
- 5·6·9절 f14 — 네이버 ARC 문장을 모두 [추정] 벤더 주장으로 쓰고, 5절·9절에서 위치 추정·이동 계획을 클라우드에 두는 것은 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 서술하며 ROP 직접 범위의 근거로 쓰지 않는다고 밝혔다.
- 5절 — 병원 사례 서술 첫 문장에 특정 병원의 배치 결과가 아니라 공공 의료기관용 미들웨어 구조임을 밝혔고, 네 사례 모두 근거가 없는 칸은 '미확인'으로 두었다(site_matrix_updates 에서도 제외).
- 11절 열린 질문 1 — '클라우드나 5G 연결'에서 '5G'를 빼 '클라우드 연결'로 고쳤다(open_question_updates 도 같음).
- 13절 — ref-004·ref-031 은 새 각주 id 를 만들지 않고 기존 id 를 재사용했다. 다만 기존 참고문헌 페이지의 '각주 형식' 줄이 입력에 없어 브리프 출처 값(기관·제목·URL·접근일)으로 적었으며, 기존 줄과의 대조를 additional_research_requests 로 퍼블리셔에 요청했다.
- 2차: 3절 FogROS2-FT 일반화 — '클라우드 로보틱스 연구는 … 약점으로 꼽는다'의 주어를 'Chen 외의 FogROS2-FT(IROS 2024)는'으로 바꾸고 '클라우드 로보틱스의 약점으로 꼽는다'로 고쳤다.
- 2차: 3절 태그 없는 문장 — '로봇–관제 표준은 이 접점을 채우지 않는다.'를 '로봇–관제 표준인 VDA 5050 은 이 접점을 범위 밖에 둔다: 3.0.0 명세는 … 다루지 않는다. [사실][^ref-031]' 한 문장으로 좁혀 근거 표준을 밝혔다.
- 2차: 4절 도입 단락 — 목록 앞에 '이 절은 판단 배치와 외부 API 를 이해하는 데 필요한 개념인 클라우드 로보틱스·계산 오프로딩·현장 클라우드·플릿 어댑터와 제어 수준·OpenAPI·AsyncAPI·웹훅·브레인리스 로봇을 정리한다.' 한 문장 단락을 두었다.
- 2차: [의견] 주체 표시 — 5절 병원 사례 마지막 문장과 7절 첫 문장 끝(태그 앞)에 '(구축자 의견)'을 넣었다. outline 의 7절 요약도 같게 고쳤다.
- 2차: 약어 첫 등장 풀이 — 분리 전 본문의 첫 등장 위치에서 ERP·MES·WMS·REST(3절 둘째 단락), SDK(3절 넷째 단락), SLAM(4절 계산 오프로딩 항목), ICT·DDS(5절 병원 사례 표와 서술), P99·JWT(6절 FogROS2-FT 문단과 인증·권한 문단), AMR(8절 Singhal 외 항목)을 풀어 썼다. 아울러 outline 의 10절 요약을 번호와 이름으로 고쳤다.
- 분량 초과 자동 분리: 41. 플랫폼 아키텍처·외부 API 본문 11,628자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,233자
