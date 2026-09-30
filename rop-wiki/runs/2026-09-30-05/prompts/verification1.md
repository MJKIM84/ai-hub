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
- verification_stage: first
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
        "ref-1023"
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
        "ref-1023"
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
        "ref-1024"
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
        "ref-1031"
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
        "ref-1031"
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
        "ref-1026"
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
        "ref-1035"
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
        "ref-1030"
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
        "ref-1024",
        "ref-1032",
        "ref-1031",
        "ref-1025",
        "ref-1023",
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
        "ref-1035",
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
        "ref-1026",
        "ref-1033",
        "ref-031",
        "ref-1028",
        "ref-1027",
        "ref-1023"
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
        "ref-1024",
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
        "ref-1031",
        "ref-1023",
        "ref-1034",
        "ref-004",
        "ref-1035",
        "ref-031",
        "ref-1026",
        "ref-1025",
        "ref-1030",
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
      "id": "ref-1023",
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
      "id": "ref-1024",
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
      "id": "ref-1026",
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
      "id": "ref-1030",
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
      "id": "ref-1031",
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
      "id": "ref-1035",
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
      "ref-1029·ref-1030 기사 제목 전체 미확인, ref-1030 발행일 미확인",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-1023~ref-1037, 예약 구간 안)로 출처 상한에 도달해 더 넣지 못했다. 재사용 2건(ref-004·ref-031 은 github_raw 로 다시 열었다; 참고문헌 목록 전체가 입력에 없어 ref-004 의 값은 규칙 파일 예시, ref-031 의 값은 같은 날 이전 브리프 2026-09-30-04 의 출처 표를 따랐다). 원문 열람: 17건 모두 열었다(webfetch 12건, github_raw 5건). 논문은 초록 페이지다. 교차 확인 1건(f11, 두 arXiv 논문이라 신뢰도 medium). 벤더 문서·기사만 근거로 한 finding(f14~f20)은 모두 vendor_claim: true·태그 추정·'벤더 주장' 첫머리로 냈다. 분류 원문 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에는 f21 로 답했고 결론은 '로봇–현장 서버–클라우드 혼합 배치 + REST·이벤트 API·웹훅·SDK 를 인증·권한과 함께 여는 조합'이라는 추정이다. 현장 유형 사례는 병원(f13)·제조 공장(f12)·물류창고(f17·f18, 벤더 주장)·기타(f14, 사무 건물, 벤더 주장)이며 상업 시설·가정·실외 사례는 찾지 못했다. 국내 자료는 네이버(ref-1025)·뉴스핌(ref-1029)·로봇신문(ref-1030) 세 건이고 국내 표준은 찾지 못했다. L. AI·학습 기술 관련 finding 은 없다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(네이버 ARC eye 의 디지털 트윈 언급은 위치 추정용 현재 상태 표현으로만 인용). 용어집에 이미 있는 포그 컴퓨팅·브레인리스 로봇·플릿 어댑터·플릿 제어 수준·MQTT·JSON 스키마·의미적 버전 관리·멱등성 키는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
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

### docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md (요약)

```markdown
# 42. 분산 시스템·통신·컴퓨팅 구조

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 네트워크**: 와이파이 로밍·5G·사설망, 지연·대역폭·음영 구역을 설계하고 점검한다
- **연결이 끊겨도 계속 운영**: 인터넷이나 서버가 끊겨도 현장에서 어디까지 계속 운영할지 정하고 구현한다
- **다현장 운영 구조**: 여러 현장을 한 플랫폼에서 나누어 운영하는 구조를 만든다
- **확장성·성능**: 로봇과 작업 수가 늘어도 처리 성능을 유지한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 [옛 분류원문]

> 옛 질문: 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [옛 분류원문]

## 2. 핵심 질문

인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]
```

### docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md (요약)

```markdown
# 43. 데이터·관측성·배포

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **데이터 수집·저장·보존**: 로그·이벤트·텔레메트리를 수집·저장하고 보존 기간을 정한다
- **플랫폼 관측성**: 플랫폼 서비스 자체의 상태·오류·성능을 추적한다
- **배포·업데이트 자동화**: 플랫폼 소프트웨어를 현장과 클라우드에 배포하고 되돌린다
- **운영 비용 관리**: 클라우드와 언어 모델 호출 비용을 측정하고 관리한다

## 2. 핵심 질문

플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
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

### inbox/corrections.md

````markdown
# 정정 요청함 (inbox/corrections.md)

이 파일은 위키 내용에 대한 정정 요청을 모으는 곳이다. 형식, 처리 흐름, 거부되는 경우는 docs/corrections.md(정정 요청 안내)에 있다.

- 한 요청은 `## corr-NNN` 제목으로 시작하는 블록 하나다. id 는 corr-001 부터 순서대로 늘리며, 아래 "요청 목록"에 새 블록을 덧붙인다.
- 필드는 서식의 여섯 줄(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)을 그대로 쓰고 값만 채운다. 각 필드는 한 줄로 쓴다. 페이지·문제 문장·근거·요청일은 빌드 사양서 7.4 의 필드이고, 요청자·상태는 구축자가 더한 것이다. [가정]
- 상태는 요청자가 `open` 으로 쓴다. `applied`(반영됨)·`rejected`(반영하지 않음)는 퍼블리셔가 바꾸고, 그때 "처리 실행"과 "처리 메모" 줄을 덧붙인다.
- 리서치 에이전트는 다음 실행에서 이 파일 전체를 읽는다. 대상 페이지에 걸린 `open` 요청은 반드시 조사 질문에 들어가고, 내용 검증 에이전트가 1차 검증 항목 11(정정 요청 반영 여부)로 확인하며, 처리 결과는 docs/changelog.md(변경 이력)에 남는다.
- 분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다. 새 주제나 우선 영역은 config/priority.yaml 에 적는다.

## 서식

아래 블록을 복사해 "요청 목록" 끝에 붙이고, 제목의 `corr-NNN` 을 실제 id 로 바꾼 뒤 값을 채운다. 코드 펜스 안의 서식은 요청으로 읽히지 않는다(정정 요청을 읽는 스크립트는 코드 펜스 안의 `## corr-` 줄을 제외해야 한다). [가정]

```markdown
## corr-NNN

- 페이지: docs/<경로>/<파일>.md
- 문제 문장: "페이지에 있는 문장을 태그까지 그대로 옮긴다"
- 근거: 출처 URL 또는 설명
- 요청일: YYYY-MM-DD
- 요청자: 이름 또는 역할
- 상태: open
```

## 요청 목록

(아직 요청이 없다.)
````

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-09-30-04/research.md

```markdown
# 리서치 브리프 2026-09-30-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-04 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 16. 장소 의미·지도 관리 |
| 대분류 | D. 공간·지도 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 지도 버전(mapId·mapVersion), 구역 집합(zoneSet), 대체 이름(alt_name), 의미 지도, 3차원 장면 그래프 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정(청소 로봇 의미 지도 갱신), 병원(평면도 주요 위치 주석), 기타(로봇 친화형 건축물 정밀지도) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 장소 이름 레지스트리, 지도·구역 집합 버전 배포·활성화, 차선 폐쇄, 지도 변경 감지·갱신, 계층형 의미 지도 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDA 5050 지도·구역, LIF, IMDF, IEEE 1873, Open-RMF 교통 편집기·LaneRequest, osmAG 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 반영 안 됨
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]
2. 장소의 이름·별칭·용도·접근 제한을 표현하는 표준·오픈소스 모델(IMDF, Open-RMF 교통 편집기, LIF, IEEE 1873, 계층형 의미 지도)은 무엇이며 각각 무엇을 표현하는가? (섹션 4·6·7 겨냥)
3. 지도 버전과 임시 통제 구역은 로봇–관제 인터페이스(VDA 5050, Open-RMF)에서 어떻게 배포·활성화·폐기되며 누가 책임지는가? (섹션 6·7·9 겨냥)
4. 공간이 바뀔 때 지도와 장소 의미를 갱신하는 연구와 운영 사례(가정·물류창고·병원 등)는 무엇이며 어떤 결과를 보고하는가? (섹션 5·8 겨냥)
5. 국내 공간정보·건축물 인증 체계는 로봇용 지도·장소 정보를 어떻게 다루는가? (섹션 3·5 겨냥, 한국 자료 우선)
6. 장소 의미·지도 관리에서 ROP가 직접 맡을 것과 로봇 자체 지도 작성·갱신, 건물 데이터 소유자, 설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)
7. oq-193 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추는가? (섹션 5·11 겨냥; oq-188·oq-190 은 11절 반영 대상으로만 확인)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 명세에서 지도는 작업 공간 구역을 가리키는 mapId 와 갱신을 나타내는 mapVersion 의 조합으로 식별되고 상태는 ENABLED·DISABLED 이며, 관제(fleet control)가 downloadMap·enableMap·deleteMap 즉시 동작으로 지도 서버의 지도를 로봇에 내려받게 하고 활성화하되 같은 mapId 에서는 한 버전만 활성화된다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f2 | [사실] | VDA 5050 3.0.0 명세는 올바른 지도가 활성화되도록 보장하는 책임을 관제에 두고, 로봇이 스스로 지도를 지우지 못하게 하며 사용 중인 지도의 삭제 요청은 로봇이 거부하게 한다. | ref-031 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f3 | [사실] | VDA 5050 3.0.0 명세는 진입 금지(BLOCKED)·유도선 주행(LINE_GUIDED)·해제(RELEASE)·재계획 조율·속도 제한·동작 구역과 우선·벌점·방향 구역을 구역 유형으로 두고, 구역 묶음(zoneSet)은 전역 고유 zoneSetId 를 가지며 mapVersion 이 아니라 mapId 에 묶이고 mapId 당 하나만 활성화되며 내용이 바뀌면 새 zoneSetId 가 필요하다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f4 | [사실] | VDA 5050 3.0.0 명세는 경로·경로망·스테이션 정의 같은 설정을 구현 단계의 일로 보고 명세 범위 밖에 두며, 구현 단계에서 LIF(Layout Interchange Format)로 경로를 관제에 가져올 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [사실] | VDMA 의 LIF 는 무인운반차 통합사업자가 궤도 레이아웃(에지·노드·스테이션의 모음)을 제3자 상위 관제 시스템으로 넘기기 위한 교환 형식이며, 공식 저장소 README 기준 1.0.0 판은 2023-09 에 나왔다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f6 | [사실] | IMDF 의 Unit(실내의 구별되는 공간)은 기능 분류(category)·접근 제한(restriction)·접근성(accessibility)·이름(name)·대체 이름(alt_name)·표시 지점(display_point)·소속 층(level_id)을 속성으로 가지며, 분류에는 승강기·에스컬레이터·계단·경사로·방·화장실·비공개 구역 등이 있다. | ref-1026 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f7 | [사실] | IMDF 용어집에서 이름(name)은 현실에 물리적으로 있고 보행자에게 표시되어야 할 기준 레이블이고, 대체 이름(alt_name)은 공간·물체·서비스를 가리키는 동의어로 색인·질의·검색에 쓰이며, 접근 제한(restriction)은 직원 전용처럼 일반 대중의 일부에게만 허용된 공간을 나타낸다. | ref-1027 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f8 | [사실] | OGC 는 IMDF 1.0.0 을 커뮤니티 표준 20-094 로 2021-02-02 승인하고 2021-02-18 게시했으며, 이 표준은 venue·building·level·unit·opening·fixture·anchor·occupant·geofence 등 16개 지형지물 유형을 정의한다. | ref-1028 | 아니오 | medium | 2021-02-18 | — | — |
| f9 | [사실] | Open-RMF 교통 편집기에서 로봇이 어떤 경유점에서 끝나는 작업을 주려면 그 경유점에 이름을 붙여야 하며, 경유점에는 주차(is_parking_spot)·대기(is_holding_point)·충전(is_charger)·디스펜서·인제스터 같은 속성을 달고, 층별 경유점(좌표·높이·이름)·벽·문·차선을 담은 .building.yaml 을 building_map_generator 로 항법 그래프로 내보내 플릿 어댑터가 쓴다. | ref-079 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | Open-RMF 의 차선 요청 메시지(LaneRequest)는 플릿 이름과 열 차선(open_lanes)·닫을 차선(close_lanes)의 차선 번호 배열로 이루어져, 지도 파일을 다시 만들지 않고 운영 중에 항법 그래프의 특정 차선을 닫거나 다시 열게 한다. | ref-569 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f11 | [사실] | 에스토니아 타르투 대학병원 현장 시험에서는 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소와 함께 주요 위치를 주석해 로봇 운반 작업의 목적지를 정했고, 이 지도로 중환자실에서 검사실까지 혈액 검체를 운반했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 작업 대상 | 원문 미열람 |
| f12 | [사실] | Narayana 외(IROS 2020)는 실제 가정의 바닥 청소 로봇 수천 대에 배포한 평생 의미 지도(lifelong semantic map)에서, 로봇 원시 지도가 주행마다 달라져도 사용자와 공유하는 의미 정보를 새 지도로 옮기고(공간 의미 전이), 메타 의미 계층으로 동적 물체 때문에 생긴 의미 충돌을 찾아 해소하며, 새로 탐색한 공간의 의미를 찾아 더하는 방법을 제시했다. | ref-1036 | 아니오 | medium | 2020-10 | 가정 / 작업 대상 | — |
| f13 | [사실] | 연계 대상: Stefanini 외(Sensors, 2023)의 LiDAR 점유 격자 지도 갱신 알고리즘은 격자 변화가 여러 스캔에서 반복될 때만(버퍼 10회 중 7회 이상) 지도에 반영하고, 감지된 변화량이 위치 추정 오류가 의심되는 범위이면 갱신을 멈춰 지도 오염을 막으며, 모의 창고 100개 시나리오와 80 m² 실험실에서 갱신 지도로 평균 위치 오차를 10 cm 아래(정적 지도는 50 cm 초과)로 유지했다고 보고했다. | ref-1037 | 아니오 | medium | 2023-07 | 예외·성과 | — |
| f14 | [사실] | Hughes 외(IJRR)는 3차원 장면 그래프를 물체·장소·방·건물 같은 추상화 층으로 환경을 묶는 계층형 공간 표현으로 제시하고, 시각·관성 데이터로 이를 실시간 구축하는 공개 소스 시스템 Hydra 를 Clearpath Jackal·Unitree A1 로봇으로 시험했다. | ref-347 | 아니오 | medium | 2023-05 | — | — |
| f15 | [사실] | Feng 외의 osmAG 는 OpenStreetMap XML 형식 위에 실내·실외 다층 환경의 계층형 위상·거리 의미 지도를 담는 파일 형식으로, 기존 OSM 도구로 사람이 읽고 고칠 수 있으며 로봇의 이동 방식과 속성을 고려한 전역 경로 계획을 지원하는 ROS 연동 C++ 라이브러리를 함께 제공한다. | ref-1031 | 아니오 | medium | 2023-09 | — | — |
| f16 | [사실] | Xie·Schwertfeger·Blum 의 osmAG-LLM(RA-L 2026 채택)은 금방 낡는 고정밀 물체 지도 대신 osmAG 의미 지도를 환경 맥락으로 쓰고 대규모 언어 모델(LLM)이 방 속성 같은 지도 단서로 옮겨졌거나 지도에 없는 물체의 위치를 추론하게 해, 동적·미기록 대상에서 기존 방법보다 나은 탐색 성공을 보고했다. | ref-1032 | 아니오 | medium | 2025-07 | — | — |
| f17 | [사실] | IEEE 1873-2015(Robot Map Data Representation for Navigation)는 항법하는 이동 로봇의 2차원 메트릭·위상 지도에 대한 데이터 모델과 데이터 형식을 정한 IEEE 로봇자동화학회(RAS) 표준으로 2015-09-03 승인·2015-10-26 발행됐으며, 10년 안에 개정되지 않아 2026-03-26 비활성 보류(Inactive-Reserved) 상태가 됐다. | ref-1033 | 아니오 | medium | 2026-03-26 | — | — |
| f18 | [사실] | 지디넷코리아(2022-04-11)에 따르면 네이버 제2사옥 1784 는 스마트도시협회가 처음 실시한 로봇 친화형 건축물 인증(4개 부문·25개 평가 범주)을 받았고, 평가위원은 이 건물이 로봇이 인식하는 정밀지도와 측위 인프라를 제공하며 이동형 서비스 로봇의 승강기 이동을 지원한다고 평가했다. | ref-956 | 아니오 | low | 2022-04-11 | 기타 / 수행 자원 | — |
| f19 | [사실] | 국토지리정보원은 지하철·철도역사와 평창동계올림픽 관련 시설 등을 대상으로 LoD2 수준의 실내공간정보(2차원 도면·3차원 성과, shp·3ds·max 형식)를 구축해 공간정보 오픈 플랫폼(브이월드)으로 제공하며, 활용처로 길안내·시설물관리·안전·소방을 들고 로봇 활용은 언급하지 않는다. | ref-1035 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에 대해, 같은 이름은 장소마다 고유 식별자·기준 이름·별칭·용도 분류·접근 제한을 둔 장소 목록을 지도 요소(경유점·공간·스테이션)에 묶는 방식으로 표현되고(f6·f7·f9), 공간 변경은 지도 자체의 버전 교체(mapId·mapVersion)와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 나뉘어 관리되는 것으로 보인다(f1·f3·f10). | ref-1026, ref-1027, ref-079, ref-031, ref-569 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇이 만든 원시 지도는 주행과 환경 변화에 따라 계속 달라지는데(f12·f13) 작업 목적지와 사용자 대화는 장소 이름으로 이루어지므로 이름과 지도 요소의 연결을 버전이 바뀌어도 유지해야 하고, VDA 5050 이 올바른 지도 활성화 책임을 관제에 두므로(f2) 여러 제조사 로봇을 묶는 ROP 가 그 책임을 이어받게 되기 때문이다. | ref-1036, ref-1037, ref-031, ref-079 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 16. 장소 의미·지도 관리에서 ROP 가 직접 맡을 범위는 장소 목록(식별자·이름·별칭·용도·접근 제한)의 관리와 제조사별 지도 요소와의 연결(f6·f7·f9), 제조사별 지도·구역 집합의 버전 기록과 배포·활성화 지시(f1·f2·f3), 공사·청소 같은 임시 통제 구역과 차선 폐쇄의 선언·해제(f3·f10), 사람이 층·공간·장소를 고치는 편집 화면과 변경 이력이다. | ref-1026, ref-1027, ref-079, ref-031, ref-569 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM 지도 작성·점유 격자 갱신·장면 그래프 구축 같은 센서 기반 지도 생성(f13·f14)은 로봇 자체 지능·제어에, 공공 실내공간정보·BIM 같은 건물 공간 데이터의 구축·갱신(f19)은 건물·공공 데이터 소유자에, 승강기 운행은 시설·설비 제어에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 만든 지도·데이터를 받아 장소 의미를 붙이고 버전을 관리하는 인터페이스를 맡을 것으로 보인다. | ref-1037, ref-347, ref-1035, ref-031 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 이 영역은 기준 평면도를 주는 14. 도면·BIM에서 지도 만들기(f11), 좌표 정렬·공간 그래프를 다루는 15. 지도·공간·위치 모델(f9·f15), 대화로 지도를 고치고 장소 이름을 찾는 8. 채팅으로 맵 작성과 12. 채팅으로 업무 지시·오케스트레이션(f7·f16), 현재 활성 지도 버전·폐쇄 구역을 알아야 하는 18. 실시간 세계 상태·데이터 일관성(f1·f10), 차선 폐쇄를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f10), 지도 교환 표준을 다루는 21. 상호운용 표준·적합성(f5·f8·f17), 버전 이력을 다루는 57. 자산·소프트웨어 수명주기 관리(f1), 접근 제한 공간을 다루는 51. 인증·권한·격리(f7), 장면 이해를 다루는 45. 문서·도면·장면 이해(f14·f16), 적용 현장인 63. 병원·의료(f11)·65. 가정·공동주택(f12)·67. 기타 현장(f18)과 이어진다. | ref-869, ref-079, ref-1031, ref-1027, ref-1032, ref-031, ref-569, ref-046, ref-1028, ref-1033, ref-347, ref-1036, ref-956 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | medium | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-1026 | Apple (Apple Business Register) | Unit - Indoor Mapping Data Format | 미확인 | 표준 | high | 2026-09-30 | https://register.apple.com/resources/imdf/types/unit | 아니오 |
| ref-1027 | Apple (Apple Business Register) | Glossary - Indoor Mapping Data Format | 미확인 | 표준 | high | 2026-09-30 | https://register.apple.com/resources/imdf/glossary | 아니오 |
| ref-1028 | Open Geospatial Consortium (OGC) | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 2021-02-18 | 표준 | high | 2026-09-30 | https://docs.ogc.org/cs/20-094/index.html | 아니오 |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-347 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (IJRR) | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 2023-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2305.07154 | 아니오 |
| ref-1031 | Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv) | osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics | 2023-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2309.04791 | 아니오 |
| ref-1032 | Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv) | osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning | 2025-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.12753 | 아니오 |
| ref-1033 | IEEE Standards Association (IEEE RAS) | IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation | 2015-10-26 | 표준 | medium | 2026-09-30 | https://standards.ieee.org/standard/1873-2015.html | 아니오 |
| ref-956 | 지디넷코리아 | 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 | 2022-04-11 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20220411142336 | 아니오 |
| ref-1035 | 국토지리정보원 | 실내공간정보 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.ngii.go.kr/kor/content.do?sq=324 | 아니오 |
| ref-1036 | Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020) | Lifelong update of semantic maps in dynamic environments | 2020-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2010.08846 | 아니오 |
| ref-1037 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066) | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 2023-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/ | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/place-semantics-and-map-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(원시 지도 변화와 이름 기반 작업·관제 책임), f20(핵심 질문 답, 추정) / 섹션 4: 지도 버전 f1, 구역 집합 f3, 이름·대체 이름·접근 제한 f6·f7, 의미 지도 f12, 3차원 장면 그래프 f14 / 섹션 5: 병원 — f11(타르투 대학병원 평면도 주요 위치 주석, 재인용), 가정 — f12(청소 로봇 의미 지도 갱신), 기타 — f18(네이버 1784 정밀지도·측위 인프라, 기사 기준 신뢰도 low). 여섯 항목 중 시작 조건·완료·인계 근거는 부족함을 명시. 물류창고 사례는 모의 실험(f13)뿐이라 현장 사례로 쓰지 않음 / 섹션 6: 장소 목록과 지도 요소 연결 f6·f7·f9, 지도 버전 배포·활성화 f1·f2, 임시 통제 구역 f3·차선 폐쇄 f10, 지도 변경 감지·갱신 f13(연계 대상), 평생 의미 지도 f12, 계층형 의미 지도 f14·f15, LLM 과 의미 지도 f16 / 섹션 7: VDA 5050 f1~f4, LIF f5, IMDF f6~f8, Open-RMF f9·f10, IEEE 1873 f17(비활성 보류 명시), osmAG f15 / 섹션 8: f12~f16, f19(국내 공공 실내공간정보) / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 8, 12, 14, 15, 18, 21, 27, 45, 51, 57, 63, 65, 67 / 섹션 11: 기존 oq-188·oq-190·oq-193 과 open_questions_new 5건. 다음 실행 후보: 21. 상호운용 표준·적합성 페이지에 f5·f8·f17 반영, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 지도 버전 | Map Version (VDA 5050 mapId / mapVersion) | 같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 에서는 관제가 내려받게 한 여러 버전 가운데 한 버전만 활성화해 로봇이 쓰게 한다. |
| 대체 이름 | Alternative Name (IMDF alt_name) | IMDF 에서 공간·물체·서비스를 가리키는 동의어나 다른 표현으로, 기준 이름(name)과 별도로 색인·질의·검색에 쓰인다. |
| 의미 지도 | Semantic Map | 기하 지도 위에 방·구역·물체의 이름과 용도 같은 높은 수준의 정보를 얹어 로봇과 사람이 함께 쓰는 공간 표현이다. |
| 3차원 장면 그래프 | 3D Scene Graph | 물체·장소·방·건물 같은 추상화 층을 노드와 관계로 묶어 환경을 여러 해상도로 표현하는 계층형 공간 그래프다. |

## 열린 질문

새로 생긴 질문:

- 제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 15. 지도·공간·위치 모델 | 근거: f1 | 종류: 일반
- IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 21. 상호운용 표준·적합성 | 근거: f17 | 종류: 일반
- 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 40. 운영 절차·요청 창구, 63. 병원·의료 | 근거: f3 | 종류: 일반
- IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 12. 채팅으로 업무 지시·오케스트레이션 | 근거: f7 | 종류: 일반
- 국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? | 관련 영역: 16. 장소 의미·지도 관리, 67. 기타 현장 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 13건
- 미확인 항목:
    - f5 LIF 스키마의 layoutVersion·stationName 등 필드는 검색 요약에만 나와 README·스키마 원문으로 확인하지 못함(GitHub 저장소 페이지 403, VDMA 가이드라인 PDF 본문 추출 실패)
    - f13 수치는 저자 보고이며 교차 확인 실패
    - f14·f15·f16·f12 는 초록 기준이며 본문 실험 조건 미확인
    - f17 IEEE 1873 표준 본문(유료) 미열람, Amigoni 외 해설 논문(oru.diva-portal.org)은 ECONNRESET 으로 열지 못함
    - f18 기사 기준이며 스마트도시협회 인증 원자료 미확인
    - Nav2 금지 구역·속도 필터(costmap filter) 문서는 docs.nav2.org·raw 경로 404, navigation.ros.org 연결 거부로 열지 못해 넣지 않음
    - MiR 지도 편집기(바닥 계층과 구역·위치 구성 요소, 로봇 수 제한 구역)는 PDF 본문 추출 실패로 넣지 않음
    - oq-193 건설 현장 지도–BIM 동기화 주기는 이번 조사에서도 확인되지 않음
    - oq-188·oq-190 은 조사하지 않음(11절 반영 대상으로만 둠)
    - 물류창고·제조 공장·상업 시설의 실제 운영 현장에서 지도 버전·장소 이름을 관리한 공개 사례는 확인하지 못함
- 범위 경계 위반 의심:
    - f13: 로봇 점유 격자 지도 갱신은 분류 원문 19장의 로봇 자체 지능·제어(SLAM)이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 장면 그래프를 센서로 구축하는 부분은 로봇 인식(연계 대상)이며 계층형 표현 구조만 이 영역 근거로 쓰도록 제안함(f23 에서 구분)
    - f19: 공공 실내공간정보 구축은 공공 데이터 소유자의 일이므로 입력 데이터 가용성 근거로만 제안함
    - f23: SLAM·건물 데이터 구축·승강기 운행을 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 18회/30, 신규 출처 13건/15, 재사용 3건(ref-031·ref-079 는 github_raw 로 다시 열었고 ref-869 는 2026-09-30-03 브리프 재인용으로 이번에 열지 않음). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1014 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-03)가 ref-1015·ref-1017·ref-1019·ref-1024 를 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-046~ref-1037 을 순서대로 썼다. 원문 열람: 신규 13건 모두 열었다(webfetch 11건, github_raw 2건). 논문은 대부분 초록 페이지이고 Stefanini 외(ref-1037)만 PMC 본문을 열었다. 열지 못해 쓰지 않은 것: Nav2 문서(404·연결 거부), MiR Fleet 참조 안내서 PDF(본문 추출 실패), VDMA LIF 가이드라인 PDF(본문 추출 실패), LIF GitHub 저장소 페이지(403), MDPI·preprints.org(403), IEEE 1873 해설 논문(ECONNRESET). 교차 확인 0건, 신뢰도 high finding 없음(사실 finding 은 모두 단일 출처; IMDF 는 Apple 문서와 OGC 게시본이 같은 원천이라 독립 출처로 보지 않음). 분류 원문 핵심 질문(같은 장소를 같은 이름으로 부르고 공간이 바뀌면 지도를 따라 바꾸기)에는 f20 으로 답했고, 결론은 '장소 목록을 지도 요소에 묶고, 지도 버전 교체와 지도와 따로 배포되는 임시 통제(구역 집합·차선 폐쇄)로 변경을 나눠 관리한다'는 추정이다. 현장 유형 사례는 병원(f11, 재인용)·가정(f12)·기타(f18)이며, 물류창고 근거는 모의 실험(f13)뿐이라 site_type 을 null 로 두었다. 국내 자료는 국토지리정보원(ref-1035)·지디넷코리아(ref-956) 두 건이며 국내 로봇 지도 표준(KS)은 검색 2회에서 찾지 못했다. L. AI·학습 기술 관련(f14 장면 그래프, f16 LLM 추론)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 8. 채팅으로 맵 작성에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 활성 지도 버전·폐쇄 구역으로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 IMDF·IndoorGML·LIF·구역 집합·차선 폐쇄·필터 마스크·위상 지도·반정적 객체·공간 그래프는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-188·oq-190·oq-193 은 해결되지 않았다.
```

### runs/2026-09-30-03/research.md

```markdown
# 리서치 브리프 2026-09-30-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-03 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 14. 도면·BIM에서 지도 만들기 |
| 대분류 | D. 공간·지도 모델 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 기준점(fiducial), 공간 경계, 설계–준공 편차, 포즈 그래프 지도 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(도면 주석·로봇 지도 정합), 기타(대학 건물 BIM 기반 위치 추정) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 래스터 평면도 벡터화, CAD 기호 인식, BIM→점유 격자·위상 지도 변환, 축척 보정·좌표 변환 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IFC 4.3(IfcSpace·IfcTransportElement), Open-RMF 교통 편집기·플릿 어댑터 좌표 변환 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — CubiCasa5K, Raster-to-Vector, FloorPlanCAD, AI Hub 건축 도면 데이터, BIM 기반 위치 추정 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 반영 안 됨
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]
2. 평면도(이미지·CAD)에서 벽·문·공간·기호를 인식하는 대표 방법과 공개 데이터셋(국내 데이터 포함)은 무엇이며 보고된 성능은 어느 수준인가? (섹션 4·6·8 겨냥)
3. IFC 같은 BIM(Building Information Modeling)에서 공간·문·승강기를 가져와 로봇 지도(점유 격자·위상 지도)를 만드는 표준 요소·연구·도구는 무엇인가? (섹션 6·7·8 겨냥)
4. 도면 픽셀을 미터로 보정하고 제조사별 로봇 지도를 도면 좌표에 맞추는 절차는 오픈소스 관제(Open-RMF)와 제품에서 어떻게 이루어지며, 누가 확인하는가? (섹션 5·6·7 겨냥, oq-126 관련)
5. 도면·BIM 과 실제 현장이 다를 때(설계–준공 편차, 가구·배치 변경) 어떻게 확인하고 반영하는가? (섹션 3·6·11 겨냥, oq-193 관련)
6. 병원·건설 현장 등 실제 현장에서 도면 기반 지도를 쓴 사례는 무엇이며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥)
7. 도면·BIM 지도 작성에서 ROP가 직접 맡을 것과 로봇 자체 위치 추정·BIM 저작·설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 교통 편집기(traffic-editor)는 건축 도면 같은 기존 평면도 이미지를 배경으로 불러와 그 위에 교통 기반 시설을 그리게 하며, 주석은 기준 평면도 이미지의 왼쪽 위를 원점으로 하는 픽셀 좌표로 만들어지고 평면도가 제조사별 로봇 지도의 기준 좌표계 역할을 한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f2 | [사실] | Open-RMF 교통 편집기에서 도면 축척은 도면의 축척 막대처럼 실제 거리를 아는 두 점 사이에 측정선을 긋고 실제 길이를 미터로 입력해 층별 픽셀–미터 비율을 정하는 방식으로 설정한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f3 | [사실] | Open-RMF 교통 편집기는 여러 층을 맞출 때 기둥처럼 층 사이에 수직으로 같은 위치에 있을 것으로 기대되는 기준점(fiducial)을 층마다 찍고, 이를 대응시켜 층 사이의 이동·회전·축척 변환을 자동으로 계산한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f4 | [사실] | Open-RMF 교통 편집기에서 도면 위에 주석으로 표현하는 요소는 벽, 문(여닫이·미닫이 등 유형 지정), 여러 층에 걸친 승강기(층별 카 문 위치 포함), 이동 그래프를 이루는 차선(lane), 충전 위치(is_charger 속성의 지점)다. | ref-079 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f5 | [사실] | Open-RMF 교통 편집기는 로봇이 만든 지도를 레이어로 불러와 축척·이동·회전 변환을 주어 기준 평면도와 겹치도록 맞추게 한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 교통 편집기 좌표계가 다르면 두 좌표계에서 서로 대응하는 지점 쌍(reference_coordinates)을 설정 파일에 적게 하고 최소 4개 대응 지점을 권장하며, nudged 라이브러리로 회전·축척·이동 변환을 추정해 명령 좌표를 자동으로 바꾼다. | ref-153 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | Valner 외(Frontiers in Robotics and AI, 2022-08)에 따르면 에스토니아 타르투 대학병원 현장 시험에서는 PAL Robotics TIAGo 를 원격 조작해 SLAM 으로 격자 지도를 만들고, 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소·주요 위치를 주석한 뒤 격자 지도를 평면도에 정합해 두 좌표 표현 사이 변환을 정했으며, 이 지도로 중환자실에서 검사실까지 시간이 중요한 혈액 검체를 운반하고 RFID·근접 센서로 여는 반자동 문 두 곳을 통과했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 수행 자원 | — |
| f8 | [사실] | 같은 타르투 대학병원 시험의 저자들은 넓은 구역을 한 번에 매핑하면 누적 불확실성 때문에 지도가 비틀리기 쉬우므로 작은 구역으로 나눠 매핑하고 하위 지도를 손으로 합치는 편이 더 정확하다고 보고했다. | ref-869 | 아니오 | medium | 2022-08-23 | 병원 / 예외·성과 | — |
| f9 | [사실] | IFC 4.3 문서에서 IfcSpace 는 건물 안에서 특정 기능을 제공하는 실제 또는 이론상 경계로 둘러싸인 면적·부피이며, IfcRelAggregates 로 층(building storey, 외부 공간은 site)에 속해 공간 계층을 이루고 IfcRelSpaceBoundary 로 물리적·가상 경계가 정의된다. | ref-156 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | IFC 4.3 문서에서 IfcTransportElement 는 시설 안에서 사람·동물·물품을 옮기는 운송 요소 전체를 일반화한 요소로, 승강기(lift)·에스컬레이터·무빙워크를 포함하며 PredefinedType 이나 IfcTransportElementType 으로 구분한다. | ref-213 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f11 | [사실] | Kalervo 외(2019)의 CubiCasa5K 는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 주석한 데이터셋이며, 저자들은 휴리스틱·저수준 픽셀 연산 대신 개선된 다중 작업 합성곱 신경망으로 평면도를 자동 해석하는 방법을 함께 제시했다. | ref-063 | 아니오 | medium | 2019-04 | — | — |
| f12 | [사실] | Liu·Wu·Kohli·Furukawa(ICCV 2017)의 Raster-to-Vector 는 신경망으로 벽 모서리·문 끝점 같은 접합점을 찾고 정수 계획법으로 이를 벽선·문선·아이콘 상자로 묶어 위상·기하가 일관된 벡터 평면도를 만들며, 저자 평가에서 정밀도·재현율 약 90%를 얻고 실제 서비스용 평면도 이미지 수십만 장을 벡터로 변환했다고 보고했다. | ref-1015 | 아니오 | medium | 2017 | — | — |
| f13 | [사실] | Fan 외(ICCV 2021)의 FloorPlanCAD 는 주거·상업 건물의 벡터 CAD 평면도 1만 장 이상을 30개 객체 범주로 선 단위 주석한 데이터셋으로, 셀 수 있는 사물 인스턴스와 셀 수 없는 영역의 의미를 함께 찾는 파놉틱 심볼 스포팅 과제와 CNN–GCN 결합 방법을 제시했다. | ref-067 | 아니오 | medium | 2021-05 | — | — |
| f14 | [사실] | AI Hub 의 '건축 도면 데이터'(2022년 구축, 주관기관 에이치씨아이플러스)는 평면도 41,556장을 포함한 건축 도면 48,033장으로 이루어지며, 출입문·창호·벽체 등 구조 8종, 거실·침실·주방·현관·화장실 등 공간 12종, 객체 5종 라벨과 문자 인식(OCR) 304,462건을 담은 인공지능 학습용 데이터다. | ref-1019 | 아니오 | medium | 2026-09-30 | — | — |
| f15 | [사실] | 연계 대상: Hendrikx 외(ICRA 2021)는 IFC 형식 BIM 의 의미 요소를 로봇용 세계 모델 표현으로 바꿔 공간 데이터베이스에 저장하고, 로봇 주변의 구조 요소를 질의해 특징 검출기를 설정한 뒤 그래프 기반 방법으로 위치를 추정해, 2D LiDAR 와 주행거리계만 가진 로봇이 BIM 이 있는 대형 대학 건물에서 자세를 추적할 수 있음을 보였다. | ref-1017 | 아니오 | medium | 2021 | 기타 | — |
| f16 | [사실] | Vega Torres·Braun·Borrmann(ECPPM 2022)은 복잡한 BIM 에서 구조 요소만 담은 2D 점유 격자 지도를 자동 생성하고 이를 포즈 그래프 지도로 바꾸는 방법을 제안했으며, BIM 과 현실의 차이(Scan-BIM 편차)가 가구·잡동사니뿐 아니라 설계 모델과 준공 상태의 차이에서도 생긴다고 지적하고, 제안 방법이 변화·동적 환경에서 일반 AMCL 보다 강건하게 위치를 추정했다고 보고했다. | ref-081 | 아니오 | medium | 2022-09 | 제약 | — |
| f17 | [사실] | 연계 대상: 같은 연구진의 BIM-SLAM(ISARC 2023, arXiv 2024-08)은 BIM 에서 포즈 그래프 지도·기술자 같은 세션 데이터를 먼저 만들고 다중 세션 앵커링으로 실제 LiDAR 측정과 맞추며, BIM 에 없는 요소를 찾아 묶고 표면으로 재구성해 설계 모델과 실제 실내 상태의 차이를 드러내고, 로봇의 초기 자세를 몰라도 BIM 에 정렬된 지도를 만든다. | ref-221 | 아니오 | medium | 2024-08 | 제약 | — |
| f18 | [사실] | Zhang·Wu·Ma·Schwertfeger(arXiv 2507.00552, 2025-07; 2026-03 개정)는 SLAM 매핑의 시간·노력·강건성 한계를 피하려고 건축 CAD 파일에서 구조 요소를 추출하고 AreaGraph 기반 위상 분할로 이동 가능한 공간을 나누며 CAD 의 문자 라벨을 넣고 여러 층을 합쳐 로봇 항법용 계층형 위상·거리 OpenStreetMap 실내 지도를 자동 생성하는 파이프라인과 GUI 를 공개했다. | ref-083 | 아니오 | medium | 2025-07 | — | — |
| f19 | [추정] | 모빌리오(Mobilio Robotics)는 자사 산업용 순찰 로봇 관제 솔루션이 사용자가 기둥·모서리 같은 기준점 3개 이상을 지정하면 2D LiDAR 지도를 CAD·BIM 도면에 정합하고 회전각·크기를 미세 조정해 로봇 위치를 실제 도면 위에 보여 주며, 공장·플랜트를 대상으로 한다고 주장한다. | ref-817 | 아니오 | low | 2026-08-24 | — | 벤더 주장 |
| f20 | [사실] | 엔지니어링데일리 보도에 따르면 국토교통부의 건설산업 BIM 활성화 로드맵은 설계 단계부터 BIM 100% 도입을 핵심 목표로 삼고 측량·설계·시공·감리·유지관리까지 전 단계에 BIM 을 쓰게 하며, LH 공공주택부터 BIM 적용을 의무화해 단계적으로 넓히는 계획을 담았다. | ref-1024 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에 대해, 평면도의 벽·문·공간·기호 인식과 BIM·CAD 에서 점유 격자·위상 지도를 만드는 일은 연구 수준에서 자동화가 진행됐지만(f12·f13·f16·f18), 축척 설정·로봇 지도와의 좌표 정합·설계–준공 편차 확인은 측정선·기준점 입력과 사람의 확인에 기대고 있어(f2·f3·f6·f7·f16), 현재 형태는 '자동 초안 + 사람 확인·보정'에 가깝다. | ref-1015, ref-067, ref-081, ref-083, ref-079, ref-153, ref-869 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 도면·BIM 지도가 중요한 까닭은, 넓은 공간을 로봇으로 매핑하면 지도가 비틀리기 쉽고 제조사마다 지도 좌표가 다른 반면 평면도는 여러 제조사 로봇 지도를 묶는 공통 기준 좌표와 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점을 주기 때문이다(f1·f4·f8·f10). | ref-079, ref-869, ref-213 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 14. 도면·BIM에서 지도 만들기에서 ROP 가 직접 맡을 범위는 평면도·CAD·IFC 를 받아 공간·문·승강기·충전 위치 초안과 공용 자원 목록을 만들고(f4·f9·f10), 층별 축척과 층 간 기준점을 설정하며(f2·f3), 제조사별 로봇 지도와 공통 좌표 사이 변환을 등록·관리하고(f5·f6), 도면과 현장의 차이를 표시해 사람이 확인·승인하게 하는 일이다(f16, oq-126 과 연결). | ref-079, ref-153, ref-156, ref-213, ref-081 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM·LiDAR 위치 추정(BIM 을 사전 지도로 쓰는 위치 추정 포함)은 로봇 자체 지능·제어에, 승강기 운행 제어는 시설·설비 제어에 속하고, BIM 모델의 저작·갱신은 건물 소유자·설계·시공 측 체계에 속하므로, 이종 제조사를 잇는 ROP 는 이들로부터 모델·지도를 받아 공통 공간 모델로 정합하고 차이를 확인하는 인터페이스를 맡을 것으로 보인다. | ref-1017, ref-081, ref-221, ref-213, ref-1024 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 좌표 정렬·다층 모델을 다루는 15. 지도·공간·위치 모델(f3·f5·f6), 지도 편집·버전을 다루는 16. 장소 의미·지도 관리(f1·f16), 대화로 맵을 만드는 8. 채팅으로 맵 작성(f2·f6), 도면 해석 AI 를 다루는 45. 문서·도면·장면 이해(f11~f14), 승강기·문 연동을 다루는 22. 설비·건물 시스템 연동(f4·f10), 충전 위치를 다루는 28. 공용 자원·충전·에너지 최적화(f4), 차선 그래프를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f4), 설치 때 매핑·정합을 하는 55. 현장 조사·설치·시운전(f7·f8), 현재 상태의 차이를 다루는 18. 실시간 세계 상태·데이터 일관성(f17), 병원 적용을 다루는 63. 병원·의료(f7)와 이어진다. | ref-079, ref-153, ref-081, ref-063, ref-1015, ref-067, ref-1019, ref-213, ref-869, ref-221 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-156 | buildingSMART International | IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md | 아니오 |
| ref-213 | buildingSMART International | IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main) | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1904.01920 | 아니오 |
| ref-1015 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017) | Raster-to-Vector: Revisiting Floorplan Transformation | 2017 | 논문 | medium | 2026-09-30 | https://art-programmer.github.io/floorplan-transformation.html | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021) | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2105.07147 | 아니오 |
| ref-1017 | Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021) | Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization | 2021 | 논문 | medium | 2026-09-30 | https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/ | 아니오 |
| ref-081 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022) | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 2022-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2308.05443 | 아니오 |
| ref-1019 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-817 | 모빌리오(Mobilio Robotics) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션) | 2026-08-24 | 벤더 문서 | low | 2026-09-30 | https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98 | 아니오 |
| ref-869 | Valner, R. 외 (Frontiers in Robotics and AI) | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |
| ref-083 | Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv) | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 2025-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2507.00552 | 아니오 |
| ref-221 | Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023) | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 2024-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2408.15870 | 아니오 |
| ref-1024 | 엔지니어링데일리 | "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 … (제목 일부만 확인) | 미확인 | 기사 | low | 2026-09-30 | https://www.engdaily.com/news/articleView.html?idxno=12613 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(공통 기준 좌표·공용 자원 목록의 출발점), f8(넓은 구역 매핑의 누적 오차), f20(국내 BIM 전 단계 적용 정책, 기사 기준 신뢰도 low) / 섹션 4: 기준점(fiducial) f3, 공간·공간 경계 f9, 운송 요소 f10, 설계–준공 편차 f16, 포즈 그래프 지도 f16 / 섹션 5: 병원 — f7(타르투 대학병원 평면도 주석·격자 지도 정합·검체 운반), f8(예외·성과); 기타 — f15(대학 건물 BIM 기반 위치 추정, 연계 대상 표시). 여섯 항목 가운데 시작 조건·완료·인계 근거는 부족함을 명시 / 섹션 6: 래스터 평면도 벡터화 f12, CAD 기호 인식 f13, 평면도 해석 데이터셋 f11·f14, BIM→점유 격자·포즈 그래프 f16, CAD→위상 OSM f18, 축척 보정 f2, 층 정렬 f3, 로봇 지도 정합 f5·f6, 편차 검출 f17, 제품 사례 f19(벤더 주장 병기 필수), 자동화 수준 종합 f21 / 섹션 7: IFC 4.3 f9·f10, Open-RMF 교통 편집기 f1~f5, 플릿 어댑터 좌표 변환 f6 / 섹션 8: f11~f18, f7 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 8, 15, 16, 18, 22, 27, 28, 45, 55, 63 / 섹션 11: 기존 oq-126·oq-193 과 open_questions_new 4건. 다음 실행 후보: 15. 지도·공간·위치 모델 페이지에 f6(대응점 기반 좌표 변환) 반영, 45. 문서·도면·장면 이해 페이지에 f11~f14 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 층 정렬 기준점 | Fiducial (Level Alignment Fiducial) | 기둥처럼 여러 층에서 수직으로 같은 위치에 있다고 기대되는 지점에 찍는 표식으로, 대응시킨 기준점들로 층 사이의 이동·회전·축척 변환을 계산하는 데 쓴다. |
| 공간 경계 | Space Boundary (IfcRelSpaceBoundary) | IFC 에서 공간(IfcSpace)을 둘러싼 벽·슬래브 같은 물리적 요소나 가상 경계와 그 공간을 잇는 관계로, 공간의 범위와 인접 관계를 정의한다. |
| 설계–준공 편차 | As-planned vs As-built Deviation | 설계 단계에서 만든 건물 모델과 실제 지어진 상태 사이의 차이로, BIM 을 로봇 지도로 쓸 때 위치 추정 오차의 원인이 된다. |

## 열린 질문

새로 생긴 질문:

- Raster-to-Vector 의 약 90% 정밀도·재현율처럼 보고된 평면도 인식 성능은 주로 주거용 도면 기준인데, 병원·공장·물류창고 같은 비주거 시설 도면에서 벽·문·승강기·충전 위치 인식 정확도를 보고한 자료가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f12 | 종류: 일반
- AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 승강기·계단·충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f14 | 종류: 일반
- 도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 제품 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 55. 현장 조사·설치·시운전 | 근거: f6 | 종류: 일반
- 국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 22. 설비·건물 시스템 연동 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 13회 · 신규 출처 15건
- 미확인 항목:
    - f20 국토교통부 원문 보도자료(molit.go.kr)는 ECONNRESET 으로 열지 못해 기사 기준이며, 공공공사 금액별 BIM 의무화 연도(검색 요약에만 나옴)는 넣지 않음
    - ref-1024 기사 발행일과 제목 전체 미확인
    - ref-817 모빌리오 글의 제목 전체 미확인, 정합 기능·성능은 벤더 주장이며 독립 확인 없음
    - ref-1019 AI Hub 데이터 공개일 미확인(구축 연도 2022 만 확인)
    - f11~f13·f15~f18 은 논문 초록·프로젝트 페이지 기준이며 본문의 실험 조건 미확인(Raster-to-Vector CVF 본문 403)
    - f12 의 약 90% 수치는 저자 평가이며 교차 확인 실패
    - f9·f10 은 IFC 4.3 개발 브랜치 문서 기준으로 게시판(ADD2)과의 문구 일치 미확인
    - 도면 인식 결과를 로봇 지도로 확정하는 승인 주체·시점(oq-126)은 어느 자료에서도 확인되지 않음
    - 건설 현장 지도–BIM 동기화 주기와 국내 사례(oq-193)는 이번 조사에서 확인되지 않음
    - 병원 외 현장 유형(물류창고·제조 공장·상업 시설)의 도면 기반 지도 사례는 벤더 주장(f19) 외에 확인되지 않음
- 범위 경계 위반 의심:
    - f15·f17: BIM 을 사전 지도로 쓰는 로봇 위치 추정·SLAM 은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·SLAM)이므로 claim 을 '연계 대상: '으로 시작함
    - f16: BIM→점유 격자 지도 생성은 직접 범위 후보이나 AMCL 비교 등 위치 추정 성능 부분은 로봇 자체 지능·제어 쪽 근거로만 쓰도록 제안함
    - f24: 승강기 제어(시설·설비 제어), BIM 저작·갱신(건물 측 체계)을 '연계 대상: '으로 표시함
    - f20: BIM 정책은 이 영역의 입력 데이터 가용성 근거로만 쓰고 ROP 직접 범위로 서술하지 않음
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치: finding f7 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음): 직전 반환값(runs/2026-09-30-03/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. finding·출처 번호는 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-817)만 근거로 한 finding 은 f19 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 이번 f7 은 동료심사 논문(ref-869, Frontiers)에 근거한 병원 사례이며 벤더 문서를 근거로 하지 않는다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f7, f19). web_fetch_available: true · fetch_mode full. 사용량은 검색 13회/30, 신규 출처 15건/15(ref-079~ref-1024, 예약 구간 안)로 출처 상한에 도달했다. 그래서 BIM2RDT(건설 현장 BIM–로봇 디지털 트윈, arXiv 2509.20705, 열었음), 평면도 사전지식 기반 장기 위치 추정(arXiv 2303.10959), IFC→ROS 지도 도구 BIRS, Nav2 지도 YAML 형식(해상도·원점; 문서 URL 404)은 넣지 못했다. 원문 열람: 15건 모두 열었다(github_raw 4건, webfetch 11건). 논문은 대부분 초록 페이지다. 열지 못해 쓰지 않은 것: 국토교통부 보도자료·ancnews(ECONNRESET), 한국경제(403), Springer 'Improving autonomous robotic navigation using IFC files'(인증 리디렉션), CVF 논문 페이지(403). 교차 확인 0건, 신뢰도 high finding 없음(모든 사실 finding 이 단일 출처). 분류 원문 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에는 f21 로 답했고 결론은 '인식·변환은 연구 수준에서 자동화됐으나 축척·정합·편차 확인은 사람 입력·확인에 기대는 자동 초안 + 사람 확인 형태'라는 추정이다. 현장 유형 사례는 병원(f7·f8)과 기타(f15, 대학 건물)이며, 물류창고·제조 공장·상업 시설 사례는 벤더 주장(f19, 현장 유형 미특정) 외에 찾지 못했다. 국내 자료는 AI Hub(ref-1019)·엔지니어링데일리(ref-1024)·모빌리오(ref-817) 세 건이다. L. AI·학습 기술 관련(평면도 인식 f11~f14)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 14. 도면·BIM에서 지도 만들기에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 상태와 BIM 차이(f17)로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 평면도 인식·래스터–벡터 변환·파놉틱 심볼 스포팅·스캔 대 BIM 비교·지도 정합·유사 변환·IFC·점유 격자 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 은 관련 근거(f6·f7, f16·f17)가 늘었으나 해결되지 않았다.
```

### data/source_texts/ref-004.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# RMF Core Overview

This chapter describes RMF, an umbrella term for a wide range of open specifications and software
tools that aim to ease the integration and interoperability of robotic systems,
building infrastructure, and user interfaces. `rmf_core` consists of:
 - [rmf_traffic](https://github.com/open-rmf/rmf_traffic): Core scheduling and traffic management systems
 - [rmf_traffic_ros2](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_traffic_ros2): rmf_traffic for ros2
 - [rmf_task](https://github.com/open-rmf/rmf_task): Task planner for rmf
 - [rmf_battery](https://github.com/open-rmf/rmf_battery): rmf battery estimation
 - [rmf_ros2](https://github.com/open-rmf/rmf_ros2): ros2 adapters and nodes and python bindings for rmf_core
 - [rmf_utils](https://github.com/open-rmf/rmf_utils): utility for rmf

## Traffic deconfliction

Avoiding mobile robot traffic conflicts is a key functionality of `rmf_core`.
There are two levels to traffic deconfliction: (1) prevention, and (2)
resolution.

### Prevention

Preventing traffic conflicts whenever possible is the best-case scenario.
To facilitate traffic conflict prevention, we have implemented a
platform-agnostic Traffic Schedule Database. The traffic schedule is a living
database whose contents will change over time to reflect delays, cancellations,
or route changes. All fleet managers that are integrated into an RMF deployment must
report the expected itineraries of their vehicles to the traffic schedule. With
the information available on the schedule, compliant fleet managers can plan
routes for their vehicles that avoid conflicts with any other vehicles, no
matter which fleet they belong to. `rmf_traffic` provides a
[`Planner`](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Planner.hpp)
class to help facilitate this for vehicles that behave like standard AGVs (Automated Guided Vehicles),
rigidly following routes along a pre-determined grid. In the future
we intend to provide a similar utility for AMRs (Autonomous Mobile Robots) that can perform ad hoc motion
planning around unanticipated obstacles.

### Negotiation

It is not always possible to perfectly prevent traffic conflicts.
Mobile robots may experience delays because of unanticipated obstacles in their
environment, or the predicted schedule may be flawed for any number of reasons.
In cases where a conflict does arise, `rmf_traffic` has a Negotiation scheme.
When the Traffic Schedule Database detects an upcoming conflict between two or
more schedule participants, it will send a conflict notice out to the relevant
fleet managers, and a negotiation between the fleet managers will begin. Each
fleet manager will submit its preferred itineraries, and each will respond with
itineraries that can accommodate the others. A third-party judge (deployed by
the system integrator) will choose the set of proposals that is considered
preferable and notify the fleet managers about which itineraries they should
follow.

There may be situations where a sudden, urgent task needs to take place
(for example, a response to an emergency), and the current traffic schedule does not
accommodate it in a timely manner. In such a situation, a traffic participant
may intentionally post a traffic conflict onto the schedule and force a
negotiation to take place. The negotiation can be forced to choose an itinerary
arrangement that favors the emergency task by implementing the third-party
judge to always favor the high-priority participant.

## Traffic Schedule

The traffic schedule is a centralized database of all the intended robot traffic
trajectories in a facility. Note that it contains the intended trajectories; it is
looking into the future. The job of the schedule is to identify conflicts in
the intentions of the different robot fleets and notify the fleets when a
conflict is identified. Upon receiving the notification, the fleets will begin
a traffic negotiation, as described above.

![Schedule and Fleet Adapters](images/rmf_core/schedule_and_fleet_adapters.png)

## Fleet Adapters

Each robot fleet that participates in an RMF deployment is expected to have a
fleet adapter that connects its fleet-specific API to the interfaces
of the core RMF traffic scheduling and negotiation system. The fleet adapter is
also responsible for handling communication between the fleet and the various
standardized smart infrastructure interfaces, e.g. to open doors, summon lifts,
and wake up dispensers.

Different robot fleets have different features and capabilities, dependent on
how they were designed and developed. The traffic scheduling and negotiation system
does not postulate assumptions about what the capabilities of the fleets will be.
However, to minimize the duplication of integration effort, we have identified 4
different broad categories of control that we expect to encounter among various
real-world fleet managers.

**Fleet adapter type** | **Robot/Fleetmanager API feature set**  | **Remarks**
--- | --- | ---
`Full Control` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Request robot to move to [x, y, yaw] coordinate</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Get route/path taken by robot to destination</li><li>ETA to destination</li><li>Read battery status of the robot</li><li>Infer when robot is done navigating to [x, y, yaw]</li><li>Send robot to docking/charging station</li><li>Switch on board map and re-localize robot.</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is provided with live status updates and full control over the paths that each individual mobile robot uses when navigating through the environment. This control level provides the highest overall efficiency and compliance with RMF, which allows RMF to minimize stoppages and deal with unexpected scenarios gracefully. *(API available)*
`Traffic Light` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Read battery status of the robot</li><li>Send robot to docking/charging station</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is given the status as well as pause/resume control over each mobile robot, which is useful for deconflicting traffic schedules especially when sharing resources like corridors, lifts and doors. *(API available)
`Read Only` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Read or infer the path that the robot will take to its current destination</li><li>Read average speed of the robot or ETA to destination</li><li>Read battery status of the robot</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is not given any control over the mobile robots but is provided with regular status updates. This will allow other mobile robot fleets with higher control levels to avoid conflicts with this fleet. _Note that any shared space is allowed to have a maximum of just one "Read Only" fleet in operation. Having none is ideal._ *(Preliminary API available)*
`No Interface` | | Without any interface to the fleet, other fleets cannot coordinate with it through RMF, and will likely result in deadlocks when sharing the same navigable environment or resource. This level will not function with an RMF-enabled environment. *(Not compatible)*

In short, the more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together.
Note again that there can only ever be one "Read Only" fleet in a shared space, as any two or more of such fleets will make avoiding deadlock or resource conflict nearly impossible.

Currently we provide a reusable C++ API (as well as Python bindings) for integrating the **Full Control** category of fleet management.
A preliminary ROS 2 message API is available for the **Read Only** category, but that API will be deprecated in favor of a C++ API
(with [Python bindings](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python/) available) in a future release.
The **Traffic Light** control category is compatible with the core RMF scheduling system, but we have not yet implemented a reusable API for it.
To implement a **Traffic Light** fleet adapter, a system integrator would have to use the core traffic schedule and negotiation APIs directly, as well as implement the integration with the various infrastructure APIs (e.g. doors, lifts, and dispensers).

The API for the **Full Control** category is described in the [Mobile Robot Fleets](./integration_fleets.md) section of the Integration chapter, and the **Read Only** category is described in the [Read Only Fleets](./integration_read-only.md) section of the Integration chapter.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope

action type | counter action | description | idempotent | parameters | linked state | instant | node | edge | zone
---|---|---|---|---|---|---|---|---|---
startPause | stopPause | Activates the pause mode. <br>A linked state is required, because many mobile robots can be paused by using a hardware switch. <br>No more automatic driving - reaching next node is not necessary. Actions that can be paused (`pauseAllowed`=`true`), shall be paused, other actions continue. Order execution is resumed after stopPause. | yes | - | paused | yes | no | no | no
stopPause | startPause | Deactivates the pause mode. <br>Movement and all other actions will be resumed (if any). <br>A linked state is required because many mobile robots can be paused by using a hardware switch. <br>stopPause can also restart mobile robots that were stopped with a hardware button that triggered startPause (if configured). | yes | - | paused | yes | no | no | no
startHibernation | stopHibernation | Initiates hibernate mode, in which the mobile robot shall remain connected to the MQTT broker but no longer needs to send state messages. The mobile robot shall report this action as 'FINISHED' before discontinuing publishing state messages and publish a connection state of 'HIBERNATING'. If the mobile robot has an active order, it shall clear it. Reaching the next node is not required.<br>While in 'HIBERNATING' connection state, mobile robot shall not be moving. The mobile robot shall only receive and respond to the instant action 'stopHibernation' and shall not respond to any other commands, such as orders or additional instant actions. <br>If the mobile robot's battery becomes critically low while in this mode, the mobile robot may stop 'HIBERNATING' autonomously to report an error. In case a wake‑up time is set, the mobile robot is able to autonomously exit the 'HIBERNATING' connection state at the specified time and will publish the corresponding connection state transition before resuming normal operation. | yes | wakeUpTime (string, optional) | - | yes | no | no
stopHibernation | startHibernation | Ends hibernate mode. To initiate wake‑up while the mobile robot is in the 'HIBERNATING' state, a control device (onboard or external) shall subscribe to the `instantAction` topic and remain connected to the MQTT broker. Because the mobile robots standard control device may be partially shut down during hibernation, the wake‑up may be triggered by a distinct MQTT client (separate from the mobile robots usual communication client).<br>Upon success, the mobile robot shall publish the connection state ONLINE.| yes | - | - | yes | no | no
shutdown | - | Initiates a coordinated shutdown of the mobile robot, where it disconnects from the MQTT broker. The execution of the shutdown action requires the mobile robot to be in an idle state. There is no way using the VDA 5050 protocol to automatically restart due to the connection being terminated.<br>If a mobile robot is in hibernate mode but should be shut down, it shall first exit hibernation (via stopHibernation) before executing shutdown.| yes | - | - | yes | no | no | no
startCharging | stopCharging | Activates the charging process. <br>Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). <br>Protection against overcharging is the responsibility of the mobile robot. | yes | - | powerSupply.charging | yes | yes | no | no
stopCharging | startCharging | Discontinues the charging process. <br>The charging process can also be interrupted by the mobile robot or the charging station, e.g., if the battery is full. | yes | - | powerSupply.charging | yes | yes | no | no
initializePosition | - | Resets (overrides) the pose of the mobile robot with the given parameters. | yes | x (float64)<br>y (float64)<br>theta (float64)<br>mapId (string)<br>lastNodeId (string) | mobileRobotPosition.x<br>mobileRobotPosition.y<br>mobileRobotPosition.theta<br>mobileRobotPosition.mapId<br>lastNodeId<br> maps | yes | yes<br>(Elevator) | no | no
enableMap | - | Enable a previously downloaded map explicitly to be used in orders without initializing a new position. | yes | mapId (string)<br>mapVersion (string) | maps | yes | yes | no | no
downloadMap | - | Trigger the download of a new map. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the map for use and setting the map in the state. | yes | mapId (string)<br>mapVersion (string)<br>mapDownloadLink (string)<br>mapHash (string, optional) | maps | yes | no | no | no
deleteMap | - | Trigger the removal of a map from the mobile robot's memory. | yes | mapId (string)<br>mapVersion (string) | maps | yes | no | no | no
downloadZoneSet | - | Trigger the download of a zone set. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the zone set for use and setting the zone set in the state. | yes | zoneSetId (string)<br>zoneSetDownloadLink (string)<br>zoneSetHash (string, optional) | zoneSets | yes | no | no | no
enableZoneSet | - | Enable a previously downloaded zone set explicitly to be used in orders. | yes | zoneSetId (string)<br> | zoneSets | yes | yes | no | no
deleteZoneSet | - | Trigger the removal of a zone set from the mobile robot's memory. | yes | zoneSetId (string) | zoneSets | yes | no | no | no
clearInstantActions | - | Removes all finished or failed instant actions from the mobile robot state. | yes | - | instantActionStates | yes | yes | no | no
clearZoneActions | - | Removes all finished or failed zone actions from the mobile robot's state. | yes | - | zoneActionStates | yes | yes | no | no
stateRequest | - | Requests the mobile robot to send a new state message. | yes | - | - | yes | no | no | no
logReport | - | Requests the mobile robot to generate and store a log report. | yes | reason<br>(string) | - | yes | no | no | no
pick | drop<br><br>(if automated) | Request the mobile robot to pick a load. <br>Mobile robots with multiple load handling devices can process multiple pick operations in parallel. <br>In this case, the parameter lhd needs to be present (e.g., LHD1). <br>The parameter stationType informs how the pick operation is handled in detail (e.g., floor location, rack location, passive conveyor, active conveyor, etc.). <br>The load type informs about the load unit and can be used to switch field for example (e.g., EPAL, INDU, etc). <br>For preparing the load handling device (e.g., pre-lift operations based on the height parameter), the action could be announced in the horizon in advance. <br>But, pre-Lift operations, etc., are not reported as 'RUNNING' in the mobile robot state, because the associated node is not released yet.<br>If on an edge, the mobile robot can use its sensing device to detect the position for picking the node. | no |lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional) <br>loadId (string, optional)<br>height (float64, optional)<br>defines bottom of the load related to the floor<br>depth (float64, optional) for forklifts<br>side (string, optional) e.g., conveyor | .load | no | yes | yes | no
drop | pick<br><br>(if automated) | Request the mobile robot to drop a load. <br>See action pick for more details. | no | lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional)<br>loadId (string, optional)<br>height (float64, optional)<br>depth (float64, optional) <br>… | .load | no | yes | yes | no
detectObject | - | Mobile robot detects object (e.g., load, charging spot, free parking position). | yes | objectType (string, optional) | - | no | yes | yes | yes
finePositioning | - | On a node, mobile robot will position exactly on a target.<br>The mobile robot is allowed to deviate from its node position.<br>On an edge, the mobile robot will e.g., align on stationary equipment while traversing an edge. | yes | stationType (string, optional)<br>stationName (string, optional) | - | no | yes | yes | yes
waitForTrigger | - | Mobile robot shall wait for a trigger of the type defined specified in the triggerType parameter, which is an array of strings. Two predefined values shall be used when semantically appropriate: 'FLEET_CONTROL' if the trigger originates from the fleet control, and 'LOCAL' if the trigger comes from an input on the mobile robot (e.g., button press, manual loading). If none of the predefined values meet the specific requirements, custom values can be defined. <br>Fleet control is responsible for handling the timeout and shall cancel the order if necessary. | yes | triggerType [string] (array) | - | no | yes | no | yes
trigger | - | Fleet control system notifies the mobile robot that a waitForTrigger action has been released. Typically, this occurs when the fleet control system receives information from a third-party system indicating that the process the mobile robot was waiting for has completed. | yes | - | - | yes | no | no | no
retry | - | Mobile robot retries action defined via actionId that is currently in state RETRIABLE. | yes | actionId (string) | - | yes | no | no | no
skipRetry | - | Mobile robot shall skip the action defined via actionId that is currently in state RETRIABLE, setting action to FAILED. | yes | actionId (string) | - | yes | no | no | no
cancelOrder | - | Mobile robot stops as soon as possible. This could be immediately or on the next node. See Chapter 6.1.3 Order cancellation. | yes | orderId (string, optional) | - | yes | no | no | no
factsheetRequest | - | Requests the mobile robot to send a factsheet | yes | - | - | yes | no | no | no
updateCertificate | - | Request the mobile robot to download and activate a new certificate set, the service parameter is an extensible enum with the predefined parameter 'MQTT' to be used for mqtt connection. | yes | service (string)<br>keyDownloadLink (string)<br>certificateDownloadLink (string)<br>certificateAuthorityDownloadLink (string, optional) | - | yes | no | no | no

>Table 4 - Predefined actions and their scope (instant, node, edge, zone)

#### 6.2.3.2 Action states

action type | 'INITIALIZING' | 'RUNNING' | 'PAUSED' | 'FINISHED' | 'FAILED' | 'RETRIABLE'
---|---|---|---|---|---|---
startPause | - | Activation of the mode is in preparation.<br>If the mobile robot supports an instant transition, this state can be omitted. | - | Mobile robot is not moving. <br>All pauseable actions are paused. <br> The pause mode has been activated. <br>The mobile robot reports paused: "true". | The pause mode cannot be activated for some reason (e.g., overridden by hardware switch).
stopPause | - | Deactivation of the mode is in preparation. <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pause mode has been deactivated. <br>All paused actions are resumed. <br>The mobile robot reports paused: "false". | The pause mode cannot be deactivated for some reason (e.g., overridden by hardware switch). | -
startHibernation | - | Activation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The active order has been cleared, if any. No state messages are sent by the mobile robot. <br>Hibernate mode has been activated. The mobile robot reports connection state "HIBERNATING".| The HIBERNATING connection state could not be published (e.g., overridden by a hardware switch).| -
stopHibernation | - | Deactivation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Hibernate mode has been deactivated.<br>The mobile robot reports connectionState "ONLINE".| The hibernate mode could not be deactivated (e.g., overridden by a hardware switch).| -
shutdown | - | Activation of the OFFLINE connection state is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The connection between mobile robot and broker is terminated in a coordinated way.<br>The mobile robot reports connection state "OFFLINE".| The shutdown cannot be executed for some reason (e.g., mobile robot is not in idle state, overridden by a hardware switch).| -
startCharging | - | Activation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been started. <br>The mobile robot reports powerSupply.charging: "true". | The charging process could not be started for some reason (e.g., not aligned to charger). Charging problems should correspond with an error. | The charging process could not be initiated. The mobile robot is waiting for intervention from fleet control or an operator.
stopCharging | - | Deactivation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been stopped. <br>The mobile robot reports powerSupply.charging: "false" | The charging process could not be stopped for some reason (e.g., not aligned to charger).<br> Charging problems should correspond with an error. | -
initializePosition | - | Initializing of the new pose in progress (confidence checks, etc.). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pose has been reset. <br>The mobile robot reports <br>mobileRobotPosition.x = x, <br>mobileRobotPosition.y = y, <br>mobileRobotPosition.theta = theta <br>mobileRobotPosition.mapId = mapId <br>mobileRobotPosition.lastNodeId = lastNodeId | The pose is not valid or cannot be reset. <br>General localization problems should correspond with an error. | -
downloadMap | Initialize the connection to the map server. | Mobile robot is downloading the map. | - | The download has finished. Mobile robot updates its state by setting the mapId/mapVersion and the corresponding mapStatus to 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, Map server unreachable, mapId/mapVersion not existing on map server). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableMap | - | The mobile robot enables the map with the requested mapId and mapVersion and disables any other map with the same mapId. | - | The map has been enabled. The mobile robot updates the corresponding mapStatus of the requested map to 'ENABLED' and the other versions with same mapId to 'DISABLED'. | The requested combination of mapId/mapVersion does not exist.| -
deleteMap | - | Mobile robot deletes map with requested mapId and mapVersion from its internal memory. | - | The map has been deleted. The mobile robot removes mapId/mapVersion from its state. | The map could not be deleted, e.g., because map is currently in use or requested combination of mapId/mapVersion has already been deleted before. | -
downloadZoneSet | Initialize the connection to the zone set server. | Mobile robot is downloading the zone set. | - | The download has finished. The mobile robot updates its state by setting a corresponding zoneSet object in its state with zoneSetStatus 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, server unreachable, zone set not existing, zone set with same zoneSetId already on mobile robot). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableZoneSet | - | Mobile robot enables the zone set with the requested zoneSetId and disables any other zone set for the same mapId. | - | The zone set has been enabled. The mobile robot updates the corresponding zoneSetStatus of the requested zoneSet to 'ENABLED' and the other zone sets for the same mapId to 'DISABLED'. | The requested zone set does not exist.| -
deleteZoneSet | - | Mobile robot deletes the zone set with requested zoneSetId from its internal memory. | - | The zone set has been deleted. The mobile robot removes zoneSet object from its state. | The zone set could not be deleted, deleted, e.g., because zone set is currently in use or the requested zone set has already been deleted before. | -
clearInstantActions | - | | - | The instant actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
clearZoneActions | - | | - | The zone actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
stateRequest | - | - | - | The state has been communicated | - | -
logReport | - | The report is being generated. <br>If the mobile robot supports an instant generation, this state can be omitted. | - | The report has been stored. <br>The name of the log is reported as part of the action state. | The report can not be stored (e.g., no space).| -
pick | Initializing of the pick process, e.g., outstanding lift operations. | The pick process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The pick process is being paused, e.g., if a safety field is violated. <br>After removing the violation, the pick process continues. | Pick has been done. <br>Load has entered the mobile robot and mobile robot reports new load state. | Pick failed, e.g., station is unexpected empty. <br> Failed pick operations should correspond with an error. | Pick failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
drop | Initializing of the drop process, e.g., outstanding lift operations. | The drop process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The drop process is being paused, e.g., if a safety field is violated. <br>After removing the violation the drop process continues. | Drop has been done. <br>Load has left the mobile robot and mobile robot reports new load state. | Drop failed, e.g., station is unexpected occupied. <br>Failed drop operations should correspond with an error. | Drop failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
detectObject | - | Object detection is running. | - | Object has been detected. | Could not detect the object. | Object detection failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
finePositioning | - | Mobile robot positions itself exactly on a target. | The fine positioning process is being paused, e.g., if a safety field is violated. <br> The fine positioning continues after e.g. the violation had been resolved. | Goal position in reference to the station has been reached. | Goal position in reference to the station could not be reached. | Fine positioning failed but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
waitForTrigger | - | Mobile robot is waiting for the trigger | - | Trigger has been triggered. | waitForTrigger fails, if order has been canceled. | -
cancelOrder | - | Mobile robot is stopping or driving, until it reaches the next node. | - | Mobile robot is not moving. Mobile robot has canceled executing the order and is in idle state. | <br>Mobile robot has no active order<br>The previous order has already been canceled.<br>Passed orderId does not match the currently active orderId. | -
factsheetRequest | - | - | - | The factsheet has been communicated | - | -
updateCertificate | - | Mobile robot is downloading and installing certificates | - | Certificates have been downloaded, installed and are active. | Download or installation failed. | -

>Table 5 - Expected behavior in action states of predefined actions

#### 6.2.3.3 Update mobile robot certificate

For security reasons, mobile robot communication (at least for fleet management) should be secured. Typically, communication to the MQTT broker is secured via TLS, which requires one or more root certificates and a mobile robot-specific key pair. The parameter `service` specifies the service (e.g., 'MQTT') for which the certificates are to be used. The parameter `certificateAuthorityDownloadLink` specifies the URL for the root certificate(s). The parameters `certificateDownloadLink` and `keyDownloadLink` specify the URLs for the mobile robot-specific public and private keys.

The download shall be secured via TLS as well, since the sender of the instantAction cannot be verified. It is also advisable to validate the certificate chain before it is activated.

## 6.3 Maps

To ensure consistent navigation among different types of mobile robots, the position is always specified in reference to the project-specific coordinate system (see Figure 12). The project-specific coordinate system is referring to the coordinate system that is defined for the interaction between fleet control and the mobile robot.
For the differentiation between different levels of a site or location, a unique `mapId` is used.
The map coordinate system is to be specified as a right-handed coordinate system with the z-axis pointing skywards.
A positive rotation therefore is to be understood as a counterclockwise rotation.
The mobile robot coordinate system is also specified as a right-handed coordinate system (ISO 9787 4.1) with the x-axis pointing in the forward direction of the mobile robot and the z-axis pointing upward (ISO 9787 5.5). The mobile robot reference point is defined as (0,0,0) in the mobile robot reference frame, unless specified otherwise.

![Figure 12 Coordinate system with sample mobile robot and orientation](./assets/coordinate_system_vehicle_orientation.png)
>Figure 12 - Coordinate system with sample mobile robot and orientation

The X, Y, and Z coordinates shall be given in meters.
The orientation shall be in radians and shall be within -Pi and +Pi.

### 6.3.1 Map distribution

To enable an automatic map distribution and intelligent management of restarting the mobile robots if necessary, fleet control can manage the maps on the mobile robot.

The map files to be distributed are stored on a dedicated map server that is accessible by the mobile robots. To ensure efficient transmission, each transmission should consist of a single file. If multiple maps or files are required, they should be bundled or packed into a single file. The process of transferring a map from the map server to a mobile robot is a pull operation, initiated by the fleet control triggering a download command using an `instantAction`.

Each map is uniquely identified by a combination of a map identifier (field `mapId`) and a map version (field `mapVersion`). The map identifier describes a specific area of the mobile robot's physical workspace, and the map version indicates updates to previous versions. Before accepting a new order, the mobile robot shall check that there is a map on the mobile robot for each map identifier in the requested order. If a corresponding `mapId` is missing in the list of available maps, the mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'. It is the responsibility of the fleet control to ensure that the correct maps are enabled to operate the mobile robot.

In order to minimize downtime and make it easier for the fleet control to synchronize the process of enabling of new maps, maps shall be pre-loaded or buffered on the mobile robots. The status of the maps on the mobile robot is reflected in the mobile robot's state. Transferring a map to a mobile robot and enabling the map are different processes. To enable a pre-loaded map on a mobile robot, the fleet control shall send an instant action. As a result, any other map with the same map identifier but a different map version shall be disabled by the mobile robot.

Deletion of maps can also be done by the fleet control via an instant action.

The map distribution process is shown in Figure 13.

![Figure 13 Map distribution process](./assets/map_distribution_process.png)
>Figure 13 - Communication required between fleet control, mobile robot and map server to download, enable, and delete a map.

### 6.3.2 Maps in the mobile robot state

The `mapId` field in the `mobileRobotPosition` of the state represents the currently active map.

Information about the maps available on a mobile robot is presented in the `maps` array, which is a component of the state message. Each entry in this array is a JSON object consisting of the mandatory fields `mapId`, `mapVersion`, and `mapStatus`, which can be either 'ENABLED' or 'DISABLED'. An 'ENABLED' map can be used by the mobile robot if necessary. A 'DISABLED' map shall not be used. The status of the download process is indicated by the current action not being completed. Errors are also reported in the state.
Note that multiple maps with different `mapId` can be enabled at the same time. There shall only be one version of maps with the same `mapId` enabled at a time. If the `maps` array is empty, no maps are currently available on the mobile robot.

### 6.3.3 Map download

The map download shall be triggered by the `downloadMap` instant action from the fleet control. It shall contain the mandatory parameters `mapId` and `mapDownloadLink` under which the map is stored on the map server and which can be accessed by the mobile robot.

The mobile robot sets the `actionStatus` to 'RUNNING' as soon as it starts downloading the map file. If the download is successful, the `actionStatus` is updated to 'FINISHED'. If the download is unsuccessful, the status is set to 'FAILED'. Once the download has been successfully completed, the map shall be added to the array of `maps` in the state. Maps shall not be reported in the state until they are ready to be enabled.

The process of downloading a map shall not modify, delete, enable, or disable any existing maps on the mobile robot.
The mobile robot shall reject the download of a map with a `mapId` and `mapVersion` that is already on the mobile robot. An error of type 'DUPLICATE_MAP' and level 'WARNING' shall be reported, and the status of the instant action shall be set to 'FAILED'. The fleet control shall first delete the map on the mobile robot and then restart the download.

### 6.3.4 Enable downloaded maps

There are two ways to enable a map on a mobile robot:

1. **Fleet control enables map**: Use the `enableMap` instant action to set a map to 'ENABLED' on the mobile robot. Other Versions of the same `mapId` with different `mapVersion` are set to 'DISABLED'.
2. **Manually enable a map on the mobile robot**: In some cases, it might be necessary to enable the maps on the mobile robot directly. The result shall be reported in the mobile robot state.

Fleet control shall ensure that the correct maps are activated on the mobile robot when sending the corresponding `mapId` as part of a `nodePosition` in an order.
If the mobile robot is to be set to a specific position on a new map, the `initializePosition` instant action shall be used.

### 6.3.5 Delete maps on the mobile robot

The fleet control can request the deletion of a specific map from a mobile robot. This shall be done by using the instant action `deleteMap`. When a mobile robot runs out of memory, it should report this to the fleet control, which can then initiate the deletion of maps. The mobile robot itself shall not delete maps.
After successfully deleting a map, the mobile robot shall remove the corresponding entry from its `maps` array in the state message.

## 6.4 Zones

Zones are used to define rules for specific areas of the mobile robot workspace. In this way, zones allow mobile robots to navigate freely between nodes while giving the fleet control the ability to manage traffic. Zones can be used to locally deny mobile robots access to areas or to link access to conditions (zone types: 'BLOCKED' and 'RELEASE'). It is also possible to enforce specific behavior while within the zone (zone types: 'LINE_GUIDED', 'SPEED_LIMIT', 'COORDINATED_REPLANNING', and 'ACTION') or influence the driving behavior by incentivizing or penalizing certain areas (zone types: 'PRIORITY' and 'PENALTY') or giving a predefined driving direction (zone types: 'DIRECTED', 'BIDIRECTED'). The zone types are defined in the following sections.

Potential conflicts in orders due to overlapping of zones or combination of zone and edge properties and how to resolve them are addressed in section [6.4.4 Interaction between zones](#644-interactions-between-zones). For released nodes that are part of the order but are restricted due to zones (e.g., node located within a 'BLOCKED' or 'RELEASE' zone), the robot is expected to act according to the zones (e.g., not enter or wait for 'GRANTED' state of the request).
Some mobile robots cannot process zones at all, while other mobile robots might only be able to work with a certain subset of zone types, such as 'BLOCKED'. All mobile robots shall therefore report to fleet control which zones they are able to understand by adding the according zone names to the `supportedZones` array under `typeSpecifications` in their factsheet.
Also (virtually) line-guided mobile robots can choose to support zone-based navigation if they can implement the logic of the corresponding zone types defined in the following.
A zone set shall only be changed and distributed by fleet control to keep consistency in the system.

### 6.4.1 Zone types

Two categories of zones are distinguished: contour-based zones and kinematic center-based zones. This distinction is based on the different conditions for when the mobile robot is considered to be entering and exiting zones.

#### 6.4.1.1 Contour-based zones

For contour-based zones, the contour of the mobile robot (including its load) determines zone entry and exit. Any part of the contour entering the zone is a zone entry. As soon as no part of the mobile robot's contour remains within the zone, it is a zone exit.

![Figure 14 Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)](./assets/contour_entry.png)
>Figure 14 - Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)

The following contour-based zones are defined:

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| BLOCKED | none | | Mobile robots shall not enter this zone. If a mobile robot has entered the zone or finds itself within one, it shall stop and throw an 'BLOCKED_ZONE_VIOLATION' error with level set to 'CRITICAL'.|
| LINE_GUIDED | none | | No free navigation is allowed in this zone, mobile robots shall follow the predefined trajectories on edges. Mobile robots may only enter this zone if the route is explicitly specified by the fleet control in the form of a node-edge graph. Any movement of the mobile robot that requires it to enter this zone shall follow a predefined trajectory. When entering the zone, the mobile robot shall be on the trajectory of the edge that crosses the zone. The edges that enter and are inside the line-guided zone require a trajectory sent from the fleet control or a predefined trajectory on the mobile robot. A corridor can be sent to allow the mobile robot to deviate from the trajectory. |
| RELEASE | | - | Mobile robots are only allowed entering this zone once they have been granted access through fleet control. |
| | releaseLossBehavior | string | Enum {'STOP', 'CONTINUE', 'EVACUATE'}<br>When the access to this zone is revoked or expired, the mobile robot can either 'STOP', 'CONTINUE', or 'EVACUATE' the zone. This action is only executed, when the mobile robot is already in the zone and the release expires or is revoked. If not defined, the mobile robot is expected to STOP and report an error.<br>'STOP': Mobile robot stops and sends a 'RELEASE_LOST' error with level 'CRITICAL'.<br>'EVACUATE': Execute the evacuation behavior of the mobile robot to leave the zone, keeping the `zoneRequest` object granting release in its state until the zone is left.<br>'CONTINUE': If the release is revoked or expires after the mobile robot has already entered the zone, the mobile robot continues its path, keeping the `zoneRequest` object granting the zone release in its state. If the order ends inside the zone, the mobile robot waits for a new order.|
| COORDINATED_REPLANNING | none | | No autonomous replanning is allowed within this zone. Mobile robots are only allowed adjusting their path if granted permission by fleet control. |
| SPEED_LIMIT | | | Mobile robots shall not drive faster than the defined maximum speed within this zone. |
| | maximumSpeed | float64 | Maximum permitted speed for mobile robot within the zone in m/s. The speed limit shall already be reached upon entering the zone.|
| ACTION | | | The mobile robot shall perform predefined actions when entering, traversing, or exiting the zone. The factsheet defines which actions can be executed when. |
| | entryActions[action] | array | Actions to be triggered when entering the zone. Empty array, if no actions required. |
| | duringActions[action] | array | Actions to be executed while crossing the zone. Empty array, if no actions required. |
| | exitActions[action] | array | Actions to be triggered when leaving the zone. Empty array, if no actions required. |

>Table 6 - Contour-based zone types and their parameters

#### 6.4.1.2 Kinematic center-based zones

In kinematic center-based zones, the mobile robot's kinematic center determines its entry and exit of the zones. When the mobile robot's kinematic center is inside a zone, the mobile robot shall follow the defined behavior.
'PRIORITY' and 'PENALTY' zones are zones which only influence the path planning of mobile robots.
'DIRECTED' zones define a preferred direction of travel within the zone. 'BIDIRECTED' zones define a travel direction and its opposite direction to be used. Other directions shall be avoided. The `directedLimitation` and `bidirectedLimitation` enums specify the limits within which the mobile robot may deviate from its direction of travel. The direction of travel is the velocity vector in the project-specific coordinate system.

![Figure 15 Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)](./assets/kinematic_center_entry.png)
>Figure 15 - Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| PRIORITY | | | The workspace encompassed by this zone is associated with an incentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | priorityFactor | float64 | [0.0...1.0]<br>Relative factor that determines the preference of the zone over a workspace without a zone. 0.0 means no preference, as if there was no zone, 1.0 is maximum preference.|
| PENALTY | | | The workspace encompassed by this zone is associated with a disincentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | penaltyFactor | float64 | [0.0...1.0]<br> Relative factor that determines the penalty of the zone compared to a workspace without that zone. 0.0 means no penalty, as if there was no zone, 1.0 is the maximum penalty, causing the mobile robot to take this path only if it cannot find any other feasible route. |
| DIRECTED | | | Mobile robots shall traverse this zone in a specific direction of travel. |
| | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system. |
| | directedLimitation | string | Enum {'SOFT','RESTRICTED','STRICT'}<br>SOFT: Mobile robots may deviate from the defined direction of travel, but should avoid it, RESTRICTED: The mobile robot may deviate from the defined direction of travel, e.g., to avoid an obstacle, but shall never traverse opposite to the defined direction of travel, STRICT: The mobile robot shall maintain the defined direction of travel as precisely as its technical capabilities allow. |
| BIDIRECTED | | | While in this zone, mobile robots shall only move in the defined direction of travel and its direct opposite (+ Pi), mobile robots should not cross this zone in any other direction. |
 | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system.|
| | bidirectedLimitation | string | Enum {'SOFT', 'RESTRICTED'}<\br>SOFT: Mobile robots may deviate from the defined directions of travel, but should avoid it, RESTRICTED: The mobile robot shall not traverse in any other direction than the directions of travel, except for obstacle avoidance. |

>Table 7 - Kinematic center-based zone types and their parameters

### 6.4.2 Zone set transfer

Zone sets shall only be changed and distributed by fleet control to keep consistency in the system. The preferred way to distribute zone sets is via the `zoneSet` topic. If the mobile robot supports zones, the update via the `zoneSet` topic shall be supported. Larger zone sets can also be shared through the `downloadZoneSet` instant action, following the map distribution concept in figure 13.

A `zoneSet` is an array of `zone` objects with a globally unique identifier, `zoneSetId`. It is associated with a single map referenced through the `mapId`. The `mapVersion` shall not be referenced, as the same zone set might be intended to be used for several versions of one map. In general, several zone sets can be defined in addition to a single map and it is upon fleet control to ensure that the right zone set is enabled for each map on the mobile robot. As with maps, the `zoneSetStatus` indicates which zone set is currently used by the mobile robot. Only a single zone set can be active at once for each `mapId` on the mobile robot. Zones shall not extend beyond the spatial boundaries of a map.
The content of a zone set with a unique `zoneSetId` shall not change. If changes are required within a zone set, it shall be referenced with a new `zoneSetId`.

The `zoneSetStatus` of a newly added zone set shall always be set to 'DISABLED' and shall be enabled through the `enableZoneSet` instant action before use.

If the mobile robot receives a new zone set via the `zoneSet` topic or `downloadZoneSet` instant action with the same `zoneSetId` as an existing one, it shall not take over the zone set in its internal memory and report an error of type 'DUPLICATE_ZONE_SET' and level 'WARNING' for a reasonable amount of time for the fleet control to notice that the zone update failed.

## 6.4.3 Communication for interactive zones

For communicating requests for the interactive zones 'RELEASE' and 'COORDINATED_REPLANNING', the field `zoneRequests` in the state message is used. The separate topic `responses` is used by fleet control to respond to these requests.

Before entering an interactive zone, the mobile robot shall state a request.
A request before entry of an interactive zone is necessary, even if the order contains released nodes within the zone.
The mobile robot decides at which point before entering the zone to make its requests.
If the response is not received in time, the mobile robot shall not enter the zone.

Requests shall only be made for zones of enabled zone sets. Zone requests can also be made for zone sets belonging to maps that the mobile robot is not currently on.

The `requestId` allows fleet control to distinguish between different requests and allows the mobile robot to issue several alternative requests for the same zone at the same time.
Each request attempt shall use a unique identifier per mobile robot. Ids can be reused after a mobile robot restart.

For requests to enter a 'RELEASE' zone, a `zoneRequest` object of `requestType` 'ACCESS' shall be added to the state message.
For permission to enter a 'COORINATED_REPLANNING' zone with a planned path or for replanning its path within the zone, the `requestType` shall be set to 'REPLANNING'.
For a 'REPLANNING' request, the planned path shall be added as NURBS to the `trajectory` field of the `zoneRequest`. Multiple requests with different trajectories for the same zone can be made. Each path shall be requested with its own `zoneRequest` object.
If a mobile robot requires access to a workspace covered by two or more 'RELEASE' zones, it shall request access and receive approval for all necessary zones before entering the area.
If a mobile robot navigates through a workspace on the map that is covered by two or more 'COORDINATED REPLANNING' zones, it shall request its path within this area individually for each zone and receive approval from the fleet control before entering or changing paths.

The parameter `requestStatus` shall be initially set to 'REQUESTED' by the mobile robot when stating its request.

Fleet control responds to zone requests via the `responses` topic.
The response message contains an array of `response` objects. Each `response` shall only respond to a single request referenced by the `requestId`.
Each response has a `responseType` that is either 'GRANTED', 'QUEUED', 'REVOKED', or 'REJECTED'.
If the `responseType` is 'GRANTED', the mobile robot is allowed to enter the zone or use the requested trajectory.
Fleet control can set the `responseType` to 'QUEUED' to acknowledge the mobile robot's request without giving permission, informing the mobile robot that its request is being processed.
If the `responseType` is 'REJECTED', the mobile robot shall not enter the zone or use the requested trajectory.
The `responseType` 'REVOKED' indicates that the permission is no longer valid. The fleet control shall assume a 'REVOKED' request as still being 'GRANTED', until the `requestStatus` of the mobile robot is set to 'REVOKED'.
The `response` object can include a `leaseExpiry` which specifies until when a 'GRANTED' request is valid. To extend the `leaseExpiry` fleet control can resend a response message with an updated `leaseExpiry` time.

The mobile robot shall acknowledge the fleet controls response by setting the `requestStatus` accordingly and keep the request for as long as it considers the information relevant. See also Section [6.9 Request/response mechanism](#69-requestresponse-mechanism).

The interaction between the mobile robot and the fleet control for 'RELEASE' zones shall be according to Figure 16.

While the mobile robot remains in the 'RELEASE' zone, it keeps the `zoneRequest` object in its state and continues to report `requestStatus` as 'GRANTED' to inform fleet control that it is still inside the zone. After mobile robot has exited the zone, it shall remove the corresponding `zoneRequest` entry from its state message.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state. When the `leaseExpiry` has passed, the requestStatus shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall report a warning and react according to the `releaseLossBehavior` defined in the zone definition.

![Figure 16 Zone request behavior for a RELEASE zone.](./assets/request_release_zone_access.png)
>Figure 16 - Zone request behavior for a RELEASE zone.

The interaction between the mobile robot and the fleet control for 'COORDINATED_REPLANNING' zones shall be according to Figure 17.

The mobile robot shall choose one of the trajectories of all 'GRANTED' requests to the zone and set the corresponding `requestStatus`to 'GRANTED' while removing all other requests from its state.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state and not enter the 'COORDINATED_REPLANNING' zone. When the `leaseExpiry` has passed, the `requestStatus` shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall stop driving and report a warning. To continue, the mobile robot shall state a new request.

![Figure 17 Zone request behavior for a COORDINATED_REPLANNING zone.](./assets/request_coordinated_replanning_zone_replanning.png)
>Figure 17 - Zone request behavior for a COORDINATED_REPLANNING zone.

### 6.4.4 Interactions between zones

In the following matrix possible interactions between zones are described. The matrix is symmetric, as the interaction between two zones is the same, regardless of the order in which they are considered. For each combination, there is either a zone behavior that is overrulling the other (e.g., a 'BLOCKED' zone overrules a 'LINE_GUIDED' zone) or there is no conflict (e.g., a 'LINE_GUIDED' zone and a 'COORDINATED_REPLANNING' zone). 'DIRECTED' and 'BIDIRECTED' zones shall not overlap, since this might lead to an undefined behavior. The column No Zone defines the behavior for contour-based zones, where mobile robots can be inside a defined zone type and an area without a zone at the same time. For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so there is no possible interaction.

| |**BLOCKED**|**RELEASE**|**LINE_GUIDED**|**COORDINATED_REPLANNING**|**SPEED_LIMIT**|**ACTION**|**PRIORITY**|**PENALTY**|**DIRECTED**|**BIDIRECTED**|**No Zone**|**EDGE-PROPERTIES**
---|---|---|---|---|---|---|---|---|---|---|---|---
**BLOCKED**|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|
**RELEASE**||No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict
**LINE_GUIDED**|||No conflict|LINE_GUIDED|No Conflict| (1) |LINE_GUIDED|LINE_GUIDED|LINE_GUIDED|No conflict|LINE_GUIDED|No conflict
**COORDINATED_REPLANNING**||||(2)|No conflict|(1)|No conflict|No conflict|No conflict|No conflict|COORDINATED_REPLANNING|(3)
**SPEED_LIMIT** |||||(4)|No conflict|No conflict|No conflict|No conflict|No conflict|SPEED_LIMIT|(4)
**ACTION** ||||||(5)|No conflict|No conflict|No conflict|No conflict|ACTION|(5)
**PRIORITY** |||||||(6)|(6)|No conflict|No conflict|(7)|No conflict
**PENALTY** ||||||||(6)|No conflict|No conflict|(7)|No conflict
**DIRECTED** |||||||||(8)|(8)|(7)|(9)
**BIDIRECTED** ||||||||||(8)|(7)|(9)

>Table 8 - Interaction matrix for zones

1) If actions would conflict with other zones' behavior, report a 'ZONE_ACTION_CONFLICT' error with level 'CRITICAL' (order error) and stop the mobile robot.
2) Planned trajectory required to be granted for all 'COORDINATED_REPLANNING' zones.
3) If a trajectory is predefined for the edge, it shall be sent in the zone request.
4) The lowest of the competing `maximumSpeed` values applies.
5) Execute all actions.
6) The most restrictive one is always selected here; for PRIORITY zones, the lowest `priorityFactor` is used; for overlapping PRIORITY and PENALTY zones, the highest `penaltyFactor` is used; for overlapping PENALTY zones, the highest `penaltyFactor` is used.
7) For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so this overlap is not possible.
8) Zones shall not overlap, since the behavior is not defined.
9) A `trajectory` as part of the edge properties shall override the directed and bidirected zones.

### 6.4.5 Error handling within zones

If at any point of the order execution, a mobile robot realizes, that it can not reach a node in its order, it shall report a 'NODE_UNREACHABLE' error with level 'CRITICAL' to the fleet control. The fleet control shall then decide how to proceed. The mobile robot shall not try to reach the node again, but wait for further instructions from the fleet control.

## 6.5 Connection

During the connection of a mobile robot client to the broker, a last will topic and message shall be set, which is published by the broker upon disconnection of the mobile robot client from the broker.
Thus, the fleet control can detect a disconnection event by subscribing the connection topics of all mobile robots.
The disconnection is detected via a heartbeat that is exchanged between the broker and the client.
Thus, the fleet control can detect a disconnection event by subscribing to the `connection` topic of each mobile robot.

As a result, the timestamp and headerId fields will always be outdated.

Mobile robot wants to disconnect gracefully:

1. Mobile robot sends "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to `OFFLINE`.
2. Disconnect the MQTT connection with a disconnect command.

Mobile robot comes online:

1. Set the last will to "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN', when the MQTT connection is created.
2. Send the topic "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to 'ONLINE'.

All messages on this topic shall be sent with a `retained` flag.

When connection between the mobile robot and the broker stops unexpectedly, the broker will send the last will to the topic: "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN'.

## 6.6 State

The mobile robot state shall be published on a single topic.
Compared to separate messages (e.g., for current order progress, battery state and errors), using a single topic reduces the workload of both the broker and the fleet control system when handling messages, while also keeping the mobile robot state information synchronized.

The mobile robot state message shall be published when relevant events occur or at least every 30 seconds.

The following events shall trigger a transmission of the state message:

- Receiving an order
- Receiving an order update
- Changes in the `load` object
- Change in the `errors` array
- Change in the `operatingMode` field
- Change in the `driving` field
- Change in the `paused` field
- Change in the `safetyState` object
- Change in the `newBaseRequest` field
- Change in the `lastNodeId` or `lastNodeSequenceId` field
- Change in the `edgeRequests` or `zoneRequests` arrays
- Change in the `powerSupply.charging` field
- Change in the `nodeStates` or `edgeStates` arrays
- Change in the `actionStates`, `instantActionStates` or `zoneActionStates` arrays
- Change in the `zoneSets` array
- Change in the `maps` array

*Remark: For above mentioned arrays, changes in the individual items of the array as well as adding or removing entries shall trigger a state message transmission.*

There should be an effort to curb the amount of communication.
If two events correlate with each other (e.g., the receiving of a new order usually forces an update of the `nodeStates` and `edgeStates`; as does the driving over a node), it is sensible to trigger one state update instead of multiple. The minimum time between two consecutive state messages is defined by the factsheet ([7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) `protocolLimits.timing.minimumStateInterval`) .

### 6.6.1 Concept and logic

The order progress is tracked by the `nodeStates` and `edgeStates`.
Additionally, if the mobile robot is capable of determining its current position, it shall publish it via the `mobileRobotPosition` field.

The `nodeStates` and `edgeStates` include all upcoming nodes and edges for the mobile robot to traverse.

![Figure 18 Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted](./assets/order_information_state_topic.png)
>Figure 18 - Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted

### 6.6.2 Traversal of nodes and edges

The mobile robot decides on its own when a node should count as traversed.
A requirement for the traversal is that the mobile robot's control point shall be within the node's `allowedDeviationXY` and its orientation within `allowedDeviationTheta`.
The `allowedDeviationXY` defines at what point a line-guided mobile robot can deviate from its predefined trajectory, to cut the corner along a smoother path rather than reaching the node's exact position. When leaving the `allowedDeviationXY` the mobile robot shall be back on its predefined trajectory of the subsequent edge.
If the edge attribute `corridor` of the subsequent edge is set, these boundaries should be met additionally.

In case the mobile robot is located too far away from the first node of an order, the fleet control can add an extended `allowedDeviationXY` to this node to include the mobile robot's current position.

The mobile robot shall report the traversal of a node by removing its `nodeState` from the `nodeStates` array and setting the `lastNodeId` and `lastNodeSequenceId` to the traversed node's values.

As soon as the mobile robot reports the node as traversed, the mobile robot shall trigger the actions associated with the node, if any.
The traversal of a node also necessarily implies leaving the edge that is leading up to the node.
The edge shall then also be removed from the `edgeStates` and the actions that were active on the edge shall be finished.

The traversal of the node also marks the moment when the mobile robot enters the following edge, if there is one.
The edge's actions shall be triggered, if any.
An exception to this rule is if the mobile robot shall stop on the node (because of a soft or hard blocking action) – then the mobile robot only enters the following edge once it begins driving again.

When an active order exists, the fields `lastNodeId` and `lastNodeSequenceId` shall be updated only when the mobile robot traverses a released node that is part of this order. For example if a physically line‑guided mobile robot detects a physical marker/tag that is not part of the active order’s `nodes`, this detection shall not lead to a change of `lastNodeId` or `lastNodeSequenceId`.

![Figure 19 Depiction of nodeStates, edgeStates, and actionStates during order handling](./assets/states_during_order_handling.png)
>Figure 19 - Depiction of `nodeStates`, `edgeStates`, and `actionStates` during order handling

#### 6.6.2.1 Definition of allowedDeviationXY as an ellipse

The allowedDeviationXY is defined as an ellipse around the node position to allow more flexible approaches to the node.

![Figure 20 allowedDeviationXY ellipse](./assets/ellipse.png)
>Figure 20 - allowedDeviation ellipse

### 6.6.3 Base request

If the mobile robot detects that its base is running short, it can set the `newBaseRequest` flag to "true" to attempt to prevent unnecessary braking.

### 6.6.4 Information

The mobile robot can submit arbitrary additional information to the fleet control via the `information` array.
It is up to the mobile robot to decide how long it reports information via an information message.

The fleet control shall not use the information for logic; they shall only be used for visualization and debugging purposes.

### 6.6.5 Errors

The mobile robot reports any issues via the `errors` array.

#### 6.6.5.1 Error levels

The issues can have four levels: 'WARNING', 'URGENT', 'CRITICAL', and 'FATAL'.

- A 'WARNING' level issue does not require immediate attention. The mobile robot can continue its current order and is able to take new orders. The error might be self-resolving, e.g., a dirty LiDar-scanner.
- An 'URGENT' level issue, e.g., a low battery level, requires immediate attention. The mobile robot can continue its current order and is able to take new orders.
- A 'CRITICAL' level issue requires immediate attention, e.g., trying to pick an object, that is not there. The mobile robot shall not continue driving since it can not continue its current order but is able to take new orders.
- A 'FATAL' level issue requires user intervention, e.g., losing localization. The mobile robot shall not continue driving since it can neither continue its currently active order nor take any new orders.

The mobile robot can add references that help with finding the cause of the error via the `errorReferences` array.
The fields `errorDescription` and `errorHint` may provide human-readable text explaining the error or suggesting a possible resolution.

Regardless of the level of the issue, the mobile robot shall never clear its order due to it.

#### 6.6.5.2 Error references

If an error occurs due to an erroneous order or execution failure, the mobile robot can return meaningful error references in the field `errorReferences` to support finding the cause of the error.
This can include the following information:

- `headerId`
- Topic (`order` or `instantAction`)
- `orderId` and `orderUpdateId` if error was caused by an order update
- `actionId` if error was caused by an action
- List of parameters if error was caused by erroneous action parameters

#### 6.6.5.3 Error translations

For both `errorDescription` and `errorHint`, the mobile robot can provide translations by using the `errorDescriptionTranslations` and `errorHintTranslations` arrays.
Each translation consists of an ISO 639-1 language code and the corresponding translated text.

#### 6.6.5.4 Predefined error types

The mobile robot shall use predefined error types to report specific issues. The following table lists the predefined error types and their description.

Error Type | Error level | Description | Reference | Report duration
---|---|---|---|---
'UNSUPPORTED_PARAMETER' | 'CRITICAL' | Receival of message with an unsupported optional parameter. | Name of parameter | Until new order is accepted.
'NO_ORDER_TO_CANCEL' | 'WARNING'  | The mobile robot received a `cancelOrder` action, but it does not have an active order to cancel. | `actionId` of `cancelOrder` | Until new order is accepted.
'VALIDATION_FAILURE'|'WARNING'| Receival of malformed order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_ORDER_ACTION' | 'WARNING' | Receival of an order containing unsupported actions. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_INSTANT_ACTION' | 'WARNING' | Receival of an unsupported instant action. | `actionId` of `instantAction` | Until new instant action is accepted.
'OUTDATED_ORDER_UPDATE'| 'WARNING' | Receival of an order with correct `orderId` but outdated `orderUpdateId`. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'SAME_ORDER_UPDATE_ID' | 'WARNING' | Receival of a duplicate order message (same `orderId` and `orderUpdateId`) | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'ORDER_UPDATE_FOLLOWING_CANCEL' | 'WARNING' | Receival of an order update for an order that has already been cancelled. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'OUTSIDE_OF_CORRIDOR' | 'CRITICAL' | Leaving the corridor defined for an edge. | `edgeId` | Until the mobile robot is no longer violating the corridor boundaries.
'INSUFFICIENT_MEMORY' | 'URGENT' | Mobile robot does not have enough memory to process received order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'DUPLICATE_MAP' | 'WARNING' | Receival of a map with `mapId` and `mapVersion` already existing. | `mapId` and `mapVersion` of duplicate | Until a new map related instantAction was accepted.
'BLOCKED_ZONE_VIOLATION' | 'CRITICAL' | Entering a 'BLOCKED' zone. | `zoneId` | Until the mobile robot is no longer violating the blocked zone.
'DUPLICATE_ZONE_SET' | 'WARNING' | Receival of a zone set with `zoneSetId` already existing. | `zoneSetId` or `actionId` of `instantAction` | Reasonable amount of time for the fleet control to notice that the zone update failed.
'RELEASE_LOST' | 'CRITICAL' | Losing the release for a 'RELEASE' zone. | `zoneId` | Until the mobile robot is no longer within the 'RELEASE' zone or is granted a the release again.
'ZONE_ACTION_CONFLICT' | 'CRITICAL' | Conflict between zone behavior and zone actions. | `zoneId` of 'ACTION' zone | Until the mobile robot is no longer violating the zone behavior.
'NODE_UNREACHABLE'|'CRITICAL'| The mobile robot cannot reach a node in its order. | `nodeId` | Until new order is accepted.
'LOCALIZATION_ERROR'|'FATAL'| The mobile robot is not localized. | | Until localization is regained.
'NO_ROUTE_TO_TARGET' | 'WARNING' | Receival of an order with at least one unreachable node. | `orderId` | Until new order is accepted.
'OTHER_ORDER_ACTIVE' | 'WARNING' | Receival of a new order while another order is still active. | `orderId` | Until new order is accepted.
'START_NODE_OUT_OF_RANGE' | 'WARNING' | Receival of an order with unreachable first node. | `orderId` | Until new order is accepted.
'MOBILE_ROBOT_NOT_AVAILABLE' | 'WARNING' | Receival of an order while not in 'AUTOMATIC', 'SEMIAUTOMATIC' or 'INTERVENED' operating mode. | `orderId` | Until operating mode allows for new orders
'UNKNOWN_MAP_ID' | 'WARNING' | Receival of an order containing nodes referencing an unknown `mapId`. | `orderId` | Until new order is accepted.

> Table 9 - Predefined error types

### 6.6.6 Operating Mode
…(발췌: 전체 207,642자 중 앞 110,737자)
````
