(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-18
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 40. 운영 절차·요청 창구 (J. 현장 운영·관제)
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

### runs/2026-09-30-18/target.json

```json
{
  "run_id": "2026-09-30-18",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 127,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 40,
    "area_name": "40. 운영 절차·요청 창구",
    "category": "J. 현장 운영·관제",
    "category_letter": "J"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=40"
}
```

### runs/2026-09-30-18/research.json

```json
{
  "run_id": "2026-09-30-18",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 40,
    "area_name": "40. 운영 절차·요청 창구",
    "category": "J. 현장 운영·관제"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 요청 창구(호출 버튼·단말·앱·API), 요청자 식별, 교대 인수인계, 역할 정의 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·상업 시설·제조 공장·가정의 요청 창구와 운영 조직 사례, 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 요청 접수 스키마, 권한 모델, 구조화된 교대 인수인계, 전담 운영 조직의 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open-RMF 작업 요청 API, VDA 5050 범위, ANSI/A3 R15.08-3, 산업안전보건기준에 관한 규칙 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-203 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? [분류원문]",
    "현장 사용자가 로봇에게 일을 요청하는 창구(호출 버튼·터치스크린·앱·전화 경유·API)는 어떤 형태이며, 요청에 요청자·시각·우선순위 같은 무엇이 담기는가? (섹션 4·6·7 겨냥)",
    "운영자 교대 인수인계에 대해 연속 운영·고위험 분야(공정 산업·의료)의 지침과 근거는 무엇이며, 로봇 관제의 교대에 옮길 수 있는가? (섹션 4·6·8 겨냥)",
    "로봇 운영 절차·역할·교육을 요구하는 표준·법령(ANSI/A3 R15.08 시리즈, 산업안전보건기준에 관한 규칙 등)은 무엇을 요구하는가? (섹션 7 겨냥, 한국 법령 우선)",
    "병원·상업 시설·제조 공장·가정 현장에서 로봇 요청 창구와 운영 조직을 어떻게 두었고, 절차·역할이 불분명할 때 어떤 문제가 보고되었는가? (섹션 3·5 겨냥, 한국 사례 우선)",
    "공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (oq-203, 섹션 6·11 겨냥)",
    "운영 절차·요청 창구에서 ROP가 직접 맡을 것과 업무 시스템·현장 조직·로봇 제조사에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Open-RMF 의 작업 요청(task_request) JSON 스키마는 작업 범주(category)와 그 범주에 맞는 설명(description)만 필수로 두고, 요청자 식별자(requester), 요청 목적 레이블(labels, 예: dashboard), 요청 시각, 가장 이른 시작 시각, 우선순위, 수행을 허용할 플릿 이름을 선택 항목으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1255"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "스키마 필드: category·description 필수, requester는 \"An identifier for the entity that requested this task\", labels·unix_millis_request_time·unix_millis_earliest_start_time·priority·fleet_name 선택 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f2",
      "claim": "Open-RMF 웹 API 서버(rmf-web api-server)는 OpenID Connect 액세스 토큰(JWT)으로 사용자를 확인하고, 역할·동작·자원의 권한 그룹 세 요소로 권한을 판정하며(관리자는 모든 그룹에 모든 동작 가능), 기록을 관계형 데이터베이스에 저장한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1256"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "권한 모델은 role, action, authorization group 의 조합이며 사용자는 여러 역할을 가질 수 있음. 토큰의 preferred_username 클레임 사용. PostgreSQL·SQLite·MySQL·MariaDB 지원 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f3",
      "claim": "VDA 5050 명세는 플릿 관제(마스터 컨트롤)와 로봇 사이 통신을 다루며, 현장 사용자·업무 담당자가 운반 요청을 관제에 올리는 방법은 정하지 않고 프로젝트 조정·수행 절차도 범위 밖에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 2절이 'Project Coordination and Implementation Procedures'를 범위 밖에 두고, 5.3절 플릿 관제 기능은 로봇에 대한 주문 배정을 다룰 뿐 상위 요청 접수 방식은 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f4",
      "claim": "Open-RMF 의 차선 폐쇄 요청 메시지(rmf_fleet_msgs/LaneRequest)는 플릿 이름, 열 차선 id 목록, 닫을 차선 id 목록 세 필드만 가지며 요청자·사유·유효 기간·승인 정보를 담는 필드는 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1257"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메시지 정의 전문: string fleet_name / uint64[] open_lanes / uint64[] close_lanes (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "차선 폐쇄 메시지에 요청자·사유·해제 시점이 없으므로, 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지는 메시지 규격이 아니라 운영 절차와 그 위의 요청·권한 계층(예: 역할 기반 API 서버)에서 정하고 기록해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1257",
        "ref-1256"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "LaneRequest 는 세 필드뿐이고, 권한 판정은 API 서버의 역할·동작·권한 그룹 모델에 있음(f2·f4 종합). oq-203 의 공개 병원·상업 시설 절차 사례는 이번에 찾지 못함",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "영국 보건안전청(HSE)의 인적 요인 지침(Briefing Note No. 8, 2005)과 Brazier·Pacitti(2008)는 교대 인수인계를 대면으로, 양방향 확인 대화로, 문서화된 교대 일지로 뒷받침하고 충분한 시간을 두어 하도록 권고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1258",
        "ref-1259"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "HSE BN8: 대면·양방향 대화·교대 일지 기록·충분한 시간 배정 권고. Brazier·Pacitti: 구조화된 일지, 대면 회의, 양방향 대화, 표준 체크리스트 권고 (공정 산업 맥락)",
      "as_of": "2008",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f7",
      "claim": "Brazier·Pacitti(2008)는 교대 인수인계가 실패하는 원인으로 핵심 운전 정보의 누락, 표준화되지 않은 비공식적 방식, 대면·양방향 대화의 부재, 불완전하거나 찾기 어려운 교대 일지를 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1259"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Hazards XX 논문: inadequate information transfer, lack of structure, poor communication, insufficient documentation 을 문제로 제시",
      "as_of": "2008",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f8",
      "claim": "병원 인수인계 사례: Blazin 외(2020)에 따르면 구조화된 인계 프로그램 I-PASS(질병 중증도·환자 요약·할 일 목록·상황 인식과 비상 계획·수신자의 요약 확인)는 Starmer 외 연구에서 소아 병원 9곳 전공의의 의료 오류를 23%, 예방 가능한 유해 사건을 30% 줄였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1267"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"led to a 23% reduction in medical errors and a 30% reduction in preventable adverse events\" — 원 연구(Starmer 외, NEJM 2014)를 인용한 2차 서술",
      "as_of": "2020-07",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f9",
      "claim": "공정 산업·의료의 교대 인수인계 근거(구조화된 항목, 대면·양방향 확인, 기록)는 로봇 관제 교대에도 옮길 수 있을 것으로 보이나, 여러 로봇을 운영하는 관제의 교대 인수인계 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외 등)을 정한 공개 절차나 표준은 이번 조사에서 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1258",
        "ref-1259",
        "ref-1267"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6~f8 종합. 로봇 관제 전용 교대 절차 자료는 검색(영문·국문)에서 확인하지 못함",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f10",
      "claim": "한국 산업안전보건기준에 관한 규칙 제222조는 산업용 로봇의 작동범위에서 교시 등 작업을 할 때 사업주가 로봇의 조작방법·순서, 매니퓰레이터 속도, 2명 이상 작업 시 신호방법, 이상 발견 시 조치, 이상으로 정지한 뒤 재가동할 때의 조치에 관한 지침을 정해 그에 따라 작업하게 하고, 기동스위치 등에 작업 중 표시를 하도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1269"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "지침 항목: \"이상을 발견하여 로봇의 운전을 정지시킨 후 이를 재가동시킬 경우의 조치\" 등. 국가법령정보센터 조문(시행 2025-09-01 판)",
      "as_of": "2025-09-01",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "ANSI/A3 R15.08-3-2026(산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용, 2026-04-23 발행)은 사용자가 제조사·통합자가 준 정보를 적용해 산업용 이동로봇 응용과 운영 환경을 안전하게 운용·정비하기 위한 요구사항을 정하며, 위험성평가와 응용·현재 운영 환경의 변경 관리, 수명주기 전반의 인원 안전을 강조한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1265"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 요약 기준: user requirements for applying the information provided by the IMR manufacturer and system integrator; management of change of the IMR application and the current operating environment (COE); 77쪽",
      "as_of": "2026-04-23",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "병원 사례: Mutlu·Forlizzi(HRI 2008)의 15개월 민족지 연구에서 자율 배송 로봇(TUG)은 내과 병동에서는 업무 중단에 대한 낮은 허용도, 인지된 비용과 이익의 불일치, 복잡한 통로에서의 주행 중단 때문에 업무 흐름에 부정적 영향을 주고 직원 저항을 낳았지만, 산후 병동에서는 업무 흐름과 사회적 맥락에 통합되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1263"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "같은 로봇이 병동의 환자 특성에 따른 업무 흐름·목표·사회적 관계·공간 사용 차이로 전혀 다르게 받아들여졌다고 보고(workflow, social, and environmental factors)",
      "as_of": "2008-03",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "병원 사례: 같은 연구의 TUG 운용에서는 직원이 터치스크린 단말에서 배송을 시작하고, 지정된 직원이 물품을 싣고 내리며, 로봇이 도움을 요청하면 직원이 알림에 응답하는 방식이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1263"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "원문 PDF 요약 추출: staff initiated deliveries through touchscreen interfaces; designated staff load/unload; staff respond to robot notifications (추출 품질이 낮아 세부 절차 미확인)",
      "as_of": "2008-03",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f14",
      "claim": "병원 사례(한국): 한림대학교성심병원은 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했으며, 커맨드센터는 사용 시나리오 개발, 업무 프로세스 조율, 실시간 모니터링과 문제 대응을 맡는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1261",
        "ref-1262"
      ],
      "cross_checked": true,
      "confidence": "low",
      "evidence_excerpt": "지디넷코리아(2024-09): 7종 73대, 커맨드센터 중심 관제·운영. 로봇신문(2024-04): 7종 73대, 커맨드센터가 통합관제 시스템으로 중앙 관리, 시나리오 개발·업무 프로세스 조율·모니터링·문제 대응",
      "as_of": "2024-09-19",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f15",
      "claim": "병원 사례(한국): 로봇신문 보도에 따르면 한림대학교성심병원에서는 의료진·환자가 안내 데스크나 각 부서에 요청하면 담당자가 로봇으로 서비스를 제공하며, 지디넷코리아 보도에 따르면 2022-08~2024-05 누적 사용은 35,492건이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1262",
        "ref-1261"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "요청 경로는 로봇신문(2024-04)에만, 누적 35,492건은 지디넷코리아(2024-09)에만 있음. 약제 배송·검체 이송·물품 배송·문서 수거·고중량 이송·실외 배송·환자 안내 7개 업무",
      "as_of": "2024-09-19",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f16",
      "claim": "상업 시설 사례: 2017년 뉴욕 알로프트 호텔의 배송 로봇(Savioke Relay) 운용에서는 투숙객이 프런트에 전화로 요청하면 직원이 주문 내용과 객실 번호를 시스템에 입력했고(주문 접수는 자동화되지 않음), 로봇이 승강기와 연동해 이동한 뒤 객실 앞 도착 시 객실 전화로 자동 알림을 보냈다.",
      "tag": "사실",
      "source_ids": [
        "ref-1264"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국일보(2017-04): 투숙객 전화 → 직원이 주문·객실 번호 입력, 도착 시 투숙객에게 자동 알림 전화, 로봇 2대를 월 2,000달러에 임차",
      "as_of": "2017-04-18",
      "site_type": "상업 시설",
      "flow_item": "시작 조건"
    },
    {
      "id": "f17",
      "claim": "상업 시설 사례: Fu·Zheng·Wong(International Journal of Hospitality Management 2022)이 중국 고급 호텔 직원 19명을 면담한 결과, 로봇이 기술·시설·서비스 부서 가운데 어디에 속하는지가 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육, 동료 교육, 고장 처리·고객 안내 같은 추가 업무가 직원의 로봇 사용 저항으로 이어졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1260"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"It's still controversial whether a robot belongs to technology, engineering, or the department that the robot serves.\" (반구조화 면담, 2020-01~04)",
      "as_of": "2022",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f18",
      "claim": "병원 사례: Proof News(2026-06) 보도에 따르면 미국 MultiCare 계열 두 병원(Good Samaritan, Tacoma General)의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기에서 막혀 사람이 계속 따라다녀야 했고, 기존 기송관 설비가 있어 간호사들이 로봇의 쓸모에 의문을 제기했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1266"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "\"Why do we have the robot if we have a human with her all the time?\" (ICU 간호사 발언, 기사)",
      "as_of": "2026-06-09",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f19",
      "claim": "OMRON 은 버튼 하나를 눌러 지정 위치로 자율이동로봇(AMR)을 부르는 입출력 장치(Mobile I/O Box)를 제품으로 제시한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1268"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: \"used to summon an autonomous mobile robot (AMR) to a designated location by just pressing a button\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건",
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가)에 대해, 요청 창구 기술(작업 요청 API 스키마, 역할 기반 권한, 호출 버튼, 터치스크린, 프런트 경유 입력)과 사용자 측 운영 요구 표준(ANSI/A3 R15.08-3)·교시 작업 지침 법령은 있으나, 여러 제조사 로봇을 한 관제에서 운영할 때의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 확인하지 못했고, 사례에서는 전담 운영 조직을 두거나(한림대학교성심병원) 역할이 불분명해 저항이 생기는(호텔) 형태로 현장마다 따로 정해지는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1255",
        "ref-1256",
        "ref-1268",
        "ref-1265",
        "ref-1269",
        "ref-1261",
        "ref-1262",
        "ref-1260",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f3·f10·f11·f13·f14·f16·f17·f19 종합",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 40. 운영 절차·요청 창구에서 ROP가 직접 맡을 범위는 호출 버튼·단말·앱·업무 시스템 API 등 여러 요청 창구를 하나의 요청 형식(요청자·목적·시각·우선순위)으로 받는 접수 기능, 요청자·운영자·관리자 역할과 권한 정의, 요청 상태 알림, 임시 통제 구역 선언·해제의 요청자·승인·기한 기록, 교대 인수인계용 운영 상태 요약(열린 작업·폐쇄 구역·예외)의 제공과 기록으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1255",
        "ref-1256",
        "ref-1257",
        "ref-1258",
        "ref-1267",
        "ref-1264"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f4·f5·f6·f8·f16 종합",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f22",
      "claim": "연계 대상: 분류 원문 19장 기준으로 전자의무기록·호텔 객실 관리·제조 실행 시스템 같은 업무 시스템의 요청 발생, 병원·호텔의 인력 편성과 교대 근무 제도, 로봇 교시·정비 작업 지침(사업주·제조사 책임), 승강기·공동현관 제어는 각 업무 시스템·현장 조직·제조사·설비 업체가 맡으므로, ROP는 그 요청과 상태를 받아 작업·권한·경로 제약으로 연결하는 쪽을 맡는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1269",
        "ref-1265",
        "ref-1264",
        "ref-1260",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f10·f11·f16·f17 종합",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f23",
      "claim": "이 영역은 대화로 업무를 요청하는 12. 채팅으로 업무 지시·오케스트레이션(f1), 업무 시스템 요청을 받는 23. 업무 시스템 연동(f16·f22), 요청을 작업으로 바꾸는 24. 작업·워크플로 모델링과 25. 작업 배정 — MRTA(f1), 승강기·문 연동의 22. 설비·건물 시스템 연동(f16·f18), 임시 통제 구역의 16. 장소 의미·지도 관리(f4·f5), 인수인계 상태 표시의 37. 관제 화면·실행 기록(f9), 알림·에스컬레이션의 38. 모니터링·이상 탐지·원인 분석(f13), 이상 시 재가동 절차의 32. 예외 복구·재계획·업무 연속성과 48. 안전·위험 관리(f10), 요청 권한의 51. 인증·권한·격리(f2), 현장 협업의 31. 사람–로봇 협업(f12·f13), 운영 교육·전담 조직의 56. 운영 이관·확대·교육(f14·f17), 사용자 요구 표준의 50. 안전 표준·인증·사고 조사(f11), 부서·사업자 책임의 58. 다사업자 책임·계약·데이터(f17), 수용성의 60. 노동·수용성·접근성(f12·f17·f18), 적용 현장인 63. 병원·의료(f12~f15·f18)·64. 상업 시설(f16·f17)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1255",
        "ref-1256",
        "ref-1257",
        "ref-1263",
        "ref-1261",
        "ref-1262",
        "ref-1264",
        "ref-1260",
        "ref-1266",
        "ref-1269",
        "ref-1265"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1~f19 의 근거 영역 종합",
      "as_of": "2026-09-30",
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
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 명세 원문. 플릿 관제와 이동로봇 간 통신을 정의하며 프로젝트 조정·수행 절차는 범위 밖에 둔다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-1255",
      "org": "Open-RMF (open-rmf/rmf_api_msgs 저장소)",
      "title": "rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 작업 요청 JSON 스키마. category·description 필수, requester·labels·요청 시각·가장 이른 시작 시각·priority·fleet_name 선택.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
      "source_unopened": false
    },
    {
      "id": "ref-1256",
      "org": "Open-RMF (open-rmf/rmf-web 저장소)",
      "title": "rmf-web/packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 대시보드용 API 서버 설명. OpenID Connect JWT 인증, 역할·동작·권한 그룹 기반 권한, 데이터베이스 기록.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/packages/api-server/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1257",
      "org": "Open-RMF (open-rmf/rmf_internal_msgs 저장소)",
      "title": "rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 차선 열기·닫기 요청 메시지 정의. fleet_name, open_lanes, close_lanes 세 필드.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "source_unopened": false
    },
    {
      "id": "ref-1258",
      "org": "UK Health and Safety Executive (HSE) (humanfactors101.com 게재본)",
      "title": "Human Factors Briefing Note No. 8 — Safety-Critical Communications",
      "published": "2005",
      "url": "https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "HSE 인적 요인 지침. 교대 인수인계를 대면·양방향 대화·교대 일지·충분한 시간으로 하도록 권고. 제3자 사이트 게재본이라 medium.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1259",
      "org": "Brazier, A., & Pacitti, B. (IChemE Hazards XX)",
      "title": "Improving shift handover and maximising its value to the business",
      "published": "2008",
      "url": "https://www.icheme.org/media/9743/xx-paper-48.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "공정 산업 교대 인수인계의 실패 원인(정보 누락, 비구조화, 문서 부족)과 구조화된 일지·대면·양방향 대화·체크리스트 권고.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1260",
      "org": "Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management)",
      "title": "The perils of hotel technology: The robot usage resistance model",
      "published": "2022",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "중국 고급 호텔 직원 19명 면담으로 로봇 사용 저항 요인(역할·부서 소속 모호, 추가 업무, 사용성 등)을 도출.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1261",
      "org": "지디넷코리아",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원 커맨드센터의 7종 73대 서비스 로봇 운영, 2022-08~2024-05 누적 35,492건, RaaS 모델과 타 병원 확산 계획 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1262",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인)",
      "published": "2024-04",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원 커맨드센터가 7종 73대 로봇을 통합관제로 운영하며 시나리오 개발·업무 조율·모니터링·문제 대응을 맡는다는 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1263",
      "org": "Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008-03",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "병원 배송 로봇 TUG 의 15개월 민족지 연구. 병동별 업무 흐름·사회적·환경 요인에 따라 수용이 크게 달랐음. PDF 추출 품질이 낮아 medium.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1264",
      "org": "한국일보",
      "title": "“딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인)",
      "published": "2017-04-18",
      "url": "https://www.hankookilbo.com/news/article/201704180418820469",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "뉴욕 알로프트 호텔의 Savioke Relay 배송 로봇 운용 절차(프런트 전화 접수·직원 입력·승강기 연동·객실 전화 알림) 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1265",
      "org": "ANSI (The ANSI Blog)",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": null,
      "url": "https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 산업용 이동로봇 안전 요구사항 제3부(사용) 소개. 사용자 요구사항, 위험성평가, 응용·운영 환경 변경 관리, 2026-04-23 발행(검색 요약 기준).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1266",
      "org": "Proof News (Varsha Bansal)",
      "title": "Meet the Robot That Nurses Unplugged",
      "published": "2026-06-09",
      "url": "https://www.proofnews.org/moxi/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "MultiCare 계열 두 병원의 Moxi 로봇 운용 문제(길 잃음, 승강기 막힘, 상시 동행 필요)와 간호사 반응 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1267",
      "org": "Blazin, L. J. 외 (Pediatric Quality & Safety)",
      "title": "Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings",
      "published": "2020-07",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "I-PASS 구조화 인계를 여러 인계 상황에 적용한 연구. 원 연구(Starmer 외)의 오류 23%·예방 가능 유해 사건 30% 감소와 I-PASS 구성 요소를 서술.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1268",
      "org": "OMRON Industrial Automation Europe",
      "title": "Autonomous Mobile Robots (AMR)",
      "published": null,
      "url": "https://industrial.omron.eu/en/products/autonomous-mobile-robot",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "OMRON AMR 제품 페이지. 버튼으로 AMR 을 지정 위치로 부르는 Mobile I/O Box 와 MobilePlanner 소개.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1269",
      "org": "고용노동부 (국가법령정보센터)",
      "title": "산업안전보건기준에 관한 규칙 제222조(교시 등)",
      "published": "2025-09-01",
      "url": "https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "산업용 로봇 교시 등 작업 시 조작방법·속도·신호방법·이상 시 조치·재가동 조치 지침을 정하고 작업 중 표시를 하도록 한 조문(시행 2025-09-01 판).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
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
      "rationale": "섹션 3: f20(핵심 질문 답, 추정), f12·f17·f18(절차·역할이 불분명할 때의 문제) / 섹션 4: 작업 요청 스키마·요청자 f1, 역할 기반 권한 f2, 교대 인수인계 f6·f7, I-PASS f8, 호출 버튼 f19(벤더 주장 병기) / 섹션 5: 병원 — f12(예외·성과)·f13(시작 조건)·f14(수행 자원, 한국)·f15(시작 조건, 한국)·f18(예외·성과), 상업 시설 — f16(시작 조건)·f17(수행 자원). 제조 공장은 f10(법령)·f19(벤더 제품)뿐이고 물류창고·가정·실외 요청 창구 사례는 찾지 못했음을 명시 / 섹션 6: 요청 접수 형식 f1, 권한 f2, 구조화된 교대 인수인계 f6~f9, 전담 운영 조직 f14, 임시 통제 구역 절차 f4·f5 / 섹션 7: Open-RMF 작업 요청 API f1·f2, 차선 폐쇄 메시지 f4, VDA 5050 범위 f3, ANSI/A3 R15.08-3 f11(원문 미열람), 산업안전보건기준에 관한 규칙 제222조 f10, HSE 지침 f6 / 섹션 8: f6·f7·f8·f12·f17 / 섹션 9: f21(직접 범위), f22(연계 대상) / 섹션 10: f23 — 12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64 / 섹션 11: 기존 oq-203(f4·f5 로 부분 근거, 미해결 유지)과 open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f12·f14·f15·f18, 64. 상업 시설 페이지에 f16·f17 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "교대 인수인계",
      "term_en": "Shift Handover",
      "definition": "연속 운영 현장에서 나가는 근무조가 들어오는 근무조에게 설비·작업 상태와 위험 정보를 넘기는 절차로, 대면·양방향 확인과 교대 일지 기록이 권고된다."
    },
    {
      "term_ko": "I-PASS 인계 프로그램",
      "term_en": "I-PASS Handoff Program",
      "definition": "질병 중증도·환자 요약·할 일 목록·상황 인식과 비상 계획·수신자의 요약 확인 다섯 항목으로 의료진 인계를 구조화한 프로그램이다."
    },
    {
      "term_ko": "역할 모호성",
      "term_en": "Role Ambiguity",
      "definition": "로봇 같은 새 설비의 운영·정비 책임이 어느 부서·사람에게 있는지 불분명한 상태로, 추가 업무와 사용 저항의 원인으로 보고된다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 로봇을 한 관제에서 운영할 때 교대 인수인계로 넘길 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외)을 정한 공개 절차나 체크리스트가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 37. 관제 화면·실행 기록 | 근거: f9 | 종류: 일반",
    "병원·호텔에서 안내 데스크·프런트 담당자가 로봇 요청을 대신 입력하는 방식과 현장 사용자가 직접 요청하는 방식의 처리 시간·오류·업무 부담을 비교한 연구가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 63. 병원·의료, 64. 상업 시설 | 근거: f15 | 종류: 일반",
    "ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? | 관련 영역: 40. 운영 절차·요청 창구, 50. 안전 표준·인증·사고 조사, 58. 다사업자 책임·계약·데이터 | 근거: f11 | 종류: 일반",
    "로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 56. 운영 이관·확대·교육, 60. 노동·수용성·접근성 | 근거: f17 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 2,
    "unverified": [
      "oq-203 미해결: 임시 통제 구역 선언·승인·해제 절차를 공개한 병원·상업 시설 사례를 찾지 못함(f4·f5 로 부분 근거만)",
      "f11 ANSI/A3 R15.08-3-2026 은 ANSI 블로그·A3 상점 모두 403 으로 원문 미열람, 검색 요약 기준",
      "f8 I-PASS 원 연구(Starmer 외, NEJM 2014)는 NEJM·WUSTL 저장소 403 으로 열지 못해 2차 서술(Blazin 2020)만 근거로 씀 — 교차 확인 아님",
      "f13 Mutlu·Forlizzi PDF 추출 품질이 낮아 요청·인계 세부 절차 미확인",
      "f14 한림대학교성심병원 로봇 규모는 2024년 보도 기준 7종 73대이며, 2025년 보도 검색 요약에는 11종 77대로 나옴(시점 차이로 보이나 미확인, 출처로 넣지 않음)",
      "HSE 공식 사이트 교대 인수인계 페이지(communications.htm)는 열었으나 신규 출처 상한으로 넣지 않음. HSG256(교대 근무 관리) PDF 는 추출 실패",
      "ISO/IEC 20000-1:2018 서비스 요청 관리(8.6.3) 조항은 공식 자료를 열지 못해 넣지 않음",
      "Diligent Moxi 요청 창구(키오스크·문자·음성 버튼)는 기사 검색 요약에만 있고 벤더 페이지에서 확인되지 않아 넣지 않음",
      "가정(아파트 입주민 앱 로봇 호출) 사례는 기사 본문 확인이 불충분해 넣지 않음"
    ],
    "scope_violations": [
      "f10: 산업용 로봇 교시 작업 지침은 사업주·제조사의 로봇 작업 안전 절차로 원문 19장 '로봇 자체 지능·제어'·설비 안전 쪽에 가까워, ROP 직접 범위는 f21 에서 요청·권한·인수인계 기록으로 한정하고 f22 에서 연계 대상으로 구분함",
      "f16·f18: 승강기·기송관 등 설비 연동은 원문 19장 '시설·설비 제어' 연계 대상이며 요청 창구 사례의 맥락으로만 씀",
      "f6·f7·f8: 공정 산업·의료의 교대 인수인계 근거는 로봇 분야 자료가 아니므로 방법 참고로만 제안하고 로봇 관제 적용은 추정(f9)으로 둠"
    ],
    "budget_used": {
      "queries": 26,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 26회/30, 신규 출처 15건/15(ref-1255~ref-1269, 예약 구간 안)로 신규 출처 상한에 도달해 HSE 공식 페이지·NEJM 원 연구를 출처로 넣지 않았다. 재사용 1건(ref-031): 참고문헌 목록 요약에 행이 없어 값은 이전 브리프 2026-09-30-17 출처 표를 따랐고(요약 문장은 이번 확인 내용으로 작성), 이번에 GitHub 공식 저장소 원문을 다시 열어 사용자 요청 접수 방식이 범위 밖임을 확인했다. 원문 열람: 16건 중 15건을 열었고(github_raw 5, webfetch 10) ref-1265 만 403 으로 못 열어 source_unopened 로 표시했다. ref-1263·ref-1258·ref-1259 는 PDF 추출이 부분적이다. 교차 확인 2건(f6: HSE·Brazier, f14: 지디넷코리아·로봇신문). 벤더 주장 1건(f19). 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '요청 창구 기술과 사용자 측 운영 요구 표준·법령은 있으나 다중 제조사 관제의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 확인하지 못했고 현장마다 따로 정해진다'는 추정이다. 현장 유형 사례는 병원(f12~f15·f18, 한국 포함)·상업 시설(f16·f17)이며, 제조 공장은 법령(f10)과 벤더 제품(f19)뿐이고 물류창고·가정·실외·기타의 요청 창구 사례는 근거 있는 자료를 찾지 못했다. 국내 자료는 산업안전보건기준에 관한 규칙(ref-1269)·지디넷코리아·로봇신문·한국일보다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 서비스 수준 협약·역할 기반 접근 통제·차선 폐쇄·구역 집합·감독 제어·원격 조작은 후보로 내지 않았다. 기존 열린 질문 oq-203 은 부분 근거만 있어 해결 제안하지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md

```markdown
---
title: "40. 운영 절차·요청 창구"
type: area
category: "J. 현장 운영·관제"
area_no: 40
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [J. 현장 운영·관제](index.md) › 40. 운영 절차·요청 창구

# 40. 운영 절차·요청 창구

!!! info "소속 대분류"
    [J. 현장 운영·관제](index.md) — 핵심 질문:
    운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

운영 절차·교대, 현장 사용자의 요청 창구 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 절차·교대**: 운영 표준 절차, 교대 인수인계, 역할을 정한다
- **현장 사용자 요청 창구**: 간호사·객실 직원·거주자처럼 비전문 사용자가 호출 버튼·앱·단말로 일을 요청한다

## 2. 핵심 질문

현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? [분류원문]

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

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md (요약)

```markdown
# 37. 관제 화면·실행 기록

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **관제 화면**: 지도 위에 로봇·작업·설비·사람·물품 상태를 보여 주고 층을 골라 본다
- **설명 가능한 상태 표시**: 로봇이 지금 무엇을 왜 하고 있는지 운영자가 알아볼 수 있게 표시한다
- **실행 기록·재생**: 실행 기록을 저장하고 시간축으로 재생하며 사건을 찾아본다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’에서 왔다. 그 본문은 [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? [분류원문]
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

### docs/categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md (요약)

```markdown
# 39. 운영 성과 측정·개선

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-26 · 버전: 3

## 1. 한 줄 정의

지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 성과 측정**: 처리량·완료 시간·가동률·대기 시간·에너지 같은 지표를 정의하고 측정한다
- **로봇 성과와 업무 성과 구분**: 로봇 가동률이 올라간 것이 실제 업무 성과(처리량·서비스 시간·비용)로 이어졌는지 나눠 본다
- **운영 개선**: 측정 결과로 운영 정책·배치·절차를 고치고 효과를 다시 잰다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 4번 영역 ‘성과·경제성·프로세스 개선’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 [옛 분류원문]

> 옛 질문: 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? [옛 분류원문]

## 2. 핵심 질문

로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1123건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 313개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
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
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
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
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
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
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
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
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
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
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
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
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
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

### docs/open-questions.md (요약: 대상 영역 [40] 에 걸린 1건 / 전체 250건)

```markdown
- oq-203 [열림] 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (영역 16, 40, 63)
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

### runs/2026-09-30-17/research.md

```markdown
# 리서치 브리프 2026-09-30-17

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-17 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 36. 가상 시운전·실제 상황 재현 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 가상 시운전의 시험 구성(MiL·SiL·HiL), 에뮬레이션, 로그 재생·비반응 재생, 시뮬레이션–현실 상관 지표, 모델·시뮬레이션 신뢰도 평가 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·제조 공장·병원·기타 현장의 가상 시운전·재현 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 실행 전 계획 검증, 가상 시운전, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리의 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — VDI/VDE 3693, NASA-STD-7009, Open-RMF 시뮬레이션, rosbag2, VDA 5050 범위 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-132, oq-156 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]
2. 가상 시운전은 표준·문헌에서 어떻게 정의되고 어떤 시험 구성(MiL·SiL·HiL)을 쓰며, 분산 시스템·여러 로봇으로 어떻게 넓혀지는가? (섹션 4·6·7 겨냥)
3. 여러 로봇의 관제·오케스트레이션을 설치 전에 가상 환경에서 시험하는 도구와 현장 사례(물류창고·제조 공장·병원·기타)는 무엇인가? (섹션 5·7 겨냥, 한국 사례 우선)
4. 운영 기록(로그)으로 시뮬레이션의 초기 상태와 사건을 다시 구성하는 방법과 그 한계는 무엇인가? (섹션 6·8 겨냥)
5. 재현한 시뮬레이션이 실제 기록과 '맞는다'고 판정할 지표와 허용 기준, 승인 주체는 무엇인가? (oq-132, 섹션 6·11 겨냥)
6. 실행 전 계획 검증과 시뮬레이션 검증·실기 검증 단계에 대응하는 기존 검증 수준·신뢰도 평가 체계가 있는가? (oq-156, 섹션 6·7 겨냥)
7. 가상 시운전·재현에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·설비 업체·로봇 제조사에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDI/VDE 3693 Blatt 1 은 2025-05 개정판(39쪽, 독·영)에서 가상 시운전(virtual commissioning)을 체계적으로 정의하고 자동화 설비·기계의 수명주기 안에 위치시키며, 기본 시험 구성, 시험 방법, 필요한 모델 유형, 시뮬레이션 구성을 보완했다. | ref-1165 | 아니오 | medium | 2025-05 | — | — |
| f2 | [사실] | Rosenberger 외(Sensors 2023)는 VDI 3693 에 따라 가상 시운전 시험 구성을 자동화 모델만 쓰는 모델 인 더 루프(MiL), 실제 제어 언어 코드를 하드웨어와 분리해 돌리는 소프트웨어 인 더 루프(SiL), 실제 대상 하드웨어(가상 머신·컨테이너로 가상화한 하드웨어 포함)를 쓰는 하드웨어 인 더 루프(HiL)로 구분한다. | ref-1172 | 아니오 | medium | 2023-03-28 | — | — |
| f3 | [사실] | 제조 공장 사례: Rosenberger 외(Sensors 2023)는 가상 시운전을 제어 루프에서 분산 에지 컴퓨팅 시스템 전체로 넓혀, 물리 설비 시뮬레이션과 응용 사이의 직접 피드백 루프로 여러 장치를 함께 시험하는 구조 3가지를 제안하고, 끝단 팔레타이징 포장 설비 시뮬레이션에 실제 제어기 3대와 가상화 인스턴스 9대를 붙여 시험했으나, 시운전 기간·비용 절감 수치는 제시하지 않았고 비실시간 시뮬레이션이라는 한계를 밝혔다. | ref-1172 | 아니오 | medium | 2023-03-28 | 제조 공장 / 수행 자원 | — |
| f4 | [사실] | Open-RMF 의 시뮬레이션 문서는 traffic_editor 로 도면에 교통 정보·경유점·공유 자원을 주석한 뒤 building_map_generator 가 Gazebo·Ignition 세계와 플릿 어댑터용 주행 그래프를 자동 생성하고, 로봇(slotcar)·문·승강기·작업셀(디스펜서·인제스터)·군중(Menge) 플러그인으로 배치 전 시험, 로봇 추가 시 규모 평가, 드문 실패 상황 검토를 할 수 있다고 설명한다. | ref-1169 | 아니오 | medium | 2026-09-30 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 명세는 프로젝트 관리, 통합 방법, 시운전 작업 흐름, 검증·인수 절차를 포함하는 '프로젝트 조정·수행 절차'를 명세 범위 밖에 두므로, 이 인터페이스 규격을 따르는 것만으로 여러 제조사 로봇의 시운전 절차가 정해지지는 않는다. | ref-031 | 아니오 | medium | 2026-09-30 | — | — |
| f6 | [사실] | ROS 2 의 rosbag2 는 토픽 메시지를 시각과 함께 기록하고 재생하며, --clock 옵션으로 재생 세션 동안 /clock 을 발행해 재생 데이터에 맞춘 시뮬레이션 시각을 주고, 일시정지·재개·탐색·속도 조정·한 메시지씩 진행 같은 재생 제어 서비스를 제공하며 기본 저장 형식은 MCAP 이다. | ref-1166 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f7 | [사실] | 연계 대상: 자율주행 분야의 Waymax(Gulino 외, 2023)는 Waymo Open Motion Dataset 같은 실제 주행 기록으로 다중 에이전트 시나리오를 초기화하거나 재생하고, 단순 재생을 넘어 상호작용이 가능하도록 학습된 행동 모델과 규칙 기반 행동 모델을 함께 넣은 가속 시뮬레이터다. | ref-1168 | 아니오 | medium | 2023-10-12 | 실외 | — |
| f8 | [추정] | 기록된 궤적을 그대로 재생하는 방식은 주변 에이전트가 바뀐 조건에 반응하지 않으므로, 실제 운영 기록으로 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교하려면 주변 로봇·사람을 반응형 행동 모델로 바꾸는 단계가 필요할 것으로 보인다. | ref-1168, ref-1166 | 아니오 | low | 2026-09-30 | 예외·성과 | — |
| f9 | [사실] | Kadian 외(2020)는 시뮬레이션에서의 성능 개선이 실제 성능 개선으로 이어지는지를 재는 시뮬레이션–현실 상관 계수(SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 성공률 기준 SRCC 가 0.18 로 낮았던 원인이 에이전트가 충돌 동역학을 악용해 벽을 따라 미끄러지는 것임을 찾아 시뮬레이터 설정을 조정해 0.844 로 높였다. | ref-1167 | 아니오 | medium | 2020-08 | 예외·성과 | 원문 미열람 |
| f10 | [사실] | Aljalbout 외(2025)는 시뮬레이션이 추상화와 근사로 이루어져 현실과의 차이(현실 격차)를 피할 수 없다고 보고, 영역 무작위화, 현실→시뮬레이션 전이, 상태·행동 추상화, 시뮬레이션–현실 공동 학습 같은 대응 기법과 현실 격차 평가 지표를 정리했다. | ref-1174 | 아니오 | medium | 2025-10-23 | — | — |
| f11 | [의견] | Luckcuck 외(ACM Computing Surveys 2019)는 자율 로봇이 복잡하고 혼성적이며 안전에 중요한 시스템이어서 시험과 시뮬레이션만으로는 정확성을 보장하거나 인증에 충분한 증거를 내기 어렵다고 보고, 형식 명세·검증 기법을 보완 수단으로 정리했다. | ref-1173 | 아니오 | medium | 2019 | — | — |
| f12 | [사실] | NASA-STD-7009B '모델·시뮬레이션 표준'(문서일 2024-03-05, 현행)은 모델·시뮬레이션을 개발·수용·사용하는 요구·권고·기준을 정하고, 개정판에서 개발·사용 단계의 신뢰도 평가 산출물에 초점을 두며, 결과를 쓰기 전에 수용 기준을 위임된 기술 권한자가 정의·승인하도록 한다. | ref-1177 | 아니오 | medium | 2024-03-05 | — | — |
| f13 | [사실] | 병원 사례: 고려대학교 구로병원의 약품 배송 로봇 연구(Lee 외, Digital Health 2026-03)는 2025-06-18~29 의 실제 배송 122건에서 로봇 원격측정 기록과 승강기 시스템 데이터를 모아 승강기 가동률(EOR) 59.01% 를 임계값으로 찾았고(이하에서 배송 성공률 95.5%, 90% 초과에서 실패 집중), 측정한 점유율로 모수를 정한 몬테카를로 시뮬레이션으로 승강기 탑승 실패 기제를 재현했다. | ref-1170 | 아니오 | medium | 2026-03 | 병원 / 예외·성과 | — |
| f14 | [의견] | 같은 연구의 저자들은 여러 병원 시험이 어려울 때 병원별 구조·통행 구성·승강기 제어 정책을 재현한 병원 디지털 트윈으로 현장 배치 전에 결과의 일반화 가능성을 부하 시험할 수 있다고 제안하고, 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰자고 했다. | ref-1170 | 아니오 | medium | 2026-03 | 병원 / 제약 | — |
| f15 | [추정] | 물류창고 사례(벤더 주장): Rockwell Automation 사례 소개에 따르면 통합자 Bastian Solutions 는 미국 남부의 약 30만 제곱피트 규모 물류센터 구축에서 컨베이어·피킹 모듈·PLC·I/O 매핑·제어 코드를 에뮬레이션으로 설치 전에 검증해 전체 프로젝트 기간을 18% 줄이고 현장 시운전을 5주 단축했다고 한다. | ref-1179 | 아니오 | low | 2024-08-28 | 물류창고 / 예외·성과 | 벤더 주장 |
| f16 | [사실] | 제조 공장 사례: 최성욱·박상철·왕지남(2008, 대한산업공학회 추계학술대회)은 자동차 차체 생산라인의 PLC 코드를 검증하려고 설비 상태·사건을 이산 사건 모델로 정의하고, 실제 PLC 하드웨어와 3D CAD·디지털 목업 기반 가상 공정 시뮬레이터를 양방향 통신으로 연동하는 가상 플랜트 구축 절차를 제안해 라인 안정화 기간과 비용을 줄이는 것을 목표로 했다. | ref-1175 | 아니오 | medium | 2008-11 | 제조 공장 / 작업 대상 | — |
| f17 | [추정] | 제조 공장 사례(벤더 주장): 현대자동차그룹은 싱가포르 혁신센터(HMGICS)에서 디지털 트윈 가상 공장으로 설비·로봇 배치 변경을 실제 생산을 멈추지 않고 가상에서 먼저 검증한다고 소개하나, 시운전 기간 단축 같은 수치는 밝히지 않았다. | ref-1176 | 아니오 | low | 2023-11-21 | 제조 공장 / 제약 | 벤더 주장 |
| f18 | [사실] | 기타(대학 건물) 사례: Ortega 외(Frontiers in Robotics and AI 2024-08)는 도면 DSL 로 만든 실내 환경, 동적 객체의 초기 자세, 시간·거리 조건으로 움직이는 문 같은 동적 요소, 주행 과제, 위치 추정 오차·충돌 회피 같은 수용 기준을 조합해 실행 가능한 이동로봇 시험 시나리오를 만드는 방법을 제안하고, 실측 점유 격자로 모델링한 대학 건물 1층에서 평가했으나 현장 기록의 재생은 다루지 않았다. | ref-1178 | 아니오 | medium | 2024-08-02 | 기타 / 완료·인계 | — |
| f19 | [사실] | VirTooS(Drudi 외, 2026-08 arXiv)는 ROS 2 와 Unity 를 결합해 실제 로봇과 가상 로봇이 같은 환경에서 상호작용하는 혼합 현실 실험으로 자율이동로봇(AMR) 플릿 관리(작업 배정) 전략을 시험하는 도구로, 가상·실제 센서를 함께 쓸 수 있으나 초록에는 정량 결과가 없다. | ref-1171 | 아니오 | medium | 2026-08-26 | 수행 자원 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(설치 전에 가상으로 시운전하고 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가)에 대해, 설치 전 가상 시운전은 제조·물류 설비 제어 분야에서 VDI/VDE 3693 과 MiL·SiL·HiL 구성으로 정립되어 있고 다중 로봇 쪽에는 Open-RMF 시뮬레이션·혼합 현실 도구가 있으며, 운영 기록 재생 도구(rosbag2)와 기록 기반 시나리오 초기화(Waymax)도 있지만, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차 표준과 재현 결과의 현실 일치 판정 기준은 확인하지 못했다. | ref-1165, ref-1172, ref-1169, ref-1171, ref-1166, ref-1168, ref-031, ref-1167 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 재현 시뮬레이션의 현실 일치 판정(oq-132)에는 비교한 여러 설정의 시뮬레이션 성능과 실제 성능 사이 상관을 보는 SRCC 같은 예측력 지표와, 결과 사용 전에 수용 기준을 권한자가 정의·승인하게 하는 NASA-STD-7009B 방식, 시나리오마다 수용 기준을 명시하는 방식을 조합할 수 있을 것으로 보이나, 로봇 플릿 재현에 이를 적용해 허용 기준을 정한 사례는 찾지 못했다. | ref-1167, ref-1177, ref-1178 | 아니오 | low | 2026-09-30 | 완료·인계 | — |
| f22 | [추정] | 분류 원문의 지원 단계 표시 가운데 시뮬레이션 검증·실기 검증 단계(oq-156)는 VDI/VDE 3693 의 MiL·SiL·HiL 시험 구성과 NASA-STD-7009B 의 신뢰도 평가에 부분적으로 대응시킬 수 있을 것으로 보이나, 문서 확인·구조화·어댑터 연결까지 이어지는 단계를 한 체계로 정한 기존 성숙도 체계는 이번 조사에서 찾지 못했다. | ref-1165, ref-1172, ref-1177 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 36. 가상 시운전·실제 상황 재현에서 ROP가 직접 맡을 범위는 제조사 플릿·문·승강기 인터페이스의 가상 대응물을 붙여 오케스트레이션 논리와 운영 정책을 설치 전에 SiL 방식으로 시험하는 환경, 재생 가능한 형태로 시각이 맞춰진 오케스트레이션 수준 실행 기록, 기록에서 시뮬레이션 초기 상태와 사건을 구성하는 기능, 재현 결과와 실제의 차이 지표와 수용 승인 기록의 관리로 보인다. | ref-1169, ref-1166, ref-1172, ref-1167, ref-1177, ref-031 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 시뮬레이션 자산, 로봇 내부 주행·인식 제어의 현실 격차 보정은 시뮬레이션 도구·로봇 제조사가, 컨베이어·PLC·승강기 제어 코드의 에뮬레이션과 가상 시운전은 설비 업체·통합자가, 자율주행 차량의 기록 기반 시뮬레이션은 해당 업계가 맡으므로, ROP는 이들의 가상 모델·에뮬레이터와 연결되는 인터페이스와 시험 결과를 받아 들이는 쪽을 맡는 것으로 보인다. | ref-1172, ref-1175, ref-1179, ref-1174, ref-1168, ref-1169 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f25 | [추정] | 이 영역은 시나리오 형식의 33. 시나리오 모델·편집(f18), 시뮬레이션 엔진과 가정한 미래 실험의 34. 시뮬레이션·예측용 디지털 트윈(f4·f10), 재현의 원천 기록을 주는 18. 실시간 세계 상태·데이터 일관성과 37. 관제 화면·실행 기록(f6), 대화로 재현을 요청하는 11. 채팅으로 실제 상황 시뮬레이션 재현, 도면에서 시뮬레이션 세계를 만드는 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f4), 플릿 어댑터의 20. 로봇·제조사 관제 연동(f4·f5), 문·승강기의 22. 설비·건물 시스템 연동(f4·f13), 배차 정책의 25. 작업 배정 — MRTA(f13·f19), 원인 분석의 38. 모니터링·이상 탐지·원인 분석(f13), 계획 검증·형식 검증의 54. 시험·형식 검증·벤치마크(f11·f12), 현장 시운전의 55. 현장 조사·설치·시운전(f1·f15), 현실 격차 보정 학습의 47. AI·학습·적응과 모델 운영(f10), 적용 현장인 61. 물류창고(f15)·62. 제조 공장(f3·f16·f17)·63. 병원·의료(f13·f14)·67. 기타 현장(f18)과 이어진다. | ref-1178, ref-1169, ref-1174, ref-1166, ref-031, ref-1170, ref-1171, ref-1173, ref-1177, ref-1165, ref-1179, ref-1172, ref-1175, ref-1176 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1165 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions | 2025-05 | 표준 | high | 2026-09-30 | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions | 아니오 |
| ref-1166 | ROS 2 (Open Robotics 외, ros2/rosbag2 저장소) | rosbag2 README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/ros2/rosbag2 | 아니오 |
| ref-1167 | Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L) | Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance? | 2020-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1912.06321 | 예 |
| ref-1168 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 2023-10-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2310.08710 | 아니오 |
| ref-1169 | Open Robotics | Simulation — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-1170 | Lee 외 (Digital Health, SAGE) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-1171 | Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv) | VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots | 2026-08-26 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2608.26066 | 아니오 |
| ref-1172 | Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545) | Virtual Commissioning of Distributed Systems in the Industrial Internet of Things | 2023-03-28 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/ | 아니오 |
| ref-1173 | Luckcuck, M., Farrell, M., Dennis, L., Dixon, C., & Fisher, M. (ACM Computing Surveys 52(5)) | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 2019 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1807.00048 | 아니오 |
| ref-1174 | Aljalbout, E., Xing, J., Romero, A. 외 (arXiv) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 2025-10-23 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2510.20808 | 아니오 |
| ref-1175 | 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회) | 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스 | 2008-11 | 논문 | medium | 2026-09-30 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794 | 아니오 |
| ref-1176 | 현대자동차그룹 | 가상의 디지털 공간에 세운 쌍둥이 공장 | 2023-11-21 | 벤더 문서 | low | 2026-09-30 | https://www.hyundaimotorgroup.com/ko/story/CONT0000000000122330 | 아니오 |
| ref-1177 | NASA | NASA-STD-7009B Standard for Models and Simulations | 2024-03-05 | 표준 | high | 2026-09-30 | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 | 아니오 |
| ref-1178 | Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI) | Composable and executable scenarios for simulation-based testing of mobile robots | 2024-08-02 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1363281/full | 아니오 |
| ref-1179 | Rockwell Automation | Emulation Technology Speeds Up Warehouse Automation | 2024-08-28 | 벤더 문서 | low | 2026-09-30 | https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f20(핵심 질문 답, 추정), f5(규격이 시운전 절차를 정하지 않음), f11(시험·시뮬레이션만으로는 증거 부족이라는 의견) / 섹션 4: 가상 시운전 정의 f1, MiL·SiL·HiL f2, 로그 재생·/clock f6, 비반응 재생 f8(추정), SRCC f9, 현실 격차 f10, 신뢰도 평가·수용 승인 f12 / 섹션 5: 물류창고 — f15(예외·성과, 벤더 주장 병기), 제조 공장 — f3(수행 자원)·f16(작업 대상: PLC 코드)·f17(벤더 주장 병기), 병원 — f13(예외·성과: 실제 기록 기반 승강기 실패 재현)·f14(제약, 의견), 기타(대학 건물) — f18(완료·인계: 수용 기준). 상업 시설·가정·실외 로봇 현장 사례는 찾지 못했음을 명시(f7 은 자율주행 방법 참고로만) / 섹션 6: 실행 전 계획 검증 f11, 가상 시운전 f1~f4·f19, 운영 기록 기반 재현 f6~f8·f13, 시뮬레이션–현실 차이 관리 f9·f10·f21 / 섹션 7: VDI/VDE 3693 f1, NASA-STD-7009B f12, Open-RMF 시뮬레이션 f4, rosbag2·MCAP f6, VDA 5050 범위 f5, Waymax f7, VirTooS f19 / 섹션 8: f3·f9·f10·f11·f13·f16·f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 11, 14, 15, 18, 20, 22, 25, 33, 34, 37, 38, 47, 54, 55, 61, 62, 63, 67. 18. 실시간 세계 상태·데이터 일관성은 재현의 원천 기록, 34. 시뮬레이션·예측용 디지털 트윈은 가정한 미래 실험으로 구분해 서술 / 섹션 11: 기존 oq-132(f21 로 부분 근거)·oq-156(f22 로 부분 근거) 미해결 유지와 open_questions_new 4건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f13·f14, 55. 현장 조사·설치·시운전 페이지에 f1·f2·f15 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 소프트웨어 인 더 루프 | Software-in-the-Loop (SiL) | 실제 제어 언어로 작성한 제어 프로그램을 대상 하드웨어 없이 가상 제어기에서 돌려 설비 시뮬레이션 모델과 연결해 시험하는 가상 시운전 구성이다. |
| 하드웨어 인 더 루프 | Hardware-in-the-Loop (HiL) | 나중에 현장에 쓸 실제 제어 하드웨어(또는 그 가상화 인스턴스)를 설비 시뮬레이션 모델과 연결해 제어 프로그램과 하드웨어·통신을 함께 시험하는 가상 시운전 구성이다. |
| 시뮬레이션–현실 상관 계수 | Sim-vs-Real Correlation Coefficient (SRCC) | 여러 방법·설정을 비교할 때 시뮬레이션에서의 성능 차이가 실제 로봇에서의 성능 차이와 얼마나 같은 방향으로 나타나는지를 상관계수로 재는 시뮬레이션 예측력 지표다. |
| 모델·시뮬레이션 신뢰도 평가 | Models and Simulations Credibility Assessment (NASA-STD-7009) | 모델·시뮬레이션 결과를 의사결정에 쓰기 전에 검증·타당성 확인 등 신뢰도 요소를 평가하고 미리 승인된 수용 기준과 대조하는 절차다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇 플릿을 지휘하는 플랫폼 수준에서 VDI/VDE 3693 의 MiL·SiL·HiL 구성을 적용해 오케스트레이션 논리와 플릿 어댑터를 설치 전에 가상 시운전한 절차나 공개 사례가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 20. 로봇·제조사 관제 연동, 55. 현장 조사·설치·시운전 | 근거: f1 | 종류: 일반
- 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 19. 사람·보행자 모델, 33. 시나리오 모델·편집 | 근거: f8 | 종류: 일반
- 물류창고·공장 가상 시운전의 효과(프로젝트 기간·현장 시운전 기간 단축)를 벤더 사례가 아닌 독립 연구가 같은 기준선으로 측정한 결과가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 3. 경제성·조달·사업 모델 | 근거: f15 | 종류: 일반
- 한 병원의 실제 기록으로 찾은 승강기 가동률 임계값 같은 운영 기준이 다른 병원 구조·승강기 제어 정책을 재현한 시뮬레이션에서도 유지되는지 검증한 연구가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 63. 병원·의료, 22. 설비·건물 시스템 연동 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 19회 · 신규 출처 15건
- 미확인 항목:
    - oq-132 미해결: 로봇 플릿 재현에 사건 순서 유사도·시각 오차·처리량 오차 지표와 허용 기준을 적용한 자료를 찾지 못함(f21 로 후보만 제시)
    - oq-156 미해결: 문서 확인→구조화→시뮬레이션 연결→어댑터 연결→시뮬레이션 검증→실기 검증을 한 체계로 정한 기존 성숙도 체계를 찾지 못함(f22)
    - NASA-STD-7009 신뢰도 평가 척도(요소 8개, 0~4 점수, 전체 신뢰도는 최저 점수)는 검색 요약에만 있어 넣지 않음
    - Striffler·Voigt(2023) 가상 시운전 종합 리뷰(Journal of Manufacturing Systems 71)는 ScienceDirect 403 으로 열지 못해 넣지 않음
    - Kulkarni(IISE) 창고 로봇 가상 시운전 논문 소개 페이지 403, Siemens Ferrero·Wipro PARI 사례는 신규 출처 상한으로 넣지 않음
    - VAL(PDDL 계획 검증기) 논문 PDF 추출 실패, 공식 저장소 README 에 검증 항목 설명이 없어 실행 전 계획 검증의 전용 근거를 넣지 못함
    - Waymax 의 로그 재생 대 IDM 반응형 에이전트 모드 구분은 검색 요약에만 있어 초록 범위로 한정(f7)
    - f15 Bastian Solutions 수치(18%, 5주)는 벤더 주장이며 측정 방법·기준선 미확인
    - f17 현대자동차그룹 콘텐츠 제목은 검색 결과 제목 기준, 정량 수치 없음
    - f16 최성욱 외 2008 논문은 초록만 확인
    - f9·f10·f11 은 arXiv 초록만 확인
    - 상업 시설·가정·실외 로봇 현장의 가상 시운전·재현 사례를 찾지 못함
    - 국내 가상 시운전 표준(KS)이나 공공 지침은 찾지 못함
- 범위 경계 위반 의심:
    - f3·f15·f16: PLC·컨베이어 제어 코드의 가상 시운전은 원문 19장 '시설·설비 제어' 연계 대상이므로 방법 근거로만 쓰고 f24 에서 '연계 대상: '으로 구분함
    - f7: 자율주행 차량 기록 기반 시뮬레이션은 원문 19장 '업종별 조건'(실외 차량) 연계 대상이므로 claim 을 '연계 대상: '으로 시작하고 재현 방법의 참고로만 제안함
    - f9·f10: 로봇 주행·조작 정책의 현실 격차 보정은 원문 19장 '로봇 자체 지능·제어' 연계 대상이며, ROP 에는 예측력 지표 개념만 가져오는 것으로 f23·f24 에서 구분함
- 한계: web_fetch_available: true · fetch_mode full. 검색 19회/30, 신규 출처 15건/15(ref-1165~ref-1179, 예약 구간 안)로 신규 출처 상한에 도달해 Siemens Ferrero·Wipro PARI 가상 시운전 사례, Siemens Plant Simulation AGV 가상 시운전 블로그, Striffler·Voigt 리뷰를 출처로 넣지 못했다. 재사용 1건(ref-031): 값은 이전 브리프 2026-09-30-14 출처 표를 따랐고 이번에 GitHub 공식 저장소 원문을 다시 열어 시운전·검증·인수 절차가 범위 밖임을 확인했다. 원문 열람: 16건 모두 열었으나(webfetch 13, github_raw 3) ref-1167·ref-1168·ref-1171·ref-1173·ref-1174 는 arXiv 초록, ref-1175 는 DBpia 초록, ref-1165·ref-1177 은 표준 공식 소개 페이지만 읽었다. ScienceDirect·CRB·Strathprints PDF·IEEE CSDL 은 열지 못했다. 교차 확인 0건(주장마다 독립 출처 2곳을 찾지 못함). 벤더 주장 2건(f15·f17)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '설치 전 가상 시운전은 설비 제어 분야에서 표준·시험 구성이 정립되어 있고 다중 로봇 시뮬레이션·기록 재생 도구도 있으나, 여러 제조사 플릿 전체의 가상 시운전 절차 표준과 재현 결과의 현실 일치 판정 기준은 확인하지 못했다'는 추정이다. 현장 유형 사례는 물류창고(f15, 벤더)·제조 공장(f3·f16·f17)·병원(f13·f14, 한국)·기타(f18, 대학 건물)이며 상업 시설·가정은 찾지 못했고 실외는 자율주행 방법 참고(f7)뿐이다. 국내 자료는 고려대 구로병원 연구(ref-1170), 아주대 학술대회 논문(ref-1175), 현대자동차그룹 콘텐츠(ref-1176)다. 18. 실시간 세계 상태·데이터 일관성은 재현의 원천 기록으로, 34. 시뮬레이션·예측용 디지털 트윈은 엔진·가정한 미래 실험으로 구분해 f25 에 적었다. L. AI·학습 기술 관련은 현실 격차 보정 학습(f10)을 47. AI·학습·적응과 모델 운영과 함께 제안했다. 용어집에 이미 있는 가상 시운전·로그 재생·현실 격차·시나리오 재구성·사전 실행 계획 검증·백 파일·MCAP·디지털 섀도·시뮬레이션 모델 검증·타당성 확인·승강기 가동률은 후보로 내지 않았다. 기존 열린 질문 oq-132·oq-156 은 부분 근거(f21·f22)만 있어 해결 제안하지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-30-16/research.md

```markdown
# 리서치 브리프 2026-09-30-16

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-16 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 53. 개인정보·영상 데이터 |
| 대분류 | N. 보안·개인정보 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 이동형 영상정보처리기기, 촬영 거부(opt-out), 가명처리, 얼굴 가림, 작업 한정 인지 출력 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정(로봇청소기)·병원·실외(배달로봇) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 촬영 표시, 검출 후 블러, 명세 기반 실시간 가림, 촬영 시점 저해상도화, 출력 필드 축소의 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 개인정보 보호법 제25조의2, 이동형 영상정보처리기기 안내서, 가명정보 처리 가이드라인, EDPB 영상 장치 지침, EgoBlur 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-143, oq-171, oq-181, oq-185, oq-211, oq-214, oq-228 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
2. 한국 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)와 개인정보보호위원회 안내서는 로봇 카메라 촬영에 무엇을 요구하며, 병원·가정 내부 촬영에는 어떻게 적용되는가? (섹션 4·7 겨냥, oq-171, oq-181)
3. 로봇 영상을 인공지능 학습·사고 조사 등 다른 목적으로 쓸 때 가명처리·원본 활용 조건은 무엇인가? (섹션 6·7 겨냥, oq-228)
4. 로봇 영상에서 얼굴 등 식별 정보를 가리거나 처음부터 적게 모으는 기술(검출 후 블러, 명세 기반 가림, 저해상도 촬영, 출력 필드 축소)은 무엇이고 한계는 무엇인가? (섹션 6·8 겨냥)
5. 현장 유형별로 로봇 영상 유출·보안 취약점·보호 조치 사례는 무엇이 보고되었는가? (섹션 3·5 겨냥, 가정·병원·실외, 한국 사례 우선)
6. 영상·위치 데이터 보호에서 ROP가 직접 맡을 것과 제조사·운영 사업자·규제기관에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥, oq-211)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 한국 개인정보 보호법상 이동형 영상정보처리기기는 사람이 신체에 착용·휴대하거나 이동 가능한 물체에 부착해 사람 또는 사물의 영상을 촬영하는 장치로, 개인정보보호위원회는 스마트안경·드론·자율주행차 등을 예로 들고 로봇을 같은 범주의 기기로 안내한다. | ref-1138, ref-1135 | 아니오 | medium | 2026-09-30 | 수행 자원 | — |
| f2 | [사실] | 개인정보 보호법 제25조의2는 업무 목적으로 공개된 장소에서 이동형 영상정보처리기기로 사람을 촬영하는 것을 원칙적으로 제한하되, 동의 등 제15조제1항의 경우와 촬영 사실을 명확히 표시했는데도 정보주체가 거부 의사를 밝히지 않은 경우 등을 허용하고, 촬영 시 불빛·소리·안내판 등으로 촬영 사실을 표시하게 하며, 목욕실 등 사생활 침해 우려가 큰 장소에서의 촬영은 금지한다. | ref-1138, ref-1136 | 예 | high | 2026-09-30 | 제약 | — |
| f3 | [사실] | 개인정보보호위원회는 2024-10-14 '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.)'를 게시해, 제25조의2 신설에 따라 공개된 장소에서 업무 목적으로 이동형 기기로 개인을 알아볼 수 있는 영상을 촬영할 수 있는 경우와 수집·이용 시 준수할 보호·활용 기준을 제시했다. | ref-1135, ref-1137 | 예 | high | 2024-10-14 | — | — |
| f4 | [사실] | 같은 안내서는 촬영 거부를 사전 차단 권리가 아닌 선택 해제(opt-out) 방식으로 설명해 기본적으로 촬영하되 피촬영자가 명확히 거부하면 운영자가 받아들이게 하고, 촬영 사실 표시는 불빛·소리·안내판·안내서면·안내방송 등 기기 특성에 맞는 다중 채널 방식을 권장하며, 기획·설계 단계부터 목적 명확화와 최소 수집, 보관·파기 단계의 보유기간 설정과 영상정보 보호책임자 지정·운영방침 공개를 요구한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f5 | [사실] | 같은 안내서는 안전 주행 목적으로 촬영된 사고 영상을 사고 원인 파악·보험 처리에 이용·제공하는 것은 당초 수집 목적과 관련성이 있다고 보지만, 동의 없이 인공지능 학습에 쓰는 것은 정보주체의 예측 가능성이 없어 허용되지 않는다고 설명한다. | ref-1136 | 아니오 | medium | 2026-09-30 | 완료·인계 | — |
| f6 | [사실] | 같은 안내서는 고속으로 이동하며 촬영해 거부 의사를 파악하기 어려운 기기의 영상을 자율주행 인공지능 개발 등에 쓸 때 얼굴 모자이크 같은 익명·가명처리를 하도록 권고하고, 연구 목적상 원본이 불가피하면 규제샌드박스 실증특례를 검토하게 한다. | ref-1136, ref-1137 | 예 | medium | 2024-10-14 | 작업 대상 | — |
| f7 | [사실] | 실외 사례: 안내서 공개 보도는 카메라를 단 자율주행차와 배달로봇이 차량·로봇 외부에 촬영 사실과 구체적 내용을 표시해야 하고, 영상 처리를 위탁할 때는 보호책임자 지정과 정기 점검이 필요하다고 전한다. | ref-1137 | 아니오 | medium | 2024-10-14 | 실외 / 제약 | — |
| f8 | [사실] | 개인정보보호위원회는 2023-11 자율주행차와 이동형 로봇 서비스 고도화 목적에 한해 영상정보 원본 활용 규제샌드박스 실증특례를 본격 운영하고 그해 안에 9개 기업 승인을 추진한다고 발표했다. | ref-1139 | 아니오 | medium | 2023-11-15 | 제약 | — |
| f9 | [사실] | 개인정보보호위원회는 2024-02 가명정보 처리 가이드라인을 개정해 이미지·영상·음성·텍스트 같은 비정형 데이터를 포함시켰고, 처리 목적·환경·민감도에 따른 식별 위험 판단, 적용 기술의 신뢰성 문서화와 처리 후 자체 검증을 요구하며, 영상·이미지 처리 방법으로 필터링·암호화·합성 얼굴·인페인팅·AI 기반 처리를 제시한다. | ref-1140 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f10 | [사실] | 가정 사례: 한국소비자원과 한국인터넷진흥원이 로봇청소기 6종을 모바일앱 보안·정책 관리·기기 보안으로 나눠 점검한 결과, 나르왈·드리미·에코백스 3개 제품은 사용자 인증 절차가 미비해 집 내부 사진이 외부로 노출되거나 카메라가 강제로 활성화될 수 있었고, 삼성전자·LG전자 제품은 접근 통제와 업데이트 체계가 양호했다. | ref-1141 | 아니오 | low | 2025-09-02 | 가정 / 예외·성과 | — |
| f11 | [사실] | 가정 사례: 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 사업자 점검에서는 영상·음성·사진의 개인정보 침해 위험이 확인되지 않았고, 실시간 영상은 암호화해 사용자 앱으로 직접 보내고, 음성 명령은 서버에 저장하지 않으며, 장애물 인식 사진은 임시 저장 뒤 24시간 안 또는 다음 청소 뒤 삭제하는 방식이 확인되었으나, 동의와 계약 이행 처리의 구분, 서비스 개선용 수집의 사전 거부 선택권, 국외 이전 고지, 국내대리인 지정은 미흡했다. | ref-1142 | 아니오 | low | 2026-09-14 | 가정 / 예외·성과 | — |
| f12 | [사실] | 가정 사례: MIT Technology Review 조사에 따르면 카메라를 단 개발용 로봇청소기(iRobot Roomba J7 계열)가 시험 가정에서 찍은 화장실의 여성, 미성년자 등 사적 장면의 스크린샷 15장이 학습 데이터 라벨링 위탁(Scale AI의 해외 계약 작업자)을 거쳐 SNS에 유출되었고, iRobot은 Scale AI에 200만 장 넘는 이미지를 공유했으며 시험 참가자 동의와 녹화 중 표시 스티커를 근거로 들었다. | ref-1143 | 아니오 | medium | 2022-12-19 | 가정 / 예외·성과 | — |
| f13 | [사실] | Meta Reality Labs의 EgoBlur(arXiv 2023)는 1인칭 영상에서 행인 얼굴과 차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델을 공개했다. | ref-1144 | 아니오 | medium | 2023-08-24 | 작업 대상 | — |
| f14 | [사실] | Choi 외(arXiv 2025)의 PCVS 는 '사람이 있을 때 얼굴을 보이지 않는다' 같은 논리 명세로 가릴 대상을 정하고 프레임마다 검출과 등각 예측으로 명세 만족 확률의 하한을 보장하며 실시간으로 가리는 방법으로, 여러 데이터셋에서 95% 넘는 명세 만족을 보였고 가린 영상으로도 로봇이 정상 동작함을 확인했다고 보고했다. | ref-1145 | 아니오 | medium | 2025-05-08 | 작업 대상 | — |
| f15 | [사실] | Huang·Pan·Reinhardt·Bennewitz(arXiv 2026)는 카메라를 단 이동 서비스 로봇에 관한 두 차례 사용자 연구에서 사용자가 시각적 추상화와 촬영 시점 저해상도화를 선호하고 원하는 해상도가 요구 프라이버시 수준과 로봇과의 거리에 따라 달라진다는 결과를 얻어, 사용자가 설정하는 거리–해상도 프라이버시 정책을 제안했다. | ref-1146 | 아니오 | medium | 2026-04-07 | 제약 | — |
| f16 | [사실] | Xu·Ayday(arXiv 2026-09)는 가정용 로봇이 원본 대신 계획기·클라우드·로그·학습 파이프라인으로 내보내는 작업 한정 인지 출력 3종이 과업 성공(1.000)과 경로 효율(0.898)은 같아도 표현 수준 연결 가능성이 0.532~0.970으로 크게 다르고, 목표 레이블을 공간 영역으로 바꾸면 목표 범주 추정 정확도가 0.077로 떨어지면서 과업 성공은 0.995를 유지했다고 보고하며, 필드 제거나 추상화가 보편적으로 더 안전하지 않아 과업별 평가가 필요하다고 결론지었다. | ref-1147 | 아니오 | medium | 2026-09-02 | 작업 대상 | — |
| f17 | [사실] | 병원 사례(모의): HRI 2026 컴패니언 논문은 의사·환자를 알아보도록 학습한 얼굴 인식으로 대상이 아닌 사람의 얼굴을 가리는 서비스 로봇을 진료실 모의 시나리오로 실험해, 대상이 아닌 사람은 안정적으로 가려졌으나 자세 변화·가림·조명 변화가 인식 신뢰도를 낮춰 보호에 한계가 있음을 보고했다. | ref-1148 | 아니오 | medium | 2026-03 | 병원 / 작업 대상 | 원문 미열람 |
| f18 | [사실] | 유럽데이터보호이사회(EDPB)는 GDPR 을 영상 장치의 개인정보 처리에 적용하는 지침 3/2019 최종판을 2020-01 채택해 처리의 적법 근거, 투명성, 정보주체 권리, 기술적 보호조치를 다룬다. | ref-1149 | 아니오 | medium | 2020-01 | 제약 | — |
| f19 | [추정] | 로봇 영상 유출 사례(f12)와 안내서의 위탁 처리 요구(f7)를 보면, 로봇 영상은 촬영 장치보다 학습·라벨링 위탁 같은 이차 이용 경로에서 유출 위험이 커지므로, 영상을 모으는 쪽은 이차 이용 목적과 위탁 사슬의 접근 범위를 수집 시점부터 정해 둘 필요가 있는 것으로 보인다. | ref-1143, ref-1137, ref-1136 | 아니오 | low | 2026-09-30 | 예외·성과 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가)에 대해, 한국에서는 공개된 장소의 로봇 촬영에 촬영 사실 표시와 거부 의사 수용이 요구되고 이차 이용(특히 인공지능 학습)에는 가명처리나 별도 특례가 필요하며, 기술적으로는 검출 후 가림, 명세 기반 실시간 가림, 촬영 시점 저해상도화, 출력 필드 축소가 제안되었지만 모두 인식 오류나 재식별 위험의 한계가 보고되어, 수집 범위를 목적별로 정하고 이차 이용을 통제하는 운영 규칙이 기술과 함께 필요한 것으로 보인다. | ref-1138, ref-1136, ref-1140, ref-1144, ref-1145, ref-1146, ref-1147, ref-1148 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 53. 개인정보·영상 데이터에서 ROP가 직접 맡을 범위는 로봇 등록 정보에 카메라 유무·촬영 사실 표시 수단·영상 전송 경로를 기록하는 일, 관제 표시·사고 조사·학습 같은 목적별로 영상·위치 데이터의 흐름과 보유 기간을 나눠 관리하는 일, 촬영 금지 장소(화장실·탈의실 등)를 지도 구역으로 표시해 경로·카메라 모드 제약으로 반영하는 일, 로봇이 내보내는 인지 출력의 필드를 과업에 필요한 만큼으로 줄이는 일, 촬영 거부 의사를 받아 여러 로봇에 전달하는 창구로 보인다. | ref-1138, ref-1136, ref-1147, ref-1142 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 카메라 펌웨어·기기 쪽 가림 처리·모바일앱 인증은 제조사가, 로봇 외부의 촬영 표시 부착과 영상정보 보호책임자 지정·운영방침 공개 같은 영상기기 운영자 의무는 현장 운영 사업자가, 시설 CCTV 는 시설 관리자가, 원본 영상 활용 특례 승인은 개인정보보호위원회가 맡으므로, ROP는 그 결과와 상태를 받아 작업·경로·권한 제약과 데이터 흐름 규칙에 반영하는 것으로 보인다. | ref-1141, ref-1136, ref-1139, ref-1137 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f23 | [추정] | 이 영역은 명령 권한과 고객·현장 격리의 51. 인증·권한·격리(f10), 통신 암호화와 감사 기록의 52. 통신 보호·위협 관리·감사(f10·f11), 보행자 위치의 19. 사람·보행자 모델(f15·f16), 촬영 금지 구역을 지도에 두는 16. 장소 의미·지도 관리(f2), 영상·기록 보존의 43. 데이터·관측성·배포와 37. 관제 화면·실행 기록(f4·f11), 사고 영상 이용의 50. 안전 표준·인증·사고 조사(f5), 학습 데이터 이용의 47. AI·학습·적응과 모델 운영과 45. 문서·도면·장면 이해(f6·f9·f12·f13), 재식별 위험 평가의 54. 시험·형식 검증·벤치마크(f14·f16), 위탁·운영자 책임의 58. 다사업자 책임·계약·데이터(f7·f12), 법령의 59. 법·규제·보험·라이선스(f2·f8·f18), 사용자 선호의 60. 노동·수용성·접근성(f15), 적용 현장인 63. 병원·의료(f17)·65. 가정·공동주택(f10~f12)·66. 실외(f7)와 이어진다. | ref-1141, ref-1142, ref-1146, ref-1147, ref-1138, ref-1136, ref-1140, ref-1143, ref-1144, ref-1145, ref-1137, ref-1139, ref-1149, ref-1148 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1135 | 개인정보보호위원회 | [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.) | 2024-10-14 | 정부·연구기관 | high | 2026-09-30 | https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679 | 아니오 |
| ref-1136 | 김·장 법률사무소 | ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터) | 미확인 | 업계 보고서 | medium | 2026-09-30 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 아니오 |
| ref-1137 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" (제목 일부만 확인) | 2024-10-14 | 기사 | medium | 2026-09-30 | https://www.koit.co.kr/news/articleView.html?idxno=125844 | 아니오 |
| ref-1138 | 개인정보보호위원회 (개인정보 포털) | 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286 | 아니오 |
| ref-1139 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용 | 2023-11-15 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 | 아니오 |
| ref-1140 | 법무법인(유) 세종 | 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터) | 미확인 | 업계 보고서 | medium | 2026-09-30 | https://www.shinkim.com/kor/media/newsletter/2342 | 아니오 |
| ref-1141 | 경향신문 | 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인) | 2025-09-02 | 기사 | low | 2026-09-30 | https://www.khan.co.kr/article/202509021447001 | 아니오 |
| ref-1142 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 2026-09-14 | 기사 | low | 2026-09-30 | https://view.asiae.co.kr/article/2026091410054053414 | 아니오 |
| ref-1143 | MIT Technology Review | A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? | 2022-12-19 | 기사 | medium | 2026-09-30 | https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/ | 아니오 |
| ref-1144 | Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv) | EgoBlur: Responsible Innovation in Aria | 2023-08-24 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2308.13093 | 아니오 |
| ref-1145 | Choi, M. 외 (arXiv) | Real-Time Privacy Preservation for Robot Visual Perception | 2025-05-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2505.05519 | 아니오 |
| ref-1146 | Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv) | Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences | 2026-04-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2604.06382 | 아니오 |
| ref-1147 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 2026-09-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.03055 | 아니오 |
| ref-1148 | ACM/IEEE HRI 2026 Companion (저자 미확인) | The Privacy-Preserving Capabilities of a Service Robot in a Healthcare Setting | 2026-03 | 논문 | medium | 2026-09-30 | https://doi.org/10.1145/3776734.3794481 | 예 |
| ref-1149 | European Data Protection Board (EDPB) | Guidelines 3/2019 on processing of personal data through video devices | 2020-01 | 정부·연구기관 | medium | 2026-09-30 | https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/privacy-and-video-data.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f12·f10(가정 로봇 영상 유출·취약점), f19(이차 이용 경로 위험, 추정), f20(핵심 질문 답, 추정) / 섹션 4: 이동형 영상정보처리기기 f1, 촬영 표시·거부(opt-out) f2·f4, 가명처리 f9, 원본 활용 특례 f8, 작업 한정 인지 출력 f16 / 섹션 5: 가정 — f10(예외·성과: 앱 인증 취약점)·f11(예외·성과: 점검 결과, 단기 삭제)·f12(예외·성과: 위탁 경유 유출), 병원 — f17(작업 대상: 얼굴 가림, 모의 실험임 명시), 실외 — f7(제약: 배달로봇 외부 표시). 물류창고·제조 공장·상업 시설 사례는 찾지 못함을 명시 / 섹션 6: 촬영 표시·거부 수용 f2·f4, 검출 후 블러 f13, 명세 기반 실시간 가림 f14, 촬영 시점 저해상도화 f15, 출력 필드 설계 f16, 목적별 이용 구분 f5·f6 / 섹션 7: 개인정보 보호법 제25조의2 f2, 이동형 영상정보처리기기 안내서 f3~f6, 가명정보 처리 가이드라인 f9, 규제샌드박스 실증특례 f8, EDPB 지침 3/2019 f18, EgoBlur f13 / 섹션 8: f13~f17 / 섹션 9: f21(직접 범위), f22(연계 대상) / 섹션 10: f23 — 16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66 / 섹션 11: 기존 oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228(미해결 유지; oq-181 은 f11 로 부분 근거, oq-228 은 f5·f6 로 부분 근거)과 open_questions_new 4건. 다음 실행 후보: 65. 가정·공동주택 페이지 5절에 f10~f12, 63. 병원·의료 페이지에 f17 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 가명처리 | Pseudonymisation | 추가 정보 없이는 특정 개인을 알아볼 수 없도록 개인정보의 일부를 삭제·대체하는 처리로, 한국 가명정보 처리 가이드라인은 2024년 개정에서 영상·이미지·음성 같은 비정형 데이터로 대상을 넓혔다. |
| 얼굴 가림 | Face Obfuscation | 영상에서 얼굴을 검출한 뒤 블러·모자이크·합성 얼굴 등으로 가려 신원을 알아볼 수 없게 하는 처리로, 로봇 영상의 저장·전송·학습 전에 쓰인다. |
| 영상정보 원본 활용 규제샌드박스 실증특례 | Regulatory Sandbox Special Demonstration Exemption for Raw Video Use | 자율주행차·이동형 로봇 개발에 가명처리하지 않은 영상 원본을 쓰도록 개인정보보호위원회가 안전조치를 조건으로 기업별로 허용하는 한시적 특례다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 58. 다사업자 책임·계약·데이터 | 근거: f22 | 종류: 일반
- 로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 54. 시험·형식 검증·벤치마크 | 근거: f16 | 종류: 일반
- 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 19. 사람·보행자 모델 | 근거: f4 | 종류: 일반
- EDPB 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가? | 관련 영역: 53. 개인정보·영상 데이터, 59. 법·규제·보험·라이선스 | 근거: f18 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 3
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - 개인정보 보호법 제25조의2 조문 원문: 국가법령정보센터 페이지 본문 추출 실패, 개인정보 포털과 법률사무소 요약으로 확인(시행일 2023-09-15 는 비공식 법령 DB 에만 있어 넣지 않음)
    - 안내서(2024.9.) PDF 본문 미열람: 세부 내용은 김·장 뉴스레터·정보통신신문 요약 기준
    - 가명정보 처리 가이드라인 개정판 원문 미열람: 개인정보 포털 게시글은 본문 없음, 세종 뉴스레터 요약 기준
    - f10 한국소비자원·한국인터넷진흥원 보도자료 원문은 인증서 오류로 열지 못해 기사 기준
    - f11 개인정보보호위원회 로봇청소기 점검 보도자료 원문 미확인(기사 기준)
    - f13 EgoBlur 학습 데이터 규모·성능 수치는 검색 요약에만 있어 넣지 않음
    - f15 선호 해상도 32×32 이하 수치는 검색 요약에만 있어 넣지 않음
    - f17 HRI 2026 논문 원문 미열람(ACM 403), 저자 미확인
    - f18 EDPB 지침 PDF 본문 추출 실패로 보존 기간·가정 활동 예외 세부 미확인
    - ISO 31700-1:2023(소비재 개인정보 중심 설계) 은 ISO 페이지 403 으로 원문을 열지 못하고 신규 출처 상한 때문에 넣지 않음
    - 보행자 위치 데이터 최소 수집·궤적 익명화 전용 자료는 찾지 못함
    - oq-171·oq-181: 병원·세대 내부가 제25조의2 의 '공개된 장소'에 해당하는지 개인정보보호위원회 해석 원문 미확인
    - oq-214 안전성 확보조치 기준 개정판 조항은 이번에 조사하지 못함
- 범위 경계 위반 의심:
    - f7: 실외 배달로봇의 외부 표시 의무는 현장 운영 사업자의 법적 의무이며 원문 19장 '업종별 조건'에 가까워, ROP 직접 범위는 f21 에서 표시 수단 기록·거부 의사 전달로 한정함
    - f10: 로봇청소기 앱 인증·펌웨어 취약점은 제조사 제품 보안(로봇 자체) 문제로 f22 에서 '연계 대상: '으로 구분함
    - f13·f14·f17: 기기 쪽 얼굴 검출·가림은 원문 19장 '로봇 자체 지능·제어'(센서 인식)에 걸칠 수 있어 기술 근거로만 제안하고, 플랫폼 수준 적용 여부는 추정(f21)으로 둠
- 한계: web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1135~ref-1149, 예약 구간 안)로 신규 출처 상한에 도달해 ISO 31700-1:2023, 개인정보 포털 가명정보 가이드라인 게시글, 로봇신문 로봇청소기 보안 기사, 비공식 법령 DB(casenote)의 조문 전문을 출처로 넣지 않았다. 재사용 출처 없음(참고문헌 목록 요약에 이 영역 인용 0건; 같은 URL 이 이미 있으면 퍼블리셔가 합친다). 원문 열람: 14건 WebFetch 로 열었고 ref-1148 만 403 으로 못 열어 source_unopened 로 표시했다. arXiv 4건(ref-1144~ref-1147)은 초록만 읽었다. 국가법령정보센터·한국소비자원·KISA·ISO·ACM 은 본문 추출 실패·인증서 오류·403 이었다. 교차 확인 3건(f2: 개인정보 포털·김·장, f3: 개인정보보호위원회 게시판·정보통신신문, f6: 김·장·정보통신신문). 기사 근거 finding(f10·f11)은 low. 벤더 기능 주장 없음(f11 의 처리 방식은 규제기관 점검 결과 보도). 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '공개된 장소 촬영은 표시·거부 수용이 요구되고 이차 이용에는 가명처리나 특례가 필요하며, 가림 기술은 인식 오류·재식별 한계가 있어 목적별 수집 범위와 이차 이용 통제 규칙이 함께 필요하다'는 추정이다. 현장 유형 사례는 가정(f10~f12)·병원(f17, 모의)·실외(f7)이며 물류창고·제조 공장·상업 시설·기타는 찾지 못했다. 국내 자료는 개인정보보호위원회 3건(ref-1135·ref-1138·ref-1139)·법률사무소 2건·기사 3건이다. 이 영역에 걸린 기존 열린 질문 7건은 원문 확인이 부족해 해결 제안하지 않았다(oq-181 은 f11 이 동의·계약 구분 점검을 보여 부분 근거, oq-228 은 f5·f6 이 목적 외 이용 판단 사례를 보여 부분 근거). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding(f13·f14·f16의 인식·학습 데이터)은 적용 대상인 이 영역과 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에 함께 연결했다(f23). 용어집에 이미 있는 이동형 영상정보처리기기·역할 기반 접근 통제·감사 추적은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
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
