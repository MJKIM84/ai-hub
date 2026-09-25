(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-69
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 28. 표준·상호운용성·다사업자 거버넌스 (G. 안전·보안·지능·거버넌스)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-25-69/target.json

```json
{
  "run_id": "2026-09-25-69",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 69,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 28,
    "area_name": "28. 표준·상호운용성·다사업자 거버넌스",
    "category": "G. 안전·보안·지능·거버넌스",
    "category_letter": "G"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=28"
}
```

### runs/2026-09-25-69/research.json

```json
{
  "run_id": "2026-09-25-69",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 28,
    "area_name": "28. 표준·상호운용성·다사업자 거버넌스",
    "category": "G. 안전·보안·지능·거버넌스"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음(적합성 시험·ECLASS·의미 식별자는 용어집에 있으나 의미적 버전 관리·서비스 수준 협약·감사 추적·산업데이터 없음)",
    "섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음(트랙 반영 제안 12건 대기)",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음(oq-004·005·020·025·026·027·041·044·055·065·085·089·091·096 이 이 영역에 걸려 있음)"
  ],
  "research_questions": [
    "제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]",
    "로봇–관제 공통 규격(VDA 5050, MassRobotics AMR 상호운용 표준, Open-RMF)은 누가 관리하고, 각 규격은 관제와 로봇 사이 책임을 어떻게 나누는가? (섹션 3·7·9 겨냥)",
    "공통 규격과 ROP API 의 변경 정책(판 번호 규칙, 하위 호환, 폐기 예고)은 어떻게 정해지는가? (섹션 4·6 겨냥, oq-091 관련)",
    "적합성 시험·인증은 어떤 형태로 운영되는가(OPC UA 인증, VDA 5050 인증 발표, 국내 단체표준 상호운용성 시험 절차)? (섹션 6·7 겨냥, oq-055 관련)",
    "여러 사업자가 함께 만든 로봇 운행 데이터의 소유권·접근권은 국내외 법제에서 어떻게 다뤄지는가? (섹션 3·9 겨냥)",
    "다사업자 운영에서 서비스 수준과 감사 이력은 어떤 표준 요구로 뒷받침되는가? (섹션 4·6·7 겨냥)",
    "한국의 로봇 상호운용·건물 연동 관련 국가표준·단체표준은 무엇이 있는가? (섹션 7 겨냥, oq-041·oq-026 관련)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 5050 은 VDA 와 VDMA 가 개발하고 카를스루에 공대(KIT) 물류연구소(IFL)가 위탁을 받아 개발을 주도하며 공식 GitHub 저장소를 관리하고, 명세는 사용이 선택적이고 구속력이 없다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-704"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 명세: VDA·VDMA 개발, KIT IFL 이 개발 주도·공식 GitHub 저장소 관리. 'The use of this specification is optional and non-binding'. 두 출처 모두 VDA 측 문서라 독립 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "VDA 5050 3.0.0 은 주문 배정·경로 계산·교착 탐지와 해소·교통 제어를 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송을 이동로봇 쪽 책임으로 나누고, 기능·운영·시스템 안전 요구와 교통 관리 로직은 다루지 않는다고 명시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "관제: 주문 배정, 경로 계산, 교착 탐지·해소, 교통 제어 / 로봇: 위치 추정, 경로 실행, 동작 실행, 상태 지속 전송. 안전 요구와 교통 관리 로직은 범위 밖으로 명시 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 공식 저장소 README 는 VDA 웹사이트의 공식 PDF 가 GitHub 내용보다 우선하며, 어느 판에 대해서도 지원·유지보수·문제 해결을 받을 법적 권리가 없다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-704"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: VDA 웹사이트 공식 PDF 가 GitHub 내용에 우선. 'no legal entitlement to support, maintenance, troubleshooting' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 5050 의 변경은 GitHub 이슈로 제안되고 월례 회의에서 논의되는 이슈에 진행 표시를, 수용된 변경에 반영 예정 판의 마일스톤을 붙이는 방식으로 관리되며, 3.0.1 은 오타·수정, 3.1.0 은 하위 호환 변경용이고 호환을 깨는 4.0.0 은 현재 계획되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-704"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 이슈에 'VD(M)A in progress' 표시(월례 회의), 수용 변경에 마일스톤. V3.0.1 오타·수정, V3.1.0 비파괴·하위 호환, V4.0.0 파괴적 변경·현재 미계획 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 은 의미적 버전 관리를 따라 필수 필드 추가 같은 파괴적 변경은 주 버전, 선택 매개변수 추가 같은 기능 추가는 부 버전, 오타 수정은 수 버전으로 올리고, 메시지 헤더의 version 필드에 [Major].[Minor].[Patch] 형식의 프로토콜 판을 싣는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세: Major = 새 필수 필드 등 파괴적 변경, Minor = 선택 매개변수 추가, Patch = 오타 수정. state.schema 헤더 version 설명 'Version of the protocol [Major].[Minor].[Patch]' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "의미적 버전 관리(Semantic Versioning) 2.0.0 은 공개 API 선언을 요구하고, 호환되지 않는 API 변경은 MAJOR, 하위 호환 기능 추가는 MINOR, 하위 호환 버그 수정은 PATCH 를 올리며, 기능을 폐기할 때는 먼저 폐기 표시를 담은 부 버전을 낸 뒤 주 버전에서 제거하도록 권한다.",
      "tag": "사실",
      "source_ids": [
        "ref-706"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'Software using Semantic Versioning MUST declare a public API.' 폐기 시 폐기 표시를 담은 새 부 버전 발행 후 주 버전에서 제거. 0.y.z 는 초기 개발 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "IETF RFC 9745 는 자원이 폐기되었거나 폐기될 것임을 알리는 Deprecation HTTP 응답 헤더를 정하고, RFC 8594 의 Sunset 헤더와 함께 쓰일 때 Sunset 시각은 Deprecation 시각보다 이르면 안 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-713"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: Deprecation 헤더는 URI 로 식별되는 자원의 폐기(예정)를 알리며 자원의 의미·기능 변화를 뜻하지 않는다. Sunset 시각은 Deprecation 시각보다 이를 수 없다 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "ROP 의 API 변경 정책은 상위 업무 시스템에 여는 API 에는 의미적 버전 관리와 폐기 예고·종료 시각 공지를 적용하고, 로봇 쪽에는 VDA 5050 헤더 version 처럼 로봇별 프로토콜 판을 기록해 판 차이를 관리하는 두 갈래로 설계할 수 있어 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-706",
        "ref-713",
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5·f6·f7 종합. 물류 로봇 관제에 이 정책을 적용한 공개 사례는 확인하지 못함",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f9",
      "claim": "MassRobotics AMR 상호운용 표준의 JSON 스키마는 신원 보고(identityReport)와 상태 보고(statusReport) 두 보고 메시지만 정의하고 명령·작업 배정 메시지는 두지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-253"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "스키마: identityReport 필수 uuid·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope / statusReport 필수 uuid·timestamp·operationalState·location. 명령 메시지 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "MassRobotics AMR 상호운용 표준은 여러 제조사의 AMR 이 같은 현장에서 공존하도록 로봇의 위치·속도·방향·상태(health)·작업 가용성 정보를 공유하게 하는 것을 목적으로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-253"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 'location, speed, direction, health, tasking / availability and other performance characteristics' 공유로 다수 제조사 AMR 의 공존 지원 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Open-RMF 는 플릿마다 플릿 어댑터가 제조사 고유 API 를 RMF 교통 일정·협상 인터페이스에 잇게 하고, 연동 수준을 전체 제어(Full Control)·신호등(Traffic Light)·읽기 전용(Read Only)·인터페이스 없음(No Interface)으로 나눠 제조사 관제를 표준화 없이 그 수준에 맞춰 통합한다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'Each robot fleet ... is expected to have a fleet adapter that connects its fleet-specific API to the interfaces of the core RMF traffic scheduling and negotiation system' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f12",
      "claim": "Open-RMF 는 2024-04-15 운영을 시작한 오픈소스 로보틱스 연합(OSRA) 체계에서 프로젝트 관리 위원회(PMC)가 일상 운영을 맡고, 기술 거버넌스 위원회(TGC)가 PMC 활동을 감독하며, 거버넌스 문서 개정은 해당 기구의 승인과 이사회 비준을 거친다.",
      "tag": "사실",
      "source_ids": [
        "ref-711",
        "ref-710"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "헌장(검색 요약): Open-RMF PMC 가 일상 운영 담당, TGC 가 PMC 감독. P&P 저장소 README: TGC 문서는 TGC 승인·OSRF 이사회 비준, PMC 는 저장소 목록·작업반 헌장 비준. 두 출처 모두 OSRA 측",
      "as_of": "2024-03",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f13",
      "claim": "OPC Foundation 은 규격 적합성을 확인하는 적합성 시험 도구(CTT)를 제공하고, 제조사가 자체 인증하거나 재단이 인정한 독립 시험소의 인증을 받게 하며, 통과 제품에 인증서와 인증 로고를 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-712"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'self-certification' 또는 독립 인증 시험소(Certification Test Lab) 인증 선택, OPC Foundation 인증서·'Certified' 로고 발급 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "이번에 읽은 VDA 5050 3.0.0 명세와 저장소 README 에는 공식 적합성 시험·인증 절차가 정의되어 있지 않아 보이며, 확인한 VDA 5050 인증 근거는 제조사–관제 업체 간 인증 발표와 제3자 오픈소스 시험 도구뿐이다(부재 확정 아님).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-704",
        "ref-608",
        "ref-407",
        "ref-408"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "명세·README 에 인증 절차 언급 없음(읽은 범위 기준). vda5050-sim·vda5050-lab 은 개인 프로젝트이며 VDA·VDMA 공식 시험 아님 (재인용: 2026-09-25-67)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f15",
      "claim": "OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 업체와 인증을 마쳤다고 발표했으나 인증의 시험 항목과 주체는 공개 자료로 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-608"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: OTTO 100·600·1200·1500 이 VDA 5050 관제 업체들과 'certified' 라고 발표(2026-04, 검색 요약)",
      "as_of": "2026-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f16",
      "claim": "한국지능형로봇표준포럼(KOROS)은 단체표준 KOROS 1148-8:2025 '서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차'를 제·개정 현황에 올렸다.",
      "tag": "사실",
      "source_ids": [
        "ref-718"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KOROS 제·개정 현황 게시물 제목 기준. 시험 항목·ISO 22166 계열과의 관계는 원문 미열람으로 미확인",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "EU 데이터법(Regulation (EU) 2023/2854, 2023-12-13 채택, 2024-01-11 발효)은 기업·이용자·공공 사이 데이터 접근·이용 규칙을 정하고, 제품 제조사와 데이터 보유자에게 데이터 공유·상호운용성 의무를, 데이터 처리 서비스 제공자에게 고객의 사업자 전환 허용 의무를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-707"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'Product manufacturers and holders of data are subject to extensive data sharing and data interoperability requirements', 처리 서비스 제공자는 전환(switching) 허용 의무",
      "as_of": "2023-12-13",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "한국 산업디지털전환촉진법은 상당한 투자와 노력으로 산업데이터를 새로 생성한 자에게 사용·수익 권리를 주고, 2인 이상이 공동으로 생성하거나 제3자에게 제공한 경우 당사자 약정이 없으면 각자 사용·수익 권리를 가진다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-708",
        "ref-709"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 2022-07 시행. 공동 생성 시 각자 사용·수익 권리, 약정이 있으면 약정에 따름. 제3자 제공 시 생성자와 제3자 모두 권리. 요약이 두 출처 중 어디서 왔는지 구분 불가",
      "as_of": "2022-01-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "로봇 상태·운행 기록처럼 제조사 로봇, ROP, 현장 운영사가 함께 만드는 데이터는 국내법상 공동 생성 데이터로 볼 여지가 있어, 약정이 없으면 각 사업자가 사용·수익 권리를 가지므로 연동 계약에서 데이터 범위·이용 목적·제3자 제공을 따로 정해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-708",
        "ref-707"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f17·f18 을 ROP 운영 데이터에 적용한 추정. 법률 해석·국내 계약 사례는 확인하지 못함",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자(integrator)가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-560"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'Industrial robot applications and robot cells', 2025-02 발행, 'reasonably foreseeable by the integrator' 위험을 다룸. 물류 이동로봇 플릿 적용 범위는 미확인",
      "as_of": "2025-02",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-004",
        "ref-560",
        "ref-704"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2(관제·로봇 책임 분리, 안전 범위 밖), f11(플릿 어댑터), f20(통합자 위험), f3(표준 기구는 지원 의무 없음) 종합 추정",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f22",
      "claim": "IEC 62443-3-3:2013 은 제어 시스템이 감사 대상 이벤트를 기록하고(SR 2.8), 감사 기록에 타임스탬프를 쓰며(SR 2.11), 감사 정보를 보호하도록(SR 3.9) 요구하고, SR 2.8 의 강화 요구로 중앙에서 관리하는 시스템 전체 감사 추적을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-715"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: SR 2.8 auditable events, SR 2.9 저장 용량, SR 2.10 감사 처리 실패 대응, SR 2.11 타임스탬프, SR 3.9 감사 정보 보호, RE 'centrally managed, system-wide audit trail'",
      "as_of": "2013-08",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "ISO/IEC 20000-1:2018 은 서비스 관리 시스템의 수립·실행·유지·지속 개선 요구사항을 정하는 표준으로, 서비스 수준 관리를 관계·합의 프로세스에 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-716"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'specifies requirements for establishing, implementing, maintaining and continually improving a service management system', 서비스 수준 관리 포함",
      "as_of": "2018",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "이종 플릿 환경의 서비스 수준은 ROP 가 고객과 맺는 가용성·응답 목표가 제조사 관제·설비업체의 목표에 기대므로, 서비스 관리 표준의 서비스 수준 관리와 감사 추적 요구를 결합해 사업자별 목표와 장애 귀책을 기록으로 확인하는 구조가 필요해 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-716",
        "ref-715"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f22·f23 종합 추정. 물류 로봇 다사업자 SLA 공개 사례·수치는 확인하지 못해 넣지 않음",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "산업통상자원부 국가기술표준원은 2021-11-11 행정안전부(승강기 안전기준 소관)와 협력해 로봇의 엘리베이터 탑승 시 안전 요구사항과 실내 배송 로봇 등에 관한 국가표준(KS)을 제정한다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-717"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료(검색 요약): 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준. KS 번호는 확인하지 못함",
      "as_of": "2021-11-11",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "출하 단계에서 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀌면, 관제가 헤더 version 으로 판 차이를 감지하고 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 변경 승인 전 판 호환 시험과 수정 책임을 계약으로 정해 두어야 출하 마감 전 작업 실패를 막을 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5 와 이전 실행의 UNSUPPORTED_PARAMETER(CRITICAL) 보고 규정을 결합한 시나리오 (재인용: 2026-09-25-67)",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과"
    },
    {
      "id": "f27",
      "claim": "입고 단계에서 새 제조사 로봇을 등록할 때 MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면, 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-253",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "identityReport 필수 manufacturerName·robotModel·robotSerialNumber, VDA 5050 헤더 manufacturer·serialNumber 를 근거로 한 적용 추정",
      "as_of": "2026-09-25",
      "flow_step": "입고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f28",
      "claim": "연계 대상: VDA 5050 이 범위 밖으로 둔 기능·시스템 안전과 로봇의 위치 추정·주행 실행은 제조사 쪽이며, 28. 표준·상호운용성·다사업자 거버넌스에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2 의 범위 제외 문구와 분류 원문 9장 '로봇 자체 지능·제어' 경계를 대조한 추정",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "VDA 5050 공식 저장소 main 브랜치 명세는 3.0.0 판이며 문서 머리에 발행일이 적혀 있지 않아, 3.0.0 발행일 충돌(oq-005)은 명세 원문으로 해소되지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "raw 명세: 'Version 3.0.0', 머리에 발행일 없음, 저작권자 VDA (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "28. 표준·상호운용성·다사업자 거버넌스는 규격 판·책임 분리로 9. 로봇·제조사 관제 연동, 적합성 시험으로 23. 시험·형식 검증·벤치마크, 판 이행으로 24. 자산·소프트웨어 수명주기 관리, 감사 추적으로 26. 사이버보안·접근권한·개인정보, 통합자 위험성평가로 25. 안전·위험 관리, 승강기 연동 표준으로 10. 설비·건물 시스템 연동과 맞물리는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-004",
        "ref-712",
        "ref-715",
        "ref-560",
        "ref-717"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f11·f13·f22·f20·f25 를 세부영역에 대응시킨 종합",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
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
      "accessed": "2026-09-25",
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
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 관제·로봇 책임 분리, 범위 제외, 의미적 버전 규칙.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. 헤더 version·manufacturer·serialNumber, 오류 수준 정의.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/state.schema",
      "source_unopened": false
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 개인 프로젝트의 VDA 5050 3.0.0 시뮬레이터·적합성 시험 묶음. 공식 시험 아님.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MQTT 기록에서 VDA 5050 주문·재연결·취소 불일치를 진단하는 개인 도구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OTTO AMR 이 여러 VDA 5050 관제 업체와 인증을 마쳤다는 벤더 발표.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-704",
      "org": "VDA / VDMA / KIT IFL (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — README",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 공식 저장소 README. 기여·이슈 처리 방식, 계획 판(3.0.1·3.1.0·4.0.0), 공식 PDF 우선과 지원 의무 부인 문구.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-253",
      "org": "MassRobotics",
      "title": "AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema)",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "MassRobotics 공식 저장소. 다수 제조사 AMR 공존 목적, identityReport·statusReport 두 보고 메시지 스키마.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/main/AMR_Interop_Standard.json",
      "source_unopened": true
    },
    {
      "id": "ref-706",
      "org": "Semantic Versioning (Tom Preston-Werner, semver.org)",
      "title": "Semantic Versioning 2.0.0",
      "published": null,
      "url": "https://semver.org/spec/v2.0.0.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "공개 API 선언과 MAJOR·MINOR·PATCH 증가 규칙, 폐기 절차를 정한 버전 관리 명세.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/semver/semver/master/semver.md",
      "source_unopened": false
    },
    {
      "id": "ref-707",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act)",
      "published": "2023-12-13",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 데이터법. 연결 제품 데이터 접근·공유, 제조사·데이터 보유자의 공유·상호운용성 의무, 처리 서비스 전환 의무.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-708",
      "org": "국가법령정보센터(산업통상자원부)",
      "title": "산업 디지털 전환 촉진법 (법률 제18692호)",
      "published": "2022-01-04",
      "url": "https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업데이터 생성자의 사용·수익 권리, 공동 생성·제3자 제공 시 권리 귀속 규정.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-709",
      "org": "소프트웨어정책연구소(SPRi)",
      "title": "산업 디지털 전환 촉진법의 의미와 시사점",
      "published": null,
      "url": "https://spri.kr/posts/view/23480?code=industry_trend",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 디지털 전환 촉진법의 내용과 시사점 분석.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-710",
      "org": "Open Source Robotics Alliance (Open Robotics)",
      "title": "osra-policies-and-procedures — README",
      "published": null,
      "url": "https://github.com/openrobotics/osra-policies-and-procedures",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "OSRA 정책·절차 문서 저장소. TGC 문서 승인·이사회 비준, PMC 의 저장소 목록·작업반 헌장 비준, 개정 제안 절차.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/openrobotics/osra-policies-and-procedures/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-711",
      "org": "Open Source Robotics Alliance",
      "title": "Charter of the Open Source Robotics Alliance Project 'Open-RMF'",
      "published": "2024-03",
      "url": "https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 프로젝트 헌장. 프로젝트 리더·PMC·작업반 구성과 PMC 의 일상 운영 책임.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-712",
      "org": "OPC Foundation",
      "title": "How to Certify - OPC Foundation",
      "published": null,
      "url": "https://opcfoundation.org/certification/how-to-certify/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OPC 제품의 자체 인증·독립 시험소 인증 절차와 적합성 시험 도구 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-713",
      "org": "IETF (RFC Editor)",
      "title": "RFC 9745: The Deprecation HTTP Response Header Field",
      "published": null,
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자원 폐기(예정)를 알리는 Deprecation HTTP 응답 헤더와 Sunset 헤더(RFC 8594)와의 관계.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-560",
      "org": "ISO",
      "title": "ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells",
      "published": "2025-02",
      "url": "https://www.iso.org/standard/73934.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 적용·로봇 셀의 안전 요구. 통합자가 예견 가능한 위험을 대상으로 함.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-715",
      "org": "IEC",
      "title": "IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample)",
      "published": "2013-08",
      "url": "https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 자동화·제어 시스템의 시스템 보안 요구. 감사 대상 이벤트·타임스탬프·감사 정보 보호 요구 포함.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-716",
      "org": "ISO/IEC",
      "title": "ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements",
      "published": "2018",
      "url": "https://www.iso.org/standard/70636.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 관리 시스템 요구사항 표준. 서비스 수준 관리 포함.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-717",
      "org": "대한민국 정책브리핑(산업통상자원부 국가기술표준원)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://korea.kr/news/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇 KS 제정 보도자료.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-718",
      "org": "한국지능형로봇표준포럼(KOROS)",
      "title": "KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "published": "2025",
      "url": "http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈 정보모델의 상호운용성 시험 절차 단체표준 제·개정 게시물.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
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
      "rationale": "seed 페이지 3~11절 첫 작성. 3절: f21(분류 원문 질문, 추정), f1·f3(표준 기구는 구속력·지원 의무 없음), f17·f18(데이터 권리 법제) / 4절: f6(의미적 버전 관리), f7(폐기 예고), f22(감사 추적), f23(서비스 수준 관리), f18(산업데이터) / 5절: f26(출하·예외·성과), f27(입고·수행 자원) / 6절: f4·f5·f6·f7·f8(변경 정책), f13·f14·f15(적합성 시험·인증, f15 벤더 주장 병기), f19·f24 / 7절: f1·f2·f4·f5·f29(VDA 5050, 트랙 반영 제안 2026-09-25-02 의 3.0.0 판 확인분), f9·f10(MassRobotics, 2026-09-25-02 f13 확인분), f11·f12(Open-RMF·OSRA), f13(OPC UA 인증), f16·f25(국내 단체표준·KS), f17·f18·f20·f22·f23 / 8절: f14 근거 도구 / 9절: f21·f24(직접), f28('연계 대상') / 10절: f30 / 11절: oq-005·055·091·096·041·026 유지와 open_questions_new 4건. 다음 실행 후보: 트랙 반영 제안 12건 중 IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·LIF·CAD 레이어·SHACL·IDS 관련(2026-09-25-11·16·19·28·35·36·41·44·47·53·54)은 출처 메타데이터가 입력에 없어 이번에 재확인하지 못했다."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "의미적 버전 관리",
      "term_en": "Semantic Versioning (SemVer)",
      "definition": "공개 API 를 선언하고 호환되지 않는 변경·하위 호환 기능 추가·하위 호환 수정을 각각 MAJOR·MINOR·PATCH 번호로 올려 변경의 호환성을 판 번호로 알리는 규칙이다."
    },
    {
      "term_ko": "서비스 수준 협약",
      "term_en": "Service Level Agreement (SLA)",
      "definition": "서비스 제공자와 고객이 가용성·응답 시간 같은 측정 가능한 서비스 목표와 미달 시 처리 방식을 합의해 문서로 정한 것이다."
    },
    {
      "term_ko": "감사 추적",
      "term_en": "Audit Trail",
      "definition": "누가 언제 무엇을 했는지를 시간 순서로 남긴 변경·접근·명령 기록으로, 사후에 책임과 원인을 확인하는 데 쓴다."
    },
    {
      "term_ko": "산업데이터",
      "term_en": "Industrial Data",
      "definition": "한국 산업디지털전환촉진법에서 산업 활동 과정에서 생성·활용되는 데이터로, 상당한 투자로 이를 생성한 자에게 사용·수익 권리가 인정된다."
    }
  ],
  "open_questions_new": [
    "ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f18 | 종류: 일반",
    "EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 9. 로봇·제조사 관제 연동 | 근거: f17 | 종류: 일반",
    "KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 23. 시험·형식 검증·벤치마크 | 근거: f16 | 종류: 일반",
    "이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 20. 예외 복구·재계획·업무 연속성 | 근거: f24 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 21,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음(단일 출처이거나 같은 기관 출처 쌍: f1 은 VDA 명세·README, f12 는 OSRA 헌장·정책 저장소, f5 는 VDA 명세·스키마)",
      "f18 검색 요약 문구가 ref-708·ref-709 중 어느 출처에서 왔는지 구분 불가",
      "f17 EU 데이터법의 적용 개시일(2025-09-12)은 법률사무소 검색 요약에만 있어 넣지 않음",
      "f25 로봇 엘리베이터 탑승 KS 의 번호·세부 메시지 미확인(oq-041 미해결)",
      "f16 KOROS 1148-8:2025 시험 항목과 ISO 22166 계열 관계 미확인",
      "f15 OTTO VDA 5050 인증의 시험 항목·주체 미확인(벤더 주장)",
      "ref-704·ref-253·ref-706·ref-709·ref-710·ref-712·ref-713 발행일 미확인",
      "oq-005 VDA 5050 3.0.0 발행일은 명세 원문에 날짜가 없어 해소 못 함(f29)",
      "oq-055 VDA 5050 공식 적합성 시험 부재는 읽은 명세·README 범위에서만 확인(f14), 해결 제안하지 않음"
    ],
    "scope_violations": [
      "f28: 기능·시스템 안전과 로봇 주행 실행은 분류 원문 9장 로봇 자체 지능·제어 경계라 '연계 대상:' 표시",
      "f25: 승강기 안전기준·제어는 시설·설비 제어 경계라 표준 존재만 기술하고 10. 설비·건물 시스템 연동과의 연결로 제안",
      "f20: ISO 10218-2 는 산업용 로봇 셀 표준이라 물류 이동로봇 적용은 미확인으로 명시",
      "f17·f18·f19: 법 해석은 ROP 직접 범위가 아니며 계약 조건으로 반영할 과제로만 제안"
    ],
    "budget_used": {
      "queries": 18,
      "sources": 15
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-051(state.schema), ref-004(rmf-core.md), ref-704(VDA5050 README), ref-253(MassRobotics README·JSON 스키마), ref-706(semver.md), ref-710(OSRA P&P README). 나머지 14건은 검색 요약 기준 원문 미열람(신뢰도 상한 medium). 원문을 연 출처가 있어도 공통 규칙 0절 6항에 따라 high 는 주지 않았다. 신규 출처 15건(ref-704~ref-718, 예약 구간 안)으로 신규 출처 상한에 도달해 실외이동로봇 운행안전인증(KIRIA)·국내 로봇 표준화 로드맵 논문은 넣지 못했다. 재사용 6건(ref-004·031·051·407·408·608)은 이전 브리프·역할 규칙 예시의 값을 썼다. 트랙 반영 제안 12건 가운데 VDA 5050 3.0.0 판(2026-09-25-02)과 MassRobotics(2026-09-25-02 f13)는 f29·f9·f10 으로 확인했고, 나머지(IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·VDMA LIF·CAD 레이어 표준·SHACL·IDS)는 해당 ref id 의 메타데이터가 입력에 없어 이번 실행에서 재확인하지 못하고 다음 실행 후보로 남겼다. 한국 자료: 산업디지털전환촉진법(ref-708), SPRi(ref-709), 국가기술표준원 보도자료(ref-717), KOROS 단체표준(ref-718). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 27. AI·학습·적응과 모델 운영 관련 주장 없음. 정정 요청 없음. 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-25-69/verification.json

```json
{
  "run_id": "2026-09-25-69",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-031) 0 Foreword 에 VDA·VDMA 공동 개발과 KIT IFL 의 개발 주도·이슈 검토·공식 GitHub 저장소 관리가 있고, 2 Scope 에 'optional and non-binding' 이 있다. ref-704 README 도 raw 로 열어 확인. 두 출처 모두 VDA 측 문서라 독립 교차 확인은 아니다. 발행일 미확인."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-031 5.3·5.4절(관제: 주문 배정, 경로 계산, 교착 탐지·해소, 교통 제어 / 로봇: 위치 추정, 경로·동작 실행, 상태 지속 전송)과 2 Scope 의 안전 요구·교통 관리 로직 제외 문구와 일치. 5.3절이 교착 해소를 관제 기능으로 두면서 2절이 그 알고리즘을 범위 밖으로 둔 점은 서술에서 구분해야 한다(수정 지시). 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw README 에서 'the PDF on the VDA website is valid' 와 'no legal entitlement to support, maintenance, troubleshooting' 문구 확인. 발행일 미확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw README 에 월례 VDA 5050 회의에서 논의하는 이슈의 'VD(M)A in progress' 표시, 수용 이슈의 마일스톤, V3.0.1 오타·수정 / V3.1.0 비파괴·하위 호환 / V4.0.0 현재 미계획이 있다. 단일 출처."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-031 1 Introduction 의 의미적 버전 규칙(Major 파괴적 변경·새 필수 필드, Minor 선택 매개변수, Patch 오타)과 raw state.schema 헤더 version 설명 'Version of the protocol [Major].[Minor].[Patch]' 확인. ref-031·ref-051 은 같은 기관 문서라 독립 아님."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw semver.md 에서 공개 API 선언 요구, MAJOR·MINOR·PATCH 정의, FAQ 의 폐기 절차(폐기 표시를 담은 부 버전 발행 후 주 버전에서 제거) 확인. 발행일 미확인."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(검증 환경 차단). 검색 결과에 RFC Editor 의 RFC 9745 페이지가 있고 'Sunset 시각은 Deprecation 시각보다 이르면 안 된다(MUST NOT be earlier)' 문구가 스니펫에 나타난다. 발행일 미확인."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: f5·f6·f7 종합 설계안이며 적용 사례 없음을 스스로 밝혔다. 근거 출처 가운데 ref-713 은 원문 미열람."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증 단계에서 raw AMR_Interop_Standard.json 을 열어 identityReport(필수 uuid·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope)와 statusReport(필수 uuid·timestamp·operationalState·location) 두 메시지만 있고 명령·작업 배정 메시지가 없음을 확인(statusReport 의 destinations 는 예상 위치). 브리프는 ref-253 를 fetched false 로 적었으므로 페이지 표시는 원문 미열람을 유지한다. 판·발행일은 README·스키마에 없어 미확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증 단계에서 raw README 를 열어 'location, speed, direction, health, tasking / availability and other performance' 공유 목적 문구 확인. 판(1.0 등)·발행일은 README 에 없어 미확인."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-004 의 Fleet Adapters 절과 네 제어 범주 표. 다만 원문은 인터페이스 없음(No Interface)을 'Not compatible'로 두고 RMF 환경에서 동작하지 않는다고 적으므로, '네 수준에 맞춰 통합한다'는 표현은 고쳐야 한다(수정 지시). '표준화 없이'는 원문의 '플릿 능력을 가정하지 않는다' 로 바꾼다. 발행일 미확인."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-711 헌장은 원문 미열람이며 검색 결과로 PMC 의 프로젝트 운영·TGC 의 PMC 감독은 확인된다. ref-710 README 는 raw 로 열어 확인했는데, TGC 문서는 TGC 승인·OSRF 이사회 비준, 저장소 목록·작업반 헌장은 해당 PMC 비준으로 나뉘어 있어 '해당 기구의 승인과 이사회 비준'은 과잉 일반화다. '2024-04-15 운영 시작'은 인용한 두 출처(ref-710·ref-711)에 없고 다른 검색 결과(Open Robotics 발표 등)에만 나타난다. 두 출처 모두 OSRA 측 문서라 독립 아님."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에 OPC Foundation 'How to Certify' 페이지가 있고, 스니펫들이 CTT 로 하는 자체 시험(self-testing)·독립 인증 시험소 인증·통과 제품 인증 로고를 확인한다. '인증서' 발급은 스니펫에 직접 나타나지 않으므로 서술은 '인증 로고' 중심으로 한다. 발행일 미확인."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 검증 단계에서 raw README 를 다시 열어 인증·적합성 시험 언급이 없음을 확인했다. ref-407·ref-408·ref-608 은 이전 실행(2026-09-25-67)에서 재사용한 출처이며, 이번 검증에서는 검증 예산을 모두 써서 다시 확인하지 못했다(원문 미열람). '부재 확정 아님' 단서 유지."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·벤더 주장·vendor_claim true 표시가 규칙에 맞다. ref-608 은 이전 실행에서 재사용한 벤더 보도자료이며, 이번 검증에서는 예산 소진으로 다시 확인하지 못했다(원문 미열람)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에 KOROS 제·개정 현황 게시물(같은 URL·제목)이 있고, 스니펫에 게시일 2025-06-04 가 나온다. 시험 항목은 미확인이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에 EUR-Lex 의 Regulation (EU) 2023/2854 가 있고, 2024-01-11 발효와 처리 서비스 전환 규정은 스니펫으로 확인했다. 대부분 조항의 적용 개시일(2025-09-12)과 연결 제품 설계 의무 대상(2026-09-12 이후 출시 제품)은 EUR-Lex 가 아닌 스니펫에만 나와 이번 finding 에서 뺐다. 발효와 적용 시점이 다르다는 점은 서술에 남긴다(수정 지시)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(국가법령정보센터 URL, 해설 기사)의 스니펫이 공동 생성 시 각자 사용·수익 권리, 약정 우선을 뒷받침한다. 최신성: 이 법은 2025-05-27 일부개정(법률 제20964호)된 판이 검색된다. ref-708 은 제18692호(2022-01-04 공포, 2022-07 시행) 판이므로 기준 판을 적고, 개정 뒤 조문이 같은지는 미확인으로 남긴다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 법 해석과 계약 사례가 확인되지 않았음을 밝혔다. 근거 출처는 모두 원문 미열람이다. 법 해석은 ROP 직접 범위가 아니므로 계약 과제로만 서술한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(ISO 페이지, ANSI 블로그 등)에서 산업용 로봇 적용·로봇 셀 범위와 '통합자가 합리적으로 예견할 수 있는' 위험을 다룬다는 문구를 확인했다. 물류 이동로봇 플릿에 적용되는지는 미확인이다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 공식 기준을 확인하지 못했음을 밝혔다. 참고로 ref-031 2 Scope 는 '운영자·통합자·차량 제조사·관제 제공자 사이 책임을 배분하지 않는다(Operational Responsibilities)'고 명시하는데, 브리프는 이 문구를 finding 으로 올리지 않았다. 다음 실행에서 보강할 후보다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(iTeh 샘플 URL과 같은 문서, 벤더 해설)에서 SR 2.8 감사 대상 이벤트와 RE 1 중앙 관리 시스템 전체 감사 추적, SR 2.11 타임스탬프, SR 3.9 감사 정보 보호를 확인했다. 기준판은 2013-08 이다(EN IEC 62443-3-3:2019 는 유럽 채택판)."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. ISO 페이지 스니펫에서 서비스 관리 시스템의 수립·실행·유지·지속 개선 요구가, 해설 스니펫에서 서비스 수준 관리가 관계·합의 요구에 들어 있음이 확인된다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: f22·f23 을 종합한 추정이며 공개 SLA 수치를 넣지 않았다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 정책브리핑 보도자료(같은 URL·제목)와 여러 기사 스니펫에서 2021-11-11 발표, 행정안전부와의 협력, 속도 제어·보호 정지·높낮이차와 틈새 극복·추락과 넘어짐 방지 요구를 확인했다. KS 번호는 미확인이다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. UNSUPPORTED_PARAMETER 가 CRITICAL 수준이고 오류 필드를 참조로 보고한다는 점은 ref-031 6.1.4.2·6.6.5.4 에서 확인했다. 헤더 version 으로 판 차이를 감지한다는 부분은 추론이다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 필수 필드는 raw MassRobotics 스키마 identityReport 와 ref-051 헤더 manufacturer·serialNumber 에서 확인했다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. '연계 대상:' 표시가 분류 원문 9장 로봇 자체 지능·제어 경계와 맞다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 머리에 'Version 3.0.0' 과 발행자 VDA 만 있고 발행일이 없다. oq-005 는 해소되지 않았다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 연결 대상 세부영역을 번호와 이름으로 적었다."
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
    "ok": true,
    "overlaps": [
      "f29 는 oq-005(VDA 5050 3.0.0 발행일 출처 충돌)와 겹친다. 해결로 보지 않고 oq-005 를 열린 채로 둔다",
      "f14 는 oq-055(VDA 5050 공식 적합성 시험 유무)와 겹친다. 해결 제안 없이 유지",
      "f4·f26 은 oq-091(2.x·3.0.0 판 혼재 운영)과 관련된다. 해결 아님",
      "f21 은 oq-096(통합자 위험성평가 수행 주체)과 관련된다. 해결 아님",
      "트랙 반영 제안 2026-09-25-02 의 'VDA 5050 3.0.0 발행 2026-03 [사실]'은 f29(원문에 발행일 없음)·oq-005 와 충돌한다. 발행일을 사실로 싣지 않는다"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f11 의 '연동 수준(전체 제어·신호등·읽기 전용·인터페이스 없음)'은 용어집 fleet-control-level '플릿 제어 수준'과 표기가 다르다"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f12: [사실] → [추정]으로 강등한다. '2024-04-15 운영 시작'은 인용 출처 ref-710·ref-711 에 없으므로 본문에서 뺀다. 개정 절차는 'TGC 문서는 TGC 승인·OSRF 이사회 비준, 저장소 목록·작업반 헌장은 해당 PMC 비준'으로 나눠 쓴다 — 원문(ref-710 README)이 두 경로를 구분하고 있어 현재 문장은 과잉 일반화다.",
    "f11: '네 수준에 맞춰 통합한다'를 '전체 제어·신호등·읽기 전용 세 수준으로 통합하고, 인터페이스 없음은 RMF 와 호환되지 않는다'로 고친다. '표준화 없이'는 '플릿 능력을 가정하지 않고'로 바꾼다. 수준 명칭은 용어집 '플릿 제어 수준'으로 표기한다 — ref-004 원문이 No Interface 를 'Not compatible'로 두고 있다.",
    "f2: 7절·9절에서 '관제가 교착 탐지·해소 기능을 맡되, 교통 조율 알고리즘 자체는 VDA 5050 범위 밖'으로 두 문장을 구분해 쓴다 — ref-031 은 5.3절과 2절에서 이 둘을 따로 다룬다.",
    "f17: 본문에 발효일(2024-01-11)만 [사실]로 쓰고 '주요 조항의 적용 개시일은 미확인'을 덧붙인다 — 적용 개시일은 EUR-Lex 가 아닌 검색 요약에서만 확인됐다.",
    "f18: 기준 판을 '법률 제18692호(2022-01-04 공포) 기준'으로 적고, '2025-05-27 일부개정 판에서 같은 조문인지는 미확인'을 덧붙인다 — 더 새로운 개정판이 검색된다.",
    "f16: 기준일을 '2025'에서 '2025-06-04(KOROS 게시일, 원문 미열람)'로 고친다.",
    "f13: '인증서'라는 표현을 빼고 '인증 로고'만 쓴다 — 스니펫에서 확인된 범위다.",
    "f15: 본문에 [추정]과 '벤더 주장'을 함께 적어 유지한다. 인증의 시험 항목과 주체가 미확인이라는 문구도 유지한다.",
    "f8·f14·f19·f21·f24·f26·f27·f28·f30: [추정] 태그를 유지하고 [사실]로 올리지 않는다. f21 은 9절에서 '공식 기준은 확인되지 않았다'는 단서를 그대로 둔다.",
    "모든 각주 정의: fetched false 인 출처(ref-407·ref-408·ref-608·ref-253·ref-707·ref-708·ref-709·ref-711·ref-712·ref-713·ref-560·ref-715·ref-716·ref-717·ref-718)는 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates[] 의 해당 항목에 source_unopened: true 를 넣는다 — web_fetch_available: false 환경이다.",
    "7절(트랙 반영 제안): 이번 실행에서 확인한 f1·f2·f4·f5·f29(VDA 5050)와 f9·f10(MassRobotics)만 반영한다. 2026-09-25-02 제안의 'VDA 5050 3.0.0 발행 2026-03'과 'MassRobotics 1.0' 판 표기는 싣지 않고 oq-005 로 남긴다. 나머지 10건(2026-09-25-11·16·19·28·35·36·41·44·47·53·54)은 이번 페이지에 반영하지 않는다 — 이번 실행에서 재확인하지 않았다.",
    "glossary_candidates '산업데이터': 정의를 '산업 활동 과정에서 생성·활용되는 데이터(산업디지털전환촉진법의 용어)'로 줄인다. 사용·수익 권리는 정의 문장에서 빼고 f18 본문에서 다룬다 — 용어 정의와 권리 규정은 조문이 다르다.",
    "glossary_candidates '서비스 수준 협약': 정의에서 '미달 시 처리 방식'을 뺀다 — 브리프의 어느 finding 도 이를 뒷받침하지 않는다.",
    "11절: oq-005·oq-055·oq-091·oq-096·oq-041·oq-026 은 해결로 바꾸지 않고 열린 질문으로 유지한다. open_questions_new 4건은 그대로 등록한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 1건, 교차 확인 0건. 강등: f12 사실 → 추정(인용 출처에 없는 날짜, 개정 절차의 과잉 일반화). 원문 미열람 출처: ref-407, ref-408, ref-608, ref-253(검증 단계에서 raw 스키마와 README 를 열어 f9·f10 을 확인했으나 브리프 표시는 미열람), ref-707, ref-708, ref-709, ref-711, ref-712, ref-713, ref-560, ref-715, ref-716, ref-717, ref-718. 브리프 표시 불일치: self_check.limits 는 ref-253 를 열었다고 적었지만 sources[] 에는 fetched false 로 되어 있다. 원문을 연 출처는 ref-004, ref-031, ref-051, ref-704, ref-706, ref-710 이다. 주의: 핵심 수치·사실은 모두 단일 기관 출처라 독립 교차 확인이 없다. 9절의 책임 분담(f21)과 데이터 권리 적용(f19)은 추정이다. VDA 5050 명세 자체가 운영 주체 간 책임을 배분하지 않는다고 적고 있다(ref-031 2 Scope). 이 문구는 다음 실행에서 finding 으로 보강할 후보다. 산업디지털전환촉진법은 2025-05-27 개정판이 있어 조문을 다시 확인해야 한다. 트랙 반영 제안 12건 가운데 VDA 5050·MassRobotics 관련만 반영하고 10건은 보류한다. 검증 검색 12회로 회당 상한 30회에 도달해 ref-608·ref-407·ref-408 은 다시 확인하지 못했다. 정정 요청 없음. 해결 인정한 열린 질문 없음.",
  "retry_reason": null
}
```

### runs/2026-09-25-69/pages.json

```json
{
  "run_id": "2026-09-25-69",
  "outline": [
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "로봇–관제 공통 규격은 연동 오류 수정·변경 승인 책임을 정하지 않는다. [의견] VDA 5050 은 구속력이 없고 지원 의무도 부인한다. [사실][^ref-031][^ref-704]",
      "planned_findings": [
        "f1",
        "f3",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 800,
      "summary": "의미적 버전 관리·폐기 예고·감사 추적·서비스 수준 관리·산업데이터가 이 영역의 기본 용어다. [사실][^ref-706][^ref-713][^ref-715][^ref-716][^ref-708]",
      "planned_findings": [
        "f6",
        "f7",
        "f22",
        "f23",
        "f18"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 700,
      "summary": "입고 단계의 새 제조사 로봇 등록과 출하 단계의 펌웨어 판 변경에서 식별자·판 호환 시험·수정 책임이 쓰인다. [추정][^ref-031][^ref-051][^ref-253]",
      "planned_findings": [
        "f2",
        "f26",
        "f27",
        "f21"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1000,
      "summary": "판 번호 규칙과 폐기 예고, 적합성 시험·인증, 연동 수준 분리, 서비스 수준·감사 이력 결합이 대표 접근이다. [사실][^ref-031][^ref-712][^ref-004]",
      "planned_findings": [
        "f4",
        "f5",
        "f7",
        "f8",
        "f11",
        "f13",
        "f14",
        "f15",
        "f19",
        "f24"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "VDA 5050·MassRobotics·Open-RMF·OPC UA 인증·SemVer·RFC 9745·IEC 62443-3-3·ISO/IEC 20000-1·ISO 10218-2·국내 단체표준과 KS 가 관련된다. [사실][^ref-031][^ref-253][^ref-004]",
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f5",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f16",
        "f20",
        "f22",
        "f23",
        "f25",
        "f29"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 500,
      "summary": "VDA 5050 저장소, MassRobotics 저장소, 제3자 시험 도구, OSRA 헌장, 국가기술표준원 보도자료, SPRi 해설이 주요 자료다. [사실][^ref-704][^ref-253]",
      "planned_findings": [
        "f14",
        "f12",
        "f25"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 750,
      "summary": "ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽이며, 로봇 위치 추정·주행과 안전은 연계 대상이다. [추정][^ref-031]",
      "planned_findings": [
        "f2",
        "f8",
        "f21",
        "f24",
        "f25",
        "f28",
        "f20"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 500,
      "summary": "9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 23·24·25·26 영역과 맞물린다. [추정][^ref-031]",
      "planned_findings": [
        "f30"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "VDA 5050 발행일·적합성 시험·판 혼재, 통합자 위험성평가, 국내 표준 부합화와 데이터 권리·SLA 연쇄가 열려 있다.",
      "planned_findings": [
        "f29",
        "f14",
        "f16",
        "f17",
        "f18",
        "f24"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area28-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,840자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area28-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 \"6. 대표 접근법과 기술\" 절(1,549자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area28-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 \"11. 열린 질문\" 절(1,233자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area28-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 \"4. 핵심 개념과 용어\" 절(1,053자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area28-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 \"3. 왜 중요한가\" 절(802자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 28. 표준·상호운용성·다사업자 거버넌스 | seed → draft: 3~11절 첫 작성(규격 구속력·데이터 권리, 판 번호·폐기 예고·적합성 시험, 입고·출하 시나리오, 책임 경계·연결·열린 질문), f12 추정 강등 반영, 2차 수정(9절 태그·단서, 5절 시작 조건 태그) | run 2026-09-25-69",
  "index_updates": {
    "home_recent": "2026-09-25 — 28. 표준·상호운용성·다사업자 거버넌스: 3~11절 첫 작성(VDA 5050 판 정책·책임 분리, 적합성 시험, 데이터 권리 법제, 감사·서비스 수준)",
    "category_recent": "2026-09-25 — 28. 표준·상호운용성·다사업자 거버넌스: seed → draft, 3~11절 첫 작성과 13절 각주",
    "area_recent": "2026-09-25 — 28. 표준·상호운용성·다사업자 거버넌스: 3~11절 첫 작성(실행 2026-09-25-69), 트랙 반영 제안 가운데 VDA 5050·MassRobotics 분만 7절에 반영"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "semantic-versioning",
      "term_ko": "의미적 버전 관리",
      "term_en": "Semantic Versioning (SemVer)",
      "definition": "공개 API 를 선언하고 호환되지 않는 변경·하위 호환 기능 추가·하위 호환 수정을 각각 MAJOR·MINOR·PATCH 번호로 올려 변경의 호환성을 판 번호로 알리는 규칙이다.",
      "description": "VDA 5050 3.0.0 도 이 규칙을 따라 메시지 헤더 version 에 프로토콜 판을 싣는다.",
      "related_areas": [
        28,
        24,
        9
      ],
      "sources": [
        "ref-706",
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "service-level-agreement",
      "term_ko": "서비스 수준 협약",
      "term_en": "Service Level Agreement (SLA)",
      "definition": "서비스 제공자와 고객이 가용성·응답 시간 같은 측정 가능한 서비스 목표를 합의해 문서로 정한 것이다.",
      "related_areas": [
        28,
        20
      ],
      "sources": [
        "ref-716"
      ]
    },
    {
      "action": "new",
      "slug": "audit-trail",
      "term_ko": "감사 추적",
      "term_en": "Audit Trail",
      "definition": "누가 언제 무엇을 했는지를 시간 순서로 남긴 변경·접근·명령 기록으로, 사후에 책임과 원인을 확인하는 데 쓴다.",
      "description": "IEC 62443-3-3:2013 은 감사 대상 이벤트 기록, 타임스탬프, 감사 정보 보호를 요구한다.",
      "related_areas": [
        28,
        26
      ],
      "sources": [
        "ref-715"
      ]
    },
    {
      "action": "new",
      "slug": "industrial-data",
      "term_ko": "산업데이터",
      "term_en": "Industrial Data",
      "definition": "산업 활동 과정에서 생성·활용되는 데이터(산업디지털전환촉진법의 용어).",
      "related_areas": [
        28
      ],
      "sources": [
        "ref-708"
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
      "accessed": "2026-09-25",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
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
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 관제·로봇 책임 분리, 범위 제외, 의미적 버전 규칙.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. 헤더 version·manufacturer·serialNumber, 오류 수준 정의.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 개인 프로젝트의 VDA 5050 3.0.0 시뮬레이터·적합성 시험 묶음. 공식 시험 아님.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MQTT 기록에서 VDA 5050 주문·재연결·취소 불일치를 진단하는 개인 도구.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OTTO AMR 이 여러 VDA 5050 관제 업체와 인증을 마쳤다는 벤더 발표.",
      "cited_by": [
        "docs/topics/2026/2026-09-25-area28-s6.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-704",
      "org": "VDA / VDMA / KIT IFL (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — README",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 공식 저장소 README. 기여·이슈 처리 방식, 계획 판(3.0.1·3.1.0·4.0.0), 공식 PDF 우선과 지원 의무 부인 문구.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-253",
      "org": "MassRobotics",
      "title": "AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema)",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MassRobotics 공식 저장소. 다수 제조사 AMR 공존 목적, identityReport·statusReport 두 보고 메시지 스키마.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-706",
      "org": "Semantic Versioning (Tom Preston-Werner, semver.org)",
      "title": "Semantic Versioning 2.0.0",
      "published": null,
      "url": "https://semver.org/spec/v2.0.0.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "공개 API 선언과 MAJOR·MINOR·PATCH 증가 규칙, 폐기 절차를 정한 버전 관리 명세.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-707",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act)",
      "published": "2023-12-13",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 데이터법. 연결 제품 데이터 접근·공유, 제조사·데이터 보유자의 공유·상호운용성 의무, 처리 서비스 전환 의무.",
      "cited_by": [
        "docs/topics/2026/2026-09-25-area28-s3.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-708",
      "org": "국가법령정보센터(산업통상자원부)",
      "title": "산업 디지털 전환 촉진법 (법률 제18692호)",
      "published": "2022-01-04",
      "url": "https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업데이터 생성자의 사용·수익 권리, 공동 생성·제3자 제공 시 권리 귀속 규정. 2025-05-27 일부개정 판과의 조문 동일 여부는 미확인.",
      "cited_by": [
        "docs/topics/2026/2026-09-25-area28-s3.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-709",
      "org": "소프트웨어정책연구소(SPRi)",
      "title": "산업 디지털 전환 촉진법의 의미와 시사점",
      "published": null,
      "url": "https://spri.kr/posts/view/23480?code=industry_trend",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 디지털 전환 촉진법의 내용과 시사점 분석.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-710",
      "org": "Open Source Robotics Alliance (Open Robotics)",
      "title": "osra-policies-and-procedures — README",
      "published": null,
      "url": "https://github.com/openrobotics/osra-policies-and-procedures",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "OSRA 정책·절차 문서 저장소. TGC 문서 승인·이사회 비준, PMC 의 저장소 목록·작업반 헌장 비준, 개정 제안 절차.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-711",
      "org": "Open Source Robotics Alliance",
      "title": "Charter of the Open Source Robotics Alliance Project 'Open-RMF'",
      "published": "2024-03",
      "url": "https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 프로젝트 헌장. 프로젝트 리더·PMC·작업반 구성과 PMC 의 일상 운영 책임.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-712",
      "org": "OPC Foundation",
      "title": "How to Certify - OPC Foundation",
      "published": null,
      "url": "https://opcfoundation.org/certification/how-to-certify/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OPC 제품의 자체 인증·독립 시험소 인증 절차와 적합성 시험 도구 안내.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-713",
      "org": "IETF (RFC Editor)",
      "title": "RFC 9745: The Deprecation HTTP Response Header Field",
      "published": null,
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자원 폐기(예정)를 알리는 Deprecation HTTP 응답 헤더와 Sunset 헤더(RFC 8594)와의 관계.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-560",
      "org": "ISO",
      "title": "ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells",
      "published": "2025-02",
      "url": "https://www.iso.org/standard/73934.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 적용·로봇 셀의 안전 요구. 통합자가 예견 가능한 위험을 대상으로 함.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-715",
      "org": "IEC",
      "title": "IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample)",
      "published": "2013-08",
      "url": "https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업 자동화·제어 시스템의 시스템 보안 요구. 감사 대상 이벤트·타임스탬프·감사 정보 보호 요구 포함.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-716",
      "org": "ISO/IEC",
      "title": "ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements",
      "published": "2018",
      "url": "https://www.iso.org/standard/70636.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 관리 시스템 요구사항 표준. 서비스 수준 관리 포함.",
      "cited_by": [
        "docs/topics/2026/2026-09-25-area28-s4.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-717",
      "org": "대한민국 정책브리핑(산업통상자원부 국가기술표준원)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://korea.kr/news/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇 KS 제정 보도자료.",
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-718",
      "org": "한국지능형로봇표준포럼(KOROS)",
      "title": "KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "published": "2025-06-04",
      "url": "http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈 정보모델의 상호운용성 시험 절차 단체표준 제·개정 게시물(게시일 2025-06-04).",
      "cited_by": [
        "docs/topics/2026/2026-09-25-area28-s7.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가?",
      "areas": [
        28
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가?",
      "areas": [
        28,
        9
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가?",
      "areas": [
        28,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가?",
      "areas": [
        28,
        20
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "입고",
      "item": "시작 조건",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "28. 표준·상호운용성·다사업자 거버넌스"
    },
    {
      "step": "입고",
      "item": "수행 자원",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "28. 표준·상호운용성·다사업자 거버넌스"
    },
    {
      "step": "출하",
      "item": "시작 조건",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "28. 표준·상호운용성·다사업자 거버넌스"
    },
    {
      "step": "출하",
      "item": "수행 자원",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "28. 표준·상호운용성·다사업자 거버넌스"
    },
    {
      "step": "출하",
      "item": "제약",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "28. 표준·상호운용성·다사업자 거버넌스"
    },
    {
      "step": "출하",
      "item": "예외·성과",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "28. 표준·상호운용성·다사업자 거버넌스"
    }
  ],
  "standards_updates": [
    {
      "name": "Semantic Versioning 2.0.0",
      "kind": "프레임워크",
      "org": "Semantic Versioning (semver.org)",
      "url": "https://semver.org/spec/v2.0.0.html",
      "related_areas": [
        28,
        24
      ],
      "summary": "공개 API 선언과 MAJOR·MINOR·PATCH 증가 규칙, 폐기 절차를 정한 버전 관리 명세.",
      "ref_id": "ref-706"
    },
    {
      "name": "IETF RFC 9745 The Deprecation HTTP Response Header Field",
      "kind": "표준",
      "org": "IETF",
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "related_areas": [
        28,
        1
      ],
      "summary": "자원의 폐기(예정)를 알리는 Deprecation 헤더. Sunset 헤더와 함께 쓰일 때 Sunset 시각은 Deprecation 시각보다 이르면 안 된다(원문 미열람).",
      "ref_id": "ref-713"
    },
    {
      "name": "IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준",
      "kind": "표준",
      "org": "IEC",
      "url": "https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf",
      "related_areas": [
        28,
        26
      ],
      "summary": "감사 대상 이벤트 기록·타임스탬프·감사 정보 보호와 중앙 관리 시스템 전체 감사 추적 강화 요구(원문 미열람).",
      "ref_id": "ref-715"
    },
    {
      "name": "ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항",
      "kind": "표준",
      "org": "ISO/IEC",
      "url": "https://www.iso.org/standard/70636.html",
      "related_areas": [
        28
      ],
      "summary": "서비스 관리 시스템의 수립·실행·유지·지속 개선 요구사항. 서비스 수준 관리를 관계·합의 프로세스에 포함(원문 미열람).",
      "ref_id": "ref-716"
    },
    {
      "name": "KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "kind": "표준",
      "org": "한국지능형로봇표준포럼(KOROS)",
      "url": "http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223",
      "related_areas": [
        28,
        23
      ],
      "summary": "서비스 로봇 소프트웨어 모듈 정보모델의 상호운용성 시험 절차 단체표준(게시일 2025-06-04, 시험 항목 미확인, 원문 미열람).",
      "ref_id": "ref-718"
    },
    {
      "name": "OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증)",
      "kind": "평가 프로그램",
      "org": "OPC Foundation",
      "url": "https://opcfoundation.org/certification/how-to-certify/",
      "related_areas": [
        28,
        23
      ],
      "summary": "자체 인증 또는 재단이 인정한 독립 시험소 인증을 거쳐 통과 제품에 인증 로고를 주는 프로그램(원문 미열람).",
      "ref_id": "ref-712"
    }
  ],
  "additional_research_requests": [
    "9절·3절: VDA 5050 3.0.0 2 Scope 의 '운영자·통합자·차량 제조사·관제 제공자 사이 책임을 배분하지 않는다(Operational Responsibilities)' 문구를 finding 으로 올려 책임 경계 서술을 [사실]로 보강할 필요가 있다(1차 검증 노트 제안).",
    "7절: 트랙 반영 제안 10건(2026-09-25-11·16·19·28·35·36·41·44·47·53·54 — IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·VDMA LIF·CAD 레이어·SHACL·IDS)은 이번 실행에서 재확인하지 못해 반영하지 않았다. 해당 출처 메타데이터를 입력에 넣고 재확인해야 한다.",
    "7절: 국가기술표준원이 발표한 로봇 엘리베이터 탑승 KS 의 번호가 표준 목록의 KS B 7317 과 같은지 확인이 필요하다(oq-041 관련).",
    "3절: EU 데이터법 주요 조항의 적용 개시일을 EUR-Lex 원문으로 확인해야 한다.",
    "3절: 산업디지털전환촉진법 2025-05-27 일부개정 판(법률 제20964호)에서 산업데이터 공동 생성 조문이 같은지 확인해야 한다.",
    "7절·9절: KOROS 1148-8:2025 의 시험 항목과 ISO 22166 계열과의 관계, ISO 10218-2:2025 의 물류 이동로봇 플릿 적용 여부 확인이 필요하다.",
    "6절: 물류 로봇 다사업자 SLA 의 공개 계약 구조·사례, 그리고 VDA 5050 공식 적합성 시험 유무(oq-055)를 추가 조사해야 한다."
  ],
  "fixes_applied": [
    "f12 강등 — 7절·8절에서 Open-RMF 거버넌스 문장을 [추정]으로 쓰고 '2024-04-15 운영 시작'을 빼고, 개정 경로를 'TGC 문서는 TGC 승인·OSRF 이사회 비준, 저장소 목록·작업반 헌장은 해당 PMC 비준'으로 나눠 썼다.",
    "f11 수정 — 6절에서 '플릿 능력을 가정하지 않고 전체 제어·신호등·읽기 전용 세 수준으로 통합하고, 인터페이스 없음은 RMF 와 호환되지 않는다'로 고치고 용어집 '플릿 제어 수준' 링크로 표기했다.",
    "f2 구분 — 7절과 9절에서 '관제가 교착 탐지·해소 기능을 맡는다'와 '교통 조율 알고리즘 자체와 안전 요구는 VDA 5050 범위 밖'을 별도 문장으로 썼다.",
    "f17 — 3절에 발효일 2024-01-11 만 [사실]로 쓰고 '주요 조항의 적용 개시일은 미확인이다'를 덧붙였다.",
    "f18 — 3절에 '법률 제18692호, 2022-01-04 공포 기준'을 적고 '2025-05-27 일부개정 판에서 같은 조문인지는 미확인'을 덧붙였다.",
    "f16 — 7절 문장의 기준일을 '2025-06-04, KOROS 게시일, 원문 미열람'으로 고치고 각주·참고문헌 발행일도 2025-06-04 로 맞췄다.",
    "f13 — 6절·7절에서 '인증서'를 빼고 '인증 로고'만 썼다.",
    "f15 — 6절에 '[추정] 벤더 주장' 표기와 시험 항목·주체 미확인 문구를 유지했다.",
    "f8·f14·f19·f21·f24·f26·f27·f28·f30 — 모두 [추정] 태그를 유지했고, 9절 f21 문장에 '이를 정한 공식 기준은 확인되지 않았다'를 그대로 두었다.",
    "각주 — fetched false 출처 15건(ref-407·408·608·253·707·708·709·711·712·713·560·715·716·717·718)의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "7절 트랙 반영 — VDA 5050(f1·f2·f4·f5·f29)과 MassRobotics(f9·f10)만 반영하고 'VDA 5050 3.0.0 발행 2026-03'과 'MassRobotics 1.0' 판 표기는 싣지 않았으며(발행일은 oq-005 로 유지), 나머지 10건은 반영하지 않았다.",
    "산업데이터 용어 — glossary_updates 정의를 '산업 활동 과정에서 생성·활용되는 데이터(산업디지털전환촉진법의 용어)'로 줄이고 권리 규정은 3절 본문에서 다뤘다.",
    "서비스 수준 협약 용어 — glossary_updates 정의에서 '미달 시 처리 방식'을 뺐다.",
    "11절 — oq-005·055·091·096·041·026 을 열림으로 유지하고 open_questions_new 4건을 새 질문으로 쓰고 open_question_updates 에 new 로 냈다.",
    "2차: 9절 표 '시설·설비 제어' 행 — 외부 연계 칸 '연계 대상: 승강기 안전기준·제어.'의 태그를 [사실]에서 [추정][^ref-717]로 고쳤다.",
    "2차: 9절 ISO 10218-2:2025 문장(f20) — 문장 뒤에 '물류 이동로봇 플릿에 적용되는지는 미확인이다.'를 덧붙였다.",
    "2차: 5절 표 '시작 조건' 칸 — (입고)·(출하) 두 문장에 '(설명용 가상 설정)'을 밝히고, 셀 끝(출하 문장 뒤)에 [추정][^ref-031][^ref-051]을 붙였다.",
    "2차: fixes_applied '각주' 항목 — 원문 미열람 출처 목록의 'ref-705'·'ref-714'를 'ref-253'·'ref-560'으로 고쳤다."
  ]
}
```

### runs/2026-09-25-69/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-69/pages/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [VDA 5050, 의미적 버전 관리, 적합성 시험, 감사 추적, 데이터 권리]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-407, ref-408, ref-608, ref-704, ref-253, ref-706, ref-707, ref-708, ref-709, ref-710, ref-711, ref-712, ref-713, ref-560, ref-715, ref-716, ref-717, ref-718]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 28. 표준·상호운용성·다사업자 거버넌스

# 28. 표준·상호운용성·다사업자 거버넌스

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [분류원문]

## 2. SCM 관점의 질문

제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]

## 3. 왜 중요한가

로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가](../../topics/2026/2026-09-25-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 입고 → 출하

**시나리오:** 새 제조사 로봇 등록(입고)과 펌웨어 갱신 뒤 출하 마감 작업 유지(출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | (입고) 입고 물량에 대응하려고 새 제조사 로봇을 현장 관제에 등록한다(설명용 가상 설정). (출하) 출하 마감 전에 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀐다(설명용 가상 설정). [추정][^ref-031][^ref-051] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | (출하) VDA 5050 3.0.0 에서 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송은 이동로봇 쪽 책임이다. [사실][^ref-031] (입고) MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. [추정][^ref-253][^ref-051] |
| 제약 | (출하) 변경 승인 전에 판 호환 시험과 수정 책임을 계약으로 정해 두어야 할 것으로 보인다. [추정][^ref-031][^ref-051] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | (출하) 관제가 헤더 version 으로 판 차이를 감지하고, 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 사전 시험이 없으면 출하 마감 전 작업 실패로 이어질 수 있을 것으로 보인다. [추정][^ref-031][^ref-051] |

다음은 설명을 위한 가상의 시나리오이다. 입고 물량이 늘어 새 제조사 로봇을 들이는 날, 등록 단계에서 어떤 식별자로 제조사를 구분할지 정해 두면 뒤에 생기는 연동 오류를 누구의 것인지 가릴 수 있다. [추정][^ref-253][^ref-051]

며칠 뒤 한 제조사가 펌웨어를 올려 프로토콜 판이 바뀌면, 출하 마감 직전에 관제가 보낸 주문의 일부 필드가 거부될 수 있다. 이때 규격 불일치를 누가 고치고 판 변경을 누가 승인하는지가 미리 정해져 있어야 복구가 빨라지지만, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-704]

## 6. 대표 접근법과 기술

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견]

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]

- VDA / VDMA / KIT IFL, VDA 5050 공식 저장소 README(발행일 미확인) — 변경 제안 절차, 계획 판, 지원 의무 부인 문구를 담아 규격 거버넌스를 읽는 기본 자료다. [사실][^ref-704]
- MassRobotics, AMR_Interop_Standard 저장소(발행일 미확인) — 신원·상태 보고 스키마만 두는 보고 중심 규격이다. [사실][^ref-253]
- gpue, vda5050-sim / ekusiadadus, vda5050-lab(발행일 미확인) — VDA 5050 시뮬레이션·적합성 시험 묶음과 MQTT 기록 진단 도구로, 개인 프로젝트이며 VDA·VDMA 공식 시험이 아닌 것으로 보인다. [추정][^ref-407][^ref-408]
- OSRA, Open-RMF 프로젝트 헌장(2024-03)과 정책·절차 저장소 — 오픈소스 관제 프레임워크의 운영·개정 권한 구조를 보여 준다. [추정][^ref-711][^ref-710]
- 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점(발행일 미확인) — 산업데이터 권리 규정을 해설한 국내 자료다. [사실][^ref-709]
- 국가기술표준원, 로봇 엘리베이터 탑승 KS 제정 보도자료(2021-11-11) — 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준을 다룬다. KS 번호는 미확인이다. [사실][^ref-717]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 인터페이스 판·적합성·책임 경계를 정하고 확인한다. [추정][^ref-031] | 연계 대상: 로봇의 위치 추정·주행 실행, 기능·시스템 안전(제조사 쪽). [추정][^ref-031] |
| 시설·설비 제어 | 승강기 연동 표준의 요구를 작업·경로 제약으로 반영한다. [의견] | 연계 대상: 승강기 안전기준·제어. [추정][^ref-717] |
| 상위 업무 시스템 | 상위 시스템에 여는 API 의 판 번호·폐기 예고 정책. [추정][^ref-706][^ref-713] | 연계 대상: 데이터 권리의 법률 해석과 계약 조건. [의견] |

VDA 5050 3.0.0 에서 교착 탐지·해소는 관제 쪽 기능이다. [사실][^ref-031] 그러나 교통 조율 알고리즘 자체와 기능·운영·시스템 안전 요구는 명세 범위 밖이다. [사실][^ref-031] 그래서 28. 표준·상호운용성·다사업자 거버넌스에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. [추정][^ref-031]

분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-704] ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. [사실][^ref-560] 물류 이동로봇 플릿에 적용되는지는 미확인이다. 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

28. 표준·상호운용성·다사업자 거버넌스는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-712][^ref-715][^ref-560][^ref-717]

- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 규격 판과 관제–로봇 책임 분리가 연동 구현의 전제다.
- [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) — 로봇 승강기 탑승 KS 같은 설비 연동 표준을 공유한다.
- [23. 시험·형식 검증·벤치마크](../f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — 적합성 시험·인증을 새 로봇 연동 승인에 쓰는 방법을 다룬다.
- [24. 자산·소프트웨어 수명주기 관리](../f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) — 펌웨어·프로토콜 판 이행과 폐기 예고가 수명주기 관리와 겹친다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) — 통합자의 시스템 수준 위험성평가를 누가 맡는지가 책임 경계의 핵심이다.
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) — 감사 추적 요구가 보안 표준에서 온다.

## 11. 열린 질문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-704]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-706]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-709]: 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점, 미확인, https://spri.kr/posts/view/23480?code=industry_trend, 접근일 2026-09-25 (원문 미열람)
[^ref-710]: Open Source Robotics Alliance (Open Robotics), osra-policies-and-procedures — README, 미확인, https://github.com/openrobotics/osra-policies-and-procedures, 접근일 2026-09-25
[^ref-711]: Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF', 2024-03, https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-712]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-09-25 (원문 미열람)
[^ref-713]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-715]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-717]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 28
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 28. 표준·상호운용성·다사업자 거버넌스

# 28. 표준·상호운용성·다사업자 거버넌스

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [분류원문]

## 2. SCM 관점의 질문

제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

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

### runs/2026-09-25-69/pages/topics/2026/2026-09-25-area28-s7.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-704, ref-253, ref-706, ref-710, ref-711, ref-712, ref-713, ref-560, ref-715, ref-716, ref-717, ref-718]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#7
---

[홈](../../index.md) › [주제](../index.md) › 28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스

# 28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [VDA 5050](../../glossary/vda-5050.md) (3.0.0) | 표준 | 관제–이동로봇 책임 분리, 의미적 버전 규칙과 판 계획. 발행일은 명세 머리에 없어 미확인 | [^ref-031][^ref-704][^ref-051] |
| MassRobotics AMR 상호운용 표준 | 표준 | 다수 제조사 AMR 공존을 위한 신원·상태 보고. 판·발행일 미확인(원문 미열람) | [^ref-253] |
| [Open-RMF](../../glossary/open-rmf.md) | 오픈소스 | 플릿 어댑터와 플릿 제어 수준으로 이종 관제 통합, OSRA 거버넌스 | [^ref-004][^ref-711][^ref-710] |
| OPC Foundation 인증 프로그램 | 평가 프로그램 | 적합성 시험 도구(CTT)와 자체·독립 시험소 인증 | [^ref-712] |
| Semantic Versioning 2.0.0 | 프레임워크 | API 변경의 호환성을 판 번호로 알리는 규칙 | [^ref-706] |
| IETF RFC 9745 | 표준 | API 자원 폐기 예고 헤더 | [^ref-713] |
| IEC 62443-3-3:2013 | 표준 | 감사 대상 이벤트·타임스탬프·감사 정보 보호 | [^ref-715] |
| ISO/IEC 20000-1:2018 | 표준 | 서비스 관리 시스템과 서비스 수준 관리 | [^ref-716] |
| ISO 10218-2:2025 | 표준 | 통합자가 예견할 수 있는 위험 대상. 물류 이동로봇 플릿 적용 범위는 미확인 | [^ref-560] |
| KOROS 1148-8:2025 | 표준 | 서비스 로봇 소프트웨어 모듈 정보모델의 상호운용성 시험 절차(단체표준). 시험 항목 미확인 | [^ref-718] |
| 로봇 엘리베이터 탑승 안전 요구사항 KS(번호 미확인) | 표준 | 로봇–승강기 연동의 안전 요구 | [^ref-717] |

VDA 5050 3.0.0 은 주문 배정·경로 계산·교착 탐지와 해소·교통 제어를 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송을 이동로봇 쪽 책임으로 나눈다. [사실][^ref-031] 곧 관제가 교착 탐지·해소 기능을 맡는다. [사실][^ref-031] 그러나 교통 조율 알고리즘(교통 관리 로직) 자체와 기능·운영·시스템 안전 요구는 VDA 5050 범위 밖이라고 명시한다. [사실][^ref-031] 공식 저장소 main 브랜치 명세는 3.0.0 판이며 문서 머리에 발행일이 적혀 있지 않아, 발행일 충돌은 명세 원문으로 해소되지 않는다(확인일 2026-09-25). [사실][^ref-031]

MassRobotics AMR 상호운용 표준은 여러 제조사의 AMR 이 같은 현장에서 공존하도록 로봇의 위치·속도·방향·상태(health)·작업 가용성 정보를 공유하게 하는 것을 목적으로 한다. [사실][^ref-253] JSON 스키마는 [신원 보고(identityReport)](../../glossary/identity-report.md)와 상태 보고(statusReport) 두 보고 메시지만 정의하고 명령·작업 배정 메시지는 두지 않는다(확인일 2026-09-25). [사실][^ref-253]

Open-RMF 는 오픈소스 로보틱스 연합(Open Source Robotics Alliance, OSRA) 체계에서 프로젝트 관리 위원회(PMC)가 일상 운영을 맡고 기술 거버넌스 위원회(TGC)가 PMC 활동을 감독하는 것으로 보인다. 문서 개정 경로는 TGC 문서는 TGC 승인·OSRF 이사회 비준, 저장소 목록·작업반 헌장은 해당 PMC 비준으로 나뉜다. [추정][^ref-711][^ref-710]

한국지능형로봇표준포럼(KOROS)은 단체표준 KOROS 1148-8:2025 ‘서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차’를 제·개정 현황에 올렸다(기준일 2025-06-04, KOROS 게시일, 원문 미열람). [사실][^ref-718] 산업통상자원부 국가기술표준원은 2021-11-11 행정안전부(승강기 안전기준 소관)와 협력해 로봇의 엘리베이터 탑승 시 안전 요구사항과 실내 배송 로봇 등에 관한 국가표준(KS)을 제정한다고 밝혔다. [사실][^ref-717]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-704]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-706]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-710]: Open Source Robotics Alliance (Open Robotics), osra-policies-and-procedures — README, 미확인, https://github.com/openrobotics/osra-policies-and-procedures, 접근일 2026-09-25
[^ref-711]: Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF', 2024-03, https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-712]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-09-25 (원문 미열람)
[^ref-713]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-715]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-716]: ISO/IEC, ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements, 2018, https://www.iso.org/standard/70636.html, 접근일 2026-09-25 (원문 미열람)
[^ref-717]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-718]: 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차, 2025-06-04, http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-69 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-69 | 28. 표준·상호운용성·다사업자 거버넌스 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-69/pages/topics/2026/2026-09-25-area28-s6.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-407, ref-408, ref-608, ref-704, ref-706, ref-707, ref-708, ref-712, ref-713, ref-715, ref-716]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#6
---

[홈](../../index.md) › [주제](../index.md) › 28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술

# 28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견]
- 이 페이지는 [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견]

### 판 번호와 변경 정책

VDA 5050 3.0.0 은 의미적 버전 관리를 따라 새 필수 필드 추가 같은 파괴적 변경은 주 버전, 선택 매개변수 추가 같은 기능 추가는 부 버전, 오타 수정은 수 버전으로 올리고, 메시지 헤더의 version 필드에 [Major].[Minor].[Patch] 형식의 프로토콜 판을 싣는다. [사실][^ref-031][^ref-051] 변경은 GitHub 이슈로 제안되고 월례 회의에서 논의되는 이슈에 진행 표시를, 수용된 변경에 반영 예정 판의 마일스톤을 붙여 관리하며, 3.0.1 은 오타·수정, 3.1.0 은 하위 호환 변경용이고 호환을 깨는 4.0.0 은 현재 계획되지 않았다(확인일 2026-09-25). [사실][^ref-704]

ROP 의 API 변경 정책은 상위 업무 시스템에 여는 API 에는 의미적 버전 관리와 폐기 예고·종료 시각 공지를 적용하고, 로봇 쪽에는 VDA 5050 헤더 version 처럼 로봇별 프로토콜 판을 기록해 판 차이를 관리하는 두 갈래로 설계할 수 있어 보인다. 물류 로봇 관제에 이 정책을 적용한 공개 사례는 확인하지 못했다. [추정][^ref-706][^ref-713][^ref-031][^ref-051]

### 적합성 시험과 인증

OPC Foundation 은 규격 적합성을 확인하는 적합성 시험 도구(CTT)를 제공하고, 제조사가 자체 인증하거나 재단이 인정한 독립 시험소의 인증을 받게 하며, 통과 제품에 인증 로고를 준다. [사실][^ref-712]

이번에 읽은 VDA 5050 3.0.0 명세와 저장소 README 에는 공식 적합성 시험·인증 절차가 정의되어 있지 않아 보이며, 확인한 VDA 5050 인증 근거는 제조사–관제 업체 간 인증 발표와 제3자 오픈소스 시험 도구뿐이다(부재 확정 아님). [추정][^ref-031][^ref-704][^ref-608][^ref-407][^ref-408] 예컨대 OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 업체와 인증을 마쳤다고 발표했으나(2026-04), 인증의 시험 항목과 주체는 공개 자료로 확인되지 않았다. [추정] 벤더 주장[^ref-608]

### 연동 수준을 나눠 이종 관제를 통합

Open-RMF 는 플릿마다 [플릿 어댑터](../../glossary/fleet-adapter.md)가 제조사 고유 API 를 RMF 교통 일정·협상 인터페이스에 잇게 하고, 플릿 능력을 가정하지 않고 [플릿 제어 수준](../../glossary/fleet-control-level.md)을 전체 제어(Full Control)·신호등(Traffic Light)·읽기 전용(Read Only) 세 수준으로 나눠 제조사 관제를 통합한다. 인터페이스 없음(No Interface)은 RMF 와 호환되지 않는다. [사실][^ref-004]

### 서비스 수준·감사 이력·데이터 약정

이종 플릿 환경의 서비스 수준은 ROP 가 고객과 맺는 가용성·응답 목표가 제조사 관제·설비업체의 목표에 기대므로, 서비스 관리 표준의 서비스 수준 관리와 감사 추적 요구를 결합해 사업자별 목표와 장애 귀책을 기록으로 확인하는 구조가 필요해 보인다. [추정][^ref-716][^ref-715]

로봇 상태·운행 기록처럼 제조사 로봇, ROP, 현장 운영사가 함께 만드는 데이터는 국내법상 공동 생성 데이터로 볼 여지가 있어, 약정이 없으면 각 사업자가 사용·수익 권리를 가지므로 연동 계약에서 데이터 범위·이용 목적·제3자 제공을 따로 정해야 할 것으로 보인다. 법률 해석과 국내 계약 사례는 확인하지 못했다. [추정][^ref-708][^ref-707]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-608]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-704]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-706]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-707]: European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act), 2023-12-13, https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng, 접근일 2026-09-25 (원문 미열람)
[^ref-708]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104), 접근일 2026-09-25 (원문 미열람)
[^ref-712]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-09-25 (원문 미열람)
[^ref-713]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-715]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-716]: ISO/IEC, ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements, 2018, https://www.iso.org/standard/70636.html, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-69 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-69 | 28. 표준·상호운용성·다사업자 거버넌스 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-69/pages/topics/2026/2026-09-25-area28-s11.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#11
---

[홈](../../index.md) › [주제](../index.md) › 28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문

# 28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-005** (상태: 열림 · 실행 2026-09-25-69 재확인) 출처 충돌: VDA 5050 3.0.0 의 정확한 발행일은 언제인가? 공식 저장소 명세 머리에는 발행일이 없어 원문으로 해소되지 않았다. [사실][^ref-031]
- **oq-055** (상태: 열림) VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가?
- **oq-091** (상태: 열림) VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가?
- **oq-096** (상태: 열림) 여러 제조사 로봇이 섞인 현장에서 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가?
- **oq-041** (상태: 열림) 대한승강기협회의 엘리베이터–로봇 상호 연동 가이드라인 단체표준은 어떤 메시지·상태를 정하며, Open-RMF 승강기 메시지와 어떻게 대응하는가?
- **oq-026** (상태: 열림) KS B 7321-2 가 ISO 22166-202 와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가?
- (새 질문, 제기 2026-09-25 · 실행 2026-09-25-69) ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가?
- (새 질문, 제기 2026-09-25 · 실행 2026-09-25-69) EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가?
- (새 질문, 제기 2026-09-25 · 실행 2026-09-25-69) KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가?
- (새 질문, 제기 2026-09-25 · 실행 2026-09-25-69) 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-69 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-69 | 28. 표준·상호운용성·다사업자 거버넌스 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-25-69/pages/topics/2026/2026-09-25-area28-s4.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-706, ref-708, ref-713, ref-715, ref-716]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#4
---

[홈](../../index.md) › [주제](../index.md) › 28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어

# 28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]
- 이 페이지는 [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]

- **의미적 버전 관리(Semantic Versioning, SemVer)** — 공개 API 선언을 요구하고, 호환되지 않는 API 변경은 MAJOR, 하위 호환 기능 추가는 MINOR, 하위 호환 버그 수정은 PATCH 를 올린다. 기능을 폐기할 때는 먼저 폐기 표시를 담은 부 버전을 낸 뒤 주 버전에서 제거하도록 권한다. [사실][^ref-706]
- **폐기 예고(Deprecation)와 종료 시각(Sunset)** — IETF RFC 9745 는 자원이 폐기되었거나 폐기될 것임을 알리는 Deprecation HTTP 응답 헤더를 정하고, RFC 8594 의 Sunset 헤더와 함께 쓰일 때 Sunset 시각은 Deprecation 시각보다 이르면 안 된다. [사실][^ref-713]
- **감사 추적(Audit Trail)** — 누가 언제 무엇을 했는지 남긴 기록이다. IEC 62443-3-3:2013 은 제어 시스템이 감사 대상 이벤트를 기록하고(SR 2.8), 감사 기록에 타임스탬프를 쓰며(SR 2.11), 감사 정보를 보호하도록(SR 3.9) 요구하고, SR 2.8 의 강화 요구로 중앙에서 관리하는 시스템 전체 감사 추적을 둔다. [사실][^ref-715]
- **서비스 수준 관리(Service Level Management)** — ISO/IEC 20000-1:2018 은 서비스 관리 시스템의 수립·실행·유지·지속 개선 요구사항을 정하는 표준이며, 서비스 수준 관리를 관계·합의 프로세스에 포함한다. [사실][^ref-716] 서비스 수준 협약(Service Level Agreement, SLA)은 그 합의를 문서로 정한 것이다.
- **산업데이터(Industrial Data)** — 산업 활동 과정에서 생성·활용되는 데이터를 가리키는 산업디지털전환촉진법의 용어다. [사실][^ref-708]
- **[적합성 시험(Conformance Test)](../../glossary/conformance-test.md)**, **[플릿 어댑터(Fleet Adapter)](../../glossary/fleet-adapter.md)**, **[플릿 제어 수준(Fleet Control Level)](../../glossary/fleet-control-level.md)** — 용어집 정의를 따른다. 이 영역에서의 쓰임은 6절에서 다룬다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-706]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-708]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104), 접근일 2026-09-25 (원문 미열람)
[^ref-713]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-715]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-716]: ISO/IEC, ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements, 2018, https://www.iso.org/standard/70636.html, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-69 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-69 | 28. 표준·상호운용성·다사업자 거버넌스 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-69/pages/topics/2026/2026-09-25-area28-s3.md

```markdown
---
title: "28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 28
related_areas: [9, 10, 23, 24, 25, 26]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-704, ref-707, ref-708, ref-709]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#3
---

[홈](../../index.md) › [주제](../index.md) › 28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가

# 28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]
- 이 페이지는 [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]

대표 규격인 VDA 5050 은 VDA 와 VDMA 가 개발하고 카를스루에 공대(KIT) 물류연구소(IFL)가 위탁을 받아 개발을 주도하며 공식 GitHub 저장소를 관리한다(확인일 2026-09-25). [사실][^ref-031][^ref-704] 명세는 사용이 선택적이고 구속력이 없다고 스스로 밝힌다. [사실][^ref-031] 공식 저장소 README 는 VDA 웹사이트의 공식 PDF 가 GitHub 내용보다 우선하며, 어느 판에 대해서도 지원·유지보수·문제 해결을 받을 법적 권리가 없다고 적는다. [사실][^ref-704] 규격을 만든 기구에 현장 연동 오류의 수정을 기대할 수 없으므로, 수정과 변경 승인은 현장 사업자 사이의 약속으로 정해야 한다. [의견]

데이터도 여러 사업자가 함께 만든다. EU 데이터법(Regulation (EU) 2023/2854)은 2023-12-13 채택되어 2024-01-11 발효됐으며, 제품 제조사와 데이터 보유자에게 데이터 공유·상호운용성 의무를, 데이터 처리 서비스 제공자에게 고객의 사업자 전환 허용 의무를 둔다. [사실][^ref-707] 주요 조항의 적용 개시일은 미확인이다.

한국 산업디지털전환촉진법은 상당한 투자와 노력으로 산업데이터를 새로 생성한 자에게 사용·수익 권리를 주고, 2인 이상이 공동으로 생성하거나 제3자에게 제공한 경우 당사자 약정이 없으면 각자 사용·수익 권리를 가진다고 정한다(법률 제18692호, 2022-01-04 공포 기준). [사실][^ref-708][^ref-709] 2025-05-27 일부개정 판에서 같은 조문인지는 미확인이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-704]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-707]: European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act), 2023-12-13, https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng, 접근일 2026-09-25 (원문 미열람)
[^ref-708]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104), 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점, 미확인, https://spri.kr/posts/view/23480?code=industry_trend, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-69 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-69 | 28. 표준·상호운용성·다사업자 거버넌스 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-25-69/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/what-is-rop.md
categories/a-business-supply-chain-design/01-order-and-business-system-integration.md
categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md
categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md
categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md
categories/a-business-supply-chain-design/index.md
categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md
categories/b-common-information-and-environment-model/06-map-space-and-location-model.md
categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md
categories/b-common-information-and-environment-model/index.md
categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md
categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
categories/c-connectivity-and-execution-foundation/index.md
categories/d-planning-and-optimization/13-task-allocation-mrta.md
categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md
categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md
categories/d-planning-and-optimization/index.md
categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md
categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md
categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md
categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md
categories/e-collaboration-and-field-operations/index.md
categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md
categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md
categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md
categories/f-deployment-verification-and-maintenance/index.md
categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md
categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md
categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md
categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md
categories/g-safety-security-intelligence-and-governance/index.md
changelog.md
corrections.md
flow-matrix.md
glossary/action-dependency-graph.md
glossary/age-of-information.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/b2mml.md
glossary/battery-swapping.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/compensating-transaction.md
glossary/condition-based-maintenance.md
glossary/conflict-based-search.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/crdt.md
glossary/cross-schedule-dependency.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/goal-condition.md
glossary/grai.md
glossary/hallucination.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/isa-95.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/milp.md
glossary/mobile-manipulator.md
glossary/model-checking.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/order-batching.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/plug-and-produce.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/signal-temporal-logic.md
glossary/situation-awareness-based-agent-transparency.md
glossary/skill.md
glossary/slot-filling.md
glossary/software-nameplate.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/virtual-commissioning.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
glossary/zone-set.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/nl-task-chatbot.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/index.md
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
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
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
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
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
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/index.md
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
tracks/nl-task-chatbot/experiments.md
tracks/nl-task-chatbot/index.md
tracks/nl-task-chatbot/log.md
tracks/nl-task-chatbot/question-backlog.md
tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
tracks/nl-task-chatbot/stage-2-data-and-standards.md
tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
tracks/nl-task-chatbot/task-model-draft.md
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 637건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 163개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
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
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- lane-closure: 차선 폐쇄 (Lane Closure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-registry: 모델 레지스트리 (Model Registry)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [28] 에 걸린 17건 / 전체 108건)

```markdown
- oq-004 [열림] IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? (영역 28, 5)
- oq-005 [열림] 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. (영역 9, 28)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 1, 9, 28)
- oq-025 [열림] 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? (영역 28, 6)
- oq-026 [열림] KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) (영역 28, 5)
- oq-027 [열림] ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? (영역 6, 28)
- oq-041 [열림] 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (영역 10, 28)
- oq-044 [열림] 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? (영역 6, 28)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 9, 23, 28)
- oq-065 [열림] 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? (영역 16, 28)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 22, 28)
- oq-089 [열림] 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? (영역 23, 28)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 24, 9, 28)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 25, 28)
- oq-101 [열림] 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? (영역 26, 28)
- oq-105 [열림] 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? (영역 27, 28)
- oq-108 [열림] 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? (영역 22, 28)
```

### _source/ROP_SCM_연구분야_분류.md

```markdown
# SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야

> 문서화: 2026-09-24  
> 범위: 7개 대분류·28개 세부 연구영역, ROP의 책임 경계, 기존 아이디어의 위치, SCM 기반 분석 방법  
> 이 문서는 앞선 대화의 분류 내용을 Markdown으로 정리한 자료다. 공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.

## 1. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다.

연구 범위는 다음과 같이 구분한다.

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1]

## 2. A — 업무·공급망 설계

**무슨 일을 왜, 얼마나 해야 하는가**를 연구한다. 로봇을 움직이기 전에 공급망의 요구를 실행 가능한 업무로 정의하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **1. 주문·업무 시스템 연계** | ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 | 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? |
| **2. 공정·워크플로 모델링** | 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 | ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? |
| **3. 처리능력·거점·설비 계획** | 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 | 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? |
| **4. 성과·경제성·프로세스 개선** | 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 | 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? |

핵심은 **로봇 개별 성능과 공급망 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 공정이 막히면 대기 재고만 늘어날 수 있다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2]

## 3. B — 공통 정보·환경 모델

**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **5. 로봇 능력·작업 온톨로지** | 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 | 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? |
| **6. 지도·공간·위치 모델** | BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 | 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? |
| **7. 화물·재고·자산 식별과 추적** | 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 | 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? |
| **8. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 | 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? |

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3]

6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다.

## 4. C — 연결·실행 기반

**계획한 작업을 실제 장비가 확실하게 수행하게 하는 방법**을 연구한다. 공통 모델을 실제 명령·통신·실행으로 연결하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **9. 로봇·제조사 관제 연동** | 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 | 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? |
| **10. 설비·건물 시스템 연동** | 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 | 컨베이어 준비와 로봇 도착을 어떻게 맞출까? |
| **11. 분산 시스템·통신·컴퓨팅 구조** | 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? |
| **12. 명령·작업 실행의 신뢰성** | 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 | 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? |

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4]

## 5. D — 계획·최적화

**누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가**를 연구한다. 논문에서 작업 배정이나 경로 계획으로 많이 등장하는 영역이다. 네 항목은 분리해서 연구할 수 있지만 실제 운영에서는 서로 영향을 준다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **13. 작업 배정 — MRTA** | 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? |
| **14. 작업 순서·스케줄링** | 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 | 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? |
| **15. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? |
| **16. 공용 자원·충전·에너지 최적화** | 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? |

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6]

## 6. E — 협업·현장 운영

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? |

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7]

## 7. F — 도입·검증·유지관리

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? |

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다.

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8]

## 8. G — 안전·보안·지능·거버넌스

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? |

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다.

## 9. ROP가 직접 소유할 범위와 외부 연계 경계

전체를 연구하되 **ROP가 직접 소유할 범위는 별도로 정해야 한다.** 그렇지 않으면 SCM 시스템부터 로봇의 모터 제어까지 모두 만드는 프로젝트가 된다.

| 경계 | ROP에서 다룰 내용 | 주로 연계할 외부 영역 |
|---|---|---|
| **상위 업무 시스템** | 주문·납기·재고 제약을 받아 실행하고 결과 반영 | 수요예측, 구매, 재무, 전사 재고정책 |
| **로봇 자체 지능·제어** | 가능한 기능과 실행 조건, 상태·실패·완료 확인 | 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어 |
| **시설·설비 제어** | 작업 요청·예약·인계·상태 확인 | 승강기·컨베이어·PLC·설비 안전 제어 |
| **거점 간 운송** | 입출고 시간과 인계, 현장 작업 동기화 | 배차·운송계획·운임·국제물류 |
| **업종별 조건** | 해당 조건을 작업·경로·권한 제약으로 반영 | 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항 |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.**

## 10. 논의한 아이디어의 연구영역 매핑

| 아이디어 | 중심 연구영역 | 함께 필요한 영역 |
|---|---|---|
| 매뉴얼 기반 로봇 온톨로지 | **5. 능력·작업 온톨로지** | 9. 어댑터, 21. 온보딩, 23. 검증, 24. 버전 관리 |
| 건축 도면 기반 이동 지도 | **6. 지도·공간 모델** | 15. 교통 관리, 21. 시운전, 22. 시뮬레이션 |
| 로봇과 건물 조건을 함께 판단 | **5+6+8. 능력·공간·현재 상태** | 13. 배정, 16. 자원, 25. 안전 |
| SCM 전체와 연결한 ROP | **1+2+4. 업무 연계·공정·성과** | C~G의 필요한 기능을 조합 |

## 11. SCM 관점의 연구 시작 방법

**기술 목록에 실제 물류 흐름을 교차해서 본다.**

첫 분석 대상으로 한 현장의 **입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품**을 잡고, 각 단계마다 다음 여섯 항목을 채운다.

1. **시작 조건:** 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가?
2. **작업 대상:** 어떤 화물·운반구를 다루는가?
3. **수행 자원:** 로봇·사람·설비 중 누가 어떤 부분을 맡는가?
4. **제약:** 납기·공간·적재량·설비·권한 제약은 무엇인가?
5. **완료·인계:** 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가?
6. **예외·성과:** 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?

예를 들어 **‘피킹한 박스를 포장대로 운반’**이라는 작업 하나에서도 로봇 배정, 경로, 포장대 수용능력, 화물 식별, 인계 확인, 고장 복구가 연결된다. 이 흐름을 먼저 정하면, 온톨로지와 지도 자동화가 **전체 공급망의 어느 비용과 병목을 줄이는 기술인지** 구체적으로 판단할 수 있다.

## 12. 참고 자료

아래는 앞선 답변에서 확인·인용한 공식 자료와 연구 논문이다. 분류표 전체를 단일 출처에서 가져온 것은 아니며, 세부 분류와 연구 질문은 이를 바탕으로 구성한 분석이다.

1. ASCM. [SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/). 공급망 프로세스 범위 참고.
2. ISA. [Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of), 2025. 기업 업무와 제조 운영·제어의 통합 경계 참고.
3. GS1. [EPCIS and CBV Linked Data Model](https://ref.gs1.org/epcis/). 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고.
4. Open Robotics. [RMF Core Overview — Programming Multiple Robots with ROS 2](https://osrf.github.io/ros2multirobotbook/rmf-core.html). 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
5. Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses](https://arxiv.org/abs/2005.07371), 2020. 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구.
6. Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks](https://arxiv.org/abs/1705.10868), 2017. 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구.
7. NIST. [Performance of Collaborative Robot Systems](https://www.nist.gov/programs-projects/performance-collaborative-robot-systems). 사람–로봇 및 이종 로봇 협업 성능 평가 참고.
8. NIST. [ARIAC Documentation](https://pages.nist.gov/ARIAC_docs/en/latest/). 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고.
9. ROS 2 Design. [ROS 2 DDS-Security Integration](https://design.ros2.org/articles/ros2_dds_security.html). 인증·암호화·접근통제 구조 참고.
10. ROS 2 Design. [ROS 2 Robotic Systems Threat Model](https://design.ros2.org/articles/ros2_threat_model.html). 로봇 시스템의 보안 위협과 대응 설계 참고.
```

### runs/2026-09-25-69/verification2.json

```json
{
  "run_id": "2026-09-25-69",
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
    "세부영역 페이지 9절 표 '시설·설비 제어' 행: 외부 연계 칸의 '연계 대상: 승강기 안전기준·제어. [사실][^ref-717]'을 [추정][^ref-717]으로 고친다. 이유: 이 문장은 분류 원문 9장에 비춘 경계 판단이고, ref-717(f25)은 KS 제정 발표만 뒷받침한다. 경계 판단 문장에 [사실]을 붙이면 태그를 올린 것이 된다.",
    "세부영역 페이지 9절 ISO 10218-2:2025 문장(f20) 끝에 '물류 이동로봇 플릿에 적용되는지는 미확인이다'를 덧붙인다. 이유: 1차 f20 메모와 브리프 self_check.scope_violations 가 이 단서를 요구했다. 주제 페이지 2026-09-25-area28-s7 표에는 단서가 있지만, 통합자 책임 근거로 쓰인 9절에서는 빠졌다.",
    "세부영역 페이지 5절 표 '시작 조건' 칸: (입고)·(출하) 두 문장에 태그가 없다. 셀 끝에 '(설명용 가상 설정)'을 밝히거나, 출하 문장에 [추정][^ref-031][^ref-051]을 붙인다. 이유: 출하 문장의 펌웨어 갱신·판 변경 전제는 f26([추정])에서 왔고, 태그 없는 주장으로 남으면 안 된다. 이 칸은 flow_matrix_updates 의 입고·출하 '시작 조건' 연결 대상이다.",
    "pages.json fixes_applied 의 '각주' 항목: 원문 미열람 출처 목록의 'ref-705'와 'ref-714'를 브리프·1차 지시에 있는 'ref-253'과 'ref-560'으로 고친다. 실제 각주와 reference_updates 는 ref-253·ref-560 에 맞게 반영됐으나, 보고 문구의 id 가 브리프에 없는 값이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 1건, 교차 확인 0건. 강등: f12 사실 → 추정(인용 출처에 없는 날짜, 개정 절차의 과잉 일반화). 원문 미열람 출처: ref-407, ref-408, ref-608, ref-253, ref-707, ref-708, ref-709, ref-711, ref-712, ref-713, ref-560, ref-715, ref-716, ref-717, ref-718. 주의: 핵심 사실은 모두 단일 기관 출처라 독립 교차 확인이 없다. 9절의 책임 분담(f21)과 데이터 권리 적용(f19)은 추정이다. 산업디지털전환촉진법은 2025-05-27 개정판이 있어 조문을 다시 확인해야 한다. 트랙 반영 제안 가운데 VDA 5050·MassRobotics 관련만 반영했다. / 2차 수정 후 재검증. 1차 수정 지시 14건은 모두 이행됐다(f12 강등, f11 세 수준 표기, f2 구분, f17 발효일, f18 기준 판, f16 기준일, f13 인증 로고, 원문 미열람 각주, 용어 정의 축약 등). 드리프트 1건(9절 승강기 연계 칸의 [사실] 태그)과 단서 누락 1건(9절 ISO 10218-2 적용 범위)이 있다. 5절 시작 조건 칸에 태그가 없고, fixes_applied 의 출처 id 두 개가 틀렸다. [분류원문] 보존, 섹션 순서 준수, 링크 유효. 자동 분리된 주제 페이지 5건은 원 절 내용을 그대로 옮겼다.",
  "retry_reason": null
}
```
