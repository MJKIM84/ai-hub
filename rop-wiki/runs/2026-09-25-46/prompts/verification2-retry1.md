(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-46
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 18. 사람–로봇 협업·운영 인터페이스 (E. 협업·현장 운영)
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

### runs/2026-09-25-46/target.json

```json
{
  "run_id": "2026-09-25-46",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 46,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 18,
    "area_name": "18. 사람–로봇 협업·운영 인터페이스",
    "category": "E. 협업·현장 운영",
    "category_letter": "E"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=18"
}
```

### runs/2026-09-25-46/research.json

```json
{
  "run_id": "2026-09-25-46",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 18,
    "area_name": "18. 사람–로봇 협업·운영 인터페이스",
    "category": "E. 협업·현장 운영"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음",
    "섹션 5. 현장 시나리오 비어 있음 — 피킹 단계의 사람 피커–운반 로봇 대기 시나리오 필요",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 nl-task-chatbot 반영 제안 4건(지시·확인·되묻기·실행 전 확인) 대기",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 트랙 반영 제안 2건 대기",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 기존 oq-009(교대조별 작업자 수와 로봇 수)가 이 영역과 관련"
  ],
  "research_questions": [
    "사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [분류원문]",
    "사람 피커와 AMR(Autonomous Mobile Robot, 자율이동로봇)이 함께 피킹할 때 대기·배치(batch)·속도·인원 구성을 어떻게 정하는가, 교대조별 작업자 수와 로봇 수를 함께 정하는 모델이 있는가? (oq-009 관련, 섹션 5·6·8 겨냥)",
    "승인·수동 전환·일시정지·비상정지 같은 사람 개입을 로봇–관제 인터페이스 표준(VDA 5050)과 오픈소스 관제(Open-RMF)는 어떤 필드·기능으로 다루는가? (섹션 6·7 겨냥)",
    "사람과 이동로봇이 같은 공간에서 일할 때 적용되는 안전 표준과 국내 규제·지침은 무엇이며, ROP 인터페이스가 맡을 부분은 어디까지인가? (섹션 7·9 겨냥)",
    "운영자에게 로봇 상태와 실패를 설명 가능하게 보여 주는 방법과 한 운영자가 감독할 수 있는 로봇 수에 관한 연구는 무엇이 있는가? (섹션 4·6·8 겨냥)",
    "트랙 nl-task-chatbot 이 제안한 반영 내용 6건(자연어 지시 제품, 음성 피킹 확인, 되묻기 방식, 실행 전 확인)은 이 영역 6·8절에 어떻게 넣을 수 있는가? (섹션 6·8, 27. AI·학습·적응과 모델 운영 연결)",
    "사람–로봇 협업 인터페이스에서 ROP 직접 범위와 연계 대상(로봇 본체 안전 기능, WMS 화면)의 경계는 어디인가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Žulj 외(2022)는 창고를 구역으로 나눠 구역마다 피커 1명을 두고, 피커가 통로에서 배치를 채운 뒤 교차 통로에서 기다리는 AMR에 넘기면 AMR이 출하 거점까지 운반하는 AMR 보조 피커–부품(picker-to-parts) 시스템을 다루며, AMR 보조로 피커의 비생산적 보행 시간을 줄일 수 있다고 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-467"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'handing over the completed batch to an AMR waiting at the cross aisle'; 구역당 피커 1명, 배치 구성과 배치 순서를 함께 결정(EJOR 298(1)). 원문 미열람.",
      "as_of": "2022",
      "flow_step": "피킹",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "Löffler·Boysen·Schneider(2023)는 AMR이 주문 용기를 싣고 선반 앞에서 기다리고 피커가 물품을 넣은 뒤 다른 대기 AMR로 옮겨 가며 출발점으로 돌아가지 않는 로봇 보조 피킹에서, 여러 AMR과 여러 피커의 조율을 작업 완료 시각(makespan) 최소화 문제로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-468"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: AMRs 'carry bins ... wait in front of shelves'; pickers 'continuously moving between different waiting AMRs without returning to the depot'; 목표 makespan 최소화(Transportation Science 57(4)). 원문 미열람.",
      "as_of": "2023",
      "flow_step": "피킹",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "Löffler 외(2023)는 확률적 피킹 시간이 일으키는 연쇄 지연(ripple effect)을 작업자를 작은 하위 집단으로 나누어 줄일 수 있고, 피커와 AMR의 이동 속도가 비슷해야 하며 AMR이 더 느리면 시스템 성과가 나빠진다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-468"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'ripple effect caused by stochastic picking times can be effectively mitigated by separating the workforce into smaller subgroups'; 'slower AMRs deteriorate system performance'. 저자 계산 실험 결과. 원문 미열람.",
      "as_of": "2023",
      "flow_step": "피킹",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "Yang 외(IISE Transactions, 2026)는 협동 피킹을 로봇1–피커1, 로봇1–피커 다수, 피커1–로봇 다수, 피커 다수–로봇 다수의 네 모드로 나누고, 모드마다 포크–조인 대기행렬 네트워크(fork-join queueing network)와 피로–회복 모델로 투입할 피커 수와 로봇 수를 분석한다.",
      "tag": "사실",
      "source_ids": [
        "ref-469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: four modes (couple, SR-to-MP, SP-to-MR, multiple pickers to multiple robots); 'fork-join queuing network (FJQN) model' 과 'fatigue-recovery model'. IISE Transactions 58(3), 304-323. 교대조 단위 결정 여부는 요약에 없음. 원문 미열람.",
      "as_of": "2026-03",
      "flow_step": "피킹",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "f1~f4 에 따르면 분류 원문의 질문(사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하기)은 인터페이스 단독이 아니라 구역·배치 구성, 피커와 로봇의 수 비율, 로봇 속도, 다음 작업 안내의 결합으로 풀리는 것으로 보이며, ROP 운영 인터페이스는 그 결정 결과(다음 대기 로봇 위치, 넘겨줄 배치)를 작업자에게 전달하는 접점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-467",
        "ref-468",
        "ref-469"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1(교차 통로 인계), f2(대기 AMR 사이 이동), f3(하위 집단·속도), f4(모드별 인원 투입)를 SCM 질문에 대응시킨 이 위키의 추론. 결합 방식을 제시한 단일 출처는 찾지 못함.",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "VDA 5050 최신판 상태(state) 메시지 스키마는 이동로봇의 운용 모드(operatingMode)를 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값으로 보고하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema 원문: \"operatingMode\" description 'Current operating mode of the mobile robot.', enum 7개 값. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f7",
      "claim": "VDA 5050 최신판 명세는 SEMIAUTOMATIC 모드에서 로봇이 관제 주문을 받되 운영자가 로봇 HMI(Human-Machine Interface)로 실행을 확인해야 하고, INTERVENED 모드에서는 운영자가 HMI로 제어를 넘겨받아 새 주문을 받지 않으며, MANUAL 모드에서는 관제가 주문을 보낼 수 없다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 열람 응답(요약 도구 경유): SEMIAUTOMATIC 'an operator must confirm execution via HMI before proceeding'; INTERVENED 'operator has taken control via HMI, overriding fleet control'. 문구가 도구 요약일 수 있어 명세 표와 글자 단위 대조는 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "VDA 5050 최신판 상태 스키마는 안전 상태(safetyState)로 비상정지 종류(activeEmergencyStop: 로봇에서 수동 확인하는 MANUAL, 시설 비상정지를 원격 확인하는 REMOTE, NONE)와 보호 필드 침범(fieldViolation)을 필수로 두고, 물리 버튼이나 즉시 동작으로 일시정지된 상태(paused)를 보고하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "state.schema 원문: activeEmergencyStop 'MANUAL: e-stop shall be acknowledged manually at the mobile robot. REMOTE: facility e-stop shall be acknowledged remotely.'; paused 'either because of the push of a physical button ... or because of an instantAction'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f9",
      "claim": "Open-RMF Web(rmf-web)은 Open-RMF 배치를 웹에서 시각화하고 제어하기 위한 패키지 모음으로, API 서버·API 클라이언트·대시보드 프레임워크로 구성된다.",
      "tag": "사실",
      "source_ids": [
        "ref-302"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: 'a collection of packages that provide a web-based interface for users to visualize and control all aspects of Open-RMF deployments.' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Open-RMF 데모(rmf_demos)는 웹 대시보드에서 작업을 제출하고 로봇·작업 상태를 볼 수 있게 하며, 비상 경보(/fire_alarm_trigger 토픽)를 켜면 모든 로봇을 가장 가까운 주차 위치로 보낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: 'All robots will get directed to the nearest parking spot when the emergency alarm is triggered.' 대시보드는 fleet adapter 의 server_uri 연결로 상태를 받음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "ISO 3691-4:2023(제2판, 2020판 대체)은 무인 산업용 트럭과 그 시스템(차량, 제어 시스템, 하역 장치, 배터리 충전소, 적재물 인계 스테이션)의 안전 요구사항을 정하며, 사람 감지 설정·운전 모드·제동 같은 안전 기능 요구를 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 2023-06 발행, 제1판(2020) 대체, 'active detection field'·'operational stop' 용어 추가. 적용 범위에 battery charging stations, load transfer stations 포함. 원문(유료) 미열람.",
      "as_of": "2023-06",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "ISO 10218-1:2025·ISO 10218-2:2025 개정판은 협동 적용(collaborative application) 안전 요구를 본문에 넣어 ISO/TS 15066 의 내용을 흡수하고, 기능 안전 요구를 명확히 하며 사이버보안 요구를 더했고, '협동로봇' 대신 '협동 적용'이라는 용어를 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-471"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약(A3 FAQ 등): 2011판 이후 첫 개정, 협동 적용 요구 통합·기능 안전 명확화·사이버보안 추가, 'cobot' 대신 'collaborative applications'. 표준 원문 미열람.",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "ANSI/A3 R15.08 계열은 산업용 이동로봇(IMR)의 안전을 제조사 요구(1부), 현장 통합·적용 요구(2부, 2023), 사용자 책임(3부)으로 나누고, 2부는 IMR 또는 IMR 플릿을 현장에 통합·설정하는 요구를 정하며 조작기를 단 이동로봇(유형 C)까지 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-472"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: Part 2 'specifies requirements for integrating, configuring, and customizing an IMR or fleet of IMRs into a site'; Type A/B/C. 원문 미열람.",
      "as_of": "2023-10",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "고용노동부·한국산업안전보건공단은 2023-07 '고정식·이동식 산업용 로봇의 협동작업 안전 가이드'를 배포해 감지기를 활용한 충돌방지 조치, 작업자의 안전한 이동·작업 방법, 충돌방지조치 점검표, 이동식 로봇 예시(완제품 이송 공정)를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-473",
        "ref-474"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 가이드 구성 '로봇 사용 시 필요한 충돌방지 조치, 로봇 충돌방지조치 점검표, ... 이동식 로봇 충돌방지조치 예시(완제품 이송 공정)'. 기사는 같은 보도자료 기반이라 독립 교차 아님. 원문 미열람.",
      "as_of": "2023-07",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "로봇신문 보도에 따르면 이 가이드는 로봇 이동 플랫폼이 비정상 작동할 때 긴급 정지할 수 있도록 작업자가 접근 가능한 위치에 비상정지장치를 두도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-474"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 요약: '작업자가 접근 가능한 위치에 비상정지장치가 설치되어야 한다'. 가이드 원문 대조 미확인. 원문 미열람. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "중소벤처기업부·대구광역시 발표에 따르면 대구 이동식 협동로봇 규제자유특구 실증을 거쳐 이동식 협동로봇 안전기준 한국산업표준(KS)이 제정되었으며, 그 전에는 명확한 안전기준이 없어 작업공간 분리나 안전 울타리 설치가 필요했다.",
      "tag": "사실",
      "source_ids": [
        "ref-475"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: '11월 1일부터 ... 안전기준에 관한 한국산업표준(KS)이 제정'; 표준은 적용범위·용어·안전 요구사항과 위험성 감소 대책 포함. KS 번호는 요약에 없음. 원문 미열람.",
      "as_of": "2024-11",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "Das·Banerjee·Chernova(HRI 2021)는 계획 실행 중 예기치 않은 실패의 원인을 비전문가에게 설명하는 방식을 비교해, 실패의 맥락과 지난 행동 이력을 담은 설명이 비전문가의 실패·해결책 파악에 가장 효과적이었다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-476"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'explanations capturing the context of a failure and history of past actions are the most effective for failure and solution identification among non-experts'. 가정 환경 실험. 원문 미열람.",
      "as_of": "2021-01",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "상황 인식 기반 에이전트 투명성(SAT) 모델은 에이전트의 현재 행동·계획(1수준), 추론(2수준), 미래 결과 예측(3수준)을 운영자에게 보여 주는 틀이며, 관련 연구에서 높은 수준의 투명성 화면이 운영자의 상황 인식과 신뢰를 높였다고 보고된다.",
      "tag": "사실",
      "source_ids": [
        "ref-477"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: Level 1 current actions and plans, Level 2 reasoning process, Level 3 projection of future outcomes; higher SAT interfaces → greater situation awareness and trust. 군사·다중 로봇 중재 연구 맥락. 원문 미열람. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수(팬아웃, fan-out)는 운영자가 방치해도 로봇 성과가 유지되는 정도(neglect tolerance)와 로봇 하나를 다루는 데 드는 상호작용 시간에 따라 정해진다는 척도가 제안되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-478"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 'The number of robots that can be operated simultaneously is called the fan-out'; 'Robots that have high neglect tolerance and lower interaction time will achieve higher fan-out.' CHI 2004 논문. 원문 미열람.",
      "as_of": "2004",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "독일 연방산업안전보건연구소(BAuA) 연구자의 문헌 고찰(Rey-Becerra·Wischniewski, Ergonomics, 2025)은 한 사람이 여러 로봇을 감독하는 시스템 연구 44건을 분석해 효율·유연성의 이점과 함께 주의·인지 부하 관리의 어려움을 지적하고, 설계·평가용 점검표를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-479"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약: 658건 중 44건 분석; 'challenges in managing attention and cognitive load'; 'practical checklist for designing and evaluating SHMR systems'. 원문 미열람.",
      "as_of": "2025-07-11",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "국내 물류 로봇 업체 플로틱스는 100평 규모 물류센터 환경에서 작업자 2명이 로봇 6대와 존피킹을 수행하는 구성을 시연했다고 보도되었다.",
      "tag": "추정",
      "source_ids": [
        "ref-480"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 기사 검색 요약 '100평 규모로 구현한 물류센터 환경에서 2명의 작업자가 6대 로봇과 함께 존피킹'. 실측 생산성 수치는 독립 확인 없음. 원문 미열람.",
      "as_of": "2023-12-22",
      "flow_step": "피킹",
      "flow_item": "수행 자원",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f22",
      "claim": "음성 피킹은 시스템이 위치와 수량을 음성으로 지시하고 작업자가 위치 체크 디지트·수량 같은 짧은 음성 응답으로 동작마다 확인하는 방식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-272",
        "ref-275"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "Lucas Systems 음성 지시 창고 자료와 VOCOLLECT 양수 미국 특허 US 8868519(위치 체크 디지트 불일치 경고)가 각각 기술. 두 출처 원문 미열람. (재인용: 2026-09-25-26)",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "Locus Robotics 는 협동 피킹 로봇 화면에 품목·위치·수량을 보여 주고 선택 기능으로 위치·용기 바코드 스캔 뒤 화면 확인을 받는다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-279"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: LocusONE 사용자 인터페이스 페이지 요약. 원문 미열람. (재인용: 2026-09-25-26)",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "완료·인계",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f24",
      "claim": "InOrbit 는 RobOps Copilot 을 2024년에 로봇 운영 데이터에 대한 자연어 질의·설명 기능으로 발표했다.",
      "tag": "추정",
      "source_ids": [
        "ref-176",
        "ref-278"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 2024-05 보도자료와 제품 페이지 요약. 미션 정의 방식과 실행 전 확인·승인 절차는 미확인. 같은 회사 자료라 독립 교차 아님. 원문 미열람. (재인용: 2026-09-25-21)",
      "as_of": "2024-05",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f25",
      "claim": "Rasa 3.x 의 폼(Forms)은 필요한 슬롯 목록을 정해 두고 비어 있는 필수 슬롯을 사용자에게 차례로 묻는 방식으로 작업 지향 대화의 되묻기를 구현한다.",
      "tag": "사실",
      "source_ids": [
        "ref-356"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Rasa 문서 forms.mdx 요약: required_slots 를 채울 때까지 질문. 이번 실행에서 다시 열지 않음. (재인용: 2026-09-25-30)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "KnowNo(CoRL 2023)는 LLM 계획기의 선택지 불확실성을 등각 예측(conformal prediction)으로 재어 불확실할 때 사람에게 도움을 요청하게 하는 방법이다.",
      "tag": "사실",
      "source_ids": [
        "ref-351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Ren 외(2023) 'Robots That Ask For Help' 초록 요약. 가정·실험실 환경. 원문 미열람. (재인용: 2026-09-25-30)",
      "as_of": "2023-07",
      "flow_step": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "CLARA(IEEE RA-L 2024, 고려대 등)는 사용자 명령을 명확·모호·수행 불가로 분류하고 모호한 명령에는 되묻는 질문을 생성하는 방법이다.",
      "tag": "사실",
      "source_ids": [
        "ref-353"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Park 외(2024) 초록 요약: classifying and disambiguating user commands. 원문 미열람. (재인용: 2026-09-25-30)",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f28",
      "claim": "SafeGate(Purdue, 2026)는 LLM 이 해석한 자연어 명령에서 안전 속성을 추출해 실행 전에 결정적 규칙으로 승인·거부하는 게이트를 제안하며, ISO 13482(개인 돌봄 로봇) 기반이고 물류 현장 평가는 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Obi 외(2026-04) 초록 요약: pre-execution safety gate, task safety contracts. 성능은 저자 보고. 원문 미열람. (재인용: 2026-09-25-37)",
      "as_of": "2026-04",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "연계 대상: Mecalux 는 WMS(Easy WMS)의 생성형 AI 비서가 채팅 지시를 실행하기 전에 수행할 동작과 영향을 요약해 보여 주고 채팅으로 확인을 받는다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-418"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Mecalux 뉴스 페이지 요약. WMS 쪽 사례이며 로봇 지시가 아님. 원문 미열람. (재인용: 2026-09-25-37)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f30",
      "claim": "f7·f22·f25~f29 를 나란히 놓으면 운영 인터페이스의 확인은 대상과 시점에 따라 로봇 동작 실행 전 운영자 확인(VDA 5050 SEMIAUTOMATIC), 작업자 동작마다의 확인(음성 체크 디지트), 자연어 지시의 해석 확인(되묻기·실행 전 게이트)으로 구분되는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-272",
        "ref-275",
        "ref-356",
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 출처의 확인 방식을 대상(로봇 동작·작업자 동작·지시 해석)과 시점(실행 전·동작 중)으로 묶은 이 위키의 정리. 이 구분을 제시한 단일 출처는 찾지 못함.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계",
      "source_unopened": false
    },
    {
      "id": "f31",
      "claim": "연계 대상: 사람 감지·보호 필드·비상정지 회로·속도와 거리 감시 같은 안전 기능은 로봇 제조사와 현장 통합사가 ISO 3691-4·ISO 10218·R15.08 에 따라 갖추는 것이므로, 이종 로봇을 연결하는 ROP 는 운용 모드·안전 상태의 표시, 작업 재개·수동 전환의 승인 흐름, 구역·권한 설정 반영을 맡는 경계가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-470",
        "ref-472",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8(safetyState·paused 는 로봇이 보고), f11·f13(안전 기능은 차량·시스템·통합 요구)을 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 경계에 대응시킨 추론.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": false
    }
  ],
  "sources": [
    {
      "id": "ref-467",
      "org": "Žulj, I., Salewski, H., Goeke, D., & Schneider, M.",
      "title": "Order batching and batch sequencing in an AMR-assisted picker-to-parts system",
      "published": "2022",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 구역별 피커가 배치를 채워 교차 통로의 AMR에 넘기는 AMR 보조 피킹에서 배치 구성·순서를 최적화한 EJOR 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-468",
      "org": "Löffler, M., Boysen, N., & Schneider, M.",
      "title": "Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers",
      "published": "2023",
      "url": "https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 선반 앞에서 기다리는 AMR과 여러 피커의 조율을 makespan 최소화로 다룬 Transportation Science 57(4) 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-469",
      "org": "Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M.",
      "title": "Deploying pickers and robots in cobot-based collaborative order picking systems",
      "published": "2026-03",
      "url": "https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 네 가지 사람–로봇 협동 피킹 모드를 포크–조인 대기행렬 네트워크와 피로–회복 모델로 분석해 피커·로봇 투입 수를 정하는 IISE Transactions 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업용 트럭(AGV·AMR)과 그 시스템의 안전 요구·검증 표준 제2판 소개 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-471",
      "org": "A3(Association for Advancing Automation)",
      "title": "Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs)",
      "published": null,
      "url": "https://www.automate.org/robotics/blogs/updated-iso-10218-faq",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 10218-1/2:2025 개정의 주요 변경(협동 적용 통합, 기능 안전, 사이버보안)을 설명하는 로봇 산업 협회 자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-472",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available",
      "published": "2023-10",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 이동로봇 시스템·적용의 현장 통합 안전 요구(R15.08-2) 발행을 알리는 표준 개발 기관 공지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-473",
      "org": "고용노동부",
      "title": "고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포",
      "published": "2023-07",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 고용노동부·한국산업안전보건공단의 고정식·이동식 산업용 로봇 협동작업 안전 가이드 게시 자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-474",
      "org": "로봇신문",
      "title": "'이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나?",
      "published": null,
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=32130",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 2023-07 이동식 산업용 로봇 안전 가이드의 충돌방지·비상정지 내용을 소개한 기사.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-475",
      "org": "중소벤처기업부(대한민국 정책브리핑)",
      "title": "｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!",
      "published": "2024-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 대구 규제자유특구 실증을 거친 이동식 협동로봇 안전기준 KS 제정을 알린 보도자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-476",
      "org": "Das, D., Banerjee, S., & Chernova, S.",
      "title": "Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery",
      "published": "2021-01",
      "url": "https://arxiv.org/abs/2101.01625",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 실행 실패를 비전문가에게 설명하는 설명 유형을 비교·자동 생성한 HRI 2021 논문의 프리프린트.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-477",
      "org": "Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science)",
      "title": "Situation awareness-based agent transparency and human-autonomy teaming effectiveness",
      "published": null,
      "url": "https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 에이전트의 행동·추론·예측을 세 수준으로 보여 주는 SAT 모델과 그 효과를 정리한 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-478",
      "org": "Olsen, D. R. 외(CHI 2004)",
      "title": "Fan-out: measuring human control of multiple robots",
      "published": "2004",
      "url": "https://dl.acm.org/doi/10.1145/985692.985722",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한 사람이 동시에 다룰 수 있는 로봇 수(팬아웃)를 방치 허용도와 상호작용 시간으로 재는 척도를 제안한 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-479",
      "org": "Rey-Becerra, E., & Wischniewski, S.",
      "title": "Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance",
      "published": "2025-07-11",
      "url": "https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한 사람이 여러 로봇을 감독하는 시스템 연구 44건을 고찰하고 설계·평가 점검표를 낸 Ergonomics 논문(BAuA).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-480",
      "org": "ZDNet Korea",
      "title": "\"대형 물류센터 집품 작업, 로봇 6대로 효율화\"",
      "published": "2023-12-22",
      "url": "https://zdnet.co.kr/view/?no=20231222165139",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플로틱스의 존피킹 로봇 시연(작업자 2명·로봇 6대)을 전한 기사.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(3.0.0) 명세 원문. 이번 실행에서 운용 모드별 설명과 일시정지 동작을 확인했다.",
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
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마 원본. 이번 실행에서 operatingMode·paused·safetyState 정의를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/state.schema",
      "source_unopened": false
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 배치를 웹에서 시각화·제어하는 패키지 모음(API 서버·클라이언트·대시보드)의 공식 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 데모 README. 이번 실행에서 웹 대시보드 연동과 비상 경보 시 로봇의 주차 위치 이동을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_demos/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-272",
      "org": "Lucas Systems",
      "title": "Voice-Directed Warehousing - Solutions | Lucas Systems",
      "published": null,
      "url": "https://www.lucasware.com/voice-directed-warehousing/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 음성 지시 창고 작업(음성 피킹)과 체크 디지트 확인 방식을 설명하는 벤더 자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-275",
      "org": "USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.)",
      "title": "System and method for generating and updating location check digits (US 8868519)",
      "published": null,
      "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 위치 체크 디지트 생성·갱신과 불일치 경고를 기술한 미국 특허 공보.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-279",
      "org": "Locus Robotics",
      "title": "Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface)",
      "published": null,
      "url": "https://locusrobotics.com/locusone/automated-warehouse-software/user-interface",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 협동 피킹 로봇의 작업자용 화면 인터페이스를 소개하는 벤더 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-176",
      "org": "InOrbit.AI",
      "title": "InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024",
      "published": "2024-05",
      "url": "https://www.inorbit.ai/press/inorbit-robops-copilot",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RobOps Copilot 발표 보도자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-278",
      "org": "InOrbit.AI",
      "title": "InOrbit RobOps Copilot - Bring AI power to robot operations",
      "published": null,
      "url": "https://www.inorbit.ai/robopscopilot",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RobOps Copilot 제품 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z. 외",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 등각 예측으로 LLM 계획기의 불확실성을 재어 도움을 요청하게 하는 KnowNo 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-353",
      "org": "Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S.",
      "title": "CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents",
      "published": "2024",
      "url": "https://arxiv.org/abs/2306.10376",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 사용자 명령을 명확·모호·수행 불가로 분류하고 되묻는 CLARA 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-356",
      "org": "Rasa Technologies (RasaHQ/rasa GitHub)",
      "title": "Forms — Rasa documentation (docs/docs/forms.mdx)",
      "published": null,
      "url": "https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이번 실행에서 다시 열지 않았다. 필수 슬롯을 채울 때까지 되묻는 Rasa 폼 문서(참고문헌 목록 신뢰도 high, 이번 실행 미열람으로 medium 상한).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-417",
      "org": "Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 이 해석한 명령의 안전 속성을 실행 전 결정적 게이트로 판정하는 SafeGate 프리프린트.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-418",
      "org": "Mecalux",
      "title": "Mecalux integrates generative AI into Easy WMS",
      "published": null,
      "url": "https://www.mecalux.com/news/generative-ai-easy-wms-mecalux",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. WMS 의 생성형 AI 대화형 비서 기능을 알리는 벤더 뉴스.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
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
      "rationale": "3절 왜 중요한가: f1·f2·f3·f5(사람 피커–로봇 대기 문제), f20(감독 인지 부하) / 4절 용어: f6·f7(운용 모드), f18(SAT), f19(팬아웃), f12(협동 적용) / 5절 시나리오: 피킹 단계 f1·f2·f3·f5·f22 (시작 조건·수행 자원·완료·인계·예외·성과), f21 은 벤더 주장 병기 / 6절 접근법: 협동 피킹 조율 f1~f4, 운용 모드·일시정지·비상정지 f6~f8, 관제 대시보드 f9·f10, 설명·투명성 f17·f18, 트랙 nl-task-chatbot 반영 제안 6건 검토 결과 f22~f30(음성 확인, 벤더 자연어 제품 f23·f24 벤더 주장, 되묻기 f25~f27, 실행 전 게이트 f28, WMS 연계 사례 f29, 확인 유형 정리 f30) — 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 7절 표준·오픈소스: f6~f8(VDA 5050), f9·f10(Open-RMF), f11(ISO 3691-4), f12(ISO 10218:2025), f13(R15.08), f14~f16(국내 가이드·KS) / 8절 연구·자료: f1~f4, f17~f20, 트랙 제안 자료 f25~f28 / 9절 범위: f31(안전 기능은 연계 대상, ROP 는 모드 표시·승인 흐름), f29(WMS 는 연계 대상) / 10절 연결: 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링(f1~f4), 3. 처리능력·거점·설비 계획(f4, oq-009), 9. 로봇·제조사 관제 연동(f6~f8), 20. 예외 복구·재계획·업무 연속성(f10·f17), 19. 모니터링·이상 탐지·원인 분석(f17·f18), 25. 안전·위험 관리(f11~f16), 27. AI·학습·적응과 모델 운영(f24~f28) / 11절 열린 질문: oq-009 와 새 질문 4건"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "팬아웃",
      "term_en": "Fan-out (human-robot team)",
      "definition": "한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수로, 로봇의 방치 허용도와 로봇 하나를 다루는 상호작용 시간으로 추정한다."
    },
    {
      "term_ko": "운용 모드",
      "term_en": "Operating Mode (VDA 5050 operatingMode)",
      "definition": "VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, 운영자 확인이 필요한지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다."
    },
    {
      "term_ko": "상황 인식 기반 에이전트 투명성",
      "term_en": "Situation Awareness-based Agent Transparency (SAT)",
      "definition": "자율 에이전트의 현재 행동·계획, 추론, 미래 결과 예측을 세 수준으로 운영자에게 보여 주어 상황 인식과 신뢰를 돕는 인터페이스 설계 모델이다."
    },
    {
      "term_ko": "협동 적용",
      "term_en": "Collaborative Application",
      "definition": "ISO 10218:2025 에서 로봇 자체가 아니라 사람과 로봇이 함께 일하도록 설계된 적용 방식을 기준으로 안전을 판단하기 위해 '협동로봇' 대신 쓰는 용어이다."
    }
  ],
  "open_questions_new": [
    "2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 25. 안전·위험 관리 | 근거: f16 | 종류: 일반",
    "국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 4. 성과·경제성·프로세스 개선 | 근거: f5 | 종류: 일반",
    "VDA 5050 SEMIAUTOMATIC 모드의 실행 확인을 로봇 HMI 가 아닌 관제·ROP 화면에서 원격으로 할 수 있는지, 원격 확인에 필요한 안전 조건을 정한 규정이나 사례가 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 9. 로봇·제조사 관제 연동 | 근거: f7 | 종류: 일반",
    "물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 19. 모니터링·이상 탐지·원인 분석 | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 28,
    "cross_checked_count": 1,
    "unverified": [
      "이동식 협동로봇 안전기준 KS 번호와 본문 미확인(f16)",
      "f7 운용 모드 설명은 요약 도구 경유 원문 열람이라 명세 표 문구와 글자 단위 대조 미확인",
      "f11~f13 표준 원문(유료) 미열람, 검색 요약·발행 기관 소개 기준",
      "f12 ISO 10218:2025 는 ISO 공식 페이지가 아닌 A3 자료 기준",
      "ref-477 발행 연도 미확인(TIES 게재, 2017 온라인 공개 추정)",
      "ref-478 공저자 전체 미확인",
      "f21 플로틱스 시연 수치 벤더 주장, 독립 확인 없음",
      "oq-009 부분 관련: f4 가 피커·로봇 수 결정 모델을 주지만 교대조 단위 결정 여부 미확인 — 해결 제안하지 않음",
      "특구 참여기업 생산성 9.3% 증가(검색 요약)는 단일 발표·방법 미공개라 finding 으로 내지 않음"
    ],
    "scope_violations": [
      "f31: 사람 감지·보호 필드·비상정지 회로는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 ROP 는 표시·승인 흐름만 맡는다고 구분",
      "f29: WMS 화면 기능은 상위 업무 시스템 쪽 연계 대상으로 표시"
    ],
    "budget_used": {
      "queries": 28,
      "sources": 14
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031(VDA 5050 명세)·ref-051(state.schema)·ref-302(rmf-web README)·ref-104(rmf_demos README). 신규 ref-467~ref-480(예약 구간 안)과 그 밖의 재사용 출처는 원문 미열람(신뢰도 상한 medium). 검색 28회/30, 신규 출처 14건/15. 트랙 반영 제안 6건 처리: 제안 1(InOrbit 등)→f24, 제안 2(음성·Locus 확인)→f22·f23·f30, 제안 3(자료)→f22~f24 출처 재사용(Amazon Proteus·Formant·다임리서치는 이번 브리프에 다시 넣지 않음, 다음 실행 후보), 제안 4·5(되묻기 방식·자료)→f25~f27, 제안 6(실행 전 확인)→f28·f29. 한국 자료: 고용노동부 가이드(f14·f15), 중기부 KS 제정(f16), 국내 업체 시연 기사(f21). 27. AI·학습·적응과 모델 운영 관련 finding(f24~f28)은 27번 영역과 양쪽 연결하도록 10절 제안에 적음. 8. 실시간 세계 상태·데이터 일관성, 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 원격 조작(teleoperation) 관련 공개 자료는 벤더 블로그 위주라 finding 으로 내지 못함 — 원격 조작은 섹션 6에서 약한 부분으로 남음."
  }
}
```

### runs/2026-09-25-46/verification.json

```json
{
  "run_id": "2026-09-25-46",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). ref-467 서지(Žulj·Salewski·Goeke·Schneider, EJOR 2022)가 알려진 논문과 같다. 검증 검색 예산이 없어 추가 검색은 하지 않았고, 브리프 스니펫 기준으로 판단했다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). ref-468 Transportation Science 57(4) 논문. 브리프 스니펫 기준, 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). 저자 계산 실험 결과이므로 본문에 '저자 계산 실험 기준'을 병기해야 한다. 단일 출처."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증 검색에서 IISE Transactions 58(3) 304-323, 저자 5명, 네 모드, FJQN·피로–회복 모델이 스니펫과 일치했다. 온라인 공개일은 2025-06-02이고 권호는 2026-03(as_of)이다. 교대조 단위 결정 여부는 미확인이다. 원문 미열람."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 이 위키의 추론이고 f1~f4 에 근거한다. '이 위키의 정리'임을 밝힌다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증자가 raw.githubusercontent.com state.schema 원문을 열어 operatingMode 설명과 enum 7개 값이 같음을 확인했다. 발행일 미확인(확인일 기준)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "불일치. 입력 원문 텍스트(data/source_texts/ref-031.txt) 6.6.6절 표 10·11과 대조했다. SEMIAUTOMATIC 은 '관제가 제어하며 주행 속도는 HMI가, 조향은 자동 제어'로 되어 있고, 운영자가 HMI로 실행을 확인해야 한다는 내용은 없다. INTERVENED 는 관제가 주문·주문 갱신을 보낼 수 있고, 그 주문은 AUTOMATIC·SEMIAUTOMATIC 으로 돌아간 뒤 실행되며, 즉시 동작은 cancelOrder 만 허용된다. 따라서 '새 주문을 받지 않는다'는 원문과 다르다. MANUAL 에서 관제가 주문·동작을 보내지 않는다는 부분만 원문과 일치한다. 브리프 스스로 '요약 도구 경유'라고 적은 문구가 원문과 어긋난 경우다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증자가 state.schema 원문을 열어 safetyState 필수 필드(activeEmergencyStop·fieldViolation), MANUAL/REMOTE/NONE 설명, paused 설명(물리 버튼 또는 instantAction)이 같음을 확인했다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증자가 rmf-web README 원문을 열어 첫 문장과 구성(API 서버·API 클라이언트·대시보드 프레임워크)을 확인했다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증자가 rmf_demos README 원문을 열어 server_uri 로 rmf-web api-server 에 작업·로봇 상태를 보내 대시보드에서 감시·작업 시작이 가능하다는 점과 /fire_alarm_trigger 시 가장 가까운 주차 위치로 이동한다는 점을 확인했다. 이는 데모 기능이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "핵심(2023 제2판, 2020판 대체, 적용 범위에 충전소·적재물 인계 스테이션 포함)은 스니펫과 일치한다. 표준 원문(유료)은 미열람이다. '운전 모드·제동'은 브리프 발췌에 나타나지 않으므로 본문에서 뺀다(수정 지시)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). ISO 공식 페이지가 아니라 A3(업계 협회) 해설 자료 기준이다. 본문에 'A3 해설 기준, ISO 원문 미열람'을 병기한다. 발행일 미확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "2부(2023-10) 범위와 유형 A/B/C 는 발행 기관(A3) 공지 스니펫과 일치한다. 원문 미열람. 3부(사용자 책임)의 발행 여부는 발췌에 없으므로 '발행 여부 미확인'을 병기한다(수정 지시)."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). 고용노동부 게시 자료 기준이다. ref-474 기사는 같은 보도자료를 바탕으로 해 독립 교차가 아니다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 근거가 기사(ref-474) 단일 출처이고 가이드 원문과 대조하지 않았다. '로봇신문 보도에 따르면'이라는 서술 형식은 유지한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). 정부 보도자료(2024-11) 기준이다. KS 번호는 미확인으로 남긴다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). arXiv 2101.01625(HRI 2021)이다. 가정 환경 실험임을 병기한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). ref-477 발행일은 미확인이다(브리프 추정 2017 온라인 공개는 확인하지 않았으므로 쓰지 않는다). 군사·다중 로봇 연구 맥락임을 병기한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). CHI 2004 논문이다. 공저자 전체는 미확인이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 검증 검색에서 논문(Ergonomics, 2025-07-11 온라인, BAuA 저자)은 실재하고 주의·인지 부하 과제도 일치했다. 그러나 검색 요약은 '658건 중 35건 선정'으로 나와 브리프의 '44건'과 다르다. 분석 건수는 미확인으로 남긴다. 점검표 제시는 검증 스니펫에서 확인하지 못했다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 벤더 주장 유지(vendor_claim: true). 기사가 전한 업체 시연이며 원문 미열람이다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "브리프는 cross_checked: true 로 적었으나 검증자가 두 출처(ref-272 벤더, ref-275 특허)를 이번에 확인하지 못해 false 로 적는다(원문 미열람). 수치 없는 방식 설명이라 [사실] 유지. 용어집 voice-picking·location-check-digit 를 재사용한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 벤더 주장 유지. 원문 미열람."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 벤더 주장 유지. 같은 회사 자료 두 건이라 독립 교차가 아니다. 원문 미열람."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검증자가 raw.githubusercontent.com 으로 forms.mdx 를 열어 폼이 다음 필수 슬롯 값을 묻는다는 문장을 확인했다(브리프는 미열람으로 기록했으며 신뢰도는 올리지 않는다)."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). arXiv 2307.01928 초록 기준이다. 가정·실험실 환경임을 병기한다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). arXiv 2306.10376 초록 기준이다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람). 2026-04 프리프린트다. '물류 현장 평가는 없다'는 부재 단정이므로 '초록에서 물류 현장 평가는 확인되지 않음'으로 바꾼다(수정 지시). 성능은 저자 보고다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 벤더 주장 유지. 연계 대상(상위 업무 시스템 WMS) 표시가 적절하다. 원문 미열람."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다만 구성 요소 가운데 'VDA 5050 SEMIAUTOMATIC 의 실행 전 운영자 확인'은 f7 불일치로 근거가 없으므로 그 항목을 빼고 두 유형(작업자 동작마다의 확인, 자연어 지시의 해석 확인)으로 서술한다. 근거 출처 대부분이 원문 미열람인데 source_unopened: false 로 적혀 있다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 경계에 맞게 안전 기능을 '연계 대상'으로 표시했다. ref-470·ref-472 는 원문 미열람이다."
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
      "f22 는 용어집 voice-picking(음성 피킹)·location-check-digit(위치 체크 디지트)과 겹친다. 새 용어로 등록하지 않고 기존 용어를 링크한다",
      "f4·열린 질문은 oq-009(교대조별 작업자 수와 로봇·작업대 수)와 관련된다. 해결로 바꾸지 않고 열림을 유지한다",
      "f22~f29 는 트랙 nl-task-chatbot 반영 제안 6건과 같은 출처를 재사용한다(ref-272·ref-275·ref-279·ref-176·ref-278·ref-356·ref-351·ref-353·ref-417·ref-418). 기존 ref id 를 그대로 쓴다"
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
    "f7: 'SEMIAUTOMATIC 에서 운영자가 HMI로 실행을 확인해야 한다'와 'INTERVENED 에서 새 주문을 받지 않는다'를 본문·용어집에서 삭제한다 — 입력 원문(ref-031 6.6.6절 표 10·11)과 다르다. 운용 모드를 서술하려면 표 10·11 그대로 쓴다: SEMIAUTOMATIC 은 관제가 제어하고 주행 속도는 HMI가, 조향은 자동으로 제어한다. INTERVENED 는 운영자가 HMI로 조향·속도·하역 장치를 제어하며, 관제는 복귀 뒤 실행될 주문을 보낼 수 있고 즉시 동작은 cancelOrder 만 보낼 수 있다. MANUAL 은 관제가 주문·동작을 보내지 않는다. 이 문장만 [사실][^ref-031] 로 쓸 수 있다(검증자가 입력 원문으로 확인).",
    "f30: 확인 유형에서 'VDA 5050 SEMIAUTOMATIC 의 실행 전 운영자 확인' 항목을 빼고, 작업자 동작마다의 확인(음성 체크 디지트)과 자연어 지시의 해석 확인(되묻기·실행 전 게이트)의 두 유형으로 [추정] 서술한다 — 근거 f7 이 원문과 불일치한다.",
    "용어집 후보 '운용 모드' 정의에서 '운영자 확인이 필요한지'를 'HMI가 주행 속도를 제어하는지'로 고친다 — f7 불일치를 반영한다.",
    "열린 질문 후보 3('SEMIAUTOMATIC 모드의 실행 확인을 원격으로 할 수 있는지')은 등록하지 않는다 — 전제인 f7 이 원문과 다르다.",
    "f15: [사실] → [추정]으로 강등한다 — 근거가 기사(ref-474) 단일 출처이고 가이드 원문과 대조하지 않았다.",
    "f20: '44건'을 쓰지 않고 분석 건수는 '미확인'으로 두며 [사실] → [추정]으로 강등한다 — 검증 검색 요약은 '35건 선정'으로 브리프와 다르다.",
    "f11: '운전 모드·제동 같은 안전 기능 요구'를 삭제하고 판·대체·적용 범위(충전소·적재물 인계 스테이션 포함)만 [사실]로 쓴다 — 삭제한 부분은 근거 발췌에 없다.",
    "f13: '3부(사용자 책임)'에 '발행 여부 미확인'을 병기한다 — 근거 공지는 2부만 다룬다.",
    "f12: 7절에서 ISO 10218:2025 개정 내용 뒤에 'A3 해설 기준, ISO 원문 미열람'을 병기한다 — 출처가 발행 기관(ISO)이 아니다.",
    "f28: '물류 현장 평가는 없다'를 '초록에서 물류 현장 평가는 확인되지 않는다'로 바꾼다 — 부재를 확인하지 않았다.",
    "f3·f17·f26: 결과가 저자 계산 실험·가정·실험실 환경 기준임을 문장에 병기한다 — 물류 현장 결과로 읽히지 않게 하기 위해서다.",
    "f21·f23·f24·f29: 본문에서 [추정]에 '벤더 주장'을 병기한 상태를 유지한다(f29 는 '연계 대상: ' 표시도 유지한다).",
    "7·9절: f11~f16 의 안전 표준·국내 가이드·KS 는 로봇 제조사·현장 통합사의 안전 기능 요구로 서술하고, ROP 쪽 역할은 f31 의 [추정](운용 모드·안전 상태 표시, 재개·수동 전환 승인 흐름, 구역·권한 반영)으로만 쓴다. 10절에서 25. 안전·위험 관리로 연결한다 — 분류 원문 9장 경계에 따른 것이다.",
    "10절: f24~f28 은 27. AI·학습·적응과 모델 운영과 양쪽으로 연결한다 — 공통 규칙 5(교차 규칙)에 따른 것이다.",
    "각주: fetched:false 인 모든 출처(ref-467~ref-480, ref-272, ref-275, ref-279, ref-176, ref-278, ref-351, ref-353, ref-356, ref-417, ref-418)의 각주 정의에서 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 해당 항목에 source_unopened: true 를 넣는다. ref-031·ref-051·ref-302·ref-104 는 GitHub 원문을 열었으므로 붙이지 않는다.",
    "ref-477·ref-471·ref-474 발행일은 각주에 '미확인'으로 적는다(브리프의 2017 추정은 쓰지 않는다)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 2건(f7, f20), 교차 확인 0건. 강등: f7 사실 → 추정(VDA 5050 SEMIAUTOMATIC·INTERVENED 설명이 명세 표 10·11과 불일치해 원문대로 고쳐 씀), f15 사실 → 추정(기사 단일 출처), f20 사실 → 추정(분석 건수 44건/35건 불일치, 미확인). 원문 미열람 출처: ref-467~ref-480, ref-272, ref-275, ref-279, ref-176, ref-278, ref-351, ref-353, ref-417, ref-418(ref-356 은 검증자가 GitHub 원문으로 f25 를 확인함). 검증자가 GitHub 원문으로 확인한 것은 ref-051(state.schema), ref-302(rmf-web), ref-104(rmf_demos)와 입력 원문 ref-031 이다. 검증 검색 2회로 ref-469(IISE Transactions 58(3), 2025-06-02 온라인)와 ref-479 가 실재함을 확인했다. 리서치와 검증을 합친 검색은 30회로 상한에 도달했다. 주의: 사람 피커–로봇 대기에 관한 근거는 논문 모델·계산 실험 기준이며 국내 현장 실측은 없다. 안전 표준(ISO 3691-4, ISO 10218:2025, R15.08)은 원문을 열지 못했고 ISO 10218 은 A3 해설 기준이다. 안전 기능은 연계 대상이며 ROP 역할(f31)은 추정이다. 원격 조작 관련 근거는 없다. 정정 요청 없음. oq-009 는 해결로 바꾸지 않는다.",
  "retry_reason": null
}
```

### runs/2026-09-25-46/pages.json

```json
{
  "run_id": "2026-09-25-46",
  "outline": [
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "사람 피커와 AMR의 협동 피킹은 피커의 비생산적 보행을 줄이려는 구성이며, 연구는 두 자원의 조율을 배치·순서와 작업 완료 시각 문제로 다룬다. [사실][^ref-467][^ref-468]",
      "planned_findings": [
        "f1",
        "f2",
        "f5",
        "f6",
        "f8",
        "f20"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 650,
      "summary": "이 영역의 기본 용어는 VDA 5050 운용 모드·안전 상태, 협동 적용, 팬아웃, 상황 인식 기반 에이전트 투명성, 음성 피킹 확인이다. [사실][^ref-051]",
      "planned_findings": [
        "f6",
        "f8",
        "f12",
        "f18",
        "f19",
        "f22"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 800,
      "summary": "피킹 단계에서 구역 피커가 배치를 채워 교차 통로에서 기다리는 AMR에 넘기는 가상 시나리오로 여섯 항목을 채운다. [사실][^ref-467]",
      "planned_findings": [
        "f1",
        "f3",
        "f5",
        "f8",
        "f21",
        "f22",
        "f31"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1300,
      "summary": "접근법은 협동 피킹 조율 모델, 로봇이 보고하는 운용 모드·안전 상태, 관제 대시보드, 실패 설명·투명성, 작업자 확인과 자연어 지시 되묻기로 나뉜다. [사실][^ref-468][^ref-051]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f17",
        "f18",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 700,
      "summary": "로봇–관제 인터페이스 VDA 5050, 관제 대시보드 Open-RMF, 안전 표준 ISO 3691-4·ISO 10218·R15.08, 국내 가이드·KS가 이 영역과 이어진다. [사실][^ref-051][^ref-470]",
      "planned_findings": [
        "f6",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f25",
        "f31"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 600,
      "summary": "협동 피킹 조율 논문 3건과 운영자 감독·설명 연구, 되묻기·실행 전 게이트 연구가 대표 자료다. [사실][^ref-469][^ref-478]",
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f17",
        "f19",
        "f20",
        "f26",
        "f27",
        "f28",
        "f21"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 550,
      "summary": "안전 기능은 로봇 제조사·현장 통합사의 연계 대상이고, ROP는 운용 모드·안전 상태 표시와 재개·수동 전환 승인 흐름, 구역·권한 반영을 맡는 경계가 될 것으로 보인다. [추정][^ref-051][^ref-470]",
      "planned_findings": [
        "f31",
        "f29",
        "f10",
        "f5"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 600,
      "summary": "배정·순서·처리능력 계획, 관제 연동, 모니터링·예외 복구, 안전, AI 영역과 연결된다.",
      "planned_findings": [
        "f1",
        "f4",
        "f6",
        "f10",
        "f17",
        "f11",
        "f24",
        "f28"
      ]
    },
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "section": "11. 열린 질문",
      "budget_chars": 400,
      "summary": "oq-009와 새 질문 3건(국내 KS 내용, 국내 대기 실측, 관제 요원당 감독 로봇 수)이 열려 있다.",
      "planned_findings": [
        "f16",
        "f5",
        "f19"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 관제 대시보드, 안전 표준·국내 가이드, 설명·감독, 트랙 자연어 업무 지시 챗봇 반영 제안 6건 검토 반영), 페이지 상태 자동 영역 추가. 2차: 9절 시설·설비 제어 행을 [추정]으로 낮추고 Open-RMF 데모 내용을 따로 적음"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area18-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 \"6. 대표 접근법과 기술\" 절을 옮겼다. 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 기준 경로로 고침. 2차: 운용 모드 소절 마지막 문장을 [사실]과 [추정]으로 나눔"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area18-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,079자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area18-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 \"4. 핵심 개념과 용어\" 절(897자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area18-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 \"8. 대표 연구와 자료\" 절(750자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 18. 사람–로봇 협업·운영 인터페이스 | 3~11절 신규 작성: 협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 관제 대시보드, 안전 표준·국내 가이드, 설명·감독, 트랙 반영 제안 6건 검토 | run 2026-09-25-46",
  "index_updates": {
    "home_recent": "2026-09-25 — 18. 사람–로봇 협업·운영 인터페이스: 영역 심화 초안 작성(협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 안전 표준·국내 가이드, 자연어 지시 확인 방식)",
    "category_recent": "2026-09-25 — 18. 사람–로봇 협업·운영 인터페이스: 3~11절 신규 작성, 피킹 단계 시나리오와 ROP 직접·연계 범위 정리",
    "area_recent": "2026-09-25 — 18. 사람–로봇 협업·운영 인터페이스: 3~11절 신규 작성(트랙 자연어 업무 지시 챗봇 반영 제안 6건을 6·8절에 검토 반영)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "fan-out",
      "term_ko": "팬아웃",
      "term_en": "Fan-out (human-robot team)",
      "definition": "한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수로, 로봇의 방치 허용도와 로봇 하나를 다루는 상호작용 시간으로 추정한다.",
      "related_areas": [
        18,
        19
      ],
      "sources": [
        "ref-478"
      ]
    },
    {
      "action": "new",
      "slug": "operating-mode",
      "term_ko": "운용 모드",
      "term_en": "Operating Mode (VDA 5050 operatingMode)",
      "definition": "VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, HMI가 주행 속도를 제어하는지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다.",
      "description": "상태 메시지의 operatingMode 는 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값이다(2026-09-25 확인).",
      "related_areas": [
        9,
        18
      ],
      "sources": [
        "ref-051",
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "situation-awareness-based-agent-transparency",
      "term_ko": "상황 인식 기반 에이전트 투명성",
      "term_en": "Situation Awareness-based Agent Transparency (SAT)",
      "definition": "자율 에이전트의 현재 행동·계획, 추론, 미래 결과 예측을 세 수준으로 운영자에게 보여 주어 상황 인식과 신뢰를 돕는 인터페이스 설계 모델이다.",
      "related_areas": [
        18,
        19
      ],
      "sources": [
        "ref-477"
      ]
    },
    {
      "action": "new",
      "slug": "collaborative-application",
      "term_ko": "협동 적용",
      "term_en": "Collaborative Application",
      "definition": "ISO 10218:2025 에서 로봇 자체가 아니라 사람과 로봇이 함께 일하도록 설계된 적용 방식을 기준으로 안전을 판단하기 위해 '협동로봇' 대신 쓰는 용어이다.",
      "description": "A3 해설 기준이며 ISO 원문은 미열람이다.",
      "related_areas": [
        18,
        25
      ],
      "sources": [
        "ref-471"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-467",
      "org": "Žulj, I., Salewski, H., Goeke, D., & Schneider, M.",
      "title": "Order batching and batch sequencing in an AMR-assisted picker-to-parts system",
      "published": "2022",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 구역별 피커가 배치를 채워 교차 통로의 AMR에 넘기는 AMR 보조 피킹에서 배치 구성·순서를 최적화한 EJOR 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-468",
      "org": "Löffler, M., Boysen, N., & Schneider, M.",
      "title": "Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers",
      "published": "2023",
      "url": "https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 선반 앞에서 기다리는 AMR과 여러 피커의 조율을 makespan 최소화로 다룬 Transportation Science 57(4) 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-469",
      "org": "Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M.",
      "title": "Deploying pickers and robots in cobot-based collaborative order picking systems",
      "published": "2026-03",
      "url": "https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 네 가지 사람–로봇 협동 피킹 모드를 포크–조인 대기행렬 네트워크와 피로–회복 모델로 분석해 피커·로봇 투입 수를 정하는 IISE Transactions 58(3) 논문(온라인 2025-06-02).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업용 트럭(AGV·AMR)과 그 시스템의 안전 요구·검증 표준 제2판 소개 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md",
        "docs/topics/2026/2026-09-25-area18-s6.md"
      ]
    },
    {
      "id": "ref-471",
      "org": "A3(Association for Advancing Automation)",
      "title": "Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs)",
      "published": null,
      "url": "https://www.automate.org/robotics/blogs/updated-iso-10218-faq",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 10218-1/2:2025 개정의 주요 변경(협동 적용 통합, 기능 안전, 사이버보안)을 설명하는 로봇 산업 협회 자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-472",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available",
      "published": "2023-10",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 이동로봇 시스템·적용의 현장 통합 안전 요구(R15.08-2) 발행을 알리는 표준 개발 기관 공지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-473",
      "org": "고용노동부",
      "title": "고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포",
      "published": "2023-07",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 고용노동부·한국산업안전보건공단의 고정식·이동식 산업용 로봇 협동작업 안전 가이드 게시 자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-474",
      "org": "로봇신문",
      "title": "'이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나?",
      "published": null,
      "url": "https://www.irobotnews.com/news/articleView.html?idxno=32130",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 2023-07 이동식 산업용 로봇 안전 가이드의 충돌방지·비상정지 내용을 소개한 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-475",
      "org": "중소벤처기업부(대한민국 정책브리핑)",
      "title": "｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!",
      "published": "2024-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 대구 규제자유특구 실증을 거친 이동식 협동로봇 안전기준 KS 제정을 알린 보도자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-476",
      "org": "Das, D., Banerjee, S., & Chernova, S.",
      "title": "Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery",
      "published": "2021-01",
      "url": "https://arxiv.org/abs/2101.01625",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 실행 실패를 비전문가에게 설명하는 설명 유형을 비교·자동 생성한 HRI 2021 논문의 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-477",
      "org": "Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science)",
      "title": "Situation awareness-based agent transparency and human-autonomy teaming effectiveness",
      "published": null,
      "url": "https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 에이전트의 행동·추론·예측을 세 수준으로 보여 주는 SAT 모델과 그 효과를 정리한 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-478",
      "org": "Olsen, D. R. 외(CHI 2004)",
      "title": "Fan-out: measuring human control of multiple robots",
      "published": "2004",
      "url": "https://dl.acm.org/doi/10.1145/985692.985722",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한 사람이 동시에 다룰 수 있는 로봇 수(팬아웃)를 방치 허용도와 상호작용 시간으로 재는 척도를 제안한 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-479",
      "org": "Rey-Becerra, E., & Wischniewski, S.",
      "title": "Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance",
      "published": "2025-07-11",
      "url": "https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한 사람이 여러 로봇을 감독하는 시스템 연구를 고찰한 Ergonomics 논문(BAuA). 분석 건수는 미확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-480",
      "org": "ZDNet Korea",
      "title": "\"대형 물류센터 집품 작업, 로봇 6대로 효율화\"",
      "published": "2023-12-22",
      "url": "https://zdnet.co.kr/view/?no=20231222165139",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 플로틱스의 존피킹 로봇 시연(작업자 2명·로봇 6대)을 전한 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 최신판(3.0.0) 명세 원문. 이번 실행에서 운용 모드별 설명(6.6.6절 표 10·11)을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 상태 메시지 JSON 스키마 원본. 이번 실행에서 operatingMode·paused·safetyState 정의를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 배치를 웹에서 시각화·제어하는 패키지 모음(API 서버·클라이언트·대시보드)의 공식 README.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 데모 README. 웹 대시보드 연동과 비상 경보 시 로봇의 주차 위치 이동을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-272",
      "org": "Lucas Systems",
      "title": "Voice-Directed Warehousing - Solutions | Lucas Systems",
      "published": null,
      "url": "https://www.lucasware.com/voice-directed-warehousing/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 음성 지시 창고 작업(음성 피킹)과 체크 디지트 확인 방식을 설명하는 벤더 자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-275",
      "org": "USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.)",
      "title": "System and method for generating and updating location check digits (US 8868519)",
      "published": null,
      "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 위치 체크 디지트 생성·갱신과 불일치 경고를 기술한 미국 특허 공보.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-279",
      "org": "Locus Robotics",
      "title": "Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface)",
      "published": null,
      "url": "https://locusrobotics.com/locusone/automated-warehouse-software/user-interface",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 협동 피킹 로봇의 작업자용 화면 인터페이스를 소개하는 벤더 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-176",
      "org": "InOrbit.AI",
      "title": "InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024",
      "published": "2024-05",
      "url": "https://www.inorbit.ai/press/inorbit-robops-copilot",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RobOps Copilot 발표 보도자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-278",
      "org": "InOrbit.AI",
      "title": "InOrbit RobOps Copilot - Bring AI power to robot operations",
      "published": null,
      "url": "https://www.inorbit.ai/robopscopilot",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. RobOps Copilot 제품 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z. 외",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 등각 예측으로 LLM 계획기의 불확실성을 재어 도움을 요청하게 하는 KnowNo 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-353",
      "org": "Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S.",
      "title": "CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents",
      "published": "2024",
      "url": "https://arxiv.org/abs/2306.10376",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 사용자 명령을 명확·모호·수행 불가로 분류하고 되묻는 CLARA 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-356",
      "org": "Rasa Technologies (RasaHQ/rasa GitHub)",
      "title": "Forms — Rasa documentation (docs/docs/forms.mdx)",
      "published": null,
      "url": "https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이번 실행에서 다시 열지 않았다. 필수 슬롯을 채울 때까지 되묻는 Rasa 폼 문서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-417",
      "org": "Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 이 해석한 명령의 안전 속성을 실행 전 결정적 게이트로 판정하는 SafeGate 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    },
    {
      "id": "ref-418",
      "org": "Mecalux",
      "title": "Mecalux integrates generative AI into Easy WMS",
      "published": null,
      "url": "https://www.mecalux.com/news/generative-ai-easy-wms-mecalux",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. WMS 의 생성형 AI 대화형 비서 기능을 알리는 벤더 뉴스.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가?",
      "areas": [
        18,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가?",
      "areas": [
        18,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가?",
      "areas": [
        18,
        19
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "18. 사람–로봇 협업·운영 인터페이스"
    },
    {
      "step": "피킹",
      "item": "작업 대상",
      "link": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "18. 사람–로봇 협업·운영 인터페이스"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "18. 사람–로봇 협업·운영 인터페이스"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "18. 사람–로봇 협업·운영 인터페이스"
    },
    {
      "step": "피킹",
      "item": "완료·인계",
      "link": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "18. 사람–로봇 협업·운영 인터페이스"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시",
      "title": "18. 사람–로봇 협업·운영 인터페이스"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/83545.html",
      "related_areas": [
        18,
        25
      ],
      "summary": "무인 산업용 트럭과 그 시스템(차량, 제어 시스템, 하역 장치, 배터리 충전소, 적재물 인계 스테이션)의 안전 요구를 정한 제2판(2020판 대체). 원문 미열람.",
      "ref_id": "ref-470"
    },
    {
      "name": "ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합)",
      "kind": "표준",
      "org": "ISO (A3 해설 경유)",
      "url": "https://www.automate.org/robotics/blogs/updated-iso-10218-faq",
      "related_areas": [
        18,
        25
      ],
      "summary": "협동 적용 안전 요구를 본문에 넣어 ISO/TS 15066 내용을 흡수하고 기능 안전을 명확히 하며 사이버보안 요구를 더한 개정판. A3 해설 기준, ISO 원문 미열람.",
      "ref_id": "ref-471"
    },
    {
      "name": "ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준",
      "kind": "표준",
      "org": "A3(Association for Advancing Automation)",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "related_areas": [
        18,
        25
      ],
      "summary": "IMR 또는 IMR 플릿을 현장에 통합·설정하는 안전 요구(2023-10). 원문 미열람.",
      "ref_id": "ref-472"
    },
    {
      "name": "고정식·이동식 산업용 로봇의 협동작업 안전 가이드",
      "kind": "프레임워크",
      "org": "고용노동부·한국산업안전보건공단",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065",
      "related_areas": [
        18,
        25
      ],
      "summary": "감지기 활용 충돌방지 조치, 작업자 이동·작업 방법, 점검표, 이동식 로봇 예시를 제시한 2023-07 안전 가이드. 원문 미열람.",
      "ref_id": "ref-473"
    },
    {
      "name": "이동식 협동로봇 안전기준 KS(표준 번호 미확인)",
      "kind": "표준",
      "org": "중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구)",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517",
      "related_areas": [
        18,
        25
      ],
      "summary": "규제자유특구 실증을 거쳐 2024-11 제정된 이동식 협동로봇 안전기준 한국산업표준. 번호·본문 미확인.",
      "ref_id": "ref-475"
    },
    {
      "name": "Open-RMF rmf_demos",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_demos",
      "related_areas": [
        18,
        20
      ],
      "summary": "웹 대시보드 작업 제출·상태 감시와 비상 경보 시 로봇의 가장 가까운 주차 위치 이동을 보여 주는 Open-RMF 데모.",
      "ref_id": "ref-104"
    }
  ],
  "additional_research_requests": [
    "6절 원격 조작(teleoperation): 분류 원문 정의에 있으나 공개 근거가 없어 쓰지 못했다. 물류 이동로봇의 원격 조작 방식·표준·연구 자료가 필요하다.",
    "7·11절: 이동식 협동로봇 안전기준 KS 의 표준 번호와 본문(KSSN 등) 확인이 필요하다.",
    "7절: ISO 10218-1·10218-2:2025 개정 내용을 ISO 공식 자료로 확인해야 한다(현재 A3 해설 기준).",
    "7절: ANSI/A3 R15.08-3(사용자 책임) 발행 여부 확인이 필요하다.",
    "8절: Rey-Becerra·Wischniewski(2025)의 분석 건수(44건/35건)와 설계·평가 점검표 제시 여부를 원문으로 확인해야 한다.",
    "8·11절: Yang 외(2026) 모델이 교대조 단위 인원·로봇 수 결정을 다루는지(oq-009 해결 여부) 원문 확인이 필요하다.",
    "9절: 시설 비상 경보를 받았을 때 오케스트레이션 계층(ROP)이 맡는 역할을 정한 표준·사례가 필요하다(현재는 Open-RMF 데모 기능만 근거).",
    "6·8절: 트랙 반영 제안 가운데 이번 브리프에 없는 자료(Formant F3, 다임리서치 다비스, Amazon Proteus 2026-06 발표, Locus Aila 사례 ref-280, CLARA ref-352, KnowNo ref-350, 작업 지향 대화 서베이 ref-357)는 브리프에 없어 넣지 못했다. 다음 실행에서 재확인 후 반영을 검토한다.",
    "5절: 국내 물류센터의 피커 유휴·로봇 대기 실측 자료가 필요하다.",
    "퍼블리셔 담당 요청: 사전 검사에서 보고된 logs/daily/2026-09-25.md 의 깨진 링크 ../glossary/hierarchical-task-network.md 는 이번 스토리텔러 산출 페이지가 아니라 일일 로그(퍼블리셔 생성)에 있으므로 이 출력으로 고칠 수 없다. 용어집 항목 생성 또는 로그 링크 제거가 필요하다."
  ],
  "fixes_applied": [
    "f7 운용 모드 설명 교정 — 'SEMIAUTOMATIC 운영자 HMI 실행 확인'과 'INTERVENED 새 주문 불수신'을 본문·용어집에서 빼고, 6절에 명세 표 10·11 그대로(SEMIAUTOMATIC 관제 제어·속도 HMI·조향 자동, INTERVENED 운영자 HMI 제어·복귀 뒤 실행될 주문 수신·즉시 동작은 cancelOrder 만, MANUAL 주문·동작 불가)를 [사실][^ref-031]로 썼다.",
    "f30 확인 유형 — 6절에서 VDA 5050 SEMIAUTOMATIC 항목을 빼고 작업자 동작마다의 확인과 자연어 지시의 해석 확인 두 유형으로 [추정] 서술했다(각주에서 ref-031 제외).",
    "용어집 '운용 모드' 정의 — '운영자 확인이 필요한지'를 'HMI가 주행 속도를 제어하는지'로 고쳐 glossary_updates 에 냈다.",
    "열린 질문 후보 3(SEMIAUTOMATIC 원격 확인) — 11절과 open_question_updates 에 등록하지 않았다.",
    "f15 강등 — 7절 국내 가이드 행에서 비상정지장치 위치 내용을 '보도에 따르면 … [추정]'으로 썼다.",
    "f20 강등 — 3·8절에서 '44건'을 쓰지 않고 분석 건수 미확인으로 두었으며 [추정]으로 썼다(검증되지 않은 점검표 제시도 넣지 않음).",
    "f11 — 7절 ISO 3691-4 행에서 '운전 모드·제동'을 빼고 판·대체·적용 범위(충전소·적재물 인계 스테이션 포함)만 [사실]로 썼다.",
    "f13 — 7절 R15.08 행에 '사용자 책임(3부, 발행 여부 미확인)'을 병기했다.",
    "f12 — 4절 협동 적용과 7절 ISO 10218 행에 'A3 해설 기준, ISO 원문 미열람'을 병기했다.",
    "f28 — 6절 SafeGate 문장을 '초록에서 물류 현장 평가는 확인되지 않는다'로 바꿨다.",
    "f3·f17·f26 — 5·6·8절에 '저자 계산 실험 기준', '가정 환경 실험', '가정·실험실 환경'을 병기했다.",
    "f21·f23·f24·f29 — 5·6·9절에서 [추정] 벤더 주장 병기를 유지했고 f29 에 '연계 대상: ' 표시를 유지했다.",
    "7·9절 경계 — 안전 표준·국내 가이드·KS를 로봇 제조사·현장 통합사의 안전 기능 요구로 서술하고 ROP 역할은 f31 [추정](모드·안전 상태 표시, 재개·수동 전환 승인, 구역·권한 반영)으로만 썼으며 10절에서 25. 안전·위험 관리로 연결했다.",
    "10절 — f24~f28 을 27. AI·학습·적응과 모델 운영과 연결했다(6절 본문에도 링크).",
    "각주 — fetched:false 출처 전부의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-031·ref-051·ref-302·ref-104 는 붙이지 않았다.",
    "ref-477·ref-471·ref-474 발행일 — 각주 발행일을 '미확인'으로 적고 2017 추정은 쓰지 않았다.",
    "분량 초과 자동 분리: 18. 사람–로봇 협업·운영 인터페이스 본문 7,496자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,795자",
    "형식 검증 재작성: docs/topics/2026/2026-09-25-area18-s6.md 의 깨진 링크 ../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md 를 주제 페이지 기준 경로 ../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md 로 고쳤다. 세부영역 페이지 4절 첫 항목의 빠진 목록 기호('- ')를 보정했다. 주장·태그·각주는 바꾸지 않았다. logs/daily/2026-09-25.md 의 깨진 링크는 스토리텔러 산출물이 아니어서 고치지 못했다(additional_research_requests 에 기록).",
    "2차: 세부영역 페이지 9절 '시설·설비 제어' 행 — 'ROP가 직접 맡는 것' 칸을 '시설 비상 경보 상태를 받아 작업 흐름에 반영하는 것으로 보인다. [추정][^ref-104]'로 낮추고, Open-RMF 데모 내용은 '(Open-RMF 데모는 경보 시 로봇을 가장 가까운 주차 위치로 보낸다) [사실][^ref-104]'로 따로 적었으며 '멈추고'를 삭제했다.",
    "2차: 주제 페이지 docs/topics/2026/2026-09-25-area18-s6.md 3절 '운용 모드·일시정지·비상정지 보고' 소절 마지막 문장을 '안전 상태와 일시정지는 로봇이 보고하는 값이다. [사실][^ref-051]'과 '운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이 될 것으로 보인다. [추정][^ref-051][^ref-470]'으로 나눴고, ref-470 각주 정의와 프런트매터 sources 를 그 페이지에 더했다."
  ]
}
```

### runs/2026-09-25-46/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-46/pages/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md

```markdown
---
title: "18. 사람–로봇 협업·운영 인터페이스"
type: area
category: "E. 협업·현장 운영"
area_no: 18
related_areas: [1, 3, 4, 9, 13, 14, 19, 20, 25, 27]
tags: [협동 피킹, VDA 5050 운용 모드, 안전 상태 표시, 운영자 감독, 작업자 확인]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-467, ref-468, ref-469, ref-470, ref-471, ref-472, ref-473, ref-474, ref-475, ref-476, ref-477, ref-478, ref-479, ref-480, ref-031, ref-051, ref-302, ref-104, ref-272, ref-275, ref-279, ref-176, ref-278, ref-351, ref-353, ref-356, ref-417, ref-418]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [E. 협업·현장 운영](index.md) › 18. 사람–로봇 협업·운영 인터페이스

# 18. 사람–로봇 협업·운영 인터페이스

!!! info "소속 대분류"
    [E. 협업·현장 운영](index.md) — 핵심 질문:
    계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [분류원문]

## 2. SCM 관점의 질문

사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [분류원문]

## 3. 왜 중요한가

사람 피커와 자율이동로봇(Autonomous Mobile Robot, AMR)이 함께 피킹하는 방식은 AMR이 운반을 맡아 피커의 비생산적 보행 시간을 줄이려는 구성이며, 연구들은 두 자원의 조율을 배치 구성·순서와 작업 완료 시각(makespan) 최소화 문제로 다룬다. [사실][^ref-467][^ref-468]

이 연구들을 분류 원문의 질문에 대응시키면, 서로 기다리지 않게 하는 일은 인터페이스 하나로 풀리지 않고 구역·배치 구성, 피커와 로봇의 수 비율, 로봇 속도, 다음 작업 안내가 함께 맞아야 하는 것으로 보인다. 이 대응은 이 위키의 정리다. [추정][^ref-467][^ref-468][^ref-469]

운영 인터페이스는 사람의 개입 상태를 관제와 주고받는 접점이기도 하다. VDA 5050 상태 메시지는 로봇의 운용 모드와 비상정지·보호 필드 침범 같은 안전 상태를 보고하게 한다(2026-09-25 확인). [사실][^ref-051] 한 사람이 여러 로봇을 감독하는 시스템에 대한 문헌 고찰은 효율·유연성의 이점과 함께 주의·인지 부하 관리의 어려움을 지적했다. [추정][^ref-479]

## 4. 핵심 개념과 용어

- **운용 모드(operating mode)** — [VDA 5050](../../glossary/vda-5050.md) 상태 메시지의 operatingMode 로, STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값 가운데 하나를 보고한다(2026-09-25 확인). [사실][^ref-051]
- **안전 상태(safetyState)·일시정지(paused)** — 비상정지 종류(로봇에서 수동 확인하는 MANUAL, 시설 비상정지를 원격 확인하는 REMOTE, NONE)와 보호 필드 침범을 필수로 보고하고, 물리 버튼이나 즉시 동작(instantAction)으로 멈춘 상태를 따로 보고한다. [사실][^ref-051]

자세한 내용은 주제 페이지 [18. 사람–로봇 협업·운영 인터페이스 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area18-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹

**시나리오:** 구역 피커가 채운 배치를 교차 통로에서 기다리는 AMR에 넘겨 출하 거점으로 보낸다

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출고 주문이 배치로 묶여 피킹 구역에 내려온다(가상). 배치 구성과 배치 순서는 피커–AMR 조율에서 함께 정하는 결정 변수로 다뤄진다. [사실][^ref-467] |
| 작업 대상 | 주문 용기에 담기는 피킹 품목과 완성된 배치(가상) |
| 수행 자원 | 구역마다 피커 1명이 통로에서 배치를 채워 교차 통로에서 기다리는 AMR에 넘기고, AMR이 출하 거점까지 운반한다. [사실][^ref-467] ROP 운영 인터페이스는 다음 대기 로봇 위치와 넘길 배치를 작업자에게 전달하는 접점이 될 것으로 보인다. [추정][^ref-468][^ref-469] |
| 제약 | 사람과 로봇이 통로를 함께 쓰므로 사람 감지·비상정지 같은 안전 기능이 필요하며, 이는 로봇 제조사·현장 통합사가 갖추는 연계 대상으로 보인다. [추정][^ref-470][^ref-472] |
| 완료·인계 | 음성 피킹이라면 작업자가 위치 체크 디지트·수량을 짧게 응답해 동작마다 확인한다. [사실][^ref-272][^ref-275] 배치를 AMR에 넘긴 시점을 인계로 본다(가상). |
| 예외·성과 | 피킹 시간이 들쭉날쭉하면 대기가 연쇄로 번지는데, 작업자를 작은 하위 집단으로 나누면 줄일 수 있고 AMR이 피커보다 느리면 성과가 나빠진다는 결과가 있다(저자 계산 실험 기준). [사실][^ref-468] 로봇이 비상정지되거나 일시정지되면 그 상태를 안전 상태로 보고한다. [사실][^ref-051] |

다음은 설명을 위한 가상의 시나리오이다. 피커는 자기 구역에서만 움직이고, 운반은 AMR이 맡는다. 이 영역이 관여하는 칸은 수행 자원(누가 어디서 기다리는가), 완료·인계(무엇으로 확인하는가), 예외·성과(멈춘 로봇을 사람이 어떻게 알아보는가)이다.

국내에서는 한 물류 로봇 업체가 100평 규모 환경에서 작업자 2명이 로봇 6대와 존피킹하는 구성을 시연했다고 보도되었다(2023-12). [추정] 벤더 주장[^ref-480] 국내 현장에서 피커 유휴·로봇 대기를 실측한 공개 자료는 이번 조사에서 찾지 못했다(11절).

## 6. 대표 접근법과 기술

접근법은 협동 피킹 조율 모델, 로봇이 보고하는 운용 모드·안전 상태, 관제 대시보드, 실패 설명·투명성, 작업자 확인과 자연어 지시의 되묻기로 나뉜다. [사실][^ref-468][^ref-051]

자세한 내용은 주제 페이지 [18. 사람–로봇 협업·운영 인터페이스 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area18-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

로봇–관제 인터페이스 VDA 5050, 관제 대시보드 Open-RMF, 사람과 이동로봇이 함께 일하는 현장의 안전 표준과 국내 가이드·KS가 이 영역과 이어진다. [사실][^ref-051][^ref-470]

자세한 내용은 주제 페이지 [18. 사람–로봇 협업·운영 인터페이스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area18-s7.md)에 있다.

## 8. 대표 연구와 자료

협동 피킹 조율 논문과 운영자 감독·실패 설명 연구, 자연어 지시의 되묻기·실행 전 게이트 연구가 이 영역의 대표 자료다. [사실][^ref-469][^ref-478]

자세한 내용은 주제 페이지 [18. 사람–로봇 협업·운영 인터페이스 — 대표 연구와 자료](../../topics/2026/2026-09-25-area18-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고하는 운용 모드·안전 상태·일시정지의 표시, 작업 재개·수동 전환의 승인 흐름, 구역·권한 설정 반영 [추정][^ref-051] | 사람 감지·보호 필드·비상정지 회로·속도와 거리 감시(로봇 제조사·현장 통합사) [추정][^ref-470][^ref-472] |
| 시설·설비 제어 | 시설 비상 경보 상태를 받아 작업 흐름에 반영하는 것으로 보인다. [추정][^ref-104] (Open-RMF 데모는 경보 시 로봇을 가장 가까운 주차 위치로 보낸다) [사실][^ref-104] | 시설 비상정지와 설비 안전 제어(연계 대상) |
| 상위 업무 시스템 | 조율 결과(다음 대기 로봇 위치, 넘길 배치)를 작업자에게 전달 [추정][^ref-467][^ref-468] | 연계 대상: WMS 화면과 대화형 비서 [추정] 벤더 주장[^ref-418] |

이종 제조사를 연결하는 ROP는 안전 기능 자체를 만들지 않고, 로봇이 보고한 상태를 사람에게 보여 주고 사람의 승인·전환을 작업 흐름에 반영하는 경계가 될 것으로 보인다. [추정][^ref-051][^ref-470] 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

- [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md) — WMS 화면·대화형 비서는 상위 업무 시스템 쪽 연계 대상이다.
- [3. 처리능력·거점·설비 계획](../a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) — 피커·로봇 투입 수 분석이 교대조별 인원·로봇 계획(oq-009)과 이어진다.
- [4. 성과·경제성·프로세스 개선](../a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) — 피커 유휴·로봇 대기 실측이 성과 지표와 이어진다.
- [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) — 운용 모드·안전 상태는 VDA 5050 상태 메시지로 들어온다.
- [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md) — 피커와 AMR의 짝짓기는 배정 문제다.
- [14. 작업 순서·스케줄링](../d-planning-and-optimization/14-task-sequencing-and-scheduling.md) — 배치 순서와 작업 완료 시각 최소화가 스케줄링 문제다.
- [19. 모니터링·이상 탐지·원인 분석](19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 실패 설명과 투명성 화면이 원인 분석 결과를 사람에게 전달한다.
- [20. 예외 복구·재계획·업무 연속성](20-exception-recovery-replanning-and-business-continuity.md) — 비상 경보 대응과 수동 전환 뒤 재개가 복구 절차와 이어진다.
- [25. 안전·위험 관리](../g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) — ISO 3691-4·ISO 10218·R15.08·국내 가이드·KS의 안전 요구를 다룬다.
- [27. AI·학습·적응과 모델 운영](../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 자연어 질의, 되묻기(KnowNo·CLARA), 실행 전 게이트(SafeGate)는 AI 연구 방법을 이 영역에 적용한 것이다.

## 11. 열린 질문

- **oq-009** (열림) 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? 협동 피킹의 인원·로봇 투입 모델은 찾았으나 교대조 단위 결정 여부는 미확인이다.[^ref-469]
- (새 질문, 열림) 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가?[^ref-475]
- (새 질문, 열림) 국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가?
- (새 질문, 열림) 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가?[^ref-478]

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-467]: Žulj, I., Salewski, H., Goeke, D., & Schneider, M., Order batching and batch sequencing in an AMR-assisted picker-to-parts system, 2022, https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616, 접근일 2026-09-25 (원문 미열람)
[^ref-468]: Löffler, M., Boysen, N., & Schneider, M., Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers, 2023, https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207, 접근일 2026-09-25 (원문 미열람)
[^ref-469]: Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M., Deploying pickers and robots in cobot-based collaborative order picking systems, 2026-03, https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-472]: A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-475]: 중소벤처기업부(대한민국 정책브리핑), ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!, 2024-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517, 접근일 2026-09-25 (원문 미열람)
[^ref-478]: Olsen, D. R. 외(CHI 2004), Fan-out: measuring human control of multiple robots, 2004, https://dl.acm.org/doi/10.1145/985692.985722, 접근일 2026-09-25 (원문 미열람)
[^ref-479]: Rey-Becerra, E., & Wischniewski, S., Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance, 2025-07-11, https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316, 접근일 2026-09-25 (원문 미열람)
[^ref-480]: ZDNet Korea, "대형 물류센터 집품 작업, 로봇 6대로 효율화", 2023-12-22, https://zdnet.co.kr/view/?no=20231222165139, 접근일 2026-09-25 (원문 미열람)
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-272]: Lucas Systems, Voice-Directed Warehousing - Solutions - Lucas Systems, 미확인, https://www.lucasware.com/voice-directed-warehousing/, 접근일 2026-09-25 (원문 미열람)
[^ref-275]: USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.), System and method for generating and updating location check digits (US 8868519), 미확인, https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519, 접근일 2026-09-25 (원문 미열람)
[^ref-418]: Mecalux, Mecalux integrates generative AI into Easy WMS, 미확인, https://www.mecalux.com/news/generative-ai-easy-wms-mecalux, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md

```markdown
---
title: "18. 사람–로봇 협업·운영 인터페이스"
type: area
category: "E. 협업·현장 운영"
area_no: 18
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [E. 협업·현장 운영](index.md) › 18. 사람–로봇 협업·운영 인터페이스

# 18. 사람–로봇 협업·운영 인터페이스

!!! info "소속 대분류"
    [E. 협업·현장 운영](index.md) — 핵심 질문:
    계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [분류원문]

## 2. SCM 관점의 질문

사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [분류원문]

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

### runs/2026-09-25-46/pages/topics/2026/2026-09-25-area18-s6.md

```markdown
---
title: "18. 사람–로봇 협업·운영 인터페이스 — 대표 접근법과 기술"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 18
related_areas: [1, 3, 4, 9, 13, 14, 19, 20, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-051, ref-104, ref-176, ref-272, ref-275, ref-278, ref-279, ref-302, ref-351, ref-353, ref-356, ref-417, ref-418, ref-467, ref-468, ref-469, ref-470, ref-476, ref-477]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#6
---

[홈](../../index.md) › [주제](../index.md) › 18. 사람–로봇 협업·운영 인터페이스 — 대표 접근법과 기술

# 18. 사람–로봇 협업·운영 인터페이스 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 접근법은 협동 피킹 조율 모델, 로봇이 보고하는 운용 모드·안전 상태, 관제 대시보드, 실패 설명·투명성, 작업자 확인과 자연어 지시의 되묻기로 나뉜다. [사실][^ref-468][^ref-051]
- 이 페이지는 [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

접근법은 협동 피킹 조율 모델, 로봇이 보고하는 운용 모드·안전 상태, 관제 대시보드, 실패 설명·투명성, 작업자 확인과 자연어 지시의 되묻기로 나뉜다. [사실][^ref-468][^ref-051]

### 협동 피킹의 조율 모델

- 구역 피커–교차 통로 AMR 인계 구조에서 배치 구성과 순서를 함께 최적화한다(2022). [사실][^ref-467]
- AMR이 주문 용기를 싣고 선반 앞에서 기다리고 피커는 출발점으로 돌아가지 않고 대기 AMR 사이를 옮겨 다니는 방식에서, 여러 AMR·피커 조율을 작업 완료 시각 최소화로 푼다(2023). [사실][^ref-468] 작업자 하위 집단 분할과 속도 균형의 효과는 저자 계산 실험 결과다. [사실][^ref-468]
- 협동 피킹을 로봇1–피커1, 로봇1–피커 다수, 피커1–로봇 다수, 다수–다수의 네 모드로 나누고 포크–조인 대기행렬 네트워크(fork-join queueing network)와 피로–회복 모델로 피커·로봇 투입 수를 분석한다(2026-03 권호). 교대조 단위 결정 여부는 미확인이다. [사실][^ref-469]

### 운용 모드·일시정지·비상정지 보고

VDA 5050 최신판 명세(2026-09-25 확인)에서 SEMIAUTOMATIC 은 관제가 제어하고 주행 속도는 HMI(Human-Machine Interface, 사람–기계 인터페이스)가, 조향은 자동으로 제어한다. INTERVENED 는 운영자가 HMI로 조향·속도·하역 장치를 제어하며, 관제는 복귀 뒤 실행될 주문을 보낼 수 있고 즉시 동작은 cancelOrder 만 보낼 수 있다. MANUAL 에서는 관제가 주문·동작을 보내지 않는다. [사실][^ref-031] 안전 상태와 일시정지는 로봇이 보고하는 값이다. [사실][^ref-051] 운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이 될 것으로 보인다. [추정][^ref-051][^ref-470]

### 관제 대시보드

[Open-RMF](../../glossary/open-rmf.md)의 rmf-web 은 배치를 웹에서 시각화·제어하는 패키지 모음(API 서버·API 클라이언트·대시보드 프레임워크)이다. [사실][^ref-302] 데모(rmf_demos)는 웹 대시보드에서 작업을 제출하고 로봇·작업 상태를 보게 하며, 비상 경보를 켜면 로봇을 가장 가까운 주차 위치로 보낸다. 이는 데모 기능이다. [사실][^ref-104]

### 실패 설명과 투명성

계획 실행 중 실패의 원인을 비전문가에게 설명할 때 실패의 맥락과 지난 행동 이력을 담은 설명이 실패·해결책 파악에 가장 효과적이었다는 결과가 있다(가정 환경 실험, 2021). [사실][^ref-476] SAT 모델은 행동·추론·예측을 단계적으로 보여 주는 화면 설계 틀이다. [사실][^ref-477]

### 작업자 확인과 자연어 지시 (트랙 반영)

[자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) 트랙이 제안한 내용을 검토해 옮긴다. 음성 피킹은 동작마다 짧은 음성 응답으로 확인한다. [사실][^ref-272][^ref-275] 협동 피킹 로봇 화면이 품목·위치·수량을 보여 주고 선택 기능으로 바코드 스캔 뒤 화면 확인을 받는다는 설명이 있다. [추정] 벤더 주장[^ref-279] 로봇 운영 데이터에 대한 자연어 질의·설명 기능이 2024년에 발표되었다. [추정] 벤더 주장[^ref-176][^ref-278]

지시를 받는 쪽의 되묻기로는 비어 있는 필수 슬롯을 차례로 묻는 폼(Rasa 3.x) [사실][^ref-356], 등각 예측(conformal prediction)으로 LLM 계획기의 불확실성을 재어 도움을 요청하는 KnowNo(가정·실험실 환경) [사실][^ref-351], 명령을 명확·모호·수행 불가로 나눠 되묻는 CLARA [사실][^ref-353]가 있다. 실행 전 확인으로는 자연어 명령의 안전 속성을 추출해 결정적 규칙으로 승인·거부하는 SafeGate(ISO 13482 기반, 성능은 저자 보고, 초록에서 물류 현장 평가는 확인되지 않는다) [사실][^ref-417]와, 연계 대상: WMS 대화형 비서가 동작과 영향을 요약해 채팅으로 확인받는 사례가 있다. [추정] 벤더 주장[^ref-418]

이들을 나란히 놓으면 확인은 작업자 동작마다의 확인(음성 체크 디지트)과 자연어 지시의 해석 확인(되묻기·실행 전 게이트)의 두 유형으로 구분되는 것으로 보인다. 이 구분은 이 위키의 정리다. [추정][^ref-272][^ref-356][^ref-417] 자연어 지시 방법은 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)과 함께 본다. 원격 조작(teleoperation)은 이번 조사에서 근거를 확보하지 못했다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [14. 작업 순서·스케줄링](../../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-176]: InOrbit.AI, InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024, 2024-05, https://www.inorbit.ai/press/inorbit-robops-copilot, 접근일 2026-09-25 (원문 미열람)
[^ref-272]: Lucas Systems, Voice-Directed Warehousing - Solutions - Lucas Systems, 미확인, https://www.lucasware.com/voice-directed-warehousing/, 접근일 2026-09-25 (원문 미열람)
[^ref-275]: USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.), System and method for generating and updating location check digits (US 8868519), 미확인, https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519, 접근일 2026-09-25 (원문 미열람)
[^ref-278]: InOrbit.AI, InOrbit RobOps Copilot - Bring AI power to robot operations, 미확인, https://www.inorbit.ai/robopscopilot, 접근일 2026-09-25 (원문 미열람)
[^ref-279]: Locus Robotics, Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface), 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/user-interface, 접근일 2026-09-25 (원문 미열람)
[^ref-302]: Open Robotics (open-rmf), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-09-25
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-353]: Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S., CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents, 2024, https://arxiv.org/abs/2306.10376, 접근일 2026-09-25 (원문 미열람)
[^ref-356]: Rasa Technologies (RasaHQ/rasa GitHub), Forms — Rasa documentation (docs/docs/forms.mdx), 미확인, https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-418]: Mecalux, Mecalux integrates generative AI into Easy WMS, 미확인, https://www.mecalux.com/news/generative-ai-easy-wms-mecalux, 접근일 2026-09-25 (원문 미열람)
[^ref-467]: Žulj, I., Salewski, H., Goeke, D., & Schneider, M., Order batching and batch sequencing in an AMR-assisted picker-to-parts system, 2022, https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616, 접근일 2026-09-25 (원문 미열람)
[^ref-468]: Löffler, M., Boysen, N., & Schneider, M., Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers, 2023, https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207, 접근일 2026-09-25 (원문 미열람)
[^ref-469]: Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M., Deploying pickers and robots in cobot-based collaborative order picking systems, 2026-03, https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-476]: Das, D., Banerjee, S., & Chernova, S., Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery, 2021-01, https://arxiv.org/abs/2101.01625, 접근일 2026-09-25 (원문 미열람)
[^ref-477]: Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 미확인, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-46 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-46 | 18. 사람–로봇 협업·운영 인터페이스 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-46/pages/topics/2026/2026-09-25-area18-s7.md

```markdown
---
title: "18. 사람–로봇 협업·운영 인터페이스 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 18
related_areas: [1, 3, 4, 9, 13, 14, 19, 20, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-031, ref-051, ref-104, ref-302, ref-356, ref-470, ref-471, ref-472, ref-473, ref-474, ref-475]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#7
---

[홈](../../index.md) › [주제](../index.md) › 18. 사람–로봇 협업·운영 인터페이스 — 관련 표준·프레임워크·오픈소스

# 18. 사람–로봇 협업·운영 인터페이스 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇–관제 인터페이스 VDA 5050, 관제 대시보드 Open-RMF, 사람과 이동로봇이 함께 일하는 현장의 안전 표준과 국내 가이드·KS가 이 영역과 이어진다. [사실][^ref-051][^ref-470]
- 이 페이지는 [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇–관제 인터페이스 VDA 5050, 관제 대시보드 Open-RMF, 사람과 이동로봇이 함께 일하는 현장의 안전 표준과 국내 가이드·KS가 이 영역과 이어진다. [사실][^ref-051][^ref-470]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDA 5050 (최신판 명세·state.schema) | 표준 | 운용 모드·안전 상태·일시정지를 로봇이 관제에 보고한다. [사실] | [^ref-031][^ref-051] |
| Open-RMF rmf-web·rmf_demos | 오픈소스 | 웹 대시보드로 작업 제출·상태 감시, 데모의 비상 경보 대응. [사실] | [^ref-302][^ref-104] |
| ISO 3691-4:2023 | 표준 | 제2판(2020판 대체). 무인 산업용 트럭과 그 시스템(차량, 제어 시스템, 하역 장치, 배터리 충전소, 적재물 인계 스테이션)의 안전 요구. 원문 미열람. [사실] | [^ref-470] |
| ISO 10218-1·10218-2:2025 | 표준 | 협동 적용 안전 요구를 본문에 넣어 ISO/TS 15066 내용을 흡수하고 기능 안전을 명확히 하며 사이버보안 요구를 더했다(A3 해설 기준, ISO 원문 미열람). [사실] | [^ref-471] |
| ANSI/A3 R15.08 계열 | 표준 | 산업용 이동로봇 안전을 제조사 요구(1부), 현장 통합·적용(2부, 2023, 조작기 단 유형 C 포함), 사용자 책임(3부, 발행 여부 미확인)으로 나눈다. 원문 미열람. [사실] | [^ref-472] |
| 고정식·이동식 산업용 로봇의 협동작업 안전 가이드(고용노동부·한국산업안전보건공단, 2023-07) | 프레임워크 | 감지기를 활용한 충돌방지 조치, 작업자 이동·작업 방법, 점검표, 이동식 로봇 예시를 제시했다. [사실] 보도에 따르면 작업자가 접근 가능한 위치에 비상정지장치를 두도록 한다. [추정] | [^ref-473][^ref-474] |
| 이동식 협동로봇 안전기준 KS(번호 미확인, 2024-11) | 표준 | 대구 규제자유특구 실증을 거쳐 제정되었고, 그 전에는 작업공간 분리나 안전 울타리가 필요했다. [사실] | [^ref-475] |
| Rasa 폼(Rasa 3.x) | 오픈소스 | 필수 슬롯 되묻기. [사실] | [^ref-356] |

안전 표준·국내 가이드·KS는 로봇 제조사와 현장 통합사가 갖출 안전 기능의 요구로 읽고, ROP 쪽 역할은 9절의 추정 범위로만 둔다. [추정][^ref-470][^ref-472] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [14. 작업 순서·스케줄링](../../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-302]: Open Robotics (open-rmf), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-09-25
[^ref-356]: Rasa Technologies (RasaHQ/rasa GitHub), Forms — Rasa documentation (docs/docs/forms.mdx), 미확인, https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-471]: A3(Association for Advancing Automation), Updated ISO 10218 - Answers to Frequently Asked Questions (FAQs), 미확인, https://www.automate.org/robotics/blogs/updated-iso-10218-faq, 접근일 2026-09-25 (원문 미열람)
[^ref-472]: A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-473]: 고용노동부, 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포, 2023-07, https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065, 접근일 2026-09-25 (원문 미열람)
[^ref-474]: 로봇신문, '이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나?, 미확인, https://www.irobotnews.com/news/articleView.html?idxno=32130, 접근일 2026-09-25 (원문 미열람)
[^ref-475]: 중소벤처기업부(대한민국 정책브리핑), ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!, 2024-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-46 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-46 | 18. 사람–로봇 협업·운영 인터페이스 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-46/pages/topics/2026/2026-09-25-area18-s4.md

```markdown
---
title: "18. 사람–로봇 협업·운영 인터페이스 — 핵심 개념과 용어"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 18
related_areas: [1, 3, 4, 9, 13, 14, 19, 20, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-051, ref-272, ref-275, ref-471, ref-477, ref-478]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#4
---

[홈](../../index.md) › [주제](../index.md) › 18. 사람–로봇 협업·운영 인터페이스 — 핵심 개념과 용어

# 18. 사람–로봇 협업·운영 인터페이스 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **운용 모드(operating mode)** — [VDA 5050](../../glossary/vda-5050.md) 상태 메시지의 operatingMode 로, STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값 가운데 하나를 보고한다(2026-09-25 확인). [사실][^ref-051]
- **안전 상태(safetyState)·일시정지(paused)** — 비상정지 종류(로봇에서 수동 확인하는 MANUAL, 시설 비상정지를 원격 확인하는 REMOTE, NONE)와 보호 필드 침범을 필수로 보고하고, 물리 버튼이나 즉시 동작(instantAction)으로 멈춘 상태를 따로 보고한다. [사실][^ref-051]
- 이 페이지는 [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **운용 모드(operating mode)** — [VDA 5050](../../glossary/vda-5050.md) 상태 메시지의 operatingMode 로, STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값 가운데 하나를 보고한다(2026-09-25 확인). [사실][^ref-051]
- **안전 상태(safetyState)·일시정지(paused)** — 비상정지 종류(로봇에서 수동 확인하는 MANUAL, 시설 비상정지를 원격 확인하는 REMOTE, NONE)와 보호 필드 침범을 필수로 보고하고, 물리 버튼이나 즉시 동작(instantAction)으로 멈춘 상태를 따로 보고한다. [사실][^ref-051]
- **협동 적용(collaborative application)** — ISO 10218:2025 개정판이 '협동로봇' 대신 쓰는 용어로, 로봇이 아니라 사람과 함께 일하도록 설계된 적용 방식을 안전 판단의 기준으로 삼는다(A3 해설 기준, ISO 원문 미열람). [사실][^ref-471]
- **팬아웃(fan-out)** — 한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수로, 로봇을 방치해도 성과가 유지되는 정도(neglect tolerance)와 로봇 하나를 다루는 상호작용 시간으로 정해진다는 척도다(2004). [사실][^ref-478]
- **상황 인식 기반 에이전트 투명성(Situation Awareness-based Agent Transparency, SAT)** — 에이전트의 현재 행동·계획, 추론, 미래 결과 예측을 세 수준으로 운영자에게 보여 주는 틀이며, 군사·다중 로봇 중재 연구 맥락에서 높은 투명성 화면이 상황 인식과 신뢰를 높였다고 보고된다. [사실][^ref-477]
- **[음성 피킹](../../glossary/voice-picking.md)과 [위치 체크 디지트](../../glossary/location-check-digit.md)** — 시스템이 위치와 수량을 음성으로 지시하고 작업자가 체크 디지트·수량 같은 짧은 응답으로 동작마다 확인하는 방식이다. [사실][^ref-272][^ref-275]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [14. 작업 순서·스케줄링](../../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-272]: Lucas Systems, Voice-Directed Warehousing - Solutions - Lucas Systems, 미확인, https://www.lucasware.com/voice-directed-warehousing/, 접근일 2026-09-25 (원문 미열람)
[^ref-275]: USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.), System and method for generating and updating location check digits (US 8868519), 미확인, https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519, 접근일 2026-09-25 (원문 미열람)
[^ref-471]: A3(Association for Advancing Automation), Updated ISO 10218 - Answers to Frequently Asked Questions (FAQs), 미확인, https://www.automate.org/robotics/blogs/updated-iso-10218-faq, 접근일 2026-09-25 (원문 미열람)
[^ref-477]: Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science), Situation awareness-based agent transparency and human-autonomy teaming effectiveness, 미확인, https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750, 접근일 2026-09-25 (원문 미열람)
[^ref-478]: Olsen, D. R. 외(CHI 2004), Fan-out: measuring human control of multiple robots, 2004, https://dl.acm.org/doi/10.1145/985692.985722, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-46 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-46 | 18. 사람–로봇 협업·운영 인터페이스 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-46/pages/topics/2026/2026-09-25-area18-s8.md

```markdown
---
title: "18. 사람–로봇 협업·운영 인터페이스 — 대표 연구와 자료"
type: topic
category: "E. 협업·현장 운영"
primary_area_no: 18
related_areas: [1, 3, 4, 9, 13, 14, 19, 20, 25, 27]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-351, ref-353, ref-417, ref-467, ref-468, ref-469, ref-476, ref-478, ref-479]
last_run: 2026-09-25
version: 1
split_from: docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md#8
---

[홈](../../index.md) › [주제](../index.md) › 18. 사람–로봇 협업·운영 인터페이스 — 대표 연구와 자료

# 18. 사람–로봇 협업·운영 인터페이스 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 협동 피킹 조율 논문과 운영자 감독·실패 설명 연구, 자연어 지시의 되묻기·실행 전 게이트 연구가 이 영역의 대표 자료다. [사실][^ref-469][^ref-478]
- 이 페이지는 [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

협동 피킹 조율 논문과 운영자 감독·실패 설명 연구, 자연어 지시의 되묻기·실행 전 게이트 연구가 이 영역의 대표 자료다. [사실][^ref-469][^ref-478]

- Žulj·Salewski·Goeke·Schneider, AMR 보조 피커–부품 시스템의 주문 배치와 배치 순서(2022) — 구역 피커–교차 통로 AMR 인계 구조의 최적화. [사실][^ref-467]
- Löffler·Boysen·Schneider, 사람–로봇 협업: AMR과 사람 피커의 조율(2023) — 대기 AMR 사이를 옮겨 다니는 피킹의 작업 완료 시각 최소화, 속도 균형의 중요성(저자 계산 실험). [사실][^ref-468]
- Yang 외, 협동 피킹 시스템의 피커·로봇 투입(IISE Transactions, 2026-03) — 네 모드별 인원·로봇 수 분석. [oq-009](../../open-questions.md)와 관련되나 교대조 단위 여부는 미확인. [사실][^ref-469]
- Olsen 외, 팬아웃(CHI 2004) — 한 사람이 다룰 수 있는 로봇 수의 척도. [사실][^ref-478]
- Rey-Becerra·Wischniewski, 한 사람–여러 로봇 시스템 고찰(Ergonomics, 2025-07-11) — 주의·인지 부하 관리의 어려움 지적, 분석 건수는 미확인. [추정][^ref-479]
- Das·Banerjee·Chernova, 로봇 실패 설명(HRI 2021) — 맥락·이력 설명의 효과(가정 환경 실험). [사실][^ref-476]
- Ren 외 KnowNo(2023)·Park 외 CLARA(IEEE RA-L 2024)·Obi 외 SafeGate(2026-04 프리프린트) — 불확실성 기반 도움 요청, 명령 판별·되묻기, 실행 전 안전 게이트. [사실][^ref-351][^ref-353][^ref-417]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)
- 관련 영역: [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md), [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md), [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md), [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [14. 작업 순서·스케줄링](../../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-353]: Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S., CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents, 2024, https://arxiv.org/abs/2306.10376, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-467]: Žulj, I., Salewski, H., Goeke, D., & Schneider, M., Order batching and batch sequencing in an AMR-assisted picker-to-parts system, 2022, https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616, 접근일 2026-09-25 (원문 미열람)
[^ref-468]: Löffler, M., Boysen, N., & Schneider, M., Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers, 2023, https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207, 접근일 2026-09-25 (원문 미열람)
[^ref-469]: Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M., Deploying pickers and robots in cobot-based collaborative order picking systems, 2026-03, https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036, 접근일 2026-09-25 (원문 미열람)
[^ref-476]: Das, D., Banerjee, S., & Chernova, S., Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery, 2021-01, https://arxiv.org/abs/2101.01625, 접근일 2026-09-25 (원문 미열람)
[^ref-478]: Olsen, D. R. 외(CHI 2004), Fan-out: measuring human control of multiple robots, 2004, https://dl.acm.org/doi/10.1145/985692.985722, 접근일 2026-09-25 (원문 미열람)
[^ref-479]: Rey-Becerra, E., & Wischniewski, S., Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance, 2025-07-11, https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-46 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-46 | 18. 사람–로봇 협업·운영 인터페이스 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-46/docs_tree.txt

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
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/conflict-based-search.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cora.md
glossary/crdt.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-shadow.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fleet-adapter.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/grai.md
glossary/hallucination.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoorgml.md
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
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/order-batching.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/skill.md
glossary/slot-filling.md
glossary/space-graph.md
glossary/sscc.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
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
references/ref-199.md
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 448건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 113개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-perception: 협동 인지 (Collaborative Perception)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoorgml: IndoorGML (IndoorGML)
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- order-batching: 주문 배치 (Order Batching)
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
```

### docs/open-questions.md (요약: 대상 영역 [18] 에 걸린 1건 / 전체 69건)

```markdown
- oq-009 [열림] 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? (영역 3, 18)
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

### runs/2026-09-25-46/verification2.json

```json
{
  "run_id": "2026-09-25-46",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": false,
    "issues": [
      "세부영역 페이지 9절 표 '시설·설비 제어' 행: 'ROP가 직접 맡는 것' 칸에 '비상 경보를 받아 로봇 작업을 멈추고 대기 위치로 보내는 작업 측 대응'을 [사실][^ref-104]로 적었다. f10 은 Open-RMF 데모 기능(경보 시 가장 가까운 주차 위치로 이동)만 뒷받침하고, ROP 직접 범위로 배정한 근거는 브리프에 없다(f31 의 ROP 역할은 운용 모드·안전 상태 표시, 재개·수동 전환 승인 흐름, 구역·권한 반영뿐이다). '멈추고'도 출처에 없는 표현이다."
    ]
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "f22 는 기존 용어집 voice-picking·location-check-digit 을 링크로 재사용했다(신규 등록 없음)",
      "oq-009 는 열림을 유지했고 해결로 바꾸지 않았다"
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
    "세부영역 페이지 9절 표 '시설·설비 제어' 행의 'ROP가 직접 맡는 것' 칸: '비상 경보를 받아 로봇 작업을 멈추고 대기 위치로 보내는 작업 측 대응'을 ROP 직접 범위의 사실처럼 쓰지 않는다. 이 칸은 '시설 비상 경보 상태를 받아 작업 흐름에 반영하는 것으로 보인다 [추정][^ref-104]' 수준으로 낮추거나 비우고, Open-RMF 데모 내용은 '(Open-RMF 데모는 경보 시 로봇을 가장 가까운 주차 위치로 보낸다) [사실][^ref-104]'로 따로 적는다. '멈추고'는 삭제한다 — f10 은 데모 기능만 뒷받침하며, ROP 역할 배정은 f31 에 없는 브리프 밖 주장이고 '멈춘다'는 출처에 없다.",
    "주제 페이지 docs/topics/2026/2026-09-25-area18-s6.md 3절 '운용 모드·일시정지·비상정지 보고' 소절 마지막 문장 '안전 상태와 일시정지는 로봇이 보고하는 값이므로, 운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이다. [사실][^ref-051]'을 둘로 나눈다: '안전 상태와 일시정지는 로봇이 보고하는 값이다. [사실][^ref-051]' / '운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이 될 것으로 보인다. [추정][^ref-051][^ref-470]' — 뒷부분은 f31 의 [추정]이며 태그를 올릴 수 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 2건(f7, f20), 교차 확인 0건. 강등: f7 사실 → 추정(VDA 5050 SEMIAUTOMATIC·INTERVENED 설명이 명세 표 10·11과 불일치해 원문대로 고쳐 씀), f15 사실 → 추정(기사 단일 출처), f20 사실 → 추정(분석 건수 44건/35건 불일치, 미확인). 원문 미열람 출처: ref-467~ref-480, ref-272, ref-275, ref-279, ref-176, ref-278, ref-351, ref-353, ref-356, ref-417, ref-418. 검증자가 GitHub 원문으로 확인한 것은 ref-051(state.schema), ref-302(rmf-web), ref-104(rmf_demos)와 입력 원문 ref-031 이다. 주의: 사람 피커–로봇 대기에 관한 근거는 논문 모델·계산 실험 기준이며 국내 현장 실측은 없다. 안전 표준(ISO 3691-4, ISO 10218:2025, R15.08)은 원문을 열지 못했고 ISO 10218 은 A3 해설 기준이다. 안전 기능은 연계 대상이며 ROP 역할(f31)은 추정이다. 원격 조작 관련 근거는 없다. 정정 요청 없음. oq-009 는 해결로 바꾸지 않는다. / 2차 수정 후 재검증. 드리프트 2건(9절 '시설·설비 제어' 행에서 Open-RMF 데모 기능을 ROP 직접 범위의 사실로 배정하고 '멈추고'를 더함, 분리 주제 페이지 6절에서 f31 의 추정을 [사실]로 씀) 수정 지시. 1차 수정 지시 16건은 모두 이행 확인(f7 표 10·11 기준 재서술, f30 두 유형, 열린 질문 후보 3 제외, f11·f13·f12·f28 문구, 강등 3건, 벤더 주장·원문 미열람 병기, 25·27 연결). [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 통과). 참고: 세부영역 페이지 프런트매터 sources 는 분리 주제 페이지로 옮긴 절의 출처까지 포함해 본문 각주보다 많다.",
  "retry_reason": null
}
```
