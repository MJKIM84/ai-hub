(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-07
- date: 2026-10-12
- run_type: update (갱신)
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

## 입력

### runs/2026-10-12-07/target.json

```json
{
  "run_id": "2026-10-12-07",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 179,
  "run_type": "update",
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
  "selection_rationale": "CLI 지정 run_type=update, area=45"
}
```

### runs/2026-10-12-07/research.json

```json
{
  "run_id": "2026-10-12-07",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 45,
    "area_name": "45. 문서·도면·장면 이해",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 5. 적용 사례 — 실외 표(116·119행)가 '여러 로봇(대수 미확인)', '미확인(실험 수치가 초록에 없음)'으로 초록 기준이고, 물류창고 표(95·100·101·104행)가 '창고 CCTV 카메라 30대'로 기존 시설 CCTV 처럼 읽히며 작업 대상·예외·성과가 미확인",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area45-s6) — AAS-RAIL 문장(45행)에 56.2%의 산출 조건(낙관적 정규식)과 고정 슬롯 평가 조건이 없고, LangExtract 소절(49행)에 원문 위치를 못 찾는 경우의 표시가 없으며, 도면 인식 소절에 입력 형식·제외 객체가, 융합 소절에 관측 주기·좌표 기준 조건이 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area45-s7) — 근거 위치 자료형(Docling ProvenanceItem), 장면 그래프 파일 API(Spark-DSG), 한국어 문서 OCR 평가 자원, BIM 좌표 변환 범위(IfcMapConversion) 없음. AI Hub 문단(49행)에 메타데이터 필드 없음",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area45-s8) — Raster2Seq·면적 추정(Aliyev·Barsi)·Hydra-Multi·BIM-Loc 없음, AAS-RAIL(42행)·Robinson(44행)·Strader(46행) 항목의 조건 미기재",
    "섹션 9. 책임 경계 — '카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인'(148행)",
    "섹션 11. 열린 질문(분리 2026-09-30-area45-s11) — oq-147·oq-196·oq-225·oq-226·oq-227 의 부분 근거 갱신 필요. oq-197 은 이미 해결(도면 트랙 stage-2 q2-04)이라 대상이 아님",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 창고 카메라 30대의 설치 주체, Strader 실물 2대·데이터셋 3대 구분, AAS-RAIL 56.2% 조건"
  ],
  "research_questions": [
    "매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]",
    "oq-196 관련: 보고된 도면 인식 점수는 어떤 입력 형식·판정 기준·제외 객체·평가 분모 위에서 나왔으며 비주거 시설 도면에 옮길 수 있는가? (섹션 6·8 겨냥)",
    "oq-147·oq-226 관련: 데이터시트·URDF 추출 정확도 수치는 어떤 조건의 값이며, 공개 구현은 추출 항목의 원문 위치를 찾지 못한 경우를 어떻게 표시하는가? (섹션 6·7·8 겨냥)",
    "다중 로봇 장면 그래프·카메라망 기반 다중 로봇 실증은 실물 로봇 몇 대·어떤 카메라·어떤 판정 기준으로 무엇을 보였고 사람 개입은 얼마나 있었는가? (섹션 5·8·9 겨냥)",
    "oq-227 관련: 고정 카메라와 로봇 관측을 합칠 때 공개 자료는 관측 주기·동기화·좌표 기준을 어떻게 다루는가, BIM 좌표·현장 정합의 조건은 무엇인가? (섹션 6·7 겨냥)",
    "oq-225 관련: 한국어 문서 OCR·파싱 평가 자원과 국내 도면 데이터의 메타데이터는 무엇을 담고 무엇이 빠져 있는가? (섹션 7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "AECV-Bench 의 평가는 모두 원본 CAD·BIM 형식(DWG, RVT, IFC)이 아닌 래스터 PNG 도면 영상을 입력으로 쓴다. 벡터 기하나 객체 계층을 쓰는 모델은 평가하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1073"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 PDF 6절 한계 'Focus on 2D raster images'(p.19): \"All evaluations use rasterized PNG images of drawings rather than native CAD or BIM formats (DWG, RVT, IFC)\". 평면도 120장·QA 192쌍 벤치마크의 범위 조건",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "AECV-Bench 의 개수 세기 과제는 문·창·침실·화장실 4종만 다루며, 계단·엘리베이터·기계 설비·구조 부재·내화 구성(fire-rated assemblies)은 평가하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1073"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 PDF 6절 한계 'Limited object classes'(p.20): \"stairs, elevators, mechanical equipment, structural members, fire-rated assemblies, are not evaluated\". 메모는 앞의 세 종류만 적었으나 검증에서 다섯 종류를 함께 적도록 보완",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Raster2Seq 는 선행 연구(Stekovic 외 2021, MonteFloor)의 평가 프로토콜을 따라 정답 방마다 IoU 가 가장 큰 예측 방을 짝지어 Room·Corner·Angle 을 정밀도·재현율·F1 으로 평가하며, 방 단위 짝은 IoU 가 0.5 를 넘을 때 유효로 본다.",
      "tag": "사실",
      "source_ids": [
        "ref-1667"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v3 §4.1 Metrics: \"We follow the evaluation protocol used by prior work [Stekovic et al. 2021]\" … \"a match is considered valid if the IoU exceeds 0.5\". 모든 데이터셋을 256×256 고정 해상도로 실험. 통과 폭·지도 안전성 지표가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Raster2Seq 의 모서리 판정(예측과 정답 모서리 거리 10픽셀 이내, 각도 차 5도 미만)은 이 논문 고유 기준이 아니라 Stekovic 외(2021)의 프로토콜을 따른 것이며, 256×256 영상 기준의 픽셀 허용 오차다.",
      "tag": "사실",
      "source_ids": [
        "ref-1667"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v3 §4.1: \"we follow the protocol of [Stekovic et al. 2021] … A corner is considered correctly recovered if the distance is within 10 pixels and the angle difference is less than 5 degrees\". 메모 F04 를 선행 프로토콜 기준으로 정정. 시설별 미터 허용 오차와 다름",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Raster2Seq 는 한계로, 문·창처럼 드문 의미 구조의 위치를 가끔(occasionally) 잘못 잡아 방 내부에 문·창을 생성하는 실패 예를 제시하며, 이 실패의 발생률은 보고하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1667"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v3 §4.5 Limitations·Fig. 8: \"the model occasionally fails to accurately localize windows and doors\", 캡션 \"may generate windows and doors inside rooms\". 전체 데이터에서의 발생 비율 수치 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Aliyev·Barsi 의 실험에서 BakLLaVA 는 색상으로 방 유형을 구분한 주거 평면도 100장 모두에서 실제 예측 대신 템플릿 자리표시자를 출력해(검증 실패 시 1회 재시도 후 사용 불가 처리) 정량 평가에서 제외됐고, LLaVA-LLaMA 3 와 MiniCPM-V 2.6 만 평가됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1668"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.4(p.895): \"Responses failing validation were retried once\" … \"BakLLaVA consistently returned template placeholders rather than genuine predictions across all 100 plans and we excluded it\". 본문 모델명 LLaVA-LLaMA 3, 보충자료 modelfile 은 llama3.2-vision",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "이 연구는 방을 개체 단위가 아니라 방 유형 단위로 맞춘다. 한 도면 안 같은 유형의 정답 면적을 합쳐 비교점 하나로 만들어, 정답 방 다각형 894개에서 비교 쌍 472개를 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1668"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.4(p.895): \"all ground-truth instances of the same type within a plan were aggregated into a single comparison point\" … \"resulting in 472 matched comparisons in total (100 plans × up to 5 room types, minus 27 … 1 …)\". 주거 도면만 대상",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "같은 논문 안에서 픽셀 세기 기준선의 평가 단위 서술이 어긋난다. 초록은 MAPE 5.68%를 방 개체 단위, 1.58%를 도면 단위라고 적지만, §4.1·표 2 는 5.68%를 방 유형별 도면 단위 비교 472쌍 전체의 값으로 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1668"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"MAPE = 5.68% at the room-instance level, and MAPE = 1.58% when evaluated at the floor plan level\". §4.1: \"aggregated across all 472 plan-level room-type comparisons … MAPE 5.68 ± 7.21%\", 표 2 제목 \"plan-level evaluation\". 어느 쪽이 맞는지는 판단하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "ROP 가 도면 인식 점수를 인용할 때는 입력 형식(래스터/벡터·BIM), 평가에서 빠진 객체, 판정 기준(IoU·픽셀 허용 오차), 평가 분모(유효 출력 표본과 전체 표본)를 함께 적어야 하며, 픽셀 기준 점수를 미터 단위 통과 가능성으로 바꿔 읽지 않고 승강기·방화문·충전 위치 같은 운영 객체는 별도 인수 시험으로 확인해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1073",
        "ref-1667",
        "ref-1668"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2(입력 PNG·미평가 객체), f3·f4(IoU 0.5·10 px/5° at 256×256), f6·f7·f8(유효 출력 제외와 집계 단위)에서 도출. 메모 A01~A03 'ROP 시사점'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "IFC 4.3 의 IfcMapConversion 은 국지 공학 좌표계를 지도 좌표계로 옮기는 변환(세 축 공통 축척 하나로 단위 변환, z축 기준 반시계 회전, Eastings·Northings·OrthogonalHeight 이동)을 기술하며, 지리 좌표계에서 지도로의 투영 자체는 다루지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1669"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ifc4.3-main 원본 IfcMapConversion.md: \"NOTE The IfcMapConversion does not handle the projection of a map from the geodetic coordinate reference system.\" 축척·회전·이동 정의 같은 문서. 공식 HTML(IFC4.3.2.0)은 Cloudflare 차단으로 못 열어 판·절 번호는 적지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "BIM-Loc 의 실제 공사장 데이터(홍콩시립대 공사 현장)는 손에 든 센서로 Ouster OS0-128 7개·Livox Mid-360 2개, 모두 9개 시퀀스(누적 3.5 km 초과)로 구성되며, 운용 중인 로봇 대수와는 무관하다.",
      "tag": "사실",
      "source_ids": [
        "ref-1670"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 §4.2.1: 공사장 \"9 data sequences\", 두 LiDAR(Ouster OS0-128, Livox Mid-360)로 수집, 누적 3.5 km 초과, handheld sensor suite. 사무실 벤치마크(HKUST, 9개 시퀀스)와 구별",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "BIM-Loc 의 공사장 실험에는 정답 궤적이 없어, 사무실 실험의 절대 궤적 오차(ATE) 대신 MME·scan-to-BIM·Wasserstein 같은 대리 지표로 평가한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1670"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 §4.2.3: \"where ground truth trajectories were unavailable\" → 대리 지표(MME, scan-to-BIM, Wasserstein). IJRR 게재판(DOI 10.1177/02783649261462593)과 문구 대조는 하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "Hilti × Trimble 2026 SLAM 챌린지 데이터 설명은 평면도가 공사 종료 시점의 의도된(완공) 상태를 보여 주며, 공사 중 벽·기둥이 차례로 지어지므로 이른 시기 기록에는 평면도 요소가 모두 있지는 않다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1676"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: README 'Dataset Floorplans': \"The floorplans show the intended state of the building at the end of construction … not all elements are present in the earlier recordings.\" Hilti·Trimble·Oxford DRS 공동 산업 벤치마크 저장소(고정 커밋 e0c9277)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "같은 저장소는 2026-09-21 에 정답 수집 장치의 센서 동기화 설명을 추가했다고 기록하며, 그 설명은 정답 LiDAR·IMU 는 PPS 신호로 하드웨어 동기화하고 독립 동작하는 Insta360 은 두 IMU 신호의 자이로 크기를 맞춰 시간 오프셋과 시계 배율을 추정해 맞춘다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1676"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: README News \"[2026-09-21] Added the explanation about the sensors synchronization in the ground truth collection device\", 'Sensors synchronization' 절. 문서 변경 기록이며 동기화 효과 수치·허용 시간 기준은 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f15",
      "claim": "BIM·도면 좌표와 현장 정합에 관해 이 영역에는 요약·연결만 두는 것이 맞다. ROP 지도 인계 기록에는 좌표 변환 메타데이터 검사·실측 정합 검사·주행 가능성 검사 결과를 따로 두고, 도면 판(완공 의도 상태인지)·촬영일·센서 시간 보정 방식과 정합에 쓴 정답 종류를 함께 남겨야 한다. 주 서술 위치는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙이다.",
      "tag": "의견",
      "source_ids": [
        "ref-1669",
        "ref-1670",
        "ref-1676"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10(투영 미처리)·f11·f12(정답 궤적 없음)·f13·f14(완공 의도 평면도, 동기화 설명)에서 도출. 독립 검증 결과의 배치 판단(A04~A06 은 14영역·도면 트랙 stage-2·stage-4 가 주 위치)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "AAS-RAIL 은 미리 정한 목표 속성마다 값 하나를 채우는 고정 슬롯 값 예측으로 평가하며(문법 제약 디코딩), 속성 검출은 평가 범위 밖이라 정밀도·재현율·F1 은 보고하지 않는다. 51.8%→71.7%는 이 조건의 속성 추출 정확도다.",
      "tag": "사실",
      "source_ids": [
        "ref-1071"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 §3.4: \"The task is evaluated as a fixed-slot value prediction problem with a predefined set of target properties\" … \"Precision, recall, and F1-score are not reported because property detection is outside the scope\". 4개 제조사 데이터시트–AAS 200쌍",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "AAS-RAIL 의 56.2%는 여러 번 나오거나 무관한 일치의 모호성을 일부러 무시한 낙관적 정규식 검색으로 정답 속성값이 문서에서 발견된 비율이며, 속성 이름과 값이 함께 문서에 있는 경우는 13.4%뿐이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1071"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 §5 Discussion: \"a regular-expression search that deliberately ignored ambiguities arising from multiple occurrences or unrelated matches. Despite these optimistic assumptions, … only 56.2% … only 13.4% contained both the property name and value\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "기존 위키의 AAS-RAIL 서술(51.8%→71.7%, 원문에서 확인 가능한 속성 56.2%)은 틀린 문장이 아니므로 지우지 말고, '고정 슬롯 평가'와 '모호성을 무시한 낙관적 정규식 기준, 이름·값 동시 13.4%'라는 조건을 붙여야 한다. 원문에 같은 값이 있다는 것과 그 값이 그 속성의 근거라는 것은 따로 검토해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1071"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f16·f17 에서 도출. 대상: 2026-09-30-area45-s8.md 42행, 2026-09-30-area45-s6.md 45행 AAS-RAIL 문장",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "URDF 에서 로봇 온톨로지를 채우는 LLM 파이프라인(gpt-oss:20b, PR2·Pepper·TIAGo 예비 평가)은 Pepper 의 사용자 신호용 ChestButton 을 접촉면 하위 유형의 Bumper 로 분류했고, 저자들은 물리적 성질은 맞았지만 항행 안전 센서와 사람–로봇 상호작용 입력을 구분할 기능 문맥이 없었다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-239"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 §4.3 Pepper: \"mapped the non-standard interaction hardware ChestButton_frame, as a Bumper with a ContactSurface sub-type\"; §4.4: 기능 문맥 부족 설명. ICSR 2026 게재(arXiv 표기). 세 플랫폼 예비 사례라 오류 비율은 산출 불가",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "LangExtract 의 Extraction 자료형은 추출 텍스트를 원문에서 찾지 못하면 원문 문자 구간(char_interval)을 None 으로 둔다. 즉 항목마다 원문 위치가 항상 붙는 것은 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1671"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고정 커밋 74df59f langextract/core/data.py Extraction 설명: \"char_interval: The character interval of the extraction in the original text. None when the extraction text could not be located in the source document.\" 자료형 정의이며 로봇 문서 성능은 미측정",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Docling Core 의 ProvenanceItem(PDF·HTML·docx·pptx 에서 추출한 요소가 원문을 가리키는 근거 항목)은 쪽 번호(page_no)·영역 상자(bbox)·문자 구간(charspan) 세 필드를 모두 필수로 가진다.",
      "tag": "사실",
      "source_ids": [
        "ref-1672"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고정 커밋 0d5a7bd docling_core/types/doc/common/reference.py: class ProvenanceItem — page_no: int, bbox: BoundingBox, charspan: CharSpan(기본값 없음). 설명 \"lightweight pointer back into the original document\". 추출 내용의 의미 정확성은 보장하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "추출값과 근거 위치는 따로 저장하고, char_interval 이 None 이거나 근거 항목(ProvenanceItem) 자체가 없는 추출은 검토 대기로 두어야 한다. Docling 자료형에서는 세 필드가 필수라 '쪽·상자가 빈 근거 항목'은 생기지 않으므로 메모의 그 표현은 맞지 않다. 위치가 있다는 사실만으로 로봇 능력을 실행 가능으로 확정하지도 않는다.",
      "tag": "의견",
      "source_ids": [
        "ref-1671",
        "ref-1672"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f20·f21 에서 도출. 메모 A09 'ROP 시사점' 문구를 검증 결과(F18 필드 필수)대로 정정. oq-147 부분 근거",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "AI Hub 「건축 도면 데이터」(71465)의 건축 개요 데이터 속성표(3-2-4)는 14개 필수 속성 가운데 설계단계(design_stage, 범위 계획·실시)와 축척(scale, 원문 표기 '축적도')을 둔다. 데이터는 1.0판 2023-07-26 개방, 1.1판 2023-12-15 최종 개방이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1012"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 데이터 페이지 3-2-4: \"design_stage | string | y | 설계단계 | 계획, 실시\", \"scale | number | y | 축적도\"(축척의 오기로 보임). 변경 이력: 1.1 2023-12-15, 1.0 2023-07-26, 2025-05-08 구축업체정보 수정. 샘플값 완전성은 검증하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "ONTHEIT 는 KDoc-OCRBench-V2 를 한국 공공부문 단일 쪽 PDF 849개와 검증된 시험 56,197건(문장 존재 6,290·표 셀 49,115·머리말/꼬리말 792, 표가 약 87%)으로 구성하고, 실버 라벨 뒤 수동 검토했다고 설명한다. 문서 유형에 공공 매뉴얼(216개)은 있으나 로봇 매뉴얼은 따로 없다.",
      "tag": "추정",
      "source_ids": [
        "ref-1673"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 고정 커밋 cdfc6d0 kdoc_benchmark_v2/README.md \"56,197 verified test cases across 849 single-page PDFs from Korean public-sector documents\", 파일별 건수, \"silver labelling, and manual review: ONTHEIT\". 제공자 자체 집계·외부 재현 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f25",
      "claim": "Hydra-Multi 는 각 로봇의 장면 그래프 전체를 제어 스테이션으로 주기적으로 전송하고, 로봇 쪽에서 삭제된 노드·엣지는 중앙 그래프에서도 지운다. 변경분만 보내거나 통신 단절 복구를 보장하는 방식의 근거가 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1674"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 III-A: \"the entire scene graph is transmitted periodically from each robot to the control station\", 삭제된 노드·엣지를 프런트엔드 그래프에서도 제거하는 book-keeping 설명. IROS 2023(DOI 10.1109/IROS55552.2023.10341838)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "Hydra-Multi 의 평가는 uHumans2 시뮬레이션, 손에 든 장치로 따로 기록한 두 시퀀스를 서로 다른 두 로봇으로 취급한 SidPac, 실물 Jackal 2대로 기록한 Simmons 데이터로 이뤄진다. 재생 시퀀스 수를 동시에 운용한 로봇 대수로 세면 안 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1674"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 IV-A: SidPac \"two separate recordings as two different robots\", Simmons 는 Intel Realsense D455 를 단 Jackal 로봇 2대, uH2 는 시뮬레이션",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "Strader 외의 종단 간 실물 실험(West Point Camp Buckner 실외)은 이종 로봇 2대(Clearpath Husky, Boston Dynamics Spot)로 했고, 장면 그래프 융합 절제 실험(§5.2)은 Kimera-Multi 데이터셋의 로봇 3대 기록(acl_jackal2, sparkal1, sparkal2)을 썼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1070"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v2 §5.1: \"two heterogeneous robots: a wheeled robot (Clearpath Husky) and a quadruped (Boston Dynamics Spot)\"; §5.2: Kimera-Multi hybrid·outdoor 시퀀스에서 \"acl jackal2, sparkal1, and sparkal2 robots\" 데이터. 그래서 논문 전체를 '2대'로 단정하지 않음",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f28",
      "claim": "이 연구의 재위치 평가는 Husky 와 Spot 이 비슷하게 지난 약 500 m 구간에서 10 m 마다 두 로봇 카메라 간 상대 자세를 추정해, 수동 확인한 루프 폐쇄로 자세 그래프 최적화한 의사 정답과 5 m·10도 이내면 성공으로 보았고, 성공률은 Husky 64%, Spot 65%였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1070"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v2 §5.1: \"within 5 meters and 10 degrees of the pseudo ground truth pose computed via pose graph optimization with manually verified loop closures. The Husky achieved a relocalization success rate of 64%, while the Spot achieved 65%\". 측량 정답이 아니며 도킹 정밀도 판정 아님",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f29",
      "claim": "같은 실험의 자연어 임무 시험은 단일 로봇 8회·다중 로봇 12회로, 실행 성공률은 단일 로봇이 쉬움·중간·어려움 100%·50%·50%, 다중 로봇이 66%·100%·75%였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1070"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v2 표 1: grounding·planning·execution 성공률, \"single-robot (8 trials) and multi-robot (12 trials)\". Execute 열 단일 100/50/50, 다중 66/100/75. 시험 횟수가 적어 비율 비교에 한계",
      "as_of": "2026-10-12",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f30",
      "claim": "MIT-SPARK 의 Spark-DSG 는 Python 예제에서 JSON 장면 그래프 파일을 DynamicSceneGraph.load 로 불러와 객체·장소·방 등 층과 노드에 접근하는 API 를 보여 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-1675"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고정 커밋 3c40997 examples/python_api.py: \"G = dsg.DynamicSceneGraph.load(str(path_to_dsg))\"(uHumans2 예제 그래프). 같은 연구실 구현의 내부 API 이며 다중 제조사 교환 표준이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "Spark-DSG 의 그래프 파일 API 는 교환 어댑터의 출발점으로는 쓸 수 있지만, 다른 제조사 장면 그래프와의 단위·좌표계·객체 식별자·삭제 표시 의미는 별도 계약으로 정해야 하며, Hydra-Multi 의 주기적 전체 전송을 플릿 통신 설계의 근거로 그대로 옮기지 말고 전송량·삭제 전파·초기 좌표 정합을 인수 시험에서 따로 재야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1674",
        "ref-1675"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f25·f26·f30 에서 도출. 메모 A11·A13 'ROP 시사점'. 16. 장소 의미·지도 관리, 18. 실시간 세계 상태·데이터 일관성과 연결 검토",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "Robinson 외의 창고 실험은 통로 6개(각 약 27 m)의 중형 창고 시험 구역에 로봇만 둔 상태에서, 연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4 와 Camera Module 3, PoE 전원, 5 fps)로 했다. 창고가 원래 운영하던 CCTV 를 재사용한 것이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1065"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 §4.1: \"with only robots present in the test area. We instrumented it with 30 custom cameras (Raspberry Pi 4 Model B with Camera Module 3, powered over PoE), each streaming at 5 fps\". 기존 위키 '창고 CCTV 카메라 30대'(본 페이지 5절 표, s8)의 정정 근거",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f33",
      "claim": "전체 시스템 검증(§5.2)에서는 로봇 4대가 30개 카메라 시야 가운데 무작위로 정한 목표 지점으로 이동하고 도착하면 바로 새 목표를 받는 방식으로 45분 동안 1.3 km 를 다니며 지점 간 임무 76건을 마쳤다.",
      "tag": "사실",
      "source_ids": [
        "ref-1065"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 §5.2: \"Each was assigned a random goal position among the 30 camera views\" … \"The system ran for 45 min, over which the fleet traversed 1.3 km\", \"The fleet completed 76 point-to-point missions\". 운반물 처리 성과가 아님",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f34",
      "claim": "이 45분 시험에는 10·17·37·41분에 네 번 사람 개입이 있었다. 앞의 두 번은 최대 곡률 구간 추종 실패에 따른 충돌로 17분 뒤 현장에서 제어 이득을 조정해 해소했고, 뒤의 두 번은 로봇 일시 오분류와 학습이 적은 시각 영역에서의 방향 추정 오류가 자세 갱신 시간 초과로 제어기를 멈춘 인식 문제였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1065"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 §5.2: \"the system needed four interventions, at minutes 10, 17, 37, and 41\" … \"The first two were collisions\" … \"The last two were perception-driven\" … \"triggered a pose-update timeout that halted the controller\". 저자는 시제품 조건이라고 밝힘",
      "as_of": "2026-10-12",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f35",
      "claim": "Brorsson 외의 상용차 공장 배치에서 각 천장 카메라는 장애물 검출용 저해상도(640×360) 영상을 10 Hz, 로봇 위치 추정용 고해상도(3840×2160) 영상을 1 Hz 로 보내고, 로봇은 1 Hz 위치 추정값을 탑재 모터 오도메트리와 융합해 실시간 위치를 얻는다.",
      "tag": "사실",
      "source_ids": [
        "ref-308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 IV-A2 카메라 영상 두 흐름(10 Hz 장애물, 1 Hz 위치)과 IV-B1: \"performed at a low frequency (1 Hz). However, onboard the robot, the low-rate position estimates are fused with motor odometry\". 메모는 [추정]으로 냈으나 원문에 직접 서술된 구성이라 [사실]",
      "as_of": "2026-10-12",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f36",
      "claim": "RGB-only 능동 장면 그래프 연구는 MapAnything 이 모든 카메라 자세를 첫 입력 영상 기준으로 내므로, 첫 영상의 자세(외부 카메라 또는 로봇 초기 시점)만 알면 모든 자세를 일관된 전역 좌표로 나타내기에 충분하다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1069"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 III-B: \"knowing the pose of the first input image (e.g., an external camera or the robot's initial viewpoint) is sufficient to express all poses in a consistent global frame\". 실제 시설 측량 정합 성능은 검증하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "같은 연구의 기하 관계 판정 임계값(수직 간격·바닥 겹침·수평 근접)은 실험 내내 고정하되 데이터셋마다 한 번 경험적으로 맞췄고, 데이터셋에 관계 정답이 없어 정량 평가는 노드에만 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1069"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "v1 III-B: \"All geometric relation thresholds … are fixed across experiments and tuned empirically once per dataset\"; IV: \"Quantitative evaluation is therefore restricted to nodes, since datasets … do not provide ground-truth relational annotations\". Replica·ReplicaCAD 기준",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "고정 카메라와 로봇 관측을 합치는 입력에는 수집 시각·좌표 기준·관측 주기·동기화 방식(하드웨어 동기 여부)·정답 종류를 붙여야 하며, 공장 배치 보고·시뮬레이션 연구·데이터셋 설명의 서로 다른 조건을 합쳐 범용 허용 시간 차를 만들어서는 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-308",
        "ref-1069",
        "ref-1676"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f35(1 Hz 위치+오도메트리), f36·f37(첫 영상 자세, 데이터셋별 임계값), f14(PPS 동기·IMU 정렬)에서 도출. oq-227·oq-035 부분 근거이며 허용 시간 차 수치는 여전히 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "다중 로봇 실증을 인용할 때는 임무 완료 수와 사람 개입 수, 실물 로봇 대수와 데이터셋 재생 대수를 함께 적어야 하며, 재위치 성공률(5 m·10도 기준)을 좁은 통로·도킹의 정밀 위치 보증으로 다시 쓰지 않아야 한다. 외부 카메라 기반 운용은 로봇 외형이 비슷해지거나 학습이 적은 구역이 생길 때 인식 재검증·정지·복구 담당을 정해 두어야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1065",
        "ref-1070"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f27~f29(2대/3대, 64%·65%, 8·12회), f32~f34(45분·76건·개입 4회, 인식 원인 정지)에서 도출. 메모 A12·A14 'ROP 시사점'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1073",
      "org": "Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv)",
      "title": "AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding",
      "published": "2026-01-08",
      "url": "https://arxiv.org/abs/2601.04819",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "도면 이해 멀티모달 벤치마크(기존 출처, arXiv DOI 10.48550/arXiv.2601.04819). 이번에 v1 PDF 6절 한계(p.19–20)에서 래스터 PNG 입력과 개수 세기 4종 외 미평가 객체를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2601.04819v1",
      "source_unopened": false
    },
    {
      "id": "ref-1071",
      "org": "Groß, J., & Heidrich, J. (arXiv)",
      "title": "AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning",
      "published": "2026-09-07",
      "url": "https://arxiv.org/abs/2609.07334",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "데이터시트에서 AAS 속성을 검색 증강 문맥 예시로 추출하는 연구(기존 출처, arXiv DOI 10.48550/arXiv.2609.07334). 이번에 v1 PDF §3.4 고정 슬롯 평가와 §5 의 56.2%·13.4% 산출 조건을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2609.07334v1",
      "source_unopened": false
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "URDF 에서 LLM 으로 로봇 온톨로지를 채우는 예비 연구(기존 출처, arXiv v1 2026-06-10, ICSR 2026 게재 표기). 이번에 PDF §4.3·§4.4 에서 Pepper ChestButton→Bumper 분류 사례를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2606.17073v1",
      "source_unopened": false
    },
    {
      "id": "ref-1012",
      "org": "AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주)",
      "title": "건축 도면 데이터",
      "published": "2023-07-26",
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "주거 3종 건축 도면 48,033장 학습 데이터(기존 출처). 이번에 3-2-4 건축 개요 데이터 속성표(design_stage·scale 필수)와 변경 이력(1.0판 2023-07-26, 1.1판 2023-12-15, 2025-05-08 구축업체정보 수정)을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1070",
      "org": "Strader, J., Ray, A., Arkin, J. 외 (arXiv)",
      "title": "Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs",
      "published": "2025-07-10",
      "url": "https://arxiv.org/abs/2506.07454",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "다중 로봇 3차원 장면 그래프와 LLM 계획의 실외 실증(기존 출처, v1 2025-06-09·v2 2025-07-10, 공동저자 공식 목록 기준 ISER 2025). 이번에 v2 PDF §5.1(Husky·Spot, 재위치 64%·65%, 표 1)과 §5.2(Kimera-Multi 3대)를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2506.07454v2",
      "source_unopened": false
    },
    {
      "id": "ref-1065",
      "org": "Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv)",
      "title": "Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse",
      "published": "2026-06-04",
      "url": "https://arxiv.org/abs/2606.06762",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "보정하지 않은 카메라망과 외부 계산으로 창고 로봇 4대를 계획·제어한 실증(기존 출처). 이번에 v1 PDF §4.1(연구팀 설치 카메라 30대)과 §5.2(45분·76임무·개입 4회)를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2606.06762v1",
      "source_unopened": false
    },
    {
      "id": "ref-308",
      "org": "Brorsson, E. 외",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "천장 카메라 기반 사내 물류 이동 로봇의 상용차 공장 배치 보고(기존 출처, arXiv v1 2025-12-17). 이번에 v1 PDF IV-A2·IV-B1 에서 영상 흐름(10 Hz·1 Hz)과 모터 오도메트리 융합을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2512.15215v1",
      "source_unopened": false
    },
    {
      "id": "ref-1069",
      "org": "Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv)",
      "title": "RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots",
      "published": "2026-05-18",
      "url": "https://arxiv.org/abs/2605.18197",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "RGB 영상만으로 능동 3차원 장면 그래프를 만드는 연구(기존 출처). 이번에 v1 PDF III-B 의 첫 영상 자세 조건과 데이터셋별 임계값 조정, 관계 엣지 정량 평가 제외를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2605.18197v1",
      "source_unopened": false
    },
    {
      "id": "ref-1667",
      "org": "Phung, H., & Averbuch-Elor, H. (Cornell University, arXiv; SIGGRAPH 2026)",
      "title": "Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction",
      "published": "2026-08-07",
      "url": "https://arxiv.org/abs/2602.09016v3",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "평면도 래스터 영상을 방 다각형 시퀀스로 복원하는 모델. arXiv v3(2026-08-07; v1 2026-02-09, v2 2026-05-11), SIGGRAPH 2026 Conference Papers 게재판 DOI 10.1145/3799902.3811124(2026-07-19, Crossref 확인). §4.1 평가 프로토콜과 §4.5 한계를 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2602.09016v3",
      "source_unopened": false
    },
    {
      "id": "ref-1668",
      "org": "Aliyev, N., & Barsi, Á. (Periodica Polytechnica Civil Engineering)",
      "title": "Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images",
      "published": "2026-08-05",
      "url": "https://pp.bme.hu/ci/article/view/44138",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "시각–언어 모델 3종의 평면도 방 면적 추정을 주거 평면도 100장으로 평가한 동료심사 논문. 70(3), pp.891–901, DOI 10.3311/PPci.44138(온라인 2026-08-05, Crossref 확인). 본문 PDF §3.4·§4.1·표 2 와 보충자료를 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1669",
      "org": "buildingSMART (IFC4.3.x-development GitHub)",
      "title": "IFC 4.3 — IfcMapConversion (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 HTML과 문구가 다를 수 있음)",
      "published": null,
      "url": "https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "국지 공학 좌표를 지도 좌표로 옮기는 IFC 엔터티 정의 원본. 공식 HTML(standards.buildingsmart.org, IFC4.3.2.0)은 Cloudflare 차단으로 열지 못해 판·절 번호는 확인하지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md",
      "source_unopened": false
    },
    {
      "id": "ref-1670",
      "org": "Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research)",
      "title": "BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization",
      "published": "2026-06-12",
      "url": "https://arxiv.org/abs/2606.14237v1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "BIM 과 현장 불일치를 고려한 LiDAR 실내 위치 추정. arXiv v1(2026-06-12), IJRR 온라인 게재 DOI 10.1177/02783649261462593(2026-07-06, Crossref 확인). §4.2.1~4.2.3 사무실·공사장 실험을 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2606.14237v1",
      "source_unopened": false
    },
    {
      "id": "ref-1671",
      "org": "Google (google/langextract)",
      "title": "LangExtract — langextract/core/data.py (Extraction 자료형, commit 74df59f)",
      "published": null,
      "url": "https://github.com/google/langextract/blob/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "LangExtract 추출 결과 자료형 정의(고정 커밋). char_interval 이 원문에서 위치를 찾지 못하면 None 이 된다는 설명을 확인했다. README 는 기존 ref-1074.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/google/langextract/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py",
      "source_unopened": false
    },
    {
      "id": "ref-1672",
      "org": "Docling Project (docling-project/docling-core)",
      "title": "docling-core — docling_core/types/doc/common/reference.py (ProvenanceItem, commit 0d5a7bd)",
      "published": null,
      "url": "https://github.com/docling-project/docling-core/blob/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Docling 문서 모델의 근거 위치 자료형 ProvenanceItem 정의(고정 커밋). page_no·bbox·charspan 세 필드가 모두 필수임을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/docling-project/docling-core/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py",
      "source_unopened": false
    },
    {
      "id": "ref-1673",
      "org": "ONTHEIT (ONTHEIT-AI/BizOnAI-OCR)",
      "title": "KDoc-OCRBench-V2 (Korean Document OCR Benchmark v2) — README (commit cdfc6d0)",
      "published": null,
      "url": "https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "국내 업체가 공개한 한국어 공공부문 문서 OCR 벤치마크 설명(고정 커밋). 문서 849개·시험 56,197건 구성과 라벨링 방식은 제공자 자체 설명이다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ONTHEIT-AI/BizOnAI-OCR/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1674",
      "org": "Chang, Y., Hughes, N., Ray, A., & Carlone, L. (MIT SPARK, arXiv; IROS 2023)",
      "title": "Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams",
      "published": "2023-04-26",
      "url": "https://arxiv.org/abs/2304.13487v1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "여러 로봇의 3차원 장면 그래프를 중앙에서 온라인으로 합치는 시스템. arXiv v1(2023-04-26), IROS 2023 pp.10995–11002, DOI 10.1109/IROS55552.2023.10341838(Crossref 확인). III-A 전송 방식과 IV-A 실험 데이터를 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/pdf/2304.13487v1",
      "source_unopened": false
    },
    {
      "id": "ref-1675",
      "org": "MIT-SPARK (MIT-SPARK/Spark-DSG)",
      "title": "Spark-DSG — examples/python_api.py (commit 3c40997)",
      "published": null,
      "url": "https://github.com/MIT-SPARK/Spark-DSG/blob/3c40997e4ae739c56ed3cdd6ef5e882d403d8b64/examples/python_api.py",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "MIT SPARK 연구실의 동적 장면 그래프 라이브러리 Python 예제(고정 커밋). JSON 그래프를 DynamicSceneGraph.load 로 읽어 층·노드에 접근하는 API 를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MIT-SPARK/Spark-DSG/3c40997e4ae739c56ed3cdd6ef5e882d403d8b64/examples/python_api.py",
      "source_unopened": false
    },
    {
      "id": "ref-1676",
      "org": "Hilti Research · Trimble · Oxford DRS (Hilti-Research/hilti-trimble-slam-challenge-2026)",
      "title": "Hilti × Trimble 360 Visual-Inertial SLAM Challenge 2026 — README (commit e0c9277)",
      "published": null,
      "url": "https://github.com/Hilti-Research/hilti-trimble-slam-challenge-2026/blob/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "공사 현장 시계열 SLAM 챌린지 데이터 설명(고정 커밋, 회사 주도 산업 벤치마크). 평면도 설명·2026-09-21 센서 동기화 설명 추가 기록을 확인했다. README 가 인용하는 arXiv 2607.06464(Centanni 외)는 열지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/Hilti-Research/hilti-trimble-slam-challenge-2026/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 실외 표: '수행 자원' 행(116행) '여러 로봇(대수 미확인)' → 실물 종단 간 실험은 Clearpath Husky·Boston Dynamics Spot 2대, 장면 그래프 융합 절제 실험은 Kimera-Multi 데이터셋 로봇 3대 기록(f27, '2대'로 단정하지 않음); '예외·성과' 행(119행) 미확인 → 재위치 성공률 Husky 64%·Spot 65%(5 m·10도, 수동 확인 루프 폐쇄 기반 의사 정답, f28), 임무 시험 단일 8회·다중 12회와 실행 성공률(f29). 물류창고 표: 사례 제목(95행)과 '수행 자원'(101행) '창고 CCTV 카메라 30대' → 연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4·Camera Module 3, PoE, 5 fps)로 정정(f32); '작업 대상'(100행) → 30개 카메라 시야 안 무작위 목표 지점 간 이동 임무(f33); '제약'에 시험 구역에 로봇만 있었음(f32); '예외·성과'(104행) → 45분·1.3 km·지점 간 임무 76건(f33), 개입 4회(충돌 2·인식 2, f34). 의견 f39. 기존 내용 확인: 제조 공장 표 '제약' 행(87행)의 카메라 하드웨어 미동기(ref-308) — 메모 V02 는 넣지 않음. 메모 A05(BIM-Loc 공사장)는 5절 새 사례로 만들지 않고 6절 요약으로 둠 / 섹션 6(분리 2026-09-30-area45-s6) — 속성 추출 소절 45행 AAS-RAIL 문장: 51.8%→71.7% 는 유지하고 고정 슬롯 평가(f16)·56.2% 는 모호성을 무시한 낙관적 정규식 기준이며 이름·값 동시 13.4%(f17) 조건을 붙임, 의견 f18; URDF ChestButton→Bumper 기능 의미 오류(f19); 원문 위치 소절 49행 LangExtract 뒤에 char_interval None(f20)·Docling ProvenanceItem 필수 필드(f21), 의견 f22(메모 시사점 '쪽·상자가 빈 항목' 표현은 검증 결과대로 정정); 도면 인식 소절에 AECV-Bench 입력 PNG·미평가 객체(f1·f2), 의견 f9; BIM 좌표·현장 정합은 요약·연결 수준 2~3문장만: IfcMapConversion 투영 미처리(f10), BIM-Loc 공사장 9개 시퀀스·정답 궤적 없음(f11·f12), Hilti 평면도 완공 의도 상태·동기화 설명(f13·f14 [추정]·벤더 주장), 의견 f15 — 주 서술은 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙(stage-2 q2-09, stage-4 q4-03·q4-15)으로 연결 제안; 융합 소절에 Brorsson 위치 1 Hz+모터 오도메트리·장애물 10 Hz(f35), RGB-only 첫 영상 자세 조건(f36)·임계값 데이터셋별 조정·관계 엣지 미평가(f37), 의견 f38 / 섹션 7(분리 2026-09-30-area45-s7) — 표: LangExtract 행에 위치 못 찾으면 char_interval None(f20), Docling 행에 ProvenanceItem(f21), 새 행 Spark-DSG(f30, 의견 f31), KDoc-OCRBench-V2(f24, 벤더 주장 [추정]), IfcMapConversion(f10, ifc4.3-main 원본 출처, IFC4.3.2.0 판·절 번호는 적지 않음, 요약·연결 수준). AI Hub 문단(49행)에 건축 개요 메타데이터 design_stage(계획·실시)·scale 필수와 1.0/1.1판 날짜(f23; 도면 트랙 q2-04·14영역 쪽 반영 검토). 기존 내용 확인: IDS 사용자 설명의 적용 대상·요구 구성(메모 F09)은 ref-1362, docs/topics/2026/2026-10-11-area21-s7.md 61~65행, 도면 트랙 stage-2 에 있어 넣지 않음 / 섹션 8(분리 2026-09-30-area45-s8) — 새 항목: Phung·Averbuch-Elor, Raster2Seq(SIGGRAPH 2026, f3~f5; 판정 기준은 Stekovic 외 2021 프로토콜), Aliyev·Barsi(Periodica Polytechnica Civil Eng. 70(3), f6~f8; 5.68%·1.58% 는 평가 단위 충돌로 재사용 보류), Chang 외 Hydra-Multi(IROS 2023, f25·f26), Zhang 외 BIM-Loc(IJRR 2026, f11·f12, 한 줄 요약). 기존 항목 보강: AAS-RAIL(42행, f16·f17), Robinson(44행 '카메라 30대' → 연구팀 설치 카메라, 45분·76임무·개입 4회, f32~f34), Strader(46행, 실물 2대·재위치 64%·65%, ISER 2025, f27~f29), Dussard·Sarthou(f19) / 섹션 9 — 148행 '카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인' → 5절 물류창고 사례의 카메라는 연구팀이 설치했고 시설이 원래 운영하던 CCTV 를 재사용한 사례가 아님(f32). 기존 시설 CCTV 재사용의 소유·운영 주체는 여전히 미확인 / 섹션 10(분리 2026-09-30-area45-s10) — 연결 제안: f10~f15 는 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙, f16~f22 는 로봇 매뉴얼 기반 능력 온톨로지 트랙 stage-3(q3-03·q3-05·q3-08), f25·f26·f30·f31 은 16. 장소 의미·지도 관리·18. 실시간 세계 상태·데이터 일관성 / 섹션 11(분리 2026-09-30-area45-s11) — 해결 제안 없음. 부분 근거: oq-147(f20·f21·f22, 로봇 전용 확정·반려 구현은 여전히 없음), oq-196(f1~f8 은 입력·판정·분모 조건만 보여 주며 비주거 시설 측정값은 없음), oq-225(f24 공공문서 OCR, 로봇 매뉴얼 전용 평가는 없음), oq-226(f16·f17·f19), oq-227(f35~f38, 허용 시간 차 수치 없음; oq-035 와 관련), oq-228 은 답하지 않음(53. 개인정보·영상 데이터 연결). oq-197 은 docs/open-questions.md 에서 이미 '해결'(tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-04)이라 부분 답을 쓰지 않고, AI Hub 구조 8종 이름 문제(메모 U02)도 다루지 않음(f23 은 7절 메타데이터로만 씀). 메모의 '새 질문' 4건은 문구 대조로 기존 oq-225~oq-228 과 같아 새로 만들지 않음 / 후속 정리(이번 갱신 범위 밖): Robinson 외 사례를 인용한 다른 영역 페이지에 '창고 CCTV' 표현이 있으면 f32 로 정리 필요(후속 정리 필요). 다음 실행 후보: 14. 도면·BIM에서 지도 만들기(f10~f15), 18. 실시간 세계 상태·데이터 일관성(f25·f35~f38)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "출처 충돌: Aliyev·Barsi(2026)의 픽셀 세기 기준선 MAPE 5.68%·1.58%는 초록(방 개체 단위·도면 단위)과 §4.1·표 2(방 유형별 도면 단위 비교 472쌍)가 평가 단위를 다르게 적는데, 어느 쪽이 맞으며 재현 가능한 출력이 공개됐는가? | 관련 영역: 45. 문서·도면·장면 이해, 14. 도면·BIM에서 지도 만들기 | 근거: f8 | 종류: 출처 충돌",
    "도면 인식 벤치마크의 픽셀 기준 점수(방 IoU 0.5, 모서리 10픽셀·5도)를 실제 문 통과 폭·충전기 접근 가능성 같은 미터 단위 주행 조건으로 검증한 평가나 사례가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 14. 도면·BIM에서 지도 만들기 | 근거: f4 | 종류: 일반",
    "여러 제조사 로봇이 장면 그래프를 공유할 때 주기적 전체 전송 대신 변경분 전송, 통신 단절 뒤 재접속, 삭제 충돌 처리를 시험해 허용 기준을 보고한 사례나 공개 구현이 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 18. 실시간 세계 상태·데이터 일관성 | 근거: f25 | 종류: 일반",
    "시설 카메라망 기반 다중 로봇 제어를 사람이 함께 다니는 구역이나 장시간 운용에서 시험해 시간당 사람 개입 수와 인식 원인 정지를 보고한 사례가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 54. 시험·형식 검증·벤치마크 | 근거: f34 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 18,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-07/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f10: buildingSMART 공식 HTML(IFC4.3.2.0, standards.buildingsmart.org)은 Cloudflare 차단으로 열지 못해 ifc4.3-main 원본으로 확인했다. 게시판 판의 절 번호(메모의 §8.18.3.6.1)와 문구 일치는 미확인",
      "f8: Aliyev·Barsi 의 5.68%·1.58% 평가 단위는 논문 안에서 서술이 충돌해 어느 쪽인지 확정하지 않음(저자 자료 미확인)",
      "f12: BIM-Loc 공사장 시퀀스의 실측 정답 궤적 오차는 저자가 제공하지 않아 미확인. IJRR 게재판 본문은 열지 않고 arXiv v1 로만 확인",
      "f13·f14: Hilti 저장소 README 만 근거(회사 주도 저장소)라 [추정]·벤더 주장. README 가 인용한 arXiv 2607.06464 는 열지 않음",
      "f24: KDoc-OCRBench-V2 구성·라벨링은 제공자 자체 설명이며 외부 재현 없음. 로봇 매뉴얼 대상 한국어 추출 정확도(oq-225)는 여전히 미확인",
      "f19: URDF 기능 의미 오류는 세 플랫폼 예비 사례라 발생률 산출 불가. f16·f17: AAS-RAIL 의 새 제조사 일반화·유의성(신뢰구간) 미보고",
      "f29: 임무 시험 횟수(8·12회)가 적어 성공률 비교에 한계. f27 의 ISER 2025 게재와 Robinson 외(f32~f34)의 학회 게재 여부는 출판사 판으로 확인하지 않음",
      "f34: 개입 4회는 45분, 로봇만 있는 시험 구역 조건이다. 사람 혼재·야간·장기 운용 개입률은 미확인",
      "oq-147(로봇 전용 확정·반려 구현), oq-196(비주거 시설 도면 정밀도·재현율), oq-226(로봇 매뉴얼 추출 벤치마크), oq-227(허용 시간 차·정합 기준 수치), oq-228(국내 CCTV 법령 판단)은 이번 메모로 완전히 답하지 못함",
      "메모가 진단에 쓴 위키 고정 커밋(85960d2)과 배포 페이지의 동일성은 확인하지 않음"
    ],
    "scope_violations": [
      "f10~f15: BIM 좌표 변환·현장 정합은 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙이 주 위치라 이 영역에는 요약·연결 수준으로만 제안함",
      "f11·f12·f27·f28·f35·f36: LiDAR 위치 추정·재위치·로봇 탑재 오도메트리 융합은 로봇 쪽 SLAM·위치 추정(분류 원문 19장의 외부 연계)에 걸치므로 플랫폼이 받는 결과의 조건·평가 기준으로만 씀",
      "f25·f26·f30·f31: 장면 그래프 공유·교환은 16. 장소 의미·지도 관리, 18. 실시간 세계 상태·데이터 일관성과 겹치며 이 영역에는 장면 인식 결과의 표현·교환 조건으로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 10
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1667~ref-1676, 예약 구간 ref-1667~ref-1696 안), 재사용 8건(ref-1073·ref-1071·ref-239·ref-1012·ref-1070·ref-1065·ref-308·ref-1069). 출처 매핑(검증 결과 기준): 메모 n1→ref-1073, n2→ref-1667, n3→ref-1668, n4→ref-1669(공식 HTML 대신 ifc4.3-main 원본, ref-213 과 같은 형식), n5→ref-1670, n6→ref-1071, n7→ref-239, n8→ref-1671(ref-1074 는 README 라 별도), n9→ref-1672, n10→ref-1012, n11→ref-1673(벤더 문서), n12→ref-1674, n13→ref-1070, n14→ref-1675, n15→ref-1065, n16→ref-308, n17→ref-1069, n18(IDS UserManual)→기존 ref-1362 이나 F09 를 중복으로 빼서 sources 에 넣지 않음, n19→ref-1676(벤더 문서). 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 연구 계열: Hydra-Multi·Strader·Spark-DSG 는 MIT SPARK 계열, Robinson·Modi 는 De Martini 공동저자) — 신뢰도 medium 이하. 검증 반영: F09(IDS)·V02(Brorsson 하드웨어 미동기)·U02(AI Hub 구조 8종)는 중복·대상 외로 넣지 않음; oq-197 은 이미 해결이라 부분 답 안 씀; F02 미평가 객체에 구조 부재·내화 구성 추가; F04 를 Stekovic 외 2021 선행 프로토콜 기준으로 정정(f3·f4); F06 재시도 1회·모델명 확인; F08 출처를 공식 HTML 에서 ifc4.3-main 원본으로 바꾸고 판·절 번호 삭제; F11 '공사장' 명시(사무실 벤치마크와 구별); F12·F13 [추정]·벤더 주장; F18 Docling 세 필드 필수를 반영해 메모 시사점 표현 정정(f22); F22 Strader 실물 2대·절제 데이터셋 3대 구분과 재위치 64%·65% 추가(f27·f28), 임무 시험 횟수(f29); A14 '창고 CCTV 카메라 30대'를 연구팀 설치 카메라로 정정하고 작업 대상을 무작위 목표 이동으로(f32·f33); V01 [추정]·벤더 주장 유지; V03 은 원문 IV-B1 직접 서술이라 [사실](f35); 서지 DOI 보완 — Raster2Seq SIGGRAPH 2026 DOI 10.1145/3799902.3811124, BIM-Loc IJRR DOI 10.1177/02783649261462593, Aliyev·Barsi 70(3) pp.891–901 DOI 10.3311/PPci.44138, Hydra-Multi IROS 2023 DOI 10.1109/IROS55552.2023.10341838(모두 Crossref 로 확인, 메모 U16 해소). A04~A06(f10~f15)은 45 에는 요약·연결 수준으로 제안하고 주 위치는 14영역·도면 트랙으로 둠. 열린 질문: 해결 제안 없음, 부분 근거 oq-147·oq-196·oq-225·oq-226·oq-227. 메모의 '새 질문' 4건은 기존 oq-225~oq-228 과 같아 새로 만들지 않음. 메모 U01~U17 가운데 U01→oq-196, U03→oq-225·oq-226, U04→oq-147, U12→oq-227(oq-035 관련), U15→oq-228 로 기존 질문에 붙이고, U02 는 폐기, U16 은 Crossref 확인으로 해소, U06·U05·U11·U13 만 새 질문 4건으로 올림(나머지 U07~U10·U14·U17 은 unverified 에 남김). 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-12-07/verification.json

```json
{
  "run_id": "2026-10-12-07",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). arXiv 초록 페이지에서 기관·제목·v1 2026-01-08, 평면도 120장·QA 192쌍을 확인했다. 검증자가 연 PDF·HTML(404)·alphaxiv 는 본문을 파싱하지 못해 6절 한계 문구(래스터 PNG, DWG·RVT·IFC 미사용)는 다시 확인하지 못했다. alphaxiv 요약의 '픽셀을 넘어 벡터 정보를 직접 받아들이자'는 권고와는 부합한다. 한계 절 인용은 리서치 열람에 기대므로 high 불가"
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 개수 세기 대상 4종(문·창·침실·화장실)은 초록에서 확인했다. 미평가 객체 다섯 종 목록(한계 절 p.20)은 검증자 재열람 실패로 리서치 열람에 기댄다. 단일 출처"
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v3(2026-08-07, SIGGRAPH Conference Papers '26 표기) §4.1 에서 Stekovic 외 2021 프로토콜, 최대 IoU 짝짓기, IoU>0.5, 256×256 입력을 확인했다"
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §4.1 의 모서리 판정(10픽셀 이내, 각도 차 5도 미만)이 선행 프로토콜을 따른 것임을 확인했다"
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §4.5·그림 8 캡션의 '가끔 문·창 위치 오류', '방 안에 문·창 생성'을 확인했다. 발생률 미보고도 확인"
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 학술지 페이지(70(3) pp.891–901, DOI 10.3311/PPci.44138, 온라인 2026-08-05)와 본문 PDF §3.4 에서 1회 재시도, BakLLaVA 의 100장 전부 자리표시자 출력과 제외, LLaVA-LLaMA 3·MiniCPM-V 2.6 을 확인했다. 보충자료의 llama3.2-vision 표기는 검증자가 열지 않았다"
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 같은 유형 방을 비교점 하나로 합친다는 서술과 방 894개→비교 472쌍을 본문과 초록에서 확인했다. 주거 도면만 대상"
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 초록은 5.68% 를 방 개체 단위, 1.58% 를 도면 단위로 적고, §4.1·표 2 는 5.68±7.21% 를 472개 도면 단위 방 유형 비교의 값으로 적는다. 같은 논문 안의 서술 충돌이므로 한쪽을 고르지 않고 둘 다 제시해야 한다(열린 질문 신규 1번)"
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 근거 f1~f8 이 살아 있다. 구축자(리서치) 의견임을 밝혀야 한다"
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ifc4.3-main 원본(raw)에서 공통 축척 하나, z축 반시계 회전, Eastings·Northings·OrthogonalHeight 이동, 투영 미처리 NOTE 를 확인했다. 게시판 IFC4.3.2.0 판과의 문구 일치는 미확인(개발 브랜치)"
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 에서 CityU 공사 현장 9개 시퀀스, 누적 3.5 km 초과를 확인했다. 다만 원문은 Ouster OS0-128 손에 든 센서로 기록한 시퀀스 7개(06~12층), Livox Mid-360 으로 기록한 시퀀스 2개(06·08층)라고 적는다. 브리프 문구 'Ouster 7개·Livox 2개'는 센서 대수로 읽힐 수 있으므로 시퀀스 수로 고쳐야 한다"
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 공사장 정답 궤적이 없어 MME·scan-to-BIM·Wasserstein 으로 평가하고, 사무실(HKUST, 9개 시퀀스)은 ATE 로 평가함을 확인했다. IJRR 게재판은 열지 않았다"
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 고정 커밋 README 에서 평면도는 공사 종료 시점의 의도 상태이고 이른 기록에는 일부 요소가 없다는 서술, 주최(Hilti·Trimble·Oxford DRS)를 확인했다. 회사 주도 저장소이므로 [추정]·벤더 주장 유지"
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. News 2026-09-21 항목과 동기화 절(정답 LiDAR·IMU 는 PPS 하드웨어 동기, Insta360 은 두 IMU 자이로 크기 맞춤으로 시간 오프셋·시계 배율 추정)을 확인했다. 효과 수치 없음. [추정]·벤더 주장 유지"
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 근거 f10~f14 가 살아 있다. 구축자 의견임을 밝히고, 주 서술 위치는 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙으로 연결만 한다"
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 §3.4 에서 고정 슬롯 값 예측과 P·R·F1 미보고를 확인했다. 51.8%→71.7% 는 표 2 Overall 행이고, §3.3 은 4개 회사의 데이터시트–AAS 200쌍이다"
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §5 에서 모호성을 일부러 무시한 정규식 검색, 56.2%, 이름·값 동시 13.4% 를 확인했다"
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(f16·f17 근거). 기존 문장을 지우지 않고 조건을 덧붙이는 처리. 구축자 의견임을 밝힌다"
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 §4·§4.3·§4.4 에서 gpt-oss:20b, PR2·Pepper·TIAGo, ChestButton_frame→ContactSurface 하위 유형 Bumper, 기능 문맥 부족 설명을 확인했다. 'ICSR 2026 게재'는 열람 본문에 표기가 없어 확인하지 못했다"
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 고정 커밋 74df59f data.py Extraction docstring 의 char_interval None 설명을 확인했다"
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 고정 커밋 0d5a7bd reference.py 에서 ProvenanceItem 의 page_no·bbox·charspan 이 기본값 없는 필수 필드임과 docstring(PDF·HTML·docx·pptx, lightweight pointer)을 확인했다"
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(f20·f21 근거). '메모의 표현이 맞지 않다'는 내부 정정 문구는 페이지에 싣지 않는다"
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. AI Hub 데이터 페이지 3-2-4 에서 14개 속성 모두 필수, design_stage(계획·실시), scale(원문 표기 '축적도')를 확인했다. 변경이력은 1.0 2023-07-26(Beta)과 1.1 2023-12-15(최종 개방)이다. 2025-05-08 구축업체정보 수정은 변경이력 표가 아니라 '데이터 히스토리' 표에 있다. '축척의 오기'는 판단이므로 사실로 쓰지 않는다"
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 고정 커밋 README 에서 849개 단일 쪽 PDF, 56,197건(6,290·49,115·792), 실버 라벨·수동 검토, 범주 통계 283·보고서 238·매뉴얼 216·공지 112 를 확인했다. 로봇 관련 언급은 없다. 제공자 자체 설명이므로 [추정]·벤더 주장 유지"
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 III-A 에서 주기적 전체 장면 그래프 전송과 삭제 노드·엣지 정리를 확인했다. IROS 2023 DOI 는 검증자가 Crossref 로 다시 보지 않았다"
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IV-A 에서 uH2 시뮬레이션, SidPac 은 손에 든 장치로 따로 기록한 두 시퀀스를 두 로봇으로 취급, Simmons 는 D455 를 단 Jackal 2대임을 확인했다"
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v2 §5.1(Camp Buckner, Husky·Spot)과 §5.2(Kimera-Multi hybrid·outdoor, acl_jackal2·sparkal1·sparkal2)를 확인했다. ISER 2025 게재는 확인하지 못했다"
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 약 500 m, 10 m 간격, 5 m·10도, 수동 확인 루프 폐쇄 기반 의사 정답, Husky 64%·Spot 65% 를 확인했다"
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 표 1 의 단일 8회·다중 12회, 실행 성공률 단일 100/50/50·다중 66/100/75 를 확인했다. 시험 횟수가 적다는 한계를 함께 적는다"
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 고정 커밋 3c40997 examples/python_api.py 의 DynamicSceneGraph.load 와 층·노드 접근(uhumans2_office…json)을 확인했다. 파일 형식은 경로 확장자로 본 것이다"
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(f25·f26·f30 근거). 구축자 의견임을 밝힌다"
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 §4.1 에서 로봇만 있는 시험 구역, 연구팀 설치 맞춤 카메라 30대(RPi 4·Camera Module 3, PoE, 5 fps), 약 27 m 통로 6개를 확인했다. 기존 5절 '창고 CCTV 카메라 30대'의 정정 근거로 유효하다"
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §5.2 에서 로봇 4대, 30개 카메라 시야 가운데 무작위 목표, 45분, 1.3 km, 지점 간 임무 76건을 확인했다"
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 10·17·37·41분 개입 4회, 앞 두 번은 최대 곡률 구간 추종 실패 충돌로 두 번째(17분) 뒤 제어 이득을 현장에서 조정해 해소, 뒤 두 번은 인식 원인(37분 일시 오분류, 41분 학습이 적은 영역의 불규칙한 방향 추정)으로 자세 갱신 시간 초과가 제어기를 멈췄음을 확인했다"
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 IV-A2(640×360 10 Hz 장애물, 3840×2160 1 Hz 위치)와 IV-B1(1 Hz 위치 추정과 모터 오도메트리 융합)을 확인했다. 현장은 Volvo 상용차 제조 현장이다"
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv HTML v1 III-B 에서 첫 입력 영상 기준 자세와 '첫 영상 자세만 알면 충분' 서술을 확인했다"
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 데이터셋마다 한 번 경험적으로 맞춘 고정 임계값, 관계 정답이 없어 노드만 정량 평가함을 확인했다"
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(f14·f35·f36·f37 근거). 허용 시간 차 수치는 없다는 점을 유지한다"
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(f27~f29·f32~f34 근거). 구축자 의견임을 밝힌다"
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
      "f32~f34 는 대상 페이지 5절 물류창고 사례와 9절의 기존 ref-1065 서술('창고 CCTV 카메라 30대', '카메라망 소유·운영 주체 미확인')을 정정·보강한다. 새 각주 없이 ref-1065 를 재사용한다",
      "f27~f29 는 5절 실외 사례의 ref-1070 서술('대수 미확인', '실험 수치가 초록에 없음')을 보강한다. ref-1070 재사용",
      "f16·f17 은 분리 주제 페이지 s6·s8 의 AAS-RAIL(ref-1071) 서술에 조건을 덧붙인다. ref-1071 재사용",
      "f35 는 5절 제조 공장 사례(ref-308)와 같은 출처다. 기존 '카메라 간 하드웨어 동기화 없음' 문장과 충돌하지 않는다",
      "f10~f15 는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙의 주 서술 범위와 겹친다. 이 영역에는 요약·연결만 둔다",
      "f23 은 oq-197(해결, 도면 트랙 q2-04)과 같은 데이터셋이다. 해결된 질문은 건드리지 않는다",
      "ref-1669(IfcMapConversion 원본)는 같은 저장소의 다른 IFC 출처(브리프가 언급한 ref-213 등)와 URL 이 다르다. 같은 URL 이 있으면 퍼블리셔가 합친다"
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
    "f11: 'Ouster OS0-128 7개·Livox Mid-360 2개'를 'Ouster OS0-128 손에 든 센서로 기록한 시퀀스 7개(06~12층)와 Livox Mid-360 으로 기록한 시퀀스 2개(06·08층), 모두 9개 시퀀스(누적 3.5 km 초과)'로 고쳐 쓴다 — 원문 §4.2.1 의 7·2 는 센서 대수가 아니라 시퀀스 수다.",
    "f19: 'ICSR 2026 게재'를 사실로 쓰지 않는다. 서지는 arXiv 2606.17073(2026-06-10)로만 적거나 게재처를 '미확인'으로 둔다 — 열람한 본문에서 게재처 표기를 확인하지 못했다.",
    "f27: 'ISER 2025 게재'를 사실로 쓰지 않고 arXiv v2(2025-07-10)로 적는다. 게재처를 밝히려면 '미확인'을 병기한다 — 브리프도 출판사 판으로 확인하지 않았다고 적었다.",
    "f13·f14·f24: 본문에서 [추정]을 유지하고 '벤더 주장'을 병기한다 — 출처 ref-1676·ref-1673 이 회사가 관리하는 저장소의 자체 설명이고 독립 확인이 없다.",
    "f8: Aliyev·Barsi 의 5.68%·1.58% 를 성능 근거로 쓰지 않는다. 8절에는 초록(방 개체 단위·도면 단위)과 §4.1·표 2(472개 도면 단위 방 유형 비교)의 평가 단위 서술이 서로 다르다는 사실만 두 서술을 모두 제시해 적고, 신규 열린 질문(출처 충돌)으로 올린다 — 같은 논문 안의 서술 충돌이며 한쪽을 고르지 않는다.",
    "f9·f15·f18·f22·f31·f38·f39: 본문에서 [의견]으로 두고 '구축자 의견'임과 근거 finding 의 출처 각주를 함께 밝힌다. 내부 작업 문구('메모 시사점', '메모의 표현을 정정' 등)는 페이지에 싣지 않는다 — 의견의 주체를 밝혀야 하고, 외부 조사 메모는 출처가 아니다.",
    "f10~f15: 6절(분리 주제 페이지 s6)에는 BIM 좌표·현장 정합 요약을 2~3문장만 두고, 10절에서 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙으로 연결한다. BIM-Loc 의 LiDAR 위치 추정(f11·f12)과 Strader 외의 재위치(f28)는 '연계 대상: 로봇 자체 위치 추정'으로 표시하고, ROP 는 그 결과의 조건·평가 기준만 받는다고 쓴다 — 분류 원문 19장 경계상 SLAM·위치 추정은 외부 연계 영역이다.",
    "5절 물류창고 사례(f32~f34): 사례 제목과 '수행 자원' 칸의 '창고 CCTV 카메라 30대'를 '연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4·Camera Module 3, PoE, 5 fps)'로 고친다. '작업 대상' 칸은 30개 카메라 시야 안 무작위 목표 지점 간 이동 임무로 채우고 '운반물 처리 아님'을 밝힌다. '제약' 칸에 시험 구역에 로봇만 있었다는 조건을 더한다. '예외·성과' 칸은 45분·1.3 km·임무 76건과 개입 4회(충돌 2·인식 원인 2)로 채운다. 각주 ref-1065 의 논문 제목('…CCTV Camera Networks…')은 그대로 둔다 — 원문 §4.1·§5.2 와 일치시키되 서지 제목은 바꾸지 않는다.",
    "9절: '카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인이다'를 '5절 물류창고 사례의 카메라는 연구팀이 설치했고 시설이 원래 운영하던 CCTV 를 재사용한 사례가 아니다 [사실][^ref-1065]. 기존 시설 CCTV 를 재사용할 때의 소유·운영 주체는 미확인이다'라는 취지로 바꾼다 — f32 근거. 미확인 부분은 남긴다.",
    "5절 실외 사례(f27~f29): '수행 자원' 칸에 실물 종단 간 실험은 Husky·Spot 2대이고 장면 그래프 융합 절제 실험은 Kimera-Multi 데이터셋 로봇 3대 기록임을 함께 적는다('2대'로 단정하지 않는다). '예외·성과' 칸에는 재위치 성공률 64%·65%(5 m·10도, 의사 정답 기준)와 임무 시험 단일 8회·다중 12회의 실행 성공률을 적고 시험 횟수가 적다는 한계를 병기한다. site_matrix_updates 는 실외 사례의 실제로 채운 칸만 낸다.",
    "f16·f17: 51.8%→71.7% 문장은 지우지 않고 '고정 슬롯 값 예측 조건(속성 검출 미평가)'을 덧붙인다. 56.2% 에는 '모호성을 무시한 낙관적 정규식 기준'과 '이름·값이 함께 있는 경우 13.4%'를 덧붙인다 — 원문 §3.4·§5 의 산출 조건이다.",
    "f23: AI Hub 문단에는 설계단계(계획·실시)와 축척이 필수 속성이라는 점, 1.0판 2023-07-26·1.1판 2023-12-15 를 적는다. 'scale 의 원문 표기 축적도는 축척의 오기'라는 판단은 쓰지 않거나 [추정]으로만 쓴다. 각주 ref-1012 의 발행일 '미확인'을 참고문헌 목록과 같은 2023-07-26 으로 맞춘다 — 데이터 페이지 변경이력과 docs/references/index.md 가 일치한다.",
    "각주: 새 출처 ref-1667~ref-1676 의 각주 정의를 공통 형식으로 추가한다. 발행일이 없는 ref-1669·ref-1671·ref-1672·ref-1673·ref-1675·ref-1676 은 발행일 자리에 '미확인'을 쓰고, ref-1669 제목에는 개발 브랜치 원본이라는 표기를 유지한다. 기존 출처(ref-1073·ref-1071·ref-239·ref-1012·ref-1070·ref-1065·ref-308·ref-1069)는 기존 id 를 재사용하고 접근일을 2026-10-12 로 갱신한다. 프런트매터 sources 를 각주와 맞춘다.",
    "인용: 페이지의 직접 인용은 출처당 1회, 짧은 구절로 제한하고 나머지는 요약·재서술한다. 특히 ref-1065·ref-1070·ref-1071 처럼 브리프 발췌에 여러 구절이 있는 출처를 주의한다 — 공통 규칙 5.3.",
    "열린 질문(11절): oq-147·oq-196·oq-225·oq-226·oq-227 에는 부분 근거만 연결하고 상태를 바꾸지 않는다. oq-197(해결)과 oq-228 은 건드리지 않는다. 신규 질문 4건은 브리프 문구 그대로 등록한다 — 해결 제안이 없고, 해결로 인정할 finding 이 없다.",
    "트랙 반영 제안 3건(실행 2026-10-09-21·23·26, 8. 대표 연구와 자료 대상)은 이번 브리프에 근거 finding·출처가 없으므로 8절에 반영하지 않는다. 상태는 '제안'으로 두고 다음 해당 영역 실행으로 넘긴다 — 검증을 거치지 않은 브리프 밖 내용은 드리프트가 된다.",
    "약어·전문용어: IoU(Intersection over Union, 교집합 대 합집합 비), MAPE(평균 절대 백분율 오차), ATE(절대 궤적 오차), PPS(초당 펄스 신호), IMU(관성 측정 장치), OCR(광학 문자 인식)을 첫 등장 때 풀어 쓴다 — 공통 표기 규약."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 39건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: 없음. 다만 검증자는 ref-1073(AECV-Bench) PDF 를 파싱하지 못해 한계 절(f1·f2)을 다시 읽지 못했고, 초록에서 4종 개수 세기·평면도 120장·QA 192쌍만 확인했다. ref-1669 는 공식 HTML 대신 개발 브랜치 원본으로 확인했다. 주의: 모든 [사실] 주장이 단일 출처이거나 같은 연구 계열이다(Hydra-Multi·Strader·Spark-DSG 는 MIT SPARK, Robinson·Modi 는 공동저자 공유). 그래서 신뢰도는 medium 이다. 수치는 각 논문의 실험 조건에 묶여 있다(256×256 픽셀 허용 오차, 주거 도면 100장, 로봇만 있는 45분 시험, 5 m·10도 재위치, 8·12회 임무 시험). Aliyev·Barsi 의 5.68%·1.58% 는 논문 안에서 평가 단위 서술이 충돌하므로 성능 근거로 쓰지 않는다. Ouster·Livox 7·2 는 시퀀스 수다. ICSR 2026·ISER 2025 게재처는 확인하지 못했다. 브리프는 외부 조사 메모를 변환한 것이라 검색 횟수 집계가 없다(queries 0). 리서치는 메모의 새 질문 4건을 기존 질문과 같다고 적으면서도 신규 질문 4건을 올렸다. 검증자가 대조한 결과 4건은 기존 oq-225~oq-228 과 겹치지 않는다. 분리 주제 페이지(s6·s7·s8·s10·s11) 본문은 입력에 없어, 중복 검사는 브리프가 밝힌 위치 진술에 기댔다. 트랙 반영 제안 3건은 이번 브리프에 근거가 없어 반영하지 않고 다음 실행으로 넘긴다. 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-10-12-07/pages.json

```json
{
  "run_id": "2026-10-12-07",
  "outline": [
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 350,
      "summary": "변경 없음. 해석 오류가 등록 정보·지도·세계 상태 오류로 이어진다는 기존 [추정] 요약과 분리 주제 페이지 링크를 유지한다."
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 120,
      "summary": "변경 없음. 기존 요약 문장과 분리 주제 페이지 링크를 유지한다."
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2600,
      "summary": "물류창고 사례의 카메라 30대는 연구팀이 설치한 맞춤 카메라이며 45분·임무 76건·사람 개입 4회가 보고됐다 [사실][^ref-1065]. 실외 사례는 실물 2대·데이터셋 3대, 재위치 64%·65%, 임무 시험 8·12회를 적는다 [사실][^ref-1070].",
      "planned_findings": [
        "f27",
        "f28",
        "f29",
        "f32",
        "f33",
        "f34",
        "f39"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2600,
      "summary": "문서·도면·장면 접근법의 점수는 입력 형식·평가 범위·산출 조건에 묶여 있다 [사실][^ref-1073][^ref-1071]. 원문 위치 자료형도 위치가 빈 추출을 낼 수 있다 [사실][^ref-1671].",
      "planned_findings": [
        "f1",
        "f2",
        "f9",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f35",
        "f36",
        "f37",
        "f38"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1300,
      "summary": "근거 위치 자료형(LangExtract·Docling), 장면 그래프 파일 API(Spark-DSG), 한국어 OCR 벤치마크(벤더 주장), IfcMapConversion을 표에 더한다 [사실][^ref-1672][^ref-1675].",
      "planned_findings": [
        "f10",
        "f20",
        "f21",
        "f23",
        "f24",
        "f30",
        "f31"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 2000,
      "summary": "Raster2Seq·Aliyev·Barsi·Hydra-Multi·BIM-Loc을 더하고 AAS-RAIL·Robinson·Strader·Dussard·Sarthou 항목의 조건을 적는다 [사실][^ref-1667][^ref-1668].",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f11",
        "f12",
        "f16",
        "f17",
        "f19",
        "f25",
        "f26",
        "f27",
        "f28",
        "f32",
        "f33",
        "f34"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1300,
      "summary": "물류창고 사례의 카메라는 연구팀이 설치했고 시설 CCTV 재사용이 아니다 [사실][^ref-1065]. 로봇 자체 위치 추정은 연계 대상이며 ROP는 결과의 조건만 받는다 [의견][^ref-1670][^ref-1070].",
      "planned_findings": [
        "f32",
        "f12",
        "f28"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "BIM 좌표·정합은 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙, 추출 조건은 매뉴얼 기반 로봇 기능 온톨로지 트랙, 장면 그래프·융합은 16·18 영역으로 연결한다.",
      "planned_findings": [
        "f15"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "section": "11. 열린 질문",
      "budget_chars": 1400,
      "summary": "oq-147·oq-196·oq-225·oq-226·oq-227에 부분 근거를 붙이고 새 질문 4건(출처 충돌 1건 포함)을 올린다.",
      "planned_findings": [
        "f8",
        "f4",
        "f25",
        "f34"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 5절 물류창고 사례(연구팀 설치 카메라 30대·임무 76건·개입 4회)·실외 사례(실물 2대·데이터셋 3대·재위치 64%·65%·임무 시험) 보강, 6~8·10·11절에 2026-10-12 갱신 소절(평가 조건·근거 위치·BIM 정합 요약·새 연구 4건·연결·부분 근거·새 질문 4건), 9절 카메라 주체 문장 정정, 13절 각주 신규 10건·접근일 갱신",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-308",
              "ref-1065",
              "ref-063",
              "ref-1012",
              "ref-1066",
              "ref-239",
              "ref-1067",
              "ref-513",
              "ref-1068",
              "ref-1069",
              "ref-1070",
              "ref-067",
              "ref-1071",
              "ref-1072",
              "ref-1073",
              "ref-1074",
              "ref-1667",
              "ref-1668",
              "ref-1669",
              "ref-1670",
              "ref-1671",
              "ref-1672",
              "ref-1673",
              "ref-1674",
              "ref-1675",
              "ref-1676"
            ],
            "last_run": "2026-10-12"
          },
          "content": "(절 본문 생략 — runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area45-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"6. 대표 접근법과 기술\" 절(2,996자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area45-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"8. 대표 연구와 자료\" 절(2,545자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area45-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"11. 열린 질문\" 절(1,701자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area45-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,522자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area45-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 45. 문서·도면·장면 이해 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,054자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-12 | 45. 문서·도면·장면 이해 | 차등 갱신: 5절 물류창고 사례의 카메라 설치 주체 정정(연구팀 설치 카메라 30대, 45분·임무 76건·개입 4회)과 실외 사례 로봇 대수·재위치·임무 성공률 보강, 6~8절에 도면 인식 점수 조건·AAS-RAIL 산출 조건·근거 위치 자료형·BIM 정합 요약·새 연구 4건, 9절 카메라 주체 문장 정정, 10절 연결 추가, 11절 부분 근거와 새 질문 4건, 각주 신규 10건 | run 2026-10-12-07",
  "index_updates": {
    "home_recent": "2026-10-12 — 45. 문서·도면·장면 이해: 창고 카메라망 실증의 카메라 설치 주체를 정정하고, 도면 인식·데이터시트 추출 점수의 평가 조건과 근거 위치 자료형, 다중 로봇 장면 그래프 실증의 로봇 대수·성공률을 보강했다",
    "category_recent": "2026-10-12 — 45. 문서·도면·장면 이해: 5절 물류창고·실외 사례 보강, 6~8절 평가 조건·근거 위치·BIM 정합 요약·새 연구 4건(Raster2Seq, Aliyev·Barsi, Hydra-Multi, BIM-Loc), 9절 카메라 주체 정정, 새 열린 질문 4건",
    "area_recent": "2026-10-12 — 45. 문서·도면·장면 이해: 차등 갱신(5·9절 정정, 6·7·8·10·11절에 2026-10-12 갱신 소절, 각주 신규 10건)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1073",
      "org": "Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv)",
      "title": "AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding",
      "published": "2026-01-08",
      "url": "https://arxiv.org/abs/2601.04819",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "도면 이해 멀티모달 벤치마크. v1 PDF 6절 한계에서 래스터 PNG 입력과 개수 세기 4종 외 미평가 객체를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1071",
      "org": "Groß, J., & Heidrich, J. (arXiv)",
      "title": "AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning",
      "published": "2026-09-07",
      "url": "https://arxiv.org/abs/2609.07334",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "데이터시트에서 AAS 속성을 검색 증강 문맥 예시로 추출하는 연구. §3.4 고정 슬롯 평가와 §5 의 56.2%·13.4% 산출 조건을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "URDF 에서 LLM 으로 로봇 온톨로지를 채우는 예비 연구(arXiv v1 2026-06-10, 게재처 미확인). §4.3·§4.4 에서 Pepper ChestButton→Bumper 분류 사례를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1012",
      "org": "AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주)",
      "title": "건축 도면 데이터",
      "published": "2023-07-26",
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "주거 3종 건축 도면 학습 데이터. 건축 개요 데이터 속성표(14개 필수 속성, design_stage·scale 포함)와 변경 이력(1.0판 2023-07-26, 1.1판 2023-12-15 최종 개방)을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1070",
      "org": "Strader, J., Ray, A., Arkin, J. 외 (arXiv)",
      "title": "Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs",
      "published": "2025-07-10",
      "url": "https://arxiv.org/abs/2506.07454",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "다중 로봇 3차원 장면 그래프와 LLM 계획의 실외 실증(arXiv v2, 게재처 미확인). §5.1(Husky·Spot, 재위치 64%·65%, 표 1)과 §5.2(Kimera-Multi 3대)를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1065",
      "org": "Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv)",
      "title": "Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse",
      "published": "2026-06-04",
      "url": "https://arxiv.org/abs/2606.06762",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "보정하지 않은 카메라망과 외부 계산으로 창고 로봇 4대를 계획·제어한 실증. §4.1(연구팀 설치 카메라 30대)과 §5.2(45분·76임무·개입 4회)를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-308",
      "org": "Brorsson, E. 외",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "천장 카메라 기반 사내 물류 이동 로봇의 상용차 공장 배치 보고. IV-A2·IV-B1 에서 영상 흐름(10 Hz·1 Hz)과 모터 오도메트리 융합을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1069",
      "org": "Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv)",
      "title": "RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots",
      "published": "2026-05-18",
      "url": "https://arxiv.org/abs/2605.18197",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "RGB 영상만으로 능동 3차원 장면 그래프를 만드는 연구. III-B 의 첫 영상 자세 조건과 데이터셋별 임계값 조정, 관계 엣지 정량 평가 제외를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1667",
      "org": "Phung, H., & Averbuch-Elor, H. (Cornell University, arXiv; SIGGRAPH 2026)",
      "title": "Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction",
      "published": "2026-08-07",
      "url": "https://arxiv.org/abs/2602.09016v3",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "평면도 래스터 영상을 방 다각형 시퀀스로 복원하는 모델(arXiv v3, SIGGRAPH 2026). §4.1 평가 프로토콜(Stekovic 외 2021, IoU 0.5, 10픽셀·5도, 256×256)과 §4.5 한계를 열람했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1668",
      "org": "Aliyev, N., & Barsi, Á. (Periodica Polytechnica Civil Engineering)",
      "title": "Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images",
      "published": "2026-08-05",
      "url": "https://pp.bme.hu/ci/article/view/44138",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "시각–언어 모델 3종의 평면도 방 면적 추정을 주거 평면도 100장으로 평가한 동료심사 논문(70(3), pp.891–901). 초록과 §4.1·표 2 의 MAPE 평가 단위 서술이 서로 다르다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1669",
      "org": "buildingSMART (IFC4.3.x-development GitHub)",
      "title": "IFC 4.3 — IfcMapConversion (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 HTML과 문구가 다를 수 있음)",
      "published": null,
      "url": "https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "국지 공학 좌표를 지도 좌표로 옮기는 IFC 엔터티 정의 원본. 투영 미처리 NOTE 를 확인했고, 게시판 IFC4.3.2.0 판의 절 번호는 확인하지 않았다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1670",
      "org": "Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research)",
      "title": "BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization",
      "published": "2026-06-12",
      "url": "https://arxiv.org/abs/2606.14237v1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "BIM 과 현장 불일치를 고려한 LiDAR 실내 위치 추정. 공사장 9개 시퀀스(Ouster 7·Livox 2)와 정답 궤적 없는 대리 지표 평가를 arXiv v1 에서 확인했다. IJRR 게재판 본문은 열지 않았다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1671",
      "org": "Google (google/langextract)",
      "title": "LangExtract — langextract/core/data.py (Extraction 자료형, commit 74df59f)",
      "published": null,
      "url": "https://github.com/google/langextract/blob/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "LangExtract 추출 결과 자료형 정의(고정 커밋). 원문에서 위치를 찾지 못하면 char_interval 이 None 이 된다는 설명을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1672",
      "org": "Docling Project (docling-project/docling-core)",
      "title": "docling-core — docling_core/types/doc/common/reference.py (ProvenanceItem, commit 0d5a7bd)",
      "published": null,
      "url": "https://github.com/docling-project/docling-core/blob/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Docling 문서 모델의 근거 위치 자료형 ProvenanceItem 정의(고정 커밋). page_no·bbox·charspan 세 필드가 모두 필수임을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1673",
      "org": "ONTHEIT (ONTHEIT-AI/BizOnAI-OCR)",
      "title": "KDoc-OCRBench-V2 (Korean Document OCR Benchmark v2) — README (commit cdfc6d0)",
      "published": null,
      "url": "https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "국내 업체가 공개한 한국어 공공부문 문서 OCR 벤치마크 설명(고정 커밋). 문서 849개·시험 56,197건 구성과 라벨링 방식은 제공자 자체 설명이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1674",
      "org": "Chang, Y., Hughes, N., Ray, A., & Carlone, L. (MIT SPARK, arXiv; IROS 2023)",
      "title": "Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams",
      "published": "2023-04-26",
      "url": "https://arxiv.org/abs/2304.13487v1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "여러 로봇의 3차원 장면 그래프를 중앙에서 온라인으로 합치는 시스템. III-A 주기적 전체 전송·삭제 정리와 IV-A 실험 데이터(uHumans2·SidPac·Simmons)를 열람했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1675",
      "org": "MIT-SPARK (MIT-SPARK/Spark-DSG)",
      "title": "Spark-DSG — examples/python_api.py (commit 3c40997)",
      "published": null,
      "url": "https://github.com/MIT-SPARK/Spark-DSG/blob/3c40997e4ae739c56ed3cdd6ef5e882d403d8b64/examples/python_api.py",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "MIT SPARK 연구실의 동적 장면 그래프 라이브러리 Python 예제(고정 커밋). JSON 그래프를 DynamicSceneGraph.load 로 읽어 층·노드에 접근하는 API 를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    },
    {
      "id": "ref-1676",
      "org": "Hilti Research · Trimble · Oxford DRS (Hilti-Research/hilti-trimble-slam-challenge-2026)",
      "title": "Hilti × Trimble 360 Visual-Inertial SLAM Challenge 2026 — README (commit e0c9277)",
      "published": null,
      "url": "https://github.com/Hilti-Research/hilti-trimble-slam-challenge-2026/blob/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "공사 현장 시계열 SLAM 챌린지 데이터 설명(고정 커밋, 회사 주도 산업 벤치마크). 평면도 완공 의도 상태 설명과 2026-09-21 센서 동기화 설명 추가 기록을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "출처 충돌: Aliyev·Barsi(2026)의 픽셀 세기 기준선 MAPE 5.68%·1.58%는 초록(방 개체 단위·도면 단위)과 §4.1·표 2(방 유형별 도면 단위 비교 472쌍)가 평가 단위를 다르게 적는데, 어느 쪽이 맞으며 재현 가능한 출력이 공개됐는가?",
      "areas": [
        45,
        14
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "도면 인식 벤치마크의 픽셀 기준 점수(방 IoU 0.5, 모서리 10픽셀·5도)를 실제 문 통과 폭·충전기 접근 가능성 같은 미터 단위 주행 조건으로 검증한 평가나 사례가 있는가?",
      "areas": [
        45,
        14
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "여러 제조사 로봇이 장면 그래프를 공유할 때 주기적 전체 전송 대신 변경분 전송, 통신 단절 뒤 재접속, 삭제 충돌 처리를 시험해 허용 기준을 보고한 사례나 공개 구현이 있는가?",
      "areas": [
        45,
        18
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "시설 카메라망 기반 다중 로봇 제어를 사람이 함께 다니는 구역이나 장시간 운용에서 시험해 시간당 사람 개입 수와 인식 원인 정지를 보고한 사례가 있는가?",
      "areas": [
        45,
        54
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
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
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
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
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#5-적용-사례-현장-유형-명시",
      "title": "45. 문서·도면·장면 이해"
    }
  ],
  "standards_updates": [
    {
      "name": "Spark-DSG (동적 장면 그래프 라이브러리, Python API)",
      "kind": "오픈소스",
      "org": "MIT-SPARK",
      "url": "https://github.com/MIT-SPARK/Spark-DSG/blob/3c40997e4ae739c56ed3cdd6ef5e882d403d8b64/examples/python_api.py",
      "related_areas": [
        45,
        16,
        18
      ],
      "ref_id": "ref-1675",
      "summary": "JSON 장면 그래프 파일을 DynamicSceneGraph.load 로 불러와 객체·장소·방 층과 노드에 접근하는 API 를 제공한다. 같은 연구실 구현의 API 이며 다중 제조사 교환 표준은 아니다."
    },
    {
      "name": "KDoc-OCRBench-V2 (한국어 문서 OCR 벤치마크 v2)",
      "kind": "평가 프로그램",
      "org": "ONTHEIT",
      "url": "https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md",
      "related_areas": [
        45
      ],
      "ref_id": "ref-1673",
      "summary": "제공자 설명에 따르면 한국 공공부문 단일 쪽 PDF 849개와 검증 시험 56,197건으로 구성한 OCR 벤치마크다(벤더 주장, 외부 재현 없음). 로봇 매뉴얼은 따로 포함하지 않는다."
    }
  ],
  "additional_research_requests": [
    "6·7·8·11절 분리 주제 페이지(docs/topics/2026/2026-09-30-area45-s6.md·s7.md·s8.md·s11.md) 본문이 입력에 없어, AAS-RAIL·LangExtract·Robinson·Strader 기존 문장에 조건을 직접 덧붙이지 못하고 세부영역 페이지 각 절의 '2026-10-12 갱신' 소절로 붙였다. 다음 갱신 실행에서 이 주제 페이지들을 입력에 넣어 해당 문장 자리에 조건을 반영할지 검토가 필요하다.",
    "트랙 반영 제안 3건(실행 2026-10-09-21·2026-10-09-23·2026-10-09-26, 8. 대표 연구와 자료 대상)은 이번 브리프에 근거 finding·출처가 없어 반영하지 않았다. 다음 45. 문서·도면·장면 이해 실행의 리서치가 해당 트랙 실행의 finding 과 출처(도메인 이동, MMLongBench-Doc, Xia 외 유효 생성률, 평면도 학습 데이터 클래스 구성 등)를 브리프로 옮겨야 한다.",
    "후속 정리: L. AI·학습 기술 대분류 페이지의 '다른 대분류와의 연결' 절에 'CCTV 카메라 30대만으로'(22. 설비·건물 시스템 연동 연결)와 'Strader 외 … 로봇 대수·실험 수치는 초록에 없음'(D. 공간·지도 모델 연결) 문장이 남아 있다. 대분류 연결 실행이나 갱신 실행에서 ref-1065·ref-1070 의 이번 확인 결과로 정리할 필요가 있다. Robinson 외 사례를 인용한 다른 영역 페이지(예: 22. 설비·건물 시스템 연동, 61. 물류창고)의 '창고 CCTV' 표현도 확인이 필요하다.",
    "5절 물류창고 사례의 흐름 단계와 목표 도착 판정 기준, 실외 사례의 제약·완료·인계 칸은 브리프에 근거가 없어 미확인으로 두었다.",
    "oq-227: 고정 카메라와 로봇 인식 결과를 합칠 때의 허용 시간 차·좌표 정합 기준 수치를 정한 연구·제품 문서가 여전히 필요하다."
  ],
  "fixes_applied": [
    "f11: 6절 BIM 정합 요약과 8절 BIM-Loc 항목에서 'Ouster OS0-128로 기록한 시퀀스 7개, Livox Mid-360으로 기록한 시퀀스 2개, 모두 9개 시퀀스(누적 3.5 km 초과)'로 시퀀스 수임을 밝혀 썼다.",
    "f19: 'ICSR 2026 게재'를 쓰지 않고 8절 기존 항목 조건에 'arXiv 2606.17073, 2026-06-10, 게재처 미확인'으로 적었으며 각주 ref-239 도 arXiv 기준으로 유지했다.",
    "f27: 'ISER 2025 게재'를 쓰지 않고 5절 실외 서술과 8절 Strader 항목에 'arXiv v2(2025-07-10) 기준, 게재처 미확인'으로 적었다.",
    "f13·f14·f24: 6절 Hilti 문장, 7절 KDoc-OCRBench-V2 행, 11절 oq-225·oq-227 부분 근거를 모두 [추정]으로 두고 '벤더 주장'을 병기했다.",
    "f8: 8절 Aliyev·Barsi 항목에 초록(방 개체 단위·도면 단위)과 §4.1·표 2(472쌍 도면 단위 방 유형 비교) 서술을 둘 다 제시하고 성능 근거로 쓰지 않는다고 밝혔으며, 11절과 open_question_updates 에 출처 충돌 새 질문으로 올렸다.",
    "f9·f15·f18·f22·f31·f38·f39: 각 문장을 [의견]으로 두고 '구축자 의견'임과 근거 finding 의 출처 각주를 함께 달았으며(f9·f18·f22·f38은 6절, f15는 10절, f31은 7절, f39는 5절), 메모·내부 정정 문구는 싣지 않았다.",
    "f10~f15: 6절에는 BIM 좌표·현장 정합 요약을 세 문장(f10, f11·f12, f13·f14)으로만 두고 f15 의견은 10절 14. 도면·BIM에서 지도 만들기 연결로 옮겼으며, BIM-Loc(6·8절)과 Strader 외 재위치(5절)를 '연계 대상: 로봇 자체 위치 추정'으로 표시하고 9절에 ROP는 결과의 조건·평가 기준만 받는다는 문단을 더했다.",
    "5절 물류창고 사례: 사례 제목과 수행 자원 칸을 '연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4·Camera Module 3, PoE 전원, 5 fps)'로 고치고, 작업 대상을 무작위 목표 지점 간 이동 임무(운반물 처리 아님), 제약에 로봇만 있던 시험 구역, 예외·성과에 45분·1.3 km·임무 76건·개입 4회(충돌 2·인식 원인 2)를 채웠으며 각주 ref-1065 의 서지 제목은 그대로 두었다.",
    "9절: '카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인' 문장을 '5절 물류창고 사례의 카메라는 연구팀이 설치했고 시설 CCTV 재사용 사례가 아니다 [사실][^ref-1065]. 기존 시설 CCTV 재사용 시 소유·운영 주체는 미확인이다'로 바꿨다.",
    "5절 실외 사례: 수행 자원 칸에 실물 종단 간 실험 Husky·Spot 2대와 절제 실험 Kimera-Multi 데이터셋 로봇 3대 기록을 함께 적고, 예외·성과 칸에 재위치 64%·65%(5 m·10도, 의사 정답 기준)와 임무 시험 단일 8회·다중 12회 실행 성공률, 시험 횟수 한계를 적었으며 site_matrix_updates 는 실제로 채운 네 칸만 냈다.",
    "f16·f17: 기존 51.8%→71.7%·56.2% 서술은 분리 주제 페이지에 그대로 두고, 6절 갱신 소절과 8절 기존 항목 조건에 '고정 슬롯 값 예측 조건(속성 검출 미평가)'과 '모호성을 무시한 낙관적 정규식 기준, 이름·값 동시 13.4%'를 덧붙였다.",
    "f23: 7절 AI Hub 문단에 설계단계(계획·실시)·축척 필수 속성과 1.0판 2023-07-26·1.1판 2023-12-15를 적고 '축적도는 축척의 오기' 판단은 쓰지 않았으며, 각주 ref-1012 발행일을 2023-07-26 으로 맞췄다.",
    "각주: 13절에 ref-1667~ref-1676 정의를 공통 형식으로 추가하고(발행일 없는 ref-1669·1671·1672·1673·1675·1676은 '미확인', ref-1669 제목의 개발 브랜치 원본 표기 유지), 재사용 출처 8건의 접근일을 2026-10-12 로 갱신했으며 프런트매터 sources 에 새 id 를 더했다.",
    "인용: 출처 원문 직접 인용을 쓰지 않고 모두 요약·재서술했다(ref-1065·ref-1070·ref-1071 포함).",
    "열린 질문: 11절에 oq-147·oq-196·oq-225·oq-226·oq-227 의 부분 근거만 붙이고 상태는 바꾸지 않았으며, oq-197·oq-228 은 다루지 않았고, 새 질문 4건을 브리프 문구 그대로 open_question_updates 에 등록했다.",
    "트랙 반영 제안 3건(실행 2026-10-09-21·23·26)은 8절에 반영하지 않고 additional_research_requests 에 다음 해당 영역 실행으로 넘긴다고 적었다.",
    "약어: IoU(6·8절), MAPE(8절), ATE·IMU·PPS(6절), OCR(7절)를 첫 등장 때 풀어 썼다.",
    "분량 초과 자동 분리: 45. 문서·도면·장면 이해 본문 14,510자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 5,269자"
  ]
}
```

### runs/2026-10-12-07/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-12-area45-s6.md (2,996자)
    - docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-12-area45-s8.md (2,545자)
    - docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md "11. 열린 질문" → docs/topics/2026/2026-10-12-area45-s11.md (1,701자)
    - docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-12-area45-s7.md (1,522자)
    - docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-12-area45-s10.md (1,054자)
```

### runs/2026-10-12-07/pages/categories/ai-and-learning/document-drawing-and-scene-understanding.md

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
updated: 2026-10-12
sources: [ref-308, ref-1065, ref-063, ref-1012, ref-1066, ref-239, ref-1067, ref-513, ref-1068, ref-1069, ref-1070, ref-067, ref-1071, ref-1072, ref-1073, ref-1074, ref-1667, ref-1668, ref-1669, ref-1670, ref-1671, ref-1672, ref-1673, ref-1674, ref-1675, ref-1676]
last_run: 2026-10-12
version: 3
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 45. 문서·도면·장면 이해

# 45. 문서·도면·장면 이해

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
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

이기종 로봇 등록과 능력 표현에 필요한 정보는 제조사 문서·데이터시트·[URDF(Unified Robot Description Format, 통합 로봇 기술 형식)](../../glossary/urdf.md)에 흩어져 있고, 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며, 로봇 한 대로는 가려지는 공간 상태는 여러 로봇과 고정 카메라의 인식을 모아야 알 수 있으므로, 이 영역의 해석 오류는 그대로 등록 정보·지도·세계 상태의 오류로 이어진다고 볼 수 있다. [추정][^ref-1072][^ref-1071][^ref-239][^ref-1073][^ref-1066][^ref-308][^ref-1065][^ref-1069]

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
| 작업 대상 | 쇼핑몰 평면도 25장과 그 안의 점포 1,340개(공간·정보) [사실][^ref-1066] |
| 수행 자원 | 도면 인식 소프트웨어: 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고, 2단계 영역 성장 분할과 문자 인식으로 평면도의 점포 공간을 식별한다 [사실][^ref-1066] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%(2022-03 발표) [사실][^ref-1066] |

이 사례는 로봇 현장 배치가 아니라 쇼핑몰 평면도 25장에 대한 논문 평가 결과다. [사실][^ref-1066] 저자들은 실내 로봇 주행을 이 방법의 활용처 가운데 하나로 들었다. [사실][^ref-1066]

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

**사례:** 연구팀이 설치한 카메라망만으로 여러 로봇을 계획·제어하는 창고 시험(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 시험용으로 30개 카메라 시야 가운데 무작위로 정한 목표 지점이 로봇마다 배정된다 [사실][^ref-1065] |
| 작업 대상 | 30개 카메라 시야 안의 무작위 목표 지점 사이를 오가는 지점 간 이동 임무(공간)이며, 운반물 처리는 아니다 [사실][^ref-1065] |
| 수행 자원 | 작업용 주행 장비를 싣지 않은 로봇 4대, 연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4·Camera Module 3, PoE 전원, 5 fps), 외부 계산 자원 [사실][^ref-1065] |
| 제약 | 약 27 m 통로 6개의 중형 창고 시험 구역이며, 시험 구역에는 로봇만 있었다. 시야가 겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는다 [사실][^ref-1065] |
| 완료·인계 | 로봇이 목표 지점에 도착하면 바로 새 목표를 받는다(도착 판정 기준은 미확인) [사실][^ref-1065] |
| 예외·성과 | 45분 동안 로봇 4대가 1.3 km를 다니며 지점 간 임무 76건을 마쳤고, 사람 개입은 4회(10·17·37·41분)였다. 앞의 두 번은 최대 곡률 구간 추종 실패로 인한 충돌로, 두 번째 개입 뒤 현장에서 제어 이득을 조정해 해소했다. 뒤의 두 번은 로봇 일시 오분류와 학습이 적은 시각 영역의 방향 추정 오류가 자세 갱신 시간 초과로 제어기를 멈춘 인식 원인이었다 [사실][^ref-1065] |

이 시스템은 보정하지 않은 화소 단위 위상 카메라 그래프 위, 즉 영상 공간에서 여러 로봇을 계획·제어하며, 저자들은 이를 첫 현장 시연이라고 밝혔다(2026-06 발표). [사실][^ref-1065] 카메라는 연구팀이 시험 구역에 따로 설치한 것으로, 창고가 원래 운영하던 CCTV를 재사용한 것이 아니다(논문 제목의 CCTV 표현과 구별해 읽는다). [사실][^ref-1065] 개입 4회는 로봇만 있는 시험 구역에서 45분 동안 나온 값이며, 저자들은 시제품 조건이라고 밝혔다. [사실][^ref-1065] 로봇 주행을 외부 카메라로 옮긴 방식이므로 9절에서 경계가 이동한 사례로 다룬다.

**현장 유형:** 실외

**사례:** 운영자의 자연어 의도로 여러 로봇에 대규모 실외 작업 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운영자가 자연어로 의도를 말하면 LLM(Large Language Model, 대규모 언어 모델)이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 [PDDL(계획 도메인 정의 언어)](../../glossary/pddl.md) 목표로 바꾼다 [사실][^ref-1070] |
| 작업 대상 | 대규모 실외 환경과 그 안의 객체(개방형 객체 지도를 담은 공유 3차원 장면 그래프로 표현) [사실][^ref-1070] |
| 수행 자원 | 종단 간 실물 실험은 이종 로봇 2대(바퀴형 Clearpath Husky, 4족 Boston Dynamics Spot)로 했고, 장면 그래프 융합 절제 실험은 Kimera-Multi 데이터셋의 로봇 3대 기록(acl_jackal2, sparkal1, sparkal2)을 썼다. 계획 쪽은 LLM과 다중 로봇 계획·실행 시스템이 맡는다 [사실][^ref-1070] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 두 로봇 사이 재위치 성공률은 Husky 64%, Spot 65%였다(약 500 m 구간에서 10 m마다 두 로봇 카메라 간 상대 자세를 추정해, 수동 확인한 루프 폐쇄로 만든 의사 정답과 5 m·10도 이내면 성공) [사실][^ref-1070]. 자연어 임무 시험은 단일 로봇 8회·다중 로봇 12회이며, 실행 성공률은 단일 로봇이 쉬움·중간·어려움 100%·50%·50%, 다중 로봇이 66%·100%·75%였다. 시험 횟수가 적어 비율 비교에는 한계가 있다 [사실][^ref-1070]. 실패 시 복구 주체는 미확인 |

이 시스템은 개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고, 대규모 실외 환경의 실제 작업으로 평가했다(2025-07 개정판). [사실][^ref-1070] 실물 실험 장소는 West Point Camp Buckner의 실외 환경이며, 서지는 arXiv v2(2025-07-10) 기준이고 게재처는 미확인이다. [사실][^ref-1070] 재위치 성공률은 측량 정답이 아니라 의사 정답 기준이며 도킹 정밀도를 판정한 값이 아니다. [사실][^ref-1070] 재위치 자체는 연계 대상: 로봇 자체 위치 추정의 결과다(9절).

구축자 의견으로는, 다중 로봇 실증을 인용할 때 임무 완료 수와 사람 개입 수, 실물 로봇 대수와 데이터셋 재생 대수를 함께 적어야 하며, 5 m·10도 기준의 재위치 성공률을 좁은 통로나 도킹의 정밀 위치 보증으로 바꿔 읽지 않아야 한다. [의견][^ref-1065][^ref-1070] 같은 의견으로, 외부 카메라 기반 운용에서는 로봇 외형이 비슷해지거나 학습이 적은 구역이 생길 때의 인식 재검증·정지·복구 담당을 미리 정해 두어야 한다. [의견][^ref-1065]

## 6. 대표 접근법과 기술

문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1073][^ref-1071][^ref-1069]

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area45-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에서 쓰는 도구·벤치마크·데이터셋은 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area45-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 판단 근거가 된 연구와 자료는 다음과 같다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 대표 연구와 자료](../../topics/2026/2026-10-12-area45-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 인식 결과(위치·장면 그래프)를 받아 시간·좌표를 맞춰 고정 카메라 결과와 하나의 공간 상태로 합치는 플랫폼 수준 융합 [추정][^ref-308][^ref-1070] | 연계 대상: 로봇 온보드 센서 인식·SLAM·국지 회피는 로봇 제조사가 맡는다 [추정][^ref-308][^ref-1070] |
| 시설·설비 제어 | 시설 카메라의 영상·인식 결과를 받아 해석하는 인터페이스와 검토 절차 [추정][^ref-308][^ref-1065] | 연계 대상: CCTV·영상 관리 시스템과 카메라 설치·동기화 [추정][^ref-308][^ref-1065] |

ROP가 이 영역에서 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가, 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름, 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 융합이다. [추정][^ref-1067][^ref-1068][^ref-1071][^ref-1074][^ref-308][^ref-1070] 도면·BIM 작성 도구와 원본 도면은 설계·건축 쪽의 연계 대상이고, ROP는 그 결과물을 받아 해석한다. [추정][^ref-067][^ref-1012] 5절 물류창고 사례의 카메라는 연구팀이 시험을 위해 설치했고, 시설이 원래 운영하던 CCTV를 재사용한 사례가 아니다. [사실][^ref-1065] 기존 시설 CCTV를 재사용할 때의 소유·운영 주체는 미확인이다.

5절 물류창고 사례처럼 로봇에 작업용 주행 장비를 두지 않고 외부 카메라와 외부 계산으로 주행을 제어하는 방식은 ROP의 기본 범위가 아니라, [범위 경계](../../about/scope-boundary.md)의 원문 19장이 말하는 "이 경계는 제품 전략에 따라 이동할 수 있다"에 해당하는 사례로 본다. [추정][^ref-1065]

6절의 BIM 기반 LiDAR 위치 추정(BIM-Loc)과 5절 실외 사례의 두 로봇 사이 재위치는 연계 대상: 로봇 자체 위치 추정에 속한다. 구축자 의견으로는, ROP는 그 결과를 받을 때 정답 종류(실측 정답·의사 정답·대리 지표)와 판정 기준(예: 5 m·10도) 같은 조건만 함께 받아 평가 기준으로 쓰고, 위치 추정 기능 자체는 맡지 않는다. [의견][^ref-1670][^ref-1070]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 다른 연구영역과의 연결](../../topics/2026/2026-10-12-area45-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 질문과 이번 실행의 부분 근거는 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 열린 질문](../../topics/2026/2026-10-12-area45-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md) — 영역 심화: 3~11절 신규 작성(문서 파싱·데이터시트 속성 추출·도면 인식·고정 카메라와 로봇 인식 융합, 상업 시설·제조 공장·물류창고·실외 적용 사례), 각주 16건, 새 열린 질문 4건. 2차: 10절 첫 문장의 영역 호칭을 번호와 이름으로 고침 (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area45-s6.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "6. 대표 접근법과 기술" 절(2,104자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 열린 질문](../../topics/2026/2026-09-30-area45-s11.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "11. 열린 질문" 절(1,145자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area45-s7.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,004자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area45-s10.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다. 2차: 세 줄 요약 첫 항목과 본문 첫 문장의 영역 호칭을 번호와 이름으로 고침 (실행 2026-09-30-08)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-10-12
[^ref-1065]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-10-12
[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 2023-07-26, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-10-12
[^ref-1066]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-10-12
[^ref-1067]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-1068]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-1069]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-10-12
[^ref-1070]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-10-12
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-10-12
[^ref-1072]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1073]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-10-12
[^ref-1074]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
[^ref-1670]: Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research), BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization, 2026-06-12, https://arxiv.org/abs/2606.14237v1, 접근일 2026-10-12
```

### docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md

```markdown
---
title: "45. 문서·도면·장면 이해"
type: area
category: "L. AI·학습 기술"
area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [문서 파싱, 도면 인식, 자산관리셸, 출처 근거 연결, 인프라 장착 센서, 3차원 장면 그래프]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-308, ref-1065, ref-063, ref-1012, ref-1066, ref-239, ref-1067, ref-513, ref-1068, ref-1069, ref-1070, ref-067, ref-1071, ref-1072, ref-1073, ref-1074]
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
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
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

이기종 로봇 등록과 능력 표현에 필요한 정보는 제조사 문서·데이터시트·[URDF(Unified Robot Description Format, 통합 로봇 기술 형식)](../../glossary/urdf.md)에 흩어져 있고, 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며, 로봇 한 대로는 가려지는 공간 상태는 여러 로봇과 고정 카메라의 인식을 모아야 알 수 있으므로, 이 영역의 해석 오류는 그대로 등록 정보·지도·세계 상태의 오류로 이어진다고 볼 수 있다. [추정][^ref-1072][^ref-1071][^ref-239][^ref-1073][^ref-1066][^ref-308][^ref-1065][^ref-1069]

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
| 작업 대상 | 쇼핑몰 평면도 25장과 그 안의 점포 1,340개(공간·정보) [사실][^ref-1066] |
| 수행 자원 | 도면 인식 소프트웨어: 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고, 2단계 영역 성장 분할과 문자 인식으로 평면도의 점포 공간을 식별한다 [사실][^ref-1066] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%(2022-03 발표) [사실][^ref-1066] |

이 사례는 로봇 현장 배치가 아니라 쇼핑몰 평면도 25장에 대한 논문 평가 결과다. [사실][^ref-1066] 저자들은 실내 로봇 주행을 이 방법의 활용처 가운데 하나로 들었다. [사실][^ref-1066]

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
| 수행 자원 | 작업용 주행 장비를 싣지 않은 로봇 4대, 창고 CCTV 카메라 30대, 외부 계산 자원 [사실][^ref-1065] |
| 제약 | 길이 27 m 통로 6개. 시야가 겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는다 [사실][^ref-1065] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(임무 시간·조율 통계 수치가 초록에 없음) |

이 시스템은 보정하지 않은 화소 단위 위상 카메라 그래프 위, 즉 영상 공간에서 여러 로봇을 계획·제어하며, 저자들은 이를 첫 현장 시연이라고 밝혔다(2026-06 발표). [사실][^ref-1065] 로봇 주행을 외부 카메라로 옮긴 방식이므로 9절에서 경계가 이동한 사례로 다룬다.

**현장 유형:** 실외

**사례:** 운영자의 자연어 의도로 여러 로봇에 대규모 실외 작업 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운영자가 자연어로 의도를 말하면 LLM(Large Language Model, 대규모 언어 모델)이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 [PDDL(계획 도메인 정의 언어)](../../glossary/pddl.md) 목표로 바꾼다 [사실][^ref-1070] |
| 작업 대상 | 대규모 실외 환경과 그 안의 객체(개방형 객체 지도를 담은 공유 3차원 장면 그래프로 표현) [사실][^ref-1070] |
| 수행 자원 | 여러 로봇(대수 미확인)과 LLM, 다중 로봇 계획·실행 시스템 [사실][^ref-1070] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(실험 수치가 초록에 없음) |

이 시스템은 개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고, 대규모 실외 환경의 실제 작업으로 평가했다(2025-07 개정판). [사실][^ref-1070]

## 6. 대표 접근법과 기술

문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1073][^ref-1071][^ref-1069]

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
| 로봇 자체 지능·제어 | 로봇이 내는 인식 결과(위치·장면 그래프)를 받아 시간·좌표를 맞춰 고정 카메라 결과와 하나의 공간 상태로 합치는 플랫폼 수준 융합 [추정][^ref-308][^ref-1070] | 연계 대상: 로봇 온보드 센서 인식·SLAM·국지 회피는 로봇 제조사가 맡는다 [추정][^ref-308][^ref-1070] |
| 시설·설비 제어 | 시설 카메라의 영상·인식 결과를 받아 해석하는 인터페이스와 검토 절차 [추정][^ref-308][^ref-1065] | 연계 대상: CCTV·영상 관리 시스템과 카메라 설치·동기화 [추정][^ref-308][^ref-1065] |

ROP가 이 영역에서 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가, 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름, 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 융합이다. [추정][^ref-1067][^ref-1068][^ref-1071][^ref-1074][^ref-308][^ref-1070] 도면·BIM 작성 도구와 원본 도면은 설계·건축 쪽의 연계 대상이고, ROP는 그 결과물을 받아 해석한다. [추정][^ref-067][^ref-1012] 카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인이다.

5절 물류창고 사례처럼 로봇에 작업용 주행 장비를 두지 않고 외부 카메라와 외부 계산으로 주행을 제어하는 방식은 ROP의 기본 범위가 아니라, [범위 경계](../../about/scope-boundary.md)의 원문 19장이 말하는 "이 경계는 제품 전략에 따라 이동할 수 있다"에 해당하는 사례로 본다. [추정][^ref-1065]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area45-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 질문과 이번 실행의 부분 근거는 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 열린 질문](../../topics/2026/2026-09-30-area45-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md) — 영역 심화: 3~11절 신규 작성(문서 파싱·데이터시트 속성 추출·도면 인식·고정 카메라와 로봇 인식 융합, 상업 시설·제조 공장·물류창고·실외 적용 사례), 각주 16건, 새 열린 질문 4건. 2차: 10절 첫 문장의 영역 호칭을 번호와 이름으로 고침 (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area45-s6.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "6. 대표 접근법과 기술" 절(2,104자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 열린 질문](../../topics/2026/2026-09-30-area45-s11.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "11. 열린 질문" 절(1,145자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area45-s7.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,004자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-08)
- 2026-09-30 · 생성 · [45. 문서·도면·장면 이해 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area45-s10.md) — 자동 분리: 45. 문서·도면·장면 이해 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다. 2차: 세 줄 요약 첫 항목과 본문 첫 문장의 영역 호칭을 번호와 이름으로 고침 (실행 2026-09-30-08)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1065]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 미확인, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-1066]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-30
[^ref-1067]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-1068]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-1069]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1070]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1072]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1073]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-1074]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
```

### runs/2026-10-12-07/pages/topics/2026/2026-10-12-area45-s6.md

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
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1069, ref-1071, ref-1073, ref-1667, ref-1668, ref-1669, ref-1670, ref-1671, ref-1672, ref-1676, ref-239, ref-308]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md#6
---

[홈](../../index.md) › [주제](../index.md) › 45. 문서·도면·장면 이해 — 대표 접근법과 기술

# 45. 문서·도면·장면 이해 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1073][^ref-1071][^ref-1069]
- 이 페이지는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1073][^ref-1071][^ref-1069]


### 2026-10-12 갱신: 점수의 조건과 근거 위치

아래는 분리 주제 페이지 [45. 문서·도면·장면 이해 — 대표 접근법과 기술](2026-09-30-area45-s6.md)의 서술(데이터시트 속성 추출, 원문 위치 연결, 도면 인식, 고정 카메라와 로봇 인식 융합)에 붙는 조건이다. 기존 문장은 그대로 두고 조건만 더한다.

**도면 인식 점수의 입력과 범위.** AECV-Bench는 평가 전부에 원본 CAD·BIM 형식(DWG, RVT, IFC)이 아닌 래스터 PNG 도면 영상을 입력으로 쓰며, 벡터 기하나 객체 계층을 쓰는 모델은 평가하지 않는다. [사실][^ref-1073] 개수 세기 과제는 문·창·침실·화장실 4종만 다루고 계단·엘리베이터·기계 설비·구조 부재·내화 구성은 평가하지 않는다. [사실][^ref-1073] 구축자 의견으로는, ROP가 도면 인식 점수를 인용할 때 입력 형식(래스터 또는 벡터·BIM), 평가에서 빠진 객체, 판정 기준(IoU(Intersection over Union, 교집합 대 합집합 비)·픽셀 허용 오차), 평가 분모(유효 출력 표본과 전체 표본)를 함께 적어야 한다. [의견][^ref-1073][^ref-1667][^ref-1668] 같은 의견으로, 픽셀 기준 점수를 미터 단위 통과 가능성으로 바꿔 읽지 않고 승강기·방화문·충전 위치 같은 운영 객체는 별도 인수 시험으로 확인해야 한다. [의견][^ref-1073][^ref-1667]

**BIM 좌표와 현장 정합(요약).** IFC 4.3의 IfcMapConversion은 국지 공학 좌표계를 지도 좌표계로 옮기는 변환(세 축 공통 축척 하나, z축 기준 반시계 회전, Eastings·Northings·OrthogonalHeight 이동)을 기술하며, 지리 좌표계에서 지도로의 투영 자체는 다루지 않는다(개발 브랜치 원본 기준). [사실][^ref-1669] BIM-Loc의 공사장 데이터는 손에 든 센서로 기록한 9개 시퀀스(Ouster OS0-128로 기록한 시퀀스 7개, Livox Mid-360으로 기록한 시퀀스 2개, 누적 3.5 km 초과)이며, 정답 궤적이 없어 절대 궤적 오차(Absolute Trajectory Error, ATE) 대신 대리 지표로 평가한다(연계 대상: 로봇 자체 위치 추정). [사실][^ref-1670] Hilti × Trimble 2026 SLAM 챌린지 저장소는 평면도가 공사 종료 시점의 의도된 상태라 이른 시기 기록에는 일부 요소가 없다고 적고, 2026-09-21에 정답 수집 장치의 센서 동기화 설명(정답 LiDAR와 관성 측정 장치(Inertial Measurement Unit, IMU)는 초당 펄스(Pulse Per Second, PPS) 신호로 하드웨어 동기화하고, Insta360은 두 IMU 신호의 자이로 크기를 맞춰 시간 오프셋·시계 배율을 추정)을 더했다고 기록한다(벤더 주장). [추정][^ref-1676] 이 주제의 자세한 서술은 10절의 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙으로 넘긴다.

**데이터시트·URDF 추출의 조건.** AAS-RAIL의 51.8%→71.7%는 미리 정한 목표 속성마다 값 하나를 채우는 고정 슬롯 값 예측(문법 제약 디코딩) 조건의 속성 추출 정확도이며, 속성 검출은 평가 범위 밖이라 정밀도·재현율·F1은 보고되지 않았다. [사실][^ref-1071] 원문에서 확인 가능한 속성 56.2%는 여러 번 나오거나 무관한 일치의 모호성을 일부러 무시한 낙관적 정규식 검색으로 정답 속성값이 문서에서 발견된 비율이며, 속성 이름과 값이 함께 문서에 있는 경우는 13.4%였다. [사실][^ref-1071] 구축자 의견으로는, 기존 51.8%→71.7%·56.2% 서술은 유지하되 이 조건과 함께 읽어야 하며, 원문에 같은 값이 있다는 것과 그 값이 그 속성의 근거라는 것은 따로 검토해야 한다. [의견][^ref-1071] URDF에서 대규모 언어 모델(Large Language Model, LLM) gpt-oss:20b로 로봇 온톨로지를 채우는 예비 평가(PR2·Pepper·TIAGo)에서는 Pepper의 사용자 신호용 ChestButton이 접촉면 하위 유형의 Bumper로 분류됐고, 저자들은 물리적 성질은 맞았지만 항행 안전 센서와 사람–로봇 상호작용 입력을 구분할 기능 문맥이 없었다고 설명한다(세 플랫폼 예비 사례라 오류 비율은 산출할 수 없다). [사실][^ref-239]

**원문 위치 연결의 빈칸.** LangExtract의 Extraction 자료형은 추출 텍스트를 원문에서 찾지 못하면 원문 문자 구간(char_interval)을 None으로 두므로, 항목마다 원문 위치가 항상 붙는 것은 아니다. [사실][^ref-1671] Docling Core의 근거 항목 ProvenanceItem은 쪽 번호(page_no)·영역 상자(bbox)·문자 구간(charspan) 세 필드를 모두 필수로 가진다. [사실][^ref-1672] 구축자 의견으로는, 추출값과 근거 위치를 따로 저장하고 char_interval이 None이거나 근거 항목 자체가 없는 추출은 검토 대기로 두어야 하며, 위치가 있다는 사실만으로 로봇 능력을 실행 가능으로 확정하지 않는다. [의견][^ref-1671][^ref-1672]

**고정 카메라와 로봇 관측 융합의 조건.** Brorsson 외의 상용차 공장 배치에서 각 천장 카메라는 장애물 검출용 저해상도(640×360) 영상을 10 Hz, 로봇 위치 추정용 고해상도(3840×2160) 영상을 1 Hz로 보내고, 로봇은 1 Hz 위치 추정값을 탑재 모터 오도메트리와 융합해 실시간 위치를 얻는다. [사실][^ref-308] RGB 영상만 쓰는 능동 장면 그래프 연구는 MapAnything이 모든 카메라 자세를 첫 입력 영상 기준으로 내므로, 첫 영상의 자세(외부 카메라 또는 로봇 초기 시점)만 알면 모든 자세를 일관된 전역 좌표로 나타낼 수 있다고 적는다. [사실][^ref-1069] 같은 연구의 기하 관계 판정 임계값은 실험 내내 고정하되 데이터셋마다 한 번 경험적으로 맞췄고, 관계 정답이 없어 정량 평가는 노드에만 했다. [사실][^ref-1069] 구축자 의견으로는, 고정 카메라와 로봇 관측을 합치는 입력에 수집 시각·좌표 기준·관측 주기·동기화 방식(하드웨어 동기 여부)·정답 종류를 붙여야 하며, 공장 배치 보고·연구 실험·데이터셋 설명의 서로 다른 조건을 합쳐 범용 허용 시간 차를 만들어서는 안 된다. [의견][^ref-308][^ref-1069][^ref-1676] 허용 시간 차 수치는 이번 조사에서도 찾지 못했다(11절 oq-227).

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

[^ref-1069]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-10-12
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-10-12
[^ref-1073]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-10-12
[^ref-1667]: Phung, H., & Averbuch-Elor, H. (Cornell University, arXiv; SIGGRAPH 2026), Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction, 2026-08-07, https://arxiv.org/abs/2602.09016v3, 접근일 2026-10-12
[^ref-1668]: Aliyev, N., & Barsi, Á. (Periodica Polytechnica Civil Engineering), Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images, 2026-08-05, https://pp.bme.hu/ci/article/view/44138, 접근일 2026-10-12
[^ref-1669]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcMapConversion (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 HTML과 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md, 접근일 2026-10-12
[^ref-1670]: Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research), BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization, 2026-06-12, https://arxiv.org/abs/2606.14237v1, 접근일 2026-10-12
[^ref-1671]: Google (google/langextract), LangExtract — langextract/core/data.py (Extraction 자료형, commit 74df59f), 미확인, https://github.com/google/langextract/blob/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py, 접근일 2026-10-12
[^ref-1672]: Docling Project (docling-project/docling-core), docling-core — docling_core/types/doc/common/reference.py (ProvenanceItem, commit 0d5a7bd), 미확인, https://github.com/docling-project/docling-core/blob/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py, 접근일 2026-10-12
[^ref-1676]: Hilti Research · Trimble · Oxford DRS (Hilti-Research/hilti-trimble-slam-challenge-2026), Hilti × Trimble 360 Visual-Inertial SLAM Challenge 2026 — README (commit e0c9277), 미확인, https://github.com/Hilti-Research/hilti-trimble-slam-challenge-2026/blob/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md, 접근일 2026-10-12
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-10-12
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-07 | 45. 문서·도면·장면 이해 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-07/pages/topics/2026/2026-10-12-area45-s8.md

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
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1065, ref-1070, ref-1071, ref-1667, ref-1668, ref-1670, ref-1674, ref-239]
last_run: 2026-10-12
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


### 2026-10-12 갱신: 새 연구와 기존 항목의 조건

분리 주제 페이지 [45. 문서·도면·장면 이해 — 대표 연구와 자료](2026-09-30-area45-s8.md)의 목록에 더하는 항목과 기존 항목에 붙는 조건이다.

새 항목:

- Phung·Averbuch-Elor, Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction(arXiv v3 2026-08-07, SIGGRAPH 2026) — 평면도 래스터 영상을 방 다각형 시퀀스로 복원한다. 평가는 Stekovic 외(2021)의 프로토콜을 따라 정답 방마다 IoU(Intersection over Union, 교집합 대 합집합 비)가 가장 큰 예측 방을 짝짓고 IoU가 0.5를 넘을 때 유효로 보며, Room·Corner·Angle을 정밀도·재현율·F1으로 잰다. [사실][^ref-1667] 모서리 판정(거리 10픽셀 이내, 각도 차 5도 미만)도 같은 선행 프로토콜을 따른 것이고 모든 데이터셋을 256×256 해상도로 실험했으므로, 시설의 미터 단위 허용 오차와는 다른 픽셀 기준이다. [사실][^ref-1667] 저자들은 한계로 문·창 위치를 가끔 잘못 잡아 방 안에 문·창을 만드는 실패 예를 들지만 발생률은 보고하지 않는다. [사실][^ref-1667]
- Aliyev·Barsi, Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images(Periodica Polytechnica Civil Engineering 70(3), 2026-08-05 온라인) — 시각–언어 모델 3종의 방 면적 추정을 색상으로 방 유형을 구분한 주거 평면도 100장으로 평가했다. BakLLaVA는 100장 모두에서 실제 예측 대신 템플릿 자리표시자를 내(검증 실패 시 1회 재시도 후 사용 불가 처리) 정량 평가에서 빠졌고, LLaVA-LLaMA 3와 MiniCPM-V 2.6만 평가됐다. [사실][^ref-1668] 방은 개체가 아니라 방 유형 단위로 맞춰, 한 도면 안 같은 유형의 정답 면적을 합친 비교점으로 정답 방 다각형 894개에서 비교 쌍 472개를 만든다. [사실][^ref-1668] 픽셀 세기 기준선의 평균 절대 백분율 오차(Mean Absolute Percentage Error, MAPE)는 같은 논문 안에서 평가 단위 서술이 어긋난다. 초록은 5.68%를 방 개체 단위, 1.58%를 도면 단위 값으로 적지만, §4.1과 표 2는 5.68%를 방 유형별 도면 단위 비교 472쌍 전체의 값으로 보고한다. [사실][^ref-1668] 이 위키는 어느 쪽이 맞는지 판단하지 않으며, 두 값을 성능 근거로 쓰지 않고 11절의 새 질문으로 남긴다.
- Chang 외, Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams(IROS 2023, arXiv v1 2023-04-26) — 각 로봇의 장면 그래프 전체를 제어 스테이션으로 주기적으로 보내고 로봇 쪽에서 삭제된 노드·엣지는 중앙 그래프에서도 지우며, 변경분만 보내거나 통신 단절 복구를 보장하는 방식의 근거는 아니다. [사실][^ref-1674] 평가는 uHumans2 시뮬레이션, 손에 든 장치로 따로 기록한 두 시퀀스를 두 로봇으로 취급한 SidPac, 실물 Jackal 2대로 기록한 Simmons 데이터로 이뤄지므로, 재생 시퀀스 수를 동시에 운용한 로봇 대수로 세면 안 된다. [사실][^ref-1674]
- Zhang 외, BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization(arXiv v1 2026-06-12, IJRR 2026 온라인 게재, 게재판 본문은 미열람) — 공사장 실험은 Ouster OS0-128로 기록한 시퀀스 7개와 Livox Mid-360으로 기록한 시퀀스 2개, 모두 9개 시퀀스로 이뤄지며 정답 궤적 없이 대리 지표로 평가했다(6절 요약, 연계 대상: 로봇 자체 위치 추정). [사실][^ref-1670]

기존 항목에 붙는 조건:

- AAS-RAIL(Groß·Heidrich, 2026-09) — 51.8%→71.7%는 고정 슬롯 값 예측 조건(속성 검출 미평가)의 정확도이고, 56.2%는 모호성을 무시한 낙관적 정규식 기준이며 이름·값이 함께 있는 경우는 13.4%다(6절 갱신 참고). [사실][^ref-1071]
- Robinson 외(2026-06) — 카메라 30대는 연구팀이 설치한 맞춤 카메라이며, 로봇만 있는 시험 구역에서 45분 동안 지점 간 임무 76건과 사람 개입 4회가 보고됐다(5절 물류창고 사례). [사실][^ref-1065]
- Strader 외(arXiv v2 2025-07-10, 게재처 미확인) — 종단 간 실물 실험은 Husky·Spot 2대, 장면 그래프 융합 절제 실험은 Kimera-Multi 데이터셋 로봇 3대 기록이며, 재위치 성공률은 Husky 64%·Spot 65%(5 m·10도, 의사 정답 기준)다(5절 실외 사례). [사실][^ref-1070]
- Dussard·Sarthou(arXiv 2606.17073, 2026-06-10, 게재처 미확인) — Pepper의 ChestButton을 Bumper로 분류한 기능 의미 오류 사례를 보고했다(6절 갱신 참고). [사실][^ref-239]

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

[^ref-1065]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-10-12
[^ref-1070]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-10-12
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-10-12
[^ref-1667]: Phung, H., & Averbuch-Elor, H. (Cornell University, arXiv; SIGGRAPH 2026), Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction, 2026-08-07, https://arxiv.org/abs/2602.09016v3, 접근일 2026-10-12
[^ref-1668]: Aliyev, N., & Barsi, Á. (Periodica Polytechnica Civil Engineering), Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images, 2026-08-05, https://pp.bme.hu/ci/article/view/44138, 접근일 2026-10-12
[^ref-1670]: Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research), BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization, 2026-06-12, https://arxiv.org/abs/2606.14237v1, 접근일 2026-10-12
[^ref-1674]: Chang, Y., Hughes, N., Ray, A., & Carlone, L. (MIT SPARK, arXiv; IROS 2023), Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams, 2023-04-26, https://arxiv.org/abs/2304.13487v1, 접근일 2026-10-12
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-07 | 45. 문서·도면·장면 이해 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-12-07/pages/topics/2026/2026-10-12-area45-s11.md

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
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1065, ref-1069, ref-1071, ref-1073, ref-1667, ref-1668, ref-1671, ref-1672, ref-1673, ref-1674, ref-1676, ref-239, ref-308]
last_run: 2026-10-12
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


### 2026-10-12 갱신: 부분 근거와 새 질문

분리 주제 페이지 [45. 문서·도면·장면 이해 — 열린 질문](2026-09-30-area45-s11.md)의 질문에 이번 실행이 더한 부분 근거와 새 질문이다. 기존 질문의 상태는 바꾸지 않았다.

- **oq-147** (상태: 조사 중) 부분 근거: LangExtract는 원문 위치를 찾지 못한 추출의 char_interval을 None으로 둔다. [사실][^ref-1671] Docling Core의 ProvenanceItem은 쪽 번호·영역 상자·문자 구간을 필수로 가진다. [사실][^ref-1672] 로봇 문서 전용의 확정·반려 구현은 여전히 확인하지 못했다.
- **oq-196** (상태: 열림) 부분 근거: 보고된 도면 인식 점수의 조건으로 AECV-Bench의 래스터 PNG 입력과 미평가 객체 [사실][^ref-1073], Raster2Seq의 IoU 0.5·10픽셀·5도 기준과 256×256 해상도 [사실][^ref-1667], Aliyev·Barsi의 주거 평면도 100장과 유효 출력 제외를 확인했다. [사실][^ref-1668] 비주거 시설 도면의 측정값은 여전히 없다.
- **oq-225** (상태: 열림) 부분 근거: 한국 공공부문 문서 849개로 구성했다는 KDoc-OCRBench-V2가 공개돼 있다(벤더 주장). [추정][^ref-1673] 로봇 매뉴얼 전용 한국어 평가는 확인하지 못했다.
- **oq-226** (상태: 열림) 부분 근거: AAS-RAIL은 고정 슬롯 평가 조건이며 56.2%·13.4%의 산출 조건이 따로 있다. [사실][^ref-1071] URDF 온톨로지 채우기에서는 ChestButton을 Bumper로 분류한 기능 의미 오류가 보고됐다. [사실][^ref-239] 로봇 매뉴얼 대상 추출 벤치마크는 여전히 확인하지 못했다.
- **oq-227** (상태: 열림) 부분 근거: 공장 배치는 1 Hz 위치 추정을 모터 오도메트리와 융합한다. [사실][^ref-308] RGB 영상 기반 장면 그래프 연구는 첫 영상 자세로 전역 좌표를 맞추고 임계값을 데이터셋마다 조정했다. [사실][^ref-1069] SLAM 챌린지 데이터는 정답 장치를 PPS 신호로 하드웨어 동기화한다고 설명한다(벤더 주장). [추정][^ref-1676] 허용 시간 차와 좌표 정합 기준 수치는 여전히 없다.

새 질문(번호는 [열린 질문](../../open-questions.md) 목록에서 부여한다):

- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-07) 출처 충돌: Aliyev·Barsi(2026)의 픽셀 세기 기준선 MAPE 5.68%·1.58%는 초록(방 개체 단위·도면 단위)과 §4.1·표 2(방 유형별 도면 단위 비교 472쌍)가 평가 단위를 다르게 적는데, 어느 쪽이 맞으며 재현 가능한 출력이 공개됐는가? [^ref-1668]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-07) 도면 인식 벤치마크의 픽셀 기준 점수(방 IoU 0.5, 모서리 10픽셀·5도)를 실제 문 통과 폭·충전기 접근 가능성 같은 미터 단위 주행 조건으로 검증한 평가나 사례가 있는가? [^ref-1667]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-07) 여러 제조사 로봇이 장면 그래프를 공유할 때 주기적 전체 전송 대신 변경분 전송, 통신 단절 뒤 재접속, 삭제 충돌 처리를 시험해 허용 기준을 보고한 사례나 공개 구현이 있는가? [^ref-1674]
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-07) 시설 카메라망 기반 다중 로봇 제어를 사람이 함께 다니는 구역이나 장시간 운용에서 시험해 시간당 사람 개입 수와 인식 원인 정지를 보고한 사례가 있는가? [^ref-1065]

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

[^ref-1065]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-10-12
[^ref-1069]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-10-12
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-10-12
[^ref-1073]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-10-12
[^ref-1667]: Phung, H., & Averbuch-Elor, H. (Cornell University, arXiv; SIGGRAPH 2026), Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction, 2026-08-07, https://arxiv.org/abs/2602.09016v3, 접근일 2026-10-12
[^ref-1668]: Aliyev, N., & Barsi, Á. (Periodica Polytechnica Civil Engineering), Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images, 2026-08-05, https://pp.bme.hu/ci/article/view/44138, 접근일 2026-10-12
[^ref-1671]: Google (google/langextract), LangExtract — langextract/core/data.py (Extraction 자료형, commit 74df59f), 미확인, https://github.com/google/langextract/blob/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py, 접근일 2026-10-12
[^ref-1672]: Docling Project (docling-project/docling-core), docling-core — docling_core/types/doc/common/reference.py (ProvenanceItem, commit 0d5a7bd), 미확인, https://github.com/docling-project/docling-core/blob/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py, 접근일 2026-10-12
[^ref-1673]: ONTHEIT (ONTHEIT-AI/BizOnAI-OCR), KDoc-OCRBench-V2 (Korean Document OCR Benchmark v2) — README (commit cdfc6d0), 미확인, https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md, 접근일 2026-10-12
[^ref-1674]: Chang, Y., Hughes, N., Ray, A., & Carlone, L. (MIT SPARK, arXiv; IROS 2023), Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams, 2023-04-26, https://arxiv.org/abs/2304.13487v1, 접근일 2026-10-12
[^ref-1676]: Hilti Research · Trimble · Oxford DRS (Hilti-Research/hilti-trimble-slam-challenge-2026), Hilti × Trimble 360 Visual-Inertial SLAM Challenge 2026 — README (commit e0c9277), 미확인, https://github.com/Hilti-Research/hilti-trimble-slam-challenge-2026/blob/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md, 접근일 2026-10-12
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-10-12
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-07 | 45. 문서·도면·장면 이해 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-07/pages/topics/2026/2026-10-12-area45-s7.md

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
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1012, ref-1669, ref-1671, ref-1672, ref-1673, ref-1674, ref-1675]
last_run: 2026-10-12
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


### 2026-10-12 갱신: 근거 위치 자료형·장면 그래프 파일·한국어 OCR·좌표 변환

분리 주제 페이지 [45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스](2026-09-30-area45-s7.md)의 표에 더하는 항목이다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| LangExtract Extraction 자료형(고정 커밋 74df59f) | 오픈소스 | 추출 텍스트를 원문에서 찾지 못하면 원문 문자 구간(char_interval)이 None이 되므로, 원문 위치가 없는 추출이 생길 수 있다 [사실][^ref-1671] | [^ref-1671] |
| Docling Core ProvenanceItem(고정 커밋 0d5a7bd) | 오픈소스 | PDF·HTML·docx·pptx에서 추출한 요소가 원문을 가리키는 근거 항목이며 쪽 번호·영역 상자·문자 구간 세 필드가 모두 필수다. 추출 내용의 의미 정확성까지 보장하지는 않는다 [사실][^ref-1672] | [^ref-1672] |
| Spark-DSG(MIT-SPARK, 고정 커밋 3c40997) | 오픈소스 | Python 예제가 JSON 장면 그래프 파일을 DynamicSceneGraph.load로 불러와 객체·장소·방 등 층과 노드에 접근하는 API를 보여 준다. 같은 연구실 구현의 API이며 다중 제조사 교환 표준은 아니다 [사실][^ref-1675] | [^ref-1675] |
| KDoc-OCRBench-V2(ONTHEIT) | 평가 프로그램 | 한국어 문서 광학 문자 인식(Optical Character Recognition, OCR) 벤치마크로, 한국 공공부문 단일 쪽 PDF 849개와 검증된 시험 56,197건(문장 존재 6,290·표 셀 49,115·머리말/꼬리말 792)으로 구성하고 실버 라벨 뒤 수동 검토했다고 설명한다. 문서 유형에 공공 매뉴얼(216개)은 있으나 로봇 매뉴얼은 따로 없다(벤더 주장, 외부 재현 없음) [추정][^ref-1673] | [^ref-1673] |
| IFC 4.3 IfcMapConversion(buildingSMART, 개발 브랜치 ifc4.3-main 원본) | 표준 | 국지 공학 좌표를 지도 좌표로 옮기는 변환을 기술하며 지리 좌표계에서 지도로의 투영은 다루지 않는다. 게시판 IFC 4.3 판의 절 번호와 문구 일치는 확인하지 않았다 [사실][^ref-1669] | [^ref-1669] |

국내 도면 데이터 쪽에서는 AI Hub 「건축 도면 데이터」의 건축 개요 데이터 속성표가 14개 속성을 모두 필수로 두며, 그 가운데 설계단계(design_stage, 계획·실시)와 축척(scale)이 있다. [사실][^ref-1012] 이 데이터는 1.0판이 2023-07-26, 1.1판이 2023-12-15에 개방됐고 1.1판이 최종 개방이다. [사실][^ref-1012]

구축자 의견으로는, Spark-DSG의 그래프 파일 API는 교환 어댑터의 출발점으로 쓸 수 있지만 다른 제조사 장면 그래프와의 단위·좌표계·객체 식별자·삭제 표시 의미는 별도 계약으로 정해야 한다. [의견][^ref-1675] 같은 의견으로, 8절의 Hydra-Multi가 쓰는 주기적 전체 전송을 플릿 통신 설계의 근거로 그대로 옮기지 말고 전송량·삭제 전파·초기 좌표 정합을 인수 시험에서 따로 재야 한다. [의견][^ref-1674][^ref-1675]

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

[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 2023-07-26, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-10-12
[^ref-1669]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcMapConversion (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 HTML과 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md, 접근일 2026-10-12
[^ref-1671]: Google (google/langextract), LangExtract — langextract/core/data.py (Extraction 자료형, commit 74df59f), 미확인, https://github.com/google/langextract/blob/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py, 접근일 2026-10-12
[^ref-1672]: Docling Project (docling-project/docling-core), docling-core — docling_core/types/doc/common/reference.py (ProvenanceItem, commit 0d5a7bd), 미확인, https://github.com/docling-project/docling-core/blob/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py, 접근일 2026-10-12
[^ref-1673]: ONTHEIT (ONTHEIT-AI/BizOnAI-OCR), KDoc-OCRBench-V2 (Korean Document OCR Benchmark v2) — README (commit cdfc6d0), 미확인, https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md, 접근일 2026-10-12
[^ref-1674]: Chang, Y., Hughes, N., Ray, A., & Carlone, L. (MIT SPARK, arXiv; IROS 2023), Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams, 2023-04-26, https://arxiv.org/abs/2304.13487v1, 접근일 2026-10-12
[^ref-1675]: MIT-SPARK (MIT-SPARK/Spark-DSG), Spark-DSG — examples/python_api.py (commit 3c40997), 미확인, https://github.com/MIT-SPARK/Spark-DSG/blob/3c40997e4ae739c56ed3cdd6ef5e882d403d8b64/examples/python_api.py, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-07 | 45. 문서·도면·장면 이해 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-07/pages/topics/2026/2026-10-12-area45-s10.md

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
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1669, ref-1670, ref-1676]
last_run: 2026-10-12
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


### 2026-10-12 갱신: 추가 연결

- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — 6절의 BIM 좌표 변환(IfcMapConversion)과 현장 정합(BIM-Loc, Hilti × Trimble 챌린지 데이터)은 이 영역에 요약만 두고 주 서술은 14. 도면·BIM에서 지도 만들기에서 한다. 구축자 의견으로는, ROP 지도 인계 기록에 좌표 변환 메타데이터 검사·실측 정합 검사·주행 가능성 검사 결과를 따로 두고, 도면 판(완공 의도 상태인지)·촬영일·센서 시간 보정 방식·정합에 쓴 정답 종류를 함께 남겨야 한다. [의견][^ref-1669][^ref-1670][^ref-1676] 7절의 AI Hub 건축 개요 메타데이터(설계단계·축척)도 이쪽 반영을 검토할 대상이다.
- [건축 도면 자동 인식 트랙](../../tracks/floorplan-recognition/index.md) — 이번 갱신의 도면 인식 점수 조건과 BIM 좌표·정합 요약은 트랙의 [단계 2 페이지](../../tracks/floorplan-recognition/stage-2-data-and-standards.md)와 [단계 4 페이지](../../tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md)에 연결한다.
- [매뉴얼 기반 로봇 기능 온톨로지 트랙](../../tracks/manual-capability-ontology/index.md) — 6절의 AAS-RAIL 평가 조건, URDF 기능 의미 오류, 근거 위치 자료형(LangExtract·Docling)은 추출 방법을 다루는 [단계 3 페이지](../../tracks/manual-capability-ontology/stage-3-extraction-methods.md)에 연결한다.
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 8절 Hydra-Multi의 장면 그래프 공유 방식과 7절 Spark-DSG 그래프 파일 API는 장면 그래프를 장소 의미 지도로 관리하는 문제와 이어진다.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 고정 카메라와 로봇 관측 융합의 관측 주기·동기화·좌표 기준 조건과 장면 그래프의 삭제 전파는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 입력 조건이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 구분한다.
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 카메라망 기반 다중 로봇 제어의 사람 개입 수를 장시간·사람 혼재 조건에서 재는 시험은 11절 새 질문으로 남겼다.

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

[^ref-1669]: buildingSMART (IFC4.3.x-development GitHub), IFC 4.3 — IfcMapConversion (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 HTML과 문구가 다를 수 있음), 미확인, https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md, 접근일 2026-10-12
[^ref-1670]: Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research), BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization, 2026-06-12, https://arxiv.org/abs/2606.14237v1, 접근일 2026-10-12
[^ref-1676]: Hilti Research · Trimble · Oxford DRS (Hilti-Research/hilti-trimble-slam-challenge-2026), Hilti × Trimble 360 Visual-Inertial SLAM Challenge 2026 — README (commit e0c9277), 미확인, https://github.com/Hilti-Research/hilti-trimble-slam-challenge-2026/blob/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-07 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-07 | 45. 문서·도면·장면 이해 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1538건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | https://arxiv.org/abs/1904.01920 | 2026-09-25 | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | https://arxiv.org/abs/2105.07147 | 2026-09-25 | 아니오 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06 | https://arxiv.org/abs/2606.17073 | 2026-09-25 | 아니오 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | https://arxiv.org/abs/2512.15215 | 2026-09-25 | 아니오 |
| ref-513 | OpenDataLab (opendatalab/OmniDocBench GitHub) | OmniDocBench — README | 미확인 | https://github.com/opendatalab/OmniDocBench | 2026-09-25 | 예 |
| ref-1012 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 2023-07-26 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 2026-09-30 | 예 |
| ref-1065 | Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv) | Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse | 2026-06-04 | https://arxiv.org/abs/2606.06762 | 2026-09-30 | 예 |
| ref-1066 | Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)) | A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans | 2022-03-25 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/ | 2026-09-30 | 예 |
| ref-1067 | Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv) | OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations | 2025-03-25 | https://arxiv.org/abs/2412.07626 | 2026-09-30 | 예 |
| ref-1068 | Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv) | Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion | 2025-01-27 | https://arxiv.org/abs/2501.17887 | 2026-09-30 | 예 |
| ref-1069 | Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv) | RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots | 2026-05-18 | https://arxiv.org/abs/2605.18197 | 2026-09-30 | 예 |
| ref-1070 | Strader, J., Ray, A., Arkin, J. 외 (arXiv) | Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs | 2025-07-10 | https://arxiv.org/abs/2506.07454 | 2026-09-30 | 예 |
| ref-1071 | Groß, J., & Heidrich, J. (arXiv) | AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning | 2026-09-07 | https://arxiv.org/abs/2609.07334 | 2026-09-30 | 예 |
| ref-1072 | Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv) | Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0 | 2024-06-24 | https://arxiv.org/abs/2403.17209 | 2026-09-30 | 예 |
| ref-1073 | Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv) | AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding | 2026-01-08 | https://arxiv.org/abs/2601.04819 | 2026-09-30 | 예 |
| ref-1074 | Google (google/langextract) | LangExtract — README | 미확인 | https://github.com/google/langextract | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 399개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
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
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-element-proxy: 건물 요소 프록시 (Building Element Proxy (IfcBuildingElementProxy))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- buildingsmart-data-dictionary: buildingSMART 데이터 사전 (buildingSMART Data Dictionary (bSDD))
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
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
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
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
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
- domain-shift: 도메인 이동 (Domain Shift)
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
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
- generalized-voronoi-graph: 일반화 보로노이 그래프 (Generalized Voronoi Graph (GVG))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- gln-extension-component: GLN 확장 성분 (GLN Extension Component)
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
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic-on-finite-traces: 유한 트레이스 선형 시간 논리 (Linear Temporal Logic on Finite Traces (LTLf))
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- makespan: 메이크스팬 (Makespan)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- minimum-cost-flow: 최소 비용 흐름 (Minimum-Cost Flow)
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
- mqtt-quality-of-service-level: MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- oauth2-client-credentials-grant: 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- original-instructions: 원본 설명서 (Original Instructions)
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
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- phased-rollout: 단계적 배포 (Phased Rollout (Staged Rollout))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
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
- remote-attestation: 원격 증명 (Remote Attestation)
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
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
- saga: 사가 (Saga)
- satisfiability-modulo-theories: 이론 모듈로 만족 가능성 (Satisfiability Modulo Theories (SMT))
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
- skos: 단순 지식 조직 체계 (Simple Knowledge Organization System (SKOS))
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
- state-script: 상태 스크립트 (State Script (Mender))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
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
- task-dependency-graph: 작업 의존 그래프 (Task Dependency Graph (Dependency DAG))
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- trace-context: 추적 문맥 (Trace Context (W3C traceparent / tracestate))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-defined-property-set: 사용자 정의 속성 세트 (User-defined Property Set)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050-hibernation: 절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-diagram: 워크플로 다이어그램 (Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안))
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [45] 에 걸린 13건 / 전체 411건)

```markdown
- oq-147 [조사 중] 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? (영역 4, 45, 7)
- oq-196 [열림] Raster-to-Vector 의 약 90% 정밀도·재현율 같은 보고된 평면도 인식 성능이 병원·공장·물류창고 같은 비주거 시설 도면에서도 확인됐는가? (영역 14, 45)
- oq-197 [해결] AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? (영역 14, 45)
- oq-225 [열림] OmniDocBench 같은 공개 문서 파싱 벤치마크에 한국어 문서가 없는데, 한국어 로봇 매뉴얼·설비 도면을 파싱·추출할 때의 정확도를 측정한 자료가 있는가? (영역 45, 4)
- oq-226 [열림] 일반 제품 데이터시트가 아니라 로봇 매뉴얼(능력·실행 조건·오류 코드)을 대상으로 LLM 추출 정확도를 측정한 공개 벤치마크나 연구가 있는가? (영역 45, 5)
- oq-227 [열림] 하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가? (영역 45, 18)
- oq-228 [열림] 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? (영역 45, 53)
- oq-299 [열림] 비전 언어 모델의 평면도 해석이 큰 개방 구역에서 성능이 떨어진다는 보고가 물류창고·제조 공장처럼 넓은 개방 구역이 많은 비주거 시설 도면에서 어떤 오류로 나타나는가? (영역 14, 45, 61)
- oq-317 [열림] 실외 배달로봇에 승인된 원본 영상 AI 학습 실증특례가 병원·물류창고 같은 실내 현장의 로봇 카메라 영상에도 적용될 수 있는가, 적용 조건은 무엇인가? (영역 53, 45)
- oq-341 [열림] 국내 공공 AI 학습 데이터(AI Hub 등)나 연구 과제에 물류센터·공장·병원 같은 비주거 건축 도면을 랙·도크·승강기·충전 구역 라벨과 함께 담은 데이터셋이 있거나 구축 계획이 있는가? (관련 기존 질문: oq-197, 트랙 질문 q2-04) (영역 14, 45)
- oq-342 [열림] 출처 충돌: FloorPlanCAD 의 범주 수는 30개(arXiv 초록)인가 35개(프로젝트 페이지)인가? (영역 14, 45)
- oq-343 [열림] 출처 충돌: ArchCAD-400K 의 의미 범주에 엘리베이터가 있는가(앞선 실행의 검색 요약과 v3 본문 열람 결과가 다르다)? (영역 14, 45)
- oq-346 [열림] CubiCasa5K 원 SVG 주석에는 계단(Stairs)·계단실(StairWell)·엘리베이터(Elevator) 범주가 실제로 몇 개 들어 있으며, 공식 학습 매핑이 이를 일반 방으로 합치거나 빼는 상태에서 기존 위키의 'CubiCasa5K 계단 라벨 있음' 서술은 원 주석 범주 기준으로 고쳐 써야 하는가? (영역 14, 45)
```
