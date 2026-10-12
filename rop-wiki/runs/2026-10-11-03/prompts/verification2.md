(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-03
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 22. 설비·건물 시스템 연동 (F. 연동)
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

### runs/2026-10-11-03/target.json

```json
{
  "run_id": "2026-10-11-03",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 169,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 22,
    "area_name": "22. 설비·건물 시스템 연동",
    "category": "F. 연동",
    "category_letter": "F"
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
  "selection_rationale": "CLI 지정 run_type=update, area=22"
}
```

### runs/2026-10-11-03/research.json

```json
{
  "run_id": "2026-10-11-03",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 22,
    "area_name": "22. 설비·건물 시스템 연동",
    "category": "F. 연동"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 — 국토부 '로봇 친화형 건축물' 핵심기술 개발 보도자료(ref-322)는 제목만 확인돼 발행일·사업기간·세부 과제가 비어 있고, KS B 7317 은 '2021년 11월 제정'만 있어 이후 개정 이력이 없음",
    "섹션 4·6. 핵심 개념·대표 접근법(주제 페이지 2026-09-25-area10-s4) — 승강기 세션을 언제 '수락'으로 볼지, 세션 종료·잔류 처리, 작업대 결과의 완료 판정 조건 근거가 약함. 제조사 어댑터(KONE·Dormakaba)와 PLC 연결의 실제 조건이 없음",
    "섹션 5. 적용 사례 — 물류창고 가상 시나리오뿐이며 실제 설비 연결(PLC·드라이 접점)과 화재 복구, 상업 시설 사례가 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지 2026-09-25-area10-s7) — KOLA 단체표준이 '표준 번호·제정일·내용 미확인', SEMI E84 현행판·후속 개발 제안, BACnet 출입통제 문서의 지위가 비어 있음",
    "섹션 8. 대표 연구와 자료(주제 페이지 2026-09-25-area10-s8) — '모두 원문을 열지 못해 결과 수치는 쓰지 않는다'로 남아 있어 각 연구의 실험 조건(실물·수치 실험)과 승강기 결과가 비어 있음",
    "섹션 9·11 — 출입통제 연동에서 권한 확인 주체(oq-043), 단체표준–Open-RMF 대응(oq-041), 인계 신호 표준(oq-042), 물류센터 승강기 병목(oq-010)이 열려 있음"
  ],
  "research_questions": [
    "문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]",
    "oq-010 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? (섹션 3·8 겨냥)",
    "oq-041 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (oq-283 표준 번호 포함, 섹션 7 겨냥)",
    "oq-042 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? (oq-062 포함, 섹션 6·7 겨냥)",
    "oq-043 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (섹션 7·9 겨냥)",
    "KS B 7317 과 로봇 친화형 건축물 관련 국내 제도·연구개발은 현재 어느 판·단계인가? (oq-098·oq-173·oq-311·oq-179 관련, 섹션 3·7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Park·Park 의 2026년 Architectural Research 논문은 초록 기준으로 로봇 친화형 건축물 인증(REEC)과 무장애(BF) 인증을 비교 분석해 사람 중심·로봇 적응형 건축 설계 기준을 도출했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"comparative analysis … REEC … and Barrier-Free (BF) Certification … design standards were derived\". 서지 Architectural Research 28(1), 논문번호 14(Crossref). 본문 미열람이라 연구 방법(현장 실험 여부)은 단정하지 않음",
      "as_of": "2026-07-21",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "국토교통부의 로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발 연구개발은 2025년 5월 착수보고회를 열고 2028년까지 완료할 예정이라고 2차 보도됐다.",
      "tag": "추정",
      "source_ids": [
        "ref-322",
        "ref-1484"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "스마트투데이 2025-05-28 기사: 착수보고회 29일, \"이번 R&D는 2028년까지 완료될 예정\". 국토부 보도자료 원문(ref-322)은 열지 못해 사업기간 2025~2028 과 보도·배포일은 2차 보도 기준",
      "as_of": "2025-05-28",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f3",
      "claim": "같은 연구개발은 세부 중점과제 가운데 하나로 기술 실증을 통한 기술표준·인증제도 개선방안 마련을 두었다고 2차 보도됐다.",
      "tag": "추정",
      "source_ids": [
        "ref-322",
        "ref-1484"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사: 세부 중점과제 \"△기술 실증을 통한 기술표준 및 인증제도 개선방안 마련\" 포함 세 가지. 보도자료 원문 미열람(ref-322), 이후 완료·인증 시행 여부 미확인",
      "as_of": "2025-05-28",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f4",
      "claim": "e-나라표준인증의 KS B 7317 이력은 2021-11-30 제정(고시 2021-0561), 2022-12-09 개정(고시 2022-0571), 2025-05-09 개정(고시 2025-0073)을 기록한다.",
      "tag": "사실",
      "source_ids": [
        "ref-314"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "표준 이력사항 표: 2021-11-30 제정 '수요조사 반영에 의한 제정', 2022-12-09·2025-05-09 개정 '사회적 요청에 의한 개정'. 기존 '2021년 11월 제정' 서술과 맞고 개정 2회가 새 내용. 표준 본문·신구대비표 미열람",
      "as_of": "2025-05-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "같은 KS B 7317 기본정보는 적용 대상을 엘리베이터 탑승 기능이 있는 서비스 로봇과 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터로 적고, 표준개발협력기관을 한국AI·로봇산업협회로 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-314"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "적용범위: \"적용 대상 엘리베이터: 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터\", 담당 국가기술표준원 기계융합산업표준과. 목록 정보만 사용, 인증 의무로 확장하지 않음",
      "as_of": "2025-05-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "대한승강기협회(KOLA)는 2026-03-27 게시한 보도자료에서 「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」 단체표준을 제정했다고 발표했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KOLA 보도자료(작성일 2026.03.27): \"「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」단체표준을 제정했다\". 게시일을 제정일로 치환하지 않음. 기존 위키 제정 보도(ref-316·ref-317)를 협회 1차 자료로 보강",
      "as_of": "2026-03-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "e-나라표준인증 단체표준 목록은 이 가이드라인을 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 로 올려 두어, KOLA 게시일(2026-03-27)과 목록 등록일이 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "목록 행: \"B-KOLA-0001-7700 … 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 … (사)대한승강기협회 … 제정 … 등록일자 2026-03-24\". 정확한 제정일·본문 미확인 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "KOLA 발표는 이 가이드라인이 엘리베이터와 로봇 상호 연동을 위한 일반사항, 시험 설비 및 시험 절차를 제시하며 e-나라표준인증에서 무료로 내려받을 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료: \"일반사항, 시험 설비 및 시험 절차에 대한 가이드라인을 제시\", \"e-나라표준인증 … 무료로 다운로드가 가능\". 표준 본문의 메시지·상태 정의와 Open-RMF 대응은 미확인",
      "as_of": "2026-03-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Open-RMF 개발자(mxgrey)는 2024년 토론 답변에서, 세션을 안전하게 수행하려면 승강기가 별도 AGV 모드여야 하는 경우 모드 전환을 마칠 때까지 승강기 상태에 session_id 를 내보내지 말아야 한다고 권고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Discourse 아카이브(2024-08-21, GitHub 토론 #513): \"it should not broadcast the session_id value until it has finished switching into that mode\". 설계 의도 설명이며 현장 안전 동작 재현 아님",
      "as_of": "2024-08-21",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "같은 답변은 별도 AGV 모드가 없는 승강기도 있을 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Some lifts might not have a special AGV mode\" — 이 경우 승강기 상태가 다른 모드 값을 보낼 이유가 없다는 설명. 모드 상수 열거는 기존 위키(2026-09-25-area10-s4)에 있음",
      "as_of": "2024-08-21",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "rmf_ros2 의 lift_supervisor 구현은 승강기별 활성 세션을 두고, 같은 session_id 의 새 요청은 갱신으로 다시 발행하며 세션 종료 요청이면 종료를 발행하고 활성 세션을 비운다.",
      "tag": "사실",
      "source_ids": [
        "ref-1488"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Node.cpp _adapter_lift_request_update: \"curr_request->session_id == msg->session_id\" 분기에서 REQUEST_END_SESSION 이 아니면 갱신 발행, 맞으면 종료 발행 후 nullptr. 커밋 4cea3fe 고정 코드",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "같은 구현은 감독자에게 활성 요청이 없는데 승강기 상태에 세션이 남아 있으면 승강기가 풀리도록 세션 종료 요청을 계속 발행하며, 승강기 배정을 더 지능적으로 하라는 TODO 만 남겨 두고 배정 규칙은 두지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1488"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "_lift_state_update: \"we keep publishing session end requests to ensure that the lift gets released\"; 주석 \"TODO(MXG): Make this more intelligent by scheduling the lift\". 다중 플릿 배차 최적성은 입증하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "rmf_fleet_adapter 변경기록의 2.13.0(2026-06-15)에는 승강기가 이미 해당 층에 있으면 legacy 완료 상태를 내보내는 변경(#510)이 실려 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1398"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHANGELOG 2.13.0 (2026-06-15): \"emit completion legacy state if lift is already on the level (#510)\". 같은 변경기록에 2.14.0(2026-09-26)이 있어 2.13.0 을 최신판으로 부르지 않음",
      "as_of": "2026-06-15",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "rmf_ros2 의 DispenseItem 단계는 요청 id 가 일치하는 DispenserResult 가 SUCCESS 이면 완료, FAILED 이면 실패로 바꾸고, ACKNOWLEDGED 는 접수 표시만 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1489"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DispenseItem.cpp _get_status: request_guid 일치 시 ACKNOWLEDGED → _request_acknowledged, SUCCESS → STATE_COMPLETED, FAILED → STATE_FAILED. 커밋 4cea3fe 고정 코드",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f15",
      "claim": "같은 구현은 디스펜서 상태의 요청 큐에 요청 id 가 들어 있으면 접수된 것으로 보고, 접수 뒤 큐에서 요청 id 가 사라지면 결과 메시지 없이도 완료로 간주한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1489"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "주석 \"The request has been received, so if it's no longer in the queue, then we'll assume it's finished.\" 접수 표시는 큐에 들어간 것만으로도 설정됨",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f16",
      "claim": "큐 소거만으로 완료 처리하면 현장 작업대 큐에서 요청이 취소·오류로 빠진 경우에도 인계 완료로 잘못 판단할 수 있을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1489"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "구현(큐 소거 → STATE_COMPLETED)에서 도출한 설계 위험 해석. 큐 소거가 실제 적재물 센서 확인과 같다는 보장은 코드에 없음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f17",
      "claim": "CHART 계열 공개 KONE 승강기 어댑터 README 는 Open-RMF 승강기 메시지와 KONE API v2.0 사이에서 WebSocket 으로 승강기 명령을 보내고 승강기 상태를 받는 구조를 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"send various lift commands to KONE API v2.0 via websocket\", \"get lift state from KONE API v2.0 via websocket\". 2023년 고정판(KABAM-Robotics 보존 저장소, 원 저장소 안내는 sharp-rmf/kone-ros-api). 현행 KONE 계약 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "같은 README 는 실제 승강기를 제어하려면 access_id 와 access_secret 을 KONE 담당자에게서 받아야 한다고 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"To control a live elevator, you will need to get these id & secret from KONE Personnel.\" The Galen 실기 시험 문구는 프로젝트 자체 보고이며 기존 위키(ref-884)에 같은 사례가 있음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "연계 대상: Open-RMF 의 Dormakaba 문 어댑터 README 는 시험한 EL301·ED250 문 구동기에 Dormakaba IoT connector 를 장착해야 한다고 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"tested with the Dormakaba EL301 and ED250 models. It requires the Dormakaba IoT connector to be fitter[sic] to the above door operators.\" 임의 자동문 지원을 입증하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "같은 README 는 문 클라우드 API 접근 자격증명을 Dormakaba 가 제공한다고 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1491"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Credentials to access the door's cloud API will be provided by Dormakaba.\" 클라우드 자격증명 제공과 건물 출입권한 승인 정책은 별개 확인 항목",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "연계 대상: HopeTechnik 의 도서관 현장 설계 문서에서는 현장에 새로 설치한 승강기 제어함(lift controller box)의 PLC(Beckhoff CX9020)가 서버의 ADS 명령을 받아 드라이 접점으로 승강기 신호를 조작하며, 승강기 업체가 기존 승강기를 AGV 모드로 개조했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: \"A PLC is housed in a lift controller box at level 6 cargo lift lobby\", \"via ADS … manipulating corresponding signals via dry contact. Beckhoff CX9020\"; \"the lift vendor upgraded the installed lift … AGV mode\". 승강기 자체 PLC 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f22",
      "claim": "연계 대상: 같은 문서의 복구표는 화재 경보가 울리면 승강기가 수동 모드로 돌아가고 PLC 가 오류 상태에 머물러, 재시작을 위한 수동 개입이 필요하다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: Table 1 #2 Fire Alarm: \"Manual intervention is needed. PLC will stay in error state until it is restarted.\" 한 도서관 현장의 설계이므로 다른 건물의 화재 복구 조건으로 일반화하지 않음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "기타",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f23",
      "claim": "같은 문서는 승강기 상태 전송 주기를 개요에서는 1 Hz 로, 서버 절에서는 2초마다로 서로 다르게 적고, 승강기 요청은 1초마다 보낸다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: 개요: LiftState \"at a frequency of 1 Hz\"; Server 절: \"published to the AWS topic every 2 seconds\", LiftRequest \"every 1 second\". 차이를 설명하는 구절 없음 — 전송 주기 결론 보류 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "기타",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f24",
      "claim": "OMRON LD 시리즈 통합 안내서(I680-E-02)의 인계 예시는 위치·준비 상태 확인, 적재물 교환, 정지·최종 위치 확인, 출발 준비 확인을 단계로 나눈다고 외부 조사 메모가 전한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1493"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 PDF 가 접근 거부(Access Denied)로 열리지 않아 메모 서술만 근거. Lift 절은 적재 장치 리프트이며 건물 승강기 사례가 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "같은 안내서는 그 인계 절차가 예시이며 응용 요구에 따라 달라질 수 있다고 적는다고 외부 조사 메모가 전한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1493"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 미열람(접근 거부). 제조사 예시 절차이며 제조사 중립 규격이 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "SEMI 공식 판매 목록은 E84-0823 을 현행판(Current)으로 표시하고, E84 의 목적을 자동 반송 시스템(AMHS)과 생산 설비 로드포트 사이 캐리어 인계용 병렬 I/O 신호 개선으로 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-202"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "목록: \"Revision: SEMI E84-0823 - Current\"(이전 E84-1109 등 Superseded), 초록: AMHS 와 생산 설비 사이 \"carrier handoffs (load/unload)\" 신호 정의. 표준 본문 미열람 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "SEMI Doc 7442 는 E84 를 출발점으로 별도의 인계 인터페이스 규격과 TCP/IP 하위 규격을 만들자는 신규 예비 표준 개발 제안서(SNARF)라고 외부 조사 메모가 전한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1494"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "SEMI 다운로드 페이지가 봇 차단으로 열리지 않아 작성일(2025-12-17)·승인일·내용은 메모 서술만 근거. 개발 제안 승인과 표준 발행은 구분 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f28",
      "claim": "고려대 구로병원 약품 배송 로봇 논문은 ROC 로 찾은 승강기 가동률(EOR) 임계값 59.01% 를 현장 특정값으로 해석해야 하며 다른 병원에 적용할 때 재보정이 필요하다고 명시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Discussion: \"should be interpreted as site-specific and is expected to require recalibration when applied to other hospital environments\"; 승강기 카 크기·운반 카트·이용자 구성 차이를 이유로 듦",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f29",
      "claim": "2026-10-11 재확인에서도 같은 논문에는 전체 성공률 87.03% 의 분모를 설명하는 구절이 없고, 분석 대상 122건에서 실패 14건을 뺀 108건의 비율은 약 88.52% 로 보고값과 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 \"We analyzed 122 non-urgent missions\", §3.1 \"The overall success rate across all trials was 87.03%\". 'all trials' 의 범위 정의 없음. oq-215 근거 보강용이며 수치 자체는 기존 위키에 있음",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f30",
      "claim": "사람과 승강기를 함께 쓰는 실제 건물에서 로봇의 층간 이동이 지연된 사례가 서로 다른 두 연구에서 보고됐다: 병원 논문은 승강기 가동률이 높을수록 배송 시간이 길어졌다고, KAIST 지도 구축 논문은 외부 이용자 때문에 승강기가 다른 층으로 가 지연이 생겼다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-943",
        "ref-163"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "ref-943 초록 \"An increased EOR also prolonged the delivery time\"; ref-163 결과 \"6층에서 7층으로 이동하는 구간의 경우 외부 이용자에 의해 엘리베이터가 다른 층으로 이동하는 지연이 발생\". 기관이 다른 독립 출처(질적 관찰)",
      "as_of": "2026-03",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f31",
      "claim": "Han 외 다층 호텔 배송 경로계획 논문은 실제 호텔 평면·층고로 거리 행렬(68×68)만 만들고 배송 수요는 무작위 표본으로 생성했으며, 승강기 기본 대기 시간을 30초로 두었다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실험 설정: 거리는 \"derived from the actual hotel floor plan and floor height\", 수요는 \"uses random sampling to generate\" 10·20·30·60건, \"sets the base waiting time for elevators at 30 s\". 실제 호텔 운용 성능이 아님",
      "as_of": "2025-03-13",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "Kim 외 그래프 기반 다층 경로계획 논문은 15층 건물을 나타내는 그래프에서 소포 1·3·5·7개 시나리오로 알고리즘을 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-321"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5: \"graph-based environment representing a 15-story building … n = 1, 3, 5, 7\". 시뮬레이션 평가이며 실제 건물 운용 아님",
      "as_of": "2025-02-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "노주형 외 다층 지도 구축 연구는 KAIST N1 건물 5~9층에서 각 층의 절반 영역을 대상으로 평가를 수행했다.",
      "tag": "사실",
      "source_ids": [
        "ref-163"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실험: \"5층부터 9층까지 각 층의 절반 영역을 대상으로 평가를 수행\", 영문 초록 \"validated in the KAIST N1 building across five floors (5F–9F)\". 로봇 한 대의 실물 지도 구축",
      "as_of": "2026-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "같은 연구의 승강기 상호작용 시험에서는 20회 중 19회 성공이 보고됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-163"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Table 5 \"Elevator Interaction Task 19 20 95%\". 성공률 95% 자체는 기존 위키에 있으며 시행 횟수(19/20)가 새 내용",
      "as_of": "2026-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "BACnet 출입통제 백서 BAC-09-08(2008-09-27)은 SSPC 135 LSS 작업반의 진행 중 작업이자 BACnet 표준 변경 제안의 기초 문서라고 스스로 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "표지·초록: \"the basis for proposed changes to the BACnet standard. The contents are subject to change.\" 현행 ANSI/ASHRAE 135 규범 본문이 아니며 2022년 호스팅 경로는 발행일이 아님",
      "as_of": "2008-09-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "같은 백서는 인증과 권한 검사를 구분하고, 특정 시간에 특정 문을 통과할 권리를 기본 권한 검사의 예로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"A basic example of authorization validation checks would be the right to pass through a specific door at a specific time.\" 모든 검사를 통과해야 출입이 허가된다는 설명",
      "as_of": "2008-09-27",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "NAVER LABS 는 2026-07-23 블로그에서 ARC 가 Tokyo Midtown Yaesu 의 기존 화물 승강기·자동문과 출입 경로를 중앙에서 연결한다고 설명하고, 연말까지 전 층 로봇 배송으로 넓힐 계획이라고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"From freight elevators and automatic doors to entry and exit routes, ARC serves as a means for central integration\"; 전 층 확대는 \"plans to expand … by the end of the year\" 계획. 독립 운영 평가 없음",
      "as_of": "2026-07-23",
      "site_type": "상업 시설",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f38",
      "claim": "구축자 의견: ROP 의 설비 연동 수용 기준은 건축물 인증 항목·국가 연구개발 계획과 별도 목록으로 관리하고, 발주 때 인증의 적용 판·심사 범위와 현장 설비 연결 계약을 서로 다른 증빙으로 확인하는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1483",
        "ref-322",
        "ref-1484"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "설계 논문(ref-1483)·연구개발 계획 보도(ref-1484)는 인증 운영기관의 현행 심사 규칙이 아님. 외부 조사 메모 K01·K02 의 시사점을 정리",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "구축자 의견: 승강기 탑승 안전 표준을 검토할 때는 판(제정·개정 일자)·적용 범위·대상 승강기 유형을 함께 기록하는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-314"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "KS B 7317 이 두 차례 개정됐고 병원 환자 전용 엘리베이터를 적용 대상에서 뺀다는 목록 정보에 근거",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "구축자 의견: KOLA 가이드라인과 Open-RMF 승강기 메시지의 대응표는 표준 원문의 메시지·시험 시나리오를 확보한 뒤에 작성하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1485",
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "발표·목록은 대상 범위(일반사항·시험 설비·시험 절차)와 번호만 확인. 본문 미열람",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "구축자 의견: 장치별 세션 수락 조건(AGV 모드 전환 완료 뒤 session_id 보고 여부)을 어댑터 계약에 적고, 수락 전 탑승을 막는지 확인하는 시험을 두는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "mxgrey 권고와 AGV 모드가 없는 승강기 존재 설명에 근거",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "구축자 의견: 세션 유실·중복 종료·설비 상태의 세션 잔류 상황을 현장 인수 시험 항목에 넣는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1488"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "lift_supervisor 의 세션 종료 반복 발행 분기에 근거. 다중 플릿 배정 규칙은 구현에 없음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "구축자 의견: 실물 인계 성공을 뜻하는 센서·PLC 조건을 작업대 결과 메시지와 따로 정하고, 큐 소거가 취소·오류를 뜻하는 경우를 구별하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1489"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "DispenseItem 의 큐 소거 완료 간주 분기에 근거",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "구축자 의견: 제조사 승강기 어댑터를 검토할 때는 공개 어댑터의 판과 별도로 현행 API 판·권한 범위·건물 등록·세션 유지 조건을 확인하는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1490"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "KONE 어댑터는 2023년 고정 공개 구현이며 자격증명을 제조사 담당자에게 받는 구조",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "구축자 의견: 자동문 연동에서는 문 열기 API 자격증명과 별도로 로봇의 공간별 출입 권한과 비상 우선권을 누가 정하는지 확인해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1491",
        "ref-1495"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Dormakaba 는 클라우드 자격증명만 제공한다고 안내하고, BACnet 백서는 인증과 권한 검사를 구분",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "구축자 의견: ROP 장애 복구와 건물 설비의 비상 복귀를 따로 시험하고, 화재 뒤 설비 재시작 같은 수동 복귀의 책임자를 정해 두는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1492"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "HopeTechnik 복구표의 화재 경보 뒤 PLC 오류 유지·수동 재시작 요구에 근거",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f47",
      "claim": "구축자 의견: ROP 는 준비·허가·이송·완료의 의미를 현장 PLC·작업대와 합의하고, 물리 인계 완료를 상위 작업 완료에 연결하는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-202",
        "ref-1493"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "E84(반도체 범위)와 제조사 예시 절차는 서로의 적합성을 검증한 근거가 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f48",
      "claim": "구축자 의견: 병원·호텔·그래프·지도 연구의 승강기 결과를 국내 다층 물류센터 처리량으로 옮기는 것은 보류하고, 승강기 가동률·통신 상태·카 내부 점유를 나눠 수집해 현장별 임계값을 새로 검증하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-943",
        "ref-103",
        "ref-321",
        "ref-163"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "병원 논문의 재보정 명시, 호텔·그래프 연구의 수치 실험 성격, 로봇 한 대 실물 지도 구축이라는 조건에 근거(oq-010)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f49",
      "claim": "구축자 의견: 설비 API 연동과 로봇팔 버튼 조작을 서로 다른 승강기 연결 방식으로 기록하고, 공유 승강기 지연 시험을 따로 두는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-163",
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "병원 사례는 제어반 통신 모듈, KAIST 사례는 버튼 조작이며 두 사례 모두 공유 승강기 지연을 보고",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f50",
      "claim": "구축자 의견: 기존 건물 도입 사례는 연동 설비 목록과 실제 운영 중인 로봇 종류·층 범위를 고객 측 자료로 따로 확인하기 전에는 운영 실증으로 세지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Yaesu 발표의 전 층 확대는 계획이고 이기종 지원은 설계 설명",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-322",
      "org": "국토교통부",
      "title": "올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료)",
      "published": null,
      "url": "https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 외부 조사 메모가 인용한 같은 국토부 보도자료('AI 품은 건축물, 이제는 스마트+빌딩 시대', CODIL 보존본 포함)로, 이번에도 MOLIT·CODIL 원문을 열지 못해 보도·배포일과 쪽수는 확인하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1484",
      "org": "스마트투데이(이재수)",
      "title": "\"사람과 로봇이 공존하는 스마트 빌딩 앞당긴다\"...국토부 산학협력단과 기술개발 착수",
      "published": "2025-05-28",
      "url": "https://www.smarttoday.co.kr/ko-kr/articles/81933",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "국토부 스마트+빌딩 연구개발 착수 보도. 2028년까지 완료 예정과 기술 실증을 통한 기술표준·인증제도 개선방안 등 세부 과제를 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1483",
      "org": "Park, Y.; Park, S. (Architectural Research)",
      "title": "Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems",
      "published": "2026-07-21",
      "url": "https://link.springer.com/article/10.1007/s44515-026-00016-y",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "로봇 친화형 건축물 인증과 무장애 인증을 비교해 로봇 적응형 건축 설계 기준을 도출한 논문(28(1), 논문번호 14). 초록과 Crossref 서지만 확인했고 본문은 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.crossref.org/works/10.1007/s44515-026-00016-y",
      "source_unopened": false
    },
    {
      "id": "ref-314",
      "org": "국가기술표준원(e-나라표준인증·KSSN)",
      "title": "KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법",
      "published": "2025-05-09",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010135682",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B 7317 표준 정보. 이번에 e-나라표준인증 상세 페이지에서 제정(2021-11-30)·개정(2022-12-09, 2025-05-09) 이력과 적용 범위·표준개발협력기관을 확인했다. 표준 본문은 미열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB7317&menuId=919&reformNo=&tmprKsNo=KSB7317&topMenuId=502&upperMenuId=503",
      "source_unopened": false
    },
    {
      "id": "ref-1485",
      "org": "대한승강기협회(KOLA)",
      "title": "대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27)",
      "published": "2026-03-27",
      "url": "https://kola.or.kr/pages/61/68/bbs/5705",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KOLA 의 「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」 단체표준 제정 보도자료. 대상(일반사항·시험 설비·시험 절차), 협의체 구성, e-나라표준인증 무료 다운로드를 안내한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1486",
      "org": "국가기술표준원(e-나라표준인증)",
      "title": "단체표준 목록 — B-KOLA-0001-7700 엘리베이터와 로봇의 상호 연동을 위한 가이드라인",
      "published": null,
      "url": "https://www.standard.go.kr/KSCI/grpstd/getGrpStdCrtfcReqst.do?menuId=60372&topMenuId=502&upperMenuId=503",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "e-나라표준인증 단체표준 목록 검색 결과. KOLA 가이드라인의 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 를 보여 준다. 표준 본문은 미열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1487",
      "org": "cwrx777; mxgrey (Open Robotics Discourse 아카이브)",
      "title": "Lift session issues - Robot enter lift while lift is still in human mode (#513)",
      "published": "2024-08-21",
      "url": "https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "Open-RMF GitHub 토론 #513 의 Discourse 아카이브. 승강기가 AGV 모드로 바뀌기 전 로봇이 탑승한 문제와, 모드 전환 뒤에 session_id 를 보고하라는 개발자 답변을 담는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1488",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter/src/lift_supervisor/Node.cpp (commit 4cea3fe)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/lift_supervisor/Node.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 승강기 감독자 구현. 같은 세션 요청의 갱신·종료 처리와, 활성 요청 없이 남은 세션에 종료 요청을 반복 발행하는 분기를 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/lift_supervisor/Node.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1398",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "Changelog for package rmf_fleet_adapter",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_fleet_adapter 변경기록. 이번에 2.13.0(2026-06-15)의 승강기가 이미 해당 층에 있을 때 완료 상태를 내보내는 변경(#510)을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1489",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp (commit 4cea3fe)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 배송 작업의 디스펜서 단계 구현. 결과 메시지(ACKNOWLEDGED·SUCCESS·FAILED)와 상태 큐 소거로 완료를 판정하는 조건을 담는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp",
      "source_unopened": false
    },
    {
      "id": "ref-1490",
      "org": "CHART; KABAM-Robotics 보존 저장소",
      "title": "KONE RMF Lift Adapter / kone-ros-api — README (commit 9bc3a87)",
      "published": null,
      "url": "https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 승강기 메시지와 KONE API v2.0 을 WebSocket 으로 잇는 공개 어댑터 README(원 저장소 안내는 sharp-rmf/kone-ros-api). 실제 승강기 제어 자격증명을 KONE 담당자에게 받도록 안내한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/KABAM-Robotics/lift_kone_adapter/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1491",
      "org": "Open-RMF (open-rmf/door_adapter_dormakaba 저장소)",
      "title": "door_adapter_dormakaba — README (commit 2cf76a6)",
      "published": null,
      "url": "https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Dormakaba 스마트 문용 Open-RMF 문 어댑터 README. EL301·ED250 시험, IoT connector 장착 요구, 문 클라우드 API 자격증명 제공 주체를 적는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/door_adapter_dormakaba/2cf76a6b83ceee31540aeb7e0d7feb2a10042668/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1492",
      "org": "HopeTechnik (RMF Systems Engineering Handbook)",
      "title": "Lift and Doors Integration",
      "published": null,
      "url": "https://trl-rmf.github.io/website/content/lift-door-integration.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "한 도서관 현장의 승강기·문 연동 설계와 복구 설명. 승강기 제어함 PLC(Beckhoff CX9020)·드라이 접점 연결, AGV 모드 개조, 화재 경보 시 복구 절차와 메시지 주기를 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1493",
      "org": "OMRON",
      "title": "LD-Series Integration Guide (I680-E-02)",
      "published": null,
      "url": "https://www.omron.com.tw/data_pdf/mnu/i680-e-02_ld.pdf?id=3664",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. OMRON LD 시리즈 이동로봇 통합 안내서로, 외부 조사 메모는 적재물 인계 예시 절차를 담는다고 전한다. 이번 검증에서 접근 거부로 열지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-202",
      "org": "SEMI",
      "title": "E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface",
      "published": null,
      "url": "https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SEMI E84 판매 목록. 이번에 E84-0823 이 현행판(Current)으로 표시되고 AMHS–생산 설비 캐리어 인계 범위를 설명하는 초록을 확인했다. 표준 본문은 미열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1494",
      "org": "SEMI Physical Interfaces & Carriers TC (Japan)",
      "title": "SNARF for Doc 7442: Specification for Enhanced Handoff Interface",
      "published": null,
      "url": "https://downloads.semi.org/web/wstdsbal.nsf/18a679096dfd445188256d35007d447d/0db3fe2c9bb0eb2488258d9400027699!OpenDocument",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. E84 를 바탕으로 한 새 인계 인터페이스 표준 개발 제안서로 외부 조사 메모가 전한다. 이번 검증에서 봇 차단으로 열지 못해 작성·승인일은 미확인이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증. 이번에 EOR 임계값의 재보정 필요 명시, 배송 지연 관찰, 전체 성공률 분모 설명 부재를 다시 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "source_unopened": false
    },
    {
      "id": "ref-103",
      "org": "Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "다층 호텔 로봇 배송 경로계획 수치 실험. 실제 호텔 평면으로 거리 행렬을 만들고 수요는 무작위 생성했으며 승강기 기본 대기 30초·운행 40~100초를 둔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-321",
      "org": "Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982)",
      "title": "Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots",
      "published": "2025-02-28",
      "url": "https://doi.org/10.3390/electronics14050982",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "실내 배송 로봇의 승강기 선택을 최적화한 그래프 기반 다층 경로계획. 15층 건물 그래프에서 소포 1·3·5·7개 시나리오로 평가했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mdpi-res.com/d_attachment/electronics/electronics-14-00982/article_deploy/electronics-14-00982.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-163",
      "org": "노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57)",
      "title": "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템",
      "published": "2026-03",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "탐사와 승강기 연계로 다층 실내 지도를 자율 구축한 KAIST 연구. KAIST N1 5~9층 각 층 절반 영역 평가, 승강기 상호작용 19/20 성공, 외부 이용자로 인한 승강기 지연을 보고한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://jkros.org/xml/48719/48719.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1495",
      "org": "SSPC 135 LSS-WG; Isler, B. 외 (BACnet International)",
      "title": "Physical Access Control with BACnet (BAC-09-08 White Paper)",
      "published": "2008-09-27",
      "url": "https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "BACnet 으로 출입통제를 구현하기 위한 확장을 설명한 124쪽 백서. 표준 변경 제안의 기초 작업 문서이며 인증과 권한 검사를 구분한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1496",
      "org": "NAVER LABS",
      "title": "NAVER’s ARC Goes to Japan",
      "published": "2026-07-23",
      "url": "https://naverlabs.com/en/blogDetail?seq=10034507",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "NAVER 다중 로봇 플랫폼 ARC 의 Tokyo Midtown Yaesu 도입 소개. 기존 화물 승강기·자동문 연동과 연말 전 층 확대 계획을 공급자 관점에서 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
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
      "rationale": "갱신(차등): 섹션 3 — 국토부 연구개발의 2028년 완료 예정·기술표준·인증제도 개선 과제(f2·f3, 보도자료 원문 미열람이라 [추정]·'2차 보도 기준', 보도 날짜는 2025-05-28 기사 기준이며 ref-322 발행일은 미확인 유지). KS B 7317 문장은 기존 '2021년 11월 제정'을 유지하고 개정 이력(2022-12-09·2025-05-09)과 적용 범위(병원 환자 전용 엘리베이터 제외)를 덧붙임(f4·f5); ref-314 발행일을 현행 개정일 2025-05-09 로 갱신 제안 / 섹션 4(분리 2026-09-25-area10-s4) — '승강기 세션과 모드' 항목에 AGV 모드 전환 완료 뒤 session_id 보고 권고와 AGV 모드 없는 승강기(f9·f10); LiftState session_id 정의·모드 상수는 기존 내용 확인(같은 페이지 승강기 세션 항목, 2026-10-10-charging-threshold-charger-lift-evidence, 2026-09-25-area16-s4)이라 새로 넣지 않음 / 섹션 5 — 현장 유형 '기타(도서관)' 실제 설비 연결 사례: 새로 단 승강기 제어함 PLC(Beckhoff CX9020)·ADS·드라이 접점·승강기 업체 AGV 모드 개조(f21), 화재 경보 뒤 PLC 오류 유지·수동 재시작(f22), 메시지 주기 기재 불일치는 결론 없이(f23). '상업 시설' 사례로 NAVER ARC Yaesu(f37, 벤더 주장·계획 구분, f50) / 섹션 6 — 어댑터 요청·상태 감독: lift_supervisor 의 같은 세션 갱신·종료 처리와 잔류 세션 종료 반복 발행, 배정 규칙 미구현 TODO(f11·f12), 변경기록 2.13.0 #510(f13, 2.14.0 존재 병기); lift_supervisor 존재 자체는 기존 내용 확인(categories/integration/index.md 110행). 요청–결과 인계: DispenseItem 의 SUCCESS 완료·큐 소거 완료 간주(f14·f15)와 위험 해석(f16, [추정]); DispenserResult·IngestorResult 의 ACKNOWLEDGED·SUCCESS·FAILED 값 정의는 기존 내용 확인(planning-and-optimization/task-and-workflow-modeling.md 86행)이라 넣지 않음. 제조사 어댑터: KONE API v2.0 WebSocket·자격증명(f17·f18; The Galen 실기 시험은 기존 내용 확인 — ref-884, robot-ontology/ontology-based-system-and-robot-integration.md 102·113행), Dormakaba IoT connector·자격증명(f19·f20). 물리 인계 예시: OMRON(f24·f25, 원문 미열람 [추정]) / 섹션 7(분리 2026-09-25-area10-s7) — KOLA 행 '표준 번호·제정일·내용은 미확인'을 정정: 협회 보도자료(f6·f8, 게시일 2026-03-27)와 e-나라표준인증 목록 B-KOLA-0001-7700·등록일자 2026-03-24(f7)를 날짜가 다르다는 점과 함께, 메시지·RMF 대응은 미확인 유지; 제정 사실 자체는 기존 내용 확인(같은 페이지 ref-316, 2026-09-25-area10-s8 ref-317). KS B 7317 행에 개정 이력·적용 범위(f4·f5). SEMI E84 행 추가 또는 2026-09-25-area17-s7 41행 연결: E84-0823 현행판(f26), Doc7442 개발 제안(f27, 원문 미열람 [추정]). BACnet 출입통제 백서는 표준 변경 제안 작업 문서로(f35·f36) / 섹션 8(분리 2026-09-25-area10-s8) — '원문을 열지 못해 결과 수치는 쓰지 않는다' 문장 갱신: 병원 논문의 EOR 임계값 재보정 명시(f28, 새 내용), 공유 승강기 지연 독립 교차 확인(f30), Han 외는 실제 평면으로 거리 행렬만·수요는 무작위 표본·기본 대기 30초(f31), Kim 외 15층·소포 1·3·5·7(f32), 노주형 외 N1 5~9층 각 층 절반 영역·19/20(f33·f34). Park·Park 설계 기준 논문은 '초록 기준'으로(f1). 기존 내용 확인으로 넣지 않는 것: 병원 논문의 122건·실패 14건 분류(통신 2·막힘 8)·87.03%·59.01%·95.52%(objects-people-and-live-state/people-and-pedestrian-model.md 101~108행, 2026-09-29-area63-s4·s6·s8, design-and-simulation/virtual-commissioning-and-real-situation-replay.md, 2026-09-25-area03-s8), Han 외 승강기 운행 40~100초(planning-and-optimization/shared-resource-charging-and-energy-optimization.md 96~108행, 2026-09-25-area28-s3), 노주형 외 5개 층·27분·95%·버튼 조작(chat-based-configuration-and-operation/chat-map-authoring.md 113행, 2026-09-25-area06-s8, 2026-09-25-area21-s8) / 섹션 9 — 설비 제어 경계: 화재 복구·PLC 재시작은 연계 대상(설비), ROP 는 복구 책임자 지정과 시험(f22·f46); 출입통제는 문 열기 요청과 통행 권한 승인 분리(f36·f45) / 섹션 10(분리 2026-09-25-area10-s10) — 63. 병원·의료(f28·f30), 64. 상업 시설(f37·f1), 51. 인증·권한·격리(f35·f36·f45), 30. 로봇 간 협업·물리적 인계(f14~f16·f24~f27), 32. 예외 복구·재계획·업무 연속성(f22), 50. 안전 표준·인증·사고 조사(f4·f5) / 섹션 11(분리 2026-09-25-area10-s11) — 부분 근거만, 모두 열림 유지: oq-010(f28·f30~f34·f48), oq-041(f6~f10·f40), oq-283(f7 표준 번호 공개, 책임 분담은 미확인), oq-042(f24~f27·f47), oq-062(f26·f27), oq-043(f19·f20·f35·f36·f45), oq-098·oq-173·oq-311(f4·f5, 조항·기준값은 미확인), oq-067·oq-094(f11·f12, 배정 규칙 미구현), oq-215(f29, 분모 설명 없음 재확인 — 새 질문 아님), oq-258·oq-328(f28). 새 질문 6건. 넣지 않는 것: 외부 메모 F01(스마트도시협회 REEC 운영 사무국 — 기존 내용 확인: glossary/robot-friendly-building-certification.md, 2026-09-29-area64-s4 41행·s7 42행; 이번 원문은 접근 제한으로 미열람), F02(평가 분야 4개 명칭 — 확인 불가이고 기존 용어집의 4개 부문 명칭(건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스)과 충돌, 원문 재확보 필요). 다음 실행 후보: 64. 상업 시설(REEC 현행 심사 기준), 30. 로봇 간 협업·물리적 인계(OMRON·Doc7442 원문 재확보), 51. 인증·권한·격리(BACnet 출입통제)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "KS B 7317 의 2022-12-09 개정과 2025-05-09 개정은 각각 어떤 조항(요구사항·평가 방법)을 바꿨으며, 그 변경이 승강기 연동 계층이 확인해야 할 항목에 영향을 주는가? (관련 기존 질문: oq-098, oq-173, oq-311) | 관련 영역: 22. 설비·건물 시스템 연동, 50. 안전 표준·인증·사고 조사 | 근거: f4 | 종류: 일반",
    "로봇 친화형 건축물 인증의 현행 심사 기준은 어느 판이며, 승강기·자동문·출입통제 연동 항목을 어떤 시험이나 서류로 심사하는가? (관련 기존 질문: oq-179) | 관련 영역: 22. 설비·건물 시스템 연동, 64. 상업 시설 | 근거: f1 | 종류: 일반",
    "KONE 의 현행 공식 승강기 API 계약(지원 승강기, 건물 등록, 권한 범위, 세션 유지 조건)은 2023년 고정판 공개 RMF 어댑터가 전제한 KONE API v2.0 연결 조건과 어떻게 다른가? | 관련 영역: 22. 설비·건물 시스템 연동, 20. 로봇·제조사 관제 연동 | 근거: f17 | 종류: 일반",
    "SEMI Doc 7442(E84 를 출발점으로 한 새 인계 인터페이스와 TCP/IP 하위 규격) 개발 제안은 승인 뒤 표준으로 발행됐는가, 반도체 밖 이동로봇–설비 인계에도 쓸 수 있는 범위인가? (관련 기존 질문: oq-042, oq-062) | 관련 영역: 22. 설비·건물 시스템 연동, 30. 로봇 간 협업·물리적 인계 | 근거: f27 | 종류: 일반",
    "HopeTechnik 승강기·문 연동 문서가 승강기 상태 전송 주기를 1 Hz 와 2초마다로 다르게 적은 것은 어느 쪽이 실제 구현·설정이며, 이런 주기 차이가 설비 상태를 믿을 수 있는 경과 시간 판단에 어떤 영향을 주는가? (관련 기존 질문: oq-034) | 관련 영역: 22. 설비·건물 시스템 연동, 18. 실시간 세계 상태·데이터 일관성 | 근거: f23 | 종류: 일반",
    "NAVER ARC 의 Tokyo Midtown Yaesu 도입에서 기존 화물 승강기·자동문 연동이 실제로 운영 중인 층·로봇 종류·제조사 범위는 어디까지이며, 공급자 밖의 독립 운영 평가가 있는가? | 관련 영역: 22. 설비·건물 시스템 연동, 64. 상업 시설 | 근거: f37 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 22,
    "cross_checked_count": 1,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-03/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f2·f3: 국토부 보도자료 원문(MOLIT·CODIL)을 열지 못해 사업기간 2025~2028, 보도 2025-05-28·배포 2025-05-27, '3쪽'은 미확인 — 2차 보도(ref-1484) 기준 [추정]",
      "f1: Park·Park 논문은 초록·Crossref 서지만 확인(본문 미열람). 메모의 '현장실험이 아닌 기존 인증기준 비교' 중 '현장실험이 아닌'은 단정하지 않음. 메모 서지 '28,14' 는 28(1), 논문번호 14 로 정정",
      "메모 F01(스마트도시협회 REEC 운영 사무국)·F02(평가 분야 4개): 스마트도시협회 페이지가 접근 제한으로 열리지 않음. F02 명칭은 기존 용어집 4개 부문 명칭과 달라 충돌 — 원문 재확보 필요, 출처·finding 에서 뺌",
      "f7: e-나라표준인증 목록의 등록일자(2026-03-24)와 KOLA 게시일(2026-03-27)이 다르며 정확한 제정일은 미확인. 가이드라인 본문의 메시지·상태 정의, Open-RMF 대응 미확인",
      "f4·f5: KS B 7317 표준 본문·신구대비표 미열람 — 개정 조항 미확인",
      "f24·f25: OMRON I680-E-02 PDF 접근 거부(Access Denied)로 원문 미열람 — 메모 서술만 근거라 [추정], 메모의 2023-05 판 날짜도 미검증",
      "f27: SEMI Doc 7442 SNARF 페이지 봇 차단으로 원문 미열람 — 작성일 2025-12-17·승인일 2025-12-18 미검증, [추정]",
      "커밋 일자 4건(rmf_internal_msgs 2a7f01b 2026-09-22, rmf_ros2 4cea3fe 2026-10-08, KONE 어댑터 9bc3a87 2023-07-13, door_adapter_dormakaba 2cf76a6 2025-06-16)은 확인하지 못해 해당 출처 published 를 null 로 둠",
      "f17·f18: KONE 어댑터 README 는 KABAM-Robotics 보존 저장소 판이며 원 저장소(sharp-rmf/kone-ros-api)와 현행 KONE 공식 API 계약은 대조하지 않음. The Galen 실기 시험은 프로젝트 자체 보고",
      "f23: HopeTechnik 문서의 1 Hz/2초 차이를 설명하는 구현·설정 근거 없음. 문서 발행일 미확인",
      "f29: 87.03% 의 분모는 원문으로 설명되지 않음(oq-215 열림 유지)",
      "f37: NAVER Yaesu 운영 범위는 공급자 블로그뿐이며 독립 평가 없음(벤더 주장)",
      "메모 U06(현대엘리베이터 현행 API 원문)·U07(TTA 10.1486 본문)은 이번 메모에 근거 finding 이 없어 열린 질문으로 올리지 않음",
      "벤더 문서만 근거인 f21~f23 은 원문 대조로 문서 내용은 확인했으나, 저장소 규칙(6.2 항목 13)에 따라 독립 출처 교차 확인 전까지 vendor_claim: true·[추정]으로 둔다."
    ],
    "scope_violations": [
      "f19·f21·f22: 문 구동기 하드웨어(IoT connector), 승강기 제어함 PLC·드라이 접점, 화재 경보 시 설비 복귀는 분류 원문 19장의 '승강기·컨베이어·PLC·설비 안전 제어' 연계 대상이므로 claim 을 '연계 대상: '으로 시작하고, ROP 몫은 요청·상태 확인과 복구 책임 정의(f46)로 한정",
      "f4·f5·f39: KS B 7317 은 로봇 자체의 탑승 안전 요구사항으로 이 영역에는 제약 조건·판 정보로만 씀(48·50번 안전 영역 쪽 내용)",
      "f35·f36·f45: BACnet 출입통제의 권한 검사는 51. 인증·권한·격리 쪽 내용이 많아 이 영역에는 문 열기 요청과 통행 승인 분리 근거로만 씀",
      "f26·f27·f47: SEMI E84·Doc7442 는 반도체 업종 규격으로 이 영역에는 인계 신호 구조의 참고로만 쓰고 물류센터 적용을 주장하지 않음",
      "f28~f30: 병원 승강기 연구의 수치는 63. 병원·의료에서 이미 다루므로 이 영역에는 새 내용(재보정 명시·지연 교차 확인·분모 재확인)만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 14
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 14건/15(ref-1483~ref-1496, 예약 구간 ref-1483~ref-1512 안), 재사용 8건(ref-322·ref-314·ref-1398·ref-202·ref-943·ref-103·ref-321·ref-163). 출처 매핑(검증 결과 기준): 메모 n2→ref-1483, n3→ref-322(같은 국토부 보도자료, 기존 제목·URL 유지)+2차 보도 ref-1484, n4→ref-314(e-나라표준인증 상세로 열람, 발행일을 현행 개정일 2025-05-09 로 갱신), n5→ref-1485, KOLA 표준 번호→e-나라표준인증 단체표준 목록 ref-1486, n7→CHANGELOG ref-1398·lift_supervisor ref-1488·DispenseItem ref-1489, n8→ref-1487, n9→ref-1490, n10→ref-1491, n11→ref-1492, n12→ref-1493(미열람), n13→ref-202, n14→ref-1494(미열람), n15→ref-943, n16→ref-103, n17→ref-321, n18→ref-163, n19→ref-1495, n20→ref-1496. n1(스마트도시협회)은 근거 finding 이 기존 내용 중복(F01)·충돌(F02)이라 출처에서 뺐고, n6(rmf_internal_msgs: ref-286·ref-499·ref-049)은 근거 finding 이 기존 내용 중복(LiftState session_id 정의, 결과 상태값 정의)이라 넣지 않음. 기존 ref 갱신 제안: ref-103 저자(Han, L. 외)·발행일 2025-03-13, ref-321 저자(Kim, S. 외)·발행일 2025-02-28, ref-163 발행일 2026-03·권호 21(1), ref-314 발행일 2025-05-09·이력, ref-202 현행판 E84-0823. fetched: true 는 검증 서브에이전트가 2026-10-11 원문을 내려받아 대조한 출처이고, fetched: false 는 ref-322·ref-1493·ref-1494. ref-1483 은 초록·서지만 확인. 교차 확인 1건(f30: 고려대 구로병원·도구공간 논문과 KAIST 논문, 서로 다른 기관의 질적 관찰). 메모 X01 외 나머지는 단일 출처라 신뢰도 medium 이하. 벤더 주장은 f37(vendor_claim, [추정]). 현장 유형: 병원(f28·f29), 기타(도서관, f21~f23), 상업 시설(f37). 물류창고 실측 자료는 이번에도 없음(oq-010 열림). 열린 질문 해결 제안 없음 — 모두 부분 근거: oq-010 근거 f28·f30~f34·f48, oq-041 근거 f6~f10·f40, oq-283 근거 f7, oq-042 근거 f24~f27·f47, oq-062 근거 f26·f27, oq-043 근거 f19·f20·f35·f36·f45, oq-098·oq-173·oq-311 근거 f4·f5, oq-067·oq-094 근거 f11·f12, oq-215 근거 f29, oq-258·oq-328 근거 f28. 메모의 '새1~새3'은 고유 id 가 없는 질문이 아니라 docs/open-questions.md 의 oq-041·oq-042·oq-043 과 같은 질문임을 질문 문장으로 확인했다. 메모 U01=oq-010, U02=oq-041·oq-283, U09=oq-042, U10=oq-043, U13=oq-215 이므로 새로 만들지 않았다. 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 실제 위키 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-11-03/verification.json

```json
{
  "run_id": "2026-10-11-03",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Crossref 서지(Park, Youngsup·Park, Sungho, Architectural Research 28(1), 논문번호 14, 온라인 2026-07-21)와 Springer 초록 일치. 초록은 REEC 를 'Robotics-Enabled Environment Certification'으로 표기하고 BF 인증과 비교해 설계 기준을 도출했다고 적는다. 본문 미열람이라 연구 방법은 단정하지 않는다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. ref-1484(스마트투데이 2025-05-28, 이재수) 열람: '29일 … 착수보고회를 열고 … 28일 밝혔다', '2028년까지 완료될 예정'. 보도 시점에 착수보고회는 예정이었으므로 '열었다'고 쓰지 않는다(수정 지시). 기사의 사업명 문장은 오기가 있어 사업명을 확정하는 근거가 아님. ref-322 원문 미열람."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 기사가 세 세부 중점과제 가운데 하나로 '기술 실증을 통한 기술표준 및 인증제도 개선방안 마련'을 든다. ref-322 원문 미열람, 이후 진행 미확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: e-나라표준인증 KS B 7317 상세(standard.go.kr)에서 2021-11-30 제정(2021-0561), 2022-12-09 개정(2022-0571), 2025-05-09 개정(2025-0073) 이력 일치. 개정 조항 미확인. 트랙 반영 제안(2026-09-25-65)의 '2021-11-11 제정'은 이 고시일과 다르다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 적용 대상 엘리베이터는 '병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터', 표준개발협력기관은 한국AI·로봇산업협회, 담당은 국가기술표준원 기계융합산업표준과로 일치."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "KOLA 게시물(kola.or.kr)은 검증 단계에서 두 번 모두 TLS 인증서 오류로 열리지 않음. 같은 날(2026-03-27) 이뉴스투데이 기사가 같은 제정 문구를 실어 대조했다. 그 기사는 보도자료를 옮긴 것이어서 독립 출처로 세지 않는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-1486 URL 은 단체표준 목록 첫 쪽(4,019건 중 10건)만 보여 주며, B-KOLA-0001-7700 행은 검증에서 재현되지 않았다. 표준 번호를 정확 일치로 검색해도 결과가 없다. 표준 번호·등록일자 2026-03-24 는 리서치 단계의 열람에만 기댄다. 목록 검색 조건이 URL 에 없어 fetched 표시의 근거가 약하다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "KOLA 원문 열람 실패(TLS). 이뉴스투데이 2026-03-27 기사에서 '일반사항, 시험 설비 및 시험 절차', 'e-나라표준인증에 등록게재 … 무료로 다운로드' 문구를 확인했다(보도자료 기반이라 독립 출처 아님). 메시지·상태 정의는 미확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Discourse 아카이브의 제목(#513)과 날짜 2024-08-21 일치. mxgrey 답변 'should not broadcast the session_id value until it has finished switching into that mode' 확인. 설계 의도 설명이다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'Some lifts might not have a special AGV mode'."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 커밋 4cea3fe 의 Node.cpp. _adapter_lift_request_update 에 session_id 비교가 있고, REQUEST_END_SESSION 이 아니면 갱신, 맞으면 종료 발행 뒤 curr_request = nullptr 로 비운다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: _lift_state_update 주석 'we keep publishing session end requests to ensure that the lift gets released'. TODO(MXG) 주석은 _adapter_lift_request_update 안에 있다(주장은 위치를 특정하지 않으므로 문제없음)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CHANGELOG 2.13.0(2026-06-15)의 'emit completion legacy state if lift is already on the level (#510)'. 최신 2.14.0(2026-09-26) 존재도 확인했다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: DispenseItem.cpp _get_status. request_guid 일치 시 ACKNOWLEDGED → _request_acknowledged=true, SUCCESS → STATE_COMPLETED, FAILED → STATE_FAILED."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: request_guid_queue 에 들어 있으면 접수로 표시하고, 접수 뒤 큐에서 사라지면 완료로 처리한다. 주석 'if it's no longer in the queue, then we'll assume it's finished'."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정(구현에서 도출한 위험 해석) 유지. 코드에 큐 소거 원인을 구분하는 분기가 없다는 점까지만 근거가 된다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 의 KONE API v2.0 WebSocket 명령 전송과 상태 수신, CHART 개발, sharp-rmf/kone-ros-api 원 저장소. 공개 어댑터 기준이며 현행 KONE 계약이 아니다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'To control a live elevator, you will need to get these id & secret from KONE Personnel.' The Galen 시험 문구는 기존 위키(ref-884)에 있다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: EL301·ED250 시험과 IoT connector 장착 요구('fitter' 오기 원문). '연계 대상' 표시가 적절하다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'Credentials to access the door's cloud API will be provided by Dormakaba.'"
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. 도서관 현장, PLC 를 넣은 승강기 제어함, Beckhoff CX9020, ADS, 드라이 접점, AGV 모드 개조 모두 확인했다. 제어함 위치는 개요('level 6 cargo lift lobby')와 본문('service lift 4 lobby')이 달라 위치를 특정하지 않는다. 발행일·작성 주체 명시 없음(HopeTechnik 은 제목 표기)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Table 1 #2 Fire Alarm 행의 조치는 승강기 수동 모드 전환·PLC 오류 상태·경고음이고, 복구는 'Manual intervention is needed. PLC will stay in error state until it is restarted.' 벤더 주장 유지."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 개요의 LiftState 1 Hz 와 서버 절의 '2초마다'(0.5 Hz)가 충돌한다. LiftRequest 는 1초마다. 결론 보류가 맞다."
    },
    {
      "finding_id": "f24",
      "source_exists": false,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "삭제",
      "note": "ref-1493(OMRON I680-E-02) URL 은 검증에서도 403. 문서 번호·제목으로 검색해도 이 안내서가 나오지 않아 존재를 확인하지 못했다. 근거는 외부 AI 조사 메모의 전언뿐이므로 출처 없는 내용으로 본다. oq-042 는 열림을 유지한다."
    },
    {
      "finding_id": "f25",
      "source_exists": false,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "삭제",
      "note": "f24 와 같은 이유(ref-1493 존재 미확인, 메모 전언뿐)."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: SEMI 판매 목록에서 E84-0823 이 Current, E84-1109 등이 Superseded로 표시된다. 초록 'more reliable and efficient carrier handoffs (load/unload) at production equipment load ports' 확인. 표준 본문 미열람."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(원문 미열람). 검색 결과 요약에서 SEMI downloads 페이지(같은 문서 id)를 확인했다. 확인한 내용: Doc 7442 SNARF, E84 물리 I/O 대신 TCP/IP 인계를 제안하고 하위 규격 Doc 7443 을 둠, 반도체 조립·시험 범위, 작성일 2025-12-17. 같은 요약에 2026-07-29 SEMI 투표 요약에서 7442·7443 이 Passed로 나온다는 내용이 있으나 브리프 밖 정보라 넣지 않는다. 표준 발행은 미확인. '외부 조사 메모가 전한다' 표현은 지운다(수정 지시)."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC13039597 §4.5 'should be interpreted as site-specific and is expected to require recalibration…'. 이유로 카 크기·운반 카트·탑승자 구성을 든다. Digital Health 12, 2026-03-31."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 대상 122건, 실패 14건(§3.2), §3.4 의 완료 108건. 'all trials' 정의가 없고 108/122≈88.52% 로 87.03% 와 맞지 않는다. 보고값을 고치지 않고 불일치만 적는다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: ref-943 초록 'An increased EOR also prolonged the delivery time'과 ref-163 §3.3(jkros 전문)의 외부 이용자로 인한 6층→7층 구간 지연(Table 4 의 3:00)을 확인했다. 발행 기관이 다른 독립 출처다(질적 관찰). 단 ref-163 발행일은 2026-02-28 이다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Han·Ding·Liu·Meng, Sensors 25(6):1783, 2025-03-13. 실제 평면·층고로 만든 68×68 거리 행렬, 시나리오별 방 무작위 선택(10·20·30·60), 승강기 기본 대기 30 s. 수치 실험이다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "초록(PDF 메타)에서 '15-story simulation with varying parcel counts', n=1~7 을 확인했다. MDPI 본문(403)과 §5 는 판독하지 못해 1·3·5·7 이라는 이산값은 검증에서 재현하지 못했다. 저자 6명·2025-02-28 확인."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: jkros 전문 §3.3 '각 층의 절반 영역', KCI 초록 KAIST N1 5F–9F. 발행일은 jkros 기준 2026-02-28(브리프의 2026-03 아님)."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Table 5 Elevator Interaction 19/20(95%)."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "PDF 본문은 판독 실패(압축 스트림). 검색 결과 요약에서 BAC-09-08 의 2008-09-27 날짜와 'ongoing work of the SSPC135 LSS-Working Group and the basis for proposed changes to the BACnet standard … subject to change'를 확인했다. 이후 Access Door 등은 ASHRAE 135 부록(addenda)으로 채택됐다는 기사도 있어 현행 규범 본문이 아님을 밝히는 것이 맞다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. PDF 본문 판독 실패(두 URL 모두)로 '특정 시간에 특정 문을 통과할 권리' 문장과 인증·권한 검사 구분을 검증에서 재현하지 못했고, 검색 요약에도 이 내용이 없다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정·벤더 주장 유지. NAVER LABS 2026-07-23 블로그에서 화물 승강기·자동문·출입 경로의 중앙 통합과 연말 전 층 확대 계획을 확인했다. 블로그는 건물을 'a commercial building'으로 적으므로 현장 유형 '상업 시설'이 맞다. 이름이 나온 로봇은 Rookie 뿐이다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견 표시 확인. 근거 출처 실재(ref-322 는 원문 미열람)."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f4·f5 근거 확인."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. 근거 가운데 ref-1486 목록 행은 검증에서 재현하지 못했으나(f7) 의견의 취지(본문 확보 후 대응표 작성)에는 영향 없음."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f9·f10 근거 확인."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f11·f12 근거 확인."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f14·f15 근거 확인."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f17·f18 근거 확인."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. ref-1491 확인, ref-1495 의 인증·권한 구분은 검증에서 재현하지 못했으므로(f36 강등) 그 부분은 추정 근거로만 언급한다."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f22 근거 확인."
    },
    {
      "finding_id": "f47",
      "source_exists": false,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견 유지. 근거 가운데 ref-1493 은 존재 미확인이라 빼고 ref-202(E84 인계 신호)만 근거로 둔다(수정 지시)."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. 병원 논문의 재보정 명시, 호텔·그래프 연구의 수치 실험 성격, 로봇 한 대의 실물 지도 구축이라는 근거를 모두 확인했다."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. KCI 초록으로 KAIST 사례의 버튼 조작(4자유도 매니퓰레이터)을 확인했다. 병원 사례의 제어반 통신 모듈은 기존 위키 서술에 기댄다."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "구축자 의견. f37 근거 확인(전 층 확대는 계획)."
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
      "ref-943(PMC13039597)과 기존 각주 ref-060(doi 10.1177/20552076261437181)은 같은 논문(Lee, Y. 외, Digital Health 2026)이다. 이 페이지의 기존 문장은 ref-060 을 유지하고 새 문장은 ref-943 을 써도 되지만, 두 id 통합은 참고문헌 정리 대상이다",
      "f6·f8 의 KOLA 단체표준 제정은 기존 각주 ref-316(건설기술신문)·ref-317 과 겹친다. 협회 1차 자료(ref-1485)로 보강하는 것이며 새 사실은 대상 범위·무료 공개뿐이다",
      "트랙 반영 제안 2026-09-25-65 요약의 'KS B 7317 2021-11-11 제정'은 f4 의 e-나라표준인증 고시일 2021-11-30 과 다르다"
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
    "f24·f25: 삭제한다. ref-1493(OMRON I680-E-02)은 검증에서 403 이었고 검색으로도 존재를 확인하지 못했으며, 근거가 외부 조사 메모의 전언뿐이다. 6절 '물리 인계 예시' 문단, 10절 30. 로봇 간 협업·물리적 인계 연결 근거, 11절 oq-042 부분 근거, 각주, reference_updates 에서 ref-1493 을 모두 뺀다.",
    "f47: 근거 출처에서 ref-1493 을 빼고 ref-202 만 각주로 단다. [의견]과 '구축자 의견' 표시는 유지한다 — ref-1493 은 존재 미확인 출처다.",
    "f7: [사실]을 [추정]으로 강등한다. 'e-나라표준인증 단체표준 목록에 표준번호 B-KOLA-0001-7700·등록일자 2026-03-24 로 올라 있다'는 내용은 리서치 단계 열람에만 기대고 검증에서 재현하지 못했음을 문장에 밝힌다. 7절 KOLA 행과 oq-283 부분 근거의 표준 번호도 같은 수준으로 쓴다. 이유: ref-1486 URL 은 목록 첫 쪽만 보이고 해당 행이 없으며, 정확 일치 검색에서도 나오지 않는다.",
    "f36: [사실]을 [추정]으로 강등한다. BAC-09-08 의 인증·권한 검사 구분과 '특정 시간에 특정 문 통과 권리' 예시는 PDF 판독 실패로 검증에서 재현하지 못했다. f45 의견은 Dormakaba 자격증명(f20)을 주 근거로 쓰고 BACnet 쪽은 추정 근거로만 언급한다.",
    "f35: BAC-09-08 은 2008-09-27 작업 문서이고 현행 ANSI/ASHRAE 135 규범 본문이 아님을 7절 문장에 그대로 밝힌다(브리프 표현 유지). 이후 부록(addenda) 채택 여부처럼 브리프에 없는 내용은 덧붙이지 않는다.",
    "f2: '2025년 5월 착수보고회를 열고'를 '2025-05-29 착수보고회를 열 예정이라고 2025-05-28 보도됐다'로 고친다 — 출처 기사는 보도 시점에 착수보고회를 예정으로 적었다. 사업명은 기존 ref-322 보도자료 제목을 쓰고, 기사 문장을 사업명의 근거로 삼지 않는다.",
    "f2·f3·f27: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-322·ref-1494 에 source_unopened: true 를 넣는다 — 두 출처는 원문을 열지 못했다.",
    "f27: '외부 조사 메모가 전한다'는 표현을 지운다. 'SEMI 물리 인터페이스·캐리어 기술위원회(일본)의 Doc 7442 신규 예비 표준 개발 제안서(SNARF, 작성 2025-12-17)는 E84 를 출발점으로 인계 인터페이스 규격과 TCP/IP 하위 규격을 제안한다'로, 반도체 조립·시험 범위와 표준 발행 미확인을 함께 [추정]으로 쓴다 — 검증에서 검색 결과 요약으로 내용은 맞음을 확인했으나 원문은 미열람이다.",
    "ref-163: 발행일을 2026-03 이 아니라 2026-02-28(로봇학회 논문지 21(1):48–57)로 쓰고, f30·f33·f34 문장의 기준일도 2026-02-28 로 맞춘다 — jkros 게재 정보 기준.",
    "f32: '소포 1·3·5·7개'는 검증에서 본문으로 재현하지 못했다. 초록이 확인한 범위인 '15층 건물 그래프 시뮬레이션에서 소포 수 1~7개'로 쓰고 시뮬레이션 평가임을 밝힌다.",
    "트랙 반영 제안 2건(2026-09-25-65 문 설비 연동·IFC HasDrive·로봇 조작과 설비 연동의 선택 조건, 2026-09-25-76 승강기 층 이름과 지도 층의 대응표)은 브리프에 근거 finding 이 없다. 6절에 반영하지 말고, changelog_entry 와 additional_research_requests 에 '이번 실행 미처리 — 근거 finding 없음, 다음 22. 설비·건물 시스템 연동 실행으로 이월'을 적는다. 특히 2026-09-25-65 요약의 'KS B 7317 2021-11-11 제정'은 f4 의 고시일 2021-11-30 과 다르므로 페이지에 쓰지 않는다.",
    "직접 인용: 출처당 한 번, 짧은 구절만 쓴다. ref-1492(f21~f23), ref-1487(f9·f10), ref-1488(f11·f12), ref-1489(f14·f15), ref-943(f28~f30)처럼 한 출처에서 여러 발췌가 있으면 하나만 인용하고 나머지는 재서술한다.",
    "f1: '로봇 친화형 건축물 인증'은 용어집 robot-friendly-building-certification 으로 연결한다. 초록의 영문 표기(Robotics-Enabled Environment Certification, REEC)는 병기만 하고 새 용어로 등록하지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 45건, 미확인 5건, 교차 확인 1건(f30: 고려대 구로병원·도구공간 논문과 KAIST 논문, 공유 승강기 지연의 질적 관찰). 강등: f7 사실 → 추정(단체표준 목록 행 재현 불가), f36 사실 → 추정(BACnet 백서 본문 판독 실패). 삭제: f24·f25(ref-1493 OMRON 안내서 존재 미확인 — 403, 검색 불일치). 원문 미열람 출처: ref-322, ref-1494(검색 결과 요약으로 내용 대조), ref-1493(제외). 검증 단계 열람 실패: ref-1485(KOLA, TLS 오류, 같은 날 보도로 대조), ref-1486(목록 행 재현 불가), ref-1495(PDF 판독 실패, 검색 요약으로 f35만 대조), ref-321(본문 403, 초록으로 대조). 주의: 대부분의 주장은 단일 출처이며 Open-RMF 코드·README 와 한 도서관 현장의 벤더 문서(f21~f23)에 기댄다. Open-RMF 구현 분석은 설계 의도와 코드 동작이지 현장 안전 동작의 재현이 아니다. KS B 7317 개정 조항, KOLA 가이드라인의 메시지 정의와 Open-RMF 대응, 물류창고 승강기 병목(oq-010)은 여전히 미확인이다. ref-060 과 ref-943 은 같은 논문이므로 참고문헌 정리가 필요하다. 트랙 반영 제안 2건(2026-09-25-65, 2026-09-25-76)은 이번 브리프가 다루지 않아 다음 22. 설비·건물 시스템 연동 실행으로 이월한다. 브리프의 검색 횟수는 외부 조사 변환이라 집계되지 않았다(검증 검색 8회). 정정 요청 없음. 열린 질문 해결 인정 없음.",
  "retry_reason": null
}
```

### runs/2026-10-11-03/pages.json

```json
{
  "run_id": "2026-10-11-03",
  "outline": [
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1400,
      "summary": "VDA 5050 3.0.0 은 주변 설비 인터페이스를 범위에서 빼므로 설비 연동은 따로 설계해야 하고, 실제 건물에서 공유 승강기 지연이 두 연구에서 보고됐다. [사실][^ref-031][^ref-943][^ref-163] KS B 7317 은 2021-11-30 제정 뒤 두 차례 개정됐다. [사실][^ref-314]",
      "planned_findings": [
        "f30",
        "f4",
        "f5",
        "f2",
        "f3",
        "f38"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 350,
      "summary": "Open-RMF 개발자는 AGV 모드 전환을 마칠 때까지 승강기 상태에 session_id 를 내보내지 말라고 권고했다. [사실][^ref-1487]",
      "planned_findings": [
        "f9",
        "f10"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2300,
      "summary": "기타(도서관) 현장의 승강기 제어함 PLC·드라이 접점 연결과 화재 뒤 수동 복구, 병원 승강기 가동률 임계값의 재보정 필요, 상업 시설의 승강기·자동문 중앙 연결 발표를 사례로 더한다. [추정] 벤더 주장[^ref-1492]",
      "planned_findings": [
        "f21",
        "f22",
        "f23",
        "f28",
        "f29",
        "f30",
        "f37",
        "f48",
        "f50"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2300,
      "summary": "Open-RMF 승강기 감독자는 같은 세션 요청을 갱신·종료로 처리하고 잔류 세션에 종료 요청을 반복하며, 디스펜서 단계는 SUCCESS 또는 대기열 소거로 완료를 판정한다. [사실][^ref-1488][^ref-1489]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f41",
        "f42",
        "f43",
        "f44",
        "f49"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1900,
      "summary": "KS B 7317 개정 이력, KOLA 단체표준의 대상 범위, SEMI E84 현행판과 Doc 7442 개발 제안, BACnet 출입통제 백서의 지위를 표로 정리한다. [사실][^ref-314][^ref-1485][^ref-202][^ref-1495]",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f26",
        "f27",
        "f35",
        "f36",
        "f39",
        "f40"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1500,
      "summary": "승강기를 포함한 다층 이동 연구는 실물 실증·수치 실험·시뮬레이션으로 조건이 다르다. [사실][^ref-943][^ref-103][^ref-321][^ref-163]",
      "planned_findings": [
        "f1",
        "f28",
        "f30",
        "f31",
        "f32",
        "f33",
        "f34",
        "f48"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1200,
      "summary": "화재 뒤 설비 재시작은 연계 대상이고 ROP 는 복구 책임자 지정과 시험을 맡으며, 출입통제에서는 문 열기 요청과 통행 권한 승인을 나눈다. [의견][^ref-1492][^ref-1491]",
      "planned_findings": [
        "f22",
        "f46",
        "f20",
        "f36",
        "f45",
        "f47"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "63. 병원·의료, 64. 상업 시설, 67. 기타 현장, 51. 인증·권한·격리, 30. 로봇 간 협업·물리적 인계, 32. 예외 복구·재계획·업무 연속성, 50. 안전 표준·인증·사고 조사, 20. 로봇·제조사 관제 연동 연결을 더한다. [사실][^ref-943][^ref-314]",
      "planned_findings": [
        "f1",
        "f4",
        "f14",
        "f17",
        "f20",
        "f22",
        "f26",
        "f28",
        "f37"
      ]
    },
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "section": "11. 열린 질문",
      "budget_chars": 1700,
      "summary": "oq-010·oq-041·oq-042·oq-043 등은 부분 근거만 보강돼 열림을 유지하고, KS B 7317 개정 조항·REEC 심사 기준·KONE 현행 API·SEMI Doc 7442 발행·상태 주기 불일치·Yaesu 운영 범위 질문 6건을 새로 올린다.",
      "planned_findings": [
        "f4",
        "f1",
        "f17",
        "f27",
        "f23",
        "f37"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/integration/facility-and-building-system-integration.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 3절 공유 승강기 지연 교차 확인·KS B 7317 개정 이력·국토부 연구개발 2차 보도; 4절 AGV 모드와 세션 수락; 5절 기타(도서관)·병원·상업 시설 사례 추가; 6절 승강기 감독·작업대 완료 판정·제조사 어댑터; 7절 표준 보강 표; 8절 연구 실험 조건 갱신; 9절 비상 복귀·출입통제 경계; 10절 연결 8건; 11절 부분 근거·새 질문 6건; 13절 각주 갱신",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              15,
              20,
              21,
              27,
              28,
              29,
              30,
              32,
              35,
              48,
              50,
              51,
              63,
              64,
              67
            ],
            "tags": [
              "승강기 연동",
              "Open-RMF",
              "VDA 5050",
              "작업대 인계",
              "KS B 7317",
              "단체표준"
            ],
            "sources": [
              "ref-023",
              "ref-031",
              "ref-047",
              "ref-049",
              "ref-060",
              "ref-103",
              "ref-163",
              "ref-202",
              "ref-283",
              "ref-284",
              "ref-286",
              "ref-312",
              "ref-313",
              "ref-314",
              "ref-315",
              "ref-316",
              "ref-317",
              "ref-318",
              "ref-319",
              "ref-320",
              "ref-321",
              "ref-322",
              "ref-943",
              "ref-1398",
              "ref-1483",
              "ref-1484",
              "ref-1485",
              "ref-1486",
              "ref-1487",
              "ref-1488",
              "ref-1489",
              "ref-1490",
              "ref-1491",
              "ref-1492",
              "ref-1494",
              "ref-1495",
              "ref-1496"
            ],
            "last_run": "2026-10-11"
          },
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-11-area22-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 설비·건물 시스템 연동 의 \"6. 대표 접근법과 기술\" 절(2,450자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area22-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 설비·건물 시스템 연동 의 \"11. 열린 질문\" 절(1,835자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area22-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 설비·건물 시스템 연동 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,772자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area22-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 설비·건물 시스템 연동 의 \"3. 왜 중요한가\" 절(1,310자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area22-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 설비·건물 시스템 연동 의 \"8. 대표 연구와 자료\" 절(1,246자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area22-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 22. 설비·건물 시스템 연동 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(881자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-11 | 22. 설비·건물 시스템 연동 | 차등 갱신: KS B 7317 개정 이력·대한승강기협회 단체표준·Open-RMF 승강기 감독과 작업대 완료 판정·KONE·Dormakaba 어댑터·SEMI E84·BACnet 출입통제 백서 보강, 기타(도서관)·병원·상업 시설 적용 사례 추가, 대표 연구의 실험 조건 갱신, 새 열린 질문 6건; 트랙 반영 제안 2건(2026-09-25-65, 2026-09-25-76)은 이번 실행 미처리 — 근거 finding 없음, 다음 22. 설비·건물 시스템 연동 실행으로 이월 | run 2026-10-11-03",
  "index_updates": {
    "home_recent": "2026-10-11 — 22. 설비·건물 시스템 연동: KS B 7317 개정 이력, 승강기 단체표준, Open-RMF 승강기 세션 감독·작업대 완료 판정, 도서관·병원·상업 시설 승강기 연동 사례 보강",
    "category_recent": "2026-10-11 — 22. 설비·건물 시스템 연동: 승강기 세션 수락·잔류 세션 처리, 작업대 결과 완료 판정, 제조사 승강기·문 어댑터 자격증명, KS B 7317·대한승강기협회 단체표준·SEMI E84 판 정보, 기타(도서관)·병원·상업 시설 사례 추가",
    "area_recent": "2026-10-11 — 22. 설비·건물 시스템 연동: 3~11절 차등 갱신(승강기 감독·작업대 완료 판정·제조사 어댑터·표준 판 정보·연구 실험 조건·비상 복귀와 출입통제 경계·새 질문 6건), 5절에 기타(도서관)·병원·상업 시설 사례 추가"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-322",
      "org": "국토교통부",
      "title": "올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료)",
      "published": null,
      "url": "https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. 국토부 로봇 친화형 건축물 핵심기술 개발 착수 보도자료로, 이번에도 원문을 열지 못해 보도·배포일과 사업기간은 2차 보도(ref-1484) 기준이다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1484",
      "org": "스마트투데이(이재수)",
      "title": "\"사람과 로봇이 공존하는 스마트 빌딩 앞당긴다\"...국토부 산학협력단과 기술개발 착수",
      "published": "2025-05-28",
      "url": "https://www.smarttoday.co.kr/ko-kr/articles/81933",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "국토부 스마트+빌딩 연구개발 착수 보도. 2025-05-29 착수보고회 예정, 2028년까지 완료 예정, 기술 실증을 통한 기술표준·인증제도 개선방안 등 세부 과제를 전한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1483",
      "org": "Park, Y.; Park, S. (Architectural Research)",
      "title": "Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems",
      "published": "2026-07-21",
      "url": "https://link.springer.com/article/10.1007/s44515-026-00016-y",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "로봇 친화형 건축물 인증과 무장애 인증을 비교해 로봇 적응형 건축 설계 기준을 도출한 논문(28(1), 논문번호 14). 초록과 Crossref 서지만 확인했고 본문은 열지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-314",
      "org": "국가기술표준원(e-나라표준인증·KSSN)",
      "title": "KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법",
      "published": "2025-05-09",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010135682",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B 7317 표준 정보. e-나라표준인증 상세에서 제정(2021-11-30)·개정(2022-12-09, 2025-05-09) 이력과 적용 범위·표준개발협력기관을 확인했다. 표준 본문은 미열람.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1485",
      "org": "대한승강기협회(KOLA)",
      "title": "대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27)",
      "published": "2026-03-27",
      "url": "https://kola.or.kr/pages/61/68/bbs/5705",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KOLA 의 「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」 단체표준 제정 보도자료. 대상(일반사항·시험 설비·시험 절차)과 e-나라표준인증 무료 다운로드를 안내한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1486",
      "org": "국가기술표준원(e-나라표준인증)",
      "title": "단체표준 목록 — B-KOLA-0001-7700 엘리베이터와 로봇의 상호 연동을 위한 가이드라인",
      "published": null,
      "url": "https://www.standard.go.kr/KSCI/grpstd/getGrpStdCrtfcReqst.do?menuId=60372&topMenuId=502&upperMenuId=503",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "e-나라표준인증 단체표준 목록 검색 결과. 리서치 단계 열람에서 KOLA 가이드라인의 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 를 보였으나 검증 단계에서는 해당 목록 행을 재현하지 못했다. 표준 본문은 미열람.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1487",
      "org": "cwrx777; mxgrey (Open Robotics Discourse 아카이브)",
      "title": "Lift session issues - Robot enter lift while lift is still in human mode (#513)",
      "published": "2024-08-21",
      "url": "https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "Open-RMF GitHub 토론 #513 의 Discourse 아카이브. 승강기가 AGV 모드로 바뀌기 전 로봇이 탑승한 문제와, 모드 전환 뒤에 session_id 를 보고하라는 개발자 답변을 담는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1488",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter/src/lift_supervisor/Node.cpp (commit 4cea3fe)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/lift_supervisor/Node.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 승강기 감독자 구현. 같은 세션 요청의 갱신·종료 처리와, 활성 요청 없이 남은 세션에 종료 요청을 반복 발행하는 분기를 담는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1398",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "Changelog for package rmf_fleet_adapter",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rmf_fleet_adapter 변경기록. 2.13.0(2026-06-15)의 승강기가 이미 해당 층에 있을 때 legacy 완료 상태를 내보내는 변경(#510)과 2.14.0(2026-09-26) 존재를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1489",
      "org": "Open-RMF (open-rmf/rmf_ros2 저장소)",
      "title": "rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp (commit 4cea3fe)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 배송 작업의 디스펜서 단계 구현. 결과 메시지(ACKNOWLEDGED·SUCCESS·FAILED)와 상태 대기열 소거로 완료를 판정하는 조건을 담는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1490",
      "org": "CHART; KABAM-Robotics 보존 저장소",
      "title": "KONE RMF Lift Adapter / kone-ros-api — README (commit 9bc3a87)",
      "published": null,
      "url": "https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "Open-RMF 승강기 메시지와 KONE API v2.0 을 WebSocket 으로 잇는 공개 어댑터 README(원 저장소 안내는 sharp-rmf/kone-ros-api). 실제 승강기 제어 자격증명을 KONE 담당자에게 받도록 안내한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1491",
      "org": "Open-RMF (open-rmf/door_adapter_dormakaba 저장소)",
      "title": "door_adapter_dormakaba — README (commit 2cf76a6)",
      "published": null,
      "url": "https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "Dormakaba 스마트 문용 Open-RMF 문 어댑터 README. EL301·ED250 시험, IoT connector 장착 요구, 문 클라우드 API 자격증명 제공 주체를 적는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1492",
      "org": "HopeTechnik (RMF Systems Engineering Handbook)",
      "title": "Lift and Doors Integration",
      "published": null,
      "url": "https://trl-rmf.github.io/website/content/lift-door-integration.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "한 도서관 현장의 승강기·문 연동 설계와 복구 설명. 승강기 제어함 PLC(Beckhoff CX9020)·드라이 접점 연결, AGV 모드 개조, 화재 경보 시 복구 절차와 메시지 주기를 적는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-202",
      "org": "SEMI",
      "title": "E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface",
      "published": null,
      "url": "https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "SEMI E84 판매 목록. E84-0823 이 현행판(Current)으로 표시되고 AMHS–생산 설비 캐리어 인계 범위를 설명하는 초록을 확인했다. 표준 본문은 미열람.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1494",
      "org": "SEMI Physical Interfaces & Carriers TC (Japan)",
      "title": "SNARF for Doc 7442: Specification for Enhanced Handoff Interface",
      "published": null,
      "url": "https://downloads.semi.org/web/wstdsbal.nsf/18a679096dfd445188256d35007d447d/0db3fe2c9bb0eb2488258d9400027699!OpenDocument",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. E84 를 출발점으로 인계 인터페이스 규격과 TCP/IP 하위 규격을 제안하는 신규 예비 표준 개발 제안서(작성 2025-12-17, 반도체 조립·시험 범위)로, 검증에서 검색 결과 요약으로 내용을 대조했다. 표준 발행은 미확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증. EOR 임계값의 재보정 필요 명시, 배송 지연 관찰, 전체 성공률 분모 설명 부재를 확인했다. ref-060 과 같은 논문이다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-103",
      "org": "Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "다층 호텔 로봇 배송 경로계획 수치 실험. 실제 호텔 평면으로 거리 행렬을 만들고 수요는 무작위 생성했으며 승강기 기본 대기 30초를 둔다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-321",
      "org": "Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982)",
      "title": "Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots",
      "published": "2025-02-28",
      "url": "https://doi.org/10.3390/electronics14050982",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "실내 배송 로봇의 승강기 선택을 최적화한 그래프 기반 다층 경로계획. 15층 건물 그래프 시뮬레이션에서 소포 수 1~7개로 평가했다(초록 기준).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-163",
      "org": "노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57)",
      "title": "탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템",
      "published": "2026-02-28",
      "url": "https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "탐사와 승강기 연계로 다층 실내 지도를 자율 구축한 KAIST 연구. KAIST N1 5~9층 각 층 절반 영역 평가, 승강기 상호작용 19/20 성공, 외부 이용자로 인한 승강기 지연을 보고한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1495",
      "org": "SSPC 135 LSS-WG; Isler, B. 외 (BACnet International)",
      "title": "Physical Access Control with BACnet (BAC-09-08 White Paper)",
      "published": "2008-09-27",
      "url": "https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "BACnet 으로 출입통제를 구현하기 위한 확장을 설명한 백서. 표준 변경 제안의 기초 작업 문서이며 현행 ANSI/ASHRAE 135 규범 본문이 아니다. 인증·권한 검사 구분 내용은 검증에서 재현하지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    },
    {
      "id": "ref-1496",
      "org": "NAVER LABS",
      "title": "NAVER’s ARC Goes to Japan",
      "published": "2026-07-23",
      "url": "https://naverlabs.com/en/blogDetail?seq=10034507",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "NAVER 다중 로봇 플랫폼 ARC 의 Tokyo Midtown Yaesu 도입 소개. 기존 화물 승강기·자동문 연동과 연말 전 층 확대 계획을 공급자 관점에서 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/facility-and-building-system-integration.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "KS B 7317 의 2022-12-09 개정과 2025-05-09 개정은 각각 어떤 조항(요구사항·평가 방법)을 바꿨으며, 그 변경이 승강기 연동 계층이 확인해야 할 항목에 영향을 주는가? (관련 기존 질문: oq-098, oq-173, oq-311)",
      "areas": [
        22,
        50
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 친화형 건축물 인증의 현행 심사 기준은 어느 판이며, 승강기·자동문·출입통제 연동 항목을 어떤 시험이나 서류로 심사하는가? (관련 기존 질문: oq-179)",
      "areas": [
        22,
        64
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "KONE 의 현행 공식 승강기 API 계약(지원 승강기, 건물 등록, 권한 범위, 세션 유지 조건)은 2023년 고정판 공개 RMF 어댑터가 전제한 KONE API v2.0 연결 조건과 어떻게 다른가?",
      "areas": [
        22,
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "SEMI Doc 7442(E84 를 출발점으로 한 새 인계 인터페이스와 TCP/IP 하위 규격) 개발 제안은 승인 뒤 표준으로 발행됐는가, 반도체 밖 이동로봇–설비 인계에도 쓸 수 있는 범위인가? (관련 기존 질문: oq-042, oq-062)",
      "areas": [
        22,
        30
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "HopeTechnik 승강기·문 연동 문서가 승강기 상태 전송 주기를 1 Hz 와 2초마다로 다르게 적은 것은 어느 쪽이 실제 구현·설정이며, 이런 주기 차이가 설비 상태를 믿을 수 있는 경과 시간 판단에 어떤 영향을 주는가? (관련 기존 질문: oq-034)",
      "areas": [
        22,
        18
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "NAVER ARC 의 Tokyo Midtown Yaesu 도입에서 기존 화물 승강기·자동문 연동이 실제로 운영 중인 층·로봇 종류·제조사 범위는 어디까지이며, 공급자 밖의 독립 운영 평가가 있는가?",
      "areas": [
        22,
        64
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "22. 설비·건물 시스템 연동"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "22. 설비·건물 시스템 연동"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "22. 설비·건물 시스템 연동"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "22. 설비·건물 시스템 연동"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "22. 설비·건물 시스템 연동"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/integration/facility-and-building-system-integration.md#5-적용-사례-현장-유형-명시",
      "title": "22. 설비·건물 시스템 연동"
    }
  ],
  "standards_updates": [
    {
      "name": "엘리베이터와 로봇의 상호 연동을 위한 가이드라인 (대한승강기협회 단체표준)",
      "kind": "표준",
      "org": "대한승강기협회(KOLA)",
      "url": "https://kola.or.kr/pages/61/68/bbs/5705",
      "related_areas": [
        22,
        21
      ],
      "summary": "엘리베이터와 로봇 상호 연동의 일반사항·시험 설비·시험 절차를 제시하는 단체표준으로, 협회가 2026-03-27 제정을 발표했다. 표준 번호(B-KOLA-0001-7700)는 검증에서 재현하지 못했고 메시지 정의는 미확인이다.",
      "ref_id": "ref-1485"
    },
    {
      "name": "KONE RMF Lift Adapter (kone-ros-api)",
      "kind": "오픈소스",
      "org": "CHART (KABAM-Robotics 보존 저장소)",
      "url": "https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596",
      "related_areas": [
        22,
        20
      ],
      "summary": "Open-RMF 승강기 메시지와 KONE API v2.0 을 WebSocket 으로 잇는 공개 어댑터(2023년 고정판). 실제 승강기 제어 자격증명은 KONE 담당자에게 받는다.",
      "ref_id": "ref-1490"
    },
    {
      "name": "door_adapter_dormakaba (Open-RMF Dormakaba 문 어댑터)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668",
      "related_areas": [
        22,
        51
      ],
      "summary": "Dormakaba EL301·ED250 문 구동기용 Open-RMF 문 어댑터. IoT connector 장착이 필요하고 문 클라우드 API 자격증명은 Dormakaba 가 제공한다.",
      "ref_id": "ref-1491"
    }
  ],
  "additional_research_requests": [
    "이번 실행 미처리 — 근거 finding 없음, 다음 22. 설비·건물 시스템 연동 실행으로 이월: 트랙 반영 제안 2026-09-25-65(문 설비 연동·IFC HasDrive·로봇 조작과 설비 연동의 선택 조건)와 2026-09-25-76(승강기 층 이름과 지도 층의 대응표). 2026-09-25-65 요약의 'KS B 7317 2021-11-11 제정'은 e-나라표준인증 고시일 2021-11-30 과 달라 페이지에 쓰지 않았다.",
    "6절 물리 인계 예시: OMRON LD 시리즈 통합 안내서(I680-E-02)는 존재를 확인하지 못해 뺐다. 제조사 이동로봇–작업대 인계 절차의 1차 자료를 재확보해야 한다(30. 로봇 간 협업·물리적 인계, oq-042).",
    "7절·11절: KS B 7317 의 2022-12-09·2025-05-09 개정 조항(신구대비표)과 기준값 확인이 필요하다(oq-098·oq-173·oq-311).",
    "7절: 대한승강기협회 가이드라인 원문(메시지·상태·시험 시나리오)과 e-나라표준인증 단체표준 목록의 표준 번호·제정일을 재현 가능한 방식으로 확인해야 한다(oq-041·oq-283).",
    "3절: 국토교통부 로봇 친화형 건축물 핵심기술 개발 보도자료 원문(발행일·사업기간·세부 과제) 확인이 필요하다.",
    "5절: 새로 넣은 기타(도서관)·병원·상업 시설 사례의 시작 조건·작업 대상·완료·인계 칸을 채울 근거가 브리프에 없었다.",
    "참고문헌 정리: ref-060 과 ref-943 은 같은 논문(Lee, Y. 외, Digital Health 2026)이므로 id 통합이 필요하다.",
    "로봇 친화형 건축물 인증의 현행 심사 기준과 평가 부문 명칭(외부 메모 F02 와 기존 용어집 4개 부문 명칭 충돌) 원문 재확보가 필요하다(64. 상업 시설)."
  ],
  "fixes_applied": [
    "f24·f25 삭제 — 6절 물리 인계 예시, 10절 30. 로봇 간 협업·물리적 인계 연결 근거, 11절 oq-042 부분 근거, 13절 각주, reference_updates 어디에도 ref-1493 을 쓰지 않았다.",
    "f47 — 9절 물리 인계 의견 문장의 각주를 ref-202 하나로 달고 [의견]과 '이 위키 구축자의 의견' 표시를 유지했다.",
    "f7 강등 — 7절 대한승강기협회 행에서 표준번호 B-KOLA-0001-7700·등록일자 2026-03-24 를 [추정]으로 쓰고 리서치 단계 열람에만 기대며 검증에서 목록 행을 재현하지 못했다고 밝혔고, 11절 oq-041·oq-283 부분 근거에도 같은 수준으로 적었다.",
    "f36 강등 — 7절 BACnet 행과 9절 출입통제 문단에서 인증·권한 검사 구분을 [추정]으로 쓰고 재현 불가를 밝혔으며, f45 의견은 Dormakaba 자격증명(f20, ref-1491)을 주 근거로 각주를 달고 BACnet 은 추정 근거로만 언급했다.",
    "f35 — 7절 BACnet 행에 2008-09-27 작업 문서이고 현행 ANSI/ASHRAE 135 규범 본문이 아님을 밝혔고 부록 채택 여부 같은 브리프 밖 내용은 넣지 않았다.",
    "f2 — 3절에서 '2025-05-29 착수보고회를 열 예정이라고 2025-05-28 보도됐고'로 고쳤고 사업명은 ref-322 보도자료 제목을 쓰는 기존 문장을 유지했다.",
    "f2·f3·f27 — 13절 ref-322·ref-1494 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 두 출처에 source_unopened: true 를 넣었다.",
    "f27 — '외부 조사 메모가 전한다'를 쓰지 않고 7절 SEMI Doc 7442 행을 지시 문구대로(SEMI 물리 인터페이스·캐리어 기술위원회(일본), SNARF, 작성 2025-12-17, 반도체 조립·시험 범위, 표준 발행 미확인) [추정]으로 썼다.",
    "ref-163 — 각주·reference_updates 발행일을 2026-02-28(로봇학회 논문지 21(1):48–57)로 쓰고 3절 f30 문장 기준일과 8절 f33·f34 항목 기준일을 2026-02-28 로 맞췄다.",
    "f32 — 8절에서 '15층 건물 그래프 시뮬레이션에서 소포 수 1~7개'로 쓰고 시뮬레이션 평가임을 밝혔으며 reference_updates 의 ref-321 요약도 같게 고쳤다.",
    "트랙 반영 제안 2건(2026-09-25-65, 2026-09-25-76) — 6절에 반영하지 않고 changelog_entry 와 additional_research_requests 에 '이번 실행 미처리 — 근거 finding 없음, 다음 22. 설비·건물 시스템 연동 실행으로 이월'을 적었으며 'KS B 7317 2021-11-11 제정'은 페이지에 쓰지 않았다.",
    "직접 인용 — 모든 출처(ref-1492, ref-1487, ref-1488, ref-1489, ref-943 포함)를 직접 인용 없이 재서술했다.",
    "f1 — 8절에서 '로봇 친화형 건축물 인증'을 용어집 robot-friendly-building-certification 으로 연결하고 Robotics-Enabled Environment Certification(REEC)은 병기만 했으며 glossary_updates 에 새 용어를 넣지 않았다.",
    "분량 초과 자동 분리: 22. 설비·건물 시스템 연동 본문 14,192자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 5,569자"
  ]
}
```

### runs/2026-10-11-03/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/integration/facility-and-building-system-integration.md (10개 절)
- 분량 초과 자동 분리:
    - docs/categories/integration/facility-and-building-system-integration.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-11-area22-s6.md (2,450자)
    - docs/categories/integration/facility-and-building-system-integration.md "11. 열린 질문" → docs/topics/2026/2026-10-11-area22-s11.md (1,835자)
    - docs/categories/integration/facility-and-building-system-integration.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-11-area22-s7.md (1,772자)
    - docs/categories/integration/facility-and-building-system-integration.md "3. 왜 중요한가" → docs/topics/2026/2026-10-11-area22-s3.md (1,310자)
    - docs/categories/integration/facility-and-building-system-integration.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-11-area22-s8.md (1,246자)
    - docs/categories/integration/facility-and-building-system-integration.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-11-area22-s10.md (881자)
```

### runs/2026-10-11-03/pages/categories/integration/facility-and-building-system-integration.md

```markdown
---
title: "22. 설비·건물 시스템 연동"
type: area
category: "F. 연동"
area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [승강기 연동, Open-RMF, VDA 5050, 작업대 인계, KS B 7317, 단체표준]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-023, ref-031, ref-047, ref-049, ref-060, ref-103, ref-163, ref-202, ref-283, ref-284, ref-286, ref-312, ref-313, ref-314, ref-315, ref-316, ref-317, ref-318, ref-319, ref-320, ref-321, ref-322, ref-943, ref-1398, ref-1483, ref-1484, ref-1485, ref-1486, ref-1487, ref-1488, ref-1489, ref-1490, ref-1491, ref-1492, ref-1494, ref-1495, ref-1496]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [F. 연동](index.md) › 22. 설비·건물 시스템 연동

# 22. 설비·건물 시스템 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇–관제 인터페이스 표준인 VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 목록에 넣는다. [사실][^ref-031] 그러나 같은 명세는 관제–이동로봇 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. [사실][^ref-031]

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 왜 중요한가](../../topics/2026/2026-10-11-area22-s3.md)에 있다.

## 4. 핵심 개념과 용어

아래 개념은 대부분 [Open-RMF](../../glossary/open-rmf.md)와 [VDA 5050](../../glossary/vda-5050.md)의 공개 문서에서 왔으며, 각각 발행 주체 한 곳의 문서에 기댄다(확인일 2026-09-25).

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area10-s4.md)에 있다.

### 2026-10-11 보강

- **AGV 모드 전환과 세션 수락** — Open-RMF 개발자는 2024-08-21 토론 답변에서, 세션을 안전하게 수행하려면 승강기가 별도 AGV 모드여야 하는 경우 모드 전환을 마칠 때까지 승강기 상태에 세션 식별자(session_id)를 내보내지 말아야 한다고 권고했다. [사실][^ref-1487] 같은 답변은 별도 AGV 모드가 없는 승강기도 있을 수 있다고 설명한다. [사실][^ref-1487] 이 권고는 설계 의도의 설명이며 현장 안전 동작을 재현한 결과가 아니다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 수치는 쓰지 않는다.

**물류 흐름 단계:** 출하 (같은 층간 운반 구조가 입고·적치에도 나타난다)

**시나리오:** 위층 보관 구역의 출하 화물을 승강기로 내려 1층 출하 작업대(컨베이어 입구)에 인계

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 업무 시스템의 출하 지시로 운반 작업이 생기고, 출하 작업대가 화물을 받을 준비가 됐는지가 인계 단계의 진행 조건이 된다. 작업대 앞 구역을 VDA 5050 해제 구역으로 두면 로봇이 진입을 요청하고 관제가 허가·대기·철회·거절로 답한다. [사실][^ref-031] |
| 작업 대상 | 출하용 박스·토트(가상) |
| 수행 자원 | 이동로봇은 운반, 승강기·자동문은 각 설비 제어기가 제어하고, Open-RMF 구조에서는 문·승강기 어댑터가 요청을 걸러 설비 노드에 전달한다. [사실][^ref-283][^ref-284] |
| 제약 | 승강기는 요청한 세션이 점유하며 AGV 모드에서는 정지 시 문이 열려 있다. [사실][^ref-312] KS B 7317 은 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한다. [사실][^ref-314] |
| 완료·인계 | 로봇은 하역 위치에서 인제스터 서비스를 요청하고 확인을 받아야 다음 단계로 넘어간다. [사실][^ref-023] 이 요청–결과 방식과 구역 진입 허가를 조합하면 설비 준비 신호와 로봇 도착을 한 작업 흐름 안에서 맞출 수 있을 것으로 보인다. [추정][^ref-023][^ref-031] |
| 예외·성과 | 승강기가 화재·비상·오프라인 모드로 바뀌거나 문 상태가 오프라인·알 수 없음이면 해당 설비를 쓰는 작업을 멈추거나 다른 경로·사람 확인으로 넘기는 예외로 다뤄야 할 것으로 보인다. [추정][^ref-286][^ref-313] 승강기 세션 대기는 출하뿐 아니라 입고·적치의 층간 운반에서도 처리량과 운반 시간에 영향을 줄 것으로 보인다. [추정][^ref-312][^ref-286][^ref-060][^ref-103] |

이 시나리오에서 이 영역이 맡는 칸은 수행 자원(설비와의 요청 경로), 제약(승강기 점유와 탑승 조건), 완료·인계(작업대의 결과 확인)다. 분류 원문의 질문인 컨베이어 준비와 로봇 도착 맞추기에는 현재 추정 수준의 답만 있다. 두 시점을 함께 최적화한 공개 연구는 이번 조사에서 찾지 못했다.

복구 규칙 자체는 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)에서 다룬다. 흐름 전체의 칸은 [현장 유형 매트릭스](../../site-matrix.md)에 모인다.

**현장 유형:** 기타

**사례:** 도서관에서 기존 승강기를 로봇의 층간 이동에 연동 (도서관 현장 설계 문서)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 연계 대상: 현장에 새로 설치한 승강기 제어함 안의 PLC(Beckhoff CX9020)가 서버의 ADS 명령을 받아 드라이 접점으로 승강기 신호를 조작하고, 승강기 업체가 기존 승강기를 AGV 모드로 개조했다. [추정] 벤더 주장[^ref-1492] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 연계 대상: 화재 경보가 울리면 승강기가 수동 모드로 돌아가고 PLC 는 재시작할 때까지 오류 상태에 머물러, 다시 시작하려면 사람의 개입이 필요하다. [추정] 벤더 주장[^ref-1492] |

이 사례는 한 도서관 현장의 벤더 설계 문서(발행일 미확인, 확인일 2026-10-11)에 기대며, 승강기 자체 제어반이 아니라 새로 단 제어함을 거쳐 신호를 조작하는 방식이다. 같은 문서는 승강기 상태 전송 주기를 개요에서는 1 Hz 로, 서버 절에서는 2초마다로 서로 다르게 적고 승강기 요청은 1초마다 보낸다고 적는다. [추정] 벤더 주장[^ref-1492] 차이를 설명하는 근거가 없어 실제 주기는 결론을 내리지 않는다.

이 사례에서 이 영역이 맡는 칸은 수행 자원(설비 쪽 연결 경로)과 예외·성과(비상 뒤 설비 복귀)다. 한 현장의 설계이므로 다른 건물의 화재 복구 조건으로 일반화하지 않는다.

**현장 유형:** 병원

**사례:** 혼잡한 병원에서 승강기를 함께 쓰며 약품 배송 (고려대 구로병원 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 약품 [사실][^ref-943] |
| 수행 자원 | 미확인 |
| 제약 | 승강기 가동률이 높을수록 배송 시간이 길어졌다. [사실][^ref-943] 논문은 ROC 분석으로 찾은 [승강기 가동률](../../glossary/elevator-operating-rate.md)(EOR) 임계값 59.01% 를 현장 특정값으로 해석해야 하며 다른 병원에 적용하려면 재보정이 필요하다고 명시한다(2026-03-31 발표). [사실][^ref-943] |
| 완료·인계 | 미확인 |
| 예외·성과 | 2026-10-11 재확인에서도 논문에는 전체 성공률 87.03% 의 분모를 설명하는 구절이 없고, 분석 대상 122건에서 실패 14건을 뺀 108건의 비율(약 88.52%)과 보고값이 다르다. [사실][^ref-943] |

병원 쪽 요구와 다른 칸은 [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md)에서 다룬다. 이 사례에서 이 영역이 보는 것은 공유 승강기라는 설비 자원이 로봇 배송에 거는 제약이다. 병원·호텔·그래프·지도 연구의 승강기 결과를 국내 다층 물류센터 처리량으로 옮기는 것은 보류하고, 승강기 가동률·통신 상태·카 내부 점유를 나눠 수집해 현장별 임계값을 새로 검증해야 한다는 것이 이 위키 구축자의 의견이다(oq-010). [의견][^ref-943]

**현장 유형:** 상업 시설

**사례:** 상업 건물(Tokyo Midtown Yaesu)의 기존 화물 승강기·자동문을 로봇 배송에 연결 (NAVER LABS 발표)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | NAVER LABS 는 2026-07-23 블로그에서 다중 로봇 플랫폼 ARC 가 이 건물의 기존 화물 승강기·자동문과 출입 경로를 중앙에서 연결한다고 설명했다. [추정] 벤더 주장[^ref-1496] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

같은 블로그는 연말까지 전 층 로봇 배송으로 넓힐 계획이라고 밝혔으며, 이는 계획이지 운영 결과가 아니다. [추정] 벤더 주장[^ref-1496] 공급자 밖의 독립 운영 평가는 확인하지 못했다. 기존 건물 도입 사례는 연동 설비 목록과 실제 운영 중인 로봇 종류·층 범위를 고객 측 자료로 따로 확인하기 전에는 운영 실증으로 세지 않는 것이 맞다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1496]

## 6. 대표 접근법과 기술

공개 자료에서 확인한 접근법은 어댑터를 거친 요청·상태 감독, 요청–결과 방식의 작업대 인계, 관제의 구역 진입 허가 세 가지다. [사실][^ref-283][^ref-023][^ref-031]

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area22-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 공개 규격은 오픈소스 메시지 정의와 로봇 탑승 안전 표준이 중심이다. [사실][^ref-286][^ref-314] 설비–로봇 연동 자체를 정한 국제 표준은 이번 조사에서 확인하지 못했다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area22-s7.md)에 있다.

## 8. 대표 연구와 자료

승강기를 포함한 다층 이동은 경로계획·병원 배송·지도 구축 연구에서 다뤄지며, 연구마다 실물 실증·수치 실험·시뮬레이션으로 조건이 다르다. [사실][^ref-943][^ref-103][^ref-321][^ref-163] 2026-09-25 에는 원문을 열지 못해 결과 수치를 쓰지 않았고, 2026-10-11 재확인에서 아래 실험 조건과 일부 결과를 확인했다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-10-11-area22-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 시설·설비 제어 | 어댑터를 통한 작업 요청·점유 예약(승강기 세션 등)·상태 확인·완료 확인 [추정][^ref-283][^ref-284] | 연계 대상: 승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어(설비 제조사·설비 제어기) [추정][^ref-283][^ref-284][^ref-031] |
| 로봇 자체 지능·제어 | 로봇이 탑승 조건을 갖췄는지를 실행 조건으로 확인해 작업·경로 제약에 반영하는 것이 적절하다는 구축자 의견 [의견] | 연계 대상: 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법(KS B 7317) [사실][^ref-314] |

승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어는 설비 제조사·설비 제어기 쪽에 남고, ROP 는 어댑터를 통해 작업 요청·점유 예약·상태 확인·완료 확인을 맡는 것으로 보인다. [추정][^ref-283][^ref-284][^ref-031] VDA 5050 3.0.0 은 주변 시스템과의 통신을 관제 최소 기능 목록에 넣지만 주변 설비 인터페이스 자체는 범위에서 제외한다. [사실][^ref-031]

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 위의 어댑터 구조와 VDA 5050 범위 규정에 비추어, 이종 제조사를 연결하는 ROP 라면 설비 쪽 제어를 직접 만들기보다 설비별 어댑터의 요청·상태 형식과 실행 확인을 담당하는 쪽이 원문의 경계와 맞는다는 것이 이 위키 구축자의 의견이다. [의견]

건물 설비의 비상 복귀도 같은 경계로 나뉜다. 5절 기타 현장 사례처럼 화재 경보 뒤 승강기의 수동 모드 복귀와 PLC 재시작에는 사람의 개입이 필요할 수 있으며, 이는 연계 대상인 설비 쪽 조치다. [추정] 벤더 주장[^ref-1492] 그래서 ROP 장애 복구와 건물 설비의 비상 복귀를 따로 시험하고, 화재 뒤 설비 재시작 같은 수동 복귀의 책임자를 정해 두는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1492]

출입통제에서는 문 열기 요청과 통행 권한 승인을 나눠 본다. Dormakaba 문 어댑터 README 는 문 클라우드 API 접근 자격증명을 Dormakaba 가 제공한다고 안내한다. [사실][^ref-1491] BACnet 출입통제 백서가 인증과 권한 검사를 구분한다는 내용은 검증에서 재현하지 못한 추정 근거다. [추정][^ref-1495] 이에 비추어 자동문 연동에서는 문 열기 API 자격증명과 별도로 로봇의 공간별 출입 권한과 비상 우선권을 누가 정하는지 확인해야 한다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1491]

물리 인계에서는 ROP 가 준비·허가·이송·완료의 의미를 현장 PLC·작업대와 합의하고, 물리 인계 완료를 상위 작업 완료에 연결하는 것이 좋다는 것이 이 위키 구축자의 의견이다. SEMI E84 같은 업종 규격은 인계 신호 구조의 참고일 뿐 다른 현장에 대한 적합성을 검증한 근거가 아니다. [의견][^ref-202]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

설비 연동은 로봇 연동, 공용 자원 계획, 안전 제약과 함께 움직인다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area22-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 [열린 질문](../../open-questions.md) 목록에 함께 오른다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 열린 질문](../../topics/2026/2026-10-11-area22-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) — 섹션 3~11 신규 작성(Open-RMF 문·승강기 어댑터와 설비 메시지, 디스펜서·인제스터, VDA 5050 3.0.0 해제·동작 구역, KS B 7317·단체표준·제조사 API, 출하 시나리오), 페이지 상태 표식 추가. 2차 수정: 7절 요약의 '국제 표준 미확인' 태그·각주 분리, 5절 KS B 7317 문장 교체, 3·9절 [의견]에 구축자 의견 명시 (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area10-s7.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 첫 문장의 '국제 표준 미확인'을 태그 없는 조사 한계 서술로 분리 (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area10-s4.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area10-s10.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "10. 다른 연구영역과의 연결" 절을 옮겼다. 2차 수정: 9번 항목 사실·의견 분리, 17번 항목을 Open-RMF 예시 작업대로 한정, 28번 항목 사실·열린 질문 분리 (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area10-s8.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "8. 대표 연구와 자료" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-25)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-11
[^ref-163]: 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026-02-28, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-10-11
[^ref-202]: SEMI, E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface, 미확인, https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface, 접근일 2026-10-11
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-09-25
[^ref-314]: 국가기술표준원(e-나라표준인증·KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2025-05-09, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-10-11
[^ref-321]: Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982), Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots, 2025-02-28, https://doi.org/10.3390/electronics14050982, 접근일 2026-10-11
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-11
[^ref-1487]: cwrx777; mxgrey (Open Robotics Discourse 아카이브), Lift session issues - Robot enter lift while lift is still in human mode (#513), 2024-08-21, https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679, 접근일 2026-10-11
[^ref-1491]: Open-RMF (open-rmf/door_adapter_dormakaba 저장소), door_adapter_dormakaba — README (commit 2cf76a6), 미확인, https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668, 접근일 2026-10-11
[^ref-1492]: HopeTechnik (RMF Systems Engineering Handbook), Lift and Doors Integration, 미확인, https://trl-rmf.github.io/website/content/lift-door-integration.html, 접근일 2026-10-11
[^ref-1495]: SSPC 135 LSS-WG; Isler, B. 외 (BACnet International), Physical Access Control with BACnet (BAC-09-08 White Paper), 2008-09-27, https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf, 접근일 2026-10-11
[^ref-1496]: NAVER LABS, NAVER’s ARC Goes to Japan, 2026-07-23, https://naverlabs.com/en/blogDetail?seq=10034507, 접근일 2026-10-11
```

### docs/categories/integration/facility-and-building-system-integration.md

````markdown
---
title: "22. 설비·건물 시스템 연동"
type: area
category: "F. 연동"
area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 51]
tags: [승강기 연동, Open-RMF, VDA 5050, 해제 구역, 작업대 인계, KS B 7317]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-023, ref-031, ref-047, ref-049, ref-060, ref-103, ref-163, ref-283, ref-284, ref-286, ref-312, ref-313, ref-314, ref-315, ref-316, ref-317, ref-318, ref-319, ref-320, ref-321, ref-322]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 연동](index.md) › 22. 설비·건물 시스템 연동

# 22. 설비·건물 시스템 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

로봇–관제 인터페이스 표준인 VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 목록에 넣는다. [사실][^ref-031] 그러나 같은 명세는 관제–이동로봇 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. [사실][^ref-031] 위 두 사실에 비추어, 로봇 쪽 표준만으로는 설비 쪽 연결 방식이 정해지지 않으므로 이종 제조사 로봇을 연결하는 플랫폼은 설비 연동을 따로 설계해야 한다는 것이 이 위키 구축자의 의견이다. [의견]

설비는 여러 로봇이 나눠 쓰는 자원이기도 하다. 로봇이 층간 운반에 승강기를 쓰면 한 로봇의 세션이 승강기를 점유하는 동안 다른 로봇이 기다려야 하므로, 승강기 대기가 처리량과 운반 시간에 영향을 줄 것으로 보인다. [추정][^ref-312][^ref-286][^ref-060][^ref-103] 다만 물류센터 화물용 승강기에 대한 정량 자료는 아직 확인되지 않았다(열린 질문 oq-010).

국내에서도 제도 정비가 진행 중이다. 국가기술표준원은 2021년 11월 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했으며, 승강기 안전기준 소관 부처인 행정안전부와 협력해 추진했다. [사실][^ref-314][^ref-315] 국토교통부는 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'에 착수한다고 발표했다(발행일 미확인). [추정][^ref-322]

## 4. 핵심 개념과 용어

아래 개념은 대부분 [Open-RMF](../../glossary/open-rmf.md)와 [VDA 5050](../../glossary/vda-5050.md)의 공개 문서에서 왔으며, 각각 발행 주체 한 곳의 문서에 기댄다(확인일 2026-09-25).

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area10-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

다음은 설명을 위한 가상의 시나리오이다. 수치는 쓰지 않는다.

**물류 흐름 단계:** 출하 (같은 층간 운반 구조가 입고·적치에도 나타난다)

**시나리오:** 위층 보관 구역의 출하 화물을 승강기로 내려 1층 출하 작업대(컨베이어 입구)에 인계

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 업무 시스템의 출하 지시로 운반 작업이 생기고, 출하 작업대가 화물을 받을 준비가 됐는지가 인계 단계의 진행 조건이 된다. 작업대 앞 구역을 VDA 5050 해제 구역으로 두면 로봇이 진입을 요청하고 관제가 허가·대기·철회·거절로 답한다. [사실][^ref-031] |
| 작업 대상 | 출하용 박스·토트(가상) |
| 수행 자원 | 이동로봇은 운반, 승강기·자동문은 각 설비 제어기가 제어하고, Open-RMF 구조에서는 문·승강기 어댑터가 요청을 걸러 설비 노드에 전달한다. [사실][^ref-283][^ref-284] |
| 제약 | 승강기는 요청한 세션이 점유하며 AGV 모드에서는 정지 시 문이 열려 있다. [사실][^ref-312] KS B 7317 은 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한다. [사실][^ref-314] |
| 완료·인계 | 로봇은 하역 위치에서 인제스터 서비스를 요청하고 확인을 받아야 다음 단계로 넘어간다. [사실][^ref-023] 이 요청–결과 방식과 구역 진입 허가를 조합하면 설비 준비 신호와 로봇 도착을 한 작업 흐름 안에서 맞출 수 있을 것으로 보인다. [추정][^ref-023][^ref-031] |
| 예외·성과 | 승강기가 화재·비상·오프라인 모드로 바뀌거나 문 상태가 오프라인·알 수 없음이면 해당 설비를 쓰는 작업을 멈추거나 다른 경로·사람 확인으로 넘기는 예외로 다뤄야 할 것으로 보인다. [추정][^ref-286][^ref-313] 승강기 세션 대기는 출하뿐 아니라 입고·적치의 층간 운반에서도 처리량과 운반 시간에 영향을 줄 것으로 보인다. [추정][^ref-312][^ref-286][^ref-060][^ref-103] |

이 시나리오에서 이 영역이 맡는 칸은 수행 자원(설비와의 요청 경로), 제약(승강기 점유와 탑승 조건), 완료·인계(작업대의 결과 확인)다. 분류 원문의 질문인 컨베이어 준비와 로봇 도착 맞추기에는 현재 추정 수준의 답만 있다. 두 시점을 함께 최적화한 공개 연구는 이번 조사에서 찾지 못했다.

복구 규칙 자체는 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)에서 다룬다. 흐름 전체의 칸은 [현장 유형 매트릭스](../../site-matrix.md)에 모인다.

## 6. 대표 접근법과 기술

공개 자료에서 확인한 접근법은 어댑터를 거친 요청·상태 감독, 요청–결과 방식의 작업대 인계, 관제의 구역 진입 허가 세 가지다. [사실][^ref-283][^ref-023][^ref-031]

### 어댑터를 거친 요청·상태 감독

Open-RMF 는 문과 승강기 앞에 어댑터를 두어 요청을 걸러 설비 노드에 전달하고, 승강기 노드는 OPC 같은 프로토콜로 승강기 제어기와 통신한다. [사실][^ref-283][^ref-284] 설비 상태는 문 모드와 승강기 상태 메시지로 되돌아온다. [사실][^ref-313][^ref-286] 한계는 이 구조가 Open-RMF 한 곳의 문서에 기댄다는 점이다.

```mermaid
flowchart LR
  req["요청자: 플릿 어댑터·핵심 시스템"] -->|승강기 요청| la["승강기 어댑터"]
  la -->|적절할 때만 전달| ln["승강기 노드"]
  ln --> lc["승강기 제어기 (연계 대상)"]
  ln -->|승강기 상태| req
  req -->|문 요청| da["문 어댑터"]
  da --> dn["문 노드"]
  dn --> dc["자동문 제어기 (연계 대상)"]
```

위 그림은 Open-RMF 문서 설명을 바탕으로 이 위키가 직접 그린 개념도다.

### 요청–결과 방식의 작업대 인계

배송 작업에서 로봇은 픽업 위치에서 디스펜서 서비스를 요청해 확인을 기다리고, 하역 위치에서 인제스터 서비스를 요청해 확인을 기다린다. [사실][^ref-023] 두 유형은 예시 구현이므로 실제 컨베이어·자동창고에 맞춘 어댑터는 현장마다 따로 필요하다. [추정][^ref-023]

### 관제의 구역 진입 허가

VDA 5050 3.0.0 에서 로봇은 상태 메시지의 zoneRequests 로 해제 구역 진입을 요청하고, 관제는 responses 토픽으로 허가·대기·철회·거절을 답한다. 허가가 철회·만료될 때의 행동은 releaseLossBehavior(정지·계속·대피)로 정한다. [사실][^ref-031] 동작 구역은 구역 진입·통과·이탈 때 미리 정한 action 을 수행하게 하는 장치이며, 명세는 이를 문·승강기 연동 수단으로 규정하지 않는다. [사실][^ref-031]

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 공개 규격은 오픈소스 메시지 정의와 로봇 탑승 안전 표준이 중심이다. [사실][^ref-286][^ref-314] 설비–로봇 연동 자체를 정한 국제 표준은 이번 조사에서 확인하지 못했다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area10-s7.md)에 있다.

## 8. 대표 연구와 자료

승강기를 포함한 다층 이동은 경로계획·병원 배송·지도 구축 연구에서 다뤄지고 있으며, 이번에 확인한 연구는 모두 원문을 열지 못해 결과 수치는 쓰지 않는다. [사실][^ref-060][^ref-103]

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area10-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 시설·설비 제어 | 어댑터를 통한 작업 요청·점유 예약(승강기 세션 등)·상태 확인·완료 확인 [추정][^ref-283][^ref-284] | 연계 대상: 승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어(설비 제조사·설비 제어기) [추정][^ref-283][^ref-284][^ref-031] |
| 로봇 자체 지능·제어 | 로봇이 탑승 조건을 갖췄는지를 실행 조건으로 확인해 작업·경로 제약에 반영하는 것이 적절하다는 구축자 의견 [의견] | 연계 대상: 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법(KS B 7317) [사실][^ref-314] |

승강기·자동문·컨베이어·PLC 의 제어와 설비 안전 제어는 설비 제조사·설비 제어기 쪽에 남고, ROP 는 어댑터를 통해 작업 요청·점유 예약·상태 확인·완료 확인을 맡는 것으로 보인다. [추정][^ref-283][^ref-284][^ref-031] VDA 5050 3.0.0 은 주변 시스템과의 통신을 관제 최소 기능 목록에 넣지만 주변 설비 인터페이스 자체는 범위에서 제외한다. [사실][^ref-031]

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 적는다([범위 경계](../../about/scope-boundary.md)). 위의 어댑터 구조와 VDA 5050 범위 규정에 비추어, 이종 제조사를 연결하는 ROP 라면 설비 쪽 제어를 직접 만들기보다 설비별 어댑터의 요청·상태 형식과 실행 확인을 담당하는 쪽이 원문의 경계와 맞는다는 것이 이 위키 구축자의 의견이다. [의견]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

설비 연동은 로봇 연동, 공용 자원 계획, 안전 제약과 함께 움직인다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area10-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 [열린 질문](../../open-questions.md) 목록에 함께 오른다.

자세한 내용은 주제 페이지 [22. 설비·건물 시스템 연동 — 열린 질문](../../topics/2026/2026-09-25-area10-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) — 섹션 3~11 신규 작성(Open-RMF 문·승강기 어댑터와 설비 메시지, 디스펜서·인제스터, VDA 5050 3.0.0 해제·동작 구역, KS B 7317·단체표준·제조사 API, 출하 시나리오), 페이지 상태 표식 추가. 2차 수정: 7절 요약의 '국제 표준 미확인' 태그·각주 분리, 5절 KS B 7317 문장 교체, 3·9절 [의견]에 구축자 의견 명시 (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area10-s7.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 첫 문장의 '국제 표준 미확인'을 태그 없는 조사 한계 서술로 분리 (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area10-s4.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area10-s10.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "10. 다른 연구영역과의 연결" 절을 옮겼다. 2차 수정: 9번 항목 사실·의견 분리, 17번 항목을 Open-RMF 예시 작업대로 한정, 28번 항목 사실·열린 질문 분리 (실행 2026-09-25-25)
- 2026-09-25 · 생성 · [22. 설비·건물 시스템 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area10-s8.md) — 자동 분리: 10. 설비·건물 시스템 연동 의 "8. 대표 연구와 자료" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-25-25)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-09-25
[^ref-314]: 국가표준인증통합정보시스템(KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2021-11, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-09-25 (원문 미열람)
[^ref-315]: 산업통상자원부 국가기술표준원(대한민국 정책브리핑), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-322]: 국토교통부, 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료), 미확인, https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964, 접근일 2026-09-25 (원문 미열람)
````

### runs/2026-10-11-03/pages/topics/2026/2026-10-11-area22-s6.md

````markdown
---
title: "22. 설비·건물 시스템 연동 — 대표 접근법과 기술"
type: topic
category: "F. 연동"
primary_area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-023, ref-031, ref-1398, ref-1487, ref-1488, ref-1489, ref-1490, ref-1491, ref-1492, ref-163, ref-283, ref-284, ref-286, ref-313, ref-943]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/facility-and-building-system-integration.md#6
---

[홈](../../index.md) › [주제](../index.md) › 22. 설비·건물 시스템 연동 — 대표 접근법과 기술

# 22. 설비·건물 시스템 연동 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 공개 자료에서 확인한 접근법은 어댑터를 거친 요청·상태 감독, 요청–결과 방식의 작업대 인계, 관제의 구역 진입 허가 세 가지다. [사실][^ref-283][^ref-023][^ref-031]
- 이 페이지는 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

공개 자료에서 확인한 접근법은 어댑터를 거친 요청·상태 감독, 요청–결과 방식의 작업대 인계, 관제의 구역 진입 허가 세 가지다. [사실][^ref-283][^ref-023][^ref-031]

### 어댑터를 거친 요청·상태 감독

Open-RMF 는 문과 승강기 앞에 어댑터를 두어 요청을 걸러 설비 노드에 전달하고, 승강기 노드는 OPC 같은 프로토콜로 승강기 제어기와 통신한다. [사실][^ref-283][^ref-284] 설비 상태는 문 모드와 승강기 상태 메시지로 되돌아온다. [사실][^ref-313][^ref-286] 한계는 이 구조가 Open-RMF 한 곳의 문서에 기댄다는 점이다.

```mermaid
flowchart LR
  req["요청자: 플릿 어댑터·핵심 시스템"] -->|승강기 요청| la["승강기 어댑터"]
  la -->|적절할 때만 전달| ln["승강기 노드"]
  ln --> lc["승강기 제어기 (연계 대상)"]
  ln -->|승강기 상태| req
  req -->|문 요청| da["문 어댑터"]
  da --> dn["문 노드"]
  dn --> dc["자동문 제어기 (연계 대상)"]
```

위 그림은 Open-RMF 문서 설명을 바탕으로 이 위키가 직접 그린 개념도다.

### 요청–결과 방식의 작업대 인계

배송 작업에서 로봇은 픽업 위치에서 디스펜서 서비스를 요청해 확인을 기다리고, 하역 위치에서 인제스터 서비스를 요청해 확인을 기다린다. [사실][^ref-023] 두 유형은 예시 구현이므로 실제 컨베이어·자동창고에 맞춘 어댑터는 현장마다 따로 필요하다. [추정][^ref-023]

### 관제의 구역 진입 허가

VDA 5050 3.0.0 에서 로봇은 상태 메시지의 zoneRequests 로 해제 구역 진입을 요청하고, 관제는 responses 토픽으로 허가·대기·철회·거절을 답한다. 허가가 철회·만료될 때의 행동은 releaseLossBehavior(정지·계속·대피)로 정한다. [사실][^ref-031] 동작 구역은 구역 진입·통과·이탈 때 미리 정한 action 을 수행하게 하는 장치이며, 명세는 이를 문·승강기 연동 수단으로 규정하지 않는다. [사실][^ref-031]

2026-10-11 재확인에서는 위 두 접근법(어댑터를 거친 요청·상태 감독, 요청–결과 방식의 작업대 인계)의 구현 세부와 제조사 어댑터·설비 쪽 연결 방식을 보강했다.

### 승강기 세션 감독과 수락 조건

Open-RMF 의 승강기 감독자(lift_supervisor) 구현(rmf_ros2 커밋 4cea3fe, 확인일 2026-10-11)은 승강기마다 활성 세션을 두고, 같은 세션 식별자의 새 요청은 갱신으로 다시 내보내며 세션 종료 요청이 오면 종료를 내보낸 뒤 활성 세션을 비운다. [사실][^ref-1488] 감독자에게 활성 요청이 없는데 승강기 상태에 세션이 남아 있으면 승강기가 풀리도록 세션 종료 요청을 계속 내보내며, 여러 요청 사이의 승강기 배정 규칙은 두지 않고 개선 과제(TODO) 주석만 남겨 두었다. [사실][^ref-1488] 플릿 어댑터 변경기록의 2.13.0(2026-06-15)에는 승강기가 이미 해당 층에 있으면 legacy 완료 상태를 내보내는 변경(#510)이 실려 있고, 같은 변경기록에는 그 뒤 판인 2.14.0(2026-09-26)도 있다. [사실][^ref-1398]

이 분석은 코드 동작과 설계 의도이며 현장 안전 동작의 재현이 아니다. 장치별 세션 수락 조건(AGV 모드 전환을 마친 뒤 session_id 를 보고하는지)을 어댑터 계약에 적고 수락 전 탑승을 막는지 확인하는 시험을 두며, 세션 유실·중복 종료·설비 상태의 세션 잔류 상황을 현장 인수 시험 항목에 넣는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1487][^ref-1488]

### 작업대 결과와 완료 판정

Open-RMF 배송 작업의 디스펜서 단계(DispenseItem) 구현은 요청 식별자가 일치하는 결과 메시지가 SUCCESS 이면 완료, FAILED 이면 실패로 바꾸고, ACKNOWLEDGED 는 접수 표시만 한다. [사실][^ref-1489] 같은 구현은 디스펜서 상태의 요청 대기열에 요청 식별자가 들어 있으면 접수로 보고, 접수 뒤 대기열에서 그 식별자가 사라지면 결과 메시지 없이도 완료로 간주한다. [사실][^ref-1489] 대기열 소거만으로 완료 처리하면 현장 작업대 대기열에서 요청이 취소·오류로 빠진 경우에도 인계 완료로 잘못 판단할 수 있을 것으로 보인다. [추정][^ref-1489] 그래서 실물 인계 성공을 뜻하는 센서·PLC 조건을 작업대 결과 메시지와 따로 정하고, 대기열 소거가 취소·오류를 뜻하는 경우를 구별해야 한다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1489]

### 제조사 어댑터와 설비 자격증명

CHART 계열의 공개 KONE 승강기 어댑터 README(2023년 고정판을 KABAM-Robotics 저장소가 보존, 확인일 2026-10-11)는 Open-RMF 승강기 메시지와 KONE API v2.0 사이에서 WebSocket 으로 승강기 명령을 보내고 승강기 상태를 받는 구조를 설명한다. [사실][^ref-1490] 같은 README 는 실제 승강기를 제어하려면 접근 id 와 비밀값(access_id·access_secret)을 KONE 담당자에게서 받아야 한다고 안내한다. [사실][^ref-1490] 이 어댑터는 공개 구현이며 현행 KONE 계약을 보여 주지 않는다.

연계 대상: Open-RMF 의 Dormakaba 문 어댑터 README 는 시험한 EL301·ED250 문 구동기에 Dormakaba IoT connector 를 장착해야 하고, 문 클라우드 API 접근 자격증명은 Dormakaba 가 제공한다고 안내한다. [사실][^ref-1491] 제조사 어댑터를 검토할 때는 공개 어댑터의 판과 별도로 현행 API 판·권한 범위·건물 등록·세션 유지 조건을 확인하는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1490]

### 설비 쪽 연결 방식의 구분

제조사 API 대신 기존 승강기에 제어함과 PLC 를 새로 달아 드라이 접점으로 신호를 조작하는 방식도 한 도서관 현장 문서에 나온다(5절 기타 현장 사례). [추정] 벤더 주장[^ref-1492] 설비 API 연동과 로봇팔 버튼 조작을 서로 다른 승강기 연결 방식으로 기록하고, 공유 승강기 지연 시험을 따로 두는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-163][^ref-943]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/facility-and-building-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1398]: Open-RMF (open-rmf/rmf_ros2 저장소), Changelog for package rmf_fleet_adapter, 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-11
[^ref-1487]: cwrx777; mxgrey (Open Robotics Discourse 아카이브), Lift session issues - Robot enter lift while lift is still in human mode (#513), 2024-08-21, https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679, 접근일 2026-10-11
[^ref-1488]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter/src/lift_supervisor/Node.cpp (commit 4cea3fe), 미확인, https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/lift_supervisor/Node.cpp, 접근일 2026-10-11
[^ref-1489]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp (commit 4cea3fe), 미확인, https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp, 접근일 2026-10-11
[^ref-1490]: CHART; KABAM-Robotics 보존 저장소, KONE RMF Lift Adapter / kone-ros-api — README (commit 9bc3a87), 미확인, https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596, 접근일 2026-10-11
[^ref-1491]: Open-RMF (open-rmf/door_adapter_dormakaba 저장소), door_adapter_dormakaba — README (commit 2cf76a6), 미확인, https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668, 접근일 2026-10-11
[^ref-1492]: HopeTechnik (RMF Systems Engineering Handbook), Lift and Doors Integration, 미확인, https://trl-rmf.github.io/website/content/lift-door-integration.html, 접근일 2026-10-11
[^ref-163]: 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026-02-28, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-10-11
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-09-25
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-03 | 22. 설비·건물 시스템 연동 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-10-11-03/pages/topics/2026/2026-10-11-area22-s11.md

```markdown
---
title: "22. 설비·건물 시스템 연동 — 열린 질문"
type: topic
category: "F. 연동"
primary_area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: []
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/facility-and-building-system-integration.md#11
---

[홈](../../index.md) › [주제](../index.md) › 22. 설비·건물 시스템 연동 — 열린 질문

# 22. 설비·건물 시스템 연동 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 질문은 [열린 질문](../../open-questions.md) 목록에 함께 오른다.
- 이 페이지는 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 질문은 [열린 질문](../../open-questions.md) 목록에 함께 오른다.


### 2026-10-11 재확인에서 얻은 부분 근거

아래 질문은 이번 재확인에서 근거가 일부 보강됐으나 모두 열림 상태를 유지한다.

- **oq-010** (상태: 열림) 병원 논문의 재보정 명시, 공유 승강기 지연의 교차 확인, 호텔·그래프 연구의 수치 실험 성격, 지도 구축 연구의 로봇 한 대 실물 실험이라는 조건을 확인했으나 물류센터 실측 자료는 여전히 없다(8절).
- **oq-041**·**oq-283** (상태: 열림) 대한승강기협회 가이드라인의 대상 범위(일반사항·시험 설비·시험 절차)와 무료 공개를 확인했고, 표준 번호는 리서치 단계 열람에만 기댄다(7절). 메시지·상태 정의, Open-RMF 대응, 연동 장애 시 책임 분담은 미확인이다.
- **oq-042**·**oq-062** (상태: 열림) SEMI E84 현행판과 Doc 7442 개발 제안을 확인했으나 반도체 범위이며, 이동로봇–컨베이어·작업대 인계용 제조사 중립 규격은 확인하지 못했다.
- **oq-043** (상태: 열림) 문 클라우드 자격증명의 제공 주체와 BACnet 출입통제 백서의 지위를 확인했으나, 로봇 관제가 보안문을 여닫는 사례와 권한 확인 주체는 미확인이다.
- **oq-098**·**oq-173**·**oq-311** (상태: 열림) KS B 7317 의 개정 이력과 적용 범위를 확인했으나 조항과 기준값은 미확인이다.
- **oq-067**·**oq-094** (상태: 열림) Open-RMF 승강기 감독자에 여러 요청 사이의 배정 규칙이 구현돼 있지 않음을 확인했다(6절).
- **oq-215** (상태: 열림) 병원 논문의 전체 성공률 87.03% 분모 설명이 없음을 다시 확인했다(5절 병원 사례).
- **oq-258**·**oq-328** (상태: 열림) 병원 논문이 승강기 가동률 임계값의 재보정 필요를 명시함을 확인했다.

### 새로 올린 질문

- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-03) KS B 7317 의 2022-12-09 개정과 2025-05-09 개정은 각각 어떤 조항(요구사항·평가 방법)을 바꿨으며, 그 변경이 승강기 연동 계층이 확인해야 할 항목에 영향을 주는가?
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-03) 로봇 친화형 건축물 인증의 현행 심사 기준은 어느 판이며, 승강기·자동문·출입통제 연동 항목을 어떤 시험이나 서류로 심사하는가?
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-03) KONE 의 현행 공식 승강기 API 계약(지원 승강기, 건물 등록, 권한 범위, 세션 유지 조건)은 2023년 고정판 공개 RMF 어댑터가 전제한 KONE API v2.0 연결 조건과 어떻게 다른가?
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-03) SEMI Doc 7442 개발 제안은 승인 뒤 표준으로 발행됐는가, 반도체 밖 이동로봇–설비 인계에도 쓸 수 있는 범위인가?
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-03) 도서관 현장 승강기·문 연동 문서가 승강기 상태 전송 주기를 1 Hz 와 2초마다로 다르게 적은 것은 어느 쪽이 실제 구현·설정이며, 이런 주기 차이가 설비 상태를 믿을 수 있는 경과 시간 판단에 어떤 영향을 주는가?
- (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-03) NAVER ARC 의 Tokyo Midtown Yaesu 도입에서 기존 화물 승강기·자동문 연동이 실제로 운영 중인 층·로봇 종류·제조사 범위는 어디까지이며, 공급자 밖의 독립 운영 평가가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/facility-and-building-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-03 | 22. 설비·건물 시스템 연동 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-11-03/pages/topics/2026/2026-10-11-area22-s7.md

```markdown
---
title: "22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 연동"
primary_area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1485, ref-1486, ref-1494, ref-1495, ref-202, ref-286, ref-314]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/facility-and-building-system-integration.md#7
---

[홈](../../index.md) › [주제](../index.md) › 22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스

# 22. 설비·건물 시스템 연동 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역과 관련된 공개 규격은 오픈소스 메시지 정의와 로봇 탑승 안전 표준이 중심이다. [사실][^ref-286][^ref-314] 설비–로봇 연동 자체를 정한 국제 표준은 이번 조사에서 확인하지 못했다.
- 이 페이지는 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역과 관련된 공개 규격은 오픈소스 메시지 정의와 로봇 탑승 안전 표준이 중심이다. [사실][^ref-286][^ref-314] 설비–로봇 연동 자체를 정한 국제 표준은 이번 조사에서 확인하지 못했다.


### 2026-10-11 보강

이번 재확인에서 국내 표준·단체표준의 판 정보와 인계 신호·출입통제 관련 문서의 지위를 보강했다. [사실][^ref-314][^ref-1485][^ref-202][^ref-1495]

| 이름 | 유형 | 이 영역과의 관계 |
|---|---|---|
| KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 표준 | e-나라표준인증 이력상 2021-11-30 제정(고시 2021-0561), 2022-12-09 개정(고시 2022-0571), 2025-05-09 개정(고시 2025-0073)이다. 적용 대상은 엘리베이터 탑승 기능이 있는 서비스 로봇과 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터이고, 표준개발협력기관은 한국AI·로봇산업협회다. [사실][^ref-314] 개정 조항은 미확인이며, 로봇 탑승 안전 요구이므로 이 영역에서는 제약 조건과 판 정보로만 다룬다. |
| 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 (대한승강기협회 단체표준) | 표준 | 대한승강기협회는 2026-03-27 게시한 보도자료에서 이 단체표준을 제정했다고 발표했고, 일반사항·시험 설비·시험 절차를 제시하며 e-나라표준인증에서 무료로 내려받을 수 있다고 설명했다. [사실][^ref-1485] 리서치 단계 열람에서는 e-나라표준인증 단체표준 목록에 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 로 올라 있었으나, 검증 단계에서는 이 목록 행을 재현하지 못했다. [추정][^ref-1486] 등록일자와 협회 게시일이 다르고, 정확한 제정일·메시지·상태 정의·Open-RMF 대응은 미확인이다. |
| SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface | 표준 | SEMI 공식 판매 목록은 E84-0823 을 현행판으로 표시하고, 목적을 자동 반송 시스템(AMHS)과 생산 설비 로드포트 사이 캐리어 인계용 병렬 I/O 신호 개선으로 설명한다(확인일 2026-10-11). [사실][^ref-202] 반도체 업종 규격이므로 이 영역에서는 인계 신호 구조의 참고로만 쓴다. |
| SEMI Doc 7442 Specification for Enhanced Handoff Interface (개발 제안) | 표준 | SEMI 물리 인터페이스·캐리어 기술위원회(일본)의 Doc 7442 신규 예비 표준 개발 제안서(SNARF, 작성 2025-12-17)는 E84 를 출발점으로 인계 인터페이스 규격과 TCP/IP 하위 규격을 제안하며, 대상은 반도체 조립·시험 범위다. 표준으로 발행됐는지는 미확인이다. [추정][^ref-1494] |
| Physical Access Control with BACnet (BAC-09-08 백서) | 프레임워크 | 2008-09-27 백서로, SSPC 135 LSS 작업반의 진행 중 작업이자 BACnet 표준 변경 제안의 기초 문서라고 스스로 밝히며 현행 ANSI/ASHRAE 135 규범 본문이 아니다. [사실][^ref-1495] 같은 백서가 인증과 권한 검사를 구분하고 특정 시간에 특정 문을 통과할 권리를 기본 권한 검사의 예로 든다는 내용은 검증에서 본문으로 재현하지 못했다. [추정][^ref-1495] |

승강기 탑승 안전 표준을 검토할 때는 판(제정·개정 일자)·적용 범위·대상 승강기 유형을 함께 기록하는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-314] 대한승강기협회 가이드라인과 Open-RMF 승강기 메시지의 대응표는 표준 원문의 메시지·시험 시나리오를 확보한 뒤에 작성하는 것이 맞다는 것도 구축자의 의견이다. [의견][^ref-1485]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/facility-and-building-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1485]: 대한승강기협회(KOLA), 대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27), 2026-03-27, https://kola.or.kr/pages/61/68/bbs/5705, 접근일 2026-10-11
[^ref-1486]: 국가기술표준원(e-나라표준인증), 단체표준 목록 — B-KOLA-0001-7700 엘리베이터와 로봇의 상호 연동을 위한 가이드라인, 미확인, https://www.standard.go.kr/KSCI/grpstd/getGrpStdCrtfcReqst.do?menuId=60372&topMenuId=502&upperMenuId=503, 접근일 2026-10-11
[^ref-1494]: SEMI Physical Interfaces & Carriers TC (Japan), SNARF for Doc 7442: Specification for Enhanced Handoff Interface, 미확인, https://downloads.semi.org/web/wstdsbal.nsf/18a679096dfd445188256d35007d447d/0db3fe2c9bb0eb2488258d9400027699!OpenDocument, 접근일 2026-10-11 (원문 미열람)
[^ref-1495]: SSPC 135 LSS-WG; Isler, B. 외 (BACnet International), Physical Access Control with BACnet (BAC-09-08 White Paper), 2008-09-27, https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf, 접근일 2026-10-11
[^ref-202]: SEMI, E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface, 미확인, https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface, 접근일 2026-10-11
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-314]: 국가기술표준원(e-나라표준인증·KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2025-05-09, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-03 | 22. 설비·건물 시스템 연동 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-11-03/pages/topics/2026/2026-10-11-area22-s3.md

```markdown
---
title: "22. 설비·건물 시스템 연동 — 왜 중요한가"
type: topic
category: "F. 연동"
primary_area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-060, ref-103, ref-1483, ref-1484, ref-163, ref-286, ref-312, ref-314, ref-315, ref-322, ref-943]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/facility-and-building-system-integration.md#3
---

[홈](../../index.md) › [주제](../index.md) › 22. 설비·건물 시스템 연동 — 왜 중요한가

# 22. 설비·건물 시스템 연동 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇–관제 인터페이스 표준인 VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 목록에 넣는다. [사실][^ref-031] 그러나 같은 명세는 관제–이동로봇 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. [사실][^ref-031]
- 이 페이지는 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇–관제 인터페이스 표준인 VDA 5050 3.0.0 은 문·게이트·승강기 같은 주변 시스템과의 통신을 관제(fleet control) 시스템의 최소 기능 목록에 넣는다. [사실][^ref-031] 그러나 같은 명세는 관제–이동로봇 통신과 무관한 인터페이스, 곧 주변 설비·인프라 구성요소·외부 IT 시스템과의 인터페이스를 범위에서 제외한다. [사실][^ref-031] 위 두 사실에 비추어, 로봇 쪽 표준만으로는 설비 쪽 연결 방식이 정해지지 않으므로 이종 제조사 로봇을 연결하는 플랫폼은 설비 연동을 따로 설계해야 한다는 것이 이 위키 구축자의 의견이다. [의견]

설비는 여러 로봇이 나눠 쓰는 자원이기도 하다. 로봇이 층간 운반에 승강기를 쓰면 한 로봇의 세션이 승강기를 점유하는 동안 다른 로봇이 기다려야 하므로, 승강기 대기가 처리량과 운반 시간에 영향을 줄 것으로 보인다. [추정][^ref-312][^ref-286][^ref-060][^ref-103] 실제로 사람과 승강기를 함께 쓰는 건물에서 로봇의 층간 이동이 늦어진 사례가 기관이 다른 두 연구에서 보고됐다(2026-03-31·2026-02-28 발표). 병원 연구는 승강기 가동률이 높을수록 배송 시간이 길어졌다고, 대학 건물 지도 구축 연구는 외부 이용자 때문에 승강기가 다른 층으로 가 지연이 생겼다고 적는다. [사실][^ref-943][^ref-163] 다만 물류센터 화물용 승강기에 대한 정량 자료는 아직 확인되지 않았다(열린 질문 oq-010).

국내에서도 제도 정비가 진행 중이다. 국가기술표준원은 2021년 11월 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했으며, 승강기 안전기준 소관 부처인 행정안전부와 협력해 추진했다. [사실][^ref-314][^ref-315] e-나라표준인증 이력에 따르면 이 표준은 2021-11-30 제정 뒤 2022-12-09 과 2025-05-09 두 차례 개정됐고, 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터를 적용 대상으로 둔다. [사실][^ref-314] 개정된 조항은 미확인이다.

국토교통부는 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'에 착수한다고 발표했다(발행일 미확인). [추정][^ref-322] 2차 보도에 따르면 이 연구개발은 2025-05-29 착수보고회를 열 예정이라고 2025-05-28 보도됐고, 2028년까지 완료될 예정이며, 세부 중점과제에 기술 실증을 통한 기술표준·인증제도 개선방안 마련이 들어 있다. [추정][^ref-1484][^ref-322] 국토부 보도자료 원문은 열지 못해 사업기간과 과제 내용은 2차 보도 기준이며, 이후 진행은 미확인이다.

건축물 인증과 국가 연구개발 계획은 인증 운영기관의 현행 심사 규칙이 아니므로, ROP 의 설비 연동 수용 기준은 이들과 별도 목록으로 관리하고 발주 때 인증의 적용 판·심사 범위와 현장 설비 연결 계약을 서로 다른 증빙으로 확인하는 것이 좋다는 것이 이 위키 구축자의 의견이다. [의견][^ref-1483][^ref-1484]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/facility-and-building-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-11
[^ref-1483]: Park, Y.; Park, S. (Architectural Research), Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems, 2026-07-21, https://link.springer.com/article/10.1007/s44515-026-00016-y, 접근일 2026-10-11
[^ref-1484]: 스마트투데이(이재수), "사람과 로봇이 공존하는 스마트 빌딩 앞당긴다"...국토부 산학협력단과 기술개발 착수, 2025-05-28, https://www.smarttoday.co.kr/ko-kr/articles/81933, 접근일 2026-10-11
[^ref-163]: 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026-02-28, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-10-11
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-314]: 국가기술표준원(e-나라표준인증·KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2025-05-09, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-10-11
[^ref-315]: 산업통상자원부 국가기술표준원(대한민국 정책브리핑), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-322]: 국토교통부, 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료), 미확인, https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964, 접근일 2026-10-11 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-03 | 22. 설비·건물 시스템 연동 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-11-03/pages/topics/2026/2026-10-11-area22-s8.md

```markdown
---
title: "22. 설비·건물 시스템 연동 — 대표 연구와 자료"
type: topic
category: "F. 연동"
primary_area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-103, ref-1483, ref-163, ref-321, ref-943]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/facility-and-building-system-integration.md#8
---

[홈](../../index.md) › [주제](../index.md) › 22. 설비·건물 시스템 연동 — 대표 연구와 자료

# 22. 설비·건물 시스템 연동 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 승강기를 포함한 다층 이동은 경로계획·병원 배송·지도 구축 연구에서 다뤄지며, 연구마다 실물 실증·수치 실험·시뮬레이션으로 조건이 다르다. [사실][^ref-943][^ref-103][^ref-321][^ref-163] 2026-09-25 에는 원문을 열지 못해 결과 수치를 쓰지 않았고, 2026-10-11 재확인에서 아래 실험 조건과 일부 결과를 확인했다.
- 이 페이지는 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

승강기를 포함한 다층 이동은 경로계획·병원 배송·지도 구축 연구에서 다뤄지며, 연구마다 실물 실증·수치 실험·시뮬레이션으로 조건이 다르다. [사실][^ref-943][^ref-103][^ref-321][^ref-163] 2026-09-25 에는 원문을 열지 못해 결과 수치를 쓰지 않았고, 2026-10-11 재확인에서 아래 실험 조건과 일부 결과를 확인했다.


- Lee, Y. 외(고려대학교 구로병원·도구공간), Digital Health(2026-03-31) — 혼잡한 병원에서 승강기 이용을 고려한 약품 배송 로봇 실증이다. 승강기 가동률 임계값 59.01% 는 현장 특정값이며 다른 병원에 적용할 때 재보정이 필요하다고 명시한다. [사실][^ref-943]
- Han, L. 외, Sensors 25(6):1783(2025-03-13) — 실제 호텔 평면·층고로 68×68 거리 행렬만 만들고 배송 수요는 무작위 표본으로 생성했으며 승강기 기본 대기 시간을 30초로 두었다. 실제 호텔 운용 성능이 아니라 수치 실험이다. [사실][^ref-103]
- Kim, S. 외, Electronics 14(5):982(2025-02-28) — 15층 건물 그래프 시뮬레이션에서 소포 수 1~7개로 승강기 선택을 최적화한 다층 경로계획을 평가했다. 실제 건물 운용이 아닌 시뮬레이션 평가다. [사실][^ref-321]
- 노주형 외, 로봇학회 논문지 21(1):48–57(2026-02-28) — KAIST N1 건물 5~9층에서 각 층의 절반 영역을 대상으로 다층 지도 구축을 평가했고, 승강기 상호작용 시험에서는 20회 중 19회 성공을 보고했다. [사실][^ref-163]
- 두 실물 연구의 공통 관찰 — 사람과 승강기를 함께 쓰는 건물에서 병원 논문은 승강기 가동률이 높을수록 배송 시간이 길어졌다고, KAIST 논문은 외부 이용자 때문에 승강기가 다른 층으로 가 지연이 생겼다고 보고했다. 기관이 다른 두 출처의 질적 관찰이다. [사실][^ref-943][^ref-163]
- Park, Y.·Park, S., Architectural Research 28(1), 논문번호 14(2026-07-21) — 초록 기준으로 [로봇 친화형 건축물 인증](../../glossary/robot-friendly-building-certification.md)(초록 표기 Robotics-Enabled Environment Certification, REEC)과 무장애(BF) 인증을 비교 분석해 사람 중심·로봇 적응형 건축 설계 기준을 도출했다. 본문은 열지 못해 연구 방법은 단정하지 않는다. [사실][^ref-1483]

이 연구들의 승강기 결과를 국내 다층 물류센터 처리량으로 옮기는 것은 보류하고, 현장별 임계값을 새로 검증해야 한다는 것이 이 위키 구축자의 의견이다(oq-010). [의견][^ref-943][^ref-103][^ref-321][^ref-163]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/facility-and-building-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-103]: Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-10-11
[^ref-1483]: Park, Y.; Park, S. (Architectural Research), Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems, 2026-07-21, https://link.springer.com/article/10.1007/s44515-026-00016-y, 접근일 2026-10-11
[^ref-163]: 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 2026-02-28, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667, 접근일 2026-10-11
[^ref-321]: Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982), Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots, 2025-02-28, https://doi.org/10.3390/electronics14050982, 접근일 2026-10-11
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-03 | 22. 설비·건물 시스템 연동 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-11-03/pages/topics/2026/2026-10-11-area22-s10.md

```markdown
---
title: "22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결"
type: topic
category: "F. 연동"
primary_area_no: 22
related_areas: [15, 20, 21, 27, 28, 29, 30, 32, 35, 48, 50, 51, 63, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1483, ref-1489, ref-1490, ref-1491, ref-1492, ref-1496, ref-202, ref-314, ref-943]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/facility-and-building-system-integration.md#10
---

[홈](../../index.md) › [주제](../index.md) › 22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결

# 22. 설비·건물 시스템 연동 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 설비 연동은 로봇 연동, 공용 자원 계획, 안전 제약과 함께 움직인다.
- 이 페이지는 [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

설비 연동은 로봇 연동, 공용 자원 계획, 안전 제약과 함께 움직인다.


### 2026-10-11 보강

- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 약품 배송 논문은 승강기 가동률 임계값을 현장 특정값으로 보고 다른 병원에서는 재보정이 필요하다고 명시한다. [사실][^ref-943]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 상업 건물의 기존 화물 승강기·자동문을 다중 로봇 플랫폼에 중앙 연결했다는 공급자 발표가 있다. [추정] 벤더 주장[^ref-1496] 로봇 친화형 건축물 인증과 무장애 인증을 비교한 설계 기준 연구도 건물 쪽 요구의 배경이 된다. [사실][^ref-1483]
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 도서관 현장의 승강기 제어함 PLC·드라이 접점 연결과 화재 뒤 수동 복구 사례(5절)다. [추정] 벤더 주장[^ref-1492]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 자동문 어댑터의 클라우드 자격증명은 문 제조사가 제공하며, 로봇의 공간별 통행 권한 승인은 그와 별개로 정해야 한다. [사실][^ref-1491]
- [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md) — Open-RMF 디스펜서 단계의 완료 판정(SUCCESS 또는 대기열 소거)과 반도체 업종의 인계 신호 규격(SEMI E84)이 물리 인계 설계의 참고가 된다. [사실][^ref-1489][^ref-202]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 화재 경보 뒤 설비 재시작에 사람의 개입이 필요하다는 현장 문서가 있어, 설비 비상 복귀를 ROP 복구 절차와 따로 다뤄야 한다. [추정] 벤더 주장[^ref-1492]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — KS B 7317 은 2021-11-30 제정 뒤 2022-12-09·2025-05-09 에 개정됐고 병원 환자 전용 엘리베이터를 적용 대상에서 뺀다. [사실][^ref-314]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 승강기 제조사 API(KONE API v2.0)를 Open-RMF 승강기 메시지에 잇는 공개 어댑터가 있다. [사실][^ref-1490]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/facility-and-building-system-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [30. 로봇 간 협업·물리적 인계](../../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/facility-and-building-system-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1483]: Park, Y.; Park, S. (Architectural Research), Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems, 2026-07-21, https://link.springer.com/article/10.1007/s44515-026-00016-y, 접근일 2026-10-11
[^ref-1489]: Open-RMF (open-rmf/rmf_ros2 저장소), rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp (commit 4cea3fe), 미확인, https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp, 접근일 2026-10-11
[^ref-1490]: CHART; KABAM-Robotics 보존 저장소, KONE RMF Lift Adapter / kone-ros-api — README (commit 9bc3a87), 미확인, https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596, 접근일 2026-10-11
[^ref-1491]: Open-RMF (open-rmf/door_adapter_dormakaba 저장소), door_adapter_dormakaba — README (commit 2cf76a6), 미확인, https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668, 접근일 2026-10-11
[^ref-1492]: HopeTechnik (RMF Systems Engineering Handbook), Lift and Doors Integration, 미확인, https://trl-rmf.github.io/website/content/lift-door-integration.html, 접근일 2026-10-11
[^ref-1496]: NAVER LABS, NAVER’s ARC Goes to Japan, 2026-07-23, https://naverlabs.com/en/blogDetail?seq=10034507, 접근일 2026-10-11
[^ref-202]: SEMI, E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface, 미확인, https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface, 접근일 2026-10-11
[^ref-314]: 국가기술표준원(e-나라표준인증·KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2025-05-09, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-10-11
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-03 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-03 | 22. 설비·건물 시스템 연동 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 21건 / 전체 1430건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg | 2026-09-25 | 예 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 2026-09-25 | 예 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | https://doi.org/10.1177/20552076261437181 | 2026-09-25 | 아니오 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 2026-09-25 | 아니오 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 2026-09-25 | 아니오 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 2026-09-25 | 예 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 2026-09-25 | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 2026-09-25 | 예 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 2026-09-25 | 예 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 2026-09-25 | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 2026-09-25 | 아니오 |
| ref-315 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 2026-09-25 | 아니오 |
| ref-316 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 미확인 | https://www.ctman.kr/35296 | 2026-09-25 | 아니오 |
| ref-317 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 미확인 | https://www.electimes.com/news/articleView.html?idxno=320147 | 2026-09-25 | 아니오 |
| ref-318 | KONE | KONE Service Robot API | 미확인 | https://dev.kone.com/api-portal/service-robot-api/ | 2026-09-25 | 아니오 |
| ref-319 | 한국경제 | 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 | 2022-03 | https://www.hankyung.com/economy/article/202203314153Y | 2026-09-25 | 아니오 |
| ref-320 | 파이낸셜뉴스 | 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" | 2023-02 | https://www.fnnews.com/news/202302140913318867 | 2026-09-25 | 아니오 |
| ref-321 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | https://doi.org/10.3390/electronics14050982 | 2026-09-25 | 아니오 |
| ref-322 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 미확인 | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 | 2026-09-25 | 아니오 |
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

### docs/open-questions.md (요약: 대상 영역 [22] 에 걸린 25건 / 전체 371건)

```markdown
- oq-010 [열림] 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? (영역 22, 35)
- oq-034 [열림] 문·승강기·충전기 같은 설비 상태 정보를 몇 초까지 믿고 통과·배정을 확정할지 정한 표준이나 국내 현장 기준이 있는가, 없으면 대상별 허용 경과 시간을 어떤 근거로 정할 것인가? (영역 18, 22)
- oq-041 [열림] 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (영역 21, 22)
- oq-042 [열림] 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? (영역 22, 30)
- oq-043 [열림] 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (영역 22, 51)
- oq-045 [열림] 로봇 지도의 층(level) 이름과 승강기 상태의 층 이름(Open-RMF available_floors 등)을 서로 대응시키는 규칙을 정한 표준이나 공개 구현이 있는가? (영역 15, 22)
- oq-056 [열림] 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 어떤 단위로 나눠 설비 명령 권한을 제한하는지 공개한 구성이나 사례가 있는가? (영역 22, 51)
- oq-062 [열림] 반도체 업종의 SEMI E84 같은 단계별 인계 신호를 물류센터의 이동로봇–컨베이어·작업대 인계에 적용하거나 옮긴 사례가 있는가? (영역 22, 30)
- oq-067 [열림] 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? (영역 22, 28)
- oq-094 [열림] Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가? (영역 22, 34, 54, 55)
- oq-098 [열림] KS B 7317 이 정한 이동 로봇의 승강기 탑승 단차·틈새 기준값은 무엇이며, 국내 물류센터의 화물용 승강기와 이종 제조사 로봇에 그대로 적용되는가? (영역 15, 22)
- oq-173 [열림] 국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가? (영역 63, 22, 59)
- oq-176 [열림] 호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? (영역 64, 20, 22)
- oq-179 [열림] 로봇 친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가? (영역 64, 22)
- oq-182 [열림] 이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가? (영역 65, 22, 21)
- oq-191 [열림] 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? (영역 67, 22, 21)
- oq-199 [열림] 국내 공공건축 BIM 적용 확대로 만들어지는 IFC 모델을 준공 뒤 유지관리 단계에서 로봇 운영 지도로 넘겨받는 절차나 요구 수준(공간·문·승강기 정보)이 정해져 있는가? (영역 14, 22)
- oq-258 [열림] 한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가? (영역 36, 63, 22)
- oq-283 [열림] 로봇-승강기 연동 표준 과제의 결과물(표준 번호, 연동 장애 시 승강기 제조사·로봇 제조사·관제 사업자의 책임 분담)이 공개되었는가? (영역 58, 22)
- oq-311 [열림] ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가? (영역 50, 22)
- oq-322 [열림] 로봇이 직접 관측한 승강기·문 상태와 설비 제어기가 보고한 상태가 다를 때 어느 쪽을 기준으로 통과·탑승을 확정하는지 정한 표준이나 현장 사례가 있는가? (영역 18, 22)
- oq-325 [열림] 병원·호텔·쇼핑몰·공동주택에서 로봇의 승강기 연동이 승강기 제조사 API, 승강기 관리 솔루션, 로봇팔 버튼 조작, 제어반 전용 통신 모듈로 갈리는데, 이 방식들을 한 현장에서 같은 승강기 인터페이스로 묶어 제조사가 다른 로봇이 함께 쓰게 한 사례나 방식별 비교 자료가 있는가(관련 기존 질문 oq-176 은 오케스트레이션 계층, oq-182 는 공동주택 연동 절차, oq-191 은 싱가포르 표준을 묻고, 이 질문은 승강기 연동 방식 간 비교를 묻는다)? (영역 22, 63, 64, 65)
- oq-328 [열림] 병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가? (영역 19, 26, 22)
- oq-331 [열림] OpenSCENARIO 2 DSL 로 다중 로봇 플릿의 작업 배정과 승강기·문 같은 설비 사건을 기술할 수 있는가, 기술하려면 어떤 확장 라이브러리가 필요한가? (영역 33, 22)
- oq-364 [열림] 승강기 운행 시간 민감도와 실제 승강기 대기열·최대 점유 시간의 관계를 같은 실험에서 측정한 자료가 있는가? (영역 28, 22)
```
