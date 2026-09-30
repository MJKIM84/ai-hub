(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-03
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 14. 도면·BIM에서 지도 만들기 (D. 공간·지도 모델)
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

### runs/2026-09-30-03/target.json

```json
{
  "run_id": "2026-09-30-03",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 112,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 14,
    "area_name": "14. 도면·BIM에서 지도 만들기",
    "category": "D. 공간·지도 모델",
    "category_letter": "D"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=14"
}
```

### runs/2026-09-30-03/research.json

```json
{
  "run_id": "2026-09-30-03",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 14,
    "area_name": "14. 도면·BIM에서 지도 만들기",
    "category": "D. 공간·지도 모델"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 기준점(fiducial), 공간 경계, 설계–준공 편차, 포즈 그래프 지도 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(도면 주석·로봇 지도 정합), 기타(대학 건물 BIM 기반 위치 추정) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 래스터 평면도 벡터화, CAD 기호 인식, BIM→점유 격자·위상 지도 변환, 축척 보정·좌표 변환 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — IFC 4.3(IfcSpace·IfcTransportElement), Open-RMF 교통 편집기·플릿 어댑터 좌표 변환 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — CubiCasa5K, Raster-to-Vector, FloorPlanCAD, AI Hub 건축 도면 데이터, BIM 기반 위치 추정 연구 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 반영 안 됨",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]",
    "평면도(이미지·CAD)에서 벽·문·공간·기호를 인식하는 대표 방법과 공개 데이터셋(국내 데이터 포함)은 무엇이며 보고된 성능은 어느 수준인가? (섹션 4·6·8 겨냥)",
    "IFC 같은 BIM(Building Information Modeling)에서 공간·문·승강기를 가져와 로봇 지도(점유 격자·위상 지도)를 만드는 표준 요소·연구·도구는 무엇인가? (섹션 6·7·8 겨냥)",
    "도면 픽셀을 미터로 보정하고 제조사별 로봇 지도를 도면 좌표에 맞추는 절차는 오픈소스 관제(Open-RMF)와 제품에서 어떻게 이루어지며, 누가 확인하는가? (섹션 5·6·7 겨냥, oq-126 관련)",
    "도면·BIM 과 실제 현장이 다를 때(설계–준공 편차, 가구·배치 변경) 어떻게 확인하고 반영하는가? (섹션 3·6·11 겨냥, oq-193 관련)",
    "병원·건설 현장 등 실제 현장에서 도면 기반 지도를 쓴 사례는 무엇이며 여섯 항목으로 어떻게 정리되는가? (섹션 5 겨냥)",
    "도면·BIM 지도 작성에서 ROP가 직접 맡을 것과 로봇 자체 위치 추정·BIM 저작·설비 제어에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Open-RMF 의 교통 편집기(traffic-editor)는 건축 도면 같은 기존 평면도 이미지를 배경으로 불러와 그 위에 교통 기반 시설을 그리게 하며, 주석은 기준 평면도 이미지의 왼쪽 위를 원점으로 하는 픽셀 좌표로 만들어지고 평면도가 제조사별 로봇 지도의 기준 좌표계 역할을 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기존 건축 도면이 작업을 단순하게 하고 \"reference coordinate system for vendor-specific maps\"를 제공한다고 설명. 주석은 기준 평면도 이미지 왼쪽 위 원점의 픽셀 좌표.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "Open-RMF 교통 편집기에서 도면 축척은 도면의 축척 막대처럼 실제 거리를 아는 두 점 사이에 측정선을 긋고 실제 길이를 미터로 입력해 층별 픽셀–미터 비율을 정하는 방식으로 설정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "측정선(measurement)을 도면의 축척 막대 위에 그리고 실제 거리(m)를 입력하면 해당 층의 픽셀-미터 비율이 계산된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Open-RMF 교통 편집기는 여러 층을 맞출 때 기둥처럼 층 사이에 수직으로 같은 위치에 있을 것으로 기대되는 기준점(fiducial)을 층마다 찍고, 이를 대응시켜 층 사이의 이동·회전·축척 변환을 자동으로 계산한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "fiducial 은 둘 이상의 층에서 수직으로 정렬될 것으로 기대되는 위치(예: 구조 기둥)에 두는 기준 표식이며, 대응된 기준점으로 층 간 translation·rotation·scale 을 계산한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Open-RMF 교통 편집기에서 도면 위에 주석으로 표현하는 요소는 벽, 문(여닫이·미닫이 등 유형 지정), 여러 층에 걸친 승강기(층별 카 문 위치 포함), 이동 그래프를 이루는 차선(lane), 충전 위치(is_charger 속성의 지점)다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Walls, Doors(hinged·sliding 등), Lifts(층별 cabin door), Lanes(정점을 이어 그래프 구성), Chargers(is_charger 속성) 주석 기능 설명. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f5",
      "claim": "Open-RMF 교통 편집기는 로봇이 만든 지도를 레이어로 불러와 축척·이동·회전 변환을 주어 기준 평면도와 겹치도록 맞추게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "layers 탭으로 로봇 지도를 불러와 두 지도가 맞도록 scale·translation·rotation 변환을 적용한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 교통 편집기 좌표계가 다르면 두 좌표계에서 서로 대응하는 지점 쌍(reference_coordinates)을 설정 파일에 적게 하고 최소 4개 대응 지점을 권장하며, nudged 라이브러리로 회전·축척·이동 변환을 추정해 명령 좌표를 자동으로 바꾼다.",
      "tag": "사실",
      "source_ids": [
        "ref-153"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "config.yaml 에 두 좌표계의 대응 (x, y) 지점을 적고, \"A minimum of 4 matching waypoints is recommended.\" nudged 로 변환 추정. 같은 좌표계면 생략 가능. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Valner 외(Frontiers in Robotics and AI, 2022-08)에 따르면 에스토니아 타르투 대학병원 현장 시험에서는 PAL Robotics TIAGo 를 원격 조작해 SLAM 으로 격자 지도를 만들고, 병원 건축 평면도에 Open-RMF 교통 편집기로 벽·문·차선·충전소·주요 위치를 주석한 뒤 격자 지도를 평면도에 정합해 두 좌표 표현 사이 변환을 정했으며, 이 지도로 중환자실에서 검사실까지 시간이 중요한 혈액 검체를 운반하고 RFID·근접 센서로 여는 반자동 문 두 곳을 통과했다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TIAGo 원격 조작 매핑 → 평면도를 Traffic Editor 에서 주석(벽·문·차선·충전소) → 격자 지도를 평면도에 정렬. 과제: 중환자실→검사실 혈액 검체 운반, 반자동 문 2곳.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f8",
      "claim": "같은 타르투 대학병원 시험의 저자들은 넓은 구역을 한 번에 매핑하면 누적 불확실성 때문에 지도가 비틀리기 쉬우므로 작은 구역으로 나눠 매핑하고 하위 지도를 손으로 합치는 편이 더 정확하다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "넓은 영역 매핑은 누적 불확실성으로 skewed map 이 되기 쉽고, 작은 구역으로 매핑해 하위 지도를 수동 병합하면 더 정확하다는 교훈.",
      "as_of": "2022-08-23",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f9",
      "claim": "IFC 4.3 문서에서 IfcSpace 는 건물 안에서 특정 기능을 제공하는 실제 또는 이론상 경계로 둘러싸인 면적·부피이며, IfcRelAggregates 로 층(building storey, 외부 공간은 site)에 속해 공간 계층을 이루고 IfcRelSpaceBoundary 로 물리적·가상 경계가 정의된다.",
      "tag": "사실",
      "source_ids": [
        "ref-156"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"A space represents an area or volume bounded actually or theoretically.\" 층(또는 site)에 IfcRelAggregates 로 연결, IfcRelSpaceBoundary 로 경계 정의. 개발 브랜치 문서 기준.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f10",
      "claim": "IFC 4.3 문서에서 IfcTransportElement 는 시설 안에서 사람·동물·물품을 옮기는 운송 요소 전체를 일반화한 요소로, 승강기(lift)·에스컬레이터·무빙워크를 포함하며 PredefinedType 이나 IfcTransportElementType 으로 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-213"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Transportation elements include elevator (lift), escalator, moving walkway, etc.\" PredefinedType 또는 IfcTransportElementType 으로 유형 지정. 개발 브랜치 문서 기준.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f11",
      "claim": "Kalervo 외(2019)의 CubiCasa5K 는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 주석한 데이터셋이며, 저자들은 휴리스틱·저수준 픽셀 연산 대신 개선된 다중 작업 합성곱 신경망으로 평면도를 자동 해석하는 방법을 함께 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-063"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5000 개 샘플을 80개 이상 평면도 객체 범주로 다각형 주석, improved multi-task CNN 제안(arXiv 초록 기준).",
      "as_of": "2019-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "Liu·Wu·Kohli·Furukawa(ICCV 2017)의 Raster-to-Vector 는 신경망으로 벽 모서리·문 끝점 같은 접합점을 찾고 정수 계획법으로 이를 벽선·문선·아이콘 상자로 묶어 위상·기하가 일관된 벡터 평면도를 만들며, 저자 평가에서 정밀도·재현율 약 90%를 얻고 실제 서비스용 평면도 이미지 수십만 장을 벡터로 변환했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1015"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "접합점 검출 신경망 + 정수 계획법으로 벽·문·아이콘 기본 요소 구성. 약 90% precision·recall, hundred thousand production-level 평면도 변환(저자 발표 기준, 프로젝트 페이지 초록).",
      "as_of": "2017",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "Fan 외(ICCV 2021)의 FloorPlanCAD 는 주거·상업 건물의 벡터 CAD 평면도 1만 장 이상을 30개 객체 범주로 선 단위 주석한 데이터셋으로, 셀 수 있는 사물 인스턴스와 셀 수 없는 영역의 의미를 함께 찾는 파놉틱 심볼 스포팅 과제와 CNN–GCN 결합 방법을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-067"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "10,000+ 주거·상업 건물 CAD 평면도, 30개 범주, panoptic symbol spotting 과제, CNN-GCN 하이브리드(arXiv 초록 기준).",
      "as_of": "2021-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "AI Hub 의 '건축 도면 데이터'(2022년 구축, 주관기관 에이치씨아이플러스)는 평면도 41,556장을 포함한 건축 도면 48,033장으로 이루어지며, 출입문·창호·벽체 등 구조 8종, 거실·침실·주방·현관·화장실 등 공간 12종, 객체 5종 라벨과 문자 인식(OCR) 304,462건을 담은 인공지능 학습용 데이터다.",
      "tag": "사실",
      "source_ids": [
        "ref-1019"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "48,033장(평면도 41,556·단면도 3,262·입면도 1,595·구조도 1,620), 구조 8종·공간 12종·객체 5종, OCR 304,462건. 객체탐지·구조·공간분석 서비스 개발 목적. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "연계 대상: Hendrikx 외(ICRA 2021)는 IFC 형식 BIM 의 의미 요소를 로봇용 세계 모델 표현으로 바꿔 공간 데이터베이스에 저장하고, 로봇 주변의 구조 요소를 질의해 특징 검출기를 설정한 뒤 그래프 기반 방법으로 위치를 추정해, 2D LiDAR 와 주행거리계만 가진 로봇이 BIM 이 있는 대형 대학 건물에서 자세를 추적할 수 있음을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1017"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IFC 의미 요소 → robot-specific world model, 공간 DB 질의로 특징 검출기 구성, 그래프 기반 위치 추정. 시험 환경: 대형 대학 건물(초록 기준).",
      "as_of": "2021",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Vega Torres·Braun·Borrmann(ECPPM 2022)은 복잡한 BIM 에서 구조 요소만 담은 2D 점유 격자 지도를 자동 생성하고 이를 포즈 그래프 지도로 바꾸는 방법을 제안했으며, BIM 과 현실의 차이(Scan-BIM 편차)가 가구·잡동사니뿐 아니라 설계 모델과 준공 상태의 차이에서도 생긴다고 지적하고, 제안 방법이 변화·동적 환경에서 일반 AMCL 보다 강건하게 위치를 추정했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "BIM → 구조 요소만의 2D OGM 자동 생성 → Pose Graph 지도 변환. Scan-BIM 편차 원인: 가구·잡동사니와 as-planned/as-built 차이. AMCL 대비 강건(초록 기준).",
      "as_of": "2022-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f17",
      "claim": "연계 대상: 같은 연구진의 BIM-SLAM(ISARC 2023, arXiv 2024-08)은 BIM 에서 포즈 그래프 지도·기술자 같은 세션 데이터를 먼저 만들고 다중 세션 앵커링으로 실제 LiDAR 측정과 맞추며, BIM 에 없는 요소를 찾아 묶고 표면으로 재구성해 설계 모델과 실제 실내 상태의 차이를 드러내고, 로봇의 초기 자세를 몰라도 BIM 에 정렬된 지도를 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-221"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "BIM 에서 session data 생성 → multi-session anchoring 으로 LiDAR 와 정렬, BIM 에 없는 요소 검출·재구성, 초기 자세 불필요(arXiv 초록 기준).",
      "as_of": "2024-08",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "Zhang·Wu·Ma·Schwertfeger(arXiv 2507.00552, 2025-07; 2026-03 개정)는 SLAM 매핑의 시간·노력·강건성 한계를 피하려고 건축 CAD 파일에서 구조 요소를 추출하고 AreaGraph 기반 위상 분할로 이동 가능한 공간을 나누며 CAD 의 문자 라벨을 넣고 여러 층을 합쳐 로봇 항법용 계층형 위상·거리 OpenStreetMap 실내 지도를 자동 생성하는 파이프라인과 GUI 를 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CAD → 구조 요소 추출 → AreaGraph 위상 분할 → 문자 라벨 자동 반영 → 다층 병합 → 계층형 topometric OSM. 코드·데이터 공개(프리프린트 초록 기준).",
      "as_of": "2025-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "모빌리오(Mobilio Robotics)는 자사 산업용 순찰 로봇 관제 솔루션이 사용자가 기둥·모서리 같은 기준점 3개 이상을 지정하면 2D LiDAR 지도를 CAD·BIM 도면에 정합하고 회전각·크기를 미세 조정해 로봇 위치를 실제 도면 위에 보여 주며, 공장·플랜트를 대상으로 한다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-817"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'Map Registration' 기능으로 3개 이상 기준점(기둥·모서리)을 지정해 2D LiDAR 지도와 CAD/BIM 도면의 좌표계를 맞추고 회전·크기를 미세 조정한다고 설명.",
      "as_of": "2026-08-24",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "엔지니어링데일리 보도에 따르면 국토교통부의 건설산업 BIM 활성화 로드맵은 설계 단계부터 BIM 100% 도입을 핵심 목표로 삼고 측량·설계·시공·감리·유지관리까지 전 단계에 BIM 을 쓰게 하며, LH 공공주택부터 BIM 적용을 의무화해 단계적으로 넓히는 계획을 담았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1024"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "설계 단계부터 BIM 100% 도입, 측량·설계·시공·감리·유지관리 전 단계 적용, LH 공공주택 의무 적용 후 단계 확대. 국토교통부 원문 보도자료는 연결 오류로 미열람. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에 대해, 평면도의 벽·문·공간·기호 인식과 BIM·CAD 에서 점유 격자·위상 지도를 만드는 일은 연구 수준에서 자동화가 진행됐지만(f12·f13·f16·f18), 축척 설정·로봇 지도와의 좌표 정합·설계–준공 편차 확인은 측정선·기준점 입력과 사람의 확인에 기대고 있어(f2·f3·f6·f7·f16), 현재 형태는 '자동 초안 + 사람 확인·보정'에 가깝다.",
      "tag": "추정",
      "source_ids": [
        "ref-1015",
        "ref-067",
        "ref-081",
        "ref-083",
        "ref-079",
        "ref-153",
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "인식·변환 자동화(R2V 약 90%, FloorPlanCAD, BIM→OGM, CAD→OSM) 대 축척·정합·편차 확인의 수동 절차(측정선, fiducial, 4개 이상 대응점, 병원 정합 사례)를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 도면·BIM 지도가 중요한 까닭은, 넓은 공간을 로봇으로 매핑하면 지도가 비틀리기 쉽고 제조사마다 지도 좌표가 다른 반면 평면도는 여러 제조사 로봇 지도를 묶는 공통 기준 좌표와 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점을 주기 때문이다(f1·f4·f8·f10).",
      "tag": "추정",
      "source_ids": [
        "ref-079",
        "ref-869",
        "ref-213"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "교통 편집기의 기준 좌표계 역할, 도면 위 문·승강기·충전 주석, 병원 매핑의 누적 오차 교훈, IFC 운송 요소 정의를 종합한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 14. 도면·BIM에서 지도 만들기에서 ROP 가 직접 맡을 범위는 평면도·CAD·IFC 를 받아 공간·문·승강기·충전 위치 초안과 공용 자원 목록을 만들고(f4·f9·f10), 층별 축척과 층 간 기준점을 설정하며(f2·f3), 제조사별 로봇 지도와 공통 좌표 사이 변환을 등록·관리하고(f5·f6), 도면과 현장의 차이를 표시해 사람이 확인·승인하게 하는 일이다(f16, oq-126 과 연결).",
      "tag": "추정",
      "source_ids": [
        "ref-079",
        "ref-153",
        "ref-156",
        "ref-213",
        "ref-081"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "교통 편집기·플릿 어댑터 기능과 IFC 공간·운송 요소 정의, Scan-BIM 편차 연구를 분류 원문 19장 경계에 대입한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇의 SLAM·LiDAR 위치 추정(BIM 을 사전 지도로 쓰는 위치 추정 포함)은 로봇 자체 지능·제어에, 승강기 운행 제어는 시설·설비 제어에 속하고, BIM 모델의 저작·갱신은 건물 소유자·설계·시공 측 체계에 속하므로, 이종 제조사를 잇는 ROP 는 이들로부터 모델·지도를 받아 공통 공간 모델로 정합하고 차이를 확인하는 인터페이스를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1017",
        "ref-081",
        "ref-221",
        "ref-213",
        "ref-1024"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "BIM 기반 위치 추정 연구(로봇 측 기능), IFC 운송 요소(설비), BIM 전 단계 적용 정책(건물 측 체계)을 19장 경계에 대입한 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "이 영역은 좌표 정렬·다층 모델을 다루는 15. 지도·공간·위치 모델(f3·f5·f6), 지도 편집·버전을 다루는 16. 장소 의미·지도 관리(f1·f16), 대화로 맵을 만드는 8. 채팅으로 맵 작성(f2·f6), 도면 해석 AI 를 다루는 45. 문서·도면·장면 이해(f11~f14), 승강기·문 연동을 다루는 22. 설비·건물 시스템 연동(f4·f10), 충전 위치를 다루는 28. 공용 자원·충전·에너지 최적화(f4), 차선 그래프를 쓰는 27. 다중 로봇 경로·교통 관리 — MAPF(f4), 설치 때 매핑·정합을 하는 55. 현장 조사·설치·시운전(f7·f8), 현재 상태의 차이를 다루는 18. 실시간 세계 상태·데이터 일관성(f17), 병원 적용을 다루는 63. 병원·의료(f7)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-079",
        "ref-153",
        "ref-081",
        "ref-063",
        "ref-1015",
        "ref-067",
        "ref-1019",
        "ref-213",
        "ref-869",
        "ref-221"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 finding 이 다루는 기능을 분류 원문 영역 정의와 교차 규칙(도면 해석은 14번에 적용되는 AI 방법, 맵 작성은 14·15번 엔진과 짝)에 대응시킨 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 교통 편집기 장. 평면도 이미지 위 벽·문·승강기·차선·충전 위치 주석, 측정선으로 축척 설정, 기준점(fiducial)으로 층 정렬, 로봇 지도 레이어 정합을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-153",
      "org": "Open Robotics",
      "title": "Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "플릿 어댑터 작성 튜토리얼. 로봇 좌표계와 RMF 좌표계의 대응 지점(reference_coordinates, 4개 이상 권장)으로 nudged 라이브러리가 회전·축척·이동 변환을 추정하는 방법을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/integration_fleets_adapter_tutorial.md",
      "source_unopened": false
    },
    {
      "id": "ref-156",
      "org": "buildingSMART International",
      "title": "IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main)",
      "published": null,
      "url": "https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IFC 4.3 의 공간 요소 IfcSpace 정의(기능을 가진 경계 있는 면적·부피, 층 소속, 공간 경계 관계). 개발 브랜치 문서라 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md",
      "source_unopened": false
    },
    {
      "id": "ref-213",
      "org": "buildingSMART International",
      "title": "IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main)",
      "published": null,
      "url": "https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IFC 4.3 의 운송 요소 IfcTransportElement 정의. 승강기·에스컬레이터·무빙워크를 포함한다. 개발 브랜치 문서라 게시판과 문구가 다를 수 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md",
      "source_unopened": false
    },
    {
      "id": "ref-063",
      "org": "Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J.",
      "title": "CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis",
      "published": "2019-04",
      "url": "https://arxiv.org/abs/1904.01920",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "평면도 이미지 5,000장을 80개 이상 범주로 다각형 주석한 데이터셋과 다중 작업 CNN 평면도 해석 모델. arXiv 초록 페이지를 열어 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/1904.01920",
      "source_unopened": false
    },
    {
      "id": "ref-1015",
      "org": "Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017)",
      "title": "Raster-to-Vector: Revisiting Floorplan Transformation",
      "published": "2017",
      "url": "https://art-programmer.github.io/floorplan-transformation.html",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "래스터 평면도를 접합점 검출 신경망과 정수 계획법으로 벡터 평면도로 바꾸는 방법. 저자 프로젝트 페이지의 초록을 열어 확인했고 논문 본문(CVF)은 403 으로 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://art-programmer.github.io/floorplan-transformation.html",
      "source_unopened": false
    },
    {
      "id": "ref-067",
      "org": "Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021)",
      "title": "FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting",
      "published": "2021-05",
      "url": "https://arxiv.org/abs/2105.07147",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "주거·상업 건물 벡터 CAD 평면도 1만 장 이상, 30개 범주의 파놉틱 심볼 스포팅 데이터셋과 CNN–GCN 방법. arXiv 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2105.07147",
      "source_unopened": false
    },
    {
      "id": "ref-1017",
      "org": "Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021)",
      "title": "Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization",
      "published": "2021",
      "url": "https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IFC BIM 의 의미 요소를 로봇 세계 모델로 바꿔 2D LiDAR 위치 추정에 쓰는 방법. 대형 대학 건물에서 시험. 에인트호번 공대 연구 포털의 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/",
      "source_unopened": false
    },
    {
      "id": "ref-081",
      "org": "Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022)",
      "title": "Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2308.05443",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "BIM 에서 구조 요소만의 2D 점유 격자 지도를 자동 생성해 포즈 그래프 지도로 바꾸고 Scan-BIM 편차에 강건한 위치 추정을 보인 연구. arXiv 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2308.05443",
      "source_unopened": false
    },
    {
      "id": "ref-1019",
      "org": "AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주)",
      "title": "건축 도면 데이터",
      "published": null,
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2022년 구축된 건축 도면 인공지능 학습용 데이터(48,033장, 구조·공간·객체 라벨과 OCR). 데이터 소개 페이지를 열어 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "source_unopened": false
    },
    {
      "id": "ref-817",
      "org": "모빌리오(Mobilio Robotics)",
      "title": "[최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션)",
      "published": "2026-08-24",
      "url": "https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업용 순찰 로봇 웹 관제 솔루션 소개 글. LiDAR 지도와 CAD·BIM 도면의 기준점 정합 기능을 주장한다. 제목 전체는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98",
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R. 외 (Frontiers in Robotics and AI)",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타르투 대학병원에서 Open-RMF 기반 이기종 로봇 플릿으로 검체 운반을 시험한 현장 연구. 평면도 주석과 로봇 격자 지도 정합 절차를 기술한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "source_unopened": false
    },
    {
      "id": "ref-083",
      "org": "Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv)",
      "title": "Generation of Indoor Open Street Maps for Robot Navigation from CAD Files",
      "published": "2025-07",
      "url": "https://arxiv.org/abs/2507.00552",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "건축 CAD 파일에서 로봇 항법용 계층형 위상·거리 OSM 실내 지도를 자동 생성하는 파이프라인(프리프린트, 2026-03 개정). arXiv 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2507.00552",
      "source_unopened": false
    },
    {
      "id": "ref-221",
      "org": "Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023)",
      "title": "BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2408.15870",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "BIM 에서 만든 세션 데이터를 다중 세션 SLAM 으로 실제 LiDAR 와 정렬하고 BIM 에 없는 요소를 검출하는 방법. ISARC 2023 발표, arXiv 게시 2024-08. 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2408.15870",
      "source_unopened": false
    },
    {
      "id": "ref-1024",
      "org": "엔지니어링데일리",
      "title": "\"설계부터 100% 도입\" 건설산업 BIM 활성화 로드맵 … (제목 일부만 확인)",
      "published": null,
      "url": "https://www.engdaily.com/news/articleView.html?idxno=12613",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "국토교통부 건설산업 BIM 활성화 로드맵(설계부터 BIM 100% 도입, 전 단계 적용, LH 공공주택 의무화 후 확대)을 전한 기사. 국토교통부 원문은 연결 오류로 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.engdaily.com/news/articleView.html?idxno=12613",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
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
      "rationale": "섹션 3: f22(공통 기준 좌표·공용 자원 목록의 출발점), f8(넓은 구역 매핑의 누적 오차), f20(국내 BIM 전 단계 적용 정책, 기사 기준 신뢰도 low) / 섹션 4: 기준점(fiducial) f3, 공간·공간 경계 f9, 운송 요소 f10, 설계–준공 편차 f16, 포즈 그래프 지도 f16 / 섹션 5: 병원 — f7(타르투 대학병원 평면도 주석·격자 지도 정합·검체 운반), f8(예외·성과); 기타 — f15(대학 건물 BIM 기반 위치 추정, 연계 대상 표시). 여섯 항목 가운데 시작 조건·완료·인계 근거는 부족함을 명시 / 섹션 6: 래스터 평면도 벡터화 f12, CAD 기호 인식 f13, 평면도 해석 데이터셋 f11·f14, BIM→점유 격자·포즈 그래프 f16, CAD→위상 OSM f18, 축척 보정 f2, 층 정렬 f3, 로봇 지도 정합 f5·f6, 편차 검출 f17, 제품 사례 f19(벤더 주장 병기 필수), 자동화 수준 종합 f21 / 섹션 7: IFC 4.3 f9·f10, Open-RMF 교통 편집기 f1~f5, 플릿 어댑터 좌표 변환 f6 / 섹션 8: f11~f18, f7 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 8, 15, 16, 18, 22, 27, 28, 45, 55, 63 / 섹션 11: 기존 oq-126·oq-193 과 open_questions_new 4건. 다음 실행 후보: 15. 지도·공간·위치 모델 페이지에 f6(대응점 기반 좌표 변환) 반영, 45. 문서·도면·장면 이해 페이지에 f11~f14 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "층 정렬 기준점",
      "term_en": "Fiducial (Level Alignment Fiducial)",
      "definition": "기둥처럼 여러 층에서 수직으로 같은 위치에 있다고 기대되는 지점에 찍는 표식으로, 대응시킨 기준점들로 층 사이의 이동·회전·축척 변환을 계산하는 데 쓴다."
    },
    {
      "term_ko": "공간 경계",
      "term_en": "Space Boundary (IfcRelSpaceBoundary)",
      "definition": "IFC 에서 공간(IfcSpace)을 둘러싼 벽·슬래브 같은 물리적 요소나 가상 경계와 그 공간을 잇는 관계로, 공간의 범위와 인접 관계를 정의한다."
    },
    {
      "term_ko": "설계–준공 편차",
      "term_en": "As-planned vs As-built Deviation",
      "definition": "설계 단계에서 만든 건물 모델과 실제 지어진 상태 사이의 차이로, BIM 을 로봇 지도로 쓸 때 위치 추정 오차의 원인이 된다."
    }
  ],
  "open_questions_new": [
    "Raster-to-Vector 의 약 90% 정밀도·재현율처럼 보고된 평면도 인식 성능은 주로 주거용 도면 기준인데, 병원·공장·물류창고 같은 비주거 시설 도면에서 벽·문·승강기·충전 위치 인식 정확도를 보고한 자료가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f12 | 종류: 일반",
    "AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 승강기·계단·충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해 | 근거: f14 | 종류: 일반",
    "도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 제품 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 55. 현장 조사·설치·시운전 | 근거: f6 | 종류: 일반",
    "국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가? | 관련 영역: 14. 도면·BIM에서 지도 만들기, 22. 설비·건물 시스템 연동 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f20 국토교통부 원문 보도자료(molit.go.kr)는 ECONNRESET 으로 열지 못해 기사 기준이며, 공공공사 금액별 BIM 의무화 연도(검색 요약에만 나옴)는 넣지 않음",
      "ref-1024 기사 발행일과 제목 전체 미확인",
      "ref-817 모빌리오 글의 제목 전체 미확인, 정합 기능·성능은 벤더 주장이며 독립 확인 없음",
      "ref-1019 AI Hub 데이터 공개일 미확인(구축 연도 2022 만 확인)",
      "f11~f13·f15~f18 은 논문 초록·프로젝트 페이지 기준이며 본문의 실험 조건 미확인(Raster-to-Vector CVF 본문 403)",
      "f12 의 약 90% 수치는 저자 평가이며 교차 확인 실패",
      "f9·f10 은 IFC 4.3 개발 브랜치 문서 기준으로 게시판(ADD2)과의 문구 일치 미확인",
      "도면 인식 결과를 로봇 지도로 확정하는 승인 주체·시점(oq-126)은 어느 자료에서도 확인되지 않음",
      "건설 현장 지도–BIM 동기화 주기와 국내 사례(oq-193)는 이번 조사에서 확인되지 않음",
      "병원 외 현장 유형(물류창고·제조 공장·상업 시설)의 도면 기반 지도 사례는 벤더 주장(f19) 외에 확인되지 않음"
    ],
    "scope_violations": [
      "f15·f17: BIM 을 사전 지도로 쓰는 로봇 위치 추정·SLAM 은 분류 원문 19장의 로봇 자체 지능·제어(센서 인식·SLAM)이므로 claim 을 '연계 대상: '으로 시작함",
      "f16: BIM→점유 격자 지도 생성은 직접 범위 후보이나 AMCL 비교 등 위치 추정 성능 부분은 로봇 자체 지능·제어 쪽 근거로만 쓰도록 제안함",
      "f24: 승강기 제어(시설·설비 제어), BIM 저작·갱신(건물 측 체계)을 '연계 대상: '으로 표시함",
      "f20: BIM 정책은 이 영역의 입력 데이터 가용성 근거로만 쓰고 ROP 직접 범위로 서술하지 않음"
    ],
    "budget_used": {
      "queries": 13,
      "sources": 15
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치: finding f7 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시가 없음): 직전 반환값(runs/2026-09-30-03/research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상·예산 안에서 조사를 다시 해 전체 브리프를 새로 만들었다. finding·출처 번호는 직전 반환값과 다를 수 있다. 이번 브리프에서 벤더 문서 유형 출처(ref-817)만 근거로 한 finding 은 f19 하나이며 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 이번 f7 은 동료심사 논문(ref-869, Frontiers)에 근거한 병원 사례이며 벤더 문서를 근거로 하지 않는다. 벤더 문서만 근거로 한 [사실] finding 은 없다(관련 finding: f7, f19). web_fetch_available: true · fetch_mode full. 사용량은 검색 13회/30, 신규 출처 15건/15(ref-079~ref-1024, 예약 구간 안)로 출처 상한에 도달했다. 그래서 BIM2RDT(건설 현장 BIM–로봇 디지털 트윈, arXiv 2509.20705, 열었음), 평면도 사전지식 기반 장기 위치 추정(arXiv 2303.10959), IFC→ROS 지도 도구 BIRS, Nav2 지도 YAML 형식(해상도·원점; 문서 URL 404)은 넣지 못했다. 원문 열람: 15건 모두 열었다(github_raw 4건, webfetch 11건). 논문은 대부분 초록 페이지다. 열지 못해 쓰지 않은 것: 국토교통부 보도자료·ancnews(ECONNRESET), 한국경제(403), Springer 'Improving autonomous robotic navigation using IFC files'(인증 리디렉션), CVF 논문 페이지(403). 교차 확인 0건, 신뢰도 high finding 없음(모든 사실 finding 이 단일 출처). 분류 원문 핵심 질문(도면·건물 모델에서 로봇 지도를 얼마나 자동으로 만들 수 있는가)에는 f21 로 답했고 결론은 '인식·변환은 연구 수준에서 자동화됐으나 축척·정합·편차 확인은 사람 입력·확인에 기대는 자동 초안 + 사람 확인 형태'라는 추정이다. 현장 유형 사례는 병원(f7·f8)과 기타(f15, 대학 건물)이며, 물류창고·제조 공장·상업 시설 사례는 벤더 주장(f19, 현장 유형 미특정) 외에 찾지 못했다. 국내 자료는 AI Hub(ref-1019)·엔지니어링데일리(ref-1024)·모빌리오(ref-817) 세 건이다. L. AI·학습 기술 관련(평면도 인식 f11~f14)은 교차 규칙에 따라 45. 문서·도면·장면 이해와 적용 대상 14. 도면·BIM에서 지도 만들기에 함께 연결했다. 18. 실시간 세계 상태·데이터 일관성은 현재 상태와 BIM 차이(f17)로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 평면도 인식·래스터–벡터 변환·파놉틱 심볼 스포팅·스캔 대 BIM 비교·지도 정합·유사 변환·IFC·점유 격자 지도는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 oq-126·oq-193 은 관련 근거(f6·f7, f16·f17)가 늘었으나 해결되지 않았다."
  }
}
```

### runs/2026-09-30-03/verification.json

```json
{
  "run_id": "2026-09-30-03",
  "stage": "first",
  "verdict": "조건부 승인",
  "retry_reason": null,
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-079 원본(raw.githubusercontent.com traffic-editor.md) 열람. 'provide a \"reference\" coordinate system for vendor-specific maps' 문장과 기준 평면도 이미지 왼쪽 위 원점 픽셀 좌표(+X 오른쪽, +Y 아래) 서술 일치. 단일 출처, 발행일 미확인."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 축척 막대 위에 측정선을 긋고 두 점 사이 실제 거리(m)를 넣으면 축척이 갱신된다는 서술 일치(ref-079 원문). 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: fiducial 은 둘 이상 층에서 수직으로 정렬될 것으로 기대되는 위치의 기준 표식이며 이동·회전·축척 변환을 도출한다는 서술 일치(ref-079 원문)."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 벽, 유형이 있는 문(여닫이·미닫이 등), 여러 카 문을 가진 승강기, 차선, is_charger 정점 속성 서술 일치(ref-079). ref-869(Valner 외)도 교통 편집기로 벽·문·차선·충전소를 주석했다고 적어 일부(승강기 제외)를 독립 사례로 뒷받침하나 브리프가 인용하지 않아 교차 확인으로 세지 않는다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇 지도를 평면도 위에 불러와 축척·이동·회전 변환으로 맞춘다는 서술 일치(ref-079). 15. 지도·공간·위치 모델의 좌표 정렬과 겹치므로 14 페이지에서는 도면 기준 정합 절차로 한정한다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-153 원본 열람. 'A minimum of 4 matching waypoints is recommended.' 문장, nudged 로 회전·축척·이동 변환 추정 일치. 인용 구절은 원문과 같다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Frontiers in Robotics and AI, Valner 외, 2022-08-23. 타르투 대학병원, TIAGo 원격 조작 SLAM 격자 지도, 교통 편집기 평면도 주석(벽·문·차선·충전소·주요 위치), 격자 지도–평면도 정렬, 중환자실→검사실 혈액 검체, RFID·근접 센서 반자동 문 2곳 모두 원문과 일치. 동료심사 논문 단일 출처. 현장 유형 병원 적정."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 넓은 구역 매핑의 누적 불확실성, 작은 구역 매핑 후 하위 지도를 이미지 처리 소프트웨어로 수동 병합하는 편이 더 정확하다는 교훈 일치(ref-869)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IfcSpace 정의('A space represents an area or volume bounded actually or theoretically'), 층(외부 공간은 site) 소속, IfcRelAggregates, IfcRelSpaceBoundary 의 물리적·가상 경계 서술 일치. IFC 4.3 개발 브랜치(ifc4.3-main) 문서 기준이며 게시판(ADD2)과의 문구 일치 미확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 사람·동물·물품을 옮기는 운송 요소 일반화, 'elevator (lift), escalator, moving walkway' 포함, PredefinedType·IfcTransportElementType 서술 일치. 개발 브랜치 기준."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 1904.01920(2019-04-03 제출) 초록. 5,000개 샘플, 80개 이상 범주 다각형 주석, 휴리스틱·저수준 픽셀 연산 대신 개선된 다중 작업 CNN 일치. 초록 기준."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 저자 프로젝트 페이지 초록에서 접합점 신경망+정수 계획법, 벽선·문선·아이콘 상자, 'around 90% precision and recall', 'hundred thousand production-level floorplan images' 일치. 약 90% 는 저자 평가 단일 출처이므로 저자 보고로만 서술(주장 문장이 이미 그렇게 되어 있음). CVF 본문 미열람."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2105.07147 초록(1만 장 이상 주거·상업 CAD 평면도, 30개 범주, 파놉틱 심볼 스포팅, CNN–GCN) 일치. ICCV 2021 게재는 검증 검색에서 CVF Open Access 목록으로 확인."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AI Hub 소개 페이지 열람. 2022년 구축, 에이치씨아이플러스(주), 48,033장(평면도 41,556·단면도 3,262·입면도 1,595·구조도 1,620), 구조 8종·공간 12종·객체 5종, OCR 304,462건 일치. 발행일 정정 필요: 페이지에 개방일 2023-07-26, 최종개방 2023-12-15 가 있어 브리프의 '발행일 미확인'·as_of 2026-09-30 은 틀렸다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 에인트호번 공대 연구 포털. Hendrikx 외, ICRA 2021(시안). IFC 의미 요소→로봇 세계 모델, 공간 DB 질의로 특징 검출기 설정, 그래프 기반 위치 추정, 2D LiDAR·주행거리계, 대학 건물 시험 일치. '연계 대상: ' 표시 적정(로봇 자체 위치 추정). 현장 유형 기타는 시험 환경이라는 점을 밝혀야 한다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2308.05443 초록, ECPPM 2022(2022-09). 구조 요소만의 2D 점유 격자 지도 자동 생성→포즈 그래프 지도, Scan-BIM 편차가 가구·잡동사니와 as-planned/as-built 차이에서 생긴다는 문장, AMCL 대비 강건 일치. AMCL 비교 등 위치 추정 성능은 로봇 자체 지능·제어 쪽 근거로만 쓴다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2408.15870(2024-08-28 제출), ISARC 2023. BIM 에서 포즈 그래프 지도·기술자 생성, 다중 세션 앵커링, BIM 에 없는 요소 식별·표면 재구성, 초기 자세 불필요 일치. '연계 대상: ' 표시 적정."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2507.00552, 2025-07-01 제출·2026-03-31 개정. CAD 구조 레이어 추출, AreaGraph 위상 분할, 문자 라벨 자동 연결, 다층 병합, 계층형 topometric OSM, GUI·데이터 공개 일치. 동료심사 전 프리프린트."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 모빌리오 글(2026-08-24) 열람. 2D LiDAR 맵(PGM)과 CAD/BIM 도면에 기둥·모서리 등 기준점 3개 이상 지정, 회전·크기 미세 조정, 공장·플랜트 대상 서술 일치. vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리 적정. 독립 확인 없음."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 기사 원문 열람 결과 발행일 2020-12-28(조항일 기자), 국토교통부 공개일 2020-12-29 로 브리프의 '발행일 미확인'·as_of 2026-09-30 은 틀렸다. 기사 표현은 '조사-설계-발주-조달-시공-감리-유지관리 등 전 생애주기'이며 '측량'은 본문에 없고, 'LH 공공주택'이 아니라 'LH 공동주택'이다. 정부 원문 미열람의 기사 단독 출처이고 2020년 발표라 이후 이행 상황이 미확인이다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. 인용 finding(f2·f3·f6·f7·f12·f13·f16·f18)이 모두 살아남아 근거가 된다. '완전 자동'류 표현 없이 '자동 초안 + 사람 확인·보정'을 추정으로 제시해 적정."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. f1·f4·f8·f10 에 기대며 추정 태그 적정."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 분류 원문 19장 경계에 대입한 추정. 직접 범위를 도면 초안·축척·좌표 변환 등록·차이 표시·사람 승인으로 한정해 경계 적정. 구축자 추정임을 밝혀 서술."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: '연계 대상: ' 표시. SLAM·위치 추정(로봇 자체 지능·제어), 승강기 운행 제어(시설·설비 제어), BIM 저작(건물 측) 구분이 원문 19장과 맞는다. ref-1024 는 f20 강등에 따라 정책 배경으로만 쓴다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 연결 영역을 번호와 이름으로 적었고 교차 규칙(45. 문서·도면·장면 이해와 적용 대상 14 양쪽 연결, 8. 채팅으로 맵 작성은 14·15 엔진과 짝)을 지켰다. 18. 실시간 세계 상태·데이터 일관성은 현재 상태와 BIM 차이로만 연결했고 34. 시뮬레이션·예측용 디지털 트윈과 섞지 않았다."
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
      "f5·f6(로봇 지도–도면 좌표 정합, 대응점 기반 변환)은 게시된 15. 지도·공간·위치 모델의 '로봇별 지도·좌표계 정렬'과 겹친다. 충돌은 아니며, 14 페이지에서는 도면을 기준으로 한 정합 절차로 한정하고 좌표 통합 일반론은 15 로 연결해야 한다",
      "ref-079(Open-RMF 교통 편집기)·ref-153(플릿 어댑터 튜토리얼)·ref-869(Valner 외 Frontiers 2022)은 같은 URL 이 기존 참고문헌에 있을 수 있다(입력 참고문헌 색인은 이 페이지 인용분 0건만 보여 확인 불가). 같은 URL 이면 퍼블리셔가 기존 id 로 합친다"
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
    "f20: [사실] → [추정]으로 강등하고 문장을 기사 표현에 맞춘다 — '측량·설계·시공·감리·유지관리'를 '조사·설계·발주·조달·시공·감리·유지관리 등 전 생애주기'로, 'LH 공공주택'을 'LH 공동주택'으로 고치고 '2020-12 발표 기준이며 이후 이행 상황은 미확인'을 밝힌다. 이유: 기사 원문에 '측량'이 없고 표현이 다르며, 정부 원문 미열람 기사 단독 출처다.",
    "ref-1024: 각주의 발행일을 '미확인'에서 2020-12-28 로, 제목을 '\"설계부터 100% 도입\" 건설산업 BIM 활성화 로드맵 공개'로 고치고 reference_updates 의 published 를 2020-12-28 로 넣는다 — 검증 열람에서 기사 승인일 2020-12-28, 국토교통부 공개일 2020-12-29 를 확인했다. f20 을 인용하는 문장의 기준일도 2020-12 로 쓴다.",
    "ref-1019·f14: 각주 발행일을 '미확인'에서 2023-07-26(개방일, 최종개방 2023-12-15)으로 고치고 reference_updates 의 published 를 2023-07-26 으로 넣으며, f14 문장의 기준일을 2023-12-15(최종개방) 기준으로 적는다 — AI Hub 소개 페이지에 개방일이 적혀 있다.",
    "f16: 3·6절에서 BIM→점유 격자·포즈 그래프 지도 생성은 이 영역의 접근법으로 쓰되, AMCL 대비 위치 추정 강건성은 로봇 자체 지능·제어 쪽 연구 결과로 밝히고 9절의 ROP 직접 범위로 서술하지 않는다 — 분류 원문 19장 경계(센서 인식·SLAM 은 연계 대상).",
    "f16·설계–준공 편차 용어: 'Scan-BIM 편차'를 처음 쓸 때 기존 용어집 '스캔 대 BIM 비교(Scan-vs-BIM)'에 연결하고, 새 용어 '설계–준공 편차'는 그와 다른 개념(비교 방법이 아니라 모델과 실제의 차이)임을 정의 문장에서 구분한다 — 용어집 중복 방지.",
    "f5·f6: 6·7절에서 로봇 지도–도면 정합과 대응점 기반 좌표 변환은 '도면을 기준 좌표로 쓰는 정합 절차'로 한정해 쓰고, 좌표계 통합 일반론은 10절에서 15. 지도·공간·위치 모델로 연결만 한다 — 게시된 15 페이지와의 중복 방지.",
    "5절 병원 사례(f7·f8): 여섯 항목 가운데 근거가 없는 시작 조건·완료·인계 칸은 '미확인'으로 두고 채우지 않는다. 기타 사례(f15)는 상용 운영이 아니라 대학 건물에서 한 위치 추정 연구 시험임과 '연계 대상'임을 밝히고, 근거 없는 칸은 '미확인'으로 둔다 — 브리프에 해당 근거가 없다. site_matrix_updates 는 실제로 채운 칸만 낸다.",
    "f19: 6절 제품 사례로만 쓰고 '[추정] 벤더 주장'을 병기한다. 현장 유형이 특정되지 않았으므로(공장·플랜트를 대상으로 한다는 벤더 설명뿐) 5절 사례와 site_matrix_updates 의 근거로 쓰지 않는다.",
    "f9·f10: 7절에서 IFC 4.3 내용이 buildingSMART 개발 브랜치(ifc4.3-main) 문서 기준이며 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있음을 밝힌다.",
    "f12: 약 90% 정밀도·재현율과 수십만 장 변환은 '저자 보고'로만 서술하고 일반적인 도면 인식 성능처럼 일반화하지 않는다 — 단일 출처, 교차 확인 없음.",
    "open_questions_new 1번: 질문 앞부분의 '주로 주거용 도면 기준인데'를 빼고 '보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가?' 형식으로 옮긴다 — 브리프에 근거 없는 전제이며 FloorPlanCAD(f13)는 상업 건물 도면도 포함한다.",
    "open_questions_new 2번: '승강기·계단·충전 위치처럼'에서 '승강기·계단'을 빼고 '충전 위치처럼 로봇 운영에 필요한 클래스'로 좁힌다 — 검증 열람에서 AI Hub 공간 라벨에 엘리베이터·엘리베이터홀·계단실이 있음을 확인했다(ref-1019).",
    "oq-126·oq-193: 해결로 바꾸지 않고 11절에 열림 상태로 싣는다 — 관련 근거(f6·f7, f16·f17)는 늘었지만 승인 주체·동기화 주기에 답하는 finding 이 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 1건, 교차 확인 0건. 강등: f20 사실 → 추정(기사 단독, 문구 불일치, 2020-12 발표로 이후 이행 미확인). 원문 미열람 출처: 없음(15건 모두 이번 검증에서 원본 또는 초록·소개 페이지를 열었다. 논문은 초록 기준). 주의: 사실 finding 은 모두 단일 출처다. Open-RMF 교통 편집기·플릿 어댑터 문서와 IFC 4.3 개발 브랜치 문서가 절차·정의의 근거이고, 평면도 인식 성능(약 90%)은 저자 보고다. 3·9절의 중요성과 책임 경계, 핵심 질문의 답('자동 초안 + 사람 확인·보정')은 구축자 추정이다. 현장 사례는 병원(타르투 대학병원) 1건과 기타(대학 건물 위치 추정 시험) 1건뿐이며, 물류창고·제조 공장·상업 시설 사례는 벤더 주장(f19) 말고는 확인되지 않았다. 검증 열람에서 ref-1024 발행일(2020-12-28)과 ref-1019 개방일(2023-07-26)을 확인해 정정을 지시했다. 미사용 출처 없음. 정정 요청 없음. oq-126·oq-193 해결 불인정(열림 유지). 검증 검색 1회를 썼다(리서치 13회와 합쳐 14/30)."
}
```

### runs/2026-09-30-03/pages.json

```json
{
  "run_id": "2026-09-30-03",
  "outline": [
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 650,
      "summary": "도면·BIM은 여러 제조사 로봇 지도를 묶는 공통 기준 좌표이자 문·승강기·충전 위치 같은 공용 자원 목록의 출발점이 될 수 있다. [추정][^ref-079][^ref-213]",
      "planned_findings": [
        "f22",
        "f1",
        "f8",
        "f21",
        "f20"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 750,
      "summary": "층 정렬 기준점, IFC 공간·공간 경계, 운송 요소, 점유 격자·포즈 그래프 지도, 설계–준공 편차, 도면 기준 지도 정합이 이 영역의 핵심 용어다. [사실][^ref-079][^ref-156][^ref-081]",
      "planned_findings": [
        "f3",
        "f9",
        "f10",
        "f16",
        "f5"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 900,
      "summary": "병원(타르투 대학병원 평면도 주석·격자 지도 정합·검체 운반)과 기타(대학 건물 BIM 기반 위치 추정 연구 시험, 연계 대상) 두 사례를 여섯 항목으로 정리하고 근거 없는 칸은 미확인으로 둔다. [사실][^ref-869][^ref-1017]",
      "planned_findings": [
        "f7",
        "f8",
        "f15"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1200,
      "summary": "평면도 인식, BIM·CAD에서 로봇 지도로 변환, 축척 보정과 도면 기준 정합, 설계–준공 편차 확인의 네 갈래로 접근법을 정리한다. [추정][^ref-1015][^ref-081][^ref-079]",
      "planned_findings": [
        "f12",
        "f13",
        "f16",
        "f18",
        "f1",
        "f2",
        "f3",
        "f5",
        "f6",
        "f19",
        "f17",
        "f21"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 450,
      "summary": "IFC 4.3의 IfcSpace·IfcTransportElement와 Open-RMF 교통 편집기·플릿 어댑터 좌표 변환이 이 영역과 직접 닿는다. [사실][^ref-156][^ref-079]",
      "planned_findings": [
        "f9",
        "f10",
        "f1",
        "f6"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 500,
      "summary": "CubiCasa5K·Raster-to-Vector·FloorPlanCAD·AI Hub 건축 도면 데이터와 BIM 기반 지도·위치 추정 연구, 병원 현장 시험이 대표 자료다. [사실][^ref-063][^ref-1019]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f7"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 700,
      "summary": "ROP는 도면 초안·축척·좌표 변환 등록·차이 표시와 사람 승인을 맡고, SLAM·위치 추정과 승강기 운행 제어, BIM 저작은 연계 대상으로 본다. [추정][^ref-153][^ref-1017]",
      "planned_findings": [
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 650,
      "summary": "8, 15, 16, 18, 22, 27, 28, 45, 55, 63번 영역(번호와 이름 함께)과 건축 도면 자동 인식 트랙에 연결한다. [추정][^ref-079]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "oq-126·oq-193을 열림으로 유지하고 비주거 도면 인식 성능, AI Hub 라벨 범위, 정합 대응점 기준, 공공 BIM 인계 절차의 새 질문 4건을 싣는다.",
      "planned_findings": [
        "f12",
        "f14",
        "f6",
        "f20"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(병원·기타 적용 사례, 평면도 인식·BIM 변환·도면 기준 정합·편차 확인, 책임 경계, 연결 10개 영역, 열린 질문 6건), 13절 각주 15건, 프런트매터 갱신"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area14-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 14. 도면·BIM에서 지도 만들기 의 \"6. 대표 접근법과 기술\" 절(1,924자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area14-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 14. 도면·BIM에서 지도 만들기 의 \"4. 핵심 개념과 용어\" 절(1,094자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area14-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 14. 도면·BIM에서 지도 만들기 의 \"8. 대표 연구와 자료\" 절(949자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area14-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 14. 도면·BIM에서 지도 만들기 의 \"11. 열린 질문\" 절(880자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area14-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 14. 도면·BIM에서 지도 만들기 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(825자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area14-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 14. 도면·BIM에서 지도 만들기 의 \"3. 왜 중요한가\" 절(747자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 14. 도면·BIM에서 지도 만들기 | 영역 심화: 3~11절 신규 작성(병원·기타 적용 사례, 평면도 인식·BIM 변환·도면 기준 정합), 1차 조건부 승인 수정 13건 이행 | run 2026-09-30-03",
  "index_updates": {
    "home_recent": "2026-09-30 — 14. 도면·BIM에서 지도 만들기: 영역 심화로 3~11절 작성(평면도 인식·BIM→지도 변환·도면 기준 정합, 병원 적용 사례)",
    "category_recent": "2026-09-30 — 14. 도면·BIM에서 지도 만들기: 영역 심화로 3~11절 작성, 15. 지도·공간·위치 모델과 좌표 정합 역할을 나눔",
    "area_recent": "2026-09-30 — 14. 도면·BIM에서 지도 만들기: 영역 심화 3~11절 신규 작성, 각주 15건, 새 열린 질문 4건"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "level-alignment-fiducial",
      "term_ko": "층 정렬 기준점",
      "term_en": "Fiducial (Level Alignment Fiducial)",
      "definition": "기둥처럼 여러 층에서 수직으로 같은 위치에 있다고 기대되는 지점에 찍는 표식으로, 대응시킨 기준점들로 층 사이의 이동·회전·축척 변환을 계산하는 데 쓴다.",
      "description": "Open-RMF 교통 편집기는 층마다 찍은 기준점을 대응시켜 층 사이 변환을 자동으로 계산한다.",
      "related_areas": [
        14,
        15
      ],
      "sources": [
        "ref-079"
      ]
    },
    {
      "action": "new",
      "slug": "space-boundary",
      "term_ko": "공간 경계",
      "term_en": "Space Boundary (IfcRelSpaceBoundary)",
      "definition": "IFC 에서 공간(IfcSpace)을 둘러싼 벽·슬래브 같은 물리적 요소나 가상 경계와 그 공간을 잇는 관계로, 공간의 범위와 인접 관계를 정의한다.",
      "description": "IFC 4.3 개발 저장소(ifc4.3-main) 문서 기준이며 게시판(ADD2)과 문구가 다를 수 있다.",
      "related_areas": [
        14,
        16
      ],
      "sources": [
        "ref-156"
      ]
    },
    {
      "action": "new",
      "slug": "as-planned-vs-as-built-deviation",
      "term_ko": "설계–준공 편차",
      "term_en": "As-planned vs As-built Deviation",
      "definition": "설계 단계에서 만든 건물 모델과 실제 지어진 상태 사이의 차이 자체로, BIM 을 로봇 지도로 쓸 때 위치 추정 오차의 원인이 된다.",
      "description": "스캔과 모델을 비교하는 방법인 스캔 대 BIM 비교(Scan-vs-BIM)와 달리, 이 용어는 비교 방법이 아니라 모델과 실제 사이의 차이를 가리킨다. BIM 과 현실의 차이(Scan-BIM 편차)는 가구·잡동사니와 이 설계–준공 차이에서 생긴다고 보고됐다.",
      "related_areas": [
        14,
        16,
        18
      ],
      "sources": [
        "ref-081"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 교통 편집기 장. 평면도 이미지 위 벽·문·승강기·차선·충전 위치 주석, 측정선으로 축척 설정, 기준점(fiducial)으로 층 정렬, 로봇 지도 레이어 정합을 설명한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-153",
      "org": "Open Robotics",
      "title": "Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "플릿 어댑터 작성 튜토리얼. 로봇 좌표계와 RMF 좌표계의 대응 지점(reference_coordinates, 4개 이상 권장)으로 nudged 라이브러리가 회전·축척·이동 변환을 추정하는 방법을 설명한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-156",
      "org": "buildingSMART International",
      "title": "IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main)",
      "published": null,
      "url": "https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IFC 4.3 의 공간 요소 IfcSpace 정의(기능을 가진 경계 있는 면적·부피, 층 소속, 공간 경계 관계). 개발 브랜치 문서라 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-213",
      "org": "buildingSMART International",
      "title": "IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main)",
      "published": null,
      "url": "https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IFC 4.3 의 운송 요소 IfcTransportElement 정의. 승강기·에스컬레이터·무빙워크를 포함한다. 개발 브랜치 문서라 게시판과 문구가 다를 수 있다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-063",
      "org": "Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J.",
      "title": "CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis",
      "published": "2019-04",
      "url": "https://arxiv.org/abs/1904.01920",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "평면도 이미지 5,000장을 80개 이상 범주로 다각형 주석한 데이터셋과 다중 작업 CNN 평면도 해석 모델. arXiv 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1015",
      "org": "Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017)",
      "title": "Raster-to-Vector: Revisiting Floorplan Transformation",
      "published": "2017",
      "url": "https://art-programmer.github.io/floorplan-transformation.html",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "래스터 평면도를 접합점 검출 신경망과 정수 계획법으로 벡터 평면도로 바꾸는 방법. 약 90% 정밀도·재현율은 저자 보고. 저자 프로젝트 페이지 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-067",
      "org": "Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021)",
      "title": "FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting",
      "published": "2021-05",
      "url": "https://arxiv.org/abs/2105.07147",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "주거·상업 건물 벡터 CAD 평면도 1만 장 이상, 30개 범주의 파놉틱 심볼 스포팅 데이터셋과 CNN–GCN 방법. arXiv 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1017",
      "org": "Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021)",
      "title": "Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization",
      "published": "2021",
      "url": "https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IFC BIM 의 의미 요소를 로봇 세계 모델로 바꿔 2D LiDAR 위치 추정에 쓰는 방법. 대형 대학 건물에서 시험. 에인트호번 공대 연구 포털 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-081",
      "org": "Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022)",
      "title": "Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2308.05443",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "BIM 에서 구조 요소만의 2D 점유 격자 지도를 자동 생성해 포즈 그래프 지도로 바꾸고 Scan-BIM 편차에 강건한 위치 추정을 보인 연구. arXiv 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1019",
      "org": "AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주)",
      "title": "건축 도면 데이터",
      "published": "2023-07-26",
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2022년 구축된 건축 도면 인공지능 학습용 데이터(48,033장, 구조·공간·객체 라벨과 OCR). 개방일 2023-07-26, 최종개방 2023-12-15. 데이터 소개 페이지를 열어 확인했다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-817",
      "org": "모빌리오(Mobilio Robotics)",
      "title": "[최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션)",
      "published": "2026-08-24",
      "url": "https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "산업용 순찰 로봇 웹 관제 솔루션 소개 글. LiDAR 지도와 CAD·BIM 도면의 기준점 정합 기능을 주장한다(벤더 주장, 독립 확인 없음). 제목 전체는 확인하지 못했다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R. 외 (Frontiers in Robotics and AI)",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "타르투 대학병원에서 Open-RMF 기반 이기종 로봇 플릿으로 검체 운반을 시험한 현장 연구. 평면도 주석과 로봇 격자 지도 정합 절차를 기술한다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-083",
      "org": "Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv)",
      "title": "Generation of Indoor Open Street Maps for Robot Navigation from CAD Files",
      "published": "2025-07",
      "url": "https://arxiv.org/abs/2507.00552",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "건축 CAD 파일에서 로봇 항법용 계층형 위상·거리 OSM 실내 지도를 자동 생성하는 파이프라인(프리프린트, 2026-03 개정). arXiv 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-221",
      "org": "Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023)",
      "title": "BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2408.15870",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "BIM 에서 만든 세션 데이터를 다중 세션 SLAM 으로 실제 LiDAR 와 정렬하고 BIM 에 없는 요소를 검출하는 방법. ISARC 2023 발표, arXiv 게시 2024-08. 초록 기준.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1024",
      "org": "엔지니어링데일리",
      "title": "\"설계부터 100% 도입\" 건설산업 BIM 활성화 로드맵 공개",
      "published": "2020-12-28",
      "url": "https://www.engdaily.com/news/articleView.html?idxno=12613",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "국토교통부 건설산업 BIM 활성화 로드맵(설계부터 BIM 100% 도입, 조사·설계·발주·조달·시공·감리·유지관리 등 전 생애주기 적용, LH 공동주택 의무화 후 확대)을 전한 기사. 기사 승인일 2020-12-28, 국토교통부 공개일 2020-12-29. 국토교통부 원문은 열지 못했다.",
      "cited_by": [
        "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가?",
      "areas": [
        14,
        45
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가?",
      "areas": [
        14,
        45
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 벤더 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가?",
      "areas": [
        14,
        15,
        55
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가?",
      "areas": [
        14,
        22
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    },
    {
      "site_type": "기타",
      "item": "작업 대상",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#5-적용-사례-현장-유형-명시",
      "title": "14. 도면·BIM에서 지도 만들기"
    }
  ],
  "standards_updates": [],
  "additional_research_requests": [
    "5절 적용 사례: 물류창고·제조 공장·상업 시설에서 도면·BIM 기반 로봇 지도를 실제로 쓴 독립 출처 사례(벤더 주장 외)가 필요하다 — 현재 병원 1건과 기타(연구 시험) 1건뿐이다.",
    "5절 병원 사례: 타르투 대학병원 시험의 시작 조건(검체 운반 요청 방식)과 완료·인계(수령 확인) 근거가 필요하다 — 두 칸을 미확인으로 두었다.",
    "9·11절: 도면–로봇 지도 정합 결과를 누가 언제 승인·확정하는지(oq-126) 다룬 제품 문서·현장 절차 자료가 필요하다.",
    "3절: 국토교통부 BIM 활성화 로드맵 원문 보도자료(2020-12-29)와 이후 이행 상황 자료가 필요하다 — 현재 기사 단독 출처라 [추정]으로 강등했다.",
    "7절: IFC 4.3 ADD2 게시판(또는 ISO 16739-1:2024)의 IfcSpace·IfcTransportElement 문구 확인이 필요하다 — 현재 개발 저장소 문서 기준이다.",
    "11절: 건설 현장 등 변하는 공간에서 로봇 지도와 BIM 의 동기화 주기·국내 사례(oq-193) 자료가 필요하다.",
    "다음 실행 후보: 15. 지도·공간·위치 모델 페이지에 대응점 기반 좌표 변환(reference_coordinates, nudged) 반영, 45. 문서·도면·장면 이해 페이지에 CubiCasa5K·Raster-to-Vector·FloorPlanCAD·AI Hub 건축 도면 데이터 반영."
  ],
  "fixes_applied": [
    "f20 강등 — 3절의 국토교통부 BIM 로드맵 문장을 [추정]으로 쓰고 '조사·설계·발주·조달·시공·감리·유지관리 등 전 생애주기', 'LH 공동주택'으로 고쳤으며 '2020-12 발표 기준이며 이후 이행 상황은 미확인'을 덧붙였다.",
    "ref-1024 정정 — 13절 각주의 발행일을 2020-12-28, 제목을 '\"설계부터 100% 도입\" 건설산업 BIM 활성화 로드맵 공개'로 고치고 reference_updates 의 published 를 2020-12-28 로 넣었으며, 3절 문장에 기사 날짜(2020-12-28)와 2020-12 기준을 적었다.",
    "ref-1019·f14 정정 — 13절 각주 발행일을 2023-07-26 으로, reference_updates 의 published 를 2023-07-26 으로 넣고, 8절 AI Hub 문장의 기준일을 '2023-12-15 최종개방 기준'으로 적었다.",
    "f16 경계 — 6절에서 BIM→점유 격자·포즈 그래프 지도 생성은 접근법으로 쓰고, AMCL 대비 강건성은 별도 문장으로 로봇 자체 지능·제어 쪽 연구 결과이자 연계 대상이라고 밝혔으며, 9절 직접 범위에는 넣지 않고 연계 열에 '위치 추정과 그 성능'으로만 두었다.",
    "Scan-BIM 편차 용어 — 4절에서 'Scan-BIM 편차'를 처음 쓰는 자리에 용어집 스캔 대 BIM 비교(Scan-vs-BIM) 링크를 달고, 설계–준공 편차가 비교 방법이 아니라 모델과 실제의 차이 자체임을 본문과 glossary_updates 정의·설명에서 구분했다.",
    "f5·f6 중복 방지 — 6절 '축척 보정과 도면 기준 정합' 소절 첫머리에 도면을 기준 좌표로 쓰는 정합 절차로 한정한다고 밝히고 7절 표도 '도면 기준 좌표계 사이 변환'으로 적었으며, 좌표계 통합 일반론은 10절에서 15. 지도·공간·위치 모델로 연결만 했다.",
    "5절 사례 칸 — 병원 사례의 시작 조건·완료·인계를 '미확인'으로 두고, 기타 사례는 상용 운영이 아닌 대학 건물 위치 추정 연구 시험이자 연계 대상임을 제목·서술에 밝히고 근거 없는 시작 조건·제약·완료·인계를 '미확인'으로 두었으며, site_matrix_updates 는 실제로 채운 칸(병원 4칸, 기타 3칸)만 냈다.",
    "f19 — 6절 제품 사례로만 쓰고 '[추정] 벤더 주장'을 병기했으며, 5절 사례와 site_matrix_updates 근거로 쓰지 않았다.",
    "f9·f10 — 7절 표 아래에 IFC 4.3 두 행이 buildingSMART 개발 저장소(ifc4.3-main) 문서 기준이며 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있음을 밝혔다.",
    "f12 — 6절에서 약 90% 정밀도·재현율과 수십만 장 변환을 '저자들이 보고했으며 교차 확인되지 않은 저자 보고'로만 서술하고 일반화하지 않았다.",
    "open_questions_new 1번 — '주로 주거용 도면 기준인데' 전제를 빼고 '보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가?' 형식으로 11절과 open_question_updates 에 옮겼다.",
    "open_questions_new 2번 — '승강기·계단'을 빼고 '충전 위치처럼 로봇 운영에 필요한 클래스'로 좁혀 11절과 open_question_updates 에 옮겼다.",
    "oq-126·oq-193 — 해결로 바꾸지 않고 11절에 '상태: 열림'으로 싣고 확인된 근거와 아직 답하지 못한 부분을 한 문장씩 덧붙였으며, open_question_updates 에 상태 변경을 내지 않았다.",
    "분량 초과 자동 분리: 14. 도면·BIM에서 지도 만들기 본문 9,434자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,887자"
  ]
}
```

### runs/2026-09-30-03/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area14-s6.md (1,924자)
    - docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area14-s4.md (1,094자)
    - docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area14-s8.md (949자)
    - docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area14-s11.md (880자)
    - docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area14-s10.md (825자)
    - docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area14-s3.md (747자)
```

### runs/2026-09-30-03/pages/categories/space-and-map-model/maps-from-floor-plans-and-bim.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기"
type: area
category: "D. 공간·지도 모델"
area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [평면도 인식, BIM, IFC, 지도 정합, 층 정렬 기준점, 설계–준공 편차]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-079, ref-153, ref-156, ref-213, ref-063, ref-1015, ref-067, ref-1017, ref-081, ref-1019, ref-817, ref-869, ref-083, ref-221, ref-1024]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [D. 공간·지도 모델](index.md) › 14. 도면·BIM에서 지도 만들기

# 14. 도면·BIM에서 지도 만들기

!!! info "소속 대분류"
    [D. 공간·지도 모델](index.md) — 핵심 질문:
    로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

건물 도면과 건물 정보 모델링(Building Information Modeling, BIM) 모델은 여러 제조사의 로봇 지도를 묶는 공통 기준 좌표이자, 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점이 될 수 있다. [추정][^ref-079][^ref-213]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 왜 중요한가](../../topics/2026/2026-09-30-area14-s3.md)에 있다.

## 4. 핵심 개념과 용어

도면·BIM 과 로봇 지도를 잇는 데는 층을 맞추는 기준점, 건물 모델의 공간·운송 요소, 로봇용 지도 형식, 모델과 현실의 차이라는 개념이 쓰인다. [사실][^ref-079][^ref-156][^ref-081]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area14-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

확인한 자료에서 도면 기반 지도를 현장에 쓴 사례는 병원 현장 시험 1건이며, 대학 건물의 BIM 기반 위치 추정 연구 시험 1건을 연계 대상 사례로 함께 싣는다. [사실][^ref-869][^ref-1017] 물류창고·제조 공장·상업 시설 사례는 이번 자료에서 확인되지 않았다.

**현장 유형:** 병원

**사례:** 병원 평면도 주석과 로봇 격자 지도 정합으로 검체 운반 준비

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병원 건축 평면도(공간), 로봇이 만든 격자 지도(정보), 중환자실에서 검사실로 옮기는 시간이 중요한 혈액 검체(물건) [사실][^ref-869] |
| 수행 자원 | 원격 조작한 PAL Robotics TIAGo 로봇이 동시적 위치 추정 및 지도 작성(Simultaneous Localization and Mapping, SLAM)으로 격자 지도를 만들고, Open-RMF 교통 편집기로 평면도에 벽·문·차선·충전소·주요 위치를 주석한 뒤 격자 지도를 평면도에 정합했다 [사실][^ref-869] |
| 제약 | 무선 주파수 식별(Radio-Frequency Identification, RFID)·근접 센서로 여는 반자동 문 두 곳을 통과해야 했다 [사실][^ref-869] |
| 완료·인계 | 미확인 |
| 예외·성과 | 넓은 구역을 한 번에 매핑하면 누적 불확실성으로 지도가 비틀리기 쉬워, 작은 구역으로 나눠 매핑하고 하위 지도를 손으로 합치는 편이 더 정확했다. 처리량·시간·비용 영향은 미확인 [사실][^ref-869] |

Valner 외(2022-08)가 보고한 에스토니아 타르투 대학병원 현장 시험에서는 평면도와 격자 지도 두 좌표 표현 사이의 변환을 정한 뒤 그 지도로 검체 운반을 수행했다. [사실][^ref-869] 이 영역은 여섯 항목 가운데 작업 대상(평면도·격자 지도)과 수행 자원(주석·정합 작업), 예외·성과(매핑 오차 대처)에 주로 관여한다. [추정][^ref-869] 시작 조건과 완료·인계를 적은 근거는 이번 자료에 없어 미확인으로 둔다.

**현장 유형:** 기타

**사례:** 대학 건물에서 BIM 을 사전 지도로 쓰는 로봇 위치 추정 연구 시험(연계 대상)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | IFC 형식 BIM 의 의미 요소를 바꾼 로봇용 세계 모델과 이를 저장한 공간 데이터베이스(정보) [사실][^ref-1017] |
| 수행 자원 | 2D 라이다(Light Detection and Ranging, LiDAR)와 주행거리계만 가진 로봇이 주변 구조 요소를 질의해 특징 검출기를 설정하고 그래프 기반 방법으로 위치를 추정했다 [사실][^ref-1017] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | BIM 이 있는 대형 대학 건물에서 로봇이 자세를 추적할 수 있음을 보였다. 실패 시 복구 주체와 처리량·시간·비용 영향은 미확인 [사실][^ref-1017] |

이 사례는 상용 운영이 아니라 Hendrikx 외(ICRA 2021)가 대형 대학 건물에서 한 위치 추정 연구 시험이다. [사실][^ref-1017] BIM 을 사전 지도로 쓰는 위치 추정은 로봇 자체 지능·제어에 속하는 연계 대상이며, 이 영역과 맞닿는 부분은 같은 BIM 에서 구조 요소·공간 정보를 가져오는 단계다. [추정][^ref-1017]

## 6. 대표 접근법과 기술

도면·BIM 에서 로봇 지도를 만드는 기술은 평면도 인식, BIM·CAD 변환, 축척 보정과 도면 기준 정합, 설계–준공 편차 확인으로 나뉘며, 앞의 둘은 연구 수준에서 자동화가 진행됐고 뒤의 둘은 사람 입력과 확인에 기대는 부분이 크다. [추정][^ref-1015][^ref-081][^ref-079][^ref-153]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area14-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 직접 닿는 표준·오픈소스는 공간·운송 요소를 정의한 IFC 4.3 과, 도면 주석·좌표 변환을 다루는 [Open-RMF](../../glossary/open-rmf.md) 도구다. [사실][^ref-156][^ref-079]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| IFC 4.3 IfcSpace·IfcRelSpaceBoundary | 표준 | 공간과 그 경계를 가져와 층별 공간 목록을 만드는 입력 요소 [사실][^ref-156] | buildingSMART 개발 저장소 문서 |
| IFC 4.3 IfcTransportElement | 표준 | 승강기·에스컬레이터·무빙워크를 공용 자원 후보로 가져오는 입력 요소 [사실][^ref-213] | buildingSMART 개발 저장소 문서 |
| Open-RMF 교통 편집기(traffic-editor) | 오픈소스 | 평면도 위 벽·문·승강기·차선·충전 위치 주석, 측정선 축척, 층 정렬 기준점, 로봇 지도 레이어 정합 [사실][^ref-079] | Open Robotics 문서 |
| Open-RMF 플릿 어댑터 reference_coordinates 와 nudged | 오픈소스 | 로봇 좌표계와 도면 기준 좌표계 사이 대응점 기반 변환 추정 [사실][^ref-153] | Open Robotics 튜토리얼 |

IFC 4.3 두 행은 buildingSMART 개발 저장소(ifc4.3-main) 문서를 기준으로 했으며, 게시된 IFC 4.3 ADD2 판과 문구가 다를 수 있다. [사실][^ref-156] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 대표 자료는 평면도 인식 데이터셋·방법, BIM 기반 지도·위치 추정 연구, 병원 현장 시험이다. [사실][^ref-063][^ref-081][^ref-869]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 대표 연구와 자료](../../topics/2026/2026-09-30-area14-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사별 로봇 지도와 도면 기준 공통 좌표 사이 변환을 등록·관리하고, 도면과 현장의 차이를 표시해 사람이 확인·승인하게 한다 [추정][^ref-153][^ref-081] | 연계 대상: 로봇의 SLAM·LiDAR 위치 추정(BIM 을 사전 지도로 쓰는 위치 추정과 그 성능 포함) [추정][^ref-1017][^ref-221] |
| 시설·설비 제어 | 도면·IFC 에서 문·승강기·충전 위치 초안을 만들어 공용 자원 목록에 올린다 [추정][^ref-079][^ref-213] | 연계 대상: 승강기 운행 제어 [추정][^ref-213] |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 평면도·CAD·IFC 를 받아 공간·문·승강기·충전 위치 초안과 공용 자원 목록을 만들고, 층별 축척과 층 간 기준점을 설정하며, 제조사별 로봇 지도와 공통 좌표 사이 변환을 등록·관리하고, 도면과 현장의 차이를 표시해 사람이 확인·승인하게 하는 일로 보인다. [추정][^ref-079][^ref-153][^ref-156][^ref-213][^ref-081] 정합 결과를 누가 언제 확정하는지는 아직 확인되지 않았다(열린 질문 oq-126).

로봇의 SLAM·LiDAR 위치 추정은 로봇 자체 지능·제어에, 승강기 운행 제어는 시설·설비 제어에 속하고, BIM 모델의 저작·갱신은 건물 소유자·설계·시공 측 체계에 속한다. 따라서 이종 제조사를 잇는 ROP 는 이들로부터 모델·지도를 받아 공통 공간 모델로 정합하고 차이를 확인하는 인터페이스를 맡을 것으로 보인다. [추정][^ref-1017][^ref-081][^ref-221][^ref-213][^ref-1024]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

경계 기준 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 좌표 정렬·지도 관리·도면 해석 AI·설비 연동·설치 과정과 이어진다. [추정][^ref-079]

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area14-s10.md)에 있다.

## 11. 열린 질문

이 영역에는 정합 결과의 승인 주체와 변하는 현장의 BIM 동기화라는 기존 질문 두 건이 열려 있고, 이번 조사에서 새 질문 네 건이 생겼다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [14. 도면·BIM에서 지도 만들기 — 열린 질문](../../topics/2026/2026-09-30-area14-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-30
[^ref-156]: buildingSMART International, IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md, 접근일 2026-09-30
[^ref-213]: buildingSMART International, IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md, 접근일 2026-09-30
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-30
[^ref-1015]: Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017), Raster-to-Vector: Revisiting Floorplan Transformation, 2017, https://art-programmer.github.io/floorplan-transformation.html, 접근일 2026-09-30
[^ref-1017]: Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021), Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization, 2021, https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30
[^ref-221]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023), BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR, 2024-08, https://arxiv.org/abs/2408.15870, 접근일 2026-09-30
[^ref-1024]: 엔지니어링데일리, "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개, 2020-12-28, https://www.engdaily.com/news/articleView.html?idxno=12613, 접근일 2026-09-30
```

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기"
type: area
category: "D. 공간·지도 모델"
area_no: 14
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [D. 공간·지도 모델](index.md) › 14. 도면·BIM에서 지도 만들기

# 14. 도면·BIM에서 지도 만들기

!!! info "소속 대분류"
    [D. 공간·지도 모델](index.md) — 핵심 질문:
    로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

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

### runs/2026-09-30-03/pages/topics/2026/2026-09-30-area14-s6.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기 — 대표 접근법과 기술"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-079, ref-153, ref-063, ref-1015, ref-067, ref-081, ref-817, ref-083, ref-221]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#6
---

[홈](../../index.md) › [주제](../index.md) › 14. 도면·BIM에서 지도 만들기 — 대표 접근법과 기술

# 14. 도면·BIM에서 지도 만들기 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 도면·BIM 에서 로봇 지도를 만드는 기술은 평면도 인식, BIM·CAD 변환, 축척 보정과 도면 기준 정합, 설계–준공 편차 확인으로 나뉘며, 앞의 둘은 연구 수준에서 자동화가 진행됐고 뒤의 둘은 사람 입력과 확인에 기대는 부분이 크다. [추정][^ref-1015][^ref-081][^ref-079][^ref-153]
- 이 페이지는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

도면·BIM 에서 로봇 지도를 만드는 기술은 평면도 인식, BIM·CAD 변환, 축척 보정과 도면 기준 정합, 설계–준공 편차 확인으로 나뉘며, 앞의 둘은 연구 수준에서 자동화가 진행됐고 뒤의 둘은 사람 입력과 확인에 기대는 부분이 크다. [추정][^ref-1015][^ref-081][^ref-079][^ref-153]

### 평면도 인식

Liu 외(ICCV 2017)의 Raster-to-Vector 는 신경망으로 벽 모서리·문 끝점 같은 접합점을 찾고 정수 계획법으로 이를 벽선·문선·아이콘 상자로 묶어 위상·기하가 일관된 벡터 평면도를 만든다([래스터–벡터 변환](../../glossary/raster-to-vector-conversion.md)). [사실][^ref-1015] 저자들은 자체 평가에서 정밀도·재현율 약 90%를 얻고 실제 서비스용 평면도 이미지 수십만 장을 벡터로 바꿨다고 보고했으며, 이 수치는 교차 확인되지 않은 저자 보고다. [사실][^ref-1015]

Fan 외(ICCV 2021)의 FloorPlanCAD 는 주거·상업 건물의 벡터 CAD 평면도 1만 장 이상을 30개 범주로 선 단위 주석하고, 사물 인스턴스와 영역 의미를 함께 찾는 [파놉틱 심볼 스포팅](../../glossary/panoptic-symbol-spotting.md) 과제와 합성곱 신경망(Convolutional Neural Network, CNN)–그래프 합성곱 신경망(Graph Convolutional Network, GCN) 결합 방법을 제시했다. [사실][^ref-067] 이런 [평면도 인식](../../glossary/floor-plan-recognition.md)은 L. AI·학습 기술의 45. 문서·도면·장면 이해에 속하는 방법을 이 영역에 적용한 것이다. [추정][^ref-063]

### BIM·CAD 에서 로봇 지도로 변환

Vega Torres 외(ECPPM 2022)는 복잡한 BIM 에서 구조 요소만 담은 2D 점유 격자 지도를 자동 생성하고 이를 포즈 그래프 지도로 바꾸는 방법을 제안했다. [사실][^ref-081] 같은 연구는 이 지도로 한 위치 추정이 변화·동적 환경에서 일반 적응형 몬테카를로 위치 추정(Adaptive Monte Carlo Localization, AMCL)보다 강건했다고 보고했다. [사실][^ref-081] 이 위치 추정 성능은 로봇 자체 지능·제어 쪽 연구 결과로, ROP 직접 범위가 아니라 연계 대상으로 본다. [추정][^ref-081]

Zhang 외(2025-07 프리프린트, 2026-03 개정)는 건축 CAD 파일에서 구조 요소를 추출하고 AreaGraph 기반 위상 분할로 이동 가능한 공간을 나눈 뒤 CAD 의 문자 라벨을 넣고 여러 층을 합쳐, 로봇 항법용 계층형 위상·거리 OpenStreetMap 실내 지도([위상 지도](../../glossary/topological-map.md))를 자동 생성하는 파이프라인과 그래픽 사용자 인터페이스(Graphical User Interface, GUI)를 공개했다. [사실][^ref-083]

### 축척 보정과 도면 기준 정합

여기서는 도면을 기준 좌표로 쓰는 정합 절차만 다루고, 좌표계 통합 일반론은 [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md)에서 다룬다. Open-RMF 교통 편집기는 평면도 이미지를 배경으로 불러오고, 주석을 이미지 왼쪽 위 원점의 픽셀 좌표로 만든다. [사실][^ref-079] 축척은 축척 막대처럼 실제 거리를 아는 두 점 사이에 측정선을 긋고 실제 길이를 미터로 넣어 층별 픽셀–미터 비율로 정한다. [사실][^ref-079] 여러 층은 층 정렬 기준점으로 맞추고, 로봇이 만든 지도는 레이어로 불러와 축척·이동·회전 변환을 주어 평면도와 겹치게 한다. [사실][^ref-079]

[플릿 어댑터](../../glossary/fleet-adapter.md) 튜토리얼은 로봇 좌표계와 교통 편집기 좌표계가 다르면 두 좌표계의 대응 지점 쌍(reference_coordinates)을 설정 파일에 적게 하고 최소 4개를 권장하며, nudged 라이브러리가 회전·축척·이동 변환을 추정해 명령 좌표를 자동으로 바꾼다. [사실][^ref-153]

모빌리오는 자사 산업용 순찰 로봇 관제 솔루션이 기둥·모서리 같은 기준점 3개 이상으로 2D LiDAR 지도를 CAD·BIM 도면에 정합하고 회전각·크기를 미세 조정해 로봇 위치를 도면 위에 보여 주며, 공장·플랜트를 대상으로 한다고 설명한다. [추정] 벤더 주장[^ref-817]

### 설계–준공 편차 확인

연계 대상: Vega Torres 외의 BIM-SLAM(ISARC 2023)은 BIM 에서 포즈 그래프 지도·기술자 같은 세션 데이터를 먼저 만들고 다중 세션 앵커링으로 실제 LiDAR 측정과 맞추며, BIM 에 없는 요소를 찾아 표면으로 재구성해 설계 모델과 실제 실내 상태의 차이를 드러내고 로봇의 초기 자세 없이도 BIM 에 정렬된 지도를 만든다. [사실][^ref-221]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-30
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-30
[^ref-1015]: Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017), Raster-to-Vector: Revisiting Floorplan Transformation, 2017, https://art-programmer.github.io/floorplan-transformation.html, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30
[^ref-817]: 모빌리오(Mobilio Robotics), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 … (모빌리오 통합 대시보드 솔루션), 2026-08-24, https://mobilio.io/ko/%EB%AA%A8%EB%B9%8C%EB%A6%AC%EC%98%A4-%ED%86%B5%ED%95%A9-%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C-%EC%86%94%EB%A3%A8%EC%85%98, 접근일 2026-09-30
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv), Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07, https://arxiv.org/abs/2507.00552, 접근일 2026-09-30
[^ref-221]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023), BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR, 2024-08, https://arxiv.org/abs/2408.15870, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-03 | 14. 도면·BIM에서 지도 만들기 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-03/pages/topics/2026/2026-09-30-area14-s4.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기 — 핵심 개념과 용어"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-079, ref-156, ref-213, ref-081]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#4
---

[홈](../../index.md) › [주제](../index.md) › 14. 도면·BIM에서 지도 만들기 — 핵심 개념과 용어

# 14. 도면·BIM에서 지도 만들기 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 도면·BIM 과 로봇 지도를 잇는 데는 층을 맞추는 기준점, 건물 모델의 공간·운송 요소, 로봇용 지도 형식, 모델과 현실의 차이라는 개념이 쓰인다. [사실][^ref-079][^ref-156][^ref-081]
- 이 페이지는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

도면·BIM 과 로봇 지도를 잇는 데는 층을 맞추는 기준점, 건물 모델의 공간·운송 요소, 로봇용 지도 형식, 모델과 현실의 차이라는 개념이 쓰인다. [사실][^ref-079][^ref-156][^ref-081]

- **층 정렬 기준점(fiducial)** — 기둥처럼 여러 층에서 수직으로 같은 위치에 있을 것으로 기대되는 지점에 층마다 찍는 표식이며, Open-RMF 교통 편집기는 대응한 기준점으로 층 사이의 이동·회전·축척 변환을 자동으로 계산한다. [사실][^ref-079]
- **공간(IfcSpace)과 공간 경계(IfcRelSpaceBoundary)** — [산업 기초 클래스(Industry Foundation Classes, IFC)](../../glossary/ifc.md) 4.3 에서 IfcSpace 는 건물 안에서 특정 기능을 제공하는, 실제 또는 이론상 경계로 둘러싸인 면적·부피다. 층(외부 공간은 site)에 IfcRelAggregates 로 속해 공간 계층을 이루고, IfcRelSpaceBoundary 로 물리적·가상 경계가 정의된다. [사실][^ref-156]
- **운송 요소(IfcTransportElement)** — 시설 안에서 사람·동물·물품을 옮기는 요소를 일반화한 IFC 4.3 요소로, 승강기·에스컬레이터·무빙워크를 포함하며 PredefinedType 이나 IfcTransportElementType 으로 구분한다. [사실][^ref-213]
- **점유 격자 지도와 포즈 그래프 지도** — BIM 에서 구조 요소만 담은 2D [점유 격자 지도(Occupancy Grid Map, OGM)](../../glossary/occupancy-grid-map.md)를 자동 생성하고 이를 포즈 그래프 지도로 바꾸는 연구가 있다. [사실][^ref-081]
- **설계–준공 편차(as-planned vs as-built deviation)** — BIM 과 현실 사이의 차이인 Scan-BIM 편차([스캔 대 BIM 비교(Scan-vs-BIM)](../../glossary/scan-vs-bim.md)로 드러나는 차이)는 가구·잡동사니뿐 아니라 설계 모델과 준공 상태의 차이에서도 생긴다. [사실][^ref-081] 이 페이지에서 설계–준공 편차는 스캔과 모델을 비교하는 방법이 아니라, 설계 모델과 실제 지어진 상태 사이의 차이 자체를 가리킨다. [의견][^ref-081]
- **도면 기준 지도 정합** — [지도 정합(map alignment)](../../glossary/map-alignment.md) 가운데 이 영역이 다루는 것은 로봇이 만든 지도를 평면도 위 레이어로 불러와 축척·이동·회전 변환으로 겹치게 맞추는 도면 기준 절차다. [사실][^ref-079]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-156]: buildingSMART International, IfcSpace — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md, 접근일 2026-09-30
[^ref-213]: buildingSMART International, IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-03 | 14. 도면·BIM에서 지도 만들기 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-03/pages/topics/2026/2026-09-30-area14-s8.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기 — 대표 연구와 자료"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-063, ref-1015, ref-067, ref-1017, ref-081, ref-1019, ref-869, ref-083, ref-221]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#8
---

[홈](../../index.md) › [주제](../index.md) › 14. 도면·BIM에서 지도 만들기 — 대표 연구와 자료

# 14. 도면·BIM에서 지도 만들기 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 대표 자료는 평면도 인식 데이터셋·방법, BIM 기반 지도·위치 추정 연구, 병원 현장 시험이다. [사실][^ref-063][^ref-081][^ref-869]
- 이 페이지는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 대표 자료는 평면도 인식 데이터셋·방법, BIM 기반 지도·위치 추정 연구, 병원 현장 시험이다. [사실][^ref-063][^ref-081][^ref-869]

- Kalervo 외, CubiCasa5K(2019) — 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 주석한 데이터셋과, 휴리스틱·저수준 픽셀 연산 대신 개선된 다중 작업 합성곱 신경망으로 평면도를 해석하는 방법. [사실][^ref-063]
- Liu 외, Raster-to-Vector(ICCV 2017) — 래스터 평면도를 벡터 평면도로 바꾸는 방법(6절). [사실][^ref-1015]
- Fan 외, FloorPlanCAD(ICCV 2021) — CAD 평면도 파놉틱 심볼 스포팅 데이터셋(6절). [사실][^ref-067]
- AI Hub, 건축 도면 데이터(2022년 구축, 주관기관 에이치씨아이플러스, 2023-12-15 최종개방 기준) — 평면도 41,556장을 포함한 건축 도면 48,033장에 출입문·창호·벽체 등 구조 8종, 거실·침실·주방·현관·화장실 등 공간 12종, 객체 5종 라벨과 문자 인식(Optical Character Recognition, OCR) 304,462건을 담은 국내 학습용 데이터. [사실][^ref-1019]
- Vega Torres 외, BIM 기반 점유 격자·포즈 그래프 지도(ECPPM 2022)와 BIM-SLAM(ISARC 2023) — BIM 에서 로봇 지도를 만들고 현실과의 차이를 드러내는 연구(6절). [사실][^ref-081][^ref-221]
- Zhang 외, CAD 파일에서 실내 OpenStreetMap 생성(2025) — CAD 에서 계층형 위상·거리 지도를 자동 생성하는 프리프린트(6절). [사실][^ref-083]
- 연계 대상: Hendrikx 외(ICRA 2021) — IFC 의미 요소를 로봇 세계 모델로 바꿔 2D LiDAR 위치 추정에 쓴 연구(5절). [사실][^ref-1017]
- Valner 외(Frontiers in Robotics and AI, 2022-08) — 타르투 대학병원 이기종 로봇 플릿 현장 시험, 평면도 주석과 격자 지도 정합 절차 기술(5절). [사실][^ref-869]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-30
[^ref-1015]: Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017), Raster-to-Vector: Revisiting Floorplan Transformation, 2017, https://art-programmer.github.io/floorplan-transformation.html, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1017]: Hendrikx, R. W. M., Pauwels, P., Torta, E., Bruyninckx, H. P. J., & van de Molengraft, M. J. G. (ICRA 2021), Connecting Semantic Building Information Models and Robotics: An application to 2D LiDAR-based localization, 2021, https://research.tue.nl/en/publications/connecting-semantic-building-information-models-and-robotics-an-a/, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30
[^ref-1019]: AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주), 건축 도면 데이터, 2023-07-26, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv), Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07, https://arxiv.org/abs/2507.00552, 접근일 2026-09-30
[^ref-221]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023), BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR, 2024-08, https://arxiv.org/abs/2408.15870, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-03 | 14. 도면·BIM에서 지도 만들기 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-03/pages/topics/2026/2026-09-30-area14-s11.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기 — 열린 질문"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#11
---

[홈](../../index.md) › [주제](../index.md) › 14. 도면·BIM에서 지도 만들기 — 열린 질문

# 14. 도면·BIM에서 지도 만들기 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에는 정합 결과의 승인 주체와 변하는 현장의 BIM 동기화라는 기존 질문 두 건이 열려 있고, 이번 조사에서 새 질문 네 건이 생겼다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에는 정합 결과의 승인 주체와 변하는 현장의 BIM 동기화라는 기존 질문 두 건이 열려 있고, 이번 조사에서 새 질문 네 건이 생겼다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-126** (상태: 열림) 채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가? 대응점 기반 변환과 병원 정합 사례는 확인했지만 승인 주체는 확인되지 않았다.
- **oq-193** (상태: 열림) 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? BIM 기반 지도 생성·편차 검출 연구는 확인했지만 동기화 주기와 국내 사례는 확인되지 않았다.
- (새 질문, 상태: 열림) Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가?
- (새 질문, 상태: 열림) AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가?
- (새 질문, 상태: 열림) 도면과 로봇 지도의 정합에 쓰는 대응점 수(Open-RMF 4개 이상 권장, 벤더 주장 3개 이상)와 허용 오차를 정한 공통 기준이나 검수 절차가 있는가?
- (새 질문, 상태: 열림) 국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-03 | 14. 도면·BIM에서 지도 만들기 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-03/pages/topics/2026/2026-09-30-area14-s10.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기 — 다른 연구영역과의 연결"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-079, ref-153, ref-213, ref-063, ref-081, ref-869, ref-221]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#10
---

[홈](../../index.md) › [주제](../index.md) › 14. 도면·BIM에서 지도 만들기 — 다른 연구영역과의 연결

# 14. 도면·BIM에서 지도 만들기 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 좌표 정렬·지도 관리·도면 해석 AI·설비 연동·설치 과정과 이어진다. [추정][^ref-079]
- 이 페이지는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 좌표 정렬·지도 관리·도면 해석 AI·설비 연동·설치 과정과 이어진다. [추정][^ref-079]

- [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md) — 대화로 맵을 만들 때 이 영역의 축척 설정·도면 기준 정합이 대화가 부르는 엔진이 된다. [추정][^ref-153]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — 층 정렬 기준점·로봇 지도 정합·대응점 기반 좌표 변환은 좌표 정렬과 다층 모델의 일반론으로 이어진다. [추정][^ref-153]
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 도면 위 주석과 설계–준공 편차 반영은 지도 편집·버전 관리로 이어진다. [추정][^ref-081]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — BIM 에 없는 요소를 드러내는 연구처럼 지금 현장이 도면과 어떻게 다른지는 현재 상태 표현과 이어지며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 구분한다. [추정][^ref-221]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 도면·IFC 에서 가져온 문·승강기 위치는 설비 연동 대상 목록의 출발점이다. [추정][^ref-213]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 도면 위에 그린 차선은 경로·교통 관리가 쓰는 이동 그래프가 된다. [추정][^ref-079]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 도면 위 충전 위치 주석은 충전 자원 목록의 출발점이다. [추정][^ref-079]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 평면도 인식 방법·데이터셋은 L. AI·학습 기술의 도면 해석 연구를 이 영역에 적용한 것이다. [추정][^ref-063]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 설치 단계에서 로봇 매핑과 평면도 정합이 이루어진다. [추정][^ref-869]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 타르투 대학병원 사례처럼 병원 적용에서 도면 기반 지도가 쓰인다. [추정][^ref-869]
- 중점 연구 트랙 [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 이 영역을 중심 영역으로 삼는 트랙이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-30
[^ref-213]: buildingSMART International, IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md, 접근일 2026-09-30
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30
[^ref-221]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ISARC 2023), BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR, 2024-08, https://arxiv.org/abs/2408.15870, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-03 | 14. 도면·BIM에서 지도 만들기 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-03/pages/topics/2026/2026-09-30-area14-s3.md

```markdown
---
title: "14. 도면·BIM에서 지도 만들기 — 왜 중요한가"
type: topic
category: "D. 공간·지도 모델"
primary_area_no: 14
related_areas: [8, 15, 16, 18, 22, 27, 28, 45, 55, 63]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-079, ref-153, ref-213, ref-1015, ref-067, ref-081, ref-869, ref-083, ref-1024]
last_run: 2026-09-30
version: 1
split_from: docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md#3
---

[홈](../../index.md) › [주제](../index.md) › 14. 도면·BIM에서 지도 만들기 — 왜 중요한가

# 14. 도면·BIM에서 지도 만들기 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 건물 도면과 건물 정보 모델링(Building Information Modeling, BIM) 모델은 여러 제조사의 로봇 지도를 묶는 공통 기준 좌표이자, 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점이 될 수 있다. [추정][^ref-079][^ref-213]
- 이 페이지는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

건물 도면과 건물 정보 모델링(Building Information Modeling, BIM) 모델은 여러 제조사의 로봇 지도를 묶는 공통 기준 좌표이자, 층·문·승강기·충전 위치 같은 공용 자원 목록의 출발점이 될 수 있다. [추정][^ref-079][^ref-213]

Open-RMF 교통 편집기 문서는 기존 건축 도면이 작업을 단순하게 하고 제조사별 로봇 지도의 기준 좌표계 역할을 한다고 설명한다. [사실][^ref-079] 반면 로봇으로 넓은 구역을 한 번에 매핑하면 누적 불확실성 때문에 지도가 비틀리기 쉽다는 병원 현장 시험의 보고가 있다. [사실][^ref-869]

핵심 질문인 '얼마나 자동으로 만들 수 있는가'에 대해, 확인한 자료로 보면 벽·문·공간·기호 인식과 BIM·컴퓨터 지원 설계(Computer-Aided Design, CAD) 파일에서 로봇 지도를 만드는 일은 연구 수준에서 자동화가 진행됐다. 그러나 축척 설정, 로봇 지도와의 좌표 정합, 설계–준공 편차 확인은 측정선·기준점 입력과 사람의 확인에 기대고 있어 현재 형태는 '자동 초안 + 사람 확인·보정'에 가깝다. [추정][^ref-1015][^ref-067][^ref-081][^ref-083][^ref-079][^ref-153][^ref-869]

입력 데이터 쪽에서는 국내에서도 BIM 적용을 넓히려는 정책이 발표됐다. 엔지니어링데일리 보도(2020-12-28)에 따르면 국토교통부의 건설산업 BIM 활성화 로드맵은 설계 단계부터 BIM 100% 도입을 목표로 조사·설계·발주·조달·시공·감리·유지관리 등 전 생애주기에 BIM 을 쓰게 하고, LH 공동주택부터 적용을 의무화해 단계적으로 넓히는 계획을 담았다. 이는 2020-12 발표 기준이며 이후 이행 상황은 미확인이다. [추정][^ref-1024]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)
- 관련 영역: [8. 채팅으로 맵 작성](../../categories/chat-based-configuration-and-operation/chat-map-authoring.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-30
[^ref-213]: buildingSMART International, IfcTransportElement — IFC 4.3 documentation (IFC4.3.x-development, ifc4.3-main), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md, 접근일 2026-09-30
[^ref-1015]: Liu, C., Wu, J., Kohli, P., & Furukawa, Y. (ICCV 2017), Raster-to-Vector: Revisiting Floorplan Transformation, 2017, https://art-programmer.github.io/floorplan-transformation.html, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (ICCV 2021), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-081]: Vega Torres, M. A., Braun, A., & Borrmann, A. (ECPPM 2022), Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments, 2022-09, https://arxiv.org/abs/2308.05443, 접근일 2026-09-30
[^ref-869]: Valner, R. 외 (Frontiers in Robotics and AI), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-09-30
[^ref-083]: Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. (arXiv), Generation of Indoor Open Street Maps for Robot Navigation from CAD Files, 2025-07, https://arxiv.org/abs/2507.00552, 접근일 2026-09-30
[^ref-1024]: 엔지니어링데일리, "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개, 2020-12-28, https://www.engdaily.com/news/articleView.html?idxno=12613, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-03 | 14. 도면·BIM에서 지도 만들기 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1009건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 267개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
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
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
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
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- failure-explanation: 실패 설명 (Failure Explanation)
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
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
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
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
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
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
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
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
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
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
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
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
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
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
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
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [14] 에 걸린 2건 / 전체 195건)

```markdown
- oq-126 [열림] 채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가? (영역 8, 14, 55)
- oq-193 [열림] 건설 현장처럼 공간이 날마다 바뀌는 곳에서 점검 로봇의 지도와 BIM 을 어떤 주기·방식으로 맞추며, 드론과 지상 로봇을 한 계층에서 함께 운영한 국내 공개 사례가 있는가? (영역 67, 14, 16)
```
