(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-17
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 36. 가상 시운전·실제 상황 재현 (I. 설계·시뮬레이션)
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

### runs/2026-09-30-17/target.json

```json
{
  "run_id": "2026-09-30-17",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 126,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 36,
    "area_name": "36. 가상 시운전·실제 상황 재현",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=36"
}
```

### runs/2026-09-30-17/research.json

```json
{
  "run_id": "2026-09-30-17",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 36,
    "area_name": "36. 가상 시운전·실제 상황 재현",
    "category": "I. 설계·시뮬레이션"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 가상 시운전의 시험 구성(MiL·SiL·HiL), 에뮬레이션, 로그 재생·비반응 재생, 시뮬레이션–현실 상관 지표, 모델·시뮬레이션 신뢰도 평가 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·제조 공장·병원·기타 현장의 가상 시운전·재현 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 실행 전 계획 검증, 가상 시운전, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리의 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDI/VDE 3693, NASA-STD-7009, Open-RMF 시뮬레이션, rosbag2, VDA 5050 범위 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-132, oq-156 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]",
    "가상 시운전은 표준·문헌에서 어떻게 정의되고 어떤 시험 구성(MiL·SiL·HiL)을 쓰며, 분산 시스템·여러 로봇으로 어떻게 넓혀지는가? (섹션 4·6·7 겨냥)",
    "여러 로봇의 관제·오케스트레이션을 설치 전에 가상 환경에서 시험하는 도구와 현장 사례(물류창고·제조 공장·병원·기타)는 무엇인가? (섹션 5·7 겨냥, 한국 사례 우선)",
    "운영 기록(로그)으로 시뮬레이션의 초기 상태와 사건을 다시 구성하는 방법과 그 한계는 무엇인가? (섹션 6·8 겨냥)",
    "재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표와 허용 기준, 승인 주체는 무엇인가? (oq-132, 섹션 6·11 겨냥)",
    "실행 전 계획 검증과 시뮬레이션 검증·실기 검증 단계에 대응하는 기존 검증 수준·신뢰도 평가 체계가 있는가? (oq-156, 섹션 6·7 겨냥)",
    "가상 시운전·재현에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·설비 업체·로봇 제조사에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDI/VDE 3693 Blatt 1 은 2025-05 개정판(39쪽, 독·영)에서 가상 시운전(virtual commissioning)을 체계적으로 정의하고 자동화 설비·기계의 수명주기 안에 위치시키며, 기본 시험 구성, 시험 방법, 필요한 모델 유형, 시뮬레이션 구성을 보완했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1165"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDI 공식 소개 페이지: 발행 2025-05, 'a clear and systematic definition of virtual commissioning' 제공, 시험 구성·시험 방법·모델 유형·시뮬레이션 구성 부분을 개정·보완. 대상 독자는 시운전·자동화·소프트웨어 엔지니어 등. 표준 본문은 유료로 미열람.",
      "as_of": "2025-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Rosenberger 외(Sensors 2023)는 VDI 3693 에 따라 가상 시운전 시험 구성을 자동화 모델만 쓰는 모델 인 더 루프(MiL), 실제 제어 언어 코드를 하드웨어와 분리해 돌리는 소프트웨어 인 더 루프(SiL), 실제 대상 하드웨어(가상 머신·컨테이너로 가상화한 하드웨어 포함)를 쓰는 하드웨어 인 더 루프(HiL)로 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1172"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MiL: 가장 추상적, 자동화 모델만 필요 / SiL: IEC 61131 코드 사용, 하드웨어와 독립 실행 / HiL: 실제 대상 하드웨어와 올바른 프로그래밍 언어, 가상화된 하드웨어(VM·컨테이너)도 포함.",
      "as_of": "2023-03-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "제조 공장 사례: Rosenberger 외(Sensors 2023)는 가상 시운전을 제어 루프에서 분산 에지 컴퓨팅 시스템 전체로 넓혀, 물리 설비 시뮬레이션과 응용 사이의 직접 피드백 루프로 여러 장치를 함께 시험하는 구조 3가지를 제안하고, 끝단 팔레타이징 포장 설비 시뮬레이션에 실제 제어기 3대와 가상화 인스턴스 9대를 붙여 시험했으나, 시운전 기간·비용 절감 수치는 제시하지 않았고 비실시간 시뮬레이션이라는 한계를 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1172"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "구조: 단일 장치+네트워크 / 다수 장치+단일 시뮬레이션 / 다수 분산 시뮬레이션. 사례: palletizing portal packaging system, ctrlX CORE 3대+가상 9대. 한계: 비실시간, 스마트 계약 시험 미완, 단일 시나리오.",
      "as_of": "2023-03-28",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f4",
      "claim": "Open-RMF 의 시뮬레이션 문서는 traffic_editor 로 도면에 교통 정보·경유점·공유 자원을 주석한 뒤 building_map_generator 가 Gazebo·Ignition 세계와 플릿 어댑터용 주행 그래프를 자동 생성하고, 로봇(slotcar)·문·승강기·작업셀(디스펜서·인제스터)·군중(Menge) 플러그인으로 배치 전 시험, 로봇 추가 시 규모 평가, 드문 실패 상황 검토를 할 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'Long running simulations can instill confidence in facility owners prior to deployment.' 플러그인: slotcar 로봇, 문, 승강기(층간 캐빈·승강로 문), 작업셀, Menge 군중 시뮬레이션.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 명세는 프로젝트 관리, 통합 방법, 시운전 작업 흐름, 검증·인수 절차를 포함하는 '프로젝트 조정·수행 절차'를 명세 범위 밖에 두므로, 이 인터페이스 규격을 따르는 것만으로 여러 제조사 로봇의 시운전 절차가 정해지지는 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "범위 밖: 'commissioning workflows, validation and acceptance procedures' 를 포함한 Project Coordination and Implementation Procedures, 안전 요구, 교통 관리 로직, 운영 책임 배분, 사이버보안. (재인용: 2026-09-30-14)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "ROS 2 의 rosbag2 는 토픽 메시지를 시각과 함께 기록하고 재생하며, --clock 옵션으로 재생 세션 동안 /clock 을 발행해 재생 데이터에 맞춘 시뮬레이션 시각을 주고, 일시정지·재개·탐색·속도 조정·한 메시지씩 진행 같은 재생 제어 서비스를 제공하며 기본 저장 형식은 MCAP 이다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 저장소 README: '/clock is published only while a playback session is active.' 재생 제어: pause, resume, seek, set-rate, play_next. 저장 백엔드: MCAP 기본, SQLite3 선택.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f7",
      "claim": "연계 대상: 자율주행 분야의 Waymax(Gulino 외, 2023)는 Waymo Open Motion Dataset 같은 실제 주행 기록으로 다중 에이전트 시나리오를 초기화하거나 재생하고, 단순 재생을 넘어 상호작용이 가능하도록 학습된 행동 모델과 규칙 기반 행동 모델을 함께 넣은 가속 시뮬레이터다.",
      "tag": "사실",
      "source_ids": [
        "ref-1168"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 실제 주행 데이터로 'initialize or play back a diverse set of multi-agent simulated scenarios', 학습·수작성 행동 모델로 시뮬레이션 안의 상호작용을 지원. TPU·GPU 가속. 초록만 확인.",
      "as_of": "2023-10-12",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "기록된 궤적을 그대로 재생하는 방식은 주변 에이전트가 바뀐 조건에 반응하지 않으므로, 실제 운영 기록으로 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교하려면 주변 로봇·사람을 반응형 행동 모델로 바꾸는 단계가 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1168",
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Waymax 가 재생 외에 상호작용용 행동 모델을 둔 설계(f7)와 rosbag2 재생이 기록된 메시지를 시각대로 다시 발행하는 방식(f6)에서 도출한 추정. 로봇 플릿에서 이를 검증한 자료는 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f9",
      "claim": "Kadian 외(2020)는 시뮬레이션에서의 성능 개선이 실제 성능 개선으로 이어지는지를 재는 시뮬레이션–현실 상관 계수(SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 성공률 기준 SRCC 가 0.18 로 낮았던 원인이 에이전트가 충돌 동역학을 악용해 벽을 따라 미끄러지는 것임을 찾아 시뮬레이터 설정을 조정해 0.844 로 높였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1167"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "SRCC_Succ 0.18 → 0.844. 원인: agents 'abusing collision dynamics to slide along walls'. 과제: embodied PointGoal navigation, 로봇: LoCoBot. arXiv 초록 기준(IEEE RA-L 2020 게재).",
      "as_of": "2020-08",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "Aljalbout 외(2025)는 시뮬레이션이 추상화와 근사로 이루어져 현실과의 차이(현실 격차)를 피할 수 없다고 보고, 영역 무작위화, 현실→시뮬레이션 전이, 상태·행동 추상화, 시뮬레이션–현실 공동 학습 같은 대응 기법과 현실 격차 평가 지표를 정리했다.",
      "tag": "사실",
      "source_ids": [
        "ref-741"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'simulations consist of abstractions and approximations that inevitably introduce discrepancies'. 대상: 보행·주행·조작. Annual Review of Control, Robotics, and Autonomous Systems 2026 게재 예정. 초록만 확인.",
      "as_of": "2025-10-23",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Luckcuck 외(ACM Computing Surveys 2019)는 자율 로봇이 복잡하고 혼성적이며 안전에 중요한 시스템이어서 시험과 시뮬레이션만으로는 정확성을 보장하거나 인증에 충분한 증거를 내기 어렵다고 보고, 형식 명세·검증 기법을 보완 수단으로 정리했다.",
      "tag": "의견",
      "source_ids": [
        "ref-599"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'testing and simulation alone are insufficient to ensure the correctness of, or provide sufficient evidence for the certification of, autonomous robotics.'",
      "as_of": "2019",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "NASA-STD-7009B '모델·시뮬레이션 표준'(문서일 2024-03-05, 현행)은 모델·시뮬레이션을 개발·수용·사용하는 요구·권고·기준을 정하고, 개정판에서 개발·사용 단계의 신뢰도 평가 산출물에 초점을 두며, 결과를 쓰기 전에 수용 기준을 위임된 기술 권한자가 정의·승인하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1177"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NASA 표준 페이지: 7009B, ACTIVE, 문서일 2024-03-05. 'requirements, recommendations, and criteria with which M&S may be developed, accepted, and used'. 수용 기준은 위임된 Technical Authority 가 정의·승인.",
      "as_of": "2024-03-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "병원 사례: 고려대학교 구로병원의 약품 배송 로봇 연구(Lee 외, Digital Health 2026-03)는 2025-06-18~29 의 실제 배송 122건에서 로봇 원격측정 기록과 승강기 시스템 데이터를 모아 승강기 가동률(EOR) 59.01% 를 임계값으로 찾았고(이하에서 배송 성공률 95.5%, 90% 초과에서 실패 집중), 측정한 점유율로 모수를 정한 몬테카를로 시뮬레이션으로 승강기 탑승 실패 기제를 재현했다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실제 로그: 로봇 텔레메트리+승강기 데이터, 현장 관찰 보완. ROC 로 EOR 임계 59.01%. 실패는 승객·화물이 진입을 막는 승강기 차단이 주. 시뮬레이션은 완전한 디지털 트윈이 아닌 승강기 탑승 기하 모형.",
      "as_of": "2026-03",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "같은 연구의 저자들은 여러 병원 시험이 어려울 때 병원별 구조·통행 구성·승강기 제어 정책을 재현한 병원 디지털 트윈으로 현장 배치 전에 결과의 일반화 가능성을 부하 시험할 수 있다고 제안하고, 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰자고 했다.",
      "tag": "의견",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "저자 제안: 'hospital digital twins to stress-test generalizability before field deployment'. 승강기 가동률(EOR)을 배차 제어 신호로 사용.",
      "as_of": "2026-03",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "물류창고 사례(벤더 주장): Rockwell Automation 사례 소개에 따르면 통합자 Bastian Solutions 는 미국 남부의 약 30만 제곱피트 규모 물류센터 구축에서 컨베이어·피킹 모듈·PLC·I/O 매핑·제어 코드를 에뮬레이션으로 설치 전에 검증해 전체 프로젝트 기간을 18% 줄이고 현장 시운전을 5주 단축했다고 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1179"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 에뮬레이션으로 'resolve issues pre-installation, which reduces risk and speeds up commissioning'. 프로젝트 기간 18% 감소, 시운전 5주 절감. 측정 방법·기준선 미공개.",
      "as_of": "2024-08-28",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f16",
      "claim": "제조 공장 사례: 최성욱·박상철·왕지남(2008, 대한산업공학회 추계학술대회)은 자동차 차체 생산라인의 PLC 코드를 검증하려고 설비 상태·사건을 이산 사건 모델로 정의하고, 실제 PLC 하드웨어와 3D CAD·디지털 목업 기반 가상 공정 시뮬레이터를 양방향 통신으로 연동하는 가상 플랜트 구축 절차를 제안해 라인 안정화 기간과 비용을 줄이는 것을 목표로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1175"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 803~808쪽. 하드웨어 PLC 와 가상 공정 시뮬레이터의 co-simulation. 초록 기준.",
      "as_of": "2008-11",
      "site_type": "제조 공장",
      "flow_item": "작업 대상"
    },
    {
      "id": "f17",
      "claim": "제조 공장 사례(벤더 주장): 현대자동차그룹은 싱가포르 혁신센터(HMGICS)에서 디지털 트윈 가상 공장으로 설비·로봇 배치 변경을 실제 생산을 멈추지 않고 가상에서 먼저 검증한다고 소개하나, 시운전 기간 단축 같은 수치는 밝히지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-1176"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: '생산을 중단하지 않고도 생산 라인을 검증하고 미래의 운영 결과값을 도출할 수 있다'. 정량 수치 없음.",
      "as_of": "2023-11-21",
      "site_type": "제조 공장",
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f18",
      "claim": "기타(대학 건물) 사례: Ortega 외(Frontiers in Robotics and AI 2024-08)는 도면 DSL 로 만든 실내 환경, 동적 객체의 초기 자세, 시간·거리 조건으로 움직이는 문 같은 동적 요소, 주행 과제, 위치 추정 오차·충돌 회피 같은 수용 기준을 조합해 실행 가능한 이동로봇 시험 시나리오를 만드는 방법을 제안하고, 실측 점유 격자로 모델링한 대학 건물 1층에서 평가했으나 현장 기록의 재생은 다루지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1178"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "JSON-LD 기반 조합형 모델과 FloorPlan DSL, Gazebo 플러그인. 저자들은 시뮬레이션 환경 제작을 'modelling is time-consuming' 으로 인식되는 문제로 지적.",
      "as_of": "2024-08-02",
      "site_type": "기타",
      "flow_item": "완료·인계"
    },
    {
      "id": "f19",
      "claim": "VirTooS(Drudi 외, 2026-08 arXiv)는 ROS 2 와 Unity 를 결합해 실제 로봇과 가상 로봇이 같은 환경에서 상호작용하는 혼합 현실 실험으로 자율이동로봇(AMR) 플릿 관리(작업 배정) 전략을 시험하는 도구로, 가상·실제 센서를 함께 쓸 수 있으나 초록에는 정량 결과가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1171"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: task assignment 실험을 'seamless interaction among real and virtual robots' 환경에서 수행. ChoiRbot 기반, 소스 공개 예정. 가상 시운전·VDA 5050 언급 없음.",
      "as_of": "2026-08-26",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(설치 전에 가상으로 시운전하고 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가)에 대해, 설치 전 가상 시운전은 제조·물류 설비 제어 분야에서 VDI/VDE 3693 과 MiL·SiL·HiL 구성으로 정립되어 있고 다중 로봇 쪽에는 Open-RMF 시뮬레이션·혼합 현실 도구가 있으며, 운영 기록 재생 도구(rosbag2)와 기록 기반 시나리오 초기화(Waymax)도 있지만, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차 표준과 재현 결과의 현실 일치 판정 기준은 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165",
        "ref-1172",
        "ref-406",
        "ref-1171",
        "ref-831",
        "ref-1168",
        "ref-031",
        "ref-1167"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2(표준·시험 구성), f4·f19(다중 로봇 도구), f6·f7(기록 재생·기록 기반 초기화), f5(VDA 5050 은 시운전 절차 범위 밖), f9(예측력은 측정해야 함)를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "재현 시뮬레이션의 현실 일치 판정(oq-132)에는 비교한 여러 설정의 시뮬레이션 성능과 실제 성능 사이 상관을 보는 SRCC 같은 예측력 지표와, 결과 사용 전에 수용 기준을 권한자가 정의·승인하게 하는 NASA-STD-7009B 방식, 시나리오마다 수용 기준을 명시하는 방식을 조합할 수 있을 것으로 보이나, 로봇 플릿 재현에 이를 적용해 허용 기준을 정한 사례는 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1167",
        "ref-1177",
        "ref-1178"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9(SRCC), f12(수용 기준 승인 주체), f18(시나리오별 수용 기준)에서 도출. 사건 순서 유사도·시각 오차 지표의 로봇 플릿 적용 근거는 미확인.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f22",
      "claim": "분류 원문의 지원 단계 표시 가운데 시뮬레이션 검증·실기 검증 단계(oq-156)는 VDI/VDE 3693 의 MiL·SiL·HiL 시험 구성과 NASA-STD-7009B 의 신뢰도 평가에 부분적으로 대응시킬 수 있을 것으로 보이나, 문서 확인·구조화·어댑터 연결까지 이어지는 단계를 한 체계로 정한 기존 성숙도 체계는 이번 조사에서 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1165",
        "ref-1172",
        "ref-1177"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2(시험 구성 단계), f12(신뢰도 평가·수용 승인)에서 도출. 문서→구조화→어댑터 단계와의 대응 근거는 없음.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 36. 가상 시운전·실제 상황 재현에서 ROP가 직접 맡을 범위는 제조사 플릿·문·승강기 인터페이스의 가상 대응물을 붙여 오케스트레이션 논리와 운영 정책을 설치 전에 SiL 방식으로 시험하는 환경, 재생 가능한 형태로 시각이 맞춰진 오케스트레이션 수준 실행 기록, 기록에서 시뮬레이션 초기 상태와 사건을 구성하는 기능, 재현 결과와 실제의 차이 지표와 수용 승인 기록의 관리로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-406",
        "ref-831",
        "ref-1172",
        "ref-1167",
        "ref-1177",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4(RMF 플러그인이 문·승강기·로봇을 가상화), f6(기록·/clock 재생), f2·f3(SiL·분산 가상 시운전), f9·f12(차이 지표·수용 승인), f5(규격이 시운전 절차를 정하지 않음)에서 도출.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 시뮬레이션 자산, 로봇 내부 주행·인식 제어의 현실 격차 보정은 시뮬레이션 도구·로봇 제조사가, 컨베이어·PLC·승강기 제어 코드의 에뮬레이션과 가상 시운전은 설비 업체·통합자가, 자율주행 차량의 기록 기반 시뮬레이션은 해당 업계가 맡으므로, ROP는 이들의 가상 모델·에뮬레이터와 연결되는 인터페이스와 시험 결과를 받아 들이는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1172",
        "ref-1175",
        "ref-1179",
        "ref-741",
        "ref-1168",
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f15·f16(설비 제어 코드 가상 시운전은 설비·통합자 영역), f10(로봇 자체 제어의 현실 격차), f7(차량 기록 시뮬레이션), f4(연결용 플러그인 구조)에서 도출.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f25",
      "claim": "이 영역은 시나리오 형식의 33. 시나리오 모델·편집(f18), 시뮬레이션 엔진과 가정한 미래 실험의 34. 시뮬레이션·예측용 디지털 트윈(f4·f10), 재현의 원천 기록을 주는 18. 실시간 세계 상태·데이터 일관성과 37. 관제 화면·실행 기록(f6), 대화로 재현을 요청하는 11. 채팅으로 실제 상황 시뮬레이션 재현, 도면에서 시뮬레이션 세계를 만드는 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f4), 플릿 어댑터의 20. 로봇·제조사 관제 연동(f4·f5), 문·승강기의 22. 설비·건물 시스템 연동(f4·f13), 배차 정책의 25. 작업 배정 — MRTA(f13·f19), 원인 분석의 38. 모니터링·이상 탐지·원인 분석(f13), 계획 검증·형식 검증의 54. 시험·형식 검증·벤치마크(f11·f12), 현장 시운전의 55. 현장 조사·설치·시운전(f1·f15), 현실 격차 보정 학습의 47. AI·학습·적응과 모델 운영(f10), 적용 현장인 61. 물류창고(f15)·62. 제조 공장(f3·f16·f17)·63. 병원·의료(f13·f14)·67. 기타 현장(f18)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1178",
        "ref-406",
        "ref-741",
        "ref-831",
        "ref-031",
        "ref-943",
        "ref-1171",
        "ref-599",
        "ref-1177",
        "ref-1165",
        "ref-1179",
        "ref-1172",
        "ref-1175",
        "ref-1176"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결의 근거 finding 을 괄호로 표기. 11. 채팅으로 실제 상황 시뮬레이션 재현 연결은 분류 원문 C 주석(재현은 33·36번과 짝)에 따른 것.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1165",
      "org": "VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik)",
      "title": "VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions",
      "published": "2025-05",
      "url": "https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "가상 시운전의 정의와 수명주기 내 위치, 시험 구성·시험 방법·모델 유형·시뮬레이션 구성을 다루는 VDI/VDE 지침 2025-05 개정판의 공식 소개 페이지. 표준 본문은 유료로 열람하지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (Open Robotics 외, ros2/rosbag2 저장소)",
      "title": "rosbag2 README",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 토픽 기록·재생 도구 rosbag2 의 공식 README. /clock 발행, 재생 제어 서비스, MCAP·SQLite3 저장 형식을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/rosbag2/rolling/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1167",
      "org": "Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L)",
      "title": "Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?",
      "published": "2020-08",
      "url": "https://arxiv.org/abs/1912.06321",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "시뮬레이션 평가가 실제 성능을 예측하는 정도를 재는 SRCC 지표를 제안하고 LoCoBot PointGoal 주행에서 시뮬레이터 조정으로 SRCC 를 0.18 에서 0.844 로 높였다. arXiv 초록만 읽었다.",
      "fetched": false,
      "fetched_via": null,
      "source_unopened": true
    },
    {
      "id": "ref-1168",
      "org": "Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv)",
      "title": "Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research",
      "published": "2023-10-12",
      "url": "https://arxiv.org/abs/2310.08710",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실제 주행 기록으로 다중 에이전트 시나리오를 초기화·재생하고 행동 모델로 상호작용을 넣는 가속 자율주행 시뮬레이터. arXiv 초록만 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 배치를 Gazebo·Ignition 으로 시뮬레이션하는 방법(도면 기반 세계 생성, 로봇·문·승강기·작업셀·군중 플러그인)과 배치 전 시험의 목적을 설명하는 장.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/simulation.md",
      "source_unopened": false
    },
    {
      "id": "ref-943",
      "org": "Lee 외 (Digital Health, SAGE)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고려대학교 구로병원의 실제 약품 배송 로봇 기록 122건과 승강기 데이터로 승강기 가동률 임계값을 찾고 몬테카를로 시뮬레이션으로 탑승 실패 기제를 재현한 연구. 전문을 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1171",
      "org": "Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv)",
      "title": "VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots",
      "published": "2026-08-26",
      "url": "https://arxiv.org/abs/2608.26066",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실제·가상 로봇이 함께 움직이는 혼합 현실 환경에서 AMR 플릿 관리(작업 배정) 실험을 하는 ROS 2–Unity 도구. arXiv 초록만 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1172",
      "org": "Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545)",
      "title": "Virtual Commissioning of Distributed Systems in the Industrial Internet of Things",
      "published": "2023-03-28",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDI 3693 의 MiL·SiL·HiL 구분을 바탕으로 가상 시운전을 분산 에지 시스템으로 넓히는 구조 3가지를 제안하고 팔레타이징 설비 시뮬레이션으로 시험했다. 전문을 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-599",
      "org": "Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5))",
      "title": "Formal Specification and Verification of Autonomous Robotic Systems: A Survey",
      "published": "2019",
      "url": "https://arxiv.org/abs/1807.00048",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자율 로봇 시스템의 형식 명세·검증 기법과 과제를 정리한 조사 논문. 시험·시뮬레이션만으로는 인증 증거가 부족하다고 본다. arXiv 초록만 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-741",
      "org": "Aljalbout, E., Xing, J., Romero, A. 외 (arXiv)",
      "title": "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices",
      "published": "2025-10-23",
      "url": "https://arxiv.org/abs/2510.20808",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇 공학의 현실 격차 원인과 대응 기법(영역 무작위화, 현실→시뮬레이션, 추상화, 공동 학습), 평가 지표를 정리한 조사 논문. arXiv 초록만 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1175",
      "org": "최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회)",
      "title": "자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스",
      "published": "2008-11",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자동차 차체 생산라인의 PLC 코드를 실제 PLC 와 가상 공정 시뮬레이터의 연동으로 검증하는 가상 플랜트 구축 절차를 제안한 국내 학술대회 논문. DBpia 초록만 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1176",
      "org": "현대자동차그룹",
      "title": "가상의 디지털 공간에 세운 쌍둥이 공장",
      "published": "2023-11-21",
      "url": "https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "현대자동차그룹이 HMGICS 디지털 트윈 가상 공장으로 설비·로봇 배치 변경을 가상에서 먼저 검증한다고 소개하는 회사 콘텐츠. 정량 수치는 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330",
      "source_unopened": false
    },
    {
      "id": "ref-1177",
      "org": "NASA",
      "title": "NASA-STD-7009B Standard for Models and Simulations",
      "published": "2024-03-05",
      "url": "https://standards.nasa.gov/standard/NASA/NASA-STD-7009",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "모델·시뮬레이션의 개발·수용·사용 요구와 신뢰도 평가를 정한 NASA 표준의 공식 페이지(개정 B, 현행). 표준 본문 PDF 는 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1178",
      "org": "Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI)",
      "title": "Composable and executable scenarios for simulation-based testing of mobile robots",
      "published": "2024-08-02",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "도면 DSL·초기 자세·동적 객체·과제·수용 기준을 조합해 이동로봇 시뮬레이션 시험 시나리오를 만드는 방법을 제안하고 대학 건물에서 평가했다. 전문을 읽었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1179",
      "org": "Rockwell Automation",
      "title": "Emulation Technology Speeds Up Warehouse Automation",
      "published": "2024-08-28",
      "url": "https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "Bastian Solutions 가 물류센터 구축에서 컨베이어·피킹 모듈·PLC 제어 코드를 에뮬레이션으로 설치 전 검증했다는 벤더 사례. 성과 수치는 벤더 주장이다.",
      "fetched": true,
      "fetched_via": "webfetch",
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
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "관제와 AGV·AMR 사이 통신 인터페이스를 정한 VDA 5050 공식 명세(현재 main 은 3.0.0). 시운전·검증·인수 절차는 범위 밖에 둔다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
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
      "rationale": "섹션 3: f20(핵심 질문 답, 추정), f5(규격이 시운전 절차를 정하지 않음), f11(시험·시뮬레이션만으로는 증거 부족이라는 의견) / 섹션 4: 가상 시운전 정의 f1, MiL·SiL·HiL f2, 로그 재생·/clock f6, 비반응 재생 f8(추정), SRCC f9, 현실 격차 f10, 신뢰도 평가·수용 승인 f12 / 섹션 5: 물류창고 — f15(예외·성과, 벤더 주장 병기), 제조 공장 — f3(수행 자원)·f16(작업 대상: PLC 코드)·f17(벤더 주장 병기), 병원 — f13(예외·성과: 실제 기록 기반 승강기 실패 재현)·f14(제약, 의견), 기타(대학 건물) — f18(완료·인계: 수용 기준). 상업 시설·가정·실외 로봇 현장 사례는 찾지 못했음을 명시(f7 은 자율주행 방법 참고로만) / 섹션 6: 실행 전 계획 검증 f11, 가상 시운전 f1~f4·f19, 운영 기록 기반 재현 f6~f8·f13, 시뮬레이션–현실 차이 관리 f9·f10·f21 / 섹션 7: VDI/VDE 3693 f1, NASA-STD-7009B f12, Open-RMF 시뮬레이션 f4, rosbag2·MCAP f6, VDA 5050 범위 f5, Waymax f7, VirTooS f19 / 섹션 8: f3·f9·f10·f11·f13·f16·f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67. 18. 실시간 세계 상태·데이터 일관성은 재현의 원천 기록, 34. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험으로 구분해 서술 / 섹션 11: 기존 oq-132(f21 로 부분 근거)·oq-156(f22 로 부분 근거) 미해결 유지와 open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f13·f14, 55. 현장 조사·설치·시운전 페이지에 f1·f2·f15 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "소프트웨어 인 더 루프",
      "term_en": "Software-in-the-Loop (SiL)",
      "definition": "실제 제어 언어로 작성한 제어 프로그램을 대상 하드웨어 없이 가상 제어기에서 돌려 설비 시뮬레이션 모델과 연결해 시험하는 가상 시운전 구성이다."
    },
    {
      "term_ko": "하드웨어 인 더 루프",
      "term_en": "Hardware-in-the-Loop (HiL)",
      "definition": "나중에 현장에 쓸 실제 제어 하드웨어(또는 그 가상화 인스턴스)를 설비 시뮬레이션 모델과 연결해 제어 프로그램과 하드웨어·통신을 함께 시험하는 가상 시운전 구성이다."
    },
    {
      "term_ko": "시뮬레이션–현실 상관 계수",
      "term_en": "Sim-vs-Real Correlation Coefficient (SRCC)",
      "definition": "여러 방법·설정을 비교할 때 시뮬레이션에서의 성능 차이가 실제 로봇에서의 성능 차이와 얼마나 같은 방향으로 나타나는지를 상관계수로 재는 시뮬레이션 예측력 지표다."
    },
    {
      "term_ko": "모델·시뮬레이션 신뢰도 평가",
      "term_en": "Models and Simulations Credibility Assessment (NASA-STD-7009)",
      "definition": "모델·시뮬레이션 결과를 의사결정에 쓰기 전에 검증·타당성 확인 등 신뢰도 요소를 평가하고 미리 승인된 수용 기준과 대조하는 절차다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 20. 로봇·제조사 관제 연동, 55. 현장 조사·설치·시운전 | 근거: f1 | 종류: 일반",
    "실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 19. 사람·보행자 모델, 33. 시나리오 모델·편집 | 근거: f8 | 종류: 일반",
    "물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 3. 경제성·조달·사업 모델 | 근거: f15 | 종류: 일반",
    "한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 63. 병원·의료, 22. 설비·건물 시스템 연동 | 근거: f14 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "oq-132 미해결: 로봇 플릿 재현에 사건 순서 유사도·시각 오차·처리량 오차 지표와 허용 기준을 적용한 자료를 찾지 못함(f21 로 후보만 제시)",
      "oq-156 미해결: 문서 확인→구조화→시뮬레이션 연결→어댑터 연결→시뮬레이션 검증→실기 검증을 한 체계로 정한 기존 성숙도 체계를 찾지 못함(f22)",
      "NASA-STD-7009 신뢰도 평가 척도(요소 8개, 0~4 점수, 전체 신뢰도는 최저 점수)는 검색 요약에만 있어 넣지 않음",
      "Striffler·Voigt(2023) 가상 시운전 종합 리뷰(Journal of Manufacturing Systems 71)는 ScienceDirect 403 으로 열지 못해 넣지 않음",
      "Kulkarni(IISE) 창고 로봇 가상 시운전 논문 소개 페이지 403, Siemens Ferrero·Wipro PARI 사례는 신규 출처 상한으로 넣지 않음",
      "VAL(PDDL 계획 검증기) 논문 PDF 추출 실패, 공식 저장소 README 에 검증 항목 설명이 없어 실행 전 계획 검증의 전용 근거를 넣지 못함",
      "Waymax 의 로그 재생 대 IDM 반응형 에이전트 모드 구분은 검색 요약에만 있어 초록 범위로 한정(f7)",
      "f15 Bastian Solutions 수치(18%, 5주)는 벤더 주장이며 측정 방법·기준선 미확인",
      "f17 현대자동차그룹 콘텐츠 제목은 검색 결과 제목 기준, 정량 수치 없음",
      "f16 최성욱 외 2008 논문은 초록만 확인",
      "f9·f10·f11 은 arXiv 초록만 확인",
      "상업 시설·가정·실외 로봇 현장의 가상 시운전·재현 사례를 찾지 못함",
      "국내 가상 시운전 표준(KS)이나 공공 지침은 찾지 못함"
    ],
    "scope_violations": [
      "f3·f15·f16: PLC·컨베이어 제어 코드의 가상 시운전은 원문 19장 '시설·설비 제어' 연계 대상이므로 방법 근거로만 쓰고 f24 에서 '연계 대상: '으로 구분함",
      "f7: 자율주행 차량 기록 기반 시뮬레이션은 원문 19장 '업종별 조건'(실외 차량) 연계 대상이므로 claim 을 '연계 대상: '으로 시작하고 재현 방법의 참고로만 제안함",
      "f9·f10: 로봇 주행·조작 정책의 현실 격차 보정은 원문 19장 '로봇 자체 지능·제어' 연계 대상이며, ROP 에는 예측력 지표 개념만 가져오는 것으로 f23·f24 에서 구분함"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 19회/30, 신규 출처 15건/15(ref-1165~ref-1179, 예약 구간 안)로 신규 출처 상한에 도달해 Siemens Ferrero·Wipro PARI 가상 시운전 사례, Siemens Plant Simulation AGV 가상 시운전 블로그, Striffler·Voigt 리뷰를 출처로 넣지 못했다. 재사용 1건(ref-031): 값은 이전 브리프 2026-09-30-14 출처 표를 따랐고 이번에 GitHub 공식 저장소 원문을 다시 열어 시운전·검증·인수 절차가 범위 밖임을 확인했다. 원문 열람: 16건 모두 열었으나(webfetch 13, github_raw 3) ref-1167·ref-1168·ref-1171·ref-599·ref-741 는 arXiv 초록, ref-1175 는 DBpia 초록, ref-1165·ref-1177 은 표준 공식 소개 페이지만 읽었다. ScienceDirect·CRB·Strathprints PDF·IEEE CSDL 은 열지 못했다. 교차 확인 0건(주장마다 독립 출처 2곳을 찾지 못함). 벤더 주장 2건(f15·f17)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '설치 전 가상 시운전은 설비 제어 분야에서 표준·시험 구성이 정립되어 있고 다중 로봇 시뮬레이션·기록 재생 도구도 있으나, 여러 제조사 플릿 전체의 가상 시운전 절차 표준과 재현 결과의 현실 일치 판정 기준은 확인하지 못했다'는 추정이다. 현장 유형 사례는 물류창고(f15, 벤더)·제조 공장(f3·f16·f17)·병원(f13·f14, 한국)·기타(f18, 대학 건물)이며 상업 시설·가정은 찾지 못했고 실외는 자율주행 방법 참고(f7)뿐이다. 국내 자료는 고려대 구로병원 연구(ref-943), 아주대 학술대회 논문(ref-1175), 현대자동차그룹 콘텐츠(ref-1176)다. 18. 실시간 세계 상태·데이터 일관성은 재현의 원천 기록으로, 34. 시뮬레이션·예측용 디지털 트윈은 엔진·가정한 미래 실험으로 구분해 f25 에 적었다. L. AI·학습 기술 관련은 현실 격차 보정 학습(f10)을 47. AI·학습·적응과 모델 운영과 함께 제안했다. 용어집에 이미 있는 가상 시운전·로그 재생·현실 격차·시나리오 재구성·사전 실행 계획 검증·백 파일·MCAP·디지털 섀도·시뮬레이션 모델 검증·타당성 확인·승강기 가동률은 후보로 내지 않았다. 기존 열린 질문 oq-132·oq-156 은 부분 근거(f21·f22)만 있어 해결 제안하지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-17/verification.json

```json
{
  "run_id": "2026-09-30-17",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDI 공식 페이지(WebFetch)에서 발행 2025-05, 39쪽, 독·영, 가상 시운전의 체계적 정의·수명주기 내 위치, 기본 시험 구성·시험 방법·모델 유형·시뮬레이션 구성의 개정·보완 문구가 일치한다. 발행 기관 자료이며 표준 본문(유료)은 열지 않았다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1172 는 검증자가 PMC(reCAPTCHA)·MDPI(403)로 다시 열지 못해 검색 결과로 서지(Rosenberger 외, Sensors 23(7):3545, 2023-03-28)와 HiL·가상 시운전 주제만 확인했다. MiL·SiL·HiL 세부 정의는 리서치의 원문 열람 기록(fetched: true, PMC 전문)에 의존한다. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "서지와 '분산 스트림 처리 시스템을 HiL 로 연결한 산업 설비 시뮬레이션으로 시험' 은 검색 결과로 확인했다. 구조 3가지, 제어기 3대·가상 인스턴스 9대, 비실시간 한계, 절감 수치 부재는 검증자 재열람 실패로 리서치 열람 기록 기준이다. PLC·설비 제어 코드의 가상 시운전은 원문 19장 '시설·설비 제어' 연계 대상이다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GitHub 원본(src/simulation.md)에서 traffic_editor 주석(경유점·교통 차선·문·승강기 같은 공유 자원), building_map_generator 의 Gazebo/Ignition 세계·주행 그래프 생성, slotcar·문·승강기·작업셀(TeleportDispenser/Ingestor)·Menge 군중 플러그인, 'Long running simulations can instill confidence…' 문구, 참여 대수·새 플릿 도입 평가, 드물지만 결과가 심각한 경계 사례 검토가 확인된다. 발행일 없음(기준일은 접근일)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-031.txt(VDA 5050 3.0.0) 2장 Scope 가 'Project Coordination and Implementation Procedures'(commissioning workflows, validation and acceptance procedures 포함)와 안전 요구·교통 관리 로직·운영 책임·사이버보안을 범위 밖으로 둔다. 기존 각주 ref-031 을 다시 쓴다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rosbag2 README(raw, rolling 브랜치)에 '/clock is published only while a playback session is active', ~/pause·~/resume·~/seek·~/set_rate·~/play_next 서비스, 기본 저장 형식 mcap·sqlite3 플러그인이 있다. 문서 발행일 없음(기준일은 접근일)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록(2023-10-12)에 Waymo Open Motion Dataset 같은 실제 주행 데이터로 다중 에이전트 시나리오를 'initialize or play back' 하고, 학습·수작성 행동 모델로 상호작용을 지원한다고 나온다. 자율주행 차량은 원문 19장 '업종별 조건'의 연계 대상이며 로봇 현장 사례가 아니다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f6·f7 에서 끌어낸 추정으로 태그가 맞다. 로봇 플릿에서 검증한 자료가 없다는 한계가 브리프에 적혀 있다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 arXiv 초록을 열었다. SRCC_Succ 0.18 → 0.844, LoCoBot PointGoal 주행, 벽을 따라 미끄러지는 충돌 동역학 악용이 초록에 있고, IEEE RA-L 2020, 개정 2020-08-17 이다. 브리프가 이 출처를 fetched: false·source_unopened: true 로 적었으므로 페이지 각주는 원문 미열람 표기를 유지한다(R-1: 검증자는 표시를 올리지 않는다)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록(2025-10-23, Annual Review of Control, Robotics, and Autonomous Systems 2026 게재 예정)에 추상화·근사로 생기는 불일치(현실 격차), 영역 무작위화·현실→시뮬레이션·상태·행동 추상화·공동 학습, 평가 지표, 보행·주행·조작이 나온다. 초록 범위다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록에 'testing and simulation alone are insufficient to ensure the correctness of, or provide sufficient evidence for the certification of, autonomous robotics' 가 있다. 저자들의 견해이므로 [의견]이 맞고, 누구의 의견인지(Luckcuck 외) 본문에 밝혀야 한다. 발행 2019(ACM Computing Surveys 52(5))."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "NASA 표준 페이지(WebFetch)에서 7009B, ACTIVE, 문서일 2024-03-05, M&S 개발·수용·사용의 요구·권고·기준, 개정 B 가 개발·사용 단계의 신뢰도 평가 산출물에 중점을 둔다는 점을 확인했다. 다만 원문은 수용 기준을 '프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자가 승인한다'고 적는다. 권한자가 '정의·승인'한다는 브리프 표현은 부정확하므로 문구를 고친다. '결과를 쓰기 전에'는 페이지에서 확인하지 못했다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 전문(Lee 외, Digital Health, 2026-03-31)에서 고려대학교 구로병원, 2025-06-18~29 배송 122건, 로봇 기록·승강기 텔레메트리, ROC 로 정한 EOR 임계 59.01%, 그 아래 성공률 95.52%, 90% 초과에서 실패 집중, 승강기 출입 차단이 주 실패 기제, 측정한 점유 수로 모수를 정한 몬테카를로 시뮬레이션이 일치한다. 단일 출처."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 저자들이 현장별 구조·통행 구성·승강기 제어 정책을 재현하는 시뮬레이션 기반 디지털 트윈으로 배치 전 검증을 하자고 제안하고, EOR 임계값을 혼잡 모드 배차 규칙으로 쓰자고 한다. 저자 제안이므로 [의견]이 맞다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Rockwell 사례 페이지(2024-08-28)에 Bastian Solutions, 미국 남부 30만 제곱피트 물류센터, 컨베이어·피킹 모듈, Allen-Bradley PLC·I/O 모듈, Emulate3D 에뮬레이션으로 설치 전 문제 해결, 프로젝트 기간 18% 감소, 현장 시운전 약 5주 단축이 있다. 'I/O 매핑'은 페이지에 없고 'I/O 모듈'만 있다. 벤더 주장이며 [추정]·vendor_claim 표시가 맞다. 기준선·측정 방법은 공개되지 않았다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: DBpia 초록에 아주대 연구진, 자동차 차체 생산라인 PLC 코드 검증용 가상 플랜트, 이산 사건 모델로 설비 상태·사건 정의, 실제 PLC 하드웨어와 3D CAD 기반 가상 공정 시뮬레이터의 실시간 연동 시뮬레이션, 라인 안정화까지의 기간·비용 절감 목표가 있다. 학술대회명·803~808쪽·2008-11 은 검증자 조회 요약에 나타나지 않아 브리프 기록 기준이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 현대자동차그룹 콘텐츠(2023-11-21) '가상의 디지털 공간에 세운 쌍둥이 공장'에 '생산을 중단하지 않고도 생산 라인을 검증하고 미래의 운영 결과값을 도출할 수 있는 것이다'와 설비·자동화 로봇 배치를 바꿀 때 가상 시뮬레이션으로 검증한다는 문장이 있다. 정량 수치는 없다. 벤더 주장으로 [추정]이 맞다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Frontiers 전문(2024-08-02)에서 FloorPlan DSL·JSON-LD 조합 모델, 시간·거리 조건으로 움직이는 문 플러그인, 자동 생성 경유점 과제, 수용 기준(위치 추정 오차 0.35 m 등), 실측 점유 격자로 모델링한 대학 건물 1층, 'modelling is time-consuming'(참여자 발언)을 확인했다. 현장 기록 재생은 다루지 않는다. 현장 배치가 아니라 시뮬레이션 시험 사례다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록(2026-08-26)에 ROS 2·Unity 혼합 현실 가상 실험, 실제·가상 로봇, 작업 배정 시연, 가상·실제 센서(LiDAR), ChoiRbot, 공개 예정이 있다. 초록 범위다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f1·f2·f4·f5·f6·f7·f9·f19 를 종합한 추정이며, 근거 finding 들이 모두 살아남았다. 핵심 질문의 답으로 [추정]을 유지한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f9·f12·f18 에서 끌어낸 추정이다. f12 문구를 고친 뒤에도(수용 기준은 프로젝트가 정하고 권한자가 승인) 추정은 성립한다. oq-132 는 해결하지 않은 채 둔다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f1·f2·f12 에서 끌어낸 추정이며, 기존 성숙도 체계를 찾지 못했다는 한계가 적혀 있다. oq-156 은 해결하지 않은 채 둔다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "직접 범위를 인터페이스 가상 대응물·실행 기록·재현 구성·차이 지표 관리로 한정한 추정이다. 원문 19장과 맞는다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'연계 대상:'으로 시작하며 설비 제어 가상 시운전(설비 업체·통합자), 엔진·로봇 제어의 현실 격차(도구·제조사), 차량 기록 시뮬레이션(해당 업계)을 원문 19장 기준으로 나눴다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 영역의 번호·이름이 부록 A 와 일치한다. 18. 실시간 세계 상태·데이터 일관성(원천 기록)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 나눴고, 11. 채팅으로 실제 상황 시뮬레이션 재현(C 주석)과 47. AI·학습·적응과 모델 운영(L 교차 규칙) 연결도 있다."
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
      "f4(Open-RMF 시뮬레이션, ref-406)는 34. 시뮬레이션·예측용 디지털 트윈 페이지의 시뮬레이션 엔진 서술과 겹칠 수 있다. 36. 가상 시운전·실제 상황 재현에서는 '배치 전 시험·규모 평가' 쪽으로만 쓰고 엔진 설명은 34번 연결로 넘긴다",
      "용어집에 승강기 가동률(EOR)이 이미 있으므로 ref-943 이 다른 페이지(22. 설비·건물 시스템 연동, 63. 병원·의료 등)에 이미 인용됐을 수 있다. 같은 URL 이면 퍼블리셔가 기존 id 로 합친다",
      "용어집의 가상 시운전·로그 재생·현실 격차·시뮬레이션 모델 검증·타당성 확인 항목과 뜻이 겹치지 않게, 새 용어 후보는 SiL·HiL·SRCC·NASA 신뢰도 평가 네 개로 한정한다(브리프가 이미 그렇게 했다)"
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
    "f12: 본문 문장을 '수용 기준은 프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자(Technical Authority)가 승인한다'로 고치고, 확인되지 않은 '결과를 쓰기 전에'는 뺀다. f21 과 11절 열린 질문 설명에서 f12 를 인용할 때도 같은 표현을 쓴다 — ref-1177 공식 페이지는 권한자를 승인 주체로만 적는다.",
    "f15: 5절 물류창고 사례 문장에서 'PLC·I/O 매핑·제어 코드'를 'PLC·I/O 모듈과 제어 프로그램'으로 고치고, [추정] 옆에 '벤더 주장'을 병기하며, 18%·5주는 기준선·측정 방법이 공개되지 않았다고 함께 적는다 — ref-1179 는 Rockwell 사례 페이지이며 'I/O 매핑'이라는 말이 없다.",
    "f17: 5절 제조 공장 사례에서 [추정] 옆에 '벤더 주장'을 병기하고 정량 수치가 없음을 밝힌다 — ref-1176 은 현대자동차그룹 자사 콘텐츠다.",
    "f7: 5절 적용 사례에 '실외' 현장 사례로 넣지 않고 site_matrix_updates 에도 넣지 않는다. 6절(운영 기록 기반 재현의 방법 참고)과 7절에서 '연계 대상'으로만 짧게 다룬다 — 자율주행 차량 기록 시뮬레이션은 로봇 현장 사례가 아니고 원문 19장 업종별 조건의 연계 대상이다.",
    "f3·f15·f16: 5절에서 이 세 사례를 적을 때 설비 제어 코드(PLC·컨베이어)의 가상 시운전이 원문 19장 '시설·설비 제어' 연계 대상이며, ROP에는 방법 근거로만 쓴다는 한 문장을 둔다(f24 인용) — ROP 직접 범위처럼 읽히지 않게 하려는 것이다.",
    "f18: 5절 기타 현장 사례에서 이것이 실측 지도로 만든 대학 건물의 시뮬레이션 시험 사례이며 현장 배치나 현장 기록 재생이 아님을 밝힌다 — 논문은 로그 재생을 다루지 않는다.",
    "f11·f14: [의견] 문장에 의견의 주체(f11은 Luckcuck 외, f14는 Lee 외 저자들)를 문장 안에 밝힌다 — 공통 규칙 5.3.",
    "ref-1167: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1167 항목에 source_unopened: true 를 넣는다. f9 에 기댄 문장(4·6·8절, f21)의 신뢰도를 medium 보다 높이지 않는다 — 브리프가 이 출처를 미열람으로 기록했다.",
    "glossary_candidates '모델·시뮬레이션 신뢰도 평가': 정의에서 확인되지 않은 '검증·타당성 확인 등 신뢰도 요소를 평가'를 빼고 'NASA-STD-7009B 가 모델·시뮬레이션의 개발·사용 단계에서 요구하는 신뢰도 평가로, 결과를 쓰기 위한 수용 기준을 프로젝트가 정하고 위임된 기술 권한자가 승인한다' 수준으로 줄인다. 기존 용어집 항목 '시뮬레이션 모델 검증·타당성 확인'과 연결한다 — 신뢰도 요소 8개·점수 척도는 검색 요약에만 있다.",
    "5절: 상업 시설·가정 현장 사례는 찾지 못했고, 실외는 자율주행 방법 참고(f7)만 있다는 점을 적는다. site_matrix_updates 는 물류창고(f15)·제조 공장(f3·f16·f17)·병원(f13·f14)·기타(f18) 칸만 낸다 — 브리프 self_check 와 맞춘다.",
    "3절·9절: 핵심 질문의 답(f20)과 직접 범위·연계 대상(f23·f24)은 [추정] 태그를 유지해 서술하고 단정 표현을 쓰지 않는다. oq-132·oq-156 은 해결로 바꾸지 않고 11절에 부분 근거(f21·f22)와 함께 '열림'으로 둔다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 25건, 미확인 0건, 교차 확인 0건. 강등: 없음. 대신 f12 문구를 고친다(수용 기준은 프로젝트가 정하고 위임된 NASA 기술 권한자가 승인한다). 원문 미열람 출처: ref-1167. 이 출처는 브리프가 미열람으로 기록했지만, 검증자가 arXiv 초록을 열어 f9 수치를 확인했다. ref-1172(Rosenberger 외)는 검증자가 PMC·MDPI 재열람에 실패해 검색 결과로 서지만 확인했으므로 f2·f3 세부는 리서치의 원문 열람 기록에 의존한다. 주의: 모든 주장이 단일 출처이고, 핵심 질문 답(f20)과 책임 경계(f23·f24)는 추정이다. 물류창고(f15)·현대자동차그룹(f17) 사례는 벤더 주장이며, 18%·5주 수치는 기준선이 공개되지 않았다. 여러 제조사 로봇 플릿을 대상으로 한 가상 시운전 절차 표준과 재현 결과의 현실 일치 판정 기준은 확인하지 못했다(oq-132·oq-156 미해결). 상업 시설·가정·실외 로봇 현장 사례는 없다. 정정 요청 없음. 검증 검색 1회를 써서 실행 누계는 20회/30회다.",
  "retry_reason": null
}
```

### runs/2026-09-30-17/pages.json

```json
{
  "run_id": "2026-09-30-17",
  "outline": [
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "설치 전 가상 시운전은 설비 제어 분야에서 정립되어 있으나 여러 제조사 로봇 플릿 전체의 가상 시운전 절차 표준과 재현 결과의 현실 일치 판정 기준은 확인되지 않았다. [추정][^ref-1165]",
      "planned_findings": [
        "f20",
        "f5",
        "f11",
        "f9"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1400,
      "summary": "가상 시운전(VDI/VDE 3693), MiL·SiL·HiL, 로그 재생, 비반응 재생의 한계, 현실 격차, SRCC, NASA-STD-7009B 신뢰도 평가를 정리한다. [사실][^ref-1165]",
      "planned_findings": [
        "f1",
        "f2",
        "f6",
        "f8",
        "f9",
        "f10",
        "f12"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2700,
      "summary": "병원(실제 기록 기반 승강기 탑승 실패 재현), 제조 공장(분산 제어 가상 시운전), 물류창고(벤더 주장 에뮬레이션), 기타(대학 건물 시뮬레이션 시험) 사례를 여섯 항목으로 정리한다. [사실][^ref-943]",
      "planned_findings": [
        "f13",
        "f14",
        "f3",
        "f16",
        "f17",
        "f15",
        "f18",
        "f24"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1900,
      "summary": "가상 시운전은 MiL·SiL·HiL 과 Open-RMF 시뮬레이션·혼합 현실 도구로, 기록 재현은 rosbag2 재생과 기록 기반 초기화로, 차이 관리는 SRCC·현실 격차 기법·수용 기준으로 접근한다. [사실][^ref-1172]",
      "planned_findings": [
        "f2",
        "f3",
        "f4",
        "f19",
        "f6",
        "f7",
        "f8",
        "f13",
        "f9",
        "f10",
        "f21",
        "f11"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "VDI/VDE 3693 Blatt 1, NASA-STD-7009B, Open-RMF 시뮬레이션, rosbag2, VDA 5050 3.0.0(시운전 절차는 범위 밖), Waymax(연계 대상), VirTooS 를 표로 정리한다. [사실][^ref-1165]",
      "planned_findings": [
        "f1",
        "f12",
        "f4",
        "f6",
        "f5",
        "f7",
        "f19"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1100,
      "summary": "분산 가상 시운전, SRCC, 현실 격차 조사, 형식 검증 조사, 병원 기록 기반 재현, 국내 가상 플랜트, 조합형 시나리오 연구를 소개한다. [사실][^ref-1172]",
      "planned_findings": [
        "f3",
        "f9",
        "f10",
        "f11",
        "f13",
        "f16",
        "f18"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1100,
      "summary": "ROP는 인터페이스 가상 대응물을 붙인 SiL 시험 환경·재생 가능한 실행 기록·재현 구성·차이 지표와 수용 승인 기록을 맡고, 엔진·로봇 제어·설비 제어 코드·차량 기록 시뮬레이션은 연계 대상으로 보인다. [추정][^ref-406]",
      "planned_findings": [
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1500,
      "summary": "33·34번(시나리오·엔진), 18·37번(재현 원천 기록), 11번(대화형 재현), 14·15·20·22·25·38·47·54·55번과 현장 영역 61·62·63·67번에 연결한다. [추정][^ref-406]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "oq-132·oq-156 은 부분 근거만 있어 열림으로 두고, 플릿 수준 가상 시운전 사례·비반응 재생·독립 효과 측정·병원 임계값 일반화의 새 질문 4건을 올린다. [추정][^ref-1177]",
      "planned_findings": [
        "f21",
        "f22",
        "f1",
        "f8",
        "f15",
        "f14"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(현장 유형 사례 4건: 병원·제조 공장·물류창고·기타), 13절 각주 16건, 1차 조건부 승인 수정 11건 반영"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"6. 대표 접근법과 기술\" 절(1,605자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"4. 핵심 개념과 용어\" 절(1,262자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"8. 대표 연구와 자료\" 절(1,238자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"11. 열린 질문\" 절(1,205자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,078자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(836자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area36-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 36. 가상 시운전·실제 상황 재현 의 \"3. 왜 중요한가\" 절(661자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 36. 가상 시운전·실제 상황 재현 | 영역 심화: 3~11절 신규 작성(현장 유형 사례 4건: 병원·제조 공장·물류창고·기타), 각주 16건, 1차 조건부 승인 수정 11건 반영 | run 2026-09-30-17",
  "index_updates": {
    "home_recent": "2026-09-30 — 36. 가상 시운전·실제 상황 재현: 영역 심화 초안(VDI/VDE 3693·MiL·SiL·HiL, rosbag2 기록 재생, 현실 일치 판정 후보, 병원·제조 공장·물류창고·기타 사례)",
    "category_recent": "2026-09-30 — 36. 가상 시운전·실제 상황 재현: 3~11절 신규 작성, 현장 유형 사례 4건(병원 실제 기록 기반 승강기 실패 재현 포함), oq-132·oq-156 부분 근거 추가",
    "area_recent": "2026-09-30 — 36. 가상 시운전·실제 상황 재현: 영역 심화로 3~11절을 처음 작성했다(신뢰도 medium, 벤더 주장 2건 표시)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "software-in-the-loop",
      "term_ko": "소프트웨어 인 더 루프",
      "term_en": "Software-in-the-Loop (SiL)",
      "definition": "실제 제어 언어로 작성한 제어 코드를 대상 하드웨어와 분리해 돌리며 설비 시뮬레이션과 연결해 시험하는 가상 시운전 구성이다.",
      "description": "Rosenberger 외(2023)가 VDI 3693 에 따라 MiL·SiL·HiL 로 나눈 시험 구성 가운데 하나다. 관련 용어: 가상 시운전.",
      "related_areas": [
        36,
        55
      ],
      "sources": [
        "ref-1172"
      ]
    },
    {
      "action": "new",
      "slug": "hardware-in-the-loop",
      "term_ko": "하드웨어 인 더 루프",
      "term_en": "Hardware-in-the-Loop (HiL)",
      "definition": "실제 대상 하드웨어(가상 머신·컨테이너로 가상화한 하드웨어 포함)를 설비 시뮬레이션과 연결해 제어 프로그램과 하드웨어를 함께 시험하는 가상 시운전 구성이다.",
      "description": "Rosenberger 외(2023)가 VDI 3693 에 따라 구분한 시험 구성 가운데 실제 하드웨어에 가장 가까운 구성이다.",
      "related_areas": [
        36,
        55
      ],
      "sources": [
        "ref-1172"
      ]
    },
    {
      "action": "new",
      "slug": "sim-vs-real-correlation-coefficient",
      "term_ko": "시뮬레이션–현실 상관 계수",
      "term_en": "Sim-vs-Real Correlation Coefficient (SRCC)",
      "definition": "여러 방법·설정을 비교할 때 시뮬레이션에서의 성능 차이가 실제 로봇에서의 성능 차이와 얼마나 같은 방향으로 나타나는지를 상관계수로 재는 시뮬레이션 예측력 지표다.",
      "description": "Kadian 외(2020)가 제안했다. LoCoBot PointGoal 주행에서 성공률 기준 0.18 이던 값을 시뮬레이터 조정으로 0.844 로 높였다(원문 미열람, 초록 기준). 관련 용어: 현실 격차.",
      "related_areas": [
        36,
        34,
        54
      ],
      "sources": [
        "ref-1167"
      ]
    },
    {
      "action": "new",
      "slug": "models-and-simulations-credibility-assessment",
      "term_ko": "모델·시뮬레이션 신뢰도 평가",
      "term_en": "Models and Simulations Credibility Assessment (NASA-STD-7009)",
      "definition": "NASA-STD-7009B 가 모델·시뮬레이션의 개발·사용 단계에서 요구하는 신뢰도 평가로, 결과를 쓰기 위한 수용 기준을 프로젝트가 정하고 위임된 기술 권한자가 승인한다.",
      "description": "기존 용어 '시뮬레이션 모델 검증·타당성 확인'(verification-and-validation-of-simulation-models)과 연결해 본다. 신뢰도 요소와 점수 척도는 원문에서 확인하지 못했다.",
      "related_areas": [
        36,
        54
      ],
      "sources": [
        "ref-1177"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "관제와 AGV·AMR 사이 통신 인터페이스를 정한 VDA 5050 공식 명세(현재 main 은 3.0.0). 시운전·검증·인수 절차는 범위 밖에 둔다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1165",
      "org": "VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik)",
      "title": "VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions",
      "published": "2025-05",
      "url": "https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "가상 시운전의 정의와 수명주기 내 위치, 시험 구성·시험 방법·모델 유형·시뮬레이션 구성을 다루는 VDI/VDE 지침 2025-05 개정판의 공식 소개 페이지. 표준 본문은 유료로 열람하지 않았다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (Open Robotics 외, ros2/rosbag2 저장소)",
      "title": "rosbag2 README",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 토픽 기록·재생 도구 rosbag2 의 공식 README. /clock 발행, 재생 제어 서비스, MCAP·SQLite3 저장 형식을 설명한다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1167",
      "org": "Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L)",
      "title": "Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?",
      "published": "2020-08",
      "url": "https://arxiv.org/abs/1912.06321",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 시뮬레이션 평가가 실제 성능을 예측하는 정도를 재는 SRCC 지표를 제안하고 LoCoBot PointGoal 주행에서 시뮬레이터 조정으로 SRCC 를 0.18 에서 0.844 로 높였다. arXiv 초록 기준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1168",
      "org": "Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv)",
      "title": "Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research",
      "published": "2023-10-12",
      "url": "https://arxiv.org/abs/2310.08710",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실제 주행 기록으로 다중 에이전트 시나리오를 초기화·재생하고 행동 모델로 상호작용을 넣는 가속 자율주행 시뮬레이터. arXiv 초록만 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 배치를 Gazebo·Ignition 으로 시뮬레이션하는 방법(도면 기반 세계 생성, 로봇·문·승강기·작업셀·군중 플러그인)과 배치 전 시험의 목적을 설명하는 장.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-943",
      "org": "Lee 외 (Digital Health, SAGE)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고려대학교 구로병원의 실제 약품 배송 로봇 기록 122건과 승강기 데이터로 승강기 가동률 임계값을 찾고 몬테카를로 시뮬레이션으로 탑승 실패 기제를 재현한 연구. 전문을 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1171",
      "org": "Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv)",
      "title": "VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots",
      "published": "2026-08-26",
      "url": "https://arxiv.org/abs/2608.26066",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "실제·가상 로봇이 함께 움직이는 혼합 현실 환경에서 AMR 플릿 관리(작업 배정) 실험을 하는 ROS 2–Unity 도구. arXiv 초록만 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1172",
      "org": "Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545)",
      "title": "Virtual Commissioning of Distributed Systems in the Industrial Internet of Things",
      "published": "2023-03-28",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "VDI 3693 의 MiL·SiL·HiL 구분을 바탕으로 가상 시운전을 분산 에지 시스템으로 넓히는 구조 3가지를 제안하고 팔레타이징 설비 시뮬레이션으로 시험했다. 전문을 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-599",
      "org": "Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5))",
      "title": "Formal Specification and Verification of Autonomous Robotic Systems: A Survey",
      "published": "2019",
      "url": "https://arxiv.org/abs/1807.00048",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자율 로봇 시스템의 형식 명세·검증 기법과 과제를 정리한 조사 논문. 시험·시뮬레이션만으로는 인증 증거가 부족하다고 본다. arXiv 초록만 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-741",
      "org": "Aljalbout, E., Xing, J., Romero, A. 외 (arXiv)",
      "title": "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices",
      "published": "2025-10-23",
      "url": "https://arxiv.org/abs/2510.20808",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "로봇 공학의 현실 격차 원인과 대응 기법(영역 무작위화, 현실→시뮬레이션, 추상화, 공동 학습), 평가 지표를 정리한 조사 논문. arXiv 초록만 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1175",
      "org": "최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회)",
      "title": "자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스",
      "published": "2008-11",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자동차 차체 생산라인의 PLC 코드를 실제 PLC 와 가상 공정 시뮬레이터의 연동으로 검증하는 가상 플랜트 구축 절차를 제안한 국내 학술대회 논문. DBpia 초록만 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1176",
      "org": "현대자동차그룹",
      "title": "가상의 디지털 공간에 세운 쌍둥이 공장",
      "published": "2023-11-21",
      "url": "https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "현대자동차그룹이 HMGICS 디지털 트윈 가상 공장으로 설비·로봇 배치 변경을 가상에서 먼저 검증한다고 소개하는 회사 콘텐츠. 정량 수치는 없다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1177",
      "org": "NASA",
      "title": "NASA-STD-7009B Standard for Models and Simulations",
      "published": "2024-03-05",
      "url": "https://standards.nasa.gov/standard/NASA/NASA-STD-7009",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "모델·시뮬레이션의 개발·수용·사용 요구와 신뢰도 평가를 정한 NASA 표준의 공식 페이지(개정 B, 현행). 수용 기준은 프로그램·프로젝트가 정하고 위임된 기술 권한자가 승인한다. 표준 본문 PDF 는 열지 않았다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1178",
      "org": "Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI)",
      "title": "Composable and executable scenarios for simulation-based testing of mobile robots",
      "published": "2024-08-02",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "도면 DSL·초기 자세·동적 객체·과제·수용 기준을 조합해 이동로봇 시뮬레이션 시험 시나리오를 만드는 방법을 제안하고 대학 건물에서 평가했다. 전문을 읽었다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    },
    {
      "id": "ref-1179",
      "org": "Rockwell Automation",
      "title": "Emulation Technology Speeds Up Warehouse Automation",
      "published": "2024-08-28",
      "url": "https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "Bastian Solutions 가 물류센터 구축에서 컨베이어·피킹 모듈·PLC·I/O 모듈과 제어 프로그램을 에뮬레이션으로 설치 전 검증했다는 벤더 사례. 성과 수치(18%·5주)는 벤더 주장이며 기준선은 공개되지 않았다.",
      "cited_by": [
        "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가?",
      "areas": [
        36,
        20,
        55
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가?",
      "areas": [
        36,
        19,
        33
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가?",
      "areas": [
        36,
        3
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가?",
      "areas": [
        36,
        63,
        22
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "기타",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "기타",
      "item": "완료·인계",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#5-적용-사례-현장-유형-명시",
      "title": "36. 가상 시운전·실제 상황 재현"
    }
  ],
  "standards_updates": [
    {
      "name": "VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판)",
      "kind": "표준",
      "org": "VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik)",
      "url": "https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions",
      "related_areas": [
        36,
        55
      ],
      "summary": "가상 시운전을 체계적으로 정의하고 자동화 설비·기계의 수명주기 안에 위치시키며, 기본 시험 구성·시험 방법·모델 유형·시뮬레이션 구성을 다루는 지침이다. 본문은 유료이며 공식 소개 페이지 기준으로 확인했다.",
      "ref_id": "ref-1165"
    },
    {
      "name": "NASA-STD-7009B Standard for Models and Simulations",
      "kind": "표준",
      "org": "NASA",
      "url": "https://standards.nasa.gov/standard/NASA/NASA-STD-7009",
      "related_areas": [
        36,
        54
      ],
      "summary": "모델·시뮬레이션의 개발·수용·사용 요구·권고·기준과 신뢰도 평가를 정한 현행 표준(문서일 2024-03-05)이다. 수용 기준은 프로그램·프로젝트가 정하고 위임된 기술 권한자가 승인한다.",
      "ref_id": "ref-1177"
    }
  ],
  "additional_research_requests": [
    "6절 '실행 전 계획 검증': 계획을 실행하지 않고 정적으로 검사하는 도구(VAL 등)의 검증 항목을 원문에서 확인한 근거가 없어 전용 서술을 넣지 못했다. 도구 문서·논문 원문 확인이 필요하다.",
    "4·6절: NASA-STD-7009B 의 신뢰도 요소·점수 척도는 검색 요약에만 있어 넣지 못했다. 표준 본문 PDF 열람으로 확인이 필요하다.",
    "5절: 상업 시설·가정·실외 로봇 현장의 가상 시운전·실제 상황 재현 사례를 찾지 못했다. 이 현장 유형의 사례 조사가 필요하다.",
    "5·6절: 여러 제조사 로봇 플릿을 대상으로 한 가상 시운전 공개 사례(Kulkarni 창고 로봇 가상 시운전, Siemens·Wipro 사례)와 Striffler·Voigt(2023) 리뷰는 신규 출처 상한·접근 실패로 넣지 못했다. 다음 실행에서 확인이 필요하다.",
    "3·4·6절: 이번 페이지의 모든 주장이 단일 출처이므로 핵심 주장(가상 시운전 정의·MiL·SiL·HiL 구분, SRCC 수치)의 교차 확인 출처가 필요하다.",
    "7절: 국내 가상 시운전 표준(KS)이나 공공 지침이 있는지 확인이 필요하다."
  ],
  "fixes_applied": [
    "f12 문구 수정 — 4절 용어 목록, 6절 차이 관리, 7절 표, 11절 oq-132 설명에서 '수용 기준은 프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자(Technical Authority)가 승인한다'로 쓰고 '결과를 쓰기 전에'를 뺐다.",
    "f15 — 5절 물류창고 사례 작업 대상을 'PLC·I/O 모듈과 제어 프로그램'으로 쓰고, 모든 칸과 서술에 '[추정] 벤더 주장'을 병기했으며, 18%·5주 수치에 기준선·측정 방법 미공개를 함께 적었다.",
    "f17 — 5절 제조 공장 서술의 현대자동차그룹 문장에 '[추정] 벤더 주장'을 병기하고 정량 수치를 밝히지 않았음을 적었다.",
    "f7 — 5절에 실외 사례로 넣지 않고 site_matrix_updates 에서도 뺐으며, 6절 운영 기록 기반 재현과 7절 표에서 '연계 대상'으로만 짧게 다뤘다.",
    "f3·f15·f16 — 5절 첫 단락에 설비 제어 코드(PLC·컨베이어) 가상 시운전이 분류 원문 19장 '시설·설비 제어' 연계 대상이며 ROP 에는 방법 근거로만 쓴다는 문장을 [추정] 태그와 각주로 두었다(f24).",
    "f18 — 5절 기타 사례 서술에 실측 지도로 만든 대학 건물의 시뮬레이션 시험 사례이며 현장 배치나 현장 기록 재생이 아님을 밝혔다.",
    "f11·f14 — [의견] 문장마다 주체를 문장 안에 밝혔다(3·6·8절 'Luckcuck 외', 5절 병원 사례 'Lee 외 저자들').",
    "ref-1167 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1167 에 source_unopened: true 를 넣었으며, 페이지 신뢰도는 medium 을 넘지 않는다.",
    "용어집 '모델·시뮬레이션 신뢰도 평가' — 정의를 'NASA-STD-7009B 가 개발·사용 단계에서 요구하는 신뢰도 평가, 수용 기준은 프로젝트가 정하고 위임된 기술 권한자가 승인' 수준으로 줄이고 설명에 기존 용어 '시뮬레이션 모델 검증·타당성 확인'과의 연결을 적었다(4절 본문에도 링크).",
    "5절 — 상업 시설·가정 사례를 찾지 못했고 실외는 자율주행 방법 참고(f7)뿐이라는 문장을 절 끝에 두었고, site_matrix_updates 는 물류창고·제조 공장·병원·기타 칸만 냈다.",
    "3절·9절 — 핵심 질문의 답(f20)과 직접 범위·연계 대상(f23·f24)을 [추정] 태그와 '~로 보인다' 표현으로 서술했고, 11절에서 oq-132·oq-156 을 부분 근거(f21·f22)와 함께 '열림'으로 두었다(open_question_updates 에 해결 처리 없음).",
    "분량 초과 자동 분리: 36. 가상 시운전·실제 상황 재현 본문 11,353자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,449자"
  ]
}
```

### runs/2026-09-30-17/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area36-s6.md (1,605자)
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area36-s4.md (1,262자)
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area36-s8.md (1,238자)
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area36-s11.md (1,205자)
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area36-s10.md (1,078자)
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area36-s7.md (836자)
    - docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area36-s3.md (661자)
```

### runs/2026-09-30-17/pages/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현"
type: area
category: "I. 설계·시뮬레이션"
area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [가상 시운전, SiL·HiL, 로그 재생, 현실 격차, 시뮬레이션 신뢰도 평가]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-1165, ref-831, ref-1167, ref-1168, ref-406, ref-943, ref-1171, ref-1172, ref-599, ref-741, ref-1175, ref-1176, ref-1177, ref-1178, ref-1179]
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
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

설치 전 가상 시운전은 제조·물류 설비 제어 분야에서 VDI/VDE 3693 과 MiL·SiL·HiL 시험 구성으로 정립되어 있고 여러 로봇 쪽에도 Open-RMF 시뮬레이션과 혼합 현실 도구가 있지만, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차 표준은 이번 조사에서 확인하지 못했다. [추정][^ref-1165][^ref-1172][^ref-406][^ref-1171]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 왜 중요한가](../../topics/2026/2026-09-30-area36-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 설치 전 시험, 기록 재생, 시뮬레이션 결과의 신뢰 판단 세 갈래로 묶인다.

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area36-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 사례는 실제 기록으로 문제를 재현한 병원 연구, 설치 전에 제어를 시험한 제조 공장·물류창고 사례, 시뮬레이션 시험 시나리오를 만든 대학 건물 사례다. 제조 공장·물류창고 사례의 PLC·컨베이어 같은 설비 제어 코드 가상 시운전은 분류 원문 19장의 '시설·설비 제어' 경계에서 설비 업체·통합자가 맡는 연계 대상으로 보이며, 여기서는 ROP 가상 시운전의 방법 근거로만 쓴다. [추정][^ref-1172][^ref-1175][^ref-1179]

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
| 시작 조건 | 가상 시운전을 제어 루프에서 분산 에지 컴퓨팅 시스템 전체로 넓혀 여러 장치를 함께 시험하려는 연구 목적. [사실][^ref-1172] |
| 작업 대상 | 끝단 팔레타이징 포장 설비 시뮬레이션과, 이와 직접 피드백 루프로 연결된 응용. [사실][^ref-1172] |
| 수행 자원 | 실제 제어기 3대와 가상화 인스턴스 9대. [사실][^ref-1172] |
| 제약 | 비실시간 시뮬레이션이라는 한계. [사실][^ref-1172] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 시운전 기간·비용 절감 수치는 제시하지 않았다. [사실][^ref-1172] |

국내에서는 최성욱·박상철·왕지남(2008)이 자동차 차체 생산라인의 PLC 코드를 검증하려고 설비 상태·사건을 이산 사건 모델로 정의하고, 실제 PLC 하드웨어와 3D CAD·디지털 목업 기반 가상 공정 시뮬레이터를 양방향 통신으로 연동하는 가상 플랜트 구축 절차를 제안해 라인 안정화 기간과 비용을 줄이려 했다. [사실][^ref-1175] 현대자동차그룹은 싱가포르 혁신센터(HMGICS)에서 디지털 트윈 가상 공장으로 설비·로봇 배치 변경을 실제 생산을 멈추지 않고 가상에서 먼저 검증한다고 소개하지만, 시운전 기간 단축 같은 정량 수치는 밝히지 않았다. [추정] 벤더 주장[^ref-1176]

**현장 유형:** 물류창고

**사례:** 물류센터 구축에서 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미국 남부의 약 30만 제곱피트 규모 물류센터 구축(설치 전). [추정] 벤더 주장[^ref-1179] |
| 작업 대상 | 컨베이어·피킹 모듈, PLC·I/O 모듈과 제어 프로그램. [추정] 벤더 주장[^ref-1179] |
| 수행 자원 | 통합자 Bastian Solutions 가 에뮬레이션으로 설치 전에 검증. [추정] 벤더 주장[^ref-1179] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 전체 프로젝트 기간 18% 감소, 현장 시운전 5주 단축(기준선·측정 방법은 공개되지 않음). [추정] 벤더 주장[^ref-1179] |

Rockwell Automation 사례 소개(2024-08-28)에 실린 내용이며, 흐름 단계로는 피킹 모듈과 이를 잇는 컨베이어가 대상이다. 18%·5주 수치는 기준선과 측정 방법이 공개되지 않아 독립적으로 확인할 수 없다. [추정] 벤더 주장[^ref-1179]

**현장 유형:** 기타

**사례:** 대학 건물 1층을 실측 지도로 모델링해 이동로봇 시뮬레이션 시험 시나리오를 구성

| 항목 | 내용 |
|---|---|
| 시작 조건 | 이동로봇을 시뮬레이션으로 시험할 실행 가능한 시나리오가 필요함. [사실][^ref-1178] |
| 작업 대상 | 도면 DSL 로 만든 실내 환경(실측 점유 격자로 모델링한 대학 건물 1층), 동적 객체의 초기 자세, 시간·거리 조건으로 움직이는 문 같은 동적 요소. [사실][^ref-1178] |
| 수행 자원 | 시뮬레이션 안의 이동로봇이 주행 과제를 수행. [사실][^ref-1178] |
| 제약 | 해당 없음 |
| 완료·인계 | 위치 추정 오차·충돌 회피 같은 수용 기준을 시나리오에 명시해 판정. [사실][^ref-1178] |
| 예외·성과 | 현장 기록의 재생은 다루지 않았다. [사실][^ref-1178] |

이 사례는 현장 배치나 현장 기록 재생이 아니라, 실측 지도로 만든 대학 건물을 대상으로 한 시뮬레이션 시험 사례다. [사실][^ref-1178] 시나리오마다 수용 기준을 두는 방식은 재현 결과의 판정 기준을 정할 때 조합할 수 있는 요소로 보인다(11절 oq-132). [추정][^ref-1178]

이번 조사에서 상업 시설·가정 현장의 가상 시운전·재현 사례는 찾지 못했다. 실외는 자율주행 차량의 기록 기반 시뮬레이션(6절)이 재현 방법의 참고로 있을 뿐 로봇 현장 사례가 아니어서 싣지 않았다.

## 6. 대표 접근법과 기술

이 영역의 접근법은 1절의 네 가지 일에 따라 나뉘며, 이번 조사에서 근거가 가장 많은 것은 가상 시운전과 기록 재생이다.

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area36-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

가상 시운전의 정의와 시험 구성은 VDI/VDE 3693 이, 모델·시뮬레이션 결과의 수용은 NASA-STD-7009B 가 다루며, 여러 로봇 시뮬레이션과 기록 재생에는 Open-RMF 와 rosbag2 가 쓰인다. [사실][^ref-1165][^ref-1177][^ref-406][^ref-831]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area36-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 연구는 분산 가상 시운전, 시뮬레이션 예측력, 현실 격차, 형식 검증, 실제 기록 기반 재현, 시험 시나리오 구성을 다룬다.

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료](../../topics/2026/2026-09-30-area36-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 플릿 인터페이스의 가상 대응물을 붙여 오케스트레이션 논리와 운영 정책을 SiL 방식으로 시험하고, 재현 결과와 실제의 차이 지표를 관리하는 것으로 보인다. [추정][^ref-406][^ref-1172][^ref-1167] | 연계 대상: 물리·센서 시뮬레이션 엔진과 시뮬레이션 자산, 로봇 내부 주행·인식 제어의 현실 격차 보정(시뮬레이션 도구·로봇 제조사). [추정][^ref-741] |
| 시설·설비 제어 | 문·승강기 인터페이스의 가상 대응물 연결, 설비 에뮬레이터와 이어지는 인터페이스와 그 시험 결과 수용으로 보인다. [추정][^ref-406] | 연계 대상: 컨베이어·PLC·승강기 제어 코드의 에뮬레이션과 가상 시운전(설비 업체·통합자). [추정][^ref-1172][^ref-1175][^ref-1179] |
| 업종별 조건 | 재현 방법의 참고로만 가져오는 것으로 보인다. [추정][^ref-1168] | 연계 대상: 자율주행 차량의 기록 기반 시뮬레이션(해당 업계). [추정][^ref-1168] |

확인한 자료를 종합하면 ROP가 직접 맡을 범위는 제조사 플릿·문·승강기 인터페이스의 가상 대응물을 붙여 오케스트레이션 논리와 운영 정책을 설치 전에 SiL 방식으로 시험하는 환경, 재생 가능한 형태로 시각이 맞춰진 오케스트레이션 수준 실행 기록, 기록에서 시뮬레이션 초기 상태와 사건을 구성하는 기능, 재현 결과와 실제의 차이 지표와 수용 승인 기록의 관리로 보인다. [추정][^ref-406][^ref-831][^ref-1172][^ref-1167][^ref-1177][^ref-031] 이종 제조사를 잇는 ROP는 엔진·로봇 제어·설비 제어 코드를 직접 만들기보다 이들의 가상 모델·에뮬레이터와 연결되는 인터페이스와 시험 결과를 받아들이는 쪽을 맡는 것으로 보인다. [추정][^ref-1172][^ref-1175][^ref-1179][^ref-741][^ref-1168][^ref-406] 분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적으며, 기준은 [ROP 범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오 형식과 시뮬레이션 엔진, 재현의 원천 기록, 연동 대상 인터페이스, 적용 현장과 이어진다. [추정][^ref-406][^ref-831]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area36-s10.md)에 있다.

## 11. 열린 질문

재현 결과의 현실 일치 판정 기준과 단계별 검증 수준은 부분 근거만 있어 열린 질문으로 남는다. [추정][^ref-1167][^ref-1177]

자세한 내용은 주제 페이지 [36. 가상 시운전·실제 상황 재현 — 열린 질문](../../topics/2026/2026-09-30-area36-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1165]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-1167]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-1168]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-406]: Open Robotics, Simulation — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-943]: Lee 외 (Digital Health, SAGE), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1171]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-09-30
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-741]: Aljalbout, E., Xing, J., Romero, A. 외 (arXiv), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10-23, https://arxiv.org/abs/2510.20808, 접근일 2026-09-30
[^ref-1175]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-09-30
[^ref-1176]: 현대자동차그룹, 가상의 디지털 공간에 세운 쌍둥이 공장, 2023-11-21, https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330, 접근일 2026-09-30
[^ref-1177]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30
[^ref-1178]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-09-30
[^ref-1179]: Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation, 2024-08-28, https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html, 접근일 2026-09-30
```

### docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현"
type: area
category: "I. 설계·시뮬레이션"
area_no: 36
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 36. 가상 시운전·실제 상황 재현

# 36. 가상 시운전·실제 상황 재현

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s6.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-831, ref-1167, ref-1168, ref-406, ref-943, ref-1171, ref-1172, ref-599, ref-741, ref-1177, ref-1178]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#6
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술

# 36. 가상 시운전·실제 상황 재현 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 접근법은 1절의 네 가지 일에 따라 나뉘며, 이번 조사에서 근거가 가장 많은 것은 가상 시운전과 기록 재생이다.
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 접근법은 1절의 네 가지 일에 따라 나뉘며, 이번 조사에서 근거가 가장 많은 것은 가상 시운전과 기록 재생이다.

### 가상 시운전: 설치 전에 연동과 정책을 시험한다

설비 제어 분야는 가장 추상적인 MiL 에서 실제 대상 하드웨어를 쓰는 HiL 까지의 시험 구성을 쓴다(4절). [사실][^ref-1172] Rosenberger 외는 이를 분산 에지 시스템으로 넓혀 단일 장치+네트워크, 다수 장치+단일 시뮬레이션, 다수 분산 시뮬레이션의 세 구조를 제안했으나 비실시간 시뮬레이션이라는 한계를 밝혔다. [사실][^ref-1172]

여러 로봇 쪽에서는 Open-RMF 시뮬레이션 문서가 traffic_editor 로 도면에 교통 정보·경유점·공유 자원을 주석한 뒤 building_map_generator 가 Gazebo·Ignition 세계와 플릿 어댑터용 주행 그래프를 자동 생성하고, 로봇(slotcar)·문·승강기·작업셀(디스펜서·인제스터)·군중(Menge) 플러그인으로 배치 전 시험, 로봇 추가 시 규모 평가, 드문 실패 상황 검토를 할 수 있다고 설명한다. [사실][^ref-406] 시뮬레이션 엔진 자체는 [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md)에서 다룬다. VirTooS(2026-08)는 ROS 2 와 Unity 를 결합해 실제 로봇과 가상 로봇이 같은 환경에서 상호작용하는 혼합 현실 실험으로 자율이동로봇(AMR) 플릿의 작업 배정 전략을 시험하는 도구이며, 초록에는 정량 결과가 없다. [사실][^ref-1171]

### 운영 기록 기반 재현

rosbag2 는 재생 중 일시정지·재개·탐색·속도 조정·한 메시지씩 진행 같은 재생 제어 서비스를 제공한다. [사실][^ref-831] 연계 대상: 자율주행 분야의 Waymax(Gulino 외, 2023)는 Waymo Open Motion Dataset 같은 실제 주행 기록으로 다중 에이전트 시나리오를 초기화하거나 재생하고, 학습된 행동 모델과 규칙 기반 행동 모델을 넣어 단순 재생을 넘는 상호작용을 지원한다. [사실][^ref-1168] 이는 로봇 현장 사례가 아니라 재현 방법의 참고다. 로봇 플릿 재현에서도 조건을 바꿔 비교하려면 반응형 행동 모델로 바꾸는 단계가 필요할 것으로 보이나, 로봇 플릿에서 이를 검증한 자료는 찾지 못했다. [추정][^ref-1168][^ref-831] 5절 병원 사례는 실제 로봇·승강기 기록으로 모수를 정한 시뮬레이션으로 실패 기제를 재현했다. [사실][^ref-943]

### 시뮬레이션–현실 차이 관리

Kadian 외는 LoCoBot 의 PointGoal 주행에서 성공률 기준 SRCC 가 0.18 로 낮았던 원인이 에이전트가 충돌 동역학을 악용해 벽을 따라 미끄러지는 것임을 찾아, 시뮬레이터 설정을 조정해 0.844 로 높였다. [사실][^ref-1167] Aljalbout 외는 영역 무작위화, 현실→시뮬레이션 전이, 상태·행동 추상화, 시뮬레이션–현실 공동 학습 같은 대응 기법과 현실 격차 평가 지표를 정리했다. [사실][^ref-741] 재현 결과의 현실 일치 판정에는 SRCC 같은 예측력 지표, 수용 기준을 프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자가 승인하는 NASA-STD-7009B 방식, 시나리오마다 수용 기준을 명시하는 방식을 조합할 수 있을 것으로 보이나, 로봇 플릿 재현에 이를 적용해 허용 기준을 정한 사례는 찾지 못했다. [추정][^ref-1167][^ref-1177][^ref-1178]

### 실행 전 계획 검증

Luckcuck 외(2019)는 시험·시뮬레이션만으로는 부족하다고 보고 형식 명세·검증 기법을 보완 수단으로 정리했다. [의견][^ref-599] 계획을 실행하지 않고 정적으로 검사하는 도구의 근거는 이번 조사에서 확보하지 못했으므로 [사전 실행 계획 검증](../../glossary/pre-execution-plan-verification.md) 용어와 [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)를 함께 본다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-1167]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-1168]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-406]: Open Robotics, Simulation — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-943]: Lee 외 (Digital Health, SAGE), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1171]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-09-30
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-599]: Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5)), Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019, https://arxiv.org/abs/1807.00048, 접근일 2026-09-30
[^ref-741]: Aljalbout, E., Xing, J., Romero, A. 외 (arXiv), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10-23, https://arxiv.org/abs/2510.20808, 접근일 2026-09-30
[^ref-1177]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30
[^ref-1178]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s4.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1165, ref-831, ref-1167, ref-1168, ref-1172, ref-741, ref-1177]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#4
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어

# 36. 가상 시운전·실제 상황 재현 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 설치 전 시험, 기록 재생, 시뮬레이션 결과의 신뢰 판단 세 갈래로 묶인다.
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 설치 전 시험, 기록 재생, 시뮬레이션 결과의 신뢰 판단 세 갈래로 묶인다.

- **[가상 시운전](../../glossary/virtual-commissioning.md)(Virtual Commissioning)** — VDI/VDE 3693 Blatt 1 은 2025-05 개정판(39쪽, 독·영)에서 가상 시운전을 체계적으로 정의하고 자동화 설비·기계의 수명주기 안에 위치시키며, 기본 시험 구성·시험 방법·필요한 모델 유형·시뮬레이션 구성을 보완했다. [사실][^ref-1165]
- **MiL·SiL·HiL(Model·Software·Hardware-in-the-Loop)** — Rosenberger 외(2023)는 VDI 3693 에 따라 자동화 모델만 쓰는 모델 인 더 루프(MiL), 실제 제어 언어 코드를 하드웨어와 분리해 돌리는 소프트웨어 인 더 루프(SiL), 실제 대상 하드웨어(가상 머신·컨테이너로 가상화한 하드웨어 포함)를 쓰는 하드웨어 인 더 루프(HiL)로 시험 구성을 나눈다. [사실][^ref-1172]
- **[로그 재생](../../glossary/log-playback.md)(Log Playback)** — ROS 2 의 rosbag2 는 토픽 메시지를 시각과 함께 [백 파일](../../glossary/bag-file.md)로 기록·재생하고, `--clock` 옵션으로 재생 세션 동안 `/clock` 을 발행해 재생 데이터에 맞춘 시뮬레이션 시각을 주며, 기본 저장 형식은 [MCAP](../../glossary/mcap.md)이다(2026-09-30 확인). [사실][^ref-831]
- **비반응 재생의 한계** — 기록된 궤적을 그대로 재생하면 주변 에이전트가 바뀐 조건에 반응하지 않으므로, 실제 운영 기록으로 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교하려면 주변 로봇·사람을 반응형 행동 모델로 바꾸는 단계가 필요할 것으로 보인다. [추정][^ref-1168][^ref-831]
- **[현실 격차](../../glossary/reality-gap.md)(Reality Gap)** — Aljalbout 외(2025)는 시뮬레이션이 추상화와 근사로 이루어져 현실과의 차이를 피할 수 없다고 본다. [사실][^ref-741]
- **시뮬레이션–현실 상관 계수(Sim-vs-Real Correlation Coefficient, SRCC)** — Kadian 외(2020)가 제안한 지표로, 시뮬레이션에서의 성능 개선이 실제 성능 개선으로 이어지는지를 잰다. [사실][^ref-1167]
- **모델·시뮬레이션 신뢰도 평가(NASA-STD-7009B)** — NASA-STD-7009B(문서일 2024-03-05, 현행)는 모델·시뮬레이션을 개발·수용·사용하는 요구·권고·기준을 정하고 개정판에서 개발·사용 단계의 신뢰도 평가 산출물에 초점을 두며, 수용 기준은 프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자(Technical Authority)가 승인한다. [사실][^ref-1177] 기존 용어 [시뮬레이션 모델 검증·타당성 확인](../../glossary/verification-and-validation-of-simulation-models.md)과 함께 본다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1165]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-1167]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-1168]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-741]: Aljalbout, E., Xing, J., Romero, A. 외 (arXiv), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10-23, https://arxiv.org/abs/2510.20808, 접근일 2026-09-30
[^ref-1177]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s8.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1167, ref-943, ref-1172, ref-599, ref-741, ref-1175, ref-1178]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#8
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료

# 36. 가상 시운전·실제 상황 재현 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 연구는 분산 가상 시운전, 시뮬레이션 예측력, 현실 격차, 형식 검증, 실제 기록 기반 재현, 시험 시나리오 구성을 다룬다.
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 연구는 분산 가상 시운전, 시뮬레이션 예측력, 현실 격차, 형식 검증, 실제 기록 기반 재현, 시험 시나리오 구성을 다룬다.

- Rosenberger, J. 외, Virtual Commissioning of Distributed Systems in the Industrial Internet of Things(Sensors, 2023) — 가상 시운전을 분산 에지 시스템으로 넓히는 구조 3가지를 제안하고 팔레타이징 포장 설비 시뮬레이션에 실제 제어기와 가상화 인스턴스를 붙여 시험했다. [사실][^ref-1172]
- Kadian, A. 외, Sim2Real Predictivity(IEEE RA-L, 2020) — 시뮬레이션 평가가 실제 성능을 예측하는 정도를 재는 SRCC 를 제안하고 시뮬레이터 조정으로 0.18 을 0.844 로 높였다. [사실][^ref-1167]
- Aljalbout, E. 외, The Reality Gap in Robotics(2025) — 현실 격차의 원인·대응 기법·평가 지표를 보행·주행·조작에 걸쳐 정리한 조사 논문이다(초록 기준). [사실][^ref-741]
- Luckcuck, M. 외, Formal Specification and Verification of Autonomous Robotic Systems: A Survey(ACM Computing Surveys, 2019) — 형식 명세·검증 기법을 정리했고, 저자들은 시험·시뮬레이션만으로는 인증 증거가 부족하다고 본다. [의견][^ref-599]
- Lee 외, Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments(Digital Health, 2026-03) — 한국 병원의 실제 배송 기록 122건과 승강기 데이터로 임계값을 찾고 몬테카를로 시뮬레이션으로 탑승 실패를 재현했다. [사실][^ref-943]
- 최성욱·박상철·왕지남, 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스(대한산업공학회 추계학술대회, 2008) — 실제 PLC 와 가상 공정 시뮬레이터를 연동하는 국내 가상 플랜트 절차다(초록 기준). [사실][^ref-1175]
- Ortega, A. 외, Composable and executable scenarios for simulation-based testing of mobile robots(Frontiers in Robotics and AI, 2024) — 도면 DSL·동적 요소·과제·수용 기준을 조합해 이동로봇 시험 시나리오를 만든다. [사실][^ref-1178]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1167]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-943]: Lee 외 (Digital Health, SAGE), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-599]: Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5)), Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019, https://arxiv.org/abs/1807.00048, 접근일 2026-09-30
[^ref-741]: Aljalbout, E., Xing, J., Romero, A. 외 (arXiv), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10-23, https://arxiv.org/abs/2510.20808, 접근일 2026-09-30
[^ref-1175]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-09-30
[^ref-1178]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s11.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 열린 질문"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1165, ref-1167, ref-1172, ref-1177, ref-1178]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#11
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 열린 질문

# 36. 가상 시운전·실제 상황 재현 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 재현 결과의 현실 일치 판정 기준과 단계별 검증 수준은 부분 근거만 있어 열린 질문으로 남는다. [추정][^ref-1167][^ref-1177]
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

재현 결과의 현실 일치 판정 기준과 단계별 검증 수준은 부분 근거만 있어 열린 질문으로 남는다. [추정][^ref-1167][^ref-1177]

- **oq-132** (상태: 열림) 재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가? 부분 근거로 SRCC 같은 예측력 지표, 수용 기준을 프로그램·프로젝트가 정하고 위임된 NASA 기술 권한자가 승인하는 NASA-STD-7009B 방식, 시나리오별 수용 기준을 조합할 수 있을 것으로 보이나, 로봇 플릿 재현에 적용한 사례는 찾지 못했다. [추정][^ref-1167][^ref-1177][^ref-1178]
- **oq-156** (상태: 열림) 분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? 시뮬레이션 검증·실기 검증 단계는 MiL·SiL·HiL 시험 구성과 NASA-STD-7009B 신뢰도 평가에 부분적으로 대응시킬 수 있을 것으로 보이나, 문서 확인부터 어댑터 연결까지 한 체계로 정한 성숙도 체계는 찾지 못했다. [추정][^ref-1165][^ref-1172][^ref-1177]
- (새 질문, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-17) 여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가?
- (새 질문, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-17) 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가?
- (새 질문, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-17) 물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가?
- (새 질문, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-17) 한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1165]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-1167]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-1177]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30
[^ref-1178]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s10.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 다른 연구영역과의 연결"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1165, ref-831, ref-406, ref-943, ref-1171, ref-1172, ref-599, ref-741, ref-1175, ref-1176, ref-1177, ref-1178, ref-1179]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#10
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 다른 연구영역과의 연결

# 36. 가상 시운전·실제 상황 재현 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 시나리오 형식과 시뮬레이션 엔진, 재현의 원천 기록, 연동 대상 인터페이스, 적용 현장과 이어진다. [추정][^ref-406][^ref-831]
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 시나리오 형식과 시뮬레이션 엔진, 재현의 원천 기록, 연동 대상 인터페이스, 적용 현장과 이어진다. [추정][^ref-406][^ref-831]

- [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) — 2절 원문 주석대로 실제 상황 재현을 대화로 요청하는 짝 영역이다.
- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 도면 주석에서 시뮬레이션 세계를 자동 생성한다. [추정][^ref-406]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 시뮬레이션과 플릿 어댑터가 같은 주행 그래프를 쓴다. [추정][^ref-406]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 현재 상태를 표현하는 실시간 기록이 재현의 원천이 된다. [추정][^ref-831]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 플릿 어댑터의 가상 대응물을 붙여 시험하며, VDA 5050 은 시운전 절차를 정하지 않는다. [추정][^ref-406][^ref-031]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 문·승강기 가상화와 병원 승강기 실패 재현이 이어진다. [추정][^ref-406][^ref-943]
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 재현·혼합 현실 환경에서 배차 정책을 비교한다. [추정][^ref-943][^ref-1171]
- [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) — 환경·동적 요소·수용 기준을 담는 시나리오 형식을 준다. [추정][^ref-1178]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 시뮬레이션 엔진과 가정한 미래의 실험을 맡고, 이 영역은 그 엔진으로 설치 전 시운전과 실제 상황 재현을 한다. [추정][^ref-406][^ref-741]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 재현에 쓸 실행 기록을 남긴다. [추정][^ref-831]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 기록으로 찾은 실패 원인을 재현으로 확인한다. [추정][^ref-943]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 현실 격차를 줄이는 학습 기법은 L. AI·학습 기술의 연구 방법이다. [추정][^ref-741]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 형식 검증과 모델·시뮬레이션 신뢰도 평가를 공유한다. [추정][^ref-599][^ref-1177]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 가상 시운전 다음에 실제 현장 시운전이 온다. [추정][^ref-1165][^ref-1179]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 물류센터 설비 에뮬레이션 사례(벤더 주장)가 있다. [추정][^ref-1179]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 분산 제어·PLC 가상 시운전과 가상 공장 사례가 있다. [추정][^ref-1172][^ref-1175][^ref-1176]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 실제 기록 기반 승강기 탑승 실패 재현 사례가 있다. [추정][^ref-943]
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 대학 건물 시뮬레이션 시험 시나리오 사례가 있다. [추정][^ref-1178]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1165]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-406]: Open Robotics, Simulation — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-943]: Lee 외 (Digital Health, SAGE), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1171]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-09-30
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-599]: Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5)), Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019, https://arxiv.org/abs/1807.00048, 접근일 2026-09-30
[^ref-741]: Aljalbout, E., Xing, J., Romero, A. 외 (arXiv), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10-23, https://arxiv.org/abs/2510.20808, 접근일 2026-09-30
[^ref-1175]: 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회), 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스, 2008-11, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794, 접근일 2026-09-30
[^ref-1176]: 현대자동차그룹, 가상의 디지털 공간에 세운 쌍둥이 공장, 2023-11-21, https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330, 접근일 2026-09-30
[^ref-1177]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30
[^ref-1178]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full, 접근일 2026-09-30
[^ref-1179]: Rockwell Automation, Emulation Technology Speeds Up Warehouse Automation, 2024-08-28, https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s7.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1165, ref-831, ref-1168, ref-406, ref-1171, ref-1177]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#7
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 관련 표준·프레임워크·오픈소스

# 36. 가상 시운전·실제 상황 재현 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 가상 시운전의 정의와 시험 구성은 VDI/VDE 3693 이, 모델·시뮬레이션 결과의 수용은 NASA-STD-7009B 가 다루며, 여러 로봇 시뮬레이션과 기록 재생에는 Open-RMF 와 rosbag2 가 쓰인다. [사실][^ref-1165][^ref-1177][^ref-406][^ref-831]
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

가상 시운전의 정의와 시험 구성은 VDI/VDE 3693 이, 모델·시뮬레이션 결과의 수용은 NASA-STD-7009B 가 다루며, 여러 로봇 시뮬레이션과 기록 재생에는 Open-RMF 와 rosbag2 가 쓰인다. [사실][^ref-1165][^ref-1177][^ref-406][^ref-831]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| VDI/VDE 3693 Blatt 1 (2025-05 개정판) | 표준 | 가상 시운전의 정의·수명주기 내 위치·시험 구성·시험 방법·모델 유형·시뮬레이션 구성. 본문은 유료로 공식 소개 페이지 기준. [사실] | [^ref-1165] |
| NASA-STD-7009B (2024-03-05, 현행) | 표준 | 모델·시뮬레이션의 개발·수용·사용 요구와 신뢰도 평가. 수용 기준은 프로그램·프로젝트가 정하고 위임된 기술 권한자가 승인. [사실] | [^ref-1177] |
| Open-RMF 시뮬레이션(Gazebo·Ignition 플러그인) | 오픈소스 | 도면 주석에서 세계·주행 그래프를 만들고 로봇·문·승강기·작업셀·군중을 가상화해 배치 전 시험. [사실] | [^ref-406] |
| rosbag2 (기본 저장 형식 MCAP) | 오픈소스 | 토픽 기록·재생, 재생 중 /clock 발행, 재생 제어 서비스. [사실] | [^ref-831] |
| VDA 5050 3.0.0 | 표준 | 시운전 작업 흐름·검증·인수 절차를 명세 범위 밖에 둔다. [사실] | [^ref-031] |
| Waymax | 프레임워크(연계 대상) | 자율주행 기록으로 다중 에이전트 시나리오를 초기화·재생하는 가속 시뮬레이터. 재현 방법의 참고. [사실] | [^ref-1168] |
| VirTooS | 프레임워크(소스 공개 예정) | ROS 2–Unity 혼합 현실로 실제·가상 로봇 함께 AMR 플릿 작업 배정 실험. [사실] | [^ref-1171] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1165]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-1168]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-406]: Open Robotics, Simulation — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-1171]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-09-30
[^ref-1177]: NASA, NASA-STD-7009B Standard for Models and Simulations, 2024-03-05, https://standards.nasa.gov/standard/NASA/NASA-STD-7009, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-17/pages/topics/2026/2026-09-30-area36-s3.md

```markdown
---
title: "36. 가상 시운전·실제 상황 재현 — 왜 중요한가"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 36
related_areas: [11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1165, ref-831, ref-1167, ref-1168, ref-406, ref-1171, ref-1172, ref-599]
last_run: 2026-09-30
version: 1
split_from: docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md#3
---

[홈](../../index.md) › [주제](../index.md) › 36. 가상 시운전·실제 상황 재현 — 왜 중요한가

# 36. 가상 시운전·실제 상황 재현 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 설치 전 가상 시운전은 제조·물류 설비 제어 분야에서 VDI/VDE 3693 과 MiL·SiL·HiL 시험 구성으로 정립되어 있고 여러 로봇 쪽에도 Open-RMF 시뮬레이션과 혼합 현실 도구가 있지만, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차 표준은 이번 조사에서 확인하지 못했다. [추정][^ref-1165][^ref-1172][^ref-406][^ref-1171]
- 이 페이지는 [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

설치 전 가상 시운전은 제조·물류 설비 제어 분야에서 VDI/VDE 3693 과 MiL·SiL·HiL 시험 구성으로 정립되어 있고 여러 로봇 쪽에도 Open-RMF 시뮬레이션과 혼합 현실 도구가 있지만, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차 표준은 이번 조사에서 확인하지 못했다. [추정][^ref-1165][^ref-1172][^ref-406][^ref-1171]

실제로 있었던 문제를 다시 보는 쪽에서도, 운영 기록을 시각과 함께 재생하는 도구(rosbag2)와 실제 기록으로 다중 에이전트 시나리오를 초기화하는 시뮬레이터(자율주행 분야의 Waymax)는 있지만 재현 결과가 현실과 맞는지 판정하는 기준은 찾지 못했다. [추정][^ref-831][^ref-1168][^ref-1167]

인터페이스 규격도 이 빈틈을 채우지 않는데, VDA 5050 3.0.0 명세는 시운전 작업 흐름과 검증·인수 절차를 포함하는 프로젝트 조정·수행 절차를 명세 범위 밖에 두므로 이 규격을 따르는 것만으로 여러 제조사 로봇의 시운전 절차가 정해지지는 않는다. [사실][^ref-031]

Luckcuck 외(2019)는 자율 로봇이 복잡하고 혼성적이며 안전에 중요한 시스템이어서 시험과 시뮬레이션만으로는 정확성을 보장하거나 인증에 충분한 증거를 내기 어렵다는 의견을 밝혔다. [의견][^ref-599] 한 로봇 주행 연구에서는 시뮬레이션 평가가 실제 성능을 거의 예측하지 못하다가(성공률 기준 SRCC 0.18) 시뮬레이터 설정을 고친 뒤에야 예측력이 높아졌다(0.844). [사실][^ref-1167]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)
- 관련 영역: [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1165]: VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik), VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions, 2025-05, https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions, 접근일 2026-09-30
[^ref-831]: ROS 2 (Open Robotics 외, ros2/rosbag2 저장소), rosbag2 README, 미확인, https://github.com/ros2/rosbag2, 접근일 2026-09-30
[^ref-1167]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-09-30 (원문 미열람)
[^ref-1168]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-406]: Open Robotics, Simulation — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-30
[^ref-1171]: Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv), VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots, 2026-08-26, https://arxiv.org/abs/2608.26066, 접근일 2026-09-30
[^ref-1172]: Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545), Virtual Commissioning of Distributed Systems in the Industrial Internet of Things, 2023-03-28, https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/, 접근일 2026-09-30
[^ref-599]: Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5)), Formal Specification and Verification of Autonomous Robotic Systems: A Survey, 2019, https://arxiv.org/abs/1807.00048, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-17 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-17 | 36. 가상 시운전·실제 상황 재현 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1123건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 313개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
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
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
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
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
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
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
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
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
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
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
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
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
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
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
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

### docs/open-questions.md (요약: 대상 영역 [36] 에 걸린 2건 / 전체 250건)

```markdown
- oq-132 [열림] 재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표(사건 순서 유사도·시각 오차·처리량 오차)와 허용 기준은 무엇이며, 그 판정을 누가 승인해야 조건 변경 비교의 근거로 쓸 수 있는가? (영역 11, 36, 54)
- oq-156 [열림] 분류 원문이 말하는 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)에 대응하는 기존 검증 수준·성숙도 체계가 있는가, 아니면 ROP 가 자체 정의해야 하는가? (영역 7, 54, 36)
```
