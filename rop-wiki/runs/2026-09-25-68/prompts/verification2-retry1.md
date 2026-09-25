(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-68
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 27. AI·학습·적응과 모델 운영 (G. 안전·보안·지능·거버넌스)
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

### runs/2026-09-25-68/target.json

```json
{
  "run_id": "2026-09-25-68",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 68,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 27,
    "area_name": "27. AI·학습·적응과 모델 운영",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=27"
}
```

### runs/2026-09-25-68/research.json

```json
{
  "run_id": "2026-09-25-68",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 27,
    "area_name": "27. AI·학습·적응과 모델 운영",
    "category": "G. 안전·보안·지능·거버넌스"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음(LLM 에이전트·환각은 용어집에 있으나 등각 예측·AI 관리 시스템·모델 레지스트리 없음)",
    "섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)",
    "섹션 6. 대표 접근법과 기술 비어 있음(트랙 반영 제안 6건 대기)",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음(트랙 반영 제안 8건 대기)",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음(교차 규칙 적용 대상 5·6·13·19·21 연결 필요)",
    "섹션 11. 열린 질문 비어 있음(oq-030 걸려 있음)"
  ],
  "research_questions": [
    "AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]",
    "AI 시스템의 위험 관리·거버넌스를 다루는 표준·법(NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, EU AI Act, 한국 인공지능 기본법)은 무엇을 요구하며 로봇 운영 AI에 어떻게 걸리는가? (섹션 3·7·9 겨냥)",
    "LLM 이 만든 계획·해석을 실행 전에 접지·검증하고 불확실할 때 사람에게 묻는 방법(SayCan, LLM+P, Code as Policies, KnowNo, SafeGate)은 무엇인가? (섹션 4·6·8 겨냥, 트랙 nl-task-chatbot 반영 제안 확인)",
    "창고 다중 로봇 작업 배정에 학습 기반 방법(강화학습)은 어떻게 쓰이며 어떤 성능이 보고되는가? (섹션 6·8·10 겨냥, 교차 규칙상 13. 작업 배정 — MRTA)",
    "운영 중인 학습 모델의 변경·버전·시험·감시를 관리하는 방법과 도구는 무엇인가? (섹션 4·6·7 겨냥)",
    "oq-030 LTAA(arXiv 2512.02810)의 LLM 배정 완료율 77% 주장과 동적 계획법 우위라는 2차 요약 중 어느 쪽이 원문 결과인가?",
    "국내 물류 현장에서 AI 예측·계획을 운영에 쓴 사례와 국내 규제 요구는 무엇인가? (섹션 3·5 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "NIST 는 2023-01-26 AI 위험관리 프레임워크(AI RMF 1.0)를 자율 적용 프레임워크로 발표했으며, 핵심은 거버넌스(Govern)·맵(Map)·측정(Measure)·관리(Manage) 네 기능이고 거버넌스가 나머지 세 기능을 가로지른다.",
      "tag": "사실",
      "source_ids": [
        "ref-734"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NIST AI 100-1(AI RMF 1.0), 2023-01 발표. 네 기능 Govern·Map·Measure·Manage, Playbook 이 하위 범주별 권장 행동을 제공(검색 요약 기준).",
      "as_of": "2023-01-26",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "ISO/IEC 42001:2023 은 AI 시스템을 개발·제공·사용하는 조직이 AI 관리 시스템(AIMS)을 수립·실행·유지·지속 개선하기 위한 요구사항을 정하는 관리 시스템 표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-735"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (검색 요약 기준).",
      "as_of": "2023",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "ISO/IEC 23894:2023 은 ISO 31000 의 위험관리 원칙을 AI 에 맞게 적용한 지침으로, AI 를 개발·배치·사용하는 조직이 위험 평가·처리·감시·검토·기록을 AI 관련 활동에 통합하도록 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-736"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2023-02 발행, ISO 31000 기반 AI 위험관리 지침. 소통, 맥락 설정, 위험 평가·처리, 감시·검토, 기록·보고를 다룸(검색 요약 기준).",
      "as_of": "2023-02",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "한국의 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI 를 고영향 인공지능으로 두어 별도 책무를 부과한다.",
      "tag": "사실",
      "source_ids": [
        "ref-737"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기본법·시행령 2026-01-22 시행, 고영향 인공지능은 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI. 과태료 부과 유예(검색 요약 기준, 법령 원문 미열람).",
      "as_of": "2026-01-22",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I 의 EU 조화 법령(기계류 등)이 적용되는 제품의 안전 구성요소로 쓰이며 제3자 적합성 평가를 받아야 하는 AI 시스템을 고위험 AI 로 분류한다.",
      "tag": "사실",
      "source_ids": [
        "ref-738"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AI 시스템이 부속서 I 조화 법령 대상 제품의 안전 구성요소이고 제3자 적합성 평가가 필요하면 고위험(검색 요약 기준). 적용 시점은 개정 논의가 있어 이번에 확정하지 않음.",
      "as_of": "2024-06-13",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "SayCan 은 LLM 이 상위 지시에 유용한 행동을 고르는 과제 접지(Say)와, 사전 학습된 기술의 가치 함수가 현재 실행 가능성을 판정하는 세계 접지(Can)를 곱해 실행 가능하고 맥락에 맞는 기술만 선택하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-088"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "the LLM (Say) provides a task-grounding ... the learned affordance functions (Can) provide a world-grounding (초록, 검색 요약 기준).",
      "as_of": "2022-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "LLM+P 는 자연어 문제 설명을 LLM 으로 PDDL 파일로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 구조로, 저자는 LLM 단독으로는 대부분 문제에서 실행 가능한 계획도 못 냈으나 LLM+P 는 대부분에서 최적 해를 냈다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-092"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자연어→PDDL→고전 계획기→자연어. 저자 보고: 대부분 문제에서 최적 해, LLM 단독은 실행 가능한 계획도 대부분 실패(벤치마크 도메인 조건, 검색 요약 기준).",
      "as_of": "2023-04",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "KnowNo 는 등각 예측(conformal prediction)으로 LLM 계획기의 불확실성을 보정해, 과제 완수에 통계적 보장을 두면서 후보 행동이 하나로 좁혀지지 않을 때만 사람에게 도움을 요청하게 하며, 모델 미세조정 없이 쓸 수 있다고 저자가 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "conformal prediction 기반으로 과제 완수 통계적 보장과 사람 도움 최소화, 공간·수치·선호 모호성 과제의 시뮬레이션·실로봇 실험(저자 보고, 검색 요약 기준).",
      "as_of": "2023-07",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "Code as Policies 는 코드 생성 LLM 이 자연어 명령과 소수 예시를 받아 인식 출력 처리와 제어 기본 API 호출을 조합한 로봇 정책 코드를 쓰게 하는 방법으로, 사람이 정한 API 범위 안에서 명령을 재조합한다.",
      "tag": "사실",
      "source_ids": [
        "ref-742"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LLM 이 지각 출력(물체 검출기 등)을 처리하고 제어 기본 API 를 매개변수화하는 정책 코드를 few-shot 으로 생성(초록, 검색 요약 기준).",
      "as_of": "2022-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "AmbiK 데이터셋은 모호한 작업과 모호하지 않은 짝 1000쌍(보정 100, 시험 900)에 모호성 유형, 명확화 질문과 답, 작업 계획을 필드로 두어 LLM 의 모호성 탐지·되묻기를 평가하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-354"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1000쌍(보정 100·시험 900), 환경 설명·지시문·모호성 유형·명확화 질문과 답·작업 계획 필드. 주방 환경 조건 (재인용: 2026-09-25-62)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Wang 외(Learning to Ask)는 도구 호출 LLM 에이전트가 불완전한 지시에서 빠진 인자를 지어내는 문제를 다루고, 불명확 지시 벤치마크 NoisyToolBench 와 필요할 때 되묻는 방법(Ask-when-Needed)을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-359"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ToolBench 정상 표본 200건을 불완전 지시로 변형, 정확도와 되묻기 효율을 자동 평가 (재인용: 2026-09-25-62)",
      "as_of": "2024-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "Lang2LTL 연구는 자연어 명령을 선형 시간 논리(LTL) 식으로 바꿔 접지하는 방법과, LTL 식 템플릿에서 나온 식에 영어 발화를 대응시킨 말뭉치를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-056"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "47개 템플릿·2,125개 LTL 식에 약 5만 발화 대응(저자 보고, 판에 따라 수치 차이 가능) (재인용: 2026-09-25-62)",
      "as_of": "2023-02",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "LoTa-Bench 는 언어 기반 작업 계획기의 성능을 시뮬레이터(AI2-THOR 기반 ALFRED, VirtualHome 기반 Watch-And-Help 확장)의 성공률로 자동 정량화하는 벤치마크다.",
      "tag": "사실",
      "source_ids": [
        "ref-541"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "가정 서비스 에이전트 언어 기반 계획 성능을 자동 정량화, 두 환경 쌍에서 성공률 비교 (재인용: 2026-09-25-62)",
      "as_of": "2024-02",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "SafeGate 는 자연어 작업 명령에서 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람 확인 요청·거부를 정하고, 승인된 작업을 불변 조건·가드·중단 조건의 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 13482 근거 안전 속성 추출, 승인/확인 요청/거부, 작업 안전 계약. 평가는 저자 보고, 개인 돌봄 로봇 표준 기반 (재인용: 2026-09-25-63)",
      "as_of": "2026-04",
      "flow_step": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "RTAW 는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 정식화하고 주의(attention) 기반 정책을 PPO 로 학습해 총 이동 지연을 줄이며, 저자는 500개 작업에서 탐욕·후회 기반 기준 대비 최대 10% 개선과 로봇·작업 수에 독립적인 정책 크기를 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-743"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "global embeddings independent of the number of robots/tasks; 500 tasks 기준 최대 10%(25~1000초) 개선, ICRA 2023(저자 보고, 시뮬레이션 창고 조건, 검색 요약 기준).",
      "as_of": "2022-09",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "Sculley 외(NeurIPS 2015)는 실제 ML 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성, 설정 문제, 외부 세계 변화 같은 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-744"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ML-specific risk factors: boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, changes in the external world(검색 요약 기준).",
      "as_of": "2015",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "Breck 외의 ML Test Score(IEEE Big Data 2017)는 데이터·모델·인프라 시험과 감시를 1급 관심사로 두는 28개 시험·감시 항목으로 ML 시스템의 운영 준비도를 점수화하는 기준표를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-745"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "28 specific tests and monitoring needs ... production readiness 점수화(검색 요약 기준).",
      "as_of": "2017",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "오픈소스 MLflow 의 모델 레지스트리는 등록 모델마다 버전·별칭·태그와 계보(어느 실험·실행이 만들었는지)를 관리하며, 운영 대상 버전에 별칭(예: champion)을 붙이고 별칭을 다른 버전으로 옮겨 운영 모델을 교체하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-746"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "model lineage, model versioning, model aliasing ... reassigning the champion alias to a different model version(공식 문서, 검색 요약 기준).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-747"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 기업이 밝힌 적용 효과를 기사가 전한 것으로 수치·검증 조건 미확인(기사, 검색 요약 기준).",
      "as_of": "2026-09-19",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "분류 원문 질문과 관련해, 확인한 접근을 종합하면 AI 가 만든 계획·해석을 실행에 쓰는 기준은 (1) 실행 가능성 접지(SayCan), (2) 형식 명세·계획기 경유 검증(LLM+P, Lang2LTL), (3) 불확실할 때 사람 확인(KnowNo, Ask-when-Needed), (4) 실행 전 안전 판정(SafeGate), (5) 승인된 모델 버전·시험 기준(ML Test Score, 모델 레지스트리, ISO/IEC 42001)의 겹 구조로 정리될 수 있어 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-088",
        "ref-092",
        "ref-056",
        "ref-351",
        "ref-359",
        "ref-417",
        "ref-745",
        "ref-746",
        "ref-735"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 출처가 서로 다른 단계(접지·검증·확인·안전 판정·모델 관리)를 다루며, 이를 하나의 채택 기준으로 묶은 것은 이 위키의 종합이다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "피킹 단계에서 관리자가 '오늘 마감 주문을 B구역부터 피킹'처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-092",
        "ref-351",
        "ref-354"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "LLM+P 의 형식 변환·계획기 검증과 KnowNo·AmbiK 의 모호성 확인을 물류 피킹 지시에 옮긴 가상 시나리오(출처는 가정·주방·벤치마크 환경).",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려면 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고, 교체 전 시험·감시 기준을 통과시켜야 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-746",
        "ref-745",
        "ref-743",
        "ref-744"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "별칭 재지정으로 운영 모델 교체(MLflow), 운영 준비도 시험(ML Test Score), 외부 세계 변화 위험(Sculley)을 학습 배차(RTAW 유형)에 적용한 가상 시나리오.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "ROP 가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리이고, 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 이를 둘러싼 운영 틀로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-735",
        "ref-734",
        "ref-736",
        "ref-351",
        "ref-746"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 9장 경계(로봇 자체 지능·제어는 연계)에 비추어 이 위키가 나눈 범위 판단이다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "연계 대상: 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(Code as Policies 의 저수준 정책 코드, SayCan 의 사전 학습 기술)과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP 는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-742",
        "ref-088"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 9장: 센서 인식·파지·모터 제어는 로봇 쪽, 수요예측은 상위 업무 시스템 쪽 연계 대상.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "27. AI·학습·적응과 모델 운영의 방법은 교차 규칙에 따라 학습 기반 배차로 13. 작업 배정 — MRTA(RTAW), 실행 전 안전 판정과 제품 안전 구성요소 규제로 25. 안전·위험 관리(SafeGate, EU AI Act), 사람 확인 요청으로 18. 사람–로봇 협업·운영 인터페이스(KnowNo), 모델 버전·변경으로 24. 자산·소프트웨어 수명주기 관리, 평가 벤치마크로 23. 시험·형식 검증·벤치마크(LoTa-Bench)와 맞물리는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-743",
        "ref-417",
        "ref-738",
        "ref-351",
        "ref-746",
        "ref-541"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 출처가 다루는 기능을 분류 원문 영역에 대응시킨 이 위키의 판단. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-734",
      "org": "NIST",
      "title": "NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence",
      "published": "2023-01-26",
      "url": "https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. NIST AI RMF 1.0(NIST AI 100-1) 발표문. 네 기능 Govern·Map·Measure·Manage.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-735",
      "org": "ISO/IEC",
      "title": "ISO/IEC 42001:2023 - AI management systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/42001",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AI 관리 시스템(AIMS)의 수립·실행·유지·개선 요구사항 표준 소개 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-736",
      "org": "ISO/IEC",
      "title": "ISO/IEC 23894:2023 - AI — Guidance on risk management",
      "published": "2023-02",
      "url": "https://www.iso.org/standard/77304.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 31000 을 AI 에 적용한 위험관리 지침 소개 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-737",
      "org": "국가법령정보센터(과학기술정보통신부)",
      "title": "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법",
      "published": null,
      "url": "https://www.law.go.kr/lsInfoP.do?lsiSeq=268543",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국 인공지능 기본법 법령 본문. 고영향 인공지능 정의와 사업자 책무, 2026-01-22 시행(검색 요약 기준).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-738",
      "org": "European Commission",
      "title": "AI Act | Shaping Europe's digital future",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Regulation (EU) 2024/1689(AI Act)의 위험 기반 규제와 고위험 AI 분류 안내 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-088",
      "org": "Ahn, M. 외",
      "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
      "published": "2022-04",
      "url": "https://arxiv.org/abs/2204.01691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SayCan: LLM 과제 접지와 기술 가치 함수의 세계 접지를 결합한 로봇 계획.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-092",
      "org": "Liu, B. 외",
      "title": "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency",
      "published": "2023-04",
      "url": "https://arxiv.org/abs/2304.11477",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어를 PDDL 로 바꿔 고전 계획기로 푸는 LLM+P 프레임워크.",
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
      "summary": "원문 미열람. KnowNo: 등각 예측으로 LLM 계획기의 불확실성을 보정해 필요할 때만 사람에게 묻는 방법.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-742",
      "org": "Liang, J. 외",
      "title": "Code as Policies: Language Model Programs for Embodied Control",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.07753",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 코드 생성 LLM 이 인식·제어 API 를 조합한 로봇 정책 코드를 쓰는 방법.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-743",
      "org": "Agrawal, A. 외",
      "title": "RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.05738",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 다중 로봇 작업 배정의 주의 기반 강화학습(ICRA 2023).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-744",
      "org": "Sculley, D. 외",
      "title": "Hidden Technical Debt in Machine Learning Systems",
      "published": "2015",
      "url": "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ML 시스템 고유의 기술 부채와 위험 요인(NeurIPS 2015).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-745",
      "org": "Breck, E. 외 (Google Research)",
      "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
      "published": "2017",
      "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 28개 시험·감시 항목으로 ML 운영 준비도를 점수화하는 기준표(IEEE Big Data 2017).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-746",
      "org": "MLflow (Linux Foundation 오픈소스 프로젝트)",
      "title": "ML Model Registry | MLflow AI Platform",
      "published": null,
      "url": "https://mlflow.org/docs/latest/ml/model-registry/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모델 버전·별칭·태그·계보를 관리하는 MLflow 모델 레지스트리 공식 문서.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-747",
      "org": "머니투데이",
      "title": "포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI'",
      "published": "2026-09-19",
      "url": "https://www.mt.co.kr/industry/2026/09/19/2026091818023697394",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국내 물류기업의 로봇·AI 적용 사례 기사(한진 적재량 예측, CJ대한통운 포장 로봇 등).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-354",
      "org": "cog-model (AmbiK 저자)",
      "title": "AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment)",
      "published": null,
      "url": "https://github.com/cog-model/AmbiK-dataset",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모호 작업 데이터셋 AmbiK 공식 저장소 README(이번 실행에서 다시 열지 않음).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-359",
      "org": "Wang, W. 외",
      "title": "Learning to Ask: When LLM Agents Meet Unclear Instruction",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.00557",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 불명확 지시 벤치마크 NoisyToolBench 와 Ask-when-Needed.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-056",
      "org": "Liu, J. X. 외",
      "title": "Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments",
      "published": "2023-02",
      "url": "https://arxiv.org/abs/2302.11649",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Lang2LTL: 자연어 명령을 LTL 로 바꿔 접지하는 방법과 말뭉치.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-541",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "title": "LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README)",
      "published": null,
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 언어 기반 작업 계획기 자동 평가 벤치마크 LoTa-Bench 공식 저장소(이번 실행에서 다시 열지 않음).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-417",
      "org": "arXiv (SafeGate 저자, 저자명 미확인)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 명령의 실행 전 안전 판정과 작업 안전 계약 SafeGate.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
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
      "rationale": "seed 페이지 3~11절 첫 작성. 3절: f20(분류 원문 질문, 추정), f4·f5(국내외 규제 맥락), f16 / 4절: f8(등각 예측), f2(AIMS), f18(모델 레지스트리), f6(접지) / 5절: f21(피킹·시작 조건), f22(출하·예외·성과), f19(출하, 벤더 주장 병기) / 6절: f6·f7·f9·f8·f11·f14(LLM 계획 접지·검증·되묻기·안전 판정 — 트랙 nl-task-chatbot 반영 제안 2026-09-25-04·21·30·37 확인분), f15(학습 기반 배차), f16·f17·f18(모델 운영) / 7절: f1·f2·f3·f4·f5, f18 / 8절: f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17(트랙 반영 제안 2026-09-25-04·30·62 확인분) / 9절: f23(직접), f24('연계 대상') / 10절: f25와 교차 규칙 원문(5. 로봇 능력·작업 온톨로지, 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석) / 11절: oq-030 유지와 open_questions_new 3건. 다음 실행 후보: 도면 해석(2026-09-25-05·36·54)과 매뉴얼 추출(2026-09-25-57) 반영 제안, LLM 다중 로봇 서베이·ROSA·RAI(2026-09-25-21)는 출처 메타데이터가 입력에 없어 이번 브리프에서 재확인하지 못함"
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "등각 예측",
      "term_en": "Conformal Prediction",
      "definition": "보정 데이터로 예측 집합의 크기를 정해, 정답이 집합에 들어갈 확률을 사용자가 정한 수준 이상으로 통계적으로 보장하는 불확실성 정량화 방법이다."
    },
    {
      "term_ko": "AI 관리 시스템",
      "term_en": "Artificial Intelligence Management System (AIMS)",
      "definition": "조직이 AI 의 책임 있는 개발·제공·사용을 위한 정책·목표·프로세스를 세우고 운영하는 관리 체계로, ISO/IEC 42001 이 요구사항을 정한다."
    },
    {
      "term_ko": "고영향 인공지능",
      "term_en": "High-impact AI (Korea AI Basic Act)",
      "definition": "한국 인공지능 기본법에서 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있어 별도 책무가 부과되는 영역의 AI 시스템이다."
    },
    {
      "term_ko": "모델 레지스트리",
      "term_en": "Model Registry",
      "definition": "학습된 모델의 버전·별칭·태그·계보를 한곳에서 관리해 어떤 버전을 운영에 쓰는지 정하고 교체·되돌림을 추적하게 하는 저장소다."
    }
  ],
  "open_questions_new": [
    "물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f4 | 종류: 일반",
    "LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 25. 안전·위험 관리 | 근거: f5 | 종류: 일반",
    "KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? | 관련 영역: 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f8 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음(단일 출처 또는 종합 추정)",
      "oq-030 LTAA 출처 충돌 미조사: 예산 배분상 이번 실행에서 원문 결과 확인 못 함(미해결 유지)",
      "f5 EU AI Act 고위험 적용 시점은 개정 논의로 요약 간 차이가 있어 넣지 않음",
      "f4 인공지능 기본법 고영향 영역 목록과 개정 법률 시행일(2026-07-21 언급) 원문 미확인",
      "f15 RTAW 개선 수치는 저자 보고, 원문 미열람",
      "f19 한진 사례의 수치·검증 조건 미확인(기사, 벤더 주장)",
      "ref-737·ref-738·ref-746·ref-354·ref-541 발행일 미확인",
      "현대자동차·마키나락스 로봇 고장 예측 사례는 검색 요약에만 있고 출처 기사를 특정하지 못해 넣지 않음"
    ],
    "scope_violations": [
      "f24: 저수준 정책·파지 학습과 수요예측은 분류 원문 9장 로봇 자체 지능·제어, 상위 업무 시스템 쪽이라 '연계 대상:'으로 표시",
      "f19: 간선차량 상·하차 시점 예측은 거점 간 운송과 맞닿아 있어 입출고 시간·접안 동기화 범위로만 제안",
      "f14: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 적용은 추정으로만 서술하도록 제안"
    ],
    "budget_used": {
      "queries": 12,
      "sources": 14
    },
    "limits": "재실행 1회차. 반려 사유 1(finding f8 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 다시 작성했다(검색 12회/30). 이번 브리프의 f8 은 KnowNo 논문(ref-351) 근거이며 벤더 문서가 아니다. 벤더·기업 주장은 f19 한 건뿐이고 vendor_claim: true, 태그 추정, evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다. 벤더 문서만 근거로 한 [사실] finding 은 없다. web_fetch_available: false · fetch_mode mirror_only: 이번 출처는 GitHub 공식 저장소 미러가 없어 모두 원문 미열람(fetched false, 신뢰도 상한 medium). 신규 출처 14건(ref-734~ref-747, 예약 구간 안), 재사용 5건(ref-354·ref-359·ref-056·ref-541·ref-417, 참고문헌 목록 요약이 입력에 없어 이전 브리프 표의 값 사용, 신뢰도는 high 금지 규칙으로 medium). 트랙 반영 제안 15건 중 LLM 접지·검증·불확실성·안전 판정·평가 벤치마크 관련(2026-09-25-04·30·37·62 일부)은 f6~f14 로 확인했고, 도면 해석(2026-09-25-05·36·54)·매뉴얼 추출(2026-09-25-57)·LLM 다중 로봇 서베이(2026-09-25-21) 제안은 출처 메타데이터가 입력에 없고 예산 배분상 재확인하지 못해 '다음 실행 후보'로 남겼다. 교차 규칙: 학습 배차는 13. 작업 배정 — MRTA 와 양쪽 연결(f15·f25). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 한국 자료: 인공지능 기본법(ref-737), 국내 물류 AI 기사(ref-747). 정정 요청 없음."
  }
}
```

### runs/2026-09-25-68/verification.json

```json
{
  "run_id": "2026-09-25-68",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검색 결과에 nist.gov 뉴스 URL·제목과 AI RMF 1.0 자율 적용 지침(2023-01-26) 발표가 확인됨. 네 기능 Govern·Map·Measure·Manage 는 다른 검색 결과(NIST AI 100-1 등)로 확인됨. '거버넌스가 나머지 세 기능을 가로지른다'는 이번 스니펫에서 확인되지 않아 수정 지시 대상. 브리프에 교차 출처가 없어 cross_checked false."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. iso.org/standard/42001 검색 결과 일치, AIMS 수립·실행·유지·지속 개선 요구사항 표준으로 확인."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. iso.org/standard/77304.html 검색 결과 일치. 2023-02 발행, ISO 31000 을 AI 에 적용한 지침, 소통·맥락 설정·위험 평가·처리·감시·검토·기록·보고를 다룸이 스니펫으로 확인됨."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. law.go.kr lsiSeq=268543 검색 결과 일치. 시행령 시행일 2026-01-22, 고영향 인공지능이 생명·신체의 안전·기본권에 중대한 영향을 미치거나 위험을 초래할 우려가 있는 AI 라는 정의가 검색 결과로 확인됨. 개정안이 국회를 통과했다는 검색 결과가 있어 개정 법률의 시행일과 내용은 미확인. 기준일 명시 필요."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 정확한 URL(regulatory-framework-ai)은 검색 결과에 나오지 않았고, 같은 EC 'Shaping Europe's digital future' 포털의 AI Act 안내 내용(제품 안전 법령 대상 고위험 분류)과 EC AI Act Service Desk 의 제6조 설명으로 확인함. 약한 확인. 제6조(1)의 두 누적 조건(부속서 I 대상 제품의 안전 구성요소 또는 제품 자체 + 제3자 적합성 평가)과 맞음. 검색 결과에 'AI Omnibus 발효'가 있어 적용 시점이 개정됐을 수 있음. 브리프가 시점을 넣지 않은 것은 적절."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2204.01691 검색 결과 일치. Say=과제 접지, Can=사전 학습 기술의 가치 함수(affordance)를 이용한 세계 접지가 스니펫으로 확인됨. 두 값을 '곱한다'는 결합 방식은 스니펫에 없어 문구 수정 지시."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2304.11477 검색 결과 일치. 자연어→PDDL→고전 계획기→자연어 구조는 확인됨. 성능 비교 문구(대부분 최적, LLM 단독은 실행 가능한 계획도 대부분 실패)는 이번 스니펫에 직접 나오지 않음. 이전 실행 2026-09-25-66 f6 이 같은 논문(ref-092)의 저자 보고로 기록했으므로 저자 보고·벤치마크 도메인 조건 한정을 유지하는 조건으로 둔다. 같은 URL 이 기존 ref-092 로 등록돼 있어 중복 id."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2307.01928 검색 결과 일치. 등각 예측 기반 과제 완수의 통계적 보장, 사람 도움 최소화, 미세조정 없이 사용, 공간·수치·선호 모호성의 시뮬레이션·실로봇 실험이 스니펫으로 확인됨. '후보 행동이 하나로 좁혀지지 않을 때만'이라는 동작 조건은 스니펫에 없어 문구 수정 지시. 벤더 문서 근거가 아님(직전 반려 사유 해소)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2209.07753 검색 결과 일치. 인식 출력을 처리하고 제어 기본 API 를 매개변수화하는 정책 코드를 few-shot 으로 생성하며, API 호출을 재조합함이 스니펫으로 확인됨."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "브리프는 원문 미열람(fetched false)으로 적었으나, 검증 에이전트가 raw.githubusercontent.com 의 AmbiK README 를 열어 1000쌍, 보정 100·시험 900, 모호성 유형·명확화 질문과 답·작업 계획 필드를 확인함. 모호성 유형은 선호·상식·안전 세 가지. 주방 환경 조건."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 이번 실행에서 다시 검색하지 않았음(검증 예산 배분). 이전 실행 2026-09-25-30·62 에서 검증을 통과한 출처 ref-359 를 재사용함. arXiv 최초판은 2024-09, 트랙 반영 제안은 EMNLP 2025 로 적어 판 표기가 다름. 기준일 표기 수정 지시."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2302.11649 제목이 검색 결과에 나타나 실재를 확인함. 주장은 방법과 말뭉치 존재에 한정되어 있고 수치는 발췌에만 있음(저자 보고, 판에 따라 다를 수 있음). 이전 실행 검증 통과분 재사용."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 에이전트가 raw.githubusercontent.com 의 LoTa-Bench README 를 열어 가정 서비스 에이전트의 작업 계획 성능 자동 정량화, ALFRED/AI2-THOR 와 Watch-And-Help 확장/VirtualHome 두 환경 쌍을 확인함(브리프 표기는 fetched false). 2026-09-25-67 f46 과 같은 출처를 재사용함."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2604.05427 검색 결과 일치(2026-04-07 제출, Purdue SMART Lab). ISO 13482 근거 안전 속성 추출, 결정적 판정 게이트, 불변 조건·가드·중단 조건의 작업 안전 계약이 확인됨. 판정 결과는 accept·reject·defer 이며 'defer'를 '사람 확인 요청'으로 옮긴 것은 스니펫 범위를 넘어 문구 수정 지시. 개인 돌봄 로봇 표준 기반이라 물류 적용은 추정."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. arXiv 2209.05738 검색 결과 일치. MDP 정식화, 주의 기반 정책과 PPO, 총 이동 지연 최소화, 로봇·작업 수에 독립적인 전역 임베딩, 500개 작업에서 MPDM(탐욕)·RBTS(후회 기반) 대비 최대 10%(25~1000초) 개선, ICRA 2023 모두 스니펫으로 확인됨. 저자 보고, 시뮬레이션 조건, 단일 출처."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. papers.nips.cc 5656 검색 결과 일치. 스니펫에서 확인한 위험 요인은 경계 침식·얽힘·숨은 피드백 루프·선언되지 않은 소비자와 데이터 의존성이고, 설정 문제·외부 세계 변화는 이번 스니펫에 없어 목록을 줄이도록 수정 지시."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. research.google 게시 페이지와 IEEE Big Data 2017 게재가 검색 결과로 확인됨. 28개 시험·감시 항목과 운영 준비도·기술 부채 기준표가 스니펫으로 확인됨. '1급 관심사' 표현은 스니펫에 없어 문구 수정 지시."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. mlflow.org 모델 레지스트리 문서(latest 판 하위 workflow 페이지와 판별 문서)가 검색 결과로 확인됨. 계보·버전·별칭·태그, champion 별칭 재지정으로 운영 모델 교체가 스니펫으로 확인됨. 발행일 없음(문서 판 미확인). 오픈소스 문서이며 기능 설명이라 벤더 성능 주장 아님."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 머니투데이 2026-09-19 기사의 URL·제목이 검색 결과와 일치하고, 한진 대전 메가허브 AI 적재량 예측, 상·하차 종료 시점 예측, 다음 차량 접안 대기시간 단축이 스니펫으로 확인됨. 기업 발표를 전한 기사이고 수치 없음. [추정]·벤더 주장·vendor_claim true 표시 적절. 간선차량 접안은 거점 간 운송과 맞닿아 있어 범위 문구 수정 지시."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "이 위키의 종합 [추정]. 구성 출처는 모두 실재를 확인함(ref-092 은 ref-092 로 바꿈). 각 구성 요소의 성격은 해당 finding 들과 맞음. 원문 미열람."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "가상 시나리오 [추정]. 수치 없음. 출처가 가정·주방·벤치마크 환경임을 밝혔음. 피킹/시작 조건 배치 적절. ref-092 → ref-092."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "가상 시나리오 [추정]. 수치 없음. MLflow 별칭 재지정, ML Test Score, Sculley 의 위험 요인, RTAW 유형 학습 배차를 조합한 것으로 각 출처 범위와 맞음. 출하/예외·성과 배치 적절."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "분류 원문 9장에 비춘 범위 판단 [추정]. 인용 출처는 모두 실재를 확인함. ROP 직접 몫을 채택 기준·검증·확인 요청·기록·모델 버전 승인으로 한정해 경계를 지켰음."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'연계 대상:' 표시 [추정]. 저수준 정책·파지·수요예측을 분류 원문 9장의 로봇 자체 지능·제어와 상위 업무 시스템으로 둔 판단이 원문과 맞음."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "영역 대응 [추정]. 교차 규칙(학습 기반 배차 → 13. 작업 배정 — MRTA)을 적용했음. 원문 주석이 가리키는 5. 로봇 능력·작업 온톨로지, 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 19. 모니터링·이상 탐지·원인 분석은 page_proposals 10절 설명에서 원문으로 연결함. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈을 섞지 않았음."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f19: 한진 간선차량 상·하차 시점 예측과 접안 대기 단축은 분류 원문 9장 '거점 간 운송' 경계와 맞닿아 있어, ROP 몫은 입출고 시간·인계·현장 작업 동기화로만 서술하고 간선 배차·운송계획은 연계 대상으로 적어야 한다(수정 지시로 해결 가능).",
      "f14: SafeGate 는 개인 돌봄 로봇 표준(ISO 13482) 기반 연구이므로 물류 적용은 [추정]으로만 쓴다(브리프 자체 점검과 같음)."
    ]
  },
  "duplication": {
    "ok": false,
    "overlaps": [
      "ref-092(LLM+P, https://arxiv.org/abs/2304.11477)은 기존 ref-092(2026-09-25-66 브리프 출처표, 같은 URL)와 같은 출처다. f7·f20·f21 의 각주는 ref-092 를 재사용해야 한다.",
      "ref-088(SayCan)·ref-351(KnowNo)은 트랙 반영 제안이 인용한 기존 id(SayCan ref-087·ref-088, KnowNo ref-350·ref-351)와 URL 이 같을 수 있다. 참고문헌 목록 요약이 입력에 없어 확인하지 못했다. 같은 URL 이면 퍼블리셔가 기존 id 로 합친다.",
      "f13(LoTa-Bench, ref-541)은 2026-09-25-67 f46 과 같은 출처·주장이다. 모순은 없고 기존 id 재사용이 적절하다."
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
    "f7·f20·f21: 각주 ref-092 을 기존 ref-092(같은 URL https://arxiv.org/abs/2304.11477)로 바꾸고, ref-092 은 reference_updates 에 새로 등록하지 않는다. 같은 출처가 이미 등록돼 있기 때문이다.",
    "f1: '거버넌스가 나머지 세 기능을 가로지른다' 구절을 뺀다. 원문 미열람 상태에서 검색 스니펫으로 확인되지 않았기 때문이다. 나머지(2023-01-26 발표, 자율 적용, 네 기능)는 [사실]로 유지한다.",
    "f6: '곱해'를 '결합해'로 바꾼다. 스니펫은 과제 접지와 세계 접지의 결합까지만 확인해 주고 결합 방식은 확인해 주지 않기 때문이다.",
    "f8: '후보 행동이 하나로 좁혀지지 않을 때만'을 '필요할 때'로 바꾸고 '저자 보고' 한정을 둔다. 스니펫이 뒷받침하는 범위가 거기까지이기 때문이다.",
    "f14: '실행 승인·사람 확인 요청·거부'를 '승인·거부·보류(defer)'로 바꾸고, 물류 적용은 [추정]으로만 서술한다. 논문이 쓰는 판정 결과가 accept·reject·defer 이고 개인 돌봄 로봇 표준 기반이기 때문이다.",
    "f16: 위험 요인 목록을 '경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 등'으로 줄인다. 설정 문제·외부 세계 변화는 이번 스니펫에서 확인되지 않았기 때문이다. f22 의 '외부 세계 변화' 언급도 '데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험'으로 바꾼다.",
    "f17: '데이터·모델·인프라 시험과 감시를 1급 관심사로 두는'을 빼고 '28개 시험·감시 항목으로 운영 준비도를 점수화하는 기준표'로 서술한다. 스니펫 범위를 넘기 때문이다.",
    "f4: 본문과 7절에 기준일 2026-01-22(시행령 시행일)를 적고, 개정 법률의 시행일과 고영향 영역 목록은 '미확인'으로 둔다. 개정안 통과 보도가 있지만 원문을 확인하지 못했기 때문이다.",
    "f5: 적용 시점을 쓰지 않고 '적용 시점은 개정(AI Omnibus) 논의로 이 페이지에서 확정하지 않음'을 한 줄 덧붙인다. 검색 결과에 개정 발효 소식이 있기 때문이다. 고위험 분류 요건은 '안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상'으로 서술한다.",
    "f11: 기준일을 'arXiv 2024-09(학회 게재판은 미확인)'로 적는다. 트랙 반영 제안의 EMNLP 2025 표기와 판이 다르기 때문이다.",
    "f19: 본문 5절에서 [추정]과 '벤더 주장'을 함께 표기하고, ROP 쪽 몫을 입출고 시간·접안·현장 상·하차 작업 동기화로만 쓴다. 간선 배차·운송계획은 분류 원문 9장 '거점 간 운송'의 연계 대상으로 짧게 적는다.",
    "f15: 8절과 6절에서 개선 수치(최대 10%)에 '저자 보고, 시뮬레이션 창고 조건, 단일 출처'를 붙이고, 10절에서 13. 작업 배정 — MRTA 와 양쪽을 연결한다(교차 규칙: 학습 기반 배차).",
    "f21·f22: 5절 시나리오에 '가상 시나리오'임을 밝히고 수치를 넣지 않는다. 출처 환경(가정·주방·벤치마크, 시뮬레이션 창고)이 물류 현장과 다르다는 한계도 적는다.",
    "10절: 원문 주석의 교차 규칙에 따라 5. 로봇 능력·작업 온톨로지·21. 온보딩·설정·현장 시운전(매뉴얼 해석), 6. 지도·공간·위치 모델(도면 해석), 13. 작업 배정 — MRTA(학습 기반 배차), 19. 모니터링·이상 탐지·원인 분석(장애 분석)을 번호와 이름으로 모두 연결한다. 도면 해석·매뉴얼 추출 쪽은 이번 브리프에 finding 이 없으므로 '다음 실행에서 반영 예정인 트랙 제안'으로만 적고 내용은 서술하지 않는다.",
    "11절: oq-030 은 이번 실행에서 조사하지 않았으므로 열림 상태로 유지하고 해결로 바꾸지 않는다. open_questions_new 3건은 형식대로 등록한다.",
    "모든 각주 정의: 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 모든 항목에 source_unopened: true 를 넣는다. web_fetch_available: false 환경이고 브리프의 모든 출처가 fetched false 이기 때문이다.",
    "트랙 반영 제안 15건 중 이번 브리프가 다루지 않은 것(2026-09-25-05·21·36·54·57 과 -04 의 Cohen 외·Huang 외, -30 의 LMCR·구조화 출력, -37 의 DELIVER·SayPlan): 이번 페이지 본문에 넣지 않는다. 검증된 finding 이 없기 때문이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다. 확인 25건, 미확인 0건, 교차 확인 0건. 강등: 없음. 대신 f1·f6·f8·f14·f16·f17 은 검색 스니펫 범위로 문구를 줄이도록 지시했다. 원문 미열람 출처: ref-734, ref-735, ref-736, ref-737, ref-738, ref-088, ref-092, ref-351, ref-742, ref-743, ref-744, ref-745, ref-746, ref-747, ref-359, ref-056, ref-417. ref-354(AmbiK)와 ref-541(LoTa-Bench)은 검증 에이전트가 GitHub 공식 저장소 README 를 열어 확인했다. 주의: 사실로 둔 주장은 모두 단일 출처이고 논문 수치는 저자 보고다. 5절 시나리오와 9절 범위 구분은 이 위키의 추정이다. ref-738(EU AI Act 안내 페이지)은 정확한 URL 이 검색 결과에 나오지 않아 같은 포털 내용으로만 약하게 확인했다. ref-092 은 기존 ref-092 와 같은 출처라 재사용하도록 지시했다. 한국 인공지능 기본법의 개정 법률 내용과 EU AI Act 적용 시점은 미확인이다. oq-030 은 이번에 조사하지 않아 열림으로 남는다. 정정 요청 없음. 검색 사용: 검증 17회(리서치 12회와 합쳐 29/30).",
  "retry_reason": null
}
```

### runs/2026-09-25-68/pages.json

```json
{
  "run_id": "2026-09-25-68",
  "outline": [
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 750,
      "summary": "AI가 만든 계획·해석을 실행에 쓰는 기준은 접지·형식 검증·사람 확인·안전 판정·승인된 모델 버전의 겹 구조로 정리될 수 있어 보인다. [추정][^ref-088] 한국 인공지능 기본법(2026-01-22 시행)과 EU AI Act가 고영향·고위험 AI에 별도 책무를 둔다. [사실][^ref-737]",
      "planned_findings": [
        "f20",
        "f16",
        "f4",
        "f5"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 650,
      "summary": "과제·세계 접지, PDDL, 등각 예측, LLM 에이전트, AI 관리 시스템, 모델 레지스트리를 정리한다. [사실][^ref-351]",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f11",
        "f2",
        "f18"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)",
      "budget_chars": 900,
      "summary": "피킹 자연어 지시 해석과 출하 마감 시간대의 학습 배차 모델 교체를 가상 시나리오로 보인다. [추정][^ref-092]",
      "planned_findings": [
        "f21",
        "f22",
        "f19",
        "f23",
        "f8",
        "f15",
        "f4"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1100,
      "summary": "LLM 계획의 접지·형식 검증, 필요할 때 되묻기, 실행 전 안전 판정, 학습 기반 배차, 모델 운영 관리를 다룬다. [추정][^ref-088]",
      "planned_findings": [
        "f6",
        "f7",
        "f12",
        "f9",
        "f8",
        "f11",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f20"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 600,
      "summary": "NIST AI RMF, ISO/IEC 42001, ISO/IEC 23894, MLflow 모델 레지스트리, LoTa-Bench, AmbiK와 관련 법(한국 인공지능 기본법, EU AI Act)을 정리한다(안내 문장, 태그 없음).",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f18",
        "f10",
        "f13"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 800,
      "summary": "SayCan, LLM+P, KnowNo, Code as Policies, Lang2LTL, AmbiK, Learning to Ask, LoTa-Bench, SafeGate, RTAW, Sculley 외, ML Test Score를 정리한다(검증 상태 안내 문장, 태그 없음).",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)",
      "budget_chars": 600,
      "summary": "ROP는 AI 출력의 채택 기준·검증·사람 확인·기록·모델 버전 승인을 맡고, 저수준 정책·파지 학습과 수요예측은 연계 대상이다. [추정][^ref-735]",
      "planned_findings": [
        "f23",
        "f24",
        "f19"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 700,
      "summary": "교차 규칙에 따라 5. 로봇 능력·작업 온톨로지·21. 온보딩·설정·현장 시운전(매뉴얼 해석), 6. 지도·공간·위치 모델(도면 해석), 13. 작업 배정 — MRTA(학습 기반 배차), 19. 모니터링·이상 탐지·원인 분석(장애 분석)과 18. 사람–로봇 협업·운영 인터페이스, 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리, 25. 안전·위험 관리, 28. 표준·상호운용성·다사업자 거버넌스를 연결한다. [추정][^ref-743]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "section": "11. 열린 질문",
      "budget_chars": 450,
      "summary": "oq-030을 열림으로 유지하고, 고영향 인공지능 해당 여부, EU AI Act 안전 구성요소 해당 여부, 등각 예측 재보정 주기를 새로 올린다.",
      "planned_findings": [
        "f4",
        "f5",
        "f8"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(LLM 계획 접지·검증·되묻기·안전 판정, 학습 기반 배차, 모델 운영, AI 위험관리 표준·법), 페이지 상태 자동 영역 추가, 각주 19건. 2차: 7·8절 도입 문장의 태그·각주 제거, 6절 도식 지시어 수정"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area27-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. AI·학습·적응과 모델 운영 의 \"6. 대표 접근법과 기술\" 절(1,218자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area27-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. AI·학습·적응과 모델 운영 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,001자)을 옮겼다. 2차: 도입 문장의 [사실] 태그와 ref-735 각주를 떼어 안내 문장으로 바꿨다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area27-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. AI·학습·적응과 모델 운영 의 \"8. 대표 연구와 자료\" 절(969자)을 옮겼다. 2차: 도입 문장의 태그·각주 제거와 README 확인 출처 명시, KnowNo 항목 문구 수정(필요할 때·저자 보고)"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area27-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. AI·학습·적응과 모델 운영 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(760자)을 옮겼다. 본문 링크를 주제 페이지 위치 기준 경로(../../categories/…)로 고쳤다"
    },
    {
      "path": "docs/topics/2026/2026-09-25-area27-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 27. AI·학습·적응과 모델 운영 의 \"4. 핵심 개념과 용어\" 절(754자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-25 | 27. AI·학습·적응과 모델 운영 | 영역 심화: 3~11절 신규 작성(LLM 계획 접지·검증·되묻기·안전 판정, 학습 기반 배차, 모델 운영, AI 위험관리 표준·법, 출처 19건 원문 미열람) | run 2026-09-25-68",
  "index_updates": {
    "home_recent": "2026-09-25 — 27. AI·학습·적응과 모델 운영: 3~11절 첫 작성(LLM 계획 접지·형식 검증·되묻기·실행 전 안전 판정, 학습 기반 배차, 모델 레지스트리, NIST AI RMF·ISO/IEC 42001·한국 인공지능 기본법)",
    "category_recent": "2026-09-25 — 27. AI·학습·적응과 모델 운영: 영역 심화 초안 작성, 교차 규칙에 따라 5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전과 연결",
    "area_recent": "2026-09-25 — 27. AI·학습·적응과 모델 운영: 3~11절 신규 작성(신뢰도 medium, 원문 미열람 출처 19건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "conformal-prediction",
      "term_ko": "등각 예측",
      "term_en": "Conformal Prediction",
      "definition": "보정 데이터로 예측 집합의 크기를 정해, 정답이 집합에 들어갈 확률을 사용자가 정한 수준 이상으로 통계적으로 보장하는 불확실성 정량화 방법이다.",
      "description": "KnowNo는 등각 예측으로 LLM 계획기의 불확실성을 보정해 필요할 때 사람에게 도움을 요청하게 한다(저자 보고).",
      "related_areas": [
        27,
        18
      ],
      "sources": [
        "ref-351"
      ]
    },
    {
      "action": "new",
      "slug": "artificial-intelligence-management-system",
      "term_ko": "AI 관리 시스템",
      "term_en": "Artificial Intelligence Management System (AIMS)",
      "definition": "조직이 AI 의 책임 있는 개발·제공·사용을 위한 정책·목표·프로세스를 세우고 운영하는 관리 체계로, ISO/IEC 42001 이 요구사항을 정한다.",
      "related_areas": [
        27,
        28
      ],
      "sources": [
        "ref-735"
      ]
    },
    {
      "action": "new",
      "slug": "high-impact-ai",
      "term_ko": "고영향 인공지능",
      "term_en": "High-impact AI (Korea AI Basic Act)",
      "definition": "한국 인공지능 기본법에서 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있어 별도 책무가 부과되는 영역의 AI 시스템이다.",
      "description": "법과 시행령은 2026-01-22 시행되었다. 개정 법률의 시행일과 고영향 영역 목록은 미확인이다.",
      "related_areas": [
        27,
        25,
        28
      ],
      "sources": [
        "ref-737"
      ]
    },
    {
      "action": "new",
      "slug": "model-registry",
      "term_ko": "모델 레지스트리",
      "term_en": "Model Registry",
      "definition": "학습된 모델의 버전·별칭·태그·계보를 한곳에서 관리해 어떤 버전을 운영에 쓰는지 정하고 교체·되돌림을 추적하게 하는 저장소다.",
      "related_areas": [
        27,
        24
      ],
      "sources": [
        "ref-746"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-734",
      "org": "NIST",
      "title": "NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence",
      "published": "2023-01-26",
      "url": "https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. NIST AI RMF 1.0(NIST AI 100-1) 발표문. 네 기능 Govern·Map·Measure·Manage.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s7.md"
      ]
    },
    {
      "id": "ref-735",
      "org": "ISO/IEC",
      "title": "ISO/IEC 42001:2023 - AI management systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/42001",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AI 관리 시스템(AIMS)의 수립·실행·유지·개선 요구사항 표준 소개 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s4.md",
        "docs/topics/2026/2026-09-25-area27-s7.md"
      ]
    },
    {
      "id": "ref-736",
      "org": "ISO/IEC",
      "title": "ISO/IEC 23894:2023 - AI — Guidance on risk management",
      "published": "2023-02",
      "url": "https://www.iso.org/standard/77304.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 31000 을 AI 에 적용한 위험관리 지침 소개 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s7.md"
      ]
    },
    {
      "id": "ref-737",
      "org": "국가법령정보센터(과학기술정보통신부)",
      "title": "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법",
      "published": null,
      "url": "https://www.law.go.kr/lsInfoP.do?lsiSeq=268543",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국 인공지능 기본법 법령 본문. 고영향 인공지능 정의와 사업자 책무, 2026-01-22 시행(검색 요약 기준).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s7.md"
      ]
    },
    {
      "id": "ref-738",
      "org": "European Commission",
      "title": "AI Act | Shaping Europe's digital future",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Regulation (EU) 2024/1689(AI Act)의 위험 기반 규제와 고위험 AI 분류 안내 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s7.md",
        "docs/topics/2026/2026-09-25-area27-s10.md"
      ]
    },
    {
      "id": "ref-088",
      "org": "Ahn, M. 외",
      "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
      "published": "2022-04",
      "url": "https://arxiv.org/abs/2204.01691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SayCan: LLM 과제 접지와 기술 가치 함수의 세계 접지를 결합한 로봇 계획.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s4.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-092",
      "org": "Liu, B. 외",
      "title": "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency",
      "published": "2023-04",
      "url": "https://arxiv.org/abs/2304.11477",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어를 PDDL 로 바꿔 고전 계획기로 푸는 LLM+P 프레임워크(기존 id 재사용).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s4.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
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
      "summary": "원문 미열람. KnowNo: 등각 예측으로 LLM 계획기의 불확실성을 보정해 필요할 때 사람에게 묻는 방법.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s4.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md",
        "docs/topics/2026/2026-09-25-area27-s10.md"
      ]
    },
    {
      "id": "ref-742",
      "org": "Liang, J. 외",
      "title": "Code as Policies: Language Model Programs for Embodied Control",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.07753",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 코드 생성 LLM 이 인식·제어 API 를 조합한 로봇 정책 코드를 쓰는 방법.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-743",
      "org": "Agrawal, A. 외",
      "title": "RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.05738",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 다중 로봇 작업 배정의 주의 기반 강화학습(ICRA 2023).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md",
        "docs/topics/2026/2026-09-25-area27-s10.md"
      ]
    },
    {
      "id": "ref-744",
      "org": "Sculley, D. 외",
      "title": "Hidden Technical Debt in Machine Learning Systems",
      "published": "2015",
      "url": "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ML 시스템 고유의 기술 부채와 위험 요인(NeurIPS 2015).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-745",
      "org": "Breck, E. 외 (Google Research)",
      "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
      "published": "2017",
      "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 28개 시험·감시 항목으로 ML 운영 준비도를 점수화하는 기준표(IEEE Big Data 2017).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-746",
      "org": "MLflow (Linux Foundation 오픈소스 프로젝트)",
      "title": "ML Model Registry | MLflow AI Platform",
      "published": null,
      "url": "https://mlflow.org/docs/latest/ml/model-registry/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모델 버전·별칭·태그·계보를 관리하는 MLflow 모델 레지스트리 공식 문서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s4.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s7.md",
        "docs/topics/2026/2026-09-25-area27-s10.md"
      ]
    },
    {
      "id": "ref-747",
      "org": "머니투데이",
      "title": "포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI'",
      "published": "2026-09-19",
      "url": "https://www.mt.co.kr/industry/2026/09/19/2026091818023697394",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 국내 물류기업의 로봇·AI 적용 사례 기사(한진 적재량 예측 등, 기업 발표 전달).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md"
      ]
    },
    {
      "id": "ref-354",
      "org": "cog-model (AmbiK 저자)",
      "title": "AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment)",
      "published": null,
      "url": "https://github.com/cog-model/AmbiK-dataset",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모호 작업 데이터셋 AmbiK 공식 저장소 README.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s7.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-359",
      "org": "Wang, W. 외",
      "title": "Learning to Ask: When LLM Agents Meet Unclear Instruction",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.00557",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 불명확 지시 벤치마크 NoisyToolBench 와 Ask-when-Needed(arXiv 2024-09, 학회 게재판 미확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s4.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-056",
      "org": "Liu, J. X. 외",
      "title": "Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments",
      "published": "2023-02",
      "url": "https://arxiv.org/abs/2302.11649",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Lang2LTL: 자연어 명령을 LTL 로 바꿔 접지하는 방법과 말뭉치.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md"
      ]
    },
    {
      "id": "ref-541",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "title": "LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README)",
      "published": null,
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 언어 기반 작업 계획기 자동 평가 벤치마크 LoTa-Bench 공식 저장소.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s7.md",
        "docs/topics/2026/2026-09-25-area27-s8.md",
        "docs/topics/2026/2026-09-25-area27-s10.md"
      ]
    },
    {
      "id": "ref-417",
      "org": "arXiv (SafeGate 저자, 저자명 미확인)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 명령의 실행 전 안전 판정(승인·거부·보류)과 작업 안전 계약 SafeGate.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
        "docs/topics/2026/2026-09-25-area27-s6.md",
        "docs/topics/2026/2026-09-25-area27-s8.md",
        "docs/topics/2026/2026-09-25-area27-s10.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가?",
      "areas": [
        27,
        28
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가?",
      "areas": [
        27,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가?",
      "areas": [
        27,
        18
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [
    {
      "step": "피킹",
      "item": "시작 조건",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    },
    {
      "step": "피킹",
      "item": "수행 자원",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    },
    {
      "step": "피킹",
      "item": "제약",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    },
    {
      "step": "피킹",
      "item": "예외·성과",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    },
    {
      "step": "출하",
      "item": "시작 조건",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    },
    {
      "step": "출하",
      "item": "수행 자원",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    },
    {
      "step": "출하",
      "item": "예외·성과",
      "link": "docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md",
      "title": "27. AI·학습·적응과 모델 운영"
    }
  ],
  "standards_updates": [
    {
      "name": "NIST AI RMF 1.0 (NIST AI 100-1)",
      "kind": "프레임워크",
      "org": "NIST",
      "url": "https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial",
      "related_areas": [
        27,
        25
      ],
      "summary": "2023-01-26 발표된 자율 적용 AI 위험관리 프레임워크. 네 기능 Govern·Map·Measure·Manage(원문 미열람).",
      "ref_id": "ref-734"
    },
    {
      "name": "ISO/IEC 42001:2023 AI 관리 시스템",
      "kind": "표준",
      "org": "ISO/IEC",
      "url": "https://www.iso.org/standard/42001",
      "related_areas": [
        27,
        28
      ],
      "summary": "AI 시스템을 개발·제공·사용하는 조직의 AI 관리 시스템(AIMS) 수립·실행·유지·지속 개선 요구사항(원문 미열람).",
      "ref_id": "ref-735"
    },
    {
      "name": "ISO/IEC 23894:2023 AI 위험관리 지침",
      "kind": "표준",
      "org": "ISO/IEC",
      "url": "https://www.iso.org/standard/77304.html",
      "related_areas": [
        27,
        25
      ],
      "summary": "ISO 31000 을 AI 에 적용해 위험 평가·처리·감시·검토·기록을 AI 활동에 통합하도록 안내하는 지침(원문 미열람).",
      "ref_id": "ref-736"
    },
    {
      "name": "MLflow 모델 레지스트리",
      "kind": "오픈소스",
      "org": "MLflow (Linux Foundation 오픈소스 프로젝트)",
      "url": "https://mlflow.org/docs/latest/ml/model-registry/",
      "related_areas": [
        27,
        24
      ],
      "summary": "등록 모델의 버전·별칭·태그·계보를 관리하고 별칭 재지정으로 운영 모델을 교체하게 하는 기능(원문 미열람).",
      "ref_id": "ref-746"
    },
    {
      "name": "LoTa-Bench",
      "kind": "오픈소스",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "related_areas": [
        27,
        23
      ],
      "summary": "언어 기반 작업 계획기 성능을 시뮬레이터 성공률로 자동 정량화하는 벤치마크.",
      "ref_id": "ref-541"
    },
    {
      "name": "AmbiK 데이터셋",
      "kind": "오픈소스",
      "org": "cog-model (AmbiK 저자)",
      "url": "https://github.com/cog-model/AmbiK-dataset",
      "related_areas": [
        27,
        18
      ],
      "summary": "모호한 작업·모호하지 않은 짝 1000쌍(보정 100, 시험 900)으로 LLM 의 모호성 탐지·되묻기를 평가하는 데이터셋(주방 환경).",
      "ref_id": "ref-354"
    }
  ],
  "additional_research_requests": [
    "11절: oq-030 LTAA(arXiv 2512.02810)의 LLM 배정 완료율 77% 주장과 동적 계획법 우위 요약 가운데 어느 쪽이 원문 결과인지 원문 확인이 필요하다(출처 충돌 해소).",
    "3·7절: 한국 인공지능 기본법 개정 법률의 시행일(2026-07-21 언급)과 고영향 인공지능 영역 목록을 법령 원문으로 확인해야 기준일을 갱신할 수 있다.",
    "3·7절: EU AI Act 고위험 의무의 적용 시점이 개정(AI Omnibus)으로 바뀌었는지 공식 자료로 확인해야 한다.",
    "6·8절: 트랙 반영 제안 가운데 도면 해석(2026-09-25-05·36·54), 매뉴얼 추출(2026-09-25-57), LLM 다중 로봇 서베이·ROSA·RAI·ChatGPT for Robotics(2026-09-25-21), Cohen 외·Huang 외(-04), LMCR·구조화 출력(-30), DELIVER·SayPlan(-37)은 이번 브리프에 검증된 finding 이 없어 본문에 넣지 못했다. 다음 해당 영역 실행에서 재확인이 필요하다.",
    "3·6절: 한 줄 정의의 수요·고장 예측(예: 로봇 고장 예측 사례)과 19. 모니터링·이상 탐지·원인 분석에 적용되는 장애 분석 AI 자료가 브리프에 없어 쓰지 못했다.",
    "전 절: 사실 주장이 모두 단일 출처·원문 미열람이다. 핵심 주장(SayCan, KnowNo, RTAW 수치, ISO/IEC 42001)을 원문 열람 또는 독립 출처로 교차 확인해야 신뢰도를 올릴 수 있다.",
    "참고문헌: reference_updates 가 기존 id(ref-088·092·351·354·359·056·541·417)에도 source_unopened: true 를 넣으므로, 퍼블리셔가 기존 참고문헌 페이지의 열람 표시를 덮어쓰지 않는지 pipeline 담당의 확인이 필요하다(2차 검증 참고 사항)."
  ],
  "fixes_applied": [
    "f7·f20·f21 각주 ref-092 → ref-092 — 3·4·5·6·8절의 LLM+P 인용을 모두 [^ref-092]로 바꾸고 각주 정의를 ref-092 로 두었으며, reference_updates 에 ref-092 을 등록하지 않았다(ref-092 는 cited_by 갱신용으로만 넣음).",
    "f1 '거버넌스가 나머지 세 기능을 가로지른다' 삭제 — 7절 표의 NIST AI RMF 행에 발표일·자율 적용·네 기능만 [사실]로 남겼다.",
    "f6 '곱해' → '결합해' — 4절 용어와 6절·8절 SayCan 서술을 '결합해'로 썼다.",
    "f8 '필요할 때'·'저자 보고' — 4·5·6·8절의 KnowNo 서술을 '필요할 때 사람에게 도움을 요청'으로 쓰고 저자 보고 한정을 붙였다.",
    "f14 '승인·거부·보류(defer)'와 물류 적용 [추정] — 6·8절에 판정 결과를 승인·거부·보류(defer)로 쓰고, 물류 적용 가능성은 별도 [추정] 문장으로 분리했다.",
    "f16 위험 요인 목록 축소, f22 문구 변경 — 3절에 '경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 등'으로 쓰고, 5절 출하 시나리오의 '외부 세계 변화'를 '데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험'으로 바꿨다.",
    "f17 '1급 관심사' 삭제 — 6·8절에 '28개 시험·감시 항목으로 운영 준비도를 점수화하는 기준표'로만 썼다.",
    "f4 기준일 2026-01-22와 미확인 표시 — 3절과 7절에 기준일 2026-01-22를 적고 개정 법률 시행일·고영향 영역 목록을 '미확인'으로 두었다.",
    "f5 적용 시점 미확정 문구와 요건 서술 — 3·7절에 '안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상'으로 쓰고 '적용 시점은 개정(AI Omnibus) 논의로 이 페이지에서 확정하지 않는다'를 덧붙였다.",
    "f11 기준일 — 6·8절에 'arXiv 2024-09, 학회 게재판은 미확인'으로 적었다.",
    "f19 [추정]·벤더 주장, ROP 몫 한정 — 5절에서 '[추정] 벤더 주장'으로 표기하고 ROP 몫을 입출고 시간·접안·현장 상·하차 작업 동기화로, 간선 배차·운송계획을 분류 원문 9장 거점 간 운송의 연계 대상으로 적었으며 9절 표에도 같은 행을 두었다.",
    "f15 한정어와 13절 연결 — 6·8절 RTAW 수치에 '저자 보고, 시뮬레이션 창고 조건, 단일 출처'를 붙이고 10절에 13. 작업 배정 — MRTA 를 연결했다.",
    "f21·f22 가상 시나리오 명시 — 5절 첫머리에 설명용 가상 시나리오임과 수치를 넣지 않았음, 출처 환경(가정·주방·벤치마크, 시뮬레이션 창고)이 물류 현장과 다르다는 한계를 적었다.",
    "10절 교차 규칙 연결 — 5. 로봇 능력·작업 온톨로지, 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석을 번호와 이름으로 연결하고, 도면 해석·매뉴얼 추출은 '다음 실행에서 반영 예정인 트랙 제안'으로만 적었다.",
    "11절 — oq-030 을 열림 상태로 유지하고(이번 실행 미조사 명시) open_questions_new 3건을 11절과 open_question_updates 에 new 로 등록했다.",
    "모든 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 모든 항목에 source_unopened: true 를 넣었다.",
    "트랙 반영 제안 가운데 브리프가 다루지 않은 항목(2026-09-25-05·21·36·54·57, -04 의 Cohen 외·Huang 외, -30 의 LMCR·구조화 출력, -37 의 DELIVER·SayPlan)은 본문에 넣지 않고 additional_research_requests 에 재확인 요청으로만 남겼다.",
    "분량 초과 자동 분리: 27. AI·학습·적응과 모델 운영 본문 8,004자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 3,936자",
    "형식 검증: docs/topics/2026/2026-09-25-area27-s10.md 3절의 세부영역 링크 10건을 주제 페이지 위치 기준 경로(../../categories/<대분류 slug>/<파일>.md)로 고쳤다. 주장·태그·각주는 바꾸지 않았다.",
    "2차: 7절 도입 문장의 태그·각주 제거 — 세부영역 페이지 7절 첫 문장과 2026-09-25-area27-s7.md 의 1절 첫 항목·3절 첫 문장에서 '[사실][^ref-735]'를 떼어 태그 없는 안내 문장으로 두었다(ref-735 는 표의 ISO/IEC 42001 행에만 남김).",
    "2차: 8절 도입 문장의 태그·각주 제거와 확인 방식 명시 — 세부영역 페이지 8절 첫 문장과 2026-09-25-area27-s8.md 의 1절 첫 항목·3절 첫 문장에서 '[사실][^ref-351]'를 떼고 '모두'를 '대부분'으로 고쳤으며 'AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다'를 덧붙였다(세부영역 페이지에서는 목록이 주제 페이지로 옮겨졌으므로 '아래 자료는'을 '이 절의 자료는'으로 썼다).",
    "2차: 2026-09-25-area27-s8.md 3절 KnowNo 항목을 '등각 예측으로 필요할 때 사람에게 도움을 요청하는 LLM 계획기(저자 보고)'로 고쳤다.",
    "2차: 세부영역 페이지 6절 첫 단락의 '아래 도식은 3절의 겹 구조를 이 위키가 그린 것이다.'를 '3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.'로 고쳤다(주장·태그 변경 없음)."
  ]
}
```

### runs/2026-09-25-68/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-25-68/pages/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 27
related_areas: [5, 6, 13, 18, 19, 21, 23, 24, 25, 28]
tags: [LLM 계획 접지, 등각 예측, 학습 기반 배차, 모델 레지스트리, AI 위험관리]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-734, ref-735, ref-736, ref-737, ref-738, ref-088, ref-092, ref-351, ref-742, ref-743, ref-744, ref-745, ref-746, ref-747, ref-354, ref-359, ref-056, ref-541, ref-417]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 27. AI·학습·적응과 모델 운영

# 27. AI·학습·적응과 모델 운영

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 한 줄 정의

문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [분류원문]

## 2. SCM 관점의 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 3. 왜 중요한가

AI가 만든 계획·해석을 실행에 쓰는 기준은 한 가지 장치가 아니라 실행 가능성 접지, 형식 명세·계획기 경유 검증, 불확실할 때 사람 확인, 실행 전 안전 판정, 승인된 모델 버전·시험 기준이 겹친 구조로 정리될 수 있어 보인다. [추정][^ref-088][^ref-092][^ref-056][^ref-351][^ref-359][^ref-417][^ref-745][^ref-746][^ref-735] 이 구조는 각 출처가 다루는 서로 다른 단계를 이 위키가 묶은 것이며, 하나의 출처가 제시한 채택 기준은 아니다.

기준이 필요한 이유는 모델이 한 번 넣고 끝나는 부품이 아니기 때문이다. Sculley 외(2015)는 실제 머신러닝(Machine Learning, ML) 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 등 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. [사실][^ref-744]

규제도 같은 방향을 가리킨다. 한국 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI를 고영향 인공지능으로 두어 별도 책무를 부과한다(기준일 2026-01-22). [사실][^ref-737] 개정 법률의 시행일과 고영향 영역 목록은 미확인이다. EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상인 AI 시스템을 고위험 AI로 분류한다. [사실][^ref-738] 적용 시점은 개정(AI Omnibus) 논의로 이 페이지에서 확정하지 않는다.

## 4. 핵심 개념과 용어

이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.

자세한 내용은 주제 페이지 [27. AI·학습·적응과 모델 운영 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area27-s4.md)에 있다.

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

**물류 흐름 단계:** 피킹, 출하

**시나리오:** 자연어 피킹 지시의 해석 검증과 출하 마감 시간대의 학습 배차 모델 교체

다음은 설명을 위한 가상의 시나리오이다. 수치는 넣지 않았고, 근거 출처의 실험 환경(가정·주방·벤치마크, 시뮬레이션 창고)은 물류 현장과 다르다.

### 가. 피킹 — 자연어 지시 해석

| 항목 | 내용 |
|---|---|
| 시작 조건 | 관리자가 “오늘 마감 주문을 B구역부터 피킹”처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. [추정][^ref-092][^ref-351][^ref-354] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | LLM은 지시를 해석하고, ROP는 해석 결과의 채택·거부와 사람 확인 요청, 채택·거부 기록을 맡는 구조로 보인다. [추정][^ref-351] |
| 제약 | 이런 AI 활용이 인공지능 기본법의 고영향 인공지능에 해당하는지는 미확인이다(11절 열린 질문). |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해석 후보가 불확실하면 사람에게 묻는다. KnowNo는 필요할 때 사람에게 도움을 요청하게 하며 사람 도움을 줄이는 것을 목표로 한다(저자 보고). [사실][^ref-351] |

### 나. 출하 — 학습 배차 모델 교체

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려는 변경 요청(설명용 가정) |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 창고 다중 로봇 작업 배정을 강화학습 정책으로 수행하는 방법이 연구되어 있다(RTAW, 시뮬레이션 창고 조건). [사실][^ref-743] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고 교체 전 시험·감시 기준을 통과시켜야, 데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험에서 오는 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. [추정][^ref-746][^ref-745][^ref-743][^ref-744] |

피킹 시나리오에서 이 영역이 관여하는 칸은 시작 조건(지시가 작업으로 바뀌는 순간)과 예외·성과(되묻기)다. 출하 시나리오에서는 모델 교체가 예외·성과 칸의 위험이 된다.

국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. [추정] 벤더 주장[^ref-747] 이런 예측을 ROP 관점에서 쓴다면 ROP의 몫은 입출고 시간·접안·현장 상·하차 작업의 동기화까지이고, 간선 배차·운송계획은 분류 원문 9장 “거점 간 운송”의 연계 대상이다([범위 경계](../../about/scope-boundary.md)).

## 6. 대표 접근법과 기술

LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-746] 3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.

자세한 내용은 주제 페이지 [27. AI·학습·적응과 모델 운영 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area27-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [27. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area27-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절의 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.

자세한 내용은 주제 페이지 [27. AI·학습·적응과 모델 운영 — 대표 연구와 자료](../../topics/2026/2026-09-25-area27-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

ROP가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리로 보인다. [추정][^ref-735][^ref-734][^ref-736][^ref-351][^ref-746]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | AI가 낸 계획의 실행 가능 여부 확인, 채택·거부와 기록 | 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(연계 대상) |
| 상위 업무 시스템 | 주문·납기 제약을 받은 배정·계획 모델의 버전·변경 승인 | 수요예측 모델(연계 대상) |
| 거점 간 운송 | 입출고 시간·접안·현장 상·하차 작업 동기화 | 간선 배차·운송계획(연계 대상) |

연계 대상: Code as Policies의 저수준 정책 코드, SayCan의 사전 학습 기술 같은 저수준 정책·파지 학습과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. [추정][^ref-742][^ref-088] 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 ROP의 채택 기준을 둘러싼 운영 틀로 보인다. [추정][^ref-735][^ref-734][^ref-736] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류 원문 8장의 교차 규칙에 따라 이 영역의 AI 방법은 적용 대상 영역과 양쪽으로 연결된다.

자세한 내용은 주제 페이지 [27. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area27-s10.md)에 있다.

## 11. 열린 질문

아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-030** (상태: 열림) 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? 이번 실행에서는 조사하지 않았다.
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) 물류 현장 로봇의 작업 계획·배정에 쓰는 AI가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가?[^ref-737]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) LLM이나 학습 모델이 ROP의 정지·경로·구역 결정에 관여할 때 EU AI Act가 말하는 제품 안전 구성요소로 볼 수 있는가?[^ref-738]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) KnowNo의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가?[^ref-351]

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-734]: NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence, 2023-01-26, https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial, 접근일 2026-09-25 (원문 미열람)
[^ref-735]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-736]: ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management, 2023-02, https://www.iso.org/standard/77304.html, 접근일 2026-09-25 (원문 미열람)
[^ref-737]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 미확인, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-09-25 (원문 미열람)
[^ref-738]: European Commission, AI Act (Shaping Europe's digital future), 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-742]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)
[^ref-743]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-744]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-745]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)
[^ref-747]: 머니투데이, 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI', 2026-09-19, https://www.mt.co.kr/industry/2026/09/19/2026091818023697394, 접근일 2026-09-25 (원문 미열람)
[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 27
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 27. AI·학습·적응과 모델 운영

# 27. AI·학습·적응과 모델 운영

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [분류원문]

## 2. SCM 관점의 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

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

### runs/2026-09-25-68/pages/topics/2026/2026-09-25-area27-s6.md

````markdown
---
title: "27. AI·학습·적응과 모델 운영 — 대표 접근법과 기술"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 27
related_areas: [5, 6, 13, 18, 19, 21, 23, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-056, ref-092, ref-359, ref-417, ref-088, ref-351, ref-742, ref-743, ref-745, ref-746]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md#6
---

[홈](../../index.md) › [주제](../index.md) › 27. AI·학습·적응과 모델 운영 — 대표 접근법과 기술

# 27. AI·학습·적응과 모델 운영 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-746] 아래 도식은 3절의 겹 구조를 이 위키가 그린 것이다.
- 이 페이지는 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-746] 아래 도식은 3절의 겹 구조를 이 위키가 그린 것이다.

```mermaid
flowchart LR
  instr[자연어 지시·학습 모델 출력] --> ground[실행 가능성 접지]
  ground --> formal[형식 명세·계획기 검증]
  formal --> ask{불확실한가}
  ask -- 예 --> human[사람 확인 요청]
  ask -- 아니오 --> gate[실행 전 안전 판정]
  human --> gate
  gate --> exec[실행 채택·기록]
  model[승인된 모델 버전·시험 기준] -.-> instr
```

### LLM 계획의 접지와 형식 검증

SayCan은 LLM의 과제 접지와 기술 가치 함수의 세계 접지를 결합해 실행 가능하고 맥락에 맞는 기술만 선택하게 한다. [사실][^ref-088] LLM+P는 자연어를 PDDL로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기며, 저자는 LLM 단독으로는 대부분 문제에서 실행 가능한 계획도 못 냈으나 LLM+P는 대부분에서 최적 해를 냈다고 보고한다(벤치마크 도메인 조건). [사실][^ref-092] Lang2LTL은 자연어 명령을 [선형 시간 논리](../../glossary/linear-temporal-logic.md)(Linear Temporal Logic, LTL) 식으로 바꿔 접지한다. [사실][^ref-056] Code as Policies는 코드 생성 LLM이 인식 출력 처리와 제어 기본 API 호출을 조합한 정책 코드를 쓰게 해, 사람이 정한 API 범위 안에서 명령을 재조합한다. [사실][^ref-742]

### 필요할 때 되묻기

KnowNo는 등각 예측으로 LLM 계획기의 불확실성을 보정해 과제 완수에 통계적 보장을 두면서 필요할 때 사람에게 도움을 요청하게 하며, 모델 미세조정 없이 쓸 수 있다고 저자가 보고한다. [사실][^ref-351] Wang 외는 불명확 지시 벤치마크 NoisyToolBench와 필요할 때 되묻는 방법(Ask-when-Needed)을 제안했다(arXiv 2024-09, 학회 게재판은 미확인). [사실][^ref-359] 이는 [사람 참여 루프](../../glossary/human-in-the-loop.md)를 계획 단계에 두는 방식이다.

### 실행 전 안전 판정

SafeGate는 자연어 작업 명령에서 안전 관련 속성을 뽑아 결정적 판정으로 승인·거부·보류(defer)를 정하고, 승인된 작업을 불변 조건·가드·중단 조건의 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했다. [사실][^ref-417] 개인 돌봄 로봇 표준(ISO 13482) 기반 연구이므로 물류 작업 명령에 같은 구조를 쓸 수 있는지는 추정 단계다. [추정][^ref-417]

### 학습 기반 배차

RTAW는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 정식화하고 주의 기반 정책을 PPO로 학습해 총 이동 지연을 줄이며, 500개 작업에서 탐욕·후회 기반 기준 대비 최대 10% 개선과 로봇·작업 수에 독립적인 정책 크기를 보고한다(저자 보고, 시뮬레이션 창고 조건, 단일 출처). [사실][^ref-743]

### 모델 운영 관리

ML Test Score는 28개 시험·감시 항목으로 ML 시스템의 운영 준비도를 점수화하는 기준표다. [사실][^ref-745] MLflow 모델 레지스트리는 운영 대상 버전에 별칭(예: champion)을 붙이고 별칭을 다른 버전으로 옮겨 운영 모델을 교체하게 한다. [사실][^ref-746]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-742]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)
[^ref-743]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-745]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-68 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-68 | 27. AI·학습·적응과 모델 운영 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-09-25-68/pages/topics/2026/2026-09-25-area27-s7.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 27
related_areas: [5, 6, 13, 18, 19, 21, 23, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-354, ref-541, ref-734, ref-735, ref-736, ref-737, ref-738, ref-746]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md#7
---

[홈](../../index.md) › [주제](../index.md) › 27. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스

# 27. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| NIST AI RMF 1.0 (NIST AI 100-1) | 프레임워크 | 2023-01-26 자율 적용 프레임워크로 발표되었고, 핵심은 거버넌스(Govern)·맵(Map)·측정(Measure)·관리(Manage) 네 기능이다. [사실][^ref-734] | ref-734 (원문 미열람) |
| ISO/IEC 42001:2023 | 표준 | AI 시스템을 개발·제공·사용하는 조직의 AI 관리 시스템 요구사항. [사실][^ref-735] | ref-735 (원문 미열람) |
| ISO/IEC 23894:2023 | 표준 | ISO 31000 위험관리 원칙을 AI에 적용해 위험 평가·처리·감시·검토·기록을 AI 활동에 통합하도록 안내하는 지침(2023-02). [사실][^ref-736] | ref-736 (원문 미열람) |
| MLflow 모델 레지스트리 | 오픈소스 | 모델 버전·별칭·태그·계보 관리와 별칭 재지정에 의한 운영 모델 교체. [사실][^ref-746] | ref-746 (원문 미열람) |
| LoTa-Bench | 오픈소스 | 언어 기반 작업 계획기 성능을 시뮬레이터 성공률로 자동 정량화하는 벤치마크. [사실][^ref-541] | ref-541 (원문 미열람) |
| AmbiK 데이터셋 | 오픈소스 | LLM의 모호성 탐지·되묻기 평가용 모호 작업 데이터(주방 환경). [사실][^ref-354] | ref-354 (원문 미열람) |

관련 법(표준이 아니므로 표 밖에 둔다): 한국 인공지능 기본법과 시행령은 2026-01-22 시행되었다(기준일 2026-01-22, 개정 법률의 시행일과 고영향 영역 목록은 미확인). [사실][^ref-737] EU AI Act(Regulation (EU) 2024/1689)는 제품 안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상인 AI를 고위험으로 분류한다. [사실][^ref-738] EU AI Act의 적용 시점은 개정(AI Omnibus) 논의로 이 페이지에서 확정하지 않는다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-734]: NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence, 2023-01-26, https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial, 접근일 2026-09-25 (원문 미열람)
[^ref-735]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-736]: ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management, 2023-02, https://www.iso.org/standard/77304.html, 접근일 2026-09-25 (원문 미열람)
[^ref-737]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 미확인, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-09-25 (원문 미열람)
[^ref-738]: European Commission, AI Act (Shaping Europe's digital future), 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-68 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-68 | 27. AI·학습·적응과 모델 운영 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-25-68/pages/topics/2026/2026-09-25-area27-s8.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영 — 대표 연구와 자료"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 27
related_areas: [5, 6, 13, 18, 19, 21, 23, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-056, ref-092, ref-354, ref-359, ref-541, ref-417, ref-088, ref-351, ref-742, ref-743, ref-744, ref-745]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md#8
---

[홈](../../index.md) › [주제](../index.md) › 27. AI·학습·적응과 모델 운영 — 대표 연구와 자료

# 27. AI·학습·적응과 모델 운영 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.
- 이 페이지는 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.

- Ahn 외, SayCan(2022) — LLM 과제 접지와 기술 가치 함수의 세계 접지를 결합한 로봇 계획. [사실][^ref-088]
- Liu, B. 외, LLM+P(2023) — 자연어→PDDL→고전 계획기 구조로 계획 검증을 외부 계획기에 맡긴다. [사실][^ref-092]
- Ren 외, KnowNo(2023) — 등각 예측으로 필요할 때 사람에게 도움을 요청하는 LLM 계획기(저자 보고). [사실][^ref-351]
- Liang 외, Code as Policies(2022) — 정해진 API 범위 안에서 정책 코드를 생성. [사실][^ref-742]
- Liu, J. X. 외, Lang2LTL(2023) — 자연어 명령을 LTL로 접지하는 방법과, LTL 식 템플릿에서 나온 식에 영어 발화를 대응시킨 말뭉치. [사실][^ref-056]
- AmbiK 데이터셋 — 모호한 작업과 모호하지 않은 짝 1000쌍(보정 100, 시험 900)에 모호성 유형, 명확화 질문과 답, 작업 계획을 필드로 둔다. [사실][^ref-354]
- Wang 외, Learning to Ask(arXiv 2024-09, 학회 게재판은 미확인) — NoisyToolBench와 Ask-when-Needed. [사실][^ref-359]
- LoTa-Bench — AI2-THOR 기반 ALFRED, VirtualHome 기반 Watch-And-Help 확장에서 성공률로 계획기를 평가. [사실][^ref-541]
- SafeGate(2026) — 실행 전 안전 판정(승인·거부·보류)과 작업 안전 계약. [사실][^ref-417]
- Agrawal 외, RTAW(2022, ICRA 2023) — 창고 작업 배정의 주의 기반 강화학습(저자 보고, 시뮬레이션 창고 조건, 단일 출처). [사실][^ref-743]
- Sculley 외, Hidden Technical Debt in Machine Learning Systems(NeurIPS 2015) — ML 고유 유지 비용 위험. [사실][^ref-744]
- Breck 외, The ML Test Score(IEEE Big Data 2017) — 28개 시험·감시 항목의 운영 준비도 기준표. [사실][^ref-745]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-742]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)
[^ref-743]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-744]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-745]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-68 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-68 | 27. AI·학습·적응과 모델 운영 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-25-68/pages/topics/2026/2026-09-25-area27-s10.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 27
related_areas: [5, 6, 13, 18, 19, 21, 23, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-541, ref-417, ref-738, ref-351, ref-743, ref-746]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md#10
---

[홈](../../index.md) › [주제](../index.md) › 27. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결

# 27. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 분류 원문 8장의 교차 규칙에 따라 이 영역의 AI 방법은 적용 대상 영역과 양쪽으로 연결된다.
- 이 페이지는 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

분류 원문 8장의 교차 규칙에 따라 이 영역의 AI 방법은 적용 대상 영역과 양쪽으로 연결된다.

- [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 교차 규칙상 매뉴얼 해석의 적용 대상이다. 매뉴얼 추출 방법은 다음 실행에서 반영 예정인 트랙 제안이다.
- [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 교차 규칙상 매뉴얼 해석의 적용 대상이다. 다음 실행에서 반영 예정인 트랙 제안이 있다.
- [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) — 교차 규칙상 도면 해석의 적용 대상이다. 도면 해석 방법은 다음 실행에서 반영 예정인 트랙 제안이다.
- [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md) — 교차 규칙상 학습 기반 배차의 적용 대상이며, RTAW 같은 강화학습 배정이 맞물린다. [추정][^ref-743]
- [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) — 교차 규칙상 장애 분석의 적용 대상이다. 이번 조사에는 장애 분석 자료가 없다.
- [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) — 불확실할 때 사람에게 확인을 요청하는 KnowNo 방식이 맞물린다. [추정][^ref-351]
- [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) — 실행 전 안전 판정(SafeGate)과 제품 안전 구성요소 규제(EU AI Act)가 맞물린다. [추정][^ref-417][^ref-738]
- [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) — 모델 버전·변경 관리가 맞물린다. [추정][^ref-746]
- [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) — LoTa-Bench 같은 계획기 평가 벤치마크가 맞물린다. [추정][^ref-541]
- [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) — 고영향 인공지능 책무를 ROP 사업자와 현장 운영사 중 누가 지는지가 11절의 열린 질문이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-738]: European Commission, AI Act (Shaping Europe's digital future), 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-743]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-68 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-68 | 27. AI·학습·적응과 모델 운영 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-25-68/pages/topics/2026/2026-09-25-area27-s4.md

```markdown
---
title: "27. AI·학습·적응과 모델 운영 — 핵심 개념과 용어"
type: topic
category: "G. 안전·보안·지능·거버넌스"
primary_area_no: 27
related_areas: [5, 6, 13, 18, 19, 21, 23, 24, 25, 28]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-092, ref-359, ref-735, ref-088, ref-351, ref-746]
last_run: 2026-09-25
version: 1
split_from: docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md#4
---

[홈](../../index.md) › [주제](../index.md) › 27. AI·학습·적응과 모델 운영 — 핵심 개념과 용어

# 27. AI·학습·적응과 모델 운영 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.
- 이 페이지는 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.

- **과제 접지·세계 접지(Task grounding / World grounding)** — SayCan에서 대규모 언어 모델(Large Language Model, LLM)이 상위 지시에 유용한 행동을 고르는 것이 과제 접지, 사전 학습된 기술의 가치 함수가 현재 실행 가능성을 판정하는 것이 세계 접지다. [사실][^ref-088]
- **PDDL(Planning Domain Definition Language)** — LLM+P가 자연어 문제 설명을 고전 계획기에 넘기려고 바꾸는 중간 형식이다([용어집](../../glossary/pddl.md)). [사실][^ref-092]
- **등각 예측(Conformal Prediction)** — KnowNo가 LLM 계획기의 불확실성을 보정해 과제 완수에 통계적 보장을 두는 데 쓰는 방법이다(저자 보고). [사실][^ref-351]
- **LLM 에이전트(LLM Agent)** — 도구를 호출하는 LLM 에이전트는 불완전한 지시에서 빠진 인자를 지어내는 문제가 보고되었다([용어집](../../glossary/llm-agent.md), [환각](../../glossary/hallucination.md)). [사실][^ref-359]
- **AI 관리 시스템(Artificial Intelligence Management System, AIMS)** — ISO/IEC 42001:2023이 수립·실행·유지·지속 개선 요구사항을 정하는 조직 차원의 관리 체계다. [사실][^ref-735]
- **모델 레지스트리(Model Registry)** — MLflow의 모델 레지스트리는 등록 모델마다 버전·별칭·태그와 계보(어느 실험·실행이 만들었는지)를 관리한다. [사실][^ref-746]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md), [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md), [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md), [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md), [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md), [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md), [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md), [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md), [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md), [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-735]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-746]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-25-68 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-25 | 2026-09-25-68 | 27. AI·학습·적응과 모델 운영 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-25-68/docs_tree.txt

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 593건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 153개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
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
- lane-closure: 차선 폐쇄 (Lane Closure)
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
- model-checking: 모델 검사 (Model Checking)
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
```

### docs/open-questions.md (요약: 대상 영역 [27] 에 걸린 1건 / 전체 98건)

```markdown
- oq-030 [열림] 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? (영역 13, 27)
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

### runs/2026-09-25-68/verification2.json

```json
{
  "run_id": "2026-09-25-68",
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
    "세부영역 페이지 7절 첫 문장과 docs/topics/2026/2026-09-25-area27-s7.md 의 1절 첫 항목·3절 첫 문장 '조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. [사실][^ref-735]': [사실] 태그와 [^ref-735] 를 떼고 태그 없는 안내 문장으로 두거나 [추정](이 위키의 정리)으로 바꾼다 — 여러 표준·도구를 묶은 이 위키의 판단이고 ref-735(ISO/IEC 42001)는 이 문장을 뒷받침하지 않으며, 브리프에 이 문장에 대응하는 [사실] finding 이 없다(태그 상향·드리프트).",
    "세부영역 페이지 8절 첫 문장과 docs/topics/2026/2026-09-25-area27-s8.md 의 1절 첫 항목·3절 첫 문장 '아래 자료는 모두 원문 미열람 상태에서 검색 결과로 확인했고, 수치는 저자 보고다. [사실][^ref-351]': 태그와 각주를 떼고 검증 상태 안내 문장으로 둔다. 또한 '모두'를 '대부분'으로 고치거나 'AmbiK(ref-354)와 LoTa-Bench(ref-541)는 검증 과정에서 공식 저장소 README 로 확인했다'를 덧붙인다 — ref-351(KnowNo 논문)은 이 메타 진술의 근거가 아니고, 1차 검증 노트에 따르면 두 출처는 GitHub README 로 확인됐다.",
    "docs/topics/2026/2026-09-25-area27-s8.md 3절 KnowNo 항목: '필요할 때만 사람에게 묻는'을 '필요할 때 사람에게 도움을 요청하는'으로 고치고 '(저자 보고)'를 붙인다 — 1차 수정 지시(f8)가 '필요할 때'와 저자 보고 한정이었고 fixes_applied 도 8절 반영을 보고했으나 이행되지 않았다.",
    "세부영역 페이지 6절 첫 단락의 '아래 도식은 3절의 겹 구조를 이 위키가 그린 것이다.'를 '3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.'처럼 고친다 — 자동 분리로 도식이 주제 페이지로 옮겨져 세부영역 페이지에서는 가리키는 대상이 없다(주장·태그 변경 없음)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다. 확인 25건, 미확인 0건, 교차 확인 0건. 강등: 없음. 대신 f1·f6·f8·f14·f16·f17 은 검색 스니펫 범위로 문구를 줄이도록 지시했다. 원문 미열람 출처: ref-734, ref-735, ref-736, ref-737, ref-738, ref-088, ref-092, ref-351, ref-742, ref-743, ref-744, ref-745, ref-746, ref-747, ref-359, ref-056, ref-417. ref-354(AmbiK)와 ref-541(LoTa-Bench)은 검증 에이전트가 GitHub 공식 저장소 README 를 열어 확인했다. 주의: 사실로 둔 주장은 모두 단일 출처이고 논문 수치는 저자 보고다. 5절 시나리오와 9절 범위 구분은 이 위키의 추정이다. ref-738(EU AI Act 안내 페이지)은 정확한 URL 이 검색 결과에 나오지 않아 같은 포털 내용으로만 약하게 확인했다. 한국 인공지능 기본법의 개정 법률 내용과 EU AI Act 적용 시점은 미확인이다. oq-030 은 이번에 조사하지 않아 열림으로 남는다. 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 2건(7절·8절 도입 문장에 브리프에 없는 [사실] 태그와 맞지 않는 각주, 분리 주제 페이지 s7·s8 에도 같은 문장) 수정 지시, 8절 분리 페이지 KnowNo 문구의 1차 지시 미이행 1건, 6절 도식 지시어 1건. 그 밖의 1차 수정 지시(f1·f4·f5·f6·f11·f14·f15·f16·f17·f19·f21·f22, 10절 교차 규칙 연결, 11절 oq-030 유지, 각주 원문 미열람 표기)는 이행을 확인했다. [분류원문] 보존, 섹션 순서 준수, 링크 유효. 범위 경계(f19 거점 간 운송 연계, f24 연계 대상)와 8. 실시간 세계 상태·데이터 일관성/22. 시뮬레이션·예측용 디지털 트윈 구분에 문제 없음. 참고: reference_updates 가 기존 id(ref-088·092·351·354·359·056·541·417)에도 source_unopened: true 를 넣으므로 퍼블리셔가 기존 참고문헌 페이지의 열람 표시를 덮어쓰지 않는지 확인이 필요하다.",
  "retry_reason": null
}
```
