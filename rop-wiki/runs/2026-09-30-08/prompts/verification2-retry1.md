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
        "ref-063"
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
        "ref-067"
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
        "ref-1012"
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
        "ref-1012"
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
        "ref-513"
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
        "ref-239"
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
        "ref-513",
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
        "ref-239",
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
        "ref-067",
        "ref-1012"
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
        "ref-239",
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
      "id": "ref-063",
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
      "id": "ref-1012",
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
      "id": "ref-239",
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
      "id": "ref-513",
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
      "id": "ref-067",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 병원 사례와 한국어 문서 이해 자료를 더 넣지 못했다. 재사용 1건(ref-308: 참고문헌 목록 전체가 입력에 없어 값은 이전 브리프 2026-09-30-05 의 출처 표를 따랐고, 이번에 HTML 본문을 다시 열었다). 원문 열람: 16건 모두 열었다(webfetch 14건, github_raw 2건). 논문은 대부분 초록 페이지이고 Su 외(PMC 본문)·Modi 외·AAS-RAIL·Brorsson 외(arXiv HTML 본문)만 본문을 봤다. 교차 확인 0건: 수치마다 데이터·지표가 달라 같은 값을 두 출처로 확인할 수 없었고, f12·f21 은 종합 추정(low)으로 냈다. 벤더 문서는 쓰지 않았다. 분류 원문 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽어 내는가)에는 f21 로 답했고 결론은 '글자·표 파싱은 벤치마크에서 높지만 속성 추출 5~8할, 도면 심볼 세기 0.40~0.55, 고정 카메라 장면 인식은 구조 수준이라 사람 확인 없이 실행 정보로 쓰기 어렵다'는 추정이다. 현장 유형 사례는 상업 시설(f4)·제조 공장(f15~f17)·물류창고(f18)·실외(f20)·가정(f5, 주거 도면 데이터)이며 병원·기타 사례는 찾지 못했다. 국내 자료는 AI Hub 건축 도면 데이터(ref-1012) 1건이다. oq-197 해결 근거: f5·f6(비주거 도면 미포함, 공개된 객체 5종에 로봇 운영 클래스 없음; 구조·공간 라벨 전체 목록은 미확인이라 검증 판단 필요). oq-196·oq-147 은 부분 근거만 있어 해결 제안하지 않았다. 교차 규칙에 따라 매뉴얼 해석 finding(f10·f11·f13·f14)은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에, 도면 해석 finding(f1~f6)은 14. 도면·BIM에서 지도 만들기에 연결하도록 제안했다. 용어집에 이미 있는 평면도 인식·패놉틱 심볼 스포팅·파놉틱 품질·3차원 장면 그래프·협동 인지·래스터–벡터 변환·자산관리셸·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-08/verification.json

```json
{
  "run_id": "2026-09-30-08",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2601.04819 초록 열람(2026-01-08 v1, 저자 일치). 평면도 120장·질의응답 192쌍·OCR 최대 0.95·심볼 개수 세기 'often 0.40-0.55' 일치. 원문이 '흔히(often)'로 적었으므로 수치 앞에 '대개'를 붙인다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 1904.01920 초록 열람(2019-04-03). 5,000장·80개 이상 범주·다각형 조밀 주석·다중 작업 CNN 일치. 수집 지역·성능 수치는 넣지 않은 것이 맞다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2105.07147 초록 열람. 1만 장 이상·주거~상업 건물·30개 범주·벡터 그래픽·CNN-GCN 일치. 발행일 2021-11-29 는 v2 개정일이며 v1 은 2021-05-15 이므로 각주에 판을 밝힌다. 용어는 용어집 표기 '파놉틱 심볼 스포팅'으로 맞춘다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 본문 열람. Sensors 22(7), 2022-03-25, 쇼핑몰 평면도 25장·1,340개 방, 분할 92.54%·인식 90.56%·전체 83.81%, 안내판(디렉터리) 문자 인식·2단계 영역 성장, 활용처로 실내 로봇 주행 일치. 논문 평가 결과이며 로봇 현장 배치가 아니다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AI Hub 페이지 열람. 2022년·에이치씨아이플러스(주)·48,033장(평면 41,556·단면 3,262·입면 1,595·구조 1,620)·아파트·연립다세대·단독주택·구조 8·공간 12·객체 5종·YOLOv5 mAP 90.33%·DeepLabV3+ mIoU 71.2%·OCR CER 4.95%·과학기술정보통신부 표기 일치. 데이터 자원이지 가정 현장 적용 사례가 아니다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "열린 질문 이동",
      "note": "부분 불일치: 검증 열람에서 공간 12종 전체(거실·침실·주방·현관·발코니·화장실·실외기룸·드레스룸·다목적공간·엘리베이터홀·계단실·엘리베이터)가 보였다. 엘리베이터홀·엘리베이터 공간 라벨이 있으므로 '승강기 앞 대기 구역 같은 클래스는 없다'는 예시는 뒷받침되지 않는다. 충전 위치 클래스는 공개된 공간·객체 목록에 없지만, 구조 8종 가운데 출입문·창호·벽체를 뺀 5종은 여전히 미확인이다. 따라서 본문 주장으로 쓰지 않고 oq-197 의 부분 근거로만 쓴다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2412.07626 초록 열람(v1 2024-12-10, v2 2025-03-25, CVPR 2025). 9개 문서 출처·19개 레이아웃 범주·15개 속성 라벨·파이프라인과 VLM 비교 일치."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GitHub raw README 열람. v1.6(2026-04-10)·1,651쪽·10개 문서 유형·영어·간체 중국어·혼합, TeleOCR 96.91·0.0267·96.82, '연구 목적 전용, 상업 사용 불가' 일치. 순위표는 저장소 게시 값이므로 기준일을 함께 적는다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2501.17887 초록과 HTML 본문 열람(2025-01-27). 소속 'IBM Research, Rüschlikon'은 HTML 본문에서 확인했다. DocLayNet·TableFormer·MIT·일반 하드웨어·LangChain·LlamaIndex·spaCy 통합 일치."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2403.17209 초록 열람. IEEE Access 게재·'semantic node'·유효 생성률 62~79% 일치. 2024-06-24 는 arXiv v4 개정일이고 IEEE Access 게재일은 미확인이므로 각주에 이를 밝힌다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv HTML 본문 열람(2026-09-07). 4개 제조사 200쌍, 전기공학·유체동력 분야, 검색 DB 40쌍, 51.8%→71.7%, 원문에서 정답 값을 찾을 수 있는 속성 56.2%(전체 속성 기준), 전문가 검토를 남긴다는 결론 일치. 참고로 evidence_excerpt 의 '이전 오답의 22.4%'는 원문상 '전체 속성의 22.4%'이다(주장 문장에는 없다)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f10·f11 을 종합한 [추정]이다. 두 수치는 지표가 다르고(유효 생성률과 속성 추출 정확도) 대상이 로봇 매뉴얼이 아닌 일반 데이터시트라는 단서를 같은 문장에 함께 둔다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GitHub raw README 열람. 원문 위치 연결, 자체 완결 HTML 시각화, Apache 2.0, 'not an officially supported Google product', Gemini·OpenAI·Ollama 지원 일치. 발행일은 미확인. 범용 도구이므로 oq-147(로봇 매뉴얼·URDF 능력 항목)의 해결 근거는 아니다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2606.17073 초록 열람(2026-06-10, LAAS). URDF 식별자를 LLM 으로 해석해 온톨로지를 채우는 방법이며, 초록에 정량 결과가 없다는 점이 일치한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv HTML 본문 열람(v1 2025-12-17). ArUco 표식 코너로 x·y·θ를 1 Hz 로 계산해 오도메트리와 융합, 640×360 저해상도 영상의 이진 분할, 5 cm 격자, 겹치는 시야는 '대개 가장 가까운' 카메라 하나를 쓴다는 점 일치."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "대부분 확인: 카메라 15대·약 8 m·대당 약 60 m²·로봇 6대·머플러·약 150 m·주기 약 7분은 일치한다. 다만 원문은 'up to 130 transport operations are performed per day'이므로 '하루 약 130회'를 '하루 최대 130회'로 고친다. 현장은 대형 상용차(트럭) 최종 조립 공장이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: HTML 본문에서 하드웨어 비동기화로 인한 시간 차, 가림·센서 고장·제한된 범위, 작업자·독점 제품·기밀 공정 촬영 우려 문장을 확인했다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2606.06762 초록 열람(2026-06-04). 보정하지 않은 화소 단위 위상 카메라 그래프, 외부 계산만 사용, 로봇 4대·카메라 30대·27 m 통로 6개, 첫 현장 시연이라는 주장 일치. 원문은 겹치는 카메라 구역을 '배타적 자원(exclusive resources)'으로 관리해 충돌·교착을 막는다고 하므로 '순차 배정' 표현을 고친다. 저자 스스로 '첫 시연'이라 밝힌 것이므로 저자 주장으로 표기한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv HTML 본문 열람(2026-05-18). SEE 16→37 노드·재현율 0.12→0.27, 고정 카메라 3대 F1 0.421(복잡한 아파트)·0.516(가구 배치 방), '30단계 능동 탐색의 재현율에 못 미치지만 주요 구조는 잡는다'는 저자 결론 일치. 모든 실험이 시뮬레이션(Habitat·ReplicaCAD)이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "핵심 내용 확인: 초록 원문(v2 2025-07-10)에서 공유 3차원 장면 그래프(개방형 객체 지도 포함)를 통한 다중 로봇 장면 그래프 융합, 공유 장면 그래프·로봇 능력의 문맥으로 운영자 의도를 PDDL 목표로 바꾸는 방식, 대규모 실외 실제 작업 평가를 확인했다. 초록에 '대응점으로 정합' 표현은 없고, 초록 페이지에 소속 표기(MIT 등)도 없다. 이 두 부분을 고친다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "근거 finding 을 종합한 [추정]이다. 지표·데이터가 서로 달라(OCR 정확도, 종합 점수, 속성 추출 정확도, 검출 정확도, F1) 직접 비교할 수 없다는 단서를 함께 둔다. f1 수치 앞에는 '대개'를 붙인다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "근거 finding 을 종합한 [추정]이다. 문서·도면 해석 오류가 실제 실행 실패로 이어진 사례 자료는 없다는 한계를 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "영역 정의와 근거를 종합한 [추정]이다. 융합 결과가 표현하는 현재 상태는 18. 실시간 세계 상태·데이터 일관성에 둔다는 구분이 적절하다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "분류 원문 19장 기준의 연계 대상 구분([추정])이며 적절하다. 카메라망 소유·운영 주체는 출처가 밝히지 않았다는 점을 유지한다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "교차 규칙(매뉴얼 해석은 4·55, 도면 해석은 14)을 적용한 연결 [추정]이다. 다만 19. 사람·보행자 모델 연결의 근거인 f15 는 사람 인식·보행자 추적을 다루지 않으므로 이 연결은 뺀다. 34. 시뮬레이션·예측용 디지털 트윈에 연결하지 않은 것은 적절하다."
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
    "ok": false,
    "conflicts": [
      "f3·gaps·4절 제안의 '패놉틱 심볼 스포팅'은 용어집 panoptic-symbol-spotting 의 표기 '파놉틱 심볼 스포팅(Panoptic Symbol Spotting)'과 다르다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f3 및 4절: '패놉틱 심볼 스포팅'을 용어집 표기 '파놉틱 심볼 스포팅(Panoptic Symbol Spotting)'으로 고치고 용어집 페이지(docs/glossary/panoptic-symbol-spotting.md)에 링크한다 — 용어집과 표기가 충돌한다.",
    "f1·f21: 심볼 이해·개수 세기 정확도 '0.40~0.55' 앞에 '대개'를 붙인다 — ref-1088 초록이 'often 0.40-0.55'로 적었다.",
    "f16: '하루 약 130회 운반'을 '하루 최대 130회 운반'으로 고친다 — ref-308 원문이 'up to 130 transport operations are performed per day'이다.",
    "f20: '로봇마다 만든 장면 그래프와 개방형 객체 지도를 대응점으로 정합해'를 '개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고'로 고친다. 저자 표기의 'MIT 등'은 빼고 저자명(Strader 외)만 쓴다 — ref-1084 초록에 '대응점' 표현과 소속 표기가 없다.",
    "f18: '카메라 시야가 겹치는 구역을 공유 자원으로 순차 배정해 교착을 막는'을 '겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는'으로 고친다. '첫 현장 시연'은 저자가 밝힌 주장으로 쓴다. 9절에서는 로봇에 주행 장비를 두지 않는 이 방식을 ROP 기본 범위가 아니라 원문 19장의 '경계는 제품 전략에 따라 이동할 수 있다'에 해당하는 사례로 서술한다 — 원문이 'exclusive resources'라고 했고, 범위 경계를 지키기 위해서다.",
    "f6: 본문 주장으로 쓰지 않는다. '승강기 앞 대기 구역' 예시도 쓰지 않는다. 11절 oq-197 항목에 부분 근거로만 적는다: 주거 3종(아파트·연립다세대·단독주택)만 있음(f5), 공간 12종에 엘리베이터홀·엘리베이터·계단실 라벨이 있음(ref-1012, 검증 열람 확인), 공개된 공간·객체 목록에 충전 위치 클래스는 없음, 구조 8종 가운데 출입문·창호·벽체를 뺀 5종은 미확인 — 검증 열람에서 공간 라벨 전체가 확인되어 f6 의 예시와 어긋난다.",
    "oq-197: 해결로 바꾸지 않고 열림 상태로 둔다. 45번 페이지 11절과 14. 도면·BIM에서 지도 만들기 페이지 11절 모두 같다 — 구조 라벨 5종이 미확인이고 f6 이 열린 질문으로 옮겨졌다. page_proposals 1번의 11절 목록에 oq-197 을 oq-147·oq-196 과 함께 넣는다.",
    "oq-196·oq-147: 해결로 바꾸지 않는다. oq-196 에는 f3(상업 건물 포함 데이터셋)·f4(쇼핑몰 평면도 83.81~92.54%)를, oq-147 에는 f13(범용 도구 LangExtract, 로봇 문서 전용 아님)을 부분 근거로 적는다.",
    "5절: f5 를 가정 현장 적용 사례로 쓰지 않고 7·8절의 데이터 자원으로 옮긴다. site_matrix_updates 에 '가정' 칸을 넣지 않는다. 5절에는 병원·가정 현장 적용 사례를 찾지 못했다고 밝힌다 — f5 는 로봇 작업이 없는 도면 데이터셋이어서 여섯 항목을 채울 수 없다.",
    "5절 상업 시설 사례(f4): 쇼핑몰 평면도 25장에 대한 논문 평가 결과이며 로봇 현장 배치가 아님을 밝힌다. '실내 로봇 주행'은 저자가 든 활용처로 쓴다. 14. 도면·BIM에서 지도 만들기 페이지 5절에서도 같다.",
    "f12·f21: 같은 문단에 '수치들은 서로 다른 데이터·지표라 직접 비교할 수 없고, 데이터시트 연구는 로봇 매뉴얼이 아닌 일반 제품 데이터시트를 대상으로 했다'는 단서를 둔다. 이 단서는 브리프의 evidence_excerpt 에 있는 한계다.",
    "10절(f25): 19. 사람·보행자 모델 연결을 뺀다 — 근거 f15 는 사람 인식·보행자 추적을 다루지 않는다(ref-308 에 보행자 전용 추적 보고 없음).",
    "6·10절: f15·f19 의 융합 결과(현재 공간 상태)는 18. 실시간 세계 상태·데이터 일관성에 연결하고 34. 시뮬레이션·예측용 디지털 트윈에는 연결하지 않는다 — f19 의 시뮬레이션은 평가 환경일 뿐 가정한 미래를 실험하는 것이 아니다.",
    "각주 발행일: ref-067 는 '2021-11-29(v2 개정, v1 2021-05-15)', ref-1080 은 '2025-03-25(v2, v1 2024-12-10)', ref-1087 은 '2024-06-24(arXiv v4, IEEE Access 게재일 미확인)', ref-308 은 '2025-12-17'로 적는다. ref-1012·ref-1089 는 발행일을 '미확인'으로 둔다 — 검증 열람에서 판·날짜를 확인했다.",
    "용어 후보 '인프라 장착 센서' 정의에서 '사람'을 인식 대상으로 단정하지 말고 '위치·장애물 등'으로 적는다 — 근거 f15 는 사람 인식을 보고하지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 1건, 교차 확인 0건. 강등: 없음(f6 은 열린 질문으로 옮김. 검증 열람에서 AI Hub 공간 라벨 12종 전체를 확인했는데 엘리베이터홀·엘리베이터가 있어 f6 의 예시와 어긋났다). 원문 미열람 출처: 없음. 검증에서 출처 16건을 모두 다시 열었다(논문 다수는 초록 페이지, ref-1078·ref-1083·ref-1086·ref-308·ref-1082 는 본문). 이번 검증은 검색 없이 열람만으로 했다. 문구 정정: f1(대개 0.40~0.55), f16(하루 최대 130회), f18(배타적 자원), f20(대응점 정합·MIT 표기 삭제). 주의: 핵심 수치는 모두 단일 출처다. 문서 파싱·속성 추출·도면 심볼 인식·장면 인식의 수치는 지표와 데이터가 달라 직접 비교할 수 없다. 한국어 문서, 로봇 매뉴얼, 병원·공장·물류창고 같은 비주거 도면에서 측정한 자료는 없다. 병원·가정의 현장 적용 사례도 찾지 못했다. 3절(왜 중요한가)과 9절(책임 경계)은 [추정] 종합이다. oq-197 해결 불인정(구조 라벨 5종 미확인). oq-196·oq-147 은 부분 근거만 있어 열림을 유지한다. 14. 도면·BIM에서 지도 만들기 페이지의 현재 본문이 입력에 없어 그 페이지와의 중복 검사는 하지 못했다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-30-08/pages.json

```json
{
  "run_id": "2026-09-30-08",
  "outline": [
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "로봇 등록 정보는 문서·데이터시트·URDF에서, 지도는 도면 심볼에서, 공간 상태는 여러 로봇·고정 카메라 인식에서 나오므로 해석 오류가 그대로 등록 정보·지도·세계 상태 오류로 이어진다. [추정][^ref-1087][^ref-1088][^ref-308] 글자·표 파싱은 벤치마크 점수가 높지만 속성 추출·도면 심볼·장면 인식은 사람 확인 없이 쓰기 어렵다. [추정][^ref-513][^ref-1086][^ref-1083]",
      "planned_findings": [
        "f22",
        "f21",
        "f12 단서"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "문서 레이아웃 분석·표 구조 인식·출처 근거 연결·자산관리셸·파놉틱 심볼 스포팅·인프라 장착 센서·3차원 장면 그래프를 정리한다. [사실][^ref-1082][^ref-1089][^ref-067][^ref-308]",
      "planned_findings": [
        "f7",
        "f8",
        "f9",
        "f13",
        "f3",
        "f15",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2300,
      "summary": "상업 시설(쇼핑몰 평면도 인식, 논문 평가)·제조 공장(천장 카메라 15대와 로봇 6대)·물류창고(CCTV 30대로 로봇 4대 제어)·실외(공유 3차원 장면 그래프와 자연어 의도) 사례를 여섯 항목으로 정리하고, 병원·가정 사례는 찾지 못했음을 밝힌다. [사실][^ref-1078][^ref-308][^ref-1075][^ref-1084]",
      "planned_findings": [
        "f4",
        "f15",
        "f16",
        "f17",
        "f18",
        "f20"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2000,
      "summary": "문서 파싱(Docling·OmniDocBench), LLM 데이터시트 속성 추출(유효 생성률 62~79%, 51.8%→71.7%), URDF 해석, 원문 위치 근거, 도면 인식(심볼 세기 대개 0.40~0.55), 고정 카메라·로봇 인식 융합을 다룬다. [사실][^ref-1082][^ref-1087][^ref-1086][^ref-1088][^ref-1083]",
      "planned_findings": [
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f1",
        "f19",
        "f23"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "Docling·LangExtract 오픈소스, OmniDocBench·AECV-Bench 벤치마크, CubiCasa5K·FloorPlanCAD·AI Hub 건축 도면 데이터(주거 3종) 데이터셋을 표로 정리한다. [사실][^ref-1082][^ref-1089][^ref-1012]",
      "planned_findings": [
        "f9",
        "f7",
        "f8",
        "f13",
        "f1",
        "f2",
        "f3",
        "f5"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "도면 이해 벤치마크, 상업 시설 평면도 인식, 데이터시트–AAS 추출 두 편, 인프라 카메라 기반 제조 현장 배치, CCTV 기반 창고 시연, 고정 카메라 장면 그래프, 다중 로봇 공유 장면 그래프, 국내 도면 데이터를 소개한다. [사실][^ref-1088][^ref-1086][^ref-308][^ref-1012]",
      "planned_findings": [
        "f1",
        "f4",
        "f10",
        "f11",
        "f15",
        "f18",
        "f19",
        "f20",
        "f5"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 파싱·추출 파이프라인과 정확도 평가, 원문 위치 기반 검토 흐름, 플랫폼 수준 인식 융합을 맡고 로봇 온보드 인식·CCTV 설비·설계 도구는 연계 대상으로 둔다. [추정][^ref-1089][^ref-308][^ref-1084] 외부 카메라로 로봇을 직접 모는 방식은 경계가 제품 전략에 따라 옮겨간 사례로 본다. [추정][^ref-1075]",
      "planned_findings": [
        "f23",
        "f24",
        "f18"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "매뉴얼 해석은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 인식 융합 결과는 18. 실시간 세계 상태·데이터 일관성으로 이어진다. [추정][^ref-1086][^ref-1088][^ref-308]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "oq-147·oq-196·oq-197은 부분 근거만 있어 열어 두고, 한국어 문서 정확도·로봇 매뉴얼 추출 벤치마크·카메라 동기화 기준·CCTV 목적 외 이용 질문 4건을 새로 올린다. [사실][^ref-1089][^ref-1012][^ref-308]",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f6(열린 질문 이동)",
        "f13",
        "f8",
        "f11",
        "f17"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성(문서 파싱·데이터시트 속성 추출·도면 인식·고정 카메라와 로봇 인식 융합, 상업 시설·제조 공장·물류창고·실외 적용 사례), 각주 16건, 새 열린 질문 4건. 2차: 10절 첫 문장의 영역 호칭을 번호와 이름으로 고침"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"6. 대표 접근법과 기술\" 절(2,104자)을 옮겼다(2차 재실행에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"11. 열린 질문\" 절(1,145자)을 옮겼다(2차 재실행에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,004자)을 옮겼다(2차 재실행에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절을 옮겼다. 2차: 세 줄 요약 첫 항목과 본문 첫 문장의 영역 호칭을 번호와 이름으로 고침"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"4. 핵심 개념과 용어\" 절(862자)을 옮겼다(2차 재실행에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"8. 대표 연구와 자료\" 절(798자)을 옮겼다(2차 재실행에서 변경 없음)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area45-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"3. 왜 중요한가\" 절(729자)을 옮겼다(2차 재실행에서 변경 없음)"
    }
  ],
  "changelog_entry": "2026-09-30 | 45. 문서·도면·장면 이해 | 영역 심화: 3~11절 신규 작성(문서 파싱·데이터시트 속성 추출·도면 인식·고정 카메라와 로봇 인식 융합, 현장 유형 사례 4건), 각주 16건, 새 열린 질문 4건. 2차: 10절 영역 호칭을 번호와 이름으로 고침 | run 2026-09-30-08",
  "index_updates": {
    "home_recent": "2026-09-30 — 45. 문서·도면·장면 이해: 영역 심화로 3~11절 작성(문서 파싱, 데이터시트 속성 추출 5~8할, 도면 심볼 인식, 고정 카메라·로봇 인식 융합, 상업 시설·제조 공장·물류창고·실외 사례)",
    "category_recent": "2026-09-30 — 45. 문서·도면·장면 이해: 영역 심화로 3~11절 작성, 각주 16건, 새 열린 질문 4건",
    "area_recent": "2026-09-30 — 45. 문서·도면·장면 이해: 3~11절 신규 작성(문서 파싱·속성 추출·도면 인식·장면 인식 융합, 현장 유형 사례 4건, 책임 경계, 열린 질문 7건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "document-layout-analysis",
      "term_ko": "문서 레이아웃 분석",
      "term_en": "Document Layout Analysis",
      "definition": "문서 페이지 이미지나 PDF 에서 본문·제목·표·그림·수식 같은 영역을 찾아 종류를 구분하고 읽는 순서를 정하는 문서 이해의 첫 단계다.",
      "description": "Docling 은 DocLayNet 기반 모델로 레이아웃을 분석하고, OmniDocBench 는 19개 레이아웃 범주로 파싱 결과를 평가한다.",
      "related_areas": [
        45,
        4,
        55
      ],
      "sources": [
        "ref-1082",
        "ref-1080"
      ]
    },
    {
      "action": "new",
      "slug": "table-structure-recognition",
      "term_ko": "표 구조 인식",
      "term_en": "Table Structure Recognition",
      "definition": "문서 속 표의 행·열·병합 셀 구조를 복원해 표 내용을 기계가 읽을 수 있는 형식으로 바꾸는 기술로, TEDS 같은 지표로 평가한다.",
      "description": "Docling 은 TableFormer 로 표 구조를 인식하고, OmniDocBench 저장소는 표 결과를 TEDS 점수로 싣는다.",
      "related_areas": [
        45,
        4
      ],
      "sources": [
        "ref-1082",
        "ref-513"
      ]
    },
    {
      "action": "new",
      "slug": "source-grounding",
      "term_ko": "출처 근거 연결",
      "term_en": "Source Grounding",
      "definition": "언어 모델이 문서에서 추출한 항목마다 원문 속 정확한 위치를 함께 기록해 사람이 원문과 대조해 확인할 수 있게 하는 방식이다.",
      "description": "오픈소스 LangExtract 는 추출 항목마다 원문 위치를 연결하고 원문 맥락에 강조해 보여 주는 HTML 검토 화면을 만든다.",
      "related_areas": [
        45,
        4,
        7
      ],
      "sources": [
        "ref-1089"
      ]
    },
    {
      "action": "new",
      "slug": "infrastructure-mounted-sensing",
      "term_ko": "인프라 장착 센서",
      "term_en": "Infrastructure-mounted Sensing",
      "definition": "천장·벽 같은 시설에 고정한 카메라·센서로 로봇 밖에서 넓은 영역의 위치·장애물 등을 인식해 로봇 온보드 센서의 가림과 시야 한계를 보완하는 방식이다.",
      "description": "대형 상용차 조립 공장 배치에서는 천장 카메라 15대가 로봇에 붙인 표식으로 위치·방향을 계산하고 영상 분할로 장애물과 빈 공간을 구분했다.",
      "related_areas": [
        45,
        18,
        62
      ],
      "sources": [
        "ref-308"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-308",
      "org": "Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv)",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12-17",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "설비에 단 센서·계산 자원, 현장 클라우드, 로봇 온보드 자율의 세 층을 둔 사내 물류 이동 로봇 기준 아키텍처와 대형 상용차 제조 현장 배치(천장 카메라 15대·로봇 6대)를 다룬 프리프린트(v1 2025-12-17).",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    },
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-063",
      "org": "Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. (arXiv)",
      "title": "CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis",
      "published": "2019-04-03",
      "url": "https://arxiv.org/abs/1904.01920",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "평면도 이미지 5,000장을 80개 이상 범주로 다각형 주석한 데이터셋과 다중 작업 CNN. 초록 페이지만 열람(본문 PDF 텍스트 추출 실패).",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1012",
      "org": "한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주))",
      "title": "건축 도면 데이터",
      "published": null,
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2022년 구축한 주거용 건축 도면 48,033장(평면·단면·입면·구조도)과 구조·공간·객체 라벨, 객체 탐지·분할·OCR 유효성 검증 성능을 제공하는 AI 학습용 데이터 소개 페이지.",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06-10",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "URDF 의 구조·기구학 기술을 LLM 으로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 파이프라인 제안. 초록에 정량 결과 없음.",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "summary": "9개 문서 출처·19개 레이아웃 범주·15개 속성 라벨로 파이프라인 방식과 시각–언어 모델의 PDF 파싱을 다단계로 평가하는 벤치마크(CVPR 2025). 발행일은 v2 기준이며 v1 은 2024-12-10. 초록 페이지 열람.",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-513",
      "org": "OpenDataLab (opendatalab/OmniDocBench)",
      "title": "OmniDocBench — README",
      "published": "2026-04",
      "url": "https://github.com/opendatalab/OmniDocBench",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OmniDocBench v1.6 의 규모(1,651쪽, 10개 문서 유형, 영어·간체 중국어·혼합), 종단 평가 순위표, 연구 목적 전용 라이선스를 적은 공식 저장소 README. 성능 표는 저장소 게시 값.",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-067",
      "org": "Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv)",
      "title": "FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting",
      "published": "2021-11-29",
      "url": "https://arxiv.org/abs/2105.07147",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "주거·상업 건물 CAD 평면도 1만 장 이상을 벡터로 담고 30개 범주를 주석한 데이터셋과 파놉틱 심볼 스포팅 과제·CNN-GCN 기준 방법. 발행일은 v2 개정일이며 v1 은 2021-05-15. 초록 페이지 열람.",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "summary": "데이터시트 텍스트에서 의미 노드를 뽑아 LLM 에이전트로 AAS 인스턴스 모델을 생성하고 유효 생성률 62~79% 를 보고한 논문(IEEE Access 게재). 발행일은 arXiv v4 개정일이며 IEEE Access 게재일은 미확인. arXiv 초록 페이지 열람.",
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "OmniDocBench 같은 공개 문서 파싱 벤치마크에 한국어 문서가 없는데, 한국어 로봇 매뉴얼·설비 도면을 파싱·추출할 때의 정확도를 측정한 자료가 있는가?",
      "areas": [
        45,
        4
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "일반 제품 데이터시트가 아니라 로봇 매뉴얼(능력·실행 조건·오류 코드)을 대상으로 LLM 추출 정확도를 측정한 공개 벤치마크나 연구가 있는가?",
      "areas": [
        45,
        5
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가?",
      "areas": [
        45,
        18
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가?",
      "areas": [
        45,
        53
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    }
  ],
  "standards_updates": [
    {
      "name": "Docling (AI 기반 문서 변환 오픈소스 도구)",
      "kind": "오픈소스",
      "org": "IBM Research",
      "url": "https://arxiv.org/abs/2501.17887",
      "related_areas": [
        45,
        4,
        55
      ],
      "summary": "여러 문서 형식을 하나의 구조화 표현으로 바꾸는 MIT 라이선스 도구로, 레이아웃 분석에 DocLayNet 기반 모델, 표 구조 인식에 TableFormer 를 쓴다.",
      "ref_id": "ref-1082"
    },
    {
      "name": "LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리)",
      "kind": "오픈소스",
      "org": "Google (google/langextract)",
      "url": "https://github.com/google/langextract",
      "related_areas": [
        45,
        4,
        7
      ],
      "summary": "LLM 으로 비정형 텍스트에서 구조화 정보를 추출하면서 항목마다 원문 위치를 연결하고 HTML 검토 화면을 만드는 Apache 2.0 라이브러리. 구글 공식 지원 제품은 아니다.",
      "ref_id": "ref-1089"
    },
    {
      "name": "AECV-Bench (건축·엔지니어링 도면 이해 벤치마크)",
      "kind": "평가 프로그램",
      "org": "Kondratenko, A. 외 (arXiv 2601.04819)",
      "url": "https://arxiv.org/abs/2601.04819",
      "related_areas": [
        45,
        14,
        54
      ],
      "summary": "평면도 120장 개수 세기와 질의응답 192쌍으로 멀티모달 모델의 도면 이해를 평가하며, 글자 인식은 최대 0.95, 심볼 이해·개수 세기는 대개 0.40~0.55 로 보고했다.",
      "ref_id": "ref-1088"
    },
    {
      "name": "FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋)",
      "kind": "평가 프로그램",
      "org": "Fan, Z. 외 (arXiv 2105.07147)",
      "url": "https://arxiv.org/abs/2105.07147",
      "related_areas": [
        45,
        14
      ],
      "summary": "주거·상업 건물 CAD 평면도 1만 장 이상을 벡터 그래픽으로 담고 30개 범주를 주석한 데이터셋으로, 파놉틱 심볼 스포팅 과제와 기준 방법을 제시했다.",
      "ref_id": "ref-067"
    }
  ],
  "additional_research_requests": [
    "14. 도면·BIM에서 지도 만들기 페이지 5·8·11절 반영(브리프 page_proposals 2번: f4 상업 시설 사례, f1·f3·f5 자료, oq-196·oq-197 부분 근거)은 그 페이지의 현재 본문이 입력에 없어 중복 여부를 확인할 수 없으므로 이번 실행에서 미뤘다. 다음 14. 도면·BIM에서 지도 만들기 실행에서 현재 본문과 함께 반영하도록 요청한다(f4 는 논문 평가이며 로봇 배치가 아님, oq-197 은 열림 유지).",
    "5. 적용 사례 (현장 유형 명시) 절: 병원·가정(및 기타) 현장에서 문서·도면·장면 이해를 로봇 운영에 적용한 사례가 없다. 병원 고정 카메라·로봇 인식 융합이나 병원·공장·물류창고 도면 인식 사례를 조사해 달라.",
    "5절 사례들의 시작 조건·완료·인계 칸과 물류창고 시연(ref-1075)의 작업 대상·임무 시간·조율 통계, 실외 사례(ref-1084)의 로봇 대수·실험 수치가 출처 초록에 없어 미확인으로 두었다. 본문을 열어 확인해 달라.",
    "3. 왜 중요한가 절: 문서·도면 해석 오류가 실제 로봇 실행 실패로 이어진 현장 사례 자료가 없어 추정으로만 썼다. 이를 뒷받침할 사례·보고서를 조사해 달라.",
    "6·11절: 한국어 로봇 매뉴얼·설비 도면에 대한 파싱·추출 정확도, 로봇 매뉴얼(능력·실행 조건·오류 코드) 대상 LLM 추출 벤치마크 자료가 필요하다(새 열린 질문 2건의 근거).",
    "브리프가 다음 실행 후보로 제안한 4. 이기종 로봇 등록 페이지(f10·f11·f13 반영)와 18. 실시간 세계 상태·데이터 일관성 페이지(f15·f17 반영)는 이번 실행 범위 밖이므로 해당 영역 실행에서 다루도록 요청한다."
  ],
  "fixes_applied": [
    "f3 및 4절 용어 표기 — 4절·7절·이유 서술에서 '파놉틱 심볼 스포팅(Panoptic Symbol Spotting)'으로 쓰고 4절 항목을 ../../glossary/panoptic-symbol-spotting.md 로 링크했다.",
    "f1·f21 '대개' — 3절 종합 문장, 6절 도면 인식, 8절 AECV-Bench 항목의 '0.40~0.55' 앞에 모두 '대개'를 붙였다.",
    "f16 운반 횟수 — 5절 제조 공장 사례의 예외·성과 칸을 '하루 최대 130회 운반(주기 약 7분)'으로 썼다.",
    "f20 문구 — 5절 실외 사례 서술을 '개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고'로 쓰고, 저자 표기는 'Strader 외'만 써서 'MIT 등'과 '대응점' 표현을 뺐다.",
    "f18 문구와 범위 — 5절 물류창고 사례 제약 칸을 '겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는다'로 쓰고, '첫 현장 시연'은 '저자들은 이를 첫 현장 시연이라고 밝혔다'로 썼으며, 9절에서 이 방식을 ROP 기본 범위가 아닌 원문 19장의 '경계는 제품 전략에 따라 이동할 수 있다'에 해당하는 사례로 서술했다.",
    "f6 처리 — 본문 주장으로 쓰지 않았고 '승강기 앞 대기 구역' 예시도 뺐으며, 11절 oq-197 항목에 주거 3종만 있음·공간 12종의 엘리베이터홀·엘리베이터·계단실 라벨·공개 목록에 충전 위치 클래스 없음·구조 5종 미확인을 부분 근거로만 적었다.",
    "oq-197 열림 유지 — 45번 페이지 11절에 oq-147·oq-196 과 함께 [열림]으로 두었고 open_question_updates 에 해결 변경을 내지 않았다. 14. 도면·BIM에서 지도 만들기 페이지는 이번 실행에서 갱신하지 않아 그 페이지의 oq-197 상태도 바뀌지 않는다(additional_research_requests 에 미룬 사유 기재).",
    "oq-196·oq-147 부분 근거 — 11절 oq-196 에 f3(상업 건물 포함 FloorPlanCAD)·f4(쇼핑몰 평면도 83.81~92.54%), oq-147 에 f13(범용 도구 LangExtract, 로봇 문서 전용 아님)을 부분 근거로 적고 상태는 바꾸지 않았다.",
    "f5 위치 — 5절에서 가정 사례를 만들지 않고 AI Hub 건축 도면 데이터를 7절 표·설명과 8절 목록의 데이터 자원으로 옮겼으며, site_matrix_updates 에 '가정' 칸을 넣지 않고 5절 첫머리에 병원·가정 적용 사례를 찾지 못했다고 밝혔다.",
    "f4 성격 — 5절 상업 시설 사례에 '로봇 현장 배치가 아니라 쇼핑몰 평면도 25장에 대한 논문 평가 결과'임을 밝히고 '실내 로봇 주행'은 저자가 든 활용처로 썼다. 14. 도면·BIM에서 지도 만들기 페이지 5절은 이번 실행에서 갱신하지 않았다.",
    "f12·f21 단서 — 3절 종합 문단과 6절 데이터시트 추출 문단에 '서로 다른 데이터·지표라 직접 비교할 수 없고, 데이터시트 연구는 로봇 매뉴얼이 아닌 일반 제품 데이터시트를 대상으로 했다'는 단서를 같은 문단에 두었다.",
    "10절 19번 연결 삭제 — 10절 목록과 프런트매터 related_areas 에서 19. 사람·보행자 모델을 뺐다.",
    "6·10절 18/34 구분 — 6절 인식 융합 끝과 10절 18. 실시간 세계 상태·데이터 일관성 항목에서 융합 결과를 현재 상태로 18번에 연결하고 34. 시뮬레이션·예측용 디지털 트윈과 구분했으며, related_areas 에 34를 넣지 않았다. f19 는 시뮬레이션 평가 환경이라고 밝혔다.",
    "각주 발행일 — 13절에 ref-067 '2021-11-29(v2 개정, v1 2021-05-15)', ref-1080 '2025-03-25(v2, v1 2024-12-10)', ref-1087 '2024-06-24(arXiv v4, IEEE Access 게재일 미확인)', ref-308 '2025-12-17', ref-1012·ref-1089 '미확인'으로 적었다.",
    "'인프라 장착 센서' 정의 — glossary_updates 정의를 '위치·장애물 등을 인식'으로 고치고, 4절 설명도 로봇 위치·방향과 장애물·빈 공간 인식으로만 적어 사람 인식을 단정하지 않았다.",
    "분량 초과 자동 분리: 45. 문서·도면·장면 이해 본문 10,250자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,642자",
    "2차: 10절 첫 문장 영역 호칭 — 세부영역 페이지 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 절 첫 문장, docs/topics/2026/2026-09-30-area45-s10.md 의 1. 세 줄 요약 첫 항목과 3. 본문 첫 문장 세 곳을 모두 '분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.'로 같은 문장이 되게 고쳤다. 다른 부분은 바꾸지 않았다."
  ]
}
```

### runs/2026-09-30-08/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-30-08/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md

```markdown
---
title: "45. 문서·도면·장면 이해"
type: area
category: "L. AI·학습 기술"
area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [문서 파싱, 도면 인식, 자산관리셸, 출처 근거 연결, 인프라 장착 센서, 3차원 장면 그래프]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-308, ref-1075, ref-063, ref-1012, ref-1078, ref-239, ref-1080, ref-513, ref-1082, ref-1083, ref-1084, ref-067, ref-1086, ref-1087, ref-1088, ref-1089]
last_run: 2026-09-30
version: 2
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

이기종 로봇 등록과 능력 표현에 필요한 정보는 제조사 문서·데이터시트·[URDF(Unified Robot Description Format, 통합 로봇 기술 형식)](../../glossary/urdf.md)에 흩어져 있고, 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며, 로봇 한 대로는 가려지는 공간 상태는 여러 로봇과 고정 카메라의 인식을 모아야 알 수 있으므로, 이 영역의 해석 오류는 그대로 등록 정보·지도·세계 상태의 오류로 이어진다고 볼 수 있다. [추정][^ref-1087][^ref-1086][^ref-239][^ref-1088][^ref-1078][^ref-308][^ref-1075][^ref-1083]

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 왜 중요한가](../../topics/2026/2026-09-30-area45-s3.md)에 있다.

## 4. 핵심 개념과 용어

문서·도면·장면을 읽는 기술은 다음 용어로 나눠 볼 수 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area45-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 사례는 출처가 보고한 연구·시연이며, 출처가 다루지 않은 칸은 "미확인"으로 둔다. 병원·가정 현장의 적용 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 상업 시설

**사례:** 쇼핑몰 평면도에서 점포 공간 식별(논문 평가)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(출처가 다루지 않음) |
| 작업 대상 | 쇼핑몰 평면도 25장과 그 안의 점포 1,340개(공간·정보) [사실][^ref-1078] |
| 수행 자원 | 도면 인식 소프트웨어: 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고, 2단계 영역 성장 분할과 문자 인식으로 평면도의 점포 공간을 식별한다 [사실][^ref-1078] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%(2022-03 발표) [사실][^ref-1078] |

이 사례는 로봇 현장 배치가 아니라 쇼핑몰 평면도 25장에 대한 논문 평가 결과다. [사실][^ref-1078] 저자들은 실내 로봇 주행을 이 방법의 활용처 가운데 하나로 들었다. [사실][^ref-1078]

**현장 유형:** 제조 공장

**사례:** 대형 상용차 최종 조립 공장에서 천장 카메라로 운반 로봇의 위치와 장애물 인식

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 머플러를 약 150 m 구간에서 운반한다 [사실][^ref-308] |
| 수행 자원 | 약 8 m 높이에 단 카메라 15대(대당 약 60 m²)가 바닥을 덮고 로봇 6대가 운반한다. 카메라가 로봇에 붙인 ArUco 표식을 검출해 로봇 위치·방향을 계산하고, 저해상도 영상의 이진 의미 분할로 장애물과 빈 공간을 격자 단위로 구분한다 [사실][^ref-308] |
| 제약 | 카메라 간 하드웨어 동기화가 없어 생기는 시간 차 오류, 가림·센서 고장·제한된 시야 범위로 인한 위치 추정 중단, 작업자·독점 제품·기밀 공정이 영상에 찍히는 개인정보·기밀 문제 [사실][^ref-308] |
| 완료·인계 | 미확인 |
| 예외·성과 | 하루 최대 130회 운반(주기 약 7분) [사실][^ref-308]. 위치 추정이 끊겼을 때의 복구 주체는 미확인 |

카메라별 점유 지도를 전역 지도로 합칠 때 시야가 겹치는 곳은 가장 가까운 카메라 하나의 결과만 쓴다(2025-12 발표). [사실][^ref-308] 이 사례에서 이 영역이 맡는 부분은 로봇 밖의 카메라 인식 결과를 공간 상태로 모으는 일이다. [추정][^ref-308]

**현장 유형:** 물류창고

**사례:** 창고 CCTV 카메라망만으로 여러 로봇을 계획·제어하는 시연(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인(초록에 운반물 서술 없음) |
| 수행 자원 | 작업용 주행 장비를 싣지 않은 로봇 4대, 창고 CCTV 카메라 30대, 외부 계산 자원 [사실][^ref-1075] |
| 제약 | 길이 27 m 통로 6개. 시야가 겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는다 [사실][^ref-1075] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(임무 시간·조율 통계 수치가 초록에 없음) |

이 시스템은 보정하지 않은 화소 단위 위상 카메라 그래프 위, 즉 영상 공간에서 여러 로봇을 계획·제어하며, 저자들은 이를 첫 현장 시연이라고 밝혔다(2026-06 발표). [사실][^ref-1075] 로봇 주행을 외부 카메라로 옮긴 방식이므로 9절에서 경계가 이동한 사례로 다룬다.

**현장 유형:** 실외

**사례:** 운영자의 자연어 의도로 여러 로봇에 대규모 실외 작업 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운영자가 자연어로 의도를 말하면 LLM(Large Language Model, 대규모 언어 모델)이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 [PDDL(계획 도메인 정의 언어)](../../glossary/pddl.md) 목표로 바꾼다 [사실][^ref-1084] |
| 작업 대상 | 대규모 실외 환경과 그 안의 객체(개방형 객체 지도를 담은 공유 3차원 장면 그래프로 표현) [사실][^ref-1084] |
| 수행 자원 | 여러 로봇(대수 미확인)과 LLM, 다중 로봇 계획·실행 시스템 [사실][^ref-1084] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(실험 수치가 초록에 없음) |

이 시스템은 개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고, 대규모 실외 환경의 실제 작업으로 평가했다(2025-07 개정판). [사실][^ref-1084]

## 6. 대표 접근법과 기술

문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1088][^ref-1086][^ref-1083]

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area45-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에서 쓰는 도구·벤치마크·데이터셋은 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area45-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 판단 근거가 된 연구와 자료는 다음과 같다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 대표 연구와 자료](../../topics/2026/2026-09-30-area45-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 인식 결과(위치·장면 그래프)를 받아 시간·좌표를 맞춰 고정 카메라 결과와 하나의 공간 상태로 합치는 플랫폼 수준 융합 [추정][^ref-308][^ref-1084] | 연계 대상: 로봇 온보드 센서 인식·SLAM·국지 회피는 로봇 제조사가 맡는다 [추정][^ref-308][^ref-1084] |
| 시설·설비 제어 | 시설 카메라의 영상·인식 결과를 받아 해석하는 인터페이스와 검토 절차 [추정][^ref-308][^ref-1075] | 연계 대상: CCTV·영상 관리 시스템과 카메라 설치·동기화 [추정][^ref-308][^ref-1075] |

ROP가 이 영역에서 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가, 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름, 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 융합이다. [추정][^ref-1080][^ref-1082][^ref-1086][^ref-1089][^ref-308][^ref-1084] 도면·BIM 작성 도구와 원본 도면은 설계·건축 쪽의 연계 대상이고, ROP는 그 결과물을 받아 해석한다. [추정][^ref-067][^ref-1012] 카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인이다.

5절 물류창고 사례처럼 로봇에 작업용 주행 장비를 두지 않고 외부 카메라와 외부 계산으로 주행을 제어하는 방식은 ROP의 기본 범위가 아니라, [범위 경계](../../about/scope-boundary.md)의 원문 19장이 말하는 "이 경계는 제품 전략에 따라 이동할 수 있다"에 해당하는 사례로 본다. [추정][^ref-1075]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area45-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 질문과 이번 실행의 부분 근거는 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 열린 질문](../../topics/2026/2026-09-30-area45-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1075]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 미확인, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-1078]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-30
[^ref-1080]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-1082]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-1083]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1084]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1087]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1088]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-1089]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
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

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s6.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 대표 접근법과 기술"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-239, ref-1080, ref-513, ref-1082, ref-1083, ref-1084, ref-1086, ref-1087, ref-1088, ref-1089, ref-308]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#6
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 대표 접근법과 기술

# 45. 문서·도면·장면 이해 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1088][^ref-1086][^ref-1083]
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1088][^ref-1086][^ref-1083]

### 문서 파싱 — 글자·표·레이아웃을 구조화 정보로

IBM Research 가 공개한 Docling 은 여러 문서 형식을 하나의 구조화 표현으로 바꾸며, 레이아웃 분석에 DocLayNet 기반 모델, 표 구조 인식에 TableFormer 를 쓰고, 일반 하드웨어에서 적은 자원으로 동작하며 LangChain·LlamaIndex·spaCy 에 통합되어 있다(2025-01). [사실][^ref-1082] OmniDocBench 는 9개 문서 출처에 19개 레이아웃 범주와 15개 속성 라벨을 달아 파이프라인 방식과 시각–언어 모델 방식의 PDF 파싱을 전체·모듈·속성 수준에서 비교한다(CVPR 2025). [사실][^ref-1080] 저장소 README 의 2026-04 판(v1.6)은 PDF 1,651쪽·10개 문서 유형·영어와 간체 중국어·혼합 언어로 구성되고, 종단 평가 상위 모델(TeleOCR)의 종합 점수 96.91·텍스트 편집 거리 0.0267·표 TEDS 96.82 를 저장소 게시 값으로 싣는다. [사실][^ref-513] 이 벤치마크의 언어 구성에는 한국어가 없고, 데이터는 연구 목적으로만 쓸 수 있으며 상업적 사용은 허용되지 않는다. [사실][^ref-513]

### 데이터시트·로봇 기술서에서 속성 추출

Xia 외는 데이터시트 원문에서 '의미 노드'를 뽑아 LLM 에이전트로 자산관리셸 인스턴스 모델을 생성하고, 원문 정보가 오류 없이 옮겨진 비율(유효 생성률)을 62~79%로 보고했다. [사실][^ref-1087] Groß·Heidrich 의 AAS-RAIL 은 전기공학·유체동력 분야 4개 제조사의 데이터시트–AAS 쌍 200건에서, 비슷한 기존 AAS 로부터 추출 지침을 검색해 문맥 예시로 쓰는 방식으로 속성 추출 정확도를 평균 51.8%에서 71.7%로 높였으나, 원문에서 정답 속성값을 찾을 수 있는 경우가 전체 속성의 56.2%뿐이어서 전문가 검토가 여전히 필요하다고 밝혔다(2026-09). [사실][^ref-1086] 두 연구를 종합하면 오류 없이 옮겨지는 비율은 대략 5~8할이고, 원문에 정보가 없거나 이름과 값이 떨어져 있는 경우가 많아 사람의 검토 없이 등록 정보로 확정하기는 어려운 것으로 보인다. [추정][^ref-1087][^ref-1086] 다만 두 수치는 서로 다른 데이터·지표(유효 생성률과 속성 추출 정확도)라 직접 비교할 수 없고, 두 연구는 로봇 매뉴얼이 아닌 일반 제품 데이터시트를 대상으로 했다. [추정][^ref-1087][^ref-1086] 로봇 기술서 쪽에서는 Dussard·Sarthou 가 URDF 의 구조·기구학 기술 안 식별자를 LLM 이 상식으로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 채우는 파이프라인을 제안했으나, 초록에 정량 평가 결과는 없다(2026-06). [사실][^ref-239]

### 원문 위치 근거와 사람 검토

LangExtract 는 LLM 으로 비정형 텍스트에서 구조화 정보를 뽑으면서 항목마다 원문의 정확한 위치를 연결하고, 그 위치를 원문 맥락에 강조해 보여 주는 HTML 검토 화면을 만들어 사람이 대조하게 한다. [사실][^ref-1089] 이 도구는 범용 추출 도구이며 구글의 공식 지원 제품이 아니라고 밝힌다. [사실][^ref-1089]

### 도면 인식

AECV-Bench 는 평면도 120장의 문·창·침실·화장실 개수 세기와 질의응답 192쌍으로 최신 멀티모달 모델을 평가해, 글자 인식·텍스트 추출은 정확도 최대 0.95 로 가장 높고 공간 추론은 중간, 심볼 이해·개수 세기는 대개 0.40~0.55 로 가장 낮다고 보고했다(2026-01). [사실][^ref-1088] 전용 도면 인식 모델의 예는 5절의 쇼핑몰 평면도 연구이고, 학습 데이터는 7절에 정리했다.

### 고정 카메라와 여러 로봇의 인식 융합

5절의 제조 공장·물류창고 사례처럼 시설 카메라로 로봇 위치·장애물을 인식하거나 로봇 주행 자체를 제어하는 방식이 있다. [사실][^ref-308][^ref-1075] Modi 외는 RGB 카메라만으로 3차원 장면 그래프를 만드는 능동 탐색 방법을 제안하고, 천장 쪽 고정 외부 카메라 1대로 초기화하면 기준 방법의 장면 그래프 노드 수가 16개에서 37개로, 재현율이 0.12에서 0.27로 늘었으며, 로봇 없이 고정 카메라 3대만 쓰면 F1 이 0.421(복잡한 아파트)·0.516(가구 배치 방)으로 30단계 능동 탐색의 재현율에는 못 미치지만 환경의 주요 구조는 잡는다고 보고했다(2026-05). [사실][^ref-1083] 이 연구의 실험은 모두 시뮬레이션(ReplicaCAD) 평가 환경에서 이뤄졌다. [사실][^ref-1083] 이렇게 모은 인식 결과가 표현하는 것은 현재 공간 상태이므로 18. 실시간 세계 상태·데이터 일관성으로 넘기는 입력이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈의 내용이 아니다. [추정][^ref-308][^ref-1084]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-30
[^ref-1080]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-513]: OpenDataLab (opendatalab/OmniDocBench), OmniDocBench — README, 2026-04, https://github.com/opendatalab/OmniDocBench, 접근일 2026-09-30
[^ref-1082]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-1083]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1084]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1087]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1088]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-1089]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s11.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 열린 질문"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1012, ref-1078, ref-513, ref-067, ref-1086, ref-1089, ref-308]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#11
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 열린 질문

# 45. 문서·도면·장면 이해 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 질문과 이번 실행의 부분 근거는 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 질문과 이번 실행의 부분 근거는 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-147** [조사 중] 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? 이번 실행에서는 범용 도구 LangExtract 가 추출 항목마다 원문 위치를 연결한다는 점만 확인했고, 이는 로봇 문서 전용 도구가 아니다. [사실][^ref-1089] 로봇 매뉴얼·URDF 능력 항목에 원문 위치를 붙인 공개 구현은 찾지 못했다.
- **oq-196** [열림] Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가? 부분 근거로, FloorPlanCAD 는 상업 건물 도면을 포함하고 [사실][^ref-067], 쇼핑몰 평면도에서 공간 분할 92.54%·전체 검출 83.81%가 보고됐다. [사실][^ref-1078] 병원·공장·물류창고 도면에서 측정한 자료는 찾지 못했다.
- **oq-197** [열림] AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? 부분 근거로, 건물 용도는 아파트·연립다세대·단독주택의 주거 3종뿐이다. [사실][^ref-1012] 공간 12종에는 엘리베이터홀·엘리베이터·계단실 라벨이 있고, 공개된 공간·객체 목록에는 충전 위치 클래스가 없다. [사실][^ref-1012] 구조 8종 가운데 출입문·창호·벽체를 뺀 5종의 이름은 확인하지 못했다(미확인).
- 새 질문: OmniDocBench 같은 공개 문서 파싱 벤치마크에 한국어 문서가 없는데, 한국어 로봇 매뉴얼·설비 도면을 파싱·추출할 때의 정확도를 측정한 자료가 있는가?[^ref-513]
- 새 질문: 일반 제품 데이터시트가 아니라 로봇 매뉴얼(능력·실행 조건·오류 코드)을 대상으로 LLM 추출 정확도를 측정한 공개 벤치마크나 연구가 있는가?[^ref-1086]
- 새 질문: 하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가?[^ref-308]
- 새 질문: 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가?[^ref-308]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 미확인, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-1078]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-513]: OpenDataLab (opendatalab/OmniDocBench), OmniDocBench — README, 2026-04, https://github.com/opendatalab/OmniDocBench, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1089]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s7.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-063, ref-1012, ref-1080, ref-513, ref-1082, ref-067, ref-1088, ref-1089]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#7
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스

# 45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에서 쓰는 도구·벤치마크·데이터셋은 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에서 쓰는 도구·벤치마크·데이터셋은 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Docling | 오픈소스(MIT) | 여러 문서 형식을 레이아웃·표를 포함한 구조화 표현으로 변환 | [사실][^ref-1082] |
| OmniDocBench | 평가 프로그램(벤치마크, 연구 목적 전용) | PDF 문서 파싱을 전체·모듈·속성 수준에서 비교 평가, 영어·간체 중국어 | [사실][^ref-1080][^ref-513] |
| LangExtract | 오픈소스(Apache 2.0) | 추출 항목마다 원문 위치를 연결하고 HTML 검토 화면 생성 | [사실][^ref-1089] |
| AECV-Bench | 평가 프로그램(벤치마크) | 멀티모달 모델의 건축·엔지니어링 도면 이해 평가 | [사실][^ref-1088] |
| CubiCasa5K | 데이터셋 | 평면도 이미지 5,000장을 80개가 넘는 범주로 다각형 단위 조밀 주석, 다중 작업 합성곱 신경망 모델 공개(2019-04) | [사실][^ref-063] |
| FloorPlanCAD | 데이터셋·과제 | 주거·상업 건물 CAD 평면도 1만 장 이상을 벡터로 담고 30개 범주 주석, 파놉틱 심볼 스포팅 과제 제안 | [사실][^ref-067] |
| AI Hub 건축 도면 데이터 | 데이터셋(국내 공공) | 주거용 건축 도면과 구조·공간·객체 라벨, 유효성 검증 성능 제공 | [사실][^ref-1012] |

과학기술정보통신부·한국지능정보사회진흥원의 AI Hub 「건축 도면 데이터」(2022년 구축, 주관 에이치씨아이플러스)는 도면 48,033장(평면도 41,556·단면도 3,262·입면도 1,595·구조도 1,620)을 아파트·연립다세대·단독주택의 주거 용도로만 구성하고, 구조 8종(출입문·창호·벽체 등)·공간 12종(거실·침실·주방 등)·객체 5종(변기·세면대·싱크대·욕조·가스레인지) 라벨을 두며, 유효성 검증 모델 성능으로 YOLOv5 객체 탐지 mAP 90.33%, DeepLabV3+ 분할 mIoU 71.2%, 문자 인식 CER 4.95%를 제시한다. [사실][^ref-1012] 이 데이터는 도면 학습 자원이며 로봇 현장 적용 사례가 아니다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. (arXiv), CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04-03, https://arxiv.org/abs/1904.01920, 접근일 2026-09-30
[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 미확인, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-1080]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-513]: OpenDataLab (opendatalab/OmniDocBench), OmniDocBench — README, 2026-04, https://github.com/opendatalab/OmniDocBench, 접근일 2026-09-30
[^ref-1082]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1088]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-1089]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s10.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 다른 연구영역과의 연결"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1078, ref-239, ref-1080, ref-1083, ref-1084, ref-1086, ref-1087, ref-1088, ref-1089, ref-308]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#10
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 다른 연구영역과의 연결

# 45. 문서·도면·장면 이해 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.

- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 데이터시트·URDF 에서 추출한 정보가 등록 정보로 들어간다. [추정][^ref-1087][^ref-1086][^ref-239]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 매뉴얼 해석이 적용되는 또 하나의 영역이다. [추정][^ref-1086][^ref-239]
- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — URDF 해석으로 채운 온톨로지 개념이 능력 표현으로 이어진다. [추정][^ref-239]
- [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md) — 원문 위치를 붙인 추출 결과를 사람이 확정·반려하는 검토와 이어진다. [추정][^ref-1089]
- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 도면 인식 벤치마크·데이터셋·평면도 인식 결과가 지도 만들기의 입력이다. [추정][^ref-1088][^ref-1078]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md)과 [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 평면도에서 식별한 점포 공간과 공유 장면 그래프가 지도와 장소 의미가 된다. [추정][^ref-1078][^ref-1084]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 고정 카메라·로봇 인식을 합친 결과가 담는 현재 상태가 여기로 간다(가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 구분한다). [추정][^ref-308][^ref-1083]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — LLM 이 장면 그래프 문맥으로 운영자 의도를 계획 목표로 바꾼다. [추정][^ref-1084]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 5~8할 수준의 추출 결과를 실행에 쓸 기준을 정하는 영역이다. [추정][^ref-1087][^ref-1086]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 시설 카메라에 작업자·기밀 공정이 찍히는 문제가 있다. [추정][^ref-308]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — AECV-Bench·OmniDocBench 같은 벤치마크가 정확도 평가의 틀이다. [추정][^ref-1088][^ref-1080]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md) — 5절 적용 사례의 현장 유형이다. [추정][^ref-1075][^ref-308][^ref-1078][^ref-1084]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-1078]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-30
[^ref-1080]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-1083]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1084]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1087]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1088]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-1089]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s4.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 핵심 개념과 용어"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-513, ref-1082, ref-1083, ref-1084, ref-067, ref-1086, ref-1087, ref-1089, ref-308]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#4
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 핵심 개념과 용어

# 45. 문서·도면·장면 이해 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 문서·도면·장면을 읽는 기술은 다음 용어로 나눠 볼 수 있다.
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

문서·도면·장면을 읽는 기술은 다음 용어로 나눠 볼 수 있다.

- **문서 레이아웃 분석(Document Layout Analysis)** — 문서 페이지에서 본문·제목·표·그림 같은 영역을 찾아 종류를 가르는 단계로, Docling 은 DocLayNet 기반 모델로 이 일을 한다. [사실][^ref-1082]
- **표 구조 인식(Table Structure Recognition)** — 표의 행·열 구조를 복원하는 단계로, Docling 은 TableFormer 를 쓰고 OmniDocBench 는 표 결과를 TEDS 점수로 싣는다. [사실][^ref-1082][^ref-513]
- **출처 근거 연결(Source Grounding)** — 언어 모델이 추출한 항목마다 원문 텍스트의 정확한 위치를 연결해 사람이 원문과 대조하게 하는 방식으로, 오픈소스 LangExtract 가 이렇게 동작한다. [사실][^ref-1089]
- **[자산관리셸(Asset Administration Shell, AAS)](../../glossary/asset-administration-shell.md)** — 데이터시트에서 뽑은 속성을 옮겨 담는 표준 자산 모델로, 데이터시트 추출 연구 두 편이 목표 형식으로 썼다. [사실][^ref-1087][^ref-1086]
- **[파놉틱 심볼 스포팅(Panoptic Symbol Spotting)](../../glossary/panoptic-symbol-spotting.md)** — 도면에서 셀 수 있는 심볼 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 찾는 과제로, FloorPlanCAD 가 제안했다. [사실][^ref-067]
- **인프라 장착 센서(Infrastructure-mounted Sensing)** — 천장 등 시설에 고정한 카메라로 로봇 밖에서 로봇의 위치·방향과 장애물·빈 공간을 인식하는 방식이다. [사실][^ref-308]
- **[3차원 장면 그래프(3D Scene Graph)](../../glossary/3d-scene-graph.md)** — 장면 인식 결과를 담는 표현으로, RGB 카메라만으로 만들거나 여러 로봇의 장면 그래프를 하나의 공유 그래프로 합치는 연구가 있다. [사실][^ref-1083][^ref-1084]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-513]: OpenDataLab (opendatalab/OmniDocBench), OmniDocBench — README, 2026-04, https://github.com/opendatalab/OmniDocBench, 접근일 2026-09-30
[^ref-1082]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-1083]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1084]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1087]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1089]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s8.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 대표 연구와 자료"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1012, ref-1078, ref-1083, ref-1084, ref-1086, ref-1087, ref-1088, ref-308]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#8
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 대표 연구와 자료

# 45. 문서·도면·장면 이해 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 판단 근거가 된 연구와 자료는 다음과 같다.
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 판단 근거가 된 연구와 자료는 다음과 같다.

- Kondratenko 외, AECV-Bench(2026) — 멀티모달 모델이 도면의 글자는 잘 읽지만 심볼 이해·개수 세기는 대개 0.40~0.55 에 그친다는 벤치마크 결과. [사실][^ref-1088]
- Su 외, 쇼핑몰 평면도 분할·인식(Sensors, 2022) — 상업 시설 평면도에서 전체 검출 정확도 83.81%를 보고한 동료심사 논문. [사실][^ref-1078]
- Xia 외, LLM 에이전트로 자산관리셸 생성(IEEE Access, 2024) — 데이터시트에서 AAS 로 옮길 때 유효 생성률 62~79%. [사실][^ref-1087]
- Groß·Heidrich, AAS-RAIL(2026) — 검색 기반 문맥 예시로 속성 추출 정확도 51.8%→71.7%, 원문에서 확인 가능한 속성은 56.2%. [사실][^ref-1086]
- Brorsson 외, 인프라 기반 사내 물류 이동 로봇(2025) — 천장 카메라 15대·로봇 6대의 제조 현장 배치와 동기화·가림·개인정보 한계. [사실][^ref-308]
- Robinson 외, 실제 창고의 CCTV 카메라망 기반 다중 로봇 계획·제어(2026) — 로봇 4대·카메라 30대 시연. [사실][^ref-1075]
- Modi 외, RGB 기반 능동 3차원 장면 그래프 생성(2026) — 고정 외부 카메라를 장면 그래프에 통합한 효과를 시뮬레이션에서 측정. [사실][^ref-1083]
- Strader 외, 다중 로봇 3차원 장면 그래프 기반 언어 계획·실행(2025) — 공유 장면 그래프와 LLM 의 PDDL 목표 변환을 대규모 실외에서 평가. [사실][^ref-1084]
- 한국지능정보사회진흥원 AI Hub, 건축 도면 데이터(2022년 구축) — 주거 용도만 담은 국내 공개 도면 학습 데이터. [사실][^ref-1012]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 미확인, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-1078]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-1083]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1084]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1087]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1088]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-08/pages/topics/2026/2026-09-30-area45-s3.md

```markdown
---
title: "45. 문서·도면·장면 이해 — 왜 중요한가"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1075, ref-1078, ref-239, ref-513, ref-1083, ref-1086, ref-1087, ref-1088, ref-308]
last_run: 2026-09-30
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#3
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 왜 중요한가

# 45. 문서·도면·장면 이해 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이기종 로봇 등록과 능력 표현에 필요한 정보는 제조사 문서·데이터시트·[URDF(Unified Robot Description Format, 통합 로봇 기술 형식)](../../glossary/urdf.md)에 흩어져 있고, 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며, 로봇 한 대로는 가려지는 공간 상태는 여러 로봇과 고정 카메라의 인식을 모아야 알 수 있으므로, 이 영역의 해석 오류는 그대로 등록 정보·지도·세계 상태의 오류로 이어진다고 볼 수 있다. [추정][^ref-1087][^ref-1086][^ref-239][^ref-1088][^ref-1078][^ref-308][^ref-1075][^ref-1083]
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이기종 로봇 등록과 능력 표현에 필요한 정보는 제조사 문서·데이터시트·[URDF(Unified Robot Description Format, 통합 로봇 기술 형식)](../../glossary/urdf.md)에 흩어져 있고, 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며, 로봇 한 대로는 가려지는 공간 상태는 여러 로봇과 고정 카메라의 인식을 모아야 알 수 있으므로, 이 영역의 해석 오류는 그대로 등록 정보·지도·세계 상태의 오류로 이어진다고 볼 수 있다. [추정][^ref-1087][^ref-1086][^ref-239][^ref-1088][^ref-1078][^ref-308][^ref-1075][^ref-1083] 문서·도면 해석 오류가 실제 실행 실패로 이어진 현장 사례 자료는 이번 조사에서 찾지 못했다(미확인).

2절의 핵심 질문에 지금까지 확인한 자료로 답하면 이렇다. 문서의 글자·표를 읽는 파싱은 공개 벤치마크에서 높은 점수를 내지만, 데이터시트의 속성값을 표준 자산 모델로 옮기는 정확도는 5~8할 수준이고, 멀티모달 모델의 도면 심볼 개수 세기는 대개 0.40~0.55에 그치며, 전용 도면 인식 모델도 상업 시설 평면도에서 전체 검출 약 84% 수준이고, 고정 카메라 장면 인식은 구조는 잡되 세부 객체 재현율이 낮아, 어느 쪽도 사람 확인 없이 실행 정보로 쓰기에는 부족한 것으로 보인다. [추정][^ref-1088][^ref-513][^ref-1087][^ref-1086][^ref-1078][^ref-1083] 이 수치들은 서로 다른 데이터·지표(글자 인식 정확도, 종합 점수, 속성 추출 정확도, 검출 정확도, F1)라 직접 비교할 수 없고, 데이터시트 연구는 로봇 매뉴얼이 아닌 일반 제품 데이터시트를 대상으로 했으며, 한국어 문서·로봇 매뉴얼·비주거 도면에서 측정한 자료는 찾지 못했다. [추정][^ref-1087][^ref-1086][^ref-513]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [7. 온톨로지 검증·변경 관리](../../categories/robot-ontology/ontology-verification-and-change-management.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-1078]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-30
[^ref-513]: OpenDataLab (opendatalab/OmniDocBench), OmniDocBench — README, 2026-04, https://github.com/opendatalab/OmniDocBench, 접근일 2026-09-30
[^ref-1083]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1086]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1087]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1088]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-08 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-08 | 45. 문서·도면·장면 이해 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1064건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 289개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- guidance-graph: 안내 그래프 (Guidance Graph)
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
- imitation-learning: 모방 학습 (Imitation Learning)
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
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
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
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
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

### docs/open-questions.md (요약: 대상 영역 [45] 에 걸린 3건 / 전체 224건)

```markdown
- oq-147 [조사 중] 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (영역 4, 45, 7)
- oq-196 [열림] Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가? (영역 14, 45)
- oq-197 [열림] AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? (영역 14, 45)
```

### runs/2026-09-30-08/verification2.json

```json
{
  "run_id": "2026-09-30-08",
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
    "세부영역 페이지 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 절 첫 문장(자동 분리된 docs/topics/2026/2026-09-30-area45-s10.md 의 1. 세 줄 요약 첫 항목과 3. 본문 첫 문장에도 그대로 옮겨짐): '매뉴얼 해석은 4·55번 영역에, 도면 해석은 14번 영역에 적용되는 연구 방법으로 연결한다'를 '매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다'로 고친다. 이유: 분류 원문을 그대로 옮긴 인용문이 아니라 스토리텔러가 쓴 문장인데 세부영역을 번호만으로 불렀다(공통 규칙 6절 항목 호칭, verifier.md 11절 항목 6). 세 곳이 모두 같은 문장이어야 한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 1차: 확인 24건, 미확인 1건, 교차 확인 0건. 강등: 없음(f6은 열린 질문으로 옮김. AI Hub 공간 라벨 12종에 엘리베이터홀·엘리베이터가 있어 f6의 예시와 어긋났다). 원문 미열람 출처: 없음. 문구 정정: f1(대개 0.40~0.55), f16(하루 최대 130회), f18(배타적 자원), f20(대응점 정합·MIT 표기 삭제). 주의: 핵심 수치는 모두 단일 출처다. 문서 파싱·속성 추출·도면 심볼 인식·장면 인식의 수치는 지표와 데이터가 달라 직접 비교할 수 없다. 한국어 문서, 로봇 매뉴얼, 비주거 도면에서 측정한 자료는 없고 병원·가정 현장 적용 사례도 찾지 못했다. 3절(왜 중요한가)과 9절(책임 경계)은 [추정] 종합이다. oq-197은 해결로 인정하지 않았고, oq-196·oq-147은 부분 근거만 있어 열어 둔다. 2차: 드리프트 없음. [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 통과). 1차 수정 지시 15건은 모두 이행을 확인했다. 파놉틱 표기와 용어집 링크, '대개', '하루 최대 130회', 배타적 자원, 첫 현장 시연을 저자 주장으로 쓴 점, 9절 경계 이동 사례 서술, f6의 oq-197 부분 근거 처리, f5의 7·8절 이동과 가정 칸 제외, f4가 논문 평가라는 명시, 비교 불가 단서, 19번 연결 삭제, 18번과 34번의 구분, 각주 판·날짜, '인프라 장착 센서' 정의가 이에 해당한다. 태그를 올린 문장은 없다. site_matrix_updates 12칸은 5절 사례 표에서 채운 칸과 일치한다. 수정 지시는 1건이다. 10절(과 자동 분리된 주제 페이지)의 '4·55번 영역', '14번 영역'이 번호만으로 영역을 불렀다. 참고: 5절 제조 공장 사례의 '최종 조립 공장'은 1차 검증 열람에서 확인한 내용이다. 세부영역 페이지 프런트매터 sources의 ref-063·ref-513은 분리된 주제 페이지에서만 인용된다. 분리 주제 페이지의 9. 검증 노트는 코드 템플릿 문구이며 1차 판정·건수를 싣지 않는다. 퍼블리셔 담당 확인 사항으로 남긴다. 14. 도면·BIM에서 지도 만들기 페이지 반영은 입력 부족으로 다음 실행에 넘겼다. 정정 요청은 없다.",
  "retry_reason": null
}
```
