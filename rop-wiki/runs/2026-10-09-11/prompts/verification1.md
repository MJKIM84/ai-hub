(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-11
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 18. 실시간 세계 상태·데이터 일관성 (E. 사물·사람·실시간 상태)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 세부영역 반영 제안: 2건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-10-09-11/target.json

```json
{
  "run_id": "2026-10-09-11",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 144,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 18,
    "area_name": "18. 실시간 세계 상태·데이터 일관성",
    "category": "E. 사물·사람·실시간 상태",
    "category_letter": "E"
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
  "selection_rationale": "CLI 지정 run_type=update, area=18"
}
```

### runs/2026-10-09-11/research.json

```json
{
  "run_id": "2026-10-09-11",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 18,
    "area_name": "18. 실시간 세계 상태·데이터 일관성",
    "category": "E. 사물·사람·실시간 상태"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 시나리오 2건뿐, 병원·제조 공장·기타 현장 사례 없음",
    "섹션 6. 대표 접근법과 기술 — 시각 필드·QoS 외에 시간이 지날수록 믿음을 낮추는 확률 모델, 허가 만료 시각(lease) 같은 접근이 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — 로봇–승강기·자동문 인터페이스 표준(ISO 초안, 싱가포르 TR 93)과 OPC UA 시각 필드가 원문 확인 없이 비어 있음(ref-288 원문 미열람 상태)",
    "섹션 8. 대표 연구와 자료 — 반정적 대상의 지속성 추정 연구, 운영 중 시뮬레이션 초기화 연구 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 위치추정 품질 점수로 신뢰 판단을 한다는 서술이 VDA 5050 원문(로그·시각화 전용 규정)과 맞는지 미확인",
    "섹션 10. 다른 연구영역과의 연결 — 트랙 floorplan-recognition 단계 3 반영 제안 2건(정적 능력 대조와 현재 상태 층 분리, 34. 시뮬레이션·예측용 디지털 트윈에 현재 상태 초기값 공급) 미반영",
    "섹션 11. 열린 질문 — oq-034(설비 상태 허용 경과 시간), oq-035(시각 동기화), oq-028(위치추정 신뢰도), oq-037(출처 충돌)에 새 근거 없음",
    "정정 요청 없음(inbox/corrections.md 비어 있음)"
  ],
  "research_questions": [
    "조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]",
    "문·승강기·충전기 같은 설비 상태를 몇 초까지 믿을지 정한 표준·국내 기준이 새로 나왔는가, 로봇–승강기·자동문 인터페이스 표준은 어디까지 와 있는가? (oq-034, 섹션 7·11 겨냥)",
    "상태 보고 주기·시각 체계가 다른 로봇이 섞일 때 시각 동기화와 수신 시각 처리를 어떻게 하는가? (oq-035, 섹션 6 겨냥)",
    "VDA 5050 의 위치추정 품질 정보(localizationScore 등)를 관제 판단 논리에 써도 되는가? (oq-028, 섹션 9 겨냥)",
    "트랙 floorplan-recognition 단계 3 반영 제안: 정적 능력·지도 대조와 현재 상태 층(문 상태, Open-RMF 차선 폐쇄)을 어떻게 나누며, 운영 중 예측 시뮬레이션을 현재 상태로 초기화한다는 연구 근거는 무엇인가? (섹션 10 겨냥)",
    "물류창고 밖의 현장(병원·제조 공장·기타)에서 설비·로봇 상태를 통합하거나 오래된 상태를 다룬 사례는 무엇인가, 한국 자료는 있는가? (섹션 5 겨냥)",
    "오래된 관측을 고정 임계값이 아니라 시간에 따라 믿음을 낮추는 방식으로 다루는 연구가 있는가? (섹션 6·8 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Open-RMF 의 rmf_fleet_msgs/LaneRequest 메시지는 플릿 이름과 열 차선 목록(open_lanes)·닫을 차선 목록(close_lanes)만으로 이루어져, 경로망(내비게이션 그래프) 자체를 바꾸지 않고 차선의 통행 가능 여부만 바꾸는 요청이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1451"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LaneRequest.msg 정의: string fleet_name / uint64[] open_lanes / uint64[] close_lanes (open-rmf/rmf_internal_msgs main 브랜치 원문, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "Open-RMF rmf_traffic 의 LaneClosure 클래스는 그래프 안 차선의 폐쇄 상태(열림·닫힘)를 따로 기술하고 차선 번호별로 열기·닫기·열림 확인을 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1453"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"This class describes the closure status of lanes in a Graph, i.e. whether a lane is open or closed.\" (rmf_traffic API 문서, 발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "Open-RMF 유지관리자는 정비 중인 승강기·문을 RMF 에 알리는 방법으로, 그 승강기·문을 지나는 차선을 찾아 닫는 차선 폐쇄 기능을 권했고, 폐쇄 시점은 통합자가 정하며 플릿 어댑터가 승강기 상태(lift_states)의 OFFLINE 을 보고 해당 차선을 닫는 구성을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1452",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2024-01-13 답변: lift·door 를 지나는 lane 을 찾아 closed 로 설정. 2024-01-24 답변: 어댑터가 lift_states 를 구독해 OFFLINE 을 보고 nav graph 로 해당 lane 을 닫도록 권함. LiftState 에 MODE_OFFLINE=4 정의",
      "as_of": "2024-01-24",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "로봇이 어디를 지날 수 있는가에 대한 정적 대조(5. 로봇 능력·작업 표현의 능력, 15. 지도·공간·위치 모델의 경로망)와, 지금 그 길이 열려 있는가를 나타내는 현재 상태 층(문 상태, 승강기 운영 모드, 차선 폐쇄)을 분리하고 18. 실시간 세계 상태·데이터 일관성이 후자를 시각과 함께 공급하는 구성이 Open-RMF 의 설계와 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1451",
        "ref-1453",
        "ref-1452",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Open-RMF 는 경로망은 그대로 두고 차선 폐쇄 상태를 별도 객체·메시지로 바꾸며, 폐쇄 계기로 승강기 상태를 쓴다(f1~f3 종합). 트랙 floorplan-recognition 단계 3 반영 제안 1(실행 2026-09-25-65)과 같은 방향",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "기계 수준 온라인 시뮬레이션 체계적 문헌 고찰(Deubert 외, 2024)은 온라인 시뮬레이션이 시스템의 실제 상태로 초기화되어야 하며, 이를 위해 상태 데이터의 명확한 정의·가용성·충분한 품질·충분한 갱신 빈도가 필요하고, 초기화 방식으로 실시스템과 동기화된 상위 시뮬레이션에서 복제하는 방법과 센서·구성요소 상태 측정에서 시작하는 방법이 있다고 정리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1449"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.2절 Initialization: \"initialized with the actual state of the system\"(Davis 1998 인용). 전제 4가지(정의·가용성·품질·갱신 빈도, Fowler·Rose 2004 인용). 3.2.1절: 상위 시뮬레이션 복제 또는 센서 측정(Hanisch 외)",
      "as_of": "2024-01-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "Galka(WSC 2024)는 SAP EWM 을 쓰는 주문 피킹 시스템의 시뮬레이션 기반 디지털 트윈에서, 빈 부하 상태로 시작하는 기준 모델 대신 실제 시스템의 부하 상태로 동기화하는 초기화 방식을 제안해 초기 과도 구간을 크게 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1450"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과의 초록 기준: 실시스템 부하 상태와의 동기화로 재료흐름 시뮬레이션의 과도 거동을 짧은 구간으로 한정, 기준 모델은 'empty' 부하에서 시작, 개선 폭 수치는 미확인(원문 PDF 추출 실패)",
      "as_of": "2024",
      "site_type": "물류창고",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "운영 중 예측 시뮬레이션은 실제 상태로 초기화해야 한다는 점을 기계 수준 온라인 시뮬레이션 고찰과 물류창고 피킹 디지털 트윈 연구가 함께 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1449",
        "ref-1450"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "Deubert 외(2024, 실제 상태 초기화·전제 조건)와 Galka(WSC 2024, 실부하 상태 동기화로 과도 구간 단축)가 서로 다른 기관·현장에서 같은 요지를 말함. ref-1450 은 초록만 확인",
      "as_of": "2024",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f8",
      "claim": "18. 실시간 세계 상태·데이터 일관성은 현재 상태를 시각·품질 정보와 함께 34. 시뮬레이션·예측용 디지털 트윈의 초기값으로 넘기는 쪽이고, 34번은 그 초기값에서 가정한 미래를 실험하는 쪽으로 나누는 것이 분류 원문의 구분과 위 연구들의 초기화 요건(상태 정의·품질·갱신 빈도)에 맞을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1449",
        "ref-1450"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "트랙 floorplan-recognition 반영 제안 2(실행 2026-09-25-70)가 든 IFAC 2024 연구는 이번에 다시 찾지 못해, 같은 요지의 고찰(ref-1449)과 WSC 2024 연구(ref-1450)로 근거를 대신함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f9",
      "claim": "용인세브란스병원은 한국로봇산업진흥원 AI·5G 기반 서비스로봇 융합모델 실증사업으로 로봇 5종 10대를 들였고, 혈액 이송 로봇이 승강기·스피드게이트·자동문과 연동해 통제 구역과 층 사이를 이동하며, 통합반응상황실의 5G 기반 관제 플랫폼이 로봇 상태와 위치를 실시간으로 모니터링한다고 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1461"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메디포뉴스 2022-11-18 기사: 2단계 실증, LG전자·리드앤·트위니 참여, 승강기·자동문 센서 인터페이스 적용, IRS(통합반응상황실) 5G 통합관제·서비스 플랫폼",
      "as_of": "2022-11-18",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f10",
      "claim": "싱가포르 창이종합병원(CGH)의 RoMi-H 는 제조사가 다른 로봇들이 공통 미들웨어로 병원의 기존 승강기·자동문을 함께 쓰게 하며, 새로 들인 로봇도 기존 승강기·자동문과 연동하도록 설정할 수 있고 긴급한 작업을 하는 로봇에 우선권을 준다고 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1459"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Straits Times(SingHealth 게재, 2022-05-28): CGH 는 2015년 로봇 전용 승강기를 지었으나 \"we can't have different robots requiring different lift systems\"라는 이유로 RoMi-H 를 도입",
      "as_of": "2022-05-28",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f11",
      "claim": "싱가포르 국가 표준 Technical Reference 93(TR 93)은 자율 로봇과 승강기·자동문 같은 건물 설비 사이의 데이터 교환 지침을 정하며, KONE 의 차세대 승강기는 TR 93 에 맞춘 클라우드 연결·개방 API 로 RoMi-H 로봇과 시험 연동되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CGH 보도자료(2022-05-28): CHART 와 HOPE Technik 이 개발, Heartbeat @ Bedok 에서 차세대 승강기와 로봇 연동, The Galen 시험 공간. TR 93 의 상태 갱신 주기·유효 시간 조항은 미확인",
      "as_of": "2022-05-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "연계 대상: Schulze 외(Frontiers in Robotics and AI, 2025-02)의 요양 시설·대학 사무 건물 실증에서 로봇은 승강기 문 상태를 자기 라이다로 직접 판단했고, 승강기 문은 6초만 열려 있었으며, 의도하지 않은 층에서 멈춘 이유를 구분하지 못했고, 119건 작업 가운데 문·승강기가 얽힌 작업의 약 14%가 실패했으며 주된 원인은 위치추정·검출 오류였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1460"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TU Ilmenau, 요양 시설(AWO, 3층 24세대)·대학 건물(Zuse). 승강기 탑승 성공률 93.2%·88.0%, 문 조작 94.8%·88.1%. 문은 \"only stays open for 6 s\", 세 번째 시도 뒤 중단",
      "as_of": "2025-02-25",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "승강기 문처럼 열림 상태가 수 초만 유지되는 설비에서는 '열림' 정보의 허용 경과 시간을 그 설비의 유지 시간보다 짧게 잡아야 하고, 설비가 보고한 상태와 로봇이 직접 관측한 상태를 함께 확인해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1460",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f12 의 6초 개방과 층 정지 이유 구분 불가 사례, LiftState 의 door_state·current_mode·lift_time 필드를 함께 보고 도출한 추정",
      "as_of": "2026-10-09",
      "site_type": "기타",
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "김지형(2023)은 두산 로봇팔(Modbus)과 KUKA 로봇팔(UDP 소켓)을 스마트 커넥터로 OPC UA Pub/Sub 서버에 모아 3D 실시간 디지털 트윈으로 연결했으며, 초당 50개 이상 노드 수집과 약 70 fps 렌더링을 보고했으나 종단 간 지연·동기화 오차 수치는 제시하지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1462",
        "ref-296"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KoreaScience 수록본: 공장 현장 설비 대상 구조(엣지 장치·CPS 서버), 실험은 엣지 1대·서버 1대 실험실 구성, OPC UA 로 'ms 수준' 통신이라고만 서술. 영문 초록은 본문과 다른 주제(협동로봇 안전 가드)로 표기됨",
      "as_of": "2023-08-31",
      "site_type": "제조 공장",
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "같은 논문(DOI 10.7236/JIIBC.2023.23.4.189, 23권 4호 189-196쪽, 발행처 국제인공지능학회)을 KCI 는 지능정보논문지로, KoreaScience 는 한국인터넷방송통신학회논문지로 적어, 게재지 이름 충돌(oq-037)은 같은 논문에 대한 두 등재 정보의 차이로 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-296",
        "ref-1462"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI ART002993454: 학술지명 지능정보논문지, Vol.23 No.4 pp.189-196. KoreaScience: The Journal of the Institute of Internet, Broadcasting and Communication, 2023-08-31. DOI·권호·쪽·발행처 동일",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "OPC UA 의 DataValue 는 값과 함께 데이터 원천이 붙인 시각(sourceTimestamp), 서버가 값을 받거나 정확하다고 안 시각(serverTimestamp), 품질 상태 코드(Good·Uncertain·Bad)를 담고, 클라이언트는 값을 쓰기 전에 최소한 상태 코드의 심각도를 확인해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-288"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OPC 10000-4 7.11: serverTimestamp 는 서버가 값을 받았거나 \"knew it to be accurate\" 시각이며 예외 기반 원천은 값이 안 바뀌어도 주기적으로 갱신. stale 이라는 용어는 없음",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "W3C SOSA 온톨로지는 관측 활동이 끝난 시각(resultTime)과 관측 결과가 대상에 적용되는 시각(phenomenonTime)을 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-030"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "sosa.ttl(W3C/OGC 작업반 저장소 편집자 초안): resultTime = 관측·작동·표본 활동이 완료된 순간, phenomenonTime = 결과가 FeatureOfInterest 에 적용되는 시각. /TR 권고안 문구와 다를 수 있음",
      "as_of": "2017-10-19",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "VDA 5050 3.0.0 에서 로봇 상태 메시지는 관련 사건이 생기거나 최소 30초마다 발행되고, 시각은 ISO 8601 UTC 밀리초 형식이며, 이번에 읽은 범위에서 시계 동기화 요구는 찾지 못했고, connection 토픽은 관제가 로봇 상태 점검에 쓰지 말라고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.6절: \"when relevant events occur or at least every 30 seconds\". 7.2절 timestamp YYYY-MM-DDTHH:mm:ss.fffZ. 4.3절 connection 토픽은 로봇 health 점검용이 아님",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "VDA 5050 3.0.0 에서 관제가 구역·간선 사용 요청을 허가할 때 허가 만료 시각(leaseExpiry)을 붙일 수 있고, 그 시각이 지나면 허가는 무효로 보아 요청 상태를 EXPIRED 로 바꾸며, 관제는 같은 requestId 로 새 만료 시각을 보내 연장한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.4.3·6.9·7.5절: leaseExpiry 는 허가 응답에만, 그 시각까지만 유효. 상태값 REQUESTED·GRANTED·REVOKED·EXPIRED(6.9절은 QUEUED 도 적어 7.8절 열거와 불일치)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f20",
      "claim": "허가에 만료 시각을 붙이는 VDA 5050 의 방식과 연결 상실 시 값을 STALE 로 표시하는 Sparkplug 의 방식을 설비 상태에 적용하면, '문 열림' 같은 관측에 유효 만료 시각을 붙이고 지나면 재확인을 요구하는 규칙으로 허가 경과 시간 문제를 다룰 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-287"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f19 의 leaseExpiry 와 Sparkplug 5장의 NDEATH 수신 시 모든 지표를 STALE 로 표시하는 규정을 묶은 설계 추정. 설비 상태에 적용한 표준·사례는 미확인",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f21",
      "claim": "VDA 5050 3.0.0 은 위치추정 품질 점수(localizationScore)와 편차 범위(deviationRange)를 로그·시각화 용도로만 쓰라고 정하고, 판단에 쓸 수 있는 신호로는 위치추정 여부(localized: true 면 x·y·theta 를 믿을 수 있음)를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "7.8절 mobileRobotPosition: localizationScore [0.0~1.0] \"Only for logging and visualization purposes.\" deviationRange 도 같음. information 배열도 관제 논리에 쓰지 말 것",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "VDA 5050 을 따르는 로봇에 대해 ROP 가 위치를 얼마나 믿을지 판단할 때 품질 점수·편차 범위를 판단 논리로 쓰면 규격의 용도 규정과 어긋나므로, 위치추정 여부와 보고 시각, 그리고 설비·다른 로봇 관측과의 대조를 판단 근거로 삼아야 할 것으로 보이며, 이는 현재 페이지 9절의 '품질 점수·편차 범위로 판단' 서술의 수정이 필요함을 뜻한다(oq-028).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f21 의 용도 제한 규정과 현재 페이지 9절 표('위치추정 여부·품질 점수·편차 범위·지도 id 와 보고 시각을 받아 그 위치를 얼마나 믿을지 판단')를 대조한 결과",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Rosen·Mason·Leonard(ICRA 2016)는 반정적 환경의 특징이 시간이 지나며 남아 있을지 사라질지를 확률 생성 모델로 기술하고, 각 특징이 아직 존재하는지에 대한 믿음을 매 순간 정확히 온라인 계산하는 재귀 베이즈 추정기인 지속성 필터(persistence filter)를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1454"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MIT DSpace 초록: 반정적 특징의 생존 모델이 \"recursive Bayesian estimator, the persistence filter\"를 허용하며, 그래프 기반 지도 작성에 넣어 평생 환경 모델링 틀을 만든다(ICRA 2016, 1063-1070쪽)",
      "as_of": "2016-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Perpetua(Saavedra-Ruiz 외, IROS 2025)는 지속성 필터와 출현 필터를 혼합·연결해 반정적 특징이 사라지거나 다시 나타날 확률을 추정하고, 특징 변화에 대한 사전 지식을 넣고 온라인으로 적응하며, 관측 누락에 강하다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1455"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2507.18808 초록: 'persistence'·'emergence' 필터의 혼합을 이어 다중 가설을 추적, 시뮬레이션·실제 데이터에서 유사 방법보다 정확도가 높았다고 보고",
      "as_of": "2025-07-24",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "지속성 필터 계열 방법은 '몇 초까지 믿는다'는 고정 임계값 대신 마지막 관측 뒤 시간에 따라 상태 믿음을 낮추는 방식으로 오래된 관측을 다룰 수 있게 하지만, 이번에 확인한 적용 대상은 로봇 지도의 특징이며 문·승강기 같은 설비 상태에 적용한 사례는 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1454",
        "ref-1455"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f23·f24 의 적용 범위(지도 특징)와 oq-034 의 질문(설비 상태 허용 경과 시간)을 대조한 추정",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f26",
      "claim": "ISO/TC 299 의 ISO/AWI 26159-2(로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항)는 2025-11-13 신규 과제로 등록된 초안 단계로, 로봇–승강기·로봇–자동문 연동의 최소 데이터 교환·하드웨어 요구·안전 고려사항과 화재 대피 같은 비상 상황, 정전 같은 비정상 상황의 통신을 다루되 특정 메시지 프로토콜은 범위에서 뺀다.",
      "tag": "사실",
      "source_ids": [
        "ref-1456"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 과제 페이지: Stage 20.00(2025-11-13), 작업반 초안 있음, 디지털·접점식 승강기 제어 모두 대상, ISO (DIS) 21423 과 정합 의도. 상태 신선도 요구는 범위 설명에 없음",
      "as_of": "2025-11-13",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "ISO/TC 178 의 ISO/CD TS 8100-11(승강기와 다른 시스템의 상호운용)은 2026-08-28 의견 수렴이 끝난 위원회 초안으로, 원격 감시·원격 호출 등록·건물 자동화 연동·로봇(AGV·MAR) 연동의 네 사용 사례를 위한 승강기 상호운용 온톨로지와 안전 관련 기능을 정하고 oneM2M·OPC UA 를 적용 예로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1457"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 과제 페이지: Stage 30.60(2026-08-28), CD 등록 2026-07-01. 범위 설명에 상태 유효 시간·갱신 주기 언급 없음",
      "as_of": "2026-08-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "2026-10-09 기준 로봇–승강기·자동문 인터페이스의 국제 표준은 초안 단계이고 공개된 범위 설명과 싱가포르 TR 93 소개 자료 어디에도 설비 상태를 몇 초까지 믿을지 정한 내용은 보이지 않아, oq-034 는 여전히 열린 질문으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1456",
        "ref-1457",
        "ref-1458"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f26·f27·f11 의 범위·소개 문구 대조. 표준 본문(유료·초안)은 열지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f29",
      "claim": "Yang·Liew(arXiv, 2025-10)는 정밀 시간 프로토콜(PTP)로 로봇들의 운영체제 시계를 마이크로초 수준으로 맞췄지만, 로봇 컴퓨터(NUC 11)의 무선랜 카드가 PTP 에 필요한 하드웨어 시각 기록을 지원하지 않아 실험 전에 유선 이더넷으로 동기화했다고 적었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1463"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2510.02624v2 실험 절: PTP 로 \"microsecond-level accuracy\", WiFi NIC 하드웨어 타임스탬프 미지원으로 유선 LAN 에서 사전 동기화(홍콩중문대)",
      "as_of": "2025-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "Sparkplug 사양은 MQTT 브로커가 유언 메시지로 대신 보낸 노드 종료(NDEATH)의 시각은 실제 종료 시각이 아니므로 호스트가 자기 수신 UTC 시각으로 오프라인을 표시하게 하고, 이를 위해 엣지 노드와 호스트의 시계를 NTP 같은 방법으로 맞추도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-287"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "5장 Timestamps·Edge Node Session Termination: 모든 시각은 UTC, NDEATH 는 \"timestamp of receipt\" 를 써야 하며 이 때문에 시계 동기화가 필요(NTP 예시)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f31",
      "claim": "무선으로 연결된 이기종 로봇은 마이크로초 수준 동기화를 기대하기 어렵고 VDA 5050 이 시계 동기화를 요구하지 않으므로, ROP 는 로봇이 붙인 시각과 자기 수신 시각을 함께 기록하고 둘의 차이로 시계 오차를 추정해 상태의 경과 시간을 계산하는 방식이 필요할 것으로 보인다(oq-035).",
      "tag": "추정",
      "source_ids": [
        "ref-1463",
        "ref-031",
        "ref-287"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f29(무선 PTP 한계), f18(VDA 5050 시각 형식만 규정), f30(Sparkplug 수신 시각 규정)을 묶은 설계 추정. 허용 시계 오차를 정한 자료는 미확인",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-030",
      "org": "W3C / OGC",
      "title": "Semantic Sensor Network Ontology",
      "published": "2017-10-19",
      "url": "https://www.w3.org/TR/vocab-ssn/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "센서 관측·작동 온톨로지(SSN/SOSA). 이번에는 공식 작업반 저장소의 편집자 초안 sosa.ttl 을 열어 resultTime·phenomenonTime 정의를 확인했다(권고안 문구와 다를 수 있음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": "https://raw.githubusercontent.com/w3c/sdw/gh-pages/ssn/integrated/sosa.ttl",
      "source_unopened": true
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문. 상태 발행 주기, 시각 형식, 연결 토픽, 허가 만료 시각(leaseExpiry), 위치추정 품질 필드의 용도 제한을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 상태 메시지 JSON 스키마. timestamp(ISO 8601), 위치·적재물·운용 모드·안전 상태 필드.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 승강기 상태 메시지. lift_time, 문 상태, 운행 상태, 운영 모드(사람·AGV·화재·오프라인·비상), 세션 id.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-287",
      "org": "Eclipse Foundation (eclipse-sparkplug GitHub)",
      "title": "Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc)",
      "published": null,
      "url": "https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Sparkplug 운영 동작. UTC 시각과 시계 동기화, NDEATH 수신 시각 사용, 연결 상실 시 STALE 품질 표시.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-288",
      "org": "OPC Foundation",
      "title": "OPC Unified Architecture – Part 4: Services - 7.11 DataValue",
      "published": null,
      "url": "https://reference.opcfoundation.org/specs/OPC-10000-4/7.11",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OPC UA DataValue 구조. sourceTimestamp·serverTimestamp·statusCode 의 의미와 클라이언트의 상태 코드 심각도 확인 의무를 이번 실행에서 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://reference.opcfoundation.org/specs/OPC-10000-4/7.11",
      "source_unopened": false
    },
    {
      "id": "ref-296",
      "org": "김지형",
      "title": "OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현",
      "published": "2023",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "KCI 등재 정보. 학술지명을 지능정보논문지(23권 4호, 189-196쪽, DOI 10.7236/JIIBC.2023.23.4.189, 국제인공지능학회)로 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454",
      "source_unopened": false
    },
    {
      "id": "ref-1449",
      "org": "Deubert, D., Klingel, L., & Selig, A. (arXiv; The International Journal of Advanced Manufacturing Technology 2024 표기)",
      "title": "Online Simulation at Machine Level: A Systematic Review",
      "published": "2024-01-15",
      "url": "https://arxiv.org/abs/2401.07841",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "65편을 검토한 기계 수준 온라인 시뮬레이션 체계적 고찰. 실제 상태 초기화의 전제 조건과 초기화 전략(상위 시뮬레이션 복제·센서 측정·관측기·혼합)을 정리한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2401.07841v2",
      "source_unopened": false
    },
    {
      "id": "ref-1450",
      "org": "Galka, S. (Winter Simulation Conference 2024)",
      "title": "Reducing Transient Behavior in Simulation-Based Digital Twins: A Novel Initialization Approach for Order Picking Systems",
      "published": "2024",
      "url": "https://informs-sim.org/wsc24papers/con211.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. SAP EWM 을 쓰는 주문 피킹 시스템의 시뮬레이션 기반 디지털 트윈을 실부하 상태로 초기화해 과도 구간을 줄이는 방법(검색 결과의 초록 기준, PDF 본문 추출 실패).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1451",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 차선 열기·닫기 요청 메시지 정의(fleet_name, open_lanes, close_lanes).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "source_unopened": false
    },
    {
      "id": "ref-1452",
      "org": "Open Robotics Discourse (open-rmf 질의응답 #414)",
      "title": "How to inform RMF that lift or door are not available? (#414)",
      "published": "2024-01-13",
      "url": "https://discourse.openrobotics.org/t/how-to-inform-rmf-that-lift-or-door-are-not-available-414/44744",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "정비 중인 승강기·문을 RMF 에 알리는 방법에 대한 질의응답. 유지관리자가 차선 폐쇄와 lift_states OFFLINE 감시를 권한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://discourse.openrobotics.org/t/how-to-inform-rmf-that-lift-or-door-are-not-available-414/44744",
      "source_unopened": false
    },
    {
      "id": "ref-1453",
      "org": "Open Robotics (open-rmf, rmf_traffic API 문서)",
      "title": "Class LaneClosure — rmf_traffic API documentation",
      "published": null,
      "url": "https://openrmf.readthedocs.io/projects/rmf-traffic/en/latest/api/classrmf__traffic_1_1agv_1_1LaneClosure.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "그래프 안 차선의 열림·닫힘 상태를 기술하는 LaneClosure 클래스의 API 설명.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://openrmf.readthedocs.io/projects/rmf-traffic/en/latest/api/classrmf__traffic_1_1agv_1_1LaneClosure.html",
      "source_unopened": false
    },
    {
      "id": "ref-1454",
      "org": "Rosen, D. M., Mason, J., & Leonard, J. J. (MIT DSpace; ICRA 2016)",
      "title": "Towards lifelong feature-based mapping in semi-static environments",
      "published": "2016-06",
      "url": "https://dspace.mit.edu/handle/1721.1/107620",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "반정적 환경 특징의 지속 여부를 추정하는 재귀 베이즈 추정기 지속성 필터를 제시한 ICRA 2016 논문(저장소 초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://dspace.mit.edu/handle/1721.1/107620",
      "source_unopened": false
    },
    {
      "id": "ref-1455",
      "org": "Saavedra-Ruiz, M., Nashed, S. B., Gauthier, C., & Paull, L. (arXiv; IROS 2025 채택 표기)",
      "title": "Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static Environments",
      "published": "2025-07-24",
      "url": "https://arxiv.org/abs/2507.18808",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "지속성·출현 필터를 혼합해 반정적 특징의 소멸·재출현 확률을 추정하는 방법(초록 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2507.18808",
      "source_unopened": false
    },
    {
      "id": "ref-1456",
      "org": "ISO (ISO/TC 299 Robotics)",
      "title": "ISO/AWI 26159-2 Robotics — Infrastructure for robot applications — Part 2: Requirements for interfacing with lifts (elevators) and automatic doorways",
      "published": null,
      "url": "https://www.iso.org/standard/92741.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "로봇–승강기·자동문 연동 요구사항 표준 과제 페이지(Stage 20.00, 2025-11-13). 범위 설명만 확인했고 초안 본문은 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.iso.org/standard/92741.html",
      "source_unopened": false
    },
    {
      "id": "ref-1457",
      "org": "ISO (ISO/TC 178 Lifts, escalators and moving walks)",
      "title": "ISO/CD TS 8100-11 Lifts for the transport of persons and goods — Part 11: Interoperability between lift and other systems",
      "published": null,
      "url": "https://www.iso.org/standard/73063.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "승강기 상호운용 온톨로지 기술 시방서 위원회 초안 과제 페이지(Stage 30.60, 2026-08-28). 범위 설명만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.iso.org/standard/73063.html",
      "source_unopened": false
    },
    {
      "id": "ref-1458",
      "org": "Changi General Hospital (CGH)",
      "title": "Changi General Hospital, CapitaLand Investment and KONE collaborate to advance the integration of robotics in buildings",
      "published": "2022-05-28",
      "url": "https://www.cgh.com.sg/news/announcements/changi-general-hospital-capitaland-investment-and-kone-collaborate-to-advance-the-integration-of-robotics-in-buildings",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "싱가포르 공공병원 보도자료. 로봇–건물 설비 데이터 교환 국가 표준 TR 93 과 KONE 승강기 연동 시험 공간을 소개한다(보도자료).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.cgh.com.sg/news/announcements/changi-general-hospital-capitaland-investment-and-kone-collaborate-to-advance-the-integration-of-robotics-in-buildings",
      "source_unopened": false
    },
    {
      "id": "ref-1459",
      "org": "The Straits Times (SingHealth 게재, Wong Shiying)",
      "title": "New software enables different robots to communicate with each other and building infrastructure",
      "published": "2022-05-28",
      "url": "https://www.singhealth.com.sg/news/tomorrows-medicine/new-software-enables-different-robots-to-communicate-with-each-other-and-building-infrastructure",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "CGH 의 RoMi-H 로 제조사가 다른 로봇이 기존 승강기·자동문을 함께 쓰게 된 배경을 다룬 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.singhealth.com.sg/news/tomorrows-medicine/new-software-enables-different-robots-to-communicate-with-each-other-and-building-infrastructure",
      "source_unopened": false
    },
    {
      "id": "ref-1460",
      "org": "Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau; Frontiers in Robotics and AI)",
      "title": "On realizing autonomous transport services in multi story buildings with doors and elevators",
      "published": "2025-02-25",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "요양 시설·대학 건물에서 문·승강기를 지나는 자율 운반 서비스 실증. 문·승강기 상태 판단 방식, 실패 원인, 작업 성공률을 보고한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full",
      "source_unopened": false
    },
    {
      "id": "ref-1461",
      "org": "메디포뉴스 (이형규)",
      "title": "용인세브란스병원, 지능형 의료서비스로봇 생태계 구축",
      "published": "2022-11-18",
      "url": "https://medifonews.com/news/article.html?no=172554",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "용인세브란스병원의 AI·5G 기반 서비스로봇 융합모델 실증(5종 10대, 승강기·자동문·스피드게이트 연동, 5G 통합 관제) 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://medifonews.com/news/article.html?no=172554",
      "source_unopened": false
    },
    {
      "id": "ref-1462",
      "org": "김지형 (KoreaScience 수록, 한국인터넷방송통신학회논문지 표기)",
      "title": "OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 (Design and Implementation of Real-time Digital Twin in Heterogeneous Robots using OPC UA)",
      "published": "2023-08-31",
      "url": "https://koreascience.or.kr/journal/view.jsp?kj=OTNBBE&py=2023&vnc=v23n4&sp=189",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "DOI 10.7236/JIIBC.2023.23.4.189 가 가리키는 KoreaScience 수록본. OPC UA 기반 이기종 로봇팔 실시간 디지털 트윈 구조와 수집·렌더링 성능을 다룬다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://koreascience.or.kr/journal/view.jsp?kj=OTNBBE&py=2023&vnc=v23n4&sp=189",
      "source_unopened": false
    },
    {
      "id": "ref-1463",
      "org": "Yang, Q., & Liew, S. C. (The Chinese University of Hong Kong, arXiv)",
      "title": "Multi-robot Rigid Formation Navigation via Synchronous Motion and Discrete-time Communication-Control Optimization",
      "published": "2025-10-10",
      "url": "https://arxiv.org/abs/2510.02624",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "다중 로봇 대형 주행 연구. 실험에서 PTP 시계 동기화를 무선랜 하드웨어 제약 때문에 유선 이더넷으로 수행한 사실을 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2510.02624",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "갱신(update) 차등 반영. 5절 적용 사례(현장 유형 명시): 병원 사례 f9(용인세브란스, 한국)·f10(CGH RoMi-H), 기타 현장 사례 f12·f13(요양 시설·대학 건물, 연계 대상 표시), 제조 공장 사례 f14 — 물류창고 외 현장 유형 보강 / 6절 대표 접근법: f16(OPC UA 원천·서버 시각과 품질 코드), f17(SOSA 관측 시각 구분), f19·f20(허가 만료 시각 방식), f23~f25(지속성 필터 계열), f29~f31(시계 동기화와 수신 시각) / 7절 표준: f26·f27(ISO 초안 2건), f11(싱가포르 TR 93), f16(ref-288 원문 확인), f18·f19·f21(VDA 5050 3.0.0) / 8절 연구: f5~f7(온라인 시뮬레이션 초기화), f12, f14, f23·f24, f29 / 9절 책임 경계: f21·f22 — 현재 표의 '품질 점수·편차 범위로 신뢰 판단' 서술이 VDA 5050 의 '로그·시각화 전용' 규정과 어긋나므로 위치추정 여부·보고 시각·교차 관측 기준으로 고칠 것 / 10절 연결: 트랙 floorplan-recognition 단계 3 반영 제안 2건 검토 결과 — 제안 1(실행 2026-09-25-65) → f1~f4(5. 로봇 능력·작업 표현·15. 지도·공간·위치 모델의 정적 대조와 이 영역의 현재 상태 층 분리, 22. 설비·건물 시스템 연동·27. 다중 로봇 경로·교통 관리 — MAPF 와 차선 폐쇄로 연결; 제안 원문의 f20 어포던스 연구는 이번에 재확인하지 못해 제외), 제안 2(실행 2026-09-25-70) → f5~f8(34. 시뮬레이션·예측용 디지털 트윈에 현재 상태 초기값 공급; 제안이 든 IFAC 2024 연구는 재확인하지 못해 ref-1449·ref-1450 으로 대체, 제안의 옛 번호 '8.'·'22.'는 새 번호 18·34 로 표기) / 11절 열린 질문: oq-034 에 f26~f28, oq-035 에 f18·f29~f31, oq-028 에 f21·f22, oq-037 에 f15 부분 근거(해결 제안 없음)와 새 질문 3건. 다음 실행 후보: 15. 지도·공간·위치 모델 페이지의 위치추정 신뢰도 서술에 f21 반영 검토."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "지속성 필터",
      "term_en": "Persistence Filter",
      "definition": "반정적 환경의 특징이 마지막 관측 뒤에도 아직 남아 있을 확률을 시간에 따라 재귀적으로 계산하는 베이즈 추정기다."
    },
    {
      "term_ko": "허가 만료 시각",
      "term_en": "Lease Expiry (VDA 5050 leaseExpiry)",
      "definition": "VDA 5050 에서 관제가 구역·간선 사용 허가에 붙이는 만료 시각으로, 이 시각이 지나면 허가는 무효가 되어 요청 상태가 EXPIRED 로 바뀐다."
    },
    {
      "term_ko": "온라인 시뮬레이션",
      "term_en": "Online Simulation",
      "definition": "운영 중인 실제 시스템의 현재 상태로 초기화하거나 동기화해 가까운 미래의 결과를 예측하는 데 쓰는 시뮬레이션이다."
    },
    {
      "term_ko": "정밀 시간 프로토콜",
      "term_en": "Precision Time Protocol (PTP, IEEE 1588)",
      "definition": "네트워크로 연결된 장치들의 시계를 하드웨어 시각 기록의 도움을 받아 마이크로초 이하 수준으로 맞추는 시계 동기화 프로토콜이다."
    }
  ],
  "open_questions_new": [
    "로봇이 직접 관측한 승강기·문 상태와 설비 제어기가 보고한 상태가 다를 때 어느 쪽을 기준으로 통과·탑승을 확정하는지 정한 표준이나 현장 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 22. 설비·건물 시스템 연동 | 근거: f13 | 종류: 일반",
    "지속성 필터처럼 마지막 관측 뒤 시간에 따라 믿음을 낮추는 확률 모델을 문·승강기·충전기 같은 설비 상태의 허용 경과 시간 판단에 적용한 연구나 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 46. 예측·학습 기반 최적화 | 근거: f25 | 종류: 일반",
    "실시간 세계 상태를 예측 시뮬레이션의 초기값으로 넘길 때 어떤 상태 항목·품질·시각 정보를 넘겨야 하는지 정한 인터페이스가 다중 이동로봇 운영에 쓰인 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f8 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 22,
    "cross_checked_count": 1,
    "unverified": [
      "트랙 반영 제안 2가 든 IFAC 2024 연구(운영 중 예측 시뮬레이션의 실부하 상태 초기화)를 다시 찾지 못해 다른 출처로 대체함",
      "트랙 반영 제안 1의 어포던스 상태 연구(트랙 실행 2026-09-25-65 의 f20)를 재확인하지 못해 이번 브리프에 넣지 않음",
      "ref-1450 Galka(WSC 2024) PDF 본문 추출 실패, 초록(검색 결과) 범위로만 사용하고 개선 폭 수치 미확인",
      "ISO/AWI 26159-2·ISO/CD TS 8100-11·싱가포르 TR 93 본문 미열람(초안·유료), 상태 신선도 조항 유무 미확인",
      "f9 용인세브란스 사례는 기사 1건 기준이며 교차 확인 못함",
      "f15 oq-037: KCI 와 KoreaScience 가 같은 DOI·권호·쪽·발행처에 서로 다른 학술지명을 적어, 어느 이름이 현재 공식 명칭인지(학술지 명칭 변경 여부) 미확인",
      "VDA 5050 3.0.0 명세 마지막 7,761자는 읽지 않음",
      "국내 로봇–승강기 연동 TTA·KS 표준의 상태 갱신 주기·응답 시간 항목 미확인"
    ],
    "scope_violations": [
      "f12: 승강기 문 상태 라이다 검출·위치추정은 분류 원문 19장 '로봇 자체 지능·제어' 경계라 claim 을 '연계 대상: '으로 시작하고, ROP 쪽 함의는 f13 에서 상태 대조 규칙으로만 서술",
      "f26·f27·f11: 승강기·자동문 제어와 비상 운전은 '시설·설비 제어' 경계의 연계 대상이며, 이 브리프는 데이터 교환 항목(ROP 가 받는 상태)의 범위로만 다룸",
      "f29: 로봇 내부 시계·네트워크 카드는 제조사 몫이며 ROP 는 수신 시각 기록·오차 추정(f31)만 맡는 것으로 서술"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 실행 유형 update 이므로 정정 요청(없음)·빈 절·트랙 반영 제안 2건·대상 영역 열린 질문(oq-028·oq-034·oq-035·oq-037)에 해당하는 것만 조사했다. 검색 15회/30, 신규 출처 15건/15(ref-1449~ref-1463, 예약 구간 안)로 신규 출처 상한에 도달해, 더 찾지 않은 것: 국내 TTA·KS 로봇–승강기 연동 표준 본문, 상업 시설 현장의 상태 통합 사례, 시계 동기화 허용 오차 기준. 신규 출처 가운데 ref-1450 을 뺀 14건은 원문(또는 초록 페이지)을 열었다. 재사용 7건 가운데 ref-031(github_raw)·ref-030(github_raw, 편집자 초안 공식 산출물)·ref-288·ref-296(webfetch)은 이번에 열었고, ref-051·ref-286·ref-287 은 입력의 원문 텍스트(data/source_texts)를 읽었다. 교차 확인 1건(f7: 온라인 시뮬레이션 실제 상태 초기화, 단 ref-1450 은 초록만). 벤더 주장 없음. 한국 자료: ref-1461(용인세브란스, 병원), ref-1462·ref-296(김지형 2023, 제조 공장). 현장 유형: 물류창고(f6), 병원(f9·f10), 제조 공장(f14), 기타(f12·f13 요양 시설·대학 건물). 18. 실시간 세계 상태·데이터 일관성(현재 상태 공급)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 f8 에서 구분했다. 트랙 반영 제안 처리: 제안 1(2026-09-25-65) → f1~f4, 제안 2(2026-09-25-70) → f5~f8, 제안 문구의 옛 번호(6·5·8·22)는 새 번호(15·5·18·34)로 바꿔 적었다. 열린 질문 oq-028(f21·f22), oq-034(f26~f28), oq-035(f18·f29~f31), oq-037(f15)에는 부분 근거만 더했고 해결 제안은 없다. f21 은 현재 페이지 9절 표의 서술(품질 점수·편차 범위로 신뢰 판단)과 VDA 5050 원문이 어긋날 수 있음을 보이므로 9절 수정을 제안했다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md

```markdown
---
title: "18. 실시간 세계 상태·데이터 일관성"
type: area
category: "E. 사물·사람·실시간 상태"
area_no: 18
related_areas: [5, 15, 17, 20, 22, 27, 34, 38, 42]
tags: [세계 상태, 정보 나이, 발생 시각과 기록 시각, 상태 품질, 정정 이벤트]
status: published
confidence: low
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-030, ref-031, ref-044, ref-045, ref-051, ref-148, ref-282, ref-283, ref-284, ref-285, ref-286, ref-287, ref-288, ref-289, ref-290, ref-291, ref-292, ref-293, ref-294, ref-295, ref-296]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [E. 사물·사람·실시간 상태](index.md) › 18. 실시간 세계 상태·데이터 일관성

# 18. 실시간 세계 상태·데이터 일관성

!!! info "소속 대분류"
    [E. 사물·사람·실시간 상태](index.md) — 핵심 질문:
    작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

이번에 확인한 표준·프레임워크는 시각 필드·주기 발행·메시지 수명·생존성·STALE 표시 같은 장치만 주고 대상별 허용 경과 시간은 정하지 않으므로, 30초 전 '문 열림' 정보로 지금 통과를 확정할지는 ROP가 문·승강기 같은 대상마다 허용 경과 시간을 정하고 이를 넘으면 설비 어댑터에 다시 확인하는 규칙으로 답해야 할 것으로 보인다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 왜 중요한가](../../topics/2026/2026-09-25-area08-s3.md)에 있다.

## 4. 핵심 개념과 용어

- **정보 나이(Age of Information, AoI)** — 시각 표시된 상태 갱신을 받는 쪽의 정보가 얼마나 최신인지를 재는 지표로, 저지연 사이버물리 시스템의 설계·최적화 연구에서 평가 방법이 정리되어 있다(2021-05 서베이 기준). [사실][^ref-289]
- **발생 시각과 기록 시각** — GS1 EPCIS 2.0 온톨로지는 캡처 애플리케이션이 이벤트가 일어났다고 주장하는 시각(eventTime), 저장소가 이벤트를 기록한 시각(recordTime), 발생 장소의 UTC 차이(eventTimeZoneOffset)를 구분한다. [사실][^ref-045]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area08-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 이 영역은 두 시나리오 모두에서 상태가 언제의 것이고 얼마나 믿을 만한지를 판단하는 제약과 완료·인계 칸에 주로 관여한다.

### 시나리오 1. 입고한 팔레트를 문과 승강기를 지나 적치

**물류 흐름 단계:** 입고 → 적치

**시나리오:** 입고한 팔레트를 방화문과 화물 승강기를 지나 보관 구역으로 운반

| 항목 | 내용 |
|---|---|
| 시작 조건 | 입고 확정된 팔레트에 대해 WMS가 적치 작업을 내린다(설명용 가정). |
| 작업 대상 | 팔레트 1개. VDA 5050 상태 스키마는 로봇이 취급 중인 적재물(loads)을 담으므로 로봇이 실제로 무엇을 싣고 있는지 보고받을 수 있다(3.0.0 판, 공식 저장소 main 기준, 확인일 2026-09-25). [사실][^ref-051] |
| 수행 자원 | 운반 로봇, 문·승강기 어댑터, 연계 대상인 설비 제어. Open-RMF 로봇 상태는 밀리초 단위 시각, 위치, 상태 7종, 문제 목록, 배터리 충전 상태를 한 메시지에 담는다. [사실][^ref-148] |
| 제약 | 이번에 연 Open-RMF 문·승강기 연동 문서 범위에서는 상태 발행 주기나 오래된 상태를 판정하는 규칙을 찾지 못했고, 메시지 정의에는 시각 필드만 있다. [추정][^ref-283][^ref-284] 승강기 상태에는 운영 모드(사람·AGV·화재·오프라인·비상)와 세션 id 가 있다. [사실][^ref-286] |
| 완료·인계 | 입고 단계의 RFID 판독 스트림은 누락·오판독이 섞여 미들웨어 정제가 필요하다. [사실][^ref-293] EPCIS 2.0 온톨로지는 발생 시각(eventTime)과 기록 시각(recordTime)을 구분한다. [사실][^ref-045] |
| 예외·성과 | 로봇 연결이 예기치 않게 끊기면 로봇이 연결 때 등록한 MQTT 유언으로 브로커가 CONNECTION_BROKEN 을 대신 알린다(VDA 5050 3.0.0 판, 공식 저장소 main 기준, 확인일 2026-09-25). [사실][^ref-031] 처리량·시간·비용에 주는 영향 수치는 미확인이다. |

로봇이 방화문 앞에 도착했을 때 ROP가 가진 문 상태가 오래전에 받은 '열림'이라면, 허용 경과 시간을 넘긴 값으로 통과를 확정하지 말고 문 어댑터에 다시 확인해야 할 것으로 보인다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289] 승강기도 같은 방식으로 운영 모드가 화재·비상으로 바뀌지 않았는지 최신 상태로 확인한 뒤 탑승을 확정하는 흐름이 될 것으로 보인다. [추정][^ref-286]

### 시나리오 2. 보충 중 재고 기록과 실물의 불일치

**물류 흐름 단계:** 보충

**시나리오:** 피킹 위치를 보충하러 간 로봇이 WMS 기록과 다른 적재물을 보고

| 항목 | 내용 |
|---|---|
| 시작 조건 | WMS 재고 기록상 피킹 위치 수량이 기준 아래로 내려가 보충 작업이 생긴다(설명용 가정). |
| 작업 대상 | 보충용 케이스·팔레트. 로봇이 보고한 적재물과 WMS 기록을 함께 보관해 불일치를 드러내야 할 것으로 보인다. [추정][^ref-292][^ref-051] |
| 수행 자원 | 보충 로봇과 불일치를 확인하는 재고 담당자(설명용 가정). |
| 제약 | 해당 없음 |
| 완료·인계 | 잘못 들어온 완료 보고는 덮어쓰지 않고 정정 기록을 덧붙여야 원 기록과 정정 근거를 함께 추적할 수 있을 것으로 보인다. [추정][^ref-045][^ref-044] |
| 예외·성과 | 소매 자료에서 유추한 것이다: 한 소매업체 37개 매장 재고 기록의 65%가 실물과 맞지 않았다는 보고가 있으나, 이는 소매 매장 조건이며 물류센터 값이 아니다. [사실][^ref-292] 물류센터 재고 기록 정확도는 미확인이다. |

이 시나리오의 불일치 빈도는 소매 연구에서 유추한 것일 뿐이다. 물류센터에서 로봇 관측으로 WMS 재고를 정정한 공개 사례는 이번 조사에서 확인하지 못했다.

## 6. 대표 접근법과 기술

상태의 오래됨을 판정하는 기본 장치는 발행 주기·기한·수명·생존성이며, ROS 2 QoS 는 이를 정책으로 두고 기한 초과·생존성 상실·변경을 이벤트 콜백으로 알린다(Jazzy 판 문서 기준). [사실][^ref-282]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area08-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

아래 표준·프레임워크는 상태에 시각·품질·연결 정보를 붙이는 장치를 제공하지만, 대상별 허용 경과 시간은 어느 것도 정하지 않는다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area08-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 연구 자료는 정보의 신선도 지표, 기록과 실물의 불일치, 판독 정제, 복제 상태의 수렴, 디지털 표현의 분류로 나뉜다.

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 대표 연구와 자료](../../topics/2026/2026-09-25-area08-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP의 직접 범위는 로봇 관제 인터페이스(VDA 5050·Open-RMF)의 로봇 상태, 설비 어댑터의 문·승강기 상태, EPCIS 같은 업무 이벤트를 시각·품질 정보와 함께 하나의 세계 상태로 모으고 불일치를 드러내는 것이며, 설비 자체 제어와 센서 융합은 외부에 맡기는 경계가 될 것으로 보인다. [추정][^ref-031][^ref-283][^ref-045]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 보고한 위치추정 여부·품질 점수·편차 범위·지도 id 와 보고 시각을 받아 그 위치를 얼마나 믿을지 판단한다. [추정][^ref-051] | 연계 대상: 로봇의 위치추정과 그 품질 계산, 센서 융합 |
| 시설·설비 제어 | 문·승강기 상태를 시각과 함께 받아 오래됨을 판정하고, 허용 경과 시간을 넘으면 통과 확정 전에 재확인을 요청한다. [추정][^ref-031][^ref-282][^ref-287][^ref-283][^ref-289] | 연계 대상: 문·승강기 자체 제어와 설비 안전 제어. Open-RMF 에서는 문·승강기 어댑터가 로봇 작업을 방해할 요청을 막는다. [사실][^ref-283][^ref-284] |
| 상위 업무 시스템 | 업무 이벤트를 발생·기록 시각과 함께 세계 상태에 모으고 로봇 관측과의 불일치를 드러낸다. [추정][^ref-031][^ref-283][^ref-045] | 연계 대상: 전사 재고정책 |

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 이종 제조사를 연결하는 ROP라면 위치추정·설비 제어는 제조사와 설비에 맡기고, 받은 상태를 얼마나 믿을지 판단하는 규칙과 재확인 절차를 인터페이스로 맡는 구성이 된다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 현재 상태 표현은 현장과 자동으로 동기화되는 표현(디지털 섀도, ISO 23247 의 동기화된 표현)에 가깝고, 그 표현을 복제해 가정한 미래를 실험하는 쪽은 34. 시뮬레이션·예측용 디지털 트윈의 몫으로 나누는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거 자료는 제조 대상). [추정][^ref-291][^ref-290]

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area08-s10.md)에 있다.

## 11. 열린 질문

이 영역의 가장 큰 공백은 대상별 허용 경과 시간의 근거이며, 아래 질문은 [열린 질문](../../open-questions.md) 목록에도 있다.

자세한 내용은 주제 페이지 [18. 실시간 세계 상태·데이터 일관성 — 열린 질문](../../topics/2026/2026-09-25-area08-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 영역 심화: 섹션 3~11 신규 작성, 페이지 상태 자동 영역 표식 추가, 1차 조건부 승인 수정 14건 이행, 2차 수정: 5절 승강기 추론 문장에 [추정] 태그·각주 추가, 완료·인계 칸 EPCIS 문장을 사실 부분만 남김 (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area08-s7.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,454자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area08-s4.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "4. 핵심 개념과 용어" 절(1,436자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area08-s6.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "6. 대표 접근법과 기술" 절(1,386자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-24)
- 2026-09-25 · 생성 · [18. 실시간 세계 상태·데이터 일관성 — 대표 연구와 자료](../../topics/2026/2026-09-25-area08-s8.md) — 자동 분리: 8. 실시간 세계 상태·데이터 일관성 의 "8. 대표 연구와 자료" 절(1,250자)을 옮겼다. 2차 수정: Yates 외 항목에서 브리프에 없는 평가 문장을 뺐다 (실행 2026-09-25-24)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-09-25
[^ref-289]: Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S., Age of Information: An Introduction and Survey, 2021-05, https://arxiv.org/abs/2007.08564, 접근일 2026-09-25 (원문 미열람)
[^ref-290]: NIST, DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH, 미확인, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-292]: DeHoratius, N., & Raman, A., Inventory Record Inaccuracy: An Empirical Analysis, 2008, https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789, 접근일 2026-09-25 (원문 미열람)
[^ref-293]: Massawe, L. V. 외(Sensors), Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach, 2012-03-28, https://doi.org/10.3390/s120404187, 접근일 2026-09-25 (원문 미열람)
```

### data/area_reflection_proposals.json (대상 영역 18. 실시간 세계 상태·데이터 일관성 에 대한 트랙 반영 제안 2건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-65",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 18,
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "summary": "정적 능력 대조(6. 지도·공간·위치 모델, 5. 로봇 능력·작업 온톨로지)와 현재 상태 층(문 상태, Open-RMF LaneRequest 차선 폐쇄)을 분리해야 한다는 점(추정, f23)과 어포던스 상태로 막힌 경로를 설명하는 연구(f20).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-70",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 18,
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "summary": "운영 중 예측 시뮬레이션은 실제 부하 상태로 초기화해야 한다는 연구(IFAC 2024)와, 8. 실시간 세계 상태·데이터 일관성이 22. 시뮬레이션·예측용 디지털 트윈에 현재 상태 초기값을 공급하는 쪽이라는 구분(추정)",
      "status": "제안"
    }
  ]
}
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

### docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md (요약)

```markdown
# 34. 시뮬레이션·예측용 디지털 트윈

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

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
```

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md (요약)

```markdown
# 42. 분산 시스템·통신·컴퓨팅 구조

소속 대분류: K. 플랫폼 아키텍처·인프라 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 네트워크**: 와이파이 로밍·5G·사설망, 지연·대역폭·음영 구역을 설계하고 점검한다
- **연결이 끊겨도 계속 운영**: 인터넷이나 서버가 끊겨도 현장에서 어디까지 계속 운영할지 정하고 구현한다
- **다현장 운영 구조**: 여러 현장을 한 플랫폼에서 나누어 운영하는 구조를 만든다
- **확장성·성능**: 로봇과 작업 수가 늘어도 처리 성능을 유지한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 [옛 분류원문]

> 옛 질문: 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [옛 분류원문]

## 2. 핵심 질문

인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 22건 / 전체 1262건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | https://www.w3.org/TR/vocab-ssn/ | 2026-09-25 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 2026-09-25 | 예 |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl | 2026-09-25 | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 2026-09-25 | 예 |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 미확인 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html | 2026-09-25 | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 2026-09-25 | 예 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 2026-09-25 | 예 |
| ref-285 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg | 2026-09-25 | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 2026-09-25 | 예 |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 미확인 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc | 2026-09-25 | 예 |
| ref-288 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 미확인 | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 | 2026-09-25 | 아니오 |
| ref-289 | Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. | Age of Information: An Introduction and Survey | 2021-05 | https://arxiv.org/abs/2007.08564 | 2026-09-25 | 아니오 |
| ref-290 | NIST | DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH | 미확인 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 | 2026-09-25 | 아니오 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 2026-09-25 | 아니오 |
| ref-292 | DeHoratius, N., & Raman, A. | Inventory Record Inaccuracy: An Empirical Analysis | 2008 | https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789 | 2026-09-25 | 아니오 |
| ref-293 | Massawe, L. V. 외(Sensors) | Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach | 2012-03-28 | https://doi.org/10.3390/s120404187 | 2026-09-25 | 아니오 |
| ref-294 | 이동건, 송승현, 이찬혁, 노상도, 윤상문, 이현영(한국CDE학회 논문집) | 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 | 2021-12 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002781294 | 2026-09-25 | 아니오 |
| ref-295 | Preguiça, N., Baquero, C., & Shapiro, M. | Conflict-free Replicated Data Types (CRDTs) | 2018-05 | https://arxiv.org/abs/1805.06358 | 2026-09-25 | 아니오 |
| ref-296 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 2023 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 | 2026-09-25 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 358개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
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
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
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
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
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

### docs/open-questions.md (요약: 대상 영역 [18] 에 걸린 10건 / 전체 309건)

```markdown
- oq-024 [열림] 제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가? (영역 5, 18, 25)
- oq-028 [열림] 제조사마다 계산 방식이 다른 위치추정 신뢰도(VDA 5050 localizationScore 등)나 신뢰도 필드가 없는 로봇의 위치 보고를 ROP 가 같은 기준으로 수용·거부하는 방법이 있는가? (영역 15, 18)
- oq-034 [열림] 문·승강기·충전기 같은 설비 상태 정보를 몇 초까지 믿고 통과·배정을 확정할지 정한 표준이나 국내 현장 기준이 있는가, 없으면 대상별 허용 경과 시간을 어떤 근거로 정할 것인가? (영역 18, 22)
- oq-035 [열림] 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기의 ISO 8601 시각, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? (영역 18, 20, 42)
- oq-036 [열림] 로봇이 보고한 적재물 식별·판독 결과와 WMS 재고 기록이 어긋날 때 어느 쪽을 기준으로 삼고 정정 기록을 누가 발행하는가(국내 물류센터 사례 포함)? (영역 17, 18)
- oq-037 [열림] 출처 충돌: 김지형(2023) 'OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현'의 게재 학술지를 한 검색 요약은 지능정보논문지로, KoreaScience 는 한국인터넷방송통신학회논문지(DOI 10.7236/JIIBC.2023.23.4.189)로 적는다. 어느 쪽이 맞는가? (영역 18)
- oq-061 [열림] 로봇팔·워크셀의 인수 결과와 이동로봇의 적재 상태 보고가 어긋날 때(한쪽은 성공, 다른 쪽은 적재 유지) 어느 신호를 기준으로 인계 완료를 판정하는지 정한 표준이나 현장 사례가 있는가? (영역 18, 30)
- oq-227 [열림] 하드웨어 동기화가 없는 고정 카메라와 로봇 인식 결과를 하나의 현재 공간 상태로 합칠 때 허용할 시간 차와 좌표 정합 기준을 정한 연구나 제품 문서가 있는가? (영역 45, 18)
- oq-272 [열림] 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? (영역 19, 18, 53)
- oq-294 [열림] 사람 존재 정보로 세계 상태 정보의 확실도를 낮추는 방식을 물류창고·병원 같은 이동로봇 현장의 문·통로·적재물 상태 판단에 적용한 연구나 사례가 있는가? (영역 18, 19, 31)
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

### runs/2026-10-09-10/research.md

```markdown
# 리서치 브리프 2026-10-09-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-10 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | N. 보안·개인정보 |

## 갭(비어 있거나 약한 섹션)

- N. 보안·개인정보 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터와 다른 16개 대분류의 연결이 정리되지 않았다
- 51. 인증·권한·격리 페이지는 이전 분류(2026-09-25) 기준이라 C. 채팅 기반 구성·운영, D. 공간·지도 모델, J. 현장 운영·관제의 40. 운영 절차·요청 창구, P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터와 잇는 근거가 페이지 안에 없다
- 51·52·53 페이지의 10절(다른 연구영역과의 연결)은 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다
- D. 공간·지도 모델 페이지는 N. 보안·개인정보와의 연결을 '근거 없음'으로 남겼다(지도 데이터의 접근 통제·개인정보)
- Q. 현장 유형별 적용 가운데 물류창고·상업 시설·기타 현장의 보안·개인정보 사례가 51·52·53 게시 페이지에 없다
- EU 사이버복원력법 보고 의무(2026-09-11 시행)와 EU 데이터법처럼 최근 시행된 규정이 게시 페이지에 반영되지 않았다

## 조사 질문

1. 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]
2. 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
3. 51. 인증·권한·격리의 명령 권한·장비 인증은 B. 로봇 온톨로지(4·6·7)·F. 연동(20·22)·G. 계획·최적화(25)·H. 실행·협업·예외 복구(29)·K. 플랫폼 아키텍처·인프라(41)의 어느 인터페이스와 이어지는가? (oq-056, oq-082, oq-100, oq-113 관련)
4. 52. 통신 보호·위협 관리·감사의 위협·감사 기록은 C. 채팅 기반 구성·운영(12·13)·E. 사물·사람·실시간 상태(18)·J. 현장 운영·관제(37·38·40)·L. AI·학습 기술(44·47)·M. 안전(48·50)·O. 검증·도입·수명주기(54·55·57)와 어디서 만나는가? (oq-144, oq-246, oq-248, oq-291 관련)
5. 53. 개인정보·영상 데이터의 수집·보관 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(17·19)·L. AI·학습 기술(45·47)·P. 거버넌스·법규·사회(58·59·60)와 어떻게 이어지는가? (oq-259, oq-285, oq-214 관련)
6. 보안 인증·규제(IEC 62443, ISO 10218 개정, EU 사이버복원력법, EU 데이터법, 국내 로봇 보안모델)는 A. 기획·사업(1·2·3)에 어떤 요구를 넘기는가?
7. N. 보안·개인정보의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며 한국 자료는 무엇이 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 과학기술정보통신부와 한국인터넷진흥원(KISA)은 2026-03-05 로봇 보안모델 고도화판과 로봇 보안요구사항 해설서를 공개했고, 피지컬 AI 확산과 유럽·북미 사이버보안 규제 강화를 반영해 기업이 개발·수출 과정의 보안 요구를 파악하게 하는 것을 목적으로 밝혔다. | ref-1373, ref-1111 | 아니오 | medium | 2026-03-05 | — | — |
| f2 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: KUKA 는 iiQKA.OS2 운영체제와 KR C5-2 제어기 플랫폼이 IEC 62443-4-2 보안 수준 2(SL2) 인증을 받았고 로봇 제조사 가운데 처음이라고 2026-09-02 발표했으며, 발표문에는 인증 기관이 나오지 않는다. | ref-1375 | 아니오 | low | 2026-09-02 | — | 벤더 주장 |
| f3 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: IEC 62443 이 보안 수준을 정하고 로봇 제어기 단위의 인증 발표가 나오고 있으므로, 로봇·플랫폼 조달 요구에 구성요소 보안 인증 여부와 목표 보안 수준을 넣는 일이 3. 경제성·조달·사업 모델로 넘어갈 것으로 보이나, 플릿 관리 소프트웨어 단위의 인증 사례는 확인하지 못했다. | ref-1105, ref-1375 | 아니오 | low | 2026-10-09 | — | — |
| f4 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: 52. 통신 보호·위협 관리·감사 페이지는 ROP 가 자신이 여는 연결의 보안과 전체 연결 구조의 위협 모델을 맡고 로봇 제어기·펌웨어와 현장 망 보안은 제조사·시설 IT/OT 쪽 연계 대상으로 두므로, 이 보안 책임 경계가 2. 사용 사례·요구·책임 범위의 책임 범위 정의에 들어가야 할 것으로 보인다. | ref-1114, ref-1107, ref-009 | 아니오 | low | 2026-09-30 | — | — |
| f5 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: VDA 5050 3.0.0 은 로봇이 새 인증서 묶음을 내려받아 활성화하게 하는 즉시 동작 updateCertificate 를 두고, 내려받기도 TLS 로 보호해야 하며 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f6 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록·7. 온톨로지 검증·변경 관리, O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: 로봇마다 인증서 교체 지원 여부와 인증서 판·만료를 등록 정보로 두고 교체 이력을 판 관리와 함께 다루면 인증서 교체 대상과 시점을 추적할 수 있을 것으로 보이며, 교체 승인과 실패 때 되돌림 책임은 열린 질문(oq-113)으로 남는다. | ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 53. 개인정보·영상 데이터 페이지가 카메라 유무·촬영 사실 표시 수단·영상 전송 경로 기록과 로봇 인지 출력 필드 축소를 ROP 직접 범위로 보므로, 이런 개인정보 관련 속성이 4. 이기종 로봇 등록의 등록 항목으로 넘어갈 것으로 보인다. | ref-1145, ref-588 | 아니오 | low | 2026-09-30 | — | 원문 미열람 |
| f8 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: ROS 2 접근 제어 정책은 인클레이브별로 토픽·서비스·액션 단위의 허용·거부를 두므로, '진단은 허용하고 이동은 막는' 명령 단위 권한을 걸려면 6. 온톨로지 기반 시스템·로봇 연동이 능력을 실제 명령에 묶을 때 권한 정책과 같은 명령 식별자를 공유해야 할 것으로 보인다. | ref-579, ref-405 | 아니오 | low | 2026-10-09 | 제약 | — |
| f9 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: OWASP LLM01:2025 는 프롬프트 주입을 사용자가 직접 넣는 직접 주입과 문서·웹 같은 외부 내용에 숨은 지시가 들어오는 간접 주입으로 나누고 완화책을 정리한다. | ref-1106 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f10 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 대규모 언어 모델을 통합한 이동로봇 시스템에 대한 프롬프트 주입 공격 연구(Zhang 외, 2024-08)와 다중 에이전트 로봇 시스템에서 프롬프트가 로봇을 제어할 때의 프롬프트 주입 공격 연구(Nagaraja 외, 2026-08)가 있다. | ref-1113, ref-1112 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f11 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: Robey 외는 언어 모델이 제어하는 로봇에서 탈옥 알고리즘 RoboPAIR 의 공격 성공률이 자주 100%에 이르렀다고 보고했고, Ravichandran 외의 RoboGuard 는 최악의 탈옥 공격에서 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고했다. | ref-857, ref-700 | 아니오 | medium | 2025-03 | 제약 | 원문 미열람 |
| f12 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Open-RMF REST API 를 언어 모델 도구로 노출하는 MCP 서버(Nayantra) 같은 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근 통제가 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 함께 두 대분류의 경계가 될 것으로 보인다. | ref-854, ref-857 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f13 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: '사람이 확인·승인한 계획만 실행'이 지켜졌음을 사후에 보이려면 누가 어떤 계획을 언제 승인했는지를 변조 탐지가 가능한 감사 기록으로 남겨야 할 것으로 보이며, 자율 에이전트 행동을 블록체인 기록과 언어 모델 설명으로 추적하는 구조 연구(2024-03)가 그 후보다. | ref-1110 | 아니오 | low | 2026-10-09 | 완료·인계 | 원문 미열람 |
| f14 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 브랜드 점검에서 집 내부 구조를 나타내는 지도 정보는 모든 제품이 기기에 저장하고 스마트폰에는 저장하지 않았으며 일부 제품은 서버에도 저장했고, 일부 사업자는 로봇청소기 접근통제와 개인정보 전송 암호화가 미흡했다. | ref-1372, ref-1141 | 아니오 | medium | 2026-09-14 | 가정 / 작업 대상 | — |
| f15 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리: 건물 내부 지도가 개인정보 점검 대상 정보로 다뤄지고 VDA 5050 이 지도를 관제가 지정한 링크에서 내려받게 하므로, ROP 가 보관·배포하는 지도의 저장 위치·전송 암호화·접근 권한을 정하는 일이 두 대분류를 잇는 지점이 될 것으로 보인다. | ref-1372, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Shen 외(2026-09, 프리프린트)는 ROS 2 에서 환경 변수 하나를 바꾸면 사전 빌드된 훅이 텔레메트리·제어 신호를 발행 전에 가로채고 주입할 수 있음을 보였고, Secure ROS 2 를 쓴 실제 Franka 로봇팔에서 약 3 ms 지터로 위조 텔레메트리를 넣어 AI 기반 탐지기 상대로도 87% 성공했다고 보고했다. | ref-1374 | 아니오 | medium | 2026-09-08 | — | — |
| f17 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성·J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 로봇이 보고하는 상태가 통신 보호 이전 단계에서 위조될 수 있고 위치 스푸핑이 배정을 무너뜨린다는 연구가 있으므로, 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 판단과 38. 모니터링·이상 탐지·원인 분석은 암호화된 보고만 믿지 말고 설비 센서·다른 로봇 관측과 교차 확인해야 할 것으로 보인다(oq-082). | ref-1374, ref-494 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f18 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 병원 운반 로봇 Zena RX 는 생체 인식과 직원 PIN 으로 잠금 칸을 연다고 제조사가 밝히고 공동주택 배달 로봇 도입 계획은 비밀번호로 적재함을 열게 했으므로, '누구에게 넘겼는가' 기록은 인증 수단과 생체·전화번호 처리 규칙에 기댈 것으로 보인다. | ref-1299, ref-1301 | 아니오 | low | 2026-10-09 | 병원 / 완료·인계 | 원문 미열람, 벤더 주장 |
| f19 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: ROS 규약 제안 REP-155(Draft)는 사람마다 영속 ID 를 두고 얼굴·몸·음성 ID 를 후보 대응으로 연결하며, 개인정보·동의는 다루지 않는다. | ref-1173 | 아니오 | medium | 2022-01-11 | — | 원문 미열람 |
| f20 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 2025-08 한 보안 연구자는 Pudu Robotics 로봇 관리 소프트웨어가 유효한 인증 토큰만 확인하고 그 뒤 권한을 검사하지 않아, 교차 사이트 스크립팅이나 체험 계정으로 얻은 토큰으로 주문을 바꾸고 로봇을 다른 위치로 보내고 이름을 바꿀 수 있었다고 공개했다. | ref-1368, ref-1369 | 아니오 | medium | 2025-08-29 | 상업 시설 / 예외·성과 | — |
| f21 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 미국 CISA 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇 TUG 를 제어하는 Home Base Server 에서 인증 없이 웹소켓으로 로봇을 제어할 수 있는 취약점(CVE-2022-1070, CVSS 9.8)과 인가 누락 취약점을 공개했다. | ref-1107 | 아니오 | medium | 2022-04-12 | 병원 / 예외·성과 | 원문 미열람 |
| f22 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 식당 서빙 로봇과 병원 운반 로봇 사례 모두 제조사 플릿 서버·관리 API 의 인증·인가 결함이 로봇 제어로 이어졌으므로, ROP 가 제조사 관제를 연결할 때 연결 계정의 권한 범위와 인가 확인을 연동 승인 조건으로 둬야 할 것으로 보인다(oq-100). | ref-1368, ref-1107 | 아니오 | low | 2026-10-09 | 제약 | — |
| f23 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 범위 절에서 보안 통신·데이터 보호의 메커니즘·기술·절차를 정하지 않는다고 밝히고, 프로토콜 보안은 브로커 구성으로 다뤄야 하며 이 지침에서는 다루지 않는다고 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f24 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: 상호운용 규격이 통신 보안을 범위 밖 브로커 구성에 맡기므로 21. 상호운용 표준·적합성의 적합성 시험과 브로커·API 의 상호 인증·TLS 설정 확인은 별도 경로로 관리해야 할 것으로 보이며, 그 최소 요구를 정한 공개 보안 프로파일은 확인하지 못했다(oq-246). | ref-031, ref-1105 | 아니오 | low | 2026-10-09 | — | — |
| f25 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 22. 설비·건물 시스템 연동: 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)도 같은 관리 API 결함의 대상이 될 수 있다고 보도되었으므로, 로봇 관제·설비 어댑터 구성요소를 SROS 2 인클레이브처럼 별도 신원·접근 규칙으로 나눠 설비 명령 권한을 제한하는 설계가 두 대분류의 경계가 될 것으로 보인다(oq-056). | ref-1369, ref-405 | 아니오 | low | 2026-10-09 | 제약 | — |
| f26 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Francos 외(2026-08, 프리프린트)는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했다. | ref-494 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f27 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF: 제조사 관리 API 를 거쳐 주문을 바꾸거나 로봇 위치를 옮길 수 있었던 사례가 있으므로, ROP 의 배정·교통 계획은 자신이 내리지 않은 임무 변경·이동을 로봇 상태에서 감지해 해당 로봇을 계획에서 보류하는 규칙이 필요할 것으로 보인다. | ref-1368 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f28 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 에서 updateCertificate 동작은 실행 중에는 인증서를 내려받아 설치 중이라는 상태로, 실패하면 내려받기 또는 설치 실패로 보고되므로, 보안 명령도 일반 명령처럼 실행 확인·실패 처리 대상이 된다. | ref-031 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f29 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 식당 서빙 로봇 관리 API 결함으로 영업 중 플릿 전체 작업을 취소하거나 멈출 수 있었다고 보도되었으므로, 보안 사고로 플릿 일부·전체를 격리하고 수동 운영으로 넘어가는 시나리오가 32. 예외 복구·재계획·업무 연속성의 복구 절차에 들어가야 할 것으로 보인다. | ref-1368, ref-1369 | 아니오 | low | 2026-10-09 | 상업 시설 / 예외·성과 | — |
| f30 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1304 | 아니오 | medium | 2022-11-17 | — | 원문 미열람 |
| f31 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사·53. 개인정보·영상 데이터 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 가정한 미래를 실험하는 시뮬레이션과 실제 상황 재현에 운영 기록·영상을 입력으로 쓰면 그 기록의 무결성과 '재현' 목적의 이용 범위를 함께 정해야 할 것으로 보이며, 이는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 문제(f17)와 구분된다. | ref-1304, ref-588 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f32 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Fernández-Becerra 외(2024-03)는 자율 에이전트의 행동을 블록체인 기반 기록과 대규모 언어 모델 설명으로 남겨 책임 추적성과 설명 가능성을 높이는 구조를 제안했다. | ref-1110 | 아니오 | medium | 2024-03 | — | 원문 미열람 |
| f33 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 업계 해설에 따르면 EU 기계류 규정 (EU) 2023/1230 은 변조 보호, 개입 증거 기록, 안전 소프트웨어 판 추적 로그를 요구하며 2027-01-20 전면 적용된다. | ref-1109 | 아니오 | medium | 2026-08-27 | — | 원문 미열람 |
| f34 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: Pudu 사례에서 연구자의 신고(2025-08-12 시작)는 보안 신고 창구가 없어 응답을 받지 못하다가 고객사(Skylark Holdings·Zensho)에 알린 뒤에야 처리되었고, 제조사는 이후 취약점을 고치고 보안 대응 센터와 신고 주소를 만들었다. | ref-1368, ref-1369 | 아니오 | medium | 2025-09-05 | 상업 시설 / 예외·성과 | — |
| f35 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EU 사이버복원력법에 따라 2026-09-11 부터 디지털 요소 제품 제조자는 적극 악용되는 취약점과 중대 사고를 ENISA 단일 보고 플랫폼으로 알려야 하며, 인지 후 24시간 안에 조기 경보, 72시간 안에 통지, 취약점은 시정 조치가 나온 뒤 14일 안에 최종 보고를 낸다. | ref-1367 | 아니오 | medium | 2026-09-11 | 예외·성과 | — |
| f36 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: 신고 창구가 없던 제조사 사례와 24·72시간 보고 시한을 함께 보면, 여러 제조사 로봇을 운영하는 현장의 요청 창구에 보안 취약점·사고 접수와 제조사·ROP 사업자 사이 통보 경로를 두는 일이 40. 운영 절차·요청 창구로 넘어갈 것으로 보이며, 플랫폼 사업자의 보고 의무 해당 여부는 열린 질문(oq-291)이다. | ref-1367, ref-1368 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f37 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API: Open-RMF 문서는 웹 대시보드를 TLS 로 제공하고 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용하며, ROS 2 쪽 구성요소는 SROS 2 인클레이브로 권한을 나눈다고 설명한다. | ref-405 | 아니오 | medium | 2026-10-09 | — | — |
| f38 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: ROS 2 는 DDS 보안 규격의 인증·접근 통제·암호화 플러그인을 쓰고, ROS 2 위협 모델 초안은 보안이 꺼진 시스템에서는 어떤 노드든 어떤 토픽에나 발행할 수 있어 신원 위조와 명령 가로채기가 가능하다고 정리한다. | ref-009, ref-010 | 아니오 | medium | 2026-10-09 | — | — |
| f39 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: 2026-09-14 로봇청소기 점검 보도에 따르면 개인정보보호위원회는 점검 후속 조치로 접근권한 부여 내역 보관 기간을 200일에서 3년으로, 접속기록 보관 기간을 90일에서 2년 이상으로 늘리도록 했다. | ref-1372 | 아니오 | medium | 2026-09-14 | 가정 / 제약 | — |
| f40 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ L. AI·학습 기술의 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영: 개인정보보호위원회는 2023-11 자율주행차·이동형 로봇 개발에 영상데이터 원본 활용을 허용하는 방향을 밝혔고, 2026-05-06 ICT 규제샌드박스 심의위원회는 배달로봇 카메라 원본 영상을 AI 학습에 쓰는 과제에 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지 등을 조건으로 실증특례를 승인했다. | ref-1138, ref-1342 | 아니오 | medium | 2026-05-06 | 실외 / 제약 | 원문 미열람 |
| f41 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act 제12조는 고위험 AI 시스템이 수명 기간 동안 사건 기록(로그)을 자동으로 남길 수 있어야 하고, 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다. | ref-863 | 아니오 | medium | 2024-06-13 | — | 원문 미열람 |
| f42 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. | ref-1116, ref-1076 | 예 | medium | 2026-09-18 | — | 원문 미열람 |
| f43 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 서비스 로봇 안전 표준 ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 사이버보안과 데이터 보호 절을 새로 넣었다. | ref-1425 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f44 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ M. 안전의 48. 안전·위험 관리: Quarta 외(IEEE S&P 2017)는 널리 쓰이는 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 것으로 보인다. | ref-1114 | 아니오 | low | 2017 | 제조 공장 / 예외·성과 | 원문 미열람 |
| f45 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ M. 안전의 48. 안전·위험 관리: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제가 안전 평가 대상이 될 것으로 보인다. | ref-1116, ref-1425 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f46 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROS 2 위협 모델 초안은 빌드 팜과 서드파티 구성요소를 통한 공급망 위협을 주요 위협으로 들고, Shen 외(2026-09)는 제3자 Docker 컨테이너·보조 도구에 대한 폭넓은 의존을 이용해 악성 훅이 든 패키지를 퍼뜨릴 수 있다고 적는다. | ref-010, ref-1374 | 아니오 | medium | 2026-09-08 | — | — |
| f47 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: ROS 2 위협 모델 초안이 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 들므로, 설치·시운전 점검 항목에 기본 자격증명 변경과 원격 접속 범위 확인이 들어가야 할 것으로 보인다. | ref-010 | 아니오 | low | 2026-10-09 | 제약 | — |
| f48 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: 2025년 한국인터넷진흥원·한국소비자원의 로봇청소기 6종 점검은 모바일앱 보안·정책 관리·기기 보안 3개 영역 40개 항목으로 이루어졌다고 보도되어, 로봇 보안 시험 항목의 국내 참고 틀이 될 것으로 보인다. | ref-969 | 아니오 | low | 2025-10-31 | 가정 | 원문 미열람 |
| f49 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: EU 데이터법은 2025-09-12 부터 적용되며, 로봇·산업 기계 같은 연결 제품의 사용자가 사용으로 생긴 데이터에 접근해 직접 쓰거나 제3자와 공유할 수 있게 하고, 데이터 보유자(보통 제조사)는 사용자와 계약을 두고 생성 데이터 종류·양·수집 빈도를 알려야 한다. | ref-1376 | 아니오 | medium | 2026-10-09 | — | — |
| f50 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: 여러 제조사 로봇의 데이터를 모아 관제하는 ROP 사업자가 데이터법상 사용자·제3자 가운데 어느 쪽이고 개인정보 처리에서 운영자·수탁자 가운데 어느 쪽인지가 계약으로 정해야 할 쟁점이 될 것으로 보인다(oq-259). | ref-1376, ref-588 | 아니오 | low | 2026-10-09 | — | — |
| f51 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 개인정보보호위원회 이동형 영상정보처리기기 안내서 공개 보도와 법률사무소 해설은 카메라를 단 자율주행차·배달로봇이 외부에 촬영 사실을 표시하고 명확히 거부하는 사람의 의사를 받아들여야 한다고 전한다. | ref-1136, ref-588 | 아니오 | medium | 2024-10-14 | 실외 / 제약 | 원문 미열람 |
| f52 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·Q. 현장 유형별 적용의 61. 물류창고: 프랑스 개인정보 감독기관 CNIL 은 2023-12-27 결정(2024-01-23 공표)으로 Amazon France Logistique 에 3,200만 유로 과징금을 부과했는데, 물류창고 작업자 스캐너 기록으로 10분 넘는 비활동을 실시간 경보하고 1.25초 안의 빠른 스캔을 표시하는 지표와 모든 데이터·지표의 31일 보관을 과도하다고 보았다. | ref-1370, ref-1371 | 예 | medium | 2024-01-23 | 물류창고 / 제약 | — |
| f53 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·J. 현장 운영·관제의 39. 운영 성과 측정·개선: 작업자 스캐너 기록의 개인별 비활동·속도 지표가 과도한 감시로 판단된 사례가 있으므로, ROP 가 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록할 때 39. 운영 성과 측정·개선의 지표를 집계 단위로 두고 보존 기간을 줄이는 설계가 필요할 것으로 보인다(oq-285). | ref-1370, ref-589 | 아니오 | low | 2026-10-09 | 물류창고 / 제약 | — |
| f54 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 둔다. | ref-589 | 아니오 | medium | 2026-10-09 | 제약 | 원문 미열람 |
| f55 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ Q. 현장 유형별 적용의 67. 기타 현장: Pudu 관리 API 결함 보도는 사무실에서 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)이 사무실 시스템을 망가뜨리거나 지식재산을 빼내는 데 쓰일 수 있다고 평가했는데, 이는 연구자·매체의 평가이며 확인된 사고는 아니다. | ref-1369, ref-1368 | 아니오 | low | 2025-09-05 | 기타 / 예외·성과 | — |
| f56 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ Q. 현장 유형별 적용의 63. 병원·의료: 진료실을 흉내 낸 모의 시나리오에서 의사·환자를 알아보도록 학습한 서비스 로봇은 대상이 아닌 사람의 얼굴을 안정적으로 가렸지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮췄다. | ref-1146 | 아니오 | medium | 2026-03-16 | 병원 / 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_dds_security.html | 아니오 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_threat_model.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/security.html | 아니오 |
| ref-579 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 2019-08 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_access_control_policies.html | 아니오 |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.25690 | 예 |
| ref-588 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 미확인 | 업계 보고서 | medium | 2026-10-09 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 예 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 예 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 2024-11-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.13691 | 예 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 2025-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG | Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 예 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 2024-06-13 | 정부·연구기관 | medium | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 | 예 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 2025-10-31 | 기사 | low | 2026-10-09 | https://byline.network/2025/10/31-283/ | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.17822 | 예 |
| ref-1105 | IEC (SyC Smart Energy) | IEC 62443 | 미확인 | 표준 | medium | 2026-10-09 | https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ | 예 |
| ref-1106 | OWASP GenAI Security Project | LLM01:2025 Prompt Injection | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 예 |
| ref-1107 | CISA (미국 사이버보안·기반시설보안청) | Aethon TUG Home Base Server (ICSA-22-102-05) | 2022-04-12 | 정부·연구기관 | medium | 2026-10-09 | https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05 | 예 |
| ref-1109 | IES (Integrated Equipment Services) | Machinery Regulation Guide | 2026-08-27 | 업계 보고서 | medium | 2026-10-09 | https://www.ies.co.uk/reference-library/machinery-regulation-guide | 예 |
| ref-1110 | Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv) | Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models | 2024-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2403.09567 | 예 |
| ref-1111 | 엠에스투데이 | 선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시 | 2026-03-06 | 기사 | low | 2026-10-09 | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 | 예 |
| ref-1112 | Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv) | When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.00747 | 예 |
| ref-1113 | Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv) | A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems | 2024-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2408.03515 | 예 |
| ref-1114 | Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017) | An Experimental Security Analysis of an Industrial Robot Controller | 2017 | 논문 | medium | 2026-10-09 | https://files01.core.ac.uk/download/pdf/84891817.pdf | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-09 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 예 |
| ref-1136 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" | 2024-10-14 | 기사 | low | 2026-10-09 | https://www.koit.co.kr/news/articleView.html?idxno=125844 | 예 |
| ref-1138 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용 | 2023-11-15 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 | 예 |
| ref-1141 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 2026-09-14 | 기사 | low | 2026-10-09 | https://view.asiae.co.kr/article/2026091410054053414 | 예 |
| ref-1145 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 2026-09-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.03055 | 예 |
| ref-1146 | Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26) | The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting | 2026-03-16 | 논문 | medium | 2026-10-09 | https://doi.org/10.1145/3776734.3794481 | 예 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 예 |
| ref-1299 | ST Engineering Aethon (Newswire 게재 보도자료) | ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals | 2024-04-29 | 벤더 문서 | low | 2026-10-09 | https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264 | 예 |
| ref-1301 | 경향신문 (곽희양) | 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다 | 2020-07-03 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202007031130001 | 예 |
| ref-1304 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 예 |
| ref-1342 | 메트로신문 | AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원 | 2026-05-06 | 기사 | low | 2026-10-09 | https://www.metroseoul.co.kr/article/20260506500296 | 예 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 2024-10 | 표준 | medium | 2026-10-09 | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 | 예 |
| ref-1367 | European Commission (Shaping Europe's digital future) | CRA reporting | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 아니오 |
| ref-1368 | The Register | Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots | 2025-08-29 | 기사 | medium | 2026-10-09 | https://www.theregister.com/2025/08/29/pudu_robots_hackable/ | 아니오 |
| ref-1369 | Hackmag | Researcher finds a way to hack Chinese Pudu service robots | 2025-09-05 | 기사 | low | 2026-10-09 | https://hackmag.com/news/pudu-bugs | 아니오 |
| ref-1370 | Silicon UK | France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance | 2024-01-23 | 기사 | medium | 2026-10-09 | https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858 | 아니오 |
| ref-1371 | CNIL (Commission nationale de l'informatique et des libertés) | Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million | 2024-01-23 | 정부·연구기관 | medium | 2026-10-09 | https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million | 예 |
| ref-1372 | 바이라인네트워크 (곽중희) | 개인정보위 "로봇청소기 5개 브랜드, 특별한 침해 위험 없어" | 2026-09-14 | 기사 | medium | 2026-10-09 | https://byline.network/2026/09/14-623/ | 아니오 |
| ref-1373 | 바이라인네트워크 | 과기정통부, 선박·우주·로봇 보안 매뉴얼 공개 | 2026-03-06 | 기사 | medium | 2026-10-09 | https://byline.network/2026/03/6-340/ | 아니오 |
| ref-1374 | Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv) | Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics | 2026-09-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.08280 | 아니오 |
| ref-1375 | KUKA (Robotics Tomorrow 게재 보도자료) | KUKA is First to Achieve Security Level 2 Certification for Robotics Industry | 2026-09-02 | 벤더 문서 | low | 2026-10-09 | https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/ | 아니오 |
| ref-1376 | European Commission (Shaping Europe's digital future) | Data Act explained | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/data-act-explained | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/index.md | 5. 다른 대분류와의 연결 | category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1(1, 한국 보안모델), f2(3, 벤더 주장)·f3(3), f4(2) / B. 로봇 온톨로지: f5·f6(4·7, 인증서 교체, oq-113), f7(4, 개인정보 속성), f8(6, 명령 단위 권한) / C. 채팅 기반 구성·운영: f9(13), f10(12), f11(13·44), f12(12, 최소 권한), f13(12, 승인 감사 기록) — 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f14(16, 가정 지도 저장 위치)·f15(15·16) — D 페이지가 '근거 없음'으로 둔 N 연결을 채움 / E. 사물·사람·실시간 상태: f16·f17(18, 텔레메트리 위조, oq-082), f18(17, 벤더 주장), f19(19) / F. 연동: f20·f21·f22(20, oq-100), f23·f24(21, oq-246), f25(22, oq-056) / G. 계획·최적화: f26·f27(25·27) / H. 실행·협업·예외 복구: f28(29), f29(32) / I. 설계·시뮬레이션: f30(34), f31(34·36) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성(f16·f17)과 구분 / J. 현장 운영·관제: f32·f33(37, oq-248·oq-249), f17(38), f34·f35·f36(40, oq-291) / K. 플랫폼 아키텍처·인프라: f37(41), f38(42), f39(43, oq-214) / L. AI·학습 기술: f40(45·47, 원본 영상), f41(47), f11(44) / M. 안전: f42·f43(50, oq-102·oq-254), f44·f45(48) / O. 검증·도입·수명주기: f48(54), f47(55), f46·f6·f35(57) / P. 거버넌스·법규·사회: f49·f50(58, oq-259), f35·f51(59), f52·f53·f54(60, oq-285·oq-099) / Q. 현장 유형별 적용: f52(61 물류창고, 로봇이 아닌 스캐너 사례임을 밝힘), f44(62 제조 공장), f21·f56(63 병원·의료), f20·f29·f34(64 상업 시설), f14·f39·f48(65 가정·공동주택), f40·f51(66 실외), f55(67 기타 현장). 벤더 주장 f2·f18 은 [추정]과 '벤더 주장' 병기. 로봇 제어기·펌웨어 보안, 승강기 제어, 카메라 기기 쪽 처리는 '연계 대상'으로 짧게. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 56. 운영 이관·확대·교육, 5. 로봇 능력·작업 표현, 8~11. 채팅 영역. 다음 실행 후보: 51. 인증·권한·격리(이전 분류 기준) 10절에 f5·f20·f22·f37 반영, 52. 통신 보호·위협 관리·감사 7절에 f35(사이버복원력법 보고 의무) 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 적극 악용 취약점 | Actively Exploited Vulnerability (EU Cyber Resilience Act) | 악의적 악용의 믿을 만한 증거가 있는 취약점으로, EU 사이버복원력법이 2026-09-11 부터 제조자에게 24시간 조기 경보·72시간 통지·최종 보고를 요구하는 대상이다. |
| 연결 제품 | Connected Product (EU Data Act) | 사용·성능·환경 데이터를 만들고 전송할 수 있는 제품으로, EU 데이터법이 사용자에게 그 데이터의 접근·공유 권리를 주는 대상이며 집행위원회 해설은 로봇과 산업 기계를 예로 든다. |
| 원격 증명 | Remote Attestation | 원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다. |

## 열린 질문

새로 생긴 질문:

- ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가? | 관련 영역: 51. 인증·권한·격리, 20. 로봇·제조사 관제 연동, 54. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반
- 로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 18. 실시간 세계 상태·데이터 일관성, 38. 모니터링·이상 탐지·원인 분석 | 근거: f17 | 종류: 일반
- EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 53. 개인정보·영상 데이터 | 근거: f50 | 종류: 일반
- 작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 60. 노동·수용성·접근성, 39. 운영 성과 측정·개선 | 근거: f53 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 45 · 교차 확인: 2
- 예산 사용량: 검색 13회 · 신규 출처 10건
- 미확인 항목:
    - f20·f29·f34·f55 Pudu 사례는 연구자 블로그 공개를 옮긴 기사 두 건 기준이며 연구자 원문과 제조사 공식 공지는 열지 못함(교차 확인 아님)
    - ref-1371 CNIL 공지는 페이지가 '더 이상 제공되지 않음'으로 열려 검색 결과 요약 범위로만 사용
    - f39 접근권한 내역·접속기록 보관 기간 연장의 적용 대상과 근거 조항은 기사에 없어 미확인(oq-214)
    - f2 KUKA IEC 62443-4-2 SL2 인증은 벤더 주장, 인증 기관·인증서 미확인
    - MiR Fleet Enterprise 의 IEC 62443-4-2 정렬 주장은 PDF 본문을 추출하지 못해 쓰지 않음
    - ISO 10218-1:2025 사이버보안 조항 번호는 여전히 미확인(oq-102)
    - KISA 로봇 보안모델 고도화판·해설서의 요구 항목은 원문을 열지 못해 미확인(oq-250)
    - EU 사이버복원력법 규정 원문(제14조)은 열지 않고 집행위원회 안내 페이지만 확인
    - 재사용 출처 35건은 이번 실행에서 다시 열지 않음
- 범위 경계 위반 의심:
    - f2·f3·f44: 로봇 제어기 보안 인증·제어기 취약점은 원문 19장 '로봇 자체 지능·제어' 경계의 제조사 몫이라 ROP 는 조달 요구·연결 대상 위협 근거로만 서술
    - f21·f25: 병원 플릿 서버의 방화벽·VPN, 승강기 조작은 시설·설비 제어 경계의 연계 대상이며 ROP 는 연결 계정 권한과 설비 명령 권한 분리로만 서술
    - f14·f18·f56: 로봇청소기 앱 인증·기기 저장, 잠금 칸 생체 인증, 기기 쪽 얼굴 가림은 제조사 기능이라 연계 대상이며 ROP 는 결과·상태 기록 쪽만 서술
    - f35·f49·f51·f52·f54: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며 ROP 는 기록·통보·데이터 흐름 규칙 제공 범위로만 연결
    - f52: CNIL 사례는 로봇이 아닌 작업자 스캐너 기록이라 claim 에 그 사실을 밝힘
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 51·52·53 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-08, 2026-10-09-09)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 35건 가운데 이번에 다시 연 것은 ref-031(github_raw) 1건이고 나머지 34건은 fetched false·source_unopened true). 신규 출처는 10건(ref-1367~ref-1376, 예약 구간 안)이며 ref-1371(CNIL 공지)을 뺀 9건은 원문을 열었다. 검색 13회/30, 신규 출처 10건/15. 교차 확인 2건(f42 ISO 10218 사이버보안, f52 CNIL Amazon 과징금). 벤더 주장 2건(f2·f18). 같은 정부 발표를 옮긴 기사 쌍(f1, f51)과 같은 연구자 공개를 옮긴 기사 쌍(f20 등)은 독립 출처로 보지 않아 교차 확인으로 세지 않았다. 한국 자료: 신규 ref-1372·ref-1373, 재사용 ref-589·ref-588·ref-969·ref-1111·ref-1136·ref-1138·ref-1141·ref-1301·ref-1342. 현장 유형: 물류창고(f52·f53, 로봇이 아닌 스캐너 사례)·제조 공장(f44)·병원(f18·f21·f56)·상업 시설(f20·f29·f34)·가정(f14·f39·f48)·실외(f40·f51)·기타(f55) 각 1건 이상. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f16·f17)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f30·f31)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f11·f40·f41)은 적용 대상 영역과 함께 제안했다. 열린 질문 oq-056·oq-082·oq-099·oq-100·oq-102·oq-113·oq-214·oq-246·oq-248·oq-249·oq-250·oq-259·oq-285·oq-291 에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 이전 대분류 연결 실행과 같이 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)에 따라 '5'로 매겼다 [가정]. 아직 근거를 찾지 못한 연결은 page_proposals 의 rationale 에 적었다. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/2026-10-09-09/research.md

```markdown
# 리서치 브리프 2026-10-09-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-09 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- M. 안전 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 48. 안전·위험 관리, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사와 다른 16개 대분류의 연결이 정리되지 않았다
- 48. 안전·위험 관리 페이지는 이전 분류(2026-09-26) 기준이라 C. 채팅 기반 구성·운영, K. 플랫폼 아키텍처·인프라, O. 검증·도입·수명주기의 56. 운영 이관·확대·교육, P. 거버넌스·법규·사회와 잇는 근거가 페이지 안에 없다
- 48·49·50 페이지의 10절(다른 연구영역과의 연결)은 49·50 이 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다
- 정지·재개 판단에 쓰는 VDA 5050 안전 상태·운용 모드의 원문 확인과, 관제 통신이 끊겼을 때의 정지 경로(oq-095) 근거가 약하다
- ANSI/A3 R15.08-3(사용자 의무)과 국내 로봇작업 특별교육처럼 운영·교육 쪽 근거(oq-265, oq-275)가 게시 페이지에 없다
- Q. 현장 유형별 적용의 64. 상업 시설에 사람 근접 안전 적용 사례가 없다

## 조사 질문

1. 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]
2. 48. 안전·위험 관리의 정지·재개 판단은 B. 로봇 온톨로지(6)·F. 연동(20·21·22)·H. 실행·협업·예외 복구(29·31·32)·K. 플랫폼 아키텍처·인프라(42)의 어떤 상태·명령·통신 경로에 기대는가? (oq-095, oq-229 관련)
3. 49. 사람 근접 안전의 구역·속도·사람 흐름 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(18·19)·G. 계획·최적화(25·27·28)·I. 설계·시뮬레이션(34·36)과 어떻게 이어지는가?
4. 50. 안전 표준·인증·사고 조사의 표준 개정·인증·사고 기록은 A. 기획·사업(1·2·3)·J. 현장 운영·관제(37·38·40)·N. 보안·개인정보(51·52·53)·O. 검증·도입·수명주기(54·55·56·57)·P. 거버넌스·법규·사회(58·59·60)와 어디서 만나는가? (oq-102, oq-252, oq-254, oq-265, oq-275 관련)
5. 언어 모델이 지시하는 로봇 계획의 안전 검사는 C. 채팅 기반 구성·운영(12·13)과 L. AI·학습 기술(44·47)의 '사람이 확인·승인한 계획만 실행' 원칙과 어떻게 맞물리는가? (oq-106, oq-144 관련)
6. M. 안전의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며, 한국 법령·인증·사고 자료는 무엇이 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: ANSI/A3 R15.08 시리즈는 로봇 자체(1부), 산업용 이동로봇 시스템·적용의 통합(2부, 2023), 사용자의 산업용 이동로봇 적용 사용(3부, 2026)으로 나뉘어 제조사·통합자·사용자의 안전 책임을 부별로 다룬다. | ref-1419, ref-1084 | 아니오 | medium | 2026-09-17 | — | — |
| f2 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: R15.08 시리즈가 통합자와 사용자의 의무를 따로 두므로, 여러 제조사 로봇을 묶는 ROP 사업자가 현장마다 통합자 역할을 맡는지 사용자의 위험성평가를 지원하는 역할에 머무는지가 책임 범위 정의에 들어가야 할 것으로 보인다(oq-096). | ref-1419, ref-1084, ref-472 | 아니오 | low | 2026-10-09 | — | — |
| f3 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 주요 로봇 안전 표준의 개정이 2025~2026년에 몰려 있다. ISO 10218-1/-2 개정판은 2025-02에 나왔고 EN ISO 판의 참조가 2026-09-07 EU 관보에 실렸다. ANSI/A3 R15.08-3 은 A3 판매 페이지 기준 2026-04-23에 발행됐고, ISO 13482 개정판은 2026-09-15 기준 FDIS 단계다. | ref-1116, ref-1420, ref-1117 | 아니오 | medium | 2026-09 | — | — |
| f4 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 2023-11-17 시행된 개정 지능형로봇법에 따라 보도에서 실외이동로봇을 운영하는 자는 보험(또는 공제)에 의무 가입해야 한다. 산업통상자원부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정해 보험상품 출시를 지원한다. | ref-1424 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | — |
| f5 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 실외 로봇 도입에서는 보험 가입과 인증 유지가 운영비 항목이 될 것으로 보인다. 인증 단위가 로봇과 관제장치의 조합이므로, 관제를 맡는 ROP 사업자가 운영자 의무 범위에 드는지가 조달·계약 단계의 쟁점이 될 것으로 보인다. | ref-1424, ref-980 | 아니오 | low | 2026-10-09 | 실외 / 제약 | — |
| f6 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동·H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 운용 모드 가운데 AUTOMATIC 은 관제가 로봇을 완전히 제어하는 상태, SEMIAUTOMATIC 은 관제가 제어하되 주행 속도를 HMI 가 조정하는 상태다. INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 로봇을 제어하지 않는다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f7 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: 6. 온톨로지 기반 시스템·로봇 연동의 '실행 시점 조건 판단'에 배터리·적재 상태와 함께 운용 모드와 안전 상태(비상정지·보호 필드 침범)를 넣어야, 관제가 제어권이 없는 로봇에 작업을 내리지 않을 것으로 보인다. | ref-031 | 아니오 | low | 2026-10-09 | 제약 | — |
| f8 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 로봇마다 R15.08 유형(A·B·C), 적용 안전 표준과 판, 인증 상태를 등록 정보로 두면 표준 개정과 인증 범위를 배정·경로 제약으로 추적할 수 있을 것으로 보인다. | ref-1419, ref-1116, ref-980 | 아니오 | low | 2026-10-09 | — | — |
| f9 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트(SafeGate)와 작업 안전 계약을 두는 방법을 제안했다. | ref-417 | 아니오 | medium | 2026-04 | 제약 | 원문 미열람 |
| f10 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: Ravichandran 외의 RoboGuard 에서는 악성 프롬프트와 격리한 신뢰 기점 LLM 이 미리 정한 안전 규칙을 시간 논리 제약으로 바꾸고 제어 합성으로 계획과의 충돌을 푼다. 저자들은 최악의 탈옥 공격에서 위험 계획 실행이 92% 이상에서 3% 미만으로 줄었다고 보고했다. | ref-1338 | 아니오 | medium | 2026-03-03 | 제약 | 원문 미열람 |
| f11 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Robey 외(2024-10)는 언어 모델이 제어하는 로봇이 해로운 물리 행동을 하도록 만드는 탈옥 알고리즘 RoboPAIR 를 제시했다. GPT-4o 계획기를 쓴 Clearpath Jackal 과 GPT-3.5 를 연동한 Unitree Go2 등에서 공격 성공률이 자주 100%에 이르렀다고 보고했다. | ref-1337 | 아니오 | medium | 2024-10-17 | 제약 | 원문 미열람 |
| f12 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션·13. 대화형 기능의 신뢰·기반: 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙에 실행 전 안전 게이트·가드레일 같은 자동 검사를 더하면, 대화 지시에서 로봇 동작까지 이어지는 경로가 48. 안전·위험 관리의 위험성평가 대상이 될 것으로 보인다. 로봇 자체 안전 기능은 연계 대상으로 남는다. | ref-417, ref-1338 | 아니오 | low | 2026-10-09 | 완료·인계 | 원문 미열람 |
| f13 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리·F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 여기거나 적용해서는 안 된다고 범위 절에 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: VDA 5050 3.0.0 의 BLOCKED 구역에는 로봇이 들어가서는 안 되며, 구역 안에 있는 로봇은 멈추고 BLOCKED_ZONE_VIOLATION 오류를 CRITICAL 수준으로 보고한다. SPEED_LIMIT 구역에서는 구역에 들어설 때 이미 최대 속도(m/s) 이하여야 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f15 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 지도에 붙은 진입 금지·속도 제한 구역은 VDA 5050 이 정한 교통 관리 규칙이며 안전 기능이 아니다. 따라서 위험성평가에서 이를 위험 감소 조치로 인정받으려면 ISO 3691-4 의 운용 구역 준비와 로봇의 안전 등급 보호 필드 설정에 맞춰야 할 것으로 보인다(oq-229). | ref-031, ref-470 | 아니오 | low | 2026-10-09 | 제약 | — |
| f16 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고, 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023-06 | 제약 | 원문 미열람 |
| f17 | [사실] | 연계 대상: M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: Abdul Hafez 외(IJRR, 2025-05)는 무결성 위험 지표로 EKF 기반 SLAM 위치추정의 안전성을 정량화했다. 데이터 연관 오류가 위치를 크게 해칠 수 있고, 랜드마크 밀도가 지나치게 높으면 안전성이 오히려 떨어진다고 보고했다. | ref-161 | 아니오 | medium | 2025-05 | — | 원문 미열람 |
| f18 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Open-RMF 승강기 상태(LiftState)의 현재 모드에는 알 수 없음·사람·AGV·화재·오프라인·비상이 있다. 이 가운데 사람·AGV 모드만 설정할 수 있고 나머지는 읽기 전용이다. | ref-286 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f19 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: 승강기의 화재·비상 모드 제어는 시설·설비 제어 경계의 연계 대상이다. ROP 는 탑승을 확정하기 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다. | ref-286 | 아니오 | low | 2026-10-09 | 제약 | — |
| f20 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고, 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다. | ref-1181 | 아니오 | low | 2024-07-12 | 병원 / 제약 | 원문 미열람 |
| f21 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 병원의 사람·휠체어 대기 규칙이나 창고의 학습된 사람 흐름처럼 사람 흐름 정보는 구역·시간대별 대기·속도 규칙으로 49. 사람 근접 안전과 이어질 것으로 보인다. 이때 사람 검출·안전 정지는 로봇이 맡는 연계 대상이다. | ref-1181, ref-1180 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f22 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했다. | ref-945 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f23 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동·N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 구성을 로봇 유형별로 바꾸고 탑승형 로봇 절을 뺐다. 사이버보안, 데이터 보호, 승강기와 협동하는 로봇(참고 부속서 H) 절을 새로 넣었다. | ref-1425 | 아니오 | medium | 2024-10 | — | — |
| f24 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 로봇의 승강기 탑승 안전 요구가 국내 KS 와 서비스 로봇 안전 표준 개정 초안 양쪽에 들어오므로, ROP 는 승강기 연동 요청·운영 모드 확인을 맡고 탑승 안전의 적합성은 로봇·승강기 쪽 표준에 맡기는 경계가 될 것으로 보인다. 개정 초안 내용이 최종판에 남았는지는 확인하지 못했다(oq-254). | ref-945, ref-1425, ref-1117 | 아니오 | low | 2026-10-09 | 제약 | — |
| f25 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: Open-RMF 기능 요청 이슈 #658 은 화재경보가 울리면 로봇들이 주차 위치로 이동하지만, 비상 신호가 대상 플릿을 구분하지 않는 불리언 값이라고 지적한다. | ref-567 | 아니오 | medium | 2025-04-04 | 시작 조건 | 원문 미열람 |
| f26 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: ISO 21423(산업용 이동로봇 통신·상호운용성)의 범위는 여러 제조사 AMR·플릿 관리 장비·기업 자원 사이의 통신 프로토콜이다. 안전 요구와 공공 도로 이동 기계는 범위에서 뺀다. | ref-159 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f27 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 과 ISO 21423 같은 상호운용 표준이 안전 요구를 범위에서 빼므로, 연동 적합성 시험(21. 상호운용 표준·적합성)과 안전 표준 적합성·인증(50. 안전 표준·인증·사고 조사)은 별도 경로로 관리해야 할 것으로 보인다. | ref-031, ref-159 | 아니오 | low | 2026-10-09 | — | — |
| f28 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Kazemi Eskeri 외(IROS 2025)는 사람과 함께 쓰는 환경에서 사람을 고려하는 다중 로봇 작업 배정 방법을 다뤘다. | ref-1083 | 아니오 | medium | 2025-08-27 | 수행 자원 | 원문 미열람 |
| f29 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: Open-RMF 데모에서는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. | ref-104 | 아니오 | medium | 2026-10-09 | 예외·성과 | 원문 미열람 |
| f30 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f31 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Reliability Engineering & System Safety 게재 연구(2023)는 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 확률 페트리넷(SPN)으로 모델링·분석했다. | ref-565 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f32 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 안전 상태(safetyState)는 activeEmergencyStop 을 MANUAL(로봇에서 수동 확인), REMOTE(시설 비상정지를 원격 확인), NONE 으로 보고하고, fieldViolation 으로 레이저·범퍼 같은 보호 필드 침범 여부를 보고한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f33 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성·31. 사람–로봇 협업: ROP 의 재개 지시는 비상정지가 NONE 이고 운용 모드가 AUTOMATIC 으로 돌아온 것을 확인한 뒤에 내려야 할 것으로 보인다. MANUAL 비상정지는 로봇에서 사람이 확인해야 하므로 현장 인력 출동이 복구 절차에 들어갈 것으로 보인다(oq-095). | ref-031 | 아니오 | low | 2026-10-09 | 완료·인계 | — |
| f34 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f35 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 2026-09 식품 제조 공장에서 멈춘 제품 적재 로봇을 점검하던 노동자가 끼여 숨진 사고에 대해, 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다. | ref-1125 | 아니오 | low | 2026-09-29 | 제조 공장 / 제약 | 원문 미열람 |
| f36 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 2023-11 농산물유통센터에서 상자를 팔레트로 옮기는 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌다. | ref-1124 | 아니오 | low | 2023-11-08 | 물류창고 / 예외·성과 | 원문 미열람 |
| f37 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 확인한 두 사망 사고가 모두 점검·작동 확인 같은 비정상 작업 중에 났으므로, ROP 가 정지 뒤 재가동·재개를 지시하기 전에 작업 중인 사람과 잠금 상태를 확인하는 절차가 복구 절차와 운영 절차의 접점이 될 것으로 보인다. | ref-1124, ref-1125, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f38 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 만들어, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. | ref-1303 | 아니오 | medium | 2020-11-20 | 예외·성과 | 원문 미열람 |
| f39 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션에 쓴다. | ref-406 | 아니오 | medium | 2026-10-09 | 상업 시설 / 제약 | — |
| f40 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Rondoni 외(Scientific Reports, 2024-08)는 모의 병원 환경에서 병원 물류 로봇 HOSBOT 과 TIAGo 를 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 7개 지표로 비교했다. 최고 속도에서는 방향 오차가 커졌다. | ref-1081 | 아니오 | medium | 2024-08-07 | 병원 / 제약 | 원문 미열람 |
| f41 | [추정] | 연계 대상: M. 안전의 50. 안전 표준·인증·사고 조사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Wind River 인터뷰(2014)는 IEC 61508-7 이 시뮬레이션을 시험 목적의 설비 거동 모사로 정의한다고 인용하고, 기능안전 표준이 안전 확인에 시뮬레이션을 권고한다고 해석했다. 그러나 이동로봇 안전 인증이 시뮬레이션 결과를 근거로 받아들이는 절차는 찾지 못했다. | ref-1312 | 아니오 | low | 2014-11-20 | — | 원문 미열람 |
| f42 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Winfield 외(2022-05)는 사회적 로봇의 사고 조사를 위한 윤리적 블랙박스(Ethical Black Box) 개방 표준 초안을 제안했다. | ref-1120 | 아니오 | medium | 2022-05-13 | 예외·성과 | 원문 미열람 |
| f43 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: Sanders·Sener·Chen(Applied Ergonomics, 2024)은 미국 OSHA 중대 부상 보고(Severe Injury Reports)에서 작업장 로봇 관련 부상을 분석했다. | ref-1122 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f44 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 플릿 수준에서 명령·정지·재가동·운용 모드 전환·안전 상태 보고를 시각과 함께 남기는 실행 기록이 사고·아차 사고 조사의 입력이 될 것으로 보인다. 그 최소 항목을 정한 표준은 확인하지 못했다(oq-252). | ref-1120, ref-1122, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f45 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Ferrando 외(2020)의 ROSMonitoring 은 ROS 응용의 형식 속성을 ROS 바깥에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 여러 ROS 배포판에 옮겨 쓸 수 있고 특정 명세 형식에 묶이지 않는다. | ref-1426 | 아니오 | medium | 2020-12-03 | — | — |
| f46 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 진입 금지 구역 위반이나 정지 지시 뒤 응답처럼 안전과 관련된 운영 규칙을 실행 중에 감시하는 런타임 검증이 38. 모니터링·이상 탐지·원인 분석과 48. 안전·위험 관리를 잇는 방법이 될 것으로 보인다. 다만 제조사가 다른 플릿에 적용한 사례는 확인하지 못했다. | ref-1426, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f47 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: ANSI/A3 R15.08-3-2026 은 산업용 이동로봇을 운영하는 사용자에게 위험성평가와 그 결과 위험 감소 조치의 유지, 변경 관리, 직원 교육과 안전 작업 절차를 요구한다. | ref-1419, ref-1421 | 예 | medium | 2026-10-04 | — | — |
| f48 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: R15.08-3 의 사용자 교육·안전 작업 절차 요구는 40. 운영 절차·요청 창구의 현장 절차와 56. 운영 이관·확대·교육의 교육 계획으로 넘어갈 것으로 보인다. 여러 제조사 로봇이 섞인 현장에서 누가 이를 이행하는지는 확인하지 못했다(oq-265). | ref-1419, ref-1421 | 아니오 | low | 2026-10-09 | — | — |
| f49 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: FORT Robotics 사례 소개에 따르면, 한 창고의 울타리 친 AMR 구역에서 문에 단 주 제어기가 문이 열리면 모든 로봇에 무선 안전 비상정지를 보낸다. 이 시스템은 ISO 13849 범주 3·PLd 로 설계됐다고 한다. | ref-1422 | 아니오 | low | 2023-05-18 | 물류창고 / 예외·성과 | 벤더 주장 |
| f50 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 은 안전 표준이 아니고, 연결이 끊긴 로봇은 받은 주문을 이어 수행한다. 따라서 플릿 일괄 정지는 관제 메시지 경로가 아니라 그와 독립된 안전 등급 정지 경로에 맡기고, ROP 는 정지 결과를 상태로 받아 작업을 보류·재배정하는 구조가 두 대분류의 경계가 될 것으로 보인다(oq-095). | ref-031, ref-1422 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f51 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act(Regulation (EU) 2024/1689)는 부속서 I 의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이면서 제3자 적합성 평가를 받는 AI 시스템을 고위험 AI 로 분류한다. | ref-621 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f52 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법무법인 태평양 해설에 따르면 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을 정하게 하고, 운영 단계에서 성능 저하·오류의 정기 점검과 관리자 교육을 요구한다. | ref-1341 | 아니오 | medium | 2025-09-30 | 예외·성과 | 원문 미열람 |
| f53 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영: AI 가 정지·경로·구역 결정에 관여하면 실행 전 안전 게이트 같은 채택 검사는 47. AI·학습·적응과 모델 운영의 채택 기준과 48. 안전·위험 관리의 위험성평가 양쪽에 걸칠 것으로 보인다. 이런 AI 가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106). | ref-621, ref-417 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f54 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. | ref-1116, ref-1076 | 예 | medium | 2026-09-18 | — | — |
| f55 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EN ISO 10218-1:2025·-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015 에 따라 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다. | ref-1116 | 아니오 | medium | 2026-09-18 | — | — |
| f56 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1304 | 아니오 | medium | 2022-11-17 | — | 원문 미열람 |
| f57 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제와 사람 위치·영상 데이터 처리도 안전 평가 대상이 될 것으로 보인다. | ref-1116, ref-1425 | 아니오 | low | 2026-10-09 | 제약 | — |
| f58 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: Belzile 외(2025-02)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 여러 배치 상황에 적용할 수 있는 표준이 없다고 보았다. 이에 건설 현장 이동로봇 배치 전에 쓸 위험성평가 틀을 제안했다. | ref-563 | 아니오 | medium | 2025-02 | 기타 / 제약 | 원문 미열람 |
| f59 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 법령해석 23-0872(2023-11-21)는 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 '산업용 로봇'을 쓰는 작업으로 한정되지 않는다고 회답했다. KS B ISO 8373 의 '로봇'이 산업용·서비스용·의료용을 포괄한다는 점을 근거로 들었다. | ref-1423 | 아니오 | medium | 2023-11-21 | 제약 | — |
| f60 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 해석에 따르면 서비스·이동 로봇을 쓰는 작업도 로봇작업 특별교육 대상이 될 수 있으므로, ROP 를 들인 현장의 운영 이관 교육 계획에 법정 특별교육 해당 여부 판단이 들어가야 할 것으로 보인다. 고용노동부의 적용 지침은 확인하지 못했다(oq-275). | ref-1423 | 아니오 | low | 2026-10-09 | — | — |
| f61 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: R15.08-3 은 공급자가 배치한 뒤 사용자가 산업용 이동로봇이나 그 적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다고 한다. | ref-1419 | 아니오 | medium | 2026-09-17 | — | — |
| f62 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROP 에서 구역·속도 제한·경로망·운영 정책을 바꾸는 일이 사용자 쪽 변경 관리와 위험성 재평가의 계기가 될 수 있으므로, 설정 변경 이력을 판 단위로 남기고 재평가 필요 여부를 표시하는 기능이 두 영역을 잇는 것으로 보인다(oq-093, oq-282). | ref-1419, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f63 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Francis 외(2023)는 사회적 로봇 내비게이션 알고리즘의 평가 원칙과 지침을 정리했다. | ref-1079 | 아니오 | medium | 2023-06-29 | — | 원문 미열람 |
| f64 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: ANSI/A3 R15.08-2(2023-10)는 산업용 이동로봇 시스템과 적용의 안전 요구를 다루는 2부로 발표됐다. | ref-472, ref-1084 | 아니오 | medium | 2023-10 | — | 원문 미열람 |
| f65 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거하며, 인증 절차와 기준은 산업통상자원부 고시(2023-11-17)로 정해졌다. | ref-980, ref-1118 | 아니오 | medium | 2023-11-17 | 실외 / 제약 | 원문 미열람 |
| f66 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 산업용 로봇의 운전 중 위험 방지 조치를 정한다. 같은 조는 한국산업표준이나 국제 안전기준에 맞는 경우 방책 같은 조치를 생략할 수 있게 한다. | ref-562 | 아니오 | medium | 2023-07-01 | 제약 | 원문 미열람 |
| f67 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명을 면담하고 공동설계 워크숍을 연 결과, 이동장애인이 보도 로봇과 보도 공간을 두고 경쟁한다고 느끼고 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. | ref-1214 | 아니오 | medium | 2024-04-07 | 실외 / 작업 대상 | 원문 미열람 |
| f68 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 61. 물류창고: 아마존은 자사 풀필먼트 센터에서 직원이 로보틱스 테크 조끼를 켜고 로봇 구역에 들어가면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다고 설명한다. | ref-1080 | 아니오 | low | 2026-10-09 | 물류창고 / 제약 | 원문 미열람, 벤더 주장 |
| f69 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ Q. 현장 유형별 적용의 65. 가정·공동주택: Webb 외(2021)는 지원 주거 아파트에서 넘어진 거주자를 보조 로봇이 직원에게 알리지 못한 모의 사고를, 역할극 증언 면담과 윤리적 블랙박스 기록으로 조사하는 방법을 시험했다. | ref-1121 | 아니오 | medium | 2021-06-29 | 가정 / 예외·성과 | 원문 미열람 |
| f70 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 66. 실외: 한국로봇산업진흥원은 실외이동로봇 운행안전인증 대상을 최고 속도 15km/h 이하·최대 질량 500kg 이하로 두고 주변 인식과 비상정지를 심사하며, 인증 뒤 2년 주기 정기점검을 둔다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/86749.html | 예 |
| ref-161 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 2025-05 | 논문 | medium | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/02783649241287797 | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/83545.html | 예 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-10-09 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-562 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 예 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2502.20693 | 예 |
| ref-565 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 예 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-621 | European Commission | AI Act \| Shaping Europe's digital future | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 예 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-10-09 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.17822 | 예 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2306.16740 | 예 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | 벤더 문서 | low | 2026-10-09 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 예 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 예 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2508.19731 | 예 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | low | 2026-10-09 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-09 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 아니오 |
| ref-1117 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | 표준 | medium | 2026-10-09 | https://iss.rs/en/project/show/iso:proj:83498 | 예 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | medium | 2026-10-09 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 예 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2205.06564 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | medium | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 예 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-10-09 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 예 |
| ref-1124 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202311081103001 | 예 |
| ref-1125 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | 기사 | low | 2026-10-09 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 예 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | 정부·연구기관 | medium | 2026-10-09 | https://iliad-project.eu/concluding-iliad/ | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | low | 2026-10-09 | https://v.daum.net/v/bc4riunbUE | 예 |
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2404.05050 | 예 |
| ref-1303 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 2020-11-20 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2011.10294 | 예 |
| ref-1304 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 예 |
| ref-1312 | Wind River (Engblom, J. 인터뷰, Buchwieser, A.) | Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser | 2014-11-20 | 벤더 문서 | low | 2026-10-09 | https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser | 예 |
| ref-1337 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv) | Jailbreaking LLM-Controlled Robots | 2024-10-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.13691 | 예 |
| ref-1338 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv) | Safety Guardrails for LLM-Enabled Robots | 2025-03-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-1341 | 법무법인 태평양(BKL) AI팀 | AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인 | 2025-09-30 | 업계 보고서 | medium | 2026-10-09 | https://www.bkl.co.kr/law/insight/newsletter/6248 | 예 |
| ref-1419 | ANSI (American National Standards Institute) Blog | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 2026-09-17 | 표준 | medium | 2026-10-09 | https://blog.ansi.org/?p=190868 | 아니오 |
| ref-1420 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 2026-04-23 | 표준 | medium | 2026-10-09 | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download | 아니오 |
| ref-1421 | Robotics 24/7 | A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available | 2026-10-04 | 기사 | medium | 2026-10-09 | https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available | 아니오 |
| ref-1422 | FORT Robotics (A3 Case Studies 게재) | Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs | 2023-05-18 | 벤더 문서 | low | 2026-10-09 | https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs | 아니오 |
| ref-1423 | 법제처 (네플라 위키 게재본) | [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련) | 2023-11-21 | 정부·연구기관 | medium | 2026-10-09 | https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k | 아니오 |
| ref-1424 | 메트로신문 (한용수) | 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막 | 2023-11-16 | 기사 | medium | 2026-10-09 | https://www.metroseoul.co.kr/article/20231116500208 | 아니오 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 2024-10 | 표준 | medium | 2026-10-09 | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 | 아니오 |
| ref-1426 | Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS) | ROSMonitoring: A Runtime Verification Framework for ROS | 2020-12-03 | 논문 | medium | 2026-10-09 | https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/ | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/index.md | 5. 다른 대분류와의 연결 | category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1·f2(2, oq-096), f3(1), f4·f5(3, 실외 보험) / B. 로봇 온톨로지: f6·f7(6, 실행 시점 조건에 운용 모드·안전 상태), f8(4) / C. 채팅 기반 구성·운영: f9(12), f10·f11·f12(13), 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f13·f14·f15(16, oq-229), f16(15, oq-170), f17(15, 연계 대상) / E. 사물·사람·실시간 상태: f18·f19(18), f20·f21(19) / F. 연동: f22·f23·f24(22, oq-254), f25(20), f26·f27(21) / G. 계획·최적화: f28(25), f29(28), f30·f31(27) / H. 실행·협업·예외 복구: f32·f33(29·31, oq-095), f34(32), f35·f36·f37(32·40) / I. 설계·시뮬레이션: f38(34·36), f39·f40(34), f41(36, 연계 대상) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현(f18·f19)과 구분 / J. 현장 운영·관제: f42·f44(37, oq-252), f43·f45·f46(38), f47·f48(40, oq-265) / K. 플랫폼 아키텍처·인프라: f49(벤더 주장)·f50(42, oq-095) / L. AI·학습 기술: f51·f52·f53(47, oq-106) / N. 보안·개인정보: f54·f57(51·52, oq-102), f56(52), f23·f57(53) / O. 검증·도입·수명주기: f45·f63(54), f58(55), f52·f59·f60(56, oq-275), f61·f62(57, oq-093·oq-282) / P. 거버넌스·법규·사회: f2·f64(58), f4·f55·f65·f66(59), f67(60) / Q. 현장 유형별 적용: f36·f49·f68(61 물류창고), f35(62 제조 공장), f20·f40(63 병원·의료), f39(64 상업 시설, 시뮬레이션 예제), f69(65 가정·공동주택), f4·f67·f70(66 실외), f58(67 기타 현장). 벤더 주장 f49·f68 은 [추정]과 '벤더 주장'을 병기하고, 연계 대상 f17·f41 과 로봇 자체 안전 기능·승강기 모드 제어·SLAM 은 '연계 대상'으로 짧게 쓴다. 상호운용 규격(VDA 5050·ISO 21423)은 안전 표준이 아니라는 점(f13·f26)을 유지한다. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설의 실제 현장 사례. 다음 실행 후보: 48. 안전·위험 관리(이전 분류 기준) 10절에 f32·f33·f47·f61·f54 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 변경 관리 | Management of Change (MOC) | 설비·적용·운영 환경이나 설정을 바꿀 때 그 변경이 만드는 위험을 다시 평가하고 기록·승인하는 절차로, ANSI/A3 R15.08-3 이 산업용 이동로봇 사용자에게 요구하는 항목 가운데 하나다. |
| 안전 상태 보고 | Safety State (VDA 5050 safetyState) | VDA 5050 상태 메시지에서 로봇이 활성 비상정지의 종류(MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 관제에 알리는 항목이다. |
| 무선 안전 비상정지 | Wireless Safety-rated Emergency Stop | 관제 통신과 별도의 안전 등급 무선 경로로 여러 이동로봇을 한꺼번에 멈추게 하는 비상정지 방식이다. |

## 열린 질문

새로 생긴 질문:

- 관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? | 관련 영역: 48. 안전·위험 관리, 42. 분산 시스템·통신·컴퓨팅 구조, 29. 명령·작업 실행의 신뢰성 | 근거: f49 | 종류: 일반
- ISO 13482 개정 초안(ISO/DIS 13482:2024)의 승강기 협동 로봇 요구(부속서 H)는 국내 KS B 7317 과 어떻게 대응하며, 이 요구가 최종판에 남았는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 22. 설비·건물 시스템 연동 | 근거: f23 | 종류: 일반
- 진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? | 관련 영역: 48. 안전·위험 관리, 38. 모니터링·이상 탐지·원인 분석, 54. 시험·형식 검증·벤치마크 | 근거: f46 | 종류: 일반
- 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 66. 실외 | 근거: f5 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 48 · 교차 확인: 2
- 예산 사용량: 검색 11회 · 신규 출처 8건
- 미확인 항목:
    - EU 기계류 규정 (EU) 2023/1230 원문(ref-555)을 EUR-Lex 에서 두 번 열었으나 빈 본문이 돌아와 실질적 변경 정의·부속서 III 1.1.9 를 확인하지 못함(finding 으로 내지 않음)
    - Intertek 의 'EN ISO 13482:2026' 표기는 페이지가 403 으로 열리지 않아 쓰지 않음(ref-1117 의 FDIS 단계와 충돌 가능성 미확인)
    - 대한민국 정책브리핑(ref-991)은 ECONNRESET 으로 열지 못해 보험 의무 교차 확인 실패(f4 단일 출처)
    - 법무법인 지평 PDF 는 본문 추출 실패로 쓰지 않음
    - f49·f68 벤더 주장은 독립 출처로 확인하지 못함
    - f3 의 R15.08-3 발행일은 A3 판매 페이지 기준(2026-04-23)이며, 공개 발표(2026-10-04)와 날짜가 다름
    - ISO 10218-1:2025 사이버보안 요구의 조항 번호는 확인하지 못함(oq-102)
    - 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육의 교육 내용·시간은 확인하지 못함
    - 재사용 출처 40건은 이번 실행에서 다시 열지 않음
- 범위 경계 위반 의심:
    - f17: SLAM 위치추정 안전성은 원문 19장 '로봇 자체 지능·제어' 경계라 claim 을 '연계 대상: '으로 시작
    - f41: 기능안전 인증과 시뮬레이션 인정은 인증 기관·제조사 몫이라 '연계 대상: '으로 시작
    - f18·f19·f22·f24: 승강기 모드 제어와 탑승 안전은 시설·설비 제어 경계의 연계 대상이며, ROP 는 확인·요청 범위로만 서술
    - f9~f12·f32·f49: 비상정지 회로·보호 필드·무선 안전 정지 같은 안전 기능은 로봇 제조사·통합자 몫의 연계 대상이며, ROP 는 상태 수신과 작업 보류·재개로만 서술
    - f4·f5·f55·f59·f65·f66: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며, ROP 는 인증·운행 조건을 제약으로 반영하는 범위로만 연결
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 48·49·50 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-07, 2026-10-09-08)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 40건, 이번에 다시 연 것은 ref-031(github_raw)·ref-1116(webfetch) 2건이고 나머지 38건은 fetched false·source_unopened true). 신규 출처는 8건(ref-1419~ref-1426, 예약 구간 안)이고 모두 원문 페이지를 열었다. 다만 ref-1419·ref-1420·ref-1425 는 유료 표준의 공식 소개 자료여서 표준 본문은 보지 못했다. 검색 11회/30, 신규 출처 8건/15. 교차 확인 2건(f47 R15.08-3 사용자 의무, f54 ISO 10218 사이버보안). 벤더 주장 2건(f49·f68). 한국 자료: 신규 ref-1423(법제처 해석)·ref-1424(기사), 재사용 ref-562·ref-945·ref-980·ref-1118·ref-1124·ref-1125·ref-1181·ref-1341. 현장 유형: 물류창고·제조 공장·병원·상업 시설(시뮬레이션 예제)·가정·실외·기타 각 1건 이상이며, 상업 시설의 실제 현장 사례는 찾지 못했다. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f18·f19)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f38·f39)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f51~f53)은 적용 대상인 48. 안전·위험 관리와 함께 제안했다. 열린 질문 가운데 oq-095(f32·f33·f50), oq-254(f23·f24, 초안 기준), oq-265(f47·f48, 이행 주체 미확인), oq-275(f59·f60, 지침 미확인), oq-102(f54, 조항 미확인), oq-229(f15)에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)를 따라 '5'로 매겼다 [가정]. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/2026-09-25-46/research.md

```markdown
# 리서치 브리프 2026-09-25-46

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-46 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 18. 사람–로봇 협업·운영 인터페이스 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 피킹 단계의 사람 피커–운반 로봇 대기 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음 — 트랙 nl-task-chatbot 반영 제안 4건(지시·확인·되묻기·실행 전 확인) 대기
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음 — 트랙 반영 제안 2건 대기
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-009(교대조별 작업자 수와 로봇 수)가 이 영역과 관련

## 조사 질문

1. 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [분류원문]
2. 사람 피커와 AMR(Autonomous Mobile Robot, 자율이동로봇)이 함께 피킹할 때 대기·배치(batch)·속도·인원 구성을 어떻게 정하는가, 교대조별 작업자 수와 로봇 수를 함께 정하는 모델이 있는가? (oq-009 관련, 섹션 5·6·8 겨냥)
3. 승인·수동 전환·일시정지·비상정지 같은 사람 개입을 로봇–관제 인터페이스 표준(VDA 5050)과 오픈소스 관제(Open-RMF)는 어떤 필드·기능으로 다루는가? (섹션 6·7 겨냥)
4. 사람과 이동로봇이 같은 공간에서 일할 때 적용되는 안전 표준과 국내 규제·지침은 무엇이며, ROP 인터페이스가 맡을 부분은 어디까지인가? (섹션 7·9 겨냥)
5. 운영자에게 로봇 상태와 실패를 설명 가능하게 보여 주는 방법과 한 운영자가 감독할 수 있는 로봇 수에 관한 연구는 무엇이 있는가? (섹션 4·6·8 겨냥)
6. 트랙 nl-task-chatbot 이 제안한 반영 내용 6건(자연어 지시 제품, 음성 피킹 확인, 되묻기 방식, 실행 전 확인)은 이 영역 6·8절에 어떻게 넣을 수 있는가? (섹션 6·8, 27. AI·학습·적응과 모델 운영 연결)
7. 사람–로봇 협업 인터페이스에서 ROP 직접 범위와 연계 대상(로봇 본체 안전 기능, WMS 화면)의 경계는 어디인가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Žulj 외(2022)는 창고를 구역으로 나눠 구역마다 피커 1명을 두고, 피커가 통로에서 배치를 채운 뒤 교차 통로에서 기다리는 AMR에 넘기면 AMR이 출하 거점까지 운반하는 AMR 보조 피커–부품(picker-to-parts) 시스템을 다루며, AMR 보조로 피커의 비생산적 보행 시간을 줄일 수 있다고 본다. | ref-467 | 아니오 | medium | 2022 | 피킹 / 수행 자원 | 원문 미열람 |
| f2 | [사실] | Löffler·Boysen·Schneider(2023)는 AMR이 주문 용기를 싣고 선반 앞에서 기다리고 피커가 물품을 넣은 뒤 다른 대기 AMR로 옮겨 가며 출발점으로 돌아가지 않는 로봇 보조 피킹에서, 여러 AMR과 여러 피커의 조율을 작업 완료 시각(makespan) 최소화 문제로 다룬다. | ref-468 | 아니오 | medium | 2023 | 피킹 / 수행 자원 | 원문 미열람 |
| f3 | [사실] | Löffler 외(2023)는 확률적 피킹 시간이 일으키는 연쇄 지연(ripple effect)을 작업자를 작은 하위 집단으로 나누어 줄일 수 있고, 피커와 AMR의 이동 속도가 비슷해야 하며 AMR이 더 느리면 시스템 성과가 나빠진다고 보고한다. | ref-468 | 아니오 | medium | 2023 | 피킹 / 예외·성과 | 원문 미열람 |
| f4 | [사실] | Yang 외(IISE Transactions, 2026)는 협동 피킹을 로봇1–피커1, 로봇1–피커 다수, 피커1–로봇 다수, 피커 다수–로봇 다수의 네 모드로 나누고, 모드마다 포크–조인 대기행렬 네트워크(fork-join queueing network)와 피로–회복 모델로 투입할 피커 수와 로봇 수를 분석한다. | ref-469 | 아니오 | medium | 2026-03 | 피킹 / 수행 자원 | 원문 미열람 |
| f5 | [추정] | f1~f4 에 따르면 분류 원문의 질문(사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하기)은 인터페이스 단독이 아니라 구역·배치 구성, 피커와 로봇의 수 비율, 로봇 속도, 다음 작업 안내의 결합으로 풀리는 것으로 보이며, ROP 운영 인터페이스는 그 결정 결과(다음 대기 로봇 위치, 넘겨줄 배치)를 작업자에게 전달하는 접점이 될 것으로 보인다. | ref-467, ref-468, ref-469 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | 원문 미열람 |
| f6 | [사실] | VDA 5050 최신판 상태(state) 메시지 스키마는 이동로봇의 운용 모드(operatingMode)를 STARTUP·AUTOMATIC·SEMIAUTOMATIC·INTERVENED·MANUAL·SERVICE·TEACH_IN 일곱 값으로 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f7 | [사실] | VDA 5050 최신판 명세는 SEMIAUTOMATIC 모드에서 로봇이 관제 주문을 받되 운영자가 로봇 HMI(Human-Machine Interface)로 실행을 확인해야 하고, INTERVENED 모드에서는 운영자가 HMI로 제어를 넘겨받아 새 주문을 받지 않으며, MANUAL 모드에서는 관제가 주문을 보낼 수 없다고 설명한다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f8 | [사실] | VDA 5050 최신판 상태 스키마는 안전 상태(safetyState)로 비상정지 종류(activeEmergencyStop: 로봇에서 수동 확인하는 MANUAL, 시설 비상정지를 원격 확인하는 REMOTE, NONE)와 보호 필드 침범(fieldViolation)을 필수로 두고, 물리 버튼이나 즉시 동작으로 일시정지된 상태(paused)를 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | Open-RMF Web(rmf-web)은 Open-RMF 배치를 웹에서 시각화하고 제어하기 위한 패키지 모음으로, API 서버·API 클라이언트·대시보드 프레임워크로 구성된다. | ref-302 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Open-RMF 데모(rmf_demos)는 웹 대시보드에서 작업을 제출하고 로봇·작업 상태를 볼 수 있게 하며, 비상 경보(/fire_alarm_trigger 토픽)를 켜면 모든 로봇을 가장 가까운 주차 위치로 보낸다. | ref-104 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f11 | [사실] | ISO 3691-4:2023(제2판, 2020판 대체)은 무인 산업용 트럭과 그 시스템(차량, 제어 시스템, 하역 장치, 배터리 충전소, 적재물 인계 스테이션)의 안전 요구사항을 정하며, 사람 감지 설정·운전 모드·제동 같은 안전 기능 요구를 포함한다. | ref-470 | 아니오 | medium | 2023-06 | 제약 | 원문 미열람 |
| f12 | [사실] | ISO 10218-1:2025·ISO 10218-2:2025 개정판은 협동 적용(collaborative application) 안전 요구를 본문에 넣어 ISO/TS 15066 의 내용을 흡수하고, 기능 안전 요구를 명확히 하며 사이버보안 요구를 더했고, '협동로봇' 대신 '협동 적용'이라는 용어를 쓴다. | ref-471 | 아니오 | medium | 2025 | 제약 | 원문 미열람 |
| f13 | [사실] | ANSI/A3 R15.08 계열은 산업용 이동로봇(IMR)의 안전을 제조사 요구(1부), 현장 통합·적용 요구(2부, 2023), 사용자 책임(3부)으로 나누고, 2부는 IMR 또는 IMR 플릿을 현장에 통합·설정하는 요구를 정하며 조작기를 단 이동로봇(유형 C)까지 다룬다. | ref-472 | 아니오 | medium | 2023-10 | 제약 | 원문 미열람 |
| f14 | [사실] | 고용노동부·한국산업안전보건공단은 2023-07 '고정식·이동식 산업용 로봇의 협동작업 안전 가이드'를 배포해 감지기를 활용한 충돌방지 조치, 작업자의 안전한 이동·작업 방법, 충돌방지조치 점검표, 이동식 로봇 예시(완제품 이송 공정)를 제시했다. | ref-473, ref-474 | 아니오 | medium | 2023-07 | 제약 | 원문 미열람 |
| f15 | [사실] | 로봇신문 보도에 따르면 이 가이드는 로봇 이동 플랫폼이 비정상 작동할 때 긴급 정지할 수 있도록 작업자가 접근 가능한 위치에 비상정지장치를 두도록 한다. | ref-474 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f16 | [사실] | 중소벤처기업부·대구광역시 발표에 따르면 대구 이동식 협동로봇 규제자유특구 실증을 거쳐 이동식 협동로봇 안전기준 한국산업표준(KS)이 제정되었으며, 그 전에는 명확한 안전기준이 없어 작업공간 분리나 안전 울타리 설치가 필요했다. | ref-475 | 아니오 | medium | 2024-11 | 제약 | 원문 미열람 |
| f17 | [사실] | Das·Banerjee·Chernova(HRI 2021)는 계획 실행 중 예기치 않은 실패의 원인을 비전문가에게 설명하는 방식을 비교해, 실패의 맥락과 지난 행동 이력을 담은 설명이 비전문가의 실패·해결책 파악에 가장 효과적이었다고 보고한다. | ref-476 | 아니오 | medium | 2021-01 | 예외·성과 | 원문 미열람 |
| f18 | [사실] | 상황 인식 기반 에이전트 투명성(SAT) 모델은 에이전트의 현재 행동·계획(1수준), 추론(2수준), 미래 결과 예측(3수준)을 운영자에게 보여 주는 틀이며, 관련 연구에서 높은 수준의 투명성 화면이 운영자의 상황 인식과 신뢰를 높였다고 보고된다. | ref-477 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f19 | [사실] | 한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수(팬아웃, fan-out)는 운영자가 방치해도 로봇 성과가 유지되는 정도(neglect tolerance)와 로봇 하나를 다루는 데 드는 상호작용 시간에 따라 정해진다는 척도가 제안되어 있다. | ref-478 | 아니오 | medium | 2004 | 수행 자원 | 원문 미열람 |
| f20 | [사실] | 독일 연방산업안전보건연구소(BAuA) 연구자의 문헌 고찰(Rey-Becerra·Wischniewski, Ergonomics, 2025)은 한 사람이 여러 로봇을 감독하는 시스템 연구 44건을 분석해 효율·유연성의 이점과 함께 주의·인지 부하 관리의 어려움을 지적하고, 설계·평가용 점검표를 제시했다. | ref-479 | 아니오 | medium | 2025-07-11 | 수행 자원 | 원문 미열람 |
| f21 | [추정] | 국내 물류 로봇 업체 플로틱스는 100평 규모 물류센터 환경에서 작업자 2명이 로봇 6대와 존피킹을 수행하는 구성을 시연했다고 보도되었다. | ref-480 | 아니오 | low | 2023-12-22 | 피킹 / 수행 자원 | 원문 미열람, 벤더 주장 |
| f22 | [사실] | 음성 피킹은 시스템이 위치와 수량을 음성으로 지시하고 작업자가 위치 체크 디지트·수량 같은 짧은 음성 응답으로 동작마다 확인하는 방식이다. | ref-272, ref-275 | 예 | medium | 2026-09-25 | 피킹 / 완료·인계 | 원문 미열람 |
| f23 | [추정] | Locus Robotics 는 협동 피킹 로봇 화면에 품목·위치·수량을 보여 주고 선택 기능으로 위치·용기 바코드 스캔 뒤 화면 확인을 받는다고 설명한다. | ref-279 | 아니오 | low | 2026-09-25 | 피킹 / 완료·인계 | 원문 미열람, 벤더 주장 |
| f24 | [추정] | InOrbit 는 RobOps Copilot 을 2024년에 로봇 운영 데이터에 대한 자연어 질의·설명 기능으로 발표했다. | ref-176, ref-278 | 아니오 | low | 2024-05 | — | 원문 미열람, 벤더 주장 |
| f25 | [사실] | Rasa 3.x 의 폼(Forms)은 필요한 슬롯 목록을 정해 두고 비어 있는 필수 슬롯을 사용자에게 차례로 묻는 방식으로 작업 지향 대화의 되묻기를 구현한다. | ref-356 | 아니오 | medium | 2026-09-25 | 시작 조건 | 원문 미열람 |
| f26 | [사실] | KnowNo(CoRL 2023)는 LLM 계획기의 선택지 불확실성을 등각 예측(conformal prediction)으로 재어 불확실할 때 사람에게 도움을 요청하게 하는 방법이다. | ref-351 | 아니오 | medium | 2023-07 | 시작 조건 | 원문 미열람 |
| f27 | [사실] | CLARA(IEEE RA-L 2024, 고려대 등)는 사용자 명령을 명확·모호·수행 불가로 분류하고 모호한 명령에는 되묻는 질문을 생성하는 방법이다. | ref-353 | 아니오 | medium | 2024 | 시작 조건 | 원문 미열람 |
| f28 | [사실] | SafeGate(Purdue, 2026)는 LLM 이 해석한 자연어 명령에서 안전 속성을 추출해 실행 전에 결정적 규칙으로 승인·거부하는 게이트를 제안하며, ISO 13482(개인 돌봄 로봇) 기반이고 물류 현장 평가는 없다. | ref-417 | 아니오 | medium | 2026-04 | 제약 | 원문 미열람 |
| f29 | [추정] | 연계 대상: Mecalux 는 WMS(Easy WMS)의 생성형 AI 비서가 채팅 지시를 실행하기 전에 수행할 동작과 영향을 요약해 보여 주고 채팅으로 확인을 받는다고 설명한다. | ref-418 | 아니오 | low | 2026-09-25 | 완료·인계 | 원문 미열람, 벤더 주장 |
| f30 | [추정] | f7·f22·f25~f29 를 나란히 놓으면 운영 인터페이스의 확인은 대상과 시점에 따라 로봇 동작 실행 전 운영자 확인(VDA 5050 SEMIAUTOMATIC), 작업자 동작마다의 확인(음성 체크 디지트), 자연어 지시의 해석 확인(되묻기·실행 전 게이트)으로 구분되는 것으로 보인다. | ref-031, ref-272, ref-275, ref-356, ref-417 | 아니오 | low | 2026-09-25 | 완료·인계 | — |
| f31 | [추정] | 연계 대상: 사람 감지·보호 필드·비상정지 회로·속도와 거리 감시 같은 안전 기능은 로봇 제조사와 현장 통합사가 ISO 3691-4·ISO 10218·R15.08 에 따라 갖추는 것이므로, 이종 로봇을 연결하는 ROP 는 운용 모드·안전 상태의 표시, 작업 재개·수동 전환의 승인 흐름, 구역·권한 설정 반영을 맡는 경계가 될 것으로 보인다. | ref-470, ref-472, ref-051 | 아니오 | low | 2026-09-25 | 제약 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-467 | Žulj, I., Salewski, H., Goeke, D., & Schneider, M. | Order batching and batch sequencing in an AMR-assisted picker-to-parts system | 2022 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616 | 예 |
| ref-468 | Löffler, M., Boysen, N., & Schneider, M. | Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers | 2023 | 논문 | medium | 2026-09-25 | https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207 | 예 |
| ref-469 | Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M. | Deploying pickers and robots in cobot-based collaborative order picking systems | 2026-03 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 미확인 | 업계 보고서 | medium | 2026-09-25 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 예 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 2023-07 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 | 예 |
| ref-474 | 로봇신문 | '이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나? | 미확인 | 기사 | low | 2026-09-25 | https://www.irobotnews.com/news/articleView.html?idxno=32130 | 예 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 2024-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 | 예 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 2021-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2101.01625 | 예 |
| ref-477 | Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 미확인 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 예 |
| ref-478 | Olsen, D. R. 외(CHI 2004) | Fan-out: measuring human control of multiple robots | 2004 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/985692.985722 | 예 |
| ref-479 | Rey-Becerra, E., & Wischniewski, S. | Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance | 2025-07-11 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316 | 예 |
| ref-480 | ZDNet Korea | "대형 물류센터 집품 작업, 로봇 6대로 효율화" | 2023-12-22 | 기사 | low | 2026-09-25 | https://zdnet.co.kr/view/?no=20231222165139 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf-web | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-272 | Lucas Systems | Voice-Directed Warehousing - Solutions \| Lucas Systems | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.lucasware.com/voice-directed-warehousing/ | 예 |
| ref-275 | USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.) | System and method for generating and updating location check digits (US 8868519) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519 | 예 |
| ref-279 | Locus Robotics | Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://locusrobotics.com/locusone/automated-warehouse-software/user-interface | 예 |
| ref-176 | InOrbit.AI | InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024 | 2024-05 | 벤더 문서 | low | 2026-09-25 | https://www.inorbit.ai/press/inorbit-robops-copilot | 예 |
| ref-278 | InOrbit.AI | InOrbit RobOps Copilot - Bring AI power to robot operations | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.inorbit.ai/robopscopilot | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.10376 | 예 |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-418 | Mecalux | Mecalux integrates generative AI into Easy WMS | 미확인 | 벤더 문서 | low | 2026-09-25 | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절 왜 중요한가: f1·f2·f3·f5(사람 피커–로봇 대기 문제), f20(감독 인지 부하) / 4절 용어: f6·f7(운용 모드), f18(SAT), f19(팬아웃), f12(협동 적용) / 5절 시나리오: 피킹 단계 f1·f2·f3·f5·f22 (시작 조건·수행 자원·완료·인계·예외·성과), f21 은 벤더 주장 병기 / 6절 접근법: 협동 피킹 조율 f1~f4, 운용 모드·일시정지·비상정지 f6~f8, 관제 대시보드 f9·f10, 설명·투명성 f17·f18, 트랙 nl-task-chatbot 반영 제안 6건 검토 결과 f22~f30(음성 확인, 벤더 자연어 제품 f23·f24 벤더 주장, 되묻기 f25~f27, 실행 전 게이트 f28, WMS 연계 사례 f29, 확인 유형 정리 f30) — 27. AI·학습·적응과 모델 운영과 양쪽 연결 / 7절 표준·오픈소스: f6~f8(VDA 5050), f9·f10(Open-RMF), f11(ISO 3691-4), f12(ISO 10218:2025), f13(R15.08), f14~f16(국내 가이드·KS) / 8절 연구·자료: f1~f4, f17~f20, 트랙 제안 자료 f25~f28 / 9절 범위: f31(안전 기능은 연계 대상, ROP 는 모드 표시·승인 흐름), f29(WMS 는 연계 대상) / 10절 연결: 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링(f1~f4), 3. 처리능력·거점·설비 계획(f4, oq-009), 9. 로봇·제조사 관제 연동(f6~f8), 20. 예외 복구·재계획·업무 연속성(f10·f17), 19. 모니터링·이상 탐지·원인 분석(f17·f18), 25. 안전·위험 관리(f11~f16), 27. AI·학습·적응과 모델 운영(f24~f28) / 11절 열린 질문: oq-009 와 새 질문 4건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 팬아웃 | Fan-out (human-robot team) | 한 사람이 동시에 효과적으로 다룰 수 있는 로봇 수로, 로봇의 방치 허용도와 로봇 하나를 다루는 상호작용 시간으로 추정한다. |
| 운용 모드 | Operating Mode (VDA 5050 operatingMode) | VDA 5050 에서 이동로봇이 관제 주문을 자동 실행하는지, 운영자 확인이 필요한지, 운영자가 제어를 넘겨받았는지 등을 알리는 상태 값이다. |
| 상황 인식 기반 에이전트 투명성 | Situation Awareness-based Agent Transparency (SAT) | 자율 에이전트의 현재 행동·계획, 추론, 미래 결과 예측을 세 수준으로 운영자에게 보여 주어 상황 인식과 신뢰를 돕는 인터페이스 설계 모델이다. |
| 협동 적용 | Collaborative Application | ISO 10218:2025 에서 로봇 자체가 아니라 사람과 로봇이 함께 일하도록 설계된 적용 방식을 기준으로 안전을 판단하기 위해 '협동로봇' 대신 쓰는 용어이다. |

## 열린 질문

새로 생긴 질문:

- 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 25. 안전·위험 관리 | 근거: f16 | 종류: 일반
- 국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 4. 성과·경제성·프로세스 개선 | 근거: f5 | 종류: 일반
- VDA 5050 SEMIAUTOMATIC 모드의 실행 확인을 로봇 HMI 가 아닌 관제·ROP 화면에서 원격으로 할 수 있는지, 원격 확인에 필요한 안전 조건을 정한 규정이나 사례가 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 9. 로봇·제조사 관제 연동 | 근거: f7 | 종류: 일반
- 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? | 관련 영역: 18. 사람–로봇 협업·운영 인터페이스, 19. 모니터링·이상 탐지·원인 분석 | 근거: f19 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 28 · 교차 확인: 1
- 예산 사용량: 검색 28회 · 신규 출처 14건
- 미확인 항목:
    - 이동식 협동로봇 안전기준 KS 번호와 본문 미확인(f16)
    - f7 운용 모드 설명은 요약 도구 경유 원문 열람이라 명세 표 문구와 글자 단위 대조 미확인
    - f11~f13 표준 원문(유료) 미열람, 검색 요약·발행 기관 소개 기준
    - f12 ISO 10218:2025 는 ISO 공식 페이지가 아닌 A3 자료 기준
    - ref-477 발행 연도 미확인(TIES 게재, 2017 온라인 공개 추정)
    - ref-478 공저자 전체 미확인
    - f21 플로틱스 시연 수치 벤더 주장, 독립 확인 없음
    - oq-009 부분 관련: f4 가 피커·로봇 수 결정 모델을 주지만 교대조 단위 결정 여부 미확인 — 해결 제안하지 않음
    - 특구 참여기업 생산성 9.3% 증가(검색 요약)는 단일 발표·방법 미공개라 finding 으로 내지 않음
- 범위 경계 위반 의심:
    - f31: 사람 감지·보호 필드·비상정지 회로는 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이므로 '연계 대상: '으로 표시하고 ROP 는 표시·승인 흐름만 맡는다고 구분
    - f29: WMS 화면 기능은 상위 업무 시스템 쪽 연계 대상으로 표시
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031(VDA 5050 명세)·ref-051(state.schema)·ref-302(rmf-web README)·ref-104(rmf_demos README). 신규 ref-467~ref-480(예약 구간 안)과 그 밖의 재사용 출처는 원문 미열람(신뢰도 상한 medium). 검색 28회/30, 신규 출처 14건/15. 트랙 반영 제안 6건 처리: 제안 1(InOrbit 등)→f24, 제안 2(음성·Locus 확인)→f22·f23·f30, 제안 3(자료)→f22~f24 출처 재사용(Amazon Proteus·Formant·다임리서치는 이번 브리프에 다시 넣지 않음, 다음 실행 후보), 제안 4·5(되묻기 방식·자료)→f25~f27, 제안 6(실행 전 확인)→f28·f29. 한국 자료: 고용노동부 가이드(f14·f15), 중기부 KS 제정(f16), 국내 업체 시연 기사(f21). 27. AI·학습·적응과 모델 운영 관련 finding(f24~f28)은 27번 영역과 양쪽 연결하도록 10절 제안에 적음. 8. 실시간 세계 상태·데이터 일관성, 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 원격 조작(teleoperation) 관련 공개 자료는 벤더 블로그 위주라 finding 으로 내지 못함 — 원격 조작은 섹션 6에서 약한 부분으로 남음.
```

### data/source_texts/ref-004.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# RMF Core Overview

This chapter describes RMF, an umbrella term for a wide range of open specifications and software
tools that aim to ease the integration and interoperability of robotic systems,
building infrastructure, and user interfaces. `rmf_core` consists of:
 - [rmf_traffic](https://github.com/open-rmf/rmf_traffic): Core scheduling and traffic management systems
 - [rmf_traffic_ros2](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_traffic_ros2): rmf_traffic for ros2
 - [rmf_task](https://github.com/open-rmf/rmf_task): Task planner for rmf
 - [rmf_battery](https://github.com/open-rmf/rmf_battery): rmf battery estimation
 - [rmf_ros2](https://github.com/open-rmf/rmf_ros2): ros2 adapters and nodes and python bindings for rmf_core
 - [rmf_utils](https://github.com/open-rmf/rmf_utils): utility for rmf

## Traffic deconfliction

Avoiding mobile robot traffic conflicts is a key functionality of `rmf_core`.
There are two levels to traffic deconfliction: (1) prevention, and (2)
resolution.

### Prevention

Preventing traffic conflicts whenever possible is the best-case scenario.
To facilitate traffic conflict prevention, we have implemented a
platform-agnostic Traffic Schedule Database. The traffic schedule is a living
database whose contents will change over time to reflect delays, cancellations,
or route changes. All fleet managers that are integrated into an RMF deployment must
report the expected itineraries of their vehicles to the traffic schedule. With
the information available on the schedule, compliant fleet managers can plan
routes for their vehicles that avoid conflicts with any other vehicles, no
matter which fleet they belong to. `rmf_traffic` provides a
[`Planner`](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Planner.hpp)
class to help facilitate this for vehicles that behave like standard AGVs (Automated Guided Vehicles),
rigidly following routes along a pre-determined grid. In the future
we intend to provide a similar utility for AMRs (Autonomous Mobile Robots) that can perform ad hoc motion
planning around unanticipated obstacles.

### Negotiation

It is not always possible to perfectly prevent traffic conflicts.
Mobile robots may experience delays because of unanticipated obstacles in their
environment, or the predicted schedule may be flawed for any number of reasons.
In cases where a conflict does arise, `rmf_traffic` has a Negotiation scheme.
When the Traffic Schedule Database detects an upcoming conflict between two or
more schedule participants, it will send a conflict notice out to the relevant
fleet managers, and a negotiation between the fleet managers will begin. Each
fleet manager will submit its preferred itineraries, and each will respond with
itineraries that can accommodate the others. A third-party judge (deployed by
the system integrator) will choose the set of proposals that is considered
preferable and notify the fleet managers about which itineraries they should
follow.

There may be situations where a sudden, urgent task needs to take place
(for example, a response to an emergency), and the current traffic schedule does not
accommodate it in a timely manner. In such a situation, a traffic participant
may intentionally post a traffic conflict onto the schedule and force a
negotiation to take place. The negotiation can be forced to choose an itinerary
arrangement that favors the emergency task by implementing the third-party
judge to always favor the high-priority participant.

## Traffic Schedule

The traffic schedule is a centralized database of all the intended robot traffic
trajectories in a facility. Note that it contains the intended trajectories; it is
looking into the future. The job of the schedule is to identify conflicts in
the intentions of the different robot fleets and notify the fleets when a
conflict is identified. Upon receiving the notification, the fleets will begin
a traffic negotiation, as described above.

![Schedule and Fleet Adapters](images/rmf_core/schedule_and_fleet_adapters.png)

## Fleet Adapters

Each robot fleet that participates in an RMF deployment is expected to have a
fleet adapter that connects its fleet-specific API to the interfaces
of the core RMF traffic scheduling and negotiation system. The fleet adapter is
also responsible for handling communication between the fleet and the various
standardized smart infrastructure interfaces, e.g. to open doors, summon lifts,
and wake up dispensers.

Different robot fleets have different features and capabilities, dependent on
how they were designed and developed. The traffic scheduling and negotiation system
does not postulate assumptions about what the capabilities of the fleets will be.
However, to minimize the duplication of integration effort, we have identified 4
different broad categories of control that we expect to encounter among various
real-world fleet managers.

**Fleet adapter type** | **Robot/Fleetmanager API feature set**  | **Remarks**
--- | --- | ---
`Full Control` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Request robot to move to [x, y, yaw] coordinate</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Get route/path taken by robot to destination</li><li>ETA to destination</li><li>Read battery status of the robot</li><li>Infer when robot is done navigating to [x, y, yaw]</li><li>Send robot to docking/charging station</li><li>Switch on board map and re-localize robot.</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is provided with live status updates and full control over the paths that each individual mobile robot uses when navigating through the environment. This control level provides the highest overall efficiency and compliance with RMF, which allows RMF to minimize stoppages and deal with unexpected scenarios gracefully. *(API available)*
`Traffic Light` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Read battery status of the robot</li><li>Send robot to docking/charging station</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is given the status as well as pause/resume control over each mobile robot, which is useful for deconflicting traffic schedules especially when sharing resources like corridors, lifts and doors. *(API available)
`Read Only` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Read or infer the path that the robot will take to its current destination</li><li>Read average speed of the robot or ETA to destination</li><li>Read battery status of the robot</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is not given any control over the mobile robots but is provided with regular status updates. This will allow other mobile robot fleets with higher control levels to avoid conflicts with this fleet. _Note that any shared space is allowed to have a maximum of just one "Read Only" fleet in operation. Having none is ideal._ *(Preliminary API available)*
`No Interface` | | Without any interface to the fleet, other fleets cannot coordinate with it through RMF, and will likely result in deadlocks when sharing the same navigable environment or resource. This level will not function with an RMF-enabled environment. *(Not compatible)*

In short, the more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together.
Note again that there can only ever be one "Read Only" fleet in a shared space, as any two or more of such fleets will make avoiding deadlock or resource conflict nearly impossible.

Currently we provide a reusable C++ API (as well as Python bindings) for integrating the **Full Control** category of fleet management.
A preliminary ROS 2 message API is available for the **Read Only** category, but that API will be deprecated in favor of a C++ API
(with [Python bindings](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python/) available) in a future release.
The **Traffic Light** control category is compatible with the core RMF scheduling system, but we have not yet implemented a reusable API for it.
To implement a **Traffic Light** fleet adapter, a system integrator would have to use the core traffic schedule and negotiation APIs directly, as well as implement the integration with the various infrastructure APIs (e.g. doors, lifts, and dispensers).

The API for the **Full Control** category is described in the [Mobile Robot Fleets](./integration_fleets.md) section of the Integration chapter, and the **Read Only** category is described in the [Read Only Fleets](./integration_read-only.md) section of the Integration chapter.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:
…(발췌: 전체 207,642자 중 앞 11,074자)
```

### data/source_texts/ref-044.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
@prefix cbv:   <https://ref.gs1.org/cbv/> .
@prefix epcis: <https://ref.gs1.org/epcis/> .
@prefix gs1:   <https://gs1.org/voc/> .

@prefix dct:    <http://purl.org/dc/terms/> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix sw:     <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix vann:   <http://purl.org/vocab/vann/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

#################### Ontology

cbv: a owl:Ontology;
  rdfs:label "CBV Ontology";
  rdfs:comment """The Comprehensive Business Vocabulary defines various enumerations used by EPCIS.""";
  dct:creator <https://gs1.org/>;
  dct:publisher <https://gs1.org/>;
  dct:created  "2021-06-01"^^xsd:date;
  dct:modified "2021-09-30"^^xsd:date;
  # dct:issued   "2021-06-30"^^xsd:date; # after release
  rdfs:seeAlso epcis:, gs1: ;
  owl:versionInfo "2.0";
  vann:preferredNamespaceUri "https://ref.gs1.org/cbv/";
  vann:preferredNamespacePrefix "cbv".

<https://gs1.org/> a schema:Organization;
  schema:name "GS1";
  schema:description "GS1 is an international organization that sets the global standards in transport and logistics".

#################### Business Transaction Type

cbv:BTT  a                owl:Class , rdfs:Class ;
        rdfs:comment      "These identifiers may be used to populate the type attribute of a bizTransaction element in an EPCIS event."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Business Transaction Type"@en ;
        rdfs:subClassOf   cbv:TypeCode ;
        sw:term_status    "stable" .

cbv:BTT-bol  a            cbv:BTT ;
        rdfs:comment      "A document issued by a carrier to a shipper, listing and acknowledging receipt of goods for transport and specifying terms of delivery."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Bill of Lading"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:bol> ;
        sw:term_status    "stable" .

cbv:BTT-cert  a           cbv:BTT ;
        rdfs:comment      "A document confirming certain characteristics of an object (e.g. product), person, or organisation, typically issued by a third party."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Certificate"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:cert> ;
        sw:term_status    "stable" .

cbv:BTT-desadv  a         cbv:BTT ;
        rdfs:comment      "A document/message by means of which the seller or consignor informs the consignee about the despatch of goods. \nAlso called an 'Advanced Shipment Notice', but the value `desadv` is always used regardless of local nomenclature."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Despatch Advice"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:desadv> ;
        sw:term_status    "stable" .

cbv:BTT-inv  a            cbv:BTT ;
        rdfs:comment      "A document/message claiming payment for goods or services supplied under conditions agreed by the seller and buyer."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Invoice"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:inv> ;
        sw:term_status    "stable" .

cbv:BTT-pedigree  a       cbv:BTT ;
        rdfs:comment      "A record that traces the ownership or custody and transactions of a product as it moves among various trading partners."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Pedigree"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:pedigree> ;
        sw:term_status    "stable" .

cbv:BTT-po  a             cbv:BTT ;
        rdfs:comment      "A document/message that specifies details for goods and services ordered under conditions agreed by the seller and buyer."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Purchase Order"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:po> ;
        sw:term_status    "stable" .

cbv:BTT-poc  a            cbv:BTT ;
        rdfs:comment      "A document that provides confirmation from an external supplier to the request of a purchaser to deliver a specified quantity of material, or perform a specified service, at a specified price within a specified time. \n(Sometimes internally referred to as a 'Sales Order'.)"@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Purchase Order Confirmation"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:poc> ;
        sw:term_status    "stable" .

cbv:BTT-prodorder  a      cbv:BTT ;
        rdfs:comment      "An organisation-internal document or message issued by a producer that initiates a manufacturing process of goods."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Production Order"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:prodorder> ;
        sw:term_status    "stable" .

cbv:BTT-recadv  a         cbv:BTT ;
        rdfs:comment      "A document/message that provides the receiver of the shipment the capability to inform the shipper of actual goods received, compared to what was advised as being sent."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Receiving Advice"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:recadv> ;
        sw:term_status    "stable" .

cbv:BTT-rma  a            cbv:BTT ;
        rdfs:comment      "A document issued by the seller that authorises a buyer to return merchandise for credit determination."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Return Merchandise Authorisation"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:rma> ;
        sw:term_status    "stable" .

cbv:BTT-testprd  a        cbv:BTT ;
        rdfs:comment      "A document that provides a formal specification of a sequence of instructions for the purpose of verifying one or several criteria."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Test Procedure"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:testprd> ;
        sw:term_status    "stable" .

cbv:BTT-testres  a        cbv:BTT ;
        rdfs:comment      "A document that includes the outcome of the execution of a given test procedure."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Test Result"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:testres> ;
        sw:term_status    "stable" .

cbv:BTT-upevt  a        cbv:BTT ;
        rdfs:comment      "Event ID URI(s) of event(s) provided by an upstream supplier, such as packing and shipping events (e.g., as the basis for the inferred completeness of inbound aggregations)."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Upstream EPCIS Event"@en ;
        owl:sameAs        <urn:epcglobal:cbv:btt:upevt> ;
        sw:term_status    "stable" .

#################### Business Step

cbv:BizStep  a            owl:Class , rdfs:Class ;
        rdfs:comment      "These identifiers populate the bizStep field in an EPCIS event."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "Business Step ID"@en ;
        rdfs:subClassOf   cbv:TypeCode ;
        sw:term_status    "stable" .

cbv:BizStep-accepting
        a                 cbv:BizStep ;
        rdfs:comment      "Denotes a specific activity within a business process where an object changes possession and/or ownership."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "accepting"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:accepting> ;
        sw:term_status    "stable" ;
        skos:example      "Retailer X unloads a pallet on to the receiving dock. The numbers of cases on the pallet are counted. The pallets are disaggregated from the shipping conveyance. The quantity is verified against the delivery document (Freight Bill or Bill of Lading), notating any over, short or damaged product at the time of delivery. Typically this process releases freight payment and completes the contractual agreement with the carrier of delivering the product/assets to a specified location.\nA parcel carrier drops off five boxes at Distributor Y's DC. A person on the Receiving Dock signs that they accept the five boxes from the parcel carrier.\nA wholesaler is assigned a lot of fish at a fish auction, verifies the quantity and acknowledges receipt.\nA manufacturer's fork lift driver scans the IDs of components which have been removed from a consignment warehouse. In doing so, the components are added to the manufacturer's inventory."@en .

cbv:BizStep-arriving  a   cbv:BizStep ;
        rdfs:comment      "Denotes a specific activity within a business process where an object arrives at a location."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "arriving"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:arriving> ;
        sw:term_status    "stable" ;
        skos:example      "Truckload of a shipment arrives into a yard. Shipment has not yet been received or accepted."@en .

cbv:BizStep-assembling
        a                 cbv:BizStep ;
        rdfs:comment      "Denotes an activity within a business process whereby one or more objects are combined to create a new finished product. \nIn contrast to transformation, in the output of `assembling` the original objects are still recognisable and/or the process is reversible; hence, `assembling` would be used preferably in an Association Event or, alternatively, an Aggregation Event, but not a Transformation Event."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "assembling"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:assembling> ;
        sw:term_status    "stable" ;
        skos:example      "Computer parts (hard drive, battery, RAM) assembled into a consumer ready computer\nMaintenance, repair and overhaul processes involving components added to an assembly comprised of multiple parts.\nHealthcare kitting: a surgical kit including drug, syringe, and gauze are combined to create a new 'product': a *kit*."@en .

cbv:BizStep-collecting
        a                 cbv:BizStep ;
        rdfs:comment      "Denotes a specific activity within a business process where an object is picked up and collected for future disposal, recycling or re-used."@en ;
        rdfs:isDefinedBy  cbv: ;
        rdfs:label        "collecting"@en ;
        owl:sameAs        <urn:epcglobal:cbv:bizstep:collecting> ;
        sw:term_status    "stable" ;
        skos:example      "An organisation picks up disposed consumer electronics in an end of life state from various different organisations. After the goods are picked up, they typically are brought back and received into a Collection Centre\nRented or leased pallets are picked up and brought to a collection centre."@en .
…(발췌: 전체 69,067자 중 앞 10,819자)
```

### data/source_texts/ref-045.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
@prefix epcis:  <https://ref.gs1.org/epcis/> .
@prefix cbv:    <https://ref.gs1.org/cbv/> .
@prefix gs1:    <https://gs1.org/voc/> .

@prefix dct:    <http://purl.org/dc/terms/> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix sw:     <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix vann:   <http://purl.org/vocab/vann/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

#################### Ontology

epcis: a owl:Ontology;
  rdfs:label "EPCIS Ontology";
  rdfs:comment """The Electronic Product Code Information System (EPCIS) is a specification for capturing and exchanging event visibility data across the global logistics chain.
Version 2.0 is a major release that adds JSON, JSONLD and RDF payload formats, sensor reports, and other major features.""";
  dct:creator <https://gs1.org/>;
  dct:publisher <https://gs1.org/>;
  dct:created  "2021-06-01"^^xsd:date;
  dct:modified "2021-09-30"^^xsd:date;
  # dct:issued   "2021-06-30"^^xsd:date; # after release
  rdfs:seeAlso cbv:, gs1: ;
  owl:versionInfo "2.0";
  vann:preferredNamespaceUri "https://ref.gs1.org/epcis/";
  vann:preferredNamespacePrefix "epcis".

<https://gs1.org/> a schema:Organization;
  schema:name "GS1";
  schema:description "GS1 is an international organization that sets the global standards in transport and logistics".

#################### Meta-properties

epcis:jsonldLabel a owl:DatatypeProperty , rdf:Property ;
      rdfs:comment      """JSONLD term (alias) used for this property.
The default is the property local name, which is captured in rdfs:label."""@en ;
      rdfs:domain       rdf:Property;
      schema:domainIncludes rdf:Property ;
      rdfs:isDefinedBy  epcis: ;
      rdfs:label        "jsonldLabel" ;
      rdfs:range        xsd:string ;
      schema:rangeIncludes xsd:string ;
      sw:term_status    "stable" .

rdf:type epcis:jsonldLabel "type".

epcis:jsonldUriLabel a owl:DatatypeProperty , rdf:Property ;
      rdfs:comment      """JSONLD term (alias) used for the URI of nodes of this class.
There is no default: many EPCIS classes use blank nodes instead of the standard @id JSONLD term."""@en ;
      rdfs:domain       rdfs:Class;
      schema:domainIncludes rdfs:Class ;
      rdfs:isDefinedBy  epcis: ;
      rdfs:label        "jsonldUriLabel" ;
      rdfs:range        xsd:string ;
      schema:rangeIncludes xsd:string ;
      sw:term_status    "stable" .

#################### Event classes

epcis:EPCISEvent  a       owl:Class , rdfs:Class ;
        rdfs:comment      "A logistics event. This is a common superclass (base type) for all EPCIS events. All of the more specific event types are subclasses of EPCISEvent."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISEvent" ;
        sw:term_status    "stable" .

epcis:AggregationEvent   a owl:Class , rdfs:Class ;
        rdfs:comment      "The event type AggregationEvent describes events that apply to objects that have been aggregated to one another. In such an event, there is a set of 'contained' objects that have been aggregated within a 'containing' entity that's meant to identify the aggregation itself.  This event type is intended to be used for 'aggregations', meaning an association where there is a strong physical relationship between the containing and the contained objects such that they will all occupy the same location at the same time, until such time as they are disaggregated."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "AggregationEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:AssociationEvent   a owl:Class , rdfs:Class ;
        rdfs:comment      "The event type AssociationEvent describes the association or disassociation of one or several physical objects with a parent object or a specific physical location.  Like the AggregationEvent, the AssociationEvent is also used to capture associations where there is a strong physical relationship between the containing and the contained objects such that they will all occupy the same location at the same time, until such time as they are disaggregated. However, the AggregationEvent does not allow for associations of objects with physical locations;  if action is DELETE while omitting the childEPC and childQuantityList field, all contained children are disaggregated from the containing parent. Because there are situations in which associations are more permanent, i.e. beyond the physical flow of goods (e.g. packing/unpacking and loading/unloading), an AssociationEvent SHOULD be used: (a) when objects need to be associated with a physical location or (b) when the parent object could also be subject to other, more temporary associations (i.e. captured using AggregationEvent)."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "AssociationEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:ObjectEvent  a      owl:Class , rdfs:Class ;
        rdfs:comment      "An ObjectEvent captures information about an event pertaining to one or more physical or digital objects identified by instance-level (EPC) or class-level (EPC Class) identifiers. In most situations, an ObjectEvent is envisioned to represent an actual observations of objects, but strictly speaking it can be used for any event a Capturing Application wants to assert about objects, including for example capturing the fact that an expected observation failed to occur."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "ObjectEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:TransactionEvent   a owl:Class , rdfs:Class ;
        rdfs:comment      "The event type TransactionEvent describes the association or disassociation of physical or digital objects to one or more business transactions. While other event types have an optional bizTransactionList field that may be used to provide context for an event, the TransactionEvent is used to declare in an unequivocal way that certain objects have been associated or disassociated with one or more business transactions as part of the event."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "TransactionEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:Transformation a owl:Class , rdfs:Class ;
        rdfs:comment      """A transformation business processes that takes a longer period of time than a single TransformationEvent, so is associated with a series of such events.
When events share the same Transformation, the meaning is that the inputs to any of those events may have contributed in some way to each of the outputs in any of those same events."""@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "Transformation" ;
        sw:term_status    "stable" .

epcis:TransformationEvent        a owl:Class , rdfs:Class ;
        rdfs:comment      "A TransformationEvent captures information about an event in which one or more physical or digital objects identified by instance-level (EPC) or class-level (EPC Class) identifiers are fully or partially consumed as inputs and one or more objects identified by instance-level (EPC) or class-level (EPC Class) identifiers are produced as outputs. The TransformationEvent captures the relationship between the inputs and the outputs, such that any of the inputs may have contributed in some way to each of the outputs."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "TransformationEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

#################### Other classes

epcis:BizTransaction  a   owl:Class , rdfs:Class ;
        rdfs:comment      "Document that describes a particular business transaction. An example is a specific Purchase Order or Despatch Advice. Business Transaction information may be included in EPCIS events to record an event's participation in particular business transactions."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "BizTransaction" ;
        epcis:jsonldUriLabel "bizTransaction";
        sw:term_status    "stable" .

epcis:EPCISDocument a      owl:Class , rdfs:Class ;
        rdfs:comment      "An EPCISDocument is a means to transport a collection of EPCIS events, optionally accompanied by relevant master data, as a single electronic document.  It is used by the concrete bindings of the EPCIS Capture Interface.  In addition, trading partners may by mutual agreement use it as a single electronic document."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISDocument" ;
        epcis:jsonldUriLabel "id";
        sw:term_status    "stable" .

epcis:EPCISDocumentBody a      owl:Class , rdfs:Class ;
        rdfs:comment      "Intermediate node that is connected to EPCISDocument using epcisBody, and includes a list of events using eventList"@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISDocumentBody" ;
        sw:term_status    "stable" .

epcis:EPCISDocumentHeader a      owl:Class , rdfs:Class ;
        rdfs:comment      "Intermediate node that is connected to EPCISDocument using epcisHeader, and may include master data using masterData"@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISDocumentHeader" ;
        sw:term_status    "stable" .
…(발췌: 전체 60,475자 중 앞 9,823자)
```

### data/source_texts/ref-051.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "state",
    "description": "State of the mobile robot.",
    "subtopic": "/state",
    "type": "object",
    "required": [
        "headerId",
        "timestamp",
        "version",
        "manufacturer",
        "serialNumber",
        "orderId",
        "orderUpdateId",
        "lastNodeId",
        "lastNodeSequenceId",
        "nodeStates",
        "edgeStates",
        "driving",
        "actionStates",
        "instantActionStates",
        "powerSupply",
        "operatingMode",
        "errors",
        "safetyState"
    ],
    "properties": {
        "headerId": {
            "type": "integer",
            "description": "headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message."
        },
        "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ).",
            "examples": [
                "1991-03-11T11:40:03.123Z"
            ]
        },
        "version": {
            "type": "string",
            "description": "Version of the protocol [Major].[Minor].[Patch]",
            "examples": [
                "1.3.2"
            ]
        },
        "manufacturer": {
            "type": "string",
            "description": "Manufacturer of the mobile robot"
        },
        "serialNumber": {
            "type": "string",
            "description": "Serial number of the mobile robot."
        },
        "maps":{
            "type": "array",
            "description": "Array of map-objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/map"
			}
        },
        "zoneSets":{
            "type": "array",
            "description": "Array of zoneSet objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/zoneSet"
			}
        },
        "orderId": {
            "type": "string",
            "description": "Unique order identification of the current order or the previous finished order. The orderId is kept until a new order is received. Empty string (\"\") if no previous orderId is available."
        },
        "orderUpdateId": {
            "type": "integer",
            "description": "Order Update Identification to identify that an order update has been accepted by the mobile robot. 0 if no previous orderUpdateId is available."
        },
        "lastNodeId": {
            "type": "string",
            "description": "Node ID of last reached node or, if mobile robot is currently on a node, current node (e.g., \"node7\"). Empty string (\"\") if no lastNodeId is available."
        },
        "lastNodeSequenceId": {
            "type": "integer",
            "description": "sequenceId of the last reached node or, if the mobile robot is currently on a node, sequenceId of current node. 0 if no lastNodeSequenceId is available."
        },
		"nodeStates": {
            "type": "array",
            "description": "Array of nodeState-Objects, that need to be traversed for fulfilling the order. Empty list if idle.",
            "items": {
                "$ref": "#/definitions/nodeState"
            }
        },
        "edgeStates": {
            "type": "array",
            "description": "Array of edgeState-Objects, that need to be traversed for fulfilling the order, empty list if idle.",
            "items": {
				"$ref": "#/definitions/edgeState"
			}
        },
        "plannedPath": {
            "$ref": "#/definitions/plannedPath"
        },
        "intermediatePath": {
            "$ref": "#/definitions/intermediatePath"
        },
        "mobileRobotPosition": {
            "$ref": "#/definitions/mobileRobotPosition"
        },
        "velocity": {
            "type": "object",
            "description": "The mobile robot's velocity in mobile robot coordinates",
            "properties": {
                "vx": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its x direction",
                    "unit": "m/s"
                },
                "vy": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its y direction",
                    "unit": "m/s"
                },
                "omega": {
                    "type": "number",
                    "description":"The mobile robot's turning speed around its z axis.",
                    "unit": "rad/s"
                }
            }
        },
        "loads": {
            "type": "array",
            "description": "Loads, that are currently handled by the mobile robot. Optional: If mobile robot cannot determine load state, leave the array out of the state. If the mobile robot can determine the load state, but the array is empty, the mobile robot is considered unloaded.",
            "items": {
                "$ref": "#/definitions/load"
            }
        },
        "driving": {
            "type": "boolean",
            "description": "True: indicates that the mobile robot is driving and/or rotating. Other movements of the mobile robot (e.g., lift movements) are not included here.\nFalse: indicates that the mobile robot is neither driving nor rotating."
        },
        "paused": {
            "type": "boolean",
            "description": "True: mobile robot is currently in a paused state, either because of the push of a physical button on the mobile robot or because of an instantAction. The mobile robot can resume the order.\nFalse: The mobile robot is currently not in a paused state."
        },
        "newBaseRequest": {
            "type": "boolean",
            "description": "True: mobile robot is almost at the end of the base and will reduce speed if no new base is transmitted. Trigger for fleet control to send new base\nFalse: no base update required."
        },
		"zoneRequests": {
            "description": "Array of zoneRequest objects that are currently active on the mobile robot. Empty array if no zone requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/zoneRequest"
            }
        },
        "edgeRequests": {
            "description": "Array of edgeRequest objects that are currently active on the mobile robot. Empty array if no edge requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/edgeRequest"
            }
        },
        "distanceSinceLastNode": {
            "type": "number",
            "description": "Used by line guided vehicles to indicate the distance it has been driving past the lastNodeId. Distance is in meters."
        },
        "actionStates": {
            "type": "array",
            "description": "Array of the current actions and the actions which are yet to be finished. This may include actions from previous nodes that are still in progress\nWhen an action is completed, an updated state message is published with actionStatus set to finished and if applicable with the corresponding resultDescriptor. The actionStates are kept until a new order is received.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "instantActionStates": {
            "type": "array",
            "description": "Array of all instant action states that the mobile robot received. Empty array if the mobile robot has not received any instant actions. Instant actions are kept in the state until restart or action clearInstantActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "zoneActionStates": {
            "type": "array",
            "description": "Array of all zone actions that are in an end state or are currently running; sharing upcoming actions is optional. Zone action states are kept in the state message until restart or action clearZoneActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "powerSupply": {
            "$ref": "#/definitions/powerSupply"
        },
        "operatingMode": {
            "type": "string",
            "description": "Current operating mode of the mobile robot.",
            "enum": [
                "STARTUP",
                "AUTOMATIC",
                "SEMIAUTOMATIC",
                "INTERVENED",
                "MANUAL",
                "SERVICE",
                "TEACH_IN"
            ]
        },
        "errors": {
            "type": "array",
            "description": "Array of error-objects. All active errors of the mobile robot should be in the list. An empty array indicates that the mobile robot has no active errors.",
            "items": {
				"$ref": "#/definitions/error"
            }
        },
        "information": {
            "type": "array",
            "description": "Array of info-objects. An empty array indicates, that the mobile robot has no information. This should only be used for visualization or debugging – it must not be used for logic in fleet control.",
            "items": {
				"$ref": "#/definitions/info"
            }
        },
        "safetyState": {
            "$ref": "#/definitions/safetyState"
        }
    },
    "definitions": {
		"map": {
			"type": "object",
			"title": "map",
			"required": [
				"mapId",
				"mapVersion",
				"mapStatus"
			],
			"properties": {
				"mapId": {
					"type": "string",
					"description": "ID of the map describing a defined area of the mobile robot's workspace."
				},
				"mapVersion": {
					"type": "string",
					"description": "Version of the map."
				},
				"mapDescriptor": {
					"type": "string",
					"description": "A user-defined, human-readable name or descriptor"
				},
				"mapStatus": {
					"type": "string",
					"description": "Information on the status of the map indicating, if a map version is currently used on the mobile robot. ENABLED: Indicates this map is currently active / used on the mobile robot. At most one map with the same mapId can have its status set to ENABLED.<br>DISABLED: Indicates this map version is currently not enabled on the mobile robot and thus could be enabled or deleted by request.",
					"enum": [
						"ENABLED",
						"DISABLED"
					]
				}
			}
		},
		"zoneSet": {
			"type": "object",
			"title": "zoneSet",
			"required": [
				"zoneSetId",
				"mapId",
				"zoneSetStatus"
			],
			"properties": {
				"zoneSetId": {
					"type": "string",
					"description": "Unique identifier of the zone set that is currently enabled for the map.<br> This field shall be left empty only if the mobile robot has no zones defined for the corresponding map."
				},
				"mapId": {
					"type": "string",
					"description": "Identifier of the corresponding map."
				},
				"zoneSetStatus": {
					"type": "string",
…(발췌: 전체 34,440자 중 앞 11,051자)
```

### data/source_texts/ref-148.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_state.json",
  "title": "Robot State",
  "description": "The state of a robot",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "status": {
      "description": "A simple token representing the status of the robot",
      "type": "string",
      "enum": ["uninitialized", "offline", "shutdown", "idle", "charging", "working", "error"]
    },
    "task_id": {
      "description": "The ID of the task this robot is currently working on. Empty string if the robot is not working on a task.",
      "type": "string"
    },
    "unix_millis_time": { "type": "integer" },
    "location": { "$ref": "location_2D.json" },
    "battery": {
      "description": "State of charge of the battery. Values range from 0.0 (depleted) to 1.0 (fully charged)",
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "issues": {
      "description": "A list of issues with the robot that operators need to address",
      "type": "array",
      "items": { "$ref": "#/$defs/issue" }
    },
    "commission": { "$ref": "commission.json" },
    "mutex_groups": {
      "description": "Information about the mutex groups that this robot is interacting with",
      "type": "object",
      "properties": {
        "locked": {
          "description": "A list of mutex groups that this robot has currently locked",
          "type": "array",
          "items": { "type": "string" }
        },
        "requesting": {
          "description": "A list of the mutex groups that this robot is currently requesting but has not lockd yet",
          "type": "array",
          "items": { "type": "string" }
        }
      }
    }
  },
  "$defs": {
    "issue": {
      "description": "An issue that an operator needs to respond to (e.g. stuck, lost)",
      "type": "object",
      "properties": {
        "category": {
          "description": "Category of the robot's issue",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the issue",
          "anyOf": [
            { "type": "object" },
            { "type": "array" },
            { "type": "string" }
          ]
        }
      }
    }
  }
}
```

### data/source_texts/ref-283.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
## Doors

### Map Requirements

Before a door can be properly integrated, be sure to draw up the door locations with the correct door names on the navigation graph using `traffic_editor`. The instructions to do so can be found in the [Traffic Editor](./traffic-editor.md) chapter.

### Integration

Door integration is required when integrating RMF into a new environment. For hopefully obvious reasons, only automated doors can be integrated with RMF though it may be possible to trigger an alert to a designated human to open a manual door but this is not recommended. An automated door can be defined as an electronically powered door that is remotely controllable, either using a remote trigger or has been outfitted with a computing unit capable of commanding the door to open and close when needed, using certain interfaces.

Doors can be integrated with RMF using a ROS 2 door node and a door adapter, which we sometimes refer to as a door supervisor. The block diagram below displays the relationship and communication modes between each component:

<img src="images/doors_block_diagram.png">

The door node will have to be implemented based on the make and model of the door that is being integrated in order to address the specific API of the door controller module. The communication protocol will also be dependent on the door and controller model, which might be some form of `REST`, `RPCXML`, etc. The door node is in charge of publishing its state and receiving commands over ROS 2, using the messages and topics listed below:

| Message Types | ROS2 Topic | Description |
|---------------|------------|-------------|
| `rmf_door_msgs/DoorState` | `/door_states` | State of the door published by the door node
| `rmf_door_msgs/DoorRequest` | `/door_requests` | Direct requests subscribed by the door node and published by the door adapter
| `rmf_door_msgs/DoorRequest` | `/adapter_door_requests` | Requests to be sent to the door adapter/supervisor to request safe operation of doors |

The door adapter stands in between the rest of the RMF core systems, fleet adapters, and the door node, and acts like a state supervisor ensuring that the doors are not acting on requests that might obstruct an ongoing mobile robot task or accidentally closing on it. It keeps track of the door state from the door node, and receives requests from the `adapter_door_requests` topic which are published by either fleet adapters or other parts of the RMF core system. Only when the door adapter deems that a request is safe enough to be performed, it will instruct the door node using a request. It should also be noted that direct requests sent to the door node, without going through the door adapter will be negated by the door adapter, to return it to its prior state in order to prevent disruptions during operations with mobile robots.

## Door Adapter Template
To make the process of integrating doors with RMF even simpler, we have open-sourced a [template package](https://github.com/open-rmf/door_adapter_template) where users only need to update certain blocks of code with the API calls to their specific door controller.
```

### data/source_texts/ref-284.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# Lifts (i.e. Elevators)

## Map requirements

Before a lift can be properly integrated, be sure to draw up the lift locations with the correct lift names and levels on the navigation graph using `traffic_editor`. The instructions to do so can be found in [Traffic Editor](./traffic-editor.md) chapter.

## Integration

Elevator integration will allow RMF to work over multiple levels, resolving conflicts and managing shared resources on a larger scale. Similar to door integration, the basic requirement is that the lift controller accepts commands using a prescribed protocol, `OPC` is one such example.

The elevators will be integrated in a similar fashion as doors as well, relying on a lift node and a lift adapter. The following block diagram shows how each component works with each other:

<img src="images/lifts_block_diagram.png">

The lift node will act as a driver to work with the lift controller. An example of a lift node can be found in this [repository](https://github.com/sharp-rmf/kone_lift_controller). The node will publish its state and receive lift requests over ROS 2, using the messages and topics listed below.

| Message Types | ROS2 Topic | Description |
|---------------|------------|-------------|
| `rmf_lift_msgs/LiftState` | `/lift_states` | State of the lift published by the lift node
| `rmf_lift_msgs/LiftRequest` | `/lift_requests` | Direct requests subscribed by the lift node and published by the lift adapter
| `rmf_lift_msgs/LiftRequest` | `/adapter_lift_requests` | Requests to be sent to the lift adapter/supervisor to request safe operation of lifts |

A lift adapter subscribes to `lift_states` while keeping track of the internal and desired state of the lift in order to prevent it from performing any actions that might interrupt mobile robot or normal operations. The lift adapter performs this task by receiving lift requests from the fleet adapters and the RMF core systems and only relaying the instructions to the lift node if it is deemed appropriate. Any requests sent directly to the lift node, without going through the lift adapter, will also be negated by the lift adapter, to prevent unwanted disruption to mobile robot fleet operations.
```

### data/source_texts/ref-285.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
builtin_interfaces/Time door_time
string door_name
DoorMode current_mode
```

### data/source_texts/ref-286.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# lift_time records when the information in this message was generated
builtin_interfaces/Time lift_time

string lift_name

string[] available_floors
string current_floor
string destination_floor

uint8 door_state
uint8 DOOR_CLOSED=0
uint8 DOOR_MOVING=1
uint8 DOOR_OPEN=2

uint8 motion_state
uint8 MOTION_STOPPED=0
uint8 MOTION_UP=1
uint8 MOTION_DOWN=2
uint8 MOTION_UNKNOWN=3

# We can only set human or agv mode, but we can read other modes: fire, etc.
uint8[] available_modes
uint8 current_mode
uint8 MODE_UNKNOWN=0
uint8 MODE_HUMAN=1
uint8 MODE_AGV=2
uint8 MODE_FIRE=3
uint8 MODE_OFFLINE=4
uint8 MODE_EMERGENCY=5
# we can add more "read-only" modes as we come across more of them.

# this field records the session_id that has been granted control of the lift
# until it sends a request with a request_type of REQUEST_END_SESSION
string session_id
```

### data/source_texts/ref-287.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
////
Copyright © 2016-2021 The Eclipse Foundation, Cirrus Link Solutions, and others

This program and the accompanying materials are made available under the
terms of the Eclipse Public License v. 2.0 which is available at
https://www.eclipse.org/legal/epl-2.0.

SPDX-License-Identifier: EPL-2.0

Sparkplug®, Sparkplug Compatible, and the Sparkplug Logo are trademarks of the Eclipse Foundation.
////

// set default value if assetsdir hasn't been defined
ifndef::assetsdir[:assetsdir:]

[[operational_behavior]]
== Operational Behavior

An MQTT based SCADA system is unique in that the Primary Host Application is not responsible for
establishing and maintaining connections to the Edge Nodes as is the case in most existing legacy
poll/response device protocols. With an MQTT based architecture, both the Host Applications as well
as the Edge Nodes establish MQTT Sessions with one or more central MQTT Servers. This is the desired
functionality as it provides the necessary decoupling from any one application and any given
Edge Node/Device. Additional Sparkplug Host Application MQTT clients can connect and subscribe to
any of the real time data without impacting the Primary Host Application.

Due to the nature of real time SCADA solutions, it is very important for the Primary Host
Application and all connected Edge Nodes to have the MQTT Session state
information for each other. In order to accomplish this the Sparkplug Topic Namespace definitions
for Birth/Death Certificates along with the defined payloads provide both state and context between
the Primary Host Application and the associated Edge Nodes. In most use cases and solution scenarios
there are two main reasons for this "designation" of a Primary Host Application:

[arabic]
. Only the Primary Host Application should have the permission to issue commands to Edge Nodes.
. In high availability and redundancy use cases where multiple MQTT Servers are used, Sparkplug Edge
Nodes need to be aware of whether the Primary Host Application is connected to each MQTT Server in
the infrastructure. If the Primary Host Application STATE shows that an Edge Node is connected to an
MQTT Server that the Primary Host Application is *NOT* connected to, then the Edge Node should
connect to the next available MQTT Server where STATE for the Primary Host Application shows
'online=true'.

[[operational_behavior_timestamps]]
=== Timestamps in Sparkplug

An important aspect of Sparkplug is its use of time. All timestamps must be in Coordinated
Universal Time (UTC). In order to ensure this is the case, all Sparkplug Edge Nodes and Sparkplug
Host Applications must have an accurate mechanism for ensuring their clocks remain accurate. This is
typically left to the system operating system using technologies such as Network Time Protocol
(NTP). Regardless of the mechanism used, ensuring all timestamps are accurate and in UTC is
critical to all timestamps in Sparkplug.

[[operational_behavior_case_sensitivity]]
=== Case Sensitivity in Sparkplug

The MQTT specification states that MQTT topics are case sensitive [MQTTV5-4.7.3]. For example, the
topic a/b is different than A/b. Sparkplug in turn is also case sensitive with regard to both topics
as well as metric names. So, a metric 'temperature' is not the same as the metric 'Temperature'.
However, this generally should be avoided. Many Host Applications may not be able to differentiate
the two metric names as unique. Many databases are case-insensitive and would not be able to handle
this situation well.

* [tck-testable tck-id-case-sensitivity-sparkplug-ids]#[yellow-background]*[tck-id-case-sensitivity-sparkplug-ids] Edge
Nodes in a Sparkplug environment SHOULD NOT have Sparkplug IDs (Group, Edge Node, or Device IDs)
that when converted to lower case match*#
** For example there should not be two different Edge Nodes publishing NBIRTH messages on these two
topics spBv1.0/Group1/NBIRTH/EdgeNode1 and spBv1.0/group1/NBIRTH/edgenode1
* [tck-testable tck-id-case-sensitivity-metric-names]#[yellow-background]*[tck-id-case-sensitivity-metric-names] An
Edge Node SHOULD NOT publish metric names that when converted to all lower case match.*#
** For example a DBIRTH should not contain a metric 'a' and another metric 'A'.

[[operational_behavior_primary_host_application_session_establishment]]
=== Host Application Session Establishment

The Sparkplug Host Application upon startup or reconnect will immediately try to create a Host MQTT
Session with the configured MQTT Server infrastructure. Note that the establishment of an Host
Application MQTT session is asynchronous of any other MQTT Client session. If Edge Nodes are already
connected to the MQTT Server infrastructure, the Sparkplug Host Application will synchronize using
the STATE MQTT topic. If associated Edge Nodes are not connected, the Sparkplug Host Application
will synchronize with the Edge Nodes and their data streams when the Edge Nodes publish their Birth
Certificates. Any Edge Node that has specified this Sparkplug Host Application as its Primary Host
Application will will wait to publish their Birth Certificates until after they receive the STATE
message denoting that the Primary Host application is online.

.Figure 4 - Host Session Establishment
plantuml::{assetsdir}assets/plantuml/host-session-establishment.puml[format=svg, alt="Host Session Establishment"]

The session diagram in Figure 3 - Host Session Establishment shows a very simple topology with a
single MQTT Server. The steps outlined in the session diagram are defined as follows:

[arabic]
. Sparkplug Host Applications will try to create an MQTT Session using the MQTT CONNECT Control
Packet. A Death Certificate is constructed into the MQTT Will Topic and Will Payload of the
CONNECT Control Packet with a Will QoS set to 1 and Will Retain flag set to true.
+
[tck-testable tck-id-message-flow-phid-sparkplug-clean-session-311]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-clean-session-311] The
CONNECT Control Packet for all Sparkplug Host Applications when using MQTT 3.1.1 MUST set the MQTT
'Clean Session' flag to true.*#
+
[tck-testable tck-id-message-flow-phid-sparkplug-clean-session-50]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-clean-session-50] The
CONNECT Control Packet for all Sparkplug Host Applications when using MQTT 5.0 MUST set the the MQTT
'Clean Start' flag to true and the 'Session Expiry Interval' to 0.*#
+
The MQTT CONNECT Control Packet is acknowledged as successful with a valid MQTT CONNACK Control
Packet from the MQTT Server. From this point forward in time, the MQTT Server is ready to deliver a
Host Death Certificate any time the Sparkplug Host Application MQTT Client loses connectivity to the
MQTT Server.

. With the MQTT Session established, Sparkplug Host Application MUST issue an MQTT subscription for
the defined Sparkplug Topic Namespace.
+
[tck-testable tck-id-message-flow-phid-sparkplug-subscription]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-subscription] The
subscription on the Sparkplug Topic Namespace and the STATE topic MUST be done immediately after
successfully establishing the MQTT session and before publishing its own STATE message.*#

. [tck-testable tck-id-message-flow-phid-sparkplug-state-publish]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-state-publish] Once
an MQTT Session has been established, the Sparkplug Host Application subscriptions on the Sparkplug
Topic Namespace have been established and the STATE topic subscription has been established, the
Sparkplug Host Application MUST publish a new STATE message.*#
+
[tck-testable tck-id-message-flow-phid-sparkplug-state-publish-payload]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-state-publish-payload] The
Host Application Birth Certificate Payload MUST be JSON UTF-8 data. It MUST include two key/value
pairs where one key MUST be 'online' and its value is a boolean 'true'. The other key MUST be
'timestamp' and the value MUST be the same value set in the immediately prior MQTT CONNECT packet's
Will Message payload.*#
+
[tck-testable tck-id-message-flow-phid-sparkplug-state-publish-payload-timestamp]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-state-publish-payload-timestamp] The
timestamp value in the Host Application Birth Certificate payload MUST be the same value set in the
immediately prior MQTT CONNECT packet's Will Message payload.*#
+
The Host Application is now ready to start receiving MQTT messages from any connected Edge Node
within the infrastructure. At this point, the Host Application can update the MQTT Client metrics in
the Host Application with a current state of 'online' once each Edge Node publishes its Sparkplug
NBIRTH and DBIRTH messages. Since the Sparkplug Host Application is also relying on the MQTT Session
to the MQTT Server(s), the availability of MQTT Servers to the Host Application is also being
monitored and reflected in the MQTT Client metrics in the Host Application.
. If at any point in time Host Application loses connectivity with the defined MQTT Server(s), the
online=true state of the Server is immediately reflected in the MQTT Client metrics in the Host
Application.
+
[tck-not-testable]#[yellow-background]*All metric data associated with any Sparkplug Edge Node that
was connected to that MQTT Server and known by the Host Application MUST be updated to a STALE data
quality if the Host Application loses connection to the MQTT Server.*#

[tck-testable tck-id-message-flow-hid-sparkplug-state-message-delivered]#[yellow-background]*[tck-id-message-flow-hid-sparkplug-state-message-delivered] After
publishing its own Host Application STATE message, if at any point the Host Application is delivered
a STATE message on its own Host Application ID with a 'online' value of false, it MUST immediately
republish its STATE message to the same MQTT Server with a 'online' value of true and the
'timestamp' set to the same value that was used for the timestamp in its own prior MQTT CONNECT
packet Will Message payload.*#

[[operational_behavior_edge_node_session_establishment]]
=== Edge Node Session Establishment

Prior to sending an NBIRTH message, the MQTT client associated with the Edge Node must subscribe to
receive NCMD messages with the following rules.

* [tck-testable tck-id-message-flow-edge-node-ncmd-subscribe]#[yellow-background]*[tck-id-message-flow-edge-node-ncmd-subscribe] The
MQTT client associated with the Edge Node MUST subscribe to a topic of the form
'spBv1.0/group_id/NCMD/edge_node_id' where group_id is the Sparkplug Group ID and the edge_node_id
is the Sparkplug Edge Node ID for this Edge Node. It MUST subscribe on this topic with a QoS of
1.*#
** This subscription is mandatory as Edge Nodes MUST be able to respond to 'rebirth requests'.

After subscribing, the Edge Node must follow these additional rules.

* [tck-testable tck-id-message-flow-edge-node-birth-publish-connect]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-connect] Any
Edge Node in the MQTT infrastructure MUST establish an MQTT Session prior to publishing NBIRTH and
DBIRTH messages.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message] When
a Sparkplug Edge Node sends its MQTT CONNECT packet, it MUST include a Will Message.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-topic]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-topic] The
Edge Node's MQTT Will Message's topic MUST be of the form 'spBv1.0/group_id/NDEATH/edge_node_id'
where group_id is the Sparkplug Group ID and the edge_node_id is the Sparkplug Edge Node ID for this
Edge Node*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-payload]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-payload] The
Edge Node's MQTT Will Message's payload MUST be a Sparkplug Google Protobuf encoded payload.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-payload-bdSeq]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-payload-bdSeq] The
Edge Node's MQTT Will Message's payload MUST include a metric with the name of 'bdSeq', the datatype
of INT64, and the value MUST be incremented by one from the value in the previous MQTT CONNECT
packet unless the value would be greater than 255. If in the previous NBIRTH a value of 255 was
sent, the next MQTT Connect packet Will Message payload bdSeq number value MUST have a value of 0.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-qos]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-qos] The
Edge Node's MQTT Will Message's MQTT QoS MUST be 1.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-will-retained]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-will-retained] The
Edge Node's MQTT Will Message's retained flag MUST be set to false.*#

Edge Nodes can be configured to support the concept of a 'Primary Host Application'. In this case,
the Edge Node must wait until the Primary Host Application is online and subscribed to Sparkplug
messages before the Edge Node publishes its NBIRTH and DBIRTH messages. Specifying a Primary Host is
not required for an Edge Node. But it is often desired. For example say an Edge Node is in a
Sparkplug environment and there is a single consuming Host Application that historizes the data. It
would not be beneficial for the Sparkplug Edge Node to publish data if the Host Application is not
connected and subscribed to messages. Instead, it would be better for the Edge Node to store data
while the Host Application is offline. Once the Host Application is properly connected, it could
then send all of its stored data and continue publishing normally. Once the Sparkplug Edge Node has
successfully connected to the MQTT Server, it must publish a NBIRTH message. The NBIRTH message must
follow the following rules. Note if Primary Host is configured for the Edge Node, it must also wait
until the Primary Host denotes it is online before the Edge Node publishes its NBIRTH message.

* [tck-testable tck-id-message-flow-edge-node-birth-publish-phid-wait]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-phid-wait] If
the Edge Node is configured to wait for a Primary Host Application it MUST verify the Primary Host
Application is online via the STATE topic before publishing NBIRTH and DBIRTH messages.*#
** [tck-testable tck-id-message-flow-edge-node-birth-publish-phid-wait-id]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-phid-wait-id] If
the Edge Node is configured to wait for a Primary Host Application it MUST validate the Host
Application ID as the last token in the STATE message topic string matches the configured Primary
Host Application ID for this Edge Node.*#
** [tck-testable tck-id-message-flow-edge-node-birth-publish-phid-wait-online]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-phid-wait-online] If
the Edge Node is configured to wait for a Primary Host Application it MUST validate the 'online'
boolean flag is true in the STATE message payload before considering the Primary Host Application to
be online and active.*#
** [tck-testable tck-id-message-flow-edge-node-birth-publish-phid-wait-timestamp]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-phid-wait-timestamp] If
the Edge Node is configured to wait for a Primary Host Application it MUST validate the timestamp
value is greater than or equal to the previous STATE message timestamp value in the STATE message
payload before considering the Primary Host Application to be online and active. If no previous
STATE message timestamp value has been received by this Edge Node it MUST consider the incoming
STATE message to be the latest/valid.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-nbirth-topic]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-nbirth-topic] The
Edge Node's NBIRTH MQTT topic MUST be of the form 'spBv1.0/group_id/NBIRTH/edge_node_id' where
group_id is the Sparkplug Group ID and the edge_node_id is the Sparkplug Edge Node ID for this Edge
Node*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-nbirth-payload]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-nbirth-payload] The
Edge Node's NBIRTH payload MUST be a Sparkplug Google Protobuf encoded payload.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-nbirth-payload-bdSeq]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-nbirth-payload-bdSeq] The
Edge Node's NBIRTH payload MUST include a metric with the name of 'bdSeq' the datatype of INT64 and
the value MUST be the same as the previous MQTT CONNECT packet.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-nbirth-qos]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-nbirth-qos] The
Edge Node's NBIRTH MQTT QoS MUST be 0.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-nbirth-retained]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-nbirth-retained] The
Edge Node's NBIRTH retained flag MUST be set to false.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-nbirth-payload-seq]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-nbirth-payload-seq] The
Edge Node's NBIRTH payload MUST include a 'seq' number that is between 0 and 255 (inclusive).*#
** This will become the starting sequence number which all following messages will include a
sequence number that is one more than the previous up to 255 where it wraps back to zero.
* [tck-testable tck-id-message-flow-edge-node-birth-publish-phid-offline]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-phid-offline] If
the Edge Node is configured to wait for a Primary Host Application, it is connected to the MQTT
Server, and receives a STATE message on its configured Primary Host, the timestamp value in the
payload is greater than or equal to the timestamp value included in the prior 'online' STATE
message, and the 'online' value is false, it MUST immediately publish an NDEATH message and
disconnect from the MQTT Server and start the connection establishment process over.*#
** If the Edge Node did not previously receive a STATE message from this Primary Host Application,
it can not check the timestamp value against the previous value. In this case it MUST honor the
'online' boolean status flag as denoted in the payload.

Most implementations of a Sparkplug Edge Node for real time SCADA systems will try to maintain a
persistent MQTT Session with the MQTT Server Infrastructure. But there are use cases where the
MQTT Session does not need to be persistent. In either case, an Edge Node can try to establish an
MQTT Session at any time and is completely asynchronous from any other MQTT Client in the
infrastructure. The only exception to this rule is the use case where there are multiple MQTT
Servers and a Primary Host Application. Note this does not refer to the use of the MQTT 'Clean
Session' flag in MQTT 3.1.1 or the 'Clean Start' flag in MQTT 5.0. All types of MQTT clients (both
Host and Edge Nodes) in a Sparkplug system MUST always set the 'Clean Session' flag in the MQTT
3.1.1 CONNECT packet to true. When using MQTT 5.0 the 'Clean Start' flag must be set to true and the
MQTT 'Session Expiry Interval' to zero.

.Figure 5 - Edge Node MQTT Session Establishment
plantuml::{assetsdir}assets/plantuml/edge-node-mqtt-session-establishment.puml[format=svg, alt="Edge Node MQTT Session Establishment"]

The session diagram in Figure 4 - Edge Node MQTT Session Establishment shows a very simple topology
with a single MQTT Server. The steps outlined in the session diagram are defined as follows:

[arabic]
. The Edge Node MQTT Client will attempt to create an MQTT connection to the available MQTT
Server(s) using the MQTT CONNECT Control Packet.
The Death Certificate constructed into the Will Topic and Will Payload follows the format defined
in section on link:#payloads_ndeath[NDEATH messages].

. The subscription to NCMD level topics ensures that Edge Node targeted messages from the Primary
Host Application are delivered. The subscription to DCMD ensures that device targeted messages from
the Primary Host Application are delivered. In infrastructures with multiple MQTT Servers and a
designated Primary Host Application, the subscription to STATE informs the Edge Node the current
state of the Primary Host Application. At this point the Edge Node has fully completed the steps
required for establishing a valid MQTT Session with the Primary Host Application.

. Once an MQTT Session has been established, the Edge Node MQTT client MUST publish an application
level NBIRTH as defined link:#topics_birth_message_nbirth[here]. At this point, the Primary Host
Application will have all the information required to build out the Edge Node metric structure and
show the Edge Node in an 'online' state once it publishes its NBIRTH and DBIRTH messages.

. If at any point in time the Edge Node MQTT Client loses connectivity to the defined MQTT
Server(s), a Death Certificate (NDEATH) is issued by the MQTT Server on behalf of the Edge Node.
Upon receipt of the Death Certificate with a bdSeq number metric that matches the preceding bdSeq
number in the NBIRTH messages, the Primary Host Application should set the state of the Edge Node
to ‘online=false’ and update all metric timestamps related to this Edge Node. Any defined metrics
will be set to a STALE data quality.

.. The bdSeq number is used to correlate an NBIRTH with a NDEATH. Because the NDEATH is included in
the MQTT CONNECT packet, its timestamp (if included) is not useful to Sparkplug Host Applications.
Instead, a bdSeq number must be included as a metric in the payload of the NDEATH. The same bdSeq
number metric value must also be included in the NBIRTH message published immediately after the MQTT
CONNECT. This allows Host Applications to know that a NDEATH matches a specific NBIRTH message. This
is required because timing with Will Messages may result in NDEATH messages arriving after a
new/next NBIRTH message. The bdSeq number allows Host Applications to know when it must consider the
Edge Node offline.

[[operational_behavior_edge_node_session_termination]]
=== Edge Node Session Termination

[tck-testable tck-id-operational-behavior-edge-node-intentional-disconnect-ndeath]#[yellow-background]*[tck-id-operational-behavior-edge-node-intentional-disconnect-ndeath] When
an Edge Node disconnects intentionally, it MUST publish an NDEATH before terminating the connection.*#

[tck-testable tck-id-operational-behavior-edge-node-intentional-disconnect-packet]#[yellow-background]*[tck-id-operational-behavior-edge-node-intentional-disconnect-packet] Immediately
following the NDEATH publish, a DISCONNECT packet MAY be sent to the MQTT Server.*#

* If an MQTT DISCONNECT packet is sent by the Edge Node, this signals to the MQTT Server that the
Will Message MUST not be delivered by the MQTT Server to subscribers of that message. These
subscribers are typically Sparkplug Host Applications. This is why a Death message MUST be published
before disconnecting from the MQTT Server. It ensures Edge Nodes are notified the Edge Node is now
offline.
* If an MQTT DISCONNECT packet is not sent by the Sparkplug Edge Node, the MQTT Server will
eventually deliver the Will Message (Death Certificate) to the subscribers. However, this can take
some time to occur based on when the MQTT Server detects that the Edge Node is no longer connected.
By sending the Death Certificate before disconnecting without sending an MQTT DISCONNECT packet, we
are ensuring that a Death message will be delivered to subscribing clients promptly. The fact that a
second Death message will arrive when the Will Message is delivered is not significant. This is
because the Will Message Death message will contain a bdSeq number that matches the bdSeq number
that is published by the Edge Node immediately before the disconnect. Because it has a duplicate
bdSeq, the Will Message Death message MUST be ignored by the subscribing Sparkplug Host Application
clients.

This allows the MQTT Server to be notified that the Edge Node is offline and as a result the MQTT
Will Message of the Edge Node will not be delivered by the MQTT Server to subscribed MQTT clients.

When an Edge Node goes offline by sending its NDEATH or if an MQTT Server delivers an NDEATH on
behalf of an Edge Node, it is implied that all of the Edge Node's associated Devices are also
offline. In addition, it is also implied that all metrics in the previous associated NBIRTH and all
DBIRTHs in this Sparkplug session under that Edge Node are now STALE.

For the following normative statements it is up to the designers of the Sparkplug Host Application
with regard to how they 'mark' the Sparkplug Edge Node or Sparkplug Device as 'offline'. It is also
up to the designers of the Sparkplug Host Application on how they 'mark' a metric as STALE. This is
an important aspect of Sparkplug in that an NDEATH means the data was accurate at a time, but now
that the MQTT session has been lost can no longer be considered current or up to date.

Because an NDEATH may be sent on behalf of an Edge Node by an MQTT Server in the MQTT Will Message,
the Sparkplug payload timestamp does not represent the time that the Edge Node actually went
offline. As a result, the timestamp associated with NDEATH events must use the timestamp of receipt
on the Sparkplug Host Application. This is in part why Sparkplug Edge Nodes and Host Applications
must have synced system clocks and all Sparkplug timestamps must be in UTC time.

* [tck-testable tck-id-operational-behavior-edge-node-termination-host-action-ndeath-node-offline]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-action-ndeath-node-offline] Immediately
after receiving an NDEATH from an Edge Node, Host Applications MUST mark the Edge Node as offline
using the current Host Application's system UTC time*#
* [tck-testable tck-id-operational-behavior-edge-node-termination-host-action-ndeath-node-tags-stale]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-action-ndeath-node-tags-stale] Immediately
after receiving an NDEATH from an Edge Node, Host Applications MUST mark all metrics that were
included in the previous NBIRTH as STALE using the current Host Application's system UTC time*#
* [tck-testable tck-id-operational-behavior-edge-node-termination-host-action-ndeath-devices-offline]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-action-ndeath-devices-offline] Immediately
after receiving an NDEATH from an Edge Node, Host Applications MUST mark all Sparkplug Devices
associated with the Edge Node as offline using the current Host Application's system UTC time*#
* [tck-testable tck-id-operational-behavior-edge-node-termination-host-action-ndeath-devices-tags-stale]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-action-ndeath-devices-tags-stale] Immediately
after receiving an NDEATH from an Edge Node, Host Applications MUST mark all of the metrics that
were included with associated Sparkplug Device DBIRTH messages as STALEusing the current Host
Application's system UTC time*#

For the following assertions an 'online STATE message' is one where a Host Application's JSON
payload has the 'online' key's value set to true. An 'offline STATE message' is one where the Host
Application's JSON payload has the 'online' key's value set to false.

If the Edge Node is configured to use a Primary Host Application, it must also watch for 'STATE'
messages from the Primary Host Application via an MQTT subscription. If the Primary Host Application
denotes it is offline, the Edge Node must disconnect from the current MQTT server following these
rules:

* [tck-testable tck-id-operational-behavior-edge-node-termination-host-offline]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-offline] If
the Edge Node is configured to use a Primary Host Application, it MUST disconnect from the current
MQTT Server if the online JSON value is false and the timestamp value is greater than or equal to
the previous online STATE message timestamp value.*#
** [tck-testable tck-id-operational-behavior-edge-node-termination-host-offline-reconnect]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-offline-reconnect] If the Edge
Node disconnects after being in a Sparkplug session due to a valid 'offline STATE message', it MUST
attempt to connect to the next MQTT Server in its connection list to start the session establishment
procedure over again.*#
* [tck-testable tck-id-operational-behavior-edge-node-termination-host-offline-timestamp]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-offline-timestamp] Consider
an Edge Node that is configured to use a Primary Host Application and the Edge Node is connected and
publishing. Then it receives an offline STATE message. It MUST NOT disconnect if the timestamp
value is less than the value from the previous online STATE message.*#
** It must not disconnect because the older timestamp value indicates the Host Application MQTT
session that is being denoted as lost is not the one the current session the Host Application has
established with the MQTT Server. Due to how an MQTT connection can be lost it is possible and
likely that an old Host Application death message could be delivered after a new Host Application
MQTT session is established. In this case, the timestamp value on the incoming death message will
be older than the current timestamp value. For this reason, it must be ignored.

[[operational_behavior_device_session_establishment]]
=== Device Session Establishment

The aim of the Sparkplug Specification is to enable the transport of real time process variable
information from existing and new end devices measuring, monitoring, and controlling a physical
process into an MQTT infrastructure subsequently a Sparkplug Host Application. In the context of
this document an MQTT Device can represent anything from existing legacy poll/response driven PLCs,
RTUs, HART Smart Transmitters, etc., to new generation automation and instrumentation devices that
can implement a conformant MQTT client natively.

The preceding sections in this document detail how the Sparkplug Host Application interacts with the
MQTT Server infrastructure and how that infrastructure interacts with the notion of a Sparkplug
Edge Node. But to a large extent the technical requirements of those pieces of the infrastructure
have already been provided. For most use cases in this market sector the primary focus will be on
the implementation of the Sparkplug Specification between the native device and the Edge Node API’s.

Prior to sending a DBIRTH message, if the Device supports 'writing to outputs' the MQTT client
associated with the Sparkplug Device must subscribe to receive DCMD messages with the following
rules.

* [tck-testable tck-id-message-flow-device-dcmd-subscribe]#[yellow-background]*[tck-id-message-flow-device-dcmd-subscribe] If
the Device supports writing to outputs, the MQTT client associated with the Device MUST subscribe to
a topic of the form 'spBv1.0/group_id/DCMD/edge_node_id/device_id' where group_id is the Sparkplug
Group ID the edge_node_id is the Sparkplug Edge Node ID and the device_id is the Sparkplug Device ID
for this Device. It MUST subscribe on this topic with a QoS of 1.*#

A Device can publish a DBIRTH as long as an NBIRTH has been sent previously and the MQTT session is
active. The DBIRTH message must follow the following rules.

* [tck-testable tck-id-message-flow-device-birth-publish-nbirth-wait]#[yellow-background]*[tck-id-message-flow-device-birth-publish-nbirth-wait] The
NBIRTH message MUST have been sent within the current MQTT session prior to a DBIRTH being
published.*#
* [tck-testable tck-id-message-flow-device-birth-publish-dbirth-topic]#[yellow-background]*[tck-id-message-flow-device-birth-publish-dbirth-topic] The
Device's DBIRTH MQTT topic MUST be of the form 'spBv1.0/group_id/DBIRTH/edge_node_id/device_id'
where group_id is the Sparkplug Group ID the edge_node_id is the Sparkplug Edge Node ID and the
device_id is the Sparkplug Device ID for this Device.*#
* [tck-testable tck-id-message-flow-device-birth-publish-dbirth-match-edge-node-topic]#[yellow-background]*[tck-id-message-flow-device-birth-publish-dbirth-match-edge-node-topic] The
Device's DBIRTH MQTT topic group_id and edge_node_id MUST match the group_id and edge_node_id that
were sent in the prior NBIRTH message for the Edge Node this Device is associated with.*#
* [tck-testable tck-id-message-flow-device-birth-publish-dbirth-payload]#[yellow-background]*[tck-id-message-flow-device-birth-publish-dbirth-payload] The
Device's DBIRTH payload MUST be a Sparkplug Google Protobuf encoded payload.*#
* [tck-testable tck-id-message-flow-device-birth-publish-dbirth-qos]#[yellow-background]*[tck-id-message-flow-device-birth-publish-dbirth-qos] The
Device's DBIRTH MQTT QoS MUST be 0.*#
* [tck-testable tck-id-message-flow-device-birth-publish-dbirth-retained]#[yellow-background]*[tck-id-message-flow-device-birth-publish-dbirth-retained] The
Device's DBIRTH retained flag MUST be set to false.*#
* [tck-testable tck-id-message-flow-device-birth-publish-dbirth-payload-seq]#[yellow-background]*[tck-id-message-flow-device-birth-publish-dbirth-payload-seq] The
Device's DBIRTH payload MUST include a 'seq' number that is between 0 and 255 (inclusive) and be one
more than was included in the prior Sparkplug message sent from the Edge Node associated with this
Device.*#

In order to expose and populate the metrics from any device, the following simple
session diagram outlines the requirements:

.Figure 6 - MQTT Device Session Establishment
plantuml::{assetsdir}assets/plantuml/mqtt-device-session-establishment.puml[format=svg, alt="MQTT Device Session Establishment"]

The session diagram in Figure 5 - MQTT Device Session Establishment shows a simple topology with
all the Sparkplug elements in place i.e. Host Application, MQTT Server(s), Sparkplug Edge Node and
this element, the device element. The steps outlined in the session diagram are defined as follows:

This flow diagram assumes that at least one MQTT Server is available and operational within the
infrastructure. Without at least a single MQTT Server the remainder of the infrastructure is
unavailable.

[arabic]
. Assuming MQTT Server is available.

. Assuming the Primary Host Application established MQTT Session with the MQTT Server(s).

. The Session Establishment of the associated Sparkplug Edge Node is described in
link:#operational_behavior_edge_node_session_establishment[Edge Node Session Establishment]. This
flow diagram assumes that the Edge Node session has already been established with the Primary Host
Application. Depending on the target platform, the Edge Node may be a physical "Edge of Network"
gateway device polling physical legacy devices via Modbus, AB, DNP3.0, HART, etc, an MQTT enabled
sensor or device, or it might be a logical implementation of one of the Eclipse Tahu compatible
implementations for prototype Edge Nodes running on a Raspberry Pi. Regardless of the
implementation, at some point the device interface will need to provide a state and associated
metrics to publish to the MQTT infrastructure.

. State #4 in the session diagram represents the state at which the Edge Node is ready to report all
of its metric data to the MQTT Server(s) as defined in Sparkplug. It is the responsibility of the
Edge Node (logical or physical) to put this information in the form defined in
link:#payloads_dbirth[DBIRTH messages]. Upon receiving the DBIRTH message, the Primary Host
Application can build out the proper metric structure and set the Sparkplug Device to 'online'.

. Following the Sparkplug Specification in link:#payloads_ddata[Device Data Messages] (DDATA), all
subsequent metrics are published to the Primary Host Application on a Report by Exception (RBE)
basis using the DDATA message format. Time based reporting is not explicitly disallowed by the
Sparkplug Specification but it is discouraged and often unnecessary.

. If at any time the Sparkplug Device cannot provide real time information, the Sparkplug
Specification requires that an DDEATH be published. This will inform the Primary Host Application
that all metric information associated with that Sparkplug Device be set to a STALE data quality.

[[operational_behavior_device_session_termination]]
=== Device Session Termination

[tck-testable tck-id-operational-behavior-device-ddeath]#[yellow-background]*[tck-id-operational-behavior-device-ddeath] If
a Sparkplug Edge Node loses connection with an attached Sparkplug Device, it MUST publish a DDEATH
message on behalf of the device.*#

When a Sparkplug Device goes offline by having its DDEATH published by an Edge Node, it allows
Sparkplug Host Applications to know that the Sparkplug Device is no longer reporting current and
accurate values to the Edge Node. Therefore the Edge Node is not able to report live/accurate data
values on behalf of the Sparkplug Device to the MQTT Server or in turn to Sparkplug Host
Applications. As a result the Sparkplug Host Applications must mark the Device as offline and denote
the Sparkplug Device's tags as stale.

For the following normative statements it is up to the designers of the Sparkplug Host Application
with regard to how they 'mark' the Sparkplug Device as 'offline'. It is also up to the designers of
the Sparkplug Host Application on how they 'mark' a metric as STALE. This is an important aspect of
Sparkplug in that an DDEATH means the data was accurate at a time, but now that the connection
between the Sparkplug Edge Node and the Sparkplug Device has been lost can no longer be considered
current or up to date.

The DDEATH is sent on behalf of a Sparkplug Device by a Sparkplug Edge Node. Because of this, the
Sparkplug payload timestamp associated with a DDEATH is considered accurate and must be used as the
timestamp for a Sparkplug Device being marked as offline and for its associated metrics being set to
STALE.

[tck-testable tck-id-operational-behavior-edge-node-termination-host-action-ddeath-devices-offline]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-action-ddeath-devices-offline] Immediately
after receiving an DDEATH from an Edge Node, Host Applications MUST mark the Sparkplug Device
associated with the Edge Node as offline using the timestamp in the DDEATH payload*#

[tck-testable tck-id-operational-behavior-edge-node-termination-host-action-ddeath-devices-tags-stale]#[yellow-background]*[tck-id-operational-behavior-edge-node-termination-host-action-ddeath-devices-tags-stale] Immediately
after receiving an DDEATH from an Edge Node, Host Applications MUST mark all of the metrics that
were included with the associated Sparkplug Device DBIRTH messages as STALE using the timestamp in
the DDEATH payload*#

[[operational_behavior_sparkplug_host_applications]]
=== Sparkplug Host Applications

As noted above, the Sparkplug Host Application has the required permissions to send commands to Edge
Nodes and Sparkplug Devices because Edge Nodes need to know that the Primary Host Application is
connected to the same MQTT Server that it is connected to or to walk to another server in the
infrastructure. Both are common requirements of a mission critical SCADA system.

But unlike legacy SCADA system implementations, all real time process variable information being
published through the MQTT infrastructure is available to any number of additional MQTT Clients in
the business that might be interested in subsets if not all of the real time data.

The only fundamental difference between a Primary Host Application MQTT Client and other Sparkplug
Host Application MQTT Clients is that the Edge Nodes in the infrastructure know to make sure the
Primary Host Application is online before publishing data.

[[operational_behavior_host_application_message_ordering]]
=== Sparkplug Host Application Message Ordering

Sparkplug Host Applications are required to validate the order of messages arriving from Edge Nodes.
This is done using the sequence number which is sent in every NBIRTH, DBIRTH, NDATA, and DDATA
message that comes from an Edge Node. Because these MQTT messages are sent on different topics, it
is possible based on MQTT Server implementations that these messages may arrive at the Sparkplug
Host Application in a different order than they were sent from the Edge Node. This can be especially
common when using clustered MQTT Servers. It is the responsibility of the Sparkplug Host Application
to ensure that all messages arrive within a 'Reorder Timeout'. In typical environments this timeout
can be as little as a couple of seconds. In deployments with very slow networks or clustered MQTT
servers it may need to be longer. In some environments, the MQTT Server may ensure in-order delivery
of QoS0 MQTT messages even across topics. In these cases this timeout could be zero.

For example, if a Sparkplug Host Application receives messages from an Edge Node with sequence
numbers 1, 2, and 4 then at the time the message with a sequence number 4 arrives, a timer SHOULD be
started within the Host Application. This is the start of the Reordering Timeout timer. A message
with sequence number 3 MUST arrive before the Reordering Timeout elapses. If a message with sequence
number 3 does not arrive before the timeout, a Rebirth Request should be sent to the Edge Node. This
ensures that the session state is properly reestablished. If a message with a sequence number of 3
arrives before the Reorder Timeout occurs then the timer can be shutdown and normal operation of the
Host Application can continue.

It is also important to note that depending on the Sparkplug Host Application's purpose it may make
sense to never process messages out of order. It also may make sense to not process a message that
arrived out of sequence if its preceding messages didn't arrive before the Reorder Timeout. These
choices are left to the Sparkplug Host Application developer. For example, a Host Application that
is a time series database may want to insert all data that arrives regardless of the message order.
However, a rules engine Host Application may require that messages are processed in order of their
sequence numbers to preserve the order of events as they occurred at the Edge Node.

* [tck-testable tck-id-operational-behavior-host-reordering-param]#[yellow-background]*[tck-id-operational-behavior-host-reordering-param] Sparkplug
Host Applications SHOULD provide a configurable 'Reorder Timeout' parameter*#
* [tck-testable tck-id-operational-behavior-host-reordering-start]#[yellow-background]*[tck-id-operational-behavior-host-reordering-start] If
a Sparkplug Host Application is configured with a 'reordering timeout' parameter and a message
arrives with an out of order sequence number, the Host Application MUST start a timer denoting the
start of the Reorder Timeout window*#
* [tck-testable tck-id-operational-behavior-host-reordering-rebirth]#[yellow-background]*[tck-id-operational-behavior-host-reordering-rebirth] If
a Sparkplug Host Application is configured with a 'reordering timeout' parameter and the Reorder
Timeout elapses and the missing message(s) have not been received, the Sparkplug Host Application
MUST send an NCMD to the Edge Node with a 'Node Control/Rebirth' request*#
** Non-normative comment: In most cases a 'Primary Host Application' would send a Rebirth Request
but a Non-Primary Host may not
* [tck-testable tck-id-operational-behavior-host-reordering-success]#[yellow-background]*[tck-id-operational-behavior-host-reordering-success] If
the missing message(s) that triggered the start of the Reorder Timeout timer arrive before the
reordering timer elapses, the timer MUST be terminated and normal operation in the Host Application
MUST continue until another out of order message arrives.*#

[[operational_behavior_primary_application_state_in_multiple_mqtt_server_topologies]]
=== Primary Host Application STATE in Multiple MQTT Server Topologies

For implementations with multiple MQTT Servers, there is one additional aspect that needs to be
understood and managed properly. When multiple MQTT Servers are available there is the possibility
of "stranding" an Edge Node if the Primary command/control of the Primary Host Application loses
network connectivity to one of the MQTT Servers. In this instance the Edge Node would stay properly
connected to the MQTT Server publishing information not knowing that Primary Host Application was
not able to receive the messages.

[tck-testable tck-id-operational-behavior-primary-application-state-with-multiple-servers-state-subs]#[yellow-background]*[tck-id-operational-behavior-primary-application-state-with-multiple-servers-state-subs] When
using multiple MQTT Servers and Edge Nodes are configured with a Primary Host Application, the
Primary Host Application instance MUST be configured to publish a STATE Birth Certificate and all
Edge Nodes configured with a Primary Host Application MUST subscribe to this STATE message.*#

[tck-testable tck-id-operational-behavior-primary-application-state-with-multiple-servers-state]#[yellow-background]*[tck-id-operational-behavior-primary-application-state-with-multiple-servers-state] Regardless
of the number of MQTT Servers in a Sparkplug Infrastructure, every time a Primary Host Application
establishes a new MQTT Session with an MQTT Server, the STATE Birth Certificate defined in the
link:#payloads_desc_state[STATE description section] MUST be the first message that is published
after a successful MQTT Session is established with each MQTT Server.*#

Sparkplug Edge Nodes in an infrastructure that provides multiple MQTT Servers can establish a
session to any one of the MQTT Servers.

[tck-testable tck-id-operational-behavior-primary-application-state-with-multiple-servers-single-server]#[yellow-background]*[tck-id-operational-behavior-primary-application-state-with-multiple-servers-single-server] The
Edge Nodes MUST not connected to more than one server at any point in time.*#

Upon establishing a session, the Edge Node should issue a subscription to the STATE message
published by the Primary Host Application. Since the STATE message is published with the MQTT RETAIN
flag set, MQTT will guarantee that the last STATE message is always available. The Edge Node should
examine the JSON payload of this message to ensure that the value of the 'online' key is true. If
the value is false, this indicates the Primary Application has lost its MQTT Session to this
particular MQTT Server.

[tck-testable tck-id-operational-behavior-primary-application-state-with-multiple-servers-walk]#[yellow-background]*[tck-id-operational-behavior-primary-application-state-with-multiple-servers-walk] If
the Primary Host Application is offline as denoted via the STATE MQTT Message, the Edge Node MUST
terminate its session with this MQTT Server and move to the next available MQTT Server that is
available.*#

[tck-testable tck-id-operational-behavior-edge-node-birth-sequence-wait]#[yellow-background]*[tck-id-operational-behavior-edge-node-birth-sequence-wait] The
Edge Node MUST also wait to publish its BIRTH sequence until an online=true STATE message is
received by the Edge Node.*#
This use of the STATE message in this manner ensures that any loss of connectivity between an MQTT Server
and the Primary Host Application does not result in Edge Nodes being "stranded" on an MQTT server
because of network issues. The following message flow diagram outlines how the STATE message is
used when three (3) MQTT Servers are available in the infrastructure:

// suppress inspection "AsciiDocLinkResolve"
.Figure 7 – Primary Host Application STATE flow diagram
plantuml::{assetsdir}assets/plantuml/primary-host-application-state-flow-diagram.puml[format=svg, alt="Primary Host Application STATE flow diagram"]

[arabic]
. When an Edge Node is configured with multiple available MQTT Servers in the infrastructure it
should issue a subscription to the Primary Host Application STATE message. The Edge Nodes are free
to establish an MQTT Session to any of the available servers over any available network at any time
and examine the current STATE value. If the STATE message payload is online=false then the Edge Node
should disconnect and walk to the next available server.

. Upon startup, the configured Primary Host Application's MQTT Client MUST include the Primary Host
Application DEATH Certificate that indicates STATE is online=false with the message RETAIN flag set
to true in the MQTT Will Message. Then the Primary Host Application BIRTH Certificate must be
published with a STATE payload of online=true. In both of these messages the timestamp value must
match each other and represent the current connection time. The timestamp value must be a JSON
number and represent the number of UTC milliseconds since Epoch.

. As the Edge Node walks its available MQTT Server list, it will establish an MQTT Session with a
server that has a STATE message with a JSON payload that has online=true. The Edge Node can stay
connected to this server if its MQTT Session stays intact and it does not receive the Primary Host
Application DEATH Certificate.

. Having a subscription registered to the MQTT Server on the STATE topic will result in any change
to the current Primary Host Application STATE being received immediately. In this case, a
network disruption causes the Primary Host Application MQTT Session to server #2 to be terminated.
This will cause the MQTT Server, on behalf of the now terminated the Primary Host Application MQTT
Client, to deliver the Death Certificate to clients that are currently subscribed to it. Upon
receipt of the Primary Host Application Death Certificate each Edge Node will disconnect from the
current MQTT Server and connect to the next MQTT Server in its list. Before the Edge Node
disconnects and connects to the next MQTT Server it must validate that the JSON payload denotes
online=false and the timestamp value is greater than or equal to the prior STATE message timestamp
value from that Host Application's BIRTH message.

. The Edge Node connects to the next available MQTT Server and since the current STATE on this
server is online=true, it can stay connected. In the meantime, the network disruption between the
Primary Host Application and MQTT Server #2 has been corrected. The Primary Host Application has a
new MQTT Session established to server #2 with an updated Birth Certificate of online=true. Now MQTT
Server #2 is ready to accept new Edge Node session requests.

[[operational_behavior_edge_node_ndata_and_ncmd_messages]]
=== Edge Node NDATA and NCMD Messages

We’ll start this section with a description of how metric information is published to the Primary
Host Application from an Edge Node in the MQTT infrastructure. The definition of an Edge Node is
generic in that it can represent both physical "Edge of Network Gateway" devices that are
interfacing with existing legacy equipment and a logical MQTT endpoint for devices that natively
implement the Sparkplug Specification. The link:#payloads_nbirth[NBIRTH Section] defines the Edge
Node Birth Certificate MQTT Payload and the fact that it can provide any number of metrics that will
be exposed in the Primary Host Application. Some examples of these will be "read only" such as:

* Edge Node Manufacture ID
* Edge Node Device Type
* Edge Node Serial Number
* Edge Node Software Version Number
* Edge Node Configuration Change Count
* Edge Node Position (if GPS device is available)
* Edge Node Cellular RSSI value (if cellular is being used)
* Edge Node Power Supply voltage level
* Edge Node Temperature

Other metrics may be dynamic and "read/write" such as:

* Edge Node Rebirth command to republish all Edge Node and Device Birth Certificates
* Edge Node Next server command to move to next available MQTT Server
* Edge Node Reboot command to reboot the Edge Node
* Edge Node Primary Network (PRI_NETWORK) where 1 = Cellular, 2 = Ethernet

The important point to realize is that the metrics exposed in the Primary Host Application for use
in the design of applications are completely determined by what metric information is published in
the NBIRTH. This is entirely dependent on the application and use-case. Each specific Edge Node can
best determine what data to expose, and how to expose it, and it will automatically appear in the
Primary Host Application metric structure. Metrics can even be added dynamically at runtime and with
a new NBIRTH and DBIRTH sequence of messages. These metrics will automatically be added to the
Primary Host Application metric structure.

The other very important distinction to make here is that Edge Node NDATA and NCMD messages are
decoupled from the Sparkplug Device level data and command messages of DDATA and DCMD. This
decoupling in the Topic Namespace is important because it allows interaction from all MQTT Clients
in the system (to the level of permission and application) with the Edge Nodes, but NOT to the level
of sending device commands. The Primary Host Application could provide a configuration parameter
that would BLOCK output DDATA and DCMD messages but still allow NDATA and NCMD messages to flow. In
this manner, multiple application systems can be connected to the same MQTT infrastructure, but only
the ones with DCMD enabled can publish Device commands.

It is also important to note that an Access Control List (ACL) can be used to allow one or more
Sparkplug Host Applications to publish NCMD and DCMD messages to one or more Edge Nodes. Furthermore
the ability to publish NCMD or DCMD messages by other Sparkplug Host Applications could be blocked.
The decoupled nature of the commands and data messages allows for this type of granular access and
control.

The following simple message flow diagram demonstrates the messages used to update a changing
cellular RSSI value in the Primary Host Application and sending a command from the Primary Host
Application to the Edge Node to use a different primary network path.

.Figure 8 - Edge Node NDATA and NCMD Message Flow
plantuml::{assetsdir}assets/plantuml/edge-node-ndata-and-ncmd-message-flow.puml[format=svg, alt="Edge Node NDATA and NCMD Message Flow"]

[arabic]
. Assuming MQTT Server is available.
. Assuming the Primary Host Application established MQTT Session with the MQTT Server(s).
. The Edge Node has an established MQTT Session and the NBIRTH has been published. Primary Host
Application now has all defined metrics and their current value.
. The Edge Node is monitoring its local cellular RSSI level. The level has changed and now the Edge
Node wants to publish the new value to the associated metric in Primary Host Application.
. From an operational requirement, the Edge Node needs to be told to switch its primary network
interface from cellular to Ethernet. From the Primary Host Application, the new metric value is
published to the Edge Node using a NCMD Sparkplug message.

[[operational_behavior_mqtt_enabled_device_session_establishment]]
=== MQTT Enabled Device Session Establishment

When implementing Sparkplug directly on an I/O enabled Device, there are two options. The notion of
a 'Sparkplug Device' can be removed entirely. In this scenario the MQTT Client can publish 'Edge
Node level' messages (e.g. NBIRTH, NDEATH, NCMD, and NDATA) and never use the concept of 'Device
level' messages (e.g. DBIRTH, DDEATH, DCMD, and DDATA messages. All of the metrics can be published
on the Edge Node level Sparkplug verbs and simply omit use of the Device level Sparkplug verbs.
Because the Edge Node level verbs encapsulate the MQTT/Sparkplug Session, this is all that is
required.

Alternatively, the implementation can use the concept of both Edge Node and Device Sparkplug verbs
(NBIRTH, NDEATH, NDATA, NCMD, DBIRTH, DDEATH, DDATA, and DCMD) as any other Gateway based Edge Node
would. From any consuming application this would look like any other Edge Node Gateway that may be
managing one or more attached devices.

[[operational_behavior_sparkplug_host_application_session_establishment]]
=== Sparkplug Host Application Session Establishment

Sparkplug Host Applications must follow the following rules when connecting to the MQTT Server.

* [tck-testable tck-id-operational-behavior-host-application-host-id]#[yellow-background]*[tck-id-operational-behavior-host-application-host-id] The
sparkplug_host_id MUST be unique to all other Sparkplug Host IDs in the infrastructure.*#
* [tck-testable tck-id-operational-behavior-host-application-connect-will]#[yellow-background]*[tck-id-operational-behavior-host-application-connect-will] When
a Sparkplug Host Application sends its MQTT CONNECT packet, it MUST include a Will Message.*#
* [tck-testable tck-id-operational-behavior-host-application-connect-will-topic]#[yellow-background]*[tck-id-operational-behavior-host-application-connect-will-topic] The
MQTT Will Message's topic MUST be of the form 'spBv1.0/STATE/sparkplug_host_id' where host_id is the
unique identifier of the Sparkplug Host Application*#
* [tck-testable tck-id-operational-behavior-host-application-connect-will-payload]#[yellow-background]*[tck-id-operational-behavior-host-application-connect-will-payload] The
Death Certificate Payload MUST be JSON UTF-8 data. It MUST include two key/value pairs where one key
MUST be 'online' and it's value is a boolean 'false'. The other key MUST be 'timestamp' and the
value MUST be the same value that was used for the timestamp in its own prior MQTT CONNECT packet
Will Message payload.*#
* [tck-testable tck-id-operational-behavior-host-application-connect-will-qos]#[yellow-background]*[tck-id-operational-behavior-host-application-connect-will-qos] The
MQTT Will Message's MQTT QoS MUST be 1 (at least once).*#
* [tck-testable tck-id-operational-behavior-host-application-connect-will-retained]#[yellow-background]*[tck-id-operational-behavior-host-application-connect-will-retained] The
MQTT Will Message's retained flag MUST be set to true.*#

Once the Sparkplug Host Application has successfully connected to the MQTT Server, it must publish a
birth with the following rules.
…(발췌: 전체 78,622자 중 앞 58,712자)
```
