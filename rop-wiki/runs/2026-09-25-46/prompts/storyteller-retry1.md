(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- 세부영역 반영 제안: 6건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
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

### docs/categories/e-collaboration-and-field-operations/index.md

```markdown
---
title: "E. 협업·현장 운영"
type: category
status: seed
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../../index.md) › E. 협업·현장 운영

# E. 협업·현장 운영

## 핵심 질문

계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? [분류원문]

## 개요

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? | [17. 로봇 간 협업·물리적 인계](17-robot-to-robot-collaboration-and-physical-handover.md) | published |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? | [18. 사람–로봇 협업·운영 인터페이스](18-human-robot-collaboration-and-operator-interface.md) | seed |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? | [19. 모니터링·이상 탐지·원인 분석](19-monitoring-anomaly-detection-and-root-cause-analysis.md) | seed |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? | [20. 예외 복구·재계획·업무 연속성](20-exception-recovery-replanning-and-business-continuity.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7] [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [17. 로봇 간 협업·물리적 인계](17-robot-to-robot-collaboration-and-physical-handover.md) — 영역 심화: 3~11절 신규 작성, 페이지 상태 자동 표식 추가, 10절 첫 항목 목록 기호 보정. 2차: 5절 제약 칸의 ASTM F3499-21 서술을 시험 방법의 존재로 고침 (실행 2026-09-25-42)
- 2026-09-25 · 생성 · [17. 로봇 간 협업·물리적 인계 — 열린 질문](../../topics/2026/2026-09-25-area17-s11.md) — 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "11. 열린 질문" 절(1,494자)을 옮겼다 (실행 2026-09-25-42)
- 2026-09-25 · 생성 · [17. 로봇 간 협업·물리적 인계 — 대표 연구와 자료](../../topics/2026/2026-09-25-area17-s8.md) — 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "8. 대표 연구와 자료" 절(1,462자)을 옮겼다 (실행 2026-09-25-42)
- 2026-09-25 · 생성 · [17. 로봇 간 협업·물리적 인계 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area17-s7.md) — 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 25. 안전·위험 관리 링크를 주제 페이지 기준 경로로 고침. 2차: GS1 CBV 행을 어휘 정의만 [사실]로 쓰고 인계 이벤트 값은 미정(oq-006)으로 고침 (실행 2026-09-25-42)
- 2026-09-25 · 생성 · [17. 로봇 간 협업·물리적 인계 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area17-s4.md) — 자동 분리: 17. 로봇 간 협업·물리적 인계 의 "4. 핵심 개념과 용어" 절(1,232자)을 옮겼다 (실행 2026-09-25-42)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [7]은 참고문헌 [ref-007](../../references/ref-007.md)에 해당한다.[^ref-007]

[^ref-007]: NIST, Performance of Collaborative Robot Systems, 미확인, https://www.nist.gov/programs-projects/performance-collaborative-robot-systems, 접근일 2026-09-24
```

### data/area_reflection_proposals.json (대상 영역 18. 사람–로봇 협업·운영 인터페이스 에 대한 트랙 반영 제안 6건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-21",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 18,
      "section": "6. 대표 접근법과 기술",
      "summary": "로봇 운영 제품의 자연어·음성 인터페이스: InOrbit RobOps Copilot(2024 질의·설명, 2026 미션 실행), Formant F3, 다임리서치 다비스(개발 계획). 모두 [추정] 벤더 주장이며 미션 정의 방식과 실행 전 확인·승인 절차는 미확인(q1-03에서 조사).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-26",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 18,
      "section": "6. 대표 접근법과 기술",
      "summary": "작업자에게 일을 지시하는 운영 인터페이스의 확인 방식: 음성 피킹은 체크 디지트·수량 같은 짧은 음성 응답으로 동작마다 확인한다([사실], ref-272·ref-275). 협업 피킹 로봇(Locus)은 화면으로 품목·위치·수량을 보여 주고 선택 기능으로 위치·용기 바코드 스캔 뒤 화면 확인을 받는다([추정] 벤더 주장, ref-279·ref-280). 로봇 대상 자연어 지시 제품은 해석 결과의 실행 전 확인 절차가 공개 자료에서 드러나지 않아(검색 요약 범위의 관찰, 부재의 확인 아님) 동작 확인과 지시 확인은 대상·시점이 다른 것으로 보인다([추정], 이 위키의 정리).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-26",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 18,
      "section": "8. 대표 연구와 자료",
      "summary": "음성 지시 창고 작업 자료(Lucas Systems, 벤더 문서), 위치 체크 디지트 불일치 경고를 기술한 미국 특허 공보 US 8868519(양수인 VOCOLLECT, INC., 출원 2011-05-27), Locus Robotics 사용자 인터페이스와 Aila 사례(벤더 주장), 자연어 지시 로봇 사례로 Amazon 차세대 Proteus(2026-06-04 발표, 실험실 파일럿, 벤더 주장)와 InOrbit RobOps Copilot 제품 페이지(벤더 주장). 모두 원문 미열람.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-30",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 18,
      "section": "6. 대표 접근법과 기술",
      "summary": "지시를 받는 운영 인터페이스의 되묻기 방식: 필수 슬롯 폼(Rasa 3.x), 불확실성 기반 도움 요청(KnowNo, 등각 예측), 명령의 명확·모호·수행 불가 판별과 질문 생성(CLARA, 국내 연구), 세 방식의 정리는 이 위키의 [추정]. 27. AI·학습·적응과 모델 운영과 양쪽 연결",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-30",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 1,
      "area_no": 18,
      "section": "8. 대표 연구와 자료",
      "summary": "Rasa 폼 문서(ref-356), CLARA(고려대 등, IEEE RA-L 2024, ref-352·ref-353), KnowNo(CoRL 2023, ref-350·ref-351), 작업 지향 대화의 의도 인식·슬롯 채우기 서베이(Weld 외 2022, ref-357)",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-37",
      "date": "2026-09-25",
      "track": "nl-task-chatbot",
      "stage": 2,
      "area_no": 18,
      "section": "6. 대표 접근법과 기술",
      "summary": "채팅 지시 실행 전 확인 방식 두 가지: WMS 대화형 비서의 동작·영향 항목 요약 후 채팅 확인(Mecalux, [추정] 벤더 주장, WMS 쪽 연계 대상 사례, f13)과 자연어 명령의 안전 속성 추출 뒤 결정적 승인·거부 게이트(SafeGate, ISO 13482 개인 돌봄 로봇 표준 기반, 저자 보고·물류 현장 미평가, f12). 27. AI·학습·적응과 모델 운영과 함께 연결.",
      "status": "제안"
    }
  ]
}
```

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "7. 화물·재고·자산 식별과 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "B. 공통 정보·환경 모델"
area_no: {{area_no}}                        # 1~28 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [8, 12, 17]. 없으면 []
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
경로: docs/categories/<대분류 slug>/<두 자리 번호-slug>.md  (아래 경로 규약 표)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 7. 화물·재고·자산 식별과 추적의 EPCIS 언급, 6. 지도·공간·위치 모델의 지도 버전 관리 포함 주석, 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 27. AI·학습·적응과 모델 운영의 교차 적용 주석)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 SCM·로봇·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "7. 화물·재고·자산 식별과 추적", "B. 공통 정보·환경 모델". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_SCM_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다. 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 12장의 1~10번에 대응한다(ref-001 ASCM SCOR, ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 9장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 재고정책 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: 27. AI·학습·적응과 모델 운영의 AI는 매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 27. AI·학습·적응과 모델 운영 페이지와 적용 대상 영역 페이지 양쪽에 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 흐름 매트릭스는 ../../flow-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/manual-capability-ontology/index.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | a-business-supply-chain-design/ |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | b-common-information-and-environment-model/ |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | c-connectivity-and-execution-foundation/ |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | d-planning-and-optimization/ |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | e-collaboration-and-field-operations/ |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | f-deployment-verification-and-maintenance/ |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | g-safety-security-intelligence-and-governance/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 주문·업무 시스템 연계 | A. 업무·공급망 설계 | a-business-supply-chain-design/01-order-and-business-system-integration.md |
| 2 | 2. 공정·워크플로 모델링 | A. 업무·공급망 설계 | a-business-supply-chain-design/02-process-and-workflow-modeling.md |
| 3 | 3. 처리능력·거점·설비 계획 | A. 업무·공급망 설계 | a-business-supply-chain-design/03-capacity-site-and-facility-planning.md |
| 4 | 4. 성과·경제성·프로세스 개선 | A. 업무·공급망 설계 | a-business-supply-chain-design/04-performance-economics-and-process-improvement.md |
| 5 | 5. 로봇 능력·작업 온톨로지 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md |
| 6 | 6. 지도·공간·위치 모델 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/06-map-space-and-location-model.md |
| 7 | 7. 화물·재고·자산 식별과 추적 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md |
| 8 | 8. 실시간 세계 상태·데이터 일관성 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md |
| 9 | 9. 로봇·제조사 관제 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md |
| 10 | 10. 설비·건물 시스템 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md |
| 11 | 11. 분산 시스템·통신·컴퓨팅 구조 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md |
| 12 | 12. 명령·작업 실행의 신뢰성 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md |
| 13 | 13. 작업 배정 — MRTA | D. 계획·최적화 | d-planning-and-optimization/13-task-allocation-mrta.md |
| 14 | 14. 작업 순서·스케줄링 | D. 계획·최적화 | d-planning-and-optimization/14-task-sequencing-and-scheduling.md |
| 15 | 15. 다중 로봇 경로·교통 관리 — MAPF | D. 계획·최적화 | d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md |
| 16 | 16. 공용 자원·충전·에너지 최적화 | D. 계획·최적화 | d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md |
| 17 | 17. 로봇 간 협업·물리적 인계 | E. 협업·현장 운영 | e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md |
| 18 | 18. 사람–로봇 협업·운영 인터페이스 | E. 협업·현장 운영 | e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md |
| 19 | 19. 모니터링·이상 탐지·원인 분석 | E. 협업·현장 운영 | e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md |
| 20 | 20. 예외 복구·재계획·업무 연속성 | E. 협업·현장 운영 | e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md |
| 21 | 21. 온보딩·설정·현장 시운전 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md |
| 22 | 22. 시뮬레이션·예측용 디지털 트윈 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md |
| 23 | 23. 시험·형식 검증·벤치마크 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md |
| 24 | 24. 자산·소프트웨어 수명주기 관리 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md |
| 25 | 25. 안전·위험 관리 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md |
| 26 | 26. 사이버보안·접근권한·개인정보 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md |
| 27 | 27. AI·학습·적응과 모델 운영 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md |
| 28 | 28. 표준·상호운용성·다사업자 거버넌스 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md |
-->
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 28페이지(예: docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 공통 정보·환경 모델):
!!! info "소속 대분류"
    [B. 공통 정보·환경 모델](index.md) — 핵심 질문:
    로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 28페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]
<!--
분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않고, 이 절에는 다른 문장을 두지 않는다. 원문 주석은 이 절이 아니라 2절의 인용 블록에 둔다.
이 절의 문장은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. SCM 관점의 질문

{{scm_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 표의 "SCM 관점의 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]". 수정 금지.
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 7. 화물·재고·자산 식별과 추적, 8. 실시간 세계 상태·데이터 일관성, 13. 작업 배정 — MRTA, 17. 로봇 간 협업·물리적 인계, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전, 22. 시뮬레이션·예측용 디지털 트윈, 27. AI·학습·적응과 모델 운영. 예: 7. 화물·재고·자산 식별과 추적의 EPCIS 언급, 6. 지도·공간·위치 모델의 지도 버전 관리 포함 주석, 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈의 구분, 27. AI·학습·적응과 모델 운영의 교차 적용 주석)은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다(27. AI·학습·적응과 모델 운영의 교차 규칙 문단은 5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전, 27. AI·학습·적응과 모델 운영 페이지에 둔다). 문단이 둘인 영역(6. 지도·공간·위치 모델)은 인용 블록도 둘이다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 공급망 운영에서 무엇이 막히는지, 로봇 개별 성능과 공급망 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 SCM 관점 질문에서 출발한다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "WES(Warehouse Execution System, 창고 실행 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** {{flow_steps}}
<!-- 분류 원문 11장의 흐름 "입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품" 중 이 시나리오가 놓이는 단계를 이름으로 명시한다. 예: "피킹 → 포장". 여러 단계에 걸치면 모두 적는다. -->

**시나리오:** {{scenario_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "피킹한 박스를 포장대로 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{scenario_narrative}}
<!--
여섯 항목은 분류 원문 11장의 정의를 따른다. 시작 조건: 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 화물·운반구를 다루는가 / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가 / 제약: 납기·공간·적재량·설비·권한 제약은 무엇인가 / 완료·인계: 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가 / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가.
표 아래에 1~3단락으로 시나리오를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 지어낸 현장 수치는 쓰지 않는다(설명용 가상 시나리오임을 첫 문장에 밝힌다. 예: "다음은 설명을 위한 가상의 시나리오이다.").
다룬 칸(단계 × 항목)은 pages.json 의 flow_matrix_updates 로 함께 낸다. 흐름 매트릭스 페이지: ../../flow-matrix.md
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

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 9장의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 거점 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 9장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [8. 실시간 세계 상태·데이터 일관성](08-real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장". 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 27. AI·학습·적응과 모델 운영을 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/manual-capability-ontology/index.md)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/manual-capability-ontology/question-backlog.md)로 링크만 둔다.
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

### templates/category.md

```markdown
---
title: "{{category}}"                       # 원문 명칭 그대로. 예: "B. 공통 정보·환경 모델"
type: category
category: "{{category}}"                    # title 과 같은 값
tags: [{{tags}}]                            # 선택. 없으면 []
status: {{status}}                          # seed | published. 시드 대분류 페이지는 seed 이며, "다른 대분류와의 연결"이 채워져 게시되면 published 로 바꾼다 [가정]
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 원문 주석의 [n] 에 대응하는 참고문헌 id. 예: [ref-003]
version: {{version}}                        # 정수
---
<!--
[템플릿] 대분류 페이지 (type: category)
경로: docs/categories/<대분류 slug>/index.md
쓰임: 구축 시 원문 부분(핵심 질문·개요·세부 연구영역·이 대분류의 핵심 포인트)을 채워 만든다. "다른 대분류와의 연결"은 에이전트(스토리텔러)가 관련 영역을 다루는 실행에서 채우고, "세부 연구영역" 표(페이지·현재 상태 열 포함)와 "최근 업데이트"는 퍼블리셔가 자동 갱신한다.
여섯 섹션(4.3): 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 최근 업데이트. 제목·순서 고정. H2 문자열은 사양서 4.3 문구 그대로이며 번호를 붙이지 않는다(pipeline/checks/protect_source.py 의 CATEGORY_SECTIONS 와 글자 단위로 같다. "1. 핵심 질문"처럼 번호를 붙이면 "섹션 제목·순서 불일치"로 반려된다). 각주 정의를 둘 자리로 번호 없는 "참고 자료" 절을 여섯 섹션 뒤에 하나 더 두었다. 이 절은 사양서 4.3 의 여섯 섹션에 없는 구축자 추가 절이다 [가정].

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 SCM·로봇·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "7. 화물·재고·자산 식별과 추적", "B. 공통 정보·환경 모델". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_SCM_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다. 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 12장의 1~10번에 대응한다(ref-001 ASCM SCOR, ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 9장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 재고정책 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: 27. AI·학습·적응과 모델 운영의 AI는 매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 27. AI·학습·적응과 모델 운영 페이지와 적용 대상 영역 페이지 양쪽에 연결한다. 8. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 22. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 같은 대분류의 세부영역은 <파일>.md, 다른 대분류는 ../<대분류 slug>/index.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | a-business-supply-chain-design/ |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | b-common-information-and-environment-model/ |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | c-connectivity-and-execution-foundation/ |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | d-planning-and-optimization/ |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | e-collaboration-and-field-operations/ |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | f-deployment-verification-and-maintenance/ |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | g-safety-security-intelligence-and-governance/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 주문·업무 시스템 연계 | A. 업무·공급망 설계 | a-business-supply-chain-design/01-order-and-business-system-integration.md |
| 2 | 2. 공정·워크플로 모델링 | A. 업무·공급망 설계 | a-business-supply-chain-design/02-process-and-workflow-modeling.md |
| 3 | 3. 처리능력·거점·설비 계획 | A. 업무·공급망 설계 | a-business-supply-chain-design/03-capacity-site-and-facility-planning.md |
| 4 | 4. 성과·경제성·프로세스 개선 | A. 업무·공급망 설계 | a-business-supply-chain-design/04-performance-economics-and-process-improvement.md |
| 5 | 5. 로봇 능력·작업 온톨로지 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md |
| 6 | 6. 지도·공간·위치 모델 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/06-map-space-and-location-model.md |
| 7 | 7. 화물·재고·자산 식별과 추적 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md |
| 8 | 8. 실시간 세계 상태·데이터 일관성 | B. 공통 정보·환경 모델 | b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md |
| 9 | 9. 로봇·제조사 관제 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md |
| 10 | 10. 설비·건물 시스템 연동 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md |
| 11 | 11. 분산 시스템·통신·컴퓨팅 구조 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md |
| 12 | 12. 명령·작업 실행의 신뢰성 | C. 연결·실행 기반 | c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md |
| 13 | 13. 작업 배정 — MRTA | D. 계획·최적화 | d-planning-and-optimization/13-task-allocation-mrta.md |
| 14 | 14. 작업 순서·스케줄링 | D. 계획·최적화 | d-planning-and-optimization/14-task-sequencing-and-scheduling.md |
| 15 | 15. 다중 로봇 경로·교통 관리 — MAPF | D. 계획·최적화 | d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md |
| 16 | 16. 공용 자원·충전·에너지 최적화 | D. 계획·최적화 | d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md |
| 17 | 17. 로봇 간 협업·물리적 인계 | E. 협업·현장 운영 | e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md |
| 18 | 18. 사람–로봇 협업·운영 인터페이스 | E. 협업·현장 운영 | e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md |
| 19 | 19. 모니터링·이상 탐지·원인 분석 | E. 협업·현장 운영 | e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md |
| 20 | 20. 예외 복구·재계획·업무 연속성 | E. 협업·현장 운영 | e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md |
| 21 | 21. 온보딩·설정·현장 시운전 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md |
| 22 | 22. 시뮬레이션·예측용 디지털 트윈 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md |
| 23 | 23. 시험·형식 검증·벤치마크 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md |
| 24 | 24. 자산·소프트웨어 수명주기 관리 | F. 도입·검증·유지관리 | f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md |
| 25 | 25. 안전·위험 관리 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md |
| 26 | 26. 사이버보안·접근권한·개인정보 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md |
| 27 | 27. AI·학습·적응과 모델 운영 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md |
| 28 | 28. 표준·상호운용성·다사업자 거버넌스 | G. 안전·보안·지능·거버넌스 | g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md |
-->
[홈](../../index.md) › {{category}}

# {{category}}

## 핵심 질문

{{core_question}} [분류원문]
<!-- 분류 원문 1장 표의 "핵심 질문" 칸 문장 그대로. 예: "로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? [분류원문]". 수정 금지. -->

## 개요

{{overview_paragraph}} [분류원문]
<!-- 분류 원문에서 이 대분류 장의 첫 문단(표 위의 문단)을 굵게 표기까지 그대로 옮긴다. 예: "**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다. [분류원문]". G. 안전·보안·지능·거버넌스처럼 첫 문단에 굵은 표기가 없는 장도 그대로 옮긴다. -->

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{scm_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |

[분류원문]
<!-- auto:category-area-table:end -->
<!--
원문 표 4행을 그대로 옮기고(앞 3열은 원문 셀과 글자 단위로 같게, 첫 열의 굵은 표기 유지, 첫 열에 링크를 씌우지 않음), "페이지" 열에 세부영역 페이지 링크, "현재 상태" 열에 해당 페이지 프런트매터 status(seed | draft | verified | published | needs_update | deprecated)를 둔다(4.3 의 "링크와 현재 상태 열만 추가"). 표 바로 아래 빈 줄 다음에 [분류원문] 한 줄을 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_category)가 각 행의 앞 3칸과 [분류원문] 줄을 원문과 대조한다.
표 전체는 auto:category-area-table 마커 안에 있고 퍼블리셔(pipeline/lib/render.py render_category_area_table)가 원문 파서와 세부영역 페이지의 status 로 다시 쓴다. 스토리텔러는 마커 사이를 건드리지 않는다. 마커 위의 안내 문장은 마커 밖이므로 그대로 둔다. 이 key 는 사양서에 없는 구축자 추가 key 이며, 시드 대분류 페이지·agents/shared-rules.md 6절의 auto key 목록·퍼블리셔(pipeline/lib/autoregion.py AUTO_KEYS)가 같은 값을 쓴다 [가정 — 사용자 결정 항목: 표 전체를 자동 영역으로 둘지, 표는 마커 밖에 두고 현재 상태 열만 갱신할지].
-->

## 이 대분류의 핵심 포인트

{{key_point_paragraphs}}
<!--
분류 원문에서 이 대분류 장의 표 아래 설명 문단들을 순서대로 모두 옮긴다. 문단마다 끝에 " [분류원문]" 을 붙이고, 그 줄에는 태그 뒤에 아무것도(각주 포함) 붙이지 않는다. 원문의 [n] 번호 표기는 문장 안에 그대로 둔다. 예: "... 참고 표준이다. [3] [분류원문]". 대응 각주 [^ref-00n] 은 이 절이 아니라 "참고 자료" 절의 별도 문장에 둔다. 굵게·기울임 표기를 유지한다. 에이전트는 이 절의 원문 문장을 고치지 않고, 원문 문단 뒤에 자기 문장을 덧붙이지도 않는다.
퍼블리셔(pipeline/checks/protect_source.py check_category)는 이 절에서 " [분류원문]" 으로 끝나는 줄만 모아 원문 문단 목록과 글자 단위로 대조한다. 태그 뒤에 각주를 붙이면 그 줄이 빠져 "핵심 포인트 문단 불일치"로 반려된다.
-->

## 다른 대분류와의 연결

{{category_connections}}
<!--
에이전트가 채운다. 목록 형식: "- [C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md) — 이 대분류의 어떤 영역이 저 대분류의 어떤 영역과 왜 이어지는지 한두 문장(세부영역은 번호와 이름 함께)". 주장에는 태그·각주. 구축 시에는 "아직 작성되지 않음"으로 둔다.
G. 안전·보안·지능·거버넌스는 나머지 여섯 대분류 전체에 적용된다는 원문 취지를 반영한다. 27. AI·학습·적응과 모델 운영의 교차 규칙(매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전, 도면 해석은 6. 지도·공간·위치 모델, 학습 기반 배차는 13. 작업 배정 — MRTA, 장애 분석은 19. 모니터링·이상 탐지·원인 분석)을 여기서도 지킨다.
-->

## 최근 업데이트

<!-- auto:category-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:category-recent:end -->
<!-- 퍼블리셔가 이 대분류에 속한 세부영역·주제 페이지의 최근 변경을 최신순으로 넣는다(날짜 | 실행 id | 페이지 | 변경 요약). 마커 사이는 스토리텔러가 건드리지 않는다. -->

## 참고 자료

{{source_footnote_sentences}}

{{footnotes}}
<!-- "이 대분류의 핵심 포인트" 원문 문단의 [n] 에 대응하는 각주를 별도 문장으로 두고(예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]"), 그 아래에 각주 정의를 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". "다른 대분류와의 연결"에서 쓴 각주도 여기에 둔다. 각주가 없으면 "없음". 이 절은 사양서 4.3 의 여섯 섹션 밖의 보조 절로, 5.3 의 각주 정의 자리를 위해 구축자가 추가했으며 번호를 붙이지 않는다 [가정]. -->
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

### docs/standards/index.md

```markdown
---
title: "표준·프레임워크 목록"
type: standard
subtype: index
status: published
created: 2026-09-24
updated: 2026-09-24
version: 3
---

[홈](../index.md) › 표준·프레임워크 목록

# 표준·프레임워크 목록

이 위키가 참조하는 표준·오픈소스·평가 프로그램·프레임워크를 관련 세부영역과 함께 정리한다. 시드 8건은 분류 원문 12장의 참고 자료 가운데 표준·오픈소스·평가 프로그램·프레임워크에 해당하는 항목이며(12장 참고 자료 목록의 다섯째·여섯째 항목인 Li 등 2020, Ma 등 2017 논문은 제외), 각 항목의 출처는 [참고문헌](../references/index.md)의 ref-001 ~ ref-010 에 대응한다. 시드 표는 아래 "시드 목록"에 손으로 두고, 리서치 에이전트가 제안하고 내용 검증 에이전트가 실재와 최신성을 확인한 새 항목은 퍼블리셔가 "추가 항목"의 자동 갱신 영역에 표로 넣는다. [가정]

종류는 네 가지로 나눈다. **표준**은 표준 기관이 제정·관리하는 규격, **오픈소스**는 공개 저장소로 배포되는 소프트웨어와 그 공식 문서, **평가 프로그램**은 연구기관이 운영하는 성능 평가·경진대회, **프레임워크**는 규범적 규격은 아니지만 구조·어휘·설계 관점을 제공하는 참조 모델·설계 문서다. SCOR(Supply Chain Operations Reference)의 종류는 참고문헌 ref-001 의 유형(표준)과 같게 표준으로 두었고, ROS 2(Robot Operating System 2) DDS-Security와 ROS 2 위협 모델은 규격 본문이 아니라 ROS 2 설계 문서이므로 둘 다 프레임워크로 두었다. 이 둘은 구축자의 분류이며 검증 에이전트가 바꿀 수 있다. [가정]

관련 세부영역은 번호와 이름을 함께 쓴다. "원문 12장 요약" 열은 분류 원문 12장의 요약 구절을 그대로 옮긴 것이다. 세부 내용과 근거는 이름 열의 링크(용어집 항목)와 출처 열의 참고문헌 페이지에서 본다.

## 시드 목록

| 이름 | 종류 | 발행 기관 | 관련 세부영역 | 원문 12장 요약 | 출처 |
|---|---|---|---|---|---|
| [SCOR (SCOR Digital Standard)](../glossary/scor.md) | 표준 | ASCM(Association for Supply Chain Management) | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) · [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) · [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 공급망 프로세스 범위 참고. [분류원문] | [ref-001](../references/ref-001.md)[^ref-001] |
| [ISA-95 (ANSI/ISA-95)](../glossary/isa-95.md) | 표준 | ISA(International Society of Automation) | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) · [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) · [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 기업 업무와 제조 운영·제어의 통합 경계 참고. [분류원문] | [ref-002](../references/ref-002.md)[^ref-002] |
| [GS1 EPCIS](../glossary/epcis.md) | 표준 | GS1 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) · [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) · [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고. [분류원문] | [ref-003](../references/ref-003.md)[^ref-003] |
| [Open-RMF](../glossary/open-rmf.md) | 오픈소스 | Open Robotics | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) · [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) · [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) · [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md) | 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고. [분류원문] | [ref-004](../references/ref-004.md)[^ref-004] |
| [ROS 2 DDS-Security (ROS 2 DDS-Security Integration)](../glossary/dds-security.md) | 프레임워크 | ROS 2 Design | [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) · [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) · [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 인증·암호화·접근통제 구조 참고. [분류원문] | [ref-009](../references/ref-009.md)[^ref-009] |
| ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) | 프레임워크 | ROS 2 Design | [26. 사이버보안·접근권한·개인정보](../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) · [25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) · [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 로봇 시스템의 보안 위협과 대응 설계 참고. [분류원문] | [ref-010](../references/ref-010.md)[^ref-010] |
| NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) | 평가 프로그램 | NIST(National Institute of Standards and Technology) | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) · [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) · [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 사람–로봇 및 이종 로봇 협업 성능 평가 참고. [분류원문] | [ref-007](../references/ref-007.md)[^ref-007] |
| [ARIAC](../glossary/ariac.md) | 평가 프로그램 | NIST | [23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) · [22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) · [20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고. [분류원문] | [ref-008](../references/ref-008.md)[^ref-008] |

## 추가 항목

리서치·검증을 거쳐 새로 등록되는 항목은 퍼블리셔가 아래 자동 갱신 영역에 표로 넣는다. 그 표의 열 구성(이름 | 기관 | 종류 | 관련 영역 | 참고문헌 | URL)은 퍼블리셔 렌더러를 따르며, 위의 시드 표는 이 영역 밖에 있어 자동 갱신이 지우지 않는다. [가정]

<!-- auto:standards-table:start -->
| 이름 | 기관 | 종류 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| GS1 EPCIS 2.0 (ISO/IEC 19987:2024) | ISO/IEC · GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-011](../references/ref-011.md) | <https://www.iso.org/standard/85557.html> |
| GS1 CBV (Core Business Vocabulary) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-014](../references/ref-014.md) | <https://ref.gs1.org/standards/cbv/> |
| SSCC (Serial Shipping Container Code) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-016](../references/ref-016.md) | <https://www.gs1.org/standards/id-keys/sscc> |
| GS1 Logistic Label Guideline | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-018](../references/ref-018.md) | <https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf> |
| GRAI (Global Returnable Asset Identifier) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-019](../references/ref-019.md) | <https://www.gs1.org/standards/id-keys/grai> |
| GIAI (Global Individual Asset Identifier) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-020](../references/ref-020.md) | <https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods-> |
| EPC Tag Data Standard (1.11판) | GS1 | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-021](../references/ref-021.md) | <https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf> |
| VDA 5050 (2.0.0) | VDA(Verband der Automobilindustrie) | 표준 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-022](../references/ref-022.md) | <https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf> |
| OpenEPCIS | OpenEPCIS | 오픈소스 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-013](../references/ref-013.md) | <https://openepcis.io/docs/epcis/> |
| IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) | IEEE | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-025](../references/ref-025.md) | <https://ieeexplore.ieee.org/document/7084073/> |
| IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology | IEEE | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-026](../references/ref-026.md) | <https://standards.ieee.org/standard/1872_2-2021.html> |
| W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) | W3C / OGC | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-030](../references/ref-030.md) | <https://www.w3.org/TR/vocab-ssn/> |
| VDA 5050 (3.0.0) | VDA(Verband der Automobilindustrie) | 표준 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-032](../references/ref-032.md) | <https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN> |
| MassRobotics AMR Interoperability Standard (1.0) | MassRobotics | 표준 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-033](../references/ref-033.md) | <https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/> |
| OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) | OPC Foundation / VDMA | 표준 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-034](../references/ref-034.md) | <https://reference.opcfoundation.org/specs/OPC-40010-1> |
| Information Model for Capabilities, Skills & Services (CSS) | Plattform Industrie 4.0 | 프레임워크 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-035](../references/ref-035.md) | <https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html> |
| Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) | Auto-ID Labs Korea(세종대학교) | 오픈소스 | [7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-050](../references/ref-050.md) | <https://github.com/JaewookByun/epcis> |
| RAWSim-O | Merschformann, M. (RAWSim-O GitHub) | 오픈소스 | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | [ref-101](../references/ref-101.md) | <https://github.com/merschformann/RAWSim-O> |
| 스마트물류센터 인증제 | 한국교통연구원(인증스마트물류센터) | 평가 프로그램 | [3. 처리능력·거점·설비 계획](../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | [ref-106](../references/ref-106.md) | <https://cslc.koti.re.kr/> |
| BPMN 2.0 (ISO/IEC 19510:2013) | OMG(Object Management Group) · ISO/IEC | 표준 | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-112](../references/ref-112.md) | <https://www.omg.org/spec/BPMN/2.0/About-BPMN> |
| IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 | IEC / ISO | 표준 | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) | [ref-119](../references/ref-119.md) | <https://www.iso.org/standard/67480.html> |
| B2MML (Business To Manufacturing Markup Language, 판 0701) | MESA International | 표준 | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | [ref-117](../references/ref-117.md) | <https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd> |
| OCEL 2.0 (Object-Centric Event Log) | arXiv:2403.01975 저자(미확인) | 표준 | [2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | [ref-122](../references/ref-122.md) | <https://arxiv.org/abs/2403.01975> |
| ISO 22400-2:2014 제조 운영 관리 KPI 정의 | ISO | 표준 | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | [ref-139](../references/ref-139.md) | <https://www.iso.org/standard/54497.html> |
| WERC DC Measures | WERC(Warehousing Education and Research Council) | 평가 프로그램 | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | [ref-141](../references/ref-141.md) | <https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf> |
| PM4Py | Process Intelligence Solutions | 오픈소스 | [4. 성과·경제성·프로세스 개선](../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | [ref-147](../references/ref-147.md) | <https://github.com/process-intelligence-solutions/pm4py> |
| OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) | OPC Foundation / ISA | 표준 | [1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[2. 공정·워크플로 모델링](../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-130](../references/ref-130.md) | <https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL> |
| osmAG-from-cad (CAD-to-osmAG 파이프라인) | Zhang, J. (jiajiezhang7 GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-084](../references/ref-084.md) | <https://github.com/jiajiezhang7/osmAG-from-cad> |
| Ogm2Pgbm | Vega-Torres, M. A. (MigVega GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-082](../references/ref-082.md) | <https://github.com/MigVega/Ogm2Pgbm> |
| ifc2indoorgml | Diakité, A. A. 외 | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-225](../references/ref-225.md) | <https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/> |
| IDTA 02020 Capability Description 1.0 | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-229](../references/ref-229.md) | <https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description> |
| IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-234](../references/ref-234.md) | <https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles> |
| CaSkMan | CaSkade-Automation (GitHub) | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-231](../references/ref-231.md) | <https://github.com/CaSkade-Automation/CaSkMan> |
| SOMA (Socio-physical Model of Activities) | EASE CRC | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-233](../references/ref-233.md) | <https://github.com/ease-crc/soma> |
| IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) | Helmut Schmidt University, Institute of Automation Technology | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-232](../references/ref-232.md) | <https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2> |
| ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 | ISO | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-240](../references/ref-240.md) | <https://www.iso.org/standard/82334.html> |
| KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 국가표준인증통합정보시스템(KSSN) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-138](../references/ref-138.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010147546> |
| VDMA LIF (Layout Interchange Format) | VDMA | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-046](../references/ref-046.md) | <https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format> |
| IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) | buildingSMART | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-213](../references/ref-213.md) | <https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md> |
| Nav2 Docking Framework (nav2_docking) | ROS Navigation (Open Navigation) | 오픈소스 | [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-216](../references/ref-216.md) | <https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md> |
| IDTA 02020 Capability Description (AAS 서브모델 1.0) | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-243](../references/ref-243.md) | <https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json> |
| IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) | IDTA(Industrial Digital Twin Association) | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-245](../references/ref-245.md) | <https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json> |
| AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) | IDTA(Industrial Digital Twin Association) | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-247](../references/ref-247.md) | <https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf> |
| ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 | ISO | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-248](../references/ref-248.md) | <https://www.iso.org/standard/84589.html> |
| KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 국가표준인증통합정보시스템(KSSN) | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-138](../references/ref-138.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010147546> |
| SkiROS2 | RVMI lab, Aalborg University | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-250](../references/ref-250.md) | <https://github.com/RVMI/skiros2> |
| LIF (Layout Interchange Format) 1.0.0 | VDMA | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-046](../references/ref-046.md) | <https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format> |
| ISO 21423 Industrial mobile robots — Communications and interoperability | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-159](../references/ref-159.md) | <https://www.iso.org/standard/86749.html> |
| IFC 4.3 (IfcSpace) | buildingSMART International | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-156](../references/ref-156.md) | <https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md> |
| OGC IndoorGML 2.0 | OGC | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-157](../references/ref-157.md) | <https://github.com/opengeospatial/IndoorGML-SWG> |
| ISO 19164:2024 Indoor feature model | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-158](../references/ref-158.md) | <https://www.iso.org/standard/83153.html> |
| GS1 GLN (Global Location Number) | GS1 | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[7. 화물·재고·자산 식별과 추적](../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | [ref-162](../references/ref-162.md) | <https://www.gs1.org/standards/id-keys/gln/physical-location> |
| REP 105 Coordinate Frames for Mobile Platforms | ROS (ros-infrastructure/rep) | 프레임워크 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-155](../references/ref-155.md) | <https://www.ros.org/reps/rep-0105.html> |
| ROSA (ROS Agent) | NASA Jet Propulsion Laboratory | 오픈소스 | [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | [ref-171](../references/ref-171.md) | <https://github.com/nasa-jpl/rosa> |
| RAI | Robotec.ai | 오픈소스 | [27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | [ref-175](../references/ref-175.md) | <https://github.com/RobotecAI/rai> |
| free_fleet (Open-RMF 플릿 어댑터) | Open Robotics (open-rmf) | 오픈소스 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-256](../references/ref-256.md) | <https://github.com/open-rmf/free_fleet> |
| ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) | InOrbit | 오픈소스 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-255](../references/ref-255.md) | <https://github.com/inorbit-ai/ros_amr_interop> |
| Open-RMF fleet_adapter_template | Open Robotics (open-rmf) | 오픈소스 | [9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-105](../references/ref-105.md) | <https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml> |
| SLAM Toolbox | Macenski, S. (SteveMacenski GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | [ref-270](../references/ref-270.md) | <https://github.com/SteveMacenski/slam_toolbox> |
| ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) | Open Robotics (ROS 2 Documentation) | 오픈소스 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | [ref-282](../references/ref-282.md) | <https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html> |
| Eclipse Sparkplug (Chapter 5 Operational Behavior) | Eclipse Foundation | 표준 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[19. 모니터링·이상 탐지·원인 분석](../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | [ref-287](../references/ref-287.md) | <https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc> |
| OPC UA Part 4: Services (7.11 DataValue) | OPC Foundation | 표준 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | [ref-288](../references/ref-288.md) | <https://reference.opcfoundation.org/specs/OPC-10000-4/7.11> |
| ISO 23247 제조 디지털 트윈 프레임워크 | ISO (NIST 해설 경유) | 표준 | [8. 실시간 세계 상태·데이터 일관성](../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | [ref-290](../references/ref-290.md) | <https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417> |
| ROS 2 설계 문서 — ROS on DDS · QoS 정책 | ROS 2 Design | 프레임워크 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-298](../references/ref-298.md) | <https://design.ros2.org/articles/qos.html> |
| rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) | ROS 2 (ros2/rmw_zenoh) | 오픈소스 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-299](../references/ref-299.md) | <https://github.com/ros2/rmw_zenoh> |
| KubeEdge | KubeEdge (CNCF) | 오픈소스 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | [ref-300](../references/ref-300.md) | <https://github.com/kubeedge/kubeedge> |
| Open-RMF rmf-web (대시보드·API 서버) | Open Robotics (open-rmf) | 오픈소스 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-302](../references/ref-302.md) | <https://github.com/open-rmf/rmf-web> |
| MQTT Version 5.0 | OASIS | 표준 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-306](../references/ref-306.md) | <https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html> |
| NIST SP 500-325 Fog Computing Conceptual Model | NIST | 프레임워크 | [11. 분산 시스템·통신·컴퓨팅 구조](../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | [ref-303](../references/ref-303.md) | <https://csrc.nist.gov/pubs/sp/500/325/final> |
| KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 산업통상자원부 국가기술표준원 | 표준 | [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | [ref-314](../references/ref-314.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010135682> |
| Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) | Open Robotics (open-rmf) | 오픈소스 | [10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-286](../references/ref-286.md) | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg> |
| KnowRob (하이브리드 지식 베이스) | KnowRob (knowrob GitHub) | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-326](../references/ref-326.md) | <https://github.com/knowrob/knowrob> |
| IEEE1872-owl (CORA 공개 OWL 번역, 제3자) | srfiorini (IEEE1872-owl GitHub) | 오픈소스 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-330](../references/ref-330.md) | <https://github.com/srfiorini/IEEE1872-owl/blob/master/cora-bare.owl> |
| CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) | OGC | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-339](../references/ref-339.md) | <https://docs.ogc.org/is/20-010/20-010.html> |
| IMDF (Indoor Mapping Data Format) 1.0.0 | OGC / Apple | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-338](../references/ref-338.md) | <https://docs.ogc.org/cs/20-094/> |
| BOT (Building Topology Ontology) 0.3.2 | W3C Linked Building Data Community Group | 프레임워크 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-336](../references/ref-336.md) | <https://github.com/w3c-lbd-cg/bot/blob/master/bot.ttl> |
| ifcOWL | buildingSMART | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-342](../references/ref-342.md) | <https://github.com/buildingsmart-community/ifcOWL> |
| Brick Schema | Brick Consortium | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | [ref-341](../references/ref-341.md) | <https://docs.brickschema.org/brick/relationships.html> |
| ISO 16739-1:2024 (IFC 4.3) | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-335](../references/ref-335.md) | <https://www.iso.org/standard/84123.html> |
| Rasa 폼(Forms, Rasa 3.x) | Rasa Technologies | 오픈소스 | [18. 사람–로봇 협업·운영 인터페이스](../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[27. AI·학습·적응과 모델 운영](../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) | [ref-356](../references/ref-356.md) | <https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx> |
| ROS 2 액션 설계(Actions) | ROS 2 Design | 프레임워크 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-363](../references/ref-363.md) | <https://design.ros2.org/articles/actions.html> |
| ROS 2 관리형 노드 수명주기(Managed nodes) | ROS 2 Design | 프레임워크 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[24. 자산·소프트웨어 수명주기 관리](../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) | [ref-364](../references/ref-364.md) | <https://design.ros2.org/articles/node_lifecycle.html> |
| Open-RMF rmf_task | Open Robotics (open-rmf) | 오픈소스 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[20. 예외 복구·재계획·업무 연속성](../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | [ref-366](../references/ref-366.md) | <https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp> |
| IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) | IETF HTTPAPI Working Group | 표준 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[1. 주문·업무 시스템 연계](../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | [ref-367](../references/ref-367.md) | <https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md> |
| OPC UA Part 10: Programs (v1.04) | OPC Foundation | 표준 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-368](../references/ref-368.md) | <https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4> |
| ISA-TR88.00.02 Machine and Unit States (PackML) | ISA | 표준 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-369](../references/ref-369.md) | <https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp> |
| BehaviorTree.CPP | BehaviorTree (GitHub) | 오픈소스 | [12. 명령·작업 실행의 신뢰성](../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | [ref-371](../references/ref-371.md) | <https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h> |
| OR-Tools CP-SAT (스케줄링 레시피) | Google | 오픈소스 | [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | [ref-379](../references/ref-379.md) | <https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md> |
| Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) | Open Robotics (open-rmf) | 오픈소스 | [14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-377](../references/ref-377.md) | <https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp> |
| rmf_task (Open-RMF 작업 계획기 TaskPlanner) | Open Robotics (open-rmf) | 오픈소스 | [13. 작업 배정 — MRTA](../categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[14. 작업 순서·스케줄링](../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-404](../references/ref-404.md) | <https://github.com/open-rmf/rmf_task> |
| ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 | ISO | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-427](../references/ref-427.md) | <https://www.iso.org/standard/70181.html> |
| 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) | National Institute of Building Sciences | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-428](../references/ref-428.md) | <https://www.nationalcadstandard.org/ncs5/pdfs/ncs5_clg_lnf.pdf> |
| KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 | 국가표준인증통합정보시스템(KSSN) | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-429](../references/ref-429.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010129900> |
| 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) | 한국건설기술연구원(건설CALS 체계) | 표준 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-430](../references/ref-430.md) | <https://www.calspia.go.kr/portal/intro/introStandard02.do> |
| ezdxf (DXF 읽기·쓰기 라이브러리) | Moitzi, M. (mozman/ezdxf GitHub) | 오픈소스 | [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | [ref-424](../references/ref-424.md) | <https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst> |
| ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) | ECLASS e.V. | 표준 | [5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | [ref-185](../references/ref-185.md) | <https://eclass.eu/en/eclass-standard/releases> |
| IEC 공통 데이터 사전(IEC CDD) | IEC | 표준 | [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | [ref-183](../references/ref-183.md) | <https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/> |
| rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) | Open Robotics (open-rmf) | 오픈소스 | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[9. 로봇·제조사 관제 연동](../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | [ref-197](../references/ref-197.md) | <https://github.com/open-rmf/rmf_traffic> |
| Open-RMF Traffic Editor | Open Robotics | 오픈소스 | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[21. 온보딩·설정·현장 시운전](../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | [ref-079](../references/ref-079.md) | <https://osrf.github.io/ros2multirobotbook/traffic-editor.html> |
| MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) | DiligentPanda (Team Pikachu, GitHub) | 오픈소스 | [15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | [ref-191](../references/ref-191.md) | <https://github.com/DiligentPanda/MAPF-LRR2023> |
| SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface | SEMI | 표준 | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | [ref-202](../references/ref-202.md) | <https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface> |
| ASTM F3499-21 A-UGV 도킹 성능 시험 방법 | ASTM International | 표준 | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[23. 시험·형식 검증·벤치마크](../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | [ref-204](../references/ref-204.md) | <https://www.astm.org/f3499-21.html> |
| ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 | ANSI / A3 | 표준 | [25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | [ref-210](../references/ref-210.md) | <https://webstore.ansi.org/standards/ria/ansia3r15082023> |
| KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 | 국가표준인증통합정보시스템(KSSN) | 표준 | [25. 안전·위험 관리](../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | [ref-211](../references/ref-211.md) | <https://www.kssn.net/search/stddetail.do?itemNo=K001010083660> |
| Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) | Open Robotics (open-rmf) | 오픈소스 | [17. 로봇 간 협업·물리적 인계](../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[10. 설비·건물 시스템 연동](../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | [ref-499](../references/ref-499.md) | <https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserResult.msg> |
| Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) | Open Robotics (open-rmf) | 오픈소스 | [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) | [ref-536](../references/ref-536.md) | <https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp> |
| Open-RMF rmf_reservation (실험적 예약 라이브러리) | Open Robotics (open-rmf) | 오픈소스 | [16. 공용 자원·충전·에너지 최적화](../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | [ref-538](../references/ref-538.md) | <https://github.com/open-rmf/rmf_reservation> |
<!-- auto:standards-table:end -->

## 읽는 법

- 표의 항목 이름에 링크가 있으면 용어집 항목으로 이어진다. ROS 2 위협 모델과 NIST 협업 로봇 성능은 아직 용어집 항목이 없다.
- ROS 2 DDS-Security 행은 ROS 2 설계 문서 "ROS 2 DDS-Security Integration"을 가리킨다. 그 바탕이 되는 객체 관리 그룹(OMG, Object Management Group)의 DDS(Data Distribution Service) 보안 규격 DDS-Security(표준)는 용어집 항목 [DDS 보안 규격 (DDS-Security)](../glossary/dds-security.md)에서 다루며, 규격 자체는 검증을 거쳐 별도 행으로 등록될 수 있다.
- 관련 세부영역은 구축자가 분류 원문의 인용 위치와 각 항목의 성격을 바탕으로 배정한 것이며, 세부영역 페이지의 "7. 관련 표준·프레임워크·오픈소스" 절이 채워지면 그에 맞춰 조정한다. [가정]
- 표준의 현행 판본·발행일은 대부분 미확인이다. 이번 구축에서는 출처 원문을 열지 못했으므로 아래 각주에 "(원문 미열람)"을 표시했다. 판본이 바뀌거나 대체된 표준은 월간 재검증에서 `needs_update` 또는 `deprecated` 로 처리한다.
- 여기 실린 항목의 기능·성능에 관한 주장은 이 위키에서 확인하지 않았다. 각 항목의 근거 문장과 태그는 용어집 항목과 세부영역 페이지에서 본다.

## 출처

[^ref-001]: ASCM, SCOR Digital Standard, 미확인, https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/, 접근일 2026-09-24 (원문 미열람)
[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-24 (원문 미열람)
[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24 (원문 미열람)
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24 (원문 미열람)
[^ref-007]: NIST, Performance of Collaborative Robot Systems, 미확인, https://www.nist.gov/programs-projects/performance-collaborative-robot-systems, 접근일 2026-09-24 (원문 미열람)
[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24 (원문 미열람)
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24 (원문 미열람)
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24 (원문 미열람)

- 참고문헌 페이지: [ref-001](../references/ref-001.md), [ref-002](../references/ref-002.md), [ref-003](../references/ref-003.md), [ref-004](../references/ref-004.md), [ref-007](../references/ref-007.md), [ref-008](../references/ref-008.md), [ref-009](../references/ref-009.md), [ref-010](../references/ref-010.md)
- [용어집](../glossary/index.md)
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
      "diff_summary": "영역 심화: 3~11절 신규 작성(협동 피킹 조율, VDA 5050 운용 모드·안전 상태, 관제 대시보드, 안전 표준·국내 가이드, 설명·감독, 트랙 자연어 업무 지시 챗봇 반영 제안 6건 검토 반영), 페이지 상태 자동 영역 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area18-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 18. 사람–로봇 협업·운영 인터페이스 의 \"6. 대표 접근법과 기술\" 절(1,787자)을 옮겼다. 27. AI·학습·적응과 모델 운영 링크를 주제 페이지 기준 경로로 고침"
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
        "docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md"
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
    "형식 검증 재작성: docs/topics/2026/2026-09-25-area18-s6.md 의 깨진 링크 ../g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md 를 주제 페이지 기준 경로 ../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md 로 고쳤다. 세부영역 페이지 4절 첫 항목의 빠진 목록 기호('- ')를 보정했다. 주장·태그·각주는 바꾸지 않았다. logs/daily/2026-09-25.md 의 깨진 링크는 스토리텔러 산출물이 아니어서 고치지 못했다(additional_research_requests 에 기록)."
  ]
}
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
| 시설·설비 제어 | 비상 경보를 받아 로봇 작업을 멈추고 대기 위치로 보내는 작업 측 대응(Open-RMF 데모는 경보 시 가장 가까운 주차 위치로 보낸다) [사실][^ref-104] | 시설 비상정지와 설비 안전 제어(연계 대상) |
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
sources: [ref-031, ref-051, ref-104, ref-176, ref-272, ref-275, ref-278, ref-279, ref-302, ref-351, ref-353, ref-356, ref-417, ref-418, ref-467, ref-468, ref-469, ref-476, ref-477]
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

VDA 5050 최신판 명세(2026-09-25 확인)에서 SEMIAUTOMATIC 은 관제가 제어하고 주행 속도는 HMI(Human-Machine Interface, 사람–기계 인터페이스)가, 조향은 자동으로 제어한다. INTERVENED 는 운영자가 HMI로 조향·속도·하역 장치를 제어하며, 관제는 복귀 뒤 실행될 주문을 보낼 수 있고 즉시 동작은 cancelOrder 만 보낼 수 있다. MANUAL 에서는 관제가 주문·동작을 보내지 않는다. [사실][^ref-031] 안전 상태와 일시정지는 로봇이 보고하는 값이므로, 운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이다. [사실][^ref-051]

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


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 세부영역 페이지 9절 표 '시설·설비 제어' 행의 'ROP가 직접 맡는 것' 칸: '비상 경보를 받아 로봇 작업을 멈추고 대기 위치로 보내는 작업 측 대응'을 ROP 직접 범위의 사실처럼 쓰지 않는다. 이 칸은 '시설 비상 경보 상태를 받아 작업 흐름에 반영하는 것으로 보인다 [추정][^ref-104]' 수준으로 낮추거나 비우고, Open-RMF 데모 내용은 '(Open-RMF 데모는 경보 시 로봇을 가장 가까운 주차 위치로 보낸다) [사실][^ref-104]'로 따로 적는다. '멈추고'는 삭제한다 — f10 은 데모 기능만 뒷받침하며, ROP 역할 배정은 f31 에 없는 브리프 밖 주장이고 '멈춘다'는 출처에 없다.
    - 주제 페이지 docs/topics/2026/2026-09-25-area18-s6.md 3절 '운용 모드·일시정지·비상정지 보고' 소절 마지막 문장 '안전 상태와 일시정지는 로봇이 보고하는 값이므로, 운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이다. [사실][^ref-051]'을 둘로 나눈다: '안전 상태와 일시정지는 로봇이 보고하는 값이다. [사실][^ref-051]' / '운영 인터페이스는 이를 받아 사람에게 보여 주는 쪽이 될 것으로 보인다. [추정][^ref-051][^ref-470]' — 뒷부분은 f31 의 [추정]이며 태그를 올릴 수 없다.
- 검증 노트: 판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. 확인 29건, 미확인 2건(f7, f20), 교차 확인 0건. 강등: f7 사실 → 추정(VDA 5050 SEMIAUTOMATIC·INTERVENED 설명이 명세 표 10·11과 불일치해 원문대로 고쳐 씀), f15 사실 → 추정(기사 단일 출처), f20 사실 → 추정(분석 건수 44건/35건 불일치, 미확인). 원문 미열람 출처: ref-467~ref-480, ref-272, ref-275, ref-279, ref-176, ref-278, ref-351, ref-353, ref-356, ref-417, ref-418. 검증자가 GitHub 원문으로 확인한 것은 ref-051(state.schema), ref-302(rmf-web), ref-104(rmf_demos)와 입력 원문 ref-031 이다. 주의: 사람 피커–로봇 대기에 관한 근거는 논문 모델·계산 실험 기준이며 국내 현장 실측은 없다. 안전 표준(ISO 3691-4, ISO 10218:2025, R15.08)은 원문을 열지 못했고 ISO 10218 은 A3 해설 기준이다. 안전 기능은 연계 대상이며 ROP 역할(f31)은 추정이다. 원격 조작 관련 근거는 없다. 정정 요청 없음. oq-009 는 해결로 바꾸지 않는다. / 2차 수정 후 재검증. 드리프트 2건(9절 '시설·설비 제어' 행에서 Open-RMF 데모 기능을 ROP 직접 범위의 사실로 배정하고 '멈추고'를 더함, 분리 주제 페이지 6절에서 f31 의 추정을 [사실]로 씀) 수정 지시. 1차 수정 지시 16건은 모두 이행 확인(f7 표 10·11 기준 재서술, f30 두 유형, 열린 질문 후보 3 제외, f11·f13·f12·f28 문구, 강등 3건, 벤더 주장·원문 미열람 병기, 25·27 연결). [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 통과). 참고: 세부영역 페이지 프런트매터 sources 는 분리 주제 페이지로 옮긴 절의 출처까지 포함해 본문 각주보다 많다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
