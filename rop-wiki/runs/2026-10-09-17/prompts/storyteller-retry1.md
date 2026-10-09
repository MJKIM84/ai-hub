(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-17
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 41. 플랫폼 아키텍처·외부 API (K. 플랫폼 아키텍처·인프라)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-10-09-17/target.json

```json
{
  "run_id": "2026-10-09-17",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 150,
  "run_type": "update",
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
  "selection_rationale": "CLI 지정 run_type=update, area=41"
}
```

### runs/2026-10-09-17/research.json

```json
{
  "run_id": "2026-10-09-17",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 41,
    "area_name": "41. 플랫폼 아키텍처·외부 API",
    "category": "K. 플랫폼 아키텍처·인프라"
  },
  "gaps": [
    "섹션 6. 대표 접근법과 기술 — 연결이 끊겼을 때 로봇·관제가 어떻게 동작하는지, 메시지 전달 보장 수준(재전송·순서·중복)의 근거가 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 의 버전 표기 규칙과 MQTT QoS 수준, Open-RMF 플릿 어댑터 API 의 폐기 예고, rmf-web API 서버의 기계 간(M2M) 인증 설정·권한 그룹 미구현(바뀐 출처) 서술 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) — 외부 API 전달 보장과 고객·현장별 권한 격리를 누가 맡는지 근거가 약함",
    "섹션 11. 열린 질문 — oq-206·oq-207·oq-208·oq-300 의 부분 근거 미반영, oq-209·oq-267·oq-301 미조사",
    "섹션 5. 적용 사례 (현장 유형 명시) — 상업 시설·가정·실외 사례 없음(이번 재실행에서도 조사하지 못함)",
    "정정 요청 없음"
  ],
  "research_questions": [
    "어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]",
    "oq-207 로봇 관제 플랫폼·상호운용 규격은 API 버전 관리와 하위 호환, 폐기 예고를 어떻게 공개하는가? (섹션 7·11 겨냥)",
    "oq-208 로봇–관제 인터페이스와 플랫폼 외부 이벤트의 전달 보장(재시도·순서·중복 제거)은 어디까지 정해져 있는가? (섹션 6·9·11 겨냥)",
    "oq-206·oq-300 연결이 끊기거나 중앙 서비스가 재시작될 때 로봇과 진행 중 작업은 어디까지 계속되는가? (섹션 6·11 겨냥)",
    "바뀐 출처: Open-RMF rmf-web API 서버의 인증·권한 서술은 지난 확인(2026-09-30) 이후 무엇이 바뀌었고, 외부 API 의 인증·격리 범위에 무엇을 뜻하는가? (섹션 7·9 겨냥)",
    "oq-209·oq-301 국내 클라우드 로봇·통합관제 참조 구조 표준과 OpenAPI·AsyncAPI 기반 적합성 시험 도구가 있는가? (섹션 7·11 겨냥, 이번 재실행에서는 조사하지 못함)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 은 의미적 버전 관리를 써서 주 버전(x.0.0)은 새 필수 필드 도입 같은 하위 호환을 깨는 변경, 부 버전(3.x.0)은 선택 매개변수 추가 같은 새 기능, 수 버전(3.0.x)은 문서 오탈자 같은 작은 수정에 쓰고, MQTT 주제 경로에 'v' 를 붙인 주 버전(예 v3)을 넣게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1장: \"Major version changes (x.0.0) typically involve breaking changes\". 4.2절 주제 수준 표에서 majorVersion 은 'v' 를 붙인 주 버전 번호이고 예시는 vda5050/v3/KIT/0001/order 다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 무선망의 연결 끊김과 메시지 손실을 전제로 order·instantActions·state·factsheet·zoneSet·responses·visualization 주제에 MQTT QoS 0(최선 노력)을, connection 주제에 QoS 1(최소 한 번)을 쓰게 하고, 로봇이 예기치 않게 끊기면 브로커가 유언(last will) 메시지로 다른 구독자에게 알리게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4장·4.1절: 통신은 무선망에서 연결 끊김과 메시지 손실을 고려해 이뤄지며, 통신 부하를 줄이려고 connection 외 주제는 QoS 0, connection 은 QoS 1 을 쓴다. 유언 메시지 사용은 6.5절에 기술. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 주문 정보를 유지하고 마지막으로 해제(released)된 노드까지 주문을 수행하며, 관제는 MQTT 가 비동기이고 무선 전송을 믿을 수 없으므로 이미 해제한 base 구간을 바꿀 수 없고 실행된 것으로 간주해야 하며 주문 취소(cancelOrder)도 같은 이유로 신뢰할 수 없는 것으로 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.1절: 연결이 끊긴 로봇은 주문 정보를 유지하고 마지막 해제 노드까지 수행한다. 6.1.2절: base 는 바꿀 수 없어 관제는 이미 실행된 것으로 가정하며, 취소 절차도 통신 한계로 신뢰할 수 없다고 적는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 5050 3.0.0 의 주문 갱신은 같은 orderId 에 orderUpdateId 를 늘려 보내며, 로봇은 같은 orderUpdateId 로 같은 내용이 다시 오면 무시하고 내용이 다르면 SAME_ORDER_UPDATE_ID, 더 낮은 orderUpdateId 면 OUTDATED_ORDER_UPDATE 경고를 보고해 재전송과 순서 뒤바뀜을 메시지 수준에서 걸러낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.1.4.4·6.1.4.5절: 낮은 orderUpdateId 는 이전 주문을 유지하고 OUTDATED_ORDER_UPDATE(WARNING), 같은 orderUpdateId 는 내용이 같으면 무시·다르면 SAME_ORDER_UPDATE_ID(WARNING). 관제가 state 를 못 받아 재전송하는 경우를 예로 든다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 은 클라우드 사업자가 강제하는 주제 구조가 있으므로 MQTT 주제 단계 구조를 엄격히 정하지 않고 클라우드 브로커에서는 구조를 개별 조정하게 허용하되, 주제 이름(order·state 등)은 필수로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.2절: 클라우드 사업자의 필수 주제 구조 때문에 주제 구조를 엄격히 정하지 않으며, 클라우드 기반 브로커는 개별 조정이 필요할 수 있으나 제안 구조를 대략 따라야 하고 주제 이름은 필수다. 지역(local) 브로커용 단계 구조를 제안한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 은 주변 설비·기반 시설 구성 요소·외부 IT 시스템과의 인터페이스, 안전 요구사항, 교통 관리 로직, 운영자·통합사·제조사·관제 공급자 사이 운영 책임 배분, 사이버보안 조치를 범위 밖에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2장 Scope 의 제외 항목: Safety Requirements, Traffic Management Logic, Other Communication Interfaces(주변 설비·기반 시설·외부 IT 시스템), Operational Responsibilities, Cybersecurity Measures. 4.1절도 프로토콜 보안은 브로커 설정으로 다루고 지침에서는 다루지 않는다고 적는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 은 플릿 관제의 최소 기능으로 주문 배정, 경로 계산, 교착 탐지·해소, 에너지 관리, 교통 통제, 문·게이트·승강기 같은 주변 시스템과의 통신, 통신 오류 탐지·해소를 들고, 로봇의 기능으로 위치 추정·경로 실행·동작 실행·상태 연속 전송을 들어 판단 배치를 관제와 로봇으로 나눈다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5.3절 Functions of the fleet control 과 5.4절 Functions of the mobile robots 의 목록. 같은 명세가 주변 설비 인터페이스 자체는 범위 밖에 둔다(2장). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "로봇–관제 인터페이스인 VDA 5050 은 버전 표기와 주문 갱신 번호로 재전송·순서 문제를 다루지만 대부분 주제에 QoS 0 최선 노력 전달을 쓰고 외부 IT 시스템 인터페이스를 범위 밖에 두므로, 41. 플랫폼 아키텍처·외부 API 에서 업무 시스템에 내보내는 웹훅·이벤트의 전달 보장(재시도·순서·중복 제거)은 ROP 의 외부 API 가 따로 정해야 하는 것으로 보인다(oq-208 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2(QoS 0·1 구분), f4(orderUpdateId 로 중복·역순 판정), f6(외부 IT 시스템 인터페이스 제외)을 종합한 판단이다. 명세 자체는 외부 이벤트 전달 보장을 말하지 않는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Open-RMF 핵심 문서는 플릿 어댑터를 Full Control·Traffic Light·Read Only·No Interface 네 제어 수준으로 나누고, Full Control 에는 재사용 C++ API(파이썬 바인딩 포함)를 제공하며, Read Only 용 예비 ROS 2 메시지 API 는 향후 판에서 C++ API 로 대체되어 폐기될 예정이고 Traffic Light 용 재사용 API 는 아직 구현되지 않았다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Fleet Adapters 절: Read Only 용 예비 ROS 2 메시지 API 는 \"will be deprecated in favor of a C++ API\" 이며 시점은 'future release' 로만 적혀 있다. Traffic Light 는 통합사가 핵심 일정·협상 API 를 직접 써야 한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Open-RMF 의 교통 일정은 플랫폼 중립의 중앙 데이터베이스로, 배치된 모든 플릿 관리자가 예상 경로를 보고하고, 충돌이 예상되면 플릿 관리자들이 협상하며 시스템 통합사가 둔 제3자 판정자가 제안을 고르고, 긴급 작업은 의도적으로 충돌을 올려 협상을 강제할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Traffic deconfliction·Negotiation·Traffic Schedule 절: 일정 DB 는 미래 의도 경로를 담는 중앙 DB 이고, 판정자는 고우선 참여자를 항상 우선하도록 구현할 수 있다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Open-RMF rmf-web API 서버는 사용자 신원을 스스로 관리하지 않고 OpenID Connect 신원 제공자가 발급한 JWT 접근 토큰을 독립 검증하며, OAuth 2.0 client_credentials(기계 간, M2M) 흐름에서 신원 제공자가 표준 클레임을 빼고 네임스페이스 붙은 클레임만 주는 경우를 위해 선택 설정 preferred_username_claim_namespace 를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Authentication and Authorization 절: 토큰에 preferred_username 클레임이 있어야 하고, 없으면 설정한 네임스페이스 접두어를 붙인 클레임을 대신 확인한다. RFC 9068 §2.2.2·RFC 7519 §4.2 를 근거로 들고 Auth0 의 정책을 예로 든다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "rmf-web API 서버는 역할·동작·권한 그룹의 세 값으로 접근을 판정하지만, 자원의 권한 그룹을 정하는 방식이 아직 TODO 로 남아 있어 현재는 모든 자원이 기본 빈 그룹('')에 들어간다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Roles, Actions and Authorization Group 절과 TODO 절: 권한 그룹 결정 방식이 미정이거나 RMF 쪽 정보가 부족해 \"currently every resource is put into a default empty group\". (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "rmf-web API 서버는 자체 사용자·역할·권한 DB 를 신원 제공자와 동기화하지 않으므로, rmf-server 에서 사용자를 지워도 로그인만 요구하는 반보호 API 접근은 막지 못하고 로그인 자체를 막으려면 신원 제공자에서 사용자를 지워야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Synchronization (or lack of) of User Data 절: 처음 접근한 사용자는 권한 없는 사용자로 자동 생성되고, 관리자 엔드포인트는 rmf-server DB 에만 작용하며, 완전 삭제는 신원 제공자에서 해야 한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "rmf-web API 서버는 최신 API 정의를 공개 문서 사이트와 실행 중인 서버의 /docs 경로에서 보여 주고, 역방향 프록시 뒤에서 쓸 때는 public_url 을 공개 주소로 설정하고 프록시가 경로 접두어를 제거하게 해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "API 절과 Running behind a proxy 절: 예 https://example.com/rmf/api/v1 에서 서비스하면 public_url 을 그 주소로 두고 /rmf/api/v1/something 을 /something 으로 넘긴다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "rmf-web API 서버의 권한 그룹 결정이 미구현이고(f12) 사용자 해지가 신원 제공자에 달려 있으므로(f13), Open-RMF 웹 API 를 ROP 외부 API 의 기반으로 쓰면 고객·현장별 자원 격리와 외부 계정 해지는 ROP 가 신원 제공자 연동과 권한 그룹 규칙으로 직접 채워야 할 것으로 보이며, 이는 51. 인증·권한·격리와 맞닿는다.",
      "tag": "추정",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f12·f13 을 종합한 판단이다. README 는 다중 고객·다중 현장 격리를 직접 다루지 않는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "FogROS2-FT 의 다중 클라우드 복제는 상태 없는(stateless) 로봇 서비스를 대상으로 하므로, 진행 중 작업 상태를 가진 관제 서비스가 재시작한 뒤 작업을 이어 가는 문제(oq-300)는 이 방법만으로 답이 되지 않는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "상태 없는 로봇 서비스를 여러 클라우드에 복제해 가장 먼저 온 응답을 쓰는 방식(초록 기준)에서 나온 판단이다. (재인용: 2026-09-30-05)",
      "as_of": "2024-12",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "이번에 읽은 VDA 5050 3.0.0 명세 범위와 Open-RMF 핵심 문서는 버전 표기 규칙과 '향후 판에서 폐기' 같은 예고 문구는 담지만 폐기 예고 기간이나 구판 지원 기간을 정하지 않아, 로봇 관제 플랫폼 외부 API 의 폐기 정책(oq-207)은 아직 근거가 부족한 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1(주·부·수 버전 의미)과 f9(Read Only API 폐기 예정, 시점은 'future release')에서 나온 판단이다. VDA 5050 원문은 앞 48,820자까지만 읽었다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "VDA 5050 은 연결이 끊긴 로봇이 해제된 구간까지만 계속 수행하게 하고(f3) Open-RMF 는 교통 일정과 협상을 중앙 데이터베이스에 두므로(f10), 41. 플랫폼 아키텍처·외부 API 의 판단 배치 정책은 중앙 조율 서비스를 클라우드와 현장 서버 가운데 어디에 둘지와 함께 끊김 동안 로봇이 계속 갈 수 있는 해제 구간의 길이를 정해야 할 것으로 보인다(oq-206 부분 근거, 42. 분산 시스템·통신·컴퓨팅 구조와 연결).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f10 을 종합한 판단이다. 네이버 ARC 같은 클라우드 위치 추정 구조의 끊김 동작은 이번에도 확인하지 못했다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
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
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 핵심 구성(교통 일정·협상, 작업 계획)과 플릿 어댑터 제어 수준 4종, 수준별 API 제공 상태를 설명하는 공식 문서.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
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
      "accessed": "2026-10-09",
      "summary": "플릿 관제와 이동 로봇 사이 제조사 중립 통신 인터페이스 VDA 5050 3.0.0 명세. MQTT·JSON 전송, 버전 규칙, QoS, 주문·갱신·취소, 범위 제외 항목을 정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 웹 API 서버의 설정, 지원 DB, 프록시 운용, OpenID Connect 인증과 역할·권한 그룹 인가, 사용자 데이터 비동기화 방침을 설명하는 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1031",
      "org": "Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv)",
      "title": "FogROS2-FT: Fault Tolerant Cloud Robotics",
      "published": "2024-12",
      "url": "https://arxiv.org/abs/2412.05408",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 상태 없는 로봇 서비스를 여러 클라우드에 복제해 클라우드 장애와 네트워크 품질 변동에 대응하는 방법을 제안한 논문(이전 실행 초록 확인 내용 재인용).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "sections": [
        "6",
        "7",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 6 — 끊김 동안 해제 구간까지 계속 수행(f3)과 중앙 교통 일정·협상(f10)을 판단 배치 근거로, QoS 수준(f2)·주문 갱신 번호(f4)·클라우드 브로커 주제 조정(f5)·관제/로봇 기능 분담(f7) 추가 / 섹션 7 — VDA 5050 행에 버전 규칙(f1)·QoS(f2)·범위 제외(f6), Open-RMF 행에 어댑터 API 폐기 예고(f9), rmf-web 행에 M2M 인증 설정(f11)·권한 그룹 미구현(f12)·사용자 비동기화(f13)·/docs 와 프록시 설정(f14) 반영(바뀐 출처) / 섹션 9 — 외부 이벤트 전달 보장(f8)과 고객·현장별 격리(f15)를 ROP 직접 범위로, 외부 IT 인터페이스·보안이 로봇–관제 표준 밖임(f6) / 섹션 11 — oq-206 부분 근거 f18, oq-207 부분 근거 f1·f9·f17(미해결), oq-208 부분 근거 f2·f4·f8(미해결), oq-300 부분 근거 f16, 새 질문 1건. 다음 실행 후보: 42. 분산 시스템·통신·컴퓨팅 구조(f2·f3·f18), 51. 인증·권한·격리(f11~f13·f15), 29. 명령·작업 실행의 신뢰성(f4·f8)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "MQTT 서비스 품질 수준",
      "term_en": "MQTT Quality of Service (QoS) Level",
      "definition": "MQTT 에서 메시지 전달 보장을 최선 노력(QoS 0)·최소 한 번(QoS 1)·정확히 한 번(QoS 2)의 세 수준으로 고르게 하는 설정이다."
    },
    {
      "term_ko": "클라이언트 자격 증명 흐름",
      "term_en": "OAuth 2.0 Client Credentials Grant (Machine-to-Machine)",
      "definition": "사람 사용자 없이 서비스나 기계가 자기 자격 증명으로 접근 토큰을 받아 API 를 부르는 OAuth 2.0 인가 방식이다."
    }
  ],
  "open_questions_new": [
    "Open-RMF 웹 API 서버처럼 권한 그룹 자동 결정이 미구현인 오픈소스 관제 API 위에서 고객·현장별 자원 격리를 API 수준으로 구현한 공개 사례나 설계 문서가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 51. 인증·권한·격리 | 근거: f12 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 4,
    "cross_checked_count": 0,
    "unverified": [
      "oq-209 미조사: 국내 TTA·KS 참조 구조 표준 검색을 하지 않음",
      "oq-301 미조사: OpenAPI·AsyncAPI 기반 연동 적합성 시험 도구 검색을 하지 않음",
      "oq-267 미조사: 과금 단위 비교 자료",
      "섹션 5 상업 시설·가정·실외 사례 미조사",
      "ref-031 VDA 5050 3.0.0 발행일 미확인, 원문 텍스트는 앞 48,820자까지만 읽어 폐기 예고 기간 등 뒷부분 서술 미확인",
      "f16 근거 ref-1031 은 이전 실행 확인 내용 재인용이며 원문 미열람",
      "rmf-web README 의 M2M 클레임 설정(f11)이 지난 확인(2026-09-30) 이후 새로 들어갔는지는 변경 이력을 보지 않아 미확인"
    ],
    "scope_violations": [
      "f3·f7: 위치 추정·경로 실행 같은 로봇 기능과 끊김 때 로봇 동작은 로봇 자체 지능·제어 쪽 연계 대상이며, ROP 몫은 해제 구간 설정과 관제 기능 배치로 한정해 서술해야 함",
      "f6: 사이버보안·안전 요구는 52. 통신 보호·위협 관리·감사와 M. 안전 쪽이므로 이 영역에서는 '표준 범위 밖'이라는 사실만 씀",
      "f16: 클라우드 제공자 인프라는 외부 연계 대상이며 상태 연속성 논의는 42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포와 함께 다뤄야 함"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 0
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치: f8·f10·f23·f24 가 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts/ref-004·ref-031·ref-762, fetched_via inbox)와 이전 브리프 2026-09-30-05 의 재인용 1건(ref-1031)만으로 브리프를 다시 구성했다. 벤더 문서(MiR·Locus·InOrbit·NAVER)를 근거로 한 finding 은 이번 브리프에 없고, [사실] finding 은 모두 표준(ref-031) 또는 오픈소스 문서(ref-004·ref-762)만 근거로 한다. 따라서 vendor_claim 이 필요한 finding 이 없다. 검색 0회, 신규 출처 0건으로 예약 구간 ref-1397~ref-1426 은 쓰지 않았다. 재사용 4건 중 3건은 원문을 열었고(inbox), ref-1031 은 원문 미열람으로 표시했다. 교차 확인 0건이며 모든 사실 finding 은 단일 출처라 신뢰도 medium 이하다. 갱신(update) 실행이고 정정 요청이 없어 바뀐 출처(rmf-web API 서버)와 약한 절(6·7·9·11절)만 다뤘다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-206 은 f18, oq-207 은 f1·f9·f17, oq-208 은 f2·f4·f8, oq-300 은 f16. 현장 유형 사례 finding 은 없다(site_type 모두 null). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 MQTT·MQTT 유언 메시지·의미적 버전 관리·멱등성 키·웹훅·플릿 제어 수준은 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-17/verification.json

```json
{
  "run_id": "2026-10-09-17",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-031)과 검증자 WebFetch(raw.githubusercontent.com, 2026-10-09)로 1장 의미적 버전 관리 문장과 4.2절 majorVersion('v' 접두) 예시를 확인했다. 다만 4.2절의 주제 단계 구조는 지역(local) 브로커용 '제안'이고 클라우드 브로커는 조정할 수 있으므로(f5) '넣게 한다'는 단정을 한정해야 한다. 원문의 typically·generally·usually 도 살린다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4장(무선망 연결 끊김·메시지 손실 고려)과 4.1절(QoS 0 대상 7개 주제, connection 은 QoS 1, 유언 메시지)을 원문으로 확인했다. 원문이 밝힌 QoS 0 선택 이유는 '통신 부하 감소'이고 끊김·손실 고려는 4장 전체의 전제다. claim 문장은 두 내용을 인과로 묶었으므로 이유를 구분하게 수정한다. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.1절(끊긴 로봇은 주문 정보를 유지하고 마지막 해제 노드까지 수행)과 6.1.2절(base 변경 불가, 이미 실행된 것으로 간주, 취소 절차도 신뢰할 수 없음)을 원문으로 확인했다. 끊김 동안의 로봇 동작은 로봇 자체 지능·제어 쪽 연계 대상으로 표시한다. 단일 출처."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.1.2절(orderUpdateId 증가)과 6.1.4.4·6.1.4.5절(OUTDATED_ORDER_UPDATE·SAME_ORDER_UPDATE_ID, 둘 다 WARNING, 같은 내용이면 무시)을 원문으로 확인했다. 내용상 29. 명령·작업 실행의 신뢰성과 가깝다. 41에서는 전달 보장 근거로만 쓰고 29번과 연결한다. 단일 출처."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.2절 문장(클라우드 사업자의 필수 주제 구조, 개별 조정 가능, 제안 구조를 대략 따라야 함, 주제 이름 필수)을 원문과 검증자 WebFetch로 확인했다. claim 에 '제안 구조를 대략 따라야 한다'는 조건을 함께 쓴다. 단일 출처."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2장 Scope 의 제외 항목(Safety Requirements, Traffic Management Logic, Other Communication Interfaces, Operational Responsibilities, Cybersecurity Measures)과 4.1절 보안 문장을 원문으로 확인했다. 사이버보안은 52. 통신 보호·위협 관리·감사, 안전은 M. 안전과 연결만 한다. 단일 출처."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 5.3절·5.4절 목록을 원문으로 확인했다. 원문의 경로 계산은 '선 유도(line-guided) 로봇의 경로 계산·안내'이므로 한정어를 보충한다. 5.3절은 관제의 교통 통제 기능을 들지만 2장은 교통 관리 로직을 범위 밖에 둔다. 따라서 '기능은 요구하되 로직은 정하지 않는다'로 쓴다. flow_item '수행 자원'이 있으나 site_type 이 없으므로 현장 유형 매트릭스에는 쓰지 않는다. 단일 출처."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f2·f4·f6 에서 도출한 [추정]이다. 명세가 외부 이벤트 전달 보장을 말하지 않는다는 점은 브리프도 밝혔다. 버전 표기 자체는 재전송·순서 문제를 다루지 않는다. 재전송·순서 처리는 orderUpdateId 쪽으로 한정해 쓴다. oq-208 은 부분 근거일 뿐이며 해결로 보지 않는다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 강등(최신성): 원문 ref-004(Open-RMF 책 rmf-core 장, 작성 시점 미확인)가 네 플릿 제어 수준, Full Control C++ API(파이썬 바인딩), Read Only 예비 ROS 2 메시지 API 폐기 예정, Traffic Light 재사용 API 미구현을 적는 것은 확인했다. 그러나 같은 문서의 표는 Traffic Light 에 '(API available)'라고 적어 본문과 어긋난다. 검증자가 2026-10-09 검색한 Open-RMF rmf_ros2 API 문서(latest)에는 rmf_fleet_adapter 의 EasyTrafficLight 클래스와 add_easy_traffic_light 가 있다. 그러므로 'Traffic Light 재사용 API 미구현'과 'Read Only API 폐기 예정'은 현재 상태로 볼 수 없어 [추정]으로 강등하고 책의 서술임을 밝힌다. 네 제어 수준 구분과 Full Control C++ API 는 [사실]로 유지한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Prevention·Negotiation·Traffic Schedule 절(플랫폼 중립 일정 DB, 모든 플릿 관리자의 예상 경로 보고, 협상, 시스템 통합사가 둔 제3자 판정자, 긴급 작업의 의도적 충돌 게시)을 원문으로 확인했다. 내용상 27. 다중 로봇 경로·교통 관리 — MAPF 와 가깝다. 41에서는 중앙 조율을 어디에 둘지 정하는 근거로만 쓴다. 단일 출처."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 의 OpenID Connect 절과 Access Token Format·Access Token Claims 절(JWT 독립 검증, preferred_username, client_credentials(M2M) 흐름용 선택 설정 preferred_username_claim_namespace, RFC 9068·RFC 7519 근거)을 원문으로 확인했다. 2026-09-30 이후 새로 들어간 설정인지는 확인하지 못했다(검증자의 GitHub 변경 이력 열람도 HTTP 403). 따라서 '새로 추가됐다'고 쓰지 않는다. OIDC·JWT 독립 검증 부분은 이전 브리프 2026-09-30-05 f2 와 겹친다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Roles, Actions and Authorization Group 절과 TODO 절을 원문으로 확인했다. TODO 절의 '빈 그룹' 문장은 이 출처의 유일한 직접 인용이다. 이것은 README 문서의 진술이며 코드 동작은 확인하지 않았으므로 'README TODO 절 기준'으로 쓴다. 역할·동작·권한 그룹 3값 구조는 이전 브리프 2026-09-30-05 f2 와 겹친다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Synchronization (or lack of) of User Data 절(첫 접근 시 권한 없는 사용자 자동 생성, 관리자 엔드포인트는 rmf-server DB 에만 작용, 삭제해도 반보호 API·대시보드 로그인은 막지 못함, 완전 삭제는 신원 제공자에서)을 원문으로 확인했다. 단일 출처."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: API 절(공개 문서 사이트와 /docs)과 Running behind a proxy 절(public_url, 접두어 제거 필수)을 원문으로 확인했다. /docs 부분은 이전 브리프 2026-09-30-05 f1 과 겹치므로 새로 쓰지 않는다. 기존 문장의 각주만 재사용한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f12·f13 에서 도출한 [추정]이다. README 가 다중 고객·현장 격리를 다루지 않는다는 점과 맞다. 고객·현장 격리 자체는 51. 인증·권한·격리의 일이다. 41 9절에는 '외부 API 의 인증·권한 범위' 쪽으로만 쓰고 51번과 연결한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "브리프 기준 원문 미열람(이전 실행 재인용)이다. 검증자가 2026-10-09 arXiv 초록 페이지(2412.05408, 2024-12-06 제출, IROS 2024)를 열어 '독립적인 상태 없는(stateless) 로봇 서비스를 복제한다'는 서술을 확인했다. [추정] 판단으로 유지한다. 이 방법만으로 oq-300 에 답할 수 없다는 판단도 유지한다. 해결로 보지 않는다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 브리프는 VDA 5050 원문을 앞 48,820자만 읽었다. 검증자가 WebFetch 로 약 207,700자 가운데 앞 200,000자를 확인한 결과 폐기 예고 기간·구판 지원 기간 규정은 없었다. 관련 서술은 1장 버전 규칙, 7.1절 'JSON 스키마는 릴리스마다 갱신', 7.2절 헤더 version 필드뿐이었다. Open-RMF 쪽 '향후 판' 표현은 f9 강등과 함께 책의 서술로 다룬다. 주장 범위는 두 출처로 한정한다. 용어집의 'API 폐기 정책' 항목과 연결하고 위키 전체에 근거가 없다고 쓰지 않는다. oq-207 은 열림을 유지한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f3·f10 에서 도출한 [추정]이다. base(해제된 구간)의 길이를 정하는 일은 관제의 교통 통제 기능(f7)에 걸치므로 27. 다중 로봇 경로·교통 관리 — MAPF, 42. 분산 시스템·통신·컴퓨팅 구조와 연결한다. oq-206 은 부분 근거이며 열림을 유지한다. 네이버 ARC 의 끊김 동작은 여전히 미확인이다."
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
      "f11·f12 의 OpenID Connect·JWT 독립 검증·역할–동작–권한 그룹 구조는 이전 브리프 2026-09-30-05 f2(현재 41 페이지 7절 주제 페이지·9절의 [^ref-762] 문장)와 겹친다 — 새로 쓰는 것은 M2M 네임스페이스 설정·빈 그룹·사용자 비동기화뿐이다",
      "f14 의 /docs API 정의는 2026-09-30-05 f1 과 겹친다",
      "f1 의 MQTT 주제 단계 구조(interfaceName/majorVersion/…)는 2026-09-30-05 f5 와 겹친다",
      "f9 의 네 플릿 제어 수준·Full Control C++ API 는 2026-09-30-05 f4 와 겹치고 용어집 '플릿 제어 수준' 항목과도 겹친다",
      "f9 근거 ref-004 내부 불일치: 표는 Traffic Light 에 '(API available)', 본문은 재사용 API 미구현이라고 적는다. 검증자가 확인한 현재 Open-RMF rmf_ros2 API 문서에는 EasyTrafficLight 가 있다",
      "f17(폐기 정책 근거 부족)은 용어집의 'API 폐기 정책(api-deprecation-policy)' 항목과 맞닿는다 — 위키 다른 곳에 이미 정리된 근거가 있을 수 있다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f3·f18 의 '해제(released) 노드·해제 구간'은 용어집 '해제 구역(Release Zone)'과 다른 개념이다. VDA 5050 의 base(해제된 노드·엣지 집합)임을 첫 등장 때 영문과 함께 밝혀 구분한다",
      "f9 의 '제어 수준'은 용어집 표기 '플릿 제어 수준(Fleet Control Level)'으로 맞춘다",
      "용어 후보 'MQTT 서비스 품질 수준'의 정의 가운데 QoS 2(정확히 한 번)는 브리프 출처(ref-031)에 근거가 없다(원문은 QoS 0·1만 쓴다)"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f1: 주제 경로에 'v'를 붙인 주 버전을 넣는다는 부분을 'VDA 5050 3.0.0 이 지역(local) 브로커용으로 제안하는 주제 구조에서'로 한정한다. 주·부·수 버전 의미에는 원문의 '대체로'를 살린다 — 4.2절은 주제 구조를 엄격히 정하지 않으며 클라우드 브로커는 조정할 수 있다(f5).",
    "f2: QoS 0 을 쓰는 이유를 '통신 부하를 줄이기 위해'로 적는다. '무선망의 연결 끊김과 메시지 손실을 고려한다'는 통신 전반의 전제로 문장을 나눈다 — 원문 4.1절이 밝힌 QoS 0 선택 이유는 부하 감소이고, 끊김·손실 고려는 4장 첫 문장의 전제다.",
    "f5: '클라우드 브로커는 구조를 개별 조정할 수 있으나 제안 구조를 대략 따라야 한다'는 조건을 함께 쓴다 — 원문 4.2절의 단서를 빼면 과장된다.",
    "f7: '경로 계산'을 '선 유도(line-guided) 로봇의 경로 계산·안내'로 고친다. 위치 추정·경로 실행 같은 로봇 기능 목록 앞에 '연계 대상: 로봇 자체 지능·제어'를 표시한다. 관제의 교통 통제 기능은 '명세가 기능을 요구하되 그 로직은 범위 밖에 둔다(f6)'로 써서 두 문장이 모순처럼 읽히지 않게 한다.",
    "f9: 네 플릿 제어 수준 구분과 Full Control 용 C++ API(파이썬 바인딩)는 [사실]로 둔다. 'Read Only 예비 ROS 2 메시지 API 의 향후 폐기 예정'과 'Traffic Light 재사용 API 미구현'은 [추정]으로 강등한다. 이 두 내용은 'Open-RMF 책 rmf-core 장(작성 시점 미확인)의 서술'로 밝히고 현재 상태는 미확인으로 둔다 — 같은 문서 표에는 Traffic Light 가 '(API available)'로 적혀 본문과 어긋난다. 검증 시점의 Open-RMF rmf_ros2 API 문서에는 EasyTrafficLight 가 있어 문서가 오래됐을 수 있다. 현재 상태 확인은 additional_research_requests 로 넘긴다.",
    "f17: 주장 범위를 '이번에 확인한 두 출처(VDA 5050 3.0.0 명세, Open-RMF 책 rmf-core 장)에서는'으로 한정한다. 11절 oq-207 서술에 용어집 [API 폐기 정책](api-deprecation-policy) 링크를 단다. 위키 전체에 근거가 없다는 식으로 쓰지 않는다. oq-207 은 '열림'을 유지한다 — 용어집에 같은 주제 항목이 있다.",
    "f11: M2M 네임스페이스 클레임 설정을 '2026-09-30 이후 새로 추가됐다'고 쓰지 않고 '2026-10-09 확인한 README 에 있다'로만 쓴다 — 변경 이력을 리서치·검증 모두 확인하지 못했다.",
    "f12: '현재는 모든 자원이 기본 빈 그룹에 들어간다'를 'README 의 TODO 절 기준'으로 밝힌다. 코드 동작으로 확인한 것처럼 쓰지 않는다 — 근거는 README 문서뿐이다.",
    "f11·f12·f14 중복: OIDC·JWT 독립 검증, 역할–동작–권한 그룹 3값 구조, /docs API 정의는 이미 41 페이지(7절 주제 페이지·9절)에 [^ref-762]로 있다. 새 문장으로 반복하지 말고 기존 각주를 재사용한다. 새로 더할 것은 M2M 네임스페이스 설정(f11), 빈 그룹(f12), 사용자 비동기화(f13), 프록시 설정(f14 후반)뿐이다 — 2026-09-30-05 f1·f2 와 겹친다.",
    "f1·f9 중복: VDA 5050 주제 구조와 Open-RMF 네 제어 수준은 기존 서술(2026-09-30-05 f4·f5)을 갱신하는 방식으로 반영한다. 새 각주를 만들지 않고 [^ref-031]·[^ref-004]를 재사용한다.",
    "f3·f18 용어: '해제된 노드·해제 구간'이 처음 나올 때 'base(관제가 해제한 노드·엣지 구간)'로 영문을 함께 쓴다. 용어집 '해제 구역(Release Zone)'과 다른 개념임이 드러나게 한다.",
    "f9 표기: '제어 수준'을 용어집 표기 [플릿 제어 수준](fleet-control-level)으로 통일한다.",
    "f3·f7 범위: 연결이 끊긴 로봇이 base 끝까지 수행하는 동작과 위치 추정·경로 실행은 '연계 대상: 로봇 자체 지능·제어'로 표시한다. ROP 몫은 base·horizon 해제 정책과 인터페이스로 한정해 서술한다 — 분류 원문 19장 경계.",
    "f8·f15·f18: 9절과 11절에서 [추정]으로 유지하고 구축자 판단임을 밝힌다. f15 의 고객·현장 격리는 [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)와 연결한다. f6 의 사이버보안 제외는 [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)와 연결한다. f4 는 29. 명령·작업 실행의 신뢰성, f10·f18 은 27. 다중 로봇 경로·교통 관리 — MAPF·42. 분산 시스템·통신·컴퓨팅 구조와 번호와 이름을 함께 써서 연결만 한다 — 이 메커니즘들은 해당 영역의 본론이다.",
    "11절 열린 질문: oq-206(f18)·oq-207(f1·f9·f17)·oq-208(f2·f4·f8)·oq-300(f16)은 부분 근거만 적고 상태는 '열림'을 유지한다. 새 질문 1건은 관련 영역 41·51 로 등록한다 — 해결 제안이 없고 남은 finding 이 모두 부분 근거다.",
    "용어 후보 'MQTT 서비스 품질 수준': 정의에서 QoS 2(정확히 한 번)를 빼거나 '미확인'으로 둔다. 기존 용어집 'mqtt' 항목에 같은 정의가 있으면 새로 등록하지 않는다 — 브리프 출처는 QoS 0·1만 뒷받침한다.",
    "각주: [^ref-004]·[^ref-031]·[^ref-762]는 참고문헌 색인의 줄 형식에 접근일 2026-10-09 를 쓴다. [^ref-1031]은 이번 실행에서 리서치 에이전트가 다시 열지 않았으므로 기존 줄(접근일 2026-09-30)을 그대로 둔다. reference_updates 에서 접근일을 2026-10-09 로 바꾸지 않는다 — 브리프 sources 의 accessed 값은 실제 열람일과 맞지 않는다.",
    "5절·현장 유형 매트릭스: f7(flow_item 수행 자원)·f12(flow_item 제약)는 site_type 이 없다. 그러므로 site_matrix_updates 를 내지 않고 5. 적용 사례 (현장 유형 명시) 절도 바꾸지 않는다 — 현장 유형을 밝히지 않은 finding 은 사례 칸에 넣을 수 없다.",
    "차등 갱신: patches 는 6·7·9·11절만 다룬다. 6·7·11절은 기존 요약 문장과 주제 페이지 링크를 지우지 말고 이번 finding 반영 문장을 덧붙이는 방식(append 또는 요약 유지 replace)으로 쓴다 — 세 절의 본문은 2026-09-30 자동 분리로 주제 페이지에 있다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 18건, 미확인 0건, 교차 확인 0건. 강등: f9 사실 → 추정(Read Only API 폐기 예정·Traffic Light 재사용 API 미구현 부분. Open-RMF 책 rmf-core 장은 작성 시점이 미확인이고 표와 본문이 어긋난다. 검증 시점 Open-RMF rmf_ros2 API 문서에는 EasyTrafficLight 가 있다). 원문 미열람 출처: ref-1031(브리프 기준. 검증자가 2026-10-09 arXiv 초록에서 '상태 없는 로봇 서비스 복제' 서술을 확인함). 주의: 사실 finding 13건은 모두 단일 출처(VDA 5050 3.0.0 명세 ref-031, Open-RMF 문서 ref-004·ref-762)다. 9절에 더할 외부 이벤트 전달 보장(f8)과 고객·현장 격리(f15)는 구축자 판단인 [추정]이다. VDA 5050 은 리서치가 앞 48,820자만 읽었다. 검증자가 앞 200,000자까지 확인한 결과 폐기 예고 기간·구판 지원 기간 규정은 없었다(f17 보강, 마지막 약 7,700자는 미확인). rmf-web README 의 M2M 설정이 언제 들어갔는지는 변경 이력 열람(HTTP 403)으로도 확인하지 못했다. 이번 브리프는 재실행에서 검색 0회·신규 출처 0건이다. 그래서 한국어 검색이 없고, oq-209(국내 TTA·KS 참조 구조 표준)·oq-267·oq-301 과 상업 시설·가정·실외 사례는 조사되지 않았다. 브리프 출처 표기가 sources 의 fetched_via 'github_raw'와 self_check 의 'inbox'로 어긋나지만, 입력에 원문 텍스트가 있어 열람 근거는 있다. oq-206·oq-207·oq-208·oq-300 은 부분 근거만 있어 열림을 유지한다. 정정 요청 없음.",
  "retry_reason": null
}
```

### docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [클라우드 로보틱스, 현장 클라우드, 외부 API, OpenAPI, AsyncAPI, 플릿 어댑터]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-004, ref-031, ref-762, ref-304, ref-1023, ref-937, ref-1024, ref-1025, ref-1026, ref-870, ref-308, ref-1027, ref-1028, ref-1029, ref-774, ref-1030, ref-1031]
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
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
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

이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 단일 접점이 되고, 판단을 어디에 두느냐가 운영 연속성을 좌우하므로 이 영역이 중요하다. [추정][^ref-031][^ref-774][^ref-1030][^ref-1031]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 왜 중요한가](../../topics/2026/2026-09-30-area41-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 절은 판단 배치와 외부 API 를 이해하는 데 필요한 개념인 클라우드 로보틱스·계산 오프로딩·현장 클라우드·플릿 어댑터와 제어 수준·OpenAPI·AsyncAPI·웹훅·브레인리스 로봇을 정리한다.

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
| 수행 자원 | 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리, 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·정보통신기술(ICT) 시스템용 API)의 네 영역이 역할을 나눈다. [사실][^ref-937] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 특정 병원의 배치 결과가 아니라 싱가포르 창이종합병원 CHART 가 공공 의료기관용으로 내놓은 미들웨어 구조다. [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)(Robotic Middleware for Healthcare)는 OMG DDS(Data Distribution Service)를 쓰며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다. [사실][^ref-937] 외부 시스템용 API 를 통합 영역으로 따로 두는 점이 이 영역의 "외부에 무엇을 열 것인가"와 이어진다(구축자 의견). [의견][^ref-937]

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
| 시작 조건 | 창고 관리 시스템(Warehouse Management System, WMS)에서 주문을 API 로 받는다. [추정] 벤더 주장[^ref-1030] |
| 작업 대상 | WMS 주문 정보와 피킹할 품목. [추정] 벤더 주장[^ref-1030] |
| 수행 자원 | LocusONE 플랫폼이 주문을 피킹 효율 기준으로 최적화해 로봇 작업으로 내린다. [추정] 벤더 주장[^ref-1030] |
| 제약 | 기존 인프라와 분리된 전용 WiFi 망을 설치·유지한다. [추정] 벤더 주장[^ref-1030] |
| 완료·인계 | 피킹 완료 확인을 WMS 로 즉시 회신한다. [추정] 벤더 주장[^ref-1030] |
| 예외·성과 | 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 데이터를 제공한다. 실패 시 복구 주체는 미확인. [추정] 벤더 주장[^ref-1030] |

흐름 단계로는 피킹에 해당한다. 외부 API 가 작업의 시작(주문 수신)과 끝(확인 회신)을 모두 맡는 구조다. [추정] 벤더 주장[^ref-1030] 플랫폼을 클라우드와 현장 가운데 어디에 두는지는 자료에 나오지 않는다(미확인). 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽의 일이고, ROP 는 연동 인터페이스만 다룬다(9절). [추정][^ref-1030]

### 기타

**현장 유형:** 기타

**사례:** 기업 사옥에서 클라우드로 로봇 운영(네이버 제2사옥 1784 의 ARC)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 클라우드의 ARC brain(이동 계획·위치 추정·작업 수행·기반 시설 연동), ARC eye(디지털 트윈 데이터와 측위 AI 로 로봇 위치 결정), ARC mind(웹 개발자용 웹 기반 OS)가 나눠 맡고, 로봇은 연산·판단을 싣지 않는다. [추정] 벤더 주장[^ref-1023] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

네이버는 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다. [추정] 벤더 주장[^ref-1023] 위치 추정·이동 계획까지 클라우드에 두는 이 설계는 분류 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 볼 수 있으며, ROP 직접 범위의 근거로 쓰지 않는다(9절). [추정][^ref-1023] ARC mind 는 웹 개발자가 로봇 서비스를 만들게 한다는 점에서 개발자에게 여는 인터페이스의 예다. [추정] 벤더 주장[^ref-1023]

## 6. 대표 접근법과 기술

이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1027][^ref-308][^ref-304][^ref-1031][^ref-004][^ref-1025][^ref-1024]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-09-30-area41-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다(구축자 의견). [의견][^ref-004][^ref-937][^ref-031][^ref-1025][^ref-1024][^ref-304]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area41-s7.md)에 있다.

## 8. 대표 연구와 자료

판단 배치와 장애 대응의 근거는 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구이며, 모두 논문 초록 기준이다. [사실][^ref-304][^ref-1031][^ref-1027][^ref-308]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료](../../topics/2026/2026-09-30-area41-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처, 작업 요청·작업 상태·플릿 상태의 기계가독 스키마, REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기, API 호출의 인증·권한, 그리고 판단·데이터를 로봇·현장 서버·클라우드 가운데 어디에 둘지 정하는 배치 정책으로 보인다. [추정][^ref-004][^ref-937][^ref-1028][^ref-031][^ref-1025][^ref-1024][^ref-762]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터로 로봇·제조사 관제의 기능·상태를 주고받는 인터페이스와 판단 배치 정책. [추정][^ref-004] | 연계 대상: 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능은 로봇 제조사가 맡는다. FogROS2 같은 오프로딩은 로봇 내부 기능의 실행 위치 선택이다. [추정][^ref-304][^ref-1027] |
| 상위 업무 시스템 | 업무 시스템이 부르는 외부 API(요청 수신·결과 회신)와 그 인증·권한. [추정][^ref-762][^ref-1030] | 연계 대상: 주문·재고 같은 업무 판단은 WMS·ERP 가 맡는다. [추정][^ref-1030] |

클라우드 제공자 인프라는 외부 연계 대상이고, 현장 네트워크 설계는 ROP 의 다른 세부영역인 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)에서 다룬다. [추정][^ref-1031][^ref-1030]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

네이버가 밝힌 ARC 처럼 위치 추정·이동 계획까지 클라우드에 두는 설계는 위 경계를 제품 전략으로 옮긴 사례이며, 이종 제조사를 연결하는 ROP 의 직접 범위로 보지 않는다. [추정] 벤더 주장[^ref-1023] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 같은 K. 플랫폼 아키텍처·인프라의 네트워크·데이터 영역, F. 연동의 네 영역, 보안·관제·복구 영역, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1031][^ref-004]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md)에 있다.

## 11. 열린 질문

판단 배치의 단절 대응, 외부 API 의 수명주기와 전달 보장, 국내 표준 여부가 아직 확인되지 않았다.

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 열린 질문](../../topics/2026/2026-09-30-area41-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md) — 섹션 3~11 신규 작성(seed → draft): 판단 배치 혼합 구조, 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건. 1차 조건부 승인 수정 17건과 2차 수정 5건(3절 일반화 2건 좁힘, 4절 도입 단락, [의견] 주체 표시, 약어 풀이) 이행 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-09-30-area41-s6.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "6. 대표 접근법과 기술" 절(3,254자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어](../../topics/2026/2026-09-30-area41-s4.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "4. 핵심 개념과 용어" 절(1,132자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area41-s7.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "7. 관련 표준·프레임워크·오픈소스" 절(962자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(879자)을 옮겼다 (실행 2026-09-30-05)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1027]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1028]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30
```

### docs/categories/platform-architecture-and-infrastructure/index.md

```markdown
---
title: "K. 플랫폼 아키텍처·인프라"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-004, ref-009, ref-031, ref-045, ref-051, ref-105, ref-148, ref-251, ref-282, ref-287, ref-300, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-374, ref-401, ref-405, ref-493, ref-762, ref-766, ref-831, ref-854, ref-937, ref-943, ref-1023, ref-1024, ref-1025, ref-1030, ref-1031, ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1120]
---

[홈](../../index.md) › K. 플랫폼 아키텍처·인프라

# K. 플랫폼 아키텍처·인프라

## 핵심 질문

플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

## 개요

플랫폼의 구조, 클라우드·현장 서버·로봇의 역할 분담, 네트워크·가용성·다현장, 데이터·관측성·배포·비용. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **41. 플랫폼 아키텍처·외부 API** | 기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK | 어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? | [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md) | published |
| **42. 분산 시스템·통신·컴퓨팅 구조** | 현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? | [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md) | published |
| **43. 데이터·관측성·배포** | 데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 | 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? | [43. 데이터·관측성·배포](data-observability-and-deployment.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

플랫폼 구조는 현장의 네트워크 조건을 전제로 정해야 한다. **연결이 끊겼을 때 현장에서 계속할 수 있는 범위**가 구조 선택의 기준이 된다. [분류원문]

## 다른 대분류와의 연결

K. 플랫폼 아키텍처·인프라의 세 세부영역, 곧 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](data-observability-and-deployment.md)는 다른 대분류의 기능이 어디에서 돌고, 연결이 끊겼을 때 무엇을 이어 가며, 무엇을 기록으로 남기는지를 정한다. 아래 연결은 게시된 세부영역 페이지와 다른 대분류 페이지에 실린 검증된 주장을 대분류별로 묶은 것이다. 근거는 모두 단일 출처이거나 기존 페이지의 재인용이며, 교차 확인된 것은 없다. 두 영역을 잇는 해석은 추정 태그로 표시했고, 제조사·판매사 자료에 기댄 내용에는 벤더 주장을 함께 적었다.

### A. 기획·사업

[A. 기획·사업](../planning-and-business/index.md)과는 비용과 업체 전략에서 만난다.

- **43. 데이터·관측성·배포 ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)**: FinOps Foundation 은 클라우드 비용 관리를 알리기(Inform)·최적화(Optimize)·운영(Operate) 단계가 되풀이되는 주기로 설명한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1041] 같은 재단은 2025-06-03 클라우드 청구 데이터 명세 FOCUS 1.2 를 발표하면서 서비스형 소프트웨어(Software as a Service, SaaS)·서비스형 플랫폼(Platform as a Service, PaaS) 청구 데이터 지원과 청구서 대사(invoice reconciliation)를 더했다고 밝혔다(발표 글 기준이며 명세 본문은 미열람). [사실][^ref-1042] 43. 데이터·관측성·배포가 계측·배분하는 클라우드·언어 모델 호출 비용은 3. 경제성·조달·사업 모델의 총소유비용 산정과 과금 단위 결정의 입력이 될 것으로 보이나, 다중 제조사 오케스트레이션 플랫폼의 과금 단위를 공개한 자료는 확인되지 않았다(oq-267). [추정][^ref-1041][^ref-1042][^ref-1037]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 3. 경제성·조달·사업 모델**: FreightWaves 기사는 하이브리드 창고 관리 시스템(Warehouse Management System, WMS) 판매사의 조사를 인용해 창고 운영 중단 비용이 시간당 최대 10만 달러라고 전하며, 이는 연결 단절이 물류창고 투자 효과 판단에 들어갈 위험 비용이 될 수 있음을 보여 준다(기사 발행일·조사 방법·표본·하한 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-309]
- **41. 플랫폼 아키텍처·외부 API ↔ [1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md)**: 업체 사례로, 네이버는 제2사옥 1784(기타 현장, 기업 사옥)에서 로봇 100여 대를 클라우드로 제어하고 로봇에는 연산·판단을 싣지 않는 구조를 쓴다고 밝힌다(발행일 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-1023]

### B. 로봇 온톨로지

[B. 로봇 온톨로지](../robot-ontology/index.md)와는 어댑터 설정과 버전 기록에서 만난다.

- **41. 플랫폼 아키텍처·외부 API ↔ [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md)**: Open-RMF 플릿 어댑터 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-105] 41. 플랫폼 아키텍처·외부 API가 ROP 직접 범위로 두는 제조사 어댑터 계층은 6. 온톨로지 기반 시스템·로봇 연동이 능력 모델에서 만드는 어댑터 설정·명령 매핑 초안이 반영되는 자리가 될 것으로 보이나, 그렇게 초안을 만든 공개 사례는 확인되지 않았다. [추정][^ref-004][^ref-105]
- **43. 데이터·관측성·배포 ↔ [7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md)**: 43. 데이터·관측성·배포가 남기는 소프트웨어·펌웨어 배포 버전 기록은 7. 온톨로지 검증·변경 관리가 능력 정의를 다시 검증할 계기를 알려 주는 입력이 될 것으로 보이나, 두 기록을 잇는 공개 사례는 확인하지 못했다. [추정][^ref-1040]

### C. 채팅 기반 구성·운영

[C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)과는 대화가 부르는 외부 API 와 언어 모델 호출 계측에서 만난다. 분류 원문 4장 주석은 업무 지시를 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링의 기능을 대화로 쓰게 하는 것으로 보므로, 아래 12. 채팅으로 업무 지시·오케스트레이션 연결은 G. 계획·최적화 항목과 함께 읽는다.

- **41. 플랫폼 아키텍처·외부 API ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)**: Open Robotics 상호운용 SIG 의 2026-07-02 발표 안내문(2026-06-25 게시)은 Nayantra 를 소개했다. Nayantra 는 Open-RMF REST 응용 프로그래밍 인터페이스(Application Programming Interface, API)를 언어 모델이 호출하는 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버와, 평이한 영어 지시를 RMF 임무로 바꾸는 에이전트로 이루어진다(안내문 기준이며 발표 내용 자체는 미열람, 시연은 Isaac Sim 창고 시뮬레이션). [사실][^ref-854]
- **41. 플랫폼 아키텍처·외부 API ↔ [13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md)**: 대화형 기능이 플랫폼 외부 API 를 도구로 부르면, API 의 인증·권한 범위가 13. 대화형 기능의 신뢰·기반이 다루는 사용자별 대화 권한의 실제 집행 지점이 될 것으로 보인다(아래 N. 보안·개인정보 항목과 함께 읽는다). [추정][^ref-854][^ref-762]
- **43. 데이터·관측성·배포 ↔ 13. 대화형 기능의 신뢰·기반**: OpenTelemetry 생성형 AI 의미 규약 저장소는 언어 모델 클라이언트 호출의 토큰 사용량 지표를 정의하며, 이 규약은 아직 개발(Development) 단계다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1037] 13. 대화형 기능의 신뢰·기반이 언어 모델 공급자를 고르고 바꾸려면 43. 데이터·관측성·배포가 호출별 토큰·비용·지연을 계측해야 할 것으로 보이나, 계측 지표 이름은 안정 판이 나오지 않아 고정되지 않았다(oq-212). [추정][^ref-1037][^ref-1043]

### D. 공간·지도 모델

- **41. 플랫폼 아키텍처·외부 API ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)** ([D. 공간·지도 모델](../space-and-map-model/index.md)): 네이버는 ARC eye 가 클라우드에서 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정한다고 밝히지만, 위치 모델을 클라우드에 둔 이 설계에서 연결이 끊기면 로봇이 어디까지 동작하는지는 공개되지 않았다(기타 현장, 기업 사옥, oq-206). [추정] 벤더 주장[^ref-1023] 위치 추정 자체는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이므로, 이 사례는 제품 전략 사례로만 읽고 ROP 직접 범위의 근거로 쓰지 않는다.

### E. 사물·사람·실시간 상태

[E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)와의 연결은 지금의 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이며, I. 설계·시뮬레이션 항목의 미래 실험·지난 기록 재현과 구분한다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: 통신 계층에는 상태가 오래되었음을 알리는 장치가 있으며, ROS 2 서비스 품질(Quality of Service, QoS)의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 이 메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT)의 유언 메시지(Last Will)로 보내는 연결 끊김 통지가 그 예다(세 출처는 각각 한 장치만 다루므로 서로 교차 확인한 것이 아니다, 2026-10-09 확인). [사실][^ref-282][^ref-287][^ref-031] Open-RMF 로봇 상태는 밀리초 단위 유닉스 시각(unix_millis_time)을, VDA 5050 상태는 ISO 8601 형식 시각(timestamp)을 담아 시각 표현이 서로 다르며, 공통 시간축 변환과 허용 시계 오차를 정한 자료는 확인되지 않았다(oq-035). [사실][^ref-148][^ref-051]
- **43. 데이터·관측성·배포 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)·18. 실시간 세계 상태·데이터 일관성**: EPCIS 2.0 온톨로지(2021-09-30)는 발생 시각(eventTime)·기록 시각(recordTime)·UTC 차이를 구분하므로, 실행 기록과 관측 데이터에서도 발생 시각과 수신·기록 시각을 따로 남기는 설계가 두 대분류를 잇는 지점이 될 것으로 보인다. [추정][^ref-045]

### F. 연동

[F. 연동](../integration/index.md)과는 통신 전제, 어댑터 구조, API 명세, 설비·업무 시스템 기록에서 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제해 주문·상태 토픽에 재전송 없는 MQTT QoS 0 을 쓴다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031]
- **41. 플랫폼 아키텍처·외부 API ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 플릿 어댑터는 로봇의 예상 이동 경로를 시설 전체의 중앙 교통 스케줄에 보고하고, 제조사 관제가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 붙는다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004][^ref-251] 두 자료는 같은 기관 문서라 교차 확인은 아니며, 제어 수준별 교통 성능 차이는 미확인이다(oq-032).
- **41. 플랫폼 아키텍처·외부 API ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: OpenAPI 명세 3.1.0(2021-02-15)은 HTTP API 를 언어와 무관하게 기술하는 표준 인터페이스 기술 형식이고, AsyncAPI 명세 3.1.0(발행일 미확인)은 메시지 기반 API 를 기술하는 형식이다. [사실][^ref-1025][^ref-1024] 플랫폼 외부 API 를 두 형식으로 기계가 읽게 기술하면 21. 상호운용 표준·적합성이 다루는 연동 규격 적합성 시험의 기준 문서가 될 수 있을 것으로 보이나, 국내에 통합관제 플랫폼 외부 API 를 정한 TTA·KS 표준이 있는지는 확인되지 않았다(oq-209). [추정][^ref-1025][^ref-1024] 이런 기술 문서를 실제 적합성 시험에 쓴 공개 도구·절차가 있는지는 oq-209 와 함께 새 열린 질문으로 올렸다.
- **43. 데이터·관측성·배포 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: 고려대학교 구로병원 약품 배송 로봇 실증(병원)은 승강기 호출·탑승·문 동작·하차 시각을 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 1 Hz 로 남긴 승강기–로봇 통신 로그, 관찰자 기록지를 함께 모아 실패 원인을 분석했다(2026-03-31 게재). [사실][^ref-943] 승강기 통신 로그를 만드는 일은 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이고, ROP 몫은 그 기록의 수집·결합이다.
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: 물류창고에서 외부망이 끊긴 동안 현장 관제는 이미 받은 주문을 이어 갈 수 있을 것으로 보이나, 클라우드 WMS 의 새 주문 수신과 재고 확정은 멈추고 재연결 뒤 현장 완료 기록과 WMS 기록을 맞추는 절차가 필요할 것으로 보인다(물류센터 운영 기준 미확인, oq-038). [추정][^ref-031][^ref-300][^ref-310] 새 주문과 재고 확정은 분류 원문 19장의 상위 업무 시스템 경계에 속하는 연계 대상이고, ROP 는 받은 요청을 실행하고 결과를 반영하는 쪽을 맡는다.
- **41. 플랫폼 아키텍처·외부 API ↔ 23. 업무 시스템 연동**: Locus Robotics 는 LocusONE 이 WMS 주문을 API 로 받아 로봇 작업으로 내리고 피킹 완료 확인을 WMS 로 즉시 회신한다고 밝힌다(물류창고, 흐름 단계 피킹, 발행일 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-1030] 주문 최적화 판단은 상위 업무 시스템 경계의 WMS·로봇 공급사 몫이고, ROP 는 연동 인터페이스만 다룬다.

### G. 계획·최적화

[G. 계획·최적화](../planning-and-optimization/index.md)와는 배정·교통 계산을 어디에 두는지에서 만난다. 위 C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션이 부르는 엔진도 여기의 25. 작업 배정 — MRTA와 [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)이다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)**: Lott·Honary(2026-09 프리프린트, 초록 기준)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 같은 통신 저하 조건에서 비교했다. [사실][^ref-493] 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보이나, 통신이 나빠질 때 중앙 방식과 분산 방식 사이를 언제 바꿀지 정한 물류센터 기준은 확인되지 않았다(oq-083). [추정][^ref-493][^ref-401]
- **41. 플랫폼 아키텍처·외부 API·42. 분산 시스템·통신·컴퓨팅 구조 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: Open-RMF 교통 관리는 플릿 어댑터가 예상 경로를 중앙 교통 스케줄에 보고하는 구조이므로, 중앙 스케줄을 현장 서버와 클라우드 가운데 어디에 두는지가 단절 때 교통 조율을 계속할 수 있는지를 좌우할 것으로 보인다(실측 자료 없음). [추정][^ref-004]

### H. 실행·협업·예외 복구

[H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)와는 단절·재시작 뒤 일을 어떻게 이어 가는지에서 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] KubeEdge 는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-300]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: VDA 5050 은 주문·상태를 QoS 0 으로 보내고 상태를 사건 발생 시와 최대 30초 간격으로 다시 보내므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 오기를 기대하기보다 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신해야 할 것으로 보인다(VDA 5050 이 MQTT 5.0 세션 만료를 어떻게 쓰는지는 미확인). [추정][^ref-031][^ref-306]
- **43. 데이터·관측성·배포 ↔ 32. 예외 복구·재계획·업무 연속성**: Zhang·Yu·Westerlund(Sensors, 2025-08-14)는 Kubernetes 컨테이너 자동 재시작으로 ROS 2 다중 로봇 시스템이 장애 중에도 초광대역(Ultra-Wideband, UWB) 기반 상대 위치 정확도를 유지했다고 보고했으며, 이는 현장 적용 사례가 아니라 실험실 결과다. [사실][^ref-1039] Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하지만, 이번 확인에서는 이슈 원문을 다시 열지 못해 이슈가 언급한 복구 기능 제안의 내용과 현재 배포판 반영 여부를 재확인하지 못했다(oq-048). [추정][^ref-374]
- **41. 플랫폼 아키텍처·외부 API ↔ 32. 예외 복구·재계획·업무 연속성**: FogROS2-FT(IROS 2024, 초록 기준)는 클라우드 로보틱스의 장애 허용을 다루며, 독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 복제하고 먼저 온 응답을 쓴다. [사실][^ref-1031] 대상이 상태 비저장 서비스이므로, 이 방식을 진행 중인 작업 상태를 보존하는 근거로 읽지 않는다. 플랫폼 서비스를 복제하거나 자동 재시작하면서 진행 중인 작업 상태를 잃지 않은 공개 사례가 있는지는 새 열린 질문으로 올렸고, 어댑터 복구의 배포판 반영(oq-048)·무중단 순차 배포(oq-213)와 함께 본다.

### I. 설계·시뮬레이션

[I. 설계·시뮬레이션](../design-and-simulation/index.md)과의 연결은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 지난 기록을 재현하는 36. 가상 시운전·실제 상황 재현으로 나뉜다. 위 E. 사물·사람·실시간 상태의 현재 상태 표현과 함께 셋을 디지털 트윈이라는 한 이름으로 묶지 않는다.

- **43. 데이터·관측성·배포 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: Ocado 는 교통 관리·오케스트레이션 알고리즘 변경을 실제 창고(물류창고)에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1044] 이 사례는 43. 데이터·관측성·배포 쪽에서는 배포 전 검증의 근거로만 쓰고, 시뮬레이션 자체는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈의 내용으로 둔다.
- **43. 데이터·관측성·배포 ↔ [36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md)**: ROS 2 Iron Irwini(2023-05-23)부터 rosbag2 의 기본 저장 형식은 MCAP 이고, rosbag2 는 재생 속도 조절, /clock 발행, 여러 백 파일을 기록 시각순으로 동시에 재생하는 기능을 지원한다(두 출처는 서로 다른 내용을 말하므로 교차 확인이 아니다). [사실][^ref-1034][^ref-831] 43. 데이터·관측성·배포가 정하는 기록 형식과 보존 기간이 36. 가상 시운전·실제 상황 재현이 재현에 쓸 수 있는 실제 기록의 범위를 정할 것으로 보이며, 이 연결은 지난 기록을 다루는 것이라 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과는 구분된다(oq-211). [추정][^ref-1034][^ref-831]

### J. 현장 운영·관제

[J. 현장 운영·관제](../field-operations-and-monitoring/index.md)와는 실행 기록 저장과 원인 분석용 추적에서 만난다.

- **43. 데이터·관측성·배포 ↔ [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)**: Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하므로, 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]
- **43. 데이터·관측성·배포 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: ros2_tracing(IEEE RA-L, 2022-07)은 LTTng 기반 저부하 추적기로 ROS 2 실행 정보를 모으며, 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가가 평균 0.0033 ms 였다고 보고했다(저자 실험값, 독립 재현 미확인). [사실][^ref-1032] ros2probe(2026-06 프리프린트)는 관찰 도구가 관찰 대상을 교란하는 문제를 커널 선택 관찰로 줄여, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1033] 플랫폼 서비스 쪽 분산 추적(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모으므로, 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다(공개 사례 미확인, oq-210). [추정][^ref-1036][^ref-1032]

### L. AI·학습 기술

[L. AI·학습 기술](../ai-and-learning/index.md)과는 언어 모델·계산을 어디에서 돌리는지에서 만난다. 적용 대상은 이 대분류의 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](data-observability-and-deployment.md)다.

- **42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포 ↔ [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md)**: Bruno·Sim·Hagiwara(2026-09 프리프린트)는 범용 서비스 로봇의 대규모 언어 모델(Large Language Model, LLM) 연쇄 기반 작업 계획에서 로컬 모델과 클라우드 모델을 비교했고 비교의 동기는 클라우드 API 비용과 지연이었으나, 실험은 계획 성공률만 측정했고 비용·지연 자체는 측정하지 않았다. [사실][^ref-1043]
- **41. 플랫폼 아키텍처·외부 API ↔ 44. 로봇 기반 모델·언어 모델 계획**: FogROS2(2022-05)는 ROS 2 로봇의 계산 부담이 큰 작업을 클라우드·포그로 옮겨 실행하는 플랫폼이다. [사실][^ref-304] 로봇 내부 기능의 실행 위치 선택은 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이므로, 이 연구는 계산 배치 선택지의 연구 근거로만 쓴다.

### M. 안전

[M. 안전](../safety/index.md)은 통신 계층과 안전 기능의 구분, 사고 조사용 기록에서 이 대분류와 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: VDA 5050 은 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 그래서 관제 통신 계층과 48. 안전·위험 관리가 다루는 안전 기능은 구분해 다룬다.
- **43. 데이터·관측성·배포 ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md)**: Winfield 외(2022-05-13)의 윤리적 블랙박스 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 기록하는 모듈을 제안하며, 단일 로봇을 대상으로 하고 플릿·플랫폼 수준 기록은 다루지 않는다. [사실][^ref-1120] 사고 조사에 쓸 플랫폼 수준 실행 기록에는 43. 데이터·관측성·배포 쪽의 보존 기간·무결성 관리가 필요할 것으로 보이나, 로봇 플랫폼 기록의 보존 기간을 정한 기준은 개인정보 접속기록 규정 밖에서는 확인되지 않았다(oq-211). [추정][^ref-1120][^ref-766]

### N. 보안·개인정보

[N. 보안·개인정보](../security-and-privacy/index.md)는 외부 API 인증·통신 보호·접속기록에서 이 대분류와 만난다.

- **41. 플랫폼 아키텍처·외부 API ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: Open-RMF API 서버(rmf-server)는 OpenID Connect(OIDC) 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정하며, 관리자는 모든 그룹에서 모든 동작을 할 수 있고 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 51. 인증·권한·격리·[52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)**: ROS 2 는 데이터 분산 서비스(Data Distribution Service, DDS) 보안 규격의 인증(공개 키 기반 구조, PKI)·접근통제(거버넌스·권한 파일)·암호화 플러그인을 쓰고, Open-RMF 문서는 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고 웹 대시보드에는 전송 계층 보안(Transport Layer Security, TLS)·OIDC 인증을 더한다고 설명한다(두 자료는 서로 다른 계층을 설명하므로 교차 확인이 아니다). [사실][^ref-009][^ref-405]
- **43. 데이터·관측성·배포 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)**: 개인정보보호위원회 고시 「개인정보의 안전성 확보조치 기준」은 접속기록의 보관과 점검에 관한 조항을 둔다(2023-09-22 시행 판 고시 제8조 기준, 현행 조문 미확인, oq-214). [사실][^ref-766]

### O. 검증·도입·수명주기

- **43. 데이터·관측성·배포 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)** ([O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)): Mender 는 임베디드 리눅스 장치용 오픈소스 무선(Over-the-Air, OTA) 업데이트 도구로, 이미지 기반 A/B 업데이트와 실패 시 롤백을 지원한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1040] 로봇 운영체제·펌웨어의 무선 업데이트 자체는 연계 대상이다. 43. 데이터·관측성·배포의 배포·롤백 자동화가 57. 자산·소프트웨어 수명주기 관리의 버전 관리와 맞물릴 것으로 보이나, 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구는 확인되지 않았다(oq-213). [추정][^ref-1040][^ref-1039]

### P. 거버넌스·법규·사회

- **43. 데이터·관측성·배포 ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)** ([P. 거버넌스·법규·사회](../governance-law-and-society/index.md)): 연계 대상: 접속기록 보관 같은 법적 의무의 해석과 적용 판단은 59. 법·규제·보험·라이선스와 운영 사업자의 몫으로 보이고, ROP 는 그 기준에 맞춰 기록을 수집·보존·점검하는 기능을 제공하는 쪽으로 보인다(근거 고시는 2023-09-22 시행 판 제8조 기준, 현행 조문 미확인, oq-214). [추정][^ref-766]

P. 거버넌스·법규·사회와의 연결은 현재 위의 연계 대상 추정 하나뿐이다.

### Q. 현장 유형별 적용

[Q. 현장 유형별 적용](../site-type-applications/index.md)에는 현장마다 다른 요구를 모으고, 모든 현장에 공통인 구조 선택은 이 대분류에 둔다. 아래는 위 연결의 근거가 된 사례를 현장 유형별로 다시 묶은 것이다.

- **병원 — [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md) ↔ 41. 플랫폼 아키텍처·외부 API**: 창이종합병원 CHART 의 공공 의료기관용 로봇 미들웨어 RoMi-H 는 기계(하드웨어 추상화)·제어(항법·위치 추정)·중앙(플릿 관리, 로봇–기반 시설 통신)·통합(모바일·웹 앱·ICT 시스템용 API) 네 영역이 역할을 나누는 구조이며 OMG DDS 를 쓴다(2019-10-31 ROSCon 2019 에서 공식 출범). [사실][^ref-937] 이는 특정 병원의 배치 결과가 아니라 미들웨어 구조다.
- **병원 — 63. 병원·의료 ↔ 42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포**: 고려대학교 구로병원 약품 배송 로봇 실증(2025-06, 비응급 임무 122건)의 실패 14건은 승강기 막힘 8건, 복도 주행 4건, 통신 오류 2건이었다(2026-03-31 게재). [사실][^ref-943] 논문이 밝힌 전체 성공률과 이 건수가 맞지 않는 문제는 oq-215 에 있고, 이 실증의 로그 결합은 위 F. 연동 항목에 있다.
- **제조 공장 — [62. 제조 공장](../site-type-applications/manufacturing-plant.md) ↔ 41. 플랫폼 아키텍처·외부 API**: Brorsson 외(2025-12, 초록 기준)는 기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 사내 물류 이동 로봇 기준 아키텍처를 제시하고, 대형 차량(heavy-vehicle) 제조 현장 실배치로 보였다. [사실][^ref-308] 처리량·시간·비용 수치는 확인하지 못했다.
- **물류창고 — [61. 물류창고](../site-type-applications/warehouse.md) ↔ 42. 분산 시스템·통신·컴퓨팅 구조**: CJ대한통운은 2023-04 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G 를 구축했다고 발표하며 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었고, 발표 당시 로봇·설비 적용은 시범 뒤 확대 계획이었다. [추정] 벤더 주장[^ref-307] 무선망 구축은 ROP 가 소유하지 않는 통신 기반으로 연계 대상이다. 물류창고의 다른 근거는 위 A. 기획·사업(운영 중단 비용), F. 연동(단절 중 WMS 연동, 피킹 완료 회신), I. 설계·시뮬레이션(배포 전 시뮬레이션) 항목에 있다.
- **기타 — [67. 기타 현장](../site-type-applications/other-sites.md) ↔ 41. 플랫폼 아키텍처·외부 API**: 기업 사옥 사례(네이버 1784)는 위 A. 기획·사업과 D. 공간·지도 모델 항목에 벤더 주장으로 있다.
- **상업 시설·가정·실외**: [64. 상업 시설](../site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../site-type-applications/home-and-apartment.md), [66. 실외](../site-type-applications/outdoor.md)와 이 대분류를 잇는 근거는 이번 정리에 없다.

### 아직 다루지 않은 연결

이번 정리의 근거가 다루지 않은 세부영역은 다음과 같다. 연결이 없다는 뜻이 아니라 아직 근거를 모으지 않았다는 뜻이다.

- A. 기획·사업: 2. 사용 사례·요구·책임 범위
- B. 로봇 온톨로지: 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현
- C. 채팅 기반 구성·운영: 8. 채팅으로 맵 작성, 9. 채팅으로 시나리오 구성, 10. 채팅으로 로봇 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현
- D. 공간·지도 모델: 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리
- E. 사물·사람·실시간 상태: 19. 사람·보행자 모델
- G. 계획·최적화: 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화
- H. 실행·협업·예외 복구: 30. 로봇 간 협업·물리적 인계, 31. 사람–로봇 협업
- I. 설계·시뮬레이션: 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계
- J. 현장 운영·관제: 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구
- L. AI·학습 기술: 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영
- M. 안전: 49. 사람 근접 안전
- O. 검증·도입·수명주기: 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 56. 운영 이관·확대·교육
- P. 거버넌스·법규·사회: 58. 다사업자 책임·계약·데이터, 60. 노동·수용성·접근성
- Q. 현장 유형별 적용: 64. 상업 시설, 65. 가정·공동주택, 66. 실외

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-10-09
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-09
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-10-09 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-10-09
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-10-09 (원문 미열람)
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-10-09 (원문 미열람)
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-10-09 (원문 미열람)
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-10-09 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-10-09 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-10-09 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-10-09 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2 GitHub), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-10-09 (원문 미열람)
[^ref-401]: KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952, 접근일 2026-10-09 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-10-09
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-10-09 (원문 미열람)
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-766]: 국가법령정보센터(개인정보보호위원회 고시), 개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-10-09 (원문 미열람)
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09 (원문 미열람)
[^ref-937]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-10-09 (원문 미열람)
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-10-09 (원문 미열람)
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-10-09 (원문 미열람)
[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-10-09 (원문 미열람)
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-10-09 (원문 미열람)
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-10-09 (원문 미열람)
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-10-09 (원문 미열람)
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-10-09 (원문 미열람)
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-10-09 (원문 미열람)
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09 (원문 미열람)
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-10-09 (원문 미열람)
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-10-09 (원문 미열람)
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-10-09 (원문 미열람)
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more, 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-10-09 (원문 미열람)
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-10-09 (원문 미열람)
[^ref-1044]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-10-09 (원문 미열람)
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09 (원문 미열람)

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 62건이다(논문 14건 · 기사·보고서 4건 · 업체 발표 9건 · 표준·오픈소스·기관 자료 35건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-493](../../references/ref-493.md) — Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation (발행 2026-09)
- [ref-1043](../../references/ref-1043.md) — Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots (발행 2026-09)
- [ref-1033](../../references/ref-1033.md) — Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware (발행 2026-06)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-308](../../references/ref-308.md) — Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives (발행 2025-12)
- [ref-1039](../../references/ref-1039.md) — Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning (발행 2025-08-14)
- [ref-1031](../../references/ref-1031.md) — Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics (발행 2024-12)
- [ref-1032](../../references/ref-1032.md) — Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 (발행 2022-07)
- [ref-1120](../../references/ref-1120.md) — Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard (발행 2022-05-13)
- [ref-304](../../references/ref-304.md) — Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 (발행 2022-05)
- 그 밖에 4건

**기사·보고서**

- [ref-1026](../../references/ref-1026.md) — 뉴스핌, 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다 (발행 2026-05-13)
- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)
- [ref-309](../../references/ref-309.md) — FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount (발행 미확인)
- [ref-1041](../../references/ref-1041.md) — FinOps Foundation, FinOps Phases (발행 미확인)

**업체 발표**

- [ref-301](../../references/ref-301.md) — Microsoft, Operate Azure IoT Edge devices offline (발행 2026-03-02)
- [ref-1044](../../references/ref-1044.md) — Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale (발행 2025-06-04)
- [ref-227](../../references/ref-227.md) — Mobile Industrial Robots(MiR), MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 (발행 2025-01)
- [ref-307](../../references/ref-307.md) — CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 (발행 2023-04)
- [ref-1035](../../references/ref-1035.md) — Foxglove, MCAP as the ROS 2 Default Bag Format (발행 2022-12-22)
- [ref-774](../../references/ref-774.md) — Mobile Industrial Robots(MiR), MiR Fleet (발행 미확인)
- [ref-1030](../../references/ref-1030.md) — Locus Robotics, Seamless Integrations with LocusOne Robotics (발행 미확인)
- [ref-1029](../../references/ref-1029.md) — InOrbit, Contents — InOrbit Developer Portal (발행 미확인)
- [ref-1023](../../references/ref-1023.md) — NAVER Corp., 로보틱스 l NAVER Corp. (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-854](../../references/ref-854.md) — Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) (발행 2026-06-25)
- [ref-1042](../../references/ref-1042.md) — FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 2025-06-03)
- [ref-1034](../../references/ref-1034.md) — Open Robotics (ROS 2 Documentation), Iron Irwini (iron) (발행 2023-05-23)
- [ref-045](../../references/ref-045.md) — GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) (발행 2021-09-30)
- [ref-1025](../../references/ref-1025.md) — OpenAPI Initiative, OpenAPI Specification v3.1.0 (발행 2021-02-15)
- [ref-306](../../references/ref-306.md) — OASIS, MQTT Version 5.0 (발행 2019-03)
- [ref-303](../../references/ref-303.md) — NIST, NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model (발행 2018-03)
- [ref-937](../../references/ref-937.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H \| Changi General Hospital (발행 미확인)
- [ref-831](../../references/ref-831.md) — ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications) (발행 미확인)
- [ref-766](../../references/ref-766.md) — 국가법령정보센터(개인정보보호위원회 고시), 개인정보의 안전성 확보조치 기준 (발행 미확인)
- 그 밖에 25건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [K. 플랫폼 아키텍처·인프라](index.md) — '다른 대분류와의 연결' 절 신규 작성: 16개 대분류별 세부영역 연결(추정 연결 표시, 벤더 주장 6건 병기), 현장 유형별 사례, 아직 다루지 않은 세부영역 목록, 절 끝 각주 정의 44건. 2차 수정: L. AI·학습 기술 항목에 적용 대상 세부영역 링크, 약어 첫 등장 풀어 쓰기 (실행 2026-10-09-06)
- 2026-10-09 · 요약 · [K. 플랫폼 아키텍처·인프라](index.md) — K. 플랫폼 아키텍처·인프라: '다른 대분류와의 연결' 절 신규 작성(16개 대분류의 세부영역 연결, 조건부 승인 수정 18건과 2차 수정 5건 반영: f21 1 Hz 귀속 정정, f30 추정 강등) (실행 2026-10-09-06)
- 2026-09-30 · 갱신 · [43. 데이터·관측성·배포](data-observability-and-deployment.md) — 섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md) — 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,750자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md) — 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,115자)을 옮겼다 (실행 2026-09-30-06)
<!-- auto:category-recent:end -->
```

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "17. 작업 대상·자산 식별과 인계 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
area_no: {{area_no}}                        # 1~67 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [18, 29, 30]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개. 예: [EPCIS, 인계 확인, 자산 추적]. 시드면 []
status: {{status}}                          # seed | draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여. 시드면 이 줄을 뺀다
created: {{created}}                        # YYYY-MM-DD. 페이지를 처음 만든 날
updated: {{updated}}                        # YYYY-MM-DD. 마지막으로 내용을 바꾼 날
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id. 예: [ref-003, ref-021]. 없으면 []
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜 YYYY-MM-DD. 시드면 이 줄을 뺀다
version: {{version}}                        # 정수. 시드 1, 갱신마다 +1
---
<!--
[템플릿] 세부 연구영역 페이지 (type: area)
경로: docs/categories/<대분류 slug>/<영역 slug>.md  (아래 경로 규약 표. 2026-09-28 개정부터 폴더·파일 이름에 대분류 문자·영역 번호를 붙이지 않는다)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석, C. 채팅 기반 구성·운영의 엔진 짝 주석), 1절 아래 "이 영역이 다루는 일(2026-09-28 리스트업 기준)" 목록(data/area_items.json)과 옛 영역에서 이어받은 경우의 계보 안내(data/area_lineage.json)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/<트랙 slug>/index.md(예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition) 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 67페이지(예: docs/categories/robot-ontology/robot-capability-and-task-representation.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 로봇 온톨로지):
!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 67페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]

{{area_items_block}}
<!--
첫 내용 줄: 분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않는다. 원문 주석(현재 원문)은 이 절이 아니라 2절의 인용 블록에 둔다.
{{area_items_block}}: 시드가 넣은 위키 문구를 그대로 둔다(pipeline/scaffold.py area_items_block). (1) "이 영역이 다루는 일(2026-09-28 리스트업 기준):" 과 그 아래 "- **일 이름**: 정의" 목록(data/area_items.json), (2) 옛 영역에서 일부를 이어받은 영역이면 계보 안내 문장(data/area_lineage.json), (3) 옛 영역 본문을 이어받은 영역이면 옛 영역 안내 문장과 옛 정의·질문·주석 인용 블록("> 옛 정의: … [옛 분류원문]", "> 옛 질문: … [옛 분류원문]", "> 옛 원문 주석: … [옛 분류원문]"). 옛 인용 블록은 보관한 옛 원문(_source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)과 글자 단위로 같아야 하며(protect_source.py check_tagged_lines), 이력 기록이므로 에이전트가 고치거나 새 문장을 [옛 분류원문] 으로 태그하지 않는다. 해당 내용이 없는 영역은 이 자리 표시 줄을 지운다.
이 절의 원문 문장과 옛 원문 인용은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. 핵심 질문

{{core_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 세부영역 표의 "핵심 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]". 수정 금지. (대분류 페이지의 핵심 질문과 다른 문장이다. 소속 대분류의 핵심 질문은 H1 아래 admonition 에 둔다.)
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 해당 영역(2026-09-28 원문 기준): 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 36. 가상 시운전·실제 상황 재현, 38. 모니터링·이상 탐지·원인 분석, 55. 현장 조사·설치·시운전. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14~16번의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석("매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번"), C. 채팅 기반 구성·운영의 엔진 짝 주석("맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번").
굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다. 문단이 여럿인 영역(예: 14. 도면·BIM에서 지도 만들기는 셋, 15. 지도·공간·위치 모델과 25. 작업 배정 — MRTA는 둘)은 인용 블록도 원문 순서대로 그 수만큼 둔다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다. 정확한 목록은 pipeline/lib/source.py 의 area_notes(번호)가 정한다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 ROP를 구현·운영할 때 무엇이 막히는지, 로봇 개별 성능과 업무 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 핵심 질문에서 출발한다. 특정 현장 유형(예: 물류창고)에만 해당하는 이야기로 좁히지 말고, 현장 유형에 따라 달라지는 점이 있으면 어느 현장 유형인지 밝힌다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "VDA 5050(독일자동차산업협회 무인운반차 인터페이스)", "WMS(Warehouse Management System, 창고 관리 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** {{site_types}}
<!-- 이 사례가 놓이는 현장 유형을 분류 원문 21장의 일곱 가지(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 가운데 하나로 명시한다. 예: "병원". 물류창고는 일곱 현장 유형 가운데 하나일 뿐이므로 기본값으로 쓰지 않고, 브리프 근거가 있는 현장 유형을 고른다. 물류창고 사례라면 입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 중 어느 단계인지를 사례 제목이나 서술에 덧붙일 수 있다. -->

**사례:** {{case_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "병원에서 검체를 검사실로 운반", "제조 공장에서 공정 사이 부품 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
여섯 항목은 분류 원문 21장의 정의를 따른다. 시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가? / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가? / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가? / 제약: 시간·공간·적재량·설비·권한·안전 제약은 무엇인가? / 완료·인계: 무엇이 확인돼야 일이 끝났다고 인정하는가? / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?
표 아래에 1~3단락으로 사례를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 실제 도입 사례는 출처 각주와 함께 쓰고, 설명용 가상 사례이면 첫 문장에 밝힌다(예: "다음은 설명을 위한 가상의 사례이다."). 지어낸 현장 수치는 쓰지 않는다.
사례가 여럿이면 "**현장 유형:** … / **사례:** … / 여섯 항목 표 / 서술" 묶음을 사례마다 반복한다(서로 다른 현장 유형의 사례를 우선한다). 2026-09-28 개정 전에 쓴 물류창고 시나리오는 "현장 유형: 물류창고" 사례로 유지한다.
다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 함께 낸다(항목마다 site_type·item·link·title. 대분류는 퍼블리셔가 link 에서 정한다). 현장 유형 매트릭스 페이지: ../../site-matrix.md
-->

## 6. 대표 접근법과 기술

{{approaches}}
<!--
소제목(###)별로 접근법을 2~5개 정리한다. 각 접근법: 무엇을 해결하는가, 어떻게 동작하는가, 한계는 무엇인가. 주장마다 태그·각주.
벤더 제품의 기능·성능은 [추정]에 "벤더 주장"을 병기한다. 표·그림은 복제하지 않고 필요하면 mermaid 로 직접 그린다.
-->

## 7. 관련 표준·프레임워크·오픈소스

{{standards}}
<!--
표 형식: | 이름 | 유형(표준 / 오픈소스 / 평가 프로그램 / 프레임워크) | 이 영역과의 관계 | 출처 |. 각 행의 출처 칸에 각주.
표준·규격은 발행 기관의 공식 자료를 근거로 하고, 원문을 못 열었으면 "원문 미열람"을 표기한다. 대체·개정된 표준은 현재 버전을 확인해 기준일을 쓴다. 표준 목록 페이지(../../standards/index.md)와 용어집 링크를 함께 둔다.
-->

## 8. 대표 연구와 자료

{{key_research}}
<!--
목록 형식: "- 저자 또는 기관, 제목(연도) — 한두 문장 요약과 이 영역에서의 의미. [태그][^ref]". 3~8건. 학술 논문·표준·정부·연구기관 보고서를 우선하고 기사·벤더 문서는 보조로 둔다.
-->

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 현장 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 19장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장"(같은 대분류 E. 사물·사람·실시간 상태 안의 예). 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 L. AI·학습 기술의 해당 영역(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)을 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 영역이면 짝이 되는 엔진 영역(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 연결한다. 현장 유형별 요구·도입 사례는 Q. 현장 유형별 적용의 해당 영역(61. 물류창고 ~ 67. 기타 현장)을 연결한다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/<트랙 slug>/index.md. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/<트랙 slug>/question-backlog.md)로 링크만 둔다.
출처가 충돌한 주장, 확인하지 못한 수치, "분류 확장 제안"은 여기에 질문으로 올린다.
-->

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:area-recent:end -->
<!-- 퍼블리셔가 이 영역을 다룬 실행과 주제 페이지를 최신순으로 넣는다(날짜 | 실행 id | 변경 요약 | 페이지 링크). 스토리텔러는 마커 사이를 건드리지 않는다. -->

## 13. 참고 자료 (각주)

{{footnotes}}
<!--
각주 정의만 둔다. 형식: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"(공통 규칙 9). 본문에서 쓴 각주는 모두 여기에 정의하고, 정의만 있고 본문에 없는 각주는 지운다. 프런트매터 sources 와 일치시킨다.
시드 페이지는 2절 원문 주석의 [n] 에 대응하는 각주 정의만 둔다(없으면 "아직 작성되지 않음"). 각주 정의는 이 절에만 두고 [분류원문] 이 붙은 줄에는 붙이지 않는다.
-->
```

### templates/topic.md

```markdown
---
title: "{{title}}"                          # 주제 제목. 질문형 또는 명사구. 예: "로봇 도착과 작업 대상 인계 확인은 어떻게 다른가"
type: topic
category: "{{category}}"                    # 주 연구영역이 속한 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
primary_area_no: {{primary_area_no}}        # 주 연구영역 번호(1~67). 반드시 하나
track: {{track_slug}}                       # 트랙 실행에서 나온 주제 페이지만. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition. 아니면 이 줄을 뺀다
related_areas: [{{related_areas}}]          # 관련 영역 번호 0개 이상. 예: [18, 29]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개
status: {{status}}                          # draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜
version: {{version}}                        # 정수. 신규 1, 갱신마다 +1
---
<!--
[템플릿] 주제 페이지 (type: topic)
경로: docs/topics/YYYY/YYYY-MM-DD-slug.md  (YYYY-MM-DD 는 생성한 실행 날짜, slug 는 영문 소문자·하이픈)
쓰임: 파이프라인 2주기부터의 주제 조사 실행, 세부영역 페이지가 4,000자를 넘어 분리한 글, 트랙 실행에서 하나의 질문을 깊게 다룬 글. 하루 신규 주제 페이지 상한은 daily_budget.new_topic_pages 를 따른다.
필수: 주 연구영역 하나(primary_area_no)와 0개 이상의 관련 영역. 트랙 실행에서 나온 페이지는 프런트매터에 track 을 넣고, 해당 트랙 단계 페이지의 3절(조사 결과)에서 이 페이지를 링크한다.
분량: 1~7절 텍스트 합계(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외) 1,500~2,500자.
서사 골격: 왜 중요한가 → 현장에서 무슨 일이 벌어지는가(현장 유형을 밝힌 적용 사례) → 무엇이 알려져 있는가(검증된 사실) → ROP는 무엇을 맡고 무엇을 연계하는가 → 다른 영역과 어떻게 이어지는가 → 아직 모르는 것.
브리프의 발견 사항(finding)만 쓴다. 새 사실을 더하지 않는다. 필요한 사실이 브리프에 없으면 본문에 넣지 않고 pages.json 의 additional_research_requests 에 기록한다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 주제 목록은 ../index.md, 세부영역 페이지는 ../../categories/<대분류 slug>/<파일>, 대분류 페이지는 ../../categories/<대분류 slug>/index.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 트랙은 ../../tracks/<트랙 slug>/<파일>.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [주제](../index.md) › {{title}}

# {{title}}

**주 연구영역:** [{{primary_area_no}}. {{primary_area_name}}](../../categories/{{category_slug}}/{{area_file}}.md) · **관련 영역:** {{related_area_links_or_없음}} · **실행:** {{run_id}}
<!-- 관련 영역 링크는 "[18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)" 형식으로 쉼표 구분. 트랙 페이지면 "· **트랙:** [트랙 이름](../../tracks/<트랙 slug>/index.md) 단계 n" 을 덧붙인다(예: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)). -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 새 페이지에는 빈 마커 두 줄만 둔다. -->

## 1. 세 줄 요약

- {{summary_line_1}}
- {{summary_line_2}}
- {{summary_line_3}}
<!-- 정확히 세 줄. 각 줄은 한 문장. 첫 줄은 무엇을 밝혔는가, 둘째 줄은 ROP 운영에 무엇을 뜻하는가, 셋째 줄은 무엇이 아직 확인되지 않았는가. 요약에도 핵심 주장에는 태그를 붙인다. -->

## 2. 배경

{{background}}
<!--
어느 연구영역의 어떤 질문에서 출발했는지 쓴다. 주 연구영역의 원문 "핵심 질문"을 인용하면 그대로 옮기고 [분류원문] 을 붙인다. 출발점이 열린 질문(oq-NNN)이나 트랙 백로그 질문(q1-01), 정정 요청, priority.yaml 의 우선 주제이면 그 id 와 링크를 적는다. 1~2단락.
-->

## 3. 본문

### {{subheading_1}}

{{body_1}}

### {{subheading_2}}

{{body_2}}
<!--
소제목은 자유(2~5개). 주장마다 태그·각주. 검증된 발견 사항만 쓰고 순서는 서사 골격을 따른다. 출처가 충돌하면 둘 다 제시하고 7절 열린 질문에 올린다.
표·그림 복제 금지. 도식이 필요하면 mermaid 로 그리고 도식 안에서도 이름을 쓴다. 벤더 주장은 [추정]에 "벤더 주장" 병기. 조건부 승인의 수정 목록을 모두 반영하고 pages.json 의 fixes_applied 에 표시한다.
-->

## 4. 현장 시나리오

**현장 유형:** {{site_types}}

**사례:** {{case_title}}

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
절 제목 "4. 현장 시나리오"는 파이프라인(pipeline/lib/validate.py)이 쓰는 고정 문자열이므로 바꾸지 않는다. 내용은 분류 원문 21장의 방법대로 쓴다: 현장 유형(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 하나를 명시하고, 여섯 항목(시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가 / 수행 자원 / 제약 / 완료·인계 / 예외·성과)을 채운다. 물류창고는 일곱 현장 유형 가운데 하나이므로 기본값으로 쓰지 않는다. 이 주제와 직접 관련 없는 항목은 "해당 없음"으로 둔다. 실제 사례는 출처 각주와 함께, 설명용 가상 사례이면 첫 문장에 밝히고 지어낸 수치는 쓰지 않는다. 다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 낸다.
-->

## 5. ROP 관점의 시사점

**직접 범위:**
{{direct_scope_implications}}

**연계 범위:**
{{external_scope_implications}}
<!-- 분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 경계를 기준으로 ROP가 직접 맡는 것과 외부와 연계하는 것을 나누어 쓴다. 각 항목은 목록으로, 주장마다 태그·각주. 외부 연계 영역을 ROP 직접 범위처럼 쓰지 않는다. -->

## 6. 연결되는 연구영역

{{connected_areas}}
<!-- 목록 형식: "- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 연결 이유 한 문장". 주 연구영역을 첫 줄에, 관련 영역을 그 아래에. 번호와 이름을 함께 쓴다. 여기 적은 번호는 프런트매터 primary_area_no·related_areas 와 일치시킨다. AI를 다루면 27. AI·학습·적응과 모델 운영을 함께 연결한다. -->

## 7. 열린 질문

{{open_questions}}
<!-- 목록 형식: "- **oq-012** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 이 글에서 새로 생긴 질문과 답한(해결한) 질문을 나누어 적고, 해결한 질문에는 답이 있는 절을 표시한다. 트랙 질문(q1-01)은 트랙 백로그 링크만 둔다. pages.json 의 open_question_updates 로도 낸다. 없으면 "없음"과 이유. -->

## 8. 출처

{{footnotes}}
<!-- 각주 정의만 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". 본문의 각주와 프런트매터 sources 를 일치시킨다. 새 출처는 pages.json 의 reference_updates 로도 낸다. -->

## 9. 검증 노트

- 판정: 1차 {{first_verdict}} / 2차 {{second_verdict}}
- 확인·미확인: 확인 {{confirmed_count}}건 · 미확인 {{unconfirmed_count}}건 · 교차 확인 {{cross_checked_count}}건
- 강등된 주장: {{downgraded_claims_or_없음}}
- 검증자 주의: {{verification_note}}
- 신뢰도: {{confidence}}
<!-- 내용 검증 에이전트의 verification.json 에서 옮긴다. 판정 값: 1차 = 승인 | 조건부 승인 | 반려, 2차 = 통과 | 수정 후 재검증 | 불통과. 강등된 주장은 finding id 와 "사실 → 추정" 같은 변경을 적는다. "검증자 주의"는 verification_note 문구를 그대로 쓴다. 스토리텔러는 여기에 자기 의견을 넣지 않는다. -->

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| {{date}} | {{run_id}} | {{change_summary}} | {{version}} |
<!-- 신규 작성은 "신규 작성". 갱신마다 한 행을 위에 추가하고 프런트매터 version 을 올린다. 정정 요청을 반영했으면 corr-NNN id 를 적는다. -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 17건 / 전체 1324건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-304 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | https://arxiv.org/abs/2205.09778 | 2026-09-25 | 아니오 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | https://arxiv.org/abs/2512.15215 | 2026-09-25 | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 2026-09-25 | 예 |
| ref-774 | Mobile Industrial Robots(MiR) | MiR Fleet | 미확인 | https://mobile-industrial-robots.com/products/software/mir-fleet | 2026-09-25 | 아니오 |
| ref-870 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 | 2025-11-09 | https://www.irobotnews.com/news/articleView.html?idxno=43274 | 2026-09-29 | 예 |
| ref-937 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | ROMI-H | Changi General Hospital | 미확인 | https://www.cgh.com.sg/chart/projects/romi-h | 2026-09-29 | 예 |
| ref-1023 | NAVER Corp. | 로보틱스 l NAVER Corp. | 미확인 | https://www.navercorp.com/tech/robotics | 2026-09-30 | 예 |
| ref-1024 | AsyncAPI Initiative | AsyncAPI Specification 3.1.0 | 미확인 | https://www.asyncapi.com/docs/reference/specification/v3.1.0 | 2026-09-30 | 예 |
| ref-1025 | OpenAPI Initiative | OpenAPI Specification v3.1.0 | 2021-02-15 | https://spec.openapis.org/oas/v3.1.0 | 2026-09-30 | 예 |
| ref-1026 | 뉴스핌 | 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다 | 2026-05-13 | https://www.newspim.com/news/view/20260512001077 | 2026-09-30 | 예 |
| ref-1027 | Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv) | Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform | 2017-06 | https://arxiv.org/abs/1706.08931 | 2026-09-30 | 예 |
| ref-1028 | Open Robotics (open-rmf) | rmf_api_msgs — README | 미확인 | https://github.com/open-rmf/rmf_api_msgs | 2026-09-30 | 예 |
| ref-1029 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | https://developer.inorbit.ai/docs | 2026-09-30 | 예 |
| ref-1030 | Locus Robotics | Seamless Integrations with LocusOne Robotics | 미확인 | https://locusrobotics.com/locusone/automated-warehouse-software/integrations | 2026-09-30 | 예 |
| ref-1031 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 2024-12 | https://arxiv.org/abs/2412.05408 | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 377개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- asam-openscenario: 오픈시나리오 (ASAM OpenSCENARIO)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
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
- cloud-robotics: 클라우드 로보틱스 (Cloud Robotics)
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
- control-barrier-function: 제어 장벽 함수 (Control Barrier Function (CBF))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- decision-focused-learning: 결정 중심 학습 (Decision-Focused Learning)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- document-layout-analysis: 문서 레이아웃 분석 (Document Layout Analysis)
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- ethical-black-box: 윤리적 블랙박스 (Ethical Black Box (EBB))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- face-obfuscation: 얼굴 가림 (Face Obfuscation)
- failure-explanation: 실패 설명 (Failure Explanation)
- falsification: 반증 기반 시험 (Falsification)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- finops: 핀옵스 (FinOps)
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
- guidance-graph: 안내 그래프 (Guidance Graph)
- hallucination: 환각 (Hallucination)
- hardware-in-the-loop: 하드웨어 인 더 루프 (Hardware-in-the-Loop (HiL))
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- i-pass-handoff-program: I-PASS 인계 프로그램 (I-PASS Handoff Program)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
- indirect-prompt-injection: 간접 프롬프트 주입 (Indirect Prompt Injection)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
- integrity-risk: 무결성 위험 (Integrity Risk)
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
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- pseudonymisation: 가명처리 (Pseudonymisation)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- raw-video-regulatory-sandbox-exemption: 영상정보 원본 활용 규제샌드박스 실증특례 (Regulatory Sandbox Special Demonstration Exemption for Raw Video Use)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-attestation: 원격 증명 (Remote Attestation)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-ambiguity: 역할 모호성 (Role Ambiguity)
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- security-level-iec-62443: 보안 수준 (Security Level (SL, IEC 62443))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shift-handover: 교대 인수인계 (Shift Handover)
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- sim-vs-real-correlation-coefficient: 시뮬레이션–현실 상관 계수 (Sim-vs-Real Correlation Coefficient (SRCC))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
- software-in-the-loop: 소프트웨어 인 더 루프 (Software-in-the-Loop (SiL))
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- stakeholder-requirements-specification: 이해관계자 요구사항 명세 (Stakeholder Requirements Specification (StRS))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [41] 에 걸린 7건 / 전체 333건)

```markdown
- oq-206 [열림] 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? (영역 41, 42)
- oq-207 [열림] 로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가? (영역 41, 57)
- oq-208 [열림] 로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가? (영역 41, 29)
- oq-209 [열림] 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? (영역 41, 21)
- oq-267 [열림] ROP 같은 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독)를 비교하거나 공개한 자료가 있는가? (영역 3, 41)
- oq-300 [열림] 플랫폼 관제 서비스를 다중 클라우드 복제나 컨테이너 자동 재시작으로 운영하면서, 재시작 뒤 진행 중인 로봇 작업 상태를 잃지 않고 이어 간 공개 사례나 구성이 있는가? (영역 43, 41, 32)
- oq-301 [열림] 로봇 오케스트레이션 플랫폼의 외부 API 를 OpenAPI·AsyncAPI 로 기술해 연동 적합성 시험의 기준으로 쓴 공개 시험 도구나 절차가 있는가? (영역 41, 21)
```

### docs/standards/index.md (요약: 331개 — 이름 · 종류 · 발행 기관)

```markdown
- SCOR (SCOR Digital Standard) · 표준 · ASCM(Association for Supply Chain Management)
- ISA-95 (ANSI/ISA-95) · 표준 · ISA(International Society of Automation)
- GS1 EPCIS · 표준 · GS1
- Open-RMF · 오픈소스 · Open Robotics
- ROS 2 DDS-Security (ROS 2 DDS-Security Integration) · 프레임워크 · ROS 2 Design
- ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) · 프레임워크 · ROS 2 Design
- NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) · 평가 프로그램 · NIST(National Institute of Standards and Technology)
- ARIAC · 평가 프로그램 · NIST
- GS1 EPCIS 2.0 (ISO/IEC 19987:2024) · ISO/IEC · GS1 · 표준
- GS1 CBV (Core Business Vocabulary) · GS1 · 표준
- SSCC (Serial Shipping Container Code) · GS1 · 표준
- GS1 Logistic Label Guideline · GS1 · 표준
- GRAI (Global Returnable Asset Identifier) · GS1 · 표준
- GIAI (Global Individual Asset Identifier) · GS1 · 표준
- EPC Tag Data Standard (1.11판) · GS1 · 표준
- VDA 5050 (2.0.0) · VDA(Verband der Automobilindustrie) · 표준
- OpenEPCIS · OpenEPCIS · 오픈소스
- IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) · IEEE · 표준
- IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology · IEEE · 표준
- W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) · W3C / OGC · 표준
- VDA 5050 (3.0.0) · VDA(Verband der Automobilindustrie) · 표준
- MassRobotics AMR Interoperability Standard (1.0) · MassRobotics · 표준
- OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) · OPC Foundation / VDMA · 표준
- Information Model for Capabilities, Skills & Services (CSS) · Plattform Industrie 4.0 · 프레임워크
- Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) · Auto-ID Labs Korea(세종대학교) · 오픈소스
- RAWSim-O · Merschformann, M. (RAWSim-O GitHub) · 오픈소스
- 스마트물류센터 인증제 · 한국교통연구원(인증스마트물류센터) · 평가 프로그램
- BPMN 2.0 (ISO/IEC 19510:2013) · OMG(Object Management Group) · ISO/IEC · 표준
- IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 · IEC / ISO · 표준
- B2MML (Business To Manufacturing Markup Language, 판 0701) · MESA International · 표준
- OCEL 2.0 (Object-Centric Event Log) · arXiv:2403.01975 저자(미확인) · 표준
- ISO 22400-2:2014 제조 운영 관리 KPI 정의 · ISO · 표준
- WERC DC Measures · WERC(Warehousing Education and Research Council) · 평가 프로그램
- PM4Py · Process Intelligence Solutions · 오픈소스
- OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) · OPC Foundation / ISA · 표준
- osmAG-from-cad (CAD-to-osmAG 파이프라인) · Zhang, J. (jiajiezhang7 GitHub) · 오픈소스
- Ogm2Pgbm · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- ifc2indoorgml · Diakité, A. A. 외 · 오픈소스
- IDTA 02020 Capability Description 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- CaSkMan · CaSkade-Automation (GitHub) · 오픈소스
- SOMA (Socio-physical Model of Activities) · EASE CRC · 오픈소스
- IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) · Helmut Schmidt University, Institute of Automation Technology · 오픈소스
- ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 · ISO · 표준
- KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- VDMA LIF (Layout Interchange Format) · VDMA · 표준
- IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) · buildingSMART · 표준
- Nav2 Docking Framework (nav2_docking) · ROS Navigation (Open Navigation) · 오픈소스
- IDTA 02020 Capability Description (AAS 서브모델 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 · ISO · 표준
- KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- SkiROS2 · RVMI lab, Aalborg University · 오픈소스
- LIF (Layout Interchange Format) 1.0.0 · VDMA · 표준
- ISO 21423 Industrial mobile robots — Communications and interoperability · ISO · 표준
- IFC 4.3 (IfcSpace) · buildingSMART International · 표준
- OGC IndoorGML 2.0 · OGC · 표준
- ISO 19164:2024 Indoor feature model · ISO · 표준
- GS1 GLN (Global Location Number) · GS1 · 표준
- REP 105 Coordinate Frames for Mobile Platforms · ROS (ros-infrastructure/rep) · 프레임워크
- ROSA (ROS Agent) · NASA Jet Propulsion Laboratory · 오픈소스
- RAI · Robotec.ai · 오픈소스
- free_fleet (Open-RMF 플릿 어댑터) · Open Robotics (open-rmf) · 오픈소스
- ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) · InOrbit · 오픈소스
- Open-RMF fleet_adapter_template · Open Robotics (open-rmf) · 오픈소스
- SLAM Toolbox · Macenski, S. (SteveMacenski GitHub) · 오픈소스
- ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) · Open Robotics (ROS 2 Documentation) · 오픈소스
- Eclipse Sparkplug (Chapter 5 Operational Behavior) · Eclipse Foundation · 표준
- OPC UA Part 4: Services (7.11 DataValue) · OPC Foundation · 표준
- ISO 23247 제조 디지털 트윈 프레임워크 · ISO (NIST 해설 경유) · 표준
- ROS 2 설계 문서 — ROS on DDS · QoS 정책 · ROS 2 Design · 프레임워크
- rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) · ROS 2 (ros2/rmw_zenoh) · 오픈소스
- KubeEdge · KubeEdge (CNCF) · 오픈소스
- Open-RMF rmf-web (대시보드·API 서버) · Open Robotics (open-rmf) · 오픈소스
- MQTT Version 5.0 · OASIS · 표준
- NIST SP 500-325 Fog Computing Conceptual Model · NIST · 프레임워크
- KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 · 산업통상자원부 국가기술표준원 · 표준
- Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) · Open Robotics (open-rmf) · 오픈소스
- KnowRob (하이브리드 지식 베이스) · KnowRob (knowrob GitHub) · 오픈소스
- IEEE1872-owl (CORA 공개 OWL 번역, 제3자) · srfiorini (IEEE1872-owl GitHub) · 오픈소스
- CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) · OGC · 표준
- IMDF (Indoor Mapping Data Format) 1.0.0 · OGC / Apple · 표준
- BOT (Building Topology Ontology) 0.3.2 · W3C Linked Building Data Community Group · 프레임워크
- ifcOWL · buildingSMART · 표준
- Brick Schema · Brick Consortium · 오픈소스
- ISO 16739-1:2024 (IFC 4.3) · ISO · 표준
- Rasa 폼(Forms, Rasa 3.x) · Rasa Technologies · 오픈소스
- ROS 2 액션 설계(Actions) · ROS 2 Design · 프레임워크
- ROS 2 관리형 노드 수명주기(Managed nodes) · ROS 2 Design · 프레임워크
- Open-RMF rmf_task · Open Robotics (open-rmf) · 오픈소스
- IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) · IETF HTTPAPI Working Group · 표준
- OPC UA Part 10: Programs (v1.04) · OPC Foundation · 표준
- ISA-TR88.00.02 Machine and Unit States (PackML) · ISA · 표준
- BehaviorTree.CPP · BehaviorTree (GitHub) · 오픈소스
- OR-Tools CP-SAT (스케줄링 레시피) · Google · 오픈소스
- Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) · Open Robotics (open-rmf) · 오픈소스
- rmf_task (Open-RMF 작업 계획기 TaskPlanner) · Open Robotics (open-rmf) · 오픈소스
- ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 · ISO · 표준
- 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) · National Institute of Building Sciences · 표준
- KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 · 국가표준인증통합정보시스템(KSSN) · 표준
- 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) · 한국건설기술연구원(건설CALS 체계) · 표준
- ezdxf (DXF 읽기·쓰기 라이브러리) · Moitzi, M. (mozman/ezdxf GitHub) · 오픈소스
- ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) · ECLASS e.V. · 표준
- IEC 공통 데이터 사전(IEC CDD) · IEC · 표준
- rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF Traffic Editor · Open Robotics · 오픈소스
- MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) · DiligentPanda (Team Pikachu, GitHub) · 오픈소스
- SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface · SEMI · 표준
- ASTM F3499-21 A-UGV 도킹 성능 시험 방법 · ASTM International · 표준
- ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 · ANSI / A3 · 표준
- KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 · 국가표준인증통합정보시스템(KSSN) · 표준
- Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_reservation (실험적 예약 라이브러리) · Open Robotics (open-rmf) · 오픈소스
- ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 · ISO · 표준
- ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) · ISO (A3 해설 경유) · 표준
- ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 · A3(Association for Advancing Automation) · 표준
- 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 · 고용노동부·한국산업안전보건공단 · 프레임워크
- 이동식 협동로봇 안전기준 KS(표준 번호 미확인) · 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) · 표준
- Open-RMF rmf_demos · Open Robotics (open-rmf) · 오픈소스
- IEC 61360-7:2024 교차 도메인 개념 데이터 사전(General items) · IEC · 표준
- IDTA 02003 Generic Frame for Technical Data for Industrial Equipment in Manufacturing (1.2) · IDTA(Industrial Digital Twin Association) · 표준
- Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- ROS 2 diagnostics · ROS (ros/diagnostics GitHub) · 오픈소스
- ros2_tracing · ROS 2 (ros2/ros2_tracing GitHub) · 오픈소스
- OpenTelemetry Specification · OpenTelemetry (CNCF) · 오픈소스
- Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 경보 메시지(rmf_task_msgs Alert) · Open Robotics (open-rmf) · 오픈소스
- IFCtoLBD (IFC → 링크드 빌딩 데이터 변환기, 판 2.54.0) · Oraskari, J. (jyrkioraskari GitHub) · 오픈소스
- SHACL (Shapes Constraint Language) · W3C · 표준
- IDS (Information Delivery Specification) · buildingSMART · 표준
- RMF Site Editor (rmf_site) · Open Robotics (open-rmf) · 오픈소스
- ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도) · ISO · 표준
- 기업재난관리표준·재해경감 우수기업 인증제 · 행정안전부 · 평가 프로그램
- 중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022) · 고용노동부 · 프레임워크
- 보상 트랜잭션 패턴(Compensating Transaction pattern) · Microsoft (Azure Architecture Center) · 프레임워크
- Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle) · Open Robotics (open-rmf) · 오픈소스
- IEEE 1872.1-2024 Standard for Robot Task Representation · IEEE Standards Association · 표준
- Serverless Workflow (Open Workflow Specification) DSL · CNCF Serverless Workflow · 오픈소스
- HDDL (Hierarchical Domain Definition Language) · Höller 외(IPC 2020 계층 계획 부문) · 프레임워크
- FaMe (BPMN 기반 다중 로봇 시스템 개발 틀) · Pettinari, S. (UNICAM PROS) · 오픈소스
- ISO 20607:2019 기계 안전 — 설명서 일반 작성 원칙 · ISO · 표준
- IEC/IEEE 82079-1:2019 제품 사용 정보 작성 — Part 1: 원칙과 일반 요구사항 · IEC / IEEE / ISO · 표준
- OmniDocBench (PDF 문서 파싱 벤치마크) · OpenDataLab · 오픈소스
- ISO 23247-6:2026 제조 디지털 트윈 프레임워크 — 제6부: 디지털 트윈 결합 · ISO · 표준
- KS X ISO 23247 제조를 위한 디지털 트윈 프레임워크(제1부 개요 및 일반 원리 등) · 국가표준인증종합정보센터(KSSN) · 표준
- Open-RMF rmf_simulation (시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- OFacT (Open Factory Twin) · OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) · 오픈소스
- League of Robot Runners · League of Robot Runners (Amazon Robotics 후원) · 평가 프로그램
- ASTM F45 위원회(무인 자동 유도 산업 차량) · ASTM International (NIST 참여) · 표준
- KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력 · 국가표준인증종합정보센터(KSSN) · 표준
- 한국로봇산업진흥원 로봇 시험평가 · 한국로봇산업진흥원(KIRIA) · 평가 프로그램
- ros2_fault_injection · reeceholland (GitHub) · 오픈소스
- ROSMonitoring · University of Liverpool Autonomy and Verification · 오픈소스
- LSMART (Lifelong Scalable Multi-Agent Realistic Testbed) · Yan, J. 외(arXiv 2602.15721) · 오픈소스
- IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 17359:2018 기계 상태 감시·진단 일반 지침 · ISO · 표준
- ISO 55000:2024 자산 관리 — 용어·개요·원칙 · ISO (ISO/TC 251) · 표준
- IEC TR 62443-2-3:2015 IACS 환경의 패치 관리 · IEC · 표준
- REP 2000 ROS 2 Releases and Target Platforms · Open Robotics (ROS REP) · 프레임워크
- rmf_simulation (Open-RMF 시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- 협동로봇 설치 작업장 안전인증 · 한국로봇사용자협회 · 평가 프로그램
- ISO 12100:2010 기계 안전 — 설계 일반 원칙 — 위험성평가와 위험 감소 · ISO (CEN EN ISO 12100:2010) · 표준
- KS B ISO/TS 15066 로봇 및 로봇 장치 — 협동로봇 · 국가기술표준원(KSSN) · 표준
- Nav2 Route Server (nav2_route) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- NIST SP 800-82 Rev. 3 Guide to Operational Technology (OT) Security · NIST · 프레임워크
- Eclipse Mosquitto (MQTT 브로커, mosquitto.conf ACL·인증서 인증) · Eclipse Foundation · 오픈소스
- SROS 2 접근 제어 정책(ROS 2 Access Control Policies) · ROS 2 Design · 프레임워크
- ROS 2 보안 인클레이브(ROS 2 Security Enclaves) · ROS 2 Design · 프레임워크
- KISA 로봇 보안취약점 점검 체크리스트 해설서 · 한국인터넷진흥원(KISA) · 프레임워크
- NIST AI RMF 1.0 (NIST AI 100-1) · NIST · 프레임워크
- ISO/IEC 42001:2023 AI 관리 시스템 · ISO/IEC · 표준
- ISO/IEC 23894:2023 AI 위험관리 지침 · ISO/IEC · 표준
- MLflow 모델 레지스트리 · MLflow (Linux Foundation 오픈소스 프로젝트) · 오픈소스
- LoTa-Bench · lbaa2022 (LoTa-Bench 공식 저장소) · 오픈소스
- AmbiK 데이터셋 · cog-model (AmbiK 저자) · 오픈소스
- SISO CMSD (Core Manufacturing Simulation Data, SISO-STD-008-2010·SISO-STD-008-01-2012) · SISO(Simulation Interoperability Standards Organization) · 표준
- SLAPStack (블록 적재 창고 저장 위치 배정 시뮬레이션) · Rinciog, A. 외 (malerinc/slapstack GitHub) · 오픈소스
- Semantic Versioning 2.0.0 · Semantic Versioning (semver.org) · 프레임워크
- IETF RFC 9745 The Deprecation HTTP Response Header Field · IETF · 표준
- IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준 · IEC · 표준
- ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항 · ISO/IEC · 표준
- KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 · 한국지능형로봇표준포럼(KOROS) · 표준
- OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증) · OPC Foundation · 평가 프로그램
- Nav2 costmap_2d (비용 지도·비용 지도 필터: 금지 구역·속도 제한) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- SLAM2REF (라이다 데이터의 기준 지도 다중 세션 정렬 도구) · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- Open-RMF rmf_task_ros2 디스패처·입찰 경매자(평가기) · Open Robotics (open-rmf) · 오픈소스
- Rasa 폴백·사람 인계(Fallback and Human Handoff, Rasa 3.x) · Rasa Technologies · 오픈소스
- nudged (2D 유사 변환 추정 라이브러리) · Palonen, A. (axelpale/nudged GitHub) · 오픈소스
- Rasa CALM 대화 복구 패턴(rasa-calm-demo patterns.yml) · Rasa Technologies · 오픈소스
- IfcDiff (IfcOpenShell IFC 모델 비교 도구, v0.8.0 문서) · IfcOpenShell · 오픈소스
- BS EN ISO 19650 Guidance Part C: 공통 데이터 환경(Edition 1) · UK BIM Framework · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency) · OWASP · 프레임워크
- Model Context Protocol 명세 2025-06-18 (Server Features: Tools) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- LangChain Human-in-the-loop 미들웨어 · LangChain · 오픈소스
- ISO 18646-2:2024 서비스 로봇 성능 기준과 시험 방법 — Part 2: 주행 · ISO · 표준
- ASTM F3244 Standard Test Method for Navigation: Defined Area · ASTM International · 표준
- SSIG (평면도 구조 유사도 지표) · van Engelenburg, C. 외 (caspervanengelenburg GitHub) · 오픈소스
- SLABIM (SLAM–BIM 결합 데이터셋) · HKUST Aerial Robotics Group · 오픈소스
- vda5050-sim (VDA 5050 가상 로봇 플릿 시뮬레이터) · gpue (vda5050-sim GitHub, 개인 저장소) · 오픈소스
- vda-5050-lib.js (가상 AGV 어댑터 포함 VDA 5050 라이브러리) · coatyio · 오픈소스
- τ-bench (도구–에이전트–사용자 상호작용 벤치마크) · sierra-research · 평가 프로그램
- SafeAgentBench (LLM 체화 에이전트 안전 계획 벤치마크) · SafeAgentBench 저자(shengyin1224 공식 저장소) · 평가 프로그램
- JSON Schema Validation (json-schema-spec, main 브랜치 차기판 초안) · JSON Schema (json-schema-org) · 표준
- VAL (PDDL 계획 검증 도구) · KCL-Planning · 오픈소스
- JSONSchemaBench · guidance-ai · 오픈소스
- Model Context Protocol 명세 2025-06-18 (Basic: Authorization) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- NIST SP 800-162 속성 기반 접근 통제(ABAC) 정의와 고려 사항 · NIST · 프레임워크
- RobotFleet (LLM·MILP 작업 배정기를 둔 중앙 다중 로봇 계획 틀) · therohangupta (RobotFleet 공식 저장소) · 오픈소스
- rosbag2 · ROS 2 (ros2/rosbag2 GitHub) · 오픈소스
- Simod (로그 기반 업무 프로세스 시뮬레이션 모델 자동 발견 도구) · Camargo, M., Dumas, M., & González-Rojas, O. · 오픈소스
- Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 구성(compose 범주)과 단계 API(ros2multirobotbook task_new) · Open Robotics · 오픈소스
- VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개) · Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) · 오픈소스
- EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) · 개인정보보호위원회 · 프레임워크
- 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 · 과학기술정보통신부·한국정보통신기술협회(TTA) · 프레임워크
- Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크) · Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- langbar (다중 모달 GUI–MCP 아키텍처 참조 구현) · van Dam, H. G. W. · 오픈소스
- IDTA 02006 Digital Nameplate for Industrial Equipment (3.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA-01002 Asset Administration Shell Specification — API (3.2.0) · IDTA(Industrial Digital Twin Association) · 표준
- RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 평가 프로그램
- CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현) · CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) · 오픈소스
- OWL 2 Web Ontology Language Structural Specification (Second Edition) · W3C · 표준
- IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙 · IDTA(Industrial Digital Twin Association) · 표준
- KGCL (Knowledge Graph Change Language) · Hegde, H. 외 (Database, Oxford) · 프레임워크
- ISO 13482 (서비스 로봇 안전 요구사항) · ISO · 표준
- RoMi-H (Robotic Middleware for Healthcare) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 오픈소스
- 서비스로봇 실증사업 · 한국로봇산업진흥원 · 평가 프로그램
- 스마트병원 선도모델(9개 모듈) · 한국보건산업진흥원 스마트병원 확산지원센터 · 프레임워크
- 로봇 친화형 건축물 인증 · 스마트도시협회 · 평가 프로그램
- Matter 1.2 (로봇청소기 장치 유형 포함) · Connectivity Standards Alliance (CSA) · 표준
- 실외이동로봇 운행안전인증 (지능형로봇법 제40조의2) · 한국로봇산업진흥원 · 평가 프로그램
- ISO/TR 4448-1:2024 Public-area mobile robots (PMR) — Part 1: Overview of paradigm · ISO (ISO/TC 204) · 표준
- ISO 4448 시리즈 (Public-area mobile robots, Part 6·9·16 개발 중) · ISO/TC 204 · 표준
- Nav2 GPS 항법 구성 (navsat_transform·두 EKF 융합·rolling 전역 비용 지도) · Open Navigation (Nav2) · 오픈소스
- SiLA 2 (Standardization in Lab Automation 2) · SiLA Consortium · 표준
- ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역 · ISO · 표준
- SS 713 Data Exchange Between Robots, Lifts and Automated Doorways · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- TR 130 Interoperability Between Robots and Central Command Systems · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- IEEE 1873-2015 Robot Map Data Representation for Navigation · IEEE Standards Association (IEEE RAS) · 표준
- osmAG (OSM 형식 계층형 위상·거리 의미 지도) · Feng, D. 외 (arXiv) · 프레임워크
- Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) · Open Robotics (open-rmf) · 오픈소스
- OpenAPI Specification 3.1.0 · OpenAPI Initiative · 표준
- AsyncAPI Specification 3.1.0 · AsyncAPI Initiative · 표준
- FogROS2 (클라우드·포그 로보틱스 플랫폼) · Ichnowski, J., Chen, K., Dharmarajan, K. 외 · 오픈소스
- MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) · Foxglove (ROS 2 채택: Open Robotics) · 오픈소스
- OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 · OpenTelemetry (CNCF) · 오픈소스
- ros-opentelemetry · szobov (GitHub, 개인 저장소) · 오픈소스
- Mender (OTA 업데이트 관리자) · Northern.tech (mendersoftware) · 오픈소스
- FinOps 프레임워크 (FinOps Phases) · FinOps Foundation · 프레임워크
- FOCUS 1.2 (FinOps 청구 데이터 명세) · FinOps Foundation · 표준
- Open X-Embodiment 데이터셋·RT-X 모델 · Open X-Embodiment Collaboration · 오픈소스
- OpenVLA · Kim, M. J., Pertsch, K., Karamcheti, S. 외 · 오픈소스
- GR00T N1 · NVIDIA · 오픈소스
- POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) · Skrynnik, A. 외 (ICLR 2025) · 평가 프로그램
- ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 · ISO (ISO/TC 108) · 표준
- Docling (AI 기반 문서 변환 오픈소스 도구) · IBM Research · 오픈소스
- LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리) · Google (google/langextract) · 오픈소스
- AECV-Bench (건축·엔지니어링 도면 이해 벤치마크) · Kondratenko, A. 외 (arXiv 2601.04819) · 평가 프로그램
- FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋) · Fan, Z. 외 (arXiv 2105.07147) · 평가 프로그램
- Nav2 Collision Monitor (nav2_collision_monitor) · Open Navigation (ros-navigation/navigation2) · 오픈소스
- ASAM OpenSCENARIO XML (1.4.0) · ASAM e.V. · 표준
- SDFormat (Simulation Description Format) · Open Source Robotics Foundation · 오픈소스
- BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) · Stanford 등 (Li, C. 외) · 평가 프로그램
- Moving AI MAPF 벤치마크 · Moving AI Lab (Sturtevant 외) · 평가 프로그램
- Arena-Bench · Kästner, L. 외 (RA-L 2022) · 평가 프로그램
- ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) · ISA(International Society of Automation) · 표준
- Open-RMF rmf_visualization · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) · Open Robotics (open-rmf) · 오픈소스
- IEC 62559 사용 사례 방법론 (Part 1~4) · IEC · 표준
- ISO/IEC/IEEE 29148:2018 요구공학 · ISO / IEC / IEEE · 표준
- 로봇활용 표준공정모델 · 산업통상자원부 · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) · OWASP GenAI Security Project · 프레임워크
- EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) · European Union (IES 해설 경유) · 프레임워크
- KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 · 과학기술정보통신부·한국인터넷진흥원(KISA) · 프레임워크
- 윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard) · Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) · 프레임워크
- VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) · VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) · 표준
- NASA-STD-7009B Standard for Models and Simulations · NASA · 표준
- 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) · 개인정보보호위원회 · 프레임워크
- 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) · 개인정보보호위원회 · 프레임워크
- 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) · 개인정보보호위원회 · 프레임워크
- 영상정보 원본 활용 규제샌드박스 실증특례 · 개인정보보호위원회 · 프레임워크
- EDPB Guidelines 3/2019 on processing of personal data through video devices · European Data Protection Board (EDPB) · 프레임워크
- EgoBlur · Meta Reality Labs · 오픈소스
- ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 · ANSI / A3(Association for Advancing Automation) · 표준
- HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications · UK Health and Safety Executive (HSE) · 프레임워크
- IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 · IEC(International Electrotechnical Commission) · 표준
- REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) · ROS (ros-infrastructure/rep) · 프레임워크
- HuNavSim (ROS 2 사람 보행 시뮬레이터) · Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. · 오픈소스
- Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) · Open Robotics · 오픈소스
- 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) · Francis, A. 외 · 프레임워크
- BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크) · BSRIA · 프레임워크
- 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 · 법제처(법령해석 법제처-23-0872 경유) · 프레임워크
- EU 데이터법 (Regulation (EU) 2023/2854, Data Act) · European Union (European Commission 해설) · 프레임워크
- EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안 · European Commission · 프레임워크
- 산업데이터 계약 가이드라인 · 산업통상부 · 프레임워크
- Kubernetes Deprecation Policy (API 폐기 정책) · The Kubernetes Authors · 오픈소스
- ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념 · ISO/IEC (JTC 1) · 표준
- IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항 · IEC · 표준
- EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무) · European Union (Future of Life Institute 비공식 게재본 경유) · 프레임워크
- 21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적) · U.S. Food and Drug Administration · 프레임워크
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
- ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries) · ISA(International Society of Automation) · 표준
- IDTA 02005 Provision of Simulation Models (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- autoware_rosbag2_anonymizer · Autoware Foundation · 오픈소스
- Gazebo Fuel Tools (gz-fuel-tools) · Open Robotics · 오픈소스
- ISO/AWI 26159-2 로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항 (초안) · ISO (ISO/TC 299 Robotics) · 표준
- ISO/CD TS 8100-11 승강기와 다른 시스템의 상호운용 (위원회 초안) · ISO (ISO/TC 178 Lifts, escalators and moving walks) · 표준
- 싱가포르 Technical Reference 93 (TR 93) 로봇–건물 설비 데이터 교환 · 싱가포르 (CGH 보도자료 기준, 발행 기관명 미확인) · 표준
- Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_obstacle (사람 검출·lane_blocker) · Open Robotics (open-rmf) · 오픈소스
- Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리) · Pasch, F. 외 (Intel Labs 외) · 오픈소스
- RoboVAST (출처 기록 기반 시뮬레이션 시험 틀) · Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. · 프레임워크
- ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열 · ISO · 표준
- IEEE 7001-2021 자율 시스템 투명성 표준 · IEEE Standards Association · 표준
```

### runs/2026-10-09-17/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/simulator.md
about/what-is-rop.md
categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md
categories/ai-and-learning/document-drawing-and-scene-understanding.md
categories/ai-and-learning/index.md
categories/ai-and-learning/prediction-and-learning-based-optimization.md
categories/ai-and-learning/robot-foundation-models-and-llm-planning.md
categories/chat-based-configuration-and-operation/chat-map-authoring.md
categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md
categories/chat-based-configuration-and-operation/chat-robot-configuration.md
categories/chat-based-configuration-and-operation/chat-scenario-composition.md
categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md
categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md
categories/chat-based-configuration-and-operation/index.md
categories/design-and-simulation/capacity-sizing-and-layout-design.md
categories/design-and-simulation/index.md
categories/design-and-simulation/scenario-model-and-editing.md
categories/design-and-simulation/simulation-and-predictive-digital-twin.md
categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md
categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md
categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md
categories/execution-collaboration-and-recovery/human-robot-collaboration.md
categories/execution-collaboration-and-recovery/index.md
categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md
categories/field-operations-and-monitoring/control-screen-and-execution-records.md
categories/field-operations-and-monitoring/index.md
categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md
categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md
categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md
categories/governance-law-and-society/index.md
categories/governance-law-and-society/labor-acceptance-and-accessibility.md
categories/governance-law-and-society/law-regulation-insurance-and-licensing.md
categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md
categories/integration/business-system-integration.md
categories/integration/facility-and-building-system-integration.md
categories/integration/index.md
categories/integration/interoperability-standards-and-conformance.md
categories/integration/robot-and-vendor-fleet-manager-integration.md
categories/objects-people-and-live-state/index.md
categories/objects-people-and-live-state/people-and-pedestrian-model.md
categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md
categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md
categories/planning-and-business/economics-procurement-and-business-models.md
categories/planning-and-business/index.md
categories/planning-and-business/technology-market-and-vendor-trends.md
categories/planning-and-business/use-cases-requirements-and-scope.md
categories/planning-and-optimization/index.md
categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md
categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md
categories/planning-and-optimization/task-allocation-mrta.md
categories/planning-and-optimization/task-and-workflow-modeling.md
categories/planning-and-optimization/task-sequencing-and-scheduling.md
categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md
categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md
categories/platform-architecture-and-infrastructure/index.md
categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md
categories/robot-ontology/heterogeneous-robot-registration.md
categories/robot-ontology/index.md
categories/robot-ontology/ontology-based-system-and-robot-integration.md
categories/robot-ontology/ontology-verification-and-change-management.md
categories/robot-ontology/robot-capability-and-task-representation.md
categories/safety/human-proximity-safety.md
categories/safety/index.md
categories/safety/safety-and-risk-management.md
categories/safety/safety-standards-certification-and-incident-investigation.md
categories/security-and-privacy/authentication-authorization-and-isolation.md
categories/security-and-privacy/communication-protection-threat-management-and-audit.md
categories/security-and-privacy/index.md
categories/security-and-privacy/privacy-and-video-data.md
categories/site-type-applications/commercial-facilities.md
categories/site-type-applications/home-and-apartment.md
categories/site-type-applications/hospital-and-healthcare.md
categories/site-type-applications/index.md
categories/site-type-applications/manufacturing-plant.md
categories/site-type-applications/other-sites.md
categories/site-type-applications/outdoor.md
categories/site-type-applications/warehouse.md
categories/space-and-map-model/index.md
categories/space-and-map-model/map-space-and-location-model.md
categories/space-and-map-model/maps-from-floor-plans-and-bim.md
categories/space-and-map-model/place-semantics-and-map-management.md
categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md
categories/verification-deployment-and-lifecycle/index.md
categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md
categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md
categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md
changelog.md
corrections.md
glossary/3d-scene-graph.md
glossary/4d-scene-graph.md
glossary/a-b-update.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/abstract-and-concrete-scenario.md
glossary/action-dependency-graph.md
glossary/actively-exploited-vulnerability.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alarm-management.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/as-planned-vs-as-built-deviation.md
glossary/asam-openscenario.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/asyncapi-specification.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-recording-of-events.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/average-displacement-error.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-description-submodel.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/cell-based-production.md
glossary/clarification-question.md
glossary/cloud-robotics.md
glossary/coalition-formation.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/common-coordinate-system.md
glossary/common-data-environment.md
glossary/compensating-transaction.md
glossary/competency-question.md
glossary/condition-based-maintenance.md
glossary/configuration-copilot.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/confused-deputy.md
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/control-barrier-function.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-embodiment-learning.md
glossary/cross-schedule-dependency.md
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
glossary/data-provenance.md
glossary/dds-security.md
glossary/deadlock.md
glossary/decision-focused-learning.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/document-layout-analysis.md
glossary/door-to-door-robot-delivery.md
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/ethical-black-box.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explainable-mapf.md
glossary/explicit-implicit-confirmation.md
glossary/face-obfuscation.md
glossary/failure-explanation.md
glossary/falsification.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/finops.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/giai.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hardware-in-the-loop.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/hmi-philosophy.md
glossary/human-in-the-loop.md
glossary/human-motion-trajectory-prediction.md
glossary/hungarian-method.md
glossary/i-pass-handoff-program.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indirect-prompt-injection.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
glossary/integrity-risk.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/irreducible-infeasible-subset.md
glossary/isa-95.md
glossary/it-ot-convergence.md
glossary/jailbreak.md
glossary/job-shop-scheduling-problem.md
glossary/joint-goal-accuracy.md
glossary/json-schema.md
glossary/keystroke-level-model.md
glossary/kiosk-accessibility.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/lease-expiry.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/localization-score.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/managed-node.md
glossary/management-of-change.md
glossary/map-alignment.md
glossary/map-distribution.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt-last-will.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/online-simulation.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry-genai-semantic-conventions.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pay-per-pick.md
glossary/payback-period.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/persistence-filter.md
glossary/personal-delivery-device.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/precision-time-protocol.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/pseudonymisation.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/raw-video-regulatory-sandbox-exemption.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-attestation.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-standard-process-model.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-ambiguity.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-tracing.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/safety-guardrail.md
glossary/safety-state-report.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/security-level-iec-62443.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shift-handover.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/sim-vs-real-correlation-coefficient.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-awareness.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/slot-filling.md
glossary/slotcar.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
glossary/software-in-the-loop.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/stakeholder-requirements-specification.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/strict-schema.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/surrogate-model.md
glossary/synchronization-loss.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
glossary/wireless-safety-rated-emergency-stop.md
glossary/workflow-net.md
glossary/zone-set.md
glossary/zones-and-conduits.md
ideas/chat-based-configuration-and-operation.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/daily/2026-09-26.md
logs/daily/2026-09-29.md
logs/daily/2026-09-30.md
logs/daily/2026-10-09.md
logs/index.md
logs/weekly/2026-W39.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-046.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-1000.md
references/ref-1001.md
references/ref-1002.md
references/ref-1003.md
references/ref-1004.md
references/ref-1005.md
references/ref-1006.md
references/ref-1007.md
references/ref-1008.md
references/ref-1009.md
references/ref-101.md
references/ref-1010.md
references/ref-1011.md
references/ref-1012.md
references/ref-1013.md
references/ref-1014.md
references/ref-1015.md
references/ref-1016.md
references/ref-1017.md
references/ref-1018.md
references/ref-1019.md
references/ref-102.md
references/ref-1020.md
references/ref-1021.md
references/ref-1022.md
references/ref-1023.md
references/ref-1024.md
references/ref-1025.md
references/ref-1026.md
references/ref-1027.md
references/ref-1028.md
references/ref-1029.md
references/ref-103.md
references/ref-1030.md
references/ref-1031.md
references/ref-1032.md
references/ref-1033.md
references/ref-1034.md
references/ref-1035.md
references/ref-1036.md
references/ref-1037.md
references/ref-1038.md
references/ref-1039.md
references/ref-104.md
references/ref-1040.md
references/ref-1041.md
references/ref-1042.md
references/ref-1043.md
references/ref-1044.md
references/ref-1045.md
references/ref-1046.md
references/ref-1047.md
references/ref-1048.md
references/ref-1049.md
references/ref-105.md
references/ref-1050.md
references/ref-1051.md
references/ref-1052.md
references/ref-1053.md
references/ref-1054.md
references/ref-1055.md
references/ref-1056.md
references/ref-1057.md
references/ref-1058.md
references/ref-1059.md
references/ref-106.md
references/ref-1060.md
references/ref-1061.md
references/ref-1062.md
references/ref-1063.md
references/ref-1064.md
references/ref-1065.md
references/ref-1066.md
references/ref-1067.md
references/ref-1068.md
references/ref-1069.md
references/ref-107.md
references/ref-1070.md
references/ref-1071.md
references/ref-1072.md
references/ref-1073.md
references/ref-1074.md
references/ref-1075.md
references/ref-1076.md
references/ref-1077.md
references/ref-1078.md
references/ref-1079.md
references/ref-108.md
references/ref-1080.md
references/ref-1081.md
references/ref-1082.md
references/ref-1083.md
references/ref-1084.md
references/ref-1085.md
references/ref-1086.md
references/ref-1087.md
references/ref-1088.md
references/ref-1089.md
references/ref-109.md
references/ref-1090.md
references/ref-1091.md
references/ref-1092.md
references/ref-1093.md
references/ref-1094.md
references/ref-1095.md
references/ref-1096.md
references/ref-1097.md
references/ref-1098.md
references/ref-1099.md
references/ref-110.md
references/ref-1100.md
references/ref-1101.md
references/ref-1102.md
references/ref-1103.md
references/ref-1104.md
references/ref-1105.md
references/ref-1106.md
references/ref-1107.md
references/ref-1108.md
references/ref-1109.md
references/ref-111.md
references/ref-1110.md
references/ref-1111.md
references/ref-1112.md
references/ref-1113.md
references/ref-1114.md
references/ref-1115.md
references/ref-1116.md
references/ref-1117.md
references/ref-1118.md
references/ref-1119.md
references/ref-112.md
references/ref-1120.md
references/ref-1121.md
references/ref-1122.md
references/ref-1123.md
references/ref-1124.md
references/ref-1125.md
references/ref-1126.md
references/ref-1127.md
references/ref-1128.md
references/ref-1129.md
references/ref-113.md
references/ref-1130.md
references/ref-1131.md
references/ref-1132.md
references/ref-1133.md
references/ref-1134.md
references/ref-1135.md
references/ref-1136.md
references/ref-1137.md
references/ref-1138.md
references/ref-1139.md
references/ref-114.md
references/ref-1140.md
references/ref-1141.md
references/ref-1142.md
references/ref-1143.md
references/ref-1144.md
references/ref-1145.md
references/ref-1146.md
references/ref-1147.md
references/ref-1148.md
references/ref-1149.md
references/ref-115.md
references/ref-1150.md
references/ref-1151.md
references/ref-1152.md
references/ref-1153.md
references/ref-1154.md
references/ref-1155.md
references/ref-1156.md
references/ref-1157.md
references/ref-1158.md
references/ref-1159.md
references/ref-116.md
references/ref-1160.md
references/ref-1161.md
references/ref-1162.md
references/ref-1163.md
references/ref-1164.md
references/ref-1165.md
references/ref-1166.md
references/ref-1167.md
references/ref-1168.md
references/ref-1169.md
references/ref-117.md
references/ref-1170.md
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
references/ref-1195.md
references/ref-1196.md
references/ref-1197.md
references/ref-1198.md
references/ref-1199.md
references/ref-120.md
references/ref-1200.md
references/ref-1201.md
references/ref-1202.md
references/ref-1203.md
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
references/ref-1239.md
references/ref-124.md
references/ref-1240.md
references/ref-1241.md
references/ref-1242.md
references/ref-1243.md
references/ref-1244.md
references/ref-1245.md
references/ref-1246.md
references/ref-1247.md
references/ref-1248.md
references/ref-1249.md
references/ref-125.md
references/ref-1250.md
references/ref-1251.md
references/ref-1252.md
references/ref-1253.md
references/ref-1254.md
references/ref-1255.md
references/ref-1256.md
references/ref-1257.md
references/ref-1258.md
references/ref-1259.md
references/ref-126.md
references/ref-1260.md
references/ref-1261.md
references/ref-1262.md
references/ref-1263.md
references/ref-1264.md
references/ref-1265.md
references/ref-1266.md
references/ref-1267.md
references/ref-1268.md
references/ref-1269.md
references/ref-127.md
references/ref-1270.md
references/ref-1271.md
references/ref-1272.md
references/ref-1273.md
references/ref-1274.md
references/ref-1275.md
references/ref-1276.md
references/ref-1277.md
references/ref-1278.md
references/ref-1279.md
references/ref-128.md
references/ref-1280.md
references/ref-1281.md
references/ref-1282.md
references/ref-1283.md
references/ref-1284.md
references/ref-1285.md
references/ref-1286.md
references/ref-1287.md
references/ref-1288.md
references/ref-1289.md
references/ref-129.md
references/ref-1290.md
references/ref-1291.md
references/ref-1292.md
references/ref-1293.md
references/ref-1294.md
references/ref-1295.md
references/ref-1296.md
references/ref-1297.md
references/ref-1298.md
references/ref-1299.md
references/ref-130.md
references/ref-1300.md
references/ref-1301.md
references/ref-1302.md
references/ref-1303.md
references/ref-1304.md
references/ref-1305.md
references/ref-1306.md
references/ref-1307.md
references/ref-1308.md
references/ref-1309.md
references/ref-131.md
references/ref-1310.md
references/ref-1311.md
references/ref-132.md
references/ref-133.md
references/ref-1333.md
references/ref-1334.md
references/ref-1335.md
references/ref-1336.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
references/ref-437.md
references/ref-438.md
references/ref-439.md
references/ref-440.md
references/ref-441.md
references/ref-442.md
references/ref-443.md
references/ref-444.md
references/ref-445.md
references/ref-446.md
references/ref-447.md
references/ref-448.md
references/ref-449.md
references/ref-450.md
references/ref-451.md
references/ref-452.md
references/ref-453.md
references/ref-454.md
references/ref-455.md
references/ref-456.md
references/ref-457.md
references/ref-458.md
references/ref-459.md
references/ref-460.md
references/ref-461.md
references/ref-462.md
references/ref-463.md
references/ref-464.md
references/ref-465.md
references/ref-466.md
references/ref-467.md
references/ref-468.md
references/ref-469.md
references/ref-470.md
references/ref-471.md
references/ref-472.md
references/ref-473.md
references/ref-474.md
references/ref-475.md
references/ref-476.md
references/ref-477.md
references/ref-478.md
references/ref-479.md
references/ref-480.md
references/ref-481.md
references/ref-482.md
references/ref-483.md
references/ref-484.md
references/ref-485.md
references/ref-486.md
references/ref-487.md
references/ref-488.md
references/ref-489.md
references/ref-490.md
references/ref-491.md
references/ref-492.md
references/ref-493.md
references/ref-494.md
references/ref-495.md
references/ref-496.md
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-500.md
references/ref-501.md
references/ref-502.md
references/ref-503.md
references/ref-504.md
references/ref-505.md
references/ref-506.md
references/ref-507.md
references/ref-508.md
references/ref-509.md
references/ref-510.md
references/ref-511.md
references/ref-512.md
references/ref-513.md
references/ref-514.md
references/ref-515.md
references/ref-516.md
references/ref-517.md
references/ref-518.md
references/ref-519.md
references/ref-520.md
references/ref-521.md
references/ref-522.md
references/ref-523.md
references/ref-524.md
references/ref-525.md
references/ref-526.md
references/ref-527.md
references/ref-528.md
references/ref-529.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
references/ref-539.md
references/ref-540.md
references/ref-541.md
references/ref-542.md
references/ref-543.md
references/ref-544.md
references/ref-545.md
references/ref-546.md
references/ref-547.md
references/ref-548.md
references/ref-549.md
references/ref-550.md
references/ref-551.md
references/ref-552.md
references/ref-553.md
references/ref-554.md
references/ref-555.md
references/ref-556.md
references/ref-557.md
references/ref-558.md
references/ref-559.md
references/ref-560.md
references/ref-561.md
references/ref-562.md
references/ref-563.md
references/ref-564.md
references/ref-565.md
references/ref-566.md
references/ref-567.md
references/ref-568.md
references/ref-569.md
references/ref-570.md
references/ref-571.md
references/ref-572.md
references/ref-573.md
references/ref-574.md
references/ref-575.md
references/ref-576.md
references/ref-577.md
references/ref-578.md
references/ref-579.md
references/ref-580.md
references/ref-581.md
references/ref-582.md
references/ref-583.md
references/ref-584.md
references/ref-585.md
references/ref-586.md
references/ref-587.md
references/ref-588.md
references/ref-589.md
references/ref-590.md
references/ref-591.md
references/ref-592.md
references/ref-593.md
references/ref-594.md
references/ref-595.md
references/ref-596.md
references/ref-597.md
references/ref-598.md
references/ref-599.md
references/ref-600.md
references/ref-601.md
references/ref-602.md
references/ref-603.md
references/ref-604.md
references/ref-605.md
references/ref-606.md
references/ref-607.md
references/ref-608.md
references/ref-609.md
references/ref-610.md
references/ref-611.md
references/ref-612.md
references/ref-613.md
references/ref-614.md
references/ref-615.md
references/ref-616.md
references/ref-617.md
references/ref-618.md
references/ref-619.md
references/ref-620.md
references/ref-621.md
references/ref-622.md
references/ref-623.md
references/ref-624.md
references/ref-625.md
references/ref-626.md
references/ref-627.md
references/ref-628.md
references/ref-629.md
references/ref-630.md
references/ref-631.md
references/ref-632.md
references/ref-633.md
references/ref-634.md
references/ref-635.md
references/ref-636.md
references/ref-637.md
references/ref-638.md
references/ref-639.md
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
references/ref-644.md
references/ref-645.md
references/ref-646.md
references/ref-647.md
references/ref-648.md
references/ref-649.md
references/ref-650.md
references/ref-651.md
references/ref-652.md
references/ref-653.md
references/ref-654.md
references/ref-655.md
references/ref-656.md
references/ref-657.md
references/ref-658.md
references/ref-659.md
references/ref-660.md
references/ref-661.md
references/ref-662.md
references/ref-663.md
references/ref-664.md
references/ref-665.md
references/ref-666.md
references/ref-667.md
references/ref-668.md
references/ref-669.md
references/ref-670.md
references/ref-671.md
references/ref-672.md
references/ref-673.md
references/ref-674.md
references/ref-675.md
references/ref-676.md
references/ref-677.md
references/ref-678.md
references/ref-679.md
references/ref-680.md
references/ref-681.md
references/ref-682.md
references/ref-683.md
references/ref-684.md
references/ref-685.md
references/ref-686.md
references/ref-687.md
references/ref-688.md
references/ref-689.md
references/ref-690.md
references/ref-691.md
references/ref-692.md
references/ref-693.md
references/ref-694.md
references/ref-695.md
references/ref-696.md
references/ref-697.md
references/ref-698.md
references/ref-699.md
references/ref-700.md
references/ref-701.md
references/ref-702.md
references/ref-703.md
references/ref-704.md
references/ref-705.md
references/ref-706.md
references/ref-707.md
references/ref-708.md
references/ref-709.md
references/ref-710.md
references/ref-711.md
references/ref-712.md
references/ref-713.md
references/ref-714.md
references/ref-715.md
references/ref-716.md
references/ref-717.md
references/ref-718.md
references/ref-719.md
references/ref-720.md
references/ref-721.md
references/ref-722.md
references/ref-723.md
references/ref-724.md
references/ref-725.md
references/ref-726.md
references/ref-727.md
references/ref-728.md
references/ref-729.md
references/ref-730.md
references/ref-731.md
references/ref-732.md
references/ref-733.md
references/ref-734.md
references/ref-735.md
references/ref-736.md
references/ref-737.md
references/ref-738.md
references/ref-739.md
references/ref-740.md
references/ref-741.md
references/ref-742.md
references/ref-743.md
references/ref-744.md
references/ref-745.md
references/ref-746.md
references/ref-747.md
references/ref-748.md
references/ref-749.md
references/ref-750.md
references/ref-751.md
references/ref-752.md
references/ref-753.md
references/ref-754.md
references/ref-755.md
references/ref-756.md
references/ref-757.md
references/ref-758.md
references/ref-759.md
references/ref-760.md
references/ref-761.md
references/ref-762.md
references/ref-763.md
references/ref-764.md
references/ref-765.md
references/ref-766.md
references/ref-767.md
references/ref-768.md
references/ref-769.md
references/ref-770.md
references/ref-771.md
references/ref-772.md
references/ref-773.md
references/ref-774.md
references/ref-775.md
references/ref-776.md
references/ref-777.md
references/ref-778.md
references/ref-779.md
references/ref-780.md
references/ref-781.md
references/ref-782.md
references/ref-783.md
references/ref-784.md
references/ref-785.md
references/ref-786.md
references/ref-787.md
references/ref-788.md
references/ref-789.md
references/ref-790.md
references/ref-791.md
references/ref-792.md
references/ref-793.md
references/ref-794.md
references/ref-795.md
references/ref-796.md
references/ref-797.md
references/ref-798.md
references/ref-799.md
references/ref-800.md
references/ref-801.md
references/ref-802.md
references/ref-803.md
references/ref-804.md
references/ref-805.md
references/ref-806.md
references/ref-807.md
references/ref-808.md
references/ref-809.md
references/ref-810.md
references/ref-811.md
references/ref-812.md
references/ref-813.md
references/ref-814.md
references/ref-815.md
references/ref-816.md
references/ref-817.md
references/ref-818.md
references/ref-819.md
references/ref-820.md
references/ref-821.md
references/ref-822.md
references/ref-823.md
references/ref-824.md
references/ref-825.md
references/ref-826.md
references/ref-827.md
references/ref-828.md
references/ref-829.md
references/ref-830.md
references/ref-831.md
references/ref-832.md
references/ref-833.md
references/ref-834.md
references/ref-835.md
references/ref-836.md
references/ref-837.md
references/ref-838.md
references/ref-839.md
references/ref-840.md
references/ref-841.md
references/ref-842.md
references/ref-843.md
references/ref-844.md
references/ref-845.md
references/ref-846.md
references/ref-847.md
references/ref-848.md
references/ref-849.md
references/ref-850.md
references/ref-851.md
references/ref-852.md
references/ref-853.md
references/ref-854.md
references/ref-855.md
references/ref-856.md
references/ref-857.md
references/ref-858.md
references/ref-859.md
references/ref-860.md
references/ref-861.md
references/ref-862.md
references/ref-863.md
references/ref-864.md
references/ref-865.md
references/ref-866.md
references/ref-867.md
references/ref-868.md
references/ref-869.md
references/ref-870.md
references/ref-871.md
references/ref-872.md
references/ref-873.md
references/ref-874.md
references/ref-875.md
references/ref-876.md
references/ref-877.md
references/ref-878.md
references/ref-879.md
references/ref-880.md
references/ref-881.md
references/ref-882.md
references/ref-883.md
references/ref-884.md
references/ref-885.md
references/ref-886.md
references/ref-887.md
references/ref-888.md
references/ref-889.md
references/ref-890.md
references/ref-891.md
references/ref-892.md
references/ref-893.md
references/ref-894.md
references/ref-895.md
references/ref-896.md
references/ref-897.md
references/ref-898.md
references/ref-899.md
references/ref-900.md
references/ref-901.md
references/ref-902.md
references/ref-903.md
references/ref-904.md
references/ref-905.md
references/ref-906.md
references/ref-907.md
references/ref-908.md
references/ref-909.md
references/ref-910.md
references/ref-911.md
references/ref-912.md
references/ref-913.md
references/ref-914.md
references/ref-915.md
references/ref-916.md
references/ref-917.md
references/ref-918.md
references/ref-919.md
references/ref-920.md
references/ref-921.md
references/ref-922.md
references/ref-923.md
references/ref-924.md
references/ref-925.md
references/ref-926.md
references/ref-927.md
references/ref-928.md
references/ref-929.md
references/ref-930.md
references/ref-931.md
references/ref-932.md
references/ref-933.md
references/ref-934.md
references/ref-935.md
references/ref-936.md
references/ref-937.md
references/ref-938.md
references/ref-939.md
references/ref-940.md
references/ref-941.md
references/ref-942.md
references/ref-943.md
references/ref-944.md
references/ref-945.md
references/ref-946.md
references/ref-947.md
references/ref-948.md
references/ref-949.md
references/ref-950.md
references/ref-951.md
references/ref-952.md
references/ref-953.md
references/ref-954.md
references/ref-955.md
references/ref-956.md
references/ref-957.md
references/ref-958.md
references/ref-959.md
references/ref-960.md
references/ref-961.md
references/ref-962.md
references/ref-963.md
references/ref-964.md
references/ref-965.md
references/ref-966.md
references/ref-967.md
references/ref-968.md
references/ref-969.md
references/ref-970.md
references/ref-971.md
references/ref-972.md
references/ref-973.md
references/ref-974.md
references/ref-975.md
references/ref-976.md
references/ref-977.md
references/ref-978.md
references/ref-979.md
references/ref-980.md
references/ref-981.md
references/ref-982.md
references/ref-983.md
references/ref-984.md
references/ref-985.md
references/ref-986.md
references/ref-987.md
references/ref-988.md
references/ref-989.md
references/ref-990.md
references/ref-991.md
references/ref-992.md
references/ref-993.md
references/ref-994.md
references/ref-995.md
references/ref-996.md
references/ref-997.md
references/ref-998.md
references/ref-999.md
site-matrix.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
topics/2026/2026-09-25-area18-s4.md
topics/2026/2026-09-25-area18-s6.md
topics/2026/2026-09-25-area18-s7.md
topics/2026/2026-09-25-area18-s8.md
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area20-s10.md
topics/2026/2026-09-25-area20-s11.md
topics/2026/2026-09-25-area20-s4.md
topics/2026/2026-09-25-area20-s6.md
topics/2026/2026-09-25-area20-s7.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
topics/2026/2026-09-25-area22-s10.md
topics/2026/2026-09-25-area22-s4.md
topics/2026/2026-09-25-area22-s6.md
topics/2026/2026-09-25-area22-s7.md
topics/2026/2026-09-25-area22-s8.md
topics/2026/2026-09-25-area23-s10.md
topics/2026/2026-09-25-area23-s11.md
topics/2026/2026-09-25-area23-s4.md
topics/2026/2026-09-25-area23-s6.md
topics/2026/2026-09-25-area23-s7.md
topics/2026/2026-09-25-area24-s10.md
topics/2026/2026-09-25-area24-s3.md
topics/2026/2026-09-25-area24-s4.md
topics/2026/2026-09-25-area24-s6.md
topics/2026/2026-09-25-area24-s7.md
topics/2026/2026-09-25-area25-s11.md
topics/2026/2026-09-25-area25-s3.md
topics/2026/2026-09-25-area25-s6.md
topics/2026/2026-09-25-area25-s7.md
topics/2026/2026-09-25-area25-s8.md
topics/2026/2026-09-25-area26-s10.md
topics/2026/2026-09-25-area26-s11.md
topics/2026/2026-09-25-area26-s3.md
topics/2026/2026-09-25-area26-s4.md
topics/2026/2026-09-25-area26-s6.md
topics/2026/2026-09-25-area26-s7.md
topics/2026/2026-09-25-area26-s8.md
topics/2026/2026-09-25-area27-s10.md
topics/2026/2026-09-25-area27-s4.md
topics/2026/2026-09-25-area27-s6.md
topics/2026/2026-09-25-area27-s7.md
topics/2026/2026-09-25-area27-s8.md
topics/2026/2026-09-25-area28-s11.md
topics/2026/2026-09-25-area28-s3.md
topics/2026/2026-09-25-area28-s4.md
topics/2026/2026-09-25-area28-s6.md
topics/2026/2026-09-25-area28-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/2026/2026-09-26-area04-s10.md
topics/2026/2026-09-26-area25-s7.md
topics/2026/2026-09-29-area01-s10.md
topics/2026/2026-09-29-area01-s11.md
topics/2026/2026-09-29-area01-s3.md
topics/2026/2026-09-29-area01-s4.md
topics/2026/2026-09-29-area01-s6.md
topics/2026/2026-09-29-area01-s7.md
topics/2026/2026-09-29-area01-s8.md
topics/2026/2026-09-29-area04-s10.md
topics/2026/2026-09-29-area04-s11.md
topics/2026/2026-09-29-area04-s3.md
topics/2026/2026-09-29-area04-s4.md
topics/2026/2026-09-29-area04-s6.md
topics/2026/2026-09-29-area04-s7.md
topics/2026/2026-09-29-area04-s8.md
topics/2026/2026-09-29-area06-s10.md
topics/2026/2026-09-29-area06-s11.md
topics/2026/2026-09-29-area06-s3.md
topics/2026/2026-09-29-area06-s4.md
topics/2026/2026-09-29-area06-s6.md
topics/2026/2026-09-29-area06-s7.md
topics/2026/2026-09-29-area06-s8.md
topics/2026/2026-09-29-area07-s10.md
topics/2026/2026-09-29-area07-s11.md
topics/2026/2026-09-29-area07-s3.md
topics/2026/2026-09-29-area07-s4.md
topics/2026/2026-09-29-area07-s6.md
topics/2026/2026-09-29-area07-s7.md
topics/2026/2026-09-29-area07-s8.md
topics/2026/2026-09-29-area08-s10.md
topics/2026/2026-09-29-area08-s11.md
topics/2026/2026-09-29-area08-s3.md
topics/2026/2026-09-29-area08-s4.md
topics/2026/2026-09-29-area08-s6.md
topics/2026/2026-09-29-area08-s7.md
topics/2026/2026-09-29-area08-s8.md
topics/2026/2026-09-29-area09-s10.md
topics/2026/2026-09-29-area09-s11.md
topics/2026/2026-09-29-area09-s3.md
topics/2026/2026-09-29-area09-s4.md
topics/2026/2026-09-29-area09-s6.md
topics/2026/2026-09-29-area09-s7.md
topics/2026/2026-09-29-area09-s8.md
topics/2026/2026-09-29-area10-s10.md
topics/2026/2026-09-29-area10-s11.md
topics/2026/2026-09-29-area10-s3.md
topics/2026/2026-09-29-area10-s4.md
topics/2026/2026-09-29-area10-s6.md
topics/2026/2026-09-29-area10-s7.md
topics/2026/2026-09-29-area10-s8.md
topics/2026/2026-09-29-area11-s10.md
topics/2026/2026-09-29-area11-s11.md
topics/2026/2026-09-29-area11-s3.md
topics/2026/2026-09-29-area11-s4.md
topics/2026/2026-09-29-area11-s6.md
topics/2026/2026-09-29-area11-s7.md
topics/2026/2026-09-29-area11-s8.md
topics/2026/2026-09-29-area12-s10.md
topics/2026/2026-09-29-area12-s11.md
topics/2026/2026-09-29-area12-s3.md
topics/2026/2026-09-29-area12-s4.md
topics/2026/2026-09-29-area12-s6.md
topics/2026/2026-09-29-area12-s7.md
topics/2026/2026-09-29-area12-s8.md
topics/2026/2026-09-29-area13-s10.md
topics/2026/2026-09-29-area13-s11.md
topics/2026/2026-09-29-area13-s3.md
topics/2026/2026-09-29-area13-s4.md
topics/2026/2026-09-29-area13-s6.md
topics/2026/2026-09-29-area13-s7.md
topics/2026/2026-09-29-area13-s8.md
topics/2026/2026-09-29-area61-s10.md
topics/2026/2026-09-29-area61-s11.md
topics/2026/2026-09-29-area61-s3.md
topics/2026/2026-09-29-area61-s4.md
topics/2026/2026-09-29-area61-s6.md
topics/2026/2026-09-29-area61-s7.md
topics/2026/2026-09-29-area61-s8.md
topics/2026/2026-09-29-area62-s10.md
topics/2026/2026-09-29-area62-s11.md
topics/2026/2026-09-29-area62-s3.md
topics/2026/2026-09-29-area62-s4.md
topics/2026/2026-09-29-area62-s6.md
topics/2026/2026-09-29-area62-s7.md
topics/2026/2026-09-29-area62-s8.md
topics/2026/2026-09-29-area63-s10.md
topics/2026/2026-09-29-area63-s11.md
topics/2026/2026-09-29-area63-s3.md
topics/2026/2026-09-29-area63-s4.md
topics/2026/2026-09-29-area63-s6.md
topics/2026/2026-09-29-area63-s7.md
topics/2026/2026-09-29-area63-s8.md
topics/2026/2026-09-29-area64-s10.md
topics/2026/2026-09-29-area64-s11.md
topics/2026/2026-09-29-area64-s3.md
topics/2026/2026-09-29-area64-s4.md
topics/2026/2026-09-29-area64-s6.md
topics/2026/2026-09-29-area64-s7.md
topics/2026/2026-09-29-area64-s8.md
topics/2026/2026-09-29-area65-s10.md
topics/2026/2026-09-29-area65-s11.md
topics/2026/2026-09-29-area65-s3.md
topics/2026/2026-09-29-area65-s4.md
topics/2026/2026-09-29-area65-s6.md
topics/2026/2026-09-29-area65-s7.md
topics/2026/2026-09-29-area65-s8.md
topics/2026/2026-09-30-area02-s10.md
topics/2026/2026-09-30-area02-s11.md
topics/2026/2026-09-30-area02-s3.md
topics/2026/2026-09-30-area02-s4.md
topics/2026/2026-09-30-area02-s6.md
topics/2026/2026-09-30-area02-s7.md
topics/2026/2026-09-30-area02-s8.md
topics/2026/2026-09-30-area03-s10.md
topics/2026/2026-09-30-area03-s11.md
topics/2026/2026-09-30-area03-s3.md
topics/2026/2026-09-30-area03-s4.md
topics/2026/2026-09-30-area03-s6.md
topics/2026/2026-09-30-area03-s7.md
topics/2026/2026-09-30-area03-s8.md
topics/2026/2026-09-30-area14-s10.md
topics/2026/2026-09-30-area14-s11.md
topics/2026/2026-09-30-area14-s3.md
topics/2026/2026-09-30-area14-s4.md
topics/2026/2026-09-30-area14-s6.md
topics/2026/2026-09-30-area14-s8.md
topics/2026/2026-09-30-area16-s10.md
topics/2026/2026-09-30-area16-s11.md
topics/2026/2026-09-30-area16-s4.md
topics/2026/2026-09-30-area16-s6.md
topics/2026/2026-09-30-area16-s7.md
topics/2026/2026-09-30-area16-s8.md
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
topics/2026/2026-09-30-area36-s10.md
topics/2026/2026-09-30-area36-s11.md
topics/2026/2026-09-30-area36-s3.md
topics/2026/2026-09-30-area36-s4.md
topics/2026/2026-09-30-area36-s6.md
topics/2026/2026-09-30-area36-s7.md
topics/2026/2026-09-30-area36-s8.md
topics/2026/2026-09-30-area37-s10.md
topics/2026/2026-09-30-area37-s4.md
topics/2026/2026-09-30-area37-s6.md
topics/2026/2026-09-30-area37-s8.md
topics/2026/2026-09-30-area40-s10.md
topics/2026/2026-09-30-area40-s11.md
topics/2026/2026-09-30-area40-s3.md
topics/2026/2026-09-30-area40-s4.md
topics/2026/2026-09-30-area40-s6.md
topics/2026/2026-09-30-area40-s7.md
topics/2026/2026-09-30-area40-s8.md
topics/2026/2026-09-30-area41-s10.md
topics/2026/2026-09-30-area41-s11.md
topics/2026/2026-09-30-area41-s3.md
topics/2026/2026-09-30-area41-s4.md
topics/2026/2026-09-30-area41-s6.md
topics/2026/2026-09-30-area41-s7.md
topics/2026/2026-09-30-area41-s8.md
topics/2026/2026-09-30-area43-s10.md
topics/2026/2026-09-30-area43-s11.md
topics/2026/2026-09-30-area43-s3.md
topics/2026/2026-09-30-area43-s4.md
topics/2026/2026-09-30-area43-s6.md
topics/2026/2026-09-30-area43-s7.md
topics/2026/2026-09-30-area44-s10.md
topics/2026/2026-09-30-area44-s11.md
topics/2026/2026-09-30-area44-s3.md
topics/2026/2026-09-30-area44-s4.md
topics/2026/2026-09-30-area44-s6.md
topics/2026/2026-09-30-area44-s7.md
topics/2026/2026-09-30-area44-s8.md
topics/2026/2026-09-30-area45-s10.md
topics/2026/2026-09-30-area45-s11.md
topics/2026/2026-09-30-area45-s3.md
topics/2026/2026-09-30-area45-s4.md
topics/2026/2026-09-30-area45-s6.md
topics/2026/2026-09-30-area45-s7.md
topics/2026/2026-09-30-area45-s8.md
topics/2026/2026-09-30-area46-s10.md
topics/2026/2026-09-30-area46-s11.md
topics/2026/2026-09-30-area46-s3.md
topics/2026/2026-09-30-area46-s4.md
topics/2026/2026-09-30-area46-s6.md
topics/2026/2026-09-30-area46-s7.md
topics/2026/2026-09-30-area46-s8.md
topics/2026/2026-09-30-area49-s10.md
topics/2026/2026-09-30-area49-s11.md
topics/2026/2026-09-30-area49-s3.md
topics/2026/2026-09-30-area49-s4.md
topics/2026/2026-09-30-area49-s6.md
topics/2026/2026-09-30-area49-s7.md
topics/2026/2026-09-30-area49-s8.md
topics/2026/2026-09-30-area50-s10.md
topics/2026/2026-09-30-area50-s11.md
topics/2026/2026-09-30-area50-s3.md
topics/2026/2026-09-30-area50-s4.md
topics/2026/2026-09-30-area50-s6.md
topics/2026/2026-09-30-area50-s7.md
topics/2026/2026-09-30-area50-s8.md
topics/2026/2026-09-30-area52-s10.md
topics/2026/2026-09-30-area52-s11.md
topics/2026/2026-09-30-area52-s3.md
topics/2026/2026-09-30-area52-s4.md
topics/2026/2026-09-30-area52-s6.md
topics/2026/2026-09-30-area52-s8.md
topics/2026/2026-09-30-area53-s10.md
topics/2026/2026-09-30-area53-s11.md
topics/2026/2026-09-30-area53-s3.md
topics/2026/2026-09-30-area53-s4.md
topics/2026/2026-09-30-area53-s6.md
topics/2026/2026-09-30-area53-s7.md
topics/2026/2026-09-30-area53-s8.md
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
topics/2026/2026-09-30-area67-s10.md
topics/2026/2026-09-30-area67-s11.md
topics/2026/2026-09-30-area67-s3.md
topics/2026/2026-09-30-area67-s4.md
topics/2026/2026-09-30-area67-s6.md
topics/2026/2026-09-30-area67-s7.md
topics/2026/2026-09-30-area67-s8.md
topics/2026/2026-10-09-area18-s10.md
topics/2026/2026-10-09-area18-s11.md
topics/2026/2026-10-09-area18-s6.md
topics/2026/2026-10-09-area18-s7.md
topics/2026/2026-10-09-area18-s8.md
topics/2026/2026-10-09-area19-s10.md
topics/2026/2026-10-09-area19-s11.md
topics/2026/2026-10-09-area19-s6.md
topics/2026/2026-10-09-area19-s7.md
topics/2026/2026-10-09-area19-s8.md
topics/2026/2026-10-09-area33-s10.md
topics/2026/2026-10-09-area33-s11.md
topics/2026/2026-10-09-area33-s3.md
topics/2026/2026-10-09-area33-s6.md
topics/2026/2026-10-09-area33-s7.md
topics/2026/2026-10-09-area33-s8.md
topics/index.md
tracks/chat-based-configuration-and-operation/experiments.md
tracks/chat-based-configuration-and-operation/index.md
tracks/chat-based-configuration-and-operation/log.md
tracks/chat-based-configuration-and-operation/question-backlog.md
tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md
tracks/chat-based-configuration-and-operation/stage-10-integrated-verification.md
tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md
tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md
tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md
tracks/chat-based-configuration-and-operation/stage-6-chat-map-authoring.md
tracks/chat-based-configuration-and-operation/stage-7-chat-scenario-composition.md
tracks/chat-based-configuration-and-operation/stage-8-chat-robot-configuration.md
tracks/chat-based-configuration-and-operation/stage-9-chat-real-situation-replay.md
tracks/chat-based-configuration-and-operation/task-model-draft.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
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

### runs/2026-10-09-17/pages.json

```json
{
  "run_id": "2026-10-09-17",
  "outline": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 250,
      "summary": "변경 없음. 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 접점이고 판단 배치가 운영 연속성을 좌우한다. [추정][^ref-031][^ref-774][^ref-1030][^ref-1031]",
      "planned_findings": []
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 150,
      "summary": "변경 없음. 클라우드 로보틱스·계산 오프로딩·현장 클라우드·플릿 어댑터·OpenAPI·AsyncAPI·웹훅 개념은 주제 페이지에 있다.",
      "planned_findings": []
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "변경 없음(1차 검증 지시: 현장 유형이 없는 f7·f12 는 사례 칸에 넣지 않는다). 병원·제조 공장·물류창고·기타 사례 4건.",
      "planned_findings": []
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2000,
      "summary": "기존 요약·주제 페이지 링크 유지에 더해, VDA 5050 3.0.0 의 끊김 전제와 base 끝까지 수행, 관제·로봇 기능 분담, Open-RMF 중앙 교통 일정, QoS 0·1 구분과 주문 갱신 번호를 덧붙인다. 연결이 끊긴 로봇은 base 의 마지막 노드까지 주문을 수행한다. [사실][^ref-031]",
      "planned_findings": [
        "f2",
        "f3",
        "f4",
        "f5",
        "f7",
        "f10",
        "f18"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1500,
      "summary": "기존 요약 유지에 더해 VDA 5050 3.0.0 의 버전 규칙·범위 제외, Open-RMF 플릿 제어 수준과 책의 폐기 예고 서술(추정), rmf-web API 서버의 M2M 설정·빈 권한 그룹·사용자 비동기화·프록시 설정을 덧붙인다. VDA 5050 3.0.0 은 외부 IT 시스템 인터페이스와 사이버보안 조치를 범위 밖에 둔다. [사실][^ref-031]",
      "planned_findings": [
        "f1",
        "f6",
        "f9",
        "f11",
        "f12",
        "f13",
        "f14"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 150,
      "summary": "변경 없음. 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구(초록 기준). [사실][^ref-304][^ref-1031][^ref-1027][^ref-308]",
      "planned_findings": []
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1700,
      "summary": "기존 표·원문 문장 유지에 더해, 외부 이벤트 전달 보장과 외부 API 의 인증·권한 범위(고객·현장 구분, 계정 해지)를 ROP 몫으로 보는 추정과 base·horizon 해제 정책의 경계를 덧붙인다. 업무 시스템에 내보내는 웹훅·이벤트의 전달 보장은 ROP 외부 API 가 따로 정해야 할 것으로 보인다. [추정][^ref-031]",
      "planned_findings": [
        "f3",
        "f6",
        "f7",
        "f8",
        "f15"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 150,
      "summary": "변경 없음. 연결 영역 목록은 주제 페이지에 있다.",
      "planned_findings": []
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "기존 요약 유지에 더해 oq-206·oq-207·oq-208·oq-300 의 부분 근거(상태 열림 유지), 미조사 질문, 새 질문 1건을 덧붙인다. 확인한 두 출처는 폐기 예고 기간을 정하지 않는다. [추정][^ref-031][^ref-004]",
      "planned_findings": [
        "f8",
        "f16",
        "f17",
        "f18"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "6·7·9·11절에 2026-10-09 갱신 소절 덧붙임(끊김 때 base 수행·관제/로봇 기능 분담·QoS 0·1·주문 갱신 번호·클라우드 브로커 주제 조정, VDA 5050 버전 규칙·범위 제외, 플릿 제어 수준과 책의 폐기 예고 서술 강등, rmf-web M2M 설정·빈 권한 그룹·사용자 비동기화·프록시, 전달 보장·권한 범위 추정, 열린 질문 부분 근거와 새 질문 1건), 13절 ref-004·ref-031·ref-762 접근일 2026-10-09 로 갱신",
      "patches": [
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "\n### 연결이 끊길 때 판단을 어디에 두는가 (2026-10-09 갱신)\n\n로봇–관제 인터페이스인 [VDA 5050](../../glossary/vda-5050.md) 3.0.0 은 무선망에서 연결 끊김과 메시지 손실이 생길 수 있다는 것을 통신 전반의 전제로 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 연계 대상: 로봇 자체 지능·제어 — 이 명세에서 브로커와 연결이 끊긴 로봇은 주문 정보를 유지하고 base(관제가 해제(released)한 노드·엣지 구간. 용어집의 [해제 구역](../../glossary/release-zone.md)과는 다른 개념)의 마지막 노드까지 주문을 수행한다. [사실][^ref-031] 같은 명세는 [메시지 큐잉 원격 측정 전송](../../glossary/mqtt.md)(Message Queuing Telemetry Transport, MQTT)이 비동기이고 무선 전송을 믿을 수 없으므로 관제가 이미 해제한 base 를 바꿀 수 없고 실행된 것으로 간주해야 하며, 주문 취소([cancelOrder](../../glossary/vda-5050-cancel-order.md))도 같은 이유로 신뢰할 수 없다고 본다. [사실][^ref-031]\n\nVDA 5050 3.0.0 은 판단을 관제와 로봇으로 나눈다. 관제의 최소 기능으로는 주문 배정, 선 유도(line-guided) 로봇의 경로 계산·안내, 교착 탐지·해소, 에너지 관리, 교통 통제, 문·게이트·승강기 같은 주변 시스템과의 통신, 통신 오류 탐지·해소를 든다. [사실][^ref-031] 명세는 관제에 교통 통제 기능을 요구하되 그 로직은 정하지 않고 범위 밖에 둔다. [사실][^ref-031] 연계 대상: 로봇 자체 지능·제어 — 위치 추정·경로 실행·동작 실행·상태 연속 전송은 같은 명세가 로봇의 기능으로 드는 것이다. [사실][^ref-031]\n\nOpen-RMF 의 교통 일정은 플랫폼 중립의 중앙 데이터베이스로, 배치된 모든 플릿 관리자가 예상 경로를 보고하고, 충돌이 예상되면 플릿 관리자들이 협상하며 시스템 통합사가 둔 제3자 판정자가 제안을 고른다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004] 긴급 작업은 의도적으로 충돌을 올려 협상을 강제할 수 있다. [사실][^ref-004] 교통 조율 자체의 본론은 [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)에서 다루고, 이 영역에서는 중앙 조율을 어디에 둘지 정하는 근거로만 쓴다.\n\n두 자료를 함께 보면, ROP 의 판단 배치 정책은 중앙 조율 서비스를 클라우드와 현장 서버 가운데 어디에 둘지와 함께, 연결이 끊긴 동안 로봇이 계속 갈 수 있는 base 의 길이를 정해야 할 것으로 보인다(구축자 판단, oq-206 부분 근거). [추정][^ref-031][^ref-004] base 의 길이는 관제의 교통 통제 기능에 걸치므로 27. 다중 로봇 경로·교통 관리 — MAPF와 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)에서 함께 다룬다.\n\n### 메시지 전달 보장 수준 (2026-10-09 갱신)\n\nVDA 5050 3.0.0 은 통신 부하를 줄이려고 order·instantActions·state·factsheet·zoneSet·responses·visualization 주제에는 MQTT 서비스 품질(Quality of Service, QoS) 0(최선 노력)을, connection 주제에는 QoS 1(최소 한 번)을 쓰게 한다. [사실][^ref-031] 로봇이 예기치 않게 끊기면 브로커가 [유언 메시지](../../glossary/mqtt-last-will.md)(last will)로 다른 구독자에게 알린다. [사실][^ref-031]\n\n주문 갱신은 같은 orderId 에 orderUpdateId 를 늘려 보낸다. [사실][^ref-031] 로봇은 같은 orderUpdateId 로 같은 내용이 다시 오면 무시하고, 내용이 다르면 SAME_ORDER_UPDATE_ID, 더 낮은 orderUpdateId 면 OUTDATED_ORDER_UPDATE 경고를 보고해 재전송과 순서 뒤바뀜을 메시지 수준에서 걸러낸다. [사실][^ref-031] 명령 실행 신뢰성의 본론은 [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)에서 다룬다.\n\n클라우드 브로커를 쓸 때 VDA 5050 3.0.0 은 클라우드 사업자가 강제하는 주제 구조가 있으므로 MQTT 주제 단계 구조를 엄격히 정하지 않는다. [사실][^ref-031] 클라우드 브로커는 구조를 개별 조정할 수 있으나 제안 구조를 대략 따라야 하며, 주제 이름(order·state 등)은 필수다. [사실][^ref-031]\n"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "\n### 버전 규칙·범위와 오픈소스 API 의 현재 서술 (2026-10-09 갱신)\n\n- **VDA 5050 3.0.0** — [의미적 버전 관리](../../glossary/semantic-versioning.md)를 써서 주 버전(x.0.0)은 대체로(typically) 새 필수 필드 도입 같은 하위 호환을 깨는 변경, 부 버전(3.x.0)은 선택 매개변수 추가 같은 새 기능, 수 버전(3.0.x)은 문서 오탈자 같은 작은 수정에 쓴다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] VDA 5050 3.0.0 이 지역(local) 브로커용으로 제안하는 주제 구조에서는 MQTT 주제 경로에 'v' 를 붙인 주 버전(예 v3)을 넣는다. 이 주제 구조는 엄격한 규정이 아니며 클라우드 브로커는 조정할 수 있다(6절). [사실][^ref-031] 명세는 주변 설비·기반 시설·외부 IT 시스템과의 인터페이스, 안전 요구사항, 교통 관리 로직, 운영 책임 배분, 사이버보안 조치를 범위 밖에 둔다. [사실][^ref-031]\n- **Open-RMF 플릿 어댑터** — Open-RMF 핵심 문서는 플릿 어댑터를 [플릿 제어 수준](../../glossary/fleet-control-level.md) 네 가지(Full Control·Traffic Light·Read Only·No Interface)로 나누고, Full Control 에는 재사용 C++ API(파이썬 바인딩 포함)를 제공한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004] 같은 문서인 Open-RMF 책 rmf-core 장(작성 시점 미확인)은 Read Only 용 예비 ROS 2 메시지 API 가 향후 판에서 C++ API 로 대체되어 폐기될 예정이고 Traffic Light 용 재사용 API 는 아직 구현되지 않았다고 서술하지만, 이는 책의 서술이며 현재 배포판의 상태는 미확인이다. [추정][^ref-004]\n- **Open-RMF rmf-web API 서버** — 주제 페이지에 있는 기존 서술(신원 제공자 기반 인증, 역할·동작·권한 그룹 판정)에 더해, 2026-10-09 확인한 README 에는 OAuth 2.0 client_credentials(기계 간, M2M) 흐름에서 신원 제공자가 표준 클레임을 빼고 네임스페이스 붙은 클레임만 주는 경우를 위한 선택 설정 preferred_username_claim_namespace 가 있다. [사실][^ref-762] README 의 TODO 절 기준으로, 자원의 권한 그룹을 정하는 방식이 아직 정해지지 않아 현재는 모든 자원이 기본 빈 그룹('')에 들어간다(코드 동작으로는 확인하지 않음). [사실][^ref-762] 서버는 자체 사용자·역할·권한 데이터베이스를 신원 제공자와 동기화하지 않으므로, rmf-server 에서 사용자를 지워도 로그인만 요구하는 반보호 API 접근은 막지 못하고 로그인 자체를 막으려면 신원 제공자에서 사용자를 지워야 한다. [사실][^ref-762] 역방향 프록시 뒤에서 쓸 때는 public_url 을 공개 주소로 설정하고 프록시가 경로 접두어를 제거하게 해야 한다. [사실][^ref-762]\n"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "\n### 전달 보장과 외부 API 의 인증·권한 범위 (2026-10-09 갱신)\n\n로봇–관제 표준인 VDA 5050 3.0.0 은 외부 IT 시스템과의 인터페이스와 사이버보안 조치를 범위 밖에 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 사이버보안은 [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md), 안전 요구는 [M. 안전](../safety/index.md) 쪽에서 다루며 이 영역에서는 표준 범위 밖이라는 사실만 적는다.\n\n- **외부 이벤트 전달 보장**: VDA 5050 은 주문 갱신 번호(orderUpdateId)로 재전송·순서 문제를 다루지만 대부분 주제에 QoS 0 최선 노력 전달을 쓰고 외부 IT 시스템 인터페이스를 범위 밖에 둔다. 그래서 업무 시스템에 내보내는 웹훅·이벤트의 전달 보장(재시도·순서·중복 제거)은 ROP 의 외부 API 가 따로 정해야 할 것으로 보인다(구축자 판단, oq-208 부분 근거). [추정][^ref-031]\n- **외부 API 의 인증·권한 범위**: rmf-web API 서버는 README 기준으로 권한 그룹 결정이 미구현이고 사용자 해지가 신원 제공자에 달려 있다. 그래서 Open-RMF 웹 API 를 ROP 외부 API 의 기반으로 쓰면 고객·현장별 자원 구분과 외부 계정 해지를 ROP 가 신원 제공자 연동과 권한 그룹 규칙으로 직접 채워야 할 것으로 보인다(구축자 판단). [추정][^ref-762] 고객·현장 격리 자체는 [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)에서 다룬다.\n- **연결이 끊긴 동안의 실행**: 연계 대상: 로봇 자체 지능·제어 — 연결이 끊긴 로봇이 base(관제가 해제한 노드·엣지 구간)의 끝까지 수행하는 동작과 위치 추정·경로 실행은 로봇 쪽 기능이다. [사실][^ref-031] ROP 몫은 base·horizon 을 얼마나 해제할지 정하는 정책과 그 인터페이스로 한정되는 것으로 보인다(구축자 판단). [추정][^ref-031]\n"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "\n### 부분 근거와 새 질문 (2026-10-09 갱신)\n\n아래 질문은 이번 실행에서 부분 근거만 얻었으므로 모두 열림 상태를 유지한다.\n\n- **oq-206** (상태: 열림) 클라우드 연결이 끊길 때 로봇과 현장 서버가 어디까지 계속 동작하는가 — VDA 5050 의 base 끝까지 수행과 Open-RMF 의 중앙 교통 일정을 함께 보면, 중앙 조율 위치와 base 길이를 함께 정해야 할 것으로 보인다(6절, 구축자 판단). [추정][^ref-031][^ref-004] 네이버 ARC 의 끊김 동작은 여전히 미확인이다.\n- **oq-207** (상태: 열림) 외부 API 의 버전 관리·폐기 예고 정책 — 이번에 확인한 두 출처(VDA 5050 3.0.0 명세, Open-RMF 책 rmf-core 장)에서는 버전 표기 규칙과 '향후 판에서 폐기' 같은 예고 문구는 있으나 폐기 예고 기간이나 구판 지원 기간은 정하지 않는다. [추정][^ref-031][^ref-004] 관련 개념은 용어집 [API 폐기 정책](../../glossary/api-deprecation-policy.md)에 있다.\n- **oq-208** (상태: 열림) 웹훅·이벤트의 전달 보장 공통 기준 — 로봇–관제 쪽은 QoS 0·1 구분과 orderUpdateId 로 일부를 다루지만 외부 IT 인터페이스는 범위 밖이어서, 외부 이벤트 전달 보장은 ROP 가 정해야 할 것으로 보이며 공통 기준은 확인되지 않았다(9절, 구축자 판단). [추정][^ref-031]\n- **oq-300** (상태: 열림) 재시작 뒤 진행 중 작업 상태 유지 — FogROS2-FT 의 다중 클라우드 복제는 상태 없는(stateless) 로봇 서비스를 대상으로 하므로, 이 방법만으로는 답이 되지 않는 것으로 보인다. [추정][^ref-1031]\n- **새 질문** (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-17) Open-RMF 웹 API 서버처럼 권한 그룹 자동 결정이 미구현인 오픈소스 관제 API 위에서 고객·현장별 자원 격리를 API 수준으로 구현한 공개 사례나 설계 문서가 있는가? 근거는 README TODO 절의 빈 권한 그룹 서술이다. [사실][^ref-762]\n- oq-209(국내 TTA·KS 참조 구조 표준), oq-267(과금 단위), oq-301(OpenAPI·AsyncAPI 기반 적합성 시험 도구)은 이번 실행에서 조사하지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.\n"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09\n[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09\n[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09\n[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30\n[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30\n[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30\n[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30\n[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30\n[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30\n[^ref-1027]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30\n[^ref-1028]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30\n[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30\n[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30\n[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area41-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"6. 대표 접근법과 기술\" 절(1,999자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area41-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,533자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area41-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 41. 플랫폼 아키텍처·외부 API 의 \"11. 열린 질문\" 절(1,163자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 41. 플랫폼 아키텍처·외부 API | 6·7·9·11절 차등 갱신: 끊김 때 base 수행·관제/로봇 기능 분담·QoS 0·1·주문 갱신 번호, VDA 5050 버전 규칙·범위 제외, 플릿 제어 수준 폐기 예고 서술 추정 강등, rmf-web M2M 설정·빈 권한 그룹·사용자 비동기화, 전달 보장·권한 범위 추정, 열린 질문 부분 근거와 새 질문 1건 | run 2026-10-09-17",
  "index_updates": {
    "home_recent": "2026-10-09 — 41. 플랫폼 아키텍처·외부 API: 연결 끊김 때 판단 배치(VDA 5050 base·Open-RMF 중앙 교통 일정), 메시지 전달 보장 수준, 외부 API 인증·권한 범위 갱신(신뢰도 low)",
    "category_recent": "2026-10-09 — 41. 플랫폼 아키텍처·외부 API: 6·7·9·11절 갱신 — VDA 5050 3.0.0 버전 규칙·QoS·범위 제외, rmf-web API 서버 M2M 설정·빈 권한 그룹, 외부 이벤트 전달 보장 추정, 열린 질문 부분 근거",
    "area_recent": "2026-10-09 — 41. 플랫폼 아키텍처·외부 API: 6절 끊김 때 판단 배치·전달 보장 수준, 7절 VDA 5050 버전 규칙·Open-RMF 플릿 제어 수준·rmf-web 인증 설정, 9절 전달 보장·권한 범위 추정, 11절 oq-206·oq-207·oq-208·oq-300 부분 근거와 새 질문 1건 (실행 2026-10-09-17)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "mqtt-quality-of-service-level",
      "term_ko": "MQTT 서비스 품질 수준",
      "term_en": "MQTT Quality of Service (QoS) Level",
      "definition": "MQTT 에서 메시지 전달 보장 수준을 고르는 설정으로, VDA 5050 3.0.0 은 대부분 주제에 최선 노력(QoS 0)을, 연결 상태 주제에 최소 한 번(QoS 1)을 쓴다.",
      "description": "VDA 5050 3.0.0 은 통신 부하를 줄이려고 order·state 등 주제에 QoS 0 을, connection 주제에 QoS 1 을 쓴다. 이번 출처는 QoS 0·1 만 다루며 그 밖의 수준은 이 항목에서 다루지 않는다.",
      "related_areas": [
        41,
        20,
        42,
        29
      ],
      "sources": [
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "oauth2-client-credentials-grant",
      "term_ko": "클라이언트 자격 증명 흐름",
      "term_en": "OAuth 2.0 Client Credentials Grant (Machine-to-Machine)",
      "definition": "사람 사용자 없이 서비스나 기계가 자기 자격 증명으로 접근 토큰을 받아 API 를 부르는 OAuth 2.0 인가 방식이다.",
      "description": "Open-RMF rmf-web API 서버 README 는 이 흐름(M2M)에서 신원 제공자가 표준 클레임 대신 네임스페이스 붙은 클레임만 주는 경우를 위한 선택 설정 preferred_username_claim_namespace 를 둔다(2026-10-09 확인).",
      "related_areas": [
        41,
        51
      ],
      "sources": [
        "ref-762"
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
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 핵심 구성(교통 일정·협상, 작업 계획)과 플릿 어댑터 제어 수준 4종, 수준별 API 제공 상태를 설명하는 공식 문서. 수준별 API 제공 상태 서술은 작성 시점 미확인으로 현재 배포판과 다를 수 있다.",
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
      "accessed": "2026-10-09",
      "summary": "플릿 관제와 이동 로봇 사이 제조사 중립 통신 인터페이스 VDA 5050 3.0.0 명세. MQTT·JSON 전송, 버전 규칙, QoS, 주문·갱신·취소, 범위 제외 항목을 정한다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 웹 API 서버의 설정, 지원 DB, 프록시 운용, OpenID Connect 인증과 역할·권한 그룹 인가, M2M 클레임 설정, 사용자 데이터 비동기화 방침을 설명하는 README.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "Open-RMF 웹 API 서버처럼 권한 그룹 자동 결정이 미구현인 오픈소스 관제 API 위에서 고객·현장별 자원 격리를 API 수준으로 구현한 공개 사례나 설계 문서가 있는가?",
      "areas": [
        41,
        51
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [],
  "additional_research_requests": [
    "7절 Open-RMF 플릿 어댑터: 현재 Open-RMF rmf_ros2 배포판(latest API 문서)에서 Traffic Light 용 재사용 API 의 제공 여부와 Read Only 예비 ROS 2 메시지 API 의 폐기 여부·시점을 공식 문서로 확인해 달라 — 책 rmf-core 장의 서술(작성 시점 미확인)을 [추정]으로 강등했고 현재 상태는 미확인으로 두었다.",
    "11절 oq-209: 국내 클라우드 로봇·이기종 로봇 통합관제 참조 구조나 외부 API 를 정한 TTA·KS 표준 여부를 한국어로 검색해 달라 — 이번 브리프는 검색 0회였다.",
    "11절 oq-301: OpenAPI·AsyncAPI 로 기술한 외부 API 를 연동 적합성 시험 기준으로 쓴 공개 시험 도구·절차를 조사해 달라.",
    "11절 oq-267: 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독) 비교 자료를 조사해 달라.",
    "5절 적용 사례: 상업 시설·가정·실외 현장에서 플랫폼 배치(클라우드·현장 서버·로봇)나 외부 API 가 드러난 사례가 필요하다 — 현재 사례는 병원·제조 공장·물류창고·기타 네 건뿐이다.",
    "7·11절 VDA 5050: 3.0.0 명세의 발행일과 원문 마지막 약 7,700자(검증자 미확인 구간)에 폐기·구판 지원 규정이 있는지 확인해 달라.",
    "7절 rmf-web: README 의 preferred_username_claim_namespace(M2M) 설정이 언제 들어갔는지 저장소 변경 이력으로 확인해 달라 — 리서치·검증 모두 확인하지 못해 '2026-10-09 확인한 README 에 있다'로만 썼다.",
    "용어집: 기존 'mqtt' 항목의 정의가 QoS 수준 설명을 이미 포함하는지 확인해 달라 — 입력에 정의 본문이 없어 'MQTT 서비스 품질 수준'을 QoS 0·1 만으로 새로 등록 제안했다. 중복이면 퍼블리셔 단계에서 합치거나 제외한다."
  ],
  "fixes_applied": [
    "f1: 7절 갱신 소절에서 'v' 붙은 주 버전 표기를 'VDA 5050 3.0.0 이 지역(local) 브로커용으로 제안하는 주제 구조에서'로 한정하고 엄격한 규정이 아니며 클라우드 브로커는 조정할 수 있다고 덧붙였으며, 주·부·수 버전 의미에 '대체로(typically)'를 살렸다.",
    "f2: 6절 '메시지 전달 보장 수준' 소절에서 QoS 0 사용 이유를 '통신 부하를 줄이려고'로 쓰고, 무선망의 끊김·손실은 6절 첫 소절 첫 문장에서 통신 전반의 전제로 따로 썼다.",
    "f5: 6절에서 클라우드 브로커는 구조를 개별 조정할 수 있으나 제안 구조를 대략 따라야 하며 주제 이름은 필수라는 조건을 함께 썼다.",
    "f7: 6절에서 '선 유도(line-guided) 로봇의 경로 계산·안내'로 고치고, 로봇 기능 목록 앞에 '연계 대상: 로봇 자체 지능·제어'를 표시했으며, 교통 통제는 '관제에 기능을 요구하되 그 로직은 정하지 않고 범위 밖에 둔다'로 썼다.",
    "f9: 7절에서 네 플릿 제어 수준과 Full Control C++ API(파이썬 바인딩)는 [사실]로, Read Only API 폐기 예정·Traffic Light 재사용 API 미구현은 'Open-RMF 책 rmf-core 장(작성 시점 미확인)의 서술'로 밝혀 [추정]으로 강등하고 현재 상태를 미확인으로 두었으며, 현재 상태 확인을 additional_research_requests 로 넘겼다.",
    "f17: 11절 oq-207 항목에서 범위를 '이번에 확인한 두 출처(VDA 5050 3.0.0 명세, Open-RMF 책 rmf-core 장)에서는'으로 한정하고 용어집 [API 폐기 정책](api-deprecation-policy) 링크를 달았으며, 위키 전체에 근거가 없다고 쓰지 않고 상태를 열림으로 유지했다.",
    "f11: 7절에서 M2M 네임스페이스 클레임 설정을 '2026-10-09 확인한 README 에 있다'로만 쓰고 새로 추가됐다고 쓰지 않았다.",
    "f12: 7절에서 빈 권한 그룹 서술을 'README 의 TODO 절 기준'으로 밝히고 코드 동작으로는 확인하지 않았다고 적었으며, 9절에서도 'README 기준'으로 썼다.",
    "f11·f12·f14 중복: OIDC·JWT 독립 검증, 역할·동작·권한 그룹 구조, /docs API 정의는 새 문장으로 반복하지 않고 '주제 페이지에 있는 기존 서술'로만 가리켰으며, 새로 더한 것은 M2M 설정·빈 그룹·사용자 비동기화·프록시 설정뿐이고 기존 각주 [^ref-762]를 재사용했다.",
    "f1·f9 중복: 주제 페이지의 기존 서술을 지우지 않고 7절에 갱신 소절을 덧붙이는 방식으로 반영했으며 새 각주를 만들지 않고 [^ref-031]·[^ref-004]를 재사용했다.",
    "f3·f18 용어: 6절에서 처음 나올 때 'base(관제가 해제(released)한 노드·엣지 구간. 용어집의 해제 구역과는 다른 개념)'로 쓰고 해제 구역 용어집 링크를 달아 구분했다.",
    "f9 표기: 7절에서 '제어 수준'을 용어집 표기 [플릿 제어 수준](fleet-control-level) 링크로 통일했다.",
    "f3·f7 범위: 6절과 9절에서 끊긴 로봇이 base 끝까지 수행하는 동작과 위치 추정·경로 실행을 '연계 대상: 로봇 자체 지능·제어'로 표시하고, 9절에서 ROP 몫을 base·horizon 해제 정책과 그 인터페이스로 한정했다.",
    "f8·f15·f18: 9절과 11절에서 [추정]으로 두고 '구축자 판단'을 밝혔으며, f15 는 51. 인증·권한·격리, f6 의 사이버보안 제외는 52. 통신 보호·위협 관리·감사에 링크하고, f4 는 29. 명령·작업 실행의 신뢰성, f10·f18 은 27. 다중 로봇 경로·교통 관리 — MAPF·42. 분산 시스템·통신·컴퓨팅 구조에 번호와 이름을 함께 써서 연결만 했다.",
    "11절 열린 질문: oq-206(f18)·oq-207(f1·f9·f17)·oq-208(f2·f4·f8)·oq-300(f16)은 부분 근거만 적고 상태를 열림으로 유지했으며(open_question_updates 에 상태 변경을 내지 않음), 새 질문 1건을 관련 영역 41·51 로 open_question_updates 에 등록했다.",
    "용어 후보 'MQTT 서비스 품질 수준': 정의에서 QoS 2(정확히 한 번)를 빼고 QoS 0·1 만 남겼다. 기존 'mqtt' 항목의 정의 본문이 입력에 없어 같은 정의인지 확인하지 못했으므로 additional_research_requests 에 중복 확인을 요청했다.",
    "각주: 13절 패치(각주 정의만 교체)로 [^ref-004]·[^ref-031]·[^ref-762]를 참고문헌 색인 줄 형식(ref-762 제목 'rmf-web — packages/api-server/README.md')과 접근일 2026-10-09 로 고치고, [^ref-1031]은 기존 줄(접근일 2026-09-30) 그대로 두었으며 reference_updates 에 ref-1031 을 넣지 않아 접근일을 바꾸지 않았다.",
    "5절·현장 유형 매트릭스: 현장 유형이 없는 f7·f12 를 사례 칸에 넣지 않았고, 5절을 패치하지 않았으며 site_matrix_updates 를 빈 배열로 냈다.",
    "차등 갱신: 6·7·9·11절은 기존 요약 문장과 주제 페이지 링크를 지우지 않고 append 로 갱신 소절을 덧붙였다. 각주 지시(17번) 이행을 위해 13절 각주 정의만 replace 로 함께 보냈고 그 밖의 절은 보내지 않았다.",
    "분량 초과 자동 분리: 41. 플랫폼 아키텍처·외부 API 본문 9,254자 > 기준 4,000자 → 3개 절을 주제 페이지로 옮김, 남은 본문 5,062자"
  ]
}
```

### runs/2026-10-09-17/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md

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
updated: 2026-10-09
sources: [ref-004, ref-031, ref-762, ref-304, ref-1023, ref-937, ref-1024, ref-1025, ref-1026, ref-870, ref-308, ref-1027, ref-1028, ref-1029, ref-774, ref-1030, ref-1031]
last_run: 2026-09-30
version: 3
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 41. 플랫폼 아키텍처·외부 API

# 41. 플랫폼 아키텍처·외부 API

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
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

이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 단일 접점이 되고, 판단을 어디에 두느냐가 운영 연속성을 좌우하므로 이 영역이 중요하다. [추정][^ref-031][^ref-774][^ref-1030][^ref-1031]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 왜 중요한가](../../topics/2026/2026-09-30-area41-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 절은 판단 배치와 외부 API 를 이해하는 데 필요한 개념인 클라우드 로보틱스·계산 오프로딩·현장 클라우드·플릿 어댑터와 제어 수준·OpenAPI·AsyncAPI·웹훅·브레인리스 로봇을 정리한다.

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
| 수행 자원 | 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리, 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·정보통신기술(ICT) 시스템용 API)의 네 영역이 역할을 나눈다. [사실][^ref-937] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 특정 병원의 배치 결과가 아니라 싱가포르 창이종합병원 CHART 가 공공 의료기관용으로 내놓은 미들웨어 구조다. [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)(Robotic Middleware for Healthcare)는 OMG DDS(Data Distribution Service)를 쓰며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다. [사실][^ref-937] 외부 시스템용 API 를 통합 영역으로 따로 두는 점이 이 영역의 "외부에 무엇을 열 것인가"와 이어진다(구축자 의견). [의견][^ref-937]

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
| 시작 조건 | 창고 관리 시스템(Warehouse Management System, WMS)에서 주문을 API 로 받는다. [추정] 벤더 주장[^ref-1030] |
| 작업 대상 | WMS 주문 정보와 피킹할 품목. [추정] 벤더 주장[^ref-1030] |
| 수행 자원 | LocusONE 플랫폼이 주문을 피킹 효율 기준으로 최적화해 로봇 작업으로 내린다. [추정] 벤더 주장[^ref-1030] |
| 제약 | 기존 인프라와 분리된 전용 WiFi 망을 설치·유지한다. [추정] 벤더 주장[^ref-1030] |
| 완료·인계 | 피킹 완료 확인을 WMS 로 즉시 회신한다. [추정] 벤더 주장[^ref-1030] |
| 예외·성과 | 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 데이터를 제공한다. 실패 시 복구 주체는 미확인. [추정] 벤더 주장[^ref-1030] |

흐름 단계로는 피킹에 해당한다. 외부 API 가 작업의 시작(주문 수신)과 끝(확인 회신)을 모두 맡는 구조다. [추정] 벤더 주장[^ref-1030] 플랫폼을 클라우드와 현장 가운데 어디에 두는지는 자료에 나오지 않는다(미확인). 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽의 일이고, ROP 는 연동 인터페이스만 다룬다(9절). [추정][^ref-1030]

### 기타

**현장 유형:** 기타

**사례:** 기업 사옥에서 클라우드로 로봇 운영(네이버 제2사옥 1784 의 ARC)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 클라우드의 ARC brain(이동 계획·위치 추정·작업 수행·기반 시설 연동), ARC eye(디지털 트윈 데이터와 측위 AI 로 로봇 위치 결정), ARC mind(웹 개발자용 웹 기반 OS)가 나눠 맡고, 로봇은 연산·판단을 싣지 않는다. [추정] 벤더 주장[^ref-1023] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

네이버는 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다. [추정] 벤더 주장[^ref-1023] 위치 추정·이동 계획까지 클라우드에 두는 이 설계는 분류 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 볼 수 있으며, ROP 직접 범위의 근거로 쓰지 않는다(9절). [추정][^ref-1023] ARC mind 는 웹 개발자가 로봇 서비스를 만들게 한다는 점에서 개발자에게 여는 인터페이스의 예다. [추정] 벤더 주장[^ref-1023]

## 6. 대표 접근법과 기술

이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1027][^ref-308][^ref-304][^ref-1031][^ref-004][^ref-1025][^ref-1024]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-10-09-area41-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다(구축자 의견). [의견][^ref-004][^ref-937][^ref-031][^ref-1025][^ref-1024][^ref-304]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area41-s7.md)에 있다.

## 8. 대표 연구와 자료

판단 배치와 장애 대응의 근거는 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구이며, 모두 논문 초록 기준이다. [사실][^ref-304][^ref-1031][^ref-1027][^ref-308]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료](../../topics/2026/2026-09-30-area41-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처, 작업 요청·작업 상태·플릿 상태의 기계가독 스키마, REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기, API 호출의 인증·권한, 그리고 판단·데이터를 로봇·현장 서버·클라우드 가운데 어디에 둘지 정하는 배치 정책으로 보인다. [추정][^ref-004][^ref-937][^ref-1028][^ref-031][^ref-1025][^ref-1024][^ref-762]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터로 로봇·제조사 관제의 기능·상태를 주고받는 인터페이스와 판단 배치 정책. [추정][^ref-004] | 연계 대상: 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능은 로봇 제조사가 맡는다. FogROS2 같은 오프로딩은 로봇 내부 기능의 실행 위치 선택이다. [추정][^ref-304][^ref-1027] |
| 상위 업무 시스템 | 업무 시스템이 부르는 외부 API(요청 수신·결과 회신)와 그 인증·권한. [추정][^ref-762][^ref-1030] | 연계 대상: 주문·재고 같은 업무 판단은 WMS·ERP 가 맡는다. [추정][^ref-1030] |

클라우드 제공자 인프라는 외부 연계 대상이고, 현장 네트워크 설계는 ROP 의 다른 세부영역인 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)에서 다룬다. [추정][^ref-1031][^ref-1030]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

네이버가 밝힌 ARC 처럼 위치 추정·이동 계획까지 클라우드에 두는 설계는 위 경계를 제품 전략으로 옮긴 사례이며, 이종 제조사를 연결하는 ROP 의 직접 범위로 보지 않는다. [추정] 벤더 주장[^ref-1023] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

### 전달 보장과 외부 API 의 인증·권한 범위 (2026-10-09 갱신)

로봇–관제 표준인 VDA 5050 3.0.0 은 외부 IT 시스템과의 인터페이스와 사이버보안 조치를 범위 밖에 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 사이버보안은 [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md), 안전 요구는 [M. 안전](../safety/index.md) 쪽에서 다루며 이 영역에서는 표준 범위 밖이라는 사실만 적는다.

- **외부 이벤트 전달 보장**: VDA 5050 은 주문 갱신 번호(orderUpdateId)로 재전송·순서 문제를 다루지만 대부분 주제에 QoS 0 최선 노력 전달을 쓰고 외부 IT 시스템 인터페이스를 범위 밖에 둔다. 그래서 업무 시스템에 내보내는 웹훅·이벤트의 전달 보장(재시도·순서·중복 제거)은 ROP 의 외부 API 가 따로 정해야 할 것으로 보인다(구축자 판단, oq-208 부분 근거). [추정][^ref-031]
- **외부 API 의 인증·권한 범위**: rmf-web API 서버는 README 기준으로 권한 그룹 결정이 미구현이고 사용자 해지가 신원 제공자에 달려 있다. 그래서 Open-RMF 웹 API 를 ROP 외부 API 의 기반으로 쓰면 고객·현장별 자원 구분과 외부 계정 해지를 ROP 가 신원 제공자 연동과 권한 그룹 규칙으로 직접 채워야 할 것으로 보인다(구축자 판단). [추정][^ref-762] 고객·현장 격리 자체는 [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)에서 다룬다.
- **연결이 끊긴 동안의 실행**: 연계 대상: 로봇 자체 지능·제어 — 연결이 끊긴 로봇이 base(관제가 해제한 노드·엣지 구간)의 끝까지 수행하는 동작과 위치 추정·경로 실행은 로봇 쪽 기능이다. [사실][^ref-031] ROP 몫은 base·horizon 을 얼마나 해제할지 정하는 정책과 그 인터페이스로 한정되는 것으로 보인다(구축자 판단). [추정][^ref-031]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 같은 K. 플랫폼 아키텍처·인프라의 네트워크·데이터 영역, F. 연동의 네 영역, 보안·관제·복구 영역, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1031][^ref-004]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md)에 있다.

## 11. 열린 질문

판단 배치의 단절 대응, 외부 API 의 수명주기와 전달 보장, 국내 표준 여부가 아직 확인되지 않았다.

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 열린 질문](../../topics/2026/2026-10-09-area41-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md) — 섹션 3~11 신규 작성(seed → draft): 판단 배치 혼합 구조, 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건. 1차 조건부 승인 수정 17건과 2차 수정 5건(3절 일반화 2건 좁힘, 4절 도입 단락, [의견] 주체 표시, 약어 풀이) 이행 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-09-30-area41-s6.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "6. 대표 접근법과 기술" 절(3,254자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어](../../topics/2026/2026-09-30-area41-s4.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "4. 핵심 개념과 용어" 절(1,132자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area41-s7.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "7. 관련 표준·프레임워크·오픈소스" 절(962자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(879자)을 옮겼다 (실행 2026-09-30-05)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1027]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1028]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30
```

### runs/2026-10-09-17/pages/topics/2026/2026-10-09-area41-s6.md

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
created: 2026-10-09
updated: 2026-10-09
sources: [ref-004, ref-031, ref-1024, ref-1025, ref-1027, ref-1031, ref-304, ref-308]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#6
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술

# 41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1027][^ref-308][^ref-304][^ref-1031][^ref-004][^ref-1025][^ref-1024]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1027][^ref-308][^ref-304][^ref-1031][^ref-004][^ref-1025][^ref-1024]


### 연결이 끊길 때 판단을 어디에 두는가 (2026-10-09 갱신)

로봇–관제 인터페이스인 [VDA 5050](../../glossary/vda-5050.md) 3.0.0 은 무선망에서 연결 끊김과 메시지 손실이 생길 수 있다는 것을 통신 전반의 전제로 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 연계 대상: 로봇 자체 지능·제어 — 이 명세에서 브로커와 연결이 끊긴 로봇은 주문 정보를 유지하고 base(관제가 해제(released)한 노드·엣지 구간. 용어집의 [해제 구역](../../glossary/release-zone.md)과는 다른 개념)의 마지막 노드까지 주문을 수행한다. [사실][^ref-031] 같은 명세는 [메시지 큐잉 원격 측정 전송](../../glossary/mqtt.md)(Message Queuing Telemetry Transport, MQTT)이 비동기이고 무선 전송을 믿을 수 없으므로 관제가 이미 해제한 base 를 바꿀 수 없고 실행된 것으로 간주해야 하며, 주문 취소([cancelOrder](../../glossary/vda-5050-cancel-order.md))도 같은 이유로 신뢰할 수 없다고 본다. [사실][^ref-031]

VDA 5050 3.0.0 은 판단을 관제와 로봇으로 나눈다. 관제의 최소 기능으로는 주문 배정, 선 유도(line-guided) 로봇의 경로 계산·안내, 교착 탐지·해소, 에너지 관리, 교통 통제, 문·게이트·승강기 같은 주변 시스템과의 통신, 통신 오류 탐지·해소를 든다. [사실][^ref-031] 명세는 관제에 교통 통제 기능을 요구하되 그 로직은 정하지 않고 범위 밖에 둔다. [사실][^ref-031] 연계 대상: 로봇 자체 지능·제어 — 위치 추정·경로 실행·동작 실행·상태 연속 전송은 같은 명세가 로봇의 기능으로 드는 것이다. [사실][^ref-031]

Open-RMF 의 교통 일정은 플랫폼 중립의 중앙 데이터베이스로, 배치된 모든 플릿 관리자가 예상 경로를 보고하고, 충돌이 예상되면 플릿 관리자들이 협상하며 시스템 통합사가 둔 제3자 판정자가 제안을 고른다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004] 긴급 작업은 의도적으로 충돌을 올려 협상을 강제할 수 있다. [사실][^ref-004] 교통 조율 자체의 본론은 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)에서 다루고, 이 영역에서는 중앙 조율을 어디에 둘지 정하는 근거로만 쓴다.

두 자료를 함께 보면, ROP 의 판단 배치 정책은 중앙 조율 서비스를 클라우드와 현장 서버 가운데 어디에 둘지와 함께, 연결이 끊긴 동안 로봇이 계속 갈 수 있는 base 의 길이를 정해야 할 것으로 보인다(구축자 판단, oq-206 부분 근거). [추정][^ref-031][^ref-004] base 의 길이는 관제의 교통 통제 기능에 걸치므로 27. 다중 로봇 경로·교통 관리 — MAPF와 [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)에서 함께 다룬다.

### 메시지 전달 보장 수준 (2026-10-09 갱신)

VDA 5050 3.0.0 은 통신 부하를 줄이려고 order·instantActions·state·factsheet·zoneSet·responses·visualization 주제에는 MQTT 서비스 품질(Quality of Service, QoS) 0(최선 노력)을, connection 주제에는 QoS 1(최소 한 번)을 쓰게 한다. [사실][^ref-031] 로봇이 예기치 않게 끊기면 브로커가 [유언 메시지](../../glossary/mqtt-last-will.md)(last will)로 다른 구독자에게 알린다. [사실][^ref-031]

주문 갱신은 같은 orderId 에 orderUpdateId 를 늘려 보낸다. [사실][^ref-031] 로봇은 같은 orderUpdateId 로 같은 내용이 다시 오면 무시하고, 내용이 다르면 SAME_ORDER_UPDATE_ID, 더 낮은 orderUpdateId 면 OUTDATED_ORDER_UPDATE 경고를 보고해 재전송과 순서 뒤바뀜을 메시지 수준에서 걸러낸다. [사실][^ref-031] 명령 실행 신뢰성의 본론은 [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md)에서 다룬다.

클라우드 브로커를 쓸 때 VDA 5050 3.0.0 은 클라우드 사업자가 강제하는 주제 구조가 있으므로 MQTT 주제 단계 구조를 엄격히 정하지 않는다. [사실][^ref-031] 클라우드 브로커는 구조를 개별 조정할 수 있으나 제안 구조를 대략 따라야 하며, 주제 이름(order·state 등)은 필수다. [사실][^ref-031]

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

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-1027]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-17 | 41. 플랫폼 아키텍처·외부 API 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-09-17/pages/topics/2026/2026-10-09-area41-s7.md

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
created: 2026-10-09
updated: 2026-10-09
sources: [ref-004, ref-031, ref-1024, ref-1025, ref-304, ref-762, ref-937]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md#7
---

[홈](../../index.md) › [주제](../index.md) › 41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스

# 41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다(구축자 의견). [의견][^ref-004][^ref-937][^ref-031][^ref-1025][^ref-1024][^ref-304]
- 이 페이지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다(구축자 의견). [의견][^ref-004][^ref-937][^ref-031][^ref-1025][^ref-1024][^ref-304]


### 버전 규칙·범위와 오픈소스 API 의 현재 서술 (2026-10-09 갱신)

- **VDA 5050 3.0.0** — [의미적 버전 관리](../../glossary/semantic-versioning.md)를 써서 주 버전(x.0.0)은 대체로(typically) 새 필수 필드 도입 같은 하위 호환을 깨는 변경, 부 버전(3.x.0)은 선택 매개변수 추가 같은 새 기능, 수 버전(3.0.x)은 문서 오탈자 같은 작은 수정에 쓴다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] VDA 5050 3.0.0 이 지역(local) 브로커용으로 제안하는 주제 구조에서는 MQTT 주제 경로에 'v' 를 붙인 주 버전(예 v3)을 넣는다. 이 주제 구조는 엄격한 규정이 아니며 클라우드 브로커는 조정할 수 있다(6절). [사실][^ref-031] 명세는 주변 설비·기반 시설·외부 IT 시스템과의 인터페이스, 안전 요구사항, 교통 관리 로직, 운영 책임 배분, 사이버보안 조치를 범위 밖에 둔다. [사실][^ref-031]
- **Open-RMF 플릿 어댑터** — Open-RMF 핵심 문서는 플릿 어댑터를 [플릿 제어 수준](../../glossary/fleet-control-level.md) 네 가지(Full Control·Traffic Light·Read Only·No Interface)로 나누고, Full Control 에는 재사용 C++ API(파이썬 바인딩 포함)를 제공한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004] 같은 문서인 Open-RMF 책 rmf-core 장(작성 시점 미확인)은 Read Only 용 예비 ROS 2 메시지 API 가 향후 판에서 C++ API 로 대체되어 폐기될 예정이고 Traffic Light 용 재사용 API 는 아직 구현되지 않았다고 서술하지만, 이는 책의 서술이며 현재 배포판의 상태는 미확인이다. [추정][^ref-004]
- **Open-RMF rmf-web API 서버** — 주제 페이지에 있는 기존 서술(신원 제공자 기반 인증, 역할·동작·권한 그룹 판정)에 더해, 2026-10-09 확인한 README 에는 OAuth 2.0 client_credentials(기계 간, M2M) 흐름에서 신원 제공자가 표준 클레임을 빼고 네임스페이스 붙은 클레임만 주는 경우를 위한 선택 설정 preferred_username_claim_namespace 가 있다. [사실][^ref-762] README 의 TODO 절 기준으로, 자원의 권한 그룹을 정하는 방식이 아직 정해지지 않아 현재는 모든 자원이 기본 빈 그룹('')에 들어간다(코드 동작으로는 확인하지 않음). [사실][^ref-762] 서버는 자체 사용자·역할·권한 데이터베이스를 신원 제공자와 동기화하지 않으므로, rmf-server 에서 사용자를 지워도 로그인만 요구하는 반보호 API 접근은 막지 못하고 로그인 자체를 막으려면 신원 제공자에서 사용자를 지워야 한다. [사실][^ref-762] 역방향 프록시 뒤에서 쓸 때는 public_url 을 공개 주소로 설정하고 프록시가 경로 접두어를 제거하게 해야 한다. [사실][^ref-762]

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

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-17 | 41. 플랫폼 아키텍처·외부 API 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-17/pages/topics/2026/2026-10-09-area41-s11.md

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
created: 2026-10-09
updated: 2026-10-09
sources: [ref-004, ref-031, ref-1031, ref-762]
last_run: 2026-10-09
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


### 부분 근거와 새 질문 (2026-10-09 갱신)

아래 질문은 이번 실행에서 부분 근거만 얻었으므로 모두 열림 상태를 유지한다.

- **oq-206** (상태: 열림) 클라우드 연결이 끊길 때 로봇과 현장 서버가 어디까지 계속 동작하는가 — VDA 5050 의 base 끝까지 수행과 Open-RMF 의 중앙 교통 일정을 함께 보면, 중앙 조율 위치와 base 길이를 함께 정해야 할 것으로 보인다(6절, 구축자 판단). [추정][^ref-031][^ref-004] 네이버 ARC 의 끊김 동작은 여전히 미확인이다.
- **oq-207** (상태: 열림) 외부 API 의 버전 관리·폐기 예고 정책 — 이번에 확인한 두 출처(VDA 5050 3.0.0 명세, Open-RMF 책 rmf-core 장)에서는 버전 표기 규칙과 '향후 판에서 폐기' 같은 예고 문구는 있으나 폐기 예고 기간이나 구판 지원 기간은 정하지 않는다. [추정][^ref-031][^ref-004] 관련 개념은 용어집 [API 폐기 정책](../../glossary/api-deprecation-policy.md)에 있다.
- **oq-208** (상태: 열림) 웹훅·이벤트의 전달 보장 공통 기준 — 로봇–관제 쪽은 QoS 0·1 구분과 orderUpdateId 로 일부를 다루지만 외부 IT 인터페이스는 범위 밖이어서, 외부 이벤트 전달 보장은 ROP 가 정해야 할 것으로 보이며 공통 기준은 확인되지 않았다(9절, 구축자 판단). [추정][^ref-031]
- **oq-300** (상태: 열림) 재시작 뒤 진행 중 작업 상태 유지 — FogROS2-FT 의 다중 클라우드 복제는 상태 없는(stateless) 로봇 서비스를 대상으로 하므로, 이 방법만으로는 답이 되지 않는 것으로 보인다. [추정][^ref-1031]
- **새 질문** (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-17) Open-RMF 웹 API 서버처럼 권한 그룹 자동 결정이 미구현인 오픈소스 관제 API 위에서 고객·현장별 자원 격리를 API 수준으로 구현한 공개 사례나 설계 문서가 있는가? 근거는 README TODO 절의 빈 권한 그룹 서술이다. [사실][^ref-762]
- oq-209(국내 TTA·KS 참조 구조 표준), oq-267(과금 단위), oq-301(OpenAPI·AsyncAPI 기반 적합성 시험 도구)은 이번 실행에서 조사하지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

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

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-17 | 41. 플랫폼 아키텍처·외부 API 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-17/verification2.json

```json
{
  "run_id": "2026-10-09-17",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": true,
    "overlaps": []
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
    "6·7·11절 기존 주제 페이지 링크 유실(1차 수정 지시 19 '기존 요약 문장과 주제 페이지 링크를 지우지 않는다' 미이행): 자동 분리 뒤 세부영역 6·7·11절은 새 주제 페이지(2026-10-09-area41-s6·s7·s11)만 가리킨다. 새 주제 페이지 3. 본문에도 기존 주제 페이지 [2026-09-30-area41-s6](../../topics/2026/2026-09-30-area41-s6.md)·[2026-09-30-area41-s7](../../topics/2026/2026-09-30-area41-s7.md)·[2026-09-30-area41-s11](../../topics/2026/2026-09-30-area41-s11.md)로 가는 링크가 없다. 그래서 2026-09-30 에 검증된 상세 서술이 세부영역 페이지에서 끊긴다. 6·7·11절의 append 패치마다 갱신 소절 첫머리에 '이전 서술은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — <절 이름>](../../topics/2026/2026-09-30-area41-s<n>.md)에 있다'는 링크 문장을 넣는다. 세부영역 폴더와 docs/topics/2026/ 은 깊이가 같으므로 이 상대 경로는 분리 뒤에도 유효하다.",
    "7절(주제 페이지 2026-10-09-area41-s7) rmf-web 항목: '주제 페이지에 있는 기존 서술(신원 제공자 기반 인증, 역할·동작·권한 그룹 판정)'에 링크가 없어 어느 페이지인지 알 수 없다. 이 문구를 [기존 주제 페이지](../../topics/2026/2026-09-30-area41-s7.md) 링크로 바꾼다.",
    "분리된 주제 페이지 안의 절 참조가 모호하다. s7 의 '(6절)', s11 의 '(6절, 구축자 판단)'·'(9절, 구축자 판단)'은 주제 페이지 자신의 6절(연결되는 연구영역)로 읽힌다. 6절 참조는 [대표 접근법과 기술](2026-10-09-area41-s6.md) 링크로, 9절 참조는 '41. 플랫폼 아키텍처·외부 API 페이지 9절' 처럼 원 페이지를 밝혀 고친다.",
    "f1(1차 수정 지시 1 일부 미이행): 7절 VDA 5050 항목에서 '대체로(typically)'는 주 버전에만 붙어 있다. 1차 지시와 메모(원문의 typically·generally·usually 를 살린다)에 맞게 부 버전·수 버전 설명에도 '대체로'와 같은 한정어를 붙인다.",
    "세부영역 페이지 프런트매터: last_run 이 2026-09-30 그대로다. 이번 실행으로 갱신했으므로 2026-10-09 로 고친다. 주제 페이지 세 건과 같은 값이 되어야 한다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 18건, 미확인 0건, 교차 확인 0건. 강등: f9 사실 → 추정(Read Only API 폐기 예정과 Traffic Light 재사용 API 미구현 부분. Open-RMF 책 rmf-core 장은 작성 시점이 미확인이고 표와 본문이 어긋난다. 검증 시점의 Open-RMF rmf_ros2 API 문서에는 EasyTrafficLight 가 있다). 원문 미열람 출처: ref-1031(브리프 기준. 검증자가 2026-10-09 arXiv 초록에서 '상태 없는 로봇 서비스 복제' 서술을 확인함). 주의: 사실 finding 13건은 모두 단일 출처다(VDA 5050 3.0.0 명세 ref-031, Open-RMF 문서 ref-004·ref-762). 9절에 더한 외부 이벤트 전달 보장(f8)과 외부 API 의 인증·권한 범위(f15)는 구축자 판단인 [추정]이다. VDA 5050 은 리서치가 앞 48,820자만 읽었다. 검증자가 앞 200,000자까지 확인한 결과 폐기 예고 기간·구판 지원 기간 규정은 없었다(마지막 약 7,700자는 미확인). rmf-web README 의 M2M 설정이 언제 들어갔는지는 확인하지 못했다. 이번 브리프는 검색 0회라 한국어 검색이 없다. 그래서 oq-209·oq-267·oq-301 과 상업 시설·가정·실외 사례는 조사되지 않았다. oq-206·oq-207·oq-208·oq-300 은 부분 근거만 있어 열림을 유지한다. 정정 요청 없음. 2차 결과는 다음과 같다. 드리프트 없음. 1차 수정 지시 19건 가운데 17건은 이행을 확인했다. f9 강등, 벤더 주장 없음, base 와 해제 구역의 구분, 플릿 제어 수준 표기, 51·52·29·27·42 연결, ref-1031 접근일 유지가 여기에 든다. [분류원문] 보존, 섹션 순서 준수. 다만 분리된 6·7·11절에서 2026-09-30 주제 페이지로 가는 링크가 사라졌다(지시 19 미이행). f1 의 '대체로' 한정어는 일부만 반영됐다. 분리 주제 페이지 안의 절 참조가 모호하고 세부영역 last_run 이 갱신되지 않았다. 이 다섯 가지를 고쳐 재검증한다. 자동 분리 코드가 '자세한 내용은 주제 페이지 …' 링크 줄을 옮기지 않았을 가능성이 있다. pipeline 담당이 분리 처리에서 기존 링크 줄을 보존하는지 확인해야 한다. 용어 'MQTT 서비스 품질 수준'은 기존 'mqtt' 항목과 중복인지 아직 확인되지 않았다(additional_research_requests 에 올라 있음).",
  "retry_reason": null
}
```


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 6·7·11절 기존 주제 페이지 링크 유실(1차 수정 지시 19 '기존 요약 문장과 주제 페이지 링크를 지우지 않는다' 미이행): 자동 분리 뒤 세부영역 6·7·11절은 새 주제 페이지(2026-10-09-area41-s6·s7·s11)만 가리킨다. 새 주제 페이지 3. 본문에도 기존 주제 페이지 [2026-09-30-area41-s6](../../topics/2026/2026-09-30-area41-s6.md)·[2026-09-30-area41-s7](../../topics/2026/2026-09-30-area41-s7.md)·[2026-09-30-area41-s11](../../topics/2026/2026-09-30-area41-s11.md)로 가는 링크가 없다. 그래서 2026-09-30 에 검증된 상세 서술이 세부영역 페이지에서 끊긴다. 6·7·11절의 append 패치마다 갱신 소절 첫머리에 '이전 서술은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — <절 이름>](../../topics/2026/2026-09-30-area41-s<n>.md)에 있다'는 링크 문장을 넣는다. 세부영역 폴더와 docs/topics/2026/ 은 깊이가 같으므로 이 상대 경로는 분리 뒤에도 유효하다.
    - 7절(주제 페이지 2026-10-09-area41-s7) rmf-web 항목: '주제 페이지에 있는 기존 서술(신원 제공자 기반 인증, 역할·동작·권한 그룹 판정)'에 링크가 없어 어느 페이지인지 알 수 없다. 이 문구를 [기존 주제 페이지](../../topics/2026/2026-09-30-area41-s7.md) 링크로 바꾼다.
    - 분리된 주제 페이지 안의 절 참조가 모호하다. s7 의 '(6절)', s11 의 '(6절, 구축자 판단)'·'(9절, 구축자 판단)'은 주제 페이지 자신의 6절(연결되는 연구영역)로 읽힌다. 6절 참조는 [대표 접근법과 기술](2026-10-09-area41-s6.md) 링크로, 9절 참조는 '41. 플랫폼 아키텍처·외부 API 페이지 9절' 처럼 원 페이지를 밝혀 고친다.
    - f1(1차 수정 지시 1 일부 미이행): 7절 VDA 5050 항목에서 '대체로(typically)'는 주 버전에만 붙어 있다. 1차 지시와 메모(원문의 typically·generally·usually 를 살린다)에 맞게 부 버전·수 버전 설명에도 '대체로'와 같은 한정어를 붙인다.
    - 세부영역 페이지 프런트매터: last_run 이 2026-09-30 그대로다. 이번 실행으로 갱신했으므로 2026-10-09 로 고친다. 주제 페이지 세 건과 같은 값이 되어야 한다.
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 18건, 미확인 0건, 교차 확인 0건. 강등: f9 사실 → 추정(Read Only API 폐기 예정과 Traffic Light 재사용 API 미구현 부분. Open-RMF 책 rmf-core 장은 작성 시점이 미확인이고 표와 본문이 어긋난다. 검증 시점의 Open-RMF rmf_ros2 API 문서에는 EasyTrafficLight 가 있다). 원문 미열람 출처: ref-1031(브리프 기준. 검증자가 2026-10-09 arXiv 초록에서 '상태 없는 로봇 서비스 복제' 서술을 확인함). 주의: 사실 finding 13건은 모두 단일 출처다(VDA 5050 3.0.0 명세 ref-031, Open-RMF 문서 ref-004·ref-762). 9절에 더한 외부 이벤트 전달 보장(f8)과 외부 API 의 인증·권한 범위(f15)는 구축자 판단인 [추정]이다. VDA 5050 은 리서치가 앞 48,820자만 읽었다. 검증자가 앞 200,000자까지 확인한 결과 폐기 예고 기간·구판 지원 기간 규정은 없었다(마지막 약 7,700자는 미확인). rmf-web README 의 M2M 설정이 언제 들어갔는지는 확인하지 못했다. 이번 브리프는 검색 0회라 한국어 검색이 없다. 그래서 oq-209·oq-267·oq-301 과 상업 시설·가정·실외 사례는 조사되지 않았다. oq-206·oq-207·oq-208·oq-300 은 부분 근거만 있어 열림을 유지한다. 정정 요청 없음. 2차 결과는 다음과 같다. 드리프트 없음. 1차 수정 지시 19건 가운데 17건은 이행을 확인했다. f9 강등, 벤더 주장 없음, base 와 해제 구역의 구분, 플릿 제어 수준 표기, 51·52·29·27·42 연결, ref-1031 접근일 유지가 여기에 든다. [분류원문] 보존, 섹션 순서 준수. 다만 분리된 6·7·11절에서 2026-09-30 주제 페이지로 가는 링크가 사라졌다(지시 19 미이행). f1 의 '대체로' 한정어는 일부만 반영됐다. 분리 주제 페이지 안의 절 참조가 모호하고 세부영역 last_run 이 갱신되지 않았다. 이 다섯 가지를 고쳐 재검증한다. 자동 분리 코드가 '자세한 내용은 주제 페이지 …' 링크 줄을 옮기지 않았을 가능성이 있다. pipeline 담당이 분리 처리에서 기존 링크 줄을 보존하는지 확인해야 한다. 용어 'MQTT 서비스 품질 수준'은 기존 'mqtt' 항목과 중복인지 아직 확인되지 않았다(additional_research_requests 에 올라 있음).

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
