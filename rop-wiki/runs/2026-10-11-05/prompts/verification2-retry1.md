(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-05
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 49. 사람 근접 안전 (M. 안전)
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

### runs/2026-10-11-05/target.json

```json
{
  "run_id": "2026-10-11-05",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 171,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 49,
    "area_name": "49. 사람 근접 안전",
    "category": "M. 안전",
    "category_letter": "M"
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
  "selection_rationale": "CLI 지정 run_type=update, area=49"
}
```

### runs/2026-10-11-05/research.json

```json
{
  "run_id": "2026-10-11-05",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 49,
    "area_name": "49. 사람 근접 안전",
    "category": "M. 안전"
  },
  "gaps": [
    "섹션 4. 핵심 개념과 용어(분리 2026-09-30-area49-s4) — NIST SSM 논문 연도를 '2016' 으로 적어 학술지 게재 연도(2017)와 다름",
    "섹션 5. 적용 사례 — 병원 사례를 '시뮬레이션 평가' 로 잘못 분류(89행), 창고 연구(74행)는 '정량 결과 미확인', 아마존 글 '발행일 미확인'(72행), 실외 사례 제약 칸(100행)이 2023 기사의 '당시 개정안' 수치에만 기대고 현행 고시 원문 근거가 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area49-s6) — 구역 지원 신고·적재 외곽 기준 진입, Nav2·RMF 의 0 값 의미 차이, 감지 응답시간 보정 요인이 없고, Farrell(55행)·Jafari(61행) 문장이 실험 조건을 '미확인' 으로 둠",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area49-s7) — 실외 인증 행이 인증기관 페이지·기사 근거뿐이고 시행규칙·고시 원조문이 없음. ISO 13482:2014·ISO 10218-1:2025 범위·국내 실내 KS(KS B 8252) 행 없음",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area49-s8) — Farrell·HATA·Jafari 서지가 프리프린트 기준이고 Rondoni 제목·환경 표현 부정확, HATA 평가가 시뮬레이션이라는 점과 실패율 정의 없음",
    "섹션 9. 책임 경계 — 사람 위치를 플릿에 전달하는 공개 구현과 그 한계(좌표계·변환 실패), 실외 인증의 운행계획서·보행자 밀집 알림 요구 미반영",
    "섹션 11. 열린 질문 — oq-229·oq-230·oq-231·oq-232 부분 근거 미반영",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정 5건(f1·f14·f20·f24·f49)"
  ],
  "research_questions": [
    "사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]",
    "oq-229 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? (섹션 6·9·11 겨냥)",
    "oq-230 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (섹션 5·7·11 겨냥)",
    "oq-231 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (섹션 7·11 겨냥)",
    "oq-232 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (섹션 9·11 겨냥)",
    "바뀐 출처: 병원·창고·편안함 연구의 실험 조건과 출판 서지, 현행 실외 인증 고시 별표의 실제 기준은 무엇인가? (섹션 5·8 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Marvel·Norcross(NIST)의 SSM 논문 학술지판은 Robotics and Computer-Integrated Manufacturing 44권(2017) 144–155쪽에 실렸고, 2015-03-04 접수·2016-08-01 승인됐다. 위키 4절·8절과 분리 페이지의 '2016년 논문' 표기는 승인 연도 기준이라 게재 연도(2017)와 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-1075"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NIST 공개 PDF 1쪽 머리글 \"Robotics and Computer-Integrated Manufacturing 44 (2017) 144–155\", Article history \"Received 4 March 2015 … Accepted 1 August 2016\". 기존 ref-1075 published '2016'. 반응시간 0.113 s(§5)·ZR·ZS 위치 불확실성(§6)은 기존 내용(2026-09-30-area49-s6.md 41행, 2026-09-30-area49-s4.md 38행)이라 새로 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "SICK 의 기술 블로그는 안전 레이저 스캐너에서 감시 케이스(보호 필드 집합) 사이를 전환하면 시스템 응답시간이 늘어나고, 다중 샘플링 값을 올리면 물체가 연속으로 더 여러 번 감지돼야 출력이 꺼지므로 응답시간 보정분이 더해진다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1466"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: SICK 블로그(Martin Kidman, 2021-02-09) \"switching between cases adds to the response time of a system\", Multiple sampling 절 \"must see an object twice in a row … multiple sampling of 3 … three times in succession before the OSSD's switch OFF\", \"additional response time supplements due to multiple sampling settings, transmission times and case switching\". 제조사 일반 설명이며 특정 센서·제어기·하중·바닥 조건의 시험값이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약",
      "vendor_claim": true
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 은 로봇마다 처리할 수 있는 구역 유형이 다르므로, 모든 이동 로봇이 이해할 수 있는 구역 이름을 factsheet 의 typeSpecifications.supportedZones 배열로 플릿 관제에 보고하도록 요구한다(shall).",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 태그 명세 §6.4 Zones: \"Some mobile robots cannot process zones at all, while other mobile robots might only be able to work with a certain subset of zone types … All mobile robots shall therefore report to fleet control which zones they are able to understand by adding the according zone names to the `supportedZones` array\". 모든 기종이 모든 구역 유형을 지원한다는 뜻이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "같은 명세의 외곽 기준 구역(contour-based zones)에서는 적재물을 포함한 로봇 외곽이 구역 진입·이탈을 정하며, 외곽의 어느 부분이라도 구역에 들어가면 진입이고 외곽이 모두 빠져나가야 이탈이다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.4.1.1 Contour-based zones: \"the contour of the mobile robot (including its load) determines zone entry and exit. Any part of the contour entering the zone is a zone entry.\" SPEED_LIMIT 의 maximumSpeed(m/s)와 '진입 시 이미 제한 속도 도달'(Table 6)은 기존 내용(docs/categories/safety/index.md 77행)이라 새로 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "ROP 가 구역 속도 제한을 등록할 때는 로봇별 supportedZones 신고를 먼저 확인하고, 적재물로 커진 외곽이 진입 경계에 닿기 전에 감속을 마치도록 감속 시작 지점을 경계 앞에 두며, 실제 감속을 통합 시험으로 확인하는 절차가 필요하다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f4 에서 도출한 ROP 운영 시사점. 감속 거리·시간 실측값은 로봇 제조사 자료로 확인해야 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "Nav2(Jazzy) Collision Monitor 문서는 source_timeout(기본 2.0초) 안에 새 센서 데이터가 오지 않으면 로봇을 정지시키며, source_timeout 을 0.0 으로 두면 이 차단 동작이 꺼진다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1467"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Collision Monitor Node 문서(Jazzy) source_timeout 항목: \"Type: double Default: 2.0 … If no new data is received within this interval, the robot will be stopped. Setting source_timeout: 0.0 disables this blocking mechanism.\" 하드 실시간 안전 인증 미제공 문장은 기존 내용(2026-09-30-area49-s6.md 47행, ref-1077)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Nav2(Jazzy) Speed Filter 에서 speed_limit 메시지 값 0 은 정지가 아니라 '속도 제한 없음'을 뜻하며, 이는 백분율·절댓값 설정과 관계없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1468"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Speed Filter Parameters 문서(Jazzy) speed_limit_topic 설명: \"speed_limit : non-zero values show maximum allowed speed … Zero value means no speed restriction (independently on percentage).\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Open-RMF rmf_fleet_adapter 2.14.0 의 차선 속도 제한(limit_lane_speeds) 처리는 요청 속도가 0 이하이거나 차선 번호가 그래프 범위를 벗어나면 경고만 남기고 그 요청을 무시하며, 경고문은 차선을 닫으려면 close_lanes API 를 쓰라고 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1464"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "FleetUpdateHandle.cpp(2.14.0 태그) limit_lane_speeds 람다: \"request.lane_index() >= new_graph.num_lanes() || request.speed_limit() <= 0.0\" → RCLCPP_WARN \"Ignoring speed limit request … not greater than zero. If you would like to close the lane, use the FleetUpdateHandle::close_lanes(~) API instead.\" → continue",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "같은 코드에서 유효한 속도 제한은 계획 그래프의 차선 속성(speed_limit)에 기록된 뒤 새 Planner 를 만들어 작업 파라미터에 넘기고 차선 상태를 발행하는 데서 끝나며, 차량이 실제로 감속을 마쳤는지 확인하는 경로는 이 함수에 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1464"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "같은 람다 이어지는 부분: \"properties.speed_limit(request.speed_limit());\" → \"std::make_shared<const rmf_traffic::agv::Planner>(new_config, …)\" → task_parameters->planner(…) → publish_lane_states(). 계획 계층의 코드 경로이며 물리적 감속 완료 확인(ACK)은 이 함수 범위 밖",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 모두 '정지'를 뜻하지 않으므로, 이종 플릿 어댑터가 '0' 을 정지 명령으로 그대로 옮기면 의도와 반대로 제한이 풀리거나 무시될 수 있는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1467",
        "ref-1468",
        "ref-1464"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6~f8 의 문서·코드 의미를 나란히 놓은 추론. 실제 어댑터에서 이 오류가 생긴 사례나 실행 시험 자료는 확인하지 못함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "ROP 어댑터 계약은 '제한 없음', '양수 속도 제한', '통로 폐쇄', '보호 정지'를 서로 다른 명령으로 표현하고, 구역 전송·활성화·계획 반영·차량 감속 관측을 별개 상태로 기록해 계획 상태 갱신만으로 감속 완료를 보고하지 않도록 해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1464",
        "ref-1468",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8~f10 에서 도출. VDA 5050 의 zoneSet 변경 시 새 zoneSetId·DISABLED 후 enableZoneSet 활성화 규칙은 기존 내용(2026-09-30-area16-s6.md 49행, 2026-09-30-area16-s4.md 40행)이라 새로 넣지 않고 이 의견의 배경으로만 씀",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "Farrell 외의 창고 연구는 Freight·Jackal·Megarover 실물 로봇으로 실험했고, 로봇과 보행자 위치는 OptiTrack 모션 캡처로 측정했다. 정적·동적 장애물 회피 단위 실험은 설정마다 10회 수행했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1082"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2503.21141v1 §VI \"we present real-world experiments carried out to evaluate the system\", Fig. 2(c) \"Real-world robots, from left to right: Freight, Jackal, and two Megarovers\", \"The project employs the Optitrack system for precise localization\", Table III(1~3대 설정·속도별). 출판판: 2025 IEEE CASE pp.548–555, UC eScholarship 2025-08-17",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "수행 자원"
    },
    {
      "id": "f13",
      "claim": "같은 연구의 Open-RMF 플릿 실험(Table IV)은 로봇 4대·최고 1.0 m/s 또는 2대·1.5 m/s 설정에서 보행자 0·1·2명 조건을 비교했고, 표의 값은 Open-RMF 상위 계획기가 로봇을 일부러 세워 둔 시간을 뺀 것이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1082"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Table IV 제목 \"OpenRMF Experiment Results Table. These values exclude periods when the robot is stationary.\" 본문 \"we exclude periods when the robots are deliberately held stationary by OpenRMF's high-level planner\". 전체 임무 처리량 지표로 옮겨 쓰지 않음. 단위 실험(f12)과 분모가 다름",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "정정 제안: 49영역 본문 74행('정량 결과는 미확인')·2026-09-30-area49-s6.md 55행('정량 결과 미확인')·2026-09-30-area49-s8.md 42행('2025-03, 프리프린트 … 정량 결과 미확인')은 실물 실험 조건(f12)과 Table IV 조건·분모(f13)를 적고, 서지를 2025 IEEE CASE(pp.548–555, 2025-08-17) 게재로 고치는 것이 맞아 보인다. 현장 배치 사례가 아니라 연구 평가라는 기존 구분은 유지한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1082"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f12·f13 에서 도출. CASE 게재 서지(DOI 10.1109/CASE58245.2025.11164151, pp.548–555, 2025-08-17)는 UC eScholarship 공식 저장소 기준(검증 결과). Table IV 의 개별 수치는 이번 변환에서 옮기지 않음",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "HATA(Kazemi Eskeri 외) 논문의 5·10·15대 플릿 평가는 실제 기록된 사람 궤적을 재생하는 시뮬레이션 환경에서 수행됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2508.19731v1 §IV-B \"we conducted experiments within a simulated environment using the multi-agent loosely-coupled coordination framework … we replayed human trajectories\", \"fleets of size 5, 10, and 15 robots\". 실측 궤적 재생이 현장 운용 시험을 뜻하지 않음. 출판판 IROS 2025(pp.12697–12703, 2025-10), Aalto 목록 게시 2025-11-27",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "같은 논문의 실패율은 교착 또는 10분 제한시간 초과로 완료하지 못한 과제의 비율로, 사고율이나 사람과의 충돌률이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§V \"Failure rate refers to the percentage of tasks that were not successfully completed due to deadlock or timeout … The 10-minute timeout exceeds the longest observed task time (under 4 minutes)\". 기존 위키의 '최대 26%·19% 단축'(2026-09-30-area49-s6.md 57행)은 유지하되 안전 지표로 읽지 않도록 구분 필요",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "Tartu 병원 현장 시험 논문은 TIAGo·Clearpath Jackal 이종 로봇을 RMF 로 관리하는 능력을 '시험 환경'에서 검증했고, 병원 안에서 여러 배송 로봇을 운용하는 것은 아직 하지 않은 향후 과제로 적었다.",
      "tag": "사실",
      "source_ids": [
        "ref-869"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Frontiers in Robotics and AI 9(2022) §4 'Increasing the number and diversity of robots': \"we have validated RMF's capability to manage multiple heterogeneous robots (TIAGo and Clearpath Jackal mobile platforms) in a testing environment, we are yet to apply multiple delivery robots inside the Hospital\". TIAGo 의 ICU→검사실 혈액 운반 시연은 기존 내용(ref-869, 다른 영역)이라 새로 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "Rondoni 외(Scientific Reports, 2024-08-07)의 병원 주행 벤치마크는 컴퓨터 시뮬레이션이 아니라, 병상·복도·대기 공간·가구 등 실제 병원의 물리적 배치를 재현한 모의 병원 공간에서 HOSBOT·TIAGo 실물 로봇으로 수행됐고 Vicon 카메라 8대로 위치를 측정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Experimental testing: \"The experimental testing has been performed in a simulated hospital environment … that replicates the physical layout and characteristics of a real hospital, including patient's beds, corridors, waiting areas, and furnishings.\" Vicon 8대(검증 결과). 실제 환자와 함께 운영한 결과가 아님",
      "as_of": "2026-10-11",
      "site_type": "병원",
      "flow_item": "작업 대상"
    },
    {
      "id": "f19",
      "claim": "같은 연구의 이동 장애물은 사람이 아니라 정해진 경로를 고정 선속도·각속도로 원격조종해 움직인 두 번째 시험용 이동 로봇 베이스였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Mobile Obstacle: \"a moving obstacle, that is represented by a (second) testing mobile base teleoperated along the set path at fixed linear and angular speeds\". 사람을 대상으로 안전거리를 검증한 시험과 구별",
      "as_of": "2026-10-11",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f20",
      "claim": "정정 제안: 49영역 본문 89행 '이 사례는 실제 병원이 아닌 모의 병원 환경에서 수행한 시뮬레이션 평가다' 는 '실제 병원 구조를 재현한 모의 병원 공간에서 실물 로봇으로 수행한 실험 평가(이동 장애물은 원격조종 로봇)' 로 고치는 것이 맞아 보인다. 2026-09-30-area49-s8.md 41행의 논문 제목도 원문대로 단수 'hospital environment' 로 맞춘다.",
      "tag": "추정",
      "source_ids": [
        "ref-1081"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f18·f19 에서 도출. 같은 '시뮬레이션 평가' 표현이 docs/categories/safety/index.md 125행·187행에도 있으나 이번 실행 범위 밖이라 후속 정리 대상. 시험 속도 0.2·0.6·1.0 m/s 는 법정 사람 근접 속도가 아님",
      "as_of": "2026-10-11",
      "site_type": "병원",
      "flow_item": "작업 대상"
    },
    {
      "id": "f21",
      "claim": "Jafari·Nguyen·Liu 의 보행자 편안함 실험 참가자는 23~41세 자원자 32명(남 22·여 10)이었고, 폭 3.2 m 복도에서 원격조종 로봇이 1.4·2.8 m/s 로 움직였으며, 160회 시행 중 데이터 수집이 완전히 실패한 2회를 뺐다(측면 거리 관련 분석은 13회를 더 뺐다).",
      "tag": "사실",
      "source_ids": [
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2604.13677v1 §IV \"Twenty-two males and ten females volunteered\", \"The robot speed is constant at 1.4 m/s and 2.8 m/s\", \"We discard 2 of 160 trials because of complete data collection failures.\" 연령·복도 폭·원격조종·추가 13회 제외는 같은 절(검증 결과). 국립성공대 IRB 승인. arXiv 표지 \"Accepted to IEEE ICRA 2026\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f22",
      "claim": "같은 연구의 복합 예측기는 분석에 쓴 데이터와 같은 데이터로 평가돼, 독립 시험 집합에서의 성능은 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§V-C \"the same dataset used in analysis evaluates the predictors\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "논문의 오즈비 3.67 은 복합 예측기가 '편안함'으로 예측했을 때 실제로 편안했을 오즈가 그렇지 않게 예측했을 때보다 3.67배라는 뜻으로, 사고 감소 확률이나 안전 거리 기준이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§V-B Table VI 설명 \"The odds ratios …\", 결론 \"The composite estimator achieves … an odds ratio of 3.67\". 인과 효과·안전 인증과 구분",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "정정 제안: 2026-09-30-area49-s6.md 61행의 '(실험 장소·참가자 수 미확인)' 은 참가자 32명·3.2 m 복도·원격조종 로봇·1.4/2.8 m/s 조건(f21)과 같은 데이터 평가 한계(f22)로 바꾸고, 2026-09-30-area49-s8.md 40행의 '(2026-04, 프리프린트)' 는 'ICRA 2026 채택(arXiv 저자판)' 으로 고치는 것이 맞아 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f21·f22 에서 도출. 학회 발표 쪽수·DOI 는 확인하지 못함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의4제1항은 운행안전인증 기준으로 로봇의 최대 질량(적재물 포함) 500 kg 이하(1호)와 최대 속도 시속 15 km 이하(2호)를 정하고, 제2항은 그 밖의 세부사항을 산업통상부장관 고시로 위임한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "시행규칙[시행 2025-10-01, 산업통상부령 제1호] 제7조의4①: \"1. 로봇의 최대 질량(적재물의 질량을 포함한다): 500킬로그램 이하일 것 2. 로봇의 최대 속도: 시속 15킬로미터 이하일 것\", ② 고시 위임, [본조신설 2023. 11. 17.]. 수치 자체는 기존 내용(본문 100행, 인증기관 페이지 근거)이고 원조문 근거가 새 내용",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f26",
      "claim": "같은 시행규칙 제7조의5제1항은 운행안전인증 신청서에 횡단보도 통행방식, 통신장애 대응 시나리오, 사고발생 대응 시나리오, 혼잡상황 대응 시나리오 등을 담은 운행계획서를 첨부해 제출하도록 한다(4호).",
      "tag": "사실",
      "source_ids": [
        "ref-1470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제7조의5①4호: \"실외이동로봇의 운행계획서(실외이동로봇의 횡단보도 통행방식, 통신장애 대응 시나리오, 사고발생 대응 시나리오 및 혼잡상황 대응 시나리오 등을 포함한다)\", 본문 \"… 서류를 첨부하여 … 제출해야 한다. <개정 2025. 10. 1.>\"",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f27",
      "claim": "현행 「실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시」는 산업통상부고시 제2025-21호(2025-11-24 일부개정)이며 부칙에 따라 발령한 날부터 시행하고, 제4조는 운행안전인증 기준을 별표 3 으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "국가법령정보센터 행정규칙: \"[시행 2025. 11. 24.] [산업통상부고시 제2025-21호, 2025. 11. 24., 일부개정]\", 부칙 <제2025-21호> \"제1조(시행일) 이 고시는 발령한 날부터 시행한다.\" 제4조 \"운행안전인증 기준은 별표 3과 같다.\"",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "고시 제2025-21호 별표 3(실외이동로봇 운행안전인증 기준)의 상위 항목은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개이며, 한국로봇산업진흥원 인증 안내 페이지의 '총 8개 심사항목' 이름과 같다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "별표 3 PDF(law.go.kr flSeq=158938063) 항목 칸 1~8. 한국로봇산업진흥원 페이지 \"규격 및 운행속도, 겉모양, 동적 특성 등 총 8개 심사항목\"과 항목 표. 인증기관은 고시 체계 안의 기관이라 독립 교차 확인으로 세지 않음. 2023-07-28 기사(ref-992)의 '16가지'와의 대응(oq-230·oq-186)은 이번에 확인하지 못함",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "별표 3 의 1.규격 및 운행속도는 로봇과 적재물 질량 합계 500 kg 초과를 금지하고, 최대 운행 속도를 질량 230 kg 초과 500 kg 이하 5 km/h, 100 kg 초과 230 kg 이하 10 km/h, 100 kg 이하 15 km/h 로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "별표 3 1.가 \"로봇의 자체 질량과 적재물의 질량을 합하여 500 kg을 초과하지 않아야 한다\", 1.다 표 \"230 초과 500 이하 5 / 100 초과 230 이하 10 / 100 이하 15\" (km/h). 1.나 폭 800 mm(보도 최소 폭 2,500 mm 이상이면 1,200 mm)",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f30",
      "claim": "별표 3 1.라는 도로교통법상 어린이 보호구역·노인 보호구역·장애인 보호구역에서 로봇이 최대 운행 속도 5 km/h 를 지키는지 확인하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "별표 3 1.라 \"다항에도 불구하고, 도로교통법 제12조에 따른 어린이 보호구역, 제12조의2에 따른 노인 보호구역 또는 장애인 보호구역에서 로봇이 최대 운행 속도 5 km/h를 준수하는지 확인한다.\"",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f31",
      "claim": "별표 3 4.주변 인식은 로봇이 지정된 운행구역을 지키고 제한된 금지구역에 들어가지 않을 것(가), 사람이나 장애물을 감지해 안전하게 감속·정지 또는 회피할 것(다)을 요구하며, 다목의 평가 방법은 KS B 7320 의 5.6절(장애물 감지와 회피)을 따른다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "별표 3 4.가 \"로봇은 지정된 운행구역을 준수해야 하며 제한된 금지구역에 진입하지 않아야 한다.\" 4.다 \"로봇은 사람이나 장애물을 감지하여 안전하게 감속, 정지 또는 회피해야 하며, 평가 방법은 한국산업표준 KS B 7320의 5.6절(장애물 감지와 회피)에 따른다.\" 감속 거리·속도 수치는 별표에 없음",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f32",
      "claim": "별표 3 7.횡단보도 통행은 대기 장소에 도착했을 때 보행 신호가 이미 켜져 있으면 정지 상태로 기다렸다가 다음 보행 신호에 횡단하도록 하고(가.3), 횡단 중 통신이 끊기면 횡단을 마친 뒤 안전한 곳에 정차하도록 한다(나).",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "별표 3 7.가 3) \"로봇이 횡단보도 통행을 위해 대기장소에 도착한 시점에 보행 신호가 작동 중인 경우에는, 정지 상태로 대기 후 다음 보행 신호에 횡단할 것\", 7.나 \"횡단보도 통행 중 통신 단절이 발생한 경우, 로봇은 횡단보도 통행을 완료한 후 안전한 곳에 정차하여야 한다.\"",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f33",
      "claim": "별표 3 8.관제장치 다목은 주행 경로가 보행자 밀집 등으로 통행할 수 없으면 로봇이 관제장치에 알리고 관리자가 조치할 수 있어야 한다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "별표 3 8.다 \"로봇은 주행하는 경로에 보행자 밀집 등으로 인해 통행이 불가능한 경우 관제장치에 알리고 관리자에 의한 조치가 이루어질 수 있어야 한다.\" 같은 항 가·나(모든 로봇 식별, 위치·속력·배터리·통신 감도·상태 실시간 확인)·라(원격 정지 수단)",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f34",
      "claim": "49영역 본문 5절 실외 사례 제약 칸(100행)이 2023-07-28 기사의 '당시 개정안'으로 전한 질량별 속도 구간(230·100 kg 경계, 5·10·15 km/h)과 횡단보도 대기 규칙은 현행 고시 제2025-21호 별표 3 의 값과 같으므로, 현행 고시 원문을 근거로 바꿔 쓰고 보호구역 5 km/h 를 덧붙일 수 있어 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1469",
        "ref-992"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f29·f32 와 ref-992(2023-07-28 기사, 이번에 다시 열지 않음) 비교. 2023 개정안과 현행 고시 사이의 중간 개정 이력은 확인하지 않음",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f35",
      "claim": "ROP 가 실외 로봇의 관제 역할을 맡으면, 운행계획서의 통신장애·혼잡 대응 시나리오와 별표 3 8.다의 보행자 밀집 알림·관리자 조치, 보호구역 5 km/h 를 구역별 속도 제한 정책과 알림 흐름으로 연결해 두는 것이 필요하다.",
      "tag": "의견",
      "source_ids": [
        "ref-1469",
        "ref-1470"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f26·f30·f33 에서 도출. ROP 사업자가 인증 신청 주체인지는 확인한 조문에 없음(9절 기존 [추정] 유지)",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f36",
      "claim": "ISS(세르비아 표준원)가 제공하는 ISO 프로젝트 정보에서 ISO 13482:2014 는 2014-02-03 발행, 현재 단계 90.92(개정 예정)의 발행 표준(Published)으로 표시된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1471"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISS ISO 13482:2014 페이지: \"Publication date: Feb 3, 2014\", \"Current stage: 90.92\", \"Published\". iso.org 직접 열람은 403 이라 ISS 목록 기준. 개정판 ISO/FDIS 13482 의 50.20(2026-09-15) 단계는 기존 내용(ref-1117)이라 새로 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "ISS 가 제공하는 ISO 10218-1:2025(2025-02-05 발행) 적용 범위는 로봇·매니퓰레이터가 무인 산업용 트럭이나 이동 플랫폼에 고정되거나 그 일부일 때의 이동성(mobility) 관련 위험을 이 문서가 다루지 않는다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1472"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISS ISO 10218-1:2025 페이지 \"Publication date: Feb 5, 2025\", 범위 \"This document does not cover the hazards related to: … mobility when robots or manipulators are fixed to or part of driverless industrial trucks; — mobility when robots or manipulators are fixed to or part of mobile platforms\". Part 1 의 제외 위험만 확인. 이동 매니퓰레이터 전체가 표준 밖이라는 뜻은 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "국가표준 KS B 8252 '실내 이동로봇의 보호정지 시험방법'은 안전한 실내 공간에서 이동 로봇이 자율 주행할 때 정적 장애물에 대한 보호정지를 평가하는 시험방법 표준으로 ISO 13482 를 기반으로 하며, 2020-02-26 제정(고시 2020-0026)·2025-09-05 확인(고시 2025-0241, 5년 도래 확인)됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1473"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "e-나라표준인증 KS B 8252 상세: 적용범위 \"본 표준은 안전 실내 공간에서 이동 로봇의 자율 주행 중 정적 장애물의 보호정지를 평가하기 위한 것으로 ISO 13482를 기반으로 한다.\", 제정일 2020-02-26, 최종개정확인일 2025-09-05, 이력표. 표준 본문은 열지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "확인한 국내 실내 이동로봇 KS(KS B 8252)는 정적 장애물에 대한 보호정지 시험방법이어서, 움직이는 사람과의 속도·거리 기준값이나 병원·상업 시설·공동주택 실내 운행을 강제하는 기준은 이번에도 확인되지 않았다(oq-231 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1473",
        "ref-1471"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f36·f38 에서 도출. KS B 8252 본문·ISO 13482 본문 미열람이라 동적 사람 근접 요구가 본문에 없는지는 확정하지 못함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "공개 ROS 2 패키지 human_detection_fusion 은 YOLO 검출과 UWB 위치를 합쳐 사람 식별자별 위치를 '/humans/persons/<id>/position' 토픽에 ROS4HRI 의 hri_msgs/PointOfInterest3DStamped 형식으로 발행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1474"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "src/yolo_uwb_fusion_node.cpp(커밋 934ca83) get_or_create_position_pub: create_publisher<hri_msgs::msg::PointOfInterest3DStamped>(\"/humans/persons/\" + person_id + \"/position\", 10). README 의 'Standard ROS4HRI output' 은 프로젝트 자기 서술",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f41",
      "claim": "같은 코드의 transformUWBPosition 함수는 UWB 좌표를 계획 좌표계로 바꾸다 TF 변환 예외가 나면 경고 로그를 남기고 입력 좌표를 그대로 돌려준다.",
      "tag": "사실",
      "source_ids": [
        "ref-1474"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "transformUWBPosition: try { tf_buffer_->transform(…, TARGET_FRAME, …); return stamped_out.point; } catch (const tf2::TransformException& ex) { RCLCPP_WARN(… \"UWB TF transform %s→%s failed\" …); return pt; }",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "호출부는 반환된 좌표에 header.frame_id 를 TARGET_FRAME(계획 좌표계)으로 붙여 발행하므로, 변환이 실패하면 UWB 좌표계 값이 계획 좌표계 값으로 표시돼 나갈 수 있어 보인다. 실제 운용에서 오류가 났는지, 상위 계층이 이를 보정하는지는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1474"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "topic_callback 의 UWB 작업자 처리: auto uwb_in_target = transformUWBPosition(worker.position); poi.header.frame_id = TARGET_FRAME; … publish(poi). 조건부 코드 경로에 대한 해석이며 사고·운용 실패의 실증이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f43",
      "claim": "이 저장소의 'KIRO' 는 EU ARISE 1차 공개 모집의 실험 이름으로, 한국로봇융합연구원(KIRO)과는 다른 것이며, 저작권자는 그리스 연구기관 ATHENA RC 이고 라이선스는 AGPL-3.0 이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1474"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README \"the Human Detection and Tracking reusable module of the KIRO experiment (ARISE 1st Open Call)\", \"Copyright owner: ATHENA RC (KIRO partner), on behalf of the KIRO experiment within the ARISE …\", License AGPL-3.0. 기본 파라미터 planning_frame 'kiro_base_link'",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "사람 위치를 받아 플릿 감속·정지에 쓰는 ROP 연계에는 측정 시각, 좌표계, 변환 성공 여부, 만료 시각을 메시지에 명시하게 하고, 위치 수신과 차량의 실제 감속 확인을 별도 단계로 시험해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1474",
        "ref-1080"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f40~f42 와 아마존 조끼 사례(벤더 주장, 기존 5절)에서 도출. 여러 제조사 플릿에 공통으로 쓰이는 감속·정지 인터페이스는 이번에도 확인하지 못함(oq-232)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f45",
      "claim": "확인한 자료 범위에서 사람 위치를 여러 제조사 플릿에 동시에 전달해 감속·정지시키는 공통 안전 인터페이스는 없고, 기업 단독 사례(아마존 조끼, 벤더 주장)와 사람 위치 발행 형식만 정한 공개 구현(ROS4HRI 기반 human_detection_fusion)이 따로 있는 것으로 보인다(oq-232 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1080",
        "ref-1474"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f40 과 기존 5절 아마존 사례(ref-1080)에서 도출. 공개 구현은 위치 발행까지이며 차량 감속 확인(ACK)·안전 등급은 다루지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "NavWareSet 프로젝트는 통제된 실내 수집 실험에 참가자 총 17명이 참여했고 5명씩 2개 그룹과 5개 쌍으로 나뉘었다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1475"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "프로젝트 사이트 Experiment description \"In total 17 participants were assigned numbers and divided in 2 groups of 5 and 5 pairs.\" 그룹과 쌍에 같은 참가자가 겹칠 수 있어 합산하지 않음. 연결 논문 IJRR 2026(온라인 2026-05-24, DOI 10.1177/02783649261447305)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f47",
      "claim": "NavWareSet 의 시나리오에는 시야가 가려진 모퉁이에서 로봇과 사람이 마주치는 'BLIND CORNER' 가 포함된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1475"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Scenarios 표 \"BLIND CORNER — A robot and human meet at a blind corner.\" 데이터 시나리오의 존재만 확인. 검출 실패율·충돌 위험의 실증 결과가 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f48",
      "claim": "사람 근접 감속·정지 정책의 재생 시험에는 가려진 모퉁이·통로 점유·혼잡 장면을 넣고, 아동·보행 보조기·휠체어 사용자처럼 감지 특성이 다른 보행자를 따로 평가해야 하며, 기존 데이터셋만으로 취약 보행자 범위가 충족됐다고 보면 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-1475",
        "ref-1085"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f46·f47 과 f21(성인 자원자 32명) 에서 도출. 취약 보행자 대상 독립 측정 자료는 확인하지 못함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f49",
      "claim": "아마존의 로보틱스 테크 조끼 설명 글은 페이지 메타데이터 기준 2019-04-06 에 발행됐다. 49영역 본문 72행과 2026-09-30-area49-s6.md 55행의 '발행일 미확인' 을 이 날짜로 고칠 수 있다.",
      "tag": "추정",
      "source_ids": [
        "ref-1080"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: aboutamazon.com 기사 HTML 메타 \"article:published_time\" 2019-04-06T20:46:20Z(\"datePublished\" 같은 값). 조끼 동작(감속·우회·근접 정지)은 기존 내용(본문 65~72행)이라 새로 넣지 않음. 벤더 문서만 근거라 [추정]",
      "as_of": "2026-10-11",
      "site_type": "물류창고",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f50",
      "claim": "확인한 명세·코드는 구역 제한의 지원 신고(supportedZones)·적재 외곽 기준 진입 판정·계획 계층 속도 반영까지만 다루고, 플릿 구역 제한을 위험성 평가의 위험 감소 조치로 인정하는 조건이나 로봇 보호 필드 설정과의 정합을 누가 검증하는지는 다루지 않는다(oq-229 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1464",
        "ref-1467"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f4·f6·f8·f9 에서 도출. VDA 5050 이 안전 표준이 아니라는 범위 문장은 기존 내용(docs/categories/safety/index.md 77행)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1466",
      "org": "SICK (Martin Kidman)",
      "title": "The perfect size of the protective field on an industrial autonomous vehicle",
      "published": "2021-02-09",
      "url": "https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "안전 레이저 스캐너 제조사의 기술 블로그. 보호 필드 크기 산정, 감시 케이스 전환·다중 샘플링이 응답시간에 더해진다는 설명을 담았다. 제조사 일반 설명이라 벤더 주장으로만 쓴다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1467",
      "org": "Open Navigation (Nav2 documentation, Jazzy)",
      "title": "Collision Monitor Node — Nav2 Docs (Jazzy)",
      "published": null,
      "url": "https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Nav2 Jazzy 의 Collision Monitor 노드 설정 문서. source_timeout(기본 2.0초, 0.0 이면 차단 해제) 등 파라미터 의미와 하드 실시간 안전 인증 미제공 문장을 담았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1468",
      "org": "Open Navigation (Nav2 documentation, Jazzy)",
      "title": "Speed Filter Parameters — Nav2 Docs (Jazzy)",
      "published": null,
      "url": "https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Nav2 Jazzy 코스트맵 Speed Filter 파라미터 문서. speed_limit 메시지 값 0 이 '제한 없음'을 뜻한다는 정의와 백분율·절댓값 설정을 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1469",
      "org": "산업통상부 (국가법령정보센터 행정규칙)",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준",
      "published": "2025-11-24",
      "url": "https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "2025-11-24 일부개정·시행된 현행 고시 본문과 별표 3(PDF, flSeq=158938063). 별표 3 은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치 8개 항목의 심사 기준(질량별 속도, 보호구역 5 km/h, 감속·정지·회피, 보행자 밀집 알림 등)을 정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1470",
      "org": "법제처 국가법령정보센터",
      "title": "지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5",
      "published": "2025-10-01",
      "url": "https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "시행규칙 현행판. 제7조의4 운행안전인증 기준(질량 500 kg·시속 15 km 이하, 세부 고시 위임)과 제7조의5 신청 서류(횡단보도 통행방식·통신장애·사고·혼잡 대응 시나리오를 담은 운행계획서)를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1471",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots",
      "published": "2014-02-03",
      "url": "https://iss.rs/en/project/show/iso:proj:53820",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 13482:2014 의 목록 정보(발행 2014-02-03, 단계 90.92, Published)와 적용 범위 요약. iso.org 가 403 이라 ISS 가 제공하는 ISO 목록으로 확인했다. 표준 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1472",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO 10218-1:2025 Robotics — Safety requirements — Part 1: Industrial robots",
      "published": "2025-02-05",
      "url": "https://iss.rs/en/project/show/iso:proj:73933",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 10218-1:2025 목록 정보(발행 2025-02-05, 단계 60.60)와 적용 범위. 범위는 무인 산업용 트럭·이동 플랫폼에 고정되거나 그 일부인 로봇의 이동성 위험을 제외한다. 표준 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1473",
      "org": "국가기술표준원 (e-나라표준인증)",
      "title": "KS B 8252 실내 이동로봇의 보호정지 시험방법",
      "published": "2020-02-26",
      "url": "https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "국가표준 목록 상세. 안전한 실내 공간에서 자율 주행 중 정적 장애물 보호정지를 평가하는 시험방법(ISO 13482 기반), 2020-02-26 제정·2025-09-05 확인. 표준 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1474",
      "org": "ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험",
      "title": "human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18)",
      "published": "2026-06-29",
      "url": "https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "YOLO 검출과 UWB 위치를 합쳐 ROS4HRI 형식(/humans/persons/<id>/position, PointOfInterest3DStamped)으로 사람 위치를 내보내는 ROS 2 패키지. 'KIRO' 는 EU ARISE 실험 이름이며 한국로봇융합연구원과 무관하다. 날짜는 고정 커밋 시각.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/nikolaslps/human_detection_fusion/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1475",
      "org": "Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트)",
      "title": "NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트)",
      "published": "2026-05-24",
      "url": "https://anr-navware.github.io/navwareset/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "실내 사회적 로봇 주행 데이터셋 프로젝트 사이트. 로봇 2대·7개 설정, 참가자 17명, BLIND CORNER 등 시나리오를 설명한다. 연결 논문은 IJRR 2026(온라인 2026-05-24, DOI 10.1177/02783649261447305), 권호는 아직 임시.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1075",
      "org": "Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing)",
      "title": "Implementing Speed and Separation Monitoring in Collaborative Robot Workcells",
      "published": "2017",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "NIST 의 SSM 구현 논문. 이번에 NIST 공개 PDF 로 학술지 서지(RCIM 44권, 2017, 144–155쪽, 2016-08-01 승인)를 확인했다. 기존 위키의 '2016' 표기는 승인 연도 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=914783",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0.0 명세. 이번에 3.0.0 태그 본문에서 §6.4 supportedZones 보고 의무와 §6.4.1.1 외곽(적재물 포함) 기준 구역 진입 규칙을 새로 확인했다. 발표일은 명세 안에 근거가 없어 적지 않는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1464",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_ros2 2.14.0 태그의 플릿 어댑터 소스. 이번에는 같은 파일의 limit_lane_speeds 처리(0 이하·범위 밖 요청 무시와 close_lanes 안내, 유효 요청의 차선 속성 반영과 Planner 재생성)를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1082",
      "org": "Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE)",
      "title": "Safe Human Robot Navigation in Warehouse Scenario",
      "published": "2025-03-27",
      "url": "https://arxiv.org/abs/2503.21141",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "학습 기반 CBF 를 Open-RMF 에 통합한 창고 연구(arXiv v1). 실물 로봇(Freight·Jackal·Megarover)·OptiTrack 실험과 Table IV 조건을 확인했다. 출판판은 2025 IEEE CASE pp.548–555(UC eScholarship 2025-08-17, DOI 10.1109/CASE58245.2025.11164151).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2503.21141v1",
      "source_unopened": false
    },
    {
      "id": "ref-1083",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "움직임 지도 기반 사람 인지형 작업 배정(HATA). 평가가 사람 궤적 재생 시뮬레이션이고 실패율이 교착·10분 타임아웃 기준임을 확인했다. 출판판 IROS 2025 pp.12697–12703(2025-10, DOI 10.1109/IROS60139.2025.11246701).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2508.19731v1",
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Tartu 대학병원 현장 시험 논문. 이번에는 이종 다로봇(TIAGo·Jackal) 검증이 시험 환경에서 이뤄졌고 병원 내 복수 배송 로봇 적용은 향후 과제라는 문장을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1081",
      "org": "Rondoni 외 (Scientific Reports)",
      "title": "Navigation benchmarking for autonomous mobile robots in hospital environment",
      "published": "2024-08-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "병원 물류 로봇 HOSBOT·TIAGo 의 주행 벤치마크. 실제 병원 배치를 재현한 모의 병원 공간에서의 실물 실험(Vicon 8대), 원격조종 이동 장애물을 확인했다. 원문 제목은 단수 'hospital environment'.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.nature.com/articles/s41598-024-69040-z",
      "source_unopened": false
    },
    {
      "id": "ref-1085",
      "org": "Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택)",
      "title": "Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters",
      "published": "2026-04-15",
      "url": "https://arxiv.org/abs/2604.13677",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "보행자 편안함 예측 실험(arXiv v1, ICRA 2026 채택 저자판). 참가자 32명, 3.2 m 복도, 1.4·2.8 m/s 원격조종 로봇, 같은 데이터 평가, 오즈비 3.67 의 의미를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2604.13677v1",
      "source_unopened": false
    },
    {
      "id": "ref-1080",
      "org": "Amazon",
      "title": "Ever wonder how people and robots team up on your Amazon order?",
      "published": "2019-04-06",
      "url": "https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "아마존 풀필먼트 센터의 로보틱스 테크 조끼 설명 글(회사 서술과 직원 인용). 페이지 메타데이터로 발행일 2019-04-06 을 확인했다. 벤더 주장으로만 쓴다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "인증기관의 실외이동로봇 운행안전인증 안내. '총 8개 심사항목'과 항목 이름이 현행 고시 별표 3 상위 항목과 같음을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "2023-07-28 기사. 당시 개정안의 질량별 속도·횡단보도 대기 규칙과 '16가지' 안전기준을 전했다. 이번에는 다시 열지 않고 기존 위키 기록과 비교만 했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/safety/human-proximity-safety.md",
      "sections": [
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 4(분리 2026-09-30-area49-s4) — NIST 논문 서지 정정: 학술지판 RCIM 44(2017), 2016-08-01 승인(f1). 본문 53행·s4 28·37행·s8 37행의 '2016' 표기를 '2017(2016 승인)'으로. ZR·ZS 위치 불확실성(메모 H02)은 기존 내용 확인(2026-09-30-area49-s4.md 38행) / 섹션 5 — 물류창고: 아마존 글 발행일 2019-04-06(f49, 벤더 주장 [추정]; 본문 72행·s6 55행 '발행일 미확인' 정정), Farrell 연구 문단(본문 74행)의 '정량 결과는 미확인' 정정 — 실물 로봇·OptiTrack·설정별 10회(f12), Table IV 4대·1.0 m/s/2대·1.5 m/s·보행자 0~2명·정지 구간 제외(f13), CASE 2025 서지(f14). 병원: 89행 '시뮬레이션 평가' 정정 — 실제 병원 배치를 재현한 모의 병원의 실물 실험·Vicon 8대(f18), 이동 장애물은 원격조종 로봇(f19), 정정 제안 f20. 같은 오류가 docs/categories/safety/index.md 125행·187행에도 있으나 이번 실행 범위 밖이라 후속 정리 필요. Tartu: 이종 다로봇은 시험 환경·병원 내 복수 배송 로봇은 향후 과제(f17), 혈액 운반 시연(메모 H19)은 기존 내용 확인(ref-869). 실외: 제약 칸(100행)의 질량별 속도·횡단 대기를 2023 기사 '당시 개정안'에서 현행 고시 제2025-21호 별표 3 근거로 바꾸고(f27·f29·f32·f34), 보호구역 5 km/h(f30), 감속·정지·회피(f31), 보행자 밀집 알림(f33)을 더함; 시행규칙 원조문(f25, 수치는 기존·근거만 새), 운행계획서 시나리오(f26), 의견 f35 / 섹션 6(분리 2026-09-30-area49-s6) — 보호 분리 거리: SICK 케이스 전환·다중 샘플링 응답시간(f2, 벤더 주장 [추정]); NIST 0.113 s(메모 H01)는 기존 내용 확인(s6 41행). 플릿 구역: supportedZones 보고 의무(f3), 적재 외곽 기준 진입(f4), 의견 f5; maximumSpeed m/s·진입 시 이미 제한 속도 도달(메모 H06·H07)은 기존 내용 확인(docs/categories/safety/index.md 77행), zoneSetId 변경·DISABLED 후 enableZoneSet(메모 H08·H09)은 기존 내용 확인(2026-09-30-area16-s6.md 49행, 2026-09-30-area16-s4.md 40행). 로봇 측: source_timeout 0.0 차단 해제(f6), speed_limit 0 = 제한 없음(f7), RMF 0 이하 무시·close_lanes(f8)·계획 반영까지만(f9), 0 값 의미 차이 [추정](f10), 의견 f11; Nav2 하드 실시간 인증 미제공(메모 H10)은 기존 내용 확인(s6 47행, ref-1077). s6 55행 Farrell 문장 정정(f12·f13), s6 57행 HATA 는 시뮬레이션·실패율 정의(f15·f16) 보강. s6 61행 Jafari '(실험 장소·참가자 수 미확인)' 정정 — 32명·3.2 m 복도·1.4/2.8 m/s·원격조종(f21), 같은 데이터 평가(f22), 오즈비 의미(f23), 정정 제안 f24. 데이터셋: NavWareSet 17명(f46)·BLIND CORNER(f47), 의견 f48 / 섹션 7(분리 2026-09-30-area49-s7) — 실외이동로봇 운행안전인증 행(44행): 시행규칙 제7조의4·제7조의5 원조문(f25·f26), 현행 고시 제2025-21호(f27)·별표 3 상위 8개 항목과 인증기관 8개 항목 일치(f28), 질량별 속도(f29). 새 행: ISO 13482:2014 발행·90.92(f36; ISO/FDIS 13482 50.20·2026-09-15(메모 H30)은 기존 내용 확인 — ref-1117), ISO 10218-1:2025 범위의 이동성 위험 제외(f37, 판 번호는 쓰지 않음), KS B 8252 정적 장애물 보호정지 시험방법(f38)과 한계(f39). Nav2 Collision Monitor 행에 source_timeout(f6), Speed Filter 0 값(f7) 추가 / 섹션 8(분리 2026-09-30-area49-s8) — Farrell 항목(42행) 서지를 CASE 2025(pp.548–555, 2025-08-17)로·'정량 결과 미확인' 삭제(f14), Rondoni 항목(41행) 제목 단수 'environment'·'모의 병원 환경' → 실물 모의 병원 실험(f20), Jafari 항목(40행) ICRA 2026 채택·32명(f24), HATA 항목(43행) IROS 2025 pp.12697–12703·시뮬레이션 평가·실패율 정의(f15·f16), NIST 항목 연도(f1), NavWareSet 새 항목(f46·f47) / 섹션 9 — 로봇 자체 지능·제어 행: 0 값 계약 차이와 어댑터 명령 구분(f10·f11), 사람 위치 연계 공개 구현 human_detection_fusion 의 ROS4HRI 발행(f40)·변환 실패 시 원좌표 반환(f41)·좌표계 표기 문제 [추정](f42)·'KIRO' 는 EU ARISE 실험 이름(f43, 한국로봇융합연구원 아님), 의견 f44; 업종별 조건 행: 운행계획서·보행자 밀집 알림(f26·f33·f35). 아마존 조끼(메모 H34)는 기존 내용 확인(본문 65~72행), 발행일만 f49 / 섹션 11 — 해결 제안 없음, 부분 근거만: oq-229(f50, 바탕 f3·f4·f8·f9), oq-230(f28 — 현행 별표 3 상위 8개 항목과 인증기관 8개 항목은 일치하나 기사 16가지와의 대응은 미확인; 오늘 50번 영역에서도 다루므로 부분 답변으로 둠), oq-231(f38·f39), oq-232(f40·f45). 관련 기존 질문: oq-186(16→8 개정 시점, 이번 미확인), oq-333(관제장치 항목 — 별표 3 8.가~라 f33 근거가 부분 관련). 메모의 새 질문 대조: U01→oq-229 하위, U08→f29·f32 로 답해 질문으로 올리지 않음, U09→oq-230·oq-186, U10→oq-064, U11→oq-254, U12→oq-231 하위, U13→oq-232, U14→oq-272 와 같아 새로 만들지 않음. U04(Farrell 독립 재현)·U06(Jafari 표 VI·VII 정밀도·재현율 산술)·U07(Tartu 장기 운영)은 이번 검증 범위 밖이라 올리지 않음. 새 질문 4건(U02·U03·U05·U15) / 다음 실행 후보: 50. 안전 표준·인증·사고 조사(f25~f29·f36~f38), 66. 실외(f29~f35), 63. 병원·의료(f17~f20), 20. 로봇·제조사 관제 연동(f8~f11), 19. 사람·보행자 모델(f40~f47)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "로봇별 반응 시간·제동 거리·적재 하중·센서 오차가 펌웨어 변경이나 운용 조건 변화로 바뀌었을 때, 로봇 측 보호 필드와 ROP 의 구역 속도 제한·감속 시작 지점을 함께 다시 검증하는 절차나 공개 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 57. 자산·소프트웨어 수명주기 관리 | 근거: f2 | 종류: 일반",
    "Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 같은 서로 다른 '0' 의미를 이종 플릿 어댑터가 올바르게 변환하는지 실행 시험으로 확인한 공개 자료나 적합성 시험 항목이 있는가? | 관련 영역: 49. 사람 근접 안전, 20. 로봇·제조사 관제 연동 | 근거: f10 | 종류: 일반",
    "HATA 의 임무 완료 시간 최대 26%·19% 단축을 다시 계산할 수 있도록 실험별 분모, 교착·타임아웃 실패 시행의 처리 방식, 고정된 실행 코드가 공개돼 있는가? | 관련 영역: 49. 사람 근접 안전, 25. 작업 배정 — MRTA | 근거: f16 | 종류: 일반",
    "아동·휠체어 사용자·보행 보조기 사용자·시각장애인이 가려진 모퉁이나 통로 점유 상황에서 로봇을 만날 때의 감지 누락·양보 결과를 독립적으로 측정한 데이터셋이나 시험 결과가 있는가? | 관련 영역: 49. 사람 근접 안전, 60. 노동·수용성·접근성 | 근거: f47 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 21,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-05/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f2: SICK 블로그는 원문 대조로 문장을 확인했으나 저장소 규칙(6.2 항목 13)에 따라 벤더 문서만 근거라 vendor_claim: true·[추정]으로 둔다. 특정 센서·하중 조건의 응답시간 실측값은 없음",
      "f49: 아마존 글 발행일(2019-04-06)은 페이지 메타데이터 기준이며 벤더 문서만 근거라 [추정]. 조끼 신호의 거리·지연·안전 등급은 여전히 미확인",
      "f14: Farrell 의 CASE 2025 쪽수(pp.548–555)·날짜(2025-08-17)는 UC eScholarship 기준이며 IEEE Xplore 원문은 열지 않음. Table IV 개별 수치는 옮기지 않음",
      "f15: HATA 출판판 쪽수(pp.12697–12703)는 검증 결과 기준이며 IEEE Xplore 원문은 열지 않음",
      "f24: Jafari 의 ICRA 2026 발표 쪽수·DOI 미확인(arXiv 저자판 표지의 채택 표기만 확인). 메모가 부록에서 제기한 Table VI·VII 정밀도·재현율 산술 불일치(U06)는 이번 검증 범위 밖이라 확인 못 함",
      "f28·f34(oq-230·oq-186): 현행 별표 3 상위 8개 항목과 인증기관 8개 항목의 일치는 확인했으나, 2023-07-28 기사의 '16가지' 가 어느 판·계층(세부 항목)에 대응하는지와 16→8 개정 시점은 이번에 확인하지 못함. ref-992 는 다시 열지 않음",
      "f36·f37: ISO 목록은 iso.org 403 이라 ISS(세르비아 표준원) 미러로 확인. ISO 10218-1:2025 의 판 번호는 쓰지 않음. 표준 본문 미열람",
      "f38·f39: KS B 8252 본문 미열람(목록·적용범위만). kssn.net 은 502 로 열리지 않아 e-나라표준인증 상세로 확인. 국내 병원·상업·공동주택 실내의 사람 근접 속도·거리 강제 기준은 여전히 미확인(oq-231)",
      "f42: human_detection_fusion 의 변환 실패 시 좌표계 표기 문제는 코드 경로 해석이며 실제 운용 오류·상위 보정 여부는 미확인. README 의 'Standard ROS4HRI output' 은 프로젝트 자기 서술",
      "f46: NavWareSet 연결 논문(IJRR 2026)의 권호는 임시(0(0))라 확정 서지로 쓰지 않음",
      "메모의 VDA 5050 '2026-03' 날짜는 명세 안에 근거가 없어 쓰지 않음(ref-031 published null 유지)",
      "oq-229(위험 감소 조치 인정 조건·검증 주체)·oq-232(이종 플릿 공통 감속·정지 인터페이스)는 부분 근거만 있고 답을 찾지 못함"
    ],
    "scope_violations": [
      "f2·f6·f7: 안전 레이저 스캐너 응답시간과 Nav2 Collision Monitor·Speed Filter 는 로봇 측 안전·로컬 회피 기능(연계 대상)이며, ROP 몫은 그 의미를 어댑터 계약에 반영하는 데로 한정",
      "f25~f35: 실외이동로봇 운행안전인증 법령·고시는 59. 법·규제·보험·라이선스, 50. 안전 표준·인증·사고 조사, 66. 실외와 겹치므로 이 영역에는 사람 근접 감속·정지·속도 기준 근거로만 씀",
      "f36~f39: 표준 목록 정보는 50. 안전 표준·인증·사고 조사 쪽 내용이며, 이 영역에는 사람 근접 요구의 적용 범위 확인용으로만 씀",
      "f40~f43: 사람 검출·추적 모듈은 19. 사람·보행자 모델 쪽 기술이며, 이 영역에는 사람 위치를 감속·정지로 연결하는 인터페이스 근거로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 10
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1466~ref-1475, 예약 구간 ref-1466~ref-1495 안), 재사용 11건(ref-1075·ref-031·ref-1464·ref-1082·ref-1083·ref-869·ref-1081·ref-1085·ref-1080·ref-980·ref-992). 출처 매핑(검증 결과 기준): 메모 n1→ref-1075(NIST 공개 PDF 로 열람), n2→ref-1466(벤더), n3→ref-031(3.0.0 태그), n4→ref-1467(Collision Monitor 문서 페이지; H10 은 기존 ref-1077 내용이라 이번 출처에서 뺌), n5→ref-1468, n6→ref-1464(오늘 48번 영역에서 등록), n7→ref-1082, n8→ref-1083, n9→ref-869, n10→ref-1081, n11→ref-1085, n12→ref-1469(산업통상부 게시글 대신 국가법령정보센터 고시 본문·별표 3), n13→ref-1470, n14→ref-1117(H30 기존 내용 확인만, finding 없어 sources 에서 뺌), n15→ref-1471, n16→ref-1473(standard.go.kr), n17→ref-1080, n18→ref-1474, n19→ref-1475, n20→ref-1472. 추가 재사용: ref-980(8개 항목 대조), ref-992(2023 기사 수치 비교, 이번 미열람). 교차 확인 0건 — 모든 [사실] finding 이 단일 출처이거나 같은 제도·프로젝트 계열(고시·시행규칙·인증기관은 같은 운행안전인증 체계, 코드·README 는 같은 저장소). 중복 제거: 메모 H01(NIST 0.113 s)·H02(ZR·ZS)·H06·H07(maximumSpeed m/s·진입 시 도달)·H08·H09(zoneSetId·enableZoneSet)·H10(Nav2 인증 미제공)·H19(Tartu 혈액 운반)·H30(ISO/FDIS 13482 50.20)·H34(아마존 조끼 동작)는 기존 위키에 있어 새 finding 으로 넣지 않고 위치만 rationale 에 적었다. 검증 반영: H03·H34 벤더 주장 [추정] 유지, H21·H22 로 본문 89행 정정(f20), Farrell 정량 미확인 문장 정정(f14), Jafari 참가자 정정(f24), 아마존 발행일(f49), NIST 연도(f1), 고시 표기 '제2025-21호' 통일, 메모가 '별표 미열람'으로 남긴 질량별 속도·횡단 조건은 별표 3 원문으로 확인(f29~f33), H36 의 좌표계 문제는 [추정] 시사점(f42), n18 'KIRO' 는 EU ARISE 실험명(f43), ISO 목록은 ISS 근거로 판 번호 없이(f36·f37). 현장 유형: 물류창고(f12~f14·f49), 병원(f17~f20), 실외(f25~f35). 국내 자료: 시행규칙(ref-1470)·고시(ref-1469)·KS(ref-1473)·인증기관(ref-980). 열린 질문 해결 제안 없음 — 부분 근거만: oq-229(f50), oq-230(f28, 오늘 50번 영역에서도 다룸), oq-231(f38·f39), oq-232(f40·f45). 메모의 새 질문 중 U01·U08~U14 는 기존 oq 와 같거나 이번 finding 으로 답해 새로 만들지 않았고, U02·U03·U05·U15 는 docs/open-questions.md 에 같은 질문이 없어 새로 올린다(U04·U06·U07 은 검증 범위 밖이라 보류). 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 원문 절·조항과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-11-05/verification.json

```json
{
  "run_id": "2026-10-11-05",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "PMC 판에서 RCIM 44권 144–155쪽, 2017-04 호, 온라인 게재 2016-08-27 확인. NIST PDF 는 검증 열람에서 텍스트를 추출하지 못해 접수(2015-03-04)·승인(2016-08-01) 날짜는 검증자가 확인하지 못함. '2016' 표기는 승인 연도가 아니라 온라인 게재 연도로도 설명되므로 해석 문구를 고치게 함(수정 지시)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "벤더 주장 [추정] 유지. SICK 블로그 실재·발행일 2021-02-09 는 검색 결과로 확인. 검증 열람은 ECONNRESET 로 2회 실패했고, 스니펫으로는 안전 장치·제어계 응답시간이 보호 필드 크기를 좌우한다는 일반 내용까지만 확인. 케이스 전환·다중 샘플링 문장은 검증자가 대조하지 못함(원문 미열람(검증)). 저자명은 검색 결과에서 확인 안 됨."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문(data/source_texts/ref-031.txt, 3.0.0) §6.4 의 supportedZones 보고 의무(shall) 문장과 일치. 확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "같은 원문 §6.4.1.1 Contour-based zones 의 적재물 포함 외곽 진입·이탈 문장과 일치. 확인."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f3·f4 에서 도출한 운영 시사점이며 감속 거리 수치를 넣지 않았음. 누구의 의견인지(구축자 의견) 밝히게 함."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "Nav2 Jazzy Collision Monitor 문서에서 source_timeout(double, 기본 2.0, 미수신 시 정지, 0.0 이면 차단 해제) 확인. 로봇 측 로컬 회피 계층이라 연계 대상으로 서술해야 함."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "Nav2 Jazzy Speed Filter 문서에서 'Zero value means no speed restriction (independently on percentage)' 확인."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "rmf_ros2 2.14.0 FleetUpdateHandle.cpp(raw) 에서 lane_index 범위 밖 또는 speed_limit <= 0.0 이면 경고 후 건너뛰고 close_lanes API 를 안내함을 확인. 경고문은 0 이하 경우만 언급함(범위 밖은 경고문에 없음)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "같은 함수에서 properties.speed_limit 설정 → 새 Planner → task_parameters 갱신 → publish_lane_states 확인, 실제 감속 확인 경로 없음 확인."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. f6~f8 을 나란히 놓은 추론이며 실사례·시험 자료 없음을 밝힘."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지(구축자 의견으로 표기)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2503.21141v1 에서 Freight·Jackal·Megarover 실물 실험, OptiTrack, 설정마다 10회 확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "Table IV 의 보행자 0·1·2명 행, 'Four Robot Controls (1.0m/s)'·'Two Robot Controls (1.5m/s)' 열, 정지 구간 제외 확인. 다만 본문이 로봇 대수를 명시하지 않고 열 이름에서 추론한 것이므로 표현을 고치게 함."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 정정 제안 유지. UC eScholarship 기록(CASE 2025, 2025-08-17, DOI 10.1109/CASE58245.2025.11164151)은 검색 결과로 확인. 쪽수 pp.548–555 는 검증자가 확인하지 못함."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2508.19731v1 에서 시뮬레이션 환경·사람 궤적 재생·5·10·15대 확인. IROS 쪽수는 검증자가 확인하지 못함."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "실패율 = 교착 또는 시간 초과로 완료하지 못한 과제 비율, 10분 제한 확인(HTML 에 '1010 minutes' 렌더링 오류가 있으나 다음 문장이 10분을 확인)."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "Frontiers 원문에서 시험 환경 검증·병원 내 복수 배송 로봇 미적용 문장 확인."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "PMC 판에서 실제 병원 배치를 재현한 모의 병원 공간, Vicon 8대 확인. 원제목은 단수 'hospital environment'."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "이동 장애물은 고정 선속도·각속도로 원격조종한 두 번째 이동 베이스임을 확인."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 정정 제안 유지(f18·f19 근거). docs/categories/safety/index.md 의 같은 표현은 이번 페이지 제안 범위 밖이므로 본문에 넣지 않음."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "arXiv 2604.13677v1 에서 32명(남 22·여 10), 23~41세, 3.2 m 복도, 원격조종, 1.4·2.8 m/s, 160회 중 2회 제외·측면 거리 분석 13회 추가 제외, IRB, ICRA 2026 채택 표기 확인."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "분석에 쓴 데이터로 예측기를 평가했고 엄밀한 평가에는 분할이 필요하다고 저자가 적은 것 확인."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "오즈비 3.67 이 분할표의 오즈비임을 확인. 초록의 '거의 4배 더 가능성' 표현은 확률로 읽으면 안 됨."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 정정 제안 유지. ICRA 쪽수·DOI 미확인 표기 유지."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "국가법령정보센터 시행규칙(시행 2025-10-01, 산업통상부령 제1호) 제7조의4①1·2호와 ② 고시 위임, 본조신설 2023-11-17 확인. 수치 자체는 기존 내용(ref-980)과 같음."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "같은 시행규칙 제7조의5①4호 운행계획서(횡단보도 통행방식·통신장애·사고발생·혼잡상황 대응 시나리오) 문구 확인, ① 개정 2025-10-01."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "고시 제목·산업통상부고시 제2025-21호·2025-11-24 일부개정·시행 2025-11-24 확인. 제4조·부칙 본문은 검증 열람에서 표시되지 않아 검증자가 문구를 대조하지 못함."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "한국로봇산업진흥원 페이지의 '총 8개 심사항목'과 8개 항목명 확인. 별표 3 PDF(flSeq=158938063)는 실재하나(작성 2025-12-09, 한글 PDF) 검증 열람에서 텍스트를 추출하지 못해 별표 쪽 항목명은 검증자가 대조하지 못함. 인증기관은 같은 제도 안의 기관이라 독립 교차 확인 아님."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "별표 3 원문 텍스트는 검증자가 추출하지 못함. 다만 검색 결과에 '로봇의 자체 질량과 적재물의 질량을 합하여 500 kg을 초과하지 않아야 한다'는 별표 문구와 폭 800 mm(보도 2,500 mm 이상이면 1,200 mm)가 나타나고, 230·100 kg 경계와 5·10·15 km/h 는 2023년 보도(ref-992 등)와 일치. 현행 별표 3 기준으로 단정하는 근거가 검증자 대조로는 간접적이므로 기준일·고시 번호를 함께 쓰게 함."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 별표 3 PDF 텍스트 추출 실패로 1.라(보호구역 5 km/h) 문구를 검증자가 대조하지 못했고, 검색(확장 포함)에서도 보호구역 5 km/h 규정은 나타나지 않음. 리서치 대조 기록만 근거이므로 '현행 별표 3 원문 기준(검증 재확인 못 함)'으로 표기."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 별표 3 4.가·4.다와 KS B 7320 5.6절 인용을 검증자가 원문에서 대조하지 못함(PDF 텍스트 추출 실패). 검색 결과로도 확인 못 함."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 7.가 3) 횡단 대기 규칙은 2023년 보도(ref-992)와 내용이 같으나 현행 별표 3 문구와 7.나 통신 단절 시 횡단 완료 후 정차는 검증자가 대조하지 못함."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 8.다 보행자 밀집 알림·관리자 조치 문구를 검증자가 원문에서 대조하지 못했고 검색에서도 나타나지 않음."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-992 는 이번에 다시 열지 않았고(원문 미열람), 비교 대상 f32 가 강등됐으므로 '현행 고시와 같다'는 표현을 추정 수준으로 유지. 2023 개정안과 현행 고시 사이 중간 개정 이력 미확인을 함께 적게 함."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f30·f33 이 [추정]으로 강등됐으므로 의견 문장에서 이를 확정 요구처럼 쓰지 않게 함. ROP 사업자가 인증 신청 주체라는 서술은 없음."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ISS 목록에서 ISO 13482:2014 발행 2014-02-03, 단계 90.92, Published 확인. 표준 본문 미열람."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ISS 목록에서 ISO 10218-1:2025 발행 2025-02-05, 단계 60.60, 범위의 무인 산업용 트럭·이동 플랫폼 이동성 위험 제외 문구 확인."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "e-나라표준인증 상세에서 표제·적용범위(정지 장애물 보호정지, ISO 13482 기반)·제정 2020-02-26(2020-0026)·확인 2025-09-05(2025-0241, 5년 도래 확인) 확인. 표준 본문 미열람."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. KS·ISO 본문 미열람이라 확정하지 못한다는 한계를 함께 적음."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "고정 커밋 코드에서 /humans/persons/<id>/position, hri_msgs PointOfInterest3DStamped 발행 확인. README 에 'Standard ROS4HRI output' 이라는 문구는 없고 ROS4HRI(hri_msgs) 형식으로 사람별 3차원 위치를 낸다는 자기 서술만 있음."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "transformUWBPosition 의 catch 블록이 경고 후 입력 좌표(pt)를 그대로 반환함을 확인."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. UWB 단독 작업자 처리에서 header.frame_id = TARGET_FRAME 설정 확인. 코드 경로 해석이며 운용 오류 실증 아님을 밝힘."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "README 에서 KIRO 실험(ARISE 1st Open Call)의 모듈, 저작권자 ATHENA RC, AGPL-3.0 확인."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지(구축자 의견으로 표기)."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. '확인한 자료 범위에서'라는 한정을 유지하고, 아마존 사례는 벤더 주장임을 병기."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "프로젝트 사이트에서 참가자 17명, 5명 2개 그룹과 5개 쌍 확인. 연결 논문 IJRR 2026, DOI 10.1177/02783649261447305 확인(권호는 임시)."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "Scenarios 표의 BLIND CORNER 설명 확인. 시나리오 존재만 말함."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지(구축자 의견으로 표기). 취약 보행자 측정 자료가 없다는 한계에서 나온 의견임을 밝힘."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·벤더 주장 유지. 검증 열람 도구는 페이지 메타데이터를 보여 주지 않아 2019-04-06 을 검증자가 재확인하지 못함. 2019년 보도(VOA 등)가 같은 조끼를 다뤄 2019년 무렵 글이라는 점과는 어긋나지 않음."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 확인한 명세·코드 범위에 한정한 부분 근거(oq-229)."
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
      "ref-1464 와 같은 날 실행 2026-10-11-04 브리프의 ref-1529 가 같은 URL(rmf_ros2 2.14.0 FleetUpdateHandle.cpp)을 가리킨다. 퍼블리셔가 같은 URL 을 합치므로 이 실행의 각주 id 와 제목이 합쳐진 id 와 어긋날 수 있다.",
      "ref-1464 의 기존 제목은 handle_target_emergency·Node.cpp 를 가리키는데 이번 인용 부분은 같은 파일의 limit_lane_speeds 다.",
      "f20 이 지적한 '시뮬레이션 평가' 표현이 docs/categories/safety/index.md 125·187행에도 있어 이번 갱신 뒤 49영역 본문과 대분류 페이지가 서로 다르게 된다(후속 정리 대상).",
      "f25·f29 의 질량·속도 수치는 기존 5절 실외 제약 칸(ref-980·ref-992)과 같은 주장이다. 새 각주를 추가하되 기존 각주를 지우지 않는다."
    ]
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
    "f30·f31·f32·f33: [사실] → [추정]으로 강등하고 문장에 '현행 고시 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)'을 밝힌다 — 검증 열람에서 별표 3 PDF 텍스트를 추출하지 못해 문구를 대조하지 못했다.",
    "f35(의견)·f34(추정)가 f30·f32·f33 에 기대는 부분은 확정된 규정처럼 쓰지 않고 '별표 3 원문 기준으로 알려진' 수준으로 쓴다 — 근거 finding 이 [추정]으로 강등됐다.",
    "f1: 4절·8절과 분리 주제 페이지의 NIST 논문 연도는 'Robotics and Computer-Integrated Manufacturing 44권(2017년 4월호), 144–155쪽, 온라인 게재 2016-08-27'로 쓰고, '2016 표기는 승인 연도 기준'이라는 해석과 접수일(2015-03-04)·승인일(2016-08-01)은 넣지 않는다 — PMC 판으로는 온라인 게재일만 확인됐고 접수·승인일은 검증에서 확인하지 못했다. ref-1075 의 reference_updates 발행일은 '2017'로 둔다.",
    "f13: 'Open-RMF 플릿 실험은 로봇 4대·2대 설정' 대신 'Table IV 의 열 이름(Four Robot Controls 1.0 m/s, Two Robot Controls 1.5 m/s) 기준'으로 쓴다 — 논문 본문은 로봇 대수를 명시하지 않는다.",
    "f14: Farrell 서지는 '2025 IEEE CASE(2025-08-17, DOI 10.1109/CASE58245.2025.11164151)'로 쓰고 쪽수 pp.548–555 는 쓰지 않거나 '쪽수 미확인'으로 둔다 — 검증에서 쪽수를 확인하지 못했다. f15 의 IROS 2025 쪽수(pp.12697–12703)도 같은 이유로 쓰지 않는다.",
    "f2·f49: [추정]에 '벤더 주장'을 병기한다. f49 의 아마존 글 발행일 2019-04-06 은 '페이지 메타데이터 기준(벤더 문서, 독립 확인 없음)'으로 밝히고 [사실]로 쓰지 않는다 — 검증 열람에서 메타데이터 날짜를 재확인하지 못했다.",
    "f2·f6·f7·f40~f43: 안전 레이저 스캐너 응답시간, Nav2 Collision Monitor·Speed Filter, 사람 검출·추적 모듈은 9절과 6절에서 '연계 대상'(로봇 자체 지능·제어, 19. 사람·보행자 모델 쪽 기술)으로 서술하고 ROP 몫은 어댑터 계약·인터페이스 반영으로 한정한다 — 분류 원문 19장 경계.",
    "f40: README 의 'Standard ROS4HRI output' 을 인용하지 않는다 — 고정 커밋 README 에 그 문구가 없고 ROS4HRI(hri_msgs) 형식 발행이라는 서술만 있다.",
    "f5·f11·f44·f48 및 f35: [의견] 문장에 '구축자 의견'을 밝힌다.",
    "f20: docs/categories/safety/index.md 125·187행의 같은 표현은 이번 페이지에서 고치지 않고 변경 이력·후속 정리 항목으로만 남긴다 — 이번 페이지 제안 범위 밖이다.",
    "각주: 49영역 페이지와 분리 주제 페이지의 ref-1081 제목을 단수 'Navigation benchmarking for autonomous mobile robots in hospital environment'로, ref-1075·ref-1080·ref-1082·ref-1083·ref-1085 의 접근일을 2026-10-11 로 갱신하고, 새로 인용하는 ref-1466~ref-1475·ref-869·ref-1464 를 프런트매터 sources 와 13절 각주 정의에 더한다. ref-992 각주는 '(원문 미열람)'을 접근일 뒤에 붙이고 reference_updates 에 source_unopened: true 로 둔다.",
    "ref-1464: 같은 URL 을 실행 2026-10-11-04 가 ref-1529 로 등록했으므로 reference_updates 의 제목을 'rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp'처럼 파일 전체를 가리키는 이름으로 두고 limit_lane_speeds 는 본문에서 함수 이름으로만 밝힌다 — 퍼블리셔의 같은 URL 병합 뒤 제목이 인용 내용과 어긋나지 않게 한다.",
    "인용: 출처마다 직접 인용은 1회 짧은 구절로 제한하고(특히 ref-1469·ref-031·ref-1464 는 여러 finding 에 원문 구절이 있으므로 페이지에서는 재서술), 별표 3 의 표는 복제하지 않는다.",
    "11절: oq-229·oq-230·oq-231·oq-232 는 열림을 유지하고 부분 근거만 덧붙인다(oq-229 f50, oq-230 f28, oq-231 f38·f39, oq-232 f40·f45). 새 열린 질문 4건은 브리프 문구대로 등록하되 '|' 필드 문자열을 question 에 남기지 않는다.",
    "5절 실외 사례: 제약 칸의 근거를 현행 고시(ref-1469)·시행규칙(ref-1470)으로 바꾸더라도 기존 2023-07-28 기사(ref-992) 문장은 '당시 개정안' 기준으로 남겨 두고, 심사 항목 수 충돌(8개 대 16가지)은 해결로 쓰지 않는다 — 기사 16가지와의 대응은 이번에도 확인되지 않았다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 46건, 미확인 4건, 교차 확인 0건. 강등: f30·f31·f32·f33 사실 → 추정(현행 실외이동로봇 운행안전인증 고시 별표 3 의 보호구역 5 km/h, 주변 인식 감속·정지·회피, 횡단보도 통신 단절 처리, 보행자 밀집 알림 — 별표 PDF 텍스트를 검증에서 추출하지 못해 문구를 대조하지 못함). 원문 미열람 출처: ref-992(이번 미열람). 검증 열람 일부 실패: ref-1466(SICK 블로그, 검색 결과로 실재만 확인), ref-1469(별표 3 본문 미대조, 고시 번호·개정일·시행일만 확인), ref-1075(NIST PDF 텍스트 미추출, PMC 판으로 서지 확인), ref-1080(메타데이터 발행일 재확인 못 함). 주의: 모든 [사실] 주장이 단일 출처이거나 같은 제도·저장소 계열이라 독립 교차 확인이 없다. 고시·시행규칙·인증기관은 같은 운행안전인증 체계이고, VDA 5050·Nav2·Open-RMF 의 구역·속도 제한은 안전 기능이 아니라 계획·로컬 회피 계층이다. Farrell 표 IV 의 로봇 대수는 열 이름에서 읽은 것이며, HATA 실패율은 사고율이 아니고 Jafari 의 오즈비 3.67 은 같은 데이터로 평가한 값이다. 열린 질문 oq-229~oq-232 는 부분 근거만 있어 열림을 유지한다. 정정 요청 없음. 같은 URL 이 ref-1464(이번)와 ref-1529(실행 2026-10-11-04)로 등록돼 퍼블리셔 병합이 필요하다. 검증 검색 6회 사용.",
  "retry_reason": null
}
```

### runs/2026-10-11-05/pages.json

```json
{
  "run_id": "2026-10-11-05",
  "pages": [
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "4·5·6·7·8·9·11·13절 차등 갱신: NIST 논문 서지 정정(2017년 4월호, 온라인 2016-08-27), 병원 사례 '시뮬레이션 평가'를 모의 병원 공간의 실물 실험으로 정정, 창고 연구 실험 조건·Table IV 조건 보강, 아마존 글 발행일(메타데이터, 벤더 주장), 실외 사례를 현행 시행규칙·고시 제2025-21호 별표 3 근거로 보강(별표 세부 문구는 [추정]), supportedZones·외곽 기준 구역, Nav2·Open-RMF '0' 값 의미 차이, HATA·Jafari 평가 조건, NavWareSet, ISO 13482·ISO 10218-1·KS B 8252 행, 사람 위치 발행 공개 구현과 한계, 열린 질문 부분 근거와 새 질문 4건, 각주 26건. 2차 재작업: 9절 human_detection_fusion 문장을 위치 발행 범위로 한정([추정]), 태그 없던 범위 문장 2건을 구축자 의견([의견])으로, 4·6·7·8·11절에 이전 분리 페이지(2026-09-30) 명시 링크, 분리될 절의 절 번호 참조를 원 페이지 링크로, 5절 실외 제약 칸에 ref-992 각주 복원",
      "patches": [
        {
          "section": "4. 핵심 개념과 용어",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md 의 해당 절을 본다)",
          "frontmatter": {
            "sources": [
              "ref-1075",
              "ref-1076",
              "ref-470",
              "ref-1077",
              "ref-031",
              "ref-980",
              "ref-992",
              "ref-1078",
              "ref-1080",
              "ref-1081",
              "ref-1082",
              "ref-1083",
              "ref-1084",
              "ref-1085",
              "ref-869",
              "ref-1464",
              "ref-1466",
              "ref-1467",
              "ref-1468",
              "ref-1469",
              "ref-1470",
              "ref-1471",
              "ref-1472",
              "ref-1473",
              "ref-1474",
              "ref-1475"
            ],
            "confidence": "medium",
            "last_run": "2026-10-11"
          }
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-11-area49-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"6. 대표 접근법과 기술\" 절(2,648자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area49-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,225자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area49-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"11. 열린 질문\" 절(1,847자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area49-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"8. 대표 연구와 자료\" 절(1,791자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area49-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 49. 사람 근접 안전 의 \"4. 핵심 개념과 용어\" 절(680자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-11 | 49. 사람 근접 안전 | 4·5·6·7·8·9·11·13절 차등 갱신: NIST 논문 서지 정정, 병원 사례를 모의 병원 공간의 실물 실험으로 정정, 창고·HATA·편안함 연구 평가 조건 보강, 실외 사례를 현행 시행규칙·고시 제2025-21호 별표 3 근거로 보강(별표 세부 문구 4건 추정), supportedZones·외곽 기준 구역과 Nav2·Open-RMF 0 값 의미 차이, ISO 13482·ISO 10218-1·KS B 8252, 사람 위치 발행 공개 구현과 한계, 이전 분리 페이지(2026-09-30) 링크 유지, 열린 질문 부분 근거와 새 질문 4건. 후속 정리 필요: docs/categories/safety/index.md 125·187행의 병원 시뮬레이션 평가 표현, 분리 주제 페이지 2026-09-30-area49-s4·s6·s8 의 옛 서지·미확인 표기 | run 2026-10-11-05",
  "index_updates": {
    "home_recent": "2026-10-11 — 49. 사람 근접 안전: 실외이동로봇 인증을 현행 시행규칙·고시 별표 3 근거로 보강하고, 병원·창고 연구의 평가 조건을 정정했으며, 플릿 구역 제한의 supportedZones·외곽 기준과 Nav2·Open-RMF 의 '0' 값 의미 차이를 더했다",
    "category_recent": "2026-10-11 — 49. 사람 근접 안전: 4·5·6·7·8·9·11·13절 차등 갱신(NIST 서지 정정, 병원 사례 실물 실험으로 정정, 실외 고시 제2025-21호 별표 3, KS B 8252·ISO 13482·ISO 10218-1, 사람 위치 발행 공개 구현, 새 열린 질문 4건). 후속 정리 필요: 이 대분류 페이지의 병원 '시뮬레이션 평가' 표현",
    "area_recent": "2026-10-11 — 49. 사람 근접 안전: 차등 갱신(4·5·6·7·8·9·11·13절). 이전 분리 주제 페이지(2026-09-30) s4·s6·s7·s8·s11 은 새 분리 페이지에서 링크하며, 그 페이지의 옛 서지·'미확인' 표기는 이번 갱신 내용으로 대신한다"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1466",
      "org": "SICK (Martin Kidman)",
      "title": "The perfect size of the protective field on an industrial autonomous vehicle",
      "published": "2021-02-09",
      "url": "https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "안전 레이저 스캐너 제조사의 기술 블로그. 보호 필드 크기 산정과, 감시 케이스 전환·다중 샘플링이 응답시간에 더해진다는 설명을 담았다. 제조사 일반 설명이라 벤더 주장으로만 쓴다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1467",
      "org": "Open Navigation (Nav2 documentation, Jazzy)",
      "title": "Collision Monitor Node — Nav2 Docs (Jazzy)",
      "published": null,
      "url": "https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Nav2 Jazzy 의 Collision Monitor 노드 설정 문서. source_timeout(기본 2.0초, 0.0 이면 차단 해제) 등 파라미터 의미를 담았다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1468",
      "org": "Open Navigation (Nav2 documentation, Jazzy)",
      "title": "Speed Filter Parameters — Nav2 Docs (Jazzy)",
      "published": null,
      "url": "https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Nav2 Jazzy 코스트맵 Speed Filter 파라미터 문서. 속도 제한 메시지 값 0 이 '제한 없음'을 뜻한다는 정의와 백분율·절댓값 설정을 설명한다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1469",
      "org": "산업통상부 (국가법령정보센터 행정규칙)",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준",
      "published": "2025-11-24",
      "url": "https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "2025-11-24 일부개정·시행된 현행 고시 본문과 별표 3. 별표 3 은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치 8개 항목의 심사 기준을 정한다. 별표 세부 문구 일부는 2026-10-11 검증에서 재확인하지 못했다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1470",
      "org": "법제처 국가법령정보센터",
      "title": "지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5",
      "published": "2025-10-01",
      "url": "https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "시행규칙 현행판. 제7조의4 운행안전인증 기준(질량 500 kg·시속 15 km 이하, 세부 고시 위임)과 제7조의5 신청 서류(횡단보도 통행방식·통신장애·사고·혼잡 대응 시나리오를 담은 운행계획서).",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1471",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots",
      "published": "2014-02-03",
      "url": "https://iss.rs/en/project/show/iso:proj:53820",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 13482:2014 의 목록 정보(발행 2014-02-03, 단계 90.92, Published)와 적용 범위 요약. ISS 가 제공하는 ISO 목록으로 확인했고 표준 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1472",
      "org": "Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보",
      "title": "ISO 10218-1:2025 Robotics — Safety requirements — Part 1: Industrial robots",
      "published": "2025-02-05",
      "url": "https://iss.rs/en/project/show/iso:proj:73933",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 10218-1:2025 목록 정보(발행 2025-02-05)와 적용 범위. 범위는 무인 산업용 트럭·이동 플랫폼에 고정되거나 그 일부인 로봇의 이동성 위험을 제외한다. 표준 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1473",
      "org": "국가기술표준원 (e-나라표준인증)",
      "title": "KS B 8252 실내 이동로봇의 보호정지 시험방법",
      "published": "2020-02-26",
      "url": "https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "국가표준 목록 상세. 안전한 실내 공간에서 자율 주행 중 정적 장애물 보호정지를 평가하는 시험방법(ISO 13482 기반), 2020-02-26 제정·2025-09-05 확인. 표준 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1474",
      "org": "ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험",
      "title": "human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18)",
      "published": "2026-06-29",
      "url": "https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "YOLO 검출과 UWB 위치를 합쳐 ROS4HRI(hri_msgs) 형식으로 사람 위치를 내보내는 ROS 2 패키지. 확인한 코드는 위치 발행까지만 다룬다. 'KIRO' 는 EU ARISE 실험 이름이며 한국로봇융합연구원과 무관하다. 날짜는 고정 커밋 시각.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1475",
      "org": "Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트)",
      "title": "NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트)",
      "published": "2026-05-24",
      "url": "https://anr-navware.github.io/navwareset/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "실내 사회적 로봇 주행 데이터셋 프로젝트 사이트. 참가자 17명, BLIND CORNER 등 시나리오를 설명한다. 연결 논문은 IJRR 2026(온라인 2026-05-24, DOI 10.1177/02783649261447305), 권호는 아직 임시.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1075",
      "org": "Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing)",
      "title": "Implementing Speed and Separation Monitoring in Collaborative Robot Workcells",
      "published": "2017",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "NIST 의 SSM 구현 논문. 학술지판은 Robotics and Computer-Integrated Manufacturing 44권(2017년 4월호) 144–155쪽, 온라인 게재 2016-08-27 이다(PMC 판 기준).",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0.0 명세. 이번에 3.0.0 태그 본문에서 supportedZones 보고 의무와 외곽(적재물 포함) 기준 구역 진입·이탈 규칙을 확인했다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1464",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_ros2 2.14.0 태그의 플릿 어댑터 소스 파일. 비상 신호 처리와 차선 속도 제한 처리(limit_lane_speeds: 0 이하·범위 밖 요청 무시와 close_lanes 안내, 유효 요청의 계획 반영)를 담고 있다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1082",
      "org": "Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE)",
      "title": "Safe Human Robot Navigation in Warehouse Scenario",
      "published": "2025-03-27",
      "url": "https://arxiv.org/abs/2503.21141",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "학습 기반 CBF 를 Open-RMF 에 통합한 창고 연구(arXiv v1). 실물 로봇·OptiTrack 실험과 Table IV 조건을 확인했다. 출판판은 2025 IEEE CASE(2025-08-17, DOI 10.1109/CASE58245.2025.11164151, 쪽수 미확인)로 보인다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1083",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "움직임 지도 기반 사람 인지형 작업 배정(HATA). 평가가 사람 궤적 재생 시뮬레이션이고 실패율이 교착·10분 타임아웃 기준임을 확인했다. 출판판 IROS 2025(쪽수 미확인).",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-869",
      "org": "Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI",
      "title": "Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test",
      "published": "2022-08-23",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Tartu 대학병원 현장 시험 논문. 이종 다로봇(TIAGo·Jackal) 검증은 시험 환경에서 이뤄졌고 병원 내 복수 배송 로봇 적용은 향후 과제라는 문장을 확인했다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1081",
      "org": "Rondoni 외 (Scientific Reports)",
      "title": "Navigation benchmarking for autonomous mobile robots in hospital environment",
      "published": "2024-08-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "병원 물류 로봇 HOSBOT·TIAGo 의 주행 벤치마크. 실제 병원 배치를 재현한 모의 병원 공간에서의 실물 실험(Vicon 8대)과 원격조종 이동 장애물을 확인했다. 원문 제목은 단수 'hospital environment'.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1085",
      "org": "Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택)",
      "title": "Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters",
      "published": "2026-04-15",
      "url": "https://arxiv.org/abs/2604.13677",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "보행자 편안함 예측 실험(arXiv v1, ICRA 2026 채택 저자판). 참가자 32명, 3.2 m 복도, 1.4·2.8 m/s 원격조종 로봇, 같은 데이터 평가, 오즈비 3.67 의 의미를 확인했다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1080",
      "org": "Amazon",
      "title": "Ever wonder how people and robots team up on your Amazon order?",
      "published": "2019-04-06",
      "url": "https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "아마존 풀필먼트 센터의 로보틱스 테크 조끼 설명 글. 발행일 2019-04-06 은 페이지 메타데이터 기준이며 독립 확인은 없다. 벤더 주장으로만 쓴다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "인증기관의 실외이동로봇 운행안전인증 안내. '총 8개 심사항목'과 항목 이름이 현행 고시 별표 3 상위 항목과 같음을 확인했다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-992",
      "org": "지디넷코리아",
      "title": "실외 배달로봇 '시속 15km 이하로'...16가지 안전기준",
      "published": "2023-07-28",
      "url": "https://zdnet.co.kr/view/?no=20230728173101",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 2023-07-28 기사로 당시 개정안의 질량별 속도·횡단보도 대기 규칙과 '16가지' 안전기준을 전했다. 이번 실행에서는 다시 열지 않고 기존 위키 기록과 비교만 했다.",
      "cited_by": [
        "docs/categories/safety/human-proximity-safety.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "로봇별 반응 시간·제동 거리·적재 하중·센서 오차가 펌웨어 변경이나 운용 조건 변화로 바뀌었을 때, 로봇 측 보호 필드와 ROP 의 구역 속도 제한·감속 시작 지점을 함께 다시 검증하는 절차나 공개 사례가 있는가?",
      "areas": [
        49,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 같은 서로 다른 '0' 의미를 이종 플릿 어댑터가 올바르게 변환하는지 실행 시험으로 확인한 공개 자료나 적합성 시험 항목이 있는가?",
      "areas": [
        49,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "HATA 의 임무 완료 시간 최대 26%·19% 단축을 다시 계산할 수 있도록 실험별 분모, 교착·타임아웃 실패 시행의 처리 방식, 고정된 실행 코드가 공개돼 있는가?",
      "areas": [
        49,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "아동·휠체어 사용자·보행 보조기 사용자·시각장애인이 가려진 모퉁이나 통로 점유 상황에서 로봇을 만날 때의 감지 누락·양보 결과를 독립적으로 측정한 데이터셋이나 시험 결과가 있는가?",
      "areas": [
        49,
        60
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/safety/human-proximity-safety.md#5-적용-사례-현장-유형-명시",
      "title": "49. 사람 근접 안전"
    }
  ],
  "additional_research_requests": [
    "분리 주제 페이지 docs/topics/2026/2026-09-30-area49-s4.md·s6.md·s8.md 정정: 이번 실행 입력에 이 페이지들이 없어 직접 고치지 못했다(이번 재작업에서는 새 분리 페이지에서 이 페이지들로 가는 명시 링크만 유지했다). 다음 49. 사람 근접 안전 갱신 실행에 세 페이지를 입력으로 넣어 NIST 논문 '2016' 표기(→ 2017년 4월호, 온라인 게재 2016-08-27), Farrell '정량 결과 미확인'·프리프린트 서지, Jafari '(실험 장소·참가자 수 미확인)'·프리프린트 표기, HATA 시뮬레이션 평가·실패율 정의, Rondoni 제목 단수 'hospital environment'·'모의 병원 환경' 표현, ref-1081·ref-1075 등 각주 접근일을 고쳐야 한다(1차 검증 수정 지시 3·11 항의 분리 페이지 부분).",
    "docs/categories/safety/index.md 125·187행의 Rondoni 연구 '시뮬레이션 평가' 표현과 Q. 현장 유형별 적용 목록의 63. 병원·의료 항목: 이번 페이지 제안 범위 밖이라 고치지 않았다. 다음 M. 안전 대분류 연결 실행에서 '실제 병원 배치를 재현한 모의 병원 공간의 실물 실험(이동 장애물은 원격조종 로봇)'으로 정정이 필요하다(f18·f19·f20 근거).",
    "실외이동로봇 운행안전인증 고시 제2025-21호 별표 3 의 1.라(보호구역 5 km/h)·4.가·4.다(운행구역·감속·정지·회피, KS B 7320 5.6절)·7.가 3)·7.나(횡단 대기·통신 단절 처리)·8.다(보행자 밀집 알림) 문구를 텍스트 추출 가능한 판본이나 별도 출처로 재대조해야 [사실]로 올릴 수 있다(5절 실외 사례 제약·예외·성과 칸, 7절).",
    "oq-230·oq-186: 2023-07-28 기사의 '16가지' 안전기준이 어느 판·계층(세부 항목)에 대응하는지, 2023 개정안과 현행 고시 제2025-21호 사이의 중간 개정 이력을 확인해야 출처 충돌을 정리할 수 있다(5절·11절).",
    "Farrell 외 CASE 2025·HATA IROS 2025 출판판의 쪽수, Jafari 외 ICRA 2026 발표 쪽수·DOI 를 공식 출판 기록으로 확인해야 8절 서지의 '쪽수 미확인'을 채울 수 있다.",
    "oq-231: KS B 8252·ISO 13482 본문에 움직이는 사람에 대한 근접 속도·거리 요구가 있는지 본문 열람이 필요하다(7절·11절).",
    "oq-229·oq-232: 플릿 구역 제한을 위험성평가의 위험 감소 조치로 인정한 사례·지침, 여러 제조사 플릿에 사람 위치를 전달해 감속·정지를 확인(ACK)하는 표준 인터페이스 사례를 찾아야 한다(6·9·11절)."
  ],
  "fixes_applied": [
    "f30·f31·f32·f33 강등 — 5절 실외 사례의 제약·예외·성과 칸과 7절 고시 별표 3 행에서 보호구역 5 km/h, 감속·정지·회피(KS B 7320 장애물 감지와 회피 절), 횡단 대기·통신 단절 처리, 보행자 밀집 알림을 [추정]으로 쓰고 '현행 고시 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)'을 밝혔다.",
    "f34·f35 — 5절 실외 제약 칸의 2023 개정안 비교를 '별표 3 원문 기준으로 알려진 현행 값과 같아 보인다'는 [추정]으로 쓰고 중간 개정 이력 미확인을 적었으며, 9절 업종별 조건 행의 구축자 의견도 '별표 3 원문 기준으로 알려진' 수준으로 썼다.",
    "f1 — 4절·8절의 NIST 논문 서지를 'Robotics and Computer-Integrated Manufacturing 44권(2017년 4월호), 144–155쪽, 온라인 게재 2016-08-27'로 고치고 승인 연도 해석과 접수·승인일은 넣지 않았으며, ref-1075 의 reference_updates 발행일과 각주 발행일을 2017 로 두었다. 분리 주제 페이지(2026-09-30-area49-s4·s8)는 이번 입력에 없어 직접 고치지 못해 4·8절에 그 페이지의 표기를 이 서지로 읽는다고 적고 additional_research_requests 에 올렸다.",
    "f13 — 5절 창고 연구 문단에서 플릿 실험을 'Table IV 의 열 이름(Four Robot Controls 1.0 m/s, Two Robot Controls 1.5 m/s) 기준'으로 쓰고 논문 본문이 로봇 대수를 명시하지 않는다고 밝혔다.",
    "f14·f15 — 5절·8절에서 Farrell 서지를 '2025 IEEE CASE(2025-08-17, DOI 10.1109/CASE58245.2025.11164151, 쪽수 미확인)'로 쓰고, HATA 의 IROS 2025 쪽수는 쓰지 않고 '쪽수 미확인'으로 두었다.",
    "f2·f49 — 6절·9절 SICK 응답시간 문장과 5절 아마존 글 발행일 문장에 '[추정] 벤더 주장'을 붙이고, 발행일 2019-04-06 은 '페이지 메타데이터 기준(벤더 문서, 독립 확인 없음)'으로 밝혔다.",
    "범위 경계 — 6절에서 보호 필드·응답시간, Nav2 Collision Monitor·Speed Filter 를 로봇 측 연계 대상으로 쓰고, 9절 표의 로봇 자체 지능·제어 행 외부 연계 칸에 스캐너 응답시간·Nav2 계층·사람 검출·추적 모듈(19. 사람·보행자 모델 쪽 기술)을 연계 대상으로 두었으며 ROP 몫은 어댑터 계약·인터페이스로 한정했다.",
    "f40 — 9절·7절에서 README 문구를 인용하지 않고 'ROS4HRI 의 hri_msgs 형식(PointOfInterest3DStamped)으로 발행한다'로만 썼다.",
    "f5·f11·f44·f48·f35 — 6절(f5·f11·f48)과 9절(f11·f44·f35)의 [의견] 문장마다 '구축자 의견으로는'을 밝혔다.",
    "f20 — docs/categories/safety/index.md 125·187행은 이 실행에서 고치지 않고 changelog_entry·index_updates.category_recent·additional_research_requests 에 후속 정리 항목으로만 남겼다.",
    "각주 — 13절을 다시 써서 ref-1081 제목을 단수 'hospital environment'로, ref-1075·ref-1080·ref-1082·ref-1083·ref-1085 접근일을 2026-10-11 로 고치고, ref-1466~ref-1475·ref-869·ref-1464 를 13절 각주 정의와 프런트매터 sources 에 더했으며, ref-992 는 접근일 뒤에 '(원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 로 두었다(본문에서 쓰지 않는 ref-1079 는 sources 에서 뺐다). 분리 주제 페이지의 각주는 입력에 없어 additional_research_requests 로 넘겼다.",
    "ref-1464 — reference_updates 와 각주 제목을 'rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp'로 두고 limit_lane_speeds 는 6절 본문에서 함수 이름으로만 밝혔다.",
    "인용 — 고시 별표 3·VDA 5050·Open-RMF 코드 문구는 모두 재서술했고 직접 인용 구절을 두지 않았으며, 별표 3 의 표는 복제하지 않고 질량별 속도 값만 문장으로 옮겼다.",
    "11절 — oq-229·oq-230·oq-231·oq-232 를 열림으로 유지하고 각각 f50·f28·f38·f39·f40·f45 부분 근거만 덧붙였으며, 새 열린 질문 4건을 브리프 문구대로 등록하되 '|' 필드 문자열은 question 에 남기지 않았다.",
    "5절 실외 사례 — 제약 칸 근거에 현행 시행규칙(ref-1470)·고시(ref-1469)를 더하면서 2023-07-28 기사(ref-992) 문장을 '당시 개정안' 기준으로 남겼고, 심사 항목 수 충돌(8개 대 16가지)은 해결로 쓰지 않고 기사 16가지와의 대응이 확인되지 않았다고 적었다.",
    "형식 검증 재작성 — 9절의 토픽 경로 '/humans/persons/<id>/position' 이 raw HTML 태그로 읽혀, 꺾쇠 없이 코드 표기 `/humans/persons/{id}/position` 와 '(id 는 사람 식별자)' 설명으로 바꿨다. 주장·태그·각주는 바꾸지 않았다.",
    "2차: 9절 human_detection_fusion 문장 — '사람 위치를 플릿 감속·정지에 잇는 공개 구현으로는 …이 있다'를 '사람 위치를 발행하는 공개 구현으로는 ROS 2 패키지 human_detection_fusion 이 있으며, 확인한 코드는 위치 발행까지만 다루고 플릿 감속·정지 명령이나 차량 감속 확인은 다루지 않는다. [추정][^ref-1474]'로 바꿨다(f40·f45).",
    "2차: 태그 없는 범위 문장 2건 — 9절 '사람 검출·추적은 … 인터페이스다.'를 뒤따르는 구축자 의견 문장에 합쳐 '구축자 의견으로는, 사람 검출·추적은 … 인터페이스이며, … 시험해야 한다. [의견][^ref-1474][^ref-1080]'로 쓰고, 6절 '보호 필드와 응답시간 설정은 …'을 '구축자 의견으로는, 보호 필드와 응답시간 설정은 로봇 자체 안전 기능이므로 ROP 에는 연계 대상으로 두어야 한다(원 페이지 9절). [의견][^ref-1466]'로 고쳤다.",
    "2차: 이전 분리 페이지 링크 — 4·6·7·8절(과 11절) 본문에 '이전 분리 페이지 [49. 사람 근접 안전 — <절 이름>(2026-09-30)](../../topics/2026/2026-09-30-area49-s<n>.md)' 명시 링크를 넣고 '그 페이지'를 '그 이전 분리 페이지'로 바꿨다. 자동 분리 때 지워지지 않도록 '자세한 내용은 주제 페이지 …에 있다' 문형을 쓰지 않았다. 6절의 '주제 페이지에 적은 임무 완료 시간 단축 결과'도 '이전 분리 페이지(2026-09-30)에 적은 …'으로 바꿨다.",
    "2차: 절 번호 참조 — 6절 '아래와 5절의 내용'·'(9절)', 7절 표의 '(6절)'·'(4·6절)'·'(9절)'을 '원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) n절'로 고쳤다. 5·9절은 분리되지 않으므로 그 안의 절 번호 참조는 그대로 두었다.",
    "2차: 5절 실외 사례 제약 칸 첫 문장의 각주를 [^ref-980][^ref-992][^ref-1470] 으로 고쳐 기존 ref-992 각주를 되살렸다.",
    "분량 초과 자동 분리: 49. 사람 근접 안전 본문 15,665자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 7,315자"
  ],
  "outline": [
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 200,
      "summary": "변경 없음. 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라 로봇·현장마다 다르다. [추정][^ref-1075]"
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 800,
      "summary": "SSM 과 VDA 5050 의 supportedZones·외곽 기준 구역을 정의하고, NIST 논문 서지를 2017년 4월호(온라인 게재 2016-08-27)로 바로잡으며 이전 분리 페이지를 링크한다. [사실][^ref-1075][^ref-031]",
      "planned_findings": [
        "f1",
        "f3",
        "f4"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3600,
      "summary": "물류창고(아마존 조끼, 벤더 주장·Farrell 실물 실험), 병원(모의 병원 공간의 실물 실험·Tartu), 실외(현행 시행규칙·고시 별표 3) 사례를 여섯 항목으로 쓴다. [사실][^ref-1081][^ref-1469]",
      "planned_findings": [
        "f12",
        "f13",
        "f14",
        "f17",
        "f18",
        "f19",
        "f20",
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
        "f49"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 3000,
      "summary": "보호 필드 응답시간(벤더 주장), 플릿 구역 제한의 supportedZones·외곽 기준, Nav2·Open-RMF 의 '0' 값 의미 차이, HATA·편안함 연구의 평가 조건, 재생 시험 데이터셋을 정리한다. [사실][^ref-031][^ref-1464]",
      "planned_findings": [
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
        "f15",
        "f16",
        "f21",
        "f22",
        "f23",
        "f46",
        "f47",
        "f48"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2300,
      "summary": "실외 인증의 시행규칙·고시 원조문, ISO 13482:2014·ISO 10218-1:2025·KS B 8252, Nav2·Open-RMF·VDA 5050·human_detection_fusion 행을 더하고, 국내 실내 사람 근접 기준은 확인되지 않았다고 적는다. [추정][^ref-1473][^ref-1471]",
      "planned_findings": [
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30",
        "f31",
        "f36",
        "f37",
        "f38",
        "f39",
        "f40"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1800,
      "summary": "NIST·Farrell·Rondoni·Tartu·HATA·Jafari·NavWareSet 의 서지와 평가 조건을 정정된 서지로 정리하고 이전 분리 페이지를 링크한다. [사실][^ref-1075][^ref-1081]",
      "planned_findings": [
        "f1",
        "f12",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f20",
        "f21",
        "f24",
        "f46",
        "f47"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 2700,
      "summary": "ROP 는 구역·속도 제한과 사람 위치 기반 조정, 어댑터 명령 구분을 맡고, 보호 필드·로컬 회피·사람 검출은 연계 대상이며, 사람 위치 발행 공개 구현은 위치 발행까지만 다루고 좌표계 한계가 있다. [추정][^ref-031][^ref-1474]",
      "planned_findings": [
        "f10",
        "f11",
        "f35",
        "f40",
        "f41",
        "f42",
        "f43",
        "f44",
        "f45"
      ]
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 200,
      "summary": "변경 없음. 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1084][^ref-031][^ref-1083]"
    },
    {
      "path": "docs/categories/safety/human-proximity-safety.md",
      "section": "11. 열린 질문",
      "budget_chars": 2000,
      "summary": "oq-229~oq-232 는 부분 근거만 더해 열림을 유지하고, 재검증 절차·'0' 값 변환 시험·HATA 재계산·취약 보행자 측정에 관한 새 질문 4건을 올린다. [의견][^ref-031][^ref-1469]",
      "planned_findings": [
        "f2",
        "f10",
        "f16",
        "f28",
        "f38",
        "f39",
        "f40",
        "f45",
        "f47",
        "f50"
      ]
    }
  ],
  "standards_updates": [
    {
      "name": "KS B 8252 실내 이동로봇의 보호정지 시험방법",
      "kind": "표준",
      "org": "국가기술표준원 (e-나라표준인증)",
      "url": "https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503",
      "related_areas": [
        49,
        50,
        54
      ],
      "summary": "안전한 실내 공간에서 자율 주행 중 정적 장애물에 대한 보호정지를 평가하는 시험방법 국가표준(ISO 13482 기반). 2020-02-26 제정, 2025-09-05 확인.",
      "ref_id": "ref-1473"
    },
    {
      "name": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 별표 3",
      "kind": "평가 프로그램",
      "org": "산업통상부",
      "url": "https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426",
      "related_areas": [
        49,
        50,
        59,
        66
      ],
      "summary": "2025-11-24 일부개정·시행된 현행 고시. 별표 3 은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치 8개 항목의 운행안전인증 기준과 질량별 최대 운행 속도를 정한다.",
      "ref_id": "ref-1469"
    },
    {
      "name": "human_detection_fusion (YOLO·UWB 사람 위치 융합 ROS 2 패키지)",
      "kind": "오픈소스",
      "org": "ATHENA RC (EU ARISE 'KIRO' 실험)",
      "url": "https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp",
      "related_areas": [
        19,
        49
      ],
      "summary": "YOLO 검출과 UWB 위치를 합쳐 사람 식별자별 위치를 ROS4HRI 의 hri_msgs 형식으로 발행하는 ROS 2 패키지(AGPL-3.0). 위치 발행까지만 다루며, 좌표 변환 실패 시 입력 좌표를 그대로 돌려주는 코드 경로가 있다.",
      "ref_id": "ref-1474"
    }
  ]
}
```

### runs/2026-10-11-05/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/safety/human-proximity-safety.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/safety/human-proximity-safety.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-11-area49-s6.md (2,648자)
    - docs/categories/safety/human-proximity-safety.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-11-area49-s7.md (2,225자)
    - docs/categories/safety/human-proximity-safety.md "11. 열린 질문" → docs/topics/2026/2026-10-11-area49-s11.md (1,847자)
    - docs/categories/safety/human-proximity-safety.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-11-area49-s8.md (1,791자)
    - docs/categories/safety/human-proximity-safety.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-11-area49-s4.md (680자)
```

### runs/2026-10-11-05/pages/categories/safety/human-proximity-safety.md

```markdown
---
title: "49. 사람 근접 안전"
type: area
category: "M. 안전"
area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [속도·분리 감시, 보호 분리 거리, 구역별 속도 제한, 운용 구역, 실외이동로봇 운행안전인증, 사람 인지형 배정]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-11
sources: [ref-1075, ref-1076, ref-470, ref-1077, ref-031, ref-980, ref-992, ref-1078, ref-1080, ref-1081, ref-1082, ref-1083, ref-1084, ref-1085, ref-869, ref-1464, ref-1466, ref-1467, ref-1468, ref-1469, ref-1470, ref-1471, ref-1472, ref-1473, ref-1474, ref-1475]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [M. 안전](index.md) › 49. 사람 근접 안전

# 49. 사람 근접 안전

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]

## 3. 왜 중요한가

확인한 자료를 종합하면, 사람과 지켜야 할 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라지므로 로봇·현장마다 다른 값이 된다. [추정][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 왜 중요한가](../../topics/2026/2026-09-30-area49-s3.md)에 있다.

## 4. 핵심 개념과 용어

사람 근접 안전의 핵심 개념은 사람과 지켜야 할 분리 거리를 계산하는 방식과, 그 거리를 지키도록 플릿 관제가 내리는 구역·속도 제한을 표현하는 방식이다. [의견][^ref-1075][^ref-031]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area49-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 물류창고

**사례:** 로봇 구역에 들어간 직원 주변에서 로봇이 감속·우회·정지(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 직원이 로봇 구역에 들어가며 로보틱스 테크 조끼를 착용·활성화한다. [추정] 벤더 주장[^ref-1080] |
| 작업 대상 | 로봇 구역(공간)과 그 안에서 일하는 직원(사람). [추정] 벤더 주장[^ref-1080] |
| 수행 자원 | 조끼를 켠 직원과 그 신호에 반응하는 로봇. [추정] 벤더 주장[^ref-1080] |
| 제약 | 조끼를 켜면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다. [추정] 벤더 주장[^ref-1080] 감속 속도·거리 값은 미확인이다. |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(처리량 영향 자료 없음) |

이 사례는 아마존이 자사 풀필먼트 센터 운영을 설명한 글에 근거하며, 그 글의 발행일은 페이지 메타데이터 기준 2019-04-06 이다(벤더 문서, 독립 확인 없음, 확인일 2026-10-11). [추정] 벤더 주장[^ref-1080] 조끼 신호의 거리·지연·안전 등급은 여전히 확인하지 못했다. 이 영역은 제약 칸, 곧 사람 위치 신호를 받아 어느 로봇을 감속·정지시킬지 정하는 부분에 관여한다. [의견][^ref-1080]

창고를 대상으로 한 연구로는 Farrell 외(arXiv 2025-03-27)가 학습 기반 제어 장벽 함수(Control Barrier Function, CBF)를 [Open-RMF](../../glossary/open-rmf.md) 에 통합해 보행자를 포함한 정적·동적 장애물 회피를 평가한 것이 있다. [사실][^ref-1082] 출판판은 2025 IEEE CASE(2025-08-17, DOI 10.1109/CASE58245.2025.11164151, 쪽수 미확인)인 것으로 보인다(UC eScholarship 기록 기준). [추정][^ref-1082] 실험은 Freight·Jackal·Megarover 실물 로봇으로 했고, 로봇과 보행자 위치는 OptiTrack 모션 캡처로 측정했으며, 정적·동적 장애물 회피 단위 실험은 설정마다 10회 수행했다. [사실][^ref-1082] 플릿 실험 표(Table IV)는 열 이름(Four Robot Controls 1.0 m/s, Two Robot Controls 1.5 m/s) 기준으로 두 설정에서 보행자 0·1·2명 조건을 비교했고(논문 본문은 로봇 대수를 따로 명시하지 않는다), 표의 값은 Open-RMF 상위 계획기가 로봇을 일부러 세워 둔 시간을 뺀 것이다. [사실][^ref-1082] 따라서 표의 값은 단위 실험과 분모가 다르고 전체 임무 처리량으로 옮겨 읽을 수 없는 것으로 보인다. [추정][^ref-1082] 이는 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가다. [사실][^ref-1082]

**현장 유형:** 병원

**사례:** 병원 물류 로봇의 사람 보행 속도 수준 주행 평가(실제 병원 배치를 재현한 모의 병원 공간)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병상·복도·대기 공간·가구 등 실제 병원의 물리적 배치를 재현한 모의 병원 공간. [사실][^ref-1081] |
| 수행 자원 | 병원 물류용 HOSBOT 과 TIAGo 실물 로봇, 위치 측정용 Vicon 카메라 8대. [사실][^ref-1081] |
| 제약 | 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켰고, 속도 선정 근거로 사람 보행 하한 0.6~1.3 m/s 를 인용했다. [사실][^ref-1081] 이동 장애물은 사람이 아니라 정해진 경로를 고정 선속도·각속도로 원격조종해 움직인 두 번째 시험용 이동 로봇 베이스였다. [사실][^ref-1081] |
| 완료·인계 | 미확인 |
| 예외·성과 | 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 최고 속도에서 방향 오차가 커졌으며 정확도는 중간 속도에서 가장 높았다. [사실][^ref-1081] |

이 사례는 실제 병원 구조를 재현한 모의 병원 공간에서 실물 로봇으로 수행한 실험 평가이며, 실제 환자와 함께 운영한 결과가 아니다(Scientific Reports, 2024-08-07). [사실][^ref-1081] 이동 장애물이 원격조종 로봇이었으므로, 사람을 대상으로 안전거리를 검증한 시험과는 구별해 읽어야 할 것으로 보인다. [추정][^ref-1081] 시험 속도는 법정 사람 근접 속도가 아니지만, 로봇 속도를 사람 보행 속도에 맞춰 고른 점이 이 영역의 '언제 느려져야 하는가'와 이어진다. [의견][^ref-1081]

같은 병원 현장 유형에서, Tartu 대학병원 현장 시험 논문(Frontiers in Robotics and AI, 2022-08-23)은 TIAGo·Clearpath Jackal 이종 로봇을 RMF 로 관리하는 능력을 시험 환경에서 검증했고, 병원 안에서 여러 배송 로봇을 운용하는 것은 아직 하지 않은 향후 과제로 적었다. [사실][^ref-869]

**현장 유형:** 실외

**사례:** 배송 로봇의 보도·횡단보도 운행(실외이동로봇 운행안전인증 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 배송 등 목적으로 자율주행·원격제어 로봇이 실외를 운행한다. [사실][^ref-980] 인증 신청 때는 횡단보도 통행방식과 통신장애·사고발생·혼잡상황 대응 시나리오를 담은 운행계획서를 낸다(시행규칙 2025-10-01 시행본 기준). [사실][^ref-1470] |
| 작업 대상 | 횡단보도를 포함한 실외 통행 공간. [사실][^ref-980] |
| 수행 자원 | 자율주행·원격제어 로봇과 관제장치의 조합(인증 단위). [사실][^ref-980] |
| 제약 | 최고 속도 15 km/h 이하·최대 질량 500 kg 이하이며, 시행규칙 제7조의4 는 이 두 기준(질량은 적재물 포함)을 정하고 세부사항을 고시에 맡긴다(2025-10-01 시행본, 확인일 2026-10-11). [사실][^ref-980][^ref-992][^ref-1470] 현행 고시(산업통상부고시 제2025-21호, 2025-11-24 시행) 별표 3 은 로봇과 적재물 질량 합계에 따라 최대 운행 속도를 230 kg 초과 500 kg 이하 5 km/h, 100 kg 초과 230 kg 이하 10 km/h, 100 kg 이하 15 km/h 로 나눈다(기준일 2026-10-11). [사실][^ref-1469] 현행 고시 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)으로는 어린이·노인·장애인 보호구역에서 5 km/h 준수를 확인하고, 사람이나 장애물을 감지하면 안전하게 감속·정지·회피해야 하며 그 평가는 KS B 7320 의 장애물 감지와 회피 절을 따른다. [추정][^ref-1469] 같은 기준으로 보행 신호가 이미 켜진 때 도착한 로봇은 정지 상태로 기다렸다가 다음 신호에 횡단하고, 횡단 중 통신이 끊기면 횡단을 마친 뒤 안전한 곳에 정차한다. [추정][^ref-1469] 2023-07-28 기사는 당시 개정안 기준으로 질량 합계 230 kg 초과면 5 km/h, 100 kg 초과면 10 km/h, 그 이하면 15 km/h 이고 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단한다고 전했다. [사실][^ref-992] 이 값은 별표 3 원문 기준으로 알려진 현행 값과 같아 보이나, 2023 개정안과 현행 고시 사이의 중간 개정 이력은 확인하지 못했다. [추정][^ref-1469][^ref-992] |
| 완료·인계 | 미확인 |
| 예외·성과 | 주변 인식과 비상정지가 심사 항목이고, 인증 뒤 2년 주기 정기점검을 받는다. [사실][^ref-980] 현행 고시 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)으로는 보행자 밀집 등으로 경로를 지날 수 없으면 로봇이 관제장치에 알리고 관리자가 조치할 수 있어야 한다. [추정][^ref-1469] |

이 사례는 특정 도입 현장이 아니라 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 따른 인증 요구를 여섯 항목으로 옮긴 것이다. [사실][^ref-980] 심사 항목 수는 인증기관 페이지(8개 항목)와 2023-07-28 기사(16가지)가 달라, 한쪽을 고르지 않고 11절 열린 질문으로 올렸다. [사실][^ref-980][^ref-992] 현행 고시 별표 3 의 상위 항목은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개로 인증기관 페이지의 8개 심사항목 이름과 같다. [사실][^ref-1469][^ref-980] 다만 인증기관은 같은 제도 안의 기관이라 독립 교차 확인이 아니며, 기사의 16가지가 어느 단위에 대응하는지는 이번에도 확인하지 못했다. 인증 대상에 관제장치가 포함된다는 점은 9절에서 ROP 범위와 겹칠 수 있는 경계로 다룬다.

제조 공장은 산업용 로봇 사업장 규정(7절)과 협동 작업셀 연구(6절)만 확인했고 현장 유형을 밝힌 적용 사례는 찾지 못했다. 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례도 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1077][^ref-031][^ref-1083][^ref-1085]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area49-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1084][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md)에서 다룬다.

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area49-s7.md)에 있다.

## 8. 대표 연구와 자료

사람 근접 안전의 대표 연구는 분리 거리 계산(NIST), 창고·병원 주행 평가, 사람 인지형 배정, 보행자 편안함, 사회적 주행 데이터셋으로 나뉘며, 각 연구의 평가 조건(실물·모의 공간·시뮬레이션)을 함께 읽어야 한다. [의견][^ref-1075][^ref-1081][^ref-1083]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-10-11-area49-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하고, 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하며, 그 조정과 정지·재개 이력을 기록한다. [추정][^ref-031][^ref-1080][^ref-1082][^ref-1083] 구축자 의견으로는 어댑터 계약에서 '제한 없음'·'양수 속도 제한'·'통로 폐쇄'·'보호 정지'를 다른 명령으로 구분하고, 구역 전송·활성화·계획 반영·차량 감속 관측을 별개 상태로 기록하는 일도 여기에 든다. [의견][^ref-1464][^ref-1468][^ref-031] | 연계 대상: 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(로봇 제조사·시스템 통합자), Nav2 Collision Monitor 같은 로봇 측 로컬 회피 계층. [추정][^ref-1075][^ref-470][^ref-1077][^ref-1078] 연계 대상: 안전 레이저 스캐너의 감시 케이스 전환·다중 샘플링에 따른 응답시간 보정. [추정] 벤더 주장[^ref-1466] 연계 대상: 센서 데이터가 끊기면 로봇을 세우는 Collision Monitor 와 속도 제한을 적용하는 Speed Filter. [사실][^ref-1467][^ref-1468] 연계 대상: 사람 검출·추적 모듈([19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md) 쪽 기술). [사실][^ref-1474] |
| 시설·설비 제어 | 설비·로봇의 안전 설정값과 상태를 받아 계획에 반영하는 인터페이스. [추정][^ref-1078][^ref-1084] | 연계 대상: 울타리 같은 설비 안전 조치, 현장 배치의 위험성 평가(IMR 시스템 통합자). [추정][^ref-1078][^ref-1084] |
| 업종별 조건 | 실외 속도 상한·횡단보도 대기 같은 조건을 작업·경로 제약으로 반영한다. [추정][^ref-980][^ref-992] 구축자 의견으로는, 실외 로봇의 관제 역할을 맡을 때 운행계획서의 통신장애·혼잡 대응 시나리오와, 별표 3 원문 기준으로 알려진 보행자 밀집 알림·관리자 조치와 보호구역 5 km/h 를 구역별 속도 제한 정책과 알림 흐름으로 연결해 두어야 한다. [의견][^ref-1469][^ref-1470] | 연계 대상: 실외 인증 대상인 로봇·관제장치 조합의 적합성(운영 사업자). [추정][^ref-980] 연계 대상: 운행안전인증 신청과 운행계획서 제출. [사실][^ref-1470] ROP 사업자가 신청 주체인지는 확인한 조문에 없다. |

VDA 5050 명세는 스스로 안전 표준이 아니라고 밝히고 Nav2 Collision Monitor 는 하드 실시간 안전 인증을 제공하지 않는다고 밝히므로, ROP 가 내리는 구역·속도 제한과 사람 인지형 조정은 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다. [추정][^ref-031][^ref-1077] 사람 위치 신호에 따른 조정은 벤더 주장과 연구 평가에 기대고 있어 현장 효과는 아직 확인되지 않았다. [추정][^ref-1080][^ref-1082][^ref-1083] 6절에서 본 '0' 값의 의미 차이와 계획 반영까지만 하는 Open-RMF 속도 제한 처리를 보면, ROP 가 내린 제한이 실제 감속으로 이어졌는지는 계획 상태와 별도로 확인해야 할 것으로 보인다. [추정][^ref-1464][^ref-1467][^ref-1468]

사람 위치를 발행하는 공개 구현으로는 ROS 2 패키지 human_detection_fusion 이 있으며, 확인한 코드는 위치 발행까지만 다루고 플릿 감속·정지 명령이나 차량 감속 확인은 다루지 않는다. [추정][^ref-1474] 이 패키지는 YOLO 검출과 초광대역(Ultra-Wideband, UWB) 위치를 합쳐 사람 식별자별 위치를 `/humans/persons/{id}/position` 형태의 토픽(id 는 사람 식별자)에 ROS4HRI 의 hri_msgs 형식(PointOfInterest3DStamped)으로 발행한다(고정 커밋 2026-06-29 기준). [사실][^ref-1474] 같은 코드의 transformUWBPosition 함수는 UWB 좌표를 계획 좌표계로 바꾸다 변환 예외가 나면 경고를 남기고 입력 좌표를 그대로 돌려준다. [사실][^ref-1474] 호출부가 반환 좌표에 계획 좌표계 이름을 붙여 발행하므로, 변환이 실패하면 UWB 좌표계 값이 계획 좌표계 값으로 표시돼 나갈 수 있어 보인다(코드 경로 해석이며 실제 운용 오류나 상위 계층의 보정 여부는 확인하지 못했다). [추정][^ref-1474] 이 저장소의 KIRO 는 EU ARISE 1차 공개 모집의 실험 이름으로 한국로봇융합연구원과는 다르며, 저작권자는 그리스 연구기관 ATHENA RC, 라이선스는 AGPL-3.0 이다. [사실][^ref-1474] 구축자 의견으로는, 사람 검출·추적은 로봇 자체 지능·제어 경계의 연계 대상이고 ROP 몫은 그 위치를 받아 감속·정지로 잇는 인터페이스이며, 이 연계에서 측정 시각·좌표계·변환 성공 여부·만료 시각을 메시지에 명시하게 하고 위치 수신과 차량의 실제 감속 확인을 별도 단계로 시험해야 한다. [의견][^ref-1474][^ref-1080]

실외이동로봇 운행안전인증의 대상은 로봇과 관제장치의 조합이므로, ROP 가 실외 로봇의 관제 역할을 맡으면 인증 범위와 겹칠 수 있다. [추정][^ref-980] 인증 적합성을 운영 사업자의 몫으로 본 것도 확인된 규정이 아니라 추론이다. [추정][^ref-980]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1084][^ref-031][^ref-1083]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md)에 있다.

## 11. 열린 질문

이 영역의 열린 질문은 플릿 구역 제한의 안전 인정 조건, 실외 인증 심사 항목 수의 출처 충돌, 국내 실내 사람 근접 기준, 이종 플릿 공통 감속·정지 인터페이스이며, 2026-10-11 실행은 네 질문 모두 부분 근거만 더했고 해결하지 못했다. [의견][^ref-031][^ref-1469]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 열린 질문](../../topics/2026/2026-10-11-area49-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [49. 사람 근접 안전](human-proximity-safety.md) — seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계, 연결 16건, 열린 질문 4건), 각주 15건 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area49-s6.md) — 자동 분리: 49. 사람 근접 안전 의 "6. 대표 접근법과 기술" 절(1,762자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area49-s7.md) — 자동 분리: 49. 사람 근접 안전 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,599자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-09-30-area49-s8.md) — 자동 분리: 49. 사람 근접 안전 의 "8. 대표 연구와 자료" 절(1,128자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md) — 자동 분리: 49. 사람 근접 안전 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,041자)을 옮겼다 (실행 2026-09-30-10)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-10-11
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1077]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-11
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-10-11 (원문 미열람)
[^ref-1078]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1080]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 2019-04-06, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-10-11
[^ref-1081]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environment, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-10-11
[^ref-1082]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-10-11
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-11
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1085]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-10-11
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11
[^ref-1464]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
[^ref-1466]: SICK (Martin Kidman), The perfect size of the protective field on an industrial autonomous vehicle, 2021-02-09, https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle, 접근일 2026-10-11
[^ref-1467]: Open Navigation (Nav2 documentation, Jazzy), Collision Monitor Node — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/, 접근일 2026-10-11
[^ref-1468]: Open Navigation (Nav2 documentation, Jazzy), Speed Filter Parameters — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/, 접근일 2026-10-11
[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-11
[^ref-1470]: 법제처 국가법령정보센터, 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5, 2025-10-01, https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075, 접근일 2026-10-11
[^ref-1474]: ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험, human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18), 2026-06-29, https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp, 접근일 2026-10-11
```

### docs/categories/safety/human-proximity-safety.md

```markdown
---
title: "49. 사람 근접 안전"
type: area
category: "M. 안전"
area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [속도·분리 감시, 보호 분리 거리, 구역별 속도 제한, 운용 구역, 실외이동로봇 운행안전인증, 사람 인지형 배정]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1075, ref-1076, ref-470, ref-1077, ref-031, ref-980, ref-992, ref-1078, ref-1079, ref-1080, ref-1081, ref-1082, ref-1083, ref-1084, ref-1085]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [M. 안전](index.md) › 49. 사람 근접 안전

# 49. 사람 근접 안전

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]

## 3. 왜 중요한가

확인한 자료를 종합하면, 사람과 지켜야 할 안전 거리는 로봇의 정지 성능과 센서 갱신 주기에 따라 달라지므로 로봇·현장마다 다른 값이 된다. [추정][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 왜 중요한가](../../topics/2026/2026-09-30-area49-s3.md)에 있다.

## 4. 핵심 개념과 용어

**속도·분리 감시(Speed and Separation Monitoring, SSM)** — 협동로봇 기술 시방서 ISO/TS 15066 의 방식으로, 로봇과 사람의 분리 거리가 보호 분리 거리 이하가 되면 안전 감시 정지를 건다(2016년 논문 기준). [사실][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area49-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 물류창고

**사례:** 로봇 구역에 들어간 직원 주변에서 로봇이 감속·우회·정지(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 직원이 로봇 구역에 들어가며 로보틱스 테크 조끼를 착용·활성화한다. [추정] 벤더 주장[^ref-1080] |
| 작업 대상 | 로봇 구역(공간)과 그 안에서 일하는 직원(사람). [추정] 벤더 주장[^ref-1080] |
| 수행 자원 | 조끼를 켠 직원과 그 신호에 반응하는 로봇. [추정] 벤더 주장[^ref-1080] |
| 제약 | 조끼를 켜면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다. [추정] 벤더 주장[^ref-1080] 감속 속도·거리 값은 미확인이다. |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(처리량 영향 자료 없음) |

이 사례는 아마존이 자사 풀필먼트 센터 운영을 설명한 글(발행일 미확인, 2026-09-30 확인)에 근거하며, 독립 출처로 확인하지 못했다. [추정] 벤더 주장[^ref-1080] 이 영역은 제약 칸, 곧 사람 위치 신호를 받아 어느 로봇을 감속·정지시킬지 정하는 부분에 관여한다. [의견][^ref-1080]

창고를 대상으로 한 연구로는 Farrell 외(2025-03)가 학습 기반 제어 장벽 함수(Control Barrier Function, CBF)를 [Open-RMF](../../glossary/open-rmf.md) 에 통합해 보행자를 포함한 정적·동적 장애물 회피를 평가한 것이 있다. [사실][^ref-1082] 이는 현장 배치 사례가 아니라 창고 시나리오를 대상으로 한 연구 평가이며, 정량 결과는 미확인이다. [사실][^ref-1082]

**현장 유형:** 병원

**사례:** 병원 물류 로봇의 사람 보행 속도 수준 주행 평가(모의 병원 환경)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 병원 물류 로봇이 주행하는 모의 병원 환경의 공간. [사실][^ref-1081] |
| 수행 자원 | 병원 물류용 HOSBOT 과 TIAGo 두 로봇. [사실][^ref-1081] |
| 제약 | 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켰고, 속도 선정 근거로 사람 보행 하한 0.6~1.3 m/s 를 인용했다. [사실][^ref-1081] |
| 완료·인계 | 미확인 |
| 예외·성과 | 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 최고 속도에서 방향 오차가 커졌으며 정확도는 중간 속도에서 가장 높았다. [사실][^ref-1081] |

이 사례는 실제 병원이 아닌 모의 병원 환경에서 수행한 시뮬레이션 평가다(Scientific Reports, 2024-08-07). [사실][^ref-1081] 로봇 속도를 사람 보행 속도에 맞춰 고른 점이 이 영역의 '언제 느려져야 하는가'와 이어진다. [의견][^ref-1081]

**현장 유형:** 실외

**사례:** 배송 로봇의 보도·횡단보도 운행(실외이동로봇 운행안전인증 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 배송 등 목적으로 자율주행·원격제어 로봇이 실외를 운행한다. [사실][^ref-980] |
| 작업 대상 | 횡단보도를 포함한 실외 통행 공간. [사실][^ref-980] |
| 수행 자원 | 자율주행·원격제어 로봇과 관제장치의 조합(인증 단위). [사실][^ref-980] |
| 제약 | 최고 속도 15 km/h 이하·최대 질량 500 kg 이하(인증기관 페이지, 2026-09-30 확인). [사실][^ref-980][^ref-992] 2023-07-28 기사가 전한 당시 개정안 기준으로는 로봇과 적재물 질량 합계가 230 kg 초과면 5 km/h, 100 kg 초과면 10 km/h, 그 이하면 15 km/h 이고, 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단한다. [사실][^ref-992] |
| 완료·인계 | 미확인 |
| 예외·성과 | 주변 인식과 비상정지가 심사 항목이고, 인증 뒤 2년 주기 정기점검을 받는다. [사실][^ref-980] |

이 사례는 특정 도입 현장이 아니라 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 따른 인증 요구를 여섯 항목으로 옮긴 것이다. [사실][^ref-980] 심사 항목 수는 인증기관 페이지(8개 항목)와 2023-07-28 기사(16가지)가 달라, 한쪽을 고르지 않고 11절 열린 질문으로 올렸다. [사실][^ref-980][^ref-992] 인증 대상에 관제장치가 포함된다는 점은 9절에서 ROP 범위와 겹칠 수 있는 경계로 다룬다.

제조 공장은 산업용 로봇 사업장 규정(7절)과 협동 작업셀 연구(6절)만 확인했고 현장 유형을 밝힌 적용 사례는 찾지 못했다. 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례도 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1077][^ref-031][^ref-1083][^ref-1085]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area49-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1084][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md)에서 다룬다.

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area49-s7.md)에 있다.

## 8. 대표 연구와 자료

Marvel·Norcross(NIST), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells(2016) — SSM 의 보호 분리 거리를 구성요소별로 나누고 NIST 시험 결과와 구현 한계(방향 무시에 따른 불필요한 정지, 센서 잡음, 갱신 주기)를 제시했다. [사실][^ref-1075]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-09-30-area49-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하고, 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하며, 그 조정과 정지·재개 이력을 기록한다. [추정][^ref-031][^ref-1080][^ref-1082][^ref-1083] | 연계 대상: 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(로봇 제조사·시스템 통합자), Nav2 Collision Monitor 같은 로봇 측 로컬 회피 계층. [추정][^ref-1075][^ref-470][^ref-1077][^ref-1078] |
| 시설·설비 제어 | 설비·로봇의 안전 설정값과 상태를 받아 계획에 반영하는 인터페이스. [추정][^ref-1078][^ref-1084] | 연계 대상: 울타리 같은 설비 안전 조치, 현장 배치의 위험성 평가(IMR 시스템 통합자). [추정][^ref-1078][^ref-1084] |
| 업종별 조건 | 실외 속도 상한·횡단보도 대기 같은 조건을 작업·경로 제약으로 반영한다. [추정][^ref-980][^ref-992] | 연계 대상: 실외 인증 대상인 로봇·관제장치 조합의 적합성(운영 사업자). [추정][^ref-980] |

VDA 5050 명세는 스스로 안전 표준이 아니라고 밝히고 Nav2 Collision Monitor 는 하드 실시간 안전 인증을 제공하지 않는다고 밝히므로, ROP 가 내리는 구역·속도 제한과 사람 인지형 조정은 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다. [추정][^ref-031][^ref-1077] 사람 위치 신호에 따른 조정은 벤더 주장과 연구 평가에 기대고 있어 현장 효과는 아직 확인되지 않았다. [추정][^ref-1080][^ref-1082][^ref-1083]

실외이동로봇 운행안전인증의 대상은 로봇과 관제장치의 조합이므로, ROP 가 실외 로봇의 관제 역할을 맡으면 인증 범위와 겹칠 수 있다. [추정][^ref-980] 인증 적합성을 운영 사업자의 몫으로 본 것도 확인된 규정이 아니라 추론이다. [추정][^ref-980]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

범위 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성 평가·표준·사람 이동 모델·구역 전달·배정·교통·협업·법규·수용성·평가와 적용 현장 영역에 이어진다. [추정][^ref-1084][^ref-031][^ref-1083]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md)에 있다.

## 11. 열린 질문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가?[^ref-031]

자세한 내용은 주제 페이지 [49. 사람 근접 안전 — 열린 질문](../../topics/2026/2026-09-30-area49-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [49. 사람 근접 안전](human-proximity-safety.md) — seed → draft: 3~11절 첫 작성(보호 분리 거리 계산, 로봇 측·플릿 수준 감속·정지, 적용 유형별 표준·인증, 물류창고·병원·실외 사례, 책임 경계, 연결 16건, 열린 질문 4건), 각주 15건 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area49-s6.md) — 자동 분리: 49. 사람 근접 안전 의 "6. 대표 접근법과 기술" 절(1,762자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area49-s7.md) — 자동 분리: 49. 사람 근접 안전 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,599자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 대표 연구와 자료](../../topics/2026/2026-09-30-area49-s8.md) — 자동 분리: 49. 사람 근접 안전 의 "8. 대표 연구와 자료" 절(1,128자)을 옮겼다 (실행 2026-09-30-10)
- 2026-09-30 · 생성 · [49. 사람 근접 안전 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area49-s10.md) — 자동 분리: 49. 사람 근접 안전 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,041자)을 옮겼다 (실행 2026-09-30-10)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-09-30
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1077]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1078]: 지디넷코리아, "협동로봇 충돌 안전 계산하고 써야죠", 2024-03-09, https://zdnet.co.kr/view/?no=20240305160245, 접근일 2026-09-30
[^ref-1080]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 미확인, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-09-30
[^ref-1081]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environments, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-09-30
[^ref-1082]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-09-30
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1085]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-09-30
```

### runs/2026-10-11-05/pages/topics/2026/2026-10-11-area49-s6.md

```markdown
---
title: "49. 사람 근접 안전 — 대표 접근법과 기술"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1075, ref-1077, ref-1083, ref-1085, ref-1464, ref-1466, ref-1467, ref-1468, ref-1475]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#6
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 대표 접근법과 기술

# 49. 사람 근접 안전 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1077][^ref-031][^ref-1083][^ref-1085]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 근접 안전의 접근법은 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 위치를 반영한 배정·교통, 편안함 지표로 나눌 수 있다. [의견][^ref-1075][^ref-1077][^ref-031][^ref-1083][^ref-1085]

이전 분리 페이지 [49. 사람 근접 안전 — 대표 접근법과 기술(2026-09-30)](2026-09-30-area49-s6.md)에 이 절의 기존 검증 내용이 있다. 그 이전 분리 페이지의 Farrell·HATA·Jafari 문장에 남은 '정량 결과 미확인'·'실험 장소·참가자 수 미확인' 표기는 아래 내용과 원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 5절의 내용으로 대신한다.

### 보호 필드와 감지 응답시간(연계 대상)

안전 레이저 스캐너 제조사 SICK 의 기술 블로그(2021-02-09)는 감시 케이스(보호 필드 집합)를 바꾸면 시스템 응답시간이 늘고, 다중 샘플링 값을 올리면 물체가 연속해서 여러 번 감지돼야 출력이 꺼지므로 응답시간 보정분이 더해진다고 설명한다. [추정] 벤더 주장[^ref-1466] 이는 제조사의 일반 설명이며 특정 센서·하중·바닥 조건의 시험값이 아니다. 구축자 의견으로는, 보호 필드와 응답시간 설정은 로봇 자체 안전 기능이므로 ROP 에는 연계 대상으로 두어야 한다(원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 9절). [의견][^ref-1466]

### 플릿 수준 구역·속도 제한

VDA 5050 3.0.0 은 로봇마다 처리할 수 있는 구역 유형이 다르므로, 각 로봇이 이해하는 구역 이름을 팩트시트의 supportedZones 목록으로 플릿 관제에 보고하도록 요구한다. [사실][^ref-031] 이는 모든 기종이 모든 구역 유형을 지원한다는 뜻이 아니다. 같은 명세의 외곽 기준 구역에서는 적재물을 포함한 로봇 외곽이 진입·이탈을 정하며, 외곽 일부라도 구역에 들어가면 진입이고 외곽이 모두 빠져나가야 이탈이다. [사실][^ref-031] 구축자 의견으로는, ROP 가 구역 속도 제한을 등록할 때 로봇별 supportedZones 신고를 먼저 확인하고, 적재물로 커진 외곽이 경계에 닿기 전에 감속을 마치도록 감속 시작 지점을 경계 앞에 두며, 실제 감속을 통합 시험으로 확인해야 한다(감속 거리·시간 값은 로봇 제조사 자료로 정한다). [의견][^ref-031]

### 로봇 측 감속·정지 계층과 '0' 값의 의미

로봇 측 로컬 회피 계층인 Nav2(Jazzy) Collision Monitor 는 source_timeout(기본 2.0초) 안에 새 센서 데이터가 오지 않으면 로봇을 세우고, 이 값을 0.0 으로 두면 그 차단 동작이 꺼진다. [사실][^ref-1467] Nav2 Speed Filter 에서 속도 제한 메시지 값 0 은 정지가 아니라 '속도 제한 없음'을 뜻하며, 백분율·절댓값 설정과 관계없다. [사실][^ref-1468] 두 기능은 로봇 쪽 연계 대상이다. Open-RMF 플릿 어댑터(rmf_fleet_adapter 2.14.0)의 차선 속도 제한 함수 limit_lane_speeds 는 요청 속도가 0 이하이거나 차선 번호가 그래프 범위를 벗어나면 경고만 남기고 그 요청을 건너뛰며, 0 이하일 때의 경고문은 차선을 닫으려면 [차선 폐쇄](../../glossary/lane-closure.md) API(close_lanes)를 쓰라고 안내한다. [사실][^ref-1464] 유효한 제한은 계획 그래프의 차선 속성에 기록돼 새 계획기와 작업 파라미터에 반영되고 차선 상태를 발행하는 데서 끝나며, 차량이 실제로 감속을 마쳤는지 확인하는 경로는 이 함수에 없다. [사실][^ref-1464]

세 시스템 모두 '0' 이 정지를 뜻하지 않으므로, 이종 플릿 어댑터가 '0' 을 정지 명령으로 그대로 옮기면 의도와 반대로 제한이 풀리거나 무시될 수 있는 것으로 보인다(실제 오류 사례나 실행 시험 자료는 확인하지 못했다). [추정][^ref-1467][^ref-1468][^ref-1464] 구축자 의견으로는, ROP 어댑터 계약이 '제한 없음'·'양수 속도 제한'·'통로 폐쇄'·'보호 정지'를 서로 다른 명령으로 표현하고, 구역 전송·활성화·계획 반영·차량 감속 관측을 별개 상태로 기록해 계획 상태 갱신만으로 감속 완료를 보고하지 않아야 한다. [의견][^ref-1464][^ref-1468][^ref-031]

### 사람 인지형 배정의 평가 조건

HATA(Kazemi Eskeri 외, IROS 2025)의 5·10·15대 플릿 평가는 실제 기록된 사람 궤적을 재생하는 시뮬레이션 환경에서 수행됐다. [사실][^ref-1083] 이 논문의 실패율은 교착 또는 10분 제한시간 초과로 완료하지 못한 과제의 비율로, 사고율이나 사람과의 충돌률이 아니다. [사실][^ref-1083] 따라서 이전 분리 페이지(2026-09-30)에 적은 임무 완료 시간 단축 결과는 안전 지표가 아니라 효율 지표로 읽어야 할 것으로 보인다. [추정][^ref-1083]

### 편안함 지표의 실험 조건

Jafari·Nguyen·Liu 의 보행자 편안함 실험은 23~41세 자원자 32명(남 22·여 10)이 폭 3.2 m 복도에서 1.4·2.8 m/s 로 움직이는 원격조종 로봇을 만나는 조건이었고, 160회 시행 중 데이터 수집이 완전히 실패한 2회를 뺐다(측면 거리 분석에서는 13회를 더 뺐다). [사실][^ref-1085] 복합 예측기는 분석에 쓴 같은 데이터로 평가돼 독립 시험 집합에서의 성능이 아니다. [사실][^ref-1085] 논문의 오즈비 3.67 은 예측기가 '편안함'으로 예측했을 때 실제로 편안했을 오즈가 그렇지 않게 예측했을 때보다 3.67배라는 뜻으로, 사고 감소 확률이나 안전 거리 기준이 아니다. [사실][^ref-1085]

### 재생 시험용 데이터셋

NavWareSet 프로젝트는 통제된 실내 수집 실험에 참가자 17명이 참여해 5명씩 2개 그룹과 5개 쌍으로 나뉘었다고 설명한다(연결 논문 IJRR 2026, 온라인 2026-05-24). [사실][^ref-1475] 시나리오에는 시야가 가려진 모퉁이에서 로봇과 사람이 마주치는 BLIND CORNER 가 있으나, 이는 시나리오의 존재일 뿐 검출 실패율의 실증 결과가 아니다. [사실][^ref-1475] 구축자 의견으로는, 사람 근접 감속·정지 정책의 재생 시험에 가려진 모퉁이·통로 점유·혼잡 장면을 넣고, 아동·보행 보조기·휠체어 사용자처럼 감지 특성이 다른 보행자를 따로 평가해야 하며, 기존 데이터셋만으로 취약 보행자 범위가 충족됐다고 보면 안 된다. [의견][^ref-1475][^ref-1085]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-10-11
[^ref-1077]: Open Navigation (ros-navigation/navigation2), nav2_collision_monitor — README, 미확인, https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md, 접근일 2026-09-30
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-11
[^ref-1085]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-10-11
[^ref-1464]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
[^ref-1466]: SICK (Martin Kidman), The perfect size of the protective field on an industrial autonomous vehicle, 2021-02-09, https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle, 접근일 2026-10-11
[^ref-1467]: Open Navigation (Nav2 documentation, Jazzy), Collision Monitor Node — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/, 접근일 2026-10-11
[^ref-1468]: Open Navigation (Nav2 documentation, Jazzy), Speed Filter Parameters — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/, 접근일 2026-10-11
[^ref-1475]: Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트), NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트), 2026-05-24, https://anr-navware.github.io/navwareset/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-05 | 49. 사람 근접 안전 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-11-05/pages/topics/2026/2026-10-11-area49-s7.md

```markdown
---
title: "49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1076, ref-1084, ref-1464, ref-1467, ref-1468, ref-1469, ref-1470, ref-1471, ref-1472, ref-1473, ref-1474, ref-470, ref-980]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#7
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스

# 49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1084][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)에서 다룬다.
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 근접 안전과 관련된 표준·인증은 협동로봇, 무인 산업용 트럭, 산업용 이동 로봇, 실외 이동 로봇처럼 적용 유형별로 나뉘어 구역·속도·감지·정지를 정한다. [추정][^ref-1076][^ref-470][^ref-1084][^ref-980] 이 절은 사람 근접 안전과 관련된 항목만 요약하며, 표준·인증의 상세는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)에서 다룬다.

이전 분리 페이지 [49. 사람 근접 안전 — 관련 표준·프레임워크·오픈소스(2026-09-30)](2026-09-30-area49-s7.md)에 이 절의 기존 검증 내용(표준·인증 표)이 있다. 2026-10-11 갱신에서 더하거나 원조문 근거를 보강한 항목은 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| 지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의4·제7조의5 | 프레임워크 | 운행안전인증 기준으로 적재물 포함 최대 질량 500 kg 이하·최대 속도 시속 15 km 이하를 정하고 세부사항을 고시에 맡기며, 신청 때 횡단보도 통행방식과 통신장애·사고발생·혼잡상황 대응 시나리오를 담은 운행계획서를 내게 한다(2025-10-01 시행본). [사실][^ref-1470] | 국가법령정보센터[^ref-1470] |
| 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 별표 3 | 평가 프로그램 | 2025-11-24 일부개정·시행된 현행 고시이며, 별표 3 의 상위 항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개이고 질량별 최대 운행 속도(5·10·15 km/h)를 정한다. [사실][^ref-1469] 보호구역 5 km/h 와 사람·장애물 감지 시 감속·정지·회피(평가는 KS B 7320 의 장애물 감지와 회피 절)는 별표 3 원문 기준(검증 재확인 못 함, 기준일 2026-10-11)이다. [추정][^ref-1469] | 국가법령정보센터[^ref-1469] |
| ISO 13482:2014 개인 돌봄 로봇 안전 요구사항 | 표준 | 2014-02-03 발행, 2026-10-11 기준 단계 90.92(개정 예정)의 발행 표준이다(ISO 목록을 제공하는 세르비아 표준원 기준, 본문 미열람). [사실][^ref-1471] | ISS[^ref-1471] |
| ISO 10218-1:2025 산업용 로봇 안전 — 제1부 | 표준 | 2025-02-05 발행본의 적용 범위는 로봇·매니퓰레이터가 무인 산업용 트럭이나 이동 플랫폼에 고정되거나 그 일부일 때의 이동성 위험을 다루지 않는다고 적는다(본문 미열람). [사실][^ref-1472] 이것이 이동 매니퓰레이터 전체가 표준 밖이라는 뜻은 아닌 것으로 보인다. [추정][^ref-1472] | ISS[^ref-1472] |
| KS B 8252 실내 이동로봇의 보호정지 시험방법 | 표준 | 안전한 실내 공간에서 자율 주행 중 정적 장애물에 대한 보호정지를 평가하는 시험방법 표준으로 ISO 13482 를 기반으로 하며, 2020-02-26 제정·2025-09-05 확인됐다(본문 미열람). [사실][^ref-1473] | e-나라표준인증[^ref-1473] |
| Nav2 Collision Monitor (Jazzy) | 오픈소스 | source_timeout(기본 2.0초) 안에 센서 데이터가 없으면 로봇을 세우고, 0.0 이면 이 차단이 꺼진다. 로봇 측 연계 대상이다. [사실][^ref-1467] | Nav2 문서[^ref-1467] |
| Nav2 Speed Filter (Jazzy) | 오픈소스 | 속도 제한 메시지 값 0 은 '속도 제한 없음'을 뜻한다(원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 6절). [사실][^ref-1468] | Nav2 문서[^ref-1468] |
| Open-RMF rmf_fleet_adapter 2.14.0 | 오픈소스 | limit_lane_speeds 가 0 이하 속도 제한 요청을 무시하고, 유효한 제한은 계획 반영까지만 한다(원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 6절). [사실][^ref-1464] | 소스 코드[^ref-1464] |
| VDA 5050 3.0.0 | 표준 | supportedZones 보고 의무와 적재물 포함 외곽 기준 구역 진입·이탈을 정한다(원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 4·6절). [사실][^ref-031] | 명세[^ref-031] |
| human_detection_fusion | 오픈소스 | 사람 위치를 ROS4HRI 의 hri_msgs 형식으로 발행하는 ROS 2 패키지다(AGPL-3.0, 원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 9절). [사실][^ref-1474] | 소스 코드[^ref-1474] |

확인한 국내 실내 이동로봇 KS(KS B 8252)는 정적 장애물에 대한 보호정지 시험방법이어서, 움직이는 사람과의 속도·거리 기준값이나 병원·상업 시설·공동주택 실내 운행을 강제하는 기준은 이번에도 확인되지 않았다(KS·ISO 본문 미열람이라 확정하지 못함). [추정][^ref-1473][^ref-1471]

이전 분리 페이지(2026-09-30)의 실외 인증 행은 인증기관 페이지·기사 기준이며, 위 표의 시행규칙·고시 행이 원조문 근거를 더한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-09-30
[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30
[^ref-1464]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
[^ref-1467]: Open Navigation (Nav2 documentation, Jazzy), Collision Monitor Node — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/, 접근일 2026-10-11
[^ref-1468]: Open Navigation (Nav2 documentation, Jazzy), Speed Filter Parameters — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/, 접근일 2026-10-11
[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-11
[^ref-1470]: 법제처 국가법령정보센터, 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5, 2025-10-01, https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075, 접근일 2026-10-11
[^ref-1471]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots, 2014-02-03, https://iss.rs/en/project/show/iso:proj:53820, 접근일 2026-10-11
[^ref-1472]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO 10218-1:2025 Robotics — Safety requirements — Part 1: Industrial robots, 2025-02-05, https://iss.rs/en/project/show/iso:proj:73933, 접근일 2026-10-11
[^ref-1473]: 국가기술표준원 (e-나라표준인증), KS B 8252 실내 이동로봇의 보호정지 시험방법, 2020-02-26, https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503, 접근일 2026-10-11
[^ref-1474]: ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험, human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18), 2026-06-29, https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp, 접근일 2026-10-11
[^ref-470]: ISO (ISO/TC 110), ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023, https://www.iso.org/standard/83545.html, 접근일 2026-09-30 (원문 미열람)
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-05 | 49. 사람 근접 안전 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-11-05/pages/topics/2026/2026-10-11-area49-s11.md

```markdown
---
title: "49. 사람 근접 안전 — 열린 질문"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1080, ref-1083, ref-1464, ref-1466, ref-1467, ref-1468, ref-1469, ref-1471, ref-1473, ref-1474, ref-1475, ref-980]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#11
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 열린 질문

# 49. 사람 근접 안전 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 열린 질문은 플릿 구역 제한의 안전 인정 조건, 실외 인증 심사 항목 수의 출처 충돌, 국내 실내 사람 근접 기준, 이종 플릿 공통 감속·정지 인터페이스이며, 2026-10-11 실행은 네 질문 모두 부분 근거만 더했고 해결하지 못했다. [의견][^ref-031][^ref-1469]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 열린 질문은 플릿 구역 제한의 안전 인정 조건, 실외 인증 심사 항목 수의 출처 충돌, 국내 실내 사람 근접 기준, 이종 플릿 공통 감속·정지 인터페이스이며, 2026-10-11 실행은 네 질문 모두 부분 근거만 더했고 해결하지 못했다. [의견][^ref-031][^ref-1469]

- **oq-229** (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-10) 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? 부분 근거(2026-10-11): 확인한 명세·코드는 구역 제한의 지원 신고(supportedZones)·적재 외곽 기준 진입 판정·계획 계층 속도 반영까지만 다루고, 위험 감소 조치로 인정하는 조건이나 보호 필드 설정과의 정합을 누가 검증하는지는 다루지 않는다. [추정][^ref-031][^ref-1464][^ref-1467]
- **oq-230** (상태: 열림) 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? 부분 근거(2026-10-11): 현행 고시 별표 3 의 상위 항목 8개와 인증기관 페이지의 8개 항목 이름은 같다. [사실][^ref-1469][^ref-980] 기사의 16가지가 어느 판·계층에 대응하는지와 개정 시점은 미확인이다.
- **oq-231** (상태: 열림) 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? 부분 근거(2026-10-11): 확인한 KS B 8252 는 정적 장애물 보호정지 시험방법이어서, 움직이는 사람과의 속도·거리 기준값은 확인되지 않았다(표준 본문 미열람). [추정][^ref-1473][^ref-1471]
- **oq-232** (상태: 열림) 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? 부분 근거(2026-10-11): 확인한 자료 범위에서 공통 안전 인터페이스는 없고, 기업 단독 사례(아마존 조끼, 벤더 주장)와 사람 위치 발행 형식만 정한 공개 구현(human_detection_fusion)이 따로 있는 것으로 보인다. [추정][^ref-1080][^ref-1474]
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-05) 로봇별 반응 시간·제동 거리·적재 하중·센서 오차가 펌웨어 변경이나 운용 조건 변화로 바뀌었을 때, 로봇 측 보호 필드와 ROP 의 구역 속도 제한·감속 시작 지점을 함께 다시 검증하는 절차나 공개 사례가 있는가?[^ref-1466]
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-05) Nav2 의 속도 제한 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 같은 서로 다른 '0' 의미를 이종 플릿 어댑터가 올바르게 변환하는지 실행 시험으로 확인한 공개 자료나 적합성 시험 항목이 있는가?[^ref-1467][^ref-1468][^ref-1464]
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-05) HATA 의 임무 완료 시간 최대 26%·19% 단축을 다시 계산할 수 있도록 실험별 분모, 교착·타임아웃 실패 시행의 처리 방식, 고정된 실행 코드가 공개돼 있는가?[^ref-1083]
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-05) 아동·휠체어 사용자·보행 보조기 사용자·시각장애인이 가려진 모퉁이나 통로 점유 상황에서 로봇을 만날 때의 감지 누락·양보 결과를 독립적으로 측정한 데이터셋이나 시험 결과가 있는가?[^ref-1475]

이전 분리 페이지 [49. 사람 근접 안전 — 열린 질문(2026-09-30)](2026-09-30-area49-s11.md)에 기존 열린 질문 설명이 있고, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1080]: Amazon, Ever wonder how people and robots team up on your Amazon order?, 2019-04-06, https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order, 접근일 2026-10-11
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-11
[^ref-1464]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp, 미확인, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp, 접근일 2026-10-11
[^ref-1466]: SICK (Martin Kidman), The perfect size of the protective field on an industrial autonomous vehicle, 2021-02-09, https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle, 접근일 2026-10-11
[^ref-1467]: Open Navigation (Nav2 documentation, Jazzy), Collision Monitor Node — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/, 접근일 2026-10-11
[^ref-1468]: Open Navigation (Nav2 documentation, Jazzy), Speed Filter Parameters — Nav2 Docs (Jazzy), 미확인, https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/, 접근일 2026-10-11
[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-11
[^ref-1471]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots, 2014-02-03, https://iss.rs/en/project/show/iso:proj:53820, 접근일 2026-10-11
[^ref-1473]: 국가기술표준원 (e-나라표준인증), KS B 8252 실내 이동로봇의 보호정지 시험방법, 2020-02-26, https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503, 접근일 2026-10-11
[^ref-1474]: ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험, human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18), 2026-06-29, https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp, 접근일 2026-10-11
[^ref-1475]: Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트), NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트), 2026-05-24, https://anr-navware.github.io/navwareset/, 접근일 2026-10-11
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-05 | 49. 사람 근접 안전 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-11-05/pages/topics/2026/2026-10-11-area49-s8.md

```markdown
---
title: "49. 사람 근접 안전 — 대표 연구와 자료"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1075, ref-1081, ref-1082, ref-1083, ref-1085, ref-1475, ref-869]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#8
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 대표 연구와 자료

# 49. 사람 근접 안전 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 근접 안전의 대표 연구는 분리 거리 계산(NIST), 창고·병원 주행 평가, 사람 인지형 배정, 보행자 편안함, 사회적 주행 데이터셋으로 나뉘며, 각 연구의 평가 조건(실물·모의 공간·시뮬레이션)을 함께 읽어야 한다. [의견][^ref-1075][^ref-1081][^ref-1083]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 근접 안전의 대표 연구는 분리 거리 계산(NIST), 창고·병원 주행 평가, 사람 인지형 배정, 보행자 편안함, 사회적 주행 데이터셋으로 나뉘며, 각 연구의 평가 조건(실물·모의 공간·시뮬레이션)을 함께 읽어야 한다. [의견][^ref-1075][^ref-1081][^ref-1083]

이전 분리 페이지 [49. 사람 근접 안전 — 대표 연구와 자료(2026-09-30)](2026-09-30-area49-s8.md)에 이 절의 기존 목록이 있다. 아래는 2026-10-11 갱신에서 서지와 평가 조건을 바로잡은 목록이다.

- Marvel·Norcross(NIST), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells(Robotics and Computer-Integrated Manufacturing 44권, 2017년 4월호, 144–155쪽, 온라인 게재 2016-08-27) — SSM 의 보호 분리 거리를 구성요소별로 나누고 NIST 시험 결과와 구현 한계(방향 무시에 따른 불필요한 정지, 센서 잡음, 갱신 주기)를 제시했다. [사실][^ref-1075]
- Farrell 외, Safe Human Robot Navigation in Warehouse Scenario(arXiv 2025-03-27) — 학습 기반 CBF 를 Open-RMF 에 통합하고 Freight·Jackal·Megarover 실물 로봇과 OptiTrack 으로 실험했다. [사실][^ref-1082] 출판판은 2025 IEEE CASE(2025-08-17, DOI 10.1109/CASE58245.2025.11164151, 쪽수 미확인)인 것으로 보인다. [추정][^ref-1082]
- Rondoni 외, Navigation benchmarking for autonomous mobile robots in hospital environment(Scientific Reports, 2024-08-07) — 실제 병원 배치를 재현한 모의 병원 공간에서 HOSBOT·TIAGo 실물 로봇을 비교했고, 이동 장애물은 원격조종 로봇이었다. [사실][^ref-1081]
- Valner 외(University of Tartu), Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test(Frontiers in Robotics and AI, 2022-08-23) — 이종 다로봇 관리는 시험 환경에서 검증했고 병원 안 복수 배송 로봇 운용은 향후 과제로 남겼다. [사실][^ref-869]
- Kazemi Eskeri 외, Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments(arXiv 2025-08-27, IROS 2025, 쪽수 미확인) — 사람 궤적 재생 시뮬레이션으로 평가했고, 실패율은 교착·시간 초과 기준이다. [사실][^ref-1083]
- Jafari·Nguyen·Liu, Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters(arXiv 2026-04-15, arXiv 표지 기준 ICRA 2026 채택 저자판, 발표 쪽수·DOI 미확인) — 자원자 32명·원격조종 로봇 실험이며 예측기는 같은 데이터로 평가했다. [사실][^ref-1085]
- Brayan 외(NavWare 프로젝트), NavWareSet(IJRR 2026, 온라인 2026-05-24, 권호 임시) — 참가자 17명과 BLIND CORNER 등 시나리오를 담은 실내 사회적 주행 데이터셋이다. [사실][^ref-1475]

그 이전 분리 페이지(2026-09-30)의 프리프린트 기준 서지와 복수형 병원 논문 제목은 위 서지로 대신한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-10-11
[^ref-1081]: Rondoni 외 (Scientific Reports), Navigation benchmarking for autonomous mobile robots in hospital environment, 2024-08-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/, 접근일 2026-10-11
[^ref-1082]: Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE), Safe Human Robot Navigation in Warehouse Scenario, 2025-03-27, https://arxiv.org/abs/2503.21141, 접근일 2026-10-11
[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-11
[^ref-1085]: Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택), Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters, 2026-04-15, https://arxiv.org/abs/2604.13677, 접근일 2026-10-11
[^ref-1475]: Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트), NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트), 2026-05-24, https://anr-navware.github.io/navwareset/, 접근일 2026-10-11
[^ref-869]: Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI, Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test, 2022-08-23, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-05 | 49. 사람 근접 안전 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-11-05/pages/topics/2026/2026-10-11-area49-s4.md

```markdown
---
title: "49. 사람 근접 안전 — 핵심 개념과 용어"
type: topic
category: "M. 안전"
primary_area_no: 49
related_areas: [16, 19, 20, 21, 25, 27, 31, 46, 48, 50, 54, 59, 60, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1075]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/human-proximity-safety.md#4
---

[홈](../../index.md) › [주제](../index.md) › 49. 사람 근접 안전 — 핵심 개념과 용어

# 49. 사람 근접 안전 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 근접 안전의 핵심 개념은 사람과 지켜야 할 분리 거리를 계산하는 방식과, 그 거리를 지키도록 플릿 관제가 내리는 구역·속도 제한을 표현하는 방식이다. [의견][^ref-1075][^ref-031]
- 이 페이지는 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 근접 안전의 핵심 개념은 사람과 지켜야 할 분리 거리를 계산하는 방식과, 그 거리를 지키도록 플릿 관제가 내리는 구역·속도 제한을 표현하는 방식이다. [의견][^ref-1075][^ref-031]

- **속도·분리 감시(Speed and Separation Monitoring, SSM)** — 협동로봇 기술 시방서 ISO/TS 15066 의 방식으로, 로봇과 사람의 분리 거리가 [보호 분리 거리](../../glossary/protective-separation-distance.md) 이하가 되면 안전 감시 정지를 건다. [사실][^ref-1075] 근거 논문(Marvel·Norcross, NIST)은 Robotics and Computer-Integrated Manufacturing 44권(2017년 4월호) 144–155쪽에 실렸고, 온라인 게재일은 2016-08-27 이다. [사실][^ref-1075]
- **구역 지원 신고(supportedZones)** — VDA 5050 3.0.0 에서 로봇이 이해할 수 있는 구역 유형의 이름을 [팩트시트](../../glossary/vda-5050-factsheet.md)로 플릿 관제에 알리는 항목이다. [사실][^ref-031]
- **외곽 기준 구역(contour-based zone)** — 같은 명세에서 적재물을 포함한 로봇 외곽으로 구역 진입·이탈을 판정하는 구역 방식이다. [사실][^ref-031]

이전 분리 페이지 [49. 사람 근접 안전 — 핵심 개념과 용어(2026-09-30)](2026-09-30-area49-s4.md)에 이 절의 기존 검증 내용이 있다. 그 이전 분리 페이지의 '2016년 논문' 표기는 위 서지(2017년 4월호, 온라인 게재 2016-08-27)로 읽는다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/human-proximity-safety.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/human-proximity-safety.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050/VDA5050), VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1075]: Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing), Implementing Speed and Separation Monitoring in Collaborative Robot Workcells, 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-05 | 49. 사람 근접 안전 의 "핵심 개념과 용어" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1465건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | https://www.iso.org/standard/83545.html | 2026-09-25 | 아니오 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 2026-09-30 | 예 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | https://zdnet.co.kr/view/?no=20230728173101 | 2026-09-30 | 예 |
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 2026-09-30 | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | https://arxiv.org/abs/2602.17822 | 2026-09-30 | 예 |
| ref-1077 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md | 2026-09-30 | 예 |
| ref-1078 | 지디넷코리아 | "협동로봇 충돌 안전 계산하고 써야죠" | 2024-03-09 | https://zdnet.co.kr/view/?no=20240305160245 | 2026-09-30 | 예 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | https://arxiv.org/abs/2306.16740 | 2026-09-30 | 예 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 2026-09-30 | 예 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 2026-09-30 | 예 |
| ref-1082 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | https://arxiv.org/abs/2503.21141 | 2026-09-30 | 예 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | https://arxiv.org/abs/2508.19731 | 2026-09-30 | 예 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 2026-09-30 | 예 |
| ref-1085 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | https://arxiv.org/abs/2604.13677 | 2026-09-30 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [49] 에 걸린 4건 / 전체 384건)

```markdown
- oq-229 [열림] 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? (영역 49, 48)
- oq-230 [열림] 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (영역 49, 50)
- oq-231 [열림] 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (영역 49, 59)
- oq-232 [열림] 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (영역 49, 21)
```

### runs/2026-10-11-05/verification2.json

```json
{
  "run_id": "2026-10-11-05",
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
    "ok": false,
    "overlaps": [
      "ref-1464(이번 실행)와 ref-1529(실행 2026-10-11-04)가 같은 URL(rmf_ros2 2.14.0 FleetUpdateHandle.cpp)을 가리킨다. 퍼블리셔가 같은 URL을 병합해야 하며, 병합 뒤 남는 id가 이 페이지와 분리 페이지(s6·s7·s11)의 각주 id와 같은지 확인이 필요하다.",
      "이전 분리 페이지 docs/topics/2026/2026-09-30-area49-s4.md·s6.md·s8.md에는 고치지 않은 표기('2016년 논문', Farrell '정량 결과 미확인', Jafari '실험 장소·참가자 수 미확인', Rondoni 복수형 제목·'모의 병원 환경')가 남아 있어 이번 갱신본과 서로 다르다. 스토리텔러가 additional_research_requests로 넘겼다.",
      "docs/categories/safety/index.md 125·187행의 Rondoni 연구 '시뮬레이션 평가' 표현이 이번 5절 정정과 어긋난다(후속 정리 항목으로 기록됨)."
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
    "9절(human-proximity-safety.md) 문장 '사람 위치를 플릿 감속·정지에 잇는 공개 구현으로는 ROS 2 패키지 human_detection_fusion 이 있다.'를 '사람 위치를 발행하는 공개 구현으로는 ROS 2 패키지 human_detection_fusion 이 있으며, 확인한 코드는 위치 발행까지만 다루고 플릿 감속·정지 명령이나 차량 감속 확인은 다루지 않는다. [추정][^ref-1474]'처럼 고친다. 근거는 f40·f45이며, 지금 문장은 태그가 없고 브리프 범위를 넘는다. f45 note대로 공개 구현은 위치 발행까지이고 감속 확인(ACK)·안전 등급은 다루지 않는다.",
    "9절 문장 '사람 검출·추적은 로봇 자체 지능·제어 경계의 연계 대상이고, ROP 몫은 그 위치를 받아 감속·정지로 잇는 인터페이스다.'와 6절(분리 페이지 2026-10-11-area49-s6) 문장 '보호 필드와 응답시간 설정은 로봇 자체 안전 기능으로 ROP 에는 연계 대상이다(9절).'에 태그를 붙인다. [의견]과 '구축자 의견'을 쓰거나, 뒤따르는 구축자 의견 문장에 합친다. 두 문장 모두 태그 없는 주장 문장이다.",
    "4·6·7·8절 패치 본문을 고친다. 자동 분리 결과(2026-10-11-area49-s4·s6·s7·s8)에서 '그 페이지의 …' 문장이 가리킬 대상 링크가 사라졌고, 이 때문에 이전 분리 페이지(2026-09-30-area49-s4·s6·s7·s8)의 검증된 기존 내용(NIST 반응시간·ZR·ZS, 운용 구역, VDA 5050 maximumSpeed·zoneSet 규칙, ISO/TS 15066·ISO 3691-4·R15.08 행, HATA 26%·19% 등)이 세부영역 페이지와 새 분리 페이지 어디서도 닿지 않는다. 각 절 본문에 '이전 분리 페이지 [49. 사람 근접 안전 — <절 이름>(2026-09-30)](../../topics/2026/2026-09-30-area49-s<n>.md)'처럼 명시 링크를 넣고 '그 페이지'를 이 링크로 바꾼다. 이 경로는 세부영역 페이지와 주제 페이지 양쪽 깊이에서 같게 풀린다. 분리 뒤에도 링크가 남았는지 확인한다.",
    "분리될 4·6·7·8절 본문의 맨 절 번호 참조('아래와 5절의 내용', '(6절)', '(4·6절)', '(9절)')를 '원 페이지 [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) n절'처럼 고친다. 주제 페이지로 옮겨지면 같은 번호가 주제 페이지 자신의 5절(ROP 관점의 시사점)·6절(연결되는 연구영역)·9절(검증 노트)을 가리키게 되어 독자를 오도한다.",
    "5절 실외 사례 제약 칸 첫 문장('최고 속도 15 km/h 이하·최대 질량 500 kg 이하이며, 시행규칙 제7조의4 …')의 각주에 기존 [^ref-992]를 되살린다. 1차 판정(중복 항목)은 새 각주를 더하되 기존 각주를 지우지 않도록 했는데, 기존 문장의 [^ref-980][^ref-992] 가운데 ref-992가 빠졌다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 46건, 미확인 4건, 교차 확인 0건. 강등: f30·f31·f32·f33 사실 → 추정. 현행 실외이동로봇 운행안전인증 고시 별표 3의 보호구역 5 km/h, 주변 인식 감속·정지·회피, 횡단보도 통신 단절 처리, 보행자 밀집 알림이 대상이며, 별표 PDF 텍스트를 검증에서 추출하지 못해 문구를 대조하지 못했다. 원문 미열람 출처: ref-992(이번 미열람). 검증 열람 일부 실패: ref-1466(SICK 블로그, 검색 결과로 실재만 확인), ref-1469(별표 3 본문 미대조, 고시 번호·개정일·시행일만 확인), ref-1075(NIST PDF 텍스트 미추출, PMC 판으로 서지 확인), ref-1080(메타데이터 발행일 재확인 못 함). 주의: 모든 [사실] 주장이 단일 출처이거나 같은 제도·저장소 계열이라 독립 교차 확인이 없다. 고시·시행규칙·인증기관은 같은 운행안전인증 체계에 속한다. VDA 5050·Nav2·Open-RMF의 구역·속도 제한은 안전 기능이 아니라 계획·로컬 회피 계층이다. Farrell 표 IV의 로봇 대수는 열 이름에서 읽은 것이다. HATA 실패율은 사고율이 아니며, Jafari의 오즈비 3.67은 같은 데이터로 평가한 값이다. 열린 질문 oq-229~oq-232는 부분 근거만 있어 열림을 유지한다. 정정 요청 없음. 같은 URL이 ref-1464(이번)와 ref-1529(실행 2026-10-11-04)로 등록돼 퍼블리셔 병합이 필요하다. 1차 검증 검색 6회 사용. / 2차 수정 후 재검증. 드리프트 1건: 9절에서 human_detection_fusion을 '플릿 감속·정지에 잇는 공개 구현'으로 과장한 태그 없는 문장. 태그 없는 범위 문장 2건. 1차 수정 지시 15항은 모두 이행됐다(강등·벤더 주장·구축자 의견·서지·각주·인용 재서술·열린 질문 확인). [분류원문] 보존, 섹션 순서 준수. 자동 분리 페이지 s4·s6·s7·s8에서 이전 분리 페이지(2026-09-30) 링크가 빠져 기존 검증 내용에 닿지 않고 '그 페이지'·절 번호 참조가 모호하다. 실외 제약 칸에서 기존 각주 ref-992가 빠졌다. 참고: 세부영역 프런트매터 sources의 ref-1471·ref-1472·ref-1473·ref-1475는 분리 뒤 세부영역 본문에서 인용되지 않고 분리 페이지에서만 인용된다. 형식 검증 통과 항목이라 수정 지시하지 않는다. 2차에서는 검색·열람을 쓰지 않았다.",
  "retry_reason": null
}
```
