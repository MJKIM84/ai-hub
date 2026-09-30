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
- verification_stage: second
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
        "ref-125"
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
        "ref-762"
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
        "ref-569"
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
        "ref-569",
        "ref-762"
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
        "ref-1199",
        "ref-944"
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
        "ref-944",
        "ref-1199"
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
        "ref-125",
        "ref-762",
        "ref-1268",
        "ref-1265",
        "ref-1269",
        "ref-1199",
        "ref-944",
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
        "ref-125",
        "ref-762",
        "ref-569",
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
        "ref-125",
        "ref-762",
        "ref-569",
        "ref-1263",
        "ref-1199",
        "ref-944",
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
      "id": "ref-125",
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
      "id": "ref-762",
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
      "id": "ref-569",
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
      "id": "ref-1199",
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
      "id": "ref-944",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 26회/30, 신규 출처 15건/15(ref-125~ref-1269, 예약 구간 안)로 신규 출처 상한에 도달해 HSE 공식 페이지·NEJM 원 연구를 출처로 넣지 않았다. 재사용 1건(ref-031): 참고문헌 목록 요약에 행이 없어 값은 이전 브리프 2026-09-30-17 출처 표를 따랐고(요약 문장은 이번 확인 내용으로 작성), 이번에 GitHub 공식 저장소 원문을 다시 열어 사용자 요청 접수 방식이 범위 밖임을 확인했다. 원문 열람: 16건 중 15건을 열었고(github_raw 5, webfetch 10) ref-1265 만 403 으로 못 열어 source_unopened 로 표시했다. ref-1263·ref-1258·ref-1259 는 PDF 추출이 부분적이다. 교차 확인 2건(f6: HSE·Brazier, f14: 지디넷코리아·로봇신문). 벤더 주장 1건(f19). 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '요청 창구 기술과 사용자 측 운영 요구 표준·법령은 있으나 다중 제조사 관제의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 확인하지 못했고 현장마다 따로 정해진다'는 추정이다. 현장 유형 사례는 병원(f12~f15·f18, 한국 포함)·상업 시설(f16·f17)이며, 제조 공장은 법령(f10)과 벤더 제품(f19)뿐이고 물류창고·가정·실외·기타의 요청 창구 사례는 근거 있는 자료를 찾지 못했다. 국내 자료는 산업안전보건기준에 관한 규칙(ref-1269)·지디넷코리아·로봇신문·한국일보다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 은 없다. 용어집에 이미 있는 서비스 수준 협약·역할 기반 접근 통제·차선 폐쇄·구역 집합·감독 제어·원격 조작은 후보로 내지 않았다. 기존 열린 질문 oq-203 은 부분 근거만 있어 해결 제안하지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-18/verification.json

```json
{
  "run_id": "2026-09-30-18",
  "stage": "first",
  "verdict": "조건부 승인",
  "retry_reason": null,
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GitHub raw 원문을 열었다. category·description 필수, requester·labels·unix_millis_request_time·unix_millis_earliest_start_time·priority·fleet_name 은 선택 항목이고 설명도 일치한다. 발행일 미확인(확인일 2026-09-30)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 원문 열람. OpenID Connect JWT(preferred_username 클레임), 역할·동작·권한 그룹 모델, 관리자는 모든 그룹에 모든 동작 가능이 일치한다. PostgreSQL·SQLite·MySQL·MariaDB 를 지원하고 기본값은 메모리 내 SQLite 이므로 '기록을 관계형 데이터베이스에 저장한다'는 '여러 관계형 데이터베이스를 지원한다' 정도로 좁혀야 한다(수정 지시)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력의 data/source_texts/ref-031.txt(공식 저장소 main, 3.0.0판)로 대조했다. 2절이 'Project Coordination and Implementation Procedures'와 외부 IT 시스템 인터페이스를 범위 밖에 두고, 5.3절은 플릿 관제 기능만 나열한다. 발행일 미확인이므로 판(3.0.0)을 명시한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 메시지 정의 원문이 string fleet_name / uint64[] open_lanes / uint64[] close_lanes 세 필드뿐이다. 발행일 미확인(확인일 기준)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f2·f4 에서 이끈 추론이며 근거 출처 둘 다 실재한다. oq-203 은 부분 근거만 있어 미해결로 둔다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "ref-1258: 2회 열었으나 PDF 본문을 추출하지 못했다. 검색 결과로 기관·제목(HSE Human Factors Briefing Note No. 8)과 '교대 간 대면 논의, 좋은 기록 유지, 수신 확인 피드백' 권고를 확인했다(원문 미열람). ref-1259: 원문을 열어 구조화된 일지·대면·양방향 대화·체크리스트 권고를 확인했다. 두 출처는 발행 주체가 달라 교차 확인으로 인정한다. 다만 '충분한 시간을 두어'는 두 출처에서 권고로 확인되지 않아 빼야 한다(Brazier·Pacitti 에서는 시간 부족이 문제 항목으로만 나온다). 공정 산업 맥락이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 원문에서 실패 원인으로 정보 누락, 표준화되지 않은 비공식 방식, 일관되지 않은 소통, 문서화 부족, 시간 부족을 확인했다. '찾기 어려운 교대 일지'는 확인되지 않아 '문서화 부족'으로 고쳐야 한다(수정 지시). 기준일 2008."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Blazin 외(Pediatric Quality & Safety, 2020-07-23)가 Starmer 외 연구(소아 기관 9곳 전공의)의 의료 오류 23%·예방 가능 유해 사건 30% 감소와 I-PASS 다섯 요소를 서술한다. 원 연구를 인용한 2차 서술이고 교차 확인되지 않았다. 로봇 사례가 아닌 의료진 인계 연구이므로 5절 적용 사례와 현장 유형 매트릭스에는 넣지 않는다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f6~f8 근거를 로봇 관제로 옮기는 추론이며 '찾지 못했다'는 부재 진술이다. 근거 출처는 모두 실재한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 국가법령정보센터 조문(시행 2025-09-01)에서 지침 항목(조작방법·순서, 매니퓰레이터 속도, 2명 이상 작업 시 신호방법, 이상 발견 시 조치, 재가동 시 조치)과 기동스위치 작업 중 표시를 확인했다. 적용 대상은 산업용 로봇 교시 등 작업이며, 원문 19장 기준으로 사업주·제조사 쪽 연계 대상이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람: ANSI 블로그가 검증에서도 403 이었다. 검색 결과(ANSI 블로그, A3 상점)의 제목·발행일 2026-04-23·77쪽·사용자 요구사항·위험성평가·응용과 현재 운영 환경(COE)의 변경 관리·수명주기 인원 안전이 주장과 일치한다. 검색 요약 범위를 넘지 않게 쓴다. 신뢰도는 medium 이 상한이다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1263 PDF 는 검증에서 2회 열었으나 본문을 추출하지 못했다(원문 미열람). 검색 결과(ACM DL·Semantic Scholar, HRI'08 pp. 287-294)로 15개월 민족지, 내과 병동의 업무 중단에 대한 낮은 허용도·비용과 이익의 불일치·통행이 많아 생긴 주행 중단, 산후 병동의 통합을 확인했다. '복잡한 통로'는 '통행이 많은 곳'으로 고친다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: ref-1263 본문을 검증에서 열지 못했고 검색 요약에도 터치스크린 배송 시작, 지정 직원의 적재·하역, 알림 응답 절차가 나타나지 않는다. 리서치도 추출 품질이 낮다고 적었다. '원문 세부 절차 미확인'을 병기한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: 지디넷코리아(2024-09-19)의 7종 73대, 커맨드센터 운영, '의료진이 로봇을 직접 운용하느라 골머리를 쓸 필요가 없'게 한다는 내용과, 로봇신문(2024-04-15)의 7종 73대, 통합관제로 제조사별 로봇을 중앙 관리하며 시나리오 개발·업무 프로세스 조율·모니터링·문제 대응을 맡는다는 내용이 일치한다. 서로 독립된 두 매체로 교차 확인했으나 둘 다 기사다. 2024년 보도 기준이다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇신문의 '의료진과 환자의 요청에 따라 안내 데스크나 각 부서의 담당자가 로봇 서비스를 제공'과 지디넷코리아의 2022-08~2024-05 말 누적 35,492건이 일치한다. 두 사실은 각각 단일 기사에만 있다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 한국일보(2017-04-18). 객실 전화로 요청, '주문한 물건과 방 번호는 사람의 힘을 빌려 인식', 승강기·객실 전화기 연동, 도착 시 자동 알림 전화를 확인했다. 기사는 직원이 '시스템에 입력'했다고 구체적으로 적지 않으므로 표현을 좁힌다(수정 지시). 롱아일랜드 알로프트 호텔이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 원문. 중국 고급 호텔 직원 19명, 2020-01~04 면담, 부서 소속에 관한 인용문, 추가 업무(교육 참여·동료 교육·고객 안내·고장 시 제조사 연락)가 일치한다. 인용은 출처당 1회로 한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Proof News(2026-06-09). MultiCare 계열 Good Samaritan·Tacoma General, 복도에서 길을 잃음, 직원 동행이 필요함, 기존 기송관 설비, 간호사 발언을 확인했다. 기사는 '승강기에서 막혀'가 아니라 승강기 버튼을 스스로 누르지 못했다고 적으므로 고친다. 단일 기사다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OMRON 제품 페이지에서 Mobile I/O Box 문장을 확인했다. vendor_claim: true 이고 태그가 추정이므로 '벤더 주장' 병기를 유지한다. 현장 유형은 없다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 핵심 질문 답의 종합이다. 근거 가운데 f13 은 강등됐고 ref-1265 는 원문 미열람이므로 이 두 근거에 무게를 두지 않는다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: ROP 직접 범위 제안이며 원문 19장 경계(요청·권한·상태·기록)와 충돌하지 않는다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 원문 19장의 상위 업무 시스템·시설·설비 제어·업종별 조건을 연계 대상으로 올바르게 구분했다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 연결 영역 18개의 번호와 이름이 부록 A 원문 명칭과 일치한다. 12. 채팅으로 업무 지시·오케스트레이션과의 연결 근거(f1)는 간접적이므로 연결 이유를 '요청 창구의 하나'로만 쓴다."
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
      "ref-031(VDA 5050) 재사용: 2026-09-30-17 브리프와 같은 출처 id 를 쓴다. 새 각주를 만들지 않는다.",
      "f4 의 차선 폐쇄와 f2 의 역할 기반 권한은 용어집의 lane-closure(차선 폐쇄)·role-based-access-control(역할 기반 접근 통제) 항목과 겹친다. 새 용어로 만들지 않고 링크로 잇는다."
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
    "f13: [사실]을 [추정]으로 강등하고 5절 병원 사례(시작 조건)에 쓸 때 '원문 세부 절차 미확인'을 병기한다. ref-1263 본문을 검증에서 열지 못했고, 검색 요약에도 터치스크린 배송 시작·적재·알림 응답 절차가 나타나지 않는다.",
    "ref-1265, ref-1258, ref-1263: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다. ref-1265 는 403 이었고, ref-1258·ref-1263 은 검증에서 PDF 본문을 두 번씩 추출하지 못해 검색 결과 일치로만 확인했다.",
    "f6: '충분한 시간을 두어' 구절을 빼고 대면 논의, 양방향(수신 확인) 대화, 교대 일지 기록 권고로만 쓴다. 두 출처 모두에서 시간 확보가 권고로 확인되지 않았다.",
    "f7: '불완전하거나 찾기 어려운 교대 일지'를 '교대 기록(문서화) 부족'으로 고친다. 원문 실패 원인은 문서화 부족이며 '찾기 어려움'은 확인되지 않았다.",
    "f12: '복잡한 통로에서의 주행 중단'을 '통행이 많은 곳에서의 주행 중단'으로 고친다. 검색된 초록 표현이 'breakdowns due to high traffic'이다.",
    "f16: '직원이 주문 내용과 객실 번호를 시스템에 입력했고'를 '주문한 물건과 객실 번호는 사람이 확인해 처리했고(주문 접수는 자동화되지 않음)'로 좁힌다. 기사는 입력 방식을 구체적으로 밝히지 않는다.",
    "f18: '승강기에서 막혀'를 '승강기 버튼을 스스로 누르지 못해'로 고친다. 기사 서술이 그렇다.",
    "f2: '기록을 관계형 데이터베이스에 저장한다'를 '여러 관계형 데이터베이스(PostgreSQL·SQLite·MySQL·MariaDB)를 지원하며 기본값은 메모리 내 SQLite 다'로 고친다. 역할 기반 권한은 용어집의 역할 기반 접근 통제 (Role-Based Access Control (RBAC)) 항목에 링크한다. README 가 기본 DB 를 메모리 내 SQLite 로 밝힌다.",
    "f8: 4절(I-PASS)과 8절에서만 쓰고 5절 적용 사례와 site_matrix_updates 에는 넣지 않는다. 수치는 Starmer 외 원 연구를 Blazin 외가 인용한 2차 서술이고 교차 확인되지 않았음을 본문에 밝힌다. 로봇 운영 사례가 아닌 의료진 인계 연구이기 때문이다.",
    "f6·f7·f8: 공정 산업·의료의 인계 방법 참고로만 서술하고, 로봇 관제 교대로 옮길 수 있다는 내용은 f9 의 [추정]으로만 쓴다. 로봇 분야 근거가 없다.",
    "f10: 7절에는 관련 법령으로 두되 적용 대상이 산업용 로봇의 교시 등 작업임을 밝히고, 9절에서는 사업주·제조사가 맡는 연계 대상(f22)으로 쓴다. ROP 직접 범위처럼 쓰지 않는다. 원문 19장의 '로봇 자체 지능·제어'·설비 안전 쪽 내용이다.",
    "f3: VDA 5050 을 '3.0.0판(공식 저장소 main, 발행일 미확인)'으로 판을 밝혀 쓴다. ref-031 발행일이 null 이고 판에 따라 범위 문구가 다를 수 있다.",
    "f11: 발행일 2026-04-23·77쪽을 기준일로 남기고, 내용은 검색 요약 범위(사용자 요구사항, 위험성평가, 응용·현재 운영 환경의 변경 관리, 수명주기 인원 안전)를 넘지 않게 쓴다. 원문을 열지 못했다.",
    "f14·f15: 한림대학교성심병원 로봇 규모와 누적 사용 건수가 2024년 보도 기준임을 문장에 밝히고, 그 뒤의 규모 변화는 쓰지 않는다. 리서치가 2025년 규모를 확인하지 못했다.",
    "5절: 현장 유형 사례는 병원(f12·f13·f14·f15·f18)과 상업 시설(f16·f17)만 세운다. 물류창고·제조 공장·가정·실외·기타의 요청 창구 사례는 근거 자료를 찾지 못했다고 밝히고, f19(벤더 제품, 현장 유형 없음)와 f10(법령)을 제조 공장 사례로 세우지 않는다. site_matrix_updates 도 병원·상업 시설 칸으로 한정한다. 두 finding 은 현장 사례가 아니다.",
    "glossary_candidates '역할 모호성': 정의에서 '추가 업무와 사용 저항의 원인으로 보고된다'를 'Fu 외(2022) 호텔 직원 면담에서 사용 저항 요인과 함께 보고되었다'로 한정한다. 단일 연구 근거다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 22건, 미확인 1건, 교차 확인 2건(f6: HSE·Brazier·Pacitti, f14: 지디넷코리아·로봇신문). 강등: f13 사실 → 추정(원문 세부 절차 미확인). 원문 미열람 출처: ref-1265(403), ref-1258·ref-1263(검증에서 PDF 본문 추출 실패, 검색 결과 일치로 확인). 주의: 핵심 질문의 답(f20)과 책임 경계(f21·f22)는 추정이다. 교대 인수인계 근거(f6~f8)는 공정 산업·의료 분야 자료이며 로봇 관제에 적용한 공개 절차는 확인되지 않았다. 현장 사례는 병원·상업 시설뿐이고 대부분 단일 기사·단일 연구다. I-PASS 수치(f8)는 원 연구를 인용한 2차 서술이다. f6·f7·f12·f16·f18 은 출처 표현에 맞게 문구를 좁혔다. oq-203 은 부분 근거(f4·f5)만 있어 미해결로 둔다. 다음 조사에서는 VDA 5050 3.0.0(ref-031)의 RELEASE 구역 허가·만료(leaseExpiry) 절차가 oq-203 에 주는 근거를 확인할 수 있다. 정정 요청 없음. 검증 검색 3회(리서치 26회와 합쳐 29/30)."
}
```

### runs/2026-09-30-18/pages.json

```json
{
  "run_id": "2026-09-30-18",
  "outline": [
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 700,
      "summary": "여러 제조사 로봇을 한 관제에서 운영할 때의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 확인되지 않았고 현장마다 따로 정해지는 것으로 보인다. [추정][^ref-125][^ref-1265][^ref-1269][^ref-1199][^ref-1260]",
      "planned_findings": [
        "f20",
        "f12",
        "f17",
        "f14"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "작업 요청 스키마, 역할 기반 권한, 호출 버튼, 교대 인수인계, I-PASS, 역할 모호성을 정리한다. [사실][^ref-125][^ref-762][^ref-1258][^ref-1259][^ref-1267][^ref-1260]",
      "planned_findings": [
        "f1",
        "f2",
        "f19",
        "f6",
        "f8",
        "f17"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1500,
      "summary": "병원(한림대학교성심병원 커맨드센터, TUG 배송 로봇, Moxi)과 상업 시설(호텔 배송 로봇, 호텔 직원 면담) 사례만 세우고 다른 현장 유형은 근거를 찾지 못했다고 밝힌다. [사실][^ref-1199][^ref-944][^ref-1263][^ref-1264]",
      "planned_findings": [
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1300,
      "summary": "요청 형식 통일, 역할 기반 권한, 임시 통제 구역 기록, 구조화된 교대 인수인계, 전담 운영 조직의 다섯 접근을 정리한다. [사실][^ref-125][^ref-762][^ref-569][^ref-1259]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f14",
        "f17",
        "f19"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "Open-RMF 작업 요청·API 서버·차선 요청 메시지, VDA 5050 3.0.0판, ANSI/A3 R15.08-3-2026, 산업안전보건기준에 관한 규칙 제222조, HSE 지침을 표로 둔다. [사실][^ref-125][^ref-031][^ref-1265][^ref-1269]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f6",
        "f10",
        "f11"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "교대 인수인계(HSE, Brazier·Pacitti, I-PASS)와 로봇 수용(Mutlu·Forlizzi, Fu 외) 연구 다섯 건. [사실][^ref-1258][^ref-1259][^ref-1267][^ref-1263][^ref-1260]",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f12",
        "f17"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 800,
      "summary": "ROP는 요청 접수·권한·상태 알림·통제 구역 기록·인수인계 요약을, 업무 시스템·인력 제도·교시 작업 지침·승강기 제어는 연계 대상으로 둔다. [추정][^ref-125][^ref-762][^ref-1269]",
      "planned_findings": [
        "f21",
        "f22",
        "f10",
        "f3"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64번 영역과의 연결. [추정][^ref-125][^ref-569]",
      "planned_findings": [
        "f23"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "section": "11. 열린 질문",
      "budget_chars": 700,
      "summary": "oq-203 미해결 유지와 새 질문 네 건(관제 교대 인계 항목, 대리 입력 방식 비교, R15.08-3 이행 주체, 운영 책임 조직 비교).",
      "planned_findings": [
        "f4",
        "f5",
        "f9",
        "f11",
        "f15",
        "f17"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 신규 작성, 13절 각주 정의 16건, 프런트매터 related_areas·tags·confidence·sources·last_run 채움(1차 조건부 승인 수정 16건 반영)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"6. 대표 접근법과 기술\" 절(1,472자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,355자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"4. 핵심 개념과 용어\" 절(1,134자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"8. 대표 연구와 자료\" 절(938자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"11. 열린 질문\" 절(843자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(840자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area40-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 40. 운영 절차·요청 창구 의 \"3. 왜 중요한가\" 절(528자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 40. 운영 절차·요청 창구 | 영역 심화: 3~11절 신규 작성(요청 창구·역할 기반 권한·교대 인수인계, 병원·상업 시설 사례), 1차 조건부 승인 수정 16건 반영 | run 2026-09-30-18",
  "index_updates": {
    "home_recent": "2026-09-30 — 40. 운영 절차·요청 창구: 3~11절 신규 작성. 요청 창구 형식·역할 기반 권한·교대 인수인계 근거와 병원·상업 시설 사례를 정리했고, 다중 제조사 관제의 요청 접수·교대 절차를 정한 공개 표준은 확인하지 못했다",
    "category_recent": "2026-09-30 — 40. 운영 절차·요청 창구: 영역 심화로 3~11절 신규 작성(병원·상업 시설 사례, 책임 경계, 열린 질문 4건 추가)",
    "area_recent": "2026-09-30 — 40. 운영 절차·요청 창구: 3~11절 신규 작성, 각주 16건, 1차 조건부 승인 수정 16건 반영 (실행 2026-09-30-18)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "shift-handover",
      "term_ko": "교대 인수인계",
      "term_en": "Shift Handover",
      "definition": "연속 운영 현장에서 나가는 근무조가 들어오는 근무조에게 설비·작업 상태와 위험 정보를 넘기는 절차로, 대면 논의·양방향(수신 확인) 대화·교대 일지 기록이 권고된다.",
      "description": "공정 산업 지침(HSE Briefing Note No. 8, 2005)과 Brazier·Pacitti(2008)의 권고에 근거한다. 로봇 관제 교대에 옮기는 것은 추정이며 로봇 관제 전용 공개 절차는 확인되지 않았다.",
      "related_areas": [
        40,
        37,
        56
      ],
      "sources": [
        "ref-1258",
        "ref-1259"
      ]
    },
    {
      "action": "new",
      "slug": "i-pass-handoff-program",
      "term_ko": "I-PASS 인계 프로그램",
      "term_en": "I-PASS Handoff Program",
      "definition": "질병 중증도·환자 요약·할 일 목록·상황 인식과 비상 계획·수신자의 요약 확인 다섯 항목으로 의료진 인계를 구조화한 프로그램이다.",
      "description": "Blazin 외(2020)가 Starmer 외 연구의 의료 오류 23%·예방 가능한 유해 사건 30% 감소를 인용한 2차 서술이며 교차 확인되지 않았다. 로봇 운영 사례가 아닌 의료진 인계 연구다.",
      "related_areas": [
        40,
        63
      ],
      "sources": [
        "ref-1267"
      ]
    },
    {
      "action": "new",
      "slug": "role-ambiguity",
      "term_ko": "역할 모호성",
      "term_en": "Role Ambiguity",
      "definition": "로봇 같은 새 설비의 운영·정비 책임이 어느 부서·사람에게 있는지 불분명한 상태로, Fu 외(2022) 호텔 직원 면담에서 사용 저항 요인과 함께 보고되었다.",
      "related_areas": [
        40,
        56,
        58,
        60
      ],
      "sources": [
        "ref-1260"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "VDA 5050 공식 명세 원문(3.0.0판, 공식 저장소 main). 플릿 관제와 이동로봇 간 통신을 정의하며 사용자 요청 접수 방법과 프로젝트 조정·수행 절차는 범위 밖에 둔다.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-125",
      "org": "Open-RMF (open-rmf/rmf_api_msgs 저장소)",
      "title": "rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 작업 요청 JSON 스키마. category·description 필수, requester·labels·요청 시각·가장 이른 시작 시각·priority·fleet_name 선택.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open-RMF (open-rmf/rmf-web 저장소)",
      "title": "rmf-web/packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 대시보드용 API 서버 설명. OpenID Connect JWT 인증, 역할·동작·권한 그룹 기반 권한, 여러 관계형 데이터베이스 지원(기본값 메모리 내 SQLite).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-569",
      "org": "Open-RMF (open-rmf/rmf_internal_msgs 저장소)",
      "title": "rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 차선 열기·닫기 요청 메시지 정의. fleet_name, open_lanes, close_lanes 세 필드.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "summary": "원문 미열람(검증에서 PDF 본문 추출 실패, 검색 결과 일치로 확인). HSE 인적 요인 지침. 교대 인수인계를 대면 논의·양방향(수신 확인) 대화·교대 일지 기록으로 하도록 권고. 제3자 사이트 게재본.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": true
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
      "summary": "공정 산업 교대 인수인계의 실패 원인(정보 누락, 비구조화, 문서화 부족)과 구조화된 일지·대면·양방향 대화·체크리스트 권고.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1199",
      "org": "지디넷코리아",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원 커맨드센터의 7종 73대 서비스 로봇 운영, 2022-08~2024-05 누적 35,492건 보도(2024년 보도 기준).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인)",
      "published": "2024-04",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대학교성심병원 커맨드센터가 7종 73대 로봇을 통합관제로 운영하며 시나리오 개발·업무 조율·모니터링·문제 대응을 맡고, 안내 데스크·부서 담당자가 요청을 받아 로봇 서비스를 제공한다는 보도.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "summary": "원문 미열람(검증에서 PDF 본문 추출 실패, 검색 결과 일치로 확인). 병원 배송 로봇 TUG 의 15개월 민족지 연구. 병동별 업무 흐름·사회적·환경 요인에 따라 수용이 크게 달랐음.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": true
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
      "summary": "뉴욕 알로프트 호텔의 Savioke Relay 배송 로봇 운용 보도(객실 전화 요청, 주문 물건·객실 번호는 사람이 확인해 처리, 승강기 연동, 도착 시 객실 전화 자동 알림).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "summary": "원문 미열람. 산업용 이동로봇 안전 요구사항 제3부(사용) 소개. 사용자 요구사항, 위험성평가, 응용·현재 운영 환경 변경 관리, 2026-04-23 발행·77쪽(검색 요약 기준).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "summary": "MultiCare 계열 두 병원의 Moxi 로봇 운용 문제(길 잃음, 승강기 버튼을 스스로 누르지 못함, 상시 동행 필요)와 간호사 반응 보도.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "summary": "I-PASS 구조화 인계를 여러 인계 상황에 적용한 연구. 원 연구(Starmer 외)의 오류 23%·예방 가능 유해 사건 30% 감소를 인용한 2차 서술과 I-PASS 구성 요소.",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "summary": "OMRON AMR 제품 페이지. 버튼으로 AMR 을 지정 위치로 부르는 Mobile I/O Box 와 MobilePlanner 소개(벤더 주장).",
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
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
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 로봇을 한 관제에서 운영할 때 교대 인수인계로 넘길 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외)을 정한 공개 절차나 체크리스트가 있는가?",
      "areas": [
        40,
        37
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원·호텔에서 안내 데스크·프런트 담당자가 로봇 요청을 대신 입력하는 방식과 현장 사용자가 직접 요청하는 방식의 처리 시간·오류·업무 부담을 비교한 연구가 있는가?",
      "areas": [
        40,
        63,
        64
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가?",
      "areas": [
        40,
        50,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가?",
      "areas": [
        40,
        56,
        60
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    },
    {
      "site_type": "상업 시설",
      "item": "시작 조건",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    },
    {
      "site_type": "상업 시설",
      "item": "완료·인계",
      "link": "docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#5-적용-사례-현장-유형-명시",
      "title": "40. 운영 절차·요청 창구"
    }
  ],
  "standards_updates": [
    {
      "name": "ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용",
      "kind": "표준",
      "org": "ANSI / A3(Association for Advancing Automation)",
      "url": "https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/",
      "related_areas": [
        40,
        48,
        50
      ],
      "summary": "2026-04-23 발행(검색 요약 기준, 원문 미열람). 사용자가 제조사·통합자가 준 정보를 적용해 산업용 이동로봇 응용과 운영 환경을 안전하게 운용·정비하기 위한 요구사항을 정하며, 위험성평가와 응용·현재 운영 환경의 변경 관리를 강조한다.",
      "ref_id": "ref-1265"
    },
    {
      "name": "HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications",
      "kind": "프레임워크",
      "org": "UK Health and Safety Executive (HSE)",
      "url": "https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf",
      "related_areas": [
        40,
        37
      ],
      "summary": "2005년 공정 산업 인적 요인 지침(제3자 게재본, 원문 미열람). 교대 인수인계를 대면 논의·양방향(수신 확인) 대화·교대 일지 기록으로 하도록 권고한다.",
      "ref_id": "ref-1258"
    }
  ],
  "additional_research_requests": [
    "5절 적용 사례: 물류창고·제조 공장·가정(아파트 입주민 앱 로봇 호출 등)·실외·기타 현장의 로봇 요청 창구와 운영 조직 사례가 없어 병원·상업 시설 사례만 세웠다. 현장 유형 편중을 줄이기 위해 근거 자료가 필요하다.",
    "5절 병원 사례(한림대학교성심병원)의 작업 대상·제약·완료·인계 칸이 미확인이다. 요청 대상 업무 구성과 완료 확인 방식을 밝힌 자료가 필요하다. 2024년 이후 규모 변화(검색 요약의 11종 77대)도 출처 확인이 필요하다.",
    "5절 병원 TUG 사례(ref-1263)의 요청 시작·적재·알림 응답 절차가 원문 미확인이라 [추정]으로 썼다. 원문 본문 확인이 필요하다.",
    "11절 oq-203: VDA 5050 3.0.0(ref-031)의 RELEASE 구역 허가·만료(leaseExpiry) 절차가 임시 통제 구역 선언·해제에 주는 근거를 확인해야 한다(1차 검증 노트 제안).",
    "6·8절: I-PASS 수치(Starmer 외, NEJM 2014)는 2차 서술만 근거라 원 연구 원문 확인이 필요하다. 로봇 관제 교대 인수인계 항목을 정한 공개 절차·표준도 계속 찾아야 한다.",
    "7절: ANSI/A3 R15.08-3-2026 원문(또는 공식 요약)을 열어 사용자 운영 절차·교육 요구 항목을 확인해야 한다.",
    "6절 요청 접수: ISO/IEC 20000-1:2018 서비스 요청 관리 조항과 Diligent Moxi 요청 창구(키오스크·문자·음성 버튼)를 공식 자료로 확인하면 요청 창구 접근을 보강할 수 있다."
  ],
  "fixes_applied": [
    "f13 강등 — 5절 병원 TUG 사례의 시작 조건·수행 자원 칸을 [추정]으로 쓰고 '원문 세부 절차 미확인'을 병기했다.",
    "ref-1265·ref-1258·ref-1263 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 해당 항목에 source_unopened: true 를 넣었다.",
    "f6 — '충분한 시간을 두어'를 빼고 4·6·8절에서 대면 논의, 양방향(수신 확인) 대화, 교대 일지 기록 권고로만 썼다.",
    "f7 — 6·8절의 실패 원인을 '교대 기록(문서화) 부족'으로 고쳤다.",
    "f12 — 3·5·8절에서 '통행이 많은 곳에서의 주행 중단'으로 고쳤다.",
    "f16 — 5절 상업 시설 사례의 시작 조건을 '주문한 물건과 객실 번호는 사람이 확인해 처리했다(주문 접수는 자동화되지 않음)'로 좁혔다.",
    "f18 — 5절 Moxi 서술을 '승강기 버튼을 스스로 누르지 못해'로 고쳤다.",
    "f2 — 6절에 '여러 관계형 데이터베이스(PostgreSQL·SQLite·MySQL·MariaDB)를 지원하고 기본값은 메모리 내 SQLite'로 고치고, 4·6절에서 용어집 역할 기반 접근 통제 항목에 링크했다.",
    "f8 — I-PASS 는 4절과 8절(및 6절에서 4절 참조)에만 쓰고 5절 사례와 site_matrix_updates 에서 뺐으며, 수치가 Starmer 외 원 연구를 Blazin 외가 인용한 2차 서술이고 교차 확인되지 않았음을 본문에 밝혔다.",
    "f6·f7·f8 — 공정 산업·의료의 인계 방법 참고로만 서술하고, 로봇 관제 교대로 옮길 수 있다는 내용은 6절 끝의 f9 [추정] 문장으로만 썼다.",
    "f10 — 7절 표에 적용 대상이 산업용 로봇의 교시 등 작업임을 밝혀 관련 법령으로 두고, 9절 표·본문에서 사업주·제조사가 맡는 연계 대상으로 썼다.",
    "f3 — 6·7절에서 VDA 5050 을 '3.0.0판(공식 저장소 main, 발행일 미확인)'으로 판을 밝혀 썼다.",
    "f11 — 7절에 발행일 2026-04-23·77쪽을 기준일로 남기고 내용은 사용자 요구사항·위험성평가·변경 관리·수명주기 인원 안전(검색 요약 기준) 범위로만 썼으며 원문 미열람을 표시했다.",
    "f14·f15 — 3·5·6절의 한림대학교성심병원 규모(7종 73대)와 누적 사용 건수에 '2024년 보도 기준'을 밝히고 그 뒤의 규모 변화는 쓰지 않았다.",
    "5절 — 사례를 병원(f12·f13·f14·f15·f18)과 상업 시설(f16·f17)로만 세우고, 다른 현장 유형은 근거 자료를 찾지 못했다고 밝혔으며 f19·f10 을 사례로 세우지 않았고 site_matrix_updates 를 병원·상업 시설 칸으로 한정했다.",
    "glossary '역할 모호성' — 정의를 'Fu 외(2022) 호텔 직원 면담에서 사용 저항 요인과 함께 보고되었다'로 한정해 glossary_updates 와 4절에 썼다.",
    "분량 초과 자동 분리: 40. 운영 절차·요청 창구 본문 9,825자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,707자"
  ]
}
```

### runs/2026-09-30-18/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area40-s6.md (1,472자)
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area40-s7.md (1,355자)
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area40-s4.md (1,134자)
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area40-s8.md (938자)
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area40-s11.md (843자)
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area40-s10.md (840자)
    - docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area40-s3.md (528자)
```

### runs/2026-09-30-18/pages/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md

```markdown
---
title: "40. 운영 절차·요청 창구"
type: area
category: "J. 현장 운영·관제"
area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [요청 창구, 작업 요청, 역할 기반 권한, 교대 인수인계, 운영 조직]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-031, ref-125, ref-762, ref-569, ref-1258, ref-1259, ref-1260, ref-1199, ref-944, ref-1263, ref-1264, ref-1265, ref-1266, ref-1267, ref-1268, ref-1269]
last_run: 2026-09-30
version: 2
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

요청 창구 기술(작업 요청 API 스키마, 역할 기반 권한, 호출 버튼, 프런트 경유 입력)과 사용자 측 운영 요구 표준·교시 작업 지침 법령은 있지만, 여러 제조사 로봇을 한 관제에서 운영할 때의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 이번 조사에서 확인되지 않았고 현장마다 따로 정해지는 것으로 보인다. [추정][^ref-125][^ref-1265][^ref-1269][^ref-1199][^ref-1260]

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 왜 중요한가](../../topics/2026/2026-09-30-area40-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 요청을 받는 쪽(작업 요청·권한·호출 장치)과 사람 사이의 넘김(교대 인수인계·역할)으로 나뉜다.

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area40-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역에서 근거 자료가 있는 현장 유형은 병원과 상업 시설이다. 물류창고·제조 공장·가정·실외·기타 현장의 요청 창구 사례는 이번 조사에서 근거 자료를 찾지 못했다. 4절의 호출 버튼 제품과 7절의 교시 작업 법령은 현장 사례가 아니므로 사례로 세우지 않았다.

**현장 유형:** 병원

**사례:** 한림대학교성심병원에서 의료진·환자의 요청을 전담 조직이 로봇 서비스로 처리(2024년 보도 기준)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 의료진·환자가 안내 데스크나 각 부서에 요청하면 담당자가 로봇으로 서비스를 제공한다. [사실][^ref-944] |
| 작업 대상 | 미확인 |
| 수행 자원 | 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다(2024년 보도 기준). [사실][^ref-1199][^ref-944] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 커맨드센터가 실시간 모니터링과 문제 대응을 맡는다. [사실][^ref-944] 2022-08~2024-05 누적 사용은 35,492건이다(2024년 보도 기준). [사실][^ref-1199] |

이 사례에서 40. 운영 절차·요청 창구가 관여하는 칸은 시작 조건(현장 사용자가 어디로 요청하는가)과 수행 자원(누가 로봇 운영을 책임지는가)이다. 요청 경로는 로봇신문, 누적 사용 건수는 지디넷코리아 한 매체에만 있어 각각 교차 확인되지 않았다. [사실][^ref-944][^ref-1199]

**현장 유형:** 병원

**사례:** 병원 병동에서 자율 배송 로봇(TUG)으로 물품 배송(HRI 2008 민족지 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 직원이 터치스크린 단말에서 배송을 시작한 것으로 보인다(원문 세부 절차 미확인). [추정][^ref-1263] |
| 작업 대상 | 미확인 |
| 수행 자원 | 지정된 직원이 물품을 싣고 내리며, 로봇이 도움을 요청하면 직원이 알림에 응답한 것으로 보인다(원문 세부 절차 미확인). [추정][^ref-1263] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 내과 병동에서는 업무 중단에 대한 낮은 허용도, 인지된 비용과 이익의 불일치, 통행이 많은 곳에서의 주행 중단 때문에 업무 흐름에 부정적 영향을 주고 직원 저항을 낳았지만, 산후 병동에서는 업무 흐름과 사회적 맥락에 통합되었다. [사실][^ref-1263] |

같은 병원 현장 유형의 다른 보도로, Proof News(2026-06)에 따르면 미국 MultiCare 계열 두 병원(Good Samaritan, Tacoma General)의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기 버튼을 스스로 누르지 못해 사람이 계속 따라다녀야 했고, 기존 기송관 설비가 있어 간호사들이 로봇의 쓸모에 의문을 제기했다. [사실][^ref-1266] 승강기 연동은 이 영역이 아니라 외부 설비와의 연계 대상이다(9절).

**현장 유형:** 상업 시설

**사례:** 호텔에서 투숙객이 주문한 물품을 배송 로봇으로 객실 앞까지 운반(2017년 보도)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미국 뉴욕 알로프트 호텔에서 투숙객이 전화로 프런트에 요청하면, 주문한 물건과 객실 번호는 사람이 확인해 처리했다(주문 접수는 자동화되지 않음). [사실][^ref-1264] |
| 작업 대상 | 주문 물품과 투숙객 객실. [사실][^ref-1264] |
| 수행 자원 | 프런트 직원, 배송 로봇(Savioke Relay), 로봇과 연동된 승강기. [사실][^ref-1264] |
| 제약 | 미확인 |
| 완료·인계 | 로봇이 객실 앞에 도착하면 객실 전화로 자동 알림을 보냈다. [사실][^ref-1264] |
| 예외·성과 | 미확인 |

이 사례의 요청 창구는 전화와 프런트 직원이며, 로봇 운용이 시작되어도 요청 접수는 사람이 맡았다. [사실][^ref-1264] 같은 현장 유형의 다른 연구로, Fu·Zheng·Wong(2022)이 중국 고급 호텔 직원 19명을 면담한 결과 로봇이 기술·시설·서비스 부서 가운데 어디에 속하는지가 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육, 동료 교육, 고장 처리·고객 안내 같은 추가 업무가 직원의 로봇 사용 저항으로 이어졌다. [사실][^ref-1260]

## 6. 대표 접근법과 기술

확인된 접근은 요청 형식 통일, 역할 기반 권한, 임시 통제 구역 기록, 구조화된 교대 인수인계, 전담 운영 조직의 다섯 갈래이며, 여러 제조사 로봇 관제에 맞춘 공개 절차는 아직 확인되지 않았다. [추정][^ref-125][^ref-762][^ref-1259][^ref-1199]

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area40-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

요청 형식과 권한은 오픈소스 규격에서, 사용자 운영 요구와 작업 지침은 표준·법령에서, 교대 인수인계는 공정 산업 지침에서 근거를 찾을 수 있다. [사실][^ref-125][^ref-1265][^ref-1269][^ref-1258]

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area40-s7.md)에 있다.

## 8. 대표 연구와 자료

교대 인수인계 방법은 공정 산업·의료 연구에서, 요청 창구와 역할 문제는 병원·호텔의 로봇 도입 연구에서 근거를 얻는다. [사실][^ref-1259][^ref-1267][^ref-1263][^ref-1260]

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 대표 연구와 자료](../../topics/2026/2026-09-30-area40-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이번 자료를 종합하면 ROP는 요청 접수·권한·상태 알림·기록을 맡고, 요청을 만드는 업무 시스템과 인력 제도, 로봇 교시 작업 지침, 설비 제어는 연계 대상으로 두는 것으로 보인다. [추정][^ref-125][^ref-762][^ref-1269]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 호출 버튼·단말·앱·업무 시스템 API 등 여러 요청 창구를 요청자·목적·시각·우선순위를 담은 하나의 요청 형식으로 받는 접수 기능과 요청 상태 알림. [추정][^ref-125][^ref-1264] | 전자의무기록·호텔 객실 관리·제조 실행 시스템 같은 업무 시스템의 요청 발생. [추정][^ref-1264][^ref-1260] |
| 로봇 자체 지능·제어 | 요청과 로봇 상태를 받아 작업·권한·경로 제약으로 연결. [추정][^ref-1269][^ref-031] | 로봇 교시·정비 작업 지침(사업주·제조사 책임. 산업안전보건기준에 관한 규칙 제222조의 교시 등 작업 지침 포함). [추정][^ref-1269][^ref-1265] |
| 시설·설비 제어 | 임시 통제 구역 선언·해제의 요청자·승인·기한 기록. [추정][^ref-569][^ref-762] | 승강기·공동현관 제어. [추정][^ref-1264] |
| 업종별 조건 | 요청자·운영자·관리자 역할과 권한 정의, 교대 인수인계용 운영 상태 요약(열린 작업·폐쇄 구역·예외)의 제공과 기록. [추정][^ref-762][^ref-1258][^ref-1267] | 병원·호텔의 인력 편성과 교대 근무 제도. [추정][^ref-1260] |

로봇 통신 규격인 VDA 5050 3.0.0판이 사용자 요청 접수 방법을 정하지 않으므로, 이종 제조사를 연결하는 ROP의 이 영역 직접 범위는 로봇 제어가 아니라 요청을 받고 권한을 판정하고 기록을 남기는 층에 있는 것으로 보인다. [추정][^ref-031][^ref-125][^ref-762] 교시 작업 지침은 사업주·제조사가 맡는 연계 대상이며 ROP 직접 범위로 다루지 않는다. [추정][^ref-1269] 경계는 제품 전략에 따라 옮겨질 수 있으며 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

요청이 들어오는 창구, 요청이 바뀌는 작업, 요청을 막거나 허용하는 조건, 요청을 처리하는 사람과 조직 쪽으로 다음 영역과 이어진다. [추정][^ref-125][^ref-762][^ref-569]

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area40-s10.md)에 있다.

## 11. 열린 질문

요청 창구와 교대 절차는 사례·표준 근거가 얇아 다음 질문이 남아 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [40. 운영 절차·요청 창구 — 열린 질문](../../topics/2026/2026-09-30-area40-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-125]: Open-RMF (open-rmf/rmf_api_msgs 저장소), rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-30
[^ref-762]: Open-RMF (open-rmf/rmf-web 저장소), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-569]: Open-RMF (open-rmf/rmf_internal_msgs 저장소), rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-1258]: UK Health and Safety Executive (HSE) (humanfactors101.com 게재본), Human Factors Briefing Note No. 8 — Safety-Critical Communications, 2005, https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1259]: Brazier, A., & Pacitti, B. (IChemE Hazards XX), Improving shift handover and maximising its value to the business, 2008, https://www.icheme.org/media/9743/xx-paper-48.pdf, 접근일 2026-09-30
[^ref-1260]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30
[^ref-1263]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1264]: 한국일보, “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인), 2017-04-18, https://www.hankookilbo.com/news/article/201704180418820469, 접근일 2026-09-30
[^ref-1265]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-1266]: Proof News (Varsha Bansal), Meet the Robot That Nurses Unplugged, 2026-06-09, https://www.proofnews.org/moxi/, 접근일 2026-09-30
[^ref-1267]: Blazin, L. J. 외 (Pediatric Quality & Safety), Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings, 2020-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/, 접근일 2026-09-30
[^ref-1269]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등), 2025-09-01, https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202, 접근일 2026-09-30
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

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s6.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 대표 접근법과 기술"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-125, ref-762, ref-569, ref-1258, ref-1259, ref-1260, ref-1199, ref-944, ref-1264, ref-1267, ref-1268]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#6
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 대표 접근법과 기술

# 40. 운영 절차·요청 창구 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인된 접근은 요청 형식 통일, 역할 기반 권한, 임시 통제 구역 기록, 구조화된 교대 인수인계, 전담 운영 조직의 다섯 갈래이며, 여러 제조사 로봇 관제에 맞춘 공개 절차는 아직 확인되지 않았다. [추정][^ref-125][^ref-762][^ref-1259][^ref-1199]
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인된 접근은 요청 형식 통일, 역할 기반 권한, 임시 통제 구역 기록, 구조화된 교대 인수인계, 전담 운영 조직의 다섯 갈래이며, 여러 제조사 로봇 관제에 맞춘 공개 절차는 아직 확인되지 않았다. [추정][^ref-125][^ref-762][^ref-1259][^ref-1199]

### 여러 요청 창구를 하나의 요청 형식으로 받기

Open-RMF 작업 요청 스키마는 범주와 설명만 필수로 두고 요청자·레이블·요청 시각·우선순위를 선택 항목으로 둔다. [사실][^ref-125] 로봇 통신 규격인 VDA 5050 3.0.0판(공식 저장소 main, 발행일 미확인)은 플릿 관제와 로봇 사이 통신을 다루며, 현장 사용자·업무 담당자가 운반 요청을 관제에 올리는 방법은 정하지 않고 프로젝트 조정·수행 절차도 범위 밖에 둔다. [사실][^ref-031] 물리 창구로는 버튼으로 로봇을 부르는 장치가 제품으로 제시된다. [추정] 벤더 주장[^ref-1268] 사례에서는 안내 데스크나 프런트를 거쳐 사람이 요청을 받아 처리하는 방식이 보고된다. [사실][^ref-944][^ref-1264]

### 역할 기반 권한

Open-RMF 웹 API 서버(rmf-web api-server)는 OpenID Connect 액세스 토큰(JSON Web Token, JWT)으로 사용자를 확인하고, 역할·동작·권한 그룹 세 요소로 권한을 판정하며(관리자는 모든 그룹에 모든 동작 가능), 여러 관계형 데이터베이스(PostgreSQL·SQLite·MySQL·MariaDB)를 지원하고 기본값은 메모리 내 SQLite 다. [사실][^ref-762] 누가 어떤 요청을 올릴 수 있는지는 [역할 기반 접근 통제](../../glossary/role-based-access-control.md)로 나눌 수 있다.

### 임시 통제 구역의 선언·해제 기록

Open-RMF 차선 폐쇄 요청 메시지(rmf_fleet_msgs/LaneRequest)는 플릿 이름, 열 차선 id 목록, 닫을 차선 id 목록 세 필드만 가지며 요청자·사유·유효 기간·승인 정보를 담는 필드는 없다(확인일 2026-09-30). [사실][^ref-569] 그래서 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지는 메시지 규격이 아니라 운영 절차와 그 위의 요청·권한 계층(예: 역할 기반 API 서버)에서 정하고 기록해야 할 것으로 보인다. [추정][^ref-569][^ref-762] 용어는 [차선 폐쇄](../../glossary/lane-closure.md)를 참고한다. 이 절차를 공개한 병원·상업 시설 사례는 찾지 못했다(11절).

### 구조화된 교대 인수인계

공정 산업 지침과 연구는 교대 인수인계를 대면 논의, 양방향(수신 확인) 대화, 교대 일지 기록으로 하도록 권고한다. [사실][^ref-1258][^ref-1259] Brazier·Pacitti(2008)는 인수인계 실패 원인으로 핵심 운전 정보의 누락, 표준화되지 않은 비공식적 방식, 대면·양방향 대화의 부재, 교대 기록(문서화) 부족을 든다. [사실][^ref-1259] 의료에서는 I-PASS 같은 구조화 인계 프로그램이 쓰인다(4절). [사실][^ref-1267] 이 근거는 공정 산업·의료 분야의 방법 참고이며, 로봇 관제 교대에도 옮길 수 있을 것으로 보이나 여러 로봇을 운영하는 관제의 인계 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외 등)을 정한 공개 절차나 표준은 이번 조사에서 찾지 못했다. [추정][^ref-1258][^ref-1259][^ref-1267]

### 전담 운영 조직

한림대학교성심병원의 커맨드센터는 사용 시나리오 개발, 업무 프로세스 조율, 실시간 모니터링과 문제 대응을 맡는다(2024년 보도 기준). [사실][^ref-1199][^ref-944] 반면 전담 조직 없이 로봇의 부서 소속이 불분명했던 호텔에서는 정비 책임과 부서 간 소통 부담이 보고되었다. [사실][^ref-1260]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-125]: Open-RMF (open-rmf/rmf_api_msgs 저장소), rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-30
[^ref-762]: Open-RMF (open-rmf/rmf-web 저장소), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-569]: Open-RMF (open-rmf/rmf_internal_msgs 저장소), rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-1258]: UK Health and Safety Executive (HSE) (humanfactors101.com 게재본), Human Factors Briefing Note No. 8 — Safety-Critical Communications, 2005, https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1259]: Brazier, A., & Pacitti, B. (IChemE Hazards XX), Improving shift handover and maximising its value to the business, 2008, https://www.icheme.org/media/9743/xx-paper-48.pdf, 접근일 2026-09-30
[^ref-1260]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30
[^ref-1264]: 한국일보, “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인), 2017-04-18, https://www.hankookilbo.com/news/article/201704180418820469, 접근일 2026-09-30
[^ref-1267]: Blazin, L. J. 외 (Pediatric Quality & Safety), Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings, 2020-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/, 접근일 2026-09-30
[^ref-1268]: OMRON Industrial Automation Europe, Autonomous Mobile Robots (AMR), 미확인, https://industrial.omron.eu/en/products/autonomous-mobile-robot, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s7.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-125, ref-762, ref-569, ref-1258, ref-1265, ref-1269]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#7
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 관련 표준·프레임워크·오픈소스

# 40. 운영 절차·요청 창구 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 요청 형식과 권한은 오픈소스 규격에서, 사용자 운영 요구와 작업 지침은 표준·법령에서, 교대 인수인계는 공정 산업 지침에서 근거를 찾을 수 있다. [사실][^ref-125][^ref-1265][^ref-1269][^ref-1258]
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

요청 형식과 권한은 오픈소스 규격에서, 사용자 운영 요구와 작업 지침은 표준·법령에서, 교대 인수인계는 공정 산업 지침에서 근거를 찾을 수 있다. [사실][^ref-125][^ref-1265][^ref-1269][^ref-1258]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) | 오픈소스 | 범주·설명을 필수로, 요청자·레이블·시각·우선순위·플릿 이름을 선택 항목으로 두는 요청 형식의 예. [사실][^ref-125] | 공식 저장소, 확인일 2026-09-30 |
| Open-RMF rmf-web API 서버 | 오픈소스 | OpenID Connect 토큰 인증과 역할·동작·권한 그룹 기반 권한 판정. [사실][^ref-762] | 공식 저장소, 확인일 2026-09-30 |
| Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) | 오픈소스 | 플릿 이름·열 차선·닫을 차선 세 필드뿐이며 요청자·사유·기한 필드는 없음. [사실][^ref-569] | 공식 저장소, 확인일 2026-09-30 |
| [VDA 5050](../../glossary/vda-5050.md) 3.0.0판 | 표준 | 플릿 관제–로봇 통신만 다루며 사용자 요청 접수와 프로젝트 조정·수행 절차는 범위 밖. [사실][^ref-031] | 공식 저장소 main, 발행일 미확인 |
| ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 | 표준 | 2026-04-23 발행, 77쪽. 사용자가 제조사·통합자가 준 정보를 적용해 산업용 이동로봇(Industrial Mobile Robot, IMR) 응용과 운영 환경을 안전하게 운용·정비하기 위한 요구사항을 정하며, 위험성평가, 응용·현재 운영 환경의 변경 관리, 수명주기 전반의 인원 안전을 강조한다(검색 요약 기준). [사실][^ref-1265] | 원문 미열람 |
| 산업안전보건기준에 관한 규칙 제222조(교시 등) | 법령 | 적용 대상은 산업용 로봇의 작동범위에서 하는 교시 등 작업이다. 사업주가 조작방법·순서, 매니퓰레이터 속도, 2명 이상 작업 시 신호방법, 이상 발견 시 조치, 이상으로 정지한 뒤 재가동할 때의 조치에 관한 지침을 정해 따르게 하고, 기동스위치 등에 작업 중 표시를 하도록 요구한다. [사실][^ref-1269] | 국가법령정보센터, 시행 2025-09-01 판 |
| HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications | 프레임워크 | 교대 인수인계를 대면 논의·양방향(수신 확인) 대화·교대 일지 기록으로 하도록 권고하는 공정 산업 지침. [사실][^ref-1258] | 2005, 원문 미열람 |

산업안전보건기준에 관한 규칙 제222조는 로봇 교시 작업의 안전 지침이므로 ROP 직접 범위가 아니라 사업주·제조사가 맡는 연계 대상으로 본다(9절). 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-125]: Open-RMF (open-rmf/rmf_api_msgs 저장소), rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-30
[^ref-762]: Open-RMF (open-rmf/rmf-web 저장소), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-569]: Open-RMF (open-rmf/rmf_internal_msgs 저장소), rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-1258]: UK Health and Safety Executive (HSE) (humanfactors101.com 게재본), Human Factors Briefing Note No. 8 — Safety-Critical Communications, 2005, https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1265]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-1269]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등), 2025-09-01, https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s4.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 핵심 개념과 용어"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-125, ref-762, ref-1258, ref-1259, ref-1260, ref-1267, ref-1268]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#4
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 핵심 개념과 용어

# 40. 운영 절차·요청 창구 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 요청을 받는 쪽(작업 요청·권한·호출 장치)과 사람 사이의 넘김(교대 인수인계·역할)으로 나뉜다.
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 요청을 받는 쪽(작업 요청·권한·호출 장치)과 사람 사이의 넘김(교대 인수인계·역할)으로 나뉜다.

- **작업 요청(Task Request)** — [오픈 RMF](../../glossary/open-rmf.md)(Open Robotics Middleware Framework)의 작업 요청 JSON 스키마는 작업 범주(category)와 범주에 맞는 설명(description)만 필수로 두고, 요청자 식별자(requester), 요청 목적 레이블(labels), 요청 시각, 가장 이른 시작 시각, 우선순위, 수행을 허용할 플릿 이름을 선택 항목으로 둔다(확인일 2026-09-30). [사실][^ref-125]
- **역할 기반 권한(Role-Based Access Control, RBAC)** — 사용자에게 역할을 주고 역할별로 허용 동작을 정하는 방식이다([역할 기반 접근 통제](../../glossary/role-based-access-control.md)). Open-RMF 웹 API 서버는 역할·동작·권한 그룹 세 요소로 권한을 판정한다(확인일 2026-09-30). [사실][^ref-762]
- **호출 버튼(Call Button)** — OMRON은 버튼 하나를 눌러 자율이동로봇(Autonomous Mobile Robot, AMR)을 지정 위치로 부르는 입출력 장치(Mobile I/O Box)를 제품으로 제시한다(확인일 2026-09-30). [추정] 벤더 주장[^ref-1268]
- **교대 인수인계(Shift Handover)** — 나가는 근무조가 들어오는 근무조에게 설비·작업 상태와 위험 정보를 넘기는 절차로, 공정 산업 지침과 연구는 대면 논의, 양방향(수신 확인) 대화, 교대 일지 기록을 권고한다(2005년·2008년). [사실][^ref-1258][^ref-1259]
- **I-PASS 인계 프로그램(I-PASS Handoff Program)** — 질병 중증도·환자 요약·할 일 목록·상황 인식과 비상 계획·수신자의 요약 확인 다섯 항목으로 의료진 인계를 구조화한 프로그램이다. [사실][^ref-1267] Blazin 외(2020)는 Starmer 외 연구에서 소아 병원 9곳 전공의의 의료 오류가 23%, 예방 가능한 유해 사건이 30% 줄었다고 서술하며, 이 수치는 원 연구를 인용한 2차 서술이고 교차 확인되지 않았다. [사실][^ref-1267]
- **역할 모호성(Role Ambiguity)** — 로봇 같은 새 설비의 운영·정비 책임이 어느 부서·사람에게 있는지 불분명한 상태로, Fu 외(2022) 호텔 직원 면담에서 사용 저항 요인과 함께 보고되었다. [사실][^ref-1260]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-125]: Open-RMF (open-rmf/rmf_api_msgs 저장소), rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-30
[^ref-762]: Open-RMF (open-rmf/rmf-web 저장소), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-1258]: UK Health and Safety Executive (HSE) (humanfactors101.com 게재본), Human Factors Briefing Note No. 8 — Safety-Critical Communications, 2005, https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1259]: Brazier, A., & Pacitti, B. (IChemE Hazards XX), Improving shift handover and maximising its value to the business, 2008, https://www.icheme.org/media/9743/xx-paper-48.pdf, 접근일 2026-09-30
[^ref-1260]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30
[^ref-1267]: Blazin, L. J. 외 (Pediatric Quality & Safety), Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings, 2020-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/, 접근일 2026-09-30
[^ref-1268]: OMRON Industrial Automation Europe, Autonomous Mobile Robots (AMR), 미확인, https://industrial.omron.eu/en/products/autonomous-mobile-robot, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s8.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 대표 연구와 자료"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1258, ref-1259, ref-1260, ref-1263, ref-1267]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#8
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 대표 연구와 자료

# 40. 운영 절차·요청 창구 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 교대 인수인계 방법은 공정 산업·의료 연구에서, 요청 창구와 역할 문제는 병원·호텔의 로봇 도입 연구에서 근거를 얻는다. [사실][^ref-1259][^ref-1267][^ref-1263][^ref-1260]
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

교대 인수인계 방법은 공정 산업·의료 연구에서, 요청 창구와 역할 문제는 병원·호텔의 로봇 도입 연구에서 근거를 얻는다. [사실][^ref-1259][^ref-1267][^ref-1263][^ref-1260]

- UK Health and Safety Executive, Human Factors Briefing Note No. 8 — Safety-Critical Communications(2005) — 공정 산업 맥락에서 교대 인수인계를 대면 논의, 양방향(수신 확인) 대화, 교대 일지 기록으로 하도록 권고한다. [사실][^ref-1258]
- Brazier·Pacitti, Improving shift handover and maximising its value to the business(2008) — 인수인계 실패 원인(정보 누락, 비공식 방식, 대면·양방향 대화 부재, 문서화 부족)을 들고 구조화된 일지, 대면 회의, 양방향 대화, 표준 체크리스트를 권고한다. [사실][^ref-1259]
- Blazin 외, Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings(2020) — I-PASS 다섯 요소를 설명하고 Starmer 외 연구의 의료 오류 23%·예방 가능한 유해 사건 30% 감소를 인용한 2차 서술이며, 교차 확인되지 않았다. [사실][^ref-1267]
- Mutlu·Forlizzi, Robots in Organizations(HRI 2008) — 병원 배송 로봇의 15개월 민족지 연구로, 병동의 업무 흐름·사회적·환경 요인에 따라 같은 로봇의 수용이 크게 달랐음을 보였다. [사실][^ref-1263]
- Fu·Zheng·Wong, The perils of hotel technology: The robot usage resistance model(2022) — 중국 고급 호텔 직원 19명 면담으로 로봇의 부서 소속 모호와 추가 업무를 사용 저항 요인으로 도출했다. [사실][^ref-1260]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1258]: UK Health and Safety Executive (HSE) (humanfactors101.com 게재본), Human Factors Briefing Note No. 8 — Safety-Critical Communications, 2005, https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1259]: Brazier, A., & Pacitti, B. (IChemE Hazards XX), Improving shift handover and maximising its value to the business, 2008, https://www.icheme.org/media/9743/xx-paper-48.pdf, 접근일 2026-09-30
[^ref-1260]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30
[^ref-1263]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1267]: Blazin, L. J. 외 (Pediatric Quality & Safety), Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings, 2020-07, https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s11.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 열린 질문"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-569]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#11
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 열린 질문

# 40. 운영 절차·요청 창구 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 요청 창구와 교대 절차는 사례·표준 근거가 얇아 다음 질문이 남아 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

요청 창구와 교대 절차는 사례·표준 근거가 얇아 다음 질문이 남아 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-203** (상태: 열림) 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? 이번 실행에서는 차선 폐쇄 메시지에 요청자·사유·유효 기간 필드가 없다는 부분 근거만 확인했고 공개 절차 사례는 찾지 못해 미해결로 둔다. [사실][^ref-569]
- (신규, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-18) 여러 제조사 로봇을 한 관제에서 운영할 때 교대 인수인계로 넘길 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외)을 정한 공개 절차나 체크리스트가 있는가?
- (신규, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-18) 병원·호텔에서 안내 데스크·프런트 담당자가 로봇 요청을 대신 입력하는 방식과 현장 사용자가 직접 요청하는 방식의 처리 시간·오류·업무 부담을 비교한 연구가 있는가?
- (신규, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-18) ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가?
- (신규, 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-18) 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-569]: Open-RMF (open-rmf/rmf_internal_msgs 저장소), rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s10.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 다른 연구영역과의 연결"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-125, ref-762, ref-569, ref-1259, ref-1260, ref-1199, ref-1263, ref-1264, ref-1265, ref-1266, ref-1269]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#10
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 다른 연구영역과의 연결

# 40. 운영 절차·요청 창구 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 요청이 들어오는 창구, 요청이 바뀌는 작업, 요청을 막거나 허용하는 조건, 요청을 처리하는 사람과 조직 쪽으로 다음 영역과 이어진다. [추정][^ref-125][^ref-762][^ref-569]
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

요청이 들어오는 창구, 요청이 바뀌는 작업, 요청을 막거나 허용하는 조건, 요청을 처리하는 사람과 조직 쪽으로 다음 영역과 이어진다. [추정][^ref-125][^ref-762][^ref-569]

- [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — 대화는 요청 창구의 하나다. [추정][^ref-125]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 업무 시스템에서 발생한 요청을 받는다. [추정][^ref-1264]
- [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md) — 접수한 요청을 작업으로 바꾼다. [추정][^ref-125]
- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 요청의 우선순위·허용 플릿이 배정 입력이 된다. [추정][^ref-125]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 사례의 승강기 연동과 승강기 문제. [추정][^ref-1264][^ref-1266]
- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 임시 통제 구역의 선언·해제. [추정][^ref-569]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 교대 인수인계용 운영 상태 요약과 기록. [추정][^ref-1259]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 로봇의 도움 요청 알림과 대응. [추정][^ref-1263]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 이상 정지 뒤 재가동 절차. [추정][^ref-1269]
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 교시 작업 지침과 위험성평가. [추정][^ref-1269][^ref-1265]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 사용자 요구 표준 ANSI/A3 R15.08-3-2026. [추정][^ref-1265]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 요청 권한의 역할 기반 판정. [추정][^ref-762]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 적재·하역과 알림 응답 같은 현장 협업. [추정][^ref-1263]
- [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) — 전담 운영 조직과 직원 교육 부담. [추정][^ref-1199][^ref-1260]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 부서·사업자 사이의 정비 책임. [추정][^ref-1260]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 직원 저항과 수용. [추정][^ref-1263][^ref-1260][^ref-1266]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 요청 창구·운영 조직 사례. [추정][^ref-1199][^ref-1263]
- [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) — 호텔 요청 창구·역할 사례. [추정][^ref-1264][^ref-1260]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-125]: Open-RMF (open-rmf/rmf_api_msgs 저장소), rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-30
[^ref-762]: Open-RMF (open-rmf/rmf-web 저장소), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-569]: Open-RMF (open-rmf/rmf_internal_msgs 저장소), rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-09-30
[^ref-1259]: Brazier, A., & Pacitti, B. (IChemE Hazards XX), Improving shift handover and maximising its value to the business, 2008, https://www.icheme.org/media/9743/xx-paper-48.pdf, 접근일 2026-09-30
[^ref-1260]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-1263]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1264]: 한국일보, “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인), 2017-04-18, https://www.hankookilbo.com/news/article/201704180418820469, 접근일 2026-09-30
[^ref-1265]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-1266]: Proof News (Varsha Bansal), Meet the Robot That Nurses Unplugged, 2026-06-09, https://www.proofnews.org/moxi/, 접근일 2026-09-30
[^ref-1269]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등), 2025-09-01, https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-18/pages/topics/2026/2026-09-30-area40-s3.md

```markdown
---
title: "40. 운영 절차·요청 창구 — 왜 중요한가"
type: topic
category: "J. 현장 운영·관제"
primary_area_no: 40
related_areas: [12, 16, 22, 23, 24, 25, 31, 32, 37, 38, 48, 50, 51, 56, 58, 60, 63, 64]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-125, ref-1260, ref-1199, ref-944, ref-1263, ref-1265, ref-1269]
last_run: 2026-09-30
version: 1
split_from: docs/categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md#3
---

[홈](../../index.md) › [주제](../index.md) › 40. 운영 절차·요청 창구 — 왜 중요한가

# 40. 운영 절차·요청 창구 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 요청 창구 기술(작업 요청 API 스키마, 역할 기반 권한, 호출 버튼, 프런트 경유 입력)과 사용자 측 운영 요구 표준·교시 작업 지침 법령은 있지만, 여러 제조사 로봇을 한 관제에서 운영할 때의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 이번 조사에서 확인되지 않았고 현장마다 따로 정해지는 것으로 보인다. [추정][^ref-125][^ref-1265][^ref-1269][^ref-1199][^ref-1260]
- 이 페이지는 [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

요청 창구 기술(작업 요청 API 스키마, 역할 기반 권한, 호출 버튼, 프런트 경유 입력)과 사용자 측 운영 요구 표준·교시 작업 지침 법령은 있지만, 여러 제조사 로봇을 한 관제에서 운영할 때의 요청 접수·교대 인수인계 절차를 정한 공개 표준은 이번 조사에서 확인되지 않았고 현장마다 따로 정해지는 것으로 보인다. [추정][^ref-125][^ref-1265][^ref-1269][^ref-1199][^ref-1260]

절차와 역할이 분명하지 않을 때의 문제는 여러 현장에서 보고되었다. 병원 배송 로봇의 15개월 민족지 연구에서 같은 로봇이 내과 병동에서는 직원 저항을 낳고 산후 병동에서는 업무 흐름에 통합되었다(2008년). [사실][^ref-1263] 중국 고급 호텔 직원 면담에서는 로봇이 어느 부서에 속하는지 불분명해 정비 책임과 부서 간 소통 부담이 생겼다(2022년). [사실][^ref-1260]

반대로 한국의 한림대학교성심병원은 전담 부서인 커맨드센터가 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다(2024년 보도 기준). [사실][^ref-1199][^ref-944] 로봇 개별 성능만큼 누가 요청을 받고 누가 로봇을 책임지는지가 현장 수용을 가른다는 점이 이 영역을 따로 다루는 이유다. [의견][^ref-1263][^ref-1260]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [40. 운영 절차·요청 창구](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-125]: Open-RMF (open-rmf/rmf_api_msgs 저장소), rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-30
[^ref-1260]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-09-30
[^ref-1199]: 지디넷코리아, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-09-30
[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (제목 일부만 확인), 2024-04, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-09-30
[^ref-1263]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-1265]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-09-30 (원문 미열람)
[^ref-1269]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등), 2025-09-01, https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-18 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-18 | 40. 운영 절차·요청 창구 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1144건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 320개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- ethical-black-box: 윤리적 블랙박스 (Ethical Black Box (EBB))
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
- hardware-in-the-loop: 하드웨어 인 더 루프 (Hardware-in-the-Loop (HiL))
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
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
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
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
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
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
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
- sim-vs-real-correlation-coefficient: 시뮬레이션–현실 상관 계수 (Sim-vs-Real Correlation Coefficient (SRCC))
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

### docs/open-questions.md (요약: 대상 영역 [40] 에 걸린 1건 / 전체 258건)

```markdown
- oq-203 [열림] 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (영역 16, 40, 63)
```
