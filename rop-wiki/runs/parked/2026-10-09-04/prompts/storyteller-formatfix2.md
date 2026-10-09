(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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

### runs/2026-10-09-04/verification.json

```json
{
  "run_id": "2026-10-09-04",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2607.14387 초록 열람 확인: 챗봇 인터페이스, RAG, DSL 스크립트, 123개 시나리오, CSR 76.42%·30.08%·16.26%, IROS 2026 채택. 단 C. 채팅 기반 구성·운영 페이지가 인용한 ref-833 과 저자·제목·발행일이 같은 논문이므로 ref-833 재사용 필요."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 해석 [추정] 유지. ref-528 은 원문 텍스트 입력으로 확인, ref-1088 은 원문 미열람(재인용). 근거 발췌의 '실행 불가'는 원문 지표가 컴파일 성공률이므로 '컴파일 실패'로 써야 함. ref-1329 → ref-833."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2608.23622 초록 열람 확인: 질의·기준 구성 → 실험 설계 → 비교 시뮬레이션 → 해석 → 공정 매개변수 권고, 제약 공정 설계, ETFA 2026 채택. ref-832 와 같은 논문이므로 ref-832 재사용 필요."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 해석 [추정] 유지. 근거 두 건(ref-1330=ref-832, ref-1127) 모두 열람 확인, 둘 다 로봇 플릿 대상 아님을 본문에 유지."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2312.09067 초록 열람 확인: GPT-4 상식·공간 제약, 배치 최적화, Objaverse, 생성 장면 학습 에이전트의 새 환경 주행, CVPR 2024 게재(v2 2024-04-22)."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1089 는 이번 실행 원문 미열람(재인용, 33. 시나리오 모델·편집 페이지 각주와 일치)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-291 원문 미열람, B. 로봇 온톨로지 대분류 페이지·E 대분류 연결 브리프(2026-10-09-03 f30)의 같은 주장과 같은 각주 재사용. 근거가 제조 대상이라는 한계 병기."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 텍스트(data/source_texts) 대조 확인: door_supervisor 의 문 충돌 방지, lift_supervisor 의 다플릿 요청 관리, TeleportDispenser·TeleportIngestor, 같은 메시지 교환 유지 문장. 발행일 미확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 대조 확인: full control 로봇 플러그인, PathRequest·ModeRequest 구독, 레일식 직선 주행, 장애물 감지 시 정지, 정적 장애물 없는 경로·2륜 차동 구동 가정, 주행 스택 계산 부담 회피."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 대조 확인(Motivation 절): 준비·정지·초기화 부담, 배터리·충돌 비용 없음, 반복 시나리오로 수정 확인, 드문 예외, 장시간 시뮬레이션의 시설 소유자 확신."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1126·ref-1130 은 이번 실행 원문 미열람(36. 가상 시운전·실제 상황 재현 페이지 검증 주장 재인용). PLC·설비 제어 가상 시운전은 연계 대상으로 서술해야 함."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2608.26066 초록 열람 확인: ROS 2·Unity, 혼합 현실, 가상·실제 LiDAR, ChoiRbot 분산 실험, 실제·가상 로봇 작업 배정 예제, 컨테이너 배포."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 근거 출처 열람 확인. 플랫폼 배치 근거 없음(oq-040) 문구 유지."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "35. 처리능력·규모·배치 설계 페이지 3·10절 검증된 [사실] 재인용, 세 출처 모두 원문 미열람. 세 출처는 각각 다른 내용이며 교차 확인 아님."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "ref-105 원문 텍스트로 recharge_threshold 0.10('below which robots in this fleet will not operate') 확인. 그러나 '충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어진다'는 원문에 없고 35 페이지에서도 [추정]이었다. 설정값 문장은 [사실], 결론 부분은 [추정]으로 분리."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "G. 계획·최적화 대분류 페이지 검증된 [사실] 재인용, 원문 미열람. 저자 계산 실험 조건·독립 재현 미확인 단서 유지."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "34. 시뮬레이션·예측용 디지털 트윈 페이지와 G 대분류 페이지 검증된 [사실] 재인용, 두 출처 원문 미열람. 시뮬레이션 결과이며 현장 실측 아님 단서 유지."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "ref-267 원문 미열람. 연구의 존재는 34 페이지에서 [사실]이나, '경로망 배치 평가가 가정한 미래를 실험하는 쪽에 걸친다'는 G 대분류 페이지에서 [추정]으로 실린 해석이다. 연구 존재는 [사실], 위치 판단은 [추정]으로 분리."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "검증 중 movingai.com MAPF 벤치마크 페이지 열람: 지도와 지도별 시나리오 파일(even·random 각 25개) 제공은 확인. '같은 조건에서 비교하게 한다'는 페이지에 명시되지 않은 해석이고 시나리오 형식과의 연결도 해석이므로, 제공 사실만 [사실], 나머지는 [추정]."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 5절 검증된 [사실] 재인용(이번 실행 원문 미열람). ref-943 은 참고문헌의 ref-060(doi 링크)과 같은 논문이다. 승강기 제어는 연계 대상 문구 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "35 페이지 9절 검증된 [사실] 재인용, 원문 미열람. 승강기 제어 연계 대상 문구 유지."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지, 의견 주체(Lee 외 저자들) 명시됨. 36 페이지 5절 재인용, 원문 미열람."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-528 원문 텍스트 대조 확인: 컨베이어·전압 시험기 고장(START_TIME·DURATION), 진공 그리퍼(GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID). 발행일 미확인."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-116·ref-1090 원문 미열람(33 페이지 재인용). ref-1090 은 벤더 문서 유형이나 이 주장은 기능·성능 주장이 아님."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 대조 확인(.building.yaml → 층별 바닥·벽 메시, 문·승강기 sdf, 로봇 블록, 주석 수정 후 재생성, 기본 월드에 플러그인 없음·템플릿 월드). ref-079 원문 텍스트로 충전기·문·승강기 주석 확인. 두 출처 같은 기관이라 교차 확인 아님."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1092 원문 미열람(33 페이지 9절 재인용). 등록 정보–시뮬레이션 모델 연결 사례 미확인 단서 유지."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "rosbag2 README(rolling) 열람 확인: 기록·재생 도구, 기본 저장 형식 mcap, ~/set_rate·--clock·~/play 시작 오프셋, --topics, -i 여러 백 파일 기록 시각순 재생, 크기·기간 분할, zstd, 스냅숏 모드. 재생 속도·시작 시각은 CLI 플래그가 아니라 서비스·매개변수로 제공된다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 근거 출처 열람 확인, oq-131 연결 유지."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2310.08710 초록 열람 확인: 실제 주행 기록으로 초기화·재생, 학습·규칙 기반 행동 모델, TPU/GPU 그래프 안 시뮬레이션. 자율주행 대상이며 로봇 현장 사례 아님 단서 유지."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 대조 확인: crowdsim 은 선택 기능, menge 기반, rmf_traffic_editor 에서 켬, airport_terminal use_crowdsim:=1. ref-104 는 같은 기관(독립 교차 확인 아님)이며 원문 미열람. 공항은 33 페이지와 같이 상업 시설로 둔다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 1912.06321 초록 열람 확인: SRCC 제안, LoCoBot, 모델 9개 병행 시험, 성공률 SRCC 0.18 → 0.844, 벽 미끄러짐. 다만 0.18 은 'CVPR 2019 챌린지에서 쓰인 Habitat 설정'의 값이므로 '기본 설정'은 그 표현으로 고친다. RA-L 2020."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-741 원문 미열람(36 페이지 9절 재인용), ref-1127 열람 확인. 현실 격차 보정은 연계 대상 문구 유지."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 7절 검증된 [사실] 재인용, 이번 실행 원문 미열람. 발행일 2024-03-05."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. oq-156 연결, 대응 체계 자료 미확인 단서 유지."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2011.10294 초록 열람 확인: 사람 모델+최적화로 고위험 사람 행동 생성, 초기 설계 단계, 무작위·몬테카를로 탐색 비실용, 산업용 로봇 셀 개념 증명. 게재처 2020 IEEE SPCE."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1086 원문 미열람(33 페이지 재인용). 안전 인증·설비 안전 제어는 연계 대상 문구 유지."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2211.09507 초록 열람 확인: ROS 구동 시스템, 디지털 트윈에 대한 person-in-the-middle 공격이 물리 시스템 붕괴로 이어질 수 있음, 산업용 로봇·자율이동로봇 모두 해당, 완화 방안 논의. '중간자 공격' 표기 허용."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 로봇 플릿 플랫폼 사례 없음 단서 유지."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "브리프에서는 원문 미열람이었으나 검증 중 classic.gazebosim.org 튜토리얼을 열어 확인: database.config 의 license 요소, CC BY 3.0 Unported 권장(요구 아님), model.config 의 author·name·email 필수. 발행일 미확인."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "34 페이지 7·11절 검증된 주장 재인용, 두 출처 원문 미열람. 두 출처는 서로 다른 부(제1부·제6부)를 가리키며 교차 확인 아님."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·'연계 대상:' 표시 유지. ref-521 원문 미열람(34 페이지 재인용). 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "F. 연동 대분류 페이지 검증된 [사실] 재인용, 원문 미열람. 대상이 공동주택이며 물류센터가 아님을 유지."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 두 출처 원문 미열람. oq-011 연결 유지."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 36 페이지 5절 재인용, 원문 미열람. 페이지에 '벤더 주장' 병기 필수. 컨베이어·피킹 모듈 제어 에뮬레이션은 설비 업체·통합자 쪽 연계 대상."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 5절 검증된 [사실] 재인용, 원문 미열람. PLC 코드 가상 시운전은 연계 대상 문구 유지."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "33 페이지 5절 검증된 [사실] 재인용, ref-104 원문 미열람. 시뮬레이션 예제 월드이며 실제 시설 사례 아님 단서 유지."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "33 페이지 5절 검증된 [사실] 재인용, 원문 미열람. 벤치마크이며 실제 가정 배치 아님."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 검증 중 NVIDIA 블로그를 열어 확인: 발행일 2025-01-06, 'developing, testing and optimizing ... robot fleets at scale in a digital twin before deployment', 센서 시뮬레이션·합성 데이터. 브리프의 발행일 null·as_of 2026-10-09 는 2025-01-06 으로 고쳐야 함."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 34 페이지 5절의 [추정] 벤더 주장 재인용, 원문 미열람. 이후 적용 결과 미확인 단서 유지(oq-084, oq-117)."
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
      "ref-1329(Chat2Scenic, arXiv 2607.14387)은 C. 채팅 기반 구성·운영 대분류 자료 목록의 ref-833 과 저자·제목·발행일(2026-07-15)이 같은 논문이다 — 새 id 대신 ref-833 재사용",
      "ref-1330(Xia 외, LLM Agents Perform Controlled Experiments Using Simulation Models)은 ref-832 와 저자·제목·발행일(2026-08-22)이 같은 논문이다 — ref-832 재사용",
      "ref-943(PMC 링크)과 ref-060(doi 링크)은 같은 Lee 외 Digital Health 논문이다. 35. 처리능력·규모·배치 설계 페이지는 ref-060, 36. 가상 시운전·실제 상황 재현 페이지는 ref-943 을 쓴다 — 이번 절에서는 ref-943 하나로만 인용",
      "f7(18. 실시간 세계 상태·데이터 일관성 ↔ 34. 시뮬레이션·예측용 디지털 트윈 구분)은 B. 로봇 온톨로지 대분류 페이지와 E. 사물·사람·실시간 상태 연결 브리프(2026-10-09-03 f30)의 같은 주장과 겹친다 — 같은 각주 ref-291 재사용, 모순 없음",
      "f15·f17·f18·f14·f16 은 A. 기획·사업·G. 계획·최적화 대분류 페이지의 옛 분류 기준 연결과 겹친다 — 같은 각주 재사용, 태그는 그 페이지의 사실·추정 구분을 따른다"
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
    "f1·f2·ref-1329: 각주를 새 id ref-1329 가 아니라 기존 ref-833 으로 쓰고 reference_updates 에 ref-1329 를 넣지 않는다 — C. 채팅 기반 구성·운영 대분류 자료 목록의 ref-833 이 저자·제목·발행일이 같은 Chat2Scenic 논문이다.",
    "f3·f4·ref-1330: 각주를 기존 ref-832 로 쓰고 ref-1330 을 등록하지 않는다 — 같은 Xia 외 논문이 ref-832 로 이미 있다.",
    "f15: 'Open-RMF 플릿 어댑터 템플릿 설정에서 배터리가 recharge_threshold(예시값 0.10) 아래인 로봇은 작동하지 않는다'만 [사실][^ref-105]로 쓰고, '충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어진다'는 별도 문장 [추정]으로 강등한다 — 결론 부분은 원문에 없고 35. 처리능력·규모·배치 설계 페이지에서도 [추정]이었다.",
    "f18: '다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다'만 [사실][^ref-267], '경로망 배치 평가가 가정한 미래를 실험하는 쪽에 걸친다'는 [추정]으로 나눈다 — G. 계획·최적화 대분류 페이지가 이 해석을 [추정]으로 실었다.",
    "f19: 'Moving AI Lab 의 MAPF 벤치마크는 지도마다 시나리오 파일을 묶어 공개한다'만 [사실][^ref-1091], '같은 조건 비교와 시나리오 형식·라이브러리와 맞닿는다'는 [추정]으로 강등한다 — 벤치마크 페이지는 비교 목적을 명시하지 않는다(검증 중 열람 확인).",
    "f2: 본문에서 Chat2Scenic 수치를 '실행 불가'가 아니라 '컴파일 실패'로 쓴다 — 원문 지표는 컴파일 성공률(CSR)이다.",
    "f31: 'Habitat 기본 설정의 성공률 SRCC 0.18'을 'CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 0.18'로 고친다 — 초록의 표현이 그렇다.",
    "f44·f48·f49: 본문에 [추정]과 '벤더 주장'을 병기한다. f48 의 ref-527 각주 발행일을 '미확인'에서 2025-01-06 으로 고친다 — 검증 중 NVIDIA 블로그 원문에서 확인했다.",
    "각주 원문 미열람 표기: 브리프에서 원문을 열지 않은 출처(ref-104, ref-101, ref-398, ref-267, ref-098, ref-109, ref-102, ref-381, ref-943, ref-103, ref-1088, ref-1089, ref-116, ref-1090, ref-1091, ref-1092, ref-1086, ref-971, ref-291, ref-521, ref-516, ref-518, ref-1126, ref-1130, ref-1131, ref-1133, ref-741, ref-1239, ref-409, ref-106, ref-1165, ref-527, ref-526)의 각주 정의에는 접근일 뒤 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다. ref-079·ref-105·ref-528 은 data/source_texts 원문이 입력에 있으므로 원문 미열람 표기를 하지 않는다.",
    "범위 경계 문구: f8·f20·f21·f42 의 승강기·문 제어, f11·f44·f45 의 PLC·컨베이어 제어 코드 가상 시운전, f9·f32·f48 의 로봇 자체 주행·센서 시뮬레이션·현실 격차 보정, f35·f36 의 안전 인증·설비 안전 제어는 각 문장에서 '연계 대상'으로 짧게 밝힌다. f41 은 '연계 대상:'으로 시작하는 문장 그대로 둔다 — 분류 원문 19장 경계.",
    "18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈: f7 로 '18은 현재 상태 표현, 34는 가정한 미래 실험'을 E. 사물·사람·실시간 상태 연결 항목에 밝히고, f37·f38 의 디지털 트윈 동기화는 36. 가상 시운전·실제 상황 재현이 두 영역을 잇는 경로로만 서술한다. 34가 현재 상태를 표현한다고 쓰지 않는다.",
    "f14: 세 출처(ref-102·ref-098·ref-109)는 각각 다른 내용이므로 문장을 나눠 각자의 각주를 붙이고 교차 확인된 것처럼 묶어 쓰지 않는다.",
    "f20·f22: Lee 외 병원 논문은 ref-943 하나로만 인용하고 ref-060 을 같은 문장에 함께 붙이지 않는다 — 두 id 가 같은 논문이다.",
    "'아직 다루지 않은 연결' 목록을 브리프 finding 이 실제로 다루지 않은 세부영역과 맞춘다: 브리프 rationale 의 29·30·31·40·41·43·53·58·60 에 더해 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 8. 채팅으로 맵 작성, 10. 채팅으로 로봇 구성, 12. 채팅으로 업무 지시·오케스트레이션, 17. 작업 대상·자산 식별과 인계 추적, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 50. 안전 표준·인증·사고 조사, 56. 운영 이관·확대·교육, 57. 자산·소프트웨어 수명주기 관리, 66. 실외, 67. 기타 현장을 적는다. '모든 대분류와 연결' 같은 완전성 표현은 쓰지 않는다.",
    "다른 대분류와 세부영역은 새 17개 대분류 기준의 문자+이름, 번호+이름으로 쓴다(예: 'F. 연동', '25. 작업 배정 — MRTA'). A·B·F·G 대분류 페이지의 옛 대분류 이름(예: 'C. 연결·실행 기반', 'F. 도입·검증·유지관리')을 옮겨 쓰지 않는다 — 그 페이지들의 연결 절은 이전 분류 기준이다.",
    "L. AI·학습 기술 관련 연결(f5·f6·f32)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영 링크와 적용 대상인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현 링크를 함께 둔다 — 공통 규칙 5(교차 규칙)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 46건, 미확인 3건(f15·f18·f19는 사실 부분과 해석 부분이 섞여 해석을 분리), 교차 확인 0건. 강등: f15·f18·f19 사실 → 사실+추정 분리(결론·위치 판단 부분 추정). 원문 미열람 출처: ref-104, ref-101, ref-398, ref-267, ref-098, ref-109, ref-102, ref-381, ref-943, ref-103, ref-1088, ref-1089, ref-116, ref-1090, ref-1091, ref-1092, ref-1086, ref-971, ref-291, ref-521, ref-516, ref-518, ref-1126, ref-1130, ref-1131, ref-1133, ref-741, ref-1239, ref-409, ref-106, ref-1165, ref-527, ref-526(이 가운데 ref-1091·ref-1239·ref-527은 검증 중 원문을 열어 해당 진술을 확인했다). 주의: 이 절의 연결은 대부분 단일 출처 또는 게시된 세부영역 페이지의 재인용에 기대고, 연결 해석 13건은 [추정]이다. 다중 로봇 플릿 오케스트레이션에 직접 적용된 근거는 Open-RMF 시뮬레이션 문서와 VirTooS 정도이고, 대화형 시나리오 생성(Chat2Scenic: 자율주행)·언어 모델 비교 실험(제약 공정)·시뮬레이션 예측력(LoCoBot 주행)·디지털 트윈 공격(ROS 로봇) 근거는 로봇 플릿이 아닌 대상에서 나왔다. 벤더 주장 3건(f44·f48·f49)은 독립 확인되지 않았다. 신규 출처 ref-1329·ref-1330은 기존 ref-833·ref-832와 같은 논문이라 재사용을 지시했고, ref-943과 ref-060이 같은 논문으로 참고문헌에 이중 등록돼 있다. 브리프의 ref-079·ref-105·ref-528은 fetched true인데 요약이 '원문 미열람'이고 fetch_url이 비어 있어 표시가 어긋난다(입력의 data/source_texts 원문으로 열람을 확인했다). 정정 요청 없음. 검증 검색 0회, 열람 12회.",
  "retry_reason": null
}
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 62건 / 전체 1242건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [33, 34, 35, 36] 에 걸린 30건 / 전체 294건)

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

### docs/standards/index.md (요약: 318개 — 이름 · 종류 · 발행 기관)

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
- rosbag2 · ROS 2 (ros2/rosbag2 GitHub) · 오픈소스
- Simod (로그 기반 업무 프로세스 시뮬레이션 모델 자동 발견 도구) · Camargo, M., Dumas, M., & González-Rojas, O. · 오픈소스
- Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 구성(compose 범주)과 단계 API(ros2multirobotbook task_new) · Open Robotics · 오픈소스
- VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개) · Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) · 오픈소스
- EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) · 개인정보보호위원회 · 프레임워크
- 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 · 과학기술정보통신부·한국정보통신기술협회(TTA) · 프레임워크
- Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크) · Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- langbar (다중 모달 GUI–MCP 아키텍처 참조 구현) · van Dam, H. G. W. · 오픈소스
- IDTA 02006 Digital Nameplate for Industrial Equipment (3.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA-01002 Asset Administration Shell Specification — API (3.2.0) · IDTA(Industrial Digital Twin Association) · 표준
- RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 평가 프로그램
- CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현) · CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) · 오픈소스
- OWL 2 Web Ontology Language Structural Specification (Second Edition) · W3C · 표준
- IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙 · IDTA(Industrial Digital Twin Association) · 표준
- KGCL (Knowledge Graph Change Language) · Hegde, H. 외 (Database, Oxford) · 프레임워크
- ISO 13482 (서비스 로봇 안전 요구사항) · ISO · 표준
- RoMi-H (Robotic Middleware for Healthcare) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 오픈소스
- 서비스로봇 실증사업 · 한국로봇산업진흥원 · 평가 프로그램
- 스마트병원 선도모델(9개 모듈) · 한국보건산업진흥원 스마트병원 확산지원센터 · 프레임워크
- 로봇 친화형 건축물 인증 · 스마트도시협회 · 평가 프로그램
- Matter 1.2 (로봇청소기 장치 유형 포함) · Connectivity Standards Alliance (CSA) · 표준
- 실외이동로봇 운행안전인증 (지능형로봇법 제40조의2) · 한국로봇산업진흥원 · 평가 프로그램
- ISO/TR 4448-1:2024 Public-area mobile robots (PMR) — Part 1: Overview of paradigm · ISO (ISO/TC 204) · 표준
- ISO 4448 시리즈 (Public-area mobile robots, Part 6·9·16 개발 중) · ISO/TC 204 · 표준
- Nav2 GPS 항법 구성 (navsat_transform·두 EKF 융합·rolling 전역 비용 지도) · Open Navigation (Nav2) · 오픈소스
- SiLA 2 (Standardization in Lab Automation 2) · SiLA Consortium · 표준
- ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역 · ISO · 표준
- SS 713 Data Exchange Between Robots, Lifts and Automated Doorways · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- TR 130 Interoperability Between Robots and Central Command Systems · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- IEEE 1873-2015 Robot Map Data Representation for Navigation · IEEE Standards Association (IEEE RAS) · 표준
- osmAG (OSM 형식 계층형 위상·거리 의미 지도) · Feng, D. 외 (arXiv) · 프레임워크
- Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) · Open Robotics (open-rmf) · 오픈소스
- OpenAPI Specification 3.1.0 · OpenAPI Initiative · 표준
- AsyncAPI Specification 3.1.0 · AsyncAPI Initiative · 표준
- FogROS2 (클라우드·포그 로보틱스 플랫폼) · Ichnowski, J., Chen, K., Dharmarajan, K. 외 · 오픈소스
- MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) · Foxglove (ROS 2 채택: Open Robotics) · 오픈소스
- OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 · OpenTelemetry (CNCF) · 오픈소스
- ros-opentelemetry · szobov (GitHub, 개인 저장소) · 오픈소스
- Mender (OTA 업데이트 관리자) · Northern.tech (mendersoftware) · 오픈소스
- FinOps 프레임워크 (FinOps Phases) · FinOps Foundation · 프레임워크
- FOCUS 1.2 (FinOps 청구 데이터 명세) · FinOps Foundation · 표준
- Open X-Embodiment 데이터셋·RT-X 모델 · Open X-Embodiment Collaboration · 오픈소스
- OpenVLA · Kim, M. J., Pertsch, K., Karamcheti, S. 외 · 오픈소스
- GR00T N1 · NVIDIA · 오픈소스
- POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) · Skrynnik, A. 외 (ICLR 2025) · 평가 프로그램
- ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 · ISO (ISO/TC 108) · 표준
- Docling (AI 기반 문서 변환 오픈소스 도구) · IBM Research · 오픈소스
- LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리) · Google (google/langextract) · 오픈소스
- AECV-Bench (건축·엔지니어링 도면 이해 벤치마크) · Kondratenko, A. 외 (arXiv 2601.04819) · 평가 프로그램
- FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋) · Fan, Z. 외 (arXiv 2105.07147) · 평가 프로그램
- Nav2 Collision Monitor (nav2_collision_monitor) · Open Navigation (ros-navigation/navigation2) · 오픈소스
- ASAM OpenSCENARIO XML (1.4.0) · ASAM e.V. · 표준
- SDFormat (Simulation Description Format) · Open Source Robotics Foundation · 오픈소스
- BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) · Stanford 등 (Li, C. 외) · 평가 프로그램
- Moving AI MAPF 벤치마크 · Moving AI Lab (Sturtevant 외) · 평가 프로그램
- Arena-Bench · Kästner, L. 외 (RA-L 2022) · 평가 프로그램
- ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) · ISA(International Society of Automation) · 표준
- Open-RMF rmf_visualization · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) · Open Robotics (open-rmf) · 오픈소스
- IEC 62559 사용 사례 방법론 (Part 1~4) · IEC · 표준
- ISO/IEC/IEEE 29148:2018 요구공학 · ISO / IEC / IEEE · 표준
- 로봇활용 표준공정모델 · 산업통상자원부 · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) · OWASP GenAI Security Project · 프레임워크
- EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) · European Union (IES 해설 경유) · 프레임워크
- KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 · 과학기술정보통신부·한국인터넷진흥원(KISA) · 프레임워크
- 윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard) · Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) · 프레임워크
- VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) · VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) · 표준
- NASA-STD-7009B Standard for Models and Simulations · NASA · 표준
- 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) · 개인정보보호위원회 · 프레임워크
- 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) · 개인정보보호위원회 · 프레임워크
- 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) · 개인정보보호위원회 · 프레임워크
- 영상정보 원본 활용 규제샌드박스 실증특례 · 개인정보보호위원회 · 프레임워크
- EDPB Guidelines 3/2019 on processing of personal data through video devices · European Data Protection Board (EDPB) · 프레임워크
- EgoBlur · Meta Reality Labs · 오픈소스
- ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 · ANSI / A3(Association for Advancing Automation) · 표준
- HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications · UK Health and Safety Executive (HSE) · 프레임워크
- IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 · IEC(International Electrotechnical Commission) · 표준
- REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) · ROS (ros-infrastructure/rep) · 프레임워크
- HuNavSim (ROS 2 사람 보행 시뮬레이터) · Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. · 오픈소스
- Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) · Open Robotics · 오픈소스
- 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) · Francis, A. 외 · 프레임워크
- BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크) · BSRIA · 프레임워크
- 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 · 법제처(법령해석 법제처-23-0872 경유) · 프레임워크
- EU 데이터법 (Regulation (EU) 2023/2854, Data Act) · European Union (European Commission 해설) · 프레임워크
- EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안 · European Commission · 프레임워크
- 산업데이터 계약 가이드라인 · 산업통상부 · 프레임워크
- Kubernetes Deprecation Policy (API 폐기 정책) · The Kubernetes Authors · 오픈소스
- ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념 · ISO/IEC (JTC 1) · 표준
- IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항 · IEC · 표준
- EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무) · European Union (Future of Life Institute 비공식 게재본 경유) · 프레임워크
- 21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적) · U.S. Food and Drug Administration · 프레임워크
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
```

### runs/2026-10-09-04/docs_tree.txt

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
glossary/3d-scene-graph.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/as-planned-vs-as-built-deviation.md
glossary/asam-openscenario.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/asyncapi-specification.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
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
glossary/cell-based-production.md
glossary/clarification-question.md
glossary/cloud-robotics.md
glossary/coalition-formation.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/common-coordinate-system.md
glossary/common-data-environment.md
glossary/compensating-transaction.md
glossary/competency-question.md
glossary/condition-based-maintenance.md
glossary/configuration-copilot.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/confused-deputy.md
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/control-barrier-function.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-embodiment-learning.md
glossary/cross-schedule-dependency.md
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
glossary/dds-security.md
glossary/deadlock.md
glossary/decision-focused-learning.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/document-layout-analysis.md
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/ethical-black-box.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explainable-mapf.md
glossary/explicit-implicit-confirmation.md
glossary/face-obfuscation.md
glossary/failure-explanation.md
glossary/falsification.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/finops.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/giai.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hardware-in-the-loop.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/hmi-philosophy.md
glossary/human-in-the-loop.md
glossary/human-motion-trajectory-prediction.md
glossary/hungarian-method.md
glossary/i-pass-handoff-program.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indirect-prompt-injection.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/irreducible-infeasible-subset.md
glossary/isa-95.md
glossary/it-ot-convergence.md
glossary/jailbreak.md
glossary/job-shop-scheduling-problem.md
glossary/joint-goal-accuracy.md
glossary/json-schema.md
glossary/keystroke-level-model.md
glossary/kiosk-accessibility.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pay-per-pick.md
glossary/payback-period.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/personal-delivery-device.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/pseudonymisation.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/raw-video-regulatory-sandbox-exemption.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-standard-process-model.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-ambiguity.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/security-level-iec-62443.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shift-handover.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/sim-vs-real-correlation-coefficient.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-awareness.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/slot-filling.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
glossary/software-in-the-loop.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/stakeholder-requirements-specification.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
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
logs/daily/2026-09-30.md
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
references/ref-1000.md
references/ref-1001.md
references/ref-1002.md
references/ref-1003.md
references/ref-1004.md
references/ref-1005.md
references/ref-1006.md
references/ref-1007.md
references/ref-1008.md
references/ref-1009.md
references/ref-101.md
references/ref-1010.md
references/ref-1011.md
references/ref-1012.md
references/ref-1013.md
references/ref-1014.md
references/ref-1015.md
references/ref-1016.md
references/ref-1017.md
references/ref-1018.md
references/ref-1019.md
references/ref-102.md
references/ref-1020.md
references/ref-1021.md
references/ref-1022.md
references/ref-1023.md
references/ref-1024.md
references/ref-1025.md
references/ref-1026.md
references/ref-1027.md
references/ref-1028.md
references/ref-1029.md
references/ref-103.md
references/ref-1030.md
references/ref-1031.md
references/ref-1032.md
references/ref-1033.md
references/ref-1034.md
references/ref-1035.md
references/ref-1036.md
references/ref-1037.md
references/ref-1038.md
references/ref-1039.md
references/ref-104.md
references/ref-1040.md
references/ref-1041.md
references/ref-1042.md
references/ref-1043.md
references/ref-1044.md
references/ref-1045.md
references/ref-1046.md
references/ref-1047.md
references/ref-1048.md
references/ref-1049.md
references/ref-105.md
references/ref-1050.md
references/ref-1051.md
references/ref-1052.md
references/ref-1053.md
references/ref-1054.md
references/ref-1055.md
references/ref-1056.md
references/ref-1057.md
references/ref-1058.md
references/ref-1059.md
references/ref-106.md
references/ref-1060.md
references/ref-1061.md
references/ref-1062.md
references/ref-1063.md
references/ref-1064.md
references/ref-1065.md
references/ref-1066.md
references/ref-1067.md
references/ref-1068.md
references/ref-1069.md
references/ref-107.md
references/ref-1070.md
references/ref-1071.md
references/ref-1072.md
references/ref-1073.md
references/ref-1074.md
references/ref-1075.md
references/ref-1076.md
references/ref-1077.md
references/ref-1078.md
references/ref-1079.md
references/ref-108.md
references/ref-1080.md
references/ref-1081.md
references/ref-1082.md
references/ref-1083.md
references/ref-1084.md
references/ref-1085.md
references/ref-1086.md
references/ref-1087.md
references/ref-1088.md
references/ref-1089.md
references/ref-109.md
references/ref-1090.md
references/ref-1091.md
references/ref-1092.md
references/ref-1093.md
references/ref-1094.md
references/ref-1095.md
references/ref-1096.md
references/ref-1097.md
references/ref-1098.md
references/ref-1099.md
references/ref-110.md
references/ref-1100.md
references/ref-1101.md
references/ref-1102.md
references/ref-1103.md
references/ref-1104.md
references/ref-1105.md
references/ref-1106.md
references/ref-1107.md
references/ref-1108.md
references/ref-1109.md
references/ref-111.md
references/ref-1110.md
references/ref-1111.md
references/ref-1112.md
references/ref-1113.md
references/ref-1114.md
references/ref-1115.md
references/ref-1116.md
references/ref-1117.md
references/ref-1118.md
references/ref-1119.md
references/ref-112.md
references/ref-1120.md
references/ref-1121.md
references/ref-1122.md
references/ref-1123.md
references/ref-1124.md
references/ref-1125.md
references/ref-1126.md
references/ref-1127.md
references/ref-1128.md
references/ref-1129.md
references/ref-113.md
references/ref-1130.md
references/ref-1131.md
references/ref-1132.md
references/ref-1133.md
references/ref-1134.md
references/ref-1135.md
references/ref-1136.md
references/ref-1137.md
references/ref-1138.md
references/ref-1139.md
references/ref-114.md
references/ref-1140.md
references/ref-1141.md
references/ref-1142.md
references/ref-1143.md
references/ref-1144.md
references/ref-1145.md
references/ref-1146.md
references/ref-1147.md
references/ref-1148.md
references/ref-1149.md
references/ref-115.md
references/ref-1150.md
references/ref-1151.md
references/ref-1152.md
references/ref-1153.md
references/ref-1154.md
references/ref-1155.md
references/ref-1156.md
references/ref-1157.md
references/ref-1158.md
references/ref-1159.md
references/ref-116.md
references/ref-1160.md
references/ref-1161.md
references/ref-1162.md
references/ref-1163.md
references/ref-1164.md
references/ref-1165.md
references/ref-1166.md
references/ref-1167.md
references/ref-1168.md
references/ref-1169.md
references/ref-117.md
references/ref-1170.md
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
references/ref-1195.md
references/ref-1196.md
references/ref-1197.md
references/ref-1198.md
references/ref-1199.md
references/ref-120.md
references/ref-1200.md
references/ref-1201.md
references/ref-1202.md
references/ref-1203.md
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
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
references/ref-824.md
references/ref-825.md
references/ref-826.md
references/ref-827.md
references/ref-828.md
references/ref-829.md
references/ref-830.md
references/ref-831.md
references/ref-832.md
references/ref-833.md
references/ref-834.md
references/ref-835.md
references/ref-836.md
references/ref-837.md
references/ref-838.md
references/ref-839.md
references/ref-840.md
references/ref-841.md
references/ref-842.md
references/ref-843.md
references/ref-844.md
references/ref-845.md
references/ref-846.md
references/ref-847.md
references/ref-848.md
references/ref-849.md
references/ref-850.md
references/ref-851.md
references/ref-852.md
references/ref-853.md
references/ref-854.md
references/ref-855.md
references/ref-856.md
references/ref-857.md
references/ref-858.md
references/ref-859.md
references/ref-860.md
references/ref-861.md
references/ref-862.md
references/ref-863.md
references/ref-864.md
references/ref-865.md
references/ref-866.md
references/ref-867.md
references/ref-868.md
references/ref-869.md
references/ref-870.md
references/ref-871.md
references/ref-872.md
references/ref-873.md
references/ref-874.md
references/ref-875.md
references/ref-876.md
references/ref-877.md
references/ref-878.md
references/ref-879.md
references/ref-880.md
references/ref-881.md
references/ref-882.md
references/ref-883.md
references/ref-884.md
references/ref-885.md
references/ref-886.md
references/ref-887.md
references/ref-888.md
references/ref-889.md
references/ref-890.md
references/ref-891.md
references/ref-892.md
references/ref-893.md
references/ref-894.md
references/ref-895.md
references/ref-896.md
references/ref-897.md
references/ref-898.md
references/ref-899.md
references/ref-900.md
references/ref-901.md
references/ref-902.md
references/ref-903.md
references/ref-904.md
references/ref-905.md
references/ref-906.md
references/ref-907.md
references/ref-908.md
references/ref-909.md
references/ref-910.md
references/ref-911.md
references/ref-912.md
references/ref-913.md
references/ref-914.md
references/ref-915.md
references/ref-916.md
references/ref-917.md
references/ref-918.md
references/ref-919.md
references/ref-920.md
references/ref-921.md
references/ref-922.md
references/ref-923.md
references/ref-924.md
references/ref-925.md
references/ref-926.md
references/ref-927.md
references/ref-928.md
references/ref-929.md
references/ref-930.md
references/ref-931.md
references/ref-932.md
references/ref-933.md
references/ref-934.md
references/ref-935.md
references/ref-936.md
references/ref-937.md
references/ref-938.md
references/ref-939.md
references/ref-940.md
references/ref-941.md
references/ref-942.md
references/ref-943.md
references/ref-944.md
references/ref-945.md
references/ref-946.md
references/ref-947.md
references/ref-948.md
references/ref-949.md
references/ref-950.md
references/ref-951.md
references/ref-952.md
references/ref-953.md
references/ref-954.md
references/ref-955.md
references/ref-956.md
references/ref-957.md
references/ref-958.md
references/ref-959.md
references/ref-960.md
references/ref-961.md
references/ref-962.md
references/ref-963.md
references/ref-964.md
references/ref-965.md
references/ref-966.md
references/ref-967.md
references/ref-968.md
references/ref-969.md
references/ref-970.md
references/ref-971.md
references/ref-972.md
references/ref-973.md
references/ref-974.md
references/ref-975.md
references/ref-976.md
references/ref-977.md
references/ref-978.md
references/ref-979.md
references/ref-980.md
references/ref-981.md
references/ref-982.md
references/ref-983.md
references/ref-984.md
references/ref-985.md
references/ref-986.md
references/ref-987.md
references/ref-988.md
references/ref-989.md
references/ref-990.md
references/ref-991.md
references/ref-992.md
references/ref-993.md
references/ref-994.md
references/ref-995.md
references/ref-996.md
references/ref-997.md
references/ref-998.md
references/ref-999.md
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
topics/2026/2026-09-29-area01-s10.md
topics/2026/2026-09-29-area01-s11.md
topics/2026/2026-09-29-area01-s3.md
topics/2026/2026-09-29-area01-s4.md
topics/2026/2026-09-29-area01-s6.md
topics/2026/2026-09-29-area01-s7.md
topics/2026/2026-09-29-area01-s8.md
topics/2026/2026-09-29-area04-s10.md
topics/2026/2026-09-29-area04-s11.md
topics/2026/2026-09-29-area04-s3.md
topics/2026/2026-09-29-area04-s4.md
topics/2026/2026-09-29-area04-s6.md
topics/2026/2026-09-29-area04-s7.md
topics/2026/2026-09-29-area04-s8.md
topics/2026/2026-09-29-area06-s10.md
topics/2026/2026-09-29-area06-s11.md
topics/2026/2026-09-29-area06-s3.md
topics/2026/2026-09-29-area06-s4.md
topics/2026/2026-09-29-area06-s6.md
topics/2026/2026-09-29-area06-s7.md
topics/2026/2026-09-29-area06-s8.md
topics/2026/2026-09-29-area07-s10.md
topics/2026/2026-09-29-area07-s11.md
topics/2026/2026-09-29-area07-s3.md
topics/2026/2026-09-29-area07-s4.md
topics/2026/2026-09-29-area07-s6.md
topics/2026/2026-09-29-area07-s7.md
topics/2026/2026-09-29-area07-s8.md
topics/2026/2026-09-29-area08-s10.md
topics/2026/2026-09-29-area08-s11.md
topics/2026/2026-09-29-area08-s3.md
topics/2026/2026-09-29-area08-s4.md
topics/2026/2026-09-29-area08-s6.md
topics/2026/2026-09-29-area08-s7.md
topics/2026/2026-09-29-area08-s8.md
topics/2026/2026-09-29-area09-s10.md
topics/2026/2026-09-29-area09-s11.md
topics/2026/2026-09-29-area09-s3.md
topics/2026/2026-09-29-area09-s4.md
topics/2026/2026-09-29-area09-s6.md
topics/2026/2026-09-29-area09-s7.md
topics/2026/2026-09-29-area09-s8.md
topics/2026/2026-09-29-area10-s10.md
topics/2026/2026-09-29-area10-s11.md
topics/2026/2026-09-29-area10-s3.md
topics/2026/2026-09-29-area10-s4.md
topics/2026/2026-09-29-area10-s6.md
topics/2026/2026-09-29-area10-s7.md
topics/2026/2026-09-29-area10-s8.md
topics/2026/2026-09-29-area11-s10.md
topics/2026/2026-09-29-area11-s11.md
topics/2026/2026-09-29-area11-s3.md
topics/2026/2026-09-29-area11-s4.md
topics/2026/2026-09-29-area11-s6.md
topics/2026/2026-09-29-area11-s7.md
topics/2026/2026-09-29-area11-s8.md
topics/2026/2026-09-29-area12-s10.md
topics/2026/2026-09-29-area12-s11.md
topics/2026/2026-09-29-area12-s3.md
topics/2026/2026-09-29-area12-s4.md
topics/2026/2026-09-29-area12-s6.md
topics/2026/2026-09-29-area12-s7.md
topics/2026/2026-09-29-area12-s8.md
topics/2026/2026-09-29-area13-s10.md
topics/2026/2026-09-29-area13-s11.md
topics/2026/2026-09-29-area13-s3.md
topics/2026/2026-09-29-area13-s4.md
topics/2026/2026-09-29-area13-s6.md
topics/2026/2026-09-29-area13-s7.md
topics/2026/2026-09-29-area13-s8.md
topics/2026/2026-09-29-area61-s10.md
topics/2026/2026-09-29-area61-s11.md
topics/2026/2026-09-29-area61-s3.md
topics/2026/2026-09-29-area61-s4.md
topics/2026/2026-09-29-area61-s6.md
topics/2026/2026-09-29-area61-s7.md
topics/2026/2026-09-29-area61-s8.md
topics/2026/2026-09-29-area62-s10.md
topics/2026/2026-09-29-area62-s11.md
topics/2026/2026-09-29-area62-s3.md
topics/2026/2026-09-29-area62-s4.md
topics/2026/2026-09-29-area62-s6.md
topics/2026/2026-09-29-area62-s7.md
topics/2026/2026-09-29-area62-s8.md
topics/2026/2026-09-29-area63-s10.md
topics/2026/2026-09-29-area63-s11.md
topics/2026/2026-09-29-area63-s3.md
topics/2026/2026-09-29-area63-s4.md
topics/2026/2026-09-29-area63-s6.md
topics/2026/2026-09-29-area63-s7.md
topics/2026/2026-09-29-area63-s8.md
topics/2026/2026-09-29-area64-s10.md
topics/2026/2026-09-29-area64-s11.md
topics/2026/2026-09-29-area64-s3.md
topics/2026/2026-09-29-area64-s4.md
topics/2026/2026-09-29-area64-s6.md
topics/2026/2026-09-29-area64-s7.md
topics/2026/2026-09-29-area64-s8.md
topics/2026/2026-09-29-area65-s10.md
topics/2026/2026-09-29-area65-s11.md
topics/2026/2026-09-29-area65-s3.md
topics/2026/2026-09-29-area65-s4.md
topics/2026/2026-09-29-area65-s6.md
topics/2026/2026-09-29-area65-s7.md
topics/2026/2026-09-29-area65-s8.md
topics/2026/2026-09-30-area02-s10.md
topics/2026/2026-09-30-area02-s11.md
topics/2026/2026-09-30-area02-s3.md
topics/2026/2026-09-30-area02-s4.md
topics/2026/2026-09-30-area02-s6.md
topics/2026/2026-09-30-area02-s7.md
topics/2026/2026-09-30-area02-s8.md
topics/2026/2026-09-30-area03-s10.md
topics/2026/2026-09-30-area03-s11.md
topics/2026/2026-09-30-area03-s3.md
topics/2026/2026-09-30-area03-s4.md
topics/2026/2026-09-30-area03-s6.md
topics/2026/2026-09-30-area03-s7.md
topics/2026/2026-09-30-area03-s8.md
topics/2026/2026-09-30-area14-s10.md
topics/2026/2026-09-30-area14-s11.md
topics/2026/2026-09-30-area14-s3.md
topics/2026/2026-09-30-area14-s4.md
topics/2026/2026-09-30-area14-s6.md
topics/2026/2026-09-30-area14-s8.md
topics/2026/2026-09-30-area16-s10.md
topics/2026/2026-09-30-area16-s11.md
topics/2026/2026-09-30-area16-s4.md
topics/2026/2026-09-30-area16-s6.md
topics/2026/2026-09-30-area16-s7.md
topics/2026/2026-09-30-area16-s8.md
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
topics/2026/2026-09-30-area36-s10.md
topics/2026/2026-09-30-area36-s11.md
topics/2026/2026-09-30-area36-s3.md
topics/2026/2026-09-30-area36-s4.md
topics/2026/2026-09-30-area36-s6.md
topics/2026/2026-09-30-area36-s7.md
topics/2026/2026-09-30-area36-s8.md
topics/2026/2026-09-30-area37-s10.md
topics/2026/2026-09-30-area37-s4.md
topics/2026/2026-09-30-area37-s6.md
topics/2026/2026-09-30-area37-s8.md
topics/2026/2026-09-30-area40-s10.md
topics/2026/2026-09-30-area40-s11.md
topics/2026/2026-09-30-area40-s3.md
topics/2026/2026-09-30-area40-s4.md
topics/2026/2026-09-30-area40-s6.md
topics/2026/2026-09-30-area40-s7.md
topics/2026/2026-09-30-area40-s8.md
topics/2026/2026-09-30-area41-s10.md
topics/2026/2026-09-30-area41-s11.md
topics/2026/2026-09-30-area41-s3.md
topics/2026/2026-09-30-area41-s4.md
topics/2026/2026-09-30-area41-s6.md
topics/2026/2026-09-30-area41-s7.md
topics/2026/2026-09-30-area41-s8.md
topics/2026/2026-09-30-area43-s10.md
topics/2026/2026-09-30-area43-s11.md
topics/2026/2026-09-30-area43-s3.md
topics/2026/2026-09-30-area43-s4.md
topics/2026/2026-09-30-area43-s6.md
topics/2026/2026-09-30-area43-s7.md
topics/2026/2026-09-30-area44-s10.md
topics/2026/2026-09-30-area44-s11.md
topics/2026/2026-09-30-area44-s3.md
topics/2026/2026-09-30-area44-s4.md
topics/2026/2026-09-30-area44-s6.md
topics/2026/2026-09-30-area44-s7.md
topics/2026/2026-09-30-area44-s8.md
topics/2026/2026-09-30-area45-s10.md
topics/2026/2026-09-30-area45-s11.md
topics/2026/2026-09-30-area45-s3.md
topics/2026/2026-09-30-area45-s4.md
topics/2026/2026-09-30-area45-s6.md
topics/2026/2026-09-30-area45-s7.md
topics/2026/2026-09-30-area45-s8.md
topics/2026/2026-09-30-area46-s10.md
topics/2026/2026-09-30-area46-s11.md
topics/2026/2026-09-30-area46-s3.md
topics/2026/2026-09-30-area46-s4.md
topics/2026/2026-09-30-area46-s6.md
topics/2026/2026-09-30-area46-s7.md
topics/2026/2026-09-30-area46-s8.md
topics/2026/2026-09-30-area49-s10.md
topics/2026/2026-09-30-area49-s11.md
topics/2026/2026-09-30-area49-s3.md
topics/2026/2026-09-30-area49-s4.md
topics/2026/2026-09-30-area49-s6.md
topics/2026/2026-09-30-area49-s7.md
topics/2026/2026-09-30-area49-s8.md
topics/2026/2026-09-30-area50-s10.md
topics/2026/2026-09-30-area50-s11.md
topics/2026/2026-09-30-area50-s3.md
topics/2026/2026-09-30-area50-s4.md
topics/2026/2026-09-30-area50-s6.md
topics/2026/2026-09-30-area50-s7.md
topics/2026/2026-09-30-area50-s8.md
topics/2026/2026-09-30-area52-s10.md
topics/2026/2026-09-30-area52-s11.md
topics/2026/2026-09-30-area52-s3.md
topics/2026/2026-09-30-area52-s4.md
topics/2026/2026-09-30-area52-s6.md
topics/2026/2026-09-30-area52-s8.md
topics/2026/2026-09-30-area53-s10.md
topics/2026/2026-09-30-area53-s11.md
topics/2026/2026-09-30-area53-s3.md
topics/2026/2026-09-30-area53-s4.md
topics/2026/2026-09-30-area53-s6.md
topics/2026/2026-09-30-area53-s7.md
topics/2026/2026-09-30-area53-s8.md
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
topics/2026/2026-09-30-area67-s10.md
topics/2026/2026-09-30-area67-s11.md
topics/2026/2026-09-30-area67-s3.md
topics/2026/2026-09-30-area67-s4.md
topics/2026/2026-09-30-area67-s6.md
topics/2026/2026-09-30-area67-s7.md
topics/2026/2026-09-30-area67-s8.md
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

### runs/2026-10-09-04/pages.json

```json
{
  "run_id": "2026-10-09-04",
  "outline": [
    {
      "path": "docs/categories/design-and-simulation/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 9500,
      "summary": "I. 설계·시뮬레이션의 네 세부영역은 F. 연동(Open-RMF 시뮬레이션의 문·승강기·slotcar 플러그인), G. 계획·최적화(충전·배정·경로망의 시뮬레이션 평가), O. 검증·도입·수명주기(배치 전 시뮬레이션의 이점과 시뮬레이션–현실 상관) 등 다른 대분류와 이어지며, 연결 해석 대부분은 단일 출처에 기댄 추정이다. [사실][^ref-406]",
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
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30",
        "f31",
        "f32",
        "f33",
        "f34",
        "f35",
        "f36",
        "f37",
        "f38",
        "f39",
        "f40",
        "f41",
        "f42",
        "f43",
        "f44",
        "f45",
        "f46",
        "f47",
        "f48",
        "f49"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/index.md",
      "section": "참고 자료",
      "budget_chars": 120,
      "summary": "템플릿의 번호 없는 '참고 자료' 절. 이 대분류의 핵심 포인트 원문에는 [n] 표기가 없어 원문 각주가 없고, 연결 절의 각주 정의는 그 절 끝에 둔다는 안내만 둔다."
    }
  ],
  "pages": [
    {
      "path": "docs/categories/design-and-simulation/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 신규 작성: 대분류 16곳과의 연결(근거 각주 46건), 아직 다루지 않은 세부영역 23곳 명시, 1차 조건부 승인 수정 16건 반영. 형식 검증 재작성: 템플릿의 마지막 절 '참고 자료'를 추가",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-079",
              "ref-098",
              "ref-101",
              "ref-102",
              "ref-103",
              "ref-104",
              "ref-105",
              "ref-106",
              "ref-109",
              "ref-116",
              "ref-267",
              "ref-291",
              "ref-381",
              "ref-398",
              "ref-406",
              "ref-409",
              "ref-516",
              "ref-518",
              "ref-521",
              "ref-526",
              "ref-527",
              "ref-528",
              "ref-741",
              "ref-815",
              "ref-831",
              "ref-832",
              "ref-833",
              "ref-943",
              "ref-971",
              "ref-1086",
              "ref-1088",
              "ref-1089",
              "ref-1090",
              "ref-1091",
              "ref-1092",
              "ref-1126",
              "ref-1127",
              "ref-1128",
              "ref-1129",
              "ref-1130",
              "ref-1131",
              "ref-1133",
              "ref-1165",
              "ref-1239",
              "ref-1331",
              "ref-1332"
            ]
          },
          "content": "이 절은 게시된 [33. 시나리오 모델·편집](scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](capacity-sizing-and-layout-design.md), [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) 페이지와 2026-10-09 대분류 연결 조사의 검증된 주장을 근거로, I. 설계·시뮬레이션이 다른 대분류와 어디서 이어지는지 정리한다. 근거는 대부분 단일 출처이거나 로봇 플릿이 아닌 대상(자율주행·제약 공정·연구용 주행 로봇)에서 나왔으므로, 영역 사이의 연결 해석은 추정 태그로 표시했다. 분류 원문 19장의 외부 연계 영역은 문장 안에 '연계 대상'으로 밝혔다.\n\n- [A. 기획·사업](../planning-and-business/index.md) — 1. 기술·시장·업체 동향, 3. 경제성·조달·사업 모델\n    - 36. 가상 시운전·실제 상황 재현 ↔ 3. 경제성·조달·사업 모델: Rockwell Automation 사례 소개(2024-08-28)는 미국 남부 물류센터 구축에서 통합자가 컨베이어·피킹 모듈 제어(설비 업체·통합자 쪽 연계 대상)를 설치 전에 에뮬레이션으로 검증해 전체 프로젝트 기간을 18% 줄이고 현장 시운전을 5주 단축했다고 밝히지만, 기준선과 측정 방법은 공개하지 않았고 독립 연구가 같은 기준선으로 측정한 결과는 미확인이다(oq-257). [추정] 벤더 주장[^ref-1165]\n    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ 1. 기술·시장·업체 동향: NVIDIA 는 2025-01-06 산업용 로봇 플릿 디지털 트윈을 만드는 'Mega' Omniverse 블루프린트를 발표하며 센서 시뮬레이션·합성 데이터(시뮬레이터 제공자 쪽 연계 대상) 기반의 배치 전 플릿 검증을 내세웠다. [추정] 벤더 주장[^ref-527]\n- [B. 로봇 온톨로지](../robot-ontology/index.md) — 4. 이기종 로봇 등록, 7. 온톨로지 검증·변경 관리\n    - 4. 이기종 로봇 등록 ↔ 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: 시나리오가 참조하는 로봇 모델은 SDFormat 같은 로봇·환경 기술 형식으로 시뮬레이터에 들어가므로, 4. 이기종 로봇 등록의 기종 제원 기술(형상·질량·센서 등)이 시뮬레이션 자산의 원천으로 이어질 것으로 보인다(로봇 기구학·센서 모델 자체는 연계 대상이며, 등록 정보와 시뮬레이션 모델을 잇는 사례는 미확인). [추정][^ref-1092]\n    - 7. 온톨로지 검증·변경 관리 ↔ 36. 가상 시운전·실제 상황 재현: 7. 온톨로지 검증·변경 관리가 능력 정의에 붙이는 지원 단계(시뮬레이션 연결·시뮬레이션 검증·실기 검증)를 판정할 때 36. 가상 시운전·실제 상황 재현의 시뮬레이션 신뢰도 평가와 시뮬레이션–현실 상관 지표가 기준이 될 수 있으나, 두 체계를 대응시킨 자료는 확인하지 못했다(oq-156). [추정][^ref-1133][^ref-1127]\n- [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md) — [9. 채팅으로 시나리오 구성](../chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md). 분류 원문의 교차 규칙에서 이 대화 기능들이 부르는 엔진은 33. 시나리오 모델·편집과 36. 가상 시운전·실제 상황 재현이다.\n    - 9. 채팅으로 시나리오 구성 ↔ 33. 시나리오 모델·편집: Chat2Scenic(2026-07-15 공개)은 챗봇 인터페이스로 시나리오를 대화로 다듬으면서 검색 증강 방식으로 도메인 특화 언어(Domain-Specific Language, DSL) 시나리오 스크립트를 만들고, 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%(비교 방법 30.08%·16.26%)를 보고했다(대상은 자율주행 시나리오이며 로봇 현장이 아니다). [사실][^ref-833]\n    - 9. 채팅으로 시나리오 구성·13. 대화형 기능의 신뢰·기반 ↔ 33. 시나리오 모델·편집: 위 결과에서도 생성 스크립트의 약 4분의 1은 컴파일에 실패했으므로, 대화로 만든 시나리오를 33. 시나리오 모델·편집이 정하는 매개변수화·장애 선언 형식으로 받아 승인 전에 형식을 검사하는 일이 두 대분류의 인계 지점이 될 것으로 보인다(로봇 시나리오에 적용한 사례는 미확인). [추정][^ref-833][^ref-1088][^ref-528]\n    - 11. 채팅으로 실제 상황 시뮬레이션 재현 ↔ 34. 시뮬레이션·예측용 디지털 트윈: Xia 외(2026-08-22 공개, ETFA 2026 채택)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다(로봇 플릿 대상이 아니다). [사실][^ref-832]\n    - 11. 채팅으로 실제 상황 시뮬레이션 재현 ↔ 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 대화로 조건을 바꿔 비교하는 일은 언어 모델이 34. 시뮬레이션·예측용 디지털 트윈의 실험을 설계·실행하는 구조로 이어질 것으로 보이나, 비교 결과를 믿으려면 36. 가상 시운전·실제 상황 재현의 재현 충실도 지표가 함께 필요하고 로봇 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-832][^ref-1127]\n- [D. 공간·지도 모델](../space-and-map-model/index.md) — 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리\n    - 14·15·16 영역(지도) ↔ 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 의 building_map_generator 는 traffic-editor 로 주석한 건물 파일에서 층별 바닥·벽 메시와 문·승강기·로봇을 담은 시뮬레이션 월드를 만들고, 환경을 바꿀 때는 주석만 고쳐 다시 생성하면 된다(발행일 미확인, 2026-10-09 확인). [사실][^ref-406][^ref-079] 언어 모델로 생성한 가상 환경과 실제 현장 지도의 구분은 아래 L. AI·학습 기술 항목에 둔다.\n- [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md) — 18. 실시간 세계 상태·데이터 일관성, 19. 사람·보행자 모델(가상 사람 흐름은 M. 안전의 49. 사람 근접 안전 시험과도 겹친다)\n    - 18. 실시간 세계 상태·데이터 일관성 ↔ 34. 시뮬레이션·예측용 디지털 트윈: 제조 분야 분류 자료(2018)가 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분하므로, 18. 실시간 세계 상태·데이터 일관성은 현장 상태를 가상 모델에 반영해 현재 상태를 표현하고 34. 시뮬레이션·예측용 디지털 트윈은 그 모델을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거가 제조 대상이라는 한계가 있다). [추정][^ref-291]\n    - 19. 사람·보행자 모델 ↔ 36. 가상 시운전·실제 상황 재현: Waymax(2023-10-12 공개)는 실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화하거나 재생하고, 사실적 상호작용을 위해 학습된 행동 모델과 규칙 기반 행동 모델을 제공한다(자율주행 차량 대상이며 로봇 현장 사례가 아니다). [사실][^ref-1128]\n    - 19. 사람·보행자 모델 ↔ 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 공항 터미널 예제 월드가 이를 군중 시뮬레이션으로 쓴다(두 출처는 같은 기관이라 독립 교차 확인은 아니다). [사실][^ref-406][^ref-104]\n- [F. 연동](../integration/index.md) — 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동\n    - 22. 설비·건물 시스템 연동 ↔ 34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션에서는 문·승강기 플러그인이 실제와 같은 문·승강기 요청에 응답하고, door_supervisor 가 문 충돌을 막고 lift_supervisor 가 여러 플릿의 승강기 요청을 관리하며, TeleportDispenser·TeleportIngestor 가 배송 작업의 적재·하역을 흉내 낸다(승강기·문 제어 자체는 시설·설비 제어 경계의 연계 대상이고, ROP 는 요청·상태 확인을 맡는다). [사실][^ref-406]\n    - 20. 로봇·제조사 관제 연동 ↔ 34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 의 slotcar 플러그인은 플릿 어댑터의 경로·모드 요청을 받아 로봇 상태를 발행하는 전체 제어 로봇 모델로, 경유점 사이를 레일식 직선으로 움직이고 막히면 멈추며 로봇마다 주행 스택 전체를 돌리는 계산 비용을 피한다(로컬 회피·센서 인식 같은 로봇 자체 주행 거동은 제조사 쪽 연계 대상이며, 단순화 모델의 예측 오차 보정은 oq-086 으로 열려 있다). [사실][^ref-406]\n    - 22. 설비·건물 시스템 연동 ↔ 35. 처리능력·규모·배치 설계: 다층 호텔(상업 시설)의 배송 로봇 경로 계획 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다(35. 처리능력·규모·배치 설계는 승강기 시간을 제약 입력으로만 받고 승강기 제어는 연계 대상이다). [사실][^ref-103]\n    - 21. 상호운용 표준·적합성 ↔ 34. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 들어와 있고 2026년 디지털 트윈 결합을 다루는 제6부가 발행되었으나, 물류센터 이종 로봇·설비에 그대로 쓸 수 있는지는 확인되지 않았다(oq-085). [사실][^ref-516][^ref-518]\n    - 연계 대상: 성수기 주문·물동량 전망 같은 34. 시뮬레이션·예측용 디지털 트윈의 시나리오 입력은 23. 업무 시스템 연동 너머 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 물류·공급망 디지털 트윈 검토(2024)는 실제 데이터로 검증한 연구가 소수라고 보고한다. [추정][^ref-521]\n- [G. 계획·최적화](../planning-and-optimization/index.md) — 24. 작업·워크플로 모델링, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 27. 다중 로봇 경로·교통 관리 — MAPF, 28. 공용 자원·충전·에너지 최적화\n    - 28. 공용 자원·충전·에너지 최적화 ↔ 35. 처리능력·규모·배치 설계: 한 유통사 물류센터 시뮬레이션 연구(2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. [사실][^ref-102] 로봇 이동형 풀필먼트 시스템의 충전·배터리 교환 전략을 비교한 연구(2018)가 있다. [사실][^ref-098] 창고 충전소 배치를 최적화한 연구(2024)도 있다. [사실][^ref-109]\n    - 25. 작업 배정 — MRTA ↔ 35. 처리능력·규모·배치 설계: Open-RMF 플릿 어댑터 템플릿 설정에서 배터리가 recharge_threshold(예시값 0.10) 아래인 로봇은 작동하지 않는다(발행일 미확인, 2026-10-09 확인). [사실][^ref-105] 따라서 충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어질 것으로 보인다. [추정][^ref-105]\n    - 26. 작업 순서·스케줄링 ↔ 35. 처리능력·규모·배치 설계: 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정한 Boysen 외(2017)는 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다(저자 계산 실험 조건이며 독립 재현은 미확인: oq-050). [사실][^ref-381]\n    - 25. 작업 배정 — MRTA ↔ 34. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 로봇 이동형 풀필먼트 시스템의 여러 결정 문제를 연구하는 이산 사건 시뮬레이션이며, Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다(물류창고 피킹 단계의 시뮬레이션 결과이며 현장 실측이 아니다). [사실][^ref-101][^ref-398]\n    - 25. 작업 배정 — MRTA ↔ 36. 가상 시운전·실제 상황 재현: VirTooS(2026-08-26 공개)는 ROS 2와 Unity 게임 엔진을 결합한 혼합 현실 환경에서 실제·가상 로봇과 실제·가상 센서를 함께 써서 자율이동로봇 팀의 플릿 관리 작업을 시험하는 도구이며, 작업 배정 예제에서 실제 로봇과 가상 로봇이 상호작용한다. [사실][^ref-1129]\n    - 27. 다중 로봇 경로·교통 관리 — MAPF ↔ 34. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다. [사실][^ref-267] 그래서 경로망 배치 평가는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽에 걸치는 것으로 보인다. [추정][^ref-267]\n    - 27. 다중 로봇 경로·교통 관리 — MAPF ↔ 33. 시나리오 모델·편집: Moving AI Lab 의 MAPF 벤치마크는 지도마다 시나리오 파일을 묶어 공개한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1091] 이 묶음은 경로 계획기를 같은 조건에서 비교하는 데 쓰일 수 있어, 경로 계획 평가가 33. 시나리오 모델·편집의 시나리오 형식·라이브러리와 맞닿는 것으로 보인다. [추정][^ref-1091]\n    - 24. 작업·워크플로 모델링 ↔ 33. 시나리오 모델·편집: 로봇 미션 명세·실행 형식 비교 연구와 행동 트리 편집기(Groot2)가 33. 시나리오 모델·편집의 미션 기술 형식·편집기 선택 근거로 쓰였으므로, 시나리오 안의 작업 표현은 24. 작업·워크플로 모델링의 단계·선후관계·완료 조건 표현과 같은 형식을 공유해야 할 것으로 보인다(두 영역의 형식을 하나로 맞춘 공개 사례는 미확인). [추정][^ref-116][^ref-1090]\n- [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md) — 32. 예외 복구·재계획·업무 연속성\n    - 32. 예외 복구·재계획·업무 연속성 ↔ 33. 시나리오 모델·편집: NIST 산업 자동화용 민첩 로봇 경진대회(ARIAC)는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급 주문을 매개변수로 선언해 시각이나 발생 횟수 조건으로 시나리오에 주입한다(제조 공장 경진대회 시나리오이며, 여러 제조사 플릿·승강기·문 장애로 일반화한 형식은 미확인: oq-235). [사실][^ref-528]\n- [J. 현장 운영·관제](../field-operations-and-monitoring/index.md) — 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선\n    - 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석 ↔ 36. 가상 시운전·실제 상황 재현: rosbag2 는 ROS 2 통신을 시각이 찍힌 백 파일(기본 MCAP)로 기록하고, 재생 속도 조절·/clock 발행·시작 시각 지정·토픽 선택·여러 백 파일의 기록 시각순 동시 재생을 지원한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-831]\n    - 37. 관제 화면·실행 기록 ↔ 36. 가상 시운전·실제 상황 재현: 메시지 단위 기록 도구와 기록 기반 시뮬레이터가 있으나, 재현의 원천은 37. 관제 화면·실행 기록이 남기는 오케스트레이션 수준 실행 기록(작업·배정·위치·사건 시각)이어야 할 것으로 보이며 이를 시나리오 사양으로 바꾸는 공개 형식은 확인하지 못했다(oq-131). [추정][^ref-831][^ref-1128]\n    - 39. 운영 성과 측정·개선 ↔ 35. 처리능력·규모·배치 설계: 충전 방식의 비용 비교와 국내 스마트물류센터 인증 평가에서 두 영역이 만나는 것으로 보이나, 인증 세부 지표에 로봇 대수·가동률 같은 설비 계획 지표가 들어가는지는 확인하지 못했다(oq-011). [추정][^ref-098][^ref-106]\n- [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md) — 42. 분산 시스템·통신·컴퓨팅 구조\n    - 42. 분산 시스템·통신·컴퓨팅 구조 ↔ 36. 가상 시운전·실제 상황 재현: 가상 시운전 도구가 여러 머신에 컨테이너로 배포되고 시뮬레이션 플러그인이 실제와 같은 요청 메시지에 응답하므로, 가상 대응물을 어느 계산 자원에 두고 실제 시스템과 어떤 통신으로 잇는지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다(로봇 플릿 플랫폼의 현장 서버·클라우드 배치 근거는 없다: oq-040). [추정][^ref-1129][^ref-406]\n- [L. AI·학습 기술](../ai-and-learning/index.md) — [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md). 적용 대상은 [33. 시나리오 모델·편집](scenario-model-and-editing.md)과 [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md)이다.\n    - 44. 로봇 기반 모델·언어 모델 계획 ↔ 33. 시나리오 모델·편집: Holodeck(2023-12-14 공개, CVPR 2024)은 GPT-4가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성하며, 생성 장면에서 학습한 에이전트가 처음 보는 환경에서 주행했다고 보고했다. [사실][^ref-815]\n    - 44. 로봇 기반 모델·언어 모델 계획 ↔ 33. 시나리오 모델·편집(D. 공간·지도 모델과의 구분): 언어 모델·생성 모델로 시뮬레이션 환경을 만드는 연구(Holodeck, Arena 4.0)가 33. 시나리오 모델·편집의 예제 라이브러리를 채우는 수단이 될 수 있으나, 생성 환경은 실제 현장 지도가 아니므로 D. 공간·지도 모델의 도면·현장 정합과 구분해야 할 것으로 보인다. [추정][^ref-815][^ref-1089]\n    - 47. AI·학습·적응과 모델 운영 ↔ 36. 가상 시운전·실제 상황 재현: 학습 정책이 시뮬레이터의 결함을 악용하는 현실 격차가 보고되므로, 학습 기반 정책의 현실 격차 보정은 47. AI·학습·적응과 모델 운영과 로봇 제조사·시뮬레이션 도구 쪽 일(연계 대상)이고 36. 가상 시운전·실제 상황 재현은 재현 결과와 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다. [추정][^ref-741][^ref-1127]\n- [M. 안전](../safety/index.md) — 48. 안전·위험 관리(49. 사람 근접 안전과의 연결은 E. 사물·사람·실시간 상태 항목의 군중 시뮬레이션 참조)\n    - 48. 안전·위험 관리 ↔ 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 생성해, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. [사실][^ref-1331]\n    - 48. 안전·위험 관리 ↔ 33. 시나리오 모델·편집: 위험 상황을 생성·탐색하는 시뮬레이션 시험(사람 행동 최적화, 확률적 시나리오 언어 기반 반증)이 있으므로, 33. 시나리오 모델·편집에서 선언한 장애·사람 흐름 시나리오가 48. 안전·위험 관리의 위험 식별 입력이 될 수 있을 것으로 보이나 다중 이동로봇 플릿에 적용한 사례는 확인하지 못했다(안전 인증·설비 안전 제어 판단 자체는 연계 대상). [추정][^ref-1331][^ref-1086]\n- [N. 보안·개인정보](../security-and-privacy/index.md) — 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사\n    - 52. 통신 보호·위협 관리·감사 ↔ 36. 가상 시운전·실제 상황 재현: Carr 외(2022)는 물리 로봇과 동기화된 ROS 기반 로봇의 디지털 트윈에 중간자 공격을 가하면 그 영향이 물리 시스템으로 전파될 수 있으며 산업용 로봇과 자율이동로봇 모두에 해당한다고 보고했다. [사실][^ref-1332]\n    - 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ 36. 가상 시운전·실제 상황 재현: 36. 가상 시운전·실제 상황 재현이 18. 실시간 세계 상태·데이터 일관성의 현재 상태를 34. 시뮬레이션·예측용 디지털 트윈의 실험으로 옮기고 그 결과를 되돌리는 동기화 경로는 공격 표면이 될 수 있으므로, 시뮬레이션 결과가 실제 계획·설정에 반영되는 경로에 접근통제와 무결성 확인이 필요할 것으로 보인다(로봇 플릿 플랫폼 사례는 미확인). [추정][^ref-1332]\n- [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md) — 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전\n    - 54. 시험·형식 검증·벤치마크·55. 현장 조사·설치·시운전 ↔ 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Open-RMF 문서는 시뮬레이션이 하드웨어 시험의 준비·정지·초기화 부담을 덜고, 시나리오를 반복해 수정을 확인하고 드문 예외를 살피며, 장시간 시뮬레이션으로 배치 전에 시설 소유자의 확신을 높인다고 설명한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-406]\n    - 55. 현장 조사·설치·시운전 ↔ 36. 가상 시운전·실제 상황 재현: 설비 제어 분야의 가상 시운전 정의(VDI/VDE 3693 Blatt 1, 2025-05)와 실제 제어기·가상화 인스턴스를 섞은 분산 가상 시운전 연구(2023)가 있어 36. 가상 시운전·실제 상황 재현의 결과가 55. 현장 조사·설치·시운전의 현장 시운전 준비로 넘어갈 것으로 보이나, PLC·설비 제어 코드의 가상 시운전 자체는 설비 업체·통합자 쪽 연계 대상이고 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차는 확인하지 못했다(oq-255). [추정][^ref-1126][^ref-1130][^ref-406]\n    - 54. 시험·형식 검증·벤치마크 ↔ 36. 가상 시운전·실제 상황 재현: Kadian 외(IEEE RA-L, 2020)는 시뮬레이션–현실 상관 계수(Sim-vs-Real Correlation Coefficient, SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 가 0.18 이었으나 시뮬레이션 매개변수를 조정해 0.844 로 높였다고 보고했다. [사실][^ref-1127]\n    - 54. 시험·형식 검증·벤치마크 ↔ 36. 가상 시운전·실제 상황 재현: NASA-STD-7009B(2024-03-05)는 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준이다. [사실][^ref-1133]\n- [P. 거버넌스·법규·사회](../governance-law-and-society/index.md) — 59. 법·규제·보험·라이선스\n    - 59. 법·규제·보험·라이선스 ↔ 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 모델 라이선스를 지정하고 CC BY 3.0 Unported 를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다(발행일 미확인, 2026-10-09 확인. 자산 단위 추적 표준은 미확인: oq-292). [사실][^ref-1239]\n- [Q. 현장 유형별 적용](../site-type-applications/index.md) — 61. 물류창고, 62. 제조 공장, 63. 병원·의료, 64. 상업 시설, 65. 가정·공동주택. 현장마다 다른 요구는 Q. 현장 유형별 적용에 모으고, 아래 근거는 이 대분류의 공통 기능이 각 현장에서 어떻게 쓰이는지를 보여 준다.\n    - 61. 물류창고 ↔ 34. 시뮬레이션·예측용 디지털 트윈: CJ대한통운은 2021-11 현실 물류센터와 같은 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획을 발표했고 작업 동선·재고 배치·설비 효율 최적화를 목표로 들었으나, 이후 적용 결과는 확인하지 못했다(oq-084, oq-117). [추정] 벤더 주장[^ref-526] 물류창고 조건의 계획 연구(충전기 시뮬레이션, 주문·랙 순서, RAWSim-O)는 위 G. 계획·최적화 항목에 있다.\n    - 62. 제조 공장 ↔ 36. 가상 시운전·실제 상황 재현: 최성욱·박상철·왕지남(2008)은 자동차 차체 생산라인의 PLC 코드 검증을 위해 실제 PLC 와 3D 가상 공정 시뮬레이터를 양방향 통신으로 잇는 가상 플랜트 구축 절차를 제안했다(PLC 코드 가상 시운전은 시설·설비 제어 경계의 연계 대상이며 ROP 에는 방법 근거로만 쓴다). [사실][^ref-1131]\n    - 63. 병원·의료 ↔ 35. 처리능력·규모·배치 설계·36. 가상 시운전·실제 상황 재현: 고려대학교 구로병원의 약품 배송 로봇 기록(2025-06, 122건)과 몬테카를로 재현에서 승강기 가동률 59.01% 이하일 때 배송 성공률은 95.5%였고, 90%를 넘으면 실패가 몰렸다(2026-03-31 발행. 승강기 제어 자체는 22. 설비·건물 시스템 연동 쪽 연계 대상). [사실][^ref-943]\n    - 63. 병원·의료 ↔ 36. 가상 시운전·실제 상황 재현: Lee 외 저자들은 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰고, 병원별 구조·통행·승강기 제어 정책을 재현한 병원 디지털 트윈으로 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다(다른 병원에서 검증한 연구는 미확인: oq-258). [의견][^ref-943]\n    - 64. 상업 시설 ↔ 33. 시나리오 모델·편집: Open-RMF 예제 호텔 월드는 로봇 플릿 3개(로봇 4대)·승강기 2대·여러 문을 담고, 공항 터미널 월드는 대형 지도에 선택적 군중 시뮬레이션과 읽기 전용 카트를 더해 순찰·배송·청소를 실행하는 시뮬레이션 예제다(실제 시설 도입 사례가 아니다). [사실][^ref-104]\n    - 65. 가정·공동주택 ↔ 35. 처리능력·규모·배치 설계: 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 국내 인증 모델(2023)은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야 28개 항목(총점 176점)으로 구성된다. [사실][^ref-409]\n    - 65. 가정·공동주택 ↔ 33. 시나리오 모델·편집: BEHAVIOR-1K(2024-03-14 공개)는 설문으로 고른 일상 가정 활동 1,000개를 BDDL 로 명세하고 장면 50개와 주석 객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크다(실제 가정 배치가 아니다). [사실][^ref-971]\n\n**아직 다루지 않은 연결:** 이번 조사의 근거가 다루지 않은 세부영역은 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 8. 채팅으로 맵 작성, 10. 채팅으로 로봇 구성, 12. 채팅으로 업무 지시·오케스트레이션, 17. 작업 대상·자산 식별과 인계 추적, 29. 명령·작업 실행의 신뢰성, 30. 로봇 간 협업·물리적 인계, 31. 사람–로봇 협업, 40. 운영 절차·요청 창구, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 50. 안전 표준·인증·사고 조사, 53. 개인정보·영상 데이터, 56. 운영 이관·확대·교육, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터, 60. 노동·수용성·접근성, 66. 실외, 67. 기타 현장이다. 이 영역들과의 연결은 다음 조사에서 근거를 찾아 보강한다.\n\n[^ref-1165]: Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation, 2024-08-28, https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html, 접근일 2026-10-09 (원문 미열람)\n[^ref-527]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 2025-01-06, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-10-09 (원문 미열람)\n[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1133]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-10-09 (원문 미열람)\n[^ref-1127]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-10-09\n[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. (TUM 외, arXiv; IROS 2026 채택), Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-10-09\n[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-10-09 (원문 미열람)\n[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-10-09\n[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N. 외 (University of Stuttgart·AstraZeneca, arXiv; ETFA 2026 채택), LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-10-09\n[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09\n[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-10-09\n[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-10-09 (원문 미열람)\n[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-10-09\n[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-10-09 (원문 미열람)\n[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-09 (원문 미열람)\n[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-10-09 (원문 미열람)\n[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-10-09 (원문 미열람)\n[^ref-521]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-10-09 (원문 미열람)\n[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-10-09 (원문 미열람)\n[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-10-09 (원문 미열람)\n[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-10-09 (원문 미열람)\n[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09\n[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-10-09 (원문 미열람)\n[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-10-09 (원문 미열람)\n[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-10-09 (원문 미열람)\n[^ref-1129]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-10-09\n[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-10-09 (원문 미열람)\n[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-10-09 (원문 미열람)\n[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-10-09 (원문 미열람)\n[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-09\n[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-10-09 (원문 미열람)\n[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12-14, https://arxiv.org/abs/2312.09067, 접근일 2026-10-09\n[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-10-09 (원문 미열람)\n[^ref-741]: Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10, https://arxiv.org/abs/2510.20808, 접근일 2026-10-09 (원문 미열람)\n[^ref-1331]: Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020), Simulation-based Testing for Early Safety-Validation of Robot Systems, 2020-11-20, https://arxiv.org/abs/2011.10294, 접근일 2026-10-09\n[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-10-09 (원문 미열람)\n[^ref-1332]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09\n[^ref-1126]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-10-09 (원문 미열람)\n[^ref-1130]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1239]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-10-09 (원문 미열람)\n[^ref-526]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-10-09 (원문 미열람)\n[^ref-1131]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-10-09 (원문 미열람)\n[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)\n[^ref-409]: 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105), 2023, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381, 접근일 2026-10-09 (원문 미열람)\n[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03-14, https://arxiv.org/abs/2403.09227, 접근일 2026-10-09 (원문 미열람)\n"
        },
        {
          "section": "참고 자료",
          "action": "replace",
          "content": "이 대분류의 핵심 포인트 원문 문단에는 참고문헌 번호 표기가 없어 원문 각주는 없다. '다른 대분류와의 연결' 절에서 쓴 각주의 정의는 그 절 끝에 있다.\n"
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | I. 설계·시뮬레이션 | '다른 대분류와의 연결' 절 신규 작성(대분류 16곳과의 연결, 각주 46건, 1차 조건부 승인 수정 16건 반영) | run 2026-10-09-04",
  "index_updates": {
    "home_recent": "2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 신규 작성(C. 채팅 기반 구성·운영, F. 연동, G. 계획·최적화, O. 검증·도입·수명주기 등 대분류 16곳, 아직 다루지 않은 세부영역 23곳 명시)",
    "category_recent": "2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 신규 작성(대분류 16곳과의 연결 근거 정리, 연결 해석은 추정으로 표시, 각주 46건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "slotcar",
      "term_ko": "슬롯카 모델",
      "term_en": "Slotcar (Open-RMF simulated robot plugin)",
      "definition": "Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이는 단순화 로봇 모델로, 로봇마다 주행 스택 전체를 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다.",
      "description": "막히면 멈추고 2륜 차동 구동과 정적 장애물 없는 경로를 가정한다. 로컬 회피·센서 인식 같은 로봇 자체 거동은 재현하지 않으므로 제조사 쪽 연계 대상으로 남는다.",
      "related_areas": [
        20,
        34
      ],
      "sources": [
        "ref-406"
      ]
    },
    {
      "action": "new",
      "slug": "mixed-reality-testing",
      "term_ko": "혼합 현실 시험",
      "term_en": "Mixed-Reality Testing",
      "definition": "실제 로봇·센서와 가상 로봇·센서를 한 환경에 함께 두고 플릿 관리 같은 기능을 시험하는 방식으로, 모든 로봇을 실물로 갖추기 전에 작업 배정 등을 검증할 수 있게 한다.",
      "description": "예: VirTooS 는 ROS 2와 Unity 를 결합해 실제·가상 로봇이 함께 참여하는 작업 배정 실험을 지원한다.",
      "related_areas": [
        36,
        25
      ],
      "sources": [
        "ref-1129"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-833",
      "org": "Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. (TUM 외, arXiv; IROS 2026 채택)",
      "title": "Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving",
      "published": "2026-07-15",
      "url": "https://arxiv.org/abs/2607.14387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "챗봇 인터페이스로 시나리오를 대화로 다듬고 검색 증강 방식으로 DSL 시나리오 스크립트를 생성하는 틀. 123개 규제 기반 시나리오에서 컴파일 성공률 76.42%를 보고했다(초록 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-832",
      "org": "Xia, Y., Weyrich, M., Jazdi, N. 외 (University of Stuttgart·AstraZeneca, arXiv; ETFA 2026 채택)",
      "title": "LLM Agents Perform Controlled Experiments Using Simulation Models",
      "published": "2026-08-22",
      "url": "https://arxiv.org/abs/2608.23622",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "언어 모델 에이전트가 사용자 질의와 기준 구성으로 비교 시뮬레이션을 설계·실행·해석해 제약 공정 매개변수를 권고하는 다중 에이전트 틀(초록 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
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
      "accessed": "2026-10-09",
      "summary": "Open-RMF 시뮬레이션의 이점, slotcar 로봇 모델, 문·승강기 플러그인과 감독 노드, 워크셀 순간이동 플러그인, crowdsim, building_map_generator 로 월드 생성을 설명한다. mdBook 원본을 열어 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "시뮬레이션–현실 상관 계수(SRCC)를 제안하고 LoCoBot 주행에서 CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 0.18 을 시뮬레이션 매개변수 조정으로 0.844 로 높였다(초록 확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "차선·경유점·문·승강기·충전기를 지도에 주석하는 편집기. 입력의 원문 텍스트(data/source_texts)로 충전기·문·승강기 주석을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "플릿 어댑터 템플릿 설정(recharge_threshold, recharge_soc, 충전기, 작업 종료 후 동작 등). 입력의 원문 텍스트(data/source_texts)로 recharge_threshold 0.10 아래에서는 로봇이 작동하지 않는다는 설명을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "ARIAC 의 장애·긴급 주문 과제를 매개변수로 선언해 시각·발생 횟수 조건으로 주입하는 방식. 입력의 원문 텍스트(data/source_texts)로 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "원문 미열람. 병원 약품 배송 로봇 실제 기록과 몬테카를로 시뮬레이션으로 승강기 가동률과 배송 실패의 관계를 분석했다(이번 실행에서는 다시 열지 않음). ref-060 과 같은 논문이다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "원문 미열람. 다중 에이전트 경로 찾기 벤치마크 지도와 지도별 시나리오 파일 모음(1차 검증 중 지도·시나리오 파일 제공을 확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "summary": "원문 미열람. Gazebo 모델 데이터베이스의 구조와 database.config·model.config 의 라이선스·작성자 표기 규칙(1차 검증 중 license 요소·CC BY 3.0 권장·작성자 필수를 확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-527",
      "org": "NVIDIA",
      "title": "NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins",
      "published": "2025-01-06",
      "url": "https://blogs.nvidia.com/blog/mega-omniverse-blueprint",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 로봇 플릿 디지털 트윈 블루프린트 발표(벤더 주장). 발행일 2025-01-06 은 1차 검증 중 확인했다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
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
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가?",
      "areas": [
        9,
        33,
        13
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해, 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가?",
      "areas": [
        36,
        52,
        51
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가?",
      "areas": [
        48,
        34,
        19
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [],
  "additional_research_requests": [
    "다른 대분류와의 연결 절의 '아직 다루지 않은 연결'에 적은 세부영역(예: 2. 사용 사례·요구·책임 범위, 29. 명령·작업 실행의 신뢰성, 41. 플랫폼 아키텍처·외부 API, 53. 개인정보·영상 데이터, 66. 실외, 67. 기타 현장)과 I. 설계·시뮬레이션의 연결 근거 — 이번 브리프에 finding 이 없어 절 보강을 미뤘다",
    "34. 시뮬레이션·예측용 디지털 트윈과 35. 처리능력·규모·배치 설계 페이지(이전 분류 기준)의 10. 다른 연구영역과의 연결 절에 C. 채팅 기반 구성·운영, L. AI·학습 기술, M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회 연결(Xia 외, Holodeck, Huck 외, Carr 외, Gazebo 모델 라이선스 근거)을 반영할 갱신 실행 — 대분류 연결 실행은 대분류 절만 고친다",
    "참고문헌 정리 요청: ref-943(PMC 링크)과 ref-060(doi 링크)이 같은 Lee 외 Digital Health 논문으로 이중 등록되어 있다 — 이번 절은 ref-943 하나로만 인용했다",
    "벤더 주장 확인: Rockwell Automation 물류센터 에뮬레이션 사례(프로젝트 기간 18%·현장 시운전 5주 단축), NVIDIA Mega 블루프린트, CJ대한통운 디지털 트윈 계획의 독립 출처 확인 또는 이후 적용 결과",
    "pipeline 담당 확인 요청: 시드 대분류 페이지(I. 설계·시뮬레이션 등)에 템플릿의 마지막 절 '참고 자료'가 없어 형식 검증이 실패했다. 이번 재작성은 '참고 자료' 절 patch(replace)를 보냈으므로, 없는 절에 대한 patch 를 페이지 끝에 새 절로 추가하는지 확인하고, 다른 시드 대분류 페이지에도 이 절을 미리 넣을지 정해 달라"
  ],
  "fixes_applied": [
    "f1·f2·ref-1329 — Chat2Scenic 문장 두 개의 각주를 ref-833 으로 썼고 reference_updates 에 ref-1329 를 넣지 않았다(ref-833 을 cited_by 갱신용으로 넣음).",
    "f3·f4·ref-1330 — Xia 외 문장 두 개의 각주를 ref-832 로 썼고 ref-1330 을 등록하지 않았다.",
    "f15 — G. 계획·최적화 항목에서 'recharge_threshold(예시값 0.10) 아래인 로봇은 작동하지 않는다'를 [사실][^ref-105] 문장으로, '충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어질 것으로 보인다'를 별도 [추정] 문장으로 나눴다.",
    "f18 — '경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다'를 [사실][^ref-267], '가정한 미래를 실험하는 쪽에 걸친다'를 별도 [추정] 문장으로 나눴다.",
    "f19 — 'MAPF 벤치마크는 지도마다 시나리오 파일을 묶어 공개한다'만 [사실][^ref-1091]로, 같은 조건 비교와 시나리오 형식·라이브러리와 맞닿는다는 부분은 별도 [추정] 문장으로 강등했다.",
    "f2 — C. 채팅 기반 구성·운영 항목에서 '생성 스크립트의 약 4분의 1은 컴파일에 실패했으므로'로 써서 '실행 불가' 표현을 쓰지 않았다.",
    "f31 — O. 검증·도입·수명주기 항목에 'CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 가 0.18'로 썼다.",
    "f44·f48·f49 — 세 문장 모두 '[추정] 벤더 주장' 을 병기했고, ref-527 각주와 reference_updates 의 발행일을 2025-01-06 으로 고쳤다(본문에도 2025-01-06 발표로 기준일 명시).",
    "각주 원문 미열람 표기 — 지시 목록의 33개 출처 각주 정의 끝에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-079·ref-105·ref-528 은 표기하지 않고 source_unopened: false 와 원문 텍스트 확인 요약으로 고쳤다.",
    "범위 경계 문구 — f8·f20·f21·f42 쪽 승강기·문 제어(f8·f20·f21 문장 안에 '연계 대상' 명시, f42 는 인증 모델 사실만 서술해 제어를 다루지 않음), f11·f44·f45 의 PLC·컨베이어 제어 가상 시운전, f9·f32·f48 의 로봇 자체 주행·현실 격차 보정·센서 시뮬레이션, f36 의 안전 인증·설비 안전 제어를 각 문장 괄호에 '연계 대상'으로 밝혔고, f41 은 '연계 대상:'으로 시작하는 문장으로 두었다.",
    "18·34 구분 — E. 사물·사람·실시간 상태 항목에서 f7 로 '18. 실시간 세계 상태·데이터 일관성은 현재 상태 표현, 34. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험'을 밝혔고, N. 보안·개인정보 항목의 디지털 트윈 동기화는 36. 가상 시운전·실제 상황 재현이 18의 현재 상태를 34의 실험으로 옮기고 결과를 되돌리는 경로로만 서술했다.",
    "f14 — 세 출처를 세 문장으로 나눠 ref-102(충전기 부족·과잉), ref-098(충전·배터리 교환 전략 비교), ref-109(충전소 배치 최적화) 각주를 따로 붙였다.",
    "f20·f22 — 병원 문장 두 개를 ref-943 하나로만 인용했고 ref-060 을 쓰지 않았다.",
    "'아직 다루지 않은 연결' — 지시한 22개 세부영역(5·6·8·10·12·17·29·30·31·40·41·43·45·46·50·53·56·57·58·60·66·67)을 번호와 이름으로 적었고, 브리프 finding 이 다루지 않은 2. 사용 사례·요구·책임 범위도 함께 적어 실제 미연결 영역과 맞췄다. 완전성 표현은 쓰지 않았다.",
    "새 분류 명칭 — 다른 대분류는 17개 대분류 기준 문자+이름(예: 'F. 연동', 'O. 검증·도입·수명주기'), 세부영역은 번호+이름(예: '25. 작업 배정 — MRTA')으로 썼고 옛 대분류 이름을 옮기지 않았다.",
    "L. AI·학습 기술 연결 — L 항목 머리에 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영 링크와 적용 대상 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현 링크를 함께 두고 f5·f6·f32 를 그 아래에 썼다."
  ]
}
```


## 형식 검증 오류 (재작성)

직전 원고(runs/<run_id>/pages.json, pages/)가 코드 형식 검증(pipeline/validate_run.py)을 통과하지 못했다. 내용(주장·태그·각주·판정)은 바꾸지 말고 아래 형식 오류만 고친 전체 pages.json 을 다시 반환한다. 차등 갱신 실행이면 patches 로, 아니면 content 로 보낸다.

- docs/categories/design-and-simulation/index.md: 패치 대상 절을 찾지 못했다: '참고 자료'
- docs/categories/design-and-simulation/index.md: pages/ 에 파일이 없다
