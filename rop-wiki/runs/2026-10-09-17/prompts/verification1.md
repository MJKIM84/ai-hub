(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

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

### docs/categories/planning-and-business/technology-market-and-vendor-trends.md (요약)

```markdown
# 1. 기술·시장·업체 동향

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **기술·연구 동향 조사**: 카테고리마다 논문·기사·업체 발표를 모아 연구와 제품의 흐름을 추적한다
- **시장·업체·제품 지형**: 오케스트레이션·관제·상호운용 제품, 로봇 제조사, 통합 사업자의 지형을 정리한다
- **로봇 종류·형태 지형**: AMR·AGV·로봇팔·모바일 매니퓰레이터·사족 보행·휴머노이드·드론처럼 오케스트레이션 대상 로봇의 종류와 특성 변화를 추적한다

## 2. 핵심 질문

어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md (요약)

```markdown
# 32. 예외 복구·재계획·업무 연속성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

고장·통신 단절·누락에 대한 복구와 제한 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **예외 복구**: 고장·통신 단절·물품 누락·긴급 요청에 재배정·우회·수동 처리·제한 운영을 결정한다
- **제한 운영·업무 연속성**: 일부 장비가 멈춰도 업무를 이어 가는 운영 수준과 절차를 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 20번 영역 ‘예외 복구·재계획·업무 연속성’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [옛 분류원문]

> 옛 질문: 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [옛 분류원문]

## 2. 핵심 질문

작업 중 로봇이 고장 나면 남은 일은 누가 어떻게 이어받는가? [분류원문]
```

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md (요약)

```markdown
# 37. 관제 화면·실행 기록

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
```

### docs/categories/security-and-privacy/authentication-authorization-and-isolation.md (요약)

```markdown
# 51. 인증·권한·격리

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장비·사용자 인증**: 로봇·설비·사용자를 인증한다
- **명령 권한 관리**: 누가 어느 로봇에 어떤 명령까지 내릴 수 있는지 정하고 강제한다
- **원격 접속·유지보수 계정**: 외부 유지보수 계정이 접속할 수 있는 범위와 기록을 관리한다
- **고객·현장 격리**: 고객·현장·방문자별로 데이터와 제어를 분리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 26번 영역 ‘사이버보안·접근권한·개인정보’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [옛 분류원문]

> 옛 질문: 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [옛 분류원문]

## 2. 핵심 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
```

### docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md (요약)

```markdown
# 52. 통신 보호·위협 관리·감사

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **통신 보호**: 로봇·플랫폼·설비 사이 통신을 암호화하고 무결성을 지킨다(ROS 2 보안 등)
- **보안 위협 모델·취약점 관리**: 위협 모델을 세우고 취약점을 찾아 고친다(ROS 2 위협 모델, IEC 62443 등)
- **문서·대화 입력 보안**: 문서나 대화에 숨은 지시를 명령으로 실행하지 않게 막는다(프롬프트 주입 방지)
- **명령·승인 감사 기록**: 누가 언제 무엇을 지시·승인·변경했는지 지울 수 없게 기록한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? [분류원문]
```

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
```

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/other-sites.md (요약)

```markdown
# 67. 기타 현장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
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

### runs/2026-10-09-16/research.md

```markdown
# 리서치 브리프 2026-10-09-16

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-16 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 38. 모니터링·이상 탐지·원인 분석 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 보고 어휘를 '같은 시간축에 맞춘다'고만 적었고, 표준마다 시각 형식·심각도 등급·연결 상태 표현이 어떻게 다른지에 대한 근거가 없음
- 섹션 5. 적용 사례 (현장 유형 명시) — 개정 전에 쓴 물류창고 가상 시나리오 1건뿐이고 병원·상업 시설·실외·기타 현장 사례가 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 운용 모드·information 사용 제한·연결 상태(HIBERNATING), MassRobotics 오류 코드 형식, Open-RMF 배차 오류·개입 기록이 정리되지 않음(주제 페이지로 분리된 절)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 로봇 내부 진단(ROS 2 diagnostics)과 플랫폼 수준 원인 판정의 경계 근거가 README 수준 한 줄뿐
- 섹션 11. 열린 질문 — oq-033·oq-073·oq-074·oq-075·oq-210 에 대한 부분 근거 미정리
- 정정 요청 없음. 바뀐 출처 확인 대상은 입력으로 들어온 원문 텍스트(ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447)

## 조사 질문

1. 지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]
2. oq-033·oq-073 VDA 5050·MassRobotics·Open-RMF 는 오류 심각도·작업 상태·운용 상태를 각각 어떤 값과 형식으로 보고하며, 공통 어휘로 옮길 때 무엇이 어긋나는가? (섹션 3·7·11 겨냥)
3. 통신 원인을 로봇·설비 원인과 구분하는 데 쓸 수 있는 표준 신호(연결 상태, 메시지 순번, 마지막 유언 메시지)는 무엇인가? (섹션 3·7 겨냥)
4. oq-210 플랫폼 서비스의 분산 추적과 로봇 상태 메시지를 하나의 작업 식별자로 이을 수 있는 표준 필드는 무엇인가? (섹션 6·7·11 겨냥)
5. 로봇 내부 진단(센서·드라이버)과 플랫폼 수준 원인 판정의 경계는 어디인가? (섹션 9 겨냥)
6. oq-074·oq-075 병원·상업 시설·실외·기타 현장에서 로봇 정지·지연·실패의 원인이나 이상 감시 방식이 공개된 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 state 스키마는 로봇의 활성 오류 전체를 담는 errors 배열, 운용 모드(operatingMode), 안전 상태(safetyState)를 필수 항목으로 두고, 운용 모드 값을 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 가지로 정한다. | ref-051 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 state 스키마는 로봇이 보내는 부가 정보 배열(information)을 시각화·디버깅에만 쓰고 플릿 관제의 판단 로직에는 쓰지 않도록 정하므로, 원인 판정 규칙은 errors·operatingMode 같은 정해진 필드에 기대야 한다. | ref-051 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 은 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고 오류마다 사람이 읽는 설명(errorDescription)과 조치 힌트(errorHint)를 담을 수 있게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 connection 스키마는 연결 상태를 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 으로 나누어, 로봇이 질서 있게 끊으면 OFFLINE 을, 예기치 않게 끊기면 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리고, HIBERNATING 은 연결은 살아 있으나 상태 메시지를 보내지 않는 절전·통신 감축 모드로 정한다. | ref-449 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | MassRobotics AMR 상호운용 표준의 statusReport 는 운용 상태를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 두고, 오류는 심각도 필드 없이 문자열 목록(errorCodes)으로만 보고하며 정상 운용 때는 생략하게 한다. | ref-230 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f6 | [사실] | Open-RMF 작업 상태 스키마는 작업 상태 12개(blocked·error·failed·delayed 등)와 별도로 배차 상태(failed_to_assign 포함)와 배차 오류 배열을 두고, 일시정지(interruptions)·재개(resumed_by)·취소·강제 종료 요청마다 요청 시각과 라벨을 남겨, 지연이 배정 실패인지 실행 중 차단인지 사람 개입인지를 기록에서 나눠 볼 수 있다. | ref-111 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f7 | [사실] | Open-RMF 경보 메시지(Alert)는 심각도를 INFO·WARNING·ERROR 세 등급으로 두고 운영자 응답 목록(responses_available), 관련 작업 id, 화면 표시 여부를 담는다. | ref-448 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f8 | [사실] | 오늘 기준 Open-RMF 문 모드 메시지는 여전히 closed·moving·open·offline·unknown 다섯 값이고, 문 어댑터는 문 노드에 직접 보낸 요청을 무효로 돌려 진행 중 로봇 작업을 방해하지 않게 하는 상태 감독자 역할을 하므로, 페이지 5절의 문 관련 서술은 그대로 유효하다. | ref-313, ref-283 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f9 | [추정] | 오류 심각도 표현이 VDA 5050 3.0.0 은 네 단계, Open-RMF 경보는 세 등급, MassRobotics 상태 보고는 등급 없는 문자열 목록으로 서로 달라, 38. 모니터링·이상 탐지·원인 분석에서 이종 플릿의 이상을 한 경보 체계로 모으려면 ROP 가 심각도 대응 규칙을 따로 정해야 할 것으로 보인다(oq-033·oq-073 부분 근거). | ref-031, ref-448, ref-230 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f10 | [사실] | 연계 대상: ROS 2 diagnostics 는 하드웨어 드라이버·로봇 하드웨어의 진단 정보를 /diagnostics 토픽으로 모아 aggregator 로 묶고 원격 기록 도구로 외부 저장소(예: InfluxDB)에 넘기는 로봇 내부 진단 체계이므로, ROP 는 이 결과를 원인 범주 판정의 입력으로 받는 쪽에 선다. | ref-445 | 아니오 | medium | 2026-10-09 | 수행 자원 | — |
| f11 | [사실] | OpenTelemetry 명세는 분산 추적을 하나의 논리적 동작에서 비롯된 사건들을 프로세스·네트워크 경계를 넘어 모은 것으로 정의하고, 16바이트 TraceId 로 여러 프로세스의 span 을 묶으며, 일괄 처리처럼 여러 요청에서 시작된 작업은 span 간 링크(Links)로 잇게 한다. | ref-447 | 아니오 | medium | 2026-10-09 | — | — |
| f12 | [추정] | Open-RMF 작업 예약 id(booking.id)와 VDA 5050 state 의 orderId 가 각각 작업·주문을 식별하므로, ROP 서비스의 추적 TraceId 와 이 식별자들을 대응해 두면 플랫폼 처리와 로봇 상태 보고를 하나의 작업 기준으로 이어 원인 분석에 쓸 수 있을 것으로 보이나, 이를 정한 표준은 확인하지 못했다(oq-210 부분 근거). | ref-447, ref-111, ref-051 | 아니오 | low | 2026-10-09 | — | — |
| f13 | [추정] | VDA 5050 의 headerId 는 토픽마다 보낸 메시지마다 1씩 늘어나므로 수신 쪽에서 번호가 건너뛰면 메시지 유실을 의심할 수 있고, 연결 상태(CONNECTION_BROKEN·HIBERNATING)와 함께 보면 상태 보고가 끊긴 원인이 통신인지 로봇 쪽 의도된 감축인지 가르는 근거가 될 것으로 보인다. | ref-051, ref-449 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f14 | [사실] | 세 규약의 시각 표현은 VDA 5050 이 ISO 8601 문자열(밀리초까지), MassRobotics 가 date-time 문자열, Open-RMF 작업 상태가 밀리초 유닉스 시각 정수로 서로 다르다. | ref-051, ref-230, ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [추정] | VDA 5050 운용 모드의 INTERVENED·MANUAL, MassRobotics 의 manualOverride·waitingHumanEvent, Open-RMF 작업의 일시정지 라벨이 모두 사람 개입을 표시하므로, 지연 원인 범주에 로봇·설비·통신·앞 작업 외에 사람 개입·대기를 따로 두는 편이 판정에 유리할 것으로 보인다. | ref-051, ref-230, ref-111 | 아니오 | low | 2026-10-09 | 수행 자원 | — |
| f16 | [사실] | 고려대학교 구로병원 연구에서 의약품 배송 로봇의 승강기 호출·탑승은 승강기 가동률 59% 미만 구간에서 성공률 95.52% 였고 실패가 가동률 90% 초과 구간에 몰려, 병원 현장의 로봇 지연·실패 원인으로 설비(승강기) 혼잡이 드러났다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | 원문 미열람 |
| f17 | [사실] | 한림대학교성심병원은 2024-04 기준 7종 73대의 서비스 로봇을 커맨드센터의 통합관제 시스템으로 관리하지만, 이상 탐지·원인 분석 방식이나 원인별 장애 통계는 공개되지 않았다. | ref-944 | 아니오 | low | 2024-04-15 | 병원 / 수행 자원 | 원문 미열람 |
| f18 | [사실] | Equinor 의 이산화탄소 포집·저장 시설에서는 4족 로봇이 계기 판독·밸브 위치 확인·누출 탐지로 설비 이상을 찾고, 현장 운영자가 연구개발 부서 도움 없이 점검 임무를 직접 만든다. | ref-995 | 아니오 | low | 2025-11-21 | 기타 / 작업 대상 | 원문 미열람 |
| f19 | [사실] | 국내 실외이동로봇 운행안전인증은 로봇과 관제장치의 조합을 대상으로 하므로, 실외 현장에서는 관제장치의 감시 기능이 운행 조건의 하나가 된다. | ref-980 | 아니오 | low | 2026-10-09 | 실외 / 제약 | 원문 미열람 |
| f20 | [사실] | 일본 헨나 호텔에서는 객실 음성 비서·짐 운반·프런트 로봇이 기본 질문과 여권 복사 같은 업무를 해내지 못해 직원이 계속 넘겨받아야 했고, 호텔은 로봇 일부를 철수했다. | ref-961, ref-962 | 아니오 | low | 2019-01 | 상업 시설 / 예외·성과 | 원문 미열람 |
| f21 | [추정] | 이번에 확인한 병원·상업 시설·기타 현장 사례는 실패·지연 현상이나 통합관제 운영만 보고하고 원인을 로봇·설비·통신·앞 작업으로 나눈 분류나 원인별 발생 비율은 공개하지 않아, oq-074·oq-075 는 열린 채로 남는 것으로 보인다. | ref-943, ref-944, ref-961 | 아니오 | low | 2026-10-09 | 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-09 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 아니오 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 아니오 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-445 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/ros/diagnostics/blob/ros2/README.md | 아니오 |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 아니오 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 예 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | 기사 | low | 2026-10-09 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 예 |
| ref-995 | Offshore Technology (Eve Thomas) | Equinor's autonomous robotics: inspection 'dogs' and record-holding subsea drones | 2025-11-21 | 기사 | low | 2026-10-09 | https://www.offshore-technology.com/features/equinor-autonomous-robotics/ | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-961 | Responsible AI Collaborative (AI Incident Database) | Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks | 미확인 | 기사 | low | 2026-10-09 | https://incidentdatabase.ai/cite/346/ | 예 |
| ref-962 | Hotel Technology News | Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce | 2019-01 | 기사 | low | 2026-10-09 | https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md | 3, 5, 7, 9, 11 | 갱신(차등): 섹션 3 — '같은 시간축·같은 어휘' 근거로 f14(시각 형식 차이)·f9(심각도 표현 차이)·f13(통신 원인 신호)·f15(사람 개입 범주) 추가 / 섹션 5 — 물류창고 가상 시나리오의 문·작업 상태·경보 서술을 오늘 원문으로 재확인(f6·f7·f8), 현장 유형별 사례를 나눠 추가: 병원 f16(승강기 혼잡 원인)·f17(통합관제, 원인 분석 비공개), 상업 시설 f20, 실외 f19, 기타 f18 / 섹션 7(주제 페이지로 분리된 절의 요약) — VDA 5050 필수 오류·운용 모드·information 제한(f1·f2), 오류 수준(f3), 연결 상태(f4), MassRobotics 오류 코드 형식(f5), Open-RMF 배차 오류·개입 기록(f6), OpenTelemetry 추적·링크(f11) / 섹션 9 — 로봇 내부 진단은 연계 대상(f10), 심각도 대응 규칙과 작업 식별자 연결은 직접 범위 후보(f9·f12) / 섹션 11 — oq-033·oq-073 부분 근거(f9), oq-210 부분 근거(f12), oq-074·oq-075 미해결(f21), 새 질문 2건. 다음 실행 후보: 37. 관제 화면·실행 기록(f7 경보), 22. 설비·건물 시스템 연동(f16). |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 연결 상태 | Connection State (VDA 5050 connectionState) | VDA 5050 에서 로봇과 메시지 브로커 사이 연결을 ONLINE·OFFLINE·HIBERNATING·CONNECTION_BROKEN 가운데 하나로 알리는 값이며, 예기치 않은 끊김은 유언 메시지로 전달된다. |
| 경보 등급 | Alert Tier (Open-RMF Alert) | Open-RMF 경보 메시지가 운영자에게 보내는 경보의 심각도를 INFO·WARNING·ERROR 세 단계로 나타내는 필드다. |

## 열린 질문

새로 생긴 질문:

- MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 21. 상호운용 표준·적합성 | 근거: f9 | 종류: 일반
- VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f13 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 0건
- 미확인 항목:
    - oq-033·oq-073 미해결: 세 규약 사이의 공식 대응표는 원문 어디에도 없음(f9 는 도출)
    - oq-210 부분 근거만: 작업 식별자와 추적 TraceId 를 잇는 표준 미확인(f12)
    - oq-074·oq-075 미해결: 원인별 발생 비율 공개 자료 미확인(f21)
    - ref-051 원문 텍스트가 앞 13,220자 발췌라 오류 객체 정의(errorLevel enum)는 이 원문에서 확인하지 못했고 f3 은 ref-031 재인용에 기댐
    - f16 구로병원 전체 성공률 분모 미확인
    - f19 운행안전인증 관제장치 항목의 세부 요건 미확인
    - 제조 공장 현장의 이상 탐지·원인 분석 사례는 이번 브리프에 없음
- 범위 경계 위반 의심:
    - f10: 센서·드라이버 수준 진단은 로봇 자체 지능·제어 경계라 claim 을 '연계 대상: '으로 시작하고 ROP 몫은 결과 수신으로 한정
    - f8·f16: 문 개폐 제어와 승강기 운행 제어는 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 상태 확인·원인 범주 반영
    - f18: 계기 판독·누출 탐지 자체는 로봇 인식 기능(연계 대상)이며 ROP 쪽은 점검 결과를 이상 판정·업무 시스템으로 넘기는 부분만 다뤄야 함
    - f19: 인증 판단은 인증 기관·운영자 쪽이며 실외 현장 제약으로만 반영
- 한계: 재실행 1회차(실행 컨텍스트에 retry_count 가 없어 1회차로 적음). 반려 사유 1(스키마 불일치: f9 가 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts 의 ref-051·ref-449·ref-230·ref-111·ref-448·ref-313·ref-283·ref-445·ref-447, fetched_via inbox)와 이전 브리프(2026-10-09-14, 2026-10-09-15)의 기존 참고문헌만으로 브리프를 다시 구성했다. 새 f9 는 심각도 표현 비교로 [추정]이며 벤더 문서를 근거로 한 finding 은 하나도 없다(vendor_claim 대상 없음). 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1367~ref-1396 은 쓰지 않았다. 재인용한 ref-031·ref-943·ref-944·ref-995·ref-980·ref-961·ref-962 는 이번에 열지 않아 fetched false·source_unopened true 이고 신뢰도는 medium 이하다. 교차 확인 0건. 정정 요청 없음, 우선 지정 질문 없음, 입력 누락 없음. 현장 유형: 병원(f16·f17), 상업 시설(f20), 실외(f19), 기타(f18); 물류창고는 기존 5절 시나리오의 재확인(f6·f7·f8)만, 제조 공장 사례는 없음. L. AI·학습 기술 관련 새 finding 은 없어 47. AI·학습·적응과 모델 운영 연결(oq-315)은 그대로다. 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈을 섞지 않았다. 해결 제안한 열린 질문 없음.
```

### runs/2026-10-09-15/research.md

```markdown
# 리서치 브리프 2026-10-09-15

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-15 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 37. 관제 화면·실행 기록 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 병원 협약 단계 보도 1건뿐이고 물류창고·제조 공장·상업 시설·가정·실외·기타 사례가 '찾지 못했다'로 남아 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — 공통 상태 값 표준이 Open-RMF 작업 상태 스키마뿐이고(oq-237) MassRobotics·VDA 5050 의 상태·오류 수준 정의, 관제실 설계 표준(ISO 11064), 투명성 표준(IEEE 7001)이 없음. rmf-web 저장 설정(바뀐 출처) 확인 필요
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 실행 기록 보관 주체·기간 근거(oq-316, oq-239)와 사고 조사용 최소 기록 항목(oq-252) 없음
- 섹션 11. 열린 질문 — oq-131·oq-237·oq-238·oq-239·oq-240·oq-252·oq-316 해결 근거 미조사
- 정정 요청 없음, 발행 2년이 지난 표준 수치 재확인 대상은 ISA-101 계열(본문 유료, 이번에 재열람하지 않음)

## 조사 질문

1. 운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
2. oq-237 여러 제조사 로봇의 작업 상태·실행 로그를 한 화면·한 기록으로 모을 때 Open-RMF 작업 상태 스키마 말고 공통 상태 값과 로그·오류 수준을 정한 공개 규약이 있는가? (섹션 7·9 겨냥)
3. oq-238·oq-240 설명 가능한 표시를 실제 플릿 관제 화면에서 측정한 연구가 있는가, 다중 로봇 관제 화면에 쓸 수 있는 화면·관제실 설계 표준이나 투명성 표준은 무엇인가? (섹션 7·11 겨냥)
4. oq-252·oq-316·oq-239 사고 조사용 최소 기록 항목, 고위험 AI 자동 사건 기록의 보관 기간·주체, 병원 특수 물품 배송 기록의 국내 보관 요건은 무엇인가? (섹션 9·11 겨냥)
5. 물류창고·실외·가정·기타 현장과 국내 병원에서 여러 로봇을 하나의 관제 화면으로 운영한 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)
6. 바뀐 출처와 oq-131: Open-RMF rmf-web 의 실행 기록 저장 설정은 바뀌었는가, 로봇 물류 실행 기록을 객체 중심 이벤트 로그로 만든 공개 사례가 있는가? (섹션 7·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 로봇이 보고하는 동작 상태 값을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 로, 오류 수준을 WARNING·URGENT·CRITICAL·FATAL 네 단계로 정하고, 오류마다 사람이 읽는 설명(errorDescription)·조치 힌트(errorHint)와 ISO 639-1 언어 코드별 번역을 담을 수 있게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 3.0.0 은 로봇이 state 메시지의 information 배열로 보내는 부가 정보를 플릿 관제가 로직에 쓰지 말고 시각화·디버깅에만 쓰게 하며, logReport 즉시 동작으로 로봇에 로그 보고서 생성·저장을 요청하고 저장된 로그 이름을 동작 상태로 보고받게 한다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [사실] | MassRobotics AMR 상호운용 표준의 statusReport 는 uuid·timestamp·operationalState·location 을 필수로 하고, operationalState 를 navigating·idle·disabled·offline·charging·waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 아홉 값으로 정하며, 오류 코드 배열, 약 10초의 단기 경로(예측 위치 최대 10개), 목적지, 배터리 잔량을 선택 항목으로 둔다. | ref-253 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f4 | [사실] | Open-RMF 작업 상태 스키마는 작업 상태 값 12개와 별도로 배차 상태를 queued·selected·dispatched·failed_to_assign·canceled_in_flight 로 기록하고, 요청자(requester)·예약 라벨과 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다 요청 시각과 라벨(예: dashboard)을 남기게 해, 누가 어떤 창구로 작업에 개입했는지를 실행 기록에 담을 수 있다. | ref-111 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f5 | [추정] | Open-RMF 작업 상태 스키마 말고도 VDA 5050(동작 상태·오류 수준)과 MassRobotics 상호운용 표준(운용 상태)이 공개된 상태 값 집합을 정하지만 세 규약의 값 집합과 단위(작업·동작·로봇)가 서로 달라, 37. 관제 화면·실행 기록에서 여러 제조사 상태를 한 기록으로 모으려면 ROP 가 대응표를 만들어 정규화해야 할 것으로 보인다. | ref-031, ref-253, ref-111 | 아니오 | low | 2026-10-09 | — | — |
| f6 | [사실] | Open-RMF rmf-web 의 API 서버는 기본으로 메모리 안의 SQLite 를 써서 실행 기록이 남지 않지만, 설정의 db_url 로 PostgreSQL·SQLite·MySQL·MariaDB 를 지정해 영속 저장할 수 있다. | ref-762, ref-302 | 아니오 | medium | 2026-10-09 | — | — |
| f7 | [사실] | Open-RMF 로그 항목(log_entry) 스키마는 오늘 기준으로도 순번(seq)·수준(tier)·밀리초 유닉스 시각·본문을 필수로 하고 수준 값을 uninitialized·info·warning·error 로 두어, 페이지 7절의 로그 수준 서술이 그대로 유효하다. | ref-1095 | 아니오 | medium | 2026-10-09 | — | — |
| f8 | [사실] | IEEE 7001-2021(자율 시스템 투명성 표준)은 사용자, 검증·인증 담당자, 고장·사고 조사자, 소송·행정 절차의 전문 자문가, 일반 대중의 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 객관적으로 평가할 수 있는 다섯 단계의 투명성 수준을 정하며, IEEE 로봇·자동화 학회가 공동 후원했다. | ref-1338 | 아니오 | medium | 2022-05-11 | — | — |
| f9 | [추정] | IEEE 7001-2021 이 운영자(사용자)와 사고 조사자를 별도 이해관계자로 두므로, 37. 관제 화면·실행 기록의 설명 가능한 표시는 운영자용 투명성으로, 실행 기록은 조사자용 투명성으로 나눠 평가하는 근거가 될 수 있을 것으로 보이나, 표준이 화면 설계나 기록 항목을 정하는지는 확인하지 못했다. | ref-1338 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [사실] | ISO 11064(관제 센터 인간공학 설계) 계열은 설계 원칙, 관제 공간 배치, 관제실 배치, 작업대 배치·치수, 표시 장치와 조작기, 환경 요건, 관제 센터 평가 원칙, 특정 적용의 인간공학 요건의 여러 부로 나뉜다. | ref-1349 | 아니오 | medium | 2000 | — | — |
| f11 | [사실] | Winfield 외(2022-05, ICRES 2022 제출)는 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 같은 운용 데이터를 안전하게 기록하는 장치 또는 소프트웨어 모듈인 윤리적 블랙박스의 공개 표준 초안을 첫 초안으로 내놓았다. | ref-1120 | 아니오 | medium | 2022-05-13 | 예외·성과 | — |
| f12 | [추정] | 윤리적 블랙박스 초안은 로봇 한 대의 내부 기록을 대상으로 하므로, 여러 제조사 로봇을 지휘하는 플랫폼 수준의 명령·정지·재가동 기록 항목을 정한 공개 규약은 이번 조사에서도 확인하지 못해 oq-252 는 열린 채로 남는 것으로 보인다. | ref-1120, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f13 | [사실] | EU AI Act 제12조는 고위험 AI 시스템이 수명 동안 사건을 자동 기록(로그)할 수 있게 기술적으로 갖추고, 그 기록이 위험 상황·실질적 변경의 식별, 출시 후 모니터링, 배포자의 운용 모니터링(제26조 제5항)을 뒷받침하게 한다. | ref-863 | 아니오 | medium | 2024-07-12 | — | — |
| f14 | [사실] | EU AI Act 는 고위험 AI 의 자동 생성 로그를 공급자(제19조 제1항)와 배포자(제26조 제6항)가 각자 통제하는 범위에서 목적에 맞는 기간, 최소 6개월 보관하게 하고, 다른 EU·회원국 법(특히 개인정보 보호법)이 다르게 정하면 그에 따르게 한다. | ref-1341, ref-1342 | 아니오 | medium | 2024-07-12 | — | — |
| f15 | [추정] | 연계 대상: 로봇 플랫폼의 AI 구성요소가 고위험 AI 인지의 판단은 법무·규제 영역이며, 해당한다면 플랫폼 실행 기록의 보관 의무는 그 로그를 공급자와 배포자 중 누가 통제하는지에 따라 나뉘므로 ROP 는 보관 기간 설정과 통제 주체 표시를 기록 기능으로 갖추는 쪽을 맡을 것으로 보인다(oq-316 부분 근거). | ref-863, ref-1341, ref-1342 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | 한림대학교성심병원은 2024-04 기준 안내·배송·방역 로봇 등 7종 73대의 서비스 로봇을 커맨드센터의 통합관제시스템으로 운영하며, 커맨드센터 담당자는 서로 다른 제조사 로봇을 하나의 관제시스템으로 연결하는 일이 중요하다고 밝혔다. | ref-1344, ref-944 | 예 | medium | 2024-04-20 | 병원 / 수행 자원 | — |
| f17 | [사실] | 같은 보도에 따르면 한림대학교성심병원의 로봇 서비스는 2022-08 부터 2024-03 까지 3만 1607건 시행되었으나, 관제 화면 항목이나 배송 이력 조회 방식은 공개되지 않았다. | ref-1344 | 아니오 | low | 2024-04-20 | 병원 / 예외·성과 | — |
| f18 | [추정] | LG CNS 는 Open-RMF 를 바탕으로 한 로봇 통합운영 플랫폼에서 고객이 로봇의 이동 동선과 작업 처리 결과를 실시간으로 한눈에 확인할 수 있고 AGV·AMR·오토스토어·소팅로봇이 연계되어 있으며, G마켓 동탄 물류센터에서 기술검증에 착수했다고 밝혔다. | ref-1343 | 아니오 | low | 2023-07-06 | 물류창고 / 수행 자원 | 벤더 주장 |
| f19 | [사실] | 국내 실외이동로봇 운행안전인증은 속도 제어·비상정지·장애물 감지·횡단보도 통행·운행구역 준수·관제 장치 등 16개 항목을 평가하고 로봇과 관제장치의 조합에 인증을 주므로, 실외 현장에서는 관제 장치가 운행 제약의 하나가 된다. | ref-1345, ref-980 | 아니오 | low | 2024-01-31 | 실외 / 제약 | — |
| f20 | [사실] | 농촌진흥청의 통합 관리 프로그램은 자체 개발한 방제·운반·모니터링 로봇 3종을 하나의 화면으로 관리하며, 다른 제조사 로봇의 연결 여부는 보도에 없다. | ref-1007 | 아니오 | low | 2025-04-23 | 기타 / 수행 자원 | 원문 미열람 |
| f21 | [사실] | LH토지주택연구원 자료를 인용한 보도는 공동주택 단지 로봇 택배에서 택배 차량이 단지 집하처에 송장번호를 인식시키면 물품 정보가 관제실로 전달된다고 전한다. | ref-976 | 아니오 | low | 2024-07-18 | 가정 / 시작 조건 | 원문 미열람 |
| f22 | [사실] | Patel 외(2021)는 여러 운영자가 다중 로봇을 함께 감독할 때의 투명성을 다루며, 자기 작업 정보만 보이는 방식·다른 운영자 작업 정보를 공유하는 방식·둘을 섞은 방식·없음의 네 모드를 참가자 18명의 사용자 연구로 비교해 인식·신뢰·작업 부하를 쟀다. | ref-1347 | 아니오 | medium | 2021-05-14 | — | — |
| f23 | [추정] | 이번에 확인한 설명 가능한 표시·투명성 연구도 실험실 사용자 연구 수준이어서, 실제 운영 중인 로봇 플릿 관제 화면에서 운영자의 상황 인식과 대응 시간을 측정한 공개 연구는 여전히 확인하지 못해 oq-238 은 열린 채로 남는 것으로 보인다. | ref-1347, ref-1099 | 아니오 | low | 2026-10-09 | — | — |
| f24 | [사실] | Rohrer 외(2022)는 공장 물류를 모사한 RoboCup Logistics League 시뮬레이션의 사건을 데이터베이스에서 꺼내 로봇·주문·부품 객체와 11개 활동을 담은 객체 중심 이벤트 로그(OCEL JSON)로 만들고, 다음 사건과 그 시각을 예측하는 데 썼다. | ref-1348 | 아니오 | medium | 2022-07-20 | — | — |
| f25 | [추정] | 로봇 물류 실행 기록을 로봇·주문·부품 객체 중심 이벤트 로그로 만든 공개 사례는 있으나 그 로그를 시뮬레이션 시나리오 사양으로 되돌리는 변환 규칙은 이번에도 확인하지 못해, oq-131 에는 기록 쪽 형식만 부분 근거가 된 것으로 보인다. | ref-1348 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-1095 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json | 아니오 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | 기사 | low | 2026-10-09 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 예 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동 | 2025-04-23 | 기사 | low | 2026-10-09 | https://www.newstomato.com/ReadNews.aspx?no=1259970 | 예 |
| ref-976 | 정보통신신문 (김연균) | 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ | 2024-07-18 | 기사 | low | 2026-10-09 | https://www.koit.co.kr/news/articleView.html?idxno=123976 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-1099 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 2017-07-27 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ | 예 |
| ref-253 | MassRobotics (MassRobotics-AMR/AMR_Interop_Standard) | AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-1338 | IEEE Standards Association | How To Make Autonomous Systems More Transparent and Trustworthy | 2022-05-11 | 표준 | medium | 2026-10-09 | https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy | 아니오 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2205.06564 | 아니오 |
| ref-863 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 12: Record-keeping | 2024-07-12 | 정부·연구기관 | high | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 | 아니오 |
| ref-1341 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 19: Automatically generated logs | 2024-07-12 | 정부·연구기관 | high | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19 | 아니오 |
| ref-1342 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 26: Obligations of deployers of high-risk AI systems | 2024-07-12 | 정부·연구기관 | high | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26 | 아니오 |
| ref-1343 | LG CNS (LG 미디어 보도자료) | ‘로봇 통합운영 플랫폼’ 개발 | 2023-07-06 | 벤더 문서 | low | 2026-10-09 | https://lg.co.kr/media/release/26480 | 아니오 |
| ref-1344 | 코메디닷컴 | [메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠 | 2024-04-20 | 기사 | low | 2026-10-09 | https://kormedi.com/1682189/ | 아니오 |
| ref-1345 | 바이라인네트워크 (이진호) | 뉴빌리티, 실외이동 로봇 운행안전 인증 획득 | 2024-01-31 | 기사 | low | 2026-10-09 | https://byline.network/2024/01/240131_00004/ | 아니오 |
| ref-762 | Open Robotics (open-rmf/rmf-web) | rmf-web packages/api-server — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-1347 | Patel, J., Ramaswamy, T., Li, Z., & Pinciroli, C. (arXiv) | Transparency in Multi-Human Multi-Robot Interaction | 2021-05-14 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2101.10495 | 아니오 |
| ref-1348 | Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv) | Predictive Object-Centric Process Monitoring | 2022-07-20 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2207.10017 | 아니오 |
| ref-1349 | ISO (ANSI Webstore 미리보기) | ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview) | 2000 | 표준 | medium | 2026-10-09 | https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md | 5, 7, 9, 11 | 갱신(차등): 섹션 5 — 병원 사례에 f16(7종 73대 통합관제, 교차 확인)·f17(누적 3만 1607건) 추가, 물류창고 f18('벤더 주장' 병기, 흐름 단계는 서술하지 않음), 실외 f19(관제 장치가 인증 항목·제약), 기타 f20, 가정 f21 을 현장 유형마다 나눠 '찾지 못했다' 문장 교체. 제조 공장·상업 시설은 이번에도 찾지 못함 / 섹션 7 — 표에 MassRobotics statusReport(f3), VDA 5050 동작 상태·오류 수준·information·logReport(f1·f2), Open-RMF 배차 상태·개입 기록(f4), IEEE 7001-2021(f8), ISO 11064(f10), 윤리적 블랙박스 초안(f11) 행 추가, rmf-web 행을 '기본은 메모리 내 SQLite, db_url 로 영속 DB 설정'으로 갱신(f6, 바뀐 출처), 로그 수준 재확인(f7) / 섹션 9 — 상태 값 정규화를 직접 범위에(f5), EU AI Act 로그 보관 기간·주체를 연계 대상으로(f13·f14·f15) / 섹션 11 — oq-237 해결 제안(f1·f3·f4·f5), oq-238 미해결(f22·f23), oq-240 부분 근거(f8·f9·f10), oq-252 부분 근거(f11·f12), oq-316 부분 근거(f13·f14·f15), oq-131 부분 근거(f24·f25), oq-239 미해결, 새 질문 2건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석(f1 오류 수준·f10 ISO 11064), 59. 법·규제·보험·라이선스(f13·f14), 50. 안전 표준·인증·사고 조사(f11), 66. 실외(f19) 페이지 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 운용 상태 | Operational State (MassRobotics statusReport operationalState) | MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다. |
| 동작 상태 | Action Status (VDA 5050 actionStatus) | VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다. |
| 자율 시스템 투명성 수준 | Transparency Level (IEEE 7001-2021) | IEEE 7001-2021 이 사용자·인증 담당자·사고 조사자 등 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 다섯 단계로 정한, 객관적으로 평가할 수 있는 투명성 등급이다. |

## 열린 질문

새로 생긴 질문:

- VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가? | 관련 영역: 37. 관제 화면·실행 기록, 21. 상호운용 표준·적합성 | 근거: f5 | 종류: 일반
- 국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? | 관련 영역: 37. 관제 화면·실행 기록, 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-237

## 자체 점검

- 출처 수: 22 · 교차 확인: 1
- 예산 사용량: 검색 14회 · 신규 출처 13건
- 미확인 항목:
    - oq-239 미해결: 마약류 관리에 관한 법률 시행규칙의 장부·기록 2년 보존 조문을 국가법령정보센터에서 열지 못했고(본문 미표시) 검색 결과는 기사·비공식 법령 사이트뿐이라 근거로 쓰지 않음. 로봇 배송 이력 자체의 보관 요건은 확인하지 못함
    - f11 윤리적 블랙박스 초안 부록(기록 항목·보관 시간 창·보안 요건): PDF 텍스트 추출 실패로 미확인
    - f8 IEEE 7001-2021 본문 미열람(IEEE SA 소개 글 기준), 화면·기록 요건 포함 여부 미확인
    - f10 ISO 11064-1 적용 범위 절 미확인(미리보기에 없음). 검색 요약에 나온 '교통·물류 관제 시스템 포함' 범위 문구는 원문으로 확인하지 못해 넣지 않음
    - f19 운행안전인증 16개 항목 중 관제 장치 항목의 세부 요건 미확인, ref-980 이번 실행에서 다시 열지 않음
    - f16 의 ref-944 와 f20·f21 출처는 이전 실행 확인 내용 재인용이며 이번에 다시 열지 않음
    - f18 LG CNS 플랫폼 기능과 G마켓 동탄 기술검증 결과는 벤더 보도자료뿐이며 독립 확인하지 못함
    - 제조 공장·상업 시설의 관제 화면·실행 기록 사례는 이번에도 찾지 못함
    - f24 RCLL 로그 규모는 표가 깨져 미확인
- 범위 경계 위반 의심:
    - f15: 고위험 AI 해당 여부와 로그 보관 의무 해석은 법무·규제 쪽 연계 대상이라 claim 을 '연계 대상: '으로 시작하고 ROP 몫은 보관 기간 설정·통제 주체 표시로 한정
    - f19: 운행안전인증 판단은 인증 기관·운영자 쪽이며 ROP 에는 실외 현장 제약으로만 반영 제안
    - f11·f12: 윤리적 블랙박스의 센서·구동기 기록은 로봇 자체 지능·제어 쪽 기록이므로 ROP 직접 범위가 아니라 플랫폼 수준 기록 항목의 비교 대상으로만 씀
    - f2: VDA 5050 logReport 로 만드는 로그는 로봇 쪽 기록(연계 대상)이며 ROP 는 요청과 결과 이름 수신만 맡는다고 서술해야 함
- 한계: web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청이 없어 빈·약한 절(5절 현장 사례, 7절 표준, 9절 기록 보관 경계, 11절 열린 질문)과 바뀐 출처(rmf-web 저장 설정)만 조사했다. 검색 14회/30, 신규 출처 13건/15(ref-253~ref-1349, 예약 구간 안), 재사용 9건. 신규 출처는 모두 원문 또는 공식 페이지를 열었다(webfetch 10, github_raw 2, 미리보기 1). 재사용 가운데 ref-031·ref-111 은 입력의 원문 텍스트(inbox), ref-302·ref-1095 는 github_raw 로 다시 열었고, ref-944·ref-1007·ref-976·ref-980·ref-1099 는 다시 열지 않아 source_unopened 로 표시했다. 교차 확인 1건(f16, 7종 73대 통합관제: 코메디닷컴·로봇신문). oq-237 해결 근거: f1·f3·f4·f5(Open-RMF 외에 VDA 5050 과 MassRobotics 가 공개 상태 값을 정함, 대응표는 없음 — 새 질문으로 올림). oq-238·oq-239 는 미해결, oq-131·oq-240·oq-252·oq-316 은 부분 근거만. 현장 유형: 병원(f16·f17), 물류창고(f18, 벤더 주장), 실외(f19), 기타(f20), 가정(f21). 제조 공장·상업 시설 사례는 검색 1회로 찾지 못했다. 벤더 주장 1건(f18). 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 섞지 않았고 f24·f25 는 기록 형식으로만 다뤘다. 핵심 질문에 대한 새 결론은 없으며 '무엇'의 표시 근거(상태 값 규약)만 보강되었다. 용어집에 이미 있는 윤리적 블랙박스·자동 사건 기록·HMI 철학·객체 중심 이벤트 로그는 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-05/research.md

```markdown
# 리서치 브리프 2026-09-30-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-05 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 41. 플랫폼 아키텍처·외부 API |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 클라우드 로보틱스, 온프레미스(현장) 클라우드, OpenAPI, AsyncAPI, 웹훅, 이벤트 기반 아키텍처 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·제조 공장·물류창고·기타 현장의 아키텍처 배치 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 클라우드·현장 서버·로봇 역할 분담, 계산 오프로딩, 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, REST·이벤트·SDK 조합 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF(rmf-web API 서버·rmf_api_msgs), VDA 5050 전송 구조, OpenAPI, AsyncAPI, RoMi-H, FogROS2 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]
2. 클라우드·현장(온프레미스) 서버·로봇 사이의 계산·판단 배치를 다룬 연구와 오픈소스(클라우드 로보틱스, 계산 오프로딩, 현장 클라우드 기준 아키텍처)는 무엇이며 어떤 결과를 보고하는가? (섹션 3·6·8 겨냥)
3. 제조사 중립적인 플랫폼 기준 아키텍처(서비스 분리, 이벤트 구조, 제조사 어댑터 계층)는 Open-RMF·RoMi-H·VDA 5050 에서 어떻게 구성되는가? (섹션 6·7 겨냥)
4. 외부 시스템과 개발자에게 여는 API·웹훅·SDK 를 기계가 읽을 수 있게 기술하는 표준(OpenAPI, AsyncAPI)과 오픈소스·제품의 제공 형태(REST, 이벤트 스트림, 인증·권한)는 무엇인가? (섹션 4·6·7 겨냥)
5. 병원·제조 공장·물류창고·기타 현장(국내 포함)에서 플랫폼을 어디에 두고 무엇을 외부에 열었는지 보여 주는 사례는 무엇인가? (섹션 5 겨냥, 한국 자료 우선)
6. 클라우드 장애·네트워크 품질 저하가 역할 분담 결정에 주는 제약과 대응 방법은 무엇인가? (섹션 3·6·11 겨냥)
7. 플랫폼 아키텍처·외부 API 에서 ROP가 직접 맡을 것과 로봇 자체 지능·업무 시스템·클라우드 인프라에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 웹 API 서버(rmf-web api-server)는 Open-RMF 배치와 웹 대시보드·외부 클라이언트 사이에 REST 엔드포인트를 두고 그 정의를 서버의 /docs 경로에 OpenAPI 형식 문서로 제공하며, 기록용 데이터베이스는 tortoise-orm 으로 PostgreSQL·SQLite·MySQL·MariaDB 를 지원한다(기본값은 메모리 SQLite). | ref-762 | 아니오 | medium | 2026-09-30 | — | — |
| f2 | [사실] | rmf-web API 서버는 OpenID Connect 로 발급된 JWT 접근 토큰을 독립적으로 검증해 사용자를 식별하고, 사용자–역할–권한 그룹의 3단 구조(역할이 그룹에 대한 동작을 허용하고 자원은 그룹에 속함)로 접근을 통제하며 관리자는 모든 그룹에 모든 동작을 할 수 있다. | ref-762 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f3 | [사실] | Open-RMF 의 rmf_api_msgs 는 C++·Python 으로 된 RMF 구성 요소와 웹 인터페이스 사이를 잇는 JSON 메시지 스키마 모음으로, 작업 요청·예약, 작업 상태, 플릿 상태 스키마를 담고 스키마에서 타입 있는 데이터 모델을 생성할 수 있게 한다. | ref-1033 | 아니오 | medium | 2026-09-30 | — | — |
| f4 | [사실] | Open-RMF 핵심 구조는 모든 플릿 관리자가 예상 경로를 보고하는 중앙 교통 일정 데이터베이스와 충돌 시 플릿 관리자 간 협상을 두고, 제조사 고유 API 를 표준 인터페이스로 잇는 플릿 어댑터를 제어 수준(Full Control·Traffic Light·Read Only·No Interface)으로 나누며, 재사용 가능한 C++ API(파이썬 바인딩 포함)는 Full Control 에만 있다. | ref-004 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f5 | [사실] | VDA 5050 3.0.0 은 플릿 관제와 이동 로봇 사이의 제조사 중립 인터페이스로 MQTT 3.1.1 이상과 JSON 을 쓰고, 주제를 interfaceName/majorVersion/manufacturer/serialNumber/topic 구조(예 vda5050/v3/…/order)로 정하며 order·instantActions·state·visualization·connection·factsheet·responses·zoneSet 주제를 둔다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 명세는 플릿 관제–이동 로봇 통신과 무관한 인터페이스, 곧 주변 설비·기반 시설 구성 요소·외부 IT 시스템과의 인터페이스를 범위 밖으로 둔다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | OpenAPI 명세 3.1.0(2021-02-15)은 사람과 컴퓨터가 서비스의 기능을 발견·이해하게 하는 HTTP API 의 언어 중립 표준 인터페이스 기술 형식이며, 3.1.0 에서 API 가 받을 수 있는 수신 웹훅을 기술하는 webhooks 필드가 새로 들어갔다. | ref-1028 | 아니오 | medium | 2021-02-15 | — | — |
| f8 | [사실] | AsyncAPI 명세 3.1.0 은 메시지 기반 API 를 기계가 읽을 수 있게 기술하는 프로토콜 중립 형식으로 MQTT·AMQP·WebSocket·Kafka·HTTP 등에 쓰이며, 채널·동작(send/receive)·메시지·서버(브로커)·프로토콜별 바인딩을 핵심 객체로 두고 Apache 2.0 라이선스로 공개된다. | ref-1027 | 아니오 | medium | 2026-09-30 | — | — |
| f9 | [사실] | Ichnowski 외의 FogROS2(arXiv 2205.09778, 2023-04 개정)는 연산 능력이 제한된 로봇이 ROS 2 노드를 AWS·GCP·Azure 같은 원격 클라우드로 옮겨 실행하게 하는 ROS 2 배포판 포함 플랫폼으로, SLAM 지연 50% 감소, 파지 계획 14초→1.2초, 모션 계획 45배 가속, 영상 압축으로 이미지 전송 지연 97% 개선을 보고했다. | ref-304 | 아니오 | medium | 2023-04 | 예외·성과 | — |
| f10 | [사실] | Chen 외의 FogROS2-FT(IROS 2024)는 클라우드 제공자 장애, 네트워크 서비스 품질(QoS) 변동, 신뢰성 높은 인스턴스의 비용을 클라우드 로보틱스의 약점으로 보고, 상태 없는 로봇 서비스를 여러 클라우드에 복제해 가장 먼저 온 응답을 쓰는 방식으로 모션 계획 P99 지연을 최대 5.53배 줄이고 비용을 최대 2.2배 낮췄다고 보고했다. | ref-1037 | 아니오 | medium | 2024-12 | 예외·성과 | — |
| f11 | [사실] | 독립된 두 연구(Singhal 외 2017, Brorsson 외 2025)는 모두 로봇 밖의 중앙 계산 자원(클라우드 또는 현장 클라우드)이 플릿 조율·전역 계획을 맡고 각 로봇이 국지 주행 같은 온보드 자율 기능을 유지하는 혼합 구조를 제시한다. | ref-1032, ref-308 | 예 | medium | 2025-12 | 수행 자원 | — |
| f12 | [사실] | Brorsson 외(arXiv 2512.15215, 2025-12)의 RAIL 기준 아키텍처는 사내 물류 이동 로봇을 위해 설비에 단 외부 센서·계산 자원(기반 시설), 지연·연결 문제를 다루는 현장 클라우드(on-premise cloud), 로봇 온보드 자율의 세 층을 두며, 대형 상용차 제조 현장 실배치와 사용자 경험 평가로 이를 보였다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 수행 자원 | — |
| f13 | [사실] | 싱가포르 창이종합병원 CHART 의 RoMi-H(Robotic Middleware for Healthcare)는 OMG DDS 를 쓰는 미들웨어로 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리와 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·ICT 시스템용 API)의 네 영역으로 구성되며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다. | ref-937 | 아니오 | medium | 2026-09-30 | 병원 / 수행 자원 | — |
| f14 | [추정] | 네이버는 로봇 안이 아니라 클라우드에서 연산·판단을 하는 브레인리스 로봇 구조의 ARC(AI-Robot-Cloud)를 이동 계획·위치 추정·작업 수행과 기반 시설 연동을 맡는 ARC brain, 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정하는 ARC eye, 웹 개발자가 로봇 서비스를 만들게 하는 웹 기반 OS 인 ARC mind 로 나누고, 제2사옥 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다. | ref-1025 | 아니오 | low | 2026-09-30 | 기타 / 수행 자원 | 벤더 주장 |
| f15 | [추정] | MiR 은 MiR Fleet Enterprise 가 Windows Server 에서 돌며 가상화·클라우드 배치를 지원하고, ERP·MES·WMS 연동용 REST API 와 이벤트 기반 아키텍처를 갖추며, IEC 62443-4-2(SL-C 3)에 맞춰 단일 로그인·감사 기록·세분화된 사용자 권한을 제공한다고 주장한다. | ref-774 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f16 | [추정] | InOrbit 개발자 문서는 로봇 데이터 조회·원격 동작·미션 추적·감사 기록용 REST·스트리밍 API, 사고 관리용 외부 발신 웹훅과 수신 API, 서비스 사용자와 역할 기반 권한에 묶인 API 키, 로봇에 넣는 Robot SDK(C++·Python)와 현장 애플리케이션 연동용 Edge SDK, 임베드 가능한 대시보드를 제공한다고 적는다. | ref-1034 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f17 | [추정] | 물류창고 피킹에서 Locus Robotics 는 LocusONE 플랫폼이 API 로 창고 관리 시스템(WMS)과 연결돼 WMS 에서 주문을 받아 피킹 효율을 기준으로 최적화한 뒤 로봇 작업으로 내린다고 주장한다. | ref-1036 | 아니오 | low | 2026-09-30 | 물류창고 / 시작 조건 | 벤더 주장 |
| f18 | [추정] | 같은 Locus Robotics 자료는 피킹 완료 확인을 WMS 로 즉시 되돌려 보내고 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 같은 운영 성과 데이터를 제공한다고 주장한다. | ref-1036 | 아니오 | low | 2026-09-30 | 물류창고 / 완료·인계 | 벤더 주장 |
| f19 | [추정] | 뉴스핌(2026-05-12) 보도에 따르면 카카오모빌리티는 로봇–인프라–사용자를 잇는 플랫폼으로 서비스 요청을 로봇 실행 단위로 바꾸는 작업 추상화, 이종 로봇이 통신하게 하는 통합 API 인 제어 인터페이스, 고장 감지 시 다른 로봇으로 작업을 넘기는 재배정, 건물 인프라와 ERP·물류 자동화 시스템을 잇는 연동 기반을 추진한다. | ref-1029 | 아니오 | low | 2026-05-12 | — | 벤더 주장 |
| f20 | [추정] | 로봇신문 보도에 따르면 클로봇은 다중 로봇 통합관제 플랫폼 CROMS 가 서로 다른 제조사 로봇 50대 이상을 동시에 제어하고 승강기 연동으로 다층 건물에서 운용할 수 있으며 국내 첫 이기종 로봇 통합관제 솔루션이라고 밝힌다. | ref-870 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에 대해, 국지 주행·즉각적 안전 반응은 로봇에, 지연·연결에 민감한 플릿 조율·교통·설비 연동은 현장 서버(현장 클라우드)에, 무거운 계산 오프로딩과 여러 현장 집계·개발자 서비스는 클라우드에 두는 혼합 배치가 연구·오픈소스의 공통 형태이고(f4·f9·f11·f12·f14), 외부에는 동기식 REST(OpenAPI 로 기술)와 이벤트·메시지 API(AsyncAPI·웹훅), SDK 를 인증·권한 통제와 함께 여는 조합이 쓰이는 것으로 보인다(f1·f2·f7·f8·f16). | ref-004, ref-304, ref-1032, ref-308, ref-1025, ref-762, ref-1028, ref-1027, ref-1034 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 로봇–관제 표준(VDA 5050)이 업무 IT 시스템·설비와의 인터페이스를 범위 밖에 두고(f6) 제조사 관제마다 자체 REST API 를 따로 내므로(f15·f17) 이종 로봇을 묶는 플랫폼의 외부 API 가 업무 시스템과 개발자가 만나는 단일 접점이 되며, 클라우드 장애·네트워크 품질 변동(f10)이 있어 판단을 어디에 두느냐가 운영 연속성을 좌우하기 때문이다. | ref-031, ref-774, ref-1036, ref-1037 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 41. 플랫폼 아키텍처·외부 API 에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처(f4·f13), 작업 요청·작업 상태·플릿 상태의 기계가독 스키마(f3), REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기(f5·f7·f8), API 호출의 인증·권한(f2), 판단·데이터를 로봇·현장 서버·클라우드 중 어디에 둘지 정하는 배치 정책이다. | ref-004, ref-937, ref-1033, ref-031, ref-1028, ref-1027, ref-762 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능(f9·f11)은 로봇 제조사에, 주문·재고 같은 업무 판단(f17)은 상위 업무 시스템(WMS·ERP)에, 클라우드 제공자 인프라와 현장 네트워크(f10·f17)는 클라우드 사업자와 42. 분산 시스템·통신·컴퓨팅 구조 영역에 속하므로, ROP 는 이들을 부르고 받는 인터페이스와 배치 결정을 맡을 것으로 보인다. | ref-304, ref-1032, ref-1036, ref-1037 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 현장 네트워크·연결 끊김 운영을 다루는 42. 분산 시스템·통신·컴퓨팅 구조(f10·f12), 기록 DB·감사 기록·배포를 다루는 43. 데이터·관측성·배포(f1·f16), 플릿 어댑터를 다루는 20. 로봇·제조사 관제 연동(f4·f15), VDA 5050 을 다루는 21. 상호운용 표준·적합성(f5·f6), 승강기·기반 시설 연동의 22. 설비·건물 시스템 연동(f13·f14·f20), WMS·ERP 연동의 23. 업무 시스템 연동(f15·f17·f18), API 인증·권한의 51. 인증·권한·격리(f2·f16), IEC 62443 을 다루는 52. 통신 보호·위협 관리·감사(f15), 대시보드의 37. 관제 화면·실행 기록(f1·f16), 재배정의 32. 예외 복구·재계획·업무 연속성(f19), 업체 동향의 1. 기술·시장·업체 동향(f14·f19·f20), 적용 현장인 61. 물류창고(f17)·62. 제조 공장(f12)·63. 병원·의료(f13)·67. 기타 현장(f14)과 이어진다. | ref-1037, ref-308, ref-762, ref-1034, ref-004, ref-774, ref-031, ref-937, ref-1025, ref-870, ref-1036, ref-1029 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-304 | Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2205.09778 | 아니오 |
| ref-1025 | NAVER Corp. | 로보틱스 l NAVER Corp. | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.navercorp.com/tech/robotics | 아니오 |
| ref-937 | Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology) | ROMI-H | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://www.cgh.com.sg/chart/projects/romi-h | 아니오 |
| ref-1027 | AsyncAPI Initiative | AsyncAPI Specification 3.1.0 | 미확인 | 표준 | high | 2026-09-30 | https://www.asyncapi.com/docs/reference/specification/v3.1.0 | 아니오 |
| ref-1028 | OpenAPI Initiative | OpenAPI Specification v3.1.0 | 2021-02-15 | 표준 | high | 2026-09-30 | https://spec.openapis.org/oas/v3.1.0 | 아니오 |
| ref-1029 | 뉴스핌 | 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 … (제목 일부만 확인) | 2026-05-12 | 기사 | low | 2026-09-30 | https://www.newspim.com/news/view/20260512001077 | 아니오 |
| ref-870 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 … (제목 일부만 확인) | 미확인 | 기사 | low | 2026-09-30 | https://www.irobotnews.com/news/articleView.html?idxno=43274 | 아니오 |
| ref-308 | Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv) | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2512.15215 | 아니오 |
| ref-1032 | Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv) | Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform | 2017-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1706.08931 | 아니오 |
| ref-1033 | Open Robotics (open-rmf) | rmf_api_msgs — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_api_msgs | 아니오 |
| ref-1034 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://developer.inorbit.ai/docs | 아니오 |
| ref-774 | Mobile Industrial Robots (MiR) | MiR Fleet | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://mobile-industrial-robots.com/products/software/mir-fleet | 아니오 |
| ref-1036 | Locus Robotics | Seamless Integrations with LocusOne Robotics | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://locusrobotics.com/locusone/automated-warehouse-software/integrations | 아니오 |
| ref-1037 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 2024-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2412.05408 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(업무 시스템 인터페이스가 로봇–관제 표준 밖이고 클라우드 장애가 배치를 좌우), f21(핵심 질문 답, 추정) / 섹션 4: 클라우드 로보틱스·오프로딩 f9, 현장 클라우드 f12, OpenAPI·웹훅 f7, AsyncAPI f8, 플릿 어댑터·제어 수준 f4 / 섹션 5: 병원 — f13(창이종합병원 RoMi-H), 제조 공장 — f12(대형 상용차 제조 현장 RAIL), 물류창고 — f17(시작 조건: WMS 주문 수신)·f18(완료·인계: 확인 회신, 벤더 주장 병기), 기타 — f14(네이버 1784 사옥 ARC, 벤더 주장 병기). 여섯 항목 중 제약·예외 근거가 사례별로 부족함을 명시 / 섹션 6: 역할 분담 f11(교차 확인)·f12·f14, 계산 오프로딩 f9, 다중 클라우드 장애 대응 f10, 제조사 중립 어댑터 계층 f4·f13, REST·이벤트·SDK 조합 f1·f5·f16, 인증·권한 f2, 제품 사례 f15·f19·f20(벤더 주장 병기) / 섹션 7: Open-RMF f1~f4, VDA 5050 f5·f6, OpenAPI f7, AsyncAPI f8, RoMi-H f13, FogROS2 f9·f10 / 섹션 8: f9~f12 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 42. 분산 시스템·통신·컴퓨팅 구조 페이지에 f10·f12 반영, 20. 로봇·제조사 관제 연동 페이지에 f15·f16 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| OpenAPI 명세 | OpenAPI Specification (OAS) | HTTP API 의 경로·요청·응답·보안 방식을 사람과 컴퓨터가 함께 읽을 수 있게 기술하는 언어 중립 표준 형식으로, 3.1.0 부터 웹훅도 기술한다. |
| AsyncAPI 명세 | AsyncAPI Specification | MQTT·AMQP·WebSocket·Kafka 같은 메시지 기반 API 의 채널·동작·메시지·브로커를 기계가독 형식으로 기술하는 프로토콜 중립 명세다. |
| 웹훅 | Webhook | 어떤 사건이 일어났을 때 서비스가 미리 등록된 외부 URL 로 HTTP 요청을 보내 알리는 방식의 이벤트 전달 인터페이스다. |
| 클라우드 로보틱스 | Cloud Robotics | 로봇이 인터넷으로 연결된 원격 계산·저장 자원에 계산이나 데이터를 맡겨 온보드 능력의 한계를 보완하는 구조와 연구 분야다. |

## 열린 질문

새로 생긴 질문:

- 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드나 5G 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f14 | 종류: 일반
- 로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 57. 자산·소프트웨어 수명주기 관리 | 근거: f5 | 종류: 일반
- 로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반
- 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 1
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f9 FogROS2 모션 계획 가속 배수: arXiv 개정판 초록은 45배, 검색 요약의 ICRA 2023 판 서술은 28배로 보여 판에 따라 다를 수 있음(ICRA 카메라 레디 PDF 는 열지 않음)
    - f9·f10·f11·f12 는 논문 초록 기준이며 본문 실험 조건 미확인
    - f14 네이버 1784 로봇 대수: 회사 페이지는 100여 대, 검색 요약의 기사 문구는 40여 대로 기준 시점이 다를 수 있으나 기사 원문을 열지 않아 출처 충돌로 확정하지 않음
    - f14 5G 특화망 사용은 검색 요약에만 나오고 ITDaily 기사 원문은 ECONNRESET 으로 열지 못해 넣지 않음
    - f15 MiR 페이지 안에서 지원 대수 표현('최대 100대'와 '100대 넘는 배치')이 엇갈림
    - ref-1029·ref-870 기사 제목 전체 미확인, ref-870 발행일 미확인
    - ref-1027 AsyncAPI 3.1.0 발행일 미확인
    - Kehoe 외 클라우드 로보틱스 조사 논문(IEEE T-ASE 2015)은 PDF 본문 추출 실패·eScholarship 빈 페이지로 넣지 않음
    - AWS IoT RoboRunner 의 현재 서비스 상태(종료 여부)는 확인하지 못해 넣지 않음
    - MiR Fleet Enterprise 문서 PDF 는 크기 초과로 열지 못함
    - 국내 클라우드 로봇 참조 구조 표준(TTA·KS)은 검색 1회에서 찾지 못함
- 범위 경계 위반 의심:
    - f9: FogROS2 의 SLAM·파지 계획 오프로딩은 로봇 자체 지능·제어 기능의 실행 위치 선택이므로 배치 방식의 근거로만 쓰고 ROP 직접 범위로 서술하지 않도록 f24 에서 구분함
    - f11: 국지 주행·장애물 회피는 로봇 자체 지능(연계 대상)으로, 전역 조율만 이 영역 근거로 씀
    - f14: 네이버 ARC 는 위치 추정·이동 계획까지 클라우드에 두어 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례이며 원문의 '경계는 제품 전략에 따라 이동할 수 있다'는 문장에 해당함
    - f17·f18: 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽이며 ROP 는 연동 인터페이스만 다룸
    - f24: 로봇 자체 지능·업무 시스템·클라우드 인프라를 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-762~ref-1037, 예약 구간 안)로 출처 상한에 도달해 더 넣지 못했다. 재사용 2건(ref-004·ref-031 은 github_raw 로 다시 열었다; 참고문헌 목록 전체가 입력에 없어 ref-004 의 값은 규칙 파일 예시, ref-031 의 값은 같은 날 이전 브리프 2026-09-30-04 의 출처 표를 따랐다). 원문 열람: 17건 모두 열었다(webfetch 12건, github_raw 5건). 논문은 초록 페이지다. 교차 확인 1건(f11, 두 arXiv 논문이라 신뢰도 medium). 벤더 문서·기사만 근거로 한 finding(f14~f20)은 모두 vendor_claim: true·태그 추정·'벤더 주장' 첫머리로 냈다. 분류 원문 핵심 질문(어떤 판단을 어디에서 하고 외부에 무엇을 열 것인가)에는 f21 로 답했고 결론은 '로봇–현장 서버–클라우드 혼합 배치 + REST·이벤트 API·웹훅·SDK 를 인증·권한과 함께 여는 조합'이라는 추정이다. 현장 유형 사례는 병원(f13)·제조 공장(f12)·물류창고(f17·f18, 벤더 주장)·기타(f14, 사무 건물, 벤더 주장)이며 상업 시설·가정·실외 사례는 찾지 못했다. 국내 자료는 네이버(ref-1025)·뉴스핌(ref-1029)·로봇신문(ref-870) 세 건이고 국내 표준은 찾지 못했다. L. AI·학습 기술 관련 finding 은 없다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다(네이버 ARC eye 의 디지털 트윈 언급은 위치 추정용 현재 상태 표현으로만 인용). 용어집에 이미 있는 포그 컴퓨팅·브레인리스 로봇·플릿 어댑터·플릿 제어 수준·MQTT·JSON 스키마·의미적 버전 관리·멱등성 키는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
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
…(발췌: 전체 207,642자 중 앞 48,820자)
````

### data/source_texts/ref-762.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Open-RMF API Server

This API server sets up the necessary endpoints with an Open-RMF deployment and enables the use of the web dashboard. The server comes with the capability of logging to databases, as well as handling authentication and permissions.

# Setup

If not already done so, [install dependencies](../../README.md#Install-dependencies), you can use
```bash
pnpm install -w --filter api-server...
```
to install dependencies for only this package.

# API

Check out the latest API definitions [here](https://open-rmf.github.io/rmf-web/docs/api-server), or visit `/docs` relative to your running server's url, e.g. `http://localhost:8000/docs`.

# Run the server

```bash
rmf_api_server
```

## Configuration

Config files are python modules that export a variable named `config`. See [default_config.py](api_server/default_config.py) for an example and list of the options available. All options are REQUIRED unless specified otherwise.

Configuration is read from the file specified in the env `RMF_API_SERVER_CONFIG`, if not provided, the default config is used.

e.g.
```bash
RMF_API_SERVER_CONFIG='my_config.py' rmf_api_server
```
To run the api-server with PostgreSQL, assuming it has been set up to listen on 127.0.0.1:5432 with user `postgres` and password `postgres`:
```
RMF_API_SERVER_CONFIG=api_server/psql_local_config.py rmf_api_server
```

## Supported databases

rmf-server uses [tortoise-orm](https://github.com/tortoise/tortoise-orm/) to perform database operations. Currently, the supported databases are

* PostgreSQL
* SQLite
* MySQL
* MariaDB

by default it uses a in-memory sqlite instance, to use other databases, install rmf-server with the relevalent extras

* PostgreSQL - postgres
* MySQL - mysql
* MariaDB - maria

.e.g.

```bash
pip3 install rmf-server[postgres]
```

Then in your config, set the `db_url` accordingly, the url should be in the form

```
DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME?PARAM1=value&PARAM2=value
```

for example, to connect to postgres

```
postgres://<user>:<password>@<host>/<database>
```

for more information, see https://tortoise-orm.readthedocs.io/en/latest/databases.html.

### PostgreSQL
If you would like to use PostgreSQL, you will also need to install and set it up. The defaults are for PostgreSQL to be listening on 127.0.0.1:5432.

#### Docker
We can use Docker to quickly bring up a PostgreSQL instance.

Install docker: `https://docs.docker.com/engine/install/ubuntu/`
Start a a database instance: `docker run -it --rm --name rmf-postgres --network=host -e POSTGRES_PASSWORD=postgres -d postgres`

To stop the instance: `docker kill rmf-postgres`

#### Bare Metal
Alternatively, we can install PostgreSQL 'bare metal'.
```
apt install postgresql postgresql-contrib -y
# Set a default password
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"

sudo systemctl restart postgresql
# interactive prompt
sudo -i -u postgres
```
To manually reset the database:
```
sudo -u postgres bash -c "dropdb postgres; createdb postgres"
```

## Running behind a proxy

When running behind a reverse proxy like nginx, you need to set the `public_url` option to the url where rmf-server is served on. The reverse proxy also MUST strip the prefix.

For example, if rmf-server is served on https://example.com/rmf/api/v1, `public_url` must be set to `https://example.com/rmf/api/v1` and your reverse proxy must be configured to strip the prefix such that it forwards requests from `/rmf/api/v1/something` to `/something`.

## Running with RMF simulations

When running with rmf simulations, you need to set the env `RMF_SERVER_USE_SIM_TIME=true`. This is needed to ensure that times from the client are correctly converted to RMF's simulation time.

# Authentication and Authorization

## OpenID Connect

rmf-server does not manage user identities and access levels by itself, it uses an OpenID Connect compatible identity provider to perform authentication. Authorization however, is performed in-app by rmf-server.

### Access Token Format

OpenID Connect does not define the format of the access token, the canonical way for a resource server to validate an access token is to use the token introspection endpoint of the authentication server. In order to not have to connect to the identity provider for every request, rmf-server assumes the convention that the access token is a JWT that can be verified independently. Most modern identity providers like keycloak and auth0 follows this convention.

### Access Token Claims

The access token must include the `preferred_username` claim. It will be used to determine an user's authorization levels.

If your identity provider strips standard OIDC claims (such as `preferred_username`) from access tokens issued via the OAuth 2.0 `client_credentials` (M2M) flow and requires custom claims to use a collision-resistant namespaced name, set the optional `preferred_username_claim_namespace` config value to the namespace prefix used by your provider. The authenticator will then check `f"{namespace}preferred_username"` as a fallback when the bare `preferred_username` claim is absent.

This pattern aligns with [RFC 9068 §2.2.2](https://www.rfc-editor.org/rfc/rfc9068.html#section-2.2.2) (which requires that arbitrary attributes in JWT access tokens have "collision resistant" names) and [RFC 7519 §4.2](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.2) (which defines "Collision-Resistant Name" via Public Claim Names). [Auth0 enforces this policy explicitly](https://auth0.com/docs/secure/tokens/json-web-tokens/create-namespaced-custom-claims) for access tokens with a custom API audience — non-namespaced custom claims on standard OIDC names are silently dropped. Operators on other providers with comparable collision-avoidance policies may also benefit; leaving the value unset preserves the current behavior.

## Roles, Actions and Authorization Group

An user's permission to perform certain actions on a protected resource is determined by 3 values, role, action, and authorization group of the resource. A resource belongs to one authorization group and an user can belong to multiple roles. An user has access to perform an action on a resource if any of their roles has permission to perform the action on the authorization group which the resource belongs to. An admin always have permission to perform any action on any group.

For example, given the following permissions and users

Permissions:
| Role | Authz Group | Action |
| --- | --- | --- |
| role1 | group1 | task_submit |
| role2 | group2 | task_submit |
| role3 | group3 | task_submit |
| role4 | group1 | task_submit |
| role4 | group3 | task_submit |

Users:
| User | Roles | Is Admin |
| --- | --- | --- |
| user1 | role1 | false |
| user2 | role2, role3 | false |
| user3 | role4 | false |
| user4 | | true

`user1` will be able to submit a task that belongs to authorization group `group1`. `user2` can submit tasks belonging to `group2` and `group3`. `user3` can submit tasks in group `group1` and `group3`. `user4`, being an admin can submit tasks in any group.

The authorization group of a resource is determined automatically based on different factors according to the resource type. For example, a task's authorization group may be determined by the region where it takes place.

## Synchronization (or lack of) of User Data

rmf-server maintains its own database of users, roles and permissions. In order to keep compatibility with as many identitiy provider as possible and amount of code small, this database is never synchronized with the identity provider's database. Instead, rmf-server takes the following approach to keep things working even without a synchronized database.

* When an user first access any of the protected api, a new rmf-server user is automatically created, the  user will have no roles and no privileges.
  * rmf-server checks if the token is valid before creating the user. If it is valid, the user must exist in the identity provider.
* An admin can use the admin endpoints to perform various user management like
  * Create users
  * Create roles
  * Add/remove permissions to roles
  * Add/remove roles to users
* The admin endpoints only work on rmf-server's database and does not require delegation of any functions to the identity provider, as a result there are some cavaets
  * There is no endpoints to manage an user's authentication like reset user password, enable/disable users etc.
  * Endpoints that list/search users only includes users that is already added on to rmf-server.
* If an admin wishes to manage authorization for an user that exists in the identity provider, but not in rmf-server, they need to use the create user endpoint to create a new user with the same username.
* Deleting an user from rmf-server does not prevent them from accessing "semi-protected" apis (apis that require login but does not require any permissions). It also does not prevent them from logging into a frontend that connects to rmf-server (e.g. rmf dashboard).
  * This is because it does not delete the user from the identity provider and the next time they access any protected api, a new user will be automatically created.
  * Fully deleting an user so that they can no longer login should be done on the identity provider. There is no endpoint in rmf-server to forward deletion of an user to the identity provider because such behaviour may be unintuitive, undesirable and require specialized code paths for every provider.
* If the user is deleted from the identity provider, it will still exist in rmf-server.
  * This is harmless as the user will not be able to authenticate with the identity provider and get a valid token, so a "zombie" user will not be able to access any protected api.
* Since a new user is created with minimal privileges, and an admin is required to give users privileges (including the admin privilege), there is a problem.
  * This is worked around by adding a config to automatically make an user an admin on startup. Note that since there is no synchronization between the identity provider, there is no guarantee that such an user actually exists.

## TODO

A resource's authorizaion group is determined by it's contents. Exactly how they are determined for each type of resource is still either undecided or lacking information from RMF to be implemented, so currently every resource is put into a default empty group of `` (empty string).

## Database Migration

[`aerich`](https://github.com/tortoise/aerich) is a database migration tool for TortoiseORM. `aerich` requires a configuration file for initialization before doing any mutations, which can be found in `api_server.__main__.TORTOISE_ORM`.

Install `aerich`

```bash
pip3 install aerich
```

This migration example will be for PostgreSQL. First, setup `rmf-web` following [instructions](../../README.md). Then, run the `api-server` with `psql`,

```bash
# source RMF
cd ~/rmf-web/packages/api-server
pnpm run start:psql
```

In another terminal, activate the virtual environment manually and initialize `aerich`,

```bash
cd ~/rmf-web
source .venv/bin/activate
cd ~/rmf-web/packages/api-server

# First export the RMF_API_SERVER_CONFIG variable
export RMF_API_SERVER_CONFIG=psql_local_config.py

# Init aerich and save migration workspace to /tmp
aerich init -t api_server.__main__.TORTOISE_ORM --location /tmp/migrations
aerich init-db
```

You can check the current schema of a table. For example, using the `taskstate` table,

```bash
sudo -u postgres bash -c "psql -c '\d+ taskstate;'"
```

Now, modify the `TaskState` class in the `api_server/models/tortoise_models/tasks.py` to add a new field:

```python
new_field = fields.CharField(255)
```

Don't forget to make necessary changes to `api_server/repositories/tasks.py` too, to allow the dashboard to use the newly added fields.

Now attempt a migration, and allow `aerich` to find the changes required,

```bash
aerich migrate
# aerich will generate the migration file with the version
# check file at /tmp/migration/models/
```

Perform database upgrade,

```bash
aerich upgrade
```

Now, inspecting the database schema, you will find "new_field" available in the schema

```bash
sudo -u postgres bash -c "psql -c '\d+ taskstate;'"
```

Restart the `api-server` and the changes to the databse should be reflected.

## Running tests

### Running unit tests

```bash
pnpm test
```

By default in-memory sqlite database is used for testing, to test on another database, set the `RMF_API_SERVER_TEST_DB_URL` environment variable.

```bash
RMF_API_SERVER_TEST_DB_URL=<db_url> pnpm test
```

### Collecting code coverage

```bash
pnpm run test:cov
```

Generate coverage report
```bash
pnpm run test:report
```

## Live reload

```bash
uvicorn --reload api_server.app:app
```
````
