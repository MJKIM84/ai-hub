(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-05
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 41. 플랫폼 아키텍처·외부 API (K. 플랫폼 아키텍처·인프라)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-30-05/target.json

```json
{
  "run_id": "2026-09-30-05",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 114,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 41,
    "area_name": "41. 플랫폼 아키텍처·외부 API",
    "category": "K. 플랫폼 아키텍처·인프라",
    "category_letter": "K"
  },
  "topic": null,
  "track": null,
  "corrections": [],
  "budget": {
    "max_search_queries": 30,
    "max_sources_per_run": 15,
    "new_topic_pages": 1,
    "page_updates": 2,
    "max_retries": 2
  },
  "priority_reason": null,
  "priority_questions": [],
  "excluded_areas": [],
  "lifted_areas": [],
  "deferred": {
    "monthly_recheck": false,
    "weekly_review": false
  },
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=41"
}
```

### runs/2026-09-30-05/research.json

```json
{
  "run_id": "2026-09-30-05",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 41,
    "area_name": "41. 플랫폼 아키텍처·외부 API",
    "category": "K. 플랫폼 아키텍처·인프라"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 클라우드 로보틱스, 온프레미스(현장) 클라우드, OpenAPI, AsyncAPI, 웹훅, 이벤트 기반 아키텍처 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·제조 공장·물류창고·기타 현장의 아키텍처 배치 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 클라우드·현장 서버·로봇 역할 분담, 계산 오프로딩, 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, REST·이벤트·SDK 조합 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF(rmf-web API 서버·rmf_api_msgs), VDA 5050 전송 구조, OpenAPI, AsyncAPI, RoMi-H, FogROS2 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]",
    "클라우드·현장(온프레미스) 서버·로봇 사이의 계산·판단 배치를 다룬 연구와 오픈소스(클라우드 로보틱스, 계산 오프로딩, 현장 클라우드 기준 아키텍처)는 무엇이며 어떤 결과를 보고하는가? (섹션 3·6·8 겨냥)",
    "제조사 중립적인 플랫폼 기준 아키텍처(서비스 분리, 이벤트 구조, 제조사 어댑터 계층)는 Open-RMF·RoMi-H·VDA 5050 에서 어떻게 구성되는가? (섹션 6·7 겨냥)",
    "외부 시스템과 개발자에게 여는 API·웹훅·SDK 를 기계가 읽을 수 있게 기술하는 표준(OpenAPI, AsyncAPI)과 오픈소스·제품의 제공 형태(REST, 이벤트 스트림, 인증·권한)는 무엇인가? (섹션 4·6·7 겨냥)",
    "병원·제조 공장·물류창고·기타 현장(국내 포함)에서 플랫폼을 어디에 두고 무엇을 외부에 열었는지 보여 주는 사례는 무엇인가? (섹션 5 겨냥, 한국 자료 우선)",
    "클라우드 장애·네트워크 품질 저하가 역할 분담 결정에 주는 제약과 대응 방법은 무엇인가? (섹션 3·6·11 겨냥)",
    "플랫폼 아키텍처·외부 API 에서 ROP가 직접 맡을 것과 로봇 자체 지능·업무 시스템·클라우드 인프라에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Open-RMF 의 웹 API 서버(rmf-web api-server)는 Open-RMF 배치와 웹 대시보드·외부 클라이언트 사이에 REST 엔드포인트를 두고 그 정의를 서버의 /docs 경로에 OpenAPI 형식 문서로 제공하며, 기록용 데이터베이스는 tortoise-orm 으로 PostgreSQL·SQLite·MySQL·MariaDB 를 지원한다(기본값은 메모리 SQLite).",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: REST 엔드포인트와 OpenAPI 문서(/docs)로 최신 API 정의 제공, 대시보드 사용을 가능하게 함. DB 는 tortoise-orm, 기본 in-memory sqlite, 마이그레이션은 Aerich. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "rmf-web API 서버는 OpenID Connect 로 발급된 JWT 접근 토큰을 독립적으로 검증해 사용자를 식별하고, 사용자–역할–권한 그룹의 3단 구조(역할이 그룹에 대한 동작을 허용하고 자원은 그룹에 속함)로 접근을 통제하며 관리자는 모든 그룹에 모든 동작을 할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 접근 토큰은 \"a JWT that can be verified independently\"라는 전제, preferred_username 클레임으로 사용자 식별, 첫 접근 시 사용자 자동 생성, 관리자용 권한 관리 엔드포인트. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "Open-RMF 의 rmf_api_msgs 는 C++·Python 으로 된 RMF 구성 요소와 웹 인터페이스 사이를 잇는 JSON 메시지 스키마 모음으로, 작업 요청·예약, 작업 상태, 플릿 상태 스키마를 담고 스키마에서 타입 있는 데이터 모델을 생성할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1033"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: RMF 의 C++·python 구성 요소를 웹 인터페이스로 잇는 json 메시지 스키마. 작업 상태·작업 요청·플릿 상태 스키마, datamodel-code-generator 로 모델 생성 가능. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Open-RMF 핵심 구조는 모든 플릿 관리자가 예상 경로를 보고하는 중앙 교통 일정 데이터베이스와 충돌 시 플릿 관리자 간 협상을 두고, 제조사 고유 API 를 표준 인터페이스로 잇는 플릿 어댑터를 제어 수준(Full Control·Traffic Light·Read Only·No Interface)으로 나누며, 재사용 가능한 C++ API(파이썬 바인딩 포함)는 Full Control 에만 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf-core 장: 교통 일정은 지연·취소·경로 변경을 반영하는 살아 있는 데이터베이스, 충돌 통지 후 플릿 관리자 간 협상과 제3자 중재, 제어 수준 4단계. (재인용: 2026-09-30-03 등 기존 참고문헌 재사용, 이번 실행에서 원본 재열람)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 은 플릿 관제와 이동 로봇 사이의 제조사 중립 인터페이스로 MQTT 3.1.1 이상과 JSON 을 쓰고, 주제를 interfaceName/majorVersion/manufacturer/serialNumber/topic 구조(예 vda5050/v3/…/order)로 정하며 order·instantActions·state·visualization·connection·factsheet·responses·zoneSet 주제를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 3.0.0: 주제 경로에 주 버전(majorVersion)이 들어가며 order·instantActions 는 관제→로봇, state·factsheet 는 로봇→관제, connection 은 브로커·로봇→관제. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 명세는 플릿 관제–이동 로봇 통신과 무관한 인터페이스, 곧 주변 설비·기반 시설 구성 요소·외부 IT 시스템과의 인터페이스를 범위 밖으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 범위 절: \"interfaces to peripheral equipment, infrastructure components, or external IT systems\"는 다루지 않음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "OpenAPI 명세 3.1.0(2021-02-15)은 사람과 컴퓨터가 서비스의 기능을 발견·이해하게 하는 HTTP API 의 언어 중립 표준 인터페이스 기술 형식이며, 3.1.0 에서 API 가 받을 수 있는 수신 웹훅을 기술하는 webhooks 필드가 새로 들어갔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1028"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OAS 3.1.0: \"a standard, language-agnostic interface to HTTP APIs\"; OpenAPI 객체의 webhooks 필드로 API 일부로 받을 수 있는 웹훅 기술.",
      "as_of": "2021-02-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "AsyncAPI 명세 3.1.0 은 메시지 기반 API 를 기계가 읽을 수 있게 기술하는 프로토콜 중립 형식으로 MQTT·AMQP·WebSocket·Kafka·HTTP 등에 쓰이며, 채널·동작(send/receive)·메시지·서버(브로커)·프로토콜별 바인딩을 핵심 객체로 두고 Apache 2.0 라이선스로 공개된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1027"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 3.1.0: 프로토콜 중립(AMQP, MQTT, WebSockets, Kafka, STOMP, HTTP 등), 일부 내용은 OpenAPI Initiative 작업에서 가져왔다고 밝힘. 발행일은 문서에서 확인 못 함. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Ichnowski 외의 FogROS2(arXiv 2205.09778, 2023-04 개정)는 연산 능력이 제한된 로봇이 ROS 2 노드를 AWS·GCP·Azure 같은 원격 클라우드로 옮겨 실행하게 하는 ROS 2 배포판 포함 플랫폼으로, SLAM 지연 50% 감소, 파지 계획 14초→1.2초, 모션 계획 45배 가속, 영상 압축으로 이미지 전송 지연 97% 개선을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-304"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록(v2, 2023-04): FogROS1 대비 네트워크 사용 최대 3.8배 감소, 시작 시간 63% 개선, 지역·인스턴스 유형 자동 선택. 수치는 저자 실험 기준.",
      "as_of": "2023-04",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "Chen 외의 FogROS2-FT(IROS 2024)는 클라우드 제공자 장애, 네트워크 서비스 품질(QoS) 변동, 신뢰성 높은 인스턴스의 비용을 클라우드 로보틱스의 약점으로 보고, 상태 없는 로봇 서비스를 여러 클라우드에 복제해 가장 먼저 온 응답을 쓰는 방식으로 모션 계획 P99 지연을 최대 5.53배 줄이고 비용을 최대 2.2배 낮췄다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: \"automatically replicates independent stateless robotic services, routes requests to these replicas, and directs the first response back\"; 객체 검출 P99 2.0배, 의미 분할 2.1배 감소, 스팟 인스턴스 활용.",
      "as_of": "2024-12",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "독립된 두 연구(Singhal 외 2017, Brorsson 외 2025)는 모두 로봇 밖의 중앙 계산 자원(클라우드 또는 현장 클라우드)이 플릿 조율·전역 계획을 맡고 각 로봇이 국지 주행 같은 온보드 자율 기능을 유지하는 혼합 구조를 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1032",
        "ref-308"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "Singhal 외: 로봇은 이동·장애물 회피를 자율로 하고 목적지는 클라우드 전역 계획기가 줌(Rapyuta 플랫폼 비교). Brorsson 외: 기반 시설 계층·현장 클라우드·온보드 자율의 3계층.",
      "as_of": "2025-12",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "Brorsson 외(arXiv 2512.15215, 2025-12)의 RAIL 기준 아키텍처는 사내 물류 이동 로봇을 위해 설비에 단 외부 센서·계산 자원(기반 시설), 지연·연결 문제를 다루는 현장 클라우드(on-premise cloud), 로봇 온보드 자율의 세 층을 두며, 대형 상용차 제조 현장 실배치와 사용자 경험 평가로 이를 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: 대부분의 AMR 솔루션은 분산된 온보드 지능을 강조하며 기반 시설 지원형은 덜 탐구됨; \"a real-world deployment in a heavy-vehicle manufacturing environment\".",
      "as_of": "2025-12",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f13",
      "claim": "싱가포르 창이종합병원 CHART 의 RoMi-H(Robotic Middleware for Healthcare)는 OMG DDS 를 쓰는 미들웨어로 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리와 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·ICT 시스템용 API)의 네 영역으로 구성되며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다.",
      "tag": "사실",
      "source_ids": [
        "ref-937"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHART RoMi-H 페이지: 공공 의료기관 로봇 시스템 간 통신 표준화, 연구의 표준화·코드 재사용과 의료 분야 로봇 도입 가속을 목적으로 제시. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f14",
      "claim": "네이버는 로봇 안이 아니라 클라우드에서 연산·판단을 하는 브레인리스 로봇 구조의 ARC(AI-Robot-Cloud)를 이동 계획·위치 추정·작업 수행과 기반 시설 연동을 맡는 ARC brain, 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정하는 ARC eye, 웹 개발자가 로봇 서비스를 만들게 하는 웹 기반 OS 인 ARC mind 로 나누고, 제2사옥 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1025"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 네이버 로보틱스 페이지 — ARC mind 는 \"웹 개발자들이 로봇 서비스를 손쉽게 개발\"하게 함, 1784 에서 100여 대 로봇이 클라우드로 제어됨. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "MiR 은 MiR Fleet Enterprise 가 Windows Server 에서 돌며 가상화·클라우드 배치를 지원하고, ERP·MES·WMS 연동용 REST API 와 이벤트 기반 아키텍처를 갖추며, IEC 62443-4-2(SL-C 3)에 맞춰 단일 로그인·감사 기록·세분화된 사용자 권한을 제공한다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-774"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"Full featured REST-API for ERP/MES/WMS implementation\"; 이벤트 기반 구조가 네트워크 부하를 줄인다고 함. 지원 대수는 같은 페이지에 '최대 100대'와 '100대 넘는 배치' 표현이 함께 있음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f16",
      "claim": "InOrbit 개발자 문서는 로봇 데이터 조회·원격 동작·미션 추적·감사 기록용 REST·스트리밍 API, 사고 관리용 외부 발신 웹훅과 수신 API, 서비스 사용자와 역할 기반 권한에 묶인 API 키, 로봇에 넣는 Robot SDK(C++·Python)와 현장 애플리케이션 연동용 Edge SDK, 임베드 가능한 대시보드를 제공한다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1034"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Edge SDK 는 로봇마다 에이전트를 설치하지 않고 제3자·자체 현장 애플리케이션과 플랫폼을 잇게 함; Slack·PagerDuty 등 기본 연동. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f17",
      "claim": "물류창고 피킹에서 Locus Robotics 는 LocusONE 플랫폼이 API 로 창고 관리 시스템(WMS)과 연결돼 WMS 에서 주문을 받아 피킹 효율을 기준으로 최적화한 뒤 로봇 작업으로 내린다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1036"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: LocusONE 은 \"proven and reliable APIs\"로 WMS 와 연결되며 주문 수신→피킹 최적화 흐름. 기존 인프라와 분리된 전용 WiFi 망을 설치·유지한다고 함. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "물류창고",
      "flow_item": "시작 조건",
      "vendor_claim": true
    },
    {
      "id": "f18",
      "claim": "같은 Locus Robotics 자료는 피킹 완료 확인을 WMS 로 즉시 되돌려 보내고 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 같은 운영 성과 데이터를 제공한다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1036"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 확인(confirmations)을 즉시 WMS 로 전송, 관리자에게 UPH·LPH·로봇 생산성·상태 실시간 제공. 배치 위치(클라우드/현장)는 페이지에 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "물류창고",
      "flow_item": "완료·인계",
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "뉴스핌(2026-05-12) 보도에 따르면 카카오모빌리티는 로봇–인프라–사용자를 잇는 플랫폼으로 서비스 요청을 로봇 실행 단위로 바꾸는 작업 추상화, 이종 로봇이 통신하게 하는 통합 API 인 제어 인터페이스, 고장 감지 시 다른 로봇으로 작업을 넘기는 재배정, 건물 인프라와 ERP·물류 자동화 시스템을 잇는 연동 기반을 추진한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1029"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장(기사 전언): 실내 배송에서 청소·시설 안내·물류 자동화로 확장 계획, \"robots are now in the era of operations\" 취지의 발언 인용. 제목 일부만 확인.",
      "as_of": "2026-05-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "로봇신문 보도에 따르면 클로봇은 다중 로봇 통합관제 플랫폼 CROMS 가 서로 다른 제조사 로봇 50대 이상을 동시에 제어하고 승강기 연동으로 다층 건물에서 운용할 수 있으며 국내 첫 이기종 로봇 통합관제 솔루션이라고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-870"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장(기사 전언): CROMS 50대 이상 이기종 로봇 동시 관제, 승강기 연동; 하드웨어 비종속 소프트웨어 사업 강조. 제목 일부만 확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에 대해, 국지 주행·즉각적 안전 반응은 로봇에, 지연·연결에 민감한 플릿 조율·교통·설비 연동은 현장 서버(현장 클라우드)에, 무거운 계산 오프로딩과 여러 현장 집계·개발자 서비스는 클라우드에 두는 혼합 배치가 연구·오픈소스의 공통 형태이고(f4·f9·f11·f12·f14), 외부에는 동기식 REST(OpenAPI 로 기술)와 이벤트·메시지 API(AsyncAPI·웹훅), SDK 를 인증·권한 통제와 함께 여는 조합이 쓰이는 것으로 보인다(f1·f2·f7·f8·f16).",
      "tag": "추정",
      "source_ids": [
        "ref-004",
        "ref-304",
        "ref-1032",
        "ref-308",
        "ref-1025",
        "ref-762",
        "ref-1028",
        "ref-1027",
        "ref-1034"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드로 올리는 설계(f14, 벤더 주장)도 있어 배치 경계는 제품 전략에 따라 움직인다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇–관제 표준(VDA 5050)이 업무 IT 시스템·설비와의 인터페이스를 범위 밖에 두고(f6) 제조사 관제마다 자체 REST API 를 따로 내므로(f15·f17) 이종 로봇을 묶는 플랫폼의 외부 API 가 업무 시스템과 개발자가 만나는 단일 접점이 되며, 클라우드 장애·네트워크 품질 변동(f10)이 있어 판단을 어디에 두느냐가 운영 연속성을 좌우하기 때문이다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-774",
        "ref-1036",
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 근거 f6·f10·f15·f17.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 41. 플랫폼 아키텍처·외부 API 에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처(f4·f13), 작업 요청·작업 상태·플릿 상태의 기계가독 스키마(f3), REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기(f5·f7·f8), API 호출의 인증·권한(f2), 판단·데이터를 로봇·현장 서버·클라우드 중 어디에 둘지 정하는 배치 정책이다.",
      "tag": "추정",
      "source_ids": [
        "ref-004",
        "ref-937",
        "ref-1033",
        "ref-031",
        "ref-1028",
        "ref-1027",
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 분류 원문 19장의 '이종 제조사를 연결하는 ROP는 인터페이스와 실행 보장을 담당' 방향과 맞춘 해석.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "연계 대상: 분류 원문 19장 기준으로 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능(f9·f11)은 로봇 제조사에, 주문·재고 같은 업무 판단(f17)은 상위 업무 시스템(WMS·ERP)에, 클라우드 제공자 인프라와 현장 네트워크(f10·f17)는 클라우드 사업자와 42. 분산 시스템·통신·컴퓨팅 구조 영역에 속하므로, ROP 는 이들을 부르고 받는 인터페이스와 배치 결정을 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-304",
        "ref-1032",
        "ref-1036",
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. FogROS2 가 SLAM 노드를 클라우드로 옮기는 것은 로봇 내부 기능의 실행 위치 선택이며 ROP 직접 범위가 아님.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "이 영역은 현장 네트워크·연결 끊김 운영을 다루는 42. 분산 시스템·통신·컴퓨팅 구조(f10·f12), 기록 DB·감사 기록·배포를 다루는 43. 데이터·관측성·배포(f1·f16), 플릿 어댑터를 다루는 20. 로봇·제조사 관제 연동(f4·f15), VDA 5050 을 다루는 21. 상호운용 표준·적합성(f5·f6), 승강기·기반 시설 연동의 22. 설비·건물 시스템 연동(f13·f14·f20), WMS·ERP 연동의 23. 업무 시스템 연동(f15·f17·f18), API 인증·권한의 51. 인증·권한·격리(f2·f16), IEC 62443 을 다루는 52. 통신 보호·위협 관리·감사(f15), 대시보드의 37. 관제 화면·실행 기록(f1·f16), 재배정의 32. 예외 복구·재계획·업무 연속성(f19), 업체 동향의 1. 기술·시장·업체 동향(f14·f19·f20), 적용 현장인 61. 물류창고(f17)·62. 제조 공장(f12)·63. 병원·의료(f13)·67. 기타 현장(f14)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1037",
        "ref-308",
        "ref-762",
        "ref-1034",
        "ref-004",
        "ref-774",
        "ref-031",
        "ref-937",
        "ref-1025",
        "ref-870",
        "ref-1036",
        "ref-1029"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 근거 finding 은 claim 안에 병기.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/rmf-core.md",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 저장소 main 브랜치 명세(3.0.0). 플릿 관제–이동 로봇 인터페이스의 MQTT 주제 구조와 범위를 정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web/packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 API 서버의 REST·OpenAPI 문서, OpenID Connect·JWT 인증, 역할·그룹 권한, tortoise-orm 데이터베이스 설정을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/packages/api-server/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-304",
      "org": "Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv)",
      "title": "FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2",
      "published": "2022-05",
      "url": "https://arxiv.org/abs/2205.09778",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 노드를 클라우드·포그로 옮겨 실행하는 플랫폼과 SLAM·파지·모션 계획 가속 결과(초록, 2023-04 개정판).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1025",
      "org": "NAVER Corp.",
      "title": "로보틱스 l NAVER Corp.",
      "published": null,
      "url": "https://www.navercorp.com/tech/robotics",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "브레인리스 로봇 구조의 ARC(brain·eye·mind)와 1784 사옥의 클라우드 로봇 운영을 소개하는 회사 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-937",
      "org": "Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology)",
      "title": "ROMI-H",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "싱가포르 공공 의료기관용 로봇 미들웨어 RoMi-H 의 목적, DDS 기반 네 영역 구조, 발표·출범 일정을 설명하는 병원 연구센터 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1027",
      "org": "AsyncAPI Initiative",
      "title": "AsyncAPI Specification 3.1.0",
      "published": null,
      "url": "https://www.asyncapi.com/docs/reference/specification/v3.1.0",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "메시지 기반 API 를 기계가독 형식으로 기술하는 프로토콜 중립 명세(채널·동작·메시지·서버·바인딩).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1028",
      "org": "OpenAPI Initiative",
      "title": "OpenAPI Specification v3.1.0",
      "published": "2021-02-15",
      "url": "https://spec.openapis.org/oas/v3.1.0",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "HTTP API 의 언어 중립 인터페이스 기술 표준. 3.1.0 에서 webhooks 필드를 더했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1029",
      "org": "뉴스핌",
      "title": "카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 … (제목 일부만 확인)",
      "published": "2026-05-12",
      "url": "https://www.newspim.com/news/view/20260512001077",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "카카오모빌리티의 로봇 플랫폼 구상(작업 추상화, 통합 제어 인터페이스, 재배정, 건물·업무 시스템 연동)을 전하는 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-870",
      "org": "로봇신문",
      "title": "[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 … (제목 일부만 확인)",
      "published": null,
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=43274",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "클로봇의 자율주행 소프트웨어와 이기종 로봇 통합관제 플랫폼 CROMS 를 소개하는 기업 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-308",
      "org": "Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv)",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "기반 시설·현장 클라우드·온보드 자율의 3계층 기준 아키텍처 RAIL 과 대형 상용차 제조 현장 실배치(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1032",
      "org": "Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv)",
      "title": "Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform",
      "published": "2017-06",
      "url": "https://arxiv.org/abs/1706.08931",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "공장·창고 AMR 플릿에서 클라우드 전역 계획기와 로봇 국지 주행을 나누고 분산 ROS 와 Rapyuta 클라우드 플랫폼을 비교한 연구(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1033",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "RMF 구성 요소와 웹 인터페이스를 잇는 JSON 메시지 스키마(작업 요청·작업 상태·플릿 상태) 저장소.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1034",
      "org": "InOrbit",
      "title": "Contents — InOrbit Developer Portal",
      "published": null,
      "url": "https://developer.inorbit.ai/docs",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇 운영 플랫폼의 REST·스트리밍 API, 웹훅, API 키, Robot SDK·Edge SDK, 임베드, 커넥터를 설명하는 개발자 문서.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-774",
      "org": "Mobile Industrial Robots (MiR)",
      "title": "MiR Fleet",
      "published": null,
      "url": "https://mobile-industrial-robots.com/products/software/mir-fleet",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "MiR Fleet Enterprise 의 배치 환경, ERP·MES·WMS 용 REST API, 이벤트 기반 구조, IEC 62443-4-2 정합을 소개하는 제품 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1036",
      "org": "Locus Robotics",
      "title": "Seamless Integrations with LocusOne Robotics",
      "published": null,
      "url": "https://locusrobotics.com/locusone/automated-warehouse-software/integrations",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LocusONE 의 WMS API 연동(주문 수신·확인 회신), 전용 WiFi 망, 운영 성과 데이터를 소개하는 제품 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1037",
      "org": "Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv)",
      "title": "FogROS2-FT: Fault Tolerant Cloud Robotics",
      "published": "2024-12",
      "url": "https://arxiv.org/abs/2412.05408",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "상태 없는 로봇 서비스를 여러 클라우드에 복제해 장애·QoS 변동·비용 문제를 줄이는 방법과 P99 지연·비용 결과(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "섹션 3: f22(업무 시스템 인터페이스가 로봇–관제 표준 밖이고 클라우드 장애가 배치를 좌우), f21(핵심 질문 답, 추정) / 섹션 4: 클라우드 로보틱스·오프로딩 f9, 현장 클라우드 f12, OpenAPI·웹훅 f7, AsyncAPI f8, 플릿 어댑터·제어 수준 f4 / 섹션 5: 병원 — f13(창이종합병원 RoMi-H), 제조 공장 — f12(대형 상용차 제조 현장 RAIL), 물류창고 — f17(시작 조건: WMS 주문 수신)·f18(완료·인계: 확인 회신, 벤더 주장 병기), 기타 — f14(네이버 1784 사옥 ARC, 벤더 주장 병기). 여섯 항목 중 제약·예외 근거가 사례별로 부족함을 명시 / 섹션 6: 역할 분담 f11(교차 확인)·f12·f14, 계산 오프로딩 f9, 다중 클라우드 장애 대응 f10, 제조사 중립 어댑터 계층 f4·f13, REST·이벤트·SDK 조합 f1·f5·f16, 인증·권한 f2, 제품 사례 f15·f19·f20(벤더 주장 병기) / 섹션 7: Open-RMF f1~f4, VDA 5050 f5·f6, OpenAPI f7, AsyncAPI f8, RoMi-H f13, FogROS2 f9·f10 / 섹션 8: f9~f12 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 42. 분산 시스템·통신·컴퓨팅 구조 페이지에 f10·f12 반영, 20. 로봇·제조사 관제 연동 페이지에 f15·f16 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "OpenAPI 명세",
      "term_en": "OpenAPI Specification (OAS)",
      "definition": "HTTP API 의 경로·요청·응답·보안 방식을 사람과 컴퓨터가 함께 읽을 수 있게 기술하는 언어 중립 표준 형식으로, 3.1.0 부터 웹훅도 기술한다."
    },
    {
      "term_ko": "AsyncAPI 명세",
      "term_en": "AsyncAPI Specification",
      "definition": "MQTT·AMQP·WebSocket·Kafka 같은 메시지 기반 API 의 채널·동작·메시지·브로커를 기계가독 형식으로 기술하는 프로토콜 중립 명세다."
    },
    {
      "term_ko": "웹훅",
      "term_en": "Webhook",
      "definition": "어떤 사건이 일어났을 때 서비스가 미리 등록된 외부 URL 로 HTTP 요청을 보내 알리는 방식의 이벤트 전달 인터페이스다."
    },
    {
      "term_ko": "클라우드 로보틱스",
      "term_en": "Cloud Robotics",
      "definition": "로봇이 인터넷으로 연결된 원격 계산·저장 자원에 계산이나 데이터를 맡겨 온보드 능력의 한계를 보완하는 구조와 연구 분야다."
    }
  ],
  "open_questions_new": [
    "네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드나 5G 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f14 | 종류: 일반",
    "로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 57. 자산·소프트웨어 수명주기 관리 | 근거: f5 | 종류: 일반",
    "로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반",
    "국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 1,
    "unverified": [
      "f9 FogROS2 모션 계획 가속 배수: arXiv 개정판 초록은 45배, 검색 요약의 ICRA 2023 판 서술은 28배로 보여 판에 따라 다를 수 있음(ICRA 카메라 레디 PDF 는 열지 않음)",
      "f9·f10·f11·f12 는 논문 초록 기준이며 본문 실험 조건 미확인",
      "f14 네이버 1784 로봇 대수: 회사 페이지는 100여 대, 검색 요약의 기사 문구는 40여 대로 기준 시점이 다를 수 있으나 기사 원문을 열지 않아 출처 충돌로 확정하지 않음",
      "f14 5G 특화망 사용은 검색 요약에만 나오고 ITDaily 기사 원문은 ECONNRESET 으로 열지 못해 넣지 않음",
      "f15 MiR 페이지 안에서 지원 대수 표현('최대 100대'와 '100대 넘는 배치')이 엇갈림",
      "ref-1029·ref-870 기사 제목 전체 미확인, ref-870 발행일 미확인",
      "ref-1027 AsyncAPI 3.1.0 발행일 미확인",
      "Kehoe 외 클라우드 로보틱스 조사 논문(IEEE T-ASE 2015)은 PDF 본문 추출 실패·eScholarship 빈 페이지로 넣지 않음",
      "AWS IoT RoboRunner 의 현재 서비스 상태(종료 여부)는 확인하지 못해 넣지 않음",
      "MiR Fleet Enterprise 문서 PDF 는 크기 초과로 열지 못함",
      "국내 클라우드 로봇 참조 구조 표준(TTA·KS)은 검색 1회에서 찾지 못함"
    ],
    "scope_violations": [
      "f9: FogROS2 의 SLAM·파지 계획 오프로딩은 로봇 자체 지능·제어 기능의 실행 위치 선택이므로 배치 방식의 근거로만 쓰고 ROP 직접 범위로 서술하지 않도록 f24 에서 구분함",
      "f11: 국지 주행·장애물 회피는 로봇 자체 지능(연계 대상)으로, 전역 조율만 이 영역 근거로 씀",
      "f14: 네이버 ARC 는 위치 추정·이동 계획까지 클라우드에 두어 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례이며 원문의 '경계는 제품 전략에 따라 이동할 수 있다'는 문장에 해당함",
      "f17·f18: 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽이며 ROP 는 연동 인터페이스만 다룸",
      "f24: 로봇 자체 지능·업무 시스템·클라우드 인프라를 '연계 대상: '으로 표시함"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-762~ref-1037, 예약 구간 안)로 출처 상한에 도달해 더 넣지 못했다. 재사용 2건(ref-004·ref-031 은 github_raw 로 다시 열었다; 참고문헌 목록 전체가 입력에 없어 ref-004 의 값은 규칙 파일 예시, ref-031 의 값은 같은 날 이전 브리프 2026-09-30-04 의 출처 표를 따랐다). 원문 열람: 17건 모두 열었다(webfetch 12건, github_raw 5건). 논문은 초록 페이지다. 교차 확인 1건(f11, 두 arXiv 논문이라 신뢰도 medium). 벤더 문서·기사만 근거로 한 finding(f14~f20)은 모두 vendor_claim: true·태그 추정·'벤더 주장' 첫머리로 냈다. 분류 원문 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에는 f21 로 답했고 결론은 '로봇–현장 서버–클라우드 혼합 배치 + REST·이벤트 API·웹훅·SDK 를 인증·권한과 함께 여는 조합'이라는 추정이다. 현장 유형 사례는 병원(f13)·제조 공장(f12)·물류창고(f17·f18, 벤더 주장)·기타(f14, 사무 건물, 벤더 주장)이며 상업 시설·가정·실외 사례는 찾지 못했다. 국내 자료는 네이버(ref-1025)·뉴스핌(ref-1029)·로봇신문(ref-870) 세 건이고 국내 표준은 찾지 못했다. L. AI·학습 기술 관련 finding 은 없다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(네이버 ARC eye 의 디지털 트윈 언급은 위치 추정용 현재 상태 표현으로만 인용). 용어집에 이미 있는 포그 컴퓨팅·브레인리스 로봇·플릿 어댑터·플릿 제어 수준·MQTT·JSON 스키마·의미적 버전 관리·멱등성 키는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### runs/2026-09-30-05/verification.json

```json
{
  "run_id": "2026-09-30-05",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. raw README 재열람: API 엔드포인트·웹 대시보드 사용, /docs 경로와 공개 문서 사이트(open-rmf.github.io/rmf-web/docs/api-server)의 API 정의, TortoiseORM 기반 PostgreSQL·SQLite·MySQL·MariaDB, 기본 메모리 SQLite, Aerich 마이그레이션은 확인. 그러나 README 에 'REST'·'OpenAPI' 라는 말이 없고 evidence_excerpt('REST 엔드포인트와 OpenAPI 문서')가 원문과 다르다. 발행일 미확인."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(ref-762 raw README). OpenID Connect, 독립 검증 가능한 JWT 전제, preferred_username 클레임, 첫 로그인 시 권한 없는 사용자 자동 생성, 관리자는 모든 그룹에 모든 동작 가능. 다만 README 는 권한을 '역할·동작·권한 그룹' 세 값으로 정한다고 적으므로 '사용자–역할–권한 그룹 3단 구조' 표현은 고친다(required_fixes). 인용 1회."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. README 는 'C++·python 구성 요소와 웹 인터페이스를 잇는 json 메시지 스키마 모음'과 datamodel-code-generator 모델 생성을 적고 스키마 이름은 task_state 만 든다. 작업 요청(task_request·robot_task_request)과 플릿 상태(fleet_state.json, raw 열람으로 존재 확인) 스키마는 저장소 schemas 폴더 기준이다. 발행일 미확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(입력 원문 data/source_texts/ref-004.txt). 살아 있는 교통 일정 DB, 모든 플릿 관리자의 예상 경로 보고, 충돌 통지 후 협상과 제3자 판정, 4개 제어 수준, 재사용 C++ API(파이썬 바인딩)는 Full Control 용이며 Read Only 는 예비 ROS 2 메시지 API, Traffic Light 는 재사용 API 없음. 책 장의 발행일 미확인이며 현재 Open-RMF 구현과 다를 수 있다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(입력 원문 ref-031, 3.0.0). MQTT 3.1.1 최소, JSON, 주제 이름 8종. 단, interfaceName/majorVersion/… 주제 계층은 '로컬 브로커용 제안'이며 클라우드 브로커에서는 조정될 수 있다고 명세가 적으므로 '정하며'를 고친다. visualization·zoneSet·responses 는 선택 주제. 명세 발행일 미확인(3.0.0 판 기준)."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(입력 원문 ref-031 2장 Scope). 주변 설비·기반 시설 구성 요소·외부 IT 시스템 인터페이스 제외 문구 일치. 인용 1회."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(spec.openapis.org, 2021-02-15). 정의 문구와 webhooks 필드('API 일부로 받을 수 있는 수신 웹훅') 확인. '3.1.0 에서 새로 들어갔다'는 열람한 명세 본문에서 확인하지 못해 삭제 지시."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(asyncapi.com 3.1.0). 프로토콜 중립, 채널·동작(send/receive)·메시지·서버·바인딩, Apache 2.0, OpenAPI Initiative 작업 차용 문구 확인. 발행일 미확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv 초록). v1 2022-05-19, v2 2022-11-27, v3 2023-04-24. 수치(SLAM 50%, 파지 14→1.2초, 모션 계획 45배, 영상 전송 97%)는 v3 초록 기준 저자 보고이며 단일 출처. evidence_excerpt 의 'v2, 2023-04'는 v3 이므로 기준판 표기를 고친다. ICRA 판 28배 표기와의 차이는 미확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv 2412.05408, 2024-12-06 제출, IROS 2024). 복제·라우팅·첫 응답 방식, 모션 계획 P99 5.53배·비용 2.2배, 객체 검출 2.0배, 의미 분할 2.1배, 스팟 인스턴스 확인. 수치는 저자 보고."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "교차 확인(ref-1032 초록 + ref-308 초록·HTML 본문, 발행 주체 다름). 두 연구 모두 중앙 계산 자원이 플릿 조율·전역 계획을 맡는다. 로봇 쪽 역할은 연구마다 다르다: Singhal 외는 로봇이 이동·장애물 회피를 자율로 하고, Brorsson 외 본문은 현장 클라우드가 작업 일정과 궤적까지 계산하고 로봇은 궤적 추종과 필요 시 온보드 자율을 맡는다. '국지 주행 같은' 표현은 좁혀 쓰게 지시."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv 2512.15215, 2025-12-17 제출). 초록은 기반 시설 감지·현장 클라우드·온보드 자율의 기준 아키텍처, 대형 상용차 제조 현장 실배치, 사용자 경험 평가를 적고 HTML 본문이 RAIL 이라는 이름을 쓴다. 현장 클라우드를 '지연·연결 문제를 다루는' 층이라 한 수식어는 초록·본문에서 확인되지 않아(본문은 연결 장애 대비를 온보드 자율 쪽에 둔다) 삭제 지시."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(CGH CHART 페이지). OMG DDS, 기계·제어·중앙·통합 네 영역, 2018-07 국가 보건 IT 서밋 발표, 2019-10-31 ROSCon 2019 출범 확인. 발행일 미확인. 특정 병원의 배치 결과가 아니라 공공 의료기관용 미들웨어 구조임에 유의."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(네이버 로보틱스 페이지). ARC brain·eye·mind 역할과 '100여 대의 로봇이 클라우드로 제어' 문구 확인. 벤더 주장 [추정] 유지. 기사 문구(40여 대)와의 차이는 기사 원문 미열람으로 미확인."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(MiR 제품 페이지). Windows Server·가상화·클라우드, ERP/MES/WMS 용 REST API, 이벤트 기반 구조, IEC 62443-4-2(SL-C 3) 정합, SSO·감사 기록·세분 권한 확인. 같은 페이지 안에서 '최대 100대'와 '100대 넘는 배치' 표현이 엇갈린다. 벤더 주장 [추정] 유지."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(InOrbit 개발자 문서). REST·스트리밍 API, 사고 알림 웹훅과 수신 API, 서비스 사용자·역할 기반 API 키, Robot SDK(C++·Python), 로봇별 에이전트 없는 Edge SDK, 임베드, Slack·PagerDuty 등 연동 확인. 벤더 주장 [추정] 유지."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(Locus 통합 페이지). WMS 와 API 연결, 주문 수신·피킹 효율 최적화, 기존망과 분리된 전용 WiFi 설치·유지 확인. 배치 위치(클라우드/현장) 언급 없음. 벤더 주장 [추정] 유지."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(같은 Locus 페이지). 확인을 WMS 로 실시간 회신, UPH·LPH·로봇·작업자 생산성 데이터 제공 확인. 벤더 주장 [추정] 유지."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(뉴스핌 기사). 태스크 추상화, 통합 제어 인터페이스(표준 API), 재할당, 통합 연동 백본(건물·ERP·물류 자동화), 청소·안내·물류로 확장 확인. 기사 페이지 표기 발행일은 2026-05-13 이며 제목 전체는 \"카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다\"이다(발행일·제목 정정 지시). 벤더 주장(기사 전언) [추정] 유지."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(로봇신문, 2025-11-09 입력, 이정환 기자). '50대 이상 로봇을 동시 제어', 엘리베이터 탑승 기능, '국내 첫 이기종 로봇 통합관제 솔루션' 확인. 기사는 '50대 이상'과 '이기종'을 따로 적으므로 '서로 다른 제조사 로봇 50대 이상'으로 합친 표현은 고친다. 제목 전체·발행일 정정 지시. 벤더 주장(기사 전언) [추정] 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정] 유지. 근거 finding 은 대부분 확인됐으나 f1 이 강등됐으므로 'REST(OpenAPI 로 기술)' 근거에서 f1 을 빼고 f7·f15·f16 으로 한정한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정] 유지. 근거 f6·f10·f15·f17 모두 확인. f15·f17 은 벤더 주장이므로 '제조사 관제마다 자체 REST API 를 낸다'는 벤더 자료 기준임을 밝힌다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정] 유지. 원문 19장의 '인터페이스와 실행 보장' 방향과 맞다. 근거 finding 확인."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정] 유지. 다만 42. 분산 시스템·통신·컴퓨팅 구조는 외부 연계 대상이 아니라 ROP 의 다른 세부영역이므로, 클라우드 제공자 인프라(외부 연계)와 현장 네트워크 설계(42번 영역에서 다룸)를 나눠 쓰게 지시."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 [추정] 유지. 연결 대상 영역 번호·이름이 부록 A 와 일치. f1 을 43. 데이터·관측성·배포 근거로 쓸 때 강등된 f1 의 README 확인 범위(DB 설정)만 쓴다."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "참고문헌 id 충돌: 이번 브리프의 ref-304(FogROS2)·ref-937(RoMi-H)·ref-1027(AsyncAPI)·ref-1028(OpenAPI)·ref-308(Brorsson 외)·ref-1032(Singhal 외)·ref-1033(rmf_api_msgs)·ref-774(MiR)·ref-1036(Locus)·ref-1037(FogROS2-FT)가 같은 날 이전 브리프 2026-09-30-03·2026-09-30-04 에서 다른 출처(엔지니어링데일리, IMDF Unit·Glossary, OGC IMDF, osmAG, osmAG-LLM, IEEE 1873, 국토지리정보원, Narayana 외, Stefanini 외)에 이미 쓰였다. URL 이 달라 퍼블리셔의 같은 URL 병합으로 풀리지 않으므로 게시 전 id 재배정 확인이 필요하다(스토리텔러가 고칠 사항은 아님)",
      "42. 분산 시스템·통신·컴퓨팅 구조 페이지(게시됨, 옛 11번 영역 '클라우드·현장 서버·로봇의 역할 분담' 본문 포함)와 f9·f10·f11·f12 의 역할 분담·장애 대응 내용이 겹칠 수 있다. 입력은 요약본뿐이라 기존 각주와의 중복은 확인하지 못했다",
      "f4(Open-RMF 교통 일정·플릿 어댑터 제어 수준)는 용어집 '플릿 어댑터'·'플릿 제어 수준'·'오픈 RMF' 정의와 같은 내용이며 ref-004 는 기존 각주를 재사용한다",
      "f14(네이버 1784 사옥)는 2026-09-30-04 브리프 f18(ref-956, 로봇 친화형 건축물 인증)과 같은 건물을 다른 측면으로 다룬다. 충돌은 없다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f1: [사실] → [추정]으로 강등하고, 'REST'·'OpenAPI 형식' 표현을 빼고 README 가 적은 범위(웹 대시보드가 쓰는 API 엔드포인트, /docs 경로와 공개 문서 사이트의 API 정의, TortoiseORM 기반 PostgreSQL·SQLite·MySQL·MariaDB 와 기본 메모리 SQLite)로만 쓴다 — ref-762 README 에 REST·OpenAPI 라는 말이 없고 브리프 발췌가 원문과 다르다.",
    "f2: '사용자–역할–권한 그룹의 3단 구조' 를 '역할·동작·권한 그룹 세 값으로 권한을 정하는 구조' 로 고친다 — ref-762 README 의 표현이다.",
    "f3: 작업 요청·플릿 상태 스키마를 쓸 때 README 가 이름으로 드는 것은 작업 상태(task_state)뿐이고 나머지는 저장소 스키마 파일 기준임을 본문 서술로 밝힌다.",
    "f5: 주제 계층 interfaceName/majorVersion/manufacturer/serialNumber/topic 을 '정한다'가 아니라 '로컬 브로커용으로 제안하며 클라우드 브로커에서는 조정될 수 있고, 주제 이름은 필수다'로 고치고, visualization·zoneSet·responses 는 선택 주제임을 쓰며 기준 판(3.0.0)을 밝힌다 — ref-031 4.2·4.3절.",
    "f7: '3.1.0 에서 webhooks 필드가 새로 들어갔다'를 '3.1.0 에는 API 가 받을 수 있는 수신 웹훅을 기술하는 webhooks 필드가 있다'로 고친다 — 열람한 명세 본문에 도입 판 언급이 없다. 용어집 후보 'OpenAPI 명세' 정의의 '3.1.0 부터'도 같은 이유로 '3.1.0 은'으로 고친다.",
    "f9: 기준판 표기를 'arXiv v3(2023-04-24) 초록 기준, 저자 보고'로 쓰고, 모션 계획 가속 배수는 판에 따라 다를 수 있다(미확인)고 병기한다 — 브리프 발췌의 'v2, 2023-04'는 v3 이다.",
    "f11: 로봇 쪽 역할을 '국지 주행 같은 온보드 자율 기능' 대신 '온보드 실행·자율 기능(범위는 연구마다 다름)'으로 좁혀 쓴다 — ref-308 본문은 현장 클라우드가 궤적까지 계산하고 로봇은 추종과 필요 시 온보드 자율을 맡는다고 적어 ref-1032 와 로봇 쪽 범위가 다르다.",
    "f12: 현장 클라우드 앞의 수식어 '지연·연결 문제를 다루는'을 삭제한다 — ref-308 초록·본문에서 확인되지 않는다.",
    "f19·ref-1029: 발행일을 기사 페이지 표기인 2026-05-13 으로, 제목을 \"카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다\"로 고치고 '(제목 일부만 확인)'을 뗀다. f19 의 기준일도 같게 쓴다.",
    "f20·ref-870: 제목을 \"[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막\"으로, 발행일·기준일을 2025-11-09 로 고치고, '서로 다른 제조사 로봇 50대 이상'을 '50대 이상 로봇 동시 제어'와 '국내 첫 이기종 로봇 통합관제 솔루션이라는 주장'으로 나눠 쓴다 — 기사 원문이 두 내용을 따로 적는다.",
    "f15: 지원 대수를 본문에 쓰면 같은 페이지의 '최대 100대'와 '100대 넘는 배치' 두 표현을 모두 [추정] 벤더 주장으로 제시하고 한쪽을 고르지 않는다.",
    "f21: 'REST(OpenAPI 로 기술)' 부분의 근거에서 f1 을 빼고 f7·f15·f16 으로 한정한다 — f1 이 강등됐다.",
    "f24: 42. 분산 시스템·통신·컴퓨팅 구조를 외부 연계 대상으로 쓰지 않는다. 클라우드 제공자 인프라는 외부 연계 대상, 현장 네트워크 설계는 42. 분산 시스템·통신·컴퓨팅 구조 영역에서 다룬다고 나눠 쓴다 — 42번은 ROP 의 세부영역이다.",
    "5·6·9절 f14: 네이버 ARC 사례는 [추정] 벤더 주장으로 쓰고, 위치 추정·이동 계획을 클라우드에 두는 것은 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 서술한다(ROP 직접 범위로 쓰지 않는다).",
    "5절: 병원 사례(f13)는 특정 병원의 배치 결과가 아니라 공공 의료기관용 미들웨어 구조임을 밝히고, 사례마다 여섯 항목 가운데 근거가 없는 칸은 채우지 않고 '미확인'으로 둔다.",
    "11절 열린 질문 1: '클라우드나 5G 연결' 에서 '5G'를 뺀다 — 근거 f14 에 5G 언급이 없다(5G 는 브리프가 원문 미열람으로 제외했다).",
    "13절: ref-004·ref-031 은 기존 참고문헌 페이지(docs/references/ref-004.md, ref-031.md)의 '각주 형식' 줄을 그대로 쓰고 새 각주를 만들지 않는다."
  ],
  "confidence": "low",
  "verification_note": "판정: 1차 조건부 승인. 확인 24건, 미확인 1건, 교차 확인 1건(f11). 강등: f1 사실 → 추정(README 에 REST·OpenAPI 표현 없음). 원문 미열람 출처: 없음(17건 모두 열람·대조; ref-004·ref-031 은 입력 원문 텍스트, 논문은 arXiv 초록 기준이고 ref-308 은 HTML 본문도 확인). 주의: 사실 finding 은 f11 을 빼면 모두 단일 출처이고, 핵심 결론(판단 배치의 혼합 구조, 외부 API 조합, 직접 범위)은 종합 [추정]이며, 제품·국내 사례(f14~f20)는 벤더 주장 또는 기사 전언이다. FogROS2·FogROS2-FT 수치는 저자 보고다. 상업 시설·가정·실외 사례와 국내 표준은 찾지 못했다. 이번 브리프의 신규 참고문헌 id 10건이 같은 날 이전 브리프(2026-09-30-03·04)의 다른 출처 id 와 겹치므로 게시 전 id 재배정 확인이 필요하다. 검증 검색 1회(누적 18/30), 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-05/pages.json

```json
{
  "run_id": "2026-09-30-05",
  "outline": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 만나는 단일 접점이 되고, 판단 배치가 운영 연속성을 좌우한다. [추정][^ref-031][^ref-1037]",
      "planned_findings": [
        "f22",
        "f6",
        "f15",
        "f17",
        "f10",
        "f21"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "클라우드 로보틱스·계산 오프로딩·현장 클라우드·플릿 어댑터와 제어 수준·OpenAPI·AsyncAPI·웹훅·브레인리스 로봇을 정리한다. [사실][^ref-304][^ref-1028]",
      "planned_findings": [
        "f9",
        "f12",
        "f4",
        "f7",
        "f8",
        "f16",
        "f14"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2300,
      "summary": "병원(RoMi-H 구조)·제조 공장(RAIL)·물류창고(Locus 피킹, 벤더 주장)·기타(네이버 1784, 벤더 주장) 네 사례를 여섯 항목으로 정리하고 근거 없는 칸은 미확인으로 둔다. [추정][^ref-937][^ref-1036]",
      "planned_findings": [
        "f13",
        "f12",
        "f17",
        "f18",
        "f14"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2700,
      "summary": "로봇·현장 서버·클라우드 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, REST·이벤트·웹훅·SDK 외부 API 가 대표 접근법이다. [추정][^ref-1032][^ref-308][^ref-004]",
      "planned_findings": [
        "f11",
        "f12",
        "f14",
        "f21",
        "f9",
        "f10",
        "f4",
        "f13",
        "f1",
        "f2",
        "f3",
        "f5",
        "f8",
        "f15",
        "f16",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1000,
      "summary": "Open-RMF(핵심·rmf-web·rmf_api_msgs), VDA 5050 3.0.0, OpenAPI 3.1.0, AsyncAPI 3.1.0, RoMi-H, FogROS2 계열을 이 영역과의 관계로 정리한다. [의견][^ref-004][^ref-031]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f13"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 800,
      "summary": "FogROS2·FogROS2-FT·Singhal 외·Brorsson 외 네 연구가 판단 배치와 장애 대응의 근거다. [사실][^ref-304][^ref-308]",
      "planned_findings": [
        "f9",
        "f10",
        "f11",
        "f12"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1200,
      "summary": "ROP 는 제조사 중립 기준 아키텍처·기계가독 스키마·API 명세와 버전·인증·권한·배치 정책을 맡고, 로봇 자체 지능·업무 판단·클라우드 제공자 인프라는 연계 대상으로 본다. [추정][^ref-004][^ref-762]",
      "planned_findings": [
        "f23",
        "f24",
        "f14"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1400,
      "summary": "42·43·20·21·22·23·51·52·37·32·1번 영역과 61·62·63·67번 현장 유형 영역으로 이어진다. [추정][^ref-1037][^ref-004]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "클라우드 단절 시 동작 범위, 외부 API 버전 관리 정책, 웹훅 전달 보장, 국내 참조 구조 표준 네 질문을 연다.",
      "planned_findings": []
    }
  ],
  "pages": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 판단 배치 혼합 구조, 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건. 조건부 승인 수정 17건 이행"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"6. 대표 접근법과 기술\" 절(3,227자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"4. 핵심 개념과 용어\" 절(964자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(954자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(867자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"8. 대표 연구와 자료\" 절(796자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"3. 왜 중요한가\" 절(619자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area41-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"11. 열린 질문\" 절(571자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 41. 플랫폼 아키텍처·외부 API | 섹션 3~11 신규 작성(로봇·현장 서버·클라우드 혼합 배치, REST·이벤트·웹훅·SDK 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건), 조건부 승인 수정 17건 이행 | run 2026-09-30-05",
  "index_updates": {
    "home_recent": "2026-09-30 — 41. 플랫폼 아키텍처·외부 API: 판단 배치(로봇·현장 서버·클라우드)와 외부 API 조합(REST·이벤트·웹훅·SDK), 병원·제조 공장·물류창고·기타 적용 사례로 3~11절 신규 작성",
    "category_recent": "2026-09-30 — 41. 플랫폼 아키텍처·외부 API: 섹션 3~11 신규 작성(혼합 배치·계산 오프로딩·다중 클라우드 장애 대응·제조사 어댑터 계층·외부 API 와 인증·권한, 적용 사례 4건)",
    "area_recent": "2026-09-30 — 41. 플랫폼 아키텍처·외부 API: 영역 심화로 섹션 3~11 신규 작성, 신뢰도 low(핵심 결론은 종합 추정, 제품·국내 사례는 벤더 주장)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "openapi-specification",
      "term_ko": "OpenAPI 명세",
      "term_en": "OpenAPI Specification (OAS)",
      "definition": "HTTP API 의 경로·요청·응답·보안 방식을 사람과 컴퓨터가 함께 읽을 수 있게 기술하는 언어 중립 표준 형식으로, 3.1.0 은 웹훅도 기술한다.",
      "description": "OpenAPI 명세 3.1.0(2021-02-15)은 API 가 받을 수 있는 수신 웹훅을 기술하는 webhooks 필드를 둔다. 플랫폼이 외부에 여는 동기식 REST API 를 기계가 읽을 수 있게 문서화할 때 쓴다.",
      "related_areas": [
        41,
        23
      ],
      "sources": [
        "ref-1028"
      ]
    },
    {
      "action": "new",
      "slug": "asyncapi-specification",
      "term_ko": "AsyncAPI 명세",
      "term_en": "AsyncAPI Specification",
      "definition": "MQTT·AMQP·WebSocket·Kafka 같은 메시지 기반 API 의 채널·동작·메시지·브로커를 기계가독 형식으로 기술하는 프로토콜 중립 명세다.",
      "description": "3.1.0 은 채널·동작(send/receive)·메시지·서버·프로토콜별 바인딩을 핵심 객체로 두며 Apache 2.0 라이선스로 공개된다.",
      "related_areas": [
        41,
        21
      ],
      "sources": [
        "ref-1027"
      ]
    },
    {
      "action": "new",
      "slug": "webhook",
      "term_ko": "웹훅",
      "term_en": "Webhook",
      "definition": "어떤 사건이 일어났을 때 서비스가 미리 등록된 외부 URL 로 HTTP 요청을 보내 알리는 방식의 이벤트 전달 인터페이스다.",
      "description": "OpenAPI 3.1.0 은 API 가 받을 수 있는 수신 웹훅을 기술하는 필드를 두고, 로봇 운영 플랫폼 InOrbit 은 사고 관리용 외부 발신 웹훅을 제공한다고 적는다(벤더 주장).",
      "related_areas": [
        41,
        37
      ],
      "sources": [
        "ref-1028",
        "ref-1034"
      ]
    },
    {
      "action": "new",
      "slug": "cloud-robotics",
      "term_ko": "클라우드 로보틱스",
      "term_en": "Cloud Robotics",
      "definition": "로봇이 인터넷으로 연결된 원격 계산·저장 자원에 계산이나 데이터를 맡겨 온보드 능력의 한계를 보완하는 구조와 연구 분야다.",
      "description": "FogROS2 는 ROS 2 노드를 원격 클라우드로 옮겨 실행하게 하고, 클라우드 전역 계획기와 로봇 자율 이동을 나누는 플릿 관리 구조 연구도 있다.",
      "related_areas": [
        41,
        42
      ],
      "sources": [
        "ref-304",
        "ref-1032"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 저장소 main 브랜치 명세(3.0.0). 플릿 관제–이동 로봇 인터페이스의 MQTT 주제 구조와 범위를 정한다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web/packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 API 서버의 API 엔드포인트와 /docs API 정의, OpenID Connect·JWT 인증, 역할·동작·권한 그룹 권한, TortoiseORM 데이터베이스 설정을 설명한다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-304",
      "org": "Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv)",
      "title": "FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2",
      "published": "2022-05",
      "url": "https://arxiv.org/abs/2205.09778",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 노드를 클라우드·포그로 옮겨 실행하는 플랫폼과 SLAM·파지·모션 계획 가속 결과(초록, v3 2023-04-24 기준 저자 보고).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1025",
      "org": "NAVER Corp.",
      "title": "로보틱스 l NAVER Corp.",
      "published": null,
      "url": "https://www.navercorp.com/tech/robotics",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "브레인리스 로봇 구조의 ARC(brain·eye·mind)와 1784 사옥의 클라우드 로봇 운영을 소개하는 회사 페이지.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-937",
      "org": "Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology)",
      "title": "ROMI-H",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "싱가포르 공공 의료기관용 로봇 미들웨어 RoMi-H 의 목적, DDS 기반 네 영역 구조, 발표·출범 일정을 설명하는 병원 연구센터 페이지.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1027",
      "org": "AsyncAPI Initiative",
      "title": "AsyncAPI Specification 3.1.0",
      "published": null,
      "url": "https://www.asyncapi.com/docs/reference/specification/v3.1.0",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "메시지 기반 API 를 기계가독 형식으로 기술하는 프로토콜 중립 명세(채널·동작·메시지·서버·바인딩).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1028",
      "org": "OpenAPI Initiative",
      "title": "OpenAPI Specification v3.1.0",
      "published": "2021-02-15",
      "url": "https://spec.openapis.org/oas/v3.1.0",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "HTTP API 의 언어 중립 인터페이스 기술 표준. 3.1.0 에는 수신 웹훅을 기술하는 webhooks 필드가 있다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1029",
      "org": "뉴스핌",
      "title": "카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다",
      "published": "2026-05-13",
      "url": "https://www.newspim.com/news/view/20260512001077",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "카카오모빌리티의 로봇 플랫폼 구상(작업 추상화, 통합 제어 인터페이스, 재배정, 건물·업무 시스템 연동)을 전하는 기사.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-870",
      "org": "로봇신문",
      "title": "[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막",
      "published": "2025-11-09",
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=43274",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "클로봇의 자율주행 소프트웨어와 이기종 로봇 통합관제 플랫폼 CROMS 를 소개하는 기업 기사.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-308",
      "org": "Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv)",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "기반 시설·현장 클라우드·온보드 자율의 3계층 기준 아키텍처 RAIL 과 대형 상용차 제조 현장 실배치(초록 기준).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1032",
      "org": "Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv)",
      "title": "Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform",
      "published": "2017-06",
      "url": "https://arxiv.org/abs/1706.08931",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "공장·창고 AMR 플릿에서 클라우드 전역 계획기와 로봇 국지 주행을 나누고 분산 ROS 와 Rapyuta 클라우드 플랫폼을 비교한 연구(초록 기준).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1033",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "RMF 구성 요소와 웹 인터페이스를 잇는 JSON 메시지 스키마(README 는 작업 상태를 명시, 작업 요청·플릿 상태는 저장소 스키마 파일) 저장소.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1034",
      "org": "InOrbit",
      "title": "Contents — InOrbit Developer Portal",
      "published": null,
      "url": "https://developer.inorbit.ai/docs",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇 운영 플랫폼의 REST·스트리밍 API, 웹훅, API 키, Robot SDK·Edge SDK, 임베드, 커넥터를 설명하는 개발자 문서.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-774",
      "org": "Mobile Industrial Robots (MiR)",
      "title": "MiR Fleet",
      "published": null,
      "url": "https://mobile-industrial-robots.com/products/software/mir-fleet",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "MiR Fleet Enterprise 의 배치 환경, ERP·MES·WMS 용 REST API, 이벤트 기반 구조, IEC 62443-4-2 정합을 소개하는 제품 페이지.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1036",
      "org": "Locus Robotics",
      "title": "Seamless Integrations with LocusOne Robotics",
      "published": null,
      "url": "https://locusrobotics.com/locusone/automated-warehouse-software/integrations",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LocusONE 의 WMS API 연동(주문 수신·확인 회신), 전용 WiFi 망, 운영 성과 데이터를 소개하는 제품 페이지.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1037",
      "org": "Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv)",
      "title": "FogROS2-FT: Fault Tolerant Cloud Robotics",
      "published": "2024-12",
      "url": "https://arxiv.org/abs/2412.05408",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "상태 없는 로봇 서비스를 여러 클라우드에 복제해 장애·QoS 변동·비용 문제를 줄이는 방법과 P99 지연·비용 결과(초록 기준).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가?",
      "areas": [
        41,
        42
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가?",
      "areas": [
        41,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가?",
      "areas": [
        41,
        29
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가?",
      "areas": [
        41,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#5-적용-사례-현장-유형-명시",
      "title": "41. 플랫폼 아키텍처·외부 API"
    }
  ],
  "standards_updates": [
    {
      "name": "OpenAPI Specification 3.1.0",
      "kind": "표준",
      "org": "OpenAPI Initiative",
      "url": "https://spec.openapis.org/oas/v3.1.0",
      "related_areas": [
        41,
        23
      ],
      "summary": "HTTP API 를 사람과 컴퓨터가 함께 이해하도록 기술하는 언어 중립 표준 형식(2021-02-15). 3.1.0 에는 수신 웹훅을 기술하는 webhooks 필드가 있다.",
      "ref_id": "ref-1028"
    },
    {
      "name": "AsyncAPI Specification 3.1.0",
      "kind": "표준",
      "org": "AsyncAPI Initiative",
      "url": "https://www.asyncapi.com/docs/reference/specification/v3.1.0",
      "related_areas": [
        41,
        21
      ],
      "summary": "MQTT·AMQP·WebSocket·Kafka 등 메시지 기반 API 를 채널·동작·메시지·서버·바인딩으로 기술하는 프로토콜 중립 명세. Apache 2.0 라이선스.",
      "ref_id": "ref-1027"
    },
    {
      "name": "FogROS2 (클라우드·포그 로보틱스 플랫폼)",
      "kind": "오픈소스",
      "org": "Ichnowski, J., Chen, K., Dharmarajan, K. 외",
      "url": "https://arxiv.org/abs/2205.09778",
      "related_areas": [
        41,
        42
      ],
      "summary": "연산 능력이 제한된 로봇이 ROS 2 노드를 원격 클라우드로 옮겨 실행하게 하는 ROS 2 배포판 포함 플랫폼. SLAM·파지·모션 계획 가속을 저자가 보고했다(arXiv v3 초록 기준).",
      "ref_id": "ref-304"
    }
  ],
  "additional_research_requests": [
    "5. 적용 사례 (현장 유형 명시): 병원(RoMi-H)·제조 공장(RAIL)·기타(네이버 1784) 사례의 시작 조건·제약·완료·인계·예외·성과 칸 근거가 없어 미확인으로 두었다 — 실제 배치 보고서나 논문 본문에서 확인이 필요하다. 상업 시설·가정·실외 현장의 플랫폼 배치·외부 API 사례도 없다.",
    "6. 대표 접근법과 기술: FogROS2 모션 계획 가속 배수가 arXiv v3 초록(45배)과 ICRA 2023 판 서술(28배)로 다를 수 있어 미확인으로 병기했다 — ICRA 카메라 레디 판 확인이 필요하다.",
    "5·6절: 네이버 1784 의 클라우드 제어 로봇 대수(회사 페이지 100여 대, 기사 문구 40여 대)의 기준 시점 차이를 기사 원문으로 확인해야 한다.",
    "7. 관련 표준·프레임워크·오픈소스: 국내 클라우드 로봇·이기종 로봇 통합관제의 참조 구조·외부 API 표준(TTA·KS)을 찾지 못했다(열린 질문으로 올림).",
    "13. 참고 자료 (각주): ref-004·ref-031 은 기존 id 를 재사용했으나 기존 참고문헌 페이지(docs/references/ref-004.md, ref-031.md)의 '각주 형식' 줄이 입력에 없어 브리프 출처 값으로 적었다 — 퍼블리셔가 기존 줄과 대조해 맞춰 주기를 요청한다.",
    "참고문헌 id 충돌(1차 검증 지적): ref-304·ref-937·ref-1027·ref-1028·ref-308·ref-1032·ref-1033·ref-774·ref-1036·ref-1037 이 같은 날 이전 브리프(2026-09-30-03·04)의 다른 출처 id 와 겹친다. 또 ref-304(FogROS2)·ref-308(Brorsson 외)은 기존 ref-304·ref-308 과 같은 URL 로 보인다 — 게시 전 id 재배정·병합을 pipeline 담당에게 요청한다.",
    "42. 분산 시스템·통신·컴퓨팅 구조 페이지와의 중복: 역할 분담·장애 대응(FogROS2-FT·RAIL) 내용이 겹칠 수 있어 다음 해당 영역 실행에서 기존 각주와 대조가 필요하다."
  ],
  "fixes_applied": [
    "f1 강등 — 6절 '외부 API' 소절과 7절 표 rmf-web 행을 [추정]으로 쓰고 'REST'·'OpenAPI 형식' 표현을 빼, 웹 대시보드가 쓰는 API 엔드포인트, /docs 경로와 공개 문서 사이트의 API 정의, TortoiseORM 기반 PostgreSQL·SQLite·MySQL·MariaDB 와 기본 메모리 SQLite 로만 서술했다.",
    "f2 — 6절 인증·권한 문단의 권한 구조를 '역할·동작·권한 그룹 세 값으로 권한을 정하는 구조'로 고쳤고 7절 표에도 같은 표현을 썼다.",
    "f3 — 6절에서 README 가 이름으로 드는 스키마는 작업 상태(task_state)이고 작업 요청·플릿 상태 스키마는 저장소 스키마 파일 기준이라는 문장을 따로 두었다(reference_updates ref-1033 요약도 같게 고침).",
    "f5 — 6절에서 주제 계층을 '로컬 브로커용으로 제안한 것이고 클라우드 브로커에서는 조정될 수 있으며 주제 이름은 정해진 대로 써야 한다'로 고치고 visualization·zoneSet·responses 가 선택 주제임과 기준 판 3.0.0 을 밝혔다. 7절 표도 '제안'으로 썼다.",
    "f7 — 4절·7절에서 '3.1.0 에는 수신 웹훅을 기술하는 webhooks 필드가 있다'로 고쳤고, 용어집 'OpenAPI 명세' 정의의 '3.1.0 부터'를 '3.1.0 은'으로 고쳤다(reference_updates ref-1028 요약도 수정).",
    "f9 — 6절 FogROS2 문장에 'arXiv v3(2023-04-24) 초록 기준 저자 보고'를 적고 모션 계획 가속 배수는 판에 따라 다를 수 있어 미확인이라고 병기했다. 8절에도 v3 2023-04-24 를 적었다.",
    "f11 — 6절 역할 분담 문장의 로봇 쪽 역할을 '온보드 실행·자율 기능(범위는 연구마다 다름)'으로 좁혀 썼다.",
    "f12 — 4절·5절·6절·8절에서 현장 클라우드 앞의 '지연·연결 문제를 다루는' 수식어를 쓰지 않았고, f21 종합 문장의 '지연·연결에 민감한' 수식도 함께 뺐다.",
    "f19·ref-1029 — 6절 본문의 보도일과 각주·reference_updates 의 발행일을 2026-05-13 으로, 제목을 \"카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다\"로 고치고 '(제목 일부만 확인)'을 뗐다.",
    "f20·ref-870 — 제목을 \"[기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막\"으로, 발행일·기준일을 2025-11-09 로 고치고, 6절에서 '50대 이상 로봇 동시 제어·승강기 연동' 문장과 '국내 첫 이기종 로봇 통합관제 솔루션이라는 주장' 문장을 나눠 썼다.",
    "f15 — 지원 대수는 본문에 쓰지 않았다(두 표현 가운데 한쪽을 고르지 않기 위해 수치 자체를 넣지 않음). MiR 내용은 모두 [추정] 벤더 주장으로 썼다.",
    "f21 — 3절·6절의 REST(OpenAPI 로 기술) 부분 근거를 ref-1028·ref-774·ref-1034(f7·f15·f16)로 한정하고 f1(rmf-web API 엔드포인트)을 근거로 쓰지 않았다. 6절 종합 문장의 ref-762 은 인증·권한(f2) 근거로만 남겼다.",
    "f24 — 9절에서 42. 분산 시스템·통신·컴퓨팅 구조를 외부 연계 대상으로 쓰지 않고, '클라우드 제공자 인프라는 외부 연계 대상, 현장 네트워크 설계는 ROP 의 다른 세부영역인 42. 분산 시스템·통신·컴퓨팅 구조에서 다룬다'로 나눠 썼다.",
    "5·6·9절 f14 — 네이버 ARC 문장을 모두 [추정] 벤더 주장으로 쓰고, 5절·9절에서 위치 추정·이동 계획을 클라우드에 두는 것은 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 서술하며 ROP 직접 범위의 근거로 쓰지 않는다고 밝혔다.",
    "5절 — 병원 사례 서술 첫 문장에 특정 병원의 배치 결과가 아니라 공공 의료기관용 미들웨어 구조임을 밝혔고, 네 사례 모두 근거가 없는 칸은 '미확인'으로 두었다(site_matrix_updates 에서도 제외).",
    "11절 열린 질문 1 — '클라우드나 5G 연결'에서 '5G'를 빼 '클라우드 연결'로 고쳤다(open_question_updates 도 같음).",
    "13절 — ref-004·ref-031 은 새 각주 id 를 만들지 않고 기존 id 를 재사용했다. 다만 기존 참고문헌 페이지의 '각주 형식' 줄이 입력에 없어 브리프 출처 값(기관·제목·URL·접근일)으로 적었으며, 기존 줄과의 대조를 additional_research_requests 로 퍼블리셔에 요청했다.",
    "분량 초과 자동 분리: 41. 플랫폼 아키텍처·외부 API 본문 11,110자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,284자"
  ]
}
```

### runs/2026-09-30-05/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area41-s6.md (3,227자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area41-s4.md (964자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area41-s7.md (954자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area41-s10.md (867자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area41-s8.md (796자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area41-s3.md (619자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area41-s11.md (571자)
```

### runs/2026-09-30-05/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [클라우드 로보틱스, 현장 클라우드, 외부 API, OpenAPI, AsyncAPI, 플릿 어댑터]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-004, ref-031, ref-762, ref-304, ref-1025, ref-937, ref-1027, ref-1028, ref-1029, ref-870, ref-308, ref-1032, ref-1033, ref-1034, ref-774, ref-1036, ref-1037]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 41. 플랫폼 아키텍처·외부 API

# 41. 플랫폼 아키텍처·외부 API

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **클라우드·현장 서버·로봇 역할 분담**: 어떤 판단과 데이터를 클라우드·현장 서버·로봇 가운데 어디에 둘지 정한다
- **플랫폼 기준 아키텍처**: 서비스 분리, 이벤트 구조, 제조사 중립성을 갖춘 플랫폼 구조를 정한다
- **외부 API·SDK 제공**: 다른 시스템과 개발자가 플랫폼을 부를 수 있는 API·웹훅·SDK·문서를 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’에서 왔다. 그 본문은 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]

## 3. 왜 중요한가

이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 단일 접점이 되고, 판단을 어디에 두느냐가 운영 연속성을 좌우하므로 이 영역이 중요하다. [추정][^ref-031][^ref-774][^ref-1036][^ref-1037]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 왜 중요한가](../../topics/2026/2026-09-30-area41-s3.md)에 있다.

## 4. 핵심 개념과 용어

**클라우드 로보틱스(Cloud Robotics)** — 연산 능력이 제한된 로봇이 계산을 원격 클라우드로 옮겨 실행하는 구조로, ROS 2 노드를 AWS·GCP·Azure 로 옮겨 실행하게 하는 FogROS2 가 한 예다. [사실][^ref-304] - **계산 오프로딩(computation offloading)** — 로봇에서 하던 SLAM·파지 계획·모션 계획 같은 계산을 클라우드로 넘겨 처리 시간을 줄이는 방식이다. [사실][^ref-304]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어](../../topics/2026/2026-09-30-area41-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 적용 사례는 플랫폼을 어디에 두고 외부에 무엇을 여는지가 드러난 병원·제조 공장·물류창고·기타 현장의 네 건이다. 상업 시설·가정·실외 사례는 이번 조사에서 찾지 못했고, 사례마다 근거가 없는 칸은 미확인으로 둔다.

### 병원

**현장 유형:** 병원

**사례:** 공공 의료기관의 로봇 시스템을 하나의 미들웨어로 묶는 구조(RoMi-H)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리, 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·ICT 시스템용 API)의 네 영역이 역할을 나눈다. [사실][^ref-937] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 특정 병원의 배치 결과가 아니라 싱가포르 창이종합병원 CHART 가 공공 의료기관용으로 내놓은 미들웨어 구조다. [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)(Robotic Middleware for Healthcare)는 OMG DDS 를 쓰며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다. [사실][^ref-937] 외부 시스템용 API 를 통합 영역으로 따로 두는 점이 이 영역의 "외부에 무엇을 열 것인가"와 이어진다. [의견][^ref-937]

### 제조 공장

**현장 유형:** 제조 공장

**사례:** 대형 상용차 제조 현장의 사내 물류 이동 로봇 운영(RAIL 기준 아키텍처)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 사내 물류(internal logistics) 운반. 구체적 물품은 미확인. [사실][^ref-308] |
| 수행 자원 | 설비에 단 외부 센서·계산 자원(기반 시설), 현장 클라우드, 로봇 온보드 자율의 세 층이 나눠 맡는다. [사실][^ref-308] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(초록은 실배치와 사용자 경험 평가를 보고하나 처리량·시간·비용 수치는 확인하지 못함) |

Brorsson 외는 이 기준 아키텍처를 대형 상용차 제조 현장 실배치와 사용자 경험 평가로 보였다(2025-12, 초록 기준). [사실][^ref-308] 로봇 온보드 지능만이 아니라 설비 쪽 센서와 현장 계산 자원까지 판단 배치의 선택지가 된다는 점을 보여 준다. [추정][^ref-308]

### 물류창고

**현장 유형:** 물류창고

**사례:** 물류창고 피킹 — WMS 주문을 로봇 작업으로 바꾸고 결과를 되돌리기(Locus Robotics LocusONE)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 창고 관리 시스템(Warehouse Management System, WMS)에서 주문을 API 로 받는다. [추정] 벤더 주장[^ref-1036] |
| 작업 대상 | WMS 주문 정보와 피킹할 품목. [추정] 벤더 주장[^ref-1036] |
| 수행 자원 | LocusONE 플랫폼이 주문을 피킹 효율 기준으로 최적화해 로봇 작업으로 내린다. [추정] 벤더 주장[^ref-1036] |
| 제약 | 기존 인프라와 분리된 전용 WiFi 망을 설치·유지한다. [추정] 벤더 주장[^ref-1036] |
| 완료·인계 | 피킹 완료 확인을 WMS 로 즉시 회신한다. [추정] 벤더 주장[^ref-1036] |
| 예외·성과 | 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 데이터를 제공한다. 실패 시 복구 주체는 미확인. [추정] 벤더 주장[^ref-1036] |

흐름 단계로는 피킹에 해당한다. 외부 API 가 작업의 시작(주문 수신)과 끝(확인 회신)을 모두 맡는 구조다. [추정] 벤더 주장[^ref-1036] 플랫폼을 클라우드와 현장 가운데 어디에 두는지는 자료에 나오지 않는다(미확인). 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽의 일이고, ROP 는 연동 인터페이스만 다룬다(9절). [추정][^ref-1036]

### 기타

**현장 유형:** 기타

**사례:** 기업 사옥에서 클라우드로 로봇 운영(네이버 제2사옥 1784 의 ARC)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 클라우드의 ARC brain(이동 계획·위치 추정·작업 수행·기반 시설 연동), ARC eye(디지털 트윈 데이터와 측위 AI 로 로봇 위치 결정), ARC mind(웹 개발자용 웹 기반 OS)가 나눠 맡고, 로봇은 연산·판단을 싣지 않는다. [추정] 벤더 주장[^ref-1025] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

네이버는 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다. [추정] 벤더 주장[^ref-1025] 위치 추정·이동 계획까지 클라우드에 두는 이 설계는 분류 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 볼 수 있으며, ROP 직접 범위의 근거로 쓰지 않는다(9절). [추정][^ref-1025] ARC mind 는 웹 개발자가 로봇 서비스를 만들게 한다는 점에서 개발자에게 여는 인터페이스의 예다. [추정] 벤더 주장[^ref-1025]

## 6. 대표 접근법과 기술

이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1032][^ref-308][^ref-304][^ref-1037][^ref-004][^ref-1028][^ref-1027]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-09-30-area41-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다. [의견][^ref-004][^ref-937][^ref-031][^ref-1028][^ref-1027][^ref-304]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area41-s7.md)에 있다.

## 8. 대표 연구와 자료

판단 배치와 장애 대응의 근거는 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구이며, 모두 논문 초록 기준이다. [사실][^ref-304][^ref-1037][^ref-1032][^ref-308]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료](../../topics/2026/2026-09-30-area41-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처, 작업 요청·작업 상태·플릿 상태의 기계가독 스키마, REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기, API 호출의 인증·권한, 그리고 판단·데이터를 로봇·현장 서버·클라우드 가운데 어디에 둘지 정하는 배치 정책으로 보인다. [추정][^ref-004][^ref-937][^ref-1033][^ref-031][^ref-1028][^ref-1027][^ref-762]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터로 로봇·제조사 관제의 기능·상태를 주고받는 인터페이스와 판단 배치 정책. [추정][^ref-004] | 연계 대상: 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능은 로봇 제조사가 맡는다. FogROS2 같은 오프로딩은 로봇 내부 기능의 실행 위치 선택이다. [추정][^ref-304][^ref-1032] |
| 상위 업무 시스템 | 업무 시스템이 부르는 외부 API(요청 수신·결과 회신)와 그 인증·권한. [추정][^ref-762][^ref-1036] | 연계 대상: 주문·재고 같은 업무 판단은 WMS·ERP 가 맡는다. [추정][^ref-1036] |

클라우드 제공자 인프라는 외부 연계 대상이고, 현장 네트워크 설계는 ROP 의 다른 세부영역인 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)에서 다룬다. [추정][^ref-1037][^ref-1036]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

네이버가 밝힌 ARC 처럼 위치 추정·이동 계획까지 클라우드에 두는 설계는 위 경계를 제품 전략으로 옮긴 사례이며, 이종 제조사를 연결하는 ROP 의 직접 범위로 보지 않는다. [추정] 벤더 주장[^ref-1025] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 같은 대분류의 네트워크·데이터 영역, F. 연동의 네 영역, 보안·관제·복구 영역, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1037][^ref-004]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md)에 있다.

## 11. 열린 질문

판단 배치의 단절 대응, 외부 API 의 수명주기와 전달 보장, 국내 표준 여부가 아직 확인되지 않았다.

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 열린 질문](../../topics/2026/2026-09-30-area41-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1025]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1027]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1028]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1032]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1033]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1036]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30
[^ref-1037]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30
```

### docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 41
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 41. 플랫폼 아키텍처·외부 API

# 41. 플랫폼 아키텍처·외부 API

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **클라우드·현장 서버·로봇 역할 분담**: 어떤 판단과 데이터를 클라우드·현장 서버·로봇 가운데 어디에 둘지 정한다
- **플랫폼 기준 아키텍처**: 서비스 분리, 이벤트 구조, 제조사 중립성을 갖춘 플랫폼 구조를 정한다
- **외부 API·SDK 제공**: 다른 시스템과 개발자가 플랫폼을 부를 수 있는 API·웹훅·SDK·문서를 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’에서 왔다. 그 본문은 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 적용 사례 (현장 유형 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

아직 작성되지 않음

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

아직 작성되지 않음

## 11. 열린 질문

아직 작성되지 않음

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

(아직 각주가 없다. 본문이 작성되면 출처 각주를 여기에 둔다.)
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s6.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-031, ref-762, ref-304, ref-1025, ref-937, ref-1027, ref-1028, ref-1029, ref-870, ref-308, ref-1032, ref-1033, ref-1034, ref-774, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#6
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술

# 41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1032][^ref-308][^ref-304][^ref-1037][^ref-004][^ref-1028][^ref-1027]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1032][^ref-308][^ref-304][^ref-1037][^ref-004][^ref-1028][^ref-1027]

### 로봇·현장 서버·클라우드 역할 분담

독립된 두 연구(Singhal 외 2017, Brorsson 외 2025)는 모두 로봇 밖의 중앙 계산 자원(클라우드 또는 현장 클라우드)이 플릿 조율·전역 계획을 맡고 각 로봇이 온보드 실행·자율 기능(범위는 연구마다 다름)을 유지하는 혼합 구조를 제시한다. [사실][^ref-1032][^ref-308] Singhal 외에서는 클라우드 전역 계획기가 목적지를 주고 로봇이 이동·장애물 회피를 자율로 한다. [사실][^ref-1032] RAIL 은 기반 시설·현장 클라우드·온보드 자율의 세 층을 둔다. [사실][^ref-308] 네이버 ARC 처럼 이동 계획·위치 추정까지 클라우드로 올리는 설계도 있다. [추정] 벤더 주장[^ref-1025]

자료를 종합하면 국지 주행·즉각적 안전 반응은 로봇에, 플릿 조율·교통·설비 연동은 현장 서버(현장 클라우드)에, 무거운 계산 오프로딩과 여러 현장 집계·개발자 서비스는 클라우드에 두는 혼합 배치가 공통 형태로 보인다. [추정][^ref-004][^ref-304][^ref-1032][^ref-308][^ref-1025] 다만 이 배치 경계는 제품 전략에 따라 움직인다. [추정][^ref-1025]

### 계산 오프로딩과 다중 클라우드 장애 대응

Ichnowski 외의 FogROS2 는 연산 능력이 제한된 로봇이 ROS 2 노드를 AWS·GCP·Azure 같은 원격 클라우드로 옮겨 실행하게 하는 ROS 2 배포판 포함 플랫폼이며, arXiv v3(2023-04-24) 초록 기준 저자 보고로 SLAM 지연 50% 감소, 파지 계획 14초→1.2초, 모션 계획 45배 가속, 영상 압축으로 이미지 전송 지연 97% 개선을 제시했다(모션 계획 가속 배수는 논문 판에 따라 다를 수 있어 미확인). [사실][^ref-304]

Chen 외의 FogROS2-FT(IROS 2024)는 상태 없는 로봇 서비스를 여러 클라우드에 복제해 요청을 나눠 보내고 가장 먼저 온 응답을 쓰는 방식으로, 모션 계획 P99 지연을 최대 5.53배 줄이고 비용을 최대 2.2배 낮췄다고 보고했다(저자 보고). [사실][^ref-1037]

FogROS2 가 SLAM·파지 계획을 클라우드로 옮기는 것은 로봇 자체 지능 기능의 실행 위치를 고르는 일이어서, 이 영역에서는 배치 방식의 근거로만 쓴다. [추정][^ref-304]

### 제조사 중립 어댑터 계층

Open-RMF 핵심 구조는 모든 플릿 관리자가 예상 경로를 보고하는 중앙 교통 일정 데이터베이스와 충돌 시 플릿 관리자 간 협상을 두고, 제조사 고유 API 를 플릿 어댑터로 잇되 어댑터를 제어 수준(Full Control·Traffic Light·Read Only·No Interface)으로 나누며, 재사용 가능한 C++ API(파이썬 바인딩 포함)는 Full Control 에만 있다(Open-RMF 설명서의 RMF 핵심 장 기준, 발행일 미확인). [사실][^ref-004]

RoMi-H 는 기계 영역에서 하드웨어를 추상화하고, 통합 영역에서 모바일 앱·웹 앱·ICT 시스템용 API 를 둔다. [사실][^ref-937]

### 외부 API: REST·이벤트·웹훅·SDK

Open-RMF 의 웹 API 서버(rmf-web api-server)는 웹 대시보드가 쓰는 API 엔드포인트를 두고, 서버의 /docs 경로와 공개 문서 사이트에서 API 정의를 제공하며, 기록용 데이터베이스는 TortoiseORM 으로 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하고 기본값은 메모리 SQLite 다. [추정][^ref-762] 같은 계열의 rmf_api_msgs 는 RMF 의 C++·Python 구성 요소와 웹 인터페이스를 잇는 JSON 메시지 스키마 모음이며, 스키마에서 타입 있는 데이터 모델을 생성할 수 있다. [사실][^ref-1033] README 가 이름으로 드는 스키마는 작업 상태(task_state)이고, 작업 요청·플릿 상태 스키마는 저장소의 스키마 파일 기준이다. [사실][^ref-1033]

메시지·이벤트 쪽에서 VDA 5050 3.0.0 은 플릿 관제와 이동 로봇 사이의 제조사 중립 인터페이스로 MQTT 3.1.1 이상과 JSON 을 쓴다. [사실][^ref-031] 주제 계층 interfaceName/majorVersion/manufacturer/serialNumber/topic 은 로컬 브로커용으로 제안한 것이고 클라우드 브로커에서는 조정될 수 있으며, 주제 이름(order·instantActions·state·visualization·connection·factsheet·responses·zoneSet)은 정해진 대로 써야 하고 그 가운데 visualization·zoneSet·responses 는 선택 주제다. [사실][^ref-031] 이런 메시지 API 는 AsyncAPI 명세 3.1.0 으로 채널·동작(send/receive)·메시지·서버(브로커)·프로토콜별 바인딩을 기계가 읽게 기술할 수 있다. [사실][^ref-1027]

제품에서는 MiR 이 MiR Fleet Enterprise 가 Windows Server 에서 돌며 가상화·클라우드 배치를 지원하고 ERP·MES·WMS 연동용 REST API 와 이벤트 기반 아키텍처를 갖춘다고 주장한다. [추정] 벤더 주장[^ref-774] InOrbit 개발자 문서는 REST·스트리밍 API, 사고 관리용 외부 발신 웹훅과 수신 API, 로봇에 넣는 Robot SDK(C++·Python)와 로봇마다 에이전트 없이 현장 애플리케이션을 잇는 Edge SDK, 임베드 가능한 대시보드를 제공한다고 적는다. [추정] 벤더 주장[^ref-1034]

인증·권한은 API 와 함께 설계된다. rmf-web API 서버는 OpenID Connect 로 발급된, 독립적으로 검증할 수 있는 JWT 접근 토큰으로 사용자를 식별하고, 역할·동작·권한 그룹 세 값으로 권한을 정하는 구조로 접근을 통제하며, 관리자는 모든 그룹에 모든 동작을 할 수 있다. [사실][^ref-762] InOrbit 은 서비스 사용자와 역할 기반 권한에 묶인 API 키를, MiR 은 IEC 62443-4-2(SL-C 3)에 맞춘 단일 로그인·감사 기록·세분화된 사용자 권한을 제공한다고 주장한다. [추정] 벤더 주장[^ref-1034][^ref-774]

종합하면 외부에는 OpenAPI 로 기술하는 REST API, AsyncAPI·웹훅으로 기술하는 이벤트·메시지 API, SDK 를 인증·권한 통제와 함께 여는 조합이 쓰이는 것으로 보인다. [추정][^ref-1028][^ref-774][^ref-1034][^ref-1027][^ref-762]

### 국내 제품 동향

뉴스핌(2026-05-13) 보도에 따르면 카카오모빌리티는 로봇–인프라–사용자를 잇는 플랫폼으로 서비스 요청을 로봇 실행 단위로 바꾸는 작업 추상화, 이종 로봇이 통신하게 하는 통합 API 인 제어 인터페이스, 고장 감지 시 다른 로봇으로 작업을 넘기는 재배정, 건물 인프라와 ERP·물류 자동화 시스템을 잇는 연동 기반을 추진한다. [추정] 벤더 주장[^ref-1029] 로봇신문(2025-11-09) 보도에 따르면 클로봇은 통합관제 플랫폼 CROMS 가 50대 이상 로봇을 동시에 제어하고 승강기 연동으로 다층 건물에서 운용할 수 있다고 밝힌다. [추정] 벤더 주장[^ref-870] 같은 기사에서 클로봇은 CROMS 를 국내 첫 이기종 로봇 통합관제 솔루션이라고 주장한다. [추정] 벤더 주장[^ref-870]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1025]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1027]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1028]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-1029]: 뉴스핌, 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다, 2026-05-13, https://www.newspim.com/news/view/20260512001077, 접근일 2026-09-30
[^ref-870]: 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막, 2025-11-09, https://www.irobotnews.com/news/articleView.html?idxno=43274, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1032]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1033]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30
[^ref-1034]: InOrbit, Contents — InOrbit Developer Portal, 미확인, https://developer.inorbit.ai/docs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1037]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s4.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-304, ref-1025, ref-1027, ref-1028, ref-308, ref-1034]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#4
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어

# 41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **클라우드 로보틱스(Cloud Robotics)** — 연산 능력이 제한된 로봇이 계산을 원격 클라우드로 옮겨 실행하는 구조로, ROS 2 노드를 AWS·GCP·Azure 로 옮겨 실행하게 하는 FogROS2 가 한 예다. [사실][^ref-304] - **계산 오프로딩(computation offloading)** — 로봇에서 하던 SLAM·파지 계획·모션 계획 같은 계산을 클라우드로 넘겨 처리 시간을 줄이는 방식이다. [사실][^ref-304]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **클라우드 로보틱스(Cloud Robotics)** — 연산 능력이 제한된 로봇이 계산을 원격 클라우드로 옮겨 실행하는 구조로, ROS 2 노드를 AWS·GCP·Azure 로 옮겨 실행하게 하는 FogROS2 가 한 예다. [사실][^ref-304]
- **계산 오프로딩(computation offloading)** — 로봇에서 하던 SLAM·파지 계획·모션 계획 같은 계산을 클라우드로 넘겨 처리 시간을 줄이는 방식이다. [사실][^ref-304]
- **현장 클라우드(on-premise cloud)** — 현장 안에 두는 계산 자원으로, RAIL 기준 아키텍처는 이를 설비 쪽 기반 시설 층과 로봇 온보드 자율 층 사이에 둔다. [사실][^ref-308]
- **[플릿 어댑터](../../glossary/fleet-adapter.md)(Fleet Adapter)와 [플릿 제어 수준](../../glossary/fleet-control-level.md)** — Open-RMF 에서 제조사 고유 API 를 표준 인터페이스로 잇는 구성 요소이며, Full Control·Traffic Light·Read Only·No Interface 의 제어 수준으로 나뉜다. [사실][^ref-004]
- **OpenAPI 명세(OpenAPI Specification, OAS)** — HTTP API 를 사람과 컴퓨터가 함께 발견·이해하도록 기술하는 언어 중립 표준 형식이며, 3.1.0 에는 API 가 받을 수 있는 수신 웹훅을 기술하는 webhooks 필드가 있다. [사실][^ref-1028]
- **AsyncAPI 명세(AsyncAPI Specification)** — MQTT·AMQP·WebSocket·Kafka·HTTP 등 메시지 기반 API 를 채널·동작·메시지·서버·바인딩으로 기술하는 프로토콜 중립 형식이다. [사실][^ref-1027]
- **웹훅(Webhook)** — 사건을 외부에 알리는 이벤트 전달 인터페이스다. 로봇 운영 플랫폼 InOrbit 은 사고 관리용 외부 발신 웹훅을 제공한다고 적는다. [추정] 벤더 주장[^ref-1034]
- **[브레인리스 로봇](../../glossary/brainless-robot.md)(Brainless Robot)** — 로봇 안이 아니라 클라우드에서 연산·판단을 하는 구조로, 네이버가 ARC 에 쓴다고 밝힌다. [추정] 벤더 주장[^ref-1025]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1025]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-1027]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1028]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1034]: InOrbit, Contents — InOrbit Developer Portal, 미확인, https://developer.inorbit.ai/docs, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s7.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-031, ref-762, ref-304, ref-937, ref-1027, ref-1028, ref-1033, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#7
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스

# 41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다. [의견][^ref-004][^ref-937][^ref-031][^ref-1028][^ref-1027][^ref-304]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다. [의견][^ref-004][^ref-937][^ref-031][^ref-1028][^ref-1027][^ref-304]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [Open-RMF](../../glossary/open-rmf.md) 핵심(교통 일정·플릿 어댑터) | 오픈소스 | 중앙 교통 일정 데이터베이스·플릿 관리자 간 협상과 제어 수준별 플릿 어댑터로 제조사 관제를 잇는다. [사실] | [^ref-004] |
| Open-RMF rmf-web API 서버 | 오픈소스 | 대시보드용 API 엔드포인트와 /docs 의 API 정의, OpenID Connect·JWT 인증과 역할·동작·권한 그룹 권한을 둔다. [추정] | [^ref-762] |
| Open-RMF rmf_api_msgs | 오픈소스 | 작업 상태 등 RMF 구성 요소와 웹 인터페이스를 잇는 JSON 메시지 스키마 모음이다. [사실] | [^ref-1033] |
| [VDA 5050](../../glossary/vda-5050.md) 3.0.0 | 표준 | 플릿 관제–이동 로봇 MQTT·JSON 인터페이스로, 주 버전을 넣은 주제 계층을 로컬 브로커용으로 제안하고 외부 IT 시스템 인터페이스는 범위 밖에 둔다. [사실] | [^ref-031] |
| OpenAPI 명세 3.1.0 | 표준 | HTTP API 와 수신 웹훅을 기술하는 언어 중립 형식이다(2021-02-15). [사실] | [^ref-1028] |
| AsyncAPI 명세 3.1.0 | 표준 | 메시지 기반 API 를 기술하는 프로토콜 중립 형식이며 Apache 2.0 라이선스로 공개된다. [사실] | [^ref-1027] |
| RoMi-H | 프레임워크 | 공공 의료기관용 DDS 미들웨어로 기계·제어·중앙·통합 네 영역을 둔다. [사실] | [^ref-937] |
| FogROS2 · FogROS2-FT | 오픈소스 · 연구 | ROS 2 노드의 클라우드 오프로딩과 다중 클라우드 복제에 의한 장애 대응을 보인다. [사실] | [^ref-304][^ref-1037] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1027]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1028]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-1033]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30
[^ref-1037]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s10.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-004, ref-031, ref-762, ref-1025, ref-937, ref-1029, ref-870, ref-308, ref-1034, ref-774, ref-1036, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#10
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결

# 41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 같은 대분류의 네트워크·데이터 영역, F. 연동의 네 영역, 보안·관제·복구 영역, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1037][^ref-004]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 같은 대분류의 네트워크·데이터 영역, F. 연동의 네 영역, 보안·관제·복구 영역, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1037][^ref-004]

- [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) — 현장 네트워크와 연결이 끊긴 상태의 운영을 다루며, 클라우드 장애 대응과 현장 클라우드 배치가 이 영역의 판단 배치와 맞물린다. [추정][^ref-1037][^ref-308]
- [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) — API 서버의 기록용 데이터베이스 설정과 감사 기록이 이어진다. [추정][^ref-762][^ref-1034]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 플릿 어댑터와 제조사 관제 API 가 이 영역의 어댑터 계층 아래를 이룬다. [추정][^ref-004][^ref-774]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — VDA 5050 의 주제 구조와 적용 범위가 외부 API 설계의 전제가 된다. [추정][^ref-031]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 로봇–기반 시설 통신과 승강기 연동을 플랫폼의 어느 층에 둘지가 이어진다. [추정][^ref-937][^ref-1025][^ref-870]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — WMS·ERP·MES 가 외부 API 의 주 사용자다. [추정][^ref-774][^ref-1036]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — API 호출의 토큰 인증, 역할 기반 권한, API 키가 이어진다. [추정][^ref-762][^ref-1034]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — IEC 62443-4-2 정합 주장과 감사 기록이 이어진다. [추정][^ref-774]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 웹 대시보드와 임베드 대시보드가 외부 API 를 쓴다. [추정][^ref-762][^ref-1034]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 고장 시 다른 로봇으로 작업을 넘기는 재배정이 플랫폼 기능으로 제시된다. [추정][^ref-1029]
- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 네이버·카카오모빌리티·클로봇의 플랫폼 구상이 업체 동향이다. [추정][^ref-1025][^ref-1029][^ref-870]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 5절 적용 사례의 현장 유형별 요구와 도입 사례가 모인다. [추정][^ref-1036][^ref-308][^ref-937][^ref-1025]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-1025]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1029]: 뉴스핌, 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다, 2026-05-13, https://www.newspim.com/news/view/20260512001077, 접근일 2026-09-30
[^ref-870]: 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 '피지컬 AI' 시대의 서막, 2025-11-09, https://www.irobotnews.com/news/articleView.html?idxno=43274, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1034]: InOrbit, Contents — InOrbit Developer Portal, 미확인, https://developer.inorbit.ai/docs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1036]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30
[^ref-1037]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s8.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-304, ref-308, ref-1032, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#8
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료

# 41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 판단 배치와 장애 대응의 근거는 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구이며, 모두 논문 초록 기준이다. [사실][^ref-304][^ref-1037][^ref-1032][^ref-308]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

판단 배치와 장애 대응의 근거는 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구이며, 모두 논문 초록 기준이다. [사실][^ref-304][^ref-1037][^ref-1032][^ref-308]

- Ichnowski 외, FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2(2022-05 제출, v3 2023-04-24) — ROS 2 노드를 클라우드로 옮겨 SLAM·파지·모션 계획을 가속한 결과를 저자가 보고했다. 판단 배치 가운데 무거운 계산을 어디에 둘지의 근거다. [사실][^ref-304]
- Chen 외, FogROS2-FT: Fault Tolerant Cloud Robotics(IROS 2024) — 클라우드 제공자 장애·QoS 변동·비용을 약점으로 보고, 상태 없는 서비스의 다중 클라우드 복제로 꼬리 지연과 비용을 줄였다. 클라우드 의존 배치의 연속성 대책이다. [사실][^ref-1037]
- Singhal 외, Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform(2017) — 공장·창고 AMR 플릿에서 클라우드 전역 계획기와 로봇 자율 이동을 나누고 분산 ROS 와 Rapyuta 클라우드 플랫폼을 비교했다. [사실][^ref-1032]
- Brorsson 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics(2025-12) — 대부분의 AMR 솔루션이 온보드 지능을 강조하고 기반 시설 지원형은 덜 탐구됐다고 보고, 기반 시설·현장 클라우드·온보드 자율의 RAIL 기준 아키텍처를 제조 현장 실배치로 보였다. [사실][^ref-308]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1032]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1037]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s3.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 왜 중요한가"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-304, ref-1027, ref-1028, ref-308, ref-1032, ref-1034, ref-774, ref-1036, ref-1037]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#3
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 왜 중요한가

# 41. 플랫폼 아키텍처·외부 API — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 단일 접점이 되고, 판단을 어디에 두느냐가 운영 연속성을 좌우하므로 이 영역이 중요하다. [추정][^ref-031][^ref-774][^ref-1036][^ref-1037]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 단일 접점이 되고, 판단을 어디에 두느냐가 운영 연속성을 좌우하므로 이 영역이 중요하다. [추정][^ref-031][^ref-774][^ref-1036][^ref-1037]

로봇–관제 표준은 이 접점을 채우지 않는다. VDA 5050 3.0.0 명세는 주변 설비·기반 시설 구성 요소·외부 IT 시스템과의 인터페이스를 범위 밖에 둔다. [사실][^ref-031] 제조사 관제 쪽에서는 MiR 이 ERP·MES·WMS 연동용 REST API 를, Locus Robotics 가 WMS 와 잇는 API 를 각자 제공한다고 밝히며, 제조사 관제마다 자체 API 를 낸다는 판단은 이런 벤더 자료에 기댄 것이다. [추정] 벤더 주장[^ref-774][^ref-1036]

판단 배치는 성능만의 문제가 아니다. 클라우드 로보틱스 연구는 클라우드 제공자 장애, 네트워크 서비스 품질(Quality of Service, QoS) 변동, 신뢰성 높은 인스턴스의 비용을 약점으로 꼽는다. [사실][^ref-1037] 따라서 어떤 판단을 로봇·현장 서버·클라우드 가운데 어디에 두느냐가 연결이 흔들릴 때 무엇이 계속 동작하는지를 정한다. [추정][^ref-1037]

확인한 자료로 본 핵심 질문의 잠정 답은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치와, REST·이벤트 API·웹훅·SDK 를 인증·권한 통제와 함께 여는 조합이다(6절). [추정][^ref-1032][^ref-308][^ref-304][^ref-1028][^ref-1027][^ref-774][^ref-1034]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1027]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1028]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1032]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1034]: InOrbit, Contents — InOrbit Developer Portal, 미확인, https://developer.inorbit.ai/docs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1036]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30
[^ref-1037]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-30-05/pages/topics/2026/2026-09-30-area41-s11.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API — 열린 질문"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#11
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 열린 질문

# 41. 플랫폼 아키텍처·외부 API — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 판단 배치의 단절 대응, 외부 API 의 수명주기와 전달 보장, 국내 표준 여부가 아직 확인되지 않았다.
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

판단 배치의 단절 대응, 외부 API 의 수명주기와 전달 보장, 국내 표준 여부가 아직 확인되지 않았다.

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-05) 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-05) 로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-05) 로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-05) 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-05 | 41. 플랫폼 아키텍처·외부 API 의 "열린 질문" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1022건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 274개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- competency-question: 역량 질문 (Competency Question (CQ))
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- configuration-copilot: 구성 코파일럿 (Configuration Copilot)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- confused-deputy: 혼란된 대리인 (Confused Deputy)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- failure-explanation: 실패 설명 (Failure Explanation)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [41] 에 걸린 0건 / 전체 205건)

```markdown
없음
```
