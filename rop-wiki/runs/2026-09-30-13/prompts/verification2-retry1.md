(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-13
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 37. 관제 화면·실행 기록 (J. 현장 운영·관제)
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
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-30-13/target.json

```json
{
  "run_id": "2026-09-30-13",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 122,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 37,
    "area_name": "37. 관제 화면·실행 기록",
    "category": "J. 현장 운영·관제",
    "category_letter": "J"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=37"
}
```

### runs/2026-09-30-13/research.json

```json
{
  "run_id": "2026-09-30-13",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 37,
    "area_name": "37. 관제 화면·실행 기록",
    "category": "J. 현장 운영·관제"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 작업 상태 모델, 로그 수준, 시간 색인 기록 형식, 상황 인식 기반 에이전트 투명성, 설명 가능한 경로 계획 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설 관제 화면·배송 이력 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 지도 위 상태 표시, 설명 가능한 표시, 실행 기록 저장·시간축 재생 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 시각화·웹 대시보드·작업 상태/로그 스키마, VDA 5050 시각화 토픽, MCAP, ISA-101 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]",
    "여러 제조사 로봇·설비·작업 상태를 지도 위에, 층을 나눠 보여 주는 공개 구현(오픈소스·표준)은 무엇을 어떤 형식으로 표시하는가? (섹션 6·7 겨냥)",
    "로봇이 무엇을 왜 하고 있는지 운영자가 알아보게 하는 설명 가능한 표시에 관한 연구(에이전트 투명성, 계획 설명)는 무엇을 보고하는가? (섹션 4·6·8 겨냥)",
    "실행 기록을 어떤 구조로 저장하고 시간축으로 재생·검색하는가, 그리고 플릿 실행 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식이 있는가? (oq-131, 섹션 6·7 겨냥)",
    "관제 화면 설계에 쓸 수 있는 표준·지침과 다중 로봇 관제 화면에 관한 사용자 연구는 무엇인가? (섹션 7·8 겨냥)",
    "병원·상업 시설·물류창고 같은 현장에서 로봇 관제 화면과 실행 이력을 운영에 쓴 사례는 무엇인가? (섹션 5 겨냥, 한국 사례 우선)",
    "관제 화면·실행 기록에서 ROP가 직접 맡을 것과 로봇 제조사·시설 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Open-RMF 의 rmf_visualization 은 승강기·문의 위치와 상태, 플릿 관리자가 보고한 로봇 현재 위치, 닫힌 차선(회색)·속도 제한 차선(좁은 폭)을 구분한 주행 그래프, 초록 선으로 그린 로봇 예측 일정 궤적, 층 평면도를 한 화면에 겹쳐 보여 주며, 일정 궤적은 시작 시점과 조회 기간을 매개변수로 정해 시간 구간별로 조회한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1165"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 패키지 8종(building_systems, fleet_states, floorplans, navgraphs, obstacles, schedule 등). 일정 시각화는 start_duration·query_duration 매개변수로 기간을 정해 궤적을 조회한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Open-RMF 의 rmf-web 은 사용자가 Open-RMF 배치 전체를 시각화하고 제어하는 웹 인터페이스 묶음으로 API 서버·API 클라이언트·대시보드 프레임워크로 이루어지며, 기본 설정의 API 서버는 비영속 내부 데이터베이스를 쓰므로 실행 기록을 남기려면 영속 저장소를 따로 설정해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-302"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"in the default scenario, the API server will use an internal non-persistent database\" — 영속 저장은 설정 파일을 마운트해 구성한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Open-RMF API 메시지의 작업 상태(task_state) 스키마는 작업 상태를 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 12개 값으로 표현하고, 처음 추정 소요 시간과 현재 추정 소요 시간, 배정 로봇, 완료·진행·대기 단계 목록, 일시정지(interruptions)·취소·강제 종료 요청 정보를 함께 담는다.",
      "tag": "사실",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_state.json: status enum 12개, original_estimate_millis·estimate_millis, assigned_to, phases·completed·active·pending, interruptions·cancellation·killed 필드. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f4",
      "claim": "Open-RMF API 메시지의 작업 로그(task_log) 스키마는 로그를 작업 수준·단계(phase) 수준·사건(event) 수준으로 계층화하고, 각 로그 항목(log_entry)은 단조 증가하는 순번(seq), 중요도 tier(uninitialized·info·warning·error), 밀리초 단위 유닉스 시각, 본문 텍스트를 필수로 가진다.",
      "tag": "사실",
      "source_ids": [
        "ref-1168",
        "ref-1169"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_log.json 제목 \"Task Event Log\", phases 아래 events 사전. log_entry.json: seq(단조 증가, 오버플로 시 순환), tier 4값, unix_millis_time, text 모두 필수. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 명세는 차량의 위치와 계획 경로를 시각화 시스템에 높은 빈도로 보내는 visualization 토픽을 주문 확인·오류·운용 상태를 담는 state 토픽과 분리해 두며, state 메시지는 사건이 생길 때 또는 최소 30초 간격으로 보내게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 저장소 main(3.0.0) 원문: visualization 토픽은 \"High frequency communication of position and planned path\" 용도이며 agvPosition·velocity 를 담는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "MCAP 은 임의 직렬화 형식의 타임스탬프 발행·구독 메시지를 기록하는 모듈형 컨테이너 형식으로, 스키마·채널·메시지·청크 레코드와 메시지 색인·청크 색인·요약 레코드를 두어 시각 기준 임의 접근(탐색)을 지원하고 첨부·메타데이터 레코드를 함께 담을 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1171"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 개요: \"a modular container file format for recording timestamped pub/sub messages with arbitrary serialization formats\". 압축·CRC 검증은 선택. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Foxglove 문서는 기록 재생 기능으로 시간축 막대 탐색, 재생 속도 조절, 재생 구간 자르기, 사건(event) 주석의 생성·검색, 반복 재생을 제공하고, 임의 시점으로 이동할 때 구독 토픽마다 가장 최근 메시지를 불러와(lookback) 모든 패널이 같은 시점 상태를 보이게 한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1172"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 메시지는 패널·스크립트에 항상 로그 시각 순서로 전달되며, 탐색 시 lookback 으로 토픽별 최근 메시지를 가져온다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f8",
      "claim": "Kottinger·Almagor·Lahijanian(ICAPS 2022)은 다중 에이전트 경로 계획을 사람이 눈으로 검증할 수 있도록 에이전트 궤적이 서로 겹치지 않는 시간 구간별 이미지 몇 장으로 설명하는 방식을 채택하고, 이 설명 가능한 MAPF 가 환경 크기에 대해 NP-난해임을 보인 뒤 CBS 에 설명 가능성 제약을 더한 XG-CBS 를 제안해 계획 시간과 설명 가능성의 절충을 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1173"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 설명은 \"a short sequence of images representing time segments, where in each time segment the trajectories of the agents are disjoint\" 형태. arXiv 2202.09930, 2022-02 제출.",
      "as_of": "2022-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Chen 외(Theoretical Issues in Ergonomics Science, 2018)는 지능형 에이전트와 함께 일하는 운영자의 임무 환경 상황 인식을 돕기 위한 상황 인식 기반 에이전트 투명성(SAT) 모델을 Autonomous Squad Member·IMPACT 두 시스템의 사람 참여 시뮬레이션 실험에 적용했고, 에이전트가 더 투명해질수록 운영자의 작업 수행이 일관되게 나아졌다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-477"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준: human-in-the-loop 실험(Autonomous Squad Member, IMPACT)에서 에이전트 투명성이 높을수록 운영자 작업 수행이 향상됐다. 19권 3호 259–282쪽.",
      "as_of": "2018",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "Roldán 외(Sensors, 2017-07)는 드론 2대·지상 로봇 1대의 화재 감시·진압 임무 8개를 운영자 24명이 감독하는 실험에서 기존·예측형 기존·가상현실·예측형 가상현실 인터페이스를 비교해, 가상현실 인터페이스가 상황 인식(SAGAT)을 높이고 작업 부하(NASA-TLX)를 낮췄으나 예측 요소의 효과는 유의하지 않았고 오히려 부하를 늘렸다고 보고했으며, 다중 로봇 인터페이스 요건으로 정보량 줄이기, 관련 정보로 주의 유도, 로봇 위치·건강·상태·측정값을 같은 화면에 통합하기, 지도 활용을 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1175"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PMC 본문: SAGAT VRI 16.25·PVRI 16.46 대 CI 14.91·PCI 14.33(VR 묶음 p=0.042), NASA-TLX VRI 638·PVRI 740·CI 853·PCI 915. 5.35×6.70×5.00 m 실험실 환경.",
      "as_of": "2017-07-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "ISA 는 공정 자동화 시스템의 인간–기계 인터페이스(HMI) 표준으로 ISA-101.01-2015 와 기술 보고서 TR101.01-2022(HMI 철학)·TR101.02-2019(HMI 사용성과 성능)를 두며, ISA-101.01 은 설계·구현·운영·지속 개선에 이르는 HMI 수명주기를 다루고 연속·배치·이산 산업 모두에 적용된다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1176"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISA 표준 소개 페이지: \"applicable across continuous, batch and discrete industries\". 표준 본문은 유료라 열람하지 않았다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "현대자동차그룹 로보틱스랩은 통합 관제 시스템 나콘(NARCHON)을 다수 이기종 로봇의 실시간 모니터링, BPMN 2.0 기반 워크플로·시나리오 관리, 이상 탐지·보고가 있는 실시간 대시보드, 승강기·자동문·보안 게이트 연동과 층간 이동을 지원하는 시스템으로 소개하며 적용처로 건물·상업 시설을 든다.",
      "tag": "추정",
      "source_ids": [
        "ref-1177"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"다양한 환경에서 다수의 로봇을 안정적이고 효율적으로 운영·관리할 수 있는 통합 관제 시스템을 개발하고 있습니다.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f13",
      "claim": "네이버클라우드의 ARC brain 사용 가이드는 서비스 기능으로 여러 제조사 로봇의 제어와 충돌 방지, 로봇 실시간 상태 모니터링과 알림, 실시간 태스크와 운영 이력 조회, 제3자 로봇 등록, 승강기·자동문 연동, 맵 에디터 기반 동선 설정, 로봇 상태 기반 알림 설정을 든다.",
      "tag": "추정",
      "source_ids": [
        "ref-1178"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 태스크 모니터링은 실시간 태스크 및 운영 이력 조회를 제공한다. 문서 최종 수정 2026-09-17.",
      "as_of": "2026-09-17",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "아주경제(2025-04-07) 보도에 따르면 현대차·기아는 한림대학교의료원과 업무협약을 맺고 병원 맞춤형 배송 로봇과 관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1179"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사: 한림대학교성심병원(경기 안양)에서 협약식. 안면 인식 기반 인증 기능과 특수물품 배송 이력 관리 시스템 구축 계획. 실제 운영 결과는 기사에 없음.",
      "as_of": "2025-04-07",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f15",
      "claim": "확인한 자료를 종합하면 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에 대해, '무엇'을 보여 주는 요소(지도 위 로봇·설비·예측 궤적 표시, 작업 상태 값과 단계, 수준별 로그)는 공개 구현과 표준에 갖춰져 있지만(f1·f3·f4·f5), '왜'를 보여 주는 설명 가능한 표시는 실험실·시뮬레이션 연구 수준이고(f8·f9·f10) 실제 다중 제조사 플릿 관제 화면에서 효과를 측정한 공개 자료는 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165",
        "ref-111",
        "ref-1168",
        "ref-031",
        "ref-1173",
        "ref-477",
        "ref-1175"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 현장 평가 부재는 이번 실행의 검색 범위(한·영 17회) 안에서의 판단이다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 여러 로봇을 감독하는 운영자는 정보량이 많을수록 상황 인식과 작업 부하가 나빠지고(f10), 에이전트의 판단이 투명할수록 운영자 수행이 나아지며(f9), 공정 산업 HMI 표준이 화면을 수명주기 전체에 걸쳐 관리할 대상으로 보고(f11), 병원처럼 배송 이력을 남겨야 하는 현장에서는 실행 기록이 인계 확인의 근거가 되기 때문이다(f14).",
      "tag": "추정",
      "source_ids": [
        "ref-1175",
        "ref-477",
        "ref-1176",
        "ref-1179"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "확인한 자료를 종합하면 37. 관제 화면·실행 기록에서 ROP가 직접 맡을 범위는 여러 제조사 플릿과 승강기·문 같은 설비 상태를 하나의 층별 지도에 겹쳐 보여 주는 통합 화면(f1·f12·f13), 제조사마다 다른 상태를 공통 작업 상태 값·단계·수준별 로그로 정규화한 실행 기록(f3·f4), 그 기록의 영속 저장과 시각 색인 기반 재생·사건 검색(f2·f6·f7), 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시(f8·f9)다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165",
        "ref-1177",
        "ref-1178",
        "ref-111",
        "ref-1168",
        "ref-302",
        "ref-1171",
        "ref-1172",
        "ref-1173",
        "ref-477"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. f12·f13·f7 은 벤더 주장이므로 범위 근거로만 쓴다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇 온보드 센서·주행 기록(로봇 쪽 bag·MCAP 기록)과 로컬 회피 시각화는 로봇 제조사에, 승강기·자동문·CCTV 같은 시설 설비의 자체 관제 화면은 시설·설비 쪽에 속하므로, ROP 는 VDA 5050 visualization·state 토픽처럼 제조사가 내보내는 상태와 설비 상태를 받아 통합 표시·기록하는 인터페이스를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1171",
        "ref-1165"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. VDA 5050 은 차량이 시각화 시스템으로 위치·경로를 보내는 토픽을 따로 두고(f5), rmf_visualization 은 플릿 관리자가 보고한 위치를 표시한다(f1).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "이 영역은 알림·이상 탐지의 38. 모니터링·이상 탐지·원인 분석(f4·f12·f13), 작업 시각 기록을 지표로 쓰는 39. 운영 성과 측정·개선(f3), 층별 지도의 15. 지도·공간·위치 모델(f1), 현재 상태를 담는 18. 실시간 세계 상태·데이터 일관성(f5), 기록 재생의 36. 가상 시운전·실제 상황 재현과 11. 채팅으로 실제 상황 시뮬레이션 재현(f6·f7, oq-131), 경로 설명의 27. 다중 로봇 경로·교통 관리 — MAPF(f8), 투명성의 13. 대화형 기능의 신뢰·기반·31. 사람–로봇 협업(f9·f10), 상태 메시지의 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f5), 문·승강기 표시의 22. 설비·건물 시스템 연동(f1), 기록 저장의 43. 데이터·관측성·배포(f2·f6), 배송 이력의 17. 작업 대상·자산 식별과 인계 추적(f14), 적용 현장인 63. 병원·의료(f14)·64. 상업 시설(f12)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165",
        "ref-302",
        "ref-111",
        "ref-1168",
        "ref-031",
        "ref-1171",
        "ref-1172",
        "ref-1173",
        "ref-477",
        "ref-1175",
        "ref-1177",
        "ref-1178",
        "ref-1179"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1165",
      "org": "Open Robotics (open-rmf/rmf_visualization)",
      "title": "rmf_visualization — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_visualization",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 시각화 패키지 8종이 승강기·문, 로봇 위치, 주행 그래프, 예측 일정 궤적, 평면도, 장애물을 RViz 로 표시하는 방식을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_visualization/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf/rmf-web)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 대시보드·API 서버·API 클라이언트 구성과 기본 비영속 데이터베이스 설정을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 작업 상태 JSON 스키마. 상태 값 12개, 추정 소요 시간, 단계 목록, 일시정지·취소·강제 종료 정보를 정의한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
      "source_unopened": false
    },
    {
      "id": "ref-1168",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — task_log.json (Task Event Log)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 작업 로그 JSON 스키마. 작업·단계·사건 수준으로 로그를 계층화한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_log.json",
      "source_unopened": false
    },
    {
      "id": "ref-1169",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — log_entry.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 로그 항목 JSON 스키마. 순번, 중요도 tier, 밀리초 시각, 본문을 필수 필드로 둔다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/log_entry.json",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA (VDA5050/VDA5050)",
      "title": "VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 저장소 main 브랜치(3.0.0) 명세 원문. visualization 토픽과 state 토픽의 역할·전송 조건을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1171",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타임스탬프 발행·구독 메시지를 담는 MCAP 컨테이너 형식의 레코드 종류와 시각 색인 기반 임의 접근 구조를 정의한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mcap.dev/spec",
      "source_unopened": false
    },
    {
      "id": "ref-1172",
      "org": "Foxglove",
      "title": "Playback — Foxglove Documentation",
      "published": null,
      "url": "https://docs.foxglove.dev/docs/visualization/playback",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇 기록 시각화 도구의 재생 기능(시간축 탐색, 속도, 구간, 사건 주석, 반복, lookback)을 설명하는 제품 문서.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://docs.foxglove.dev/docs/visualization/playback",
      "source_unopened": false
    },
    {
      "id": "ref-1173",
      "org": "Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022)",
      "title": "Conflict-Based Search for Explainable Multi-Agent Path Finding",
      "published": "2022-02",
      "url": "https://arxiv.org/abs/2202.09930",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "궤적이 겹치지 않는 시간 구간 이미지로 다중 에이전트 경로 계획을 설명하는 XG-CBS 를 제안한다(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2202.09930",
      "source_unopened": false
    },
    {
      "id": "ref-477",
      "org": "Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3))",
      "title": "Situation awareness-based agent transparency and human-autonomy teaming effectiveness",
      "published": "2018",
      "url": "https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. SAT 모델과 Autonomous Squad Member·IMPACT 실험에서 투명성이 운영자 수행을 높였다는 결과를 검색 결과 요약으로 확인했다(출판사 페이지 403).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1175",
      "org": "Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8))",
      "title": "Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction",
      "published": "2017-07-27",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "다중 로봇 임무 감독 인터페이스 4종을 운영자 24명으로 비교해 상황 인식·작업 부하를 측정하고 인터페이스 설계 요건을 제시한 동료심사 논문(PMC 본문 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "source_unopened": false
    },
    {
      "id": "ref-1176",
      "org": "ISA (International Society of Automation)",
      "title": "ISA-101 Series of Standards",
      "published": null,
      "url": "https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISA-101.01-2015 와 TR101.01-2022·TR101.02-2019 의 목록과 범위를 소개하는 발행 기관 페이지. 표준 본문은 유료라 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards",
      "source_unopened": false
    },
    {
      "id": "ref-1177",
      "org": "현대자동차그룹 로보틱스랩",
      "title": "PROJECTS — Robot Fleet Management (NARCHON)",
      "published": null,
      "url": "https://robotics.hyundai.com/projects/research/view.do?seq=102",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "이기종 로봇 통합 관제 시스템 나콘의 모니터링 대시보드·워크플로·설비 연동·층간 이동 기능을 소개하는 연구 과제 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://robotics.hyundai.com/projects/research/view.do?seq=102",
      "source_unopened": false
    },
    {
      "id": "ref-1178",
      "org": "네이버클라우드",
      "title": "ARC brain 개요 - 사용 가이드",
      "published": null,
      "url": "https://guide.ncloud-docs.com/docs/arc-brain-overview",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "멀티 로봇 제어·모니터링 클라우드 서비스 ARC brain 의 기능(로봇·태스크 모니터링, 운영 이력, 시설 연동, 맵 에디터, 알림)을 소개한다. 문서 최종 수정 2026-09-17.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://guide.ncloud-docs.com/docs/arc-brain-overview",
      "source_unopened": false
    },
    {
      "id": "ref-1179",
      "org": "아주경제",
      "title": "현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 (제목은 검색 결과 기준)",
      "published": "2025-04-07",
      "url": "https://www.ajunews.com/view/20250407084333272",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "현대차·기아와 한림대학교의료원의 로봇 친화 병원 협약(배송 로봇·관제 시스템·안면 인식 인증·특수 물품 배송 이력 관리)을 보도한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.ajunews.com/view/20250407084333272",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
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
      "rationale": "섹션 3: f16(왜 중요한가), f15(핵심 질문 답, 추정) / 섹션 4: 작업 상태 모델 f3, 수준별 로그 f4, 시각 색인 기록 형식 f6, 에이전트 투명성 f9, 설명 가능한 MAPF f8 / 섹션 5: 병원 — f14(완료·인계: 특수 물품 배송 이력·안면 인식 수령 인증, 계획 단계임을 명시), 상업 시설 — f12(수행 자원: 건물 설비 연동 통합 관제, 벤더 주장 병기). 물류창고·제조 공장·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 지도 위 상태 표시 f1·f5, 설명 가능한 표시 f8·f9·f10, 실행 기록·재생 f2·f3·f4·f6·f7 / 섹션 7: Open-RMF rmf_visualization·rmf-web·rmf_api_msgs f1~f4, VDA 5050 visualization 토픽 f5, MCAP f6, ISA-101 f11, 상용 도구 예 f7·f13(벤더 주장) / 섹션 8: f8·f9·f10 / 섹션 9: f17(직접 범위), f18(연계 대상) / 섹션 10: f19 — 11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 36, 38, 39, 43, 63, 64 / 섹션 11: 기존 oq-131(미해결 유지)과 open_questions_new 4건. 다음 실행 후보: 36. 가상 시운전·실제 상황 재현 페이지에 f6·f7(기록 재생) 반영, 38. 모니터링·이상 탐지·원인 분석 페이지에 f4(로그 수준)·f11(ISA-101) 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "설명 가능한 다중 에이전트 경로 찾기",
      "term_en": "Explainable Multi-Agent Path Finding (Explainable MAPF)",
      "definition": "여러 에이전트의 충돌 없는 경로를 찾으면서, 궤적이 서로 겹치지 않는 시간 구간 이미지 몇 장만으로 사람이 계획의 안전을 눈으로 확인할 수 있게 하는 경로 계획 문제다."
    },
    {
      "term_ko": "HMI 철학",
      "term_en": "HMI Philosophy (ISA-TR101.01)",
      "definition": "한 조직의 인간–기계 인터페이스 화면을 일관되게 설계·운영하기 위해 원칙과 규칙을 정해 둔 상위 문서로, ISA-101 계열에서 기술 보고서로 다룬다."
    },
    {
      "term_ko": "로그 재생",
      "term_en": "Log Playback",
      "definition": "타임스탬프가 붙은 기록 데이터를 기록 시각 순서대로 다시 흘려 보내며 시간축을 탐색·가감속해 과거 시점의 상태를 다시 보는 기능이다."
    },
    {
      "term_ko": "상황 인식",
      "term_en": "Situation Awareness (SA)",
      "definition": "운영자가 주변 요소를 지각하고, 그 의미를 이해하며, 가까운 미래 상태를 예측하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? | 관련 영역: 37. 관제 화면·실행 기록, 21. 상호운용 표준·적합성 | 근거: f3 | 종류: 일반",
    "에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가? | 관련 영역: 37. 관제 화면·실행 기록, 31. 사람–로봇 협업 | 근거: f10 | 종류: 일반",
    "병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? | 관련 영역: 37. 관제 화면·실행 기록, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 일반",
    "공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? | 관련 영역: 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 근거: f11 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f9 SAT 모델 논문(ref-477): 출판사·DTIC·ADS 페이지가 403/405 로 열리지 않아 검색 결과 요약 범위로만 서술했고, SAT 세 수준의 정의는 출처 귀속이 불분명해 넣지 않음(용어집의 기존 SAT 항목 참조)",
      "f5 VDA 5050 state 메시지 최소 30초 간격: 원문을 열었으나 요약 도구를 거친 확인이라 판 번호별 문구는 검증 필요",
      "f11 ISA-101.01 본문 미열람(유료). 비정상 상황 감지·진단·대응 개선 목적, 변경 관리(MOC)·감사 작업 과정은 제3자 요약에만 있어 넣지 않음",
      "ISO 11064(관제실 인간공학 설계) 각 부의 범위: ISO 페이지 403 으로 원문을 열지 못해 출처로 넣지 않음",
      "oq-131: 플릿 실행 기록을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식은 찾지 못함. RoboCup Logistics League 경기 기록을 객체 중심 이벤트 로그(OCEL)로 만든 연구(Springer 2026 챕터)는 페이지가 열리지 않아 넣지 않음",
      "Rohrer 외(arXiv 2207.10017) 객체 중심 프로세스 예측이 RCLL 데이터를 쓰는지 초록에서 확인하지 못함(PDF 추출 실패)",
      "f12·f13·f7 벤더 기능 주장: 독립 출처로 교차 확인하지 못함",
      "f14 병원 관제·배송 이력 시스템: 협약 단계 보도뿐이며 실제 운영 여부 미확인. 계명대 동산의료원 배송 로봇 기사(병원신문 2023-04-24)는 관제 화면 내용이 없어 넣지 않음",
      "물류창고·제조 공장·가정·실외 현장의 관제 화면·실행 기록 사례는 찾지 못함"
    ],
    "scope_violations": [
      "f18: 로봇 온보드 센서·주행 기록과 로컬 회피 시각화, 시설 설비 자체 관제 화면은 연계 대상으로 표시함",
      "f6·f7: 기록 재생은 과거 실행을 다시 보는 기능으로 다루며 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)과 섞지 않음. 재생을 시뮬레이션 재현으로 넓히는 부분은 36. 가상 시운전·실제 상황 재현 연결로만 제안함",
      "f1·f5: 지도 위 현재 상태 표시는 18. 실시간 세계 상태·데이터 일관성의 상태를 보여 주는 화면으로 보고, 상태 모델 자체는 18번 소관으로 연결만 제안함"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-1165~ref-1179, 예약 구간 안)로 출처 상한에 도달해 ISO 11064, RCLL 객체 중심 이벤트 로그, 물류창고·제조 공장 관제 화면 사례를 더 넣지 못했다. 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건이고 전체 목록 id 를 받지 못함. VDA 5050·MCAP 이 기존 목록에 같은 URL 로 있으면 퍼블리셔가 합친다). 원문 열람: 14건 열었고(github_raw 6건, webfetch 8건) SAT 논문(ref-477)만 열지 못해 source_unopened 로 표시했다. 논문은 Roldán 외(PMC 본문) 외에 Kottinger 외는 초록만 봤다. 교차 확인 0건: 핵심 내용이 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더 문서 기능 주장(f7·f12·f13)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에는 f15 로 답했고 결론은 '무엇을 보여 주는 요소는 공개 구현·표준에 있으나 왜를 보여 주는 설명 표시는 실험실 연구 수준이며 현장 평가 자료를 찾지 못했다'는 추정이다. 현장 유형 사례는 병원(f14, 협약 단계)·상업 시설(f12, 벤더 주장)뿐이며 물류창고·제조 공장·가정·실외는 찾지 못했다. 국내 자료는 현대차 로보틱스랩(ref-1177)·네이버클라우드(ref-1178)·아주경제(ref-1179) 3건이다. oq-131 은 근거를 찾지 못해 해결 제안하지 않았다. 용어집에 이미 있는 백 파일·MCAP·상황 인식 기반 에이전트 투명성·감사 추적·관측성·오픈 RMF·VDA 5050 은 후보로 내지 않았다. 페이지 제안은 대상 영역 갱신 1건이고 36·38번 반영은 다음 실행 후보로 적었다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-13/verification.json

```json
{
  "run_id": "2026-09-30-13",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw README(github_raw) 열람. 패키지별로 DoorState·LiftState 상태, 플릿 상태의 로봇 위치, 닫힌 차선 회색·속도 제한 차선 좁은 폭, 일정 궤적 초록 선, BuildingMap 평면도, 장애물을 RViz 마커로 표시하고 start_duration·query_duration 으로 조회 기간을 정한다. 단일 출처(프로젝트 자체 문서), 발행일 미확인."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf-web README 열람. 'web-based interface for users to visualize and control all aspects of Open-RMF deployments', 기본 API 서버는 internal non-persistent database를 쓰고 RMF_API_SERVER_CONFIG 설정 파일로 영속 저장을 구성한다. 발행일 미확인."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: task_state.json 열람. status 값 12개는 $defs/status에 정의되고 task_state가 이를 참조한다. original_estimate_millis·estimate_millis·assigned_to·phases·completed·active·pending·interruptions·cancellation·killed 필드가 있다. 최상위 필수 필드는 booking 하나뿐이다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: task_log.json(제목 'Task Event Log', 작업·단계·사건 3계층)과 log_entry.json(seq·tier·unix_millis_time·text 모두 필수, tier 4값, seq는 단조 증가하다가 오버플로 때 순환)을 열람했다. 두 파일이 같은 저장소라 독립 교차 확인은 아니다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 공식 저장소 main(3.0.0) 원문 열람. visualization 토픽 용도는 'High frequency communication of position and planned path'이고, state는 'published when relevant events occur or at least every 30 seconds'이다. 브리프 self_check가 적은 30초 문구 미검증 항목은 이번 검증에서 해소됐다. URL이 이전 브리프(2026-09-30-10)의 ref-1079와 같다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: mcap.dev/spec 열람. 개요 문장이 인용과 일치한다. Schema·Channel·Message·Chunk·Message Index·Chunk Index·Attachment·Metadata·Summary Offset 레코드가 있고, 색인으로 시각 기준 조회를 하며 압축은 선택이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Foxglove 재생 문서 열람. 시간축 탐색·속도 조절·구간 자르기·사건 생성과 검색·반복 재생·lookback·로그 시각 순서 전달이 적혀 있다. 벤더 문서라 [추정]과 '벤더 주장' 병기를 유지한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: arXiv 초록을 열람했다. 궤적이 겹치지 않는 시간 구간 이미지로 설명하는 개념은 초록이 'a recent work introduces'라고 밝힌 선행 연구(Almagor·Lahijanian, AAMAS 2020)의 것이다. NP-난해성도 이 논문이 새로 증명한 결과가 아니라 배경으로 적혀 있다. 따라서 'NP-난해임을 보인 뒤'는 귀속 오류다. 이 논문의 기여는 CBS의 제약 트리와 하위 A* 탐색에 설명 가능성 제약을 더한 것과 계획 시간–설명 가능성 절충 분석이다. XG-CBS라는 이름은 초록에 없으나 검색 결과(ICAPS 논문집 PDF)에서 확인했다. ICAPS 2022, arXiv 제출 2022-02-20."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 원문 미열람(출판사 403): UCF STARS 초록 페이지와 검색 결과(Ingenta·T&F)로 실재를 확인했다(19권 3호 259–282쪽, 2018). 초록은 SAT 모델을 세 연구 프로그램(자율 분대원, 사람과 여러 하위 로봇 사이의 중재자, 계획 추천 에이전트)에 적용했다고 적는다. 초록이 드는 효과는 공유 이해와 신뢰 보정에 효과적이라는 것이다. 'IMPACT·두 시스템'과 '투명할수록 운영자 수행이 일관되게 나아졌다'는 열람한 초록에서 확인되지 않았다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC는 reCAPTCHA, MDPI는 403이라 Europe PMC 전문 XML로 열람했다(epub 2017-07-27). 드론 2대·지상 로봇 1대, 화재 감시·진압 임무 8개, 운영자 24명, 실험실 5.35×6.70×5.00 m를 확인했다. SAGAT 순서는 PVRI>VRI>CI>PCI(관습·VR 묶음 비교 p=0.042), NASA-TLX 순서는 VRI<PVRI<CI<PCI다. 예측 요소는 유의하지 않고 관습형에서 부하를 늘렸다. evidence_excerpt의 SAGAT·NASA-TLX 수치(16.25·638 등)는 확인하지 못했다. 원문 요약 도구가 다른 수치(백분율)를 돌려줘 수치는 쓰지 않는다. 설계 요건(정보 선별·주의 유도·상태 통합·지도)은 본문과 대체로 맞는다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ISA 발행 기관 페이지 열람. ISA-101.01-2015, ISA-TR101.01-2022(HMI Philosophy), ISA-TR101.02-2019(HMI Usability and Performance)를 확인했다. 설계·구현·운영·지속 개선 수명주기와 'continuous, batch and discrete industries'도 확인했다. 표준 본문은 유료라 열지 않았다(소개 페이지 기준)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 불일치. 태그는 이미 [추정](벤더 주장)이라 더 낮출 태그가 없으므로, 뒷받침되지 않는 구절을 삭제하는 것으로 처분한다. 연구 과제 페이지 열람 결과 BPMN 2.0 워크플로, 실시간 이상 감지와 알람, 운영 리포팅·데이터 시각화, 엘리베이터·자동문·스크린도어 등 인프라 연동, 층별·존별 트래픽 관리를 확인했다. 적용처 '건물·상업 시설'은 페이지에 없다(실내외 환경, 다양한 환경만 나온다). site_type '상업 시설'은 근거가 없다. 발행일 미확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 네이버클라우드 사용 가이드 열람(최종 수정 2026-09-17). 다중 로봇 제어·충돌 방지, 실시간 모니터링과 알림, 태스크·운영 이력 조회, 제3자 로봇 등록, 엘리베이터·자동문 연동, 맵 에디터, 알림 설정이 적혀 있다. 벤더 주장 병기를 유지한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 아주경제 기사(2025-04-07) 열람. 제목 '현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다'가 일치한다. 한림대학교성심병원(안양) 협약식, 병원 맞춤형 배송 로봇·관제 시스템, 안면 인식 인증, 특수물품 배송 이력 관리를 확인했다. 협약 단계 보도이며 운영 결과는 없다. 단일 기사라 신뢰도 low를 유지한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 유지한다. f8·f9 강등 뒤에도 '설명 표시는 연구 수준, 현장 평가 자료 미확인'이라는 결론은 성립한다. 검색 범위 한정 문구를 유지한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "태그는 이미 [추정]이라 더 낮출 태그가 없으므로 구절 삭제·재서술로 처분한다. 'f9: 투명할수록 운영자 수행이 나아진다'는 f9 강등으로 근거를 잃었다. 'f10: 정보량이 많을수록 상황 인식과 작업 부하가 나빠진다'는 Roldán 외의 실험 결과가 아니라 그들이 제시한 설계 요건이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "종합 추정으로 유지한다. f7·f12·f13은 벤더 주장이므로 범위 예시로만 쓴다. 설비는 상태 표시만 하고 제어는 설비 쪽에 두는 서술이라 원문 19장 경계와 맞는다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연계 대상 서술로 유지한다. VDA 5050 visualization·state 분리(f5)와 플릿 관리자 보고 위치 표시(f1)가 근거로 확인된다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 목록으로 유지한다. 다만 '64. 상업 시설(f12)'은 f12의 상업 시설 근거가 없어 빼야 한다(수정 지시). 나머지 연결은 finding 근거와 맞는다. 18번(현재 상태)과 36번(과거 기록 재현)은 34번과 섞이지 않았다."
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
      "ref-031(VDA 5050 VDA5050_EN.md, main 3.0.0)은 이전 브리프 2026-09-30-10의 ref-1079와 URL이 같다(https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md)",
      "oq-131(열림)은 이 영역의 조사 질문 4와 겹친다. 이번 브리프는 해결 근거가 없어 미해결 유지로 제안했고 이는 타당하다",
      "용어집에 이미 있는 MCAP·상황 인식 기반 에이전트 투명성·오픈 RMF·VDA 5050·감사 추적·관측성은 후보로 내지 않았다(중복 없음)"
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
    "f8: [사실] → [추정]으로 강등하고, 'NP-난해임을 보인 뒤'를 삭제한다. '선행 연구가 제안한 시간 구간 이미지 설명 개념을 받아 CBS의 제약 트리와 A* 탐색에 설명 가능성 제약을 더한 XG-CBS를 제안하고 계획 시간과 설명 가능성의 절충을 분석했다'로 고쳐 쓴다 — ref-1173 초록이 설명 개념과 NP-난해성을 선행 연구의 것으로 적는다.",
    "f9: [사실] → [추정]으로 강등한다. 본문은 'SAT 모델을 세 연구 프로그램(자율 분대원, 사람과 여러 하위 로봇의 중재자, 계획 추천 에이전트)에 적용했고 공유 이해와 신뢰 보정에 효과적이라고 정리했다'로 줄인다. 'IMPACT·두 시스템'과 '투명할수록 수행이 일관되게 나아졌다'는 넣지 않는다 — 열람 가능한 초록에서 확인되지 않았다.",
    "ref-477: 페이지 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates의 ref-477 항목에 source_unopened: true를 넣는다 — 출판사 페이지 403으로 원문을 열지 못했다.",
    "f10: evidence_excerpt의 SAGAT·NASA-TLX 수치(16.25·16.46·14.91·14.33·638·740·853·915)는 본문에 쓰지 않는다. 인터페이스 순서(상황 인식 PVRI>VRI>CI>PCI, 부하 VRI<PVRI<CI<PCI), VR 묶음 차이(p=0.042), '예측 요소 효과는 유의하지 않았고 관습형 인터페이스에서는 부하가 수치상 늘었다'만 쓴다 — 검증 열람에서 수치를 재현하지 못했다.",
    "f12: '적용처로 건물·상업 시설을 든다'를 삭제하고, 연동 설비는 원문 표기대로 '엘리베이터·자동문·스크린도어 등', 운영 환경은 '실내외 환경의 층별·존별 트래픽 관리'로 적는다. [추정]과 '벤더 주장' 병기를 유지한다 — ref-1177 페이지에 상업 시설 적용처가 없다.",
    "5절(적용 사례): f12를 상업 시설 사례로 쓰지 않고 site_matrix_updates에 '상업 시설' 칸을 넣지 않는다. f12는 6·7절의 벤더 사례로만 쓴다 — 현장 유형 근거가 없다.",
    "5절(적용 사례): 병원 사례(f14)는 2025-04-07 보도 기준 협약·개발 계획 단계이며 운영 결과가 확인되지 않았음을 밝힌다. 여섯 항목 가운데 근거 없는 칸(시작 조건·제약·예외·성과 등)은 '미확인'으로 둔다. 물류창고·제조 공장·상업 시설·가정·실외·기타 사례는 찾지 못했다고 적는다.",
    "f16(3절): '(f9) 에이전트의 판단이 투명할수록 운영자 수행이 나아지며'를 삭제한다. '(f10) 정보량이 많을수록 상황 인식과 작업 부하가 나빠지고'는 'Roldán 외가 다중 로봇 인터페이스 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었다'로 바꾼다. [추정]은 유지한다 — f9 강등, f10은 실험 결과가 아니라 설계 요건이다.",
    "f19(10절): '64. 상업 시설(f12)' 연결을 삭제한다 — f12에 상업 시설 근거가 없다.",
    "f7·f12·f13: 페이지 어디에 쓰든(6·7·9절 포함) [추정]과 '벤더 주장'을 함께 적는다 — 제조사·서비스 제공자 문서이고 독립 교차 확인이 없다.",
    "ref-031: 이전 실행의 ref-1079와 URL이 같으므로, ref-1079가 참고문헌에 등록돼 있으면 각주와 프런트매터 sources에서 ref-1079를 재사용하고 ref-1170은 reference_updates에 새로 넣지 않는다 — 같은 출처에는 기존 각주를 재사용한다.",
    "용어 후보 '상황 인식': 정의에서 '지각·이해·예측' 3단계 설명을 빼고, '운영자가 임무 환경의 상황을 파악하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다' 수준으로 줄인다 — 3단계 정의를 뒷받침하는 finding이 없다.",
    "용어 후보 'HMI 철학': 정의를 'ISA-101 계열이 기술 보고서 ISA-TR101.01-2022로 다루는 HMI 설계 원칙 문서' 수준으로 줄이고, '한 조직의 … 원칙과 규칙을 정해 둔 상위 문서'라는 내용 설명은 뺀다 — ISA 소개 페이지는 제목만 확인해 준다.",
    "ref-1179: 제목 뒤의 '(제목은 검색 결과 기준)'을 지운다 — 검증 열람에서 기사 제목 '현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다'를 확인했다.",
    "11절(열린 질문): oq-131은 해결로 바꾸지 않고 열림으로 유지한다. open_questions_new 4건은 형식이 맞으므로 그대로 등록한다 — 해결 근거 finding이 없다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 15건, 미확인 4건(f8·f9·f12·f16), 교차 확인 0건. 강등: f8 사실 → 추정(설명 개념과 NP-난해성을 선행 연구에 잘못 귀속), f9 사실 → 추정(열람 가능한 초록에서 수행 향상 결과 미확인), f12·f16은 이미 추정이라 뒷받침되지 않는 구절을 삭제. 원문 미열람 출처: ref-477. 주의: 핵심 내용은 모두 단일 출처이고 절반가량이 종합 추정이다. 관제 화면 요소는 Open-RMF·VDA 5050·MCAP 같은 공개 구현·명세 문서 기준이며, 설명 가능한 표시의 효과는 실험실·알고리즘 연구에 한정된다. 현장 사례는 병원 1건(협약 단계 보도)뿐이다. Roldán 외의 SAGAT·NASA-TLX 수치는 검증 열람에서 재현하지 못해 순서와 유의성만 싣는다. 나콘·ARC brain·Foxglove 기능은 벤더 주장이다. ref-1170은 이전 실행 ref-1079와 같은 URL이다. 정정 요청 없음. oq-131은 미해결 유지.",
  "retry_reason": null
}
```

### runs/2026-09-30-13/pages.json

```json
{
  "run_id": "2026-09-30-13",
  "outline": [
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 550,
      "summary": "관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다. '무엇'을 보여 주는 요소는 공개 구현·표준에 있지만 '왜'를 보여 주는 설명 표시는 연구 수준이다. [추정][^ref-1165][^ref-1175]",
      "planned_findings": [
        "f16",
        "f15"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 850,
      "summary": "관제 화면과 실행 기록에 관련된 개념을 정리한다. 작업 상태 값 12개와 3계층 작업 사건 로그, 시각 색인 기록 형식 MCAP은 [사실][^ref-111][^ref-1168][^ref-1171], 에이전트 투명성과 설명 가능한 MAPF는 [추정][^ref-477][^ref-1173]이다.",
      "planned_findings": [
        "f3",
        "f4",
        "f6",
        "f9",
        "f8",
        "f10"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 650,
      "summary": "병원: 한림대학교의료원 협약(2025-04-07 보도)의 배송 로봇·관제 시스템·안면 인식 수령 인증·특수 물품 배송 이력 관리 개발 계획. 운영 결과는 미확인이다. [사실][^ref-1179]",
      "planned_findings": [
        "f14",
        "f16"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 850,
      "summary": "지도 위 통합 상태 표시(Open-RMF 시각화, VDA 5050 visualization 토픽), 실행 기록 저장·재생(rmf-web 영속 저장, Foxglove 재생), 설명 가능한 표시(연구 단계)의 세 갈래다. [추정][^ref-1165][^ref-302][^ref-1173]",
      "planned_findings": [
        "f1",
        "f5",
        "f12",
        "f13",
        "f2",
        "f7",
        "f15"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 650,
      "summary": "Open-RMF rmf_visualization·rmf-web·rmf_api_msgs, VDA 5050 3.0.0, MCAP, ISA-101 계열과 벤더 도구 Foxglove를 표로 정리한다. [사실][^ref-1176]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f11",
        "f7"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "Kottinger 외 XG-CBS, Chen 외 SAT, Roldán 외 다중 로봇 인터페이스 실험이 설명 가능한 표시의 연구 근거다. [추정][^ref-1173][^ref-477][^ref-1175]",
      "planned_findings": [
        "f8",
        "f9",
        "f10"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 600,
      "summary": "ROP는 제조사·설비가 보고한 상태를 한 층별 지도와 공통 상태·로그로 표시·기록·재생하고, 로봇 온보드 기록과 설비 자체 관제 화면은 연계 대상이다. [추정][^ref-1165][^ref-031]",
      "planned_findings": [
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 850,
      "summary": "38. 모니터링·이상 탐지·원인 분석과 39. 운영 성과 측정·개선, 15. 지도·공간·위치 모델과 18. 실시간 세계 상태·데이터 일관성, 36. 가상 시운전·실제 상황 재현 등 재현 영역, 20·21·22 연동 영역, 43. 데이터·관측성·배포, 17·63 병원 인계 영역과 이어진다. [추정][^ref-111]",
      "planned_findings": [
        "f19"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "section": "11. 열린 질문",
      "budget_chars": 500,
      "summary": "oq-131(열림 유지)과 새 질문 4건: 공통 상태·로그 규약, 설명 표시의 현장 평가, 병원 배송 이력 보관 요건, 다중 로봇 관제 화면 설계 지침.",
      "planned_findings": [
        "f3",
        "f10",
        "f11",
        "f14"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성, 13절 각주 정의 15건, 프런트매터 related_areas·tags·confidence·sources·last_run 채움(1차 조건부 승인 수정 15건 반영). 2차: 3절 첫 문장을 태그 없는 연결 문장으로, 4절 도입 문장의 [사실] 태그 제거, 9절 '상용 예로'를 '6절에서 예로'로 고침"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area37-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"6. 대표 접근법과 기술\" 절을 옮겼다. 2차: '국내 상용 예로'를 '국내 예로(연구 과제 페이지 기준)'로 고침"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area37-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"8. 대표 연구와 자료\" 절을 옮겼다(2차 재실행에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area37-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"4. 핵심 개념과 용어\" 절을 옮겼다. 2차: 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 뗀 연결 문장으로 바꿈"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area37-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 37. 관제 화면·실행 기록 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절을 옮겼다. 2차: 짝 엔진을 번호와 이름으로 표기, 39. 운영 성과 측정·개선 항목의 '실제 소요 시간' 드리프트 수정"
    }
  ],
  "changelog_entry": "2026-09-30 | 37. 관제 화면·실행 기록 | 영역 심화: 3~11절 신규 작성(Open-RMF 시각화·작업 상태·로그 스키마, VDA 5050 시각화 토픽, MCAP, ISA-101, 설명 가능한 표시 연구, 병원 사례), 1차 조건부 승인 수정 15건과 2차 수정 6건 반영 | run 2026-09-30-13",
  "index_updates": {
    "home_recent": "2026-09-30 — 37. 관제 화면·실행 기록: 영역 심화로 3~11절을 처음 작성(지도 위 통합 상태 표시, 작업 상태·로그 스키마와 기록 재생, 설명 가능한 표시 연구, 병원 배송 이력 사례)",
    "category_recent": "2026-09-30 — 37. 관제 화면·실행 기록: 영역 심화 초안(Open-RMF·VDA 5050·MCAP·ISA-101 정리, 설명 가능한 표시는 연구 단계, 현장 사례는 병원 협약 1건)",
    "area_recent": "2026-09-30 — 37. 관제 화면·실행 기록: 3~11절 신규 작성, 새 열린 질문 4건, 신뢰도 low"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "explainable-mapf",
      "term_ko": "설명 가능한 다중 에이전트 경로 찾기",
      "term_en": "Explainable Multi-Agent Path Finding (Explainable MAPF)",
      "definition": "여러 에이전트의 충돌 없는 경로를 찾으면서, 궤적이 서로 겹치지 않는 시간 구간 이미지 몇 장만으로 사람이 계획의 안전을 눈으로 확인할 수 있게 하는 경로 계획 문제다.",
      "description": "설명 개념은 선행 연구가 제안했고, Kottinger 외(ICAPS 2022)는 충돌 기반 탐색에 설명 가능성 제약을 더한 XG-CBS를 제안했다.",
      "related_areas": [
        37,
        27
      ],
      "sources": [
        "ref-1173"
      ]
    },
    {
      "action": "new",
      "slug": "hmi-philosophy",
      "term_ko": "HMI 철학",
      "term_en": "HMI Philosophy (ISA-TR101.01)",
      "definition": "ISA-101 계열이 기술 보고서 ISA-TR101.01-2022로 다루는 HMI 설계 원칙 문서다.",
      "related_areas": [
        37,
        38
      ],
      "sources": [
        "ref-1176"
      ]
    },
    {
      "action": "new",
      "slug": "log-playback",
      "term_ko": "로그 재생",
      "term_en": "Log Playback",
      "definition": "타임스탬프가 붙은 기록 데이터를 기록 시각 순서대로 다시 흘려 보내며 시간축을 탐색·가감속해 과거 시점의 상태를 다시 보는 기능이다.",
      "related_areas": [
        37,
        36,
        43
      ],
      "sources": [
        "ref-1172",
        "ref-1171"
      ]
    },
    {
      "action": "new",
      "slug": "situation-awareness",
      "term_ko": "상황 인식",
      "term_en": "Situation Awareness (SA)",
      "definition": "운영자가 임무 환경의 상황을 파악하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다.",
      "related_areas": [
        37,
        31
      ],
      "sources": [
        "ref-1175"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1165",
      "org": "Open Robotics (open-rmf/rmf_visualization)",
      "title": "rmf_visualization — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_visualization",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 시각화 패키지 8종이 승강기·문, 로봇 위치, 주행 그래프, 예측 일정 궤적, 평면도, 장애물을 RViz 로 표시하는 방식을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf/rmf-web)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 대시보드·API 서버·API 클라이언트 구성과 기본 비영속 데이터베이스 설정을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 작업 상태 JSON 스키마. 상태 값 12개, 추정 소요 시간, 단계 목록, 일시정지·취소·강제 종료 정보를 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1168",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — task_log.json (Task Event Log)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 작업 로그 JSON 스키마. 작업·단계·사건 수준으로 로그를 계층화한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1169",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — log_entry.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 로그 항목 JSON 스키마. 순번, 중요도 tier, 밀리초 시각, 본문을 필수 필드로 둔다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA (VDA5050/VDA5050)",
      "title": "VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 저장소 main 브랜치(3.0.0) 명세 원문. visualization 토픽과 state 토픽의 역할·전송 조건(사건 발생 시 또는 최소 30초 간격)을 확인했다. 이전 실행 2026-09-30-10 의 ref-1079 와 같은 URL 이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1171",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타임스탬프 발행·구독 메시지를 담는 MCAP 컨테이너 형식의 레코드 종류와 시각 색인 기반 임의 접근 구조를 정의한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1172",
      "org": "Foxglove",
      "title": "Playback — Foxglove Documentation",
      "published": null,
      "url": "https://docs.foxglove.dev/docs/visualization/playback",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇 기록 시각화 도구의 재생 기능(시간축 탐색, 속도, 구간, 사건 주석, 반복, lookback)을 설명하는 제품 문서.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1173",
      "org": "Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022)",
      "title": "Conflict-Based Search for Explainable Multi-Agent Path Finding",
      "published": "2022-02",
      "url": "https://arxiv.org/abs/2202.09930",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "선행 연구의 시간 구간 이미지 설명 개념을 받아 CBS 의 제약 트리와 A* 탐색에 설명 가능성 제약을 더한 XG-CBS 를 제안하고 계획 시간–설명 가능성 절충을 분석한다(초록 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-477",
      "org": "Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3))",
      "title": "Situation awareness-based agent transparency and human-autonomy teaming effectiveness",
      "published": "2018",
      "url": "https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. SAT 모델을 세 연구 프로그램(자율 분대원, 사람과 여러 하위 로봇의 중재자, 계획 추천 에이전트)에 적용했고 공유 이해와 신뢰 보정에 효과적이라고 정리했다는 내용을 초록·검색 결과로 확인했다(출판사 페이지 403).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1175",
      "org": "Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8))",
      "title": "Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction",
      "published": "2017-07-27",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "다중 로봇 임무 감독 인터페이스 4종을 운영자 24명으로 비교해 상황 인식·작업 부하를 측정하고 인터페이스 설계 요건을 제시한 동료심사 논문.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1176",
      "org": "ISA (International Society of Automation)",
      "title": "ISA-101 Series of Standards",
      "published": null,
      "url": "https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ISA-101.01-2015 와 TR101.01-2022·TR101.02-2019 의 목록과 범위를 소개하는 발행 기관 페이지. 표준 본문은 유료라 열지 않았다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1177",
      "org": "현대자동차그룹 로보틱스랩",
      "title": "PROJECTS — Robot Fleet Management (NARCHON)",
      "published": null,
      "url": "https://robotics.hyundai.com/projects/research/view.do?seq=102",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "이기종 로봇 통합 관제 시스템 나콘의 모니터링 대시보드·BPMN 2.0 워크플로·엘리베이터·자동문·스크린도어 등 인프라 연동·층별·존별 트래픽 관리를 소개하는 연구 과제 페이지.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1178",
      "org": "네이버클라우드",
      "title": "ARC brain 개요 - 사용 가이드",
      "published": null,
      "url": "https://guide.ncloud-docs.com/docs/arc-brain-overview",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "멀티 로봇 제어·모니터링 클라우드 서비스 ARC brain 의 기능(로봇·태스크 모니터링, 운영 이력, 시설 연동, 맵 에디터, 알림)을 소개한다. 문서 최종 수정 2026-09-17.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    },
    {
      "id": "ref-1179",
      "org": "아주경제",
      "title": "현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다",
      "published": "2025-04-07",
      "url": "https://www.ajunews.com/view/20250407084333272",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "현대차·기아와 한림대학교의료원의 로봇 친화 병원 협약(배송 로봇·관제 시스템·안면 인식 인증·특수 물품 배송 이력 관리)을 보도한 기사. 협약 단계이며 운영 결과는 없다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가?",
      "areas": [
        37,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가?",
      "areas": [
        37,
        31
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가?",
      "areas": [
        37,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가?",
      "areas": [
        37,
        38
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시",
      "title": "37. 관제 화면·실행 기록"
    }
  ],
  "standards_updates": [
    {
      "name": "ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능)",
      "kind": "표준",
      "org": "ISA(International Society of Automation)",
      "url": "https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards",
      "related_areas": [
        37,
        38
      ],
      "summary": "공정 자동화 시스템의 HMI 표준 계열로, 설계·구현·운영·지속 개선의 HMI 수명주기를 다루며 연속·배치·이산 산업에 적용된다고 밝힌다(발행 기관 소개 페이지 기준, 본문 유료).",
      "ref_id": "ref-1176"
    },
    {
      "name": "Open-RMF rmf_visualization",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_visualization",
      "related_areas": [
        37,
        15,
        22
      ],
      "summary": "층 평면도 위에 플릿 관리자가 보고한 로봇 위치, 문·승강기 상태, 주행 그래프, 예측 일정 궤적을 겹쳐 표시하는 시각화 패키지 묶음.",
      "ref_id": "ref-1165"
    },
    {
      "name": "Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json",
      "related_areas": [
        37,
        38,
        43
      ],
      "summary": "작업·단계·사건 3계층 로그와 순번·중요도 tier·밀리초 시각·본문을 필수로 둔 로그 항목을 정의한 JSON 스키마.",
      "ref_id": "ref-1168"
    }
  ],
  "additional_research_requests": [
    "5절: 물류창고·제조 공장·상업 시설·가정·실외·기타 현장에서 로봇 관제 화면·실행 기록을 운영에 쓴 사례(여섯 항목을 채울 근거) — 현재 병원 1건(협약 단계 보도)뿐이다.",
    "5절: 한림대학교의료원 병원 배송 사례의 시작 조건·제약·예외·성과와 실제 운영 여부 — 2025-04-07 보도 이후 운영 결과 자료가 필요하다.",
    "7절: ISO 11064(관제실 인간공학 설계) 각 부의 범위 — 발행 기관 원문을 열지 못해 넣지 못했다.",
    "8절: Chen 외(2018) SAT 논문 원문 열람 — 실험 시스템(IMPACT 등)과 투명성 수준별 수행 결과를 확인해야 [사실]로 쓸 수 있다.",
    "11절 oq-131: RoboCup Logistics League 경기 기록을 객체 중심 이벤트 로그(OCEL)로 만든 연구 등 플릿 실행 기록을 시나리오로 바꾸는 공개 형식 근거.",
    "10절: 작업 실제 소요 시간(시작·완료 시각) 기록 필드와 성과 지표 산출 방식을 담은 자료 — 39. 운영 성과 측정·개선 연결을 구체화하려면 필요하다.",
    "전반: 핵심 사실(Open-RMF 스키마, VDA 5050 토픽, Roldán 외 결과)이 모두 단일 출처라 독립 교차 확인 자료가 필요하다."
  ],
  "fixes_applied": [
    "f8 강등·재서술 — 4절·8절에서 [추정]으로 쓰고 'NP-난해임을 보인 뒤'를 빼고 '선행 연구가 제안한 시간 구간 이미지 설명 개념을 받아 CBS의 제약 트리와 A* 탐색에 설명 가능성 제약을 더한 XG-CBS를 제안하고 계획 시간과 설명 가능성의 절충을 분석했다'로 고쳤다.",
    "f9 강등·축약 — 4절·8절에서 [추정]으로 쓰고 'SAT 모델을 세 연구 프로그램(자율 분대원, 사람과 여러 하위 로봇의 중재자, 계획 추천 에이전트)에 적용했고 공유 이해와 신뢰 보정에 효과적이라고 정리했다'로 줄였으며 IMPACT·두 시스템·수행 향상 문구는 넣지 않았다.",
    "ref-477 원문 미열람 표시 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 항목에 source_unopened: true 를 넣었다.",
    "f10 수치 제외 — 8절에 SAGAT·NASA-TLX 수치를 쓰지 않고 상황 인식·부하 순서, 가상현실 묶음 차이 p=0.042, 예측 요소 효과 비유의와 기존 인터페이스 부하의 수치상 증가만 썼다.",
    "f12 재서술 — 6절에서 '적용처로 건물·상업 시설' 구절을 빼고 연동 설비를 '엘리베이터·자동문·스크린도어 등', 운영 환경을 '실내외 환경의 층별·존별 트래픽 관리'로 적었으며 [추정] 벤더 주장을 병기했다.",
    "5절 상업 시설 제외 — f12를 적용 사례로 쓰지 않고 6절·9절 벤더 예로만 썼으며 site_matrix_updates 에 상업 시설 칸을 넣지 않았다.",
    "5절 병원 사례 — 2025-04-07 보도 기준 협약·개발 계획 단계이고 운영 결과가 확인되지 않았음을 밝히고, 시작 조건·제약·예외·성과 칸을 '미확인'으로 두었으며, 물류창고·제조 공장·상업 시설·가정·실외·기타 사례는 찾지 못했다고 적었다.",
    "f16 재서술 — 3절에서 f9 근거의 '투명할수록 수행이 나아진다' 구절을 빼고, f10 구절을 'Roldán 외가 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었다'로 바꾸었으며 [추정]을 유지했다.",
    "f19 연결 수정 — 10절과 프런트매터 related_areas 에서 64. 상업 시설을 뺐다.",
    "벤더 주장 병기 — f7(Foxglove)·f12(나콘)·f13(ARC brain)을 쓴 6·7·9절의 모든 문장·표 칸에 [추정] 벤더 주장을 함께 적었다.",
    "ref-031 재사용 확인 — 입력의 참고문헌 목록(docs_tree 기준)에 ref-1079가 등록돼 있지 않아 재사용할 수 없으므로 각주·sources 에 브리프 id ref-031을 쓰고 reference_updates 에 넣었으며, summary 에 이전 실행 ref-1079 와 같은 URL 임을 적어 퍼블리셔가 합칠 수 있게 했다.",
    "용어 '상황 인식' 축약 — 지각·이해·예측 3단계 설명을 빼고 '운영자가 임무 환경의 상황을 파악하는 정도로, 관제 화면 평가에서 SAGAT 같은 질의 기법으로 측정한다'로 glossary_updates 와 4절에 썼다.",
    "용어 'HMI 철학' 축약 — 정의를 'ISA-101 계열이 기술 보고서 ISA-TR101.01-2022로 다루는 HMI 설계 원칙 문서'로 줄이고 내용 설명을 뺐다.",
    "ref-1179 제목 수정 — '(제목은 검색 결과 기준)'을 지우고 '현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다'로 각주와 reference_updates 에 썼다.",
    "11절 열린 질문 — oq-131은 열림으로 유지하고(open_question_updates 에 상태 변경을 내지 않음), open_questions_new 4건을 open_question_updates 에 new 로 등록하고 11절에 적었다.",
    "2차: 짝 엔진 표기 — 분리 페이지 s10 의 11. 채팅으로 실제 상황 시뮬레이션 재현 항목에서 '짝 엔진은 33·36번 영역이다'를 '짝 엔진은 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현이다'로 고쳤다.",
    "2차: '상용' 표현 삭제 — 분리 페이지 s6 의 '국내 상용 예로'를 '국내 예로(연구 과제 페이지 기준)'로, 세부영역 9절의 '상용 예로 든 나콘·ARC brain·Foxglove'를 '6절에서 예로 든 나콘·ARC brain·Foxglove'로 고쳤고 [추정]과 '벤더 주장' 병기는 그대로 두었다.",
    "2차: 39. 운영 성과 측정·개선 연결 드리프트 — 분리 페이지 s10 의 해당 항목을 '작업 상태 값, 처음·현재 추정 소요 시간, 로그 항목의 시각 기록이 성과 지표의 원자료가 될 수 있다'로 고쳤다.",
    "2차: 3절 첫 문장 — '좌우한다' 단정과 [의견] 태그를 빼고 태그 없는 연결 문장 '관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.'로 바꿨다(outline 요약도 함께 고침).",
    "2차: 4절 도입 문장 — 세부영역 4절 첫 문장과 분리 페이지 s4 의 세 줄 요약·본문 첫 문장에서 [사실] 태그와 각주를 떼고 태그 없는 연결 문장 '관제 화면과 실행 기록에 관련된 개념을 정리한다.'로 바꿨다.",
    "2차: ref-031 요약·보고 문구 — reference_updates 의 ref-031 summary 에서 '참고문헌 목록에 ref-1079 가 없어 새 id 로 낸다' 구절을 지우고 '이전 실행 2026-09-30-10 의 ref-1079 와 같은 URL 이다.'만 남겼으며, fixes_applied 의 ref-031 항목을 실제로 쓴 id(ref-031)로 고쳤다."
  ]
}
```

### runs/2026-09-30-13/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-30-13/pages/categories/field-operations-and-monitoring/control-screen-and-execution-records.md

```markdown
---
title: "37. 관제 화면·실행 기록"
type: area
category: "J. 현장 운영·관제"
area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [관제 화면, 실행 기록, 작업 상태, 로그 재생, 설명 가능한 표시, Open-RMF]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1165, ref-302, ref-111, ref-1168, ref-1169, ref-031, ref-1171, ref-1172, ref-1173, ref-477, ref-1175, ref-1176, ref-1177, ref-1178, ref-1179]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 37. 관제 화면·실행 기록

# 37. 관제 화면·실행 기록

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]

## 3. 왜 중요한가

관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.

이 영역이 중요한 까닭은 세 가지로 정리된다. 다중 로봇 인터페이스 연구(Roldán 외)는 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었고, 공정 산업의 인간–기계 인터페이스(Human-Machine Interface, HMI) 표준은 화면을 설계·구현·운영·지속 개선의 수명주기 전체에 걸쳐 관리할 대상으로 보며, 병원처럼 배송 이력을 남기려는 현장에서는 실행 기록이 인계 확인의 근거가 된다. [추정][^ref-1175][^ref-1176][^ref-1179]

핵심 질문에 비추면, '무엇'을 보여 주는 요소(지도 위 로봇·설비·예측 궤적 표시, 작업 상태 값과 단계, 수준별 로그)는 공개 구현과 표준에 갖춰져 있지만, '왜'를 보여 주는 설명 가능한 표시는 실험실·시뮬레이션 연구 수준이다. 실제 다중 제조사 플릿 관제 화면에서 그 효과를 측정한 공개 자료는 이번 조사 범위(2026-09-30 기준)에서 찾지 못했다. [추정][^ref-1165][^ref-111][^ref-1168][^ref-031][^ref-1173][^ref-477][^ref-1175]

## 4. 핵심 개념과 용어

관제 화면과 실행 기록에 관련된 개념을 정리한다.

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area37-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 관제 화면·실행 기록의 현장 근거를 찾은 것은 병원 한 건이며, 그것도 협약·개발 계획 단계 보도다. [사실][^ref-1179]

**현장 유형:** 병원

**사례:** 병원에서 특수 물품을 로봇으로 배송하고 수령 인증과 배송 이력을 남기는 계획(한림대학교의료원 협약, 2025-04-07 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 특수 물품(품목 범위는 미확인) [사실][^ref-1179] |
| 수행 자원 | 병원 맞춤형 배송 로봇과 관제 시스템(공동 개발 계획) [사실][^ref-1179] |
| 제약 | 미확인 |
| 완료·인계 | 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템(개발 계획) [사실][^ref-1179] |
| 예외·성과 | 미확인(운영 결과 보도 없음) |

아주경제 2025-04-07 보도에 따르면 현대차·기아는 한림대학교의료원과 업무협약을 맺고 병원 맞춤형 배송 로봇과 관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 했다. [사실][^ref-1179] 이 보도는 협약·개발 계획 단계이며, 실제 운영 여부와 처리량·시간 같은 결과는 확인되지 않았다.

이 사례에서 37. 관제 화면·실행 기록은 완료·인계 칸에 관여한다. 배송 이력을 남겨야 하는 현장에서는 실행 기록이 '누구에게 넘겨졌는가'를 나중에 확인하는 근거가 된다. [추정][^ref-1179]

물류창고·제조 공장·상업 시설·가정·실외·기타 현장의 관제 화면·실행 기록 사례는 이번 조사(2026-09-30)에서 찾지 못했다.

## 6. 대표 접근법과 기술

접근법은 지도 위 통합 상태 표시, 실행 기록 저장과 시간축 재생, 설명 가능한 표시의 세 갈래로 나뉜다. 앞의 두 갈래는 공개 구현이 있고, 셋째는 연구 단계다. [추정][^ref-1165][^ref-302][^ref-1173]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area37-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

관제 화면·실행 기록에 쓸 수 있는 공개 구현과 명세는 다음과 같다(확인일 2026-09-30). [사실][^ref-1165][^ref-031][^ref-1171]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Open-RMF rmf_visualization | 오픈소스 | 층 평면도 위에 로봇 위치·문·승강기·주행 그래프·예측 궤적 표시 | [사실][^ref-1165] |
| Open-RMF rmf-web | 오픈소스 | 웹 대시보드·API 서버. 기본은 비영속 저장 | [사실][^ref-302] |
| Open-RMF rmf_api_msgs 작업 상태·작업 로그 스키마 | 오픈소스 | 상태 값 12개, 작업·단계·사건 3계층 로그 | [사실][^ref-111][^ref-1168][^ref-1169] |
| VDA 5050 3.0.0 visualization·state 토픽 | 표준 | 차량 위치·계획 경로를 시각화 시스템에 보내는 토픽을 상태 토픽과 분리 | [사실][^ref-031] |
| MCAP | 오픈소스 | 시각 색인을 둔 기록 컨테이너 형식 | [사실][^ref-1171] |
| ISA-101.01-2015, ISA-TR101.01-2022(HMI 철학), ISA-TR101.02-2019(HMI 사용성과 성능) | 표준 | HMI 수명주기(설계·구현·운영·지속 개선)를 다루며 연속·배치·이산 산업에 적용된다고 밝힌다. 표준 본문은 유료라 발행 기관 소개 페이지 기준 | [사실][^ref-1176] |
| Foxglove 재생 기능 | 벤더 도구 | 시간축 탐색·사건 주석·lookback 재생 | [추정] 벤더 주장[^ref-1172] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 8. 대표 연구와 자료

설명 가능한 표시와 다중 로봇 관제 인터페이스에 관한 연구는 다음 세 건이 대표적이며, 모두 실험실·알고리즘 수준이다. [추정][^ref-1173][^ref-477][^ref-1175]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 대표 연구와 자료](../../topics/2026/2026-09-30-area37-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 제조사 플릿과 설비가 내보내는 상태를 받아 하나의 화면과 기록으로 묶는 쪽을 맡고, 로봇 내부 기록과 설비 자체 관제 화면은 연계 대상으로 둘 것으로 보인다. [추정][^ref-1165][^ref-031]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 제조사 플릿이 보고한 위치·계획 경로·작업 상태를 하나의 층별 지도에 표시하고, 공통 작업 상태 값·단계·수준별 로그로 정규화해 기록 [추정][^ref-1165][^ref-111][^ref-1168] | 로봇 온보드 센서·주행 기록(로봇 쪽 bag·MCAP 기록), 로컬 회피 시각화 — 로봇 제조사 [추정][^ref-1171][^ref-031] |
| 시설·설비 제어 | 승강기·문 상태를 같은 지도에 겹쳐 표시하고 기록 [추정][^ref-1165] | 승강기·자동문·CCTV 같은 설비의 자체 관제 화면 — 시설·설비 쪽 [추정][^ref-1165] |

이번 자료를 종합하면 ROP가 직접 맡을 범위는 통합 화면, 정규화한 실행 기록, 그 기록의 영속 저장과 시각 색인 기반 재생·사건 검색, 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시다. [추정][^ref-1165][^ref-302][^ref-111][^ref-1168][^ref-1171][^ref-1173][^ref-477] 6절에서 예로 든 나콘·ARC brain·Foxglove도 같은 범위의 기능을 내세우지만 독립 확인이 없다. [추정] 벤더 주장[^ref-1177][^ref-1178][^ref-1172] ROP는 VDA 5050 visualization·state 토픽처럼 제조사가 내보내는 상태를 받는 인터페이스를 맡는다. [추정][^ref-031]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 화면과 기록은 운영·지도·연동·재현 영역과 두루 이어진다. 아래 연결은 이번 조사 자료를 바탕으로 한 판단이다. [추정][^ref-1165][^ref-111][^ref-1168][^ref-031][^ref-1175][^ref-1179]

자세한 내용은 주제 페이지 [37. 관제 화면·실행 기록 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area37-s10.md)에 있다.

## 11. 열린 질문

실행 기록을 시뮬레이션으로 바꾸는 형식, 공통 상태·로그 규약, 설명 표시의 현장 효과는 아직 확인되지 않았다(2026-09-30 기준). 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-131** (상태: 열림) 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? 이번 실행(2026-09-30-13)에서도 공개 형식을 찾지 못했다.
- (새 질문, 상태: 열림) 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가?
- (새 질문, 상태: 열림) 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가?
- (새 질문, 상태: 열림) 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가?
- (새 질문, 상태: 열림) 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가?

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1165]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-302]: Open Robotics (open-rmf/rmf-web), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-09-30
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-30
[^ref-1168]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-1169]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — log_entry.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json, 접근일 2026-09-30
[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1171]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-09-30
[^ref-1172]: Foxglove, Playback — Foxglove Documentation, 미확인, https://docs.foxglove.dev/docs/visualization/playback, 접근일 2026-09-30
[^ref-1173]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)
[^ref-1175]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-09-30
[^ref-1176]: ISA (International Society of Automation), ISA-101 Series of Standards, 미확인, https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards, 접근일 2026-09-30
[^ref-1177]: 현대자동차그룹 로보틱스랩, PROJECTS — Robot Fleet Management (NARCHON), 미확인, https://robotics.hyundai.com/projects/research/view.do?seq=102, 접근일 2026-09-30
[^ref-1178]: 네이버클라우드, ARC brain 개요 - 사용 가이드, 미확인, https://guide.ncloud-docs.com/docs/arc-brain-overview, 접근일 2026-09-30
[^ref-1179]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-09-30
```

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md

```markdown
---
title: "37. 관제 화면·실행 기록"
type: area
category: "J. 현장 운영·관제"
area_no: 37
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 37. 관제 화면·실행 기록

# 37. 관제 화면·실행 기록

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]

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

### runs/2026-09-30-13/pages/topics/2026/2026-09-30-area37-s6.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 대표 접근법과 기술"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1165, ref-302, ref-031, ref-1172, ref-1173, ref-477, ref-1175, ref-1177, ref-1178]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#6
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 대표 접근법과 기술

# 37. 관제 화면·실행 기록 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 접근법은 지도 위 통합 상태 표시, 실행 기록 저장과 시간축 재생, 설명 가능한 표시의 세 갈래로 나뉜다. 앞의 두 갈래는 공개 구현이 있고, 셋째는 연구 단계다. [추정][^ref-1165][^ref-302][^ref-1173]
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

접근법은 지도 위 통합 상태 표시, 실행 기록 저장과 시간축 재생, 설명 가능한 표시의 세 갈래로 나뉜다. 앞의 두 갈래는 공개 구현이 있고, 셋째는 연구 단계다. [추정][^ref-1165][^ref-302][^ref-1173]

### 지도 위 통합 상태 표시

Open-RMF의 rmf_visualization은 승강기·문의 위치와 상태, 플릿 관리자가 보고한 로봇 현재 위치, 닫힌 차선(회색)과 속도 제한 차선(좁은 폭)을 구분한 주행 그래프, 초록 선으로 그린 로봇 예측 일정 궤적, 층 평면도를 한 화면에 겹쳐 보여 준다. 일정 궤적은 시작 시점과 조회 기간 매개변수로 시간 구간별로 조회한다(확인일 2026-09-30). [사실][^ref-1165]

[VDA 5050](../../glossary/vda-5050.md) 3.0.0 명세는 차량 위치와 계획 경로를 시각화 시스템에 높은 빈도로 보내는 visualization 토픽을, 주문 확인·오류·운용 상태를 담는 state 토픽과 분리해 둔다. state 메시지는 사건이 생길 때 또는 최소 30초 간격으로 보낸다. [사실][^ref-031]

국내 예로(연구 과제 페이지 기준), 현대자동차그룹 로보틱스랩은 통합 관제 시스템 나콘(NARCHON)을 다수 이기종 로봇의 실시간 모니터링, BPMN 2.0 기반 워크플로·시나리오 관리, 이상 탐지·보고가 있는 실시간 대시보드, 엘리베이터·자동문·스크린도어 등 인프라 연동, 실내외 환경의 층별·존별 트래픽 관리를 지원하는 시스템으로 소개한다(확인일 2026-09-30). [추정] 벤더 주장[^ref-1177] 네이버클라우드 ARC brain 사용 가이드(최종 수정 2026-09-17)는 여러 제조사 로봇의 제어와 충돌 방지, 실시간 상태 모니터링과 알림, 실시간 태스크와 운영 이력 조회, 제3자 로봇 등록, 승강기·자동문 연동, 맵 에디터 기반 동선 설정을 서비스 기능으로 든다. [추정] 벤더 주장[^ref-1178]

### 실행 기록 저장과 시간축 재생

Open-RMF의 rmf-web은 배치 전체를 시각화·제어하는 웹 인터페이스 묶음(API 서버·API 클라이언트·대시보드 프레임워크)이며, 기본 설정의 API 서버는 비영속 내부 데이터베이스를 쓰므로 실행 기록을 남기려면 영속 저장소를 따로 설정해야 한다(확인일 2026-09-30). [사실][^ref-302] 재생 도구의 예로 Foxglove 문서는 시간축 막대 탐색, 재생 속도 조절, 구간 자르기, 사건 주석 생성·검색, 반복 재생을 제공하고, 임의 시점으로 이동할 때 토픽마다 가장 최근 메시지를 불러와(lookback) 각 패널이 같은 시점의 상태를 보이게 한다고 설명한다. [추정] 벤더 주장[^ref-1172]

### 설명 가능한 표시

로봇이 왜 그렇게 움직이는지 보여 주는 방법은 경로 계획을 겹치지 않는 시간 구간으로 나눠 보여 주는 설명 가능한 MAPF, 에이전트 투명성 모델, 다중 로봇 인터페이스 설계 요건 같은 연구가 중심이며(8절), 실제 플릿 관제 화면에서의 효과는 확인되지 않았다. [추정][^ref-1173][^ref-477][^ref-1175]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1165]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-302]: Open Robotics (open-rmf/rmf-web), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-09-30
[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1172]: Foxglove, Playback — Foxglove Documentation, 미확인, https://docs.foxglove.dev/docs/visualization/playback, 접근일 2026-09-30
[^ref-1173]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)
[^ref-1175]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-09-30
[^ref-1177]: 현대자동차그룹 로보틱스랩, PROJECTS — Robot Fleet Management (NARCHON), 미확인, https://robotics.hyundai.com/projects/research/view.do?seq=102, 접근일 2026-09-30
[^ref-1178]: 네이버클라우드, ARC brain 개요 - 사용 가이드, 미확인, https://guide.ncloud-docs.com/docs/arc-brain-overview, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-13 | 37. 관제 화면·실행 기록 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-13/pages/topics/2026/2026-09-30-area37-s8.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 대표 연구와 자료"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1173, ref-477, ref-1175]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#8
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 대표 연구와 자료

# 37. 관제 화면·실행 기록 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 설명 가능한 표시와 다중 로봇 관제 인터페이스에 관한 연구는 다음 세 건이 대표적이며, 모두 실험실·알고리즘 수준이다. [추정][^ref-1173][^ref-477][^ref-1175]
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

설명 가능한 표시와 다중 로봇 관제 인터페이스에 관한 연구는 다음 세 건이 대표적이며, 모두 실험실·알고리즘 수준이다. [추정][^ref-1173][^ref-477][^ref-1175]

- Kottinger·Almagor·Lahijanian, Conflict-Based Search for Explainable Multi-Agent Path Finding(ICAPS 2022, arXiv 2022-02) — 선행 연구가 제안한 시간 구간 이미지 설명 개념을 받아 충돌 기반 탐색([CBS](../../glossary/conflict-based-search.md))의 제약 트리와 A* 탐색에 설명 가능성 제약을 더한 XG-CBS를 제안하고 계획 시간과 설명 가능성의 절충을 분석했다. 경로 계획을 운영자가 눈으로 확인하게 나눠 보여 주는 표시의 알고리즘 근거다. [추정][^ref-1173]
- Chen 외, Situation awareness-based agent transparency and human-autonomy teaming effectiveness(Theoretical Issues in Ergonomics Science 19권 3호, 2018) — SAT 모델을 세 연구 프로그램(자율 분대원, 사람과 여러 하위 로봇의 중재자, 계획 추천 에이전트)에 적용했고 공유 이해와 신뢰 보정에 효과적이라고 정리했다. [추정][^ref-477]
- Roldán 외, Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction(Sensors 17권 8호, 2017-07-27) — 드론 2대·지상 로봇 1대의 화재 감시·진압 임무 8개를 운영자 24명이 감독하는 실험에서 기존·예측형 기존·가상현실·예측형 가상현실 인터페이스를 비교했다. 상황 인식은 예측형 가상현실 > 가상현실 > 기존 > 예측형 기존 순, 작업 부하(NASA-TLX)는 가상현실 < 예측형 가상현실 < 기존 < 예측형 기존 순이었고, 가상현실 묶음과 기존 묶음의 상황 인식 차이는 p=0.042였다. 예측 요소의 효과는 유의하지 않았고 기존 인터페이스에서는 부하가 수치상 늘었다. 저자들은 다중 로봇 인터페이스 요건으로 정보량 줄이기, 관련 정보로 주의 유도, 로봇 위치·건강·상태·측정값을 같은 화면에 통합하기, 지도 활용을 들었다. [사실][^ref-1175]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1173]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)
[^ref-1175]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-13 | 37. 관제 화면·실행 기록 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-13/pages/topics/2026/2026-09-30-area37-s4.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 핵심 개념과 용어"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-111, ref-1168, ref-1169, ref-1171, ref-1173, ref-477, ref-1175]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#4
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 핵심 개념과 용어

# 37. 관제 화면·실행 기록 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 관제 화면과 실행 기록에 관련된 개념을 정리한다.
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

관제 화면과 실행 기록에 관련된 개념을 정리한다.

- **작업 상태(Task State)** — [오픈 RMF](../../glossary/open-rmf.md) API 메시지의 작업 상태 스키마는 작업을 12개 상태 값(uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed)으로 나타내고, 처음·현재 추정 소요 시간, 배정 로봇, 완료·진행·대기 단계 목록, 일시정지(interruptions)·취소·강제 종료 요청 정보를 함께 담는다(확인일 2026-09-30). [사실][^ref-111]
- **작업 사건 로그(Task Event Log)** — 같은 스키마 묶음은 로그를 작업·단계(phase)·사건(event) 세 수준으로 나누고, 로그 항목마다 단조 증가 순번(seq), 중요도 tier(uninitialized·info·warning·error), 밀리초 단위 유닉스 시각, 본문 텍스트를 필수로 둔다(확인일 2026-09-30). [사실][^ref-1168][^ref-1169]
- **[MCAP](../../glossary/mcap.md)** — 임의 직렬화 형식의 타임스탬프 발행·구독 메시지를 담는 모듈형 컨테이너 형식이다. 스키마·채널·메시지·청크 레코드와 메시지 색인·청크 색인·요약 레코드로 시각 기준 임의 접근(탐색)을 지원하고 첨부·메타데이터도 담는다. [사실][^ref-1171]
- **상황 인식(Situation Awareness, SA)** — 운영자가 임무 환경의 상황을 파악하는 정도다. Roldán 외는 다중 로봇 관제 인터페이스를 비교하면서 이를 SAGAT 질의 기법으로 측정했다. [사실][^ref-1175]
- **[상황 인식 기반 에이전트 투명성](../../glossary/situation-awareness-based-agent-transparency.md)(SAT)** — 지능형 에이전트와 함께 일하는 운영자의 상황 인식을 돕기 위해 에이전트가 드러낼 정보를 정한 모델이다. [추정][^ref-477]
- **설명 가능한 다중 에이전트 경로 찾기(Explainable MAPF)** — 여러 에이전트의 경로 계획([MAPF](../../glossary/mapf.md))을 궤적이 서로 겹치지 않는 시간 구간 이미지 몇 장으로 나눠 사람이 눈으로 검증하게 하는 문제 설정이며, 이 설명 개념은 선행 연구가 제안했다. [추정][^ref-1173]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-30
[^ref-1168]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-1169]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — log_entry.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json, 접근일 2026-09-30
[^ref-1171]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-09-30
[^ref-1173]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-09-30
[^ref-477]: Chen, J. Y. C., Lakhmani, S. G., Stowers, K., Selkowitz, A. R., Wright, J. L., & Barnes, M. (Theoretical Issues in Ergonomics Science 19(3)), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 2018, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-30 (원문 미열람)
[^ref-1175]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-13 | 37. 관제 화면·실행 기록 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-13/pages/topics/2026/2026-09-30-area37-s10.md

```markdown
---
title: "37. 관제 화면·실행 기록 — 다른 연구영역과의 연결"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 37
related_areas: [11, 13, 15, 17, 18, 20, 21, 22, 27, 31, 33, 36, 38, 39, 43, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1165, ref-111, ref-1168, ref-031, ref-1175, ref-1179]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#10
---

[홈](../../index.md) › [주제](../index.md) › 37. 관제 화면·실행 기록 — 다른 연구영역과의 연결

# 37. 관제 화면·실행 기록 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 화면과 기록은 운영·지도·연동·재현 영역과 두루 이어진다. 아래 연결은 이번 조사 자료를 바탕으로 한 판단이다. [추정][^ref-1165][^ref-111][^ref-1168][^ref-031][^ref-1175][^ref-1179]
- 이 페이지는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 화면과 기록은 운영·지도·연동·재현 영역과 두루 이어진다. 아래 연결은 이번 조사 자료를 바탕으로 한 판단이다. [추정][^ref-1165][^ref-111][^ref-1168][^ref-031][^ref-1175][^ref-1179]

- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 수준별 로그와 알림·이상 탐지가 이 영역의 화면·기록 위에서 동작한다.
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 작업 상태 값, 처음·현재 추정 소요 시간, 로그 항목의 시각 기록이 성과 지표의 원자료가 될 수 있다.
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 층 평면도와 주행 그래프가 관제 화면의 바탕 지도다.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 관제 화면은 현재 상태를 보여 주는 창이며, 상태 모델 자체는 이 영역이 맡는다. 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 구분한다.
- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 실행 기록 재생을 과거 상황 재현으로 넓히는 부분이 이어진다.
- [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) — 대화로 과거 상황을 불러와 재현할 때 이 영역의 실행 기록이 입력이 되며, 짝 엔진은 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현이다.
- [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) — 열린 질문 oq-131(실행 기록을 시나리오 사양으로 바꾸는 형식)이 이 영역과 함께 걸려 있다.
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 경로 계획을 시간 구간으로 나눠 설명하는 표시가 이어진다.
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 에이전트 투명성과 운영자 상황 인식을 공유한다.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — 화면에 올릴 상태 메시지(VDA 5050 visualization·state 토픽)를 받는 통로다.
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 문·승강기 상태 표시가 설비 연동에 기댄다.
- [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) — 기록의 영속 저장과 기록 형식(MCAP)을 다룬다.
- [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) — 배송 이력과 수령 인증이 인계 기록이 된다.
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 5절의 병원 사례가 놓이는 현장 유형이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [17. 작업 대상·자산 식별과 인계 추적](../../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1165]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-09-30
[^ref-111]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-30
[^ref-1168]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-09-30
[^ref-031]: VDA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, main 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1175]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-09-30
[^ref-1179]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-13 | 37. 관제 화면·실행 기록 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1085건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 298개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
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
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
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
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
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
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
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
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
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
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
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
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
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
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [37] 에 걸린 1건 / 전체 232건)

```markdown
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
```

### runs/2026-09-30-13/verification2.json

```json
{
  "run_id": "2026-09-30-13",
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
    "10절(분리 페이지 docs/topics/2026/2026-09-30-area37-s10.md 의 11. 채팅으로 실제 상황 시뮬레이션 재현 항목): '짝 엔진은 33·36번 영역이다'를 '짝 엔진은 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현이다'로 고친다 — 원문 인용이 아닌 서술에서 번호만으로 영역을 부르면 공통 표기 규약 위반이다.",
    "6절(분리 페이지 s6)의 '국내 상용 예로, 현대자동차그룹 로보틱스랩은 …'에서 '상용'을 빼고 '국내 예로(연구 과제 페이지 기준)'처럼 고치고, 9절의 '상용 예로 든 나콘·ARC brain·Foxglove'를 '6절에서 예로 든 나콘·ARC brain·Foxglove'로 고친다 — ref-1177 은 개발 중인 연구 과제 페이지이며(1차 f12 메모) 나콘이 상용 제품이라는 근거가 브리프에 없다. [추정]과 '벤더 주장' 병기는 그대로 둔다.",
    "10절(분리 페이지 s10)의 39. 운영 성과 측정·개선 항목 '작업 상태 값과 추정·실제 소요 시간 기록이 성과 지표의 원자료가 된다'를 '작업 상태 값, 처음·현재 추정 소요 시간, 로그 항목의 시각 기록이 성과 지표의 원자료가 될 수 있다'로 고친다 — f3 은 처음·현재 추정 소요 시간만 담고 '실제 소요 시간' 필드는 브리프에 없다(드리프트).",
    "3절 첫 문장('… 운영자의 개입 판단을 좌우한다. [의견]'): 누구의 의견인지 밝혀 '[의견] 구축자 의견'으로 적거나, '좌우한다'는 단정을 빼고 태그 없는 연결 문장('관제 화면과 실행 기록은 운영자가 여러 제조사 로봇의 일을 지금 보고 나중에 되짚는 창구다.')으로 바꾼다 — 이 [의견]을 뒷받침하는 finding 이 없고 [의견]은 주체를 밝혀야 한다.",
    "4절 도입 문장('관제 화면과 실행 기록을 설계할 때는 다음 개념이 기본 어휘가 된다. [사실][^ref-111][^ref-1168][^ref-1171]', 분리 페이지 s4 의 세 줄 요약·본문 첫 문장 포함)의 태그를 [추정]으로 바꾸거나 태그·각주 없는 연결 문장으로 둔다 — '기본 어휘가 된다'는 판단이며 인용한 세 출처가 그렇게 말하지 않고, 아래 목록에는 [추정] 항목(상황 인식 기반 에이전트 투명성, 설명 가능한 MAPF)도 섞여 있다.",
    "reference_updates 의 ref-031 summary 에서 '이전 실행 2026-09-30-10 의 ref-1079 와 같은 URL 이며 참고문헌 목록에 ref-1079 가 없어 새 id 로 낸다.'를 지우고, 필요하면 '이전 실행 2026-09-30-10 의 ref-1079 와 같은 URL 이다.'만 남긴다. fixes_applied 의 ref-031 항목도 '각주·sources 에 ref-1170 을 쓰고'를 실제로 쓴 id(ref-031)로 고친다 — 페이지는 새 id 가 아니라 ref-031 을 쓰므로 summary 와 보고 문구가 페이지와 어긋나며, summary 는 참고문헌 페이지에 게시된다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 15건, 미확인 4건(f8·f9·f12·f16), 교차 확인 0건. 강등: f8 사실 → 추정(설명 개념과 NP-난해성을 선행 연구에 잘못 귀속), f9 사실 → 추정(열람 가능한 초록에서 수행 향상 결과 미확인), f12·f16은 이미 추정이라 뒷받침되지 않는 구절을 삭제. 원문 미열람 출처: ref-477. 주의: 핵심 내용은 모두 단일 출처이고 절반가량이 종합 추정이다. 관제 화면 요소는 Open-RMF·VDA 5050·MCAP 같은 공개 구현·명세 문서 기준이며, 설명 가능한 표시의 효과는 실험실·알고리즘 연구에 한정된다. 현장 사례는 병원 1건(협약 단계 보도)뿐이다. Roldán 외의 SAGAT·NASA-TLX 수치는 검증 열람에서 재현하지 못해 순서와 유의성만 싣는다. 나콘·ARC brain·Foxglove 기능은 벤더 주장이다. ref-031은 이전 실행 ref-1079와 같은 URL이다. 정정 요청 없음. oq-131은 미해결 유지. / 2차 수정 후 재검증. 1차 수정 지시 15건은 모두 이행됐다(f8·f9 강등과 재서술, ref-477 원문 미열람 표시, f10 수치 제외, f12 재서술과 상업 시설 제외, 병원 사례의 미확인 칸, f16 재서술, 64. 상업 시설 연결 삭제, 벤더 주장 병기, 용어 정의 축약, ref-1179 제목, oq-131 유지). 드리프트 2건(나콘을 '상용 예'로 부름, 39. 운영 성과 측정·개선 연결의 '실제 소요 시간')과 표기 4건(번호만 쓴 '33·36번', 주체 없는 [의견], 판단 문장의 [사실] 태그, ref-031 참고문헌 요약의 '새 id' 문구)을 국소 수정하도록 돌려보냈다. [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 통과 기준). 자동 분리된 주제 페이지 4건은 원 절 내용을 그대로 옮긴 것으로 확인했다.",
  "retry_reason": null
}
```
