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
- verification_stage: second
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
          "content": "(절 본문 생략 — runs/2026-10-09-17/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-17/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-17/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-17/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-17/pages/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md 의 해당 절을 본다)"
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

### runs/2026-10-09-17/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md (5개 절)
- 분량 초과 자동 분리:
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-09-area41-s6.md (1,999자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area41-s7.md (1,533자)
    - docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area41-s11.md (1,163자)
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
