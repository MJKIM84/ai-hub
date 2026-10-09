(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-09
- date: 2026-10-09
- run_type: category_link (대분류 연결)
- 대상: 대분류 M. 안전 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
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

### runs/2026-10-09-09/target.json

```json
{
  "run_id": "2026-10-09-09",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 142,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "M. 안전",
    "category_letter": "M"
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
  "selection_rationale": "CLI 지정 run_type=category_link"
}
```

### runs/2026-10-09-09/research.json

```json
{
  "run_id": "2026-10-09-09",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "M. 안전"
  },
  "gaps": [
    "M. 안전 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 48. 안전·위험 관리, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사와 다른 16개 대분류의 연결이 정리되지 않았다",
    "48. 안전·위험 관리 페이지는 이전 분류(2026-09-26) 기준이라 C. 채팅 기반 구성·운영, K. 플랫폼 아키텍처·인프라, O. 검증·도입·수명주기의 56. 운영 이관·확대·교육, P. 거버넌스·법규·사회와 잇는 근거가 페이지 안에 없다",
    "48·49·50 페이지의 10절(다른 연구영역과의 연결)은 49·50 이 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다",
    "정지·재개 판단에 쓰는 VDA 5050 안전 상태·운용 모드의 원문 확인과, 관제 통신이 끊겼을 때의 정지 경로(oq-095) 근거가 약하다",
    "ANSI/A3 R15.08-3(사용자 의무)과 국내 로봇작업 특별교육처럼 운영·교육 쪽 근거(oq-265, oq-275)가 게시 페이지에 없다",
    "Q. 현장 유형별 적용의 64. 상업 시설에 사람 근접 안전 적용 사례가 없다"
  ],
  "research_questions": [
    "여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]",
    "48. 안전·위험 관리의 정지·재개 판단은 B. 로봇 온톨로지(6)·F. 연동(20·21·22)·H. 실행·협업·예외 복구(29·31·32)·K. 플랫폼 아키텍처·인프라(42)의 어떤 상태·명령·통신 경로에 기대는가? (oq-095, oq-229 관련)",
    "49. 사람 근접 안전의 구역·속도·사람 흐름 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(18·19)·G. 계획·최적화(25·27·28)·I. 설계·시뮬레이션(34·36)과 어떻게 이어지는가?",
    "50. 안전 표준·인증·사고 조사의 표준 개정·인증·사고 기록은 A. 기획·사업(1·2·3)·J. 현장 운영·관제(37·38·40)·N. 보안·개인정보(51·52·53)·O. 검증·도입·수명주기(54·55·56·57)·P. 거버넌스·법규·사회(58·59·60)와 어디서 만나는가? (oq-102, oq-252, oq-254, oq-265, oq-275 관련)",
    "언어 모델이 지시하는 로봇 계획의 안전 검사는 C. 채팅 기반 구성·운영(12·13)과 L. AI·학습 기술(44·47)의 '사람이 확인·승인한 계획만 실행' 원칙과 어떻게 맞물리는가? (oq-106, oq-144 관련)",
    "M. 안전의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며, 한국 법령·인증·사고 자료는 무엇이 있는가?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: ANSI/A3 R15.08 시리즈는 로봇 자체(1부), 산업용 이동로봇 시스템·적용의 통합(2부, 2023), 사용자의 산업용 이동로봇 적용 사용(3부, 2026)으로 나뉘어 제조사·통합자·사용자의 안전 책임을 부별로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1419",
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ANSI 블로그는 3부가 \"describes user responsibilities for safe operation of IMR applications\"라고 쓰고 유형 A·B·C 정의는 1부를 따른다고 적는다. 2부가 IMR 시스템·적용 통합 안전을 다룬다는 것은 The Robot Report(2023-10-26) 기준.",
      "as_of": "2026-09-17",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f2",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: R15.08 시리즈가 통합자와 사용자의 의무를 따로 두므로, 여러 제조사 로봇을 묶는 ROP 사업자가 현장마다 통합자 역할을 맡는지 사용자의 위험성평가를 지원하는 역할에 머무는지가 책임 범위 정의에 들어가야 할 것으로 보인다(oq-096).",
      "tag": "추정",
      "source_ids": [
        "ref-1419",
        "ref-1084",
        "ref-472"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "2부는 통합, 3부는 사용자 의무로 나뉜다. ROP 사업자의 해당 역할을 정한 자료는 찾지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f3",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 주요 로봇 안전 표준의 개정이 2025~2026년에 몰려 있다. ISO 10218-1/-2 개정판은 2025-02에 나왔고 EN ISO 판의 참조가 2026-09-07 EU 관보에 실렸다. ANSI/A3 R15.08-3 은 A3 판매 페이지 기준 2026-04-23에 발행됐고, ISO 13482 개정판은 2026-09-15 기준 FDIS 단계다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116",
        "ref-1420",
        "ref-1117"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IBF: \"On 7 September 2026, their references were published in the Official Journal\". A3 판매 페이지: 발행일 2026-04-23, 77쪽. ISO 13482 단계는 50. 안전 표준·인증·사고 조사 페이지의 ref-1117 기준이다.",
      "as_of": "2026-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f4",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 2023-11-17 시행된 개정 지능형로봇법에 따라 보도에서 실외이동로봇을 운영하는 자는 보험(또는 공제)에 의무 가입해야 한다. 산업통상자원부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정해 보험상품 출시를 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1424"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메트로신문(2023-11-16): 보도에서 운영하는 자는 \"보험(또는 공제)에 의무적으로 가입해야 합니다.\" 운행안전인증 대상은 질량 500kg·속도 15km/h 이하·폭 800mm 미만이다. 조항 번호는 기사에 없다.",
      "as_of": "2023-11-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 실외 로봇 도입에서는 보험 가입과 인증 유지가 운영비 항목이 될 것으로 보인다. 인증 단위가 로봇과 관제장치의 조합이므로, 관제를 맡는 ROP 사업자가 운영자 의무 범위에 드는지가 조달·계약 단계의 쟁점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1424",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "보험 의무는 운영자에게 있다(기사). 인증 대상은 로봇과 관제장치의 조합이다(진흥원 페이지, 49. 사람 근접 안전 페이지 기준).",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f6",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동·H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 운용 모드 가운데 AUTOMATIC 은 관제가 로봇을 완전히 제어하는 상태, SEMIAUTOMATIC 은 관제가 제어하되 주행 속도를 HMI 가 조정하는 상태다. INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 로봇을 제어하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AUTOMATIC: \"Fleet control is in full control of the mobile robot.\" MANUAL·SERVICE·TEACH_IN 등은 관제가 제어하지 않는 상태이며, SERVICE 에서는 권한 있는 인력이 로봇을 재구성할 수 있다(3.0.0, 7.8절·6.6.6절).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: 6. 온톨로지 기반 시스템·로봇 연동의 '실행 시점 조건 판단'에 배터리·적재 상태와 함께 운용 모드와 안전 상태(비상정지·보호 필드 침범)를 넣어야, 관제가 제어권이 없는 로봇에 작업을 내리지 않을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 상태 메시지에는 운용 모드와 safetyState(activeEmergencyStop, fieldViolation)가 함께 들어 있다. 이를 능력 실행 조건에 넣은 공개 구현은 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 로봇마다 R15.08 유형(A·B·C), 적용 안전 표준과 판, 인증 상태를 등록 정보로 두면 표준 개정과 인증 범위를 배정·경로 제약으로 추적할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1419",
        "ref-1116",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "R15.08-3 은 유형 A·B·C 시스템에 적용된다. ISO 10218 은 판이 바뀌었고, 실외 인증은 질량·속도 조건이 붙는다. 50. 안전 표준·인증·사고 조사 페이지 9절의 등록 제안을 이어받은 것이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f9",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트(SafeGate)와 작업 안전 계약을 두는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems(arXiv 2604.05427). 48. 안전·위험 관리 페이지 10절에서 재인용했다.",
      "as_of": "2026-04",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: Ravichandran 외의 RoboGuard 에서는 악성 프롬프트와 격리한 신뢰 기점 LLM 이 미리 정한 안전 규칙을 시간 논리 제약으로 바꾸고 제어 합성으로 계획과의 충돌을 푼다. 저자들은 최악의 탈옥 공격에서 위험 계획 실행이 92% 이상에서 3% 미만으로 줄었다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-700"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "저자 보고값이며 독립 재현은 확인하지 못했다. 2026-03 개정판 기준이다. (재인용: 2026-10-09-08)",
      "as_of": "2026-03-03",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Robey 외(2024-10)는 언어 모델이 제어하는 로봇이 해로운 물리 행동을 하도록 만드는 탈옥 알고리즘 RoboPAIR 를 제시했다. GPT-4o 계획기를 쓴 Clearpath Jackal 과 GPT-3.5 를 연동한 Unitree Go2 등에서 공격 성공률이 자주 100%에 이르렀다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-857"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Jailbreaking LLM-Controlled Robots(arXiv 2410.13691). 저자 보고값이다. (재인용: 2026-10-09-08)",
      "as_of": "2024-10-17",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션·13. 대화형 기능의 신뢰·기반: 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙에 실행 전 안전 게이트·가드레일 같은 자동 검사를 더하면, 대화 지시에서 로봇 동작까지 이어지는 경로가 48. 안전·위험 관리의 위험성평가 대상이 될 것으로 보인다. 로봇 자체 안전 기능은 연계 대상으로 남는다.",
      "tag": "추정",
      "source_ids": [
        "ref-417",
        "ref-700"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 연구 모두 언어 모델 계획과 실행 사이에 검사 계층을 둔다. 다중 로봇 플릿의 배정·경로 계획에 적용한 사례는 찾지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리·F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 여기거나 적용해서는 안 된다고 범위 절에 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Scope: \"does not define functional, operational, or system safety requirements\"이며, 안전 표준으로 \"shall not be regarded or applied\"라고 적는다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: VDA 5050 3.0.0 의 BLOCKED 구역에는 로봇이 들어가서는 안 되며, 구역 안에 있는 로봇은 멈추고 BLOCKED_ZONE_VIOLATION 오류를 CRITICAL 수준으로 보고한다. SPEED_LIMIT 구역에서는 구역에 들어설 때 이미 최대 속도(m/s) 이하여야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.4.1.1절 표 6의 윤곽 기반 구역 정의다. BLOCKED 구역은 LINE_GUIDED 구역보다 우선한다(6.4.4절).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 지도에 붙은 진입 금지·속도 제한 구역은 VDA 5050 이 정한 교통 관리 규칙이며 안전 기능이 아니다. 따라서 위험성평가에서 이를 위험 감소 조치로 인정받으려면 ISO 3691-4 의 운용 구역 준비와 로봇의 안전 등급 보호 필드 설정에 맞춰야 할 것으로 보인다(oq-229).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-470"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 은 안전 요구를 정하지 않는다. ISO 3691-4 는 운용 구역 준비를 부속서 A 에 둔다(원문 미열람). 둘을 잇는 검증 주체는 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f16",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고, 운용 구역 준비를 부속서 A 에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "48. 안전·위험 관리 페이지 4절의 운용 구역 정의에서 재인용했다. 표준 본문은 열람하지 않았다(oq-170).",
      "as_of": "2023-06",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "연계 대상: M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: Abdul Hafez 외(IJRR, 2025-05)는 무결성 위험 지표로 EKF 기반 SLAM 위치추정의 안전성을 정량화했다. 데이터 연관 오류가 위치를 크게 해칠 수 있고, 랜드마크 밀도가 지나치게 높으면 안전성이 오히려 떨어진다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-161"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SLAM 위치추정 자체는 분류 원문 19장의 '로봇 자체 지능·제어' 경계에 속한다. D. 공간·지도 모델 페이지 M 절에서 재인용했다.",
      "as_of": "2025-05",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Open-RMF 승강기 상태(LiftState)의 현재 모드에는 알 수 없음·사람·AGV·화재·오프라인·비상이 있다. 이 가운데 사람·AGV 모드만 설정할 수 있고 나머지는 읽기 전용이다.",
      "tag": "사실",
      "source_ids": [
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "E. 사물·사람·실시간 상태 페이지 M 절에서 재인용했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f19",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: 승강기의 화재·비상 모드 제어는 시설·설비 제어 경계의 연계 대상이다. ROP 는 탑승을 확정하기 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "모드가 읽기 전용이므로 ROP 몫은 확인과 반영이다. 모드 정보를 몇 초까지 믿을지는 oq-034 다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f20",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고, 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1181"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "조선비즈 2024-07-12 기사 1건 기준이다. E. 사물·사람·실시간 상태 페이지 D 절에서 재인용했다.",
      "as_of": "2024-07-12",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 병원의 사람·휠체어 대기 규칙이나 창고의 학습된 사람 흐름처럼 사람 흐름 정보는 구역·시간대별 대기·속도 규칙으로 49. 사람 근접 안전과 이어질 것으로 보인다. 이때 사람 검출·안전 정지는 로봇이 맡는 연계 대상이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1181",
        "ref-1180"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ILIAD 는 학습한 사람 흐름에 맞춰 창고 자율 지게차 경로를 계획했다. 병원 사례는 기사 1건 기준이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-945"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "국가기술표준원 보도(KDI 경제정보센터 게재, 2021-11-11)이며, 50. 안전 표준·인증·사고 조사 페이지 3절에서 재인용했다.",
      "as_of": "2021-11-11",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동·N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 구성을 로봇 유형별로 바꾸고 탑승형 로봇 절을 뺐다. 사이버보안, 데이터 보호, 승강기와 협동하는 로봇(참고 부속서 H) 절을 새로 넣었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DIN Media 초안 소개: \"Die Struktur des Dokuments wurde von Sicherheitsanforderungen in spezifische Robotertypen geändert\". 초안 기준이며 최종판 반영 여부는 확인하지 못했다.",
      "as_of": "2024-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 로봇의 승강기 탑승 안전 요구가 국내 KS 와 서비스 로봇 안전 표준 개정 초안 양쪽에 들어오므로, ROP 는 승강기 연동 요청·운영 모드 확인을 맡고 탑승 안전의 적합성은 로봇·승강기 쪽 표준에 맡기는 경계가 될 것으로 보인다. 개정 초안 내용이 최종판에 남았는지는 확인하지 못했다(oq-254).",
      "tag": "추정",
      "source_ids": [
        "ref-945",
        "ref-1425",
        "ref-1117"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "KS B 7317(2021)과 ISO/DIS 13482:2024 부속서 H 가 있고, ISO 13482 는 FDIS 단계다. 두 문서의 대응 관계는 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f25",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: Open-RMF 기능 요청 이슈 #658 은 화재경보가 울리면 로봇들이 주차 위치로 이동하지만, 비상 신호가 대상 플릿을 구분하지 않는 불리언 값이라고 지적한다.",
      "tag": "사실",
      "source_ids": [
        "ref-567"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "이슈 작성 시점(2025-04-04) 기준이며 이후 구현 여부는 확인하지 못했다. 48. 안전·위험 관리 페이지 5절에서 재인용했다.",
      "as_of": "2025-04-04",
      "site_type": null,
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: ISO 21423(산업용 이동로봇 통신·상호운용성)의 범위는 여러 제조사 AMR·플릿 관리 장비·기업 자원 사이의 통신 프로토콜이다. 안전 요구와 공공 도로 이동 기계는 범위에서 뺀다.",
      "tag": "사실",
      "source_ids": [
        "ref-159"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "D. 공간·지도 모델 페이지 F 절(확인일 2026-10-09, 발행 진행 중 단계 60.00)에서 재인용했다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 과 ISO 21423 같은 상호운용 표준이 안전 요구를 범위에서 빼므로, 연동 적합성 시험(21. 상호운용 표준·적합성)과 안전 표준 적합성·인증(50. 안전 표준·인증·사고 조사)은 별도 경로로 관리해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-159"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 문서 모두 안전 요구를 정하지 않는다고 범위에서 밝힌다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f28",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Kazemi Eskeri 외(IROS 2025)는 사람과 함께 쓰는 환경에서 사람을 고려하는 다중 로봇 작업 배정 방법을 다뤘다.",
      "tag": "사실",
      "source_ids": [
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments(arXiv 2508.19731). 49. 사람 근접 안전 페이지 6절·9절에서 재인용했다.",
      "as_of": "2025-08-27",
      "site_type": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: Open-RMF 데모에서는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_demos README 기준이다. G. 계획·최적화 페이지 옛 G 절에서 재인용했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RMF Core Overview 기준이다. 48. 안전·위험 관리 페이지 5절에서 재인용했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f31",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Reliability Engineering & System Safety 게재 연구(2023)는 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 확률 페트리넷(SPN)으로 모델링·분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-565"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN. 저자는 확인하지 못했다.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 안전 상태(safetyState)는 activeEmergencyStop 을 MANUAL(로봇에서 수동 확인), REMOTE(시설 비상정지를 원격 확인), NONE 으로 보고하고, fieldViolation 으로 레이저·범퍼 같은 보호 필드 침범 여부를 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "7.8절: REMOTE 는 \"facility emergency stop shall be acknowledged remotely\"이다. 3.0.0 본문에서 AUTOACK 값은 찾지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f33",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성·31. 사람–로봇 협업: ROP 의 재개 지시는 비상정지가 NONE 이고 운용 모드가 AUTOMATIC 으로 돌아온 것을 확인한 뒤에 내려야 할 것으로 보인다. MANUAL 비상정지는 로봇에서 사람이 확인해야 하므로 현장 인력 출동이 복구 절차에 들어갈 것으로 보인다(oq-095).",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "안전 상태와 운용 모드 정의에서 끌어낸 판단이다. 재개 판정 규칙을 정한 표준은 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f34",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "4.1절: \"fulfills the order up to the last released node\".",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f35",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 2026-09 식품 제조 공장에서 멈춘 제품 적재 로봇을 점검하던 노동자가 끼여 숨진 사고에 대해, 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "경남도민일보 2026-09-29 보도 기준이며 원인은 확정되지 않았다. 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다.",
      "as_of": "2026-09-29",
      "site_type": "제조 공장",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f36",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 2023-11 농산물유통센터에서 상자를 팔레트로 옮기는 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1124"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "경향신문 2023-11-08 보도 기준이다. 경찰은 로봇이 사람을 상자로 인식한 것으로 보았다. 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다.",
      "as_of": "2023-11-08",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f37",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 확인한 두 사망 사고가 모두 점검·작동 확인 같은 비정상 작업 중에 났으므로, ROP 가 정지 뒤 재가동·재개를 지시하기 전에 작업 중인 사람과 잠금 상태를 확인하는 절차가 복구 절차와 운영 절차의 접점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1124",
        "ref-1125",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 사고는 기사 기준이다. 플릿 관제의 재개 지시와 잠금·표지를 잇는 공개 절차는 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f38",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 만들어, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1241"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Simulation-based Testing for Early Safety-Validation of Robot Systems(arXiv 2011.10294). (재인용: 2026-10-09-07)",
      "as_of": "2020-11-20",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션에 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Simulation 장 기준이다. 이는 가정한 미래를 실험하는 쪽이며 현재 상태 표현(18. 실시간 세계 상태·데이터 일관성)과 구분한다. (재인용: 2026-10-09-07)",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f40",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Rondoni 외(Scientific Reports, 2024-08)는 모의 병원 환경에서 병원 물류 로봇 HOSBOT 과 TIAGo 를 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 7개 지표로 비교했다. 최고 속도에서는 방향 오차가 커졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실제 병원이 아닌 시뮬레이션 평가다. 49. 사람 근접 안전 페이지 5절에서 재인용했다.",
      "as_of": "2024-08-07",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "연계 대상: M. 안전의 50. 안전 표준·인증·사고 조사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Wind River 인터뷰(2014)는 IEC 61508-7 이 시뮬레이션을 시험 목적의 설비 거동 모사로 정의한다고 인용하고, 기능안전 표준이 안전 확인에 시뮬레이션을 권고한다고 해석했다. 그러나 이동로봇 안전 인증이 시뮬레이션 결과를 근거로 받아들이는 절차는 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1249"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "업체 블로그의 표준 인용이며, IEC 61508-7 원문은 열람하지 않았다. (재인용: 2026-10-09-07)",
      "as_of": "2014-11-20",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Winfield 외(2022-05)는 사회적 로봇의 사고 조사를 위한 윤리적 블랙박스(Ethical Black Box) 개방 표준 초안을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1120"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "An Ethical Black Box for Social Robots: a draft Open Standard(arXiv 2205.06564). 50. 안전 표준·인증·사고 조사 페이지에서 재인용했다.",
      "as_of": "2022-05-13",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: Sanders·Sener·Chen(Applied Ergonomics, 2024)은 미국 OSHA 중대 부상 보고(Severe Injury Reports)에서 작업장 로봇 관련 부상을 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1122"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports. 50. 안전 표준·인증·사고 조사 페이지 8절에서 재인용했다.",
      "as_of": "2024",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 플릿 수준에서 명령·정지·재가동·운용 모드 전환·안전 상태 보고를 시각과 함께 남기는 실행 기록이 사고·아차 사고 조사의 입력이 될 것으로 보인다. 그 최소 항목을 정한 표준은 확인하지 못했다(oq-252).",
      "tag": "추정",
      "source_ids": [
        "ref-1120",
        "ref-1122",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "윤리적 블랙박스 초안은 사회적 로봇 단위이고, VDA 5050 은 안전 상태·운용 모드를 보고한다. 둘을 플릿 기록으로 잇는 공개 규약은 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f45",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Ferrando 외(2020)의 ROSMonitoring 은 ROS 응용의 형식 속성을 ROS 바깥에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 여러 ROS 배포판에 옮겨 쓸 수 있고 특정 명세 형식에 묶이지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1426"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준: \"portability across multiple ROS distributions\". 시험 대상은 Mars Curiosity 로버 시뮬레이션이다(LNCS, 2020-12-03).",
      "as_of": "2020-12-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 진입 금지 구역 위반이나 정지 지시 뒤 응답처럼 안전과 관련된 운영 규칙을 실행 중에 감시하는 런타임 검증이 38. 모니터링·이상 탐지·원인 분석과 48. 안전·위험 관리를 잇는 방법이 될 것으로 보인다. 다만 제조사가 다른 플릿에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1426",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ROSMonitoring 은 단일 ROS 시스템 대상이다. VDA 5050 구역 위반은 BLOCKED_ZONE_VIOLATION 오류로 보고된다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f47",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: ANSI/A3 R15.08-3-2026 은 산업용 이동로봇을 운영하는 사용자에게 위험성평가와 그 결과 위험 감소 조치의 유지, 변경 관리, 직원 교육과 안전 작업 절차를 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1419",
        "ref-1421"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "ANSI 블로그(2026-09-17)는 위험성평가·기록 유지·교육·안전 작업 절차를, Robotics 24/7(2026-10-04)은 위험성평가·변경 관리·직원 교육·정기 검토와 점검을 든다. 표준 본문은 유료라 열람하지 않았다.",
      "as_of": "2026-10-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f48",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: R15.08-3 의 사용자 교육·안전 작업 절차 요구는 40. 운영 절차·요청 창구의 현장 절차와 56. 운영 이관·확대·교육의 교육 계획으로 넘어갈 것으로 보인다. 여러 제조사 로봇이 섞인 현장에서 누가 이를 이행하는지는 확인하지 못했다(oq-265).",
      "tag": "추정",
      "source_ids": [
        "ref-1419",
        "ref-1421"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 출처 모두 사용자 의무를 들지만 이종 플릿의 이행 주체는 다루지 않는다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f49",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: FORT Robotics 사례 소개에 따르면, 한 창고의 울타리 친 AMR 구역에서 문에 단 주 제어기가 문이 열리면 모든 로봇에 무선 안전 비상정지를 보낸다. 이 시스템은 ISO 13849 범주 3·PLd 로 설계됐다고 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1422"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 로봇마다 차량 안전 제어기(VSC)를 달고 주파수 도약 무선으로 연결하며, 소규모 시험 운영 단계다. 플릿 관리 시스템·WMS 연동은 언급하지 않는다(A3 게재, 2023-05-18).",
      "as_of": "2023-05-18",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f50",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 은 안전 표준이 아니고, 연결이 끊긴 로봇은 받은 주문을 이어 수행한다. 따라서 플릿 일괄 정지는 관제 메시지 경로가 아니라 그와 독립된 안전 등급 정지 경로에 맡기고, ROP 는 정지 결과를 상태로 받아 작업을 보류·재배정하는 구조가 두 대분류의 경계가 될 것으로 보인다(oq-095).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1422"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 범위와 연결 단절 동작, 그리고 무선 안전 정지 사례(벤더 주장)에서 끌어낸 판단이다. 이 구조를 규정한 표준은 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f51",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act(Regulation (EU) 2024/1689)는 부속서 I 의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이면서 제3자 적합성 평가를 받는 AI 시스템을 고위험 AI 로 분류한다.",
      "tag": "사실",
      "source_ids": [
        "ref-621"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "European Commission AI Act 정책 페이지 기준이다. (재인용: 2026-10-09-08)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f52",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법무법인 태평양 해설에 따르면 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을 정하게 하고, 운영 단계에서 성능 저하·오류의 정기 점검과 관리자 교육을 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1341"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2025-09 초안 기준의 법무법인 해설이며, 확정 고시 원문은 확인하지 못했다. (재인용: 2026-10-09-08)",
      "as_of": "2025-09-30",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f53",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영: AI 가 정지·경로·구역 결정에 관여하면 실행 전 안전 게이트 같은 채택 검사는 47. AI·학습·적응과 모델 운영의 채택 기준과 48. 안전·위험 관리의 위험성평가 양쪽에 걸칠 것으로 보인다. 이런 AI 가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106).",
      "tag": "추정",
      "source_ids": [
        "ref-621",
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "고위험 분류 기준과 실행 전 안전 게이트 연구를 함께 본 판단이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f54",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116",
        "ref-1076"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "IBF: 개정 항목에 \"cybersecurity and risk assessment\"가 포함된다. Hartmann 외(2026-02)는 네트워크 로봇 시스템의 무단 접근 방지 요구가 추가됐다고 분석한다. 조항 번호는 확인하지 못했다(oq-102).",
      "as_of": "2026-09-18",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f55",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EN ISO 10218-1:2025·-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015 에 따라 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IBF Solutions 2026-09-18 기사 기준이다. 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 기사에 없다.",
      "as_of": "2026-09-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f56",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1242"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety(arXiv 2211.09507). (재인용: 2026-10-09-07)",
      "as_of": "2022-11-17",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f57",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제와 사람 위치·영상 데이터 처리도 안전 평가 대상이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1116",
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ISO 10218(2025) 개정과 ISO/DIS 13482:2024 초안의 새 절에서 끌어낸 판단이다. 플랫폼 명령 경로에 적용한 기준은 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f58",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: Belzile 외(2025-02)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 여러 배치 상황에 적용할 수 있는 표준이 없다고 보았다. 이에 건설 현장 이동로봇 배치 전에 쓸 위험성평가 틀을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-563"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "프리프린트이며, 50. 안전 표준·인증·사고 조사 페이지 5절의 기타 사례에서 재인용했다.",
      "as_of": "2025-02",
      "site_type": "기타",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f59",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 법령해석 23-0872(2023-11-21)는 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 '산업용 로봇'을 쓰는 작업으로 한정되지 않는다고 회답했다. KS B ISO 8373 의 '로봇'이 산업용·서비스용·의료용을 포괄한다는 점을 근거로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "회답: \"'산업용 로봇'을 사용하는 작업으로 한정되지 않습니다.\" 법원 판결 같은 기속력은 없다(네플라 위키 게재본으로 열람).",
      "as_of": "2023-11-21",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f60",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 해석에 따르면 서비스·이동 로봇을 쓰는 작업도 로봇작업 특별교육 대상이 될 수 있으므로, ROP 를 들인 현장의 운영 이관 교육 계획에 법정 특별교육 해당 여부 판단이 들어가야 할 것으로 보인다. 고용노동부의 적용 지침은 확인하지 못했다(oq-275).",
      "tag": "추정",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "해석은 로봇 범위를 산업용으로 한정하지 않았다. 서빙·배송 로봇 운영 인력에 실제로 적용한 사례는 찾지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f61",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: R15.08-3 은 공급자가 배치한 뒤 사용자가 산업용 이동로봇이나 그 적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다고 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1419"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ANSI 블로그(2026-09-17) 요약 기준이다. 사용자가 IMR, 적용 또는 운영 환경을 바꾸면 같은 의무가 적용된다.",
      "as_of": "2026-09-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f62",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROP 에서 구역·속도 제한·경로망·운영 정책을 바꾸는 일이 사용자 쪽 변경 관리와 위험성 재평가의 계기가 될 수 있으므로, 설정 변경 이력을 판 단위로 남기고 재평가 필요 여부를 표시하는 기능이 두 영역을 잇는 것으로 보인다(oq-093, oq-282).",
      "tag": "추정",
      "source_ids": [
        "ref-1419",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "R15.08-3 의 변경 관리 요구와 VDA 5050 의 관제 측 구역·지도 설정에서 끌어낸 판단이다. 이 설정 변경이 법적으로 '변경'에 해당하는지는 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f63",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Francis 외(2023)는 사회적 로봇 내비게이션 알고리즘의 평가 원칙과 지침을 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Principles and Guidelines for Evaluating Social Robot Navigation Algorithms(ACM THRI, arXiv 2306.16740). E. 사물·사람·실시간 상태 페이지 O 절에서 재인용했다.",
      "as_of": "2023-06-29",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f64",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: ANSI/A3 R15.08-2(2023-10)는 산업용 이동로봇 시스템과 적용의 안전 요구를 다루는 2부로 발표됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-472",
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "A3 발표와 The Robot Report 기사는 같은 발표를 다뤄 독립 출처로 보지 않았다. 통합자의 시스템 수준 위험성평가 주체는 oq-096 이다.",
      "as_of": "2023-10",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f65",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거하며, 인증 절차와 기준은 산업통상자원부 고시(2023-11-17)로 정해졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-980",
        "ref-1118"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다. 심사 항목 수는 출처마다 8개와 16가지로 달라 정하지 않는다(oq-186, oq-230).",
      "as_of": "2023-11-17",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f66",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 산업용 로봇의 운전 중 위험 방지 조치를 정한다. 같은 조는 한국산업표준이나 국제 안전기준에 맞는 경우 방책 같은 조치를 생략할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-562"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2023-07-01 시행본 기준이다. 물류센터 AMR 플릿에도 적용되는지는 oq-097 이다.",
      "as_of": "2023-07-01",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f67",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명을 면담하고 공동설계 워크숍을 연 결과, 이동장애인이 보도 로봇과 보도 공간을 두고 경쟁한다고 느끼고 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1214"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Co-design Accessible Public Robots(arXiv 2404.05050). E. 사물·사람·실시간 상태 페이지 P 절에서 재인용했다.",
      "as_of": "2024-04-07",
      "site_type": "실외",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f68",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 61. 물류창고: 아마존은 자사 풀필먼트 센터에서 직원이 로보틱스 테크 조끼를 켜고 로봇 구역에 들어가면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1080"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 감속 속도·거리 값은 공개되지 않았다(발행일 미확인, 확인일 기준). 49. 사람 근접 안전 페이지 5절에서 재인용했다.",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "제약",
      "vendor_claim": true,
      "source_unopened": true
    },
    {
      "id": "f69",
      "claim": "M. 안전의 50. 안전 표준·인증·사고 조사 ↔ Q. 현장 유형별 적용의 65. 가정·공동주택: Webb 외(2021)는 지원 주거 아파트에서 넘어진 거주자를 보조 로봇이 직원에게 알리지 못한 모의 사고를, 역할극 증언 면담과 윤리적 블랙박스 기록으로 조사하는 방법을 시험했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1121"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실제 사고가 아닌 모의 시나리오다. 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다.",
      "as_of": "2021-06-29",
      "site_type": "가정",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f70",
      "claim": "M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 66. 실외: 한국로봇산업진흥원은 실외이동로봇 운행안전인증 대상을 최고 속도 15km/h 이하·최대 질량 500kg 이하로 두고 주변 인식과 비상정지를 심사하며, 인증 뒤 2년 주기 정기점검을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "인증기관 페이지(확인일 2026-09-30) 기준이다. 49. 사람 근접 안전 페이지 5절에서 재인용했다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 작업·교통 조율, 플릿 어댑터, 긴급 작업의 우선 협상 구조를 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문이다. 범위 절의 안전 표준 아님 선언, 구역 유형(BLOCKED·SPEED_LIMIT), 연결 단절 동작, 운용 모드, 안전 상태(activeEmergencyStop·fieldViolation)를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 데모 세계와 비상 경보 시 주차 동작을 설명한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 이동로봇 통신·상호운용성 표준으로, 안전 요구는 범위에서 뺀다(D. 공간·지도 모델 페이지 기준).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-161",
      "org": "Abdul Hafez, O., Joerger, M., & Spenko, M.",
      "title": "Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach",
      "published": "2025-05",
      "url": "https://journals.sagepub.com/doi/10.1177/02783649241287797",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 무결성 위험 지표로 SLAM 위치추정의 안전성을 정량화한 IJRR 논문이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 승강기 상태 메시지로 층·문·운행 상태와 모드(사람·AGV·화재·오프라인·비상)를 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 시뮬레이션의 문·승강기 플러그인, crowdsim 군중 시뮬레이션을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-417",
      "org": "Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델이 제어하는 로봇에 실행 전 안전 게이트와 작업 안전 계약을 두는 방법을 다룬다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 무인 산업 차량과 그 시스템의 안전 요구·검증 표준이며 운용 구역 준비를 부속서 A 에 둔다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-472",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available",
      "published": "2023-10",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. R15.08-2(산업용 이동로봇 시스템·적용 안전) 발행 발표다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-562",
      "org": "국가법령정보센터(고용노동부)",
      "title": "산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)",
      "published": "2023-07-01",
      "url": "https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 로봇 운전 중 위험 방지 조치와 표준 부합 시 방책 생략 규정이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-563",
      "org": "Belzile, B. 외",
      "title": "From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment",
      "published": "2025-02",
      "url": "https://arxiv.org/abs/2502.20693",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동로봇 안전 표준을 검토하고 건설 현장 배치 전 위험성평가 틀을 제안한 프리프린트다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-565",
      "org": "Reliability Engineering & System Safety (저자 미확인)",
      "title": "Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN",
      "published": "2023",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 SPN 으로 분석했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-567",
      "org": "Open-RMF (open-rmf/rmf GitHub)",
      "title": "[Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf",
      "published": "2025-04-04",
      "url": "https://github.com/open-rmf/rmf/issues/658",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 화재경보 비상 신호가 플릿을 구분하지 않는 문제를 제기한 기능 요청이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-621",
      "org": "European Commission",
      "title": "AI Act | Shaping Europe's digital future",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. EU AI Act 의 위험 기반 분류와 고위험 AI 기준을 설명하는 정책 페이지다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동 로봇의 엘리베이터 탑승 안전 요구사항 KS B 7317 제정 보도다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실외이동로봇 운행안전인증의 대상·심사항목·정기점검 안내 페이지다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1076",
      "org": "Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv)",
      "title": "Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066",
      "published": "2026-02-19",
      "url": "https://arxiv.org/abs/2602.17822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 10218 2011판과 2025판을 비교하며 사이버보안·무단 접근 방지 요구가 늘었다고 분석한다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1079",
      "org": "Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv)",
      "title": "Principles and Guidelines for Evaluating Social Robot Navigation Algorithms",
      "published": "2023-06-29",
      "url": "https://arxiv.org/abs/2306.16740",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사회적 로봇 내비게이션 평가 원칙·지침이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1080",
      "org": "Amazon",
      "title": "Ever wonder how people and robots team up on your Amazon order?",
      "published": null,
      "url": "https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 풀필먼트 센터의 로보틱스 테크 조끼와 로봇 감속·정지를 설명하는 업체 글이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1081",
      "org": "Rondoni 외 (Scientific Reports)",
      "title": "Navigation benchmarking for autonomous mobile robots in hospital environments",
      "published": "2024-08-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모의 병원 환경에서 병원 물류 로봇의 주행 속도별 성능을 비교한 연구다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1083",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사람과 함께 쓰는 환경에서 사람을 고려한 다중 로봇 작업 배정을 다룬다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1084",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. R15.08-2 발행과 통합자·사용자 역할을 전한 기사다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1116",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ISO 10218-1/-2:2025 개정 항목(사이버보안 포함)과 EN ISO 판 참조의 EU 관보 등재(2026-09-07, 기계류 지침 조화)를 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "source_unopened": false
    },
    {
      "id": "ref-1117",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO/FDIS 13482 Robotics — Safety requirements for service robots",
      "published": null,
      "url": "https://iss.rs/en/project/show/iso:proj:83498",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 13482 개정 프로젝트의 FDIS 단계 정보다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1118",
      "org": "산업통상자원부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시",
      "published": "2023-11-17",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실외이동로봇 운행안전인증 절차·기준 고시다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1120",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사회적 로봇 사고 조사를 위한 윤리적 블랙박스 개방 표준 초안이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1121",
      "org": "Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI)",
      "title": "Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions",
      "published": "2021-06-29",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모의 사고를 역할극 증언 면담으로 조사하는 방법을 시험했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1122",
      "org": "Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121)",
      "title": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports",
      "published": "2024",
      "url": "https://eprints.whiterose.ac.uk/id/eprint/217393/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. OSHA 중대 부상 보고로 작업장 로봇 관련 부상을 분석했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1124",
      "org": "경향신문",
      "title": "‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망",
      "published": "2023-11-08",
      "url": "https://www.khan.co.kr/article/202311081103001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 농산물유통센터 로봇 점검 중 압착 사망 사고 보도다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1125",
      "org": "경남도민일보",
      "title": "오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다",
      "published": "2026-09-29",
      "url": "https://www.idomin.com/news/articleView.html?idxno=2015923",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 식품 공장 적재 로봇 점검 중 끼임 사망 사고와 잠금·표지 미실시 지적 보도다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1180",
      "org": "ILIAD 프로젝트 컨소시엄 (EU Horizon 2020)",
      "title": "Concluding ILIAD",
      "published": "2021-06",
      "url": "https://iliad-project.eu/concluding-iliad/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 창고 자율 지게차가 학습한 사람 흐름에 맞춰 경로를 계획한 EU 프로젝트 정리다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1181",
      "org": "조선비즈 (이정아, 다음 뉴스 게재)",
      "title": "로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘",
      "published": "2024-07-12",
      "url": "https://v.daum.net/v/bc4riunbUE",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원의 배달 로봇 경로 표시와 혼잡 대응 보도다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1214",
      "org": "Han, H. Z. 외 (Carnegie Mellon University) — CHI '24",
      "title": "Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations",
      "published": "2024-04-07",
      "url": "https://arxiv.org/abs/2404.05050",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동장애인과 로봇 실무자의 공공 로봇 접근성 공동설계 연구다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1241",
      "org": "Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020)",
      "title": "Simulation-based Testing for Early Safety-Validation of Robot Systems",
      "published": "2020-11-20",
      "url": "https://arxiv.org/abs/2011.10294",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 시뮬레이션에서 고위험 사람 행동을 생성해 로봇 셀 위험을 찾는 방법이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1242",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어짐을 보고했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1249",
      "org": "Wind River (Engblom, J. 인터뷰, Buchwieser, A.)",
      "title": "Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser",
      "published": "2014-11-20",
      "url": "https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. IEC 61508 맥락에서 시뮬레이션 활용을 다룬 업체 인터뷰다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv)",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-10-17",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 제어 로봇 탈옥 알고리즘 RoboPAIR 를 제시했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-700",
      "org": "Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv)",
      "title": "Safety Guardrails for LLM-Enabled Robots",
      "published": "2025-03-10",
      "url": "https://arxiv.org/abs/2503.07885",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 로봇용 안전 가드레일 RoboGuard 를 제안했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1341",
      "org": "법무법인 태평양(BKL) AI팀",
      "title": "AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인",
      "published": "2025-09-30",
      "url": "https://www.bkl.co.kr/law/insight/newsletter/6248",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 고영향 인공지능사업자 책무 고시·가이드라인 초안 해설이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1419",
      "org": "ANSI (American National Standards Institute) Blog",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": "2026-09-17",
      "url": "https://blog.ansi.org/?p=190868",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "R15.08-3 의 범위(유형 A·B·C, 지상 이동 로봇)와 사용자 의무(위험성평가·기록 유지·배치 후 변경 때의 적용·교육·안전 작업 절차)를 요약한 ANSI 블로그 글이다. 표준 본문은 유료라 열람하지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://blog.ansi.org/?p=190868",
      "source_unopened": false
    },
    {
      "id": "ref-1420",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications",
      "published": "2026-04-23",
      "url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "A3 판매 페이지다. 발행일 2026-04-23, 77쪽이며 사용자의 위험성평가와 변경 관리를 다룬다고 소개한다. 본문은 열람하지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "source_unopened": false
    },
    {
      "id": "ref-1421",
      "org": "Robotics 24/7",
      "title": "A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available",
      "published": "2026-10-04",
      "url": "https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "A3·ANSI 의 R15.08-3 공개 발표를 전한 기사다. 위험성평가·변경 관리·직원 교육·정기 검토와 점검을 사용자 의무로 든다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available",
      "source_unopened": false
    },
    {
      "id": "ref-1422",
      "org": "FORT Robotics (A3 Case Studies 게재)",
      "title": "Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs",
      "published": "2023-05-18",
      "url": "https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "창고 울타리 구역 AMR 에 무선 안전 비상정지(ISO 13849 범주 3·PLd 설계 주장)를 적용한 업체 사례 소개다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs",
      "source_unopened": false
    },
    {
      "id": "ref-1423",
      "org": "법제처 (네플라 위키 게재본)",
      "title": "[법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련)",
      "published": "2023-11-21",
      "url": "https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "법제처 법령해석 23-0872 의 질의·회답·이유 게재본이다. 로봇작업 특별교육 대상이 산업용 로봇 작업으로 한정되지 않는다고 회답했다. 법제처 원문 사이트에서는 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k",
      "source_unopened": false
    },
    {
      "id": "ref-1424",
      "org": "메트로신문 (한용수)",
      "title": "보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막",
      "published": "2023-11-16",
      "url": "https://www.metroseoul.co.kr/article/20231116500208",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "2023-11-17 개정 지능형로봇법 시행에 따른 실외이동로봇 보도 통행, 운행안전인증 대상, 운영자 보험 의무, 손해보장사업 실시기관 지정을 전한 기사다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.metroseoul.co.kr/article/20231116500208",
      "source_unopened": false
    },
    {
      "id": "ref-1425",
      "org": "DIN Media",
      "title": "DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024)",
      "published": "2024-10",
      "url": "https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ISO 13482 개정 초안 소개다. 로봇 유형별 구조로 바꾸고 탑승형 절을 뺐으며, 사이버보안·데이터 보호·승강기 협동 로봇(부속서 H) 절을 새로 넣었다. 초안 본문은 열람하지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303",
      "source_unopened": false
    },
    {
      "id": "ref-1426",
      "org": "Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS)",
      "title": "ROSMonitoring: A Runtime Verification Framework for ROS",
      "published": "2020-12-03",
      "url": "https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 응용의 형식 속성을 외부에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 초록만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/safety/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1·f2(2, oq-096), f3(1), f4·f5(3, 실외 보험) / B. 로봇 온톨로지: f6·f7(6, 실행 시점 조건에 운용 모드·안전 상태), f8(4) / C. 채팅 기반 구성·운영: f9(12), f10·f11·f12(13), 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f13·f14·f15(16, oq-229), f16(15, oq-170), f17(15, 연계 대상) / E. 사물·사람·실시간 상태: f18·f19(18), f20·f21(19) / F. 연동: f22·f23·f24(22, oq-254), f25(20), f26·f27(21) / G. 계획·최적화: f28(25), f29(28), f30·f31(27) / H. 실행·협업·예외 복구: f32·f33(29·31, oq-095), f34(32), f35·f36·f37(32·40) / I. 설계·시뮬레이션: f38(34·36), f39·f40(34), f41(36, 연계 대상) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현(f18·f19)과 구분 / J. 현장 운영·관제: f42·f44(37, oq-252), f43·f45·f46(38), f47·f48(40, oq-265) / K. 플랫폼 아키텍처·인프라: f49(벤더 주장)·f50(42, oq-095) / L. AI·학습 기술: f51·f52·f53(47, oq-106) / N. 보안·개인정보: f54·f57(51·52, oq-102), f56(52), f23·f57(53) / O. 검증·도입·수명주기: f45·f63(54), f58(55), f52·f59·f60(56, oq-275), f61·f62(57, oq-093·oq-282) / P. 거버넌스·법규·사회: f2·f64(58), f4·f55·f65·f66(59), f67(60) / Q. 현장 유형별 적용: f36·f49·f68(61 물류창고), f35(62 제조 공장), f20·f40(63 병원·의료), f39(64 상업 시설, 시뮬레이션 예제), f69(65 가정·공동주택), f4·f67·f70(66 실외), f58(67 기타 현장). 벤더 주장 f49·f68 은 [추정]과 '벤더 주장'을 병기하고, 연계 대상 f17·f41 과 로봇 자체 안전 기능·승강기 모드 제어·SLAM 은 '연계 대상'으로 짧게 쓴다. 상호운용 규격(VDA 5050·ISO 21423)은 안전 표준이 아니라는 점(f13·f26)을 유지한다. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설의 실제 현장 사례. 다음 실행 후보: 48. 안전·위험 관리(이전 분류 기준) 10절에 f32·f33·f47·f61·f54 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "변경 관리",
      "term_en": "Management of Change (MOC)",
      "definition": "설비·적용·운영 환경이나 설정을 바꿀 때 그 변경이 만드는 위험을 다시 평가하고 기록·승인하는 절차로, ANSI/A3 R15.08-3 이 산업용 이동로봇 사용자에게 요구하는 항목 가운데 하나다."
    },
    {
      "term_ko": "안전 상태 보고",
      "term_en": "Safety State (VDA 5050 safetyState)",
      "definition": "VDA 5050 상태 메시지에서 로봇이 활성 비상정지의 종류(MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 관제에 알리는 항목이다."
    },
    {
      "term_ko": "무선 안전 비상정지",
      "term_en": "Wireless Safety-rated Emergency Stop",
      "definition": "관제 통신과 별도의 안전 등급 무선 경로로 여러 이동로봇을 한꺼번에 멈추게 하는 비상정지 방식이다."
    }
  ],
  "open_questions_new": [
    "관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? | 관련 영역: 48. 안전·위험 관리, 42. 분산 시스템·통신·컴퓨팅 구조, 29. 명령·작업 실행의 신뢰성 | 근거: f49 | 종류: 일반",
    "ISO 13482 개정 초안(ISO/DIS 13482:2024)의 승강기 협동 로봇 요구(부속서 H)는 국내 KS B 7317 과 어떻게 대응하며, 이 요구가 최종판에 남았는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 22. 설비·건물 시스템 연동 | 근거: f23 | 종류: 일반",
    "진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? | 관련 영역: 48. 안전·위험 관리, 38. 모니터링·이상 탐지·원인 분석, 54. 시험·형식 검증·벤치마크 | 근거: f46 | 종류: 일반",
    "실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 66. 실외 | 근거: f5 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 48,
    "cross_checked_count": 2,
    "unverified": [
      "EU 기계류 규정 (EU) 2023/1230 원문(ref-555)을 EUR-Lex 에서 두 번 열었으나 빈 본문이 돌아와 실질적 변경 정의·부속서 III 1.1.9 를 확인하지 못함(finding 으로 내지 않음)",
      "Intertek 의 'EN ISO 13482:2026' 표기는 페이지가 403 으로 열리지 않아 쓰지 않음(ref-1117 의 FDIS 단계와 충돌 가능성 미확인)",
      "대한민국 정책브리핑(ref-991)은 ECONNRESET 으로 열지 못해 보험 의무 교차 확인 실패(f4 단일 출처)",
      "법무법인 지평 PDF 는 본문 추출 실패로 쓰지 않음",
      "f49·f68 벤더 주장은 독립 출처로 확인하지 못함",
      "f3 의 R15.08-3 발행일은 A3 판매 페이지 기준(2026-04-23)이며, 공개 발표(2026-10-04)와 날짜가 다름",
      "ISO 10218-1:2025 사이버보안 요구의 조항 번호는 확인하지 못함(oq-102)",
      "산업안전보건법 시행규칙 별표 5 로봇작업 특별교육의 교육 내용·시간은 확인하지 못함",
      "재사용 출처 40건은 이번 실행에서 다시 열지 않음"
    ],
    "scope_violations": [
      "f17: SLAM 위치추정 안전성은 원문 19장 '로봇 자체 지능·제어' 경계라 claim 을 '연계 대상: '으로 시작",
      "f41: 기능안전 인증과 시뮬레이션 인정은 인증 기관·제조사 몫이라 '연계 대상: '으로 시작",
      "f18·f19·f22·f24: 승강기 모드 제어와 탑승 안전은 시설·설비 제어 경계의 연계 대상이며, ROP 는 확인·요청 범위로만 서술",
      "f9~f12·f32·f49: 비상정지 회로·보호 필드·무선 안전 정지 같은 안전 기능은 로봇 제조사·통합자 몫의 연계 대상이며, ROP 는 상태 수신과 작업 보류·재개로만 서술",
      "f4·f5·f55·f59·f65·f66: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며, ROP 는 인증·운행 조건을 제약으로 반영하는 범위로만 연결"
    ],
    "budget_used": {
      "queries": 11,
      "sources": 8
    },
    "limits": "web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 48·49·50 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-07, 2026-10-09-08)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 40건, 이번에 다시 연 것은 ref-031(github_raw)·ref-1116(webfetch) 2건이고 나머지 38건은 fetched false·source_unopened true). 신규 출처는 8건(ref-1419~ref-1426, 예약 구간 안)이고 모두 원문 페이지를 열었다. 다만 ref-1419·ref-1420·ref-1425 는 유료 표준의 공식 소개 자료여서 표준 본문은 보지 못했다. 검색 11회/30, 신규 출처 8건/15. 교차 확인 2건(f47 R15.08-3 사용자 의무, f54 ISO 10218 사이버보안). 벤더 주장 2건(f49·f68). 한국 자료: 신규 ref-1423(법제처 해석)·ref-1424(기사), 재사용 ref-562·ref-945·ref-980·ref-1118·ref-1124·ref-1125·ref-1181·ref-1341. 현장 유형: 물류창고·제조 공장·병원·상업 시설(시뮬레이션 예제)·가정·실외·기타 각 1건 이상이며, 상업 시설의 실제 현장 사례는 찾지 못했다. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f18·f19)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f38·f39)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f51~f53)은 적용 대상인 48. 안전·위험 관리와 함께 제안했다. 열린 질문 가운데 oq-095(f32·f33·f50), oq-254(f23·f24, 초안 기준), oq-265(f47·f48, 이행 주체 미확인), oq-275(f59·f60, 지침 미확인), oq-102(f54, 조항 미확인), oq-229(f15)에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)를 따라 '5'로 매겼다 [가정]. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음."
  }
}
```

### runs/2026-10-09-09/verification.json

```json
{
  "run_id": "2026-10-09-09",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ANSI 블로그(2026-09-17)를 열어 확인했다. 1부는 제조사 IMR 안전 요구, 2부는 IMR 시스템·적용 통합, 3부는 사용자 책임을 다룬다(\"describes user responsibilities\"). ref-1084 는 원문 미열람이다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 1·2·3부의 책임 분담에서 끌어낸 판단이며 ROP 역할을 정한 자료는 없다(oq-096). ref-472·ref-1084 는 원문 미열람이다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IBF 기사에서 ISO 10218 개정(2025-02 발행)과 2026-09-07 관보 게재를 확인했다. A3 판매 페이지의 발행일 2026-04-23·77쪽도 확인했다. Robotics 24/7 는 2026-10-04 에 '이제 구할 수 있다'고 보도했으므로 두 날짜를 함께 쓴다. ISO 13482 FDIS 단계는 ref-1117(원문 미열람) 기준이다. '2025~2026년에 몰려 있다'는 종합 판단이므로 추정으로 분리한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 메트로신문(2023-11-16)을 열어 확인했다. 보도 운영자의 보험(또는 공제) 의무 가입, 한국로봇산업협회의 손해보장사업 실시기관 지정, 2023-11-17 시행이 기사에 있다. 단일 기사이며 조항 번호는 없다. 근거 발췌의 폭 기준('800mm 미만')은 기존 페이지의 '80cm 이하' 표기와 다르므로 본문에 쓰지 않는다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-980 은 원문 미열람이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 3.0.0 원문(github_raw) 6.6.6절 표 10을 확인했다. 관제가 제어하는 모드는 AUTOMATIC·SEMIAUTOMATIC 뿐이다. SEMIAUTOMATIC 에서는 주행 속도를 HMI 가 정한다. INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 제어하지 않는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 상태 메시지에 운용 모드와 safetyState 가 함께 있다는 점은 원문에서 확인했다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-980 은 원문 미열람이다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용): arXiv 2604.05427 의 제목이 기존 참고문헌과 일치한다. 이번 실행에서는 원문을 열지 않았다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 2026-10-09-08 검증): 92% 이상→3% 미만은 저자 보고값이며 독립 재현은 확인하지 못했다. 이번 실행에서는 원문을 열지 않았다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용): 공격 성공률은 저자 보고값이다. 이번 실행에서는 원문을 열지 않았다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 로봇 자체 안전 기능을 연계 대상으로 둔 서술은 범위 경계에 맞다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 3.0.0 2장(Scope)을 확인했다. 'does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.'"
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 6.4.1.1절 표 6을 확인했다. BLOCKED 에는 들어가지 않고, 구역 안의 로봇은 멈춘 뒤 BLOCKED_ZONE_VIOLATION 을 CRITICAL 로 보고한다. SPEED_LIMIT 는 진입 시점에 이미 최대 속도(m/s) 이하여야 한다. 6.4.4절의 BLOCKED 우선(LINE_GUIDED 보다 앞섬)도 확인했다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ISO 3691-4 는 원문 미열람이다(oq-229·oq-170)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 48. 안전·위험 관리 페이지에 게시된 사실 주장). 표준 본문은 원문 미열람이며 발행 2023-06 이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, D. 공간·지도 모델 페이지). SLAM 위치추정은 원문 19장 '로봇 자체 지능·제어' 경계에 속하므로 연계 대상으로 짧게 쓴다. 원문 미열람이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: LiftState.msg 원문 텍스트를 확인했다. 모드는 UNKNOWN·HUMAN·AGV·FIRE·OFFLINE·EMERGENCY 이고, 'We can only set human or agv mode'라고 적혀 있다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 승강기 모드 제어를 연계 대상으로 둔 서술은 범위 경계에 맞다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, E. 사물·사람·실시간 상태 페이지). 2024-07-12 기사 1건 기준이며 원문 미열람이다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 사람 검출·안전 정지를 연계 대상으로 두었다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 50. 안전 표준·인증·사고 조사 페이지). KDI 게재 보도(2021-11-11)이며 원문 미열람이다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: DIN Media 초안 소개(Ausgabedatum 2024-10)를 열어 확인했다. 로봇 유형별 구조, 탑승형 절 삭제, 사이버보안·데이터 보호·승강기 협동 로봇(참고 부속서 H) 추가가 적혀 있다. 초안 기준이다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 최종판 반영 여부는 oq-254 와 이어진다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 48. 안전·위험 관리 페이지). 이슈 작성일은 2025-04-04 이며 원문 미열람이다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, D. 공간·지도 모델 페이지, 확인일 2026-10-09). 발행 진행 중(60.00)이라 곧 바뀔 수 있는 정보다. 원문 미열람이다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). arXiv 2508.19731 은 원문 미열람이다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, G. 계획·최적화 페이지에 게시된 사실 주장). rmf_demos README 는 이번 실행에서 원문 미열람이다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: RMF Core Overview 원문 텍스트를 확인했다. 긴급 작업에서는 참여자가 충돌을 일부러 게시해 협상을 강제하고, 판정자가 높은 우선순위 참여자를 편들게 한다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 저자는 미확인이며 원문 미열람이다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 7.8절 safetyState 를 확인했다. activeEmergencyStop 값은 {MANUAL, REMOTE, NONE} 이고 AUTOACK 은 없다. fieldViolation 은 레이저 스캐너·범퍼 같은 보호 필드 침범을 나타내는 불리언이다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 재개 판정 규칙을 정한 표준은 없다(oq-095)."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 4.1절 원문 텍스트를 확인했다. 'fulfills the order up to the last released node'."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 50. 안전 표준·인증·사고 조사 페이지). 2026-09-29 보도 기준이며 원인은 미확정이다. 원문 미열람이다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 2023-11-08 보도 기준이며 원문 미열람이다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 2026-10-09-07). 개념 증명 단계이며 원문 미열람이다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Simulation 장 원문 텍스트에서 crowdsim(menge, rmf_traffic_editor 에서 켬)과 airport_world 예제를 확인했다. 다만 실제 현장이 아니라 공항 터미널 시뮬레이션 예제이므로 64. 상업 시설의 현장 사례로 세지 않는다."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 49. 사람 근접 안전 페이지). 모의 병원 환경의 시뮬레이션 평가이며 원문 미열람이다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 업체 블로그의 표준 인용이며 IEC 61508-7 원문은 열람하지 않았다. 연계 대상으로 짧게 쓴다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 원문 미열람이다."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 원문 미열람이다."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(oq-252)."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Manchester 연구 포털 초록을 확인했다(LNCS, 2020-12-03, pp.387-399). 여러 ROS 배포판 이식성, 명세 형식 독립, Mars Curiosity 로버 시뮬레이션 적용이 초록에 있다."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 이종 플릿 적용 사례는 없다."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: 두 출처를 열어 대조했다. ANSI 블로그(2026-09-17)는 위험성평가, 위험 감소 조치 유지, 기록, 교육·안전 작업 절차를 든다. Robotics 24/7(2026-10-04)은 위험성평가, 공식 변경 절차, 직원 교육, 정기 검토·점검을 든다. 위험성평가·교육은 두 출처가 일치한다. 표준 본문은 유료라 미열람이다."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(oq-265)."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: FORT Robotics 사례(A3 게재, 2023-05-18)를 열어 확인했다. 문에 단 주 VSC, 로봇별 VSC, 주파수 도약, ISO 13849 범주 3·PLd 설계, 소규모 시범 운영, 플릿 관리·WMS 언급 없음을 확인했다. 벤더 주장 표시와 추정 태그가 적정하다."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(oq-095). 벤더 사례에 기댄 부분이 있다."
    },
    {
      "finding_id": "f51",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 2026-10-09-08). 정책 페이지는 이번 실행에서 원문 미열람이다."
    },
    {
      "finding_id": "f52",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 2026-10-09-08에서 원문 열람). 2025-09 초안 기준의 법무법인 해설이다."
    },
    {
      "finding_id": "f53",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(oq-106)."
    },
    {
      "finding_id": "f54",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: IBF 기사를 열어 개정 항목에 사이버보안이 들어 있음을 확인했다. Hartmann 외(ref-1076)는 이전 실행에서 열람했고 이번에는 열지 않았다. 조항 번호는 미확인이다(oq-102)."
    },
    {
      "finding_id": "f55",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: IBF 기사에서 2026-09-07 관보 게재, 시행결정 (EU) 2026/2015, 기계류 지침 2006/42/EC 조화를 확인했다. 검색 결과(EUR-Lex ELI dec_impl/2026/2015, certifico)에서도 2026-09-04 채택, 2026-09-07 관보 게재, EN ISO 10218-1/-2:2025 포함이 일치했다. EUR-Lex 는 원문 미열람이며 페이지 각주는 ref-1116 만 쓴다."
    },
    {
      "finding_id": "f56",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 2026-10-09-07). 원문 미열람이다."
    },
    {
      "finding_id": "f57",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지."
    },
    {
      "finding_id": "f58",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 50. 안전 표준·인증·사고 조사 페이지). 프리프린트이며 원문 미열람이다."
    },
    {
      "finding_id": "f59",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검색 결과에서 해석 번호 23-0872, 해석일 2023-11-21, 회답 취지가 네플라 게재본과 일치했다. 법제처 공식 원문은 열지 못했고 제3자 게재본 기준이다."
    },
    {
      "finding_id": "f60",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(oq-275)."
    },
    {
      "finding_id": "f61",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ANSI 블로그를 확인했다. 공급자 배치 뒤 사용자가 IMR·적용·운영 환경을 바꾸는 경우에도 의무가 적용된다. A3 판매 페이지의 '변경 관리' 설명과도 맞는다."
    },
    {
      "finding_id": "f62",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(oq-093·oq-282)."
    },
    {
      "finding_id": "f63",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 원문 미열람이다."
    },
    {
      "finding_id": "f64",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 사실 내용은 R15.08-2 발행뿐이다. 58. 다사업자 책임·계약·데이터와의 연결은 f2(추정, oq-096)를 통해서만 성립한다. 원문 미열람이다."
    },
    {
      "finding_id": "f65",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 50. 안전 표준·인증·사고 조사 페이지). 원문 미열람이다."
    },
    {
      "finding_id": "f66",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 2023-07-01 시행본). 원문 미열람이다."
    },
    {
      "finding_id": "f67",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, E. 사물·사람·실시간 상태·D. 공간·지도 모델 페이지). 원문 미열람이다."
    },
    {
      "finding_id": "f68",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 벤더 주장 표시와 추정 태그가 적정하다. 발행일 미확인이며 원문 미열람이다."
    },
    {
      "finding_id": "f69",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용). 모의 사고 시나리오이며 원문 미열람이다."
    },
    {
      "finding_id": "f70",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(재인용, 49. 사람 근접 안전 페이지, 확인일 2026-09-30). 원문 미열람이다."
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
      "f13·f14·f16·f17은 D. 공간·지도 모델 페이지의 M 연결과 같은 주장이다. 같은 각주(ref-031·ref-470·ref-161)를 다시 쓰고, 상대 페이지에도 같은 연결이 있음을 밝힌다",
      "f18·f19·f20·f21은 E. 사물·사람·실시간 상태 페이지의 M 연결과 같은 주장이다(ref-286·ref-1181·ref-1180)",
      "f29는 G. 계획·최적화 페이지의 옛 G 절과 같은 주장이다(ref-104)",
      "f9·f10·f11·f51·f52는 2026-10-09-08 브리프(L. AI·학습 기술)의 f39·f63·f64·f71·f66과 같은 주장이다",
      "f38·f39·f41·f56은 2026-10-09-07 브리프(I. 설계·시뮬레이션)의 f62·f18·f64·f65와 같은 주장이다",
      "새 열린 질문 2(ISO 13482 부속서 H)의 '최종판에 남았는가' 부분은 oq-254와 겹친다"
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
    "patches 의 section 은 대분류 페이지의 기존 H2 문자열 그대로 '다른 대분류와의 연결'로 쓴다. 브리프의 '5. 다른 대분류와의 연결'처럼 번호를 붙이지 않는다. 대분류 페이지 정본에는 번호가 없고, 번호가 붙으면 퍼블리셔가 반려한다. 다른 절과 auto 마커는 건드리지 않는다.",
    "f3: R15.08-3 발행일은 'A3 판매 페이지 기준 2026-04-23, 공개 발표 보도는 2026-10-04(Robotics 24/7)'로 두 날짜를 함께 쓴다. '표준 개정이 2025~2026년에 몰려 있다'는 종합 판단은 [추정] 문장으로 분리한다. ISO 13482 FDIS 단계에는 기준일 2026-09-15 와 ref-1117 원문 미열람을 밝힌다.",
    "f4: 주장은 보험(또는 공제) 의무 가입과 손해보장사업 실시기관 지정만 [사실]로 쓰고, 근거가 기사 1건(2023-11-16)이라는 점과 기준일을 밝힌다. 근거 발췌의 폭 기준('폭 800mm 미만')은 본문에 쓰지 않는다. 기존 D. 공간·지도 모델·50. 안전 표준·인증·사고 조사 페이지의 '80cm 이하' 표기와 달라 충돌을 새로 만들기 때문이다. 조항 번호도 적지 않는다.",
    "f39: Open-RMF 공항 터미널 crowdsim 은 현장 사례가 아니라 '시뮬레이션 예제'로만 쓴다. Q. 현장 유형별 적용의 64. 상업 시설 줄에 현장 적용 사례로 넣지 않고, 'site_matrix_updates' 에도 넣지 않는다. 64. 상업 시설의 실제 사람 근접 안전 사례는 '아직 다루지 않은 연결'에 둔다.",
    "f40·f69: 각각 '모의 병원 환경의 시뮬레이션 평가', '실제 사고가 아닌 모의 사고 시나리오'임을 문장 안에 밝힌다. f35: '원인 미확정, 2026-09-29 보도 기준'을 병기한다. f20: 기사 1건 기준임을 밝힌다.",
    "f10·f11: 수치(92% 이상→3% 미만, 공격 성공률 100%)마다 '저자 보고값, 독립 재현 미확인'을 병기한다.",
    "f47·f61: 'ANSI 블로그(2026-09-17)·Robotics 24/7(2026-10-04)·A3 판매 페이지 요약 기준이며 표준 본문은 열람하지 않았다'를 밝힌다. 변경 관리는 Robotics 24/7·A3 판매 페이지 근거, 안전 작업 절차는 ANSI 블로그 근거임이 각주로 드러나게 한다.",
    "f49·f68: [추정]과 '벤더 주장'을 병기하고, f49 는 '소규모 시범 운영 단계, 플릿 관리·WMS 연동 언급 없음'을 함께 쓴다. 용어집 후보 '무선 안전 비상정지'의 정의에는 ref-1422 업체 사례에 기댄 용어임을 밝히고 성능 수준(PLd) 같은 벤더 주장을 넣지 않는다.",
    "f17·f41: '연계 대상'으로 한 문장 안에 짧게 쓴다. SLAM 위치추정 안전성과 시뮬레이션 기반 안전 인증 인정을 ROP 직접 범위처럼 쓰지 않는다. f9~f12·f32·f49·f50 에서도 비상정지 회로·보호 필드·무선 안전 정지는 로봇 제조사·통합자 몫의 연계 대상으로 두고, ROP 몫은 상태 수신과 작업 보류·재배정·재개 지시로 한정한다.",
    "f55: 'EN ISO 10218-1:2025·-2:2025 의 참조가 시행결정 (EU) 2026/2015 로 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다'까지만 쓴다. 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 미확인으로 남긴다.",
    "f64: 58. 다사업자 책임·계약·데이터 연결에서 f64 는 R15.08-2 발행 사실로만 쓴다. 통합자·ROP 사업자 역할 분담은 f2 의 [추정]과 oq-096 으로만 연결한다.",
    "18. 실시간 세계 상태·데이터 일관성(f18·f19, 현재 상태 표현)과 34. 시뮬레이션·예측용 디지털 트윈(f38·f39·f40, 가정한 미래 실험)의 연결은 이 구분을 문장으로 밝혀 따로 쓴다.",
    "각주 정의: 이번 실행에서 원문을 연 ref-004·ref-031·ref-286·ref-406(입력 원문 텍스트), ref-1116, ref-1419~ref-1426 은 접근일 2026-10-09 로 쓰고 '(원문 미열람)'을 붙이지 않는다. 나머지 재사용 출처 35건(ref-104, ref-159, ref-161, ref-417, ref-470, ref-472, ref-562, ref-563, ref-565, ref-567, ref-621, ref-945, ref-980, ref-1076, ref-1079, ref-1080, ref-1081, ref-1083, ref-1084, ref-1117, ref-1118, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-1180, ref-1181, ref-1214, ref-1241, ref-1242, ref-1249, ref-857, ref-700, ref-1341)은 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 해당 항목에 source_unopened: true 를 넣는다. ref-1423 은 기관 표기에 '(네플라 위키 게재본, 법제처 원문 미열람)'이 드러나게 한다.",
    "open_questions_new 두 번째(ISO 13482 부속서 H)는 '최종판에 남았는가' 부분이 oq-254 와 겹친다. 질문을 'ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가'로 줄이고, 최종판 반영 여부는 본문에서 oq-254 로 연결한다.",
    "D·E·G 대분류 페이지에 이미 있는 연결(f13·f14·f16·f17·f18·f19·f20·f21·f29)은 같은 각주 id 를 다시 쓰고 '같은 연결은 … 페이지의 연결 절에도 있다'로 밝힌다.",
    "브리프 rationale 이 적은 미근거 연결(23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설 실제 현장 사례)은 내용을 채우지 않고 '아직 다루지 않은 연결'에 번호와 이름으로 나열한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 70건, 미확인 0건, 교차 확인 3건(f47 R15.08-3 사용자 의무, f54 ISO 10218:2025 사이버보안, f55 EN ISO 10218 관보 게재). 강등: 없음. 수정 지시는 문구·병기·범위 조정이며, f39(공항 시뮬레이션 예제)를 64. 상업 시설 현장 사례로 세지 않도록 했다. 원문 미열람 출처: ref-104, ref-159, ref-161, ref-417, ref-470, ref-472, ref-562, ref-563, ref-565, ref-567, ref-621, ref-945, ref-980, ref-1076, ref-1079, ref-1080, ref-1081, ref-1083, ref-1084, ref-1117, ref-1118, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-1180, ref-1181, ref-1214, ref-1241, ref-1242, ref-1249, ref-857, ref-700, ref-1341. 이 가운데 다수는 이전 실행에서 검증된 주장의 재인용이다. 검증자가 직접 연 출처는 ref-031(VDA 5050 3.0.0 원문 6.4.1·6.6.6·7.8절), ref-1116, ref-1419, ref-1420, ref-1421, ref-1422, ref-1424, ref-1425, ref-1426 이다. ref-004·ref-286·ref-406 은 입력 원문 텍스트로 대조했다. ref-1423 은 검색 결과 일치로만 확인했다(법제처 원문 미열람). 검증 검색 2회. 주의: ANSI/A3 R15.08-3·ISO 10218·ISO 13482·ISO 3691-4 의 표준 본문은 열람하지 않았고, 발행 기관 소개·블로그·보도 기준이다. 연결 주장의 3분의 1가량(23건)이 추정이며, 무선 안전 비상정지(f49)와 아마존 조끼(f68)는 벤더 주장이다. 브리프 출처 표시가 서로 맞지 않는 곳이 있다. ref-004·ref-286·ref-406 은 fetched true 인데 summary 가 '원문 미열람.'으로 시작하고, self_check 는 다시 연 출처를 2건으로 적었다. 입력 원문 텍스트가 있으므로 이 셋은 연 것으로 보았다. 사고 사례(f35·f36)는 기사 기준이고 원인이 확정되지 않았다. 정정 요청은 없다.",
  "retry_reason": null
}
```

### runs/2026-10-09-09/pages.json

```json
{
  "run_id": "2026-10-09-09",
  "outline": [
    {
      "path": "docs/categories/safety/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 9500,
      "summary": "M. 안전의 세 세부영역이 다른 16개 대분류와 만나는 지점을 대분류별로 정리했다. 예를 들어 VDA 5050 3.0.0 은 스스로 안전 표준으로 적용해서는 안 된다고 범위 절에 적으므로 지도의 구역 규칙과 안전 기능을 따로 다룬다. [사실][^ref-031]",
      "planned_findings": [
        "A. 기획·사업: f1·f2·f3·f4·f5",
        "B. 로봇 온톨로지: f6·f7·f8",
        "C. 채팅 기반 구성·운영: f9·f10·f11·f12",
        "D. 공간·지도 모델: f13·f14·f15·f16·f17",
        "E. 사물·사람·실시간 상태: f18·f19·f20·f21",
        "F. 연동: f22·f23·f24·f25·f26·f27",
        "G. 계획·최적화: f28·f29·f30·f31",
        "H. 실행·협업·예외 복구: f32·f33·f34·f35·f36·f37",
        "I. 설계·시뮬레이션: f38·f39·f40·f41",
        "J. 현장 운영·관제: f42·f43·f44·f45·f46·f47·f48",
        "K. 플랫폼 아키텍처·인프라: f49·f50",
        "L. AI·학습 기술: f51·f52·f53",
        "N. 보안·개인정보: f54·f56·f57(f23·f11 참조)",
        "O. 검증·도입·수명주기: f58·f59·f60·f61·f62·f63",
        "P. 거버넌스·법규·사회: f55·f64·f65·f66·f67",
        "Q. 현장 유형별 적용: f68·f69·f70(f20·f35·f36·f40·f49·f58 참조), 64. 상업 시설은 미다룸"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/safety/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 첫 작성: 16개 대분류와의 연결(주장 70건 근거), Q. 현장 유형별 적용 현장별 정리, 아직 다루지 않은 연결 7건, 각주 정의 48건",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-004",
              "ref-031",
              "ref-104",
              "ref-159",
              "ref-161",
              "ref-286",
              "ref-406",
              "ref-417",
              "ref-470",
              "ref-472",
              "ref-562",
              "ref-563",
              "ref-565",
              "ref-567",
              "ref-621",
              "ref-945",
              "ref-980",
              "ref-1076",
              "ref-1079",
              "ref-1080",
              "ref-1081",
              "ref-1083",
              "ref-1084",
              "ref-1116",
              "ref-1117",
              "ref-1118",
              "ref-1120",
              "ref-1121",
              "ref-1122",
              "ref-1124",
              "ref-1125",
              "ref-1180",
              "ref-1181",
              "ref-1214",
              "ref-1241",
              "ref-1242",
              "ref-1249",
              "ref-857",
              "ref-700",
              "ref-1341",
              "ref-1419",
              "ref-1420",
              "ref-1421",
              "ref-1422",
              "ref-1423",
              "ref-1424",
              "ref-1425",
              "ref-1426"
            ]
          },
          "content": "(절 본문 생략 — runs/2026-10-09-09/pages/categories/safety/index.md 의 해당 절을 본다)"
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | M. 안전 | 다른 대분류와의 연결 절 첫 작성(16개 대분류와의 연결, 현장 유형별 근거, 아직 다루지 않은 연결 7건) | run 2026-10-09-09",
  "index_updates": {
    "home_recent": "2026-10-09 — M. 안전: '다른 대분류와의 연결' 절을 처음 채웠다(16개 대분류와의 연결, VDA 5050 안전 상태·운용 모드, R15.08-3 사용자 의무, 실외 보험·인증, 아직 다루지 않은 연결 7건)",
    "category_recent": "2026-10-09 — M. 안전: '다른 대분류와의 연결' 절 첫 작성(48. 안전·위험 관리·49. 사람 근접 안전·50. 안전 표준·인증·사고 조사와 A~Q 대분류의 연결, 새 열린 질문 4건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "management-of-change",
      "term_ko": "변경 관리",
      "term_en": "Management of Change (MOC)",
      "definition": "설비·적용·운영 환경이나 설정을 바꿀 때 그 변경이 만드는 위험을 다시 평가하고 기록·승인하는 절차로, ANSI/A3 R15.08-3 이 산업용 이동로봇 사용자에게 요구하는 항목 가운데 하나다.",
      "description": "R15.08-3 의 변경 관리 요구는 Robotics 24/7 보도와 A3 판매 페이지 요약 기준이며 표준 본문은 열람하지 않았다. 공급자가 배치한 뒤 사용자가 로봇·적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다.",
      "related_areas": [
        48,
        57,
        40
      ],
      "sources": [
        "ref-1421",
        "ref-1420",
        "ref-1419"
      ]
    },
    {
      "action": "new",
      "slug": "safety-state-report",
      "term_ko": "안전 상태 보고",
      "term_en": "Safety State (VDA 5050 safetyState)",
      "definition": "VDA 5050 상태 메시지에서 로봇이 활성 비상정지의 종류(MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 관제에 알리는 항목이다.",
      "description": "VDA 5050 3.0.0 기준이며 MANUAL 은 로봇에서 수동 확인, REMOTE 는 시설 비상정지를 원격 확인하는 경우다. VDA 5050 자체는 안전 표준이 아니다.",
      "related_areas": [
        48,
        29
      ],
      "sources": [
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "wireless-safety-rated-emergency-stop",
      "term_ko": "무선 안전 비상정지",
      "term_en": "Wireless Safety-rated Emergency Stop",
      "definition": "관제 통신과 별도의 안전 등급 무선 경로로 여러 이동로봇을 한꺼번에 멈추게 하는 비상정지 방식이며, 이 위키에서는 FORT Robotics 업체 사례 소개(ref-1422)에 기댄 용어다.",
      "description": "근거 사례는 창고 울타리 구역의 소규모 시범 운영이고 플릿 관리 시스템·WMS 연동은 언급되지 않았다. 성능 주장은 독립 출처로 확인되지 않았다.",
      "related_areas": [
        48,
        42
      ],
      "sources": [
        "ref-1422"
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
      "accessed": "2026-10-09",
      "summary": "작업·교통 조율, 플릿 어댑터, 긴급 작업의 우선 협상 구조를 설명한다(입력 원문 텍스트로 대조).",
      "cited_by": [
        "docs/categories/safety/index.md"
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
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문이다. 범위 절의 안전 표준 아님 선언, 구역 유형(BLOCKED·SPEED_LIMIT), 연결 단절 동작, 운용 모드, 안전 상태(activeEmergencyStop·fieldViolation)를 확인했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 데모 세계와 비상 경보 시 주차 동작을 설명한다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 이동로봇 통신·상호운용성 표준으로, 안전 요구는 범위에서 뺀다(D. 공간·지도 모델 페이지 기준).",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-161",
      "org": "Abdul Hafez, O., Joerger, M., & Spenko, M.",
      "title": "Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach",
      "published": "2025-05",
      "url": "https://journals.sagepub.com/doi/10.1177/02783649241287797",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 무결성 위험 지표로 SLAM 위치추정의 안전성을 정량화한 IJRR 논문이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "승강기 상태 메시지로 층·문·운행 상태와 모드(알 수 없음·사람·AGV·화재·오프라인·비상)를 담으며 사람·AGV 모드만 설정할 수 있다(입력 원문 텍스트로 대조).",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 시뮬레이션의 문·승강기 플러그인과 crowdsim 군중 시뮬레이션(공항 터미널 예제)을 설명한다(입력 원문 텍스트로 대조).",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-417",
      "org": "Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델이 제어하는 로봇에 실행 전 안전 게이트와 작업 안전 계약을 두는 방법을 다룬다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 무인 산업 차량과 그 시스템의 안전 요구·검증 표준이며 운용 구역 준비를 부속서 A 에 둔다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-472",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available",
      "published": "2023-10",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. R15.08-2(산업용 이동로봇 시스템·적용 안전) 발행 발표다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-562",
      "org": "국가법령정보센터(고용노동부)",
      "title": "산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)",
      "published": "2023-07-01",
      "url": "https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 로봇 운전 중 위험 방지 조치와 표준 부합 시 방책 생략 규정이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-563",
      "org": "Belzile, B. 외",
      "title": "From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment",
      "published": "2025-02",
      "url": "https://arxiv.org/abs/2502.20693",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동로봇 안전 표준을 검토하고 건설 현장 배치 전 위험성평가 틀을 제안한 프리프린트다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-565",
      "org": "Reliability Engineering & System Safety (저자 미확인)",
      "title": "Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN",
      "published": "2023",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 SPN 으로 분석했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-567",
      "org": "Open-RMF (open-rmf/rmf GitHub)",
      "title": "[Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf",
      "published": "2025-04-04",
      "url": "https://github.com/open-rmf/rmf/issues/658",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 화재경보 비상 신호가 플릿을 구분하지 않는 문제를 제기한 기능 요청이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-621",
      "org": "European Commission",
      "title": "AI Act | Shaping Europe's digital future",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. EU AI Act 의 위험 기반 분류와 고위험 AI 기준을 설명하는 정책 페이지다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동 로봇의 엘리베이터 탑승 안전 요구사항 KS B 7317 제정 보도다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실외이동로봇 운행안전인증의 대상·심사항목·정기점검 안내 페이지다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1076",
      "org": "Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv)",
      "title": "Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066",
      "published": "2026-02-19",
      "url": "https://arxiv.org/abs/2602.17822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 10218 2011판과 2025판을 비교하며 사이버보안·무단 접근 방지 요구가 늘었다고 분석한다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1079",
      "org": "Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv)",
      "title": "Principles and Guidelines for Evaluating Social Robot Navigation Algorithms",
      "published": "2023-06-29",
      "url": "https://arxiv.org/abs/2306.16740",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사회적 로봇 내비게이션 평가 원칙·지침이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1080",
      "org": "Amazon",
      "title": "Ever wonder how people and robots team up on your Amazon order?",
      "published": null,
      "url": "https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 풀필먼트 센터의 로보틱스 테크 조끼와 로봇 감속·정지를 설명하는 업체 글이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1081",
      "org": "Rondoni 외 (Scientific Reports)",
      "title": "Navigation benchmarking for autonomous mobile robots in hospital environments",
      "published": "2024-08-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모의 병원 환경에서 병원 물류 로봇의 주행 속도별 성능을 비교한 연구다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1083",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사람과 함께 쓰는 환경에서 사람을 고려한 다중 로봇 작업 배정을 다룬다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1084",
      "org": "The Robot Report",
      "title": "New AMR safety standard available with release of ANSI/A3 R15.08-2",
      "published": "2023-10-26",
      "url": "https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. R15.08-2 발행과 통합자·사용자 역할을 전한 기사다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1116",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ISO 10218-1/-2:2025 개정 항목(사이버보안 포함)과 EN ISO 판 참조의 EU 관보 등재(2026-09-07, 기계류 지침 조화)를 전한다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1117",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO/FDIS 13482 Robotics — Safety requirements for service robots",
      "published": null,
      "url": "https://iss.rs/en/project/show/iso:proj:83498",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 13482 개정 프로젝트의 FDIS 단계 정보다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1118",
      "org": "산업통상자원부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시",
      "published": "2023-11-17",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실외이동로봇 운행안전인증 절차·기준 고시다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1120",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사회적 로봇 사고 조사를 위한 윤리적 블랙박스 개방 표준 초안이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1121",
      "org": "Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI)",
      "title": "Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions",
      "published": "2021-06-29",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모의 사고를 역할극 증언 면담으로 조사하는 방법을 시험했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1122",
      "org": "Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121)",
      "title": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports",
      "published": "2024",
      "url": "https://eprints.whiterose.ac.uk/id/eprint/217393/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. OSHA 중대 부상 보고로 작업장 로봇 관련 부상을 분석했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1124",
      "org": "경향신문",
      "title": "‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망",
      "published": "2023-11-08",
      "url": "https://www.khan.co.kr/article/202311081103001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 농산물유통센터 로봇 점검 중 압착 사망 사고 보도다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1125",
      "org": "경남도민일보",
      "title": "오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다",
      "published": "2026-09-29",
      "url": "https://www.idomin.com/news/articleView.html?idxno=2015923",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 식품 공장 적재 로봇 점검 중 끼임 사망 사고와 잠금·표지 미실시 지적 보도다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1180",
      "org": "ILIAD 프로젝트 컨소시엄 (EU Horizon 2020)",
      "title": "Concluding ILIAD",
      "published": "2021-06",
      "url": "https://iliad-project.eu/concluding-iliad/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 창고 자율 지게차가 학습한 사람 흐름에 맞춰 경로를 계획한 EU 프로젝트 정리다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1181",
      "org": "조선비즈 (이정아, 다음 뉴스 게재)",
      "title": "로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘",
      "published": "2024-07-12",
      "url": "https://v.daum.net/v/bc4riunbUE",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원의 배달 로봇 경로 표시와 혼잡 대응 보도다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1214",
      "org": "Han, H. Z. 외 (Carnegie Mellon University) — CHI '24",
      "title": "Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations",
      "published": "2024-04-07",
      "url": "https://arxiv.org/abs/2404.05050",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동장애인과 로봇 실무자의 공공 로봇 접근성 공동설계 연구다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1241",
      "org": "Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020)",
      "title": "Simulation-based Testing for Early Safety-Validation of Robot Systems",
      "published": "2020-11-20",
      "url": "https://arxiv.org/abs/2011.10294",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 시뮬레이션에서 고위험 사람 행동을 생성해 로봇 셀 위험을 찾는 방법이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1242",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어짐을 보고했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1249",
      "org": "Wind River (Engblom, J. 인터뷰, Buchwieser, A.)",
      "title": "Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser",
      "published": "2014-11-20",
      "url": "https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. IEC 61508 맥락에서 시뮬레이션 활용을 다룬 업체 인터뷰다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv)",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-10-17",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 제어 로봇 탈옥 알고리즘 RoboPAIR 를 제시했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-700",
      "org": "Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv)",
      "title": "Safety Guardrails for LLM-Enabled Robots",
      "published": "2025-03-10",
      "url": "https://arxiv.org/abs/2503.07885",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 로봇용 안전 가드레일 RoboGuard 를 제안했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1341",
      "org": "법무법인 태평양(BKL) AI팀",
      "title": "AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인",
      "published": "2025-09-30",
      "url": "https://www.bkl.co.kr/law/insight/newsletter/6248",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 고영향 인공지능사업자 책무 고시·가이드라인 초안 해설이다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1419",
      "org": "ANSI (American National Standards Institute) Blog",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": "2026-09-17",
      "url": "https://blog.ansi.org/?p=190868",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "R15.08-3 의 범위(유형 A·B·C, 지상 이동 로봇)와 사용자 의무(위험성평가·기록 유지·배치 후 변경 때의 적용·교육·안전 작업 절차)를 요약한 ANSI 블로그 글이다. 표준 본문은 유료라 열람하지 않았다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1420",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications",
      "published": "2026-04-23",
      "url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "A3 판매 페이지다. 발행일 2026-04-23, 77쪽이며 사용자의 위험성평가와 변경 관리를 다룬다고 소개한다. 본문은 열람하지 않았다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1421",
      "org": "Robotics 24/7",
      "title": "A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available",
      "published": "2026-10-04",
      "url": "https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "A3·ANSI 의 R15.08-3 공개 발표를 전한 기사다. 위험성평가·변경 관리·직원 교육·정기 검토와 점검을 사용자 의무로 든다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1422",
      "org": "FORT Robotics (A3 Case Studies 게재)",
      "title": "Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs",
      "published": "2023-05-18",
      "url": "https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "창고 울타리 구역 AMR 에 무선 안전 비상정지(ISO 13849 범주 3·PLd 설계 주장)를 적용한 업체 사례 소개다. 소규모 시범 운영 단계이며 플릿 관리·WMS 연동은 언급하지 않는다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1423",
      "org": "법제처 (네플라 위키 게재본, 법제처 원문 미열람)",
      "title": "[법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련)",
      "published": "2023-11-21",
      "url": "https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "법제처 법령해석 23-0872 의 질의·회답·이유 게재본이다. 로봇작업 특별교육 대상이 산업용 로봇 작업으로 한정되지 않는다고 회답했다. 법제처 원문 사이트에서는 열지 않았다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1424",
      "org": "메트로신문 (한용수)",
      "title": "보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막",
      "published": "2023-11-16",
      "url": "https://www.metroseoul.co.kr/article/20231116500208",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "2023-11-17 개정 지능형로봇법 시행에 따른 실외이동로봇 보도 통행, 운행안전인증 대상, 운영자 보험 의무, 손해보장사업 실시기관 지정을 전한 기사다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1425",
      "org": "DIN Media",
      "title": "DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024)",
      "published": "2024-10",
      "url": "https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ISO 13482 개정 초안 소개다. 로봇 유형별 구조로 바꾸고 탑승형 절을 뺐으며, 사이버보안·데이터 보호·승강기 협동 로봇(부속서 H) 절을 새로 넣었다. 초안 본문은 열람하지 않았다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1426",
      "org": "Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS)",
      "title": "ROSMonitoring: A Runtime Verification Framework for ROS",
      "published": "2020-12-03",
      "url": "https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 응용의 형식 속성을 외부에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 초록만 확인했다.",
      "cited_by": [
        "docs/categories/safety/index.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가?",
      "areas": [
        48,
        42,
        29
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가?",
      "areas": [
        50,
        22
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가?",
      "areas": [
        48,
        38,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가?",
      "areas": [
        59,
        58,
        66
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "가정",
      "item": "예외·성과",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    },
    {
      "site_type": "기타",
      "item": "제약",
      "link": "docs/categories/safety/index.md#다른-대분류와의-연결",
      "title": "M. 안전"
    }
  ],
  "additional_research_requests": [
    "다른 대분류와의 연결 절의 '아직 다루지 않은 연결': 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화와 M. 안전(48·49·50)을 잇는 검증 가능한 근거가 필요하다(예: 안전 정지가 처리량 지표에 주는 영향, 외부 API 의 정지·재개 권한, 안전 기록의 보존·관측성).",
    "Q. 현장 유형별 적용의 64. 상업 시설에서 실제 현장의 사람 근접 안전 사례(속도·거리 규칙, 혼잡 대응)가 필요하다. 이번 근거(Open-RMF 공항 터미널 crowdsim)는 시뮬레이션 예제라 현장 사례로 쓰지 않았다.",
    "ISO 13482 개정 최종판에 승강기 협동 로봇(부속서 H)·사이버보안·데이터 보호 절이 남았는지 확인이 필요하다(oq-254).",
    "EN ISO 10218-1/-2:2025 가 기계류 규정 (EU) 2023/1230 에 따른 조화 표준으로도 지정되는지 확인이 필요하다(본문에서 미확인으로 남김).",
    "ANSI/A3 R15.08-3-2026 본문의 사용자 의무 조항(교육·안전 작업 절차·변경 관리)과, 고용노동부의 서비스 로봇 운영 인력 대상 로봇작업 특별교육 적용 지침 확인이 필요하다(oq-265, oq-275).",
    "다음 실행 후보(이번 실행 범위 밖): 48. 안전·위험 관리 페이지 10절에 이번 실행의 f32·f33(VDA 5050 안전 상태·재개 판단), f47·f61(R15.08-3 사용자 의무·배치 후 변경), f54(ISO 10218:2025 사이버보안) 반영."
  ],
  "fixes_applied": [
    "섹션 이름 — patches 의 section 을 대분류 페이지의 기존 H2 그대로 번호 없는 '다른 대분류와의 연결'로 썼고, 다른 절과 auto 마커는 보내지 않았다.",
    "f3 — A. 기획·사업 항목에서 R15.08-3 발행일을 'A3 판매 페이지 기준 2026-04-23, 공개 발표 보도 2026-10-04(Robotics 24/7)'로 함께 쓰고, '2025~2026년에 몰려 있다'는 별도 [추정] 문장으로 분리했으며, ISO 13482 FDIS 단계에 기준일 2026-09-15 와 근거 페이지 원문 미열람을 밝혔다.",
    "f4 — 보험(또는 공제) 의무 가입과 손해보장사업 실시기관 지정만 [사실]로 쓰고 '기사 1건, 2023-11-16 보도 기준'을 밝혔으며, 폭 기준(800mm 미만)과 조항 번호는 쓰지 않았다.",
    "f39 — I. 설계·시뮬레이션 항목에서 공항 터미널 crowdsim 을 '현장 사례가 아니라 시뮬레이션 예제'로만 썼고, Q 항목의 64. 상업 시설 줄에는 현장 사례로 넣지 않고 '아직 다루지 않은 연결'에 64. 상업 시설 실제 사례를 두었으며, site_matrix_updates 에 상업 시설을 넣지 않았다.",
    "f40·f69·f35·f20 — f40 에 '모의 병원 환경의 시뮬레이션 평가', f69 에 '실제 사고가 아닌 모의 사고 시나리오', f35 에 '2026-09-29 보도 기준, 원인 미확정', f20 에 '기사 1건, 2024-07-12 기준'을 문장 안에 밝혔다(Q 항목의 재언급에도 같은 병기).",
    "f10·f11 — C. 채팅 기반 구성·운영 항목의 92% 이상→3% 미만과 공격 성공률 100% 뒤에 각각 '(저자 보고값, 독립 재현 미확인)'을 병기했다.",
    "f47·f61 — J. 현장 운영·관제 항목에 'ANSI 블로그·Robotics 24/7·A3 판매 페이지의 요약 기준이며 표준 본문은 열람하지 않았다'를 밝히고, 안전 작업 절차는 ref-1419, 변경 관리는 ref-1421·ref-1420 각주로 나눠 달았다. O 항목의 f61 에도 'ANSI 블로그 2026-09-17 요약 기준, 표준 본문 미열람'을 넣었다.",
    "f49·f68 — 두 주장 모두 '[추정] 벤더 주장' 형식으로 쓰고, f49 에 '소규모 시범 운영 단계, 플릿 관리 시스템·WMS 연동 언급 없음'을 함께 썼다. 용어집 '무선 안전 비상정지' 정의에 ref-1422 업체 사례에 기댄 용어임을 밝히고 PLd 같은 성능 주장은 넣지 않았다.",
    "f17·f41 및 안전 기능 경계 — f17·f41 을 각각 '연계 대상으로'로 시작하는 한 문장으로 짧게 썼고, 머리 단락과 C·H·K 항목에서 비상정지 회로·보호 필드·무선 안전 정지를 제조사·통합자 몫의 연계 대상으로, ROP 몫을 상태 수신과 작업 보류·재배정·재개 지시로 한정했다.",
    "f55 — P. 거버넌스·법규·사회 항목에서 시행결정 (EU) 2026/2015 로 2026-09-07 관보 게재, 기계류 지침 2006/42/EC 조화까지만 쓰고 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 미확인으로 남겼다.",
    "f64 — 58. 다사업자 책임·계약·데이터 연결에서 R15.08-2 발행 사실만 [사실]로 쓰고, 통합자·ROP 사업자 역할 분담은 A 항목의 f2 [추정]과 oq-096 으로만 연결했다.",
    "18 대 34 구분 — E. 사물·사람·실시간 상태 항목(f18·f19)에 '현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽', I. 설계·시뮬레이션 항목(f38·f39·f40)에 '가정한 미래를 실험하는 34·36 쪽이며 18 과 섞지 않는다'를 문장으로 밝혀 따로 썼다.",
    "각주 정의 — 이번 실행에서 연 ref-004·ref-031·ref-286·ref-406·ref-1116·ref-1419~ref-1426 은 접근일 2026-10-09 만 쓰고, 나머지 재사용 출처 35건은 접근일 뒤에 ' (원문 미열람)'을 붙였으며 reference_updates 에 source_unopened: true 를 넣었다. ref-1423 은 각주와 reference_updates 의 기관 표기를 '법제처 (네플라 위키 게재본, 법제처 원문 미열람)'으로 썼다. ref-004·ref-286·ref-406 의 요약에서 '원문 미열람.' 접두어를 뺐다.",
    "새 열린 질문 2 — 질문을 'ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가?'로 줄였고, 최종판 반영 여부는 F. 연동 항목 본문에서 oq-254 로 연결했다.",
    "기존 연결 표시 — f13·f14·f16·f17(ref-031·ref-470·ref-161), f18~f21(ref-286·ref-1181·ref-1180), f29(ref-104)는 같은 각주 id 를 다시 쓰고 D·E·G 항목 첫머리에 '같은 연결은 … 페이지의 연결 절에도 있다'를 밝혔다.",
    "미근거 연결 — 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설 실제 사례를 내용 없이 '아직 다루지 않은 연결' 소절에 번호와 이름으로 나열했다."
  ],
  "standards_updates": []
}
```

### runs/2026-10-09-09/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/safety/index.md (1개 절)
```

### runs/2026-10-09-09/pages/categories/safety/index.md

```markdown
---
title: "M. 안전"
type: category
status: draft
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-004, ref-031, ref-104, ref-159, ref-161, ref-286, ref-406, ref-417, ref-470, ref-472, ref-562, ref-563, ref-565, ref-567, ref-621, ref-945, ref-980, ref-1076, ref-1079, ref-1080, ref-1081, ref-1083, ref-1084, ref-1116, ref-1117, ref-1118, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-1180, ref-1181, ref-1214, ref-1241, ref-1242, ref-1249, ref-857, ref-700, ref-1341, ref-1419, ref-1420, ref-1421, ref-1422, ref-1423, ref-1424, ref-1425, ref-1426]
---

[홈](../../index.md) › M. 안전

# M. 안전

## 핵심 질문

여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

## 개요

위험성 평가, 안전 기능과 정지·재개, 사람 근접 안전, 비상 대응, 안전 표준·인증, 사고 조사. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **48. 안전·위험 관리** | 위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? | [48. 안전·위험 관리](safety-and-risk-management.md) | published |
| **49. 사람 근접 안전** | 사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 | 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? | [49. 사람 근접 안전](human-proximity-safety.md) | published |
| **50. 안전 표준·인증·사고 조사** | 안전 표준 적합성·인증, 사고 기록과 사후 조사 | 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? | [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

여러 장비가 각각 안전해도 함께 움직일 때 새로운 위험이 생길 수 있다. **로봇·사람·설비의 상호작용 전체**를 위험성 평가의 대상으로 삼아야 한다. [분류원문]

## 다른 대분류와의 연결

M. 안전의 세 세부영역 [48. 안전·위험 관리](safety-and-risk-management.md), [49. 사람 근접 안전](human-proximity-safety.md), [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md)이 다른 16개 대분류와 어디서 만나는지를 대분류별로 정리한다. 근거는 게시된 세부영역·대분류 페이지의 검증된 주장과 이번 실행에서 확인한 출처이며, 다른 대분류 페이지에 이미 있는 연결은 같은 각주를 다시 쓰고 그 사실을 밝힌다.

이 절에서 비상정지 회로·보호 필드·무선 안전 정지 같은 안전 기능 자체는 로봇 제조사·통합자 몫의 연계 대상으로 적는다. ROP 몫은 안전 상태를 받아 작업을 보류·재배정하고 재개를 지시하는 범위로 한정한다. 승강기 모드 제어, 동시적 위치추정·지도작성(SLAM) 같은 로봇 자체 기능, 법령 해석과 적용 판단도 연계 대상이다.

### A. 기획·사업

[A. 기획·사업](../planning-and-business/index.md)과는 안전 책임의 분담, 표준 개정 일정, 실외 로봇의 보험 비용으로 만난다.

책임 분담에서는 48. 안전·위험 관리가 2. 사용 사례·요구·책임 범위와 만난다. ANSI/A3 R15.08 시리즈는 로봇 자체(1부), 산업용 이동로봇 시스템·적용의 통합(2부, 2023), 사용자의 산업용 이동로봇 적용 사용(3부, 2026)으로 나뉘어 제조사·통합자·사용자의 안전 책임을 부별로 다룬다. [사실][^ref-1419][^ref-1084] 통합자와 사용자의 의무가 따로 있으므로, 여러 제조사 로봇을 묶는 ROP 사업자가 현장마다 통합자 역할을 맡는지 사용자의 위험성평가를 지원하는 데 머무는지가 책임 범위 정의에 들어가야 할 것으로 보인다(열린 질문 oq-096). [추정][^ref-1419][^ref-1084][^ref-472]

표준 개정 일정에서는 50. 안전 표준·인증·사고 조사가 1. 기술·시장·업체 동향과 만난다. ISO 10218-1/-2 개정판은 2025-02에 나왔고, EN ISO 판의 참조는 2026-09-07 EU 관보에 실렸다. [사실][^ref-1116] ANSI/A3 R15.08-3 의 발행일은 A3 판매 페이지 기준 2026-04-23이고, 공개 발표 보도는 2026-10-04(Robotics 24/7)이다. [사실][^ref-1420][^ref-1421] ISO 13482 개정판은 2026-09-15 기준 최종 국제표준안(FDIS) 단계다(근거 페이지 원문은 열람하지 않았다). [사실][^ref-1117] 이를 종합하면 주요 로봇 안전 표준의 개정이 2025~2026년에 몰려 있는 것으로 보인다. [추정][^ref-1116][^ref-1420][^ref-1117]

비용·조달에서는 50. 안전 표준·인증·사고 조사가 3. 경제성·조달·사업 모델과 만난다. 2023-11-17 시행된 개정 지능형로봇법에 따라 보도에서 실외이동로봇을 운영하는 자는 보험(또는 공제)에 의무 가입해야 하고, 산업통상자원부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정해 보험상품 출시를 지원한다(기사 1건, 2023-11-16 보도 기준). [사실][^ref-1424] 실외 로봇 도입에서는 보험 가입과 인증 유지가 운영비 항목이 될 것으로 보인다. [추정][^ref-1424] 인증 단위가 로봇과 관제장치의 조합이므로, 관제를 맡는 ROP 사업자가 운영자 의무 범위에 드는지가 조달·계약 단계의 쟁점이 될 것으로 보인다. [추정][^ref-1424][^ref-980]

### B. 로봇 온톨로지

[B. 로봇 온톨로지](../robot-ontology/index.md)와는 로봇이 지금 관제를 받을 수 있는 상태인지, 어떤 안전 표준·인증을 지니는지를 표현하는 일로 만난다.

VDA 5050 3.0.0 의 운용 모드 가운데 관제가 로봇을 제어하는 것은 AUTOMATIC(관제가 완전히 제어)과 SEMIAUTOMATIC(관제가 제어하되 주행 속도는 사람–기계 인터페이스(Human-Machine Interface, HMI)가 조정)이고, INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 로봇을 제어하지 않는다. [사실][^ref-031] 따라서 6. 온톨로지 기반 시스템·로봇 연동의 실행 시점 조건 판단에 배터리·적재 상태와 함께 운용 모드와 안전 상태(비상정지·보호 필드 침범)를 넣어야, 관제가 제어권이 없는 로봇에 작업을 내리지 않을 것으로 보인다. [추정][^ref-031]

등록 정보 쪽에서는 로봇마다 R15.08 유형(A·B·C), 적용 안전 표준과 판, 인증 상태를 4. 이기종 로봇 등록의 등록 정보로 두면 표준 개정과 인증 범위를 배정·경로 제약으로 추적할 수 있을 것으로 보인다. [추정][^ref-1419][^ref-1116][^ref-980]

### C. 채팅 기반 구성·운영

[C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)과는 대화 지시가 로봇 동작으로 이어지기 전의 안전 검사로 만나며, 12. 채팅으로 업무 지시·오케스트레이션과 13. 대화형 기능의 신뢰·기반에 걸친다. 분류 원문 C. 채팅 기반 구성·운영 주석은 대화 결과를 실행 명령이 아니라 계획으로 보고 '사람이 확인·승인한 계획만 실행'하게 한다. 12. 채팅으로 업무 지시·오케스트레이션은 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링을 대화로 쓰게 하는 기능이므로(분류 원문 C 주석), 아래 G. 계획·최적화 연결과 짝으로 읽는다.

Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트(SafeGate)와 작업 안전 계약을 두는 방법을 제안했다. [사실][^ref-417] Ravichandran 외의 RoboGuard 에서는 악성 프롬프트와 격리한 신뢰 기점 대규모 언어 모델(Large Language Model, LLM)이 미리 정한 안전 규칙을 시간 논리 제약으로 바꾸고, 제어 합성으로 계획과의 충돌을 푼다(2026-03 개정판 기준). [사실][^ref-700] 저자들은 최악의 탈옥 공격에서 위험 계획 실행이 92% 이상에서 3% 미만으로 줄었다고 보고했다(저자 보고값, 독립 재현 미확인). [사실][^ref-700] 반대로 Robey 외(2024-10)는 언어 모델이 제어하는 로봇이 해로운 물리 행동을 하도록 만드는 탈옥 알고리즘 RoboPAIR 를 제시했고, GPT-4o 계획기를 쓴 Clearpath Jackal 과 GPT-3.5 를 연동한 Unitree Go2 등에서 공격 성공률이 자주 100%에 이르렀다고 보고했다(저자 보고값, 독립 재현 미확인). [사실][^ref-857]

이 연구들을 보면, '사람이 확인·승인한 계획만 실행' 원칙에 실행 전 안전 게이트·가드레일 같은 자동 검사를 더할 때 대화 지시에서 로봇 동작까지 이어지는 경로가 48. 안전·위험 관리의 위험성평가 대상이 될 것으로 보이며, 로봇 자체 안전 기능은 연계 대상으로 남는다. [추정][^ref-417][^ref-700] 관련 열린 질문은 oq-144·oq-302 다.

### D. 공간·지도 모델

[D. 공간·지도 모델](../space-and-map-model/index.md)과는 지도에 붙은 구역 규칙이 안전 조치로 인정받을 수 있는지, 운용 구역을 어떻게 정의하는지로 만난다. 같은 연결은 D. 공간·지도 모델 페이지의 연결 절에도 있다.

VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 여기거나 적용해서는 안 된다고 범위 절에 적는다. [사실][^ref-031] 구역 규칙(16. 장소 의미·지도 관리)을 보면, BLOCKED 구역에는 로봇이 들어가서는 안 되고 구역 안에 있는 로봇은 멈춘 뒤 BLOCKED_ZONE_VIOLATION 오류를 CRITICAL 수준으로 보고하며, SPEED_LIMIT 구역에서는 구역에 들어설 때 이미 최대 속도(m/s) 이하여야 한다. [사실][^ref-031] 따라서 지도에 붙은 진입 금지·속도 제한 구역은 교통 관리 규칙이지 안전 기능이 아니며, 49. 사람 근접 안전의 위험성평가에서 이를 위험 감소 조치로 인정받으려면 ISO 3691-4 의 운용 구역 준비와 로봇의 안전 등급 보호 필드 설정에 맞춰야 할 것으로 보인다(oq-229). [추정][^ref-031][^ref-470]

48. 안전·위험 관리와 15. 지도·공간·위치 모델은 운용 구역 정의로도 이어진다. ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다(2023-06 발행, 표준 본문 미열람, oq-170). [사실][^ref-470] 연계 대상으로, SLAM 위치추정의 안전성을 무결성 위험 지표로 정량화한 연구(IJRR, 2025-05)는 데이터 연관 오류와 지나치게 높은 랜드마크 밀도가 안전성을 떨어뜨릴 수 있다고 보고했으나 위치추정 자체는 로봇 자체 지능·제어 경계에 속한다. [사실][^ref-161]

### E. 사물·사람·실시간 상태

[E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)와는 설비·사람의 현재 상태를 안전 판단에 쓰는 일로 만난다. 이 연결은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이며, 아래 I. 설계·시뮬레이션의 가정한 미래 실험과 구분한다. 같은 연결은 E. 사물·사람·실시간 상태 페이지의 연결 절에도 있다.

Open-RMF 승강기 상태(LiftState)의 현재 모드에는 알 수 없음·사람·무인 운반 차량(Automated Guided Vehicle, AGV)·화재·오프라인·비상이 있고, 이 가운데 사람·AGV 모드만 설정할 수 있으며 나머지는 읽기 전용이다. [사실][^ref-286] 승강기의 화재·비상 모드 제어는 시설·설비 제어 경계의 연계 대상이고, ROP 는 탑승을 확정하기 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다(모드 정보를 몇 초까지 믿을지는 oq-034). [추정][^ref-286]

사람 흐름 쪽에서는 49. 사람 근접 안전이 19. 사람·보행자 모델과 만난다. 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다(기사 1건, 2024-07-12 기준). [사실][^ref-1181] 병원의 사람·휠체어 대기 규칙이나 창고의 학습된 사람 흐름처럼 사람 흐름 정보는 구역·시간대별 대기·속도 규칙으로 49. 사람 근접 안전과 이어질 것으로 보이며, 이때 사람 검출·안전 정지는 로봇이 맡는 연계 대상이다. [추정][^ref-1181][^ref-1180]

### F. 연동

[F. 연동](../integration/index.md)과는 상호운용 규격과 안전 표준의 경계, 비상 신호 전달, 승강기 탑승 안전으로 만난다.

상호운용 표준 쪽에서는 50. 안전 표준·인증·사고 조사가 21. 상호운용 표준·적합성과 만난다. 앞의 D. 공간·지도 모델 항목에서 본 VDA 5050 의 범위 선언에 더해, ISO 21423(산업용 이동로봇 통신·상호운용성)의 범위는 여러 제조사 자율이동로봇(Autonomous Mobile Robot, AMR)·플릿 관리 장비·기업 자원 사이의 통신 프로토콜이며 안전 요구와 공공 도로 이동 기계는 범위에서 뺀다(2026-10-09 확인, 발행 진행 중 단계). [사실][^ref-159] 따라서 연동 적합성 시험(21. 상호운용 표준·적합성)과 안전 표준 적합성·인증(50. 안전 표준·인증·사고 조사)은 별도 경로로 관리해야 할 것으로 보인다. [추정][^ref-031][^ref-159]

비상 신호 쪽에서는 48. 안전·위험 관리가 20. 로봇·제조사 관제 연동과 만난다. Open-RMF 기능 요청 이슈 #658 은 화재경보가 울리면 로봇들이 주차 위치로 이동하지만 비상 신호가 대상 플릿을 구분하지 않는 불리언 값이라고 지적한다(2025-04-04 이슈 작성 기준, 이후 구현 여부 미확인). [사실][^ref-567]

승강기 탑승 쪽에서는 50. 안전 표준·인증·사고 조사가 22. 설비·건물 시스템 연동과 만난다. 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했다. [사실][^ref-945] ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 구성을 로봇 유형별로 바꾸고 탑승형 로봇 절을 뺐으며, 사이버보안·데이터 보호·승강기와 협동하는 로봇(참고 부속서 H) 절을 새로 넣었다(초안 기준). [사실][^ref-1425] 탑승 안전 요구가 국내 KS 와 서비스 로봇 안전 표준 개정 초안 양쪽에 들어오므로, ROP 는 승강기 연동 요청·운영 모드 확인을 맡고 탑승 안전의 적합성은 로봇·승강기 쪽 표준에 맡기는 경계가 될 것으로 보인다(초안 내용이 최종판에 남았는지는 oq-254 에서 확인한다). [추정][^ref-945][^ref-1425][^ref-1117]

### G. 계획·최적화

[G. 계획·최적화](../planning-and-optimization/index.md)와는 배정·경로·대피 동작에 안전을 반영하는 일로 만난다. 비상 경보 때의 주차 동작은 G. 계획·최적화 페이지의 연결 절에도 있다.

배정 쪽에서 49. 사람 근접 안전은 25. 작업 배정 — MRTA와 만난다. Kazemi Eskeri 외(IROS 2025)는 사람과 함께 쓰는 환경에서 사람을 고려하는 다중 로봇 작업 배정 방법을 다뤘다. [사실][^ref-1083]

경로 쪽에서 48. 안전·위험 관리는 27. 다중 로봇 경로·교통 관리 — MAPF와 만난다. Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004] Reliability Engineering & System Safety 게재 연구(2023, 저자 미확인)는 다중 이동로봇 운반 작업의 충돌 위험원을 시스템 이론적 프로세스 분석(System-Theoretic Process Analysis, STPA)과 확률 페트리넷(SPN)으로 모델링·분석했다. [사실][^ref-565]

공용 자원 쪽에서 48. 안전·위험 관리는 28. 공용 자원·충전·에너지 최적화와 만난다. Open-RMF 데모에서는 비상 경보가 켜지면 로봇들을 가장 가까운 주차 위치로 보낸다. [사실][^ref-104]

### H. 실행·협업·예외 복구

[H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)와는 정지 뒤 재개 판단, 통신 단절 때의 동작, 비정상 작업 중 사고로 만난다.

재개 판단 쪽에서 48. 안전·위험 관리는 29. 명령·작업 실행의 신뢰성·31. 사람–로봇 협업과 만난다. VDA 5050 3.0.0 의 안전 상태(safetyState)는 activeEmergencyStop 을 MANUAL(로봇에서 수동 확인), REMOTE(시설 비상정지를 원격 확인), NONE 으로 보고하고, fieldViolation 으로 레이저·범퍼 같은 보호 필드 침범 여부를 보고한다. [사실][^ref-031] 앞의 B. 로봇 온톨로지 항목의 운용 모드 구분과 함께 보면, ROP 의 재개 지시는 비상정지가 NONE 이고 운용 모드가 AUTOMATIC 으로 돌아온 것을 확인한 뒤에 내려야 할 것으로 보인다. [추정][^ref-031] MANUAL 비상정지는 로봇에서 사람이 확인해야 하므로 현장 인력 출동이 복구 절차에 들어갈 것으로 보인다(oq-095). [추정][^ref-031]

통신 단절 쪽에서는 32. 예외 복구·재계획·업무 연속성과 만난다. VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다. [사실][^ref-031]

비정상 작업 중 사고에서는 50. 안전 표준·인증·사고 조사가 32. 예외 복구·재계획·업무 연속성과 J. 현장 운영·관제의 40. 운영 절차·요청 창구와 만난다. 2026-09 식품 제조 공장에서 멈춘 제품 적재 로봇을 점검하던 노동자가 끼여 숨진 사고에 대해, 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(Lockout/Tagout, LOTO)가 실시되지 않았다고 지적했다(2026-09-29 보도 기준, 원인 미확정). [사실][^ref-1125] 2023-11 농산물유통센터에서는 상자를 팔레트로 옮기는 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌다(2023-11-08 보도 기준). [사실][^ref-1124] 두 사망 사고가 모두 점검·작동 확인 같은 비정상 작업 중에 났으므로, ROP 가 정지 뒤 재가동·재개를 지시하기 전에 작업 중인 사람과 잠금 상태를 확인하는 절차가 복구 절차와 운영 절차의 접점이 될 것으로 보인다. [추정][^ref-1124][^ref-1125][^ref-031]

### I. 설계·시뮬레이션

[I. 설계·시뮬레이션](../design-and-simulation/index.md)과는 위험을 현장 투입 전에 가상으로 찾는 일로 만난다. 이 연결은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현 쪽이며, 앞의 E. 사물·사람·실시간 상태 항목에서 다룬 현재 상태 표현(18. 실시간 세계 상태·데이터 일관성)과 섞지 않는다.

48. 안전·위험 관리 쪽에서, Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 만들어 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. [사실][^ref-1241]

49. 사람 근접 안전 쪽에서는 34. 시뮬레이션·예측용 디지털 트윈과 19. 사람·보행자 모델이 함께 쓰인다. Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션에 쓴다(현장 사례가 아니라 시뮬레이션 예제다). [사실][^ref-406] Rondoni 외(Scientific Reports, 2024-08)는 모의 병원 환경의 시뮬레이션 평가에서 병원 물류 로봇 HOSBOT 과 TIAGo 를 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 7개 지표로 비교했고, 최고 속도에서는 방향 오차가 커졌다. [사실][^ref-1081]

연계 대상으로, IEC 61508-7 이 시뮬레이션을 시험 목적의 설비 거동 모사로 정의한다고 인용한 업체 인터뷰(2014)는 기능안전 표준이 안전 확인에 시뮬레이션을 권고한다고 해석했으나 이동로봇 안전 인증이 시뮬레이션 결과를 근거로 받아들이는 절차는 찾지 못했다. [추정][^ref-1249]

### J. 현장 운영·관제

[J. 현장 운영·관제](../field-operations-and-monitoring/index.md)와는 사고 조사용 기록, 실행 중 감시, 사용자 운영 절차로 만난다.

기록 쪽에서 50. 안전 표준·인증·사고 조사는 37. 관제 화면·실행 기록과 만난다. Winfield 외(2022-05)는 사회적 로봇의 사고 조사를 위한 윤리적 블랙박스(Ethical Black Box) 개방 표준 초안을 제안했다. [사실][^ref-1120] 플릿 수준에서 명령·정지·재가동·운용 모드 전환·안전 상태 보고를 시각과 함께 남기는 실행 기록이 사고·아차 사고 조사의 입력이 될 것으로 보이나, 그 최소 항목을 정한 표준은 확인하지 못했다(oq-252). [추정][^ref-1120][^ref-1122][^ref-031]

감시 쪽에서는 38. 모니터링·이상 탐지·원인 분석과 만난다. Sanders·Sener·Chen(Applied Ergonomics, 2024)은 미국 산업안전보건청(OSHA) 중대 부상 보고(Severe Injury Reports)에서 작업장 로봇 관련 부상을 분석했다. [사실][^ref-1122] Ferrando 외(2020)의 ROSMonitoring 은 로봇 운영체제(Robot Operating System, ROS) 응용의 형식 속성을 ROS 바깥에서 명세해 실행 중에 검증하는 런타임 검증 틀이며, 여러 ROS 배포판에 옮겨 쓸 수 있고 특정 명세 형식에 묶이지 않는다. [사실][^ref-1426] 진입 금지 구역 위반이나 정지 지시 뒤 응답처럼 안전과 관련된 운영 규칙을 실행 중에 감시하는 런타임 검증이 38. 모니터링·이상 탐지·원인 분석과 48. 안전·위험 관리를 잇는 방법이 될 것으로 보이나, 제조사가 다른 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-1426][^ref-031]

운영 절차 쪽에서는 40. 운영 절차·요청 창구와 만난다. ANSI/A3 R15.08-3-2026 은 산업용 이동로봇을 운영하는 사용자에게 위험성평가와 직원 교육을 요구한다. [사실][^ref-1419][^ref-1421] ANSI 블로그(2026-09-17)는 여기에 위험 감소 조치의 유지와 안전 작업 절차를 든다. [사실][^ref-1419] Robotics 24/7(2026-10-04)과 A3 판매 페이지는 변경 관리를 사용자 의무로 든다. [사실][^ref-1421][^ref-1420] 이 내용은 ANSI 블로그·Robotics 24/7·A3 판매 페이지의 요약 기준이며 표준 본문은 열람하지 않았다. R15.08-3 의 사용자 교육·안전 작업 절차 요구는 40. 운영 절차·요청 창구의 현장 절차와 O. 검증·도입·수명주기의 56. 운영 이관·확대·교육의 교육 계획으로 넘어갈 것으로 보이나, 여러 제조사 로봇이 섞인 현장에서 누가 이를 이행하는지는 확인하지 못했다(oq-265). [추정][^ref-1419][^ref-1421] 점검 중 사고와 잠금 확인 절차는 앞의 H. 실행·협업·예외 복구 항목에 적었다.

### K. 플랫폼 아키텍처·인프라

[K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)와는 플릿 일괄 정지 신호를 어떤 통신 경로에 둘지로 만나며, 48. 안전·위험 관리와 42. 분산 시스템·통신·컴퓨팅 구조가 맞닿는다.

FORT Robotics 사례 소개에 따르면, 한 창고의 울타리 친 AMR 구역에서 문에 단 주 제어기가 문이 열리면 구역의 로봇들에 무선 안전 비상정지를 보내며 이 시스템은 ISO 13849 범주 3·PLd 로 설계됐다고 한다(2023-05-18 게재). [추정] 벤더 주장[^ref-1422] 이 사례는 소규모 시범 운영 단계이고, 플릿 관리 시스템·창고 관리 시스템(WMS) 연동은 언급하지 않는다. [추정] 벤더 주장[^ref-1422] VDA 5050 은 안전 표준이 아니고 연결이 끊긴 로봇은 받은 주문을 이어 수행하므로, 플릿 일괄 정지는 관제 메시지 경로가 아니라 그와 독립된 안전 등급 정지 경로에 맡기고 ROP 는 정지 결과를 상태로 받아 작업을 보류·재배정하는 구조가 두 대분류의 경계가 될 것으로 보인다(oq-095). [추정][^ref-031][^ref-1422]

### L. AI·학습 기술

[L. AI·학습 기술](../ai-and-learning/index.md)과는 AI 가 정지·경로·구역 결정에 관여할 때의 규제 분류와 채택 검사로 만난다. 교차 규칙에 따라 이 내용은 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과, 적용 대상인 48. 안전·위험 관리 양쪽에 연결한다.

EU AI Act(Regulation (EU) 2024/1689)는 부속서 I 의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이면서 제3자 적합성 평가를 받는 AI 시스템을 고위험 AI 로 분류한다. [사실][^ref-621] 법무법인 태평양 해설에 따르면, 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을 정하게 하고 운영 단계에서 성능 저하·오류의 정기 점검과 관리자 교육을 요구한다(2025-09 초안 기준 해설). [사실][^ref-1341] AI 가 정지·경로·구역 결정에 관여하면 실행 전 안전 게이트 같은 채택 검사는 47. AI·학습·적응과 모델 운영의 채택 기준과 48. 안전·위험 관리의 위험성평가 양쪽에 걸칠 것으로 보이며, 이런 AI 가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106). [추정][^ref-621][^ref-417]

### N. 보안·개인정보

[N. 보안·개인정보](../security-and-privacy/index.md)와는 안전 표준에 들어온 사이버보안·데이터 보호 요구와, 공격이 안전 사고로 번지는 경로로 만난다.

산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다(조항 번호 미확인, oq-102). [사실][^ref-1116][^ref-1076] 서비스 로봇 쪽에서도 앞의 F. 연동 항목의 ISO 13482 개정 초안이 사이버보안·데이터 보호 절을 새로 넣었다(초안 기준). [사실][^ref-1425] 이렇게 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제(51. 인증·권한·격리)와 사람 위치·영상 데이터 처리(53. 개인정보·영상 데이터)도 안전 평가 대상이 될 것으로 보인다. [추정][^ref-1116][^ref-1425]

52. 통신 보호·위협 관리·감사 쪽에서는 공격이 안전 문제로 번진다. Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. [사실][^ref-1242] 언어 모델 제어 로봇의 탈옥 공격(RoboPAIR)은 앞의 C. 채팅 기반 구성·운영 항목에 적었으며, 같은 내용이 52. 통신 보호·위협 관리·감사와도 이어진다.

### O. 검증·도입·수명주기

[O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)와는 안전 시험, 배치 전 위험성평가, 법정 교육, 배치 후 변경 관리로 만난다.

시험 쪽에서는 54. 시험·형식 검증·벤치마크와 만난다. 앞의 J. 현장 운영·관제 항목의 런타임 검증 틀(ROSMonitoring)이 이 영역에도 걸치며, 49. 사람 근접 안전의 평가 기준과 관련해 Francis 외(2023)는 사회적 로봇 내비게이션 알고리즘의 평가 원칙과 지침을 정리했다. [사실][^ref-1079]

배치 전 평가 쪽에서는 55. 현장 조사·설치·시운전과 만난다. Belzile 외(2025-02)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과 이동로봇 전용이면서 여러 배치 상황에 적용할 수 있는 표준이 없다고 보고, 건설 현장 이동로봇 배치 전에 쓸 위험성평가 틀을 제안했다(프리프린트). [사실][^ref-563]

법정 교육 쪽에서는 56. 운영 이관·확대·교육과 만난다. 법제처 법령해석 23-0872(2023-11-21)는 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 '산업용 로봇'을 쓰는 작업으로 한정되지 않는다고 회답했고, KS B ISO 8373 의 '로봇'이 산업용·서비스용·의료용을 포괄한다는 점을 근거로 들었다(제3자 게재본 기준, 법원 판결 같은 기속력은 없음). [사실][^ref-1423] 따라서 서비스·이동 로봇을 쓰는 작업도 로봇작업 특별교육 대상이 될 수 있으므로, ROP 를 들인 현장의 운영 이관 교육 계획에 법정 특별교육 해당 여부 판단이 들어가야 할 것으로 보이나 고용노동부의 적용 지침은 확인하지 못했다(oq-275). [추정][^ref-1423] 앞의 L. AI·학습 기술 항목의 관리자 교육 요구(초안 기준 해설)와 J. 현장 운영·관제 항목의 R15.08-3 교육 요구도 56. 운영 이관·확대·교육과 이어진다.

배치 후 변경 쪽에서는 57. 자산·소프트웨어 수명주기 관리와 만난다. R15.08-3 은 공급자가 배치한 뒤 사용자가 산업용 이동로봇이나 그 적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다고 한다(ANSI 블로그 2026-09-17 요약 기준, 표준 본문 미열람). [사실][^ref-1419] ROP 에서 구역·속도 제한·경로망·운영 정책을 바꾸는 일이 사용자 쪽 변경 관리와 위험성 재평가의 계기가 될 수 있으므로, 설정 변경 이력을 판 단위로 남기고 재평가 필요 여부를 표시하는 기능이 48. 안전·위험 관리와 57. 자산·소프트웨어 수명주기 관리를 잇는 것으로 보인다(oq-093, oq-282). [추정][^ref-1419][^ref-031]

### P. 거버넌스·법규·사회

[P. 거버넌스·법규·사회](../governance-law-and-society/index.md)와는 다사업자 책임, 법령·인증·보험, 사회적 수용으로 만난다.

다사업자 책임 쪽에서 48. 안전·위험 관리는 58. 다사업자 책임·계약·데이터와 만난다. ANSI/A3 R15.08-2 는 2023-10 산업용 이동로봇 시스템과 적용의 안전 요구를 다루는 2부로 발표됐다. [사실][^ref-472][^ref-1084] 통합자와 ROP 사업자의 역할 분담은 이 발행 사실만으로 정해지지 않으며, 앞의 A. 기획·사업 항목의 추정과 열린 질문 oq-096 으로 이어진다.

법령·인증 쪽에서 50. 안전 표준·인증·사고 조사는 59. 법·규제·보험·라이선스와 만난다. EN ISO 10218-1:2025·-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015 로 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다. [사실][^ref-1116] 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 미확인이다. 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거하며, 인증 절차와 기준은 산업통상자원부 고시(2023-11-17)로 정해졌다. [사실][^ref-980][^ref-1118] 심사 항목 수는 출처마다 달라 열린 질문 oq-186·oq-230 에서 다룬다. 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 산업용 로봇의 운전 중 위험 방지 조치를 정하고, 한국산업표준이나 국제 안전기준에 맞는 경우 방책 같은 조치를 생략할 수 있게 한다(2023-07-01 시행본 기준, 물류센터 AMR 플릿 적용 여부는 oq-097). [사실][^ref-562] 실외이동로봇 운영자의 보험 의무는 앞의 A. 기획·사업 항목에 적었다.

사회적 수용 쪽에서 49. 사람 근접 안전은 60. 노동·수용성·접근성과 만난다. Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명을 면담하고 공동설계 워크숍을 연 결과, 이동장애인이 보도 로봇과 보도 공간을 두고 경쟁한다고 느끼고 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. [사실][^ref-1214]

### Q. 현장 유형별 적용

[Q. 현장 유형별 적용](../site-type-applications/index.md)은 현장마다 다른 요구를 모으고, 위 연결 가운데 모든 현장에 공통인 기능은 A~P 의 대분류에 둔다. 아래는 M. 안전의 근거가 있는 현장 유형이다.

- **61. 물류창고**: 상자를 팔레트로 옮기는 로봇의 점검 중 사망 사고가 있다(2023-11-08 보도 기준, 앞의 H. 실행·협업·예외 복구 항목). [사실][^ref-1124] 울타리 구역의 무선 안전 비상정지 사례도 있으나 업체 소개 기준이다(앞의 K. 플랫폼 아키텍처·인프라 항목). [추정] 벤더 주장[^ref-1422] 아마존은 자사 풀필먼트 센터에서 직원이 로보틱스 테크 조끼를 켜고 로봇 구역에 들어가면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명하며, 감속 속도·거리 값은 공개되지 않았다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1080]
- **62. 제조 공장**: 식품 제조 공장의 적재 로봇 점검 중 끼임 사망 사고와 잠금·표지 미실시 지적이 있다(2026-09-29 보도 기준, 원인 미확정, 앞의 H. 실행·협업·예외 복구 항목). [사실][^ref-1125]
- **63. 병원·의료**: 병원의 로봇 통행 경로·작업 정지 지점 표시(기사 1건, 앞의 E. 사물·사람·실시간 상태 항목)와 모의 병원 환경의 주행 속도 시뮬레이션 평가(앞의 I. 설계·시뮬레이션 항목)가 있다. [사실][^ref-1181][^ref-1081]
- **65. 가정·공동주택**: Webb 외(2021)는 지원 주거 아파트에서 넘어진 거주자를 보조 로봇이 직원에게 알리지 못한 모의 사고를 역할극 증언 면담과 윤리적 블랙박스 기록으로 조사하는 방법을 시험했다(실제 사고가 아닌 모의 사고 시나리오). [사실][^ref-1121]
- **66. 실외**: 한국로봇산업진흥원은 실외이동로봇 운행안전인증 대상을 최고 속도 15km/h 이하·최대 질량 500kg 이하로 두고 주변 인식과 비상정지를 심사하며, 인증 뒤 2년 주기 정기점검을 둔다(확인일 2026-09-30). [사실][^ref-980] 운영자 보험 의무(앞의 A. 기획·사업 항목)와 보도 접근성 연구(앞의 P. 거버넌스·법규·사회 항목)도 실외 현장의 요구다. [사실][^ref-1424][^ref-1214]
- **67. 기타 현장**: 건설 현장 이동로봇 배치 전 위험성평가 틀 제안이 있다(프리프린트, 앞의 O. 검증·도입·수명주기 항목). [사실][^ref-563]
- **64. 상업 시설**: 실제 현장의 사람 근접 안전 사례는 아직 다루지 않았다. 앞의 I. 설계·시뮬레이션 항목의 공항 터미널 군중 시뮬레이션은 시뮬레이션 예제이므로 현장 사례로 세지 않는다.

### 아직 다루지 않은 연결

다음 연결은 이번 실행의 근거가 없어 내용을 채우지 않았다: 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 그리고 64. 상업 시설의 실제 사람 근접 안전 사례.

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-10-09 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-10-09 (원문 미열람)
[^ref-161]: Abdul Hafez, O., Joerger, M., & Spenko, M., Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach, 2025-05, https://journals.sagepub.com/doi/10.1177/02783649241287797, 접근일 2026-10-09 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09
[^ref-417]: Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-09 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-10-09 (원문 미열람)
[^ref-472]: A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-10-09 (원문 미열람)
[^ref-562]: 국가법령정보센터(고용노동부), 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지), 2023-07-01, https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0, 접근일 2026-10-09 (원문 미열람)
[^ref-563]: Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02, https://arxiv.org/abs/2502.20693, 접근일 2026-10-09 (원문 미열람)
[^ref-565]: Reliability Engineering & System Safety (저자 미확인), Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN, 2023, https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534, 접근일 2026-10-09 (원문 미열람)
[^ref-567]: Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf, 2025-04-04, https://github.com/open-rmf/rmf/issues/658, 접근일 2026-10-09 (원문 미열람)
[^ref-621]: European Commission, AI Act | Shaping Europe's digital future, 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-10-09 (원문 미열람)
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-10-09 (원문 미열람)
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-09 (원문 미열람)
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-10-09 (원문 미열람)
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-06-29, https://arxiv.org/abs/2306.16740, 접근일 2026-10-09 (원문 미열람)
[^ref-1080]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-10-09 (원문 미열람)
[^ref-1081]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-10-09 (원문 미열람)
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-09 (원문 미열람)
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-10-09 (원문 미열람)
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-10-09
[^ref-1117]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-10-09 (원문 미열람)
[^ref-1118]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-10-09 (원문 미열람)
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09 (원문 미열람)
[^ref-1121]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-10-09 (원문 미열람)
[^ref-1122]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-10-09 (원문 미열람)
[^ref-1124]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-10-09 (원문 미열람)
[^ref-1125]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-10-09 (원문 미열람)
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-10-09 (원문 미열람)
[^ref-1181]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-10-09 (원문 미열람)
[^ref-1214]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-10-09 (원문 미열람)
[^ref-1241]: Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020), Simulation-based Testing for Early Safety-Validation of Robot Systems, 2020-11-20, https://arxiv.org/abs/2011.10294, 접근일 2026-10-09 (원문 미열람)
[^ref-1242]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09 (원문 미열람)
[^ref-1249]: Wind River (Engblom, J. 인터뷰, Buchwieser, A.), Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser, 2014-11-20, https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser, 접근일 2026-10-09 (원문 미열람)
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv), Jailbreaking LLM-Controlled Robots, 2024-10-17, https://arxiv.org/abs/2410.13691, 접근일 2026-10-09 (원문 미열람)
[^ref-700]: Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03-10, https://arxiv.org/abs/2503.07885, 접근일 2026-10-09 (원문 미열람)
[^ref-1341]: 법무법인 태평양(BKL) AI팀, AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인, 2025-09-30, https://www.bkl.co.kr/law/insight/newsletter/6248, 접근일 2026-10-09 (원문 미열람)
[^ref-1419]: ANSI (American National Standards Institute) Blog, ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 2026-09-17, https://blog.ansi.org/?p=190868, 접근일 2026-10-09
[^ref-1420]: A3(Association for Advancing Automation), ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications, 2026-04-23, https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download, 접근일 2026-10-09
[^ref-1421]: Robotics 24/7, A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available, 2026-10-04, https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available, 접근일 2026-10-09
[^ref-1422]: FORT Robotics (A3 Case Studies 게재), Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs, 2023-05-18, https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs, 접근일 2026-10-09
[^ref-1423]: 법제처 (네플라 위키 게재본, 법제처 원문 미열람), [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련), 2023-11-21, https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k, 접근일 2026-10-09
[^ref-1424]: 메트로신문 (한용수), 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막, 2023-11-16, https://www.metroseoul.co.kr/article/20231116500208, 접근일 2026-10-09
[^ref-1425]: DIN Media, DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024), 2024-10, https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303, 접근일 2026-10-09
[^ref-1426]: Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS), ROSMonitoring: A Runtime Verification Framework for ROS, 2020-12-03, https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/, 접근일 2026-10-09

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 49건이다(논문 15건 · 기사·보고서 10건 · 업체 발표 1건 · 표준·오픈소스·기관 자료 23건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1085](../../references/ref-1085.md) — Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters (발행 2026-04-15)
- [ref-417](../../references/ref-417.md) — Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems (발행 2026-04)
- [ref-1076](../../references/ref-1076.md) — Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 (발행 2026-02-19)
- [ref-1083](../../references/ref-1083.md) — Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments (발행 2025-08-27)
- [ref-1082](../../references/ref-1082.md) — Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario (발행 2025-03-27)
- [ref-563](../../references/ref-563.md) — Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment (발행 2025-02)
- [ref-1081](../../references/ref-1081.md) — Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments (발행 2024-08-07)
- [ref-1122](../../references/ref-1122.md) — Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports (발행 2024)
- [ref-1079](../../references/ref-1079.md) — Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms (발행 2023-06-29)
- [ref-565](../../references/ref-565.md) — Reliability Engineering & System Safety (저자 미확인), Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN (발행 2023)
- 그 밖에 5건

**기사·보고서**

- [ref-1125](../../references/ref-1125.md) — 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 (발행 2026-09-29)
- [ref-1116](../../references/ref-1116.md) — IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2 (발행 2026-09-18)
- [ref-791](../../references/ref-791.md) — Intertek, Machines Got Smarter, Now ISO 12100 has to Catch Up (발행 2025-12-11)
- [ref-1115](../../references/ref-1115.md) — The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul (발행 2025-02)
- [ref-1078](../../references/ref-1078.md) — 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠" (발행 2024-03-09)
- [ref-1124](../../references/ref-1124.md) — 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 (발행 2023-11-08)
- [ref-1084](../../references/ref-1084.md) — The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2 (발행 2023-10-26)
- [ref-992](../../references/ref-992.md) — 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (발행 2023-07-28)
- [ref-1123](../../references/ref-1123.md) — 서울신문, [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인) (발행 2017-04-07)
- [ref-471](../../references/ref-471.md) — A3(Association for Advancing Automation), Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) (발행 미확인)

**업체 발표**

- [ref-1080](../../references/ref-1080.md) — Amazon, Ever wonder how people and robots team up on your Amazon order? (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-567](../../references/ref-567.md) — Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf (발행 2025-04-04)
- [ref-560](../../references/ref-560.md) — ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells (발행 2025-02)
- [ref-790](../../references/ref-790.md) — DIN Media, DIN EN ISO 12100 - 2025-01 (Draft standard) (발행 2025-01)
- [ref-561](../../references/ref-561.md) — 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 (발행 2024-11-03)
- [ref-1118](../../references/ref-1118.md) — 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (발행 2023-11-17)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-472](../../references/ref-472.md) — A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available (발행 2023-10)
- [ref-562](../../references/ref-562.md) — 국가법령정보센터(고용노동부), 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) (발행 2023-07-01)
- [ref-555](../../references/ref-555.md) — European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery (발행 2023-06)
- [ref-470](../../references/ref-470.md) — ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems (발행 2023-06)
- 그 밖에 13건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) — seed → draft: 3~11절 첫 작성(표준·인증 개정 현황, 제조 공장·물류창고·실외·가정·기타 사례, 사고 기록·조사 방법, 책임 경계, 연결 17건, 열린 질문 7건). 2차 수정: 7절 머리 문장을 f1·f3 의 구체 사실로 교체, 프런트매터 sources 를 각주 정의와 일치 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 머리 문장을 f1·f3 의 구체 사실로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "4. 핵심 개념과 용어" 절(1,007자)을 옮겼다 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area50-s6.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 역할별 표준 적합성 경로의 브리프 밖 한계 문장을 f16 사실 문장으로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-09-30-area50-s11.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "11. 열린 질문" 절(978자)을 옮겼다 (실행 2026-09-30-15)
<!-- auto:category-recent:end -->
```

### docs/categories/safety/index.md

```markdown
---
title: "M. 안전"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › M. 안전

# M. 안전

## 핵심 질문

여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

## 개요

위험성 평가, 안전 기능과 정지·재개, 사람 근접 안전, 비상 대응, 안전 표준·인증, 사고 조사. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **48. 안전·위험 관리** | 위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? | [48. 안전·위험 관리](safety-and-risk-management.md) | published |
| **49. 사람 근접 안전** | 사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 | 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? | [49. 사람 근접 안전](human-proximity-safety.md) | published |
| **50. 안전 표준·인증·사고 조사** | 안전 표준 적합성·인증, 사고 기록과 사후 조사 | 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? | [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

여러 장비가 각각 안전해도 함께 움직일 때 새로운 위험이 생길 수 있다. **로봇·사람·설비의 상호작용 전체**를 위험성 평가의 대상으로 삼아야 한다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 49건이다(논문 15건 · 기사·보고서 10건 · 업체 발표 1건 · 표준·오픈소스·기관 자료 23건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1085](../../references/ref-1085.md) — Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters (발행 2026-04-15)
- [ref-417](../../references/ref-417.md) — Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems (발행 2026-04)
- [ref-1076](../../references/ref-1076.md) — Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 (발행 2026-02-19)
- [ref-1083](../../references/ref-1083.md) — Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments (발행 2025-08-27)
- [ref-1082](../../references/ref-1082.md) — Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario (발행 2025-03-27)
- [ref-563](../../references/ref-563.md) — Belzile, B. 외, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment (발행 2025-02)
- [ref-1081](../../references/ref-1081.md) — Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments (발행 2024-08-07)
- [ref-1122](../../references/ref-1122.md) — Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports (발행 2024)
- [ref-1079](../../references/ref-1079.md) — Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms (발행 2023-06-29)
- [ref-565](../../references/ref-565.md) — Reliability Engineering & System Safety (저자 미확인), Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN (발행 2023)
- 그 밖에 5건

**기사·보고서**

- [ref-1125](../../references/ref-1125.md) — 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 (발행 2026-09-29)
- [ref-1116](../../references/ref-1116.md) — IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2 (발행 2026-09-18)
- [ref-791](../../references/ref-791.md) — Intertek, Machines Got Smarter, Now ISO 12100 has to Catch Up (발행 2025-12-11)
- [ref-1115](../../references/ref-1115.md) — The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul (발행 2025-02)
- [ref-1078](../../references/ref-1078.md) — 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠" (발행 2024-03-09)
- [ref-1124](../../references/ref-1124.md) — 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 (발행 2023-11-08)
- [ref-1084](../../references/ref-1084.md) — The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2 (발행 2023-10-26)
- [ref-992](../../references/ref-992.md) — 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (발행 2023-07-28)
- [ref-1123](../../references/ref-1123.md) — 서울신문, [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인) (발행 2017-04-07)
- [ref-471](../../references/ref-471.md) — A3(Association for Advancing Automation), Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) (발행 미확인)

**업체 발표**

- [ref-1080](../../references/ref-1080.md) — Amazon, Ever wonder how people and robots team up on your Amazon order? (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-567](../../references/ref-567.md) — Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf (발행 2025-04-04)
- [ref-560](../../references/ref-560.md) — ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells (발행 2025-02)
- [ref-790](../../references/ref-790.md) — DIN Media, DIN EN ISO 12100 - 2025-01 (Draft standard) (발행 2025-01)
- [ref-561](../../references/ref-561.md) — 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 (발행 2024-11-03)
- [ref-1118](../../references/ref-1118.md) — 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (발행 2023-11-17)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-472](../../references/ref-472.md) — A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available (발행 2023-10)
- [ref-562](../../references/ref-562.md) — 국가법령정보센터(고용노동부), 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) (발행 2023-07-01)
- [ref-555](../../references/ref-555.md) — European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery (발행 2023-06)
- [ref-470](../../references/ref-470.md) — ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems (발행 2023-06)
- 그 밖에 13건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) — seed → draft: 3~11절 첫 작성(표준·인증 개정 현황, 제조 공장·물류창고·실외·가정·기타 사례, 사고 기록·조사 방법, 책임 경계, 연결 17건, 열린 질문 7건). 2차 수정: 7절 머리 문장을 f1·f3 의 구체 사실로 교체, 프런트매터 sources 를 각주 정의와 일치 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 머리 문장을 f1·f3 의 구체 사실로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "4. 핵심 개념과 용어" 절(1,007자)을 옮겼다 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area50-s6.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 역할별 표준 적합성 경로의 브리프 밖 한계 문장을 f16 사실 문장으로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-09-30-area50-s11.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "11. 열린 질문" 절(978자)을 옮겼다 (실행 2026-09-30-15)
<!-- auto:category-recent:end -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 43건 / 전체 1262건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | https://arxiv.org/abs/2604.05427 | 2026-09-25 | 아니오 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | https://www.iso.org/standard/83545.html | 2026-09-25 | 아니오 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs) | 미확인 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 2026-09-25 | 아니오 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 2026-09-25 | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 2026-09-25 | 아니오 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | https://www.iso.org/standard/73934.html | 2026-09-25 | 아니오 |
| ref-561 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 2026-09-25 | 아니오 |
| ref-562 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 2026-09-25 | 아니오 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | https://arxiv.org/abs/2502.20693 | 2026-09-25 | 아니오 |
| ref-564 | Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회) | 2018-12 | https://ieeexplore.ieee.org/document/8910126/ | 2026-09-25 | 아니오 |
| ref-565 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 2026-09-25 | 아니오 |
| ref-566 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 2026-09-25 | 아니오 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | https://github.com/open-rmf/rmf/issues/658 | 2026-09-25 | 아니오 |
| ref-783 | ISO | ISO/AWI 15066-1 - Collaborative Safety – Physical contact with robots — Part 1: Biomechanical thresholds and data | 미확인 | https://www.iso.org/standard/91522.html | 2026-09-26 | 아니오 |
| ref-790 | DIN Media | DIN EN ISO 12100 - 2025-01 (Draft standard) | 2025-01 | https://www.dinmedia.de/en/draft-standard/din-en-iso-12100/386233502 | 2026-09-26 | 아니오 |
| ref-791 | Intertek | Machines Got Smarter, Now ISO 12100 has to Catch Up | 2025-12-11 | https://www.intertek.com/blog/2025/12-11-machines-and-iso-12100/ | 2026-09-26 | 아니오 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 2026-09-29 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 2026-09-30 | 예 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 2026-09-30 | 예 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | https://zdnet.co.kr/view/?no=20230728173101 | 2026-09-30 | 예 |
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 2026-09-30 | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | https://arxiv.org/abs/2602.17822 | 2026-09-30 | 예 |
| ref-1077 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md | 2026-09-30 | 예 |
| ref-1078 | 지디넷코리아 | "협동로봇 충돌 안전 계산하고 써야죠" | 2024-03-09 | https://zdnet.co.kr/view/?no=20240305160245 | 2026-09-30 | 예 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | https://arxiv.org/abs/2306.16740 | 2026-09-30 | 예 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 2026-09-30 | 예 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 2026-09-30 | 예 |
| ref-1082 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | https://arxiv.org/abs/2503.21141 | 2026-09-30 | 예 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | https://arxiv.org/abs/2508.19731 | 2026-09-30 | 예 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 2026-09-30 | 예 |
| ref-1085 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | https://arxiv.org/abs/2604.13677 | 2026-09-30 | 예 |
| ref-1115 | The Robot Report | ISO 10218 industrial robot safety standard receives major overhaul | 2025-02 | https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/ | 2026-09-30 | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 2026-09-30 | 예 |
| ref-1117 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | https://iss.rs/en/project/show/iso:proj:83498 | 2026-09-30 | 예 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 2026-09-30 | 예 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | https://arxiv.org/abs/2205.06564 | 2026-09-30 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 2026-09-30 | 예 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 2026-09-30 | 예 |
| ref-1123 | 서울신문 | [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인) | 2017-04-07 | https://www.seoul.co.kr/news/society/2017/04/07/20170407011011 | 2026-09-30 | 예 |
| ref-1124 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | https://www.khan.co.kr/article/202311081103001 | 2026-09-30 | 예 |
| ref-1125 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 358개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
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
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
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
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
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
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
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
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [48, 49, 50] 에 걸린 29건 / 전체 309건)

```markdown
- oq-064 [열림] 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? (영역 30, 48)
- oq-070 [열림] 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? (영역 31, 48)
- oq-092 [열림] 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? (영역 48, 57)
- oq-093 [열림] EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? (영역 48, 57)
- oq-095 [열림] ROP 가 VDA 5050 의 원격(REMOTE) 비상정지나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? (영역 29, 48)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 21, 48)
- oq-097 [열림] 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? (영역 31, 48)
- oq-102 [열림] ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? (영역 48, 51)
- oq-103 [열림] EU 기계 규정 부속서 III 1.1.9 의 적용일이 사이버 복원력법(2027-12-11)에 맞춰 연기되는지 확정됐는가? (영역 48, 51)
- oq-106 [열림] LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? (영역 47, 48)
- oq-123 [열림] ISO 10218-2:2025 발행 뒤 국내 KS B ISO 10218-2 와 KS B ISO/TS 15066 은 새 판으로 부합 개정되었거나 개정 예고되었는가, 국내 협동로봇 설치 작업장 안전인증은 어느 판을 기준으로 하는가? (관련 기존 질문: oq-070, oq-092) (영역 31, 48)
- oq-144 [열림] 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? (영역 13, 52, 48)
- oq-170 [열림] ISO 3691-4:2023 의 운용 구역 분류와 사람 감지 요구가 이기종 플릿 관제 계층에 어떤 정보(구역·속도 제한·모드)를 요구하는지 표준 원문으로 확인할 수 있는가(이번 조사는 인증 기관 설명만 확인했다)? (영역 62, 50)
- oq-172 [열림] 격리 병동·감염 관리 구역을 지나는 이송 로봇의 출입 허용 규칙과 로봇 표면 소독 절차를 병원 감염관리 조직이 어떻게 정하고 로봇 플릿 관제가 이를 경로·배정 제약으로 어떻게 받는지 공개된 지침이나 연구가 있는가? (영역 63, 48)
- oq-186 [열림] 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? (영역 66, 50, 59)
- oq-229 [열림] 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? (영역 49, 48)
- oq-230 [열림] 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (영역 49, 50)
- oq-231 [열림] 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (영역 49, 59)
- oq-232 [열림] 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (영역 49, 21)
- oq-251 [열림] 국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가? (영역 50, 62)
- oq-252 [열림] 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? (영역 50, 37, 38)
- oq-253 [열림] 2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가? (영역 50, 48)
- oq-254 [열림] ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가? (영역 50, 64, 63)
- oq-265 [열림] ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? (영역 40, 50, 58)
- oq-275 [열림] 서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가? (영역 56, 59, 50)
- oq-282 [열림] 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? (영역 58, 59, 48)
- oq-302 [열림] RoboGuard 처럼 안전 규칙을 시간 논리 제약으로 바꿔 언어 모델 계획을 고치는 안전 가드레일을 다중 로봇 오케스트레이션의 승인 전 검사에 두면 사람 승인 부담을 얼마나 줄일 수 있으며, 가드레일이 계획을 수정했을 때 무엇을 사람에게 다시 승인받아야 하는가? (영역 12, 48, 13)
- oq-307 [열림] 사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? (영역 48, 34, 19)
- oq-309 [열림] 이동로봇 안전 표준(ISO 3691-4 등)이나 국내 인증 기관이 시뮬레이션·가상 시운전 결과를 안전 확인 근거로 인정하는 조건과 절차가 있는가? (영역 50, 36, 54)
```
