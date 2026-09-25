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
        "ref-406"
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
        "ref-186"
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
        "ref-470"
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
        "ref-406"
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
        "ref-406"
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
        "ref-406"
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
        "ref-470",
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
      "id": "ref-186",
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
      "id": "ref-470",
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
      "id": "ref-406",
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
    "limits": "web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: ref-629·ref-630(NIST ARIAC 2025 challenges·scoring, 미러 목록 경로), ref-633(ros2_fault_injection), ref-634(ROSMonitoring), ref-406(재사용, Open-RMF 시뮬레이션 장). 나머지 11건은 검색 요약 기준(신뢰도 상한 medium). IntelLabs scenario_execution README raw 경로는 main·jazzy 모두 404 라 출처로 넣지 않았다. League of Robot Runners Start-Kit README 는 열었으나 평가 지표가 없어 쓰지 않았다. 검색 22회/30, 신규 출처 15건/15(ref-629~ref-643, 예약 구간 안)로 신규 출처 예산에 도달해 Scenario Execution for Robotics(arXiv 2409.07080), Timed Rebeca 기반 ROS 2 다중 로봇 모델 검사(arXiv 2511.15227), KTL 로봇시험인증센터, arculus VDA 5050 적합성 시험 도구는 출처로 넣지 않았다. 재사용 1건: ref-406(2026-09-25-56 브리프 값 사용). 참고문헌 목록 전체 값이 입력에 없어 ref-007(NIST 협업 로봇 성능)·ref-008(NIST ARIAC)의 기존 값을 재사용하지 못하고 ARIAC 는 개별 페이지 URL 로 새 id 를 붙였다(퍼블리셔 대조 필요). 열린 질문: oq-055 는 f18·f19, oq-058 은 f13 이 부분 근거일 뿐 해결로 보지 않았고, oq-063·oq-077 은 이번에 조사하지 못했다. 한국 자료: KS B ISO 18646(ref-640), 한국로봇산업진흥원(ref-641). 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 섞지 않았고, 22. 시뮬레이션·예측용 디지털 트윈과의 목적 구분은 f20(의견)으로만 냈다. 정정 요청 없음."
  }
}
```

### runs/2026-09-25-59/verification.json

```json
{
  "run_id": "2026-09-25-59",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw.githubusercontent.com 의 challenges.rst 원문을 열어 Conveyor·Voltage Tester·Vacuum Tool Malfunction, High Priority Order 네 과제를 확인했다. 원문 페이지 자체에는 연도 표기가 없다. ARIAC 2025 기준이라는 근거는 미러 목록의 설명(현재 문서 = ARIAC 2025)이므로 기준일은 '문서 main 브랜치, 2026-09-25 확인'으로 적는다. 단일 출처다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: scoring.rst 원문을 열었다. 기본 점수 식, 가점(시간·검사 속도·고우선 주문·센서 비용·분류), 감점(정상 셀 낙하, 허용되지 않은 표면 위 물체, AGV·로봇 충돌, 센서 예산 초과), 시행당 5회 가운데 상위 2회 평균, 실행 80%·심사 20% 조합이 모두 원문과 맞는다. 단일 출처다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: ref-629·ref-630 원문 내용에서 이끌어 낸 추론이며 물류 현장 적용은 검증되지 않았다고 스스로 밝혔다. low 신뢰도가 적절하다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색 예산(30회 중 남은 8회)을 다른 출처에 써서 재검색하지 못했다. 서지(ACM Computing Surveys 52(5), 2019, arXiv 1807.00048)는 널리 알려진 논문과 맞는다. 다만 '시험·시뮬레이션만으로 불충분'이라는 요지는 리서치 검색 요약 기준이며 검증자가 원문으로 확인하지 못했다. 영어 직접 인용은 쓰지 않고 재서술한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(Springer, ACM DL, Zenodo 아티팩트)에서 저자 셋, FM 2026 LNCS 16556, 창고 AGV 산업 사례 연구, 전이 시스템 인코딩 세 가지, BDD 기호 분석을 확인했다. '합성·실제 레이아웃 평가'는 검증자가 본 검색 결과에 나타나지 않아 리서치 검색 요약에만 기댄다. 같은 논문의 색인들이므로 교차 확인으로 보지 않는다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색 예산 부족으로 재검색하지 못했다. 서지(IEEE ICST 2020, pp.96–107)는 알려진 논문과 맞는다. 12가지 실무, 9가지 어려움, 3개 주제, '첫 연구'라는 서술은 리서치 검색 요약 기준이다. '첫 연구'는 논문 저자들의 자기 규정이라고 밝혀 쓴다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 원문을 열었다. *_raw 프록시 구조, 편향·잡음·지연·누락, 명령 정지·재생, 서비스 강제 실패, TF 손상, YAML 단정, 헤드리스 실행기 종료 코드(0/1), 캠페인 실행기가 원문과 맞는다. 개인 프로젝트 README 의 기능 설명이므로 'README 기준'으로 한정해 서술한다. 성숙도와 라이선스는 미확인이다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 지원 메시지 유형(Odometry, LaserScan, JointState, Imu, TFMessage, Twist, PointCloud2, Trigger)이 원문과 맞는다. '연계 대상' 표기가 적절하다. Twist 는 속도 명령이므로 '센서 신호' 목록에 넣지 않도록 서술에 유의한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 원문을 열었다. 감시 노드 생성, 판정기 블록이 있으면 WebSocket 판정기 사용(온라인), 없으면 기록만(오프라인), 기록 또는 걸러 내기, 형식 비종속, ROS1·ROS2 토픽·서비스 지원이 원문과 맞는다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: simulation.md 원문을 열었다. 같은 코드를 실제 시스템에서 수정 없이 실행, 반복 가능한 시나리오로 버그 수정 확인, 드물지만 심각한 예외 상황, 장시간 시뮬레이션이 배치 전 신뢰를 높인다는 네 문장을 모두 확인했다. 직접 인용은 이 출처에서 1회만 쓴다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색 예산 부족으로 재검색하지 못했다. 서지(SoCS 2019, arXiv 1906.08291)는 알려진 논문과 맞는다. 내용은 리서치 검색 요약(초록) 기준이다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(idm-lab.org 초록과 PDF, ICAPS 2024 시연 목록, UCI ICS, pathfinding.ai)에서 대회 목표(MAPF 핵심 과제 식별, 벤치마크 인스턴스 개발, 알고리즘 성능 평가, 최신 성과 추적)와 격자 환경, 계획·스케줄링 트랙을 확인했다. 'Amazon Robotics 후원'은 리서치 검색 요약 기준이다. 주최 측 자료이므로 독립 교차 확인은 아니다. ref-636 저자는 미확인이다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(arXiv html·pdf 목록)에서 LSMART, FMS 안의 MAPF 평가용 오픈소스 시뮬레이터, pebble motion·완전 실행·통신 가정 비판, 호출 정책·실패 정책 모듈을 확인했다. 저자(Jingtian Yan 외 7인)와 제출일 2026-02-17 을 확인했으므로 ref-637 서지를 고친다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(ISO 소개 페이지, ANSI 블로그)에서 범위(무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단, 예로 AGV·AMR)를 확인했다. '사람 감지 시험·안정성 시험·Annex E 검증 절차' 세부는 검증자 검색으로 확인하지 못했다. 브리프도 미확인으로 적었으므로 본문에서 뺀다(수정 지시). 유료 표준이다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과(NIST 과제 페이지와 행사 페이지, ASTM 보도자료)에서 F45 분과 F45.01 환경 영향, F45.02 도킹·주행, F45.03 물체 감지·보호, F45.04 통신·통합, F45.91 용어와 NIST 참여(위원장 NIST 소속)를 확인했다. F3244 등 개별 시험 방법은 미확인이다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. KSSN 검색 결과에서 제1부(바퀴형 로봇의 이동능력, 2022 확인)와 제3부(조작, K001010144227)가 있음을 확인했다. '제2부 주행'은 검증자 검색에 나타나지 않아 미확인이다. 기준일은 '2022 확인'이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에서 KIRIA 시험평가 페이지가 로봇 주행 성능에 대해 경사노면·특수노면·계단·주행내구 시험을 제공한다고 확인했다. 'KS·ISO·IEC·CISPR' 적용 목록은 리서치 검색 요약 기준이다. 관련 기사(2022 삼성전자 서비스 로봇 ISO 기반 시험평가)는 다른 사실을 다루므로 교차 확인으로 세지 않는다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 벤더 주장이며 추정 유지. 검색 결과에서 OTTO 보도자료와 재게시(automate.org, NAiSE, control.com)를 확인했다. 대상 기종은 OTTO 100·600·1200·1500, 파트너는 Idealworks·NAiSE·SYNAOS, 발표 시기는 2026년 4월이다. 재게시와 파트너 사이트는 독립 출처가 아니다. 인증의 시험 항목은 미확인이다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 공식 적합성 절차를 '찾지 못함'은 부재가 확인된 것이 아니라고 브리프가 밝혔다. oq-055 는 부분 근거일 뿐 해결이 아니다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지: 분류 원문 정의(22. 시뮬레이션·예측용 디지털 트윈은 효과 예측, 23. 시험·형식 검증·벤치마크는 시험·검증)에 맞는 목적 구분이다. 누구의 의견인지('구축자 의견')를 밝혀야 한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: ref-629·ref-633·ref-406 원문 확인 내용을 합친 추론이다. 물류 현장 적용 사례를 찾지 못했다는 한계를 본문에 함께 적는다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 가상 구성안(피킹, 완료·인계)이다. 수치 없이, 가상임을 본문에 밝혀야 한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 원문을 연 ref-633·ref-634·ref-406 과 원문 미열람 ref-643 을 섞은 추론이다. 브리프의 source_unopened: false 표기와 달리 ref-643 에 기댄 부분은 원문 미열람이다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지, 연계 대상 표기 적절. 근거 네 출처 모두 원문 미열람(검색 결과 기준)이다."
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
      "ref-629·ref-630(ARIAC 문서의 challenges·scoring 개별 페이지)은 기존 ref-008(NIST ARIAC Documentation, 분류 원문 12장 8번)과 같은 문서 묶음의 하위 페이지다. 새 id 는 유지하되, ARIAC 일반 소개 문장에는 ref-008 을 재사용한다.",
      "ref-406(Open-RMF simulation 장)은 2026-09-25-56 에서 재사용한 출처다. 새 id 를 만들지 않는다."
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
    "참고 자료 절과 reference_updates: 원문을 열지 못한 ref-631·ref-632·ref-186·ref-636·ref-637·ref-470·ref-639·ref-640·ref-641·ref-642·ref-643 의 각주 정의에서 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 항목에 source_unopened: true 를 넣는다 — 이 출처들은 검색 결과로만 실재를 확인했다. 원문을 연 ref-629·ref-630·ref-633·ref-634·ref-406 에는 붙이지 않는다.",
    "ref-637: 기관 칸을 'Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.'로, 발행일을 2026-02-17 로 고친다 — 검증 검색 결과(arXiv 2602.15721)로 저자와 제출일을 확인했다.",
    "ref-642: 발행일을 2026-04 로 적는다 — 검색 결과상 OTTO 발표가 2026년 4월이다. f18 은 [추정]과 '벤더 주장' 병기를 유지한다. 본문에는 대상 기종(OTTO 100·600·1200·1500)과 파트너 세 곳만 쓰고, 인증 시험 항목은 '미확인'으로 둔다.",
    "f14(7·9절): 'ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정한다'까지만 [사실]로 쓴다. '사람 감지 시험·안정성 시험·부속서의 검증 절차' 부분은 빼거나 '세부 미확인'으로 표기한다 — 검증자와 리서치 모두 이 세부를 확인하지 못했다.",
    "f15(7절): 분과 구성과 NIST 참여만 쓰고 F3244 등 개별 ASTM 시험 방법은 본문에 쓰지 않는다 — 개별 시험 방법 내용이 미확인이다.",
    "f16(7절): 기준일을 'KS B ISO 18646-1, 2022 확인'으로 적는다. 다른 부는 '제3부 조작 등'으로만 쓰고 '제2부 주행'은 미확인으로 둔다 — 검증 검색에서 제1부·제3부만 확인됐다.",
    "f1·f2(6·7·8절): 기준일을 'ARIAC 문서 main 브랜치, 2026-09-25 확인(ARIAC 2025 기준)'으로 적는다. ARIAC 자체를 소개하는 문장에는 기존 각주 [^ref-008]을 재사용한다 — challenges·scoring 원문 페이지에는 연도 표기가 없고, ARIAC 는 분류 원문 12장 8번 참고문헌으로 이미 등록돼 있다.",
    "f4(3·8절): 원문 영어 구절 'testing and simulation alone are insufficient'를 직접 인용하지 않고 한국어로 재서술한다 — 원문을 열지 못해 인용 문구를 대조할 수 없다.",
    "f6(3·8절): '첫 연구'는 '저자들이 로봇 시스템 시험에 초점을 둔 첫 연구로 소개했다'처럼 저자의 자기 규정으로 쓴다 — 순위 표현이 단일 출처에만 기댄다.",
    "f7(6·7절): 기능 서술을 'README 기준'으로 한정한다. 개인 주도 프로젝트여서 성숙도·라이선스가 미확인이라는 점을 한 번 밝힌다.",
    "f8(9절): 센서 신호 장애 예시에서 Twist(속도 명령)를 센서로 분류하지 않는다 — 원문은 Twist 를 명령 조작 대상으로 둔다.",
    "f20(10절): [의견] 문장에 '구축자 의견'임을 밝힌다 — 의견 주체를 표시해야 한다.",
    "f22(5절): '가상 시나리오'임을 문장 안에 밝히고 수치를 넣지 않는다. 흐름 단계 '피킹', 항목 '완료·인계'를 명시한다 — 실제 사례로 읽히지 않게 한다.",
    "f19·f21·f23·f24(9·11절): [추정] 태그를 유지하고 '~해야 한다'는 단정 대신 '~로 보인다' 수준으로 쓴다. f23 의 교착 검증 부분 각주(ref-643)는 원문 미열람 표기를 따른다.",
    "11절 열린 질문: oq-055(f18·f19)와 oq-058(f13)은 부분 근거만 적고 [열림]을 유지한다. oq-063·oq-077 은 이번 실행에서 조사하지 않았으므로 상태를 바꾸지 않는다. open_questions_new 3건은 형식대로 등록한다.",
    "용어집: 새 용어 후보(장애 주입, 회귀 시험, 런타임 검증, 모델 검사)는 등록할 수 있다. 본문에서는 기존 용어집 표기인 '교착 (Deadlock)', '적합성 시험 (Conformance Test)', '다중 에이전트 경로 찾기 (MAPF)', '플릿 관리 시스템 (FMS)', '산업 자동화용 민첩 로봇 경진대회 (ARIAC)'를 그대로 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(fetch_mode mirror_only)에서 검증됐다. 확인 24건, 미확인 0건, 교차 확인 0건. 강등: 없음(태그는 모두 유지하되 f14·f15·f16 은 확인되지 않은 세부를 빼도록 지시했다). 원문 미열람 출처: ref-631, ref-632, ref-186, ref-636, ref-637, ref-470, ref-639, ref-640, ref-641, ref-642, ref-643. 원문을 연 출처는 GitHub 미러를 통한 ref-629, ref-630, ref-633, ref-634, ref-406 이다. 주의: 모든 주장이 단일 출처에 기댄다. ref-631·ref-632·ref-186 는 검증 검색 예산(리서치 22회 사용, 남은 8회)을 다른 출처에 써서 검증자가 다시 검색하지 못했고, 서지만 대조했다. 9절의 ROP 직접 범위와 연계 범위 구분, 분류 원문 질문에 대한 답(f21)은 추정이다. 물류 오케스트레이션 소프트웨어의 회귀 시험·장애 주입 현장 사례와 VDA 5050 공식 적합성 절차는 확인되지 않았다. oq-055·oq-058 은 부분 근거만 있고, oq-063·oq-077 은 이번에 다루지 않았다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-25-59/pages.json

```json
{
  "run_id": "2026-09-25-59",
  "outline": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 700,
      "summary": "로봇 시스템 시험은 실무에서도 어려운 문제로 보고되며[사실][^ref-632], 자율 로봇은 시험·시뮬레이션만으로 정확성을 보장하기 어렵다는 지적이 있다[사실][^ref-631].",
      "planned_findings": [
        "f6",
        "f4",
        "f13",
        "f10"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 750,
      "summary": "이 영역의 핵심 개념은 장애 주입·회귀 시험·형식 검증과 교착·런타임 검증·벤치마크·적합성 시험이다[사실][^ref-629][^ref-633].",
      "planned_findings": [
        "f1",
        "f7",
        "f5",
        "f9",
        "f11",
        "f19"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 800,
      "summary": "피킹 단계에서 플릿 어댑터를 바꾼 뒤 장애를 주입해 재배정과 재고 확정 시점을 단정으로 확인하는 가상의 회귀 시험이다[추정][^ref-629][^ref-633].",
      "planned_findings": [
        "f22",
        "f21",
        "f3",
        "f23"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1100,
      "summary": "대표 접근법은 장애 주입형 시험·채점, 시뮬레이션 회귀 시험, 형식 검증, 런타임 검증, 현실 조건을 넣은 벤치마크다[사실][^ref-629][^ref-634].",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f7",
        "f10",
        "f4",
        "f5",
        "f9",
        "f13",
        "f12"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "평가 프로그램, 차량·로봇 단위 표준과 국내 시험기관, 오픈소스 시험 도구를 정리한다[사실][^ref-008][^ref-470].",
      "planned_findings": [
        "f1",
        "f2",
        "f12",
        "f14",
        "f15",
        "f16",
        "f17",
        "f7",
        "f9",
        "f10",
        "f13"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "형식 검증 조사, 로봇 시험 실무 연구, MAPF 벤치마크 정의, 대회·현실적 시험대, 창고 AGV 교착 사례 연구 여섯 건이다[사실][^ref-631][^ref-643].",
      "planned_findings": [
        "f4",
        "f6",
        "f11",
        "f12",
        "f13",
        "f5"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 1000,
      "summary": "ROP 몫은 오케스트레이션 논리의 교착 검증·인터페이스 적합성·장애 회귀 시험·런타임 감시로 보이고[추정][^ref-633], 로봇 자체 안전·주행 성능 시험은 연계 대상으로 보인다[추정][^ref-470].",
      "planned_findings": [
        "f23",
        "f24",
        "f14",
        "f8",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "22. 시뮬레이션·예측용 디지털 트윈과 시뮬레이션 환경을 공유하고 여러 영역에서 시험 대상을 받는다는 것이 구축자 의견이다[의견][^ref-406].",
      "planned_findings": [
        "f20",
        "f5",
        "f11",
        "f13",
        "f9",
        "f21",
        "f14",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "oq-055·oq-058 은 부분 근거만 있어 열림을 유지하고, oq-063·oq-077 은 이번에 다루지 않았으며, 새 질문 3건을 올린다.",
      "planned_findings": [
        "f18",
        "f19",
        "f13",
        "f21",
        "f5",
        "f17"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(4·6·7·10·11절은 주제 페이지로 분리), 2차 수정: 9절 f8 태그 분리, 3절 첫 문장 범위 정정, 10절 요약 의견 주체 표시, 3·9절 약어 풀이"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area23-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 시험·형식 검증·벤치마크 의 \"6. 대표 접근법과 기술\" 절을 옮겼다(2차 수정 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area23-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 시험·형식 검증·벤치마크 의 \"7. 관련 표준·프레임워크·오픈소스\" 절을 옮겼다(2차 수정 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area23-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 시험·형식 검증·벤치마크 의 \"4. 핵심 개념과 용어\" 절을 옮겼다. 2차 수정: 적합성 시험 항목에 '벤더 주장' 병기"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area23-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 시험·형식 검증·벤치마크 의 \"11. 열린 질문\" 절을 옮겼다(2차 수정 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area23-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 23. 시험·형식 검증·벤치마크 의 \"10. 다른 연구영역과의 연결\" 절을 옮겼다. 2차 수정: 1절·3절 요약 문장에 '구축자 의견' 표시"
    }
  ],
  "changelog_entry": "2026-09-25 | 23. 시험·형식 검증·벤치마크 | 영역 심화: 3~11절 신규 작성(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크), 1차 조건부 승인 수정 16건·2차 수정 5건 반영 | run 2026-09-25-59",
  "index_updates": {
    "home_recent": "2026-09-25 — 23. 시험·형식 검증·벤치마크: 영역 심화로 3~11절 첫 작성(장애 주입·회귀 시험·형식 검증·런타임 검증·벤치마크, 피킹 단계 회귀 시험 가상 시나리오)",
    "category_recent": "2026-09-25 — 23. 시험·형식 검증·벤치마크: 영역 심화로 3~11절 첫 작성, ROP 시험 몫과 로봇 안전·성능 시험(연계 대상) 경계 정리",
    "area_recent": "2026-09-25 — 23. 시험·형식 검증·벤치마크: 3~11절 신규 작성, 열린 질문 3건 추가, oq-055·oq-058 부분 근거 기록"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "fault-injection",
      "term_ko": "장애 주입",
      "term_en": "Fault Injection",
      "definition": "시험 중 센서 신호·메시지·서비스·장비에 지연, 누락, 고장 같은 장애를 계획적으로 넣어 시스템이 장애를 감지하고 복구하는지 확인하는 시험 기법이다.",
      "description": "NIST ARIAC 는 경진 중 컨베이어 정지·공구 파지 실패 등을 주입하고, ros2_fault_injection 은 ROS 2 토픽·서비스에 장애를 넣는다(README 기준).",
      "related_areas": [
        23,
        12,
        20
      ],
      "sources": [
        "ref-629",
        "ref-633"
      ]
    },
    {
      "action": "new",
      "slug": "regression-testing",
      "term_ko": "회귀 시험",
      "term_en": "Regression Testing",
      "definition": "소프트웨어나 설정을 바꾼 뒤 기존에 통과하던 정상·장애 시나리오를 다시 실행해 변경이 기존 동작을 깨뜨리지 않았는지 확인하는 시험이다.",
      "related_areas": [
        23,
        24
      ],
      "sources": [
        "ref-633",
        "ref-406"
      ]
    },
    {
      "action": "new",
      "slug": "runtime-verification",
      "term_ko": "런타임 검증",
      "term_en": "Runtime Verification",
      "definition": "실행 중인 시스템의 사건을 감시기로 관찰해 명세한 성질의 위반을 판정하고 기록하거나 차단하는 검증 기법이다.",
      "related_areas": [
        23,
        12,
        19
      ],
      "sources": [
        "ref-634"
      ]
    },
    {
      "action": "new",
      "slug": "model-checking",
      "term_ko": "모델 검사",
      "term_en": "Model Checking",
      "definition": "시스템을 상태 전이 모델로 표현하고 교착 부재 같은 성질이 도달 가능한 모든 상태에서 성립하는지 자동으로 확인하는 형식 검증 기법이다.",
      "related_areas": [
        23,
        15
      ],
      "sources": [
        "ref-631",
        "ref-643"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-008",
      "org": "NIST",
      "title": "ARIAC Documentation",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-24",
      "summary": "원문 미열람. 분류 원문 12장 8번 참고문헌. ARIAC 소개 문장의 각주로 재사용했다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
        "docs/topics/2026/2026-09-25-area23-s6.md",
        "docs/topics/2026/2026-09-25-area23-s7.md"
      ]
    },
    {
      "id": "ref-629",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "ARIAC 2025 의 민첩성 도전 과제(컨베이어·전압 시험기·진공 공구 고장, 고우선 주문)를 설명한다. 공식 저장소 원본을 열어 읽었다. 원문에 연도 표기가 없어 기준일은 main 브랜치 2026-09-25 확인이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    },
    {
      "id": "ref-630",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Scoring",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "ARIAC 2025 채점 방식(완료 기반 기본 점수, 가점·감점, 상위 2회 평균, 실행 80%·심사 20%)을 설명한다. 공식 저장소 원본을 열어 읽었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "summary": "ROS 2 토픽·서비스·TF 에 장애를 주입하고 YAML 시나리오 단정으로 합격·불합격을 내는 C++ 틀. 개인 주도 프로젝트라 성숙도·라이선스는 미확인. README 원문을 열어 읽었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    },
    {
      "id": "ref-186",
      "org": "Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외",
      "title": "Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks",
      "published": "2019",
      "url": "https://arxiv.org/abs/1906.08291",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MAPF 가정·목적의 공통 용어와 격자 기반 벤치마크를 제시한 논문(SoCS 2019).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    },
    {
      "id": "ref-637",
      "org": "Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.",
      "title": "Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems",
      "published": "2026-02-17",
      "url": "https://arxiv.org/abs/2602.15721",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AGV 플릿 관리 시스템 안에서 MAPF 알고리즘을 현실적으로 평가하는 오픈소스 시뮬레이터 LSMART 와 설계 선택 비교 연구(프리프린트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AGV·AMR 을 포함한 무인 산업용 차량의 안전 요구사항과 검증 수단을 정하는 표준의 ISO 소개 페이지. 같은 URL 의 기존 ref-470 과 퍼블리셔 대조가 필요하다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "summary": "원문 미열람. 서비스 로봇 성능 기준·시험 방법 KS 부합화 표준의 제1부 상세 페이지(2022 확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    },
    {
      "id": "ref-642",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OTTO AMR(OTTO 100·600·1200·1500)이 Idealworks·NAiSE·SYNAOS 와 VDA 5050 인증을 마쳤다는 보도자료(벤더 주장).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 시뮬레이션 장. 같은 코드를 시뮬레이션과 실제에 쓰는 구조, 반복 가능한 시나리오, 예외 상황·장시간 시험을 설명한다. 미러 원문을 열어 읽었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가?",
      "areas": [
        23,
        24
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가?",
      "areas": [
        23,
        15
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가?",
      "areas": [
        23,
        28
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "title": "23. 시험·형식 검증·벤치마크"
    },
    {
      "step": "피킹",
      "item": "작업 대상",
      "link": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "title": "23. 시험·형식 검증·벤치마크"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "title": "23. 시험·형식 검증·벤치마크"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "title": "23. 시험·형식 검증·벤치마크"
    },
    {
      "step": "피킹",
      "item": "완료·인계",
      "link": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "title": "23. 시험·형식 검증·벤치마크"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md",
      "title": "23. 시험·형식 검증·벤치마크"
    }
  ],
  "standards_updates": [
    {
      "name": "League of Robot Runners",
      "kind": "평가 프로그램",
      "org": "League of Robot Runners (Amazon Robotics 후원)",
      "url": "https://idm-lab.org/bib/abstracts/Koen24p.html",
      "related_areas": [
        23,
        15
      ],
      "summary": "창고 물류 같은 응용을 겨냥해 로봇 동역학·지속형 계획·작업 배정·실시간 실행을 다루는 다중 로봇 조율 대회. MAPF 벤치마크 인스턴스 개발과 최신 성과 추적을 목표로 한다.",
      "ref_id": "ref-636"
    },
    {
      "name": "ASTM F45 위원회(무인 자동 유도 산업 차량)",
      "kind": "표준",
      "org": "ASTM International (NIST 참여)",
      "url": "https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles",
      "related_areas": [
        23,
        25
      ],
      "summary": "무인 자동 유도 산업 차량의 용어·권고 관행·시험 방법을 개발하는 위원회로 환경 영향, 도킹·주행, 물체 감지·보호, 통신·통합 분과를 둔다. ROP 에게는 연계 대상이다.",
      "ref_id": "ref-639"
    },
    {
      "name": "KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력",
      "kind": "표준",
      "org": "국가표준인증종합정보센터(KSSN)",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010113281",
      "related_areas": [
        23
      ],
      "summary": "서비스 로봇의 성능 기준과 시험 방법을 KS 로 부합화한 시리즈의 제1부(2022 확인). 제3부 조작 등이 있고 제2부 내용은 미확인이다.",
      "ref_id": "ref-640"
    },
    {
      "name": "한국로봇산업진흥원 로봇 시험평가",
      "kind": "평가 프로그램",
      "org": "한국로봇산업진흥원(KIRIA)",
      "url": "https://kiria.org/rp/kiria/tva/inr/page.dn",
      "related_areas": [
        23
      ],
      "summary": "KS·ISO·IEC·CISPR 등 표준 시험 방법을 적용하고 경사 노면·특수 노면·계단·주행 내구 같은 로봇 주행 성능 시험을 수행한다.",
      "ref_id": "ref-641"
    },
    {
      "name": "ros2_fault_injection",
      "kind": "오픈소스",
      "org": "reeceholland (GitHub)",
      "url": "https://github.com/reeceholland/ros2_fault_injection",
      "related_areas": [
        23
      ],
      "summary": "ROS 2 토픽·서비스·좌표 변환에 장애를 주입하고 YAML 시나리오 단정으로 합격·불합격을 내 CI 에 넘기는 틀(README 기준, 성숙도·라이선스 미확인).",
      "ref_id": "ref-633"
    },
    {
      "name": "ROSMonitoring",
      "kind": "오픈소스",
      "org": "University of Liverpool Autonomy and Verification",
      "url": "https://github.com/autonomy-and-verification-uol/ROSMonitoring",
      "related_areas": [
        23,
        12,
        19
      ],
      "summary": "ROS 1·ROS 2 토픽·서비스를 감시해 외부 판정기로 위반을 판정하고 기록하거나 걸러 내는 런타임 검증 틀.",
      "ref_id": "ref-634"
    },
    {
      "name": "LSMART (Lifelong Scalable Multi-Agent Realistic Testbed)",
      "kind": "오픈소스",
      "org": "Yan, J. 외(arXiv 2602.15721)",
      "url": "https://arxiv.org/abs/2602.15721",
      "related_areas": [
        23,
        15
      ],
      "summary": "AGV 플릿 관리 시스템 안에서 임의의 MAPF 알고리즘을 현실적으로 평가하는 오픈소스 시뮬레이터(프리프린트).",
      "ref_id": "ref-637"
    }
  ],
  "additional_research_requests": [
    "7·9절: ISO 3691-4:2023 의 사람 감지·안정성 시험과 부속서 검증 절차 세부 — 검증에서 확인되지 않아 본문에서 뺐다(유료 표준, 공개 해설 자료 필요).",
    "7절: ASTM F45 개별 시험 방법(F3244 등)의 내용 — 개별 시험 방법이 미확인이라 본문에 쓰지 않았다.",
    "7절: KS B ISO 18646 제2부의 존재·내용과 각 부의 KS 제정일·판 — 제2부가 미확인이다.",
    "9·11절(oq-055): VDA 5050 공식 적합성 시험 절차·인증 기관(VDMA 시험 환경 계획 여부)과 arculus 등 제3자 적합성 시험 도구 — 부재 여부가 확인되지 않았다.",
    "5·6절: 물류 오케스트레이션 소프트웨어에 장애 주입·회귀 시험을 적용해 결과를 공개한 현장 사례 — 2절 질문의 답(f21)이 추정에 머문다.",
    "3·8절: f4(Luckcuck 외)·f6(Afzal 외)·f11(Stern 외) 원문 또는 독립 출처 교차 확인 — 검증자가 재검색하지 못하고 서지만 대조했다.",
    "11절: oq-063(도킹 정밀도 시험과 파지 허용 오차 연결)·oq-077(지도 정합 합격 기준) 조사 — 이번 실행에서 다루지 않았다.",
    "6·7절: 예산으로 미룸 — Scenario Execution for Robotics(arXiv 2409.07080), Timed Rebeca 기반 ROS 2 다중 로봇 모델 검사(arXiv 2511.15227), KTL 로봇시험인증센터."
  ],
  "fixes_applied": [
    "원문 미열람 표기 — 13절과 분리 주제 페이지 8절에서 ref-631·632·186·636·637·470·639·640·641·642·643 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-629·630·633·634·406 에는 붙이지 않았다.",
    "ref-637 서지 정정 — 각주와 reference_updates 의 기관을 'Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J.'로, 발행일을 2026-02-17 로 고쳤다.",
    "ref-642 발행일·벤더 주장 — 발행일을 2026-04 로 적고, 9절 f18 문장은 [추정] 벤더 주장을 유지하며 대상 기종(OTTO 100·600·1200·1500)과 파트너 세 곳만 쓰고 인증 시험 항목을 '미확인'으로 두었다.",
    "f14 한정 — 7·9절에서 '안전 요구사항과 검증 수단을 정한다'까지만 [사실]로 쓰고 사람 감지·안정성 시험·부속서 절차는 빼고 '세부 미확인'으로 표기했다.",
    "f15 한정 — 7절 ASTM F45 행에 분과 구성과 NIST 참여만 쓰고 F3244 등 개별 시험 방법은 쓰지 않았다.",
    "f16 기준일 — 7절에 'KS B ISO 18646-1, 2022 확인'을 적고 다른 부는 '제3부 조작 등'으로만 쓰며 제2부 내용은 미확인으로 두었다.",
    "f1·f2 기준일과 ref-008 재사용 — 6·7절에 'ARIAC 문서 main 브랜치, 2026-09-25 확인(ARIAC 2025 기준)'을 적고 ARIAC 소개 문장과 7절 ARIAC 행에 [^ref-008]을 재사용했으며, 원문에 연도가 없으므로 ref-629·630 각주의 발행일을 '미확인'(JSON null)으로 두었다.",
    "f4 인용 금지 — 3·6·8절에서 영어 구절을 직접 인용하지 않고 한국어로 재서술했다.",
    "f6 자기 규정 — 3절에 '저자들은 이 연구를 로봇 시스템 시험에 초점을 둔 첫 연구로 소개했다'로 썼다.",
    "f7 README 한정 — 4·6·7절 기능 서술을 'README 기준'으로 한정하고 6절에 개인 주도 프로젝트로 성숙도·라이선스가 미확인임을 한 번 밝혔다.",
    "f8 Twist 분류 — 9절에서 센서 신호를 오도메트리·레이저 스캔·IMU·점군으로 적고 속도 명령(Twist)은 명령 조작 대상으로 따로 적었다.",
    "f20 의견 주체 — 10절 22. 시뮬레이션·예측용 디지털 트윈 항목의 [의견] 문장에 '구축자 의견'임을 밝혔다.",
    "f22 가상 표기 — 5절 표와 서술 문장 안에 가상 시나리오임을 밝히고 수치를 넣지 않았으며 흐름 단계 '피킹', 항목 '완료·인계'를 명시했다.",
    "f19·f21·f23·f24 표현 — 5·9·11절에서 [추정]을 유지하고 '~로 보인다' 수준으로 썼으며, 9절 표 아래에 교착 검증 근거(ref-643)가 원문 미열람 자료임을 적고 각주에도 원문 미열람을 표기했다.",
    "11절 열린 질문 — oq-055(ref-642)·oq-058(ref-637)은 부분 근거만 적고 열림을 유지했고, oq-063·oq-077 은 상태를 바꾸지 않고 미조사로 적었으며, 새 질문 3건을 open_question_updates 에 new 로 냈다.",
    "용어 표기 — 장애 주입·회귀 시험·런타임 검증·모델 검사를 glossary_updates 로 내고, 본문에 기존 용어집 표기 '교착 (Deadlock)', '적합성 시험 (Conformance Test)', '다중 에이전트 경로 찾기 (MAPF)', '플릿 관리 시스템 (FMS)', '산업 자동화용 민첩 로봇 경진대회 (ARIAC)'를 그대로 쓰고 용어집에 링크했다.",
    "분량 초과 자동 분리: 23. 시험·형식 검증·벤치마크 본문 8,450자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,667자",
    "형식 검증 오류 수정 — docs/topics/2026/2026-09-25-area23-s10.md 3절의 세부영역 링크 9개를 세부영역 페이지 기준 상대 경로에서 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤다. 주장·태그·각주는 바꾸지 않았다.",
    "2차: 9절 f8 문장 분리 — 지원 메시지 유형(오도메트리·레이저 스캔·IMU·점군은 주입 대상, 속도 명령 Twist 는 명령 조작 대상)은 README 기준 [사실][^ref-633]으로 두고, '센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하는 것으로 보인다'는 [추정][^ref-633]으로 되돌렸다.",
    "2차: 3절 첫 문장 범위 정정 — '로봇 시스템을 바꾼 뒤에도 장애 상황을 여전히 처리하는지 확인하는 일은'을 '로봇 시스템 시험은 실무에서도 어려운 문제로 보고되며'로 줄여 f6 범위에 맞췄다.",
    "2차: 의견 주체 표시 — 세부영역 페이지 10절 요약 문장과 docs/topics/2026/2026-09-25-area23-s10.md 1절 세 줄 요약·3절 첫 문장을 '…받는다는 것이 구축자 의견이다. [의견][^ref-406]'으로 고쳤다.",
    "2차: 벤더 주장 병기 — docs/topics/2026/2026-09-25-area23-s4.md 3절 적합성 시험 항목의 태그를 '[추정] 벤더 주장[^ref-642]'로 고쳤다.",
    "2차: 약어 풀이 — 세부영역 페이지 3절에 '[다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)](../../glossary/mapf.md)', '[플릿 관리 시스템(Fleet Management System, FMS)](../../glossary/fleet-management-system.md)'를 쓰고, 9절에서 '무인운반차(Automated Guided Vehicle, AGV)', '자율이동로봇(Autonomous Mobile Robot, AMR)', '관성 측정 장치(Inertial Measurement Unit, IMU)'로 첫 등장을 풀어 썼다."
  ]
}
```

### runs/2026-09-25-59/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-59/pages/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크"
type: area
category: "F. 도입·검증·유지관리"
area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [장애 주입, 회귀 시험, 형식 검증, 런타임 검증, 벤치마크]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-008, ref-629, ref-630, ref-631, ref-632, ref-633, ref-634, ref-186, ref-636, ref-637, ref-470, ref-639, ref-640, ref-641, ref-642, ref-643, ref-406]
last_run: 2026-09-25
version: 2
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

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [분류원문]

## 2. SCM 관점의 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]

## 3. 왜 중요한가

로봇 시스템 시험은 실무에서도 어려운 문제로 보고되며, 로봇 실무자 면담 연구는 시험 실무 12가지와 어려움 9가지를 도출해 실세계 복잡성, 커뮤니티와 표준, 구성요소 통합의 세 주제로 묶었다. [사실][^ref-632] 저자들은 이 연구를 로봇 시스템 시험에 초점을 둔 첫 연구로 소개했다. [사실][^ref-632]

자율 로봇 시스템은 복잡하고 혼성적이며 안전이 중요한 경우가 많아, 시험과 시뮬레이션에만 기대서는 정확성을 보장하거나 인증 근거를 대기에 부족하다는 지적이 있다. [사실][^ref-631] 이 때문에 형식 명세·검증의 과제와 접근법을 정리한 조사 연구가 나왔다. [사실][^ref-631]

물류 현장의 다중 로봇 계획도 같은 문제를 안고 있다. 기존 [다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)](../../glossary/mapf.md) 연구는 단순화한 운동 모델과 완전한 실행·통신을 가정한다는 한계가 지적되어, [플릿 관리 시스템(Fleet Management System, FMS)](../../glossary/fleet-management-system.md) 안에서 알고리즘을 평가하는 시험대가 제안됐다. [사실][^ref-637] Open-RMF 시뮬레이션 문서는 드물지만 심각한 예외 상황과 장시간 운전을 배치 전에 시뮬레이션으로 시험할 수 있다고 설명한다(2026-09-25 확인). [사실][^ref-406]

## 4. 핵심 개념과 용어

이 영역은 장애를 계획적으로 넣어 보는 시험, 변경 뒤 다시 돌리는 시험, 수학적 모델로 성질을 확인하는 검증, 운영 중 감시, 공통 기준으로 비교하는 벤치마크를 함께 다룬다. [사실][^ref-629][^ref-633]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area23-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹

**시나리오:** 플릿 어댑터 업데이트 뒤 피킹 운반 중 로봇 정지 장애를 넣는 회귀 시험

| 항목 | 내용 |
|---|---|
| 시작 조건 | [플릿 어댑터](../../glossary/fleet-adapter.md) 업데이트가 반영되어 회귀 시험을 시작한다(가상 시나리오). |
| 작업 대상 | 피킹한 화물을 실은 운반구와 그 운반 작업(시뮬레이션 안). |
| 수행 자원 | 시뮬레이션 속 로봇, 장애를 넣는 주입 도구, 합격·불합격을 내는 단정. ROP 는 재배정·복구 동작을 시험하는 몫을 맡는 것으로 보인다. [추정][^ref-633][^ref-406] |
| 제약 | 재배정 과정에서 교착·제약 위반이 없어야 한다는 조건을 판정에 넣는 예시다. 교착 검증의 근거 자료는 원문 미열람 사례 연구다. [추정][^ref-643] |
| 완료·인계 | 작업이 다른 로봇에 재배정되는지, 완료 확인 전에는 재고 변경이 확정되지 않는지를 단정으로 확인한다. [추정][^ref-629][^ref-633] |
| 예외·성과 | 장애 시나리오의 합격 여부와 함께 완료·시간·비용 지표를 판정 기준으로 둘 수 있을 것으로 보인다. [추정][^ref-629][^ref-630] |

다음은 설명을 위한 가상의 시나리오이다. 피킹 단계에서 플릿 어댑터를 업데이트한 뒤, 운반 중인 로봇이 멈추는 장애를 주입하고 작업 재배정과 재고 변경 확정 시점(완료·인계)을 단정으로 확인하는 회귀 시험을 구성할 수 있을 것으로 보인다. [추정][^ref-629][^ref-633] 실제 사례가 아니며 현장 수치는 넣지 않는다.

2절의 질문에 대해서는, 반복 가능한 시뮬레이션 시나리오에 장애 주입과 합격 판정 단정을 붙여 지속적 통합에서 변경마다 다시 돌리는 방식이 답이 될 것으로 보인다. [추정][^ref-629][^ref-633][^ref-406] 다만 물류 오케스트레이션 소프트웨어에 이를 적용해 결과를 공개한 현장 사례는 찾지 못했다. [추정][^ref-406]

## 6. 대표 접근법과 기술

대표 접근법은 장애 주입형 시험과 채점, 시뮬레이션 기반 회귀 시험, 형식 검증, 런타임 검증, 현실 조건을 넣은 벤치마크다. [사실][^ref-629][^ref-634]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area23-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 자료는 평가 프로그램, 차량·로봇 단위의 안전·성능 표준과 국내 시험기관, 오픈소스 시험 도구로 나뉜다. [사실][^ref-008][^ref-470][^ref-633]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area23-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 형식 검증 조사, 로봇 시험 실무 연구, MAPF 벤치마크 정의, 대회와 현실적 시험대, 창고 AGV 교착 사례 연구다. [사실][^ref-631][^ref-643]

- Luckcuck 외, 자율 로봇 시스템의 형식 명세와 검증 조사(2019) — 시험·시뮬레이션만으로는 부족하다는 문제의식에서 형식 방법의 과제·형식체계·접근법을 분류했다. [사실][^ref-631]
- Afzal 외, 로봇 시스템 시험의 어려움 연구(ICST 2020) — 면담으로 시험 실무 12가지와 어려움 9가지를 도출했다. [사실][^ref-632]
- Stern 외, MAPF 정의·변형·벤치마크(2019) — 가정과 목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했다. [사실][^ref-186]
- League of Robot Runners 대회 목표·설계 소개(ICAPS 2024 시스템 시연) — 벤치마크 인스턴스 개발과 최신 성과 추적을 목표로 한다. [사실][^ref-636]
- Yan 외, LSMART와 지속형 AGV 플릿 관리 설계 선택 연구(2026) — 단순 운동 모델·완전 실행 가정을 넘어 FMS 안에서 계획 시점·방법·복구를 비교했다. [사실][^ref-637]
- von Berg·Aichernig·Wedenik, 창고 AGV 의 BDD 기반 교착 회피(FM 2026 사례 연구) — 전이 시스템 인코딩 세 가지를 BDD 로 분석했다. [사실][^ref-643]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP 가 직접 맡을 시험 몫은 오케스트레이션 논리와 인터페이스, 장애 대응이고, 로봇 자체의 안전·주행 성능 시험은 제조사와 시험기관 쪽 연계 대상으로 보인다. [추정][^ref-633][^ref-470]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 작업 배정·교통 관리 논리의 교착·제약 위반 검증, 관제 인터페이스 적합성, 장애 주입 시 재배정·복구 동작의 회귀 시험, 운영 중 런타임 감시로 보인다. [추정][^ref-643][^ref-633][^ref-634][^ref-406] | 연계 대상: 사람 감지·안정성 같은 로봇 자체 안전 검증과 주행·도킹·이동 성능 시험은 제조사와 시험기관 영역이고, ROP 는 그 결과를 로봇 등록·배정 조건의 입력으로 받는 쪽으로 보인다. [추정][^ref-470][^ref-639][^ref-640][^ref-641] |

표의 교착 검증 부분 근거인 창고 무인운반차(Automated Guided Vehicle, AGV) 사례 연구는 원문 미열람 자료다. [사실][^ref-643] ISO 3691-4:2023 은 AGV·자율이동로봇(Autonomous Mobile Robot, AMR)을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정하며(세부 시험 항목 미확인), 로봇 쪽 안전 검증의 연계 대상이다. [사실][^ref-470]

연계 대상: ros2_fault_injection 은 README 기준으로 오도메트리·레이저 스캔·관성 측정 장치(Inertial Measurement Unit, IMU)·점군 같은 센서 신호를 장애 주입 대상으로 다루고, 속도 명령(Twist)은 센서가 아니라 명령 조작 대상으로 둔다. [사실][^ref-633] 이런 센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당하는 것으로 보인다. [추정][^ref-633] ROP 쪽 장애 주입은 같은 프록시 방식을 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. [추정][^ref-633]

OTTO by Rockwell Automation 은 자사 AMR(OTTO 100·600·1200·1500)이 Idealworks·NAiSE·SYNAOS 와 VDA 5050 인증을 마쳤다고 2026년 4월 발표했으며, 인증의 시험 항목은 미확인이다. [추정] 벤더 주장[^ref-642] 이번 조사에서 공식 적합성 시험 절차를 찾지 못했으므로(부재가 확인된 것은 아니다), ROP 는 새 로봇 연동마다 자체 인수 시험을 둘 필요가 있는 것으로 보인다. [추정][^ref-642]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

경계의 전체 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시뮬레이션 환경을 22. 시뮬레이션·예측용 디지털 트윈과 공유하고, 시험 대상 논리와 표준을 여러 영역에서 받는다는 것이 구축자 의견이다. [의견][^ref-406]

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area23-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 부분 근거만 얻었거나 새로 제기된 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [23. 시험·형식 검증·벤치마크 — 열린 질문](../../topics/2026/2026-09-25-area23-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24 (원문 미열람)
[^ref-629]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-630]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Scoring, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html, 접근일 2026-09-25
[^ref-631]: Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M., Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019-09, https://arxiv.org/abs/1807.00048, 접근일 2026-09-25 (원문 미열람)
[^ref-632]: Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S., A Study on Challenges of Testing Robotic Systems, 2020, https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc, 접근일 2026-09-25 (원문 미열람)
[^ref-633]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25
[^ref-634]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-636]: IDM Lab (USC) 게재 초록, 저자 미확인, The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration], 2024, https://idm-lab.org/bib/abstracts/Koen24p.html, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: NIST, ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles, 미확인, https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-640]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010113281, 접근일 2026-09-25 (원문 미열람)
[^ref-641]: 한국로봇산업진흥원(KIRIA), 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼, 미확인, https://kiria.org/rp/kiria/tva/inr/page.dn, 접근일 2026-09-25 (원문 미열람)
[^ref-642]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-643]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
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

### runs/2026-09-25-59/pages/topics/2026/2026-09-25-area23-s6.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크 — 대표 접근법과 기술"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-008, ref-629, ref-630, ref-631, ref-633, ref-634, ref-636, ref-637, ref-643, ref-406]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md#6
---

[홈](../../index.md) › [주제](../index.md) › 23. 시험·형식 검증·벤치마크 — 대표 접근법과 기술

# 23. 시험·형식 검증·벤치마크 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 접근법은 장애 주입형 시험과 채점, 시뮬레이션 기반 회귀 시험, 형식 검증, 런타임 검증, 현실 조건을 넣은 벤치마크다. [사실][^ref-629][^ref-634]
- 이 페이지는 [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 접근법은 장애 주입형 시험과 채점, 시뮬레이션 기반 회귀 시험, 형식 검증, 런타임 검증, 현실 조건을 넣은 벤치마크다. [사실][^ref-629][^ref-634]

### 장애 주입형 시험과 채점

[산업 자동화용 민첩 로봇 경진대회 (ARIAC)](../../glossary/ariac.md)는 미국 국립표준기술연구소(National Institute of Standards and Technology, NIST)가 운영하며, 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경이다. [사실][^ref-008] ARIAC 문서(main 브랜치, 2026-09-25 확인, ARIAC 2025 기준)는 경진 중 컨베이어 정지, 전압 시험기 데이터 중단, 진공 공구 파지 실패, 고우선 주문 투입을 도전 과제로 주입해 장애 감지·복구와 긴급 요청 대응을 시험한다. [사실][^ref-629] 채점은 키트·모듈 완료 비율로 기본 점수를 주고 시간 안 완료·고우선 주문 신속 처리·센서 예산 준수에 가점을, 충돌·정상 부품 낙하·잘못된 위치 배치에 감점을 준 뒤, 상위 2회 평균 실행 점수(80%)와 심사위원 평가(20%)를 합친다(같은 기준일). [사실][^ref-630] 장애를 계획적으로 넣고 완료·시간·비용·위반을 한 점수로 묶는 이 틀은 물류 오케스트레이션 회귀 시험에도 옮겨 쓸 수 있을 것으로 보이나, 제조 키팅 과제 기준이며 물류 적용은 검증되지 않았다. [추정][^ref-629][^ref-630]

### 장애 주입 도구와 시뮬레이션 회귀

ros2_fault_injection 은 README 기준(2026-09-25 확인)으로 ROS 2(Robot Operating System 2) 토픽을 가로채 편향·잡음·지연·누락·명령 정지 같은 장애를 넣어 다시 발행하고, 서비스 강제 실패와 좌표 변환 손상도 지원하며, YAML 시나리오의 단정으로 합격·불합격을 내고 헤드리스 실행기가 종료 코드로 CI 에 결과를 넘긴다. [사실][^ref-633] 개인 주도 프로젝트여서 성숙도와 라이선스는 미확인이다. [사실][^ref-633] Open-RMF 는 시뮬레이션에 쓴 코드를 실제 시스템에서 수정 없이 실행하므로, 반복 가능한 시나리오로 버그 수정을 확인할 수 있다고 설명한다. [사실][^ref-406]

### 형식 검증

형식 검증은 시험·시뮬레이션만으로 부족한 정확성 보장을 보완하려는 접근으로 정리돼 있다. [사실][^ref-631] 창고 AGV 사례 연구는 정해진 경로망을 따르는 시스템을 세 방식으로 전이 시스템에 인코딩하고 BDD 로 기호 분석해 합성·실제 레이아웃에서 교착 회피를 수행했다(2026-05 발표). [사실][^ref-643]

### 런타임 검증

ROSMonitoring 은 YAML 설정으로 ROS 토픽·서비스를 관찰하는 감시 노드를 생성하고, 온라인 모드에서는 외부 판정기의 판정을 받아 위반 메시지를 기록하거나 걸러 내며, 오프라인 모드에서는 사건만 기록한다(2026-09-25 확인). [사실][^ref-634] 명세 형식에 얽매이지 않으며 ROS 1·ROS 2 를 모두 지원한다. [사실][^ref-634]

### 현실 조건을 넣은 벤치마크

LSMART 는 AGV [플릿 관리 시스템 (FMS)](../../glossary/fleet-management-system.md) 안에서 임의의 MAPF 알고리즘을 평가하는 오픈소스 시뮬레이터로, 언제 계획할지·어떻게 계획할지·계획 실패 시 어떻게 복구할지를 비교했다(2026-02 기준). [사실][^ref-637] League of Robot Runners 는 로봇 동역학·지속형 계획·작업 배정·실시간 실행을 창고 물류 같은 응용을 겨냥해 다루는 대회다. [사실][^ref-636]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24 (원문 미열람)
[^ref-629]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-630]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Scoring, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html, 접근일 2026-09-25
[^ref-631]: Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M., Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019-09, https://arxiv.org/abs/1807.00048, 접근일 2026-09-25 (원문 미열람)
[^ref-633]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25
[^ref-634]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25
[^ref-636]: IDM Lab (USC) 게재 초록, 저자 미확인, The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration], 2024, https://idm-lab.org/bib/abstracts/Koen24p.html, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-643]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-59 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-59 | 23. 시험·형식 검증·벤치마크 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-25-59/pages/topics/2026/2026-09-25-area23-s7.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-008, ref-629, ref-630, ref-633, ref-634, ref-636, ref-637, ref-470, ref-639, ref-640, ref-641, ref-406]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md#7
---

[홈](../../index.md) › [주제](../index.md) › 23. 시험·형식 검증·벤치마크 — 관련 표준·프레임워크·오픈소스

# 23. 시험·형식 검증·벤치마크 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 자료는 평가 프로그램, 차량·로봇 단위의 안전·성능 표준과 국내 시험기관, 오픈소스 시험 도구로 나뉜다. [사실][^ref-008][^ref-470][^ref-633]
- 이 페이지는 [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 자료는 평가 프로그램, 차량·로봇 단위의 안전·성능 표준과 국내 시험기관, 오픈소스 시험 도구로 나뉜다. [사실][^ref-008][^ref-470][^ref-633] 차량·로봇 단위 표준은 ROP 에게 연계 대상이다(9절).

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| NIST ARIAC | 평가 프로그램 | 장애 주입형 도전 과제와 가점·감점 채점(ARIAC 문서 main 브랜치, 2026-09-25 확인, ARIAC 2025 기준). [사실] | [^ref-008][^ref-629][^ref-630] |
| League of Robot Runners | 평가 프로그램 | Amazon Robotics 가 후원하는 다중 로봇 조율 대회로, MAPF 핵심 과제 식별과 벤치마크 인스턴스 개발·최신 성과 추적을 목표로 한다(2024). [사실] | [^ref-636] |
| ISO 3691-4:2023 | 표준 | 연계 대상. AGV·자율이동로봇(Autonomous Mobile Robot, AMR)을 포함한 무인 산업용 차량과 그 시스템의 안전 요구사항과 검증 수단을 정한다. 시험 항목 세부는 미확인이다. [사실] | [^ref-470] |
| ASTM F45 위원회 | 표준 | 연계 대상. 무인 자동 유도 산업 차량의 용어·권고 관행·시험 방법을 개발하며 환경 영향, 도킹·주행, 물체 감지·보호, 통신·통합 분과를 두고 NIST 가 참여한다(2026-09-25 확인). [사실] | [^ref-639] |
| KS B ISO 18646 시리즈 | 표준 | 연계 대상. 서비스 로봇 성능 기준과 시험 방법의 KS 부합화로, 제1부는 바퀴형 로봇의 이동 능력을 다루고(KS B ISO 18646-1, 2022 확인) 제3부 조작 등 다른 부가 있다. 제2부 내용은 미확인이다. [사실] | [^ref-640] |
| 한국로봇산업진흥원 시험평가 | 평가 프로그램 | 연계 대상. KS·ISO·IEC·CISPR 등 표준 시험 방법을 적용하고 경사 노면·특수 노면·계단·주행 내구 같은 주행 성능 시험을 수행한다(2026-09-25 확인). [사실] | [^ref-641] |
| ros2_fault_injection | 오픈소스 | ROS 2 장애 주입과 시나리오 단정, CI 연동(README 기준, 성숙도·라이선스 미확인). [사실] | [^ref-633] |
| ROSMonitoring | 오픈소스 | ROS 1·ROS 2 런타임 검증 틀. [사실] | [^ref-634] |
| Open-RMF 시뮬레이션 | 오픈소스 | 실제와 같은 코드로 반복 가능한 시나리오 시험. [사실] | [^ref-406] |
| LSMART | 오픈소스 | FMS 안에서 MAPF 알고리즘을 현실적으로 평가하는 시뮬레이터(프리프린트). [사실] | [^ref-637] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-008]: NIST, ARIAC Documentation, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/, 접근일 2026-09-24 (원문 미열람)
[^ref-629]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-630]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Scoring, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html, 접근일 2026-09-25
[^ref-633]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25
[^ref-634]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25
[^ref-636]: IDM Lab (USC) 게재 초록, 저자 미확인, The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration], 2024, https://idm-lab.org/bib/abstracts/Koen24p.html, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: NIST, ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles, 미확인, https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-640]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010113281, 접근일 2026-09-25 (원문 미열람)
[^ref-641]: 한국로봇산업진흥원(KIRIA), 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼, 미확인, https://kiria.org/rp/kiria/tva/inr/page.dn, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-59 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-59 | 23. 시험·형식 검증·벤치마크 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-59/pages/topics/2026/2026-09-25-area23-s4.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크 — 핵심 개념과 용어"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-629, ref-633, ref-634, ref-186, ref-642, ref-643]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md#4
---

[홈](../../index.md) › [주제](../index.md) › 23. 시험·형식 검증·벤치마크 — 핵심 개념과 용어

# 23. 시험·형식 검증·벤치마크 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 장애를 계획적으로 넣어 보는 시험, 변경 뒤 다시 돌리는 시험, 수학적 모델로 성질을 확인하는 검증, 운영 중 감시, 공통 기준으로 비교하는 벤치마크를 함께 다룬다. [사실][^ref-629][^ref-633]
- 이 페이지는 [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 장애를 계획적으로 넣어 보는 시험, 변경 뒤 다시 돌리는 시험, 수학적 모델로 성질을 확인하는 검증, 운영 중 감시, 공통 기준으로 비교하는 벤치마크를 함께 다룬다. [사실][^ref-629][^ref-633]

- **장애 주입(Fault Injection)** — 시험 중 메시지·서비스·장비에 지연·누락·고장을 계획적으로 넣어 시스템이 감지·복구하는지 본다. 산업 자동화용 민첩 로봇 경진대회는 경진 중 컨베이어 정지나 공구 파지 실패를 주입한다. [사실][^ref-629]
- **회귀 시험(Regression Testing)** — 변경 뒤 기존의 정상·장애 시나리오를 다시 실행한다. ros2_fault_injection 은 README 기준으로 시나리오 단정 결과를 종료 코드로 지속적 통합(Continuous Integration, CI)에 넘긴다. [사실][^ref-633]
- **형식 검증(Formal Verification)과 [교착 (Deadlock)](../../glossary/deadlock.md)** — 시스템을 수학적 모델로 표현해 교착 부재 같은 성질을 확인한다. 창고 무인운반차(Automated Guided Vehicle, AGV) 시스템을 전이 시스템으로 인코딩하고 이진 결정 다이어그램(Binary Decision Diagram, BDD)으로 분석한 사례가 있다. [사실][^ref-643]
- **런타임 검증(Runtime Verification)** — 실행 중 사건을 감시기로 관찰해 명세 위반을 기록하거나 걸러 낸다. [사실][^ref-634]
- **벤치마크(Benchmark)** — 공통 인스턴스와 지표로 알고리즘을 비교한다. [다중 에이전트 경로 찾기 (MAPF)](../../glossary/mapf.md) 분야는 논문마다 가정과 목적함수가 달라 공통 용어와 격자 기반 벤치마크가 제안됐다. [사실][^ref-186]
- **[적합성 시험 (Conformance Test)](../../glossary/conformance-test.md)** — 로봇 연동 인터페이스가 규격대로 동작하는지 확인하는 시험이다. VDA 5050 에 대해서는 이번 조사에서 공식 적합성 시험 절차를 확인하지 못했고, 확인된 인증은 제조사와 관제 소프트웨어 업체 사이의 쌍별 인증으로 보인다. [추정] 벤더 주장[^ref-642]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-629]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-25
[^ref-633]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25
[^ref-634]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-642]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-643]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-59 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-59 | 23. 시험·형식 검증·벤치마크 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-59/pages/topics/2026/2026-09-25-area23-s11.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크 — 열린 질문"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-637, ref-642]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md#11
---

[홈](../../index.md) › [주제](../index.md) › 23. 시험·형식 검증·벤치마크 — 열린 질문

# 23. 시험·형식 검증·벤치마크 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 질문은 이번 실행에서 부분 근거만 얻었거나 새로 제기된 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 질문은 이번 실행에서 부분 근거만 얻었거나 새로 제기된 것이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-055** (상태: 열림) VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? — 부분 근거: 쌍별 연동 인증 발표(벤더 주장)만 확인했고 공식 절차는 찾지 못했다. [추정][^ref-642]
- **oq-058** (상태: 열림) 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? — 부분 근거: 격자 가정의 한계를 들어 FMS 안에서 평가하는 시뮬레이터가 제안됐으나 실제 처리량 측정은 아니다. [사실][^ref-637]
- **oq-063** (상태: 열림) ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? — 이번 실행에서 조사하지 않았다.
- **oq-077** (상태: 열림) 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? — 이번 실행에서 조사하지 않았다.
- (신규, 상태: 열림) 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가?
- (신규, 상태: 열림) BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가?
- (신규, 상태: 열림) 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-637]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-642]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-59 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-59 | 23. 시험·형식 검증·벤치마크 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-25-59/pages/topics/2026/2026-09-25-area23-s10.md

```markdown
---
title: "23. 시험·형식 검증·벤치마크 — 다른 연구영역과의 연결"
type: topic
category: "F. 도입·검증·유지관리"
primary_area_no: 23
related_areas: [9, 12, 15, 19, 20, 22, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-633, ref-634, ref-186, ref-637, ref-470, ref-642, ref-643, ref-406]
last_run: 2026-09-25
version: 1
split_from: docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md#10
---

[홈](../../index.md) › [주제](../index.md) › 23. 시험·형식 검증·벤치마크 — 다른 연구영역과의 연결

# 23. 시험·형식 검증·벤치마크 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 시뮬레이션 환경을 22. 시뮬레이션·예측용 디지털 트윈과 공유하고, 시험 대상 논리와 표준을 여러 영역에서 받는다는 것이 구축자 의견이다. [의견][^ref-406]
- 이 페이지는 [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 시뮬레이션 환경을 22. 시뮬레이션·예측용 디지털 트윈과 공유하고, 시험 대상 논리와 표준을 여러 영역에서 받는다는 것이 구축자 의견이다. [의견][^ref-406]

- [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) — 반복 가능한 시나리오·예외 상황 탐색 환경은 두 영역이 공유하지만, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측을, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인을 목적으로 나누는 것이 분류 원문 정의에 맞는다는 것이 구축자 의견이다. [의견][^ref-406]
- [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) — MAPF 벤치마크, FMS 안의 현실적 평가, 창고 AGV 교착 분석이 경로·교통 관리 논리를 시험 대상으로 삼는다. [사실][^ref-186][^ref-637][^ref-643]
- [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) — 런타임 검증 틀은 안전하지 않은 메시지·서비스 요청을 걸러 낼 수 있어 명령 실행 보장과 이어진다. [사실][^ref-634]
- [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 런타임 검증은 운영 중 사건을 감시·기록한다. [사실][^ref-634]
- [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) — 계획 실패 시 복구 방식을 비교한 연구가 있어 복구 설계를 시험으로 확인하는 연결점이 된다. [사실][^ref-637]
- [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) — 펌웨어·어댑터 업데이트마다 장애 시나리오를 다시 돌리는 회귀 시험이 필요해 보인다. [추정][^ref-633][^ref-406]
- [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) — ISO 3691-4 의 차량 안전 요구사항·검증 수단이 로봇 쪽 안전 검증의 기준이다. [사실][^ref-470]
- [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — VDA 5050 연동 인증이 쌍별로 이뤄진다는 발표가 있어 연동 승인 시험 기준이 두 영역의 과제로 보인다. [추정] 벤더 주장[^ref-642]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)
- 관련 영역: [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md), [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md), [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md), [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-633]: reeceholland (ros2_fault_injection GitHub), ros2_fault_injection — README, 미확인, https://github.com/reeceholland/ros2_fault_injection, 접근일 2026-09-25
[^ref-634]: University of Liverpool Autonomy and Verification (ROSMonitoring GitHub), ROSMonitoring: a Runtime Verification Framework for ROS — README, 미확인, https://github.com/autonomy-and-verification-uol/ROSMonitoring, 접근일 2026-09-25
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-637]: Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J., Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems, 2026-02-17, https://arxiv.org/abs/2602.15721, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-642]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-643]: von Berg, B., Aichernig, B. K., & Wedenik, F., BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper), 2026-05, https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-59 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-59 | 23. 시험·형식 검증·벤치마크 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-25-59/docs_tree.txt

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
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
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
glossary/fleet-adapter.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/grai.md
glossary/hallucination.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoorgml.md
glossary/information-delivery-specification.md
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
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/order-batching.md
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
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/root-cause-analysis-rca.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semi-open-queueing-network.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/situation-awareness-based-agent-transparency.md
glossary/skill.md
glossary/slot-filling.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
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
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
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
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 536건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 137개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
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
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
```

### docs/open-questions.md (요약: 대상 영역 [23] 에 걸린 4건 / 전체 86건)

```markdown
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 9, 23, 28)
- oq-058 [열림] 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? (영역 15, 23)
- oq-063 [열림] ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? (영역 17, 23)
- oq-077 [열림] 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? (영역 21, 6, 23)
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

### runs/2026-09-25-59/verification2.json

```json
{
  "run_id": "2026-09-25-59",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "태그 상향 미이행: 1차에서 [추정] 유지로 처분한 f8 의 앞부분('센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당')을 세부영역 페이지 9절에서 [사실][^ref-633]로 올렸다. README 로 확인되는 것은 지원 메시지 유형(오도메트리·레이저 스캔·IMU·점군, Twist 는 명령 조작 대상)뿐이다. 그것이 '로봇 자체 견고성 시험에 해당한다'는 분류는 추론이므로 [추정]이어야 한다. 이번 재검증 전에는 없던 지적이다."
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
      "ref-629·ref-630 은 ref-008(NIST ARIAC Documentation)의 하위 페이지다. ARIAC 소개 문장에 ref-008 을 재사용했으므로 1차 지시대로 처리됐다.",
      "ref-406 은 기존 id 를 재사용했다."
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
    "세부영역 페이지 9절 '연계 대상: ros2_fault_injection 이 기본으로 다루는 … 따로 다룬다.' 문장을 둘로 나눈다. 지원 메시지 유형 사실(오도메트리·레이저 스캔·IMU·점군은 주입 대상이고 속도 명령 Twist 는 명령 조작 대상이다)은 [사실][^ref-633]으로 두고, '센서 신호 장애는 로봇 자체 인식·주행의 견고성 시험에 해당한다'는 부분은 [추정][^ref-633]으로 되돌린다. 이유: 1차에서 f8 은 [추정] 유지로 처분했고, 태그를 올리는 것은 허용되지 않는다.",
    "세부영역 페이지 3절 첫 문장의 '로봇 시스템을 바꾼 뒤에도 장애 상황을 여전히 처리하는지 확인하는 일은 실무에서도 어려운 문제로 보고되며'를 '로봇 시스템 시험은 실무에서도 어려운 문제로 보고되며'처럼 f6 범위로 줄인다. 이유: ref-632(f6)는 로봇 시스템 시험 전반의 어려움을 다룬다. 변경 후 장애 처리 확인을 따로 보고했다는 내용은 브리프에 없다(드리프트).",
    "세부영역 페이지 10절 요약 문장 '이 영역은 시뮬레이션 환경을 … 받는다. [의견][^ref-406]'과 분리 주제 페이지 docs/topics/2026/2026-09-25-area23-s10.md 의 같은 문장(1절 세 줄 요약, 3절 첫 문장)에 '구축자 의견'임을 밝힌다. 이유: 1차 수정 지시(f20 의견 주체 표시)가 상세 항목에만 이행됐고 요약 문장에는 빠졌다.",
    "docs/topics/2026/2026-09-25-area23-s4.md 3절 적합성 시험 항목의 '[추정][^ref-642]'를 '[추정] 벤더 주장[^ref-642]'로 고친다. 이유: 근거가 제조사 보도자료(ref-642)뿐이다. 같은 근거를 쓴 area23-s10 페이지와 9절에는 '벤더 주장'을 병기했으므로 표기를 맞춘다.",
    "세부영역 페이지 본문에서 약어와 전문용어의 첫 등장을 풀어 쓴다. 3절에서는 '다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF)', '플릿 관리 시스템(Fleet Management System, FMS)'으로 쓰고 용어집 표기로 링크한다. 9절에서는 AGV·AMR·IMU 의 첫 등장을 풀어 쓴다. 이유: 이 설명은 분리 주제 페이지에만 있고 세부영역 페이지에는 약어만 남아 문체 규칙에 어긋난다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(fetch_mode mirror_only)에서 검증됐다. 확인 24건, 미확인 0건, 교차 확인 0건. 강등: 없음(태그는 모두 유지하되 f14·f15·f16 은 확인되지 않은 세부를 빼도록 지시했다). 원문 미열람 출처: ref-631, ref-632, ref-186, ref-636, ref-637, ref-470, ref-639, ref-640, ref-641, ref-642, ref-643. 원문을 연 출처는 GitHub 미러를 통한 ref-629, ref-630, ref-633, ref-634, ref-406 이다. 주의: 모든 주장이 단일 출처에 기댄다. ref-631·ref-632·ref-186 는 검증 검색 예산(리서치 22회 사용, 남은 8회)을 다른 출처에 써서 검증자가 다시 검색하지 못했고, 서지만 대조했다. 9절의 ROP 직접 범위와 연계 범위 구분, 분류 원문 질문에 대한 답(f21)은 추정이다. 물류 오케스트레이션 소프트웨어의 회귀 시험·장애 주입 현장 사례와 VDA 5050 공식 적합성 절차는 확인되지 않았다. oq-055·oq-058 은 부분 근거만 있고, oq-063·oq-077 은 이번에 다루지 않았다. 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 2건 처리 지시(9절 f8 태그 상향, 3절 f6 범위 밖 서술). 그 밖에 f20 요약 문장 의견 주체 누락, 주제 페이지 area23-s4 의 f19 '벤더 주장' 병기 누락, 세부영역 페이지 약어 첫 등장 풀이 누락을 고치도록 지시했다. [분류원문] 보존, 섹션 순서 준수(형식 검증 코드 통과), 링크 유효. 1차 수정 지시 16건은 위 항목 외에는 이행됐다. 자동 분리 주제 페이지 5건은 원 절 내용을 옮긴 것으로 보았다. reference_updates 의 cited_by 에 분리 주제 페이지가 일부 빠져 있으나 퍼블리셔 자동 영역(reference-cited-pages)이 다시 만든다.",
  "retry_reason": null
}
```
