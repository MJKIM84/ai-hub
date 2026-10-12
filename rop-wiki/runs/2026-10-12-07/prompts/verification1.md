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
- 세부영역 반영 제안: 3건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
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

### data/area_reflection_proposals.json (대상 영역 45. 문서·도면·장면 이해 에 대한 트랙 반영 제안 3건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-10-09-21",
      "date": "2026-10-09",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 45,
      "section": "8. 대표 연구와 자료",
      "summary": "분류 원문 13장 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 도면 해석 모델의 도메인 이동 근거를 싣는다: 산업용 건물 도면 전이 실패와 수작업 주석 32장 재학습 효과(f4, 원문 미열람), 평면도 분석 연구의 도면 양식 의존·표준 지표 부재·공개 데이터셋 부족(f5, Pizarro 외 2022-01), VLM 평면도 해석의 큰 개방 구역 성능 저하(f6), 생성 과제의 교차 데이터셋 저하와 합성 사전학습(f7, 인식 과제에는 유추 근거), 물류 도면 대상 성능 측정값 부재 종합(f9, [추정]). 실행 2026-10-09-21.",
      "status": "제안"
    },
    {
      "run_id": "2026-10-09-23",
      "date": "2026-10-09",
      "track": "manual-capability-ontology",
      "stage": 2,
      "area_no": 45,
      "section": "8. 대표 연구와 자료",
      "summary": "근거 형태별 문서 이해 정확도(MMLongBench-Doc, GPT-4o 텍스트 46.3·표 50.0·이미지 44.1, 공개 모델·OCR 파이프라인의 차트·이미지 저하), 산업 문서 다중 모달 RAG(Riedler·Langer 2024), 데이터시트→자산관리셸 추출(Xia 외 2024 유효 생성률 62~79%, AAS-RAIL 30.4~52.4% 상대 개선), 매뉴얼 질의응답(Singh 외, UR5e 포함 86.66%)과 교차 언어 기술 질의응답(Agri-Query). 매뉴얼 해석은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에 적용되는 방법으로 연결(근거: 실행 2026-10-09-23 f1~f6·f25).",
      "status": "제안"
    },
    {
      "run_id": "2026-10-09-26",
      "date": "2026-10-09",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 45,
      "section": "8. 대표 연구와 자료",
      "summary": "교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 도면 해석 학습 데이터의 클래스 구성(공식 학습 매핑에서 엘리베이터·계단실이 일반 방으로 합쳐짐)과 이용 조건(비상업 라이선스, AI허브 원 이용정책)을 반영(f1, f4, f6, f7, f8, f10).",
      "status": "제안"
    }
  ]
}
```

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md (요약)

```markdown
# 44. 로봇 기반 모델·언어 모델 계획

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

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

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

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

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-12 · 버전: 3

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

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

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

### docs/categories/security-and-privacy/privacy-and-video-data.md (요약)

```markdown
# 53. 개인정보·영상 데이터

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md (요약)

```markdown
# 55. 현장 조사·설치·시운전

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 조사, 설치·설정, 교정, 시운전, 인수 시험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 설치·설정**: 로봇·충전기·네트워크·설비를 설치하고 설정하며, 반복되는 설치 절차를 자동화한다
- **교정**: 센서·좌표·지도를 현장에 맞게 교정한다
- **현장 시운전**: 연동과 작업을 현장에서 시험 운전하며 문제를 잡는다
- **현장 조사**: 설치 전에 현장 치수·네트워크·설비·동선을 조사한다
- **인수 시험**: 합의한 수용 기준으로 인수 여부를 판정한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 21번 영역 ‘온보딩·설정·현장 시운전’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [옛 분류원문]

> 옛 질문: 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

새 현장에 설치하고 시운전할 때 반복 작업을 얼마나 줄일 수 있는가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
```

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/commercial-facilities.md (요약)

```markdown
# 64. 상업 시설

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/outdoor.md (요약)

```markdown
# 66. 실외

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1523건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [45] 에 걸린 13건 / 전체 409건)

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

### runs/2026-10-12-06/research.md

```markdown
# 리서치 브리프 2026-10-12-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-06 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 46. 예측·학습 기반 최적화 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 물류창고 사례 74행 '아마존은 로봇 이동 효율을 10% 높였다고 주장' 이 원문의 미래형·지표 차이(이동 시간 대 배치 효율)를 반영하지 못함. 병원 사례가 초록 기준이라 평가 조건(층·기간·시뮬레이션)과 수치가 없음. 국내 학습 기반 배정 사례·연구가 없음(oq-224)
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area46-s6) — '학습 실패 시 고전 정책 복귀' 가 일반론이고, 대체 정책 호출·예측 가중치 조정의 평가 근거가 없음. 2026년 학습 기반 LMAPF(RL-RH-PP JAIR, SJRL)와 최신 고전 기준선(PUSH)의 조건 비교 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area46-s7) — POGEMA 행에 분포 밖 지도·통신 한계 없음, League of Robot Runners 행이 SILLM 저자의 2023 우승 해법 비교만 근거로 함(2026 시즌 평가 구성·결과 없음), SILLM 공식 구현 없음, ISO 13381-1 서지(발행일·소관 SC) 불완전
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area46-s8) — SILLM '최고 탐색 기반 기준선보다 16.0%' 가 지도별 예외(WPPL 우세 3개 지도)·계획 시간·훈련 비용 없이 실림, Garces 외 '구체 수치는 초록에 없다', SPO '학술지 게재 연도 미확인'
- 섹션 9. 책임 경계 — 158행 '수요 예측 경계는 아직 정하지 않았다'(oq-223), 배터리 SoC 물리 모델 추정과 학습 예측의 구분, WCS 통합 제어 발표와 학습 기반 배정의 구분 없음
- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area46-s4) — 예지 정비·충전 상태 항목이 인계 값의 종류(SoC 변화·이상 클래스·예지)를 구분하지 않음
- 섹션 11. 열린 질문(분리 2026-09-30-area46-s11) — oq-220~oq-224 가 id 없이 실려 있고 부분 근거가 없음. 정정 요청 없음(target.json corrections 비어 있음)

## 조사 질문

1. 학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
2. 학습 기반 지속형 MAPF 의 평균 개선율(SILLM 16.0% 등)은 지도·밀도·계획 예산·훈련 비용 조건에서 어떻게 달라지며, 최신 대회(LoRR 2026)와 고전 기준선(PUSH)은 어떤 조건으로 평가하는가? (섹션 6·7·8 겨냥)
3. oq-220 학습 기반 배정·경로 정책의 개선을 실제 운영 현장에서 제3자가 측정한 자료가 있는가, 시뮬레이션·혼합 현실·회사 주장은 각각 무엇을 보여 주는가? (섹션 5·8·11 겨냥)
4. oq-222 학습·예측 정책이 실패하거나 요청 분포가 바뀔 때 대체 정책 호출과 예측 가중치 조정은 어떻게 설계·평가되는가? (섹션 6·8·11 겨냥)
5. oq-221 배터리 잔량·이상 분류·예지 출력은 어떤 조건에서 나오며 플릿 일정에 어떤 값으로 인계되는가? (섹션 4·9·11 겨냥)
6. oq-223·oq-224 상위 수요예측과 ROP 작업 요청의 경계는 어떻게 나누며, 국내 학습 기반 배정 연구·산업 발표는 무엇을 보여 주는가? (섹션 5·9·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | POGEMA 벤치마크의 분포 밖(Out-of-Distribution) 지표는 학습에 쓴 지도와 장애물 구조가 다른 Cities-tiles 지도 묶음(Cities 지도를 잘라 고친 것)으로 계산한다. | ref-1056 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | POGEMA 저자는 한계로 에이전트 간 통신이 현재 환경에서 분리(disentangled)되어 있지 않다고 밝혀, 통신 지연·손실을 따로 평가하는 구조가 아니다. | ref-1056 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | League of Robot Runners 2026 공식 평가는 7개 지도에 걸친 12개 인스턴스로 이루어지고, 인스턴스별 로봇(에이전트) 수 범위는 50~10,000이며, 평가 서버는 GPU 인스턴스(AMD EPYC 7R13 32 vCPU·128 GiB·Nvidia A10G)와 CPU 인스턴스(같은 CPU 32 vCPU·64 GiB)로 나뉜다. | ref-1637 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | LoRR 2026 본선 최종 결과는 2026-09-02 공지로 발표됐다(2026-07-23 공지는 8월 7일 발표 예정이라 했고 2026-08-10 공지로 지연을 알림). Combined Track 1위는 Team No Man's Sky(Task Scheduling Track 1위·Line Honours 도 같은 팀)이고, 2026-05-26 AAMAS Prize(Combined Track)는 Team SmartPath 로 별도 집계다. 수상 표에는 팀별 알고리즘(학습 사용 여부) 분류가 없다. | ref-1637 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [의견] | 대회 순위는 팀별 최종 제출 코드에서 학습을 어디에 썼는지 확인하기 전에는 학습 대 고전 방법의 승률로 바꾸지 말고, 인용할 때 시즌·트랙·인스턴스 구성·CPU/GPU 조건을 함께 적는 것이 맞다고 본다. | ref-1637 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | SILLM 논문 Table III(대형 지도·에이전트 10,000, 8회 평균 처리량)에서 WPPL 이 SILLM 보다 높은 지도가 6개 중 3개(Sortation 44.28 대 43.98, Warehouse 42.83 대 42.24, Random-1 54.38 대 53.74)이고, SILLM 은 Paris(31.00 대 23.74)·Berlin(30.52 대 20.35)·Random-2(44.37 대 37.30)에서 높았다. 단계당 평균 계획 시간은 SILLM 0.349초, WPPL 4.143초였다. | ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [추정] | 초록의 '최고 탐색 기반 기준선 대비 16.0%'는 Table III 대형 지도 6종에서 WPPL 대비 지도별 처리량 비율을 평균한 값(재계산 약 16.05%)과 일치하므로, 모든 지도에서 16% 앞섰다는 뜻이 아니라 지도별 비율의 평균으로 읽는 것이 맞아 보인다. | ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | SILLM 공식 부록은 지도마다 SILLM 모델 훈련에 12시간 미만이 걸렸다고 적으며, 훈련 서버는 72 vCPU AMD EPYC 9754·RTX 4090D(24GB) 4장·메모리 240GB였다. | ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | SILLM 공식 저장소(DiligentPanda/Scalable-Imitation-Learning-for-LMAPF) README 는 Backward Dijkstra·정적 안내(Static Guidance)·동적 안내(Dynamic Guidance) 버전을 별도 브랜치(static_guidance, dynamic_guidance)로 관리하며, Backward Dijkstra 는 정적 안내 설정에서 map_weights_path 를 비운 것과 거의 같다고 설명한다. | ref-1638 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | 공식 저장소의 1-GPU 예시 설정 파일(…sortation_small_a600_s500_none_annotated_1gpu.yaml)은 max_dagger_iterations 를 100으로 두지만 논문은 모방 학습을 12회 반복했다고 적어, 공개 예시 설정과 논문 실험 설정은 같은 것이 아니다. | ref-1638, ref-199 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [의견] | 학습 기반 경로 방법의 평균 개선율을 인용할 때는 지도별 우열, 단계당 계획 시간, 지도별 훈련 비용, 공개 구현의 브랜치·설정 파일을 함께 적어야 하며, 10,000 에이전트 시뮬레이션을 실물 플릿 규모로 읽지 않는 것이 맞다고 본다. | ref-199, ref-1638 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [사실] | RL-RH-PP(강화학습 안내 롤링 호라이즌 우선순위 계획, JAIR 85, 2026-03-24 게재)의 기준선 비교는 서로 다른 시드의 보류(held-out) 평가 환경 16개 평균이며, 800단계 창고 시뮬레이션(Amazon 풀필먼트 모사·Symbotic 모사 지도)에서 모든 해법에 계획 단계당 CPU 1초를 주고 시간 초과 해에는 같은 수리 기법을 적용했다. | ref-1639 | 아니오 | medium | 2026-10-12 | — | — |
| f13 | [사실] | RL-RH-PP 논문 Table 3 의 Symbotic 모사 지도에서 에이전트당 처리량은 80대일 때 RH-PBS 20.83 이 RL-RH-PP 18.38 보다 높았고, 100대(15.38 대 14.04)·120대(11.31 대 1.76)에서는 RL-RH-PP 가 높았다. 같은 표의 WPPL 은 16.29·13.73·10.05 였다. | ref-1639 | 아니오 | medium | 2026-10-12 | — | — |
| f14 | [사실] | RL-RH-PP 는 에이전트 밀도마다 정책을 처음부터 따로 학습했고, 가장 긴 훈련(120대)은 RTX 6000 Ada GPU 한 장으로 약 4일 걸렸다. | ref-1639 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | LSMART 는 처리량과 함께, 계획 실패 때 대체(fail) 정책을 부른 횟수를 계획기 호출 횟수로 나눈 비율을 평가 지표로 쓴다. | ref-604 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | LSMART 의 대체 정책 비교에서는 지도와 계획 창 조건에 따라 LRGW 또는 PIBT 가 가장 높은 처리량을 냈으며, 한 대체 정책이 모든 조건에서 최선은 아니었다. | ref-604 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | 2026-08 프리프린트 PUSH(Path Updates over Staggered Horizons)의 비교 실험은 1,000단계 실행·단계당 1초 계획 예산·무작위 5회 평균으로, AMD Threadripper 3990X·192GB 메모리 장비에서 수행했다. | ref-1640 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | PUSH 비교에서 RHCR 를 뺀 알고리즘은 시간 초과 시 계획 못 한 에이전트가 직전 단계 경로를 따르고, RHCR 는 K단계마다 K초를 받되 시간 초과 시 K단계 동안 PIBT 로 실행한 뒤 RHCR 로 돌아간다. | ref-1640 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [의견] | PUSH 는 학습 요소가 없는 고전 탐색 알고리즘이므로 이 영역에서는 학습 정책을 평가할 때 맞춰야 할 고전 기준선의 예산·실패 처리 조건을 보여 주는 대조 사례로만 다루고, 학습 성과 근거로 쓰지 않는 것이 맞다고 본다. | ref-1640 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [사실] | SJRL(탐색 보조 에이전트–환경 공동 강화학습, 2026-08 프리프린트)은 지도마다 256대로 정책을 학습해 같은 지도에서 32~320대(32대 간격)로 평가하며, 일반화는 초기 상태·목표·에이전트 수에 대해 보고 지도 간 일반화는 다루지 않는다. 각 평가는 512단계다. | ref-1641 | 아니오 | medium | 2026-10-12 | — | — |
| f21 | [사실] | SJRL 의 물리 로봇 검증은 실물 로봇 8대와 가상 로봇 248대를 섞은 혼합 현실 창고 환경에서 이루어졌다. | ref-1641 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | SJRL 저자는 비교한 모방학습 방법들을 회전 동작을 포함한 LMAPF-R2 문제 모델에 맞게 고치는 일을 향후 과제로 남겨, 비교 방법들의 문제 모델이 같지 않다. | ref-1641 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [추정] | Amazon Robotics 의 DeepFleet 보고서(arXiv v3, 'Unpublished technical report')는 학습에서 제외한 7개 창고 층의 7일 자료에서 로봇 궤적을 60초 앞까지 반복 추론해 실제 궤적과 비교하는 오프라인 예측 평가를 보고한다. | ref-1053 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f24 | [추정] | DeepFleet 보고서 Table 2 에서 로봇 중심(RC) 모델의 혼잡 지연 오차(CDE)는 3.40%로 네 구조 가운데 가장 낮았다(RF 9.60%, GF 14.22%, IF 186.56%). 이는 예측한 혼잡 지연과 실제의 상대 오차이며 이동 시간 절감률이 아니다. | ref-1053 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f25 | [추정] | Amazon 의 DeepFleet 10% 수치는 표현이 엇갈린다: About Amazon 발표(2025-07-01)는 핵심 요약에서 '이동 효율을 10% 높일 것(will improve)', 본문에서 '이동 시간을 10% 개선/줄여'라고 쓰고, Amazon Science 블로그(2025-08-11)는 '로봇 배치 효율을 10% 높이고 있다'고 쓴다. 비교 기간·대상 현장·분모는 공개하지 않아, 위키의 '이동 효율을 10% 높였다' 서술은 고쳐야 한다. | ref-916, ref-1054 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f26 | [의견] | 예측 정확도(궤적·혼잡 오차), 오프라인 결정 손실, 온라인 운영 개선은 서로 다른 승인 지표로 두고, 운영 개선 수치는 개입 시점과 비교 플릿을 확인한 뒤에만 성과로 반영하는 것이 맞다고 본다. | ref-1053, ref-916 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | Garces 외의 병원 배정 평가는 BIDMC 서관 입원 병동 4개 층(층당 병상 약 25~30)의 2024-06-24~2025-06-29 요청 이력에서 층마다 수요 높음·중간·낮음 주를 2주씩 골라 층당 42일, 정책당 168개 층-일을 하루 12시간(오전 6시~오후 6시) 시뮬레이션한 것이며, 나머지 이력은 학습·검증에 썼다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 시작 조건 | — |
| f28 | [사실] | Garces 외의 방법에서 예측 신뢰도 가중치는 표본 추출한 미래(예측) 요청에만 적용되고, 이미 관측된 요청과 예약 요청은 항상 가중치 1을 받는다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 제약 | — |
| f29 | [사실] | Garces 외 Table 3 의 수요 높음 조건(요청 36,948건)에서 제안 방법과 탐욕 배정을 포함한 대부분 정책의 거절 건수는 0이었고, Token Passing 과 Token Passing with Task Swaps 만 28건을 거절했다. 저자는 처리 건수만으로는 강한 정책들을 구분할 수 없어 대기 시간으로 비교했다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 예외·성과 | — |
| f30 | [사실] | Garces 외는 수요 높은 주에서 제안 방법이 일별 평균 대기 시간의 중앙값을 약 5%, 일별 95분위 대기 시간의 중앙값을 약 10% 줄였고, 두 지표의 75분위와 최댓값은 기준선 대비 15% 넘게 줄였다고 보고했다. 모든 수요 구간에서 가장 크고 일관된 개선은 95분위 대기 시간 지표에서 나왔다. | ref-1062 | 아니오 | medium | 2026-10-12 | 병원 / 예외·성과 | — |
| f31 | [의견] | 분포 이동에 대응해 예측 가중치를 낮추는 장치와, 계획 실패·시간 초과 때 고전 정책으로 돌아가는 트리거는 따로 설계·기록하고, 이미 시작한 작업과 아직 시작하지 않은 배정을 구분해 다루는 것이 맞다고 본다. | ref-1062, ref-604 | 아니오 | medium | 2026-10-12 | — | — |
| f32 | [사실] | Pookkuttath 외의 실시간 진동 분류 정확도 91%는 Snail 청소 로봇에서 모바일 앱의 요청(request-based) 표본 방식으로 모은 시험 표본 100개(Table 5)로 계산한 값이며, 클래스별 정확도는 88.7~93.5%였다. | ref-1057 | 아니오 | medium | 2026-10-12 | 기타 / 예외·성과 | — |
| f33 | [사실] | ISO 13381-1:2025 는 ISO/TC 108/SC 5 소관 제3판으로 2025-09-02 발행(단계 60.60)됐고 23쪽이다. | ref-1060 | 아니오 | medium | 2026-10-12 | — | — |
| f34 | [사실] | Open-RMF rmf_battery 의 SimpleMotionPowerSink 는 로봇이 궤적을 따라 가감속하는 데 드는 에너지로 배터리 충전 상태(SoC) 변화를 추정하고, SimpleDevicePowerSink 는 탑재 장치의 소비 전력으로 SoC 변화를 추정하는 물리 모델 API 이며 학습 모델이 아니다. | ref-1642 | 아니오 | medium | 2026-10-12 | — | — |
| f35 | [의견] | 배터리·고장 쪽 인계 값은 물리 모델의 SoC 변화 추정(Open-RMF rmf_battery, 28. 공용 자원·충전·에너지 최적화 맥락), 학습 모델의 현재 이상 클래스(진동 분류), 고장까지 남은 시간 같은 예지 출력을 서로 다른 값으로 구분해 넘기고, 이 영역은 학습·예측으로 얻은 값만 다루는 것이 경계로 맞다고 본다. | ref-1642, ref-1057, ref-1060 | 아니오 | medium | 2026-10-12 | — | — |
| f36 | [사실] | Open-RMF 작업 요청 스키마(task_request.json)의 fleet_name 은 플릿 이름 하나(문자열) 또는 이름 배열을 받을 수 있고, 지정하면 그 플릿(들)만 입찰한다. | ref-125 | 아니오 | medium | 2026-10-12 | — | — |
| f37 | [의견] | 상위 업무 시스템은 주문 전망과 시간 범위를 계획에 쓰고, ROP 는 실제로 들어온 요청을 플릿·능력·가장 이른 시작 시각 조건과 함께 받아 배정하는 것으로 책임을 나누며, 예측 요청을 확정 요청으로 자동 바꾸는 규칙은 별도 승인을 거치게 하는 것이 맞다고 본다. | ref-125, ref-1063, ref-1062 | 아니오 | medium | 2026-10-12 | — | — |
| f38 | [사실] | 강민교·김인철(한국로봇학회 논문지 18(2), 2023)의 제조 물류 작업 안전성·효율성 학습 실험은 NVIDIA Isaac 시뮬레이터 안 가상 제조 물류 환경에서 이동 로봇 2대로 수행됐고, 실제 하드웨어 로봇 적용·검증은 향후 연구로 남겼다. | ref-1643 | 아니오 | medium | 2026-10-12 | 제조 공장 / 수행 자원 | — |
| f39 | [사실] | 이 논문은 두 로봇의 정책 파라미터 등급이 같아 안전성·효율성 등급이 모두 같게 예측되는 드문 상태에서는 어느 로봇에 작업을 배정할지 판정하기 어렵다고 적고, 더 많은 정책 파라미터와 규칙이 필요하다고 본다. | ref-1643 | 아니오 | medium | 2026-10-12 | 제조 공장 / 예외·성과 | — |
| f40 | [추정] | 현대글로비스는 알티올과 공동 개발한 창고제어시스템(WCS) 플랫폼 오르카(ORCA)가 작업 계획을 실제 작업으로 바꾸고 각 설비의 상태와 우선순위에 따라 동선과 작업 순서를 실시간으로 조정하며, 어댑터 인터페이스로 다른 제조사 설비를 같은 방식으로 연결한다고 설명한다. 학습 모델이나 고전 방법 대비 성과는 밝히지 않았다. | ref-1644 | 아니오 | low | 2026-10-12 | 물류창고 / 수행 자원 | 벤더 주장 |
| f41 | [의견] | 오르카 같은 국내 통합 제어 발표는 학습 기반 배정·경로의 운영 효과 근거가 아니라 20. 로봇·제조사 관제 연동과 61. 물류창고 쪽 통합 운영 사례로 보고, 이 영역에서는 학습 요소가 확인되지 않은 경계 사례로만 다루는 것이 맞다고 본다. | ref-1644 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [사실] | Smart "Predict, then Optimize"(Elmachtoub·Grigas)는 Management Science 68권 1호 9–26쪽(2022-01)에 게재됐다. | ref-1061 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [추정] | 학습 기반 배정·경로 정책을 실제 운영 현장에서 탐색·규칙 기반 방법과 같은 조건으로 제3자가 측정한 자료는 이번에도 찾지 못했고, 확인한 근거는 시뮬레이션(SILLM·RL-RH-PP·Garces 외), 혼합 현실(SJRL 실물 8대+가상 248대), 회사 자체 주장(DeepFleet 10%)으로 나뉜다. | ref-199, ref-1639, ref-1062, ref-1641, ref-916 | 아니오 | low | 2026-10-12 | — | — |
| f44 | [의견] | 학습과 고전 방법의 우열은 지도·밀도·계획 예산·실패 처리(복귀 정책)를 같게 맞춘 조건에서만 판단하고, 한 논문의 평균 개선율을 다른 논문의 수치와 섞어 순위를 만들지 않는 것이 맞다고 본다. | ref-199, ref-1639, ref-1640, ref-604 | 아니오 | medium | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1056 | Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv) | POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding | 2025-04 | 논문 | high | 2026-10-12 | https://arxiv.org/abs/2407.14931 | 아니오 |
| ref-1637 | League of Robot Runners 조직위원회 (MAPF-Competition/web_resource, GitHub) | League of Robot Runners 2026 — Evaluation Process(evaluation.md)·Updates(updates.md)·Competition Rules(rules.md) | 미확인 | 오픈소스 문서 | medium | 2026-10-12 | https://github.com/MAPF-Competition/web_resource/tree/9d5e3378979561a55645cb737ca5e71bc91f020b | 아니오 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (ICRA 2025, arXiv) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10-28 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-1638 | He Jiang (DiligentPanda, GitHub) — SILLM 저자 공식 저장소 | Deploying Ten Thousand Robots: Scalable Imitaion Learning for Lifelong Multi-Agent Path Finding — README·예시 설정(Scalable-Imitation-Learning-for-LMAPF) | 미확인 | 오픈소스 문서 | medium | 2026-10-12 | https://github.com/DiligentPanda/Scalable-Imitation-Learning-for-LMAPF | 아니오 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2602.15721 | 아니오 |
| ref-1639 | Zheng, H., Ma, Y., Araki, B., Chen, J., & Wu, C. (MIT·Symbotic, Journal of Artificial Intelligence Research 85) | Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation | 2026-03-24 | 논문 | medium | 2026-10-12 | https://doi.org/10.1613/jair.1.20611 | 아니오 |
| ref-1640 | Sanjay, V., & Li, J. (arXiv) | Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF | 2026-08-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2608.06702 | 아니오 |
| ref-1641 | Jiang, H., Yan, J., Zhang, Y., Tang, Y., Duhan, T., Veerapaneni, R., Sartoretti, G., & Li, J. (arXiv) | Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations | 2026-08-06 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2608.05588 | 아니오 |
| ref-1053 | Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv) | DeepFleet: Multi-Agent Foundation Models for Mobile Robots | 2025-08 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2508.08574 | 아니오 |
| ref-916 | Amazon | Amazon launches a new AI foundation model to power its robotic fleet and deploys its 1 millionth robot | 2025-07-01 | 벤더 문서 | medium | 2026-10-12 | https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model | 아니오 |
| ref-1054 | Amazon Science | Amazon builds first foundation model for multirobot coordination | 2025-08-11 | 벤더 문서 | medium | 2026-10-12 | https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination | 아니오 |
| ref-1062 | Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv) | Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts | 2026-08-21 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2608.21554 | 아니오 |
| ref-1057 | Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors) | AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots | 2021-12-21 | 논문 | high | 2026-10-12 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/ | 아니오 |
| ref-1060 | ISO (ISO/TC 108/SC 5) | ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements | 2025-09-02 | 표준 | medium | 2026-10-12 | https://www.iso.org/standard/88029.html | 아니오 |
| ref-1642 | Open-RMF 유지관리자 (open-rmf, GitHub) | rmf_battery — README | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/open-rmf/rmf_battery/blob/b487ba597ca7796175ebc846e29c3c97142e50e2/README.md | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-1063 | CJ대한통운 | 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명 | 2021-07-28 | 벤더 문서 | medium | 2026-10-12 | https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238 | 아니오 |
| ref-1643 | 강민교, 김인철 (한국로봇학회 논문지 18(2)) | 다중 로봇 제조 물류 작업을 위한 안전성과 효율성 학습 (Safety and Efficiency Learning for Multi-Robot Manufacturing Logistics Tasks) | 2023-06 | 논문 | medium | 2026-10-12 | https://doi.org/10.7746/jkros.2023.18.2.225 | 아니오 |
| ref-1644 | 현대자동차그룹 (현대글로비스) | 현대글로비스가 그리는 자동화를 넘어선 물류의 미래 | 2026-04-16 | 벤더 문서 | medium | 2026-10-12 | https://www.hyundaimotorgroup.com/ko/story/hyundai-glovis-physical-ai-logistics | 아니오 |
| ref-1061 | Elmachtoub, A. N., & Grigas, P. (arXiv; Management Science 68(1)) | Smart "Predict, then Optimize" | 2017-10 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/1710.08005 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등, 정정 요청 없음): 섹션 4(분리 2026-09-30-area46-s4) — '예지와 예지 정비' 항목의 ISO 13381-1 서지를 2025-09-02 발행·제3판·ISO/TC 108/SC 5·23쪽으로 보강(f33, ref-1060 서지 보정). '충전 상태' 항목에 물리 모델 SoC 추정(rmf_battery, f34)과 학습 예측을 구분하는 경계 설명(f35)만 덧붙임(rmf_battery 는 28 맥락이며 학습 근거로 쓰지 않음) / 섹션 5 — 물류창고 사례: 74행 예외·성과 '아마존은 로봇 이동 효율을 10% 높였다고 주장' 을 f25 로 정정(발표 2025-07-01 요약은 미래형 'will improve', 본문 '이동 시간 10%', 블로그 2025-08-11 '배치 효율 10%', 비교 기간·분모 미공개, [추정] 벤더 주장 유지). DeepFleet 오프라인 예측 평가 조건(7개 층·7일·60초, f23)과 CDE 3.40%(f24)는 Amazon 자체 기술보고서라 [추정] 벤더 주장으로; 의견 f26. 기존 ref-1053 근거 [사실] 문장(모델 구성 서술)은 보고서 자체 내용 서술이라 유지하되 성능 수치는 [추정]으로 다룬다(기준 엇갈림 표시). 병원 사례: 표·본문에 평가 조건(BIDMC 4개 층·168 층-일·12시간, f27), 확정 요청 가중치 1(f28, 제약 칸), 거절 0건 동률(f29), 대기 시간 수치(f30, 예외·성과 칸 '꼬리 지연 개선이 가장 컸다' 를 수치로 보강). 제조 공장: 국내 연구 강민교·김인철(f38·f39)을 시뮬레이션 연구로만 추가(실제 배치 사례 아님). 오르카(f40)는 학습 요소가 확인되지 않은 통합 제어 발표라 사례가 아니라 경계 설명 한 문장으로(f41). 기타: 91% 가 시험 표본 100개 기준임(f32) / 섹션 6(분리 2026-09-30-area46-s6) — '학습 기반 경로·교통 관리' 에 RL-RH-PP(f12~f14)와 SJRL(f20~f22, SILLM 공동 저자라 독립 재현 아님) 추가, 실패·복귀 처리 소절에 LSMART 대체 정책 호출 비율(f15)·LRGW/PIBT 지도별 최고(f16), 고전 대조군 PUSH 의 예산·폴백 조건(f17·f18)은 대조 설명으로만(f19); 의견 f31·f44. 첫 문장 '같은 조건 비교에서는 탐색 기반 방법이 아직 앞서고' 는 f6·f13 처럼 지도·밀도별로 우열이 갈린다는 점으로 보강 / 섹션 7(분리 2026-09-30-area46-s7) — POGEMA 행에 분포 밖 평가 Cities-tiles(f1)·통신 미분리 한계(f2). League of Robot Runners 행: 기존 SILLM 2023 비교에 LoRR 2026 평가 구성(f3)과 최종 결과(f4)를 요약·연결만 추가(주 위치는 27·54·25 영역, 다음 실행 후보); 의견 f5. '기존 위키는 SILLM 비교만 소개' 류 서술은 쓰지 않음(기존 자료: ref-603 testing-formal-verification-and-benchmarking.md 115행, ref-191, ref-1306, standards/index.md 140·182행). SILLM 공식 구현 행 추가(f9·f10, 출처는 공식 DiligentPanda 저장소 ref-1638 — 메모의 wuwen-T 미러는 쓰지 않음). ISO 13381-1 행 서지 보정(f33) / 섹션 8(분리 2026-09-30-area46-s8) — SILLM 항목(대상 문장 '…최고 탐색 기반 기준선보다 16.0% 높았고…')은 삭제하지 않고 지도별 예외를 덧붙임: 대형 지도 6종 중 3종(Sortation·Warehouse·Random-1)에서 WPPL 이 높음과 단계당 0.349초 대 4.143초(f6), 16.0% 는 지도별 비율 평균으로 읽힌다는 해석은 [추정](f7), 지도별 훈련 12시간 미만·자원(f8); 의견 f11. Garces 외 항목의 '구체 수치는 초록에 없다' 를 본문 수치로 정정(f27~f30). SPO 항목 '학술지 게재 연도 미확인' → Management Science 68(1):9–26, 2022-01(f42). RL-RH-PP(f12~f14)·SJRL(f20~f22) 새 항목, PUSH(f17·f18)는 고전 대조 자료로 표시. Pookkuttath 항목 91% 표본 수(f32) / 섹션 9 — 상위 업무 시스템 행에 확정 요청 인계 경계(f36 fleet_name 문자열·배열, f37 의견), 로봇 자체 지능·제어 행에 SoC 물리 모델 추정은 28·제조사 쪽(f34·f35), 오르카 같은 WCS 통합 제어는 20·61 쪽 경계(f41). 158행 '경계는 아직 정하지 않았으며' 는 f37 의견으로 부분 보강하되 열린 질문 유지 / 섹션 11(분리 2026-09-30-area46-s11) — 해결 제안 없음. 부분 근거: oq-220(f43: 제3자 실측 없음, 근거 종류 구분), oq-221(f32·f33·f34·f35: 출력 종류만 확인, 공통 데이터 계약·모델 소유권 미확인), oq-222(f15·f16·f18·f28·f31: 가중치 조정과 대체 정책 호출은 확인, 공통 분포 이동 임계값 없음), oq-223(f36·f37: 의견 수준 경계), oq-224(f38·f39 국내 시뮬레이션 연구, f40 은 학습 성과 아님). 관련 근거: oq-058(f6·f13·f21, 벤치마크→실처리량 전이는 여전히 미확인). 분리 페이지 s11 의 질문 5개에 oq-220~oq-224 id 를 붙여 표기. 새 질문 3건 / 기존 내용 확인(새 finding 으로 넣지 않음): SILLM WPPL 비교의 회전 제거·LNS 40,000회 제한(메모 F09, 2026-10-10-area27-s8.md 42행), SILLM 실물 10대·가상 100대(s8 기존), LSMART 600초×10회·실패 정책 개념(2026-10-10-area27-s8.md 43행), CJ대한통운 iFlex 주문 유형별 수요 예측(메모 V05, 본문 5절 78행·9절 149행, ref-1063), DeepFleet 네 구조(s6·s8, ref-1053), Poskart 외 조정 결정계수 0.9629·0.9694·±0.1% 이내 약 50%·MiR100(s6·s8, ref-1058, 독립 검증 재확인), 현대차 5일·90%(5절, ref-1059 파이낸셜뉴스 — 1차 자료 미확인이라 [추정] 벤더 주장 유지), fleet_name 필드 자체(2026-09-29-area09-s7.md 40행) / 후속 정리 필요(대상 페이지 밖, 이번에 고치지 않음): docs/categories/ai-and-learning/index.md 107행 '로봇 이동 효율을 10% 높였다고 주장한다' 를 f25 로, 같은 행 Garces 요약에 f30 수치; docs/categories/site-type-applications/warehouse.md 107행 'Amazon 은 2025년 7월 발표(페이지에 발행일 표기 없음, 검색 결과 기준)' → 페이지 메타 2025-07-01 확인(ref-916); 다음 실행 후보: 27. 다중 로봇 경로·교통 관리 — MAPF·54. 시험·형식 검증·벤치마크·25. 작업 배정 — MRTA(f3·f4 LoRR 2026, f12~f22), 63. 병원·의료(f27~f30), 28. 공용 자원·충전·에너지 최적화(f34) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 학습 기반 배정·경로 정책과 고전 탐색 방법을 같은 실행 모델·지도·계획 예산·실패 처리(대체 정책) 조건으로 다시 돌려 학습의 순이득을 재현한 공개 자료가 있는가? (관련 기존 질문: oq-220, oq-058) | 관련 영역: 46. 예측·학습 기반 최적화, 54. 시험·형식 검증·벤치마크 | 근거: f44 | 종류: 일반
- 예측 요청의 가중치를 낮추는 것으로 충분한 경우와 실행 중인 계획을 중단·교체하거나 고전 정책으로 돌아가야 하는 경우를 누가 어떤 지표로 구분하는가? (관련 기존 질문: oq-222) | 관련 영역: 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 | 근거: f31 | 종류: 일반
- 배터리 SoC 변화 추정·현재 이상 클래스·고장 예지 출력을 플릿 일정에 넘길 때 값의 유효기간·불확실성·책임 주체를 어떻게 표현하는가? (관련 기존 질문: oq-221) | 관련 영역: 46. 예측·학습 기반 최적화, 28. 공용 자원·충전·에너지 최적화 | 근거: f35 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 20 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 8건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-06/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f7: SILLM 초록 16.0% 의 계산 방식은 논문에 명시되지 않아 Table III 지도별 비율 평균(재계산 16.05%)과 일치한다는 해석만 [추정]으로 둠
    - f3·f4: LoRR web_resource 고정 커밋(9d5e337)의 커밋 날짜와 최종 수상팀 제출 코드의 학습 사용 여부는 확인하지 못함(published null)
    - f9·f10: SILLM 공식 저장소 README·예시 YAML 만 읽었고 코드를 실행해 논문 결과를 재현하지 않음. dynamic_guidance 브랜치 내용은 보지 않음
    - f23·f24·f25: DeepFleet 은 Amazon 자체 기술보고서·회사 발표만 근거라 [추정] 벤더 주장. 10% 의 비교 기간·대상 층·분모·개입 대조와 제3자 확인은 없음
    - f36: fleet_name 배열 허용의 도입 버전(rmf_api_msgs 0.7.0, CHANGELOG 2026-09-18)은 독립 검증 결과를 따랐고 이번 변환에서 CHANGELOG 를 다시 열지 않음. 스키마 본문(main)은 확인
    - f42: SPO 학술지 서지는 Crossref 메타데이터로 확인했고 학술지 본문은 열지 않음
    - f33: ISO 13381-1:2025 규범 본문(유료)은 열지 않아 조항 내용과 위키 시사점의 직접 대응은 미확인
    - f40: 오르카에서 실제 학습되는 모델·정책과 그 성능 비교·운영 분모는 미공개. 현대차 예지정비 5일·90%(ref-1059)의 1차 자료도 확인하지 못함
    - oq-220~oq-224 는 모두 부분 근거만 얻어 해결 제안하지 않음. 국내 실물 창고·병원에서 학습 기반 배정·경로를 고전 방법과 대조 실측한 자료, 이종 플릿 고장 데이터 계약·모델 소유권 합의, 공통 분포 이동 복귀 임계값은 찾지 못함
- 범위 경계 위반 의심:
    - f3·f4·f5: LoRR 2026 대회 평가 구성·결과는 27. 다중 로봇 경로·교통 관리 — MAPF, 54. 시험·형식 검증·벤치마크, 25. 작업 배정 — MRTA 가 주 위치이므로 이 영역에는 요약·연결만 둠
    - f17·f18·f19(PUSH), f34(rmf_battery), f40·f41(오르카): 학습과 무관한 고전 알고리즘·물리 모델·통합 제어이므로 이 영역에서는 대조·경계 설명으로만 쓰고 학습 성과 근거로 쓰지 않음(각각 27, 28, 20·61 영역 맥락)
    - f36·f37: 작업 요청 스키마와 상위 수요예측 경계는 23. 업무 시스템 연동과 겹치며, 이 영역에는 예측 요청과 확정 요청의 인계 경계로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 8건/15(ref-1637~ref-1644, 예약 구간 ref-1637~ref-1666 안), 재사용 12건(ref-1056·ref-199·ref-604·ref-1053·ref-916·ref-1054·ref-1062·ref-1057·ref-1060·ref-125·ref-1063·ref-1061). 출처 매핑(독립 검증 결과 기준): 메모 n1→ref-1056, n2+n3→ref-1637(한 출처로 묶음, raw 경로), n4→ref-199, n5→ref-1638(메모의 wuwen-T 저장소는 미러라 공식 DiligentPanda/Scalable-Imitation-Learning-for-LMAPF 로 교체), n6→ref-604, n7→ref-1639(JAIR DOI 10.1613/jair.1.20611, 2026-03-24), n8→ref-1640, n9→ref-1641, n10→ref-1053, n11→ref-916(발행 2025-07-01), n12→ref-1062, n13→ref-1060(서지 보정), n14→ref-1057(Europe PMC 전문), n15→ref-1642, n16→ref-1063, n17→ref-1643, n18→ref-1644(벤더 문서), n19→ref-125. 추가 재사용: ref-1054(10% 표현 대조), ref-1061(SPO 게재 서지, Crossref). 검증 반영: F08 을 Warehouse 한 지도에서 6개 지도 중 3개(Sortation·Warehouse·Random-1) WPPL 우세로 확장하고 계획 시간 병기(f6), 16.0% 해석은 [추정](f7); F09(LNS 40,000회)는 2026-10-10-area27-s8 중복이라 제외; V01 은 JAIR 표 값이라 [사실]로 두고 N100·N120 의 RL-RH-PP 우세를 병기(f13); V02·V03 은 Amazon 자체 기술보고서라 [추정]·벤더 주장(f23·f24); V04 는 '높였다'가 아니라 미래형·지표 차이로 정정(f25); A11 Garces 를 본문 정량 결과로 정정(f27~f30); V05 는 기존 내용과 완전 중복이라 제외(ref-1063 은 의견 f37 참고로만); PUSH·rmf_battery·오르카는 학습과 무관해 대조·경계 설명으로만(f19·f35·f41); U16 SPO 게재 서지 확인(f42); U09 Poskart 수치는 재확인만 하고 새 finding 없음; U15 현대차 5일·90% 는 [추정] 유지. LoRR 2026(F03~F07)은 f3~f5 로 요약해 연결만. 교차 확인 0건: 모든 [사실] finding 이 단일 출처이거나 같은 연구팀·같은 회사 자료(SILLM 논문·저장소, SILLM·SJRL·LSMART 공동 저자, Amazon 발표·블로그·보고서)라 독립이 아님 — 신뢰도 medium 이하. 열린 질문: oq-220~oq-224 는 docs/open-questions.md 242~246행 문구와 분리 페이지 s11 질문이 같음을 확인. 해결 제안 없음, 부분 근거만. 메모의 새 질문 3건은 oq-220·oq-058, oq-222, oq-221 과 겹치는 부분이 있으나 같은 질문은 아니어서(재현 조건, 판단 주체, 유효기간·책임) 관련 기존 질문을 밝혀 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호와 고정 위키 커밋 행 번호는 쓰지 않고 원문 절·표와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음. finding 44건(사실 29, 추정 6, 의견 9).
```

### runs/2026-10-12-05/research.md

```markdown
# 리서치 브리프 2026-10-12-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-05 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 44. 로봇 기반 모델·언어 모델 계획 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 제조 공장 사례가 BMW 보도자료(ref-1051) 하나에 기대며, 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'가 Figure AI 발표(2025-11-19, 2026-06-30)의 존재와 맞지 않음. 10개월·11개월 문구의 출처 위치(CEO 인용·본문)와 Figure 쪽 기간 축, 99% 성공률이 목표치라는 구분이 없음. 연구 실물 사례(IMR-LLM 로봇 팔 3대)도 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area44-s6) — SMART-LLM·IMR-LLM 은 초록 수준 서술뿐이라 평가 규모(36 지시, 23장면·50작업)·실패 양상(불가능 과제, 도달 불가 배정)·풀이 방식(FIFO)이 없고, LLM+P·KnowNo 류 보장의 입력 전제(사람이 준 도메인, i.i.d., 무오류 실행)가 적혀 있지 않음. 다중 로봇 등각 예측 계획(S-ATLAS) 없음. disjunctive graph 번역어가 위키 안에서 셋으로 갈림
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area44-s7) — 'OpenVLA의 라이선스는 확인하지 못했다'(표 바로 아래)와 GR00T N1 '오픈소스(공개 모델)' 표기에 코드·가중치 라이선스 구분과 문서 간 충돌이 없음. VLA 배포물의 입출력 계약(정규화·행동 청크·개방 루프)과 GR00T N1.7 EA 상태, ROSA 의 물리 실행 조건이 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area44-s8) — 최근 로봇 기반 모델(π0.7)과 VLA 견고성 벤치마크(LIBERO-Plus)가 없고, 국내 동향이 2025-05 기사 하나뿐(산업부 M.AX 휴머노이드 과제 표 없음)
- 섹션 9. 책임 경계 — 도구 호출(MCP)로 로봇을 움직일 때 힌트·권한·승인·세션 종료·물리 정지의 관계가 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area44-s11) — oq-216~oq-219 모두 열림. 부분 근거(배포물별 입출력, 연구 벤치마크 규모, Figure 기간 축)가 연결돼 있지 않음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s7 OpenVLA 라이선스 문장, 5절 93행 Figure 자체 발표 문장

## 조사 질문

1. 범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
2. oq-217 언어 모델 기반 다중 로봇 계획기의 공개 평가는 어떤 규모·조건(시뮬레이션/실물, 로봇 수)이며 어떤 실패 양상(능력 밖 배정)을 보고하는가? (섹션 5·6 겨냥)
3. 기호 계획기 결합·등각 예측 기반 계획의 검증·보장은 어떤 입력 전제(도메인 제공자, 분포 가정, 스킬 실행 성공)에 기대는가? (섹션 6 겨냥)
4. oq-216 VLA 를 등록하려면 배포물마다 어떤 입출력(행동 공간·정규화·행동 청크·제어 모드)과 공개 상태(EA/GA)를 확인해야 하는가? (섹션 7·8 겨냥)
5. OpenVLA·GR00T N1.7·openpi 의 코드와 가중치 사용 조건은 각 문서에서 무엇이라 적혀 있고 서로 맞는가? (섹션 7 겨냥)
6. 언어 모델 도구 호출(MCP·ROSA)로 로봇을 움직일 때 권한·승인·세션 종료와 물리 정지는 어떻게 나뉘는가(oq-141 관련)? (섹션 7·9 겨냥)
7. oq-218·oq-219 BMW–Figure 와 국내 물류 실증 발표에서 목표·기간·첫 시연과 실측 성과는 어떻게 구분되는가? (섹션 5·8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | SMART-LLM 의 평가 데이터셋은 AI2-THOR 가정 시뮬레이션의 고수준 지시 36개로 구성되며, 과제마다 로봇 1~4대를 쓴다. | ref-090 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | SMART-LLM 의 불가능 과제 시험(어떤 로봇도 필요한 스킬을 갖지 않은 과제)에서 GPT-4·Claude-3 기반 구성은 배정 계획을 만들지 않았고, GPT-3.5·Llama2 기반 구성은 과제에 맞지 않는 로봇이 들어간 배정 계획을 만들었다. 이 시험은 표 I 집계에 들어 있지 않고 과제 수도 보고되지 않았다. | ref-090 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | IMR-Bench 는 생산 라인 설계 전문가가 실제 산업 현장에서 수집·각색한 장면 23개(장면당 로봇 1~7대)를 바탕으로 제조 작업 50개를 구성한 벤치마크이며, KunWu 플랫폼 위에 만들어졌다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | IMR-LLM 구현은 언어 모델이 구성을 도운 이접 그래프(disjunctive graph)의 일정을 휴리스틱 FIFO(선입선출) 알고리즘으로 푼다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | IMR-LLM 의 실물 시험은 컨베이어에 공작물을 옮기는 로봇 팔 3대의 단일 장면이었고, 전문가가 약 15분 걸려 장면 설명을 손으로 작성해 입력했다. 반복 횟수는 보고되지 않았다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | IMR-LLM 저자는 복잡한 다중 로봇 작업에서 성공률이 떨어진 주된 이유로 언어 모델의 잘못된 분해·배정(예: 팔이 닿지 않는 로봇에 작업 배정)을 들었으나, 그 빈도는 정량화하지 않았다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | LLM+P 는 행동의 전제·효과를 담은 PDDL 도메인 파일을 사람 전문가가 제공한다는 것을 입력 전제로 둔다. 언어 모델은 문제(problem) 파일만 만든다. | ref-092 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | S-ATLAS(등각 예측 기반 다중 로봇 언어 계획기)의 임무 성공률 보장은 보정(calibration) 시나리오와 시험 시나리오가 독립·동일분포(i.i.d.)라는 조건 아래에서만 성립한다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | S-ATLAS 의 임무 완료율 정리(Theorem IV.2(a))는 계획 실행에 오류가 없다는 전제를 두며, 증명은 예측 집합이 단일 원소가 아닐 때 사람이 정확한 도움을 준다는 것도 전제한다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | S-ATLAS 는 AI2-THOR 시뮬레이션의 검증 시나리오 110개로 평가했고 로봇 수는 1·3·10·15대였다. 열람한 본문에서 실물 로봇 실험은 확인되지 않았다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | OpenVLA 모델 카드에 따르면 OpenVLA 는 언어 지시와 카메라 영상 한 장을 입력받아 정규화된 7자유도 엔드이펙터 변위(x, y, z, roll, pitch, yaw, gripper)를 출력하며, 실제 로봇에서 실행하려면 로봇·데이터셋별로 계산한 통계로 역정규화해야 한다. | ref-1609 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [사실] | OpenVLA 공식 저장소(고정 커밋 c8f03f4)의 코드 라이선스는 MIT 다. | ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f13 | [사실] | 같은 OpenVLA README 는 사전학습 모델이 기반 모델의 제약을 물려받을 수 있으며, 두 모델이 Llama 2 에서 파생됐으므로 Llama Community License 가 적용될 수 있다고 적는다. | ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f14 | [사실] | OpenVLA 의 Hugging Face 모델 카드는 "모든 OpenVLA 체크포인트와 학습 코드가 MIT 라이선스로 공개된다"고 적어, 저장소 README 의 Llama Community License 적용 가능 문구와 충돌한다. 현재 main 판(커밋 47a0ec7, 2026-02-17)도 같은 문구이며, 두 문서는 같은 개발팀 자료라 어느 쪽이 맞는지는 문서만으로 정할 수 없다. | ref-1609, ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | openpi 원격 추론 예시는 정책 서버가 (action_horizon, action_dim) 형태의 행동 청크(action chunk)를 돌려준다고 설명한다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | 같은 openpi 예시는 다음 추론 호출 전까지 예측된 행동 청크의 나머지 행동을 개방 루프(open-loop)로 실행하도록 안내한다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | openpi README(커밋 215abfb)가 제공하는 기반 체크포인트는 π0, π0-FAST, π0.5 뿐이며, π0.7 가중치는 목록에 없다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | NVIDIA Isaac GR00T 저장소의 n1.7-release README 는 GR00T N1.7 을 Early Access(EA) 릴리스로 명시하고, GA(정식) 릴리스 전까지 지원·안정성 보장이 제한되며 상용 지원을 포함한 운영 배치는 GA 대상이라고 적는다. | ref-1611 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [사실] | 같은 GR00T README 의 License 절은 코드는 Apache 2.0, 모델 가중치는 NVIDIA Open Model License 로 구분한다. | ref-1611 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [추정] | GR00T README 소개 문단은 "GR00T N1.7 은 Apache 2.0 으로 완전히 상용 라이선스가 가능하다"고 적지만, 이는 같은 README 의 License 절(가중치는 별도 라이선스)·가중치 저장소 LICENSE(3.3절 비상업 한정)와 맞지 않는 벤더 소개 문구다. | ref-1611, ref-1612 | 아니오 | low | 2026-10-12 | — | — |
| f21 | [사실] | Hugging Face nvidia/GR00T-N1.7-3B 저장소의 LICENSE 파일(커밋 6949d5d, 현재 main 과 같음)은 'NVIDIA License' 표제 아래 3.3절에서 저작물과 파생물을 연구·평가 목적의 비상업 용도로만 쓸 수 있게 하고, NVIDIA 와 그 계열사는 상업적으로 쓸 수 있다는 예외를 둔다. | ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | GR00T N1.7 가중치의 사용 조건은 세 문서가 서로 다르게 적는다: README 소개(Apache 2.0 으로 상용 가능), README License 절과 3B 모델 카드(NVIDIA Open Model License, 카드는 '상업·비상업 사용 준비'), 3B 저장소 LICENSE 파일(NVIDIA License 3.3절 비상업 한정). 어느 문서가 우선하는지는 문서에 적혀 있지 않다. | ref-1611, ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [추정] | Physical Intelligence 의 π0.7 기술 보고서는 관절(joint)·엔드이펙터(ee) 행동을 함께 학습하고 프롬프트의 텍스트 식별자 c∈{joint, ee} 로 실행 제어 모드를 지정해 실행 시 과제에 따라 고른다고 설명한다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f24 | [추정] | π0.7 보고서는 추론 지연에 대비해 학습 중 0~12 타임스텝의 지연을 모사했고, 이는 50 Hz 로봇에서 최대 240 ms 에 해당한다고 적는다. 이는 학습 조건이며 측정된 추론 지연이 아니고, 보고서의 UR5e 로봇은 20 Hz 로 동작한다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f25 | [추정] | π0.7 저자들은 학습 데이터가 매우 커서 평가 과제가 학습 때 본(seen) 과제인지 처음 보는(unseen) 과제인지 확정하기 어렵다고 스스로 밝힌다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f26 | [사실] | LIBERO-Plus 는 LIBERO 시뮬레이션 조작 과제에서 물체 배치, 카메라 시점, 로봇 초기 상태, 언어 지시, 조명, 배경 질감, 센서 잡음의 7개 축으로 입력을 하나씩 교란해 VLA 모델의 견고성을 평가한다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | LIBERO-Plus 에서 OpenVLA-OFT 의 성공률은 교란 없는 원본 97.1% 에서 로봇 초기 상태 교란 시 크게 떨어진다. 수치는 판마다 다르다: arXiv v3 표 1 은 로봇 초기 상태 37.2%·카메라 시점 59.7%, CVPR 2026 게재본(제목 'LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models') 표 2 는 로봇 초기 상태 31.9%·카메라 시점 56.4% 다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f28 | [사실] | ROSA FAQ 는 핵심 ROSA 에이전트가 텍스트 상호작용에 한정되어 물리 세계와 상호작용할 수 없으며, 물리적 상호작용에는 사용자가 맞춤 도구와 프롬프트를 만들어야 한다고 설명한다. | ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f29 | [사실] | 같은 ROSA FAQ 는 로봇 능력을 넘는 행동을 막으려면 맞춤 도구 안에 실행 전 로봇 상태·능력 확인 제약과 매개변수 검증·행동 제한 같은 안전 검사를 직접 넣으라고 권고한다. | ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f30 | [사실] | MCP 공식 블로그(2026-03-16)는 도구 어노테이션(readOnlyHint·destructiveHint 등)이 위험을 알리는 힌트일 뿐 실행 강제 수단이 아니며, 확실한 보장이 필요하면 네트워크 통제나 샌드박스로 해야 한다고 설명한다. | ref-1617 | 아니오 | medium | 2026-10-12 | — | — |
| f31 | [추정] | PickNik 의 MoveIt Pro MCP 서버 문서는 공유되는 배포(deployment) MCP 키는 읽기 전용이고, 로봇 동작은 호스트 사용자 세션에서 기존 Objective 를 시작·취소하는 것으로만 한정된다고 설명한다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [추정] | 같은 문서는 MCP 서버가 별도의 실행 확인 프롬프트를 추가하지 않으며, 도구 승인은 MCP 클라이언트 설정에 달려 있고 클라이언트가 자동 승인할 수도 있다고 적는다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f33 | [추정] | 같은 문서는 run_objective 로 시작한 로봇이 세션이 끝나도 계속 움직일 수 있고, cancel_objective 는 최선 노력(best effort)일 뿐 비상 정지가 아니며 MCP 취소·소프트웨어 정지는 물리적 비상 정지를 대체하지 않는다고 적는다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f34 | [추정] | Figure AI 의 2025-11-19 발표는 BMW 스파턴버그의 Figure 02 를 '11개월 배치'라고 부르면서, 개발 착수 뒤 6개월 안에 공장에 납품·시험을 시작하고 10개월 안에 생산 라인 전면 배치를 시작했으며 '6개월의 일일 가동'과 1,250시간 이상 가동을 적는다. 세 기간의 기점·종점이 달라 BMW 보도자료의 10개월·11개월 차이를 해소하지 못한다. | ref-1619, ref-1051 | 아니오 | low | 2026-10-12 | — | — |
| f35 | [추정] | 같은 Figure 발표에서 '교대당 99% 초과 성공률'과 '교대당 개입 0회'는 목표(target·goal)로 제시되며, 달성한 실측치로 보고되지 않았다. | ref-1619 | 아니오 | low | 2026-10-12 | — | — |
| f36 | [추정] | Figure AI 는 2026-06-30 발표에서 BMW 스파턴버그 공장에서 Figure 03 이 물류 작업 흐름을 수행한 것을 '첫 시연'으로 설명하고, 자사 VLA 인 Helix 02 가 손·팔·몸통·발을 함께 제어해 무거운 대차를 끌었다고 적는다. | ref-1620 | 아니오 | low | 2026-10-12 | — | — |
| f37 | [추정] | 기존 위키 5절의 'Figure AI 자체 발표로는 교차 확인하지 못했다'(Figure 03 착수 문단)는 고쳐야 한다. Figure AI 자체 발표(2026-06-30, 2025-11-19)가 있으나, BMW 와 같은 프로젝트의 당사자 자료라 독립 교차 확인으로는 세지 않는다. | ref-1620, ref-1619, ref-1051 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [사실] | 산업통상부 2025-11-24 보도자료에 따르면 산업부와 서울대가 M.AX 얼라이언스 협력 MOU 를 맺었고, 지원 과제 표의 휴머노이드 분과 과제는 '휴머노이드 AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 핵심 연구진 장병탁·박재흥 서울대 교수)이다. | ref-1621 | 아니오 | medium | 2026-10-12 | — | — |
| f39 | [의견] | 스킬 목록이 없거나 로봇 능력 밖인 요청을 계획기가 거절하는지(또는 닿지 않는 로봇에 배정하지 않는지)를 일반 성공률과 별도의 수용 시험 항목으로 두어야 한다. | ref-090, ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f40 | [의견] | 언어 모델 다중 로봇 계획의 검증 결과에는 일정 풀이 통과와 분해·배정의 정확성을 따로 적고, 계획 검증이 기대는 전제(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행, 정확한 사람 도움)를 함께 기록해 전제가 깨질 때 보장 상태를 다시 평가해야 하며, 이 보장을 플릿의 물리적 안전 보장과 섞지 않아야 한다. | ref-170, ref-092, ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f41 | [의견] | 연구 논문의 실물 시험(예: 로봇 팔 3대 단일 장면)은 사례 표에 장면 작성자·시뮬레이션 확인·복구 책임을 함께 적고 장기 운영 실적으로 표시하지 않아야 한다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [의견] | VLA 탑재 로봇의 능력 등록에는 모델·가중치 revision(해시), 로봇 기종·카메라, 좌표계·행동 단위·제어 모드, 정규화 통계, 행동 청크의 형태·관측 시각·유효기간·중단 조건, 허용 과제와 완료 판정을 두고, 명령 완료는 로봇 외부 상태로 확인하는 것이 필요해 보인다. 이는 ROP 설계 제안이며 표준이 아니다. | ref-1609, ref-1610, ref-1613 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [의견] | 공개 VLA 를 도입할 때 코드 라이선스와 가중치 사용 조건을 따로 확인하고, README 소개 문구만으로 상용 허용을 확정하지 않으며, 문서끼리 충돌하는 조건은 배포자에게 서면으로 확인할 항목으로 남겨야 한다. | ref-1608, ref-1609, ref-1611, ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f44 | [의견] | 카메라 교체·로봇 초기 자세 변경 같은 교란을 로봇별 수용 시험에 넣고, 벤치마크 수치는 판(arXiv 판·게재본)을 밝혀 인용하며, 단일 팔 시뮬레이션 벤치마크 순위를 제조사 혼합 플릿 순위로 환산하지 않아야 한다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f45 | [의견] | 언어 모델이 도구 호출로 로봇을 움직이는 구성에서는 어노테이션 힌트나 클라이언트 자동 승인에 기대지 말고, ROP 쪽 런타임에서 읽기/실행 권한·실행 대상·승인된 계획 revision·goal id 와 물리적 완료 판정을 검사하며, 세션 종료를 별도의 정지 절차에 연결해야 한다. | ref-1617, ref-1618, ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f46 | [의견] | 벤더·도입 기업 발표는 목표·기간·첫 시연과 실측 성과를 다른 열로 나누고, 운영 기간의 기점·종점, 성공률의 분모, 개입·실패 로그, 인계 신호가 공개될 때까지 도입 KPI 비교에 쓰지 않아야 한다. 국내 실증 목표(자동화율 80%·성공률 90%)도 같다. | ref-1619, ref-1620, ref-1051, ref-1621 | 아니오 | medium | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2603.02669 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2304.11477 | 아니오 |
| ref-1051 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 2026-06-25 | 벤더 문서 | medium | 2026-10-12 | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en | 아니오 |
| ref-1607 | Wang, J., He, G., & Kantaros, Y. (IEEE Robotics and Automation Letters 10(1)) | Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction | 2025-01 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2402.15368 | 아니오 |
| ref-1608 | OpenVLA 개발팀 (openvla/openvla GitHub) | OpenVLA — README 및 LICENSE (커밋 c8f03f4) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/README.md | 아니오 |
| ref-1609 | OpenVLA 개발팀 (Hugging Face openvla/openvla-7b) | openvla/openvla-7b — Model Card | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://huggingface.co/openvla/openvla-7b | 아니오 |
| ref-1610 | Physical Intelligence (Physical-Intelligence/openpi GitHub) | openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md | 아니오 |
| ref-1611 | NVIDIA (NVIDIA/Isaac-GR00T GitHub) | Isaac GR00T N1.7 — README 및 LICENSE (n1.7-release 브랜치) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/NVIDIA/Isaac-GR00T/blob/n1.7-release/README.md | 아니오 |
| ref-1612 | NVIDIA (Hugging Face nvidia/GR00T-N1.7-3B) | GR00T-N1.7-3B — LICENSE 및 모델 카드 | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://huggingface.co/nvidia/GR00T-N1.7-3B/blob/6949d5dfab2e872283e8cca8106ac3af8adcf39b/LICENSE | 아니오 |
| ref-1613 | Physical Intelligence (Ai, B. 외, arXiv) | π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities | 2026-04-16 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2604.15483 | 아니오 |
| ref-1614 | Fei, S., Wang, S., Shi, J. 외 (arXiv) | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | 2025-10-15 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2510.13626 | 아니오 |
| ref-1615 | Fei, S., Wang, S., Shi, J. 외 (CVPR 2026, Computer Vision Foundation Open Access) | LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models | 2026 | 논문 | high | 2026-10-12 | https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html | 아니오 |
| ref-1616 | NASA Jet Propulsion Laboratory (nasa-jpl) | FAQ · nasa-jpl/rosa Wiki | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/nasa-jpl/rosa/wiki/FAQ | 아니오 |
| ref-1617 | Model Context Protocol (Hungerford, O., Morrow, S., & Chang, L.) | Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do | 2026-03-16 | 오픈소스 문서 | medium | 2026-10-12 | https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/ | 아니오 |
| ref-1618 | PickNik Robotics | Connect an AI Assistant with the MCP Server (MoveIt Pro 문서 Version 10) | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.picknik.ai/how_to/programmatic_sdks/mcp_server/ | 아니오 |
| ref-1619 | Figure AI | F.02 Contributed to the Production of 30,000 Cars at BMW | 2025-11-19 | 벤더 문서 | medium | 2026-10-12 | https://www.figure.ai/news/production-at-bmw | 아니오 |
| ref-1620 | Figure AI | F.03 Arrives at BMW | 2026-06-30 | 벤더 문서 | medium | 2026-10-12 | https://www.figure.ai/news/f-03-at-bmw | 아니오 |
| ref-1621 | 산업통상부 | 서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다. | 2025-11-24 | 정부·연구기관 | medium | 2026-10-12 | https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 제조 공장: 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 'Figure AI 자체 발표(2026-06-30 F.03 첫 시연, 2025-11-19 F.02 회고)가 같은 내용을 설명하나 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 정정(f37, 벤더 주장 [추정]). 89·91행 10/11개월 충돌은 기존 내용 확인(5절 89·91행, oq-219) — 새로 넣지 말고 11개월은 Figure CEO 인용·10개월은 본문이라는 위치와 Figure 쪽 세 기간 축(6·10·11개월, 6개월 일일 가동·1,250시간)만 보탬(f34). 예외·성과 칸에 99% 초과 성공률·개입 0회는 목표치(f35), Figure 03 은 첫 시연(f36). 연구 실물 사례로 IMR-LLM 로봇 팔 3대 단일 장면(전문가 15분 장면 작성, 반복 미보고, f5)을 '연구 평가'로 표시해 추가할 수 있음. 물류창고: 산업부 M.AX 휴머노이드 과제(f38)는 로보티즈–BGF로지스 과제와 동일성 미확인이라 별도 문장으로, 80/90 실측 없음 유지; 의견 f41·f46 / 섹션 6(분리 2026-09-30-area44-s6) — 다중 로봇 계획 소절: SMART-LLM 36개 지시·1~4대·AI2-THOR(f1, C 트랙 stage-2 166행의 '원문 미열람' 수치를 원문 확인으로 보강), 불가능 과제의 모델별 차이(f2). IMR-LLM 23장면·50작업(f3), FIFO 휴리스틱(f4), 복잡 과제 성공률 하락과 도달 불가 배정(f6). 57행 '선택 그래프(disjunctive graph)'는 위키 안에서 '선언 그래프'(C 트랙 stage-1 112행)·'이접 그래프'(같은 파일 240행)와 갈리므로 한 용어로 통일 제안(이번 갱신은 s6 만, 트랙 페이지는 후속 정리). 기호 계획기 소절: LLM+P 의 사람 제공 도메인 전제(f7). 불확실도 소절: S-ATLAS 의 i.i.d.·무오류 실행·정확한 도움 전제와 110개 시뮬레이션 시나리오(f8~f10)를 KnowNo 다음에 추가; 의견 f39·f40 / 섹션 7(분리 2026-09-30-area44-s7) — 표 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 정정: 코드 MIT(f12), README 의 Llama Community License '적용될 수 있다'(f13), HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하고 해소하지 않음. 입출력 계약: OpenVLA 역정규화(f11), openpi 행동 청크·개방 루프(f15·f16), openpi 체크포인트에 π0.7 없음(f17). GR00T 행: N1.7 은 EA(f18), README License 절 코드/가중치 구분(f19), README 71행 '상용 가능' 문구는 벤더 주장(f20), 3B LICENSE 3.3절 비상업·NVIDIA 예외(f21), 세 문서 충돌(f22) — 표의 'GR00T N1 오픈소스(공개 모델)' 유형 칸에 '코드 Apache 2.0, 가중치 별도 라이선스' 주석. ROSA 행: FAQ 의 물리 상호작용 조건(f28)과 맞춤 도구 안전 검사 권고(f29). MCP 어노테이션 한계(f30)는 7절 또는 9절에 두되 기존 MCP 명세 서술(2026-09-29-area13-s6.md 45행 ref-856, C 트랙 stage-4 253행 ref-696)과 보완 관계로 적고 재서술하지 않음; 의견 f42·f43 / 섹션 8(분리 2026-09-30-area44-s8) — π0.7 항목 추가: 제어 모드 프롬프트(f23), 학습 중 지연 모사 240 ms(50 Hz)·UR5e 20 Hz(f24), seen/unseen 판정 어려움(f25) — 모두 회사 자체 보고서라 [추정]. LIBERO-Plus 항목 추가: 7개 교란 축(f26), OpenVLA-OFT 수치는 판을 밝혀 arXiv v3(로봇 37.2·카메라 59.7)와 CVPR 2026 게재본(로봇 31.9·카메라 56.4) 병기(f27). 국내 동향에 산업부 M.AX 휴머노이드 AI 파운데이션 모델 과제(f38); 의견 f44 / 섹션 9 — 로봇 자체 지능·제어 경계 아래에 도구 호출 실행 경계 문단: MCP 힌트는 강제 수단이 아님(f30), MoveIt Pro 의 읽기 전용 배포 키·서버 확인 프롬프트 없음·세션 종료 뒤 계속 이동·cancel 은 비상 정지 아님(f31~f33, 벤더 주장 [추정]), ROSA 맞춤 도구 조건(f28·f29); 의견 f45 / 섹션 11(분리 2026-09-30-area44-s11) — 부분 답(열린 채 둠): oq-216(배포물별 입출력 f11·f15·f16·f23, 의견 f42; 공통 등록 표준·적합성 시험 미확인), oq-217(연구 벤치마크 규모·조건 f1~f6·f8~f10·f26·f27; 설비·안전·시간창 통합 공통 기준 미확인), oq-219(Figure 기간 축 f34; 기점·종점 없어 미해소), oq-141(MoveIt Pro 는 승인을 클라이언트에 맡김 f32, 벤더). 관련 근거만: oq-104(f24 학습 조건 지연, 실측 아님), oq-218(f38, 실측 결과 없음). 답하지 못함: oq-314, oq-161. 메모 새 질문 1번(VLA 공통 최소 항목)은 문구 대조로 oq-216 과 같아 새로 만들지 않음; 2·3번과 라이선스 출처 충돌 2건을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/standards/index.md 287·288행 OpenVLA·GR00T N1 '오픈소스' 유형에 코드·가중치 라이선스 구분(f12~f14, f19~f22); docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md 118행 ROSA [추정] '확인·권한 장치 설명 없음'을 FAQ(f29)로 정리, 같은 파일 112·240행과 2026-09-30-area44-s6.md 57행의 disjunctive graph 번역어 통일, 같은 파일 310행 'IMR-Bench 규모 미확인'에 f3 연결; stage-2-data-and-standards.md 166·370행 SMART-LLM '원문 미열람'에 f1 연결; task-model-draft.md 133행 LLM+P 부분에 f7 연결. 다음 실행 후보: 59. 법·규제·보험·라이선스(f12~f22), 13. 대화형 기능의 신뢰·기반(f30~f33), 54. 시험·형식 검증·벤치마크(f26·f27) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 언어 모델 다중 로봇 계획의 검증이 기대는 가정(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행)을 런타임에서 누가 감시하고, 가정이 깨졌을 때 어떤 계획을 중단·재검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f9 | 종류: 일반
- 원격 VLA 정책의 행동 청크(개방 루프 실행) 유효기간과, 도구 세션이 끝난 뒤에도 로봇이 움직일 수 있는 MCP 실행의 안전한 정지 계약을 어떻게 결합할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반
- 출처 충돌: OpenVLA 공개 가중치의 사용 조건은 저장소 README(Llama 2 파생이라 Llama Community License 가 적용될 수 있음)와 Hugging Face 모델 카드(모든 체크포인트 MIT) 가운데 어느 쪽인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 출처 충돌
- 출처 충돌: GR00T N1.7 가중치의 상업적 사용 가능 여부는 README 소개(Apache 2.0 으로 상용 가능), README License 절·3B 모델 카드(NVIDIA Open Model License, 상업·비상업 사용 준비), 3B 가중치 저장소 LICENSE 3.3절(NVIDIA·계열사 외 비상업 한정) 가운데 어느 문서가 정하는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f22 | 종류: 출처 충돌

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 15건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-05/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f14·f22: OpenVLA·GR00T N1.7 의 라이선스 문서 충돌은 문서끼리 대조한 것이며 배포자의 정정·법적 우선순위는 확인하지 못함. OpenVLA 카드는 메모의 고정 리비전 258bd1d 가 현재 main 이력에 없어 main(47a0ec7) 기준
    - ref-1608·ref-1610: OpenVLA 커밋 c8f03f4, openpi 커밋 215abfb 의 커밋 날짜 미확인. ref-1611: GR00T n1.7-release 는 브랜치 이름으로만 열어 커밋 sha 고정 못 함. ref-1618: MoveIt Pro 문서 세부 빌드·발행일 미확인
    - f17: openpi 에 π0.7 가중치가 없음을 README 목록으로 확인했을 뿐, π0.7 보고서와 공개 배포물의 대응(U10)·실제 네트워크 포함 최대 지연(U11)은 미확인
    - f10: S-ATLAS 실물 실험이 없다는 것은 열람 본문 검색 기준이며 보충 자료는 보지 않음. SMART-LLM 실물 시험 대수·반복 수(U03), IMR-LLM 장기 운영(U04) 미확인
    - f34: BMW–Figure 10/11개월의 기점·종점과 집계 관계, 교대별 실측 성공률·개입 분모(U13·U14), Figure 03 첫 시연 이후 가동률(U15) 미확인
    - f38: 산업부 M.AX 휴머노이드 과제와 로보티즈–BGF로지스 물류 과제의 동일성(U17), 자동화율 80%·성공률 90% 실측 결과(U16, oq-218) 미확인
    - 메모 V01(GR00T-N1.7-ApplePnP-V1 모델 카드)와 V11(BGF로지스 매거진 회고)은 신규 출처 예산(15건) 때문에 출처째 넣지 않음. 둘 다 벤더 [추정]이며 ROP 판단에 쓰는 내용(라이선스 충돌·80/90 실측 부재)은 다른 finding 이 담음
    - 병원·상업시설·실외에서 로봇 기반 모델·언어 모델 계획을 쓴 이기종 플릿 현장 실증(U18), 벤더 혼합 장기 운영 플릿의 독립 재현 로그(U02), VLA 공통 능력 등록 표준·적합성 시험(U06) 미확인
    - 메모가 진단에 쓴 위키 고정 커밋(85960d2)과 현재 배포판의 동일성 미확인(U01)
- 범위 경계 위반 의심:
    - f12~f22: 코드·가중치 라이선스 문구는 59. 법·규제·보험·라이선스 쪽 내용이므로 문서 원문 대조까지만 하고 상용 사용 가능 여부의 법적 판단은 하지 않음
    - f30~f33: 도구 호출 권한·승인·세션 종료는 13. 대화형 기능의 신뢰·기반, 29. 명령·작업 실행의 신뢰성과 겹치며, 이 영역에는 언어 모델 계획이 로봇 실행으로 넘어가는 경계 관점으로만 씀
    - f26·f27: LIBERO-Plus 는 단일 팔 조작 시뮬레이션 벤치마크로 54. 시험·형식 검증·벤치마크와 겹치며, 이 영역에는 VLA 수용 시험 설계의 근거로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1607~ref-1621, 예약 구간 ref-1607~ref-1636 안), 재사용 4건(ref-090·ref-170·ref-092·ref-1051). 출처 매핑(검증 결과 기준): 메모 n1→ref-090, n2→ref-170, n3→ref-092, n4→ref-1607, n5→ref-1608, n6→ref-1609(main 47a0ec7 기준), n7→ref-1610, n8(ApplePnP 카드)→예산 초과로 제외, n9→ref-1611, n10→ref-1613, n11→ref-1612(같은 저장소 모델 카드 포함), n12→ref-1617, n13→ref-1616(ref-171·172 와 다른 페이지), n14→ref-1618, n15→ref-1051(글로벌 URL, 캐나다판 대신), n16→ref-1619, n17→ref-1620, n18→ref-1621, n19(BGF 매거진)→예산 초과로 제외, n20→ref-1614, 추가: CVPR 2026 게재본→ref-1615. 모든 출처 원문 열람(fetched true). 출처 type: OpenVLA·openpi·GR00T 저장소와 Hugging Face 모델 저장소 파일은 프로젝트가 관리하는 저장소라 '오픈소스 문서'로 두어 인터페이스·라이선스 원문 옮김(f11~f19, f21·f22)은 [사실]; MoveIt Pro·Figure·BMW 는 '벤더 문서'라 해당 finding 은 모두 [추정]·vendor_claim. 교차 확인 0건(SMART-LLM/IMR-LLM/S-ATLAS 는 조건이 달라 같은 주장 아님, OpenVLA 문서쌍·GR00T 문서셋·openpi/π0.7·LIBERO-Plus 두 판·BMW/Figure 는 같은 팀·기관·프로젝트). 검증 반영: F21 은 arXiv v3 값(37.2)에 판을 명시하고 CVPR 2026 게재본 값(로봇 31.9·카메라 56.4) 병기(f27); F13 '적용된다'→'적용될 수 있다'(f13); F14 현재 main 도 같은 문구라 충돌 지속(f14); F18/README 71행 '상용 가능'은 벤더 주장으로 분리(f20)하고 README·LICENSE·카드 3자 충돌 기록(f22); F06 은 성공률 하락의 예시이며 정량화 없음; F02 에 GPT-4·Claude-3 거절과 표 I 밖 명시; F05 에 15분 수동 장면 작성·반복 미보고; U10 을 f17 로; U13 Figure 세 기간을 f34 로; 위키 5절 93행 정정 제안(f37). 중복 제거: F01 은 C 트랙 stage-2 166행 기존 수치의 원문 확인 보강으로만(f1), F07 은 기존 [추정] 보강, F23 은 기존 MCP 명세 서술과 보완 관계로 서술, V08(BMW 10/11개월 충돌)은 기존 5절·oq-219 에 있어 새 finding 으로 넣지 않고 f34 근거 메모와 rationale 에 위치만 적음. 열린 질문: 부분 답 oq-216·oq-217·oq-219·oq-141, 관련 근거 oq-104·oq-218, 해결 제안 없음(open_questions_resolved 비움). 메모 새 질문 1번은 oq-216 과 같아 만들지 않고, 2·3번과 출처 충돌 2건을 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·표·행(저장 원문 기준)과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-08/research.md

```markdown
# 리서치 브리프 2026-09-30-08

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-08 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 45. 문서·도면·장면 이해 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 문서 레이아웃 분석, 표 구조 인식, 출처 근거 연결, 패놉틱 심볼 스포팅, 외부 인프라 카메라 인식 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(도면 인식)·제조 공장(고정 카메라 인식)·물류창고(CCTV 기반 다중 로봇 조율)·실외(다중 로봇 장면 그래프) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 문서 파싱, LLM 기반 데이터시트 추출, 도면 심볼 인식, 고정 카메라·로봇 인식 융합 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Docling, OmniDocBench, LangExtract, CubiCasa5K, FloorPlanCAD, AI Hub 건축 도면 데이터 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-147·oq-196·oq-197 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]
2. 매뉴얼·데이터시트 같은 기술 문서를 파싱하고 LLM으로 구조화 정보(예: 자산관리셸 속성)를 뽑을 때 보고된 정확도와 실패 원인은 무엇인가? (섹션 3·6·8 겨냥)
3. 추출한 항목마다 원문 위치를 근거로 붙여 사람이 대조·확정하게 하는 공개 구현이나 연구가 있는가? (oq-147, 섹션 6·7 겨냥)
4. 건축 도면(평면도·CAD) 인식의 대표 데이터셋·벤치마크와 성능은 무엇이며, 병원·공장·물류창고·상업 시설 같은 비주거 도면에서도 확인됐는가? (oq-196, oq-197, 섹션 5·7·8 겨냥, 한국 자료 우선)
5. 고정 카메라(CCTV·인프라 카메라)와 여러 로봇의 인식 결과를 모아 플랫폼 수준에서 공간 상태를 인식한 연구·현장 사례와 그 한계는 무엇인가? (섹션 5·6·8 겨냥)
6. 문서·도면·장면 이해에 쓰는 오픈소스·데이터셋·벤치마크는 무엇이며 라이선스·언어 범위는 어떤가? (섹션 4·7 겨냥)
7. 문서·도면·장면 이해에서 ROP가 직접 맡을 것과 로봇 자체 인식·설비·설계 도구에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | AECV-Bench(Kondratenko 외, arXiv 2601.04819, 2026-01)는 평면도 120장의 문·창·침실·화장실 개수 세기와 질의응답 192쌍으로 최신 멀티모달 모델의 건축·엔지니어링 도면 이해를 평가해, 글자 인식·텍스트 추출은 정확도 최대 0.95로 가장 높고 공간 추론은 중간, 심볼 이해·개수 세기는 0.40~0.55로 가장 낮다고 보고했다. | ref-1088 | 아니오 | medium | 2026-01 | — | — |
| f2 | [사실] | CubiCasa5K(Kalervo 외, arXiv 1904.01920, 2019-04)는 평면도 이미지 5,000장을 80개가 넘는 평면도 객체 범주로 다각형 단위 조밀 주석을 단 데이터셋과 다중 작업 합성곱 신경망 모델을 공개했다. | ref-063 | 아니오 | medium | 2019-04 | — | — |
| f3 | [사실] | FloorPlanCAD(Fan 외, arXiv 2105.07147, 2021-11 개정)는 주거·상업 건물의 CAD 평면도 1만 장 이상을 벡터 그래픽으로 담고 30개 객체 범주를 주석한 데이터셋으로, 셀 수 있는 심볼 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 찾는 패놉틱 심볼 스포팅 과제를 제안했다. | ref-067 | 아니오 | medium | 2021-11 | — | — |
| f4 | [사실] | 상업 시설 사례로, Su 외(Sensors, 2022-03)는 쇼핑몰 평면도 25장(점포 1,340개)을 대상으로 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고 2단계 영역 성장 분할과 문자 인식으로 평면도의 각 점포 공간을 식별해 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%를 보고했으며 실내 로봇 주행을 활용처로 들었다. | ref-1078 | 아니오 | medium | 2022-03-25 | 상업 시설 / 작업 대상 | — |
| f5 | [사실] | 과학기술정보통신부·한국지능정보사회진흥원의 AI Hub 「건축 도면 데이터」(2022년 구축, 주관 에이치씨아이플러스)는 도면 48,033장(평면도 41,556·단면도 3,262·입면도 1,595·구조도 1,620)을 아파트·연립다세대·단독주택의 주거 용도로만 구성하고, 구조 8종(출입문·창호·벽체 등)·공간 12종(거실·침실·주방 등)·객체 5종(변기·세면대·싱크대·욕조·가스레인지) 라벨을 두며, 유효성 검증 모델 성능으로 YOLOv5 객체 탐지 mAP 90.33%, DeepLabV3+ 분할 mIoU 71.2%, 문자 인식 CER 4.95%를 제시한다. | ref-1012 | 아니오 | medium | 2022 | 가정 / 작업 대상 | — |
| f6 | [추정] | AI Hub 건축 도면 데이터의 라벨은 주거 건축 요소와 위생·주방 설비로 이루어져 있어 충전 위치·승강기 앞 대기 구역 같은 로봇 운영용 클래스는 들어 있지 않고 비주거 건물 도면은 포함되지 않은 것으로 보이므로, 병원·공장·물류창고 도면에 쓰려면 별도 라벨과 데이터가 필요할 것으로 추정된다. | ref-1012 | 아니오 | low | 2026-09-30 | — | — |
| f7 | [사실] | OmniDocBench(Ouyang 외, CVPR 2025)는 학술 논문·교과서·손글씨 노트·밀집 조판 신문 등 9개 문서 출처에 19개 레이아웃 범주와 15개 속성 라벨을 달아, 파이프라인 방식과 시각–언어 모델 방식의 PDF 문서 파싱을 전체·모듈·속성 수준에서 비교 평가하는 벤치마크다. | ref-1080 | 아니오 | medium | 2025-03-25 | — | — |
| f8 | [사실] | OmniDocBench 공식 저장소 README 는 2026-04 판(v1.6) 기준 PDF 1,651쪽·10개 문서 유형·영어와 중국어(간체)·혼합 언어로 구성된다고 밝히고, 종단 평가 상위 모델(TeleOCR)의 종합 점수 96.91·텍스트 편집 거리 0.0267·표 TEDS 96.82 를 싣으며, 데이터는 연구 목적으로만 쓰고 상업적 사용을 허용하지 않는다. | ref-513 | 아니오 | medium | 2026-04 | — | — |
| f9 | [사실] | IBM Research 가 공개한 Docling(Livathinos 외, arXiv 2501.17887, 2025-01)은 여러 문서 형식을 하나의 구조화 표현으로 바꾸는 MIT 라이선스 오픈소스 도구로, 레이아웃 분석에 DocLayNet 기반 모델을, 표 구조 인식에 TableFormer 를 쓰고 일반 하드웨어에서 적은 자원으로 동작하며 LangChain·LlamaIndex·spaCy 에 통합되어 있다. | ref-1082 | 아니오 | medium | 2025-01-27 | — | — |
| f10 | [사실] | Xia·Xiao·Jazdi·Weyrich(IEEE Access, 2024)는 데이터시트 원문에서 '의미 노드'를 뽑아 LLM 에이전트로 자산관리셸(AAS) 인스턴스 모델을 생성하는 시스템을 만들고, 원문 정보가 오류 없이 AAS 로 옮겨진 비율(유효 생성률)을 62~79%로 보고했다. | ref-1087 | 아니오 | medium | 2024-06 | — | — |
| f11 | [사실] | Groß·Heidrich 의 AAS-RAIL(arXiv 2609.07334, 2026-09)은 전기공학·유체동력 분야 4개 제조사의 제품 데이터시트–AAS 쌍 200건에서, 비슷한 기존 AAS 로부터 추출 지침을 검색해 문맥 예시로 쓰는 방식으로 속성 추출 정확도를 평균 51.8%에서 71.7%로 높였으나, 원문 데이터시트에서 정답 속성값을 찾을 수 있는 경우가 전체 속성의 56.2%뿐이어서 전문가 검토가 여전히 필요하다고 밝혔다. | ref-1086 | 아니오 | medium | 2026-09-07 | — | — |
| f12 | [추정] | 독립된 두 연구(f10·f11)를 종합하면 LLM 으로 기술 데이터시트를 표준 자산 모델로 옮길 때 오류 없이 옮겨지는 비율은 대략 5~8할 수준이고, 원문 자체에 정보가 없거나 이름과 값이 떨어져 있는 경우가 많아 사람의 검토 없이 등록 정보로 확정하기는 어려운 것으로 보인다. | ref-1087, ref-1086 | 아니오 | low | 2026-09-30 | — | — |
| f13 | [사실] | 오픈소스 LangExtract(google/langextract, Apache 2.0)는 LLM 으로 비정형 텍스트에서 구조화 정보를 뽑으면서 추출한 항목마다 원문 텍스트의 정확한 위치를 연결하고, 그 위치를 원문 맥락에 강조해 보여 주는 HTML 검토 화면을 만들어 사람이 대조할 수 있게 하며, 구글의 공식 지원 제품은 아니라고 밝힌다. | ref-1089 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f14 | [사실] | Dussard·Sarthou(LAAS, arXiv 2606.17073, 2026-06)는 URDF 의 구조·기구학 기술 안 식별자를 LLM 이 상식으로 해석해 기존 온톨로지 개념에 맞춰 로봇 온톨로지를 자동으로 채우는 파이프라인을 제안했으나, 초록에는 정량 평가 결과를 밝히지 않았다. | ref-239 | 아니오 | medium | 2026-06-10 | — | — |
| f15 | [사실] | 제조 공장 사례로, Brorsson 외(arXiv 2512.15215)의 인프라 기반 이동 로봇 시스템은 천장 카메라가 로봇에 붙인 ArUco 표식을 검출해 로봇 위치·방향을 계산하고, 저해상도 영상의 이진 의미 분할로 장애물과 빈 공간을 격자 단위로 구분하며, 카메라별 점유 지도를 전역 지도로 합치되 시야가 겹치는 곳은 가장 가까운 카메라 하나의 결과만 쓴다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 수행 자원 | — |
| f16 | [사실] | 같은 연구의 대형 상용차 제조 현장 배치에서는 약 8 m 높이에 단 카메라 15대(대당 약 60 m²)가 바닥을 덮고, 로봇 6대가 약 150 m 구간에서 머플러를 운반하며 하루 약 130회 운반(주기 7분)을 수행했다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 작업 대상 | — |
| f17 | [사실] | 같은 연구는 인프라 카메라 인식의 한계로 카메라 간 하드웨어 동기화가 없어 생기는 시간 차 오류, 가림·센서 고장·제한된 시야 범위로 인한 위치 추정 중단, 작업자·독점 제품·기밀 공정이 영상에 찍히는 개인정보·기밀 문제를 든다. | ref-308 | 아니오 | medium | 2025-12 | 제조 공장 / 제약 | — |
| f18 | [사실] | 물류창고 사례로, Robinson 외(Oxford, arXiv 2606.06762, 2026-06)는 로봇에 작업용 주행 장비를 싣지 않고 외부 CCTV 카메라망과 외부 계산만으로, 보정하지 않은 화소 단위 위상 카메라 그래프 위 영상 공간에서 다중 로봇을 계획·제어하며 카메라 시야가 겹치는 구역을 공유 자원으로 순차 배정해 교착을 막는 방식을 실제 창고(로봇 4대, 카메라 30대, 길이 27 m 통로 6개)에서 시연하고 이를 첫 현장 시연이라고 밝혔다. | ref-1075 | 아니오 | medium | 2026-06-04 | 물류창고 / 수행 자원 | — |
| f19 | [사실] | Modi 외(arXiv 2605.18197, 2026-05)는 RGB 카메라만으로 3차원 장면 그래프를 만드는 능동 탐색 방법을 제안하고, 시뮬레이션(ReplicaCAD)에서 천장 쪽 고정 외부 카메라 1대로 초기화하면 기준 방법의 장면 그래프 노드 수가 16개에서 37개로, 재현율이 0.12에서 0.27로 늘었으며, 로봇 없이 고정 카메라 3대만 쓰면 F1 이 0.421(복잡한 아파트)·0.516(가구 배치 방)으로 30단계 능동 탐색의 재현율에는 못 미치지만 환경의 주요 구조는 잡는다고 보고했다. | ref-1083 | 아니오 | medium | 2026-05-18 | — | — |
| f20 | [사실] | 실외 사례로, Strader 외(MIT 등, arXiv 2506.07454, 2025-07 개정)는 로봇마다 만든 장면 그래프와 개방형 객체 지도를 대응점으로 정합해 하나의 공유 3차원 장면 그래프로 합치고, LLM 이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 운영자의 자연어 의도를 PDDL 목표로 바꾸는 다중 로봇 계획·실행 시스템을 대규모 실외 환경의 실제 작업으로 평가했다. | ref-1084 | 아니오 | medium | 2025-07-10 | 실외 / 시작 조건 | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽는가)에 대해, 문서의 글자·표를 읽는 파싱은 공개 벤치마크에서 높은 점수를 내지만(f1·f8), 데이터시트에서 속성값을 표준 모델로 옮기는 정확도는 5~8할 수준이고(f10·f11), 도면의 심볼 개수 세기는 멀티모달 모델에서 0.40~0.55 에 그치며(f1), 전용 도면 인식 모델도 상업 시설 평면도에서 전체 검출 약 84% 수준이고(f4), 고정 카메라 장면 인식은 구조는 잡되 세부 객체 재현율이 낮아(f19) 어느 쪽도 사람 확인 없이 실행 정보로 쓰기에는 부족한 것으로 보인다. | ref-1088, ref-513, ref-1087, ref-1086, ref-1078, ref-1083 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 이기종 로봇 등록과 능력 표현에 필요한 정보가 제조사 문서·데이터시트·URDF 에 흩어져 있어 이를 자동으로 읽어야 하고(f10·f11·f14), 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며(f1·f4), 여러 로봇·고정 카메라의 인식을 모아야 로봇 한 대로는 가려지는 공간 상태를 알 수 있는데(f15·f18·f19), 각 단계의 오류가 그대로 등록 정보·지도·세계 상태의 오류로 이어지기 때문이다. | ref-1087, ref-1086, ref-239, ref-1088, ref-1078, ref-308, ref-1075, ref-1083 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 45. 문서·도면·장면 이해에서 ROP 가 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가(f7·f9·f11), 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름(f13), 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 플랫폼 수준 융합(f15·f17·f20)이다. | ref-1080, ref-1082, ref-1086, ref-1089, ref-308, ref-1084 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 온보드 센서 인식·SLAM·국지 회피(f15·f20의 로봇 측 인식)는 로봇 제조사에, CCTV·영상 관리 시스템과 카메라 설치·동기화(f17·f18)는 시설·보안 설비 쪽에, 도면·BIM 작성 도구와 원본 도면(f3·f5)은 설계·건축 쪽에 속하므로, ROP 는 이들이 내는 인식 결과·영상·도면을 받아 해석·융합하는 인터페이스와 검토 절차를 맡을 것으로 보인다. | ref-308, ref-1084, ref-1075, ref-067, ref-1012 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 매뉴얼 해석이 적용되는 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전(f10·f11·f14), 능력 항목을 받는 5. 로봇 능력·작업 표현(f14), 추출 결과 검토의 7. 온톨로지 검증·변경 관리(f13), 도면 해석이 적용되는 14. 도면·BIM에서 지도 만들기(f1~f5), 지도와 장소 의미의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리(f4·f20), 융합된 현재 상태를 담는 18. 실시간 세계 상태·데이터 일관성(f15·f19), 사람 인식의 19. 사람·보행자 모델(f15), 언어 모델 계획의 44. 로봇 기반 모델·언어 모델 계획(f20), AI 결과 사용 기준의 47. AI·학습·적응과 모델 운영(f12·f21), 영상 개인정보의 53. 개인정보·영상 데이터(f17), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f7), 적용 현장인 61. 물류창고(f18)·62. 제조 공장(f15~f17)·64. 상업 시설(f4)·66. 실외(f20)와 이어진다. | ref-1087, ref-1086, ref-239, ref-1089, ref-1088, ref-1078, ref-1084, ref-308, ref-1083, ref-1080, ref-1075 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1075 | Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv) | Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse | 2026-06-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.06762 | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. (arXiv) | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1904.01920 | 아니오 |
| ref-1012 | 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-1078 | Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)) | A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans | 2022-03-25 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/ | 아니오 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.17073 | 아니오 |
| ref-1080 | Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv) | OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations | 2025-03-25 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2412.07626 | 아니오 |
| ref-513 | OpenDataLab (opendatalab/OmniDocBench) | OmniDocBench — README | 2026-04 | 오픈소스 문서 | medium | 2026-09-30 | https://github.com/opendatalab/OmniDocBench | 아니오 |
| ref-1082 | Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv) | Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion | 2025-01-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2501.17887 | 아니오 |
| ref-1083 | Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv) | RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots | 2026-05-18 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2605.18197 | 아니오 |
| ref-1084 | Strader, J., Ray, A., Arkin, J. 외 (arXiv) | Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs | 2025-07-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2506.07454 | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv) | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-11-29 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2105.07147 | 아니오 |
| ref-1086 | Groß, J., & Heidrich, J. (arXiv) | AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning | 2026-09-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.07334 | 아니오 |
| ref-1087 | Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv) | Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0 | 2024-06-24 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2403.17209 | 아니오 |
| ref-1088 | Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv) | AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding | 2026-01-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2601.04819 | 아니오 |
| ref-1089 | Google (google/langextract) | LangExtract — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/google/langextract | 아니오 |
| ref-308 | Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv) | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2512.15215 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 문서 레이아웃 분석·표 구조 인식 f7·f9, 출처 근거 연결 f13, 패놉틱 심볼 스포팅 f3, 인프라 카메라 인식·공유 장면 그래프 f15·f20 / 섹션 5: 상업 시설 — f4(쇼핑몰 평면도 인식, 작업 대상: 공간), 제조 공장 — f15(수행 자원: 천장 카메라)·f16(작업 대상: 머플러 운반)·f17(제약: 동기화·가림·개인정보), 물류창고 — f18(수행 자원: CCTV 망만으로 다중 로봇 조율), 실외 — f20(시작 조건: 운영자 자연어 의도), 가정 — f5(주거 도면 데이터). 병원 사례는 찾지 못함을 명시 / 섹션 6: 문서 파싱 f7·f8·f9, LLM 데이터시트 추출 f10·f11·f12, URDF 해석 f14, 원문 위치 근거 f13, 도면 인식 f1~f4, 카메라·로봇 인식 융합 f15·f18·f19·f20 / 섹션 7: Docling f9, OmniDocBench f7·f8, LangExtract f13, CubiCasa5K f2, FloorPlanCAD f3, AI Hub 건축 도면 데이터 f5, AECV-Bench f1 / 섹션 8: f1·f4·f10·f11·f15·f18·f19·f20 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 4, 5, 7, 14, 15, 16, 18, 19, 44, 47, 53, 54, 55, 61, 62, 64, 66 / 섹션 11: 기존 oq-147·oq-196 과 open_questions_new 4건. 다음 실행 후보: 4. 이기종 로봇 등록 페이지에 f10·f11·f13 반영, 18. 실시간 세계 상태·데이터 일관성 페이지에 f15·f17 반영. |
| update | docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md | 5, 8, 11 | 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 f4 를 섹션 5(상업 시설 사례)에, f1·f3·f5 를 섹션 8 에, f5·f6(oq-197 해결 근거)·f4(oq-196 부분 근거)를 섹션 11 에 반영 제안. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 문서 레이아웃 분석 | Document Layout Analysis | 문서 페이지 이미지나 PDF 에서 본문·제목·표·그림·수식 같은 영역을 찾아 종류를 구분하고 읽는 순서를 정하는 문서 이해의 첫 단계다. |
| 표 구조 인식 | Table Structure Recognition | 문서 속 표의 행·열·병합 셀 구조를 복원해 표 내용을 기계가 읽을 수 있는 형식으로 바꾸는 기술로, TEDS 같은 트리 편집 거리 지표로 평가한다. |
| 출처 근거 연결 | Source Grounding | 언어 모델이 문서에서 추출한 항목마다 원문 속 정확한 위치(문자 범위·쪽·절)를 함께 기록해 사람이 원문과 대조해 확인할 수 있게 하는 방식이다. |
| 인프라 장착 센서 | Infrastructure-mounted Sensing | 천장·벽 같은 시설에 고정한 카메라·센서로 로봇 밖에서 넓은 영역의 위치·장애물·사람을 인식해 로봇 온보드 센서의 가림과 시야 한계를 보완하는 방식이다. |

## 열린 질문

새로 생긴 질문:

- OmniDocBench 같은 공개 문서 파싱 벤치마크에 한국어 문서가 없는데, 한국어 로봇 매뉴얼·설비 도면을 파싱·추출할 때의 정확도를 측정한 자료가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 4. 이기종 로봇 등록 | 근거: f8 | 종류: 일반
- 일반 제품 데이터시트가 아니라 로봇 매뉴얼(능력·실행 조건·오류 코드)을 대상으로 LLM 추출 정확도를 측정한 공개 벤치마크나 연구가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 5. 로봇 능력·작업 표현 | 근거: f11 | 종류: 일반
- 하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 18. 실시간 세계 상태·데이터 일관성 | 근거: f17 | 종류: 일반
- 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? | 관련 영역: 45. 문서·도면·장면 이해, 53. 개인정보·영상 데이터 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-197

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - f2 CubiCasa5K 의 수집 지역(핀란드)·주거 전용 여부와 성능 수치: 검색 요약에만 나오고 초록·README 에서 확인하지 못함(본문 PDF 추출 실패)
    - f3 FloorPlanCAD 규모·범주 수: 초록은 1만 장 이상·30개 범주·주거와 상업, 검색 요약은 1만5천 장·35개 범주·병원·학교 포함으로 판에 따라 다름. PQ 0.561 은 검색 요약에만 있어 넣지 않음
    - f6 AI Hub 구조 8종·공간 12종 라벨의 전체 목록은 페이지에 일부만 보여 미확인
    - f18 임무 시간·조율 통계 수치는 초록에 없어 미확인
    - f20 로봇 대수·실험 수치는 초록에 없어 미확인
    - f10 데이터셋 규모는 초록에 없어 미확인
    - ETRI 전자통신동향분석 '스마트제조 분야 LLM 기반 안전성 평가' 글(공장 매뉴얼 기반 질의응답 평가)은 ECONNRESET 으로 두 번 열지 못해 넣지 않음
    - Belfadel 외(arXiv 2609.31663) 산업 보고서 온톨로지 추출은 정량 수치가 초록에 없어 넣지 않음
    - 병원 현장의 고정 카메라·로봇 인식 융합 사례는 찾지 못함(찾은 arXiv 2509.26106 은 시뮬레이션 병원·저가 하드웨어라 제외)
    - oq-196 은 부분 근거만(f4 상업 시설 평면도 83.81~92.54%, f3 상업 건물 포함 데이터셋) 확보해 해결 제안하지 않음
    - oq-147 은 범용 도구 LangExtract(f13)만 찾았고 로봇 매뉴얼·URDF 능력 항목에 원문 위치를 붙인 공개 구현은 찾지 못함
- 범위 경계 위반 의심:
    - f15·f20: 로봇 측 인식·SLAM·재위치 추정은 로봇 자체 지능(연계 대상)이므로 플랫폼 수준 융합 근거로만 쓰고 f24 에서 구분함
    - f18: 로봇에 주행 장비 없이 외부 카메라·외부 계산으로 주행을 제어하는 방식은 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례('경계는 제품 전략에 따라 이동할 수 있다')이며 ROP 기본 범위로 서술하지 않도록 주의
    - f19·f15: 장면 인식 결과가 표현하는 현재 상태는 18. 실시간 세계 상태·데이터 일관성의 내용이며 34. 시뮬레이션·예측용 디지털 트윈과 섞지 않음(f19 의 시뮬레이션은 평가 환경일 뿐 예측 실험이 아님)
    - f24: CCTV·영상 관리 시스템, 설계 도구·원본 도면을 '연계 대상: '으로 표시함
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 병원 사례와 한국어 문서 이해 자료를 더 넣지 못했다. 재사용 1건(ref-308: 참고문헌 목록 전체가 입력에 없어 값은 이전 브리프 2026-09-30-05 의 출처 표를 따랐고, 이번에 HTML 본문을 다시 열었다). 원문 열람: 16건 모두 열었다(webfetch 14건, github_raw 2건). 논문은 대부분 초록 페이지이고 Su 외(PMC 본문)·Modi 외·AAS-RAIL·Brorsson 외(arXiv HTML 본문)만 본문을 봤다. 교차 확인 0건: 수치마다 데이터·지표가 달라 같은 값을 두 출처로 확인할 수 없었고, f12·f21 은 종합 추정(low)으로 냈다. 벤더 문서는 쓰지 않았다. 분류 원문 핵심 질문(매뉴얼·도면·현장 영상을 AI 가 얼마나 정확히 읽어 내는가)에는 f21 로 답했고 결론은 '글자·표 파싱은 벤치마크에서 높지만 속성 추출 5~8할, 도면 심볼 세기 0.40~0.55, 고정 카메라 장면 인식은 구조 수준이라 사람 확인 없이 실행 정보로 쓰기 어렵다'는 추정이다. 현장 유형 사례는 상업 시설(f4)·제조 공장(f15~f17)·물류창고(f18)·실외(f20)·가정(f5, 주거 도면 데이터)이며 병원·기타 사례는 찾지 못했다. 국내 자료는 AI Hub 건축 도면 데이터(ref-1012) 1건이다. oq-197 해결 근거: f5·f6(비주거 도면 미포함, 공개된 객체 5종에 로봇 운영 클래스 없음; 구조·공간 라벨 전체 목록은 미확인이라 검증 판단 필요). oq-196·oq-147 은 부분 근거만 있어 해결 제안하지 않았다. 교차 규칙에 따라 매뉴얼 해석 finding(f10·f11·f13·f14)은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에, 도면 해석 finding(f1~f6)은 14. 도면·BIM에서 지도 만들기에 연결하도록 제안했다. 용어집에 이미 있는 평면도 인식·패놉틱 심볼 스포팅·파놉틱 품질·3차원 장면 그래프·협동 인지·래스터–벡터 변환·자산관리셸·환각은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```
