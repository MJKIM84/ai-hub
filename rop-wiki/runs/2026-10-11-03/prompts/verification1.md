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

### data/area_reflection_proposals.json (대상 영역 22. 설비·건물 시스템 연동 에 대한 트랙 반영 제안 2건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-65",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 3,
      "area_no": 22,
      "section": "6. 대표 접근법과 기술",
      "summary": "문·승강기 통과를 설비 연동(Open-RMF 문 어댑터 DoorRequest·DoorState, IFC 자동 구동 문 HasDrive)으로 충족하는 방식(f6·f8), 로봇 조작과 설비 연동의 선택 조건(추정, f22). KS B 7317 은 표준명·2021-11-11 제정 사실만 [사실]로 쓰고 단차·틈새 수치는 '미확인'으로 두며, 승강기 탑승 안전 제어 자체는 '연계 대상'으로 짧게 적는다(f17).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-76",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 4,
      "area_no": 22,
      "section": "6. 대표 접근법과 기술",
      "summary": "Open-RMF 승강기 상태의 층이 주석 없는 문자열(ref-286)이고 승강기 메시지는 운행 층을 층 이름 목록으로 두므로(ref-667), 지도 층 이름과의 층 대응표가 필요할 것으로 보인다(추정, oq-045).",
      "status": "제안"
    }
  ]
}
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

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
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

### docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md (요약)

```markdown
# 28. 공용 자원·충전·에너지 최적화

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

공용 자원을 예약·배분하고 충전·에너지를 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **공용 자원 예약·배분**: 승강기·작업대·대기 공간·버퍼 같은 공용 자원을 예약하고 나눈다
- **충전·에너지 계획**: 충전 시점·충전기 배정·대기열과 작업별 에너지 예산을 계획한다

이전 분류(2026-09-24)에서 이 페이지는 옛 16번 영역 ‘공용 자원·충전·에너지 최적화’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [옛 분류원문]

> 옛 질문: 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [옛 분류원문]

## 2. 핵심 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md (요약)

```markdown
# 29. 명령·작업 실행의 신뢰성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

명령 상태 관리, 중복 실행 방지, 관측 근거 완료 판정 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **명령 상태 관리**: 접수·실행·완료·취소 상태, 제어권, 시간 초과, 재시작 뒤 상태 복원을 관리한다
- **중복 실행 방지**: 응답이 끊긴 요청을 다시 보내도 같은 일을 두 번 하지 않게 한다
- **관측 근거 완료 판정**: 대기 시간이 지났다는 이유가 아니라 관측된 증거로 작업 단계의 완료를 인정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 12번 영역 ‘명령·작업 실행의 신뢰성’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 [옛 분류원문]

> 옛 질문: 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? [옛 분류원문]

## 2. 핵심 질문

응답이 끊긴 명령을 다시 보내도 같은 일을 두 번 하지 않게 하려면? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md (요약)

```markdown
# 30. 로봇 간 협업·물리적 인계

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇 간 협업, 인계 확인, 조작 작업 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇 간 협업**: 이동로봇과 로봇팔의 협업, 공동 운반, 작업 동기화를 조율한다
- **물리적 인계 확인**: 물건을 넘길 때 받는 쪽이 실제로 받았음을 관측으로 확인한다
- **조작 작업 관리**: 로봇팔·모바일 매니퓰레이터의 집기·싣기·놓기 작업을 관측 근거로 순서대로 진행한다

이전 분류(2026-09-24)에서 이 페이지는 옛 17번 영역 ‘로봇 간 협업·물리적 인계’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 [옛 분류원문]

> 옛 질문: AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? [옛 분류원문]

> 옛 원문 주석: 17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7] [옛 분류원문]

이전 분류 기준: 원문의 [7]은 참고문헌 [ref-007](../../references/ref-007.md)에 해당한다.[^ref-007]

## 2. 핵심 질문

한 로봇이 가져온 물건을 다른 로봇이 확실히 받았음을 어떻게 확인할까? [분류원문]

> 원문 주석: 30번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 흐름으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7] [분류원문]

원문의 [7]은 참고문헌 [ref-007](../../references/ref-007.md)에 해당한다.[^ref-007]
```

### docs/categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md (요약)

```markdown
# 32. 예외 복구·재계획·업무 연속성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

고장·통신 단절·누락에 대한 복구와 제한 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **예외 복구**: 고장·통신 단절·물품 누락·긴급 요청에 재배정·우회·수동 처리·제한 운영을 결정한다
- **제한 운영·업무 연속성**: 일부 장비가 멈춰도 업무를 이어 가는 운영 수준과 절차를 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 20번 영역 ‘예외 복구·재계획·업무 연속성’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [옛 분류원문]

> 옛 질문: 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [옛 분류원문]

## 2. 핵심 질문

작업 중 로봇이 고장 나면 남은 일은 누가 어떻게 이어받는가? [분류원문]
```

### docs/categories/design-and-simulation/capacity-sizing-and-layout-design.md (요약)

```markdown
# 35. 처리능력·규모·배치 설계

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **처리능력·규모 산정**: 처리할 일의 양에 맞는 로봇 수·종류, 충전기·작업대 배치, 운영 시간대를 정한다
- **병목 분석**: 로봇·설비·사람·승강기 가운데 어디가 병목인지 찾는다
- **다현장 자원 배치**: 여러 현장 사이에서 로봇과 자원을 어디에 얼마나 둘지 정한다
- **로봇 친화 공간 설계·개조**: 문 폭·문턱·경사·승강기 연동·충전 공간처럼 로봇이 다니고 일하기 쉬운 공간을 설계하거나 기존 공간을 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 3번 영역 ‘처리능력·거점·설비 계획’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 [옛 분류원문]

> 옛 질문: 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? [옛 분류원문]

## 2. 핵심 질문

로봇을 늘려야 할까, 공간이나 설비가 병목일까? [분류원문]
```

### docs/categories/safety/safety-and-risk-management.md (요약)

```markdown
# 48. 안전·위험 관리

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

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

### docs/categories/security-and-privacy/authentication-authorization-and-isolation.md (요약)

```markdown
# 51. 인증·권한·격리

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장비·사용자 인증**: 로봇·설비·사용자를 인증한다
- **명령 권한 관리**: 누가 어느 로봇에 어떤 명령까지 내릴 수 있는지 정하고 강제한다
- **원격 접속·유지보수 계정**: 외부 유지보수 계정이 접속할 수 있는 범위와 기록을 관리한다
- **고객·현장 격리**: 고객·현장·방문자별로 데이터와 제어를 분리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 26번 영역 ‘사이버보안·접근권한·개인정보’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [옛 분류원문]

> 옛 질문: 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [옛 분류원문]

## 2. 핵심 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
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

### runs/2026-10-11-02/research.md

```markdown
# 리서치 브리프 2026-10-11-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-02 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 23. 업무 시스템 연동 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가(주제 페이지 2026-09-25-area01-s3) — 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'가 근거(ref-136) 원문과 다름: REST·MQTT 는 미래 확장 계획(미가동)
- 섹션 4. 핵심 개념과 용어(2026-09-25-area01-s4) — OPC Job Control 은 메서드 이름 나열뿐이고 Update 의 전부 교체, Cancel 의 시작 전 조건, Stop→Ended, Completed·Closed 구분, 2.0 비호환이 없음(ref-131 원문 미열람)
- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 시나리오 하나와 국내 협력 보도(ref-137, 2차 보도·원문 미열람)뿐이고 1차 출처·제조 공장·병원 인계 확인 사례가 없음
- 섹션 6. 대표 접근법과 기술(2026-09-25-area01-s6) — 요청 응답과 상태 통지·취소 결과의 구분, WMS 쪽 우선순위 변경 허용 범위, MCP 같은 새 접점의 실제 범위 근거가 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(2026-09-25-area01-s7) — OPC Job Control 2.0 의 1.0 비호환, Open-RMF 응답 스키마, 업무 시스템–로봇 연동 제품 API(SAP Warehouse Robotics·Oracle WMS)와 Mission Dispatch MCP 미반영
- 섹션 8. 대표 연구와 자료(2026-09-25-area01-s8) — GreenAuto(ref-136) 저자 미확인·REST·MQTT 가동 여부 오기, Lorenz 외(ref-133) 적용 조건 미기재, 국내 발표의 1차 출처 없음
- 섹션 11. 열린 질문 — oq-019·oq-020·oq-021·oq-002·oq-012 와 연관 oq-046·oq-141·oq-351·oq-365 의 부분 근거 미반영
- 정정 요청 없음(외부 조사 검증에서 나온 정정만 반영)

## 조사 질문

1. 업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
2. oq-020 ISA-95 작업 지시 표준(OPC UA for ISA-95 Job Control)은 갱신·취소·중단·완료를 어떤 상태 조건으로 구별하는가? (섹션 4·6·7 겨냥)
3. oq-021·oq-351 업무 시스템–관제 연동 계약은 취소 요청의 응답과 실제 취소 결과·취소 불가를 어떻게 나눠 알리는가? (섹션 6·9 겨냥)
4. oq-019 WMS 는 우선순위 변경을 어떤 작업 상태·권한에서 허용하고, 대기열 정렬 기준은 무엇인가? (섹션 5·6 겨냥)
5. 기존 8절 자료(GreenAuto, Lorenz 외, 국내 협력 발표)의 구현 범위·적용 조건·1차 출처는 원문에서 무엇으로 확인되는가? (섹션 3·5·8 겨냥)
6. oq-141 MCP·업무 객체 해석 같은 최근 접점은 공개 코드·문서에서 실제로 무엇을 제공하는가? (섹션 6·7 겨냥)
7. oq-012 로봇 도착과 업무상 인수 확인을 별도 단계로 둔 현장 사례가 있는가? (섹션 5·9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | OPC 10031-4(OPC UA for ISA-95 Part 4: Job Control) 2.00.0 의 Update 메서드는 아직 시작하지 않은 작업 지시를 새 지시 정보로 갱신하며, 이전에 저장된 정보를 모두 교체한다. | ref-131 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [사실] | 같은 명세의 Cancel 메서드는 시작하지 않은(AllowedToStart 또는 NotAllowedToStart) 작업 지시를 취소하고 저장된 정보를 지우며, 성공하면 JobOrderList 에 그 JobOrderID 의 작업 지시가 남지 않아야 한다. | ref-131 | 아니오 | medium | 2026-10-11 | 예외·성과 | — |
| f3 | [사실] | 같은 명세의 Stop 메서드는 시작된 작업 지시를 멈추며, 성공하면 작업 지시는 Ended 상태여야 한다(Abort 가 Aborted 로 바꾸는 것과 구별된다). | ref-131 | 아니오 | medium | 2026-10-11 | 예외·성과 | — |
| f4 | [사실] | 같은 명세에서 Ended 의 하위 상태 Completed 는 작업 지시의 실행이 끝난 상태이고, Closed 는 완료 뒤 더 이상 후처리도 하지 않는 상태로 구분된다. | ref-131 | 아니오 | medium | 2026-10-11 | 완료·인계 | — |
| f5 | [사실] | Job Control 2.0 은 1.0 과 호환되지 않는 변경(breaking changes)을 담고 새 namespace 를 정의해, 이전 응용이 필요하면 두 모델을 함께 지원할 수 있게 한다. | ref-131 | 아니오 | medium | 2026-10-11 | — | — |
| f6 | [의견] | 업무 쪽 '취소'를 로봇 명령 하나로 옮기기 전에 작업의 현재 상태(시작 전·실행 중·종료 후), 지울 기록과 남길 이력, 실행 종료 뒤 후처리 여부를 먼저 정해야 할 것으로 보인다. | ref-131 | 아니오 | low | 2026-10-11 | — | — |
| f7 | [사실] | Open-RMF rmf_api_msgs 의 dispatch_task_response 스키마는 성공 분기(success=true)에서 success 와 작업 상태(task_state 를 따르는 state)를 필수로 요구하고, 실패 분기(success=false)에는 실패 이유를 담는 errors 배열을 둔다. | ref-1453 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | 같은 저장소의 cancel_task_response 스키마는 자체 필드 없이 simple_response 를 참조하며, simple_response 는 성공이면 success=true 만, 실패면 success=false 와 errors 를 필수로 요구한다. | ref-1454, ref-1455 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [추정] | 따라서 Open-RMF 의 취소 응답은 요청 처리의 성패만 알리고, 작업이 실제로 멈춰 canceled 상태가 됐는지는 작업 상태(task_state)를 따로 관측해 확인해야 할 것으로 보인다. | ref-1454, ref-1455 | 아니오 | low | 2026-10-11 | 예외·성과 | — |
| f10 | [사실] | SAP Warehouse Robotics(SAP BTP 기반 제품, SAP EWM 과 다른 제품)의 2024-07-10 자 'APIs for Integration via Fleet Management Systems' 문서는 제조사 관제(FMS) 연동 API 를 Deprecated 로 표시한다. | ref-1456, ref-1458 | 아니오 | medium | 2026-10-11 | — | — |
| f11 | [사실] | 같은 SAP Warehouse Robotics FMS 연동 문서는 시스템 설계를 단순하게 하려고 FMS 가 요청에 대한 응답을 관련 콜백 메서드 호출보다 먼저 돌려주도록 요구한다(요청→응답→콜백 순서). | ref-1456 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [사실] | 같은 문서의 취소 절차에서 FMS 는 로봇 작업 취소에 성공하면 Update Robot Task Status 로 taskStatus 를 CANCELLED 로 알리고, 취소할 수 없으면 별도 메서드 Update Robot Task Cancelation Status 로 알린다. | ref-1456 | 아니오 | medium | 2026-10-11 | 예외·성과 | — |
| f13 | [사실] | 같은 문서의 공통 메시지는 UUID 형식의 messageId 를 필수로 두고, 작업 처리 예시는 이와 별도인 robotTaskId 로 로봇 작업을 가리켜 메시지 식별과 작업 식별을 나눈다. | ref-1456 | 아니오 | medium | 2026-10-11 | — | — |
| f14 | [의견] | 업무 시스템–관제 인터페이스를 비교할 때 '접수 응답', '진행 통지(콜백·상태)', '취소 결과', '업무 확정'을 따로 보는 것이 좋아 보인다. | ref-1456, ref-1453, ref-1454 | 아니오 | low | 2026-10-11 | — | — |
| f15 | [사실] | Oracle WMS Cloud 26c REST API 의 Change Task Priority API 는 Ready·Held·Created 상태인 작업의 우선순위만 바꿀 수 있다고 명시한다. | ref-1457 | 아니오 | medium | 2026-10-11 | 제약 | — |
| f16 | [사실] | 같은 API 는 외부 시스템이 다른 작업의 긴급도에 따라 작업 우선순위를 바꿀 수 있게 하되, Task/Change task priority 권한이 켜져 있을 때만 쓸 수 있다. | ref-1457 | 아니오 | medium | 2026-10-11 | 제약 | — |
| f17 | [사실] | SAP Warehouse Robotics 의 integration services 경로 문서(판 2308)는 로봇 배정 최적화를 켜지 않으면 로봇이 속한 자원 그룹의 큐 순서를 따르고(첫 큐를 끝내야 다음 큐), 큐 안의 창고 오더를 latest starting date(LSD) 순으로, LSD 가 없으면 생성 시각 순으로 정렬한다고 설명한다. | ref-1458 | 아니오 | medium | 2026-10-11 | 제약 | — |
| f18 | [의견] | 우선순위 변경 가능 여부는 업무 작업의 상태와 로봇 실행 단계에 대해 따로 검사하고, 대기열 재정렬과 진행 중 작업 선점은 별도 정책으로 두는 것이 좋아 보인다. | ref-1457, ref-1458 | 아니오 | low | 2026-10-11 | — | — |
| f19 | [사실] | Lopes 외(Applied Sciences 2025, GreenAuto)는 플릿 관리 시스템과 IIoT 시스템의 통신이 당시 구현에서 아직 활성화되지 않았다고 명시한다. | ref-136 | 아니오 | medium | 2026-10-11 | — | — |
| f20 | [사실] | 같은 문단은 MES·ERP 에 로봇 위치·상태·이벤트 같은 정형 데이터를 내주는 REST API, AMR 의 실시간 이벤트 발행을 위한 MQTT broker, VDA 5050 연동을 모두 미래 확장으로 설계했다고 적는다. | ref-136 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [사실] | 같은 논문 §4 에서 플릿 관리 시스템 개발에 쓴 로봇은 서로 다른 제조사의 AMR 2대와 AGV 1대(ABB ASTI TriBot)였다. | ref-136 | 아니오 | medium | 2026-10-11 | 수행 자원 | — |
| f22 | [사실] | 정정: Lopes 외 논문은 REST·MQTT 연동을 사용했다고 하지 않고 MES·ERP용 REST API 와 AMR 실시간 이벤트·IIoT용 MQTT broker 를 미래 확장 계획(당시 미가동)으로 두므로, 2026-09-25-area01-s3.md 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다'와 s8 42행 GreenAuto 문장은 '계획(미가동)'으로 고쳐야 한다. | ref-136 | 아니오 | medium | 2026-10-11 | — | — |
| f23 | [사실] | Lorenz·Otto·Gendreau(Networks 2025)의 온라인 주문 묶음·순서·경로 문제(OOBSRP) 모델은 피커 한 명이 맡는 피킹 구역 하나를 다룬다. | ref-133 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [사실] | 같은 연구의 로봇 카트(Robot) 조건은 피커가 배치를 마치면 빈 로봇을 바로 쓸 수 있다고 가정한다. | ref-133 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | 같은 연구의 계산실험(§4·§4.2)은 개입형 재최적화인 Pcart·Robot 두 시스템만 대상으로 OBSRP* 인스턴스 2,600개를 만들어 그중 2,380개 이상을 최적으로 풀고 Reopt 결과와 비교했으며, §4.1 은 데이터 생성 절이다. | ref-133 | 아니오 | medium | 2026-10-11 | — | — |
| f26 | [의견] | Lorenz 외 결과는 상위 계획 갱신 정책을 비교하는 참고로 두되, 다수 피커·로봇 대기·메시지 멱등성·재고 확정 같은 연동 조건의 검증 근거로 쓰지 않는 것이 맞아 보인다. | ref-133 | 아니오 | low | 2026-10-11 | — | — |
| f27 | [추정] | 아르고(테크타카)는 2025-01-21 발표에서 자사 WMS 와 플로틱 자율주행로봇을 연동한 자동화 모델을 설계해 남이천 물류센터에서 실증하고, 플로틱이 오더 피킹 특화 로봇 30대를 지원한다고 밝혔다. | ref-1459 | 아니오 | low | 2026-10-11 | 물류창고 / 수행 자원 | — |
| f28 | [추정] | 같은 발표에서 플로틱 대표는 앞선 실증사업에서 수작업으로 20분 이상 걸리던 오더 피킹을 10분 이내로 줄였다고 말했으나, 이는 남이천 30대 사업의 성과가 아니다. | ref-1459 | 아니오 | low | 2026-10-11 | 물류창고 / 예외·성과 | 벤더 주장 |
| f29 | [추정] | LG CNS 는 2026-07-16 고객 사례에서 HD현대일렉트릭 청주 배전캠퍼스 신공장에 자재 입고·보관·생산라인 공급·완제품 이송·출하를 조율하는 창고 제어 시스템(WCS)과 SCADA 기반 통합 관제를 구축했다고 설명한다. | ref-1460 | 아니오 | low | 2026-10-11 | 제조 공장 | 벤더 주장 |
| f30 | [사실] | SAP Architecture Center 의 참조구조 'Warehouse Pick & Place with Embodied AI Robotics'(2026-05-12 갱신)는 이송 오더를 만들고 관리하지만 물건을 집지는 못하는 디지털 warehouse AI agents 와 구별되는 Embodied AI agents 의 세 가지 주요 skill 중 하나로 업무 객체의 의미 이해(WMS 데이터 속성이 물리 작업 실행에 뜻하는 바, 예: 주문 우선순위·취급 요건)를 든다. | ref-1461 | 아니오 | medium | 2026-10-11 | — | — |
| f31 | [추정] | SAP 뉴스(2025-11-05 게시, 2026-06-18 수정)는 Bosch·Aimbo 공동 개념검증에서 Aimbo 의 휴머노이드 Anigon 1대가 SAP EWM 의 배송 정보·주문 우선순위·보관 위치를 실시간 업무 문맥으로 받아 창고 작업을 수행했고, 이 사업은 탐색 단계로 전용 beta·test 시스템 환경에서 검증됐다고 밝힌다. | ref-1462 | 아니오 | low | 2026-10-11 | 물류창고 | 벤더 주장 |
| f32 | [사실] | NVIDIA Isaac Mission Dispatch README(커밋 56455eb 고정본)의 Latest Update 표는 2026-03 에 Mission Dispatch MCP 추가를, 2026-08 에 VDA5050 3.0 지원과 generic action node 추가를 기록한다. | ref-1341 | 아니오 | medium | 2026-10-11 | — | — |
| f33 | [사실] | 같은 커밋의 Mission Dispatch MCP 서버는 도구 11개(로봇 상태·미션 상태·미션 중 로봇·유휴 로봇·플릿 요약·로봇 건강 점검·미션 큐·최근 실패 조회, 연결 시험, 로봇 등록, 좌표 이동 미션 전송)를 등록하며, 미션 취소 도구는 없다. | ref-1341 | 아니오 | medium | 2026-10-11 | — | — |
| f34 | [사실] | 같은 MCP 서버의 이동 미션 핸들러(_handle_dispatch_mission)는 queries.py 의 dispatch_move_mission 을 호출하고, 이 함수는 경유점 하나짜리 route 미션 트리와 timeout·deadline 을 담아 Mission Dispatch REST API 의 mission 경로로 POST 한다. | ref-1341 | 아니오 | medium | 2026-10-11 | — | — |
| f35 | [사실] | robotmcp 의 demos-ros-mcp-server 예제 1 README 는 Ubuntu 22.04·ROS 2 Humble·Ignition Gazebo Fortress 에서 ROS-MCP 서버로 창고 시뮬레이션 속 Tugbot 1대를 자연어로 이동시키고 라이다·주행거리 센서와 위치를 조회하는 예시를 설명한다. | ref-1463 | 아니오 | medium | 2026-10-11 | — | — |
| f36 | [의견] | MCP 를 업무 요청의 접점으로 평가할 때는 공개 코드가 주는 도구 범위(조회·등록·좌표 이동, 취소 없음)와 업무 요구(주문 ID 대응·허용 상태 검사·실행 전 승인·결과 대조·취소)를 따로 확인해야 하며, 공개 코드의 존재를 다사업자 WMS 주문·재고 처리의 운영 검증으로 볼 수 없다. | ref-1341, ref-1463 | 아니오 | low | 2026-10-11 | — | — |
| f37 | [사실] | Tartu 대학병원 실증의 시료 운반 절차에서는 로봇이 실험실에 도착하면 직원이 화면 버튼으로 시료를 모두 꺼냈음을 확인하고 ingestor 가 RMF 에 인수 완료를 알린 뒤에야 로봇을 ICU 로 되돌리는 요청이 나간다. | ref-869 | 아니오 | medium | 2026-10-11 | 병원 / 완료·인계 | — |
| f38 | [사실] | 같은 논문은 병원 안 운반 실증을 PAL Robotics TIAGo 1대로 했고, TIAGo·Clearpath Jackal 두 이기종 로봇을 RMF 로 관리하는 능력은 별도 시험 환경에서 검증했으며, 병원 안에는 여러 배송 로봇을 아직 적용하지 않았다고 밝힌다. | ref-869 | 아니오 | medium | 2026-10-11 | 병원 / 수행 자원 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-131 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 2024-01-31 | 표준 | high | 2026-10-11 | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 | 아니오 |
| ref-1453 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_response.json | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/dispatch_task_response.json | 아니오 |
| ref-1454 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_response.json | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/cancel_task_response.json | 아니오 |
| ref-1455 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/simple_response.json | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_api_msgs/blob/e9b7630c73a6fb41448ac143c0d7061f2b4389a2/rmf_api_msgs/schemas/simple_response.json | 아니오 |
| ref-1456 | SAP | APIs for Integration via Fleet Management Systems (API for Integration with Fleet Management Systems (Deprecated)) | 2024-07-10 | 벤더 문서 | medium | 2026-10-11 | https://help.sap.com/doc/a02ad3695d5845fca1678810cb83562b/LATEST/en-US/379d6d880e5d4007b3751618080da80f_1.pdf | 아니오 |
| ref-1457 | Oracle | WMS REST API Guide — Change Priority (Oracle Warehouse Management Cloud 26c) | 2026-08-14 | 벤더 문서 | medium | 2026-10-11 | https://docs.oracle.com/en/cloud/saas/warehouse-management/26c/owmre/change-priority.html | 아니오 |
| ref-1458 | SAP | End-User Information for Integration via Integration Services (SAP Warehouse Robotics, Document Version 2308) | 2023-08-19 | 벤더 문서 | medium | 2026-10-11 | https://help.sap.com/doc/f08ea8f8686c46e89f1d7ed121f19d68/LATEST/en-US/b82aa9c86bd74777b86ec7f5766252d0.pdf | 아니오 |
| ref-1459 | 아르고 풀필먼트(테크타카) | 아르고, 플로틱과 로봇 기반 물류 생산성 향상 실증 본격 실시 | 2025-01-21 | 벤더 문서 | medium | 2026-10-11 | https://blog.argoport.com/pr-robotcooperation250121 | 아니오 |
| ref-1460 | LG CNS | 로봇 기반 물류 자동화와 통합 관제로 HD현대일렉트릭 신공장의 새로운 운영 체계를 구축하다 | 2026-07-16 | 벤더 문서 | medium | 2026-10-11 | https://www.lgcns.com/kr/moa/customer-story/detail.smartlogistics-robotic-logistics-2607-1 | 아니오 |
| ref-1461 | SAP Architecture Center | Warehouse Pick & Place with Embodied AI Robotics | 미확인 | 벤더 문서 | medium | 2026-10-11 | https://architecture.learning.sap.com/docs/ref-arch/7e4168 | 아니오 |
| ref-1462 | SAP (Lukasz Ostrowski, SAP News Center) | How SAP Brings Business AI into the Physical World: New Robotics Pilots Across Warehouse, Manufacturing, and Inspection Use Cases | 2025-11-05 | 벤더 문서 | medium | 2026-10-11 | https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/ | 아니오 |
| ref-1463 | robotmcp | demos-ros-mcp-server — Example 1: Tugbot Warehouse Simulation (Ignition Gazebo) README | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/robotmcp/demos-ros-mcp-server/blob/edbc642849bdde1187771a15e557ec9e219184a5/1_Gazebo_Tugbot/README.md | 아니오 |
| ref-136 | Lopes, D., Pereira, T., Gonçalves, A. 외 (저자 17명; Applied Sciences, MDPI) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025-06-27 | 논문 | high | 2026-10-11 | https://www.mdpi.com/2076-3417/15/13/7235 | 아니오 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025-05 | 논문 | high | 2026-10-11 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 아니오 |
| ref-1341 | NVIDIA (nvidia-isaac GitHub) | isaac_mission_dispatch — README | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/nvidia-isaac/isaac_mission_dispatch | 아니오 |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-10-11 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/business-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 갱신(차등). 대상 문장은 실제 위키 위치로 적는다(메모가 가리킨 로컬 보존본은 저장소에 없음). 섹션 3(주제 페이지 2026-09-25-area01-s3) — 39행 '확인한 연동 사례는 자체 REST·MQTT 인터페이스를 썼다 [추정][^ref-136]'를 'MES·ERP용 REST API, AMR 실시간 이벤트·IIoT용 MQTT broker 는 계획(미가동)'으로 정정(f22, 근거 f19·f20). / 섹션 4(2026-09-25-area01-s4 40행 작업 지시 항목) — Update 전부 교체(f1), Cancel 시작 전 조건·기록 제거(f2), Stop→Ended(f3), Completed·Closed 구분(f4); ref-131 원문 열람으로 '(원문 미열람)' 해제. Abort→Aborted·메서드 목록·2.00.0 2024-01-31 은 기존 내용 확인(s4 40행·s7 44행)으로 중복 추가 안 함. / 섹션 5 — 국내 문단(본문 88행·s8 43행)에 1차 출처 ref-1459 병기와 '30대 지원 발표, 20분 이상→10분 이내는 앞선 실증 성과'(f27·f28, 벤더 주장), 제조 공장 사례 LG CNS WCS·SCADA(f29, 벤더 주장), 병원 인계 확인 후 ICU 복귀·TIAGo 1대/Jackal 별도 시험(f37·f38; ICU→검사실 운반은 ref-869 기존 내용 확인), Bosch·Aimbo 단일 Anigon 개념검증(f31, 벤더 주장·beta/test 환경). / 섹션 6(2026-09-25-area01-s6) — 취소 번역 전 상태 확인(f6), Open-RMF 배정 응답 success·state 필수(f7)와 취소 응답 simple_response 참조(f8)·관측 분리(f9), SAP Warehouse Robotics FMS API(폐기)의 응답-콜백 순서·취소 결과 통지·messageId/robotTaskId(f10~f13, 제품명은 SAP Warehouse Robotics(SAP BTP 기반)로 쓰고 EWM 과 구별), 인터페이스 비교 열(f14), 우선순위 변경 허용 상태·권한·LSD 정렬(f15~f18), Mission Dispatch MCP 도구 범위·이동 경로·Tugbot 시뮬레이션(f33~f36). priority 의 fleet 스키마 일치·cancel 요청 type·task_id 필수·task_state 상태 열거는 기존 내용 확인(s6 43행·s4 42행), phase별 취소 반응(rmf_task README ref-404·Task.hpp ref-366)은 2026-10-10 area24-s6·채팅 트랙 stage-3 에 있어 넣지 않음. / 섹션 7(2026-09-25-area01-s7 표) — OPC Job Control 행에 2.0 의 1.0 비호환·새 namespace(f5)와 '상태 전이는 원문 미열람' 해제, Open-RMF 행에 dispatch·cancel 응답 스키마(f7·f8), 새 행: SAP Warehouse Robotics FMS API(폐기, f10), Oracle WMS Change Priority API(f15·f16), Mission Dispatch MCP(2026-03)·VDA5050 3.0 지원(2026-08) 기록(f32), SAP Embodied AI 참조구조(f30). ISA-95 Part 1 2025 발행 발표(ref-002)는 기존 내용 확인으로 넣지 않음. GS1 CBV 2.0 receiving·arriving·accepting·unloading 은 area02·17·24 와 EPCIS 인계 페이지(ref-044)에 있어 넣지 않음. / 섹션 8(2026-09-25-area01-s8) — 42행 GreenAuto 항목 저자 17명·발행일로 서지 정정, 'REST·MQTT·VDA 5050 은 미래 확장(미가동), 개발 대상 AMR 2·AGV 1'(f19~f22; 최대 20대·120 ms 는 2026-10-10 area20-s8 기존 내용 확인), 40행 Lorenz 항목에 단일 피커·단일 구역, 빈 로봇 즉시 가용 가정, §4·§4.2 의 Pcart·Robot 2,600개 중 2,380개 이상 최적 풀이 범위 추가(f23~f26, 기존 결과는 유지), 43행 머니투데이 항목에 1차 출처(f27·f28). / 섹션 9 — 접수 응답·진행 통지·취소 결과·업무 확정 분리(f9·f14), 도착과 인수 확인 분리(f37), MCP 도구 범위와 업무 요구 분리(f36)를 책임 경계 근거로. / 섹션 10 — 12. 채팅으로 업무 지시·오케스트레이션(f33~f36, oq-141), 63. 병원·의료(f37·f38), 62. 제조 공장(f29), 26. 작업 순서·스케줄링(f17·f23~f26) 연결 보강. / 섹션 11(2026-09-25-area01-s11) — '새 질문' 세 개를 실제 id 로 표기(39행 oq-019, 40행 oq-020, 41행 oq-021). 부분 근거(해결 아님): oq-019 ← f15~f18, oq-020 ← f1~f6·f7, oq-021(·oq-351) ← f8·f9·f12, oq-012 ← f37(해외 사례, 국내 기준 미확인), oq-365 ← f21, oq-046 ← f11·f13, oq-141 ← f33·f36. oq-002 는 이번 근거 없음(미해결). 새 질문 3건. 다음 실행 후보: 12. 채팅으로 업무 지시·오케스트레이션(MCP 도구 범위 f33~f36), 26. 작업 순서·스케줄링(Lorenz 적용 조건 f23~f25). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 아르고(테크타카)–플로틱 남이천 물류센터 협력(오더 피킹 로봇 30대 지원 발표) 이후 실증의 시험 기간·성공 기준·완료 결과가 공개됐는가? | 관련 영역: 23. 업무 시스템 연동, 61. 물류창고 | 근거: f27 | 종류: 일반
- Yu·Srinivas(2025) 동적 주문 피킹 논문 원문의 실험 조건과 서지(권·호·쪽)로 기존 위키의 AOCT·ATT·AWTD 결과 서술을 재검증하면 그대로 맞는가? | 관련 영역: 23. 업무 시스템 연동, 26. 작업 순서·스케줄링 | 근거: ref-132 | 종류: 일반
- ISA-95 Part 1(ANSI/ISA-95.00.01-2025) 규격 본문에서 바뀐 조항은 무엇이며, OPC UA for ISA-95 Job Control 2.0·B2MML 과의 관계를 바꾸는가? | 관련 영역: 23. 업무 시스템 연동, 21. 상호운용 표준·적합성 | 근거: ref-002 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 11건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-02/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - GitHub 고정 커밋의 커밋일(rmf_api_msgs e9b7630 2026-09-19, rmf_task 3a6af29 2026-09-25, demos-ros-mcp-server edbc642 2026-07-09, isaac_mission_dispatch 56455eb 2026-09-15)은 확인 불가(403)라 published null
    - ref-1461(SAP 참조구조)의 최초 발행일 미확인(갱신 2026-05-12 만 확인), ref-133 온라인 발행 일자 미확인(2025-05 까지만)
    - f31: Bosch·Aimbo 개념검증의 실시일과 생산 운영 여부 미확인(뉴스 게시 2025-11-05, 수정 2026-06-18)
    - f27·f28: 남이천 30대 실증의 시험 기간·결과 미확인, '20분 이상→10분 이내'의 측정 조건 미공개
    - f29: LG CNS 사례의 다제조사 수·API·주문 상관키·생산계획 변경 승인 규칙 미공개, 성과 수치는 채택하지 않음
    - f21: GreenAuto 개발 3대와 §6.2 최대 20대 동시 감시의 실물/가상 구성·기간 미확인(oq-365). F20b(주된 역할은 통합 감시, 수집 데이터에 task progress 포함)는 기존 area20 서술과 겹쳐 finding 으로 넣지 않음
    - f9·f13: 취소 응답과 실제 정지의 시간 관계, 중복 요청 효과, SAP 현재 권장 연동 경로의 API 계약과 폐기 API 의 대체 관계는 확인 못 함(oq-046 관련)
    - oq-020: ISA-95 JobOrderID·JobResponse 와 VDA 5050 orderId·Open-RMF booking.id 의 공개 매핑 명세는 찾지 못함
    - oq-002: 국내 로봇 적재·하역 결과에 SSCC·EPCIS 를 연결한 운영 사례 없음. GS1 Korea SSCC 설명 페이지(메모 n16)는 물류 단위 식별 정의뿐이고 기존 ref-017 과 겹쳐 출처로 넣지 않음
    - oq-012·oq-021: 국내 WMS 입고·인수 확정의 상관키·시간 초과 기준과 적재 후 취소의 반송·재고 반제 결정권자는 확인 못 함
    - oq-141: MCP 경유 다사업자 WMS 주문·재고 처리의 운영 결과·권한·실패 복구 시험은 찾지 못함
    - ISA-95 Part 1 2025 규격 본문은 유료라 미열람(ISA 발표 ref-002 는 원문 확인됐으나 내용이 기존 s7 과 같아 finding 없음)
- 범위 경계 위반 의심:
    - f29: WCS·SCADA 통합 관제는 22. 설비·건물 시스템 연동·38. 모니터링과 겹치므로 이 영역에는 생산계획→실행 작업 조율 역할의 예로만 씀
    - f30·f31: Embodied AI 휴머노이드 작업 수행은 44. 로봇 기반 모델·언어 모델 계획 쪽 내용이라 업무 객체 해석 계층의 근거로만 씀
    - f33~f36: MCP 도구 노출은 12. 채팅으로 업무 지시·오케스트레이션과 겹치므로 업무 요청 접점 범위 판단으로 한정
    - f23~f26: 재최적화 알고리즘의 최적성은 26. 작업 순서·스케줄링 쪽 내용이라 적용 조건만 씀
    - f37·f38: 병원 인계 절차는 63. 병원·의료·30. 로봇 간 협업·물리적 인계와 겹치므로 도착과 인수 확인 분리 근거로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 11건(ref-1453, ref-1454, ref-1455, ref-1456, ref-1457, ref-1458, ref-1459, ref-1460, ref-1461, ref-1462, ref-1463, 예약 구간 ref-1453~ref-1482 안, 한도 15 이내), 재사용 5건. 메모 출처 매핑(검증 결과 E절): n1→ref-131, n2→ref-1453(dispatch_task_response)·ref-1454(cancel_task_response)·ref-1455(simple_response) 신규(task_request ref-125·cancel_task_request ref-126·task_state ref-111·README ref-1028 은 해당 내용이 기존 위키에 있어 이번 finding 에 쓰지 않음), n3→ref-404(K03 중복이라 미사용), n4→ref-1456, n5→ref-1457, n6→ref-014(K06 중복이라 미사용), n7→ref-1459(기존 2차 보도 ref-137 과 같은 사건), n8→ref-1460, n9→ref-136, n10→ref-133, n11→ref-1461, n12→ref-1462, n13→ref-1463, n14→ref-1341, n15→ref-869, n16 미사용, n17→ref-002(중복이라 미사용), n18→ref-1458. 검증 수정 반영: 위키 중복(K03 전체, K06 전체, F04, F06, F08 task_id, F09 상태 열거, F29, F31)은 finding 으로 넣지 않고 rationale 에 '기존 내용 확인'으로만; GreenAuto 는 'MES·ERP용 REST API, AMR 실시간 이벤트·IIoT용 MQTT broker 는 계획(미가동)'으로(메모 요약의 'MES·ERP용 REST/MQTT' 바로잡음) 하고 s3 39행·s8 42행 정정 finding(f22) 추가; F23 은 §4·§4.2 와 Pcart·Robot 2,600개 중 2,380개 이상 최적 풀이 범위로; K09 는 '20분 이상→10분 이내'(메모의 '10분 미만' 정정); F24 는 디지털 warehouse AI agents 와 구별되는 Embodied AI agents 의 세 skill 중 하나로; SAP 제품명은 SAP Warehouse Robotics(SAP BTP 기반)로 쓰고 EWM 과 구별; n12 수정일 2026-06-18; ref-136 저자 17명·2025-06-27·Appl. Sci. 15(13) 7235 로 정정; ref-133 published 2025-05; 메모의 출처 집계(기존 5·새 13)는 틀려 기존 9·새 9(메모 단위)로 바로잡음. 교차 확인 0건: Open-RMF 스키마 세 파일은 같은 프로젝트, SAP 문서 셋은 같은 회사, Oracle·SAP 은 서로 다른 기능이라 같은 주장의 교차 확인이 아니다. 벤더 주장(f28·f29·f31)은 vendor_claim·추정·'벤더 주장: ' 표시, 아르고 협력 발표(f27)는 추정. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-019 근거 f15~f18, oq-020 근거 f1~f7, oq-021·oq-351 근거 f8·f9·f12, oq-012 근거 f37, oq-365 근거 f21, oq-046 근거 f11·f13, oq-141 근거 f33·f36, oq-002 근거 없음. 메모 새 질문 U01~U11 가운데 기존 질문과 겹치는 U01(oq-020)·U02(oq-019)·U03(oq-021·oq-351)·U04(oq-002)·U05(oq-012)·U07(oq-365)·U09(oq-046)·U10(oq-141)은 새로 만들지 않고 U06·U08·U11 만 올렸다. 현장 유형 사례 finding: 물류창고(f27·f28·f31), 제조 공장(f29), 병원(f37·f38). 국내 자료는 아르고 발표(ref-1459)와 LG CNS 사례(ref-1460). 용어 후보 없음. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-10-11-01/research.md

```markdown
# 리서치 브리프 2026-10-11-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-01 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 21. 상호운용 표준·적합성 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 수행 자원 칸이 'VDA 5050 3.0.0 에서 주문 배정·경로 계산…은 관제 쪽'으로 경로 계산을 모든 로봇에 일반화함(원문은 선 유도 로봇). 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — '제조사가 자체 인증하거나' 문장의 근거 없음(정정 필요). 선택 필드·재전송·취소 후 갱신을 확인하는 동작 시험 방법 없음. OTTO 인증 발표 각주가 원문 미열람
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 행 발행일 표기, MassRobotics 행 '원문 미열람', OPC 행 '자체·독립 시험소 인증' 표현. 3.0.0 태그 스키마 끝 쉼표, OPC UA Robotics 서버 Facet, KS B ISO 22166-202 미반영. 트랙 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2: IDS 1.0 을 BIM 데이터 교환 요구·적합성 검사 수단으로) 미처리
- 섹션 8. 대표 연구와 자료 — vda5050-lab 원문 미열람 표시, VDA 5050 통신 평가 논문 없음
- 섹션 10. 다른 연구영역과의 연결 — 42. 분산 시스템·통신·컴퓨팅 구조, 14. 도면·BIM에서 지도 만들기 연결 없음
- 섹션 11. 열린 질문 — oq-005·oq-055·oq-091·oq-026 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
2. oq-005 VDA 5050 3.0.0 의 날짜는 공식 저장소 명세·카탈로그·보도자료·참여 업체 발표에서 각각 무엇으로 표시되는가? (섹션 7·11 겨냥)
3. oq-055 VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 도구·벤더 간 인증·전시 시연·인정 시험소 인증을 연동 승인 근거로 어떻게 구분해 쓸 수 있는가? (섹션 6·8·11 겨냥)
4. oq-091 VDA 5050 3.0.0 태그의 JSON 스키마를 시험 입력으로 그대로 쓸 수 있는가? (섹션 7·11 겨냥)
5. oq-026 KS B 7321-2 와 KS B ISO 22166-202 는 국가표준 목록에서 무엇으로 확인되는가? TTAK.KO-10.1295-Part8 은 공식 목록에서 확인되는가? (섹션 7·11 겨냥, 한국 자료 우선)
6. 트랙 반영 제안 2026-10-09-26: IDS 1.0(buildingSMART)의 적용 대상·요구 구조·패싯·값 제한은 발행 기관 자료로 무엇이며, 21. 상호운용 표준·적합성의 적합성 검사 수단으로 볼 수 있는가? (섹션 7·10 겨냥)
7. 기존 문장 점검: VDA 5050 3.0.0 은 경로 계산을 어느 로봇에 대해 관제 책임으로 두는가, OPC Foundation 은 제조사 자체 인증을 허용하는가? (섹션 5·6·7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA5050 공식 저장소의 3.0.0 명세 마크다운 표지는 판을 'Version 3.0.0'으로만 적고 날짜를 적지 않으며, VDA 가 배포하는 PDF 표지의 날짜 표기는 이번 실행에서 PDF 본문 텍스트를 읽지 못해 확인하지 못했다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [의견] | 구축자 의견: 21번 7절 표 VDA 5050 행의 발행일은 단일 날짜로 확정하지 않고 '미확인'을 유지하되, VDA 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)가 서로 다르다는 점은 20번 주제 페이지의 날짜 절로 연결하고, PDF 표지의 'March 2026' 표기는 원문 확인 전까지 [추정]으로 두는 것이 맞다. | ref-1412, ref-032, ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 §5.3 의 관제 기능 목록은 경로 계산을 일반 기능이 아니라 선 유도(line-guided) 이동로봇의 경로 계산·안내로 적고, §5.4 는 이동로봇 기능을 선 유도형과 자유 주행형(freely navigating)의 경로 실행으로 나눠 서술한다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f4 | [사실] | VDA 의 3.0 발표 보도자료는 자율도가 높은 이동로봇이 지정된 경유점 사이 경로를 스스로 계획해 상세 경로 계획이 로봇에서 이뤄지고, 그 경로를 경로 공유(path sharing)로 중앙 관제와 공유하는 구성을 설명한다. | ref-032 | 아니오 | medium | 2026-04-20 | — | — |
| f5 | [의견] | 구축자 의견: 21번 본문 5절 수행 자원 칸과 분리 7절 본문의 '주문 배정·경로 계산·…은 관제 쪽' 문장은 '선 유도 로봇의 경로 계산·안내'로 고치고, 자유 주행 로봇은 상세 경로를 스스로 계획해 공유할 수 있음을 병기해 모든 이동로봇의 상세 경로를 관제가 계산한다고 일반화하지 않는 것이 맞다. | ref-031, ref-032 | 아니오 | medium | 2026-10-11 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 §7.1.1 은 로봇이 받은 선택(optional) 필드를 무시해서는 안 되고 쓸 수 없으면 UNSUPPORTED_PARAMETER(CRITICAL)로 알리게 하며, 관제(fleet control)에는 로봇이 지원하는 선택 필드만 보내도록 의무를 둔다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 연동 시험의 기대값으로 쓸 응답을 조항으로 정한다: 지원하지 않는 선택 파라미터가 든 주문은 UNSUPPORTED_PARAMETER(CRITICAL)로 거절, 같은 orderUpdateId 재전송은 내용이 같으면 무시하고 다르면 SAME_ORDER_UPDATE_ID(WARNING)를 보고하며 이전 주문을 계속, 취소된 주문의 후속 갱신은 ORDER_UPDATE_FOLLOWING_CANCEL(WARNING). | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [의견] | 구축자 의견: 로봇 연동 승인에는 버전 문자열 확인에 더해 (1) 미지원 선택 필드 주문 거절, (2) 같은 번호·같은 내용 재전송 무시, (3) 같은 번호·다른 내용 재전송 경고, (4) 취소 후 갱신 경고, (5) 관제가 로봇 factsheet 가 지원한다고 밝힌 선택 필드만 보내는지를 확인하는 동작 시험표를 두고, 수신 직전 주문 상태와 관측 로그 누락 여부를 함께 보존하는 것이 좋다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | VDA5050 공식 저장소 3.0.0 태그의 json_schemas/order.schema·factsheet.schema·visualization.schema 에는 닫는 괄호 바로 앞에 쉼표가 오는 끝 쉼표(trailing comma)가 있어 엄격한 JSON 으로 읽히지 않으며, main 브랜치의 order.schema 는 같은 자리(궤적 제어점 weight 속성)에 끝 쉼표가 없다. | ref-1430, ref-1431, ref-1432, ref-413 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [의견] | 구축자 의견: VDA 5050 3.0.0 을 시험 입력으로 쓸 때는 '공식 태그'와 '파싱 가능한 시험 입력'을 따로 확인하고, 수정한 스키마를 쓰면 원본과의 차이·수정 근거·해시를 보존하며 main 브랜치 내용을 설명 없이 섞지 않는 것이 좋다. | ref-1430, ref-413 | 아니오 | medium | 2026-10-11 | — | — |
| f13 | [사실] | vda5050-lab README(커밋 4a1a812)는 현재 판 v0.2.0 을 개발자 프리뷰(Developer Preview)로 부르며 오프라인 진단 구현과 범위가 제한된 합성 시연을 담는다고 설명하고, 공개 알파나 인증 주장이 아니며 실제 고객 기록·외부 시험 대상(DUT)·실물 하드웨어 실행을 검증하지 않았다고 밝힌다. | ref-408 | 아니오 | medium | 2026-10-11 | — | — |
| f14 | [의견] | 구축자 의견: vda5050-lab 은 MQTT 기록 진단의 보조 도구 후보로만 두고, 그 판정을 구매·연동 승인 전체의 대체물로 쓰지 않는 것이 맞다. | ref-408 | 아니오 | medium | 2026-10-11 | — | — |
| f15 | [사실] | OPC Foundation 'How to Certify' 는 제조사가 인증 시험 전에 가능한 많은 시험을 미리 해 보도록 권고하고, 재단이 제공하는 적합성 시험 도구(compliance test tools)는 시험소가 시험에 쓰는 도구라고 설명한다. | ref-705 | 아니오 | medium | 2026-10-11 | — | — |
| f16 | [사실] | OPC Foundation 인증 개요 페이지는 인증 제품이 재단이 인정한 인증 시험소에서 시험을 거쳤다고 설명하고, 인증된 SDK 를 쓴 응용도 공식 인증 제품이 되려면 각자 인증 시험을 받아야 한다고 밝힌다. | ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | 확인한 OPC Foundation 인증 안내 두 페이지에는 제조사가 스스로 인증하는(self-certification) 경로가 없으므로, 21번 분리 6절의 '제조사가 자체 인증하거나'와 분리 7절 표 OPC 행의 '자체·독립 시험소 인증'은 이 두 출처로 뒷받침되지 않는 표현이다. | ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [의견] | 구축자 의견: OPC 적합성 체계는 '제조사의 적합성 시험 도구 사전 점검(권고)'과 '인정 시험소 인증'을 구분하는 문장으로 고치고, 이 구조를 VDA 5050 의 인증 체계로 그대로 옮겨 쓰지 않는 것이 맞다. | ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | MassRobotics AMR_Interop_Standard.json(커밋 f9357a4)의 최상위 oneOf 는 identityReport 와 statusReport 두 정의만 참조하고, 위치(location) 정의는 x·y·angle·planarDatum 네 필드를 모두 필수로 두며, 명령·주문·작업 메시지 정의는 없다. | ref-230 | 아니오 | medium | 2026-10-11 | — | — |
| f20 | [의견] | 구축자 의견: MassRobotics 보고 메시지(신원·상태) 교환만으로 작업 명령 호환성이나 좌표계 정합을 확보했다고 주장하지 않는 것이 맞다. | ref-230 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [사실] | OPC 40010-1(OPC UA for Robotics Part 1) 1.02판 §11.2.2 는 서버 기능 묶음(Facet)을 기본(Base)·운전(MDS Operation)·자산관리 확장(AM Extended)·상태감시 확장(CM Extended) 넷으로 나누고, 표 124~127 에서 각 적합성 단위를 필수(M)·선택(O)으로 구분한다. | ref-034 | 아니오 | medium | 2025-09-08 | — | — |
| f22 | [의견] | 구축자 의견: 연동 요구에는 'OPC UA 지원' 대신 OPC UA Robotics 판·서버 Facet·선택 단위·인증 범위를 적게 하고, 이 정보모델을 VDA 5050 주문 스키마와 일대일로 자동 변환할 수 있다고 보지 않는 것이 좋다. | ref-034 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [사실] | 국가표준인증통합정보시스템(KSSN) 상세 페이지에는 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 이번 열람에서는 번호와 제목만 보였고 제정일·국제표준 부합화·고시 정보는 보이지 않았다. | ref-138 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | KSSN 상세 페이지에는 KS B 7321-2 와 별도로 KS B ISO 22166-202 '로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 제정일·부합화 수준(IDT 여부)·고시 정보는 이번 열람에서 보이지 않았다. | ref-1435 | 아니오 | medium | 2026-10-11 | — | — |
| f26 | [의견] | 구축자 의견: oq-026 은 열림을 유지하고, KS B ISO 22166-202 가 국가표준 목록에 따로 있다는 점만 확인할 거리로 남기며, 그 제정일·부합화 수준과 KS B 7321-2 와의 대체 관계, 국내 적용 사례는 미확인으로 둔다. | ref-138, ref-1435 | 아니오 | low | 2026-10-11 | — | — |
| f30 | [추정] | OTTO by Rockwell Automation 은 2026-04-09 보도자료에서 OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 소프트웨어 업체와 인증을 마쳤다고 밝혔으나, 시험한 프로토콜 판·시험 항목·시험 기관은 밝히지 않는다. | ref-608 | 아니오 | low | 2026-04-09 | — | 벤더 주장 |
| f31 | [사실] | VDMA 의 Mesh-Up 2025 안내는 automatica 2025(뮌헨, 2025-06-24~27) 전시장에서 9개 기업이 참여하고 MHP 가 상위 관제를 맡아, 여러 이동로봇이 작업대를 공급하는 양식화한 생산 라인을 보여 주는 혼합 플릿 시연(전시 시연이며 실제 공장 배치가 아님)을 설명한다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 / 수행 자원 | — |
| f32 | [사실] | 같은 Mesh-Up 2025 안내(automatica 2025 전시 시연, 실제 공장 배치 아님)는 관제 소프트웨어 공급자를 바꿔 고를 수 있는 점을 전시장에서 실시간으로 시연하지는 않는다고 밝힌다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 / 예외·성과 | — |
| f33 | [의견] | 구축자 의견: Mesh-Up 같은 전시 시연은 5절 '제조 공장' 현장 유형의 혼합 플릿 구성 예로만 쓰고 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히며, 실제 도입 사례나 현장 관제 교체가 검증된 근거로 세지 않는 것이 맞다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 | — |
| f34 | [사실] | Wagner 외(제22회 IEEE WFCS 2026)는 표준이 원격 조작(teleoperation)을 기본으로 다루지 않는다고 보고 VDA 5050 원격 조작 확장과 재현 평가용 VDA 5050 트래픽 생성기를 제안하며, VDA 5050 메시지·미들웨어 전송·Open RAN 무선 링크를 잇는 구성에서 지연과 통신 오버헤드를 평가한다. | ref-1437 | 아니오 | medium | 2026-04 | — | — |
| f36 | [사실] | TU Dortmund 통신망 연구실의 논문 소개(2026-04-24)는 이 평가가 재현성 높은 가상 무선(virtual-radio) 시험대와 실제 무선(over-the-air) 검증 구성을 함께 썼다고 설명하며, 정량 결과와 로봇 대수는 소개문에 없다. | ref-1438 | 아니오 | medium | 2026-04-24 | — | — |
| f37 | [의견] | 구축자 의견: 21번에서는 Wagner 외 연구를 VDA 5050 통신 부하·지연 평가로 소개하되 적합성 시험과 구별하고, 상세 네트워크 설계는 42. 분산 시스템·통신·컴퓨팅 구조 연결로만 두는 것이 맞다. | ref-1437, ref-1438 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [의견] | 구축자 의견: VDA 5050 연동 승인의 근거는 제3자 도구의 자체 진단, 벤더 간 인증 발표, 전시 시연, 인정 시험소 인증을 서로 다른 근거 수준으로 나눠 기록하는 것이 맞다. | ref-408, ref-608, ref-1436, ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [추정] | VDA 5050 작업반 참여 업체인 Idealworks 는 2026년 3월 소식 글에서 VDMA·VDA 가 2월 17일 3.0.0 판을 정식 채택했고 이어 법적 승인 절차를 거쳤다고 적어, VDA 공식 자료의 날짜 표시(카탈로그 2026-03-17·보도자료 2026-04-20)와 또 다른 날짜를 제시한다. | ref-1442 | 아니오 | low | 2026-03 | — | — |
| f40 | [사실] | buildingSMART 는 정보 전달 명세(Information Delivery Specification, IDS)를 2024-06-01 승인된 공식 표준으로 소개하고, 데이터 요구를 기계가 읽을 수 있게 기술해 IFC 모델의 적합성을 자동으로 검사할 수 있게 한다고 설명하며, 1.0 이전 판은 공식 표준이 아니라고 밝힌다. | ref-1439 | 아니오 | medium | 2024-06-01 | — | — |
| f41 | [사실] | IDS 공식 사용자 설명서는 IDS 파일이 하나 이상의 명세(specification)로 이루어지고 각 명세가 적용 대상(applicability)과 요구(requirements)를 가지며, 둘 다 엔터티·속성(attribute)·분류·속성 값(property)·재료·소속(partOf) 패싯으로 구성되고, 받는 쪽이 IDS 와 IFC 를 함께 불러 검사해 불일치 보고를 얻는다고 설명한다. | ref-1362 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [사실] | IDS 사용자 설명서는 패싯 파라미터에 단순 값 대신 열거(enumeration)·패턴(pattern)·범위(bounds)·길이(length)의 복합 제한을 걸 수 있다고 설명한다. | ref-1365 | 아니오 | medium | 2026-10-11 | — | — |
| f43 | [사실] | IDS 공식 저장소의 문서 안내는 소프트웨어 구현의 IDS 읽기·검사 기능이 올바른지 확인하기 위한 .ids·.ifc 쌍 250개 이상의 시험 파일 묶음을 TestCases 폴더에 둔다고 설명한다. | ref-1443 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 구축자 의견: 21번 7절에는 IDS 1.0 을 '건물 정보 모델(IFC) 데이터 교환 요구의 적합성 검사 수단'으로 짧게 두고, 검사 도구 자체도 공식 시험 파일 묶음으로 확인할 수 있다는 점을 적되, 로봇–관제 메시지 적합성 시험과는 구별하며, 로봇 지도용 BIM 객체·속성 요구의 세부는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙에 두는 것이 맞다. | ref-1439, ref-1362, ref-1443 | 아니오 | medium | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04-20 | 표준 | medium | 2026-10-11 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-1412 | VDA(Verband der Automobilindustrie) | VDA 5050 | 2026-03-17 | 표준 | medium | 2026-10-11 | https://www.vda.de/en/news/publications/publication/vda-5050 | 아니오 |
| ref-1430 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/order.schema | 아니오 |
| ref-1431 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema | 아니오 |
| ref-1432 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/visualization.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/visualization.schema | 아니오 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema (main) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 아니오 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/ekusiadadus/vda5050-lab | 아니오 |
| ref-705 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | 표준 | medium | 2026-10-11 | https://opcfoundation.org/certification/how-to-certify/ | 아니오 |
| ref-1434 | OPC Foundation | Overview & Benefits — OPC Foundation Certification | 미확인 | 표준 | medium | 2026-10-11 | https://opcfoundation.org/certification/overview-benefits/ | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-11 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-034 | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 2025-09-08 | 표준 | high | 2026-10-11 | https://reference.opcfoundation.org/specs/OPC-40010-1 | 아니오 |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 | 아니오 |
| ref-1435 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010158171 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04-09 | 벤더 문서 | low | 2026-10-11 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 아니오 |
| ref-1436 | VDMA | Mobile Robots in Production: Mesh-Up 2025 | 미확인 | 업계 보고서 | medium | 2026-10-11 | https://www.vdma.eu/en/mesh-up | 아니오 |
| ref-1437 | Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P. | Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks | 2026-04 | 논문 | medium | 2026-10-11 | https://doi.org/10.1109/WFCS67029.2026.11511549 | 아니오 |
| ref-1438 | TU Dortmund, Communication Networks Institute (ComNets) | Interoperable Teleoperation of Mobile Robots in Intralogistics: Joint Paper Demonstrates End-to-End Network Co-Design for Smart Industries | 2026-04-24 | 정부·연구기관 | medium | 2026-10-11 | https://comnets.etit.tu-dortmund.de/details/interoperable-teleoperation-of-mobile-robots-in-intralogistics-joint-paper-demonstrates-end-to-end-network-co-design-for-smart-industries-63558/ | 아니오 |
| ref-1439 | buildingSMART International | Information Delivery Specification (IDS) | 미확인 | 표준 | high | 2026-10-11 | https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/ | 아니오 |
| ref-1362 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/README.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md | 아니오 |
| ref-1365 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/restrictions.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md | 아니오 |
| ref-1443 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/README.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md | 아니오 |
| ref-1442 | idealworks | VDA 5050 3.0.0 release (March 2026) | 2026-03 | 벤더 문서 | low | 2026-10-11 | https://idealworks.com/en/news/vda5050-300-release-march-2026 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/interoperability-standards-and-conformance.md | 5, 6, 7, 8, 10, 11 | 갱신(차등): 섹션 5 — 본문 수행 자원 칸의 '경로 계산'을 '선 유도 로봇의 경로 계산·안내'로 정정(f3·f5), 자유 주행 로봇의 경로 자체 계획·공유 병기(f4; 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행 연결). 현장 유형 보완: '제조 공장' 사례로 Mesh-Up 2025(f31·f32) — 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히고 매트릭스에서 도입 사례로 세지 않음(f33) / 섹션 6(분리 2026-09-25-area28-s6) — 「적합성 시험과 인증」첫 문단 '제조사가 자체 인증하거나' 정정(f15~f18: 적합성 시험 도구(compliance test tools) 사전 준비는 권고, 인증은 인정 시험소, SDK 응용도 개별 시험; 'CTT' 약어는 쓰지 않음). OTTO 문단에 날짜 2026-04-09·기종 4개·'등' 표기 보강, 각주 원문 미열람 해소(f30, 벤더 주장 유지). 선택 필드·재전송·취소 후 갱신 동작 시험표(f6·f7·f8; 재전송 규칙 자체는 2026-10-09-area41-s6 56행·command-and-task-execution-reliability.md 90행 연결). 근거 수준 구분(f38) / 섹션 7(분리 2026-09-25-area28-s7) — VDA 5050 행: 단일 발행일 미확인 유지, 저장소 명세 표지는 날짜 없음(f1), 날짜 비교는 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」로 연결하고 PDF 표지 'March 2026'은 [추정] 유지(f2), Idealworks 의 2026-02-17 채택 서술은 벤더 문서 추정으로만(f39). 본문 첫 문단 '주문 배정·경로 계산…' 정정(f3·f5). OPC 행 '자체·독립 시험소 인증' → '인정 시험소 인증(시험 도구는 사전 점검용)'(f17). MassRobotics 행 '(원문 미열람)' 해소와 location 필수 4필드·명령 메시지 부재(f19·f20). 3.0.0 태그 스키마 끝 쉼표 주의사항(f9 사실, 행·열 번호는 싣지 않음; 출처는 태그 파일 ref-1430~ref-1432 와 main 파일 ref-413, f12). OPC UA Robotics 서버 Facet 표 124~127(f21·f22). 국내 표준: KS B 7321-2·KS B ISO 22166-202 는 국가표준 목록 번호·제목만(f24·f25), 제정일·부합화는 미확인(f26). 트랙 반영 제안 2026-10-09-26(건축 도면 자동 인식 단계 2, IDS 1.0 → 7절) 처리: IDS 1.0 공식 표준(2024-06-01)·명세/적용 대상/요구 구조·패싯 여섯 종류·값 제한 네 종류·구현 검증용 시험 파일 묶음을 'BIM 데이터 교환 요구의 적합성 검사 수단'으로 짧게(f40~f44); 제안 요약의 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 원문 미확인이라 반영하지 않고 다음 실행 후보 / 섹션 8 — vda5050-lab 항목에 v0.2.0 개발자 프리뷰·인증 주장 아님 반영, 각주 '(원문 미열람)' 해소(f13·f14). Wagner 외 WFCS 2026 통신 평가 논문 추가(f34·f36, 적합성 시험과 구별 f37; 원격 조작 표기는 용어집 따름) / 섹션 10 — 42. 분산 시스템·통신·컴퓨팅 구조 연결(f37), 14. 도면·BIM에서 지도 만들기 연결(IDS, f44) / 섹션 11 — oq-005(f1·f2·f39), oq-055(f13~f18·f30·f38), oq-091(f9·f12), oq-026(f24~f26) 부분 근거, 모두 열림 유지. oq-111 은 이번에 새 근거 없음(TTA·KOROS 원문 미확인). 새 질문 2건. 후속 정리(이번 대상 아님): categories/governance-law-and-society/index.md 70행 '경로 계산' 일반화, ref-705 참고문헌 요약의 '자체 인증' 표현, ref-608 발행일 2026-04-09. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- VDA 5050 3.0.0 태그 스키마의 끝 쉼표를 고친 수정본을 연동 시험에 쓸 때 공식 PDF·태그와의 차이를 누가 승인하고 어떤 회귀 시험으로 확인하는가? | 관련 영역: 21. 상호운용 표준·적합성, 57. 자산·소프트웨어 수명주기 관리 | 근거: f9 | 종류: 일반
- VDA 5050 2.x·3.x 판이 섞인 플릿을 실제 현장에서 전환하면서 판별 스키마 차이와 시험 입력을 어떻게 검증했는지 공개한 기록이 있는가? (관련 기존 질문: oq-091) | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 5회 · 신규 출처 14건
- 미확인 항목:
    - VDA 5050 3.0.0 VDA 배포 PDF 표지의 'March 2026' 표기: WebFetch 가 압축 PDF 본문 텍스트를 읽지 못해 대조 불가(103쪽·A4 만 확인) — 출처 항목으로 넣지 않고 f2 에서 [추정] 유지를 제안
    - f9: 끝 쉼표의 정확한 행·열 번호와 main 브랜치 factsheet·visualization 스키마의 수정 여부는 확인하지 않음(main 은 order.schema 만 확인)
    - f24·f25: KSSN 상세 페이지에서 번호·제목만 보여 제정일·부합화(IDT 여부)·고시번호·쪽수 미확인
    - TTAK.KO-10.1295-Part8: 웹 검색에서 찾지 못했고 이전 브리프의 TTA 목록 URL 은 검증에서 HTTP 400 — 출처·finding 에서 뺌
    - KOROS 1148-8:2025 제정일과 TTA 표준과의 관계: 원문 봇 차단으로 미확인 — finding 에서 뺌
    - ISO 21423 단계·범위: iso.org 미열람 — 21번에는 새로 쓰지 않음
    - VDA5050 이슈 #660: 실재 미확인 — 출처에서 뺌
    - Wagner 외 본문의 평가 시나리오(로봇 수·주문 시간·원격 조작 구간)와 향후 과제 문구: 저자 공개본 PDF 텍스트를 읽지 못해 미확인
    - IDS 의 기수(필수·선택·금지), 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례(트랙 반영 제안 요약 항목): 이번에 원문으로 확인하지 못함
    - f39: Idealworks 의 2026-02-17 채택 서술은 VDA 자료로 확인되지 않음
    - VDA·VDMA 공인 적합성 인증 제도의 존재·부재(oq-055)는 확정 못 함
- 범위 경계 위반 의심:
    - f31~f33: Mesh-Up 2025 는 automatica 2025 전시 시연이며 실제 공장 배치가 아님. site_type '제조 공장'은 시연이 겨냥한 현장 유형을 뜻함
    - f34~f37: 무선망·Open RAN 통신 평가는 42. 분산 시스템·통신·컴퓨팅 구조 쪽 내용이라 21번에는 적합성 시험과 구별되는 통신 평가 연구로만 씀
    - f21·f22: OPC UA Robotics 정보모델은 4. 이기종 로봇 등록에서 이미 다루므로 21번에는 Facet·인증 범위 요구만 씀
    - f40~f44: IDS 는 건물 정보 모델 데이터 교환 표준으로 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙 쪽 내용이 많으므로 21번에는 적합성 검사 수단으로만 짧게 씀
- 한계: 재실행 1회차. 반려 사유 1(신규 참고문헌 id 충돌): 직전 실행 2026-10-10-06 이 같은 예약 구간에서 쓴 ref-1424~ref-1428 과 기존 출처 ref-1429(Franke 외)를 피해 신규 출처를 예약 구간 안의 ref-1430~ref-1443 으로 다시 매겼다. VDA 카탈로그는 기존 id ref-1412 을 재사용하고(이전 브리프의 ref-1412 표기 철회), OPC 개요는 ref-1434, Mesh-Up 은 ref-1436, Wagner 외는 ref-1437 로 옮겼다. 이전 브리프의 ref-1424(이슈 #660)·ref-1425(TTA 목록)·ref-1426(KSSN, 이제 ref-1435)·ref-1428·ref-1429 할당은 모두 없앴다. 실행 컨텍스트의 next_ref_id(ref-1412)가 이미 사용 중이라 구간 안 미사용 번호를 썼다 — pipeline/agent_runner.py 의 next_ref_id 계산 확인 필요. (관련 finding: f9·f16·f25·f31·f34) 반려 사유 2(원문 열람 재현 실패): ref-1412 PDF 는 이번에도 텍스트를 읽지 못해 출처에서 빼고 f1 을 저장소 마크다운 표지 사실로 바꿨다(관련 finding: f1·f2). KSSN 두 페이지는 다시 열었으나 번호·제목만 보여 f24·f25 를 그 범위의 사실로 줄이고 f26 은 열린 질문 유지 의견으로 바꿨다. TTA 목록은 웹 검색으로도 확인 못 해 f28 을 지웠다. Wagner 외는 PDF 텍스트를 읽지 못해 f35 를 지우고, f36 은 연구실 소개문(ref-1438)으로 확인한 가상 무선·실제 무선 구분만 남겼다. f10(파서별 행·열 번호)은 재현 근거가 없어 지웠다. 이번에 fetched: true 로 적은 출처는 모두 이번 실행에서 WebFetch 또는 raw 경로로 다시 열었고(ref-031 은 입력 원문 텍스트 + 3.0.0 태그 raw), fetch_url 이 다른 경우 적었다. 반려 사유 3(미확인 출처·전언 finding): ref-1424(이슈 #660)를 출처에서 빼고 f11·f23·f27 을 지웠으며, ref-159·ref-710 은 근거 finding 이 없어 sources 에서 뺐다. f29 는 지웠다(oq-111 열림 유지). 반려 사유 4(트랙 반영 제안 미처리): buildingSMART 공식 페이지와 공식 저장소 문서로 IDS 1.0 을 조사해 f40~f44 를 냈고 7절 반영안을 rationale 에 적었다. 제안 요약의 기수·사용자 정의 속성 세트·OBOS 프록시는 확인 못 해 다음 실행 후보로 남긴다. required_fixes 대응: [의견]은 모두 claim 첫머리에 '구축자 의견: '을 붙였다. f9 출처를 확인한 태그 파일별 항목(ref-1430~ref-1432)과 main 파일(ref-413)로 바꾸고 ref-051 은 뺐다. f13 은 'Developer Preview'로 재서술하고 'Synthetic Demo Preview' 인용을 없앴다. f21 표 번호를 124~127 로 고쳤다. ref-608 발행일을 2026-04-09 로 고쳤다. f31~f33 에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 넣었다. 새 열린 질문 가운데 TTA–KOROS 질문은 뺐고, 2.x·3.x 전환 질문의 근거를 f12 와 oq-091 로 바꿨다. 용어: '원격 조작' 표기, 'CTT' 대신 '적합성 시험 도구(compliance test tools)'. 열린 질문 해결 제안 없음: oq-005 근거 f1·f2·f39, oq-055 근거 f13~f18·f30·f38, oq-091 근거 f9·f12, oq-026 근거 f24~f26 (모두 부분 근거). 검색 5회/30, 신규 출처 14건/15. 재사용 9건(ref-031·ref-032·ref-1412·ref-408·ref-705·ref-230·ref-034·ref-138·ref-608, 모두 이번에 다시 엶). IDS 관련 URL 이 트랙 실행에서 이미 등록됐다면 퍼블리셔가 같은 URL 로 합쳐야 한다(참고문헌 목록 요약본에 없어 확인 못 함). 교차 확인 0건(VDA 계열 자료, 같은 저장소 파일, OPC 두 페이지는 각각 같은 기관). 정정 요청 없음. 용어 후보 없음(정보 전달 명세·적합성 시험·원격 조작은 용어집에 있음).
```

### runs/2026-09-25-56/research.md

```markdown
# 리서치 브리프 2026-09-25-56

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-56 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 22. 시뮬레이션·예측용 디지털 트윈 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(디지털 모델·섀도·트윈 구분, 8. 실시간 세계 상태·데이터 일관성과의 경계)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음(트랙 floorplan-recognition 반영 제안 1건: Sommer 외 2023, ref-241)
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 0건)

## 조사 질문

1. 성수기 주문량이 늘면 어디가 먼저 막힐까? [분류원문]
2. 디지털 트윈·시뮬레이션의 정의와 표준(ISO 23247, KS X ISO 23247)은 무엇이며, 디지털 모델·디지털 섀도·디지털 트윈 구분으로 8. 실시간 세계 상태·데이터 일관성과 어떻게 경계를 긋는가? (섹션 3·4·7 겨냥)
3. 물류센터 로봇 운영 정책·배치·수요 변화의 효과를 예측하는 대표 접근법(이산 사건 시뮬레이션, 물리 기반 로봇 시뮬레이터, 데이터 기반 모델 생성)은 무엇인가? (섹션 6 겨냥)
4. 오픈소스 도구(Open-RMF 시뮬레이션, RAWSim-O, OFacT)는 무엇을 재현하고 어떤 결정을 실험하게 하는가? (섹션 7 겨냥)
5. 시뮬레이션 모델의 검증·타당성 확인 방법과 실데이터 검증 부족 문제는 연구에서 어떻게 다뤄지는가? (섹션 8·11 겨냥)
6. ROP 가 직접 맡을 시뮬레이션 범위와 외부에 맡길 범위(센서·물리 시뮬레이션, 로봇 로컬 주행, 수요예측)는 어떻게 나뉘는가? (섹션 9·10 겨냥)
7. 국내 물류센터 디지털 트윈 사례와 트랙 floorplan-recognition 반영 제안(스캔·객체 인식 기반 계획용 트윈, Sommer 외 2023)은 무엇을 보여 주는가? (섹션 5·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO 23247(제조를 위한 디지털 트윈 프레임워크)은 국내에 KS X ISO 23247 로 부합화되어 있으며 제1부 개요 및 일반 원리, 제2부 참조 구조, 제4부 정보 교환 등 부로 나뉜다. | ref-659 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | ISO 는 2026년에 ISO 23247-5(디지털 트윈을 위한 디지털 스레드)와 ISO 23247-6(디지털 트윈 결합)을 발간했고, 국가기술표준원은 2026-07-28 이 두 표준이 한국(ETRI) 제안으로 발간되었다고 알렸다. | ref-661, ref-662 | 예 | medium | 2026-07-28 | — | 원문 미열람 |
| f3 | [사실] | ISO 23247-6 은 목적에 따라 여러 디지털 트윈을 골라 결합하는 방법을 정해, 제품·설비·공정의 개별 트윈을 묶어 생산 라인·공장 전체의 복합 트윈을 구성하게 한다. | ref-661, ref-662 | 아니오 | medium | 2026-07-28 | — | 원문 미열람 |
| f4 | [사실] | NIST 의 제조용 디지털 트윈 과제는 디지털 트윈을 신뢰할 수 있고 상호운용 가능하게 만드는 측정 과학과 표준 개발을 목표로 둔다. | ref-660 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f5 | [사실] | Kritzinger 외(2018)는 제조 분야 문헌을 디지털 모델·디지털 섀도·디지털 트윈으로 구분해 분류했고, 가장 높은 단계인 디지털 트윈을 다룬 문헌은 드물고 모델·섀도 문헌이 더 많다고 보고했다. | ref-291 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f6 | [의견] | 분류 원문의 구분(8. 실시간 세계 상태·데이터 일관성은 현재 상태 표현, 22. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험)에 문헌의 모델·섀도·트윈 구분을 맞추면, '디지털 트윈'이라는 이름이 실시간 동기화 수준을 가리키는 경우와 시나리오 실험 기능을 가리키는 경우가 섞여 쓰이므로 이 위키는 용도(현재 표현/미래 실험)로 나눠 적는 것이 맞아 보인다. | ref-291, ref-664 | 아니오 | low | 2020 | — | 원문 미열람 |
| f7 | [사실] | Agalianos 외(2020)는 물류 4.0 에서 이산 사건 시뮬레이션(DES)이 사물인터넷 장치의 실시간 데이터를 질의하며 디지털 트윈의 한 부분으로 진화하고, 이를 통해 창고 계획·관리·의사결정을 지원한다고 정리했다. | ref-664 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f8 | [사실] | Le·Fan(2024)의 물류·공급망 디지털 트윈 문헌 검토는 실제 데이터로 검증한 논문은 소수이고 대다수가 생성 데이터를 쓴다고 보고해, 실무 적용의 부족을 지적했다. | ref-665 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f9 | [사실] | Le·Fan(2024)은 COVID-19 이후 공급망 위험·교란 관리에서 디지털 트윈의 이점이 뚜렷해졌다고 보고, 물류·공급망 디지털 트윈 개념 틀을 제안했다. | ref-665 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f10 | [사실] | Coelho 외(2021)는 Simio 로 만든 사내 물류 시뮬레이션 의사결정 지원 도구를 제안하고, 이 모델이 현실을 대표하여 실제 운영을 방해하지 않고 개선안을 시험하는 디지털 트윈화 도구로 쓰일 수 있다고 보고했다. | ref-666 | 아니오 | medium | 2021 | — | 원문 미열람 |
| f11 | [사실] | Open-RMF 문서는 Gazebo·Ignition 물리 시뮬레이터를 ROS 2 와 연결해 시뮬레이션에 쓴 코드를 수정 없이 실제 시스템에서도 실행하고, 시나리오 반복·예외 상황 탐색·장시간 검증을 현장 배치 전에 할 수 있다고 설명한다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [사실] | Open-RMF 의 building_map_generator 는 traffic_editor 로 주석한 .building.yaml 에서 Gazebo·Ignition 월드(바닥·벽 메시)와 플릿 어댑터용 주행 그래프를 함께 생성하므로, 레이아웃이 바뀌면 주석을 고쳐 시뮬레이션 월드를 다시 만들 수 있다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [사실] | Open-RMF 시뮬레이션은 로봇용 slotcar 플러그인(레일식 주행과 가감속), 문·승강기 플러그인, 작업셀 적재·하역을 흉내 내는 TeleportDispenser·TeleportIngestor, Menge 기반 보행자 군중 시뮬레이션(CrowdSim), 배터리·충전기 동작 전환 도구를 제공한다. | ref-406, ref-668 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f14 | [추정] | 연계 대상: Open-RMF 시뮬레이션의 로봇 모델은 레일식 주행을 흉내 내는 단순화 모델이므로, 센서 인식·로컬 회피 같은 로봇 자체 거동의 충실도는 제조사·물리 시뮬레이터 쪽에 맡기고 ROP 시뮬레이션은 플릿 조율·설비 상호작용을 실험하는 데 초점이 맞는 것으로 보인다. | ref-406, ref-668 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [사실] | rmf_simulation 저장소는 Gazebo Classic 11(지원 2025년 1월 종료)과 Gazebo Fortress 를 지원 대상으로 적어, 시뮬레이션 환경도 시뮬레이터 판 교체에 따른 수명주기 관리가 필요하다. | ref-668 | 아니오 | medium | 2026-09-25 | — | — |
| f16 | [사실] | RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS)의 이산 사건 시뮬레이션 프레임워크로, 운영 중 생기는 여러 결정 문제의 효과를 연구하고 새 결정 방법을 끼워 넣을 수 있게 하며 2D·3D 화면과 로봇 위치 히트맵을 제공한다(C#, GPL v3). | ref-101 | 아니오 | medium | 2026-09-25 | 피킹 | — |
| f17 | [사실] | Merschformann 외(2019)의 RMFS 결정 규칙 연구는 이산 사건 시뮬레이션으로 배정 규칙을 가정한 미래에서 실험했고, 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-398 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f18 | [사실] | 국내 연구로 시뮬레이션과 메타모델을 결합해 자동물류센터 설계를 최적화한 연구가 있다. | ref-402 | 아니오 | medium | 2006 | — | 원문 미열람 |
| f19 | [사실] | 다중 AGV 시스템의 경로망을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있어, 경로망 배치안 평가가 시뮬레이션으로 이루어진다. | ref-267 | 아니오 | medium | 2024 | 제약 | 원문 미열람 |
| f20 | [사실] | OFacT(Open Factory Twin)는 Fraunhofer ISST 등이 개발한 생산·물류용 오픈소스 디지털 트윈 프레임워크로, 주문·자원·부품·공정으로 공장 상태를 기술하는 상태 모델, 주문·자원 에이전트 제어, 일관성 검사를 포함한 데이터 통합, 시나리오 평가·예측용 시뮬레이션, KPI 비교 계획 서비스를 갖춘다(Apache 2.0). | ref-670 | 아니오 | medium | 2026-09-25 | — | — |
| f21 | [추정] | OFacT 가 현재 상태를 담는 상태 모델·데이터 통합과 시나리오를 돌리는 시뮬레이션·계획 서비스를 별도 구성요소로 두는 것은, 8. 실시간 세계 상태·데이터 일관성(현재 표현)과 22. 시뮬레이션·예측용 디지털 트윈(미래 실험)을 나누는 분류 원문의 구분과 같은 방향의 설계로 보인다. | ref-670 | 아니오 | low | 2026-09-25 | — | — |
| f22 | [사실] | Sargent 의 시뮬레이션 모델 검증·타당성 확인(V&V) 틀은 개념 모델 타당성, 모델 검증, 운영 타당성, 데이터 타당성을 나누어 확인하고 결과 문서화와 모델 인가(accreditation)를 다룬다. | ref-671 | 아니오 | medium | 2008 | — | 원문 미열람 |
| f23 | [추정] | CJ대한통운은 2021년 11월 현실 물류센터와 같은 가상 물류센터를 구축해 작업 동선·재고 배치·설비 효율을 최적화하고 장비 고장·피킹 오류·상품 파손 원인을 사전에 파악하며, AI 가 시나리오를 학습해 몇 시간 걸릴 일을 수초~수분에 해결한다고 발표했다. | ref-672 | 아니오 | low | 2021-11 | 피킹 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f24 | [추정] | NVIDIA 는 'Mega' Omniverse 블루프린트를 공장·창고 디지털 트윈에서 로봇 플릿과 물리 AI 를 배치 전에 개발·시험·최적화하는 참조 작업 흐름(센서 시뮬레이션·합성 데이터 생성 결합)으로 소개하고, KION·Accenture 가 창고·유통 공정 최적화에 쓴다고 밝혔다. | ref-673 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f25 | [추정] | 분류 원문 질문 '성수기 주문량이 늘면 어디가 먼저 막힐까?'에 대해, 확인한 DES 연구·도구는 주문 도착량과 배정 규칙·자원 수(로봇·작업대)를 바꿔 처리량과 대기를 비교하는 방식으로 답하며, ROP 오케스트레이션 정책 자체를 성수기 시나리오로 시험한 공개 물류센터 사례는 이번 조사에서 찾지 못했다. | ref-398, ref-101, ref-666, ref-664 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f26 | [사실] | Sommer 외(2023)는 레이저 스캔과 객체 인식으로 공장의 건조 환경(built environment) 디지털 트윈을 자동 생성해 생산 계획의 입력으로 쓰는 방법을 제안했다. | ref-241 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f27 | [추정] | Sommer 외(2023)의 트윈은 생산 계획을 위한 배치·공간 모델이므로 22. 시뮬레이션·예측용 디지털 트윈의 초기 모델 생성(계획용)에 해당하고, 운영 중 현재 상태를 동기화하는 8. 실시간 세계 상태·데이터 일관성과는 구분되는 것으로 보인다. | ref-241, ref-406 | 아니오 | low | 2023 | — | — |
| f28 | [추정] | ROP 가 직접 맡을 시뮬레이션 몫은 자신의 작업 배정·교통·충전 정책과 설비 요청(문·승강기)을 시뮬레이션된 플릿·설비에 대해 그대로 실행해 보는 것으로 보이며, Open-RMF 처럼 같은 코드를 시뮬레이션과 실제에 쓰는 구조가 그 근거가 된다. | ref-406, ref-668 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f29 | [추정] | 연계 대상: 센서 시뮬레이션·합성 데이터 생성·물리 기반 로봇 거동 재현은 시뮬레이터 제공자와 로봇 제조사 영역이고, 시나리오의 주문·물동량 전망은 상위 업무 시스템의 수요예측에서 받는 입력으로 보인다. | ref-673, ref-665 | 아니오 | low | 2026-09-25 | 시작 조건 | 원문 미열람 |
| f30 | [의견] | Open-RMF 시뮬레이션이 강조하는 시나리오 반복·예외 상황 탐색은 23. 시험·형식 검증·벤치마크의 회귀·장애 시험과 환경을 공유하므로, 22. 시뮬레이션·예측용 디지털 트윈은 운영 정책·수요 변화의 효과 예측, 23. 시험·형식 검증·벤치마크는 변경 후 동작 확인이라는 목적으로 나누는 것이 분류 원문 정의에 맞아 보인다. | ref-406 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-659 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 예 |
| ref-660 | NIST | Digital Twins for Advanced Manufacturing | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing | 예 |
| ref-661 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/87426.html | 예 |
| ref-662 | 머니투데이 | 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간 | 2026-07-28 | 기사 | medium | 2026-09-25 | https://www.mt.co.kr/economy/2026/07/28/2026072809211448284 | 예 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-664 | Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G. | Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics | 2020 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2351978920320990 | 예 |
| ref-665 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 예 |
| ref-666 | Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P. | Simulation-based decision support tool for in-house logistics: the basis for a digital twin | 2021 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646 | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-668 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_simulation | 아니오 |
| ref-101 | Merschformann, M. (merschformann GitHub) | RAWSim-O — A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/merschformann/RAWSim-O | 아니오 |
| ref-670 | OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) | ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/OpenFactoryTwin/ofact | 아니오 |
| ref-671 | Sargent, R. G. | Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation) | 2008 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/abs/10.5555/1516744.1516780 | 예 |
| ref-672 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 2021-11 | 벤더 문서 | low | 2026-09-25 | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 | 예 |
| ref-673 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 미확인 | 벤더 문서 | low | 2026-09-25 | https://blogs.nvidia.com/blog/mega-omniverse-blueprint | 예 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | 논문 | medium | 2026-09-25 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f7·f9·f10·f11(배치 전 반복 시험·운영 방해 없는 개선안 시험), f8(실데이터 검증 부족) / 4절 핵심 개념: f5(디지털 모델·섀도·트윈), f6 의견·f21 추정(8. 실시간 세계 상태·데이터 일관성과의 구분: 현재 표현 vs 가정한 미래 실험), f3(디지털 트윈 결합) / 5절 현장 시나리오: f25(피킹·제약, 분류 원문 질문 — 추정), f17(피킹·예외·성과), f23(국내 사례, 벤더 주장 병기) / 6절 대표 접근법: f7(DES 와 실시간 데이터), f10(DES 의사결정 지원), f11·f13(물리 시뮬레이터·플러그인), f12·f26·f27(평면도·스캔에서 초기 모델 생성), f24(벤더 주장) / 7절 표준·오픈소스: f1·f2·f3·f4(ISO 23247·KS X ISO 23247·NIST), f11~f13·f15(Open-RMF 시뮬레이션), f16(RAWSim-O), f20(OFacT) / 8절 대표 연구: f5·f7·f8·f9·f10·f17·f18·f19·f22, 트랙 floorplan-recognition 단계 1 반영 제안(2026-09-25-19) 검토 결과 f26(사실)·f27(추정, 계획용 트윈이므로 8. 실시간 세계 상태·데이터 일관성과 구분) / 9절 경계: f28(ROP 직접: 자기 정책을 시뮬레이션된 플릿·설비에 실행), f14·f29('연계 대상': 로봇 자체 거동·센서 시뮬레이션·수요예측) / 10절 연결: 8. 실시간 세계 상태·데이터 일관성(f6·f21), 23. 시험·형식 검증·벤치마크(f30), 24. 자산·소프트웨어 수명주기 관리(f15), 21. 온보딩·설정·현장 시운전과 6. 지도·공간·위치 모델(f12·f26), 13. 작업 배정 — MRTA·15. 다중 로봇 경로·교통 관리 — MAPF(f17·f19), 27. AI·학습·적응과 모델 운영(f23·f24 벤더 주장, 학습 환경으로서 트윈), 28. 표준·상호운용성·다사업자 거버넌스(f1~f3), 20. 예외 복구·재계획·업무 연속성(f9) / 11절 열린 질문: open_questions_new 3건과 f25 의 미확인 사항. 벤더 주장 f23·f24 는 [추정]+'벤더 주장' 병기. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 디지털 스레드 | Digital Thread | 제품 수명주기 전반의 설계·생산·운영 데이터를 연결해 디지털 트윈을 만들고 유지하게 하는 데이터 연결 체계로, ISO 23247-5 가 제조 디지털 트윈용 틀을 정한다. |
| 디지털 트윈 결합 | Digital Twin Composition | 제품·설비·공정의 개별 디지털 트윈을 목적에 맞게 골라 묶어 라인·공장 단위의 복합 트윈을 만드는 방법으로, ISO 23247-6 이 다룬다. |
| 시뮬레이션 모델 검증·타당성 확인 | Verification and Validation (V&V) of Simulation Models | 시뮬레이션 모델이 설계대로 구현되었는지(검증)와 목적에 비추어 현실을 충분히 대표하는지(타당성 확인)를 개념 모델·운영·데이터 측면에서 확인하는 절차다. |

## 열린 질문

새로 생긴 질문:

- 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 4. 성과·경제성·프로세스 개선 | 근거: f8 | 종류: 일반
- 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f3 | 종류: 일반
- 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 9. 로봇·제조사 관제 연동 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 1
- 예산 사용량: 검색 23회 · 신규 출처 15건
- 미확인 항목:
    - f1: KS X ISO 23247 제3부 목록과 각 부의 KS 제정일 미확인
    - f2·f3: ISO 23247-6 본문 미열람, 결합 방법 설명은 기사 요약 중심
    - f4: NIST 과제 페이지 원문 미열람, 발행일 미확인
    - f22: Sargent 논문의 정확한 판(2008 WSC 외 여러 판 존재) 원문 미확인
    - f23·f24: 벤더 주장, 독립 출처로 효과 수치 확인 못 함
    - f25: ROP 정책을 성수기 시나리오로 시험한 공개 물류센터 사례 찾지 못함
    - ref-241: 참고문헌 목록의 기존 값을 입력으로 받지 못해 검색 결과로 기관·제목·URL 을 채움(퍼블리셔 대조 필요)
    - ref-673 발행일 미확인
- 범위 경계 위반 의심:
    - f14·f29: 센서 인식·로컬 주행·센서 시뮬레이션과 수요예측은 분류 원문 9장 외부 연계 영역이므로 '연계 대상:'으로 표시
    - f24: 물리 AI 학습·센서 시뮬레이션은 ROP 직접 범위가 아님(벤더 주장으로만 서술)
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처는 ref-406(Open-RMF 시뮬레이션 장, 미러 목록 경로), ref-668(rmf_simulation), ref-101(RAWSim-O), ref-670(OFacT) 4건이며 나머지는 검색 요약 기준(신뢰도 상한 medium). 검색 23회/30, 신규 출처 15건/15(ref-659~ref-673, 예약 구간 안) — 신규 출처 예산에 도달해 ISO 23247-1 정의 원문, 물류 디지털 트윈 대규모 사례(Ashrafian·Pedersen 2023), 데이터 기반 시뮬레이션 모델 자동 생성 검토 논문은 출처로 넣지 않음. 재사용 4건: ref-398·ref-402·ref-267(2026-09-25-55 브리프 값 사용), ref-241(입력에 참고문헌 목록 값이 없어 검색으로 확인한 값으로 기재). 트랙 반영 제안 1건(2026-09-25-19, floorplan-recognition 단계 1, 8절)은 f26(사실)·f27(추정)으로 조사해 반영을 제안. 교차 확인은 f2 1건뿐. 한국 자료: KS X ISO 23247(ref-659), 국표원 발표 기사(ref-662), 국내 연구(ref-402), CJ대한통운 보도자료(ref-672, 벤더 주장). 한국어 검색에서 나온 업체 블로그는 출처로 쓰지 않음. 27. AI·학습·적응과 모델 운영 연결은 f23·f24 벤더 주장뿐이라 교차 규칙 대상(5·21·6·13·19)에 직접 해당하는 근거는 없음. 정정 요청 없음, 대상 영역 열린 질문 0건, 해결 제안 없음.
```

### data/source_texts/ref-023.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
## Workcells

Currently RMF has 2 types of sample workcells, namely: `Dispenser` and `Ingestor`.

| Message Types | ROS2 Topic | Description |
|---------------|------------|-------------|
| `rmf_dispenser_msgs/DispenserRequest` | `/dispenser_reqeusts` | Direct requests subscribed by the dispenser node |
| `rmf_dispenser_msgs/DispenserResult` | `/dispenser_results` |  Result of a dispenser request, published by the dispenser  |
| `rmf_dispenser_msgs/DispenserState` | `/dispenser_states` |  State of the dispenser published by the dispenser periodically |
| `rmf_ingestor_msgs/IngestorRequest` | `/ingestor_requests` |  Direct requests subscribed by the ingestor node |
| `rmf_ingestor_msgs/IngestorResult` | `/ingestor_results` |  Result of a ingestor request, published by the ingestor |
| `rmf_ingestor_msgs/IngestorState` | `/ingestor_states` |  State of the dispenser published by the ingestor periodically |

In `rmf_demos` world, both `TeleportDispenser` and `TeleportIngestor`
[plugins](https://github.com/open-rmf/rmf_simulation/tree/main/rmf_robot_sim_gz_plugins/src) act as workcell adapter nodes.

Workcells currently work alongside with Delivery Task. In `fleet_adapter.lauch.xml`,
`perform_deliveries` needs to be `true` for the robot to accept a delivery task.

A Full Delivery:
1) The robot will first move to the `pickup_waypoint`
2) Requests a `DispenserRequest` till receives a `DispenserResult`. (Done Dispensing)
3) Continue delivery and moves to `dropoff_waypoint`
4) Requests a `IngestorRequest` till receives a `IngestorResult`. (Done Ingesting)
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
…(발췌: 전체 207,642자 중 앞 14,754자)
```

### data/source_texts/ref-047.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
builtin_interfaces/Time time

# A unique ID for this request
string request_guid

# The unique name of the dispenser that this request is aimed at
string target_guid

# below are custom workcell message fields
string transporter_type
DispenserRequestItem[] items
```

### data/source_texts/ref-049.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
builtin_interfaces/Time time

# A unique ID for the request which this result is for
string request_guid

# The unique ID of the workcell that this result was sent from
string source_guid

# Different basic result statuses
uint8 status
uint8 ACKNOWLEDGED=0
uint8 SUCCESS=1
uint8 FAILED=2

# below are custom workcell message fields
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

### data/source_texts/ref-312.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
string lift_name
builtin_interfaces/Time request_time

# session_id should be unique at least between different requesters.
# For example, session_id could be the requester's node name.
string session_id

# AGV mode means that the doors are always open when the lift is stopped
# Human mode means that LiftDoorRequest messages must be used to open/close
# the doors explicitly, since they may "time out" and close automatically.
uint8 request_type
uint8 REQUEST_END_SESSION=0
uint8 REQUEST_AGV_MODE=1
uint8 REQUEST_HUMAN_MODE=2

# The destination_floor must be one of the values returned in a LiftState.
string destination_floor

# Explicit door requests are necessary in "human" mode to open/close doors.
# Door requests are not necessary in "AGV" mode, when the doors are always
# held open when the lift cabin is stopped.
uint8 door_state
uint8 DOOR_CLOSED=0
uint8 DOOR_OPEN=2
```

### data/source_texts/ref-313.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# The DoorMode message captures the "mode" of an automatic door controller.
# Most door controllers default to running in "closed" mode, and transition
# through some sort of "moving" mode until reaching the "open" mode.

uint32 value

# "value" must be one of the following enumerations:
uint32 MODE_CLOSED=0
uint32 MODE_MOVING=1
uint32 MODE_OPEN=2
uint32 MODE_OFFLINE=3
uint32 MODE_UNKNOWN=4
```
