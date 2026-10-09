(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-07
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
- verification_stage: second
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-10-09-07/target.json

```json
{
  "run_id": "2026-10-09-07",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 140,
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

### runs/2026-10-09-07/research.json

```json
{
  "run_id": "2026-10-09-07",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "I. 설계·시뮬레이션"
  },
  "gaps": [
    "I. 설계·시뮬레이션 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다(같은 대상의 실행 2026-10-09-04 는 형식 검증 실패로 보류되어 반영되지 않았다)",
    "보류 실행 2026-10-09-04 의 1차 검증(조건부 승인)이 낸 수정 지시가 아직 이행되지 않았다: ref-1329·ref-1330 대신 기존 ref-833·ref-832 재사용, f15·f18·f19 사실·추정 분리, SRCC 표현 정정, ref-527 발행일 정정, ref-943 단독 인용",
    "보류 실행에서 '아직 다루지 않은 연결'로 남았던 H. 실행·협업·예외 복구의 29·30·31, K. 플랫폼 아키텍처·인프라의 41·43, N. 보안·개인정보의 53, P. 거버넌스·법규·사회의 58·60, L. AI·학습 기술의 45·46, M. 안전의 50, O. 검증·도입·수명주기의 57, C. 채팅 기반 구성·운영의 12, Q. 현장 유형별 적용의 66·67 연결 근거가 없었다",
    "34. 시뮬레이션·예측용 디지털 트윈과 35. 처리능력·규모·배치 설계 페이지는 이전 분류(2026-09-25) 기준이라 C·L·M·N·P 대분류와 잇는 근거가 페이지 안에 없다",
    "한국 현장의 가상 시운전·디지털 트윈 사전 검증 자료가 계획·MOU 기사 위주다"
  ],
  "research_questions": [
    "현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]",
    "I. 설계·시뮬레이션의 네 세부영역은 C. 채팅 기반 구성·운영(9. 채팅으로 시나리오 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현, 12. 채팅으로 업무 지시·오케스트레이션)과 L. AI·학습 기술(44~47)에서 무엇을 받고 무엇을 넘기는가?",
    "34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현은 F. 연동(20~23)의 어떤 인터페이스를 가상으로 대신해 시험하며, B. 로봇 온톨로지(4·7)와 O. 검증·도입·수명주기(54·55·57)로 무엇을 넘기는가?",
    "35. 처리능력·규모·배치 설계와 34. 시뮬레이션·예측용 디지털 트윈의 결과는 G. 계획·최적화(24~28)와 H. 실행·협업·예외 복구(29~32, 특히 31. 사람–로봇 협업)의 결정과 어떻게 맞물리는가? (oq-009, oq-129 관련)",
    "36. 가상 시운전·실제 상황 재현은 E. 사물·사람·실시간 상태(17~19)·J. 현장 운영·관제(37~39)·K. 플랫폼 아키텍처·인프라(41~43)의 상태·기록·API 를 어떻게 원천으로 쓰며, 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 34. 시뮬레이션·예측용 디지털 트윈의 미래 실험을 어떻게 구분하는가? (oq-131 관련)",
    "시뮬레이션·디지털 트윈은 M. 안전(48·50), N. 보안·개인정보(51~53), P. 거버넌스·법규·사회(58~60), A. 기획·사업, Q. 현장 유형별 적용(61~67)과 어디서 만나는가(한국 자료 포함)? (oq-255, oq-292 관련)",
    "보류 실행 2026-10-09-04 의 1차 검증 수정 지시를 이행하고, 그 실행의 '아직 다루지 않은 연결'을 얼마나 줄일 수 있는가?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: Howard(Cal Poly 석사논문, 2026-06)는 처리량 최대화 기준의 AMR 대수 산정이 서비스형 로봇(RaaS) 구독 과금에서 플릿을 과대 산정한다고 보고, 대수 산정을 주문 라인당 비용 최소화 문제로 바꿔 이산 사건 시뮬레이션 27,000회로 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-822"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "피킹 구역제 창고, FlexSim 완전요인 DES 27,000회. 라인당 비용 곡선은 AMR:작업자 비율에 대해 U자형이며 최적 비율은 저수요 1에서 고수요 2.5로 이동. 석사논문(지도교수 Awwad), 저자 보고값.",
      "as_of": "2026-06",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f2",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: Rockwell Automation 사례 소개는 미국 남부 물류센터 구축에서 통합자가 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증해 전체 프로젝트 기간을 18% 줄이고 현장 시운전을 5주 단축했다고 밝히지만 기준선과 측정 방법은 공개하지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 18%·5주 수치는 기준선 미공개. 컨베이어·PLC 제어 코드 에뮬레이션은 설비 업체·통합자 쪽 연계 대상. (재인용: 36. 가상 시운전·실제 상황 재현 페이지 5절)",
      "as_of": "2024-08-28",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f3",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: NVIDIA 는 2025-01-06 산업용 로봇 플릿 디지털 트윈을 만드는 'Mega' Omniverse 블루프린트를 발표하며 센서 시뮬레이션·합성 데이터로 배치 전에 로봇 플릿을 시험·최적화할 수 있다고 내세운다.",
      "tag": "추정",
      "source_ids": [
        "ref-527"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 실제 시설 배치 전 디지털 트윈에서 로봇 플릿과 피지컬 AI 를 시험·최적화, 고충실도 센서 시뮬레이션·합성 데이터 사용(블로그 2025-01-06 확인). 센서 시뮬레이션은 시뮬레이터 제공자 쪽 연계 대상.",
      "as_of": "2025-01-06",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f4",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 시나리오가 참조하는 로봇 모델은 SDFormat 같은 로봇·환경 기술 형식으로 시뮬레이터에 들어가므로, 기종 제원 기술(형상·질량·센서)이 시뮬레이션 자산의 원천으로 이어질 것으로 보이나 등록 정보와 시뮬레이션 모델을 잇는 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1092"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "SDFormat 은 로봇·환경을 시뮬레이터용으로 기술하는 형식. 33. 시나리오 모델·편집 페이지 9절이 로봇 모델 기술을 연계 대상으로 둠. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: IDTA 서브모델 템플릿 'Provision of Simulation Models'(1.0)는 자산관리셸(AAS)을 통해 자산의 시뮬레이션 모델 파일을 모델 유형·사용법·적용 분야와 함께 제공하게 하고, 현재 단계 사용 사례로 시뮬레이션 모델 검색과 제조사·유통사에 대한 모델 파일 요청을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1314"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 저장소 README: 주 대상은 DAE 모델이며 CAD·FMEA 모델도 포함, 특정 시뮬레이터용 파일·소스 코드·FMI 같은 교환 형식으로 제공 가능. 향후 단계로 시뮬레이션 환경 자동 통합과 BOM 기반 전체 시스템 시뮬레이션 생성을 듦.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ B. 로봇 온톨로지의 7. 온톨로지 검증·변경 관리: 7. 온톨로지 검증·변경 관리가 능력 정의에 붙이는 지원 단계(시뮬레이션 연결·시뮬레이션 검증·실기 검증)를 판정하려면 모델·시뮬레이션 신뢰도 평가와 시뮬레이션–현실 상관 지표가 기준이 될 수 있으나, 두 체계를 대응시킨 자료는 확인하지 못했다(oq-156).",
      "tag": "추정",
      "source_ids": [
        "ref-1133",
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "NASA-STD-7009B 는 M&S 결과 수용·신뢰도 평가, Kadian 외는 SRCC 제안. 로봇 능력 지원 단계와의 대응 근거 없음. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ C. 채팅 기반 구성·운영의 9. 채팅으로 시나리오 구성: Chat2Scenic(2026-07, 자율주행 대상)은 챗봇 인터페이스로 시나리오를 대화로 다듬으면서 검색 증강 방식으로 도메인 특화 언어 시나리오 스크립트를 만들고, 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%(비교 방법 30.08%·16.26%)를 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-833"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2607.14387 초록 기준(보류 실행 1차 검증이 열람 확인). 지표는 컴파일 성공률(CSR). 자율주행 시나리오이며 로봇 플릿 대상 아님. (재인용: 2026-10-09-04)",
      "as_of": "2026-07-15",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ C. 채팅 기반 구성·운영의 9. 채팅으로 시나리오 구성·13. 대화형 기능의 신뢰·기반: 대화로 만든 시나리오의 출력 형식은 33. 시나리오 모델·편집이 정하는 매개변수화·장애 선언 형식이 되고, 생성 스크립트가 컴파일되지 않는 경우가 남으므로 승인 전 형식 검사가 두 대분류의 인계 지점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-833",
        "ref-1088",
        "ref-528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Chat2Scenic 컴파일 실패 잔존, OpenSCENARIO 의 매개변수화, ARIAC 의 장애 매개변수 선언을 조합한 해석. 의도 일치 검사 방법은 미확인. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f9",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현: Xia 외(2026-08, ETFA 2026 채택)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다.",
      "tag": "사실",
      "source_ids": [
        "ref-832"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2608.23622 초록 기준(보류 실행 1차 검증이 열람 확인). 제약 공정 대상이며 로봇 플릿 아님. (재인용: 2026-10-09-04)",
      "as_of": "2026-08-22",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현: 대화로 조건을 바꿔 비교하는 일은 언어 모델이 34쪽 시뮬레이션 실험을 설계·실행하는 구조로 이어질 것으로 보이나, 비교 결과를 믿으려면 36쪽 재현 충실도 지표가 함께 필요하고 로봇 플릿에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-832",
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Xia 외(공정 설계)와 Kadian 외(SRCC, LoCoBot 주행) 모두 로봇 플릿 대상 아님. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: SayPlan(Rana 외, CoRL 2023)은 언어 모델이 3차원 장면 그래프로 세운 초기 계획을 실행 전에 장면 그래프 시뮬레이터로 확인하고 그 피드백으로 실행 불가능한 동작을 고치는 반복 재계획을 두며, 최대 3개 층·36개 방·140개 자산·물체 환경에서 이동 매니퓰레이터로 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-416"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 시맨틱 탐색으로 관련 하위 그래프를 고르고, 고전 경로 계획기로 계획 범위를 줄이며, 'iterative replanning' 으로 시뮬레이터 피드백에 따라 초기 계획을 다듬는다. 단일 로봇 대상.",
      "as_of": "2023-07-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 대화로 만든 계획을 사람이 승인하기 전에 36. 가상 시운전·실제 상황 재현의 '실행 전 계획 검증'으로 실행 가능성을 먼저 걸러 내는 구조가 두 영역의 접점이 될 것으로 보이나, 다중 로봇 플릿 계획에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-416"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "SayPlan 의 시뮬레이터 피드백 재계획은 단일 이동 매니퓰레이터 대상. 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행'과의 순서 관계는 해석.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ C. 채팅 기반 구성·운영의 8. 채팅으로 맵 작성: Open-RMF 에서 같은 건물 파일(.building.yaml)이 주행 그래프와 시뮬레이션 월드를 모두 만들므로, 대화로 작성·수정한 지도가 같은 형식으로 저장되면 시뮬레이션 월드도 다시 생성할 수 있을 것으로 보이나 대화형 지도 작성과 연결한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-406",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "building_map_generator 의 gazebo 모드는 .world 와 모델 폴더를, nav 모드는 플릿 어댑터용 주행 그래프를 만든다(원문 확인). 대화형 지도 작성과의 연결은 해석.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f14",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리: Open-RMF 의 building_map_generator 는 traffic-editor 로 주석한 건물 파일에서 층별 바닥·벽과 문·승강기를 담은 시뮬레이션 월드와 주행 그래프를 만들고, 환경을 바꿀 때는 주석을 고쳐 다시 생성한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation 장 원문(github_raw) 확인: gazebo 모드는 .building.yaml 을 파싱해 .world 파일과 모델 폴더 생성, nav 모드는 주행 그래프 생성. traffic-editor 는 문·승강기·충전기 주석. 두 출처 같은 기관.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f15",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: 언어 모델·생성 모델로 시뮬레이션 환경을 만드는 연구(Holodeck, Arena 4.0)가 33. 시나리오 모델·편집의 예제 라이브러리를 채우는 수단이 될 수 있으나, 생성 환경은 실제 현장 지도가 아니므로 D. 공간·지도 모델의 도면·현장 정합과 구분해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-815",
        "ref-1089"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Holodeck 은 글 지시로 3D 환경 생성, Arena 4.0 은 생성 모델 기반 환경 생성. 실측 정합 언급 없음. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: 제조 분야 분류 자료가 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분하므로, 18은 현장 상태를 가상 모델에 반영하는 현재 상태 표현을, 34는 그 모델을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-291"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Kritzinger 외(2018) 분류. 근거 자료는 제조 대상. E. 사물·사람·실시간 상태 대분류 페이지 연결 절에 같은 각주로 실린 주장과 같다. (재인용: 2026-10-09-03)",
      "as_of": "2018",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: Waymax(2023)는 실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화하거나 재생하고, 사실적 상호작용을 위해 학습된 행동 모델과 규칙 기반 행동 모델을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1128"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자율주행 대상이며 로봇 현장 사례 아님. 기록 재생 시 다른 행위자가 반응하지 않는 문제(oq-256)의 참고. (재인용: 2026-10-09-04)",
      "as_of": "2023-10-12",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델·M. 안전의 49. 사람 근접 안전: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션으로 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-406",
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation 장: crowdsim 은 선택 기능이며 menge 가 각 에이전트를 제어. rmf_demos README: 공항 터미널에서 use_crowdsim:=1 로 실행. 두 출처 같은 기관(독립 교차 아님).",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: NIST ARIAC 시나리오는 작업 대상인 배터리 셀의 종류(Li-Ion·Ni-MH)·전압 허용 범위·결함(찌그러짐·부풂·긁힘)과 4셀 키트를 정의하고, 키트는 출하 지점에서 제출 서비스가 셀 결함·전압·종류·총전압 조건을 모두 만족할 때만 받아들인다.",
      "tag": "사실",
      "source_ids": [
        "ref-1087"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "scenario.rst(github_raw): 전압 ±0.2 V 밖 셀은 재활용 통, 키트 총전압 4·Vcell ±0.15, AGV 이동 전 키트 품질 확인 서비스 호출. 경진대회 시뮬레이션이며 실제 공장 아님.",
      "as_of": "2026-10-09",
      "site_type": "제조 공장",
      "flow_item": "작업 대상"
    },
    {
      "id": "f20",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·G. 계획·최적화의 24. 작업·워크플로 모델링: ARIAC 처럼 시나리오가 작업 대상의 속성과 완료 판정 조건을 함께 담으면, 시나리오 형식이 17의 작업 대상 식별자와 24의 완료 조건 어휘를 공유해야 할 것으로 보이나 이를 정한 공통 형식은 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1087"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ARIAC 시나리오의 셀 속성·키트 제출 조건에서 끌어낸 해석. 물류·병원 시나리오에 적용한 공개 형식 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f21",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ F. 연동의 22. 설비·건물 시스템 연동: Open-RMF 시뮬레이션의 문·승강기 플러그인은 실제와 같은 문·승강기 요청 메시지에 응답하고, door_supervisor 는 한 로봇이 다른 로봇 앞에서 문을 닫는 것 같은 충돌을 막으며 lift_supervisor 는 여러 플릿의 승강기 요청을 관리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문(github_raw): 문 플러그인은 /door_requests 의 DoorRequest, 승강기 플러그인은 /lift_requests 의 LiftRequest 에 응답. 실제 승강기·문 제어는 시설·설비 제어 경계의 연계 대상이며 ROP 는 요청·상태 확인만.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f22",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ F. 연동의 20. 로봇·제조사 관제 연동: Open-RMF 의 slotcar 플러그인은 플릿 어댑터의 경로·모드 요청(PathRequest·ModeRequest)을 받아 경유점 사이를 레일식 직선으로 움직이고 장애물을 감지하면 멈추는 단순화 로봇 모델로, 센서 기반 주행 스택을 돌리는 계산 부담을 피한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문(github_raw) 확인. 로봇 자체 주행·인식 거동의 충실도는 제조사·물리 시뮬레이터 쪽 연계 대상.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f23",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ F. 연동의 21. 상호운용 표준·적합성: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 들어와 있고 2026년 디지털 트윈 결합을 다루는 제6부가 발행되었으나, 물류센터 이종 로봇·설비에 그대로 쓸 수 있는지는 확인되지 않았다(oq-085).",
      "tag": "사실",
      "source_ids": [
        "ref-516",
        "ref-518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 출처는 서로 다른 부(제1부·제6부)를 가리키며 교차 확인 아님. 34 페이지 7·11절 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2026",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "연계 대상: I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ F. 연동의 23. 업무 시스템 연동: 성수기 주문·물동량 전망 같은 시나리오 입력은 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 물류·공급망 디지털 트윈 검토는 실제 데이터로 검증한 연구가 소수라고 보고한다.",
      "tag": "추정",
      "source_ids": [
        "ref-521"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Le·Fan(2024) 검토. 수요예측은 분류 원문 19장 상위 업무 시스템 경계의 외부 영역. (재인용: 2026-10-09-04)",
      "as_of": "2024",
      "site_type": "물류창고",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계·36. 가상 시운전·실제 상황 재현 ↔ F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 63. 병원·의료: 고려대학교 구로병원의 약품 배송 로봇 기록(2025-06, 122건)과 몬테카를로 재현에서 승강기 가동률 59.01% 이하일 때 배송 성공률 95.5%, 90% 초과에서 실패가 몰렸다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36 페이지 5절 검증된 [사실] 재인용. 같은 논문이 ref-060(doi)으로도 등록돼 있으나 ref-943 하나로만 인용. 승강기 제어는 연계 대상. (재인용: 2026-10-09-04)",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 64. 상업 시설: 다층 호텔의 배송 로봇 경로 계획 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "35 페이지 9절 검증된 [사실] 재인용. 승강기 제어 자체는 연계 대상. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 65. 가정·공동주택: 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 국내 인증 모델(2023)은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야 28개 항목(총점 176점)으로 구성된다.",
      "tag": "사실",
      "source_ids": [
        "ref-409"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 연동 대분류 페이지 검증된 [사실] 재인용. 대상은 공동주택이며 물류센터 아님. 35의 '로봇 친화 공간 설계·개조'와 연결. (재인용: 2026-10-09-04)",
      "as_of": "2023",
      "site_type": "가정",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f28",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ F. 연동의 20. 로봇·제조사 관제 연동·O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: 2025-07 보도에 따르면 클로봇은 산업통상자원부 국가로봇테스트필드 기술개발 과제(54억원) 주관기관으로 KETI 와 함께 다종·다수 로봇 제어 FMS 요소기술, 로봇과 디지털 트윈·시뮬레이터 간 인터페이스, 실환경 연동 디지털 트윈 증강 시뮬레이션을 2028년까지 개발해 국가로봇테스트필드에 적용하는 것을 목표로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1310"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "파이낸스스코프 2025-07-11 기사 1건 기준. 과제 공고·성과는 미확인. 국내 공공 과제가 로봇–시뮬레이터 인터페이스를 직접 다루는 사례.",
      "as_of": "2025-07-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 공개 오픈소스 vda5050-sim 은 VDA 5050 3.0.0 을 주 대상으로 기본 5종 AGV 를 흉내 내 실제 하드웨어 없이 관제 시스템을 시험하게 하며, 2.1.0·2.0.0·1.1.0 구형 펌웨어 로봇의 축소된 메시지와 기능도 흉내 내고, 공식 JSON 스키마 대조 적합성 시험 묶음을 둔다고 README 에 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-407"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw): 로봇별 MQTT 또는 NATS 연결, 주문·즉시 동작·상태·구역 프로토콜. 유지 기관 미기재의 개인 프로젝트 자기 기술이며 VDA·VDMA 공식 적합성 시험 아님.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: 한 유통사 물류센터 팔레트 이동 데이터로 한 AMR 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-102"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "35 페이지 3절 검증된 [사실] 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2025",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: 로봇 이동형 풀필먼트 시스템의 충전·배터리 교환 전략을 반개방형 대기행렬 네트워크로 비교한 연구(Zou 외, 2018)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-098"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "35 페이지 4·10절 검증된 [사실] 재인용. 결과 수치는 이번에 확인하지 않음. (재인용: 2026-10-09-04)",
      "as_of": "2018",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: 창고 충전소 배치를 페이지랭크 유사 방법으로 최적화하는 연구(Stark 외, 2024-06)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "35 페이지 10절 검증된 [사실] 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2024-06",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Open-RMF 플릿 어댑터 템플릿 설정에서 배터리가 recharge_threshold(예시값 0.10) 아래인 로봇은 작동하지 않으며, 충전 작업의 목표 충전 수준은 recharge_soc(예시값 1.0)로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml(github_raw): 'Battery level below which robots in this fleet will not operate'. task_capabilities 에 loop·delivery 선언.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f34",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: 충전 임계값 아래 로봇이 작업하지 않으므로, 충전기 수·위치 같은 충전 설비 계획의 결과가 운영 중 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어질 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-105",
        "ref-102"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문에 없는 연결 해석(35 페이지 10절에서도 [추정]). 공개 사례 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f35",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ G. 계획·최적화의 26. 작업 순서·스케줄링: 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정한 Boysen 외(2017)는 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-381"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "G. 계획·최적화 대분류 페이지 검증된 [사실] 재인용. 저자 계산 실험 조건, 독립 재현 미확인. (재인용: 2026-10-09-04)",
      "as_of": "2017",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f36",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: RAWSim-O 는 로봇 이동형 풀필먼트 시스템의 여러 결정 문제를 연구하는 이산 사건 시뮬레이션이며, Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다.",
      "tag": "사실",
      "source_ids": [
        "ref-101",
        "ref-398"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "34 페이지와 G 대분류 페이지 검증된 [사실] 재인용. 시뮬레이션 결과이며 현장 실측 아님. 두 출처는 도구와 연구로 서로 다른 내용. (재인용: 2026-10-09-04)",
      "as_of": "2019",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f37",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-267"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "34 페이지 5절 검증된 [사실] 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2024",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f38",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: 경로망 배치를 시뮬레이션으로 평가하는 일은 현재 상태 표현이 아니라 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽에 걸치는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-267"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "G. 계획·최적화 대분류 페이지가 [추정]으로 실은 위치 판단과 같다. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Moving AI Lab 의 MAPF 벤치마크는 지도마다 시나리오 파일(even·random 각 25개)을 묶어 공개한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1091"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보류 실행 1차 검증이 벤치마크 페이지를 열어 지도별 시나리오 파일 제공을 확인. 이번 실행은 다시 열지 않음. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: 지도와 시나리오 파일을 묶어 공개하는 방식은 경로 계획기를 같은 조건에서 비교하게 하는 시나리오 라이브러리 구성의 예로 쓰일 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1091"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤치마크 페이지는 비교 목적을 명시하지 않음(1차 검증 지적). 해석.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ G. 계획·최적화의 24. 작업·워크플로 모델링: 로봇 미션 명세·실행 형식 비교 연구와 행동 트리 편집기(Groot2)가 33의 미션 기술 형식·편집기 선택 근거로 쓰였으므로, 시나리오 안의 작업 표현은 24의 단계·선후관계·완료 조건 표현과 같은 형식을 공유해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-116",
        "ref-1090"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "33 페이지 9절 재인용. Groot2 는 벤더 문서 유형이나 기능·성능 주장은 아님. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: VirTooS(2026-08)는 ROS 2와 Unity 를 결합한 혼합 현실 환경에서 실제·가상 로봇과 실제·가상 센서를 함께 써서 자율이동로봇 팀의 플릿 관리 작업을 시험하는 도구이며, 작업 배정 예제에서 실제 로봇과 가상 로봇이 상호작용한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1129"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록 기준(보류 실행 1차 검증이 열람 확인). 컨테이너 배포. (재인용: 2026-10-09-04)",
      "as_of": "2026-08-26",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·Q. 현장 유형별 적용의 63. 병원·의료: Lee 외 저자들은 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰고, 병원별 구조·통행·승강기 제어 정책을 재현한 병원 디지털 트윈으로 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다.",
      "tag": "의견",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "의견 주체: Lee 외 저자. 36 페이지 5절 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: NIST ARIAC 는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급 주문을 매개변수로 선언해 시각이나 발생 횟수 조건으로 시나리오에 주입한다.",
      "tag": "사실",
      "source_ids": [
        "ref-528"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "33 페이지 5절 검증된 [사실] 재인용. 경진대회 시나리오이며 실제 공장 아님. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f45",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성·32. 예외 복구·재계획·업무 연속성: vda5050-sim 은 로봇별 고장 프로필로 연결 끊김·오류 주입·필드 위반·서비스 모드·비상 정지의 확률을 정하고, 명세의 재시도 가능 동작 흐름(RETRIABLE·retry·skipRetry)을 구현한다고 README 에 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-407"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw) 확인. 개인 프로젝트의 자기 기술이며 공식 적합성 시험 아님. 실행 신뢰성·예외 복구를 설치 전에 장애 주입으로 시험하는 도구의 예.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f46",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ H. 실행·협업·예외 복구의 30. 로봇 간 협업·물리적 인계: Open-RMF 시뮬레이션의 TeleportDispenser 는 DispenserRequest 에 응답해 적재물을 가장 가까운 로봇 위로 순간 이동시키고, TeleportIngestor 는 IngestorRequest 에 응답해 로봇의 적재물을 월드로 옮겨 배송 작업의 적재·하역을 흉내 낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation 장 원문(github_raw) 확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f47",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ H. 실행·협업·예외 복구의 30. 로봇 간 협업·물리적 인계: 적재·하역을 순간 이동으로 대신하므로 이 시뮬레이션은 물리적 인계 동작이 아니라 인계 요청–응답 흐름과 그 순서를 시험하는 데 쓰이며, 인계 실패 같은 물리 거동은 별도 모델이 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Teleport 플러그인 설명에서 끌어낸 해석. 파지·적재 물리 시뮬레이션은 로봇 자체 제어 쪽 연계 대상.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f48",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업: Garg·Maywald·Naman(IJRDM, 2025)은 AMR 과 피킹 작업자 수를 바꾼 창고 구성 48가지의 이산 사건 시뮬레이션에서 처리량·효율이 AMR:작업자 약 2:1 에서 가장 높았고, 교차 통로 배치의 처리량 효과는 통계적으로 유의하지 않았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1306"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 고속 소매·전자상거래 물류의 혼합 피킹, 비용 효율 분석 1,200 시나리오. 저자 시뮬레이션 조건이며 다른 운영에 그대로 옮겨지는지 미확인.",
      "as_of": "2025-10-14",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f49",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업·P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Howard(2026)의 시뮬레이션에서는 작업자 유휴 시간이 교대당 AMR 유휴 시간보다 약 2.5배 비싸 작업자와 로봇이 서로 기다리는 동기화 손실의 비용이 주로 노동 쪽에 떨어졌고, 세 배차 휴리스틱은 라인당 비용에 유의한 차이를 내지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-822"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3구역 순차 구역제·연속 도착 조건, 석사논문 저자 보고값. 작업자 배치와 로봇 대수를 함께 정하는 문제(oq-009)에 부분 근거이나 교대조 단위는 아님.",
      "as_of": "2026-06",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f50",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석: rosbag2 는 ROS 2 통신을 백 파일(기본 저장 형식 MCAP)로 기록하고, 재생 속도 조절(~/set_rate)·/clock 발행(--clock)·토픽 선택(--topics)·여러 백 파일의 수신 시각순 동시 재생(-i)을 지원하며, 시작 시각 지정은 ~/play 서비스로 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(rolling, github_raw) 확인. 시작 시각 지정은 CLI 옵션이 아니라 서비스로 문서화됨.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f51",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 메시지 단위 기록 도구와 기록 기반 시뮬레이터가 있으나, 재현의 원천은 37이 남기는 오케스트레이션 수준 실행 기록(작업·배정·위치·사건 시각)이어야 할 것으로 보이며 이를 시나리오 사양으로 바꾸는 공개 형식은 확인하지 못했다(oq-131).",
      "tag": "추정",
      "source_ids": [
        "ref-831",
        "ref-1128"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "rosbag2 는 메시지 기록·재생, Waymax 는 주행 기록 기반 시뮬레이션. 오케스트레이션 기록→시나리오 변환 형식 미확인. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f52",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ J. 현장 운영·관제의 39. 운영 성과 측정·개선: 충전 방식의 비용 비교와 국내 스마트물류센터 인증 평가에서 두 영역이 만나는 것으로 보이나, 인증 세부 지표에 로봇 대수·가동률 같은 설비 계획 지표가 들어가는지는 확인하지 못했다(oq-011).",
      "tag": "추정",
      "source_ids": [
        "ref-098",
        "ref-106"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "35 페이지 10절 연결 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f53",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API: rmf_demos 는 시뮬레이션 데모에서 플릿 어댑터의 server_uri 를 rmf-web API 서버(ws://localhost:8000/_internal)로 지정하면 어댑터가 최신 작업·로봇 상태를 API 서버에 보내고 대시보드로 볼 수 있게 하며, Docker 대시보드는 빠른 연동·시험용이라고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw): 'the fleetadapter will update rmf-web api-server with the latest task and robot states'. API 서버 localhost:8000, 대시보드 localhost:3000.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f54",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API: 시뮬레이션 플릿과 실제 플릿이 같은 플랫폼 API·대시보드에 붙으므로, 외부 시스템 연동과 운영자 화면을 설치 전에 가상 플릿으로 시험할 수 있을 것으로 보이나 이를 시운전 절차로 정리한 공개 사례는 확인하지 못했다(oq-255).",
      "tag": "추정",
      "source_ids": [
        "ref-104",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "rmf_demos 의 server_uri 연결과 시뮬레이션 플러그인이 실제와 같은 메시지에 응답한다는 설명에서 끌어낸 해석.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f55",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: 가상 시운전 도구가 여러 머신에 컨테이너로 배포되고 시뮬레이션 플러그인이 실제와 같은 요청 메시지에 응답하므로, 가상 대응물을 어느 계산 자원에 두고 실제 시스템과 어떤 통신으로 잇는지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1129",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "플랫폼 배치 근거 없음(oq-040). (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f56",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: MCAP 은 시각이 찍힌 발행·구독 메시지를 담는 컨테이너 형식으로, 메시지마다 기록 시각(log_time)과 발행 시각(publish_time)을 따로 두고 청크 색인에 청크별 최초·최종 기록 시각을 담아 시각·토픽으로 메시지를 찾게 하며, rosbag2 의 기본 저장 형식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1096",
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MCAP 명세(webfetch): 채널별 메시지 인코딩, zstd·lz4 압축 청크. rosbag2 README: 기본 저장 플러그인 mcap. 두 출처는 서로 다른 내용(형식 정의와 채택).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f57",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: Holodeck(CVPR 2024)은 GPT-4 가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성하며, 생성 장면에서 학습한 에이전트가 처음 보는 환경에서 주행했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-815"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2312.09067 초록 기준(보류 실행 1차 검증이 열람 확인). (재인용: 2026-10-09-04)",
      "as_of": "2023-12-14",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f58",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ L. AI·학습 기술의 45. 문서·도면·장면 이해: Sommer 외(2023)는 기존 건물 환경의 스캔과 객체 인식을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-241"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "34 페이지 6·8절이 인용한 스캔 기반 자동 생성 연구. 이번 실행은 원문을 다시 열지 않음. 로봇 플릿 시뮬레이션에 쓴 사례 미확인.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f59",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ L. AI·학습 기술의 46. 예측·학습 기반 최적화: Smit 외(2024-04, arXiv)는 작업자와 AMR 이 피킹 위치에서 만나는 창고에서 작업자–AMR 배정을 다목적 심층 강화학습으로 정하고, 이를 학습·평가하려고 이산 사건 시뮬레이션 모델을 만들었으며, 학습 정책이 효율과 작업자 부하 공정성 모두에서 비교 방법을 앞섰다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 창고를 그래프로 모델링, 크기가 다른 창고로 어느 정도 일반화, 시뮬레이션 구현 공개. 프리프린트, 저자 보고. 25. 작업 배정 — MRTA 의 학습 기반 배정과도 이어짐.",
      "as_of": "2024-04-09",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f60",
      "claim": "I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 ↔ L. AI·학습 기술의 46. 예측·학습 기반 최적화: Howard(2026)는 반개방형 대기행렬 모델로 설계안을 걸러 내고 XGBoost 대리 모델과 등각 예측 구간으로 추가 시뮬레이션 없이 연속 설계 공간의 비용을 예측했으며, 대기행렬 모델은 시뮬레이션 라인당 비용과 약 5%, 대리 모델은 교차 검증에서 3% 안에서 맞았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-822"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "석사논문 초록, 저자 보고값. 이 모델 계층으로 공개 의사결정 지원 도구를 만들었다고 밝힘.",
      "as_of": "2026-06",
      "site_type": "물류창고",
      "flow_item": null
    },
    {
      "id": "f61",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: 학습 정책이 시뮬레이터의 결함을 악용하는 현실 격차가 보고되므로, 학습 기반 정책의 현실 격차 보정은 47쪽(및 로봇 제조사·시뮬레이션 도구) 일이고 36은 재현 결과와 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-741",
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "현실 격차 보정은 연계 대상. 36 페이지 9절 경계와 같다. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f62",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ M. 안전의 48. 안전·위험 관리: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 생성해, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1303"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 무작위·몬테카를로 탐색은 큰 탐색 공간에서 비실용적이라 최적화로 위험 행동을 찾는다. 협동 로봇 셀 대상이며 이동로봇 플릿 아님.",
      "as_of": "2020-11-20",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f63",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ M. 안전의 48. 안전·위험 관리: 위험 상황을 생성·탐색하는 시뮬레이션 시험(사람 행동 최적화, 확률적 시나리오 언어 기반 반증)이 있으므로, 33에서 선언한 장애·사람 흐름 시나리오가 48의 위험 식별 입력이 될 수 있을 것으로 보이나 다중 이동로봇 플릿에 적용한 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1303",
        "ref-1086"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "안전 인증·설비 안전 제어 판단은 연계 대상이며 시나리오가 위험 식별 입력이 될 수 있다는 범위로만 서술. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f64",
      "claim": "연계 대상: I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: Wind River 인터뷰(2014)는 IEC 61508-7 C.5.19 가 시뮬레이션을 시험 목적으로만 피제어 설비(EUC)의 거동을 흉내 내는 시스템으로 정의한다고 인용하고 기능안전 표준들이 안전 확인에 시뮬레이션을 강하게 권고한다고 해석하지만, 이동로봇 안전 표준이 시뮬레이션 결과를 인증 근거로 받아들이는 절차는 이번 조사에서 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1312"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "업체 블로그의 표준 인용·해석이며 표준 원문 미확인. 장애 주입도 강하게 권고되는 확인 기법으로 언급. ISO 3691-4 의 시뮬레이션 관련 조항은 검색에서 확인되지 않음.",
      "as_of": "2014-11-20",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f65",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고하고 완화 방안을 논의했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1304"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2211.09507 초록(webfetch) 확인. 프리프린트.",
      "as_of": "2022-11-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f66",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사: 36이 다루는 디지털 트윈 동기화(실시간 상태를 가상 모델에 반영하고 결과를 되돌리는 경로)는 공격 표면이 될 수 있으므로, 시뮬레이션 결과가 실제 계획·설정에 반영되는 경로에 접근통제와 무결성 확인이 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1304"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "로봇 플릿 플랫폼 적용 사례 없음. 34가 현재 상태를 표현한다고 보지 않고 36의 동기화 경로로만 서술.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f67",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터: Autoware 재단의 autoware_rosbag2_anonymizer 는 ROS 2 백 파일(sqlite3·mcap)의 이미지에서 사람 얼굴·번호판 같은 대상을 GroundingDINO·OpenCLIP·SegmentAnything2·YOLO 로 찾아 가우시안 블러로 가린 익명화 백 파일을 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1309"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw): 대상은 validation.json 의 프롬프트로 정의(예: 차 안의 번호판, 사람 몸 안의 얼굴). GPU 메모리 요구가 크고 처리가 느릴 수 있다고 적음. 자율주행 생태계 도구.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f68",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터: 운영 기록으로 상황을 재현하거나 기록을 외부와 공유하기 전에 영상 기록의 얼굴 등을 가리는 익명화 단계가 두 영역의 경계가 될 것으로 보이나, 로봇 플릿 재현에서 익명화가 재현 충실도에 주는 영향을 다룬 자료는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1309",
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "rosbag2 기록 + 익명화 도구 조합에서 끌어낸 해석. 국내 개인정보 처리 요건과의 관계는 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f69",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크·55. 현장 조사·설치·시운전: Open-RMF 문서는 시뮬레이션 로봇이 배터리 소모·충돌 비용이 없어 시나리오를 반복해 수정을 확인하고 드문 예외를 살필 수 있으며, 장시간 시뮬레이션으로 배치 전에 시설 소유자의 확신을 높일 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "simulation 장 Motivation(github_raw): 'Robots in simulation neither run out of battery nor incur costs when they happen to unfortunately crash into something.'",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f70",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: 설비 제어 분야의 가상 시운전 정의(VDI/VDE 3693)와 실제 제어기·가상화 인스턴스를 섞은 분산 가상 시운전 연구가 있어 36의 결과가 55의 현장 시운전 준비로 넘어갈 것으로 보이나, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차는 확인하지 못했다(oq-255).",
      "tag": "추정",
      "source_ids": [
        "ref-1126",
        "ref-1130",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "PLC·설비 제어 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상. 36 페이지 3절 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f71",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Kadian 외(RA-L 2020)는 시뮬레이션–현실 상관 계수(SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 가 0.18 이었으나 시뮬레이션 매개변수를 조정해 0.844 로 높였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1127"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1차 검증 지시에 따라 '기본 설정'을 'CVPR 2019 챌린지에서 쓰인 Habitat 설정'으로 고침. 원인으로 벽 미끄러짐 지목. (재인용: 2026-10-09-04)",
      "as_of": "2020-08",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f72",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: NASA-STD-7009B(2024-03-05)는 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1133"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36 페이지 7절 검증된 [사실] 재인용. (재인용: 2026-10-09-04)",
      "as_of": "2024-03-05",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f73",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: Gazebo Fuel 서버의 모델·월드를 내려받고 올리는 gz-fuel-tools 의 README 로드맵은 원격 모델의 새 버전이 올라왔을 때 이를 감지하는 방법을 아직 정해야 할 과제로 적고 해시 기반 방식을 아이디어로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1313"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw, main). 시뮬레이션 자산의 판 변경 추적이 클라이언트 도구에서 완결되지 않았다는 근거. 모델별 판 목록 형식은 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f74",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 모델 라이선스를 지정하고 CC BY 3.0 Unported 를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1231"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보류 실행 1차 검증이 튜토리얼을 열어 확인(권장이며 요구 아님). 이번 실행은 다시 열지 않음. oq-292 관련. (재인용: 2026-10-09-04)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f75",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Kassem·Michahelles(Mensch und Computer 2022 워크숍)는 협동 로봇이 공장·물류·제조 현장에 들어오면서 사람–기계 상호작용을 빠르게 평가할 필요가 커졌다고 보고, 소비자용 VR·AR 헤드셋으로 로봇을 가상으로 흉내 내 사용자 연구에 쓰는 방법과 방향을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1311"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준. 이동로봇 플릿 도입 전 작업자 수용성을 가상 환경으로 측정한 사례는 이번 조사에서 찾지 못함.",
      "as_of": "2022-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f76",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: IDTA 'Provision of Simulation Models' 서브모델이 제조사·유통사에 시뮬레이션 모델 파일을 요청하는 사용 사례를 두므로, 로봇·설비 제조사가 가상 시운전용 모델을 어떤 형식·충실도로 제공할지가 다사업자 계약·데이터 제공 항목이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1314"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "서브모델 README 의 사용 사례에서 끌어낸 해석. 로봇 플릿 조달 계약에 넣은 사례 미확인.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f77",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·35. 처리능력·규모·배치 설계 ↔ Q. 현장 유형별 적용의 62. 제조 공장: Stączek 외(Sensors, 2021)는 통로가 좁은 생산 홀의 AMR 운영 환경을 ROS 와 연결한 Gazebo 디지털 트윈으로 만들어 현장 시험 전에 위치 추정·주행·작업 시간을 확인했고, 통로에 회전용 홈을 내는 배치 변경안이 도킹 복귀 시간을 평균 44초에서 22.5~23.3초로 줄였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1307"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원래 통로는 로봇이 회전하지 못해 후진 복귀(후진 0.3 m/s, 전진 0.7 m/s). 2×0.4 m 홈 두 안 비교. 저자들은 디지털 트윈 표준 설계 패턴·범용 도구 부족을 지적.",
      "as_of": "2021-11-25",
      "site_type": "제조 공장",
      "flow_item": "제약"
    },
    {
      "id": "f78",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ Q. 현장 유형별 적용의 62. 제조 공장: 최성욱·박상철·왕지남(2008)은 자동차 차체 생산라인의 PLC 코드 검증을 위해 실제 PLC 와 3D 가상 공정 시뮬레이터를 양방향 통신으로 잇는 가상 플랜트 구축 절차를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1131"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36 페이지 5절 검증된 [사실] 재인용. PLC 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상이며 ROP 가상 시운전의 방법 근거로만 사용. (재인용: 2026-10-09-04)",
      "as_of": "2008-11",
      "site_type": "제조 공장",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f79",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ Q. 현장 유형별 적용의 62. 제조 공장: 2026-08 보도에 따르면 아바코는 산업통상자원부 산업 AI 솔루션 실증확산 지원사업(이차전지 분야, 한국생산기술연구원 주관)에서 AMR 스마트 물류 시스템을 개발·실증하며 실물 설비 구축 전에 디지털 트윈 가상 환경에서 물류 동선과 장비 운용을 검증했고, 공정물류 다운타임 20% 절감과 물류 자동화율 90% 이상을 달성했다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1316"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 수치는 회사 발표를 옮긴 기사(파이낸스스코프 2026-08-14) 1건 기준이며 기준선·측정 방법 미공개.",
      "as_of": "2026-08-14",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f80",
      "claim": "I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈 ↔ Q. 현장 유형별 적용의 61. 물류창고: CJ대한통운은 2021-11 현실 물류센터와 같은 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획을 발표했고 작업 동선·재고 배치·설비 효율 최적화를 목표로 들었으나, 이후 적용 결과는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-526"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 34 페이지 5절의 [추정] 벤더 주장 재인용. oq-084·oq-117 관련. (재인용: 2026-10-09-04)",
      "as_of": "2021-11",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f81",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ Q. 현장 유형별 적용의 64. 상업 시설: Open-RMF 예제 호텔 월드는 로비와 객실 2개 층에 승강기 2대·여러 문·로봇 플릿 3개(로봇 4대)를 담고, 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 플릿·설비·사람의 상호작용과 청소 작업을 보이는 시뮬레이션 예제다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw) 확인. 작업은 dispatch_patrol·dispatch_delivery·dispatch_clean 명령으로 따로 넣음. 실제 시설 사례 아님.",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f82",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ Q. 현장 유형별 적용의 65. 가정·공동주택: BEHAVIOR-1K 는 설문으로 고른 일상 가정 활동 1,000개를 BDDL 로 명세하고 장면 50개와 주석 객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크다.",
      "tag": "사실",
      "source_ids": [
        "ref-971"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "33 페이지 5절 검증된 [사실] 재인용. 벤치마크이며 실제 가정 배치 아님. (재인용: 2026-10-09-04)",
      "as_of": "2024-03-14",
      "site_type": "가정",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f83",
      "claim": "I. 설계·시뮬레이션의 33. 시나리오 모델·편집 ↔ Q. 현장 유형별 적용의 66. 실외: Open-RMF 예제 캠퍼스 월드는 GPS(WGS84) 좌표를 쓰는 넓은 실외 지도에서 여러 배송 로봇이 위치를 플릿 어댑터에 보내는 시뮬레이션 예제다.",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(github_raw) 확인. 실제 캠퍼스 배치 사례 아님.",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "작업 대상"
    },
    {
      "id": "f84",
      "claim": "I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 ↔ Q. 현장 유형별 적용의 67. 기타 현장: Ortega 외(Frontiers in Robotics and AI, 2024)는 실측 점유 격자로 모델링한 대학 건물 1층을 대상으로 동적 요소와 수용 기준(위치 추정 오차·충돌 회피)을 명시한 실행 가능한 이동로봇 시뮬레이션 시험 시나리오를 구성했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1134"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "36 페이지 5절 검증된 [사실] 재인용. 현장 기록 재생은 다루지 않음.",
      "as_of": "2024-08-02",
      "site_type": "기타",
      "flow_item": "완료·인계",
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-833",
      "org": "Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J.",
      "title": "Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving",
      "published": "2026-07-15",
      "url": "https://arxiv.org/abs/2607.14387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 챗봇 대화와 검색 증강으로 자율주행 시나리오 DSL 스크립트를 생성하고 컴파일 성공률을 보고한 프리프린트(C. 채팅 기반 구성·운영 자료 목록의 기존 id 재사용).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-832",
      "org": "Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P.",
      "title": "LLM Agents Perform Controlled Experiments Using Simulation Models",
      "published": "2026-08-22",
      "url": "https://arxiv.org/abs/2608.23622",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 에이전트가 시뮬레이션 비교 실험을 설계·실행·해석하는 틀을 제약 공정 설계에 적용(ETFA 2026 채택).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 도로 교통 시나리오의 동적 내용을 기술하는 표준 소개 페이지.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. ARIAC 의 장애(컨베이어·전압 시험기·그리퍼)와 긴급 주문을 매개변수로 선언하는 과제 문서.",
      "source_unopened": false,
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null
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
      "summary": "원문 미열람. 시뮬레이션–현실 상관 계수(SRCC)를 제안하고 시뮬레이터 매개변수 조정으로 예측력을 높인 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-416",
      "org": "Rana, K., Haviland, J., Garg, S., Abou-Chakra, J., Reid, I., & Suenderhauf, N. (CoRL 2023, arXiv)",
      "title": "SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning",
      "published": "2023-07-12",
      "url": "https://arxiv.org/abs/2307.06135",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "3차원 장면 그래프로 언어 모델 계획을 근거 짓고, 실행 전 장면 그래프 시뮬레이터 피드백으로 계획을 반복 수정하는 방법(CoRL 2023 구두 발표). 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2307.06135",
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
      "summary": "Open-RMF 시뮬레이션의 동기, slotcar·문·승강기·Teleport 플러그인, building_map_generator, crowdsim 을 설명하는 장.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
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
      "summary": "원문 미열람. 건물 파일에 차선·문·승강기·충전기를 주석하는 traffic-editor 설명.",
      "source_unopened": false,
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null
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
      "summary": "원문 미열람. 로봇·환경을 시뮬레이터용으로 기술하는 XML 형식.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1314",
      "org": "IDTA (Industrial Digital Twin Association, admin-shell-io/submodel-templates)",
      "title": "Provision of Simulation Models (IDTA 02005) 1.0 — README",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "자산관리셸로 자산의 시뮬레이션 모델 파일을 모델 유형·사용법·적용 분야와 함께 제공하게 하는 IDTA 공식 서브모델 템플릿의 저장소 README(명세 본문 아님).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/admin-shell-io/submodel-templates/main/published/Provision%20of%20Simulation%20Models/1/0/README.md",
      "source_unopened": false
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
      "summary": "원문 미열람. 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 언어 지시로 3D 체화 AI 환경을 생성하는 방법(CVPR 2024).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 생성 모델 기반 환경 생성을 포함한 ROS 2 사람 중심 주행 벤치마크 플랫폼.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분한 제조 분야 문헌 검토.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 실제 주행 기록으로 다중 에이전트 시뮬레이션을 초기화·재생하는 데이터 기반 시뮬레이터.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 예제 월드(호텔·사무실·공항 터미널·클리닉·캠퍼스·제조·물류)와 작업 명령, rmf-web 대시보드 연결, crowdsim, 화재 경보 동작을 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_demos/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1087",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC Documentation — Scenario",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ARIAC 배터리 생산 시설 시나리오의 셀·결함·키트·모듈·설비와 키트·모듈 제출 검사를 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/scenario.rst",
      "source_unopened": false
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
      "summary": "원문 미열람. 제조용 디지털 트윈 프레임워크 ISO 23247 제1부의 국내 KS 부합 표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 디지털 트윈 결합을 다루는 ISO 23247 제6부.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 물류·공급망 디지털 트윈 문헌 검토와 개념 틀, 실데이터 검증 연구가 소수임을 보고.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 병원 약품 배송 로봇 실제 기록과 몬테카를로 재현으로 승강기 가동률과 배송 실패의 관계를 분석.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1310",
      "org": "파이낸스스코프 (윤영훈)",
      "title": "클로봇, 국책사업으로 피지컬AI 기술 표준 이끈다...산자부 주관사 선정",
      "published": "2025-07-11",
      "url": "https://www.finance-scope.com/article/view/scp202507110007",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "클로봇이 산업통상자원부 국가로봇테스트필드 기술개발 과제(54억원) 주관기관으로 KETI 와 디지털 트윈 연동 증강 실험 기술을 2028년까지 개발한다는 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.finance-scope.com/article/view/scp202507110007",
      "source_unopened": false
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 로봇 플릿 시뮬레이터 README: 구형 판 흉내, 로봇별 고장 프로필, 공식 JSON 스키마 대조 시험(개인 프로젝트의 자기 기술).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/gpue/vda5050-sim/main/README.md",
      "source_unopened": false
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
      "summary": "원문 미열람. 유통사 물류센터 데이터로 AMR 플릿 규모와 충전기 수를 시뮬레이션으로 산정한 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. RMFS 의 충전·배터리 교환 전략 비교 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 플릿 어댑터 템플릿 설정: recharge_threshold·recharge_soc·task_capabilities 등.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/fleet_adapter_template/main/fleet_adapter_template/config.yaml",
      "source_unopened": false
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
      "summary": "원문 미열람. 랙 이동 로봇 작업대의 주문·랙 순서를 함께 최적화해 필요 로봇 대수를 줄인 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. RMFS 결정 문제 연구용 이산 사건 시뮬레이션 프레임워크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. RMFS 결정 규칙을 시뮬레이션으로 비교한 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 다중 AGV 경로망을 시뮬레이션으로 자동 설계하는 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 다중 에이전트 경로 찾기 벤치마크 지도와 지도별 시나리오 파일.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 로봇 미션 명세·실행 형식 비교 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 행동 트리 편집·모니터링 도구 소개.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 실제·가상 로봇과 센서를 섞은 혼합 현실 플릿 관리 시험 도구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1306",
      "org": "Garg, V., Maywald, J. D., & Naman, M. (International Journal of Retail & Distribution Management 53(10-11))",
      "title": "Optimising human-robot collaboration for efficiency in retail warehousing",
      "published": "2025-10-14",
      "url": "https://www.emerald.com/ijrdm/article/53/10-11/1123/1303314/Optimising-human-robot-collaboration-for",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "AMR 와 피킹 작업자 수를 바꾼 창고 구성 48가지 이산 사건 시뮬레이션으로 AMR:작업자 약 2:1 에서 효율이 가장 높다고 보고(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.emerald.com/ijrdm/article/53/10-11/1123/1303314/Optimising-human-robot-collaboration-for",
      "source_unopened": false
    },
    {
      "id": "ref-822",
      "org": "Howard, T. L. (California Polytechnic State University, San Luis Obispo, 석사논문)",
      "title": "A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities",
      "published": "2026-06",
      "url": "https://digitalcommons.calpoly.edu/theses/3387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "RaaS 과금 아래 협업형 AMR 대수 산정을 라인당 비용 최소화로 바꾸고 DES 27,000회·대기행렬 모델·XGBoost 대리 모델로 분석한 석사논문(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://digitalcommons.calpoly.edu/theses/3387",
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
      "summary": "ROS 2 통신 기록·재생 도구 README: 기본 MCAP 저장, 재생 속도·/clock·토픽 선택·여러 백 파일 시각순 재생.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/rosbag2/rolling/README.md",
      "source_unopened": false
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
      "summary": "원문 미열람. 국내 스마트물류센터 인증 제도 안내 사이트.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1096",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "시각이 찍힌 발행·구독 메시지를 담는 MCAP 컨테이너 형식 명세: 기록·발행 시각, 메시지·청크 색인, 채널별 인코딩.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mcap.dev/spec",
      "source_unopened": false
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
      "summary": "원문 미열람. 로봇 시뮬레이션–현실 격차의 원인과 대응을 정리한 서베이.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1308",
      "org": "Smit, I. G., Bukhsh, Z., Pechenizkiy, M., Alogariastos, K., Hendriks, K., & Zhang, Y. (arXiv)",
      "title": "Learning Efficient and Fair Policies for Uncertainty-Aware Collaborative Human-Robot Order Picking",
      "published": "2024-04-09",
      "url": "https://arxiv.org/abs/2404.08006",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "작업자–AMR 배정을 다목적 심층 강화학습으로 정하고 이산 사건 시뮬레이션으로 학습·평가한 프리프린트(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2404.08006",
      "source_unopened": false
    },
    {
      "id": "ref-241",
      "org": "Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M.",
      "title": "Automated generation of digital twin for a built environment using scan and object detection as input for production planning",
      "published": "2023",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 스캔과 객체 인식으로 생산 계획용 건물 환경 디지털 트윈을 자동 생성하는 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1303",
      "org": "Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020)",
      "title": "Simulation-based Testing for Early Safety-Validation of Robot Systems",
      "published": "2020-11-20",
      "url": "https://arxiv.org/abs/2011.10294",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 모델과 최적화로 시뮬레이션 안에서 고위험 사람 행동을 생성해 초기 설계 단계 로봇 셀의 위험을 찾는 방법(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2011.10294",
      "source_unopened": false
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
      "summary": "원문 미열람. 확률적 시나리오 언어 Scenic 3.0 의 3D 환경 모델링과 반증 기반 시험.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1312",
      "org": "Wind River (Engblom, J. 인터뷰, Buchwieser, A.)",
      "title": "Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser",
      "published": "2014-11-20",
      "url": "https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "IEC 61508-7 C.5.19 의 시뮬레이션 정의를 인용하고 기능안전 표준이 시뮬레이션·장애 주입을 권고한다고 해석한 업체 블로그 인터뷰.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser",
      "source_unopened": false
    },
    {
      "id": "ref-1304",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 구동 로봇의 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어질 수 있음을 보인 프리프린트(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2211.09507",
      "source_unopened": false
    },
    {
      "id": "ref-1309",
      "org": "Autoware Foundation (autowarefoundation GitHub)",
      "title": "autoware_rosbag2_anonymizer — README",
      "published": null,
      "url": "https://github.com/autowarefoundation/autoware_rosbag2_anonymizer",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ROS 2 백 파일 이미지의 얼굴·번호판 등을 탐지·분할 모델로 찾아 블러 처리하는 익명화 도구 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/autowarefoundation/autoware_rosbag2_anonymizer/main/README.md",
      "source_unopened": false
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
      "summary": "원문 미열람. 가상 시운전의 모델 유형·용어·정의 지침.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 실제 제어기와 가상화 인스턴스를 섞은 분산 시스템 가상 시운전 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1313",
      "org": "Open Robotics (gazebosim/gz-fuel-tools GitHub)",
      "title": "Gazebo Fuel Tools — README",
      "published": null,
      "url": "https://github.com/gazebosim/gz-fuel-tools",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Gazebo Fuel 서버의 모델·월드를 목록·다운로드·업로드하는 클라이언트 라이브러리와 gz fuel 명령 README, 원격 모델 새 버전 감지를 로드맵 과제로 적음.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/gazebosim/gz-fuel-tools/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1231",
      "org": "Open Robotics (Gazebo Classic)",
      "title": "Gazebo : Tutorial : Model structure and requirements",
      "published": null,
      "url": "https://classic.gazebosim.org/tutorials?tut=model_structure",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Gazebo 클래식 모델 데이터베이스의 폴더 구조·database.config·model.config 요구사항.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1311",
      "org": "Kassem, K., & Michahelles, F. (Mensch und Computer 2022 Workshop Proceedings, Gesellschaft für Informatik)",
      "title": "Exploring Human-robot Interaction by Simulating Robots",
      "published": "2022-09",
      "url": "https://dl.gi.de/items/1f2227be-b32d-467c-bf94-77d37e5194ce/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VR·AR 환경에서 로봇을 가상으로 흉내 내 사람–로봇 상호작용 사용자 연구를 하는 방법을 다룬 워크숍 논문(초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://dl.gi.de/items/1f2227be-b32d-467c-bf94-77d37e5194ce/full",
      "source_unopened": false
    },
    {
      "id": "ref-1307",
      "org": "Stączek, P., Pizoń, J., Danilczuk, W., & Gola, A. (Sensors 21(23):7830)",
      "title": "A Digital Twin Approach for the Improvement of an Autonomous Mobile Robots (AMR's) Operating Environment—A Case Study",
      "published": "2021-11-25",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8659435/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "생산 홀 AMR 운영 환경을 Gazebo·ROS 디지털 트윈으로 시험해 통로 배치 변경안을 평가한 사례 연구.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8659435/",
      "source_unopened": false
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
      "summary": "원문 미열람. 실제 PLC 와 3D 가상 공정 시뮬레이터를 잇는 가상 플랜트 구축 절차.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1316",
      "org": "파이낸스스코프",
      "title": "아바코, AMR 스마트 물류 시스템 개발·실증 완료… 피지컬 AI 사업 가속",
      "published": "2026-08-14",
      "url": "https://www.finance-scope.com/article/view/scp202608140009",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "아바코가 이차전지 분야 산업 AI 실증 과제에서 디지털 트윈으로 물류 동선·장비 운용을 사전 검증하고 성과 수치를 발표했다는 보도(회사 발표 수치).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.finance-scope.com/article/view/scp202608140009",
      "source_unopened": false
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
      "summary": "원문 미열람. 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획 보도자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 일상 활동 1,000개를 BDDL 로 명세하고 OmniGibson 에 구현한 벤치마크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1134",
      "org": "Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI)",
      "title": "Composable and executable scenarios for simulation-based testing of mobile robots",
      "published": "2024-08-02",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 도면 DSL·동적 요소·수용 기준을 담은 이동로봇 시뮬레이션 시험 시나리오 구성.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "원문 미열람. 물류센터 구축에서 에뮬레이션으로 제어를 사전 검증한 업체 사례 소개.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
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
      "summary": "산업용 로봇 플릿 디지털 트윈 블루프린트 발표 블로그(2025-01-06). 참고문헌 목록의 발행일 '미확인'을 원문으로 확인해 고쳤다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://blogs.nvidia.com/blog/mega-omniverse-blueprint",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/design-and-simulation/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "대분류 연결(category_link): '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1(3, 35), f2(3, 36, 벤더 주장), f3(1, 34, 벤더 주장) / B. 로봇 온톨로지: f4·f5(4), f6(7, oq-156) / C. 채팅 기반 구성·운영: f7·f8(9·13 ↔ 33), f9·f10(11 ↔ 34·36), f11·f12(12 ↔ 36), f13(8 ↔ 34) — 분류 원문 C 주석(시나리오 구성과 실제 상황 재현은 33·36번)과 짝 / D. 공간·지도 모델: f14, f15 / E. 사물·사람·실시간 상태: f16(18 ↔ 34, 현재 상태 표현 대 가정한 미래 실험 구분), f17·f18(19), f19·f20(17) / F. 연동: f21·f25·f26·f27(22), f22·f28·f29(20), f23(21, oq-085), f24(23, 연계 대상) / G. 계획·최적화: f30~f34(28·25), f35(26), f36·f42·f43(25), f37~f40(27), f41(24) / H. 실행·협업·예외 복구: f44·f45(32·29), f46·f47(30), f48·f49(31) / J. 현장 운영·관제: f50·f51(37·38, oq-131), f52(39) / K. 플랫폼 아키텍처·인프라: f53·f54(41), f55(42), f56(43) / L. AI·학습 기술: f57·f15(44), f58(45), f59·f60(46), f61(47) — 교차 규칙에 따라 적용 대상 33·34·35·36 링크와 함께 / M. 안전: f62·f63(48), f18(49), f64(50, 연계 대상) / N. 보안·개인정보: f65·f66(51·52), f67·f68(53) / O. 검증·도입·수명주기: f69~f72(54·55), f73(57), f28(54) / P. 거버넌스·법규·사회: f76(58), f74(59, oq-292), f75·f49(60) / Q. 현장 유형별 적용: f80·f30·f48·f59(61 물류창고), f77·f78·f79·f19·f44(62 제조 공장), f25·f43(63 병원·의료), f26·f81·f18(64 상업 시설), f27·f82(65 가정·공동주택), f83(66 실외), f84(67 기타 현장). 벤더 주장 f2·f3·f79·f80 은 [추정]과 '벤더 주장' 병기. 연계 대상 f24·f64 와 승강기·문·PLC·센서 시뮬레이션 문장은 '연계 대상'으로 짧게. 보류 실행 1차 검증 수정 지시 반영: ref-833·ref-832 재사용, f33/f34·f37/f38·f39/f40 사실·추정 분리, f71 표현, ref-527 발행일 2025-01-06, ref-943 단독 인용. 아직 다루지 않은 연결: 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성(oq-129 관련 근거만 있음), 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육. 다음 실행 후보: 34·35 페이지(이전 분류 기준) 10절에 f9·f57·f59·f60·f62·f65·f74·f77 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "슬롯카 모델",
      "term_en": "Slotcar (Open-RMF simulated robot plugin)",
      "definition": "Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이고 장애물이 있으면 멈추는 단순화 로봇 모델로, 로봇마다 주행 스택을 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다."
    },
    {
      "term_ko": "대리 모델",
      "term_en": "Surrogate Model",
      "definition": "시뮬레이션처럼 계산 비용이 큰 모델의 입력–출력 관계를 학습한 근사 모델로, 추가 시뮬레이션 없이 설계 공간의 성능·비용을 빠르게 예측하는 데 쓴다."
    },
    {
      "term_ko": "동기화 손실",
      "term_en": "Synchronization Loss",
      "definition": "사람 작업자와 로봇이 함께 일하는 공정에서 한쪽이 다른 쪽을 기다리며 생기는 유휴 시간과 그 비용을 가리킨다."
    }
  ],
  "open_questions_new": [
    "대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 33. 시나리오 모델·편집, 13. 대화형 기능의 신뢰·기반 | 근거: f8 | 종류: 일반",
    "대화로 만든 다중 로봇 작업 계획을 사람이 승인하기 전에 시뮬레이션으로 실행 가능성을 미리 확인하는 절차를 플릿 오케스트레이션에 적용한 공개 사례가 있는가? | 관련 영역: 12. 채팅으로 업무 지시·오케스트레이션, 36. 가상 시운전·실제 상황 재현, 44. 로봇 기반 모델·언어 모델 계획 | 근거: f12 | 종류: 일반",
    "실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 52. 통신 보호·위협 관리·감사, 51. 인증·권한·격리 | 근거: f66 | 종류: 일반",
    "사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? | 관련 영역: 48. 안전·위험 관리, 34. 시뮬레이션·예측용 디지털 트윈, 19. 사람·보행자 모델 | 근거: f62 | 종류: 일반",
    "운영 기록으로 상황을 재현하기 전에 영상 기록을 익명화하면 재현 충실도가 얼마나 떨어지며, 국내 개인정보 처리 기준에서 재현용 기록을 어떻게 보관·공유해야 하는가? | 관련 영역: 53. 개인정보·영상 데이터, 36. 가상 시운전·실제 상황 재현 | 근거: f68 | 종류: 일반",
    "이동로봇 안전 표준(ISO 3691-4 등)이나 국내 인증 기관이 시뮬레이션·가상 시운전 결과를 안전 확인 근거로 인정하는 조건과 절차가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 36. 가상 시운전·실제 상황 재현, 54. 시험·형식 검증·벤치마크 | 근거: f64 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 63,
    "cross_checked_count": 0,
    "unverified": [
      "f2·f3·f79·f80 벤더 주장 수치·기능은 독립 출처로 확인하지 못함",
      "f28 클로봇·KETI 과제는 기사 1건 기준이며 과제 공고·성과 미확인",
      "f64 IEC 61508-7 C.5.19 문구는 업체 블로그 인용이며 표준 원문 미열람, ISO 3691-4 의 시뮬레이션 관련 조항은 확인하지 못함",
      "f48 Garg 외는 초록만 확인(WSC 2021 PDF 는 본문 추출 실패)",
      "f1·f49·f60 Howard 수치는 석사논문 초록의 저자 보고값이며 독립 재현 미확인",
      "f73 gz fuel download 의 -v 옵션이 모델 판 선택인지 출력 상세도인지 확인하지 못해 claim 에서 뺌",
      "IDTA 02005 1.0 발행일은 검색 결과상 2022-12 로 보이나 열람한 README 에 없어 published 를 null 로 둠",
      "Valiollahi 외(Scientific Reports 2026, ref-838) 원문은 이번에도 검색에서 찾지 못해 쓰지 않음",
      "운영자 교육용 다중 로봇 플릿 시뮬레이터(56. 운영 이관·확대·교육 연결) 근거 미확보",
      "oq-009 는 f49·f48 이 작업자 수와 AMR 비율을 함께 다룬 부분 근거만 제공(교대조 단위 아님), 해결 제안하지 않음",
      "oq-129 는 f1(비용 최소화 목적)이 부분 근거, 목적 결정 주체는 미확인"
    ],
    "scope_violations": [
      "f24: 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역 — claim 을 '연계 대상: '으로 시작",
      "f64: 안전 인증·기능안전 판정은 안전 인증 기관·제조사 몫 — '연계 대상: '으로 시작",
      "f21·f25·f26·f27: 승강기·문 제어 자체는 시설·설비 제어 경계의 연계 대상, ROP 는 요청·상태 확인과 제약 입력만",
      "f2·f70·f78: PLC·컨베이어 제어 코드 가상 시운전은 설비 업체·통합자 몫(연계 대상), ROP 가상 시운전의 방법 근거로만 사용",
      "f3·f22·f47·f61: 로봇 자체 주행·인식·파지 거동, 센서 시뮬레이션, 현실 격차 보정은 로봇 제조사·시뮬레이터 제공자 쪽 연계 대상",
      "f62·f63: 안전 인증·설비 안전 제어는 연계 대상, 시나리오가 위험 식별 입력이 될 수 있다는 범위로만 서술",
      "f67: 익명화 도구는 자율주행 생태계 도구로 ROP 직접 범위 아님, 재현용 기록 처리 경계의 참고로만"
    ],
    "budget_used": {
      "queries": 11,
      "sources": 14
    },
    "limits": "web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행. 같은 대상의 실행 2026-10-09-04 는 1차 검증 조건부 승인 뒤 형식 검증 실패로 보류되었으므로, 그 브리프의 finding 을 이번 브리프의 새 finding 으로 다시 적고(evidence_excerpt 끝 '(재인용: 2026-10-09-04)') 1차 검증 수정 지시를 이행했다: Chat2Scenic·Xia 논문은 새 id 대신 기존 ref-833·ref-832 를 재사용, 옛 f15·f18·f19 를 사실·추정으로 분리(f33/f34, f37/f38, f39/f40), SRCC 표현을 'CVPR 2019 챌린지에서 쓰인 Habitat 설정'으로 정정(f71), ref-527 발행일을 원문 열람으로 2025-01-06 확인, 옛 f14 를 출처별로 분리(f30·f31·f32), Lee 외 병원 논문은 ref-943 하나로만 인용, '실행 불가'를 '컴파일 실패'로(f8). 보류 실행이 새로 매겼던 ref-1331(Huck)·ref-1332(Carr)는 게시되지 않아 이번 예약 구간의 ref-1303·ref-1304 로 다시 부여했다(같은 URL 이 이미 등록돼 있으면 퍼블리셔 병합). 검색 11회/30, 신규 출처 14건/15(ref-1303~ref-1316, 예약 구간 안), 재사용 49건. 원문 열람: 신규 14건 모두 열었고(arXiv·학회 초록, 기사, github_raw README), 재사용 가운데 ref-104·ref-105·ref-406·ref-407·ref-831·ref-1087(github_raw), ref-1096·ref-527(webfetch)을 다시 열었다. 나머지 재사용 41건은 열지 않아 fetched false·source_unopened true 이고 그 출처에 기댄 finding 에도 표시했다. 입력 참고문헌 요약에 신뢰도 열이 없어 재사용 출처 reliability 는 researcher.md 5절 유형 기준으로 적었다. 교차 확인 0건(연결 주장이 대부분 단일 출처이거나 서로 다른 내용의 출처 조합). 벤더 주장 4건(f2·f3·f79·f80). 보류 실행의 '아직 다루지 않은 연결' 가운데 29·30·31·41·43·45·46·50·53·57·58·60·12·8·17·66·67 연결을 새로 채웠고, 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성, 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육은 근거를 찾지 못해 남긴다. 분류 원문 핵심 질문에는 별도 답 finding 을 내지 않고 연결 근거로 f69(배치 전 시뮬레이션 이점)·f71(예측력 한계)·f24(실데이터 검증 부족)·f77(현장 시험 전 배치 변경 검증)을 제시했다. 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)은 f16·f38 에서 구분했고, 디지털 트윈 동기화 보안(f66)은 36. 가상 시운전·실제 상황 재현의 경로로만 서술했다. L. AI·학습 기술 연결(f15·f57~f61)은 적용 대상인 33·34·35·36 과 함께 제안했다. 한국 자료: 신규 ref-1310·ref-1316(기사), 재사용 ref-1131·ref-409·ref-106·ref-516·ref-526. 현장 유형: 물류창고·제조 공장·병원·상업 시설·가정·실외·기타 각 1건 이상. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음. 해결 제안한 열린 질문 없음."
  }
}
```

### runs/2026-10-09-07/verification.json

```json
{
  "run_id": "2026-10-09-07",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 Cal Poly 석사논문 페이지 열람 확인: Howard, T. L., MS Industrial Engineering, 2026-06, 지도교수 Awwad. 처리량 최대화 산정이 RaaS 구독 과금에서 플릿을 '과대 산정'한다는 주장, FlexSim 완전요인 DES 27,000회, U자형 라인당 비용, 비용 최소 AMR:피커 비율 1→2.5 모두 초록과 일치. 저자 보고값, 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 36 페이지 5절 벤더 주장 재인용, 이번 실행에서 원문을 열지 않음(원문 미열람). 18%·5주는 기준선 미공개. 컨베이어·피킹 모듈 제어 에뮬레이션은 설비 업체·통합자 쪽 연계 대상."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 보류 실행 1차 검증과 이번 브리프 모두 NVIDIA 블로그를 열어 발행일 2025-01-06 확인(보류 실행 수정 지시 이행). 센서 시뮬레이션·합성 데이터는 시뮬레이터 제공자 쪽 연계 대상."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1092 원문 미열람(33 페이지 9절 재인용). 등록 정보와 시뮬레이션 모델을 잇는 사례 미확인 단서 유지."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 IDTA 공식 저장소 README(1/0) 열람 확인: 1.0 판이 IDTA 공식 발행 첫 판, 주 대상 DAE 모델·CAD·FMEA 포함(FEM 제외), 시뮬레이터별 파일·소스 코드·FMI 같은 교환 형식, 현재 사용 사례(모델 검색, 제조사·유통사에 모델 파일 요청), 향후 단계(자동 통합, BOM 기반 전체 시뮬레이션). README 에 IDTA 번호(02005)와 발행일은 없음 — published null 유지, 번호는 제목 표기로만 둔다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1133·ref-1127 원문 미열람(재인용). 두 체계의 대응 자료 미확인(oq-156) 단서 유지."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 수정 지시대로 기존 ref-833 재사용 확인. 보류 실행 1차 검증이 arXiv 2607.14387 초록 열람으로 CSR 76.42%·30.08%·16.26%, 123개 시나리오 확인. 이번 실행은 원문 미열람. 자율주행 대상임을 본문에 유지."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-833 재사용, '실행 불가'를 '컴파일 실패'로 고친 수정 이행 확인. ref-528 은 입력 원문 텍스트로 장애 매개변수 선언 확인, ref-1088 원문 미열람."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "기존 ref-832 재사용 확인. 보류 실행 1차 검증이 arXiv 2608.23622 초록 열람으로 확인(ETFA 2026 채택, 제약 공정). 이번 실행 원문 미열람. 로봇 플릿 대상 아님 단서 유지."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 두 근거 모두 로봇 플릿 대상이 아님을 본문에 밝힌다. 원문 미열람(재인용)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2307.06135 열람 확인: CoRL 2023 구두 발표, 장면 그래프 시뮬레이터 피드백 반복 재계획, 최대 3개 층·36개 방·140개 자산·물체. 다만 초록은 '두 대형 환경에서 평가하고 이동 매니퓰레이터로 실행을 시연'이라 적으므로 '이동 매니퓰레이터로 평가했다'는 표현을 고쳐야 한다(required_fixes)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 단일 로봇 대상 연구에서 끌어낸 해석이며, 원문 C 주석의 '사람이 확인·승인한 계획만 실행'과의 순서 관계도 해석임을 유지."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-406 원문 텍스트로 building_map_generator 의 gazebo·nav 두 모드 확인. 대화형 지도 작성과의 연결은 해석."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406·ref-079 원문 텍스트 대조 확인: .building.yaml 에서 층별 바닥·벽 메시와 문·승강기 sdf 요소 생성, 주석 수정 후 재생성, nav 모드 주행 그래프. 두 출처 같은 기관이라 교차 확인 아님."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(보류 실행 f6 과 같음). ref-815·ref-1089 원문 미열람. L. AI·학습 기술 연결은 44 와 적용 대상 33 을 함께 링크."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-291 원문 미열람, E. 사물·사람·실시간 상태 대분류 페이지 연결 절의 같은 주장과 같은 각주 재사용. 근거가 제조 대상이라는 한계 병기. 18=현재 상태 표현, 34=가정한 미래 실험 구분과 일치."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 1차 검증이 arXiv 2310.08710 초록 열람으로 확인. 이번 실행 원문 미열람. 자율주행 대상이며 로봇 현장 사례 아님 단서 유지(oq-256)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 텍스트(crowdsim 선택 기능, menge, rmf_traffic_editor 에서 활성)와 검증 중 rmf_demos README 열람(공항 터미널 use_crowdsim:=1) 확인. 같은 기관 자료라 독립 교차 아님. 공항은 33 페이지와 같이 상업 시설로 둔다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 ARIAC_docs scenario.rst 열람 확인: Li-Ion·Ni-MH, 찌그러짐·긁힘·부풂 결함, 4셀 키트, 셀 전압 ±0.2 V 밖은 재활용 통, 키트 총전압 4·Vcell ±0.15 V, 결함·전압·종류·총전압 검사, AGV 이동 전 키트 품질 확인 서비스. 경진대회 시뮬레이션이며 실제 공장 아님."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ARIAC 시나리오에서 끌어낸 해석, 공통 형식 미확인 단서 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 텍스트 대조 확인: /door_requests 의 DoorRequest, /lift_requests 의 LiftRequest 에 응답, door_supervisor 의 문 충돌 방지, lift_supervisor 의 다플릿 요청 관리. 실제 승강기·문 제어는 시설·설비 제어 경계의 연계 대상."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 텍스트 대조 확인: PathRequest·ModeRequest 구독, 레일식 직선 주행, 장애물 감지 시 정지, 주행 스택 계산 부담 회피. 로봇 자체 주행 거동 충실도는 연계 대상."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "34 페이지 7·11절 검증된 주장 재인용, 두 출처 원문 미열람. 두 출처는 서로 다른 부(제1부·제6부)이며 교차 확인 아님."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·'연계 대상:' 표시 유지. ref-521 원문 미열람(34 페이지 재인용). 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 5절 검증된 [사실] 재인용, 이번 실행 원문 미열람. 보류 실행 수정 지시대로 ref-943 단독 인용(ref-060 은 같은 논문). 승강기 제어는 연계 대상."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "35 페이지 9절 검증된 [사실] 재인용, 원문 미열람. 승강기 제어는 연계 대상."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "F. 연동 대분류 페이지 검증된 [사실] 재인용, 원문 미열람. 대상이 공동주택(현장 유형 가정)임을 유지."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 파이낸스스코프 기사 열람 확인(윤영훈, 2025-07-11): 산업통상자원부 국가로봇테스트필드 기술개발 협약, 54억원, KETI 공동, 클로봇은 FMS 요소기술·로봇–디지털 트윈·시뮬레이터 인터페이스, KETI 는 실환경 연동 디지털 트윈 증강 시뮬레이션, 2028년까지, 테스트필드 적용은 목표. 기사 1건(회사 선정 발표 보도)이며 과제 공고·성과 미확인 — '보도에 따르면'·'목표' 표현 유지. 기능·성능 주장이 아니므로 벤더 주장 병기 대상은 아님."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "검증 중 vda5050-sim README 열람: 3.0.0 주 대상, 2.1.0·2.0.0·1.1.0 구형 판 흉내, 메시지 스키마가 공식 3.0.0 JSON 스키마 위에 세워지고 동작은 적합성 시험 묶음으로 검증, 로봇별 MQTT 또는 NATS 연결은 일치. 그러나 기본 로봇은 'AGV 5종'이 아니라 Spot·Go2·TIAGo·H1·PiDog 로봇 원형 5종(사족 보행·휴머노이드·모바일 매니퓰레이터 등)이다. '기본 5종 AGV' 구절은 삭제하고, 남는 진술만 개인 프로젝트 README 의 자기 기술로 쓴다(공식 적합성 시험 아님)."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "35 페이지 3절 검증된 [사실] 재인용, 원문 미열람. 보류 실행 수정 지시대로 출처별로 분리(f30·f31·f32) 확인."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "35 페이지 4·10절 검증된 [사실] 재인용, 원문 미열람. 결과 수치는 쓰지 않음."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "35 페이지 10절 검증된 [사실] 재인용, 원문 미열람."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문 텍스트(ref-105 config.yaml) 대조 확인: recharge_threshold 0.10 'Battery level below which robots in this fleet will not operate', recharge_soc 1.0, task_capabilities loop·delivery. 보류 실행 수정 지시대로 설정값 문장만 [사실]로 분리."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(35 페이지 10절에서도 [추정]). 보류 실행 f15 분리 지시 이행."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "G. 계획·최적화 대분류 페이지 검증된 [사실] 재인용, 원문 미열람. 저자 계산 실험 조건·독립 재현 미확인 단서 유지."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "34 페이지와 G 대분류 페이지 검증된 [사실] 재인용, 두 출처 원문 미열람. 도구와 연구로 서로 다른 내용이며 교차 확인 아님. 시뮬레이션 결과임을 유지."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "34 페이지 5절 검증된 [사실] 재인용, 원문 미열람. 보류 실행 f18 분리 지시대로 연구 존재만 [사실]."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(G 대분류 페이지의 위치 판단과 같음). 34=가정한 미래 실험 구분과 일치."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 1차 검증이 벤치마크 페이지를 열어 지도별 시나리오 파일(even·random 각 25개) 제공 확인. 이번 실행 원문 미열람. 보류 실행 f19 분리 지시 이행."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 벤치마크 페이지가 비교 목적을 명시하지 않는다는 지적 반영."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-116·ref-1090 원문 미열람(33 페이지 재인용). ref-1090 은 벤더 문서 유형이나 기능·성능 주장이 아님."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 1차 검증이 arXiv 2608.26066 초록 열람으로 확인(실제·가상 로봇 작업 배정 예제, 컨테이너 배포). 이번 실행 원문 미열람."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지, 의견 주체 Lee 외 저자 명시. 36 페이지 5절 재인용, 원문 미열람. ref-943 단독 인용."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문 텍스트(ref-528 challenges.rst) 대조 확인: 컨베이어 고장(START_TIME·DURATION), 전압 시험기 고장(TESTER), 진공 그리퍼(GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID). 경진대회 시나리오이며 실제 공장 아님."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 vda5050-sim README 열람 확인: 로봇별 연결 끊김·오류 주입·필드 위반·서비스 모드·비상 정지 확률, 실패 동작의 RETRIABLE 상태와 retry·skip 흐름. 개인 프로젝트의 자기 기술이며 공식 적합성 시험 아님."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 텍스트 대조 확인: TeleportDispenser 는 DispenserRequest 에 적재물을 가장 가까운 로봇 위로, TeleportIngestor 는 IngestorRequest 에 로봇 적재물을 자기 위치로 순간 이동."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 원문은 '향후 실제 워크셀·로봇팔로 대체돼도 메시지 교환은 같다'고 적어 해석을 뒷받침. 파지·적재 물리 시뮬레이션은 연계 대상."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 Emerald 페이지 열람 확인: Garg·Maywald·Naman, IJRDM 53(10-11) 1123–1138, 온라인 2025-10-14, DES 48개 구성, AMR:피커 약 2:1 에서 처리량·효율 최고, 교차 통로의 처리량 효과 유의하지 않음, 사후 비용 효율 1,200 시나리오. 저자 시뮬레이션 조건."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "초록 열람 확인: 피커 유휴가 교대당 AMR 유휴보다 평균 2.5배 비쌈, 동기화 손실의 경제적 영향이 주로 노동 쪽, 3구역 순차 구역제·연속 도착 조건에서 세 배차 휴리스틱 선택이 라인당 비용에 유의한 영향 없음. 원문은 '작업자'가 아니라 '피커(picker)'. P. 거버넌스·법규·사회의 60. 노동·수용성·접근성 연결은 노동 비용 측면일 뿐 수용성 근거가 아님."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 rosbag2 README(rolling) 열람 확인: 기본 저장 mcap, ~/set_rate, --clock, --topics, -i 여러 백 파일을 원래 수신 시각순으로 재생(--message-order 로 발행 시각 기준 전환 가능), 시작 시각은 ~/play 서비스."
    },
    {
      "finding_id": "f51",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 오케스트레이션 기록→시나리오 변환 형식 미확인(oq-131) 단서 유지."
    },
    {
      "finding_id": "f52",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 두 출처 원문 미열람(35 페이지 10절 재인용). oq-011 연결."
    },
    {
      "finding_id": "f53",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 rmf_demos README 열람 확인: server_uri 를 ws://localhost:8000/_internal 로 지정하면 플릿 어댑터가 rmf-web api-server 에 최신 작업·로봇 상태를 보냄, Docker 대시보드는 실행 중 재설정 불가이며 빠른 연동·시험용."
    },
    {
      "finding_id": "f54",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 시운전 절차로 정리한 공개 사례 미확인(oq-255) 단서 유지."
    },
    {
      "finding_id": "f55",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(보류 실행 f13 과 같음). 플랫폼 배치 근거 없음(oq-040). ref-1129 원문 미열람."
    },
    {
      "finding_id": "f56",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 MCAP 명세 열람 확인: Message 의 log_time·publish_time, Chunk Index 의 message_start_time·message_end_time(청크 안 최초·최종 기록 시각), 채널별 message_encoding. rosbag2 기본 저장 mcap 확인. 두 출처는 형식 정의와 채택으로 서로 다른 내용."
    },
    {
      "finding_id": "f57",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 1차 검증이 arXiv 2312.09067 초록 열람으로 확인(CVPR 2024). 이번 실행 원문 미열람. L. AI·학습 기술의 44 와 적용 대상 33 을 함께 링크."
    },
    {
      "finding_id": "f58",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "34 페이지가 인용한 자료 재인용, 원문 미열람. 로봇 플릿 시뮬레이션에 쓴 사례 미확인 단서 유지. L. AI·학습 기술의 45 와 적용 대상 34 를 함께 링크."
    },
    {
      "finding_id": "f59",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2404.08006 열람 확인: 피커와 AMR 이 피킹 위치에서 만남, 불확실성 아래 다목적 심층 강화학습 배정, 그래프 모델, DES 로 학습·평가, 효율·공정성 모두 비교 방법 우위, 다른 크기 창고로 일반화, 코드 공개. 프리프린트."
    },
    {
      "finding_id": "f60",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "초록 열람 확인: 반개방형 대기행렬 모델이 시뮬레이션 라인당 비용을 약 5% 안에서 재현, XGBoost 대리 모델이 교차 검증에서 3% 안, 등각 예측 구간. 저자 보고값, 독립 재현 미확인."
    },
    {
      "finding_id": "f61",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(36 페이지 9절 경계와 같음). ref-741·ref-1127 원문 미열람. 현실 격차 보정은 연계 대상."
    },
    {
      "finding_id": "f62",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2011.10294 열람 확인: Huck·Ledermann·Kröger, 2020-11-20, SPCE 2020, 사람 모델+최적화로 고위험 사람 행동 생성, 물리 시제품 이전 위험 식별, 무작위·몬테카를로 탐색의 한계, 산업용 로봇 셀 개념 증명. 협동 로봇 셀 대상."
    },
    {
      "finding_id": "f63",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1086 원문 미열람. 안전 인증·설비 안전 제어는 연계 대상, 위험 식별 입력 범위로만 서술."
    },
    {
      "finding_id": "f64",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 Wind River 블로그 열람 확인(2014-11-20, Engblom 이 Buchwieser 인터뷰): IEC 61508-7 C.5.19 정의 인용('mimics the behavior of the equipment under control (EUC)'), 안전 표준이 시뮬레이션·장애 주입을 강하게 권고한다는 해석은 Wind River 직원의 발언. 표준 원문 미확인이므로 [추정]·'연계 대상:' 유지, 표준 문구를 사실로 쓰지 않는다."
    },
    {
      "finding_id": "f65",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2211.09507 열람 확인: Carr·Wang·Wang·Han, 2022-11-17, ROS 기반 시스템 디지털 트윈에 대한 person-in-the-middle 공격이 산업용·이동 로봇의 물리적 실패로 이어질 수 있음, 완화 방안 논의. 프리프린트."
    },
    {
      "finding_id": "f66",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 로봇 플릿 플랫폼 적용 사례 없음. 동기화 경로를 36 쪽으로만 서술해 34 가 현재 상태를 표현한다고 쓰지 않은 점 확인."
    },
    {
      "finding_id": "f67",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 README 열람 확인: mcap·sqlite3 입력, GroundingDINO·OpenCLIP·SegmentAnything 2·YOLO 결합, 가우시안 블러, validation.json 의 prompt·should_inside(예: 차 안 번호판, 사람 몸 안 얼굴), GPU 메모리·처리 시간 경고. 자율주행 생태계 도구이며 ROP 직접 범위 아님."
    },
    {
      "finding_id": "f68",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 익명화가 재현 충실도에 주는 영향과 국내 개인정보 요건은 미확인."
    },
    {
      "finding_id": "f69",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-406 원문 텍스트 Motivation 절 대조 확인: 배터리·충돌 비용 없음, 반복 시나리오로 수정 확인, 드문 예외, 장시간 시뮬레이션의 시설 소유자 확신. 직접 인용은 출처당 1회 범위."
    },
    {
      "finding_id": "f70",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-1126·ref-1130 원문 미열람(36 페이지 재인용). PLC·설비 제어 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상."
    },
    {
      "finding_id": "f71",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 수정 지시대로 'CVPR 2019 챌린지에서 쓰인 Habitat 설정'으로 정정 확인. 보류 실행 1차 검증이 초록 열람(SRCC 0.18→0.844, 벽 미끄러짐). 이번 실행 원문 미열람."
    },
    {
      "finding_id": "f72",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 7절 검증된 [사실] 재인용, 이번 실행 원문 미열람. 발행일 2024-03-05."
    },
    {
      "finding_id": "f73",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 gz-fuel-tools README(main) 열람 확인: 로드맵에 'Think about how to detect when new versions of remote models have been uploaded'와 'Idea of a hash'. 판 선택 옵션 진술을 뺀 것은 적절."
    },
    {
      "finding_id": "f74",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보류 실행 1차 검증이 튜토리얼 열람으로 확인(CC BY 3.0 권장이며 요구 아님, author name·email 필수). 이번 실행 원문 미열람. oq-292 관련."
    },
    {
      "finding_id": "f75",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 GI 디지털 라이브러리 열람 확인: Kassem·Michahelles, Mensch und Computer 2022 워크숍(2022-09, Darmstadt), 협동 로봇이 공장·물류·제조에 들어오며 빠른 HRI 평가 필요, 소비자용 VR·AR 헤드셋으로 로봇을 흉내 낸 사용자 연구와 방향 제시. 이동로봇 플릿 수용성 측정 사례가 아님을 유지."
    },
    {
      "finding_id": "f76",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 서브모델 README 의 '제조사·유통사에 시뮬레이션 모델 파일 요청' 사용 사례 확인(f5). 로봇 플릿 조달 계약 사례 미확인."
    },
    {
      "finding_id": "f77",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 PMC(reCAPTCHA)·MDPI(403)가 열리지 않아 원문 재열람 실패. 검색 결과로 저자·제목·Sensors 21(23):7830·2021-11-25 와 '생산 홀 좁은 통로에서 디지털 트윈으로 AMR 운영 환경을 시험·개선한 사례 연구'는 확인. 도킹 복귀 시간 44 s → 22.5~23.3 s 와 홈 치수·속도 수치는 리서치 열람 기록(fetched webfetch)에만 기대며 검증 단계에서 대조하지 못함."
    },
    {
      "finding_id": "f78",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 5절 검증된 [사실] 재인용, 원문 미열람. PLC 코드 가상 시운전은 연계 대상이며 방법 근거로만 사용."
    },
    {
      "finding_id": "f79",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 검증 중 기사 열람 확인(남지완, 2026-08-14): 이차전지 분야 산업 AI 솔루션 실증확산, 한국생산기술연구원 주관·아바코 수요기업, AMR·4-way 셔틀 단일 관제, 실물 설비 전 가상 환경 검증, 다운타임 20% 절감·자동화율 90% 이상. 회사 발표 수치, 기준선·측정 방법 미공개."
    },
    {
      "finding_id": "f80",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. 34 페이지 5절 벤더 주장 재인용, 원문 미열람. 이후 적용 결과 미확인(oq-084·oq-117)."
    },
    {
      "finding_id": "f81",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 rmf_demos README 열람 확인: 호텔은 로비와 객실 2개 층, 승강기 2대·여러 문·플릿 3개(로봇 4대), 공항 터미널은 차선·목적지·로봇이 많은 대형 지도. 실제 시설 사례 아님."
    },
    {
      "finding_id": "f82",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "33 페이지 5절 검증된 [사실] 재인용, 원문 미열람. 벤치마크이며 실제 가정 배치 아님."
    },
    {
      "finding_id": "f83",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 rmf_demos README 열람 확인: 차선을 WGS84 로 주석한 대규모 캠퍼스 월드, 각 로봇이 WGS84 좌표로 위치를 보냄. 실제 캠퍼스 배치 아님."
    },
    {
      "finding_id": "f84",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "36 페이지 5절 검증된 [사실] 재인용, 원문 미열람. 시뮬레이션 시험 사례이며 현장 기록 재생은 다루지 않음."
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
      "f16(18. 실시간 세계 상태·데이터 일관성 ↔ 34. 시뮬레이션·예측용 디지털 트윈 구분)은 E. 사물·사람·실시간 상태·B. 로봇 온톨로지 대분류 페이지 연결 절의 같은 주장과 겹친다 — 같은 각주 ref-291 재사용, 모순 없음",
      "f21·f25·f26·f27 은 F. 연동 대분류 페이지 연결 절의 승강기·문·로봇 친화 공간 주장과 겹친다 — 같은 각주(ref-406·ref-943·ref-103·ref-409) 재사용",
      "f30~f38 은 A. 기획·사업·G. 계획·최적화 대분류 페이지(옛 분류 기준 연결)와 겹친다 — 같은 각주 재사용, 사실·추정 구분은 그 페이지를 따랐다",
      "ref-943 과 ref-060 은 같은 Lee 외 Digital Health 논문이다 — 이번 절은 ref-943 하나로만 인용(보류 실행 지시 이행)",
      "ref-833·ref-832 는 보류 실행에서 새 id(ref-1329·ref-1330)로 잘못 매겼던 논문의 기존 id 로, 이번 브리프가 재사용했다",
      "f55·f53 의 플랫폼 배치·API 연결은 K. 플랫폼 아키텍처·인프라 대분류 연결 실행(2026-10-09-06)의 f34·f35(rosbag2·기록 보존)와 방향이 반대인 같은 연결이다 — 모순 없음, 같은 각주 ref-831 재사용"
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
    "f29: '기본 5종 AGV 를 흉내 내' 구절을 쓰지 않는다 — README 의 기본 로봇은 AGV 가 아니라 Spot·Go2·TIAGo·H1·PiDog 로봇 원형 5종이다. 남는 진술은 'VDA 5050 3.0.0 을 주 대상으로 2.1.0·2.0.0·1.1.0 구형 판도 흉내 내고, 공식 3.0.0 JSON 스키마 위에 세운 메시지 스키마와 적합성 시험 묶음을 둔다고 README 에 적는다'로 쓰고, 개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아님을 밝힌다.",
    "f11: '이동 매니퓰레이터로 평가했다'를 '최대 3개 층·36개 방·140개 자산·물체의 두 대형 환경에서 평가하고 이동 매니퓰레이터로 실행을 시연했다'로 고친다 — 초록 표현이 그렇다. 단일 로봇 대상임을 밝힌다.",
    "f49: 원문 용어에 맞춰 '작업자'를 '피커(작업자)'로 쓰고, P. 거버넌스·법규·사회의 60. 노동·수용성·접근성 연결에 쓸 때는 '노동 비용 측면의 근거이며 수용성·노동 영향의 직접 근거는 아니다'를 밝힌다 — 논문은 비용 분석이다.",
    "f77: 수치(44 s → 22.5~23.3 s)는 저자 사례 연구의 보고값임을 밝히고 단정 표현을 쓰지 않는다 — 검증 단계에서 원문을 다시 열지 못해 수치를 대조하지 못했다.",
    "f2·f3·f79·f80: 본문에 [추정]과 '벤더 주장'을 병기하고 수치(18%·5주, 다운타임 20%·자동화율 90%)는 기준선·측정 방법 미공개임을 함께 쓴다. f28 은 '2025-07 보도에 따르면'과 '목표' 표현을 유지한다.",
    "f64: IEC 61508-7 C.5.19 문구는 Wind River 블로그 인터뷰(2014)의 인용으로만 쓰고 '연계 대상:'으로 시작하는 [추정] 문장 하나로 짧게 둔다. '안전 표준이 시뮬레이션·장애 주입을 강하게 권고한다'는 업체 직원의 해석임을 밝힌다 — 표준 원문은 확인하지 않았다.",
    "각주 원문 미열람 표기: ref-833, ref-832, ref-1088, ref-1127, ref-1092, ref-1133, ref-815, ref-1089, ref-291, ref-1128, ref-516, ref-518, ref-521, ref-943, ref-103, ref-409, ref-102, ref-098, ref-109, ref-381, ref-101, ref-398, ref-267, ref-1091, ref-116, ref-1090, ref-1129, ref-106, ref-741, ref-241, ref-1086, ref-1126, ref-1130, ref-1231, ref-1131, ref-526, ref-971, ref-1134, ref-1165 의 각주 정의는 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다. ref-528·ref-079·ref-105·ref-406 은 입력 원문 텍스트로, ref-104·ref-407·ref-831·ref-1087·ref-1096·ref-527·ref-1303~ref-1316 은 이번 실행에서 열었으므로 표기하지 않는다(ref-1307 은 리서치 열람 기록 기준).",
    "ref-527 각주 발행일을 2025-01-06 으로 쓰고(참고문헌의 '미확인'을 정정), ref-1314 의 발행일은 '미확인'으로 둔다 — README 에 발행일·IDTA 번호가 없다.",
    "범위 경계 문구: f21·f25·f26·f27 의 승강기·문 제어, f2·f70·f78 의 PLC·컨베이어 제어 코드 가상 시운전, f3·f22·f47·f61 의 로봇 자체 주행·센서 시뮬레이션·파지 물리·현실 격차 보정, f62·f63 의 안전 인증·설비 안전 제어는 각 문장에서 '연계 대상'으로 짧게 밝힌다. f24·f64 는 '연계 대상:'으로 시작하는 문장 그대로 둔다 — 분류 원문 19장.",
    "18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈: f16 으로 '18 은 현재 상태 표현, 34 는 가정한 미래 실험'을 E. 사물·사람·실시간 상태 항목에 밝히고, f65·f66 의 디지털 트윈 동기화는 36. 가상 시운전·실제 상황 재현의 경로로만 서술한다. 34 가 현재 상태를 표현한다고 쓰지 않는다.",
    "C. 채팅 기반 구성·운영 항목(f7~f13)은 분류 원문 4장 주석에 따라 대화 기능과 짝을 이루는 엔진(시나리오 구성·실제 상황 재현은 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현, 맵 작성은 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델, 업무 지시는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링)과 함께 읽도록 연결한다. f7·f9·f11 이 자율주행·제약 공정·단일 로봇 대상임을 밝힌다.",
    "L. AI·학습 기술 연결(f15·f57~f61)은 44. 로봇 기반 모델·언어 모델 계획, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 링크와 적용 대상인 33·34·35·36 링크를 함께 둔다 — 공통 규칙 5(교차 규칙).",
    "f43 은 [의견]으로 두고 의견 주체(Lee 외 저자)를 문장에 밝힌다. f23 의 두 출처(ref-516·ref-518)는 서로 다른 부를 가리키므로 교차 확인된 것처럼 묶어 쓰지 않는다. f30·f31·f32 와 f36 도 출처별로 각자의 각주를 붙인다.",
    "'아직 다루지 않은 연결'은 브리프 finding 이 실제로 다루지 않은 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성(oq-129 관련 부분 근거만 있음), 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육으로 적는다. '모든 대분류와 연결' 같은 완전성 표현은 쓰지 않는다.",
    "다른 대분류·세부영역은 새 17개 대분류 기준의 문자+이름, 번호+이름으로 쓴다(예: 'F. 연동', '25. 작업 배정 — MRTA'). A·B·F·G 대분류 페이지의 옛 대분류 이름(예: 'C. 연결·실행 기반', 'F. 도입·검증·유지관리')을 옮겨 쓰지 않는다.",
    "Q. 현장 유형별 적용 항목은 현장 유형을 이름으로 밝히고(물류창고·제조 공장·병원·상업 시설·가정·실외·기타), 예제 월드·벤치마크·경진대회 시나리오(f18·f19·f44·f81~f84)는 실제 현장 배치가 아님을 밝힌다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 83건, 미확인 1건(f29: '기본 5종 AGV' 구절이 README 와 다름), 교차 확인 0건. 강등: f29 일부 구절 삭제(남는 진술만 [사실]). 원문 미열람 출처: ref-833, ref-832, ref-1088, ref-1127, ref-1092, ref-1133, ref-815, ref-1089, ref-291, ref-1128, ref-516, ref-518, ref-521, ref-943, ref-103, ref-409, ref-102, ref-098, ref-109, ref-381, ref-101, ref-398, ref-267, ref-1091, ref-116, ref-1090, ref-1129, ref-106, ref-741, ref-241, ref-1086, ref-1126, ref-1130, ref-1231, ref-1131, ref-526, ref-971, ref-1134, ref-1165. 주의: 이 절의 연결은 대부분 단일 출처이거나 게시된 세부영역 페이지의 재인용에 기대며, 연결 해석 30건은 [추정], 1건은 [의견]이다. 다중 로봇 플릿 오케스트레이션에 직접 적용된 근거는 Open-RMF 시뮬레이션 문서·예제 월드, VirTooS, vda5050-sim(개인 프로젝트) 정도다. 대화형 시나리오 생성(자율주행), 언어 모델 비교 실험(제약 공정), 실행 전 시뮬레이터 확인(단일 이동 매니퓰레이터), 시뮬레이션 예측력(LoCoBot 주행), 디지털 트윈 공격(ROS 로봇) 근거는 로봇 플릿이 아닌 대상에서 나왔다. 벤더 주장 4건(f2·f3·f79·f80)은 독립 확인되지 않았다. Stączek 외(ref-1307)의 도킹 시간 수치는 검증 단계에서 원문을 다시 열지 못해(PMC 보안 확인·MDPI 403) 리서치 열람 기록에만 기댄다. 브리프 출처 표시 어긋남: ref-528·ref-079 는 fetched true 인데 요약이 '원문 미열람.'으로 시작하고 fetch_url 이 비어 있다(입력의 data/source_texts 원문으로 열람 확인). 보류 실행 2026-10-09-04 의 1차 수정 지시(ref-833·ref-832 재사용, 사실·추정 분리, SRCC 표현, ref-527 발행일, ref-943 단독 인용, '컴파일 실패')는 이행됐다. 정정 요청 없음. 열린 질문 해결 인정 없음. 검증 검색 2회(리서치 11회와 합쳐 13/30), 열람 21회.",
  "retry_reason": null
}
```

### runs/2026-10-09-07/pages.json

```json
{
  "run_id": "2026-10-09-07",
  "outline": [
    {
      "path": "docs/categories/design-and-simulation/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 12000,
      "summary": "I. 설계·시뮬레이션의 네 세부영역이 다른 대분류 16곳의 모델·기록·인터페이스를 받아 가상 실험을 하고 결과를 계획·도입·운영 결정으로 넘기는 연결을 대분류 문자 순으로 적는다. 예: 35. 처리능력·규모·배치 설계의 대수 산정을 주문 라인당 비용 최소화로 바꾸면 A. 기획·사업의 서비스형 로봇 과금 판단과 이어진다. [사실][^ref-822]",
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
        "f49",
        "f50",
        "f51",
        "f52",
        "f53",
        "f54",
        "f55",
        "f56",
        "f57",
        "f58",
        "f59",
        "f60",
        "f61",
        "f62",
        "f63",
        "f64",
        "f65",
        "f66",
        "f67",
        "f68",
        "f69",
        "f70",
        "f71",
        "f72",
        "f73",
        "f74",
        "f75",
        "f76",
        "f77",
        "f78",
        "f79",
        "f80",
        "f81",
        "f82",
        "f83",
        "f84"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/design-and-simulation/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 작성: 다른 대분류 16곳과의 연결(finding 84건, 각주 63건), 아직 다루지 않은 연결 6개 영역 명시, 1차 조건부 승인 수정 16건 반영",
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
              "ref-241",
              "ref-267",
              "ref-291",
              "ref-381",
              "ref-398",
              "ref-406",
              "ref-407",
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
              "ref-1087",
              "ref-1088",
              "ref-1089",
              "ref-1090",
              "ref-1091",
              "ref-1092",
              "ref-1096",
              "ref-1126",
              "ref-1127",
              "ref-1128",
              "ref-1129",
              "ref-1130",
              "ref-1131",
              "ref-1133",
              "ref-1134",
              "ref-1165",
              "ref-1231",
              "ref-1303",
              "ref-1304",
              "ref-416",
              "ref-1306",
              "ref-1307",
              "ref-1308",
              "ref-1309",
              "ref-1310",
              "ref-1311",
              "ref-1312",
              "ref-1313",
              "ref-1314",
              "ref-822",
              "ref-1316"
            ]
          },
          "content": "(절 본문 생략 — runs/2026-10-09-07/pages/categories/design-and-simulation/index.md 의 해당 절을 본다)"
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | I. 설계·시뮬레이션 | '다른 대분류와의 연결' 절 작성(다른 대분류 16곳, 각주 63건, 1차 조건부 승인 수정 16건 반영, 보류 실행 2026-10-09-04 대체) | run 2026-10-09-07",
  "index_updates": {
    "home_recent": "2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 작성(다른 대분류 16곳과의 연결, 연결 해석은 대부분 추정·단일 출처, 벤더 주장 4건 병기)",
    "category_recent": "2026-10-09 — I. 설계·시뮬레이션: '다른 대분류와의 연결' 절 작성(33. 시나리오 모델·편집~36. 가상 시운전·실제 상황 재현과 다른 대분류 16곳의 연결, 아직 다루지 않은 연결 6개 영역 명시)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "slotcar",
      "term_ko": "슬롯카 모델",
      "term_en": "Slotcar (Open-RMF simulated robot plugin)",
      "definition": "Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이고 장애물이 있으면 멈추는 단순화 로봇 모델로, 로봇마다 주행 스택을 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다.",
      "related_areas": [
        34,
        20
      ],
      "sources": [
        "ref-406"
      ]
    },
    {
      "action": "new",
      "slug": "surrogate-model",
      "term_ko": "대리 모델",
      "term_en": "Surrogate Model",
      "definition": "시뮬레이션처럼 계산 비용이 큰 모델의 입력–출력 관계를 학습한 근사 모델로, 추가 시뮬레이션 없이 설계 공간의 성능·비용을 빠르게 예측하는 데 쓴다.",
      "related_areas": [
        35,
        46
      ],
      "sources": [
        "ref-822"
      ]
    },
    {
      "action": "new",
      "slug": "synchronization-loss",
      "term_ko": "동기화 손실",
      "term_en": "Synchronization Loss",
      "definition": "사람 작업자와 로봇이 함께 일하는 공정에서 한쪽이 다른 쪽을 기다리며 생기는 유휴 시간과 그 비용을 가리킨다.",
      "related_areas": [
        31,
        35
      ],
      "sources": [
        "ref-822"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-833",
      "org": "Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J.",
      "title": "Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving",
      "published": "2026-07-15",
      "url": "https://arxiv.org/abs/2607.14387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 챗봇 대화와 검색 증강으로 자율주행 시나리오 DSL 스크립트를 생성하고 컴파일 성공률을 보고한 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-832",
      "org": "Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P.",
      "title": "LLM Agents Perform Controlled Experiments Using Simulation Models",
      "published": "2026-08-22",
      "url": "https://arxiv.org/abs/2608.23622",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 에이전트가 시뮬레이션 비교 실험을 설계·실행·해석하는 틀을 제약 공정 설계에 적용(ETFA 2026 채택).",
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
      "summary": "원문 미열람. 도로 교통 시나리오의 동적 내용을 기술하는 표준 소개 페이지.",
      "source_unopened": true,
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
      "summary": "ARIAC 의 장애(컨베이어·전압 시험기·그리퍼)와 긴급 주문을 매개변수로 선언하는 과제 문서(입력 원문 텍스트로 열람 확인).",
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
      "summary": "원문 미열람. 시뮬레이션–현실 상관 계수(SRCC)를 제안하고 시뮬레이터 매개변수 조정으로 예측력을 높인 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-416",
      "org": "Rana, K., Haviland, J., Garg, S., Abou-Chakra, J., Reid, I., & Suenderhauf, N. (CoRL 2023, arXiv)",
      "title": "SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning",
      "published": "2023-07-12",
      "url": "https://arxiv.org/abs/2307.06135",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "3차원 장면 그래프로 언어 모델 계획을 근거 짓고, 실행 전 장면 그래프 시뮬레이터 피드백으로 계획을 반복 수정하는 방법(CoRL 2023 구두 발표). 초록 기준.",
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
      "summary": "Open-RMF 시뮬레이션의 동기, slotcar·문·승강기·Teleport 플러그인, building_map_generator, crowdsim 을 설명하는 장.",
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
      "summary": "건물 파일에 차선·문·승강기·충전기를 주석하는 traffic-editor 설명(입력 원문 텍스트로 열람 확인).",
      "source_unopened": false,
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
      "summary": "원문 미열람. 로봇·환경을 시뮬레이터용으로 기술하는 XML 형식.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1314",
      "org": "IDTA (Industrial Digital Twin Association, admin-shell-io/submodel-templates)",
      "title": "Provision of Simulation Models (IDTA 02005) 1.0 — README",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "자산관리셸로 자산의 시뮬레이션 모델 파일을 모델 유형·사용법·적용 분야와 함께 제공하게 하는 IDTA 공식 서브모델 템플릿의 저장소 README(명세 본문 아님, 발행일·IDTA 번호는 README 에 없음).",
      "source_unopened": false,
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
      "summary": "원문 미열람. 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준.",
      "source_unopened": true,
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
      "summary": "원문 미열람. 언어 지시로 3D 체화 AI 환경을 생성하는 방법(CVPR 2024).",
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
      "summary": "원문 미열람. 생성 모델 기반 환경 생성을 포함한 ROS 2 사람 중심 주행 벤치마크 플랫폼.",
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
      "summary": "원문 미열람. 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분한 제조 분야 문헌 검토.",
      "source_unopened": true,
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
      "summary": "원문 미열람. 실제 주행 기록으로 다중 에이전트 시뮬레이션을 초기화·재생하는 데이터 기반 시뮬레이터.",
      "source_unopened": true,
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
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 예제 월드(호텔·사무실·공항 터미널·클리닉·캠퍼스·제조·물류)와 작업 명령, rmf-web 대시보드 연결, crowdsim, 화재 경보 동작을 설명.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1087",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC Documentation — Scenario",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ARIAC 배터리 생산 시설 시나리오의 셀·결함·키트·모듈·설비와 키트·모듈 제출 검사를 설명.",
      "source_unopened": false,
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
      "summary": "원문 미열람. 제조용 디지털 트윈 프레임워크 ISO 23247 제1부의 국내 KS 부합 표준.",
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
      "summary": "원문 미열람. 디지털 트윈 결합을 다루는 ISO 23247 제6부.",
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
      "summary": "원문 미열람. 물류·공급망 디지털 트윈 문헌 검토와 개념 틀, 실데이터 검증 연구가 소수임을 보고.",
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
      "summary": "원문 미열람. 병원 약품 배송 로봇 실제 기록과 몬테카를로 재현으로 승강기 가동률과 배송 실패의 관계를 분석.",
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
      "id": "ref-1310",
      "org": "파이낸스스코프 (윤영훈)",
      "title": "클로봇, 국책사업으로 피지컬AI 기술 표준 이끈다...산자부 주관사 선정",
      "published": "2025-07-11",
      "url": "https://www.finance-scope.com/article/view/scp202507110007",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "클로봇이 산업통상자원부 국가로봇테스트필드 기술개발 과제(54억원) 주관기관으로 KETI 와 디지털 트윈 연동 증강 실험 기술을 2028년까지 개발한다는 보도.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 로봇 플릿 시뮬레이터 README: 구형 판 흉내, 로봇별 고장 프로필, 공식 JSON 스키마 위의 메시지 스키마와 적합성 시험 묶음(개인 프로젝트의 자기 기술, 기본 로봇은 AGV 가 아닌 로봇 원형 5종).",
      "source_unopened": false,
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
      "summary": "원문 미열람. 유통사 물류센터 데이터로 AMR 플릿 규모와 충전기 수를 시뮬레이션으로 산정한 연구.",
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
      "summary": "원문 미열람. RMFS 의 충전·배터리 교환 전략 비교 연구.",
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
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 플릿 어댑터 템플릿 설정: recharge_threshold·recharge_soc·task_capabilities 등.",
      "source_unopened": false,
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
      "summary": "원문 미열람. 랙 이동 로봇 작업대의 주문·랙 순서를 함께 최적화해 필요 로봇 대수를 줄인 연구.",
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
      "summary": "원문 미열람. RMFS 결정 문제 연구용 이산 사건 시뮬레이션 프레임워크.",
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
      "summary": "원문 미열람. RMFS 결정 규칙을 시뮬레이션으로 비교한 연구.",
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
      "summary": "원문 미열람. 다중 AGV 경로망을 시뮬레이션으로 자동 설계하는 연구.",
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
      "summary": "원문 미열람. 다중 에이전트 경로 찾기 벤치마크 지도와 지도별 시나리오 파일.",
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
      "summary": "원문 미열람. 로봇 미션 명세·실행 형식 비교 연구.",
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
      "summary": "원문 미열람. 행동 트리 편집·모니터링 도구 소개.",
      "source_unopened": true,
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
      "summary": "원문 미열람. 실제·가상 로봇과 센서를 섞은 혼합 현실 플릿 관리 시험 도구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1306",
      "org": "Garg, V., Maywald, J. D., & Naman, M. (International Journal of Retail & Distribution Management 53(10-11))",
      "title": "Optimising human-robot collaboration for efficiency in retail warehousing",
      "published": "2025-10-14",
      "url": "https://www.emerald.com/ijrdm/article/53/10-11/1123/1303314/Optimising-human-robot-collaboration-for",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "AMR 와 피킹 작업자 수를 바꾼 창고 구성 48가지 이산 사건 시뮬레이션으로 AMR:작업자 약 2:1 에서 효율이 가장 높다고 보고(초록 기준).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-822",
      "org": "Howard, T. L. (California Polytechnic State University, San Luis Obispo, 석사논문)",
      "title": "A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities",
      "published": "2026-06",
      "url": "https://digitalcommons.calpoly.edu/theses/3387",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "RaaS 과금 아래 협업형 AMR 대수 산정을 라인당 비용 최소화로 바꾸고 DES 27,000회·대기행렬 모델·XGBoost 대리 모델로 분석한 석사논문(초록 기준).",
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
      "summary": "ROS 2 통신 기록·재생 도구 README: 기본 MCAP 저장, 재생 속도·/clock·토픽 선택·여러 백 파일 시각순 재생.",
      "source_unopened": false,
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
      "summary": "원문 미열람. 국내 스마트물류센터 인증 제도 안내 사이트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1096",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "시각이 찍힌 발행·구독 메시지를 담는 MCAP 컨테이너 형식 명세: 기록·발행 시각, 메시지·청크 색인, 채널별 인코딩.",
      "source_unopened": false,
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
      "summary": "원문 미열람. 로봇 시뮬레이션–현실 격차의 원인과 대응을 정리한 서베이.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1308",
      "org": "Smit, I. G., Bukhsh, Z., Pechenizkiy, M., Alogariastos, K., Hendriks, K., & Zhang, Y. (arXiv)",
      "title": "Learning Efficient and Fair Policies for Uncertainty-Aware Collaborative Human-Robot Order Picking",
      "published": "2024-04-09",
      "url": "https://arxiv.org/abs/2404.08006",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "작업자–AMR 배정을 다목적 심층 강화학습으로 정하고 이산 사건 시뮬레이션으로 학습·평가한 프리프린트(초록 기준).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-241",
      "org": "Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M.",
      "title": "Automated generation of digital twin for a built environment using scan and object detection as input for production planning",
      "published": "2023",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 스캔과 객체 인식으로 생산 계획용 건물 환경 디지털 트윈을 자동 생성하는 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1303",
      "org": "Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020)",
      "title": "Simulation-based Testing for Early Safety-Validation of Robot Systems",
      "published": "2020-11-20",
      "url": "https://arxiv.org/abs/2011.10294",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 모델과 최적화로 시뮬레이션 안에서 고위험 사람 행동을 생성해 초기 설계 단계 로봇 셀의 위험을 찾는 방법(초록 기준).",
      "source_unopened": false,
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
      "summary": "원문 미열람. 확률적 시나리오 언어 Scenic 3.0 의 3D 환경 모델링과 반증 기반 시험.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1312",
      "org": "Wind River (Engblom, J. 인터뷰, Buchwieser, A.)",
      "title": "Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser",
      "published": "2014-11-20",
      "url": "https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "IEC 61508-7 C.5.19 의 시뮬레이션 정의를 인용하고 기능안전 표준이 시뮬레이션·장애 주입을 권고한다고 해석한 업체 블로그 인터뷰(표준 원문 아님).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1304",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 구동 로봇의 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어질 수 있음을 보인 프리프린트(초록 기준).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1309",
      "org": "Autoware Foundation (autowarefoundation GitHub)",
      "title": "autoware_rosbag2_anonymizer — README",
      "published": null,
      "url": "https://github.com/autowarefoundation/autoware_rosbag2_anonymizer",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ROS 2 백 파일 이미지의 얼굴·번호판 등을 탐지·분할 모델로 찾아 블러 처리하는 익명화 도구 README.",
      "source_unopened": false,
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
      "summary": "원문 미열람. 가상 시운전의 모델 유형·용어·정의 지침.",
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
      "summary": "원문 미열람. 실제 제어기와 가상화 인스턴스를 섞은 분산 시스템 가상 시운전 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1313",
      "org": "Open Robotics (gazebosim/gz-fuel-tools GitHub)",
      "title": "Gazebo Fuel Tools — README",
      "published": null,
      "url": "https://github.com/gazebosim/gz-fuel-tools",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Gazebo Fuel 서버의 모델·월드를 목록·다운로드·업로드하는 클라이언트 라이브러리와 gz fuel 명령 README, 원격 모델 새 버전 감지를 로드맵 과제로 적음.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1231",
      "org": "Open Robotics (Gazebo Classic)",
      "title": "Gazebo : Tutorial : Model structure and requirements",
      "published": null,
      "url": "https://classic.gazebosim.org/tutorials?tut=model_structure",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Gazebo 클래식 모델 데이터베이스의 폴더 구조·database.config·model.config 요구사항.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1311",
      "org": "Kassem, K., & Michahelles, F. (Mensch und Computer 2022 Workshop Proceedings, Gesellschaft für Informatik)",
      "title": "Exploring Human-robot Interaction by Simulating Robots",
      "published": "2022-09",
      "url": "https://dl.gi.de/items/1f2227be-b32d-467c-bf94-77d37e5194ce/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VR·AR 환경에서 로봇을 가상으로 흉내 내 사람–로봇 상호작용 사용자 연구를 하는 방법을 다룬 워크숍 논문(초록 기준).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1307",
      "org": "Stączek, P., Pizoń, J., Danilczuk, W., & Gola, A. (Sensors 21(23):7830)",
      "title": "A Digital Twin Approach for the Improvement of an Autonomous Mobile Robots (AMR's) Operating Environment—A Case Study",
      "published": "2021-11-25",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8659435/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "생산 홀 AMR 운영 환경을 Gazebo·ROS 디지털 트윈으로 시험해 통로 배치 변경안을 평가한 사례 연구(수치는 리서치 열람 기록 기준, 검증 단계 재대조 못함).",
      "source_unopened": false,
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
      "summary": "원문 미열람. 실제 PLC 와 3D 가상 공정 시뮬레이터를 잇는 가상 플랜트 구축 절차.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1316",
      "org": "파이낸스스코프",
      "title": "아바코, AMR 스마트 물류 시스템 개발·실증 완료… 피지컬 AI 사업 가속",
      "published": "2026-08-14",
      "url": "https://www.finance-scope.com/article/view/scp202608140009",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "아바코가 이차전지 분야 산업 AI 실증 과제에서 디지털 트윈으로 물류 동선·장비 운용을 사전 검증하고 성과 수치를 발표했다는 보도(회사 발표 수치).",
      "source_unopened": false,
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
      "summary": "원문 미열람. 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획 보도자료.",
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
      "summary": "원문 미열람. 일상 활동 1,000개를 BDDL 로 명세하고 OmniGibson 에 구현한 벤치마크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/index.md"
      ]
    },
    {
      "id": "ref-1134",
      "org": "Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI)",
      "title": "Composable and executable scenarios for simulation-based testing of mobile robots",
      "published": "2024-08-02",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 도면 DSL·동적 요소·수용 기준을 담은 이동로봇 시뮬레이션 시험 시나리오 구성.",
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
      "summary": "원문 미열람. 물류센터 구축에서 에뮬레이션으로 제어를 사전 검증한 업체 사례 소개.",
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
      "summary": "산업용 로봇 플릿 디지털 트윈 블루프린트 발표 블로그(2025-01-06). 참고문헌 목록의 발행일 '미확인'을 원문 열람으로 정정.",
      "source_unopened": false,
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
      "question": "대화로 만든 다중 로봇 작업 계획을 사람이 승인하기 전에 시뮬레이션으로 실행 가능성을 미리 확인하는 절차를 플릿 오케스트레이션에 적용한 공개 사례가 있는가?",
      "areas": [
        12,
        36,
        44
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가?",
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
    },
    {
      "action": "new",
      "question": "운영 기록으로 상황을 재현하기 전에 영상 기록을 익명화하면 재현 충실도가 얼마나 떨어지며, 국내 개인정보 처리 기준에서 재현용 기록을 어떻게 보관·공유해야 하는가?",
      "areas": [
        53,
        36
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "이동로봇 안전 표준(ISO 3691-4 등)이나 국내 인증 기관이 시뮬레이션·가상 시운전 결과를 안전 확인 근거로 인정하는 조건과 절차가 있는가?",
      "areas": [
        50,
        36,
        54
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    },
    {
      "site_type": "기타",
      "item": "완료·인계",
      "link": "docs/categories/design-and-simulation/index.md#다른-대분류와의-연결",
      "title": "I. 설계·시뮬레이션"
    }
  ],
  "standards_updates": [
    {
      "name": "IDTA 02005 Provision of Simulation Models (1.0)",
      "kind": "표준",
      "org": "IDTA(Industrial Digital Twin Association)",
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models",
      "related_areas": [
        34,
        36,
        4,
        58
      ],
      "summary": "자산관리셸 서브모델 템플릿으로, 자산의 시뮬레이션 모델 파일을 모델 유형·사용법·적용 분야와 함께 제공하게 하고 시뮬레이션 모델 검색과 제조사·유통사에 대한 모델 파일 요청을 사용 사례로 둔다(저장소 README 기준, 발행일 미확인).",
      "ref_id": "ref-1314"
    },
    {
      "name": "autoware_rosbag2_anonymizer",
      "kind": "오픈소스",
      "org": "Autoware Foundation",
      "url": "https://github.com/autowarefoundation/autoware_rosbag2_anonymizer",
      "related_areas": [
        53,
        36
      ],
      "summary": "ROS 2 백 파일(sqlite3·mcap) 이미지에서 얼굴·번호판 같은 대상을 탐지·분할 모델로 찾아 가우시안 블러로 가린 익명화 백 파일을 만드는 도구(자율주행 생태계).",
      "ref_id": "ref-1309"
    },
    {
      "name": "Gazebo Fuel Tools (gz-fuel-tools)",
      "kind": "오픈소스",
      "org": "Open Robotics",
      "url": "https://github.com/gazebosim/gz-fuel-tools",
      "related_areas": [
        34,
        57
      ],
      "summary": "Gazebo Fuel 서버의 모델·월드를 목록·다운로드·업로드하는 클라이언트 라이브러리와 명령 도구. README 로드맵은 원격 모델 새 버전 감지를 미해결 과제로 적는다.",
      "ref_id": "ref-1313"
    }
  ],
  "additional_research_requests": [
    "'다른 대분류와의 연결' 절의 '아직 다루지 않은 연결': 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성(oq-129), 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육(운영자 교육용 다중 로봇 플릿 시뮬레이터 등)과 I. 설계·시뮬레이션 영역을 잇는 근거 — 연결 공백을 줄이기 위해 필요하다.",
    "M. 안전 연결: IEC 61508-7 C.5.19 원문과 ISO 3691-4 의 시뮬레이션·가상 검증 관련 조항 — 현재 업체 블로그 인용(ref-1312)에만 기대므로 표준 원문 근거가 필요하다.",
    "Stączek 외(ref-1307)의 도킹 복귀 시간 수치(44초 → 22.5~23.3초)를 원문으로 다시 대조 — 1차 검증 단계에서 원문을 열지 못했다.",
    "IDTA 02005 'Provision of Simulation Models' 1.0 의 공식 발행일과 번호를 IDTA 공식 목록에서 확인 — 각주 발행일이 미확인이다.",
    "벤더 주장(Rockwell Automation 18%·5주, 아바코 다운타임 20%·자동화율 90%, NVIDIA Mega, CJ대한통운 디지털 트윈 계획)의 독립 확인 또는 같은 기준선의 독립 측정 연구(oq-257·oq-084).",
    "34. 시뮬레이션·예측용 디지털 트윈·35. 처리능력·규모·배치 설계 페이지(이전 분류 기준)의 10절 갱신: Xia 외·Holodeck·Smit 외·Howard·Huck 외·Carr 외·Gazebo 라이선스 규칙·Stączek 외 연결 반영 — 이번 실행 유형(대분류 연결)은 대분류 페이지 한 절만 고치므로 다음 해당 영역 실행으로 미룬다."
  ],
  "fixes_applied": [
    "f29 — vda5050-sim 문장(F. 연동 항목)에서 '기본 5종 AGV' 구절을 빼고, 'VDA 5050 3.0.0 을 주 대상으로 2.1.0·2.0.0·1.1.0 구형 판도 흉내 내고 공식 3.0.0 JSON 스키마 위에 세운 메시지 스키마와 적합성 시험 묶음을 둔다고 README 에 적는다'로 쓰고 개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아님을 밝혔다.",
    "f11 — SayPlan 문장(C. 채팅 기반 구성·운영 항목)을 '최대 3개 층·36개 방·140개 자산·물체의 두 대형 환경에서 평가하고 이동 매니퓰레이터로 실행을 시연했다'로 고치고 '(단일 로봇 대상)'을 붙였다.",
    "f49 — H. 실행·협업·예외 복구 항목에서 '피커(작업자)'로 쓰고, P. 거버넌스·법규·사회의 60. 노동·수용성·접근성 연결에서는 '노동 비용 측면의 근거이며 수용성·노동 영향의 직접 근거는 아니다(논문은 비용 분석이다)'를 밝혔다.",
    "f77 — Q. 현장 유형별 적용의 제조 공장 항목에서 도킹 복귀 시간 수치를 '보고했다'로 쓰고 '저자 사례 연구의 보고값이며 검증 단계에서 다시 대조하지 못했다'를 병기했다.",
    "f2·f3·f79·f80 — 각 문장에 벤더 주장을 밝히고 [추정] 태그를 붙였으며 18%·5주, 다운타임 20%·자동화율 90% 는 기준선·측정 방법 미공개임을 함께 썼다. f28 은 '2025-07 보도에 따르면'과 '목표' 표현을 유지했다.",
    "f64 — M. 안전 항목에 '연계 대상:'으로 시작하는 [추정] 문장 하나로만 두고, IEC 61508-7 C.5.19 는 Wind River 블로그 인터뷰(2014)의 인용으로, 시뮬레이션·장애 주입 권고는 업체 직원의 해석으로 밝히고 표준 원문 미확인을 적었다.",
    "각주 원문 미열람 표기 — 지시된 39개 출처의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-528·ref-079·ref-105·ref-406·ref-104·ref-407·ref-831·ref-1087·ref-1096·ref-527·ref-1303~ref-1316 은 표기하지 않았고, ref-528·ref-079 의 요약에서 '원문 미열람.' 접두어를 뺐다.",
    "ref-527 각주 발행일을 2025-01-06 으로 쓰고 reference_updates 의 published 도 정정했으며, ref-1314 의 발행일은 각주에 '미확인', JSON 에 null 로 두었다.",
    "범위 경계 문구 — f21·f25·f26·f27 의 승강기·문 제어, f2·f70·f78 의 컨베이어·PLC 제어 코드 가상 시운전, f3·f22·f47·f61 의 센서 시뮬레이션·로봇 자체 주행·파지 물리·현실 격차 보정, f62·f63 의 안전 인증·설비 안전 제어를 각 문장 괄호 안에 '연계 대상'으로 짧게 밝혔고, f24·f64 는 '연계 대상:'으로 시작하는 문장으로 두었다.",
    "18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 — E. 사물·사람·실시간 상태 항목에 f16 으로 '18 은 현재 상태 표현, 34 는 가정한 미래 실험'을 밝히고, f65·f66 의 디지털 트윈 동기화는 N. 보안·개인정보 항목에서 36. 가상 시운전·실제 상황 재현의 경로로만 서술했다. 34 가 현재 상태를 표현한다고 쓰지 않았다.",
    "C. 채팅 기반 구성·운영 항목 머리에 분류 원문 주석의 엔진 짝(33·36, 14·15, 25·26 을 번호와 이름으로)을 링크와 함께 적고, f7(자율주행)·f9(제약 공정)·f11(단일 로봇) 문장에 대상을 밝혔다.",
    "L. AI·학습 기술 항목에 44·45·46·47 링크와 적용 대상 33·34·35·36 을 함께 적었고, f15 는 D. 공간·지도 모델 항목에서 44 와 33 을 함께 링크했다. f59 에는 25. 작업 배정 — MRTA 연결도 밝혔다.",
    "f43 은 [의견]으로 두고 'Lee 외 저자들은 … 제안했다'로 의견 주체를 밝혔다. f23 은 ref-516(제1부)·ref-518(제6부) 문장을 나눠 각자의 각주를 붙였고, f30·f31·f32 와 f36(ref-101·ref-398)도 출처별 문장과 각주로 나눴다.",
    "'아직 다루지 않은 연결'을 절 끝에 2. 사용 사례·요구·책임 범위, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 10. 채팅으로 로봇 구성(oq-129 관련 부분 근거만 있음), 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육으로 적었고 완전성 표현은 쓰지 않았다.",
    "다른 대분류·세부영역은 새 17개 대분류 기준의 문자+이름(예: 'F. 연동')과 번호+이름(예: '25. 작업 배정 — MRTA')으로 쓰고, 옛 대분류 이름을 옮겨 쓰지 않았다.",
    "Q. 현장 유형별 적용 항목에서 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타)을 이름으로 밝히고, f18·f19·f44·f81~f84 의 예제 월드·벤치마크·경진대회 시나리오는 각 문장에 실제 현장 배치가 아님을 밝혔다."
  ]
}
```

### runs/2026-10-09-07/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/design-and-simulation/index.md (1개 절)
```

### runs/2026-10-09-07/pages/categories/design-and-simulation/index.md

```markdown
---
title: "I. 설계·시뮬레이션"
type: category
status: draft
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-079, ref-098, ref-101, ref-102, ref-103, ref-104, ref-105, ref-106, ref-109, ref-116, ref-241, ref-267, ref-291, ref-381, ref-398, ref-406, ref-407, ref-409, ref-516, ref-518, ref-521, ref-526, ref-527, ref-528, ref-741, ref-815, ref-831, ref-832, ref-833, ref-943, ref-971, ref-1086, ref-1087, ref-1088, ref-1089, ref-1090, ref-1091, ref-1092, ref-1096, ref-1126, ref-1127, ref-1128, ref-1129, ref-1130, ref-1131, ref-1133, ref-1134, ref-1165, ref-1231, ref-1303, ref-1304, ref-416, ref-1306, ref-1307, ref-1308, ref-1309, ref-1310, ref-1311, ref-1312, ref-1313, ref-1314, ref-822, ref-1316]
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

I. 설계·시뮬레이션의 네 세부영역 — [33. 시나리오 모델·편집](scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](simulation-and-predictive-digital-twin.md), [35. 처리능력·규모·배치 설계](capacity-sizing-and-layout-design.md), [36. 가상 시운전·실제 상황 재현](virtual-commissioning-and-real-situation-replay.md) — 이 다른 대분류의 세부영역에서 무엇을 받고 무엇을 넘기는지 대분류 문자 순으로 적는다. 연결을 해석한 문장은 대부분 추정이고, 근거 가운데 일부는 로봇 플릿이 아닌 대상(자율주행·제약 공정·단일 로봇)에서 나왔으므로 문장마다 그 대상을 밝힌다. 승강기·문·PLC 제어, 로봇 자체 주행·인식, 안전 인증, 수요예측은 연계 대상으로만 다룬다.

- [A. 기획·사업](../planning-and-business/index.md)
    - 35. 처리능력·규모·배치 설계 ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md): Howard(Cal Poly 석사논문, 2026-06)는 처리량 최대화 기준의 자율이동로봇(Autonomous Mobile Robot, AMR) 대수 산정이 서비스형 로봇(Robot-as-a-Service, RaaS) 구독 과금에서 플릿을 과대 산정한다고 보고, 대수 산정을 주문 라인당 비용 최소화 문제로 바꿔 피킹 구역제 물류창고를 이산 사건 시뮬레이션 27,000회로 분석했다. [사실][^ref-822] 그 조건에서 라인당 비용은 AMR:피커 비율에 대해 U자형이었고, 비용이 가장 낮은 비율은 저수요 1에서 고수요 2.5로 옮겨 갔다(저자 보고값). [사실][^ref-822]
    - 36. 가상 시운전·실제 상황 재현 ↔ 3. 경제성·조달·사업 모델: Rockwell Automation 사례 소개(2024-08-28)는 미국 남부 물류센터 구축에서 통합자가 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증해 전체 프로젝트 기간을 18%, 현장 시운전을 5주 줄였다고 밝히지만, 이는 벤더 주장이며 18%·5주의 기준선과 측정 방법은 공개되지 않았다(컨베이어 제어 에뮬레이션은 설비 업체·통합자 쪽 연계 대상, 독립 측정은 [oq-257](../../open-questions.md)). [추정][^ref-1165]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md): NVIDIA 는 2025-01-06 산업용 로봇 플릿 디지털 트윈을 만드는 'Mega' Omniverse 블루프린트를 발표하며 배치 전에 센서 시뮬레이션·합성 데이터로 로봇 플릿을 시험·최적화할 수 있다고 내세우지만, 이는 독립 확인되지 않은 벤더 주장이다(센서 시뮬레이션은 시뮬레이터 제공자 쪽 연계 대상). [추정][^ref-527]
- [B. 로봇 온톨로지](../robot-ontology/index.md)
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md): 시나리오가 참조하는 로봇 모델은 SDFormat 같은 로봇·환경 기술 형식으로 시뮬레이터에 들어가므로 기종 제원 기술(형상·질량·센서)이 시뮬레이션 자산의 원천으로 이어질 것으로 보이나, 등록 정보와 시뮬레이션 모델을 잇는 사례는 확인하지 못했다. [추정][^ref-1092]
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ 4. 이기종 로봇 등록: IDTA 서브모델 템플릿 'Provision of Simulation Models'(1.0, IDTA 02005)는 자산관리셸(Asset Administration Shell, AAS)을 통해 자산의 시뮬레이션 모델 파일을 모델 유형·사용법·적용 분야와 함께 제공하게 하고, 현재 단계 사용 사례로 시뮬레이션 모델 검색과 제조사·유통사에 대한 모델 파일 요청을 둔다. [사실][^ref-1314]
    - 36. 가상 시운전·실제 상황 재현 ↔ [7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md): 7. 온톨로지 검증·변경 관리가 능력 정의에 붙이는 지원 단계(시뮬레이션 연결·시뮬레이션 검증·실기 검증)를 판정하려면 모델·시뮬레이션 신뢰도 평가와 시뮬레이션–현실 상관 지표가 기준이 될 수 있으나, 두 체계를 대응시킨 자료는 확인하지 못했다([oq-156](../../open-questions.md)). [추정][^ref-1133][^ref-1127]
- [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md) — 분류 원문의 C. 채팅 기반 구성·운영 주석에 따라 대화 기능은 엔진과 짝으로 읽는다. 시나리오 구성과 실제 상황 재현의 엔진은 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현, 맵 작성의 엔진은 [14. 도면·BIM에서 지도 만들기](../space-and-map-model/maps-from-floor-plans-and-bim.md)·[15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md), 업무 지시의 엔진은 [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)·[26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)이다. 아래 근거는 로봇 플릿이 아닌 대상에서 나온 것이 많다.
    - 33. 시나리오 모델·편집 ↔ [9. 채팅으로 시나리오 구성](../chat-based-configuration-and-operation/chat-scenario-composition.md): Chat2Scenic(2026-07)은 챗봇 인터페이스로 시나리오를 대화로 다듬으면서 검색 증강 방식으로 도메인 특화 언어 시나리오 스크립트를 만들고, 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%(비교 방법 30.08%·16.26%)를 보고했다(자율주행 시나리오 대상이며 로봇 플릿이 아니다). [사실][^ref-833]
    - 33. 시나리오 모델·편집 ↔ 9. 채팅으로 시나리오 구성·[13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md): 대화로 만든 시나리오의 출력 형식은 33. 시나리오 모델·편집이 정하는 매개변수화·장애 선언 형식이 되고, 생성 스크립트가 컴파일되지 않는 경우가 남으므로 승인 전 형식 검사가 두 대분류의 인계 지점이 될 것으로 보인다(사용자 의도와의 일치를 검사하는 방법은 미확인). [추정][^ref-833][^ref-1088][^ref-528]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md): Xia 외(2026-08, ETFA 2026 채택)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다(로봇 플릿 대상이 아니다). [사실][^ref-832]
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ 11. 채팅으로 실제 상황 시뮬레이션 재현: 대화로 조건을 바꿔 비교하는 일은 언어 모델이 34. 시뮬레이션·예측용 디지털 트윈의 시뮬레이션 실험을 설계·실행하는 구조로 이어질 것으로 보이나, 비교 결과를 믿으려면 36. 가상 시운전·실제 상황 재현의 재현 충실도 지표가 함께 필요하고 로봇 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-832][^ref-1127]
    - 36. 가상 시운전·실제 상황 재현 ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md): SayPlan(Rana 외, CoRL 2023)은 언어 모델이 3차원 장면 그래프로 세운 초기 계획을 실행 전에 장면 그래프 시뮬레이터로 확인하고 그 피드백으로 실행 불가능한 동작을 고치는 반복 재계획을 두며, 최대 3개 층·36개 방·140개 자산·물체의 두 대형 환경에서 평가하고 이동 매니퓰레이터로 실행을 시연했다(단일 로봇 대상). [사실][^ref-416] 대화로 만든 계획을 사람이 승인하기 전에 36. 가상 시운전·실제 상황 재현의 실행 전 계획 검증으로 실행 가능성을 먼저 걸러 내는 구조가 두 영역의 접점이 될 것으로 보이나, 다중 로봇 플릿 계획에 적용한 사례는 확인하지 못했다. [추정][^ref-416]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [8. 채팅으로 맵 작성](../chat-based-configuration-and-operation/chat-map-authoring.md): Open-RMF 에서 같은 건물 파일(`.building.yaml`)이 주행 그래프와 시뮬레이션 월드를 모두 만들므로, 대화로 작성·수정한 지도가 같은 형식으로 저장되면 시뮬레이션 월드도 다시 생성할 수 있을 것으로 보이나 대화형 지도 작성과 연결한 사례는 확인하지 못했다. [추정][^ref-406][^ref-079]
- [D. 공간·지도 모델](../space-and-map-model/index.md)
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·[16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md): Open-RMF 의 `building_map_generator` 는 traffic-editor 로 주석한 건물 파일에서 층별 바닥·벽과 문·승강기를 담은 시뮬레이션 월드와 주행 그래프를 만들고, 환경을 바꿀 때는 주석을 고쳐 다시 생성한다(두 출처는 같은 기관 자료). [사실][^ref-406][^ref-079]
    - 33. 시나리오 모델·편집 ↔ 14. 도면·BIM에서 지도 만들기, L. AI·학습 기술의 [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md): 언어 모델·생성 모델로 시뮬레이션 환경을 만드는 연구(Holodeck, Arena 4.0)가 33. 시나리오 모델·편집의 예제 라이브러리를 채우는 수단이 될 수 있으나, 생성 환경은 실제 현장 지도가 아니므로 D. 공간·지도 모델의 도면·현장 정합과 구분해야 할 것으로 보인다. [추정][^ref-815][^ref-1089]
- [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): 제조 분야 분류 자료가 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분하므로, 18. 실시간 세계 상태·데이터 일관성은 현장 상태를 가상 모델에 반영하는 현재 상태 표현을, 34. 시뮬레이션·예측용 디지털 트윈은 그 모델을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거 자료는 제조 대상). [추정][^ref-291]
    - 36. 가상 시운전·실제 상황 재현 ↔ [19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md): Waymax(2023)는 실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화하거나 재생하고, 사실적 상호작용을 위해 학습된 행동 모델과 규칙 기반 행동 모델을 제공한다(자율주행 대상이며 로봇 현장 사례가 아니다. 관련 열린 질문 [oq-256](../../open-questions.md)). [사실][^ref-1128]
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ 19. 사람·보행자 모델, M. 안전의 [49. 사람 근접 안전](../safety/human-proximity-safety.md): Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드(현장 유형: 상업 시설)가 이를 군중 시뮬레이션으로 쓴다(예제 월드이며 실제 시설 배치가 아니다. 두 출처는 같은 기관 자료). [사실][^ref-406][^ref-104]
    - 33. 시나리오 모델·편집 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md): NIST ARIAC 시나리오는 작업 대상인 배터리 셀의 종류(Li-Ion·Ni-MH)·전압 허용 범위·결함(찌그러짐·부풂·긁힘)과 4셀 키트를 정의하고, 키트는 출하 지점에서 제출 서비스가 셀 결함·전압·종류·총전압 조건을 모두 만족할 때만 받아들인다(현장 유형: 제조 공장, 경진대회 시뮬레이션이며 실제 공장이 아니다). [사실][^ref-1087] 이처럼 시나리오가 작업 대상의 속성과 완료 판정 조건을 함께 담으면 시나리오 형식이 17. 작업 대상·자산 식별과 인계 추적의 작업 대상 식별자와 G. 계획·최적화의 [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md)의 완료 조건 어휘를 공유해야 할 것으로 보이나, 이를 정한 공통 형식은 확인하지 못했다. [추정][^ref-1087]
- [F. 연동](../integration/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 시뮬레이션의 문·승강기 플러그인은 실제와 같은 문·승강기 요청 메시지에 응답하고, `door_supervisor` 는 한 로봇이 다른 로봇 앞에서 문을 닫는 것 같은 충돌을 막으며 `lift_supervisor` 는 여러 플릿의 승강기 요청을 관리한다(실제 승강기·문 제어는 연계 대상이며 ROP 는 요청·상태 확인만 맡는다). [사실][^ref-406]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): Open-RMF 의 slotcar(슬롯카) 플러그인은 플릿 어댑터의 경로·모드 요청(`PathRequest`·`ModeRequest`)을 받아 경유점 사이를 레일식 직선으로 움직이고 장애물을 감지하면 멈추는 단순화 로봇 모델로, 센서 기반 주행 스택을 돌리는 계산 부담을 피한다(로봇 자체 주행·인식 거동의 충실도는 제조사·물리 시뮬레이터 쪽 연계 대상). [사실][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ 20. 로봇·제조사 관제 연동: 공개 오픈소스 vda5050-sim 은 VDA 5050 3.0.0 을 주 대상으로 2.1.0·2.0.0·1.1.0 구형 판도 흉내 내고, 공식 3.0.0 JSON 스키마 위에 세운 메시지 스키마와 적합성 시험 묶음을 둔다고 README 에 적는다(개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아니다). [사실][^ref-407]
    - 36. 가상 시운전·실제 상황 재현 ↔ 20. 로봇·제조사 관제 연동, O. 검증·도입·수명주기의 [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md): 2025-07 보도에 따르면 클로봇은 산업통상자원부 국가로봇테스트필드 기술개발 과제(54억원) 주관기관으로 KETI 와 함께 다종·다수 로봇 제어 플릿 관리 시스템(Fleet Management System, FMS) 요소기술, 로봇과 디지털 트윈·시뮬레이터 간 인터페이스, 실환경 연동 디지털 트윈 증강 시뮬레이션을 2028년까지 개발해 국가로봇테스트필드에 적용하는 것을 목표로 한다(기사 1건 기준이며 과제 공고·성과는 미확인). [사실][^ref-1310]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md): 제조용 디지털 트윈 프레임워크 ISO 23247 은 제1부가 국내에 KS X ISO 23247-1 로 들어와 있다. [사실][^ref-516] 디지털 트윈 결합을 다루는 ISO 23247 제6부는 2026년에 발행되었으나, 이 프레임워크를 물류센터 이종 로봇·설비에 그대로 쓸 수 있는지는 확인되지 않았다([oq-085](../../open-questions.md)). [사실][^ref-518]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md): 연계 대상: 성수기 주문·물동량 전망 같은 시나리오 입력은 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 물류·공급망 디지털 트윈 검토(Le·Fan, 2024)는 실제 데이터로 검증한 연구가 소수라고 보고한다. [추정][^ref-521]
    - 35. 처리능력·규모·배치 설계·36. 가상 시운전·실제 상황 재현 ↔ 22. 설비·건물 시스템 연동, Q. 현장 유형별 적용의 63. 병원·의료: 고려대학교 구로병원의 약품 배송 로봇 기록(2025-06, 122건)과 몬테카를로 재현에서 승강기 가동률 59.01% 이하일 때 배송 성공률 95.5%, 90% 초과에서 실패가 몰렸다(현장 유형: 병원, 승강기 제어 자체는 연계 대상). [사실][^ref-943]
    - 35. 처리능력·규모·배치 설계 ↔ 22. 설비·건물 시스템 연동, Q. 현장 유형별 적용의 64. 상업 시설: 다층 호텔의 배송 로봇 경로 계획 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다(현장 유형: 상업 시설, 승강기 제어 자체는 연계 대상). [사실][^ref-103]
    - 35. 처리능력·규모·배치 설계 ↔ 22. 설비·건물 시스템 연동, Q. 현장 유형별 적용의 65. 가정·공동주택: 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 국내 인증 모델(2023)은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야 28개 항목(총점 176점)으로 구성된다(현장 유형: 가정, 공동주택 대상). [사실][^ref-409]
- [G. 계획·최적화](../planning-and-optimization/index.md)
    - 35. 처리능력·규모·배치 설계 ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md): 한 유통사 물류센터 팔레트 이동 데이터로 한 AMR 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. [사실][^ref-102] 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS)의 충전·배터리 교환 전략을 반개방형 대기행렬 네트워크로 비교한 연구(Zou 외, 2018)가 있다. [사실][^ref-098] 창고 충전소 배치를 페이지랭크 유사 방법으로 최적화하는 연구(Stark 외, 2024-06)도 있다. [사실][^ref-109]
    - 35. 처리능력·규모·배치 설계 ↔ 25. 작업 배정 — MRTA: Open-RMF 플릿 어댑터 템플릿 설정에서 배터리가 `recharge_threshold`(예시값 0.10) 아래인 로봇은 작동하지 않으며, 충전 작업의 목표 충전 수준은 `recharge_soc`(예시값 1.0)로 둔다. [사실][^ref-105] 그래서 충전기 수·위치 같은 충전 설비 계획의 결과가 운영 중 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어질 것으로 보이나, 공개 사례는 확인하지 못했다. [추정][^ref-105][^ref-102]
    - 35. 처리능력·규모·배치 설계 ↔ 26. 작업 순서·스케줄링: 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정한 Boysen 외(2017)는 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다(저자 계산 실험 조건, 독립 재현 미확인). [사실][^ref-381]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ 25. 작업 배정 — MRTA: RAWSim-O 는 로봇 이동형 풀필먼트 시스템의 여러 결정 문제를 연구하는 이산 사건 시뮬레이션이다. [사실][^ref-101] Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다(시뮬레이션 결과이며 현장 실측이 아니다). [사실][^ref-398]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다. [사실][^ref-267] 경로망 배치를 시뮬레이션으로 평가하는 일은 현재 상태 표현이 아니라 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽에 걸치는 것으로 보인다. [추정][^ref-267]
    - 33. 시나리오 모델·편집 ↔ 27. 다중 로봇 경로·교통 관리 — MAPF: Moving AI Lab 의 다중 에이전트 경로 찾기(MAPF) 벤치마크는 지도마다 시나리오 파일(even·random 각 25개)을 묶어 공개한다. [사실][^ref-1091] 지도와 시나리오 파일을 묶어 공개하는 방식은 경로 계획기를 같은 조건에서 비교하게 하는 시나리오 라이브러리 구성의 예로 쓰일 수 있을 것으로 보인다. [추정][^ref-1091]
    - 33. 시나리오 모델·편집 ↔ 24. 작업·워크플로 모델링: 로봇 미션 명세·실행 형식 비교 연구와 행동 트리 편집기(Groot2)가 33. 시나리오 모델·편집의 미션 기술 형식·편집기 선택 근거로 쓰였으므로, 시나리오 안의 작업 표현은 24. 작업·워크플로 모델링의 단계·선후관계·완료 조건 표현과 같은 형식을 공유해야 할 것으로 보인다. [추정][^ref-116][^ref-1090]
    - 36. 가상 시운전·실제 상황 재현 ↔ 25. 작업 배정 — MRTA: VirTooS(2026-08)는 ROS 2와 Unity 를 결합한 혼합 현실 환경에서 실제·가상 로봇과 실제·가상 센서를 함께 써서 자율이동로봇 팀의 플릿 관리 작업을 시험하는 도구이며, 작업 배정 예제에서 실제 로봇과 가상 로봇이 상호작용한다. [사실][^ref-1129] Lee 외 저자들은 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰고, 병원별 구조·통행·승강기 제어 정책을 재현한 병원 디지털 트윈으로 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다(현장 유형: 병원). [의견][^ref-943]
- [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)
    - 33. 시나리오 모델·편집 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): NIST ARIAC 는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급 주문을 매개변수로 선언해 시각이나 발생 횟수 조건으로 시나리오에 주입한다(현장 유형: 제조 공장, 경진대회 시나리오이며 실제 공장이 아니다). [사실][^ref-528]
    - 36. 가상 시운전·실제 상황 재현 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)·32. 예외 복구·재계획·업무 연속성: vda5050-sim 은 로봇별 고장 프로필로 연결 끊김·오류 주입·필드 위반·서비스 모드·비상 정지의 확률을 정하고, 명세의 재시도 가능 동작 흐름(`RETRIABLE`·`retry`·`skipRetry`)을 구현한다고 README 에 적는다(개인 프로젝트의 자기 기술이며 공식 적합성 시험이 아니다). [사실][^ref-407]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md): Open-RMF 시뮬레이션의 `TeleportDispenser` 는 `DispenserRequest` 에 응답해 적재물을 가장 가까운 로봇 위로 순간 이동시키고, `TeleportIngestor` 는 `IngestorRequest` 에 응답해 로봇의 적재물을 월드로 옮겨 배송 작업의 적재·하역을 흉내 낸다. [사실][^ref-406] 적재·하역을 순간 이동으로 대신하므로 이 시뮬레이션은 물리적 인계 동작이 아니라 인계 요청–응답 흐름과 그 순서를 시험하는 데 쓰이며, 인계 실패 같은 물리 거동은 별도 모델이 필요할 것으로 보인다(파지·적재 물리는 로봇 자체 제어 쪽 연계 대상). [추정][^ref-406]
    - 35. 처리능력·규모·배치 설계 ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): Garg·Maywald·Naman(IJRDM, 2025)은 AMR 과 피킹 작업자 수를 바꾼 창고 구성 48가지의 이산 사건 시뮬레이션에서 처리량·효율이 AMR:작업자 약 2:1 에서 가장 높았고, 교차 통로 배치의 처리량 효과는 통계적으로 유의하지 않았다고 보고했다(저자 시뮬레이션 조건). [사실][^ref-1306] Howard(2026)의 시뮬레이션(3구역 순차 구역제·연속 도착 조건)에서는 피커(작업자) 유휴 시간이 교대당 AMR 유휴 시간보다 약 2.5배 비싸 피커와 로봇이 서로 기다리는 동기화 손실의 비용이 주로 노동 쪽에 떨어졌고, 세 배차 휴리스틱은 라인당 비용에 유의한 차이를 내지 않았다(교대조 단위 계획은 [oq-009](../../open-questions.md)로 남아 있다). [사실][^ref-822]
- [J. 현장 운영·관제](../field-operations-and-monitoring/index.md)
    - 36. 가상 시운전·실제 상황 재현 ↔ [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)·[38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): rosbag2 는 ROS 2 통신을 백 파일(기본 저장 형식 MCAP)로 기록하고, 재생 속도 조절(`~/set_rate`)·`/clock` 발행(`--clock`)·토픽 선택(`--topics`)·여러 백 파일의 수신 시각순 동시 재생(`-i`)을 지원하며, 시작 시각 지정은 `~/play` 서비스로 제공한다. [사실][^ref-831]
    - 36. 가상 시운전·실제 상황 재현 ↔ 37. 관제 화면·실행 기록: 메시지 단위 기록 도구와 기록 기반 시뮬레이터가 있으나, 재현의 원천은 37. 관제 화면·실행 기록이 남기는 오케스트레이션 수준 실행 기록(작업·배정·위치·사건 시각)이어야 할 것으로 보이며 이를 시나리오 사양으로 바꾸는 공개 형식은 확인하지 못했다([oq-131](../../open-questions.md)). [추정][^ref-831][^ref-1128]
    - 35. 처리능력·규모·배치 설계 ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md): 충전 방식의 비용 비교와 국내 스마트물류센터 인증 평가에서 두 영역이 만나는 것으로 보이나, 인증 세부 지표에 로봇 대수·가동률 같은 설비 계획 지표가 들어가는지는 확인하지 못했다([oq-011](../../open-questions.md)). [추정][^ref-098][^ref-106]
- [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [41. 플랫폼 아키텍처·외부 API](../platform-architecture-and-infrastructure/platform-architecture-and-external-api.md): rmf_demos 는 시뮬레이션 데모에서 플릿 어댑터의 `server_uri` 를 rmf-web API 서버(`ws://localhost:8000/_internal`)로 지정하면 어댑터가 최신 작업·로봇 상태를 API 서버에 보내고 대시보드로 볼 수 있게 하며, Docker 대시보드는 빠른 연동·시험용이라고 적는다. [사실][^ref-104] 시뮬레이션 플릿과 실제 플릿이 같은 플랫폼 API·대시보드에 붙으므로 외부 시스템 연동과 운영자 화면을 설치 전에 가상 플릿으로 시험할 수 있을 것으로 보이나, 이를 시운전 절차로 정리한 공개 사례는 확인하지 못했다([oq-255](../../open-questions.md)). [추정][^ref-104][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): 가상 시운전 도구가 여러 머신에 컨테이너로 배포되고 시뮬레이션 플러그인이 실제와 같은 요청 메시지에 응답하므로, 가상 대응물을 어느 계산 자원에 두고 실제 시스템과 어떤 통신으로 잇는지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다([oq-040](../../open-questions.md)). [추정][^ref-1129][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md): MCAP 은 시각이 찍힌 발행·구독 메시지를 담는 컨테이너 형식으로, 메시지마다 기록 시각(`log_time`)과 발행 시각(`publish_time`)을 따로 두고 청크 색인에 청크별 최초·최종 기록 시각을 담아 시각·토픽으로 메시지를 찾게 한다. [사실][^ref-1096] rosbag2 의 기본 저장 형식이 MCAP 이다. [사실][^ref-831]
- [L. AI·학습 기술](../ai-and-learning/index.md) — 교차 규칙에 따라 L. AI·학습 기술의 영역과 적용 대상인 이 대분류의 영역을 함께 적는다. D. 공간·지도 모델 항목의 생성 환경 구분도 44. 로봇 기반 모델·언어 모델 계획과 33. 시나리오 모델·편집을 잇는다.
    - [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md) ↔ 33. 시나리오 모델·편집: Holodeck(CVPR 2024)은 GPT-4 가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성하며, 생성 장면에서 학습한 에이전트가 처음 보는 환경에서 주행했다고 보고했다. [사실][^ref-815]
    - [45. 문서·도면·장면 이해](../ai-and-learning/document-drawing-and-scene-understanding.md) ↔ 34. 시뮬레이션·예측용 디지털 트윈: Sommer 외(2023)는 기존 건물 환경의 스캔과 객체 인식을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 다룬다(로봇 플릿 시뮬레이션에 쓴 사례는 미확인). [사실][^ref-241]
    - [46. 예측·학습 기반 최적화](../ai-and-learning/prediction-and-learning-based-optimization.md) ↔ 34. 시뮬레이션·예측용 디지털 트윈: Smit 외(2024-04, arXiv)는 작업자와 AMR 이 피킹 위치에서 만나는 창고에서 작업자–AMR 배정을 다목적 심층 강화학습으로 정하고, 이를 학습·평가하려고 이산 사건 시뮬레이션 모델을 만들었으며, 학습 정책이 효율과 작업자 부하 공정성 모두에서 비교 방법을 앞섰다고 보고했다(프리프린트, 학습 기반 배정이므로 25. 작업 배정 — MRTA 와도 이어진다). [사실][^ref-1308]
    - 46. 예측·학습 기반 최적화 ↔ 35. 처리능력·규모·배치 설계: Howard(2026)는 반개방형 대기행렬 모델로 설계안을 걸러 내고 XGBoost 대리 모델과 등각 예측 구간으로 추가 시뮬레이션 없이 연속 설계 공간의 비용을 예측했으며, 대기행렬 모델은 시뮬레이션 라인당 비용과 약 5%, 대리 모델은 교차 검증에서 3% 안에서 맞았다고 보고했다(저자 보고값, 독립 재현 미확인). [사실][^ref-822]
    - [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ 36. 가상 시운전·실제 상황 재현: 학습 정책이 시뮬레이터의 결함을 악용하는 현실 격차가 보고되므로, 학습 기반 정책의 현실 격차 보정은 47. AI·학습·적응과 모델 운영(및 로봇 제조사·시뮬레이션 도구 쪽 연계 대상)의 일이고 36. 가상 시운전·실제 상황 재현은 재현 결과와 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다. [추정][^ref-741][^ref-1127]
- [M. 안전](../safety/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md): Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 생성해, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다(협동 로봇 셀 대상이며 이동로봇 플릿이 아니다. 안전 인증·설비 안전 제어는 연계 대상). [사실][^ref-1303]
    - 33. 시나리오 모델·편집 ↔ 48. 안전·위험 관리: 위험 상황을 생성·탐색하는 시뮬레이션 시험(사람 행동 최적화, 확률적 시나리오 언어 기반 반증)이 있으므로 33. 시나리오 모델·편집에서 선언한 장애·사람 흐름 시나리오가 48. 안전·위험 관리의 위험 식별 입력이 될 수 있을 것으로 보이나, 다중 이동로봇 플릿에 적용한 사례는 확인하지 못했다. [추정][^ref-1303][^ref-1086]
    - 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈 ↔ 49. 사람 근접 안전: E. 사물·사람·실시간 상태 항목의 Open-RMF 군중 시뮬레이션(crowdsim)이 이 연결의 예다.
    - 36. 가상 시운전·실제 상황 재현 ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md): 연계 대상: Wind River 블로그 인터뷰(2014)는 IEC 61508-7 C.5.19 가 시뮬레이션을 시험 목적으로만 피제어 설비(Equipment Under Control, EUC)의 거동을 흉내 내는 시스템으로 정의한다고 인용하고 기능안전 표준들이 안전 확인에 시뮬레이션·장애 주입을 강하게 권고한다고 해석하지만, 이는 업체 직원의 인용·해석이고 표준 원문은 확인하지 않았으며, 이동로봇 안전 표준이 시뮬레이션 결과를 인증 근거로 받아들이는 절차는 이번 조사에서 찾지 못했다. [추정][^ref-1312]
- [N. 보안·개인정보](../security-and-privacy/index.md)
    - 36. 가상 시운전·실제 상황 재현 ↔ [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md): Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고하고 완화 방안을 논의했다(프리프린트). [사실][^ref-1304]
    - 36. 가상 시운전·실제 상황 재현 ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)·52. 통신 보호·위협 관리·감사: 36. 가상 시운전·실제 상황 재현이 다루는 디지털 트윈 동기화(실시간 상태를 가상 모델에 반영하고 결과를 되돌리는 경로)는 공격 표면이 될 수 있으므로, 시뮬레이션 결과가 실제 계획·설정에 반영되는 경로에 접근통제와 무결성 확인이 필요할 것으로 보인다(로봇 플릿 플랫폼 적용 사례는 확인하지 못했다). [추정][^ref-1304]
    - 36. 가상 시운전·실제 상황 재현 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md): Autoware 재단의 `autoware_rosbag2_anonymizer` 는 ROS 2 백 파일(sqlite3·mcap)의 이미지에서 사람 얼굴·번호판 같은 대상을 GroundingDINO·OpenCLIP·SegmentAnything2·YOLO 로 찾아 가우시안 블러로 가린 익명화 백 파일을 만든다(자율주행 생태계 도구이며 ROP 직접 범위가 아니다). [사실][^ref-1309] 운영 기록으로 상황을 재현하거나 기록을 외부와 공유하기 전에 영상 기록의 얼굴 등을 가리는 익명화 단계가 두 영역의 경계가 될 것으로 보이나, 로봇 플릿 재현에서 익명화가 재현 충실도에 주는 영향을 다룬 자료는 확인하지 못했다. [추정][^ref-1309][^ref-831]
- [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ 54. 시험·형식 검증·벤치마크·[55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md): Open-RMF 문서는 시뮬레이션 로봇이 배터리 소모·충돌 비용이 없어 시나리오를 반복해 수정을 확인하고 드문 예외를 살필 수 있으며, 장시간 시뮬레이션으로 배치 전에 시설 소유자의 확신을 높일 수 있다고 설명한다. [사실][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ 55. 현장 조사·설치·시운전: 설비 제어 분야의 가상 시운전 정의(VDI/VDE 3693)와 실제 제어기·가상화 인스턴스를 섞은 분산 가상 시운전 연구가 있어 36. 가상 시운전·실제 상황 재현의 결과가 55. 현장 조사·설치·시운전의 현장 시운전 준비로 넘어갈 것으로 보이나, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차는 확인하지 못했다(PLC·설비 제어 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상, [oq-255](../../open-questions.md)). [추정][^ref-1126][^ref-1130][^ref-406]
    - 36. 가상 시운전·실제 상황 재현 ↔ 54. 시험·형식 검증·벤치마크: Kadian 외(RA-L 2020)는 시뮬레이션–현실 상관 계수(Sim-vs-Real Correlation Coefficient, SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 가 0.18 이었으나 시뮬레이션 매개변수를 조정해 0.844 로 높였다고 보고했다(단일 로봇 주행 대상). [사실][^ref-1127] NASA-STD-7009B(2024-03-05)는 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준이다. [사실][^ref-1133] F. 연동 항목의 국가로봇테스트필드 과제 보도도 이 연결에 해당한다.
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md): Gazebo Fuel 서버의 모델·월드를 내려받고 올리는 gz-fuel-tools 의 README 로드맵은 원격 모델의 새 버전이 올라왔을 때 이를 감지하는 방법을 아직 정해야 할 과제로 적고 해시 기반 방식을 아이디어로 든다. [사실][^ref-1313]
- [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md): IDTA 'Provision of Simulation Models' 서브모델이 제조사·유통사에 시뮬레이션 모델 파일을 요청하는 사용 사례를 두므로, 로봇·설비 제조사가 가상 시운전용 모델을 어떤 형식·충실도로 제공할지가 다사업자 계약·데이터 제공 항목이 될 것으로 보인다(로봇 플릿 조달 계약에 넣은 사례는 미확인). [추정][^ref-1314]
    - 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md): Gazebo(클래식) 모델 데이터베이스 규칙은 `database.config` 의 license 요소로 모델 라이선스를 지정하고 CC BY 3.0 Unported 를 권장하며(요구가 아니라 권장), 각 모델의 `model.config` 에 작성자 이름·이메일을 필수로 적게 한다([oq-292](../../open-questions.md)). [사실][^ref-1231]
    - 34. 시뮬레이션·예측용 디지털 트윈 ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md): Kassem·Michahelles(Mensch und Computer 2022 워크숍)는 협동 로봇이 공장·물류·제조 현장에 들어오면서 사람–기계 상호작용을 빠르게 평가할 필요가 커졌다고 보고, 소비자용 VR·AR 헤드셋으로 로봇을 가상으로 흉내 내 사용자 연구에 쓰는 방법과 방향을 제시했다(이동로봇 플릿 도입 전 작업자 수용성을 가상 환경으로 측정한 사례는 찾지 못했다). [사실][^ref-1311]
    - 35. 처리능력·규모·배치 설계 ↔ 60. 노동·수용성·접근성: H. 실행·협업·예외 복구 항목의 Howard(2026) 결과에서 동기화 손실의 비용이 주로 노동 쪽에 떨어진 것은 노동 비용 측면의 근거이며, 수용성·노동 영향의 직접 근거는 아니다(논문은 비용 분석이다). [사실][^ref-822]
- [Q. 현장 유형별 적용](../site-type-applications/index.md) — 현장마다 다른 요구는 Q. 현장 유형별 적용에 모으고, 현장 유형에 공통인 시뮬레이션 기능은 이 대분류에 둔다. 아래의 예제 월드·벤치마크·경진대회 시나리오는 실제 현장 배치가 아니다.
    - 현장 유형 물류창고 — [61. 물류창고](../site-type-applications/warehouse.md): CJ대한통운은 2021-11 현실 물류센터와 같은 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획을 발표하고 작업 동선·재고 배치·설비 효율 최적화를 목표로 들었으나(벤더 주장), 이후 적용 결과는 확인하지 못했다([oq-084](../../open-questions.md)). [추정][^ref-526] 위 A. 기획·사업, G. 계획·최적화, H. 실행·협업·예외 복구, L. AI·학습 기술 항목의 Howard·FAIM 2025·Garg 외·Smit 외 연구도 물류창고 조건이다.
    - 현장 유형 제조 공장 — [62. 제조 공장](../site-type-applications/manufacturing-plant.md): Stączek 외(Sensors, 2021-11)는 통로가 좁은 생산 홀의 AMR 운영 환경을 ROS 와 연결한 Gazebo 디지털 트윈으로 만들어 현장 시험 전에 위치 추정·주행·작업 시간을 확인했고, 통로에 회전용 홈을 내는 배치 변경안에서 도킹 복귀 시간이 평균 44초에서 22.5~23.3초로 줄었다고 보고했다(34. 시뮬레이션·예측용 디지털 트윈·35. 처리능력·규모·배치 설계와 연결. 수치는 저자 사례 연구의 보고값이며 검증 단계에서 다시 대조하지 못했다). [사실][^ref-1307] 최성욱·박상철·왕지남(2008)은 자동차 차체 생산라인의 PLC 코드 검증을 위해 실제 PLC 와 3D 가상 공정 시뮬레이터를 양방향 통신으로 잇는 가상 플랜트 구축 절차를 제안했다(PLC 코드 가상 시운전은 설비 업체·통합자 쪽 연계 대상이며 방법 근거로만 쓴다). [사실][^ref-1131] 2026-08 보도에 따르면 아바코는 산업통상자원부 산업 AI 솔루션 실증확산 지원사업(이차전지 분야, 한국생산기술연구원 주관)에서 AMR 스마트 물류 시스템을 개발·실증하며 실물 설비 구축 전에 디지털 트윈 가상 환경에서 물류 동선과 장비 운용을 검증했고 공정물류 다운타임 20% 절감·물류 자동화율 90% 이상을 달성했다고 밝혔으나, 이는 벤더 주장이며 수치의 기준선·측정 방법은 공개되지 않았다. [추정][^ref-1316] E. 사물·사람·실시간 상태와 H. 실행·협업·예외 복구 항목의 ARIAC 시나리오도 제조 공장을 본뜬 경진대회 시뮬레이션이다.
    - 현장 유형 병원 — [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): F. 연동 항목의 고려대학교 구로병원 약품 배송 로봇 재현과 G. 계획·최적화 항목의 Lee 외 저자 의견이 해당한다.
    - 현장 유형 상업 시설 — [64. 상업 시설](../site-type-applications/commercial-facilities.md): Open-RMF 예제 호텔 월드는 로비와 객실 2개 층에 승강기 2대·여러 문·로봇 플릿 3개(로봇 4대)를 담고, 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 플릿·설비·사람의 상호작용과 청소 작업을 보이는 시뮬레이션 예제다(실제 시설 사례가 아니다). [사실][^ref-104] F. 연동 항목의 다층 호텔 경로 계획 연구와 E. 사물·사람·실시간 상태 항목의 군중 시뮬레이션도 상업 시설 조건이다.
    - 현장 유형 가정 — [65. 가정·공동주택](../site-type-applications/home-and-apartment.md): BEHAVIOR-1K 는 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(Behavior Domain Definition Language, BDDL)로 명세하고 장면 50개와 주석 객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크다(33. 시나리오 모델·편집과 연결, 실제 가정 배치가 아니다). [사실][^ref-971] F. 연동 항목의 아파트 단지 로봇 친화형 환경 인증 모델도 이 현장 유형에 해당한다.
    - 현장 유형 실외 — [66. 실외](../site-type-applications/outdoor.md): Open-RMF 예제 캠퍼스 월드는 GPS(WGS84) 좌표를 쓰는 넓은 실외 지도에서 여러 배송 로봇이 위치를 플릿 어댑터에 보내는 시뮬레이션 예제다(33. 시나리오 모델·편집과 연결, 실제 캠퍼스 배치가 아니다). [사실][^ref-104]
    - 현장 유형 기타 — [67. 기타 현장](../site-type-applications/other-sites.md): Ortega 외(Frontiers in Robotics and AI, 2024)는 실측 점유 격자로 모델링한 대학 건물 1층을 대상으로 동적 요소와 수용 기준(위치 추정 오차·충돌 회피)을 명시한 실행 가능한 이동로봇 시뮬레이션 시험 시나리오를 구성했다(36. 가상 시운전·실제 상황 재현과 연결, 시뮬레이션 시험 사례이며 현장 기록 재생은 다루지 않는다). [사실][^ref-1134]

**아직 다루지 않은 연결:** [2. 사용 사례·요구·책임 범위](../planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md), [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md), [10. 채팅으로 로봇 구성](../chat-based-configuration-and-operation/chat-robot-configuration.md)(oq-129 관련 부분 근거만 있음), [40. 운영 절차·요청 창구](../field-operations-and-monitoring/operating-procedures-and-request-channels.md), [56. 운영 이관·확대·교육](../verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)과 이 대분류의 세부영역을 잇는 근거는 이번 조사에서 찾지 못했다.

[^ref-822]: Howard, T. L. (California Polytechnic State University, San Luis Obispo, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities, 2026-06, https://digitalcommons.calpoly.edu/theses/3387, 접근일 2026-10-09
[^ref-1165]: Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation, 2024-08-28, https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html, 접근일 2026-10-09 (원문 미열람)
[^ref-527]: NVIDIA, NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins, 2025-01-06, https://blogs.nvidia.com/blog/mega-omniverse-blueprint, 접근일 2026-10-09
[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-10-09 (원문 미열람)
[^ref-1314]: IDTA (Industrial Digital Twin Association, admin-shell-io/submodel-templates), Provision of Simulation Models (IDTA 02005) 1.0 — README, 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Provision%20of%20Simulation%20Models, 접근일 2026-10-09
[^ref-1133]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-10-09 (원문 미열람)
[^ref-1127]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-10-09 (원문 미열람)
[^ref-833]: Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving, 2026-07-15, https://arxiv.org/abs/2607.14387, 접근일 2026-10-09 (원문 미열람)
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-10-09 (원문 미열람)
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC 2025 Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-10-09
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-10-09 (원문 미열람)
[^ref-416]: Rana, K., Haviland, J., Garg, S., Abou-Chakra, J., Reid, I., & Suenderhauf, N. (CoRL 2023, arXiv), SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning, 2023-07-12, https://arxiv.org/abs/2307.06135, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-10-09
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12-14, https://arxiv.org/abs/2312.09067, 접근일 2026-10-09 (원문 미열람)
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-10-09 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-10-09 (원문 미열람)
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-10-09 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-10-09
[^ref-1087]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-10-09
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-10-09
[^ref-1310]: 파이낸스스코프 (윤영훈), 클로봇, 국책사업으로 피지컬AI 기술 표준 이끈다...산자부 주관사 선정, 2025-07-11, https://www.finance-scope.com/article/view/scp202507110007, 접근일 2026-10-09
[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-10-09 (원문 미열람)
[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-10-09 (원문 미열람)
[^ref-521]: Le, T. V., & Fan, R., Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-09 (원문 미열람)
[^ref-409]: 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105), 2023, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381, 접근일 2026-10-09 (원문 미열람)
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-10-09 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-10-09 (원문 미열람)
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-10-09 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-10-09 (원문 미열람)
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-10-09 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-10-09 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-10-09 (원문 미열람)
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-10-09 (원문 미열람)
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-10-09 (원문 미열람)
[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-10-09 (원문 미열람)
[^ref-1129]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-10-09 (원문 미열람)
[^ref-1306]: Garg, V., Maywald, J. D., & Naman, M. (International Journal of Retail & Distribution Management 53(10-11)), Optimising human-robot collaboration for efficiency in retail warehousing, 2025-10-14, https://www.emerald.com/ijrdm/article/53/10-11/1123/1303314/Optimising-human-robot-collaboration-for, 접근일 2026-10-09
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-09
[^ref-106]: 한국교통연구원(인증스마트물류센터), 인증스마트물류센터, 미확인, https://cslc.koti.re.kr/, 접근일 2026-10-09 (원문 미열람)
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-09
[^ref-741]: Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10, https://arxiv.org/abs/2510.20808, 접근일 2026-10-09 (원문 미열람)
[^ref-1308]: Smit, I. G., Bukhsh, Z., Pechenizkiy, M., Alogariastos, K., Hendriks, K., & Zhang, Y. (arXiv), Learning Efficient and Fair Policies for Uncertainty-Aware Collaborative Human-Robot Order Picking, 2024-04-09, https://arxiv.org/abs/2404.08006, 접근일 2026-10-09
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-10-09 (원문 미열람)
[^ref-1303]: Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020), Simulation-based Testing for Early Safety-Validation of Robot Systems, 2020-11-20, https://arxiv.org/abs/2011.10294, 접근일 2026-10-09
[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-10-09 (원문 미열람)
[^ref-1312]: Wind River (Engblom, J. 인터뷰, Buchwieser, A.), Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser, 2014-11-20, https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser, 접근일 2026-10-09
[^ref-1304]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09
[^ref-1309]: Autoware Foundation (autowarefoundation GitHub), autoware_rosbag2_anonymizer — README, 미확인, https://github.com/autowarefoundation/autoware_rosbag2_anonymizer, 접근일 2026-10-09
[^ref-1126]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-10-09 (원문 미열람)
[^ref-1130]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-10-09 (원문 미열람)
[^ref-1313]: Open Robotics (gazebosim/gz-fuel-tools GitHub), Gazebo Fuel Tools — README, 미확인, https://github.com/gazebosim/gz-fuel-tools, 접근일 2026-10-09
[^ref-1231]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-10-09 (원문 미열람)
[^ref-1311]: Kassem, K., & Michahelles, F. (Mensch und Computer 2022 Workshop Proceedings, Gesellschaft für Informatik), Exploring Human-robot Interaction by Simulating Robots, 2022-09, https://dl.gi.de/items/1f2227be-b32d-467c-bf94-77d37e5194ce/full, 접근일 2026-10-09
[^ref-1307]: Stączek, P., Pizoń, J., Danilczuk, W., & Gola, A. (Sensors 21(23):7830), A Digital Twin Approach for the Improvement of an Autonomous Mobile Robots (AMR's) Operating Environment—A Case Study, 2021-11-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC8659435/, 접근일 2026-10-09
[^ref-1131]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-10-09 (원문 미열람)
[^ref-1316]: 파이낸스스코프, 아바코, AMR 스마트 물류 시스템 개발·실증 완료… 피지컬 AI 사업 가속, 2026-08-14, https://www.finance-scope.com/article/view/scp202608140009, 접근일 2026-10-09
[^ref-526]: CJ대한통운, 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료), 2021-11, https://www.cjlogistics.com/ko/newsroom/news/NR_00000905, 접근일 2026-10-09 (원문 미열람)
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03-14, https://arxiv.org/abs/2403.09227, 접근일 2026-10-09 (원문 미열람)
[^ref-1134]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-10-09 (원문 미열람)

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 62건 / 전체 1248건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/glossary/index.md (요약: 용어 353개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [33, 34, 35, 36] 에 걸린 30건 / 전체 301건)

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
