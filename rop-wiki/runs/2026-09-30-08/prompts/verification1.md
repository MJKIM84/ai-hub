(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-08
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 45. 문서·도면·장면 이해 (L. AI·학습 기술)
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

### runs/2026-09-30-08/target.json

```json
{
  "run_id": "2026-09-30-08",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 117,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 45,
    "area_name": "45. 문서·도면·장면 이해",
    "category": "L. AI·학습 기술",
    "category_letter": "L"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=45"
}
```

### runs/2026-09-30-08/research.json

```json
{
  "run_id": "2026-09-30-08",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 45,
    "area_name": "45. 문서·도면·장면 이해",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 문서 레이아웃 분석, 표 구조 인식, 출처 근거 연결, 패놉틱 심볼 스포팅, 외부 인프라 카메라 인식 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(도면 인식)·제조 공장(고정 카메라 인식)·물류창고(CCTV 기반 다중 로봇 조율)·실외(다중 로봇 장면 그래프) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 문서 파싱, LLM 기반 데이터시트 추출, 도면 심볼 인식, 고정 카메라·로봇 인식 융합 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Docling, OmniDocBench, LangExtract, CubiCasa5K, FloorPlanCAD, AI Hub 건축 도면 데이터 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-147·oq-196·oq-197 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]",
    "매뉴얼·데이터시트 같은 기술 문서를 파싱하고 LLM으로 구조화 정보(예: 자산관리셸 속성)를 뽑을 때 보고된 정확도와 실패 원인은 무엇인가? (섹션 3·6·8 겨냥)",
    "추출한 항목마다 원문 위치를 근거로 붙여 사람이 대조·확정하게 하는 공개 구현이나 연구가 있는가? (oq-147, 섹션 6·7 겨냥)",
    "건축 도면(평면도·CAD) 인식의 대표 데이터셋·벤치마크와 성능은 무엇이며, 병원·공장·물류창고·상업 시설 같은 비주거 도면에서도 확인됐는가? (oq-196, oq-197, 섹션 5·7·8 겨냥, 한국 자료 우선)",
    "고정 카메라(CCTV·인프라 카메라)와 여러 로봇의 인식 결과를 모아 플랫폼 수준에서 공간 상태를 인식한 연구·현장 사례와 그 한계는 무엇인가? (섹션 5·6·8 겨냥)",
    "문서·도면·장면 이해에 쓰는 오픈소스·데이터셋·벤치마크는 무엇이며 라이선스·언어 범위는 어떤가? (섹션 4·7 겨냥)",
    "문서·도면·장면 이해에서 ROP가 직접 맡을 것과 로봇 자체 인식·설비·설계 도구에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "AECV-Bench(Kondratenko 외, arXiv 2601.04819, 2026-01)는 평면도 120장의 문·창·침실·화장실 개수 세기와 질의응답 192쌍으로 최신 멀티모달 모델의 건축·엔지니어링 도면 이해를 평가해, 글자 인식·텍스트 추출은 정확도 최대 0.95로 가장 높고 공간 추론은 중간, 심볼 이해·개수 세기는 0.40~0.55로 가장 낮다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1088"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "과제: 평면도 120장 객체 개수 세기, 문서 QA 192쌍(OCR·개수·공간 추론·비교 추론). OCR·텍스트 추출 최대 0.95, 심볼 이해·개수 0.40–0.55. 저자 결론: 문서 보조 도구로는 쓸 만하나 'drawing literacy'가 약하다.",
      "as_of": "2026-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "CubiCasa5K(Kalervo 외, arXiv 1904.01920, 2019-04)는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 단위 조밀 주석을 단 데이터셋과 다중 작업 합성곱 신경망 모델을 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1076"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 5000 samples annotated into over 80 floorplan object categories, 다각형 기반 조밀 주석, 다중 작업 CNN. 수치 성능과 수집 지역·건물 용도는 초록에 없음(본문 PDF 추출 실패).",
      "as_of": "2019-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "FloorPlanCAD(Fan 외, arXiv 2105.07147, 2021-11 개정)는 주거·상업 건물의 CAD 평면도 1만 장 이상을 벡터 그래픽으로 담고 30개 객체 범주를 주석한 데이터셋으로, 셀 수 있는 심볼 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 찾는 패놉틱 심볼 스포팅 과제를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 10,000 이상 평면도, residential and commercial buildings, 30 object categories, 모두 벡터 그래픽, CNN-GCN 방법으로 의미 심볼 스포팅 SOTA와 패놉틱 기준선 제시. 판(v1/v2)에 따라 규모·범주 수 서술이 다를 수 있음.",
      "as_of": "2021-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "상업 시설 사례로, Su 외(Sensors, 2022-03)는 쇼핑몰 평면도 25장(점포 1,340개)을 대상으로 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고 2단계 영역 성장 분할과 문자 인식으로 평면도의 각 점포 공간을 식별해 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%를 보고했으며 실내 로봇 주행을 활용처로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1078"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "25개 쇼핑몰 평면도, 1,340개 방. 안내판 텍스트 매칭 + 평면도 매칭(2단계 영역 성장 + OCR). room segmentation 92.54%, recognition 90.56%, overall detection 83.81%. 활용처: 실내 로봇 주행, 면적·위치 분석, 3차원 재구성.",
      "as_of": "2022-03-25",
      "site_type": "상업 시설",
      "flow_item": "작업 대상"
    },
    {
      "id": "f5",
      "claim": "과학기술정보통신부·한국지능정보사회진흥원의 AI Hub 「건축 도면 데이터」(2022년 구축, 주관 에이치씨아이플러스)는 도면 48,033장(평면도 41,556·단면도 3,262·입면도 1,595·구조도 1,620)을 아파트·연립다세대·단독주택의 주거 용도로만 구성하고, 구조 8종(출입문·창호·벽체 등)·공간 12종(거실·침실·주방 등)·객체 5종(변기·세면대·싱크대·욕조·가스레인지) 라벨을 두며, 유효성 검증 모델 성능으로 YOLOv5 객체 탐지 mAP 90.33%, DeepLabV3+ 분할 mIoU 71.2%, 문자 인식 CER 4.95%를 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1077"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"2022년/48,033장\". 주택유형: 아파트, 연립다세대, 단독주택. 구조 8종·공간 12종·객체 5종. YOLOv5 mAP 90.33%(목표 72 이상), DeepLabV3+ mIoU 71.2%(목표 60 이상), OCR CER 4.95%(목표 5% 이하).",
      "as_of": "2022",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f6",
      "claim": "AI Hub 건축 도면 데이터의 라벨은 주거 건축 요소와 위생·주방 설비로 이루어져 있어 충전 위치·승강기 앞 대기 구역 같은 로봇 운영용 클래스는 들어 있지 않고 비주거 건물 도면은 포함되지 않은 것으로 보이므로, 병원·공장·물류창고 도면에 쓰려면 별도 라벨과 데이터가 필요할 것으로 추정된다.",
      "tag": "추정",
      "source_ids": [
        "ref-1077"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "객체 5종 목록(변기·세면대·싱크대·욕조·가스레인지)은 전체가 공개되었고 로봇 운영 클래스 없음. 구조 8종·공간 12종은 페이지에 일부만 표시되어 나머지 클래스는 미확인. 건물 용도는 주거 3종뿐.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "OmniDocBench(Ouyang 외, CVPR 2025)는 학술 논문·교과서·손글씨 노트·밀집 조판 신문 등 9개 문서 출처에 19개 레이아웃 범주와 15개 속성 라벨을 달아, 파이프라인 방식과 시각–언어 모델 방식의 PDF 문서 파싱을 전체·모듈·속성 수준에서 비교 평가하는 벤치마크다.",
      "tag": "사실",
      "source_ids": [
        "ref-1080"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v2(2025-03-25) 초록: nine document sources, 19 layout categories, 15 attribute labels, 종단·과제별·속성별 다단계 평가, 파이프라인과 VLM 의 문서 유형별 강약점 제시. CVPR 2025 채택.",
      "as_of": "2025-03-25",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "OmniDocBench 공식 저장소 README 는 2026-04 판(v1.6) 기준 PDF 1,651쪽·10개 문서 유형·영어와 중국어(간체)·혼합 언어로 구성된다고 밝히고, 종단 평가 상위 모델(TeleOCR)의 종합 점수 96.91·텍스트 편집 거리 0.0267·표 TEDS 96.82 를 싣으며, 데이터는 연구 목적으로만 쓰고 상업적 사용을 허용하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"1651 PDF pages, covering 10 document types, 5 layout types, and 5 language types\"; 언어는 영어·간체 중국어·혼합. 상위: TeleOCR 96.91/0.0267/96.82, OvisOCR2 96.47, PaddleOCR-VL-1.6 96.34. 연구 목적 전용 라이선스. 한국어 문서는 없음.",
      "as_of": "2026-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "IBM Research 가 공개한 Docling(Livathinos 외, arXiv 2501.17887, 2025-01)은 여러 문서 형식을 하나의 구조화 표현으로 바꾸는 MIT 라이선스 오픈소스 도구로, 레이아웃 분석에 DocLayNet 기반 모델을, 표 구조 인식에 TableFormer 를 쓰고 일반 하드웨어에서 적은 자원으로 동작하며 LangChain·LlamaIndex·spaCy 에 통합되어 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1082"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: parse several types of popular document formats into a unified, richly structured representation; 레이아웃 DocLayNet, 표 TableFormer; MIT; Python API·CLI; commodity hardware. 타 도구와의 수치 비교는 초록에 없음.",
      "as_of": "2025-01-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Xia·Xiao·Jazdi·Weyrich(IEEE Access, 2024)는 데이터시트 원문에서 '의미 노드'를 뽑아 LLM 에이전트로 자산관리셸(AAS) 인스턴스 모델을 생성하는 시스템을 만들고, 원문 정보가 오류 없이 AAS 로 옮겨진 비율(유효 생성률)을 62~79%로 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1087"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: effective generation rate of 62-79%, 원문 정보의 상당 부분이 오류 없이 목표 디지털 트윈 인스턴스 모델로 옮겨짐. 여러 LLM 비교와 RAG 절제 실험 포함. 데이터셋 규모는 초록에 없음.",
      "as_of": "2024-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "Groß·Heidrich 의 AAS-RAIL(arXiv 2609.07334, 2026-09)은 전기공학·유체동력 분야 4개 제조사의 제품 데이터시트–AAS 쌍 200건에서, 비슷한 기존 AAS 로부터 추출 지침을 검색해 문맥 예시로 쓰는 방식으로 속성 추출 정확도를 평균 51.8%에서 71.7%로 높였으나, 원문 데이터시트에서 정답 속성값을 찾을 수 있는 경우가 전체 속성의 56.2%뿐이어서 전문가 검토가 여전히 필요하다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1086"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "평가 200쌍(4개 제조사) + 검색 DB 40쌍. 기준선 51.8% → RAIL 71.7%(상대 +38.4%). 이전 오답의 22.4%가 정답으로, 2.0%만 퇴행. 원문에서 속성값 확인 가능 56.2%, 속성명과 값이 함께 있는 경우 13.4%.",
      "as_of": "2026-09-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "독립된 두 연구(f10·f11)를 종합하면 LLM 으로 기술 데이터시트를 표준 자산 모델로 옮길 때 오류 없이 옮겨지는 비율은 대략 5~8할 수준이고, 원문 자체에 정보가 없거나 이름과 값이 떨어져 있는 경우가 많아 사람의 검토 없이 등록 정보로 확정하기는 어려운 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1087",
        "ref-1086"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10: 유효 생성률 62~79%. f11: 속성 추출 51.8%→71.7%, 원문에서 정답 확인 가능 56.2%. 대상 문서(일반 데이터시트)가 로봇 매뉴얼이 아니므로 로봇 문서에 그대로 적용할 수 있는지는 미확인.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "오픈소스 LangExtract(google/langextract, Apache 2.0)는 LLM 으로 비정형 텍스트에서 구조화 정보를 뽑으면서 추출한 항목마다 원문 텍스트의 정확한 위치를 연결하고, 그 위치를 원문 맥락에 강조해 보여 주는 HTML 검토 화면을 만들어 사람이 대조할 수 있게 하며, 구글의 공식 지원 제품은 아니라고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1089"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"map every extraction to its exact location in the source text\"; 자체 완결 HTML 시각화로 수천 개 항목을 원문 맥락에서 검토; 예시 기반 스키마; Gemini·OpenAI·Ollama 지원; not an officially supported Google product. 로봇 문서 전용 도구는 아님.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f14",
      "claim": "Dussard·Sarthou(LAAS, arXiv 2606.17073, 2026-06)는 URDF 의 구조·기구학 기술 안 식별자를 LLM 이 상식으로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 파이프라인을 제안했으나, 초록에는 정량 평가 결과를 밝히지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: URDF 식별자는 의미 회복에 commonsense interpretation 이 필요; 기존 온톨로지 개념에 맞춘 분류; 'initial results'만 언급, 수치 없음. 원문 위치 근거 부착 여부 언급 없음.",
      "as_of": "2026-06-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "제조 공장 사례로, Brorsson 외(arXiv 2512.15215)의 인프라 기반 이동 로봇 시스템은 천장 카메라가 로봇에 붙인 ArUco 표식을 검출해 로봇 위치·방향을 계산하고, 저해상도 영상의 이진 의미 분할로 장애물과 빈 공간을 격자 단위로 구분하며, 카메라별 점유 지도를 전역 지도로 합치되 시야가 겹치는 곳은 가장 가까운 카메라 하나의 결과만 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: 마커 코너의 2D 영상 좌표로 (x,y,θ) 계산; binary semantic segmentation 으로 점유/빈 칸 분류; per-camera occupancy maps → global map, 겹치는 시야는 가장 가까운 카메라 기준. 보행자 전용 추적은 보고되지 않음.",
      "as_of": "2025-12",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f16",
      "claim": "같은 연구의 대형 상용차 제조 현장 배치에서는 약 8 m 높이에 단 카메라 15대(대당 약 60 m²)가 바닥을 덮고, 로봇 6대가 약 150 m 구간에서 머플러를 운반하며 하루 약 130회 운반(주기 7분)을 수행했다.",
      "tag": "사실",
      "source_ids": [
        "ref-308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: 15 cameras, six robots transporting mufflers ~150 m, ~130 transport operations daily, 7-minute cycle, 카메라 높이 약 8 m·대당 약 60 m². (재인용: 2026-09-30-05, 이번에 HTML 본문 다시 열람)",
      "as_of": "2025-12",
      "site_type": "제조 공장",
      "flow_item": "작업 대상"
    },
    {
      "id": "f17",
      "claim": "같은 연구는 인프라 카메라 인식의 한계로 카메라 간 하드웨어 동기화가 없어 생기는 시간 차 오류, 가림·센서 고장·제한된 시야 범위로 인한 위치 추정 중단, 작업자·독점 제품·기밀 공정이 영상에 찍히는 개인정보·기밀 문제를 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "본문: cameras are not hardware-synchronized → time shift 오류; occlusions, sensor faults, or limited coverage 가 위치 추정을 방해; 시각 센서가 작업자 이미지·독점 제품·기밀 공정을 담을 수 있음.",
      "as_of": "2025-12",
      "site_type": "제조 공장",
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "물류창고 사례로, Robinson 외(Oxford, arXiv 2606.06762, 2026-06)는 로봇에 작업용 주행 장비를 싣지 않고 외부 CCTV 카메라망과 외부 계산만으로, 보정하지 않은 화소 단위 위상 카메라 그래프 위 영상 공간에서 다중 로봇을 계획·제어하며 카메라 시야가 겹치는 구역을 공유 자원으로 순차 배정해 교착을 막는 방식을 실제 창고(로봇 4대, 카메라 30대, 길이 27 m 통로 6개)에서 시연하고 이를 첫 현장 시연이라고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1075"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: entirely in image space over an uncalibrated, pixel-wise topological camera graph; 계층형 계획, 겹치는 카메라 영역을 공유 자원으로; 실창고 4 robots, 30 cameras, 6 aisles(27 m). 임무 시간·조율 통계 보고(수치는 초록에 없음).",
      "as_of": "2026-06-04",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f19",
      "claim": "Modi 외(arXiv 2605.18197, 2026-05)는 RGB 카메라만으로 3차원 장면 그래프를 만드는 능동 탐색 방법을 제안하고, 시뮬레이션(ReplicaCAD)에서 천장 쪽 고정 외부 카메라 1대로 초기화하면 기준 방법의 장면 그래프 노드 수가 16개에서 37개로, 재현율이 0.12에서 0.27로 늘었으며, 로봇 없이 고정 카메라 3대만 쓰면 F1 이 0.421(복잡한 아파트)·0.516(가구 배치 방)으로 30단계 능동 탐색의 재현율에는 못 미치지만 환경의 주요 구조는 잡는다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "HTML 본문: SEE 16→37 노드(+125%), 재현율 0.12→0.27; ASP 23→36; 고정 카메라 1~3대 단독 270회 시행(90개 장면), 3대 F1 0.421/0.516. 모든 실험이 시뮬레이션이며 창고·실제 배치 없음.",
      "as_of": "2026-05-18",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "실외 사례로, Strader 외(MIT 등, arXiv 2506.07454, 2025-07 개정)는 로봇마다 만든 장면 그래프와 개방형 객체 지도를 대응점으로 정합해 하나의 공유 3차원 장면 그래프로 합치고, LLM 이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 운영자의 자연어 의도를 PDDL 목표로 바꾸는 다중 로봇 계획·실행 시스템을 대규모 실외 환경의 실제 작업으로 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: shared 3D scene graph incorporating an open-set object-based map, 다중 로봇 조율·실시간 재위치 추정; LLM translates operator intent into PDDL goals; real-world tasks in large-scale, outdoor environments. 로봇 대수는 초록에 없음.",
      "as_of": "2025-07-10",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽는가)에 대해, 문서의 글자·표를 읽는 파싱은 공개 벤치마크에서 높은 점수를 내지만(f1·f8), 데이터시트에서 속성값을 표준 모델로 옮기는 정확도는 5~8할 수준이고(f10·f11), 도면의 심볼 개수 세기는 멀티모달 모델에서 0.40~0.55 에 그치며(f1), 전용 도면 인식 모델도 상업 시설 평면도에서 전체 검출 약 84% 수준이고(f4), 고정 카메라 장면 인식은 구조는 잡되 세부 객체 재현율이 낮아(f19) 어느 쪽도 사람 확인 없이 실행 정보로 쓰기에는 부족한 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1088",
        "ref-1081",
        "ref-1087",
        "ref-1086",
        "ref-1078",
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "수치들은 서로 다른 데이터·지표(OCR 정확도, 종합 점수, 속성 추출 정확도, 검출 정확도, F1)라 직접 비교할 수 없고, 한국어 문서·로봇 매뉴얼·비주거 도면에서 측정한 자료는 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 이기종 로봇 등록과 능력 표현에 필요한 정보가 제조사 문서·데이터시트·URDF 에 흩어져 있어 이를 자동으로 읽어야 하고(f10·f11·f14), 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며(f1·f4), 여러 로봇·고정 카메라의 인식을 모아야 로봇 한 대로는 가려지는 공간 상태를 알 수 있는데(f15·f18·f19), 각 단계의 오류가 그대로 등록 정보·지도·세계 상태의 오류로 이어지기 때문이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1087",
        "ref-1086",
        "ref-1079",
        "ref-1088",
        "ref-1078",
        "ref-308",
        "ref-1075",
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "근거 finding 의 종합. 실제 ROP 운영에서 문서·도면 해석 오류가 실행 실패로 이어진 사례 자료는 이번 실행에서 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 45. 문서·도면·장면 이해에서 ROP 가 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가(f7·f9·f11), 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름(f13), 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 플랫폼 수준 융합(f15·f17·f20)이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1080",
        "ref-1082",
        "ref-1086",
        "ref-1089",
        "ref-308",
        "ref-1084"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "영역 정의(매뉴얼·도면 해석과 플랫폼 수준의 장면 인식)와 근거 finding 의 종합. 융합 결과가 표현하는 현재 상태 자체는 18. 실시간 세계 상태·데이터 일관성의 내용이다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇 온보드 센서 인식·SLAM·국지 회피(f15·f20의 로봇 측 인식)는 로봇 제조사에, CCTV·영상 관리 시스템과 카메라 설치·동기화(f17·f18)는 시설·보안 설비 쪽에, 도면·BIM 작성 도구와 원본 도면(f3·f5)은 설계·건축 쪽에 속하므로, ROP 는 이들이 내는 인식 결과·영상·도면을 받아 해석·융합하는 인터페이스와 검토 절차를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-308",
        "ref-1084",
        "ref-1075",
        "ref-1085",
        "ref-1077"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 19장: 로봇 자체 지능·제어의 외부 연계 영역에 센서 인식·SLAM·로컬 회피가 있음. 카메라 망 소유·운영 주체는 출처가 밝히지 않음.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "이 영역은 매뉴얼 해석이 적용되는 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전(f10·f11·f14), 능력 항목을 받는 5. 로봇 능력·작업 표현(f14), 추출 결과 검토의 7. 온톨로지 검증·변경 관리(f13), 도면 해석이 적용되는 14. 도면·BIM에서 지도 만들기(f1~f5), 지도와 장소 의미의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리(f4·f20), 융합된 현재 상태를 담는 18. 실시간 세계 상태·데이터 일관성(f15·f19), 사람 인식의 19. 사람·보행자 모델(f15), 언어 모델 계획의 44. 로봇 기반 모델·언어 모델 계획(f20), AI 결과 사용 기준의 47. AI·학습·적응과 모델 운영(f12·f21), 영상 개인정보의 53. 개인정보·영상 데이터(f17), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f7), 적용 현장인 61. 물류창고(f18)·62. 제조 공장(f15~f17)·64. 상업 시설(f4)·66. 실외(f20)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1087",
        "ref-1086",
        "ref-1079",
        "ref-1089",
        "ref-1088",
        "ref-1078",
        "ref-1084",
        "ref-308",
        "ref-1083",
        "ref-1080",
        "ref-1075"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "교차 규칙(원문 13장 주석: 매뉴얼 해석은 4·55번, 도면 해석은 14번)과 근거 finding 의 종합. 34. 시뮬레이션·예측용 디지털 트윈과는 이번 근거로 연결하지 않음.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1075",
      "org": "Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv)",
      "title": "Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse",
      "published": "2026-06-04",
      "url": "https://arxiv.org/abs/2606.06762",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "외부 CCTV 카메라망과 외부 계산만으로 영상 공간의 위상 카메라 그래프 위에서 다중 로봇을 계획·제어하고 실제 창고(로봇 4대, 카메라 30대)에서 시연한 프리프린트. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2606.06762",
      "source_unopened": false
    },
    {
      "id": "ref-1076",
      "org": "Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. (arXiv)",
      "title": "CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis",
      "published": "2019-04-03",
      "url": "https://arxiv.org/abs/1904.01920",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "평면도 이미지 5,000장을 80개 이상 범주로 다각형 주석한 데이터셋과 다중 작업 CNN. 초록 페이지만 열람(본문 PDF 텍스트 추출 실패).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/1904.01920",
      "source_unopened": false
    },
    {
      "id": "ref-1077",
      "org": "한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주))",
      "title": "건축 도면 데이터",
      "published": null,
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2022년 구축한 주거용 건축 도면 48,033장(평면·단면·입면·구조도)과 구조·공간·객체 라벨, 객체 탐지·분할·OCR 유효성 검증 성능을 제공하는 AI 학습용 데이터 소개 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "source_unopened": false
    },
    {
      "id": "ref-1078",
      "org": "Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7))",
      "title": "A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans",
      "published": "2022-03-25",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "쇼핑몰 평면도 25장(1,340개 방)에서 안내판 텍스트 매칭과 2단계 영역 성장·OCR 로 점포 공간을 분할·인식해 분할 92.54%, 인식 90.56%, 전체 83.81% 를 보고한 동료심사 논문. PMC 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/",
      "source_unopened": false
    },
    {
      "id": "ref-1079",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06-10",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "URDF 의 구조·기구학 기술을 LLM 으로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 파이프라인 제안. 초록에 정량 결과 없음.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2606.17073",
      "source_unopened": false
    },
    {
      "id": "ref-1080",
      "org": "Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv)",
      "title": "OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations",
      "published": "2025-03-25",
      "url": "https://arxiv.org/abs/2412.07626",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "9개 문서 출처·19개 레이아웃 범주·15개 속성 라벨로 파이프라인 방식과 시각–언어 모델의 PDF 파싱을 다단계로 평가하는 벤치마크(CVPR 2025). 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2412.07626",
      "source_unopened": false
    },
    {
      "id": "ref-1081",
      "org": "OpenDataLab (opendatalab/OmniDocBench)",
      "title": "OmniDocBench — README",
      "published": "2026-04",
      "url": "https://github.com/opendatalab/OmniDocBench",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OmniDocBench v1.6 의 규모(1,651쪽, 10개 문서 유형, 영어·간체 중국어·혼합), 종단 평가 순위표, 연구 목적 전용 라이선스를 적은 공식 저장소 README. 성능 표는 저장소 게시 값.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/opendatalab/OmniDocBench/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1082",
      "org": "Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv)",
      "title": "Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion",
      "published": "2025-01-27",
      "url": "https://arxiv.org/abs/2501.17887",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "여러 문서 형식을 구조화 표현으로 바꾸는 MIT 라이선스 오픈소스 도구 Docling(DocLayNet 레이아웃 모델, TableFormer 표 모델)을 설명한 기술 보고. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2501.17887",
      "source_unopened": false
    },
    {
      "id": "ref-1083",
      "org": "Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv)",
      "title": "RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots",
      "published": "2026-05-18",
      "url": "https://arxiv.org/abs/2605.18197",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "RGB 만으로 능동 탐색하며 3차원 장면 그래프를 만들고, 고정 외부 카메라를 같은 표현에 통합하는 효과를 시뮬레이션에서 평가한 프리프린트. HTML 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2605.18197",
      "source_unopened": false
    },
    {
      "id": "ref-1084",
      "org": "Strader, J., Ray, A., Arkin, J. 외 (arXiv)",
      "title": "Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs",
      "published": "2025-07-10",
      "url": "https://arxiv.org/abs/2506.07454",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "여러 로봇의 장면 그래프를 공유 3차원 장면 그래프로 융합하고 LLM 으로 운영자 의도를 PDDL 목표로 바꾸는 다중 로봇 계획·실행 시스템을 대규모 실외에서 평가. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2506.07454",
      "source_unopened": false
    },
    {
      "id": "ref-1085",
      "org": "Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv)",
      "title": "FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting",
      "published": "2021-11-29",
      "url": "https://arxiv.org/abs/2105.07147",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "주거·상업 건물 CAD 평면도 1만 장 이상을 벡터로 담고 30개 범주를 주석한 데이터셋과 패놉틱 심볼 스포팅 과제·CNN-GCN 기준 방법. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2105.07147",
      "source_unopened": false
    },
    {
      "id": "ref-1086",
      "org": "Groß, J., & Heidrich, J. (arXiv)",
      "title": "AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning",
      "published": "2026-09-07",
      "url": "https://arxiv.org/abs/2609.07334",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "PDF 제품 데이터시트에서 AAS 속성을 추출할 때 비슷한 기존 AAS 의 추출 지침을 검색해 문맥 예시로 쓰는 방법으로 정확도를 51.8%→71.7% 로 높인 프리프린트. HTML 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2609.07334",
      "source_unopened": false
    },
    {
      "id": "ref-1087",
      "org": "Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv)",
      "title": "Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0",
      "published": "2024-06-24",
      "url": "https://arxiv.org/abs/2403.17209",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "데이터시트 텍스트에서 의미 노드를 뽑아 LLM 에이전트로 AAS 인스턴스 모델을 생성하고 유효 생성률 62~79% 를 보고한 논문(IEEE Access 게재). arXiv 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2403.17209",
      "source_unopened": false
    },
    {
      "id": "ref-1088",
      "org": "Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv)",
      "title": "AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding",
      "published": "2026-01-08",
      "url": "https://arxiv.org/abs/2601.04819",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "평면도 객체 개수 세기(120장)와 도면 질의응답(192쌍)으로 멀티모달 모델의 건축·엔지니어링 도면 이해를 평가한 벤치마크. 초록 페이지 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2601.04819",
      "source_unopened": false
    },
    {
      "id": "ref-1089",
      "org": "Google (google/langextract)",
      "title": "LangExtract — README",
      "published": null,
      "url": "https://github.com/google/langextract",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "LLM 으로 비정형 텍스트에서 구조화 정보를 추출하며 항목마다 원문 위치를 연결하고 HTML 검토 화면을 만드는 Apache 2.0 오픈소스 라이브러리의 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/google/langextract/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-308",
      "org": "Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv)",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "설비에 단 센서·계산 자원, 현장 클라우드, 로봇 온보드 자율의 세 층을 둔 사내 물류 이동 로봇 기준 아키텍처와 대형 상용차 제조 현장 배치를 다룬 프리프린트. 이번 실행에서 HTML 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2512.15215",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
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
      "rationale": "섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 문서 레이아웃 분석·표 구조 인식 f7·f9, 출처 근거 연결 f13, 패놉틱 심볼 스포팅 f3, 인프라 카메라 인식·공유 장면 그래프 f15·f20 / 섹션 5: 상업 시설 — f4(쇼핑몰 평면도 인식, 작업 대상: 공간), 제조 공장 — f15(수행 자원: 천장 카메라)·f16(작업 대상: 머플러 운반)·f17(제약: 동기화·가림·개인정보), 물류창고 — f18(수행 자원: CCTV 망만으로 다중 로봇 조율), 실외 — f20(시작 조건: 운영자 자연어 의도), 가정 — f5(주거 도면 데이터). 병원 사례는 찾지 못함을 명시 / 섹션 6: 문서 파싱 f7·f8·f9, LLM 데이터시트 추출 f10·f11·f12, URDF 해석 f14, 원문 위치 근거 f13, 도면 인식 f1~f4, 카메라·로봇 인식 융합 f15·f18·f19·f20 / 섹션 7: Docling f9, OmniDocBench f7·f8, LangExtract f13, CubiCasa5K f2, FloorPlanCAD f3, AI Hub 건축 도면 데이터 f5, AECV-Bench f1 / 섹션 8: f1·f4·f10·f11·f15·f18·f19·f20 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 4, 5, 7, 14, 15, 16, 18, 19, 44, 47, 53, 54, 55, 61, 62, 64, 66 / 섹션 11: 기존 oq-147·oq-196 과 open_questions_new 4건. 다음 실행 후보: 4. 이기종 로봇 등록 페이지에 f10·f11·f13 반영, 18. 실시간 세계 상태·데이터 일관성 페이지에 f15·f17 반영."
    },
    {
      "action": "update",
      "path": "docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md",
      "sections": [
        "5",
        "8",
        "11"
      ],
      "rationale": "교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 f4 를 섹션 5(상업 시설 사례)에, f1·f3·f5 를 섹션 8 에, f5·f6(oq-197 해결 근거)·f4(oq-196 부분 근거)를 섹션 11 에 반영 제안."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "문서 레이아웃 분석",
      "term_en": "Document Layout Analysis",
      "definition": "문서 페이지 이미지나 PDF 에서 본문·제목·표·그림·수식 같은 영역을 찾아 종류를 구분하고 읽는 순서를 정하는 문서 이해의 첫 단계다."
    },
    {
      "term_ko": "표 구조 인식",
      "term_en": "Table Structure Recognition",
      "definition": "문서 속 표의 행·열·병합 셀 구조를 복원해 표 내용을 기계가 읽을 수 있는 형식으로 바꾸는 기술로, TEDS 같은 트리 편집 거리 지표로 평가한다."
    },
    {
      "term_ko": "출처 근거 연결",
      "term_en": "Source Grounding",
      "definition": "언어 모델이 문서에서 추출한 항목마다 원문 속 정확한 위치(문자 범위·쪽·절)를 함께 기록해 사람이 원문과 대조해 확인할 수 있게 하는 방식이다."
    },
    {
      "term_ko": "인프라 장착 센서",
      "term_en": "Infrastructure-mounted Sensing",
      "definition": "천장·벽 같은 시설에 고정한 카메라·센서로 로봇 밖에서 넓은 영역의 위치·장애물·사람을 인식해 로봇 온보드 센서의 가림과 시야 한계를 보완하는 방식이다."
    }
  ],
  "open_questions_new": [
    "OmniDocBench 같은 공개 문서 파싱 벤치마크에 한국어 문서가 없는데, 한국어 로봇 매뉴얼·설비 도면을 파싱·추출할 때의 정확도를 측정한 자료가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 4. 이기종 로봇 등록 | 근거: f8 | 종류: 일반",
    "일반 제품 데이터시트가 아니라 로봇 매뉴얼(능력·실행 조건·오류 코드)을 대상으로 LLM 추출 정확도를 측정한 공개 벤치마크나 연구가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 5. 로봇 능력·작업 표현 | 근거: f11 | 종류: 일반",
    "하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 18. 실시간 세계 상태·데이터 일관성 | 근거: f17 | 종류: 일반",
    "플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? | 관련 영역: 45. 문서·도면·장면 이해, 53. 개인정보·영상 데이터 | 근거: f17 | 종류: 일반"
  ],
  "open_questions_resolved": [
    "oq-197"
  ],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "f2 CubiCasa5K 의 수집 지역(핀란드)·주거 전용 여부와 성능 수치: 검색 요약에만 나오고 초록·README 에서 확인하지 못함(본문 PDF 추출 실패)",
      "f3 FloorPlanCAD 규모·범주 수: 초록은 1만 장 이상·30개 범주·주거와 상업, 검색 요약은 1만5천 장·35개 범주·병원·학교 포함으로 판에 따라 다름. PQ 0.561 은 검색 요약에만 있어 넣지 않음",
      "f6 AI Hub 구조 8종·공간 12종 라벨의 전체 목록은 페이지에 일부만 보여 미확인",
      "f18 임무 시간·조율 통계 수치는 초록에 없어 미확인",
      "f20 로봇 대수·실험 수치는 초록에 없어 미확인",
      "f10 데이터셋 규모는 초록에 없어 미확인",
      "ETRI 전자통신동향분석 '스마트제조 분야 LLM 기반 안전성 평가' 글(공장 매뉴얼 기반 질의응답 평가)은 ECONNRESET 으로 두 번 열지 못해 넣지 않음",
      "Belfadel 외(arXiv 2609.31663) 산업 보고서 온톨로지 추출은 정량 수치가 초록에 없어 넣지 않음",
      "병원 현장의 고정 카메라·로봇 인식 융합 사례는 찾지 못함(찾은 arXiv 2509.26106 은 시뮬레이션 병원·저가 하드웨어라 제외)",
      "oq-196 은 부분 근거만(f4 상업 시설 평면도 83.81~92.54%, f3 상업 건물 포함 데이터셋) 확보해 해결 제안하지 않음",
      "oq-147 은 범용 도구 LangExtract(f13)만 찾았고 로봇 매뉴얼·URDF 능력 항목에 원문 위치를 붙인 공개 구현은 찾지 못함"
    ],
    "scope_violations": [
      "f15·f20: 로봇 측 인식·SLAM·재위치 추정은 로봇 자체 지능(연계 대상)이므로 플랫폼 수준 융합 근거로만 쓰고 f24 에서 구분함",
      "f18: 로봇에 주행 장비 없이 외부 카메라·외부 계산으로 주행을 제어하는 방식은 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례('경계는 제품 전략에 따라 이동할 수 있다')이며 ROP 기본 범위로 서술하지 않도록 주의",
      "f19·f15: 장면 인식 결과가 표현하는 현재 상태는 18. 실시간 세계 상태·데이터 일관성의 내용이며 34. 시뮬레이션·예측용 디지털 트윈과 섞지 않음(f19 의 시뮬레이션은 평가 환경일 뿐 예측 실험이 아님)",
      "f24: CCTV·영상 관리 시스템, 설계 도구·원본 도면을 '연계 대상: '으로 표시함"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 병원 사례와 한국어 문서 이해 자료를 더 넣지 못했다. 재사용 1건(ref-308: 참고문헌 목록 전체가 입력에 없어 값은 이전 브리프 2026-09-30-05 의 출처 표를 따랐고, 이번에 HTML 본문을 다시 열었다). 원문 열람: 16건 모두 열었다(webfetch 14건, github_raw 2건). 논문은 대부분 초록 페이지이고 Su 외(PMC 본문)·Modi 외·AAS-RAIL·Brorsson 외(arXiv HTML 본문)만 본문을 봤다. 교차 확인 0건: 수치마다 데이터·지표가 달라 같은 값을 두 출처로 확인할 수 없었고, f12·f21 은 종합 추정(low)으로 냈다. 벤더 문서는 쓰지 않았다. 분류 원문 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽어 내는가)에는 f21 로 답했고 결론은 '글자·표 파싱은 벤치마크에서 높지만 속성 추출 5~8할, 도면 심볼 세기 0.40~0.55, 고정 카메라 장면 인식은 구조 수준이라 사람 확인 없이 실행 정보로 쓰기 어렵다'는 추정이다. 현장 유형 사례는 상업 시설(f4)·제조 공장(f15~f17)·물류창고(f18)·실외(f20)·가정(f5, 주거 도면 데이터)이며 병원·기타 사례는 찾지 못했다. 국내 자료는 AI Hub 건축 도면 데이터(ref-1077) 1건이다. oq-197 해결 근거: f5·f6(비주거 도면 미포함, 공개된 객체 5종에 로봇 운영 클래스 없음; 구조·공간 라벨 전체 목록은 미확인이라 검증 판단 필요). oq-196·oq-147 은 부분 근거만 있어 해결 제안하지 않았다. 교차 규칙에 따라 매뉴얼 해석 finding(f10·f11·f13·f14)은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에, 도면 해석 finding(f1~f6)은 14. 도면·BIM에서 지도 만들기에 연결하도록 제안했다. 용어집에 이미 있는 평면도 인식·패놉틱 심볼 스포팅·파놉틱 품질·3차원 장면 그래프·협동 인지·래스터–벡터 변환·자산관리셸·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md

```markdown
---
title: "45. 문서·도면·장면 이해"
type: area
category: "L. AI·학습 기술"
area_no: 45
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 45. 문서·도면·장면 이해

# 45. 문서·도면·장면 이해

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

매뉴얼·도면 해석과 플랫폼 수준의 장면 인식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **문서·도면 해석 AI**: 매뉴얼과 도면을 해석하는 모델을 다룬다
- **플랫폼 수준 장면 인식**: 고정 카메라와 여러 로봇의 인식 결과를 모아 공간 상태를 인식한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]

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

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md (요약)

```markdown
# 44. 로봇 기반 모델·언어 모델 계획

소속 대분류: L. AI·학습 기술 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
```

### docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md (요약)

```markdown
# 46. 예측·학습 기반 최적화

소속 대분류: L. AI·학습 기술 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

학습 기반 배정·경로, 수요·고장 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **학습 기반 배정·경로**: 강화학습 같은 학습 방법으로 배정과 경로를 정한다
- **수요·고장 예측**: 일의 양과 고장을 예측해 계획과 정비에 쓴다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
```

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1044건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 282개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
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
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
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
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [45] 에 걸린 3건 / 전체 215건)

```markdown
- oq-147 [조사 중] 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (영역 4, 45, 7)
- oq-196 [열림] Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가? (영역 14, 45)
- oq-197 [열림] AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? (영역 14, 45)
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

### runs/2026-09-30-07/research.md

```markdown
# 리서치 브리프 2026-09-30-07

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-07 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 44. 로봇 기반 모델·언어 모델 계획 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 로봇 기반 모델, 교차 형태 학습, 행동 토큰화, LLM-모듈로, 불확실도 정렬 연결 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정·제조 공장·물류창고 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 시각–언어–행동 모델, 언어 모델 계획과 기호 계획기 결합, 다중 로봇 계획, 불확실도 기반 도움 요청 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open X-Embodiment, OpenVLA, GR00T N1, ROSA 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
2. 시각–언어–행동(Vision-Language-Action, VLA) 모델과 로봇 기반 모델은 무엇이며 어떤 데이터·구조로 여러 로봇·작업에 일반화하는가? (섹션 4·6·8 겨냥)
3. 대규모 언어 모델(LLM)로 작업을 계획·분해할 때의 한계는 무엇이고, 기호 계획기·외부 검증기·불확실도 기반 도움 요청으로 어떻게 보완하는가? (섹션 3·6·8 겨냥)
4. 언어 모델로 여러 로봇의 작업 분해·연합 형성·배정을 계획하는 연구와 공개 오픈소스(ROS 연동 에이전트 포함)는 무엇인가? (섹션 6·7 겨냥)
5. 가정·제조 공장·물류창고 등 현장(국내 포함)에서 로봇 기반 모델을 적용한 사례와 그 조건·성과는 무엇인가? (섹션 5 겨냥, 한국 자료 우선)
6. 로봇 기반 모델·언어 모델 계획에서 ROP가 직접 맡을 것과 로봇 제조사·모델 제공자에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Brohan 외의 RT-2(arXiv 2307.15818, 2023-07)는 로봇 행동을 텍스트 토큰으로 표현해 자연어 토큰과 같은 방식으로 학습 데이터에 넣고, 시각–언어 모델을 로봇 궤적 데이터와 웹 시각 질의응답 과제에 함께 미세조정한 시각–언어–행동(VLA) 모델로, 6,000회 평가에서 새 물체·학습에 없던 명령에 대한 일반화가 좋아졌다고 보고했다. | ref-1045 | 아니오 | medium | 2023-07 | — | — |
| f2 | [사실] | Open X-Embodiment 협력단(arXiv 2310.08864, 2023-10)은 21개 기관이 모은 22종 로봇의 데이터(527개 스킬, 160,266개 작업)를 표준 형식으로 공개하고, 이 데이터로 학습한 RT-X 모델이 다른 로봇의 경험을 활용해 여러 로봇의 능력을 높이는 긍정적 전이를 보였다고 보고했다. | ref-1048 | 아니오 | medium | 2023-10 | — | — |
| f3 | [사실] | Kim 외의 OpenVLA(arXiv 2406.09246, 2024-06)는 Llama 2 에 DINOv2·SigLIP 시각 특징을 결합한 70억 매개변수 공개 VLA 모델로 실제 로봇 시연 97만 건으로 학습했고, 29개 작업에서 매개변수가 7배 많은 RT-2-X(550억)보다 절대 성공률이 16.5%p 높았으며, 모델 체크포인트·미세조정 노트북·PyTorch 코드를 공개했다. | ref-1046 | 아니오 | medium | 2024-06 | — | — |
| f4 | [사실] | Physical Intelligence 의 π0.5(arXiv 2504.16054, 2025-04)는 여러 로봇의 데이터·고수준 의미 예측·웹 데이터 등 이질적 과제를 함께 학습(co-training)해, 처음 보는 가정집에서 부엌·침실 정리 같은 장기·정교한 조작 작업을 수행했다고 보고했다. | ref-1047 | 아니오 | medium | 2025-04 | 가정 / 작업 대상 | — |
| f5 | [사실] | NVIDIA 의 GR00T N1(arXiv 2503.14734, 2025-03)은 환경을 해석하는 시각–언어 모듈(System 2)과 실시간 운동 명령을 만드는 확산 트랜스포머(System 1)를 나눈 이중 시스템 구조의 공개 휴머노이드용 VLA 모델로, 실제 로봇 궤적·사람 영상·합성 데이터를 섞어 학습하고 Fourier GR-1 휴머노이드의 양손 조작에 배치했다고 보고했다. | ref-1054 | 아니오 | medium | 2025-03 | — | — |
| f6 | [사실] | Ahn 외의 SayCan(arXiv 2204.01691, 2022-04)은 언어 모델이 긴 추상적 지시를 수행하는 절차 지식을 제공하고, 로봇이 미리 학습한 스킬의 가치 함수가 현재 물리 환경에서 그 스킬이 실행 가능한 정도를 제공해 둘을 결합하는 방식으로 언어 모델 계획을 로봇 능력에 접지(grounding)했으며, 모바일 매니퓰레이터로 실험했다. | ref-1049 | 아니오 | medium | 2022-04 | — | — |
| f7 | [사실] | Liu 외의 LLM+P(arXiv 2304.11477, 2023-04)는 자연어 문제 설명을 언어 모델로 PDDL(계획 도메인 정의 언어) 문제로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 3단계 방식으로, 대부분의 벤치마크 문제에서 최적해를 낸 반면 언어 모델 단독은 대부분 실행 가능한 계획조차 내지 못했다고 보고했다. | ref-1050 | 아니오 | medium | 2023-04 | — | — |
| f8 | [의견] | Kambhampati 외(ICML 2024, arXiv 2402.01817)는 자기회귀 언어 모델이 스스로 계획하거나 자기 검증할 수 없다고 보고, 언어 모델을 근사적 지식원으로 두고 외부 기호 검증기와 양방향으로 상호작용하게 하는 LLM-모듈로(LLM-Modulo) 프레임워크를 제안했다. | ref-1051 | 아니오 | medium | 2024-06 | — | — |
| f9 | [사실] | Ren 외의 KnowNo(CoRL 2023, arXiv 2307.01928)는 언어 모델 계획기가 확신에 찬 환각 예측을 내는 문제에 대해 등각 예측으로 불확실도를 측정해, 공간·수량·선호·언어 모호성이 있을 때 사람에게 도움을 요청하게 하고 사람 도움을 최소화하면서 작업 완료에 통계적 보장을 주며, 모델 미세조정이 필요 없다고 보고했다. | ref-1053 | 아니오 | medium | 2023-07 | 예외·성과 | — |
| f10 | [사실] | Kannan·Venkatesh·Min 의 SMART-LLM(arXiv 2309.10062, IROS 2024 투고)은 프로그램 형식의 퓨샷 프롬프트로 언어 모델이 고수준 지시를 작업 분해·연합 형성·작업 배정의 세 단계로 다중 로봇 계획으로 바꾸게 하고, 복잡도가 다른 네 범주의 지시로 된 벤치마크를 만들어 시뮬레이션과 실제 로봇으로 시험했다. | ref-1052 | 아니오 | medium | 2023-09 | — | — |
| f11 | [사실] | Su 외의 IMR-LLM(arXiv 2603.02669, 2026-03)은 가정용보다 제약이 엄격한 산업 다중 로봇 생산 작업을 대상으로, 언어 모델이 선택 그래프(disjunctive graph) 구성을 돕고 결정적 풀이 방법으로 실행 가능한 고수준 계획을 얻은 뒤 공정 트리를 따라 실행 가능한 저수준 프로그램을 생성하게 했으며, 세 난이도의 벤치마크 IMR-Bench 로 평가했다(초록에는 실제 공장 배치가 적혀 있지 않다). | ref-1055 | 아니오 | medium | 2026-03 | 제조 공장 / 제약 | — |
| f12 | [사실] | NASA 제트추진연구소(JPL)가 관리하는 오픈소스 ROSA(ROS Agent)는 LangChain 위에 만든 에이전트로, ROS 1(Noetic)과 ROS 2(Humble·Iron·Jazzy) 기반 로봇 시스템에 자연어로 질의하고 명령하게 한다. | ref-1056 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [추정] | BMW 그룹은 2025년 스파턴버그 공장에 Figure AI 의 휴머노이드 Figure 02 를 11개월 동안 배치해 용접 공정용 판금 부품 투입을 맡겼고, 이 로봇이 BMW X3 3만 대 이상의 생산을 도왔다고 밝힌다. | ref-1058 | 아니오 | low | 2026-06-25 | 제조 공장 / 예외·성과 | 벤더 주장 |
| f14 | [추정] | 같은 BMW 그룹 자료는 후속 Figure 03 이 스파턴버그 공장에서 대용량 용기에 섞여 들어온 부품을 집어 순서 대차(sequencing trolley)에 정리하고, 대차가 자동화 시스템으로 조립 공정에 운반되는 순서 공급(just in sequence) 물류 작업을 맡으며, 음성 대화 기능과 무선 충전을 갖췄다고 밝힌다. | ref-1058 | 아니오 | low | 2026-06-25 | 제조 공장 / 완료·인계 | 벤더 주장 |
| f15 | [사실] | 지디넷코리아 보도(2025-05-01)에 따르면 2025-04-10 출범한 산업통상자원부 주도 K-휴머노이드 연합에서 레인보우로보틱스·에이로봇·홀리데이로보틱스·로보티즈·로브로스 5개 로봇기업이 개발 중인 휴머노이드를 서울대 AI연구원에 제공해 로봇 AI 파운데이션 모델 개발을 지원하기로 했다. | ref-1057 | 아니오 | low | 2025-05-01 | — | — |
| f16 | [추정] | 헬로티 보도(2025-11-26)에 따르면 로보티즈는 산업통상부 과제 'AI 파운데이션 모델 기반 유통 공정 특화 휴머노이드 로봇 개발'(정부 출연금 약 60억 원)로 VLA 모델을 넣은 상체형 휴머노이드 AI 워커를 BGF로지스 물류센터에 투입해 입·출고, 오발주 재분류, 비정형 상품 분류, 반품 처리 작업을 수행하게 한다. | ref-1059 | 아니오 | low | 2025-11-26 | 물류창고 / 작업 대상 | 벤더 주장 |
| f17 | [추정] | 같은 보도에 따르면 이 과제는 물류센터 핵심 공정 자동화율 80% 이상과 오발주 재분류·피킹 작업 성공률 90% 이상을 목표로 한다(달성 결과가 아니라 목표치다). | ref-1059 | 아니오 | low | 2025-11-26 | 물류창고 / 예외·성과 | 벤더 주장 |
| f18 | [추정] | 확인한 자료를 종합하면 핵심 질문(범용 로봇 모델과 언어 모델이 오케스트레이션의 무엇을 바꾸는가)에 대해, 로봇 기반 모델은 로봇 쪽 기능을 고정된 스킬 목록에서 새 물체·지시에 일반화하는 학습된 정책으로 바꾸고(f1~f5), 언어 모델은 지시 해석·작업 분해·다중 로봇 배정의 입력 방식을 바꾸지만(f6·f10·f11), 언어 모델 단독 계획은 실행 가능성·검증이 약해 기호 계획기·외부 검증기·불확실도 기반 사람 확인과 짝지어 쓰는 형태가 연구의 공통 방향으로 보인다(f7·f8·f9). | ref-1045, ref-1048, ref-1046, ref-1047, ref-1054, ref-1049, ref-1052, ref-1055, ref-1050, ref-1051, ref-1053 | 아니오 | low | 2026-09-30 | — | — |
| f19 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 여러 로봇의 데이터를 모아 하나의 정책을 학습하는 흐름(f2·f3)이 이종 로봇의 능력 표현과 등록 방식에 영향을 주고, 언어 모델 계획이 확신에 찬 오류를 낼 수 있어(f8·f9) 대화로 받은 지시를 실행 전에 검증할 장치가 필요하며, 제조 공장·물류창고에서 휴머노이드·VLA 적용이 시작됐다고 발표되고 있기 때문이다(f13·f16). | ref-1048, ref-1046, ref-1051, ref-1053, ref-1058, ref-1059 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 44. 로봇 기반 모델·언어 모델 계획에서 ROP 가 직접 맡을 범위는 언어 모델이 만든 작업 분해·배정 계획을 기호 계획기·제약 검사로 검증하는 계층(f7·f8·f11), 불확실할 때 사람에게 확인을 요청하는 절차(f9), 로봇 기반 모델을 탑재한 로봇을 포함한 이종 로봇에 계획을 내리는 인터페이스(f6·f10·f12)다. | ref-1050, ref-1051, ref-1055, ref-1053, ref-1049, ref-1052, ref-1056 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 VLA·로봇 기반 모델이 카메라 영상에서 관절·그리퍼 행동을 직접 생성하는 저수준 조작 정책(f1·f3·f4·f5)은 로봇 자체 지능·제어(파지·모터·관절 제어)에 속하므로 로봇 제조사·모델 제공자가 맡고, 이종 제조사를 잇는 ROP 는 그런 로봇의 가능한 기능·실행 조건·완료·실패 확인을 받는 인터페이스를 맡을 것으로 보인다. | ref-1045, ref-1046, ref-1047, ref-1054 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 이 영역은 학습된 범용 기능을 표현해야 하는 5. 로봇 능력·작업 표현과 4. 이기종 로봇 등록(f2·f3), 언어 모델 계획을 대화로 부르는 12. 채팅으로 업무 지시·오케스트레이션과 13. 대화형 기능의 신뢰·기반(f9·f12), 작업 분해의 24. 작업·워크플로 모델링(f7·f11), 연합 형성·배정의 25. 작업 배정 — MRTA(f10), 공정 순서의 26. 작업 순서·스케줄링(f11), 계획 검증의 29. 명령·작업 실행의 신뢰성과 54. 시험·형식 검증·벤치마크(f7·f8·f11), 사람 확인의 31. 사람–로봇 협업(f9), 실행 기준의 47. AI·학습·적응과 모델 운영(f8·f9), 업체 동향의 1. 기술·시장·업체 동향(f13·f15·f16), 적용 현장인 61. 물류창고(f16)·62. 제조 공장(f11·f13)·65. 가정·공동주택(f4)과 이어진다. | ref-1048, ref-1046, ref-1053, ref-1056, ref-1050, ref-1055, ref-1052, ref-1051, ref-1058, ref-1057, ref-1059, ref-1047 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1045 | Brohan, A., Brown, N. 외 (Google DeepMind, arXiv) | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023-07-28 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.15818 | 아니오 |
| ref-1046 | Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv) | OpenVLA: An Open-Source Vision-Language-Action Model | 2024-06-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2406.09246 | 아니오 |
| ref-1047 | Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv) | π0.5: a Vision-Language-Action Model with Open-World Generalization | 2025-04-22 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2504.16054 | 아니오 |
| ref-1048 | Open X-Embodiment Collaboration (arXiv) | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023-10-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2310.08864 | 아니오 |
| ref-1049 | Ahn, M., Brohan, A., Brown, N. 외 (arXiv) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2204.01691 | 아니오 |
| ref-1050 | Liu, B., Jiang, Y., Zhang, X. 외 (arXiv) | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04-22 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2304.11477 | 아니오 |
| ref-1051 | Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv) | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 2024-02-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2402.01817 | 아니오 |
| ref-1052 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09-18 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-1053 | Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-1054 | NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv) | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 2025-03-18 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2503.14734 | 아니오 |
| ref-1055 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv) | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2603.02669 | 아니오 |
| ref-1056 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/nasa-jpl/rosa | 아니오 |
| ref-1057 | 지디넷코리아 | K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과 | 2025-05-01 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20250501140356 | 아니오 |
| ref-1058 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 2026-06-25 | 벤더 문서 | medium | 2026-09-30 | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en | 아니오 |
| ref-1059 | 헬로티 | VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입 | 2025-11-26 | 기사 | low | 2026-09-30 | https://www.hellot.net/news/article.html?no=107567 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(왜 중요한가), f18(핵심 질문 답, 추정) / 섹션 4: VLA·행동 토큰화 f1, 교차 형태 학습 f2, 이중 시스템 구조 f5, 접지 f6, LLM-모듈로 f8, 불확실도 정렬 f9 / 섹션 5: 가정 — f4, 제조 공장 — f11(벤치마크 한정)·f13·f14(벤더 주장 병기), 물류창고 — f16·f17(국내, 벤더 주장·목표치 병기). 병원·상업 시설·실외 사례는 찾지 못함을 명시 / 섹션 6: 로봇 기반 모델 f1~f5, 언어 모델 계획과 기호 계획기·검증기 결합 f6~f8, 다중 로봇 계획 f10·f11, 불확실도 기반 도움 요청 f9 / 섹션 7: Open X-Embodiment f2, OpenVLA f3, GR00T N1 f5, ROSA f12, PDDL f7 / 섹션 8: f1~f11, 국내 동향 f15 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65 / 섹션 11: open_questions_new 3건. 다음 실행 후보: 12. 채팅으로 업무 지시·오케스트레이션 페이지에 f7~f9 반영, 25. 작업 배정 — MRTA 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 로봇 기반 모델 | Robot Foundation Model | 여러 로봇·작업·환경의 대규모 데이터로 사전 학습해 새 작업·물체·로봇에 미세조정하거나 바로 쓸 수 있게 한 범용 로봇 모델로, 시각–언어–행동 모델이 대표적이다. |
| 교차 형태 학습 | Cross-embodiment Learning | 형태·센서·구동 방식이 다른 여러 로봇의 데이터를 함께 학습해 한 로봇의 경험이 다른 로봇의 성능을 높이게 하는 학습 방식이다. |
| 이중 시스템 구조 | Dual-system Architecture (System 1 / System 2) | 느린 시각–언어 추론 모듈(System 2)이 상황을 해석하고 빠른 행동 생성 모듈(System 1)이 실시간 운동 명령을 만드는 로봇 기반 모델 구조다. |

## 열린 질문

새로 생긴 질문:

- 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 5. 로봇 능력·작업 표현 | 근거: f3 | 종류: 일반
- 언어 모델 기반 다중 로봇 계획기를 현장 제약(설비·안전·시간창)이 있는 조건에서 비교할 공통 벤치마크나 평가 기준이 있는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f11 | 종류: 일반
- 국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 61. 물류창고 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 5회 · 신규 출처 15건
- 미확인 항목:
    - f1~f11 은 arXiv 초록 기준이며 본문 실험 조건 미확인
    - f13·f14: Figure AI 자체 발표 페이지(figure.ai/news/production-at-bmw)는 연결 오류로 열지 못해 교차 확인 실패
    - f15: 산업통상자원부 보도자료(korea.kr, 2025-04-10) 본문은 첨부 파일에만 있어 교차 확인 실패, '2028년까지 로봇 AI 파운데이션 모델 구축' 목표는 검색 요약에만 있어 넣지 않음
    - f16·f17: 로보티즈·BGF로지스 1차 발표 미확인, 목표치는 실측 결과 아님
    - OpenVLA 라이선스는 요약 결과가 모호해 넣지 않음
    - 병원·상업 시설·실외 현장의 로봇 기반 모델·언어 모델 계획 실배치 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1·f3·f4·f5: VLA 의 저수준 조작 정책은 로봇 자체 지능·제어 영역이므로 동향 근거로만 쓰고 f21 에서 '연계 대상: '으로 구분함
    - f11: 공정 프로그램 생성은 로봇 제어 코드에 닿으므로 계획 검증 근거로만 제안함
    - f13·f14·f16·f17: 벤더·기사 주장이므로 vendor_claim: true·태그 추정으로 냄
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치 — f15·f17 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON(runs/2026-09-30-07/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상으로 브리프를 다시 만들고 벤더·기사가 전한 기능·성능 주장(f13·f14·f16·f17)을 모두 vendor_claim: true·태그 추정·evidence_excerpt 첫머리 '벤더 주장: '으로 냈다. 새 브리프의 f15 는 기사(ref-1057)의 정부 협력 사실 보도로 벤더 문서가 아니며 신뢰도 low 로 두었다. 직전 브리프와 finding 번호·출처 번호가 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 5회/30, 신규 출처 15건/15(ref-1045~ref-1059, 예약 구간 안)로 출처 상한 도달. 원문 열람: 15건 모두 열었다(webfetch 14건, github_raw 1건). 논문은 초록 페이지다. 교차 확인 0건. 분류 원문 핵심 질문에는 f18 로 답했고 결론은 '로봇 기반 모델은 로봇 쪽 기능을 학습된 범용 정책으로 바꾸고, 언어 모델은 지시·분해·배정의 입력을 바꾸되 기호 계획기·외부 검증기·불확실도 기반 사람 확인과 짝지어 쓰는 방향'이라는 추정이다. 현장 유형 사례는 가정(f4)·제조 공장(f11 벤치마크, f13·f14 벤더 주장)·물류창고(f16·f17 국내, 벤더 주장)다. 국내 자료는 지디넷코리아(ref-1057)·헬로티(ref-1059) 두 건이다. 교차 규칙에 따라 이 영역의 L. AI·학습 기술 내용은 적용 대상인 25. 작업 배정 — MRTA(f10)와 C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션(f7~f9)에 함께 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 VLA·LLM 에이전트·LLM-모듈로·PDDL·등각 예측·불확도 정렬·작업 분해·어포던스·연합 형성은 후보로 내지 않았다. 입력 누락: runs/2026-09-30-07/research.json(직전 반환값) 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### runs/2026-09-30-06/research.md

```markdown
# 리서치 브리프 2026-09-30-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-06 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 43. 데이터·관측성·배포 |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 관측성, OpenTelemetry, MCAP, FinOps·FOCUS, A/B 분할 업데이트 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(운영 로그 기반 실패 분석)·물류창고(배포 전 시뮬레이션 검증) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 기록 형식, 추적·지표·로그 수집, 컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 비용 계측 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — rosbag2·MCAP, ros2_tracing, OpenTelemetry, Mender, FOCUS 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
2. 로봇·플랫폼의 로그·이벤트·텔레메트리를 기록·저장하는 형식과 도구(rosbag2·MCAP, 플랫폼 기록 DB)는 무엇이며, 보존 기간을 정하는 국내 규제 근거는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)
3. 플랫폼 관측성을 구현하는 표준·오픈소스(OpenTelemetry, ros2_tracing, 커널 기반 관찰)는 무엇이며 관찰 자체의 성능 부담은 얼마로 보고되는가? (섹션 6·7·8 겨냥)
4. 현장 서버·로봇·클라우드에 플랫폼 소프트웨어를 배포하고 되돌리는 방법(컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 배포 전 시뮬레이션 검증)은 무엇이며 어떤 결과가 보고되는가? (섹션 6·7·8 겨냥)
5. 클라우드와 언어 모델 호출 비용을 측정·할당·관리하는 기준(FinOps 주기, FOCUS 청구 데이터 명세, OpenTelemetry 생성형 AI 토큰 지표)은 무엇인가? (섹션 4·6·7 겨냥)
6. 병원·물류창고 등 현장에서 운영 데이터를 수집해 실패 원인을 분석하거나 소프트웨어 변경을 배포 전에 검증한 사례는 무엇인가? (섹션 5 겨냥)
7. 데이터·관측성·배포에서 ROP가 직접 맡을 것과 로봇 제조사·클라우드 사업자·법규에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Bédard·Lütkebohle·Dagenais 의 ros2_tracing(IEEE RA-L 7(3), 2022-07)은 저부하 추적기 LTTng 를 써서 ROS 2 의 실행 정보를 수집하는 계측·추적 도구 모음으로, ROS 2 추적 데이터를 운영체제 추적과 결합할 수 있고, ROS 2 계측을 모두 켰을 때 종단 간 메시지 지연 증가가 평균 0.0033 ms 라고 보고했다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f2 | [사실] | ros2_tracing 저자들은 미들웨어 수준의 표준 데이터 기록만으로는 내부 계산과 성능 병목에 관한 정보가 충분하지 않다고 보고, 이를 실행 추적 도구가 필요한 이유로 든다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f3 | [사실] | Yu·Lee·Choi·Park 의 ros2probe(arXiv 2606.10746, 2026-06)는 ROS 2 도메인에 구독자로 참여하는 관찰 도구가 탐색(discovery) 부담과 역직렬화 비용을 더해 관찰 대상을 교란한다고 보고, 탐색 패킷으로 통신 그래프를 복원한 뒤 사용자가 지정한 토픽만 커널 안에서 걸러 관찰하는 방식으로 관찰자 CPU 사용을 최대 7배·메모리를 최대 28배 줄이고, 포화 조건에서 도메인 참여형 도구가 38.5% 메시지를 잃을 때 메시지 손실 0을 보고했다. | ref-1039 | 아니오 | medium | 2026-06 | — | — |
| f4 | [사실] | ROS 2 Iron Irwini(2023-05-23 출시)부터 rosbag2 가 새 백 파일을 기록하는 기본 형식을 sqlite3 에서 MCAP 로 바꿨고, 같은 판에서 서비스 호출로 원격에서 기록을 일시 정지·재개·분할하는 기능이 더해졌다. | ref-1040, ref-1041 | 예 | high | 2023-05-23 | — | — |
| f5 | [추정] | Foxglove 는 MCAP 이 SQLite3 의 '복원력' 모드 수준의 데이터 안전성과 '쓰기 최적화' 모드 수준의 쓰기 처리량을 함께 제공하고, zstd·lz4 압축을 고를 수 있으며, 메시지 정의를 파일 안에 담아 외부 스키마 없이 다른 도구가 읽을 수 있다고 주장한다. | ref-1041 | 아니오 | low | 2022-12-22 | — | 벤더 주장 |
| f6 | [사실] | OpenTelemetry 명세 상태 요약에 따르면 추적(tracing)은 API·SDK·프로토콜이 모두 안정(stable)이고 장기 지원 대상이며, 로그는 브리지 API·SDK·프로토콜이 안정, 지표(metrics)는 API·프로토콜이 안정이나 SDK 는 혼합 상태, 프로파일(profiles)은 프로토콜이 개발(development) 단계다. | ref-1042 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | OpenTelemetry 생성형 AI 의미 규약 저장소의 토큰 지표 문서는 입력·출력·캐시 읽기·캐시 쓰기 입력·추론 출력 토큰 카운터(gen_ai.client.inference.usage.*)와 호출별 입력·출력 토큰 히스토그램(gen_ai.client.inference.operation.*)을 정의하고, 작업 이름·제공자 이름을 필수 속성으로 두며, 모든 지표가 개발(Development) 단계다. | ref-1043 | 아니오 | medium | 2026-09-30 | — | — |
| f8 | [사실] | 오픈소스 ros-opentelemetry 는 송신 측이 추적 문맥을 ROS 2 메시지의 사용자 정의 필드에 넣고 수신 측이 꺼내 이어 붙이는 방식으로 토픽·서비스·액션을 가로지르는 분산 추적을 C++·Python 노드에 제공하고, 로그를 추적 구간(span)에 연결하는 로거를 둔다. | ref-1044 | 아니오 | medium | 2026-09-30 | — | — |
| f9 | [사실] | Zhang·Yu·Westerlund(Sensors, 2025-08)는 TurtleBot4 에 얹은 Jetson Nano 5대를 작업 노드로, 노트북 1대를 마스터로 둔 K3s 클러스터에서 컨테이너화한 ROS 2 노드로 다중 로봇 UWB 상대 위치 추정을 운영했고, 오차 보정용 LSTM 파드 5개를 모두 종료시킨 경우에도 Kubernetes 가 파드를 자동 재시작해 위치 오차(APE)가 약 0.12~0.14 m 로 장애 없는 경우와 비슷하게 유지됐다고 보고했다. | ref-1045 | 아니오 | medium | 2025-08-14 | 예외·성과 | — |
| f10 | [사실] | 연계 대상: 오픈소스 Mender 는 임베디드 리눅스·사물인터넷 장치용 클라이언트–서버 방식 무선(OTA) 업데이트 관리자로, 이중 A/B 루트 파일시스템 분할에 이미지 단위로 원자적 배포를 해 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있게 하며, 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트를 지원하고 Apache 2.0 라이선스로 공개된다. | ref-1046 | 아니오 | medium | 2026-09-30 | — | — |
| f11 | [사실] | 개인정보보호위원회 「개인정보의 안전성 확보조치 기준」(고시 제2023-6호, 2023-09-22 시행) 제8조는 개인정보처리자가 개인정보취급자의 개인정보처리시스템 접속기록을 1년 이상(5만 명 이상의 정보주체 개인정보를 처리하는 시스템 등은 2년 이상) 보관·관리하고, 월 1회 이상 점검하며, 위조·변조·도난·분실되지 않도록 안전하게 보관하게 한다. | ref-766 | 아니오 | medium | 2023-09-22 | 제약 | — |
| f12 | [사실] | FinOps 재단의 FinOps 프레임워크는 기술 비용·사용량·효율 데이터를 수집·배분·보고·예측하는 정보(Inform), 사용량 최적화와 요금 최적화를 찾는 최적화(Optimize), 엔지니어링·재무·사업 팀이 함께 개선을 실행하는 운영(Operate)의 세 단계를 반복하는 방식으로 설명하며, 대상 기술 범주에 공용 클라우드·SaaS 와 함께 AI 서비스를 든다. | ref-1048 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | FinOps 재단의 청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)는 SaaS·PaaS 청구 데이터를 클라우드 비용과 같은 스키마에 넣고, 크레딧·토큰 같은 가상 통화와 다중 통화 정규화(PricingCurrency 등), 청구서 연결용 InvoiceId 열을 더했으며, AWS·Microsoft·Google Cloud·Oracle Cloud·Alibaba Cloud·Databricks·Grafana 가 지원을 밝혔다. | ref-1049 | 아니오 | medium | 2025-05-29 | — | — |
| f14 | [사실] | Bruno·Sim·Hagiwara(arXiv 2609.29043, 2026-09)는 클라우드 언어 모델 API 는 로봇이 긴 작업을 반복할수록 요청당 비용이 쌓이고 네트워크 지연이 실시간 반응을 떨어뜨린다고 보고, 두 단계 연쇄(chaining) 계획으로 추론당 프롬프트 길이를 약 45% 줄여 로컬 모델(Qwen2.5-14B·Cogito-14B)의 계획 성공을 최대 37%p 높였으며 클라우드 모델(Claude Sonnet 4.6)과 함께 비교했다. | ref-1051 | 아니오 | medium | 2026-09 | 예외·성과 | — |
| f15 | [사실] | 고려대학교 구로병원의 자율 약품 배송 로봇 실증(Lee 외, Digital Health, 2026-03)에서 배송 임무는 응급실 직원이 웹 애플리케이션으로 요청하면 시작됐다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 시작 조건 | — |
| f16 | [사실] | 같은 병원 실증은 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 넘겨 간호사가 받는 것을 배송 성공으로 정의했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 완료·인계 | — |
| f17 | [사실] | 같은 병원 실증은 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 담은 승강기 통신 로그, 관찰자가 적은 수기 기록지(탑승객·화물·결과)를 함께 모아 분석했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 작업 대상 | — |
| f18 | [사실] | 같은 병원 실증에서 전체 배송 성공률은 87.03%, 승강기 가동률 59% 미만일 때 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었으며, 승강기 가동률이 높을수록 실패가 많았다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f19 | [추정] | Ocado 는 물류창고 로봇 교통 관리·오케스트레이션 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 초당 10회 로봇 통신 같은 실제 운영 데이터로 모델을 다듬으며, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. | ref-1052 | 아니오 | low | 2025-06-04 | 물류창고 / 예외·성과 | 벤더 주장 |
| f20 | [사실] | Open-RMF 의 웹 API 서버(rmf-web api-server)는 기록용 데이터베이스로 tortoise-orm 을 통해 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하며 기본값은 메모리 SQLite 다. | ref-762 | 아니오 | medium | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에 대해, 데이터는 자기 기술형 기록 형식(MCAP)과 플랫폼 기록 DB 로 남기고(f4·f20), 상태는 OpenTelemetry 의 추적·지표·로그로 플랫폼 서비스를 관찰하면서 로봇 내부 실행은 저부하 추적·커널 필터로 교란 없이 보며(f1·f3·f6·f8), 배포는 컨테이너 오케스트레이션의 자동 재시작과 이미지 기반 A/B 롤백, 배포 전 시뮬레이션 검증을 조합하고(f9·f10·f19), 비용은 표준 청구 데이터(FOCUS)와 토큰 지표를 FinOps 주기로 관리하는 조합이 공개 자료의 공통 형태로 보인다(f7·f12·f13). | ref-1040, ref-762, ref-1038, ref-1039, ref-1042, ref-1044, ref-1045, ref-1046, ref-1052, ref-1043, ref-1048, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 미들웨어 기록만으로는 내부 병목을 알 수 없고(f2) 관찰 도구 자체가 시스템을 교란할 수 있으며(f3), 병원 실증처럼 실패 원인이 로봇·승강기 로그를 함께 모아야 드러나고(f17·f18), 클라우드 언어 모델 호출 비용이 반복 작업에서 누적되며(f14), 개인정보를 다루는 시스템은 접속기록 보존·점검 의무를 지기 때문이다(f11). | ref-1038, ref-1039, ref-943, ref-1051, ref-766 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 43. 데이터·관측성·배포에서 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책(f6·f11), 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스(f4·f8·f17), 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증(f9·f19), 클라우드·언어 모델 호출 비용의 계측·배분(f7·f13)이다. | ref-1042, ref-766, ref-1040, ref-1044, ref-943, ref-1045, ref-1052, ref-1043, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 운영체제·펌웨어의 무선 업데이트와 로봇 내부 ROS 2 실행 추적(f1·f10)은 로봇 제조사에, 클라우드 청구 데이터 생성(f13)은 클라우드 사업자에, 승강기 통신 로그(f17)는 설비 제어 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 내는 기록·업데이트 상태·청구 데이터를 받아 모으는 인터페이스를 맡을 것으로 보인다. | ref-1038, ref-1046, ref-1049, ref-943 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 실행 기록을 보여 주는 37. 관제 화면·실행 기록(f17·f20), 로그로 원인을 찾는 38. 모니터링·이상 탐지·원인 분석(f2·f18), 성과 지표의 39. 운영 성과 측정·개선(f18), 컨테이너·DDS 통신의 42. 분산 시스템·통신·컴퓨팅 구조(f9), 기록 DB 를 두는 41. 플랫폼 아키텍처·외부 API(f20), 업데이트·버전의 57. 자산·소프트웨어 수명주기 관리(f10), 배포 전 검증의 54. 시험·형식 검증·벤치마크와 34. 시뮬레이션·예측용 디지털 트윈(f19), 접속기록의 53. 개인정보·영상 데이터와 52. 통신 보호·위협 관리·감사(f11), 비용의 3. 경제성·조달·사업 모델(f12·f13), 언어 모델 비용의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영·13. 대화형 기능의 신뢰·기반(f7·f14), 승강기 로그의 22. 설비·건물 시스템 연동(f17), 적용 현장인 63. 병원·의료(f15~f18)·61. 물류창고(f19)와 이어진다. | ref-943, ref-762, ref-1038, ref-1045, ref-1046, ref-1052, ref-766, ref-1048, ref-1049, ref-1043, ref-1051 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1038 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2201.00393 | 아니오 |
| ref-1039 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 2026-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.10746 | 아니오 |
| ref-1040 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 2023-05-23 | 오픈소스 문서 | high | 2026-09-30 | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html | 아니오 |
| ref-1041 | Foxglove | MCAP as the ROS 2 Default Bag Format | 2022-12-22 | 벤더 문서 | medium | 2026-09-30 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | 아니오 |
| ref-1042 | OpenTelemetry (CNCF) | Specification Status Summary | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://opentelemetry.io/docs/specs/status/ | 아니오 |
| ref-1043 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md | 아니오 |
| ref-1044 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://github.com/szobov/ros-opentelemetry | 아니오 |
| ref-1045 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 2025-08-14 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ | 아니오 |
| ref-1046 | Northern.tech (mendersoftware) | mender — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/mendersoftware/mender | 아니오 |
| ref-766 | 개인정보보호위원회 (국가법령정보센터) | 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호) | 2023-09-22 | 정부·연구기관 | high | 2026-09-30 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 아니오 |
| ref-1048 | FinOps Foundation | FinOps Phases | 미확인 | 업계 보고서 | medium | 2026-09-30 | https://www.finops.org/framework/phases/ | 아니오 |
| ref-1049 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 미확인 | 표준 | medium | 2026-09-30 | https://www.finops.org/insights/focus-1-2-available/ | 아니오 |
| ref-943 | Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-1051 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 2026-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.29043 | 아니오 |
| ref-1052 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies | 2025-06-04 | 벤더 문서 | medium | 2026-09-30 | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 관측성·실행 추적 f1·f2, MCAP f4·f5(벤더 주장 병기), OpenTelemetry f6, 토큰 지표 f7, A/B 분할 업데이트 f10, FinOps·FOCUS f12·f13 / 섹션 5: 병원 — f15(시작 조건)·f16(완료·인계)·f17(작업 대상: 로봇·승강기 로그 정보)·f18(예외·성과), 물류창고 — f19(배포 전 시뮬레이션 검증, 벤더 주장 병기). 제조 공장·상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 기록 f4·f20, 관찰 f1·f3·f6·f8, 배포 f9·f10·f19, 비용 f7·f12·f13·f14 / 섹션 7: rosbag2·MCAP f4·f5, ros2_tracing f1, ros2probe f3, OpenTelemetry f6·f7, ros-opentelemetry f8, K3s f9, Mender f10, FOCUS f13, 개인정보 고시 f11 / 섹션 8: f1·f3·f9·f14·f15~f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3·f17·f18 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 관측성 | Observability | 시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다. |
| 오픈텔레메트리 | OpenTelemetry (OTel) | 추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다. |
| MCAP | MCAP | 여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다. |
| 핀옵스 | FinOps | 클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 38. 모니터링·이상 탐지·원인 분석 | 근거: f8 | 종류: 일반
- 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f11 | 종류: 일반
- OpenTelemetry 생성형 AI 토큰 지표가 개발 단계에서 이름이 바뀌고 있는데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? | 관련 영역: 43. 데이터·관측성·배포, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반
- 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리 | 근거: f10 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 1
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - f1·f3·f14 는 논문 초록(또는 HTML 일부) 기준이며 본문 실험 조건 미확인
    - f7: 검색 결과 요약의 다른 문서들은 gen_ai.client.token.usage 히스토그램을 설명하지만, 열어 본 현재 저장소는 gen_ai.client.inference.usage.* 로 정의함. 이름 변경 시점과 이전 이름의 폐기 여부 미확인
    - f11 의 '5만 명 이상' 조건 문구는 검색 요약으로 보완했고 법령 페이지 요약에서는 1년/2년 구분만 확인
    - f13 FOCUS 1.2 명세 본문(PDF) 미열람, 발표 글만 열람
    - f8 ros-opentelemetry 라이선스·유지 주체 미확인(개인 관리 저장소)
    - ref-1049·ref-1052 제목 일부는 검색 결과 제목 기준
    - Zampetti 외 CPS CI/CD 인터뷰 연구(ACM TOSEM 2023)는 ACM 403·PDF 본문 추출 실패로 넣지 않음
    - Docker·Kubernetes 기반 ROS 설계 흐름 논문(ACM 10.1145/3594539)은 403 으로 넣지 않음
    - 실외이동로봇 운행안전인증에서 관제·소프트웨어 원격 업데이트 시 변경 인증 필요 여부는 KIRIA 안내 페이지에 없어 확인하지 못함
    - 제조 공장·상업 시설·가정·실외 현장의 데이터·배포 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1·f3: ROS 2 내부 실행 추적은 로봇 소프트웨어 쪽 기법이므로 관찰 방법 근거로만 쓰고, 이종 제조사 로봇 내부 추적은 f24 에서 연계 대상으로 구분함
    - f10: 로봇 운영체제·펌웨어 OTA 는 로봇 제조사 영역이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 언어 모델 계획 자체는 44. 로봇 기반 모델·언어 모델 계획의 내용이며 이 영역에는 비용·지연 근거로만 제안함
    - f17: 승강기 통신 로그 생성은 설비 제어 쪽이며 ROP 는 수집·결합만 맡는 것으로 f24 에서 구분함
    - f19: 시뮬레이션·디지털 트윈 자체는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 내용이며 이 영역에는 배포 전 검증 근거로만 제안함. 18. 실시간 세계 상태·데이터 일관성과 섞지 않음
- 한계: web_fetch_available: true · fetch_mode full. 검색 22회/30, 신규 출처 15건/15(출처 상한 도달). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1032 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-04·2026-09-30-05)가 ref-1032~ref-1037 을 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-1038~ref-1052 를 순서대로 썼다. 재사용 1건(ref-762, 이전 브리프 2026-09-30-05 재인용, 이번에 다시 열지 않음; 값은 그 브리프의 출처 표를 따랐고 참고문헌 목록 전체는 입력에 없음). 원문 열람: 신규 15건 모두 열었다(webfetch 11건, github_raw 4건). 논문 가운데 Zhang 외(ref-1045)·Lee 외(ref-943)는 PMC 본문을, 나머지는 초록 페이지를 열었다. 교차 확인 1건(f4: ROS 2 공식 릴리스 노트와 Foxglove 블로그). 벤더 문서만 근거로 한 f5·f19 는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에는 f21 로 답했고 결론은 '자기 기술형 기록 형식과 기록 DB + OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적 + 컨테이너 자동 재시작·A/B 롤백·배포 전 시뮬레이션 검증 + 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기'라는 추정이다. 현장 유형 사례는 병원(f15~f18, 국내 고려대학교 구로병원)·물류창고(f19, 벤더 주장)뿐이다. 국내 자료는 개인정보보호위원회 고시(ref-766)와 국내 병원 실증 논문(ref-943) 두 건이다. L. AI·학습 기술 관련 f7·f14 는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안했다. 용어집에 이미 있는 분산 추적·백 파일·무선 업데이트·서비스 수준 협약·감사 추적·모델 레지스트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```
