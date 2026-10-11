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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### docs/categories/safety/safety-and-risk-management.md (요약)

```markdown
# 48. 안전·위험 관리

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 4

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
```

### docs/categories/safety/safety-standards-certification-and-incident-investigation.md (요약)

```markdown
# 50. 안전 표준·인증·사고 조사

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
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

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (요약)

```markdown
# 19. 사람·보행자 모델

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

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

### docs/categories/execution-collaboration-and-recovery/human-robot-collaboration.md (요약)

```markdown
# 31. 사람–로봇 협업

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

사람과의 작업 분담, 수동 개입·원격 조작, 주변 사람과의 소통 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람–로봇 작업 분담**: 사람과 로봇이 서로 기다리지 않도록 일을 나누고 작업자의 부담(인체공학)을 고려한다
- **수동 개입·원격 조작**: 운영자가 승인·수동 전환·원격 조작으로 로봇 작업에 개입한다
- **주변 사람과의 소통**: 로봇이 빛·소리·화면으로 의도를 알리고 주변 사람을 안내한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [옛 분류원문]

> 옛 질문: 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [옛 분류원문]

## 2. 핵심 질문

사람과 로봇이 같은 공간에서 서로 기다리거나 방해하지 않게 하려면? [분류원문]
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

### docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md (요약)

```markdown
# 59. 법·규제·보험·라이선스

소속 대분류: P. 거버넌스·법규·사회 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]
```

### docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md (요약)

```markdown
# 60. 노동·수용성·접근성

소속 대분류: P. 거버넌스·법규·사회 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]
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

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
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

### runs/2026-10-11-04/research.md

```markdown
# 리서치 브리프 2026-10-11-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-04 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 48. 안전·위험 관리 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가(분리 2026-09-25-area25-s3) — 국내 위험성평가 실시 주체(도급·수급)·근로자 참여·수시평가 조건 근거 없음
- 섹션 5. 적용 사례 — '출하 마감 전 화재경보' 제약 칸(107행)의 'RMF 비상 신호는 플릿을 구분하지 않는 불리언, 이후 구현 여부 미확인' 이 2.10.0 이후 상태와 맞지 않음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-25-area25-s6) — STPA 의 실제 분석 산출물(단계·위험한 제어 행동 유형), 근로자 참여 기록 방법, 감시와 대응의 구분이 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-25-area25-s7·2026-09-26-area25-s7) — R15.08 Part 3 '예정' 표현(2026-09-25-area25-s7.md 43행), ISO 3691-4 차기판 '제2판 초안' 표현(2026-09-26-area25-s7.md 46행), 이동식 협동로봇 KS '표준 번호 미확인'(같은 파일 46행 표)이 낡음
- 섹션 8. 대표 연구와 자료(분리 2026-09-25-area25-s8) — Bensaci 2020 Bowtie 결합 연구 없음, Belzile 사례 조건(현장·로봇)과 잔류 위험 추정 방식, SafeGate 평가 층위·분모 문제 미반영
- 섹션 9. 책임 경계 — 제조사 매뉴얼의 인터록·PL 책임 구분, EU 실질적 변경 정의의 조건 미반영
- 섹션 11. 열린 질문 — oq-064·oq-070·oq-093·oq-095·oq-096 부분 근거 미반영
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정 3건(f7·f10·f32)

## 조사 질문

1. 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
2. oq-070 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? (섹션 7·11 겨냥)
3. oq-064 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? (섹션 7·11 겨냥)
4. oq-096 여러 제조사 로봇이 섞인 현장에서 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (섹션 3·9·11 겨냥, 국내 고시 우선)
5. oq-095 ROP 의 원격·플릿 일괄 정지 지시 경로가 성능 수준(PL) 요구를 받는가? (섹션 9·11 겨냥)
6. oq-093 EU 기계 규정의 실질적 변경 판단이 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? (섹션 9·11 겨냥)
7. 바뀐 출처: R15.08 Part 3 발행, ISO 3691-4·ISO 12100 개정 단계, KS B ISO 3691-4 개정, Open-RMF 비상 신호 구현 상태는 무엇인가? (섹션 5·7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | STPA Handbook 은 STPA 분석을 분석 목적 정의, 제어 구조 모델링, 위험한 제어 행동(Unsafe Control Action) 식별, 손실 시나리오 식별의 네 단계로 제시한다. | ref-1520 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [사실] | STPA Handbook 은 위험한 제어 행동을 제어 행동을 제공하지 않음, 위험하게 제공함, 너무 이르거나 늦게·순서가 틀리게 제공함, 지속 제어를 너무 오래 끌거나 너무 일찍 멈춤의 네 유형으로 나눠 찾게 한다. | ref-1520 | 아니오 | medium | 2026-10-11 | — | — |
| f3 | [사실] | Bensaci 외(2020, Alexandria Engineering Journal)는 초록 기준으로 다중 로봇 시스템에 STPA 와 Bowtie 를 결합해, 서로 다른 계층형 조정 구조의 위험 시나리오와 요인을 STPA 로 도출한 뒤 Bowtie 로 평가하고 위험을 분류해 제어 구조 비교에 쓴다. | ref-1521 | 아니오 | medium | 2020-10 | — | — |
| f4 | [추정] | Bensaci 외(2020)의 분석 대상은 기존 2018년 연구(ref-564)와 같이 화학 분석실에서 화학제품을 운반하는 다중 로봇(메모 기준 11대) 시스템인 것으로 보이나, 본문을 열지 못해 로봇 대수와 사례 조건은 확인하지 못했다. | ref-1521 | 아니오 | low | 2020-10 | — | — |
| f5 | [사실] | Belzile 외의 사례 연구는 캐나다 몬트리올의 건설사 Pomerleau 건설 현장에 Clearpath Jackal 을 배치하려는(intended deployment) 상황을 대상으로 위험성평가를 수행한다. | ref-563 | 아니오 | medium | 2025-02-28 | 기타 / 수행 자원 | — |
| f6 | [사실] | Belzile 외의 잔류 위험지수는 실험으로 측정한 값이 아니라 제안한 완화 대책을 적용한다고 보고 다시 추정한 값이다. | ref-563 | 아니오 | medium | 2025-02-28 | 기타 / 예외·성과 | — |
| f7 | [추정] | 정정: 분리 페이지 2026-09-25-area25-s7.md 43행의 'R15.08-2 … 사용자 요구는 예정된 Part 3 이 맡는다' 는 표현은 낡았다. A3 판매 페이지는 ANSI/A3 R15.08-3-2026(Part 3: Use of IMR Applications)의 발행일을 2026-04-23 으로 표시하며, 이 내용은 위키에 이미 있다(ref-1255, safety/index.md 53행). | ref-1255 | 아니오 | medium | 2026-04-23 | — | 원문 미열람 |
| f8 | [추정] | 메모에 따르면 ISO 3691-4 차기판 프로젝트는 ISO/DIS 3691-4(Edition 3)로 2026-09-10 단계 40.60(DIS 투표 종료)에 있으나, 이번 대조에서 iso.org 가 403 이라 확인하지 못했고 위키 ref-789 는 같은 URL 을 2026-09-26 'ISO/CD 3691-4' 로 기록해 서로 충돌한다. | ref-789 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f9 | [추정] | 메모에 따르면 ISO 12100 개정 프로젝트(ISO/DIS 12100.3)는 2026-09-15 단계 40.60 에 있으나, iso.org 403 으로 확인하지 못했다. | ref-1522 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f10 | [추정] | 정정 제안: 2026-09-26-area25-s7.md 46행은 ISO 3691-4 차기판을 '제2판 초안' 이라 적었으나, ISO 3691-4 는 2020 판이 제1판, 2023 판이 제2판이므로 차기판은 제3판이라고 쓰는 것이 정합적으로 보인다(차기판의 개발 단계와 날짜는 미확인). | ref-470, ref-789 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f11 | [사실] | 국가표준 목록에서 KS B 7327 의 표제는 '산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항'이고, 발행일 2024-11-01, 국가기술표준원 고시 제2024-0480호로 제정됐으며 61쪽이다. 고시 사유는 모바일 로봇과 협동로봇이 결합된 로봇에 적용할 표준·인증이 없다는 것이다. | ref-1523 | 아니오 | medium | 2024-11-01 | — | — |
| f12 | [사실] | KS B 7327 목록의 적용범위는 통합 제조 시스템(IMS), 관제 시스템, 군집 관리 시스템, 기타 기계 설비류를 이 표준에서 다루지 않는다고 적는다. | ref-1523 | 아니오 | medium | 2024-11-01 | 제약 | — |
| f13 | [사실] | KS B 7327 목록은 국제표준 부합화 칸이 비어 있고, 인용표준으로 KS B ISO 10218-1·KS B ISO 10218-2·KS B ISO 3691-4·KS B ISO 12100·KS B ISO 13849-1 을 든다. | ref-1523 | 아니오 | medium | 2024-11-01 | — | — |
| f14 | [추정] | 중소벤처기업부가 2024-11-03 발표한 '이동식 협동로봇 안전기준 KS'(2024-11-01 부터 활용)는 발행일과 고시 사유가 일치하는 KS B 7327 인 것으로 보인다(oq-070 의 표준 번호 부분 답변). | ref-1523, ref-561 | 아니오 | low | 2026-10-11 | — | — |
| f15 | [추정] | KS B 7327 은 이동 머니퓰레이터 응용의 안전 요구를 다루므로 R15.08-2 유형 C(모바일 매니퓰레이터) 통합 요구에 대응하는 국내 KS 후보로 보이나, 부합화 칸이 비어 있고 관제·군집 관리 시스템을 범위에서 빼므로 R15.08-2 와의 동등성이나 플릿 통합 전체를 포괄하는지는 확인되지 않는다(oq-064 부분 답변). | ref-1523 | 아니오 | low | 2026-10-11 | — | — |
| f16 | [사실] | 국가표준 목록에서 KS B ISO 3691-4 는 2026-09-14 개정(국가기술표준원 고시 제2026-0288호)됐고, 국제표준 부합화를 ISO 3691-4:2023(IDT)로 표시하며 81쪽이다. 구판은 2021-11-30 판이다. | ref-1524 | 아니오 | medium | 2026-09-14 | — | — |
| f17 | [사실] | 현행 「사업장 위험성평가에 관한 지침」(고용노동부고시 제2024-76호, 2024-12-18 일부개정, 2025-01-02 시행) 제5조제2항은 작업의 일부 또는 전부를 도급하는 사업에서 도급사업주와 수급사업주가 각각 위험성평가를 실시하도록 한다. | ref-1525 | 아니오 | medium | 2025-01-02 | 수행 자원 | — |
| f18 | [사실] | 같은 지침 제6조는 위험성 수준 판단 기준 마련, 유해·위험요인 파악, 허용 가능 여부 결정, 감소대책 수립·실행, 감소대책 실행 여부 확인의 다섯 경우에 해당 작업에 종사하는 근로자를 참여시키도록 한다. | ref-1525 | 아니오 | medium | 2025-01-02 | — | — |
| f19 | [사실] | 같은 지침 제15조제2항은 건설물 설치·변경, 기계·기구·설비의 신규 도입 또는 변경, 정비·보수, 작업방법·절차의 신규 도입 또는 변경, 중대산업사고·산업재해 발생, 그 밖에 사업주가 필요하다고 판단한 경우로 추가적인 유해·위험요인이 생기면 수시 위험성평가를 하도록 한다. | ref-1525 | 아니오 | medium | 2025-01-02 | 시작 조건 | — |
| f20 | [사실] | 같은 지침 제15조제4항은 사업주가 매월 1회 이상 근로자 제안제도 활용·아차사고 확인·사업장 순회점검 등으로 유해·위험요인을 발굴해 위험성 결정과 감소대책을 수립·실행하는 등 상시적 위험성평가를 이행하면 제2항·제3항의 수시평가와 정기평가를 실시한 것으로 본다(간주 규정). | ref-1525 | 아니오 | medium | 2025-01-02 | — | — |
| f21 | [사실] | 고용노동부의 「위험성평가 근로자 참여 가이드」(2024-12)는 수급업체 근로자를 대상으로 청취조사를 해 아차사고 경험과 개선 의견을 모으는 방법을 제시한다. | ref-1527 | 아니오 | medium | 2024-12-31 | — | — |
| f22 | [사실] | 같은 가이드는 일용근로자 사례로 문자와 QR코드를 활용해 익명으로 위험 요인을 제안받는 방식을 소개한다. | ref-1527 | 아니오 | medium | 2024-12-31 | — | — |
| f23 | [사실] | 고용노동부(산재예방지원과)는 2026-09-23 「사업장 위험성평가에 관한 지침」 전부개정고시(안)을 행정예고했다. 이는 예고안이며 최종 고시·시행이 아니다. | ref-1526 | 아니오 | medium | 2026-09-23 | — | — |
| f24 | [추정] | 메모에 따르면 이 행정예고는 고용노동부 공고 제2026-461호이고 의견 제출 마감은 2026-10-13 이나, 이번 대조에서 공고 번호와 마감일은 확인하지 못했다. | ref-1526 | 아니오 | low | 2026-10-11 | — | — |
| f25 | [사실] | Monitoring ROS2 논문(Perez 외, EPTCS 371)은 관련 연구 절에서 DeRoS 와 비교하며, DeRoS 는 속성 위반을 어떻게 처리할지 지정하게 하지만 자기들의 방식은 위반의 탐지와 보고로 한정된다고 밝힌다. | ref-1530 | 아니오 | medium | 2022-09-28 | — | — |
| f26 | [추정] | OMRON LD Safety Guide(Rev H)는 플릿 안의 로봇들이 위치·크기·경로 계획 정보를 주고받아 장애물 회피에 쓰는 것을 충돌을 막는 인터록 방식으로 보지 않으며, 필요한 인터록은 사용자·통합자가 따로 갖춰야 한다고 설명한다. | ref-1528 | 아니오 | low | 2019-10 | 제약 | 벤더 주장 |
| f27 | [추정] | 같은 매뉴얼은 외부 비상정지 회로에 사용자가 공급한 부품이 포함될 때 그 부품을 포함한 전체 PL·PFH 계산과 최종 위험성평가를 사용자 책임으로 둔다. | ref-1528 | 아니오 | low | 2019-10 | 수행 자원 | 벤더 주장 |
| f28 | [추정] | Open-RMF issue #658(2025-04-04) 작성자는 두 건물에 로봇을 배치한 상황에서 한 건물의 화재경보가 모든 로봇을 주차시킨다는 문제를 보고한 것으로 보이나, 이번 재열람이 GitHub 403 으로 실패해 '두 건물' 같은 세부는 확인하지 못했다. | ref-567 | 아니오 | low | 2025-04-04 | 기타 / 시작 조건 | 원문 미열람 |
| f29 | [사실] | rmf_fleet_adapter 변경 이력(2.14.0 태그)은 2.10.0(2025-05-09) 절에 '플릿 이름으로 화재경보를 분리하는 선택지'를 추가한 #413 을 싣는다. | ref-1398 | 아니오 | medium | 2025-05-09 | — | — |
| f30 | [사실] | rmf_ros2 2.14.0 의 플릿 어댑터는 대상 비상 신호(EmergencySignal)의 fleet_names 가 비어 있거나 자기 플릿 이름을 포함할 때만 handle_emergency 에 is_emergency 값을 넘긴다. 즉 빈 목록은 모든 플릿에 적용된다. | ref-1529 | 아니오 | medium | 2026-10-11 | — | — |
| f31 | [사실] | 같은 2.14.0 코드에는 플릿을 가리지 않는 기존 불리언 비상 알림(EmergencyNotice) 구독 경로도 함께 남아 있다. | ref-1529 | 아니오 | medium | 2026-10-11 | — | — |
| f32 | [추정] | 정정 제안: 48영역 페이지 5절 '출하 마감 전 화재경보' 표의 제약 칸(107행) '비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었고, 이후 구현 여부는 미확인' 은, 2.10.0(2025-05-09)부터 플릿 이름으로 대상을 고르는 비상 신호가 추가됐고 2.14.0 에는 기존 불리언 경로와 대상 지정 경로가 함께 있다는 내용으로 고치는 것이 맞아 보인다. | ref-1398, ref-1529, ref-567 | 아니오 | low | 2026-10-11 | 물류창고 / 제약 | — |
| f33 | [사실] | EU 기계 규정 2023/1230 제3조(16)의 실질적 변경은, 제조자가 예견·계획하지 않은 물리적·디지털 변경이 새 위험요인을 만들거나 기존 위험을 키워 안전에 영향을 주고, 그 결과 (a) 기존 안전 제어 시스템의 변경이 필요한 방호장치·보호장치 추가 또는 (b) 안정성·기계적 강도를 보장할 추가 보호조치 채택이 필요할 때로 한정된다. | ref-555 | 아니오 | medium | 2026-07-27 | — | — |
| f34 | [사실] | 같은 규정 제54조는 일반 적용일을 2027-01-20 으로 두되, 제26~42조는 2024-01-20, 제50조(1)은 2026-10-20, 제6조(7)·제48조·제52조는 2023-07-19, 제6조(2)~(6)·(8)·(11)·제47조·제53조(3)은 2024-07-20 부터 적용한다. | ref-555 | 아니오 | medium | 2026-07-27 | — | — |
| f35 | [추정] | 제3조(16)이 디지털 변경을 포함하되 새 위험·기존 위험 증가와 (a)·(b) 조치 필요성을 함께 요구하므로, ROP 정책·어댑터 업데이트가 실질적 변경인지는 업데이트마다 그 조건을 따져야 하며 '디지털 변경이므로 모두 재인증 대상' 이라고 볼 수는 없어 보인다. 특정 업데이트의 법적 분류와 누가 제조자 의무를 지는지(제18조)는 이번 자료로 판단하지 않았다(oq-093·oq-282 부분 근거). | ref-555 | 아니오 | low | 2026-10-11 | — | — |
| f36 | [사실] | SafeGate 논문의 평가는 세 층위로 나뉜다. 230개 합성 로봇 작업 벤치마크는 실행 전 단계 1~3(위험 분석·결합·결정 게이트)을 평가하고, 30개 AI2-THOR 시나리오는 시뮬레이션 실행을 평가하며, 실물 로봇 실험은 §VI-C 에서 정성 결과로만 보고하고 단계 4~6(계약 컴파일·정적 계획 검증·실행 중 감시)을 시험한다. | ref-417 | 아니오 | medium | 2026-04-07 | — | — |
| f37 | [사실] | SafeGate 논문의 충돌률(CR) 식(9)은 분모를 실행된 작업 수(T_exec)로 두는데, §VI-B 는 30개 시나리오를 모두 차단한 경우의 CR 을 0% 로 보고해, 실행 0건일 때의 산정 규칙이 논문에 명시되지 않는다. | ref-417 | 아니오 | medium | 2026-04-07 | 예외·성과 | — |
| f38 | [사실] | SafeGate 논문 표 II 의 혼동행렬 합계는 183건(TP 100, FN 0, FP 6, TN 77)으로 전체 230개 벤치마크와 47건 차이가 난다. | ref-417 | 아니오 | medium | 2026-04-07 | — | — |
| f39 | [추정] | 표 II 의 183건과 230건의 차이는 결정 게이트가 판단을 미룬(ambiguous·defer) 작업을 혼동행렬에서 뺀 결과로 보이나, 논문이 47건 제외를 명시하지 않아 확정할 수 없다. | ref-417 | 아니오 | low | 2026-04-07 | — | — |
| f40 | [의견] | f1·f2 의 STPA 절차를 혼합 플릿에 쓰려면 제어 구조에 ROP·어댑터·로봇·설비·현장 운영자를 넣고, 정지 명령 누락뿐 아니라 잘못된 재개, 늦은 정지, 오래된 상태에 근거한 재배정을 위험한 제어 행동으로 등록해 손실→위험→제어 행동→안전 제약→시험으로 이어지는 연결표를 두는 방식이 필요해 보인다. | ref-1520 | 아니오 | low | 2026-10-11 | — | — |
| f41 | [추정] | 국내 지침은 도급·수급사업주가 각각 위험성평가를 하고 근로자를 참여시키게 하고(f17·f18), 제조사 매뉴얼은 시스템 통합 때 추가한 부품의 PL·PFH 계산과 최종 위험성평가를 사용자 몫으로 두므로(f27), 혼합 플릿 현장의 위험성평가는 현장 사업주(도급 구조에 따라 각각)가 주체가 되고 ROP 사업자·제조사·설비업체는 계약에 따라 자료와 분석을 제공하는 구조로 보이나, 실제 책임 배분은 현장의 법적 주체·계약에 따라 달라 확정되지 않는다(oq-096 부분 근거). | ref-1525, ref-1528 | 아니오 | low | 2026-10-11 | — | — |
| f42 | [추정] | VDA 5050 은 스스로 안전 표준이 아니라고 하고 activeEmergencyStop 의 REMOTE 는 비상정지 상태 보고 값일 뿐이며(기존 위키 내용), 제조사 매뉴얼은 플릿 정보 교환을 인터록으로 보지 않으므로(f26), ROP 의 원격·플릿 일괄 정지 지시 경로에 요구되는 PL 은 이들 문서로 정해지지 않고 기능별 위험성평가와 제조사 안전 인터페이스로 따로 정해야 하는 것으로 보인다(oq-095 부분 근거). | ref-031, ref-1528 | 아니오 | low | 2026-10-11 | — | — |
| f43 | [의견] | VDA 5050 의 startPause·stopPause 는 업무 일시정지·재개 명령이고 안전 기능 해제 절차가 아니므로, ROP 는 업무 pause 해제와 현장 안전정지 해제 승인을 별도 상태로 관리하고 제조사·설비의 해제 조건 충족을 확인하기 전에는 재개를 지시하지 않는 정책을 두는 것이 바람직하다. | ref-031 | 아니오 | low | 2026-10-11 | 물류창고 / 완료·인계 | — |
| f44 | [의견] | Nav2 Collision Monitor 는 하드 실시간 안전 인증을 제공하지 않고(기존 위키 내용) Ogma 생성 감시기는 위반의 탐지·보고로 한정되므로(f25), ROP 위험등록부에는 탐지 주체, 대응 결정자, 실제 정지 장치, 허용 지연, 감시 자체의 장애 시 대응을 따로 적어야 한다. | ref-1077, ref-1530 | 아니오 | low | 2026-10-11 | — | — |
| f45 | [의견] | RMF 의 대상 비상 신호에서 빈 fleet_names 가 전체 플릿을 뜻하므로(f30), 운영 화면은 빈 목록을 '전체 플릿' 으로 명확히 표시하고, 잘못된 플릿 선택·지연·중복 신호·재개 전 승인 조건을 시험 항목으로 두는 것이 필요하다. 화재 시 로봇의 이동·정지 정책은 현장 대피 계획과 함께 정해야 한다. | ref-1529 | 아니오 | low | 2026-10-11 | 물류창고 / 예외·성과 | — |
| f46 | [의견] | SafeGate 처럼 실행 전 차단과 실행 결과를 함께 보고하는 평가에서는 위험 작업 차단률과 실제 실행된 작업의 안전 결과를 서로 다른 분모로 공개하고, 실행되지 않은 작업을 안전하게 실행된 작업으로 세지 않아야 한다. | ref-417 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1520 | Leveson, N. G., Thomas, J. P. (MIT Partnership for Systems Approaches to Safety and Security) | STPA Handbook | 2018-03 | 정부·연구기관 | high | 2026-10-11 | https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf | 아니오 |
| ref-1521 | Bensaci, C., Zennir, Y., Pomorski, D., Innal, F., Liu, Y., Tolba, C. (Alexandria Engineering Journal) | STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison | 2020-10 | 논문 | medium | 2026-10-11 | https://doi.org/10.1016/j.aej.2020.06.036 | 아니오 |
| ref-1522 | ISO | ISO/DIS 12100.3 - Safety of machinery — General principles for design — Risk assessment and risk reduction | 미확인 | 표준 | medium | 2026-10-11 | https://www.iso.org/standard/88578.html | 예 |
| ref-1523 | 한국표준협회 KSSN(국가기술표준원 고시) | KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항 | 2024-11-01 | 표준 | high | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010149365 | 아니오 |
| ref-1524 | 한국표준협회 KSSN(국가기술표준원 고시) | KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템 | 2026-09-14 | 표준 | high | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010158178 | 아니오 |
| ref-1525 | 고용노동부(국가법령정보센터) | 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호) | 2024-12-18 | 정부·연구기관 | high | 2026-10-11 | https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202 | 아니오 |
| ref-1526 | 고용노동부(산재예방지원과) | 사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고 | 2026-09-23 | 정부·연구기관 | medium | 2026-10-11 | https://moel.go.kr/info/lawinfo/lawmaking/view.do?bbs_seq=20260900747 | 아니오 |
| ref-1527 | 고용노동부 | 위험성평가 근로자 참여 가이드 | 2024-12 | 정부·연구기관 | high | 2026-10-11 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20241202175 | 아니오 |
| ref-1528 | OMRON (Omron Adept Technologies) | Mobile Robot LD Safety Guide (I616-E-06 / 18393-000 Rev H) | 2019-10 | 벤더 문서 | medium | 2026-10-11 | https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1 | 아니오 |
| ref-1529 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp | 아니오 |
| ref-1530 | Perez, I., Mavridou, A., Pressburger, T., Will, A., Martin, P. J. (EPTCS 371) | Monitoring ROS2: from Requirements to Autonomous Robots | 2022-09 | 논문 | high | 2026-10-11 | https://arxiv.org/abs/2209.14030 | 아니오 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2502.20693 | 아니오 |
| ref-1255 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 2026-04-23 | 표준 | medium | 2026-10-11 | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download | 예 |
| ref-789 | ISO | ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 미확인 | 표준 | medium | 2026-10-11 | https://www.iso.org/standard/88615.html | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-10-11 | https://www.iso.org/standard/83545.html | 예 |
| ref-561 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | 정부·연구기관 | medium | 2026-10-11 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1077 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md | 아니오 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-1398 | Open-RMF (open-rmf/rmf_ros2 저장소) | Changelog for package rmf_fleet_adapter | 2026-09-26 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | high | 2026-10-11 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 아니오 |
| ref-417 | Obi, I. 외(arXiv) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2604.05427 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/safety-and-risk-management.md | 3, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 3(분리 2026-09-25-area25-s3) — 국내 위험성평가 실시 주체와 변경 조건: 도급·수급사업주 각각 실시(f17), 근로자 참여 5개 경우(f18), 수시평가 1~6호(f19), 제15조④ 간주 규정(f20). 2026 전부개정안은 예고안으로만(f23, 공고 번호·마감일은 f24 [추정]) / 섹션 5 — '출하 마감 전 화재경보' 표 제약 칸(107행) 정정: 2.10.0(2025-05-09) #413 플릿 이름 선택(f29 [사실]), 2.14.0 대상 비상 신호 처리(f30 [사실])와 기존 불리언 EmergencyNotice 경로 병존(f31 [사실])을 함께 적고 '이후 구현 여부 미확인' 을 지움(f32). 이슈 세부(두 건물)는 f28 [추정]. 같은 주장이 docs/categories/safety/index.md 95행과 docs/categories/governance-law-and-society/index.md 84행에도 있으나 이번 실행 범위 밖이라 후속 정리 필요. 운영 시사점 f45. Belzile 사례는 현장 유형 '기타(건설 현장)' 로 8절에만 넣고 5절 시나리오로 만들지 않음 / 섹션 6(분리 2026-09-25-area25-s6) — STPA 산출물: 네 단계(f1)·위험한 제어 행동 네 유형(f2)과 ROP 적용 의견(f40); 운영자 참여 기록: 청취조사 아차사고·개선 의견(f21), 일용근로자 사례 문자·QR 익명 제안(f22), 제15조④ 간주 규정과 연결(f20); 감시와 대응 구분: Ogma 탐지·보고 한정(f25, 위치는 §3 Related work 의 DeRoS 비교 문장), 의견 f44. VDA 5050 pause 의견 f43. 기존 내용 확인(새로 넣지 않음): VDA 5050 안전 표준 아님(2026-09-25-area25-s3.md 39행, 2026-09-25-area25-s6.md 49행), startPause·stopPause(2026-09-25-area20-s4.md 42행, 2026-09-25-area25-s6.md 49행), activeEmergencyStop MANUAL·REMOTE·NONE(docs/categories/safety/index.md 113행), Nav2 하드 실시간 인증 미제공(2026-09-30-area49-s6.md 47행, 2026-09-30-area49-s7.md 47행, ref-1077) / 섹션 7(분리 2026-09-25-area25-s7·2026-09-26-area25-s7) — 2026-09-25-area25-s7.md 43행 R15.08-2 행의 '예정된 Part 3' 을 'Part 3(2026-04-23 발행)' 으로 정정(f7; 발행 사실은 기존 내용 확인 — ref-1255, safety/index.md 53행, 재추가하지 않음). 2026-09-26-area25-s7.md 46행 '차기판(제2판 초안)' 은 2023 판이 제2판이므로 '차기판(제3판)' 으로 정정 제안(f10 [추정], 단계·날짜는 미확인). ISO/DIS 3691-4 Edition 3·40.60(2026-09-10)과 ISO/DIS 12100.3 40.60(2026-09-15)은 확인 불가라 [추정]으로만(f8·f9) — ref-789 는 2026-09-26 'ISO/CD' 로 기록돼 메모와 충돌하므로 제목 갱신 보류. 이동식 협동로봇 KS 행(2026-09-25-area25-s7.md 46행 '표준 번호는 미확인'): KS B 7327 번호·표제·발행일·고시(f11), 관제·군집 관리 제외 범위(f12), 부합화 칸 공란·인용표준(f13), 발표 KS = KS B 7327(f14 [추정]). KS B ISO 3691-4 2026-09-14 개정·ISO 3691-4:2023(IDT) 행 추가(f16) / 섹션 8(분리 2026-09-25-area25-s8) — Bensaci 외 2020 AEJ(f3, 초록 범위로 축소; 11대·한계는 f4 [추정]/제외), Belzile 사례 조건: Pomerleau·몬트리올·Clearpath Jackal 배치 예정(f5), 잔류 위험지수는 재추정 값(f6) — 기존 '현장 전문가 검증을 거쳤다고 저자가 보고' [추정] 문장은 유지; ICAR 2021 판 날짜는 근거가 없어 쓰지 않음. SafeGate 평가 층위(f36: 230개·30개 수치는 기존 내용 확인 — 2026-09-25-area25-s6.md 53행, safety/index.md 69행, 실물 실험 정성 결과·단계 4~6 시험이 새 내용), CR 분모 문제(f37), 표 II 183건(f38)과 차이 해석(f39 [추정]), 의견 f46 / 섹션 9 — 로봇 자체·시설 경계에 제조사 매뉴얼의 플릿 정보≠인터록(f26)·사용자 부품 포함 PL·PFH·최종 위험성평가 사용자 책임(f27) 을 벤더 주장 [추정]으로; 업종별 조건 행에 국내 지침의 도급·수급 각각 실시(f17)와 책임 배분 추정(f41); EU 실질적 변경 정의의 (a)·(b) 조건(f33)·제54조 조항별 적용일(f34, 일반 적용일 2027-01-20 은 기존 내용 확인 — 2026-09-25-area24-s3.md 41행)과 해석(f35) / 섹션 11 — 부분 근거만(해결 제안 없음): oq-070 근거 f11·f14, oq-064 근거 f13·f15, oq-093 근거 f33~f35(oq-282 와 겹침), oq-095 근거 f42, oq-096 근거 f41. 메모의 '신규 질문' 3건(혼합 플릿 RA 수행·갱신 주체, VDA 원격/플릿 정지 경로 PL, 규칙 223 울타리 생략의 AMR 플릿 적용)은 질문 문구를 대조해 각각 기존 oq-096·oq-095·oq-097 과 같아 새로 만들지 않음. oq-092·oq-097 은 이번 메모가 답하지 못함(확인 못 함). 관련 기존 질문: oq-265(R15.08-3 사용자 의무, f7 은 발행 사실만), oq-123(KS 새 판 부합 — f16 은 3691-4 에 관한 것이라 10218-2·TS 15066 질문에는 답하지 않음), oq-170(ISO 3691-4 원문, 미해결). 새 질문 3건. 다음 실행 후보: 50. 안전 표준·인증·사고 조사(f7~f16), 58. 다사업자 책임·계약·데이터(f17·f41), 59. 법·규제·보험·라이선스(f33~f35), 47. AI·학습·적응과 모델 운영(f36~f39). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- SafeGate 논문의 충돌률(CR)은 실행된 작업이 0건일 때 어떻게 산정되며, 표 II 의 183건과 전체 230건 사이에서 빠진 47건은 어떤 범주(판단 보류 등)인지 저자 코드·원자료로 재현할 수 있는가? | 관련 영역: 48. 안전·위험 관리, 47. AI·학습·적응과 모델 운영 | 근거: f37 | 종류: 일반
- Open-RMF 의 플릿 이름 기반 비상 신호(fleet_names)를 건물·구역 단위 대피 계획에 연결할 때, 여러 건물에 걸친 플릿 공유·재개 승인·네트워크 단절·기존 불리언 신호와의 충돌을 어떻게 시험·검증하는가? | 관련 영역: 48. 안전·위험 관리, 22. 설비·건물 시스템 연동 | 근거: f30 | 종류: 일반
- 여러 제조사 로봇이 섞인 현장에서 STPA 제어 구조 분석, 변경 이력(수시 위험성평가), 근로자 아차사고 제보를 하나의 위험등록부로 연결해 운영한 공개 실증 사례가 있는가? | 관련 영역: 48. 안전·위험 관리, 50. 안전 표준·인증·사고 조사 | 근거: f40 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 11건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-04/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f3·f4: Bensaci 외 2020 은 초록·Crossref 서지만 확인(본문 미접근). 메모 F03(11로봇·화학 분석실)은 [추정], F05(시나리오 병합 한계)는 확인 불가로 finding 에서 뺌. 'semi quantitative'·'modified hierarchical' 표현과 '2020-06-21 채택' 은 미확인
    - f5·f6: Belzile 논문은 arXiv v1(2025-02-28) PDF 기준. 메모의 'ICAR 2021 워크숍판·2021-12-07' 은 근거가 없어 쓰지 않음(arXiv 에는 'Workshop … at ICAR' 표기만)
    - f7: A3 판매 페이지 재열람 403 — 발행일은 기존 ref-1255(2026-10-09 열람) 기준
    - f8~f10: iso.org 403 으로 ISO/DIS 3691-4(Edition 3, 40.60, 2026-09-10)·ISO/DIS 12100.3(40.60, 2026-09-15) 미확인. ref-789 의 2026-09-26 'ISO/CD' 기록과 충돌. 3691-4 의 판 번호(2020 제1판·2023 제2판)도 목록 원문으로 재확인 필요
    - f13·f14: KS B 7327 과 R15.08-2·ISO 10218 의 조항별 대응·동등 인증 미확인(본문 미열람). 정책브리핑 발표 KS 와의 동일성은 날짜·고시 사유 일치에 근거한 추정
    - f24: 행정예고 공고 번호(2026-461)와 의견 제출 마감(2026-10-13) 미확인. 최종 고시 발령·시행 상태 미확인
    - f28: RMF issue #658 재열람 GitHub 403 — '두 건물' 등 세부 미확인
    - f26·f27: OMRON 매뉴얼은 원문 대조로 문서 내용을 확인했으나, 저장소 규칙(6.2 항목 13)에 따라 벤더 문서만 근거라 vendor_claim: true·[추정]으로 둔다
    - f37~f39: SafeGate 저자 코드·원자료 미확인, 게재지 미확인(arXiv v1 프리프린트)
    - 메모의 VDA 5050 '2026-03' 날짜는 명세 안에 근거가 없어 쓰지 않음(ref-031 published null 유지)
    - oq-092(펌웨어·안전 파라미터 변경 재심사)·oq-097(규칙 223 울타리 생략의 AMR 플릿 적용)은 이번 메모에 근거가 없어 확인 못 함
    - f7(R15.08-3 발행일 2026-04-23)은 위키에 2026-10-09 원문 열람 기록(ref-1255)이 있으나 이번에 A3 페이지를 다시 열지 못해 [추정]으로 둔다.
- 범위 경계 위반 의심:
    - f17~f24: 국내 위험성평가 고시·가이드는 사업장 안전보건 법규로 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스와 겹치므로 이 영역에는 위험성평가 실시 주체·참여·변경 조건 근거로만 씀
    - f26·f27: 비상정지 회로·PL·PFH 설계는 로봇 제조사·통합자 쪽 안전 기능(연계 대상)이며, ROP 몫은 인터페이스 구분과 검증 자료 요구로 한정
    - f33~f35: EU 기계 규정 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인과 판단 조건 정리까지만 하고 개별 업데이트의 법적 분류는 하지 않음
    - f36~f39·f46: SafeGate 는 LLM 명령의 실행 전 판정으로 47. AI·학습·적응과 모델 운영과 겹치며, 이 영역에는 평가 분모·층위 해석만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 11건/15(ref-1520~ref-1530, 예약 구간 ref-1520~ref-1549 안), 재사용 11건(ref-563·ref-1255·ref-789·ref-470·ref-561·ref-031·ref-1077·ref-567·ref-1398·ref-555·ref-417). 출처 매핑(검증 결과 기준): 메모 n1→ref-1520, n2→ref-1521(DOI 서지·초록), n3→ref-563, n4→ref-1255, n5→ref-789(제목 CD→DIS 갱신 보류), n6→ref-1522(미열람), n7→ref-1523, n8→ref-1524, n9→ref-1525, n10→ref-1526, n11→ref-1527, n12→ref-031, n13→ref-1077, n14→ref-1528, n15→ref-567(미열람), n16→ref-1529, n17→ref-1398, n18→ref-555(2026-07-27 통합본으로 열람), n19→ref-417, n20→ref-1530. 추가 재사용: ref-470(판 번호 정정 근거), ref-561(발표 KS 대응). fetched: false 는 ref-1522·ref-1255·ref-789·ref-470·ref-561·ref-567(이번 재열람 403 또는 미열람). ref-1521 은 초록·서지만 확인. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: 고시·가이드는 고용노동부, CHANGELOG·코드·이슈는 Open-RMF) — 신뢰도 medium 이하. 중복 제거: 메모 F08(R15.08-3 발행일)·F22~F25(VDA 5050 안전 표준 아님·startPause·stopPause·activeEmergencyStop)·F26(Nav2 인증 미제공)·F33 일반 정의와 F35 일반 적용일·F36·F37 수치는 기존 위키에 있어 새 finding 으로 넣지 않고 위치만 rationale 에 적었다(f7·f42~f44 는 정정·추론·의견에서 참조). 검증 반영: F03·F05 [추정]/제외, F04 초록 범위로 축소, F09~F11 [추정](ref-789 충돌), 공고 번호·F21 마감일 [추정], F30 세부 [추정], F17 의 '상시평가 인정 경로' → '제15조④ 간주 규정', F19 '일용근로자 사례' 명시, F27 위치 '§3 Related work DeRoS 비교 문장', F28·F29 벤더 주장 [추정], 2.14.0 의 불리언 EmergencyNotice 병존(f31) 추가, 2026-09-26-area25-s7.md 46행 '제2판 초안' 정정 제안(f10). 현장 유형: 물류창고(f32·f43·f45, 기존 가상 시나리오의 정정·의견), 기타(건설 현장 f5·f6, 다중 건물 배치 f28). 국내 자료: 고용노동부 고시·가이드·행정예고(ref-1525~ref-1527), KS 목록(ref-1523·ref-1524). 열린 질문 해결 제안 없음 — 부분 근거만: oq-064(f13·f15), oq-070(f11·f14), oq-093·oq-282(f33~f35), oq-095(f42), oq-096(f41). 메모의 '신규 질문' 3건은 기존 oq-095·oq-096·oq-097 과 같은 질문임을 질문 문장으로 확인해 새로 만들지 않았고, '새로 생긴 열린 질문' 3건은 docs/open-questions.md 에 같은 질문이 없어 새로 올린다. 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 원문 절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음(STPA·위험성평가는 이미 용어집에 있음).
```

### runs/2026-10-11-03/research.md

```markdown
# 리서치 브리프 2026-10-11-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-03 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 22. 설비·건물 시스템 연동 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 국토부 '로봇 친화형 건축물' 핵심기술 개발 보도자료(ref-322)는 제목만 확인돼 발행일·사업기간·세부 과제가 비어 있고, KS B 7317 은 '2021년 11월 제정'만 있어 이후 개정 이력이 없음
- 섹션 4·6. 핵심 개념·대표 접근법(주제 페이지 2026-09-25-area10-s4) — 승강기 세션을 언제 '수락'으로 볼지, 세션 종료·잔류 처리, 작업대 결과의 완료 판정 조건 근거가 약함. 제조사 어댑터(KONE·Dormakaba)와 PLC 연결의 실제 조건이 없음
- 섹션 5. 적용 사례 — 물류창고 가상 시나리오뿐이며 실제 설비 연결(PLC·드라이 접점)과 화재 복구, 상업 시설 사례가 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지 2026-09-25-area10-s7) — KOLA 단체표준이 '표준 번호·제정일·내용 미확인', SEMI E84 현행판·후속 개발 제안, BACnet 출입통제 문서의 지위가 비어 있음
- 섹션 8. 대표 연구와 자료(주제 페이지 2026-09-25-area10-s8) — '모두 원문을 열지 못해 결과 수치는 쓰지 않는다'로 남아 있어 각 연구의 실험 조건(실물·수치 실험)과 승강기 결과가 비어 있음
- 섹션 9·11 — 출입통제 연동에서 권한 확인 주체(oq-043), 단체표준–Open-RMF 대응(oq-041), 인계 신호 표준(oq-042), 물류센터 승강기 병목(oq-010)이 열려 있음

## 조사 질문

1. 문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
2. oq-010 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? (섹션 3·8 겨냥)
3. oq-041 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (oq-283 표준 번호 포함, 섹션 7 겨냥)
4. oq-042 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? (oq-062 포함, 섹션 6·7 겨냥)
5. oq-043 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (섹션 7·9 겨냥)
6. KS B 7317 과 로봇 친화형 건축물 관련 국내 제도·연구개발은 현재 어느 판·단계인가? (oq-098·oq-173·oq-311·oq-179 관련, 섹션 3·7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Park·Park 의 2026년 Architectural Research 논문은 초록 기준으로 로봇 친화형 건축물 인증(REEC)과 무장애(BF) 인증을 비교 분석해 사람 중심·로봇 적응형 건축 설계 기준을 도출했다. | ref-1483 | 아니오 | medium | 2026-07-21 | — | — |
| f2 | [추정] | 국토교통부의 로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발 연구개발은 2025년 5월 착수보고회를 열고 2028년까지 완료할 예정이라고 2차 보도됐다. | ref-322, ref-1484 | 아니오 | low | 2025-05-28 | — | — |
| f3 | [추정] | 같은 연구개발은 세부 중점과제 가운데 하나로 기술 실증을 통한 기술표준·인증제도 개선방안 마련을 두었다고 2차 보도됐다. | ref-322, ref-1484 | 아니오 | low | 2025-05-28 | — | — |
| f4 | [사실] | e-나라표준인증의 KS B 7317 이력은 2021-11-30 제정(고시 2021-0561), 2022-12-09 개정(고시 2022-0571), 2025-05-09 개정(고시 2025-0073)을 기록한다. | ref-314 | 아니오 | medium | 2025-05-09 | — | — |
| f5 | [사실] | 같은 KS B 7317 기본정보는 적용 대상을 엘리베이터 탑승 기능이 있는 서비스 로봇과 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터로 적고, 표준개발협력기관을 한국AI·로봇산업협회로 적는다. | ref-314 | 아니오 | medium | 2025-05-09 | — | — |
| f6 | [사실] | 대한승강기협회(KOLA)는 2026-03-27 게시한 보도자료에서 「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」 단체표준을 제정했다고 발표했다. | ref-1485 | 아니오 | medium | 2026-03-27 | — | — |
| f7 | [사실] | e-나라표준인증 단체표준 목록은 이 가이드라인을 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 로 올려 두어, KOLA 게시일(2026-03-27)과 목록 등록일이 다르다. | ref-1486 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | KOLA 발표는 이 가이드라인이 엘리베이터와 로봇 상호 연동을 위한 일반사항, 시험 설비 및 시험 절차를 제시하며 e-나라표준인증에서 무료로 내려받을 수 있다고 설명한다. | ref-1485 | 아니오 | medium | 2026-03-27 | — | — |
| f9 | [사실] | Open-RMF 개발자(mxgrey)는 2024년 토론 답변에서, 세션을 안전하게 수행하려면 승강기가 별도 AGV 모드여야 하는 경우 모드 전환을 마칠 때까지 승강기 상태에 session_id 를 내보내지 말아야 한다고 권고했다. | ref-1487 | 아니오 | medium | 2024-08-21 | 제약 | — |
| f10 | [사실] | 같은 답변은 별도 AGV 모드가 없는 승강기도 있을 수 있다고 설명한다. | ref-1487 | 아니오 | medium | 2024-08-21 | 제약 | — |
| f11 | [사실] | rmf_ros2 의 lift_supervisor 구현은 승강기별 활성 세션을 두고, 같은 session_id 의 새 요청은 갱신으로 다시 발행하며 세션 종료 요청이면 종료를 발행하고 활성 세션을 비운다. | ref-1488 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [사실] | 같은 구현은 감독자에게 활성 요청이 없는데 승강기 상태에 세션이 남아 있으면 승강기가 풀리도록 세션 종료 요청을 계속 발행하며, 승강기 배정을 더 지능적으로 하라는 TODO 만 남겨 두고 배정 규칙은 두지 않는다. | ref-1488 | 아니오 | medium | 2026-10-11 | 예외·성과 | — |
| f13 | [사실] | rmf_fleet_adapter 변경기록의 2.13.0(2026-06-15)에는 승강기가 이미 해당 층에 있으면 legacy 완료 상태를 내보내는 변경(#510)이 실려 있다. | ref-1398 | 아니오 | medium | 2026-06-15 | — | — |
| f14 | [사실] | rmf_ros2 의 DispenseItem 단계는 요청 id 가 일치하는 DispenserResult 가 SUCCESS 이면 완료, FAILED 이면 실패로 바꾸고, ACKNOWLEDGED 는 접수 표시만 한다. | ref-1489 | 아니오 | medium | 2026-10-11 | 완료·인계 | — |
| f15 | [사실] | 같은 구현은 디스펜서 상태의 요청 큐에 요청 id 가 들어 있으면 접수된 것으로 보고, 접수 뒤 큐에서 요청 id 가 사라지면 결과 메시지 없이도 완료로 간주한다. | ref-1489 | 아니오 | medium | 2026-10-11 | 완료·인계 | — |
| f16 | [추정] | 큐 소거만으로 완료 처리하면 현장 작업대 큐에서 요청이 취소·오류로 빠진 경우에도 인계 완료로 잘못 판단할 수 있을 것으로 보인다. | ref-1489 | 아니오 | low | 2026-10-11 | 완료·인계 | — |
| f17 | [사실] | CHART 계열 공개 KONE 승강기 어댑터 README 는 Open-RMF 승강기 메시지와 KONE API v2.0 사이에서 WebSocket 으로 승강기 명령을 보내고 승강기 상태를 받는 구조를 설명한다. | ref-1490 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [사실] | 같은 README 는 실제 승강기를 제어하려면 access_id 와 access_secret 을 KONE 담당자에게서 받아야 한다고 안내한다. | ref-1490 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | 연계 대상: Open-RMF 의 Dormakaba 문 어댑터 README 는 시험한 EL301·ED250 문 구동기에 Dormakaba IoT connector 를 장착해야 한다고 안내한다. | ref-1491 | 아니오 | medium | 2026-10-11 | 수행 자원 | — |
| f20 | [사실] | 같은 README 는 문 클라우드 API 접근 자격증명을 Dormakaba 가 제공한다고 안내한다. | ref-1491 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [추정] | 연계 대상: HopeTechnik 의 도서관 현장 설계 문서에서는 현장에 새로 설치한 승강기 제어함(lift controller box)의 PLC(Beckhoff CX9020)가 서버의 ADS 명령을 받아 드라이 접점으로 승강기 신호를 조작하며, 승강기 업체가 기존 승강기를 AGV 모드로 개조했다. | ref-1492 | 아니오 | medium | 2026-10-11 | 기타 / 수행 자원 | 벤더 주장 |
| f22 | [추정] | 연계 대상: 같은 문서의 복구표는 화재 경보가 울리면 승강기가 수동 모드로 돌아가고 PLC 가 오류 상태에 머물러, 재시작을 위한 수동 개입이 필요하다고 적는다. | ref-1492 | 아니오 | medium | 2026-10-11 | 기타 / 예외·성과 | 벤더 주장 |
| f23 | [추정] | 같은 문서는 승강기 상태 전송 주기를 개요에서는 1 Hz 로, 서버 절에서는 2초마다로 서로 다르게 적고, 승강기 요청은 1초마다 보낸다고 적는다. | ref-1492 | 아니오 | medium | 2026-10-11 | 기타 | 벤더 주장 |
| f24 | [추정] | OMRON LD 시리즈 통합 안내서(I680-E-02)의 인계 예시는 위치·준비 상태 확인, 적재물 교환, 정지·최종 위치 확인, 출발 준비 확인을 단계로 나눈다고 외부 조사 메모가 전한다. | ref-1493 | 아니오 | low | 2026-10-11 | 완료·인계 | 원문 미열람 |
| f25 | [추정] | 같은 안내서는 그 인계 절차가 예시이며 응용 요구에 따라 달라질 수 있다고 적는다고 외부 조사 메모가 전한다. | ref-1493 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f26 | [사실] | SEMI 공식 판매 목록은 E84-0823 을 현행판(Current)으로 표시하고, E84 의 목적을 자동 반송 시스템(AMHS)과 생산 설비 로드포트 사이 캐리어 인계용 병렬 I/O 신호 개선으로 설명한다. | ref-202 | 아니오 | medium | 2026-10-11 | — | — |
| f27 | [추정] | SEMI Doc 7442 는 E84 를 출발점으로 별도의 인계 인터페이스 규격과 TCP/IP 하위 규격을 만들자는 신규 예비 표준 개발 제안서(SNARF)라고 외부 조사 메모가 전한다. | ref-1494 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f28 | [사실] | 고려대 구로병원 약품 배송 로봇 논문은 ROC 로 찾은 승강기 가동률(EOR) 임계값 59.01% 를 현장 특정값으로 해석해야 하며 다른 병원에 적용할 때 재보정이 필요하다고 명시한다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 제약 | — |
| f29 | [사실] | 2026-10-11 재확인에서도 같은 논문에는 전체 성공률 87.03% 의 분모를 설명하는 구절이 없고, 분석 대상 122건에서 실패 14건을 뺀 108건의 비율은 약 88.52% 로 보고값과 다르다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f30 | [사실] | 사람과 승강기를 함께 쓰는 실제 건물에서 로봇의 층간 이동이 지연된 사례가 서로 다른 두 연구에서 보고됐다: 병원 논문은 승강기 가동률이 높을수록 배송 시간이 길어졌다고, KAIST 지도 구축 논문은 외부 이용자 때문에 승강기가 다른 층으로 가 지연이 생겼다고 적는다. | ref-943, ref-163 | 예 | high | 2026-03 | 제약 | — |
| f31 | [사실] | Han 외 다층 호텔 배송 경로계획 논문은 실제 호텔 평면·층고로 거리 행렬(68×68)만 만들고 배송 수요는 무작위 표본으로 생성했으며, 승강기 기본 대기 시간을 30초로 두었다. | ref-103 | 아니오 | medium | 2025-03-13 | — | — |
| f32 | [사실] | Kim 외 그래프 기반 다층 경로계획 논문은 15층 건물을 나타내는 그래프에서 소포 1·3·5·7개 시나리오로 알고리즘을 평가했다. | ref-321 | 아니오 | medium | 2025-02-28 | — | — |
| f33 | [사실] | 노주형 외 다층 지도 구축 연구는 KAIST N1 건물 5~9층에서 각 층의 절반 영역을 대상으로 평가를 수행했다. | ref-163 | 아니오 | medium | 2026-03 | — | — |
| f34 | [사실] | 같은 연구의 승강기 상호작용 시험에서는 20회 중 19회 성공이 보고됐다. | ref-163 | 아니오 | medium | 2026-03 | — | — |
| f35 | [사실] | BACnet 출입통제 백서 BAC-09-08(2008-09-27)은 SSPC 135 LSS 작업반의 진행 중 작업이자 BACnet 표준 변경 제안의 기초 문서라고 스스로 밝힌다. | ref-1495 | 아니오 | medium | 2008-09-27 | — | — |
| f36 | [사실] | 같은 백서는 인증과 권한 검사를 구분하고, 특정 시간에 특정 문을 통과할 권리를 기본 권한 검사의 예로 든다. | ref-1495 | 아니오 | medium | 2008-09-27 | — | — |
| f37 | [추정] | NAVER LABS 는 2026-07-23 블로그에서 ARC 가 Tokyo Midtown Yaesu 의 기존 화물 승강기·자동문과 출입 경로를 중앙에서 연결한다고 설명하고, 연말까지 전 층 로봇 배송으로 넓힐 계획이라고 밝혔다. | ref-1496 | 아니오 | low | 2026-07-23 | 상업 시설 | 벤더 주장 |
| f38 | [의견] | 구축자 의견: ROP 의 설비 연동 수용 기준은 건축물 인증 항목·국가 연구개발 계획과 별도 목록으로 관리하고, 발주 때 인증의 적용 판·심사 범위와 현장 설비 연결 계약을 서로 다른 증빙으로 확인하는 것이 좋다. | ref-1483, ref-322, ref-1484 | 아니오 | low | 2026-10-11 | — | — |
| f39 | [의견] | 구축자 의견: 승강기 탑승 안전 표준을 검토할 때는 판(제정·개정 일자)·적용 범위·대상 승강기 유형을 함께 기록하는 것이 좋다. | ref-314 | 아니오 | low | 2026-10-11 | — | — |
| f40 | [의견] | 구축자 의견: KOLA 가이드라인과 Open-RMF 승강기 메시지의 대응표는 표준 원문의 메시지·시험 시나리오를 확보한 뒤에 작성하는 것이 맞다. | ref-1485, ref-1486 | 아니오 | low | 2026-10-11 | — | — |
| f41 | [의견] | 구축자 의견: 장치별 세션 수락 조건(AGV 모드 전환 완료 뒤 session_id 보고 여부)을 어댑터 계약에 적고, 수락 전 탑승을 막는지 확인하는 시험을 두는 것이 좋다. | ref-1487 | 아니오 | low | 2026-10-11 | — | — |
| f42 | [의견] | 구축자 의견: 세션 유실·중복 종료·설비 상태의 세션 잔류 상황을 현장 인수 시험 항목에 넣는 것이 좋다. | ref-1488 | 아니오 | low | 2026-10-11 | — | — |
| f43 | [의견] | 구축자 의견: 실물 인계 성공을 뜻하는 센서·PLC 조건을 작업대 결과 메시지와 따로 정하고, 큐 소거가 취소·오류를 뜻하는 경우를 구별하는 것이 맞다. | ref-1489 | 아니오 | low | 2026-10-11 | — | — |
| f44 | [의견] | 구축자 의견: 제조사 승강기 어댑터를 검토할 때는 공개 어댑터의 판과 별도로 현행 API 판·권한 범위·건물 등록·세션 유지 조건을 확인하는 것이 좋다. | ref-1490 | 아니오 | low | 2026-10-11 | — | — |
| f45 | [의견] | 구축자 의견: 자동문 연동에서는 문 열기 API 자격증명과 별도로 로봇의 공간별 출입 권한과 비상 우선권을 누가 정하는지 확인해야 한다. | ref-1491, ref-1495 | 아니오 | low | 2026-10-11 | — | — |
| f46 | [의견] | 구축자 의견: ROP 장애 복구와 건물 설비의 비상 복귀를 따로 시험하고, 화재 뒤 설비 재시작 같은 수동 복귀의 책임자를 정해 두는 것이 좋다. | ref-1492 | 아니오 | low | 2026-10-11 | — | — |
| f47 | [의견] | 구축자 의견: ROP 는 준비·허가·이송·완료의 의미를 현장 PLC·작업대와 합의하고, 물리 인계 완료를 상위 작업 완료에 연결하는 것이 좋다. | ref-202, ref-1493 | 아니오 | low | 2026-10-11 | — | — |
| f48 | [의견] | 구축자 의견: 병원·호텔·그래프·지도 연구의 승강기 결과를 국내 다층 물류센터 처리량으로 옮기는 것은 보류하고, 승강기 가동률·통신 상태·카 내부 점유를 나눠 수집해 현장별 임계값을 새로 검증하는 것이 맞다. | ref-943, ref-103, ref-321, ref-163 | 아니오 | low | 2026-10-11 | — | — |
| f49 | [의견] | 구축자 의견: 설비 API 연동과 로봇팔 버튼 조작을 서로 다른 승강기 연결 방식으로 기록하고, 공유 승강기 지연 시험을 따로 두는 것이 좋다. | ref-163, ref-943 | 아니오 | low | 2026-10-11 | — | — |
| f50 | [의견] | 구축자 의견: 기존 건물 도입 사례는 연동 설비 목록과 실제 운영 중인 로봇 종류·층 범위를 고객 측 자료로 따로 확인하기 전에는 운영 실증으로 세지 않는 것이 맞다. | ref-1496 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-322 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 미확인 | 정부·연구기관 | medium | 2026-10-11 | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 | 예 |
| ref-1484 | 스마트투데이(이재수) | "사람과 로봇이 공존하는 스마트 빌딩 앞당긴다"...국토부 산학협력단과 기술개발 착수 | 2025-05-28 | 기사 | low | 2026-10-11 | https://www.smarttoday.co.kr/ko-kr/articles/81933 | 아니오 |
| ref-1483 | Park, Y.; Park, S. (Architectural Research) | Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems | 2026-07-21 | 논문 | medium | 2026-10-11 | https://link.springer.com/article/10.1007/s44515-026-00016-y | 아니오 |
| ref-314 | 국가기술표준원(e-나라표준인증·KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2025-05-09 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 아니오 |
| ref-1485 | 대한승강기협회(KOLA) | 대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27) | 2026-03-27 | 정부·연구기관 | medium | 2026-10-11 | https://kola.or.kr/pages/61/68/bbs/5705 | 아니오 |
| ref-1486 | 국가기술표준원(e-나라표준인증) | 단체표준 목록 — B-KOLA-0001-7700 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://www.standard.go.kr/KSCI/grpstd/getGrpStdCrtfcReqst.do?menuId=60372&topMenuId=502&upperMenuId=503 | 아니오 |
| ref-1487 | cwrx777; mxgrey (Open Robotics Discourse 아카이브) | Lift session issues - Robot enter lift while lift is still in human mode (#513) | 2024-08-21 | 오픈소스 문서 | medium | 2026-10-11 | https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679 | 아니오 |
| ref-1488 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter/src/lift_supervisor/Node.cpp (commit 4cea3fe) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/lift_supervisor/Node.cpp | 아니오 |
| ref-1398 | Open-RMF (open-rmf/rmf_ros2 저장소) | Changelog for package rmf_fleet_adapter | 2026-09-26 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-1489 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp (commit 4cea3fe) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp | 아니오 |
| ref-1490 | CHART; KABAM-Robotics 보존 저장소 | KONE RMF Lift Adapter / kone-ros-api — README (commit 9bc3a87) | 미확인 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596 | 아니오 |
| ref-1491 | Open-RMF (open-rmf/door_adapter_dormakaba 저장소) | door_adapter_dormakaba — README (commit 2cf76a6) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668 | 아니오 |
| ref-1492 | HopeTechnik (RMF Systems Engineering Handbook) | Lift and Doors Integration | 미확인 | 벤더 문서 | medium | 2026-10-11 | https://trl-rmf.github.io/website/content/lift-door-integration.html | 아니오 |
| ref-1493 | OMRON | LD-Series Integration Guide (I680-E-02) | 미확인 | 벤더 문서 | medium | 2026-10-11 | https://www.omron.com.tw/data_pdf/mnu/i680-e-02_ld.pdf?id=3664 | 예 |
| ref-202 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 미확인 | 표준 | medium | 2026-10-11 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface | 아니오 |
| ref-1494 | SEMI Physical Interfaces & Carriers TC (Japan) | SNARF for Doc 7442: Specification for Enhanced Handoff Interface | 미확인 | 표준 | medium | 2026-10-11 | https://downloads.semi.org/web/wstdsbal.nsf/18a679096dfd445188256d35007d447d/0db3fe2c9bb0eb2488258d9400027699!OpenDocument | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-103 | Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 2025-03-13 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 아니오 |
| ref-321 | Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025-02-28 | 논문 | high | 2026-10-11 | https://doi.org/10.3390/electronics14050982 | 아니오 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026-03 | 논문 | high | 2026-10-11 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 아니오 |
| ref-1495 | SSPC 135 LSS-WG; Isler, B. 외 (BACnet International) | Physical Access Control with BACnet (BAC-09-08 White Paper) | 2008-09-27 | 표준 | medium | 2026-10-11 | https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf | 아니오 |
| ref-1496 | NAVER LABS | NAVER’s ARC Goes to Japan | 2026-07-23 | 벤더 문서 | low | 2026-10-11 | https://naverlabs.com/en/blogDetail?seq=10034507 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/facility-and-building-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 갱신(차등): 섹션 3 — 국토부 연구개발의 2028년 완료 예정·기술표준·인증제도 개선 과제(f2·f3, 보도자료 원문 미열람이라 [추정]·'2차 보도 기준', 보도 날짜는 2025-05-28 기사 기준이며 ref-322 발행일은 미확인 유지). KS B 7317 문장은 기존 '2021년 11월 제정'을 유지하고 개정 이력(2022-12-09·2025-05-09)과 적용 범위(병원 환자 전용 엘리베이터 제외)를 덧붙임(f4·f5); ref-314 발행일을 현행 개정일 2025-05-09 로 갱신 제안 / 섹션 4(분리 2026-09-25-area10-s4) — '승강기 세션과 모드' 항목에 AGV 모드 전환 완료 뒤 session_id 보고 권고와 AGV 모드 없는 승강기(f9·f10); LiftState session_id 정의·모드 상수는 기존 내용 확인(같은 페이지 승강기 세션 항목, 2026-10-10-charging-threshold-charger-lift-evidence, 2026-09-25-area16-s4)이라 새로 넣지 않음 / 섹션 5 — 현장 유형 '기타(도서관)' 실제 설비 연결 사례: 새로 단 승강기 제어함 PLC(Beckhoff CX9020)·ADS·드라이 접점·승강기 업체 AGV 모드 개조(f21), 화재 경보 뒤 PLC 오류 유지·수동 재시작(f22), 메시지 주기 기재 불일치는 결론 없이(f23). '상업 시설' 사례로 NAVER ARC Yaesu(f37, 벤더 주장·계획 구분, f50) / 섹션 6 — 어댑터 요청·상태 감독: lift_supervisor 의 같은 세션 갱신·종료 처리와 잔류 세션 종료 반복 발행, 배정 규칙 미구현 TODO(f11·f12), 변경기록 2.13.0 #510(f13, 2.14.0 존재 병기); lift_supervisor 존재 자체는 기존 내용 확인(categories/integration/index.md 110행). 요청–결과 인계: DispenseItem 의 SUCCESS 완료·큐 소거 완료 간주(f14·f15)와 위험 해석(f16, [추정]); DispenserResult·IngestorResult 의 ACKNOWLEDGED·SUCCESS·FAILED 값 정의는 기존 내용 확인(planning-and-optimization/task-and-workflow-modeling.md 86행)이라 넣지 않음. 제조사 어댑터: KONE API v2.0 WebSocket·자격증명(f17·f18; The Galen 실기 시험은 기존 내용 확인 — ref-884, robot-ontology/ontology-based-system-and-robot-integration.md 102·113행), Dormakaba IoT connector·자격증명(f19·f20). 물리 인계 예시: OMRON(f24·f25, 원문 미열람 [추정]) / 섹션 7(분리 2026-09-25-area10-s7) — KOLA 행 '표준 번호·제정일·내용은 미확인'을 정정: 협회 보도자료(f6·f8, 게시일 2026-03-27)와 e-나라표준인증 목록 B-KOLA-0001-7700·등록일자 2026-03-24(f7)를 날짜가 다르다는 점과 함께, 메시지·RMF 대응은 미확인 유지; 제정 사실 자체는 기존 내용 확인(같은 페이지 ref-316, 2026-09-25-area10-s8 ref-317). KS B 7317 행에 개정 이력·적용 범위(f4·f5). SEMI E84 행 추가 또는 2026-09-25-area17-s7 41행 연결: E84-0823 현행판(f26), Doc7442 개발 제안(f27, 원문 미열람 [추정]). BACnet 출입통제 백서는 표준 변경 제안 작업 문서로(f35·f36) / 섹션 8(분리 2026-09-25-area10-s8) — '원문을 열지 못해 결과 수치는 쓰지 않는다' 문장 갱신: 병원 논문의 EOR 임계값 재보정 명시(f28, 새 내용), 공유 승강기 지연 독립 교차 확인(f30), Han 외는 실제 평면으로 거리 행렬만·수요는 무작위 표본·기본 대기 30초(f31), Kim 외 15층·소포 1·3·5·7(f32), 노주형 외 N1 5~9층 각 층 절반 영역·19/20(f33·f34). Park·Park 설계 기준 논문은 '초록 기준'으로(f1). 기존 내용 확인으로 넣지 않는 것: 병원 논문의 122건·실패 14건 분류(통신 2·막힘 8)·87.03%·59.01%·95.52%(objects-people-and-live-state/people-and-pedestrian-model.md 101~108행, 2026-09-29-area63-s4·s6·s8, design-and-simulation/virtual-commissioning-and-real-situation-replay.md, 2026-09-25-area03-s8), Han 외 승강기 운행 40~100초(planning-and-optimization/shared-resource-charging-and-energy-optimization.md 96~108행, 2026-09-25-area28-s3), 노주형 외 5개 층·27분·95%·버튼 조작(chat-based-configuration-and-operation/chat-map-authoring.md 113행, 2026-09-25-area06-s8, 2026-09-25-area21-s8) / 섹션 9 — 설비 제어 경계: 화재 복구·PLC 재시작은 연계 대상(설비), ROP 는 복구 책임자 지정과 시험(f22·f46); 출입통제는 문 열기 요청과 통행 권한 승인 분리(f36·f45) / 섹션 10(분리 2026-09-25-area10-s10) — 63. 병원·의료(f28·f30), 64. 상업 시설(f37·f1), 51. 인증·권한·격리(f35·f36·f45), 30. 로봇 간 협업·물리적 인계(f14~f16·f24~f27), 32. 예외 복구·재계획·업무 연속성(f22), 50. 안전 표준·인증·사고 조사(f4·f5) / 섹션 11(분리 2026-09-25-area10-s11) — 부분 근거만, 모두 열림 유지: oq-010(f28·f30~f34·f48), oq-041(f6~f10·f40), oq-283(f7 표준 번호 공개, 책임 분담은 미확인), oq-042(f24~f27·f47), oq-062(f26·f27), oq-043(f19·f20·f35·f36·f45), oq-098·oq-173·oq-311(f4·f5, 조항·기준값은 미확인), oq-067·oq-094(f11·f12, 배정 규칙 미구현), oq-215(f29, 분모 설명 없음 재확인 — 새 질문 아님), oq-258·oq-328(f28). 새 질문 6건. 넣지 않는 것: 외부 메모 F01(스마트도시협회 REEC 운영 사무국 — 기존 내용 확인: glossary/robot-friendly-building-certification.md, 2026-09-29-area64-s4 41행·s7 42행; 이번 원문은 접근 제한으로 미열람), F02(평가 분야 4개 명칭 — 확인 불가이고 기존 용어집의 4개 부문 명칭(건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스)과 충돌, 원문 재확보 필요). 다음 실행 후보: 64. 상업 시설(REEC 현행 심사 기준), 30. 로봇 간 협업·물리적 인계(OMRON·Doc7442 원문 재확보), 51. 인증·권한·격리(BACnet 출입통제). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- KS B 7317 의 2022-12-09 개정과 2025-05-09 개정은 각각 어떤 조항(요구사항·평가 방법)을 바꿨으며, 그 변경이 승강기 연동 계층이 확인해야 할 항목에 영향을 주는가? (관련 기존 질문: oq-098, oq-173, oq-311) | 관련 영역: 22. 설비·건물 시스템 연동, 50. 안전 표준·인증·사고 조사 | 근거: f4 | 종류: 일반
- 로봇 친화형 건축물 인증의 현행 심사 기준은 어느 판이며, 승강기·자동문·출입통제 연동 항목을 어떤 시험이나 서류로 심사하는가? (관련 기존 질문: oq-179) | 관련 영역: 22. 설비·건물 시스템 연동, 64. 상업 시설 | 근거: f1 | 종류: 일반
- KONE 의 현행 공식 승강기 API 계약(지원 승강기, 건물 등록, 권한 범위, 세션 유지 조건)은 2023년 고정판 공개 RMF 어댑터가 전제한 KONE API v2.0 연결 조건과 어떻게 다른가? | 관련 영역: 22. 설비·건물 시스템 연동, 20. 로봇·제조사 관제 연동 | 근거: f17 | 종류: 일반
- SEMI Doc 7442(E84 를 출발점으로 한 새 인계 인터페이스와 TCP/IP 하위 규격) 개발 제안은 승인 뒤 표준으로 발행됐는가, 반도체 밖 이동로봇–설비 인계에도 쓸 수 있는 범위인가? (관련 기존 질문: oq-042, oq-062) | 관련 영역: 22. 설비·건물 시스템 연동, 30. 로봇 간 협업·물리적 인계 | 근거: f27 | 종류: 일반
- HopeTechnik 승강기·문 연동 문서가 승강기 상태 전송 주기를 1 Hz 와 2초마다로 다르게 적은 것은 어느 쪽이 실제 구현·설정이며, 이런 주기 차이가 설비 상태를 믿을 수 있는 경과 시간 판단에 어떤 영향을 주는가? (관련 기존 질문: oq-034) | 관련 영역: 22. 설비·건물 시스템 연동, 18. 실시간 세계 상태·데이터 일관성 | 근거: f23 | 종류: 일반
- NAVER ARC 의 Tokyo Midtown Yaesu 도입에서 기존 화물 승강기·자동문 연동이 실제로 운영 중인 층·로봇 종류·제조사 범위는 어디까지이며, 공급자 밖의 독립 운영 평가가 있는가? | 관련 영역: 22. 설비·건물 시스템 연동, 64. 상업 시설 | 근거: f37 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 1
- 예산 사용량: 검색 0회 · 신규 출처 14건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-03/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f2·f3: 국토부 보도자료 원문(MOLIT·CODIL)을 열지 못해 사업기간 2025~2028, 보도 2025-05-28·배포 2025-05-27, '3쪽'은 미확인 — 2차 보도(ref-1484) 기준 [추정]
    - f1: Park·Park 논문은 초록·Crossref 서지만 확인(본문 미열람). 메모의 '현장실험이 아닌 기존 인증기준 비교' 중 '현장실험이 아닌'은 단정하지 않음. 메모 서지 '28,14' 는 28(1), 논문번호 14 로 정정
    - 메모 F01(스마트도시협회 REEC 운영 사무국)·F02(평가 분야 4개): 스마트도시협회 페이지가 접근 제한으로 열리지 않음. F02 명칭은 기존 용어집 4개 부문 명칭과 달라 충돌 — 원문 재확보 필요, 출처·finding 에서 뺌
    - f7: e-나라표준인증 목록의 등록일자(2026-03-24)와 KOLA 게시일(2026-03-27)이 다르며 정확한 제정일은 미확인. 가이드라인 본문의 메시지·상태 정의, Open-RMF 대응 미확인
    - f4·f5: KS B 7317 표준 본문·신구대비표 미열람 — 개정 조항 미확인
    - f24·f25: OMRON I680-E-02 PDF 접근 거부(Access Denied)로 원문 미열람 — 메모 서술만 근거라 [추정], 메모의 2023-05 판 날짜도 미검증
    - f27: SEMI Doc 7442 SNARF 페이지 봇 차단으로 원문 미열람 — 작성일 2025-12-17·승인일 2025-12-18 미검증, [추정]
    - 커밋 일자 4건(rmf_internal_msgs 2a7f01b 2026-09-22, rmf_ros2 4cea3fe 2026-10-08, KONE 어댑터 9bc3a87 2023-07-13, door_adapter_dormakaba 2cf76a6 2025-06-16)은 확인하지 못해 해당 출처 published 를 null 로 둠
    - f17·f18: KONE 어댑터 README 는 KABAM-Robotics 보존 저장소 판이며 원 저장소(sharp-rmf/kone-ros-api)와 현행 KONE 공식 API 계약은 대조하지 않음. The Galen 실기 시험은 프로젝트 자체 보고
    - f23: HopeTechnik 문서의 1 Hz/2초 차이를 설명하는 구현·설정 근거 없음. 문서 발행일 미확인
    - f29: 87.03% 의 분모는 원문으로 설명되지 않음(oq-215 열림 유지)
    - f37: NAVER Yaesu 운영 범위는 공급자 블로그뿐이며 독립 평가 없음(벤더 주장)
    - 메모 U06(현대엘리베이터 현행 API 원문)·U07(TTA 10.1486 본문)은 이번 메모에 근거 finding 이 없어 열린 질문으로 올리지 않음
    - 벤더 문서만 근거인 f21~f23 은 원문 대조로 문서 내용은 확인했으나, 저장소 규칙(6.2 항목 13)에 따라 독립 출처 교차 확인 전까지 vendor_claim: true·[추정]으로 둔다.
- 범위 경계 위반 의심:
    - f19·f21·f22: 문 구동기 하드웨어(IoT connector), 승강기 제어함 PLC·드라이 접점, 화재 경보 시 설비 복귀는 분류 원문 19장의 '승강기·컨베이어·PLC·설비 안전 제어' 연계 대상이므로 claim 을 '연계 대상: '으로 시작하고, ROP 몫은 요청·상태 확인과 복구 책임 정의(f46)로 한정
    - f4·f5·f39: KS B 7317 은 로봇 자체의 탑승 안전 요구사항으로 이 영역에는 제약 조건·판 정보로만 씀(48·50번 안전 영역 쪽 내용)
    - f35·f36·f45: BACnet 출입통제의 권한 검사는 51. 인증·권한·격리 쪽 내용이 많아 이 영역에는 문 열기 요청과 통행 승인 분리 근거로만 씀
    - f26·f27·f47: SEMI E84·Doc7442 는 반도체 업종 규격으로 이 영역에는 인계 신호 구조의 참고로만 쓰고 물류센터 적용을 주장하지 않음
    - f28~f30: 병원 승강기 연구의 수치는 63. 병원·의료에서 이미 다루므로 이 영역에는 새 내용(재보정 명시·지연 교차 확인·분모 재확인)만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 14건/15(ref-1483~ref-1496, 예약 구간 ref-1483~ref-1512 안), 재사용 8건(ref-322·ref-314·ref-1398·ref-202·ref-943·ref-103·ref-321·ref-163). 출처 매핑(검증 결과 기준): 메모 n2→ref-1483, n3→ref-322(같은 국토부 보도자료, 기존 제목·URL 유지)+2차 보도 ref-1484, n4→ref-314(e-나라표준인증 상세로 열람, 발행일을 현행 개정일 2025-05-09 로 갱신), n5→ref-1485, KOLA 표준 번호→e-나라표준인증 단체표준 목록 ref-1486, n7→CHANGELOG ref-1398·lift_supervisor ref-1488·DispenseItem ref-1489, n8→ref-1487, n9→ref-1490, n10→ref-1491, n11→ref-1492, n12→ref-1493(미열람), n13→ref-202, n14→ref-1494(미열람), n15→ref-943, n16→ref-103, n17→ref-321, n18→ref-163, n19→ref-1495, n20→ref-1496. n1(스마트도시협회)은 근거 finding 이 기존 내용 중복(F01)·충돌(F02)이라 출처에서 뺐고, n6(rmf_internal_msgs: ref-286·ref-499·ref-049)은 근거 finding 이 기존 내용 중복(LiftState session_id 정의, 결과 상태값 정의)이라 넣지 않음. 기존 ref 갱신 제안: ref-103 저자(Han, L. 외)·발행일 2025-03-13, ref-321 저자(Kim, S. 외)·발행일 2025-02-28, ref-163 발행일 2026-03·권호 21(1), ref-314 발행일 2025-05-09·이력, ref-202 현행판 E84-0823. fetched: true 는 검증 서브에이전트가 2026-10-11 원문을 내려받아 대조한 출처이고, fetched: false 는 ref-322·ref-1493·ref-1494. ref-1483 은 초록·서지만 확인. 교차 확인 1건(f30: 고려대 구로병원·도구공간 논문과 KAIST 논문, 서로 다른 기관의 질적 관찰). 메모 X01 외 나머지는 단일 출처라 신뢰도 medium 이하. 벤더 주장은 f37(vendor_claim, [추정]). 현장 유형: 병원(f28·f29), 기타(도서관, f21~f23), 상업 시설(f37). 물류창고 실측 자료는 이번에도 없음(oq-010 열림). 열린 질문 해결 제안 없음 — 모두 부분 근거: oq-010 근거 f28·f30~f34·f48, oq-041 근거 f6~f10·f40, oq-283 근거 f7, oq-042 근거 f24~f27·f47, oq-062 근거 f26·f27, oq-043 근거 f19·f20·f35·f36·f45, oq-098·oq-173·oq-311 근거 f4·f5, oq-067·oq-094 근거 f11·f12, oq-215 근거 f29, oq-258·oq-328 근거 f28. 메모의 '새1~새3'은 고유 id 가 없는 질문이 아니라 docs/open-questions.md 의 oq-041·oq-042·oq-043 과 같은 질문임을 질문 문장으로 확인했다. 메모 U01=oq-010, U02=oq-041·oq-283, U09=oq-042, U10=oq-043, U13=oq-215 이므로 새로 만들지 않았다. 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 실제 위키 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-10/research.md

```markdown
# 리서치 브리프 2026-09-30-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-10 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 49. 사람 근접 안전 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 속도·분리 감시(SSM), 동력·힘 제한(PFL), 보호 분리 거리, 운용 구역, 속도 제한·진입 금지 구역, 움직임 지도(Maps of Dynamics) 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·실외·제조 공장 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 인지형 배정·교통 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙 제223조, VDA 5050 구역, Nav2 Collision Monitor 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
2. 로봇과 사람 사이의 분리 거리는 표준에서 어떤 변수(사람 속도, 반응 시간, 정지 거리, 측정 불확실도)로 계산하며, 실제 구현에서 어떤 한계가 보고되는가? (섹션 4·6·8 겨냥)
3. 이동 로봇·협동로봇·실외 로봇의 사람 근접 안전을 다루는 국내외 표준·법규·인증(ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙)은 구역·속도·감지·정지를 어떻게 규정하는가? (섹션 7 겨냥, 한국 자료 우선)
4. 구역별 속도 제한과 진입 금지를 플릿 관제 수준에서 표현·전달하는 인터페이스와 오픈소스(VDA 5050 구역, Nav2 Collision Monitor 등)는 무엇이며 안전 기능으로 인정되는가? (섹션 6·7·9 겨냥)
5. 물류창고·병원·실외·상업 시설 같은 현장에서 사람 근접 시 감속·정지·양보를 적용한 사례와 그 속도 기준은 무엇인가? (섹션 5 겨냥)
6. 안전 거리와 별개로 사람이 편안하게 느끼는 거리·속도, 사람의 움직임을 배정·교통에 반영하는 연구는 무엇을 보고하는가? (섹션 6·8 겨냥)
7. 사람 근접 안전에서 ROP가 직접 맡을 것과 로봇 제조사·시스템 통합자·설비에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Marvel·Norcross(NIST, Robotics and Computer-Integrated Manufacturing)는 ISO/TS 15066 의 속도·분리 감시(SSM)에서 보호 분리 거리가 사람 이동 속도, 로봇 반응 시간, 로봇 정지 시간(정지 거리), 침입 거리, 로봇·사람 위치 측정 불확실도로 계산되며, 분리 거리가 이 값 이하가 되면 안전 감시 정지를 건다고 정리했다. | ref-1075 | 아니오 | medium | 2016 | 제약 | — |
| f2 | [사실] | 같은 연구는 사람 속도로 ISO 13855 의 1,600 mm/s(최악 조건 2,000 mm/s), 침입 거리로 ISO 13855 기준 850~1,200 mm 를 들고, NIST 시험에서 레일 장착 로봇의 반응 시간을 약 0.113초로 측정했다고 보고했다. | ref-1075 | 아니오 | medium | 2016 | 제약 | — |
| f3 | [사실] | 같은 연구는 SSM 식이 속도의 방향을 무시하고 크기만 써서 멀어지는 로봇도 불필요한 정지를 일으킬 수 있고, 센서 잡음이 속도 추정 오차를 키우며, 갱신 주기가 낮을수록 로봇 평균 속도가 떨어지고, 보호 거리는 주로 로봇 제동 거리와 반응 시간이 좌우한다고 보고했다. | ref-1075 | 아니오 | medium | 2016 | 예외·성과 | — |
| f4 | [사실] | Hartmann 외(arXiv 2602.17822, 2026-02)는 ISO 10218-1/2 의 2025년 개정판이 협동 작업 기술 시방서 ISO/TS 15066 을 선택적 지침에서 규범적 요구로 본문에 통합하고, 로봇·협동 적용의 새 분류와 사이버보안 요구를 더했다고 분석했다. | ref-1076 | 아니오 | medium | 2026-02 | — | — |
| f5 | [사실] | 국내 산업안전보건기준에 관한 규칙 제223조는 산업용 로봇 운전 중 위험 방지를 위해 높이 1.8미터 이상의 울타리와 안전매트 설치를 기본으로 하되 2016년부터 한국산업표준 등 안전기준에 맞는 협동 운전 로봇은 울타리 설치를 면제하며, 협동 작업 방식은 속도·분리 감시(SSM), 핸드 가이딩(HGC), 동력·힘 제한(PFL)으로 나뉜다고 지디넷코리아가 전했다. | ref-1082 | 아니오 | low | 2024-03 | 제약 | — |
| f6 | [추정] | ISO 3691-4:2023(무인 산업용 트럭과 그 시스템의 안전 요구·검증)은 사람이 있는 운용 구역에서는 인력 감지를 요구하고, 훈련된 인원만 들어가는 제한 구역과 울타리 등으로 사람을 배제한 구역을 구분해 구역에 따라 보호 조치를 달리하는 것으로 알려져 있다. | ref-470 | 아니오 | low | 2023 | 제약 | 원문 미열람 |
| f7 | [추정] | 같은 표준은 인력 감지를 끄거나 완전히 작동하지 않는 상황(예: 도킹)에서 속도를 0.3 m/s 이하로 제한하고, 인력 감지 성능을 서 있는 사람(지름 200 mm·높이 600 mm 원통)과 누운 사람(지름 70 mm·길이 400 mm 원통) 시험편으로 확인하는 것으로 알려져 있다. | ref-470 | 아니오 | low | 2023 | 제약 | 원문 미열람 |
| f8 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR)을 특정 적용과 현장에 맞춰 통합·배치할 때의 안전 요구를 다루며, 배치 시스템의 위험성 평가는 IMR 시스템 통합자가 수행하도록 하고 모바일 매니퓰레이터와 잔여 위험, 최종 사용자 정보·교육을 포함한다고 The Robot Report 가 전했다. | ref-1088 | 아니오 | low | 2023-10-26 | — | — |
| f9 | [사실] | 한국로봇산업진흥원의 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거해 배송 등 목적의 자율주행·원격제어 로봇과 관제장치의 조합을 대상으로 최고 속도 15 km/h 이하·최대 질량 500 kg 이하를 요구하고, 주변 인식·비상정지·횡단보도 통행·관제장치 등을 심사하며 2년 주기 정기점검을 둔다. | ref-980, ref-992 | 예 | high | 2026-09-30 | 실외 / 제약 | — |
| f10 | [사실] | 지디넷코리아(2023-07-28)는 산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준이 로봇과 적재물 질량 합계에 따라 최고 속도를 230 kg 초과 5 km/h, 100 kg 초과 10 km/h, 그 이하 15 km/h 로 나누고, 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단하게 하며 심사 항목을 16가지로 두었다고 전했다. | ref-992 | 아니오 | medium | 2023-07-28 | 실외 / 제약 | — |
| f11 | [사실] | VDA 5050 3.0.0 은 플릿 관제가 이동 로봇에 전달하는 구역 유형으로 진입 금지(BLOCKED), 플릿 관제 승인 후 진입(RELEASE), 최고 속도 제한(SPEED_LIMIT), 자율 재계획 금지, 동작 유발, 우선·벌점·방향 구역을 정의하며, 속도 제한 구역에서는 로봇이 정해진 최고 속도보다 빠르게 달려서는 안 된다고 규정한다. | ref-031 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f12 | [사실] | VDA 5050 3.0.0 은 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 밝혀, 구역·속도 제한 전달이 안전 기능 자체를 대신하지 않음을 명시한다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | ROS 2 내비게이션 스택 Nav2 의 Collision Monitor 는 컨트롤러 속도 명령을 거르는 독립 노드로, 영역 안 장애물 점 수에 따른 정지·감속(비율)·속도 제한과 충돌까지 남은 시간 기반 접근 모델을 두고 여러 영역이 동시에 걸리면 가장 강한 조치를 쓰지만, 하드 실시간 안전 인증을 제공하지 않아 안전 등급 하드웨어를 대신하지 않는다고 밝힌다. | ref-1078 | 아니오 | medium | 2026-09-30 | 예외·성과 | — |
| f14 | [추정] | 아마존은 풀필먼트 센터에서 로봇 구역에 들어가는 직원이 로보틱스 테크 조끼를 착용·활성화하면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명한다. | ref-1084 | 아니오 | low | 2026-09-30 | 물류창고 / 제약 | 벤더 주장 |
| f15 | [사실] | Francis 외 52명(ACM Transactions on Human-Robot Interaction, arXiv 2306.16740)은 사회적 로봇 주행의 원칙을 안전·편안함·가독성·예의·사회적 역량·상대 이해·능동성·맥락 적합성 8가지로 정하고, 알고리즘을 공정하게 비교하기 위한 지표·시나리오·벤치마크·시뮬레이터 지침을 제시했다. | ref-1083 | 아니오 | medium | 2023-09 | — | — |
| f16 | [사실] | Jafari·Nguyen·Liu(arXiv 2604.13677, 2026-04)는 이동 로봇과 자원 보행자의 일대일 조우 실험에서 보행자가 보고한 편안함이 최소 거리와 최소 예상 충돌 시간 같은 운동학 변수와 중간 정도의 유의한 상관을 보였고, 이들을 합친 복합 지표가 오즈비 3.67 로 가장 잘 예측했다고 보고했다. | ref-1089 | 아니오 | medium | 2026-04 | 제약 | — |
| f17 | [사실] | Rondoni 외(Scientific Reports, 2024-08)는 병원 물류용 HOSBOT 과 TIAGo 를 시뮬레이션 병원 환경에서 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 속도가 높을수록 정확도가 떨어졌다고 보고했다. | ref-1085 | 아니오 | medium | 2024-08-07 | 병원 / 제약 | — |
| f18 | [사실] | Farrell 외(UC San Diego, arXiv 2503.21141, 2025-03)는 학습 기반 제어 장벽 함수(CBF)를 Open-RMF 에 통합해 창고의 다중 로봇·다중 행위자 상황에서 보행자를 포함한 정적·동적 장애물을 피하는 안전 강화 제어를 제안하고 로봇 수·속도·장애물 수를 바꿔 평가했다. | ref-1086 | 아니오 | medium | 2025-03-27 | 물류창고 | — |
| f19 | [사실] | Kazemi Eskeri 외(IROS 2025)의 사람 인지형 작업 배정(HATA)은 과거 사람 이동 패턴을 담은 시공간 질의형 움직임 지도(Maps of Dynamics)로 사람이 작업 실행 시간에 주는 영향을 확률적 비용으로 추정해 배정에 반영했고, 사람 움직임을 고려하지 않는 기준선보다 임무 완료 시간을 26%, 기존 기준선보다 19% 줄였다고 보고했다. | ref-1087 | 아니오 | medium | 2025-08-27 | 수행 자원 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에 대해, 분리 거리는 고정값이 아니라 사람 속도·반응 시간·정지 거리·측정 불확실도로 그때그때 계산되고(f1~f3), 감속·정지 기준은 적용 유형별 표준·인증이 구역·속도 상한으로 정하며(f6·f7·f9·f10), 사람이 편안하게 느끼는 거리·충돌 시간은 안전 정지 거리와 별도의 기준이 필요한 것으로 보인다(f15·f16). | ref-1075, ref-470, ref-980, ref-992, ref-1083, ref-1089 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 안전 거리가 로봇 정지 성능과 센서 갱신에 따라 달라져 로봇·현장마다 다르고(f1~f3), 협동로봇·무인 트럭·실외 로봇이 각기 다른 표준·법규로 울타리 면제·구역·속도 상한을 정하며(f4~f10), 보수적인 감속·정지가 처리량과 수용성에 영향을 주기 때문이다(f3·f16·f19). | ref-1075, ref-1076, ref-1082, ref-470, ref-1088, ref-980, ref-992, ref-1089, ref-1087 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 49. 사람 근접 안전에서 ROP가 직접 맡을 범위는 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하는 것(f11), 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하는 것(f14·f18·f19), 그 조정과 정지·재개 이력을 기록하는 것이며, 이는 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다(f12·f13). | ref-031, ref-1084, ref-1086, ref-1087, ref-1078 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(f1·f5·f6·f7)은 로봇 제조사와 시스템 통합자에, 현장 배치의 위험성 평가(f8)는 시스템 통합자에, 울타리·안전매트·인터록(f5)은 설비 안전 쪽에, 실외 인증 대상인 로봇·관제장치 조합의 적합성(f9)은 운영 사업자에 속하므로, ROP 는 그 설정값과 상태를 받아 계획에 반영하는 인터페이스를 맡을 것으로 보인다. | ref-1075, ref-1082, ref-470, ref-1088, ref-980 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 이 영역은 위험성 평가·정지·재개의 48. 안전·위험 관리(f8), 표준·인증의 50. 안전 표준·인증·사고 조사(f4~f10), 사람 이동 모델의 19. 사람·보행자 모델(f16·f19), 구역을 담는 16. 장소 의미·지도 관리(f11), 구역을 전달하는 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f11·f12), 사람 인지형 배정의 25. 작업 배정 — MRTA(f19), 구역·속도를 반영하는 27. 다중 로봇 경로·교통 관리 — MAPF(f11·f18), 협동 작업의 31. 사람–로봇 협업(f1·f5), 법규의 59. 법·규제·보험·라이선스(f5·f9), 수용성의 60. 노동·수용성·접근성(f15·f16), 평가의 54. 시험·형식 검증·벤치마크(f15·f17), 적용 현장인 61. 물류창고(f14·f18)·63. 병원·의료(f17)·66. 실외(f9·f10)와 이어진다. | ref-1088, ref-1076, ref-980, ref-1089, ref-1087, ref-031, ref-1086, ref-1075, ref-1082, ref-1083, ref-1085, ref-1084 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2016 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 아니오 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2602.17822 | 아니오 |
| ref-470 | ISO (ISO/TC 110) | ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems (제목 일부는 검색 결과 기준) | 2023 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/83545.html | 예 |
| ref-1078 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md | 아니오 |
| ref-031 | VDA / VDMA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0) | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부는 검색 결과 기준) | 2023-07-28 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1082 | 지디넷코리아 | "협동로봇 충돌 안전 계산하고 써야죠" | 2024-03 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240305160245 | 아니오 |
| ref-1083 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2306.16740 | 아니오 |
| ref-1084 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 아니오 |
| ref-1085 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 아니오 |
| ref-1086 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2503.21141 | 아니오 |
| ref-1087 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-1088 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | low | 2026-09-30 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 아니오 |
| ref-1089 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2604.13677 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/human-proximity-safety.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(왜 중요한가), f20(핵심 질문 답, 추정) / 섹션 4: 속도·분리 감시·보호 분리 거리 f1·f2, 동력·힘 제한 f5, 운용 구역 f6, 속도 제한·진입 금지·승인 구역 f11, 움직임 지도 f19, 제어 장벽 함수 f18, 사회적 주행 원칙 f15 / 섹션 5: 물류창고 — f14(제약: 조끼 신호로 감속·우회·정지, 벤더 주장 병기)·f18(연구, 창고 시나리오), 병원 — f17(제약: 보행 속도 기반 0.2~1.0 m/s, 시뮬레이션 병원임을 명시), 실외 — f9·f10(제약: 15 km/h·질량별 속도 상한·횡단보도 대기). 제조 공장은 f5(산업용 로봇 사업장 규정)로 서술하되 현장 사례가 아님을 밝히고, 상업 시설·가정·기타 사례는 찾지 못함을 명시 / 섹션 6: 계산형 보호 거리 f1~f3, 로봇 측 감속·정지 영역 f13, 플릿 수준 구역·속도 제한 f11·f12, 착용형 신호 f14, 사람 인지형 배정·교통 f18·f19, 편안함 지표 f16 / 섹션 7: ISO 10218·ISO/TS 15066 f4, ISO 3691-4 f6·f7(원문 미열람), ANSI/A3 R15.08-2 f8, 실외이동로봇 운행안전인증 f9·f10, 산업안전보건기준에 관한 규칙 제223조 f5, VDA 5050 구역 f11·f12, Nav2 Collision Monitor f13 / 섹션 8: f1·f3·f15·f16·f17·f18·f19·f4 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 16, 19, 20, 21, 25, 27, 31, 48, 50, 54, 59, 60, 61, 63, 66 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 50. 안전 표준·인증·사고 조사 페이지 섹션 7 에 f4·f6~f10 반영, 16. 장소 의미·지도 관리 페이지에 f11 구역 유형 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 속도·분리 감시 | Speed and Separation Monitoring (SSM) | 로봇과 사람의 거리와 속도를 계속 감시해 분리 거리가 보호 분리 거리보다 작아지기 전에 로봇을 감속하거나 정지시키는 협동 작업 방식이다. |
| 보호 분리 거리 | Protective Separation Distance | 사람 이동 속도, 로봇 반응·정지 시간, 침입 거리, 위치 측정 불확실도로 계산하는, 로봇이 사람에 닿기 전에 멈출 수 있도록 유지해야 하는 최소 거리다. |
| 동력·힘 제한 | Power and Force Limiting (PFL) | 로봇이 사람과 접촉하더라도 해를 주지 않도록 동력과 힘을 정해진 한계 안으로 제한해 작동시키는 협동 작업 방식이다. |
| 움직임 지도 | Maps of Dynamics (MoD) | 과거 사람 이동을 장소와 시간에 따라 모아 특정 위치·시각의 이동 방향과 흐름을 질의할 수 있게 만든 시공간 지도다. |
| 제어 장벽 함수 | Control Barrier Function (CBF) | 로봇 상태가 안전 집합 밖으로 나가지 않도록 제어 입력에 제약을 거는 함수로, 기존 제어 명령을 안전 쪽으로 걸러 내는 데 쓴다. |

## 열린 질문

새로 생긴 질문:

- 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? | 관련 영역: 49. 사람 근접 안전, 48. 안전·위험 관리 | 근거: f12 | 종류: 일반
- 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? | 관련 영역: 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사 | 근거: f10 | 종류: 출처 충돌
- 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? | 관련 영역: 49. 사람 근접 안전, 59. 법·규제·보험·라이선스 | 근거: f9 | 종류: 일반
- 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 21. 상호운용 표준·적합성 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 13회 · 신규 출처 15건
- 미확인 항목:
    - f6·f7 ISO 3691-4:2023 의 구역 구분, 감지 무효화 시 0.3 m/s, 시험편 치수: ISO·ANSI 블로그 페이지 403 으로 원문 미열람, 검색 결과 요약 기준이라 추정·low 로 둠
    - f5 산업안전보건기준에 관한 규칙 제223조 조문: law.go.kr 페이지에서 조문 본문을 읽지 못했고 yeslaw 는 인증서 오류로 열지 못해 기사(ref-1082)만 근거
    - f8 ANSI/A3 R15.08-2 원문 미열람(유료). 플릿(IMRF) 포함 여부는 검색 요약에만 있어 claim 에 넣지 않음
    - f14 아마존 조끼: 2018년 25개 창고 도입 등 수치는 검색 요약(위키백과)에만 있어 넣지 않음. 독립 출처 교차 확인 실패
    - f15 근접학 거리(0.45 m·1.2 m) 예시는 검색 요약에만 있어 넣지 않음
    - f16 실험 장소·참가자 수, f18 정량 결과, f19 실험 환경은 초록에 없어 미확인
    - f10 심사 항목 16가지와 f9 인증기관 페이지 8개 항목의 차이: 출처 충돌로 열린 질문에 올림
    - ISO 13482(개인 돌봄 로봇) 개정판 내용: 검색 1회에서 2025년 개정 세부를 확인하지 못해 넣지 않음
    - 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례는 찾지 못함(쇼핑몰·공항 검색 1회, 찾은 소매점 배치 연구 arXiv 2601.01946 은 근접 안전 내용이 없어 제외)
    - 제조 공장 현장 사례는 규정(f5)과 작업셀 연구(f1~f3)만 있고 현장 유형을 밝힌 적용 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1~f3·f5~f7: 안전 등급 인력 감지·보호 정지·SSM·PFL 은 로봇 제조사·시스템 통합자의 안전 기능(원문 19장 로봇 자체 지능·제어, 설비 안전 제어 연계 대상)이므로 개념·기준 근거로만 쓰고 f23 에서 '연계 대상: '으로 구분함
    - f13: Nav2 Collision Monitor 는 로봇 측 로컬 회피 계층(연계 대상)이며 안전 인증이 없음을 명시; ROP 직접 범위로 서술하지 않도록 주의
    - f9·f10: 실외이동로봇 인증 대상은 로봇과 관제장치의 조합이라 관제장치 쪽이 ROP 범위와 겹칠 수 있음. 인증 책임은 운영 사업자 몫으로 f23 에서 구분
    - f18: 제어 장벽 함수는 로봇 제어 계층 기법이지만 Open-RMF 플릿 계층에 통합한 사례로만 인용
- 한계: web_fetch_available: true · fetch_mode full. 검색 13회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 ISO 13482·ISO 13855 원문, 상업 시설·가정 사례, 국내 서비스 로봇 기준을 더 넣지 못했다. 주의: 입력의 이전 브리프 2026-09-30-08 도 ref-1075~ref-1089 를 썼으나 실행 컨텍스트가 이 구간을 이 실행 전용으로 예약했다고 밝혀 그대로 썼다(퍼블리셔의 id 충돌 확인 필요). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건; VDA 5050·ISO 3691-4 가 기존 참고문헌에 있으면 퍼블리셔가 같은 URL 로 합쳐야 한다). 원문 열람: 14건 열었고(webfetch 12건, github_raw 2건) ISO 3691-4(ref-470)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Marvel·Norcross(ref-1075)·Rondoni 외(ref-1085)는 PMC 본문, 나머지는 초록 페이지다. 교차 확인 1건(f9: 15 km/h·500 kg 을 인증기관 페이지와 기사로 확인). 벤더 문서는 아마존(ref-1084) 1건이며 f14 는 vendor_claim·추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에는 f20 으로 답했고 결론은 '분리 거리는 계산값이고, 감속·정지 상한은 적용 유형별 표준·인증이 구역·속도로 정하며, 편안함 기준은 별도'라는 추정이다. 현장 유형 사례는 물류창고(f14·f18)·병원(f17, 시뮬레이션)·실외(f9·f10)이며 제조 공장은 규정 수준, 상업 시설·가정·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-980)·지디넷코리아 2건(ref-992·ref-1082)이다. 용어집에 이미 있는 운용 구역·구역 집합·위험성평가·협동 적용·실외이동로봇 운행안전인증·공공 영역 이동로봇·필터 마스크·해제 구역은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
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

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope

action type | counter action | description | idempotent | parameters | linked state | instant | node | edge | zone
---|---|---|---|---|---|---|---|---|---
startPause | stopPause | Activates the pause mode. <br>A linked state is required, because many mobile robots can be paused by using a hardware switch. <br>No more automatic driving - reaching next node is not necessary. Actions that can be paused (`pauseAllowed`=`true`), shall be paused, other actions continue. Order execution is resumed after stopPause. | yes | - | paused | yes | no | no | no
stopPause | startPause | Deactivates the pause mode. <br>Movement and all other actions will be resumed (if any). <br>A linked state is required because many mobile robots can be paused by using a hardware switch. <br>stopPause can also restart mobile robots that were stopped with a hardware button that triggered startPause (if configured). | yes | - | paused | yes | no | no | no
startHibernation | stopHibernation | Initiates hibernate mode, in which the mobile robot shall remain connected to the MQTT broker but no longer needs to send state messages. The mobile robot shall report this action as 'FINISHED' before discontinuing publishing state messages and publish a connection state of 'HIBERNATING'. If the mobile robot has an active order, it shall clear it. Reaching the next node is not required.<br>While in 'HIBERNATING' connection state, mobile robot shall not be moving. The mobile robot shall only receive and respond to the instant action 'stopHibernation' and shall not respond to any other commands, such as orders or additional instant actions. <br>If the mobile robot's battery becomes critically low while in this mode, the mobile robot may stop 'HIBERNATING' autonomously to report an error. In case a wake‑up time is set, the mobile robot is able to autonomously exit the 'HIBERNATING' connection state at the specified time and will publish the corresponding connection state transition before resuming normal operation. | yes | wakeUpTime (string, optional) | - | yes | no | no
stopHibernation | startHibernation | Ends hibernate mode. To initiate wake‑up while the mobile robot is in the 'HIBERNATING' state, a control device (onboard or external) shall subscribe to the `instantAction` topic and remain connected to the MQTT broker. Because the mobile robots standard control device may be partially shut down during hibernation, the wake‑up may be triggered by a distinct MQTT client (separate from the mobile robots usual communication client).<br>Upon success, the mobile robot shall publish the connection state ONLINE.| yes | - | - | yes | no | no
shutdown | - | Initiates a coordinated shutdown of the mobile robot, where it disconnects from the MQTT broker. The execution of the shutdown action requires the mobile robot to be in an idle state. There is no way using the VDA 5050 protocol to automatically restart due to the connection being terminated.<br>If a mobile robot is in hibernate mode but should be shut down, it shall first exit hibernation (via stopHibernation) before executing shutdown.| yes | - | - | yes | no | no | no
startCharging | stopCharging | Activates the charging process. <br>Charging can be done on a charging spot (mobile robot stopped) or on a charging lane (while driving). <br>Protection against overcharging is the responsibility of the mobile robot. | yes | - | powerSupply.charging | yes | yes | no | no
stopCharging | startCharging | Discontinues the charging process. <br>The charging process can also be interrupted by the mobile robot or the charging station, e.g., if the battery is full. | yes | - | powerSupply.charging | yes | yes | no | no
initializePosition | - | Resets (overrides) the pose of the mobile robot with the given parameters. | yes | x (float64)<br>y (float64)<br>theta (float64)<br>mapId (string)<br>lastNodeId (string) | mobileRobotPosition.x<br>mobileRobotPosition.y<br>mobileRobotPosition.theta<br>mobileRobotPosition.mapId<br>lastNodeId<br> maps | yes | yes<br>(Elevator) | no | no
enableMap | - | Enable a previously downloaded map explicitly to be used in orders without initializing a new position. | yes | mapId (string)<br>mapVersion (string) | maps | yes | yes | no | no
downloadMap | - | Trigger the download of a new map. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the map for use and setting the map in the state. | yes | mapId (string)<br>mapVersion (string)<br>mapDownloadLink (string)<br>mapHash (string, optional) | maps | yes | no | no | no
deleteMap | - | Trigger the removal of a map from the mobile robot's memory. | yes | mapId (string)<br>mapVersion (string) | maps | yes | no | no | no
downloadZoneSet | - | Trigger the download of a zone set. Active during the download. Errors reported in mobile robot state. Finished after verifying the successful download, preparing the zone set for use and setting the zone set in the state. | yes | zoneSetId (string)<br>zoneSetDownloadLink (string)<br>zoneSetHash (string, optional) | zoneSets | yes | no | no | no
enableZoneSet | - | Enable a previously downloaded zone set explicitly to be used in orders. | yes | zoneSetId (string)<br> | zoneSets | yes | yes | no | no
deleteZoneSet | - | Trigger the removal of a zone set from the mobile robot's memory. | yes | zoneSetId (string) | zoneSets | yes | no | no | no
clearInstantActions | - | Removes all finished or failed instant actions from the mobile robot state. | yes | - | instantActionStates | yes | yes | no | no
clearZoneActions | - | Removes all finished or failed zone actions from the mobile robot's state. | yes | - | zoneActionStates | yes | yes | no | no
stateRequest | - | Requests the mobile robot to send a new state message. | yes | - | - | yes | no | no | no
logReport | - | Requests the mobile robot to generate and store a log report. | yes | reason<br>(string) | - | yes | no | no | no
pick | drop<br><br>(if automated) | Request the mobile robot to pick a load. <br>Mobile robots with multiple load handling devices can process multiple pick operations in parallel. <br>In this case, the parameter lhd needs to be present (e.g., LHD1). <br>The parameter stationType informs how the pick operation is handled in detail (e.g., floor location, rack location, passive conveyor, active conveyor, etc.). <br>The load type informs about the load unit and can be used to switch field for example (e.g., EPAL, INDU, etc). <br>For preparing the load handling device (e.g., pre-lift operations based on the height parameter), the action could be announced in the horizon in advance. <br>But, pre-Lift operations, etc., are not reported as 'RUNNING' in the mobile robot state, because the associated node is not released yet.<br>If on an edge, the mobile robot can use its sensing device to detect the position for picking the node. | no |lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional) <br>loadId (string, optional)<br>height (float64, optional)<br>defines bottom of the load related to the floor<br>depth (float64, optional) for forklifts<br>side (string, optional) e.g., conveyor | .load | no | yes | yes | no
drop | pick<br><br>(if automated) | Request the mobile robot to drop a load. <br>See action pick for more details. | no | lhd (string, optional)<br>stationType (string, optional)<br>stationName (string, optional)<br>loadType (string, optional)<br>loadId (string, optional)<br>height (float64, optional)<br>depth (float64, optional) <br>… | .load | no | yes | yes | no
detectObject | - | Mobile robot detects object (e.g., load, charging spot, free parking position). | yes | objectType (string, optional) | - | no | yes | yes | yes
finePositioning | - | On a node, mobile robot will position exactly on a target.<br>The mobile robot is allowed to deviate from its node position.<br>On an edge, the mobile robot will e.g., align on stationary equipment while traversing an edge. | yes | stationType (string, optional)<br>stationName (string, optional) | - | no | yes | yes | yes
waitForTrigger | - | Mobile robot shall wait for a trigger of the type defined specified in the triggerType parameter, which is an array of strings. Two predefined values shall be used when semantically appropriate: 'FLEET_CONTROL' if the trigger originates from the fleet control, and 'LOCAL' if the trigger comes from an input on the mobile robot (e.g., button press, manual loading). If none of the predefined values meet the specific requirements, custom values can be defined. <br>Fleet control is responsible for handling the timeout and shall cancel the order if necessary. | yes | triggerType [string] (array) | - | no | yes | no | yes
trigger | - | Fleet control system notifies the mobile robot that a waitForTrigger action has been released. Typically, this occurs when the fleet control system receives information from a third-party system indicating that the process the mobile robot was waiting for has completed. | yes | - | - | yes | no | no | no
retry | - | Mobile robot retries action defined via actionId that is currently in state RETRIABLE. | yes | actionId (string) | - | yes | no | no | no
skipRetry | - | Mobile robot shall skip the action defined via actionId that is currently in state RETRIABLE, setting action to FAILED. | yes | actionId (string) | - | yes | no | no | no
cancelOrder | - | Mobile robot stops as soon as possible. This could be immediately or on the next node. See Chapter 6.1.3 Order cancellation. | yes | orderId (string, optional) | - | yes | no | no | no
factsheetRequest | - | Requests the mobile robot to send a factsheet | yes | - | - | yes | no | no | no
updateCertificate | - | Request the mobile robot to download and activate a new certificate set, the service parameter is an extensible enum with the predefined parameter 'MQTT' to be used for mqtt connection. | yes | service (string)<br>keyDownloadLink (string)<br>certificateDownloadLink (string)<br>certificateAuthorityDownloadLink (string, optional) | - | yes | no | no | no

>Table 4 - Predefined actions and their scope (instant, node, edge, zone)

#### 6.2.3.2 Action states

action type | 'INITIALIZING' | 'RUNNING' | 'PAUSED' | 'FINISHED' | 'FAILED' | 'RETRIABLE'
---|---|---|---|---|---|---
startPause | - | Activation of the mode is in preparation.<br>If the mobile robot supports an instant transition, this state can be omitted. | - | Mobile robot is not moving. <br>All pauseable actions are paused. <br> The pause mode has been activated. <br>The mobile robot reports paused: "true". | The pause mode cannot be activated for some reason (e.g., overridden by hardware switch).
stopPause | - | Deactivation of the mode is in preparation. <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pause mode has been deactivated. <br>All paused actions are resumed. <br>The mobile robot reports paused: "false". | The pause mode cannot be deactivated for some reason (e.g., overridden by hardware switch). | -
startHibernation | - | Activation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The active order has been cleared, if any. No state messages are sent by the mobile robot. <br>Hibernate mode has been activated. The mobile robot reports connection state "HIBERNATING".| The HIBERNATING connection state could not be published (e.g., overridden by a hardware switch).| -
stopHibernation | - | Deactivation of the hibernate mode is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Hibernate mode has been deactivated.<br>The mobile robot reports connectionState "ONLINE".| The hibernate mode could not be deactivated (e.g., overridden by a hardware switch).| -
shutdown | - | Activation of the OFFLINE connection state is in preparation. If the mobile robot supports an instant transition, this state can be omitted.| - | Mobile robot is not moving. The connection between mobile robot and broker is terminated in a coordinated way.<br>The mobile robot reports connection state "OFFLINE".| The shutdown cannot be executed for some reason (e.g., mobile robot is not in idle state, overridden by a hardware switch).| -
startCharging | - | Activation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been started. <br>The mobile robot reports powerSupply.charging: "true". | The charging process could not be started for some reason (e.g., not aligned to charger). Charging problems should correspond with an error. | The charging process could not be initiated. The mobile robot is waiting for intervention from fleet control or an operator.
stopCharging | - | Deactivation of the charging process is in progress (communication with charger is running). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The charging process has been stopped. <br>The mobile robot reports powerSupply.charging: "false" | The charging process could not be stopped for some reason (e.g., not aligned to charger).<br> Charging problems should correspond with an error. | -
initializePosition | - | Initializing of the new pose in progress (confidence checks, etc.). <br>If the mobile robot supports an instant transition, this state can be omitted. | - | The pose has been reset. <br>The mobile robot reports <br>mobileRobotPosition.x = x, <br>mobileRobotPosition.y = y, <br>mobileRobotPosition.theta = theta <br>mobileRobotPosition.mapId = mapId <br>mobileRobotPosition.lastNodeId = lastNodeId | The pose is not valid or cannot be reset. <br>General localization problems should correspond with an error. | -
downloadMap | Initialize the connection to the map server. | Mobile robot is downloading the map. | - | The download has finished. Mobile robot updates its state by setting the mapId/mapVersion and the corresponding mapStatus to 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, Map server unreachable, mapId/mapVersion not existing on map server). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableMap | - | The mobile robot enables the map with the requested mapId and mapVersion and disables any other map with the same mapId. | - | The map has been enabled. The mobile robot updates the corresponding mapStatus of the requested map to 'ENABLED' and the other versions with same mapId to 'DISABLED'. | The requested combination of mapId/mapVersion does not exist.| -
deleteMap | - | Mobile robot deletes map with requested mapId and mapVersion from its internal memory. | - | The map has been deleted. The mobile robot removes mapId/mapVersion from its state. | The map could not be deleted, e.g., because map is currently in use or requested combination of mapId/mapVersion has already been deleted before. | -
downloadZoneSet | Initialize the connection to the zone set server. | Mobile robot is downloading the zone set. | - | The download has finished. The mobile robot updates its state by setting a corresponding zoneSet object in its state with zoneSetStatus 'DISABLED'. | The download failed, updated in mobile robot state (e.g., connection lost, server unreachable, zone set not existing, zone set with same zoneSetId already on mobile robot). | Download failed or was interrupted. The mobile robot is waiting for intervention from fleet control.
enableZoneSet | - | Mobile robot enables the zone set with the requested zoneSetId and disables any other zone set for the same mapId. | - | The zone set has been enabled. The mobile robot updates the corresponding zoneSetStatus of the requested zoneSet to 'ENABLED' and the other zone sets for the same mapId to 'DISABLED'. | The requested zone set does not exist.| -
deleteZoneSet | - | Mobile robot deletes the zone set with requested zoneSetId from its internal memory. | - | The zone set has been deleted. The mobile robot removes zoneSet object from its state. | The zone set could not be deleted, deleted, e.g., because zone set is currently in use or the requested zone set has already been deleted before. | -
clearInstantActions | - | | - | The instant actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
clearZoneActions | - | | - | The zone actions array has been cleaned from all FINISHED or FAILED instantActions. | - | -
stateRequest | - | - | - | The state has been communicated | - | -
logReport | - | The report is being generated. <br>If the mobile robot supports an instant generation, this state can be omitted. | - | The report has been stored. <br>The name of the log is reported as part of the action state. | The report can not be stored (e.g., no space).| -
pick | Initializing of the pick process, e.g., outstanding lift operations. | The pick process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The pick process is being paused, e.g., if a safety field is violated. <br>After removing the violation, the pick process continues. | Pick has been done. <br>Load has entered the mobile robot and mobile robot reports new load state. | Pick failed, e.g., station is unexpected empty. <br> Failed pick operations should correspond with an error. | Pick failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
drop | Initializing of the drop process, e.g., outstanding lift operations. | The drop process is running (mobile robot is moving into station, load handling device is busy, communication with station is running, etc.). | The drop process is being paused, e.g., if a safety field is violated. <br>After removing the violation the drop process continues. | Drop has been done. <br>Load has left the mobile robot and mobile robot reports new load state. | Drop failed, e.g., station is unexpected occupied. <br>Failed drop operations should correspond with an error. | Drop failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
detectObject | - | Object detection is running. | - | Object has been detected. | Could not detect the object. | Object detection failed, but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
finePositioning | - | Mobile robot positions itself exactly on a target. | The fine positioning process is being paused, e.g., if a safety field is violated. <br> The fine positioning continues after e.g. the violation had been resolved. | Goal position in reference to the station has been reached. | Goal position in reference to the station could not be reached. | Fine positioning failed but is retriable. The mobile robot is waiting for intervention from fleet control or an operator.
waitForTrigger | - | Mobile robot is waiting for the trigger | - | Trigger has been triggered. | waitForTrigger fails, if order has been canceled. | -
cancelOrder | - | Mobile robot is stopping or driving, until it reaches the next node. | - | Mobile robot is not moving. Mobile robot has canceled executing the order and is in idle state. | <br>Mobile robot has no active order<br>The previous order has already been canceled.<br>Passed orderId does not match the currently active orderId. | -
factsheetRequest | - | - | - | The factsheet has been communicated | - | -
updateCertificate | - | Mobile robot is downloading and installing certificates | - | Certificates have been downloaded, installed and are active. | Download or installation failed. | -

>Table 5 - Expected behavior in action states of predefined actions

#### 6.2.3.3 Update mobile robot certificate

For security reasons, mobile robot communication (at least for fleet management) should be secured. Typically, communication to the MQTT broker is secured via TLS, which requires one or more root certificates and a mobile robot-specific key pair. The parameter `service` specifies the service (e.g., 'MQTT') for which the certificates are to be used. The parameter `certificateAuthorityDownloadLink` specifies the URL for the root certificate(s). The parameters `certificateDownloadLink` and `keyDownloadLink` specify the URLs for the mobile robot-specific public and private keys.

The download shall be secured via TLS as well, since the sender of the instantAction cannot be verified. It is also advisable to validate the certificate chain before it is activated.

## 6.3 Maps

To ensure consistent navigation among different types of mobile robots, the position is always specified in reference to the project-specific coordinate system (see Figure 12). The project-specific coordinate system is referring to the coordinate system that is defined for the interaction between fleet control and the mobile robot.
For the differentiation between different levels of a site or location, a unique `mapId` is used.
The map coordinate system is to be specified as a right-handed coordinate system with the z-axis pointing skywards.
A positive rotation therefore is to be understood as a counterclockwise rotation.
The mobile robot coordinate system is also specified as a right-handed coordinate system (ISO 9787 4.1) with the x-axis pointing in the forward direction of the mobile robot and the z-axis pointing upward (ISO 9787 5.5). The mobile robot reference point is defined as (0,0,0) in the mobile robot reference frame, unless specified otherwise.

![Figure 12 Coordinate system with sample mobile robot and orientation](./assets/coordinate_system_vehicle_orientation.png)
>Figure 12 - Coordinate system with sample mobile robot and orientation

The X, Y, and Z coordinates shall be given in meters.
The orientation shall be in radians and shall be within -Pi and +Pi.

### 6.3.1 Map distribution

To enable an automatic map distribution and intelligent management of restarting the mobile robots if necessary, fleet control can manage the maps on the mobile robot.

The map files to be distributed are stored on a dedicated map server that is accessible by the mobile robots. To ensure efficient transmission, each transmission should consist of a single file. If multiple maps or files are required, they should be bundled or packed into a single file. The process of transferring a map from the map server to a mobile robot is a pull operation, initiated by the fleet control triggering a download command using an `instantAction`.

Each map is uniquely identified by a combination of a map identifier (field `mapId`) and a map version (field `mapVersion`). The map identifier describes a specific area of the mobile robot's physical workspace, and the map version indicates updates to previous versions. Before accepting a new order, the mobile robot shall check that there is a map on the mobile robot for each map identifier in the requested order. If a corresponding `mapId` is missing in the list of available maps, the mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'. It is the responsibility of the fleet control to ensure that the correct maps are enabled to operate the mobile robot.

In order to minimize downtime and make it easier for the fleet control to synchronize the process of enabling of new maps, maps shall be pre-loaded or buffered on the mobile robots. The status of the maps on the mobile robot is reflected in the mobile robot's state. Transferring a map to a mobile robot and enabling the map are different processes. To enable a pre-loaded map on a mobile robot, the fleet control shall send an instant action. As a result, any other map with the same map identifier but a different map version shall be disabled by the mobile robot.

Deletion of maps can also be done by the fleet control via an instant action.

The map distribution process is shown in Figure 13.

![Figure 13 Map distribution process](./assets/map_distribution_process.png)
>Figure 13 - Communication required between fleet control, mobile robot and map server to download, enable, and delete a map.

### 6.3.2 Maps in the mobile robot state

The `mapId` field in the `mobileRobotPosition` of the state represents the currently active map.

Information about the maps available on a mobile robot is presented in the `maps` array, which is a component of the state message. Each entry in this array is a JSON object consisting of the mandatory fields `mapId`, `mapVersion`, and `mapStatus`, which can be either 'ENABLED' or 'DISABLED'. An 'ENABLED' map can be used by the mobile robot if necessary. A 'DISABLED' map shall not be used. The status of the download process is indicated by the current action not being completed. Errors are also reported in the state.
Note that multiple maps with different `mapId` can be enabled at the same time. There shall only be one version of maps with the same `mapId` enabled at a time. If the `maps` array is empty, no maps are currently available on the mobile robot.

### 6.3.3 Map download

The map download shall be triggered by the `downloadMap` instant action from the fleet control. It shall contain the mandatory parameters `mapId` and `mapDownloadLink` under which the map is stored on the map server and which can be accessed by the mobile robot.

The mobile robot sets the `actionStatus` to 'RUNNING' as soon as it starts downloading the map file. If the download is successful, the `actionStatus` is updated to 'FINISHED'. If the download is unsuccessful, the status is set to 'FAILED'. Once the download has been successfully completed, the map shall be added to the array of `maps` in the state. Maps shall not be reported in the state until they are ready to be enabled.

The process of downloading a map shall not modify, delete, enable, or disable any existing maps on the mobile robot.
The mobile robot shall reject the download of a map with a `mapId` and `mapVersion` that is already on the mobile robot. An error of type 'DUPLICATE_MAP' and level 'WARNING' shall be reported, and the status of the instant action shall be set to 'FAILED'. The fleet control shall first delete the map on the mobile robot and then restart the download.

### 6.3.4 Enable downloaded maps

There are two ways to enable a map on a mobile robot:

1. **Fleet control enables map**: Use the `enableMap` instant action to set a map to 'ENABLED' on the mobile robot. Other Versions of the same `mapId` with different `mapVersion` are set to 'DISABLED'.
2. **Manually enable a map on the mobile robot**: In some cases, it might be necessary to enable the maps on the mobile robot directly. The result shall be reported in the mobile robot state.

Fleet control shall ensure that the correct maps are activated on the mobile robot when sending the corresponding `mapId` as part of a `nodePosition` in an order.
If the mobile robot is to be set to a specific position on a new map, the `initializePosition` instant action shall be used.

### 6.3.5 Delete maps on the mobile robot

The fleet control can request the deletion of a specific map from a mobile robot. This shall be done by using the instant action `deleteMap`. When a mobile robot runs out of memory, it should report this to the fleet control, which can then initiate the deletion of maps. The mobile robot itself shall not delete maps.
After successfully deleting a map, the mobile robot shall remove the corresponding entry from its `maps` array in the state message.

## 6.4 Zones

Zones are used to define rules for specific areas of the mobile robot workspace. In this way, zones allow mobile robots to navigate freely between nodes while giving the fleet control the ability to manage traffic. Zones can be used to locally deny mobile robots access to areas or to link access to conditions (zone types: 'BLOCKED' and 'RELEASE'). It is also possible to enforce specific behavior while within the zone (zone types: 'LINE_GUIDED', 'SPEED_LIMIT', 'COORDINATED_REPLANNING', and 'ACTION') or influence the driving behavior by incentivizing or penalizing certain areas (zone types: 'PRIORITY' and 'PENALTY') or giving a predefined driving direction (zone types: 'DIRECTED', 'BIDIRECTED'). The zone types are defined in the following sections.

Potential conflicts in orders due to overlapping of zones or combination of zone and edge properties and how to resolve them are addressed in section [6.4.4 Interaction between zones](#644-interactions-between-zones). For released nodes that are part of the order but are restricted due to zones (e.g., node located within a 'BLOCKED' or 'RELEASE' zone), the robot is expected to act according to the zones (e.g., not enter or wait for 'GRANTED' state of the request).
Some mobile robots cannot process zones at all, while other mobile robots might only be able to work with a certain subset of zone types, such as 'BLOCKED'. All mobile robots shall therefore report to fleet control which zones they are able to understand by adding the according zone names to the `supportedZones` array under `typeSpecifications` in their factsheet.
Also (virtually) line-guided mobile robots can choose to support zone-based navigation if they can implement the logic of the corresponding zone types defined in the following.
A zone set shall only be changed and distributed by fleet control to keep consistency in the system.

### 6.4.1 Zone types

Two categories of zones are distinguished: contour-based zones and kinematic center-based zones. This distinction is based on the different conditions for when the mobile robot is considered to be entering and exiting zones.

#### 6.4.1.1 Contour-based zones

For contour-based zones, the contour of the mobile robot (including its load) determines zone entry and exit. Any part of the contour entering the zone is a zone entry. As soon as no part of the mobile robot's contour remains within the zone, it is a zone exit.

![Figure 14 Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)](./assets/contour_entry.png)
>Figure 14 - Depiction of a mobile robot entering a zone based on its contour (left) and a loaded mobile robot with corresponding extended bounding box exiting a zone (right)

The following contour-based zones are defined:

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| BLOCKED | none | | Mobile robots shall not enter this zone. If a mobile robot has entered the zone or finds itself within one, it shall stop and throw an 'BLOCKED_ZONE_VIOLATION' error with level set to 'CRITICAL'.|
| LINE_GUIDED | none | | No free navigation is allowed in this zone, mobile robots shall follow the predefined trajectories on edges. Mobile robots may only enter this zone if the route is explicitly specified by the fleet control in the form of a node-edge graph. Any movement of the mobile robot that requires it to enter this zone shall follow a predefined trajectory. When entering the zone, the mobile robot shall be on the trajectory of the edge that crosses the zone. The edges that enter and are inside the line-guided zone require a trajectory sent from the fleet control or a predefined trajectory on the mobile robot. A corridor can be sent to allow the mobile robot to deviate from the trajectory. |
| RELEASE | | - | Mobile robots are only allowed entering this zone once they have been granted access through fleet control. |
| | releaseLossBehavior | string | Enum {'STOP', 'CONTINUE', 'EVACUATE'}<br>When the access to this zone is revoked or expired, the mobile robot can either 'STOP', 'CONTINUE', or 'EVACUATE' the zone. This action is only executed, when the mobile robot is already in the zone and the release expires or is revoked. If not defined, the mobile robot is expected to STOP and report an error.<br>'STOP': Mobile robot stops and sends a 'RELEASE_LOST' error with level 'CRITICAL'.<br>'EVACUATE': Execute the evacuation behavior of the mobile robot to leave the zone, keeping the `zoneRequest` object granting release in its state until the zone is left.<br>'CONTINUE': If the release is revoked or expires after the mobile robot has already entered the zone, the mobile robot continues its path, keeping the `zoneRequest` object granting the zone release in its state. If the order ends inside the zone, the mobile robot waits for a new order.|
| COORDINATED_REPLANNING | none | | No autonomous replanning is allowed within this zone. Mobile robots are only allowed adjusting their path if granted permission by fleet control. |
| SPEED_LIMIT | | | Mobile robots shall not drive faster than the defined maximum speed within this zone. |
| | maximumSpeed | float64 | Maximum permitted speed for mobile robot within the zone in m/s. The speed limit shall already be reached upon entering the zone.|
| ACTION | | | The mobile robot shall perform predefined actions when entering, traversing, or exiting the zone. The factsheet defines which actions can be executed when. |
| | entryActions[action] | array | Actions to be triggered when entering the zone. Empty array, if no actions required. |
| | duringActions[action] | array | Actions to be executed while crossing the zone. Empty array, if no actions required. |
| | exitActions[action] | array | Actions to be triggered when leaving the zone. Empty array, if no actions required. |

>Table 6 - Contour-based zone types and their parameters

#### 6.4.1.2 Kinematic center-based zones

In kinematic center-based zones, the mobile robot's kinematic center determines its entry and exit of the zones. When the mobile robot's kinematic center is inside a zone, the mobile robot shall follow the defined behavior.
'PRIORITY' and 'PENALTY' zones are zones which only influence the path planning of mobile robots.
'DIRECTED' zones define a preferred direction of travel within the zone. 'BIDIRECTED' zones define a travel direction and its opposite direction to be used. Other directions shall be avoided. The `directedLimitation` and `bidirectedLimitation` enums specify the limits within which the mobile robot may deviate from its direction of travel. The direction of travel is the velocity vector in the project-specific coordinate system.

![Figure 15 Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)](./assets/kinematic_center_entry.png)
>Figure 15 - Depiction of a mobile robot entering a zone based on its kinematic center (left) and a loaded mobile robot exiting a zone based on its kinematic center (right)

| **Zone Type**| **Zone Parameters** | **Data type** | **Description** |
| --- | --- | --- | --- |
| PRIORITY | | | The workspace encompassed by this zone is associated with an incentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | priorityFactor | float64 | [0.0...1.0]<br>Relative factor that determines the preference of the zone over a workspace without a zone. 0.0 means no preference, as if there was no zone, 1.0 is maximum preference.|
| PENALTY | | | The workspace encompassed by this zone is associated with a disincentive for the mobile robot to plan its route through this zone compared to an otherwise equivalent area without such a zone on the map.|
| | penaltyFactor | float64 | [0.0...1.0]<br> Relative factor that determines the penalty of the zone compared to a workspace without that zone. 0.0 means no penalty, as if there was no zone, 1.0 is the maximum penalty, causing the mobile robot to take this path only if it cannot find any other feasible route. |
| DIRECTED | | | Mobile robots shall traverse this zone in a specific direction of travel. |
| | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system. |
| | directedLimitation | string | Enum {'SOFT','RESTRICTED','STRICT'}<br>SOFT: Mobile robots may deviate from the defined direction of travel, but should avoid it, RESTRICTED: The mobile robot may deviate from the defined direction of travel, e.g., to avoid an obstacle, but shall never traverse opposite to the defined direction of travel, STRICT: The mobile robot shall maintain the defined direction of travel as precisely as its technical capabilities allow. |
| BIDIRECTED | | | While in this zone, mobile robots shall only move in the defined direction of travel and its direct opposite (+ Pi), mobile robots should not cross this zone in any other direction. |
 | direction | float64 | Preferred direction of travel within the zone in radians. The direction of travel is the angular orientation of the mobile robot's velocity vector in the project-specific coordinate system.|
| | bidirectedLimitation | string | Enum {'SOFT', 'RESTRICTED'}<\br>SOFT: Mobile robots may deviate from the defined directions of travel, but should avoid it, RESTRICTED: The mobile robot shall not traverse in any other direction than the directions of travel, except for obstacle avoidance. |

>Table 7 - Kinematic center-based zone types and their parameters

### 6.4.2 Zone set transfer

Zone sets shall only be changed and distributed by fleet control to keep consistency in the system. The preferred way to distribute zone sets is via the `zoneSet` topic. If the mobile robot supports zones, the update via the `zoneSet` topic shall be supported. Larger zone sets can also be shared through the `downloadZoneSet` instant action, following the map distribution concept in figure 13.

A `zoneSet` is an array of `zone` objects with a globally unique identifier, `zoneSetId`. It is associated with a single map referenced through the `mapId`. The `mapVersion` shall not be referenced, as the same zone set might be intended to be used for several versions of one map. In general, several zone sets can be defined in addition to a single map and it is upon fleet control to ensure that the right zone set is enabled for each map on the mobile robot. As with maps, the `zoneSetStatus` indicates which zone set is currently used by the mobile robot. Only a single zone set can be active at once for each `mapId` on the mobile robot. Zones shall not extend beyond the spatial boundaries of a map.
The content of a zone set with a unique `zoneSetId` shall not change. If changes are required within a zone set, it shall be referenced with a new `zoneSetId`.

The `zoneSetStatus` of a newly added zone set shall always be set to 'DISABLED' and shall be enabled through the `enableZoneSet` instant action before use.

If the mobile robot receives a new zone set via the `zoneSet` topic or `downloadZoneSet` instant action with the same `zoneSetId` as an existing one, it shall not take over the zone set in its internal memory and report an error of type 'DUPLICATE_ZONE_SET' and level 'WARNING' for a reasonable amount of time for the fleet control to notice that the zone update failed.

## 6.4.3 Communication for interactive zones

For communicating requests for the interactive zones 'RELEASE' and 'COORDINATED_REPLANNING', the field `zoneRequests` in the state message is used. The separate topic `responses` is used by fleet control to respond to these requests.

Before entering an interactive zone, the mobile robot shall state a request.
A request before entry of an interactive zone is necessary, even if the order contains released nodes within the zone.
The mobile robot decides at which point before entering the zone to make its requests.
If the response is not received in time, the mobile robot shall not enter the zone.

Requests shall only be made for zones of enabled zone sets. Zone requests can also be made for zone sets belonging to maps that the mobile robot is not currently on.

The `requestId` allows fleet control to distinguish between different requests and allows the mobile robot to issue several alternative requests for the same zone at the same time.
Each request attempt shall use a unique identifier per mobile robot. Ids can be reused after a mobile robot restart.

For requests to enter a 'RELEASE' zone, a `zoneRequest` object of `requestType` 'ACCESS' shall be added to the state message.
For permission to enter a 'COORINATED_REPLANNING' zone with a planned path or for replanning its path within the zone, the `requestType` shall be set to 'REPLANNING'.
For a 'REPLANNING' request, the planned path shall be added as NURBS to the `trajectory` field of the `zoneRequest`. Multiple requests with different trajectories for the same zone can be made. Each path shall be requested with its own `zoneRequest` object.
If a mobile robot requires access to a workspace covered by two or more 'RELEASE' zones, it shall request access and receive approval for all necessary zones before entering the area.
If a mobile robot navigates through a workspace on the map that is covered by two or more 'COORDINATED REPLANNING' zones, it shall request its path within this area individually for each zone and receive approval from the fleet control before entering or changing paths.

The parameter `requestStatus` shall be initially set to 'REQUESTED' by the mobile robot when stating its request.

Fleet control responds to zone requests via the `responses` topic.
The response message contains an array of `response` objects. Each `response` shall only respond to a single request referenced by the `requestId`.
Each response has a `responseType` that is either 'GRANTED', 'QUEUED', 'REVOKED', or 'REJECTED'.
If the `responseType` is 'GRANTED', the mobile robot is allowed to enter the zone or use the requested trajectory.
Fleet control can set the `responseType` to 'QUEUED' to acknowledge the mobile robot's request without giving permission, informing the mobile robot that its request is being processed.
If the `responseType` is 'REJECTED', the mobile robot shall not enter the zone or use the requested trajectory.
The `responseType` 'REVOKED' indicates that the permission is no longer valid. The fleet control shall assume a 'REVOKED' request as still being 'GRANTED', until the `requestStatus` of the mobile robot is set to 'REVOKED'.
The `response` object can include a `leaseExpiry` which specifies until when a 'GRANTED' request is valid. To extend the `leaseExpiry` fleet control can resend a response message with an updated `leaseExpiry` time.

The mobile robot shall acknowledge the fleet controls response by setting the `requestStatus` accordingly and keep the request for as long as it considers the information relevant. See also Section [6.9 Request/response mechanism](#69-requestresponse-mechanism).

The interaction between the mobile robot and the fleet control for 'RELEASE' zones shall be according to Figure 16.

While the mobile robot remains in the 'RELEASE' zone, it keeps the `zoneRequest` object in its state and continues to report `requestStatus` as 'GRANTED' to inform fleet control that it is still inside the zone. After mobile robot has exited the zone, it shall remove the corresponding `zoneRequest` entry from its state message.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state. When the `leaseExpiry` has passed, the requestStatus shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall report a warning and react according to the `releaseLossBehavior` defined in the zone definition.

![Figure 16 Zone request behavior for a RELEASE zone.](./assets/request_release_zone_access.png)
>Figure 16 - Zone request behavior for a RELEASE zone.

The interaction between the mobile robot and the fleet control for 'COORDINATED_REPLANNING' zones shall be according to Figure 17.

The mobile robot shall choose one of the trajectories of all 'GRANTED' requests to the zone and set the corresponding `requestStatus`to 'GRANTED' while removing all other requests from its state.
When receiving a response with `responseType` 'REVOKED', the mobile robot shall remove the request from its state and not enter the 'COORDINATED_REPLANNING' zone. When the `leaseExpiry` has passed, the `requestStatus` shall be set to 'EXPIRED' and the zone shall not be entered. If the mobile robot is already inside the 'RELEASE' zone when the `leaseExpiry` has passed or the request is 'REVOKED', it shall stop driving and report a warning. To continue, the mobile robot shall state a new request.

![Figure 17 Zone request behavior for a COORDINATED_REPLANNING zone.](./assets/request_coordinated_replanning_zone_replanning.png)
>Figure 17 - Zone request behavior for a COORDINATED_REPLANNING zone.

### 6.4.4 Interactions between zones

In the following matrix possible interactions between zones are described. The matrix is symmetric, as the interaction between two zones is the same, regardless of the order in which they are considered. For each combination, there is either a zone behavior that is overrulling the other (e.g., a 'BLOCKED' zone overrules a 'LINE_GUIDED' zone) or there is no conflict (e.g., a 'LINE_GUIDED' zone and a 'COORDINATED_REPLANNING' zone). 'DIRECTED' and 'BIDIRECTED' zones shall not overlap, since this might lead to an undefined behavior. The column No Zone defines the behavior for contour-based zones, where mobile robots can be inside a defined zone type and an area without a zone at the same time. For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so there is no possible interaction.

| |**BLOCKED**|**RELEASE**|**LINE_GUIDED**|**COORDINATED_REPLANNING**|**SPEED_LIMIT**|**ACTION**|**PRIORITY**|**PENALTY**|**DIRECTED**|**BIDIRECTED**|**No Zone**|**EDGE-PROPERTIES**
---|---|---|---|---|---|---|---|---|---|---|---|---
**BLOCKED**|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|BLOCKED|
**RELEASE**||No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict|No Conflict
**LINE_GUIDED**|||No conflict|LINE_GUIDED|No Conflict| (1) |LINE_GUIDED|LINE_GUIDED|LINE_GUIDED|No conflict|LINE_GUIDED|No conflict
**COORDINATED_REPLANNING**||||(2)|No conflict|(1)|No conflict|No conflict|No conflict|No conflict|COORDINATED_REPLANNING|(3)
**SPEED_LIMIT** |||||(4)|No conflict|No conflict|No conflict|No conflict|No conflict|SPEED_LIMIT|(4)
**ACTION** ||||||(5)|No conflict|No conflict|No conflict|No conflict|ACTION|(5)
**PRIORITY** |||||||(6)|(6)|No conflict|No conflict|(7)|No conflict
**PENALTY** ||||||||(6)|No conflict|No conflict|(7)|No conflict
**DIRECTED** |||||||||(8)|(8)|(7)|(9)
**BIDIRECTED** ||||||||||(8)|(7)|(9)

>Table 8 - Interaction matrix for zones

1) If actions would conflict with other zones' behavior, report a 'ZONE_ACTION_CONFLICT' error with level 'CRITICAL' (order error) and stop the mobile robot.
2) Planned trajectory required to be granted for all 'COORDINATED_REPLANNING' zones.
3) If a trajectory is predefined for the edge, it shall be sent in the zone request.
4) The lowest of the competing `maximumSpeed` values applies.
5) Execute all actions.
6) The most restrictive one is always selected here; for PRIORITY zones, the lowest `priorityFactor` is used; for overlapping PRIORITY and PENALTY zones, the highest `penaltyFactor` is used; for overlapping PENALTY zones, the highest `penaltyFactor` is used.
7) For kinematic center-based zones the mobile robot can only be completely within or outside the zone, so this overlap is not possible.
8) Zones shall not overlap, since the behavior is not defined.
9) A `trajectory` as part of the edge properties shall override the directed and bidirected zones.

### 6.4.5 Error handling within zones

If at any point of the order execution, a mobile robot realizes, that it can not reach a node in its order, it shall report a 'NODE_UNREACHABLE' error with level 'CRITICAL' to the fleet control. The fleet control shall then decide how to proceed. The mobile robot shall not try to reach the node again, but wait for further instructions from the fleet control.

## 6.5 Connection

During the connection of a mobile robot client to the broker, a last will topic and message shall be set, which is published by the broker upon disconnection of the mobile robot client from the broker.
Thus, the fleet control can detect a disconnection event by subscribing the connection topics of all mobile robots.
The disconnection is detected via a heartbeat that is exchanged between the broker and the client.
Thus, the fleet control can detect a disconnection event by subscribing to the `connection` topic of each mobile robot.

As a result, the timestamp and headerId fields will always be outdated.

Mobile robot wants to disconnect gracefully:

1. Mobile robot sends "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to `OFFLINE`.
2. Disconnect the MQTT connection with a disconnect command.

Mobile robot comes online:

1. Set the last will to "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN', when the MQTT connection is created.
2. Send the topic "vda5050/v3/manufacturer/serialNumber/connection" with `connectionState` set to 'ONLINE'.

All messages on this topic shall be sent with a `retained` flag.

When connection between the mobile robot and the broker stops unexpectedly, the broker will send the last will to the topic: "vda5050/v3/manufacturer/serialNumber/connection" with the field `connectionState` set to 'CONNECTION_BROKEN'.

## 6.6 State

The mobile robot state shall be published on a single topic.
Compared to separate messages (e.g., for current order progress, battery state and errors), using a single topic reduces the workload of both the broker and the fleet control system when handling messages, while also keeping the mobile robot state information synchronized.

The mobile robot state message shall be published when relevant events occur or at least every 30 seconds.

The following events shall trigger a transmission of the state message:

- Receiving an order
- Receiving an order update
- Changes in the `load` object
- Change in the `errors` array
- Change in the `operatingMode` field
- Change in the `driving` field
- Change in the `paused` field
- Change in the `safetyState` object
- Change in the `newBaseRequest` field
- Change in the `lastNodeId` or `lastNodeSequenceId` field
- Change in the `edgeRequests` or `zoneRequests` arrays
- Change in the `powerSupply.charging` field
- Change in the `nodeStates` or `edgeStates` arrays
- Change in the `actionStates`, `instantActionStates` or `zoneActionStates` arrays
- Change in the `zoneSets` array
- Change in the `maps` array

*Remark: For above mentioned arrays, changes in the individual items of the array as well as adding or removing entries shall trigger a state message transmission.*

There should be an effort to curb the amount of communication.
If two events correlate with each other (e.g., the receiving of a new order usually forces an update of the `nodeStates` and `edgeStates`; as does the driving over a node), it is sensible to trigger one state update instead of multiple. The minimum time between two consecutive state messages is defined by the factsheet ([7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) `protocolLimits.timing.minimumStateInterval`) .

### 6.6.1 Concept and logic

The order progress is tracked by the `nodeStates` and `edgeStates`.
Additionally, if the mobile robot is capable of determining its current position, it shall publish it via the `mobileRobotPosition` field.

The `nodeStates` and `edgeStates` include all upcoming nodes and edges for the mobile robot to traverse.

![Figure 18 Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted](./assets/order_information_state_topic.png)
>Figure 18 - Order information provided by the state topic. Only the ID of the last node and the remaining nodes and edges are transmitted

### 6.6.2 Traversal of nodes and edges

The mobile robot decides on its own when a node should count as traversed.
A requirement for the traversal is that the mobile robot's control point shall be within the node's `allowedDeviationXY` and its orientation within `allowedDeviationTheta`.
The `allowedDeviationXY` defines at what point a line-guided mobile robot can deviate from its predefined trajectory, to cut the corner along a smoother path rather than reaching the node's exact position. When leaving the `allowedDeviationXY` the mobile robot shall be back on its predefined trajectory of the subsequent edge.
If the edge attribute `corridor` of the subsequent edge is set, these boundaries should be met additionally.

In case the mobile robot is located too far away from the first node of an order, the fleet control can add an extended `allowedDeviationXY` to this node to include the mobile robot's current position.

The mobile robot shall report the traversal of a node by removing its `nodeState` from the `nodeStates` array and setting the `lastNodeId` and `lastNodeSequenceId` to the traversed node's values.

As soon as the mobile robot reports the node as traversed, the mobile robot shall trigger the actions associated with the node, if any.
The traversal of a node also necessarily implies leaving the edge that is leading up to the node.
The edge shall then also be removed from the `edgeStates` and the actions that were active on the edge shall be finished.

The traversal of the node also marks the moment when the mobile robot enters the following edge, if there is one.
The edge's actions shall be triggered, if any.
An exception to this rule is if the mobile robot shall stop on the node (because of a soft or hard blocking action) – then the mobile robot only enters the following edge once it begins driving again.

When an active order exists, the fields `lastNodeId` and `lastNodeSequenceId` shall be updated only when the mobile robot traverses a released node that is part of this order. For example if a physically line‑guided mobile robot detects a physical marker/tag that is not part of the active order’s `nodes`, this detection shall not lead to a change of `lastNodeId` or `lastNodeSequenceId`.

![Figure 19 Depiction of nodeStates, edgeStates, and actionStates during order handling](./assets/states_during_order_handling.png)
>Figure 19 - Depiction of `nodeStates`, `edgeStates`, and `actionStates` during order handling

#### 6.6.2.1 Definition of allowedDeviationXY as an ellipse

The allowedDeviationXY is defined as an ellipse around the node position to allow more flexible approaches to the node.

![Figure 20 allowedDeviationXY ellipse](./assets/ellipse.png)
>Figure 20 - allowedDeviation ellipse

### 6.6.3 Base request

If the mobile robot detects that its base is running short, it can set the `newBaseRequest` flag to "true" to attempt to prevent unnecessary braking.

### 6.6.4 Information

The mobile robot can submit arbitrary additional information to the fleet control via the `information` array.
It is up to the mobile robot to decide how long it reports information via an information message.

The fleet control shall not use the information for logic; they shall only be used for visualization and debugging purposes.

### 6.6.5 Errors

The mobile robot reports any issues via the `errors` array.

#### 6.6.5.1 Error levels

The issues can have four levels: 'WARNING', 'URGENT', 'CRITICAL', and 'FATAL'.

- A 'WARNING' level issue does not require immediate attention. The mobile robot can continue its current order and is able to take new orders. The error might be self-resolving, e.g., a dirty LiDar-scanner.
- An 'URGENT' level issue, e.g., a low battery level, requires immediate attention. The mobile robot can continue its current order and is able to take new orders.
- A 'CRITICAL' level issue requires immediate attention, e.g., trying to pick an object, that is not there. The mobile robot shall not continue driving since it can not continue its current order but is able to take new orders.
- A 'FATAL' level issue requires user intervention, e.g., losing localization. The mobile robot shall not continue driving since it can neither continue its currently active order nor take any new orders.

The mobile robot can add references that help with finding the cause of the error via the `errorReferences` array.
The fields `errorDescription` and `errorHint` may provide human-readable text explaining the error or suggesting a possible resolution.

Regardless of the level of the issue, the mobile robot shall never clear its order due to it.

#### 6.6.5.2 Error references

If an error occurs due to an erroneous order or execution failure, the mobile robot can return meaningful error references in the field `errorReferences` to support finding the cause of the error.
This can include the following information:

- `headerId`
- Topic (`order` or `instantAction`)
- `orderId` and `orderUpdateId` if error was caused by an order update
- `actionId` if error was caused by an action
- List of parameters if error was caused by erroneous action parameters

#### 6.6.5.3 Error translations

For both `errorDescription` and `errorHint`, the mobile robot can provide translations by using the `errorDescriptionTranslations` and `errorHintTranslations` arrays.
Each translation consists of an ISO 639-1 language code and the corresponding translated text.

#### 6.6.5.4 Predefined error types

The mobile robot shall use predefined error types to report specific issues. The following table lists the predefined error types and their description.

Error Type | Error level | Description | Reference | Report duration
---|---|---|---|---
'UNSUPPORTED_PARAMETER' | 'CRITICAL' | Receival of message with an unsupported optional parameter. | Name of parameter | Until new order is accepted.
'NO_ORDER_TO_CANCEL' | 'WARNING'  | The mobile robot received a `cancelOrder` action, but it does not have an active order to cancel. | `actionId` of `cancelOrder` | Until new order is accepted.
'VALIDATION_FAILURE'|'WARNING'| Receival of malformed order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_ORDER_ACTION' | 'WARNING' | Receival of an order containing unsupported actions. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'INVALID_INSTANT_ACTION' | 'WARNING' | Receival of an unsupported instant action. | `actionId` of `instantAction` | Until new instant action is accepted.
'OUTDATED_ORDER_UPDATE'| 'WARNING' | Receival of an order with correct `orderId` but outdated `orderUpdateId`. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'SAME_ORDER_UPDATE_ID' | 'WARNING' | Receival of a duplicate order message (same `orderId` and `orderUpdateId`) | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'ORDER_UPDATE_FOLLOWING_CANCEL' | 'WARNING' | Receival of an order update for an order that has already been cancelled. | `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'OUTSIDE_OF_CORRIDOR' | 'CRITICAL' | Leaving the corridor defined for an edge. | `edgeId` | Until the mobile robot is no longer violating the corridor boundaries.
'INSUFFICIENT_MEMORY' | 'URGENT' | Mobile robot does not have enough memory to process received order. | If possible, `orderId` and `orderUpdateId` of rejected message. | Until new order is accepted.
'DUPLICATE_MAP' | 'WARNING' | Receival of a map with `mapId` and `mapVersion` already existing. | `mapId` and `mapVersion` of duplicate | Until a new map related instantAction was accepted.
'BLOCKED_ZONE_VIOLATION' | 'CRITICAL' | Entering a 'BLOCKED' zone. | `zoneId` | Until the mobile robot is no longer violating the blocked zone.
'DUPLICATE_ZONE_SET' | 'WARNING' | Receival of a zone set with `zoneSetId` already existing. | `zoneSetId` or `actionId` of `instantAction` | Reasonable amount of time for the fleet control to notice that the zone update failed.
'RELEASE_LOST' | 'CRITICAL' | Losing the release for a 'RELEASE' zone. | `zoneId` | Until the mobile robot is no longer within the 'RELEASE' zone or is granted a the release again.
'ZONE_ACTION_CONFLICT' | 'CRITICAL' | Conflict between zone behavior and zone actions. | `zoneId` of 'ACTION' zone | Until the mobile robot is no longer violating the zone behavior.
'NODE_UNREACHABLE'|'CRITICAL'| The mobile robot cannot reach a node in its order. | `nodeId` | Until new order is accepted.
'LOCALIZATION_ERROR'|'FATAL'| The mobile robot is not localized. | | Until localization is regained.
'NO_ROUTE_TO_TARGET' | 'WARNING' | Receival of an order with at least one unreachable node. | `orderId` | Until new order is accepted.
'OTHER_ORDER_ACTIVE' | 'WARNING' | Receival of a new order while another order is still active. | `orderId` | Until new order is accepted.
'START_NODE_OUT_OF_RANGE' | 'WARNING' | Receival of an order with unreachable first node. | `orderId` | Until new order is accepted.
'MOBILE_ROBOT_NOT_AVAILABLE' | 'WARNING' | Receival of an order while not in 'AUTOMATIC', 'SEMIAUTOMATIC' or 'INTERVENED' operating mode. | `orderId` | Until operating mode allows for new orders
'UNKNOWN_MAP_ID' | 'WARNING' | Receival of an order containing nodes referencing an unknown `mapId`. | `orderId` | Until new order is accepted.

> Table 9 - Predefined error types

### 6.6.6 Operating Mode

For regular order execution, fleet control shall be in full control of the mobile robot. There are however situations where this is not possible, e.g., when manual interaction on the mobile robot is required. The mobile robot shall report this using the field `operatingMode`.

The following lists describe the values of the field `operatingMode`, their meaning, and implications on the interaction between mobile robot and fleet control:

Operating Mode | Description
---|---
AUTOMATIC | Fleet control is in full control of the mobile robot. <br>Mobile robot moves and executes actions based on orders from the fleet control.
SEMIAUTOMATIC | Fleet control is in control of the mobile robot.<br> Mobile robot moves and executes actions based on orders from the fleet control. <br>The driving speed is controlled by the HMI.<br>The steering is under automatic control.
INTERVENED | Fleet control is not in control of the mobile robot. The mobile robot is reporting its state correctly.<br>HMI can be used to control the steering, velocity and handling devices of the mobile robot.<br>Fleet control is allowed to send orders or order updates to the mobile robot to be executed after changing back into operating mode 'AUTOMATIC' or 'SEMI-AUTOMATIC'. Fleet control shall not send any instant action except `cancelOrder`.<br>The mobile robot shall not clear the order but shall remove all zone requests from the state, also if the mobile robot is already inside a 'RELEASE' zone. (*Remark: If necessary, the fleet control can continue to track the position of the mobile robot and decide whether clearance for other mobile robots is possible.*) The mobile robot shall not request any permissions to enter a 'RELEASE' zone or for replanning inside a 'COORDINATED_REPLANNING' zone.<br>If entering operating mode 'INTERVENED' has any impact on running actions the mobile robot shall reflect this in the state message accordingly.<br>If the mobile robot leaves this operating mode and does not directly switch into 'AUTOMATIC' or 'SEMI-AUTOMATIC' mode it shall act according to new operating mode. If the mobile robot leaves this operating mode and switches directly into 'AUTOMATIC' or 'SEMI-AUTOMATIC' mode the mobile robot shall continue executing any current order. If the mobile robot detects during operating mode 'INTERVENED' that a continuation of the current order is not possible the mobile robot shall switch into operating mode 'MANUAL' and act accordingly.
MANUAL | Fleet control is not in control of the mobile robot. <br>Fleet control shall not send orders or actions to the mobile robot. <br>HMI can be used to control the steering, velocity and handling devices of the mobile robot.<br>The position of the mobile robot is sent to the fleet control.<br>When the mobile robot enters this mode, it immediately clears any current order.<br>If, while being in this mode, the mobile robot detects that it is being moved to a position where the current value of `lastNodeId` cannot be used as a start node of a new order, it shall set `lastNodeId` to an empty string ("").
STARTUP | Fleet control is not in control of the mobile robot. The mobile robot is starting up and not ready to receive orders. State message parameters may be incomplete or invalid until startup is finished.
SERVICE | Fleet control is not in control of the mobile robot. <br>Fleet control shall not send orders or actions to the mobile robot. <br>When the mobile robot enters this mode, it immediately clears any current order.<br>The mobile robot shall set `lastNodeId` to an empty string ("").<br>Authorized personnel can reconfigure the mobile robot.
TEACH_IN | Fleet control is not in control of the mobile robot. <br>Fleet control shall not send orders or actions to the mobile robot. <br>When the mobile robot enters this mode, it immediately clears any current order.<br>The mobile robot shall set `lastNodeId` to an empty string ("").<br>The mobile robot is being taught, e.g., mapping is done by an operator.

>Table 10 - Operating modes of the mobile robot

Operating Mode | Fleet Control in control | Valid state message content | Clear order when entering | Set `lastNodeId` to empty | Clear zone requests when entering | Sending instant actions allowed | Sending orders allowed
--- | --- | --- | --- | --- | --- | --- | ---
AUTOMATIC | YES | YES | NO | NO | NO | YES | YES
SEMIAUTOMATIC | YES | YES | NO | NO | NO | YES | YES
INTERVENED | NO | YES | NO | NO | YES | Only `cancelOrder` allowed | YES
MANUAL | NO | YES | YES | YES, if continuation of order is not possible | YES | NO | NO
STARTUP | NO | NO | YES | YES | YES | NO | NO
SERVICE | NO | YES | YES | YES | YES | NO | NO
TEACH_IN | NO | YES | YES | YES | YES | NO | NO

>Table 11 - Overview of operating modes and their implications

### 6.6.7 Clearing the order on the mobile robot

In response to one of the following events, the mobile robot shall stop executing the current order:

- The mobile robot is changing the operating mode to 'MANUAL', 'STARTUP', 'SERVICE' or 'TEACH_IN' (see also [6.6.6 Operating Mode](#666-operating-mode)).
- The mobile robot receives a `cancelOrder` instant action from fleet control.
- The mobile robot receives a `startHibernation` instant action.

In these cases the mobile robot shall clear its current order which means that:

- Any scheduled actions in the `actionStates` shall be cancelled and be reported as 'FAILED' in `actionStates`.
- Any running action in the `actionStates` that
	- can be cancelled (cancelAllowed = true) shall be cancelled and be reported as 'FAILED' in `actionStates`.
	- cannot be cancelled (cancelAllowed = false) shall be reflected by reporting 'RUNNING' while being executed, and afterwards as the respective state ('FINISHED' if successful, 'FAILED' otherwise).
- The value of `orderId`, `orderUpdateId`, `lastNodeId` and `lastNodeSequenceId` remain unchanged.
- The arrays `nodeStates` and `edgeStates` are set to empty lists.
- Any requests shall be removed from the state.

As long as the actions of an order are not in state 'FINISHED' or 'FAILED' the mobile robot shall not report operating mode 'MANUAL', 'SERVICE' or 'TEACH_IN'. `nodesStates` and `edgeStates` shall not be emptied before the operating mode 'MANUAL', 'SERVICE' or 'TEACH_IN' is reported.

An order cancellation can only be triggered by fleet control.

### 6.6.8 Idle state of the mobile robot

A mobile robot is idle if its `nodeStates` and `edgeStates` are empty and all actions in the `actionStates` are either 'FINISHED' or 'FAILED'. A new order shall only be accepted if the mobile robot is idle. An order update can be accepted when the mobile robot is idle or during order execution. When idle, a mobile robot can execute instantActions.

### 6.6.9 Action states

When a mobile robot receives an `action` as part of the order (attached to a `node` or `edge` of an order), it shall report this `action` with an `actionState` in its `actionStates` array.
When a mobile robot receives an `instantAction`, it shall report this `action` with an `actionState` in its `instantActionStates` array.
When a mobile robot executes a `zoneAction`, it shall report this `action` with an `actionState` in its `zoneActionStates` array. Optionally, a mobile robot can report any planned `zoneAction` here.

The current stage of an action shall be reflected in the field `actionStatus` of the corresponding `actionState` (see Table 2).

actionStatus | Description
---|---
'WAITING' | Action was received by the mobile robot but the corresponding node was not yet traversed or the corresponding edge was not yet entered.
'INITIALIZING' | Action was triggered, preparatory measures are initiated.
'RUNNING' | The action is running.
'PAUSED' | The action is paused because of a pause instantAction or external trigger (pause button on the mobile robot)
'RETRIABLE' | Actions that failed, but can be retried, specified by the retriable parameter in the action of an order. Transition from this state is triggered by a retry or skipRetry instantAction or an external trigger.
'FINISHED' | The action is finished. <br>A result is reported via the `actionResult`.
'FAILED' | Action could not be finished for whatever reason.

>Table 12 - Feasible values for the `actionStatus` field

All possible action state transitions are visualized in Figure 21 and examples are given in the following matrix:
…(발췌: 전체 207,642자 중 앞 119,109자)
````
