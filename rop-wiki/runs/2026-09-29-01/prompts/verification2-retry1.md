(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-01
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 8. 채팅으로 맵 작성 (C. 채팅 기반 구성·운영)
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
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-29-01/target.json

```json
{
  "run_id": "2026-09-29-01",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 93,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 8,
    "area_name": "8. 채팅으로 맵 작성",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=8"
}
```

### runs/2026-09-29-01/research.json

```json
{
  "run_id": "2026-09-29-01",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 8,
    "area_name": "8. 채팅으로 맵 작성",
    "category": "C. 채팅 기반 구성·운영"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 위상 지도·의미 지도·빌딩 맵·레이아웃 교환 형식·축척 보정·명확화 질문 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음",
    "섹션 6. 대표 접근법과 기술 비어 있음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음 — 원문 주석대로 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델과 짝 연결 필요",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문·정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]",
    "자연어 설명이나 경로 지시만으로 로봇용 위상·의미 지도를 만들거나 편집하는 연구는 무엇이 있고 어느 정도 정확한가? (섹션 6·8 겨냥)",
    "언어 모델로 평면도를 생성·편집·이해하는 연구는 기하·위상 제약을 얼마나 지키며 어떤 한계가 보고되는가? (섹션 3·6·8·11 겨냥)",
    "대화 결과를 담을 지도 형식(Open-RMF 빌딩 맵, VDMA LIF·VDA 5050 노드·에지, 도면 변환 결과)은 층·구역·통로·문·승강기·충전 위치를 어떤 요소로 표현하고 축척은 어떻게 정하는가? (섹션 4·7 겨냥)",
    "병원·제조 공장·실외 같은 현장 유형에서 층·승강기·문을 포함한 지도 작성·정합 사례는 무엇인가? (섹션 5 겨냥, 국내 자료 포함)",
    "말로 확정할 수 없는 값(축척·치수·통과 조건)을 확인 질문으로 받아 확정하는 방식의 근거가 되는 대화 연구는 무엇인가? (섹션 4·6 겨냥, 13. 대화형 기능의 신뢰·기반 연결)",
    "지도 작성에서 ROP가 직접 맡을 것과 로봇 자체 SLAM·도면 해석 등 외부에 맡길 것의 경계는 어디인가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Deguchi 외(ICRA 2024)는 대규모 언어 모델로 자연어 경로 지시문을 노드·에지·행동으로 된 위상 지도로 바꾸는 방법을 제안했고, 기하 지도나 카메라 없이 언어만으로 지도를 만들며, 지도를 언어 모델 기억에 암묵적으로 두는 것보다 명시적 위상 지도를 만드는 쪽이 정확도가 뚜렷이 높았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-815"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: 입력은 자연어 경로 지시, 출력은 노드·에지·행동의 위상 지도. \"generating explicit maps achieves significantly higher accuracy than storing implicit maps in the LLMs\". 실제 환경에서 만든 경로 지시로 평가. ICRA 2024 채택.",
      "as_of": "2024-03-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "SENT-Map(2025)은 실내 환경을 의미 정보가 붙은 JSON 형식 위상 지도로 표현해 사람과 기반 모델이 같은 형식을 읽고 고칠 수 있게 하며, 시각 기반 모델과 운영자가 짝을 이뤄 지도를 만든 뒤 자연어 질의로 계획하는 2단계 방식으로 소형 로컬 모델도 실내 계획을 할 수 있음을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-816"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: JSON 위상 지도에 의미 정보를 더해 사람과 기반 모델이 함께 편집. 1단계 시각 기반 모델+운영자 지도 작성, 2단계 자연어 질의 계획. ICRA 2025 워크숍 채택.",
      "as_of": "2025-11-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Walter 외(RSS 2013)는 사람이 말로 설명한 장소 이름과 공간 관계를 센서 관측과 함께 계량·위상·의미가 결합된 의미 그래프로 공동 추정하는 알고리즘을 제시했고, 자연어를 넣으면 센서만 쓸 때보다 지도 정확도가 올라간다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-819"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RSS IX 초록: \"jointly estimates a hybrid metric, topological, and semantic representation of the environment\". 자연어 흐름과 저수준 센서 정보를 바탕으로 의미 그래프의 분포를 유지. 자연어 포함 시 계량·위상·의미 모두 정확도 향상.",
      "as_of": "2013-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "위 세 연구를 보면 대화로 만드는 지도는 장소·연결·이름 같은 위상·의미 층을 담는 데 강점이 있고 정확한 기하(치수·좌표)는 센서·도면·사람 확인에서 와야 하므로, ROP의 채팅 맵 작성은 위상·의미 요소를 대화로 만들고 기하 정합은 별도 입력으로 받는 구조가 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-815",
        "ref-816",
        "ref-819"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1은 언어만으로 위상 지도, f2는 JSON 위상 지도의 사람·모델 공동 편집, f3은 언어와 센서의 결합 추정을 다루며 셋 다 순수 언어에서 정확한 계량 기하를 얻는다고 주장하지 않는다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Tell2Design(ACL 2023)은 자연어 지시와 짝지은 8만 건 이상의 평면도 설계 데이터셋으로 언어 유도 평면도 생성 과제를 제시했고, 예술적 이미지 생성과 달리 공간·관계 제약을 만족해야 하는 점을 핵심 난점으로 꼽았다.",
      "tag": "사실",
      "source_ids": [
        "ref-817"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: 8만 건 이상의 평면도와 자연어 지시. \"designs must satisfy different constraints ... particularly spatial and relational constraints\". Seq2Seq 기준 모델과 텍스트 조건 이미지 생성 모델 비교, 사람 평가 포함.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "HouseMind(CVPR 2026)는 방 단위 이산 토큰으로 어휘를 만들어 멀티모달 언어 모델 하나가 평면도를 이해·생성하고 텍스트 지시로 편집하게 했으며, 기하 타당성과 제어 가능성이 기존 확산·언어 모델 방식보다 낫고 로컬 배포가 가능하다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-823"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: \"discrete room-instance tokens to construct a unified vocabulary\"로 이해·생성·편집을 한 모델에 통합. 텍스트 지시로 제어 가능한 편집. 기하 타당성·제어 가능성 우위, 로컬 배포 가능 주장.",
      "as_of": "2026-03-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Holodeck(CVPR 2024)은 한 문장 설명에서 GPT-4가 평면도·출입구·창·재질을 설계하고 객체 사이 공간 관계 제약을 생성해 최적화로 배치하는 방식으로 3D 실내 환경을 만들며, 사람 평가에서 주거 장면에 대해 절차적 생성 기준선보다 선호되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-825"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: GPT-4가 \"generate spatial relational constraints between objects\" 뒤 제약 최적화로 배치. Objaverse 3D 자산 사용. 주거 장면 사람 평가에서 절차적 기준선보다 선호. 신규 장면 객체 내비게이션으로 유용성 검증.",
      "as_of": "2023-12-14",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "FloorplanQA(2025)는 JSON·XML 로 기술한 실내 평면도에 대해 거리 측정·가시성·경로 찾기·객체 배치 질문으로 최신 공개·상용 언어 모델을 평가했고, 모델들이 단순 질문은 처리하지만 물리 제약을 지키지 못하고 공간 일관성을 잃는 약점이 있다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-822"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: 구조화 텍스트 평면도에 대한 네 가지 공간 능력 평가. 모델들은 \"often fail to respect physical constraints, preserve spatial coherence\". 작은 공간 변화에는 비교적 강건.",
      "as_of": "2025-07-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "평면도 생성 데이터셋 연구와 평면도 공간 추론 벤치마크가 서로 독립적으로 언어 모델의 공간·물리 제약 준수를 핵심 난점으로 지목하므로, 채팅으로 만든 층·구역·통로·문 배치는 언어 모델 출력 그대로 쓰지 말고 기하 검증기나 사람 확인을 거쳐야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-817",
        "ref-822"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "Tell2Design(싱가포르·SUTD 등, 2023)은 공간·관계 제약 만족을 난점으로, FloorplanQA(KAUST 등, 2025)는 물리 제약 미준수·공간 일관성 상실을 실측 약점으로 보고. 발행 기관·저자가 다른 두 출처가 같은 방향을 말한다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "Open-RMF 의 Traffic Editor 는 2D 평면도 이미지 위에 층(레벨)·벽·꼭짓점(충전소·주차·도킹 속성 부여 가능)·플릿별 교통 차선·문 4종(여닫이·양여닫이·미닫이·양미닫이)·여러 층을 잇는 승강기·바닥 다각형을 그려 제조사 중립 빌딩 맵을 만들고 결과를 .building.yaml 로 저장한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "mdBook 원문(traffic-editor.md): 레벨·벽(기본 두께 10cm·높이 2.5m)·꼭짓점 속성·플릿별 내비게이션 그래프·문 4종·승강기·바닥. 주석은 YAML(.building.yaml)로 저장. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f11",
      "claim": "Traffic Editor 에서 층의 축척은 사용자가 실제 거리를 아는 두 점 사이에 측정선을 긋고 그 물리 거리를 미터로 입력해야 정해지므로, 평면도 이미지만으로는 축척이 확정되지 않고 사람이 값을 넣어야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "Traffic Editor 의 빌딩 맵이 층·차선·문·승강기·충전 위치를 담는 텍스트(YAML) 구조이고 축척은 사람이 준 거리로 정해지는 점을 보면, 채팅 맵 작성은 이런 텍스트 지도 구조를 대화로 채우되 축척·치수처럼 말로 확정할 수 없는 값은 확인 질문으로 받는 흐름이 자연스러울 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-079",
        "ref-816"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10·f11(빌딩 맵의 요소와 축척 입력 방식)과 f2(사람과 모델이 함께 읽고 고치는 JSON 지도)에서 도출한 추정이며, 대화로 빌딩 맵을 채운 사례를 직접 확인한 것은 아니다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f13",
      "claim": "Open-RMF 공식 데모 저장소의 Clinic 월드는 두 층과 승강기 2대, 역할이 다른 로봇 플릿 2개를 두고 로봇이 승강기로 층을 오가는 시뮬레이션 빌딩 맵이며, Hotel 월드는 객실 층 2개·로비·승강기 2대·여러 문·플릿 3개를 둔다(실제 현장 배치가 아닌 시뮬레이션 데모).",
      "tag": "사실",
      "source_ids": [
        "ref-104"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_demos README: Clinic World — \"Two different robot fleets with different roles navigate across two levels by lifts.\" Hotel World — 객실 층 2개, 로비, 승강기 2대, 여러 문, 플릿 3개(로봇 4대). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합자가 노드·에지·스테이션으로 된 주행 레이아웃을 제3자 관제 시스템에 처음 넘겨 주기 위한 형식이며 VDA 5050 의 영향을 받아 정의되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-046"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 저장소 README: 버전 1.0.0, 2023-09. \"The integrator of the driverless transport vehicles will be able to initially transfer a track layout to a central (third-party) master control system for use and integration.\" VDA 5050 영향 명시. 법적 구속력 없음.",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f15",
      "claim": "LIF 의 노드·에지·스테이션과 Open-RMF 빌딩 맵의 꼭짓점·차선·문·승강기처럼 플릿 관제가 실제로 읽는 지도 형식이 이미 여럿이므로, 채팅 맵 작성의 결과물은 자유 서술이 아니라 이런 형식에 맞는 구조화 지도 요소여야 하고 형식마다 요소 대응(예: 충전 위치를 스테이션·꼭짓점 속성 어디에 둘지)이 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-046",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f14(LIF 노드·에지·스테이션)와 f10(빌딩 맵 요소)의 비교에서 도출. 두 형식 사이의 공식 변환 규칙은 이번 조사에서 확인하지 못했다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Zhang 외(2025)는 건축 CAD 파일에서 구조 레이어 분리, AreaGraph 기반 위상 분할, 도면 글자와 방의 자동 연결, 다층 융합을 거쳐 로봇 내비게이션용 계층 위상·계량 OSM 지도를 자동 생성하는 GUI 포함 파이프라인을 제시하며, SLAM 기반 지도 작성은 시간·노동·강건성에서 한계가 있다고 주장했다.",
      "tag": "사실",
      "source_ids": [
        "ref-083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록: CAD → \"hierarchical topometric OpenStreetMap (OSM) representation\". 레이어 분리·AreaGraph 분할·텍스트-방 연결·다층 융합. SLAM 은 대규모 동적 실내에서 시간·노동·강건성 한계. 코드·데이터셋 공개.",
      "as_of": "2025-07-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "김영재·김세윤·김홍준(2022)은 공공 지도 서비스 데이터로 자율주행 이동 로봇의 분기점 단위 전역 경로 계획용 위상 지도를 구축하는 방법을 제안하고 A* 모의실험으로 유효성을 검증해, 실외 로봇 서비스의 지도 구축 비용을 줄일 수 있다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-820"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DBpia 초록(대한공간정보학회지 30권 2호, 2022-06): 공공지도 서비스 기반 \"분기점 단위의 전역경로계획용 지도\" 설계·구현, A* 기반 모의실험, 전역경로 계획 데이터 생성 비용 절감.",
      "as_of": "2022-06",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "연계 대상: 노주형 외(2026, 로봇학회 논문지)는 3D 라이다·IMU SLAM 과 프런티어 탐사, 매니퓰레이터로 승강기 버튼을 누르는 승강기 연동으로 로봇이 다층 실내 지도를 스스로 만드는 시스템을 제시해 KAIST N1 건물 5개 층을 27분에 지도화하고 승강기 상호작용 성공률 95%를 보고했으며, 이는 로봇 자체 지능·제어 쪽 지도 작성이다.",
      "tag": "사실",
      "source_ids": [
        "ref-163"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록(21권 1호, 48–57쪽): 3D LiDAR–IMU SLAM·다중 센서 융합 코스트맵·프런티어 탐사, RGB-D 카메라와 4자유도 매니퓰레이터로 버튼 조작. 5F–9F 27분 완료, 승강기 성공률 95%, 탐사 시간 약 33% 단축.",
      "as_of": "2026",
      "site_type": "기타",
      "flow_item": "수행 자원"
    },
    {
      "id": "f19",
      "claim": "국내 업체 모빌리오는 공장 순찰 로봇 관제 화면에서 2D 라이다 지도(PGM)와 CAD·BIM 도면을 기둥·모서리 같은 기준점 3개 이상으로 맞춰 좌표계를 일치시킨 뒤 회전각·크기를 미세 조정해 정합하는 '맵 정합' 기능을 제공한다고 밝히며, 도면 자체나 구역을 편집하는 기능은 설명하지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-827"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"기둥·모서리 등 기준점 3개 이상(A, B, C)을 지정해 좌표계 일치\" 뒤 회전각·크기 미세 조정으로 1:1 정합. 경로는 웨이포인트 티칭. 게시일 2026-08-24, 공장·산업 현장 대상.",
      "as_of": "2026-08-24",
      "site_type": "제조 공장",
      "flow_item": "완료·인계",
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "Doğan·Torre·Leite(HRI 2022)는 요청에서 가리킨 물체가 모호할 때 로봇이 아는 환경 정보로 후속 명확화 질문을 하는 시스템을 63명 사용자 연구로 평가해, 명확화 질문을 받은 사람들이 과제를 더 쉽게 느끼고 로봇의 과제 이해·역량을 더 높게 평가했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-826"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약: HRI '22, IEEE Press 461–469. 63명 사용자 연구. 명확화 질문 시 과제가 더 쉽게 느껴지고 로봇의 이해·역량 평가가 높아짐. 프레임 차이(예: '의자 오른쪽')로 인한 공간 모호성도 다룸.",
      "as_of": "2022-03",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "명확화 질문이 사용자 인식을 개선한다는 연구와 축척이 사람의 거리 입력으로만 정해지는 편집기 관행을 함께 보면, 채팅 맵 작성은 축척·치수·통과 조건처럼 말로 확정할 수 없는 값을 모델이 추정해 채우지 않고 선택지가 붙은 확인 질문으로 받는 쪽이 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-826",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f20(명확화 질문의 효과)과 f11(축척은 사람이 준 거리로 확정)에서 도출. 지도 작성 대화에 특화된 확인 질문 연구는 이번 조사에서 찾지 못했다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f22",
      "claim": "연계 대상: 라이다 SLAM 으로 점유 격자를 만들고 위치를 추정하는 일(노주형 외, 모빌리오의 PGM 지도)과 도면을 벡터·위상 구조로 해석하는 일(Zhang 외)은 각각 분류 원문 19장의 로봇 자체 지능·제어와 14. 도면·BIM에서 지도 만들기·45. 문서·도면·장면 이해의 몫이며, 8. 채팅으로 맵 작성은 그 결과를 입력으로 받는 쪽이다.",
      "tag": "추정",
      "source_ids": [
        "ref-163",
        "ref-827",
        "ref-083"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f16·f18·f19의 대상(CAD 변환, 로봇 SLAM, 라이다 지도–도면 정합)을 분류 원문 19장의 경계와 C. 채팅 기반 구성·운영 주석(맵 작성은 14·15번의 기능을 대화로 쓰게 하는 것)에 대조한 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "8. 채팅으로 맵 작성에서 ROP가 직접 맡을 범위는 대화에서 층·구역·통로·문·승강기·충전 위치 같은 구조화 지도 요소를 만들어 플릿 중립 형식(빌딩 맵·LIF 류)에 담고, 확정할 수 없는 값을 확인 질문으로 받아 사람이 화면에서 확인·승인한 지도만 확정하는 일이며, 기하 지도 생성과 도면 해석 엔진은 연계 대상으로 두는 것이 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-079",
        "ref-046",
        "ref-816",
        "ref-822"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10·f14(대상 형식), f2(사람·모델 공동 편집 가능한 텍스트 지도), f8(언어 모델의 공간 제약 미준수)을 원문 19장 경계와 '사람이 확인·승인한 계획만 실행' 주석에 맞춘 추정.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f24",
      "claim": "언어·멀티모달 모델로 평면도를 이해·생성·편집하거나(HouseMind, FloorplanQA) CAD 에서 지도를 뽑는(Zhang 외) 연구는 L. AI·학습 기술의 45. 문서·도면·장면 이해에 속하는 방법이며, 원문 교차 규칙대로 적용 대상인 14. 도면·BIM에서 지도 만들기와 이 영역 양쪽에서 연결해야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-823",
        "ref-822",
        "ref-083"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f8·f16의 대상이 도면·평면도 해석이며, 분류 원문 L 주석은 도면 해석을 14번에 적용되는 연구 방법으로 둔다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-815",
      "org": "Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs)",
      "title": "Language to Map: Topological map generation from natural language path instructions",
      "published": "2024-03-15",
      "url": "https://arxiv.org/abs/2403.10008",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 경로 지시문을 언어 모델로 노드·에지·행동의 명시적 위상 지도로 바꾸는 방법. 암묵적 지도보다 정확도가 높음. ICRA 2024.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-816",
      "org": "Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K.",
      "title": "SENT Map -- Semantically Enhanced Topological Maps with Foundation Models",
      "published": "2025-11-05",
      "url": "https://arxiv.org/abs/2511.03165",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "사람과 기반 모델이 함께 읽고 고치는 JSON 위상 지도 표현. 운영자와 시각 기반 모델이 짝지어 지도를 만들고 자연어 질의로 계획. ICRA 2025 워크숍.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-817",
      "org": "Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W.",
      "title": "Tell2Design: A Dataset for Language-Guided Floor Plan Generation",
      "published": "2023",
      "url": "https://arxiv.org/abs/2311.15941",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 지시와 짝지은 8만 건 이상 평면도 데이터셋과 Seq2Seq 기준 모델. 공간·관계 제약 만족이 핵심 난점. ACL 2023.",
      "fetched": true,
      "fetched_via": "webfetch",
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
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 빌딩 맵 편집기 설명: 레벨·벽·꼭짓점·차선·문·승강기·바닥 요소, 측정선으로 축척 설정, .building.yaml 저장.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-819",
      "org": "Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX)",
      "title": "Learning Semantic Maps from Natural Language Descriptions",
      "published": "2013-06",
      "url": "https://www.roboticsproceedings.org/rss09/p04.html",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "말로 된 장소 설명과 센서 관측을 결합해 계량·위상·의미 지도를 공동 추정하는 의미 그래프 방법. 자연어 포함 시 정확도 향상.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-820",
      "org": "김영재, 김세윤, 김홍준 (대한공간정보학회지)",
      "title": "공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구",
      "published": "2022-06",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "공공 지도 서비스 데이터로 실외 이동 로봇의 분기점 단위 위상 지도를 구축하고 A* 모의실험으로 검증한 국내 논문.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF GitHub)",
      "title": "Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA)",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDMA 레이아웃 교환 형식 1.0.0 공식 저장소 README. 통합자가 노드·에지·스테이션 레이아웃을 제3자 관제에 넘기는 형식, VDA 5050 영향.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/Intralogistics-2X-LIF/Layout-Interchange-Format/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-822",
      "org": "Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P.",
      "title": "FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations",
      "published": "2025-07-10",
      "url": "https://arxiv.org/abs/2507.07644",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "JSON·XML 평면도에 대한 거리·가시성·경로·배치 질문 벤치마크. 언어 모델이 물리 제약과 공간 일관성을 자주 어김.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-823",
      "org": "Qin, S., Weber, R. E., & Lu, X.",
      "title": "Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans",
      "published": "2026-03-12",
      "url": "https://arxiv.org/abs/2603.11640",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "방 단위 토큰으로 멀티모달 언어 모델이 평면도를 이해·생성·텍스트 지시로 편집하는 HouseMind. CVPR 2026.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — README (Demonstrations of Open-RMF)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 공식 데모 월드 목록: Hotel(2층·승강기 2대·문·플릿 3개), Office, Airport Terminal, Clinic(2층·승강기 2대·플릿 2개), Campus, Manufacturing & Logistics.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_demos/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-825",
      "org": "Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등)",
      "title": "Holodeck: Language Guided Generation of 3D Embodied AI Environments",
      "published": "2023-12-14",
      "url": "https://arxiv.org/abs/2312.09067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "텍스트 설명에서 GPT-4 가 평면도·출입구·창을 설계하고 공간 관계 제약 최적화로 3D 실내 환경을 생성. 사람 평가에서 절차적 기준선보다 선호. CVPR 2024.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-826",
      "org": "Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022)",
      "title": "Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation",
      "published": "2022-03",
      "url": "https://dl.acm.org/doi/10.5555/3523760.3523822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 모호한 요청에 로봇이 후속 명확화 질문을 하는 시스템의 63명 사용자 연구. 질문을 받은 사용자가 과제를 쉽게 느끼고 로봇 역량을 높게 평가.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-827",
      "org": "모빌리오(Mobilio)",
      "title": "[최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법",
      "published": "2026-08-24",
      "url": "https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "국내 업체의 공장 순찰 로봇 관제 소개. 2D 라이다 지도와 CAD·BIM 도면을 기준점 3개 이상으로 정합하는 맵 정합 기능을 주장.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-083",
      "org": "Zhang, J., Wu, S., Ma, X., & Schwertfeger, S.",
      "title": "Generation of Indoor Open Street Maps for Robot Navigation from CAD Files",
      "published": "2025-07-01",
      "url": "https://arxiv.org/abs/2507.00552",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "건축 CAD 파일에서 레이어 분리·AreaGraph 분할·글자–방 연결·다층 융합으로 로봇용 계층 위상·계량 OSM 지도를 자동 생성. GUI·코드 공개.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-163",
      "org": "노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지)",
      "title": "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템",
      "published": "2026",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "3D 라이다·IMU SLAM 과 프런티어 탐사, 매니퓰레이터 승강기 버튼 조작으로 다층 실내 지도를 자동 구축. KAIST N1 5개 층 27분, 승강기 성공률 95%.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
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
      "rationale": "섹션 3: f9(언어 모델의 공간 제약 미준수 → 확인·검증 필요), f16(SLAM 지도 작성의 시간·노동 한계와 도면 활용), f11(축척은 사람이 줘야 확정) / 섹션 4: f1(위상 지도), f2(사람·모델이 함께 고치는 JSON 지도), f10(빌딩 맵 요소), f11(축척 보정), f14(레이아웃 교환 형식), f20(명확화 질문) / 섹션 5: 병원 — f13(Clinic 데모 월드의 2층·승강기 2대, 시뮬레이션임을 명시), 제조 공장 — f19(벤더 주장 병기, 라이다 지도–도면 정합), 실외 — f17(공공 지도 기반 위상 지도), 기타 — f18(연계 대상: 대학 건물 다층 자율 지도화) / 섹션 6: f1·f3(언어→위상·의미 지도), f2(공동 편집 텍스트 지도), f5·f6·f7(언어→평면도 생성·편집), f8·f9(공간 추론 한계와 검증), f12·f21(텍스트 지도 구조를 대화로 채우고 확정 불가 값은 확인 질문) / 섹션 7: f10·f11(Open-RMF Traffic Editor·building.yaml), f14·f15(VDMA LIF·VDA 5050 노드·에지·스테이션), f13(rmf_demos) / 섹션 8: f1, f2, f3, f5, f6, f7, f8, f16, 국내 f17·f18 / 섹션 9: f22(연계 대상: SLAM·도면 해석), f23(직접 범위: 구조화 지도 요소 생성·확인 질문·사람 승인) / 섹션 10: 14. 도면·BIM에서 지도 만들기(f16·f24), 15. 지도·공간·위치 모델(f10·f14·f15), 16. 장소 의미·지도 관리(f2·f3), 45. 문서·도면·장면 이해(f24, 교차 규칙), 13. 대화형 기능의 신뢰·기반(f9·f20·f21), 22. 설비·건물 시스템 연동(f13 승강기·문), 20. 로봇·제조사 관제 연동(f14), 21. 상호운용 표준·적합성(f15) / 섹션 11: open_questions_new 3건. 다음 실행 후보: 14. 도면·BIM에서 지도 만들기 페이지에 f16·f24 반영, 15. 지도·공간·위치 모델 페이지에 f14·f15 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "트래픽 에디터",
      "term_en": "Traffic Editor (Open-RMF)",
      "definition": "2D 평면도 이미지 위에 층·벽·꼭짓점·플릿별 차선·문·승강기를 그려 제조사 중립 빌딩 맵(.building.yaml)을 만드는 Open-RMF 의 GUI 편집 도구이다."
    },
    {
      "term_ko": "언어 유도 평면도 생성",
      "term_en": "Language-guided Floor Plan Generation",
      "definition": "방 종류·위치·크기·관계를 적은 자연어 설명에서 공간·관계 제약을 만족하는 평면도를 생성하는 과제이다."
    },
    {
      "term_ko": "명확화 질문",
      "term_en": "Clarification Question (Follow-up Clarification)",
      "definition": "요청이 모호할 때 시스템이 아는 정보를 바탕으로 사용자에게 되묻는 질문으로, 확정할 수 없는 값을 추정으로 채우지 않고 사람에게 확인받는 대화 장치이다."
    }
  ],
  "open_questions_new": [
    "대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? | 관련 영역: 8. 채팅으로 맵 작성, 15. 지도·공간·위치 모델, 21. 상호운용 표준·적합성 | 근거: f15 | 종류: 일반",
    "언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가? | 관련 영역: 8. 채팅으로 맵 작성, 13. 대화형 기능의 신뢰·기반 | 근거: f9 | 종류: 일반",
    "채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가? | 관련 영역: 8. 채팅으로 맵 작성, 14. 도면·BIM에서 지도 만들기, 55. 현장 조사·설치·시운전 | 근거: f22 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 1,
    "unverified": [
      "f20 ACM 원문 403 으로 미열람, 검색 결과 요약(63명 사용자 연구, 효과)만 사용",
      "f19 모빌리오 맵 정합 기능은 벤더 주장이며 독립 출처 교차 확인 없음",
      "f9 외 모든 finding 교차 확인 실패(연구·문서마다 발행 주체 한 곳)",
      "f10·f11·f13 발행일 미확인(오픈소스 문서)",
      "VDMA LIF 공식 가이드라인 PDF 는 텍스트 추출 실패로 공식 저장소 README 만 확인, JSON 구조 세부(층·지도 id 필드)는 미확인",
      "ArchPlanVQA(ASCE, 도면 CAD 이해 벤치마크)는 403 으로 열지 못해 넣지 않음",
      "Nav2 keepout 필터 문서는 docs.nav2.org·raw 경로 모두 404 로 열지 못해 넣지 않음",
      "대화만으로 로봇 지도를 만든 실제 현장 배치 사례(연구 프로토타입·시뮬레이션 데모 외)는 찾지 못함",
      "국내 언어 모델 기반 지도 작성 연구는 검색에서 확인되지 않음(국내 자료는 위상 지도 구축·다층 SLAM·벤더 정합 기능뿐)"
    ],
    "scope_violations": [
      "f18: 로봇 자체 SLAM·승강기 조작은 분류 원문 19장 '로봇 자체 지능·제어'·'시설·설비 제어' 연계 영역이므로 '연계 대상: '으로 표시함",
      "f22: 라이다 지도 생성·도면 해석은 연계 영역(로봇 자체 지능·제어, 14. 도면·BIM에서 지도 만들기·45. 문서·도면·장면 이해)이므로 '연계 대상: '으로 표시함",
      "f5·f6·f7: 건축 설계용 평면도 생성 연구는 로봇 지도 작성이 아니므로 방법 참고로만 제안함"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 신규 출처 15건(ref-815~ref-163) 상한 도달로 rmf_traffic_editor 저장소 README(같은 Open Robotics 계열), LLM-Geo 류 GIS 에이전트 연구, HouseLLM·HypergraphFormer 등 추가 평면도 생성 연구는 넣지 못했다. 검색 19회/30. 원문 열람 14건(webfetch 11, github_raw 3), 미열람 1건(ref-826). 교차 확인 1건(f9: Tell2Design·FloorplanQA 독립 출처). 모든 finding 신뢰도 medium 이하(대부분 단일 출처, 논문은 초록 확인). 분류 원문 핵심 질문(말·도면만으로 쓸 수 있는 지도)에는 f1·f3(언어→위상·의미 지도 가능), f16(CAD→로봇 지도 자동 생성), f8·f9(언어 모델의 기하 제약 미준수)로 답했으며 결론은 '위상·의미 요소는 가능하나 기하·축척은 사람 확인이나 별도 입력이 필요'라는 추정(f4·f21·f23)이다. 현장 유형: 병원(f13, 시뮬레이션 데모임을 명시), 제조 공장(f19, 벤더 주장), 실외(f17), 기타(f18)로 물류창고 사례는 없다. L. AI·학습 기술 관련 finding(f6·f8·f16·f24)은 45. 문서·도면·장면 이해와 적용 대상 14. 도면·BIM에서 지도 만들기 양쪽에 연결하도록 제안했다. 참고문헌 목록 입력이 이 페이지 인용분(0건)만 요약되어 전체 807건과의 URL 중복을 대조하지 못했으므로 Traffic Editor·rmf_demos 등은 퍼블리셔가 기존 id 로 합칠 수 있다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-29-01/verification.json

```json
{
  "run_id": "2026-09-29-01",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2403.10008 초록·HTML 본문 열람: 제목·저자·2024-03-15·ICRA 2024 일치. 'generating explicit maps achieves significantly higher accuracy than storing implicit maps in the LLMs' 및 'creates a map using only natural language information' 원문 확인. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2511.03165 열람: JSON 형식 위상 지도, 사람·기반 모델 공동 편집, 2단계(시각 기반 모델+운영자 → 자연어 질의 계획), 소형 로컬 모델 계획 가능 모두 초록에 있음. ICRA 2025 워크숍 채택 일치. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 브리프 URL(roboticsproceedings.org/rss09/p04)은 검증 중 연결 오류(ECONNRESET) 2회로 열지 못했으나 검색 결과의 기관·제목·URL 이 일치하고, 같은 논문의 MIT DSpace 사본(dspace.mit.edu/handle/1721.1/87051)에서 초록을 열어 'jointly estimates a hybrid metric, topological, and semantic representation' 과 자연어 포함 시 계량·위상·의미 정확도 향상 문장을 확인. RSS IX 2013-06 일치. 단일 출처."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f1·f2·f3 이 모두 살아남았고 세 논문 어느 것도 순수 언어에서 정확한 계량 기하를 얻는다고 주장하지 않으므로 추정으로 적절. 구축자 추정임을 본문에서 드러낼 것."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2311.15941 열람: 8만 건 이상 평면도·자연어 지시, 공간·관계 제약 만족이 난점, Seq2Seq 기준 모델, 텍스트 조건 이미지 생성 모델 비교, 사람 평가 모두 초록에 있음. ACL 2023(Area Chair Award). 발행일 '2023'은 arXiv 등록 2023-11-27 기준으로 유지 가능. 단일 출처. 건축 설계용 연구이므로 방법 참고로만."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2603.11640 열람: HouseMind, 방 단위 이산 토큰 통합 어휘, 이해·생성·편집 통합, 텍스트 지시 편집, 기하 타당성·제어 가능성 우위, 로컬 배포 가능 모두 초록에 있음. CVPR 2026 채택, 2026-03-12 일치. 우위 주장은 저자 보고값이므로 본문에서 '저자 보고'로 서술. 단일 출처."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2312.09067 초록·HTML 본문 열람: GPT-4 가 평면도·재질·출입구·창을 설계하고 객체 간 공간 관계 제약을 생성해 제약 최적화로 배치, Objaverse 자산, 주거 장면 사람 평가에서 절차적 기준선보다 선호, 신규 장면 내비게이션 확인. CVPR 2024, 2023-12-14(v2 2024-04-22). 단일 출처."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2507.07644 열람: JSON/XML 평면도, 거리·가시성·경로·배치 네 과제, 'often fail to respect physical constraints, preserve spatial coherence', 작은 변화에 강건 모두 초록에 있음. 최신성: v4 가 2026-05-25 에 개정되고 ICML 2026 채택으로 표시됨 — 본문 기준일에 버전·학회를 병기할 것. 단일 출처."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. Tell2Design(SUTD·NUS 등, 2023)과 FloorplanQA(KAUST 등, 2025)를 각각 열어 공간·관계 제약 만족의 어려움과 물리 제약 미준수를 확인. 발행 주체·저자가 다르고 인용 관계가 아니므로 독립 교차 확인 인정. 추정 태그 적절(도출 결론은 구축자 추정)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. traffic-editor.md 원문(github_raw) 열람: 레벨·벽(기본 10cm·2.5m)·꼭짓점 속성(충전소·주차·도킹)·플릿별 차선·문 4종(hinged·double-hinged·sliding·double-sliding)·다층 승강기·바닥 다각형·.building.yaml 저장 모두 일치. 발행일 미확인(확인일 기준) 표기 유지. 단일 출처(Open Robotics)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 인용 구절 'Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.' 원문과 일치. 측정선·거리 입력 방식 확인. 같은 출처 직접 인용은 이 1회만 허용."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f10·f11·f2 에서 도출한 추정이며 근거 finding 이 모두 살아남음. 대화로 빌딩 맵을 채운 사례를 직접 확인하지 않았다는 한계를 본문에 남길 것."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. rmf_demos README 원문(github_raw) 열람: Clinic World 'two levels and two lifts … Two different robot fleets with different roles navigate across two levels by lifts', Hotel World '2 guest levels … two lifts, multiple doors and 3 robot fleets (4 robots)' 일치. 시뮬레이션 데모이며 실제 현장 배치가 아님을 5절에서 반드시 명시. Hotel 은 상업 시설 사례로 나눌 수 있음."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. LIF README 원문(github_raw) 열람: 1.0.0(2023-09), 'edges, nodes and stations', 통합자가 제3자 관제에 레이아웃을 넘긴다는 문장, VDA5050 영향, 'non-binding approach' 모두 일치. 출처 유형이 '표준'이나 문서 스스로 비구속 가이드라인이라 하므로 본문에서 그렇게 표기."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f14·f10 이 살아남았고 두 형식의 공식 변환 규칙은 미확인이라는 한계가 열린 질문으로 올라가 있음. 추정 적절."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2507.00552 열람: CAD → 계층 위상·계량 OSM, 레이어 분리·AreaGraph 분할·글자–방 연결·다층 융합·GUI·코드 공개, SLAM 의 시간·노동·강건성 한계 주장 모두 초록에 있음. v3 2026-03-31 개정, 학회 표기 없음(기준일에 버전 병기). 단일 출처. 14. 도면·BIM에서 지도 만들기 쪽 내용이므로 이 페이지에서는 연계·참고로 다룰 것."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. DBpia 열람: 대한공간정보학회지 30권 2호(2022-06) 11–20쪽, 김영재·김세윤·김홍준(대전대). 공공 지도 데이터 기반 분기점 단위 전역 경로 계획용 위상 지도, A* 모의실험, 비용 절감·실외 서비스 상용화 촉진 모두 초록에 있음. 단일 출처."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. KCI 열람: 로봇학회 논문지 21권 1호 48–57쪽(2026), 노주형·강규리·김연찬·심현철(KAIST). 3D LiDAR–IMU SLAM, 프런티어 탐사(약 33% 단축), 4자유도 매니퓰레이터 승강기 버튼 조작, N1 건물 5F–9F 27분, 승강기 성공률 95% 모두 초록에 있음. 수치는 저자 보고값이며 단일 출처. '연계 대상' 표시 유지."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 모빌리오 페이지 열람(2026-08-24): 2D 라이다 지도(PGM)와 CAD/BIM 도면을 기준점 3개 이상(기둥·모서리)으로 좌표계 일치 후 회전각·크기 미세 조정, 웨이포인트 티칭 경로, 도면·구역 편집 기능 설명 없음 모두 일치. 벤더 주장·추정 표기 적절(vendor_claim: true). 용어는 용어집 '지도 정합(Map Alignment)'으로 맞추고 벤더 표기 '맵 정합'은 따옴표로."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 원문 미열람. ACM DL 은 403, DiVA 학위논문·Reviewerly 는 연결 오류로 열지 못함. 검색 결과에서 기관(ACM/IEEE HRI 2022)·제목·저자(Doğan·Torre·Leite)·URL·461–469쪽·2022-03-07 일치와 '63명 사용자 연구'는 확인했으나, 명확화 질문을 받은 사용자가 과제를 더 쉽게 느끼고 로봇의 이해·역량을 더 높게 평가했다는 효과 결론은 어느 스니펫에서도 나타나지 않았다. 스니펫 범위 밖 주장이므로 8절 3항에 따라 강등하고 각주에 (원문 미열람) 표기."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f11(축척 입력 방식)은 원문으로 확인, f20 은 추정으로 강등됨. 추정 태그 유지하되 본문에서 f20 의 효과 결론이 원문 미확인임을 함께 밝힐 것."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f16·f18·f19 가 모두 살아남았고 분류 원문 19장 경계와 C 대분류 주석(맵 작성은 14·15번의 기능을 대화로 쓰게 하는 것)에 맞는 추정. '연계 대상' 표시 유지."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 근거 finding(f10·f14·f2·f8) 모두 살아남음. 원문 19장 경계와 '사람이 확인·승인한 계획만 실행' 주석에 맞는 구축자 추정으로 9절에 적절."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. f6·f8·f16 이 도면·평면도 해석 연구이고 분류 원문 L 주석이 도면 해석을 14번 적용 연구 방법으로 두므로 교차 규칙 적용이 맞음. 10절에서 45. 문서·도면·장면 이해와 14. 도면·BIM에서 지도 만들기 양쪽에 연결."
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
      "ref-079(Traffic Editor)·ref-104(rmf_demos)는 이전 실행들이 같은 Open Robotics 계열 문서(rmf-core, integration_doors 등)를 이미 등록했으므로 참고문헌 전체 목록에 같은 URL 이 있으면 퍼블리셔가 기존 id 로 합친다(이번 입력에는 인용 0건만 요약되어 대조하지 못함)",
      "용어 후보 '명확화 질문'은 기존 용어 '명시적 확인·암시적 확인(explicit-implicit-confirmation)'·'슬롯 채우기(slot-filling)'와 뜻이 겹치지 않으나 인접하므로 정의에 관계를 적고 등록"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f19 '맵 정합' — 용어집 '지도 정합 (Map Alignment)'과 표기가 다름. 본문은 용어집 표기를 쓰고 벤더 명칭은 따옴표로 병기",
      "f14·f15 '레이아웃 교환 형식(LIF)'은 용어집 'layout-interchange-format' 과 일치 — 신규 등록하지 않고 링크",
      "f1·f17 '위상 지도'는 용어집 'topological-map' 과 일치 — 링크 재사용"
    ]
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f20: [사실] → [추정]으로 강등하고, 본문에서는 '63명 사용자 연구'까지만 확인된 사실로 두고 효과 결론(과제가 쉽게 느껴짐·로봇 역량 평가 상승)은 원문 미확인으로 서술한다 — ACM 원문을 열지 못했고 검색 스니펫에 효과 결론이 없다.",
    "ref-826: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다 — 원문 403.",
    "f21: 추정을 유지하되 근거 문장에서 f20 의 효과 결론이 원문 미확인임을 밝힌다 — f20 강등에 따른 정합.",
    "f19: 용어를 용어집 '지도 정합(Map Alignment)'으로 쓰고 벤더 표기 '맵 정합'은 따옴표 병기하며, [추정]에 '벤더 주장'을 유지하고 5절 제조 공장 사례임을 명시한다 — 단일 벤더 문서.",
    "f13: 5절 병원 사례는 Open-RMF Clinic 시뮬레이션 데모 월드임을 문장에 명시하고 실제 병원 배치 사례처럼 쓰지 않는다. Hotel 월드를 쓰면 상업 시설 사례로 따로 나눈다 — 출처가 시뮬레이션 데모 README.",
    "f18: 5절(기타 현장)·9절에서 '연계 대상'으로 짧게만 다루고 ROP 직접 범위처럼 쓰지 않는다 — 로봇 자체 SLAM·승강기 조작은 분류 원문 19장의 로봇 자체 지능·제어·시설·설비 제어 영역.",
    "f5·f6·f7: 6·8절에서 건축 설계용 평면도 생성 연구임을 밝히고 로봇 지도 작성 방법의 참고로만 서술하며, f6 의 '기하 타당성·제어 가능성 우위'는 저자 보고값으로 표기한다 — 로봇 지도 작성이 아닌 대상.",
    "f8·f16: 기준일에 arXiv 개정 버전을 병기한다(FloorplanQA v4 2026-05-25, ICML 2026 채택 / Zhang 외 v3 2026-03-31) — 발행일 이후 개정판 존재.",
    "f14: 7절에서 VDMA LIF 를 표준이 아니라 '법적 구속력 없는 VDMA 가이드라인'으로 표기한다 — README 가 non-binding approach 로 명시.",
    "f16·f24: 10절에서 14. 도면·BIM에서 지도 만들기와 45. 문서·도면·장면 이해 양쪽에 연결하고, 이 페이지 6절에는 도면 해석 엔진을 연계 대상으로만 둔다 — 원문 L 대분류 교차 규칙.",
    "f11: Traffic Editor 직접 인용은 이 구절 1회만 쓰고 f10 은 요약·재서술한다 — 출처당 직접 인용 1회.",
    "용어집: '레이아웃 교환 형식(LIF)'·'위상 지도'·'지도 정합'은 기존 용어(layout-interchange-format, topological-map, map-alignment)에 링크하고 신규 등록하지 않는다. '명확화 질문' 정의에는 '명시적 확인·암시적 확인'·'슬롯 채우기'와의 관계를 한 문장 더한다 — 용어 중복 방지.",
    "ref-079·ref-104: reference_updates 에서 참고문헌 전체 목록에 같은 URL 이 이미 있으면 기존 id 를 재사용한다 — 이번 입력에 전체 목록이 없어 대조하지 못함."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 23건, 미확인 1건, 교차 확인 1건(f9). 강등: f20 사실 → 추정(효과 결론이 검색 스니펫에 없음). 원문 미열람 출처: ref-826(ACM 403). 주의: ref-819 는 브리프 URL(roboticsproceedings.org)이 검증 중 연결 오류로 열리지 않아 MIT DSpace 사본으로 초록을 확인했다. 나머지 13건은 원문(arXiv 초록·HTML, github_raw, DBpia, KCI, 벤더 페이지)을 열어 기관·제목·발행일·주장 일치를 확인했다. 사실 태그 finding 은 모두 단일 출처이며 논문은 초록·본문 일부만 확인했으므로 페이지 신뢰도는 medium 이다. 대화만으로 로봇 지도를 만든 실제 현장 배치 사례는 없고, 병원 사례는 Open-RMF 시뮬레이션 데모, 제조 공장 사례는 벤더 주장이다. f8·f16 은 발행 후 arXiv 개정판(2026)이 있어 기준일에 버전을 병기한다. 정정 요청 없음. 미사용 출처 없음.",
  "retry_reason": null
}
```

### runs/2026-09-29-01/pages.json

```json
{
  "run_id": "2026-09-29-01",
  "outline": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "대화로 만든 지도는 위상·의미 요소에 강점이 있으나 층·구역·통로·문 배치를 언어 모델 출력 그대로 쓰면 공간·물리 제약이 어긋날 수 있어 검증·사람 확인이 필요하다. [추정][^ref-817][^ref-822] 축척은 사람이 거리를 넣어야 정해진다. [사실][^ref-079]",
      "planned_findings": [
        "f9",
        "f16",
        "f11"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 800,
      "summary": "위상 지도·의미 지도·빌딩 맵·레이아웃 교환 형식·축척 보정·명확화 질문·지도 정합·공동 편집 텍스트 지도를 정의한다. [사실][^ref-815][^ref-079][^ref-046]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f10",
        "f11",
        "f14",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1300,
      "summary": "병원(Open-RMF Clinic 시뮬레이션 데모)·제조 공장(벤더 주장 지도 정합)·실외(공공 지도 기반 위상 지도) 사례를 여섯 항목으로 쓰고 기타 현장의 다층 자율 지도화는 연계 대상으로만 둔다. [사실][^ref-104][^ref-820]",
      "planned_findings": [
        "f13",
        "f19",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1000,
      "summary": "언어→위상·의미 지도, 사람·모델 공동 편집 텍스트 지도, 건축 설계용 평면도 생성(방법 참고), 공간 제약 검증과 확인 질문, 연계 대상인 도면 해석·SLAM 엔진을 정리한다. [사실][^ref-815][^ref-816][^ref-819]",
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
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 450,
      "summary": "Open-RMF Traffic Editor·rmf_demos·VDMA LIF(법적 구속력 없는 가이드라인)·VDA 5050 을 표로 정리한다. [사실][^ref-079][^ref-046]",
      "planned_findings": [
        "f10",
        "f11",
        "f13",
        "f14",
        "f15"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "언어→지도 연구 3건, 평면도 생성·편집·추론 연구 4건, CAD→지도 1건, 국내 연구 2건을 요약한다. [사실][^ref-815][^ref-820][^ref-163]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f5",
        "f6",
        "f7",
        "f8",
        "f16",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 600,
      "summary": "ROP 는 대화에서 구조화 지도 요소를 만들고 확인 질문·사람 승인으로 확정하며, 기하 지도 생성(SLAM)·도면 해석·승강기 제어는 연계 대상이다. [추정][^ref-079][^ref-046][^ref-816][^ref-822]",
      "planned_findings": [
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 550,
      "summary": "짝 엔진 14·15번, 16번, 교차 규칙에 따른 45번, 13번, 20·21·22번과 두 트랙에 연결한다. [추정][^ref-083][^ref-823]",
      "planned_findings": [
        "f16",
        "f24",
        "f10",
        "f14",
        "f15",
        "f2",
        "f3",
        "f9",
        "f20",
        "f21",
        "f13"
      ]
    },
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "section": "11. 열린 질문",
      "budget_chars": 400,
      "summary": "공통 중간 표현·변환 규칙, 대화 지도 작성 평가 지표, 정합 결과의 확인·승인 주체에 관한 새 질문 3건을 올린다.",
      "planned_findings": [
        "f15",
        "f9",
        "f22"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "3~11절 신규 작성(seed → draft), 출처 15건, 열린 질문 3건, 현장 유형 사례 3건(병원·제조 공장·실외). 2차 재검증 수정 지시 이행: 10절 14. 도면·BIM에서 지도 만들기 항목을 사실 문장과 추정 문장으로 나눔(태그 상향 해소)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"6. 대표 접근법과 기술\" 절(1,767자)을 옮겼다(2차 재검증에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"4. 핵심 개념과 용어\" 절(1,091자)을 옮겼다(2차 재검증에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"8. 대표 연구와 자료\" 절(979자)을 옮겼다(2차 재검증에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"3. 왜 중요한가\" 절(742자)을 옮겼다. 2차 재검증 수정: 3절의 태그 없는 판단 문장 2건에 [추정]·[의견] 태그와 각주를 붙이고 sources·출처에 ref-815·ref-816·ref-819 추가"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(690자)을 옮겼다(2차 재검증에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(618자)을 옮겼다. 2차 재검증 수정: 14. 도면·BIM에서 지도 만들기 항목을 사실·추정 문장으로 나누고 15. 지도·공간·위치 모델 항목 태그를 [추정]으로 바꿈"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area08-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 8. 채팅으로 맵 작성 의 \"11. 열린 질문\" 절(589자)을 옮겼다(2차 재검증에서 변경 없음)"
    }
  ],
  "changelog_entry": "2026-09-29 | 8. 채팅으로 맵 작성 | 3~11절 신규 작성(seed → draft), 출처 15건, 현장 유형 사례 3건, 열린 질문 3건, 2차 재검증 수정 지시 3건 반영(10절 태그 상향 2건 되돌림, 3절 판단 문장 태그) | run 2026-09-29-01",
  "index_updates": {
    "home_recent": "2026-09-29 — 8. 채팅으로 맵 작성: 3~11절 신규 작성. 언어→위상·의미 지도 연구, Open-RMF 빌딩 맵·VDMA LIF 형식, 축척·통과 조건은 확인 질문으로 받는 원칙 정리",
    "category_recent": "2026-09-29 — 8. 채팅으로 맵 작성: 3~11절 신규 작성(초안). 병원(시뮬레이션 데모)·제조 공장(벤더 주장)·실외 사례, 열린 질문 3건",
    "area_recent": "2026-09-29 — 8. 채팅으로 맵 작성: 실행 2026-09-29-01 에서 3~11절 신규 작성. 출처 15건(ref-815~ref-163), 신뢰도 medium"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "traffic-editor",
      "term_ko": "트래픽 에디터",
      "term_en": "Traffic Editor (Open-RMF)",
      "definition": "2D 평면도 이미지 위에 층·벽·꼭짓점·플릿별 차선·문·승강기를 그려 제조사 중립 빌딩 맵(.building.yaml)을 만드는 Open-RMF 의 GUI 편집 도구이다.",
      "description": "층의 축척은 실제 거리를 아는 두 점 사이에 측정선을 긋고 물리 거리를 미터로 입력해 정한다. 꼭짓점에 충전소·주차·도킹 속성을 줄 수 있고 문은 여닫이·양여닫이·미닫이·양미닫이 4종이다.",
      "related_areas": [
        8,
        15,
        22
      ],
      "sources": [
        "ref-079"
      ]
    },
    {
      "action": "new",
      "slug": "language-guided-floor-plan-generation",
      "term_ko": "언어 유도 평면도 생성",
      "term_en": "Language-guided Floor Plan Generation",
      "definition": "방 종류·위치·크기·관계를 적은 자연어 설명에서 공간·관계 제약을 만족하는 평면도를 생성하는 과제이다.",
      "description": "건축 설계용 과제로 제안되었으며(Tell2Design, ACL 2023), 예술적 이미지 생성과 달리 공간·관계 제약을 만족해야 하는 점이 핵심 난점이다. 로봇 지도 작성에서는 방법의 참고로만 쓴다.",
      "related_areas": [
        8,
        14,
        45
      ],
      "sources": [
        "ref-817",
        "ref-823"
      ]
    },
    {
      "action": "new",
      "slug": "clarification-question",
      "term_ko": "명확화 질문",
      "term_en": "Clarification Question (Follow-up Clarification)",
      "definition": "요청이 모호할 때 시스템이 아는 정보를 바탕으로 사용자에게 되묻는 질문으로, 확정할 수 없는 값을 추정으로 채우지 않고 사람에게 확인받는 대화 장치이다.",
      "description": "명시적 확인·암시적 확인이 이미 해석한 값을 사용자에게 되짚어 확인받는 장치이고 슬롯 채우기가 빠진 값을 차례로 묻는 절차라면, 명확화 질문은 해석이 여러 갈래로 갈리는 지점에서 갈래를 좁히기 위해 되묻는 질문이라는 점에서 인접하되 구분된다. 로봇 대화에서 63명 사용자 연구로 평가한 연구(HRI 2022)가 있으나 효과 결론은 원문 미열람으로 확인하지 못했다.",
      "related_areas": [
        8,
        13
      ],
      "sources": [
        "ref-826"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-815",
      "org": "Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs)",
      "title": "Language to Map: Topological map generation from natural language path instructions",
      "published": "2024-03-15",
      "url": "https://arxiv.org/abs/2403.10008",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 경로 지시문을 언어 모델로 노드·에지·행동의 명시적 위상 지도로 바꾸는 방법. 암묵적 지도보다 정확도가 높음. ICRA 2024.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-816",
      "org": "Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K.",
      "title": "SENT Map -- Semantically Enhanced Topological Maps with Foundation Models",
      "published": "2025-11-05",
      "url": "https://arxiv.org/abs/2511.03165",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "사람과 기반 모델이 함께 읽고 고치는 JSON 위상 지도 표현. 운영자와 시각 기반 모델이 짝지어 지도를 만들고 자연어 질의로 계획. ICRA 2025 워크숍.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-817",
      "org": "Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W.",
      "title": "Tell2Design: A Dataset for Language-Guided Floor Plan Generation",
      "published": "2023",
      "url": "https://arxiv.org/abs/2311.15941",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "자연어 지시와 짝지은 8만 건 이상 평면도 데이터셋과 Seq2Seq 기준 모델. 공간·관계 제약 만족이 핵심 난점. ACL 2023.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 빌딩 맵 편집기 설명: 레벨·벽·꼭짓점·차선·문·승강기·바닥 요소, 측정선으로 축척 설정, .building.yaml 저장. 참고문헌 전체 목록에 같은 URL 이 있으면 기존 id 로 합친다.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-819",
      "org": "Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX)",
      "title": "Learning Semantic Maps from Natural Language Descriptions",
      "published": "2013-06",
      "url": "https://www.roboticsproceedings.org/rss09/p04.html",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "말로 된 장소 설명과 센서 관측을 결합해 계량·위상·의미 지도를 공동 추정하는 의미 그래프 방법. 자연어 포함 시 정확도 향상. 검증은 MIT DSpace 사본으로 초록을 확인.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-820",
      "org": "김영재, 김세윤, 김홍준 (대한공간정보학회지)",
      "title": "공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구",
      "published": "2022-06",
      "url": "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "공공 지도 서비스 데이터로 실외 이동 로봇의 분기점 단위 위상 지도를 구축하고 A* 모의실험으로 검증한 국내 논문.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-046",
      "org": "VDMA (Intralogistics-2X-LIF GitHub)",
      "title": "Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA)",
      "published": "2023-09",
      "url": "https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "VDMA 레이아웃 교환 형식 1.0.0 공식 저장소 README. 통합자가 노드·에지·스테이션 레이아웃을 제3자 관제에 넘기는 형식, VDA 5050 영향. 문서 스스로 법적 구속력 없는 가이드라인이라 밝힘.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-822",
      "org": "Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P.",
      "title": "FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations",
      "published": "2025-07-10",
      "url": "https://arxiv.org/abs/2507.07644",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "JSON·XML 평면도에 대한 거리·가시성·경로·배치 질문 벤치마크. 언어 모델이 물리 제약과 공간 일관성을 자주 어김. arXiv v4 2026-05-25 개정, ICML 2026 채택.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-823",
      "org": "Qin, S., Weber, R. E., & Lu, X.",
      "title": "Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans",
      "published": "2026-03-12",
      "url": "https://arxiv.org/abs/2603.11640",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "방 단위 토큰으로 멀티모달 언어 모델이 평면도를 이해·생성·텍스트 지시로 편집하는 HouseMind. CVPR 2026.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — README (Demonstrations of Open-RMF)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "Open-RMF 공식 데모 월드 목록: Hotel(2층·승강기 2대·문·플릿 3개), Office, Airport Terminal, Clinic(2층·승강기 2대·플릿 2개), Campus, Manufacturing & Logistics. 참고문헌 전체 목록에 같은 URL 이 있으면 기존 id 로 합친다.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-825",
      "org": "Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등)",
      "title": "Holodeck: Language Guided Generation of 3D Embodied AI Environments",
      "published": "2023-12-14",
      "url": "https://arxiv.org/abs/2312.09067",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "텍스트 설명에서 GPT-4 가 평면도·출입구·창을 설계하고 공간 관계 제약 최적화로 3D 실내 환경을 생성. 사람 평가에서 절차적 기준선보다 선호. CVPR 2024.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-826",
      "org": "Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022)",
      "title": "Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation",
      "published": "2022-03",
      "url": "https://dl.acm.org/doi/10.5555/3523760.3523822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 모호한 요청에 로봇이 후속 명확화 질문을 하는 시스템의 63명 사용자 연구. 효과 결론(과제가 쉽게 느껴짐·로봇 역량 평가 상승)은 검색 스니펫에서 확인되지 않아 추정으로 둠.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-827",
      "org": "모빌리오(Mobilio)",
      "title": "[최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법",
      "published": "2026-08-24",
      "url": "https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "국내 업체의 공장 순찰 로봇 관제 소개. 2D 라이다 지도와 CAD·BIM 도면을 기준점 3개 이상으로 정합하는 '맵 정합' 기능을 주장(벤더 주장).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-083",
      "org": "Zhang, J., Wu, S., Ma, X., & Schwertfeger, S.",
      "title": "Generation of Indoor Open Street Maps for Robot Navigation from CAD Files",
      "published": "2025-07-01",
      "url": "https://arxiv.org/abs/2507.00552",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "건축 CAD 파일에서 레이어 분리·AreaGraph 분할·글자–방 연결·다층 융합으로 로봇용 계층 위상·계량 OSM 지도를 자동 생성. GUI·코드 공개. arXiv v3 2026-03-31 개정.",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-163",
      "org": "노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지)",
      "title": "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템",
      "published": "2026",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "3D 라이다·IMU SLAM 과 프런티어 탐사, 매니퓰레이터 승강기 버튼 조작으로 다층 실내 지도를 자동 구축. KAIST N1 5개 층 27분, 승강기 성공률 95%(저자 보고값).",
      "cited_by": [
        "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가?",
      "areas": [
        8,
        15,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가?",
      "areas": [
        8,
        13
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가?",
      "areas": [
        8,
        14,
        55
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "제조 공장",
      "item": "완료·인계",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "실외",
      "item": "완료·인계",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시",
      "title": "8. 채팅으로 맵 작성"
    }
  ],
  "additional_research_requests": [
    "5절·6절: 대화만으로 로봇용 빌딩 맵·레이아웃을 채운 실제 현장 배치 사례(연구 프로토타입·시뮬레이션 데모 외)가 없어 병원 사례를 설명용으로 썼다. 실제 도입 사례가 필요하다.",
    "4절·7절: VDMA LIF 의 JSON 구조 세부(층·지도 id 필드, 스테이션 속성)가 미확인이라 빌딩 맵과의 요소 대응을 쓰지 못했다. 공식 가이드라인 PDF 원문 확인이 필요하다.",
    "4절·6절: 명확화 질문 연구(ref-826)의 효과 결론이 원문 미열람으로 추정에 머물렀다. ACM 원문 또는 저자 공개본(DiVA 등)으로 재확인이 필요하다.",
    "6절: 지도 작성 대화에 특화된 확인 질문·모호성 해소 연구와 언어 모델 기반 지도 작성의 국내 연구가 없어 열린 질문으로만 두었다.",
    "7절: Nav2 keepout 필터 문서(금지 구역 지도 요소)와 rmf_traffic_editor 저장소 README 는 이번 조사에서 열지 못해 표에 넣지 못했다.",
    "5절: 병원 사례의 예외·성과 항목과 제조 공장 사례의 예외·성과 항목을 채울 처리량·시간·비용 근거가 없어 미확인으로 두었다.",
    "7절: VDA 5050 의 노드·에지 개념이 LIF 노드·에지의 기원인지는 브리프에 근거가 없어 2차 지시대로 삭제했다. VDA 5050 원문(노드·에지 정의)과 LIF 가이드라인의 관계를 확인하면 7절 표와 10절 21. 상호운용 표준·적합성 연결에 반영할 수 있다.",
    "10절: CAD 도면 변환 결과(Zhang 외)가 실제로 채팅 맵 작성의 입력으로 쓰인 사례가 브리프에 없어 '입력이 된다'는 역할 판단을 추정으로만 두었다. 도면 변환 → 대화 편집 → 플릿 지도 형식으로 이어진 실제 파이프라인 사례가 있으면 사실로 올릴 수 있다."
  ],
  "fixes_applied": [
    "f20 강등 — 4절 명확화 질문 항목과 6절 확인 질문 단락을 [추정][^ref-826]으로 쓰고, '63명 사용자 연구'까지만 확인된 것으로 두고 효과 결론(과제가 쉽게 느껴짐·로봇 역량 평가 상승)은 원문을 열지 못해 확인하지 못했다고 서술했다.",
    "ref-826 원문 미열람 표기 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-826 항목에 source_unopened: true 를 넣었다.",
    "f21 정합 — 6절 '공간 제약 검증과 확인 질문' 단락에서 추정을 유지하되 '명확화 질문의 효과 결론은 원문 미확인'임을 근거 문장에 밝혔다.",
    "f19 용어·표기 — 4절과 5절 제조 공장 사례에서 용어집 '지도 정합(Map Alignment)'을 링크해 쓰고 벤더 표기는 '맵 정합'으로 따옴표 병기했으며, 모든 문장에 [추정] 벤더 주장[^ref-827]을 유지하고 현장 유형을 제조 공장으로 명시했다.",
    "f13 시뮬레이션 명시 — 5절 병원 사례 첫 문장에 Open-RMF Clinic 시뮬레이션 데모 월드 기반 설명용 사례이며 실제 병원 배치 사례가 아님을 명시했다. Hotel 월드는 별도 사례로 쓰지 않고 7절 rmf_demos 행에서 데모 예시로만 언급했다.",
    "f18 연계 대상 — 5절 끝에 '기타 현장의 연계 대상 사례' 단락으로 짧게만 다루고(여섯 항목 표·매트릭스 칸 없음), 9절에서도 로봇 자체 지능·제어 몫으로만 언급해 ROP 직접 범위처럼 쓰지 않았다.",
    "f5·f6·f7 참고 표기 — 6절 소제목을 '언어 모델의 평면도 생성·편집(건축 설계용, 방법 참고)'으로 두고 첫 문장에서 로봇 지도 작성이 아닌 건축 설계용임을 밝혔으며, 8절에서도 '건축 설계용'을 적고 f6 의 기하 타당성·제어 가능성 우위는 '저자 보고값'으로 표기했다.",
    "f8·f16 개정 버전 병기 — FloorplanQA 는 3·6·8절에서 '2025년 7월 초판, v4 2026-05-25 개정, ICML 2026 채택'으로, Zhang 외는 3·8절에서 'v3 2026-03-31 개정'으로 기준일에 병기했다.",
    "f14 LIF 표기 — 4절 정의와 7절 표의 유형 칸에서 표준이 아니라 '법적 구속력 없는 VDMA 가이드라인'으로 표기하고 유형은 프레임워크로 두었다.",
    "f16·f24 교차 연결 — 10절에서 14. 도면·BIM에서 지도 만들기와 45. 문서·도면·장면 이해 양쪽에 연결하고, 6절에는 '연계 대상: 도면 해석·SLAM 엔진' 소제목으로 도면 해석 엔진을 연계 대상으로만 두었다.",
    "f11 직접 인용 1회 — 브리프의 Traffic Editor 직접 인용 구절은 본문에 옮기지 않고 f10·f11 모두 요약·재서술했으므로 ref-079 직접 인용은 0회다(출처당 1회 상한 안).",
    "용어집 — '레이아웃 교환 형식(LIF)'·'위상 지도'·'지도 정합'은 기존 용어(layout-interchange-format, topological-map, map-alignment)에 링크만 하고 신규 등록하지 않았으며, '명확화 질문' 항목의 description 에 명시적 확인·암시적 확인·슬롯 채우기와의 관계를 한 문장 더했다.",
    "ref-079·ref-104 id 재사용 — 참고문헌 전체 목록이 입력에 없어 대조하지 못했으므로 브리프 id 그대로 넣고 reference_updates 의 두 항목 summary 에 '같은 URL 이 있으면 기존 id 로 합친다'를 적어 퍼블리셔 병합에 맡겼다.",
    "2차: 6절 '연계 대상: 도면 해석·SLAM 엔진' 단락 — 문장 중간의 '[사실][^ref-083]과'·'[사실][^ref-163]은' 표기를 없애고 한 문장으로 다시 써서 끝에 '…이 위키의 추정이다. [추정][^ref-083][^ref-163]' 을 두었다(f22 처분과 일치).",
    "2차: 7절 표 VDA 5050 행 — '노드·에지 개념의 근원' 구절을 지우고 'LIF 정의에 영향을 준 무인운반차 인터페이스. [사실]' 까지만 남겼으며, 삭제한 관계는 additional_research_requests 에 조사 요청으로 적었다.",
    "2차: 10절 22. 설비·건물 시스템 연동 항목과 16. 장소 의미·지도 관리 항목 — 문장 끝 [사실] 을 [추정] 으로 바꿨다(각주 [^ref-104], [^ref-816][^ref-819] 유지).",
    "2차: 6절 평면도 생성·편집 단락 끝 문장 — '이 위키의 의견으로, 제약을 먼저 뽑고 최적화로 배치하는 구조는 지도 요소 배치에도 참고할 만하다. [의견][^ref-825]' 로 고쳐 태그와 각주를 붙였다.",
    "2차: 8절 첫 항목(Deguchi 외) — 첫 문장 끝에 [사실][^ref-815] 을 두고 '언어만으로 위상 지도가 가능함을 보인 직접 근거다.' 를 그 뒤에 이었다. 자동 분리로 첫 문장만 남아도 태그·각주가 남는다.",
    "2차: 5절 제조 공장 사례 — 표 앞 첫 문장에 '모빌리오가 \"맵 정합\"이라 부르는 [지도 정합(Map Alignment)](../../glossary/map-alignment.md) 기능' 으로 용어집 링크와 벤더 표기 따옴표 병기를 넣고 [추정] 벤더 주장[^ref-827] 을 붙였다. 1차 f19 항목이 이제 4절·5절 모두에서 이행된다.",
    "2차: SLAM·IMU·PGM 풀이 — 세부영역 페이지에 남는 5절에서 처음 나오는 자리(제조 공장 표 시작 조건 칸의 PGM·BIM, 기타 현장 단락의 IMU·SLAM)에 영문 전체 이름과 풀이를 적고, 9절 표의 '라이다 SLAM' 과 6절 연계 대상 단락에도 풀이를 병기했다. 9절 본문의 PGM 은 'PGM 형식 지도' 로 적어 5절 풀이를 따른다.",
    "2차(재검증): 10절 14. 도면·BIM에서 지도 만들기 항목 — 세부영역 페이지 10절 첫 항목과 분리 페이지 2026-09-29-area08-s10.md 의 1절 첫 항목·3절 첫 항목 세 곳 모두 'CAD 파일에서 로봇 지도를 자동 생성하는 연구가 있다. [사실][^ref-083] 그 결과가 이 영역의 입력이 된다는 것은 이 위키의 추정이다. [추정][^ref-083]' 으로 사실 문장과 추정 문장으로 나눴다(f22·f24 처분과 일치).",
    "2차(재검증): 10절 15. 지도·공간·위치 모델 항목 — 분리 페이지 2026-09-29-area08-s10.md 3절 두 번째 항목을 '…요소가 대화 결과를 담는 모델이라는 것이 이 위키의 추정이다. [추정][^ref-079][^ref-046]' 으로 바꿨다(f15·f23 처분과 일치).",
    "2차(재검증): 3절 판단 문장 — 분리 페이지 2026-09-29-area08-s3.md 3절에서 (a) '2절의 핵심 질문에 대한 현재 답은 …에 가깝다' 를 '…에 가깝다는 것이 이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819]' 로, (b) '말로도 그림으로도 확정할 수 없는 값을 … 핵심 설계 문제다' 를 '이 위키의 의견으로, … 핵심 설계 문제다. [의견][^ref-079]' 로 고쳤다. 새 각주 ref-815·ref-816·ref-819 를 그 페이지 8절 출처와 프런트매터 sources 에 더했다. 세부영역 페이지 3절 요약과 분리 페이지 1절 요약에는 이 두 문장이 없어 손대지 않았다.",
    "분량 초과 자동 분리: 8. 채팅으로 맵 작성 본문 9,590자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,577자"
  ]
}
```

### runs/2026-09-29-01/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-29-01/pages/categories/chat-based-configuration-and-operation/chat-map-authoring.md

```markdown
---
title: "8. 채팅으로 맵 작성"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [위상 지도, 빌딩 맵, 레이아웃 교환 형식, 축척 보정, 명확화 질문, 언어 모델 평면도]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-815, ref-816, ref-817, ref-079, ref-819, ref-820, ref-046, ref-822, ref-823, ref-104, ref-825, ref-826, ref-827, ref-083, ref-163]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 8. 채팅으로 맵 작성

# 8. 채팅으로 맵 작성

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 맵 작성**: 공간을 글이나 말로 설명하거나 도면·사진을 올리면 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다
- **대화 중 지도 확인·확정**: 대화로 만든 지도를 화면에 보여 주고, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 확인 질문으로 받아 확정한다

## 2. 핵심 질문

공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]

## 3. 왜 중요한가

대화로 만든 층·구역·통로·문 배치는 언어 모델 출력 그대로 쓰지 말고 기하 검증기나 사람 확인을 거쳐야 한다는 것이 이 위키의 추정이다. [추정][^ref-817][^ref-822] 건축 설계용 언어 유도 평면도 생성 데이터셋 연구(2023)와 구조화 텍스트 평면도에 대한 공간 추론 벤치마크(2025년 7월 초판, arXiv v4 2026-05-25 개정, ICML 2026 채택)가 서로 독립적으로 언어 모델의 공간·물리 제약 준수를 핵심 난점으로 지목했다.

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 왜 중요한가](../../topics/2026/2026-09-29-area08-s3.md)에 있다.

## 4. 핵심 개념과 용어

**[위상 지도(Topological Map)](../../glossary/topological-map.md)** — 장소를 노드, 연결을 에지로 표현한 지도. 기하 지도나 카메라 없이 자연어 경로 지시문만으로 노드·에지·행동의 위상 지도를 만드는 방법이 제안되었다. [사실][^ref-815]

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area08-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 병원

**사례:** 두 층과 승강기 2대를 둔 클리닉의 빌딩 맵을 대화로 채우고 확인하기

다음은 Open-RMF 공식 데모의 Clinic 시뮬레이션 월드를 바탕으로 한 설명용 사례이며, 실제 병원에 배치된 사례가 아니다. Clinic 월드는 두 층과 승강기 2대, 역할이 다른 로봇 플릿 2개를 두고 로봇이 승강기로 층을 오가는 시뮬레이션 빌딩 맵이다. [사실][^ref-104]

| 항목 | 내용 |
|---|---|
| 시작 조건 | 시설 담당자가 두 층의 평면도 이미지를 올리고 승강기 2대로 층을 잇고 플릿마다 다니는 통로를 나눠 달라고 요청한다(설명용) |
| 작업 대상 | 층 2개, 승강기 2대, 문, 플릿별 차선, 충전·주차 속성을 가진 꼭짓점 같은 빌딩 맵 요소. [사실][^ref-079] |
| 수행 자원 | 대화 기능이 층·승강기·차선 요소를 만들고 담당자가 화면에서 확인·승인한다. 승강기의 실제 제어는 연계 대상이다(설명용) |
| 제약 | 축척은 실제 거리를 아는 두 점의 미터 값을 사람이 넣어야 정해진다. [사실][^ref-079] 감염 관리 구역 같은 통과 조건은 확인 질문으로 받는다(설명용) |
| 완료·인계 | 사람이 확인·승인한 빌딩 맵(.building.yaml)이 플릿 어댑터로 넘어갈 때 완료로 본다는 것이 이 위키의 추정이다. [추정][^ref-079][^ref-046] |
| 예외·성과 | 미확인(데모에는 성과 수치가 없다) |

이 사례에서 이 영역이 관여하는 항목은 작업 대상(지도 요소 생성)과 제약·완료·인계(확정할 수 없는 값의 확인 질문과 사람 승인)다. 대화만으로 빌딩 맵을 채운 사례를 직접 확인한 것은 아니다.

**현장 유형:** 제조 공장

**사례:** 순찰 로봇의 라이다 지도와 공장 도면을 정합해 관제 지도로 쓰기

이 사례는 국내 업체 모빌리오가 '맵 정합'이라 부르는 [지도 정합(Map Alignment)](../../glossary/map-alignment.md) 기능에 관한 것으로, 단일 벤더 문서(2026-08-24)에 근거한 벤더 주장이며 독립 출처로 교차 확인되지 않았다. [추정] 벤더 주장[^ref-827]

| 항목 | 내용 |
|---|---|
| 시작 조건 | 공장 순찰 로봇 도입 시 라이다로 만든 2D 지도(PGM, Portable Gray Map 형식의 점유 격자 이미지)와 CAD·BIM(Building Information Modeling, 건물 정보 모델링) 도면을 한 화면에서 쓰려는 요구. [추정] 벤더 주장[^ref-827] |
| 작업 대상 | 라이다 지도, CAD·BIM 도면, 기둥·모서리 같은 기준점 3개 이상. [추정] 벤더 주장[^ref-827] |
| 수행 자원 | 운영자가 관제 화면에서 기준점을 지정하고 회전각·크기를 미세 조정하며, 경로는 웨이포인트 티칭으로 만든다. [추정] 벤더 주장[^ref-827] |
| 제약 | 기준점 3개 이상으로 좌표계를 맞춰야 하며, 도면 자체나 구역을 편집하는 기능은 설명되지 않았다. [추정] 벤더 주장[^ref-827] |
| 완료·인계 | 두 지도가 1:1 로 정합된 상태를 완료로 본다. [추정] 벤더 주장[^ref-827] |
| 예외·성과 | 미확인 |

대화가 아닌 화면 조작이지만, 채팅 맵 작성이 받는 도면·라이다 지도 입력의 정합 결과를 누가 확인하는지를 보여 주는 국내 제조 공장 사례다.

**현장 유형:** 실외

**사례:** 공공 지도 데이터로 실외 이동 로봇의 전역 경로 계획용 위상 지도 만들기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 실외 로봇 서비스에 필요한 전역 경로 계획용 지도를 새로 구축해야 하는 상황. [사실][^ref-820] |
| 작업 대상 | 공공 지도 서비스 데이터와 분기점 단위 위상 지도. [사실][^ref-820] |
| 수행 자원 | 공공 지도 데이터를 지도 구축 방법으로 변환하며, 로봇 주행은 이 지도로 전역 경로를 계획한다. [사실][^ref-820] |
| 제약 | 분기점 단위로 표현하므로 분기점 사이의 세부 기하는 이 지도가 담지 않는다(이 위키의 해석). [추정][^ref-820] |
| 완료·인계 | A* 기반 모의실험으로 지도의 유효성을 검증했다. [사실][^ref-820] |
| 예외·성과 | 전역 경로 계획 데이터 생성 비용을 줄일 수 있다고 보고했다. [사실][^ref-820] |

국내 연구(대한공간정보학회지, 2022-06)로, 사람이 그리거나 로봇이 주행해 만드는 대신 이미 있는 데이터에서 위상 지도를 얻는 사례다. 대화로 만드는 지도도 이런 외부 데이터를 시작점으로 받을 수 있다.

**기타 현장의 연계 대상 사례.** 대학 건물 5개 층을 로봇이 3D 라이다·IMU(Inertial Measurement Unit, 관성 측정 장치) SLAM(Simultaneous Localization and Mapping, 동시적 위치 추정과 지도 작성)과 프런티어 탐사, 매니퓰레이터 승강기 버튼 조작으로 27분에 스스로 지도화하고 승강기 상호작용 성공률 95% 를 보고한 국내 연구(로봇학회 논문지, 2026)가 있다. [사실][^ref-163] 이는 로봇 자체 지능·제어와 시설·설비 제어 쪽의 지도 작성이므로 연계 대상이며, 이 영역은 그 결과 지도를 입력으로 받는 쪽이다.

## 6. 대표 접근법과 기술

대화로 만드는 지도는 위상·의미 층을 담는 데 강점이 있고 정확한 기하는 센서·도면·사람 확인에서 와야 한다는 것이 이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819] Deguchi 외(ICRA 2024)는 대규모 언어 모델로 자연어 경로 지시문을 노드·에지·행동으로 된 위상 지도로 바꾸며, 지도를 언어 모델 기억에 암묵적으로 두는 것보다 명시적 위상 지도를 만드는 쪽이 정확도가 뚜렷이 높았다고 보고했다. [사실][^ref-815]

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area08-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

플릿 관제가 실제로 읽는 지도 형식이 이미 여럿이므로 채팅 맵 작성의 결과물은 자유 서술이 아니라 이런 형식에 맞는 구조화 지도 요소여야 하고, 형식마다 요소 대응(예: 충전 위치를 스테이션과 꼭짓점 속성 가운데 어디에 둘지)이 필요하다는 것이 이 위키의 추정이다. [추정][^ref-046][^ref-079] 두 형식 사이의 공식 변환 규칙은 확인하지 못했다.

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area08-s7.md)에 있다.

## 8. 대표 연구와 자료

Deguchi, Shibata, Taguchi, Language to Map(ICRA 2024) — 자연어 경로 지시문을 명시적 위상 지도로 바꾸며 암묵적 지도보다 정확도가 높았다. [사실][^ref-815] 언어만으로 위상 지도가 가능함을 보인 직접 근거다.

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 대표 연구와 자료](../../topics/2026/2026-09-29-area08-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 대화에서 층·구역·통로·문·승강기·충전 위치 같은 구조화 지도 요소를 만들어 플릿 중립 형식(빌딩 맵·LIF 류)에 담고, 확정할 수 없는 값을 확인 질문으로 받아 사람이 화면에서 확인·승인한 지도만 확정하는 일 | 라이다 SLAM(Simultaneous Localization and Mapping, 동시적 위치 추정과 지도 작성)으로 점유 격자를 만들고 위치를 추정하는 일(로봇 제조사) |
| 시설·설비 제어 | 승강기·문을 지도 요소로 등록하고 통과 조건을 제약으로 반영하는 일 | 승강기 호출·버튼 조작 같은 실제 설비 제어 |
| 업종별 조건 | 감염 관리 구역·공장 안전 구역 같은 조건을 통과 제약으로 받는 일 | 조건 자체의 전문 요구사항 |

위 표의 직접 범위는 이 위키의 추정이며, 원문 19장 경계와 "사람이 확인·승인한 계획만 실행" 주석에 맞춘 것이다. [추정][^ref-079][^ref-046][^ref-816][^ref-822] 라이다 지도 생성(노주형 외의 3D 라이다·IMU SLAM, 모빌리오의 PGM 형식 지도)과 도면을 벡터·위상 구조로 해석하는 일(Zhang 외)은 각각 로봇 자체 지능·제어와 14. 도면·BIM에서 지도 만들기·45. 문서·도면·장면 이해의 몫이고, 이 영역은 그 결과를 입력으로 받는다. [추정][^ref-163][^ref-827][^ref-083] 경계는 제품 전략에 따라 이동할 수 있으나, 이종 제조사를 연결하는 ROP 는 기하 지도 생성 엔진과 도면 해석 엔진을 연계 대상으로 두고 지도 요소의 인터페이스와 확정 절차를 맡는 편이 원문 경계에 맞다. 범위 경계 전체는 [ROP 범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[14. 도면·BIM에서 지도 만들기](../space-and-map-model/maps-from-floor-plans-and-bim.md) — 맵 작성 대화가 부르는 짝 엔진. CAD 파일에서 로봇 지도를 자동 생성하는 연구가 있다. [사실][^ref-083] 그 결과가 이 영역의 입력이 된다는 것은 이 위키의 추정이다. [추정][^ref-083]

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area08-s10.md)에 있다.

## 11. 열린 질문

**신규(id 는 퍼블리셔가 부여)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-01) 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? [^ref-046][^ref-079]

자세한 내용은 주제 페이지 [8. 채팅으로 맵 작성 — 열린 질문](../../topics/2026/2026-09-29-area08-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-815]: Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs), Language to Map: Topological map generation from natural language path instructions, 2024-03-15, https://arxiv.org/abs/2403.10008, 접근일 2026-09-29
[^ref-816]: Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models, 2025-11-05, https://arxiv.org/abs/2511.03165, 접근일 2026-09-29
[^ref-817]: Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W., Tell2Design: A Dataset for Language-Guided Floor Plan Generation, 2023, https://arxiv.org/abs/2311.15941, 접근일 2026-09-29
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-819]: Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX), Learning Semantic Maps from Natural Language Descriptions, 2013-06, https://www.roboticsproceedings.org/rss09/p04.html, 접근일 2026-09-29
[^ref-820]: 김영재, 김세윤, 김홍준 (대한공간정보학회지), 공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구, 2022-06, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654, 접근일 2026-09-29
[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-29
[^ref-822]: Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations, 2025-07-10, https://arxiv.org/abs/2507.07644, 접근일 2026-09-29
[^ref-104]: Open Robotics (open-rmf), rmf_demos — README (Demonstrations of Open-RMF), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-29
[^ref-827]: 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법, 2026-08-24, https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/, 접근일 2026-09-29
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S., Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07-01, https://arxiv.org/abs/2507.00552, 접근일 2026-09-29
[^ref-163]: 노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-09-29
```

### docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md

```markdown
---
title: "8. 채팅으로 맵 작성"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 8
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 8. 채팅으로 맵 작성

# 8. 채팅으로 맵 작성

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 맵 작성**: 공간을 글이나 말로 설명하거나 도면·사진을 올리면 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다
- **대화 중 지도 확인·확정**: 대화로 만든 지도를 화면에 보여 주고, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 확인 질문으로 받아 확정한다

## 2. 핵심 질문

공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]

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

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s6.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 대표 접근법과 기술"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-079, ref-083, ref-163, ref-815, ref-816, ref-817, ref-819, ref-822, ref-823, ref-825, ref-826]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#6
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 대표 접근법과 기술

# 8. 채팅으로 맵 작성 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대화로 만드는 지도는 위상·의미 층을 담는 데 강점이 있고 정확한 기하는 센서·도면·사람 확인에서 와야 한다는 것이 이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819] Deguchi 외(ICRA 2024)는 대규모 언어 모델로 자연어 경로 지시문을 노드·에지·행동으로 된 위상 지도로 바꾸며, 지도를 언어 모델 기억에 암묵적으로 두는 것보다 명시적 위상 지도를 만드는 쪽이 정확도가 뚜렷이 높았다고 보고했다. [사실][^ref-815]
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대화로 만드는 지도는 위상·의미 층을 담는 데 강점이 있고 정확한 기하는 센서·도면·사람 확인에서 와야 한다는 것이 이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819] Deguchi 외(ICRA 2024)는 대규모 언어 모델로 자연어 경로 지시문을 노드·에지·행동으로 된 위상 지도로 바꾸며, 지도를 언어 모델 기억에 암묵적으로 두는 것보다 명시적 위상 지도를 만드는 쪽이 정확도가 뚜렷이 높았다고 보고했다. [사실][^ref-815]

### 언어에서 위상·의미 지도로

Walter 외(RSS 2013)는 말로 설명한 장소 이름·공간 관계를 센서 관측과 함께 계량·위상·의미가 결합된 의미 그래프로 공동 추정했고, 자연어를 넣으면 센서만 쓸 때보다 지도 정확도가 올라간다고 보고했다. [사실][^ref-819] 위 두 연구와 아래 SENT-Map 어느 것도 순수 언어에서 정확한 계량 기하를 얻는다고 주장하지 않는다.

### 사람과 모델이 함께 고치는 텍스트 지도

SENT-Map(2025)은 실내 환경을 의미 정보가 붙은 JSON 위상 지도로 표현해 사람과 기반 모델이 같은 형식을 읽고 고치게 하며, 시각 기반 모델과 운영자가 짝을 이뤄 지도를 만든 뒤 자연어 질의로 계획하는 2단계 방식으로 소형 로컬 모델도 실내 계획을 할 수 있음을 보였다. [사실][^ref-816] 빌딩 맵이 층·차선·문·승강기·충전 위치를 담는 텍스트(YAML) 구조이고 축척은 사람이 준 거리로 정해지는 점을 보면, 채팅 맵 작성은 이런 텍스트 지도 구조를 대화로 채우되 확정할 수 없는 값은 확인 질문으로 받는 흐름이 자연스럽다는 것이 이 위키의 추정이며, 대화로 빌딩 맵을 채운 사례를 직접 확인한 것은 아니다. [추정][^ref-079][^ref-816]

### 언어 모델의 평면도 생성·편집(건축 설계용, 방법 참고)

다음 세 연구는 로봇 지도 작성이 아니라 건축 설계용 평면도를 다루므로 방법의 참고로만 둔다. Tell2Design(ACL 2023)은 자연어 지시와 짝지은 8만 건 이상의 평면도 데이터셋으로 언어 유도 평면도 생성 과제를 제시하고 공간·관계 제약 만족을 핵심 난점으로 꼽았다. [사실][^ref-817] HouseMind(CVPR 2026)는 방 단위 이산 토큰 어휘로 멀티모달 언어 모델 하나가 평면도를 이해·생성하고 텍스트 지시로 편집하게 했으며, 기하 타당성·제어 가능성이 기존 방식보다 낫고 로컬 배포가 가능하다는 것은 저자 보고값이다. [사실][^ref-823] Holodeck(CVPR 2024)은 한 문장 설명에서 GPT-4 가 평면도·출입구·창을 설계하고 객체 사이 공간 관계 제약을 생성해 최적화로 배치하며, 주거 장면 사람 평가에서 절차적 생성 기준선보다 선호되었다. [사실][^ref-825] 이 위키의 의견으로, 제약을 먼저 뽑고 최적화로 배치하는 구조는 지도 요소 배치에도 참고할 만하다. [의견][^ref-825]

### 공간 제약 검증과 확인 질문

FloorplanQA(2025년 7월 초판, v4 2026-05-25 개정, ICML 2026)는 JSON·XML 로 기술한 평면도에 대해 거리·가시성·경로·배치 질문으로 언어 모델을 평가했고, 모델들이 단순 질문은 처리하지만 물리 제약을 지키지 못하고 공간 일관성을 잃는 약점이 있다고 보고했다. [사실][^ref-822] 이 위키는 여기에 명확화 질문 연구와 축척 입력 관행을 더해, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 모델이 추정해 채우지 않고 선택지가 붙은 확인 질문으로 받는 쪽이 맞다고 추정한다. [추정][^ref-826][^ref-079] 다만 명확화 질문의 효과 결론은 원문 미확인이며, 지도 작성 대화에 특화된 확인 질문 연구는 찾지 못했다.

### 연계 대상: 도면 해석·SLAM 엔진

CAD 파일에서 계층 위상·계량 지도를 자동 생성하는 파이프라인과 로봇 SLAM(Simultaneous Localization and Mapping, 동시적 위치 추정과 지도 작성) 지도 작성은 각각 14. 도면·BIM에서 지도 만들기·45. 문서·도면·장면 이해와 로봇 자체 지능·제어의 몫이며, 이 영역은 그 결과를 입력으로 받는다는 것이 이 위키의 추정이다. [추정][^ref-083][^ref-163] 상세는 10절과 해당 영역 페이지에 둔다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S., Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07-01, https://arxiv.org/abs/2507.00552, 접근일 2026-09-29
[^ref-163]: 노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-09-29
[^ref-815]: Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs), Language to Map: Topological map generation from natural language path instructions, 2024-03-15, https://arxiv.org/abs/2403.10008, 접근일 2026-09-29
[^ref-816]: Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models, 2025-11-05, https://arxiv.org/abs/2511.03165, 접근일 2026-09-29
[^ref-817]: Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W., Tell2Design: A Dataset for Language-Guided Floor Plan Generation, 2023, https://arxiv.org/abs/2311.15941, 접근일 2026-09-29
[^ref-819]: Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX), Learning Semantic Maps from Natural Language Descriptions, 2013-06, https://www.roboticsproceedings.org/rss09/p04.html, 접근일 2026-09-29
[^ref-822]: Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations, 2025-07-10, https://arxiv.org/abs/2507.07644, 접근일 2026-09-29
[^ref-823]: Qin, S., Weber, R. E., & Lu, X., Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans, 2026-03-12, https://arxiv.org/abs/2603.11640, 접근일 2026-09-29
[^ref-825]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12-14, https://arxiv.org/abs/2312.09067, 접근일 2026-09-29
[^ref-826]: Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022), Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation, 2022-03, https://dl.acm.org/doi/10.5555/3523760.3523822, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s4.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 핵심 개념과 용어"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-046, ref-079, ref-815, ref-816, ref-819, ref-826, ref-827]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#4
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 핵심 개념과 용어

# 8. 채팅으로 맵 작성 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **[위상 지도(Topological Map)](../../glossary/topological-map.md)** — 장소를 노드, 연결을 에지로 표현한 지도. 기하 지도나 카메라 없이 자연어 경로 지시문만으로 노드·에지·행동의 위상 지도를 만드는 방법이 제안되었다. [사실][^ref-815]
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **[위상 지도(Topological Map)](../../glossary/topological-map.md)** — 장소를 노드, 연결을 에지로 표현한 지도. 기하 지도나 카메라 없이 자연어 경로 지시문만으로 노드·에지·행동의 위상 지도를 만드는 방법이 제안되었다. [사실][^ref-815]
- **의미 지도(Semantic Map)** — 장소 이름·공간 관계 같은 의미 정보를 계량·위상 표현과 결합한 지도. 사람이 말로 설명한 장소와 센서 관측을 함께 추정하면 센서만 쓸 때보다 정확도가 올라간다고 보고되었다. [사실][^ref-819]
- **빌딩 맵(Building Map, Open-RMF)** — 층·벽·꼭짓점(충전소·주차·도킹 속성)·플릿별 차선·문 4종·승강기·바닥을 담는 제조사 중립 지도로 .building.yaml 로 저장된다. [사실][^ref-079]
- **[레이아웃 교환 형식(Layout Interchange Format, LIF)](../../glossary/layout-interchange-format.md)** — 무인운반차 통합자가 노드·에지·스테이션으로 된 주행 레이아웃을 제3자 관제 시스템에 처음 넘겨 주기 위한 VDMA(독일기계설비제조업협회)의 법적 구속력 없는 가이드라인(1.0.0, 2023-09)이며 [VDA 5050](../../glossary/vda-5050.md)의 영향을 받았다. [사실][^ref-046]
- **축척 보정(Scale Calibration)** — 평면도 이미지의 픽셀 거리를 실제 거리로 맞추는 일. Traffic Editor 는 두 점 사이 물리 거리를 사람이 미터로 넣어야 축척이 정해진다. [사실][^ref-079]
- **명확화 질문(Clarification Question)** — 요청이 모호할 때 시스템이 아는 정보로 사용자에게 되묻는 질문. 로봇 대화에서 이를 63명 사용자 연구로 평가한 연구(HRI 2022)가 있으나, 질문을 받은 사용자가 과제를 쉽게 느끼고 로봇 역량을 높게 평가했다는 효과 결론은 원문을 열지 못해 확인하지 못했다. [추정][^ref-826] 이 용어는 [명시적 확인·암시적 확인](../../glossary/explicit-implicit-confirmation.md)·[슬롯 채우기](../../glossary/slot-filling.md)와 인접한 대화 장치다.
- **[지도 정합(Map Alignment)](../../glossary/map-alignment.md)** — 라이다 지도와 도면처럼 서로 다른 지도의 좌표계를 기준점으로 맞추는 일. 국내 업체 모빌리오는 이를 '맵 정합' 이라는 이름으로 제공한다고 주장한다. [추정] 벤더 주장[^ref-827]
- **공동 편집 텍스트 지도** — 사람과 기반 모델이 같은 JSON 위상 지도를 읽고 고치는 표현(SENT-Map, 2025). [사실][^ref-816]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-29
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-815]: Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs), Language to Map: Topological map generation from natural language path instructions, 2024-03-15, https://arxiv.org/abs/2403.10008, 접근일 2026-09-29
[^ref-816]: Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models, 2025-11-05, https://arxiv.org/abs/2511.03165, 접근일 2026-09-29
[^ref-819]: Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX), Learning Semantic Maps from Natural Language Descriptions, 2013-06, https://www.roboticsproceedings.org/rss09/p04.html, 접근일 2026-09-29
[^ref-826]: Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022), Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation, 2022-03, https://dl.acm.org/doi/10.5555/3523760.3523822, 접근일 2026-09-29 (원문 미열람)
[^ref-827]: 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법, 2026-08-24, https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s8.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 대표 연구와 자료"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-083, ref-163, ref-815, ref-816, ref-817, ref-819, ref-820, ref-822, ref-823, ref-825]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#8
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 대표 연구와 자료

# 8. 채팅으로 맵 작성 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Deguchi, Shibata, Taguchi, Language to Map(ICRA 2024) — 자연어 경로 지시문을 명시적 위상 지도로 바꾸며 암묵적 지도보다 정확도가 높았다. [사실][^ref-815] 언어만으로 위상 지도가 가능함을 보인 직접 근거다.
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- Deguchi, Shibata, Taguchi, Language to Map(ICRA 2024) — 자연어 경로 지시문을 명시적 위상 지도로 바꾸며 암묵적 지도보다 정확도가 높았다. [사실][^ref-815] 언어만으로 위상 지도가 가능함을 보인 직접 근거다.
- Rajendran Kathirvel 외, SENT-Map(ICRA 2025 워크숍) — 사람과 기반 모델이 함께 고치는 JSON 위상 지도. 대화와 화면 편집을 한 형식으로 잇는 참고. [사실][^ref-816]
- Walter 외, Learning Semantic Maps from Natural Language Descriptions(RSS 2013) — 언어와 센서를 결합한 의미 그래프 공동 추정. 언어가 지도 정확도를 올린 초기 근거. [사실][^ref-819]
- Leng 외, Tell2Design(ACL 2023) — 건축 설계용 언어 유도 평면도 생성 데이터셋. 공간·관계 제약이 난점임을 보임. [사실][^ref-817]
- Qin, Weber, Lu, HouseMind(CVPR 2026) — 건축 설계용. 방 단위 토큰으로 평면도 이해·생성·텍스트 편집을 한 모델에 통합. 우위 주장은 저자 보고값. [사실][^ref-823]
- Yang 외, Holodeck(CVPR 2024) — 건축·시뮬레이션 환경 생성용. 제약 생성 뒤 최적화 배치 구조. [사실][^ref-825]
- Rodionov 외, FloorplanQA(2025, v4 2026-05-25, ICML 2026) — 구조화 평면도 공간 추론 벤치마크. 물리 제약 미준수 약점 보고. [사실][^ref-822]
- Zhang 외, CAD 파일에서 실내 OSM 지도 생성(2025, v3 2026-03-31) — 연계 대상. 도면 해석 결과가 이 영역의 입력이 되는 경로. [사실][^ref-083]
- 김영재·김세윤·김홍준, 공공 맵 데이터 기반 전역 경로 계획용 지도 생성(대한공간정보학회지, 2022-06) — 국내 실외 위상 지도 구축 연구. [사실][^ref-820]
- 노주형 외, 탐사·엘리베이터 연계 완전 자율 다층 실내 지도 구축(로봇학회 논문지, 2026) — 연계 대상. 국내 다층 SLAM 지도화 연구. [사실][^ref-163]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S., Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07-01, https://arxiv.org/abs/2507.00552, 접근일 2026-09-29
[^ref-163]: 노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-09-29
[^ref-815]: Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs), Language to Map: Topological map generation from natural language path instructions, 2024-03-15, https://arxiv.org/abs/2403.10008, 접근일 2026-09-29
[^ref-816]: Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models, 2025-11-05, https://arxiv.org/abs/2511.03165, 접근일 2026-09-29
[^ref-817]: Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W., Tell2Design: A Dataset for Language-Guided Floor Plan Generation, 2023, https://arxiv.org/abs/2311.15941, 접근일 2026-09-29
[^ref-819]: Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX), Learning Semantic Maps from Natural Language Descriptions, 2013-06, https://www.roboticsproceedings.org/rss09/p04.html, 접근일 2026-09-29
[^ref-820]: 김영재, 김세윤, 김홍준 (대한공간정보학회지), 공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구, 2022-06, https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654, 접근일 2026-09-29
[^ref-822]: Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations, 2025-07-10, https://arxiv.org/abs/2507.07644, 접근일 2026-09-29
[^ref-823]: Qin, S., Weber, R. E., & Lu, X., Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans, 2026-03-12, https://arxiv.org/abs/2603.11640, 접근일 2026-09-29
[^ref-825]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12-14, https://arxiv.org/abs/2312.09067, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s3.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 왜 중요한가"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-079, ref-083, ref-815, ref-816, ref-817, ref-819, ref-822]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#3
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 왜 중요한가

# 8. 채팅으로 맵 작성 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대화로 만든 층·구역·통로·문 배치는 언어 모델 출력 그대로 쓰지 말고 기하 검증기나 사람 확인을 거쳐야 한다는 것이 이 위키의 추정이다. [추정][^ref-817][^ref-822] 건축 설계용 언어 유도 평면도 생성 데이터셋 연구(2023)와 구조화 텍스트 평면도에 대한 공간 추론 벤치마크(2025년 7월 초판, arXiv v4 2026-05-25 개정, ICML 2026 채택)가 서로 독립적으로 언어 모델의 공간·물리 제약 준수를 핵심 난점으로 지목했다.
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대화로 만든 층·구역·통로·문 배치는 언어 모델 출력 그대로 쓰지 말고 기하 검증기나 사람 확인을 거쳐야 한다는 것이 이 위키의 추정이다. [추정][^ref-817][^ref-822] 건축 설계용 언어 유도 평면도 생성 데이터셋 연구(2023)와 구조화 텍스트 평면도에 대한 공간 추론 벤치마크(2025년 7월 초판, arXiv v4 2026-05-25 개정, ICML 2026 채택)가 서로 독립적으로 언어 모델의 공간·물리 제약 준수를 핵심 난점으로 지목했다. 2절의 핵심 질문에 대한 현재 답은 "장소·연결·이름 같은 위상·의미 요소는 대화로 만들 수 있으나 기하·축척은 별도 확인이 필요하다"에 가깝다는 것이 이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819]

지도를 만드는 다른 입력이 필요한 이유도 있다. 로봇 SLAM(Simultaneous Localization and Mapping, 동시적 위치 추정과 지도 작성) 기반 지도 작성은 대규모·동적 실내에서 시간·노동·강건성에 한계가 있다는 주장이 CAD(Computer-Aided Design) 도면에서 로봇 지도를 자동 생성하는 연구(2025년 7월 초판, arXiv v3 2026-03-31 개정)에서 제기되었다. [사실][^ref-083] 도면과 대화는 이 한계를 보완하는 입력이 될 수 있다.

그림만으로 정해지지 않는 값이 있다. Open-RMF Traffic Editor 에서는 사용자가 실제 거리를 아는 두 점 사이에 측정선을 긋고 물리 거리를 미터로 입력해야 층의 축척이 정해진다. [사실][^ref-079] 이 위키의 의견으로, 말로도 그림으로도 확정할 수 없는 값을 누가 어떻게 확인하느냐가 이 영역의 핵심 설계 문제다. [의견][^ref-079]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S., Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07-01, https://arxiv.org/abs/2507.00552, 접근일 2026-09-29
[^ref-815]: Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs), Language to Map: Topological map generation from natural language path instructions, 2024-03-15, https://arxiv.org/abs/2403.10008, 접근일 2026-09-29
[^ref-816]: Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models, 2025-11-05, https://arxiv.org/abs/2511.03165, 접근일 2026-09-29
[^ref-817]: Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W., Tell2Design: A Dataset for Language-Guided Floor Plan Generation, 2023, https://arxiv.org/abs/2311.15941, 접근일 2026-09-29
[^ref-819]: Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX), Learning Semantic Maps from Natural Language Descriptions, 2013-06, https://www.roboticsproceedings.org/rss09/p04.html, 접근일 2026-09-29
[^ref-822]: Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations, 2025-07-10, https://arxiv.org/abs/2507.07644, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고, 2차 재검증 지시에 따라 3절의 판단 문장 두 개에 [추정]·[의견] 태그를 붙였다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s7.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-046, ref-079, ref-104]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#7
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 관련 표준·프레임워크·오픈소스

# 8. 채팅으로 맵 작성 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 플릿 관제가 실제로 읽는 지도 형식이 이미 여럿이므로 채팅 맵 작성의 결과물은 자유 서술이 아니라 이런 형식에 맞는 구조화 지도 요소여야 하고, 형식마다 요소 대응(예: 충전 위치를 스테이션과 꼭짓점 속성 가운데 어디에 둘지)이 필요하다는 것이 이 위키의 추정이다. [추정][^ref-046][^ref-079] 두 형식 사이의 공식 변환 규칙은 확인하지 못했다.
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

플릿 관제가 실제로 읽는 지도 형식이 이미 여럿이므로 채팅 맵 작성의 결과물은 자유 서술이 아니라 이런 형식에 맞는 구조화 지도 요소여야 하고, 형식마다 요소 대응(예: 충전 위치를 스테이션과 꼭짓점 속성 가운데 어디에 둘지)이 필요하다는 것이 이 위키의 추정이다. [추정][^ref-046][^ref-079] 두 형식 사이의 공식 변환 규칙은 확인하지 못했다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| [Open-RMF](../../glossary/open-rmf.md) Traffic Editor | 오픈소스 | 2D 평면도 위에 층·벽·꼭짓점·플릿별 차선·문 4종·승강기·바닥을 그려 .building.yaml 빌딩 맵을 만드는 편집기. 축척은 측정선에 사람이 미터 값을 넣어 정한다. 대화 결과를 담을 후보 형식. [사실] | [^ref-079] |
| Open-RMF rmf_demos | 오픈소스 | Clinic(2층·승강기 2대·플릿 2개)·Hotel(객실 층 2개·로비·승강기 2대·문·플릿 3개) 등 층·승강기·문을 포함한 시뮬레이션 빌딩 맵 예시. [사실] | [^ref-104] |
| VDMA [LIF](../../glossary/layout-interchange-format.md) 1.0.0 | 프레임워크(법적 구속력 없는 VDMA 가이드라인) | 통합자가 노드·에지·스테이션 레이아웃을 제3자 관제에 넘기는 형식. 대화 결과의 또 다른 목표 형식. [사실] | [^ref-046] |
| [VDA 5050](../../glossary/vda-5050.md) | 표준 | LIF 정의에 영향을 준 무인운반차 인터페이스. [사실] | [^ref-046] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-29
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-104]: Open Robotics (open-rmf), rmf_demos — README (Demonstrations of Open-RMF), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s10.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 다른 연구영역과의 연결"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-046, ref-079, ref-083, ref-104, ref-816, ref-819, ref-822, ref-823, ref-826]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#10
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 다른 연구영역과의 연결

# 8. 채팅으로 맵 작성 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 맵 작성 대화가 부르는 짝 엔진. CAD 파일에서 로봇 지도를 자동 생성하는 연구가 있다. [사실][^ref-083] 그 결과가 이 영역의 입력이 된다는 것은 이 위키의 추정이다. [추정][^ref-083]
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 맵 작성 대화가 부르는 짝 엔진. CAD 파일에서 로봇 지도를 자동 생성하는 연구가 있다. [사실][^ref-083] 그 결과가 이 영역의 입력이 된다는 것은 이 위키의 추정이다. [추정][^ref-083]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 짝 엔진. 빌딩 맵과 LIF 의 층·꼭짓점·차선·문·승강기·스테이션 요소가 대화 결과를 담는 모델이라는 것이 이 위키의 추정이다. [추정][^ref-079][^ref-046]
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 장소 이름·공간 관계 같은 의미 층을 대화로 만들고 고치는 일이 겹친다. [추정][^ref-816][^ref-819]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 원문 교차 규칙대로 평면도 이해·생성·편집 연구와 CAD 지도 생성은 이 영역과 14. 도면·BIM에서 지도 만들기 양쪽에 연결한다. [추정][^ref-823][^ref-822][^ref-083]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 언어 모델의 공간 제약 미준수와 확인 질문·사람 승인 절차가 이 영역의 신뢰 기반이다. [추정][^ref-822][^ref-826]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 대화로 등록한 승강기·문 요소가 실제 설비 연동의 대상이 된다. [추정][^ref-104]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — LIF 는 통합자가 제3자 관제에 레이아웃을 넘기는 형식이다. [사실][^ref-046]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — 빌딩 맵과 LIF 사이 요소 대응·변환 규칙이 상호운용 과제다. [추정][^ref-046][^ref-079]
- 트랙: [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md), [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-29
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S., Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07-01, https://arxiv.org/abs/2507.00552, 접근일 2026-09-29
[^ref-104]: Open Robotics (open-rmf), rmf_demos — README (Demonstrations of Open-RMF), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-29
[^ref-816]: Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K., SENT Map -- Semantically Enhanced Topological Maps with Foundation Models, 2025-11-05, https://arxiv.org/abs/2511.03165, 접근일 2026-09-29
[^ref-819]: Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX), Learning Semantic Maps from Natural Language Descriptions, 2013-06, https://www.roboticsproceedings.org/rss09/p04.html, 접근일 2026-09-29
[^ref-822]: Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations, 2025-07-10, https://arxiv.org/abs/2507.07644, 접근일 2026-09-29
[^ref-823]: Qin, S., Weber, R. E., & Lu, X., Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans, 2026-03-12, https://arxiv.org/abs/2603.11640, 접근일 2026-09-29
[^ref-826]: Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022), Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation, 2022-03, https://dl.acm.org/doi/10.5555/3523760.3523822, 접근일 2026-09-29 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고, 2차 재검증 지시에 따라 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델 항목의 역할 판단 문장을 [추정]으로 되돌렸다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-01/pages/topics/2026/2026-09-29-area08-s11.md

```markdown
---
title: "8. 채팅으로 맵 작성 — 열린 질문"
type: topic
category: "C. 채팅 기반 구성·운영"
primary_area_no: 8
related_areas: [13, 14, 15, 16, 20, 21, 22, 45]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-046, ref-079, ref-822]
last_run: 2026-09-29
version: 1
split_from: docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#11
---

[홈](../../index.md) › [주제](../index.md) › 8. 채팅으로 맵 작성 — 열린 질문

# 8. 채팅으로 맵 작성 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **신규(id 는 퍼블리셔가 부여)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-01) 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? [^ref-046][^ref-079]
- 이 페이지는 [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **신규(id 는 퍼블리셔가 부여)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-01) 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? [^ref-046][^ref-079]
- **신규(id 는 퍼블리셔가 부여)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-01) 언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가? [^ref-822]
- **신규(id 는 퍼블리셔가 부여)** (상태: 열림 · 제기 2026-09-29 · 실행 2026-09-29-01) 채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다. 트랙 전용 질문은 [채팅 기반 구성·운영 질문 백로그](../../tracks/chat-based-configuration-and-operation/question-backlog.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md)
- 관련 영역: [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-046]: VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA), 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-29
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-29
[^ref-822]: Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P., FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations, 2025-07-10, https://arxiv.org/abs/2507.07644, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-01 | 8. 채팅으로 맵 작성 의 "열린 질문" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 807건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 205개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
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
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
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

### docs/open-questions.md (요약: 대상 영역 [8] 에 걸린 0건 / 전체 123건)

```markdown
없음
```

### runs/2026-09-29-01/verification2.json

```json
{
  "run_id": "2026-09-29-01",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "브리프·1차 처분은 [추정]. 그러나 10절 '14. 도면·BIM에서 지도 만들기' 항목의 문장 'CAD 파일에서 로봇 지도를 자동 생성하는 연구는 이 영역의 입력을 만든다'가 [사실][^ref-083]로 적혀 있다. 연구의 존재(f16)는 사실이지만 '이 영역의 입력이 된다'는 역할 판단은 f22·f24 의 추정이므로 태그 상향에 해당한다. 추정 유지로 되돌릴 것(이전 2차 지시로 보고된 항목에는 없던 새 지적)."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "브리프·1차 처분은 [추정]. 10절 '15. 지도·공간·위치 모델' 항목의 문장 '빌딩 맵과 LIF 의 … 요소가 대화 결과를 담는 모델이다'가 [사실][^ref-079][^ref-046]로 적혀 있다. 요소 목록(f10·f14)은 사실이나 '대화 결과를 담는 모델'이라는 판단은 f15·f23 의 추정이므로 태그 상향이다. 추정으로 되돌릴 것(이전 2차 지시로 보고된 항목에는 없던 새 지적)."
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
    "overlaps": []
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
    "10절 '14. 도면·BIM에서 지도 만들기' 항목(세부영역 페이지 10절 첫 항목과 자동 분리 페이지 docs/topics/2026/2026-09-29-area08-s10.md 의 1절 첫 항목·3절 첫 항목이 같은 문장): 'CAD 파일에서 로봇 지도를 자동 생성하는 연구는 이 영역의 입력을 만든다. [사실][^ref-083]' 을 '[추정][^ref-083]' 으로 바꾸거나, 'CAD 파일에서 로봇 지도를 자동 생성하는 연구가 있다. [사실][^ref-083] 그 결과가 이 영역의 입력이 된다는 것은 이 위키의 추정이다. [추정][^ref-083]' 처럼 사실 문장과 추정 문장으로 나눈다 — '입력이 된다'는 역할 판단은 f22·f24 의 [추정]이며 [사실]로 쓰면 태그 상향이다.",
    "10절 '15. 지도·공간·위치 모델' 항목(docs/topics/2026/2026-09-29-area08-s10.md 3절 두 번째 항목): '빌딩 맵과 LIF 의 층·꼭짓점·차선·문·승강기·스테이션 요소가 대화 결과를 담는 모델이다. [사실][^ref-079][^ref-046]' 의 태그를 [추정][^ref-079][^ref-046] 으로 바꾸거나 요소 목록(사실)과 '대화 결과를 담는 모델'(추정) 문장으로 나눈다 — 후자는 f15·f23 의 [추정]이다.",
    "3절(docs/topics/2026/2026-09-29-area08-s3.md 3절): 태그 없는 판단 문장 두 개를 고친다. (a) '2절의 핵심 질문에 대한 현재 답은 \"…\"에 가깝다' 는 문장 끝에 '이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819]' 를 붙이거나 삭제한다 — f4·f21·f23 에서 도출한 결론이므로 태그가 필요하다. (b) '말로도 그림으로도 확정할 수 없는 값을 누가 어떻게 확인하느냐가 이 영역의 핵심 설계 문제다' 는 '이 위키의 의견으로, …핵심 설계 문제다. [의견][^ref-079]' 로 바꾸거나 삭제한다 — 근거 없는 단정을 피한다(6절의 [의견] 처리와 같은 방식)."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 23건, 미확인 1건, 교차 확인 1건(f9). 강등: f20 사실 → 추정(효과 결론이 검색 스니펫에 없음). 원문 미열람 출처: ref-826(ACM 403). 주의: ref-819 는 브리프 URL(roboticsproceedings.org)이 검증 중 연결 오류로 열리지 않아 MIT DSpace 사본으로 초록을 확인했다. 나머지 13건은 원문(arXiv 초록·HTML, github_raw, DBpia, KCI, 벤더 페이지)을 열어 기관·제목·발행일·주장 일치를 확인했다. 사실 태그 finding 은 모두 단일 출처이며 논문은 초록·본문 일부만 확인했으므로 페이지 신뢰도는 medium 이다. 대화만으로 로봇 지도를 만든 실제 현장 배치 사례는 없고, 병원 사례는 Open-RMF 시뮬레이션 데모, 제조 공장 사례는 벤더 주장이다. f8·f16 은 발행 후 arXiv 개정판(2026)이 있어 기준일에 버전을 병기한다. 정정 요청 없음. 미사용 출처 없음. / 2차 수정 후 재검증. 드리프트 없음(브리프 밖 사실·수치·사례 추가 없음), 다만 10절 14번·15번 항목에서 [추정] 처분 finding(f22·f24, f15·f23)의 결론이 [사실]로 상향된 2건과 3절의 태그 없는 판단 문장 2건에 수정 지시. 1차 수정 지시 13건은 모두 이행 확인(f20 강등, ref-826 원문 미열람 표기, f19 지도 정합 용어, f13 시뮬레이션 명시, f18 연계 대상, f5·f6·f7 건축 설계용 표기, f8·f16 버전 병기, f14 가이드라인 표기, f16·f24 교차 연결, 직접 인용 0회, 용어집 링크 재사용, ref-079·ref-104 병합 위임). [분류원문] 보존(admonition 세 줄·1절·2절 시드와 동일), 섹션 순서 준수(H2 13개 정본), 자동 분리 주제 페이지 7건은 원 절 첫 단락과 일치. 링크 유효: docs_tree.txt 가 입력에 없어 부록 A 경로·용어집 색인·입력 페이지로만 검사했고 docs/about/scope-boundary.md 는 확인하지 못했다. pages.json 이 언급한 '2차 수정 지시 7건'의 직전 verification2.json 은 입력에 없어 브리프·1차 판정과 직접 대조했다. 세부영역 페이지 프런트매터 sources 에 분리 뒤 본문에서 인용되지 않는 ref-823·ref-825·ref-826 이 남아 있으나 형식 검증을 통과했으므로 퍼블리셔 처리에 맡긴다.",
  "retry_reason": null
}
```
