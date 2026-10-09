(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-18
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 42. 분산 시스템·통신·컴퓨팅 구조 (K. 플랫폼 아키텍처·인프라)
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

### runs/2026-10-09-18/target.json

```json
{
  "run_id": "2026-10-09-18",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 151,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 42,
    "area_name": "42. 분산 시스템·통신·컴퓨팅 구조",
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
  "selection_rationale": "CLI 지정 run_type=update, area=42"
}
```

### runs/2026-10-09-18/research.json

```json
{
  "run_id": "2026-10-09-18",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 42,
    "area_name": "42. 분산 시스템·통신·컴퓨팅 구조",
    "category": "K. 플랫폼 아키텍처·인프라"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 개정 전에 쓴 물류창고 시나리오 1건뿐이고 병원·상업 시설·제조 공장·실외·기타 현장 사례 없음(이번 재실행에서도 조사하지 못함)",
    "섹션 5. 적용 사례 — 'VDA 5050이 MQTT 5.0의 세션 만료 같은 장치를 어떻게 쓰는지는 미확인' 문장의 재확인 필요",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 3.0.0 의 연결(connection) 토픽 의미, 상태 보고 최소·최대 간격, 절전(HIBERNATING) 모드, 구역 허가 만료, 지도 사전 적재 같은 끊김 대비 장치가 정리되지 않음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 관제 쪽 통신 오류 탐지·시간 초과 처리 책임과 표준 범위 밖(외부 IT 인터페이스·사이버보안·운영 책임)의 근거가 약함",
    "섹션 11. 열린 질문 — oq-038·oq-039·oq-206 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]",
    "oq-038·oq-206 로봇–관제 표준은 로봇과 관제·브로커의 연결이 끊긴 동안 로봇이 어디까지 계속 움직이고, 관제는 무엇을 실행된 것으로 간주해야 한다고 정하는가? (섹션 5·9·11 겨냥)",
    "VDA 5050 3.0.0 은 연결 끊김을 어떻게 탐지·표시하고(연결 토픽, 유언 메시지, 절전 모드), 재연결 뒤 상태를 다시 세우는 수단을 무엇으로 두는가? (섹션 5·7 겨냥)",
    "oq-039 VDA 5050 3.0.0 은 명령·상태 메시지의 전달 보장 수준과 보고 간격을 어떻게 정하며, 허용 지연·손실률 수치를 정하는가? (섹션 7·11 겨냥)",
    "클라우드 브로커와 현장 브로커 배치, 지도·구역 배포 방식은 외부망 단절 중 운영 범위에 어떤 영향을 주는가? (섹션 6·9 겨냥)",
    "로봇–관제 표준이 범위 밖에 두는 것(외부 IT 인터페이스, 사이버보안, 운영 책임 배분)은 무엇이고, ROP 의 직접 범위와 연계 대상은 어떻게 갈리는가? (섹션 9 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 3.0.0 은 로봇–관제 통신이 무선망으로 이루어지며 연결 실패와 메시지 손실이 생길 수 있음을 전제로 하고, MQTT 를 JSON 형식과 함께 쓰며 MQTT 3.1.1 을 호환을 위한 최소 버전으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4장 전송 규약: 무선망 통신과 연결 실패·메시지 손실의 영향을 고려하며, 메시지 규약은 MQTT+JSON, 최소 호환 버전은 MQTT 3.1.1 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 통신 부담을 줄이기 위해 order·instantActions·state·factsheet·zoneSet·responses·visualization 토픽에 MQTT QoS 0(최선 노력)을, connection 토픽에 QoS 1(최소 한 번)을 쓰게 하고, 프로토콜 보안은 브로커 설정으로 다루되 이 지침에서는 정하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.1절: 통신 오버헤드를 줄이려고 7개 토픽은 QoS 0, connection 토픽은 QoS 1 을 쓴다. 보안은 브로커 구성에서 고려하되 지침 범위 밖 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행하며, 관제는 MQTT 가 비동기이고 무선 전송을 믿을 수 없으므로 이미 해제한 베이스(base)를 바꿀 수 없고 실행된 것으로 간주해야 하며 주문 취소(cancelOrder)도 같은 이유로 신뢰할 수 없는 것으로 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.1절 \"fulfills the order up to the last released node\". 6.1.2절: 베이스는 바꿀 수 없어 관제는 베이스가 이미 실행된 것으로 가정해야 하고, 취소 절차도 통신 한계로 신뢰할 수 없다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "VDA 5050 3.0.0 의 connection 토픽은 브로커–클라이언트 사이 하트비트로 끊김을 탐지해 브로커가 유언 메시지로 CONNECTION_BROKEN 을 알리는 MQTT 프로토콜 수준의 연결 확인용이며, 모든 메시지를 retained 플래그로 보내고, 관제가 로봇의 건강 상태 확인에 쓰지 않도록 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.3절 표: connection 은 로봇 연결 상실을 알리며 관제가 로봇 건강 확인에 쓰지 않는다. 6.5절: 하트비트로 끊김 탐지, 접속 시 유언을 CONNECTION_BROKEN 으로 설정, 메시지는 retained 로 전송 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 에서 로봇 상태 메시지는 정해진 사건(주문 수신, 오류·운용 모드·노드 상태 변화 등)이 생길 때와 적어도 30초마다 보내고, 연속 상태 메시지 사이의 최소 간격은 로봇이 팩트시트의 protocolLimits.timing.minimumStateInterval 로 알리며, 관련 사건은 하나의 상태 갱신으로 묶어 통신량을 줄이도록 권한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.6절: 상태는 관련 사건 발생 시 또는 최소 30초마다 발행, 상관된 사건은 한 번의 갱신으로, 최소 간격은 팩트시트 minimumStateInterval 이 정한다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 의 startHibernation 즉시 동작은 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 연결 상태를 HIBERNATING 으로 알리며 활성 주문을 지우고 움직이지 않게 하고, 배터리가 위급하거나 설정한 기상 시각(wakeUpTime)이 되면 로봇이 스스로 이 상태를 벗어날 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.2.3.1절 표 startHibernation: 연결 유지·상태 메시지 중단·HIBERNATING 발행·활성 주문 삭제·정지, stopHibernation 만 응답, 배터리 위급 시나 wakeUpTime 에 자율 해제 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 의 RELEASE 구역은 관제의 허가를 받아야 들어갈 수 있고, 로봇은 응답을 제때 받지 못하면 들어가지 않으며, 관제는 허가에 만료 시각(leaseExpiry)을 붙일 수 있고, 이미 구역 안에서 허가가 만료·철회되면 로봇은 구역 정의의 releaseLossBehavior(STOP·CONTINUE·EVACUATE)에 따라 움직인다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.4.1.1절 RELEASE·releaseLossBehavior, 6.4.3절: 응답이 제때 오지 않으면 진입하지 않음, leaseExpiry 갱신은 응답 재전송으로, 만료 시 EXPIRED 처리 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "VDA 5050 3.0.0 은 클라우드 사업자가 강제하는 토픽 구조가 있어 클라우드 기반 MQTT 브로커에서는 토픽 단계 구조를 개별 조정하게 허용하고, 로컬 브로커에는 interfaceName/majorVersion/manufacturer/serialNumber/topic 구조를 제안하되 토픽 이름은 필수로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.2절: 클라우드 사업자의 필수 토픽 구조 때문에 구조를 엄격히 정하지 않음, 로컬 브로커용 제안 구조와 예 vda5050/v3/KIT/0001/order (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "VDA 5050 3.0.0 에서 지도는 관제가 즉시 동작(downloadMap)으로 지시하면 로봇이 지도 서버에서 끌어오는(pull) 방식으로 배포되고, 정지 시간을 줄이려 지도를 미리 적재해 두었다가 enableMap 으로 따로 활성화하며, 다운로드가 실패·중단되면 동작 상태를 RETRIABLE 로 두고 관제 개입을 기다린다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.3.1절: 지도 서버의 파일을 로봇이 pull, 사전 적재·버퍼링 후 즉시 동작으로 활성화. 표 5 downloadMap: 실패·중단 시 RETRIABLE (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "VDA 5050 3.0.0 은 플릿 관제의 최소 기능에 문·게이트·승강기 같은 주변 시스템과의 통신과 통신 오류의 탐지·해소를 넣고, 로봇의 기능으로 위치 추정·경로 실행·동작 실행·상태 연속 전송을 두어 통신 오류 대응을 관제 쪽 책임으로 배치한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5.3절 관제 기능 목록에 'Detection and resolution of communication errors', 5.4절 로봇 기능 목록 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f11",
      "claim": "VDA 5050 3.0.0 은 주변 설비·기반 시설·외부 IT 시스템과의 인터페이스, 운영자·통합사·제조사·관제 공급자 사이의 운영 책임 배분, 보안 통신·데이터 보호의 사이버보안 조치를 범위 밖에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2장 범위: Other Communication Interfaces·Operational Responsibilities·Cybersecurity Measures 를 다루지 않는다고 명시 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "VDA 5050 3.0.0 의 waitForTrigger 동작에서 시간 초과 처리는 관제의 책임이며 필요하면 관제가 주문을 취소해야 하고, 로봇은 stateRequest 즉시 동작을 받으면 새 상태 메시지를 보낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.2.3.1절 표: waitForTrigger 는 관제가 타임아웃을 처리하고 필요 시 주문 취소, stateRequest 는 로봇에 새 상태 메시지를 요청 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "이번에 읽은 VDA 5050 3.0.0 명세 앞부분은 MQTT 3.1.1 을 최소 버전으로 두고 연결 확인을 유언 메시지와 하트비트로만 서술하며 MQTT 5.0 의 세션 만료 같은 기능을 쓰는 방법은 다루지 않아, 페이지 5절의 해당 '미확인' 서술은 그대로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 텍스트 207,642자 중 앞 119,109자 범위에서 MQTT 5.0 세션 만료 언급을 찾지 못함. 4장·6.5절은 MQTT 3.1.1 최소 버전, 유언·하트비트만 서술 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "VDA 5050 3.0.0 에서 주문·상태가 QoS 0 이고 connection 메시지가 retained 로 보내지며 stateRequest 즉시 동작이 있으므로, 재연결 뒤 관제는 connection 토픽의 ONLINE 전환을 받은 다음 stateRequest 나 다음 상태 메시지로 로봇 상태를 다시 세우고 끊긴 동안 해제된 베이스는 실행된 것으로 놓고 주문을 갱신하는 절차를 둘 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f3·f4·f12 의 명세 내용을 조합한 추론이며 명세가 재연결 절차를 직접 정한 것은 아니다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "VDA 5050 3.0.0 은 상태 보고의 최대 간격(30초)과 팩트시트의 최소 간격만 두고 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간 수치를 정하지 않으므로, oq-039 는 이 표준만으로 답이 되지 않는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "4장·6.6절에 손실·지연 전제와 보고 간격은 있으나 지연·손실률 허용치 수치는 읽은 범위에서 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "KubeEdge 는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-300"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KubeEdge README 의 엣지 자율성(edge autonomy) 서술. 이번 실행에서 원문을 다시 열지 않음 (발행일 미확인, 확인일 기준) (재인용: 2026-09-25-27)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "VDA 5050 은 클라우드 브로커 사용을 허용하지만(f8) 브로커와 끊긴 로봇은 해제된 노드까지만 진행하므로(f3), 관제와 브로커를 클라우드에 두면 외부망 단절이 곧 로봇–관제 단절이 되어 해제 구간 뒤에서 로봇이 멈추고, 현장 서버에 두면 엣지 자율 운영 구조(f16)처럼 현장 내 배정을 이어 갈 수 있어, 관제·브로커의 배치가 단절 중 운영 범위를 정하는 핵심 결정인 것으로 보인다(oq-038·oq-206 부분 근거, 41. 플랫폼 아키텍처·외부 API 와 연결).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-300"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 4.1·4.2절과 KubeEdge 엣지 자율성 서술을 대응시킨 추론. 물류센터·병원 등의 공개 운영 기준으로 확인한 것은 아니다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f18",
      "claim": "VDA 5050 의 구역 허가 만료(leaseExpiry)와 releaseLossBehavior 는 관제가 허가를 갱신하지 못하는 상황, 곧 관제 장애나 통신 단절 때 공용 구역 점유를 시간으로 제한하는 장치로 쓸 수 있을 것으로 보이나, 명세는 이를 통신 단절 대책으로 명시하지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "6.4.3절의 leaseExpiry 갱신·만료 규칙과 6.4.1.1절 releaseLossBehavior 에서 도출한 추론 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    }
  ],
  "sources": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문. 무선망 손실을 전제한 MQTT 전송 규약, QoS, 연결 토픽·유언 메시지, 주문의 베이스/호라이즌, 상태 보고 간격, 절전 모드, 구역 허가 만료, 지도 배포, 범위 제외 항목을 정한다(이번 실행은 앞 119,109자 범위를 읽음).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-300",
      "org": "KubeEdge (CNCF, kubeedge GitHub)",
      "title": "KubeEdge — README",
      "published": null,
      "url": "https://github.com/kubeedge/kubeedge",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 클라우드–엣지 연결이 끊겨도 엣지 노드와 애플리케이션이 자율 동작하는 쿠버네티스 기반 엣지 플랫폼 README(이전 실행 2026-09-25-27 확인 내용 재인용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "sections": [
        "5",
        "7",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 물류창고 시나리오의 제약·예외 행을 오늘 원문으로 재확인(f1·f3·f5), 연결 탐지·재연결 서술 보강(f4·f12·f14), MQTT 5.0 세션 만료 '미확인' 유지 근거(f13) / 섹션 7(주제 페이지로 분리된 절의 요약) — VDA 5050 의 QoS·보안 위임(f2), 연결 토픽 의미(f4), 상태 보고 간격(f5), 절전 모드(f6), 구역 허가 만료(f7), 클라우드 브로커 토픽 조정(f8), 지도 사전 적재(f9), KubeEdge 엣지 자율성 재확인(f16) / 섹션 9 — 통신 오류 탐지·해소와 시간 초과 처리를 관제(ROP) 쪽 책임으로(f10·f12), 외부 IT 인터페이스·사이버보안·운영 책임은 표준 범위 밖(f11) / 섹션 11 — oq-038·oq-206 부분 근거 f17, oq-039 미해결 근거 f15, 새 질문 1건(f18). 다음 실행 후보: 52. 통신 보호·위협 관리·감사(f2·f11), 27. 다중 로봇 경로·교통 관리 — MAPF(f7·f18)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "절전 모드",
      "term_en": "Hibernation (VDA 5050 startHibernation / HIBERNATING)",
      "definition": "VDA 5050 에서 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 주문을 지운 채 정지해 있다가 stopHibernation 이나 설정한 기상 시각에 정상 운용으로 돌아오는 통신 감축 상태다."
    },
    {
      "term_ko": "보존 메시지",
      "term_en": "MQTT Retained Message",
      "definition": "브로커가 토픽의 마지막 메시지를 보관했다가 나중에 구독한 클라이언트에게 곧바로 전달하게 하는 MQTT 발행 옵션으로, VDA 5050 은 연결 상태 메시지에 이를 쓰게 한다."
    }
  ],
  "open_questions_new": [
    "VDA 5050 구역 허가 만료 시각(leaseExpiry)과 허가 상실 시 동작(releaseLossBehavior)을 관제 장애·통신 단절 대책으로 쓸 때 만료 시간과 동작 값을 어떤 기준으로 정하는지 공개한 현장 사례나 지침이 있는가? | 관련 영역: 42. 분산 시스템·통신·컴퓨팅 구조, 27. 다중 로봇 경로·교통 관리 — MAPF | 근거: f18 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 2,
    "cross_checked_count": 0,
    "unverified": [
      "oq-038·oq-206 미해결: 외부망 단절 중 운영 범위를 정한 공개 운영 기준·사례 미확인(f17 은 추론)",
      "oq-039 미해결: 허용 지연·손실률·로밍 중단 시간 수치를 정한 표준·측정 자료 미확인(f15)",
      "oq-035·oq-040·oq-083·oq-310·oq-326 이번 재실행에서 미조사",
      "ref-031 원문 텍스트가 앞 119,109자 발췌라 7장 메시지 명세 뒷부분(팩트시트 protocolLimits 세부 등) 미확인",
      "ref-031 VDA 5050 3.0.0 발행일 미확인",
      "ref-300 은 이번 실행에서 원문을 다시 열지 않음",
      "섹션 5 병원·상업 시설·제조 공장·실외·기타 현장 사례 미조사"
    ],
    "scope_violations": [
      "f3·f10: 위치 추정·경로 실행과 끊김 중 로봇 주행은 로봇 자체 지능·제어 쪽 연계 대상이며, ROP 몫은 해제 구간 설정·통신 오류 탐지·상태 재구성으로 한정해 서술해야 함",
      "f2·f11: 브로커 보안·사이버보안 조치는 52. 통신 보호·위협 관리·감사 쪽이므로 이 영역에서는 '표준 범위 밖'이라는 사실만 씀",
      "f16·f17: 엣지 플랫폼·클라우드 인프라 자체는 외부 연계 대상이며 배치 결정은 41. 플랫폼 아키텍처·외부 API 와 함께 다뤄야 함"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 0
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치: f13 이 벤더 문서만 근거로 한 [사실] 인데 vendor_claim 표시 없음): 지시에 따라 새 조사 없이 형식만 고치려 했으나 직전 반환값이 입력에 포함되지 않아 그대로 수정할 수 없었다. 그래서 입력으로 받은 원문 텍스트(data/source_texts/ref-031.txt, fetched_via inbox)와 기존 페이지가 인용한 참고문헌(ref-300 재인용)만으로 브리프를 다시 구성했다. 새 f13 은 표준(ref-031)만 근거로 한 [추정]이다. 벤더 문서(CJ대한통운 ref-307, FreightWaves 기사 ref-309 등)를 근거로 한 finding 은 이번 브리프에 하나도 없으므로 vendor_claim 이 필요한 finding 이 없다. 검색 0회, WebFetch 0회, 신규 출처 0건으로 예약 구간 ref-1337~ref-1366 은 쓰지 않았다. 재사용 2건 중 ref-031 은 원문을 열었고(inbox), ref-300 은 원문 미열람으로 표시했다. 교차 확인 0건이며 모든 사실 finding 은 단일 출처라 신뢰도 medium 이하다. 갱신(update) 실행이고 정정 요청이 없어 약한 절(5·7·9·11절)만 다뤘다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-038·oq-206 은 f17, oq-039 는 f15. 현장 유형 사례 finding 은 없다(site_type 모두 null). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 MQTT·MQTT 유언 메시지·허가 만료 시각·CAP 정리·포그 컴퓨팅·5G 특화망은 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-18/verification.json

```json
{
  "run_id": "2026-10-09-18",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-031 원문(data/source_texts/ref-031.txt) 4장 — 무선망 전제·연결 실패·메시지 손실, MQTT+JSON, MQTT 3.1.1 최소 버전. 단일 출처. 기존 5절 제약 행과 같은 내용이므로 기존 문장과 ref-031 각주를 재사용한다. 3.0.0 발행일은 미확인 유지(벤더 게시물은 2026-02-17 채택이라 적지만 VDA 공식 발행일 미확인)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.1절 — 7개 토픽 QoS 0, connection QoS 1, 프로토콜 보안은 브로커 설정으로 고려하되 지침 범위 밖. 보안 부분은 52. 통신 보호·위협 관리·감사 연계 대상으로만 쓴다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.1절(주문 정보 유지·마지막 해제 노드까지 수행), 6.1.2절(베이스 변경 불가·실행된 것으로 가정, 취소 절차도 신뢰 불가). 기존 5절에 같은 직접 인용이 이미 있으므로 ref-031 의 두 번째 직접 인용을 만들지 않는다. 끊김 중 로봇 주행 자체는 로봇 자체 지능·제어(연계 대상)."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.3절 표 2(connection 은 연결 상실 표시, 관제가 로봇 건강 확인에 쓰지 않음, MQTT 프로토콜 수준 확인용), 6.5절(하트비트로 끊김 탐지, 유언 CONNECTION_BROKEN, 모든 메시지 retained)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.6절 — 사건 발생 시 또는 최소 30초마다 발행, 상관된 사건은 한 번의 갱신, 최소 간격은 팩트시트 protocolLimits.timing.minimumStateInterval. 30초 서술은 기존 5절과 겹치므로 기존 문장을 재확인 형태로 갱신한다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.2.3.1절 표 4 startHibernation — 브로커 연결 유지, 상태 메시지 중단, HIBERNATING 발행, 활성 주문 삭제, 정지, stopHibernation 에만 응답, 배터리 위급 시 오류 보고를 위해 자율 해제 가능, wakeUpTime 에 자율 해제. 에너지 측면은 28. 공용 자원·충전·에너지 최적화와 맞닿는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.4.1.1절 표 6 RELEASE·releaseLossBehavior(STOP·CONTINUE·EVACUATE, 미정의 시 STOP 과 오류), 6.4.3절(응답이 제때 오지 않으면 진입 금지, leaseExpiry, 갱신은 응답 재전송, 만료 시 EXPIRED). 용어는 용어집의 '해제 구역(Release Zone)'·'허가 만료 시각(leaseExpiry)'으로 맞춘다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.2절. 다만 원문은 클라우드 브로커에서도 제안 구조를 '대략 따라야 한다(should roughly follow)'고 덧붙이므로 이 단서를 함께 쓴다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 일반화. 6.3.1절의 지도 서버 pull 배포·사전 적재·enableMap 별도 활성화는 원문과 맞다. 그러나 6.3.3절은 다운로드가 실패하면 FAILED 로 정하고, 표 5 의 downloadMap 은 FAILED(연결 끊김·지도 서버 접근 불가 등)와 RETRIABLE(실패·중단 뒤 관제 개입 대기)을 따로 둔다. '실패·중단되면 RETRIABLE' 은 원문보다 넓다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 5.3절 관제 최소 기능(주변 시스템과의 통신, 통신 오류 탐지·해소)과 5.4절 로봇 기능. 단 마지막 구절 '관제 쪽 책임으로 배치한다'는 2장이 운영 책임 배분을 다루지 않는다고 밝힌 것과 어긋나므로 '관제의 최소 기능으로 둔다'로 고친다(수정 지시). VDA 5050 의 관제를 곧 ROP 로 보지 않는다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2장 범위 제외 목록(외부 IT·주변 설비 인터페이스, 운영 책임 배분, 사이버보안 조치). 원문은 안전 요구사항·교통 관리 로직·프로젝트 절차도 제외하지만 주장이 그 일부만 든 것은 문제가 아니다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.2.3.1절 표 4 — waitForTrigger 시간 초과는 관제 책임이고 필요하면 주문 취소, stateRequest 는 새 상태 메시지를 요청."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지): 브리프가 읽은 범위의 4장·6.5절은 MQTT 3.1.1 최소 버전과 유언·하트비트만 다룬다. 검증 중 원문 뒷부분(119,000자 이후)을 공식 저장소 raw 로 열어 보니 'MQTT 5'·'session expiry' 언급이 없었다. 5절의 '미확인' 문장은 그대로 둔다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지): f2·f3·f4·f12 의 조합 추론이다. 검증 중 원문 뒷부분을 확인했으나 CONNECTION_BROKEN 뒤 재연결 절차는 정해져 있지 않아 '명세가 직접 정하지 않는다'는 단서와 맞다. 기존 5절 마지막 단락의 [추정] 문장(ref-031·ref-306)과 겹치므로 그 문장을 보강한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지): 검증 중 원문 뒷부분을 열어 지연·손실률·로밍 중단 허용 수치가 전체 문서에 없음을 확인했다. 다만 팩트시트 protocolLimits.timing 에는 minimumStateInterval 외에 minimumOrderInterval·defaultStateInterval·visualizationInterval 도 있으므로 '최소 간격만 둔다'는 한정 표현은 고친다(수정 지시). oq-039 는 미해결로 둔다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 브리프는 원문 미열람(재인용)이었으나 검증 중 KubeEdge README 원문(raw)을 열어 Edge Autonomy 항목(클라우드–엣지 네트워크가 불안정하거나 엣지가 오프라인일 때 엣지 노드·애플리케이션이 정상 동작)을 확인했다. 기존 7절 문장과 같은 내용이므로 새 문장을 더하지 않는다. 엣지 플랫폼 자체는 연계 대상이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지): f3·f8·f16 과 6.1.2절(베이스가 늘지 않으면 결정 지점에서 정지)을 바탕으로 한 추론이며 공개 운영 기준으로 확인한 것은 아니다. oq-038·oq-206 의 해결 근거가 아니라 부분 근거다. 기존 5절의 가상 시나리오 [추정] 문장과 겹친다. 배치 결정은 41. 플랫폼 아키텍처·외부 API 와 연결한다. 브리프는 이 finding 의 source_unopened 를 false 로 적었으나 근거 출처 ref-300 은 브리프에서 원문 미열람이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(추정 유지): 6.4.3절의 leaseExpiry 갱신·만료 규칙과 releaseLossBehavior 에서 이끌어 낸 추론이며, 명세가 이를 통신 단절 대책으로 명시하지 않는다는 단서가 붙어 있다. 새 열린 질문의 근거로 적절하다."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": false,
    "issues": [
      "page_proposals 의 rationale: '통신 오류 탐지·해소와 시간 초과 처리를 관제(ROP) 쪽 책임으로(f10·f12)'는 VDA 5050 의 플릿 관제를 곧 ROP 로 본 것이다. 이종 제조사 연결 ROP 는 제조사 관제(20. 로봇·제조사 관제 연동)를 거칠 수도 있고, 2장은 운영 책임 배분을 다루지 않는다고 밝힌다. 9절은 'ROP 가 VDA 5050 관제 역할을 맡을 때' 같은 조건을 붙인 [추정]으로 써야 한다.",
      "f3·f10: 끊김 중 로봇의 주행·위치 추정·경로 실행은 로봇 자체 지능·제어(연계 대상)다. ROP 몫은 해제 구간(베이스) 길이 설정, 통신 오류 탐지, 재연결 뒤 상태 재구성으로 한정한다.",
      "f2·f11: 브로커 보안·사이버보안 조치는 52. 통신 보호·위협 관리·감사 쪽이다. 이 영역에서는 '표준 범위 밖'이라는 사실만 쓴다.",
      "f16·f17: 엣지 플랫폼(KubeEdge)과 클라우드 인프라 자체는 연계 대상이다. 관제·브로커 배치 결정은 41. 플랫폼 아키텍처·외부 API 와 함께 다룬다."
    ]
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "f1·f3·f5: 기존 5절 제약·예외·성과 행과 마지막 단락에 같은 내용(무선망 전제·QoS 0, 해제 노드까지 수행, 30초 보고)이 ref-031 로 이미 있다. 새 문장을 더하지 않고 기존 문장을 재확인한 것으로 처리하고 ref-031 각주를 재사용한다.",
      "f14: 기존 5절 마지막 단락의 [추정] 문장('재연결 뒤 관제는 … 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신하는 구조가 필요할 것으로 보인다', ref-031·ref-306)과 겹친다.",
      "f16: 기존 7절 둘째 문장(KubeEdge 엣지 자율 동작, ref-300)과 같다.",
      "f17: 기존 5절의 가상 시나리오 [추정] 문장(현장 서버에 관제·브로커를 둔 경우, ref-031·ref-300·ref-301·ref-310)과 겹친다.",
      "f2·f3·f8·f10·f11: 같은 날 실행 2026-10-09-17(41. 플랫폼 아키텍처·외부 API) 브리프의 f2·f3·f5·f7·f6 과 같은 출처·같은 내용이다. 충돌은 없으며 페이지 사이에는 연결만 한다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f7 의 'RELEASE 구역'은 용어집 release-zone '해제 구역 (Release Zone)'으로 쓴다. leaseExpiry 는 용어집 lease-expiry '허가 만료 시각'을 쓴다.",
      "용어 후보 '보존 메시지(MQTT Retained Message)': 정의의 MQTT 일반 동작(브로커가 마지막 메시지를 보관했다가 새 구독자에게 전달)을 뒷받침하는 finding 이 없다. ref-031 은 retained 플래그 사용만 정한다. 이번 실행에서는 등록하지 않는다.",
      "용어 후보 '절전 모드(Hibernation)': 기존 용어와 충돌하지 않는다. 정의는 f6 과 같게, 배터리 위급 시 자율 해제를 포함해 쓴다."
    ]
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f9: [사실] → [추정]으로 강등하고, 다운로드 실패 처리 구절을 '실패하면 FAILED(연결 끊김·지도 서버 접근 불가 등)로, 실패·중단 뒤 관제 개입을 기다릴 때는 RETRIABLE 로 보고한다'로 원문의 두 상태를 모두 밝혀 쓴다 — 6.3.3절과 표 5 는 FAILED 와 RETRIABLE 을 따로 두므로 'RETRIABLE 로 둔다'는 일반화다.",
    "f10: 마지막 구절 '통신 오류 대응을 관제 쪽 책임으로 배치한다'를 '통신 오류의 탐지·해소를 플릿 관제의 최소 기능 목록에 둔다'로 바꾼다 — VDA 5050 2장은 운영 책임 배분을 다루지 않는다고 밝힌다.",
    "9절: f10·f12 를 근거로 쓸 때 'VDA 5050 의 관제 = ROP'로 쓰지 않는다. 'ROP 가 VDA 5050 플릿 관제 역할을 맡을 때 통신 오류 탐지·해소와 waitForTrigger 시간 초과 처리가 ROP 몫이 될 것으로 보인다'처럼 [추정]으로 쓰고, 제조사 관제를 거치는 경우는 20. 로봇·제조사 관제 연동에 연결한다 — 이종 제조사를 연결하는 ROP 는 제조사 관제에 실행을 맡길 수 있다(분류 원문 19장).",
    "9절·5절: f3 의 끊김 중 로봇 주행은 로봇 자체 지능·제어 쪽 연계 대상으로 쓴다. ROP 직접 범위는 해제 구간(베이스) 길이 설정, 통신 오류 탐지, 재연결 뒤 상태 재구성으로 한정한다 — 범위 경계(분류 원문 19장).",
    "f2·f11: 브로커 보안·사이버보안은 'VDA 5050 범위 밖'이라는 사실만 적고 52. 통신 보호·위협 관리·감사로 연결한다. ROP 직접 범위처럼 서술하지 않는다.",
    "f16·f17: KubeEdge·엣지 플랫폼은 연계 대상으로 쓰고, 관제·브로커를 클라우드와 현장 서버 가운데 어디에 둘지는 41. 플랫폼 아키텍처·외부 API 와 함께 다룬다고 연결한다.",
    "f15: '상태 보고의 최대 간격(30초)과 팩트시트의 최소 간격만 두고'의 한정 표현을 'VDA 5050 3.0.0 은 메시지 간격 규정 외에 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간 수치를 정하지 않으므로'로 바꾼다 — 팩트시트 protocolLimits.timing 에는 minimumStateInterval 외의 간격 항목도 있다(검증 중 원문 확인). [추정] 태그는 그대로 둔다.",
    "f8: '개별 조정 허용' 뒤에 '제안 구조를 대략 따르도록 한다'는 원문 단서를 붙인다 — 4.2절은 'should roughly follow the proposed structure'라고 쓴다.",
    "f7·f18: 'RELEASE 구역'을 용어집 표기 '해제 구역(RELEASE 구역)'으로, leaseExpiry 를 '허가 만료 시각(leaseExpiry)'으로 쓴다 — 용어집 release-zone·lease-expiry 와 맞춘다.",
    "f1·f3·f5: 5절의 기존 같은 내용 문장은 새로 쓰지 말고 그대로 두되, ref-031 각주 정의의 접근일을 2026-10-09 로 바꾼다 — 같은 주장에 기존 각주를 재사용한다.",
    "f3: ref-031 에서 새 직접 인용을 만들지 않는다 — 5절에 이미 'fulfills the order up to the last released node' 인용이 있으며 출처당 직접 인용은 1회다.",
    "f14: 새 문장을 더하지 말고 5절 마지막 단락의 기존 [추정] 문장(재연결 뒤 상태 재구성)에 'connection 토픽의 ONLINE 전환과 stateRequest 즉시 동작을 쓸 수 있고, 명세가 재연결 절차를 직접 정하지는 않는다'를 보강해 [추정][^ref-031] 로 둔다.",
    "f16: 7절의 기존 KubeEdge 문장과 같으므로 문장을 추가하지 않는다. ref-300 각주 줄은 기존 줄(접근일 2026-09-25)을 그대로 두고 reference_updates 에 ref-300 을 넣지 않는다 — 이번 브리프에서는 원문 미열람 재인용이다.",
    "f17: 5절의 가상 시나리오 문장을 다시 쓰지 말고, 9절 또는 11절에서 oq-038·oq-206 의 부분 근거로만 [추정]으로 쓴다. 해결로 표시하지 않는다.",
    "f6·f7·f9: 이 영역에서는 끊김·통신 감축 대비 장치로만 서술한다. 구역·지도·충전 관리 자체 내용은 27. 다중 로봇 경로·교통 관리 — MAPF, 16. 장소 의미·지도 관리, 28. 공용 자원·충전·에너지 최적화로 연결만 한다.",
    "5절: 'VDA 5050이 MQTT 5.0의 세션 만료 같은 장치를 어떻게 쓰는지는 미확인이다' 문장은 유지한다(f13). 필요하면 '명세는 MQTT 3.1.1 을 최소 버전으로 두고 유언·하트비트만 서술한다 [추정][^ref-031]'를 덧붙인다.",
    "11절: oq-038·oq-039·oq-206 은 열림 상태를 유지하고 각각 부분 근거(f17, f15, f17)만 적는다. 새 열린 질문 1건(f18, 관련 영역 42. 분산 시스템·통신·컴퓨팅 구조, 27. 다중 로봇 경로·교통 관리 — MAPF, 종류 일반)은 등록한다.",
    "glossary_updates: '절전 모드(Hibernation)'는 f6 과 같게 '배터리 위급 시나 설정한 기상 시각에 스스로 벗어날 수 있다'를 포함해 등록한다. '보존 메시지(MQTT Retained Message)'는 등록하지 않는다 — 정의의 MQTT 일반 동작을 뒷받침하는 finding 이 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 17건, 미확인 1건, 교차 확인 0건. 강등: f9 사실 → 추정(지도 다운로드 실패 상태를 RETRIABLE 로 일반화. 원문은 FAILED 와 RETRIABLE 을 따로 둔다). 원문 미열람 출처: ref-300(브리프 기준 재인용. 검증 중 KubeEdge README 원문을 열어 엣지 자율성 서술을 확인했다). 주의: 사실 주장이 모두 VDA 5050 3.0.0 명세(ref-031) 한 출처에 기대므로 신뢰도는 medium 이다. VDA 5050 의 플릿 관제는 곧 ROP 가 아니며, 명세는 운영 책임 배분과 사이버보안을 범위 밖에 둔다. 외부망 단절 중 운영 범위(oq-038·oq-206)와 허용 지연·손실률(oq-039)은 공개 기준을 찾지 못해 열려 있다. 검증 중 원문 뒷부분을 확인했으나 MQTT 5.0 세션 만료, 재연결 절차, 지연·손실률 수치는 명세 어디에도 없었다. VDA 5050 3.0.0 의 공식 발행일은 미확인이다(벤더 게시물은 2026-02-17 채택이라 적는다). 이번 재실행은 검색 0회로 입력 원문만 써서 한국어·영어 검색과 현장 유형 사례 조사를 하지 않았다. 5절 적용 사례는 여전히 물류창고 1건뿐이다. 브리프의 ref-031 fetched_via(github_raw)는 한계 서술의 inbox 와 어긋나고 fetch_url 이 비어 있으나, 입력 원문 텍스트로 열람을 확인했다. 정정 요청 없음. 검증 사용량: 검색 1회, 열람 2회.",
  "retry_reason": null
}
```

### runs/2026-10-09-18/pages.json

```json
{
  "run_id": "2026-10-09-18",
  "outline": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "변경 없음. 연결 단절이 운영 중단 원인으로 보고되나 근거는 판매사 조사 수준이다. [추정][^ref-309]"
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 150,
      "summary": "변경 없음. 주제 페이지로 분리된 절의 요약과 링크."
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1600,
      "summary": "물류창고 피킹 운반 중 외부망·무선망 단절 사례. 마지막 단락에 끊김 중 주행의 연계 대상 표시, 재연결 뒤 상태 재구성 보강(ONLINE 전환·stateRequest), MQTT 5.0 미확인 유지 근거를 더했다. [추정][^ref-031]",
      "planned_findings": [
        "f1",
        "f3",
        "f5",
        "f13",
        "f14"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 150,
      "summary": "변경 없음. 주제 페이지로 분리된 절의 요약과 링크."
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2300,
      "summary": "VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한 통신 방식을 정한다. [사실][^ref-031] 이번에 QoS·연결 토픽·상태 보고 간격·절전 모드·해제 구역 허가 만료·클라우드 브로커 토픽·지도 사전 적재를 끊김 대비 장치로 정리했다.",
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f18"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 150,
      "summary": "변경 없음. 주제 페이지로 분리된 절의 요약과 링크."
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1900,
      "summary": "ROP는 통신 품질 요구·연결 상태 감시·재연결 뒤 상태 재구성을 맡고 무선망과 로봇 주행은 연계 대상으로 두는 것으로 보인다. [추정][^ref-031][^ref-307] VDA 5050 의 플릿 관제가 곧 ROP 는 아니며, 명세는 운영 책임 배분·사이버보안을 범위 밖에 둔다. [사실][^ref-031]",
      "planned_findings": [
        "f3",
        "f10",
        "f11",
        "f12",
        "f2",
        "f16"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "기존 요약·링크를 두고, 이번 갱신이 새로 잇는 16·20·27·28·41·52번 영역을 덧붙였다. [의견]"
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "section": "11. 열린 질문",
      "budget_chars": 1300,
      "summary": "oq-038·oq-206 에 관제·브로커 배치 추론(부분 근거), oq-039 에 지연·손실률 수치 부재(부분 근거)를 적고 해결로 보지 않는다. 해제 구역 허가 만료를 단절 대책으로 쓰는 기준을 새 질문으로 올렸다. [추정][^ref-031]",
      "planned_findings": [
        "f15",
        "f17",
        "f18"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 5절 마지막 단락 보강(끊김 중 주행 연계 대상, 재연결 상태 재구성, MQTT 5.0 미확인 근거), 7절에 VDA 5050 3.0.0 끊김·통신 감축 대비 장치 정리 추가, 9절 책임 경계 조건부 서술·범위 밖 항목 추가, 10절 연결 영역 6개 추가, 11절 열린 질문 id 표기·부분 근거·새 질문 1건, 13절 ref-031 접근일 갱신",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              16,
              18,
              20,
              23,
              27,
              28,
              29,
              32,
              35,
              41,
              47,
              51,
              52
            ],
            "confidence": "medium",
            "last_run": "2026-10-09"
          },
          "content": "(절 본문 생략 — runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area42-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 42. 분산 시스템·통신·컴퓨팅 구조 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,178자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area42-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 42. 분산 시스템·통신·컴퓨팅 구조 의 \"11. 열린 질문\" 절(1,376자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area42-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 42. 분산 시스템·통신·컴퓨팅 구조 의 \"3. 왜 중요한가\" 절(675자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area42-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 42. 분산 시스템·통신·컴퓨팅 구조 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(606자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 42. 분산 시스템·통신·컴퓨팅 구조 | 5·7·9·10·11·13절 차등 갱신: VDA 5050 3.0.0 끊김 대비 장치(QoS·연결 토픽·상태 보고 간격·절전 모드·해제 구역 허가 만료·클라우드 브로커 토픽·지도 사전 적재) 정리, 책임 경계 조건부 서술, 열린 질문 부분 근거와 새 질문 1건, 조건부 승인 수정 18건 이행 | run 2026-10-09-18",
  "index_updates": {
    "home_recent": "2026-10-09 — 42. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 3.0.0 원문을 다시 읽어 끊김·통신 감축 대비 장치와 책임 경계를 보강하고 열린 질문에 부분 근거를 더했다",
    "category_recent": "2026-10-09 — 42. 분산 시스템·통신·컴퓨팅 구조: 5·7·9·11절 갱신(VDA 5050 연결 토픽·QoS·절전 모드·해제 구역 허가 만료·지도 사전 적재, 플릿 관제와 ROP 의 구분, oq-038·oq-039·oq-206 부분 근거, 새 질문 1건)",
    "area_recent": "2026-10-09 — 42. 분산 시스템·통신·컴퓨팅 구조: 5절 재연결 서술 보강, 7절 VDA 5050 3.0.0 끊김 대비 장치 정리, 9절 책임 경계 조건부 서술·범위 밖 항목, 10절 연결 영역 6개 추가, 11절 부분 근거와 새 질문 1건, 조건부 승인 수정 18건 이행"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "vda-5050-hibernation",
      "term_ko": "절전 모드",
      "term_en": "Hibernation (VDA 5050 startHibernation / HIBERNATING)",
      "definition": "VDA 5050 에서 로봇이 브로커 연결은 유지하되 상태 메시지 발행을 멈추고 연결 상태를 HIBERNATING 으로 알리며 활성 주문을 지운 채 정지해 있다가, stopHibernation 을 받거나 배터리가 위급할 때나 설정한 기상 시각(wakeUpTime)이 되면 스스로 벗어날 수 있는 통신 감축 상태다.",
      "description": "VDA 5050 3.0.0 의 startHibernation 즉시 동작으로 들어간다. 이 상태의 로봇은 stopHibernation 에만 응답한다. 42. 분산 시스템·통신·컴퓨팅 구조에서는 통신 감축 장치로, 28. 공용 자원·충전·에너지 최적화에서는 배터리 측면으로 다룬다.",
      "related_areas": [
        42,
        28
      ],
      "sources": [
        "ref-031"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문. 무선망 손실을 전제한 MQTT 전송 규약, QoS, 연결 토픽·유언 메시지, 주문의 베이스/호라이즌, 상태 보고 간격, 절전 모드, 구역 허가 만료, 지도 배포, 범위 제외 항목을 정한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "VDA 5050 해제 구역(RELEASE 구역)의 허가 만료 시각(leaseExpiry)과 허가 상실 시 동작(releaseLossBehavior)을 관제 장애·통신 단절 대책으로 쓸 때 만료 시간과 동작 값을 어떤 기준으로 정하는지 공개한 현장 사례나 지침이 있는가?",
      "areas": [
        42,
        27
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시",
      "title": "42. 분산 시스템·통신·컴퓨팅 구조"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시",
      "title": "42. 분산 시스템·통신·컴퓨팅 구조"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시",
      "title": "42. 분산 시스템·통신·컴퓨팅 구조"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시",
      "title": "42. 분산 시스템·통신·컴퓨팅 구조"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시",
      "title": "42. 분산 시스템·통신·컴퓨팅 구조"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#5-적용-사례-현장-유형-명시",
      "title": "42. 분산 시스템·통신·컴퓨팅 구조"
    }
  ],
  "additional_research_requests": [
    "5. 적용 사례 (현장 유형 명시): 병원·상업 시설·제조 공장·실외·기타 현장에서 관제·통신 단절 때 로봇 동작과 작업 재배정을 다룬 공개 사례가 필요하다 — 현재 사례가 물류창고 1건뿐이고 이번 재실행은 검색 0회였다(oq-326 과 연결).",
    "11. 열린 질문 oq-038·oq-206: 외부망 단절 중 운영 범위를 정한 물류센터·병원 등의 공개 운영 기준이나 사례가 필요하다 — 현재 근거는 VDA 5050 과 KubeEdge 문서를 대응시킨 추론(f17)뿐이다.",
    "11. 열린 질문 oq-039: 로봇 관제 통신의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 필요하다 — VDA 5050 3.0.0 에는 이 수치가 없다(f15).",
    "7. 관련 표준·프레임워크·오픈소스: VDA 5050 3.0.0 의 공식 발행일 확인이 필요하다 — 각주 발행일이 미확인이며 벤더 게시물의 2026-02-17 채택 일자는 VDA 공식 자료로 확인하지 못했다.",
    "5·9절: VDA 5050 기반 관제 구현(오픈소스 포함)이 CONNECTION_BROKEN 뒤 재연결 절차(ONLINE 전환 확인, stateRequest, 주문 갱신)를 실제로 어떻게 두는지 확인할 자료가 필요하다 — 명세가 재연결 절차를 직접 정하지 않아 현재 서술은 추정이다.",
    "13. 참고 자료: ref-300(KubeEdge README)은 브리프 기준 원문 미열람 재인용이었으므로 다음 실행에서 원문을 열어 각주 접근일을 갱신할 필요가 있다."
  ],
  "fixes_applied": [
    "f9 강등 — 7절 '지도 사전 적재' 항목을 [추정][^ref-031]으로 쓰고, 다운로드 실패 처리를 'FAILED(연결 끊김·지도 서버 접근 불가 등)'와 '실패·중단 뒤 관제 개입 대기 시 RETRIABLE' 두 상태로 나눠 썼다.",
    "f10 표현 수정 — 9절에서 '통신 오류의 탐지·해소를 플릿 관제의 최소 기능 목록에 둔다'로 쓰고 '관제 쪽 책임으로 배치한다'는 쓰지 않았다.",
    "9절 VDA 5050 관제≠ROP — 'ROP가 VDA 5050 플릿 관제 역할을 맡을 때 통신 오류 탐지·해소와 waitForTrigger 시간 초과 처리가 ROP 몫이 될 것으로 보인다'를 [추정][^ref-031]으로 쓰고, 제조사 관제를 거치는 경우는 20. 로봇·제조사 관제 연동으로 연결했다.",
    "9절·5절 끊김 중 주행 — 5절 마지막 단락과 9절 표·본문에 끊긴 동안의 주행·위치 추정·경로 실행을 로봇 자체 지능·제어 쪽 연계 대상으로 쓰고, ROP 직접 범위를 해제 구간(베이스) 길이 설정·통신 오류 탐지·재연결 뒤 상태 재구성으로 한정했다.",
    "f2·f11 보안 — 7절과 9절에 브로커 보안·사이버보안이 VDA 5050 범위 밖이라는 사실만 [사실][^ref-031]로 적고 52. 통신 보호·위협 관리·감사로 연결했다.",
    "f16·f17 — 9절에 KubeEdge 같은 엣지 플랫폼과 클라우드 인프라를 연계 대상으로 쓰고, 관제·브로커 배치는 41. 플랫폼 아키텍처·외부 API 와 함께 다룬다고 연결했다(7절 브로커 항목에도 같은 연결).",
    "f15 표현 수정 — 11절 oq-039 부분 근거를 'VDA 5050 3.0.0 은 메시지 간격 규정 외에 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간 수치를 정하지 않으므로'로 쓰고 [추정] 태그를 유지했다.",
    "f8 단서 — 7절 '클라우드 브로커의 토픽 구조' 항목에 '제안 구조를 대략 따르도록 한다'를 붙였다.",
    "f7·f18 용어 — 7절과 11절에서 '해제 구역(RELEASE 구역)', '허가 만료 시각(leaseExpiry)'으로 쓰고 용어집 release-zone·lease-expiry 를 링크했다.",
    "f1·f3·f5 중복 — 5절의 기존 같은 내용 문장(무선망 전제·QoS 0, 해제 노드까지 수행, 30초 보고)은 새로 쓰지 않고 그대로 두었으며, 13절 ref-031 각주 접근일을 2026-10-09 로 바꿨다.",
    "f3 직접 인용 — ref-031 에서 새 직접 인용을 만들지 않았다(5절 기존 인용 1회만 유지, 9절의 베이스·취소 서술은 재서술).",
    "f14 — 새 문장을 더하지 않고 5절 마지막 단락의 기존 [추정] 문장에 'connection 토픽의 ONLINE 전환과 stateRequest 즉시 동작'과 '명세가 이 재연결 절차를 직접 정하지는 않는다'를 보강해 [추정][^ref-031]로 두었다.",
    "f16 — 7절 기존 KubeEdge 문장에 문장을 더하지 않았고, ref-300 각주 줄은 기존 접근일 2026-09-25 그대로 두었으며 reference_updates 에 ref-300 을 넣지 않았다.",
    "f17 — 5절 가상 시나리오 문장은 다시 쓰지 않고, 11절 oq-038·oq-206 의 부분 근거로만 [추정][^ref-031][^ref-300]으로 쓰며 해결로 표시하지 않았다.",
    "f6·f7·f9 — 7절에서 끊김·통신 감축 대비 장치로만 서술하고 충전·에너지는 28. 공용 자원·충전·에너지 최적화, 구역 교통은 27. 다중 로봇 경로·교통 관리 — MAPF, 지도 관리는 16. 장소 의미·지도 관리로 연결만 했다.",
    "5절 MQTT 5.0 — '미확인이다' 문장을 유지하고 그 뒤에 '명세는 MQTT 3.1.1을 최소 버전으로 두고 연결 확인은 유언 메시지와 하트비트로만 서술한다. [추정][^ref-031]'을 덧붙였다.",
    "11절 — oq-038·oq-039·oq-206 을 열림으로 유지하고 각각 부분 근거(f17, f15, f17)만 적었으며, 새 열린 질문 1건(f18, 관련 영역 42·27, 종류 일반)을 본문과 open_question_updates 에 등록했다.",
    "glossary_updates — '절전 모드(Hibernation)'를 배터리 위급 시나 설정한 기상 시각에 스스로 벗어날 수 있다는 내용을 포함해 등록했고, '보존 메시지(MQTT Retained Message)'는 등록하지 않았다.",
    "분량 초과 자동 분리: 42. 분산 시스템·통신·컴퓨팅 구조 본문 8,454자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 4,351자"
  ]
}
```

### runs/2026-10-09-18/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md (6개 절)
- 분량 초과 자동 분리:
    - docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area42-s7.md (2,178자)
    - docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area42-s11.md (1,376자)
    - docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md "3. 왜 중요한가" → docs/topics/2026/2026-10-09-area42-s3.md (675자)
    - docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-09-area42-s10.md (606자)
```

### runs/2026-10-09-18/pages/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 42
related_areas: [16, 18, 20, 23, 27, 28, 29, 32, 35, 41, 47, 51, 52]
tags: [VDA 5050, MQTT, Zenoh, 엣지 컴퓨팅, 포그 컴퓨팅, CAP 정리]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-09
sources: [ref-031, ref-256, ref-300, ref-301, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-311]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 42. 분산 시스템·통신·컴퓨팅 구조

# 42. 분산 시스템·통신·컴퓨팅 구조

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

연결이 끊기면 자동화 자산이 멈추는 일이 창고 운영 중단의 한 원인으로 보고되지만, 그 근거는 아직 판매사 조사 수준이다. [추정][^ref-309] 하이브리드 WMS(창고 관리 시스템, Warehouse Management System) 판매사 Synergy Logistics의 조사 주장을 전한 FreightWaves 기사에 따르면, 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 한 번 이상 겪었고 절반 가까이는 소프트웨어·연결 중단으로 자동화 자산이 멈췄다. [추정][^ref-309]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 왜 중요한가](../../topics/2026/2026-10-09-area42-s3.md)에 있다.

## 4. 핵심 개념과 용어

2절의 질문을 다루려면 계산 계층, 분산 시스템의 이론적 한계, 통신 품질을 가리키는 용어를 먼저 맞춰야 한다. 아래 용어는 이 페이지 전체에서 같은 뜻으로 쓴다.

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area11-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 운반 도중 현장과 클라우드를 잇는 외부망이 끊김

| 항목 | 내용 |
|---|---|
| 시작 조건 | 클라우드 WMS가 내린 피킹 주문으로 ROP가 운반 작업을 만들어 로봇에 배정했고, 운반 도중 외부망이 끊긴다. |
| 작업 대상 | 피킹한 상품을 담은 토트·박스 |
| 수행 자원 | 현장 서버의 관제·브로커가 배정과 로봇 통신을 맡고 로봇은 받은 경로를 주행한다. Open-RMF free_fleet는 로봇마다 Zenoh 브리지를 두고 라우터를 플릿 어댑터와 같은 네트워크에서 실행하는 구성을 공개한다. [사실][^ref-256] |
| 제약 | VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제하고 주문·상태 토픽에 재전송 없는 MQTT QoS 0을 쓴다. [사실][^ref-031] 공장 자동화 같은 초저지연 서비스는 종단 간 10ms 미만 지연을 요구한다고 정리된다(2020년 논문 기준). [사실][^ref-311] |
| 완료·인계 | 단절 중에는 클라우드 WMS의 새 주문 수신과 재고 확정이 멈추고, 재연결 뒤 현장 완료 기록을 WMS 기록과 맞춰야 할 것으로 보인다. [추정][^ref-310] |
| 예외·성과 | 로봇은 브로커와 끊겨도 이미 해제된 노드까지 주문을 수행한다. [사실][^ref-031] 재연결 뒤 관제는 다음 상태 메시지로 로봇 상태를 다시 세워야 할 것으로 보인다. [추정][^ref-031][^ref-306] |

다음은 설명을 위한 가상의 시나리오이다. 관제와 브로커를 현장 서버에 두었다면 외부망 단절 중에도 이미 받은 주문과 현장 내 배정은 이어 갈 수 있으나, 클라우드 WMS의 새 주문 수신과 재고 확정은 멈추고 CAP 제약에 따라 단절 중 현장 기록과 WMS 기록을 재연결 뒤 맞추는 절차가 필요할 것으로 보인다. [추정][^ref-031][^ref-300][^ref-301][^ref-310] 이 판단은 로봇·엣지 플랫폼 문서를 대응시킨 추론이며, 물류센터의 외부망 단절 운영 기준이나 공개 사례로 확인한 것은 아니다.

현장 무선망이 끊기는 경우는 사정이 다르다. VDA 5050 3.0.0에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 "fulfills the order up to the last released node" — 곧 해제된 베이스까지만 수행하고 해제되지 않은 호라이즌 구간은 주행하지 않는다. [사실][^ref-031] 끊긴 동안 로봇이 해제 구간을 주행하는 일 자체는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이며, ROP가 맡는 몫은 9절에서 나눈다. [추정][^ref-031] 주문·상태가 QoS 0이고 상태는 사건 발생 시와 적어도 30초마다(최대 간격 30초) 다시 보내므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 전달되리라 기대하기보다 connection 토픽의 ONLINE 전환과 stateRequest 즉시 동작, 또는 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신하는 구조가 필요할 것으로 보이며, 명세가 이 재연결 절차를 직접 정하지는 않는다. [추정][^ref-031] VDA 5050이 MQTT 5.0의 세션 만료 같은 장치를 어떻게 쓰는지는 미확인이다. 명세는 MQTT 3.1.1을 최소 버전으로 두고 연결 확인은 유언 메시지와 하트비트로만 서술한다. [추정][^ref-031]

## 6. 대표 접근법과 기술

공개 자료가 다루는 접근법은 분산 발견과 라우터 연결, 손실을 전제한 메시지 설계, 엣지의 단절 중 운영, 클라우드·포그로의 계산 이전, 관제 서버 가용성과 다거점 구성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area11-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한 통신 방식을 정한다. [사실][^ref-031] KubeEdge는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다. [사실][^ref-300]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area42-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 학술 자료는 계산 계층 모델, 분산 시스템의 이론적 한계, 클라우드 로보틱스, 초저지연 무선 통신으로 나뉜다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 연구와 자료](../../topics/2026/2026-09-25-area11-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 명령·상태 메시지의 통신 품질 요구, 연결 상태 감시, 재연결 뒤 상태 재구성을 맡고, 무선망 구축과 로봇 탑재 주행·회피는 연계 대상으로 두는 것으로 보인다. [추정][^ref-031][^ref-307]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 외부망 단절 중 이미 받은 주문·현장 내 배정의 지속 범위 판단, 재연결 뒤 완료·재고 기록을 WMS와 맞추는 절차 [추정][^ref-310] | 클라우드 WMS의 새 주문 발행·재고 확정(연계 대상) |
| 로봇 자체 지능·제어 | 해제 구간(베이스) 길이 설정, 명령·상태 메시지의 통신 품질 요구, last will 등을 이용한 연결 상태 감시(통신 오류 탐지), 재연결 뒤 상태 재구성 [추정][^ref-031] | 로봇 탑재부의 실시간 주행·회피와 인식·계획 계산(클라우드·포그로 옮기는 연구 포함)은 연계 대상이다 [추정][^ref-304][^ref-308] 끊긴 동안 해제 구간을 주행하는 일도 로봇 쪽 연계 대상이다 [추정][^ref-031] |

VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신과 통신 오류의 탐지·해소를 플릿 관제의 최소 기능 목록에 두고, 로봇의 기능으로 위치 추정·경로 실행·동작 실행·상태 연속 전송을 둔다. [사실][^ref-031] waitForTrigger 동작의 시간 초과 처리는 관제의 책임이며 필요하면 관제가 주문을 취소해야 하고, 로봇은 stateRequest 즉시 동작을 받으면 새 상태 메시지를 보낸다. [사실][^ref-031] 또 관제는 MQTT 가 비동기이고 무선 전송을 믿을 수 없으므로 이미 해제한 베이스를 바꿀 수 없어 실행된 것으로 간주해야 하며, 주문 취소(cancelOrder)도 같은 이유로 신뢰할 수 없는 것으로 본다. [사실][^ref-031]

다만 이 명세는 주변 설비·기반 시설·외부 IT 시스템과의 인터페이스, 운영자·통합사·제조사·관제 공급자 사이의 운영 책임 배분, 보안 통신·데이터 보호 같은 사이버보안 조치를 범위 밖에 둔다. [사실][^ref-031] 그래서 VDA 5050 의 플릿 관제가 곧 ROP 인 것은 아니다. [의견] ROP가 VDA 5050 플릿 관제 역할을 맡을 때 통신 오류 탐지·해소와 waitForTrigger 시간 초과 처리가 ROP 몫이 될 것으로 보인다. [추정][^ref-031] 제조사 관제에 실행을 맡기는 경우의 몫 나눔은 [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)에서 다룬다. 사이버보안 조치는 [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)에서 다룬다.

끊긴 동안 로봇의 주행·위치 추정·경로 실행은 로봇 자체 지능·제어 경계의 연계 대상이고, 이 영역에서 ROP 직접 범위는 해제 구간(베이스) 길이 설정, 통신 오류 탐지, 재연결 뒤 상태 재구성으로 한정하는 것으로 보인다. [추정][^ref-031] KubeEdge 같은 엣지 플랫폼과 클라우드 인프라 자체는 연계 대상이고, 관제·브로커를 클라우드와 현장 서버 가운데 어디에 둘지는 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md)와 함께 다룬다. [의견]

무선망(와이파이·5G 특화망) 구축·운영은 분류 원문 19장 표에 명시된 항목은 아니지만, ROP가 소유하지 않는 통신 기반 연계 대상에 가까운 것으로 보인다. [추정][^ref-307] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에서 본다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 통신·계산 배치 결정은 관제 연동, 명령 신뢰성, 세계 상태, 업무 연속성과 직접 맞물린다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area42-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 열린 질문 가운데 이번 갱신이 부분 근거를 더한 것과 새로 올린 것은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 열린 질문](../../topics/2026/2026-10-09-area42-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md) — 섹션 3~11 신규 작성(외부망 단절 운영 범위, VDA 5050 무선망 전제·QoS·베이스/호라이즌, ROS 2 DDS·Zenoh, 엣지 단절 운영, 계산 배치 선례, 피킹 시나리오), 페이지 상태 표식 추가, 조건부 승인 수정 16건 이행, 4·6·7·8·10절 주제 페이지 분리 상태 유지. 2차 수정: 7절 첫 문장을 VDA 5050·KubeEdge 두 사례에 한정한 [사실] 문장으로 교체 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area11-s6.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "6. 대표 접근법과 기술" 절(2,039자)을 옮겼다 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area11-s4.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "4. 핵심 개념과 용어" 절(1,171자)을 옮겼다 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 연구와 자료](../../topics/2026/2026-09-25-area11-s8.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "8. 대표 연구와 자료" 절(855자)을 옮겼다. 2차 수정: NIST 항목의 쓰임새 평가를 [의견]으로, Gilbert·Lynch 항목의 적용 구절을 [추정]으로 분리 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area11-s7.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "7. 관련 표준·프레임워크·오픈소스" 절(769자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장의 '대부분' 일반화를 VDA 5050·KubeEdge 두 사례에 한정한 [사실] 문장으로 교체 (실행 2026-09-25-27)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-256]: Open Robotics (open-rmf), free_fleet — README (A free fleet management system), 미확인, https://github.com/open-rmf/free_fleet, 접근일 2026-09-25
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25
[^ref-301]: Microsoft, Operate Azure IoT Edge devices offline, 2026-03-02, https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities, 접근일 2026-09-25
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-25 (원문 미열람)
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-09-25 (원문 미열람)
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-09-25 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-25 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-09-25 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-09-25 (원문 미열람)
[^ref-311]: ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행), Ultra-low-latency services in 5G systems: A perspective from 3GPP standards, 2020, https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 42
related_areas: [18, 20, 23, 29, 32, 35, 47, 51]
tags: [VDA 5050, MQTT, Zenoh, 엣지 컴퓨팅, 포그 컴퓨팅, CAP 정리]
status: published
confidence: low
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-256, ref-300, ref-301, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-311]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 42. 분산 시스템·통신·컴퓨팅 구조

# 42. 분산 시스템·통신·컴퓨팅 구조

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

연결이 끊기면 자동화 자산이 멈추는 일이 창고 운영 중단의 한 원인으로 보고되지만, 그 근거는 아직 판매사 조사 수준이다. [추정][^ref-309] 하이브리드 WMS(창고 관리 시스템, Warehouse Management System) 판매사 Synergy Logistics의 조사 주장을 전한 FreightWaves 기사에 따르면, 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 한 번 이상 겪었고 절반 가까이는 소프트웨어·연결 중단으로 자동화 자산이 멈췄다. [추정][^ref-309] 중단 비용은 시간당 최대 10만 달러로 제시되었으나 하한은 미확인이고, 조사 방법·표본과 기사 발행일도 확인하지 못했다. [추정][^ref-309]

현장 무선망의 품질도 같은 문제다. CJ대한통운은 2023년 4월 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G를 구축했다고 발표하면서 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었고, 와이파이 대비 약 1,000배 빠른 속도를 주장했다. [추정] 벤더 주장[^ref-307] 발표 당시 로봇·설비·CCTV 적용은 무선 단말 시범 적용 뒤의 확대 계획이었다. [추정] 벤더 주장[^ref-307]

그래서 2절의 질문은 로봇 한 대의 성능이 아니라 통신과 계산을 어디에 두는가의 문제가 된다. 다만 외부망 단절 중 운영 범위를 정한 물류센터의 공개 기준이나 사례는 이번 조사에서 찾지 못했고, 아래 5절의 답은 관제 표준과 엣지 플랫폼 문서에서 끌어낸 추론이다. [추정][^ref-031][^ref-300]

## 4. 핵심 개념과 용어

2절의 질문을 다루려면 계산 계층, 분산 시스템의 이론적 한계, 통신 품질을 가리키는 용어를 먼저 맞춰야 한다. 아래 용어는 이 페이지 전체에서 같은 뜻으로 쓴다.

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area11-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 운반 도중 현장과 클라우드를 잇는 외부망이 끊김

| 항목 | 내용 |
|---|---|
| 시작 조건 | 클라우드 WMS가 내린 피킹 주문으로 ROP가 운반 작업을 만들어 로봇에 배정했고, 운반 도중 외부망이 끊긴다. |
| 작업 대상 | 피킹한 상품을 담은 토트·박스 |
| 수행 자원 | 현장 서버의 관제·브로커가 배정과 로봇 통신을 맡고 로봇은 받은 경로를 주행한다. Open-RMF free_fleet는 로봇마다 Zenoh 브리지를 두고 라우터를 플릿 어댑터와 같은 네트워크에서 실행하는 구성을 공개한다. [사실][^ref-256] |
| 제약 | VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제하고 주문·상태 토픽에 재전송 없는 MQTT QoS 0을 쓴다. [사실][^ref-031] 공장 자동화 같은 초저지연 서비스는 종단 간 10ms 미만 지연을 요구한다고 정리된다(2020년 논문 기준). [사실][^ref-311] |
| 완료·인계 | 단절 중에는 클라우드 WMS의 새 주문 수신과 재고 확정이 멈추고, 재연결 뒤 현장 완료 기록을 WMS 기록과 맞춰야 할 것으로 보인다. [추정][^ref-310] |
| 예외·성과 | 로봇은 브로커와 끊겨도 이미 해제된 노드까지 주문을 수행한다. [사실][^ref-031] 재연결 뒤 관제는 다음 상태 메시지로 로봇 상태를 다시 세워야 할 것으로 보인다. [추정][^ref-031][^ref-306] |

다음은 설명을 위한 가상의 시나리오이다. 관제와 브로커를 현장 서버에 두었다면 외부망 단절 중에도 이미 받은 주문과 현장 내 배정은 이어 갈 수 있으나, 클라우드 WMS의 새 주문 수신과 재고 확정은 멈추고 CAP 제약에 따라 단절 중 현장 기록과 WMS 기록을 재연결 뒤 맞추는 절차가 필요할 것으로 보인다. [추정][^ref-031][^ref-300][^ref-301][^ref-310] 이 판단은 로봇·엣지 플랫폼 문서를 대응시킨 추론이며, 물류센터의 외부망 단절 운영 기준이나 공개 사례로 확인한 것은 아니다.

현장 무선망이 끊기는 경우는 사정이 다르다. VDA 5050 3.0.0에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 "fulfills the order up to the last released node" — 곧 해제된 베이스까지만 수행하고 해제되지 않은 호라이즌 구간은 주행하지 않는다. [사실][^ref-031] 주문·상태가 QoS 0이고 상태는 사건 발생 시와 적어도 30초마다(최대 간격 30초) 다시 보내므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 전달되리라 기대하기보다 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신하는 구조가 필요할 것으로 보인다. [추정][^ref-031][^ref-306] VDA 5050이 MQTT 5.0의 세션 만료 같은 장치를 어떻게 쓰는지는 미확인이다.

## 6. 대표 접근법과 기술

공개 자료가 다루는 접근법은 분산 발견과 라우터 연결, 손실을 전제한 메시지 설계, 엣지의 단절 중 운영, 클라우드·포그로의 계산 이전, 관제 서버 가용성과 다거점 구성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area11-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한 통신 방식을 정한다. [사실][^ref-031] KubeEdge는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다. [사실][^ref-300]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area11-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 학술 자료는 계산 계층 모델, 분산 시스템의 이론적 한계, 클라우드 로보틱스, 초저지연 무선 통신으로 나뉜다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 연구와 자료](../../topics/2026/2026-09-25-area11-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 명령·상태 메시지의 통신 품질 요구, 연결 상태 감시, 재연결 뒤 상태 재구성을 맡고, 무선망 구축과 로봇 탑재 주행·회피는 연계 대상으로 두는 것으로 보인다. [추정][^ref-031][^ref-307]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 외부망 단절 중 이미 받은 주문·현장 내 배정의 지속 범위 판단, 재연결 뒤 완료·재고 기록을 WMS와 맞추는 절차 [추정][^ref-310] | 클라우드 WMS의 새 주문 발행·재고 확정(연계 대상) |
| 로봇 자체 지능·제어 | 명령·상태 메시지의 통신 품질 요구, last will 등을 이용한 연결 상태 감시, 재연결 뒤 상태 재구성 [추정][^ref-031] | 로봇 탑재부의 실시간 주행·회피와 인식·계획 계산(클라우드·포그로 옮기는 연구 포함)은 연계 대상이다 [추정][^ref-304][^ref-308] |

무선망(와이파이·5G 특화망) 구축·운영은 분류 원문 19장 표에 명시된 항목은 아니지만, ROP가 소유하지 않는 통신 기반 연계 대상에 가까운 것으로 보인다. [추정][^ref-307] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에서 본다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 통신·계산 배치 결정은 관제 연동, 명령 신뢰성, 세계 상태, 업무 연속성과 직접 맞물린다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area11-s10.md)에 있다.

## 11. 열린 질문

이번 실행은 다음 질문을 새로 올린다(id 는 [열린 질문](../../open-questions.md) 목록에 등록될 때 부여된다).

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 외부망이 끊겨 클라우드 WMS와 단절된 동안 현장 ROP가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가?

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md) — 섹션 3~11 신규 작성(외부망 단절 운영 범위, VDA 5050 무선망 전제·QoS·베이스/호라이즌, ROS 2 DDS·Zenoh, 엣지 단절 운영, 계산 배치 선례, 피킹 시나리오), 페이지 상태 표식 추가, 조건부 승인 수정 16건 이행, 4·6·7·8·10절 주제 페이지 분리 상태 유지. 2차 수정: 7절 첫 문장을 VDA 5050·KubeEdge 두 사례에 한정한 [사실] 문장으로 교체 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area11-s6.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "6. 대표 접근법과 기술" 절(2,039자)을 옮겼다 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area11-s4.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "4. 핵심 개념과 용어" 절(1,171자)을 옮겼다 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 연구와 자료](../../topics/2026/2026-09-25-area11-s8.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "8. 대표 연구와 자료" 절(855자)을 옮겼다. 2차 수정: NIST 항목의 쓰임새 평가를 [의견]으로, Gilbert·Lynch 항목의 적용 구절을 [추정]으로 분리 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area11-s7.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "7. 관련 표준·프레임워크·오픈소스" 절(769자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장의 '대부분' 일반화를 VDA 5050·KubeEdge 두 사례에 한정한 [사실] 문장으로 교체 (실행 2026-09-25-27)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-256]: Open Robotics (open-rmf), free_fleet — README (A free fleet management system), 미확인, https://github.com/open-rmf/free_fleet, 접근일 2026-09-25
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25
[^ref-301]: Microsoft, Operate Azure IoT Edge devices offline, 2026-03-02, https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities, 접근일 2026-09-25
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-25 (원문 미열람)
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-09-25 (원문 미열람)
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-09-25 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-25 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-09-25 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-09-25 (원문 미열람)
[^ref-311]: ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행), Ultra-low-latency services in 5G systems: A perspective from 3GPP standards, 2020, https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-09-18/pages/topics/2026/2026-10-09-area42-s7.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 42
related_areas: [16, 18, 20, 23, 27, 28, 29, 32, 35, 41, 47, 51, 52]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-300]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#7
---

[홈](../../index.md) › [주제](../index.md) › 42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스

# 42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한 통신 방식을 정한다. [사실][^ref-031] KubeEdge는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다. [사실][^ref-300]
- 이 페이지는 [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한 통신 방식을 정한다. [사실][^ref-031] KubeEdge는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다. [사실][^ref-300]


### VDA 5050 3.0.0 의 끊김·통신 감축 대비 장치

아래는 2026-10-09 에 다시 읽은 VDA 5050 3.0.0 명세 원문(발행일 미확인)에서 끊김과 통신 감축에 대비한 장치만 골라 정리한 것이다. 모두 한 출처에 기댄 내용이다.

- **전송 규약과 QoS**: VDA 5050 3.0.0 은 MQTT 를 JSON 형식과 함께 쓰고 MQTT 3.1.1 을 호환을 위한 최소 버전으로 둔다. [사실][^ref-031] 통신 부담을 줄이려 order·instantActions·state·factsheet·zoneSet·responses·visualization 토픽에는 MQTT QoS 0(최선 노력)을, connection 토픽에는 QoS 1(최소 한 번)을 쓰게 한다. [사실][^ref-031] 프로토콜 보안은 브로커 설정에서 고려할 일로 두되 이 지침에서는 정하지 않는다. [사실][^ref-031] 보안 조치는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)에서 다룬다.
- **연결 토픽**: connection 토픽은 브로커–클라이언트 사이 하트비트로 끊김을 탐지해 브로커가 [유언 메시지](../../glossary/mqtt-last-will.md)로 CONNECTION_BROKEN 을 알리는 MQTT 프로토콜 수준의 연결 확인용이며, 모든 메시지를 retained 플래그로 보낸다. [사실][^ref-031] 명세는 관제가 이 토픽을 로봇의 건강 상태 확인에 쓰지 않도록 정한다. [사실][^ref-031] 용어: [연결 상태](../../glossary/connection-state.md)
- **상태 보고 간격**: 상태 메시지는 주문 수신, 오류·운용 모드·노드 상태 변화 같은 정해진 사건이 생길 때와 적어도 30초마다 보낸다(5절과 같은 내용). [사실][^ref-031] 연속 상태 메시지 사이의 최소 간격은 로봇이 [팩트시트](../../glossary/vda-5050-factsheet.md)의 protocolLimits.timing.minimumStateInterval 로 알리고, 관련 사건은 하나의 상태 갱신으로 묶어 통신량을 줄이도록 권한다. [사실][^ref-031]
- **절전 모드**: startHibernation 즉시 동작을 받은 로봇은 브로커 연결은 유지하되 상태 메시지 발행을 멈추고, 연결 상태를 HIBERNATING 으로 알리며, 활성 주문을 지우고 움직이지 않는다. [사실][^ref-031] 배터리가 위급하거나 설정한 기상 시각(wakeUpTime)이 되면 로봇은 스스로 이 상태를 벗어날 수 있다. [사실][^ref-031] 이 영역에서는 통신 감축 장치로만 보고, 충전·에너지 관리는 [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md)로 잇는다.
- **해제 구역 허가 만료**: 해제 구역(RELEASE 구역)은 관제의 허가를 받아야 들어갈 수 있고, 로봇은 응답을 제때 받지 못하면 들어가지 않는다. [사실][^ref-031] 관제는 허가에 허가 만료 시각(leaseExpiry)을 붙일 수 있고, 이미 구역 안에서 허가가 만료·철회되면 로봇은 구역 정의의 releaseLossBehavior(STOP·CONTINUE·EVACUATE)에 따라 움직인다. [사실][^ref-031] 이 장치는 관제가 허가를 갱신하지 못하는 관제 장애나 통신 단절 때 공용 구역 점유를 시간으로 제한하는 데 쓸 수 있을 것으로 보이나, 명세는 이를 통신 단절 대책으로 명시하지 않는다(11절 열린 질문). [추정][^ref-031] 구역 교통 관리 자체는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)로 잇는다. 용어: [해제 구역](../../glossary/release-zone.md), [허가 만료 시각](../../glossary/lease-expiry.md)
- **클라우드 브로커의 토픽 구조**: 클라우드 사업자가 강제하는 토픽 구조가 있어 클라우드 기반 MQTT 브로커에서는 토픽 단계 구조를 개별 조정하게 허용하되, 제안 구조를 대략 따르도록 한다. [사실][^ref-031] 로컬 브로커에는 interfaceName/majorVersion/manufacturer/serialNumber/topic 구조를 제안하며 토픽 이름은 필수로 둔다. [사실][^ref-031] 브로커를 클라우드와 현장 서버 가운데 어디에 둘지는 [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md)와 함께 다룬다.
- **지도 사전 적재**: 지도는 관제가 즉시 동작(downloadMap)으로 지시하면 로봇이 지도 서버에서 끌어오는(pull) 방식으로 배포되고, 정지 시간을 줄이려 미리 적재해 두었다가 enableMap 으로 따로 활성화하며, 다운로드가 실패하면 FAILED(연결 끊김·지도 서버 접근 불가 등)로, 실패·중단 뒤 관제 개입을 기다릴 때는 RETRIABLE 로 보고한다. [추정][^ref-031] 지도 관리 자체는 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md)로 잇는다. 용어: [지도 배포](../../glossary/map-distribution.md)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-18 | 42. 분산 시스템·통신·컴퓨팅 구조 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-18/pages/topics/2026/2026-10-09-area42-s11.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조 — 열린 질문"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 42
related_areas: [16, 18, 20, 23, 27, 28, 29, 32, 35, 41, 47, 51, 52]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-300]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#11
---

[홈](../../index.md) › [주제](../index.md) › 42. 분산 시스템·통신·컴퓨팅 구조 — 열린 질문

# 42. 분산 시스템·통신·컴퓨팅 구조 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 열린 질문 가운데 이번 갱신이 부분 근거를 더한 것과 새로 올린 것은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 열린 질문 가운데 이번 갱신이 부분 근거를 더한 것과 새로 올린 것은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-038** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 외부망이 끊겨 클라우드 WMS와 단절된 동안 현장 ROP가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가?
    - 부분 근거(실행 2026-10-09-18): VDA 5050 은 클라우드 브로커를 허용하지만 브로커와 끊긴 로봇은 해제된 노드까지만 진행하므로, 관제·브로커를 클라우드에 두면 외부망 단절이 곧 로봇–관제 단절이 되어 해제 구간 뒤에서 로봇이 멈추고, 현장 서버에 두면 엣지 자율 운영 구조처럼 현장 내 배정을 이어 갈 수 있어, 관제·브로커의 배치가 단절 중 운영 범위를 정하는 핵심 결정인 것으로 보인다. [추정][^ref-031][^ref-300] 공개 운영 기준이나 사례로 확인한 것은 아니므로 해결로 보지 않는다.
- **oq-039** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가?
    - 부분 근거(실행 2026-10-09-18): VDA 5050 3.0.0 은 메시지 간격 규정 외에 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간 수치를 정하지 않으므로, 이 표준만으로는 답이 되지 않는 것으로 보인다. [추정][^ref-031]
- **oq-040** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가?
- **oq-206** (상태: 열림) 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가?
    - 부분 근거(실행 2026-10-09-18): oq-038 의 부분 근거와 같은 추론, 곧 관제·브로커를 어디에 두는지가 단절 중 운영 범위를 정한다는 판단이 이 질문에도 걸린다. [추정][^ref-031][^ref-300] 해결로 보지 않는다.
- (상태: 열림 · 제기 2026-10-09 · 실행 2026-10-09-18) 해제 구역(RELEASE 구역)의 허가 만료 시각(leaseExpiry)과 허가 상실 시 동작(releaseLossBehavior)을 관제 장애·통신 단절 대책으로 쓸 때 만료 시간과 동작 값을 어떤 기준으로 정하는지 공개한 현장 사례나 지침이 있는가? (id 는 열린 질문 목록에 등록될 때 부여된다)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-18 | 42. 분산 시스템·통신·컴퓨팅 구조 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-18/pages/topics/2026/2026-10-09-area42-s3.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조 — 왜 중요한가"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 42
related_areas: [16, 18, 20, 23, 27, 28, 29, 32, 35, 41, 47, 51, 52]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: [ref-031, ref-300, ref-307, ref-309]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#3
---

[홈](../../index.md) › [주제](../index.md) › 42. 분산 시스템·통신·컴퓨팅 구조 — 왜 중요한가

# 42. 분산 시스템·통신·컴퓨팅 구조 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 연결이 끊기면 자동화 자산이 멈추는 일이 창고 운영 중단의 한 원인으로 보고되지만, 그 근거는 아직 판매사 조사 수준이다. [추정][^ref-309] 하이브리드 WMS(창고 관리 시스템, Warehouse Management System) 판매사 Synergy Logistics의 조사 주장을 전한 FreightWaves 기사에 따르면, 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 한 번 이상 겪었고 절반 가까이는 소프트웨어·연결 중단으로 자동화 자산이 멈췄다. [추정][^ref-309]
- 이 페이지는 [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

연결이 끊기면 자동화 자산이 멈추는 일이 창고 운영 중단의 한 원인으로 보고되지만, 그 근거는 아직 판매사 조사 수준이다. [추정][^ref-309] 하이브리드 WMS(창고 관리 시스템, Warehouse Management System) 판매사 Synergy Logistics의 조사 주장을 전한 FreightWaves 기사에 따르면, 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 한 번 이상 겪었고 절반 가까이는 소프트웨어·연결 중단으로 자동화 자산이 멈췄다. [추정][^ref-309] 중단 비용은 시간당 최대 10만 달러로 제시되었으나 하한은 미확인이고, 조사 방법·표본과 기사 발행일도 확인하지 못했다. [추정][^ref-309]

현장 무선망의 품질도 같은 문제다. CJ대한통운은 2023년 4월 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G를 구축했다고 발표하면서 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었고, 와이파이 대비 약 1,000배 빠른 속도를 주장했다. [추정] 벤더 주장[^ref-307] 발표 당시 로봇·설비·CCTV 적용은 무선 단말 시범 적용 뒤의 확대 계획이었다. [추정] 벤더 주장[^ref-307]

그래서 2절의 질문은 로봇 한 대의 성능이 아니라 통신과 계산을 어디에 두는가의 문제가 된다. 다만 외부망 단절 중 운영 범위를 정한 물류센터의 공개 기준이나 사례는 이번 조사에서 찾지 못했고, 아래 5절의 답은 관제 표준과 엣지 플랫폼 문서에서 끌어낸 추론이다. [추정][^ref-031][^ref-300]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-09-25 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-18 | 42. 분산 시스템·통신·컴퓨팅 구조 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-09-18/pages/topics/2026/2026-10-09-area42-s10.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조 — 다른 연구영역과의 연결"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 42
related_areas: [16, 18, 20, 23, 27, 28, 29, 32, 35, 41, 47, 51, 52]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-09
updated: 2026-10-09
sources: []
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md#10
---

[홈](../../index.md) › [주제](../index.md) › 42. 분산 시스템·통신·컴퓨팅 구조 — 다른 연구영역과의 연결

# 42. 분산 시스템·통신·컴퓨팅 구조 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 통신·계산 배치 결정은 관제 연동, 명령 신뢰성, 세계 상태, 업무 연속성과 직접 맞물린다. [의견]
- 이 페이지는 [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 통신·계산 배치 결정은 관제 연동, 명령 신뢰성, 세계 상태, 업무 연속성과 직접 맞물린다. [의견]


2026-10-09 갱신이 5·7·9·11절에서 새로 잇는 영역은 다음과 같다.

- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 지도 사전 적재·활성화는 이 영역에서 끊김 대비 장치로만 보고, 지도 관리 자체는 그쪽에서 다룬다. [의견]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사 관제에 실행을 맡길 때 통신 오류 처리의 몫을 나누는 일이 그쪽 연동 문제다. [의견]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 해제 구역 허가 만료를 단절 대책으로 쓰는 기준(11절 새 질문)이 구역 교통 관리와 맞닿는다. [의견]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 절전 모드의 배터리 측면은 충전·에너지 관리와 맞닿는다. [의견]
- [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) — 관제·브로커를 클라우드와 현장 서버 가운데 어디에 둘지가 단절 중 운영 범위를 정하는 결정이다. [의견]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — VDA 5050 이 범위 밖에 둔 브로커 보안·사이버보안 조치를 다룬다. [의견]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-18 | 42. 분산 시스템·통신·컴퓨팅 구조 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 11건 / 전체 1324건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | https://github.com/open-rmf/free_fleet | 2026-09-25 | 예 |
| ref-300 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 미확인 | https://github.com/kubeedge/kubeedge | 2026-09-25 | 예 |
| ref-301 | Microsoft | Operate Azure IoT Edge devices offline | 2026-03-02 | https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities | 2026-09-25 | 예 |
| ref-304 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | https://arxiv.org/abs/2205.09778 | 2026-09-25 | 아니오 |
| ref-306 | OASIS | MQTT Version 5.0 | 2019-03 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html | 2026-09-25 | 아니오 |
| ref-307 | CJ대한통운 | CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 | 2023-04 | https://www.cjlogistics.com/ko/newsroom/news/NR_00001046 | 2026-09-25 | 아니오 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | https://arxiv.org/abs/2512.15215 | 2026-09-25 | 아니오 |
| ref-309 | FreightWaves | Warehouses face $100K-hour downtime risk as cloud outages mount | 미확인 | https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms | 2026-09-25 | 아니오 |
| ref-310 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 2002-06 | https://dl.acm.org/doi/10.1145/564585.564601 | 2026-09-25 | 아니오 |
| ref-311 | ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행) | Ultra-low-latency services in 5G systems: A perspective from 3GPP standards | 2020 | https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200 | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 381개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
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
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
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
- mqtt-quality-of-service-level: MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- oauth2-client-credentials-grant: 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))
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

### docs/open-questions.md (요약: 대상 영역 [42] 에 걸린 9건 / 전체 336건)

```markdown
- oq-035 [열림] 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기의 ISO 8601 시각, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? (영역 18, 20, 42)
- oq-038 [열림] 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? (영역 23, 32, 42)
- oq-039 [열림] 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가? (영역 20, 42)
- oq-040 [열림] 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가? (영역 35, 42)
- oq-083 [열림] 현장 서버·클라우드·로봇 사이 통신이 나빠질 때 물류센터의 작업 배정을 중앙 방식으로 유지할지 분산 방식으로 전환할지 정한 기준이나 실측 자료가 있는가? (영역 25, 42)
- oq-206 [열림] 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? (영역 41, 42)
- oq-310 [열림] 관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? (영역 48, 42, 29)
- oq-326 [열림] 병원·오피스처럼 5G 특화망으로 로봇을 연결하거나 클라우드에서 제어하는 현장에서 통신이 끊길 때 로봇의 현장 동작과 진행 중 작업의 재배정 기준을 공개한 사례가 있는가? (영역 42, 63, 67)
- oq-335 [열림] VDA 5050 headerId 결번이나 상태 메시지가 오지 않는 구간을 통신 원인으로 판정하는 기준(결번 수, 무응답 시간)을 정한 표준이나 현장 연구가 있는가? (영역 38, 42)
```
