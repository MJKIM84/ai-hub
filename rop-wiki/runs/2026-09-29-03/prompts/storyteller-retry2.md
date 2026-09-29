(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-03
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 11. 채팅으로 실제 상황 시뮬레이션 재현 (C. 채팅 기반 구성·운영)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- retry_count: 2
- max_retries: 2

## 입력

### runs/2026-09-29-03/target.json

```json
{
  "run_id": "2026-09-29-03",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 95,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 11,
    "area_name": "11. 채팅으로 실제 상황 시뮬레이션 재현",
    "category": "C. 채팅 기반 구성·운영",
    "category_letter": "C"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=11"
}
```

### runs/2026-09-29-03/research.json

```json
{
  "run_id": "2026-09-29-03",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 11,
    "area_name": "11. 채팅으로 실제 상황 시뮬레이션 재현",
    "category": "C. 채팅 기반 구성·운영"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 자동 시뮬레이션 모델 생성·사건 트레이스·시나리오 재구성·로그 재생(rosbag)·조건부 검증 용어 없음(디지털 트윈·이산 사건 시뮬레이션·현실 격차·시뮬레이션 V&V 는 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 짝 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]",
    "자연어 대화나 텍스트 설명에서 실행 가능한 시뮬레이션 모델·시나리오를 만드는 연구는 무엇이 있고, 정확도와 한계는 어떻게 보고되는가? (섹션 3·6·8 겨냥)",
    "운영 기록(이벤트 로그·로봇 통신 기록)을 지정해 시뮬레이션을 자동으로 만들거나 재생하는 방법과 도구는 무엇인가? (섹션 4·6·7 겨냥)",
    "재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 어떤 방법으로 비교하고, 맞지 않는 부분을 어떻게 찾아내는가? (섹션 4·6 겨냥)",
    "대화로 로봇 수·경로·정책 같은 조건을 바꿔 다시 돌리고 결과 차이를 설명하는 언어 모델 에이전트 방식은 무엇이며 무엇을 검증해야 하는가? (섹션 6·8·11 겨냥, 13. 대화형 기능의 신뢰·기반 연결)",
    "병원·제조 공장·물류창고·실외 등 현장 유형별로 실제 상황을 시뮬레이션에 재현하거나 조건을 바꿔 비교한 사례(국내 자료 포함)는 무엇인가? (섹션 5 겨냥)",
    "실제 상황 재현에서 ROP가 직접 맡을 것(기록→시나리오 변환, 대화, 비교·설명)과 시뮬레이션 엔진·로봇 자체 기록 재생처럼 외부에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Elbasheer 외(2025, Journal of Intelligent Manufacturing)는 대규모 언어 모델과 자동 시뮬레이션 모델 생성(ASMG)을 결합해 자연어 대화에서 실행 가능한 제조 시스템 시뮬레이션 모델을 직접 만드는 방법을 제안했고, 의도 표현→템플릿 기반 지식 추출→객체지향 데이터 기반 구성요소로 모델 구성→실행·결과 분석의 4단계로 18개 동작 유형을 지원하며 응답 시간이 단순 동작 8초에서 전체 시스템 생성 5분까지라고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-836"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: LLM 과 ASMG 를 통합해 자연어 대화에서 실행 가능한 시뮬레이션 모델을 직접 생성. 4단계 절차(의도 표현, 구조화 템플릿으로 지식 추출, 객체지향 데이터 기반 구성요소로 모델 구성, 자원 이용률·병목·일정 분석). 성능 시험에서 18개 동작 유형, 응답 시간 8초(단순)~5분(전체 제조 시스템 생성). Semantic Scholar API 초록으로 확인.",
      "as_of": "2025-11-14",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "Kleiman 외(2025)의 Simulation Agent 프레임워크는 시뮬레이션이 언어 모델의 답을 실제 시스템의 구조적 표현에 접지시키고, 언어 모델은 비전문가가 복잡한 시뮬레이터를 대화로 다루게 하는 인터페이스가 되는 결합 구조를 제안하며 초록에는 정량 평가가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-824"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 시뮬레이션은 구조적 정확성이 있으나 비전문가가 쓰기 어렵고, LLM 은 대화 인터페이스를 주지만 접지된 인과 추론이 약함. \"utilizing simulations to ground the LLMs\" 라는 결합을 제안. 정량 결과·벤치마크는 초록에 없음.",
      "as_of": "2025-05-19",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Xia 외(2026)는 언어 모델 에이전트들이 사용자 질의와 기준 구성에서 구조화 과제 표현을 만들고 실험을 설계해 매개변수 구성을 나란히 시뮬레이션한 뒤 결과를 해석해 권고를 내는 다중 에이전트 프레임워크를 제약 공정 설계에 적용했고, 언어만 쓰는 방식보다 출력 구체성과 사용자 평가 정확도·유용성이 높았다고 절제 실험과 사례로 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-832"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 사용자 질의·기준 구성 → 구조화 과제 표현 → 실험 설계 → 비교 시뮬레이션 실행 → 결과 해석 → 최적화 권고. 제약 공정 설계 적용. 언어 전용 접근보다 구체성·사용자 평가 정확도·유용성 개선, 절제 실험. \"reasoning through intervention, comparison, and observation\".",
      "as_of": "2026-08-22",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "대화로 모델을 만드는 연구(f1), 시뮬레이션으로 언어 모델을 접지하는 구조(f2), 에이전트가 구성을 바꿔 비교 실험을 돌리는 연구(f3)를 함께 보면, 이 영역의 '대화로 조건 바꿔 비교'는 언어 모델이 시뮬레이터의 매개변수(로봇 수·경로·정책)를 바꿔 실행하고 결과 차이를 설명하는 에이전트 구조로 구현되며 결론은 언어 모델의 추론이 아니라 시뮬레이션 출력에 근거해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-836",
        "ref-824",
        "ref-832"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "세 연구가 공통으로 언어 모델을 인터페이스·실험 설계에 두고 수치 결론은 시뮬레이션 실행에서 얻는 구조를 택함(f1·f2·f3 종합 추정).",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f5",
      "claim": "Chen 외(2026)는 자연어 환경 사양에서 DEVS 형식의 이산 사건 시뮬레이터를 생성하되 구성요소 상호작용의 구조 추론과 구성요소별 사건·타이밍 논리 생성을 단계로 나누고, 생성된 시뮬레이터가 내는 구조화 사건 트레이스를 사양에서 도출한 시간·인과·의미 제약과 대조해 검증하는 벤치마크를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-825"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 공급망·업무 프로세스 같은 이산 사건 도메인에서 자연어 사양으로부터 DEVS 세계 모델을 합성. \"simulators emit structured event traces, which are then validated against specification-derived temporal, causal, and semantic constraints\". 장기 시뮬레이션에서 일관성 유지.",
      "as_of": "2026-03-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Camargo·Dumas·González-Rojas(Simod, 2020)는 정보시스템 이벤트 로그에서 프로세스 모델을 자동 발견하고 시뮬레이션 매개변수를 추출해 업무 프로세스 시뮬레이션 모델을 만들되, 하이퍼파라미터 최적화로 시뮬레이션 행동과 로그에서 관측된 행동의 유사도를 최대화하는 방법을 도구로 구현하고 여러 도메인 로그로 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-828"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 실행 로그에서 시뮬레이션 모델을 자동 발견, 단계별 설정 매개변수를 하이퍼파라미터 최적화로 탐색해 \"similarity between the behavior of the simulation model and the behavior observed in the log\" 를 최대화. 여러 도메인에서 도구로 평가.",
      "as_of": "2020",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "로그에서 시뮬레이션 모델을 발견하고 로그와의 유사도로 조정하는 방법(f6)과 생성된 시뮬레이터의 사건 트레이스를 제약과 대조하는 방법(f5)을 보면, 이 영역의 '운영 기록을 지정하면 재현'과 '재현 충실도 확인'은 기록에서 모델·매개변수를 뽑아 돌린 뒤 재현 트레이스와 실제 기록의 사건 순서·시각 유사도를 재는 흐름으로 구현할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-828",
        "ref-825"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Simod 의 로그 유사도 최대화와 DEVS 연구의 사건 트레이스 검증을 이 영역의 기능 정의(운영 기록 지정, 시각·위치·사건 순서 비교)에 대응시킨 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f8",
      "claim": "Ghasemloo·Eckman·Li(2026)는 시뮬레이션 모델·디지털 트윈을 관측된 시스템 상태에서 반복 초기화하고 일부 확률 입력을 실제 관측값으로 고정한 채 나머지를 시뮬레이션해 조건부 출력 분포에 적합도 검정을 하는 '서브트레이스 조건부 검증'을 제안했고, 어느 입력 모델이 실제와의 불일치를 만드는지 진단하는 도구를 M/M/1 과 직렬 대기행렬 디지털 트윈 사례로 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-826"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 과거 트레이스 데이터에서 일부 확률 입력 모델의 무작위 원시값을 관측 실현값으로 고정, 조건부 출력 분포를 실제 시스템 행동과 비교(적합도 검정). 주변 분포 검증이 놓치는 오지정을 잡고 불일치 원인 입력 모델을 진단. 사례: M/M/1, 직렬 대기행렬 디지털 트윈.",
      "as_of": "2026-07-19",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "서브트레이스 조건부 검증(f8)이 불일치의 원인이 되는 입력 모델을 진단하는 점을 보면, 이 영역의 '맞지 않는 부분을 알려 준다'는 기능은 도착·처리 시간·고장 같은 입력 모델 가운데 어느 것이 실제 기록과 어긋나는지를 통계 절차로 짚어 대화로 설명하는 방식으로 뒷받침될 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-826"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8 의 진단 도구를 이 영역의 재현 충실도 확인 기능에 대응시킨 추정. 로봇 플릿 적용 사례는 확인하지 못함.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "rosbag2 는 ROS 2 시스템의 통신을 기록·재생하는 공식 도구로, ros2 bag record 로 토픽 메시지를 시각과 함께 저장하고 ros2 bag play 로 재생하며 재생 속도·시작 시점(seek)·토픽 선택·반복·/clock 토픽으로 시뮬레이션 시각 발행 같은 옵션을 두고 MCAP·SQLite3 저장 형식을 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"the tool for recording and playback of communications in ROS 2 systems\". record(전체 토픽 -a, 필터, 압축, 분할), play(--rate, --seek, --topics, loop, /clock 발행), 저장 형식 MCAP·SQLite3. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f11",
      "claim": "연계 대상: rosbag2 로 로봇 통신 기록을 재생하는 일은 로봇 한 대의 센서·제어 메시지를 되살려 로봇 자체 소프트웨어를 디버깅하는 로봇 자체 지능·제어 쪽 도구이며, 11. 채팅으로 실제 상황 시뮬레이션 재현이 다루는 재현은 플릿 수준 실행 기록(작업·배정·위치·사건 시각)을 시나리오로 바꿔 여러 로봇과 설비의 상황을 다시 돌리는 일이므로 두 층을 구분해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "rosbag2 README 가 기록 단위를 ROS 2 토픽 메시지로 두는 점과 분류 원문 19장의 '로봇 자체 지능·제어' 경계를 대응시킨 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "SoVAR(Guo 외, ASE 2024)는 대규모 언어 모델 프롬프트로 사고 보고서 텍스트에서 사고 정보를 추출하고 제약을 풀어 차량 궤적을 생성해 여러 지도 구조에 사고 시나리오를 재구성하는 도구로, NHTSA 사고 보고서로 Baidu Apollo 를 시험해 5종의 안전 위반을 찾았으며, 보고서 정보와 시뮬레이션 지도의 대응이 어렵고 기존 재구성 방법의 정보 추출 정확도가 제한적이라는 한계를 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-834"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 언어 패턴 프롬프트로 사고 보고서에서 정보 추출, 제약 해결로 궤적 생성, 여러 지도에 재구성. NHTSA 보고서·Baidu Apollo 시험, \"5 distinct safety violation types\". 한계: 사고 정보와 시뮬레이션 지도 대응, 추출 정확도.",
      "as_of": "2024-09-12",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f13",
      "claim": "OmniTester(Lu 외, 2024)는 멀티모달 언어 모델에 프롬프트 설계, SUMO 교통 시뮬레이터 연동, 검색 증강 생성과 자기 개선을 결합해 자율주행 시험 시나리오를 만들며, 실제 사고 보고서에서 추출한 새 시나리오를 재구성하고 생성 시나리오의 현실성·제어 가능성을 검증했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-835"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 프롬프트 공학, SUMO 연동으로 코드 복잡도 완화, RAG·자기 개선. 제어 가능한 매개변수의 도전적 시나리오 생성, 사고 보고서의 새 시나리오 재구성, 현실성·제어 가능성 검증.",
      "as_of": "2024-09-10",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f14",
      "claim": "서로 다른 두 연구 그룹(SoVAR, OmniTester)이 각각 언어 모델로 사고 보고서 텍스트에서 시나리오를 재구성해 시뮬레이터에서 재현하는 방법을 자율주행 시험에 적용했다고 보고해, 텍스트 기록에서 실제 상황을 시뮬레이션으로 재현하는 접근이 한 곳 이상에서 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-834",
        "ref-835"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "SoVAR(난징대 등, ASE 2024)와 OmniTester(칭화대 등, 2024)가 독립적으로 사고 보고서→시나리오 재구성을 보고. 둘 다 arXiv 초록 확인이라 medium.",
      "as_of": "2024-09",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Chat2Scenic(Gao 외, 2026)은 규정 문서를 대화형 인터페이스와 도메인 특화 언어 지식의 검색 증강 생성으로 반복 정제해 Scenic 시나리오로 바꾸며, 규정에서 뽑은 123개 시나리오에서 컴파일 성공 76.42%, 프레임워크 정확도 58.17%를 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-833"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 반복 RAG, 대화형 인터페이스로 시나리오를 상호작용 정제, DSL 문법 접지. NHTSA·UN 규정에서 123개 시나리오, 컴파일 성공 76.42%, 프레임워크 정확도 58.17%. 실제 사고 보고서 재구성은 초록에 없음. 코드 공개.",
      "as_of": "2026-07-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "텍스트에서 시나리오를 재구성하는 세 연구(f12·f13·f15)가 정보 추출 정확도 제한, 지도 대응의 어려움, 58% 수준의 프레임워크 정확도를 보고하므로, 채팅으로 설명한 상황을 시뮬레이션에 재현한 결과는 언어 모델 출력 그대로 쓰지 말고 사람이 확인해야 하며, 실제 기록(위치·시각·사건)이 있으면 말로 한 설명보다 기록을 우선 입력으로 삼는 것이 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-834",
        "ref-835",
        "ref-833"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f12 의 한계 서술, f15 의 정확도 수치, f13 의 검증 필요성을 종합한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "BedreFlyt(Sieve 외, 오슬로대, 2025)는 병원 입원 병동의 환자 입원 흐름을 최적화 문제로 바꾸는 디지털 트윈으로, 실행 가능한 형식 모델·온톨로지·SMT 해결기를 결합하고 오케스트레이터 설정으로 평균·최악 자원 수요와 가용 자원 변동을 아우르는 what-if 시나리오를 만들어 병상 배정 문제에 적용했다.",
      "tag": "사실",
      "source_ids": [
        "ref-829"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 입원 환자 흐름을 최적화 문제로 변환, 형식 모델·온톨로지·SMT. 시나리오는 \"average-case as well as worst-case resource needs\" 와 가용 자원 변동을 오케스트레이터 설정으로 탐색. 병상 배정 사례.",
      "as_of": "2025-05-07",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "우지영·신효진·전창훈·박상찬(Electronics, 2025)은 감염병 환자가 도착했을 때 병원에서 일어나는 전 과정을 시뮬레이션하는 연합(federated) 디지털 트윈으로 간호사 추종 음압 이송 침대 로봇 여러 대를 동시에 운용하는 한국 병원 사례를 제시하고 시나리오 기반 시뮬레이션으로 시스템 성능을 검증했다.",
      "tag": "사실",
      "source_ids": [
        "ref-837"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록(Semantic Scholar API): 감염병 상황용 간호사 추종 환자 이송 침대 로봇의 디지털 트윈, 여러 침대 로봇 동시 운용을 위한 연합 디지털 트윈 구조, \"all processes that occur in a hospital when an infectious disease patient arrives\" 를 시뮬레이션해 시나리오 기반 성능 검증. 저자 한글 표기는 영문 이름에서 옮긴 것으로 미확인.",
      "as_of": "2025-12-17",
      "site_type": "병원",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "이동건 외(성균관대·LG전자, 한국CDE학회 논문집 2021)는 자동물류시스템을 설계 단계에서 가상으로 검증하고 운영 단계에서 실시간 모니터링·분석하는 디지털트윈을 개발해 국내 제조업체의 AGV 자동물류시스템에 적용하고 진단·분석·예측·최적화의 실효성을 검증했다.",
      "tag": "사실",
      "source_ids": [
        "ref-830"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 시스템이 구성·운영되기 전에는 문제를 예측·대응할 수 없다는 한계를 디지털트윈으로 극복. 설계 단계 가상 검증 + 운영 단계 실시간 모니터링·분석. 국내 제조업체 AGV 시스템 적용, 진단·분석·예측·최적화 검증.",
      "as_of": "2021-12",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f20",
      "claim": "Valiollahi 외(Scientific Reports, 2026)는 운송·조립 역할이 다른 이기종 로봇 플릿과 공정·공장 배치를 함께 모델링한 디지털 트윈 시뮬레이션으로 기존 공장(브라운필드)에서는 혼잡 때문에 플릿 확장 효과가 체감하고, 신규 공장(그린필드)에서는 배치·플릿 규모·역할 비율을 비교해 로봇당 생산성을 줄이지 않고 처리량을 최대 3.5배 높이는 구성을 찾았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-838"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록(Semantic Scholar API): 공정·배치·이기종 로봇 팀 통합 모델링, 브라운필드에서 혼잡으로 확장성 한계, 그린필드에서 배치·팀 규모·역할 비교, \"up to 3.5× throughput gains without reducing productivity per robot\". 실제 공장 데이터 대조 여부는 초록에서 확인 못 함.",
      "as_of": "2026-07-18",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "Yang 외(2025)는 언어 모델을 디지털 트윈에 쓰는 연구를 기술(description)–예측(prediction)–처방(prescription) 프레임워크와 적용 단계별 분류로 정리하고, 정확한 모델링을 위한 데이터 부족·분석 비효율·물리–디지털 상호작용의 설명 부족을 과제로 꼽으며 자동 모델링·최적화를 보이는 기업 디지털 트윈 시스템을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-827"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 과제 \"limited data for accurate system modeling, inefficiencies in system analysis, and a lack of explainability\". 통일된 description-prediction-prescription 프레임워크, 단계별 LLM 기능 분류, 기업 디지털 트윈 시스템 시연.",
      "as_of": "2025-03-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "자연어에서 시뮬레이션 모델을 만들거나(Elbasheer 외, Chen 외) 언어 모델 에이전트가 시뮬레이션 실험을 설계·해석하는(Xia 외) 연구는 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과 47. AI·학습·적응과 모델 운영에 속하는 방법이며, 원문 교차 규칙에 따라 대화가 부르는 엔진 영역인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 이 영역 양쪽에 연결해야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-836",
        "ref-825",
        "ref-832"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 C. 채팅 기반 구성·운영 주석(시나리오 구성과 실제 상황 재현은 33·36번)과 L. AI·학습 기술 주석을 f1·f3·f5 에 적용한 판단.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 11. 채팅으로 실제 상황 시뮬레이션 재현에서 ROP가 직접 맡을 범위는 플릿 실행 기록을 시나리오 사양으로 바꾸고, 대화로 조건 변경을 받아 시뮬레이션 실행을 요청하며, 재현 트레이스를 실제 기록과 대조해 차이를 설명하고 사람이 확인하게 하는 일이고, 이산 사건·물리 시뮬레이션 엔진과 로봇 자체 통신 기록 재생은 연계 대상으로 두는 것이 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-825",
        "ref-826",
        "ref-831",
        "ref-832"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5(사양→시뮬레이터 생성)·f8(트레이스 대조 검증)·f10(로봇 단위 재생)·f3(에이전트 실험 설계)에 분류 원문 19장 경계를 적용한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f24",
      "claim": "국내 자동물류 디지털트윈 연구가 설계 단계의 가상 검증과 운영 단계의 실시간 모니터링을 구분하는 점(f19)을 보면, 실제 상황 재현은 과거 기록을 가정한 조건으로 다시 실행하는 일이므로 34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현 쪽에 두고, 18. 실시간 세계 상태·데이터 일관성은 재현에 쓰는 기록의 원천으로만 연결해야 원문의 '현재 상태 표현' 대 '가정한 미래 실험' 구분을 지킬 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-830"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 I. 설계·시뮬레이션 주석(18번 현재 상태 표현 vs 34번 가정한 미래 실험)을 f19 의 설계 검증/운영 모니터링 구분에 대응시킨 판단.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-824",
      "org": "Kleiman, J., Frank, K., Voyles, J., & Campagna, S.",
      "title": "Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making",
      "published": "2025-05-19",
      "url": "https://arxiv.org/abs/2505.13761",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "시뮬레이션으로 언어 모델을 접지하고 언어 모델을 시뮬레이터의 대화 인터페이스로 쓰는 결합 프레임워크. 초록에 정량 평가 없음(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2505.13761",
      "source_unopened": false
    },
    {
      "id": "ref-825",
      "org": "Chen, Z., Zhuang, H., Li, Z., & Li, C.",
      "title": "Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism",
      "published": "2026-03-04",
      "url": "https://arxiv.org/abs/2603.03784",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 사양에서 DEVS 이산 사건 시뮬레이터를 단계별로 생성하고, 사건 트레이스를 시간·인과·의미 제약과 대조해 검증하는 벤치마크(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2603.03784",
      "source_unopened": false
    },
    {
      "id": "ref-826",
      "org": "Ghasemloo, M., Eckman, D. J., & Li, Y.",
      "title": "Subtrace-Conditional Validation of Simulation Models and Digital Twins",
      "published": "2026-07-19",
      "url": "https://arxiv.org/abs/2607.17088",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "관측 트레이스의 일부 입력을 고정한 조건부 시뮬레이션과 적합도 검정으로 디지털 트윈을 검증하고 불일치 원인 입력 모델을 진단하는 통계 방법(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2607.17088",
      "source_unopened": false
    },
    {
      "id": "ref-827",
      "org": "Yang, L., Luo, S., Cheng, X., & Yu, L.",
      "title": "Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges",
      "published": "2025-03-04",
      "url": "https://arxiv.org/abs/2503.02167",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델을 디지털 트윈 모델링에 쓰는 연구를 기술–예측–처방 프레임워크와 단계별 분류로 정리한 서베이(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2503.02167",
      "source_unopened": false
    },
    {
      "id": "ref-828",
      "org": "Camargo, M., Dumas, M., & González-Rojas, O.",
      "title": "Automated Discovery of Business Process Simulation Models from Event Logs",
      "published": "2020",
      "url": "https://arxiv.org/abs/1910.05404",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "이벤트 로그에서 프로세스 시뮬레이션 모델을 자동 발견하고 로그와의 행동 유사도를 최대화하도록 조정하는 Simod 방법(arXiv 판, Decision Support Systems 게재).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/1910.05404",
      "source_unopened": false
    },
    {
      "id": "ref-829",
      "org": "Sieve, R., Kobialka, P., Slaughter, L., Schlatte, R., Johnsen, E. B., & Tapia Tarifa, S. L. (University of Oslo)",
      "title": "BedreFlyt: Improving Patient Flows through Hospital Wards with Digital Twins",
      "published": "2025-05-07",
      "url": "https://arxiv.org/abs/2505.06287",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "병원 병동 환자 흐름 디지털 트윈으로 형식 모델·온톨로지·SMT 해결기를 결합하고 평균·최악 자원 시나리오를 오케스트레이터 설정으로 탐색(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2505.06287",
      "source_unopened": false
    },
    {
      "id": "ref-830",
      "org": "이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4))",
      "title": "자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용",
      "published": "2021-12",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자동물류시스템의 설계 단계 가상 검증과 운영 단계 실시간 모니터링·분석을 위한 디지털트윈을 국내 제조업체 AGV 시스템에 적용한 국내 학술지 논문(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861",
      "source_unopened": false
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (ros2/rosbag2 GitHub)",
      "title": "rosbag2 — README (Recording and playback of ROS 2 communications)",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "ROS 2 공식 기록·재생 도구. record/play 명령, 재생 속도·시작 시점·토픽 선택·반복·/clock 발행 옵션, MCAP·SQLite3 저장 형식을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/rosbag2/rolling/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-832",
      "org": "Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P.",
      "title": "LLM Agents Perform Controlled Experiments Using Simulation Models",
      "published": "2026-08-22",
      "url": "https://arxiv.org/abs/2608.23622",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 에이전트가 사용자 질의에서 실험을 설계하고 매개변수 구성을 나란히 시뮬레이션해 결과를 해석·권고하는 다중 에이전트 프레임워크를 제약 공정 설계에 적용(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2608.23622",
      "source_unopened": false
    },
    {
      "id": "ref-833",
      "org": "Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J.",
      "title": "Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving",
      "published": "2026-07-15",
      "url": "https://arxiv.org/abs/2607.14387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "규정 문서를 대화형 인터페이스와 반복 검색 증강 생성으로 Scenic 시나리오로 바꾸는 프레임워크. 123개 시나리오에서 컴파일 성공 76.42%, 프레임워크 정확도 58.17%(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2607.14387",
      "source_unopened": false
    },
    {
      "id": "ref-834",
      "org": "Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024)",
      "title": "SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing",
      "published": "2024-09-12",
      "url": "https://arxiv.org/abs/2409.08081",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델로 사고 보고서에서 정보를 추출하고 제약 해결로 궤적을 만들어 여러 지도에 사고 시나리오를 재구성하는 자율주행 시험 도구(ASE 2024 채택, arXiv 초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2409.08081",
      "source_unopened": false
    },
    {
      "id": "ref-835",
      "org": "Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S.",
      "title": "Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles",
      "published": "2024-09-10",
      "url": "https://arxiv.org/abs/2409.06450",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "멀티모달 언어 모델·SUMO·검색 증강 생성으로 자율주행 시험 시나리오를 만들고 사고 보고서 시나리오를 재구성하는 OmniTester(프리프린트).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2409.06450",
      "source_unopened": false
    },
    {
      "id": "ref-836",
      "org": "Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing)",
      "title": "Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems",
      "published": "2025-11-14",
      "url": "https://link.springer.com/article/10.1007/s10845-025-02732-z",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 자연어 대화에서 실행 가능한 제조 시뮬레이션 모델을 만드는 LLM+ASMG 방법(4단계, 18개 동작 유형, 응답 8초~5분). Springer 페이지는 인증 리다이렉트라 Semantic Scholar API 초록으로 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-837",
      "org": "Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24))",
      "title": "Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins",
      "published": "2025-12-17",
      "url": "https://www.mdpi.com/2079-9292/14/24/4954",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 감염병 환자 이송용 간호사 추종 침대 로봇 여러 대를 연합 디지털 트윈으로 시뮬레이션해 검증한 한국 병원 사례. MDPI 페이지 403 이라 Semantic Scholar API 초록으로 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-838",
      "org": "Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports)",
      "title": "Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts",
      "published": "2026-07-18",
      "url": "https://www.nature.com/articles/s41598-026-57316-5",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 이기종 로봇 플릿·공정·배치를 함께 모델링한 디지털 트윈으로 브라운필드·그린필드 공장 시나리오를 비교(최대 3.5배 처리량). Nature 페이지는 인증 리다이렉트라 Semantic Scholar API 초록으로 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
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
      "rationale": "섹션 3: f16(텍스트→시나리오 재현의 정확도 한계와 사람 확인 필요), f4(비교 결론은 시뮬레이션 출력에 근거), f21(데이터 부족·설명 부족 과제) / 섹션 4: f1(자동 시뮬레이션 모델 생성), f5(사건 트레이스), f12(시나리오 재구성), f10(bag 기록·재생), f8(서브트레이스 조건부 검증), f6(로그 기반 모델 발견) / 섹션 5: 병원 — f17(입원 흐름 what-if, 병상 배정), f18(국내 감염병 이송 로봇 연합 디지털 트윈, 시뮬레이션 검증임을 명시), 제조 공장 — f19(국내 AGV 자동물류 디지털트윈), f20(플릿·배치 시나리오 비교), 실외 — f12·f13(사고 보고서 재구성, 자율주행 시험 도구임을 명시) / 섹션 6: f1·f2·f3·f4(대화→모델 생성·에이전트 비교 실험), f5·f6·f7(사양·로그→시뮬레이터, 트레이스 대조), f8·f9(조건부 검증·불일치 진단), f12·f13·f14·f15·f16(텍스트→시나리오 재구성과 한계) / 섹션 7: f10·f11(rosbag2), f5(DEVS), f6(Simod), f13(SUMO), f15(Scenic) / 섹션 8: f1, f3, f5, f6, f8, f12, f13, f14, f17, f20, f21, 국내 f18·f19 / 섹션 9: f23(직접 범위: 기록→시나리오, 대화 조건 변경, 트레이스 대조·설명, 사람 확인; 연계: 시뮬레이션 엔진·로봇 통신 기록 재생), f11(연계 대상) / 섹션 10: 36. 가상 시운전·실제 상황 재현과 33. 시나리오 모델·편집(f22, 원문 주석의 짝), 34. 시뮬레이션·예측용 디지털 트윈과 18. 실시간 세계 상태·데이터 일관성(f24, 구분), 37. 관제 화면·실행 기록(f7 기록 원천), 38. 모니터링·이상 탐지·원인 분석(f9), 9. 채팅으로 시나리오 구성(f1·f5), 13. 대화형 기능의 신뢰·기반(f4·f16), 54. 시험·형식 검증·벤치마크(f8·f15), 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영(f22, 교차 규칙), 63. 병원·의료·62. 제조 공장(f17~f20) / 섹션 11: open_questions_new 4건. 다음 실행 후보: 36. 가상 시운전·실제 상황 재현 페이지에 f5·f8·f14 반영, 34. 시뮬레이션·예측용 디지털 트윈 페이지에 f20·f21 반영, 63. 병원·의료 페이지에 f18 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "자동 시뮬레이션 모델 생성",
      "term_en": "Automatic Simulation Model Generation (ASMG)",
      "definition": "사람이 시뮬레이션 도구를 직접 다루지 않고 데이터·사양·자연어 설명에서 실행 가능한 시뮬레이션 모델을 자동으로 만드는 기법이다."
    },
    {
      "term_ko": "사건 트레이스",
      "term_en": "Event Trace",
      "definition": "시스템이나 시뮬레이터가 실행 중에 낸 사건을 시각 순서대로 기록한 구조화 목록으로, 재현 결과를 실제 기록이나 제약과 대조하는 데 쓴다."
    },
    {
      "term_ko": "시나리오 재구성",
      "term_en": "Scenario Reconstruction",
      "definition": "사고 보고서·운영 기록 같은 실제 상황의 기록에서 정보를 추출해 시뮬레이터에서 다시 실행할 수 있는 시나리오로 만드는 일이다."
    },
    {
      "term_ko": "백 파일",
      "term_en": "Bag File (rosbag2)",
      "definition": "ROS 2 에서 토픽 메시지를 시각과 함께 저장한 기록 파일로, 나중에 재생해 로봇 소프트웨어를 실제 하드웨어 없이 시험·디버깅하는 데 쓴다."
    }
  ],
  "open_questions_new": [
    "플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 37. 관제 화면·실행 기록, 33. 시나리오 모델·편집 | 근거: f7 | 종류: 일반",
    "재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 36. 가상 시운전·실제 상황 재현, 54. 시험·형식 검증·벤치마크 | 근거: f9 | 종류: 일반",
    "대화로 재현·비교한 시뮬레이션 결과를 근거로 로봇 수·경로·정책을 바꾸는 결정에서 언어 모델의 결과 해석 오류를 막는 검증·승인 절차와 평가 지표는 무엇인가? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 13. 대화형 기능의 신뢰·기반 | 근거: f4 | 종류: 일반",
    "국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? | 관련 영역: 11. 채팅으로 실제 상황 시뮬레이션 재현, 61. 물류창고, 63. 병원·의료 | 근거: f19 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 1,
    "unverified": [
      "f1 Elbasheer 외 원문 미열람(Springer 인증 리다이렉트, d-nb.info PDF 는 텍스트 추출 실패) — Semantic Scholar API 초록만 사용, 시뮬레이션 도구·정확도 검증 방식 미확인",
      "f18 우지영 외 원문 미열람(MDPI 403) — 초록만 사용, 시뮬레이션 도구·정량 결과·승강기 연동 여부 미확인, 저자 한글 표기 미확인",
      "f20 Valiollahi 외 원문 미열람(Nature 인증 리다이렉트) — 초록만 사용, 실제 공장 데이터 대조 여부 미확인",
      "f6 Simod 의 정량 결과(유사도 수치)는 초록에 없어 미확인",
      "f12 SoVAR 의 재현 성공률 수치는 초록에 없어 미확인",
      "f14 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)",
      "f10 rosbag2 README 발행일 미확인",
      "Frydenlund 외 'Modeler in a box'(Sage), MDPI 'Conversational Digital Twins' 프레임워크, ScienceDirect 'LLM-driven discrete-event simulation'(JMS), Webb·Tokhi·Alkan AMR 플릿 디지털 트윈(SSRN), Springer AS/RS 디지털 트윈 검증 논문, WSC 2022 창고 디지털 트윈 논문(PDF 텍스트 추출 실패)은 열지 못해 넣지 않음",
      "국내 언어 모델 기반 시뮬레이션 재현 연구는 검색에서 확인되지 않음(국내 자료는 AGV 자동물류 디지털트윈과 병원 이송 로봇 연합 디지털 트윈뿐)",
      "대화만으로 실제 상황을 시뮬레이션에 재현한 실제 현장 운영 사례는 찾지 못함(연구 프로토타입·자율주행 시험 도구·시나리오 검증 사례뿐)"
    ],
    "scope_violations": [
      "f11: rosbag2 로봇 통신 기록 재생은 분류 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시함",
      "f12·f13·f14: 자율주행 시험용 사고 시나리오 재구성은 로봇 자체 지능 시험 도구이며 업종별 조건(실외 차량)에 걸치므로 텍스트→시나리오 재현 방법의 선례로만 제안함",
      "f3: 제약 공정 설계(비로봇) 연구는 에이전트 비교 실험 방법 참고로만 제안함",
      "f17: 병원 병상 배정 최적화는 ROP 직접 범위 밖의 업무 계획이므로 what-if 시나리오 구성 방식의 사례로만 제안함"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 19회/30, 신규 출처 15건/15(ref-824~ref-838, 예약 구간 안) 상한 도달로 Webb·Tokhi·Alkan 의 AMR 플릿 디지털 트윈 사고 대응 논문(검색 요약: 대리모델로 makespan 2~10% 단축), CALM-DT(언어 모델 자체를 디지털 트윈 시뮬레이터로 쓰는 연구), 병원 디지털 트윈 ML 검증 논문(arXiv 2303.04117)은 열었거나 확인했으나 넣지 못했다. 원문 열람 12건(webfetch 11, github_raw 1: rosbag2 README), 미열람 3건(ref-836·ref-837·ref-838, Semantic Scholar API 초록으로 기관·제목·발행일 확인). 교차 확인 1건(f14: SoVAR·OmniTester 독립 연구 그룹). 모든 finding 신뢰도 medium 이하(논문은 arXiv·DBpia 초록 확인). 분류 원문 핵심 질문(대화만으로 실제 상황 재현·조건 비교)에는 f1·f2·f3(대화→모델 생성·에이전트 비교 실험 가능), f5·f6·f8(사양·로그→시뮬레이터, 트레이스 대조 검증), f12·f13·f14·f15(텍스트 기록→시나리오 재구성 가능하나 정확도 한계)로 답했으며 결론은 '대화·텍스트로 시나리오를 만들고 조건을 바꿔 비교하는 것은 가능하나 재현 정확도는 실제 기록 대조와 사람 확인이 필요하고 물류·병원 로봇 플릿에 적용한 사례는 없다'는 추정(f4·f7·f9·f16·f23)이다. 현장 유형: 병원(f17·f18, 시뮬레이션 검증임을 명시), 제조 공장(f19·f20), 실외(f12·f13·f14, 자율주행 시험 도구임을 명시)로 물류창고·상업 시설·가정 사례는 없다. L. AI·학습 기술 관련 finding(f1·f3·f5·f22)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 적용 대상 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현 양쪽에 연결하도록 제안했고, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분은 f24 로 지켰다. 벤더 문서 출처는 이번 실행에 없다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 823건과의 URL 중복을 대조하지 못했으므로 rosbag2·Simod 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 용어집에 이미 있는 디지털 트윈·디지털 섀도·이산 사건 시뮬레이션·현실 격차·시뮬레이션 V&V·가상 시운전·프로세스 마이닝은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-29-03/verification.json

```json
{
  "run_id": "2026-09-29-03",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-836 원문 미열람(Springer 인증 리다이렉트 재현). Semantic Scholar API 초록으로 기관(Journal of Intelligent Manufacturing)·제목·발행일 2025-11-14 일치 확인. 초록에 4단계 절차, 18개 동작 유형, 응답 시간 8초~5분이 그대로 있음. 단일 출처, 저자 보고값."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2505.13761 초록 열람, 'utilizing the simulations to ground the LLMs' 구절 일치, 정량 평가 없음 확인. v2(2025-05-21) 있음."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2608.23622 초록 열람, 구조화 과제 표현→실험 설계→비교 시뮬레이션→해석→권고, 제약 공정 설계, 절제 실험, 언어 전용 대비 구체성·사용자 평가 개선 일치. ETFA 2026 채택 표기 있음. 비로봇 도메인이므로 본문에 그 점을 밝힌다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f1·f2·f3 종합 추정이며 [추정] 태그 적정. 로봇 플릿 적용 사례가 없음을 본문에 남긴다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2603.03784 초록 열람, DEVS·단계 분리·사건 트레이스 제약 대조·벤치마크 일치. v2(2026-05-21) 있음 — 각주에 판 표기."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 1910.05404 초록 열람, 로그 기반 모델 발견·하이퍼파라미터 최적화로 유사도 최대화·다도메인 평가 일치. Decision Support Systems(2020) 게재. 'Simod' 명칭은 초록에 없고 본문 도구명이므로 각주에 게재지를 병기한다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f5·f6 대응 추정, [추정] 적정."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2607.17088 초록 열람, 서브트레이스 조건부 검증·입력 고정·적합도 검정·불일치 원인 진단·M/M/1·직렬 대기행렬 일치."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f8 대응 추정, [추정] 적정. 로봇 플릿 적용 미확인을 본문에 남긴다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. rosbag2 README(github_raw) 열람, 첫 문장 인용 일치, record(-a, 토픽 필터, 압축, 분할)·play(--rate, --topics, --clock, 반복, 시작 위치 탐색)·MCAP·SQLite3 확인. 발행일 미확인(공식 저장소 문서, 확인일 기준)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. '연계 대상' 표시가 있는 [추정]으로 분류 원문 19장 경계 적용 적정."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2409.08081 초록 열람, ASE 2024, 프롬프트 추출·제약 해결·다중 지도 재구성·NHTSA·Baidu Apollo·5종 안전 위반·한계 일치. 자율주행 시험 도구이므로 5절 현장 사례가 아니라 6절 방법 선례로 다룬다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2409.06450 초록 열람, OmniTester·멀티모달 LLM·SUMO·RAG·자기 개선·사고 보고서 시나리오 재구성·현실성·제어 가능성 일치. f12 와 같이 6절 방법 선례로."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. SoVAR(난징대 등)와 OmniTester(칭화대 등) 두 초록을 각각 열어 독립 연구 그룹의 사고 보고서→시나리오 재구성 보고를 확인. 교차 확인 인정."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2607.14387 초록 열람, 123개 시나리오·컴파일 성공 76.42%·프레임워크 정확도 58.17%·반복 RAG·대화형 인터페이스·코드 공개 일치. 실제 사고 보고서 재구성은 초록에 없음(브리프 기록과 같음)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f12·f13·f15 종합 추정, [추정] 적정."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2505.06287 초록 열람, 오슬로대 저자, 형식 모델·온톨로지·SMT·평균·최악 자원 시나리오·병상 배정 일치. 병상 배정 최적화는 ROP 범위 밖 업무 계획이므로 what-if 시나리오 구성 방식 사례로만."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-837 원문 미열람(MDPI 403 재현). Semantic Scholar API 초록으로 기관(Electronics)·제목·발행일 2025-12-17 일치, 감염병 상황 간호사 추종 침대 로봇·연합 디지털 트윈·전 과정 정의·시나리오 시뮬레이션 검증 확인. 저자 한글 표기는 미확인이므로 영문 표기(Woo, J., Shin, H., Jeon, C., & Park, S.)를 쓴다. 시뮬레이션 검증 사례임을 본문에 명시."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. DBpia 페이지 열람, 한국CDE학회 논문집 26(4), 2021-12, 성균관대·LG전자 저자, 설계 단계 가상 검증·운영 단계 실시간 모니터링·국내 제조업체 AGV 적용·진단·분석·예측·최적화 일치."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분 수정 필요). ref-838 원문 미열람(Nature 인증 리다이렉트 재현). Semantic Scholar API 초록으로 Scientific Reports·제목·2026-07-18 일치, 브라운필드 혼잡·그린필드 배치·플릿 규모·역할 균형·최대 3.5배 확인. 단, 초록은 역할을 'transportation and manipulation'이라 하므로 '운송·조립'은 '운송·조작(manipulation)'으로 고친다. 실제 공장 데이터 대조 여부는 초록에 없음."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2503.02167 초록 열람, 세 과제 문구·기술–예측–처방 프레임워크·기업 디지털 트윈 시스템 시연 일치."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 분류 원문 교차 규칙 적용 판단, [추정] 적정. 영역 이름·번호 표기 정확."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 분류 원문 19장 경계 적용 추정, [추정] 적정."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 구분을 지킨 추정, [추정] 적정."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f12·f13·f14: 자율주행 사고 시나리오 재구성은 로봇 자체 지능 시험 도구이며 업종별 조건(실외 차량)에 걸치므로 5절 '실외' 적용 사례로 세우지 않고 6절 방법 선례로만 다룬다(브리프도 같은 취지로 표시)",
      "f17: 병상 배정 최적화는 상위 업무 계획(연계 영역)이므로 what-if 시나리오 구성 방식의 예시로만 쓴다",
      "f11: rosbag2 재생은 로봇 자체 지능·제어 쪽 도구로 '연계 대상' 표시 유지"
    ]
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "대상 페이지는 시드(본문 없음)이며 관련 영역 페이지(8·9·10·12·13)와 주장 중복 없음",
      "참고문헌 id 충돌 위험: 이 브리프의 ref-824~ref-830 은 같은 날 이전 실행 2026-09-29-01(ref-825 Holodeck, ref-826 Doğan 외, ref-827 모빌리오)·2026-09-29-02(ref-824 Valerio 외, ref-825 심현재 외, ref-828 Figat 외, ref-829 Howard, ref-830 폴라리스3D)가 다른 출처에 부여한 id 와 겹친다. 퍼블리셔가 URL 기준으로 새 id 를 재부여해야 한다(내용 중복은 아님)"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f20: '운송·조립 역할'을 '운송·조작(manipulation) 역할'로 고친다 — ref-838 초록이 'transportation and manipulation'이라 적고 있어 '조립'은 출처에 없다.",
    "f18: 저자를 '우지영·신효진·전창훈·박상찬'으로 쓰지 않고 영문 표기 'Woo, J., Shin, H., Jeon, C., & Park, S.'로 쓴다 — 한글 표기는 원문에서 확인되지 않았다.",
    "ref-836·ref-837·ref-838: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다 — Springer·MDPI·Nature 페이지를 열지 못했고 Semantic Scholar API 초록으로만 확인했다.",
    "f12·f13·f14: 5절 적용 사례의 '실외' 항목으로 세우지 않고 6절 대표 접근법에서 '자율주행 시험 도구의 텍스트→시나리오 재구성 선례'로 다루며, site_matrix_updates 에 실외 칸을 넣지 않는다 — 로봇 오케스트레이션 현장 사례가 아니라 차량 소프트웨어 시험 도구다. 5절은 병원(f18 을 중심 사례로, f17 은 what-if 시나리오 구성 방식 보조)과 제조 공장(f19·f20)만 현장 유형 × 여섯 항목으로 쓰고, 두 사례 모두 실제 운영 기록 재현이 아니라 시뮬레이션 검증·설계 비교 사례임을 문장에 밝힌다.",
    "f3: 본문에서 적용 대상이 제약 공정 설계(비로봇 도메인)임을 문장에 밝히고 에이전트 비교 실험 방법의 선례로만 쓴다 — 로봇 플릿 적용 근거가 아니다.",
    "f17: 병상 배정 최적화 자체는 분류 원문 19장의 상위 업무 시스템 연계 영역이므로 ROP 기능처럼 서술하지 않고 '평균·최악 자원 시나리오를 설정으로 만드는 방식'의 예시로만 쓴다.",
    "f6·ref-828: 각주에 게재지 'Decision Support Systems (2020)'를 병기하고 본문에서 Simod 라는 도구명을 쓸 때 초록이 아니라 논문 본문의 도구명임을 각주 요약에 남긴다.",
    "ref-824·ref-825: 각주 발행일에 판을 표기한다(ref-824 '2025-05-19 (v1; v2 2025-05-21)', ref-825 '2026-03-04 (v1; v2 2026-05-21)') — 더 새 판이 있으므로 기준일·버전을 명시한다.",
    "f1·f9·f4: 본문에 '로봇 플릿 운영 기록을 대화로 재현한 현장 사례는 이번 조사에서 확인되지 않았다'는 한계를 3절 또는 11절에 한 문장으로 남긴다 — 브리프 self_check 의 미확인 항목이며 독자가 알아야 할 한계다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 0건, 교차 확인 1건(f14: SoVAR·OmniTester 독립 연구 그룹). 강등: 없음. 원문 미열람 출처: ref-836, ref-837, ref-838(발행사 페이지 접근 차단, Semantic Scholar API 초록으로 기관·제목·발행일 일치 확인). 주의: 모든 사실 주장은 논문 초록·공식 저장소 README 확인에 근거한 단일 출처이며 정량 수치(f1 응답 시간, f15 정확도, f20 3.5배)는 저자 보고값이다. 대화만으로 로봇 플릿의 실제 운영 기록을 시뮬레이션에 재현한 현장 사례는 확인되지 않았고, 현장 사례는 병원·제조 공장의 시뮬레이션 검증·설계 비교 사례뿐이다. 자율주행 사고 재구성(f12~f14)은 현장 사례가 아닌 방법 선례로만 쓴다. f20 의 '조립'은 출처의 'manipulation'과 달라 수정을 지시했다. 참고문헌 id ref-824~ref-830 은 같은 날 이전 실행(2026-09-29-01·-02)이 다른 출처에 부여한 id 와 겹칠 수 있으므로 퍼블리셔가 URL 기준으로 재부여해야 한다. 검증에 검색은 쓰지 않았고 WebFetch 열람 18회(출처당 2회 이내)로 확인했다. 정정 요청 없음.",
  "retry_reason": null
}
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 11
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현

# 11. 채팅으로 실제 상황 시뮬레이션 재현

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]

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

### docs/categories/chat-based-configuration-and-operation/index.md

```markdown
---
title: "C. 채팅 기반 구성·운영"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › C. 채팅 기반 구성·운영

# C. 채팅 기반 구성·운영

## 핵심 질문

맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

## 개요

채팅으로 맵을 그리고, 시나리오를 구성하고, 로봇을 구성하고, 실제 상황을 시뮬레이션으로 재현하고, 업무를 지시·관리하는 대화형 기능 전체와 그 신뢰 기반. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **8. 채팅으로 맵 작성** | 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 | 공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? | [8. 채팅으로 맵 작성](chat-map-authoring.md) | published |
| **9. 채팅으로 시나리오 구성** | 대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 | 할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? | [9. 채팅으로 시나리오 구성](chat-scenario-composition.md) | seed |
| **10. 채팅으로 로봇 구성** | 대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 | 어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? | [10. 채팅으로 로봇 구성](chat-robot-configuration.md) | published |
| **11. 채팅으로 실제 상황 시뮬레이션 재현** | 실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 | 실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? | [11. 채팅으로 실제 상황 시뮬레이션 재현](chat-real-situation-simulation-replay.md) | seed |
| **12. 채팅으로 업무 지시·오케스트레이션** | 대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 | 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? | [12. 채팅으로 업무 지시·오케스트레이션](chat-task-instruction-and-orchestration.md) | seed |
| **13. 대화형 기능의 신뢰·기반** | 오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 | 언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? | [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

대화 결과는 실행 명령이 아니라 계획이다. **사람이 확인·승인한 계획만 실행**되어야 언어 모델의 잘못된 해석이 로봇 동작으로 이어지지 않는다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 31건이다(논문 23건 · 기사·보고서 0건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 6건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-819](../../references/ref-819.md) — Valerio, D., Kogler, P., Bischof, S., Hubauer, T., & Rangwala, H., Neuro-symbolic AI for Industrial Configuration (발행 2026-09-24)
- [ref-759](../../references/ref-759.md) — Ko, T.-H., & Lin, C.-T.(National Central University), Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin (발행 2026-09)
- [ref-822](../../references/ref-822.md) — Howard, T. L. (California Polytechnic State University, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities (발행 2026-06)
- [ref-674](../../references/ref-674.md) — Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH), Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins (발행 2026-06)
- [ref-201](../../references/ref-201.md) — Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A., From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation (발행 2026-06)
- [ref-813](../../references/ref-813.md) — Qin, S., Weber, R. E., & Lu, X., Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans (발행 2026-03-12)
- [ref-821](../../references/ref-821.md) — Figat, M., Mackey, R. M., & Ingham, M. D., Ontology-Driven Robotic Specification Synthesis (발행 2026-02-05)
- [ref-163](../../references/ref-163.md) — 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (발행 2026)
- [ref-786](../../references/ref-786.md) — Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models (발행 2025-11-05)
- [ref-677](../../references/ref-677.md) — CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재), LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning (발행 2025-11)
- 그 밖에 13건

**기사·보고서**

- 아직 없음

**업체 발표**

- [ref-817](../../references/ref-817.md) — 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 (발행 2026-08-24)
- [ref-823](../../references/ref-823.md) — 폴라리스3D(Polaris3D), AMR 도입 ROI 어떻게 계산할까? 물류 자동화 투자 회수 기간 알아보기 (발행 2026-06-12)

**표준·오픈소스·기관 자료**

- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-229](../../references/ref-229.md) — IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) (발행 미확인)
- [ref-105](../../references/ref-105.md) — Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml (발행 미확인)
- [ref-104](../../references/ref-104.md) — Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README) (발행 미확인)
- [ref-079](../../references/ref-079.md) — Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2 (발행 미확인)
- [ref-031](../../references/ref-031.md) — VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 (발행 미확인)
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [10. 채팅으로 로봇 구성](chat-robot-configuration.md) — 3~11절 신규 작성(seed → draft), 출처 16건, 현장 유형 사례 3건(물류창고·제조 공장·병원), 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 지시 10건 이행. 2차 재검증 수정: 5절 물류창고 사례 표 시작 조건 칸의 첫 등장 '대수 산정'을 용어집 표기·링크로 고침 (실행 2026-09-29-02)
- 2026-09-29 · 생성 · [10. 채팅으로 로봇 구성 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area10-s6.md) — 자동 분리: 10. 채팅으로 로봇 구성 의 "6. 대표 접근법과 기술" 절(2,293자)을 옮겼다(2차 재검증에서 변경 없음) (실행 2026-09-29-02)
- 2026-09-29 · 생성 · [10. 채팅으로 로봇 구성 — 대표 연구와 자료](../../topics/2026/2026-09-29-area10-s8.md) — 자동 분리: 10. 채팅으로 로봇 구성 의 "8. 대표 연구와 자료" 절(1,679자)을 옮겼다(2차 재검증에서 변경 없음) (실행 2026-09-29-02)
- 2026-09-29 · 생성 · [10. 채팅으로 로봇 구성 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area10-s4.md) — 자동 분리: 10. 채팅으로 로봇 구성 의 "4. 핵심 개념과 용어" 절(1,394자)을 옮겼다(2차 재검증에서 변경 없음) (실행 2026-09-29-02)
- 2026-09-29 · 생성 · [10. 채팅으로 로봇 구성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area10-s10.md) — 자동 분리: 10. 채팅으로 로봇 구성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,016자)을 옮겼다. 2차 재검증 수정: 20. 로봇·제조사 관제 연동 항목과 25. 작업 배정 — MRTA 항목의 태그를 [사실]에서 [추정]으로 되돌림 (실행 2026-09-29-02)
<!-- auto:category-recent:end -->
```

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "17. 작업 대상·자산 식별과 인계 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
area_no: {{area_no}}                        # 1~67 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [18, 29, 30]. 없으면 []
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
경로: docs/categories/<대분류 slug>/<영역 slug>.md  (아래 경로 규약 표. 2026-09-28 개정부터 폴더·파일 이름에 대분류 문자·영역 번호를 붙이지 않는다)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석, C. 채팅 기반 구성·운영의 엔진 짝 주석), 1절 아래 "이 영역이 다루는 일(2026-09-28 리스트업 기준)" 목록(data/area_items.json)과 옛 영역에서 이어받은 경우의 계보 안내(data/area_lineage.json)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/<트랙 slug>/index.md(예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition) 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 67페이지(예: docs/categories/robot-ontology/robot-capability-and-task-representation.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 로봇 온톨로지):
!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 67페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]

{{area_items_block}}
<!--
첫 내용 줄: 분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않는다. 원문 주석(현재 원문)은 이 절이 아니라 2절의 인용 블록에 둔다.
{{area_items_block}}: 시드가 넣은 위키 문구를 그대로 둔다(pipeline/scaffold.py area_items_block). (1) "이 영역이 다루는 일(2026-09-28 리스트업 기준):" 과 그 아래 "- **일 이름**: 정의" 목록(data/area_items.json), (2) 옛 영역에서 일부를 이어받은 영역이면 계보 안내 문장(data/area_lineage.json), (3) 옛 영역 본문을 이어받은 영역이면 옛 영역 안내 문장과 옛 정의·질문·주석 인용 블록("> 옛 정의: … [옛 분류원문]", "> 옛 질문: … [옛 분류원문]", "> 옛 원문 주석: … [옛 분류원문]"). 옛 인용 블록은 보관한 옛 원문(_source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)과 글자 단위로 같아야 하며(protect_source.py check_tagged_lines), 이력 기록이므로 에이전트가 고치거나 새 문장을 [옛 분류원문] 으로 태그하지 않는다. 해당 내용이 없는 영역은 이 자리 표시 줄을 지운다.
이 절의 원문 문장과 옛 원문 인용은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. 핵심 질문

{{core_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 세부영역 표의 "핵심 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]". 수정 금지. (대분류 페이지의 핵심 질문과 다른 문장이다. 소속 대분류의 핵심 질문은 H1 아래 admonition 에 둔다.)
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 해당 영역(2026-09-28 원문 기준): 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 36. 가상 시운전·실제 상황 재현, 38. 모니터링·이상 탐지·원인 분석, 55. 현장 조사·설치·시운전. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14~16번의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석("매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번"), C. 채팅 기반 구성·운영의 엔진 짝 주석("맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번").
굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다. 문단이 여럿인 영역(예: 14. 도면·BIM에서 지도 만들기는 셋, 15. 지도·공간·위치 모델과 25. 작업 배정 — MRTA는 둘)은 인용 블록도 원문 순서대로 그 수만큼 둔다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다. 정확한 목록은 pipeline/lib/source.py 의 area_notes(번호)가 정한다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 ROP를 구현·운영할 때 무엇이 막히는지, 로봇 개별 성능과 업무 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 핵심 질문에서 출발한다. 특정 현장 유형(예: 물류창고)에만 해당하는 이야기로 좁히지 말고, 현장 유형에 따라 달라지는 점이 있으면 어느 현장 유형인지 밝힌다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "VDA 5050(독일자동차산업협회 무인운반차 인터페이스)", "WMS(Warehouse Management System, 창고 관리 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** {{site_types}}
<!-- 이 사례가 놓이는 현장 유형을 분류 원문 21장의 일곱 가지(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 가운데 하나로 명시한다. 예: "병원". 물류창고는 일곱 현장 유형 가운데 하나일 뿐이므로 기본값으로 쓰지 않고, 브리프 근거가 있는 현장 유형을 고른다. 물류창고 사례라면 입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 중 어느 단계인지를 사례 제목이나 서술에 덧붙일 수 있다. -->

**사례:** {{case_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "병원에서 검체를 검사실로 운반", "제조 공장에서 공정 사이 부품 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
여섯 항목은 분류 원문 21장의 정의를 따른다. 시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가? / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가? / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가? / 제약: 시간·공간·적재량·설비·권한·안전 제약은 무엇인가? / 완료·인계: 무엇이 확인돼야 일이 끝났다고 인정하는가? / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?
표 아래에 1~3단락으로 사례를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 실제 도입 사례는 출처 각주와 함께 쓰고, 설명용 가상 사례이면 첫 문장에 밝힌다(예: "다음은 설명을 위한 가상의 사례이다."). 지어낸 현장 수치는 쓰지 않는다.
사례가 여럿이면 "**현장 유형:** … / **사례:** … / 여섯 항목 표 / 서술" 묶음을 사례마다 반복한다(서로 다른 현장 유형의 사례를 우선한다). 2026-09-28 개정 전에 쓴 물류창고 시나리오는 "현장 유형: 물류창고" 사례로 유지한다.
다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 함께 낸다(항목마다 site_type·item·link·title. 대분류는 퍼블리셔가 link 에서 정한다). 현장 유형 매트릭스 페이지: ../../site-matrix.md
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

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 현장 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 19장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장"(같은 대분류 E. 사물·사람·실시간 상태 안의 예). 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 L. AI·학습 기술의 해당 영역(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)을 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 영역이면 짝이 되는 엔진 영역(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 연결한다. 현장 유형별 요구·도입 사례는 Q. 현장 유형별 적용의 해당 영역(61. 물류창고 ~ 67. 기타 현장)을 연결한다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/<트랙 slug>/index.md. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/<트랙 slug>/question-backlog.md)로 링크만 둔다.
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
title: "{{category}}"                       # 원문 명칭 그대로. 예: "B. 로봇 온톨로지"
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
쓰임: 구축 시 원문 부분(핵심 질문·개요·세부 연구영역·이 대분류의 핵심 포인트)을 채워 만든다. "다른 대분류와의 연결"은 에이전트(스토리텔러)가 관련 영역을 다루는 실행에서 채우고, "세부 연구영역" 표(페이지·현재 상태 열 포함)와 "이 대분류의 자료"(논문·기사·업체 발표·표준 묶음별 출처 목록, 2026-09-28 추가), "최근 업데이트"는 퍼블리셔가 자동 갱신한다.
일곱 섹션(4.3 + 2026-09-28 추가): 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 이 대분류의 자료 / 최근 업데이트. 제목·순서 고정. H2 문자열은 사양서 4.3 문구 그대로이며 번호를 붙이지 않는다(pipeline/checks/protect_source.py 의 CATEGORY_SECTIONS 와 글자 단위로 같다. "1. 핵심 질문"처럼 번호를 붙이면 "섹션 제목·순서 불일치"로 반려된다). 각주 정의를 둘 자리로 번호 없는 "참고 자료" 절을 여섯 섹션 뒤에 하나 더 두었다. 이 절은 사양서 4.3 의 여섯 섹션에 없는 구축자 추가 절이다 [가정].

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 같은 대분류의 세부영역은 <파일>.md, 다른 대분류는 ../<대분류 slug>/index.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › {{category}}

# {{category}}

## 핵심 질문

{{core_question}} [분류원문]
<!-- 분류 원문 1장 표의 "핵심 질문" 칸 문장 그대로. 예: "서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]". 수정 금지. -->

## 개요

{{overview_paragraph}} [분류원문]
<!-- 분류 원문에서 이 대분류 장의 첫 문단(표 위의 문단)을 굵게 표기까지 그대로 옮긴다. 예: "서로 다른 제조사의 로봇을 등록하고, 무엇을 할 수 있는지 공통 모델로 표현하고, 그 모델로 시스템과 로봇이 쉽게 연동되게 하는 온톨로지 기능 전체. [분류원문]". 굵은 표기가 있으면 그대로 두고, 명사형으로 끝나는 문단도 고치지 않는다. -->

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |

[분류원문]
<!-- auto:category-area-table:end -->
<!--
원문 표의 행(대분류마다 3~7행)을 모두 그대로 옮기고(앞 3열은 원문 셀과 글자 단위로 같게, 첫 열의 굵은 표기 유지, 첫 열에 링크를 씌우지 않음), "페이지" 열에 세부영역 페이지 링크, "현재 상태" 열에 해당 페이지 프런트매터 status(seed | draft | verified | published | needs_update | deprecated)를 둔다(4.3 의 "링크와 현재 상태 열만 추가"). 표 바로 아래 빈 줄 다음에 [분류원문] 한 줄을 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_category)가 각 행의 앞 3칸과 [분류원문] 줄을 원문과 대조한다.
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
에이전트가 채운다. 목록 형식: "- [F. 연동](../integration/index.md) — 이 대분류의 어떤 영역이 저 대분류의 어떤 영역과 왜 이어지는지 한두 문장(세부영역은 번호와 이름 함께)". 주장에는 태그·각주. 구축 시에는 "아직 작성되지 않음"으로 둔다.
M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회처럼 여러 대분류에 걸쳐 적용되는 대분류는 그 적용 관계를 드러낸다. Q. 현장 유형별 적용은 현장마다 다른 요구를 모으고 모든 현장에 공통인 기능은 A~P에 둔다는 원문 취지를 지킨다. L. AI·학습 기술의 교차 규칙(매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석)과 C. 채팅 기반 구성·운영의 엔진 짝(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 여기서도 지킨다.
-->

## 이 대분류의 자료

<!-- auto:category-sources:start -->
(퍼블리셔가 자동 생성: 이 대분류 페이지·소속 세부영역·주제 페이지가 인용한 출처를 논문 / 기사·보고서 / 업체 발표(벤더 문서) / 표준·오픈소스·기관 자료로 묶어 최근 발행순으로 보인다)
<!-- auto:category-sources:end -->

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 823건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 211개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automation-bias: 자동화 편향 (Automation Bias)
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
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
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
- edit-cost: 편집 비용 (Edit Cost)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
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
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
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
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
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
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
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
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
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

### docs/open-questions.md (요약: 대상 영역 [11] 에 걸린 0건 / 전체 130건)

```markdown
없음
```

### docs/standards/index.md (요약: 210개 — 이름 · 종류 · 발행 기관)

```markdown
- SCOR (SCOR Digital Standard) · 표준 · ASCM(Association for Supply Chain Management)
- ISA-95 (ANSI/ISA-95) · 표준 · ISA(International Society of Automation)
- GS1 EPCIS · 표준 · GS1
- Open-RMF · 오픈소스 · Open Robotics
- ROS 2 DDS-Security (ROS 2 DDS-Security Integration) · 프레임워크 · ROS 2 Design
- ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) · 프레임워크 · ROS 2 Design
- NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) · 평가 프로그램 · NIST(National Institute of Standards and Technology)
- ARIAC · 평가 프로그램 · NIST
- GS1 EPCIS 2.0 (ISO/IEC 19987:2024) · ISO/IEC · GS1 · 표준
- GS1 CBV (Core Business Vocabulary) · GS1 · 표준
- SSCC (Serial Shipping Container Code) · GS1 · 표준
- GS1 Logistic Label Guideline · GS1 · 표준
- GRAI (Global Returnable Asset Identifier) · GS1 · 표준
- GIAI (Global Individual Asset Identifier) · GS1 · 표준
- EPC Tag Data Standard (1.11판) · GS1 · 표준
- VDA 5050 (2.0.0) · VDA(Verband der Automobilindustrie) · 표준
- OpenEPCIS · OpenEPCIS · 오픈소스
- IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) · IEEE · 표준
- IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology · IEEE · 표준
- W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) · W3C / OGC · 표준
- VDA 5050 (3.0.0) · VDA(Verband der Automobilindustrie) · 표준
- MassRobotics AMR Interoperability Standard (1.0) · MassRobotics · 표준
- OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) · OPC Foundation / VDMA · 표준
- Information Model for Capabilities, Skills & Services (CSS) · Plattform Industrie 4.0 · 프레임워크
- Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) · Auto-ID Labs Korea(세종대학교) · 오픈소스
- RAWSim-O · Merschformann, M. (RAWSim-O GitHub) · 오픈소스
- 스마트물류센터 인증제 · 한국교통연구원(인증스마트물류센터) · 평가 프로그램
- BPMN 2.0 (ISO/IEC 19510:2013) · OMG(Object Management Group) · ISO/IEC · 표준
- IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 · IEC / ISO · 표준
- B2MML (Business To Manufacturing Markup Language, 판 0701) · MESA International · 표준
- OCEL 2.0 (Object-Centric Event Log) · arXiv:2403.01975 저자(미확인) · 표준
- ISO 22400-2:2014 제조 운영 관리 KPI 정의 · ISO · 표준
- WERC DC Measures · WERC(Warehousing Education and Research Council) · 평가 프로그램
- PM4Py · Process Intelligence Solutions · 오픈소스
- OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) · OPC Foundation / ISA · 표준
- osmAG-from-cad (CAD-to-osmAG 파이프라인) · Zhang, J. (jiajiezhang7 GitHub) · 오픈소스
- Ogm2Pgbm · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- ifc2indoorgml · Diakité, A. A. 외 · 오픈소스
- IDTA 02020 Capability Description 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- CaSkMan · CaSkade-Automation (GitHub) · 오픈소스
- SOMA (Socio-physical Model of Activities) · EASE CRC · 오픈소스
- IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) · Helmut Schmidt University, Institute of Automation Technology · 오픈소스
- ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 · ISO · 표준
- KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- VDMA LIF (Layout Interchange Format) · VDMA · 표준
- IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) · buildingSMART · 표준
- Nav2 Docking Framework (nav2_docking) · ROS Navigation (Open Navigation) · 오픈소스
- IDTA 02020 Capability Description (AAS 서브모델 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 · ISO · 표준
- KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- SkiROS2 · RVMI lab, Aalborg University · 오픈소스
- LIF (Layout Interchange Format) 1.0.0 · VDMA · 표준
- ISO 21423 Industrial mobile robots — Communications and interoperability · ISO · 표준
- IFC 4.3 (IfcSpace) · buildingSMART International · 표준
- OGC IndoorGML 2.0 · OGC · 표준
- ISO 19164:2024 Indoor feature model · ISO · 표준
- GS1 GLN (Global Location Number) · GS1 · 표준
- REP 105 Coordinate Frames for Mobile Platforms · ROS (ros-infrastructure/rep) · 프레임워크
- ROSA (ROS Agent) · NASA Jet Propulsion Laboratory · 오픈소스
- RAI · Robotec.ai · 오픈소스
- free_fleet (Open-RMF 플릿 어댑터) · Open Robotics (open-rmf) · 오픈소스
- ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) · InOrbit · 오픈소스
- Open-RMF fleet_adapter_template · Open Robotics (open-rmf) · 오픈소스
- SLAM Toolbox · Macenski, S. (SteveMacenski GitHub) · 오픈소스
- ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) · Open Robotics (ROS 2 Documentation) · 오픈소스
- Eclipse Sparkplug (Chapter 5 Operational Behavior) · Eclipse Foundation · 표준
- OPC UA Part 4: Services (7.11 DataValue) · OPC Foundation · 표준
- ISO 23247 제조 디지털 트윈 프레임워크 · ISO (NIST 해설 경유) · 표준
- ROS 2 설계 문서 — ROS on DDS · QoS 정책 · ROS 2 Design · 프레임워크
- rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) · ROS 2 (ros2/rmw_zenoh) · 오픈소스
- KubeEdge · KubeEdge (CNCF) · 오픈소스
- Open-RMF rmf-web (대시보드·API 서버) · Open Robotics (open-rmf) · 오픈소스
- MQTT Version 5.0 · OASIS · 표준
- NIST SP 500-325 Fog Computing Conceptual Model · NIST · 프레임워크
- KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 · 산업통상자원부 국가기술표준원 · 표준
- Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) · Open Robotics (open-rmf) · 오픈소스
- KnowRob (하이브리드 지식 베이스) · KnowRob (knowrob GitHub) · 오픈소스
- IEEE1872-owl (CORA 공개 OWL 번역, 제3자) · srfiorini (IEEE1872-owl GitHub) · 오픈소스
- CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) · OGC · 표준
- IMDF (Indoor Mapping Data Format) 1.0.0 · OGC / Apple · 표준
- BOT (Building Topology Ontology) 0.3.2 · W3C Linked Building Data Community Group · 프레임워크
- ifcOWL · buildingSMART · 표준
- Brick Schema · Brick Consortium · 오픈소스
- ISO 16739-1:2024 (IFC 4.3) · ISO · 표준
- Rasa 폼(Forms, Rasa 3.x) · Rasa Technologies · 오픈소스
- ROS 2 액션 설계(Actions) · ROS 2 Design · 프레임워크
- ROS 2 관리형 노드 수명주기(Managed nodes) · ROS 2 Design · 프레임워크
- Open-RMF rmf_task · Open Robotics (open-rmf) · 오픈소스
- IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) · IETF HTTPAPI Working Group · 표준
- OPC UA Part 10: Programs (v1.04) · OPC Foundation · 표준
- ISA-TR88.00.02 Machine and Unit States (PackML) · ISA · 표준
- BehaviorTree.CPP · BehaviorTree (GitHub) · 오픈소스
- OR-Tools CP-SAT (스케줄링 레시피) · Google · 오픈소스
- Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) · Open Robotics (open-rmf) · 오픈소스
- rmf_task (Open-RMF 작업 계획기 TaskPlanner) · Open Robotics (open-rmf) · 오픈소스
- ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 · ISO · 표준
- 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) · National Institute of Building Sciences · 표준
- KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 · 국가표준인증통합정보시스템(KSSN) · 표준
- 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) · 한국건설기술연구원(건설CALS 체계) · 표준
- ezdxf (DXF 읽기·쓰기 라이브러리) · Moitzi, M. (mozman/ezdxf GitHub) · 오픈소스
- ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) · ECLASS e.V. · 표준
- IEC 공통 데이터 사전(IEC CDD) · IEC · 표준
- rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF Traffic Editor · Open Robotics · 오픈소스
- MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) · DiligentPanda (Team Pikachu, GitHub) · 오픈소스
- SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface · SEMI · 표준
- ASTM F3499-21 A-UGV 도킹 성능 시험 방법 · ASTM International · 표준
- ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 · ANSI / A3 · 표준
- KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 · 국가표준인증통합정보시스템(KSSN) · 표준
- Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_reservation (실험적 예약 라이브러리) · Open Robotics (open-rmf) · 오픈소스
- ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 · ISO · 표준
- ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) · ISO (A3 해설 경유) · 표준
- ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 · A3(Association for Advancing Automation) · 표준
- 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 · 고용노동부·한국산업안전보건공단 · 프레임워크
- 이동식 협동로봇 안전기준 KS(표준 번호 미확인) · 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) · 표준
- Open-RMF rmf_demos · Open Robotics (open-rmf) · 오픈소스
- IEC 61360-7:2024 교차 도메인 개념 데이터 사전(General items) · IEC · 표준
- IDTA 02003 Generic Frame for Technical Data for Industrial Equipment in Manufacturing (1.2) · IDTA(Industrial Digital Twin Association) · 표준
- Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- ROS 2 diagnostics · ROS (ros/diagnostics GitHub) · 오픈소스
- ros2_tracing · ROS 2 (ros2/ros2_tracing GitHub) · 오픈소스
- OpenTelemetry Specification · OpenTelemetry (CNCF) · 오픈소스
- Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 경보 메시지(rmf_task_msgs Alert) · Open Robotics (open-rmf) · 오픈소스
- IFCtoLBD (IFC → 링크드 빌딩 데이터 변환기, 판 2.54.0) · Oraskari, J. (jyrkioraskari GitHub) · 오픈소스
- SHACL (Shapes Constraint Language) · W3C · 표준
- IDS (Information Delivery Specification) · buildingSMART · 표준
- RMF Site Editor (rmf_site) · Open Robotics (open-rmf) · 오픈소스
- ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도) · ISO · 표준
- 기업재난관리표준·재해경감 우수기업 인증제 · 행정안전부 · 평가 프로그램
- 중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022) · 고용노동부 · 프레임워크
- 보상 트랜잭션 패턴(Compensating Transaction pattern) · Microsoft (Azure Architecture Center) · 프레임워크
- Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle) · Open Robotics (open-rmf) · 오픈소스
- IEEE 1872.1-2024 Standard for Robot Task Representation · IEEE Standards Association · 표준
- Serverless Workflow (Open Workflow Specification) DSL · CNCF Serverless Workflow · 오픈소스
- HDDL (Hierarchical Domain Definition Language) · Höller 외(IPC 2020 계층 계획 부문) · 프레임워크
- FaMe (BPMN 기반 다중 로봇 시스템 개발 틀) · Pettinari, S. (UNICAM PROS) · 오픈소스
- ISO 20607:2019 기계 안전 — 설명서 일반 작성 원칙 · ISO · 표준
- IEC/IEEE 82079-1:2019 제품 사용 정보 작성 — Part 1: 원칙과 일반 요구사항 · IEC / IEEE / ISO · 표준
- OmniDocBench (PDF 문서 파싱 벤치마크) · OpenDataLab · 오픈소스
- ISO 23247-6:2026 제조 디지털 트윈 프레임워크 — 제6부: 디지털 트윈 결합 · ISO · 표준
- KS X ISO 23247 제조를 위한 디지털 트윈 프레임워크(제1부 개요 및 일반 원리 등) · 국가표준인증종합정보센터(KSSN) · 표준
- Open-RMF rmf_simulation (시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- OFacT (Open Factory Twin) · OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) · 오픈소스
- League of Robot Runners · League of Robot Runners (Amazon Robotics 후원) · 평가 프로그램
- ASTM F45 위원회(무인 자동 유도 산업 차량) · ASTM International (NIST 참여) · 표준
- KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력 · 국가표준인증종합정보센터(KSSN) · 표준
- 한국로봇산업진흥원 로봇 시험평가 · 한국로봇산업진흥원(KIRIA) · 평가 프로그램
- ros2_fault_injection · reeceholland (GitHub) · 오픈소스
- ROSMonitoring · University of Liverpool Autonomy and Verification · 오픈소스
- LSMART (Lifelong Scalable Multi-Agent Realistic Testbed) · Yan, J. 외(arXiv 2602.15721) · 오픈소스
- IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 17359:2018 기계 상태 감시·진단 일반 지침 · ISO · 표준
- ISO 55000:2024 자산 관리 — 용어·개요·원칙 · ISO (ISO/TC 251) · 표준
- IEC TR 62443-2-3:2015 IACS 환경의 패치 관리 · IEC · 표준
- REP 2000 ROS 2 Releases and Target Platforms · Open Robotics (ROS REP) · 프레임워크
- rmf_simulation (Open-RMF 시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- 협동로봇 설치 작업장 안전인증 · 한국로봇사용자협회 · 평가 프로그램
- ISO 12100:2010 기계 안전 — 설계 일반 원칙 — 위험성평가와 위험 감소 · ISO (CEN EN ISO 12100:2010) · 표준
- KS B ISO/TS 15066 로봇 및 로봇 장치 — 협동로봇 · 국가기술표준원(KSSN) · 표준
- Nav2 Route Server (nav2_route) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- NIST SP 800-82 Rev. 3 Guide to Operational Technology (OT) Security · NIST · 프레임워크
- Eclipse Mosquitto (MQTT 브로커, mosquitto.conf ACL·인증서 인증) · Eclipse Foundation · 오픈소스
- SROS 2 접근 제어 정책(ROS 2 Access Control Policies) · ROS 2 Design · 프레임워크
- ROS 2 보안 인클레이브(ROS 2 Security Enclaves) · ROS 2 Design · 프레임워크
- KISA 로봇 보안취약점 점검 체크리스트 해설서 · 한국인터넷진흥원(KISA) · 프레임워크
- NIST AI RMF 1.0 (NIST AI 100-1) · NIST · 프레임워크
- ISO/IEC 42001:2023 AI 관리 시스템 · ISO/IEC · 표준
- ISO/IEC 23894:2023 AI 위험관리 지침 · ISO/IEC · 표준
- MLflow 모델 레지스트리 · MLflow (Linux Foundation 오픈소스 프로젝트) · 오픈소스
- LoTa-Bench · lbaa2022 (LoTa-Bench 공식 저장소) · 오픈소스
- AmbiK 데이터셋 · cog-model (AmbiK 저자) · 오픈소스
- SISO CMSD (Core Manufacturing Simulation Data, SISO-STD-008-2010·SISO-STD-008-01-2012) · SISO(Simulation Interoperability Standards Organization) · 표준
- SLAPStack (블록 적재 창고 저장 위치 배정 시뮬레이션) · Rinciog, A. 외 (malerinc/slapstack GitHub) · 오픈소스
- Semantic Versioning 2.0.0 · Semantic Versioning (semver.org) · 프레임워크
- IETF RFC 9745 The Deprecation HTTP Response Header Field · IETF · 표준
- IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준 · IEC · 표준
- ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항 · ISO/IEC · 표준
- KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 · 한국지능형로봇표준포럼(KOROS) · 표준
- OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증) · OPC Foundation · 평가 프로그램
- Nav2 costmap_2d (비용 지도·비용 지도 필터: 금지 구역·속도 제한) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- SLAM2REF (라이다 데이터의 기준 지도 다중 세션 정렬 도구) · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- Open-RMF rmf_task_ros2 디스패처·입찰 경매자(평가기) · Open Robotics (open-rmf) · 오픈소스
- Rasa 폴백·사람 인계(Fallback and Human Handoff, Rasa 3.x) · Rasa Technologies · 오픈소스
- nudged (2D 유사 변환 추정 라이브러리) · Palonen, A. (axelpale/nudged GitHub) · 오픈소스
- Rasa CALM 대화 복구 패턴(rasa-calm-demo patterns.yml) · Rasa Technologies · 오픈소스
- IfcDiff (IfcOpenShell IFC 모델 비교 도구, v0.8.0 문서) · IfcOpenShell · 오픈소스
- BS EN ISO 19650 Guidance Part C: 공통 데이터 환경(Edition 1) · UK BIM Framework · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency) · OWASP · 프레임워크
- Model Context Protocol 명세 2025-06-18 (Server Features: Tools) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- LangChain Human-in-the-loop 미들웨어 · LangChain · 오픈소스
- ISO 18646-2:2024 서비스 로봇 성능 기준과 시험 방법 — Part 2: 주행 · ISO · 표준
- ASTM F3244 Standard Test Method for Navigation: Defined Area · ASTM International · 표준
- SSIG (평면도 구조 유사도 지표) · van Engelenburg, C. 외 (caspervanengelenburg GitHub) · 오픈소스
- SLABIM (SLAM–BIM 결합 데이터셋) · HKUST Aerial Robotics Group · 오픈소스
- vda5050-sim (VDA 5050 가상 로봇 플릿 시뮬레이터) · gpue (vda5050-sim GitHub, 개인 저장소) · 오픈소스
- vda-5050-lib.js (가상 AGV 어댑터 포함 VDA 5050 라이브러리) · coatyio · 오픈소스
- τ-bench (도구–에이전트–사용자 상호작용 벤치마크) · sierra-research · 평가 프로그램
- SafeAgentBench (LLM 체화 에이전트 안전 계획 벤치마크) · SafeAgentBench 저자(shengyin1224 공식 저장소) · 평가 프로그램
- JSON Schema Validation (json-schema-spec, main 브랜치 차기판 초안) · JSON Schema (json-schema-org) · 표준
- VAL (PDDL 계획 검증 도구) · KCL-Planning · 오픈소스
- JSONSchemaBench · guidance-ai · 오픈소스
- Model Context Protocol 명세 2025-06-18 (Basic: Authorization) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- NIST SP 800-162 속성 기반 접근 통제(ABAC) 정의와 고려 사항 · NIST · 프레임워크
- RobotFleet (LLM·MILP 작업 배정기를 둔 중앙 다중 로봇 계획 틀) · therohangupta (RobotFleet 공식 저장소) · 오픈소스
```

### runs/2026-09-29-03/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/simulator.md
about/what-is-rop.md
categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md
categories/ai-and-learning/document-drawing-and-scene-understanding.md
categories/ai-and-learning/index.md
categories/ai-and-learning/prediction-and-learning-based-optimization.md
categories/ai-and-learning/robot-foundation-models-and-llm-planning.md
categories/chat-based-configuration-and-operation/chat-map-authoring.md
categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md
categories/chat-based-configuration-and-operation/chat-robot-configuration.md
categories/chat-based-configuration-and-operation/chat-scenario-composition.md
categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md
categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md
categories/chat-based-configuration-and-operation/index.md
categories/design-and-simulation/capacity-sizing-and-layout-design.md
categories/design-and-simulation/index.md
categories/design-and-simulation/scenario-model-and-editing.md
categories/design-and-simulation/simulation-and-predictive-digital-twin.md
categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md
categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md
categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md
categories/execution-collaboration-and-recovery/human-robot-collaboration.md
categories/execution-collaboration-and-recovery/index.md
categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md
categories/field-operations-and-monitoring/control-screen-and-execution-records.md
categories/field-operations-and-monitoring/index.md
categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md
categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md
categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md
categories/governance-law-and-society/index.md
categories/governance-law-and-society/labor-acceptance-and-accessibility.md
categories/governance-law-and-society/law-regulation-insurance-and-licensing.md
categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md
categories/integration/business-system-integration.md
categories/integration/facility-and-building-system-integration.md
categories/integration/index.md
categories/integration/interoperability-standards-and-conformance.md
categories/integration/robot-and-vendor-fleet-manager-integration.md
categories/objects-people-and-live-state/index.md
categories/objects-people-and-live-state/people-and-pedestrian-model.md
categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md
categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md
categories/planning-and-business/economics-procurement-and-business-models.md
categories/planning-and-business/index.md
categories/planning-and-business/technology-market-and-vendor-trends.md
categories/planning-and-business/use-cases-requirements-and-scope.md
categories/planning-and-optimization/index.md
categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md
categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md
categories/planning-and-optimization/task-allocation-mrta.md
categories/planning-and-optimization/task-and-workflow-modeling.md
categories/planning-and-optimization/task-sequencing-and-scheduling.md
categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md
categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md
categories/platform-architecture-and-infrastructure/index.md
categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md
categories/robot-ontology/heterogeneous-robot-registration.md
categories/robot-ontology/index.md
categories/robot-ontology/ontology-based-system-and-robot-integration.md
categories/robot-ontology/ontology-verification-and-change-management.md
categories/robot-ontology/robot-capability-and-task-representation.md
categories/safety/human-proximity-safety.md
categories/safety/index.md
categories/safety/safety-and-risk-management.md
categories/safety/safety-standards-certification-and-incident-investigation.md
categories/security-and-privacy/authentication-authorization-and-isolation.md
categories/security-and-privacy/communication-protection-threat-management-and-audit.md
categories/security-and-privacy/index.md
categories/security-and-privacy/privacy-and-video-data.md
categories/site-type-applications/commercial-facilities.md
categories/site-type-applications/home-and-apartment.md
categories/site-type-applications/hospital-and-healthcare.md
categories/site-type-applications/index.md
categories/site-type-applications/manufacturing-plant.md
categories/site-type-applications/other-sites.md
categories/site-type-applications/outdoor.md
categories/site-type-applications/warehouse.md
categories/space-and-map-model/index.md
categories/space-and-map-model/map-space-and-location-model.md
categories/space-and-map-model/maps-from-floor-plans-and-bim.md
categories/space-and-map-model/place-semantics-and-map-management.md
categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md
categories/verification-deployment-and-lifecycle/index.md
categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md
categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md
categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md
changelog.md
corrections.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/affordance.md
glossary/age-of-information.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automation-bias.md
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
glossary/capability-description-submodel.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/clarification-question.md
glossary/coalition-formation.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/common-coordinate-system.md
glossary/common-data-environment.md
glossary/compensating-transaction.md
glossary/condition-based-maintenance.md
glossary/configuration-copilot.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/confused-deputy.md
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
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
glossary/edit-cost.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/event-driven-rescheduling.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explicit-implicit-confirmation.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/giai.md
glossary/goal-condition.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/hallucination.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
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
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/irreducible-infeasible-subset.md
glossary/isa-95.md
glossary/job-shop-scheduling-problem.md
glossary/joint-goal-accuracy.md
glossary/json-schema.md
glossary/keystroke-level-model.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/milp.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-registry.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
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
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/schedule-stability.md
glossary/scor.md
glossary/semantic-id.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/signal-temporal-logic.md
glossary/similarity-transformation.md
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
glossary/success-weighted-by-path-length.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/time-window.md
glossary/topological-map.md
glossary/traversability.md
glossary/user-simulator.md
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
glossary/zones-and-conduits.md
ideas/chat-based-configuration-and-operation.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/daily/2026-09-26.md
logs/daily/2026-09-29.md
logs/index.md
logs/weekly/2026-W39.md
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
references/ref-569.md
references/ref-570.md
references/ref-571.md
references/ref-572.md
references/ref-573.md
references/ref-574.md
references/ref-575.md
references/ref-576.md
references/ref-577.md
references/ref-578.md
references/ref-579.md
references/ref-580.md
references/ref-581.md
references/ref-582.md
references/ref-583.md
references/ref-584.md
references/ref-585.md
references/ref-586.md
references/ref-587.md
references/ref-588.md
references/ref-589.md
references/ref-590.md
references/ref-591.md
references/ref-592.md
references/ref-593.md
references/ref-594.md
references/ref-595.md
references/ref-596.md
references/ref-597.md
references/ref-598.md
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
references/ref-610.md
references/ref-611.md
references/ref-612.md
references/ref-613.md
references/ref-614.md
references/ref-615.md
references/ref-616.md
references/ref-617.md
references/ref-618.md
references/ref-619.md
references/ref-620.md
references/ref-621.md
references/ref-622.md
references/ref-623.md
references/ref-624.md
references/ref-625.md
references/ref-626.md
references/ref-627.md
references/ref-628.md
references/ref-629.md
references/ref-630.md
references/ref-631.md
references/ref-632.md
references/ref-633.md
references/ref-634.md
references/ref-635.md
references/ref-636.md
references/ref-637.md
references/ref-638.md
references/ref-639.md
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
references/ref-644.md
references/ref-645.md
references/ref-646.md
references/ref-647.md
references/ref-648.md
references/ref-649.md
references/ref-650.md
references/ref-651.md
references/ref-652.md
references/ref-653.md
references/ref-654.md
references/ref-655.md
references/ref-656.md
references/ref-657.md
references/ref-658.md
references/ref-659.md
references/ref-660.md
references/ref-661.md
references/ref-662.md
references/ref-663.md
references/ref-664.md
references/ref-665.md
references/ref-666.md
references/ref-667.md
references/ref-668.md
references/ref-669.md
references/ref-670.md
references/ref-671.md
references/ref-672.md
references/ref-673.md
references/ref-674.md
references/ref-675.md
references/ref-676.md
references/ref-677.md
references/ref-678.md
references/ref-679.md
references/ref-680.md
references/ref-681.md
references/ref-682.md
references/ref-683.md
references/ref-684.md
references/ref-685.md
references/ref-686.md
references/ref-687.md
references/ref-688.md
references/ref-689.md
references/ref-690.md
references/ref-691.md
references/ref-692.md
references/ref-693.md
references/ref-694.md
references/ref-695.md
references/ref-696.md
references/ref-697.md
references/ref-698.md
references/ref-699.md
references/ref-700.md
references/ref-701.md
references/ref-702.md
references/ref-703.md
references/ref-704.md
references/ref-705.md
references/ref-706.md
references/ref-707.md
references/ref-708.md
references/ref-709.md
references/ref-710.md
references/ref-711.md
references/ref-712.md
references/ref-713.md
references/ref-714.md
references/ref-715.md
references/ref-716.md
references/ref-717.md
references/ref-718.md
references/ref-719.md
references/ref-720.md
references/ref-721.md
references/ref-722.md
references/ref-723.md
references/ref-724.md
references/ref-725.md
references/ref-726.md
references/ref-727.md
references/ref-728.md
references/ref-729.md
references/ref-730.md
references/ref-731.md
references/ref-732.md
references/ref-733.md
references/ref-734.md
references/ref-735.md
references/ref-736.md
references/ref-737.md
references/ref-738.md
references/ref-739.md
references/ref-740.md
references/ref-741.md
references/ref-742.md
references/ref-743.md
references/ref-744.md
references/ref-745.md
references/ref-746.md
references/ref-747.md
references/ref-748.md
references/ref-749.md
references/ref-750.md
references/ref-751.md
references/ref-752.md
references/ref-753.md
references/ref-754.md
references/ref-755.md
references/ref-756.md
references/ref-757.md
references/ref-758.md
references/ref-759.md
references/ref-760.md
references/ref-761.md
references/ref-762.md
references/ref-763.md
references/ref-764.md
references/ref-765.md
references/ref-766.md
references/ref-767.md
references/ref-768.md
references/ref-769.md
references/ref-770.md
references/ref-771.md
references/ref-772.md
references/ref-773.md
references/ref-774.md
references/ref-775.md
references/ref-776.md
references/ref-777.md
references/ref-778.md
references/ref-779.md
references/ref-780.md
references/ref-781.md
references/ref-782.md
references/ref-783.md
references/ref-784.md
references/ref-785.md
references/ref-786.md
references/ref-787.md
references/ref-788.md
references/ref-789.md
references/ref-790.md
references/ref-791.md
references/ref-792.md
references/ref-793.md
references/ref-794.md
references/ref-795.md
references/ref-796.md
references/ref-797.md
references/ref-798.md
references/ref-799.md
references/ref-800.md
references/ref-801.md
references/ref-802.md
references/ref-803.md
references/ref-804.md
references/ref-805.md
references/ref-806.md
references/ref-807.md
references/ref-808.md
references/ref-809.md
references/ref-810.md
references/ref-811.md
references/ref-812.md
references/ref-813.md
references/ref-814.md
references/ref-815.md
references/ref-816.md
references/ref-817.md
references/ref-818.md
references/ref-819.md
references/ref-820.md
references/ref-821.md
references/ref-822.md
references/ref-823.md
site-matrix.md
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
topics/2026/2026-09-25-area26-s10.md
topics/2026/2026-09-25-area26-s11.md
topics/2026/2026-09-25-area26-s3.md
topics/2026/2026-09-25-area26-s4.md
topics/2026/2026-09-25-area26-s6.md
topics/2026/2026-09-25-area26-s7.md
topics/2026/2026-09-25-area26-s8.md
topics/2026/2026-09-25-area27-s10.md
topics/2026/2026-09-25-area27-s4.md
topics/2026/2026-09-25-area27-s6.md
topics/2026/2026-09-25-area27-s7.md
topics/2026/2026-09-25-area27-s8.md
topics/2026/2026-09-25-area28-s11.md
topics/2026/2026-09-25-area28-s3.md
topics/2026/2026-09-25-area28-s4.md
topics/2026/2026-09-25-area28-s6.md
topics/2026/2026-09-25-area28-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/2026/2026-09-26-area04-s10.md
topics/2026/2026-09-26-area25-s7.md
topics/2026/2026-09-29-area08-s10.md
topics/2026/2026-09-29-area08-s11.md
topics/2026/2026-09-29-area08-s3.md
topics/2026/2026-09-29-area08-s4.md
topics/2026/2026-09-29-area08-s6.md
topics/2026/2026-09-29-area08-s7.md
topics/2026/2026-09-29-area08-s8.md
topics/2026/2026-09-29-area10-s10.md
topics/2026/2026-09-29-area10-s11.md
topics/2026/2026-09-29-area10-s3.md
topics/2026/2026-09-29-area10-s4.md
topics/2026/2026-09-29-area10-s6.md
topics/2026/2026-09-29-area10-s7.md
topics/2026/2026-09-29-area10-s8.md
topics/index.md
tracks/chat-based-configuration-and-operation/experiments.md
tracks/chat-based-configuration-and-operation/index.md
tracks/chat-based-configuration-and-operation/log.md
tracks/chat-based-configuration-and-operation/question-backlog.md
tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md
tracks/chat-based-configuration-and-operation/stage-10-integrated-verification.md
tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md
tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md
tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md
tracks/chat-based-configuration-and-operation/stage-6-chat-map-authoring.md
tracks/chat-based-configuration-and-operation/stage-7-chat-scenario-composition.md
tracks/chat-based-configuration-and-operation/stage-8-chat-robot-configuration.md
tracks/chat-based-configuration-and-operation/stage-9-chat-real-situation-replay.md
tracks/chat-based-configuration-and-operation/task-model-draft.md
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

### runs/2026-09-29-03/pages.json

```json
{
  "run_id": "2026-09-29-03",
  "outline": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 800,
      "summary": "언어 모델을 디지털 트윈에 쓰는 연구가 꼽는 데이터 부족·분석 비효율·설명 부족 과제가 이 영역의 세 가지 일과 맞물린다. [사실][^ref-827] 텍스트→시나리오 재구성의 정확도 한계 때문에 재현 결과는 사람이 확인하고 기록을 우선 입력으로 삼아야 할 것으로 보인다. [추정][^ref-834][^ref-835][^ref-833]",
      "planned_findings": [
        "f21",
        "f16",
        "f4",
        "한계 문장(f1·f9·f4)"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "자동 시뮬레이션 모델 생성·사건 트레이스·시나리오 재구성·로그 기반 모델 발견·서브트레이스 조건부 검증·백 파일 여섯 용어를 각주와 함께 정의한다. [사실][^ref-836][^ref-825][^ref-834][^ref-828][^ref-826][^ref-831]",
      "planned_findings": [
        "f1",
        "f5",
        "f12",
        "f6",
        "f8",
        "f10"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1700,
      "summary": "병원(감염병 환자 이송 침대 로봇 연합 디지털 트윈 시뮬레이션 검증)과 제조 공장(국내 무인운반차 자동물류 디지털트윈, 이기종 플릿·배치 시나리오 비교) 두 사례를 여섯 항목으로 쓰고, 둘 다 실제 운영 기록 재현이 아니라 시뮬레이션 검증·설계 비교임을 밝힌다. [사실][^ref-837][^ref-830][^ref-838]",
      "planned_findings": [
        "f18",
        "f17",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2200,
      "summary": "대화→모델 생성, 사양·로그→시뮬레이터와 트레이스 대조, 조건부 검증·불일치 진단, 텍스트→시나리오 재구성(자율주행 시험 도구 선례) 네 접근법을 정리한다. [사실][^ref-836][^ref-825][^ref-826][^ref-834]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 600,
      "summary": "rosbag2·DEVS·Simod·SUMO·Scenic 을 이 영역과의 관계와 함께 표로 둔다. rosbag2 재생은 로봇 자체 지능·제어 쪽 연계 대상이다. [사실][^ref-831] [추정][^ref-831]",
      "planned_findings": [
        "f10",
        "f11",
        "f5",
        "f6",
        "f13",
        "f15"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1650,
      "summary": "자연어→시뮬레이션 모델, 에이전트 비교 실험, DEVS 생성 벤치마크, 로그 기반 모델 발견, 조건부 검증, 언어 모델 디지털 트윈 서베이, 국내 병원·제조 공장 디지털 트윈 연구를 목록으로 둔다. [사실][^ref-836][^ref-832][^ref-825][^ref-828][^ref-826][^ref-827][^ref-837][^ref-830][^ref-838][^ref-829]",
      "planned_findings": [
        "f1",
        "f3",
        "f5",
        "f6",
        "f8",
        "f21",
        "f18",
        "f19",
        "f20",
        "f17"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1100,
      "summary": "ROP는 플릿 실행 기록→시나리오 변환, 대화로 조건 변경 접수, 재현 트레이스 대조·설명, 사람 확인을 맡고 시뮬레이션 엔진과 로봇 통신 기록 재생은 연계 대상으로 둘 것으로 보인다. [추정][^ref-825][^ref-826][^ref-831][^ref-832]",
      "planned_findings": [
        "f23",
        "f11",
        "f17"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 950,
      "summary": "원문 주석의 짝인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현, 34번과 18번의 구분, 37·38·9·13·54·44·47·62·63번과 트랙을 연결한다. [추정][^ref-836][^ref-825][^ref-832] [추정][^ref-830]",
      "planned_findings": [
        "f22",
        "f24",
        "f7",
        "f9",
        "f4",
        "f16",
        "f8",
        "f15"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "summary": "기록→시나리오 변환 형식, 재현 충실도 판정 지표와 승인 주체, 언어 모델 해석 오류를 막는 절차, 국내 물류창고·병원의 운영 기록 재현 사례 네 질문을 올린다.",
      "planned_findings": [
        "open_questions_new 4건"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3~11절 신규 작성(seed → draft), 출처 15건, 현장 유형 사례 2건(병원·제조 공장), 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 지시 9건 이행. 2차 재검증 수정 8건 이행(약어 AGV·SMT·DEVS·NHTSA·PLC 첫 등장 풀어 쓰기, 9절 원문 문장 재서술, 6절 단락 분리, 10절 연결 판단 2건 [추정] 태그, 6절 절 참조 이름 병기)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"6. 대표 접근법과 기술\" 절(2,271자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"8. 대표 연구와 자료\" 절(1,684자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"4. 핵심 개념과 용어\" 절(1,010자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(922자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"3. 왜 중요한가\" 절(796자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"11. 열린 질문\" 절(787자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area11-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(630자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | 3~11절 신규 작성(seed → draft), 출처 15건, 현장 유형 사례 2건(병원·제조 공장), 열린 질문 4건, 용어 4건, 1차 조건부 승인 수정 지시 9건 이행, 2차 재검증 수정 8건 이행(약어 풀어 쓰기·9절 원문 문장 재서술·6절 단락 분리·10절 태그 2건) | run 2026-09-29-03",
  "index_updates": {
    "home_recent": "2026-09-29 — 11. 채팅으로 실제 상황 시뮬레이션 재현: 3~11절 신규 작성(seed → draft). 대화→시뮬레이션 모델 생성, 사양·로그→시뮬레이터와 사건 트레이스 대조, 서브트레이스 조건부 검증, 텍스트→시나리오 재구성 선례를 정리하고 병원·제조 공장 사례 2건, 열린 질문 4건, 용어 4건을 더했다. 로봇 플릿 운영 기록을 대화로 재현한 현장 사례는 미확인",
    "category_recent": "2026-09-29 — 11. 채팅으로 실제 상황 시뮬레이션 재현: 3~11절 신규 작성(seed → draft), 출처 15건(원문 미열람 3건), 현장 유형 사례 2건(병원·제조 공장, 시뮬레이션 검증·설계 비교 사례), 열린 질문 4건, 용어 4건. 1차 조건부 승인 수정 지시 9건 이행. 2차 재검증 수정 8건 이행(약어 AGV·SMT·DEVS·NHTSA·PLC 첫 등장 풀어 쓰기, 9절 분류 원문 19장 문장 재서술, 6절 단락 분리, 10절 연결 판단 2건 [추정] 태그)",
    "area_recent": "2026-09-29 — 실행 2026-09-29-03: 3~11절 신규 작성. 대화·기록에서 시뮬레이션을 만들고 재현 충실도를 확인하는 접근법 4종, 병원·제조 공장 사례, 열린 질문 4건, 용어 4건. 로봇 플릿 운영 기록을 대화로 재현한 현장 사례는 미확인. 2차 재검증 수정 8건 이행"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "automatic-simulation-model-generation",
      "term_ko": "자동 시뮬레이션 모델 생성",
      "term_en": "Automatic Simulation Model Generation (ASMG)",
      "definition": "사람이 시뮬레이션 도구를 직접 다루지 않고 데이터·사양·자연어 설명에서 실행 가능한 시뮬레이션 모델을 자동으로 만드는 기법이다.",
      "description": "Elbasheer 외(2025)는 대규모 언어 모델과 ASMG 를 결합해 의도 표현→템플릿 기반 지식 추출→객체지향 데이터 기반 구성요소로 모델 구성→실행·결과 분석의 4단계로 자연어 대화에서 제조 시스템 시뮬레이션 모델을 직접 만들었다. 11. 채팅으로 실제 상황 시뮬레이션 재현과 9. 채팅으로 시나리오 구성이 기대는 방법이다.",
      "related_areas": [
        11,
        9,
        33,
        36,
        44
      ],
      "sources": [
        "ref-836"
      ]
    },
    {
      "action": "new",
      "slug": "event-trace",
      "term_ko": "사건 트레이스",
      "term_en": "Event Trace",
      "definition": "시스템이나 시뮬레이터가 실행 중에 낸 사건을 시각 순서대로 기록한 구조화 목록으로, 재현 결과를 실제 기록이나 제약과 대조하는 데 쓴다.",
      "description": "Chen 외(2026)는 자연어 사양에서 생성한 이산 사건 시스템 명세(Discrete Event System Specification, DEVS) 시뮬레이터가 내는 구조화 사건 트레이스를 사양에서 도출한 시간·인과·의미 제약과 대조해 검증하는 벤치마크를 제안했다. 11. 채팅으로 실제 상황 시뮬레이션 재현의 재현 충실도 확인이 이 대조에 기댄다.",
      "related_areas": [
        11,
        36,
        54
      ],
      "sources": [
        "ref-825"
      ]
    },
    {
      "action": "new",
      "slug": "scenario-reconstruction",
      "term_ko": "시나리오 재구성",
      "term_en": "Scenario Reconstruction",
      "definition": "사고 보고서·운영 기록 같은 실제 상황의 기록에서 정보를 추출해 시뮬레이터에서 다시 실행할 수 있는 시나리오로 만드는 일이다.",
      "description": "SoVAR(ASE 2024)와 OmniTester(2024)가 언어 모델로 사고 보고서 텍스트에서 시나리오를 재구성해 자율주행 시험 시뮬레이터에서 재현했다. 정보 추출 정확도와 지도 대응의 한계가 보고되어, 11. 채팅으로 실제 상황 시뮬레이션 재현에서는 사람 확인과 실제 기록 우선 입력이 필요한 것으로 본다.",
      "related_areas": [
        11,
        33,
        36
      ],
      "sources": [
        "ref-834",
        "ref-835"
      ]
    },
    {
      "action": "new",
      "slug": "bag-file",
      "term_ko": "백 파일",
      "term_en": "Bag File (rosbag2)",
      "definition": "ROS 2 에서 토픽 메시지를 시각과 함께 저장한 기록 파일로, 나중에 재생해 로봇 소프트웨어를 실제 하드웨어 없이 시험·디버깅하는 데 쓴다.",
      "description": "rosbag2 는 ros2 bag record 로 기록하고 ros2 bag play 로 재생 속도·시작 시점·토픽 선택·반복·/clock 발행 옵션을 두어 재생하며 MCAP·SQLite3 저장 형식을 지원한다. 로봇 한 대의 통신 기록을 재생하는 로봇 자체 지능·제어 쪽 도구이며, 플릿 수준 실제 상황 재현과는 층이 다르다.",
      "related_areas": [
        11,
        36,
        43
      ],
      "sources": [
        "ref-831"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-824",
      "org": "Kleiman, J., Frank, K., Voyles, J., & Campagna, S.",
      "title": "Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making",
      "published": "2025-05-19",
      "url": "https://arxiv.org/abs/2505.13761",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "시뮬레이션으로 언어 모델을 접지하고 언어 모델을 시뮬레이터의 대화 인터페이스로 쓰는 결합 프레임워크. 초록에 정량 평가 없음(프리프린트, v1 2025-05-19; v2 2025-05-21 있음).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-825",
      "org": "Chen, Z., Zhuang, H., Li, Z., & Li, C.",
      "title": "Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism",
      "published": "2026-03-04",
      "url": "https://arxiv.org/abs/2603.03784",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 사양에서 DEVS 이산 사건 시뮬레이터를 단계별로 생성하고, 사건 트레이스를 시간·인과·의미 제약과 대조해 검증하는 벤치마크(프리프린트, v1 2026-03-04; v2 2026-05-21 있음).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-826",
      "org": "Ghasemloo, M., Eckman, D. J., & Li, Y.",
      "title": "Subtrace-Conditional Validation of Simulation Models and Digital Twins",
      "published": "2026-07-19",
      "url": "https://arxiv.org/abs/2607.17088",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "관측 트레이스의 일부 입력을 고정한 조건부 시뮬레이션과 적합도 검정으로 디지털 트윈을 검증하고 불일치 원인 입력 모델을 진단하는 통계 방법(프리프린트).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-827",
      "org": "Yang, L., Luo, S., Cheng, X., & Yu, L.",
      "title": "Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges",
      "published": "2025-03-04",
      "url": "https://arxiv.org/abs/2503.02167",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델을 디지털 트윈 모델링에 쓰는 연구를 기술–예측–처방 프레임워크와 단계별 분류로 정리한 서베이(프리프린트).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-828",
      "org": "Camargo, M., Dumas, M., & González-Rojas, O.",
      "title": "Automated Discovery of Business Process Simulation Models from Event Logs",
      "published": "2020",
      "url": "https://arxiv.org/abs/1910.05404",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "이벤트 로그에서 프로세스 시뮬레이션 모델을 자동 발견하고 로그와의 행동 유사도를 최대화하도록 조정하는 방법(arXiv 판, Decision Support Systems (2020) 게재). 'Simod' 라는 도구명은 초록이 아니라 논문 본문의 명칭이다.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-829",
      "org": "Sieve, R., Kobialka, P., Slaughter, L., Schlatte, R., Johnsen, E. B., & Tapia Tarifa, S. L. (University of Oslo)",
      "title": "BedreFlyt: Improving Patient Flows through Hospital Wards with Digital Twins",
      "published": "2025-05-07",
      "url": "https://arxiv.org/abs/2505.06287",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "병원 병동 환자 흐름 디지털 트윈으로 형식 모델·온톨로지·SMT 해결기를 결합하고 평균·최악 자원 시나리오를 오케스트레이터 설정으로 탐색(프리프린트).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-830",
      "org": "이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4))",
      "title": "자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용",
      "published": "2021-12",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자동물류시스템의 설계 단계 가상 검증과 운영 단계 실시간 모니터링·분석을 위한 디지털트윈을 국내 제조업체 AGV 시스템에 적용한 국내 학술지 논문(초록 확인).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (ros2/rosbag2 GitHub)",
      "title": "rosbag2 — README (Recording and playback of ROS 2 communications)",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "ROS 2 공식 기록·재생 도구. record/play 명령, 재생 속도·시작 시점·토픽 선택·반복·/clock 발행 옵션, MCAP·SQLite3 저장 형식을 설명한다.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-832",
      "org": "Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P.",
      "title": "LLM Agents Perform Controlled Experiments Using Simulation Models",
      "published": "2026-08-22",
      "url": "https://arxiv.org/abs/2608.23622",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델 에이전트가 사용자 질의에서 실험을 설계하고 매개변수 구성을 나란히 시뮬레이션해 결과를 해석·권고하는 다중 에이전트 프레임워크를 제약 공정 설계에 적용(프리프린트).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-833",
      "org": "Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J.",
      "title": "Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving",
      "published": "2026-07-15",
      "url": "https://arxiv.org/abs/2607.14387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "규정 문서를 대화형 인터페이스와 반복 검색 증강 생성으로 Scenic 시나리오로 바꾸는 프레임워크. 123개 시나리오에서 컴파일 성공 76.42%, 프레임워크 정확도 58.17%(프리프린트).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-834",
      "org": "Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024)",
      "title": "SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing",
      "published": "2024-09-12",
      "url": "https://arxiv.org/abs/2409.08081",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "언어 모델로 사고 보고서에서 정보를 추출하고 제약 해결로 궤적을 만들어 여러 지도에 사고 시나리오를 재구성하는 자율주행 시험 도구(ASE 2024 채택, arXiv 초록 확인).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-835",
      "org": "Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S.",
      "title": "Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles",
      "published": "2024-09-10",
      "url": "https://arxiv.org/abs/2409.06450",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "멀티모달 언어 모델·SUMO·검색 증강 생성으로 자율주행 시험 시나리오를 만들고 사고 보고서 시나리오를 재구성하는 OmniTester(프리프린트).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-836",
      "org": "Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing)",
      "title": "Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems",
      "published": "2025-11-14",
      "url": "https://link.springer.com/article/10.1007/s10845-025-02732-z",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 자연어 대화에서 실행 가능한 제조 시뮬레이션 모델을 만드는 LLM+ASMG 방법(4단계, 18개 동작 유형, 응답 8초~5분). Springer 페이지는 인증 리다이렉트라 Semantic Scholar API 초록으로 확인.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-837",
      "org": "Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24))",
      "title": "Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins",
      "published": "2025-12-17",
      "url": "https://www.mdpi.com/2079-9292/14/24/4954",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 감염병 환자 이송용 간호사 추종 침대 로봇 여러 대를 연합 디지털 트윈으로 시뮬레이션해 검증한 한국 병원 사례. MDPI 페이지 403 이라 Semantic Scholar API 초록으로 확인.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-838",
      "org": "Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports)",
      "title": "Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts",
      "published": "2026-07-18",
      "url": "https://www.nature.com/articles/s41598-026-57316-5",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 운송·조작(manipulation) 역할이 다른 이기종 로봇 플릿·공정·배치를 함께 모델링한 디지털 트윈으로 브라운필드·그린필드 공장 시나리오를 비교(최대 3.5배 처리량). Nature 페이지는 인증 리다이렉트라 Semantic Scholar API 초록으로 확인.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가?",
      "areas": [
        11,
        37,
        33
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가?",
      "areas": [
        11,
        36,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "대화로 재현·비교한 시뮬레이션 결과를 근거로 로봇 수·경로·정책을 바꾸는 결정에서 언어 모델의 결과 해석 오류를 막는 검증·승인 절차와 평가 지표는 무엇인가?",
      "areas": [
        11,
        13
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)?",
      "areas": [
        11,
        61,
        63
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "11. 채팅으로 실제 상황 시뮬레이션 재현"
    }
  ],
  "standards_updates": [
    {
      "name": "rosbag2",
      "kind": "오픈소스",
      "org": "ROS 2 (ros2/rosbag2 GitHub)",
      "url": "https://github.com/ros2/rosbag2",
      "related_areas": [
        11,
        36,
        43
      ],
      "summary": "ROS 2 통신을 기록·재생하는 공식 도구. record/play 명령, 재생 속도·시작 시점·토픽 선택·반복·/clock 발행 옵션, MCAP·SQLite3 저장 형식. 로봇 한 대의 통신 기록 재생이라 플릿 수준 실제 상황 재현과는 연계 대상으로 구분한다.",
      "ref_id": "ref-831"
    },
    {
      "name": "Simod (로그 기반 업무 프로세스 시뮬레이션 모델 자동 발견 도구)",
      "kind": "오픈소스",
      "org": "Camargo, M., Dumas, M., & González-Rojas, O.",
      "url": "https://arxiv.org/abs/1910.05404",
      "related_areas": [
        11,
        36,
        37
      ],
      "summary": "이벤트 로그에서 프로세스 모델과 시뮬레이션 매개변수를 자동 발견하고 하이퍼파라미터 최적화로 시뮬레이션 행동과 로그 행동의 유사도를 최대화하는 도구. 운영 기록을 지정하면 시뮬레이션을 재현하는 방법의 선례다.",
      "ref_id": "ref-828"
    }
  ],
  "additional_research_requests": [
    "5절 병원·제조 공장 사례의 '완료·인계' 칸에 넣을 사실: Woo 외(ref-837)·이동건 외(ref-830)·Valiollahi 외(ref-838)의 원문(초록 밖)에서 완료 판정 기준, 승강기 연동 여부, 정량 결과, 실제 공장 데이터 대조 여부를 확인해야 한다.",
    "6절·8절에 넣을 사실: Elbasheer 외(ref-836)의 원문에서 어떤 시뮬레이션 도구를 썼고 생성 모델의 정확도를 어떻게 검증했는지 확인해야 한다(초록에는 없음).",
    "5절 물류창고·상업 시설 사례: 물류창고·상업 시설에서 로봇 운영 기록으로 실제 상황을 시뮬레이션에 재현하거나 조건을 바꿔 비교한 사례가 없어 두 현장 유형의 사례를 쓰지 못했다. 예산 상한으로 넣지 못한 Webb·Tokhi·Alkan 의 AMR 플릿 디지털 트윈 사고 대응 논문과 WSC 2022 창고 디지털 트윈 논문을 다음 실행에서 확인하면 물류창고 사례가 될 수 있다.",
    "6절 재현 충실도 확인: Simod(ref-828)의 정량 유사도 수치와 SoVAR(ref-834)의 재현 성공률이 초록에 없어 본문에 수치를 쓰지 못했다.",
    "6절·11절: 언어 모델 자체를 디지털 트윈 시뮬레이터로 쓰는 연구(CALM-DT)와 병원 디지털 트윈 검증 논문(arXiv 2303.04117)은 예산 상한으로 브리프에 들어오지 못해 본문에 넣지 못했다."
  ],
  "fixes_applied": [
    "f20 '운송·조립'을 '운송·조작(manipulation)'으로 — 5절 제조 공장 사례 표의 수행 자원 칸과 reference_updates 의 ref-838 요약에서 '운송·조작(manipulation) 역할'로 썼고 '조립'은 어디에도 쓰지 않았다.",
    "f18 저자 영문 표기 — 5절 병원 사례 서술과 8절 목록, 각주 정의에서 'Woo, J., Shin, H., Jeon, C., & Park, S.'로 쓰고 한글 표기 '우지영·신효진·전창훈·박상찬'은 쓰지 않았다.",
    "ref-836·ref-837·ref-838 원문 미열람 표시 — 13절 세 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 의 세 항목에 source_unopened: true 를 넣었으며 요약이 '원문 미열람. '으로 시작하게 두었다.",
    "f12·f13·f14 를 5절 '실외' 사례로 세우지 않음 — 5절은 병원(f18 중심, f17 은 what-if 시나리오 구성 방식 보조)과 제조 공장(f19·f20) 두 사례만 현장 유형 × 여섯 항목으로 썼고, 두 사례 모두 실제 운영 기록 재현이 아니라 시뮬레이션 검증·설계 비교 사례임을 서술 문장에 밝혔다. SoVAR·OmniTester·Chat2Scenic 은 6절 소제목 '텍스트 기록에서 시나리오 재구성 — 자율주행 시험 도구의 선례'에서 차량 소프트웨어 시험 도구임을 첫 문장에 밝혀 다뤘고, site_matrix_updates 에는 병원·제조 공장 칸만 넣고 실외 칸을 넣지 않았다.",
    "f3 적용 대상 명시 — 6절 '언어 모델 에이전트의 비교 실험'에서 Xia 외의 적용 대상이 제약 공정 설계(비로봇 도메인)임을 문장으로 밝히고 로봇 플릿 적용 근거가 아니라 방법의 선례로만 쓴다고 적었으며, 8절 목록에도 '비로봇 도메인의 선례'를 병기했다.",
    "f17 병상 배정을 ROP 기능처럼 쓰지 않음 — 5절 병원 사례 보조 단락에서 BedreFlyt 를 '평균·최악 자원 수요와 가용 자원 변동을 오케스트레이터 설정으로 what-if 시나리오로 만드는 방식'의 예시로만 쓰고, 병상 배정 최적화 자체는 상위 업무 시스템 연계 영역이라고 적었다. 9절 표의 상위 업무 시스템 행에도 병상 배정을 외부 연계 칸에 두었다.",
    "f6·ref-828 게재지 병기 — 13절 ref-828 각주 정의 제목 뒤에 'Decision Support Systems (2020) 게재, arXiv 판'을 병기하고 8절 목록에도 게재지를 적었으며, reference_updates 의 ref-828 요약에 'Simod' 도구명이 초록이 아니라 논문 본문의 명칭임을 남겼다.",
    "ref-824·ref-825 판 표기 — 13절 각주 발행일을 ref-824 '2025-05-19 (v1; v2 2025-05-21)', ref-825 '2026-03-04 (v1; v2 2026-05-21)'로 썼다. reference_updates 의 published 는 스키마 패턴 때문에 v1 날짜만 넣고 판 정보는 summary 에 적었다.",
    "f1·f9·f4 한계 문장 — 3절 마지막 단락에 '로봇 플릿의 실제 운영 기록을 대화로 시뮬레이션에 재현한 현장 사례는 이번 조사(2026-09-29 기준)에서 확인되지 않았고, 확인된 것은 연구 프로토타입과 병원·제조 공장의 시뮬레이션 검증·설계 비교 사례뿐이다'를 두었고, 11절 첫 문장과 6절 조건부 검증 단락(로봇 플릿 적용 사례 미확인)에도 같은 한계를 남겼다.",
    "2차: AGV 첫 등장 풀어 쓰기 — 5절 제조 공장 사례 제목을 '무인운반차(Automated Guided Vehicle, AGV) 자동물류시스템을 …'으로 썼고(표의 작업 대상·수행 자원 칸은 그 뒤 등장이므로 약어 유지), 자동 분리로 별도 페이지가 되어도 첫 등장이 풀어 쓰이도록 8절 이동건 외 항목에도 '국내 제조업체 무인운반차(Automated Guided Vehicle, AGV) 자동물류시스템'으로 썼다.",
    "2차: SMT 첫 등장 풀어 쓰기 — 5절 병원 사례 보조 단락(BedreFlyt)에 브리프 f17 의 '실행 가능한 형식 모델·온톨로지·충족 가능성 모듈로 이론(Satisfiability Modulo Theories, SMT) 해결기를 결합한'을 넣고, 8절 Sieve 외 항목에서도 같은 표기로 풀어 썼다.",
    "2차: DEVS·NHTSA·PLC 첫 등장 풀어 쓰기 — 6절 '사양·기록에서 시뮬레이터를 만들고 트레이스로 대조하기' 단락의 첫 DEVS 를 '이산 사건 시스템 명세(Discrete Event System Specification, DEVS) 형식'으로, 7절 표의 이름 칸을 같은 표기로, 6절 시나리오 재구성 단락의 NHTSA 를 '미국 도로교통안전국(National Highway Traffic Safety Administration, NHTSA) 사고 보고서'로, 9절 표 시설·설비 제어 행의 PLC 를 '프로그래머블 로직 컨트롤러(Programmable Logic Controller, PLC)'로 썼다. 4절 용어 정의에는 세 약어가 나오지 않음을 확인했고, glossary_updates 의 사건 트레이스 설명에서도 DEVS 를 풀어 썼다.",
    "2차: 9절 마지막 단락의 분류 원문 19장 문장 재서술 — '이 경계는 제품 전략에 따라 이동할 수 있다.'를 '분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 본다.'로 바꾸고, 따옴표 구절 \"인터페이스와 실행 보장\"을 따옴표 없이 '시뮬레이션 엔진과의 연결 인터페이스와 재현 실행의 보장을 맡는 쪽에 가깝다'로 재서술했다. [분류원문] 태그는 붙이지 않았다.",
    "2차: 6절 '텍스트 기록에서 시나리오 재구성 — 자율주행 시험 도구의 선례' 단락 분리 — 선례 안내·SoVAR·OmniTester·교차 확인 문장(f12·f13·f14) 4문장을 첫 단락으로, Chat2Scenic·종합 추정 문장(f15·f16) 2문장을 둘째 단락으로 나눴다.",
    "2차: 10절 '9. 채팅으로 시나리오 구성' 항목 태그 — '대화에서 시나리오·모델을 만드는 방법을 공유한다.'의 태그를 [사실]에서 [추정]으로 바꾸고 각주 [^ref-836][^ref-825]는 유지했다.",
    "2차: 10절 '54. 시험·형식 검증·벤치마크' 항목 태그 — '조건부 검증과 시나리오 생성 정확도 지표가 검증 방법에 해당한다.'의 태그를 [사실]에서 [추정]으로 바꾸고 각주 [^ref-826][^ref-833]은 유지했다.",
    "2차: 6절 마지막 문장의 절 참조 — '3절에서 말한'을 '3. 왜 중요한가 절에서 말한'으로 바꿔 자동 분리 뒤 주제 페이지에 놓여도 원 페이지의 절임이 드러나게 했다(따옴표 구절은 따옴표를 빼고 '사람 확인과 기록 우선 판단'으로 썼다).",
    "분량 초과 자동 분리: 11. 채팅으로 실제 상황 시뮬레이션 재현 본문 10,944자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,229자"
  ]
}
```

### runs/2026-09-29-03/pages/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [시뮬레이션 재현, 시나리오 재구성, 사건 트레이스, 자동 시뮬레이션 모델 생성, 조건부 검증]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-824, ref-825, ref-826, ref-827, ref-828, ref-829, ref-830, ref-831, ref-832, ref-833, ref-834, ref-835, ref-836, ref-837, ref-838]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현

# 11. 채팅으로 실제 상황 시뮬레이션 재현

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]

## 3. 왜 중요한가

실제 상황을 시뮬레이션에 되살려 조건을 바꿔 보는 일은, 언어 모델을 [디지털 트윈](../../glossary/digital-twin.md)에 쓰는 연구가 공통으로 꼽는 세 과제인 정확한 모델링을 위한 데이터 부족, 시스템 분석의 비효율, 물리–디지털 상호작용의 설명 부족과 그대로 맞닿아 있다. [사실][^ref-827] 기록에서 모델을 만들고, 대화로 분석을 쉽게 하고, 재현과 실제의 차이를 설명하는 일이 이 영역이 다루는 세 가지 일이다.

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 왜 중요한가](../../topics/2026/2026-09-29-area11-s3.md)에 있다.

## 4. 핵심 개념과 용어

**자동 시뮬레이션 모델 생성(Automatic Simulation Model Generation, ASMG)** — 사람이 시뮬레이션 도구를 직접 다루지 않고 데이터·사양·자연어 설명에서 실행 가능한 시뮬레이션 모델을 자동으로 만드는 기법이다. Elbasheer 외는 대규모 언어 모델과 결합해 자연어 대화에서 제조 시스템 시뮬레이션 모델을 직접 만들었다. [사실][^ref-836]

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area11-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 병원

**사례:** 감염병 환자 도착 시 음압 이송 침대 로봇 여러 대의 환자 운반을 연합 디지털 트윈으로 시뮬레이션해 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 감염병 환자가 병원에 도착하는 사건. 시뮬레이션은 이 도착 시점부터 병원에서 일어나는 전 과정을 다룬다. [사실][^ref-837] |
| 작업 대상 | 감염병 환자(사람)와 환자를 실은 음압 챔버 이송 침대. [사실][^ref-837] |
| 수행 자원 | 간호사 추종 음압 이송 침대 로봇 여러 대와 간호사. 연합(federated) 디지털 트윈 구조가 여러 대의 동시 운용을 시뮬레이션한다. [사실][^ref-837] |
| 제약 | 감염 관리(음압 챔버)와 간호사 추종 주행. 승강기 연동·구역 제한 여부는 초록에서 미확인. [사실][^ref-837] |
| 완료·인계 | 미확인(초록에 완료 판정 기준이 없다). |
| 예외·성과 | 시나리오 기반 시뮬레이션으로 시스템 성능을 검증했다. 정량 결과와 실패 복구 절차는 미확인. [사실][^ref-837] |

이 사례는 실제 운영 기록을 시뮬레이션에 재현한 것이 아니라, 감염병 환자 도착부터 병원에서 일어나는 전 과정을 시나리오로 정의해 시뮬레이션으로 성능을 검증한 사례다(Woo, J., Shin, H., Jeon, C., & Park, S., Electronics, 2025-12-17 발행). [사실][^ref-837] 이 영역의 관점에서는 시작 조건(환자 도착)과 수행 자원(로봇 여러 대·간호사)을 시나리오로 잡는 방식이 실제 상황 재현의 입력 정의에 해당한다.

조건을 바꿔 비교하는 방식의 예로, 오슬로대의 BedreFlyt 는 실행 가능한 형식 모델·온톨로지·충족 가능성 모듈로 이론(Satisfiability Modulo Theories, SMT) 해결기를 결합한 병원 병동 환자 흐름 디지털 트윈에서 평균·최악 자원 수요와 가용 자원 변동을 아우르는 what-if 시나리오를 오케스트레이터 설정으로 만들어 탐색한다. [사실][^ref-829] 병상 배정 최적화 자체는 상위 업무 시스템의 연계 영역이므로 여기서는 시나리오를 설정으로 만드는 방식만 참고한다.

**현장 유형:** 제조 공장

**사례:** 무인운반차(Automated Guided Vehicle, AGV) 자동물류시스템을 설계 단계에서 가상으로 검증하고 로봇 플릿·배치 시나리오를 비교

| 항목 | 내용 |
|---|---|
| 시작 조건 | 시스템이 구성·운영되기 전에는 문제를 예측·대응할 수 없다는 설계 단계의 한계에서 가상 검증 요구가 생긴다. [사실][^ref-830] |
| 작업 대상 | AGV 자동물류시스템이 나르는 공정 물류와, 공정·공장 배치·로봇 플릿을 함께 모델링한 정보. [사실][^ref-830] [사실][^ref-838] |
| 수행 자원 | 국내 제조업체의 AGV 플릿. [사실][^ref-830] 시나리오 비교 연구에서는 운송·조작(manipulation) 역할이 다른 이기종 로봇 플릿. [사실][^ref-838] |
| 제약 | 기존 공장(브라운필드)에서는 혼잡 때문에 플릿 확장 효과가 체감한다. [사실][^ref-838] |
| 완료·인계 | 미확인(두 초록 모두 완료 판정 기준을 적지 않았다). |
| 예외·성과 | 국내 사례는 진단·분석·예측·최적화의 실효성을 검증했다. [사실][^ref-830] 신규 공장(그린필드)에서는 배치·플릿 규모·역할 비율을 비교해 로봇당 생산성을 줄이지 않고 처리량을 최대 3.5배 높이는 구성을 찾았다(저자 보고값). [사실][^ref-838] |

두 연구 모두 실제 운영 기록을 재현한 것이 아니라 설계 단계의 가상 검증과 시나리오 기반 설계 비교 사례다. 성균관대·LG전자의 국내 연구는 설계 단계의 가상 검증과 운영 단계의 실시간 모니터링·분석을 하나의 디지털트윈으로 묶어 국내 제조업체 AGV 자동물류시스템에 적용했다. [사실][^ref-830] Valiollahi 외의 연구가 실제 공장 데이터와 대조했는지는 초록에서 확인되지 않았다. [사실][^ref-838] 이 영역에서 보면 두 사례는 조건을 바꿔 비교하는 절차의 선례이며, 실제 기록을 지정하면 재현하는 부분은 아직 확인된 사례가 없다.

## 6. 대표 접근법과 기술

대화로 시뮬레이션 모델을 만드는 연구, 시뮬레이션으로 언어 모델을 접지하는 구조, 에이전트가 구성을 바꿔 비교 실험을 돌리는 연구를 함께 보면 이 영역의 기능은 언어 모델이 인터페이스와 실험 설계를 맡고 수치 결론은 시뮬레이션 실행에서 얻는 구조로 수렴한다. [추정][^ref-836][^ref-824][^ref-832]

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area11-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준·프레임워크 전체 목록은 [표준 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area11-s7.md)에 있다.

## 8. 대표 연구와 자료

Elbasheer 외, Natural language-driven production planning(2025, Journal of Intelligent Manufacturing) — 자연어 대화에서 실행 가능한 제조 시뮬레이션 모델을 만드는 4단계 방법. 이 영역의 대화로 재현하는 일에 가장 가까운 방법이나 원문은 열지 못했다. [사실][^ref-836]

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 연구와 자료](../../topics/2026/2026-09-29-area11-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 플릿 수준 실행 기록(작업·배정·위치·사건 시각)을 시나리오 사양으로 바꾸고 여러 로봇·설비의 상황을 다시 돌린다 | rosbag2 같은 로봇 한 대의 통신 기록 재생과 로봇 자체 소프트웨어 디버깅 |
| 시설·설비 제어 | 승강기 대기·문 개폐 같은 설비 사건을 기록에서 시나리오 조건으로 반영한다 | 승강기·컨베이어·프로그래머블 로직 컨트롤러(Programmable Logic Controller, PLC)의 제어 자체와 설비 시뮬레이션 모델 |
| 상위 업무 시스템 | 대화로 받은 조건 변경(로봇 수·경로·정책)을 시뮬레이션 실행 요청으로 바꾸고 비교 결과를 설명한다 | 병상 배정·생산 계획 같은 업무 최적화 판단 |
| 업종별 조건 | 감염 관리 구역·실외 차량 규정 같은 조건을 시나리오 제약으로 받는다 | 의료·실외 차량 등의 전문 요구사항 정의 |

확인한 자료를 종합하면 이 영역에서 ROP가 직접 맡을 범위는 플릿 실행 기록을 시나리오 사양으로 바꾸고, 대화로 조건 변경을 받아 시뮬레이션 실행을 요청하며, 재현 트레이스를 실제 기록과 대조해 차이를 설명하고 사람이 확인하게 하는 일이고, 이산 사건·물리 시뮬레이션 엔진과 로봇 자체 통신 기록 재생은 연계 대상으로 두는 것이 맞을 것으로 보인다. [추정][^ref-825][^ref-826][^ref-831][^ref-832] rosbag2 가 기록 단위를 ROS 2 토픽 메시지로 두는 점을 보면, 로봇 한 대의 센서·제어 메시지를 되살리는 층과 플릿 수준 상황을 다시 돌리는 층은 구분해야 할 것으로 보인다. [추정][^ref-831]

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 본다. 이종 제조사를 연결하는 ROP는 시뮬레이션 엔진을 직접 만들지 않고 시뮬레이션 엔진과의 연결 인터페이스와 재현 실행의 보장을 맡는 쪽에 가깝다([범위 경계](../../about/scope-boundary.md) 참고). 병원 병상 배정처럼 업무 계획 자체를 최적화하는 일은 연계 대상이며, ROP는 그 계획이 바뀌었을 때 로봇 운영이 어떻게 달라지는지를 재현·비교하는 데 머문다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 원문 주석대로 이 영역의 대화가 부르는 엔진 영역이다. 사양·기록에서 시뮬레이터를 만들고 트레이스로 대조하는 방법은 이 영역과 양쪽에 연결한다. [추정][^ref-836][^ref-825][^ref-832]

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area11-s10.md)에 있다.

## 11. 열린 질문

로봇 플릿 운영 기록을 대화로 시뮬레이션에 재현한 현장 사례는 이번 조사(2026-09-29 기준)에서 확인되지 않았으며, 아래 질문은 그 공백에서 나온 것이다. id 는 퍼블리셔가 부여한다.

자세한 내용은 주제 페이지 [11. 채팅으로 실제 상황 시뮬레이션 재현 — 열린 질문](../../topics/2026/2026-09-29-area11-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-824]: Kleiman, J., Frank, K., Voyles, J., & Campagna, S., Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making, 2025-05-19 (v1; v2 2025-05-21), https://arxiv.org/abs/2505.13761, 접근일 2026-09-29
[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-826]: Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins, 2026-07-19, https://arxiv.org/abs/2607.17088, 접근일 2026-09-29
[^ref-827]: Yang, L., Luo, S., Cheng, X., & Yu, L., Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges, 2025-03-04, https://arxiv.org/abs/2503.02167, 접근일 2026-09-29
[^ref-829]: Sieve, R., Kobialka, P., Slaughter, L., Schlatte, R., Johnsen, E. B., & Tapia Tarifa, S. L. (University of Oslo), BedreFlyt: Improving Patient Flows through Hospital Wards with Digital Twins, 2025-05-07, https://arxiv.org/abs/2505.06287, 접근일 2026-09-29
[^ref-830]: 이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4)), 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용, 2021-12, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861, 접근일 2026-09-29
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-29
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)
[^ref-837]: Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24)), Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins, 2025-12-17, https://www.mdpi.com/2079-9292/14/24/4954, 접근일 2026-09-29 (원문 미열람)
[^ref-838]: Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports), Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts, 2026-07-18, https://www.nature.com/articles/s41598-026-57316-5, 접근일 2026-09-29 (원문 미열람)
```

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s6.md

````markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 접근법과 기술"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-824, ref-825, ref-826, ref-828, ref-832, ref-833, ref-834, ref-835, ref-836]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#6
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 접근법과 기술

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대화로 시뮬레이션 모델을 만드는 연구, 시뮬레이션으로 언어 모델을 접지하는 구조, 에이전트가 구성을 바꿔 비교 실험을 돌리는 연구를 함께 보면 이 영역의 기능은 언어 모델이 인터페이스와 실험 설계를 맡고 수치 결론은 시뮬레이션 실행에서 얻는 구조로 수렴한다. [추정][^ref-836][^ref-824][^ref-832]
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대화로 시뮬레이션 모델을 만드는 연구, 시뮬레이션으로 언어 모델을 접지하는 구조, 에이전트가 구성을 바꿔 비교 실험을 돌리는 연구를 함께 보면 이 영역의 기능은 언어 모델이 인터페이스와 실험 설계를 맡고 수치 결론은 시뮬레이션 실행에서 얻는 구조로 수렴한다. [추정][^ref-836][^ref-824][^ref-832]

```mermaid
flowchart LR
  Records["플릿 실행 기록 또는 대화 설명"] --> Spec["시나리오 사양"]
  Spec --> Engine["시뮬레이션 엔진(연계 대상)"]
  Engine --> Trace["재현 사건 트레이스"]
  Trace --> Compare["실제 기록과 대조·불일치 진단"]
  Compare --> Explain["대화로 차이 설명"]
  Explain --> Approve["사람 확인·승인"]
```

### 대화에서 실행 가능한 시뮬레이션 모델 만들기

Elbasheer 외는 대규모 언어 모델과 자동 시뮬레이션 모델 생성을 결합해 의도 표현, 템플릿 기반 지식 추출, 객체지향 데이터 기반 구성요소로 모델 구성, 실행·결과 분석의 4단계로 자연어 대화에서 제조 시스템 시뮬레이션 모델을 만들었고, 18개 동작 유형을 지원하며 응답 시간이 단순 동작 8초에서 전체 시스템 생성 5분까지라고 보고했다. [사실][^ref-836] Kleiman 외의 Simulation Agent 프레임워크는 시뮬레이션이 언어 모델의 답을 실제 시스템의 구조적 표현에 접지시키고, 언어 모델은 비전문가가 복잡한 시뮬레이터를 대화로 다루게 하는 인터페이스가 되는 결합 구조를 제안하며 초록에는 정량 평가가 없다. [사실][^ref-824]

### 언어 모델 에이전트의 비교 실험

Xia 외는 [LLM 에이전트](../../glossary/llm-agent.md)들이 사용자 질의와 기준 구성에서 구조화 과제 표현을 만들고 실험을 설계해 매개변수 구성을 나란히 시뮬레이션한 뒤 결과를 해석해 권고를 내는 다중 에이전트 프레임워크를 제약 공정 설계에 적용했고, 언어만 쓰는 방식보다 출력 구체성과 사용자 평가 정확도·유용성이 높았다고 절제 실험과 사례로 보고했다. [사실][^ref-832] 적용 대상이 제약 공정 설계라는 비로봇 도메인이므로, 이 연구는 로봇 플릿 적용 근거가 아니라 대화로 조건을 바꿔 비교 실험을 돌리는 방법의 선례로만 본다.

### 사양·기록에서 시뮬레이터를 만들고 트레이스로 대조하기

Chen 외는 자연어 환경 사양에서 이산 사건 시스템 명세(Discrete Event System Specification, DEVS) 형식의 이산 사건 시뮬레이터를 생성하되 구성요소 상호작용의 구조 추론과 구성요소별 사건·타이밍 논리 생성을 단계로 나누고, 생성된 시뮬레이터가 내는 구조화 사건 트레이스를 사양에서 도출한 시간·인과·의미 제약과 대조해 검증하는 벤치마크를 제안했다. [사실][^ref-825] Camargo·Dumas·González-Rojas 는 이벤트 로그에서 프로세스 모델을 자동 발견하고 매개변수를 추출해 시뮬레이션 모델을 만들되, 하이퍼파라미터 최적화로 시뮬레이션 행동과 로그에서 관측된 행동의 유사도를 최대화하는 방법을 Simod 도구로 구현하고 여러 도메인 로그로 평가했다. [사실][^ref-828] 두 방법을 보면 이 영역의 운영 기록을 지정하면 재현하는 일과 재현 충실도 확인은 기록에서 모델·매개변수를 뽑아 돌린 뒤 재현 트레이스와 실제 기록의 사건 순서·시각 유사도를 재는 흐름으로 구현할 수 있을 것으로 보인다. [추정][^ref-828][^ref-825]

### 재현 충실도 확인과 불일치 진단

Ghasemloo·Eckman·Li 는 서브트레이스 조건부 검증을 제안하고, 어느 입력 모델이 실제와의 불일치를 만드는지 진단하는 도구를 M/M/1 과 직렬 대기행렬 디지털 트윈 사례로 보였다. [사실][^ref-826] 이 진단 방식을 보면 맞지 않는 부분을 알려 주는 기능은 도착·처리 시간·고장 같은 입력 모델 가운데 어느 것이 실제 기록과 어긋나는지를 통계 절차로 짚어 대화로 설명하는 방식으로 뒷받침될 수 있을 것으로 보이나, 로봇 플릿 적용 사례는 확인되지 않았다. [추정][^ref-826]

### 텍스트 기록에서 시나리오 재구성 — 자율주행 시험 도구의 선례

다음 세 연구는 로봇 오케스트레이션 현장 사례가 아니라 차량 소프트웨어 시험 도구이며, 텍스트 기록에서 실제 상황을 시뮬레이션으로 재현하는 방법의 선례로만 본다. SoVAR 는 언어 모델 프롬프트로 사고 보고서 텍스트에서 사고 정보를 추출하고 제약을 풀어 차량 궤적을 생성해 여러 지도 구조에 사고 시나리오를 재구성하며, 미국 도로교통안전국(National Highway Traffic Safety Administration, NHTSA) 사고 보고서로 Baidu Apollo 를 시험해 5종의 안전 위반을 찾았고, 보고서 정보와 시뮬레이션 지도의 대응이 어렵고 정보 추출 정확도가 제한적이라는 한계를 밝혔다. [사실][^ref-834] OmniTester 는 멀티모달 언어 모델에 프롬프트 설계, SUMO 교통 시뮬레이터 연동, 검색 증강 생성과 자기 개선을 결합해 시험 시나리오를 만들며 실제 사고 보고서에서 추출한 시나리오를 재구성하고 현실성·제어 가능성을 검증했다. [사실][^ref-835] 서로 다른 두 연구 그룹이 각각 사고 보고서 텍스트에서 시나리오를 재구성해 시뮬레이터에서 재현하는 방법을 보고해, 이 접근은 한 곳 이상에서 확인된다. [사실][^ref-834][^ref-835]

Chat2Scenic 은 규정 문서를 대화형 인터페이스와 도메인 특화 언어 지식의 검색 증강 생성으로 반복 정제해 Scenic 시나리오로 바꾸며, 123개 시나리오에서 컴파일 성공 76.42%, 프레임워크 정확도 58.17%를 보고했다. [사실][^ref-833] 이 세 연구가 보고한 정확도 한계가 3. 왜 중요한가 절에서 말한 사람 확인과 기록 우선 판단의 근거다. [추정][^ref-834][^ref-835][^ref-833]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-824]: Kleiman, J., Frank, K., Voyles, J., & Campagna, S., Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making, 2025-05-19 (v1; v2 2025-05-21), https://arxiv.org/abs/2505.13761, 접근일 2026-09-29
[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-826]: Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins, 2026-07-19, https://arxiv.org/abs/2607.17088, 접근일 2026-09-29
[^ref-828]: Camargo, M., Dumas, M., & González-Rojas, O., Automated Discovery of Business Process Simulation Models from Event Logs (Decision Support Systems (2020) 게재, arXiv 판), 2020, https://arxiv.org/abs/1910.05404, 접근일 2026-09-29
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-09-29
[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-09-29
[^ref-834]: Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024), SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing, 2024-09-12, https://arxiv.org/abs/2409.08081, 접근일 2026-09-29
[^ref-835]: Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S., Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles, 2024-09-10, https://arxiv.org/abs/2409.06450, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s8.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 연구와 자료"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-825, ref-826, ref-827, ref-828, ref-829, ref-830, ref-832, ref-836, ref-837, ref-838]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#8
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 연구와 자료

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Elbasheer 외, Natural language-driven production planning(2025, Journal of Intelligent Manufacturing) — 자연어 대화에서 실행 가능한 제조 시뮬레이션 모델을 만드는 4단계 방법. 이 영역의 대화로 재현하는 일에 가장 가까운 방법이나 원문은 열지 못했다. [사실][^ref-836]
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Elbasheer 외, Natural language-driven production planning(2025, Journal of Intelligent Manufacturing) — 자연어 대화에서 실행 가능한 제조 시뮬레이션 모델을 만드는 4단계 방법. 이 영역의 대화로 재현하는 일에 가장 가까운 방법이나 원문은 열지 못했다. [사실][^ref-836]
- Xia 외, LLM Agents Perform Controlled Experiments Using Simulation Models(2026) — 에이전트가 실험을 설계해 구성을 나란히 시뮬레이션하고 해석하는 프레임워크. 비로봇 도메인의 선례다. [사실][^ref-832]
- Chen 외, Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism(2026) — 사양에서 시뮬레이터를 만들고 사건 트레이스를 제약과 대조하는 벤치마크. 재현 충실도 확인의 방법 근거다. [사실][^ref-825]
- Camargo·Dumas·González-Rojas, Automated Discovery of Business Process Simulation Models from Event Logs(2020, Decision Support Systems) — 로그에서 시뮬레이션 모델을 발견하고 유사도로 조정하는 방법. 운영 기록 지정 재현의 선례다. [사실][^ref-828]
- Ghasemloo·Eckman·Li, Subtrace-Conditional Validation of Simulation Models and Digital Twins(2026) — 관측 트레이스 일부를 고정한 조건부 검증과 불일치 원인 진단. [사실][^ref-826]
- Yang 외, Leveraging Large Language Models for Enhanced Digital Twin Modeling(2025) — 기술–예측–처방 프레임워크로 언어 모델 디지털 트윈 연구를 정리하고 자동 모델링·최적화를 보이는 기업 디지털 트윈 시스템을 제시한 서베이. [사실][^ref-827]
- Woo, J., Shin, H., Jeon, C., & Park, S., Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber(2025, Electronics) — 한국 병원의 감염병 환자 이송 침대 로봇 연합 디지털 트윈 시뮬레이션 검증. [사실][^ref-837]
- 이동건·송승현·이찬혁·노상도·윤상문·이현영, 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용(2021, 한국CDE학회 논문집) — 국내 제조업체 무인운반차(Automated Guided Vehicle, AGV) 자동물류시스템에 적용한 설계 검증·운영 모니터링 디지털트윈. [사실][^ref-830]
- Valiollahi 외, Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts(2026, Scientific Reports) — 이기종 로봇 플릿·공정·배치 시나리오 비교. [사실][^ref-838]
- Sieve 외, BedreFlyt(2025, 오슬로대) — 형식 모델·온톨로지·충족 가능성 모듈로 이론(Satisfiability Modulo Theories, SMT) 해결기를 결합한 병원 병동 디지털 트윈의 what-if 시나리오 구성 방식. [사실][^ref-829]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-826]: Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins, 2026-07-19, https://arxiv.org/abs/2607.17088, 접근일 2026-09-29
[^ref-827]: Yang, L., Luo, S., Cheng, X., & Yu, L., Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges, 2025-03-04, https://arxiv.org/abs/2503.02167, 접근일 2026-09-29
[^ref-828]: Camargo, M., Dumas, M., & González-Rojas, O., Automated Discovery of Business Process Simulation Models from Event Logs (Decision Support Systems (2020) 게재, arXiv 판), 2020, https://arxiv.org/abs/1910.05404, 접근일 2026-09-29
[^ref-829]: Sieve, R., Kobialka, P., Slaughter, L., Schlatte, R., Johnsen, E. B., & Tapia Tarifa, S. L. (University of Oslo), BedreFlyt: Improving Patient Flows through Hospital Wards with Digital Twins, 2025-05-07, https://arxiv.org/abs/2505.06287, 접근일 2026-09-29
[^ref-830]: 이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4)), 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용, 2021-12, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861, 접근일 2026-09-29
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)
[^ref-837]: Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24)), Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins, 2025-12-17, https://www.mdpi.com/2079-9292/14/24/4954, 접근일 2026-09-29 (원문 미열람)
[^ref-838]: Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports), Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts, 2026-07-18, https://www.nature.com/articles/s41598-026-57316-5, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s4.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 핵심 개념과 용어"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-825, ref-826, ref-828, ref-831, ref-834, ref-836]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#4
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 핵심 개념과 용어

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **자동 시뮬레이션 모델 생성(Automatic Simulation Model Generation, ASMG)** — 사람이 시뮬레이션 도구를 직접 다루지 않고 데이터·사양·자연어 설명에서 실행 가능한 시뮬레이션 모델을 자동으로 만드는 기법이다. Elbasheer 외는 대규모 언어 모델과 결합해 자연어 대화에서 제조 시스템 시뮬레이션 모델을 직접 만들었다. [사실][^ref-836]
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **자동 시뮬레이션 모델 생성(Automatic Simulation Model Generation, ASMG)** — 사람이 시뮬레이션 도구를 직접 다루지 않고 데이터·사양·자연어 설명에서 실행 가능한 시뮬레이션 모델을 자동으로 만드는 기법이다. Elbasheer 외는 대규모 언어 모델과 결합해 자연어 대화에서 제조 시스템 시뮬레이션 모델을 직접 만들었다. [사실][^ref-836]
- **사건 트레이스(Event Trace)** — 시스템이나 시뮬레이터가 실행 중에 낸 사건을 시각 순서대로 기록한 구조화 목록이다. 생성된 시뮬레이터가 내는 트레이스를 사양에서 도출한 시간·인과·의미 제약과 대조해 검증하는 데 쓴다. [사실][^ref-825]
- **시나리오 재구성(Scenario Reconstruction)** — 사고 보고서·운영 기록 같은 실제 상황의 기록에서 정보를 추출해 시뮬레이터에서 다시 실행할 수 있는 시나리오로 만드는 일이다. 언어 모델 프롬프트로 정보를 뽑고 제약을 풀어 궤적을 만드는 방식이 자율주행 시험에서 보고됐다. [사실][^ref-834]
- **로그 기반 시뮬레이션 모델 발견** — 정보시스템 이벤트 로그에서 프로세스 모델을 자동 발견하고 시뮬레이션 매개변수를 추출해 모델을 만들되, 시뮬레이션 행동과 로그에서 관측된 행동의 유사도를 최대화하도록 조정하는 [프로세스 마이닝](../../glossary/process-mining.md)의 한 갈래다. [사실][^ref-828]
- **서브트레이스 조건부 검증(Subtrace-Conditional Validation)** — 시뮬레이션 모델을 관측된 시스템 상태에서 반복 초기화하고 일부 확률 입력을 실제 관측값으로 고정한 채 나머지를 시뮬레이션해, 조건부 출력 분포에 적합도 검정을 하는 [시뮬레이션 모델 검증·타당성 확인](../../glossary/verification-and-validation-of-simulation-models.md) 방법이다. [사실][^ref-826]
- **백 파일(Bag File, rosbag2)** — ROS 2 에서 토픽 메시지를 시각과 함께 저장한 기록 파일로, 재생 속도·시작 시점·토픽 선택·반복 옵션으로 재생하며 MCAP·SQLite3 저장 형식을 지원한다. [사실][^ref-831]

이 영역이 기대는 [이산 사건 시뮬레이션](../../glossary/discrete-event-simulation.md), [현실 격차](../../glossary/reality-gap.md), [가상 시운전](../../glossary/virtual-commissioning.md)은 용어집에 있는 정의를 따른다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-826]: Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins, 2026-07-19, https://arxiv.org/abs/2607.17088, 접근일 2026-09-29
[^ref-828]: Camargo, M., Dumas, M., & González-Rojas, O., Automated Discovery of Business Process Simulation Models from Event Logs (Decision Support Systems (2020) 게재, arXiv 판), 2020, https://arxiv.org/abs/1910.05404, 접근일 2026-09-29
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-29
[^ref-834]: Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024), SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing, 2024-09-12, https://arxiv.org/abs/2409.08081, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s10.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 다른 연구영역과의 연결"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-825, ref-826, ref-828, ref-830, ref-832, ref-833, ref-834, ref-835, ref-836, ref-837]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#10
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 다른 연구영역과의 연결

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 원문 주석대로 이 영역의 대화가 부르는 엔진 영역이다. 사양·기록에서 시뮬레이터를 만들고 트레이스로 대조하는 방법은 이 영역과 양쪽에 연결한다. [추정][^ref-836][^ref-825][^ref-832]
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 원문 주석대로 이 영역의 대화가 부르는 엔진 영역이다. 사양·기록에서 시뮬레이터를 만들고 트레이스로 대조하는 방법은 이 영역과 양쪽에 연결한다. [추정][^ref-836][^ref-825][^ref-832]
- [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) — 재현할 상황을 담는 시나리오 사양의 모델이 여기서 온다. 원문 주석의 짝이다.
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 실제 상황 재현은 과거 기록을 가정한 조건으로 다시 실행하는 일이므로 가정한 미래를 실험하는 이 영역 쪽에 둔다. [추정][^ref-830]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 현재 상태를 표현하는 영역이므로 재현에 쓰는 기록의 원천으로만 연결하고 재현 기능과 섞지 않는다. [추정][^ref-830]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 재현의 입력이 되는 플릿 실행 기록을 남기는 영역이다. [추정][^ref-828][^ref-825]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 재현과 실제의 불일치 원인을 짚는 진단이 원인 분석과 이어진다. [추정][^ref-826]
- [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) — 대화에서 시나리오·모델을 만드는 방법을 공유한다. [추정][^ref-836][^ref-825]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 재현 결과를 언어 모델 출력 그대로 쓰지 않고 사람이 확인하는 절차가 여기에 속한다. [추정][^ref-834][^ref-835][^ref-833]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 조건부 검증과 시나리오 생성 정확도 지표가 검증 방법에 해당한다. [추정][^ref-826][^ref-833]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 자연어에서 시뮬레이션 모델을 만들거나 에이전트가 실험을 설계·해석하는 방법은 L. AI·학습 기술의 연구 방법이며, 교차 규칙에 따라 적용 대상 영역과 양쪽에 연결한다. [추정][^ref-836][^ref-825][^ref-832]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 5절의 병원·제조 공장 사례가 속하는 현장 유형이다. [사실][^ref-837][^ref-830]
- 트랙: [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)의 [단계 9. 채팅으로 실제 상황 재현](../../tracks/chat-based-configuration-and-operation/stage-9-chat-real-situation-replay.md)이 이 영역을 중심 영역으로 다룬다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-826]: Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins, 2026-07-19, https://arxiv.org/abs/2607.17088, 접근일 2026-09-29
[^ref-828]: Camargo, M., Dumas, M., & González-Rojas, O., Automated Discovery of Business Process Simulation Models from Event Logs (Decision Support Systems (2020) 게재, arXiv 판), 2020, https://arxiv.org/abs/1910.05404, 접근일 2026-09-29
[^ref-830]: 이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4)), 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용, 2021-12, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861, 접근일 2026-09-29
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-09-29
[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-09-29
[^ref-834]: Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024), SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing, 2024-09-12, https://arxiv.org/abs/2409.08081, 접근일 2026-09-29
[^ref-835]: Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S., Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles, 2024-09-10, https://arxiv.org/abs/2409.06450, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)
[^ref-837]: Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24)), Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins, 2025-12-17, https://www.mdpi.com/2079-9292/14/24/4954, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s3.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 왜 중요한가"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-824, ref-827, ref-832, ref-833, ref-834, ref-835, ref-836]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#3
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 왜 중요한가

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 실제 상황을 시뮬레이션에 되살려 조건을 바꿔 보는 일은, 언어 모델을 [디지털 트윈](../../glossary/digital-twin.md)에 쓰는 연구가 공통으로 꼽는 세 과제인 정확한 모델링을 위한 데이터 부족, 시스템 분석의 비효율, 물리–디지털 상호작용의 설명 부족과 그대로 맞닿아 있다. [사실][^ref-827] 기록에서 모델을 만들고, 대화로 분석을 쉽게 하고, 재현과 실제의 차이를 설명하는 일이 이 영역이 다루는 세 가지 일이다.
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

실제 상황을 시뮬레이션에 되살려 조건을 바꿔 보는 일은, 언어 모델을 [디지털 트윈](../../glossary/digital-twin.md)에 쓰는 연구가 공통으로 꼽는 세 과제인 정확한 모델링을 위한 데이터 부족, 시스템 분석의 비효율, 물리–디지털 상호작용의 설명 부족과 그대로 맞닿아 있다. [사실][^ref-827] 기록에서 모델을 만들고, 대화로 분석을 쉽게 하고, 재현과 실제의 차이를 설명하는 일이 이 영역이 다루는 세 가지 일이다.

혼잡·고장·승강기 대기처럼 현장에서 실제로 있었던 상황을 되살릴 수 없으면, 운영자는 같은 상황이 다시 왔을 때 로봇 수나 정책을 바꾸면 어떻게 됐을지를 추측으로만 판단해야 한다. 2절의 핵심 질문은 이 재현과 조건 비교를 비전문 사용자가 대화만으로 할 수 있는가를 묻는다.

텍스트에서 시나리오를 재구성하는 연구들이 정보 추출 정확도의 한계, 지도 대응의 어려움, 58% 수준의 프레임워크 정확도를 보고하므로, 채팅으로 설명한 상황을 시뮬레이션에 재현한 결과는 언어 모델 출력 그대로 쓰지 말고 사람이 확인해야 하며, 실제 기록(위치·시각·사건)이 있으면 말로 한 설명보다 기록을 우선 입력으로 삼는 것이 맞을 것으로 보인다. [추정][^ref-834][^ref-835][^ref-833] 대화로 조건을 바꿔 비교하는 기능도 언어 모델이 시뮬레이터의 매개변수를 바꿔 실행하고 결과 차이를 설명하는 에이전트 구조로 구현되며, 결론은 언어 모델의 추론이 아니라 시뮬레이션 출력에 근거해야 할 것으로 보인다. [추정][^ref-836][^ref-824][^ref-832]

로봇 플릿의 실제 운영 기록을 대화로 시뮬레이션에 재현한 현장 사례는 이번 조사(2026-09-29 기준)에서 확인되지 않았고, 확인된 것은 연구 프로토타입과 병원·제조 공장의 시뮬레이션 검증·설계 비교 사례뿐이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-824]: Kleiman, J., Frank, K., Voyles, J., & Campagna, S., Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making, 2025-05-19 (v1; v2 2025-05-21), https://arxiv.org/abs/2505.13761, 접근일 2026-09-29
[^ref-827]: Yang, L., Luo, S., Cheng, X., & Yu, L., Leveraging Large Language Models for Enhanced Digital Twin Modeling: Trends, Methods, and Challenges, 2025-03-04, https://arxiv.org/abs/2503.02167, 접근일 2026-09-29
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-09-29
[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-09-29
[^ref-834]: Guo, A., Zhou, Y., Tian, H. 외 (ASE 2024), SoVAR: Building Generalizable Scenarios from Accident Reports for Autonomous Driving Testing, 2024-09-12, https://arxiv.org/abs/2409.08081, 접근일 2026-09-29
[^ref-835]: Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S., Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles, 2024-09-10, https://arxiv.org/abs/2409.06450, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s11.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 열린 질문"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-824, ref-825, ref-826, ref-828, ref-830, ref-832, ref-836, ref-837]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#11
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 열린 질문

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 플릿 운영 기록을 대화로 시뮬레이션에 재현한 현장 사례는 이번 조사(2026-09-29 기준)에서 확인되지 않았으며, 아래 질문은 그 공백에서 나온 것이다. id 는 퍼블리셔가 부여한다.
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 플릿 운영 기록을 대화로 시뮬레이션에 재현한 현장 사례는 이번 조사(2026-09-29 기준)에서 확인되지 않았으며, 아래 질문은 그 공백에서 나온 것이다. id 는 퍼블리셔가 부여한다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-03) 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? [추정][^ref-828][^ref-825]
- (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-03) 재현한 시뮬레이션이 실제 기록과 맞는다고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가? [추정][^ref-826]
- (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-03) 대화로 재현·비교한 시뮬레이션 결과를 근거로 로봇 수·경로·정책을 바꾸는 결정에서 언어 모델의 결과 해석 오류를 막는 검증·승인 절차와 평가 지표는 무엇인가? [추정][^ref-836][^ref-824][^ref-832]
- (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-03) 국내 물류창고·병원에서 로봇 운영 기록으로 혼잡·고장·승강기 대기 같은 실제 상황을 시뮬레이션에 재현한 사례가 있는가(이번 조사에서 확인된 국내 자료는 설계 검증·모니터링용 디지털 트윈과 시나리오 기반 검증뿐이다)? [사실][^ref-830][^ref-837]

트랙 전용 질문은 [채팅 기반 구성·운영 트랙의 질문 백로그](../../tracks/chat-based-configuration-and-operation/question-backlog.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-824]: Kleiman, J., Frank, K., Voyles, J., & Campagna, S., Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making, 2025-05-19 (v1; v2 2025-05-21), https://arxiv.org/abs/2505.13761, 접근일 2026-09-29
[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-826]: Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins, 2026-07-19, https://arxiv.org/abs/2607.17088, 접근일 2026-09-29
[^ref-828]: Camargo, M., Dumas, M., & González-Rojas, O., Automated Discovery of Business Process Simulation Models from Event Logs (Decision Support Systems (2020) 게재, arXiv 판), 2020, https://arxiv.org/abs/1910.05404, 접근일 2026-09-29
[^ref-830]: 이동건, 송승현, 이찬혁, 노상도(성균관대학교), 윤상문, 이현영(LG전자) (한국CDE학회 논문집 26(4)), 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용, 2021-12, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10671861, 접근일 2026-09-29
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-09-29
[^ref-836]: Elbasheer, M., Laili, Y., Longo, F., Solina, V., Tao, Y., Veltri, P., Zhang, Y., & Zhang, L. (Journal of Intelligent Manufacturing), Natural language-driven production planning: integrating large language models with automatic simulation model generation in manufacturing systems, 2025-11-14, https://link.springer.com/article/10.1007/s10845-025-02732-z, 접근일 2026-09-29 (원문 미열람)
[^ref-837]: Woo, J., Shin, H., Jeon, C., & Park, S. (Electronics 14(24)), Design and Application of a Nurse-Following Medical Bed Robot with a Negative Pressure Chamber for Patient Transportation in the Hospital: A Korean Case of Federated Digital Twins, 2025-12-17, https://www.mdpi.com/2079-9292/14/24/4954, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-03/pages/topics/2026/2026-09-29-area11-s7.md

```markdown
---
title: "11. 채팅으로 실제 상황 시뮬레이션 재현 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 11
related_areas: [9, 13, 18, 33, 34, 36, 37, 38, 44, 47, 54, 62, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-825, ref-828, ref-831, ref-833, ref-835]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md#7
---

[홈](../../index.md) › [주제](../index.md) › 11. 채팅으로 실제 상황 시뮬레이션 재현 — 관련 표준·프레임워크·오픈소스

# 11. 채팅으로 실제 상황 시뮬레이션 재현 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준·프레임워크 전체 목록은 [표준 목록](../../standards/index.md)에 있다.
- 이 페이지는 [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준·프레임워크 전체 목록은 [표준 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| rosbag2 | 오픈소스 | ROS 2 통신을 기록·재생하는 공식 도구. record 로 토픽 메시지를 시각과 함께 저장하고 play 로 재생 속도·시작 시점·토픽 선택·반복·/clock 발행 옵션을 두며 MCAP·SQLite3 를 지원한다. [사실][^ref-831] 연계 대상: 로봇 한 대의 센서·제어 메시지를 되살리는 로봇 자체 지능·제어 쪽 도구이며, 이 영역의 플릿 수준 재현과는 층이 다르다. [추정][^ref-831] | [^ref-831] |
| 이산 사건 시스템 명세(Discrete Event System Specification, DEVS) 형식 | 프레임워크 | 자연어 사양에서 생성한 이산 사건 시뮬레이터의 표현 형식이며, 사건 트레이스 검증 벤치마크의 바탕이다. [사실][^ref-825] | [^ref-825] |
| Simod | 오픈소스 | 이벤트 로그에서 업무 프로세스 시뮬레이션 모델을 자동 발견하고 로그와의 유사도로 조정하는 도구. [사실][^ref-828] | [^ref-828] |
| SUMO | 오픈소스 | OmniTester 가 시나리오 생성·재구성에 연동한 교통 시뮬레이터. [사실][^ref-835] | [^ref-835] |
| Scenic | 프레임워크 | Chat2Scenic 이 규정 문서를 대화로 정제해 바꾸는 시나리오 기술 언어. [사실][^ref-833] | [^ref-833] |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-825]: Chen, Z., Zhuang, H., Li, Z., & Li, C., Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism, 2026-03-04 (v1; v2 2026-05-21), https://arxiv.org/abs/2603.03784, 접근일 2026-09-29
[^ref-828]: Camargo, M., Dumas, M., & González-Rojas, O., Automated Discovery of Business Process Simulation Models from Event Logs (Decision Support Systems (2020) 게재, arXiv 판), 2020, https://arxiv.org/abs/1910.05404, 접근일 2026-09-29
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-29
[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-09-29
[^ref-835]: Lu, Q., Wang, X., Jiang, Y., Zhao, G., Ma, M., & Feng, S., Multimodal Large Language Model Driven Scenario Testing for Autonomous Vehicles, 2024-09-10, https://arxiv.org/abs/2409.06450, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-03 | 11. 채팅으로 실제 상황 시뮬레이션 재현 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-03/verification2.json

```json
{
  "run_id": "2026-09-29-03",
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
    "overlaps": [
      "참고문헌 id ref-824~ref-830 이 같은 날 이전 실행(2026-09-29-01·-02)의 다른 출처 id 와 겹칠 수 있음 — 1차·직전 2차와 같은 지적이며 퍼블리셔가 URL 기준으로 재부여한다(내용 중복 아님)"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "분리 주제 페이지 docs/topics/2026/2026-09-29-area11-s3.md 3. 본문 둘째 단락의 '2절의 핵심 질문은 이 재현과 조건 비교를 비전문 사용자가 대화만으로 할 수 있는가를 묻는다.': 이 문장은 자동 분리 뒤 주제 페이지에만 남아 '2절'이 그 페이지의 '2. 배경'을 가리키게 된다 — '원 페이지의 2. 핵심 질문 절은'처럼 절 이름을 함께 써서 11. 채팅으로 실제 상황 시뮬레이션 재현 페이지의 절임을 드러낸다(직전 2차 지시 8번과 같은 유형이며, 직전 지시에는 없었던 새 항목이다).",
    "분리 주제 페이지 docs/topics/2026/2026-09-29-area11-s10.md 3. 본문의 '63. 병원·의료, 62. 제조 공장' 항목 '5절의 병원·제조 공장 사례가 속하는 현장 유형이다. [사실][^ref-837][^ref-830]': 자동 분리 뒤 이 문장이 주제 페이지에 놓여 '5절'이 그 페이지의 '5. ROP 관점의 시사점'을 가리키게 된다 — '원 페이지의 5. 적용 사례 (현장 유형 명시) 절의'처럼 절 이름을 함께 써서 원 페이지의 절임을 드러낸다(태그·각주는 유지. 직전 지시에는 없었던 새 항목이다)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 24건, 미확인 0건, 교차 확인 1건(f14: SoVAR·OmniTester 독립 연구 그룹). 강등: 없음. 원문 미열람 출처: ref-836, ref-837, ref-838(발행사 페이지 접근 차단, Semantic Scholar API 초록으로 기관·제목·발행일 일치 확인). 주의: 모든 사실 주장은 논문 초록·공식 저장소 README 확인에 근거한 단일 출처이며 정량 수치(f1 응답 시간, f15 정확도, f20 3.5배)는 저자 보고값이다. 대화만으로 로봇 플릿의 실제 운영 기록을 시뮬레이션에 재현한 현장 사례는 확인되지 않았고, 현장 사례는 병원·제조 공장의 시뮬레이션 검증·설계 비교 사례뿐이다. 자율주행 사고 재구성(f12~f14)은 현장 사례가 아닌 방법 선례로만 쓴다. 참고문헌 id ref-824~ref-830 은 같은 날 이전 실행이 다른 출처에 부여한 id 와 겹칠 수 있으므로 퍼블리셔가 URL 기준으로 재부여해야 한다. 정정 요청 없음. / 2차 수정 후 재검증(재검증 1회차). 직전 2차 지시 8건은 모두 이행됐다: AGV·SMT·DEVS·NHTSA·PLC 첫 등장 풀어 쓰기(5절 사례 제목, 5절 BedreFlyt 단락, 분리 페이지 6·7·8절, 9절 표), 9절 분류 원문 19장 문장 재서술과 따옴표 제거, 6절 시나리오 재구성 단락 2개로 분리(4문장+2문장), 10절 9번·54번 항목 [추정] 전환(각주 유지), 6절 마지막 문장 '3. 왜 중요한가 절' 표기. 드리프트 없음(세부영역 페이지와 분리 주제 페이지 7건의 태그 문장 전부가 브리프 finding·1차 처분·분류 원문·용어집에 대응하고 삭제·이동 처분 finding 없음), [분류원문] 보존(admonition 세 줄·1절·2절이 시드와 글자 단위 일치, auto 마커 내용 시드와 동일), 섹션 순서 준수(세부영역 13절·주제 10절 정본과 일치), 링크 유효(부록 A 경로·용어집 색인과 대조한 세부영역·용어집 링크 모두 유효, 페이지마다 각주 정의와 프런트매터 sources 일치. docs_tree.txt 가 입력에 없어 docs/about/scope-boundary.md, docs/topics/index.md, 트랙 단계 페이지 stage-9-chat-real-situation-replay.md, 트랙 question-backlog.md 의 존재는 이번에도 확인하지 못했다). 새로 남은 지적 2건(직전 지시에 없었던 항목): 분리 주제 페이지 s3 의 '2절의 핵심 질문', s10 의 '5절의 병원·제조 공장 사례'가 자동 분리 뒤 주제 페이지의 다른 절을 가리키므로 절 이름을 함께 쓰도록 수정 지시했다. 참고: 세부영역 페이지 프런트매터 sources 15건이 분리 뒤 본문 각주 11건보다 많은 점과 reference_updates 의 cited_by 가 분리 주제 페이지를 담지 않은 점은 형식 검증 코드·퍼블리셔 자동 영역(reference-cited-pages)이 다루는 항목으로 보아 지적하지 않았다. 신뢰도는 medium 을 유지한다.",
  "retry_reason": null
}
```


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 분리 주제 페이지 docs/topics/2026/2026-09-29-area11-s3.md 3. 본문 둘째 단락의 '2절의 핵심 질문은 이 재현과 조건 비교를 비전문 사용자가 대화만으로 할 수 있는가를 묻는다.': 이 문장은 자동 분리 뒤 주제 페이지에만 남아 '2절'이 그 페이지의 '2. 배경'을 가리키게 된다 — '원 페이지의 2. 핵심 질문 절은'처럼 절 이름을 함께 써서 11. 채팅으로 실제 상황 시뮬레이션 재현 페이지의 절임을 드러낸다(직전 2차 지시 8번과 같은 유형이며, 직전 지시에는 없었던 새 항목이다).
    - 분리 주제 페이지 docs/topics/2026/2026-09-29-area11-s10.md 3. 본문의 '63. 병원·의료, 62. 제조 공장' 항목 '5절의 병원·제조 공장 사례가 속하는 현장 유형이다. [사실][^ref-837][^ref-830]': 자동 분리 뒤 이 문장이 주제 페이지에 놓여 '5절'이 그 페이지의 '5. ROP 관점의 시사점'을 가리키게 된다 — '원 페이지의 5. 적용 사례 (현장 유형 명시) 절의'처럼 절 이름을 함께 써서 원 페이지의 절임을 드러낸다(태그·각주는 유지. 직전 지시에는 없었던 새 항목이다).
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 24건, 미확인 0건, 교차 확인 1건(f14: SoVAR·OmniTester 독립 연구 그룹). 강등: 없음. 원문 미열람 출처: ref-836, ref-837, ref-838(발행사 페이지 접근 차단, Semantic Scholar API 초록으로 기관·제목·발행일 일치 확인). 주의: 모든 사실 주장은 논문 초록·공식 저장소 README 확인에 근거한 단일 출처이며 정량 수치(f1 응답 시간, f15 정확도, f20 3.5배)는 저자 보고값이다. 대화만으로 로봇 플릿의 실제 운영 기록을 시뮬레이션에 재현한 현장 사례는 확인되지 않았고, 현장 사례는 병원·제조 공장의 시뮬레이션 검증·설계 비교 사례뿐이다. 자율주행 사고 재구성(f12~f14)은 현장 사례가 아닌 방법 선례로만 쓴다. 참고문헌 id ref-824~ref-830 은 같은 날 이전 실행이 다른 출처에 부여한 id 와 겹칠 수 있으므로 퍼블리셔가 URL 기준으로 재부여해야 한다. 정정 요청 없음. / 2차 수정 후 재검증(재검증 1회차). 직전 2차 지시 8건은 모두 이행됐다: AGV·SMT·DEVS·NHTSA·PLC 첫 등장 풀어 쓰기(5절 사례 제목, 5절 BedreFlyt 단락, 분리 페이지 6·7·8절, 9절 표), 9절 분류 원문 19장 문장 재서술과 따옴표 제거, 6절 시나리오 재구성 단락 2개로 분리(4문장+2문장), 10절 9번·54번 항목 [추정] 전환(각주 유지), 6절 마지막 문장 '3. 왜 중요한가 절' 표기. 드리프트 없음(세부영역 페이지와 분리 주제 페이지 7건의 태그 문장 전부가 브리프 finding·1차 처분·분류 원문·용어집에 대응하고 삭제·이동 처분 finding 없음), [분류원문] 보존(admonition 세 줄·1절·2절이 시드와 글자 단위 일치, auto 마커 내용 시드와 동일), 섹션 순서 준수(세부영역 13절·주제 10절 정본과 일치), 링크 유효(부록 A 경로·용어집 색인과 대조한 세부영역·용어집 링크 모두 유효, 페이지마다 각주 정의와 프런트매터 sources 일치. docs_tree.txt 가 입력에 없어 docs/about/scope-boundary.md, docs/topics/index.md, 트랙 단계 페이지 stage-9-chat-real-situation-replay.md, 트랙 question-backlog.md 의 존재는 이번에도 확인하지 못했다). 새로 남은 지적 2건(직전 지시에 없었던 항목): 분리 주제 페이지 s3 의 '2절의 핵심 질문', s10 의 '5절의 병원·제조 공장 사례'가 자동 분리 뒤 주제 페이지의 다른 절을 가리키므로 절 이름을 함께 쓰도록 수정 지시했다. 참고: 세부영역 페이지 프런트매터 sources 15건이 분리 뒤 본문 각주 11건보다 많은 점과 reference_updates 의 cited_by 가 분리 주제 페이지를 담지 않은 점은 형식 검증 코드·퍼블리셔 자동 영역(reference-cited-pages)이 다루는 항목으로 보아 지적하지 않았다. 신뢰도는 medium 을 유지한다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
