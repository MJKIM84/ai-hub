(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-10-06
- date: 2026-10-10
- run_type: update (갱신)
- 대상: 20. 로봇·제조사 관제 연동 (F. 연동)
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

### runs/2026-10-10-06/target.json

```json
{
  "run_id": "2026-10-10-06",
  "date": "2026-10-10",
  "weekday": "Sat",
  "run_number": 166,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 20,
    "area_name": "20. 로봇·제조사 관제 연동",
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
  "selection_rationale": "CLI 지정 run_type=update, area=20"
}
```

### runs/2026-10-10-06/research.json

```json
{
  "run_id": "2026-10-10-06",
  "date": "2026-10-10",
  "run_type": "update",
  "target": {
    "area_no": 20,
    "area_name": "20. 로봇·제조사 관제 연동",
    "category": "F. 연동"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 — IO-AMRs 과제 문장(ref-258)이 원문 미열람이고 주관 기관·과제 단계(계획인지 완료인지)가 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 출하 시나리오 하나뿐이고 '수행 자원' 행이 추정이며 직접 제어·위임 비교 자료 없음(oq-031). 연동 위치와 제어 수준을 나눠 보는 기준, 상업 시설·전시 시연 사례 없음",
    "섹션 6. 대표 접근법과 기술 — 연결 단절 시 실행 의미와 상태 분리, 신호등 수준 연동의 정지 시간 전제·교착 시 사람 개입(oq-032), 상태·오류 변환의 실제 필드 매핑 사례(oq-033) 근거가 약함",
    "섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 3.0.0 발행일 미확인(oq-005), 공개 구현(free_fleet·ros_amr_interop·vda-5050-lib.js)의 판별 지원 범위와 Open-RMF 구역 기능의 개발 상태 미반영",
    "섹션 8. 대표 연구와 자료 — Lopes 외 논문(ref-136) 저자 미확인·120 ms 지표 명칭과 측정 조건 미확인, Franke 외(ref-1429) 원문 미열람·워크숍 구성 미기재",
    "섹션 10. 다른 연구영역과의 연결 — 21. 상호운용 표준·적합성(ISO 21423 단계), 47. AI·학습·적응과 모델 운영(MCP 연동)과의 연결 없음",
    "섹션 11. 열린 질문 — oq-005·oq-031·oq-032·oq-033 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]",
    "oq-005 VDA 5050 3.0.0 의 발행일은 공식 자료에서 무엇으로 표시되는가? (섹션 7·11 겨냥)",
    "oq-032 제조사 관제가 일시정지·재개만 허용하는 신호등 수준 연동에서 정지·교착 처리의 전제는 무엇인가? (섹션 6·11 겨냥)",
    "oq-033 공개 구현은 로봇 상태·오류를 표준 필드로 어떻게 옮기는가? (섹션 6·11 겨냥)",
    "oq-031 직접 제어와 제조사 관제 위임을 고르는 기준이나 비교 자료가 있는가? (섹션 5·11 겨냥)",
    "기존 8절·3절 연구 자료(Lopes 외, Franke 외, IO-AMRs)의 서지·측정 조건·단계는 원문에서 무엇으로 확인되는가? (섹션 3·8 겨냥)",
    "VDA 5050·Open-RMF 공개 구현의 판별 지원 범위와 개발 중 기능은 무엇인가? (섹션 7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA 보도자료 'Version 3.0 of VDA 5050 released'의 본문 날짜는 2026-04-20(Berlin, April 20, 2026)이며, 보도자료 URL 은 260421 계열이다.",
      "tag": "사실",
      "source_ids": [
        "ref-032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료 제목 아래 \"Berlin\" · \"April 20, 2026\". URL 경로 260421_PM_VDA_5050_EN 의 숫자를 본문 날짜로 대체하지 않음. oq-005 관련",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목은 날짜를 2026-03-17(March 17, 2026)로 표시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "카탈로그 제목 'VDA 5050' 아래 \"March 17, 2026\", VDA-Recommendations PDF 3,38 MB, 'VDA 5050 Version 3.0.0 Mobile Robot Communication Interface'. 카탈로그 표시일이 문서 발행일인지는 페이지에 설명 없음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "VDA 가 배포하는 VDA 5050 3.0.0 공식 PDF 의 표지는 판 표기를 'Version 3.0.0, March 2026'으로 적어 월 단위(2026-03)까지만 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공식 PDF(https://www.vda.de/dam/jcr%3A09f03b91-13e2-4db3-bf30-4f221710071b/VDA5050-V3.0.0-2025-03.pdf) 표지 \"Version 3.0.0, March 2026\". 파일 이름의 2025 는 발행연도로 쓰지 않음. ref-031 과 같은 명세의 PDF 판",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 의 공식 자료 세 가지가 VDA 5050 3.0.0 의 날짜를 서로 다르게 표시한다: 카탈로그 2026-03-17, 보도자료 본문 2026-04-20, 명세 표지 2026-03.",
      "tag": "사실",
      "source_ids": [
        "ref-1423",
        "ref-032",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f1·f2·f3 의 원문 표시를 나란히 둔 것. 세 자료 모두 VDA 계열이라 독립 교차 확인이 아니다. 일자 차이의 원인(업무 단계)은 어느 자료에도 설명이 없다",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "VDA 5050 3.0.0 의 발행일은 하나로 확정하지 않고 서지에는 판 표기의 월(2026-03)을 적으며, 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)는 주석으로 함께 남기는 것이 맞아 보인다(oq-005 부분 답변).",
      "tag": "의견",
      "source_ids": [
        "ref-031",
        "ref-032",
        "ref-1423"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4 에서 도출. 저장소 릴리스 설명에 있다는 2026-03-19 와 게시 시각은 이번 환경에서 원문을 확인하지 못해 근거로 쓰지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 §4.1 은 로봇이 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4.1 Connection handling, security and QoS: \"it keeps all the order information and fulfills the order up to the last released node\". 대분류 F 개요(42↔32 연결)에 같은 번역어 '마지막으로 해제된 노드'로 이미 있음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 은 주문에 딸린 동작·즉시 동작·구역 동작의 상태를 상태 메시지의 actionStates·instantActionStates·zoneActionStates 세 배열로 나눠 보고하게 하며, 구역 동작의 예정 상태 보고는 선택 사항이다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.6.9 Action states, §7.8 state 메시지 표. actionStates 는 새 주문 수락 시 비우고, instantActionStates·zoneActionStates 는 clearInstantActions·clearZoneActions 실행 때까지 유지(목록이 길면 *_STATES_FULL 오류 가능). 구역 동작 지원 시 zoneActionStates 필수",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "로봇이 단절 중에도 해제된 노드까지 주행을 이어 가므로(f6) ROP 어댑터는 연결 단절(connection 상태)을 곧 정지로 해석하지 말고, 연결 상태와 동작 실패(동작 상태 배열의 FAILED)를 별도 상태로 보존해 단절 시 실행 의미와 상태를 분리하는 것이 좋아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f7 에서 도출한 설계 판단. 단절 뒤 복구 절차는 32. 예외 복구·재계획·업무 연속성 연결로 한정. 명세 3.0.0 범위",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Open-RMF EasyTrafficLight API(rmf_fleet_adapter 2.14.0)의 moving_from() 경고는 로봇이 다음 체크포인트에서 멈출 시간이 있을 때만, 곧 정지 명령의 통신 지연과 로봇 최대 감속을 감안해 호출하라고 하며, 이를 어기면 MovingError·WaitingError 가 나고 교통 흐름이 끊기거나 교착될 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1424"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EasyTrafficLight.hpp \\warning: \"accounting for the network latency of sending out the stop command and the maximum deceleration of the robot\". API 계약의 전제이며 실험 수치가 아님",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "같은 헤더의 Blocker 설명은 해결할 수 없는 충돌로 교착이 생기면 RMF 교통 협상 시스템이 충돌 참여자를 충분히 제어하지 못하므로 사람 개입이 필요할 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1424"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "deadlock_callback 에 넘기는 Blocker 클래스 주석: \"Human intervention may be required at this point, because the RMF traffic negotiation system does not have a high enough level of control\"",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "신호등 수준으로 붙는 제조사 플릿의 연동 계약에는 정지 명령의 유무만이 아니라 정지 가능 시간(통신 지연·최대 감속)과 정지 확인 응답, 교착 시 사람 개입 경로를 함께 적는 것이 좋아 보이며, 제어 수준별 교통 성능을 같은 조건에서 비교한 자료는 여전히 찾지 못했다(oq-032 부분 근거).",
      "tag": "의견",
      "source_ids": [
        "ref-1424"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9·f10 에서 도출. 단일 프로젝트 API 문서 근거이며 제한 제어가 모든 교착을 해결한다는 보장으로 넓히지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "신호등 연동을 평가·재현할 때는 쓰는 rmf_fleet_adapter 패키지 판을 함께 기록하는 것이 좋아 보인다. 2.14.0(2026-09-26) 변경 이력에 EasyTrafficLight 의 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 들어 있기 때문이다.",
      "tag": "의견",
      "source_ids": [
        "ref-1398"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "CHANGELOG 2.14.0: \"Fix EasyTrafficLight publish fleet state\"(#525), \"Fix cumulative delay calculation in EasyTrafficLight\"(#524). 이 수정 사실은 27. 다중 로봇 경로·교통 관리 — MAPF 주제 페이지에 이미 있어 영역 20 에는 평가 관점만 더함. 수정 이력은 성능 향상을 증명하지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "InOrbit 개발자 문서는 InOrbit 이 제어하는 로봇 플릿을 RMF core 에 잇는 오픈소스 전체 제어(full control) 플릿 어댑터를 제공해 여러 제조사 로봇의 중앙 교통 조정을 가능하게 한다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1029"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Open-RMF 절 \"InOrbit provides an open source full control fleet adapter for RMF\". 제조사 관제 API 경유 전체 제어 조건은 5절 '제약' 행(ref-251)에 이미 있어 보강 근거로만 씀 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "연동 위치(제조사 관제 API 를 거치는지, 로봇에 직접 붙는지)와 제어 수준(전체 제어인지)은 따로 판단해 별도 항목으로 기록하고, 제어 권한은 경로 지정·교체, 정지, 진행 상태 반환으로 나눠 적는 것이 좋아 보인다(oq-031 판단 기준 보강).",
      "tag": "의견",
      "source_ids": [
        "ref-251",
        "ref-1029"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Open-RMF 책은 전체 제어 조건을 '제조사 관제가 명시 경로를 지정·중단·교체할 수 있고 위치를 갱신'으로 둠(\"fleet manager allows us to specify explicit paths\"). InOrbit 문서는 관제 플랫폼 경유 전체 제어 어댑터를 밝힘. 국내 물류센터 비중·비용·처리량 비교는 미확인",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Lopes 외(Applied Sciences 2025, 15(13), 7235, 2025-06-27) 논문은 본문 §6.2 에서 로봇 상태의 평균 갱신 간격(average update interval)을 약 120 ms, 사용자 화면 지연을 1초 미만으로 보고하며, 초록은 같은 값을 'average latency'로 표현한다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "p.21 §6.2 \"The average update interval for the robot status was approximately 120 ms\". p.1 초록 \"average latency of 120 ms\". 측정 지점·타임스탬프 정의는 논문에 없음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "같은 논문은 실험 시험 중 AMR·AGV 를 포함해 최대 20대를 화면·서버 성능의 큰 저하 없이 동시에 감시할 수 있었고 시험 기간 서버 가동률이 99.5% 이상이었다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "p.21 §6.2 \"simultaneously monitor up to 20 robots, including AMRs ... and AGVs\". 20대의 기종 구성·시험 기간·표본 수는 밝히지 않음. 감시·감독 중심 결과이며 주행 제어 성능이 아님",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "같은 논문의 §5.3(로봇 지도 작성·연결) 시험은 코임브라 공학연구소 기계공학과의 약 500 m² 실험실에서 수행됐으며, 120 ms·20대 결과를 어디서 측정했는지는 논문에 명시돼 있지 않다.",
      "tag": "사실",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "p.12 §5.3 Mapping and Interconnection of Robots: \"within a laboratory covering an area of approximately 500 m2\", 시제품이 설치될 공장 조건을 대략 모사. 기존 위키의 ref-136 저자 '미확인'은 17명 저자로 정정",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "Lopes 외의 결과는 자동차 공장 적용을 목표로 한 실험실 연구의 감시 성능이므로, 자동차 공장의 장기 운영 지연이나 20대 동시 주행 제어 성능으로 인용하지 않고, 기존 '작업 상태 갱신 평균 지연 120 ms' 표현은 '로봇 상태 평균 갱신 간격 약 120 ms'로 고치는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-136"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15~f17 에서 도출. 단일 연구팀 결과이며 독립 재현 미확인",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Franke 외(Logistics Journal: Proceedings No.19, 2023-10-11) 연구는 2023년 봄 소프트웨어 기업 2곳·하드웨어 제조사 3곳·창고 사용자 1곳 등 여섯 회사가 참여한 워크숍으로 VDA 5050 개념에 기반한 새 표준 인터페이스 요구를 수집했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1429"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "p.5 §3.1: \"two software enterprises, three hardware manufacturers and one end-user from warehousing\", \"six participating\", \"in spring 2023\". DOI 10.2195/lj_proc_franke_en_202310_01",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "Franke 외 연구는 연동 요구 분석 자료로 분류하고, 실물 플릿을 비교한 실험이 아니므로 직접 제어와 제조사 관제 위임의 처리량 비교 근거로 쓰지 않는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1429"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f19 에서 도출. 워크숍 기반 요구 수집 연구. 기존 8절의 '주변 설비 인터페이스 미포함' 문장은 반복하지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "ARM Institute 의 IO-AMRs 과제 소개는 주관 기관을 Siemens Technology 로, 협력 기관을 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 로 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-258"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Participants: \"Lead: Siemens Technology\", \"Partners: FedEx, Yaskawa Motoman, Waypoint Robotics, University of Memphis\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "IO-AMRs 과제 소개는 다중 지도 관리자·연결 계층·전역 플릿 관리자를 이전 ARM 지원 과제의 산출물을 활용해 만들 '계획'으로 서술해, 이 과제가 소개 시점에 계획 단계였음을 보여 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-258"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Technical Approach: \"will leverage outputs from a prior ARM-funded project to create a muti-map manager[원문 철자], connectivity layer, and global fleet manager\". 운영자 면담으로 인력·기술 전환 계획도 만든다고 함. 완료일·공개 코드·실물 결과는 페이지에 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "IO-AMRs 소개는 과제 목표의 근거로만 쓰고 달성한 운영 성과의 근거로 쓰지 않으며, 3절의 목표 문장에는 주관 기관과 계획 단계라는 범위만 보태는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-258"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f21·f22 에서 도출. 과제 발주 기관의 1차 자료이나 독립 성능 평가가 아님",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Open-RMF rmf_ros2 PR #516 'Add GoToZone feature'는 구역 이름을 받아 구역 안 경유점을 예약하는 기능을 제안하며 2026-10-10 기준 미병합 상태인 것으로 보이나, 이번 환경에서 PR 원문과 상태를 직접 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모의 PR 설명('zone booking system')·상태 Open·merged_at null 기록에 의존. GitHub API 접근이 막혀 대조 실패",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "Open Robotics Discourse 의 2026-05-04 Interop SIG 공지는 CHART 가 RMF-2.0 프로젝트로 개발한 새 기능을 단계적으로 공개하며 첫 단계가 시설 '구역(zones)' 관리 기능이고, 공지 시점에 이 기능이 검토 중(currently undergoing review)이라고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1426"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공지(2026-05-04 게시, 확인일 2026-10-10): \"this new zone feature which is currently undergoing review\". 발표 예시로 환자 중심 목적지 선택과 승강기 공유를 듦. 2026-07-08 녹화 링크 게시. 병합 여부는 이 공지로 알 수 없음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "어댑터 기능 목록을 정리할 때는 배포판(태그)에 든 기능과 검토 중인 기능(예: Open-RMF 구역 기능)을 구분해 적는 것이 좋아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1426",
        "ref-1425"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f24·f25 에서 도출. CHART 의 하드웨어 시험 주장을 업스트림 배포판 검증으로 바꾸지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "ros_amr_interop 1.1.1 의 MassRobotics 송신 예제 설정은 ROS 토픽 /we_b_robots/mode(std_msgs/String)를 operationalState 에, /troubleshooting/errorcodes 를 errorCodes 에 연결하고, 오류 코드는 쉼표로 구분한 문자열로 받아 MassRobotics 표준이 요구하는 배열로 바꾼다고 주석에 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-255"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "massrobotics_amr_sender_py/params/sample_config.yaml(태그 1.1.1): operationalState.valueFrom.rosTopic, errorCodes.valueFrom.rosTopic, 주석 \"Error codes are expected to be comma-separated strings\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "MassRobotics AMR 상호운용 표준 1.0 태그의 JSON 스키마는 상태 보고(statusReport)의 필수 필드를 uuid·timestamp·operationalState·location 넷으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AMR_Interop_Standard.json(태그 1.0) statusReport.required = [uuid, timestamp, operationalState, location]. errorCodes 는 필수가 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "ros_amr_interop 예제는 ROS→MassRobotics 한 방향의 운용 상태·오류 매핑 사례일 뿐이므로 Open-RMF·VDA 5050·MassRobotics 세 체계의 공통 상태·오류 어휘 표준으로 일반화하지 않는 것이 맞아 보이며, 세 체계를 함께 다루는 표준 매핑은 이번에도 확인하지 못했다(oq-033 부분 근거).",
      "tag": "의견",
      "source_ids": [
        "ref-255",
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f27·f28 에서 도출. 1.1.1·1.0 은 고정된 과거 태그이며 최신 지원 범위를 뜻하지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "free_fleet 1.3.0 태그의 README 는 메시지를 CycloneDDS 의 dds_idlc 로 FleetMessages.idl 에서 생성한다고 설명하고, ROS 1·ROS 2 양쪽의 cyclonedds 판을 같게 맞춰야 한다고 권고하며, DDS 를 쓰지 않는 새 판을 준비 중이라고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-256"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README(태그 1.3.0) Message Generation: \"dds_idlc from CycloneDDS\". Prerequisites: \"the version of cyclonedds used/built should be the same\". 태그 커밋일은 확인하지 못해 발행일 미확인 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "위키의 free_fleet 설명(현재 기본 브랜치의 zenoh 기반 Nav2·Nav1 어댑터)과 과거 태그 1.3.0 의 CycloneDDS 기반 설치 절차는 섞지 않고 판을 밝혀 적는 것이 좋아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-256"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f30 과 기존 7절(ref-256 기본 브랜치 README, zenoh) 비교에서 도출. zenoh 판에 대응하는 배포 태그는 확인하지 못함",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "vda-5050-lib.js 의 v1.7.0(2026-04-29) 변경 이력은 VDA 5050 3.0 지원을 추가하며 새 Topic.ZoneSet·Topic.Responses 토픽, VdaVersion 의 '3.0.0', 3.0 용 사전 컴파일 검증기와 타입을 넣었다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-742"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "CHANGELOG.md 1.7.0 (2026-04-29) 'VDA5050 V3.0 Support': \"new Topic.ZoneSet and Topic.Responses topics, extended VdaVersion type with \\\"3.0.0\\\", V3.0 pre-compiled validators\"",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "어댑터에 VDA 5050 라이브러리를 쓸 때는 라이브러리 판과 지원 규격 판을 함께 고정하는 것이 좋아 보이며, 라이브러리가 선언한 3.0 지원은 제조사 로봇과의 적합성·실물 호환성 검증으로 세지 않는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-742"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f32 에서 도출. 규격 원문과 별개 프로젝트의 구현 이력",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "InOrbit 은 Automate 2026 시연에서 Ati Robotics·Kärcher·Neura Robotics·Omron·Peer Robotics·Quasi Robotics·Unitree 7개사 로봇이 공유 공간에서 함께 임무를 수행하고, Slamcore·Guide Robotics 의 실시간 위치 추적(RTLS)으로 수동 차량까지 묶어 InOrbit 을 포함해 10개사가 협업했다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1427"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"Robots from Ati Robotics, Kärcher, Neura Robotics, Omron, Peer Robotics, Quasi Robotics, and Unitree ... execute complex missions together\", \"ten companies in total, including InOrbit.AI\". 현장 유형은 전시 시연 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-10",
      "site_type": "기타",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f35",
      "claim": "Automate 2026 시연의 '10개사'는 참여 기업 수(로봇 7·위치 추적 2·InOrbit 1)이지 로봇 대수나 AMR 제조사 수가 아니므로, 상용 운영 사례가 아닌 전시 시연으로 분류하는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1427"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f34 에서 도출. 로봇 대수·성능·가동률·실패 기록은 페이지에 없음",
      "as_of": "2026-10-10",
      "site_type": "기타",
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "카카오모빌리티는 2024년 로보티즈와 업무협약을 맺고 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용해 왔다고 발표했다(2026-03-16).",
      "tag": "추정",
      "source_ids": [
        "ref-1428",
        "ref-1200"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 보도자료 \"신라스테이 서초, 반얀트리 클럽 앤 스파 서울 등 프리미엄 호텔에서 상용 로봇 배송 서비스를 적용\". 아시아경제 기사(ref-1200)는 보도자료를 옮긴 것이라 독립 확인 아님. 2. 사용 사례·요구·책임 범위에 같은 사례 있음",
      "as_of": "2026-10-10",
      "site_type": "상업 시설",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f37",
      "claim": "카카오모빌리티–로보티즈 호텔 사례는 국내 플랫폼–로봇 제조사 연동 사례로 분류하되, 제어 위임 방식·API·로봇 대수가 공개되지 않아 한 현장에서 여러 제조사 플릿을 함께 운영한 증거나 직접 제어·위임 비교 근거(oq-031)로는 쓰지 않는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-1428",
        "ref-1200"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f36 에서 도출. 가동률 8배·배송 성공률 100% 는 분모·기간 미확인이라 새로 넣지 않음. 다수 제조사 협력은 사업 계획으로만 언급됨",
      "as_of": "2026-10-10",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "연계 대상: ISO 21423(산업용 이동로봇 통신·상호운용) 공식 카탈로그가 2026-10-10 기준 '60.00 Under publication' 단계를 표시한다는 외부 메모의 기록이 있으나, iso.org 가 403 으로 막혀 이번에 직접 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-159"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "외부 조사 메모 기록에 의존(카탈로그 Life cycle 60.00). 규격 본문 미열람. 공통 좌표계 등 내용은 oq-027(21. 상호운용 표준·적합성)에서 다룸",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "Open Robotics Discourse 의 Interop SIG 2026-07-02 세션 공지는 Open-RMF REST API 를 언어 모델이 호출할 수 있는 MCP 도구로 노출하는 서버와, 영어 명령을 다단계 RMF 임무로 바꿔 NVIDIA Isaac Sim 창고의 로봇이 Nav2 로 실행하는 에이전트(Nayantra)를 발표한다고 알린다.",
      "tag": "사실",
      "source_ids": [
        "ref-854"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2026-06-25 공지: \"an MCP server that exposes the Open-RMF REST API as LLM-callable tools\", \"executed by a robot in an NVIDIA Isaac Sim warehouse\". 영상 전체·실물 대수는 확인하지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "MCP 로 Open-RMF REST API 를 노출하는 시연은 47. AI·학습·적응과 모델 운영(및 12. 채팅으로 업무 지시·오케스트레이션)과의 연결 지점으로 제안할 만하나, 시뮬레이션 창고 시연이므로 실물 다사업자 플릿의 안정성 근거로 쓰지 않는 것이 맞아 보인다.",
      "tag": "의견",
      "source_ids": [
        "ref-854"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f39 에서 도출. 승인 관문 위치는 기존 oq-141 이 다룸. 코드 태그·실패 처리 시험은 확인하지 않음",
      "as_of": "2026-10-10",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 3.0.0 명세 원문. 이번에는 3.0.0 태그판의 §4.1(단절 시 마지막으로 해제된 노드까지 수행)·§6.6.9·§7.8(세 동작 상태 배열)을 대조했고, VDA 공식 PDF 표지의 판 표기 'Version 3.0.0, March 2026'을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-032",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "Version 3.0 of VDA 5050 released",
      "published": "2026-04-20",
      "url": "https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 3.0 판 공개를 알리는 VDA 보도자료. 본문 날짜는 'Berlin, April 20, 2026'이다(URL 은 260421 계열).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1423",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "VDA 5050",
      "published": "2026-03-17",
      "url": "https://www.vda.de/en/news/publications/publication/vda-5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0(Interface for the Communication between Mobile Robots and a Fleet Control) 항목. 표시 날짜는 2026-03-17이며 PDF(3.38 MB) 내려받기를 제공한다. 발행일은 카탈로그 표시일 기준이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 책의 플릿 통합 장. 전체 제어·신호등·읽기 전용 수준과, 전체 제어에 필요한 조건(제조사 관제가 명시 경로를 지정·중단·교체)을 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1029",
      "org": "InOrbit",
      "title": "Contents — InOrbit Developer Portal",
      "published": null,
      "url": "https://developer.inorbit.ai/docs",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "로봇 운영 플랫폼의 API·SDK·커넥터를 설명하는 개발자 문서. 이번에는 Open-RMF 절의 오픈소스 전체 제어 플릿 어댑터 언급을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1424",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 신호등 수준 연동 API 헤더(2.14.0 태그). moving_from() 호출 전제(정지 시간·통신 지연·최대 감속)와 교착 시 사람 개입 가능성(Blocker)을 적는다. 발행일은 2.14.0 패키지판 날짜다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp",
      "source_unopened": false
    },
    {
      "id": "ref-1398",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그). 2.14.0(2026-09-26)에 EasyTrafficLight 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 기록돼 있다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "source_unopened": false
    },
    {
      "id": "ref-136",
      "org": "Lopes, D., Pereira, T., Gonçalves, A. 외 17명 (Polytechnic University of Coimbra 등; Applied Sciences, MDPI)",
      "title": "Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector",
      "published": "2025-06-27",
      "url": "https://www.mdpi.com/2076-3417/15/13/7235",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Applied Sciences 15(13) 7235, DOI 10.3390/app15137235. 자동차 공장 적용을 목표로 여러 제조사 AGV·AMR 을 하나의 웹 플랫폼으로 감시하는 플릿 관리 소프트웨어를 실험실에서 시험했다. 기존 ref-136 저자 '미확인' 정정(출판 PDF 첫 원문 열람, 저자 17명 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://mdpi-res.com/d_attachment/applsci/applsci-15-07235/article_deploy/applsci-15-07235.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1429",
      "org": "Franke, S., Lünsch, D., Jost, J., & Roidl, M.",
      "title": "Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept",
      "published": "2023-10-11",
      "url": "https://proc.logistics-journal.de/article/download/1067/1036/8465",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Logistics Journal: Proceedings No.19, DOI 10.2195/lj_proc_franke_en_202310_01. 2023년 봄 여섯 회사 워크숍으로 VDA 5050 개념 기반 새 표준 인터페이스 요구를 정리했다. 기존 ResearchGate URL 대신 학술지 원문 PDF 를 처음 열람했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-258",
      "org": "ARM Institute",
      "title": "Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs)",
      "published": null,
      "url": "https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "ARM Institute 과제 소개. 주관 기관 Siemens Technology, 협력 기관 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 이며 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만들 계획을 적는다. 이번이 첫 원문 열람이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1425",
      "org": "chart-singapore / CHART (open-rmf/rmf_ros2 GitHub)",
      "title": "Add GoToZone feature (rmf_ros2 pull request #516)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/pull/516",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "원문 미열람. 구역 이름을 받아 구역 안 경유점을 예약하는 GoToZone 기능을 제안하는 풀 리퀘스트로 외부 조사 메모가 미병합이라 기록했으나, 이번 환경에서 GitHub 접근이 막혀 상태를 확인하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1426",
      "org": "Open Robotics Discourse (OSRA Interop SIG)",
      "title": "Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature",
      "published": "2026-05-04",
      "url": "https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "CHART 가 RMF-2.0 프로젝트로 개발한 Open-RMF 구역(zones) 기능을 소개하는 2026-05-07 SIG 세션 공지. 공지 시점에 기능이 검토 중이라고 밝히고, 2026-07-08 녹화 링크가 덧붙었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://discourse.openrobotics.org/t/54490.json",
      "source_unopened": false
    },
    {
      "id": "ref-255",
      "org": "InOrbit (inorbit-ai GitHub)",
      "title": "ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender)",
      "published": null,
      "url": "https://github.com/inorbit-ai/ros_amr_interop",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "InOrbit 의 AMR 상호운용 ROS 패키지 저장소. 이번에는 1.1.1 태그의 MassRobotics 송신 예제 설정(operationalState·errorCodes 토픽 매핑)을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/inorbit-ai/ros_amr_interop/1.1.1/massrobotics_amr_sender_py/params/sample_config.yaml",
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마. 이번에는 1.0 태그에서 statusReport 필수 필드(uuid·timestamp·operationalState·location)를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/1.0/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-256",
      "org": "Open Robotics (open-rmf)",
      "title": "free_fleet — README (A free fleet management system)",
      "published": null,
      "url": "https://github.com/open-rmf/free_fleet",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF free_fleet README. 이번에는 과거 태그 1.3.0 의 README(CycloneDDS dds_idlc 메시지 생성, ROS 1·2 cyclonedds 판 일치 권고)를 확인했다. 태그 커밋일은 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/free_fleet/1.3.0/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-742",
      "org": "coatyio (vda-5050-lib.js GitHub)",
      "title": "vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README)",
      "published": null,
      "url": "https://github.com/coatyio/vda-5050-lib.js",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Node.js·브라우저용 VDA 5050 라이브러리. 이번에는 v1.7.0(2026-04-29) 변경 이력의 VDA 5050 3.0 지원(ZoneSet·Responses 토픽, 3.0 검증기)을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/coatyio/vda-5050-lib.js/v1.7.0/CHANGELOG.md",
      "source_unopened": false
    },
    {
      "id": "ref-1427",
      "org": "InOrbit.AI",
      "title": "10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026",
      "published": null,
      "url": "https://www.inorbit.ai/automate-2026",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-10",
      "summary": "InOrbit 의 Automate 2026 다중 제조사 로봇 오케스트레이션 시연 페이지. 로봇 7개사·위치 추적 2개사·InOrbit 을 합쳐 10개사 협업이라고 밝힌다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1428",
      "org": "카카오모빌리티",
      "title": "카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속",
      "published": "2026-03-16",
      "url": "https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-10",
      "summary": "카카오모빌리티 보도자료. 로보티즈와 협력해 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용했고 가동률·성공률 개선을 주장한다. 같은 내용을 옮긴 기사는 기존 ref-1200 이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1200",
      "org": "아시아경제",
      "title": "호텔 룸서비스도 카카오모빌리티 로봇이…\"가동률 ... (제목 일부만 확인)",
      "published": "2026-03-16",
      "url": "https://view.asiae.co.kr/article/2026031610244491183",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-10",
      "summary": "카카오모빌리티·로보티즈의 호텔 룸서비스 로봇 배송 사례(신라스테이 서초·반얀트리 클럽 앤 스파 서울)와 회사가 밝힌 가동률·성공률·매출 수치를 전한 기사. 카카오모빌리티 보도자료(ref-1428)를 옮긴 것이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "원문 미열람. 서로 다른 공급사의 산업용 이동로봇·플릿 관리자 사이 통신·상호운용을 다루는 ISO 규격 페이지. 외부 메모는 2026-10-10 단계 60.00(발행 중)을 기록했으나 이번 환경에서 iso.org 가 403 으로 막혀 확인하지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-854",
      "org": "Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse",
      "title": "Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)",
      "published": "2026-06-25",
      "url": "https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "OSRA 상호운용 SIG 2026-07-02 세션 공지(2026-06-25 게시). Open-RMF REST API 를 MCP 도구로 노출하는 서버와 NVIDIA Isaac Sim 창고 로봇을 움직이는 에이전트(Nayantra)를 다룬다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://discourse.openrobotics.org/t/55687.json",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "sections": [
        "3",
        "5",
        "6",
        "7",
        "8",
        "10",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3 — IO-AMRs 목표 문장(기존 내용 확인)에 주관 기관 Siemens Technology·협력 기관과 '계획 단계' 범위만 보탬(f21·f22·f23). / 섹션 5 — 연동 위치와 제어 수준을 따로 기록하는 기준(f14, InOrbit 문서 f13 은 벤더 주장 보강 근거로만; 제조사 관제 API 경유 전체 제어 조건은 '제약' 행 ref-251 에 이미 있어 중복 추가 안 함), 새 사례 두 개: 전시 시연(현장 유형 기타, f34·f35, 벤더 주장), 국내 호텔(현장 유형 상업 시설, f36·f37, 벤더 주장; 2. 사용 사례·요구·책임 범위의 ref-1200 사례와 같은 건이므로 '플랫폼–제조사 연동 사례' 분류 관점만 짧게). / 섹션 6(주제 페이지 2026-09-25-area09-s6 요약) — VDA 연결 단절 시 실행 의미와 상태 분리(f6~f8; '마지막으로 해제된 노드' 번역어는 대분류 개요와 같게, f6 사실은 개요에 이미 있으므로 영역 20 에는 상태 분리 관점으로), 신호등 연동의 정지 시간 전제·교착 시 사람 개입(f9~f11), 상태·오류 변환표 절에 ros_amr_interop→MassRobotics 필드 매핑 사례(f27~f29). / 섹션 7(주제 페이지 2026-09-25-area09-s7 표) — VDA 5050 3.0.0 행의 '정확한 발행일 미확인'을 공식 자료 세 날짜 표시로 교체(f1~f5), Open-RMF 신호등 연동 평가 시 패키지 판 기록(f12; 2.14.0 수정 사실은 27. 다중 로봇 경로·교통 관리 — MAPF 에 이미 있음), Open-RMF 구역 기능 개발 상태(f24 추정·f25·f26), free_fleet 1.3.0 판 구분(f30·f31), vda-5050-lib.js v1.7.0 3.0 지원(f32·f33). / 섹션 8(주제 페이지 2026-09-25-area09-s8) — Lopes 외 항목의 저자 '미확인'을 17명 저자·DOI 로, '작업 상태 갱신 평균 지연 120 ms'를 '로봇 상태 평균 갱신 간격 약 120 ms'로 정정하고 20대 감시·§5.3 실험실 범위 추가(f15~f18), Franke 외 항목에 워크숍 구성과 서지 보강(f19·f20). / 섹션 10(주제 페이지 2026-09-25-area09-s10) — 21. 상호운용 표준·적합성: ISO 21423 단계 기록은 추정으로 연결 제안 수준(f38, oq-027 과 겹치므로 링크만), 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션: MCP 로 Open-RMF REST API 노출 시연(f39·f40, oq-141 관련). / 섹션 11(주제 페이지 2026-09-25-area09-s11) — 분리 페이지의 '신규' 세 질문을 실제 id 로 표기(oq-031·oq-032·oq-033), 부분 근거: oq-005 ← f1~f5, oq-032 ← f9~f11, oq-033 ← f27~f29, oq-031 ← f14·f20·f37(답 아님, 판단 기준만). 모두 열림 유지. 새 질문 5건. 다음 실행 후보: 21. 상호운용 표준·적합성(ISO 21423 발행 확인, f38), 27. 다중 로봇 경로·교통 관리 — MAPF(신호등 연동 교착, f9~f11)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "Lopes 외 논문이 보고한 로봇 상태 평균 갱신 간격 약 120 ms 와 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점(타임스탬프 정의)으로 측정했는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 37. 관제 화면·실행 기록 | 근거: f15 | 종류: 일반",
    "ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f22 | 종류: 일반",
    "zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가? | 관련 영역: 20. 로봇·제조사 관제 연동, 42. 분산 시스템·통신·컴퓨팅 구조 | 근거: f30 | 종류: 일반",
    "InOrbit 의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동 | 근거: f34 | 종류: 일반",
    "카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API 와 로봇 대수·운영 기간은 공개됐는가? | 관련 영역: 20. 로봇·제조사 관제 연동, 64. 상업 시설 | 근거: f36 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 21,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI(ChatGPT) 조사 메모(runs/2026-10-10-06/external_research.md)를 변환했다. 2026-10-10 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정)을 반영했다.",
      "VDA 5050 3.0.0 GitHub 릴리스 설명의 'March 19th, 2026'과 게시 시각(published_at)은 이 환경에서 확인하지 못해 출처로 넣지 않았다(발행일 null 유지).",
      "f24: GoToZone PR #516(ref-1425)의 설명·미병합 상태는 GitHub 접근 차단으로 원문 대조 실패. 간접 근거로 2026-05-04 SIG 공지(ref-1426, f25)만 사실로 둠",
      "f38: ISO 21423 카탈로그의 '60.00 Under publication' 단계는 iso.org 403 으로 확인 실패(ref-159 원문 미열람)",
      "f15~f17: Lopes 외 120 ms·20대 결과의 측정 장소·로봇 구성·시험 기간은 논문에 명시돼 있지 않음",
      "f30: free_fleet 1.3.0 태그 커밋일 미확인(published null)",
      "f34·f36: Automate 2026 시연과 카카오모빌리티 호텔 사례는 벤더 발표만 있고 독립 확인 없음(ref-1200 은 보도자료를 옮긴 기사)",
      "oq-031: 국내 물류센터의 직접 제어·위임 비중·비용·처리량 비교 자료는 이번에도 찾지 못함"
    ],
    "scope_violations": [
      "f38: ISO 21423 은 21. 상호운용 표준·적합성 쪽 내용이므로 claim 을 '연계 대상: '으로 시작하고 10절 연결 제안 수준으로만 씀",
      "f9~f11: 신호등 연동의 교착 처리는 27. 다중 로봇 경로·교통 관리 — MAPF 와 겹치므로 영역 20 에는 연동 계약 관점으로 한정",
      "f39·f40: MCP·언어 모델 연동은 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션 쪽 내용이라 연결 제안으로만 씀",
      "f36·f37: 호텔 사례의 업무 범위는 2. 사용 사례·요구·책임 범위·64. 상업 시설에 이미 있으므로 영역 20 에는 연동 사례 분류만"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 6
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(queries 0 은 집계 없음을 뜻함). 신규 출처 6건(ref-1423, ref-1424, ref-1425, ref-1426, ref-1427, ref-1428, 예약 구간 ref-1423~ref-1452 안), 재사용 15건. 메모 출처 매핑: n1·VDA 공식 PDF→ref-031, n3→ref-032, n4→ref-1423(신규), n5→ref-251, n6→ref-1424(신규, 위키에 EasyTrafficLight.hpp 출처 없음), n7→ref-136, n8→ref-1429, n9→ref-258, n10→ref-1398, n11→ref-1425(신규, 미열람), n12→ref-742, n13→ref-255, n14→ref-230, n15→ref-256, n16→ref-1427(신규; 기존 ref-177 은 RoboticsTomorrow 게재 보도자료라 다른 문서), n17→ref-1428(신규, 카카오모빌리티 보도자료 원문)+ref-1200(같은 내용을 옮긴 아시아경제 기사, 이번에 재열람해 호텔 이름 확인), n18→ref-854, n19→ref-159, n20→ref-1029. n2(GitHub 릴리스)는 넣지 않음. 간접 근거로 SIG 공지 ref-1426(신규) 추가. 검증 수정 반영: VDA 날짜는 세 공식 표시가 다르다는 것을 사실로, 하나로 확정하지 않는 것은 의견으로(f4·f5); 상태 배열 근거를 §6.6.9·§7.8 로(§7.7 아님, f7); '마지막으로 해제된 노드' 번역어를 대분류 개요와 맞춤(f6); Lopes 120 ms 를 '평균 갱신 간격'으로, 실험실 범위를 §5.3 지도 작성·연결 작업으로 좁힘(f15~f17); Franke 근거 쪽수 p.5(f19); IO-AMRs 는 주관 기관·계획 단계만 새로(f21·f22); 제조사 관제 API 경유 전체 제어는 5절 '제약' 행 기존 내용이라 중복 추가 안 함(f13 은 보강); EasyTrafficLight 2.14.0 수정은 의견으로만(f12); GoToZone PR·ISO 21423 단계는 추정·미열람(f24·f38); Automate·호텔은 벤더 주장·추정 유지. 교차 확인 0건: VDA 날짜 세 자료는 모두 VDA 계열, Open-RMF 헤더·변경 이력은 같은 프로젝트, ref-1200 은 ref-1428 을 옮긴 기사라 독립 출처가 아니다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-005 근거 f1~f5, oq-032 근거 f9~f11, oq-033 근거 f27~f29, oq-031 판단 기준 f14·f20·f37. 분리 페이지 11절의 '신규' 세 질문은 oq-031·oq-032·oq-033 이다. 메모의 새 질문 U1~U11 가운데 기존 질문과 겹치는 U1(oq-005)·U2(oq-031)·U3(oq-032)·U4(oq-033)·U11(oq-141 과 겹침)과 본문 근거가 없는 U6 은 빼고 U5·U7·U8·U9·U10 을 다듬어 5건을 올렸다. 현장 유형 사례 finding: 상업 시설(호텔, f36·f37), 기타(전시 시연, f34·f35). 용어 후보 없음(플릿 어댑터·VDA 5050·오픈 RMF 는 용어집에 있음). 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-10-06/verification.json

```json
{
  "run_id": "2026-10-10-06",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 보도자료를 열람함. 제목 'Version 3.0 of VDA 5050 released', 날짜 표기 'Berlin, April 20, 2026'. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 발행물 카탈로그를 열람함. 'March 17, 2026', 'VDA 5050 Version 3.0.0', 'PDF 3,38 MB'. 카탈로그 표시일이 문서 발행일인지는 페이지에 설명이 없다(브리프와 같은 판단)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 검증 단계에서 VDA 배포 PDF(3.4 MB, 카탈로그 표시 크기와 일치)를 열었으나 바이너리여서 표지 문구 'Version 3.0.0, March 2026'을 대조하지 못함. 또 ref-031 의 URL 은 GitHub 마크다운 명세이고 그 본문에는 'Version 3.0.0'만 있고 월 표기가 없다. 따라서 PDF 표지에 관한 주장의 근거로는 맞지 않는다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 확인: 카탈로그(2026-03-17)와 보도자료(2026-04-20)의 날짜가 다르다는 것은 확인함. 세 번째 표시(PDF 표지 2026-03)는 f3 과 같은 이유로 미대조. 세 자료 모두 VDA 계열이라 독립 교차 확인이 아니다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지(위키 의견으로 표기). 발행일을 하나로 확정하지 않는다는 판단은 f1·f2 로 뒷받침된다. 다만 전제인 PDF 표지 월(f3)이 강등됐으므로 ref-031 각주의 발행일을 2026-03 으로 바꾸지 않는다. 산업계 2차 자료(idealworks)는 2026-03-19 공개를 적고 있어 oq-005 는 열린 채로 둔다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-031.txt §4.1 'it keeps all the order information and fulfills the order up to the last released node'. 대분류 F 개요에 같은 사실이 이미 있다(중복). 영역 20 에는 상태 분리 관점으로만 쓴다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3.0.0 태그 원문 §6.6.9·§7.8 을 열람함. 세 배열 구분과 각 배열의 보존·삭제 규칙(actionStates 는 새 주문 수락 시 삭제, 나머지 둘은 clearInstantActions·clearZoneActions 실행 때까지 유지)이 맞다. zoneActionStates 는 구역 동작을 지원하면 필수이고, 예정 구역 동작 보고는 선택이다. *_STATES_FULL 은 'may throw'이며, 6.6.5.4 오류 표와 errorType 열거값에는 없다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. f6·f7 에서 도출한 설계 판단이며, 위키 의견임을 밝힌다. 복구 절차는 '32. 예외 복구·재계획·업무 연속성'과 연결만 한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: EasyTrafficLight.hpp(2.14.0 태그)를 열람함. \\warning 문구(network latency·maximum deceleration)와 MovingError·WaitingError, 'interrupted or deadlocked'가 맞다. 이는 API 계약의 전제이며 실험 수치가 아니다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 헤더의 Blocker 주석 'Human intervention may be required at this point'를 확인함."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 단일 프로젝트 API 문서에서 도출했다. 제어 수준별 교통 성능 비교 자료가 없다는 점은 oq-032 의 부분 근거로만 쓴다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CHANGELOG.rst 2.14.0(2026-09-26)에 #524·#525 가 있음. 같은 URL 이 실행 2026-10-10-04 에서 ref-1513 으로도 등록돼 있어 id 가 중복된다(퍼블리셔 URL 병합 대상)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 주장): InOrbit 개발자 문서에서 'open source full control fleet adapter for RMF'를 확인함. 추정·벤더 주장으로 유지한다. 발행일 미확인."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. ref-251 원문(입력 source_texts)에 전체 제어 조건('specify explicit paths … interrupted … replaced')이 있음. 국내 비중·비용 비교 자료는 미확인."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정(본문 부분). MDPI HTML 은 403 이고 PDF 본문은 판독하지 못함. PDF 메타데이터와 검색 결과의 초록은 'an average latency of 120 ms for task status updates'와 'interface refresh rate of less than 1 s'로 적는다. 즉 초록은 '작업 상태 갱신'의 평균 지연이라 하고, 브리프가 인용한 본문 §6.2 는 '로봇 상태' 평균 갱신 간격이라 한다. 같은 논문 안에서 표현이 다르다. 초록 문장은 확인한 사실, 본문 §6.2 문장은 검증 단계에서 대조하지 못한 것이다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. '최대 20대 동시 감시'와 '서버 가동률 99.5% 이상'은 본문 §6.2 기준이다. 검증 단계에서는 PDF 판독 실패와 MDPI 403 때문에 대조하지 못했고, 검색 결과(초록)에도 없음. 리서치의 열람 기록에만 의존한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. §5.3 의 약 500 m² 실험실과 '측정 장소 미명시'는 본문 기준이며 검증 단계에서 대조하지 못함. 저자 17명은 PDF 메타데이터로 확인함(David Lopes 외 16명)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "열린 질문 이동",
      "note": "기존 위키 표현 '작업 상태 갱신 평균 지연 120 ms'는 검증 단계에서 확인한 초록 문구와 일치한다. 그러므로 이를 본문 표현으로 '고치는' 것은 같은 논문 안의 두 표현 가운데 하나를 고르는 일이 된다(공통 규칙 2절). 교체하지 않고 두 표현을 함께 둔다. 차이는 Lopes 관련 새 열린 질문에 합친다. 실험실 감시 결과를 장기 운영·주행 제어 성능으로 인용하지 않는다는 한정은 f15~f17 서술 안에 남길 수 있다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 확인: 학술지 페이지(proc.logistics-journal.de/article/view/1067)에서 저자 4명, 발행 2023-10-11, DOI 10.2195/lj_proc_franke_en_202310_01, Proceedings Nr. 19, '소프트웨어 업체·하드웨어 제조사·최종 사용자와의 워크숍'을 확인함. '2·3·1, 여섯 회사, 2023년 봄'이라는 구성 수치는 본문 p.5 기준이며, PDF 판독 실패로 검증 단계에서 대조하지 못함. 페이지 원제는 독일어이고 브리프 제목은 영문판이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 초록이 워크숍 기반 요구 수집 연구임을 확인함. 처리량 비교 근거로 쓰지 않는다는 한정은 타당하다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ARM Institute 과제 페이지를 열람함. 'Lead: Siemens Technology', 협력 기관 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis. 발행일 미확인."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Technical Approach 의 'will leverage outputs from a prior ARM-funded project to create a muti-map manager …'(원문 철자). 완료일·결과는 페이지에 없음."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 과제 소개는 계획 서술이므로 성과 근거로 쓰지 않는다는 판단은 타당하다."
    },
    {
      "finding_id": "f24",
      "source_exists": false,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "삭제",
      "note": "ref-1425(rmf_ros2 PR #516)는 github.com 과 api.github.com 모두 403 이고, 'Add GoToZone feature' 검색에서도 해당 PR 이 나오지 않아 실재를 확인하지 못함. 외부 메모에만 의존한 주장이므로 삭제한다. 구역 기능의 개발 상태는 f25(ref-1426)만으로 서술한다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Discourse 공지를 열람함(2026-05-04 게시). 'currently undergoing review', CHART, RMF-2.0 Project, 환자 중심 목적지 선택·승강기 공유 예시, 2026-07-08 녹화 게시를 확인함. 병합 여부는 알 수 없다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 근거 출처는 ref-1426 하나로 줄인다(f24 삭제)."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 1.1.1 태그 sample_config.yaml 을 열람함. /we_b_robots/mode → operationalState, /troubleshooting/errorcodes → errorCodes, 쉼표 구분 문자열을 MassRobotics 표준의 배열로 바꾼다는 주석이 있다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 1.0 태그 JSON 스키마에서 statusReport.required 는 uuid·timestamp·operationalState·location 이고 errorCodes 는 선택이다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 한 방향 예제를 일반화하지 않는다는 한정은 타당하다. oq-033 의 부분 근거."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: free_fleet 1.3.0 README 를 열람함. dds_idlc 로 FleetMessages.idl 에서 생성, 'the version of cyclonedds used/built should be the same', DDS 를 쓰지 않는 새 판 작업 중. 태그 날짜는 미확인."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 판을 밝혀 적는다는 권고."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CHANGELOG 1.7.0(2026-04-29) 'VDA5050 V3.0 Support', ZoneSet·Responses 토픽, VdaVersion '3.0.0', V3.0 사전 컴파일 검증기(타입은 별도 패키지 vda-5050-types-3.0)."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 라이브러리의 지원 선언을 적합성 근거로 세지 않는다는 한정."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 주장): InOrbit 페이지에서 로봇 7개사, RTLS 2개사(Slamcore·Guide Robotics), 'ten companies in total, including InOrbit.AI'를 확인함. 로봇 대수와 행사 날짜는 페이지에 없다. 추정·벤더 주장으로 유지한다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 10개사는 참여 기업 수라는 해석이 페이지와 맞다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 주장): 카카오모빌리티 보도자료(2026-03-16)에서 2024년 로보티즈 업무협약과 신라스테이 서초·반얀트리 클럽 앤 스파 서울을 확인함. 아시아경제 기사(ref-1200, 2026-03-16)는 같은 내용을 옮긴 것이라 독립 확인이 아니다. '2. 사용 사례·요구·책임 범위'에 같은 사례가 있다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 제어 위임 방식·API·대수가 공개되지 않았음을 두 자료에서 확인함. 가동률 8배 등 수치를 넣지 않는다는 판단은 타당하다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 단계에서 iso.org 카탈로그를 열어 'ISO 21423 Robotics — Industrial mobile robots — Communications and interoperability', 단계 60.00(발행 중)을 확인함. 브리프에는 미열람으로 적혀 있고 태그는 올리지 않으므로 [추정]과 '연계 대상' 서술을 유지한다. 규격 본문은 미열람."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Discourse 공지(2026-06-25 게시). 'an MCP server that exposes the Open-RMF REST API as LLM-callable tools', plain-English 명령을 다단계 임무로 바꾸는 에이전트(Nayantra), NVIDIA Isaac Sim 창고, Nav2."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "의견 유지. 시뮬레이션 시연이므로 실물 근거로 쓰지 않는다는 한정은 타당하다. 승인 관문 문제는 oq-141 과 연결만 한다."
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
      "f6(VDA 5050 §4.1, 마지막으로 해제된 노드까지 수행)은 F. 연동 대분류 개요에 이미 있다 — 같은 번역어·각주(ref-031)를 쓰고, 영역 20 에는 상태 분리 관점만 더한다",
      "f12(rmf_fleet_adapter 2.14.0 EasyTrafficLight 수정)는 27. 다중 로봇 경로·교통 관리 — MAPF 갱신(실행 2026-10-10-04)에 이미 있다. 또 같은 URL(rmf_ros2 2.14.0 CHANGELOG.rst)에 ref-1398(이번 브리프·실행 2026-10-10-05)과 ref-1513(실행 2026-10-10-04) 두 id 가 붙어 있다",
      "f13 이 근거로 쓰는 전체 제어 조건은 5절 '제약' 행(ref-251)에 이미 있다 — 새 문장을 만들지 않는다",
      "f36(카카오모빌리티–로보티즈 호텔)은 2. 사용 사례·요구·책임 범위의 ref-1200 사례와 같은 건이다",
      "f38(ISO 21423)은 oq-027·21. 상호운용 표준·적합성의 내용과 겹친다 — 링크만 둔다",
      "f39·f40(MCP 로 Open-RMF REST API 노출)은 oq-141 과 겹친다",
      "f15·f18: 초록의 '작업 상태 갱신 평균 지연 120 ms'(기존 위키 표현과 같음)와 본문 §6.2 의 '로봇 상태 평균 갱신 간격 약 120 ms'(브리프)가 같은 논문 안에서 서로 다르다"
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
    "f3: [사실]을 [추정]으로 강등한다. 'VDA 배포 PDF 표지는 판 표기를 2026년 3월로 적는 것으로 보고됐다(검증 단계 미대조)'처럼 쓰고, 각주는 그 PDF를 내려받게 하는 카탈로그 ref-1423 으로 단다. 이유: ref-031 의 URL 은 GitHub 마크다운 명세로 월 표기가 없고, 검증 단계에서 PDF 표지를 판독하지 못했다.",
    "f4: 'VDA 카탈로그(2026-03-17)와 보도자료 본문(2026-04-20)의 날짜가 서로 다르다'는 [사실](ref-1423·ref-032)로 쓰고, PDF 표지의 월(2026-03)은 f3 처럼 [추정]으로 나눠 쓴다. 이유: 세 번째 표시가 미대조다.",
    "f5: [의견]으로 두되 '이 위키는 …로 본다'처럼 누구의 의견인지 밝힌다. ref-031 각주의 발행일은 '미확인'으로 둔다(2026-03 으로 바꾸지 않는다). 이유: 근거가 된 f3 이 강등됐고, oq-005 는 열린 채로 남는다.",
    "7절(주제 페이지 2026-09-25-area09-s7)과 11절의 oq-005: 해결로 바꾸지 않는다. 부분 근거로 f1·f2·f4(나눠 쓴 형태)와 f5 의견만 덧붙이고 상태는 '열림'으로 유지한다.",
    "f15: 같은 논문 안의 두 표현을 함께 제시한다. 초록 '작업 상태 갱신(task status updates)의 평균 지연 120 ms, 화면 갱신 1초 미만'은 [사실](ref-136)로, 본문 §6.2 '로봇 상태 평균 갱신 간격 약 120 ms'는 [추정](검증 단계 미대조)으로 쓴다. 이유: 초록과 본문이 측정 대상을 다르게 부르고, 본문은 검증 단계에서 대조하지 못했다.",
    "f18: 8절의 기존 표현 '작업 상태 갱신 평균 지연 120 ms'를 '로봇 상태 평균 갱신 간격'으로 교체하지 않는다. 대신 f15 의 두 표현 병기로 처리하고, 실험실 감시 결과라는 한정만 서술에 남긴다. 표현 차이는 Lopes 관련 새 열린 질문 문장에 '초록의 작업 상태 갱신 지연과 본문의 로봇 상태 갱신 간격은 같은 측정인가'로 합친다. 이유: 기존 표현은 초록과 일치하므로 한쪽을 고르면 안 된다.",
    "f16·f17: [사실]을 [추정]으로 강등하고 '논문 본문 §6.2·§5.3 은 …를 보고한다(검증 단계 미대조)'로 쓴다. 이유: 20대·99.5%·500 m²는 본문 수치인데 검증 단계에서 PDF 판독 실패와 MDPI 403 으로 대조하지 못했다.",
    "ref-136: 기관 칸 'Lopes, D., Pereira, T., Gonçalves, A. 외 17명'을 'Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명)'으로 고친다. 8절 분리 페이지의 저자 '미확인'은 이것으로 바꾼다. 이유: PDF 메타데이터 기준 저자는 모두 17명이다.",
    "f19: 저자 4명, 발행 2023-10-11, DOI, 'Logistics Journal: Proceedings Nr. 19', '소프트웨어 업체·하드웨어 제조사·최종 사용자와의 워크숍'은 [사실](ref-1429)로 쓴다. '소프트웨어 2·하드웨어 3·창고 사용자 1, 여섯 회사, 2023년 봄'은 [추정](본문 p.5 기준, 검증 단계 미대조)으로 쓴다.",
    "ref-1429 각주: URL 을 학술지 원문 PDF(https://proc.logistics-journal.de/article/download/1067/1036/8465)로, 발행일을 2023-10-11 로, 접근일을 2026-10-10 으로 바꾸고 '(원문 미열람)'을 뗀다. 기존 8절 문장 'VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다'는 초록으로 확인됐으므로 유지한다.",
    "ref-258 각주: 접근일을 2026-10-10 으로 바꾸고 '(원문 미열람)'을 뗀다(이번 브리프 fetched true, 검증 단계 열람 확인). 3절 IO-AMRs 문장에는 f21(주관 기관)·f22(계획 단계)·f23 의 범위 한정만 덧붙이고, 성과 근거로 쓰지 않는다.",
    "f24: 본문·표·열린 질문 어디에도 넣지 않는다. ref-1425 는 reference_updates 에서 뺀다(미사용·실재 미확인 출처). f26 의 근거 각주는 ref-1426 하나로 단다. 이유: PR #516 은 github.com·api.github.com 403 이고 검색에서도 확인되지 않았다.",
    "f12: 2.14.0 CHANGELOG 의 각주는 퍼블리셔 참고문헌 색인에서 그 URL 에 이미 붙은 id 하나만 쓴다(ref-1398 과 ref-1513 이 같은 URL 이다). 수정 사실 자체는 27. 다중 로봇 경로·교통 관리 — MAPF 에 있으므로 영역 20 에는 '판을 기록한다'는 평가 관점만 [의견]으로 쓴다.",
    "f6: 문장을 새로 만들지 않고, 대분류 F 개요와 같은 번역어 '마지막으로 해제된 노드'와 같은 각주(ref-031)를 쓴다. 6절에는 f8 의 상태 분리 관점([의견])을 중심으로 쓴다. 이유: 같은 사실이 대분류 개요에 이미 있다.",
    "f13·f34·f36: [추정]에 '벤더 주장'을 병기한다. 독립 확인이 없으며, ref-1200 은 ref-1428 을 옮긴 기사이므로 교차 확인으로 쓰지 않는다.",
    "5절 새 사례 두 건(현장 유형 '기타' 전시 시연 f34·f35, '상업 시설' 호텔 f36·f37): 여섯 항목(시작 조건·작업 대상·수행 자원·제약·완료·인계·예외·성과) 가운데 근거가 없는 칸은 '미확인'으로 둔다. 로봇 대수·위임 방식·성과 수치는 채우지 않는다. site_matrix_updates 에는 근거로 실제로 채운 칸만 낸다.",
    "f38: '연계 대상: ' 서술과 [추정]을 유지하고, 10절에서 21. 상호운용 표준·적합성으로 연결만 한다. ref-159 각주는 브리프 기록대로 접근일 뒤 '(원문 미열람)'을 둔다.",
    "f39·f40: 10절에서 47. AI·학습·적응과 모델 운영, 12. 채팅으로 업무 지시·오케스트레이션과 연결하는 문장으로만 쓰고(번호와 이름 함께), 승인 관문 문제는 oq-141 링크로 넘긴다. 시뮬레이션 시연임을 밝힌다.",
    "직접 인용: 페이지에서는 출처마다 직접 인용을 1회 이하로 한다. 특히 ref-031(f6), ref-136(f15~f17), ref-1424(f9·f10), ref-1427(f34)은 브리프 발췌에 인용이 여러 개이므로 하나만 남기고 나머지는 재서술한다. ARM 페이지 인용의 'muti-map' 같은 원문 오탈자는 재서술로 피한다.",
    "트랙 반영 제안(data/area_reflection_proposals.json): 실행 2026-09-25-23 의 제안(팩트시트 2.x→3.0.0 필드 이름 변화)은 이번 브리프에 근거 finding 이 없으므로 이번 실행에서 7절에 반영하지 않고 '제안' 상태로 둔다. 실행 2026-09-25-35 의 제안은 f28(statusReport 필수 필드) 범위만 반영한다. 운용 상태 9종·적재 여유 비율·형식·단위 정규화는 이번 브리프 finding 이 없으므로 반영하지 않는다.",
    "open_questions_new: 다섯 질문은 형식이 맞으므로 등록한다. 다만 첫 질문(Lopes)에는 f18 처리에 따라 초록과 본문 표현의 차이를 함께 묻는 문장을 덧붙인다. oq-031·oq-032·oq-033·oq-005 는 모두 '열림'을 유지하고 부분 근거만 단다. oq-032 는 f9~f11, oq-033 은 f27~f29, oq-031 은 f14·f20·f37 이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 32건, 미확인 8건, 교차 확인 0건. 강등: f3·f4·f15·f16·f17·f19 사실 → 추정(VDA PDF 표지와 Lopes·Franke 논문 본문 수치는 검증 단계에서 원문 판독 실패로 미대조), f18 열린 질문 이동(초록 '작업 상태 갱신 평균 지연 120 ms'와 본문 '로봇 상태 평균 갱신 간격'의 표현 차이), f24 삭제(ref-1425 실재 미확인). 원문 미열람 출처: ref-1425(제외), ref-159(브리프 기준 미열람. 검증 단계에서 iso.org 카탈로그의 단계 60.00 표시는 확인함). 주의: VDA 5050 3.0.0 의 날짜는 VDA 카탈로그 2026-03-17 과 보도자료 2026-04-20 이 서로 다르다. 산업계 2차 자료에는 2026-03-19 공개라는 기록도 있어 발행일을 하나로 확정하지 않으며, oq-005 는 열려 있다. 새로 더한 내용은 대부분 단일 출처이거나 위키 의견(신호등 연동 계약 항목, 연결 상태와 동작 실패의 분리, 판 기록)이다. 전시 시연(기타)과 호텔(상업 시설) 사례는 벤더 주장이고 로봇 대수·위임 방식은 공개되지 않았다. 같은 URL(rmf_ros2 2.14.0 CHANGELOG)에 ref-1398·ref-1513 두 id 가 있어 퍼블리셔 병합이 필요하다. 트랙 반영 제안 2건 가운데 근거 finding 이 있는 MassRobotics 상태 보고 필수 필드만 반영하고, 나머지는 제안으로 남긴다. 정정 요청 없음. 검증 검색 5회 사용.",
  "retry_reason": null
}
```

### runs/2026-10-10-06/pages.json

```json
{
  "run_id": "2026-10-10-06",
  "outline": [
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1100,
      "summary": "기존 3단락을 유지하고 IO-AMRs 과제의 주관·협력 기관과 계획 단계라는 범위 한정 단락만 더한다. [사실][^ref-258]",
      "planned_findings": [
        "f21",
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1900,
      "summary": "연동 위치와 제어 수준을 나눠 기록하자는 위키 의견을 더하고, 전시 시연(기타)과 호텔 배송(상업 시설) 사례를 벤더 주장으로 추가한다. [의견][^ref-251][^ref-1029]",
      "planned_findings": [
        "f13",
        "f14",
        "f34",
        "f35",
        "f36",
        "f37"
      ]
    },
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "VDA 5050 단절 시 연결 상태와 동작 실패를 나눠 보존하는 관점, 신호등 연동의 정지 시간 전제와 교착 시 사람 개입, ROS→MassRobotics 상태·오류 매핑 사례를 더한다. [의견][^ref-031]",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f11",
        "f27",
        "f29"
      ]
    },
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1600,
      "summary": "VDA 5050 3.0.0 공식 자료의 날짜가 서로 다름(카탈로그 2026-03-17, 보도자료 2026-04-20)을 병기하고 공개 구현의 판 정보를 더한다. [사실][^ref-1423][^ref-032]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f12",
        "f25",
        "f26",
        "f28",
        "f30",
        "f31",
        "f32",
        "f33"
      ]
    },
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1300,
      "summary": "Lopes 외 논문의 초록·본문 표현 차이를 병기하고 실험실 감시 결과로 한정하며, Franke 외 연구의 서지와 워크숍 구성을 보강한다. [사실][^ref-136][^ref-1429]",
      "planned_findings": [
        "f15",
        "f16",
        "f17",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 900,
      "summary": "21. 상호운용 표준·적합성(ISO 21423 단계, 추정), 47. AI·학습·적응과 모델 운영·12. 채팅으로 업무 지시·오케스트레이션(MCP 시연), 2·64·67번 사례 연결을 더한다. [사실][^ref-854]",
      "planned_findings": [
        "f38",
        "f39",
        "f40"
      ]
    },
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "section": "11. 열린 질문",
      "budget_chars": 1000,
      "summary": "oq-005·oq-031·oq-032·oq-033 에 부분 근거만 달고 열림을 유지하며 새 질문 5건을 적는다.",
      "planned_findings": [
        "f5",
        "f11",
        "f14",
        "f29"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 3절 IO-AMRs 범위 한정 추가, 5절 연동 위치·제어 수준 기록 기준과 상업 시설·기타 사례 추가, 6절 단절 시 상태 분리·신호등 연동 전제·상태 변환 사례, 7절 VDA 5050 3.0.0 날짜 병기·공개 구현 판 정보, 8절 Lopes·Franke 서지·범위 보강, 10절 21·47·12·2·64·67번 연결, 11절 부분 근거와 새 질문 5건, 13절 각주 갱신(ref-258·ref-1429 열람 반영, 신규 각주)",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              2,
              5,
              12,
              15,
              21,
              22,
              25,
              27,
              29,
              32,
              42,
              47,
              64,
              67
            ],
            "sources": [
              "ref-004",
              "ref-031",
              "ref-032",
              "ref-105",
              "ref-136",
              "ref-148",
              "ref-153",
              "ref-159",
              "ref-230",
              "ref-251",
              "ref-252",
              "ref-254",
              "ref-255",
              "ref-256",
              "ref-257",
              "ref-258",
              "ref-1429",
              "ref-742",
              "ref-854",
              "ref-1029",
              "ref-1398",
              "ref-1423",
              "ref-1424",
              "ref-1426",
              "ref-1427",
              "ref-1428"
            ],
            "last_run": "2026-10-10"
          },
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-10-area20-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 로봇·제조사 관제 연동 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,846자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area20-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 로봇·제조사 관제 연동 의 \"6. 대표 접근법과 기술\" 절(1,564자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area20-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 로봇·제조사 관제 연동 의 \"11. 열린 질문\" 절(1,353자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area20-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 로봇·제조사 관제 연동 의 \"8. 대표 연구와 자료\" 절(1,168자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area20-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 로봇·제조사 관제 연동 의 \"3. 왜 중요한가\" 절(915자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-10-area20-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 20. 로봇·제조사 관제 연동 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(879자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-10 | 20. 로봇·제조사 관제 연동 | 차등 갱신: VDA 5050 3.0.0 공식 자료 날짜 차이 병기, 단절 시 상태 분리·신호등 연동 전제·상태 변환 사례, 상업 시설·기타 사례 추가, Lopes·Franke·IO-AMRs 서지·범위 보강, 새 열린 질문 5건 | run 2026-10-10-06",
  "index_updates": {
    "home_recent": "2026-10-10 — 20. 로봇·제조사 관제 연동: VDA 5050 3.0.0 공식 자료의 날짜 차이(카탈로그 2026-03-17·보도자료 2026-04-20) 병기, 신호등 연동 전제와 단절 시 상태 분리, 상업 시설·기타 현장 사례 추가",
    "category_recent": "2026-10-10 — 20. 로봇·제조사 관제 연동: 3·5·6·7·8·10·11절 차등 갱신(VDA 5050 3.0.0 날짜 병기, Open-RMF 신호등 연동 전제, ros_amr_interop 상태 매핑, Lopes·Franke 서지 보강)",
    "area_recent": "2026-10-10 — 20. 로봇·제조사 관제 연동: 연동 위치·제어 수준 기록 기준과 호텔(상업 시설)·전시 시연(기타) 사례, 단절 시 상태 분리, 공개 구현 판 정보, 21·47·12번 연결과 새 열린 질문 5건 추가"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 3.0.0 명세 원문. 3.0.0 태그판의 §4.1(단절 시 마지막으로 해제된 노드까지 수행)·§6.6.9·§7.8(세 동작 상태 배열)을 대조했다. 이 마크다운 본문에는 판의 월 표기가 없어 발행일은 미확인으로 둔다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-032",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "Version 3.0 of VDA 5050 released",
      "published": "2026-04-20",
      "url": "https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "VDA 5050 3.0 판 공개를 알리는 VDA 보도자료. 본문 날짜는 2026-04-20(베를린)이며 URL 은 260421 계열이다. 카탈로그 표시일(2026-03-17)과 다르다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1423",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "VDA 5050",
      "published": "2026-03-17",
      "url": "https://www.vda.de/en/news/publications/publication/vda-5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목. 표시 날짜 2026-03-17, PDF(3.38 MB) 내려받기 제공. 표시일이 문서 발행일인지는 설명이 없고, 배포 PDF 표지의 판 표기(2026년 3월)는 검증 단계에서 대조하지 못했다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 책의 플릿 통합 장. 전체 제어·신호등·읽기 전용 수준과, 전체 제어에 필요한 조건(제조사 관제가 명시 경로를 지정·중단·교체)을 설명한다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1029",
      "org": "InOrbit",
      "title": "Contents — InOrbit Developer Portal",
      "published": null,
      "url": "https://developer.inorbit.ai/docs",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "로봇 운영 플랫폼의 API·SDK·커넥터를 설명하는 개발자 문서. Open-RMF 절에서 InOrbit 이 제어하는 플릿을 RMF core 에 잇는 오픈소스 전체 제어 플릿 어댑터를 밝힌다(벤더 주장).",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1424",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF 신호등 수준 연동 API 헤더(2.14.0 태그). 이동 시작 통지의 전제(정지 시간·통신 지연·최대 감속)와 교착 시 사람 개입 가능성(Blocker)을 적는다. 발행일은 2.14.0 패키지판 날짜다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1398",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0)",
      "published": "2026-09-26",
      "url": "https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "rmf_fleet_adapter 패키지 변경 이력(2.14.0 태그). 2.14.0(2026-09-26)에 EasyTrafficLight 플릿 상태 발행 수정(#525)과 누적 지연 계산 수정(#524)이 기록돼 있다. 같은 URL 에 ref-1513 이 붙어 있어 병합이 필요하다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-136",
      "org": "Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명) (Polytechnic University of Coimbra 등; Applied Sciences, MDPI)",
      "title": "Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector",
      "published": "2025-06-27",
      "url": "https://www.mdpi.com/2076-3417/15/13/7235",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Applied Sciences 15(13) 7235, DOI 10.3390/app15137235. 자동차 공장 적용을 목표로 여러 제조사 AGV·AMR 을 하나의 웹 플랫폼으로 감시하는 플릿 관리 소프트웨어를 실험실에서 시험했다. 초록은 작업 상태 갱신 평균 지연 120 ms 를, 본문 §6.2 는 로봇 상태 평균 갱신 간격 약 120 ms 를 적는 것으로 보고됐다(본문은 검증 단계 미대조). 저자 '미확인'을 17명으로 정정.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1429",
      "org": "Franke, S., Lünsch, D., Jost, J., & Roidl, M.",
      "title": "Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept",
      "published": "2023-10-11",
      "url": "https://proc.logistics-journal.de/article/download/1067/1036/8465",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Logistics Journal: Proceedings Nr. 19, DOI 10.2195/lj_proc_franke_en_202310_01. 소프트웨어 업체·하드웨어 제조사·최종 사용자와의 워크숍으로 VDA 5050 개념 기반 새 표준 인터페이스 요구를 정리했다. 학술지 원문 PDF 로 URL 을 바꿨다(원 페이지 제목은 독일어, 여기 제목은 영문판).",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-258",
      "org": "ARM Institute",
      "title": "Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs)",
      "published": null,
      "url": "https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "ARM Institute 과제 소개. 주관 기관 Siemens Technology, 협력 기관 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis 이며 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만들 계획을 적는다. 완료일·결과는 페이지에 없다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1426",
      "org": "Open Robotics Discourse (OSRA Interop SIG)",
      "title": "Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature",
      "published": "2026-05-04",
      "url": "https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "CHART 가 RMF-2.0 프로젝트로 개발한 Open-RMF 구역(zones) 기능을 소개하는 2026-05-07 SIG 세션 공지. 공지 시점에 기능이 검토 중이라고 밝히며 병합 여부는 알 수 없다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-255",
      "org": "InOrbit (inorbit-ai GitHub)",
      "title": "ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender)",
      "published": null,
      "url": "https://github.com/inorbit-ai/ros_amr_interop",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "InOrbit 의 AMR 상호운용 ROS 패키지 저장소. 1.1.1 태그의 MassRobotics 송신 예제 설정에서 운용 상태·오류 코드 토픽 매핑과 쉼표 구분 문자열의 배열 변환을 확인했다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마. 1.0 태그에서 statusReport 필수 필드(uuid·timestamp·operationalState·location)와 errorCodes 가 선택임을 확인했다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-256",
      "org": "Open Robotics (open-rmf)",
      "title": "free_fleet — README (A free fleet management system)",
      "published": null,
      "url": "https://github.com/open-rmf/free_fleet",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-10",
      "summary": "Open-RMF free_fleet README. 과거 태그 1.3.0 의 README(CycloneDDS dds_idlc 메시지 생성, ROS 1·2 cyclonedds 판 일치 권고, DDS 를 쓰지 않는 새 판 준비)를 확인했다. 태그 날짜는 미확인.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-742",
      "org": "coatyio (vda-5050-lib.js GitHub)",
      "title": "vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README)",
      "published": null,
      "url": "https://github.com/coatyio/vda-5050-lib.js",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "Node.js·브라우저용 VDA 5050 라이브러리. v1.7.0(2026-04-29) 변경 이력의 VDA 5050 3.0 지원(ZoneSet·Responses 토픽, 판 값 3.0.0, 3.0 검증기)을 확인했다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1427",
      "org": "InOrbit.AI",
      "title": "10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026",
      "published": null,
      "url": "https://www.inorbit.ai/automate-2026",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-10",
      "summary": "InOrbit 의 Automate 2026 다중 제조사 로봇 오케스트레이션 시연 페이지. 로봇 7개사·위치 추적 2개사·InOrbit 을 합쳐 10개사 협업이라고 밝힌다(벤더 주장). 로봇 대수·행사 날짜는 없다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1428",
      "org": "카카오모빌리티",
      "title": "카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속",
      "published": "2026-03-16",
      "url": "https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-10",
      "summary": "카카오모빌리티 보도자료. 2024년 로보티즈와 업무협약을 맺고 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 상용 로봇 배송 서비스를 적용했다고 밝힌다(벤더 주장). 제어 위임 방식·API·로봇 대수는 공개되지 않았다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "원문 미열람. 서로 다른 공급사의 산업용 이동로봇·플릿 관리자 사이 통신·상호운용을 다루는 ISO 규격 페이지. 외부 메모는 2026-10-10 단계 60.00(발행 중)을 기록했으나 리서치 단계에서 iso.org 가 막혀 확인하지 못했다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-854",
      "org": "Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse",
      "title": "Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)",
      "published": "2026-06-25",
      "url": "https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-10",
      "summary": "OSRA 상호운용 SIG 2026-07-02 세션 공지(2026-06-25 게시). Open-RMF REST API 를 MCP 도구로 노출하는 서버와 NVIDIA Isaac Sim 창고 로봇을 움직이는 에이전트(Nayantra)를 다룬다.",
      "cited_by": [
        "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "Lopes 외 논문 초록의 작업 상태 갱신 평균 지연 120 ms 와 본문 §6.2 의 로봇 상태 평균 갱신 간격 약 120 ms 는 같은 측정인가, 그리고 이 값과 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점(타임스탬프 정의)으로 측정했는가?",
      "areas": [
        20,
        37
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가?",
      "areas": [
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가?",
      "areas": [
        20,
        42
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "InOrbit 의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가?",
      "areas": [
        20
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API 와 로봇 대수·운영 기간은 공개됐는가?",
      "areas": [
        20,
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
      "link": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#5-적용-사례-현장-유형-명시",
      "title": "20. 로봇·제조사 관제 연동"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#5-적용-사례-현장-유형-명시",
      "title": "20. 로봇·제조사 관제 연동"
    }
  ],
  "additional_research_requests": [
    "분리 주제 페이지 topics/2026/2026-09-25-area09-s7.md·s8.md·s11.md 의 본문이 이번 입력에 없어 직접 고치지 못했다. 다음 갱신에서 그 페이지들을 입력으로 넣어 (1) s7 표 VDA 5050 3.0.0 행의 '정확한 발행일 미확인'을 카탈로그 2026-03-17·보도자료 2026-04-20 병기로, (2) s8 의 ref-136 저자 '미확인'을 'Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명)'으로, (3) s11 의 '신규' 세 질문을 oq-031·oq-032·oq-033 으로 바꾸도록 요청한다(이번에는 세부영역 페이지 7·8·11절과 reference_updates 로만 반영).",
    "트랙 반영 제안(실행 2026-09-25-23): VDA 5050 팩트시트 2.1.0 태그와 3.0.0 의 필드 이름 변화(agvGeometry→mobileRobotGeometry 등)와 추가 필드를 7절에 넣으려면 이번 브리프에 없는 원문 대조 finding 이 필요하다.",
    "트랙 반영 제안(실행 2026-09-25-35): MassRobotics 운용 상태 9종·적재 여유 비율·화물 최대 중량·부피의 형식·단위 정규화를 7절에 넣으려면 ref-230 원문 대조 finding 이 필요하다.",
    "3절·8절: IO-AMRs 과제의 완료 여부·결과 보고서, Lopes 외 논문 본문 §6.2·§5.3 수치(PDF 판독)와 Franke 외 p.5 워크숍 구성의 원문 대조가 필요하다(현재 [추정]).",
    "7절·10절: VDA 5050 3.0.0 GitHub 릴리스 설명의 날짜와 ISO 21423 카탈로그 단계(60.00)를 원문으로 확인해 oq-005·21. 상호운용 표준·적합성 쪽에 반영할 근거가 필요하다.",
    "7절: Open-RMF 구역(zones) 기능이 배포판(태그)에 병합됐는지 확인할 원문 근거가 필요하다(rmf_ros2 PR #516 은 실재 미확인으로 제외)."
  ],
  "fixes_applied": [
    "f3 강등 — 7절에서 PDF 표지의 판 표기(2026년 3월)를 '보고됐으나 검증 단계에서 대조하지 못했다' [추정]으로 쓰고 각주를 ref-1423 으로 달았다.",
    "f4 분리 — 7절에서 카탈로그 2026-03-17 과 보도자료 2026-04-20 의 날짜 차이는 [사실](ref-1423·ref-032)로, PDF 표지의 월은 별도 [추정] 문장으로 나눠 썼다.",
    "f5 — 7절에 '이 위키는 … 맞다고 본다' 형식의 [의견]으로 썼고, 13절 ref-031 각주 발행일은 '미확인' 그대로 두었다.",
    "oq-005 — 7절과 11절에 부분 근거(f1·f2·f4 분리형, f5 의견)만 덧붙이고 상태는 열림으로 유지했다(open_question_updates 에 해결 변경 없음).",
    "f15 — 8절에서 초록의 작업 상태 갱신(task status updates) 평균 지연 120 ms·화면 갱신 1초 미만은 [사실], 본문 §6.2 의 로봇 상태 평균 갱신 간격은 [추정](검증 단계 미대조)으로 병기했다.",
    "f18 — 기존 '작업 상태 갱신 평균 지연 120 ms' 표현을 교체하지 않고 8절에 두 표현을 병기했으며, 실험실 감시 결과라는 한정만 [의견]으로 남기고 표현 차이는 Lopes 새 열린 질문 문장에 합쳤다.",
    "f16·f17 — 8절에서 20대·99.5%·약 500 m²·측정 장소 미명시를 '논문 본문 §6.2·§5.3 은 … 보고한다(검증 단계 미대조)' [추정]으로 썼다.",
    "ref-136 기관 — reference_updates 와 13절 각주의 기관을 'Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명)'으로 고쳤다. 분리 페이지(2026-09-25-area09-s8)의 본문은 입력에 없어 직접 패치하지 못했고, 참고문헌 갱신으로 반영되도록 하고 additional_research_requests 에 후속 갱신을 요청했다.",
    "f19 — 8절에서 저자 4명·2023-10-11·DOI·Proceedings Nr. 19·워크숍 참여 주체는 [사실](ref-1429), 2·3·1 여섯 회사·2023년 봄은 [추정](본문 p.5, 검증 단계 미대조)으로 썼다.",
    "ref-1429 각주 — 13절에서 URL 을 학술지 PDF 로, 발행일 2023-10-11, 접근일 2026-10-10 으로 바꾸고 '(원문 미열람)'을 뗐으며, 분리 페이지의 주변 설비 인터페이스 문장은 건드리지 않았다.",
    "ref-258 각주 — 13절에서 접근일을 2026-10-10 으로 바꾸고 '(원문 미열람)'을 뗐으며, 3절에 f21·f22 와 성과 근거로 쓰지 않는다는 f23 범위 한정만 덧붙였다.",
    "f24 — 본문·표·열린 질문 어디에도 넣지 않았고 ref-1425 를 reference_updates 에서 뺐으며, 7절 구역 기능의 의견(f26)은 ref-1426 하나만 각주로 달았다.",
    "f12 — 참고문헌 색인에 있는 ref-1398 하나만 각주로 쓰고(ref-1513 미사용), 7절에 패키지 판을 기록한다는 평가 관점만 [의견]으로 쓰며 수정 내용은 27. 다중 로봇 경로·교통 관리 — MAPF 로 넘겼다.",
    "f6 — 6절에서 새 사실 문장을 만들지 않고 F. 연동 대분류 페이지를 가리키며 같은 번역어 '마지막으로 해제된 노드'와 같은 각주 ref-031 을 썼고, 중심은 f8 의 상태 분리 [의견]으로 두었다.",
    "f13·f34·f36 — 5절의 해당 문장 모두 [추정]에 '벤더 주장'을 병기했고, ref-1200 은 인용·교차 확인에 쓰지 않았다.",
    "5절 새 사례 — 기타(전시 시연)와 상업 시설(호텔) 사례의 근거 없는 칸은 '미확인'으로 두고 로봇 대수·위임 방식·성과 수치를 채우지 않았으며, site_matrix_updates 에는 근거로 채운 '수행 자원' 칸 두 개만 냈다.",
    "f38 — 10절에서 '연계 대상: ' 서술과 [추정]을 유지해 21. 상호운용 표준·적합성으로 연결만 했고, 13절 ref-159 각주에 '(원문 미열람)'을 두었다.",
    "f39·f40 — 10절에서 47. AI·학습·적응과 모델 운영, 12. 채팅으로 업무 지시·오케스트레이션과 잇는 연결 문장으로만 쓰고 시뮬레이션 시연임을 밝혔으며 승인 관문 문제는 oq-141 로 넘겼다.",
    "직접 인용 — 출처 원문 인용은 ref-136 의 'task status updates' 한 구절뿐이며, ref-031·ref-1424·ref-1427·ref-258 은 모두 재서술했다('muti-map' 오탈자는 쓰지 않음).",
    "트랙 반영 제안 — 실행 2026-09-25-23 제안(팩트시트 필드 이름 변화)은 반영하지 않고 제안 상태로 두었고, 실행 2026-09-25-35 제안은 7절에 f28(statusReport 필수 필드) 범위만 반영했다.",
    "open_questions_new — 다섯 질문을 open_question_updates 에 new 로 냈고 Lopes 질문에 초록·본문 표현 차이를 묻는 문장을 합쳤으며, oq-005·oq-031·oq-032·oq-033 은 상태 변경 없이 11절에 부분 근거(oq-032 f9~f11, oq-033 f27~f29, oq-031 f14·f20·f37)만 달았다.",
    "분량 초과 자동 분리: 20. 로봇·제조사 관제 연동 본문 11,882자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 5,097자"
  ]
}
```

### runs/2026-10-10-06/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-10-area20-s7.md (1,846자)
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-10-area20-s6.md (1,564자)
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md "11. 열린 질문" → docs/topics/2026/2026-10-10-area20-s11.md (1,353자)
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-10-area20-s8.md (1,168자)
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md "3. 왜 중요한가" → docs/topics/2026/2026-10-10-area20-s3.md (915자)
    - docs/categories/integration/robot-and-vendor-fleet-manager-integration.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-10-area20-s10.md (879자)
```

### runs/2026-10-10-06/pages/categories/integration/robot-and-vendor-fleet-manager-integration.md

```markdown
---
title: "20. 로봇·제조사 관제 연동"
type: area
category: "F. 연동"
area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [플릿 어댑터, VDA 5050, Open-RMF, MassRobotics, 제조사 관제, 명령·상태 변환]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-10
sources: [ref-004, ref-031, ref-032, ref-105, ref-136, ref-148, ref-153, ref-159, ref-230, ref-251, ref-252, ref-254, ref-255, ref-256, ref-257, ref-258, ref-1429, ref-742, ref-854, ref-1029, ref-1398, ref-1423, ref-1424, ref-1426, ref-1427, ref-1428]
last_run: 2026-10-10
version: 3
---

[홈](../../index.md) › [F. 연동](index.md) › 20. 로봇·제조사 관제 연동

# 20. 로봇·제조사 관제 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

AMR(Autonomous Mobile Robot, 자율이동로봇) 제조사마다 자체 플릿 관리 소프트웨어를 쓰기 때문에 여러 브랜드를 섞은 플릿을 한 현장에서 운영하기 어렵다는 문제가 연구 과제로 다뤄지고 있다. [사실][^ref-258] 미국 ARM Institute의 IO-AMRs 과제는 이 문제를 풀려고 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만드는 것을 목표로 한다. [사실][^ref-258]

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 왜 중요한가](../../topics/2026/2026-10-10-area20-s3.md)에 있다.

## 4. 핵심 개념과 용어

**[플릿 어댑터](../../glossary/fleet-adapter.md)(Fleet Adapter)** — Open-RMF에서 제조사별 API를 RMF 교통 스케줄·협상 시스템의 인터페이스에 잇고, 로봇의 예상 이동 경로(itinerary)를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 하는 구성요소이다. [사실][^ref-004] Open-RMF 통합 문서는 어댑터를 하드웨어별 인터페이스와 RMF 범용 인터페이스 사이의 다리로 설명한다. [사실][^ref-252]

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area09-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 출하

**시나리오:** 출하 팔레트를 제조사가 다른 AMR로 출하 도크까지 운반

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 출하 팔레트 운반을 요청하면, ROP는 연동 방식에 따라 이를 VDA 5050 주문(노드·엣지와 pick·drop action)이나 제조사 관제·Open-RMF 어댑터의 이동·동작 명령으로 바꿔 전달해야 할 것으로 보인다. [추정][^ref-031][^ref-153] |
| 작업 대상 | 해당 없음(화물 식별은 [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)에서 다룬다) |
| 수행 자원 | 개별 로봇 제어(저수준 제어·전체 제어·VDA 5050 직접 연결)는 ROP가 경로·교통을 통합 조정할 수 있는 대신 제조사가 경로 지정·중단·교체 API나 VDA 5050 지원을 제공해야 하고, 제조사 관제 위임이나 신호등·읽기 전용 수준 연동은 연동 부담이 작은 대신 공용 통로·승강기·문에서의 조정이 일시정지·재개나 상태 관측에 그칠 것으로 보인다. [추정][^ref-004][^ref-251][^ref-257][^ref-031] 두 방식의 처리량·비용을 정량 비교한 자료는 이번 조사에서 찾지 못했다. |
| 제약 | Open-RMF 전체 제어로 붙이려면 제조사 관제(또는 로봇 API)가 로봇이 따를 명시적 경로를 지정할 수 있고, 그 경로를 언제든 중단해 새 경로로 바꿀 수 있으며, 이동 중 위치를 실시간으로 갱신해 주어야 한다. [사실][^ref-251] |
| 완료·인계 | VDA 5050 3.0.0의 pick·drop action은 적재물이 로봇에 들어왔거나 떠났고 로봇이 새 적재 상태를 보고했을 때를 완료(FINISHED)로 정의하므로, 관제는 action 상태와 적재 상태로 적재·하역 완료를 확인할 수 있다. [사실][^ref-031] Open-RMF 어댑터 튜토리얼은 로봇·제조사 관제 API에 명령 완료 확인 함수를 요구한다. [사실][^ref-153] |
| 예외·성과 | 주문 거절 오류(NO_ROUTE_TO_TARGET 등), 연결 단절(CONNECTION_BROKEN), Open-RMF 로봇 상태 error가 보고되면 ROP는 이를 공통 예외로 옮겨 다른 로봇·플릿 재배정이나 사람 확인으로 넘겨야 할 것으로 보인다. [추정][^ref-031][^ref-148] |

다음은 설명을 위한 가상의 시나리오이다. 한 물류센터가 VDA 5050을 지원하는 A사 AMR 플릿과 자체 관제 API만 여는 B사 AMR 플릿을 함께 쓰고, ROP가 상위 시스템의 출하 운반 요청을 두 플릿에 나눠 준다고 가정한다.

A사 플릿에는 ROP가 주문을 직접 보내고 pick·drop action 완료로 적재·하역을 확인한다. B사 플릿은 제조사 관제가 경로 교체를 허용하지 않으면 신호등이나 읽기 전용 수준으로만 붙으므로, 공용 통로에서 ROP가 할 수 있는 일이 일시정지·재개나 관측으로 좁아진다. 오류가 나면 두 플릿의 서로 다른 오류 어휘를 공통 예외로 옮긴 뒤 복구를 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)의 규칙에 넘긴다.

### 연동 위치와 제어 수준을 나눠 기록하기

위 물류창고 사례의 '수행 자원'과 '제약' 행은 연동 위치와 제어 수준을 한데 다룬다. 이 위키는 연동 위치(제조사 관제 API를 거치는지, 로봇에 직접 붙는지)와 [제어 수준](../../glossary/fleet-control-level.md)(전체 제어인지)을 따로 판단해 별도 항목으로 기록하고, 제어 권한은 경로 지정·교체, 정지, 진행 상태 반환으로 나눠 적는 것이 좋다고 본다. [의견][^ref-251][^ref-1029]

InOrbit 개발자 문서는 자사 플랫폼이 제어하는 로봇 플릿을 RMF core에 잇는 오픈소스 전체 제어 플릿 어댑터를 제공해 여러 제조사 로봇의 중앙 교통 조정을 가능하게 한다고 밝힌다(벤더 주장, 발행일 미확인, 2026-10-10 확인). [추정][^ref-1029] 관제 플랫폼을 거치는 연동도 전체 제어로 붙을 수 있다는 예이므로, 위치와 수준을 한 항목으로 묶으면 이런 구성이 구분되지 않는다고 이 위키는 본다. [의견][^ref-251][^ref-1029] 직접 제어와 제조사 관제 위임의 처리량·비용을 같은 조건에서 비교한 자료는 이번 갱신(2026-10-10)에서도 찾지 못했다([열린 질문](../../open-questions.md) oq-031).

**현장 유형:** 기타

**사례:** 전시회 공유 공간에서 여러 제조사 로봇이 함께 임무를 수행하는 시연(Automate 2026)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | Ati Robotics·Kärcher·Neura Robotics·Omron·Peer Robotics·Quasi Robotics·Unitree 7개사 로봇이 공유 공간에서 함께 임무를 수행하고, Slamcore·Guide Robotics의 실시간 위치 추적(Real-Time Locating System, RTLS)으로 수동 차량까지 묶었다고 InOrbit이 밝힌다(벤더 주장, 로봇 대수 미확인). [추정][^ref-1427] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

InOrbit은 이 시연에 자사를 포함해 모두 10개사가 협업했다고 밝힌다(벤더 주장, 발행일 미확인, 2026-10-10 확인). [추정][^ref-1427] 이 위키는 '10개사'를 로봇 7개사·위치 추적 2개사·InOrbit을 합친 참여 기업 수로 읽으며, 로봇 대수나 AMR 제조사 수가 아니므로 상용 운영 사례가 아닌 전시 시연으로 분류한다. [의견][^ref-1427] 발표 페이지에는 로봇 대수·성능·임무 실패 기록이 없어, 이 사례를 연동 방식의 효과를 판단하는 근거로 쓰지 않는다.

**현장 유형:** 상업 시설

**사례:** 호텔 로봇 배송에서 플랫폼과 로봇 제조사의 연동(카카오모빌리티–로보티즈)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 카카오모빌리티(플랫폼)가 2024년 로보티즈(로봇 제조사)와 업무협약을 맺고 호텔에 상용 로봇 배송 서비스를 적용해 왔다고 발표했다(벤더 주장). [추정][^ref-1428] 제어 위임 방식·연동 API·로봇 대수는 미확인이다. |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(회사가 밝힌 가동률·성공률 수치는 분모·기간이 확인되지 않아 싣지 않는다) |

카카오모빌리티는 2026-03-16 보도자료에서 신라스테이 서초·반얀트리 클럽 앤 스파 서울 등 호텔에 이 서비스를 적용했다고 밝혔다(벤더 주장, 독립 확인 없음). [추정][^ref-1428] 같은 사례가 [2. 사용 사례·요구·책임 범위](../planning-and-business/use-cases-requirements-and-scope.md)에도 있다. 이 위키는 이 사례를 국내 플랫폼–로봇 제조사 연동 사례로 분류하되, 제어 위임 방식·API·로봇 대수가 공개되지 않았으므로 한 현장에서 여러 제조사 플릿을 함께 운영한 증거나 직접 제어·위임 비교 근거(oq-031)로는 쓰지 않는다. [의견][^ref-1428]

## 6. 대표 접근법과 기술

Open-RMF 플릿 어댑터는 제조사 관제나 로봇 API가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 RMF에 붙는다. [사실][^ref-004][^ref-251] 아래는 이번 조사에서 확인한 연동 방식이다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 대표 접근법과 기술](../../topics/2026/2026-10-10-area20-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050 3.0.0은 제조사 중립 관제–로봇 인터페이스로서 팩트시트, 주문 거절 오류, action 진행 상태 보고를 둔다. [사실][^ref-031] 아래 표는 이 영역이 참조하는 표준과 공개 구현이다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-10-area20-s7.md)에 있다.

## 8. 대표 연구와 자료

VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실][^ref-1429] 이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 대표 연구와 자료](../../topics/2026/2026-10-10-area20-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 이종 제조사를 잇는 어댑터의 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스 [추정][^ref-031][^ref-251][^ref-105][^ref-153] | 연계 대상: 로컬 경로 계획·장애물 회피·위치추정 같은 로봇 자체 주행 기능은 로봇·제조사 쪽에 남는 것으로 보인다. [추정][^ref-031][^ref-251][^ref-105][^ref-153] |
| 시설·설비 제어 | 로봇 작업과 설비를 잇는 별도 인터페이스. [추정][^ref-031][^ref-251][^ref-105][^ref-153] VDA 5050은 AGV·관제와 주변 설비 사이 인터페이스를 다루지 않는다. [사실][^ref-1429] | 연계 대상: 승강기·문 제어 자체. Open-RMF 커뮤니티는 승강기·문 어댑터를 플릿 어댑터와 따로 둔다. [사실][^ref-254] |

이종 제조사를 잇는 ROP의 어댑터는 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스를 맡는 것으로 보인다. [추정][^ref-031][^ref-251][^ref-105][^ref-153] 교통 조정은 VDA 5050 명세 범위 밖이어서 관제 구현의 몫으로 남는다. [사실][^ref-031]

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 보며, 이종 제조사를 연결하는 ROP는 로컬 주행 기능을 제조사에 맡기고 "인터페이스와 실행 보장을 담당할 수 있다"고 적는다([범위 경계](../../about/scope-boundary.md)). free_fleet처럼 내비게이션 스택에 직접 붙는 방식도 주행 기능을 ROP로 가져오는 것이 아니라 연결 지점을 바꾸는 것이다. [추정][^ref-256]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md) — VDA 5050 팩트시트와 Open-RMF task_capabilities 선언은 능력 모델과 맞춰야 할 입력으로 보인다. [추정][^ref-031][^ref-105]

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-10-10-area20-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 질문과 이번 실행에서 새로 올린 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 열린 질문](../../topics/2026/2026-10-10-area20-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) — 섹션 3~11 신규 작성(제어 수준 4범주, 어댑터 API 요구, VDA 5050 3.0.0, MassRobotics, 출하 시나리오), 트랙 반영 제안 7절 반영, 페이지 상태 표식 추가. 2차 수정: 9절 설비 행 태그 분리·free_fleet 문장 태그와 ref-256 각주 추가, 8절 요약 문장 교체 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area09-s7.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,784자)을 옮겼다 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area09-s8.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "8. 대표 연구와 자료" 절(1,706자)을 옮겼다. 2차 수정: 1절·3절 첫 요약 문장을 ref-1429 범위 문장과 조사 범위 설명 두 문장으로 교체 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area09-s6.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "6. 대표 접근법과 기술" 절(1,498자)을 옮겼다 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 열린 질문](../../topics/2026/2026-09-25-area09-s11.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "11. 열린 질문" 절(1,297자)을 옮겼다 (실행 2026-09-25-20)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25
[^ref-252]: Open Robotics, Integration (integration) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-254]: Open Robotics (open-rmf), awesome_adapters — A curated list of adapters from the community which can be used with Open-RMF (README), 미확인, https://github.com/open-rmf/awesome_adapters, 접근일 2026-09-25
[^ref-256]: Open Robotics (open-rmf), free_fleet — README (A free fleet management system), 미확인, https://github.com/open-rmf/free_fleet, 접근일 2026-09-25
[^ref-257]: Interact Analysis, AMR Multi-Fleet Orchestration Software Explained, 미확인, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-25 (원문 미열람)
[^ref-258]: ARM Institute, Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs), 미확인, https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/, 접근일 2026-10-10
[^ref-1429]: Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept, 2023-10-11, https://proc.logistics-journal.de/article/download/1067/1036/8465, 접근일 2026-10-10
[^ref-1029]: InOrbit, Contents — InOrbit Developer Portal, 미확인, https://developer.inorbit.ai/docs, 접근일 2026-10-10
[^ref-1427]: InOrbit.AI, 10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026, 미확인, https://www.inorbit.ai/automate-2026, 접근일 2026-10-10
[^ref-1428]: 카카오모빌리티, 카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속, 2026-03-16, https://www.kakaomobility.com/newsroom/detail/%EC%B9%B4%EC%B9%B4%EC%98%A4%EB%AA%A8%EB%B9%8C%EB%A6%AC%ED%8B%B0-%EA%B5%AD%EB%82%B4-%EB%A1%9C%EB%B4%87-%EA%B8%B0%EC%97%85-%ED%98%91%EB%A0%A5%ED%95%B4-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EA%B8%B0%EB%B0%98-%EB%A1%9C%EB%B4%87-%EC%83%9D%ED%83%9C%EA%B3%84-%ED%99%95%EC%9E%A5-%EC%A7%80%EC%86%8D-361, 접근일 2026-10-10
```

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md

```markdown
---
title: "20. 로봇·제조사 관제 연동"
type: area
category: "F. 연동"
area_no: 20
related_areas: [5, 15, 22, 25, 27, 29, 32, 42]
tags: [플릿 어댑터, VDA 5050, Open-RMF, MassRobotics, 제조사 관제, 명령·상태 변환]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-105, ref-148, ref-251, ref-252, ref-153, ref-254, ref-256, ref-257, ref-258, ref-259]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 연동](index.md) › 20. 로봇·제조사 관제 연동

# 20. 로봇·제조사 관제 연동

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

AMR(Autonomous Mobile Robot, 자율이동로봇) 제조사마다 자체 플릿 관리 소프트웨어를 쓰기 때문에 여러 브랜드를 섞은 플릿을 한 현장에서 운영하기 어렵다는 문제가 연구 과제로 다뤄지고 있다. [사실][^ref-258] 미국 ARM Institute의 IO-AMRs 과제는 이 문제를 풀려고 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만드는 것을 목표로 한다. [사실][^ref-258]

표준 쪽에서도 같은 문제를 다룬다. VDA 5050은 서로 다른 제조사의 AGV(Automated Guided Vehicle, 무인운반차)·AMR을 하나의 관제(fleet control)로 운용하기 위한 제조사 중립 통신 인터페이스이다. [사실][^ref-031][^ref-259]

이 영역의 옛 분류의 질문은 개별 로봇을 직접 제어할지, 제조사 관제에 작업을 맡길지이다. Interact Analysis는 자사 분석(의견)에서 제3자 관제가 로봇에 직접 접속하는 저수준 제어가 현재 가장 흔하고 제조사 관제에 작업을 넘기는 고수준 제어가 늘고 있으나, 장기적으로 어느 쪽이 쓰일지는 아직 정해지지 않았다고 본다. [의견][^ref-257] 어느 쪽을 고르느냐에 따라 ROP가 공용 통로·승강기·문에서 다른 플릿과 교통을 조정할 수 있는 정도와 제조사에 요구해야 할 API가 달라질 것으로 보인다. [추정][^ref-004][^ref-251]

## 4. 핵심 개념과 용어

**[플릿 어댑터](../../glossary/fleet-adapter.md)(Fleet Adapter)** — Open-RMF에서 제조사별 API를 RMF 교통 스케줄·협상 시스템의 인터페이스에 잇고, 로봇의 예상 이동 경로(itinerary)를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 하는 구성요소이다. [사실][^ref-004] Open-RMF 통합 문서는 어댑터를 하드웨어별 인터페이스와 RMF 범용 인터페이스 사이의 다리로 설명한다. [사실][^ref-252]

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area09-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 출하

**시나리오:** 출하 팔레트를 제조사가 다른 AMR로 출하 도크까지 운반

| 항목 | 내용 |
|---|---|
| 시작 조건 | 상위 시스템이 출하 팔레트 운반을 요청하면, ROP는 연동 방식에 따라 이를 VDA 5050 주문(노드·엣지와 pick·drop action)이나 제조사 관제·Open-RMF 어댑터의 이동·동작 명령으로 바꿔 전달해야 할 것으로 보인다. [추정][^ref-031][^ref-153] |
| 작업 대상 | 해당 없음(화물 식별은 [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)에서 다룬다) |
| 수행 자원 | 개별 로봇 제어(저수준 제어·전체 제어·VDA 5050 직접 연결)는 ROP가 경로·교통을 통합 조정할 수 있는 대신 제조사가 경로 지정·중단·교체 API나 VDA 5050 지원을 제공해야 하고, 제조사 관제 위임이나 신호등·읽기 전용 수준 연동은 연동 부담이 작은 대신 공용 통로·승강기·문에서의 조정이 일시정지·재개나 상태 관측에 그칠 것으로 보인다. [추정][^ref-004][^ref-251][^ref-257][^ref-031] 두 방식의 처리량·비용을 정량 비교한 자료는 이번 조사에서 찾지 못했다. |
| 제약 | Open-RMF 전체 제어로 붙이려면 제조사 관제(또는 로봇 API)가 로봇이 따를 명시적 경로를 지정할 수 있고, 그 경로를 언제든 중단해 새 경로로 바꿀 수 있으며, 이동 중 위치를 실시간으로 갱신해 주어야 한다. [사실][^ref-251] |
| 완료·인계 | VDA 5050 3.0.0의 pick·drop action은 적재물이 로봇에 들어왔거나 떠났고 로봇이 새 적재 상태를 보고했을 때를 완료(FINISHED)로 정의하므로, 관제는 action 상태와 적재 상태로 적재·하역 완료를 확인할 수 있다. [사실][^ref-031] Open-RMF 어댑터 튜토리얼은 로봇·제조사 관제 API에 명령 완료 확인 함수를 요구한다. [사실][^ref-153] |
| 예외·성과 | 주문 거절 오류(NO_ROUTE_TO_TARGET 등), 연결 단절(CONNECTION_BROKEN), Open-RMF 로봇 상태 error가 보고되면 ROP는 이를 공통 예외로 옮겨 다른 로봇·플릿 재배정이나 사람 확인으로 넘겨야 할 것으로 보인다. [추정][^ref-031][^ref-148] |

다음은 설명을 위한 가상의 시나리오이다. 한 물류센터가 VDA 5050을 지원하는 A사 AMR 플릿과 자체 관제 API만 여는 B사 AMR 플릿을 함께 쓰고, ROP가 상위 시스템의 출하 운반 요청을 두 플릿에 나눠 준다고 가정한다.

A사 플릿에는 ROP가 주문을 직접 보내고 pick·drop action 완료로 적재·하역을 확인한다. B사 플릿은 제조사 관제가 경로 교체를 허용하지 않으면 신호등이나 읽기 전용 수준으로만 붙으므로, 공용 통로에서 ROP가 할 수 있는 일이 일시정지·재개나 관측으로 좁아진다. 오류가 나면 두 플릿의 서로 다른 오류 어휘를 공통 예외로 옮긴 뒤 복구를 [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)의 규칙에 넘긴다.

## 6. 대표 접근법과 기술

Open-RMF 플릿 어댑터는 제조사 관제나 로봇 API가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 RMF에 붙는다. [사실][^ref-004][^ref-251] 아래는 이번 조사에서 확인한 연동 방식이다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area09-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050 3.0.0은 제조사 중립 관제–로봇 인터페이스로서 팩트시트, 주문 거절 오류, action 진행 상태 보고를 둔다. [사실][^ref-031] 아래 표는 이 영역이 참조하는 표준과 공개 구현이다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area09-s7.md)에 있다.

## 8. 대표 연구와 자료

VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실][^ref-259] 이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area09-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 이종 제조사를 잇는 어댑터의 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스 [추정][^ref-031][^ref-251][^ref-105][^ref-153] | 연계 대상: 로컬 경로 계획·장애물 회피·위치추정 같은 로봇 자체 주행 기능은 로봇·제조사 쪽에 남는 것으로 보인다. [추정][^ref-031][^ref-251][^ref-105][^ref-153] |
| 시설·설비 제어 | 로봇 작업과 설비를 잇는 별도 인터페이스. [추정][^ref-031][^ref-251][^ref-105][^ref-153] VDA 5050은 AGV·관제와 주변 설비 사이 인터페이스를 다루지 않는다. [사실][^ref-259] | 연계 대상: 승강기·문 제어 자체. Open-RMF 커뮤니티는 승강기·문 어댑터를 플릿 어댑터와 따로 둔다. [사실][^ref-254] |

이종 제조사를 잇는 ROP의 어댑터는 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스를 맡는 것으로 보인다. [추정][^ref-031][^ref-251][^ref-105][^ref-153] 교통 조정은 VDA 5050 명세 범위 밖이어서 관제 구현의 몫으로 남는다. [사실][^ref-031]

분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 보며, 이종 제조사를 연결하는 ROP는 로컬 주행 기능을 제조사에 맡기고 "인터페이스와 실행 보장을 담당할 수 있다"고 적는다([범위 경계](../../about/scope-boundary.md)). free_fleet처럼 내비게이션 스택에 직접 붙는 방식도 주행 기능을 ROP로 가져오는 것이 아니라 연결 지점을 바꾸는 것이다. [추정][^ref-256]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

[5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md) — VDA 5050 팩트시트와 Open-RMF task_capabilities 선언은 능력 모델과 맞춰야 할 입력으로 보인다. [추정][^ref-031][^ref-105]

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area09-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 질문과 이번 실행에서 새로 올린 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [20. 로봇·제조사 관제 연동 — 열린 질문](../../topics/2026/2026-09-25-area09-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) — 섹션 3~11 신규 작성(제어 수준 4범주, 어댑터 API 요구, VDA 5050 3.0.0, MassRobotics, 출하 시나리오), 트랙 반영 제안 7절 반영, 페이지 상태 표식 추가. 2차 수정: 9절 설비 행 태그 분리·free_fleet 문장 태그와 ref-256 각주 추가, 8절 요약 문장 교체 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area09-s7.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,784자)을 옮겼다 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 대표 연구와 자료](../../topics/2026/2026-09-25-area09-s8.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "8. 대표 연구와 자료" 절(1,706자)을 옮겼다. 2차 수정: 1절·3절 첫 요약 문장을 ref-259 범위 문장과 조사 범위 설명 두 문장으로 교체 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area09-s6.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "6. 대표 접근법과 기술" 절(1,498자)을 옮겼다 (실행 2026-09-25-20)
- 2026-09-25 · 생성 · [20. 로봇·제조사 관제 연동 — 열린 질문](../../topics/2026/2026-09-25-area09-s11.md) — 자동 분리: 9. 로봇·제조사 관제 연동 의 "11. 열린 질문" 절(1,297자)을 옮겼다 (실행 2026-09-25-20)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25
[^ref-252]: Open Robotics, Integration (integration) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-254]: Open Robotics (open-rmf), awesome_adapters — A curated list of adapters from the community which can be used with Open-RMF (README), 미확인, https://github.com/open-rmf/awesome_adapters, 접근일 2026-09-25
[^ref-256]: Open Robotics (open-rmf), free_fleet — README (A free fleet management system), 미확인, https://github.com/open-rmf/free_fleet, 접근일 2026-09-25
[^ref-257]: Interact Analysis, AMR Multi-Fleet Orchestration Software Explained, 미확인, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-25 (원문 미열람)
[^ref-258]: ARM Institute, Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs), 미확인, https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/, 접근일 2026-09-25 (원문 미열람)
[^ref-259]: Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept, 2023, https://www.researchgate.net/publication/374741902_Identification_of_requirements_and_opportunities_for_new_types_of_standardized_interfaces_for_AGV_systems_based_on_the_VDA_5050_concept, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-10-06/pages/topics/2026/2026-10-10-area20-s7.md

```markdown
---
title: "20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 연동"
primary_area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-032, ref-1398, ref-1423, ref-1426, ref-230, ref-256, ref-742]
last_run: 2026-10-10
version: 1
split_from: docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#7
---

[홈](../../index.md) › [주제](../index.md) › 20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스

# 20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050 3.0.0은 제조사 중립 관제–로봇 인터페이스로서 팩트시트, 주문 거절 오류, action 진행 상태 보고를 둔다. [사실][^ref-031] 아래 표는 이 영역이 참조하는 표준과 공개 구현이다.
- 이 페이지는 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

VDA 5050 3.0.0은 제조사 중립 관제–로봇 인터페이스로서 팩트시트, 주문 거절 오류, action 진행 상태 보고를 둔다. [사실][^ref-031] 아래 표는 이 영역이 참조하는 표준과 공개 구현이다.


### VDA 5050 3.0.0의 날짜 표시

VDA 발행물 카탈로그의 [VDA 5050](../../glossary/vda-5050.md) Version 3.0.0 항목은 날짜를 2026-03-17로 표시하고, VDA 보도자료 'Version 3.0 of VDA 5050 released'의 본문 날짜는 2026-04-20(베를린)이어서 두 공식 자료의 날짜가 서로 다르다. [사실][^ref-1423][^ref-032] 카탈로그 표시일이 문서 발행일인지는 그 페이지에 설명이 없다. [사실][^ref-1423]

카탈로그에서 내려받는 VDA 배포 PDF의 표지는 판 표기를 2026년 3월로 적는 것으로 보고됐으나, 검증 단계에서 표지 문구를 대조하지 못했다. [추정][^ref-1423] 이 자료들은 모두 VDA 계열이라 독립 교차 확인이 아니며, 날짜 차이의 원인은 어느 자료에도 설명이 없다.

이 위키는 VDA 5050 3.0.0의 발행일을 하나로 확정하지 않고, 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)를 함께 남기는 것이 맞다고 본다. [의견][^ref-1423][^ref-032] 명세 원문 각주의 발행일은 '미확인'으로 두며, [열린 질문](../../open-questions.md) oq-005는 열린 채로 남는다.

### 공개 구현과 판 정보

- **MassRobotics AMR 상호운용 표준**: 1.0 태그의 JSON 스키마는 상태 보고(statusReport)의 필수 필드를 uuid·timestamp·operationalState·location 넷으로 두며, 오류 코드(errorCodes)는 필수가 아니다(발행일 미확인, 2026-10-10 확인). [사실][^ref-230]
- **Open-RMF 신호등 연동**: 이 위키는 신호등 연동을 평가·재현할 때 쓰는 rmf_fleet_adapter 패키지 판을 함께 기록하는 것이 좋다고 본다. 2.14.0(2026-09-26) 변경 이력에 EasyTrafficLight 관련 수정이 들어 있기 때문이며, 수정 내용은 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)에서 다룬다. [의견][^ref-1398]
- **Open-RMF 구역 기능**: Open Robotics Discourse의 상호운용 관심 그룹(Interop SIG) 공지(2026-05-04 게시)는 CHART가 RMF-2.0 프로젝트로 개발한 새 기능을 단계적으로 공개하며, 첫 단계인 시설 구역(zones) 관리 기능이 공지 시점에 검토 중이라고 밝힌다. 병합 여부는 이 공지로 알 수 없다. [사실][^ref-1426] 이 위키는 어댑터 기능 목록을 정리할 때 배포판(태그)에 든 기능과 이런 검토 중 기능을 구분해 적는 것이 좋다고 본다. [의견][^ref-1426]
- **free_fleet**: 1.3.0 태그의 README는 메시지를 CycloneDDS의 dds_idlc로 FleetMessages.idl에서 생성하고, ROS 1·ROS 2 양쪽의 cyclonedds 판을 같게 맞추라고 권고하며, DDS를 쓰지 않는 새 판을 준비 중이라고 적는다(태그 날짜 미확인, 2026-10-10 확인). [사실][^ref-256] 이 위키는 현재 기본 브랜치의 zenoh 기반 어댑터 설명과 과거 1.3.0 태그의 CycloneDDS 기반 설치 절차를 섞지 않고 판을 밝혀 적는 것이 좋다고 본다. [의견][^ref-256]
- **vda-5050-lib.js**: v1.7.0(2026-04-29) 변경 이력은 VDA 5050 3.0 지원을 추가하며 [구역 집합](../../glossary/zone-set.md)(ZoneSet)·응답(Responses) 토픽, 판 값 3.0.0, 3.0용 사전 컴파일 검증기를 넣었다고 적는다. [사실][^ref-742] 이 위키는 어댑터에 VDA 5050 라이브러리를 쓸 때 라이브러리 판과 지원 규격 판을 함께 고정하고, 라이브러리가 선언한 3.0 지원을 제조사 로봇과의 적합성·실물 호환성 검증으로 세지 않는 것이 좋다고 본다. [의견][^ref-742]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-032]: VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released, 2026-04-20, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-10-10
[^ref-1398]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10
[^ref-1423]: VDA(Verband der Automobilindustrie), VDA 5050, 2026-03-17, https://www.vda.de/en/news/publications/publication/vda-5050, 접근일 2026-10-10
[^ref-1426]: Open Robotics Discourse (OSRA Interop SIG), Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature, 2026-05-04, https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490, 접근일 2026-10-10
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-10
[^ref-256]: Open Robotics (open-rmf), free_fleet — README (A free fleet management system), 미확인, https://github.com/open-rmf/free_fleet, 접근일 2026-09-25
[^ref-742]: coatyio (vda-5050-lib.js GitHub), vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README), 미확인, https://github.com/coatyio/vda-5050-lib.js, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-06 | 20. 로봇·제조사 관제 연동 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-10-06/pages/topics/2026/2026-10-10-area20-s6.md

```markdown
---
title: "20. 로봇·제조사 관제 연동 — 대표 접근법과 기술"
type: topic
category: "F. 연동"
primary_area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-004, ref-031, ref-1424, ref-230, ref-251, ref-255]
last_run: 2026-10-10
version: 1
split_from: docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#6
---

[홈](../../index.md) › [주제](../index.md) › 20. 로봇·제조사 관제 연동 — 대표 접근법과 기술

# 20. 로봇·제조사 관제 연동 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- Open-RMF 플릿 어댑터는 제조사 관제나 로봇 API가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 RMF에 붙는다. [사실][^ref-004][^ref-251] 아래는 이번 조사에서 확인한 연동 방식이다.
- 이 페이지는 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

Open-RMF 플릿 어댑터는 제조사 관제나 로봇 API가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 RMF에 붙는다. [사실][^ref-004][^ref-251] 아래는 이번 조사에서 확인한 연동 방식이다.


### 연결 단절 시 실행 의미와 상태 분리

[F. 연동](../../categories/integration/index.md) 대분류 페이지에 적었듯이 VDA 5050 3.0.0에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 마지막으로 해제된 노드까지 주문을 수행한다. [사실][^ref-031] 같은 판은 주문에 딸린 동작·즉시 동작·구역 동작의 [동작 상태](../../glossary/action-status.md)를 상태 메시지의 actionStates·instantActionStates·zoneActionStates 세 배열로 나눠 보고하게 하며, 구역 동작의 예정 상태 보고는 선택 사항이다. [사실][^ref-031]

이 위키는 로봇이 단절 중에도 해제된 노드까지 주행을 이어 가므로, ROP 어댑터가 [연결 상태](../../glossary/connection-state.md)의 단절을 곧 정지로 해석하지 말고 연결 상태와 동작 실패(동작 상태 배열의 FAILED)를 별도 상태로 보존해야 한다고 본다. [의견][^ref-031] 단절 뒤 복구 절차는 [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)에서 다룬다.

### 신호등 수준 연동의 전제

Open-RMF의 신호등 수준 연동 API(EasyTrafficLight, rmf_fleet_adapter 2.14.0, 2026-09-26)는 로봇이 다음 체크포인트에서 멈출 시간이 있을 때만, 곧 정지 명령의 통신 지연과 로봇의 최대 감속을 감안해 이동 시작을 알리라고 경고한다. 이를 어기면 이동·대기 오류(MovingError·WaitingError)가 나고 교통 흐름이 끊기거나 교착될 수 있다고 적는다. [사실][^ref-1424] 이는 API 계약의 전제이며 실험 수치가 아니다.

같은 헤더는 해결할 수 없는 충돌로 [교착](../../glossary/deadlock.md)이 생기면 RMF 교통 협상 시스템이 충돌 참여자를 충분히 제어하지 못하므로 사람 개입이 필요할 수 있다고 적는다. [사실][^ref-1424] 이 위키는 신호등 수준으로 붙는 제조사 플릿의 연동 계약에 정지 명령의 유무만이 아니라 정지 가능 시간(통신 지연·최대 감속), 정지 확인 응답, 교착 시 사람 개입 경로를 함께 적는 것이 좋다고 본다. [의견][^ref-1424] 제어 수준별 교통 성능을 같은 조건에서 비교한 자료는 여전히 찾지 못했다(oq-032). 교착 해소 방법 자체는 [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)에서 다룬다.

### 상태·오류 변환 사례

ros_amr_interop 1.1.1 태그의 MassRobotics 송신 예제 설정은 ROS 토픽 /we_b_robots/mode를 [운용 상태](../../glossary/operational-state.md)(operationalState)에, /troubleshooting/errorcodes를 오류 코드(errorCodes)에 잇고, 쉼표로 구분한 오류 코드 문자열을 MassRobotics 표준이 요구하는 배열로 바꾼다고 주석에 적는다(발행일 미확인, 2026-10-10 확인). [사실][^ref-255] MassRobotics 상태 보고의 필수 필드는 7절에 적었다.

이 위키는 이 예제를 ROS에서 MassRobotics로 가는 한 방향의 운용 상태·오류 매핑 사례로만 보고, Open-RMF·VDA 5050·MassRobotics 세 체계의 공통 상태·오류 어휘로 일반화하지 않는다. [의견][^ref-255][^ref-230] 세 체계를 함께 다루는 표준 매핑은 이번에도 확인하지 못했다(oq-033).

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-1424]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp (2.14.0), 2026-09-26, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp, 접근일 2026-10-10
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-10
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25
[^ref-255]: InOrbit (inorbit-ai GitHub), ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender), 미확인, https://github.com/inorbit-ai/ros_amr_interop, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-06 | 20. 로봇·제조사 관제 연동 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-10-06/pages/topics/2026/2026-10-10-area20-s11.md

```markdown
---
title: "20. 로봇·제조사 관제 연동 — 열린 질문"
type: topic
category: "F. 연동"
primary_area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: []
last_run: 2026-10-10
version: 1
split_from: docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#11
---

[홈](../../index.md) › [주제](../index.md) › 20. 로봇·제조사 관제 연동 — 열린 질문

# 20. 로봇·제조사 관제 연동 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 기존 질문과 이번 실행에서 새로 올린 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 기존 질문과 이번 실행에서 새로 올린 질문이다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.


### 이번 갱신에서 덧붙인 근거와 새 질문(2026-10-10)

분리 페이지의 '신규' 세 질문은 각각 oq-031·oq-032·oq-033이다. 아래 기존 질문은 모두 열림을 유지하며, 이번 갱신은 부분 근거만 더했다.

- **oq-005** (상태: 열림) VDA 5050 3.0.0의 발행일 — 카탈로그 2026-03-17과 보도자료 2026-04-20이 서로 다르고, PDF 표지의 월 표기는 검증 단계에서 대조하지 못했다(7절).
- **oq-031** (상태: 열림) 직접 제어와 제조사 관제 위임의 선택 — 판단 기준(연동 위치와 제어 수준을 나눠 기록)만 보탰고, Franke 외 연구와 호텔 사례는 비교 근거가 아니다(5절·8절).
- **oq-032** (상태: 열림) 신호등 수준 연동의 교착 — 정지 가능 시간 전제와 교착 시 사람 개입 가능성을 API 문서에서 확인했으나 성능 비교 자료는 없다(6절).
- **oq-033** (상태: 열림) 공통 상태·오류 어휘 — ROS에서 MassRobotics로 가는 한 방향 매핑 예제만 확인했다(6절).

이번 실행에서 새로 올린 질문(id는 등록 때 부여된다):

- **신규** (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-06) Lopes 외 논문 초록의 작업 상태 갱신 평균 지연 120 ms와 본문 §6.2의 로봇 상태 평균 갱신 간격 약 120 ms는 같은 측정인가, 그리고 이 값과 최대 20대 동시 감시는 어디서 어떤 로봇 구성·시험 기간·측정 지점으로 측정했는가?
- **신규** (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-06) ARM Institute IO-AMRs 과제의 완료 보고서·공개 코드·실물 로봇 대수와 정량 결과는 공개됐는가?
- **신규** (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-06) zenoh 기반 free_fleet 어댑터에 대응하는 배포 태그와 지원 조합(ROS 2 배포판·Nav2·zenoh 판) 시험표는 무엇인가?
- **신규** (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-06) InOrbit의 Automate 2026 다중 제조사 시연에서 실제 투입된 로봇 대수와 임무 실패·재시도 기록이 공개됐는가?
- **신규** (상태: 열림 · 제기 2026-10-10 · 실행 2026-10-10-06) 카카오모빌리티–로보티즈 호텔 배송 서비스에서 플랫폼은 로봇을 직접 제어하는가, 로보티즈 관제에 임무 단위로 맡기는가, 그 연동 API와 로봇 대수·운영 기간은 공개됐는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-06 | 20. 로봇·제조사 관제 연동 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-10-06/pages/topics/2026/2026-10-10-area20-s8.md

```markdown
---
title: "20. 로봇·제조사 관제 연동 — 대표 연구와 자료"
type: topic
category: "F. 연동"
primary_area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-136, ref-1429]
last_run: 2026-10-10
version: 1
split_from: docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#8
---

[홈](../../index.md) › [주제](../index.md) › 20. 로봇·제조사 관제 연동 — 대표 연구와 자료

# 20. 로봇·제조사 관제 연동 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실][^ref-1429] 이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.
- 이 페이지는 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실][^ref-1429] 이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.


### 서지와 결과 범위 보강(2026-10-10)

- Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency(Applied Sciences 15(13) 7235, 2025-06-27) — 초록은 작업 상태 갱신(task status updates)의 평균 지연을 120 ms, 화면 갱신을 1초 미만으로 보고한다. [사실][^ref-136] 반면 본문 §6.2는 같은 값을 로봇 상태의 평균 갱신 간격(약 120 ms)으로 적는 것으로 보고됐으나 검증 단계에서 대조하지 못했다. [추정][^ref-136] 두 표현이 같은 측정인지는 열린 질문으로 남긴다.
- 같은 논문 본문 §6.2는 AMR·AGV를 포함해 최대 20대를 화면·서버 성능의 큰 저하 없이 동시에 감시했고 시험 기간 서버 가동률이 99.5% 이상이었다고 보고한다(검증 단계 미대조). [추정][^ref-136] 본문 §5.3의 지도 작성·연결 시험은 약 500 m² 실험실에서 이뤄졌고, 120 ms·20대 결과의 측정 장소는 논문에 명시되지 않은 것으로 보고됐다(검증 단계 미대조). [추정][^ref-136] 이 위키는 이 결과를 실험실 감시 성능으로 한정하고, 자동차 공장의 장기 운영 지연이나 20대 동시 주행 제어 성능으로 인용하지 않는다. [의견][^ref-136]
- Franke, S., Lünsch, D., Jost, J., & Roidl, M.(Logistics Journal: Proceedings Nr. 19, 2023-10-11, DOI 10.2195/lj_proc_franke_en_202310_01) — 소프트웨어 업체·하드웨어 제조사·최종 사용자와의 워크숍으로 VDA 5050 개념에 기반한 새 표준 인터페이스 요구를 정리한 연구다. [사실][^ref-1429] 본문 p.5는 참여사를 소프트웨어 기업 2곳·하드웨어 제조사 3곳·창고 사용자 1곳의 여섯 회사로, 시기를 2023년 봄으로 적는 것으로 보고됐다(검증 단계 미대조). [추정][^ref-1429] 이 위키는 이 연구를 연동 요구 분석 자료로 분류하며, 실물 플릿을 비교한 실험이 아니므로 직접 제어와 제조사 관제 위임의 처리량 비교 근거로 쓰지 않는다. [의견][^ref-1429]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-136]: Lopes, D., Pereira, T., Gonçalves, A. 외 14명(저자 17명) (Polytechnic University of Coimbra 등; Applied Sciences, MDPI), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector, 2025-06-27, https://www.mdpi.com/2076-3417/15/13/7235, 접근일 2026-10-10
[^ref-1429]: Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept, 2023-10-11, https://proc.logistics-journal.de/article/download/1067/1036/8465, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-06 | 20. 로봇·제조사 관제 연동 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-10-06/pages/topics/2026/2026-10-10-area20-s3.md

```markdown
---
title: "20. 로봇·제조사 관제 연동 — 왜 중요한가"
type: topic
category: "F. 연동"
primary_area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-004, ref-031, ref-251, ref-257, ref-258, ref-1429]
last_run: 2026-10-10
version: 1
split_from: docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#3
---

[홈](../../index.md) › [주제](../index.md) › 20. 로봇·제조사 관제 연동 — 왜 중요한가

# 20. 로봇·제조사 관제 연동 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- AMR(Autonomous Mobile Robot, 자율이동로봇) 제조사마다 자체 플릿 관리 소프트웨어를 쓰기 때문에 여러 브랜드를 섞은 플릿을 한 현장에서 운영하기 어렵다는 문제가 연구 과제로 다뤄지고 있다. [사실][^ref-258] 미국 ARM Institute의 IO-AMRs 과제는 이 문제를 풀려고 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만드는 것을 목표로 한다. [사실][^ref-258]
- 이 페이지는 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

AMR(Autonomous Mobile Robot, 자율이동로봇) 제조사마다 자체 플릿 관리 소프트웨어를 쓰기 때문에 여러 브랜드를 섞은 플릿을 한 현장에서 운영하기 어렵다는 문제가 연구 과제로 다뤄지고 있다. [사실][^ref-258] 미국 ARM Institute의 IO-AMRs 과제는 이 문제를 풀려고 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만드는 것을 목표로 한다. [사실][^ref-258]

과제 소개 페이지는 주관 기관을 Siemens Technology로, 협력 기관을 FedEx·Yaskawa Motoman·Waypoint Robotics·University of Memphis로 적는다(발행일 미확인, 2026-10-10 확인). [사실][^ref-258] 같은 페이지는 위 세 구성요소를 이전 ARM Institute 지원 과제의 산출물을 활용해 만들 계획으로 서술하므로, 소개 시점의 과제는 계획 단계였다. [사실][^ref-258] 완료일·공개 코드·실물 결과가 소개 페이지에 없으므로, 이 위키는 이 소개를 과제 목표의 근거로만 쓰고 달성한 운영 성과의 근거로는 쓰지 않는다. [의견][^ref-258]

표준 쪽에서도 같은 문제를 다룬다. VDA 5050은 서로 다른 제조사의 AGV(Automated Guided Vehicle, 무인운반차)·AMR을 하나의 관제(fleet control)로 운용하기 위한 제조사 중립 통신 인터페이스이다. [사실][^ref-031][^ref-1429]

이 영역의 옛 분류의 질문은 개별 로봇을 직접 제어할지, 제조사 관제에 작업을 맡길지이다. Interact Analysis는 자사 분석(의견)에서 제3자 관제가 로봇에 직접 접속하는 저수준 제어가 현재 가장 흔하고 제조사 관제에 작업을 넘기는 고수준 제어가 늘고 있으나, 장기적으로 어느 쪽이 쓰일지는 아직 정해지지 않았다고 본다. [의견][^ref-257] 어느 쪽을 고르느냐에 따라 ROP가 공용 통로·승강기·문에서 다른 플릿과 교통을 조정할 수 있는 정도와 제조사에 요구해야 할 API가 달라질 것으로 보인다. [추정][^ref-004][^ref-251]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25
[^ref-257]: Interact Analysis, AMR Multi-Fleet Orchestration Software Explained, 미확인, https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/, 접근일 2026-09-25 (원문 미열람)
[^ref-258]: ARM Institute, Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs), 미확인, https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/, 접근일 2026-10-10
[^ref-1429]: Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept, 2023-10-11, https://proc.logistics-journal.de/article/download/1067/1036/8465, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-06 | 20. 로봇·제조사 관제 연동 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-10-06/pages/topics/2026/2026-10-10-area20-s10.md

```markdown
---
title: "20. 로봇·제조사 관제 연동 — 다른 연구영역과의 연결"
type: topic
category: "F. 연동"
primary_area_no: 20
related_areas: [2, 5, 12, 15, 21, 22, 25, 27, 29, 32, 42, 47, 64, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-10
updated: 2026-10-10
sources: [ref-031, ref-105, ref-159, ref-854]
last_run: 2026-10-10
version: 1
split_from: docs/categories/integration/robot-and-vendor-fleet-manager-integration.md#10
---

[홈](../../index.md) › [주제](../index.md) › 20. 로봇·제조사 관제 연동 — 다른 연구영역과의 연결

# 20. 로봇·제조사 관제 연동 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — VDA 5050 팩트시트와 Open-RMF task_capabilities 선언은 능력 모델과 맞춰야 할 입력으로 보인다. [추정][^ref-031][^ref-105]
- 이 페이지는 [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

[5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — VDA 5050 팩트시트와 Open-RMF task_capabilities 선언은 능력 모델과 맞춰야 할 입력으로 보인다. [추정][^ref-031][^ref-105]


### 이번 갱신에서 더한 연결(2026-10-10)

- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — 연계 대상: ISO 21423(산업용 이동로봇의 통신·상호운용)의 공식 카탈로그가 2026-10-10 기준 60.00(발행 중) 단계를 표시한다는 외부 메모 기록이 있으나, 리서치 단계에서는 원문을 열지 못했다. [추정][^ref-159] 규격 내용과 공통 좌표계 문제는 21. 상호운용 표준·적합성 페이지와 oq-027에서 다룬다.
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — Open Robotics Discourse의 상호운용 관심 그룹 2026-07-02 세션 공지(2026-06-25 게시)는 Open-RMF REST API를 언어 모델이 호출할 수 있는 [모델 컨텍스트 프로토콜](../../glossary/model-context-protocol.md)(MCP) 도구로 노출하는 서버와, 영어 명령을 다단계 RMF 임무로 바꿔 NVIDIA Isaac Sim 창고의 로봇이 Nav2로 실행하게 하는 에이전트(Nayantra)를 발표한다고 알린다. [사실][^ref-854] 이 위키는 이를 관제 연동과 언어 모델 연동이 만나는 지점으로 보되, 시뮬레이션 창고 시연이므로 실물 다사업자 플릿의 안정성 근거로 쓰지 않는다. [의견][^ref-854] 실행 전 승인 관문을 어디에 둘지는 [열린 질문](../../open-questions.md) oq-141에서 다룬다.
- [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md) — 5절의 호텔 배송 사례가 업무 범위 쪽에서 실려 있다.
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 5절의 호텔 배송 사례가 놓이는 현장 유형이다.
- [67. 기타 현장](../../categories/site-type-applications/other-sites.md) — 5절의 전시 시연 사례가 놓이는 현장 유형이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md)
- 관련 영역: [2. 사용 사례·요구·책임 범위](../../categories/planning-and-business/use-cases-requirements-and-scope.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-10-10 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-10

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-10-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-10 | 2026-10-10-06 | 20. 로봇·제조사 관제 연동 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 12건 / 전체 1413건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 2026-09-25 | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 2026-09-25 | 예 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 2026-09-25 | 예 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 2026-09-25 | 예 |
| ref-252 | Open Robotics | Integration (integration) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration.html | 2026-09-25 | 예 |
| ref-254 | Open Robotics (open-rmf) | awesome_adapters — A curated list of adapters from the community which can be used with Open-RMF (README) | 미확인 | https://github.com/open-rmf/awesome_adapters | 2026-09-25 | 예 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | https://github.com/open-rmf/free_fleet | 2026-09-25 | 예 |
| ref-257 | Interact Analysis | AMR Multi-Fleet Orchestration Software Explained | 미확인 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 2026-09-25 | 아니오 |
| ref-258 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 미확인 | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ | 2026-09-25 | 아니오 |
| ref-259 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 2023 | https://www.researchgate.net/publication/374741902_Identification_of_requirements_and_opportunities_for_new_types_of_standardized_interfaces_for_AGV_systems_based_on_the_VDA_5050_concept | 2026-09-25 | 아니오 |
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

### docs/open-questions.md (요약: 대상 영역 [20] 에 걸린 40건 / 전체 364건)

```markdown
- oq-001 [열림] 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? (영역 17, 20, 30)
- oq-005 [열림] 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. (영역 20, 21)
- oq-007 [열림] VDA 5050 3.0.0에서 관제가 loadId를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가? (영역 17, 20)
- oq-014 [열림] 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? (영역 20, 24, 29)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 21, 23)
- oq-031 [열림] 국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가? (영역 20, 35)
- oq-032 [열림] 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? (영역 20, 27)
- oq-033 [열림] Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 29, 38)
- oq-035 [열림] 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기의 ISO 8601 시각, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? (영역 18, 20, 42)
- oq-039 [열림] 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가? (영역 20, 42)
- oq-047 [열림] VDA 5050 로봇이 재부팅되면 받아 둔 주문을 유지하는지에 대한 규정이 명세에서 확인되지 않는데, 제조사 구현이나 공개 사례는 재부팅 뒤 주문·동작 상태를 어떻게 복원하거나 폐기하는가? (영역 20, 29)
- oq-049 [열림] 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? (영역 20, 25, 26)
- oq-053 [열림] ROP 가 플릿 단위로 작업을 입찰·배정하고 제조사 관제가 플릿 안에서 다시 로봇을 고르는 두 수준 배정에서 전체 최적성이 얼마나 손실되며, 이를 줄이려면 제조사 관제가 어떤 비용·상태 정보를 내야 하는가? (관련 기존 질문: oq-031) (영역 20, 25)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 20, 21, 54)
- oq-057 [열림] VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가? (영역 20, 27)
- oq-073 [열림] VDA 5050 3.0.0 판의 네 단계 오류 수준(WARNING·URGENT·CRITICAL·FATAL)과 이전 판(2.x)의 오류 수준이 다를 때, 두 판이 섞인 이종 플릿에서 오류 수준을 어떻게 맞춰 해석하는가? (영역 20, 38)
- oq-076 [열림] 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? (영역 20, 55)
- oq-086 [열림] 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? (영역 20, 34)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 20, 21, 57)
- oq-100 [열림] 외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? (영역 20, 51)
- oq-110 [열림] EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? (영역 20, 21)
- oq-113 [열림] ROP 가 VDA 5050 updateCertificate 같은 보안 명령으로 제조사 로봇의 인증서를 교체할 때, 교체 시점·대상 승인과 실패 시 되돌림 책임은 ROP 사업자·제조사·현장 IT 조직 중 누가 지는가? (영역 20, 51, 57)
- oq-137 [열림] 완료 기한·반복 주기·실패 처리 조건처럼 관제 작업 요청 스키마에 자리가 없는 시나리오 항목을 어느 층(시나리오 모델·워크플로 모델·스케줄러)이 보관하고 실행 시점에 어떻게 작업 요청으로 변환하는가? (영역 9, 24, 26, 20)
- oq-141 [열림] 언어 모델이 MCP 도구 호출로 관제 작업 API 를 직접 부르는 구현에서 실행 전 승인 관문을 어디에 두는지(에이전트 안·MCP 서버·관제 API 앞) 공개 구현이나 운영 사례가 있는가? (영역 12, 20, 13)
- oq-151 [열림] 등록된 능력 온톨로지나 자산관리셸 능력 기술에서 플릿 어댑터의 설정·명령 핸들러·상태 변환 규칙 초안을 자동 생성한 공개 구현이나 현장 사례가 있는가? (영역 6, 20, 4)
- oq-163 [열림] 국내 물류센터에서 서로 다른 제조사의 AGV·소팅봇·무인지게차·하역 로봇을 하나의 오케스트레이션 계층으로 관제한 공개 사례가 있는가(쿠팡 대구·CJ대한통운 사례는 설비별 도입만 확인됐다)? (영역 61, 20)
- oq-174 [열림] 한림대성심병원처럼 제조사가 다른 여러 로봇을 통합관제하는 국내 병원은 어떤 인터페이스·표준(Open-RMF, VDA 5050, 제조사 API)으로 로봇과 승강기를 연결하며 그 구조가 공개돼 있는가? (영역 63, 20)
- oq-176 [열림] 호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? (영역 64, 20, 22)
- oq-183 [열림] 한 아파트 단지에서 제조사가 다른 배송·청소·순찰·주차 로봇을 하나의 관제 계층으로 묶어 공동현관·승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? (영역 65, 20)
- oq-187 [열림] 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? (영역 66, 20, 59)
- oq-192 [열림] 농촌진흥청 통합 관리 프로그램은 다른 제조사의 농업 로봇도 연결할 수 있는 공개 인터페이스를 갖는가, 아니면 자체 개발 로봇 3종 전용인가? (영역 67, 20)
- oq-246 [열림] 여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가? (영역 52, 20, 21)
- oq-255 [열림] 여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가? (영역 36, 20, 55)
- oq-271 [열림] 이기종 로봇 통합 비용이 로봇 도입 총소유비용에서 차지하는 비중과, 공통 인터페이스·오케스트레이션 플랫폼이 그 비용을 얼마나 줄이는지 측정한 독립 연구가 있는가? (영역 3, 20)
- oq-280 [열림] 로봇 제조사·관제 API 의 주 버전 변경이나 폐기를 오케스트레이션 플랫폼에 사전 통지하는 기간과 유예 기간을 계약이나 인터페이스 표준에 명시한 공개 사례가 있는가? (영역 58, 20, 57)
- oq-318 [열림] ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가? (영역 51, 20, 54)
- oq-345 [열림] 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) (영역 20, 21, 24)
- oq-354 [열림] 서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? (관련 기존 질문: oq-053, oq-082) (영역 25, 20)
- oq-355 [열림] 플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가? (영역 25, 20)
- oq-359 [열림] 제조사별 예상 완료 시간의 오차를 고려해 출하 마감 대비 여유 시간을 얼마나 두는가? (영역 26, 20)
```
