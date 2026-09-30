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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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
        "ref-1166"
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
        "ref-1167"
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
        "ref-1170"
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
        "ref-1174"
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
        "ref-1167",
        "ref-1168",
        "ref-1170",
        "ref-1173",
        "ref-1174",
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
        "ref-1174",
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
        "ref-1167",
        "ref-1168",
        "ref-1166",
        "ref-1171",
        "ref-1172",
        "ref-1173",
        "ref-1174"
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
        "ref-1170",
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
        "ref-1166",
        "ref-1167",
        "ref-1168",
        "ref-1170",
        "ref-1171",
        "ref-1172",
        "ref-1173",
        "ref-1174",
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
      "id": "ref-1166",
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
      "id": "ref-1167",
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
      "id": "ref-1170",
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
      "id": "ref-1174",
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
      "f9 SAT 모델 논문(ref-1174): 출판사·DTIC·ADS 페이지가 403/405 로 열리지 않아 검색 결과 요약 범위로만 서술했고, SAT 세 수준의 정의는 출처 귀속이 불분명해 넣지 않음(용어집의 기존 SAT 항목 참조)",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-1165~ref-1179, 예약 구간 안)로 출처 상한에 도달해 ISO 11064, RCLL 객체 중심 이벤트 로그, 물류창고·제조 공장 관제 화면 사례를 더 넣지 못했다. 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건이고 전체 목록 id 를 받지 못함. VDA 5050·MCAP 이 기존 목록에 같은 URL 로 있으면 퍼블리셔가 합친다). 원문 열람: 14건 열었고(github_raw 6건, webfetch 8건) SAT 논문(ref-1174)만 열지 못해 source_unopened 로 표시했다. 논문은 Roldán 외(PMC 본문) 외에 Kottinger 외는 초록만 봤다. 교차 확인 0건: 핵심 내용이 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더 문서 기능 주장(f7·f12·f13)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가)에는 f15 로 답했고 결론은 '무엇을 보여 주는 요소는 공개 구현·표준에 있으나 왜를 보여 주는 설명 표시는 실험실 연구 수준이며 현장 평가 자료를 찾지 못했다'는 추정이다. 현장 유형 사례는 병원(f14, 협약 단계)·상업 시설(f12, 벤더 주장)뿐이며 물류창고·제조 공장·가정·실외는 찾지 못했다. 국내 자료는 현대차 로보틱스랩(ref-1177)·네이버클라우드(ref-1178)·아주경제(ref-1179) 3건이다. oq-131 은 근거를 찾지 못해 해결 제안하지 않았다. 용어집에 이미 있는 백 파일·MCAP·상황 인식 기반 에이전트 투명성·감사 추적·관측성·오픈 RMF·VDA 5050 은 후보로 내지 않았다. 페이지 제안은 대상 영역 갱신 1건이고 36·38번 반영은 다음 실행 후보로 적었다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
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

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md (요약)

```markdown
# 39. 운영 성과 측정·개선

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 성과 측정**: 처리량·완료 시간·가동률·대기 시간·에너지 같은 지표를 정의하고 측정한다
- **로봇 성과와 업무 성과 구분**: 로봇 가동률이 올라간 것이 실제 업무 성과(처리량·서비스 시간·비용)로 이어졌는지 나눠 본다
- **운영 개선**: 측정 결과로 운영 정책·배치·절차를 고치고 효과를 다시 잰다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 4번 영역 ‘성과·경제성·프로세스 개선’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [옛 분류원문]

> 옛 질문: 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [옛 분류원문]

## 2. 핵심 질문

로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? [분류원문]
```

### docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md (요약)

```markdown
# 40. 운영 절차·요청 창구

소속 대분류: J. 현장 운영·관제 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

운영 절차·교대, 현장 사용자의 요청 창구 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 절차·교대**: 운영 표준 절차, 교대 인수인계, 역할을 정한다
- **현장 사용자 요청 창구**: 간호사·객실 직원·거주자처럼 비전문 사용자가 호출 버튼·앱·단말로 일을 요청한다

## 2. 핵심 질문

현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1074건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 293개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
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

### docs/open-questions.md (요약: 대상 영역 [37] 에 걸린 1건 / 전체 228건)

```markdown
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
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

### runs/2026-09-30-12/research.md

```markdown
# 리서치 브리프 2026-09-30-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-12 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 33. 시나리오 모델·편집 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 시나리오 기술 언어, 정적 환경과 동적 내용의 분리, 매개변수화·카탈로그, 장애 주입 선언, 반증 기반 시험 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(호텔·공항)·병원(클리닉)·실외(캠퍼스)·가정(가정 활동)·제조 공장(배터리 생산) 시나리오 예제와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 확률적 시나리오 언어, 건물 주석 편집기, 행동 트리·BPMN 같은 미션 형식, LLM 기반 환경·시나리오 생성 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ASAM OpenSCENARIO, SDFormat, VDMA LIF, Open-RMF rmf_demos·traffic-editor, BEHAVIOR-1K·BDDL, NIST ARIAC, MovingAI MAPF 벤치마크, Groot2 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131·oq-135 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]
2. 로봇 시뮬레이션·자율 시스템 시험에서 쓰는 시나리오 기술 형식·언어는 무엇이며 환경·개체·작업·사건·장애를 어떻게 나누어 담고 판(버전)을 어떻게 관리하는가? (섹션 4·6·7 겨냥)
3. 현장 유형별(호텔·병원·공장·가정·실외·물류창고) 시나리오 예제·템플릿 라이브러리로 공개된 것은 무엇이고 각각 무엇을 담는가? (섹션 5·7 겨냥, 한국 자료 우선)
4. 사람이 화면에서 시나리오·워크플로·미션을 그리고 고치는 편집기와 미션 기술 형식(행동 트리·상태 기계·BPMN 등)은 무엇이며 비교 연구는 무엇을 말하는가? (섹션 6·7·8 겨냥)
5. 언어 모델로 시뮬레이션 환경·시나리오를 자동 생성하는 연구는 무엇을 입력으로 받아 무엇을 만들고 어떻게 평가했는가? (섹션 6·8 겨냥, 9. 채팅으로 시나리오 구성과의 연결)
6. oq-131 플릿 관제 실행 기록을 시나리오 사양으로 바꾸는 공개 형식·변환 규칙, oq-135 시나리오 구성 시 되물어야 할 항목의 표준 목록이 있는가? (섹션 11 겨냥)
7. 33. 시나리오 모델·편집에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·로봇 제조사·설비 쪽에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Vin 외의 Scenic 3.0(CAV 2023)은 자율 시스템·로봇의 환경을 모델링하는 확률적 프로그래밍 언어 Scenic 에 3차원 기하, 가림을 고려한 광선 추적 기반 가시성 판정을 갖춘 정밀 형상 모델, 선형 시간 논리(LTL)로 쓰는 시간 요구사항을 더해 반증(falsification) 기반 시험에 쓸 수 있게 했다. | ref-1135 | 아니오 | medium | 2023-07 | — | — |
| f2 | [사실] | ASAM OpenSCENARIO XML 은 주행·교통 시뮬레이터의 동적 내용(차량·보행자 등 여러 개체의 동기화된 기동)을 계층 구조의 XML 파일(.xosc)로 기술하는 표준으로, 2026-05-19 에 1.4.0 판이 나왔고, 기동·동작·궤적을 카탈로그로 묶고 시나리오 전체를 매개변수화해 시나리오 파일을 대량으로 만들지 않고도 시험을 자동화할 수 있게 한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f3 | [사실] | ASAM 은 도로망은 OpenDRIVE, 노면 형상은 OpenCRG 로 따로 기술하고 OpenSCENARIO XML 은 그 위의 동적 내용만 담게 나누며, 병행 표준 OpenSCENARIO DSL 은 대규모 검증용, XML 은 예측 가능한 정밀 시나리오용으로 역할을 구분한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f4 | [사실] | Open-RMF 의 rmf_demos 는 호텔 월드로 로비와 객실 2개 층, 승강기 2대, 여러 문, 로봇 플릿 3개(로봇 4대)가 층을 오가며 순찰(loop)·청소 작업을 하는 다중 플릿 시나리오를 예제로 제공한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 상업 시설 / 수행 자원 | — |
| f5 | [사실] | rmf_demos 의 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 여러 플릿과 설비·이용자의 상호작용을 보이며, 선택적으로 군중 시뮬레이션을 켜고 사람이 직접 모는 읽기 전용(read_only) 카트를 함께 두고 순찰·배송·청소 작업을 실행한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 상업 시설 / 제약 | — |
| f6 | [사실] | rmf_demos 의 클리닉 월드는 승강기 2대가 있는 2개 층 시설에서 역할이 다른 로봇 플릿 2개가 층을 오가며 간호 스테이션 사이를 순찰하는 병원형 시나리오 예제다. | ref-1136 | 아니오 | medium | 2026-09-30 | 병원 / 제약 | — |
| f7 | [사실] | rmf_demos 의 캠퍼스 월드는 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스에서 여러 배송 로봇이 장거리 순찰을 하는 실외 시나리오 예제이고, 제조·물류 월드는 컨베이어·고정 매니퓰레이터 작업셀과 여러 AMR 플릿의 연동을 영상으로만 보인다. | ref-1136 | 아니오 | medium | 2026-09-30 | 실외 / 작업 대상 | — |
| f8 | [사실] | rmf_demos 에서 시나리오는 월드(건물 구성·차선·승강기·문·충전 위치)를 띄운 뒤 dispatch_patrol·dispatch_delivery·dispatch_clean 같은 명령으로 작업을 따로 넣는 구조이며, 디스패처가 플릿 어댑터들 사이의 작업 입찰을 조율한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f9 | [사실] | Open-RMF 의 traffic-editor 는 시설 지도 위에 벽·문(여닫이·미닫이·양문)·층·승강기, 최대 9개 그래프의 교통 차선, 충전·주차·대기·도킹·시뮬레이션 로봇 생성 위치 같은 웨이포인트 속성, 층 정렬용 기준점을 그려 넣는 GUI 편집기로, 결과를 .building.yaml 파일로 저장하고 building_map_generator 가 이를 물리 시뮬레이션 월드로 자동 생성한다. | ref-1137 | 아니오 | medium | 2026-09-30 | — | — |
| f10 | [사실] | Stanford 등의 BEHAVIOR-1K(arXiv 2403.09227, 예비판 CoRL 2022)는 '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(BDDL)로 형식 명세하고, 주택·정원·식당·사무실 등 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상, 강체·변형체·액체를 다루는 OmniGibson 시뮬레이터 위에 구현한 활동 라이브러리다. | ref-1138 | 아니오 | medium | 2024-03 | 가정 / 작업 대상 | — |
| f11 | [사실] | NIST ARIAC 문서의 시나리오는 전기차 배터리 생산 시설로, 배터리 셀 4개를 트레이에 담는 키팅과 셀 4개와 상하 케이스로 모듈을 조립하는 두 작업을 주문으로 받고, 우선순위가 높은 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않게 정한다. | ref-1140 | 아니오 | medium | 2026-09-30 | 제조 공장 / 작업 대상 | — |
| f12 | [사실] | NIST ARIAC 는 컨베이어 고장(START_TIME·DURATION), 전압 시험기 고장(시작·지속·대상 TESTER), 진공 그리퍼 파지 실패(TOOL·몇 번째 파지인지 GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID) 네 가지 민첩성 과제를 매개변수로 선언해, 장애와 긴급 요청을 시각 또는 발생 횟수 조건으로 시나리오에 주입한다. | ref-1139 | 아니오 | medium | 2026-09-30 | 제조 공장 / 예외·성과 | — |
| f13 | [사실] | Kästner 외의 Arena-Bench(RA-L 2022)는 동적 환경의 시나리오·월드 생성 도구와 평가 지표를 갖춘 벤치마크 모음으로, 3차원 환경에서 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오로 비교하고 실물 로봇 배치까지 보였다. | ref-1142 | 아니오 | medium | 2022-06 | — | — |
| f14 | [사실] | Shcherbyna 외의 Arena 4.0(arXiv 2409.12471)은 대규모 언어 모델과 확산 모델로 텍스트 설명이나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고, 의미 주석이 달린 3D 자산 데이터베이스로 객체를 배치하며, 사용자 연구에서 이전 판보다 사용성·효율이 나아졌다고 보고했다. | ref-1143 | 아니오 | medium | 2024-09 | — | — |
| f15 | [사실] | Yang 외의 Holodeck(CVPR 2024)은 GPT-4 가 텍스트 설명에서 평면 배치·재질·문과 창을 정하고 공간 관계 제약을 만들어 최적화로 Objaverse 3D 자산을 배치하는 방식으로 오락실·스파·박물관 같은 상호작용 가능한 환경을 자동 생성하며, 주거 장면에서 평가자가 절차적 생성 기준선보다 선호했고 사람이 만든 데이터 없이 음악실·어린이집 같은 새 장면의 주행 학습에 썼다. | ref-1144 | 아니오 | medium | 2023-12 | — | — |
| f16 | [추정] | 행동 트리 편집기 Groot2 는 끌어놓기로 트리를 만들며 XML 을 실시간으로 미리 보고, 실행 중인 BehaviorTree.CPP 실행기에 붙어 상태를 보여 주고 전이를 로그로 기록해 속도를 바꿔 재생하며, 유료판에서 블랙보드 표시·중단점·장애 주입을 제공한다고 밝힌다. | ref-1145 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f17 | [사실] | Filippone·Pettinari·Pelliccione(IEEE TSE, arXiv 2603.15427)는 단일·다중 로봇 미션 기술 형식으로 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·표현력·도구 지원 측면에서 비교하며, 미션을 명세하는 표준이나 널리 받아들여진 형식이 없고 미션은 로봇 전문가가 아닌 도메인 전문가가 정의하는 경우가 많다고 지적했다. | ref-1146 | 아니오 | medium | 2026-03 | — | — |
| f18 | [사실] | Moving AI 연구실의 MAPF 벤치마크는 도시·게임·창고형·무작위·미로·방 등 격자 지도 36개마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 두어 모두 1,800개의 시나리오 파일을 공개한 재사용 가능한 시나리오 라이브러리다. | ref-1147 | 아니오 | medium | 2026-09-30 | — | — |
| f19 | [사실] | SDFormat(Simulation Description Format)은 로봇 시뮬레이터·시각화·제어용으로 로봇(기구학·동역학·센서)과 환경(조명·지형·OpenStreetMap 도로·3D 모델), 물리 설정을 기술하는 XML 형식으로, Gazebo 에서 시작했고 Open Source Robotics Foundation 이 Apache 2.0 으로 관리한다. | ref-1148 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합업체가 주행 경로 레이아웃(간선·노드·스테이션)을 제3자 상위 관제 시스템에 처음 넘길 때 쓰는 비구속적 교환 형식이며, VDA 5050 인터페이스 정의의 영향을 받아 만들어졌다. | ref-1149 | 아니오 | medium | 2023-09 | — | — |
| f21 | [추정] | 확인한 형식들은 공통으로 정적 환경(SDFormat 월드, Open-RMF .building.yaml, VDMA LIF 레이아웃, OpenDRIVE 도로망)과 동적 내용(작업 명령, OpenSCENARIO 스토리보드, ARIAC 주문·장애 과제, BDDL 활동)을 나누어 기술하며, 형식 자체의 판(OpenSCENARIO XML 1.4.0, LIF 1.0.0)은 두지만 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 자료에서 찾지 못했다. | ref-1148, ref-1137, ref-1149, ref-1141, ref-1136, ref-1139, ref-1138 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 공개 형식은 분야별로 나뉘어(자율주행 OpenSCENARIO, 가정 활동 BDDL, 시설 다중 로봇 Open-RMF 건물 파일과 작업 명령, 제조 ARIAC 과제 설정, MAPF .scen) 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 찾지 못했고 미션 기술에도 표준이 없으며(f17), 재사용은 매개변수화·카탈로그(f2), 확률 분포 표본 추출(f1), 현장 유형별 예제 월드(f4~f7), 대규모 활동·시나리오 라이브러리(f10·f18), 언어 모델 생성(f14·f15)으로 이루어지는 것으로 보인다. | ref-1141, ref-1138, ref-1136, ref-1139, ref-1147, ref-1146, ref-1135, ref-1143, ref-1144 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 계획기·정책을 같은 조건에서 비교하려면 고정된 시나리오 파일이 있어야 하고(f13·f18), 장애·긴급 요청을 시나리오에 선언해야 예외 대응 시험을 반복할 수 있으며(f12), 매개변수화가 없으면 조건별 시나리오 파일이 불어나고(f2), 비전문가가 미션과 환경을 정의해야 하는데 공통 형식이 없기 때문이다(f17). | ref-1142, ref-1147, ref-1139, ref-1141, ref-1146 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 확인한 자료를 종합하면 33. 시나리오 모델·편집에서 ROP가 직접 맡을 범위는 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 버전 있는 시나리오 모델(f8·f12·f21), 현장 유형별 예제 라이브러리(f4~f7), 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택(f9·f16·f17), 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환(f9·f19)으로 보인다. | ref-1136, ref-1139, ref-1137, ref-1145, ref-1146, ref-1148 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 로봇 기구학·센서 모델(SDFormat 로봇 기술, f19)은 시뮬레이터·로봇 제조사 쪽에, 컨베이어·작업셀 같은 설비 제어(f7·f12)는 설비 쪽에, 도로 교통 시나리오 표준(f2·f3)은 자율주행 분야에 속하므로, ROP 는 이들을 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. | ref-1148, ref-1136, ref-1139, ref-1141 | 아니오 | low | 2026-09-30 | — | — |
| f26 | [추정] | 이 영역은 시나리오를 대화로 만드는 9. 채팅으로 시나리오 구성(f14·f15)과 11. 채팅으로 실제 상황 시뮬레이션 재현, 시나리오를 실행하는 34. 시뮬레이션·예측용 디지털 트윈(f19), 기록 재생·재현의 36. 가상 시운전·실제 상황 재현(f16), 규모 산정의 35. 처리능력·규모·배치 설계, 건물·레이아웃 주석의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f9·f20), 군중·보행자의 19. 사람·보행자 모델(f5·f14), 승강기 연동의 22. 설비·건물 시스템 연동(f4·f6), 미션 형식의 24. 작업·워크플로 모델링(f17), 장애 주입의 32. 예외 복구·재계획·업무 연속성(f12), 경로 시나리오의 27. 다중 로봇 경로·교통 관리 — MAPF(f18), 언어 모델 생성의 44. 로봇 기반 모델·언어 모델 계획(f15), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f13·f18), 적용 현장인 62. 제조 공장(f11·f12)·63. 병원·의료(f6)·64. 상업 시설(f4·f5)·65. 가정·공동주택(f10)·66. 실외(f7)와 이어진다. | ref-1143, ref-1144, ref-1148, ref-1145, ref-1137, ref-1149, ref-1136, ref-1146, ref-1139, ref-1147, ref-1135, ref-1142, ref-1140, ref-1138 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1135 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.03325 | 아니오 |
| ref-1136 | Open-RMF (open-rmf/rmf_demos) | rmf_demos — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-1137 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Traffic Editor | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-1138 | Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2403.09227 | 아니오 |
| ref-1139 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Challenges | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-1140 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 아니오 |
| ref-1141 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | 표준 | high | 2026-09-30 | https://www.asam.net/standards/detail/openscenario-xml/ | 아니오 |
| ref-1142 | Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv) | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2206.05728 | 아니오 |
| ref-1143 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2409.12471 | 아니오 |
| ref-1144 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2312.09067 | 아니오 |
| ref-1145 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.behaviortree.dev/groot/ | 아니오 |
| ref-1146 | Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-1147 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://movingai.com/benchmarks/mapf/index.html | 아니오 |
| ref-1148 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | 오픈소스 문서 | high | 2026-09-30 | http://sdformat.org/ | 아니오 |
| ref-1149 | VDMA (Intralogistics-2X-LIF) | Layout Interchange Format (LIF) — README | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f23(왜 중요한가), f22(핵심 질문 답, 추정) / 섹션 4: 확률적 시나리오 언어·반증 f1, 매개변수화·카탈로그 f2, 정적 환경과 동적 내용 분리 f3·f21, 장애 주입 선언 f12, 미션 기술 형식 f17 / 섹션 5: 상업 시설 — f4(호텔, 수행 자원)·f5(공항 터미널, 제약: 군중·수동 카트), 병원 — f6(클리닉, 제약: 층간 승강기), 실외 — f7(캠퍼스, 작업 대상: WGS84 공간), 가정 — f10(일상 활동 라이브러리), 제조 공장 — f11(배터리 생산 작업 대상)·f12(장애 주입 예외·성과). 물류창고는 f18 격자 지도와 f20 레이아웃 형식뿐이고 실제 현장 사례는 찾지 못함을 명시 / 섹션 6: 확률적 언어 f1, 건물 주석 편집 f9, 월드+작업 명령 구조 f8, 미션 형식 비교 f17, 행동 트리 편집·재생 f16(벤더 주장 병기), 언어 모델 기반 환경 생성 f14·f15 / 섹션 7: ASAM OpenSCENARIO f2·f3, SDFormat f19, VDMA LIF f20, Open-RMF rmf_demos·traffic-editor f4~f9, BEHAVIOR-1K·BDDL f10, NIST ARIAC f11·f12, MovingAI MAPF f18, Arena f13·f14, Groot2 f16 / 섹션 8: f1·f10·f13·f14·f15·f17 / 섹션 9: f24(직접 범위), f25(연계 대상) / 섹션 10: f26 — 9, 11, 14, 15, 19, 22, 24, 27, 32, 34, 35, 36, 44, 54, 62, 63, 64, 65, 66 / 섹션 11: 기존 oq-131·oq-135(미해결)와 open_questions_new 4건. 다음 실행 후보: 9. 채팅으로 시나리오 구성 페이지에 f14·f15, 36. 가상 시운전·실제 상황 재현 페이지에 f12·f16 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 오픈시나리오 | ASAM OpenSCENARIO | ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다. |
| 행동 영역 정의 언어 | Behavior Domain Definition Language (BDDL) | BEHAVIOR 벤치마크가 가정 활동을 시뮬레이션된 물리 상태와 연결된 논리 술어로 형식 명세하는 데 쓰는 도메인 특화 언어다. |
| 시뮬레이션 기술 형식 | Simulation Description Format (SDFormat) | Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다. |
| 반증 기반 시험 | Falsification | 시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다. |

## 열린 질문

새로 생긴 질문:

- 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? | 관련 영역: 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f21 | 종류: 일반
- 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반
- ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 65. 가정·공동주택 | 근거: f4 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f10 BDDL 이 활동을 초기 조건·목표 조건 쌍으로 정의한다는 세부 구조는 검색 요약에만 있어 claim 에 넣지 않음
    - f1 Scenic 이 한 프로그램에서 표본 추출로 여러 장면을 만든다는 설명과 로봇 적용 사례(암석 지대)는 검색 요약에만 있어 넣지 않음
    - f15 Holodeck 3D 자산 수(약 5만 개)는 검색 요약에만 있어 넣지 않음
    - f13 Arena 시나리오 편집기의 끌어놓기 배치·보행자 웨이포인트 기능은 검색 요약에만 있어 넣지 않음
    - f16 Groot2 기능은 제품 페이지뿐이며 독립 출처로 교차 확인하지 못함
    - f2 OpenSCENARIO XML 1.4.0 명세 본문은 열지 않았고 공식 소개 페이지 기준
    - oq-131 미해결: 플릿 실행 기록을 시나리오로 바꾸는 공개 형식은 찾지 못함(찾은 JoyAI-Sim arXiv 2606.16776 은 탁상 조작 과제 재구성이라 제외)
    - oq-135 미해결: 시나리오 구성 시 되물을 항목의 표준 목록은 이번 조사에서 찾지 못함(검색하지 못함)
    - 물류창고 실제 현장의 시나리오 예제·템플릿 사례와 국내 자료는 찾지 못함
    - Bourr·Tiezzi 의 BPMN→X-Klaim 변환(arXiv 2311.04126)은 철회된 논문이라 제외
    - Moskovskaya 외 안내 로봇 LLM 시나리오 생성(arXiv 2509.10317)은 대화 행동 대본 의미의 시나리오라 제외
- 범위 경계 위반 의심:
    - f19: SDFormat 의 로봇 기구학·센서 기술은 로봇 제조사·시뮬레이터 쪽 내용이므로 형식 참조 근거로만 쓰고 f25 에서 연계 대상으로 구분함
    - f2·f3: OpenSCENARIO 는 자율주행 도로 시나리오 표준이므로 ROP 직접 범위가 아니라 참조 설계 사례로만 제안함
    - f7·f12: 컨베이어·작업셀 설비 제어는 설비 쪽 연계 대상이며 시나리오에 장애를 선언하는 방식만 근거로 씀
    - f8·f21: 시나리오는 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 섞지 않음
    - f14·f15: 언어 모델 기반 생성은 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획)과 9. 채팅으로 시나리오 구성에도 연결하도록 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1135~ref-1149, 예약 구간 안)로 출처 상한에 도달해 물류창고 실제 현장 시나리오와 국내 자료, oq-135 조사를 더 하지 못했다. 재사용 출처 없음: NIST ARIAC 는 공통 규칙상 ref-008 이지만 입력 참고문헌 요약에 ref-008 의 등록 URL·제목이 없어 이번에 연 개별 문서 페이지(challenges·scenario)를 새 id(ref-1139·ref-1140)로 적었다. 같은 URL 이면 퍼블리셔가 합치고, 다르면 ref-008 과의 관계를 검증에서 확인해 주기 바란다. 원문 열람: 15건 모두 열었다(webfetch 10건, github_raw 5건). 논문은 모두 초록 페이지 기준이다. VDMA LIF 지침 PDF 는 본문 추출에 실패해 공식 저장소 README 로 대신했다. 교차 확인 0건: 각 형식·사례가 한 출처에만 기술되어 있어 finding 신뢰도는 medium 이하로 두었다. Groot2 기능(f16)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에는 f22 로 답했고 결론은 '공개 형식은 분야별로 나뉘고 공통 표준은 없으며, 재사용은 매개변수화·표본 추출·예제 라이브러리·언어 모델 생성으로 이루어진다'는 추정이다. 현장 유형 사례는 상업 시설(f4·f5)·병원(f6)·실외(f7)·가정(f10)·제조 공장(f11·f12)이며 물류창고는 격자 지도 벤치마크(f18)와 레이아웃 교환 형식(f20)만 있고 현장 사례는 찾지 못했다. 국내 자료는 한국어 검색 2회에서 이 영역에 맞는 것을 찾지 못했다(찾은 한국지능시스템학회 시뮬레이터 리뷰는 시나리오 정의를 다루지 않아 제외). 기존 열린 질문 oq-131·oq-135 는 해결 근거가 없어 해결 제안하지 않았다. 용어집에 이미 있는 행동 트리·BPMN·HTN·레이아웃 교환 형식·가상 시운전·시나리오 재구성·미션 명세 패턴은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-10/research.md

```markdown
# 리서치 브리프 2026-09-30-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-10 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 49. 사람 근접 안전 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 속도·분리 감시(SSM), 동력·힘 제한(PFL), 보호 분리 거리, 운용 구역, 속도 제한·진입 금지 구역, 움직임 지도(Maps of Dynamics) 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·실외·제조 공장 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 인지형 배정·교통 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙 제223조, VDA 5050 구역, Nav2 Collision Monitor 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
2. 로봇과 사람 사이의 분리 거리는 표준에서 어떤 변수(사람 속도, 반응 시간, 정지 거리, 측정 불확실도)로 계산하며, 실제 구현에서 어떤 한계가 보고되는가? (섹션 4·6·8 겨냥)
3. 이동 로봇·협동로봇·실외 로봇의 사람 근접 안전을 다루는 국내외 표준·법규·인증(ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙)은 구역·속도·감지·정지를 어떻게 규정하는가? (섹션 7 겨냥, 한국 자료 우선)
4. 구역별 속도 제한과 진입 금지를 플릿 관제 수준에서 표현·전달하는 인터페이스와 오픈소스(VDA 5050 구역, Nav2 Collision Monitor 등)는 무엇이며 안전 기능으로 인정되는가? (섹션 6·7·9 겨냥)
5. 물류창고·병원·실외·상업 시설 같은 현장에서 사람 근접 시 감속·정지·양보를 적용한 사례와 그 속도 기준은 무엇인가? (섹션 5 겨냥)
6. 안전 거리와 별개로 사람이 편안하게 느끼는 거리·속도, 사람의 움직임을 배정·교통에 반영하는 연구는 무엇을 보고하는가? (섹션 6·8 겨냥)
7. 사람 근접 안전에서 ROP가 직접 맡을 것과 로봇 제조사·시스템 통합자·설비에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Marvel·Norcross(NIST, Robotics and Computer-Integrated Manufacturing)는 ISO/TS 15066 의 속도·분리 감시(SSM)에서 보호 분리 거리가 사람 이동 속도, 로봇 반응 시간, 로봇 정지 시간(정지 거리), 침입 거리, 로봇·사람 위치 측정 불확실도로 계산되며, 분리 거리가 이 값 이하가 되면 안전 감시 정지를 건다고 정리했다. | ref-1075 | 아니오 | medium | 2016 | 제약 | — |
| f2 | [사실] | 같은 연구는 사람 속도로 ISO 13855 의 1,600 mm/s(최악 조건 2,000 mm/s), 침입 거리로 ISO 13855 기준 850~1,200 mm 를 들고, NIST 시험에서 레일 장착 로봇의 반응 시간을 약 0.113초로 측정했다고 보고했다. | ref-1075 | 아니오 | medium | 2016 | 제약 | — |
| f3 | [사실] | 같은 연구는 SSM 식이 속도의 방향을 무시하고 크기만 써서 멀어지는 로봇도 불필요한 정지를 일으킬 수 있고, 센서 잡음이 속도 추정 오차를 키우며, 갱신 주기가 낮을수록 로봇 평균 속도가 떨어지고, 보호 거리는 주로 로봇 제동 거리와 반응 시간이 좌우한다고 보고했다. | ref-1075 | 아니오 | medium | 2016 | 예외·성과 | — |
| f4 | [사실] | Hartmann 외(arXiv 2602.17822, 2026-02)는 ISO 10218-1/2 의 2025년 개정판이 협동 작업 기술 시방서 ISO/TS 15066 을 선택적 지침에서 규범적 요구로 본문에 통합하고, 로봇·협동 적용의 새 분류와 사이버보안 요구를 더했다고 분석했다. | ref-1076 | 아니오 | medium | 2026-02 | — | — |
| f5 | [사실] | 국내 산업안전보건기준에 관한 규칙 제223조는 산업용 로봇 운전 중 위험 방지를 위해 높이 1.8미터 이상의 울타리와 안전매트 설치를 기본으로 하되 2016년부터 한국산업표준 등 안전기준에 맞는 협동 운전 로봇은 울타리 설치를 면제하며, 협동 작업 방식은 속도·분리 감시(SSM), 핸드 가이딩(HGC), 동력·힘 제한(PFL)으로 나뉜다고 지디넷코리아가 전했다. | ref-1082 | 아니오 | low | 2024-03 | 제약 | — |
| f6 | [추정] | ISO 3691-4:2023(무인 산업용 트럭과 그 시스템의 안전 요구·검증)은 사람이 있는 운용 구역에서는 인력 감지를 요구하고, 훈련된 인원만 들어가는 제한 구역과 울타리 등으로 사람을 배제한 구역을 구분해 구역에 따라 보호 조치를 달리하는 것으로 알려져 있다. | ref-1077 | 아니오 | low | 2023 | 제약 | 원문 미열람 |
| f7 | [추정] | 같은 표준은 인력 감지를 끄거나 완전히 작동하지 않는 상황(예: 도킹)에서 속도를 0.3 m/s 이하로 제한하고, 인력 감지 성능을 서 있는 사람(지름 200 mm·높이 600 mm 원통)과 누운 사람(지름 70 mm·길이 400 mm 원통) 시험편으로 확인하는 것으로 알려져 있다. | ref-1077 | 아니오 | low | 2023 | 제약 | 원문 미열람 |
| f8 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR)을 특정 적용과 현장에 맞춰 통합·배치할 때의 안전 요구를 다루며, 배치 시스템의 위험성 평가는 IMR 시스템 통합자가 수행하도록 하고 모바일 매니퓰레이터와 잔여 위험, 최종 사용자 정보·교육을 포함한다고 The Robot Report 가 전했다. | ref-1088 | 아니오 | low | 2023-10-26 | — | — |
| f9 | [사실] | 한국로봇산업진흥원의 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거해 배송 등 목적의 자율주행·원격제어 로봇과 관제장치의 조합을 대상으로 최고 속도 15 km/h 이하·최대 질량 500 kg 이하를 요구하고, 주변 인식·비상정지·횡단보도 통행·관제장치 등을 심사하며 2년 주기 정기점검을 둔다. | ref-1080, ref-1081 | 예 | high | 2026-09-30 | 실외 / 제약 | — |
| f10 | [사실] | 지디넷코리아(2023-07-28)는 산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준이 로봇과 적재물 질량 합계에 따라 최고 속도를 230 kg 초과 5 km/h, 100 kg 초과 10 km/h, 그 이하 15 km/h 로 나누고, 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단하게 하며 심사 항목을 16가지로 두었다고 전했다. | ref-1081 | 아니오 | medium | 2023-07-28 | 실외 / 제약 | — |
| f11 | [사실] | VDA 5050 3.0.0 은 플릿 관제가 이동 로봇에 전달하는 구역 유형으로 진입 금지(BLOCKED), 플릿 관제 승인 후 진입(RELEASE), 최고 속도 제한(SPEED_LIMIT), 자율 재계획 금지, 동작 유발, 우선·벌점·방향 구역을 정의하며, 속도 제한 구역에서는 로봇이 정해진 최고 속도보다 빠르게 달려서는 안 된다고 규정한다. | ref-1079 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f12 | [사실] | VDA 5050 3.0.0 은 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 밝혀, 구역·속도 제한 전달이 안전 기능 자체를 대신하지 않음을 명시한다. | ref-1079 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | ROS 2 내비게이션 스택 Nav2 의 Collision Monitor 는 컨트롤러 속도 명령을 거르는 독립 노드로, 영역 안 장애물 점 수에 따른 정지·감속(비율)·속도 제한과 충돌까지 남은 시간 기반 접근 모델을 두고 여러 영역이 동시에 걸리면 가장 강한 조치를 쓰지만, 하드 실시간 안전 인증을 제공하지 않아 안전 등급 하드웨어를 대신하지 않는다고 밝힌다. | ref-1078 | 아니오 | medium | 2026-09-30 | 예외·성과 | — |
| f14 | [추정] | 아마존은 풀필먼트 센터에서 로봇 구역에 들어가는 직원이 로보틱스 테크 조끼를 착용·활성화하면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명한다. | ref-1084 | 아니오 | low | 2026-09-30 | 물류창고 / 제약 | 벤더 주장 |
| f15 | [사실] | Francis 외 52명(ACM Transactions on Human-Robot Interaction, arXiv 2306.16740)은 사회적 로봇 주행의 원칙을 안전·편안함·가독성·예의·사회적 역량·상대 이해·능동성·맥락 적합성 8가지로 정하고, 알고리즘을 공정하게 비교하기 위한 지표·시나리오·벤치마크·시뮬레이터 지침을 제시했다. | ref-1083 | 아니오 | medium | 2023-09 | — | — |
| f16 | [사실] | Jafari·Nguyen·Liu(arXiv 2604.13677, 2026-04)는 이동 로봇과 자원 보행자의 일대일 조우 실험에서 보행자가 보고한 편안함이 최소 거리와 최소 예상 충돌 시간 같은 운동학 변수와 중간 정도의 유의한 상관을 보였고, 이들을 합친 복합 지표가 오즈비 3.67 로 가장 잘 예측했다고 보고했다. | ref-1089 | 아니오 | medium | 2026-04 | 제약 | — |
| f17 | [사실] | Rondoni 외(Scientific Reports, 2024-08)는 병원 물류용 HOSBOT 과 TIAGo 를 시뮬레이션 병원 환경에서 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 속도가 높을수록 정확도가 떨어졌다고 보고했다. | ref-1085 | 아니오 | medium | 2024-08-07 | 병원 / 제약 | — |
| f18 | [사실] | Farrell 외(UC San Diego, arXiv 2503.21141, 2025-03)는 학습 기반 제어 장벽 함수(CBF)를 Open-RMF 에 통합해 창고의 다중 로봇·다중 행위자 상황에서 보행자를 포함한 정적·동적 장애물을 피하는 안전 강화 제어를 제안하고 로봇 수·속도·장애물 수를 바꿔 평가했다. | ref-1086 | 아니오 | medium | 2025-03-27 | 물류창고 | — |
| f19 | [사실] | Kazemi Eskeri 외(IROS 2025)의 사람 인지형 작업 배정(HATA)은 과거 사람 이동 패턴을 담은 시공간 질의형 움직임 지도(Maps of Dynamics)로 사람이 작업 실행 시간에 주는 영향을 확률적 비용으로 추정해 배정에 반영했고, 사람 움직임을 고려하지 않는 기준선보다 임무 완료 시간을 26%, 기존 기준선보다 19% 줄였다고 보고했다. | ref-1087 | 아니오 | medium | 2025-08-27 | 수행 자원 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에 대해, 분리 거리는 고정값이 아니라 사람 속도·반응 시간·정지 거리·측정 불확실도로 그때그때 계산되고(f1~f3), 감속·정지 기준은 적용 유형별 표준·인증이 구역·속도 상한으로 정하며(f6·f7·f9·f10), 사람이 편안하게 느끼는 거리·충돌 시간은 안전 정지 거리와 별도의 기준이 필요한 것으로 보인다(f15·f16). | ref-1075, ref-1077, ref-1080, ref-1081, ref-1083, ref-1089 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 안전 거리가 로봇 정지 성능과 센서 갱신에 따라 달라져 로봇·현장마다 다르고(f1~f3), 협동로봇·무인 트럭·실외 로봇이 각기 다른 표준·법규로 울타리 면제·구역·속도 상한을 정하며(f4~f10), 보수적인 감속·정지가 처리량과 수용성에 영향을 주기 때문이다(f3·f16·f19). | ref-1075, ref-1076, ref-1082, ref-1077, ref-1088, ref-1080, ref-1081, ref-1089, ref-1087 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 49. 사람 근접 안전에서 ROP가 직접 맡을 범위는 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하는 것(f11), 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하는 것(f14·f18·f19), 그 조정과 정지·재개 이력을 기록하는 것이며, 이는 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다(f12·f13). | ref-1079, ref-1084, ref-1086, ref-1087, ref-1078 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(f1·f5·f6·f7)은 로봇 제조사와 시스템 통합자에, 현장 배치의 위험성 평가(f8)는 시스템 통합자에, 울타리·안전매트·인터록(f5)은 설비 안전 쪽에, 실외 인증 대상인 로봇·관제장치 조합의 적합성(f9)은 운영 사업자에 속하므로, ROP 는 그 설정값과 상태를 받아 계획에 반영하는 인터페이스를 맡을 것으로 보인다. | ref-1075, ref-1082, ref-1077, ref-1088, ref-1080 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 이 영역은 위험성 평가·정지·재개의 48. 안전·위험 관리(f8), 표준·인증의 50. 안전 표준·인증·사고 조사(f4~f10), 사람 이동 모델의 19. 사람·보행자 모델(f16·f19), 구역을 담는 16. 장소 의미·지도 관리(f11), 구역을 전달하는 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f11·f12), 사람 인지형 배정의 25. 작업 배정 — MRTA(f19), 구역·속도를 반영하는 27. 다중 로봇 경로·교통 관리 — MAPF(f11·f18), 협동 작업의 31. 사람–로봇 협업(f1·f5), 법규의 59. 법·규제·보험·라이선스(f5·f9), 수용성의 60. 노동·수용성·접근성(f15·f16), 평가의 54. 시험·형식 검증·벤치마크(f15·f17), 적용 현장인 61. 물류창고(f14·f18)·63. 병원·의료(f17)·66. 실외(f9·f10)와 이어진다. | ref-1088, ref-1076, ref-1080, ref-1089, ref-1087, ref-1079, ref-1086, ref-1075, ref-1082, ref-1083, ref-1085, ref-1084 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2016 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 아니오 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2602.17822 | 아니오 |
| ref-1077 | ISO (ISO/TC 110) | ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems (제목 일부는 검색 결과 기준) | 2023 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/83545.html | 예 |
| ref-1078 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md | 아니오 |
| ref-1079 | VDA / VDMA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0) | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1080 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-1081 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부는 검색 결과 기준) | 2023-07-28 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1082 | 지디넷코리아 | "협동로봇 충돌 안전 계산하고 써야죠" | 2024-03 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240305160245 | 아니오 |
| ref-1083 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2306.16740 | 아니오 |
| ref-1084 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 아니오 |
| ref-1085 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 아니오 |
| ref-1086 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2503.21141 | 아니오 |
| ref-1087 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-1088 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | low | 2026-09-30 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 아니오 |
| ref-1089 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2604.13677 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/human-proximity-safety.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(왜 중요한가), f20(핵심 질문 답, 추정) / 섹션 4: 속도·분리 감시·보호 분리 거리 f1·f2, 동력·힘 제한 f5, 운용 구역 f6, 속도 제한·진입 금지·승인 구역 f11, 움직임 지도 f19, 제어 장벽 함수 f18, 사회적 주행 원칙 f15 / 섹션 5: 물류창고 — f14(제약: 조끼 신호로 감속·우회·정지, 벤더 주장 병기)·f18(연구, 창고 시나리오), 병원 — f17(제약: 보행 속도 기반 0.2~1.0 m/s, 시뮬레이션 병원임을 명시), 실외 — f9·f10(제약: 15 km/h·질량별 속도 상한·횡단보도 대기). 제조 공장은 f5(산업용 로봇 사업장 규정)로 서술하되 현장 사례가 아님을 밝히고, 상업 시설·가정·기타 사례는 찾지 못함을 명시 / 섹션 6: 계산형 보호 거리 f1~f3, 로봇 측 감속·정지 영역 f13, 플릿 수준 구역·속도 제한 f11·f12, 착용형 신호 f14, 사람 인지형 배정·교통 f18·f19, 편안함 지표 f16 / 섹션 7: ISO 10218·ISO/TS 15066 f4, ISO 3691-4 f6·f7(원문 미열람), ANSI/A3 R15.08-2 f8, 실외이동로봇 운행안전인증 f9·f10, 산업안전보건기준에 관한 규칙 제223조 f5, VDA 5050 구역 f11·f12, Nav2 Collision Monitor f13 / 섹션 8: f1·f3·f15·f16·f17·f18·f19·f4 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 16, 19, 20, 21, 25, 27, 31, 48, 50, 54, 59, 60, 61, 63, 66 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 50. 안전 표준·인증·사고 조사 페이지 섹션 7 에 f4·f6~f10 반영, 16. 장소 의미·지도 관리 페이지에 f11 구역 유형 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 속도·분리 감시 | Speed and Separation Monitoring (SSM) | 로봇과 사람의 거리와 속도를 계속 감시해 분리 거리가 보호 분리 거리보다 작아지기 전에 로봇을 감속하거나 정지시키는 협동 작업 방식이다. |
| 보호 분리 거리 | Protective Separation Distance | 사람 이동 속도, 로봇 반응·정지 시간, 침입 거리, 위치 측정 불확실도로 계산하는, 로봇이 사람에 닿기 전에 멈출 수 있도록 유지해야 하는 최소 거리다. |
| 동력·힘 제한 | Power and Force Limiting (PFL) | 로봇이 사람과 접촉하더라도 해를 주지 않도록 동력과 힘을 정해진 한계 안으로 제한해 작동시키는 협동 작업 방식이다. |
| 움직임 지도 | Maps of Dynamics (MoD) | 과거 사람 이동을 장소와 시간에 따라 모아 특정 위치·시각의 이동 방향과 흐름을 질의할 수 있게 만든 시공간 지도다. |
| 제어 장벽 함수 | Control Barrier Function (CBF) | 로봇 상태가 안전 집합 밖으로 나가지 않도록 제어 입력에 제약을 거는 함수로, 기존 제어 명령을 안전 쪽으로 걸러 내는 데 쓴다. |

## 열린 질문

새로 생긴 질문:

- 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? | 관련 영역: 49. 사람 근접 안전, 48. 안전·위험 관리 | 근거: f12 | 종류: 일반
- 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? | 관련 영역: 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사 | 근거: f10 | 종류: 출처 충돌
- 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? | 관련 영역: 49. 사람 근접 안전, 59. 법·규제·보험·라이선스 | 근거: f9 | 종류: 일반
- 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 21. 상호운용 표준·적합성 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 13회 · 신규 출처 15건
- 미확인 항목:
    - f6·f7 ISO 3691-4:2023 의 구역 구분, 감지 무효화 시 0.3 m/s, 시험편 치수: ISO·ANSI 블로그 페이지 403 으로 원문 미열람, 검색 결과 요약 기준이라 추정·low 로 둠
    - f5 산업안전보건기준에 관한 규칙 제223조 조문: law.go.kr 페이지에서 조문 본문을 읽지 못했고 yeslaw 는 인증서 오류로 열지 못해 기사(ref-1082)만 근거
    - f8 ANSI/A3 R15.08-2 원문 미열람(유료). 플릿(IMRF) 포함 여부는 검색 요약에만 있어 claim 에 넣지 않음
    - f14 아마존 조끼: 2018년 25개 창고 도입 등 수치는 검색 요약(위키백과)에만 있어 넣지 않음. 독립 출처 교차 확인 실패
    - f15 근접학 거리(0.45 m·1.2 m) 예시는 검색 요약에만 있어 넣지 않음
    - f16 실험 장소·참가자 수, f18 정량 결과, f19 실험 환경은 초록에 없어 미확인
    - f10 심사 항목 16가지와 f9 인증기관 페이지 8개 항목의 차이: 출처 충돌로 열린 질문에 올림
    - ISO 13482(개인 돌봄 로봇) 개정판 내용: 검색 1회에서 2025년 개정 세부를 확인하지 못해 넣지 않음
    - 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례는 찾지 못함(쇼핑몰·공항 검색 1회, 찾은 소매점 배치 연구 arXiv 2601.01946 은 근접 안전 내용이 없어 제외)
    - 제조 공장 현장 사례는 규정(f5)과 작업셀 연구(f1~f3)만 있고 현장 유형을 밝힌 적용 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1~f3·f5~f7: 안전 등급 인력 감지·보호 정지·SSM·PFL 은 로봇 제조사·시스템 통합자의 안전 기능(원문 19장 로봇 자체 지능·제어, 설비 안전 제어 연계 대상)이므로 개념·기준 근거로만 쓰고 f23 에서 '연계 대상: '으로 구분함
    - f13: Nav2 Collision Monitor 는 로봇 측 로컬 회피 계층(연계 대상)이며 안전 인증이 없음을 명시; ROP 직접 범위로 서술하지 않도록 주의
    - f9·f10: 실외이동로봇 인증 대상은 로봇과 관제장치의 조합이라 관제장치 쪽이 ROP 범위와 겹칠 수 있음. 인증 책임은 운영 사업자 몫으로 f23 에서 구분
    - f18: 제어 장벽 함수는 로봇 제어 계층 기법이지만 Open-RMF 플릿 계층에 통합한 사례로만 인용
- 한계: web_fetch_available: true · fetch_mode full. 검색 13회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 ISO 13482·ISO 13855 원문, 상업 시설·가정 사례, 국내 서비스 로봇 기준을 더 넣지 못했다. 주의: 입력의 이전 브리프 2026-09-30-08 도 ref-1075~ref-1089 를 썼으나 실행 컨텍스트가 이 구간을 이 실행 전용으로 예약했다고 밝혀 그대로 썼다(퍼블리셔의 id 충돌 확인 필요). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건; VDA 5050·ISO 3691-4 가 기존 참고문헌에 있으면 퍼블리셔가 같은 URL 로 합쳐야 한다). 원문 열람: 14건 열었고(webfetch 12건, github_raw 2건) ISO 3691-4(ref-1077)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Marvel·Norcross(ref-1075)·Rondoni 외(ref-1085)는 PMC 본문, 나머지는 초록 페이지다. 교차 확인 1건(f9: 15 km/h·500 kg 을 인증기관 페이지와 기사로 확인). 벤더 문서는 아마존(ref-1084) 1건이며 f14 는 vendor_claim·추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에는 f20 으로 답했고 결론은 '분리 거리는 계산값이고, 감속·정지 상한은 적용 유형별 표준·인증이 구역·속도로 정하며, 편안함 기준은 별도'라는 추정이다. 현장 유형 사례는 물류창고(f14·f18)·병원(f17, 시뮬레이션)·실외(f9·f10)이며 제조 공장은 규정 수준, 상업 시설·가정·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-1080)·지디넷코리아 2건(ref-1081·ref-1082)이다. 용어집에 이미 있는 운용 구역·구역 집합·위험성평가·협동 적용·실외이동로봇 운행안전인증·공공 영역 이동로봇·필터 마스크·해제 구역은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```
