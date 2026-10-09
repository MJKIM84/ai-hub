(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-04
- date: 2026-10-09
- run_type: category_link (대분류 연결)
- 대상: 대분류 I. 설계·시뮬레이션 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
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

### runs/2026-10-09-04/target.json

```json
{
  "run_id": "2026-10-09-04",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 137,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "I. 설계·시뮬레이션",
    "category_letter": "I"
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

### runs/2026-10-09-04/research.json

```json
{
  "run_id": "2026-10-09-04",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "I. 설계·시뮬레이션"
  },
  "gaps": [
    "I. 설계·시뮬레이션 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다",
    "게시된 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 35. 처리능력·규모·배치 설계, 36. 가상 시운전·실제 상황 재현 페이지에는 영역 단위 연결(10절)만 있고, 대분류 단위로 묶은 연결은 없다",
    "34. 시뮬레이션·예측용 디지털 트윈과 35. 처리능력·규모·배치 설계 페이지는 이전 분류(2026-09-25) 기준으로 쓰여 C. 채팅 기반 구성·운영, L. AI·학습 기술, M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회와 잇는 근거가 없다",
    "H. 실행·협업·예외 복구(32 제외), J. 현장 운영·관제의 40. 운영 절차·요청 창구, K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API, N. 보안·개인정보의 53. 개인정보·영상 데이터와의 연결 근거가 게시 페이지에 없다"
  ],
  "research_questions": [
    "현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]",
    "I. 설계·시뮬레이션의 네 세부영역은 C. 채팅 기반 구성·운영(9. 채팅으로 시나리오 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현)과 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획, 47. AI·학습·적응과 모델 운영)에서 무엇을 받고 무엇을 넘기는가?",
    "34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현은 F. 연동(20·21·22·23)의 어떤 인터페이스를 가상으로 대신해 시험하며, O. 검증·도입·수명주기(54·55)와 B. 로봇 온톨로지(4·7)로 무엇을 넘기는가?",
    "35. 처리능력·규모·배치 설계와 34. 시뮬레이션·예측용 디지털 트윈의 결과는 G. 계획·최적화(25. 작업 배정 — MRTA ~ 28. 공용 자원·충전·에너지 최적화)의 결정과 어떻게 맞물리는가?",
    "36. 가상 시운전·실제 상황 재현은 E. 사물·사람·실시간 상태(18·19)와 J. 현장 운영·관제(37·38)의 상태·기록을 어떻게 원천으로 쓰며, 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 34. 시뮬레이션·예측용 디지털 트윈의 미래 실험을 어떻게 구분하는가?",
    "시뮬레이션·디지털 트윈은 M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회, A. 기획·사업, Q. 현장 유형별 적용과 어디서 만나는가(한국 자료 포함)?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "C. 채팅 기반 구성·운영의 9. 채팅으로 시나리오 구성 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Chat2Scenic(2026-07)은 챗봇 인터페이스로 시나리오를 대화로 다듬으면서 검색 증강 방식으로 도메인 특화 언어(DSL) 시나리오 스크립트를 만들고, 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%(비교 방법 30.08%·16.26%)를 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1329"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: \"Chat2Scenic provides a chatbot interface that supports interactive scenario refinement.\" 규제 문서 기반 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%, 비교 방법 30.08%·16.26%. 대상은 자율주행 시나리오이며 로봇 현장이 아니다.",
      "as_of": "2026-07-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "C. 채팅 기반 구성·운영의 9. 채팅으로 시나리오 구성·13. 대화형 기능의 신뢰·기반 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 대화로 만든 시나리오의 출력 형식은 33. 시나리오 모델·편집이 정하는 매개변수화·장애 선언 형식이 되고, 생성 스크립트가 컴파일되지 않는 경우가 남으므로 승인 전 형식 검사가 두 대분류의 인계 지점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1329",
        "ref-1088",
        "ref-528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1 의 컴파일 성공률 76.42% 는 생성 스크립트 약 4분의 1이 실행 불가였음을 뜻한다. OpenSCENARIO 는 정적·동적 분리와 매개변수화, ARIAC 는 장애를 매개변수로 선언한다(재인용: 2026-09-30-12). 로봇 시나리오에 적용한 사례는 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f3",
      "claim": "C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Xia 외(2026-08, ETFA 2026 채택)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1330"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: 질의·기준 구성 구조화 → 실험 설계 → 비교 시뮬레이션 실행 → 결과 해석 → 권고. 산업 환경에서 언어만 쓴 추론보다 구체적이고 사용자 평가가 높았다고 보고. 대상은 제약 공정 시뮬레이션이며 로봇 플릿이 아니다.",
      "as_of": "2026-08-22",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 대화로 조건을 바꿔 비교하는 일은 언어 모델이 34쪽 시뮬레이션 실험을 설계·실행하는 구조로 이어질 것으로 보이나, 비교 결과를 믿으려면 36쪽 재현 충실도 지표가 함께 필요하고 로봇 플릿에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1330",
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3 은 공정 시뮬레이션 대상. Kadian 외는 시뮬레이션 성과 차이가 실제로 이어지지 않을 수 있음을 상관계수로 보였다(f31). 두 연구 모두 로봇 플릿 오케스트레이션 대상이 아니다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Holodeck(CVPR 2024)은 GPT-4가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성하며, 생성 장면에서 학습한 에이전트가 처음 보는 환경에서 주행했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-815"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: 텍스트 프롬프트로 3D 환경 자동 생성, GPT-4 가 상식 지식과 공간 관계 제약을 제공하고 배치를 최적화, Objaverse 객체 사용, 생성 장면에서 학습한 에이전트가 음악실·어린이집 같은 새 환경을 주행.",
      "as_of": "2023-12-14",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 언어 모델·생성 모델로 시뮬레이션 환경을 만드는 연구(Holodeck, Arena 4.0)가 33의 예제 라이브러리를 채우는 수단이 될 수 있으나, 생성 환경은 실제 현장 지도가 아니므로 D. 공간·지도 모델의 도면·현장 정합과 구분해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-815",
        "ref-1089"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Holodeck 은 글 지시로 장면을, Arena 4.0 은 생성 모델로 사람 중심 주행 시험 환경을 만든다(재인용: 2026-09-30-12). 실제 현장과의 일치는 두 연구의 목표가 아니다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f7",
      "claim": "E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 제조 분야 분류 자료가 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분하므로, 18은 현장 상태를 가상 모델에 반영하는 현재 상태 표현을, 34는 그 모델을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-291"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Kritzinger 외(2018)의 분류는 물리–가상 데이터 흐름이 수동/한 방향 자동/양방향 자동인지로 세 개념을 나눈다(재인용: B. 로봇 온톨로지 대분류 페이지). 근거가 제조 대상이라는 한계가 있다.",
      "as_of": "2018",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "F. 연동의 22. 설비·건물 시스템 연동 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션은 문·승강기 플러그인이 실제와 같은 문·승강기 요청에 응답하고, door_supervisor 가 충돌을 막고 lift_supervisor 가 여러 플릿의 승강기 요청을 관리하며, TeleportDispenser·TeleportIngestor 가 배송 작업의 적재·하역을 흉내 낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md 원문 요약: 승강기 칸 문은 이동 전에 닫히고 목적층에서만 열린다. 향후 실제 워크셀·로봇팔도 같은 메시지 교환을 쓸 것이라고 적는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "F. 연동의 20. 로봇·제조사 관제 연동 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 의 slotcar 플러그인은 플릿 어댑터의 경로·모드 요청을 받아 로봇 상태를 발행하는 전체 제어 로봇 모델로, 경유점 사이를 레일식 직선으로 움직이고 막히면 멈추며 로봇마다 주행 스택 전체를 돌리는 계산 비용을 피한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md 원문: slotcar 는 \"full control\" 로봇 플러그인, 2륜 차동 구동과 정적 장애물 없는 경로를 가정한다. 로컬 회피·센서 인식 같은 로봇 자체 거동은 연계 대상으로 남는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크·55. 현장 조사·설치·시운전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Open-RMF 문서는 시뮬레이션이 하드웨어 시험의 준비·정지·초기화 부담을 덜고, 시나리오를 반복해 수정을 확인하고 드문 예외를 살피며, 장시간 시뮬레이션으로 배치 전에 시설 소유자의 확신을 높인다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md 원문 요약: 시뮬레이션의 로봇은 배터리가 닳지 않고 충돌해도 비용이 없으며, 반복 가능한 시나리오로 수정 사항을 확인할 수 있다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 설비 제어 분야의 가상 시운전 정의(VDI/VDE 3693)와 실제 제어기·가상화 인스턴스를 섞은 분산 가상 시운전 연구가 있어 36의 결과가 55의 현장 시운전 준비로 넘어갈 것으로 보이나, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차는 확인하지 못했다(oq-255).",
      "tag": "추정",
      "source_ids": [
        "ref-1126",
        "ref-1130",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDI/VDE 3693 Blatt 1(2025-05)은 가상 시운전 모델 유형·용어를 정의하고, Rosenberger 외(2023)는 실제 제어기 3대와 가상화 인스턴스 9대로 팔레타이징 설비를 시험했다(재인용: 2026-09-30-17).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f12",
      "claim": "G. 계획·최적화의 25. 작업 배정 — MRTA ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: VirTooS(2026-08)는 ROS 2와 Unity 게임 엔진을 결합한 혼합 현실 환경에서 실제·가상 로봇과 실제·가상 센서를 함께 써서 자율이동로봇 팀의 플릿 관리 작업을 시험하는 도구이며, 작업 배정 예제에서 실제 로봇과 가상 로봇이 상호작용한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1129"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: 가상 시나리오 생성·사용자화, 실제·가상 LiDAR 로 혼합 현실 환경 지도 작성·주행, 작업 배정 실험이 동기 예제, ChoiRbot 기반 분산 실험 루틴과 여러 머신 배포용 컨테이너 묶음 제공.",
      "as_of": "2026-08-26",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 가상 시운전 도구가 여러 머신에 컨테이너로 배포되고 시뮬레이션 플러그인이 실제와 같은 요청 메시지에 응답하므로, 가상 대응물을 어느 계산 자원에 두고 실제 시스템과 어떤 통신으로 잇는지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1129",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VirTooS 의 컨테이너 배포·분산 실험 루틴(f12)과 Open-RMF 시뮬레이션 플러그인의 요청 응답 구조(f8·f9). 로봇 플릿 플랫폼의 현장 서버·클라우드 배치 근거는 없다(oq-040).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 한 유통사 물류센터 시뮬레이션 연구(2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼고, 로봇 이동형 풀필먼트 시스템의 충전·배터리 교환 전략 비교(2018)와 창고 충전소 배치 최적화(2024) 연구도 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-102",
        "ref-098",
        "ref-109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "35. 처리능력·규모·배치 설계 페이지 3·10절의 검증된 주장(재인용: 2026-09-25-10). 세 출처는 각각 다른 내용을 말하며 교차 확인 관계가 아니다.",
      "as_of": "2025",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "G. 계획·최적화의 25. 작업 배정 — MRTA ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: Open-RMF 플릿 어댑터 템플릿 설정에서는 배터리가 recharge_threshold 아래인 로봇이 작업을 맡지 않으므로, 충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어진다.",
      "tag": "사실",
      "source_ids": [
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 의 recharge_threshold(예시값 0.10), recharge_soc, 로봇별 충전기, 작업 종료 후 동작 설정(재인용: 2026-09-25-10). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f16",
      "claim": "G. 계획·최적화의 26. 작업 순서·스케줄링 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정한 Boysen 외(2017)는 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다(저자 계산 실험 조건).",
      "tag": "사실",
      "source_ids": [
        "ref-381"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "G. 계획·최적화 대분류 페이지의 검증된 주장(재인용: 2026-09-25-55). 독립 재현은 확인되지 않았고 물류창고 피킹 작업대 조건이다(oq-050).",
      "as_of": "2017",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "G. 계획·최적화의 25. 작업 배정 — MRTA ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 로봇 이동형 풀필먼트 시스템의 여러 결정 문제를 연구하는 이산 사건 시뮬레이션이며, Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다.",
      "tag": "사실",
      "source_ids": [
        "ref-101",
        "ref-398"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "34. 시뮬레이션·예측용 디지털 트윈 페이지 5절과 G. 계획·최적화 대분류 페이지의 검증된 주장(재인용: 2026-09-25-56). 물류창고 피킹 단계의 시뮬레이션 결과이며 현장 실측이 아니다.",
      "as_of": "2019",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있어 경로망 배치 평가가 가정한 미래를 실험하는 쪽에 걸친다.",
      "tag": "사실",
      "source_ids": [
        "ref-267"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "34. 시뮬레이션·예측용 디지털 트윈 페이지 5절 '경로망 배치도 시뮬레이션으로 설계하는 연구가 있다'(재인용: 2026-09-25-56).",
      "as_of": "2024",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Moving AI Lab 의 MAPF 벤치마크는 지도와 시나리오 파일을 묶어 공개해 경로 계획기를 같은 조건에서 비교하게 하므로, 경로 계획 평가가 시나리오 형식·라이브러리와 맞닿는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1091"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "33. 시나리오 모델·편집 페이지 3·5·7절이 경로 찾기 벤치마크의 시나리오 파일을 형식 사례로 다룬다(재인용: 2026-09-30-12). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 63. 병원·의료 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계·36. 가상 시운전·실제 상황 재현: 고려대학교 구로병원의 약품 배송 로봇 기록(2025-06, 122건)과 몬테카를로 재현에서 승강기 가동률 59.01% 이하일 때 배송 성공률 95.5%, 90% 초과에서 실패가 몰렸다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36. 가상 시운전·실제 상황 재현 페이지 5절 병원 사례(재인용: 2026-09-30-17). 주된 실패는 승객·화물이 로봇의 승강기 진입을 막는 경우. 승강기 제어 자체는 원문 19장 시설·설비 제어 경계의 연계 대상.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 64. 상업 시설 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 다층 호텔의 배송 로봇 경로 계획 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "35. 처리능력·규모·배치 설계 페이지 9절의 검증된 주장(재인용: 2026-09-25-10). 35는 승강기 시간을 제약 입력으로만 받고, 승강기 제어는 22쪽 연계 대상이다.",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "G. 계획·최적화의 25. 작업 배정 — MRTA·Q. 현장 유형별 적용의 63. 병원·의료 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Lee 외 저자들은 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰고, 병원별 구조·통행·승강기 제어 정책을 재현한 병원 디지털 트윈으로 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다.",
      "tag": "의견",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36. 가상 시운전·실제 상황 재현 페이지 5절의 [의견] 문장 두 개(재인용: 2026-09-30-17). 다른 병원에서 검증한 연구는 미확인(oq-258).",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: NIST ARIAC 는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급 주문을 매개변수로 선언해 시각이나 발생 횟수 조건으로 시나리오에 주입한다.",
      "tag": "사실",
      "source_ids": [
        "ref-528"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "33. 시나리오 모델·편집 페이지 5절 제조 공장 사례(경진대회 시나리오, 재인용: 2026-09-30-12). 여러 제조사 플릿·승강기·문 장애로 일반화한 형식은 미확인(oq-235). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f24",
      "claim": "G. 계획·최적화의 24. 작업·워크플로 모델링 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 로봇 미션 명세·실행 형식 비교 연구와 행동 트리 편집기(Groot2)가 33의 미션 기술 형식·편집기 선택 근거로 쓰였으므로, 시나리오 안의 작업 표현은 24의 단계·선후관계·완료 조건 표현과 같은 형식을 공유해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-116",
        "ref-1090"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "33. 시나리오 모델·편집 페이지 6·9절이 미션 기술 형식과 편집기를 직접 범위로 둔다(재인용: 2026-09-30-12). 두 영역의 형식을 하나로 맞춘 공개 사례는 확인하지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 의 building_map_generator 는 traffic-editor 로 주석한 건물 파일에서 층별 바닥·벽 메시와 문·승강기·로봇을 담은 시뮬레이션 월드를 만들고, 환경을 바꿀 때는 주석만 고쳐 다시 생성하면 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-406",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md 원문 요약: .building.yaml 을 읽어 .world 파일 생성, 기본 월드에는 센서가 없어 템플릿으로 카메라·LiDAR 추가. traffic-editor 는 차선·문·승강기·충전기를 주석한다(재인용: 2026-09-30-12). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f26",
      "claim": "B. 로봇 온톨로지의 4. 이기종 로봇 등록 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: 시나리오가 참조하는 로봇 모델은 SDFormat 같은 로봇·환경 기술 형식으로 시뮬레이터에 들어가므로, 4의 기종 제원 기술(형상·질량·센서 등)이 시뮬레이션 자산의 원천으로 이어질 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1092"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "33. 시나리오 모델·편집 페이지 9절: 로봇 기구학·동역학·센서 모델(SDFormat 로봇 기술)은 연계 대상, ROP 는 참조로 묶는다(재인용: 2026-09-30-12). 등록 정보와 시뮬레이션 모델을 잇는 사례는 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: rosbag2 는 ROS 2 통신을 시각이 찍힌 백 파일(기본 MCAP)로 기록하고, 재생 속도 조절·/clock 발행·시작 시각 지정·토픽 선택·여러 백 파일의 기록 시각순 동시 재생을 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 원문: rosbag2 는 \"the tool for recording and playback of communications in ROS 2 systems\". 크기·기간 분할, zstd 압축, 메모리 버퍼 스냅샷 모드도 있다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 메시지 단위 기록 도구와 기록 기반 시뮬레이터가 있으나, 재현의 원천은 37이 남기는 오케스트레이션 수준 실행 기록(작업·배정·위치·사건 시각)이어야 할 것으로 보이며 이를 시나리오 사양으로 바꾸는 공개 형식은 확인하지 못했다(oq-131).",
      "tag": "추정",
      "source_ids": [
        "ref-831",
        "ref-1128"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "rosbag2 는 토픽 메시지를 기록·재생하고(f27), Waymax 는 실제 주행 기록으로 시뮬레이션을 초기화·재생한다(f29). 둘 다 로봇 플릿 오케스트레이션 기록 형식을 정하지 않는다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Waymax(2023)는 실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화하거나 재생하고, 사실적 상호작용을 위해 학습된 행동 모델과 규칙 기반 행동 모델을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1128"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: Waymo Open Motion Dataset 같은 실제 주행 기록 사용, \"learned and hard-coded behavior models\", TPU/GPU 가속기에서 그래프 안 시뮬레이션. 자율주행 차량 대상이며 로봇 현장 사례가 아니다.",
      "as_of": "2023-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "E. 사물·사람·실시간 상태의 19. 사람·보행자 모델·M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 공항 터미널 예제 월드가 이를 군중 시뮬레이션으로 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-406",
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation.md 원문 요약: crowdsim 은 menge 로 에이전트 제어, 공항 예제는 use_crowdsim:=1 로 실행. rmf_demos README 도 공항 월드의 선택적 군중 시뮬레이션을 적는다(같은 기관이라 독립 교차 확인 아님). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f31",
      "claim": "O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Kadian 외(RA-L 2020)는 시뮬레이션–현실 상관 계수(SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 Habitat 기본 설정의 성공률 SRCC 가 0.18 이었으나 시뮬레이션 매개변수를 조정해 0.844 로 높였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: 실험실을 3D 스캔한 가상 복제에서 모델 9개를 시뮬레이션·실기 양쪽으로 시험, 에이전트가 시뮬레이터의 충돌 동역학을 악용해 벽을 미끄러져 지나갔다.",
      "as_of": "2020-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "L. AI·학습 기술의 47. AI·학습·적응과 모델 운영 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 학습 정책이 시뮬레이터의 결함을 악용하는 현실 격차가 보고되므로, 학습 기반 정책의 현실 격차 보정은 47쪽(및 로봇 제조사·시뮬레이션 도구) 일이고 36은 재현 결과와 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-741",
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "36. 가상 시운전·실제 상황 재현 페이지 9절은 현실 격차 보정을 연계 대상, 차이 지표 관리를 직접 범위로 둔다(재인용: 2026-09-30-17). f31 의 충돌 동역학 악용 사례.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f33",
      "claim": "O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: NASA-STD-7009B(2024-03-05)는 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1133"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36. 가상 시운전·실제 상황 재현 페이지 7절 '모델·시뮬레이션 결과의 수용은 NASA-STD-7009B 가 다루며'(재인용: 2026-09-30-17).",
      "as_of": "2024-03-05",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f34",
      "claim": "B. 로봇 온톨로지의 7. 온톨로지 검증·변경 관리 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 7이 능력 정의에 붙이는 지원 단계(시뮬레이션 연결·시뮬레이션 검증·실기 검증)를 판정하려면 36의 시뮬레이션 신뢰도 평가와 시뮬레이션–현실 상관 지표가 기준이 될 수 있으나, 두 체계를 대응시킨 자료는 확인하지 못했다(oq-156).",
      "tag": "추정",
      "source_ids": [
        "ref-1133",
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "NASA-STD-7009B 의 신뢰도 평가(f33)와 SRCC(f31)는 로봇 능력 온톨로지의 검증 단계를 정의하지 않는다. 대응 체계는 ROP 가 자체 정의해야 할 수 있다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f35",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 생성해, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1331"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: 복잡한 로봇 시스템의 위험은 초기 설계 단계에서 숨어 있기 쉽고, 무작위·몬테카를로 탐색은 탐색 공간이 커서 비실용적이라고 본다. 산업용 로봇 셀 적용 예 하나의 개념 증명.",
      "as_of": "2020-11-20",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f36",
      "claim": "M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 위험 상황을 생성·탐색하는 시뮬레이션 시험(사람 행동 최적화, 확률적 시나리오 언어 기반 반증)이 있으므로, 33에서 선언한 장애·사람 흐름 시나리오가 48의 위험 식별 입력이 될 수 있을 것으로 보이나 다중 이동로봇 플릿에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1331",
        "ref-1086"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Huck 외는 산업용 로봇 셀(f35), Scenic 3.0 은 3D 환경 모델링 기반 반증 시험(재인용: 2026-09-30-12)을 다룬다. 설비 안전 제어와 안전 인증 판단 자체는 연계 대상.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f37",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Carr 외(2022)는 물리 로봇과 동기화된 ROS 기반 로봇의 디지털 트윈에 중간자 공격을 가하면 그 영향이 물리 시스템으로 전파될 수 있으며 산업용 로봇과 자율이동로봇 모두에 해당한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1332"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 요약: 동기화된 디지털 트윈이 공격 표면이 되어 물리 시스템을 붕괴시킬 수 있다고 주장하고 완화 방안을 논의한다(구체 방안은 초록에 없음).",
      "as_of": "2022-11-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 36이 다루는 디지털 트윈 동기화(실시간 상태를 가상 모델에 반영하고 결과를 되돌리는 경로)는 공격 표면이 될 수 있으므로, 시뮬레이션 결과가 실제 계획·설정에 반영되는 경로에 접근통제와 무결성 확인이 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1332"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f37 의 중간자 공격 전파. 로봇 플릿 오케스트레이션 플랫폼의 디지털 트윈 보안 사례는 이번 조사에서 찾지 못했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 모델 라이선스를 지정하고 CC BY 3.0 Unported 를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1239"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "59. 법·규제·보험·라이선스 브리프 f20(재인용: 2026-09-30-23). 34가 다루는 시뮬레이션 자산(3D 모델)의 출처·라이선스 관리와 맞닿는다. 자산 단위 추적 표준은 미확인(oq-292). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "F. 연동의 21. 상호운용 표준·적합성 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 들어와 있고 2026년 디지털 트윈 결합을 다루는 제6부가 발행되었으나, 물류센터 이종 로봇·설비에 그대로 쓸 수 있는지는 확인되지 않았다(oq-085).",
      "tag": "사실",
      "source_ids": [
        "ref-516",
        "ref-518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "34. 시뮬레이션·예측용 디지털 트윈 페이지 7·11절(재인용: 2026-09-25-56). 두 출처는 각각 다른 부(제1부, 제6부)를 가리킨다.",
      "as_of": "2026",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "연계 대상: F. 연동의 23. 업무 시스템 연동 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 성수기 주문·물동량 전망 같은 시나리오 입력은 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 물류·공급망 디지털 트윈 검토는 실제 데이터로 검증한 연구가 소수라고 보고한다.",
      "tag": "추정",
      "source_ids": [
        "ref-521"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "34. 시뮬레이션·예측용 디지털 트윈 페이지 5·9절(재인용: 2026-09-25-56). 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역이다.",
      "as_of": "2024",
      "site_type": "물류창고",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 국내 인증 모델(2023)은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야 28개 항목(총점 176점)으로 구성된다.",
      "tag": "사실",
      "source_ids": [
        "ref-409"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 연동 대분류 페이지의 검증된 주장(재인용: 2026-09-25 F 대분류 연결). 35가 다루는 로봇 친화 공간 설계·개조의 평가 틀이 될 수 있다. 대상은 공동주택이다.",
      "as_of": "2023",
      "site_type": "가정",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 충전 방식의 비용 비교와 국내 스마트물류센터 인증 평가에서 두 영역이 만나는 것으로 보이나, 인증 세부 지표에 로봇 대수·가동률 같은 설비 계획 지표가 들어가는지는 확인하지 못했다(oq-011).",
      "tag": "추정",
      "source_ids": [
        "ref-098",
        "ref-106"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "35. 처리능력·규모·배치 설계 페이지 10절(재인용: 2026-09-25-10). 인증 제도는 한국교통연구원 인증스마트물류센터 사이트 기준.",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "A. 기획·사업의 3. 경제성·조달·사업 모델 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Rockwell Automation 사례 소개는 미국 남부 물류센터 구축에서 통합자가 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증해 전체 프로젝트 기간을 18% 줄이고 현장 시운전을 5주 단축했다고 밝히지만 기준선과 측정 방법은 공개하지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 36. 가상 시운전·실제 상황 재현 페이지 5절 물류창고 사례(재인용: 2026-09-30-17). 독립 연구로 같은 기준선에서 측정한 결과는 미확인(oq-257).",
      "as_of": "2024-08-28",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f45",
      "claim": "Q. 현장 유형별 적용의 62. 제조 공장 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 최성욱·박상철·왕지남(2008)은 자동차 차체 생산라인의 PLC 코드 검증을 위해 실제 PLC 와 3D 가상 공정 시뮬레이터를 양방향 통신으로 잇는 가상 플랜트 구축 절차를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36. 가상 시운전·실제 상황 재현 페이지 5절(재인용: 2026-09-30-17). PLC 코드 가상 시운전은 원문 19장 시설·설비 제어 경계의 연계 대상이며 ROP 에는 방법 근거로만 쓴다.",
      "as_of": "2008-11",
      "site_type": "제조 공장",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f46",
      "claim": "Q. 현장 유형별 적용의 64. 상업 시설 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Open-RMF 예제 호텔 월드는 로봇 플릿 3개(로봇 4대)·승강기 2대·여러 문을 담고, 공항 터미널 월드는 대형 지도에 선택적 군중 시뮬레이션과 읽기 전용 카트를 더해 순찰·배송·청소를 실행하는 시뮬레이션 예제다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "33. 시나리오 모델·편집 페이지 5절 상업 시설 사례(시뮬레이션 예제 월드, 재인용: 2026-09-30-12). 실제 시설 도입 사례가 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f47",
      "claim": "Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: BEHAVIOR-1K 는 설문으로 고른 일상 가정 활동 1,000개를 BDDL 로 명세하고 장면 50개와 주석 객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크다.",
      "tag": "사실",
      "source_ids": [
        "ref-971"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "33. 시나리오 모델·편집 페이지 5절 가정 사례(벤치마크, 재인용: 2026-09-30-12). 장면에는 주택 외 정원·식당·사무실도 있다.",
      "as_of": "2024-03-14",
      "site_type": "가정",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f48",
      "claim": "A. 기획·사업의 1. 기술·시장·업체 동향 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: NVIDIA 는 산업용 로봇 플릿 디지털 트윈을 만드는 'Mega' Omniverse 블루프린트를 발표하며 센서 시뮬레이션·합성 데이터 기반의 배치 전 플릿 검증을 내세운다.",
      "tag": "추정",
      "source_ids": [
        "ref-527"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 34. 시뮬레이션·예측용 디지털 트윈 페이지 9절이 센서 시뮬레이션·합성 데이터를 시뮬레이터 제공자 영역(연계 대상)으로 둔다(재인용: 2026-09-25-56). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f49",
      "claim": "Q. 현장 유형별 적용의 61. 물류창고 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: CJ대한통운은 2021-11 현실 물류센터와 같은 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획을 발표했고 작업 동선·재고 배치·설비 효율 최적화를 목표로 들었으나, 이후 적용 결과는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-526"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 34. 시뮬레이션·예측용 디지털 트윈 페이지 5절(재인용: 2026-09-25-56). 이번 한국어 검색에서도 국내 물류센터 로봇 시운전 전 디지털 트윈 검증 결과를 수치로 공개한 사례는 찾지 못했다(oq-084, oq-117).",
      "as_of": "2021-11",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    }
  ],
  "sources": [
    {
      "id": "ref-1329",
      "org": "Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. (TUM 외, arXiv; IROS 2026 채택으로 검색 결과에 표시)",
      "title": "Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving",
      "published": "2026-07-15",
      "url": "https://arxiv.org/abs/2607.14387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "챗봇 인터페이스로 시나리오를 대화로 다듬고 검색 증강 방식으로 DSL 시나리오 스크립트를 생성하는 틀. 123개 규제 기반 시나리오에서 컴파일 성공률 76.42%를 보고했다(초록 확인). C. 채팅 기반 구성·운영 페이지가 인용한 ref-833 과 같은 논문일 수 있다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2607.14387",
      "source_unopened": false
    },
    {
      "id": "ref-1330",
      "org": "Xia, Y., Weyrich, M., Jazdi, N. 외 (University of Stuttgart·AstraZeneca, arXiv; ETFA 2026 채택)",
      "title": "LLM Agents Perform Controlled Experiments Using Simulation Models",
      "published": "2026-08-22",
      "url": "https://arxiv.org/abs/2608.23622",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "언어 모델 에이전트가 사용자 질의와 기준 구성으로 비교 시뮬레이션을 설계·실행·해석해 제약 공정 매개변수를 권고하는 다중 에이전트 틀(초록 확인). C. 채팅 기반 구성·운영 페이지가 인용한 ref-832 와 같은 논문일 수 있다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2608.23622",
      "source_unopened": false
    },
    {
      "id": "ref-1331",
      "org": "Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020)",
      "title": "Simulation-based Testing for Early Safety-Validation of Robot Systems",
      "published": "2020-11-20",
      "url": "https://arxiv.org/abs/2011.10294",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 모델과 최적화 알고리즘으로 시뮬레이션 안의 고위험 사람 행동을 생성해 초기 설계 단계에서 산업용 로봇 셀의 위험을 드러내는 개념 증명(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2011.10294",
      "source_unopened": false
    },
    {
      "id": "ref-1332",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "물리 로봇과 동기화된 ROS 기반 로봇 디지털 트윈에 대한 중간자 공격이 물리 시스템으로 전파될 수 있음을 다루고 완화 방안을 논의한다(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2211.09507",
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 시뮬레이션의 이점, slotcar 로봇 모델, 문·승강기 플러그인과 감독 노드, 워크셀 순간이동 플러그인, crowdsim, building_map_generator 로 월드 생성을 설명한다. mdBook 원본을 열어 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
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
      "accessed": "2026-10-09",
      "summary": "ROS 2 통신의 기록·재생 도구. 재생 속도·/clock·시작 시각·토픽 선택·여러 백 파일 동시 재생, 기본 저장 형식 MCAP. 공식 저장소 README 원문을 열어 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/rosbag2/rolling/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1128",
      "org": "Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv)",
      "title": "Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research",
      "published": "2023-10-12",
      "url": "https://arxiv.org/abs/2310.08710",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화·재생하고 학습·규칙 기반 행동 모델을 제공하는 가속기 기반 시뮬레이터(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2310.08710",
      "source_unopened": false
    },
    {
      "id": "ref-1129",
      "org": "Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv)",
      "title": "VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots",
      "published": "2026-08-26",
      "url": "https://arxiv.org/abs/2608.26066",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 2 와 Unity 를 결합한 혼합 현실 환경에서 실제·가상 로봇으로 플릿 관리 작업(작업 배정)을 시험하는 도구(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2608.26066",
      "source_unopened": false
    },
    {
      "id": "ref-815",
      "org": "Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등)",
      "title": "Holodeck: Language Guided Generation of 3D Embodied AI Environments",
      "published": "2023-12-14",
      "url": "https://arxiv.org/abs/2312.09067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "GPT-4 로 장면 구성과 공간 관계를 만들어 글 지시로 3D 환경을 생성하는 시스템(CVPR 2024, 초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2312.09067",
      "source_unopened": false
    },
    {
      "id": "ref-1127",
      "org": "Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L)",
      "title": "Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?",
      "published": "2020-08",
      "url": "https://arxiv.org/abs/1912.06321",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "시뮬레이션–현실 상관 계수(SRCC)를 제안하고 LoCoBot 주행에서 0.18 이던 성공률 SRCC 를 시뮬레이션 매개변수 조정으로 0.844 로 높였다(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/1912.06321",
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
      "summary": "원문 미열람. Open-RMF 예제 월드(호텔·클리닉·공항 터미널·캠퍼스 등)의 구성과 작업 명령. 이번 실행에서는 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 플릿 어댑터 템플릿 설정(recharge_threshold, recharge_soc, 충전기, 작업 종료 후 동작 등). 이번 실행에서는 다시 열지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 차선·경유점·문·승강기·충전기를 지도에 주석하는 편집기. 이번 실행에서는 다시 열지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-101",
      "org": "Merschformann, M. (RAWSim-O GitHub)",
      "title": "RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README)",
      "published": null,
      "url": "https://github.com/merschformann/RAWSim-O",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 운영의 결정 문제를 연구하는 이산 사건 시뮬레이션 프레임워크. 이번 실행에서는 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-398",
      "org": "Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L.",
      "title": "Decision rules for robotic mobile fulfillment systems",
      "published": "2019",
      "url": "https://www.sciencedirect.com/science/article/pii/S2214716019300946",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 결정 규칙을 시뮬레이션으로 비교한 연구. 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-267",
      "org": "IEEE 게재 논문 저자(미확인)",
      "title": "Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개))",
      "published": "2024",
      "url": "https://ieeexplore.ieee.org/document/10287275/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 AGV 시스템 경로망을 시뮬레이션으로 자동 설계하는 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-098",
      "org": "Zou, B., Gong, Y., de Koster, R., & Xu, X.",
      "title": "Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system",
      "published": "2018",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 의 충전·배터리 교환 전략을 대기행렬 모델로 비교한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-109",
      "org": "Stark, H.-G. 외",
      "title": "A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.17003",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 창고 충전소 배치 최적화 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-102",
      "org": "Springer(FAIM 2025 발표 논문, 저자 미확인)",
      "title": "Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics",
      "published": "2025",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 유통사 물류센터 팔레트 이동 데이터로 AMR 대수와 충전기 수를 시뮬레이션으로 정한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-381",
      "org": "Boysen, N., Briskorn, D., & Emde, S.",
      "title": "Parts-to-picker based order processing in a rack-moving mobile robots environment",
      "published": "2017",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정해 필요한 로봇 대수를 줄인 계산 실험 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원 약품 배송 로봇 실제 기록과 몬테카를로 시뮬레이션으로 승강기 가동률과 배송 실패의 관계를 분석했다(이번 실행에서는 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-103",
      "org": "PMC 게재 논문(저자 미확인)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": null,
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다층 호텔 배송 로봇 경로 계획에서 승강기를 대기·운행 시간으로 모델링한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-528",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ARIAC 의 장애·긴급 주문 과제를 매개변수로 선언해 주입하는 방식. 이번 실행에서는 다시 열지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1088",
      "org": "ASAM e.V.",
      "title": "ASAM OpenSCENARIO® XML",
      "published": null,
      "url": "https://www.asam.net/standards/detail/openscenario-xml/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 도로 교통 동적 시나리오 기술 표준. 이번 실행에서는 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1089",
      "org": "Shcherbyna, V. 외 (arXiv)",
      "title": "Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.12471",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 생성 모델 기반 환경 생성을 쓰는 사람 중심 주행 개발·벤치마크 플랫폼.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-116",
      "org": "Filippone, G., Pettinari, S., & Pelliccione, P.",
      "title": "Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.15427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 미션 명세·실행 형식을 비교 분석한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1090",
      "org": "BehaviorTree.CPP 프로젝트 (behaviortree.dev)",
      "title": "Groot2",
      "published": null,
      "url": "https://www.behaviortree.dev/groot/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 행동 트리 편집·모니터링 도구 안내 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1091",
      "org": "Moving AI Lab (Sturtevant 외)",
      "title": "MAPF Benchmarks",
      "published": null,
      "url": "https://movingai.com/benchmarks/mapf/index.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 에이전트 경로 찾기 벤치마크 지도와 시나리오 파일 모음.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1092",
      "org": "Open Source Robotics Foundation",
      "title": "SDFormat (Simulation Description Format)",
      "published": null,
      "url": "http://sdformat.org/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇과 환경을 시뮬레이터용으로 기술하는 XML 형식.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1086",
      "org": "Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv)",
      "title": "3D Environment Modeling for Falsification and Beyond with Scenic 3.0",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.03325",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 확률적 시나리오 언어 Scenic 3.0 의 3D 환경 모델링과 반증 시험.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-971",
      "org": "Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판)",
      "title": "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation",
      "published": "2024-03-14",
      "url": "https://arxiv.org/abs/2403.09227",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 일상 가정 활동 1,000개를 BDDL 로 명세하고 OmniGibson 에 구현한 벤치마크.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-291",
      "org": "Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W.",
      "title": "Digital Twin in manufacturing: A categorical literature review and classification",
      "published": "2018",
      "url": "https://www.sciencedirect.com/science/article/pii/S2405896318316021",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분한 제조 분야 문헌 분류.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-521",
      "org": "Le, T. V., & Fan, R.",
      "title": "Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 물류·공급망 디지털 트윈 문헌 검토와 개념 틀. 실데이터 검증 연구가 소수라고 보고.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-516",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 23247-1 을 국내에 도입한 KS 표준 소개 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-518",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 제조용 디지털 트윈 프레임워크의 디지털 트윈 결합(제6부) 표준 소개 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1126",
      "org": "VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik)",
      "title": "VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions",
      "published": "2025-05",
      "url": "https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 가상 시운전의 모델 유형·용어·정의를 다루는 지침 소개 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1130",
      "org": "Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545)",
      "title": "Virtual Commissioning of Distributed Systems in the Industrial Internet of Things",
      "published": "2023-03-28",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 분산 에지 컴퓨팅 시스템의 가상 시운전을 팔레타이징 설비로 시험한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1131",
      "org": "최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회)",
      "title": "자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스",
      "published": "2008-11",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 실제 PLC 와 3D 가상 공정 시뮬레이터를 연동하는 가상 플랜트 구축 절차.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1133",
      "org": "NASA",
      "title": "NASA-STD-7009B Standard for Models and Simulations",
      "published": "2024-03-05",
      "url": "https://standards.nasa.gov/standard/NASA/NASA-STD-7009",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모델·시뮬레이션 결과의 신뢰도 평가와 수용을 다루는 NASA 표준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-741",
      "org": "Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington)",
      "title": "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices",
      "published": "2025-10",
      "url": "https://arxiv.org/abs/2510.20808",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 공학의 시뮬레이션–현실 격차 원인과 해결 방법을 정리한 서베이.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1239",
      "org": "Open Robotics (Gazebo Classic)",
      "title": "Gazebo : Tutorial : Model structure and requirements",
      "published": null,
      "url": "https://classic.gazebosim.org/tutorials?tut=model_structure",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Gazebo 모델 데이터베이스의 구조와 database.config·model.config 의 라이선스·작성자 표기 규칙(이번 실행에서는 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-409",
      "org": "한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인)",
      "title": "아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105)",
      "published": "2023",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 친화형 건축물 인증을 아파트 단지로 확장한 4개 분야 28개 항목 인증 모델.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-106",
      "org": "한국교통연구원(인증스마트물류센터)",
      "title": "인증스마트물류센터",
      "published": null,
      "url": "https://cslc.koti.re.kr/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 스마트물류센터 인증 제도 안내 사이트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1165",
      "org": "Rockwell Automation",
      "title": "Emulation Technology Speeds Up Warehouse Automation",
      "published": "2024-08-28",
      "url": "https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 물류센터 구축에서 컨베이어·피킹 모듈 제어를 에뮬레이션으로 검증한 사례 소개(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-527",
      "org": "NVIDIA",
      "title": "NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins",
      "published": null,
      "url": "https://blogs.nvidia.com/blog/mega-omniverse-blueprint",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 로봇 플릿 디지털 트윈 블루프린트 발표(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-526",
      "org": "CJ대한통운",
      "title": "가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료)",
      "published": "2021-11",
      "url": "https://www.cjlogistics.com/ko/newsroom/news/NR_00000905",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 가상 물류센터 단계적 구축 계획 보도자료(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/design-and-simulation/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "대분류 연결 실행: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f44(3. 경제성·조달·사업 모델, 벤더 주장), f48(1. 기술·시장·업체 동향, 벤더 주장) / B. 로봇 온톨로지: f26(4. 이기종 로봇 등록), f34(7. 온톨로지 검증·변경 관리, oq-156) / C. 채팅 기반 구성·운영: f1·f2(9. 채팅으로 시나리오 구성·13. 대화형 기능의 신뢰·기반), f3·f4(11. 채팅으로 실제 상황 시뮬레이션 재현) — 분류 원문 4장 주석(시나리오 구성과 실제 상황 재현은 33·36번)과 짝 / D. 공간·지도 모델: f25, f6 / E. 사물·사람·실시간 상태: f7(18↔34 원문 구분), f29·f30(19. 사람·보행자 모델) / F. 연동: f8(22), f9(20), f40(21, oq-085), f41(23, 연계 대상), f20·f21·f42(22 승강기·로봇 친화 공간) / G. 계획·최적화: f14(28), f15(25), f16(26), f17(25), f18·f19(27), f24(24), f12(25), f22 / H. 실행·협업·예외 복구: f23(32) / J. 현장 운영·관제: f27·f28(37·38, oq-131), f43(39) / K. 플랫폼 아키텍처·인프라: f13(42) / L. AI·학습 기술: f5·f6(44), f32(47) / M. 안전: f35·f36(48), f30(49) / N. 보안·개인정보: f37·f38(51·52) / O. 검증·도입·수명주기: f10·f11(54·55), f31·f33(54) / P. 거버넌스·법규·사회: f39(59, oq-292) / Q. 현장 유형별 적용: f20·f22(63), f21·f30·f46(64), f42·f47(65), f45(62), f49·f16·f17(61). 아직 다루지 않은 연결: H. 실행·협업·예외 복구의 29·30·31, J. 현장 운영·관제의 40, K. 플랫폼 아키텍처·인프라의 41·43, N. 보안·개인정보의 53, P. 거버넌스·법규·사회의 58·60. 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)의 구분을 f7 로 명시. 다음 실행 후보: 34·35 페이지(이전 분류 기준)의 10절에 C·L·M·N·P 연결(f3·f5·f35·f37·f39) 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "슬롯카 모델",
      "term_en": "Slotcar (Open-RMF simulated robot plugin)",
      "definition": "Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이는 단순화 로봇 모델로, 로봇마다 주행 스택 전체를 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다."
    },
    {
      "term_ko": "혼합 현실 시험",
      "term_en": "Mixed-Reality Testing",
      "definition": "실제 로봇·센서와 가상 로봇·센서를 한 환경에 함께 두고 플릿 관리 같은 기능을 시험하는 방식으로, 모든 로봇을 실물로 갖추기 전에 작업 배정 등을 검증할 수 있게 한다."
    }
  ],
  "open_questions_new": [
    "대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 33. 시나리오 모델·편집, 13. 대화형 기능의 신뢰·기반 | 근거: f1 | 종류: 일반",
    "실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해, 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 52. 통신 보호·위협 관리·감사, 51. 인증·권한·격리 | 근거: f37 | 종류: 일반",
    "사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? | 관련 영역: 48. 안전·위험 관리, 34. 시뮬레이션·예측용 디지털 트윈, 19. 사람·보행자 모델 | 근거: f35 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 45,
    "cross_checked_count": 0,
    "unverified": [
      "Valiollahi 외(Scientific Reports 2026, 제조 로봇 플릿·공장 배치 시나리오 기반 디지털 트윈)는 C. 채팅 기반 구성·운영 페이지 자료 목록에 ref-838 로 있으나 검색 2회로 원문을 찾지 못해 쓰지 않음",
      "f1 Chat2Scenic 의 프레임워크 정확도 수치와 Scenic 언어 명시는 초록에서 확인하지 못해 claim 에서 뺌",
      "f29 Waymax 의 구체적 행동 모델 종류(기록 재생·IDM 등)는 초록에 없어 미확인",
      "f19 MAPF 벤치마크의 시나리오 파일 구성은 이번 실행에서 다시 열지 않았다(재인용)",
      "Gazebo Fuel 의 모델 단위 라이선스 필드는 확인하지 못함(oq-292 유지)",
      "국내 물류센터에서 AMR 시운전 전 디지털 트윈 검증 결과를 수치로 공개한 사례 미확인(한국어 검색 결과는 계획·MOU 기사뿐)",
      "f2·f4·f6·f13·f24·f26·f28·f32·f34·f36·f38·f41·f43 은 연결 해석([추정])이며 단일·재인용 근거"
    ],
    "scope_violations": [
      "f41: 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역이므로 claim 을 '연계 대상: '으로 시작함",
      "f20·f21·f8: 승강기·문 제어 자체는 시설·설비 제어 경계의 연계 대상이며 ROP 는 요청·상태 확인과 제약 입력만 맡는다고 발췌에 명시",
      "f45·f11: PLC·컨베이어 제어 코드의 가상 시운전은 설비 업체·통합자 몫(연계 대상)으로, ROP 가상 시운전의 방법 근거로만 사용",
      "f9·f32·f48: 로봇 자체 주행·인식 거동과 센서 시뮬레이션·현실 격차 보정은 로봇 제조사·시뮬레이터 제공자 쪽 연계 대상",
      "f35·f36: 안전 인증·설비 안전 제어 판단은 연계 대상이며 시나리오가 위험 식별 입력이 될 수 있다는 범위로만 서술"
    ],
    "budget_used": {
      "queries": 8,
      "sources": 4
    },
    "limits": "web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행으로 근거는 먼저 게시된 33·34·35·36 페이지와 A·B·F·G 대분류 페이지, 이전 브리프(2026-09-30-23)의 검증된 주장과 각주를 재사용했다. 검색 8회/30, 신규 출처 4건/15(ref-1329~ref-1332, 예약 구간 안). 재사용 출처 41건. 원문 열람: 신규 4건(arXiv 초록)과 재사용 6건(ref-406·ref-831 은 github_raw, ref-1128·ref-1129·ref-815·ref-1127 은 arXiv 초록 webfetch)을 이번에 열었고, 나머지 재사용 35건은 다시 열지 않아 fetched false·source_unopened true 로 표시했다. 입력 참고문헌 요약에 신뢰도 열이 없어 재사용 출처의 reliability 는 researcher.md 5절 유형 기준(미열람이면 medium 이하, 벤더 문서 low)으로 적었다. ref-381·ref-101·ref-409·ref-1239 는 이번 대상 페이지가 인용하지 않은 출처라 G·F 대분류 페이지 각주와 이전 브리프 2026-09-30-23 출처 표의 값을 옮겼다. ref-1329·ref-1330 은 C. 채팅 기반 구성·운영 페이지 자료 목록의 ref-833·ref-832 와 같은 논문일 가능성이 있으나 그 URL 을 입력에서 볼 수 없어 새 id 로 적었다(같은 URL 이면 퍼블리셔 병합 필요). 교차 확인 0건(대부분 연결 주장이 단일 출처 또는 서로 다른 내용의 출처 조합). 벤더 주장 3건(f44·f48·f49). 분류 원문 핵심 질문(현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가?)에는 대분류 연결 실행이므로 별도 답 finding 을 내지 않았고, 연결 근거로 f10(배치 전 시뮬레이션 이점)·f31(시뮬레이션 예측력 한계)·f41(실데이터 검증 부족)을 제시했다. L. AI·학습 기술 관련 finding(f5·f6·f32)은 적용 대상인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 함께 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 f7 에서 구분했다. 현장 유형 근거는 물류창고(f14·f16·f17·f41·f43·f44·f49), 병원(f20·f22), 상업 시설(f21·f30·f46), 가정(f42·f47), 제조 공장(f23·f45)이며 실외·기타는 로봇 현장 근거가 없어 null 로 두었다. H. 실행·협업·예외 복구의 29·30·31, J. 현장 운영·관제의 40, K. 플랫폼 아키텍처·인프라의 41·43, N. 보안·개인정보의 53, P. 거버넌스·법규·사회의 58·60 연결은 근거를 찾지 않아 '아직 다루지 않은 연결'로 남긴다. 한국 자료는 재사용(ref-1131·ref-409·ref-106·ref-516·ref-526) 위주이며 한국어 검색 1회에서 새로 쓸 만한 1차 자료는 찾지 못했다. 기존 열린 질문은 해결하지 못했다(oq-085·oq-131·oq-156·oq-235·oq-255·oq-257·oq-258·oq-292 는 연결 서술에서 참조만 함). 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음."
  }
}
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 62건 / 전체 1238건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 2026-09-25 | 아니오 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | https://doi.org/10.1177/20552076261437181 | 2026-09-25 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 2026-09-25 | 예 |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | https://repub.eur.nl/pub/107376/ | 2026-09-25 | 아니오 |
| ref-097 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 2020 | https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517 | 2026-09-25 | 아니오 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 2026-09-25 | 아니오 |
| ref-099 | Le-Anh, T., & de Koster, M. B. M. | A review of design and control of automated guided vehicle systems | 2006 | https://www.sciencedirect.com/science/article/abs/pii/S0377221705001840 | 2026-09-25 | 아니오 |
| ref-100 | Vis, I. F. A. | Survey of research in the design and control of automated guided vehicle systems | 2006 | https://www.sciencedirect.com/science/article/abs/pii/S0377221704006459 | 2026-09-25 | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | https://github.com/merschformann/RAWSim-O | 2026-09-25 | 예 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 2026-09-25 | 아니오 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 2026-09-25 | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | https://github.com/open-rmf/rmf_demos | 2026-09-25 | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 2026-09-25 | 예 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | https://cslc.koti.re.kr/ | 2026-09-25 | 아니오 |
| ref-107 | 법제처 국가법령정보센터 | 물류시설의 개발 및 운영에 관한 법률 | 미확인 | https://www.law.go.kr/LSW/lsInfoP.do?lsId=000091 | 2026-09-25 | 아니오 |
| ref-108 | 이문수, 채준재(로지스틱스연구) | AGV 기반 제조물류시스템의 성능평가를 위한 해석적 모형에 관한 연구 - 반도체 Tandem 레이아웃 시스템을 중심으로 - | 2010 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001485142 | 2026-09-25 | 아니오 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | https://arxiv.org/abs/2406.17003 | 2026-09-25 | 아니오 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | https://arxiv.org/abs/2603.15427 | 2026-09-25 | 아니오 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 2026-09-25 | 아니오 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | https://ieeexplore.ieee.org/document/10287275/ | 2026-09-25 | 아니오 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 2026-09-25 | 아니오 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 2026-09-25 | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/simulation.html | 2026-09-25 | 예 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 2026-09-25 | 아니오 |
| ref-517 | NIST | Digital Twins for Advanced Manufacturing | 미확인 | https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing | 2026-09-25 | 아니오 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | https://www.iso.org/standard/87426.html | 2026-09-25 | 아니오 |
| ref-519 | 머니투데이 | 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간 | 2026-07-28 | https://www.mt.co.kr/economy/2026/07/28/2026072809211448284 | 2026-09-25 | 아니오 |
| ref-520 | Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G. | Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics | 2020 | https://www.sciencedirect.com/science/article/pii/S2351978920320990 | 2026-09-25 | 아니오 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 2026-09-25 | 아니오 |
| ref-522 | Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P. | Simulation-based decision support tool for in-house logistics: the basis for a digital twin | 2021 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646 | 2026-09-25 | 아니오 |
| ref-523 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | https://github.com/open-rmf/rmf_simulation | 2026-09-25 | 예 |
| ref-524 | OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) | ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) | 미확인 | https://github.com/OpenFactoryTwin/ofact | 2026-09-25 | 예 |
| ref-525 | Sargent, R. G. | Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation) | 2008 | https://dl.acm.org/doi/abs/10.5555/1516744.1516780 | 2026-09-25 | 아니오 |
| ref-526 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 2021-11 | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 | 2026-09-25 | 아니오 |
| ref-527 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 미확인 | https://blogs.nvidia.com/blog/mega-omniverse-blueprint | 2026-09-25 | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 2026-09-25 | 예 |
| ref-599 | Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M. | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 2019-09 | https://arxiv.org/abs/1807.00048 | 2026-09-25 | 아니오 |
| ref-726 | Kästner, L. 외 | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | https://arxiv.org/abs/2206.05728 | 2026-09-25 | 아니오 |
| ref-741 | Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 2025-10 | https://arxiv.org/abs/2510.20808 | 2026-09-25 | 아니오 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12-14 | https://arxiv.org/abs/2312.09067 | 2026-09-29 | 예 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 미확인 | https://github.com/ros2/rosbag2 | 2026-09-29 | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 2026-09-29 | 예 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03-14 | https://arxiv.org/abs/2403.09227 | 2026-09-29 | 예 |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | https://arxiv.org/abs/2307.03325 | 2026-09-30 | 예 |
| ref-1087 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 2026-09-30 | 예 |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | https://www.asam.net/standards/detail/openscenario-xml/ | 2026-09-30 | 예 |
| ref-1089 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | https://arxiv.org/abs/2409.12471 | 2026-09-30 | 예 |
| ref-1090 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | https://www.behaviortree.dev/groot/ | 2026-09-30 | 예 |
| ref-1091 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | https://movingai.com/benchmarks/mapf/index.html | 2026-09-30 | 예 |
| ref-1092 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | http://sdformat.org/ | 2026-09-30 | 예 |
| ref-1126 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions | 2025-05 | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions | 2026-09-30 | 예 |
| ref-1127 | Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L) | Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance? | 2020-08 | https://arxiv.org/abs/1912.06321 | 2026-09-30 | 아니오 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 2023-10-12 | https://arxiv.org/abs/2310.08710 | 2026-09-30 | 예 |
| ref-1129 | Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv) | VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots | 2026-08-26 | https://arxiv.org/abs/2608.26066 | 2026-09-30 | 예 |
| ref-1130 | Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545) | Virtual Commissioning of Distributed Systems in the Industrial Internet of Things | 2023-03-28 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/ | 2026-09-30 | 예 |
| ref-1131 | 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회) | 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스 | 2008-11 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794 | 2026-09-30 | 예 |
| ref-1132 | 현대자동차그룹 | 가상의 디지털 공간에 세운 쌍둥이 공장 | 2023-11-21 | https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330 | 2026-09-30 | 예 |
| ref-1133 | NASA | NASA-STD-7009B Standard for Models and Simulations | 2024-03-05 | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 | 2026-09-30 | 예 |
| ref-1134 | Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI) | Composable and executable scenarios for simulation-based testing of mobile robots | 2024-08-02 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full | 2026-09-30 | 예 |
| ref-1165 | Rockwell Automation | Emulation Technology Speeds Up Warehouse Automation | 2024-08-28 | https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 346개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
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
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
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
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
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

### docs/open-questions.md (요약: 대상 영역 [33, 34, 35, 36] 에 걸린 30건 / 전체 292건)

```markdown
- oq-008 [열림] 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? (영역 35, 39)
- oq-009 [열림] 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? (영역 31, 35)
- oq-010 [열림] 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? (영역 22, 35)
- oq-011 [열림] 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? (영역 35, 39)
- oq-017 [열림] 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? (영역 35, 39)
- oq-031 [열림] 국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가? (영역 20, 35)
- oq-040 [열림] 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가? (영역 35, 42)
- oq-050 [열림] 로봇 작업대의 주문·랙 순서 최적화 연구가 보고한 로봇 대수·랙 방문 절감 효과를 이종 로봇과 사람 포장대가 섞인 국내 물류센터에서 검증한 자료가 있는가? (영역 26, 35)
- oq-081 [열림] 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? (영역 32, 34)
- oq-084 [열림] 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? (영역 34, 39)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 21, 34)
- oq-086 [열림] 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? (영역 20, 34)
- oq-094 [열림] Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가? (영역 22, 34, 54, 55)
- oq-108 [열림] 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? (영역 21, 34)
- oq-117 [열림] 국내 물류센터 로봇 관제 도입에서 디지털 트윈·가상 로봇으로 관제 소프트웨어를 사전 검증한 결과를 실제 시운전 결과와 비교해 공개한 사례가 있는가? (관련 기존 질문: oq-094) (영역 34, 55)
- oq-118 [열림] 국내 물류센터 로봇 관제에서 작업 지시나 배정 결과를 배치 전에 시뮬레이션(디지털 트윈)으로 모의 실행해 확인하는 운영 사례나 연구가 있는가? (영역 25, 34)
- oq-129 [열림] 채팅으로 정한 로봇 대수를 시뮬레이션 기반 대수 산정과 어떻게 연결하고, 처리량 최대화와 비용 최소화 가운데 어느 목적을 누가 정하는가? (영역 10, 35, 3)
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
- oq-132 [열림] 재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가? (영역 11, 36, 54)
- oq-135 [열림] 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? (영역 9, 33)
- oq-156 [열림] 분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? (영역 7, 54, 36)
- oq-233 [열림] 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? (영역 33, 34)
- oq-234 [열림] 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? (영역 33, 57)
- oq-235 [열림] ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? (영역 33, 32)
- oq-236 [열림] 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? (영역 33, 65)
- oq-255 [열림] 여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가? (영역 36, 20, 55)
- oq-256 [열림] 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? (영역 36, 19, 33)
- oq-257 [열림] 물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가? (영역 36, 3)
- oq-258 [열림] 한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가? (영역 36, 63, 22)
- oq-292 [열림] 시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가? (영역 59, 36, 57)
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

### runs/2026-10-09-03/research.md

```markdown
# 리서치 브리프 2026-10-09-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-03 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | E. 사물·사람·실시간 상태 |

## 갭(비어 있거나 약한 섹션)

- E. 사물·사람·실시간 상태 대분류 페이지의 '다른 대분류와의 연결' 절 비어 있음(아직 작성되지 않음)
- A. 기획·사업과 E. 사물·사람·실시간 상태의 세 세부영역을 직접 잇는 검증된 근거가 게시 페이지에 없음
- C. 채팅 기반 구성·운영과의 연결 근거가 E 쪽 게시 페이지에 없음 — 이번 실행에서 12. 채팅으로 업무 지시·오케스트레이션 쪽 근거(ref-854)를 보강
- 17. 작업 대상·자산 식별과 인계 추적의 '수령인 확인'(사람에게 넘길 때)과 N. 보안·개인정보·Q. 현장 유형별 적용을 잇는 근거 없음 — 병원·공동주택·사무 건물 사례를 새로 찾음
- L. AI·학습 기술의 45. 문서·도면·장면 이해와 18·19의 연결(oq-227 고정 카메라·로봇 인식 결합)은 근거 미확보
- 옛 분류 기준으로 다른 대분류 페이지(A·B·F·G)에 E 쪽 영역과의 연결이 실려 있으나 새 17개 대분류 이름으로 다시 정리되지 않음

## 조사 질문

1. 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문] — 이 답이 다른 대분류의 어느 세부영역으로 넘어가는가?
2. 17. 작업 대상·자산 식별과 인계 추적은 F. 연동(20·22·23), G. 계획·최적화(24), H. 실행·협업·예외 복구(30·32), P. 거버넌스·법규·사회(58)와 어떤 신호·기록을 주고받는가? (oq-001, oq-003, oq-006, oq-036, oq-079 관련)
3. 17. 작업 대상·자산 식별과 인계 추적의 수령인 확인은 병원·공동주택 현장에서 어떤 인증 수단으로 이루어지며 N. 보안·개인정보(51·53)와 어떻게 이어지는가? (oq-180, oq-184 관련)
4. 18. 실시간 세계 상태·데이터 일관성은 B. 로봇 온톨로지(5·6), D. 공간·지도 모델(15), F. 연동(20·22), G. 계획·최적화(28), I. 설계·시뮬레이션(34), J. 현장 운영·관제(38·39), K. 플랫폼 아키텍처·인프라(42·43), M. 안전(48)과 무엇을 주고받는가? (oq-024, oq-028, oq-034, oq-035 관련)
5. 19. 사람·보행자 모델은 D. 공간·지도 모델(15·16), G. 계획·최적화(26·27), H. 실행·협업·예외 복구(31), I. 설계·시뮬레이션(34·36), L. AI·학습 기술(46), M. 안전(49), N. 보안·개인정보(53), O. 검증·도입·수명주기(54), P. 거버넌스·법규·사회(60), Q. 현장 유형별 적용(61·63·64·66)과 어떻게 이어지는가? (oq-256, oq-261, oq-272, oq-273, oq-274 관련)
6. C. 채팅 기반 구성·운영의 대화형 업무 지시가 18. 실시간 세계 상태·데이터 일관성의 현재 상태를 근거로 쓰는 공개 구현이 있는가?
7. E. 사물·사람·실시간 상태와 다른 대분류의 연결 가운데 근거가 아직 없는 쌍은 무엇인가? (다루지 않은 연결 목록)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ B. 로봇 온톨로지의 5. 로봇 능력·작업 표현: VDA 5050 팩트시트가 로봇이 취급할 수 있는 적재 유형을 선언하고 상태 메시지의 loadId 가 실제로 실린 적재물을 식별하므로, '이 로봇이 이 적재물을 다룰 수 있는가'를 판단하려면 능력 표현의 적재 유형과 17의 적재물 식별을 같은 어휘로 맞춰야 할 것으로 보이며 공통 어휘는 확인되지 않았다(oq-023). | ref-228, ref-051 | 아니오 | low | 2026-10-09 | 작업 대상 | — |
| f2 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ B. 로봇 온톨로지의 5. 로봇 능력·작업 표현: Naqvi 외(Scientific Reports, 2025-10-02)는 로봇 능력 온톨로지(RCO)에서 제조사가 공개한 능력 수치와 운용 중 로봇이 실제로 보인 성능을 구분해 연결한다. | ref-041 | 아니오 | medium | 2025-10-02 | — | 원문 미열람 |
| f3 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: 18이 모은 로봇의 관측 상태(배터리·문제 목록·위치)가 능력의 '지금 실행 가능 여부' 판단과 운용 능력 갱신의 입력이 될 것으로 보이며, 선언 능력과 관측 능력 가운데 무엇을 배정 기준으로 삼을지는 열린 질문(oq-024)으로 남아 있다. | ref-041, ref-148 | 아니오 | low | 2026-10-09 | 수행 자원 | — |
| f4 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 2026-07-02 Open Robotics 상호운용 SIG 발표(Nayantra)는 Open-RMF REST API 를 언어 모델이 호출할 수 있는 MCP 도구로 감싸고, 평이한 영어 지시를 여러 단계의 RMF 임무로 바꿔 Nav2 로 보내는 구성을 소개했다. | ref-854 | 아니오 | medium | 2026-06-25 | 시작 조건 | — |
| f5 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 대화로 '어디까지 했는가·왜 멈췄는가'에 답하려면 로봇 상태의 시각·상태 값·문제 목록 같은 현재 상태 기록을 근거로 써야 할 것으로 보이나, Open-RMF–MCP 연동이 상태 질의까지 제공하는지는 확인하지 못했다. | ref-854, ref-148 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f6 | [추정] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현·I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 실제 운영 기록을 재생해 상황을 재현하면 기록된 사람이 바뀐 조건(로봇 수·배차 정책)에 반응하지 않는 문제가 생기며, 19. 사람·보행자 모델 페이지는 이를 열린 질문(oq-256)으로 두고 기록 재현 시뮬레이터(Waymax)와 사람 행동 시뮬레이터(HuNavSim)를 참고로 든다. | ref-1128, ref-1179 | 아니오 | low | 2026-09-30 | — | 원문 미열람 |
| f7 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: VDA 5050 상태 스키마는 위치추정 품질(localizationScore), 미터 단위 위치 편차 범위(deviationRange), 작업 공간 지도 식별자(mapId)를 두어, 보고된 위치를 얼마나 믿을지(18)와 어느 지도 위의 위치인지(15)가 같은 메시지로 넘어온다. | ref-051 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f8 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리: GS1 GLN 이 도크 문·보관 위치 같은 하위 위치를 식별할 수 있으므로, 인계 이벤트의 업무 위치와 로봇 지도 위 장소를 대응시키는 계층이 ROP 쪽에 필요할 것으로 보이며 국내 적용 사례는 확인되지 않았다(oq-029). | ref-162, ref-031 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f9 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: 움직임 지도(maps of dynamics)는 공간에 사람의 전형적 움직임 패턴을 덧붙인 지도이며, EU ILIAD 프로젝트는 학습한 사람 흐름에 맞춰 창고 자율 지게차의 경로를 계획했다. | ref-1171, ref-1180 | 아니오 | medium | 2023 | 물류창고 / 제약 | 원문 미열람 |
| f10 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다(기사 1건 기준). | ref-1181 | 아니오 | medium | 2024-07-12 | 병원 / 제약 | 원문 미열람 |
| f11 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ F. 연동의 20. 로봇·제조사 관제 연동: VDA 5050 상태 스키마의 loads 는 로봇이 현재 취급 중인 적재물을 담고, loadId 는 바코드·RFID 같은 적재물 식별 번호, loadPosition 은 어느 적재 장치를 쓰는지를 나타낸다. | ref-051 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f12 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ F. 연동의 22. 설비·건물 시스템 연동: Open-RMF 배송 작업에서 로봇은 픽업 지점의 DispenserResult, 하역 지점의 IngestorResult 를 받을 때까지 요청을 되풀이하고, IngestorResult 는 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. | ref-023, ref-049 | 아니오 | medium | 2026-09-25 | 완료·인계 | — |
| f13 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ F. 연동의 22. 설비·건물 시스템 연동: 설비의 인수 결과에는 화물 식별자·인계 당사자가 없으므로 설비 쪽 SUCCESS 를 17의 식별·인계 기록과 결합해야 '무엇이 누구에게 넘겨졌는지'가 확정될 것으로 보이며, 이를 정한 표준 매핑은 확인되지 않았다(oq-001, oq-061). | ref-049, ref-014, ref-015 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f14 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·18. 실시간 세계 상태·데이터 일관성 ↔ F. 연동의 23. 업무 시스템 연동: DeHoratius·Raman(2008)은 한 소매업체 37개 매장 재고 기록의 65%가 실물과 맞지 않았다고 보고했다(소매 매장 조건이며 물류센터 값이 아니다). | ref-292 | 아니오 | medium | 2008 | 상업 시설 / 예외·성과 | 원문 미열람 |
| f15 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·18. 실시간 세계 상태·데이터 일관성 ↔ F. 연동의 23. 업무 시스템 연동: 로봇이 보고한 적재물 식별 결과와 WMS 재고 기록이 어긋나면 덮어쓰지 않고 두 기록을 함께 보관해 정정 이벤트로 업무 시스템에 되돌리는 것이 두 대분류의 넘겨받는 지점이 될 것으로 보이며, 어느 쪽을 기준으로 삼고 누가 정정하는지는 열린 질문(oq-036)이다. | ref-292, ref-051, ref-492 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f16 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ F. 연동의 22. 설비·건물 시스템 연동: Open-RMF 문 상태(DoorState)는 생성 시각 door_time·문 이름·현재 모드를, 승강기 상태(LiftState)는 생성 시각 lift_time·현재·목적 층·문 상태·운행 상태·현재 모드·제어 세션 id 를 담고, 두 메시지 모두 허용 경과 시간은 정하지 않는다. | ref-285, ref-286 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f17 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ F. 연동의 20. 로봇·제조사 관제 연동: Open-RMF 로봇 상태는 밀리초 유닉스 시각(unix_millis_time), 상태 7종, 0~1 배터리, 운영자가 풀어야 할 문제 목록(issues)을 담고, VDA 5050 상태는 ISO 8601 형식 시각(timestamp)을 담는다. | ref-148, ref-051 | 아니오 | medium | 2026-10-09 | 수행 자원 | — |
| f18 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 관제 인터페이스마다 시각 표현과 보고 주기가 달라 20의 어댑터가 받은 상태를 18의 공통 시간축으로 옮기는 변환·시계 오차 기준이 필요할 것으로 보이나, 이를 규정한 자료는 확인하지 못했다(oq-035). | ref-148, ref-051 | 아니오 | low | 2026-10-09 | — | — |
| f19 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ G. 계획·최적화의 24. 작업·워크플로 모델링: GS1 CBV 는 도착(arriving)·입고(receiving)·인수(accepting)를 서로 다른 업무 단계로 정의하고, VDA 5050 은 하역(drop) 완료를 적재물이 로봇을 떠나 로봇이 새 적재 상태를 보고한 때로 정의한다. | ref-044, ref-031 | 아니오 | medium | 2021-09-30 | 완료·인계 | — |
| f20 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: Open-RMF 로봇 상태는 배터리를 0.0(빈)~1.0(가득)으로, VDA 5050 상태는 powerSupply.stateOfCharge 를 퍼센트로 보고한다. | ref-148, ref-051 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f21 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: Open-RMF 가 작업을 끝낼 충전량이 부족하면 충전 작업을 일정에 끼워 넣으므로, 충전 계획은 18이 표현하는 현재 배터리 상태를 단위를 맞춰 입력으로 쓰는 것으로 보인다. | ref-104, ref-148 | 아니오 | low | 2026-09-25 | 제약 | — |
| f22 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Vintr 외(2022)는 장기 시공간 보행자 흐름 지도를 경로 계획에 쓰고 예상 조우(Expected Encounters)와 예상 경로 길이로 비교했으며, 대학 건물 현장 실험에서 예측형 주행은 불편을 드러낸 사람이 두 세션 모두 0명, 반응형은 2명·1명이었다(40분 세션 4회의 매우 작은 표본). | ref-1178 | 아니오 | medium | 2022-07-04 | 기타 / 예외·성과 | 원문 미열람 |
| f23 | [추정] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ G. 계획·최적화의 26. 작업 순서·스케줄링: 낮 시간 복도 혼잡과 '무조건 대기' 규칙(병원), 혼잡을 예상해 위치를 정하는 계획(쇼핑몰 연구)처럼 사람 흐름은 로봇 작업 시간과 순서에 영향을 줄 것으로 보이나, 시간대별 혼잡을 작업 시간 추정·스케줄링에 넣어 효과를 측정한 현장 연구는 확인하지 못했다(oq-273). | ref-1181, ref-1182 | 아니오 | low | 2026-09-30 | 제약 | 원문 미열람 |
| f24 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ H. 실행·협업·예외 복구의 30. 로봇 간 협업·물리적 인계: EPCIS 가 소유·점유·위치 이전을 출발지·도착지(source/destination)로 표현하므로, 로봇·설비 사이 물리적 인계의 확인은 17의 식별자·인계 당사자 기록과 결합해야 할 것으로 보인다(oq-001, oq-006). | ref-049, ref-014, ref-015 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f25 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 팔레트 RFID 태그 판독성이 제품·포장·태그 위치·적재 패턴에 따라 달라진다는 실험 보고가 있어, 판독 실패·오판독 때 인계 보류·재스캔·사람 확인 규칙이 복구 과제로 넘어갈 것으로 보인다(oq-003). | ref-024 | 아니오 | low | 2009 | 예외·성과 | 원문 미열람 |
| f26 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: EPCIS 1.2 는 이미 기록된 이벤트를 오류 선언(errorDeclaration)으로 정정하게 하므로, 고장 로봇에서 회수한 화물의 위치·이벤트 정정이 식별·추적 쪽 기록 규칙에 기대게 된다(oq-079). | ref-492 | 아니오 | medium | 2016-09-29 | 완료·인계 | 원문 미열람 |
| f27 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성·32. 예외 복구·재계획·업무 연속성: VDA 5050 3.0.0 에서 로봇 연결이 예기치 않게 끊기면 브로커가 MQTT 유언으로 CONNECTION_BROKEN 을 대신 알리고, 로봇은 받은 주문을 유지한 채 마지막으로 해제된 노드까지 수행한다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f28 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성·19. 사람·보행자 모델 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업: Riedelbauch·Werner·Henrich(RAAD 2017)는 사람과 함께 쓰는 작업 공간에서 세계 모델의 정보마다 확실도 값을 붙이고, 전역 센서가 감지한 사람 존재에 따라 이 값을 시간에 따라 조정해 로봇이 정보가 아직 유효한지 판단하게 했다. | ref-1302 | 아니오 | medium | 2017 | — | — |
| f29 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성·19. 사람·보행자 모델 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업: 사람이 드나든 구역의 물품·설비 상태는 관측 뒤 바뀌었을 가능성이 높으므로, 19의 사람 위치 정보가 18의 상태 신뢰도를 낮추는 근거로 쓰일 수 있을 것으로 보이나 이동로봇 현장 적용 사례는 확인하지 못했다. | ref-1302 | 아니오 | low | 2026-10-09 | — | — |
| f30 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 제조 분야 분류 자료가 현장 상태가 한 방향으로 자동 반영되는 디지털 섀도와 디지털 트윈을 구분하므로, 18은 현재 상태를 표현하고 34는 그 표현을 복제해 가정한 미래를 실험하는 쪽으로 나누는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거 자료는 제조 대상). | ref-291, ref-290 | 아니오 | low | 2018 | — | 원문 미열람 |
| f31 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: HuNavSim 은 사람 인지 내비게이션을 벤치마크하기 위한 ROS 2 사람 이동 시뮬레이터이고, Kidokoro 외(HRI 2013)는 보행자 행동 모델로 가상 주행 상황을 시뮬레이션해 혼잡을 피하는 로봇 위치를 계획했다. | ref-1179, ref-1182 | 아니오 | medium | 2023-09-13 | — | 원문 미열람 |
| f32 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·39. 운영 성과 측정·개선: 로봇 상태의 상태 값·배터리·문제 목록·시각과 문·승강기 상태의 시각을 한 세계 상태 기록에 모으면, 가동률·충전·오류 시간 지표와 '지연 원인이 로봇인지 문인지' 분석이 같은 기록을 쓰게 될 것으로 보인다. | ref-148, ref-285, ref-286 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f33 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지처럼 통신 계층에 상태의 오래됨을 알리는 장치가 있다. | ref-282, ref-287, ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f34 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·18. 실시간 세계 상태·데이터 일관성 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: EPCIS 2.0 온톨로지가 발생 시각(eventTime)·기록 시각(recordTime)·UTC 차이를 구분하므로, 실행 기록과 관측 데이터에서도 발생 시각과 수신·기록 시각을 따로 남기는 설계가 두 대분류를 잇는 지점이 될 것으로 보인다. | ref-045 | 아니오 | low | 2021-09-30 | — | — |
| f35 | [추정] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ L. AI·학습 기술의 46. 예측·학습 기반 최적화: Rudenko 외 서베이가 정리한 사람 움직임 궤적 예측은 19의 가까운 미래 사람 위치 추정 방법이므로, 예측 결과를 경로·배정 비용에 넣는 일이 46과 이어질 것으로 보인다. | ref-1172 | 아니오 | low | 2019-12-17 | — | 원문 미열람 |
| f36 | [사실] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ M. 안전의 48. 안전·위험 관리: Open-RMF 승강기 상태의 현재 모드에는 알 수 없음·사람·AGV·화재·오프라인·비상이 있으며 사람·AGV 모드만 설정할 수 있고 나머지는 읽기 전용이다. | ref-286 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f37 | [추정] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ M. 안전의 49. 사람 근접 안전: 병원의 '사람·휠체어와 마주치면 무조건 대기' 규칙과 창고의 움직임별 사회적 비용에 따른 속도 제약처럼 사람 흐름 정보는 구역별 대기·속도 규칙으로 49와 이어지며, ROP 는 규칙을 요청·관리하고 사람 검출·안전 정지는 연계 대상으로 로봇이 맡는 경계가 될 것으로 보인다. | ref-1181, ref-1180 | 아니오 | low | 2026-09-30 | 제약 | 원문 미열람 |
| f38 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터: ROS 규약 제안 REP-155(Draft, 2022-01-11 작성)는 사람마다 영속 ID 를 두고 얼굴·몸·음성 ID 를 후보 대응으로 연결하며, 이 문서는 개인정보·동의를 다루지 않는다. | ref-1173 | 아니오 | medium | 2022-01-11 | 작업 대상 | — |
| f39 | [추정] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터: 사람 표현의 영속 ID 가 얼굴·음성 인식과 연결될 수 있으므로 ROP 가 보관하는 사람 정보는 구역·시간대 집계·익명화로 두는 것이 두 대분류의 경계가 될 것으로 보이며, 여러 출처의 사람 위치를 합치는 익명화 형식과 촬영 거부 의사 공유 방법은 열린 질문(oq-261, oq-272)이다. | ref-1173 | 아니오 | low | 2026-09-30 | 제약 | — |
| f40 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ N. 보안·개인정보의 51. 인증·권한·격리: 병원용 운반 로봇 Zena RX(ST Engineering Aethon, 2024-04 출시 발표)는 생체 인식과 직원 PIN 코드로 잠금 칸을 열게 해 권한 있는 직원만 약품·검체를 꺼낼 수 있다고 제조사는 밝힌다. | ref-1299 | 아니오 | low | 2024-04-29 | 병원 / 완료·인계 | 벤더 주장 |
| f41 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ N. 보안·개인정보의 51. 인증·권한·격리: 2019-10 우아한형제들 본사(서울 잠실) 시범 운영에서 배달 로봇 딜리타워는 라이더가 주문번호 앞 네 자리와 층을 입력하면 승강기로 이동해 고객에게 전화를 걸고, 고객이 휴대전화 번호 뒤 네 자리를 입력해야 음식 칸이 열렸다(기사 기준). | ref-1300 | 아니오 | low | 2019-10-17 | 기타 / 완료·인계 | — |
| f42 | [사실] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ N. 보안·개인정보의 51. 인증·권한·격리: 2020-07 보도에 따르면 딜리타워의 공동주택(포레나 영등포) 도입 계획에서는 라이더와 고객이 모두 로봇 화면에 비밀번호를 눌러 적재함을 열고, 로봇은 도착 시 고객에게 문자와 전화로 알리게 되어 있었다. | ref-1301 | 아니오 | low | 2020-07-03 | 가정 / 완료·인계 | — |
| f43 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: 확인한 사례의 수령인 확인 수단이 생체+PIN(병원), 전화번호 뒤 네 자리(사무 건물), 비밀번호(공동주택 계획)로 서로 달라, 17의 '누구에게 넘겼는가' 기록은 51의 인증 수단과 53의 생체·전화번호 처리에 기대게 될 것으로 보이며, 그 결과가 주문·업무 시스템에 완료 이벤트로 기록되는지는 확인하지 못했다(oq-180, oq-184). | ref-1299, ref-1300, ref-1301 | 아니오 | low | 2026-10-09 | 완료·인계 | — |
| f44 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: 사회적 로봇 내비게이션 알고리즘 평가 원칙·지침(Francis 외, 2023)과 장기 시공간 보행자 흐름 지도의 벤치마크 연구(Vintr 외, 2022)가 있어, 사람 모델을 쓴 계획의 효과를 시험하는 방법이 54와 이어진다. | ref-1079, ref-1178 | 아니오 | medium | 2023-06-29 | — | 원문 미열람 |
| f45 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Han 외(CHI 2024)는 이동장애인 15명·로봇 실무자 8명 면담과 4회 공동설계 워크숍에서 보도 로봇이 들어오면 이동장애인이 보도 공간을 두고 경쟁해야 한다고 느끼며, 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. | ref-1265 | 아니오 | medium | 2024-04-07 | 실외 / 제약 | — |
| f46 | [추정] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 보행 약자가 지나야 하는 연석 경사로·좁은 통로를 사람 흐름 모델의 양보·비정차 구역으로 표현해야 60의 접근성 요구가 경로·대기 위치 제약으로 이어질 것으로 보이나, 국내 기준은 확인하지 못했다(oq-188 관련). | ref-1265 | 아니오 | low | 2026-10-09 | 실외 / 제약 | — |
| f47 | [추정] | E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: CBV 의 출발지·도착지 유형(owning_party·possessing_party·location)이 소유·점유 이전을 당사자 단위로 기록하므로, 제조사·운영사·화주 사이 인계 책임의 기록 근거가 17의 이벤트에서 나올 것으로 보인다. | ref-014, ref-015, ref-044 | 아니오 | low | 2021-09-30 | 완료·인계 | — |
| f48 | [사실] | 연계 대상: E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ Q. 현장 유형별 적용의 66. 실외 — 행정안전부 인파관리지원시스템은 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사 기지국 접속정보로 인파 밀집도를 추정해 위험 수준에 따라 지자체 공무원에게 경보를 보내며, 실외 로봇 운행 제약과 연동한 사례는 확인되지 않았다(oq-274). | ref-1177 | 아니오 | medium | 2023-12-27 | 실외 / 시작 조건 | 원문 미열람 |
| f49 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ Q. 현장 유형별 적용의 61. 물류창고·63. 병원·의료·64. 상업 시설: 게시된 19. 사람·보행자 모델 페이지의 적용 사례는 스웨덴 외레브로 창고의 자율 지게차 플릿(ILIAD), 한림대학교성심병원의 복도 혼잡 대응, 쇼핑몰에서 혼잡을 예상하는 로봇(Kidokoro 외)이다. | ref-1180, ref-1181, ref-1182 | 아니오 | medium | 2026-09-30 | — | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-014 | GS1 | Core Business Vocabulary (CBV) Standard | 미확인 | 표준 | medium | 2026-10-09 | https://ref.gs1.org/standards/cbv/ | 예 |
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 미확인 | 표준 | medium | 2026-10-09 | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf | 예 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 아니오 |
| ref-024 | Singh, J. 외 | RFID tag readability issues with palletized loads of consumer goods | 2009 | 논문 | medium | 2026-10-09 | https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 2025-10-02 | 논문 | medium | 2026-10-09 | https://www.nature.com/articles/s41598-025-16649-3 | 예 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | 표준 | medium | 2026-10-09 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 아니오 |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | 표준 | medium | 2026-10-09 | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl | 아니오 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-162 | GS1 | Identifying a physical location - GLN | 미확인 | 표준 | medium | 2026-10-09 | https://www.gs1.org/standards/id-keys/gln/physical-location | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html | 예 |
| ref-285 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc | 아니오 |
| ref-290 | NIST | DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 | 예 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-292 | DeHoratius, N., & Raman, A. | Inventory Record Inaccuracy: An Empirical Analysis | 2008 | 논문 | medium | 2026-10-09 | https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789 | 예 |
| ref-492 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 2016-09-29 | 표준 | medium | 2026-10-09 | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse | Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 아니오 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2306.16740 | 예 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 2023-10-12 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2310.08710 | 예 |
| ref-1171 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 2023 | 논문 | medium | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/02783649231190428 | 예 |
| ref-1172 | Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020) | Human Motion Trajectory Prediction: A Survey | 2019-12-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/1905.06113 | 예 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 아니오 |
| ref-1177 | 행정안전부 (대한민국 정책브리핑) | 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 | 2023-12-27 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148924176 | 예 |
| ref-1178 | Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI) | Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation | 2022-07-04 | 논문 | medium | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full | 예 |
| ref-1179 | Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023) | HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation | 2023-09-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2305.01303 | 예 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | 정부·연구기관 | medium | 2026-10-09 | https://iliad-project.eu/concluding-iliad/ | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | medium | 2026-10-09 | https://v.daum.net/v/bc4riunbUE | 예 |
| ref-1182 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 2013-03 | 논문 | medium | 2026-10-09 | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 | 예 |
| ref-1265 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | high | 2026-10-09 | https://arxiv.org/abs/2404.05050 | 아니오 |
| ref-1299 | ST Engineering Aethon (Newswire 게재 보도자료) | ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals | 2024-04-29 | 벤더 문서 | low | 2026-10-09 | https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264 | 아니오 |
| ref-1300 | 바이라인네트워크 (엄지용) | 엘리베이터 타는 배달로봇과의 조우 | 2019-10-17 | 기사 | low | 2026-10-09 | https://byline.network/2019/10/17-73/ | 아니오 |
| ref-1301 | 경향신문 (곽희양) | 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다 | 2020-07-03 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202007031130001 | 아니오 |
| ref-1302 | Riedelbauch, D., Werner, T., & Henrich, D. (RAAD 2017, Springer) | Supporting a Human-Aware World Model through Sensor Fusion | 2017 | 논문 | medium | 2026-10-09 | https://eref.uni-bayreuth.de/92445 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/index.md | 5. 다른 대분류와의 연결 | 대분류 연결 실행: '다른 대분류와의 연결' 절만 patches 로 채움. B. 로봇 온톨로지: f1(17↔5), f2·f3(18↔5·6) / C. 채팅 기반 구성·운영: f4·f5(18↔12), f6(19↔11·36) / D. 공간·지도 모델: f7(18↔15), f8(17↔15·16), f9(19↔15), f10(19↔16) / F. 연동: f11(17↔20), f12·f13(17↔22), f14·f15(17·18↔23), f16(18↔22), f17·f18(18↔20) / G. 계획·최적화: f19(17↔24), f20·f21(18↔28), f22(19↔27), f23(19↔26) / H. 실행·협업·예외 복구: f24(17↔30), f25·f26(17↔32), f27(18↔29·32), f28·f29(18·19↔31) / I. 설계·시뮬레이션: f30(18↔34, 18·34 구분 유지), f31(19↔34) / J. 현장 운영·관제: f32(18↔38·39) / K. 플랫폼 아키텍처·인프라: f33(18↔42), f34(17·18↔43) / L. AI·학습 기술: f35(19↔46) / M. 안전: f36(18↔48), f37(19↔49) / N. 보안·개인정보: f38·f39(19↔53), f40~f43(17↔51·53, 벤더 주장 f40 병기) / O. 검증·도입·수명주기: f44(19↔54) / P. 거버넌스·법규·사회: f45·f46(19↔60), f47(17↔58) / Q. 현장 유형별 적용: f48(19↔66, 연계 대상), f49(19↔61·63·64), 수령인 확인 사례 f40(병원)·f41(기타)·f42(가정). 아직 다루지 않은 연결: A. 기획·사업 전체, 18·19 ↔ 45. 문서·도면·장면 이해(oq-227), 17 ↔ 54·55·57, 37. 관제 화면·실행 기록·40. 운영 절차·요청 창구, 52. 통신 보호·위협 관리·감사, 59. 법·규제·보험·라이선스. 추정 태그 finding 은 추정 그대로, 관련 열린 질문 id 병기. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 병원 운반 로봇의 생체 인식·PIN 수령 확인처럼 수령인 인증 결과를 작업 완료·인계 이벤트로 ROP 와 병원 정보 시스템에 남기는 공개 인터페이스나 표준 필드가 있는가? | 관련 영역: 17. 작업 대상·자산 식별과 인계 추적, 51. 인증·권한·격리, 63. 병원·의료 | 근거: f40 | 종류: 일반
- 사람 존재 정보로 세계 상태 정보의 확실도를 낮추는 방식을 물류창고·병원 같은 이동로봇 현장의 문·통로·적재물 상태 판단에 적용한 연구나 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 19. 사람·보행자 모델, 31. 사람–로봇 협업 | 근거: f28 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 40 · 교차 확인: 0
- 예산 사용량: 검색 7회 · 신규 출처 4건
- 미확인 항목:
    - f2 Naqvi 외 논문 본문 미열람(PMC·HAL 봇 차단), 검색 요약 기준
    - f4 MCP 연동이 로봇·플릿 상태 질의 도구까지 제공하는지 미확인(발표 안내문에 없음)
    - f40 Zena RX 의 수령 기록·감사 로그 기능 미확인(aethon.com/healthcare-eu 404), 벤더 주장이며 독립 확인 없음
    - f41·f42 딜리타워 수령 방식이 2019(전화번호 뒤 네 자리, 사무 건물)과 2020(비밀번호, 공동주택 계획) 보도에서 다름 — 시점·현장이 달라 출처 충돌로 올리지 않았고 현재 운영 방식은 미확인
    - f28 Riedelbauch 외 PDF 본문 추출 실패, 초록 기준
    - 18·19 ↔ 45. 문서·도면·장면 이해(oq-227) 연결 근거 미확보 — 검색 결과에 고정 카메라·로봇 인식 결합 연구가 있었으나 원문을 열지 않아 넣지 않음
    - A. 기획·사업과의 연결 근거 미확보
- 범위 경계 위반 의심:
    - f36: 승강기 화재·비상 모드 제어와 설비 안전은 분류 원문 19장 시설·설비 제어 경계의 연계 대상, ROP 는 모드 확인만으로 서술
    - f37: 사람 검출·안전 정지·국소 회피는 로봇 자체 지능·제어의 연계 대상으로 구분
    - f48: 인파관리지원시스템은 외부 공공 시스템(연계 대상: 표시)
    - f40: 로봇 본체 잠금 칸·생체 인식은 제조사 기능(벤더 주장), ROP 몫은 인증 결과 수신·기록으로 한정해야 함
    - f14: 소매 매장 재고 기록 부정확성은 물류센터 값이 아님을 명시
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결 실행으로 근거를 게시된 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 19. 사람·보행자 모델 페이지와 다른 대분류 페이지(A·B·F·G)의 검증된 주장·각주에서 먼저 찾고(재사용 36건), 빈 연결(C. 채팅 기반 구성·운영, N. 보안·개인정보의 수령인 인증, H. 실행·협업·예외 복구의 31. 사람–로봇 협업)만 새로 조사했다. 검색 7회/30, 신규 출처 4건/15(ref-1299~ref-1302, 예약 구간 안). 재사용 출처 ref-854 는 이번에 원문을 다시 열었다. 원문 열람: github_raw 로 ref-051·ref-148·ref-285·ref-286·ref-1173 을, webfetch 로 ref-854·ref-1265·ref-1299~ref-1302 를 열었다. 나머지 재사용 출처는 이번에 다시 열지 않았다(fetched false). 이전 분류 기준 대분류 연결 절(A·B·F·G 페이지, 옛 E 연결 브리프 2026-09-25-60)에서 재인용한 finding 은 evidence_excerpt 끝에 재인용 실행 id 를 적었다. 교차 확인 0건. 벤더 주장 1건(f40). 한국어 검색 2회(딜리타워·아파트 배송로봇), 국내 자료는 바이라인네트워크·경향신문·정책브리핑(재사용)·조선비즈(재사용). 현장 유형은 물류창고(f9)·병원(f10·f40)·상업 시설(f14)·기타(f22·f41)·가정(f42)·실외(f45·f46·f48)로 나눴다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 f30·f21 에서 구분했다. L. AI·학습 기술 연결은 f35(46. 예측·학습 기반 최적화)뿐이며 적용 대상 19. 사람·보행자 모델과 함께 제안했다. 새 용어 후보 없음(관련 용어가 용어집에 이미 있음). 기존 열린 질문은 해결하지 못했다(oq-180·oq-184 는 f41·f42 가 수령 인증 수단만 부분 근거로 제공, 완료 이벤트 기록 방식은 미확인). 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/2026-09-30-24/research.md

```markdown
# 리서치 브리프 2026-09-30-24

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-24 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 60. 노동·수용성·접근성 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 기술 수용 모델(UTAUT·Almere 모델), 노사협의·공동결정, 근로자 감시 설비, 무인정보단말기 접근성, 연석 경사로 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고(부상·감시 우려), 병원(작업 흐름 적합성·종사자·환자 만족도), 실외(휠체어 이용자와 보도 로봇) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 수용성 측정 모델, 참여 설계(co-design), 직무 설계, 노동자 참여 절차 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO/IEC Guide 71, 장애인차별금지법 무인정보단말기 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음 — 로봇의 고용·임금 효과(미국·한국), 창고 로봇과 부상, 병원 로봇 민족지 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-146, oq-188, oq-266 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]
2. 로봇 도입은 고용·임금과 일하는 방식(작업 속도·부상·직무 내용)을 어떻게 바꾸는가(미국·한국 실증 연구, 물류창고 부상 자료)? (섹션 3·5·8 겨냥)
3. 일하는 사람과 이용하는 사람의 로봇 수용성은 어떤 모델로 측정하고, 어떤 요인(작업 흐름 적합성, 감시·데이터, 사회적 상호작용)이 좌우하는가(병원·돌봄·물류창고 사례)? (섹션 4·5·6 겨냥)
4. 고령자·장애인·어린이가 로봇 서비스를 안전하게 쓰고 피할 수 있게 하는 표준·법 의무(ISO/IEC Guide 71, 장애인차별금지법 무인정보단말기 접근성)는 무엇인가? (섹션 7 겨냥, 한국 자료 우선)
5. 보도 로봇이 휠체어 이용자 등 보행 약자의 통행을 막지 않게 하는 설계·운영 기준이나 사례가 있는가? (섹션 5·6 겨냥, oq-188 관련)
6. 로봇 도입과 작업자 데이터 수집에 노동자 참여·협의를 요구하는 법 절차(한국 근로자참여법, 독일 사업장조직법)는 무엇인가? (섹션 6·7 겨냥, oq-266 관련)
7. 노동·수용성·접근성에서 ROP가 직접 맡을 것과 사용자·노사·제조사·법무에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU-OSHA(유럽 산업안전보건청)는 2022-06-16 보고서 'Advanced robotics and automation: implications for occupational safety and health'에서 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다뤘다. | ref-1277 | 아니오 | medium | 2022-06-16 | — | — |
| f2 | [추정] | EU-OSHA 게시 페이지 요약은 첨단 로봇의 심리사회적 위험으로 고용 불안, 작업 강도 증가, 의사결정 자율성 감소, 탈숙련, 로봇에 대한 신뢰 문제를 들고, 도입 결정에 노동자 참여·인간 중심 설계·교육을 권고하는 것으로 보인다. | ref-1277 | 아니오 | low | 2022-06-16 | 예외·성과 | — |
| f3 | [사실] | 물류창고 사례(미국 아마존 풀필먼트 센터): Burtch·Greenwood·Ravindran(ILR Review, 2025)은 로봇 풀필먼트 센터에서 기존 센터보다 중대 부상이 40% 줄고 비중대 부상이 77% 늘었다고 보고했고, 작업자 온라인 게시글에서는 로봇 센터의 피킹 목표량이 2~3배 높다는 진술이 나왔다. | ref-1264 | 아니오 | medium | 2025-08-26 | 물류창고 / 예외·성과 | — |
| f4 | [의견] | 같은 연구진은 창고 자동화가 위험 작업을 없애는 대신 남은 작업의 다양성을 줄이고 작업 속도를 높여 반복성 긴장 손상 같은 비중대 부상을 늘리므로, 위험이 사라지기보다 재분배되며 직무 설계로 대응해야 한다고 해석한다. | ref-1264 | 아니오 | medium | 2025-08-26 | 물류창고 / 제약 | — |
| f5 | [사실] | 물류창고 사례: Malik·Brandão·Coopamootoo(International Journal of Social Robotics, 2026)는 창고 작업자 12명 반구조화 면담에서 로봇 운영에 딸린 데이터 감시에 대한 우려와 더 주체적인 협업에 대한 요구를 확인하고, 수동 무시(override)·개인정보 통제·감시 활동 알림 같은 작업자 중심 요구를 제시했다. | ref-1278 | 아니오 | medium | 2026 | 물류창고 / 제약 | — |
| f6 | [사실] | Acemoglu·Restrepo(NBER 작업논문 w23285, 2017-03; Journal of Political Economy 2020 게재)는 1990~2007년 미국 통근권역 자료로 노동자 1천 명당 로봇 1대가 늘면 고용률이 약 0.18~0.34%p, 임금이 0.25~0.5% 낮아진다고 추정했다. | ref-1275 | 아니오 | medium | 2017-03 | — | — |
| f7 | [사실] | 한국노동연구원 보고서 '기술 혁신과 노동시장 변화'(2024-12)를 전한 보도에 따르면, 노동자 1천 명당 로봇 6.6대 증가(로봇 노출도 한 단계)마다 고숙련 제조업 노동자의 임금은 2.5%, 고용률은 0.55%p 올랐으나 저숙련 제조업 노동자 임금은 4.5~4.9% 줄었고 45~54세 고용률은 0.37%p 낮아졌다. | ref-1266, ref-1267 | 아니오 | low | 2025-04-01 | — | — |
| f8 | [사실] | 병원 사례(미국): Mutlu·Forlizzi(HRI 2008)의 자율 배송 로봇 TUG 민족지 연구에서 내과 병동은 방해에 대한 낮은 허용도, 인식된 비용과 이득의 불일치, 붐비는 통로의 운행 중단 때문에 로봇이 작업 흐름을 해치고 직원 저항을 불렀지만 산후 병동은 로봇을 작업 흐름과 사회적 맥락에 통합했다. | ref-1151 | 아니오 | medium | 2008 | 병원 / 예외·성과 | — |
| f9 | [사실] | 병원 사례(한국): 한림대성심병원은 2022-08~2024-12 의료서비스로봇 11종 77대를 도입해 51,092건을 사용했고, 2023년 하반기 간호사 109명 조사에서 90% 이상이 단순업무 경감, 94%가 계속 사용을 희망했으며, 입원환자 147명 중 93.9%가 영상 안내가 도움이 됐고 99%가 로봇에 거부감이 없다고 답했다고 보도됐다. | ref-1274 | 아니오 | low | 2025-01-21 | 병원 / 예외·성과 | — |
| f10 | [사실] | Heerink 외(International Journal of Social Robotics 2(4), 2010)의 Almere 모델은 통합 기술 수용 이론(UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하며, 요양시설과 가정에서 세 가지 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다. | ref-1269 | 아니오 | medium | 2010 | — | — |
| f11 | [사실] | 김소라(주관성 연구 63, 2023)는 Q방법론으로 노인 이용자·가족·돌봄서비스 종사자의 돌봄로봇 인식을 '불가피한 대체재', '상호보완적 동반자', '열등한 보조재', '불완전한 경쟁자'의 네 유형으로 나눴다. | ref-1273 | 아니오 | medium | 2023 | — | — |
| f12 | [사실] | 실외 사례(미국): Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명 면담, 4회의 공동설계 워크숍으로 보도 로봇이 들어오면 이동장애인이 보도 공간을 두고 경쟁한다고 느끼고, 실무자는 기업이 문제가 생긴 뒤에야 접근성을 다룬다고 인정했으며, 두 집단 모두 처음부터 접근성을 통합해야 한다고 보았음을 보고했다. | ref-1265 | 아니오 | medium | 2024-04-07 | 실외 / 제약 | — |
| f13 | [사실] | 같은 연구가 출발점으로 삼은 사례에서 배송 로봇이 연석 경사로에 멈춰 휠체어 이용자의 횡단 후 통행을 막았고 이용자가 이를 공개하자 업체가 로봇 운행을 잠시 중단했으며, 참여자들은 연석 경사로로 다가오는 사람을 감지하면 로봇이 자동으로 경로를 다시 계획하고 스스로 비켜 주차하는 기능을 제안했다. | ref-1265 | 아니오 | medium | 2024-04-07 | 실외 / 예외·성과 | — |
| f14 | [사실] | ISO/IEC Guide 71:2014(2판, 2014-12)는 사람이 쓰는 제품·서비스·건축 환경을 다루는 표준에 접근성 요구를 넣도록 표준 개발자에게 지침을 주며 장애인·어린이·고령자의 접근성 요구를 주로 다룬다. | ref-1276 | 아니오 | medium | 2014-12 | 제약 | 원문 미열람 |
| f15 | [사실] | 한국에서는 2026-01-28부터 무인정보단말기를 설치·운영하는 모든 사업자가 디지털 접근성 지침의 검증 기준을 충족하는 장애인 접근 가능 기기를 제공해야 하며, 바닥면적 50㎡ 미만 시설·소상공인·테이블 주문형 기기는 보조기기·보조 인력·호출벨 등으로 대신할 수 있고, 위반은 장애인 차별에 해당한다. | ref-1268 | 아니오 | medium | 2026-01-28 | 제약 | — |
| f16 | [사실] | 한국 근로자참여 및 협력증진에 관한 법률 제20조 제1항은 노사협의회가 협의할 사항으로 근로자의 채용·배치 및 교육훈련(제2호), 신기계·기술의 도입 또는 작업 공정의 개선(제9호), 사업장 내 근로자 감시 설비의 설치(제14호)를 둔다. | ref-1272 | 아니오 | medium | 2019-07-17 | 시작 조건 | — |
| f17 | [사실] | 독일 사업장조직법(BetrVG) 제87조 제1항 제6호는 법률·단체협약 규정이 없는 한 노동자의 행동이나 성과를 감시하도록 정해진 기술 장치의 도입과 적용에 사업장협의회의 공동결정권을 두고, 합의가 안 되면 중재위원회(Einigungsstelle)가 결정한다. | ref-1271 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f18 | [추정] | f5·f16·f17을 종합하면 로봇 작업과 연결해 개별 작업자의 처리량·위치·행동 데이터를 남기는 오케스트레이션 기능은 한국에서는 노사협의회 협의 사항(신기계 도입, 근로자 감시 설비), 독일에서는 공동결정 대상 감시 장치로 다뤄질 수 있어 도입 전에 노동자 참여 절차가 필요할 가능성이 있으나, 해당 여부는 법적 판단으로 확인하지 못했다. | ref-1278, ref-1272, ref-1271 | 아니오 | low | 2026-09-30 | 제약 | — |
| f19 | [추정] | 확인한 자료를 종합하면 핵심 질문(로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가)의 답은 한 가지가 아니며, 일하는 사람 쪽은 작업 흐름 적합성(f8)·작업 속도와 직무 설계(f3·f4)·데이터 감시(f5)·고용과 숙련 효과(f6·f7)가, 이용하는 사람 쪽은 사회적 상호작용 요인(f10·f11)과 보행 약자의 공간·접근성(f12·f13·f15)이 수용 여부를 가르는 것으로 보이고, 기관 자체 설문은 높은 만족도를 보고한다(f9). | ref-1151, ref-1264, ref-1278, ref-1275, ref-1266, ref-1269, ref-1273, ref-1265, ref-1268, ref-1274 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 60. 노동·수용성·접근성에서 ROP가 직접 맡을 범위는 로봇과 사람의 작업 분담·작업 속도(목표량) 설정을 드러내고 조정할 수 있게 하는 것, 작업자 데이터 수집 범위 표시·감시 알림·수동 무시 같은 작업자 통제 수단을 제공하는 것, 연석 경사로·통로에서 보행 약자에게 양보하고 멈추지 않는 대기 위치 규칙을 경로·작업 제약으로 반영하는 것, 운영자·이용자 화면의 접근성을 갖추는 것으로 보인다. | ref-1264, ref-1278, ref-1265, ref-1268 | 아니오 | low | 2026-09-30 | 제약 | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 고용·임금·재교육 정책, 노사협의·공동결정 절차와 근로자 감시 설비의 적법성 판단(사업주·노동자 대표·법무), 장애인차별금지법 등 접근성 법적 적합성 판단(운영자·법무), 로봇 본체의 물리적 접근성 설계(높이·음성 조작 등 제조사)는 외부가 맡고, ROP는 그 결정을 작업·경로·권한 제약과 화면 설계로 받아 반영하고 근거 기록을 제공하는 쪽인 것으로 보인다. | ref-1272, ref-1271, ref-1268, ref-1265, ref-1266 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f22 | [추정] | 이 영역은 작업 분담·속도의 31. 사람–로봇 협업과 25. 작업 배정 — MRTA(f3·f4), 부상의 49. 사람 근접 안전(f3), 작업자 데이터 감시의 53. 개인정보·영상 데이터(f5·f18), 보행 약자와 대기 위치의 19. 사람·보행자 모델과 16. 장소 의미·지도 관리(f12·f13), 목표량 지표의 39. 운영 성과 측정·개선(f3), 교육·도입 절차의 56. 운영 이관·확대·교육(f2·f8), 화면 접근성의 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반(f15), 법 의무의 59. 법·규제·보험·라이선스(f15·f16·f17), 효과 추정의 3. 경제성·조달·사업 모델(f6·f7), 적용 현장인 61. 물류창고·63. 병원·의료·66. 실외(f3·f5·f8·f9·f12)와 이어진다. | ref-1264, ref-1278, ref-1265, ref-1277, ref-1151, ref-1268, ref-1272, ref-1271, ref-1275, ref-1266, ref-1274 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1264 | George Mason University Costello College of Business | Warehouse automation hasn't made workers safer — it's just reshuffled risk | 2025-08-26 | 정부·연구기관 | medium | 2026-09-30 | https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk | 아니오 |
| ref-1265 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | high | 2026-09-30 | https://arxiv.org/abs/2404.05050 | 아니오 |
| ref-1266 | 한국경제 | 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인) | 2025-04-01 | 기사 | low | 2026-09-30 | https://www.hankyung.com/article/2025040138391 | 아니오 |
| ref-1267 | 한국노동연구원 (국회 정책정보 포털 NABIS 게재) | 기술 혁신과 노동시장 변화 | 2024-12 | 정부·연구기관 | medium | 2026-09-30 | https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861 | 아니오 |
| ref-1268 | 대한민국 정책브리핑 (보건복지부) | 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행 | 2026-01-28 | 정부·연구기관 | high | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148958690 | 아니오 |
| ref-1269 | Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics) | Assessing acceptance of assistive social agent technology by older adults: the Almere model | 2010 | 논문 | medium | 2026-09-30 | https://doi.org/10.1007/s12369-010-0068-5 | 아니오 |
| ref-1151 | Mutlu, B., Forlizzi, J. (HRI 2008) | Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction | 2008 | 논문 | medium | 2026-09-30 | https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf | 아니오 |
| ref-1271 | Bundesministerium der Justiz (gesetze-im-internet.de) | Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.gesetze-im-internet.de/betrvg/__87.html | 아니오 |
| ref-1272 | 대한민국 국회 (법률 제16320호, 케이스노트 게재) | 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) | 2019-04-16 | 정부·연구기관 | medium | 2026-09-30 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0 | 아니오 |
| ref-1273 | 김소라 (주관성 연구, 한국주관성연구학회) | 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구 | 2023 | 논문 | medium | 2026-09-30 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146 | 아니오 |
| ref-1274 | 의협신문 | "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파 | 2025-01-21 | 기사 | low | 2026-09-30 | https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208 | 아니오 |
| ref-1275 | Acemoglu, D., Restrepo, P. (NBER) | Robots and Jobs: Evidence from US Labor Markets | 2017-03 | 논문 | medium | 2026-09-30 | https://www.nber.org/papers/w23285 | 아니오 |
| ref-1276 | ISO/IEC | ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards | 2014-12 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/57385.html | 예 |
| ref-1277 | European Agency for Safety and Health at Work (EU-OSHA) | Advanced robotics and automation: implications for occupational safety and health | 2022-06-16 | 정부·연구기관 | medium | 2026-09-30 | https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health | 아니오 |
| ref-1278 | Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics) | Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety | 2026 | 논문 | medium | 2026-09-30 | https://doi.org/10.1007/s12369-026-01359-1 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(핵심 질문 답, 추정), f3·f4(위험 재분배), f6·f7(고용·임금 효과), f12(보행 약자 공간 경쟁) / 섹션 4: 기술 수용 모델 UTAUT·Almere 모델 f10, 돌봄로봇 인식 유형 f11, 노사협의 협의 사항·근로자 감시 설비 f16, 공동결정 f17, 무인정보단말기 접근성 f15, 연석 경사로 f13, 접근성 대상 집단 f14 / 섹션 5: 물류창고 — f3(예외·성과), f4·f5(제약), 병원 — f8(예외·성과, 미국), f9(예외·성과, 한국), 실외 — f12(제약)·f13(예외·성과). 제조 공장·상업 시설·가정 사례는 찾지 못했음을 명시(f7 은 현장 사례가 아니라 산업 통계) / 섹션 6: 수용성 측정 모델 f10·f11, 참여 설계 f12·f13, 직무 설계 f4, 노동자 참여 절차 f2·f16·f17·f18 / 섹션 7: ISO/IEC Guide 71 f14(원문 미열람), 장애인차별금지법 무인정보단말기 의무 f15, 근로자참여법 제20조 f16, 독일 사업장조직법 제87조 f17 / 섹션 8: f1·f3·f6·f7·f8·f10·f12 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66 / 섹션 11: 기존 oq-146·oq-188·oq-266(모두 미해결 유지; oq-188 은 f13 이 해외 사례만 제공, oq-266 은 f8 이 병동 단위 차이만 제공)과 open_questions_new 4건. 다음 실행 후보: 61. 물류창고 페이지에 f3·f5, 66. 실외 페이지에 f12·f13, 63. 병원·의료 페이지에 f8·f9 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 통합 기술 수용 이론 | Unified Theory of Acceptance and Use of Technology (UTAUT) | 성과 기대·노력 기대·사회적 영향·촉진 조건으로 기술 사용 의도와 실제 사용을 설명하는 기술 수용 모델로, 로봇 수용성 연구의 출발점으로 널리 쓰인다. |
| 알메러 모델 | Almere Model | UTAUT 에 사회적 존재감·신뢰 같은 사회적 상호작용 변수를 더해 고령자의 보조 소셜 로봇·에이전트 수용성을 측정하도록 만든 모델이다(Heerink 외, 2010). |
| 무인정보단말기 접근성 | Kiosk Accessibility (Unmanned Information Terminal Accessibility) | 키오스크 같은 무인정보단말기를 시각·이동 등 장애가 있는 사람도 동등하게 쓸 수 있게 하는 요건으로, 한국은 장애인차별금지법에 따라 2026-01-28부터 모든 설치 사업자에게 의무화했다. |
| 연석 경사로 | Curb Cut (Curb Ramp) | 보도와 차도 사이 턱을 경사로로 낮춘 부분으로, 휠체어·유모차 이용자가 횡단할 때 반드시 지나야 하므로 로봇이 이곳에 멈추면 통행을 막는다. |

## 열린 질문

새로 생긴 질문:

- 서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가? | 관련 영역: 60. 노동·수용성·접근성, 59. 법·규제·보험·라이선스, 64. 상업 시설 | 근거: f15 | 종류: 일반
- 오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가? | 관련 영역: 60. 노동·수용성·접근성, 53. 개인정보·영상 데이터, 59. 법·규제·보험·라이선스 | 근거: f18 | 종류: 일반
- 로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 31. 사람–로봇 협업, 25. 작업 배정 — MRTA | 근거: f3 | 종류: 일반
- 국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 63. 병원·의료, 61. 물류창고 | 근거: f9 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 15건
- 미확인 항목:
    - f2 EU-OSHA 보고서 PDF 본문이 읽히지 않아 심리사회적 위험 목록과 권고를 원문에서 확인하지 못함(게시 페이지 요약 기준, 추정·low)
    - f3 ILR Review 논문 원문(SAGE·SSRN 403) 미열람 — 대학 뉴스 기준이며 데이터 출처(OSHA 사업장 부상 보고 2016~2020)는 검색 요약에만 있어 claim 에서 뺌
    - f6 JPE 게재본 수치(고용률 0.2%p·임금 0.42%)는 검색 요약에만 있어 NBER 작업논문 범위값으로 적음
    - f7 한국노동연구원 보고서 수치는 보도 기준이며 보고서 원문 미열람. 저자 한글 이름 미확인
    - f9 간호사 조사 표본이 보도마다 다름(109명 90% 이상 / 병동 99명 91.9%) — 두 보도가 같은 병원 발표에서 나와 독립 교차 확인 불가
    - f14 ISO/IEC Guide 71 원문·ISO 페이지 403 으로 미열람
    - f16 국가법령정보센터 본문이 열리지 않아 법령 게재 사이트로 확인
    - 시각장애인과 공원 청소 로봇 현장 연구(ACM 2026, 10.1145/3776734.3794493)는 ACM 403 과 출처 상한으로 넣지 않음
    - oq-146(국내 음성 지시 인식률)·oq-188(국내 대기 위치·점자블록 기준)·oq-266(운영 책임 조직 비교) 근거를 찾지 못함
    - 제조 공장·상업 시설·가정 현장의 노동·수용성·접근성 사례 미확인
- 범위 경계 위반 의심:
    - f6·f7: 로봇의 고용·임금 효과는 노동시장 정책 영역이므로 배경 근거로만 쓰고 ROP 직접 범위로 서술하지 않음(f21 연계 대상)
    - f16·f17·f18: 노사협의·공동결정 절차와 감시 설비 적법성 판단은 사업주·노동자 대표·법무의 몫이며 59. 법·규제·보험·라이선스와 겹치므로 규칙 목록으로만 제안
    - f15: 접근성 법 의무 적합성 판단은 운영자·법무 몫이며 로봇에 적용되는지는 열린 질문으로 보냄
    - f13: 로봇 본체의 물리적 접근성 설계(높이 조절·음성 조작)는 제조사 영역이므로 ROP 몫은 경로·대기 위치 제약으로 한정(f20·f21)
- 한계: web_fetch_available: true · fetch_mode full. 검색 20회/30, 신규 출처 15건/15(ref-1264~ref-1278, 예약 구간 안)로 신규 출처 상한에 도달해 시각장애인·공공 로봇 현장 연구, 제조 공장 사례 추가 조사를 하지 못했다. 재사용 출처 없음(참고문헌 목록 요약에 이 영역 인용 0건). 원문 열람: 15건 중 14건을 webfetch 로 열었고 ISO/IEC Guide 71(ref-1276)만 403 으로 미열람이다. 다만 ref-1269·ref-1273·ref-1278 은 초록만, ref-1151 은 PDF 일부만, ref-1277 은 게시 페이지만 읽었다. 교차 확인 0건(한림대성심병원 수치는 같은 병원 발표에서 나온 두 보도라 독립 아님). 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '한 가지 답은 없고, 일하는 사람 쪽은 작업 흐름 적합성·작업 속도·데이터 감시·고용 효과가, 이용하는 사람 쪽은 사회적 상호작용과 보행 약자 접근성이 수용을 가르며 기관 자체 설문은 높은 만족을 보고한다'는 추정이다. 현장 유형 사례는 물류창고(f3·f4·f5, 미국·영국계 연구), 병원(f8 미국, f9 한국), 실외(f12·f13 미국)이고 돌봄(f10·f11)은 출처가 현장 유형을 하나로 밝히지 않아 null 로 두었다. 제조 공장·상업 시설·가정 사례는 찾지 못했다. 국내 자료는 한국경제·국회 정책정보(한국노동연구원 보고서)·정책브리핑·근로자참여법·KCI 논문·의협신문이다. 기존 열린 질문 oq-146·oq-188·oq-266 은 해결하지 못했다(oq-188 은 f13 이 해외 연석 경사로 사례만, oq-266 은 f8 이 병동 단위 수용 차이만 제공). L. AI·학습 기술 관련 finding 은 없고, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 역할 모호성·자동화 편향·공공 영역 이동로봇·서비스 삼자 관계·이동형 영상정보처리기기는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### data/source_texts/ref-406.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Simulation

This chapter describes how to generate building models from
`traffic_editor` files, and then simulate fleets of robots in those models.

## Motivation

Simulation environments for testing robotic solutions offer immense value across
various stages of R&D and deployment. More notably, simulations provide the
following benefits:

- **Time and resource saving:** While testing with hardware is indispensable,
  the process can slow development with additional setup time, robot
  downtime and reset periods between trials. As the number of participants
  scale, so do costs associated with purchasing hardware and consumables for
  testing. This is especially true when utilizing a solution such as RMF, which aims to
  integrate several mobile/stationary robots together with building systems such as doors
  and lifts. Simulations provide a potentially cost-effective and time-saving alternative
  for evaluating the behavior of robot systems at scale. More importantly,
  simulations can help answer questions prior to deployment such as how many
  participants can be supported or how the existing behavior would change with
  the introduction of a new fleet, both of which can inform purchasing decisions
  for facility owners.

- **Robust testing:** Robots in simulation neither run out of battery nor incur costs when they happen to unfortunately crash into something. Scenarios
  can be tested for hours at a stretch, at faster speeds, to fine tune
  algorithms and verify their robustness. One consideration about the appropriate amount of scenario testing to run is a decision that depends on how much compute power you want to avail for the simulation. With the introduction of cloud simulation, this limit is then a trade off of cost and speed as well. As scenarios in simulation are
  repeatable, fixes for undesirable bugs encountered can be readily validated.
  Reaction of the system to edge cases which are rare but have severe
  consequences can also be studied through simulation. Data logged from hardware
  trials can be used to recreate the scenario in simulation which may be further
  helpful for debugging. Lastly, long running simulations can instill confidence
  in facility owners prior to deployment.

Physics-based simulators, such as `Gazebo`, carry the benefit of easily
interfacing with ROS 2 nodes through wrappers provided by `gazebo_ros_pkgs`.
Gazebo plugins can be developed that accurately emulate the behavior of robots,
sensors and infrastructure systems which enhance the overall fidelity of
simulations. It is worth emphasizing here that the exact same code used to run the simulations
will also be run on the physical system as well without any changes.

However, despite these compelling benefits, simulations are sparingly employed
by developers and system integrators, citing complexity over generating
environments and configuring them with appropriate plugins. In a recent publication "_A Study on the Challenges of Using Robotics Simulators for Testing_," by Afsoon Afzal, Deborah S. Katz, Claire Le Goues and Christopher S. Timperley they noted the main reasons participants gave for not using simulation for a particular project and summarized their findings as follows:

| Reason for not using simulation  | #  | %  |
|---|---|---|
| Lack of time or resources | 15 | 53.57% |
| Not realistic/accurate enough | 15 | 53.57% |
| Lack of expertise or knowledge on how to use software-based simulation | 6  | 21.43% |
| There was no simulator for the robot | 4  | 14.29% |
| Not applicable | 4  | 14.29% |
| Too much time or compute resources | 2  | 7.14%  |
| Nobody suggested it | 0  | 0.00%  |
| Other | 2  | 7.14%  |

The RMF project aims to address these hurdles by simplifying the process of setting up
simulation environments for multi-fleet traffic control, as we will explain further throughout this section.

## Building Map Generator
`traffic_editor`, discussed in the previous chapter, is a tool to annotate building
floor plans with fleet-specific traffic information in a vendor neutral manner.
This includes waypoints of interest, traffic lanes and shared resources such as
doorways and lifts. It can also be used to markup the walls and floors and add
thumbnails of artifacts in the environment. The ability to auto-generate a 3D
world using this annotated map is significantly valuable for simplifying the
creation and management of simulations. To this end, the `building_map_tools`
package in `traffic_editor` contains an executable `building_map_generator`. The
executable operates in two modes:

1. Generate a Gazebo/Ignition compliant `.world` file
2. Export the fleet specific traffic information in the form
of navigation graphs which are utilized by `fleet_adapters` for planning

![Building map generator](images/building_map_generator.png)

To auto-generate a Gazebo simulation world, the executable takes in the command argument `gazebo` along with others described below:

```bash
usage: building_map_generator gazebo [-h] [--TEMPLATE_WORLD_FILE TEMPLATE_WORLD_FILE]
                                     INPUT OUTPUT_WORLD OUTPUT_MODEL_DIR

positional arguments:
  INPUT                 Input building.yaml file to process
  OUTPUT_WORLD          Name of the .world file to output
  OUTPUT_MODEL_DIR      Path to output the map model files

options:
  -h, --help            show this help message and exit
  --TEMPLATE_WORLD_FILE TEMPLATE_WORLD_FILE
                        Specify the template for the base simulation.
```

The script parses the `.building.yaml` file and generates meshes for the
flooring and walls for each level. Those meshes are then combined into a `model.sdf` file in
the `OUTPUT_MODEL_DIR/` directory. The `model.sdf` files for each level are
imported into the `.world` with filepath `OUTPUT_WORLD`. Model sub-elements for
various static objects annotated in the `traffic_editor` are included in the
`.world` as seen in the snippet below:

```xml
<include>
  <name>OfficeChairBlack_6</name>
  <uri>model://OfficeChairBlack</uri>
  <pose>4.26201267190027 -7.489812761393875 0 0 0 1.1212</pose>
  <static>True</static>
</include>
```

Similar blocks for annotated robots are
generated. It is the responsibility of the user to append the environment
variable `$GAZEBO_MODEL_PATH` with the relevant paths to the models prior to
loading the `.world` file in Gazebo. This process can be simplified through ROS 2
launch files and will be discussed in later sections.

The parser also includes sdf elements for other dynamic assets such as doors and
lifts. Their mechanisms are discussed in the next section.

By default, the simulation world is loaded without any additional plugins. So if
you were to spawn things like cameras or lidars in your gazebo world it would not
work. This can be bypassed by using the `--TEMPLATE_WORLD_FILE`. This allows you
to add additional simulation assets to your world.

Reconfiguring simulation environments becomes as trivial as editing the
annotations on the 2D drawing and re-running the `building_map_generator`. This
is exceedingly useful to quickly evaluate traffic flow as the spatial
configuration in the facility changes.

To generate navigation graphs for fleet adapters, the `building_map_generator`
is executed with command argument `nav`. The navigation graph is generated as
a `.yaml` file and is parsed during launch by the corresponding fleet adapter.

```bash
usage: building_map_generator nav [-h] INPUT OUTPUT_DIR

positional arguments:
  INPUT       Input building.yaml file to process
  OUTPUT_DIR  Path to output the nav .yaml files
```

## RMF Assets and Plugins

Assets play a pivotal role in recreating environments in simulation. Projects
such as RMF, SubT and others have allowed developers to create and open source
3D models of robots, mechanical infrastructure systems and scene objects.
They are available for download on the [Ignition Fuel app](https://app.ignitionrobotics.org/OpenRobotics/fuel/collections/).
Beyond imparting visual accuracy, assets can be dynamic and interface with RMF
core systems through the aid of plugins.

To simulate the behavior of hardware such as robot models and infrastructure
systems, several Gazebo plugins have been architected. These plugins are
derivatives of the [ModelPlugin](http://osrf-distributions.s3.amazonaws.com/gazebo/api/dev/classgazebo_1_1ModelPlugin.html)
class and tie in standard ROS 2 and RMF core messages to provide necessary
functionality. The following sections briefly describe some of these plugins.

### Robots
As highlighted earlier, several robot models (SESTO, MiR100, Magni, Hospi) have been
open sourced for use in simulation. For these models to emulate the behavior of
their physical counterparts which have been integrated with RMF, they need to 1)
interface with `rmf_fleet_adapters` and 2) navigate to locations in the
simulated world. These functionalities, for a "_full control_" robot type, are
achieved through the `slotcar` [plugin](https://github.com/open-rmf/rmf_simulation/blob/main/rmf_robot_sim_gazebo_plugins/src/slotcar.cpp).
The plugin subscribes to `/robot_path_requests` and `/robot_mode_requests`
topics and responds to relevant `PathRequest` and `ModeRequest` messages
published by its `rmf_fleet_adapter`. The plugin also publishes the robot's
state to the `/robot_state` topic.

To navigate the robot through waypoints in a `PathRequest` message, a simple
"rail-like" navigation algorithm is utilized which accelerates and decelerates
the robot along a straight line from its current position to the next waypoint.
The plugin relies on these fundamental assumptions:
  * The robot model is a two-wheel differential drive robot
  * The left and right wheel joints are named  `joint_tire_left` and `joint_tire_right` respectively

Other parameters, the majority of which are kinematic properties of the robot, are inferred from sdf parameters:
```xml
<plugin name="slotcar" filename="libslotcar.so">
  <nominal_drive_speed>0.5</nominal_drive_speed>
  <nominal_drive_acceleration>0.25</nominal_drive_acceleration>
  <max_drive_acceleration>0.75</max_drive_acceleration>
  <nominal_turn_speed>0.6</nominal_turn_speed>
  <nominal_turn_acceleration>1.5</nominal_turn_acceleration>
  <max_turn_acceleration>2.0</max_turn_acceleration>
  <tire_radius>0.1</tire_radius>
  <base_width>0.3206</base_width>
  <stop_distance>0.75</stop_distance>
  <stop_radius>0.75</stop_radius>
</plugin>
```

During simulation, it is assumed that the robot's path is free of static
obstacles, but the plugin still contains logic to pause the robot's motion if an
obstacle is detected in its path. While it is possible to deploy a sensor based
navigation stack, the approach is avoided to minimize the computational load on
the system from running a navigation stack for each robot in the simulation.
Given the focus on traffic management of heterogeneous fleets and not robot
navigation, the `slotcar` plugin provides an efficient means to simulate the
interaction between RMF core systems and robots.

The `slotcar` plugin is meant to serve as a generalized solution. Vendors are
encouraged to develop and distribute plugins that represent the
capabilities of their robot and the level of integration with RMF more accurately.

### Doors
Unlike robot models whose geometries are fixed and hence can be directly
included in the generated `.world` file, doors are custom defined in
`traffic_editor` and have their own generation pipeline. As seen in the figure
below, an annotated door has several properties which include the location of
its ends, the type of door (hinged, double_hinged, sliding, double_sliding) and
its range of motion (for hinged doors).

![Door properties](images/door_traffic_editor.png)

The `building_map_generator gazebo` script parses a `.building.yaml` file for
any doors and automatically generates an sdf sub-element with links and joints
required for the door along with a configured plugin. The sdf sub-element
generated for the door in the figure above is presented below.

```xml
<model name="coe_door">
  <pose>8.077686357313898 -5.898342045416362 0.0 0 0 1.1560010438234292</pose>
  <plugin filename="libdoor.so" name="door">
    <v_max_door>0.5</v_max_door>
    <a_max_door>0.3</a_max_door>
    <a_nom_door>0.15</a_nom_door>
    <dx_min_door>0.01</dx_min_door>
    <f_max_door>500.0</f_max_door>
    <door left_joint_name="left_joint" name="coe_door" right_joint_name="empty_joint" type="SwingDoor" />
  </plugin>
  <link name="left">
    <pose>0 0 1.11 0 0 0</pose>
    <visual name="left">
      <material>
        <ambient>120 60 0 0.6</ambient>
        <diffuse>120 60 0 0.6</diffuse>
      </material>
      <geometry>
        <box>
          <size>0.8766026166317483 0.03 2.2</size>
        </box>
      </geometry>
    </visual>
    <collision name="left">
      <surface>
        <contact>
          <collide_bitmask>0x02</collide_bitmask>
        </contact>
      </surface>
      <geometry>
        <box>
          <size>0.8766026166317483 0.03 2.2</size>
        </box>
      </geometry>
    </collision>
    <inertial>
      <mass>50.0</mass>
      <inertia>
        <ixx>20.17041666666667</ixx>
        <iyy>23.36846728119012</iyy>
        <izz>3.20555061452345</izz>
      </inertia>
    </inertial>
  </link>
  <joint name="left_joint" type="revolute">
    <parent>world</parent>
    <child>left</child>
    <axis>
      <xyz>0 0 1</xyz>
      <limit>
        <lower>-1.57</lower>
        <upper>0</upper>
      </limit>
    </axis>
    <pose>0.44330130831587417 0 0 0 0 0</pose>
  </joint>
</model>
```

The door [plugin](https://github.com/open-rmf/rmf_simulation/blob/main/rmf_building_sim_common/src/door_common.cpp) responds to `DoorRequest` messages with `door_name` matching its `model name` sdf tag. These messages are published over the `/door_requests` topic. The plugin is agnostic of the type of door defined and relies on the `left_joint_name` and `right_joint_name` parameters to determine which joints to actuate during open and close motions. During these motions, the joints are commanded to their appropriate limits which are specified in the parent element. The joint motions adhere to kinematic constraints specified by sdf parameters while following acceleration and deceleration profiles similar to the `slotcar`.

To avoid situations where one robot requests a door to close on another robot, a `door_supervisor` [node](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter/src/door_supervisor) is deployed in practice. The node publishes to `/door_requests` and subscribes to `/adapter_door_requests` which the fleet adapters publish to when their robot requires access through a door. The `door_supervisor` keeps track of requests from all the fleet adapters in the system and relays the request to the door adapters while avoiding aforementioned conflicts.

### Lifts
The ability to test lift integration is crucial as these systems are often the operational bottlenecks in facilities given their shared usage by both humans and multi robot fleets. As with annotated doors, lifts can be customized in a number of ways in the `traffic_editor` GUI including the dimension & orientation of the cabin and mapping cabin doors to building levels.

![Customizing lifts in Traffic Editor](images/lift_traffic_editor.png)

The `building_map_generator gazebo` script parses the `.building.yaml` file for lift definitions and auto-generates the sdf elements for the cabin, cabin doors and lift shaft doors.
A prismatic joint is defined at the base of the cabin which is actuated by the lift plugin to move the cabin between different levels.
While the cabin doors are part of the cabin structure, the shaft doors are fixed to the building.
Both sets of doors open and close simultaneously at a given level and are controlled by the lift plugin itself.
These doors are created using the same method as other doors in the building and include the door plugin as well.

The `building_map_generator` also appends a lift plugin (TODO add link element with required parameters to the lift's model sdf block.)

```xml
<plugin filename="liblift.so" name="lift">
  <lift_name>Lift1</lift_name>
  <floor elevation="0.0" name="L1">
    <door_pair cabin_door="CabinDoor_Lift1_door1" shaft_door="ShaftDoor_Lift1_L1_door1" />
  </floor>
  <floor elevation="10.0" name="L2">
    <door_pair cabin_door="CabinDoor_Lift1_door1" shaft_door="ShaftDoor_Lift1_L2_door1" />
    <door_pair cabin_door="CabinDoor_Lift1_door2" shaft_door="ShaftDoor_Lift1_L2_door2" />
  </floor>
  <floor elevation="20.0" name="L3">
    <door_pair cabin_door="CabinDoor_Lift1_door1" shaft_door="ShaftDoor_Lift1_L3_door1" />
  </floor>
  <reference_floor>L1</reference_floor>
  <v_max_cabin>2.0</v_max_cabin>
  <a_max_cabin>1.2</a_max_cabin>
  <a_nom_cabin>1.0</a_nom_cabin>
  <dx_min_cabin>0.001</dx_min_cabin>
  <f_max_cabin>25323.0</f_max_cabin>
  <cabin_joint_name>cabin_joint</cabin_joint_name>
</plugin>
```

The plugin subscribes to `/lift_requests` topic and responds to `LiftRequest` messages with `lift_name` matching its `model name` sdf tag.
The displacement between the cabin's current elevation and that of the `destination_floor` is computed and a suitable velocity is applied to the cabin joint.
Prior to any motion, the cabin doors are closed and only opened at the `destination_floor` if specified in the `LiftRequest` message.
As the cabin and shaft doors are configured with the `door` plugin, they are commanded through `DoorRequest` messages published by the `lift` plugin.
Analogous to the `door_supervisor`, a `lift_supervisor` [node](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter/src/lift_supervisor) is started in practice to manage requests from different robot fleets.

### Workcells

A common use case is robots performing deliveries within facilities, so a `Delivery` task is configured into the `rmf_fleet_adapters`.
In a delivery task, a payload is loaded onto the robot at one location (pickup waypoint) and unloaded at another (dropoff waypoint).
The loading and unloading of the payload onto and from a robot may be automated by robots/workcells in the facility. These devices are henceforth referred to as dispensers and ingestors respectively.

To replicate the loading and unloading processes in simulation, the `TeleportDispenser` and `TeleportIngestor` [plugins](https://github.com/open-rmf/rmf_simulation/tree/main/rmf_robot_sim_gazebo_plugins/src) have been designed.
These plugins are attached to the `TeleportDispenser` and `TeleportIngestor` [3D models](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_assets/models), respectively.
To setup a payload loading station in simulation:
* Add a `TeleportDispenser` model beside the pickup waypoint and assign it a
  unique `name`
* Add the payload model beside the `TeleportDispenser` model (Coke can in image below)

To setup a payload unloading station in simulation:
* Add a `TeleportIngestor` model beside the dropoff waypoint and assign it a
  unique `name`

When a `DispenserRequest` message is published with `target_guid` matching the
name of the `TeleportDispenser` model, the plugin will teleport the payload onto
the nearest robot model. Conversely, when an `IngestorRequest` message is published
with the `target_guid` matching the name of the `TeleportIngestor` model, the
`TeleportIngestor` plugin will teleport the payload from the robot to its location in
the world. The combinations of these plugins allow delivery requests to be simulated.
In the future, these mechanisms will be replaced by actual workcells or robot arms
but the underlying message exchanges will remain the same.

![TeleportDispenser and TeleportIngestor models](images/dispensers.png)

### Crowdsim

Crowd Simulation, aka `CrowdSim` is an optional feature in RMF simulation. User can
choose to enable crowdsim on `rmf_traffic_editor`. In RMF, the crowdsim plugin uses
[menge](https://github.com/open-rmf/menge_vendor) as the core to control each of
simulated agent in the world.

An example of crowdsim is demonstrated on rmf_demos's `airport_world`:
```bash
ros2 launch rmf_demos_gz airport_terminal.launch.xml use_crowdsim:=1
```

For more details on how `crowdsim` works and how to configure it,
please dive in to [the detailed guide for using Crowdsim](https://github.com/FloodShao/crowd_simulation/blob/master/crowd_simulation_doc/crowd_simulation_usage.md).

![crowdsim example](images/airport_crowdsim.png)

---

## Creating Simulations and Running Scenarios
The section aims to provide an overview of the various components in the `rmf_demos` [repository](https://github.com/open-rmf/rmf_demos) which may serve as a reference for setting up other simulations and assigning tasks to robots. Here, we will focus on the `office` world.

### Map package
The `rmf_demos_maps` package houses annotated `traffic_editor` files which will be used for the 3D world generation. Opening the `office.project.yaml` file in `traffic_editor` reveals a single level floorplan that has walls, floors, scale measurements, doors, lanes and models annotated. All the robot lanes are set to `bidirectional` with `graph_idx` equal to "0". The latter signifies that all the lanes belong to the same fleet. In the `airport` world, we have two sets of graphs with indices "0" and "1" which reflect laneways occupiable by two fleets respectively. The figure below highlights properties assigned to a lane and a waypoint that serves as a robot spawn location.

![Robot spawn location properties](images/rmf_demos_maps.png)

To export a 3D world file along with the navigation graphs, the `building_map_generator` script is used. The `CMakeLists.txt` file of this package is configured to automatically run the generator scripts when the package is built. The outputs are installed to the `share/` directory for the package. This allows for the generated files to be easily located and used by other packages in the demo.

```cmake
foreach(path ${traffic_editor_paths})

  # Get the output world name
  string(REPLACE "." ";" list1 ${path})
  list(GET list1 0 name)
  string(REPLACE "/" ";" list2 ${name})
  list(GET list2 -1 world_name)

  set(map_path ${path})
  set(output_world_name ${world_name})
  set(output_dir ${CMAKE_CURRENT_BINARY_DIR}/maps/${output_world_name})
  set(output_world_path ${output_dir}/${output_world_name}.world)
  set(output_model_dir ${output_dir}/models)

  # first, generate the world
  add_custom_command(
    OUTPUT ${output_world_path}
    COMMAND ros2 run rmf_building_map_tools building_map_generator gazebo ${map_path} ${output_world_path} ${output_model_dir}
    DEPENDS ${map_path}
  )

  add_custom_target(generate_${output_world_name} ALL
    DEPENDS ${output_world_path}
  )

  # now, generate the nav graphs
  set(output_nav_graphs_dir ${output_dir}/nav_graphs/)
  set(output_nav_graphs_phony ${output_nav_graphs_dir}/phony)
  add_custom_command(
    OUTPUT ${output_nav_graphs_phony}
    COMMAND ros2 run rmf_building_map_tools building_map_generator nav ${map_path} ${output_nav_graphs_dir}
    DEPENDS ${map_path}
  )

  add_custom_target(generate_${output_world_name}_nav_graphs ALL
    DEPENDS ${output_nav_graphs_phony}
  )

  install(
    DIRECTORY ${output_dir}
    DESTINATION share/${PROJECT_NAME}/maps
  )

endforeach()

```

### Launch Files
The `rmf_demos` package includes all the essential launch files required to bring up the simulation world and start various RMF services. The office simulation is launched using the `office.launch.xml` file. First, a `common.launch.xml` file is loaded and starts:
  * The `rmf_traffic_schedule` node responsible for maintaining the database of robot trajectories and monitoring traffic for conflicts. If a conflict is detected, notifications are sent to relevant fleet adapters which begin the negotiation process to find an optimal resolution.
  * The `building_map_server` which publishes a `BuildingMap` message used by UIs for visualization. The executable takes in the path to the relevant `.building.yaml` file as an argument. The `office.building.yaml` file installed by the `rmf_demos_maps` package is located using the `find-pkg-share` substitution command and is stored in the `config_file` argument.
  * The `rmf_schedule_visualizer` which is an RViz based UI to visualize the traffic lanes, actual positions of the robots, expected trajectory of robots as reflected in the `rmf_traffic_schedule` and states of building systems such as door and lifts.
  * The `door_supervisor` and `lift_supervisor` nodes to manage requests submitted by fleet adapter and UIs.

```xml
<!-- Common launch -->
<include file="$(find-pkg-share demos)/common.launch.xml">
  <arg name="use_sim_time" value="true"/>
  <arg name="viz_config_file" value ="$(find-pkg-share demos)/include/office/office.rviz"/>
  <arg name="config_file" value="$(find-pkg-share rmf_demos_maps)/office/office.building.yaml"/>
</include>
```

To launch a simulated world in gazebo, a snippet from [rmf_demos_gz](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_gz)
is shown below. Similarly, user can also choose to run with ignition
simulator, [rmf_demos_ign](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_ign)

```xml
  <group>
    <let name="world_path" value="$(find-pkg-share rmf_demos_maps)/maps/office/office.world" />
    <let name="model_path" value="$(find-pkg-share rmf_demos_maps)/maps/office/models:$(find-pkg-share rmf_demos_assets)/models:/usr/share/gazebo-9/models" />
    <let name="resource_path" value="$(find-pkg-share rmf_demos_assets):/usr/share/gazebo-9" />
    <let name="plugin_path" value="$(find-pkg-prefix rmf_gazebo_plugins)/lib:$(find-pkg-prefix building_gazebo_plugins)/lib" />

    <executable cmd="gzserver --verbose -s libgazebo_ros_factory.so -s libgazebo_ros_init.so $(var world_path)" output="both">
      <env name="GAZEBO_MODEL_PATH" value="$(var model_path)" />
      <env name="GAZEBO_RESOURCE_PATH" value="$(var resource_path)" />
      <env name="GAZEBO_PLUGIN_PATH" value="$(var plugin_path)" />
      <env name="GAZEBO_MODEL_DATABASE_URI" value="" />
    </executable>
    <executable cmd="gzclient --verbose $(var world_path)" output="both">
      <env name="GAZEBO_MODEL_PATH" value="$(var model_path)" />
      <env name="GAZEBO_RESOURCE_PATH" value="$(var resource_path)" />
      <env name="GAZEBO_PLUGIN_PATH" value="$(var plugin_path)" />
    </executable>
  </group>
```

Lastly, instances of the "full control" `rmf_fleet_adapter` are launched for each robot type annotated in the map. The navigation graphs for each fleet as generated by the `building_map_generator` script is passed via the `nav_graph_file` argument. For the office map, a single fleet of `Magni` robots is defined. Hence, a single `magni_adapter.launch.xml` file configured with the kinematic properties of this robot type along with spatial thresholds used for planning, is launched. Along with the fleet adapter, a `robot_state_aggregator` node is started. This node aggregates `RobotState` messages with `RobotState.name` containing the `robot_prefix` argument and publishes the aggregate to `/fleet_states` with `FleetState.name` specified by the `fleet_name` argument.

```xml
<group>
  <let name="fleet_name" value="magni"/>
  <include file="$(find-pkg-share rmf_demos)/include/adapters/magni_adapter.launch.xml">
    <arg name="fleet_name" value="$(var fleet_name)"/>
    <arg name="use_sim_time" value="$(var use_sim_time)"/>
    <arg name="nav_graph_file" value="$(find-pkg-share rmf_demos_maps)/maps/office/nav_graphs/0.yaml" />
  </include>
  <include file="$(find-pkg-share rmf_fleet_adapter)/robot_state_aggregator.launch.xml">
    <arg name="robot_prefix" value="magni"/>
    <arg name="fleet_name" value="$(var fleet_name)"/>
    <arg name="use_sim_time" value="true"/>
  </include>
</group>
```

When testing RMF with hardware, the same launch files can be used, with the exception of starting `Gazebo`.
More information on running demos with hardware can be found [the chapter on Integration](integration.md).

### Task Requests
RMF supports various tasks out of the box. For more information see [Tasks in RMF](./task.md)
A web-based dashboard is provided to allow users to send commands to RMF.
Once the [dashboard server](https://github.com/open-rmf/rmf_demos/blob/0d4265a6c81a24e2bbfe6378b4060e94f50066a9/rmf_demos/launch/common.launch.xml#L67-L72) is launched, it can be accessed at https://open-rmf.github.io/rmf-panel-js/.

![Custom RMF web panel](https://github.com/open-rmf/rmf_demos/raw/media/RMF_Panel.png?raw=true)

Alternatively several scripts exist in `rmf_demos_tasks` to assist users with submitting requests from the terminal. Presently the `dispatch_loop.py`, `dispatch_delivery.py` and `dispatch_clean.py` scripts can be used to submit `Loop`, `Delivery` and `Clean` requests.

## Conclusion

This chapter covered the utilization of the `traffic_editor` tool to create annotated maps that allow the auto-generation of 3D worlds for simulations.
It also covered the assets used within simulations and the corresponding plugins necessary for ROS 2 and RMF to interface with them.
A working example of these components running together, in the form of the `rmf_demos_maps` package, was provided as a reference for how to actualize a custom system.
The next chapter will introduces the basic concept behind RMF.
````

### data/source_texts/ref-105.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# FLEET CONFIG =================================================================
# RMF Fleet parameters

rmf_fleet:
  name: "tinyRobot"
  limits:
    linear: [0.5, 0.75] # velocity, acceleration
    angular: [0.6, 2.0] # velocity, acceleration
  profile: # Robot profile is modelled as a circle
    footprint: 0.3 # radius in m
    vicinity: 0.5 # radius in m
  reversible: True # whether robots in this fleet can reverse
  battery_system:
    voltage: 12.0 # V
    capacity: 24.0 # Ahr
    charging_current: 5.0 # A
  mechanical_system:
    mass: 20.0 # kg
    moment_of_inertia: 10.0 #kgm^2
    friction_coefficient: 0.22
  ambient_system:
    power: 20.0 # W
  tool_system:
    power: 0.0 # W
  recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate
  recharge_soc: 1.0 # Battery level to which robots in this fleet should be charged up to during recharging tasks
  publish_fleet_state: 10.0 # Publish frequency for fleet state, ensure that it is same as robot_state_update_frequency
  account_for_battery_drain: True
  task_capabilities: # Specify the types of RMF Tasks that robots in this fleet are capable of performing
    loop: True
    delivery: True
  actions: ["some_action_here"]
  finishing_request: "park" # [park, charge, nothing]
  responsive_wait: True # Should responsive wait be on/off for the whole fleet by default? False if not specified.
  robots:
    tinyRobot1:
        charger: "tinyRobot1_charger"
        responsive_wait: False # Should responsive wait be on/off for this specific robot? Overrides the fleet-wide setting.
    tinyRobot2:
        charger: "tinyRobot2_charger"
        # No mention of responsive_wait means the fleet-wide setting will be used

  robot_state_update_frequency: 10.0 # Hz

fleet_manager:
  prefix: "http://127.0.0.1:8080"
  user: "some_user"
  password: "some_password"

# TRANSFORM CONFIG =============================================================
# For computing transforms between Robot and RMF coordinate systems

# Optional
reference_coordinates:
  L1:
    rmf: [[20.33, -3.156],
          [8.908, -2.57],
          [13.02, -3.601],
          [21.93, -4.124]]
    robot: [[59, 399],
          [57, 172],
          [68, 251],
          [75, 429]]
```

### data/source_texts/ref-079.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Traffic Editor

This section describes the traffic-editor GUI and simulation tools.

## Introduction and Objectives

Traffic management of heterogeneous robot fleets is non-trivial. One of the
challenges with coordinated management arises from varying semantics in
information models used across fleets. Representations of waypoints, lanes,
charging/docking stations, restricted zones, infrastructure  systems such as
doors & lifts, among others, are subject to vendor's discretion. However,
standardized conventions that convey the capabilities and intentions of fleets
in a shared facility are quintessential for planning. Multi-agent participants
in other modes of transportation such as roadways collectively adhere to a set
of rules and conventions which minimize chaos. More importantly, they allow for
a new participant to readily integrate into the system by following the
prescribed rules. Existing agents can accommodate the new participant as its
behavior is apparent.

Traffic conventions for multi-robot systems do not exist.
The objective of the `traffic_editor` is to fill this gap by expressing the
intentions of various fleets in a standardized, vendor neutral manner through a
graphical interface. Collated traffic information from different fleets can then
be exported for planning and control. A secondary objective and benefit of the
`traffic_editor` is to facilitate generation of 3D simulation worlds which
accurately reflect physical environments.

## Overview

The `traffic_editor` [repository](https://github.com/open-rmf/rmf_traffic_editor) is home to the `traffic_editor` GUI and tools to auto-generate simulation worlds from GUI output.
The GUI is an easy-to-use interface which can create and annotate 2D floor plans with robot traffic along with building infrastructure information.
Often times, there are existing floor plans of the environment, such as architectural drawings, which simplify the task and provide a "reference" coordinate system for vendor-specific maps.
For such cases, `traffic-editor` can import these types of "backgroud images" to serve as a canvas upon which to draw the intended robot traffic maps, and to make it easy to trace the important wall segments required for simulation.

The `traffic_editor` GUI projects are stored as `yaml` files with `.building.yaml` file extensions.
Although the typical workflow uses the GUI and does not require hand-editing the `yaml` files directly, we have used a `yaml` file format to make it easy to parse using custom scripting if needed.
Each `.building.yaml` file includes several attributes for each level in the site as annotated by the user.
An empty `.building.yaml` file appears below.
The GUI tries to make it easy to add and update content to these file.

```yaml
levels:
  L1:
    doors:
      - []
    drawing:
      filename:
    fiducials:
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    floors:
      - parameters: {}
        vertices: []
    lanes:
      - []
    layers:
      {}
    measurements:
      - []
    models:
      -{}
    vertices:
      {}
    walls:
      {}
lifts:
  {}
name: building

```

## GUI Layout

The layout of the `traffic_editor` includes a `Toolbar`, a `Working Area` and a `Sidebar` as seen in the figure below:

![Traffic Editor GUI](images/traffic_editor/layout.png)

The toolbar contains a variety of tools to support actions such as setting the scale of the drawing, aligning levels for multi-level scenarios, adding virtual models to simulated environments, adding robot traffic lanes, simulated flooring, and so on.

As usual in a modern GUI, the top Toolbar contains a variety of tools to interact with items in the main Working Area.
This document will introduce and explain the tools as an example project is created.
However, the first three tools in the toolbar are commonly found in 2D drawing tools, and should behave as expected:

|                    Icon                           |  Name  | Shortkey |               Function               |
|:-------------------------------------------------:|:------:|:--------:|:------------------------------------:|
| ![Select icon](images/traffic_editor/icons/select.svg) | Select |   `Esc`  | Select an entity in the `Working Area` |
|  ![Move icon](images/traffic_editor/icons/move.svg)    |  Move  |    `m`   |  Move an entity in the `Working Area`  |
| ![Rotate icon](images/traffic_editor/icons/rotate.svg) | Rotate |    `r`   | Rotate an entity in the `Working Area` |

The `Working Area` is where the levels, along with their annotations, are rendered.
The user is able to zoom via the mouse scroll wheel, and pan the view by pressing the scroll wheel and moving the mouse cursor.

The `Sidebar` on the right side of the window contains multiple tabs with various functionalities:
* **levels:** to add a new level to the building. This can be done from scratch or by importing a floor plan image file.
* **layers:** to overlap other images such as lidar maps over the level
* **lifts:** to configure and add lifts to the building
* **traffic:** to select which "navigation graph" is currently being edited, and toggle which graph(s) are being rendered.

## Annotation Guide
This section walks through the process of annotating facilities while highlighting the capabilities of the `traffic_editor` GUI.

To create a new traffic editor `Building` file, launch the traffic editor from a terminal window (first sourcing the workspace if `traffic-editor` is built from source).
Then, click `Building -> New...` and choose a location and filename for your `.building.yaml` file.

### Adding a level
A new level in the building can be added by clicking the `Add` button in the `levels` tab of the `Sidebar`.
The operation will open a dialog box where the `name`, `elevation` (in meters) and path to a 2D `drawing` file (`.png`) can be specified.
In most use cases, the floor plan for the level is used as the drawing.
If unspecified, the user may explicitly enter dimensions of the level in the fields provided.

![Add a level dialog](images/traffic_editor/add_level.png)

In the figure above, a new level `L1` at `0m` elevation and a floor plan have been added as reflected in the `levels` tab.
A default scale `1px = 5cm` is applied.
The actual scale can be set by adding a measurement.
Any offsets applied to align levels will be reflected in the `X` and `Y` columns.
Saving the project will update the `tutorial.building.yaml` files as seen below:
```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
lifts:
  {}
name: building
```
### Adding a vertex
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Vertex icon](images/traffic_editor/icons/vertex.svg)| `v` |

A vertex is a fundamental component of multiple annotations.
Walls, measurements, doors, floor polygons and traffic lanes are created from two or more vertices.
To create a vertex, click on the vertex icon in the `Toolbar` and then click anywhere on the canvas.
The default attributes of a vertex are its coordinates along with an empty name field.
Additional attributes may be added by first selecting the vertex (which will turn it red), and then clicking the `Add` button in the figure.
Short descriptions of these are presented below:
* **is_holding_point:** if true and if the waypoint is part of a traffic lane,
  the `rmf_fleet_adapter` will treat this as a _holding point_ during path
  planning, i.e., the robot is allowed to wait at this waypoint for an indefinite
  period of time.
* **is_parking_spot:** robot's parking spot. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L73-L76)
* **is_passthrough_point:** waypoint which the robot shouldnt stop. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L63-L68)
* **is_charger:** if true and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will treat this as a charging station.
* **is_cleaning_zone** indicate if current waypoint is a cleaning zone, specifically for `Clean` Task.
* **dock_name:** if specified and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will issue an `rmf_fleet_msgs::ModeRequest` message with
  `MODE_DOCKING` and `task_id` equal to the specified name to the robot as it approaches this waypoint. This is used when the robot is executing their custom docking sequence (or custom travel path).
* **spawn_robot_type:** the name of the robot model to spawn at this waypoint in
  simulation. The value must match the model's folder name in the assets
  repository. More details on the robot model and plugin required for simulation
  can be found in [Simulation](simulation.md)
* **spawn_robot_name:** a unique identifier for the robot spawned at this
  waypoint. The `rmf_fleet_msgs::RobotState` message published by this robot
  will have `name` field equal to this value.
* **pickup_dispenser** name of the dispenser workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **dropoff_ingestor** name of the ingestor workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **human_goal_set_name** The `goal_sets.set_area` name, used by crowd simulation. For more info about `crowd_sim`, please see the [Crowdsim section] (https://osrf.github.io/ros2multirobotbook/simulation.html#crowdsim) of the Simulation Chapter for more details.

![Vertex attributes](images/traffic_editor/add_vertex.png)

Each vertex is stored in the `tutorial.building.yaml` file as a list of x-coordinate, y-coordinate, elevation, vertex_name and a set of additional parameters.

```yaml
  vertices:
    - [1364.76, 1336.717, 0, magni1_charger, {is_charger: [4, true], is_parking_spot: [4, true], spawn_robot_name: [1, magni1], spawn_robot_type: [1, Magni]}]
```
### Adding a measurement
|                    Icon                    |
|:------------------------------------------:|
| ![Measurement icon](images/traffic_editor/icons/measurement.svg)|

Adding a measurement sets the scale of the imported 2D drawing, which is essential for planning and simulation accuracy.
Scalebars or reference dimensions in the floor plan aid with the process. Often, you can draw the measurement line directly on top of a reference scale bar in a drawing.
With the editor in _Building_ mode, select the _Add Measurement_ tool and click on two points with known dimensions.
A pink line is rendered on the map with two vertices at its ends at the selected points.

Note:
A measurement line may be drawn by clicking on existing vertices.
In this scenario, no additional vertices are created at its ends.

Selecting the line populates various parameters in the Properties window of the `Sidebar`.
Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.
Currently, you must save the project and restart `traffic-editor` to see the changes reflected (todo: fix this...).

![Measurement properties](images/traffic_editor/add_measurement.png)

The above process adds two `vertices` and a `measurement` field to the `tutorial.building.yaml` file as seen below.
For the measurement field, the first two elements represent the indices of vertices representing the ends of
the line.
The `distance` value is stored in a sub-list of parameters.

```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
    measurements:
      - [1, 0, {distance: [3, 8.409]}]
    vertices:
      - [2951.728, 368.353, 0, ""]
      - [2808.142, 1348.9, 0, ""]

lifts:
  {}
name: building
```

### Adding a wall
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Wall icon](images/traffic_editor/icons/wall.svg)| `w` |

To annotate walls in the map, select the _Add Wall_ icon from the `Toolbar` and click on consecutive vertices that represent the corners of the wall.
The process of adding wall segments is continuous, and can be exited by pressing the `Esc` key.
Blue lines between vertices are rendered on the map which represent the drawn walls.
If the corner vertices are not present, they will automatically be created when using this tool.
Meshes of the annotated walls are automatically generated during 3D world generation using `building_map_generator`.
By default, the walls are of thickness of 10cm and height 2.5m.
The `wall_height` and `wall_thickness` attributes may be
modified [in the source code](https://github.com/open-rmf/rmf_traffic_editor/blob/main/rmf_building_map_tools/building_map/wall.py#L16-L17).

Wall texture options are available [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) in the source code.

![Annotating walls](images/traffic_editor/add_wall.png)

Walls are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices of the wall segment along with an empty parameter set.
```yaml
    walls:
      - [3, 4, {}]
      - [4, 5, {}]
      - [5, 6, {}]
      - [6, 7, {}]
      - [6, 8, {}]
      - [8, 9, {}]
```

### Adding a floor
|                    Icon                    |
|:------------------------------------------:|
| ![Floor icon](images/traffic_editor/icons/floor.svg)|

Flooring is essential for simulations as it provides a ground plane for the robots to travel over.
Floors are annotated using the _Add floor polygon_ tool from the `Main Toolbar` in _Building_ edit mode.
To define a floor, select consecutive vertices to create a polygon that accurately represents the flooring area as seen below.
These vertices will need to be added manually prior to this step.
Once created, save the project and reload.
Selecting the defined floor highlights its texture attributes. Similarly, [default list of available textures](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) is available in the source code.

![Highlighting floor's textures](images/traffic_editor/add_floor.png)

Certain scenarios may call for floors with cavities, for example, to represent elevator shafts.
The _Add hole polygon_ tool may be used for this purpose.
Additionally, the shape of a drawn polygon (floor or hole) may be modified using the _Edit polygon_ tool.
Clicking on the tool after selecting an existing polygon enables the user to modify vertices of the polygon.

Each polygon is stored in the `tutorial.building.yaml` file in the format below:
```yaml
    floors:
      - parameters: {texture_name: [1, blue_linoleum], texture_rotation: [3, 0], texture_scale: [3, 1]}
        vertices: [11, 10, 14, 15, 13, 12]
```

### Adding a door
|                    Icon                    |
|:------------------------------------------:|
| ![Door icon](images/traffic_editor/icons/door.svg)|

A door between two vertices can be added in _Building_ edit mode by selecting the _Add door_ tool from the `Main Toolbar`, and clicking on vertices representing the ends of the door.
Selecting an annotated door highlights its properties as seen in the figure below.
Presently, four door `types` are supported: "hinged", "double_hinged", "sliding" and "double_sliding".
The `motion_degrees` parameter specifies the range of motion in the case of hinged doors while the `motion_direction` dictates the direction of swing.
In order for the door to work in simulation, a `name` must be given to the door.

![Door type properties](images/traffic_editor/add_door.png)

Doors are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices along with the set of parameters that describes the door.

```yaml
 doors:
      - [24, 25, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, 1], name: [1, D001], type: [1, double_sliding]}]
```

### Adding a traffic lane
One of the most important tools in the `traffic_editor` GUI is the _Add lane_ tool.
The allowable motions of each fleet operating in the facility is conveyed through its respective Graph which consists of waypoints and connecting lanes.
In this approach, we assume that robots travel along effectively straight-line paths between waypoints.
While this may be perceived as an oversimplification of paths taken by robots that are capable of autonomous navigation, in practice the assumption holds fairly well given that these robots mostly travel along corridors or hallways and seldom in unconstrained open spaces.
For example, even in theoretically unconstrained spaces like building lobbies or shopping-mall atriums, it is likely that the site operator would prefer for the robots to operate in a "traffic lane" on the edge of the space, in order to not impede typical human traffic flows.

The `traffic` tab in the `Sidebar` has a default of nine Graphs for nine different fleets. To annotate lanes for a graph, say Graph 0, select the Graph from the `traffic` tab and click the _Add lane_ tool.
Lanes for this graph can be drawn by clicking vertices to be connected.
If a vertex is not present, it will automatically be added. Properties may be assigned to each vertex as described in the preceding section.
To issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint.

![Graphs' lane colors](images/traffic_editor/add_lane.png)

Each Graph has a unique color for its lanes, and their visibility may be toggled using the checkbox in the `traffic` tab.
A lane that is defined between two waypoints may be configured with these additional properties:
* **bidirectional:** if `true`, the `rmf_fleet_adapter` will plan routes for its
  robot assuming the lanes can be traversed in both directions. Lanes that are
  not bidirectional have arrows indicating their directionality (indigo lanes in
  figure above). A handy shortcut is that when a lane segment is selected, you can
  press the `b` key to toggle between unidirectional and bidirectional motion along that lane.
* **graph_idx**: the Graph number a lane corresponds to
* **orientation**: constrain the lane to make the robot travel in `forward` or `backward` orientation. This can be useful for the final lane segment approaching a docking point or charger, for example.

While lifts that move between levels are now supported in the `traffic_editor`, the **demo_mock_floor_name** and **demo_mock_lift_name** properties were originally engineered to showcase shared lift access in a single floor demonstration environment with a "mock" lift that receives lift commands and transmits lift states but does not actually move between any different floors in a building.
However, as there may be interest in such functionality for testing single-floor hardware setups that seek to emulate multi-floor scenarios, these properties were retained.

* **demo_mock_floor_name**: name of the floor that the robot is on while
  traversing the lane
* **demo_mock_lift_name**: name of the lift that is being entered or exited
  while the robot traverses the lane

To further explain these properties, consider this representation of a
navigation graph where numbers are waypoints and letters are lanes:
```
1 <---a---> 2 <---b---> 3

Waypoint 1 is on floor L1
Waypoint 2 is inside the "lift" named LIFT001
Waypoint 3 is on floor L3
The properties of edge "a" are:
    bidirectional: true
    demo_mock_floor_name: L1
    demo_mock_lift_name: LIFT001
The properties of edge "b" are:
    bidirectional: true
    demo_mock_floor_name: L3
    demo_mock_lift_name: LIFT001
```

If the robot is to travel from waypoint 1 to waypoint 3, the `rmf_fleet_adapter` will request for the "mock lift" to arrive at L1 when the robot approaches waypoint 1.
With confirmation of the "lift" at L1 and its doors in "open" state, the robot will be instructed to move into the "lift" to waypoint 2.
Once the "lift" indicates that it has reached L3, the robot will exit along lane b toward waypoint 3.

Note: when annotating graphs, it is highly recommended to follow an ascending sequence of graph indices without skipping intermediate numbers. Drawn lanes can only be interacted with if their associated Graph is first selected in the `traffic` tab.

The annotated Graphs are eventually exported as `navigation graphs` using the `building_map_generator` which are then used by respective `rmf_fleet_adapters` for path planning.

Lanes are stored in the following format in `tutorial.building.yaml`.
The data structure is a list with the first two elements representing the indices of the two vertices of the lane and a set of parameters with configured properties.
```yaml
    lanes:
      - [32, 33, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 2], orientation: [1, forward]}]
```

### Deriving coordinate-space transforms

Coordinate spaces are confusing!
For historical reasons, the GUI internally creates traffic maps by annotating images, so the "raw" annotations are actually encoded in pixel coordinates of the "base" floorplan image, in pixel coordinates, with +X=right and +Y=down, with the origin in the upper-left of the base floorplan image.
However, during the building map generation step, the vertical axis is flipped to end up in a Cartesian plane, so the vast majority of RMF (that is, everything downstream of traffic-editor and the building map generators) uses a "normal" Cartesian coordinate system. (As an aside -- the next version of traffic-editor is intended to be more flexible in this respect, and will default to a normal Cartesian coordinate system (not an image-based coordinate system), or even global coordinates (lat/lon). Although preliminary work is underway, there is not a hard schedule for this next-gen editor at time of writing, so the rest of this chapter will describe the existing `traffic-editor`.)

Although `traffic-editor` currently uses the upper-left corner of the base floorplan image as the reference frame, maps generated by robots likely will have their origin elsewhere, and will likely be oriented and scaled differently.
It is critical to derive the correct transform between coordinate frames in `traffic_editor` maps and robot maps as
`rmf_fleet_adapters` expect all robots to publish their locations in the RMF coordinate system while the `rmf_fleet_adapters` also issue path requests in the same frame.

To derive such transforms, the `traffic_editor` GUI allows users to overlay robot maps on a floor plan and apply scale, translation and rotation transformations such that the two maps align correctly.
The user can then apply the same transformations to convert between robot map and RMF coordinates when programming interfaces for their robot.

The robot map can be imported by clicking the `Add` button from the `layers` tab in the `Sidebar`.
A dialog box will then prompt the user to upload the robot map image.
The same box contains fields for setting the scale for the image along with applying translations and rotation.
Through visual feedback, the user can determine appropriate values for these fields.
As seen in the image below, importing the robot-generated map into the GUI has it located and oriented
differently than the floor plan.
With the right transformation values, the two maps can be made to overlap.

![Overlap robot-generated map](images/traffic_editor/coordinate_transform.png)

### Adding fiducials
|                    Icon                    |
|:------------------------------------------:|
| ![Fiducial icon](images/traffic_editor/icons/fiducial.svg)|

For maps with multiple levels, fiducials provide a means to scale and align different levels with respect to a reference level.
This is crucial for ensuring dimensional accuracy of annotations across different levels and aligning the
same for simulation.
Fiducials are reference markers placed at locations which are expected to be vertically aligned between two or more levels.
For example, structural columns may run through multiple floors and their locations are often indicated on floor plans.
With two or more pairs of corresponding markers between a level and a reference level, a geometric transformation (translation, rotation and scale) may be derived between the two levels.
This transformation can then be applied to all the vertices and models in the newly defined level.

To begin, add two or more non-collinear fiducials to the reference level with unique `name` attributes using the _Add fiducial_ tool (left image in figure below).
In the newly created level, add the same number of fiducials at locations that are expected to be vertically aligned with matching names as the reference level (right image in figure below).
Saving and reloading the project computes the transformation between the levels which is evident from the Scale
and X-Y offsets for the new level as seen in the `levels` tab.
This level is now ready to be annotated.

![Adding fiducials](images/traffic_editor/add_fiducial.png)

For each level, fiducials are stored in a list of their X & Y coordinates along with their name.
```yaml
    fiducials:
      - [936.809, 1323.141, F1]
      - [1622.999, 1379.32, F2]
      - [2762.637, 346.69, F3]
```

### Adding a lift
Lifts are integral resources that are shared between humans and robot fleets in multi-level facilities.
To add a lift to a building, click the `Add` button in the `lifts` tab in the `Sidebar`.
A dialog box with various configurable properties will load.
It is essential to specify the Name, Reference level and the X&Y coordinates (pixel units) of its cabin center.
A yaw (radians) may further be added to orient the lift as desired.
The width and depth of the cabin (meters) can also be customized.
Lifts can be designed to have multiple cabin doors which may open at more than one level.
To add a cabin door, click the `Add` button in the box below the cabin image.
Each cabin door requires a name along with positional and orientational information.
Here, the X&Y coordinates are relative to the cabin center.

![Configuring lift properties](images/traffic_editor/add_lift.png)

The configured lift is stored in the `tutorial.building.yaml` file as described below:
```yaml
lifts:
  LF001:
    depth: 2
    doors:
      door1:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: 1
        y: 0
      door2:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: -1
        y: 0
    level_doors:
      L1: [door1]
      L2: [door2]
    reference_floor_name: L1
    width: 2
    x: 827
    y: 357.7
    yaw: 1.09
```

After adding the lift, we would also wish to let our robots to transverse through the lift.
To achieve that, the user needs to create vertices/waypoints which are located within the lift cabin on each floor.
Once done, connect the waypoint within the lift cabin to other vertices via __add_lane__.

### Adding environment assets
Levels may be annotated with thumbnails of models available for simulation using the __Add model__ tool in __Building__ edit mode.
Selecting this tool opens a dialog box with a list of model names and matching thumbnails which can be imported to the map.
Once on the map, their positions and orientations can be adjusted using the _Move_ and _Rotate_ tools. Sample models are provided [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor_assets/assets/thumbnails/images/cropped/OpenRobotics)

The [thumbnail_generator documentation](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor#generating-custom-thumbnails) contains instructions on expanding the list of thumbnails for other models.

> Note: If no models are shown on the __add models__ window, Go to "Edit -> Preference", then indicate the thumbnail path. (`e.g. $HOME/rmf_ws/src/rmf/rmf_traffic_editor/rmf_traffic_editor_assets/assets/thumbnails`)

![Model name and thumbnails dialog](images/traffic_editor/add_model.png)

## Conclusion
This chapter covered various capabilities of the `traffic_editor` which are useful for annotating maps of facilities while adhering to a standardized set of semantics.
Examples of other traffic editor projects can be found in the [rmf_demos](https://github.com/open-rmf/rmf_demos) repository.
Running physics based simulations with RMF in the annotated sites is described in the [Simulation](simulation.md) chapter.
````

### data/source_texts/ref-528.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
.. _CHALLENGES:

==========
Challenges
==========

The agility challenges test teams' ability to adapt to unexpected situations and system failures during competition runs. Successfully handling these challenges is crucial for maintaining high performance and achieving competitive scores.

The competition incorporates challenges to test the robustness of team systems. Teams should be able to recognize when a challenge is occurring and properly handle the situation. There are four possible challenges that can occur during a run:

* **Conveyor Malfunction** - Inspection conveyor stops operating
* **Voltage Tester Malfunction** - One or both voltage testers stop providing data
* **Vacuum Tool Malfunction** - Vacuum gripper fails to grasp objects
* **High Priority Order** - Urgent kit request with time constraints

Conveyor Malfunction
====================

When the conveyor malfunction challenge occurs, the inspection conveyor will pause its motion. In addition, the cell feed will pause, so no new cells can be added during the challenge.

.. list-table:: Conveyor Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the malfunction begins (minimum: 0)
   * - ``DURATION``
     - int
     - Duration in seconds the malfunction lasts (minimum: 1)

Teams are expected to handle this challenge by:

1. **Detecting the malfunction** by monitoring the conveyor status topic (:ref:`reference <inspection_challenge_anchor>`)
2. **Pausing the inspection system** to avoid conflicts
3. **Waiting for recovery** by monitoring the status topic until it reports operational status
4. **Resuming operations** once the conveyor and cell feed return to normal

Voltage Tester Malfunction
==========================

When the voltage tester malfunction occurs, one or both voltage testers will stop publishing data.

.. list-table:: Voltage Tester Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the malfunction begins
   * - ``DURATION``
     - int
     - Duration in seconds the malfunction lasts
   * - ``TESTER``
     - int
     - Which voltage tester is affected (1 or 2)

Teams are expected to handle this challenge by:

1. **Detecting the malfunction** by monitoring voltage tester topics for data availability (:ref:`reference <inspection_challenge_anchor>`)
2. **Adapting operations** to avoid using the affected voltage tester(s)
3. **Monitoring for recovery** by watching the status topic until operational status is restored
4. **Continuing progress** using any operational voltage testers to maintain productivity
5. **Resuming full operations** once all voltage testers return to operational status

Vacuum Tool Malfunction
=======================

When the vacuum tool malfunction occurs, a specified vacuum gripper will fail during grasp attempts.

.. list-table:: Vacuum Tool Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``TOOL``
     - int
     - Which vacuum tool is affected (1 or 2)
   * - ``GRASP_OCCURRENCE``
     - int
     - Which grasp attempt will fail (minimum: 1)

.. note::

  **TOOL**: Refers to the :ref:`vacuum gripper tools <vacuumtools_msg>` VG_2 and VG_4 available to assembly robot 2.

.. note::

  **GRASP_OCCURRENCE**: Specifies which attempt at grasping will fail. For example, if set to 3, the first two grasp attempts will succeed normally, but the third attempt will fail and require retry.

Teams are expected to handle this challenge by:

1. **Detecting the failure** by monitoring the response from the grasp service (:ref:`reference <vacuum_tool_challenge_anchor>`)
2. **Repositioning the gripper** by moving it away from the target object
3. **Retrying the grasp** with proper positioning and approach

High Priority Order
===================

When a high priority order is requested, an internal timer starts tracking completion time. Teams should minimize the time taken to submit this urgent kit request.

.. list-table:: High Priority Order Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the high priority order is announced
   * - ``ID``
     - string
     - Unique identifier for the high priority order

Teams are expected to handle this challenge by:

1. **Detecting the request** by monitoring the high priority order topic (:ref:`reference <high-priority-anchor>`)
2. **Switching cell feed** to begin feeding NiMH cells
3. **Building the kit** using four NiMH cells with proper voltage specifications
4. **Delivering the kit** by moving the AGV to the shipping location
5. **Submitting the order** using the high priority submission service with the correct order ID (:ref:`reference <high-priority-anchor>`)
6. **Restoring normal operations** by switching cell feed back to Li-ion batteries
7. **Resuming standard tasks** to continue regular production

Configuration Example
======================

For complete challenge configuration examples showing all challenge types with valid parameters, see the :ref:`Challenges Configuration Reference <challenges_config_example>`.
```

### docs/categories/design-and-simulation/index.md

```markdown
---
title: "I. 설계·시뮬레이션"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › I. 설계·시뮬레이션

# I. 설계·시뮬레이션

## 핵심 질문

현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

## 개요

시나리오를 모델링하고, 시뮬레이션으로 처리능력·배치·정책을 미리 보고, 가상 시운전과 실제 상황 재현을 하는 설계 사용자의 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **33. 시나리오 모델·편집** | 시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 | 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? | [33. 시나리오 모델·편집](scenario-model-and-editing.md) | published |
| **34. 시뮬레이션·예측용 디지털 트윈** | 물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 | 현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? | [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md) | published |
| **35. 처리능력·규모·배치 설계** | 필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 | 로봇을 늘려야 할까, 공간이나 설비가 병목일까? | [35. 처리능력·규모·배치 설계](capacity-sizing-and-layout-design.md) | published |
| **36. 가상 시운전·실제 상황 재현** | 설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 | 설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? | [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 63건이다(논문 34건 · 기사·보고서 1건 · 업체 발표 5건 · 표준·오픈소스·기관 자료 23건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1129](../../references/ref-1129.md) — Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots (발행 2026-08-26)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-116](../../references/ref-116.md) — Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis (발행 2026-03)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-741](../../references/ref-741.md) — Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices (발행 2025-10)
- [ref-102](../../references/ref-102.md) — Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics (발행 2025)
- [ref-1089](../../references/ref-1089.md) — Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation (발행 2024-09)
- [ref-1134](../../references/ref-1134.md) — Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots (발행 2024-08-02)
- [ref-109](../../references/ref-109.md) — Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse (발행 2024-06)
- [ref-971](../../references/ref-971.md) — Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation (발행 2024-03-14)
- 그 밖에 24건

**기사·보고서**

- [ref-519](../../references/ref-519.md) — 머니투데이, 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간 (발행 2026-07-28)

**업체 발표**

- [ref-1165](../../references/ref-1165.md) — Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation (발행 2024-08-28)
- [ref-1132](../../references/ref-1132.md) — 현대자동차그룹, 가상의 디지털 공간에 세운 쌍둥이 공장 (발행 2023-11-21)
- [ref-526](../../references/ref-526.md) — CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) (발행 2021-11)
- [ref-527](../../references/ref-527.md) — NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins (발행 미확인)
- [ref-1090](../../references/ref-1090.md) — BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2 (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-518](../../references/ref-518.md) — ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition (발행 2026)
- [ref-1126](../../references/ref-1126.md) — VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions (발행 2025-05)
- [ref-1133](../../references/ref-1133.md) — NASA, NASA-STD-7009B Standard for Models and Simulations (발행 2024-03-05)
- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-831](../../references/ref-831.md) — ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications) (발행 미확인)
- [ref-528](../../references/ref-528.md) — NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges (발행 미확인)
- [ref-524](../../references/ref-524.md) — OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund), ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) (발행 미확인)
- [ref-523](../../references/ref-523.md) — Open Robotics (open-rmf), rmf_simulation — README (발행 미확인)
- [ref-517](../../references/ref-517.md) — NIST, Digital Twins for Advanced Manufacturing (발행 미확인)
- [ref-516](../../references/ref-516.md) — 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 (발행 미확인)
- 그 밖에 13건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) — 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건: 병원·제조 공장·물류창고·기타), 13절 각주 16건, 1차 조건부 승인 수정 11건 반영 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area36-s6.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "6. 대표 접근법과 기술" 절(1,605자)을 옮겼다 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area36-s4.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "4. 핵심 개념과 용어" 절(1,262자)을 옮겼다 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료](../../topics/2026/2026-09-30-area36-s8.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "8. 대표 연구와 자료" 절(1,238자)을 옮겼다 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 열린 질문](../../topics/2026/2026-09-30-area36-s11.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "11. 열린 질문" 절(1,205자)을 옮겼다 (실행 2026-09-30-17)
<!-- auto:category-recent:end -->
```

### docs/categories/design-and-simulation/scenario-model-and-editing.md

```markdown
---
title: "33. 시나리오 모델·편집"
type: area
category: "I. 설계·시뮬레이션"
area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [시나리오 형식, OpenSCENARIO, Open-RMF, 장애 주입, 시나리오 라이브러리, 미션 기술 형식]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1086, ref-104, ref-079, ref-971, ref-528, ref-1087, ref-1088, ref-726, ref-1089, ref-815, ref-1090, ref-116, ref-1091, ref-1092, ref-046]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 33. 시나리오 모델·편집

# 33. 시나리오 모델·편집

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

## 3. 왜 중요한가

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1091][^ref-528][^ref-1088][^ref-116]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 왜 중요한가](../../topics/2026/2026-09-30-area33-s3.md)에 있다.

## 4. 핵심 개념과 용어

시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [추정][^ref-1088][^ref-1086][^ref-528]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 다섯 사례는 모두 실제 현장 배치가 아니라 공개된 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오를 여섯 항목으로 정리한 것이며, 이 영역에서는 각 시나리오가 무엇을 어떤 단위로 담았는지를 본다. [사실][^ref-104][^ref-971][^ref-1087]

**현장 유형:** 상업 시설

**사례:** Open-RMF 예제 호텔·공항 터미널 월드의 다중 플릿 순찰·청소 시나리오(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 월드를 띄운 뒤 dispatch_clean·dispatch_patrol 같은 작업 명령을 따로 넣으면 작업이 생긴다. [사실][^ref-104] |
| 작업 대상 | 호텔 월드의 로비와 객실 2개 층 공간을 순찰(loop)·청소한다(예제 명령은 로비 청소). [사실][^ref-104] |
| 수행 자원 | 호텔 월드에는 로봇 플릿 3개(로봇 4대), 승강기 2대, 여러 문이 있고, 디스패처가 [플릿 어댑터](../../glossary/fleet-adapter.md)들 사이의 작업 입찰을 조율한다. [사실][^ref-104] |
| 제약 | 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에 선택적으로 군중 시뮬레이션과 사람이 모는 읽기 전용(read_only) 카트를 더해 순찰·배송·청소를 실행한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

rmf_demos의 시나리오는 건물 구성(차선·승강기·문·충전 위치)을 담은 월드를 띄운 뒤 작업을 명령으로 따로 넣는 구조다(2026-09-30 확인). [사실][^ref-104] 호텔·공항 터미널 모두 시뮬레이션 예제 월드이며 실제 시설의 도입 사례가 아니다.

**현장 유형:** 병원

**사례:** Open-RMF 예제 클리닉 월드에서 두 층의 간호 스테이션 사이 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 순찰 명령(dispatch_patrol)으로 작업을 넣는다. 예제 명령은 1층과 2층의 간호 스테이션을 순찰 지점으로 지정한다. [사실][^ref-104] |
| 작업 대상 | 두 층에 걸친 간호 스테이션 사이의 순찰 경로(공간) [사실][^ref-104] |
| 수행 자원 | 역할이 다른 로봇 플릿 2개와 승강기 2대 [사실][^ref-104] |
| 제약 | 로봇이 승강기 2대가 있는 2개 층 시설에서 층을 오가며 순찰해야 한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

클리닉 월드는 병원형 시나리오 예제이며 실제 병원 배치 사례가 아니다. 이 월드는 승강기 2대가 있는 2개 층 시설이고, 로봇이 층을 오가며 순찰한다. [사실][^ref-104] 층간 이동이 승강기를 거친다는 점에서 이 예제는 설비를 시나리오 요소로 담는 예로 볼 수 있다. [추정][^ref-104]

**현장 유형:** 실외

**사례:** Open-RMF 예제 캠퍼스 월드의 배송 로봇 장거리 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 명령으로 장거리 순찰을 넣는다. [사실][^ref-104] |
| 작업 대상 | 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스 공간 [사실][^ref-104] |
| 수행 자원 | 여러 대의 배송 로봇 [사실][^ref-104] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

캠퍼스 월드는 실내 층 좌표 대신 지구 좌표로 공간을 주석한 실외 시나리오 예제다. [사실][^ref-104] 같은 예제 모음의 제조·물류 월드는 영상 데모뿐이라 사례로 세우지 않고 7절에서만 다룬다.

**현장 유형:** 가정

**사례:** BEHAVIOR-1K의 일상 가정 활동 라이브러리(벤치마크)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 BDDL로 명세하고, 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상(강체·변형체·액체)을 OmniGibson 시뮬레이터에 구현했다. [사실][^ref-971] |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 활동이 일상 가정 활동이라서 현장 유형을 '가정'으로 분류했으며, 장면에는 주택뿐 아니라 정원·식당·사무실도 들어 있다. [사실][^ref-971] 실제 가정 배치가 아니라 시뮬레이션 벤치마크다.

**현장 유형:** 제조 공장

**사례:** NIST ARIAC 전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립과 장애 주입(경진대회 시나리오)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 키팅과 모듈 조립 두 작업을 주문으로 받는다. [사실][^ref-1087] |
| 작업 대상 | 배터리 셀 4개를 트레이에 담는 키트, 셀 4개와 상하 케이스로 조립하는 모듈 [사실][^ref-1087] |
| 수행 자원 | 시나리오에 컨베이어·전압 시험기·진공 그리퍼가 들어 있고, 각각을 고장 대상으로 선언할 수 있다. [사실][^ref-528] |
| 제약 | 해당 없음 |
| 완료·인계 | 아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않는다. [사실][^ref-1087] |
| 예외·성과 | 컨베이어 고장(시작 시각·지속 시간), 전압 시험기 고장(시작·지속·대상 시험기), 진공 그리퍼 파지 실패(도구·몇 번째 파지인지), 긴급 주문(시작 시각·주문 id) 네 과제를 매개변수로 선언해 시각이나 발생 횟수 조건으로 주입한다. [사실][^ref-528] |

ARIAC는 경진대회용 시뮬레이션 시나리오이며 실제 공장 사례가 아니다. ARIAC는 장애와 긴급 요청을 매개변수로 선언해 시나리오에 주입한다. [사실][^ref-528] 예외를 시나리오 안의 선언으로 다루는 이 방식은 이 영역이 참고할 점으로 보인다. [추정][^ref-528]

물류창고 현장의 시나리오 예제·템플릿 사례는 이번 조사에서 찾지 못했다. 경로 찾기 벤치마크의 시나리오 파일과 VDMA 레이아웃 교환 형식은 현장 사례가 아니므로 7절에서 다룬다. 국내 자료도 찾지 못했다.

## 6. 대표 접근법과 기술

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1088][^ref-104][^ref-971][^ref-528][^ref-1091]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md)에 있다.

## 8. 대표 연구와 자료

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 연구와 자료](../../topics/2026/2026-09-30-area33-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

확인한 자료를 종합하면 ROP는 시나리오 모델·현장 유형별 예제 라이브러리·편집기·형식 변환을 맡고, 물리·센서 시뮬레이션 엔진과 로봇 모델, 설비 제어, 도로 교통 시나리오 표준은 참조·변환해 묶는 연계 대상으로 두는 것으로 보인다. [추정][^ref-104][^ref-528][^ref-1092][^ref-1088]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 시나리오에 어떤 로봇을 어디에 둘지(로봇 구성)를 정하고 로봇 모델을 참조로 묶는다. [추정][^ref-104][^ref-1092] | 물리·센서 시뮬레이션 엔진과 로봇 기구학·동역학·센서 모델(SDFormat 로봇 기술)은 시뮬레이터·로봇 제조사 쪽 연계 대상이다. [추정][^ref-1092] |
| 시설·설비 제어 | 승강기·문·컨베이어 같은 설비를 시나리오 요소로 선언하고 설비 장애를 시각·발생 조건으로 주입한다. [추정][^ref-104][^ref-528] | 컨베이어·작업셀 같은 설비 제어 자체는 설비 쪽 연계 대상이다. [추정][^ref-104][^ref-528] |
| 업종별 조건 | 도로 교통 시나리오 표준의 구조(정적·동적 분리, 매개변수화)를 참조 설계로 삼는다. [추정][^ref-1088] | 도로 교통 시나리오 표준(OpenSCENARIO·OpenDRIVE)은 자율주행 분야의 연계 대상이다. [추정][^ref-1088] |

ROP가 직접 맡을 범위는 네 가지로 보인다: 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 시나리오 모델, 현장 유형별 예제 라이브러리, 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택, 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환이다. [추정][^ref-104][^ref-528][^ref-079][^ref-1090][^ref-116][^ref-1092]

시나리오 모델에 판(버전)을 두는 것은 1절 리스트업이 정한 목표다. 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 공개 자료에서 찾지 못했으므로, 판 관리 규칙은 아직 근거 없이 설계해야 하는 부분이다. [추정][^ref-1088][^ref-046][^ref-104][^ref-079]

경계는 제품 전략에 따라 이동할 수 있다. 이종 제조사를 연결하는 ROP는 시뮬레이터·제조사·설비 쪽 기능을 직접 만들기보다 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. [추정][^ref-1092][^ref-104][^ref-528][^ref-1088] 경계 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1089]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 열린 질문](../../topics/2026/2026-09-30-area33-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [33. 시나리오 모델·편집](scenario-model-and-editing.md) — 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건: 상업 시설·병원·실외·가정·제조 공장), 1차 조건부 승인 수정 13건 반영, 13절 각주 15건. 2차 수정: 4절 요약 태그 [추정]으로 정정, 5절 병원·제조 공장 사례 서술의 사실·추정 분리 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md) — 자동 분리: 33. 시나리오 모델·편집 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,795자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md) — 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,571자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md) — 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(1,360자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md) — 자동 분리: 33. 시나리오 모델·편집 의 "4. 핵심 개념과 용어" 절(1,249자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장 태그를 [사실]에서 [추정]으로 정정 (실행 2026-09-30-12)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1087]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30
```

### docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md

```markdown
---
title: "34. 시뮬레이션·예측용 디지털 트윈"
type: area
category: "I. 설계·시뮬레이션"
area_no: 34
related_areas: [15, 18, 20, 21, 25, 27, 32, 39, 47, 54, 55, 57]
tags: [디지털 트윈, 이산 사건 시뮬레이션, ISO 23247, Open-RMF 시뮬레이션, 시나리오 실험]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-101, ref-241, ref-267, ref-291, ref-398, ref-406, ref-516, ref-518, ref-520, ref-521, ref-522, ref-523, ref-524, ref-525, ref-526, ref-527]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 34. 시뮬레이션·예측용 디지털 트윈

# 34. 시뮬레이션·예측용 디지털 트윈

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시뮬레이션 엔진**: 로봇·설비·물품·사람을 물리·센서 수준에서 가상으로 재현한다(MuJoCo·Gazebo·Isaac Sim 등)
- **운영 정책·수요 변화 예측**: 배치·운영 정책·일의 양이 바뀔 때의 효과를 가상 환경에서 미리 본다
- **시뮬레이션 관측 모델**: 잡음·지연이 있는 관측을 만들어 시뮬레이션 시험이 현실의 불확실성을 반영하게 한다
- **시뮬레이션 자산 관리**: 로봇·물품·환경의 3D 모델과 물성 값을 출처·라이선스와 함께 관리해 시뮬레이션에 쓴다

이전 분류(2026-09-24)에서 이 페이지는 옛 22번 영역 ‘시뮬레이션·예측용 디지털 트윈’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [옛 분류원문]

> 옛 질문: 성수기 주문량이 늘면 어디가 먼저 막힐까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]

## 3. 왜 중요한가

시뮬레이션·예측용 디지털 트윈은 실제 운영을 방해하지 않고 개선안을 먼저 시험하는 도구로 쓰일 수 있어, 2절의 성수기 병목 질문에 실제 성수기가 오기 전에 답하는 수단이 된다. [추정][^ref-522]

Coelho 외(2021)는 사내 물류 시뮬레이션 모델이 현실을 대표하면 실제 운영을 방해하지 않고 개선안을 시험하는 디지털 트윈화 도구로 쓰일 수 있다고 보고했다. [사실][^ref-522] 로봇 플릿 쪽에서는 Open-RMF 문서가 물리 시뮬레이터를 쓰면 배터리 소모나 충돌 비용 없이 시나리오를 반복하고, 드문 예외 상황을 탐색하고, 현장 배치 전에 장시간 검증을 할 수 있다고 설명한다(확인일 2026-09-25). [사실][^ref-406]

공급망 수준에서도 Le·Fan(2024)은 COVID-19 이후 위험·교란 관리에서 디지털 트윈의 이점이 뚜렷해졌다고 보고 물류·공급망 디지털 트윈 개념 틀을 제안했다. [사실][^ref-521] 다만 같은 검토는 실제 데이터로 검증한 논문이 소수이고 대다수가 생성 데이터를 쓴다고 보고해, 예측이 현장에서 얼마나 맞는지는 아직 확인할 과제로 남는다. [사실][^ref-521]

## 4. 핵심 개념과 용어

이 위키는 디지털 트윈을 용도로 나눈다: 현재 상태를 표현하는 것은 18. 실시간 세계 상태·데이터 일관성, 그 모델을 이용해 가정한 미래를 실험하는 것은 이 영역이다. 분류 원문의 해당 문장은 2절 원문 주석에 있다.

자세한 내용은 주제 페이지 [34. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area22-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 성수기 주문 증가를 앞두고 피킹 배정 규칙과 로봇 대수를 가상 환경에서 비교

| 항목 | 내용 |
|---|---|
| 시작 조건 | 성수기 주문·물동량 전망이 시나리오 입력으로 들어온다. 이 전망은 상위 업무 시스템의 수요예측에서 받는 입력으로 보인다(연계 대상). [추정][^ref-521][^ref-527] |
| 작업 대상 | 가정한 성수기 주문의 피킹 작업(가상 환경 안의 주문·운반 흐름) |
| 수행 자원 | 시뮬레이션된 로봇(slotcar 모델)과 문·승강기 설비 플러그인이 Open-RMF 의 경로·문·승강기 요청에 응답한다. [사실][^ref-406][^ref-523] ROP는 자기 배정·교통·충전 정책을 이 가상 플릿·설비에 그대로 실행해 보는 것으로 보인다. [추정][^ref-406][^ref-523] |
| 제약 | 주문 도착량·배정 규칙·자원 수(로봇·작업대)를 바꿔 처리량과 대기를 비교하는 방식으로 어디가 먼저 막히는지 본다. [추정][^ref-398][^ref-101] 경로망 배치도 시뮬레이션으로 설계하는 연구가 있다. [사실][^ref-267] |
| 완료·인계 | 시뮬레이션 결과를 업무 완료나 재고 변경으로 인정하지 않고, 채택안의 변경 후 동작 확인은 54. 시험·형식 검증·벤치마크로 넘긴다는 구분은 구축자 의견이다. [의견][^ref-406] |
| 예외·성과 | Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398] 예측이 실제와 맞는지는 실데이터 검증이 부족해 미확인이다. [사실][^ref-521] |

다음은 설명을 위한 가상의 시나리오이다. 물류센터 운영자가 성수기 전에 피킹 구역에서 어느 자원이 먼저 포화되는지 알고 싶어 한다. 이미 공개된 이산 사건 시뮬레이션 연구·도구는 이런 질문에 도착량·규칙·자원 수를 바꿔 결과를 비교하는 방식으로 답한다. 다만 ROP 오케스트레이션 정책 자체를 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사 범위에서 찾지 못했다. [추정][^ref-398][^ref-101][^ref-522][^ref-520]

국내에서는 CJ대한통운이 2021-11-22 현실 물류센터와 같은 가상 물류센터를 12월부터 단계적으로 구축해 2023년 AI·알고리즘을 적용한 디지털 트윈을 완성하겠다는 계획을 발표했고, 작업 동선·재고 배치·설비 효율 최적화와 장비 고장·피킹 오류·상품 파손 원인의 사전 파악을 목표로 들었다. [추정] 벤더 주장[^ref-526]

## 6. 대표 접근법과 기술

이 위키는 대표 접근을 이산 사건 시뮬레이션, 같은 코드를 쓰는 물리 시뮬레이터, 도면·스캔에서 초기 모델을 만드는 방법으로 정리한다(구축자 의견). [의견][^ref-520][^ref-406][^ref-241]

자세한 내용은 주제 페이지 [34. 시뮬레이션·예측용 디지털 트윈 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area22-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

표준으로는 제조용 디지털 트윈 프레임워크 ISO 23247(국내 KS X ISO 23247)이 있고, 오픈소스로는 Open-RMF 시뮬레이션·RAWSim-O·OFacT가 이 영역의 실험 도구다. [사실][^ref-516][^ref-406][^ref-101][^ref-524]

자세한 내용은 주제 페이지 [34. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area22-s7.md)에 있다.

## 8. 대표 연구와 자료

이 위키는 대표 자료를 개념 구분, 물류 DES와 디지털 트윈의 결합, 물류·공급망 디지털 트윈 검토, 모델 검증 틀, 스캔 기반 자동 생성 연구로 정리한다(구축자 의견). [의견][^ref-291][^ref-520][^ref-521][^ref-525][^ref-241]

자세한 내용은 주제 페이지 [34. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료](../../topics/2026/2026-09-25-area22-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡는 몫은 자기 작업 배정·교통·충전 정책과 설비 요청을 시뮬레이션된 플릿·설비에 대해 그대로 실행해 보는 것으로 보인다. [추정][^ref-406][^ref-523]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 경로 요청을 받는 단순화 로봇 모델에 자기 배정·교통·충전 정책을 실행해 보는 것 [추정][^ref-406][^ref-523] | 연계 대상: 센서 인식·로컬 회피 같은 로봇 자체 거동의 충실도는 제조사·물리 시뮬레이터 영역으로 보인다. [추정][^ref-406][^ref-523] 센서 시뮬레이션·합성 데이터·물리 AI는 시뮬레이터 제공자 영역이다. [추정] 벤더 주장[^ref-527] |
| 시설·설비 제어 | 문·승강기 요청을 시뮬레이션 설비 플러그인에 보내고 응답을 받는 흐름의 시험 [추정][^ref-406] | 연계 대상: 실제 승강기·컨베이어·PLC·설비 안전 제어([범위 경계](../../about/scope-boundary.md)) |
| 상위 업무 시스템 | 주문 도착량·배정 규칙·자원 수를 바꿔 처리량·대기를 비교하는 시나리오 실험 [추정][^ref-398][^ref-101] | 연계 대상: 시나리오의 주문·물동량 전망은 수요예측에서 받는 입력 [추정][^ref-521] |

Open-RMF 시뮬레이션의 로봇 모델은 경로 요청을 받아 레일식으로 움직이는 단순화 모델이어서, ROP 시뮬레이션은 로봇 거동보다 플릿 조율·설비 상호작용 실험에 초점이 맞는 것으로 보인다. [추정][^ref-406][^ref-523] 센서 시뮬레이션·합성 데이터를 앞세운 제품 소개는 벤더 주장이며 ROP 직접 범위가 아니다. [추정] 벤더 주장[^ref-527] 경계는 제품 전략에 따라 움직일 수 있으므로 [범위 경계](../../about/scope-boundary.md) 페이지를 함께 본다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 현재 상태 모델(18. 실시간 세계 상태·데이터 일관성)을 받아 미래를 실험하고, 그 결과를 시험·배정·교통·수명주기 영역으로 넘긴다. 아래 연결은 이 절의 각 문장 태그대로 읽는다.

자세한 내용은 주제 페이지 [34. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area22-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? 실데이터 검증 논문이 소수라는 검토가 배경이다.[^ref-521]
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가?[^ref-518]
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-56) 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가?[^ref-523]

2절의 질문 가운데 ROP 정책을 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사에서 찾지 못해 미확인으로 남긴다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md) — 영역 심화: 3~11절 신규 작성(4·6·7·8·10절은 주제 페이지로 분리), 2차 수정: 4절 끊긴 문장 정정, 5절 수행 자원·완료·인계 칸 태그 정정, 6·8절 요약 [의견]화, 7절 요약 각주 보강, 9절 벤더 주장 병기, sources 정리 (실행 2026-09-25-56)
- 2026-09-25 · 생성 · [34. 시뮬레이션·예측용 디지털 트윈 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area22-s7.md) — 자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 요약·첫 문장에 RAWSim-O·OFacT 근거 각주(ref-101·ref-524) 추가 (실행 2026-09-25-56)
- 2026-09-25 · 생성 · [34. 시뮬레이션·예측용 디지털 트윈 — 대표 연구와 자료](../../topics/2026/2026-09-25-area22-s8.md) — 자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 요약·첫 문장의 대표 자료 선정을 [의견] (구축자 의견)으로 바꾸고 근거 각주 보강 (실행 2026-09-25-56)
- 2026-09-25 · 생성 · [34. 시뮬레이션·예측용 디지털 트윈 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area22-s10.md) — 자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 "10. 다른 연구영역과의 연결" 절을 옮겼다. 2차 수정: 번호만 쓴 호칭 2곳 정정, 6. 지도·공간·위치 모델 연결을 [사실]/[추정]으로 분리, 28 연결의 '표준 기반' 단정 정정 (실행 2026-09-25-56)
- 2026-09-25 · 생성 · [34. 시뮬레이션·예측용 디지털 트윈 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area22-s4.md) — 자동 분리: 22. 시뮬레이션·예측용 디지털 트윈 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 수정 없음) (실행 2026-09-25-56)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-101]: Merschformann, M. (merschformann GitHub), RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-520]: Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G., Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics, 2020, https://www.sciencedirect.com/science/article/pii/S2351978920320990, 접근일 2026-09-25 (원문 미열람)
[^ref-521]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-09-25 (원문 미열람)
[^ref-522]: Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P., Simulation-based decision support tool for in-house logistics: the basis for a digital twin, 2021, https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646, 접근일 2026-09-25 (원문 미열람)
[^ref-523]: Open Robotics (open-rmf), rmf_simulation — README, 미확인, https://github.com/open-rmf/rmf_simulation, 접근일 2026-09-25
[^ref-524]: OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund), ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README), 미확인, https://github.com/OpenFactoryTwin/ofact, 접근일 2026-09-25
[^ref-525]: Sargent, R. G., Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation), 2008, https://dl.acm.org/doi/abs/10.5555/1516744.1516780, 접근일 2026-09-25 (원문 미열람)
[^ref-526]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-09-25 (원문 미열람)
[^ref-527]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 미확인, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-09-25 (원문 미열람)
```

### docs/categories/design-and-simulation/capacity-sizing-and-layout-design.md

````markdown
---
title: "35. 처리능력·규모·배치 설계"
type: area
category: "I. 설계·시뮬레이션"
area_no: 35
related_areas: [22, 25, 28, 34, 39]
tags: [소요대수 산정, RMFS, 대기행렬 모델, 충전 설비, 승강기 병목]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-096, ref-097, ref-098, ref-099, ref-100, ref-101, ref-102, ref-060, ref-103, ref-104, ref-105, ref-106, ref-108, ref-109]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 35. 처리능력·규모·배치 설계

# 35. 처리능력·규모·배치 설계

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **처리능력·규모 산정**: 처리할 일의 양에 맞는 로봇 수·종류, 충전기·작업대 배치, 운영 시간대를 정한다
- **병목 분석**: 로봇·설비·사람·승강기 가운데 어디가 병목인지 찾는다
- **다현장 자원 배치**: 여러 현장 사이에서 로봇과 자원을 어디에 얼마나 둘지 정한다
- **로봇 친화 공간 설계·개조**: 문 폭·문턱·경사·승강기 연동·충전 공간처럼 로봇이 다니고 일하기 쉬운 공간을 설계하거나 기존 공간을 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 3번 영역 ‘처리능력·거점·설비 계획’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 [옛 분류원문]

> 옛 질문: 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? [옛 분류원문]

## 2. 핵심 질문

로봇을 늘려야 할까, 공간이나 설비가 병목일까? [분류원문]

## 3. 왜 중요한가

확인한 연구들을 보면 처리량은 로봇 수만으로 정해지지 않는다. 작업대 위치·수, 충전기 수, 공용 승강기도 함께 처리량을 좌우한다. 그래서 로봇을 늘릴지 병목 설비를 늘릴지는 공유 자원의 가동률을 함께 계산해야 판단할 수 있는 것으로 보인다. [추정][^ref-096][^ref-097][^ref-102][^ref-060][^ref-103]

필요 대수를 정하는 문제는 오래 연구돼 왔다. 2006년에 나온 두 서베이는 차량 소요대수 산정을 무인운반차(Automated Guided Vehicle, AGV) 시스템 설계의 핵심 과제 가운데 하나로 다룬다. 두 서베이는 저자가 서로 다르다. [사실][^ref-099][^ref-100]

그런데 로봇만 늘리면 다른 자원에서 막히는 사례가 보고돼 있다. 한 유통사 물류센터의 팔레트 이동 데이터로 시뮬레이션한 2025년 연구에서, 충전기가 부족하면 큰 지연이 생겼고 남으면 불필요한 비용이 생겼다. [사실][^ref-102] 한 3차 병원의 약품 배송 로봇 사례(2025년 6월 관찰)에서는 승강기 가동률이 높을수록 배송 실패가 많았고 배송 시간도 길어졌다. 이 결과는 병원 사례이며, 물류센터에 그대로 적용되는지는 확인되지 않았다. [사실][^ref-060]

```mermaid
flowchart LR
  demand[물동량] --> robots[로봇 대수]
  demand --> stations[작업대 위치·수]
  demand --> chargers[충전기 수]
  demand --> lifts[공용 승강기]
  robots --> throughput[처리량]
  stations --> throughput
  chargers --> throughput
  lifts --> throughput
```

## 4. 핵심 개념과 용어

처리능력 계획을 읽을 때 필요한 기본 용어는 다음과 같다. 소요대수 모델은 Vis(2006)의 분류에 따라 결정론적 모델, 확률(대기행렬) 모델, 시뮬레이션 모델의 세 부류로 나뉜다. [사실][^ref-100]

- **차량 소요대수 산정(Fleet Sizing)** — 물동량과 서비스 수준을 맞추는 데 필요한 로봇·운반 차량 대수를 정하는 계획 문제다. 모델은 위의 세 부류로 나뉜다. [사실][^ref-100]
- **로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS)** — 로봇이 상품을 담은 이동식 선반(pod)을 피킹 스테이션과 보충 스테이션으로 옮기는 창고 방식이다. 품목당 선반 수와 두 스테이션 수의 비율이 설계 변수가 된다. [사실][^ref-097]
- **반개방형 대기행렬 네트워크(Semi-Open Queueing Network, SOQN)** — 주문은 밖에서 들어오지만 로봇 같은 자원은 정해진 수만큼 순환하는 시스템을 해석하는 모델이다. RMFS의 재고 배치 연구와 충전 전략 연구에 쓰였다. [사실][^ref-097][^ref-098]
- **이산 사건 시뮬레이션(Discrete Event Simulation, DES)** — 사건이 일어나는 시점마다 시스템 상태를 갱신하는 시뮬레이션이다. RAWSim-O는 RMFS용 이산 사건 시뮬레이션이다. [사실][^ref-101]
- **충전 임계값(recharge_threshold)** — Open-RMF 플릿 어댑터 템플릿의 설정값이다. 배터리가 이 수준보다 낮으면 그 플릿의 로봇은 작업하지 않는다(확인일 2026-09-25). [사실][^ref-105]

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

이 시나리오는 성수기 물동량에 대비해 로봇을 더 들일지, 작업대와 충전기를 늘릴지 비교하는 계획 작업이다. 로봇 가동률과 처리량은 대기행렬 모델로 추정할 수 있다. [사실][^ref-096]

**물류 흐름 단계:** 적치 → 보충 → 피킹 → 포장

**시나리오:** 성수기 물동량 증가에 대비해 로봇 증차와 작업대·충전기 증설을 비교

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 업무 시스템이 성수기 주문 도착률(물동량)을 넘긴다. 연계 대상: 물동량 예측 자체는 수요예측에서 받는 입력으로 보인다. [추정][^ref-096][^ref-100] |
| 작업 대상 | RMFS의 이동식 선반(pod)과 그 안의 품목. 품목당 선반 수가 설계 변수다. [사실][^ref-097] |
| 수행 자원 | 로봇은 선반을 운반하고, 피킹·보충 스테이션에서는 작업자가 일하며, 충전기가 로봇을 충전한다. 대기행렬 네트워크 모델로 로봇 가동률과 최대 주문 처리량을 해석적으로 추정할 수 있다. [사실][^ref-096] 피킹 스테이션과 보충 스테이션 수의 비율도 결정 변수다. [사실][^ref-097] |
| 제약 | 보관 구역 둘레에서 작업대가 어디에 있는지가 최대 처리량(처리 능력)에 영향을 준다. [사실][^ref-096] 포장대가 병목인지는 공유 자원의 가동률을 함께 계산해야 판단할 수 있을 것으로 보인다. 다만 물류센터 포장대를 병목으로 직접 분석한 1차 자료는 확인하지 못함. [추정][^ref-096][^ref-102] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 팔레트 이동 사례에서 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. [사실][^ref-102] |

다음은 설명을 위한 가상의 시나리오이다. 한 물류센터가 성수기를 앞두고 로봇을 몇 대 더 들일지, 피킹 스테이션이나 충전기를 늘릴지 정해야 한다. 계획자는 먼저 해석적 모델로 대안을 빠르게 추려 낸 뒤, 남은 대안을 시뮬레이션으로 확인하는 순서를 쓸 수 있을 것으로 보인다. [추정][^ref-096][^ref-101]

여러 층을 쓰는 센터라면 승강기도 공유 자원이다. 그러나 이번에 찾은 승강기 근거는 병원과 호텔 사례뿐이다. 물류센터 승강기의 정량 근거는 [11. 열린 질문](#11-열린-질문)으로 남긴다. [사실][^ref-060][^ref-103]

## 6. 대표 접근법과 기술

처리능력 계획에는 두 가지 방법이 함께 쓰이는 것으로 보인다. 설계 초기에는 해석적 대기행렬 모델로 대안을 빠르게 비교하고, 변동·배차 규칙·충전 상호작용은 이산 사건 시뮬레이션으로 반영한다. [추정][^ref-100][^ref-096][^ref-098][^ref-101][^ref-102][^ref-108]

자세한 내용은 주제 페이지 [35. 처리능력·규모·배치 설계 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area03-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에 참고할 도구는 시뮬레이터, 오케스트레이션 설정, 국내 인증 제도로 나뉜다. RAWSim-O는 RMFS 운영의 여러 결정 문제를 연구하는 오픈소스 이산 사건 시뮬레이션 프레임워크다. [사실][^ref-101]

자세한 내용은 주제 페이지 [35. 처리능력·규모·배치 설계 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area03-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 RMFS 대기행렬 연구와 승강기 연구다. RMFS 연구는 작업대 배치와 스테이션 비율이 처리량에 주는 영향을 다루고, 승강기 연구는 호텔·병원에서 승강기가 배송에 주는 영향을 다룬다. [사실][^ref-096][^ref-097][^ref-060][^ref-103]

자세한 내용은 주제 페이지 [35. 처리능력·규모·배치 설계 — 대표 연구와 자료](../../topics/2026/2026-09-25-area03-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

연계 대상: 물동량 예측 자체는 상위 업무 시스템의 수요예측에서 받는 입력이다. ROP의 직접 범위는 그 물동량을 받아 로봇·작업대·충전기 소요를 계산하고 검증할 운영 데이터와 모델을 제공하는 쪽으로 보인다. [추정][^ref-096][^ref-100]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 물동량을 받아 로봇·작업대·충전기 소요를 계산·검증할 운영 데이터와 모델 | 연계 대상: 수요예측(물동량 예측) |
| 시설·설비 제어 | 승강기 대기·운행 시간을 처리능력 계산의 공유 자원 제약으로 반영 | 연계 대상: 승강기 운행·제어(22. 설비·건물 시스템 연동) |

충전 임계값, 충전기 배정, 작업 종료 후 동작은 오케스트레이션 계층의 플릿 설정값이다. 따라서 충전 설비 계획의 결과는 ROP 운영 설정으로 이어지는 것으로 보인다. 반대로 ROP가 쌓는 충전 대기·가동률 기록은 다음 설비 계획의 입력이 될 수 있다. 다만 이를 보여 주는 공개 사례는 확인하지 못했다. [추정][^ref-105][^ref-004][^ref-102]

호텔 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다. [사실][^ref-103] 승강기 제어는 이 영역의 범위가 아니며, 이 영역은 승강기 시간을 제약 입력으로 다루는 데까지만 맡는다. 이는 분류 원문 19장 시설·설비 제어 경계에 따른 이 위키의 판단이다. [의견] 경계 기준은 [범위 경계](../../about/scope-boundary.md)를 본다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 아래 다섯 영역과 이어진다.

- [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 충전 방식 비교, 충전소 위치 결정, 충전 임계값 설정이 두 영역에 모두 걸린다. [사실][^ref-098][^ref-109][^ref-105]
- [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md) — 여러 플릿이 공용 승강기를 쓰는 환경이 있다. 이 영역은 승강기를 제약으로 다루고, 승강기 제어는 저쪽이 맡는다. [사실][^ref-104][^ref-060]
- [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 충전 방식을 비용 면에서 비교할 때와 스마트물류센터 인증 평가에서 두 영역이 만난다. [사실][^ref-098][^ref-106]
- [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md) — RMFS 시뮬레이터와 사례 시뮬레이션은 가정한 미래(증차·증설 대안)를 실험하는 용도로 연결된다. 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과는 구분한다. [추정][^ref-101][^ref-102]
- [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md) — Open-RMF 플릿 어댑터 템플릿 설정에서는 충전 임계값보다 배터리가 낮은 로봇이 작업하지 않는다. [사실][^ref-105] 그래서 충전 설정이 배정 가능한 로봇 수에 영향을 주는 것으로 보인다. [추정][^ref-105]

## 11. 열린 질문

원문 정의에 있는 교대 운영과 여러 거점의 자원 배치는 이번 조사에서 근거 자료를 찾지 못했다. 그래서 본문에 쓰지 않고 주제 페이지의 질문으로 남긴다.

자세한 내용은 주제 페이지 [35. 처리능력·규모·배치 설계 — 열린 질문](../../topics/2026/2026-09-25-area03-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [35. 처리능력·규모·배치 설계](capacity-sizing-and-layout-design.md) — 3~11절 신규 작성(소요대수 산정 모델, 작업대·충전기·승강기 병목, 가상 시나리오, ROP 경계, 열린 질문 4건). 2차 수정: 8절 각주 보강, 10절 순위 문장 삭제·MRTA 범위 한정, 9절 사실·의견 분리, 11절 문구, sources 에서 ref-107 제외 (실행 2026-09-25-10)
- 2026-09-25 · 생성 · [35. 처리능력·규모·배치 설계 — 대표 연구와 자료](../../topics/2026/2026-09-25-area03-s8.md) — 자동 분리: 3. 처리능력·거점·설비 계획 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 요약 문장 각주에 ref-097·ref-103 추가 (실행 2026-09-25-10)
- 2026-09-25 · 생성 · [35. 처리능력·규모·배치 설계 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area03-s6.md) — 자동 분리: 3. 처리능력·거점·설비 계획 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 드리프트 문장 삭제, 태그 없는 주장 3문장에 태그·각주 (실행 2026-09-25-10)
- 2026-09-25 · 생성 · [35. 처리능력·규모·배치 설계 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area03-s7.md) — 자동 분리: 3. 처리능력·거점·설비 계획 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정 없음, ref-107 인용 페이지) (실행 2026-09-25-10)
- 2026-09-25 · 생성 · [35. 처리능력·규모·배치 설계 — 열린 질문](../../topics/2026/2026-09-25-area03-s11.md) — 자동 분리: 3. 처리능력·거점·설비 계획 의 "11. 열린 질문" 절을 옮겼다(2차 수정 없음) (실행 2026-09-25-10)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-096]: Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System (EJOR 256(3), 976–990), 2017, https://repub.eur.nl/pub/107376/, 접근일 2026-09-25 (원문 미열람)
[^ref-097]: Lamballais, T., Roy, D., & de Koster, M. B. M., Inventory allocation in robotic mobile fulfillment systems, 2020, https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-099]: Le-Anh, T., & de Koster, M. B. M., A review of design and control of automated guided vehicle systems, 2006, https://www.sciencedirect.com/science/article/abs/pii/S0377221705001840, 접근일 2026-09-25 (원문 미열람)
[^ref-100]: Vis, I. F. A., Survey of research in the design and control of automated guided vehicle systems, 2006, https://www.sciencedirect.com/science/article/abs/pii/S0377221704006459, 접근일 2026-09-25 (원문 미열람)
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-09-25 (원문 미열람)
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-09-25 (원문 미열람)
[^ref-108]: 이문수, 채준재(로지스틱스연구), AGV 기반 제조물류시스템의 성능평가를 위한 해석적 모형에 관한 연구 - 반도체 Tandem 레이아웃 시스템을 중심으로 -, 2010, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001485142, 접근일 2026-09-25 (원문 미열람)
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현"
type: area
category: "I. 설계·시뮬레이션"
area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [가상 시운전, SiL·HiL, 로그 재생, 현실 격차, 시뮬레이션 신뢰도 평가]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-1126, ref-831, ref-1127, ref-1128, ref-406, ref-943, ref-1129, ref-1130, ref-599, ref-741, ref-1131, ref-1132, ref-1133, ref-1134, ref-1165]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 36. 가상 시운전·실제 상황 재현

# 36. 가상 시운전·실제 상황 재현

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실행 전 계획 검증**: 선언한 초기 조건에서 경로·자원·능력을 실제로 실행하지 않고 정적으로 검사한다
- **가상 시운전**: 실제 설치 전에 연동과 운영 정책을 가상 환경에서 시험한다
- **운영 기록 기반 재현**: 실제 운영 기록으로 시뮬레이션의 초기 상태와 사건을 다시 구성한다
- **시뮬레이션–현실 차이 관리**: 시뮬레이션 결과를 현실에 적용할 때 생기는 차이를 측정하고 보정한다
- **디지털 트윈 동기화**: 실시간 상태를 가상 모델에 계속 반영해 현재 상태 표현과 미래 실험을 잇는다

## 2. 핵심 질문

설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

## 3. 왜 중요한가

설치 전 가상 시운전은 제조·물류 설비 제어 분야에서 VDI/VDE 3693 과 MiL·SiL·HiL 시험 구성으로 정립되어 있고 여러 로봇 쪽에도 Open-RMF 시뮬레이션과 혼합 현실 도구가 있지만, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차 표준은 이번 조사에서 확인하지 못했다. [추정][^ref-1126][^ref-1130][^ref-406][^ref-1129]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 왜 중요한가](../../topics/2026/2026-09-30-area36-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 설치 전 시험, 기록 재생, 시뮬레이션 결과의 신뢰 판단 세 갈래로 묶인다.

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area36-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 사례는 실제 기록으로 문제를 재현한 병원 연구, 설치 전에 제어를 시험한 제조 공장·물류창고 사례, 시뮬레이션 시험 시나리오를 만든 대학 건물 사례다. 제조 공장·물류창고 사례의 PLC·컨베이어 같은 설비 제어 코드 가상 시운전은 분류 원문 19장의 '시설·설비 제어' 경계에서 설비 업체·통합자가 맡는 연계 대상으로 보이며, 여기서는 ROP 가상 시운전의 방법 근거로만 쓴다. [추정][^ref-1130][^ref-1131][^ref-1165]

**현장 유형:** 병원

**사례:** 병원에서 약품 배송 로봇의 승강기 탑승 실패를 실제 기록으로 분석하고 시뮬레이션으로 재현

| 항목 | 내용 |
|---|---|
| 시작 조건 | 고려대학교 구로병원에서 약품 배송 로봇이 실제로 수행한 배송(2025-06-18~29, 122건). [사실][^ref-943] |
| 작업 대상 | 약품과, 재현의 원천이 된 로봇 원격측정 기록·승강기 시스템 데이터. [사실][^ref-943] |
| 수행 자원 | 배송 로봇과 승강기가 실제 배송을 맡고, 측정한 점유율로 모수를 정한 몬테카를로 시뮬레이션으로 승강기 탑승 실패 기제를 재현했다. [사실][^ref-943] |
| 제약 | [승강기 가동률](../../glossary/elevator-operating-rate.md)(EOR) — Lee 외 저자들은 이를 혼잡 인지 배차의 제어 신호로 쓰자고 제안했다. [의견][^ref-943] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 승강기 가동률 임계값 59.01% 이하에서 배송 성공률 95.5%, 90% 초과에서 실패가 몰렸고, 주된 실패는 승객·화물이 로봇의 승강기 진입을 막는 경우였다. [사실][^ref-943] |

이 연구는 실제 운영 기록으로 문제 상황의 모수를 정하고 시뮬레이션으로 실패 기제를 다시 본 사례이며, 시뮬레이션은 완전한 디지털 트윈이 아니라 승강기 탑승 기하 모형이다. [사실][^ref-943] Lee 외 저자들은 여러 병원 시험이 어려울 때 병원별 구조·통행 구성·승강기 제어 정책을 재현한 병원 디지털 트윈으로 현장 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다. [의견][^ref-943]

**현장 유형:** 제조 공장

**사례:** 제조 공장에서 끝단 팔레타이징 포장 설비의 분산 제어를 가상 시운전

| 항목 | 내용 |
|---|---|
| 시작 조건 | 가상 시운전을 제어 루프에서 분산 에지 컴퓨팅 시스템 전체로 넓혀 여러 장치를 함께 시험하려는 연구 목적. [사실][^ref-1130] |
| 작업 대상 | 끝단 팔레타이징 포장 설비 시뮬레이션과, 이와 직접 피드백 루프로 연결된 응용. [사실][^ref-1130] |
| 수행 자원 | 실제 제어기 3대와 가상화 인스턴스 9대. [사실][^ref-1130] |
| 제약 | 비실시간 시뮬레이션이라는 한계. [사실][^ref-1130] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 시운전 기간·비용 절감 수치는 제시하지 않았다. [사실][^ref-1130] |

국내에서는 최성욱·박상철·왕지남(2008)이 자동차 차체 생산라인의 PLC 코드를 검증하려고 설비 상태·사건을 이산 사건 모델로 정의하고, 실제 PLC 하드웨어와 3D CAD·디지털 목업 기반 가상 공정 시뮬레이터를 양방향 통신으로 연동하는 가상 플랜트 구축 절차를 제안해 라인 안정화 기간과 비용을 줄이려 했다. [사실][^ref-1131] 현대자동차그룹은 싱가포르 혁신센터(HMGICS)에서 디지털 트윈 가상 공장으로 설비·로봇 배치 변경을 실제 생산을 멈추지 않고 가상에서 먼저 검증한다고 소개하지만, 시운전 기간 단축 같은 정량 수치는 밝히지 않았다. [추정] 벤더 주장[^ref-1132]

**현장 유형:** 물류창고

**사례:** 물류센터 구축에서 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미국 남부의 약 30만 제곱피트 규모 물류센터 구축(설치 전). [추정] 벤더 주장[^ref-1165] |
| 작업 대상 | 컨베이어·피킹 모듈, PLC·I/O 모듈과 제어 프로그램. [추정] 벤더 주장[^ref-1165] |
| 수행 자원 | 통합자 Bastian Solutions 가 에뮬레이션으로 설치 전에 검증. [추정] 벤더 주장[^ref-1165] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 전체 프로젝트 기간 18% 감소, 현장 시운전 5주 단축(기준선·측정 방법은 공개되지 않음). [추정] 벤더 주장[^ref-1165] |

Rockwell Automation 사례 소개(2024-08-28)에 실린 내용이며, 흐름 단계로는 피킹 모듈과 이를 잇는 컨베이어가 대상이다. 18%·5주 수치는 기준선과 측정 방법이 공개되지 않아 독립적으로 확인할 수 없다. [추정] 벤더 주장[^ref-1165]

**현장 유형:** 기타

**사례:** 대학 건물 1층을 실측 지도로 모델링해 이동로봇 시뮬레이션 시험 시나리오를 구성

| 항목 | 내용 |
|---|---|
| 시작 조건 | 이동로봇을 시뮬레이션으로 시험할 실행 가능한 시나리오가 필요함. [사실][^ref-1134] |
| 작업 대상 | 도면 DSL 로 만든 실내 환경(실측 점유 격자로 모델링한 대학 건물 1층), 동적 객체의 초기 자세, 시간·거리 조건으로 움직이는 문 같은 동적 요소. [사실][^ref-1134] |
| 수행 자원 | 시뮬레이션 안의 이동로봇이 주행 과제를 수행. [사실][^ref-1134] |
| 제약 | 해당 없음 |
| 완료·인계 | 위치 추정 오차·충돌 회피 같은 수용 기준을 시나리오에 명시해 판정. [사실][^ref-1134] |
| 예외·성과 | 현장 기록의 재생은 다루지 않았다. [사실][^ref-1134] |

이 사례는 현장 배치나 현장 기록 재생이 아니라, 실측 지도로 만든 대학 건물을 대상으로 한 시뮬레이션 시험 사례다. [사실][^ref-1134] 시나리오마다 수용 기준을 두는 방식은 재현 결과의 판정 기준을 정할 때 조합할 수 있는 요소로 보인다(11절 oq-132). [추정][^ref-1134]

이번 조사에서 상업 시설·가정 현장의 가상 시운전·재현 사례는 찾지 못했다. 실외는 자율주행 차량의 기록 기반 시뮬레이션(6절)이 재현 방법의 참고로 있을 뿐 로봇 현장 사례가 아니어서 싣지 않았다.

## 6. 대표 접근법과 기술

이 영역의 접근법은 1절의 네 가지 일에 따라 나뉘며, 이번 조사에서 근거가 가장 많은 것은 가상 시운전과 기록 재생이다.

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area36-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

가상 시운전의 정의와 시험 구성은 VDI/VDE 3693 이, 모델·시뮬레이션 결과의 수용은 NASA-STD-7009B 가 다루며, 여러 로봇 시뮬레이션과 기록 재생에는 Open-RMF 와 rosbag2 가 쓰인다. [사실][^ref-1126][^ref-1133][^ref-406][^ref-831]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area36-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 연구는 분산 가상 시운전, 시뮬레이션 예측력, 현실 격차, 형식 검증, 실제 기록 기반 재현, 시험 시나리오 구성을 다룬다.

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료](../../topics/2026/2026-09-30-area36-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 플릿 인터페이스의 가상 대응물을 붙여 오케스트레이션 논리와 운영 정책을 SiL 방식으로 시험하고, 재현 결과와 실제의 차이 지표를 관리하는 것으로 보인다. [추정][^ref-406][^ref-1130][^ref-1127] | 연계 대상: 물리·센서 시뮬레이션 엔진과 시뮬레이션 자산, 로봇 내부 주행·인식 제어의 현실 격차 보정(시뮬레이션 도구·로봇 제조사). [추정][^ref-741] |
| 시설·설비 제어 | 문·승강기 인터페이스의 가상 대응물 연결, 설비 에뮬레이터와 이어지는 인터페이스와 그 시험 결과 수용으로 보인다. [추정][^ref-406] | 연계 대상: 컨베이어·PLC·승강기 제어 코드의 에뮬레이션과 가상 시운전(설비 업체·통합자). [추정][^ref-1130][^ref-1131][^ref-1165] |
| 업종별 조건 | 재현 방법의 참고로만 가져오는 것으로 보인다. [추정][^ref-1128] | 연계 대상: 자율주행 차량의 기록 기반 시뮬레이션(해당 업계). [추정][^ref-1128] |

확인한 자료를 종합하면 ROP가 직접 맡을 범위는 제조사 플릿·문·승강기 인터페이스의 가상 대응물을 붙여 오케스트레이션 논리와 운영 정책을 설치 전에 SiL 방식으로 시험하는 환경, 재생 가능한 형태로 시각이 맞춰진 오케스트레이션 수준 실행 기록, 기록에서 시뮬레이션 초기 상태와 사건을 구성하는 기능, 재현 결과와 실제의 차이 지표와 수용 승인 기록의 관리로 보인다. [추정][^ref-406][^ref-831][^ref-1130][^ref-1127][^ref-1133][^ref-031] 이종 제조사를 잇는 ROP는 엔진·로봇 제어·설비 제어 코드를 직접 만들기보다 이들의 가상 모델·에뮬레이터와 연결되는 인터페이스와 시험 결과를 받아들이는 쪽을 맡는 것으로 보인다. [추정][^ref-1130][^ref-1131][^ref-1165][^ref-741][^ref-1128][^ref-406] 분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적으며, 기준은 [ROP 범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오 형식과 시뮬레이션 엔진, 재현의 원천 기록, 연동 대상 인터페이스, 적용 현장과 이어진다. [추정][^ref-406][^ref-831]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area36-s10.md)에 있다.

## 11. 열린 질문

재현 결과의 현실 일치 판정 기준과 단계별 검증 수준은 부분 근거만 있어 열린 질문으로 남는다. [추정][^ref-1127][^ref-1133]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 열린 질문](../../topics/2026/2026-09-30-area36-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) — 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건: 병원·제조 공장·물류창고·기타), 13절 각주 16건, 1차 조건부 승인 수정 11건 반영 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area36-s6.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "6. 대표 접근법과 기술" 절(1,605자)을 옮겼다 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area36-s4.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "4. 핵심 개념과 용어" 절(1,262자)을 옮겼다 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료](../../topics/2026/2026-09-30-area36-s8.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "8. 대표 연구와 자료" 절(1,238자)을 옮겼다 (실행 2026-09-30-17)
- 2026-09-30 · 생성 · [36. 가상 시운전·실제 상황 재현 — 열린 질문](../../topics/2026/2026-09-30-area36-s11.md) — 자동 분리: 36. 가상 시운전·실제 상황 재현 의 "11. 열린 질문" 절(1,205자)을 옮겼다 (실행 2026-09-30-17)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1126]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-1127]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-406]: Open Robotics, Simulation — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-943]: Lee 외 (Digital Health, SAGE), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1129]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-09-30
[^ref-1130]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-741]: Aljalbout, E., Xing, J., Romero, A. 외 (arXiv), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10-23, https://arxiv.org/abs/2510.20808, 접근일 2026-09-30
[^ref-1131]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-09-30
[^ref-1132]: 현대자동차그룹, 가상의 디지털 공간에 세운 쌍둥이 공장, 2023-11-21, https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330, 접근일 2026-09-30
[^ref-1133]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30
[^ref-1134]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-09-30
[^ref-1165]: Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation, 2024-08-28, https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html, 접근일 2026-09-30
```

### docs/categories/planning-and-business/index.md

````markdown
---
title: "A. 기획·사업"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-002, ref-023, ref-031, ref-044, ref-049, ref-060, ref-098, ref-101, ref-102, ref-103, ref-104, ref-105, ref-111, ref-115, ref-121, ref-125, ref-129, ref-130, ref-132, ref-133, ref-134, ref-146, ref-148, ref-149]
---

[홈](../../index.md) › A. 기획·사업

# A. 기획·사업

## 핵심 질문

어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? [분류원문]

## 개요

플랫폼을 들이기 전과 들이는 동안 무엇을 왜 할지 정하는 일. 기술·시장 동향 조사, 사용 사례·요구·책임 범위, 경제성·조달·사업 모델. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **1. 기술·시장·업체 동향** | 카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 | 어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? | [1. 기술·시장·업체 동향](technology-market-and-vendor-trends.md) | published |
| **2. 사용 사례·요구·책임 범위** | 로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 | 로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? | [2. 사용 사례·요구·책임 범위](use-cases-requirements-and-scope.md) | published |
| **3. 경제성·조달·사업 모델** | 투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 | 도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? | [3. 경제성·조달·사업 모델](economics-procurement-and-business-models.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

핵심은 **로봇 개별 성능과 업무 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 단계가 막히면 대기만 늘어날 수 있다. [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 A. 업무·공급망 설계 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


A. 업무·공급망 설계가 정한 업무는 다른 여섯 대분류의 세부영역으로 넘어가 실행되고 측정된다. 예를 들어 VDA 5050 은 외부 IT 시스템과의 인터페이스를 범위에서 제외하므로, 상위 주문을 로봇 작업 요청으로 번역하는 계층이 넘겨받는 지점이 될 것으로 보인다. [추정][^ref-031][^ref-125]

아래 연결은 게시된 23. 업무 시스템 연동 ~ 39. 운영 성과 측정·개선 페이지에서 검증된 주장을 근거로 한다. 연결 상대 세부영역은 대부분 아직 심화 조사 전이라, 상대편에 관한 서술도 A. 업무·공급망 설계 쪽 근거에 기댄다. 확인일은 2026-09-25이고, 출처별 발행일은 참고 자료 절의 각주에 있다.

```mermaid
flowchart LR
  a1["23. 업무 시스템 연동"]
  a2["24. 작업·워크플로 모델링"]
  a3["35. 처리능력·규모·배치 설계"]
  a4["39. 운영 성과 측정·개선"]
  b7["17. 작업 대상·자산 식별과 인계 추적"]
  b8["18. 실시간 세계 상태·데이터 일관성"]
  c9["20. 로봇·제조사 관제 연동"]
  c10["22. 설비·건물 시스템 연동"]
  c12["29. 명령·작업 실행의 신뢰성"]
  d13["25. 작업 배정 — MRTA"]
  d14["26. 작업 순서·스케줄링"]
  d16["28. 공용 자원·충전·에너지 최적화"]
  e17["30. 로봇 간 협업·물리적 인계"]
  e19["38. 모니터링·이상 탐지·원인 분석"]
  e20["32. 예외 복구·재계획·업무 연속성"]
  f22["34. 시뮬레이션·예측용 디지털 트윈"]
  f23["54. 시험·형식 검증·벤치마크"]
  g28["21. 상호운용 표준·적합성"]
  a1 --> c9
  a1 --> c12
  a1 --> d13
  a1 --> d14
  a1 --> e20
  a1 --> g28
  a2 --> b7
  a2 --> c12
  a2 --> e17
  a2 --> f23
  a3 --> c10
  a3 --> d13
  a3 --> d16
  a3 --> f22
  a4 --> b8
  a4 --> d16
  a4 --> e19
  a4 --> f22
```

### [옛 B. 공통 정보·환경 모델](../robot-ontology/index.md)

- **[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)** — '운반 완료'와 '인수 확인·재고 반영 완료'를 잇는 신호가 여기서 나온다. GS1 핵심 업무 어휘(Core Business Vocabulary, CBV)는 객체가 위치에 도착하는 arriving, 수령자 재고에 추가되는 receiving, 점유·소유가 바뀌는 accepting 을 서로 다른 업무 단계로 정의한다. [사실][^ref-044] VDA 5050 은 drop 동작의 완료를 적재물이 로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-031] 로봇 완료 신호는 arriving 수준의 물리적 인도에 가까우므로, 공정 모델의 '인수 확인·재고 반영 완료' 조건은 17. 작업 대상·자산 식별과 인계 추적이 다루는 식별자와 receiving·accepting 이벤트에 기대야 할 것으로 보인다. [추정][^ref-044][^ref-031][^ref-049] 이 구성을 적용한 표준·사례는 확인하지 못했다([열린 질문](../../open-questions.md) oq-001, oq-012).
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)** — Open-RMF 로봇 상태 스키마는 상태 값(idle·charging·working·error 등), 0~1 범위의 배터리, 현재 작업 id, 운영자가 대응할 문제 목록, 위치, 기록 시각을 담는다. [사실][^ref-148] 이 필드들은 가동률·충전 시간·오류 시간 같은 성과 지표를 계산하는 원천이 될 것으로 보이며, 이 연결은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽에 속한다. [추정][^ref-148]

### [옛 C. 연결·실행 기반](../integration/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)** — VDA 5050 3.0.0 명세는 관제 시스템과 이동로봇 사이 통신에 해당하지 않는 인터페이스, 곧 주변 설비·인프라·외부 IT 시스템과의 인터페이스를 범위에서 뺀다. [사실][^ref-031] 이처럼 로봇 인터페이스가 상위 시스템 연동을 범위 밖에 두므로, 상위 주문을 로봇 작업 요청(Open-RMF 작업 요청 등)으로 번역하는 계층이 두 대분류가 넘겨받는 지점이 될 것으로 보인다. [추정][^ref-031][^ref-125] 이 번역 계층을 규정한 표준은 확인하지 못했다.
- **[23. 업무 시스템 연동](../integration/business-system-integration.md)·[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)** — 상위 쪽 변경·취소 명령이 로봇 쪽 실행 상태와 만나는 지점이다. B2MML 거래 프로파일은 CHANGE·CANCEL 등의 거래 동사를 정의한다. [사실][^ref-129] OPC UA for ISA-95 Job Control 은 Update·Pause·Resume·Abort·Cancel 등의 작업 지시 메서드를 정의한다. [사실][^ref-130] 로봇 쪽 VDA 5050 은 주문을 수행하는 중에 다른 주문을 받으면 로봇이 OTHER_ORDER_ACTIVE 오류를 경고(WARNING) 수준으로 보고하게 한다. [사실][^ref-031] 취소할 수 없는 동작은 주문 취소(cancelOrder) 뒤에도 실행 중(RUNNING)을 거쳐 완료(FINISHED) 또는 실패(FAILED)로 보고하게 한다. [사실][^ref-031] Open-RMF 작업 상태 스키마는 queued·underway·completed·canceled·killed·failed 등의 상태 값, 시작·종료 시각, 소요 시간 추정, 취소·강제 종료·중단 요청 기록을 담는다. [사실][^ref-111] 이 기록은 두 세부영역이 상위 시스템에 되돌려 줄 결과의 원천이 될 것으로 보인다. [추정][^ref-111]
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)** — Open-RMF 데모의 호텔 환경은 승강기 2대, 여러 문, 3개 플릿(로봇 4대)이 다층 건물에서 함께 일하는 구성을 보이고, 공간과 승강기·문 같은 건물 설비를 공유하는 로봇의 교통 관리를 설명한다. [사실][^ref-104] 병원 약품 배송 로봇 사례에서는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다. [사실][^ref-060] 다층 호텔의 배송 로봇 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다. [사실][^ref-103] 두 사례는 병원·호텔이며 물류센터 적용 여부는 미확인이다([열린 질문](../../open-questions.md) oq-010). 35. 처리능력·규모·배치 설계은 승강기를 처리능력의 제약 입력으로만 받는다. 승강기 제어 자체는 분류 원문 19장의 시설·설비 제어 경계에 따라 연계 대상이며, ROP 는 22. 설비·건물 시스템 연동을 통해 작업 요청·예약·상태 확인을 맡는다.

### [옛 D. 계획·최적화](../planning-and-optimization/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)** — 웨이브·웨이브리스 출고 지시 정책 연구(Gallien·Weber, 2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(Lorenz 외, 2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. [추정][^ref-134][^ref-133]
- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)** — 작업자가 피킹하고 자율이동로봇(Autonomous Mobile Robot, AMR)이 운반하는 동적 주문 피킹 연구(2025)는 AMR 가용성에 따른 개입 전략을 다룬다. [추정][^ref-132] 이 연구는 주문 변경과 로봇 배정이 맞물리는 사례가 될 것으로 보인다. [추정][^ref-132]
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)** — Open-RMF 플릿 어댑터 템플릿 설정은 배터리가 recharge_threshold(예시값 0.10) 아래로 내려간 로봇에게 작업을 맡기지 않게 한다. [사실][^ref-105] 또 충전 목표(recharge_soc), 로봇별 충전기, 작업 종료 후 동작(park·charge·nothing)을 둔다. [사실][^ref-105]
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)** — AMR 물류센터 시뮬레이션 연구(2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. [사실][^ref-102] 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS)의 충전·배터리 교환 전략을 비교한 연구(2018)도 있다. [사실][^ref-098]
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)** — Omega(2024)에 실린 연구는 RMFS 에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. [사실][^ref-146] 이 수치는 모델·시뮬레이션 조건의 저자 보고값이며 현장 실측이 아니다. [사실][^ref-146]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)** — 상위 시스템의 취소(CANCEL)가 로봇이 화물을 이미 실은 뒤에 오거나, 취소할 수 없는 동작이 끝까지 수행될 수 있다. [추정][^ref-031][^ref-129] 이 경우 되돌림 작업과 재고 반영이 복구·재계획 과제로 넘어갈 것으로 보인다. [추정][^ref-031][^ref-129] 되돌림 규칙을 정한 표준·사례는 확인하지 못했다([열린 질문](../../open-questions.md) oq-021).
- **[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)** — 공정 모델이 완료 조건으로 삼을 수 있는 인계 확인 신호가 여기에 있다. Open-RMF 배송 작업에서 로봇은 하역 지점의 워크셀(workcell)에 IngestorRequest 를 보내고, IngestorResult 를 받을 때까지 이를 반복한다. [사실][^ref-023] IngestorResult 는 시각, 요청 id, 워크셀 id, 상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-049]
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)** — 제조 처리량의 병목 탐지 방법을 검토한 문헌(2023)과 창고 이벤트 로그에 프로세스 마이닝을 적용한 사례(2015)가 있다. [추정][^ref-115][^ref-149] 이를 로봇 상태 기록에 적용하면 성과 분석과 이상·원인 분석이 같은 로그를 공유할 것으로 보인다. [추정][^ref-115][^ref-149][^ref-148] 이런 적용 연구는 확인하지 못했다([열린 질문](../../open-questions.md) oq-018).

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- **[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)** — 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있다. [추정][^ref-121] 따라서 공정 모델의 형식적 설계 점검은 형식 검증과 이어질 것으로 보인다. [추정][^ref-121] 물류 로봇 공정에 적용한 사례는 확인하지 못했다.
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)** — RAWSim-O 는 RMFS 운영의 여러 결정 문제가 미치는 효과를 연구하기 위한 이산 사건 시뮬레이션이다. [사실][^ref-101] 이런 도구는 증차·증설처럼 가정한 미래를 실험하는 데 쓰일 것으로 보인다. [추정][^ref-101]
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)** — 우선순위 정책이나 충전 대안을 운영 전에 비교하는 일은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽 일이다. 이 일은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과 역할을 나눠 연결될 것으로 보인다. [추정][^ref-146][^ref-102]

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)** — ISA-95 계열의 작업 지시 동사·메서드와 VDA 5050·Open-RMF 의 주문·작업 요청을 잇는 표준 매핑은 이번 조사 범위에서 확인되지 않았다. 그래서 번역 규칙을 누가 소유하고 누가 변경을 승인하는지가 상호운용성 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-129][^ref-130][^ref-031][^ref-125] 관련 질문은 [열린 질문](../../open-questions.md) oq-020 이다.

### 아직 다루지 않은 연결

42. 분산 시스템·통신·컴퓨팅 구조, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 48. 안전·위험 관리, 51. 인증·권한·격리, 47. AI·학습·적응과 모델 운영과의 연결은 검증된 근거가 아직 없어 싣지 않았다. 해당 세부영역의 조사가 게시되면 보강한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 68건이다(논문 19건 · 기사·보고서 23건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 24건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1104](../../references/ref-1104.md) — Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study (발행 2026-04-14)
- [ref-1161](../../references/ref-1161.md) — Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios (발행 2026-04)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-1160](../../references/ref-1160.md) — Lee, J. S., & Aswani, A. (arXiv), Profit Maximization for a Robotics-as-a-Service Model (발행 2025-09-30)
- [ref-165](../../references/ref-165.md) — Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자, Large Language Models for Multi-Robot Systems: A Survey (발행 2025-02)
- [ref-133](../../references/ref-133.md) — Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? (발행 2025)
- [ref-132](../../references/ref-132.md) — Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations (발행 2025)
- [ref-102](../../references/ref-102.md) — Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics (발행 2025)
- [ref-1162](../../references/ref-1162.md) — Sivalingam, C. S., & Subramaniam, S. K. (Heliyon), Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process (발행 2024-02-15)
- [ref-146](../../references/ref-146.md) — Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority (발행 2024)
- 그 밖에 9건

**기사·보고서**

- [ref-909](../../references/ref-909.md) — 서울신문, 부품 배치 '척척' 무거운 짐도 '사뿐'… 아틀라스 2.5만대 로봇 학교 간다 (발행 2026-09-23)
- [ref-908](../../references/ref-908.md) — 아시아경제, CJ대한통운, 물류업계 최초 AI 휴머노이드 상용화 '첫발' (발행 2026-09-03)
- [ref-1170](../../references/ref-1170.md) — Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream (발행 2026-06-01)
- [ref-901](../../references/ref-901.md) — International Federation of Robotics (IFR), Robot Density Surges in Europe, Asia, and Americas (발행 2026-04-08)
- [ref-1200](../../references/ref-1200.md) — 아시아경제, 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인) (발행 2026-03-16)
- [ref-903](../../references/ref-903.md) — 로봇신문 (한국로봇산업진흥원 '2024년 국내 로봇산업 실태조사 결과 보고서' 요약), [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약 (발행 2026-01-25)
- [ref-902](../../references/ref-902.md) — International Federation of Robotics (IFR), Top 5 Global Robotics Trends 2026 (발행 2026-01-08)
- [ref-1166](../../references/ref-1166.md) — 전자신문, 조달청, 2026년 혁신제품 시범구매 기본계획 발표 (발행 2025-12-18)
- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)
- [ref-899](../../references/ref-899.md) — International Federation of Robotics (IFR), World Robotics 2025 report – SERVICE ROBOTS – released by IFR (발행 2025-10-07)
- 그 밖에 13건

**업체 발표**

- [ref-906](../../references/ref-906.md) — Agility Robotics, Digit Moves Over 100,000 Totes in Commercial Deployment (발행 2025-11-20)
- [ref-1163](../../references/ref-1163.md) — AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics? (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-1158](../../references/ref-1158.md) — Messina, E. & Saidi, K. S. (NIST, National Institute of Standards and Technology), Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054) (발행 2024-06-07)
- [ref-130](../../references/ref-130.md) — OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) (발행 2024-01-31)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-129](../../references/ref-129.md) — MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd (발행 2023)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-1195](../../references/ref-1195.md) — 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수 (발행 2020-06-25)
- [ref-1203](../../references/ref-1203.md) — ISO / IEC / IEEE, ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering (발행 2018)
- [ref-1167](../../references/ref-1167.md) — IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing (발행 2017-01-27)
- [ref-947](../../references/ref-947.md) — 한국로봇산업진흥원, 서비스로봇 실증사업 (발행 미확인)
- 그 밖에 14건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [3. 경제성·조달·사업 모델](economics-procurement-and-business-models.md) — 섹션 3~11 신규 작성(현장 유형 사례 5건: 물류창고·제조 공장·병원 2·상업 시설, 표준·제도 6건, 자료 8건, 경계 2행, 연결 16개, 열린 질문 9건), 프런트매터 채움, 13절 각주. 2차: 3절 첫 문장을 설문 범위로 한정, ref-031 접근일 2026-09-30 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area03-s6.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "6. 대표 접근법과 기술" 절(1,380자)을 옮겼다. 2차: ref-031 접근일 2026-09-30 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area03-s8.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "8. 대표 연구와 자료" 절(1,281자)을 옮겼다 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 열린 질문](../../topics/2026/2026-09-30-area03-s11.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "11. 열린 질문" 절(1,265자)을 옮겼다 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area03-s10.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,106자)을 옮겼다. 2차: ref-031 접근일 2026-09-30 (실행 2026-09-30-19)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-115]: Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes, 2023, https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-149]: Springer(학술대회 발표 논문, 저자 미확인), Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study, 2015, https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/planning-and-business/technology-market-and-vendor-trends.md (요약)

```markdown
# 1. 기술·시장·업체 동향

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **기술·연구 동향 조사**: 카테고리마다 논문·기사·업체 발표를 모아 연구와 제품의 흐름을 추적한다
- **시장·업체·제품 지형**: 오케스트레이션·관제·상호운용 제품, 로봇 제조사, 통합 사업자의 지형을 정리한다
- **로봇 종류·형태 지형**: AMR·AGV·로봇팔·모바일 매니퓰레이터·사족 보행·휴머노이드·드론처럼 오케스트레이션 대상 로봇의 종류와 특성 변화를 추적한다

## 2. 핵심 질문

어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]
```

### docs/categories/planning-and-business/use-cases-requirements-and-scope.md (요약)

```markdown
# 2. 사용 사례·요구·책임 범위

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **책임 범위 정의**: 플랫폼이 직접 맡을 범위와 외부(업무 시스템·로봇 자체 지능·설비 제어·현장 간 운송·업종별 조건)에 맡길 범위를 정한다
- **사용 사례 발굴·요구 정의**: 로봇에게 맡길 일과 성공 기준·수용 기준을 정한다
- **현장 유형별 요구 정리**: 물류창고·제조 공장·병원·상업 시설·가정·실외 같은 현장 유형마다 공통 요구와 고유 요구를 정리한다

## 2. 핵심 질문

로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
```

### docs/categories/robot-ontology/index.md

````markdown
---
title: "B. 로봇 온톨로지"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-003, ref-162, ref-031, ref-044, ref-148, ref-228, ref-105, ref-040, ref-153, ref-051, ref-286, ref-079, ref-023, ref-049, ref-285, ref-284, ref-282, ref-287, ref-236, ref-041, ref-014, ref-015, ref-024, ref-238, ref-239, ref-080, ref-224, ref-291, ref-290, ref-076, ref-234, ref-240, ref-138, ref-159]
---

[홈](../../index.md) › B. 로봇 온톨로지

# B. 로봇 온톨로지

## 핵심 질문

서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

## 개요

서로 다른 제조사의 로봇을 등록하고, 무엇을 할 수 있는지 공통 모델로 표현하고, 그 모델로 시스템과 로봇이 쉽게 연동되게 하는 온톨로지 기능 전체. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **4. 이기종 로봇 등록** | 서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 | 제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? | [4. 이기종 로봇 등록](heterogeneous-robot-registration.md) | published |
| **5. 로봇 능력·작업 표현** | 능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 | 로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? | [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) | published |
| **6. 온톨로지 기반 시스템·로봇 연동** | 온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 | 온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? | [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md) | published |
| **7. 온톨로지 검증·변경 관리** | 온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 | 온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? | [7. 온톨로지 검증·변경 관리](ontology-verification-and-change-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

같은 기능도 제조사마다 이름·매개변수·실행 조건이 다르다. **능력을 공통 모델로 표현해야** 작업에 맞는 로봇을 질의로 찾고, 새 로봇을 연동할 때 반복 작업을 줄일 수 있다. [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 B. 공통 정보·환경 모델 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


이 절은 B. 공통 정보·환경 모델의 게시된 세부영역 페이지(5. 로봇 능력·작업 표현, 15. 지도·공간·위치 모델, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성)의 검증된 주장과 각주를 근거로, 이 대분류의 모델이 다른 대분류의 어느 세부영역과 무엇으로 이어지는지 정리한다. 연결 상대 세부영역 가운데 상당수는 아직 본문이 없으므로, 연결의 근거는 이 대분류 쪽 자료에 기댄다.

```mermaid
graph LR
  B5["5. 로봇 능력·작업 표현"]
  B6["15. 지도·공간·위치 모델"]
  B7["17. 작업 대상·자산 식별과 인계 추적"]
  B8["18. 실시간 세계 상태·데이터 일관성"]
  CatA["A. 업무·공급망 설계"]
  CatC["C. 연결·실행 기반"]
  CatD["D. 계획·최적화"]
  CatE["E. 협업·현장 운영"]
  CatF["F. 도입·검증·유지관리"]
  CatG["G. 안전·보안·지능·거버넌스"]
  B5 --> CatC
  B5 --> CatD
  B5 --> CatF
  B5 --> CatG
  B6 --> CatA
  B6 --> CatC
  B6 --> CatD
  B6 --> CatF
  B6 --> CatG
  B7 --> CatA
  B7 --> CatC
  B7 --> CatE
  B8 --> CatA
  B8 --> CatC
  B8 --> CatE
  B8 --> CatF
  B8 --> CatG
```

### [옛 A. 업무·공급망 설계](../planning-and-business/index.md)

- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md): GS1 GLN 은 도크 문·보관 위치 같은 하위 위치를 식별할 수 있고 GLN 확장 요소는 조직 내부나 거래 당사자 간 합의로만 쓰므로, 업무 위치와 로봇 지도 장소의 대응은 ROP 쪽 대응 계층이 맡게 될 것으로 보인다. [추정][^ref-162][^ref-031] 국내 사례는 [열린 질문](../../open-questions.md) oq-029 에서 다룬다.
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md): GS1 CBV 는 도착(arriving)·입고(receiving)·인수(accepting)를 서로 다른 업무 단계로 정의하고, VDA 5050 은 하역(drop) 완료를 적재물이 로봇을 떠나 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-044][^ref-031] 같은 연결은 [A. 업무·공급망 설계](../planning-and-business/index.md) 페이지의 다른 대분류와의 연결 절에도 같은 각주로 실려 있다.
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md): Open-RMF 로봇 상태 스키마는 상태(idle·charging·working·error 등), 배터리, 현재 작업 id, 문제 목록, 위치, 기록 시각을 담는다. [사실][^ref-148] 이 필드들은 가동률·충전·오류 시간 지표의 원천이 될 것으로 보인다. [추정][^ref-148] 이 연결도 [A. 업무·공급망 설계](../planning-and-business/index.md) 페이지와 같은 각주를 쓴다.

### [옛 C. 연결·실행 기반](../integration/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 팩트시트는 적재 명세(loadSets: 적재 유형·최대 중량·처리 높이·픽·드롭 소요 시간)와 지원 동작(mobileRobotActions)을 선언하고, Open-RMF 플릿 어댑터 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다. [사실][^ref-228][^ref-105] 두 자료는 서로 다른 인터페이스의 사례다.
- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md): 팩트시트에서 선언한 동작 이름(actionType)이 명령과 완료 보고에 그대로 쓰이고 Open-RMF 어댑터가 로봇 API 의 완료 확인 뒤 완료를 알리므로, 능력 선언이 실행 확인의 기준 어휘가 될 것으로 보인다. [추정][^ref-228][^ref-040]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): Open-RMF 플릿 어댑터는 로봇 좌표계가 RMF 와 다르면 같은 위치를 가리키는 좌표 쌍으로 회전·축척·이동 변환을 추정하며(대응점 4개 이상 권장), 템플릿 설정은 층별 reference_coordinates 로 이 좌표 쌍을 둔다. [사실][^ref-153][^ref-105] 이 작업은 용어집의 [지도 정합](../../glossary/map-alignment.md)에 해당한다. VDA 5050 상태 스키마는 위치추정 품질(localizationScore), 편차 범위(deviationRange), 지도 식별자(mapId)를 두며, 편차를 추정할 수 없는 로봇은 편차 범위를 생략할 수 있다. [사실][^ref-051] 그래서 위치 신뢰도 보고가 제조사 구현에 따라 달라질 수 있다. [추정][^ref-051] 수용 기준은 열린 질문 oq-028 에서 다룬다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 승강기 상태는 층을 층 이름 문자열(available_floors, current_floor, destination_floor)로 나타내므로, 지도의 층 이름과 승강기의 층 이름을 맞추는 대응이 두 대분류 사이에 필요할 것으로 보인다. [추정][^ref-286][^ref-079] 이 대응 규칙은 새 열린 질문으로 올렸고, 공통 좌표계 대응(oq-027)·업무 위치 대응(oq-029)과 함께 본다.
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 상태 스키마의 적재물 목록(loads)은 로봇이 취급 중인 적재물을 담되 적재 상태를 판단할 수 없는 로봇은 생략할 수 있고, 적재물 식별 번호(loadId)는 바코드·RFID 같은 식별 값이며 아직 식별하지 않았으면 비워 둔다. [사실][^ref-051]
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 배송 작업에서 로봇은 픽업 지점 워크셀에서 DispenserResult 를, 하역 지점 워크셀에서 IngestorResult 를 받을 때까지 요청을 되풀이한다. [사실][^ref-023] IngestorResult 는 시각, 요청 id, 워크셀 id, 상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-049]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 문·승강기 상태 메시지는 시각 필드(door_time, lift_time)를 담고, 승강기 어댑터는 적절하다고 판단한 요청만 승강기에 전달한다. [사실][^ref-285][^ref-286][^ref-284] 상태 발행 주기나 오래됨 판정 규칙은 이번에 연 승강기 연동 문서 범위에서는 찾지 못했다. [추정][^ref-284]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지처럼 통신 계층에도 상태의 오래됨을 알리는 장치가 있다. [사실][^ref-282][^ref-287][^ref-031] 세 출처는 각각 한 장치만 다룬다.

### [옛 D. 계획·최적화](../planning-and-optimization/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md): 이종 다중 로봇 작업 배정에서 온톨로지 기반 실행 가능성 판정 결과를 배정기와 독립된 입력으로 넘기는 연구가 있다(2026-08 발행). [사실][^ref-236] 제조사가 광고한 능력과 운용 중 관측된 능력을 온톨로지로 구분해 통합하는 연구도 있어, 배정 기준을 어느 값으로 둘지가 두 대분류 사이의 쟁점이 될 것으로 보인다(열린 질문 oq-024). [추정][^ref-041]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): Open-RMF traffic-editor 로 주석한 차선·경유점 그래프는 building_map_generator 로 주행 그래프(navigation graph)로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. [사실][^ref-079]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md): traffic-editor 는 주차 위치·충전기 위치·승강기·문·층을 지도에 주석하게 하므로, 공용 자원의 위치 정보가 지도 모델에서 나온다. [사실][^ref-079]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md): 설비의 인수 결과에는 화물 식별자·인계 당사자가 없고 EPCIS 는 소유·점유·위치 이전을 출발지·도착지(source/destination)로 표현하므로, 물리적 인계 확인은 17. 작업 대상·자산 식별과 인계 추적의 식별·인계 기록과 결합해야 할 것으로 보인다(열린 질문 oq-001). [추정][^ref-049][^ref-014][^ref-015]
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): 팔레트 RFID 태그 판독성이 제품·포장·태그 위치·적재 패턴에 따라 달라진다는 2009년 실험 보고가 있어, 판독 실패 때 인계 보류·재스캔·사람 확인 규칙이 복구 과제로 넘어갈 것으로 보인다(열린 질문 oq-003). [추정][^ref-024]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): 로봇 상태의 문제 목록·오류 상태와 설비 상태의 시각 정보를 한 세계 상태에 모으면, 지연 원인이 로봇인지 문인지 구분하는 분석이 같은 상태 기록을 쓰게 될 것으로 보인다. [추정][^ref-148][^ref-285]

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md): 매뉴얼·로봇 기술 파일을 해석해 능력 모델 초안을 만드는 일은 새 로봇 등록 때 필요한 작업이 될 것으로 보이며, 이는 분류 개정 전 원문 8장의 매뉴얼 해석 교차 규칙과 같은 방향이다. [추정][^ref-238][^ref-239] 온보딩 현장에 적용한 사례는 아직 확인하지 못했다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md): 도면에서 만든 지도에는 대기 위치 같은 운영 요소와 도면–현장 편차가 자동으로 담기지 않아, 시운전 때 사람의 주석·정렬 단계가 남는 것으로 보인다(열린 질문 oq-022). [추정][^ref-079][^ref-080][^ref-224]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md): 제조 분야를 대상으로 한 분류 자료는 현장 상태가 한 방향으로 자동 반영되는 [디지털 섀도](../../glossary/digital-shadow.md)와 디지털 트윈을 구분하므로, 18. 실시간 세계 상태·데이터 일관성은 현재 상태 표현을, 34. 시뮬레이션·예측용 디지털 트윈은 그 표현을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다. [추정][^ref-291][^ref-290] 근거 자료가 물류가 아닌 제조 대상이라는 한계가 있다.

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md): 대규모 언어 모델(Large Language Model, LLM)로 능력 온톨로지를 생성하는 연구(2024-04)와 로봇 기술 파일(URDF)에서 로봇 온톨로지를 LLM 으로 채우는 연구(2026-06)가 있다. [사실][^ref-238][^ref-239] 매뉴얼 해석의 적용 대상은 위 55. 현장 조사·설치·시운전 연결과 함께 본다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md): 비전 언어 모델로 평면도 지도를 해석하는 연구(2024-09)가 있어, 분류 개정 전 원문 8장 교차 규칙의 도면 해석이 두 대분류를 잇는다. [사실][^ref-076]
- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md): 무인운반차 기술 데이터 서브모델 IDTA 02047, 서비스 로봇 모듈 공통 정보 모델 ISO 22166-201(2024-02), 국내 KS B 7321-2 같은 제조사 독립 정보 모델 표준이 있다. [사실][^ref-234][^ref-240][^ref-138] KS 부합화 여부는 열린 질문 oq-004·oq-026 에서 다룬다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md): ISO 21423 은 산업용 이동로봇의 통신·상호운용성을 다루는 표준이다. [사실][^ref-159] 그 공통 좌표계가 제조사 지도 식별자와 어떻게 대응하는지는 아직 확인되지 않았다(열린 질문 oq-027).
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md): Open-RMF 승강기 상태의 운영 모드에 사람·AGV·화재·오프라인·비상이 있으므로, 탑승 확정 전에 최신 모드를 확인하는 규칙이 안전 조건과 맞물릴 것으로 보인다. [추정][^ref-286] 여기서 ROP 는 상태를 확인하는 범위만 맡고, 설비 안전 제어 자체는 분류 원문 19장 시설·설비 제어 경계의 연계 대상이다.

### 아직 다루지 않은 연결

26. 작업 순서·스케줄링, 31. 사람–로봇 협업, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리, 51. 인증·권한·격리 와 이 대분류 세부영역 사이의 연결은 게시 페이지에 검증된 근거가 없어 싣지 않았다. 이 연결은 해당 세부영역 조사가 진행되면 보강한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 88건이다(논문 40건 · 기사·보고서 1건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 47건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-894](../../references/ref-894.md) — Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying (발행 2026-09-08)
- [ref-236](../../references/ref-236.md) — Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation (발행 2026-08-11)
- [ref-239](../../references/ref-239.md) — Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF (발행 2026-06)
- [ref-201](../../references/ref-201.md) — Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A., From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation (발행 2026-06)
- [ref-898](../../references/ref-898.md) — Osmani, A., From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance (발행 2026-05-05)
- [ref-896](../../references/ref-896.md) — Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J., Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models (발행 2026-04-17)
- [ref-895](../../references/ref-895.md) — Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation (발행 2026-04-03)
- [ref-041](../../references/ref-041.md) — Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots (발행 2025-10-02)
- [ref-890](../../references/ref-890.md) — Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics (발행 2025-09-26)
- [ref-880](../../references/ref-880.md) — Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics (발행 2025-04-30)
- 그 밖에 30건

**기사·보고서**

- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-874](../../references/ref-874.md) — OPC Foundation, OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02) (발행 2025-09-08)
- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-198](../../references/ref-198.md) — IDTA(Industrial Digital Twin Association), IDTA 02047-1-0 Technical Data for AGV in Intralogistics (발행 2025-03)
- [ref-240](../../references/ref-240.md) — ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules (발행 2024-02)
- [ref-035](../../references/ref-035.md) — Plattform Industrie 4.0, Information Model for Capabilities, Skills & Services (발행 2022-11)
- [ref-026](../../references/ref-026.md) — IEEE, IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology (발행 2022)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-459](../../references/ref-459.md) — W3C RDF Data Shapes Working Group, Shapes Constraint Language (SHACL) (W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음) (발행 2017)
- [ref-025](../../references/ref-025.md) — IEEE, 1872-2015 - IEEE Standard Ontologies for Robotics and Automation (발행 2015)
- [ref-886](../../references/ref-886.md) — W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition) (발행 2012-12-11)
- 그 밖에 37건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [7. 온톨로지 검증·변경 관리](ontology-verification-and-change-management.md) — 영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건·2차 수정 4건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area07-s6.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "6. 대표 접근법과 기술" 절(2,811자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 대표 연구와 자료](../../topics/2026/2026-09-29-area07-s8.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "8. 대표 연구와 자료" 절(1,834자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area07-s4.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "4. 핵심 개념과 용어" 절(1,478자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 열린 질문](../../topics/2026/2026-09-29-area07-s11.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "11. 열린 질문" 절(1,150자)을 옮겼다. 2차 수정: 신규 질문 4번째의 태그를 진술 문장으로 옮김 (실행 2026-09-29-09)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-162]: GS1, Identifying a physical location - GLN, 미확인, https://www.gs1.org/standards/id-keys/gln/physical-location, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25
[^ref-285]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-014]: GS1, Core Business Vocabulary (CBV) Standard, 미확인, https://ref.gs1.org/standards/cbv/, 접근일 2026-09-25 (원문 미열람)
[^ref-015]: GS1, EPCIS and CBV Implementation Guideline, 미확인, https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-024]: Singh, J. 외, RFID tag readability issues with palletized loads of consumer goods, 2009, https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864, 접근일 2026-09-25 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-09-25 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-09-25 (원문 미열람)
[^ref-080]: Open Robotics, Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html, 접근일 2026-09-25 (원문 미열람)
[^ref-224]: Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H., Tightly Coupled SLAM with Imprecise Architectural Plans, 2024-08, https://arxiv.org/abs/2408.01737, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-290]: NIST, DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH, 미확인, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417, 접근일 2026-09-25 (원문 미열람)
[^ref-076]: DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps, 2024-09, https://arxiv.org/abs/2409.12842, 접근일 2026-09-25 (원문 미열람)
[^ref-234]: IDTA(Industrial Digital Twin Association), IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-240]: ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules, 2024-02, https://www.iso.org/standard/82334.html, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-09-25 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/robot-ontology/heterogeneous-robot-registration.md (요약)

```markdown
# 4. 이기종 로봇 등록

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/robot-ontology/robot-capability-and-task-representation.md (요약)

```markdown
# 5. 로봇 능력·작업 표현

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇 능력 표현**: 이동·계단·적재·도어 조작·충전·파지·점검 같은 능력을 매개변수·입출력·전제조건·제약·실패 모드와 함께 공통 모델로 표현한다
- **작업 유형·작업 요구 표현**: 배송·운반·인계·순찰·점검·조작 같은 작업 유형과 각 작업이 요구하는 능력·조건을 능력 모델과 같은 어휘로 표현한다
- **환경 조건과 능력 대조**: 층·문·승강기·계단·충전기 같은 공간 조건을 온톨로지에 함께 담아 로봇별로 지나갈 수 있는 곳과 쓸 수 있는 시설을 판단한다
- **표현 표준 정렬**: 능력·작업 표현을 로봇 온톨로지 표준(IEEE 1872 계열), VDA 5050 팩트시트, 자산 관리 셸 같은 기존 규격과 대응시킨다
- **온톨로지 저장·질의 기반**: 온톨로지를 저장하고 질의하는 기술(그래프 데이터베이스, RDF·OWL, SPARQL, JSON 스키마)을 고르고 성능을 확인한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md), [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 5번 영역 ‘로봇 능력·작업 온톨로지’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [옛 분류원문]

> 옛 질문: 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md (요약)

```markdown
# 6. 온톨로지 기반 시스템·로봇 연동

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]
```

### docs/categories/robot-ontology/ontology-verification-and-change-management.md (요약)

```markdown
# 7. 온톨로지 검증·변경 관리

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **온톨로지 검증**: 역량 질문, 원문 대조, 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)로 완전성과 정확성을 확인한다
- **온톨로지 버전·변경 관리**: 문서·펌웨어 개정에 따라 능력 정의의 버전을 관리하고, 영향받는 작업·현장을 찾아 다시 검증한다

## 2. 핵심 질문

온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]
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
| **9. 채팅으로 시나리오 구성** | 대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 | 할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? | [9. 채팅으로 시나리오 구성](chat-scenario-composition.md) | published |
| **10. 채팅으로 로봇 구성** | 대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 | 어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? | [10. 채팅으로 로봇 구성](chat-robot-configuration.md) | published |
| **11. 채팅으로 실제 상황 시뮬레이션 재현** | 실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 | 실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? | [11. 채팅으로 실제 상황 시뮬레이션 재현](chat-real-situation-simulation-replay.md) | published |
| **12. 채팅으로 업무 지시·오케스트레이션** | 대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 | 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? | [12. 채팅으로 업무 지시·오케스트레이션](chat-task-instruction-and-orchestration.md) | published |
| **13. 대화형 기능의 신뢰·기반** | 오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 | 언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? | [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

대화 결과는 실행 명령이 아니라 계획이다. **사람이 확인·승인한 계획만 실행**되어야 언어 모델의 잘못된 해석이 로봇 동작으로 이어지지 않는다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 89건이다(논문 70건 · 기사·보고서 1건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 16건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-819](../../references/ref-819.md) — Valerio, D., Kogler, P., Bischof, S., Hubauer, T., & Rangwala, H., Neuro-symbolic AI for Industrial Configuration (발행 2026-09-24)
- [ref-759](../../references/ref-759.md) — Ko, T.-H., & Lin, C.-T.(National Central University), Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin (발행 2026-09)
- [ref-832](../../references/ref-832.md) — Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models (발행 2026-08-22)
- [ref-842](../../references/ref-842.md) — Tao, M., Tao, Y., & Wang, P., Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents (발행 2026-08-16)
- [ref-865](../../references/ref-865.md) — Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways (발행 2026-07-23)
- [ref-841](../../references/ref-841.md) — Tack, J., Laban, P., & Neville, J., LLMs Get Lost in Evolving User Intent (발행 2026-07-22)
- [ref-867](../../references/ref-867.md) — Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement (발행 2026-07-20)
- [ref-826](../../references/ref-826.md) — Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins (발행 2026-07-19)
- [ref-838](../../references/ref-838.md) — Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports), Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts (발행 2026-07-18)
- [ref-833](../../references/ref-833.md) — Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving (발행 2026-07-15)
- 그 밖에 60건

**기사·보고서**

- [ref-855](../../references/ref-855.md) — OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025 (발행 2025)

**업체 발표**

- [ref-817](../../references/ref-817.md) — 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 (발행 2026-08-24)
- [ref-823](../../references/ref-823.md) — 폴라리스3D(Polaris3D), AMR 도입 ROI 어떻게 계산할까? 물류 자동화 투자 회수 기간 알아보기 (발행 2026-06-12)

**표준·오픈소스·기관 자료**

- [ref-854](../../references/ref-854.md) — Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) (발행 2026-06-25)
- [ref-862](../../references/ref-862.md) — 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) (발행 2025-08)
- [ref-856](../../references/ref-856.md) — Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18) (발행 2025-06-18)
- [ref-863](../../references/ref-863.md) — European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) (발행 2024-06-13)
- [ref-860](../../references/ref-860.md) — 과학기술정보통신부·한국정보통신기술협회(TTA), 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기) (발행 2024-02)
- [ref-851](../../references/ref-851.md) — 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)), 거대언어모델 기반 로봇 인공지능 기술 동향 (발행 2024-02)
- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-831](../../references/ref-831.md) — ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications) (발행 미확인)
- [ref-229](../../references/ref-229.md) — IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) (발행 미확인)
- [ref-125](../../references/ref-125.md) — Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json (발행 미확인)
- 그 밖에 6건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) — 3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-868 신규, ref-351·ref-840·ref-165·ref-753 재사용), 상업 시설 사례 1건, 열린 질문 4건 추가, 1차 조건부 승인 수정 7건 이행 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area13-s6.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "6. 대표 접근법과 기술" 절(3,607자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료](../../topics/2026/2026-09-29-area13-s8.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "8. 대표 연구와 자료" 절(1,988자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 열린 질문](../../topics/2026/2026-09-29-area13-s11.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "11. 열린 질문" 절(1,562자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area13-s4.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "4. 핵심 개념과 용어" 절(1,495자)을 옮겼다 (실행 2026-09-29-06)
<!-- auto:category-recent:end -->
```

### docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md (요약)

```markdown
# 8. 채팅으로 맵 작성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 맵 작성**: 공간을 글이나 말로 설명하거나 도면·사진을 올리면 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다
- **대화 중 지도 확인·확정**: 대화로 만든 지도를 화면에 보여 주고, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 확인 질문으로 받아 확정한다

## 2. 핵심 질문

공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md (요약)

```markdown
# 9. 채팅으로 시나리오 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-robot-configuration.md (요약)

```markdown
# 10. 채팅으로 로봇 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 로봇 구성**: 투입할 로봇의 종류·대수·장착 장비·초기 위치·역할을 대화로 정하고, 온톨로지로 수행 가능 여부를 확인해 알려 준다
- **로봇 구성 적합성 사전 확인**: 대화로 정한 로봇 구성이 시나리오의 작업·공간·시설 조건을 채우는지 실행 전에 확인하고 부족한 능력이나 대수를 알려 준다

## 2. 핵심 질문

어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md (요약)

```markdown
# 12. 채팅으로 업무 지시·오케스트레이션

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
```

### docs/categories/space-and-map-model/index.md

```markdown
---
title: "D. 공간·지도 모델"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › D. 공간·지도 모델

# D. 공간·지도 모델

## 핵심 질문

로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

## 개요

건물 도면·센서 지도·좌표계를 하나의 공간 모델로 만들고, 장소에 의미를 붙이고, 바뀔 때 관리하는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **14. 도면·BIM에서 지도 만들기** | 평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 | 이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? | [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md) | published |
| **15. 지도·공간·위치 모델** | 로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 | 제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? | [15. 지도·공간·위치 모델](map-space-and-location-model.md) | published |
| **16. 장소 의미·지도 관리** | 장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 | 같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? | [16. 장소 의미·지도 관리](place-semantics-and-map-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 54건이다(논문 20건 · 기사·보고서 2건 · 업체 발표 1건 · 표준·오픈소스·기관 자료 31건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-163](../../references/ref-163.md) — 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (발행 2026)
- [ref-1018](../../references/ref-1018.md) — Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv), osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning (발행 2025-07)
- [ref-083](../../references/ref-083.md) — Zhang, J. 외, Generation of Indoor Open Street Maps for Robot Navigation from CAD Files (발행 2025-07)
- [ref-161](../../references/ref-161.md) — Abdul Hafez, O., Joerger, M., & Spenko, M., Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach (발행 2025-05)
- [ref-073](../../references/ref-073.md) — Luo, R. 외, ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting (발행 2025-03)
- [ref-160](../../references/ref-160.md) — Prakhya, S. M., Yang, L., & Liu, Z., Lifelong 3D Mapping Framework for Hand-held & Robot-mounted LiDAR Mapping Systems (발행 2025-01)
- [ref-076](../../references/ref-076.md) — DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps (발행 2024-09)
- [ref-224](../../references/ref-224.md) — Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H., Tightly Coupled SLAM with Imprecise Architectural Plans (발행 2024-08)
- [ref-221](../../references/ref-221.md) — Vega Torres, M. A., Braun, A., & Borrmann, A., BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR (발행 2024-08)
- [ref-078](../../references/ref-078.md) — Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S., Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans (발행 2024-08)
- 그 밖에 10건

**기사·보고서**

- [ref-956](../../references/ref-956.md) — 지디넷코리아 (김성현), 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 (발행 2022-04-11)
- [ref-1013](../../references/ref-1013.md) — 엔지니어링데일리, "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개 (발행 2020-12-28)

**업체 발표**

- [ref-817](../../references/ref-817.md) — 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 (발행 2026-08-24)

**표준·오픈소스·기관 자료**

- [ref-071](../../references/ref-071.md) — Agour, M. 외 (ResPlan), ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) (발행 2025-08)
- [ref-158](../../references/ref-158.md) — ISO, ISO 19164:2024 - Geographic information — Indoor feature model (발행 2024)
- [ref-070](../../references/ref-070.md) — Hu, S. 외, Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) (발행 2024)
- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-1012](../../references/ref-1012.md) — AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주), 건축 도면 데이터 (발행 2023-07-26)
- [ref-069](../../references/ref-069.md) — Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT), MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) (발행 2023)
- [ref-1016](../../references/ref-1016.md) — Open Geospatial Consortium (OGC), Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 (발행 2021-02-18)
- [ref-066](../../references/ref-066.md) — FloorPlanCAD 프로젝트(Fan, Z. 외), FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) (발행 2021)
- [ref-064](../../references/ref-064.md) — Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W., DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) (발행 2019)
- [ref-065](../../references/ref-065.md) — Liu, C., Wu, J., Kohli, P., & Furukawa, Y., FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) (발행 2017)
- 그 밖에 21건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [16. 장소 의미·지도 관리](place-semantics-and-map-management.md) — 영역 심화: 3~11절 신규 작성(병원·가정·기타 적용 사례, 장소 목록·지도 버전·구역 집합·차선 폐쇄, 책임 경계, 연결 14개 영역, 열린 질문 9건), 13절 각주, 프런트매터 갱신. 2차 수정: 8절 첫 문장을 이번 브리프 자료 범위로 한정하고 ref-1017 각주 정의 추가 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area16-s6.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "6. 대표 접근법과 기술" 절(2,190자)을 옮겼다 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 열린 질문](../../topics/2026/2026-09-30-area16-s11.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "11. 열린 질문" 절(1,766자)을 옮겼다 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area16-s7.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,125자)을 옮겼다 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 대표 연구와 자료](../../topics/2026/2026-09-30-area16-s8.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 1절·3절 첫 문장을 이번 브리프 자료 범위로 한정 (실행 2026-09-30-04)
<!-- auto:category-recent:end -->
```

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md (요약)

```markdown
# 14. 도면·BIM에서 지도 만들기

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/space-and-map-model/place-semantics-and-map-management.md (요약)

```markdown
# 16. 장소 의미·지도 관리

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/objects-people-and-live-state/index.md

```markdown
---
title: "E. 사물·사람·실시간 상태"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › E. 사물·사람·실시간 상태

# E. 사물·사람·실시간 상태

## 핵심 질문

작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

## 개요

작업 대상과 자산의 식별·인계, 현장의 사람, 로봇·설비·공간의 현재 상태를 믿을 수 있게 관리하는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **17. 작업 대상·자산 식별과 인계 추적** | 물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 | 로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? | [17. 작업 대상·자산 식별과 인계 추적](work-object-and-asset-identification-and-handover-tracking.md) | published |
| **18. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 | 조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? | [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) | published |
| **19. 사람·보행자 모델** | 현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 | 현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? | [19. 사람·보행자 모델](people-and-pedestrian-model.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

**17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 58건이다(논문 17건 · 기사·보고서 1건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 40건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1128](../../references/ref-1128.md) — Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research (발행 2023-10-12)
- [ref-1179](../../references/ref-1179.md) — Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation (발행 2023-09-13)
- [ref-1079](../../references/ref-1079.md) — Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms (발행 2023-06-29)
- [ref-296](../../references/ref-296.md) — 김지형, OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 (발행 2023)
- [ref-1171](../../references/ref-1171.md) — Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots (발행 2023)
- [ref-1178](../../references/ref-1178.md) — Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation (발행 2022-07-04)
- [ref-294](../../references/ref-294.md) — 이동건, 송승현, 이찬혁, 노상도, 윤상문, 이현영(한국CDE학회 논문집), 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 (발행 2021-12)
- [ref-289](../../references/ref-289.md) — Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S., Age of Information: An Introduction and Survey (발행 2021-05)
- [ref-1172](../../references/ref-1172.md) — Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey (발행 2019-12-17)
- [ref-1175](../../references/ref-1175.md) — Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020), THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset (발행 2019-12-11)
- 그 밖에 7건

**기사·보고서**

- [ref-1181](../../references/ref-1181.md) — 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 (발행 2024-07-12)

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-032](../../references/ref-032.md) — VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released (발행 2026-04)
- [ref-011](../../references/ref-011.md) — ISO/IEC, ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) (발행 2024-03)
- [ref-012](../../references/ref-012.md) — ISO/IEC, ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) (발행 2024)
- [ref-1177](../../references/ref-1177.md) — 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 (발행 2023-12-27)
- [ref-1173](../../references/ref-1173.md) — ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (발행 2022-01-11)
- [ref-022](../../references/ref-022.md) — VDA(Verband der Automobilindustrie), VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control (발행 2022-01)
- [ref-045](../../references/ref-045.md) — GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) (발행 2021-09-30)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-1180](../../references/ref-1180.md) — ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD (발행 2021-06)
- [ref-017](../../references/ref-017.md) — GS1 Korea(대한상공회의소 유통물류진흥원), SSCC (Serial Shipping Container Code) GS1 Information Vol. 21 (발행 2019-09)
- 그 밖에 30건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [19. 사람·보행자 모델](people-and-pedestrian-model.md) — 영역 심화: 섹션 3~11 신규 작성(현장 유형 사례 4건: 물류창고·병원·상업 시설·기타), 13절 각주, 1차 조건부 승인 수정 16건 이행, 2차 수정: 5절 기타 사례 제약 칸을 비교 지표로 바로잡음·완료·인계 칸 두 곳 미확인·병원 서술의 검증 상태 문장 태그 제거, 7절 요약 문장을 사실·추정으로 분리 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md) — 자동 분리: 19. 사람·보행자 모델 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 장기 시공간 흐름 지도 첫 문장을 ref-1171 확인 범위(전형적 움직임 패턴 지도)로 고침 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md) — 자동 분리: 19. 사람·보행자 모델 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area19-s7.md) — 자동 분리: 19. 사람·보행자 모델 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 요약·첫 문장을 REP-155 사실 문장과 종합 판단 추정 문장으로 나눔 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area19-s8.md) — 자동 분리: 19. 사람·보행자 모델 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Helbing·Molnár 항목에서 '보행자 시뮬레이션에 널리 쓰이는' 삭제 (실행 2026-09-30-20)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-28
```

### docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md (요약)

```markdown
# 17. 작업 대상·자산 식별과 인계 추적

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 4

## 1. 한 줄 정의

물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 대상 식별·추적**: 물품·자산·도구·운반구·검체·세탁물처럼 작업 대상의 식별자·위치·적재 관계를 추적한다
- **인계·책임 기록**: 누가 언제 무엇을 넘겨받았는지 관측 근거와 함께 기록한다
- **이벤트 공통 형식**: 상태·위치·이동·인계 이벤트를 공통 형식으로 주고받는다(GS1 EPCIS 등)
- **수령인 확인**: 물건을 사람에게 넘길 때 받는 사람을 PIN·카드·앱으로 확인하고 인계 기록을 남긴다

이전 분류(2026-09-24)에서 이 페이지는 옛 7번 영역 ‘화물·재고·자산 식별과 추적’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [옛 분류원문]

> 옛 질문: 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [옛 분류원문]

> 옛 원문 주석: **7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [옛 분류원문]

이전 분류 기준: 원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

## 2. 핵심 질문

로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]

> 원문 주석: **17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (요약)

```markdown
# 19. 사람·보행자 모델

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
```

### docs/categories/integration/index.md

````markdown
---
title: "F. 연동"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-004, ref-009, ref-023, ref-031, ref-049, ref-051, ref-060, ref-079, ref-103, ref-105, ref-111, ref-125, ref-129, ref-130, ref-148, ref-153, ref-159, ref-228, ref-251, ref-253, ref-282, ref-283, ref-284, ref-285, ref-286, ref-287, ref-300, ref-310, ref-312, ref-314, ref-315, ref-316, ref-317, ref-364, ref-365, ref-367, ref-374, ref-405, ref-406, ref-407, ref-408, ref-409]
---

[홈](../../index.md) › F. 연동

# F. 연동

## 핵심 질문

제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

## 개요

제조사 관제·로봇, 문·승강기 같은 설비, 업무 시스템과 실제로 연결하고 표준으로 호환성을 확보하는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **20. 로봇·제조사 관제 연동** | 제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 | 로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? | [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) | published |
| **21. 상호운용 표준·적합성** | 로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 | 어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? | [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) | published |
| **22. 설비·건물 시스템 연동** | 문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 | 문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? | [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) | published |
| **23. 업무 시스템 연동** | 업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 | 업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? | [23. 업무 시스템 연동](business-system-integration.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4] [분류원문]

업무 시스템과 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 업무 시스템·관제·ROP의 책임은 겹칠 수 있다. [2] [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 C. 연결·실행 기반 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


C. 연결·실행 기반은 다른 대분류가 정한 업무·모델·계획을 로봇과 설비가 실제로 받는 명령과 상태로 옮기는 자리이므로, 다른 대분류와의 연결은 대부분 "무엇을 넘겨받고 무엇을 되돌려 주는가"의 문제로 나타난다. [의견] 이 절의 연결은 게시된 [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) 페이지와 A. 업무·공급망 설계·B. 공통 정보·환경 모델 대분류 페이지의 검증된 주장을 다시 쓴 것이 많다. D. 계획·최적화부터 G. 안전·보안·지능·거버넌스까지의 세부영역은 대부분 아직 본문이 없어서, 상대편 쪽 서술도 C. 연결·실행 기반 쪽 근거에 기댄다.

```mermaid
flowchart LR
  C["C. 연결·실행 기반"]
  A["A. 업무·공급망 설계"]
  B["B. 공통 정보·환경 모델"]
  D["D. 계획·최적화"]
  E["E. 협업·현장 운영"]
  F["F. 도입·검증·유지관리"]
  G["G. 안전·보안·지능·거버넌스"]
  AI["47. AI·학습·적응과 모델 운영"]
  A -->|"작업 요청·변경·취소"| C
  B -->|"능력·좌표·적재물·상태"| C
  C -->|"교통 스케줄·충전·구역 점유"| D
  C -->|"오류·인계 결과·작업 기록"| E
  F -->|"설정·시뮬레이션·적합성 시험·수명주기"| C
  G -->|"안전·보안·표준 제약"| C
  AI -.->|"근거 없음"| C
```

### A. 업무·공급망 설계

[A. 업무·공급망 설계](../planning-and-business/index.md) 쪽에서 본 같은 연결은 그 페이지의 [다른 대분류와의 연결](../planning-and-business/index.md#다른-대분류와의-연결) 절에 같은 태그와 각주로 실려 있다.

- **20. 로봇·제조사 관제 연동 ↔ [23. 업무 시스템 연동](business-system-integration.md)**: VDA 5050 3.0.0 은 외부 IT 시스템과의 인터페이스를 범위에서 제외한다. 그래서 상위 주문을 Open-RMF 작업 요청 같은 로봇 작업 요청으로 번역하는 계층이 두 대분류가 일을 넘겨받는 지점이 될 것으로 보인다. [추정][^ref-031][^ref-125]
- **29. 명령·작업 실행의 신뢰성 ↔ 23. 업무 시스템 연동·[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md)**: 상위 쪽은 B2MML 거래 동사(CHANGE·CANCEL 등)와 OPC UA for ISA-95 Job Control 메서드(Update·Pause·Resume·Abort·Cancel 등)로 변경·취소를 표현한다. 로봇 쪽 Open-RMF 작업 상태는 queued·underway·completed·canceled·killed·failed 같은 상태 값과 취소·강제 종료 요청 기록을 담는다. [사실][^ref-129][^ref-130][^ref-111] 세 자료는 서로 다른 계층의 사례이며 같은 내용을 교차 확인한 것은 아니다.
- **29. 명령·작업 실행의 신뢰성 ↔ 23. 업무 시스템 연동**: Open-RMF 작업 요청·파견 요청 스키마에는 요청자가 정하는 요청 식별자 필드가 없다. 따라서 상위 요청 id 와 작업 id 의 대응을 ROP 쪽에서 보존해 중복을 걸러야 할 것으로 보인다. [추정][^ref-365][^ref-125][^ref-367] 그 대응을 얼마 동안 보존할지는 [열린 질문](../../open-questions.md) oq-046 으로 남아 있다.
- **22. 설비·건물 시스템 연동 ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)**: 병원 약품 배송 로봇 사례에서 승강기 가동률이 높을수록 배송 실패가 많고 시간이 길었으며, 다층 호텔 배송 연구는 승강기를 경로 계획의 대기·운행 시간으로 모델링했다. [사실][^ref-060][^ref-103] 두 사례는 병원·호텔이며 물류센터 적용은 미확인이다(oq-010). 승강기 제어 자체는 분류 원문 19장 '시설·설비 제어' 경계의 연계 대상이며, 35. 처리능력·규모·배치 설계은 이를 제약 입력으로만 받는다. [의견]
- **22. 설비·건물 시스템 연동·42. 분산 시스템·통신·컴퓨팅 구조 ↔ 35. 처리능력·규모·배치 설계**: 국내에서 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 인증 모델은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야의 28개 항목(총점 176점)으로 구성된다(2023년 발행). [사실][^ref-409] 이 모델의 대상은 공동주택(아파트 단지)이며 물류센터가 아니다. 건물 설비와 통신 기반을 로봇 운영 조건으로 평가하는 이런 틀이 거점·설비 계획과 설비·통신 연동을 잇는 근거가 될 수 있다. [추정][^ref-409]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 23. 업무 시스템 연동**: 외부망이 끊긴 동안 현장 관제는 이미 받은 주문을 이어 갈 수 있으나 클라우드 WMS 의 새 주문 수신과 재고 확정은 멈추고, CAP 제약에 따라 재연결 뒤 현장 완료 기록과 WMS 기록을 맞추는 절차가 필요할 것으로 보인다. [추정][^ref-031][^ref-300][^ref-310] 물류센터 운영 기준은 미확인이다(oq-038).

### B. 공통 정보·환경 모델

[B. 공통 정보·환경 모델](../robot-ontology/index.md) 페이지의 [다른 대분류와의 연결](../robot-ontology/index.md#다른-대분류와의-연결) 절에 같은 연결이 같은 각주로 있다.

- **20. 로봇·제조사 관제 연동 ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: VDA 5050 팩트시트는 적재 명세(loadSets)와 지원 동작(mobileRobotActions)을, Open-RMF [플릿 어댑터](../../glossary/fleet-adapter.md) 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다. [사실][^ref-228][^ref-105]
- **20. 로봇·제조사 관제 연동 ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)**: 플릿 어댑터는 로봇 좌표계가 RMF 와 다르면 같은 위치를 가리키는 좌표 쌍으로 회전·축척·이동 변환을 추정하고, 템플릿 설정은 층별 reference_coordinates 로 이 좌표 쌍을 둔다. [사실][^ref-153][^ref-105] 이 작업이 용어집의 [지도 정합](../../glossary/map-alignment.md)이다.
- **22. 설비·건물 시스템 연동 ↔ 15. 지도·공간·위치 모델**: Open-RMF 승강기 상태는 층을 층 이름 문자열(available_floors, current_floor, destination_floor)로 나타내므로, 지도의 층 이름과 승강기 층 이름을 맞추는 대응이 필요할 것으로 보인다. [추정][^ref-286][^ref-079] 대응 규칙을 정한 표준은 미확인이다(oq-045).
- **20. 로봇·제조사 관제 연동 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)**: VDA 5050 상태 스키마의 적재물 목록(loads)은 적재 상태를 판단할 수 없는 로봇이 생략할 수 있고, 적재물 식별 번호(loadId)는 바코드·RFID 같은 식별 값이며 아직 식별하지 않았으면 비워 둔다. [사실][^ref-051]
- **22. 설비·건물 시스템 연동 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: Open-RMF 문·승강기 상태 메시지는 시각 필드(door_time, lift_time)를 담고, [승강기 어댑터](../../glossary/lift-adapter.md)는 적절하다고 판단한 요청만 승강기에 전달한다. [사실][^ref-285][^ref-286][^ref-284] 상태를 몇 초까지 믿을지 정한 규칙은 미확인이다(oq-034).
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 18. 실시간 세계 상태·데이터 일관성**: ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지처럼 통신 계층에 상태의 오래됨을 알리는 장치가 있다. [사실][^ref-282][^ref-287][^ref-031] 이 연결은 현재 상태를 표현하는 쪽이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 아래 F. 도입·검증·유지관리 항목에서 따로 다룬다.

### D. 계획·최적화

- **20. 로봇·제조사 관제 연동 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: [D. 계획·최적화](../planning-and-optimization/index.md)의 교통 관리와 관련해, Open-RMF 플릿 어댑터는 로봇의 예상 이동 경로를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 하며, 제조사 관제가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 붙는다. [사실][^ref-004][^ref-251] 제어 수준별 교통 성능 차이는 미확인이다(oq-032).
- **20. 로봇·제조사 관제 연동 ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)**: 플릿 어댑터 템플릿 설정은 배터리가 recharge_threshold 아래로 내려간 로봇에게 작업을 맡기지 않게 하고, 충전 목표·로봇별 충전기·작업 종료 후 동작(park·charge·nothing)을 둔다. [사실][^ref-105]
- **22. 설비·건물 시스템 연동 ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)**: Open-RMF 승강기 요청은 세션 단위로 승강기를 점유하고 AGV 모드에서는 정지 시 문이 열려 있으며, VDA 5050 3.0.0 은 [해제 구역](../../glossary/release-zone.md) 진입 요청에 관제가 허가·대기·철회·거절로 답하게 한다. [사실][^ref-312][^ref-031] 이런 점유·허가 정보가 승강기와 구역을 공용 자원으로 예약·배분하는 입력이 될 것으로 보인다. [추정][^ref-312][^ref-031]
- **29. 명령·작업 실행의 신뢰성 ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)**: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. [추정][^ref-031]

### E. 협업·현장 운영

- **22. 설비·건물 시스템 연동 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)**: [E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)의 물리적 인계와 관련해, Open-RMF 배송 작업에서 로봇은 하역 지점 워크셀([디스펜서·인제스터](../../glossary/dispenser-ingestor.md))에 IngestorRequest 를 보내고 IngestorResult 를 받을 때까지 반복하며, IngestorResult 는 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-023][^ref-049] 인수 결과를 화물 식별·인계 기록과 잇는 방법은 열린 질문으로 남아 있다(oq-001, oq-042).
- **20. 로봇·제조사 관제 연동 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: VDA 5050 의 주문 거절 오류(NO_ROUTE_TO_TARGET 등)·연결 단절(CONNECTION_BROKEN)과 Open-RMF 로봇 상태 error 를 공통 예외로 옮긴 뒤 재배정이나 사람 확인으로 넘기는 것이 두 대분류의 인계 지점이 될 것으로 보인다. [추정][^ref-031][^ref-148] 공통 상태·오류 어휘 매핑은 미확인이다(oq-033).
- **29. 명령·작업 실행의 신뢰성 ↔ 32. 예외 복구·재계획·업무 연속성**: Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하고, 작업 로그·백업을 SQLite 에 저장해 복구하는 기능이 별도 풀 리퀘스트로 제안되었다고 적는다. [사실][^ref-374] 현재 배포판 반영 여부는 미확인이다(oq-048).
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 32. 예외 복구·재계획·업무 연속성**: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 명세 표현으로 "fulfills the order up to the last released node", 곧 마지막으로 해제된 노드까지 주문을 수행한다. [사실][^ref-031]
- **29. 명령·작업 실행의 신뢰성 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: Open-RMF 작업 상태 기록(취소·강제 종료·중단 요청, 시작·종료 시각)이 이상 탐지와 원인 분석의 입력이 될 것으로 보인다. [추정][^ref-111]

### F. 도입·검증·유지관리

- **20. 로봇·제조사 관제 연동 ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)**: [F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)의 온보딩과 관련해, 새 플릿을 붙일 때 플릿 어댑터 설정에 층별 기준 좌표 쌍·충전기·지원 작업·동작을 채우는 일이 로봇 등록·지도 설정의 반복 작업이 될 것으로 보인다. [추정][^ref-105][^ref-153] 온보딩 소요를 측정한 자료는 확인하지 못했다.
- **22. 설비·건물 시스템 연동 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: Open-RMF 문서는 traffic-editor 로 주석한 지도에서 문·승강기·워크셀(TeleportDispenser·TeleportIngestor)을 포함한 시뮬레이션 세계를 생성하고, 여러 플릿의 승강기 요청을 조율하는 lift_supervisor 까지 재현하는 흐름을 제시한다. [사실][^ref-406] 이는 가정한 운영 상황을 가상으로 실험하는 쪽이며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 문·승강기 상태 메시지와는 구분한다.
- **22. 설비·건물 시스템 연동 ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: 같은 문서는 이렇게 만든 시뮬레이션으로 배치 전에 설비 연동을 시험해 시간과 자원을 아낄 수 있다고 설명한다. [사실][^ref-406]
- **20. 로봇·제조사 관제 연동·29. 명령·작업 실행의 신뢰성 ↔ 54. 시험·형식 검증·벤치마크**: 공개 오픈소스 가운데 VDA 5050 3.0.0 로봇 플릿 시뮬레이터(vda5050-sim)는 주문 수명주기·사전 정의 동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을 둔다고, MQTT 기록 진단 도구(vda5050-lab)는 반복된 주문·갱신 id, 기반·호라이즌 연결, 재연결 뒤 연결 상태, 취소·동작 수명주기 불일치를 진단한다고 각각 README 에 적는다. [사실][^ref-407][^ref-408] 두 도구는 개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아니다.
- **29. 명령·작업 실행의 신뢰성 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)**: ROS 2 [관리형 노드](../../glossary/managed-node.md)는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate·deactivate·cleanup·shutdown 같은 전이를 두어, 감독 도구가 모든 구성요소가 올바르게 준비됐는지 확인한 뒤 실행을 허용하게 한다. [사실][^ref-364]

### G. 안전·보안·지능·거버넌스

- **22. 설비·건물 시스템 연동 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: [G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)의 안전 관리와 관련해, 국가기술표준원은 2021년 11월 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한 KS B 7317 을 제정했고, Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있다. [사실][^ref-314][^ref-315][^ref-286] ROP 는 운영 모드 확인과 작업·경로 제약 반영만 맡고, 승강기 탑승 안전과 설비 안전 제어 자체는 분류 원문 19장 '시설·설비 제어' 경계의 연계 대상이다. [의견]
- **42. 분산 시스템·통신·컴퓨팅 구조·20. 로봇·제조사 관제 연동 ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: ROS 2 는 [DDS 보안 규격](../../glossary/dds-security.md)의 인증(PKI)·접근통제(거버넌스·권한 파일)·암호화 플러그인을 쓴다. Open-RMF 문서는 같은 신원과 접근통제 규칙을 공유하는 프로세스 묶음인 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고, 웹 대시보드에는 TLS·OIDC 인증을 더한다고 설명한다. [사실][^ref-009][^ref-405]
- **22. 설비·건물 시스템 연동 ↔ 51. 인증·권한·격리**: 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서는 어느 관제 구성요소가 어떤 설비 명령을 낼 수 있는지를 인클레이브·권한 파일 같은 접근통제 단위로 정해야 할 것으로 보인다. [추정][^ref-405][^ref-283][^ref-284] 출입통제 시스템 연동 사례는 미확인이다(oq-043).
- **20. 로봇·제조사 관제 연동 ↔ [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md)**: 제조사 중립 연동의 기준으로 VDA 5050(관제–이동로봇 통신), MassRobotics AMR 상호운용 표준(상태 보고), 그리고 개발 중인 국제표준 ISO 21423(산업용 이동로봇의 통신·상호운용성, 검색 결과상 FDIS 단계, 발행 여부 미확인)이 있다. [사실][^ref-031][^ref-253][^ref-159]
- **20. 로봇·제조사 관제 연동 ↔ 21. 상호운용 표준·적합성**: 이번에 확인한 VDA 5050 적합성 시험 도구가 제3자 오픈소스뿐이라, 어느 시험 결과를 연동 승인 기준으로 삼고 누가 연동 오류를 판정할지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-407][^ref-408][^ref-031] VDA 공식 적합성 인증 절차가 없다는 것은 확정된 사실이 아니다.
- **22. 설비·건물 시스템 연동 ↔ 21. 상호운용 표준·적합성**: 국내에서는 대한승강기협회가 엘리베이터와 로봇의 연동을 위한 단체표준을 제정했다고 전해진다(기사 보도 기준, 단체표준 원문·발행일 미확인). [추정][^ref-316][^ref-317] 표준이 정하는 메시지 내용은 oq-041 로 남아 있다.

### 아직 다루지 않은 연결

- **[47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)**: 이번 조사에서 C. 연결·실행 기반의 네 세부영역과 47. AI·학습·적응과 모델 운영을 잇는 검증된 근거를 찾지 못했다. 위의 29. 명령·작업 실행의 신뢰성 ↔ 38. 모니터링·이상 탐지·원인 분석 연결도 AI 기반 장애 분석이 아니라 작업 기록을 입력으로 쓰는 일반 연결로만 적었다.
- **[31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**, **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)**: 이번 실행에서는 C. 연결·실행 기반과 잇는 근거를 조사하지 않았다.
- 새로 올린 열린 질문: VDA 5050 공식 적합성 시험·인증 절차의 유무와 제3자 시험 결과의 승인 기준 활용, 그리고 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 나누는 공개 구성 사례. 두 질문은 [열린 질문](../../open-questions.md) 목록에 등록된다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 91건이다(논문 12건 · 기사·보고서 10건 · 업체 발표 3건 · 표준·오픈소스·기관 자료 66건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-260](../../references/ref-260.md) — ScienceDirect 게재 논문(저자 미확인), Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory (발행 2026)
- [ref-163](../../references/ref-163.md) — 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (발행 2026)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-321](../../references/ref-321.md) — Electronics(MDPI) 게재 논문(저자 미확인), Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots (발행 2025)
- [ref-136](../../references/ref-136.md) — Applied Sciences(MDPI) 게재 논문 저자(미확인), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector (발행 2025)
- [ref-133](../../references/ref-133.md) — Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? (발행 2025)
- [ref-132](../../references/ref-132.md) — Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations (발행 2025)
- [ref-409](../../references/ref-409.md) — 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) (발행 2023)
- [ref-259](../../references/ref-259.md) — Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept (발행 2023)
- [ref-134](../../references/ref-134.md) — Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter (발행 2010)
- 그 밖에 2건

**기사·보고서**

- [ref-264](../../references/ref-264.md) — 머니투데이, "로봇 통합 관제 기술, 인정받았다"..노바테크, 70억원 투자 유치 (발행 2026-07-14)
- [ref-263](../../references/ref-263.md) — 디지털투데이, 카카오모빌리티, 로봇 플랫폼 사업 본격화..."이기종 로봇 통합 운영" (발행 2026-05)
- [ref-137](../../references/ref-137.md) — 머니투데이, 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" (발행 2025-01)
- [ref-002](../../references/ref-002.md) — ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems (발행 2025)
- [ref-320](../../references/ref-320.md) — 파이낸셜뉴스, 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" (발행 2023-02)
- [ref-319](../../references/ref-319.md) — 한국경제, 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 (발행 2022-03)
- [ref-317](../../references/ref-317.md) — 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 (발행 미확인)
- [ref-316](../../references/ref-316.md) — 건설기술신문, 승강기협, 엘리베이터-로봇 연동 단체표준 제정 (발행 미확인)
- [ref-261](../../references/ref-261.md) — 헬로티(HelloT), 미르, 다기종 모바일 로봇 연동 SW 어댑터 ‘MiR VDA 5050’ 론칭 (발행 미확인)
- [ref-257](../../references/ref-257.md) — Interact Analysis, AMR Multi-Fleet Orchestration Software Explained (발행 미확인)

**업체 발표**

- [ref-608](../../references/ref-608.md) — OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments (발행 2026-04)
- [ref-318](../../references/ref-318.md) — KONE, KONE Service Robot API (발행 미확인)
- [ref-262](../../references/ref-262.md) — 클로봇(Clobot), 통합 로봇 관제 플랫폼 크롬스[CROMS] (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-032](../../references/ref-032.md) — VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released (발행 2026-04)
- [ref-710](../../references/ref-710.md) — 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 (발행 2025-06-04)
- [ref-560](../../references/ref-560.md) — ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells (발행 2025-02)
- [ref-135](../../references/ref-135.md) — ASCM, SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) (발행 2025)
- [ref-704](../../references/ref-704.md) — Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF' (발행 2024-03)
- [ref-130](../../references/ref-130.md) — OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) (발행 2024-01-31)
- [ref-636](../../references/ref-636.md) — European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) (발행 2023-12-13)
- [ref-129](../../references/ref-129.md) — MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd (발행 2023)
- [ref-637](../../references/ref-637.md) — 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호) (발행 2022-01-04)
- [ref-709](../../references/ref-709.md) — 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 (발행 2021-11-11)
- 그 밖에 56건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [4]는 참고문헌 [ref-004](../../references/ref-004.md)에 해당한다.[^ref-004] 원문의 [2]는 참고문헌 [ref-002](../../references/ref-002.md)에 해당한다.[^ref-002]

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-28

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-25
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25 (원문 미열람)
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25 (원문 미열람)
[^ref-253]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — README, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25 (원문 미열람)
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25 (원문 미열람)
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25 (원문 미열람)
[^ref-285]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-09-25 (원문 미열람)
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-09-25 (원문 미열람)
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-314]: 국가표준인증통합정보시스템(KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2021-11, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-09-25 (원문 미열람)
[^ref-315]: 산업통상자원부 국가기술표준원(대한민국 정책브리핑), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-316]: 건설기술신문, 승강기협, 엘리베이터-로봇 연동 단체표준 제정, 미확인, https://www.ctman.kr/35296, 접근일 2026-09-25 (원문 미열람)
[^ref-317]: 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 미확인, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: ROS 2 Design, Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-365]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-367]: IETF HTTPAPI Working Group (Jena, J., & Dalal, S.), The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header), 미확인, https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md, 접근일 2026-09-25 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2 GitHub), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-09-25 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25
[^ref-409]: 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105), 2023, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/index.md

````markdown
---
title: "G. 계획·최적화"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-005, ref-006, ref-004, ref-031, ref-051, ref-079, ref-090, ref-104, ref-105, ref-109, ref-117, ref-125, ref-132, ref-133, ref-134, ref-146, ref-168, ref-186, ref-188, ref-199, ref-228, ref-236, ref-237, ref-267, ref-286, ref-312, ref-376, ref-381, ref-385, ref-388, ref-398, ref-399, ref-401, ref-402, ref-403, ref-405, ref-531, ref-533, ref-493, ref-494]
---

[홈](../../index.md) › G. 계획·최적화

# G. 계획·최적화

## 핵심 질문

누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

## 개요

작업을 모델링·분해하고, 로봇에 배정하고, 순서·경로·공용 자원·충전을 최적화하는 결정 알고리즘. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **24. 작업·워크플로 모델링** | 현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 | 현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? | [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) | published |
| **25. 작업 배정 — MRTA** | 작업을 로봇 또는 로봇 팀에 배정한다 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? | [25. 작업 배정 — MRTA](task-allocation-mrta.md) | published |
| **26. 작업 순서·스케줄링** | 순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 | 일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? | [26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) | published |
| **27. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로·통과 시점·우선권을 조율한다 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? | [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) | published |
| **28. 공용 자원·충전·에너지 최적화** | 공용 자원을 예약·배분하고 충전·에너지를 계획한다 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? | [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

로봇 운영에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 요청이 계속 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6] [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 D. 계획·최적화 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


D. 계획·최적화의 네 세부영역은 다른 대분류에서 주문·능력·지도·상태를 입력으로 받고, 결정한 배정·순서·경로·충전 계획을 실행 기반에 넘긴다. 아래 연결은 게시된 세부영역 페이지의 검증된 주장과, 이번 실행에서 공식 저장소 원문을 다시 연 자료(확인일 2026-09-25)에 기댄다. 연결 대부분은 단일 출처에 기대고 교차 확인되지 않았다. E. 협업·현장 운영, F. 도입·검증·유지관리, G. 안전·보안·지능·거버넌스의 세부영역 다수가 아직 심화되지 않아 그쪽 연결은 D. 계획·최적화 쪽 근거에 기댄다.

```mermaid
flowchart LR
  A[A. 업무·공급망 설계] -->|주문·시작 시각·우선순위| D[D. 계획·최적화]
  B[B. 공통 정보·환경 모델] -->|능력·경로망·배터리 상태| D
  D -->|배정·순서·경로·충전 결정| C[C. 연결·실행 기반]
  C -->|입찰·제어 수준·세션 제약| D
  D ---|사람 협업·인계·모니터링·예외 복구| E[E. 협업·현장 운영]
  F[F. 도입·검증·유지관리] -->|시뮬레이션·벤치마크·현장 설정| D
  G[G. 안전·보안·지능·거버넌스] -->|안전·보안·AI·표준 제약| D
```

### [옛 A. 업무·공급망 설계](../planning-and-business/index.md)

- **[25. 작업 배정 — MRTA](task-allocation-mrta.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: VDA 5050 명세(3.0.0 판)는 이동로봇에 대한 주문 배정을 관제(fleet control)의 기능으로 두면서, 주변 설비·인프라·외부 IT 시스템과의 인터페이스는 명세 범위에서 뺀다. [사실][^ref-031] 로봇 인터페이스 표준이 상위 시스템 연동을 범위 밖에 두고 Open-RMF 작업 요청에도 마감 필드가 없으므로, 배정의 입력인 주문·납기·출하 마감 제약은 창고 관리 시스템(Warehouse Management System, WMS) 같은 상위 업무 시스템에서 받아 ROP가 배정 기준으로 옮겨야 할 것으로 보인다. [추정][^ref-031][^ref-125] 납기·출하 마감을 정하는 일 자체는 분류 원문 19장의 상위 업무 시스템 경계에 속하는 연계 대상이며, 결합 방법은 [열린 질문](../../open-questions.md) oq-054 로 남아 있다.
- **[26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) ↔ 23. 업무 시스템 연동**: Open-RMF 작업 요청 스키마는 시각·순서 관련 필드로 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후를 지정하는 필드는 두지 않는다(2026-09-25 확인). [사실][^ref-125] 웨이브·웨이브리스 출고 지시 정책 연구(2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. [추정][^ref-134][^ref-133]
- **26. 작업 순서·스케줄링 ↔ [24. 작업·워크플로 모델링](task-and-workflow-modeling.md)**: B2MML 공통 스키마의 Dependency1Type 은 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등)을 표현하며, 창고 물류 작업에 적용한 사례는 확인되지 않았다(oq-013). [사실][^ref-117]
- **26. 작업 순서·스케줄링 ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)**: 랙 이동 로봇 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는, 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. 이는 저자 계산 실험 조건의 보고값이며 독립 재현은 확인되지 않았다. [사실][^ref-381]
- **26. 작업 순서·스케줄링 ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)**: 풋월 주문 통합 연구(2019)는 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다고 보아, 포장 작업자 대기가 순서 결정의 성과 지표로 이어진다(지표 정의는 oq-051). [사실][^ref-385]
- **[28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) ↔ 35. 처리능력·규모·배치 설계**: 충전 정책 연구(2024)와 창고 충전소 배치 최적화 연구(2024)가 있어, 충전 정책 결정이 충전기 수·위치 같은 설비 계획으로 이어지는 것으로 보인다. [추정][^ref-533][^ref-109]
- **28. 공용 자원·충전·에너지 최적화 ↔ 39. 운영 성과 측정·개선**: Omega 게재 연구(2024)는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. 이 값은 모델·시뮬레이션 조건의 저자 보고값으로 현장 실측이 아니며 독립 재현은 확인되지 않았다. [사실][^ref-146]

### [옛 B. 공통 정보·환경 모델](../robot-ontology/index.md)

- **25. 작업 배정 — MRTA ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026-08). [사실][^ref-236][^ref-237]
- **28. 공용 자원·충전·에너지 최적화 ↔ 5. 로봇 능력·작업 표현**: VDA 5050 팩트시트는 임계 저충전 수준(criticalLowChargingLevel)과 최소·최대 희망 충전 수준·최소 충전 시간을 로봇 선언으로 두고, Open-RMF 플릿 어댑터 템플릿은 운영 설정 recharge_threshold(예시값 0.10)와 충전 목표 recharge_soc(예시값 1.0)를 둔다(2026-09-25 확인). [사실][^ref-228][^ref-105] 두 값 가운데 무엇을 충전 하한으로 삼을지는 oq-068 로 남아 있다.
- **[27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)**: Open-RMF traffic-editor 는 차선의 양방향 여부와 대기 지점·충전소·주차 지점 같은 경유점 속성, 문·승강기를 주석하게 하고, 이 그래프를 building_map_generator 로 주행 그래프로 내보내 플릿 어댑터의 경로 계획에 쓰게 한다. [사실][^ref-079]
- **28. 공용 자원·충전·에너지 최적화 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: Open-RMF 는 로봇이 작업을 끝낼 충전량이 부족하면 충전 작업을 일정에 끼워 넣으므로, 충전 시점 계획은 로봇이 보고하는 현재 배터리 상태를 입력으로 쓰며, 이 현재 상태 표현은 18. 실시간 세계 상태·데이터 일관성 쪽에 속하는 것으로 보인다. [추정][^ref-104][^ref-051] 이 연결은 현재 상태를 표현하는 쪽이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 연결(아래 F. 도입·검증·유지관리)과 구분한다.

### [옛 C. 연결·실행 기반](../integration/index.md)

- **25. 작업 배정 — MRTA ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: Open-RMF 디스패처는 작업 요청을 받으면 모든 플릿 어댑터에 입찰 공고(BidNotice)를 보내고, 처리 가능한 플릿이 비용을 담은 입찰(BidProposal)을 내면 가장 빨리 끝나는 것·가장 낮은 비용 같은 설정 기준으로 비교해 작업을 줄 플릿을 정한다. [사실][^ref-376] 작업 요청 스키마의 fleet_name 필드는 작업을 수행할 수 있는 플릿 이름(하나 또는 목록)을 지정해, 요청 단계에서 배정 후보 플릿을 제한할 수 있게 한다. [사실][^ref-125]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 는 플릿 연동을 전체 제어·신호등(일시정지·재개)·읽기 전용으로 나누고 공유 공간마다 읽기 전용 플릿을 최대 하나만 허용하며, 충돌이 나면 플릿들이 선호 경로와 상대를 수용하는 경로를 내고 시스템 통합사가 배치한 제3자 판정자가 조합을 고른다. [사실][^ref-004] VDA 5050 은 경로 결정·우선순위·혼잡 처리·교착 해소 같은 교통 조율 전략과 알고리즘을 명세에서 빼면서도, 막힘 탐지·해소와 교통 제어(버퍼 경로·대기 위치)를 관제 기능으로 둔다. [사실][^ref-031]
- **28. 공용 자원·충전·에너지 최적화 ↔ 20. 로봇·제조사 관제 연동**: VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다는 것을 관제의 에너지 관리 기능으로 두고, 과충전 보호는 이동로봇의 책임으로 명시한다. [사실][^ref-031] 과충전 보호는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이며, ROP는 충전 시작·중지 요청과 상태 확인만 맡는다.
- **28. 공용 자원·충전·에너지 최적화 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: Open-RMF 승강기 요청은 요청자 사이에서 유일한 세션 id 로 승강기를 점유하고 세션 종료 요청을 보낼 때까지 제어권이 그 세션에 남으며, AGV 모드에서는 승강기가 정지해 있는 동안 문이 열린 채 유지된다. [사실][^ref-312][^ref-286] 승강기 운행과 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, ROP는 승강기 세션 요청과 운영 모드 확인만 맡는다.
- **26. 작업 순서·스케줄링 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. [추정][^ref-031]
- **25. 작업 배정 — MRTA ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)**: Lott·Honary(2026-09, 프리프린트, 원문 미열람)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 등 통신 저하 조건에서 비교했다. [사실][^ref-493] 이 비교와 클라우드에 연결된 로봇·로봇그룹의 작업 계획을 다룬 국내 과제 보고서가 있어, 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 영역을 잇는 설계 쟁점이 될 것으로 보이나, 물류센터 적용 근거는 없다. [추정][^ref-493][^ref-401]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- **25. 작업 배정 — MRTA ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**: 작업자가 피킹하고 자율이동로봇이 운반하는 동적 주문 피킹 연구(2025)가 있어, 로봇 배정이 사람 작업자의 배치와 맞물린다. [사실][^ref-132]
- **26. 작업 순서·스케줄링 ↔ 31. 사람–로봇 협업**: 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구(2025)가 있다(결과 수치는 미확인). [사실][^ref-388]
- **26. 작업 순서·스케줄링 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)**: Open-RMF 배정이 플릿 단위 입찰로 이루어지고 작업 요청 스키마에 작업 간 선후 필드가 없으므로, 피킹 로봇 완료 뒤 운반 로봇 출발 같은 제조사 간 인계 선후는 ROP가 작업 흐름 수준에서 관리해야 할 것으로 보인다(oq-049). [추정][^ref-376][^ref-125]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: 창고 MAPF 실행 연구(2019)는 지연이 쌓일 때 행동 의존 그래프로 순서를 지키며 실행을 이어가는 방법을 다루어, 계획 유지와 재계획의 판단이 두 영역을 잇는다. [사실][^ref-188]
- **25. 작업 배정 — MRTA ↔ 32. 예외 복구·재계획·업무 연속성**: VDA 5050 에서 브로커 연결이 끊긴 로봇은 받은 주문 정보를 유지한 채 마지막으로 해제된 노드까지 주문을 수행하므로, 통신 단절 때 ROP가 다시 배정할 수 있는 몫은 아직 해제하지 않은 구간과 새 작업으로 한정될 것으로 보인다. [추정][^ref-031]
- **25. 작업 배정 — MRTA ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터는 위치 신뢰도와 작업 실행 행동 증거를 결합해 에이전트를 분류하므로, 실행 기록으로 이상 로봇을 가려 배정 입력에서 빼는 일이 모니터링과 배정을 잇는 지점이 될 것으로 보인다. 이 연구는 GPS 스푸핑 데이터와 택시 수요로 실험했으며 물류센터 적용은 확인되지 않았다. [추정][^ref-494]

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- **25. 작업 배정 — MRTA ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: 로봇 이동형 풀필먼트 시스템(2019)과 국내 자동물류센터의 이산 사건 시뮬레이션 연구가 배정 규칙을 가정한 미래에서 실험하는 도구로 쓰였고, 한 연구에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398][^ref-402]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 34. 시뮬레이션·예측용 디지털 트윈**: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(2024)가 있어, 경로망 설계 평가는 가정한 미래를 실험하는 쪽에 속하는 것으로 보인다. [추정][^ref-267]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)**: 현장 도입 때 플릿별 경로망과 차선 방향, 대기·충전·주차 경유점을 traffic-editor 로 주석해 설정하는 일이 온보딩 작업이 될 것으로 보인다. [추정][^ref-079]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: MAPF 연구는 정의·변형·벤치마크를 정리한 공통 틀(2019)을 가지고 있으나, 격자·단위 시간 가정의 벤치마크 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). [사실][^ref-186]
- **25. 작업 배정 — MRTA ↔ 54. 시험·형식 검증·벤치마크**: 분산 배정기를 같은 사례 묶음과 통신 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크(2026-09, 프리프린트)가 있어, 배정 방식 선택을 시험 조건과 함께 평가하는 틀이 된다. [사실][^ref-493]
- **28. 공용 자원·충전·에너지 최적화 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)**: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 일정을 정하는 연구(2026-03)가 있어, 충전·배정 계획이 배터리 열화 관리와 이어진다. [사실][^ref-403]

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- **28. 공용 자원·충전·에너지 최적화 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있고(설정은 사람·AGV 모드만 가능), Open-RMF 데모는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. [사실][^ref-286][^ref-104] 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, ROP는 운영 모드를 확인해 계획에 반영하는 쪽을 맡는다.
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 48. 안전·위험 관리**: VDA 5050 은 진입 금지·속도 제한·해제·우선·벌점 등 구역 유형을 교통 관리 수단으로 정의하면서, 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다. [사실][^ref-031] 따라서 이 연결은 교통 관리 수단과 안전 기능을 구분하는 지점으로만 다룬다.
- **25. 작업 배정 — MRTA ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 계획 정보와 실행을 어긋나게 하면 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선이 사라질 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안한다. 실험은 GPS 스푸핑 데이터와 택시 수요로 했으며 물류센터 적용은 확인되지 않았다. [사실][^ref-494] Open-RMF 문서는 같은 신원과 접근통제 규칙을 공유하는 프로세스 묶음인 SROS 2 인클레이브로 구성요소의 권한을 나누고, 웹 대시보드는 TLS 로 제공하며 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용한다고 설명한다. [사실][^ref-405] 작업 요청이 대시보드·API 서버를 거쳐 디스패처로 들어가고 배정이 플릿의 입찰 비용과 위치 보고에 기대므로, 누가 작업을 요청·우선 지정할 수 있는지와 입찰·위치 보고를 얼마나 믿을지가 배정의 보안 경계가 될 것으로 보인다. 창고 배정의 보안 사례는 찾지 못했다. [추정][^ref-405][^ref-376][^ref-494]
- **25. 작업 배정 — MRTA ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)**: 분류 개정 전 원문 8장의 교차 규칙은 학습 기반 배차를 25. 작업 배정 — MRTA에 적용되는 47. AI·학습·적응과 모델 운영의 연구 방법으로 둔다. 학습 기반 배차(이종 그래프 어텐션 스케줄러)와 대규모 언어 모델(Large Language Model, LLM) 기반 다중 로봇 작업 배정 연구가 있어 이 교차 규칙에 따라 두 영역이 이어진다. [사실][^ref-399][^ref-090][^ref-168] LLM 배정의 결과 수치는 출처가 충돌해(oq-030) 여기서 쓰지 않는다.
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 47. AI·학습·적응과 모델 운영**: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있어, 학습 기반 경로 계획이 두 영역을 잇는다. [사실][^ref-199]
- **28. 공용 자원·충전·에너지 최적화 ↔ 47. AI·학습·적응과 모델 운영**: 자율 피킹 로봇의 충전소 선택·충전 시간 결정에 심층 강화학습을 쓰는 연구(2026-07)가 있어, 학습 기반 충전 결정이 두 영역을 잇는 것으로 보인다. [추정][^ref-531]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: VDA 5050 은 구역·경로 해제로 교통 규칙을 정하되 조율 전략은 빼고, Open-RMF 는 여러 플릿의 교통 협상에서 시스템 통합사가 배치한 판정자가 조합을 고르게 하므로, 한 현장에서 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-057). [추정][^ref-031][^ref-004]

### 아직 다루지 않은 연결

- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)과 D. 계획·최적화를 잇는 근거는 이번 조사에서 확보하지 못했다.
- 42. 분산 시스템·통신·컴퓨팅 구조, 38. 모니터링·이상 탐지·원인 분석, 51. 인증·권한·격리와의 연결은 물류센터 조건이 아닌 2026년 프리프린트 두 편에 기대므로, 물류 현장 근거가 나오면 다시 확인한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 108건이다(논문 66건 · 기사·보고서 0건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 40건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-493](../../references/ref-493.md) — Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation (발행 2026-09)
- [ref-192](../../references/ref-192.md) — Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (발행 2026-09)
- [ref-236](../../references/ref-236.md) — Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation (발행 2026-08-11)
- [ref-494](../../references/ref-494.md) — Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems (발행 2026-08)
- [ref-531](../../references/ref-531.md) — arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers (발행 2026-07)
- [ref-403](../../references/ref-403.md) — Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots (발행 2026-03)
- [ref-116](../../references/ref-116.md) — Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis (발행 2026-03)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-168](../../references/ref-168.md) — Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms (발행 2025-12)
- [ref-268](../../references/ref-268.md) — Rüdt, M., Enke, C., & Furmans, K. (KIT), Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) (발행 2025-11)
- 그 밖에 56건

**기사·보고서**

- 아직 없음

**업체 발표**

- [ref-219](../../references/ref-219.md) — Mobile Industrial Robots(MiR) (ManualsLib 게재본), MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) (발행 미확인)
- [ref-113](../../references/ref-113.md) — Camunda, Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-117](../../references/ref-117.md) — MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd (발행 2023)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-119](../../references/ref-119.md) — IEC / ISO, IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management (발행 2016)
- [ref-538](../../references/ref-538.md) — Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub) (발행 미확인)
- [ref-537](../../references/ref-537.md) — Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp (발행 미확인)
- [ref-536](../../references/ref-536.md) — Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp (발행 미확인)
- [ref-405](../../references/ref-405.md) — Open Robotics, Security - Programming Multiple Robots with ROS 2 (발행 미확인)
- [ref-404](../../references/ref-404.md) — Open Robotics (open-rmf), rmf_task — README (발행 미확인)
- [ref-401](../../references/ref-401.md) — KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 (발행 미확인)
- [ref-390](../../references/ref-390.md) — Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp (발행 미확인)
- 그 밖에 30건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [G. 계획·최적화](index.md) — '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 아직 다루지 않은 연결에 7. 화물·재고·자산 식별과 추적 명시), '참고 자료' 끝에 새 각주 정의 38건 추가 (실행 2026-09-25-55)
- 2026-09-25 · 요약 · [G. 계획·최적화](index.md) — D. 계획·최적화: '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 1차 수정 지시 14건 이행) (실행 2026-09-25-55)
- 2026-09-25 · 갱신 · [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 섹션 3~11 신규 작성(트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행), 2차 수정: 4·8절 연결 문장 태그 제거, 5절 조사 한계 문장 태그·각주 제거와 oq-010 연결, 6절 첫 문장을 출처 범위로 좁힘 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장을 출처 범위(충전 작업 삽입·뮤텍스 그룹·승강기 세션)로 좁혔다 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 첫 문장 태그 제거, 병원·호텔 연구 문구를 연관 관계로 고침, ref-535 제목 원문 복원 (실행 2026-09-25-40)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [5]는 참고문헌 [ref-005](../../references/ref-005.md)에 해당한다.[^ref-005] 원문의 [6]은 참고문헌 [ref-006](../../references/ref-006.md)에 해당한다.[^ref-006]

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-24
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-188]: Hönig, W., Kiesel, S. 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-199]: arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-388]: Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지), 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링, 2025, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-399]: Wang, Z., & Gombolay, M., Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints, 미확인, https://link.springer.com/article/10.1007/s10514-021-09997-2, 접근일 2026-09-25 (원문 미열람)
[^ref-401]: KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952, 접근일 2026-09-25 (원문 미열람)
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-09-25 (원문 미열람)
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (요약)

```markdown
# 26. 작업 순서·스케줄링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 순서·스케줄링**: 작업 묶음, 선후관계, 시간 제약, 작업 간 동기화, 긴급 작업 삽입을 다룬다
- **계속 들어오는 작업의 재계획**: 새 작업과 지연이 계속 생기는 조건에서 계획을 이어서 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 14번 영역 ‘작업 순서·스케줄링’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 [옛 분류원문]

> 옛 질문: 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? [옛 분류원문]

## 2. 핵심 질문

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
```

### docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md (요약)

```markdown
# 28. 공용 자원·충전·에너지 최적화

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

공용 자원을 예약·배분하고 충전·에너지를 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **공용 자원 예약·배분**: 승강기·작업대·대기 공간·버퍼 같은 공용 자원을 예약하고 나눈다
- **충전·에너지 계획**: 충전 시점·충전기 배정·대기열과 작업별 에너지 예산을 계획한다

이전 분류(2026-09-24)에서 이 페이지는 옛 16번 영역 ‘공용 자원·충전·에너지 최적화’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [옛 분류원문]

> 옛 질문: 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [옛 분류원문]

## 2. 핵심 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
```

### docs/ideas/index.md

````markdown
---
title: "확장 아이디어 연결 구조"
type: idea
subtype: index
related_areas: [5, 15, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 38, 47, 48, 51, 54, 55, 57]
tags: [확장 아이디어, 공통 데이터 모델, 연구영역 매핑]
status: published
created: 2026-09-25
updated: 2026-09-25
version: 1
---

[홈](../index.md) › 확장 아이디어 연결 구조

# 확장 아이디어 연결 구조

이 페이지는 사용자가 제안한 세 확장 아이디어가 서로 어떻게 이어지는지, 무엇을 공통 데이터로 주고받는지, 67개 세부 연구영역과 어떻게 대응하는지를 한곳에 모은다. 아이디어는 분류를 바꾸지 않는다. 17개 대분류·67개 세부 연구영역의 이름·순서·번호·정의는 그대로이고, 아이디어는 세부영역에 연결을 더할 뿐이다. 각 아이디어의 연구는 중점 연구 트랙이 단계적으로 진행하며, 이 페이지의 구조와 데이터 모델은 구축자 제안이다. [가정]

## 세 아이디어

| 아이디어 | 정의(사용자 문구 그대로) | 연구하는 트랙 |
|---|---|---|
| [아이디어 1. 로봇 기능 온톨로지](robot-capability-ontology.md) | 로봇 매뉴얼·SDK 문서에서 로봇별 능력(이동·계단·적재·도어 조작·충전)과 제약을 추출해 온톨로지로 정리. 작업 할당 시 수행 가능한 로봇을 질의로 찾고, 신규 로봇 온보딩 시 능력 정의 초안을 자동 생성 | [매뉴얼 기반 로봇 기능 온톨로지](../tracks/manual-capability-ontology/index.md)(기존 트랙 확장) |
| [아이디어 2. 채팅 기반 구성·운영](chat-based-configuration-and-operation.md) | 사용자가 채팅으로 상황과 처리할 일을 입력하면 AI가 업무를 파악·분해하고, 온톨로지로 적합한 로봇을 찾아 배정·배치한 뒤 작업 진행과 스케줄링을 자동으로 관리 | [채팅 기반 구성·운영](../tracks/chat-based-configuration-and-operation/index.md)(새 트랙) |
| [아이디어 3. 건축 도면 자동 인식](floorplan-recognition.md) | 평면도에서 벽·문·엘리베이터·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록을 자동 생성하고, 공간 그래프로 온톨로지에 적재. 현장 모델링 시간을 줄이고 시뮬레이션 초기값으로 사용 | [건축 도면 자동 인식](../tracks/floorplan-recognition/index.md)(새 트랙) |

## 이어지는 구조

세 아이디어는 하나의 흐름으로 이어진다. 도면 인식(아이디어 3)이 평면도에서 공간과 시설(공간 노드, 공용 자원)을 뽑아 공간 그래프로 온톨로지에 적재하고, 로봇 기능 온톨로지(아이디어 1)가 로봇의 능력과 제약을 같은 온톨로지에 담는다. 챗봇(아이디어 2)은 사용자의 지시를 작업으로 분해한 뒤 그 온톨로지를 질의해 작업을 할 수 있는 로봇과 경로·자원을 고른다. [가정]

이 흐름은 분류 개정 전 원문 10장의 "로봇과 건물 조건을 함께 판단" 아이디어가 가리키는 지점과 겹친다. 원문은 그 중심 연구영역을 [5. 로봇 능력·작업 표현](../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)으로, 함께 필요한 영역을 [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [48. 안전·위험 관리](../categories/safety/safety-and-risk-management.md)로 둔다(원문 표는 [논의한 아이디어의 연구영역 매핑](../about/idea-mapping.md)에 있다).

```mermaid
flowchart LR
  plan["평면도"] --> idea3["아이디어 3. 건축 도면 자동 인식"]
  idea3 -->|"공간 노드·공용 자원"| sgraph["공간 그래프"]
  manual["로봇 매뉴얼·SDK 문서"] --> idea1["아이디어 1. 로봇 기능 온톨로지"]
  idea1 -->|"로봇 능력·제약"| onto["공통 온톨로지"]
  sgraph -->|"적재"| onto
  chat["사용자 채팅 지시"] --> idea2["아이디어 2. 채팅 기반 구성·운영"]
  idea2 -->|"작업 요구 질의"| onto
  onto -->|"수행 가능한 로봇·경로·공용 자원"| idea2
  idea2 -->|"배정·배치·일정"| rop["ROP 실행: 배정·경로·자원 예약"]
  idea3 -.->|"층별 지도(초기값)"| sim["시뮬레이션·예측용 디지털 트윈"]
  idea1 -.->|"능력 정의 초안"| onboard["신규 로봇 온보딩"]
```

## 공통 데이터 모델

세 아이디어가 함께 쓰는 네 요소다. 정의와 속성은 아이디어 정의 문구에서 구축자가 도출한 출발점이며, 각 트랙의 초안([능력 온톨로지 초안](../tracks/manual-capability-ontology/ontology-draft.md), [업무 분해·배정 설계 초안](../tracks/chat-based-configuration-and-operation/task-model-draft.md), [공간 그래프 스키마 초안](../tracks/floorplan-recognition/space-graph-schema-draft.md))이 근거와 함께 고친다. [가정]

| 요소 | 정의 | 주요 속성 | 생산하는 아이디어 | 소비하는 아이디어 |
|---|---|---|---|---|
| 공간 노드 | 로봇이 머물거나 지나가는 공간 단위(층·구역·통로)와 그 사이를 잇는 문·엘리베이터·계단 | 층, 종류, 연결된 노드, 통과 조건, 이름·별칭, 근거 도면 | 아이디어 3 | 아이디어 1(계단·도어 조작 능력과 통과 조건 대조), 아이디어 2(지시 속 장소 해석, 배치 경로) |
| 공용 자원 | 여러 로봇이 나눠 쓰는 시설(엘리베이터, 충전 위치 등) | 종류, 위치(공간 노드), 수용량, 예약·사용 조건, 설비 연동 여부 | 아이디어 3(공용 자원 목록) | 아이디어 1(충전·도어 조작 능력과 대응), 아이디어 2(배치·일정의 자원 예약) |
| 로봇 능력 | 로봇이 수행할 수 있는 기능과 그 제약(범위 능력: 이동·계단·적재·도어 조작·충전) | 기능, 제약, 장착 장비, 실행 조건, 근거 문서 | 아이디어 1 | 아이디어 2(작업 할당 질의), 아이디어 3(로봇별 통과 가능 경로 판단) |
| 작업 | 지시에서 분해된 실행 단위와 그 요구 | 작업 종류, 장소(공간 노드), 대상, 기한·우선순위, 작업 요구(필요 능력·제약), 배정 로봇, 진행 상태 | 아이디어 2 | 아이디어 1(작업 요구와 기능의 대응 질의) |

## 아이디어 사이의 입출력

| 보내는 아이디어 | 받는 아이디어 | 전달하는 것 | 받는 쪽의 쓰임 |
|---|---|---|---|
| 아이디어 3. 건축 도면 자동 인식 | 아이디어 1. 로봇 기능 온톨로지 | 공간 그래프(공간 노드·공용 자원) | 온톨로지에 적재해 로봇 능력(계단·도어 조작·충전)과 공간 조건을 같은 기준으로 대조 |
| 아이디어 3. 건축 도면 자동 인식 | 아이디어 2. 채팅 기반 구성·운영 | 층·구역 이름과 별칭, 경로, 공용 자원 목록 | 지시 속 장소 해석, 배치 경로와 자원 예약 |
| 아이디어 1. 로봇 기능 온톨로지 | 아이디어 2. 채팅 기반 구성·운영 | 작업 할당 질의 결과(수행 가능한 로봇 후보와 근거) | 배정 후보 선택과 배정 근거 설명 |
| 아이디어 2. 채팅 기반 구성·운영 | 아이디어 1. 로봇 기능 온톨로지 | 작업 요구(필요 능력·제약), 질의가 실패한 사례 | 질의 입력, 온톨로지 보강 질문 |
| 아이디어 2. 채팅 기반 구성·운영 | 아이디어 3. 건축 도면 자동 인식 | 해석하지 못한 장소 표현 | 공간 노드 이름·별칭 보강 |

표의 입출력은 구축자가 아이디어 정의에서 도출한 설계 가설이며, 각 트랙의 단계 3(구현 가설 설계)이 근거와 함께 확정하거나 고친다. [가정]

## 67개 세부 연구영역 매핑표

각 칸의 ●는 그 아이디어의 중심 영역, ○는 함께 필요한 영역, 빈칸은 직접 연결이 없음을 뜻한다. 원천은 각 트랙 정의(`config/tracks/*.yaml`)의 `idea_areas`이며, 퍼블리셔가 이 표와 세부영역 페이지 머리의 "관련 연구 트랙" 안내를 같은 원천에서 다시 만든다. 매핑 근거는 각 아이디어 페이지의 "2. 관련 세부 연구영역"과 결정 기록에 있다. 분류 개정 전 원문 10장이 정한 매핑(아이디어 1의 5·9·21·23·24, 아이디어 3의 6·15·21·22)과 8장의 교차 규칙(47. AI·학습·적응과 모델 운영의 문서·도면 해석)은 그대로 따랐고, 나머지는 구축자 제안이다. [가정]

<!-- auto:idea-area-map:start -->
| 대분류 | 세부 연구영역 | [아이디어 1. 로봇 기능 온톨로지](robot-capability-ontology.md) | [아이디어 2. 채팅 기반 구성·운영](chat-based-configuration-and-operation.md) | [아이디어 3. 건축 도면 자동 인식](floorplan-recognition.md) |
|---|---|---|---|---|
| [A. 기획·사업](../categories/planning-and-business/index.md) | [1. 기술·시장·업체 동향](../categories/planning-and-business/technology-market-and-vendor-trends.md) |  |  |  |
| [A. 기획·사업](../categories/planning-and-business/index.md) | [2. 사용 사례·요구·책임 범위](../categories/planning-and-business/use-cases-requirements-and-scope.md) |  |  |  |
| [A. 기획·사업](../categories/planning-and-business/index.md) | [3. 경제성·조달·사업 모델](../categories/planning-and-business/economics-procurement-and-business-models.md) |  |  |  |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [4. 이기종 로봇 등록](../categories/robot-ontology/heterogeneous-robot-registration.md) | ○ |  |  |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [5. 로봇 능력·작업 표현](../categories/robot-ontology/robot-capability-and-task-representation.md) | ● | ○ | ○ |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [6. 온톨로지 기반 시스템·로봇 연동](../categories/robot-ontology/ontology-based-system-and-robot-integration.md) | ○ |  |  |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [7. 온톨로지 검증·변경 관리](../categories/robot-ontology/ontology-verification-and-change-management.md) | ○ |  |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [8. 채팅으로 맵 작성](../categories/chat-based-configuration-and-operation/chat-map-authoring.md) |  | ● | ○ |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [9. 채팅으로 시나리오 구성](../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [10. 채팅으로 로봇 구성](../categories/chat-based-configuration-and-operation/chat-robot-configuration.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [11. 채팅으로 실제 상황 시뮬레이션 재현](../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) |  | ● |  |
| [D. 공간·지도 모델](../categories/space-and-map-model/index.md) | [14. 도면·BIM에서 지도 만들기](../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) |  |  | ● |
| [D. 공간·지도 모델](../categories/space-and-map-model/index.md) | [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md) |  | ○ | ○ |
| [D. 공간·지도 모델](../categories/space-and-map-model/index.md) | [16. 장소 의미·지도 관리](../categories/space-and-map-model/place-semantics-and-map-management.md) |  |  |  |
| [E. 사물·사람·실시간 상태](../categories/objects-people-and-live-state/index.md) | [17. 작업 대상·자산 식별과 인계 추적](../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) |  |  |  |
| [E. 사물·사람·실시간 상태](../categories/objects-people-and-live-state/index.md) | [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) | ○ | ○ | ○ |
| [E. 사물·사람·실시간 상태](../categories/objects-people-and-live-state/index.md) | [19. 사람·보행자 모델](../categories/objects-people-and-live-state/people-and-pedestrian-model.md) |  |  |  |
| [F. 연동](../categories/integration/index.md) | [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md) | ○ |  |  |
| [F. 연동](../categories/integration/index.md) | [21. 상호운용 표준·적합성](../categories/integration/interoperability-standards-and-conformance.md) | ○ |  | ○ |
| [F. 연동](../categories/integration/index.md) | [22. 설비·건물 시스템 연동](../categories/integration/facility-and-building-system-integration.md) | ○ |  | ○ |
| [F. 연동](../categories/integration/index.md) | [23. 업무 시스템 연동](../categories/integration/business-system-integration.md) |  | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [24. 작업·워크플로 모델링](../categories/planning-and-optimization/task-and-workflow-modeling.md) |  | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md) | ○ | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [26. 작업 순서·스케줄링](../categories/planning-and-optimization/task-sequencing-and-scheduling.md) |  | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [27. 다중 로봇 경로·교통 관리 — MAPF](../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) |  |  | ○ |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [28. 공용 자원·충전·에너지 최적화](../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) | ○ | ○ | ○ |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [29. 명령·작업 실행의 신뢰성](../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) | ○ | ○ |  |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [30. 로봇 간 협업·물리적 인계](../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md) |  |  |  |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [31. 사람–로봇 협업](../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) |  | ○ |  |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [32. 예외 복구·재계획·업무 연속성](../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) |  | ○ |  |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [33. 시나리오 모델·편집](../categories/design-and-simulation/scenario-model-and-editing.md) |  |  |  |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [34. 시뮬레이션·예측용 디지털 트윈](../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) |  |  | ○ |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [35. 처리능력·규모·배치 설계](../categories/design-and-simulation/capacity-sizing-and-layout-design.md) |  |  | ○ |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [36. 가상 시운전·실제 상황 재현](../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) |  |  |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [37. 관제 화면·실행 기록](../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) |  |  |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [38. 모니터링·이상 탐지·원인 분석](../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) |  | ○ |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [39. 운영 성과 측정·개선](../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) |  |  |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [40. 운영 절차·요청 창구](../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) |  |  |  |
| [K. 플랫폼 아키텍처·인프라](../categories/platform-architecture-and-infrastructure/index.md) | [41. 플랫폼 아키텍처·외부 API](../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) |  |  |  |
| [K. 플랫폼 아키텍처·인프라](../categories/platform-architecture-and-infrastructure/index.md) | [42. 분산 시스템·통신·컴퓨팅 구조](../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) |  |  |  |
| [K. 플랫폼 아키텍처·인프라](../categories/platform-architecture-and-infrastructure/index.md) | [43. 데이터·관측성·배포](../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [44. 로봇 기반 모델·언어 모델 계획](../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [45. 문서·도면·장면 이해](../categories/ai-and-learning/document-drawing-and-scene-understanding.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [46. 예측·학습 기반 최적화](../categories/ai-and-learning/prediction-and-learning-based-optimization.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [47. AI·학습·적응과 모델 운영](../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) | ○ | ○ | ○ |
| [M. 안전](../categories/safety/index.md) | [48. 안전·위험 관리](../categories/safety/safety-and-risk-management.md) | ○ | ○ |  |
| [M. 안전](../categories/safety/index.md) | [49. 사람 근접 안전](../categories/safety/human-proximity-safety.md) |  |  |  |
| [M. 안전](../categories/safety/index.md) | [50. 안전 표준·인증·사고 조사](../categories/safety/safety-standards-certification-and-incident-investigation.md) |  |  |  |
| [N. 보안·개인정보](../categories/security-and-privacy/index.md) | [51. 인증·권한·격리](../categories/security-and-privacy/authentication-authorization-and-isolation.md) |  | ○ |  |
| [N. 보안·개인정보](../categories/security-and-privacy/index.md) | [52. 통신 보호·위협 관리·감사](../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) |  |  |  |
| [N. 보안·개인정보](../categories/security-and-privacy/index.md) | [53. 개인정보·영상 데이터](../categories/security-and-privacy/privacy-and-video-data.md) |  |  |  |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [54. 시험·형식 검증·벤치마크](../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) | ○ | ○ | ○ |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [55. 현장 조사·설치·시운전](../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) | ○ |  | ○ |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [56. 운영 이관·확대·교육](../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) |  |  |  |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [57. 자산·소프트웨어 수명주기 관리](../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) | ○ |  | ○ |
| [P. 거버넌스·법규·사회](../categories/governance-law-and-society/index.md) | [58. 다사업자 책임·계약·데이터](../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) |  |  |  |
| [P. 거버넌스·법규·사회](../categories/governance-law-and-society/index.md) | [59. 법·규제·보험·라이선스](../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) |  |  |  |
| [P. 거버넌스·법규·사회](../categories/governance-law-and-society/index.md) | [60. 노동·수용성·접근성](../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [61. 물류창고](../categories/site-type-applications/warehouse.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [62. 제조 공장](../categories/site-type-applications/manufacturing-plant.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [63. 병원·의료](../categories/site-type-applications/hospital-and-healthcare.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [64. 상업 시설](../categories/site-type-applications/commercial-facilities.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [65. 가정·공동주택](../categories/site-type-applications/home-and-apartment.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [66. 실외](../categories/site-type-applications/outdoor.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [67. 기타 현장](../categories/site-type-applications/other-sites.md) |  |  |  |

● 중심 영역 · ○ 함께 필요한 영역 · 빈칸은 직접 연결 없음. 영역 수:

- 아이디어 1. 로봇 기능 온톨로지: ● 1개 · ○ 15개 · 합계 16개 영역 ([트랙 개요](../tracks/manual-capability-ontology/index.md))
- 아이디어 2. 채팅 기반 구성·운영: ● 6개 · ○ 16개 · 합계 22개 영역 ([트랙 개요](../tracks/chat-based-configuration-and-operation/index.md))
- 아이디어 3. 건축 도면 자동 인식: ● 1개 · ○ 14개 · 합계 15개 영역 ([트랙 개요](../tracks/floorplan-recognition/index.md))
<!-- auto:idea-area-map:end -->

## 관련 페이지

- [논의한 아이디어의 연구영역 매핑](../about/idea-mapping.md) — 분류 개정 전 원문 10장의 표 원문
- [매뉴얼 기반 로봇 기능 온톨로지](../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../tracks/chat-based-configuration-and-operation/index.md), [건축 도면 자동 인식](../tracks/floorplan-recognition/index.md) — 세 아이디어를 연구하는 중점 연구 트랙
- [에이전트 소개](../about/agents.md) — 트랙 실행과 트랙 조사 비중 설정
````
