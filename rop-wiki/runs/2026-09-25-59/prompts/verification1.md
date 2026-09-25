(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-59
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 23. 시험·형식 검증·벤치마크 (F. 도입·검증·유지관리)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-25-59/target.json

```json
{
  "run_id": "2026-09-25-59",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 59,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 23,
    "area_name": "23. 시험·형식 검증·벤치마크",
    "category": "F. 도입·검증·유지관리",
    "category_letter": "F"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=23"
}
```

### runs/2026-09-25-59/research.json

```json
{
  "run_id": "2026-09-25-59",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 23,
    "area_name": "23. 시험·형식 검증·벤치마크",
    "category": "F. 도입·검증·유지관리"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크 구분 필요)",
    "섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음(22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분 필요)",
    "섹션 11. 열린 질문 비어 있음(대상 영역 열린 질문 oq-055·oq-058·oq-063·oq-077 반영 필요)"
  ],
  "research_questions": [
    "업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]",
    "로봇 시스템 시험에서 장애 주입·시나리오 기반 시뮬레이션 시험·회귀 시험은 어떤 도구와 방식으로 이루어지며 실무의 어려움은 무엇인가? (섹션 3·4·6 겨냥)",
    "다중 로봇·AGV 시스템의 교착·제약 위반을 형식 검증(모델 검사, BDD 기반 분석)과 런타임 검증으로 확인하는 연구·도구는 무엇인가? (섹션 6·8 겨냥)",
    "다중 로봇 경로·작업 배정 알고리즘과 로봇 작업 능력을 비교하는 벤치마크·대회(MAPF 벤치마크, League of Robot Runners, NIST ARIAC)는 무엇을 어떻게 측정하며, 격자 가정 성과가 실제 처리량으로 이어지는가? (섹션 7·8 겨냥, oq-058)",
    "이동로봇·무인운반차의 안전·성능 시험을 정하는 표준(ISO 3691-4, ASTM F45, KS B ISO 18646)과 국내 시험기관(한국로봇산업진흥원)의 시험 항목은 무엇인가? (섹션 7·9 겨냥, 한국 자료 우선)",
    "VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (oq-055, 섹션 9·11 겨냥)",
    "ROP 가 직접 맡을 시험 범위(오케스트레이션 논리·인터페이스·장애 대응)와 제조사·시험기관에 맡길 범위(로봇 자체 안전·주행 성능)는 어떻게 나뉘는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "NIST ARIAC 2025 문서는 경진 중 컨베이어 정지, 전압 시험기 데이터 중단, 진공 공구 파지 실패, 고우선 주문 투입을 '민첩성 도전 과제'로 주입해 시스템의 장애 감지·복구와 긴급 요청 대응을 시험한다.",
      "tag": "사실",
      "source_ids": [
        "ref-629"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ARIAC 2025 문서 challenges 페이지: Conveyor Malfunction(검사 컨베이어 정지), Voltage Tester Malfunction(데이터 전송 중단), Vacuum Tool Malfunction(파지 중 공구 실패, 재시도 필요), High Priority Order(시간 제약 안의 긴급 주문) 네 가지를 둔다.",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f2",
      "claim": "NIST ARIAC 2025 채점은 제출한 키트·모듈의 완료 비율로 기본 점수를 주고 시간 안 완료·고우선 주문 신속 처리·센서 예산 준수 등에 가점을, 충돌·정상 부품 낙하·잘못된 위치 배치 등에 감점을 준 뒤, 시행별 상위 2회 평균 실행 점수(80%)와 심사위원 평가(20%)를 합친다.",
      "tag": "사실",
      "source_ids": [
        "ref-630"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "scoring 페이지: 기본 점수 B = ω1·(k_c/k_d) + ω2·(m_c/m_d), 실행 점수 R = B + Σβ − Σρ·o, 시행 점수는 상위 2회 평균. 최종 순위는 실행 점수 80%와 심사위원 평가 20%.",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f3",
      "claim": "ARIAC 가 장애를 시험 중에 계획적으로 주입하고 완료·시간·비용(센서 예산)·위반을 한 점수로 묶는 방식은, 물류 현장 오케스트레이션의 회귀 시험에서도 장애 시나리오와 처리량·시간·비용 지표를 함께 판정 기준으로 두는 틀로 옮겨 쓸 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-629",
        "ref-630"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ARIAC 는 장애 주입형 도전 과제(challenges)와 가점·감점 채점(scoring)을 함께 둔다. 제조 키팅 과제 기준이며 물류 현장 적용은 검증되지 않았다.",
      "as_of": "2025",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "Luckcuck 외(2019)의 자율 로봇 형식 명세·검증 조사 논문은 자율 로봇 시스템이 복잡하고 혼성적이며 안전 필수인 경우가 많아, 시험과 시뮬레이션만으로는 정확성 보장이나 인증 근거로 충분하지 않다고 보고 형식 방법의 과제·형식체계·접근법을 분류했다.",
      "tag": "사실",
      "source_ids": [
        "ref-631"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ACM Computing Surveys 52(5) 논문 100, 2019. 요지: testing and simulation alone are insufficient 로 형식 명세·검증의 필요를 제기하고 과제·형식체계·접근법을 분류한다.",
      "as_of": "2019-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "von Berg·Aichernig·Wedenik(FM 2026 사례 연구)은 정해진 경로망을 따라 움직이는 창고 AGV 시스템을 세 가지 방식으로 전이 시스템에 인코딩하고 이진 결정 다이어그램(BDD)으로 기호적 분석해, 합성 레이아웃과 실제 레이아웃 모두에서 교착 회피를 수행했다.",
      "tag": "사실",
      "source_ids": [
        "ref-643"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Formal Methods 2026(FM 2026, 도쿄) 사례 연구 논문. 창고 물류 AGV 교착 회피, 세 가지 전이 시스템 인코딩, BDD 기호 분석, 합성·실제 레이아웃 평가(검색 요약 기준).",
      "as_of": "2026-05",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "Afzal 외(ICST 2020)는 로봇 실무자 면담으로 로봇 시스템 시험 실무 12가지와 어려움 9가지를 도출해 실세계 복잡성, 커뮤니티와 표준, 구성요소 통합의 세 주제로 묶었고, 이를 로봇 시스템 시험에 초점을 맞춘 첫 연구로 소개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-632"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IEEE ICST 2020 pp.96–107. 반구조화 면담 기반 질적 연구. 12 testing practices, 9 challenges, 3 themes(검색 요약 기준).",
      "as_of": "2020",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "ros2_fault_injection 은 ROS 2 토픽을 *_raw 로 돌려 받아 편향·잡음·지연·누락·명령 정지 같은 장애를 넣어 다시 발행하고, 서비스 강제 실패와 좌표 변환 손상도 지원하며, YAML 시나리오의 단정(assertion)으로 합격·불합격을 내고 헤드리스 실행기가 종료 코드로 지속적 통합(CI)에 결과를 넘긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-633"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 단정은 장애를 넣지 않고 'observe framework events and publish pass/fail results'. fault_scenario_runner_node 는 CI 용 종료 코드, fault_campaign_runner_node 는 파라미터 스윕과 요약 보고서.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "연계 대상: ros2_fault_injection 이 기본으로 다루는 오도메트리·레이저 스캔·IMU 등 센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하고, ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-633"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "지원 토픽: Odometry, LaserScan, JointState, IMU, PointCloud2, Twist, TFMessage, 서비스는 std_srvs/Trigger. 관제·작업 수준 메시지용 기본 주입기는 README 에 없다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "ROSMonitoring 은 YAML 설정으로 ROS 토픽·서비스를 관찰하는 감시 노드를 생성하며, 온라인 모드에서는 외부 판정기(oracle)의 판정을 받아 위반 메시지를 기록하거나 걸러 내고 오프라인 모드에서는 사건만 기록하는 명세 형식 비종속 런타임 검증 틀로 ROS 1·ROS 2 를 모두 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-634"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: 생성된 감시기는 ROS 노드이고 JSON-over-WebSocket 판정기를 쓰며 formalism-agnostic 이다. 위반 시 logging 또는 filtering(안전하지 않은 메시지·서비스 요청 차단).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "Open-RMF 시뮬레이션 문서는 시뮬레이션에 쓴 코드를 실제 시스템에서 수정 없이 실행하므로 시뮬레이션의 반복 가능한 시나리오로 버그 수정을 확인하고, 드물지만 심각한 예외 상황과 장시간 운전을 배치 전에 시험할 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-667"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation 장: 'As scenarios in simulation are repeatable, fixes for undesirable bugs encountered can be readily validated.' 장시간 시뮬레이션이 배치 전 시설 소유자의 신뢰를 높인다고 적는다. 지속적 통합(CI)은 다루지 않는다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Stern 외(2019)는 다중 에이전트 경로 찾기(MAPF) 논문마다 가정과 목적함수가 달라 기준선 비교가 어렵다는 문제를 들어 공통 용어를 정리하고 새 격자 기반 벤치마크를 소개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-635"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SoCS 2019 'Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks'. 가정·목적을 통일된 용어로 기술하고 grid-based benchmark 를 제시(초록 기준).",
      "as_of": "2019",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "League of Robot Runners 는 Amazon Robotics 가 후원하는 다중 로봇 조율 대회로, MAPF 의 핵심 과제를 찾고 벤치마크 인스턴스를 만들어 최신 성과를 추적하는 것을 목표로 하며 로봇 동역학·지속형 계획·작업 배정·실시간 실행을 창고 물류 같은 응용을 겨냥해 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-636"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ICAPS 2024 시스템 시연 초록: 핵심 과제 식별, 적합한 벤치마크 인스턴스 개발, 알고리즘 성능 평가와 최신 성과 추적. 응용 예로 창고 물류·JIT 제조(검색 요약 기준).",
      "as_of": "2024",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "LSMART(2026)는 기존 MAPF·지속형 MAPF 연구가 단순화한 운동 모델과 완전한 실행·통신을 가정한다는 한계를 들어, AGV 플릿 관리 시스템(FMS) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터를 내고 언제 계획할지·어떻게 계획할지·계획 실패 시 어떻게 복구할지를 비교했다.",
      "tag": "사실",
      "source_ids": [
        "ref-637"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2602.15721. 설계 선택 세 가지(when to plan, how to plan, how to recover)를 최신 방법으로 실험. pebble motion·perfect execution 가정 비판(초록 기준).",
      "as_of": "2026-02",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "연계 대상: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정하며, 사람 감지 시험·안정성 시험과 부속서의 검증 절차를 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-638"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 3691-4:2023 범위: safety requirements and the means for their verification. 예시로 automated guided vehicle, autonomous mobile robot 등을 든다. 사람 감지·안정성 시험, Annex E 검증 절차(검색 요약 기준).",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "연계 대상: ASTM F45 위원회(무인 자동 유도 산업 차량)는 용어·권고 관행·시험 방법을 개발하며 환경 영향, 도킹·주행, 물체 감지·보호, 통신·통합 분과를 두고, NIST 가 이 표준 개발에 참여한다.",
      "tag": "사실",
      "source_ids": [
        "ref-639"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NIST 'ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles' 과제 페이지. 분과 F45.01~F45.04, F45.91 용어. 도킹·주행 시험 방법 예: F3244 Navigation: Defined Area(검색 요약 기준).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "연계 대상: KS B ISO 18646 시리즈는 서비스 로봇의 성능 기준과 관련 시험 방법을 KS 로 부합화한 것으로, 제1부는 바퀴형 로봇의 이동 능력을 다루고 주행·조작 등을 다루는 다른 부가 함께 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-640"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN: KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부: 바퀴형 로봇의 이동능력. 검색 요약상 제2부 주행, 제3부 조작이 있다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "한국로봇산업진흥원은 로봇 시험평가에 KS·ISO·IEC·CISPR 등 표준 시험 방법을 적용하고, 경사 노면·특수 노면·계단·주행 내구 같은 로봇 주행 성능 시험을 수행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-641"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KIRIA 첨단로봇 실증지원 디지털 플랫폼 시험평가 페이지: 표준 시험평가 방법 적용, 로봇 주행 성능 시험 항목(검색 요약 기준). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 대응 인트라로지스틱스 소프트웨어 업체들과 인증을 마쳤다고 발표했다.",
      "tag": "추정",
      "source_ids": [
        "ref-642"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: OTTO 보도자료 'OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments'. 인증 주체는 각 플릿 관리 소프트웨어 업체(검색 요약 기준). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "oq-055 관련: 이번 조사에서 VDA 5050 공식 인증 기관이나 공식 적합성 시험 절차는 확인하지 못했고, 확인된 인증은 로봇 제조사와 관제 소프트웨어 업체 사이의 쌍별 연동 인증 형태여서, ROP 는 새 로봇 연동마다 자체 인수 시험을 두어야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-642"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "OTTO 발표의 인증은 Idealworks·NAiSE·SYNAOS 와의 개별 인증이다. 공식 시험 절차를 검색 범위 안에서 찾지 못했다는 뜻이며 부재가 확인된 것은 아니다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "Open-RMF 시뮬레이션이 강조하는 시나리오 반복·예외 상황 탐색 환경은 22. 시뮬레이션·예측용 디지털 트윈과 공유되지만, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측을, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인을 목적으로 나누는 것이 분류 원문 정의에 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-667"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Open-RMF 시뮬레이션 장의 반복 가능한 시나리오·예외 상황·장시간 시험 설명을 근거로 한 목적 구분. (재인용: 2026-09-25-56)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "분류 원문 질문 '업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가?'에 대해, 확인한 자료로 보면 반복 가능한 시뮬레이션 시나리오에 장애 주입과 합격 판정 단정을 붙여 지속적 통합에서 매 변경마다 다시 돌리는 방식이 답이 될 것으로 보이나, 물류 오케스트레이션 소프트웨어에 이를 적용해 결과를 공개한 현장 사례는 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-629",
        "ref-633",
        "ref-667"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ARIAC 의 장애 주입형 과제, ros2_fault_injection 의 시나리오 단정·CI 실행기, Open-RMF 의 반복 가능한 시뮬레이션 시나리오를 합친 추론이다. 물류 현장 적용 사례는 미확인.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f22",
      "claim": "시나리오 예시(가상): 피킹 단계에서 플릿 어댑터를 업데이트한 뒤, 운반 중인 로봇이 멈추는 장애를 주입하고 작업이 재배정되는지와 완료 확인 전에는 재고 변경이 확정되지 않는지를 단정으로 확인하는 회귀 시험을 구성할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-629",
        "ref-633"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ARIAC 의 공구 파지 실패 후 재시도 과제와 ros2_fault_injection 의 명령 정지·서비스 강제 실패·단정 구조를 물류 흐름에 대응시킨 구성안이며 실제 사례가 아니다.",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "완료·인계"
    },
    {
      "id": "f23",
      "claim": "ROP 가 직접 맡을 시험 몫은 작업 배정·교통 관리 논리의 교착·제약 위반 검증, 관제 인터페이스 적합성, 장애 주입 시 재배정·복구 동작의 회귀 시험, 운영 중 런타임 감시로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-643",
        "ref-633",
        "ref-634",
        "ref-667"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "BDD 기반 AGV 교착 분석(FM 2026), ROS 2 장애 주입·런타임 검증 도구, Open-RMF 의 동일 코드 시뮬레이션 구조를 분류 원문 9장 경계에 맞춰 정리한 추론이다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": false
    },
    {
      "id": "f24",
      "claim": "연계 대상: 로봇 자체의 사람 감지·안정성 같은 안전 검증(ISO 3691-4)과 주행·도킹·이동 성능 시험(ASTM F45, KS B ISO 18646, 한국로봇산업진흥원 주행 성능 시험)은 제조사와 시험기관 영역이고, ROP 는 그 결과를 로봇 등록·배정 조건의 입력으로 받는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-638",
        "ref-639",
        "ref-640",
        "ref-641"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "네 출처 모두 개별 차량·로봇 단위의 안전·성능 시험을 다루며 다중 로봇 관제 소프트웨어 수준의 시험 항목은 검색 요약에 나타나지 않았다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-629",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Challenges",
      "published": "2025",
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "ARIAC 2025 의 민첩성 도전 과제(컨베이어·전압 시험기·진공 공구 고장, 고우선 주문)를 설명한다. 공식 저장소 Sphinx 원본을 열어 읽었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/challenges.rst",
      "source_unopened": false
    },
    {
      "id": "ref-630",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Scoring",
      "published": "2025",
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "ARIAC 2025 채점 방식(완료 기반 기본 점수, 가점·감점, 상위 2회 평균, 실행 80%·심사 20%)을 설명한다. 공식 저장소 원본을 열어 읽었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/scoring.rst",
      "source_unopened": false
    },
    {
      "id": "ref-631",
      "org": "Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M.",
      "title": "Formal Specification and Verification of Autonomous Robotic Systems: A Survey",
      "published": "2019-09",
      "url": "https://arxiv.org/abs/1807.00048",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 로봇 형식 명세·검증의 과제·형식체계·접근법을 분류한 조사 논문(ACM Computing Surveys 52(5)).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-632",
      "org": "Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S.",
      "title": "A Study on Challenges of Testing Robotic Systems",
      "published": "2020",
      "url": "https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 실무자 면담으로 시험 실무 12가지와 어려움 9가지를 도출한 질적 연구(IEEE ICST 2020).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-633",
      "org": "reeceholland (ros2_fault_injection GitHub)",
      "title": "ros2_fault_injection — README",
      "published": null,
      "url": "https://github.com/reeceholland/ros2_fault_injection",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 토픽·서비스·TF 에 장애를 주입하고 YAML 시나리오 단정으로 합격·불합격을 내는 C++ 틀. 개인 주도 프로젝트라 성숙도는 미확인. README 원문을 열어 읽었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/reeceholland/ros2_fault_injection/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-634",
      "org": "University of Liverpool Autonomy and Verification (ROSMonitoring GitHub)",
      "title": "ROSMonitoring: a Runtime Verification Framework for ROS — README",
      "published": null,
      "url": "https://github.com/autonomy-and-verification-uol/ROSMonitoring",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "ROS 1·2 용 런타임 검증 틀. 감시 노드 생성, 외부 판정기 연동, 위반 기록·차단. README 원문을 열어 읽었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/autonomy-and-verification-uol/ROSMonitoring/master/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-635",
      "org": "Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외",
      "title": "Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks",
      "published": "2019",
      "url": "https://arxiv.org/abs/1906.08291",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MAPF 가정·목적의 공통 용어와 격자 기반 벤치마크를 제시한 논문(SoCS 2019).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-636",
      "org": "IDM Lab (USC) 게재 초록, 저자 미확인",
      "title": "The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration]",
      "published": "2024",
      "url": "https://idm-lab.org/bib/abstracts/Koen24p.html",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Amazon Robotics 후원 다중 로봇 조율 대회의 목표·설계를 소개한 ICAPS 2024 시스템 시연 초록.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-637",
      "org": "arXiv 게재 논문(저자 미확인)",
      "title": "Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems",
      "published": "2026-02",
      "url": "https://arxiv.org/abs/2602.15721",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AGV 플릿 관리 시스템 안에서 MAPF 알고리즘을 현실적으로 평가하는 오픈소스 시뮬레이터 LSMART 와 설계 선택 비교 연구(프리프린트).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-638",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AGV·AMR 을 포함한 무인 산업용 차량의 안전 요구사항과 검증 수단을 정하는 표준의 ISO 소개 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-639",
      "org": "NIST",
      "title": "ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles",
      "published": null,
      "url": "https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 자동 유도 산업 차량의 용어·시험 방법을 개발하는 ASTM F45 위원회와 NIST 참여를 소개하는 과제 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-640",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010113281",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 성능 기준·시험 방법 KS 부합화 표준의 제1부 상세 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-641",
      "org": "한국로봇산업진흥원(KIRIA)",
      "title": "시험평가 | KIRIA 첨단로봇 실증지원 디지털 플랫폼",
      "published": null,
      "url": "https://kiria.org/rp/kiria/tva/inr/page.dn",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇산업진흥원의 표준 기반 로봇 시험평가와 주행 성능 시험 항목 안내 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-642",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": null,
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OTTO AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 대응 소프트웨어 업체와 인증을 마쳤다는 보도자료(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-643",
      "org": "von Berg, B., Aichernig, B. K., & Wedenik, F.",
      "title": "BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper)",
      "published": "2026-05",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 AGV 시스템을 전이 시스템으로 인코딩해 BDD 기호 분석으로 교착을 회피하는 사례 연구(FM 2026).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-667",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션 장. 같은 코드를 시뮬레이션과 실제에 쓰는 구조, 반복 가능한 시나리오, 예외 상황·장시간 시험을 설명한다. 재사용 출처이며 이번 실행에서 미러 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
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
      "rationale": "seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f4(시험·시뮬레이션만으로 불충분), f6(로봇 시험의 어려움), f10(배치 전 반복 시험), f13(격자 가정과 현실 실행의 차이) / 4절 핵심 개념: 장애 주입(f1·f7), 회귀 시험과 CI(f7·f21), 형식 검증·교착(f4·f5), 런타임 검증(f9), 벤치마크(f11·f12) / 5절 현장 시나리오: f22(피킹·완료·인계, 가상 구성안임을 명시), f21(분류 원문 질문, 추정) / 6절 대표 접근법: f1·f3(장애 주입형 시험), f5(BDD 교착 분석), f7·f8(장애 주입 도구), f9(런타임 검증), f10(시뮬레이션 회귀), f13(현실적 MAPF 평가) / 7절 표준·오픈소스: f14(ISO 3691-4), f15(ASTM F45), f16(KS B ISO 18646), f17(한국로봇산업진흥원), f7·f9·f10(오픈소스), f1·f2(NIST ARIAC) / 8절 대표 연구: f4·f5·f6·f11·f12·f13 / 9절 경계: f23(ROP 직접), f8·f14·f15·f16·f24('연계 대상') / 10절 연결: 22. 시뮬레이션·예측용 디지털 트윈(f20), 15. 다중 로봇 경로·교통 관리 — MAPF(f5·f11~f13), 12. 명령·작업 실행의 신뢰성과 19. 모니터링·이상 탐지·원인 분석(f9), 24. 자산·소프트웨어 수명주기 관리(f21, 업데이트 후 재검증), 25. 안전·위험 관리(f14), 9. 로봇·제조사 관제 연동과 28. 표준·상호운용성·다사업자 거버넌스(f18·f19), 20. 예외 복구·재계획·업무 연속성(f13 복구 설계) / 11절 열린 질문: oq-055(f18·f19 부분 근거), oq-058(f13 부분 근거), oq-063, oq-077, open_questions_new 3건. f18 은 [추정]+'벤더 주장' 병기."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "장애 주입",
      "term_en": "Fault Injection",
      "definition": "시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다."
    },
    {
      "term_ko": "회귀 시험",
      "term_en": "Regression Testing",
      "definition": "소프트웨어나 설정을 바꾼 뒤 기존에 통과하던 정상·장애 시나리오를 다시 실행해 변경이 기존 동작을 깨뜨리지 않았는지 확인하는 시험이다."
    },
    {
      "term_ko": "런타임 검증",
      "term_en": "Runtime Verification",
      "definition": "실행 중인 시스템의 사건을 감시기로 관찰해 명세한 성질의 위반을 판정하고 기록하거나 차단하는 검증 기법이다."
    },
    {
      "term_ko": "모델 검사",
      "term_en": "Model Checking",
      "definition": "시스템을 상태 전이 모델로 표현하고 교착 부재 같은 성질이 도달 가능한 모든 상태에서 성립하는지 자동으로 확인하는 형식 검증 기법이다."
    }
  ],
  "open_questions_new": [
    "로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반",
    "BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 15. 다중 로봇 경로·교통 관리 — MAPF | 근거: f5 | 종류: 일반",
    "국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? | 관련 영역: 23. 시험·형식 검증·벤치마크, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f17 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음(단일 출처)",
      "f5·f11·f12·f13: 논문 원문 미열람, 초록·검색 요약 범위",
      "f14: ISO 3691-4 부속서 검증 절차 세부 미확인(유료 표준)",
      "f15: F3244 등 개별 ASTM 시험 방법 내용 미확인",
      "f16: KS B ISO 18646 각 부의 KS 제정일·판 미확인",
      "f18: OTTO 인증의 시험 항목·주체 미확인(벤더 주장)",
      "f19: VDA 5050 공식 적합성 시험 절차의 부재 여부 미확인(검색 요약에 VDMA 가 시험 환경을 계획한다는 언급이 있었으나 출처가 명확하지 않아 쓰지 않음)",
      "ref-636·ref-637 저자 미확인",
      "ref-633 라이선스 미확인"
    ],
    "scope_violations": [
      "f8·f14·f15·f16·f24: 로봇 자체 센서 인식·주행 성능·차량 안전 시험은 분류 원문 9장 '로봇 자체 지능·제어' 쪽 외부 연계 영역이므로 '연계 대상:'으로 표시",
      "f22: 가상 시나리오 구성안이며 실제 사례로 서술하지 않도록 claim 에 '시나리오 예시(가상)' 표기"
    ],
    "budget_used": {
      "queries": 22,
      "sources": 15
    },
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-629·ref-630(NIST ARIAC 2025 challenges·scoring, 미러 목록 경로), ref-633(ros2_fault_injection), ref-634(ROSMonitoring), ref-667(재사용, Open-RMF 시뮬레이션 장). 나머지 11건은 검색 요약 기준(신뢰도 상한 medium). IntelLabs scenario_execution README raw 경로는 main·jazzy 모두 404 라 출처로 넣지 않았다. League of Robot Runners Start-Kit README 는 열었으나 평가 지표가 없어 쓰지 않았다. 검색 22회/30, 신규 출처 15건/15(ref-629~ref-643, 예약 구간 안)로 신규 출처 예산에 도달해 Scenario Execution for Robotics(arXiv 2409.07080), Timed Rebeca 기반 ROS 2 다중 로봇 모델 검사(arXiv 2511.15227), KTL 로봇시험인증센터, arculus VDA 5050 적합성 시험 도구는 출처로 넣지 않았다. 재사용 1건: ref-667(2026-09-25-56 브리프 값 사용). 참고문헌 목록 전체 값이 입력에 없어 ref-007(NIST 협업 로봇 성능)·ref-008(NIST ARIAC)의 기존 값을 재사용하지 못하고 ARIAC 는 개별 페이지 URL 로 새 id 를 붙였다(퍼블리셔 대조 필요). 열린 질문: oq-055 는 f18·f19, oq-058 은 f13 이 부분 근거일 뿐 해결로 보지 않았고, oq-063·oq-077 은 이번에 조사하지 못했다. 한국 자료: KS B ISO 18646(ref-640), 한국로봇산업진흥원(ref-641). 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 섞지 않았고, 22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분은 f20(의견)으로만 냈다. 정정 요청 없음."
  }
}
```

### docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크"
type: area
category: "F. 도입·검증·유지관리"
area_no: 23
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [F. 도입·검증·유지관리](index.md) › 23. 시험·형식 검증·벤치마크

# 23. 시험·형식 검증·벤치마크

!!! info "소속 대분류"
    [F. 도입·검증·유지관리](index.md) — 핵심 질문:
    새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [분류원문]

## 2. SCM 관점의 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]

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

### docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md (요약)

```markdown
# 21. 온보딩·설정·현장 시운전

소속 대분류: F. 도입·검증·유지관리 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [분류원문]

## 2. SCM 관점의 질문

새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md (요약)

```markdown
# 22. 시뮬레이션·예측용 디지털 트윈

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [분류원문]

## 2. SCM 관점의 질문

성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]

> 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md (요약)

```markdown
# 24. 자산·소프트웨어 수명주기 관리

소속 대분류: F. 도입·검증·유지관리 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [분류원문]

## 2. SCM 관점의 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 513건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 133개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoorgml: IndoorGML (IndoorGML)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
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
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- order-batching: 주문 배치 (Order Batching)
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
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [23] 에 걸린 4건 / 전체 83건)

```markdown
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 9, 23, 28)
- oq-058 [열림] 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (영역 15, 23)
- oq-063 [열림] ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? (영역 17, 23)
- oq-077 [열림] 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? (영역 21, 6, 23)
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
# area_no 는 1~28 의 세부영역 번호다. 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 7. 화물·재고·자산 식별과 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 7            # 7. 화물·재고·자산 식별과 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "팔레트 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 7            # 주 연구영역: 7. 화물·재고·자산 식별과 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 팔레트 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 7            # 7. 화물·재고·자산 식별과 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1~7). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-09-25-58/research.md

```markdown
# 리서치 브리프 2026-09-25-58

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-58 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 3 · 답한 질문 q3-02

## 갭(비어 있거나 약한 섹션)

- 단계 3 질문 q3-02 열림(target.json 지정, CLI 지정 질문 id). 단계 3 페이지 3절에 q3-02 소제목 없음
- 완료 조건: 아이디어 3. 건축 도면 자동 인식 5절 '핵심 구성 요소' 소절이 '아직 조사되지 않음'(공간 그래프 단위 q3-02 미답)
- 완료 조건: 공간 그래프 스키마 초안 v0.6 에 단계 3 근거 갱신 없음 — 공간 노드와 주행 경유점·차선의 구분, 엣지 통과 조건, 공용 자원 예약 단위가 6절 미해결 질문으로만 남아 있음
- 6. 지도·공간·위치 모델 6절(주제 페이지 분리)에 공간 그래프의 노드·엣지 단위와 층위(구역 수준·차선 수준) 구분이 없음
- 16. 공용 자원·충전·에너지 최적화 쪽에 문·승강기·충전 위치를 그래프에서 예약 단위로 표현하는 근거 없음

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q3-02 공간 그래프의 노드(방·구역·문·엘리베이터·계단·충전 위치)와 엣지(연결·통과 조건)를 어떤 단위로 정해야 배정·경로·자원 예약에 모두 쓰이는가?
3. 오픈소스 관제(Open-RMF rmf_traffic·traffic-editor·건물 지도 메시지)는 경유점·차선을 어떤 속성으로 두고 문·승강기·충전소·상호 배제를 그래프 어디에 표현하는가? (단계 3 페이지 3절, 스키마 초안 2·3절 겨냥)
4. VDA 5050 3.0.0 주문의 노드·엣지는 어떤 통과 조건 속성을 갖고, 로봇별 통행 제한과 구역 단위 접근 허가(RELEASE 구역)는 어디에 두는가? (16. 공용 자원·충전·에너지 최적화 연결)
5. 실내 공간 표준·연구는 공간 노드의 세분화 수준과 층위 사이 포함 관계를 어떻게 다루는가? (국내 연구 포함, 한국 자료 우선 규칙)
6. 경로망의 노드 배치·엣지 방향은 다중 로봇 교통 성능에 어떤 영향을 주며, 도면에서 만든 차선 그래프를 그대로 써도 되는가? (15. 다중 로봇 경로·교통 관리 — MAPF 연결)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF rmf_traffic 의 그래프 API 에서 경유점(Waypoint)은 지도 이름·위치와 함께 대기 지점·통과 전용 지점·주차 위치·충전소 여부, 상호 배제 그룹, 승강기 안 위치 여부(LiftProperties)를 속성으로 갖는다. | ref-689 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | rmf_traffic 의 차선(Lane)은 진입·진출 노드와 그 노드에 걸리는 이벤트(문 열기·닫기, 승강기 세션 시작·이동·문 열기·종료, 도킹, 대기), 선택적 속도 제한, 상호 배제 그룹으로 이루어져 문·승강기를 그래프 노드가 아니라 차선 이벤트로 표현한다. | ref-689 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | rmf_traffic 에서 상호 배제 그룹에 속한 경유점·차선은 한 번에 로봇 한 대만 점유할 수 있어, 좁은 구역·공용 자원의 점유 예약을 그래프 요소 묶음 단위로 표현한다. | ref-689 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | Open-RMF traffic-editor 문서는 차선에 양방향 여부·그래프 번호(graph_idx)·주행 방향 제약을 두고 플릿마다 자기 그래프로 허용 동작을 전달하며, 승강기는 층마다 칸 안에 경유점을 만들어 차선으로 잇고 문은 정점 사이에 따로 추가해 차선이 문을 지나게 한다. | ref-079 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f5 | [사실] | Open-RMF 건물 지도 메시지에서 그래프 노드(GraphNode)는 x·y·이름·파라미터 목록만, 그래프 간선(GraphEdge)은 두 꼭짓점 번호·파라미터 목록·양방향/단방향 유형만 가져 통과 조건은 일반 파라미터로 붙는다. | ref-690, ref-691 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | Open-RMF 주행 지도 통합 문서는 경유점마다 층 이름과 미터 좌표, 적재·하역 주차 지점이나 충전소 같은 특수 속성을 요구하고, 차선은 양방향·단방향과 구간 속도 제한을 가질 수 있다고 적는다. | ref-080 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | VDA 5050 주문 JSON 스키마에서 노드는 위치(x·y·방향, 허용 편차 타원·각도, mapId)와 동작 목록을, 엣지는 최대 속도·로봇 최대 높이·적재장치 최소 높이·방향과 방향 유형·주행 방향·회전 조건·궤적(NURBS)·길이·통로(corridor)·동작 목록을 통과 조건으로 갖는다. | ref-692 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f8 | [사실] | VDA 5050 3.0.0 에서 전체 노드·엣지 그래프와 어느 로봇이 어느 엣지를 지날 수 있는지의 제한은 관제가 보유하며 로봇에 전달하지 않고, 관제는 그 로봇이 지날 수 있는 엣지만 주문에 넣는다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f9 | [사실] | VDA 5050 3.0.0 은 지도(mapId)에 붙는 다각형 구역 가운데 RELEASE 구역에 대해 로봇이 상태 메시지로 접근을 요청하고 관제가 응답(GRANTED·QUEUED·REVOKED·REJECTED, 선택적 임대 만료 시각)으로 허가하게 해, 구역 단위 점유 허가를 그래프 밖 다각형으로 표현한다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f10 | [사실] | VDA 5050 3.0.0 에서 충전은 노드나 즉시 동작으로 쓰는 startCharging 으로 표현되며 정지한 충전 지점뿐 아니라 주행 중 충전 차선에서도 할 수 있다고 적는다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f11 | [사실] | Claridades·Choi·Lee(ISPRS IJGI 11, 2022)는 실내 공간의 위계를 여러 수준의 노드–관계 구조(NRS)로 표현하는 세분화(subspacing) 틀을 IndoorGML 핵심 모델 확장으로 제안하고, 표본 자료에서 서로 다른 상세 수준의 네트워크를 생성해 보였다. | ref-694 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f12 | [사실] | Henkel·Toussaint(SAC 2020)는 경로망 정점 위치와 엣지 방향을 확률적 경사하강으로 최적화한 방향 경로망(ODRM)이 벽에 나란한 엣지, 양방향 두 차선 도로·회전교차로 같은 패턴을 만들어 다중 로봇 충돌 회피에 유리하다고 보고했다. | ref-693 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f13 | [사실] | 연계 대상: 로봇 인식으로 만드는 계층형 3D 장면 그래프는 메시·객체·장소(주행 가능 영역)·방 층을 두고 층 안 엣지는 공간 제약, 층 사이 엣지는 포함 관계로 두며, 이 계층을 이용해 대규모 환경의 작업·동작 계획 문제를 희소하게 구성하는 연구가 있다. | ref-695 | 아니오 | medium | 2024-03 | — | 원문 미열람 |
| f14 | [추정] | 확인한 표현을 종합하면 공간 그래프는 배정·장소 이름 해석에 쓰는 구역 수준 노드(방·구역·업무 장소)와 경로 계획·교통에 쓰는 차선 수준 경유점·차선을 서로 다른 층위로 두고 포함 관계로 잇는 구조여야 세 용도에 함께 쓰일 것으로 보인다. | ref-689, ref-079, ref-692, ref-694, ref-695 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [추정] | 확인한 관제 형식에서 문·승강기는 차선 이벤트와 승강기 칸 경유점, 좁은 구역은 상호 배제 그룹이나 RELEASE 구역 다각형, 충전은 노드 동작으로 흩어져 표현되므로, 자원 예약의 단위는 그래프 노드 하나가 아니라 공용 자원 개체가 자신이 걸친 경유점·차선·구역을 가리키는 형태로 두어야 할 것으로 보인다. | ref-689, ref-079, ref-031 | 아니오 | low | 2026-09-25 | 제약 | — |
| f16 | [추정] | 확인한 엣지 속성은 속도·높이·방향·통로·이벤트 같은 운동·설비 조건이고 계단 주행·문 조작 같은 로봇 능력 조건은 엣지 속성이 아니라 플릿별 그래프(Open-RMF)나 관제가 보유한 로봇별 통행 제한(VDA 5050)으로 처리되므로, 공간 그래프는 플릿 중립의 기본 그래프와 로봇별 통행 가능 여부를 분리해 두는 것이 맞아 보인다. | ref-692, ref-031, ref-079 | 아니오 | low | 2026-09-25 | 제약 | — |
| f17 | [추정] | 분류 원문 질문의 ‘3층 출하 대기장’은 구역 수준 노드 하나로 두고 이름·층을 붙인 뒤, 제조사 플릿마다 그 구역에 포함되는 경유점·스테이션을 대응시키는 방식이면 제조사별 지도 차이를 흡수할 수 있을 것으로 보인다. | ref-079, ref-692, ref-212 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f18 | [추정] | 경로망의 정점 배치와 엣지 방향이 다중 로봇 충돌 회피와 경로망 품질을 좌우한다는 연구를 보면, 도면 인식으로 얻은 차선 수준 그래프는 최종 경로망이 아니라 경로망 자동 생성·최적화의 입력 초안으로 두는 것이 맞아 보인다. | ref-693, ref-268 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-689 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 아니오 |
| ref-690 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphEdge.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphEdge.msg | 아니오 |
| ref-691 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphNode.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphNode.msg | 아니오 |
| ref-692 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 아니오 |
| ref-693 | Henkel, C., & Toussaint, M. | Optimized Directed Roadmap Graph for Multi-Agent Path Finding Using Stochastic Gradient Descent | 2020-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2003.12924 | 예 |
| ref-694 | Claridades, A. R. C., Choi, H.-S., & Lee, J. | An Indoor Space Subspacing Framework for Implementing a 3D Hierarchical Network-Based Topological Data Model | 2022 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/ijgi11020076 | 예 |
| ref-695 | arXiv 2403.08094 저자(미확인) | Task and Motion Planning in Hierarchical 3D Scene Graphs | 2024-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2403.08094 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html | 아니오 |
| ref-212 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json | 예 |
| ref-268 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 2025-11 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2511.07175 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | 2, 3, 4, 5, 6, 8, 9 | q3-02 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18 (신뢰도 low) — 2절 q3-02 상태 답함, 3절 q3-02 소제목 신설({#q3-02}): 관제 그래프의 경유점·차선 속성(f1·f2·f5·f6·f7), 상호 배제·구역 허가·충전 동작(f3·f9·f10), 플릿별 그래프와 관제 보유 통행 제한(f4·f8), 공간 세분화·계층 연구(f11·f13 연계 대상), 경로망 최적화(f12), 종합: 구역 수준·차선 수준 두 층위(f14), 자원 예약 단위(f15), 통과 조건 분리(f16), 분류 원문 질문(f17), 도면 차선 그래프는 초안(f18) / 4절 결론·불확실성(두 층위 구조는 이 위키의 종합, 단일 출처 없음) / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/floorplan-recognition.md | 5 | 아이디어 페이지 5절 '핵심 구성 요소' 소절 첫 작성(트랙 산출물): 공간 그래프의 두 층위(f14 추정)와 근거 형식(f1·f2·f4·f7·f8), 공용 자원 예약 단위(f15 추정, 근거 f3·f9·f10), 통과 조건 분리(f16). 능력 대조(q3-03)·시뮬레이션 초기값(q3-04)은 아직 없음을 명시 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | 2, 3, 4, 6 | 트랙 산출물 갱신: track.ontology_changes 가 검증 승인되면 개념 '경유점'·'주행 차선' 추가(f1·f2·f4·f5·f6·f7), 관계 '공간 노드 / 포함한다 / 경유점'(f11·f13, 승인 시), 공용 자원 속성 '상호 배제 그룹·점유 요소'(f3·f15). 미승인 제안과 f14·f16 은 6절 질문(q3-02 항목 근거 보강)으로 |
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f11, f14, f17): 6절(주제 페이지 area06-s6)에 공간 그래프를 구역 수준과 차선 수준 층위로 두고 업무 장소 이름을 구역 노드에 붙이는 접근(추정)과 IndoorGML 세분화 연구 |
| update | docs/categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f2, f3, f9, f10, f15): 문·승강기의 차선 이벤트 표현, 상호 배제 그룹, VDA 5050 RELEASE 구역 접근 허가, 충전 동작의 위치, 공용 자원 예약 단위 |
| update | docs/categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md | 6 | 트랙 floorplan-recognition 단계 3 반영 제안 (f4, f7, f12, f18): 플릿별 주행 그래프와 엣지 통과 조건, 방향 경로망 최적화(ODRM), 도면 차선 그래프를 경로망 초안으로 두는 관점 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 상호 배제 그룹 | Mutex Group (Open-RMF) | Open-RMF 주행 그래프에서 한 번에 로봇 한 대만 점유할 수 있도록 묶은 경유점·차선의 집합이다. |
| 공간 세분화 | Subspacing (Indoor Space Subdivision) | 실내 공간을 목적에 맞는 상세 수준의 하위 공간으로 나누고 수준 사이 포함 관계를 유지해 여러 상세 수준의 연결 네트워크를 만드는 방법이다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 12 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 7건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 형식·연구마다 발행 주체 한 곳의 자료만 있음(f5 의 두 출처는 같은 Open Robotics)
    - f11·f12·f13 원문 미열람(검색 요약 범위), ref-695 저자 미확인
    - f13 의 층 구조 설명은 arXiv 2403.08094 검색 요약이 Hydra 를 설명한 문장 기준
    - IndoorGML 2.0 JSON 인코딩 초안(26-043)의 Node·Edge·InterLayerConnection 속성은 미러 HTML 이 머리말 위주로 읽혀 확인하지 못함(첫 열람 응답의 클래스 목록은 재확인 결과 본문에 없어 버림)
    - osmAG 의 영역·통로 태그 구조는 README 에 없어 확인하지 못함
    - f14~f18 은 이 위키의 종합이며 두 층위 구조를 제시한 단일 출처는 찾지 못함
    - rmf_traffic Graph.hpp 의 인용 문구는 WebFetch 요약 모델이 전한 문장이며 docs.ros.org 검색 요약과 일치
- 범위 경계 위반 의심:
    - f13: 3D 장면 그래프는 로봇 센서 인식으로 만드는 표현이라 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 계층 구조 사례로만 제안함
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 신규 ref-689(rmf_traffic Graph.hpp)·ref-690(GraphEdge.msg)·ref-691(GraphNode.msg)·ref-692(VDA 5050 order.schema), 재사용 ref-079(traffic-editor.md)·ref-080(integration_nav-maps.md). ref-031 은 입력 원문 텍스트(inbox). arXiv 는 프록시가 거부해 ref-693~ref-695 는 검색 요약 기준(신뢰도 상한 medium). 재사용 ref-212·ref-268 은 다시 열지 않음. 검색 7회/40, 신규 출처 7건/20(ref-689~ref-695, 예약 구간 안), 재사용 5건. 질문 선택: target.json 지정 q3-02 1건. q3-02 는 확인 사실(관제 그래프의 노드·엣지 속성, 자원 표현 위치, 공간 세분화 연구)을 근거로 '구역 수준·차선 수준 두 층위 + 공용 자원 개체가 점유 요소를 가리킴 + 로봇별 통행 가능 여부 분리'로 답했으나 핵심 종합(f14~f18)이 추정이라 종합 신뢰도 low. 한국 자료: 서울시립대 연구진의 IndoorGML 세분화 연구(ref-694). 한국어 검색 1회에서 물류 현장 사례는 찾지 못함. 교차 규칙: 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 일반 열린 질문 신규 없음(새 질문은 트랙 전용). 후속 질문 2건, 온톨로지 변경 제안 3건. 정정 요청 없음.

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 3
- 답한 질문 id: q3-02

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 도면 인식은 방·구역 같은 구역 수준 노드를 주지만 주행 경유점·차선은 주지 않을 때, 구역 수준 노드와 제조사 플릿별 차선 수준 경유점·스테이션 사이의 포함 관계를 자동으로 만들거나 사람이 확인하는 규칙은 무엇인가? (q3-02 에서 파생) | 3 | f14 |
| — | 플릿 중립의 기본 공간 그래프에서 제조사 플릿별 주행 그래프(Open-RMF graph_idx)나 VDA 5050 관제 보유 통행 제한을 파생·동기화할 때, 로봇별 통행 가능 여부를 어디에 저장하고 도면·지도 판이 바뀌면 어떻게 다시 맞추는가? (q3-02 에서 파생) | 4 | f16 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| add | concept | 경유점 (Waypoint) | f1, f5, f6, f7 | 로봇이 지나거나 머무는 좌표 지점(층·지도 식별자·미터 좌표). 속성 후보: 대기 가능·통과 전용·주차·충전 여부, 허용 편차, 승강기 안 여부. 공간 노드(구역 단위)와 구분되는 차선 수준 개념이며, 공간 노드와 같은 개념으로 볼지에 대해서는 기존 정의와 충돌 가능성이 있어 검토 필요. |
| add | concept | 주행 차선 (Lane) | f2, f4, f5, f7 | 두 경유점을 잇는 주행 엣지. 속성 후보: 방향(양방향·단방향), 속도 제한, 높이 제한, 주행 방향 제약, 이벤트(문 열기·승강기 세션·도킹), 플릿 그래프 번호. 기존 관계 '문 / 두 공간 노드를 잇는다'(구역 수준)와 층위가 다르다. |
| modify | concept | 공용 자원 (Shared Resource) | f3, f9, f10 | 속성 후보 '점유 요소(자원이 걸친 경유점·차선·구역)'와 '상호 배제 여부'를 더하는 제안. 근거: rmf_traffic 상호 배제 그룹, VDA 5050 RELEASE 구역 접근 허가, 노드 동작으로서의 충전. 종합 판단(f15)은 추정이므로 속성 값은 후보로 둔다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 아이디어 3. 건축 도면 자동 인식 5절 핵심 구성 요소는 이번 제안(q3-02)의 검증 승인 전이며 능력 대조(q3-03)·시뮬레이션 초기값(q3-04) 미답
    - 다른 아이디어와의 연결 근거 없음
    - 공간 그래프 스키마 초안의 단계 3 근거 갱신은 이번 온톨로지 변경 제안의 검증 승인 전
    - 실험 페이지에 제안된 실험 계획 없음
    - 열린 질문 q3-03·q3-04·q3-05·q3-06·q3-07·q3-08
```

### runs/2026-09-25-57/research.md

```markdown
# 리서치 브리프 2026-09-25-57

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-57 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 5. 로봇 능력·작업 온톨로지 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `manual-capability-ontology` · 단계 2 · 답한 질문 q2-01

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-01, q2-02, q2-03 열림(target.json 지정, CLI 지정 질문 id). 단계 2 페이지는 seed 상태로 3절 조사 결과·4절 결론·5절 후속 질문이 비어 있음
- 완료 조건: 문서 유형 매트릭스(document-type-matrix.md) 7행 × 8열 모든 칸 미조사
- 완료 조건: 공개 문서 샘플 목록 비어 있음
- 능력 온톨로지 초안의 근거 문서 개념에 문서 유형·정보 형태·이용 조건 속성이 없음(6절 '근거 문서의 단위와 버전' 질문)
- 아이디어 1. 로봇 기능 온톨로지 4절에 제조사 문서 유형·형태 근거 없음

## 조사 질문

1. 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [분류원문]
2. q2-01 제조사가 제공하는 문서 유형(사용자 매뉴얼, 통합·API 가이드, 사양서·데이터시트, 안전 매뉴얼, 오류 코드표, 릴리스 노트, 치수도·도면)은 무엇이며 각각 어떤 기능 정보를 담는가?
3. q2-02 기능 정보는 어떤 형태(문장, 표, 그림·다이어그램, 코드 예제, 파라미터 표)로 존재하며 형태별 추출 난이도는 어떠한가?
4. q2-03 공개적으로 접근할 수 있는 대표 문서 샘플(AMR, 협동로봇, 로봇팔 등)은 무엇이고 이용 조건은 어떠한가?
5. 사용 정보(설명서)의 구성과 내용을 정하는 표준(ISO 20607, IEC/IEEE 82079-1)은 제조사 문서 유형을 어떻게 규정하는가? (단계 2 페이지 3절 q2-01 겨냥)
6. 국내 협동로봇 제조사(두산로보틱스·레인보우로보틱스)는 어떤 문서를 어떤 경로·조건으로 공개하는가? (한국 자료 우선 규칙, q2-03 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO 20607:2019 는 기계 제조사가 설명서(instruction handbook)의 안전 관련 부분을 작성할 때의 요구사항을 정하며, 기계 수명주기 전 단계를 고려한 안전 관련 내용·구조·표현을 다루고 ISO 12100:2010 6.4.5 의 사용 정보 일반 요구를 구체화한다. | ref-723 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f2 | [사실] | IEC/IEEE 82079-1:2019 는 조립·설치·운전·유지보수·폐기에 필요한 모든 유형의 사용 정보(instructions for use)의 설계·작성 원칙과 요구사항을 정하고, 정보 품질·정보 관리 과정과 사용 정보의 실증적 평가 방법을 규범 부분에 둔다. | ref-724 | 아니오 | medium | 2019 | — | 원문 미열람 |
| f3 | [추정] | Boston Dynamics Spot SDK 공식 저장소 README 는 문서를 개념 설명, 파이썬 클라이언트 라이브러리(예제·빠른 시작), 페이로드 개발자 문서(기계·전기·소프트웨어 인터페이스), API 프로토콜 참조, 릴리스 노트, 라이선스로 나눈다. | ref-719 | 아니오 | medium | 2026-09-25 | — | 벤더 주장 |
| f4 | [추정] | Kinova Kortex API 공식 저장소 README 는 C++·Python API 메커니즘과 예제, Modbus 인터페이스, 언어별 오류 처리 문서, 펌웨어·API 판별 다운로드(Gen3 2.8.0, Gen3 lite 2.3.4)를 안내한다. | ref-720 | 아니오 | medium | 2026-09-25 | — | 벤더 주장 |
| f5 | [추정] | 두산로보틱스는 로봇랩 포털에서 설치 매뉴얼(설치 방법·인터페이스·수동/자동 모드·안전 관련 기능)과 기타 매뉴얼(액세서리·퀵 가이드·ROS·API 사용 방법)을 제공한다. | ref-725 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f6 | [추정] | 두산로보틱스 doosan-robot2 공식 저장소 README 는 튜토리얼 등 자세한 내용을 공식 ROS2 매뉴얼 포털로 안내하며 ROS2 Humble 에서 전 기종 지원을 밝히고 Apache 2.0·BSD 3-Clause 로 배포한다. | ref-721 | 아니오 | medium | 2026-09-25 | — | 벤더 주장 |
| f7 | [추정] | 레인보우로보틱스는 다운로드 페이지(도면·카탈로그·기술자료)와 GitHub Pages 기술자료(rb_cobot_docs)를 두고, 공식 클라이언트 라이브러리 rbpodo 는 제어 박스와 5000번 포트로 명령·응답을, 5001번 포트로 상태 데이터를 주고받는다고 적는다. | ref-722, ref-726 | 아니오 | medium | 2026-09-25 | — | 벤더 주장 |
| f8 | [사실] | VDA 5050 팩트시트 JSON 스키마는 유형 명세·물리 파라미터·프로토콜 한계·지원 기능·기하·적재 명세 블록을 기계가독 형식으로 두어, 이동로봇 쪽 사양서·데이터시트 정보의 표준화된 대응물이 된다. | ref-228 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f9 | [추정] | 확인한 사례를 문서 유형에 대응시키면 통합·API 가이드는 기능·인터페이스(명령·상태)·오류 처리를, 설치·안전 매뉴얼은 운전 모드·안전 제약을, 릴리스 노트는 판별 변경을, 페이로드·액세서리 문서는 장착 장비 인터페이스를, 사양서·데이터시트는 파라미터 범위를 주로 담는 것으로 보인다. | ref-719, ref-720, ref-725, ref-723, ref-228 | 아니오 | low | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF PerformAction 튜토리얼은 플릿이 수행할 수 있는 동작을 config.yaml 의 actions 목록으로 선언하고, 작업 요청을 JSON 으로, 동작 실행 논리를 파이썬 코드 예제로 보여 주어 기능 정보가 설정 파일·JSON·코드 예제 형태로 존재하는 사례가 된다. | ref-040 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [추정] | Kinova Kortex 는 Google Protocol Buffers 문서를 참조하고 Spot SDK 는 API 프로토콜 참조를 두어, 두 제조사 모두 API 를 기계가독 프로토콜 정의와 코드 예제 형태로 제공하는 것으로 보인다. | ref-719, ref-720 | 아니오 | low | 2026-09-25 | — | 벤더 주장 |
| f12 | [사실] | OmniDocBench 공식 저장소 README 는 PDF 문서 파싱을 텍스트 문단·표·수식·읽기 순서로 나눠 편집 거리·TEDS 등으로 평가하며, 문서 유형으로 논문·재무 보고서·신문·교과서·손글씨 노트 등을 들고 매뉴얼은 명시하지 않는다. | ref-727 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [추정] | 범용 문서 파싱 벤치마크가 요소 형태별로 따로 평가하고 매뉴얼을 문서 유형에 두지 않으므로, 로봇 매뉴얼의 형태별(문장·표·그림·코드) 추출 난이도는 공개 측정 자료로 확인되지 않은 것으로 보인다. | ref-727, ref-728 | 아니오 | low | 2026-09-25 | — | — |
| f14 | [사실] | Springer 게재 장 'Conversational Knowledge Extraction from Technical Manuals'는 매뉴얼 전처리·색인, 온톨로지 제약을 건 검색 증강 생성(RAG) 기반 개체·관계 추출, 대화형 절차 안내를 결합한 LLM 프레임워크를 제안했다. | ref-728 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f15 | [사실] | ManuExtract 는 제조 분야 문서에서 항목–속성–값 삼중항을 추출하는 벤치마크 데이터셋으로, LLM 생성 주석을 도메인 전문가가 다듬어 구축했다. | ref-729 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f16 | [추정] | 확인한 사례로 보면 기능 정보의 형태는 기계가독 스키마·설정(VDA 5050 팩트시트, Open-RMF config.yaml, 프로토콜 정의) → 파라미터 표 → 문장 → 그림·다이어그램 순으로 구조화 추출이 쉬워질 것으로 보이나, 로봇 문서에서 이를 측정한 자료는 찾지 못했다. | ref-228, ref-040, ref-727, ref-728 | 아니오 | low | 2026-09-25 | — | — |
| f17 | [추정] | Spot SDK 는 GitHub 에 공개되어 있으나 사용·복제·배포가 Boston Dynamics SDK 라이선스(20191101-BDSDK-SL) 조건을 따른다. | ref-719 | 아니오 | medium | 2026-09-25 | — | 벤더 주장 |
| f18 | [추정] | Kinova Kortex API 저장소는 BSD 3-Clause 라이선스로 공개되어 있다. | ref-720 | 아니오 | medium | 2026-09-25 | — | 벤더 주장 |
| f19 | [추정] | 국내 협동로봇 제조사의 공개 저장소(두산 doosan-robot2: Apache 2.0·BSD 3-Clause, 레인보우 rbpodo: Apache 2.0)는 코드에 개방 라이선스를 달지만, 포털에서 내려받는 매뉴얼 문서 자체의 이용 조건은 이번에 확인하지 못했다. | ref-721, ref-722, ref-725 | 아니오 | low | 2026-09-25 | — | 벤더 주장 |
| f20 | [추정] | 이번에 확인한 공개 문서 샘플은 로봇팔·협동로봇(Kinova, 두산로보틱스, 레인보우로보틱스)과 4족 보행 로봇(Spot)이며, AMR 제조사의 공개 매뉴얼 샘플은 찾지 못해 AMR 쪽은 VDA 5050 팩트시트·MassRobotics 스키마 같은 표준 스키마로만 대신되는 것으로 보인다. | ref-719, ref-720, ref-721, ref-722, ref-228, ref-230 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-719 | Boston Dynamics (boston-dynamics/spot-sdk GitHub) | spot-sdk — README | 미확인 | 벤더 문서 | medium | 2026-09-25 | https://github.com/boston-dynamics/spot-sdk | 아니오 |
| ref-720 | Kinova (Kinovarobotics/kortex GitHub) | kortex — readme | 미확인 | 벤더 문서 | medium | 2026-09-25 | https://github.com/Kinovarobotics/kortex | 아니오 |
| ref-721 | Doosan Robotics (doosan-robotics/doosan-robot2 GitHub) | doosan-robot2 — README (humble) | 미확인 | 벤더 문서 | medium | 2026-09-25 | https://github.com/doosan-robotics/doosan-robot2 | 아니오 |
| ref-722 | Rainbow Robotics (RainbowRobotics/rbpodo GitHub) | rbpodo — README | 미확인 | 벤더 문서 | medium | 2026-09-25 | https://github.com/RainbowRobotics/rbpodo | 아니오 |
| ref-723 | ISO | ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles | 2019 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/68519.html | 예 |
| ref-724 | IEC / IEEE / ISO | IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 2019 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/71620.html | 예 |
| ref-725 | 두산로보틱스 | 매뉴얼 : Doosan Robotics Training & Service | 미확인 | 벤더 문서 | low | 2026-09-25 | https://robotlab.doosanrobotics.com/ko/board/Resources/Manual | 예 |
| ref-726 | Rainbow Robotics | Rainbow Robotics 협동로봇 기술자료 (rb_cobot_docs) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://rainbowrobotics.github.io/rb_cobot_docs/ko/ | 예 |
| ref-727 | OpenDataLab (opendatalab/OmniDocBench GitHub) | OmniDocBench — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/opendatalab/OmniDocBench | 아니오 |
| ref-728 | Springer Nature (게재 장 저자 미확인) | Conversational Knowledge Extraction from Technical Manuals: An LLM-Based Framework with Ontological Guidance | 미확인 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-19096-3_30 | 예 |
| ref-729 | Springer Nature (게재 장 저자 미확인) | Enhancing LLMs for Manufacturing Information Extraction | 미확인 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-981-92-1468-6_21 | 예 |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 예 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-2-document-types.md | 2, 3, 4, 5, 6, 8, 9 | q2-01 답: f1·f2·f3·f4·f5·f6·f7·f8·f9 (신뢰도 low) / q2-02 부분 답: f10·f11·f12·f13·f14·f15·f16 / q2-03 부분 답: f17·f18·f19·f20 — 2절 q2-01 답함, q2-02·q2-03 조사 중, 3절 질문별 소제목 신설(제조사 문서는 벤더 주장 병기), 4절 결론·불확실성(형태별 추출 난이도 측정 자료 없음, AMR 공개 매뉴얼 미확인), 5절 후속 질문, 6절 완료 조건 현황, 8절 출처, 9절 이력 |
| update | docs/tracks/manual-capability-ontology/document-type-matrix.md | 3, 4, 5, 7, 8 | 트랙 산출물 갱신: 통합·API 가이드 행(기능·인터페이스·오류 의미, f3·f4·f11), 안전 매뉴얼 행(안전 제약, f1·f5), 릴리스 노트 행(f3), 사양서·데이터시트 행(파라미터 범위·제약, f8) 일부 칸 채움(모두 샘플 병기, 벤더 주장), 4절 공개 문서 샘플 목록에 Spot SDK·Kinova Kortex·두산 doosan-robot2·레인보우 rbpodo 추가(이용 조건 f17~f19), AMR 샘플 없음(f20) |
| update | docs/categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md | 6 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f9, f16): 능력 정보가 문서 유형·형태별로 흩어져 있고 기계가독 스키마가 가장 구조화된 원천이라는 점 |
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | 6 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f5, f7, f19, f20): 온보딩 때 모을 제조사 문서 유형과 공개 경로·이용 조건, 국내 제조사 사례 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 6, 8 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f12, f13, f14, f15): 교차 규칙(매뉴얼 해석은 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용)에 따라 문서 파싱 벤치마크와 매뉴얼 대상 LLM 추출 연구를 양쪽 연결 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사용 정보 | Information for Use (Instructions for Use) | 제품을 조립·설치·운전·유지보수·폐기하는 사람에게 제조사가 제공하는 설명 정보로, IEC/IEEE 82079-1 이 작성 원칙과 요구사항을 정한다. |

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 5회 · 신규 출처 11건
- 미확인 항목:
    - q2-02 부분 답: 로봇 매뉴얼의 형태별(문장·표·그림·코드) 추출 정확도 측정 자료 없음
    - q2-03 부분 답: AMR 제조사 공개 매뉴얼 샘플 미확인, 포털 매뉴얼 문서의 이용 약관 미확인
    - f5·f7(rb_cobot_docs)·f14·f15 원문 미열람(검색 요약 범위)
    - 오류 코드표·치수도 문서 유형은 샘플에서 따로 확인하지 못함
    - ref-728·ref-729 저자·발행일 미확인
    - 모든 finding 교차 확인 없음
- 범위 경계 위반 의심:
    - f4: Kortex 의 서보 모드 등 저수준 제어 문서는 분류 원문 9장 '로봇 자체 지능·제어' 쪽 연계 대상이므로 문서 유형 사례로만 쓰고 ROP 직접 범위로 서술하지 않음
- 한계: 스키마 불일치 재실행: 직전 반환 JSON 이 이번 프롬프트 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 질문(q2-01·q2-02·q2-03)으로 브리프를 다시 만들었다. 벤더 문서만 근거로 한 finding(f3~f7, f11, f17~f19)은 모두 태그 추정, vendor_claim true, evidence_excerpt 첫머리 '벤더 주장: '으로 냈고, 사실 태그는 표준·오픈소스·논문 출처 finding 에만 두었다. 답한 질문: q2-01. q2-02·q2-03 은 부분 답. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-719·ref-720·ref-721·ref-722·ref-727, inbox 원문 ref-040. MiR 저장소 raw 경로는 404. 검색 5회/40, 신규 출처 11건/20(ref-719~ref-729, 예약 구간 안), 재사용 3건. 한국 자료: 두산로보틱스·레인보우로보틱스 문서 경로 포함. 온톨로지 변경 1건 제안(근거 문서 속성). 후속 질문 3건. 정정 요청 없음. 27. AI·학습·적응과 모델 운영 관련 finding(f13~f15)은 적용 대상 5·21 영역과 함께 반영 제안. 8·22 관련 주장 없음.

## 트랙 블록

- 트랙: manual-capability-ontology · 단계: 2
- 답한 질문 id: q2-01

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | AMR 제조사(MiR·OTTO·국내 물류로봇 업체 등)가 공개하는 매뉴얼·REST API 문서는 무엇이며, 공개되지 않을 때 표준 스키마(VDA 5050 팩트시트·MassRobotics)로 대신할 수 있는 정보와 없는 정보는 무엇인가? (q2-03 에서 파생) | 2 | f20 |
| — | 로봇 매뉴얼의 형태별(문장·파라미터 표·그림·코드 예제) 추출 정확도를 범용 문서 파싱 벤치마크와 비교해 측정할 수 있는 공개 데이터셋이나 평가 방법이 있는가? (q2-02 에서 파생) | 3 | f13 |
| — | SDK 코드 라이선스와 별개로 제조사 매뉴얼 문서를 자동 추출·재가공해 능력 온톨로지에 쓰는 것이 이용 조건상 허용되는가, 이를 누가 확인하고 기록하는가? (q2-03 에서 파생) | 6 | f19 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 근거 문서 (Evidence Document) | f3, f9, f16, f17 | 속성 '문서 유형(사용자 매뉴얼·통합·API 가이드·사양서·안전 매뉴얼·릴리스 노트 등)', '정보 형태(문장·표·그림·코드·기계가독 스키마)', '이용 조건(라이선스)'을 더하는 제안. 초안 6절 '근거 문서의 단위와 버전' 질문과 함께 검토 필요. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 문서 유형 매트릭스: 일부 칸만 채울 근거가 있고 오류 코드표·치수도 행 미조사
    - 공개 문서 샘플 목록: AMR 샘플 없음, 매뉴얼 이용 조건 미확인
    - q2-02·q2-03 부분 답, q2-04·q2-05·q2-06 열림
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
