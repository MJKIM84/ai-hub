(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-05
- date: 2026-10-09
- run_type: category_link (대분류 연결)
- 대상: 대분류 J. 현장 운영·관제 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko

## 입력

### runs/2026-10-09-05/target.json

```json
{
  "run_id": "2026-10-09-05",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 138,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
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
  "selection_rationale": "CLI 지정 run_type=category_link"
}
```

### runs/2026-10-09-05/research.json

```json
{
  "run_id": "2026-10-09-05",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "J. 현장 운영·관제"
  },
  "gaps": [
    "대분류 페이지 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. J. 현장 운영·관제의 네 세부영역(37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구)과 다른 16개 대분류를 잇는 연결이 하나도 정리되지 않았다",
    "38. 모니터링·이상 탐지·원인 분석과 39. 운영 성과 측정·개선 페이지의 10절은 개정 전 분류(2026-09-25) 기준으로 쓰였다. 따라서 K. 플랫폼 아키텍처·인프라, M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회, Q. 현장 유형별 적용과의 연결 근거가 약하다",
    "B. 로봇 온톨로지와 J. 현장 운영·관제를 잇는 검증된 근거가 게시 페이지에 없다",
    "37. 관제 화면·실행 기록과 M. 안전(사고 조사 기록), P. 거버넌스·법규·사회(기록 보관 의무)의 연결은 열린 질문(oq-239, oq-252)뿐이고 근거 자료가 없다",
    "38. 모니터링·이상 탐지·원인 분석의 경보 설계를 H. 실행·협업·예외 복구의 운영자 대응(31. 사람–로봇 협업)과 잇는 근거 자료가 없다"
  ],
  "research_questions": [
    "운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]",
    "지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]",
    "37. 관제 화면·실행 기록이 남기는 실행 기록은 C. 채팅 기반 구성·운영(11. 채팅으로 실제 상황 시뮬레이션 재현, 12. 채팅으로 업무 지시·오케스트레이션), I. 설계·시뮬레이션(36. 가상 시운전·실제 상황 재현), K. 플랫폼 아키텍처·인프라(43. 데이터·관측성·배포), M. 안전(50. 안전 표준·인증·사고 조사), P. 거버넌스·법규·사회(59. 법·규제·보험·라이선스)에 무엇을 넘겨주는가? (oq-131, oq-239, oq-252 관련)",
    "38. 모니터링·이상 탐지·원인 분석은 F. 연동과 E. 사물·사람·실시간 상태에서 어떤 신호를 받는가? 그리고 판정 결과와 경보를 H. 실행·협업·예외 복구, G. 계획·최적화, L. AI·학습 기술, N. 보안·개인정보 쪽으로 어떻게 넘기는가? (oq-033, oq-072, oq-082, oq-210 관련)",
    "39. 운영 성과 측정·개선의 지표는 A. 기획·사업(투자 효과), F. 연동(주문 단위 지표), G. 계획·최적화·I. 설계·시뮬레이션(정책 비교), N. 보안·개인정보·P. 거버넌스·법규·사회(작업자 데이터)와 어디서 만나는가? (oq-015, oq-084 관련)",
    "40. 운영 절차·요청 창구의 요청 접수·권한·통제 구역·교육은 F. 연동, D. 공간·지도 모델, N. 보안·개인정보, M. 안전, O. 검증·도입·수명주기, P. 거버넌스·법규·사회, Q. 현장 유형별 적용과 어떻게 이어지는가? (oq-203, oq-265, oq-266 관련)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델 연결 근거: Open-RMF rmf_visualization 은 층 평면도 위에 로봇 위치, 문·승강기, 주행 그래프, 예측 궤적을 겹쳐 표시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1093"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "37. 관제 화면·실행 기록 페이지 7절 표에 따르면 rmf_visualization 은 층 평면도 위에 로봇 위치·문·승강기·주행 그래프·예측 궤적을 표시한다. 관제 화면이 층별 지도를 바탕으로 그려진다는 뜻이다. (발행일 미확인, 확인일 기준) (재인용: 2026-09-30-13)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Open-RMF 작업 이벤트 로그는 작업·단계·사건의 3계층으로 나뉘고 MCAP 은 시각 색인을 둔 기록 형식이어서, 37. 관제 화면·실행 기록이 남긴 기록은 시간축 재현의 입력이 될 수 있어 보인다. 다만 이 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식은 확인되지 않았다(oq-131).",
      "tag": "추정",
      "source_ids": [
        "ref-1094",
        "ref-1096"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_log.json(오늘 원문 열람)은 task_id 와 작업 수준 log, 단계 번호별 phases 의 log, 사건 번호별 events 로그 배열을 둔다. MCAP 명세는 시각 색인을 둔 기록 컨테이너다(37. 관제 화면·실행 기록 페이지 7절). 변환 규칙은 oq-131 에서 미해결이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현: 11. 채팅으로 실제 상황 시뮬레이션 재현은 재현 결과를 실제 기록(시각·위치·사건 순서)과 비교해야 한다. 그 실제 기록은 37. 관제 화면·실행 기록이 정규화해 저장하는 실행 기록에서 나올 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1094",
        "ref-1096"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "11. 채팅으로 실제 상황 시뮬레이션 재현 페이지의 리스트업 항목 '재현 충실도 확인'은 실제 기록의 시각·위치·사건 순서와 비교하는 일이다. 37. 관제 화면·실행 기록 페이지 9절은 정규화한 실행 기록의 영속 저장과 재생을 ROP 직접 범위로 본다(추정).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 12. 채팅으로 업무 지시·오케스트레이션은 진행 상황 질의에 실행 기록과 시각을 근거로 답한다. Open-RMF 작업 상태 스키마의 상태 값, 시작·종료 시각, 단계 목록, 취소·강제 종료 기록이 그 답의 근거 자료가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_state.json(오늘 원문 열람)의 status 는 uninitialized·blocked·error·failed·queued·standby·underway·delayed·skipped·canceled·killed·completed 12개 값이다. 이 밖에 unix_millis_start_time·finish_time, estimate_millis, phases·completed·active·pending, interruptions·cancellation·killed 를 둔다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ F. 연동의 20. 로봇·제조사 관제 연동 연결 근거: VDA 5050 3.0.0 은 차량 위치·계획 경로를 시각화 시스템에 보내는 visualization 토픽을 상태(state) 토픽과 따로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "37. 관제 화면·실행 기록 페이지 7절 표에 따르면 VDA 5050 3.0.0 은 visualization·state 토픽을 분리한다. 같은 페이지 9절은 ROP가 제조사가 내보내는 상태를 받는 인터페이스를 맡는다고 본다(추정). (발행일 미확인, 확인일 기준) (재인용: 2026-09-30-13)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 연결 근거: Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원한다. 따라서 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다.",
      "tag": "사실",
      "source_ids": [
        "ref-762",
        "ref-302"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "api-server README(오늘 원문 열람)는 tortoise-orm 으로 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하고 기본은 메모리 내 SQLite 인스턴스라고 적는다. 스키마 변경은 aerich 로 이전한다. rmf-web README 도 기본 저장을 비영속으로 둔다(37. 관제 화면·실행 기록 페이지 7절). 두 문서는 같은 프로젝트라 독립 출처가 아니다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업 연결 근거: 다중 로봇 인터페이스 연구(Roldán 외, Sensors 2017)는 운영자 상황 인식을 위한 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1099"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "37. 관제 화면·실행 기록 페이지 3절은 다중 로봇 인터페이스 연구(Roldán 외)가 정보 선별과 관련 정보로의 주의 유도를 설계 요건으로 들었다고 정리한다. 이 연구의 몰입·예측 실험은 실험실 조건이다. (재인용: 2026-09-30-13)",
      "as_of": "2017-07-27",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF 연결 근거: 설명 가능한 다중 에이전트 경로 찾기 연구(Kottinger·Almagor·Lahijanian, ICAPS 2022)는 경로 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 문제를 다루지만 알고리즘 수준의 연구다.",
      "tag": "사실",
      "source_ids": [
        "ref-1098"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "37. 관제 화면·실행 기록 페이지 9절은 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 표시를 ROP 직접 범위로 보며, 근거로 ref-1098 을 든다. 8절은 이 연구를 실험실·알고리즘 수준으로 분류한다. (재인용: 2026-09-30-13)",
      "as_of": "2022-02",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 한림대학교의료원 협약은 안면 인식 기반 수령 인증과 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 한 것이다. 이를 보면 수령인 확인(17. 작업 대상·자산 식별과 인계 추적)과 배송 이력 기록(37. 관제 화면·실행 기록)은 완료·인계 단계에서 한 기록으로 묶일 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1103"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "아주경제 2025-04-07 보도에 따르면 현대차·기아와 한림대학교의료원은 병원 맞춤형 배송 로봇·관제 시스템, 안면 인식 기반 수령 인증, 특수 물품 배송 이력 관리 시스템을 공동 개발하기로 했다. 협약·개발 계획 단계이며 운영 결과는 미확인이다.",
      "as_of": "2025-04-07",
      "site_type": "병원",
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ M. 안전의 50. 안전 표준·인증·사고 조사 연결 근거: Winfield 외(2022)의 윤리적 블랙박스 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록하는 장치나 소프트웨어 모듈을 제안한다. 이 초안은 단일 소셜 로봇을 대상으로 하며 플릿·플랫폼 수준 기록은 다루지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1360"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2205.06564(2022-05-13 제출, 초록 열람): 윤리적 블랙박스(EBB)는 소셜 로봇의 운영 데이터(센서·구동기·제어 결정)를 안전하게 기록해 사고와 아차 사고 조사를 지원한다. 표준 초안은 논문 부록에 실렸고 토론용이다.",
      "as_of": "2022-05-13",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "연계 대상: J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스 연결 근거: 국내 병원·약국은 2018-05-18부터 마약류 취급 내역을 마약류통합관리시스템에 전산 보고할 수 있게 되었고, 종전 마약류 관리대장은 2년간 보관해야 한다고 보도되었다. 로봇 배송 이력이 이 보고·보관 대상에 드는지는 확인하지 못했다(oq-239).",
      "tag": "사실",
      "source_ids": [
        "ref-1364"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "데일리팜 2018-07-13 보도(원문 열람)에 따르면 2018-05-18부터 병원·약국의 마약류 취급 내역을 마약류통합관리시스템에 전산 보고한다. 기사는 '종전 마약류 관리대장은 2년간 보관해야 한다'고 적는다. 법령 원문과 현행 여부는 미확인이다.",
      "as_of": "2018-07-13",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ Q. 현장 유형별 적용의 63. 병원·의료 연결 근거: 국내 병원 현장에서 관제 시스템과 특수 물품 배송 이력 관리를 함께 개발하기로 한 협약이 2025-04 보도되었다. 37. 관제 화면·실행 기록 페이지가 찾은 현장 근거는 이 병원 사례 한 건뿐이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1103"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "37. 관제 화면·실행 기록 페이지 5절은 현장 근거로 병원 한 건(한림대학교의료원 협약)만 찾았다고 적는다. 물류창고·제조 공장·상업 시설·가정·실외·기타 사례는 2026-09-30 조사에서 찾지 못했다.",
      "as_of": "2025-04-07",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Open-RMF 로봇 상태는 상태 값·문제 목록과 함께 기록 시각을 담는다. 그러므로 원인 구분은 18. 실시간 세계 상태·데이터 일관성이 시각과 함께 유지하는 로봇·문·작업의 현재 상태를 같은 시간축에 맞춘 데이터를 쓸 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-148",
        "ref-051",
        "ref-313"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "robot_state.json(오늘 원문 열람)은 name, status, task_id, unix_millis_time, location, battery(0~1), issues(운영자 대응이 필요한 문제), commission, mutex_groups 를 둔다. 38. 모니터링·이상 탐지·원인 분석 페이지 10절은 같은 시간축에 맞춘 데이터가 필요하다고 본다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ F. 연동의 20. 로봇·제조사 관제 연동: VDA 5050 의 오류 수준과 연결 상태(CONNECTION_BROKEN), MassRobotics 의 외부 사건 대기(waitingExternalEvent), Open-RMF 의 작업 지연·차단은 서로 다른 어휘로 보고된다. 그래서 20. 로봇·제조사 관제 연동에서 들어온 신호를 ROP 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. 공통 매핑 표준은 확인되지 않았다(oq-033, oq-073).",
      "tag": "추정",
      "source_ids": [
        "ref-051",
        "ref-449",
        "ref-230",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "38. 모니터링·이상 탐지·원인 분석 페이지 3절은 이종 로봇 현장에서 VDA 5050 오류 수준·연결 끊김, MassRobotics 외부 사건 대기, Open-RMF 작업 지연·차단이 서로 다른 어휘로 보고되며 대응표가 없다고 정리한다(추정). (재인용: 2026-09-25-48)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ F. 연동의 22. 설비·건물 시스템 연동 연결 근거: Open-RMF 문 모드는 closed·moving·open·offline·unknown 다섯 값이다. 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-313",
        "ref-283"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "38. 모니터링·이상 탐지·원인 분석 페이지 5절 제약 칸에 따르면 문 노드는 /door_states 로 상태를 발행하고 문 모드는 다섯 값이다. 문 어댑터는 상태 감독자 역할을 한다. 문 개폐 제어 자체는 연계 대상(시설·설비 제어)이다. (재인용: 2026-09-25-48)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성 연결 근거: Open-RMF 작업 상태 스키마는 blocked·error·failed·delayed·canceled·killed 를 포함한 12개 상태 값을 둔다. 또 작업에 걸린 중단(interruptions)·취소·강제 종료 요청 기록을 담아, 실행 결과 확인과 이상 탐지가 같은 기록을 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "task_state.json(오늘 원문 열람): status 열거값 12개, interruptions(요청 토큰별 중단), cancellation·killed(요청 시각·라벨), unix_millis_start_time·finish_time.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: Open-RMF 경보(Alert) 메시지는 심각도 등급(info 0·warning 1·error 2), 운영자가 고를 수 있는 응답 목록(responses_available), 관련 작업 id 를 담는다. 원인 판정 뒤의 운영자 선택이 이 메시지로 복구 조치에 넘어간다.",
      "tag": "사실",
      "source_ids": [
        "ref-448"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Alert.msg(오늘 원문 열람)는 id, title·subtitle·message, display(기본 true), tier(info·warning·error), responses_available(응답이 필요 없으면 비움), alert_parameters, task_id(관련 작업이 없으면 비움)로 이루어진다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f18",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업 연결 근거: 다중 로봇 수색·구조 과제 실험(Mehrotra·Sycara·Lewis·Chien·Wang, HFES 2011)에서 경보를 제한 없이 띄운 조건은 가장 중요한 경보 하나만 보여 준 조건보다 운영자가 고장을 더 빨리 발견했다. 탐색 면적과 발견한 피해자 수에는 차이가 없었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1363"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Pitt D-Scholarship 초록(원문 열람): 경보 없음, 자유 표시(ADSC), 최상위 경보만 보이는 의사결정 보조의 세 조건을 비교했다. 탐색 면적과 피해자 수에는 차이가 없었고 자유 표시 조건에서 고장과 피해자를 더 빨리 탐지했다. 실험실 시뮬레이션 조건이다.",
      "as_of": "2011",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업 연결 근거: ANSI/ISA 18.2-2016 은 공정 산업 시설에서 제어 시스템을 거쳐 운영자에게 표시되는 경보 전체의 수명주기 관리 원칙과 절차를 정한다. 다중 로봇 플릿에 특화된 경보 관리 표준은 이번 조사에서 찾지 못했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1359"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ANSI 웹스토어 소개(원문 열람): 경보 시스템의 'lifecycle management' 일반 원칙과 절차를 정한다. 기본 공정 제어·경보판·화재·가스 패키지·안전계장 시스템의 경보를 포함하며 2009년 판을 개정했다. 표준 본문은 유료라 미열람이다.",
      "as_of": "2016",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터는 위치 신뢰도와 실행 행동 증거를 결합해 에이전트를 분류한다. 이로 미루어 실행 기록으로 이상 로봇을 가려 배정 후보에서 빼는 일이 두 영역의 접점이 될 것으로 보인다(oq-082). 물류센터 적용은 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-494"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "G. 계획·최적화 페이지의 연결 절에 따르면 이 연구는 GPS 스푸핑 데이터와 택시 수요로 실험했고 탐지된 적대 에이전트를 이후 계획에서 뺀다. 원문은 미열람이다. (재인용: 2026-09-25-55)",
      "as_of": "2026-08",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: 플랫폼 서비스 쪽 분산 추적(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모은다. 그래서 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다(oq-210).",
      "tag": "추정",
      "source_ids": [
        "ref-447",
        "ref-1361"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "OpenTelemetry 명세 개요는 분산 서비스의 추적·지표·로그 신호를 다룬다(38. 모니터링·이상 탐지·원인 분석 페이지 7절 출처). ros2_tracing 은 LTTng 로 ROS 2 런타임 실행 정보를 모으고 운영체제 추적과 결합할 수 있다(초록). 두 계층을 잇는 공개 사례는 미확인이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 연결 근거: ros2_tracing(Bédard·Lütkebohle·Dagenais, IEEE RA-L 2022)은 저부하 LTTng 추적기로 ROS 2 실행 정보를 모은다. 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가는 평균 0.0033 ms 였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1361"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2201.00393 초록(원문 열람, v4 2022-07-30): 모든 계측을 켠 지연 실험에서 종단 메시지 지연 오버헤드가 평균 0.0033 ms 였고, 저자는 실시간 운영 시스템에 쓸 만하다고 본다. 저자 실험 조건의 값이며 독립 재현은 미확인이다.",
      "as_of": "2022-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: 분류 원문의 교차 규칙은 장애 분석을 38. 모니터링·이상 탐지·원인 분석에 적용되는 AI 연구 방법으로 둔다. 대규모 언어 모델로 로봇 실패를 설명하는 REFLECT(2023) 같은 연구가 두 영역을 잇는 예가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-453"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "38. 모니터링·이상 탐지·원인 분석 페이지 2절 원문 주석은 '장애 분석은 38번'에 적용되는 연구 방법이라고 적는다. 같은 페이지 10절은 LLM 실패 설명(REFLECT)을 그 예로 든다. REFLECT 원문은 미열람이다.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: EU 사이버복원력법은 2026-09-11부터 디지털 요소 제품의 제조자에게 실제 악용되는 취약점과 중대 보안 사고를 24시간 안에 조기 경보하게 한다. 그래서 이상 탐지가 보안 사고를 가려내는 시점이 보고 의무와 맞물릴 수 있어 보인다. 오케스트레이션 플랫폼이 제조자에 해당하는지는 미확인이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1236"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "59. 법·규제·보험·라이선스 조사(실행 2026-09-30-23)에 따르면 제조자는 ENISA 단일 보고 플랫폼으로 24시간 조기 경보, 72시간 통지, 이후 최종 보고를 해야 한다. 플랫폼의 제조자 해당 여부는 그 실행의 열린 질문이다. (재인용: 2026-09-30-23)",
      "as_of": "2026-09-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 39. 운영 성과 측정·개선 페이지는 투자 수익률·순현재가치·회수 기간 같은 재무 평가를 연계 대상으로 둔다. ROP는 그 입력인 처리량·가동률·충전·예외 실행 데이터를 제공한다고 보므로, 운영 지표가 투자 효과 판단으로 넘어가는 지점에서 두 영역이 이어지는 것으로 보인다(oq-268).",
      "tag": "추정",
      "source_ids": [
        "ref-150",
        "ref-139",
        "ref-148"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "39. 운영 성과 측정·개선 페이지 9절(추정)은 재무적 투자 평가와 원가 배분을 상위 업무 영역의 몫으로, 처리량·가동률·충전·예외 실행 데이터 제공과 효과 측정을 ROP 몫으로 본다. 오토스토어 경제성 수치는 벤더 주장이라 여기서 쓰지 않는다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f26",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 연결 근거: Open-RMF 로봇 상태 스키마는 상태 값(uninitialized·offline·shutdown·idle·charging·working·error), 0~1 범위의 배터리, 현재 작업 id, 문제 목록, 기록 시각을 담는다. 이 값은 가동률·충전·오류 시간 지표의 원천이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-148"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "robot_state.json(오늘 원문 열람)의 status 열거값은 7개이고 battery 는 0.0~1.0 이며 task_id·issues·unix_millis_time 을 둔다. 지표 원천이라는 판단은 A. 기획·사업 페이지 연결 절의 추정과 같다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ F. 연동의 23. 업무 시스템 연동: 로봇·작업 상태 기록만으로는 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표를 계산할 수 없다. 이 지표는 23. 업무 시스템 연동을 거쳐 WMS·ERP 주문 데이터와 이어야 계산될 것으로 보인다(oq-015).",
      "tag": "추정",
      "source_ids": [
        "ref-140",
        "ref-148",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "39. 운영 성과 측정·개선 페이지 5절(추정)은 가동률·충전·오류 시간·작업 사이클 타임은 ROP 안에서 계산되지만 완전 주문 이행률·주문 이행 사이클 타임은 WMS·ERP 주문 데이터와 연결해야 계산된다고 본다. SCOR RL.1.1 은 주문의 모든 품목 줄이 완전해야 완전 주문으로 센다.",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "완료·인계",
      "source_unopened": false
    },
    {
      "id": "f28",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화 연결 근거: Omega(2024) 게재 연구는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. 모델·시뮬레이션 조건의 저자 보고값이며 현장 실측이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-146"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "39. 운영 성과 측정·개선 페이지 5절 예외·성과 칸, A. 기획·사업과 G. 계획·최적화 페이지 연결 절에 같은 값과 단서가 실려 있다. 원문은 미열람이다. (재인용: 2026-09-25-14)",
      "as_of": "2024",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f29",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 연결 근거: AMR 물류센터 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. 설계 단계의 충전기 수 결정이 운영 성과 지표에 그대로 나타난다는 뜻이다.",
      "tag": "사실",
      "source_ids": [
        "ref-102"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "39. 운영 성과 측정·개선 페이지 5절 제약 칸에 따르면 충전기 부족은 큰 지연, 과잉은 불필요한 비용으로 이어졌다(2025). 시뮬레이션 결과이며 원문은 미열람이다. (재인용: 2026-09-25-14)",
      "as_of": "2025",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터 연결 근거: 창고 작업자 12명을 반구조화 면담한 연구(Malik·Brandão·Coopamootoo, 2026)는 로봇 운영에 따르는 데이터 감시에 대한 작업자 우려를 확인했다. 연구는 감시 활동 알림·개인정보 통제 같은 작업자 중심 요구를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1278"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "60. 노동·수용성·접근성 조사(실행 2026-09-30-24)의 f5 를 다시 인용했다. 근거는 초록이며, 수동 무시·개인정보 통제·감시 활동 알림을 요구로 제시한다. (재인용: 2026-09-30-24)",
      "as_of": "2026",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 한국 근로자참여법 제20조는 신기계·기술 도입과 사업장 내 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다. 따라서 성과 측정이 개별 작업자의 처리량·위치까지 기록하면 도입 전 노동자 참여 절차가 필요할 가능성이 있다. 법적 해당 여부는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1272",
        "ref-1278"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "60. 노동·수용성·접근성 조사의 f16(제20조 제1항 제9호·제14호)과 f18(추정) 을 39. 운영 성과 측정·개선의 작업자 단위 지표에 적용한 판단이다. (재인용: 2026-09-30-24)",
      "as_of": "2019-04-16",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ Q. 현장 유형별 적용의 61. 물류창고 연결 근거: 로봇 이동형 풀필먼트 시스템 대기행렬 모델(Lamballais 외, 2017)에서는 처리량이 보관 구역 둘레의 작업대 위치에 영향을 받았다. 협업형 AMR 피킹 해석 모델(Ghelichi·Kilaru, 2021)에서는 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우했다.",
      "tag": "사실",
      "source_ids": [
        "ref-096",
        "ref-145"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "39. 운영 성과 측정·개선 페이지 5절 수행 자원 칸에 두 연구의 결과가 실려 있다. 두 연구 모두 모델 연구이며 현장 실측이 아니다. 원문은 미열람이다. (재인용: 2026-09-25-14)",
      "as_of": "2021",
      "site_type": "물류창고",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ Q. 현장 유형별 적용의 62. 제조 공장 연결 근거: ISO 22400-2:2014 는 제조 운영 관리의 핵심성과지표 정의를 다루는 현행판이다. 에너지 관리 KPI 를 더한 개정 1(2017-04)이 있고, 개정판 ISO/DIS 22400-2 의 발행은 2026-09-26 기준 확인되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-139"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "39. 운영 성과 측정·개선 페이지 7절 재검증(2026-09-26)에 따른 내용이다. 이동로봇 플릿에 OEE 를 적용하는 합의된 정의는 oq-016 으로 미해결이다. 원문은 미열람이다.",
      "as_of": "2014",
      "site_type": "제조 공장",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f34",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ F. 연동의 23. 업무 시스템 연동 연결 근거: 미국 ChristianaCare 는 간호사가 키오스크에서 Moxi 로봇을 호출하던 방식에 더해, 로봇을 Cerner 전자의무기록과 연동해 주문이 들어오면 로봇이 물품을 가지러 가게 하는 계획을 밝혔다(2022-08 보도). 실제 운영 결과는 확인하지 못했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1362"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "TechTarget(Hannah Nelson, 2022-08-11, 원문 열람)에 따르면 간호사는 키오스크로 Moxi 를 요청한다. 미국간호재단 보조금으로 코봇 3대를 더해 Cerner EHR 과 연동하면 주문이 들어올 때 로봇이 'go and fetch the supplies needed' 하게 된다.",
      "as_of": "2022-08-11",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f35",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ G. 계획·최적화의 26. 작업 순서·스케줄링: Open-RMF 작업 요청 스키마는 가장 이른 시작 시각과 우선순위만 두고 마감 시각 필드는 두지 않는다. 그래서 요청 창구에서 받은 긴급도·기한을 순서 결정 입력으로 옮기는 규칙이 두 영역의 접점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "G. 계획·최적화 페이지 연결 절(2026-09-25 확인)에 따르면 task_request 스키마의 시각·순서 관련 필드는 가장 이른 시작 시각과 우선순위이고 마감·선후 필드는 없다. 40. 운영 절차·요청 창구 페이지 9절은 요청 형식에 우선순위를 담는 것을 ROP 몫으로 본다(추정).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f36",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: Open-RMF 차선 요청(LaneRequest)은 플릿 이름과 열고 닫을 차선 목록 세 필드만 둔다. 따라서 임시 통제 구역을 누가 왜 언제까지 닫았는지는 40. 운영 절차·요청 창구의 운영 기록이, 차선·구역 반영은 16. 장소 의미·지도 관리가 맡는 접점이 될 것으로 보인다(oq-203).",
      "tag": "추정",
      "source_ids": [
        "ref-569"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LaneRequest.msg(오늘 원문 열람)는 string fleet_name, uint64[] open_lanes, uint64[] close_lanes 만 둔다. 40. 운영 절차·요청 창구 페이지 9절은 통제 구역 선언·해제의 요청자·승인·기한 기록을 ROP 몫으로 본다(추정).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f37",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ N. 보안·개인정보의 51. 인증·권한·격리 연결 근거: Open-RMF API 서버(rmf-server)는 OpenID Connect 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정한다. 관리자는 모든 그룹에서 모든 동작을 할 수 있고, 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "api-server README(오늘 원문 열람): 신원 공급자는 인증만 하고 권한은 rmf-server 가 판정한다(in-app). 토큰은 preferred_username 클레임을 가진 JWT 다. 사용자는 여러 역할을 가질 수 있고 관리자는 검사를 우회한다. 모든 자원은 기본 빈 그룹에 속한다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f38",
      "claim": "연계 대상: J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 40. 운영 절차·요청 창구 페이지는 로봇 교시·정비 작업 지침(산업안전보건기준에 관한 규칙 제222조)과 ANSI/A3 R15.08-3-2026 이 사용자에게 두는 운영 요구를 사업주·제조사 책임의 연계 대상으로 둔다. 이렇게 보면 ROP는 요청·권한·기록 층으로 그 이행을 받쳐 주는 쪽으로 보인다(oq-265).",
      "tag": "추정",
      "source_ids": [
        "ref-1157",
        "ref-1153"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "40. 운영 절차·요청 창구 페이지 9절 표는 로봇 자체 지능·제어 경계의 외부 연계 칸에 교시·정비 작업 지침(사업주·제조사 책임, 제222조 포함)을 둔다. ANSI/A3 R15.08-3-2026 은 원문 미열람이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육 연결 근거: 중국 고급 호텔 직원 19명 면담 연구(Fu·Zheng·Wong, 2022)에서는 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼다. 근무 중 로봇 교육, 동료 교육, 고장 처리·고객 안내 같은 추가 업무도 직원의 사용 저항으로 이어졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1150"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "40. 운영 절차·요청 창구 페이지 5절 상업 시설 사례 서술에 실린 내용이다. 운영 책임 조직과 교육의 연결은 oq-266·oq-278 로 미해결이다. (재인용: 2026-09-30-18)",
      "as_of": "2022",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성 연결 근거: 병원 자율 배송 로봇(TUG) 민족지 연구(Mutlu·Forlizzi, HRI 2008)에서 내과 병동은 업무 중단에 대한 낮은 허용도, 비용과 이익의 불일치, 통행이 많은 곳의 주행 중단 때문에 직원 저항을 보였다. 반면 산후 병동은 로봇을 업무 흐름에 통합했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1151"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "40. 운영 절차·요청 창구 페이지 5절 병원 사례(TUG)의 예외·성과 칸에 실린 내용이다. 60. 노동·수용성·접근성 조사(f8)도 같은 연구를 인용했다. (재인용: 2026-09-30-18)",
      "as_of": "2008-03",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ Q. 현장 유형별 적용의 63. 병원·의료 연결 근거: 한림대학교성심병원은 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다고 2024년 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1199",
        "ref-944"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "40. 운영 절차·요청 창구 페이지 5절 수행 자원 칸은 두 보도를 함께 인용한다. 두 보도 모두 병원 발표에서 나왔을 수 있어 독립 교차 확인으로 보지 않았다. (재인용: 2026-09-30-18)",
      "as_of": "2024-09-19",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ Q. 현장 유형별 적용의 64. 상업 시설 연결 근거: 미국 뉴욕 알로프트 호텔에서는 투숙객이 전화로 프런트에 요청하면 주문 물건과 객실 번호를 사람이 확인해 처리했다. 배송 로봇(Savioke Relay)은 객실 앞에 도착하면 객실 전화로 자동 알림을 보냈다(2017년 보도).",
      "tag": "사실",
      "source_ids": [
        "ref-1152"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "40. 운영 절차·요청 창구 페이지 5절 상업 시설 사례에 실린 내용이다. 요청 접수는 자동화되지 않았고 프런트 직원이 맡았다. (재인용: 2026-09-30-18)",
      "as_of": "2017-04-18",
      "site_type": "상업 시설",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "연계 대상: J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ F. 연동의 22. 설비·건물 시스템 연동 연결 근거: 미국 MultiCare 계열 두 병원의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기 버튼을 스스로 누르지 못해 사람이 계속 따라다녀야 했다고 2026-06 보도되었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1154"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "40. 운영 절차·요청 창구 페이지 5절에 따르면 Proof News(2026-06)는 Good Samaritan·Tacoma General 병원 사례를 보도했다. 같은 페이지는 승강기 연동을 이 영역이 아닌 외부 설비 연계 대상으로 둔다. (재인용: 2026-09-30-18)",
      "as_of": "2026-06-09",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-1093",
      "org": "Open Robotics (open-rmf/rmf_visualization)",
      "title": "rmf_visualization — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_visualization",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "층 평면도 위에 로봇·문·승강기·주행 그래프·예측 궤적을 표시하는 Open-RMF 시각화 패키지 README.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1094",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — task_log.json (Task Event Log)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "작업·단계·사건 3계층 로그 구조를 정의한 작업 이벤트 로그 스키마. 이번 실행에서 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_log.json",
      "source_unopened": false
    },
    {
      "id": "ref-1096",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "시각 색인을 둔 로봇 기록 컨테이너 형식 명세.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "작업 상태 값 12개, 시작·종료 시각, 단계, 중단·취소·강제 종료 기록을 담는 Open-RMF 작업 상태 스키마. 이번 실행에서 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "관제–이동로봇 통신 명세(main 3.0.0). visualization·state 토픽 분리 등.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "rmf-server 의 OIDC 인증, 앱 내 역할·동작·그룹 기반 권한 판정, 기본 메모리 내 SQLite 와 지원 데이터베이스를 설명한다. 이번 실행에서 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf-web/main/packages/api-server/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 웹 대시보드·API 서버 저장소 README(기본 비영속 저장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1099",
      "org": "Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8))",
      "title": "Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction",
      "published": "2017-07-27",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "다중 로봇 인터페이스의 몰입·예측이 운영자 상황 인식에 주는 영향을 실험한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1098",
      "org": "Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022)",
      "title": "Conflict-Based Search for Explainable Multi-Agent Path Finding",
      "published": "2022-02",
      "url": "https://arxiv.org/abs/2202.09930",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람이 확인할 수 있게 나눠 보여 주는 설명 가능한 다중 에이전트 경로 계획 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1103",
      "org": "아주경제",
      "title": "현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다",
      "published": "2025-04-07",
      "url": "https://www.ajunews.com/view/20250407084333272",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "현대차·기아와 한림대학교의료원의 배송 로봇·관제·수령 인증·특수 물품 배송 이력 관리 공동 개발 협약 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-148",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "로봇 상태 값 7개, 배터리, 현재 작업 id, 문제 목록, 위치, 기록 시각을 담는 로봇 상태 스키마. 이번 실행에서 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_state.json",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 상태 메시지 JSON 스키마(오류 수준 등).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-313",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "문 모드 다섯 값(closed·moving·open·offline·unknown) 정의.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-449",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/connection.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 연결 상태(ONLINE·OFFLINE·CONNECTION_BROKEN) 스키마.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마(운용 상태 waitingExternalEvent 등).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-283",
      "org": "Open Robotics",
      "title": "Doors (integration_doors) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_doors.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 문 연동과 문 어댑터의 상태 감독자 역할 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-448",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_task_msgs/msg/Alert.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "심각도 등급(info·warning·error), 응답 목록, 관련 작업 id 를 담는 경보 메시지 정의. 이번 실행에서 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_task_msgs/msg/Alert.msg",
      "source_unopened": false
    },
    {
      "id": "ref-494",
      "org": "Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU)",
      "title": "Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.25690",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 위치 스푸핑 공격 모델과 신뢰 인지 모니터로 적대 에이전트를 계획에서 빼는 다중 로봇 롤아웃 계획 프리프린트.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-447",
      "org": "OpenTelemetry (CNCF)",
      "title": "OpenTelemetry Specification — Overview",
      "published": null,
      "url": "https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "분산 서비스의 추적·지표·로그 신호와 컨텍스트 전파를 정의하는 명세 개요.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-453",
      "org": "Liu, Z., Bahety, A., & Song, S.",
      "title": "REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction",
      "published": "2023",
      "url": "https://arxiv.org/abs/2306.15724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 경험 요약과 대규모 언어 모델로 실패를 설명하고 수정하는 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1236",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Cyber Resilience Act - Reporting obligations",
      "published": "2026-09-11",
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "EU 사이버복원력법의 취약점·중대 사고 보고 의무(24시간 조기 경보, 72시간 통지, 최종 보고) 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-150",
      "org": "CIO Korea",
      "title": "오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표",
      "published": null,
      "url": "https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 오토스토어가 발표한 국내 도입 기업 경제성 연구 보도(벤더 주장).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-139",
      "org": "ISO",
      "title": "ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions",
      "published": "2014",
      "url": "https://www.iso.org/standard/54497.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 제조 운영 관리 핵심성과지표의 정의와 설명.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-140",
      "org": "ASCM",
      "title": "SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment",
      "published": null,
      "url": "https://scor.ascm.org/performance/reliability/RL.1.1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. SCOR 완전 주문 이행률 지표 정의.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-146",
      "org": "Omega 게재 논문(저자 미확인)",
      "title": "The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 에서 동적 우선순위 규칙의 에너지·처리량 효과를 모델·시뮬레이션으로 평가.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-102",
      "org": "Springer(FAIM 2025 발표 논문, 저자 미확인)",
      "title": "Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics",
      "published": "2025",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 물류센터 AMR 플릿·충전기 규모를 시뮬레이션으로 산정한 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1278",
      "org": "Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics)",
      "title": "Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety",
      "published": "2026",
      "url": "https://doi.org/10.1007/s12369-026-01359-1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "창고 작업자 12명 면담으로 로봇 운영의 데이터 감시 우려와 작업자 중심 요구(수동 무시·개인정보 통제·감시 알림)를 확인한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1272",
      "org": "대한민국 국회 (법률 제16320호, 케이스노트 게재)",
      "title": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항)",
      "published": "2019-04-16",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "노사협의회 협의 사항(신기계·기술 도입, 근로자 감시 설비 설치 등)을 정한 조항.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-096",
      "org": "Lamballais, T., Roy, D., & de Koster, M. B. M.",
      "title": "Estimating performance in a Robotic Mobile Fulfillment System",
      "published": "2017",
      "url": "https://repub.eur.nl/pub/107376/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 대기행렬 모델로 작업대 위치 등이 처리량에 미치는 영향을 추정.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-145",
      "org": "Ghelichi, Z., & Kilaru, S.",
      "title": "Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers",
      "published": "2021",
      "url": "https://www.sciencedirect.com/science/article/pii/S0307904X20305801",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 협업형 AMR 피킹의 해석적 성과 모델.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 작업 요청 스키마(가장 이른 시작 시각·우선순위·플릿 지정).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-569",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "플릿 이름과 열고 닫을 차선 목록만 담는 차선 요청 메시지. 이번 실행에서 원문을 다시 열었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "source_unopened": false
    },
    {
      "id": "ref-1153",
      "org": "ANSI (The ANSI Blog)",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": null,
      "url": "https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 이동로봇 적용(사용자 측 요구) 표준 소개 글.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1157",
      "org": "고용노동부 (국가법령정보센터)",
      "title": "산업안전보건기준에 관한 규칙 제222조(교시 등)",
      "published": "2025-09-01",
      "url": "https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "산업용 로봇 교시 등 작업 시 작업 지침 등을 정한 조항.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1150",
      "org": "Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management)",
      "title": "The perils of hotel technology: The robot usage resistance model",
      "published": "2022",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "호텔 직원 면담으로 로봇 사용 저항 요인(역할 모호성·추가 업무 등)을 정리한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1151",
      "org": "Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008-03",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "병원 자율 배송 로봇(TUG) 민족지 연구. 병동별 수용 차이를 업무 흐름·사회·환경 요인으로 설명.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원'",
      "published": "2024-04-15",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "한림대학교성심병원 커맨드센터의 서비스 로봇 통합 관제·요청 경로 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1199",
      "org": "ZDNet Korea",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "한림대학교성심병원 커맨드센터의 7종 73대 로봇 운영과 누적 사용 건수 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1152",
      "org": "한국일보",
      "title": "“딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인)",
      "published": "2017-04-18",
      "url": "https://www.hankookilbo.com/news/article/201704180418820469",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "뉴욕 알로프트 호텔의 프런트 경유 요청과 배송 로봇(Savioke Relay) 운영 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1154",
      "org": "Proof News (Varsha Bansal)",
      "title": "Meet the Robot That Nurses Unplugged",
      "published": "2026-06-09",
      "url": "https://www.proofnews.org/moxi/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "MultiCare 계열 병원의 Moxi 로봇 운영 문제(길 잃음, 승강기 버튼 조작 불가, 사람 동행)를 다룬 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1359",
      "org": "ISA (ANSI Webstore 게재)",
      "title": "ANSI/ISA 18.2-2016 Management of Alarm Systems for the Process Industries",
      "published": "2016",
      "url": "https://webstore.ansi.org/standards/isa/ansiisa182016",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "공정 산업 시설에서 운영자에게 표시되는 경보 시스템의 수명주기 관리 원칙·절차를 정한 표준의 판매 소개 페이지. 본문은 유료라 소개 문구만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://webstore.ansi.org/standards/isa/ansiisa182016",
      "source_unopened": false
    },
    {
      "id": "ref-1360",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사고·아차 사고 조사를 위해 소셜 로봇의 센서·구동기·제어 결정을 안전하게 기록하는 윤리적 블랙박스의 초안 공개 표준. 초록만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2205.06564",
      "source_unopened": false
    },
    {
      "id": "ref-1361",
      "org": "Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L 7(3), arXiv)",
      "title": "ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2",
      "published": "2022-07",
      "url": "https://arxiv.org/abs/2201.00393",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "LTTng 기반 ROS 2 실행 정보 추적 도구와 계측. 저자 실험에서 평균 종단 지연 증가는 0.0033 ms 였다. 초록만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2201.00393",
      "source_unopened": false
    },
    {
      "id": "ref-1362",
      "org": "TechTarget (Hannah Nelson, Xtelligent Healthcare Media)",
      "title": "Hospital Looks to 'Cobot' EHR Integration to Alleviate Nurse Burnout",
      "published": "2022-08-11",
      "url": "https://techtarget.com/searchhealthit/feature/Hospital-Looks-to-Cobot-EHR-Integration-to-Alleviate-Nurse-Burnout",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "ChristianaCare 가 키오스크로 호출하던 Moxi 로봇을 Cerner 전자의무기록과 연동해 주문으로 출동시키려는 계획을 다룬 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://techtarget.com/searchhealthit/feature/Hospital-Looks-to-Cobot-EHR-Integration-to-Alleviate-Nurse-Burnout",
      "source_unopened": false
    },
    {
      "id": "ref-1363",
      "org": "Mehrotra, S., Sycara, K., Lewis, M., Chien, S.-Y., & Wang, H. (Proceedings of the Human Factors and Ergonomics Society)",
      "title": "Effects of alarms on control of robot teams",
      "published": "2011",
      "url": "https://d-scholarship.pitt.edu/12400/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "다중 로봇 수색·구조 과제에서 경보 없음·자유 표시·최상위 경보만 표시 조건을 비교한 실험. 저장소의 초록을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://d-scholarship.pitt.edu/12400/",
      "source_unopened": false
    },
    {
      "id": "ref-1364",
      "org": "데일리팜 (김지은)",
      "title": "마약통합시스템 시행 2개월…병원·약국 다빈도 질문은",
      "published": "2018-07-13",
      "url": "https://dailypharm.com/user/news/85066",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "2018-05-18 시행된 마약류통합관리시스템 전산 보고와 종전 마약류 관리대장 2년 보관, 과태료 유예를 다룬 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://dailypharm.com/user/news/85066",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/field-operations-and-monitoring/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "'다른 대분류와의 연결' 절만 채운다(category_link, patches). 대분류별 근거는 다음과 같다. A. 기획·사업: f25 / B. 로봇 온톨로지: 근거 없음, '아직 다루지 않은 연결'로 명시 / C. 채팅 기반 구성·운영: f3·f4 / D. 공간·지도 모델: f1·f36 / E. 사물·사람·실시간 상태: f9·f13·f26 / F. 연동: f5·f14·f15·f27·f34·f43 / G. 계획·최적화: f8·f20·f28·f35 / H. 실행·협업·예외 복구: f7·f16·f17·f18·f19 / I. 설계·시뮬레이션: f2·f29 / K. 플랫폼 아키텍처·인프라: f6·f21·f22 / L. AI·학습 기술: f23 / M. 안전: f10·f38 / N. 보안·개인정보: f24·f30·f37 / O. 검증·도입·수명주기: f39 / P. 거버넌스·법규·사회: f11·f31·f40 / Q. 현장 유형별 적용: f12·f32·f33·f41·f42. 이 중 f20·f23·f24·f31·f38 은 추정·low 이므로 단정하지 말고 쓰고, f11·f38·f43 은 '연계 대상'으로 짧게 다룬다. 18. 실시간 세계 상태·데이터 일관성(f13·f26, 현재 상태)과 34·35 쪽 시뮬레이션·설계(f2·f29, 가정한 미래)는 구분해 쓴다. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 10절에 f18·f19·f21·f22 반영, 37. 관제 화면·실행 기록 11절 oq-252 에 f10, oq-239 에 f11 근거 추가."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "경보 관리",
      "term_en": "Alarm Management (ANSI/ISA 18.2)",
      "definition": "운영자에게 표시되는 경보를 정의·설계·운영·유지·변경하는 수명주기 전체를 관리하는 일로, 공정 산업에서는 ANSI/ISA 18.2-2016 이 일반 원칙과 절차를 정한다."
    },
    {
      "term_ko": "런타임 추적",
      "term_en": "Runtime Tracing (ros2_tracing)",
      "definition": "실행 중인 소프트웨어 내부의 콜백·메시지 전달 같은 실행 정보를 저부하 추적기로 기록하는 방법으로, ROS 2 에서는 LTTng 기반 ros2_tracing 이 이를 제공한다."
    }
  ],
  "open_questions_new": [
    "다중 로봇 플릿 관제에서 경보 우선순위, 경보 홍수 기준, 경보 합리화 절차를 ANSI/ISA 18.2 처럼 정한 로봇 운영용 경보 관리 표준이나 공개 지침이 있는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 31. 사람–로봇 협업 | 근거: f19 | 종류: 일반",
    "전자의무기록 주문이 로봇 작업 요청을 자동으로 만드는 병원 연동에서 주문 취소·변경을 진행 중인 로봇 작업에 반영하고 결과를 기록에 되돌린 공개 사례가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 23. 업무 시스템 연동, 63. 병원·의료 | 근거: f34 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 46,
    "cross_checked_count": 0,
    "unverified": [
      "f11 마약류 관리대장 2년 보관·전산 보고는 2018년 업계 기사 기준이다. 법령 원문과 현행 여부는 미확인이다. 로봇 배송 이력이 보고 대상에 드는지도 미확인이다(oq-239 미해결)",
      "f19 ANSI/ISA 18.2-2016 본문은 유료라 미열람이다. 경보 홍수 기준(10분 10건 등)은 벤더 자료 요약에만 있어 넣지 않았다",
      "f22 ros2_tracing 의 0.0033 ms 는 저자 실험값이며 독립 재현은 미확인이다",
      "f34 ChristianaCare 의 EHR 연동은 2022 계획 보도이며 실행 여부는 미확인이다",
      "f41 한림대학교성심병원 수치는 병원 발표에서 나온 보도 두 건이라 독립 교차 확인으로 보지 않았다",
      "NCS(국가직무능력표준)의 로봇 운용·관제 능력단위는 검색에서 확인하지 못했다(oq-278 미해결)",
      "이종 플릿 예지 정비 공개 연구는 벤더 자료뿐이라 넣지 않았다(oq-221 미해결)"
    ],
    "scope_violations": [
      "f11: 마약류 보고·보관 의무는 업종별 조건(의료)과 병원 업무 시스템의 몫이다. '연계 대상:'으로 표시했다",
      "f38: 교시·정비 작업 지침과 사용자 측 안전 요구 이행은 사업주·제조사 몫이다. '연계 대상:'으로 표시했다",
      "f43: 승강기 조작은 시설·설비 제어 경계의 연계 대상이다. '연계 대상:'으로 표시했다",
      "f15: 문 개폐 제어 자체는 연계 대상이며 ROP 몫은 문 상태 확인으로 한정했다",
      "f24: 사이버복원력법 보고 의무는 제조자의 법적 의무이며, 플랫폼이 제조자에 해당하는지는 판단하지 않았다",
      "f19: ISA 18.2 는 공정 산업 표준이므로 로봇 플릿 적용을 단정하지 않았다"
    ],
    "budget_used": {
      "queries": 9,
      "sources": 6
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 9회/30, 신규 출처 6건/15(ref-1359~ref-1364, 예약 구간 안), 재사용 출처 40건. 재사용 출처 가운데 Open-RMF 공식 저장소 원문 6건(ref-111, ref-148, ref-448, ref-569, ref-762, ref-1094)은 raw.githubusercontent.com 으로 다시 열어 확인했다. 나머지 재사용 출처는 게시된 세부영역 페이지(37·38·39·40)와 이전 브리프(2026-09-30-23, 2026-09-30-24), 다른 대분류 페이지(G. 계획·최적화)의 검증된 주장을 재인용했으며 다시 열지 않았다. 참고문헌 목록 원문 열람이 '아니오'인 출처에 기댄 finding 에는 source_unopened 를 표시했다. 신규 출처 6건은 모두 열었으나 ISA 18.2 는 판매 소개 페이지, arXiv 2건과 HFES 1건은 초록만 읽었다. 교차 확인은 0건이다(대부분 단일 출처, 한림대 보도 2건은 독립이 아님). 벤더 기능·성능 주장은 finding 으로 내지 않았다(오토스토어 수치는 f25 에서 제외). B. 로봇 온톨로지와 J. 현장 운영·관제를 잇는 근거는 게시 페이지에서 찾지 못해 finding 이 없으며, 스토리텔러는 '아직 다루지 않은 연결'로 적어야 한다. 현장 유형 근거는 물류창고·제조 공장·병원·상업 시설이고 가정·실외·기타는 없다. L. AI·학습 기술 연결(f23)은 분류 원문 교차 규칙(장애 분석은 38번)에 기댄다. 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34·35(가정한 미래 실험·설계)를 섞지 않았다. 열린 질문 oq-131·oq-203·oq-210·oq-239·oq-252·oq-265 는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)로 '5'를 매겼다 [가정]. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-05/verification.json

```json
{
  "run_id": "2026-10-09-05",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 raw README(open-rmf/rmf_visualization main)를 열어 확인했다. 층별 평면도·플릿 보고 로봇 위치·문·승강기·주행 그래프·예측 스케줄 시각화기를 둔다. 브리프는 fetched false로 적었으므로 페이지 각주에는 원문 미열람 표시를 유지한다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. task_log.json(ref-1094)은 원문을 열었고, MCAP(ref-1096)은 미열람 재인용이다. 변환 형식이 없다는 점은 oq-131로 둔다. 36. 가상 시운전·실제 상황 재현과 이어지는 연결이므로 가정·재현 쪽 서술로 쓰고 18. 실시간 세계 상태·데이터 일관성과 섞지 않는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 게시 페이지 두 곳의 서술을 이은 해석이므로 단정하지 않는다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. 입력 원문(task_state.json)과 대조한 결과 status 열거값 12개와 시작·종료 시각, phases, interruptions·cancellation·killed 필드를 확인했다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문 ref-031(VDA5050_EN.md 3.0.0) 목차에 6.7 Visualization과 7.9 visualization message가 state message와 따로 있음을 확인했다. fetch_url은 null이지만 data/source_texts 원문이 있으므로 fetched true를 인정한다. 발행일은 미확인이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 api-server README(ref-762)를 열어 확인했다. 기본은 메모리 내 SQLite이고, 지원 DB는 PostgreSQL·SQLite·MySQL·MariaDB이며, db_url로 설정한다. ref-302는 미열람이고 같은 프로젝트라 독립 출처가 아니다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "게시된 37. 관제 화면·실행 기록 페이지의 기존 검증(2026-09-30)을 재인용했다. 이번 검증에서는 원문을 다시 열지 않았다(검증 예산). 실험실 조건이라는 단서를 유지한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "게시 페이지를 재인용했고 이번 검증에서는 미열람이다. 용어는 용어집의 '설명 가능한 다중 에이전트 경로 찾기'와 일치한다. 알고리즘 수준 연구라는 단서를 유지한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 협약·개발 계획 단계의 기사 1건에 기대고 원문은 미열람이다. 현장 유형은 병원, 항목은 완료·인계이다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 arXiv 초록을 열어 확인했다. 2022-05-13 제출이고, 소셜 로봇의 센서·구동기·제어 결정 기록, 사고·아차 사고 조사 지원, 부속서(annex)의 초안 표준을 담는다. '플릿·플랫폼 수준 기록은 다루지 않는다'는 초록 범위의 판단이므로 '초록에는 플릿 수준 기록 언급이 없다'로 좁혀 쓴다(수정 지시 참조)."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 데일리팜 2018-07-13 기사(김지은)를 열어 확인했다. 원문은 '2018년 5월 18일 마약류를 입고한 내역부터' 전산보고하고, '종전 마약류 관리대장은 2년간 보관'한다고 적는다. 기사 1건이고 8년 전 기준이며 현행 법령 여부는 미확인이다. '보도되었다'는 형태로만 [사실]을 유지하고, 연계 대상으로 짧게 다룬다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "게시된 37. 관제 화면·실행 기록 페이지 5절의 서술과 일치한다. ref-1103은 이번에 미열람이다. 현장 유형은 병원이다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. 입력 원문 robot_state.json에서 status·issues·unix_millis_time을 확인했다. 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽 연결로 쓴다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. 입력 원문에서 connection.schema의 CONNECTION_BROKEN, MassRobotics의 waitingExternalEvent, task_state의 delayed·blocked를 확인했다. 공통 매핑 부재는 oq-033과 oq-073으로 둔다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문 DoorMode.msg에서 다섯 값을, integration_doors에서 문 어댑터가 상태 감독자 역할을 한다는 점을 확인했다. 문 개폐 제어 자체는 연계 대상으로 둔다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "스키마 내용(12개 상태 값, interruptions·cancellation·killed, 시작·종료 시각)은 원문으로 확인했다. 끝 절 '실행 결과 확인과 이상 탐지가 같은 기록을 쓴다'는 해석이므로 [추정] 문장으로 분리한다(수정 지시)."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "Alert.msg 원문으로 tier(0·1·2), responses_available, task_id를 확인했다. '운영자 선택이 이 메시지로 복구 조치에 넘어간다'는 해석이므로 [추정] 문장으로 분리한다(수정 지시)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 Pitt D-Scholarship 초록을 열어 확인했다. 비교한 조건은 경보 없음, 자유 표시, 최상위 경보만 보이는 의사결정 보조의 세 가지다. 자유 표시 조건이 고장과 피해자를 더 빨리 탐지했고, 탐색 면적과 피해자 수에는 차이가 없었다. 다만 초록은 속도 비교의 기준 조건을 명시하지 않는다. 그래서 claim의 '최상위 경보 하나만 보여 준 조건보다'라는 특정은 원문 범위를 넘으므로 비교 기준을 빼고 재서술한다(수정 지시). 실험실 시뮬레이션 조건이다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 ANSI 웹스토어를 열어 확인했다. 공정 산업 경보 시스템의 수명주기 관리 원칙·절차를 다루고, 2009판을 개정했으며, BPCS·경보판·화재·가스 패키지·SIS 경보를 포함한다. 검색 결과로는 2016판이 최신이고 후속 개정은 계획만 확인된다(2026-10-09). 공정 산업 표준이므로 로봇 플릿에 적용한다고 단정하지 않는다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). G. 계획·최적화 페이지 연결 절의 같은 주장을 재인용했고 원문은 미열람이다. 같은 각주 ref-494를 재사용하고, 물류센터 적용이 미확인이라는 단서를 유지한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). OpenTelemetry 개요(ref-447)는 원문으로, ros2_tracing은 초록으로 확인했다. 두 계층을 잇는 공개 사례는 미확인이며 oq-210으로 둔다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 arXiv 초록을 열어 확인했다. v4 2022-07-30, IEEE RA-L 7(3) 6511-6518이며, LTTng 기반이고 모든 계측을 켰을 때 평균 0.0033 ms다. 저자 실험값이고 독립 재현은 미확인이라는 단서를 유지한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 교차 규칙은 분류 원문으로 확인했다. REFLECT 원문은 미열람이다. 공통 규칙 5에 따라 47. AI·학습·적응과 모델 운영과 38. 모니터링·이상 탐지·원인 분석 양쪽에 연결한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 59. 법·규제·보험·라이선스 조사를 재인용했고 원문은 미열람이다. 보고 의무 적용일 2026-09-11은 CRA 경과 규정과 맞는다. 플랫폼이 제조자에 해당하는지는 미확인으로 둔다. 용어는 용어집 '사이버복원력법'과 일치한다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 39. 운영 성과 측정·개선 페이지 9절의 판단을 재인용했다. ref-150(오토스토어, 벤더 주장)과 ref-139는 미열람인데 finding의 source_unopened가 false로 적혀 있어 표시가 어긋난다. 벤더 수치는 쓰지 않는다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "robot_state.json 원문으로 7개 상태 값, battery 0~1, task_id·issues·unix_millis_time을 확인했다. 'KPI 원천이 된다'는 A. 기획·사업 페이지에서도 [추정]으로 실린 해석이므로 [추정] 문장으로 분리한다(수정 지시). A 페이지와 같은 각주 ref-148을 재사용한다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. 39. 운영 성과 측정·개선 페이지 5절과 일치한다. ref-140은 미열람이다. 현장 유형은 물류창고이며 oq-015와 연결한다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "A. 기획·사업 페이지와 G. 계획·최적화 페이지에 같은 값과 단서로 실린 [사실]을 재인용했다. 원문은 미열람이다. 모델·시뮬레이션 조건의 저자 보고값이고 현장 실측이 아니라는 단서를 반드시 유지한다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "39. 운영 성과 측정·개선 페이지와 I. 설계·시뮬레이션 연결 브리프(2026-10-09-04 f14)에 같은 주장이 있다. 원문은 미열람이다. 시뮬레이션 결과라는 단서와 35. 처리능력·규모·배치 설계(설계·가정 실험) 쪽 서술을 유지한다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "60. 노동·수용성·접근성 조사를 재인용했고 근거는 초록이며 이번 검증에서 미열람이다. 현장 유형은 물류창고다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 근로자참여법 제20조 제1항 제9호·제14호는 재인용이다. 법적 해당 여부는 미확인으로 두고 단정하지 않는다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "39. 운영 성과 측정·개선 페이지 5절의 [사실]을 재인용했고 원문은 미열람이다. as_of가 2021 하나로 묶여 있으므로 각 연구 연도(2017, 2021)를 따로 밝힌다. 모델 연구라는 단서를 유지한다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "개정 1(2017)과 ISO/DIS 미발행 진술의 근거는 ref-782와 ref-781인데 source_ids에는 ref-139만 있다(수정 지시). 검증 검색 결과 ISO 페이지는 여전히 FDIS 등록 승인 단계(40.99)로 표시되며, 2026-10-09 기준 새 판 발행은 미확인이다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 TechTarget 2022-08-11(Hannah Nelson) 기사를 열어 확인했다. 현재는 키오스크로 호출하고, ANF 보조금으로 코봇 3대를 추가하며(총 5대), Cerner EHR 연동 뒤 주문이 들어오면 로봇이 물품을 가지러 가는 계획이다. 계획 보도이며 운영 결과는 미확인이다. 직접 인용은 이 출처에서 1회만 쓴다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. 입력 원문 task_request.json에서 unix_millis_earliest_start_time과 priority는 있고 마감 필드는 없음을 확인했다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다. LaneRequest.msg 원문에서 필드 세 개(fleet_name, open_lanes, close_lanes)를 확인했다. oq-203과 연결한다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증에서 raw README를 다시 열어 확인했다. OIDC는 인증만 하고 권한은 in-app으로 판정하며, preferred_username 클레임을 쓰고, 관리자는 모든 그룹·동작이 가능하다. TODO 절에 '모든 자원은 빈 문자열 기본 그룹'이라는 문구가 있다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]을 유지한다(low). 40. 운영 절차·요청 창구 페이지 9절과 일치한다. 연계 대상 표시가 적절하다. ANSI/A3 R15.08-3-2026은 미열람이다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "40. 운영 절차·요청 창구 페이지 5절의 [사실]을 재인용했고 이번 검증에서 미열람이다. 현장 유형은 상업 시설이며 oq-266·oq-278과 연결한다."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "40. 운영 절차·요청 창구 페이지 5절과 60. 노동·수용성·접근성 조사가 같은 연구를 인용했다. 원문은 미열람이다. 현장 유형은 병원이다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "보도 2건이 병원 발표에서 나왔을 수 있어 독립 교차 확인이 아니다. 2024년 보도 기준이라는 단서를 유지한다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "2017년 기사 1건을 재인용했다. 현장 유형은 상업 시설이다. 요청 접수를 사람이 맡았다는 점을 유지한다."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "40. 운영 절차·요청 창구 페이지 5절을 재인용했다. 승강기 조작은 시설·설비 제어 경계의 연계 대상이므로 짧게 다룬다."
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
      "f26(39. 운영 성과 측정·개선 ↔ 18. 실시간 세계 상태·데이터 일관성)·f28(39 ↔ 28. 공용 자원·충전·에너지 최적화)은 A. 기획·사업 페이지 '다른 대분류와의 연결' 절에 같은 각주(ref-148, ref-146)로 이미 있다. 각주 id를 재사용하고 표현을 맞춘다",
      "f20(38. 모니터링·이상 탐지·원인 분석 ↔ 25. 작업 배정 — MRTA)은 G. 계획·최적화 페이지 연결 절에 같은 각주 ref-494로 있다",
      "f29는 I. 설계·시뮬레이션 대분류 연결 브리프(2026-10-09-04 f14)와 같은 출처 ref-102를 쓴다. f2는 같은 브리프 f28과 같은 결론(oq-131 미해결)이며 서로 모순되지 않는다",
      "f13·f26은 E. 사물·사람·실시간 상태 대분류 연결 브리프(2026-10-09-03 f32)와 같은 방향의 연결이다. 모순은 없다"
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
    "patches 대상 절: 대분류 페이지 H2는 번호 없는 '다른 대분류와의 연결'이다. 브리프 page_proposals의 '5. 다른 대분류와의 연결'이 아니라 페이지 문자열과 같은 절 이름으로 patch를 보내고(action replace), 기존 '아직 작성되지 않음(에이전트가 채운다).' 문장을 교체한다. 다른 절과 auto 마커는 고치지 않는다 — 부록 C 대분류 절 제목 정본에 번호가 없다.",
    "각주 정의: 이 절에서 쓴 각주는 '[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일 2026-10-09' 형식으로 정의한다. 페이지에 '참고 자료' 절이 없으므로 이번 patch 안(절 끝)에 둔다. 각주 정의가 없으면 형식 검증이 실패한다.",
    "원문 미열람 표시: 브리프에서 fetched false인 출처 ref-1093, ref-1096, ref-302, ref-1099, ref-1098, ref-1103, ref-494, ref-453, ref-1236, ref-150, ref-139, ref-140, ref-146, ref-102, ref-1278, ref-1272, ref-096, ref-145, ref-1153, ref-1157, ref-1150, ref-1151, ref-944, ref-1199, ref-1152, ref-1154(그리고 아래에서 추가하는 ref-781·ref-782)는 각주 접근일 뒤에 ' (원문 미열람)'을 붙인다. reference_updates에서도 source_unopened: true로 둔다.",
    "f16: 'Open-RMF 작업 상태 스키마는 12개 상태 값과 중단·취소·강제 종료 기록을 담는다'는 [사실][^ref-111]로 쓴다. '실행 결과 확인과 이상 탐지가 같은 기록을 쓴다'는 별도 문장으로 [추정][^ref-111]을 붙인다 — 스키마가 말하지 않는 해석이다.",
    "f17: Alert 메시지의 필드(심각도 등급 info·warning·error, 응답 목록, 관련 작업 id)는 [사실][^ref-448]로 쓴다. '운영자 선택이 이 메시지로 복구 조치에 넘어간다'는 별도 문장으로 [추정]을 붙인다 — 메시지 정의 밖의 해석이다.",
    "f26: 로봇 상태 스키마의 필드는 [사실][^ref-148]로 쓴다. '가동률·충전·오류 시간 지표의 원천이 된다'는 [추정][^ref-148]으로 분리한다 — A. 기획·사업 페이지에서도 이 해석은 [추정]이다.",
    "f18: '최상위 경보 하나만 보여 준 조건보다'를 빼고 원문 범위로 다시 쓴다. 비교한 세 조건(경보 없음·자유 표시·최상위 경보만 보이는 의사결정 보조)을 밝히고, 자유 표시 조건의 운영자가 고장과 피해자를 더 빨리 탐지했으며 탐색 면적·발견 피해자 수에는 차이가 없었다고 [사실]로 쓴다. 실험실 시뮬레이션 조건이라는 단서를 붙인다 — 초록은 속도 비교의 기준 조건을 명시하지 않는다.",
    "f10: '플릿·플랫폼 수준 기록은 다루지 않는다'를 '초록에는 플릿·플랫폼 수준 기록에 대한 언급이 없다'로 좁힌다. 초안 표준이 논문 부속서(annex)로 실렸고 토론용 초안이라는 점을 밝힌다 — 부속서 본문은 열람하지 않았다. 용어는 용어집의 '윤리적 블랙박스'로 링크한다.",
    "f11: '연계 대상'으로 한두 문장만 쓴다. '2018-05-18 입고 내역부터 전산 보고, 종전 관리대장 2년 보관'으로 출처 표현에 맞추고, 기준일(2018-07-13 보도)과 '법령 원문·현행 여부 미확인'을 병기한다. 로봇 배송 이력이 대상인지는 oq-239로 남긴다.",
    "f33: ISO 22400-2:2014/Amd 1:2017과 ISO/DIS 22400-2 미발행 진술에는 기존 각주 ref-782와 ref-781을 재사용해 붙인다. 기준일은 '2026-09-26 확인'으로 둔다 — 브리프 source_ids의 ref-139만으로는 이 두 진술을 뒷받침할 수 없다.",
    "f25: ref-150의 오토스토어 경제성 수치는 본문에 쓰지 않는다. ref-150을 각주로 남기면 그 문장은 [추정]이어야 하고 '벤더 주장'을 병기한다.",
    "f32: 두 연구의 발행 연도(Lamballais 외 2017, Ghelichi·Kilaru 2021)를 각각 밝히고, 모델 연구이며 현장 실측이 아니라는 단서를 붙인다.",
    "f28·f22·f29·f41: 단서를 문장 안에 유지한다. f28은 '모델·시뮬레이션 조건의 저자 보고값', f22는 '저자 실험값·독립 재현 미확인', f29는 '시뮬레이션 결과', f41은 '2024년 보도 기준, 병원 발표 출처일 수 있어 독립 확인 아님'이다.",
    "추정·low finding(f3, f9, f20, f23, f24, f25, f31, f38)은 '것으로 보인다'·'가능성이 있다' 형태로만 쓰고 단정하지 않는다. f24에는 '플랫폼의 제조자 해당 여부 미확인', f31에는 '법적 해당 여부 미확인'을 병기한다.",
    "범위 경계: f11·f38·f43은 문장 첫머리를 '연계 대상:'으로 하고 짧게 다룬다. f15에서는 문 개폐 제어를, f43에서는 승강기 조작을 연계 대상으로 밝히고, ROP 몫은 상태 확인·요청으로 한정한다. f19는 ANSI/ISA 18.2-2016이 공정 산업 표준이며 로봇 플릿용 경보 관리 표준은 찾지 못했다고 쓴다(새 열린 질문과 연결).",
    "18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분: f13·f26은 현재 상태를 표현하는 18 쪽 연결로, f2(36. 가상 시운전·실제 상황 재현)와 f29(35. 처리능력·규모·배치 설계)는 가정한 미래·재현 쪽 연결로 따로 쓴다.",
    "L. AI·학습 기술: f23은 47. AI·학습·적응과 모델 운영 페이지와 38. 모니터링·이상 탐지·원인 분석 페이지 양쪽으로 링크한다. 교차 규칙 원문을 인용하려면 분류 원문 문장을 한 글자도 바꾸지 않고 [분류원문]을 붙이고, 그렇지 않으면 태그 없는 서술로 쓴다.",
    "'아직 다루지 않은 연결' 소절을 둔다: B. 로봇 온톨로지 전체(게시 페이지에 근거 없음)를 명시하고, 이번 근거가 없는 세부영역(예: 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터)을 번호와 이름으로 적는다. Q. 현장 유형별 적용 연결에서는 근거가 물류창고·제조 공장·병원·상업 시설뿐이고 가정·실외·기타 근거는 없다고 밝힌다.",
    "중복 각주 재사용: f26·f28은 A. 기획·사업 페이지, f20은 G. 계획·최적화 페이지와 같은 출처 id(ref-148, ref-146, ref-494)와 같은 단서 표현을 쓴다. 상대 대분류 페이지에 같은 연결이 실려 있으면 그 절로 링크해도 된다.",
    "표기: 대분류는 문자와 이름('F. 연동'), 세부영역은 번호와 이름('38. 모니터링·이상 탐지·원인 분석')을 함께 쓰고 Mermaid 노드 표시 이름도 같게 한다. 링크는 docs/categories/field-operations-and-monitoring/index.md 위치 기준 상대 경로(.md 포함)로 쓴다.",
    "f34·f11·f19의 직접 인용은 출처당 1회, 짧은 구절로만 쓴다. 나머지는 재서술한다.",
    "새 열린 질문 2건(경보 관리 표준 — 근거 f19, EHR 주문 연동 취소·변경 — 근거 f34)은 형식이 맞으므로 등록한다. 용어 후보 '경보 관리'와 '런타임 추적'은 등록하되, '런타임 추적' 정의에는 기존 용어 '분산 추적'과 다른 계층(ROS 2 런타임 내부)임을 밝힌다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 43건, 미확인 0건, 교차 확인 0건. 이번 검증에서 원문을 연 것은 신규 출처 6건(ref-1359~ref-1364)과 ref-762, ref-1093이다. 재인용 출처에만 기댄 19건(f7, f8, f9, f12, f20, f23, f24, f28~f33, f38~f43)은 원문을 다시 열지 않았고, 게시 페이지의 기존 검증 결과에 기대어 확인으로 셌다(검증 예산). 검색은 2회 썼다. 강등: 없음. 대신 f16·f17·f26은 해석 절을 [추정] 문장으로 분리하고, f10·f18은 원문 범위로 좁혀 쓰도록 지시했다. 원문 미열람 출처: ref-1096, ref-302, ref-1099, ref-1098, ref-1103, ref-494, ref-453, ref-1236, ref-150, ref-139, ref-140, ref-146, ref-102, ref-1278, ref-1272, ref-096, ref-145, ref-1153, ref-1157, ref-1150, ref-1151, ref-944, ref-1199, ref-1152, ref-1154(ref-1093은 검증에서 확인했으나 브리프 기준 미열람). 브리프 표시 불일치가 있다: f25·f27은 미열람 출처에 기대는데 source_unopened가 false로 적혀 있다. 또 page_proposals의 절 이름에 번호('5.')를 붙였다. 주의: 대부분의 연결은 단일 출처이거나 게시 페이지 판단의 재인용이다. ANSI/ISA 18.2-2016은 공정 산업 표준이며 2016판이 최신으로 확인된다(후속 개정 계획만 있음). ISO 22400-2 개정판은 2026-10-09 기준 FDIS 단계로 미발행이다. 마약류 관리대장 보관 기간은 2018년 기사 기준이고 현행 법령은 미확인이다. B. 로봇 온톨로지와의 연결 근거는 없다. 현장 근거는 물류창고·제조 공장·병원·상업 시설에 한정된다. 정정 요청 없음.",
  "retry_reason": null
}
```

### templates/category.md

```markdown
---
title: "{{category}}"                       # 원문 명칭 그대로. 예: "B. 로봇 온톨로지"
type: category
category: "{{category}}"                    # title 과 같은 값
tags: [{{tags}}]                            # 선택. 없으면 []
status: {{status}}                          # seed | published. 시드 대분류 페이지는 seed 이며, "다른 대분류와의 연결"이 채워져 게시되면 published 로 바꾼다 [가정]
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 원문 주석의 [n] 에 대응하는 참고문헌 id. 예: [ref-003]
version: {{version}}                        # 정수
---
<!--
[템플릿] 대분류 페이지 (type: category)
경로: docs/categories/<대분류 slug>/index.md
쓰임: 구축 시 원문 부분(핵심 질문·개요·세부 연구영역·이 대분류의 핵심 포인트)을 채워 만든다. "다른 대분류와의 연결"은 에이전트(스토리텔러)가 관련 영역을 다루는 실행에서 채우고, "세부 연구영역" 표(페이지·현재 상태 열 포함)와 "이 대분류의 자료"(논문·기사·업체 발표·표준 묶음별 출처 목록, 2026-09-28 추가), "최근 업데이트"는 퍼블리셔가 자동 갱신한다.
일곱 섹션(4.3 + 2026-09-28 추가): 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 이 대분류의 자료 / 최근 업데이트. 제목·순서 고정. H2 문자열은 사양서 4.3 문구 그대로이며 번호를 붙이지 않는다(pipeline/checks/protect_source.py 의 CATEGORY_SECTIONS 와 글자 단위로 같다. "1. 핵심 질문"처럼 번호를 붙이면 "섹션 제목·순서 불일치"로 반려된다). 각주 정의를 둘 자리로 번호 없는 "참고 자료" 절을 여섯 섹션 뒤에 하나 더 두었다. 이 절은 사양서 4.3 의 여섯 섹션에 없는 구축자 추가 절이다 [가정].

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 같은 대분류의 세부영역은 <파일>.md, 다른 대분류는 ../<대분류 slug>/index.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › {{category}}

# {{category}}

## 핵심 질문

{{core_question}} [분류원문]
<!-- 분류 원문 1장 표의 "핵심 질문" 칸 문장 그대로. 예: "서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]". 수정 금지. -->

## 개요

{{overview_paragraph}} [분류원문]
<!-- 분류 원문에서 이 대분류 장의 첫 문단(표 위의 문단)을 굵게 표기까지 그대로 옮긴다. 예: "서로 다른 제조사의 로봇을 등록하고, 무엇을 할 수 있는지 공통 모델로 표현하고, 그 모델로 시스템과 로봇이 쉽게 연동되게 하는 온톨로지 기능 전체. [분류원문]". 굵은 표기가 있으면 그대로 두고, 명사형으로 끝나는 문단도 고치지 않는다. -->

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |

[분류원문]
<!-- auto:category-area-table:end -->
<!--
원문 표의 행(대분류마다 3~7행)을 모두 그대로 옮기고(앞 3열은 원문 셀과 글자 단위로 같게, 첫 열의 굵은 표기 유지, 첫 열에 링크를 씌우지 않음), "페이지" 열에 세부영역 페이지 링크, "현재 상태" 열에 해당 페이지 프런트매터 status(seed | draft | verified | published | needs_update | deprecated)를 둔다(4.3 의 "링크와 현재 상태 열만 추가"). 표 바로 아래 빈 줄 다음에 [분류원문] 한 줄을 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_category)가 각 행의 앞 3칸과 [분류원문] 줄을 원문과 대조한다.
표 전체는 auto:category-area-table 마커 안에 있고 퍼블리셔(pipeline/lib/render.py render_category_area_table)가 원문 파서와 세부영역 페이지의 status 로 다시 쓴다. 스토리텔러는 마커 사이를 건드리지 않는다. 마커 위의 안내 문장은 마커 밖이므로 그대로 둔다. 이 key 는 사양서에 없는 구축자 추가 key 이며, 시드 대분류 페이지·agents/shared-rules.md 6절의 auto key 목록·퍼블리셔(pipeline/lib/autoregion.py AUTO_KEYS)가 같은 값을 쓴다 [가정 — 사용자 결정 항목: 표 전체를 자동 영역으로 둘지, 표는 마커 밖에 두고 현재 상태 열만 갱신할지].
-->

## 이 대분류의 핵심 포인트

{{key_point_paragraphs}}
<!--
분류 원문에서 이 대분류 장의 표 아래 설명 문단들을 순서대로 모두 옮긴다. 문단마다 끝에 " [분류원문]" 을 붙이고, 그 줄에는 태그 뒤에 아무것도(각주 포함) 붙이지 않는다. 원문의 [n] 번호 표기는 문장 안에 그대로 둔다. 예: "... 참고 표준이다. [3] [분류원문]". 대응 각주 [^ref-00n] 은 이 절이 아니라 "참고 자료" 절의 별도 문장에 둔다. 굵게·기울임 표기를 유지한다. 에이전트는 이 절의 원문 문장을 고치지 않고, 원문 문단 뒤에 자기 문장을 덧붙이지도 않는다.
퍼블리셔(pipeline/checks/protect_source.py check_category)는 이 절에서 " [분류원문]" 으로 끝나는 줄만 모아 원문 문단 목록과 글자 단위로 대조한다. 태그 뒤에 각주를 붙이면 그 줄이 빠져 "핵심 포인트 문단 불일치"로 반려된다.
-->

## 다른 대분류와의 연결

{{category_connections}}
<!--
에이전트가 채운다. 목록 형식: "- [F. 연동](../integration/index.md) — 이 대분류의 어떤 영역이 저 대분류의 어떤 영역과 왜 이어지는지 한두 문장(세부영역은 번호와 이름 함께)". 주장에는 태그·각주. 구축 시에는 "아직 작성되지 않음"으로 둔다.
M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회처럼 여러 대분류에 걸쳐 적용되는 대분류는 그 적용 관계를 드러낸다. Q. 현장 유형별 적용은 현장마다 다른 요구를 모으고 모든 현장에 공통인 기능은 A~P에 둔다는 원문 취지를 지킨다. L. AI·학습 기술의 교차 규칙(매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석)과 C. 채팅 기반 구성·운영의 엔진 짝(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 여기서도 지킨다.
-->

## 이 대분류의 자료

<!-- auto:category-sources:start -->
(퍼블리셔가 자동 생성: 이 대분류 페이지·소속 세부영역·주제 페이지가 인용한 출처를 논문 / 기사·보고서 / 업체 발표(벤더 문서) / 표준·오픈소스·기관 자료로 묶어 최근 발행순으로 보인다)
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:category-recent:end -->
<!-- 퍼블리셔가 이 대분류에 속한 세부영역·주제 페이지의 최근 변경을 최신순으로 넣는다(날짜 | 실행 id | 페이지 | 변경 요약). 마커 사이는 스토리텔러가 건드리지 않는다. -->

## 참고 자료

{{source_footnote_sentences}}

{{footnotes}}
<!-- "이 대분류의 핵심 포인트" 원문 문단의 [n] 에 대응하는 각주를 별도 문장으로 두고(예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]"), 그 아래에 각주 정의를 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". "다른 대분류와의 연결"에서 쓴 각주도 여기에 둔다. 각주가 없으면 "없음". 이 절은 사양서 4.3 의 여섯 섹션 밖의 보조 절로, 5.3 의 각주 정의 자리를 위해 구축자가 추가했으며 번호를 붙이지 않는다 [가정]. -->
```

### docs/categories/field-operations-and-monitoring/index.md

```markdown
---
title: "J. 현장 운영·관제"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › J. 현장 운영·관제

# J. 현장 운영·관제

## 핵심 질문

운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]

## 개요

운영 사용자가 상태를 보고, 이상을 알아차리고, 원인을 찾고, 성과를 측정하고, 운영 절차를 돌리는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **37. 관제 화면·실행 기록** | 지도 위 상태 표시, 설명 가능한 표시, 실행 기록 재생 | 운영자가 지금 무슨 일이 왜 일어나는지 한눈에 알 수 있는가? | [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) | published |
| **38. 모니터링·이상 탐지·원인 분석** | 감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 | 지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? | [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) | published |
| **39. 운영 성과 측정·개선** | 지표 정의·측정, 로봇 성과와 업무 성과 구분, 운영 개선 | 로봇 가동률이 오른 것이 실제 업무 성과로 이어졌는가? | [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) | published |
| **40. 운영 절차·요청 창구** | 운영 절차·교대, 현장 사용자의 요청 창구 | 현장 사람들이 로봇에게 일을 맡기고 운영자가 교대하는 절차가 정해져 있는가? | [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

운영 화면은 로봇 상태를 보여 주는 데서 끝나지 않는다. **왜 그런 상태인지와 사람이 무엇을 해야 하는지**까지 보여 줘야 운영자가 개입할 수 있다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 67건이다(논문 24건 · 기사·보고서 8건 · 업체 발표 4건 · 표준·오픈소스·기관 자료 31건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-455](../../references/ref-455.md) — DBpia 게재 논문(저자 미확인), 다중 자율이동로봇 (AMR) 운영을 위한 웹 기반 사용자 중심 관제 인터페이스 설계 연구 (발행 2026-07)
- [ref-102](../../references/ref-102.md) — Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics (발행 2025)
- [ref-454](../../references/ref-454.md) — International Journal of Production Research(Taylor & Francis), 저자 미확인, Process mining in supply chain management: state-of-the-art, use cases and research outlook (발행 2024)
- [ref-146](../../references/ref-146.md) — Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority (발행 2024)
- [ref-453](../../references/ref-453.md) — Liu, Z., Bahety, A., & Song, S., REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction (발행 2023)
- [ref-115](../../references/ref-115.md) — Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes (발행 2023)
- [ref-1098](../../references/ref-1098.md) — Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding (발행 2022-02)
- [ref-452](../../references/ref-452.md) — Soldani, J., & Brogi, A., Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey (발행 2022)
- [ref-1150](../../references/ref-1150.md) — Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model (발행 2022)
- [ref-145](../../references/ref-145.md) — Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers (발행 2021)
- 그 밖에 14건

**기사·보고서**

- [ref-1154](../../references/ref-1154.md) — Proof News (Varsha Bansal), Meet the Robot That Nurses Unplugged (발행 2026-06-09)
- [ref-1103](../../references/ref-1103.md) — 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 (발행 2025-04-07)
- [ref-141](../../references/ref-141.md) — WERC(Warehousing Education and Research Council), WERC DC Measures Survey - 2025 (발행 2025)
- [ref-1199](../../references/ref-1199.md) — ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인) (발행 2024-09-19)
- [ref-944](../../references/ref-944.md) — 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' (발행 2024-04-15)
- [ref-1152](../../references/ref-1152.md) — 한국일보, “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인) (발행 2017-04-18)
- [ref-150](../../references/ref-150.md) — CIO Korea, 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 (발행 미확인)
- [ref-143](../../references/ref-143.md) — Project Production Institute, Little’s Law – A Practical Approach to Understanding Production System Performance (발행 미확인)

**업체 발표**

- [ref-1156](../../references/ref-1156.md) — OMRON Industrial Automation Europe, Autonomous Mobile Robots (AMR) (발행 미확인)
- [ref-1102](../../references/ref-1102.md) — 네이버클라우드, ARC brain 개요 - 사용 가이드 (발행 미확인)
- [ref-1101](../../references/ref-1101.md) — 현대자동차그룹 로보틱스랩, PROJECTS — Robot Fleet Management (NARCHON) (발행 미확인)
- [ref-1097](../../references/ref-1097.md) — Foxglove, Playback — Foxglove Documentation (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-1157](../../references/ref-1157.md) — 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등) (발행 2025-09-01)
- [ref-782](../../references/ref-782.md) — ISO, ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management (발행 2017-04)
- [ref-139](../../references/ref-139.md) — ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions (발행 2014)
- [ref-1148](../../references/ref-1148.md) — UK Health and Safety Executive (HSE) (humanfactors101.com 게재본), Human Factors Briefing Note No. 8 — Safety-Critical Communications (발행 2005)
- [ref-781](../../references/ref-781.md) — ISO, ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions (발행 미확인)
- [ref-762](../../references/ref-762.md) — Open Robotics (open-rmf), rmf-web — packages/api-server/README.md (발행 미확인)
- [ref-569](../../references/ref-569.md) — Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg (발행 미확인)
- [ref-449](../../references/ref-449.md) — VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema (발행 미확인)
- [ref-448](../../references/ref-448.md) — Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg (발행 미확인)
- [ref-447](../../references/ref-447.md) — OpenTelemetry (CNCF), OpenTelemetry Specification — Overview (발행 미확인)
- 그 밖에 21건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) — 영역 심화: 3~11절 신규 작성, 13절 각주 정의 16건, 프런트매터 related_areas·tags·confidence·sources·last_run 채움(1차 조건부 승인 수정 16건 반영). 2차 재실행에서 이 페이지 본문은 변경 없음 (실행 2026-09-30-18)
- 2026-09-30 · 생성 · [40. 운영 절차·요청 창구 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area40-s6.md) — 자동 분리: 40. 운영 절차·요청 창구 의 "6. 대표 접근법과 기술" 절(1,472자)을 옮겼다. 2차: '전담 운영 조직' 소제목의 호텔 문장에서 출처에 없는 '전담 조직 없이'를 뺌 (실행 2026-09-30-18)
- 2026-09-30 · 생성 · [40. 운영 절차·요청 창구 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area40-s7.md) — 자동 분리: 40. 운영 절차·요청 창구 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,355자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-18)
- 2026-09-30 · 생성 · [40. 운영 절차·요청 창구 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area40-s4.md) — 자동 분리: 40. 운영 절차·요청 창구 의 "4. 핵심 개념과 용어" 절(1,134자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-18)
- 2026-09-30 · 생성 · [40. 운영 절차·요청 창구 — 대표 연구와 자료](../../topics/2026/2026-09-30-area40-s8.md) — 자동 분리: 40. 운영 절차·요청 창구 의 "8. 대표 연구와 자료" 절(938자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-18)
<!-- auto:category-recent:end -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 77건 / 전체 1242건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-001 | ASCM | SCOR Digital Standard | 미확인 | https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/ | 2026-09-24 | 아니오 |
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 2026-09-25 | 아니오 |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | https://www.w3.org/TR/vocab-ssn/ | 2026-09-25 | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | https://repub.eur.nl/pub/107376/ | 2026-09-25 | 아니오 |
| ref-097 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 2020 | https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517 | 2026-09-25 | 아니오 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 2026-09-25 | 아니오 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 2026-09-25 | 아니오 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | https://cslc.koti.re.kr/ | 2026-09-25 | 아니오 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 2026-09-25 | 예 |
| ref-115 | Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본) | Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes | 2023 | https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031 | 2026-09-25 | 아니오 |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | https://www.iso.org/standard/67480.html | 2026-09-25 | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 2026-09-25 | 예 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | https://www.iso.org/standard/54497.html | 2026-09-25 | 아니오 |
| ref-140 | ASCM | SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment | 미확인 | https://scor.ascm.org/performance/reliability/RL.1.1 | 2026-09-25 | 아니오 |
| ref-141 | WERC(Warehousing Education and Research Council) | WERC DC Measures Survey - 2025 | 2025 | https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf | 2026-09-25 | 아니오 |
| ref-142 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Overall Equipment Effectiveness: consistency of ISO standard with literature | 2020 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527 | 2026-09-25 | 아니오 |
| ref-143 | Project Production Institute | Little’s Law – A Practical Approach to Understanding Production System Performance | 미확인 | https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/ | 2026-09-25 | 아니오 |
| ref-144 | Azadeh, K., de Koster, R., & Roy, D. | Robotized and Automated Warehouse Systems: Review and Recent Developments | 2019 | https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873 | 2026-09-25 | 아니오 |
| ref-145 | Ghelichi, Z., & Kilaru, S. | Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers | 2021 | https://www.sciencedirect.com/science/article/pii/S0307904X20305801 | 2026-09-25 | 아니오 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 2026-09-25 | 아니오 |
| ref-147 | Process Intelligence Solutions (PM4Py GitHub) | pm4py — Official public repository for PM4Py (Process Mining for Python) (README) | 미확인 | https://github.com/process-intelligence-solutions/pm4py | 2026-09-25 | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 2026-09-25 | 예 |
| ref-149 | Springer(학술대회 발표 논문, 저자 미확인) | Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study | 2015 | https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9 | 2026-09-25 | 아니오 |
| ref-150 | CIO Korea | 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 | 미확인 | https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html | 2026-09-25 | 아니오 |
| ref-151 | 박정수, 안영효(유통경영학회지) | 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구 | 2010 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387 | 2026-09-25 | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 2026-09-25 | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 2026-09-25 | 예 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | https://github.com/open-rmf/rmf-web | 2026-09-25 | 예 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 2026-09-25 | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 2026-09-25 | 아니오 |
| ref-345 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 2018-03-05 | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 | 2026-09-25 | 아니오 |
| ref-445 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 미확인 | https://github.com/ros/diagnostics/blob/ros2/README.md | 2026-09-25 | 예 |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 2026-09-25 | 예 |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 2026-09-25 | 예 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 2026-09-25 | 예 |
| ref-451 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 2003 | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ | 2026-09-25 | 아니오 |
| ref-452 | Soldani, J., & Brogi, A. | Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey | 2022 | https://dl.acm.org/doi/full/10.1145/3501297 | 2026-09-25 | 아니오 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023 | https://arxiv.org/abs/2306.15724 | 2026-09-25 | 아니오 |
| ref-454 | International Journal of Production Research(Taylor & Francis), 저자 미확인 | Process mining in supply chain management: state-of-the-art, use cases and research outlook | 2024 | https://www.tandfonline.com/doi/full/10.1080/00207543.2024.2412285 | 2026-09-25 | 아니오 |
| ref-455 | DBpia 게재 논문(저자 미확인) | 다중 자율이동로봇 (AMR) 운영을 위한 웹 기반 사용자 중심 관제 인터페이스 설계 연구 | 2026-07 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12892366 | 2026-09-25 | 아니오 |
| ref-477 | Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 미확인 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 2026-09-25 | 아니오 |
| ref-486 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 2019 | https://www.iso.org/standard/75106.html | 2026-09-25 | 아니오 |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | https://www.omg.org/spec/BPMN/2.0.2/ | 2026-09-25 | 아니오 |
| ref-509 | ISO | ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles | 2019 | https://www.iso.org/standard/68519.html | 2026-09-25 | 아니오 |
| ref-510 | IEC / IEEE / ISO | IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 2019 | https://www.iso.org/standard/71620.html | 2026-09-25 | 아니오 |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 2026-09-25 | 예 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 2026-09-25 | 아니오 |
| ref-679 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보구축작업규정 (고시 제2021-1445호, 2021-12-24) | 2021-12-24 | https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/%EC%8B%A4%EB%82%B4%EA%B3%B5%EA%B0%84%EC%A0%95%EB%B3%B4%EA%B5%AC%EC%B6%95%EC%9E%91%EC%97%85%EA%B7%9C%EC%A0%95/(2021-1445,20211224) | 2026-09-25 | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 2026-09-25 | 예 |
| ref-767 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels | 2013-08 | https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013 | 2026-09-25 | 아니오 |
| ref-781 | ISO | ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 미확인 | https://www.iso.org/standard/87563.html | 2026-09-26 | 아니오 |
| ref-782 | ISO | ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management | 2017-04 | https://www.iso.org/standard/68295.html | 2026-09-26 | 아니오 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 2026-09-29 | 예 |
| ref-1093 | Open Robotics (open-rmf/rmf_visualization) | rmf_visualization — README | 미확인 | https://github.com/open-rmf/rmf_visualization | 2026-09-30 | 예 |
| ref-1094 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_log.json (Task Event Log) | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json | 2026-09-30 | 예 |
| ref-1095 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json | 2026-09-30 | 예 |
| ref-1096 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | https://mcap.dev/spec | 2026-09-30 | 예 |
| ref-1097 | Foxglove | Playback — Foxglove Documentation | 미확인 | https://docs.foxglove.dev/docs/visualization/playback | 2026-09-30 | 예 |
| ref-1098 | Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022) | Conflict-Based Search for Explainable Multi-Agent Path Finding | 2022-02 | https://arxiv.org/abs/2202.09930 | 2026-09-30 | 예 |
| ref-1099 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 2017-07-27 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ | 2026-09-30 | 예 |
| ref-1100 | ISA (International Society of Automation) | ISA-101 Series of Standards | 미확인 | https://www.isa.org/standards-and-publications/isa-standards/isa-101-standards | 2026-09-30 | 예 |
| ref-1101 | 현대자동차그룹 로보틱스랩 | PROJECTS — Robot Fleet Management (NARCHON) | 미확인 | https://robotics.hyundai.com/projects/research/view.do?seq=102 | 2026-09-30 | 예 |
| ref-1102 | 네이버클라우드 | ARC brain 개요 - 사용 가이드 | 미확인 | https://guide.ncloud-docs.com/docs/arc-brain-overview | 2026-09-30 | 예 |
| ref-1103 | 아주경제 | 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 | 2025-04-07 | https://www.ajunews.com/view/20250407084333272 | 2026-09-30 | 예 |
| ref-1148 | UK Health and Safety Executive (HSE) (humanfactors101.com 게재본) | Human Factors Briefing Note No. 8 — Safety-Critical Communications | 2005 | https://humanfactors101.com/wp-content/uploads/2016/04/human-factors-briefing-note-safety-critical-communications.pdf | 2026-09-30 | 예 |
| ref-1149 | Brazier, A., & Pacitti, B. (IChemE Hazards XX) | Improving shift handover and maximising its value to the business | 2008 | https://www.icheme.org/media/9743/xx-paper-48.pdf | 2026-09-30 | 예 |
| ref-1150 | Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management) | The perils of hotel technology: The robot usage resistance model | 2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/ | 2026-09-30 | 예 |
| ref-1151 | Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008) | Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction | 2008-03 | https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf | 2026-09-30 | 예 |
| ref-1152 | 한국일보 | “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인) | 2017-04-18 | https://www.hankookilbo.com/news/article/201704180418820469 | 2026-09-30 | 예 |
| ref-1153 | ANSI (The ANSI Blog) | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 미확인 | https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/ | 2026-09-30 | 아니오 |
| ref-1154 | Proof News (Varsha Bansal) | Meet the Robot That Nurses Unplugged | 2026-06-09 | https://www.proofnews.org/moxi/ | 2026-09-30 | 예 |
| ref-1155 | Blazin, L. J. 외 (Pediatric Quality & Safety) | Improving Patient Handoffs and Transitions through Adaptation and Implementation of I-PASS Across Multiple Handoff Settings | 2020-07 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7382547/ | 2026-09-30 | 예 |
| ref-1156 | OMRON Industrial Automation Europe | Autonomous Mobile Robots (AMR) | 미확인 | https://industrial.omron.eu/en/products/autonomous-mobile-robot | 2026-09-30 | 예 |
| ref-1157 | 고용노동부 (국가법령정보센터) | 산업안전보건기준에 관한 규칙 제222조(교시 등) | 2025-09-01 | https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202 | 2026-09-30 | 예 |
| ref-1199 | ZDNet Korea | 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인) | 2024-09-19 | https://zdnet.co.kr/view/?no=20240919162124 | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 346개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
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

### docs/open-questions.md (요약: 대상 영역 [37, 38, 39, 40] 에 걸린 35건 / 전체 294건)

```markdown
- oq-008 [열림] 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? (영역 35, 39)
- oq-011 [열림] 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? (영역 35, 39)
- oq-015 [열림] 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? (영역 23, 39)
- oq-016 [열림] 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? (영역 28, 39)
- oq-017 [열림] 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? (영역 35, 39)
- oq-018 [열림] 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? (영역 38, 39)
- oq-033 [열림] Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 29, 38)
- oq-051 [열림] 피킹–포장 동기화의 성과를 포장 작업자 대기시간이나 주문 완료 시간 분산 같은 지표로 재는 합의된 정의가 있는가, ROP 가 순서 결정의 목적함수로 쓸 수 있는가? (영역 26, 39)
- oq-052 [열림] 국내외 물류센터에서 최근접 배정 규칙과 전역 최적화(또는 LLM 기반) 배정을 같은 조건에서 비교해 총 이동거리·처리량·납기 준수를 실측한 자료가 있는가? (영역 25, 39)
- oq-066 [열림] 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? (영역 28, 39)
- oq-071 [열림] 국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가? (영역 31, 39)
- oq-072 [열림] 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? (영역 31, 38)
- oq-073 [열림] VDA 5050 3.0.0 판의 네 단계 오류 수준(WARNING·URGENT·CRITICAL·FATAL)과 이전 판(2.x)의 오류 수준이 다를 때, 두 판이 섞인 이종 플릿에서 오류 수준을 어떻게 맞춰 해석하는가? (영역 20, 38)
- oq-074 [열림] 물류 로봇 작업 지연을 로봇·설비·통신·공정 원인으로 나누는 공개 원인 분류 체계나 현장 데이터셋이 있는가? (영역 38, 39)
- oq-075 [열림] 국내 물류센터에서 로봇 정지·지연의 원인별 발생 비율이나 이상 대응 시간을 실측해 공개한 자료가 있는가? (영역 32, 38)
- oq-082 [열림] 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? (영역 25, 38, 51)
- oq-084 [열림] 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? (영역 34, 39)
- oq-119 [열림] 국내에서 실내공간정보 구축이나 로봇 도입 시 지도·공용 자원 설정 공수(인·일)를 산정하는 품셈이나 공공 기준이 있는가? (영역 39, 55)
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
- oq-194 [열림] 플랜트·변전소 점검 로봇이 얻은 계기값·열화상·이상 판정은 설비 보전 시스템의 작업 지시·점검 기록으로 어떤 형식과 승인 절차를 거쳐 돌아가는가? (영역 67, 23, 38)
- oq-203 [열림] 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? (영역 16, 40, 63)
- oq-210 [열림] 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? (영역 43, 38)
- oq-221 [열림] 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? (영역 46, 38)
- oq-237 [열림] 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? (영역 37, 21)
- oq-238 [열림] 에이전트 투명성이나 계획 분할 시각화 같은 설명 가능한 표시를 실제 운영 중인 로봇 플릿 관제 화면에 적용해 운영자의 상황 인식과 대응 시간을 현장에서 측정한 연구가 있는가? (영역 37, 31)
- oq-239 [열림] 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? (영역 37, 59)
- oq-240 [열림] 공정 산업의 ISA-101 처럼 다중 로봇 관제 화면에 특화된 화면 설계 표준이나 지침이 있는가, 아니면 공정 HMI 표준을 옮겨 써야 하는가? (영역 37, 38)
- oq-248 [열림] 명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가? (영역 52, 37)
- oq-252 [열림] 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? (영역 50, 37, 38)
- oq-263 [열림] 여러 제조사 로봇을 한 관제에서 운영할 때 교대 인수인계로 넘길 항목(열린 작업, 폐쇄 구역, 수동 모드 로봇, 미해결 예외)을 정한 공개 절차나 체크리스트가 있는가? (영역 40, 37)
- oq-264 [열림] 병원·호텔에서 안내 데스크·프런트 담당자가 로봇 요청을 대신 입력하는 방식과 현장 사용자가 직접 요청하는 방식의 처리 시간·오류·업무 부담을 비교한 연구가 있는가? (영역 40, 63, 64)
- oq-265 [열림] ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? (영역 40, 50, 58)
- oq-266 [열림] 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? (영역 40, 56, 60)
- oq-268 [열림] 사용량 기반 서비스형 로봇 계약에서 과금·최소 요금·가동률 미달을 판정하는 계량 데이터를 누가 측정하고, 여러 사업자가 함께 쓰는 현장에서 그 값을 어떻게 합의하는가? (영역 3, 58, 39)
- oq-278 [열림] 로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가? (영역 56, 40, 60)
```

### docs/standards/index.md (요약: 318개 — 이름 · 종류 · 발행 기관)

```markdown
- SCOR (SCOR Digital Standard) · 표준 · ASCM(Association for Supply Chain Management)
- ISA-95 (ANSI/ISA-95) · 표준 · ISA(International Society of Automation)
- GS1 EPCIS · 표준 · GS1
- Open-RMF · 오픈소스 · Open Robotics
- ROS 2 DDS-Security (ROS 2 DDS-Security Integration) · 프레임워크 · ROS 2 Design
- ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) · 프레임워크 · ROS 2 Design
- NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) · 평가 프로그램 · NIST(National Institute of Standards and Technology)
- ARIAC · 평가 프로그램 · NIST
- GS1 EPCIS 2.0 (ISO/IEC 19987:2024) · ISO/IEC · GS1 · 표준
- GS1 CBV (Core Business Vocabulary) · GS1 · 표준
- SSCC (Serial Shipping Container Code) · GS1 · 표준
- GS1 Logistic Label Guideline · GS1 · 표준
- GRAI (Global Returnable Asset Identifier) · GS1 · 표준
- GIAI (Global Individual Asset Identifier) · GS1 · 표준
- EPC Tag Data Standard (1.11판) · GS1 · 표준
- VDA 5050 (2.0.0) · VDA(Verband der Automobilindustrie) · 표준
- OpenEPCIS · OpenEPCIS · 오픈소스
- IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) · IEEE · 표준
- IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology · IEEE · 표준
- W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) · W3C / OGC · 표준
- VDA 5050 (3.0.0) · VDA(Verband der Automobilindustrie) · 표준
- MassRobotics AMR Interoperability Standard (1.0) · MassRobotics · 표준
- OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) · OPC Foundation / VDMA · 표준
- Information Model for Capabilities, Skills & Services (CSS) · Plattform Industrie 4.0 · 프레임워크
- Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) · Auto-ID Labs Korea(세종대학교) · 오픈소스
- RAWSim-O · Merschformann, M. (RAWSim-O GitHub) · 오픈소스
- 스마트물류센터 인증제 · 한국교통연구원(인증스마트물류센터) · 평가 프로그램
- BPMN 2.0 (ISO/IEC 19510:2013) · OMG(Object Management Group) · ISO/IEC · 표준
- IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 · IEC / ISO · 표준
- B2MML (Business To Manufacturing Markup Language, 판 0701) · MESA International · 표준
- OCEL 2.0 (Object-Centric Event Log) · arXiv:2403.01975 저자(미확인) · 표준
- ISO 22400-2:2014 제조 운영 관리 KPI 정의 · ISO · 표준
- WERC DC Measures · WERC(Warehousing Education and Research Council) · 평가 프로그램
- PM4Py · Process Intelligence Solutions · 오픈소스
- OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) · OPC Foundation / ISA · 표준
- osmAG-from-cad (CAD-to-osmAG 파이프라인) · Zhang, J. (jiajiezhang7 GitHub) · 오픈소스
- Ogm2Pgbm · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- ifc2indoorgml · Diakité, A. A. 외 · 오픈소스
- IDTA 02020 Capability Description 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- CaSkMan · CaSkade-Automation (GitHub) · 오픈소스
- SOMA (Socio-physical Model of Activities) · EASE CRC · 오픈소스
- IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) · Helmut Schmidt University, Institute of Automation Technology · 오픈소스
- ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 · ISO · 표준
- KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- VDMA LIF (Layout Interchange Format) · VDMA · 표준
- IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) · buildingSMART · 표준
- Nav2 Docking Framework (nav2_docking) · ROS Navigation (Open Navigation) · 오픈소스
- IDTA 02020 Capability Description (AAS 서브모델 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 · ISO · 표준
- KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- SkiROS2 · RVMI lab, Aalborg University · 오픈소스
- LIF (Layout Interchange Format) 1.0.0 · VDMA · 표준
- ISO 21423 Industrial mobile robots — Communications and interoperability · ISO · 표준
- IFC 4.3 (IfcSpace) · buildingSMART International · 표준
- OGC IndoorGML 2.0 · OGC · 표준
- ISO 19164:2024 Indoor feature model · ISO · 표준
- GS1 GLN (Global Location Number) · GS1 · 표준
- REP 105 Coordinate Frames for Mobile Platforms · ROS (ros-infrastructure/rep) · 프레임워크
- ROSA (ROS Agent) · NASA Jet Propulsion Laboratory · 오픈소스
- RAI · Robotec.ai · 오픈소스
- free_fleet (Open-RMF 플릿 어댑터) · Open Robotics (open-rmf) · 오픈소스
- ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) · InOrbit · 오픈소스
- Open-RMF fleet_adapter_template · Open Robotics (open-rmf) · 오픈소스
- SLAM Toolbox · Macenski, S. (SteveMacenski GitHub) · 오픈소스
- ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) · Open Robotics (ROS 2 Documentation) · 오픈소스
- Eclipse Sparkplug (Chapter 5 Operational Behavior) · Eclipse Foundation · 표준
- OPC UA Part 4: Services (7.11 DataValue) · OPC Foundation · 표준
- ISO 23247 제조 디지털 트윈 프레임워크 · ISO (NIST 해설 경유) · 표준
- ROS 2 설계 문서 — ROS on DDS · QoS 정책 · ROS 2 Design · 프레임워크
- rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) · ROS 2 (ros2/rmw_zenoh) · 오픈소스
- KubeEdge · KubeEdge (CNCF) · 오픈소스
- Open-RMF rmf-web (대시보드·API 서버) · Open Robotics (open-rmf) · 오픈소스
- MQTT Version 5.0 · OASIS · 표준
- NIST SP 500-325 Fog Computing Conceptual Model · NIST · 프레임워크
- KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 · 산업통상자원부 국가기술표준원 · 표준
- Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) · Open Robotics (open-rmf) · 오픈소스
- KnowRob (하이브리드 지식 베이스) · KnowRob (knowrob GitHub) · 오픈소스
- IEEE1872-owl (CORA 공개 OWL 번역, 제3자) · srfiorini (IEEE1872-owl GitHub) · 오픈소스
- CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) · OGC · 표준
- IMDF (Indoor Mapping Data Format) 1.0.0 · OGC / Apple · 표준
- BOT (Building Topology Ontology) 0.3.2 · W3C Linked Building Data Community Group · 프레임워크
- ifcOWL · buildingSMART · 표준
- Brick Schema · Brick Consortium · 오픈소스
- ISO 16739-1:2024 (IFC 4.3) · ISO · 표준
- Rasa 폼(Forms, Rasa 3.x) · Rasa Technologies · 오픈소스
- ROS 2 액션 설계(Actions) · ROS 2 Design · 프레임워크
- ROS 2 관리형 노드 수명주기(Managed nodes) · ROS 2 Design · 프레임워크
- Open-RMF rmf_task · Open Robotics (open-rmf) · 오픈소스
- IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) · IETF HTTPAPI Working Group · 표준
- OPC UA Part 10: Programs (v1.04) · OPC Foundation · 표준
- ISA-TR88.00.02 Machine and Unit States (PackML) · ISA · 표준
- BehaviorTree.CPP · BehaviorTree (GitHub) · 오픈소스
- OR-Tools CP-SAT (스케줄링 레시피) · Google · 오픈소스
- Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) · Open Robotics (open-rmf) · 오픈소스
- rmf_task (Open-RMF 작업 계획기 TaskPlanner) · Open Robotics (open-rmf) · 오픈소스
- ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 · ISO · 표준
- 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) · National Institute of Building Sciences · 표준
- KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 · 국가표준인증통합정보시스템(KSSN) · 표준
- 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) · 한국건설기술연구원(건설CALS 체계) · 표준
- ezdxf (DXF 읽기·쓰기 라이브러리) · Moitzi, M. (mozman/ezdxf GitHub) · 오픈소스
- ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) · ECLASS e.V. · 표준
- IEC 공통 데이터 사전(IEC CDD) · IEC · 표준
- rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF Traffic Editor · Open Robotics · 오픈소스
- MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) · DiligentPanda (Team Pikachu, GitHub) · 오픈소스
- SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface · SEMI · 표준
- ASTM F3499-21 A-UGV 도킹 성능 시험 방법 · ASTM International · 표준
- ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 · ANSI / A3 · 표준
- KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 · 국가표준인증통합정보시스템(KSSN) · 표준
- Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_reservation (실험적 예약 라이브러리) · Open Robotics (open-rmf) · 오픈소스
- ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 · ISO · 표준
- ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) · ISO (A3 해설 경유) · 표준
- ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 · A3(Association for Advancing Automation) · 표준
- 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 · 고용노동부·한국산업안전보건공단 · 프레임워크
- 이동식 협동로봇 안전기준 KS(표준 번호 미확인) · 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) · 표준
- Open-RMF rmf_demos · Open Robotics (open-rmf) · 오픈소스
- IEC 61360-7:2024 교차 도메인 개념 데이터 사전(General items) · IEC · 표준
- IDTA 02003 Generic Frame for Technical Data for Industrial Equipment in Manufacturing (1.2) · IDTA(Industrial Digital Twin Association) · 표준
- Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- ROS 2 diagnostics · ROS (ros/diagnostics GitHub) · 오픈소스
- ros2_tracing · ROS 2 (ros2/ros2_tracing GitHub) · 오픈소스
- OpenTelemetry Specification · OpenTelemetry (CNCF) · 오픈소스
- Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 경보 메시지(rmf_task_msgs Alert) · Open Robotics (open-rmf) · 오픈소스
- IFCtoLBD (IFC → 링크드 빌딩 데이터 변환기, 판 2.54.0) · Oraskari, J. (jyrkioraskari GitHub) · 오픈소스
- SHACL (Shapes Constraint Language) · W3C · 표준
- IDS (Information Delivery Specification) · buildingSMART · 표준
- RMF Site Editor (rmf_site) · Open Robotics (open-rmf) · 오픈소스
- ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도) · ISO · 표준
- 기업재난관리표준·재해경감 우수기업 인증제 · 행정안전부 · 평가 프로그램
- 중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022) · 고용노동부 · 프레임워크
- 보상 트랜잭션 패턴(Compensating Transaction pattern) · Microsoft (Azure Architecture Center) · 프레임워크
- Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle) · Open Robotics (open-rmf) · 오픈소스
- IEEE 1872.1-2024 Standard for Robot Task Representation · IEEE Standards Association · 표준
- Serverless Workflow (Open Workflow Specification) DSL · CNCF Serverless Workflow · 오픈소스
- HDDL (Hierarchical Domain Definition Language) · Höller 외(IPC 2020 계층 계획 부문) · 프레임워크
- FaMe (BPMN 기반 다중 로봇 시스템 개발 틀) · Pettinari, S. (UNICAM PROS) · 오픈소스
- ISO 20607:2019 기계 안전 — 설명서 일반 작성 원칙 · ISO · 표준
- IEC/IEEE 82079-1:2019 제품 사용 정보 작성 — Part 1: 원칙과 일반 요구사항 · IEC / IEEE / ISO · 표준
- OmniDocBench (PDF 문서 파싱 벤치마크) · OpenDataLab · 오픈소스
- ISO 23247-6:2026 제조 디지털 트윈 프레임워크 — 제6부: 디지털 트윈 결합 · ISO · 표준
- KS X ISO 23247 제조를 위한 디지털 트윈 프레임워크(제1부 개요 및 일반 원리 등) · 국가표준인증종합정보센터(KSSN) · 표준
- Open-RMF rmf_simulation (시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- OFacT (Open Factory Twin) · OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) · 오픈소스
- League of Robot Runners · League of Robot Runners (Amazon Robotics 후원) · 평가 프로그램
- ASTM F45 위원회(무인 자동 유도 산업 차량) · ASTM International (NIST 참여) · 표준
- KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력 · 국가표준인증종합정보센터(KSSN) · 표준
- 한국로봇산업진흥원 로봇 시험평가 · 한국로봇산업진흥원(KIRIA) · 평가 프로그램
- ros2_fault_injection · reeceholland (GitHub) · 오픈소스
- ROSMonitoring · University of Liverpool Autonomy and Verification · 오픈소스
- LSMART (Lifelong Scalable Multi-Agent Realistic Testbed) · Yan, J. 외(arXiv 2602.15721) · 오픈소스
- IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 17359:2018 기계 상태 감시·진단 일반 지침 · ISO · 표준
- ISO 55000:2024 자산 관리 — 용어·개요·원칙 · ISO (ISO/TC 251) · 표준
- IEC TR 62443-2-3:2015 IACS 환경의 패치 관리 · IEC · 표준
- REP 2000 ROS 2 Releases and Target Platforms · Open Robotics (ROS REP) · 프레임워크
- rmf_simulation (Open-RMF 시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- 협동로봇 설치 작업장 안전인증 · 한국로봇사용자협회 · 평가 프로그램
- ISO 12100:2010 기계 안전 — 설계 일반 원칙 — 위험성평가와 위험 감소 · ISO (CEN EN ISO 12100:2010) · 표준
- KS B ISO/TS 15066 로봇 및 로봇 장치 — 협동로봇 · 국가기술표준원(KSSN) · 표준
- Nav2 Route Server (nav2_route) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- NIST SP 800-82 Rev. 3 Guide to Operational Technology (OT) Security · NIST · 프레임워크
- Eclipse Mosquitto (MQTT 브로커, mosquitto.conf ACL·인증서 인증) · Eclipse Foundation · 오픈소스
- SROS 2 접근 제어 정책(ROS 2 Access Control Policies) · ROS 2 Design · 프레임워크
- ROS 2 보안 인클레이브(ROS 2 Security Enclaves) · ROS 2 Design · 프레임워크
- KISA 로봇 보안취약점 점검 체크리스트 해설서 · 한국인터넷진흥원(KISA) · 프레임워크
- NIST AI RMF 1.0 (NIST AI 100-1) · NIST · 프레임워크
- ISO/IEC 42001:2023 AI 관리 시스템 · ISO/IEC · 표준
- ISO/IEC 23894:2023 AI 위험관리 지침 · ISO/IEC · 표준
- MLflow 모델 레지스트리 · MLflow (Linux Foundation 오픈소스 프로젝트) · 오픈소스
- LoTa-Bench · lbaa2022 (LoTa-Bench 공식 저장소) · 오픈소스
- AmbiK 데이터셋 · cog-model (AmbiK 저자) · 오픈소스
- SISO CMSD (Core Manufacturing Simulation Data, SISO-STD-008-2010·SISO-STD-008-01-2012) · SISO(Simulation Interoperability Standards Organization) · 표준
- SLAPStack (블록 적재 창고 저장 위치 배정 시뮬레이션) · Rinciog, A. 외 (malerinc/slapstack GitHub) · 오픈소스
- Semantic Versioning 2.0.0 · Semantic Versioning (semver.org) · 프레임워크
- IETF RFC 9745 The Deprecation HTTP Response Header Field · IETF · 표준
- IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준 · IEC · 표준
- ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항 · ISO/IEC · 표준
- KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 · 한국지능형로봇표준포럼(KOROS) · 표준
- OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증) · OPC Foundation · 평가 프로그램
- Nav2 costmap_2d (비용 지도·비용 지도 필터: 금지 구역·속도 제한) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- SLAM2REF (라이다 데이터의 기준 지도 다중 세션 정렬 도구) · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- Open-RMF rmf_task_ros2 디스패처·입찰 경매자(평가기) · Open Robotics (open-rmf) · 오픈소스
- Rasa 폴백·사람 인계(Fallback and Human Handoff, Rasa 3.x) · Rasa Technologies · 오픈소스
- nudged (2D 유사 변환 추정 라이브러리) · Palonen, A. (axelpale/nudged GitHub) · 오픈소스
- Rasa CALM 대화 복구 패턴(rasa-calm-demo patterns.yml) · Rasa Technologies · 오픈소스
- IfcDiff (IfcOpenShell IFC 모델 비교 도구, v0.8.0 문서) · IfcOpenShell · 오픈소스
- BS EN ISO 19650 Guidance Part C: 공통 데이터 환경(Edition 1) · UK BIM Framework · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency) · OWASP · 프레임워크
- Model Context Protocol 명세 2025-06-18 (Server Features: Tools) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- LangChain Human-in-the-loop 미들웨어 · LangChain · 오픈소스
- ISO 18646-2:2024 서비스 로봇 성능 기준과 시험 방법 — Part 2: 주행 · ISO · 표준
- ASTM F3244 Standard Test Method for Navigation: Defined Area · ASTM International · 표준
- SSIG (평면도 구조 유사도 지표) · van Engelenburg, C. 외 (caspervanengelenburg GitHub) · 오픈소스
- SLABIM (SLAM–BIM 결합 데이터셋) · HKUST Aerial Robotics Group · 오픈소스
- vda5050-sim (VDA 5050 가상 로봇 플릿 시뮬레이터) · gpue (vda5050-sim GitHub, 개인 저장소) · 오픈소스
- vda-5050-lib.js (가상 AGV 어댑터 포함 VDA 5050 라이브러리) · coatyio · 오픈소스
- τ-bench (도구–에이전트–사용자 상호작용 벤치마크) · sierra-research · 평가 프로그램
- SafeAgentBench (LLM 체화 에이전트 안전 계획 벤치마크) · SafeAgentBench 저자(shengyin1224 공식 저장소) · 평가 프로그램
- JSON Schema Validation (json-schema-spec, main 브랜치 차기판 초안) · JSON Schema (json-schema-org) · 표준
- VAL (PDDL 계획 검증 도구) · KCL-Planning · 오픈소스
- JSONSchemaBench · guidance-ai · 오픈소스
- Model Context Protocol 명세 2025-06-18 (Basic: Authorization) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- NIST SP 800-162 속성 기반 접근 통제(ABAC) 정의와 고려 사항 · NIST · 프레임워크
- RobotFleet (LLM·MILP 작업 배정기를 둔 중앙 다중 로봇 계획 틀) · therohangupta (RobotFleet 공식 저장소) · 오픈소스
- rosbag2 · ROS 2 (ros2/rosbag2 GitHub) · 오픈소스
- Simod (로그 기반 업무 프로세스 시뮬레이션 모델 자동 발견 도구) · Camargo, M., Dumas, M., & González-Rojas, O. · 오픈소스
- Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 구성(compose 범주)과 단계 API(ros2multirobotbook task_new) · Open Robotics · 오픈소스
- VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개) · Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) · 오픈소스
- EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) · 개인정보보호위원회 · 프레임워크
- 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 · 과학기술정보통신부·한국정보통신기술협회(TTA) · 프레임워크
- Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크) · Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- langbar (다중 모달 GUI–MCP 아키텍처 참조 구현) · van Dam, H. G. W. · 오픈소스
- IDTA 02006 Digital Nameplate for Industrial Equipment (3.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA-01002 Asset Administration Shell Specification — API (3.2.0) · IDTA(Industrial Digital Twin Association) · 표준
- RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 평가 프로그램
- CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현) · CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) · 오픈소스
- OWL 2 Web Ontology Language Structural Specification (Second Edition) · W3C · 표준
- IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙 · IDTA(Industrial Digital Twin Association) · 표준
- KGCL (Knowledge Graph Change Language) · Hegde, H. 외 (Database, Oxford) · 프레임워크
- ISO 13482 (서비스 로봇 안전 요구사항) · ISO · 표준
- RoMi-H (Robotic Middleware for Healthcare) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 오픈소스
- 서비스로봇 실증사업 · 한국로봇산업진흥원 · 평가 프로그램
- 스마트병원 선도모델(9개 모듈) · 한국보건산업진흥원 스마트병원 확산지원센터 · 프레임워크
- 로봇 친화형 건축물 인증 · 스마트도시협회 · 평가 프로그램
- Matter 1.2 (로봇청소기 장치 유형 포함) · Connectivity Standards Alliance (CSA) · 표준
- 실외이동로봇 운행안전인증 (지능형로봇법 제40조의2) · 한국로봇산업진흥원 · 평가 프로그램
- ISO/TR 4448-1:2024 Public-area mobile robots (PMR) — Part 1: Overview of paradigm · ISO (ISO/TC 204) · 표준
- ISO 4448 시리즈 (Public-area mobile robots, Part 6·9·16 개발 중) · ISO/TC 204 · 표준
- Nav2 GPS 항법 구성 (navsat_transform·두 EKF 융합·rolling 전역 비용 지도) · Open Navigation (Nav2) · 오픈소스
- SiLA 2 (Standardization in Lab Automation 2) · SiLA Consortium · 표준
- ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역 · ISO · 표준
- SS 713 Data Exchange Between Robots, Lifts and Automated Doorways · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- TR 130 Interoperability Between Robots and Central Command Systems · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- IEEE 1873-2015 Robot Map Data Representation for Navigation · IEEE Standards Association (IEEE RAS) · 표준
- osmAG (OSM 형식 계층형 위상·거리 의미 지도) · Feng, D. 외 (arXiv) · 프레임워크
- Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) · Open Robotics (open-rmf) · 오픈소스
- OpenAPI Specification 3.1.0 · OpenAPI Initiative · 표준
- AsyncAPI Specification 3.1.0 · AsyncAPI Initiative · 표준
- FogROS2 (클라우드·포그 로보틱스 플랫폼) · Ichnowski, J., Chen, K., Dharmarajan, K. 외 · 오픈소스
- MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) · Foxglove (ROS 2 채택: Open Robotics) · 오픈소스
- OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 · OpenTelemetry (CNCF) · 오픈소스
- ros-opentelemetry · szobov (GitHub, 개인 저장소) · 오픈소스
- Mender (OTA 업데이트 관리자) · Northern.tech (mendersoftware) · 오픈소스
- FinOps 프레임워크 (FinOps Phases) · FinOps Foundation · 프레임워크
- FOCUS 1.2 (FinOps 청구 데이터 명세) · FinOps Foundation · 표준
- Open X-Embodiment 데이터셋·RT-X 모델 · Open X-Embodiment Collaboration · 오픈소스
- OpenVLA · Kim, M. J., Pertsch, K., Karamcheti, S. 외 · 오픈소스
- GR00T N1 · NVIDIA · 오픈소스
- POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) · Skrynnik, A. 외 (ICLR 2025) · 평가 프로그램
- ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 · ISO (ISO/TC 108) · 표준
- Docling (AI 기반 문서 변환 오픈소스 도구) · IBM Research · 오픈소스
- LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리) · Google (google/langextract) · 오픈소스
- AECV-Bench (건축·엔지니어링 도면 이해 벤치마크) · Kondratenko, A. 외 (arXiv 2601.04819) · 평가 프로그램
- FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋) · Fan, Z. 외 (arXiv 2105.07147) · 평가 프로그램
- Nav2 Collision Monitor (nav2_collision_monitor) · Open Navigation (ros-navigation/navigation2) · 오픈소스
- ASAM OpenSCENARIO XML (1.4.0) · ASAM e.V. · 표준
- SDFormat (Simulation Description Format) · Open Source Robotics Foundation · 오픈소스
- BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) · Stanford 등 (Li, C. 외) · 평가 프로그램
- Moving AI MAPF 벤치마크 · Moving AI Lab (Sturtevant 외) · 평가 프로그램
- Arena-Bench · Kästner, L. 외 (RA-L 2022) · 평가 프로그램
- ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) · ISA(International Society of Automation) · 표준
- Open-RMF rmf_visualization · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) · Open Robotics (open-rmf) · 오픈소스
- IEC 62559 사용 사례 방법론 (Part 1~4) · IEC · 표준
- ISO/IEC/IEEE 29148:2018 요구공학 · ISO / IEC / IEEE · 표준
- 로봇활용 표준공정모델 · 산업통상자원부 · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) · OWASP GenAI Security Project · 프레임워크
- EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) · European Union (IES 해설 경유) · 프레임워크
- KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 · 과학기술정보통신부·한국인터넷진흥원(KISA) · 프레임워크
- 윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard) · Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) · 프레임워크
- VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) · VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) · 표준
- NASA-STD-7009B Standard for Models and Simulations · NASA · 표준
- 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) · 개인정보보호위원회 · 프레임워크
- 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) · 개인정보보호위원회 · 프레임워크
- 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) · 개인정보보호위원회 · 프레임워크
- 영상정보 원본 활용 규제샌드박스 실증특례 · 개인정보보호위원회 · 프레임워크
- EDPB Guidelines 3/2019 on processing of personal data through video devices · European Data Protection Board (EDPB) · 프레임워크
- EgoBlur · Meta Reality Labs · 오픈소스
- ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 · ANSI / A3(Association for Advancing Automation) · 표준
- HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications · UK Health and Safety Executive (HSE) · 프레임워크
- IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 · IEC(International Electrotechnical Commission) · 표준
- REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) · ROS (ros-infrastructure/rep) · 프레임워크
- HuNavSim (ROS 2 사람 보행 시뮬레이터) · Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. · 오픈소스
- Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) · Open Robotics · 오픈소스
- 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) · Francis, A. 외 · 프레임워크
- BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크) · BSRIA · 프레임워크
- 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 · 법제처(법령해석 법제처-23-0872 경유) · 프레임워크
- EU 데이터법 (Regulation (EU) 2023/2854, Data Act) · European Union (European Commission 해설) · 프레임워크
- EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안 · European Commission · 프레임워크
- 산업데이터 계약 가이드라인 · 산업통상부 · 프레임워크
- Kubernetes Deprecation Policy (API 폐기 정책) · The Kubernetes Authors · 오픈소스
- ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념 · ISO/IEC (JTC 1) · 표준
- IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항 · IEC · 표준
- EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무) · European Union (Future of Life Institute 비공식 게재본 경유) · 프레임워크
- 21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적) · U.S. Food and Drug Administration · 프레임워크
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
```

### runs/2026-10-09-05/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/simulator.md
about/what-is-rop.md
categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md
categories/ai-and-learning/document-drawing-and-scene-understanding.md
categories/ai-and-learning/index.md
categories/ai-and-learning/prediction-and-learning-based-optimization.md
categories/ai-and-learning/robot-foundation-models-and-llm-planning.md
categories/chat-based-configuration-and-operation/chat-map-authoring.md
categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md
categories/chat-based-configuration-and-operation/chat-robot-configuration.md
categories/chat-based-configuration-and-operation/chat-scenario-composition.md
categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md
categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md
categories/chat-based-configuration-and-operation/index.md
categories/design-and-simulation/capacity-sizing-and-layout-design.md
categories/design-and-simulation/index.md
categories/design-and-simulation/scenario-model-and-editing.md
categories/design-and-simulation/simulation-and-predictive-digital-twin.md
categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md
categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md
categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md
categories/execution-collaboration-and-recovery/human-robot-collaboration.md
categories/execution-collaboration-and-recovery/index.md
categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md
categories/field-operations-and-monitoring/control-screen-and-execution-records.md
categories/field-operations-and-monitoring/index.md
categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md
categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md
categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md
categories/governance-law-and-society/index.md
categories/governance-law-and-society/labor-acceptance-and-accessibility.md
categories/governance-law-and-society/law-regulation-insurance-and-licensing.md
categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md
categories/integration/business-system-integration.md
categories/integration/facility-and-building-system-integration.md
categories/integration/index.md
categories/integration/interoperability-standards-and-conformance.md
categories/integration/robot-and-vendor-fleet-manager-integration.md
categories/objects-people-and-live-state/index.md
categories/objects-people-and-live-state/people-and-pedestrian-model.md
categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md
categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md
categories/planning-and-business/economics-procurement-and-business-models.md
categories/planning-and-business/index.md
categories/planning-and-business/technology-market-and-vendor-trends.md
categories/planning-and-business/use-cases-requirements-and-scope.md
categories/planning-and-optimization/index.md
categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md
categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md
categories/planning-and-optimization/task-allocation-mrta.md
categories/planning-and-optimization/task-and-workflow-modeling.md
categories/planning-and-optimization/task-sequencing-and-scheduling.md
categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md
categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md
categories/platform-architecture-and-infrastructure/index.md
categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md
categories/robot-ontology/heterogeneous-robot-registration.md
categories/robot-ontology/index.md
categories/robot-ontology/ontology-based-system-and-robot-integration.md
categories/robot-ontology/ontology-verification-and-change-management.md
categories/robot-ontology/robot-capability-and-task-representation.md
categories/safety/human-proximity-safety.md
categories/safety/index.md
categories/safety/safety-and-risk-management.md
categories/safety/safety-standards-certification-and-incident-investigation.md
categories/security-and-privacy/authentication-authorization-and-isolation.md
categories/security-and-privacy/communication-protection-threat-management-and-audit.md
categories/security-and-privacy/index.md
categories/security-and-privacy/privacy-and-video-data.md
categories/site-type-applications/commercial-facilities.md
categories/site-type-applications/home-and-apartment.md
categories/site-type-applications/hospital-and-healthcare.md
categories/site-type-applications/index.md
categories/site-type-applications/manufacturing-plant.md
categories/site-type-applications/other-sites.md
categories/site-type-applications/outdoor.md
categories/site-type-applications/warehouse.md
categories/space-and-map-model/index.md
categories/space-and-map-model/map-space-and-location-model.md
categories/space-and-map-model/maps-from-floor-plans-and-bim.md
categories/space-and-map-model/place-semantics-and-map-management.md
categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md
categories/verification-deployment-and-lifecycle/index.md
categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md
categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md
categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md
changelog.md
corrections.md
glossary/3d-scene-graph.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/as-planned-vs-as-built-deviation.md
glossary/asam-openscenario.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/asyncapi-specification.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-description-submodel.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/cell-based-production.md
glossary/clarification-question.md
glossary/cloud-robotics.md
glossary/coalition-formation.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/common-coordinate-system.md
glossary/common-data-environment.md
glossary/compensating-transaction.md
glossary/competency-question.md
glossary/condition-based-maintenance.md
glossary/configuration-copilot.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/confused-deputy.md
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/control-barrier-function.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-embodiment-learning.md
glossary/cross-schedule-dependency.md
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
glossary/dds-security.md
glossary/deadlock.md
glossary/decision-focused-learning.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/document-layout-analysis.md
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/ethical-black-box.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explainable-mapf.md
glossary/explicit-implicit-confirmation.md
glossary/face-obfuscation.md
glossary/failure-explanation.md
glossary/falsification.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/finops.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/giai.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hardware-in-the-loop.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/hmi-philosophy.md
glossary/human-in-the-loop.md
glossary/human-motion-trajectory-prediction.md
glossary/hungarian-method.md
glossary/i-pass-handoff-program.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indirect-prompt-injection.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/irreducible-infeasible-subset.md
glossary/isa-95.md
glossary/it-ot-convergence.md
glossary/jailbreak.md
glossary/job-shop-scheduling-problem.md
glossary/joint-goal-accuracy.md
glossary/json-schema.md
glossary/keystroke-level-model.md
glossary/kiosk-accessibility.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pay-per-pick.md
glossary/payback-period.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/personal-delivery-device.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/pseudonymisation.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/raw-video-regulatory-sandbox-exemption.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-standard-process-model.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-ambiguity.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/security-level-iec-62443.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shift-handover.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/sim-vs-real-correlation-coefficient.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-awareness.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/slot-filling.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
glossary/software-in-the-loop.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/stakeholder-requirements-specification.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
glossary/zone-set.md
glossary/zones-and-conduits.md
ideas/chat-based-configuration-and-operation.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/daily/2026-09-26.md
logs/daily/2026-09-29.md
logs/daily/2026-09-30.md
logs/index.md
logs/weekly/2026-W39.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-046.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-1000.md
references/ref-1001.md
references/ref-1002.md
references/ref-1003.md
references/ref-1004.md
references/ref-1005.md
references/ref-1006.md
references/ref-1007.md
references/ref-1008.md
references/ref-1009.md
references/ref-101.md
references/ref-1010.md
references/ref-1011.md
references/ref-1012.md
references/ref-1013.md
references/ref-1014.md
references/ref-1015.md
references/ref-1016.md
references/ref-1017.md
references/ref-1018.md
references/ref-1019.md
references/ref-102.md
references/ref-1020.md
references/ref-1021.md
references/ref-1022.md
references/ref-1023.md
references/ref-1024.md
references/ref-1025.md
references/ref-1026.md
references/ref-1027.md
references/ref-1028.md
references/ref-1029.md
references/ref-103.md
references/ref-1030.md
references/ref-1031.md
references/ref-1032.md
references/ref-1033.md
references/ref-1034.md
references/ref-1035.md
references/ref-1036.md
references/ref-1037.md
references/ref-1038.md
references/ref-1039.md
references/ref-104.md
references/ref-1040.md
references/ref-1041.md
references/ref-1042.md
references/ref-1043.md
references/ref-1044.md
references/ref-1045.md
references/ref-1046.md
references/ref-1047.md
references/ref-1048.md
references/ref-1049.md
references/ref-105.md
references/ref-1050.md
references/ref-1051.md
references/ref-1052.md
references/ref-1053.md
references/ref-1054.md
references/ref-1055.md
references/ref-1056.md
references/ref-1057.md
references/ref-1058.md
references/ref-1059.md
references/ref-106.md
references/ref-1060.md
references/ref-1061.md
references/ref-1062.md
references/ref-1063.md
references/ref-1064.md
references/ref-1065.md
references/ref-1066.md
references/ref-1067.md
references/ref-1068.md
references/ref-1069.md
references/ref-107.md
references/ref-1070.md
references/ref-1071.md
references/ref-1072.md
references/ref-1073.md
references/ref-1074.md
references/ref-1075.md
references/ref-1076.md
references/ref-1077.md
references/ref-1078.md
references/ref-1079.md
references/ref-108.md
references/ref-1080.md
references/ref-1081.md
references/ref-1082.md
references/ref-1083.md
references/ref-1084.md
references/ref-1085.md
references/ref-1086.md
references/ref-1087.md
references/ref-1088.md
references/ref-1089.md
references/ref-109.md
references/ref-1090.md
references/ref-1091.md
references/ref-1092.md
references/ref-1093.md
references/ref-1094.md
references/ref-1095.md
references/ref-1096.md
references/ref-1097.md
references/ref-1098.md
references/ref-1099.md
references/ref-110.md
references/ref-1100.md
references/ref-1101.md
references/ref-1102.md
references/ref-1103.md
references/ref-1104.md
references/ref-1105.md
references/ref-1106.md
references/ref-1107.md
references/ref-1108.md
references/ref-1109.md
references/ref-111.md
references/ref-1110.md
references/ref-1111.md
references/ref-1112.md
references/ref-1113.md
references/ref-1114.md
references/ref-1115.md
references/ref-1116.md
references/ref-1117.md
references/ref-1118.md
references/ref-1119.md
references/ref-112.md
references/ref-1120.md
references/ref-1121.md
references/ref-1122.md
references/ref-1123.md
references/ref-1124.md
references/ref-1125.md
references/ref-1126.md
references/ref-1127.md
references/ref-1128.md
references/ref-1129.md
references/ref-113.md
references/ref-1130.md
references/ref-1131.md
references/ref-1132.md
references/ref-1133.md
references/ref-1134.md
references/ref-1135.md
references/ref-1136.md
references/ref-1137.md
references/ref-1138.md
references/ref-1139.md
references/ref-114.md
references/ref-1140.md
references/ref-1141.md
references/ref-1142.md
references/ref-1143.md
references/ref-1144.md
references/ref-1145.md
references/ref-1146.md
references/ref-1147.md
references/ref-1148.md
references/ref-1149.md
references/ref-115.md
references/ref-1150.md
references/ref-1151.md
references/ref-1152.md
references/ref-1153.md
references/ref-1154.md
references/ref-1155.md
references/ref-1156.md
references/ref-1157.md
references/ref-1158.md
references/ref-1159.md
references/ref-116.md
references/ref-1160.md
references/ref-1161.md
references/ref-1162.md
references/ref-1163.md
references/ref-1164.md
references/ref-1165.md
references/ref-1166.md
references/ref-1167.md
references/ref-1168.md
references/ref-1169.md
references/ref-117.md
references/ref-1170.md
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
references/ref-1195.md
references/ref-1196.md
references/ref-1197.md
references/ref-1198.md
references/ref-1199.md
references/ref-120.md
references/ref-1200.md
references/ref-1201.md
references/ref-1202.md
references/ref-1203.md
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
references/ref-437.md
references/ref-438.md
references/ref-439.md
references/ref-440.md
references/ref-441.md
references/ref-442.md
references/ref-443.md
references/ref-444.md
references/ref-445.md
references/ref-446.md
references/ref-447.md
references/ref-448.md
references/ref-449.md
references/ref-450.md
references/ref-451.md
references/ref-452.md
references/ref-453.md
references/ref-454.md
references/ref-455.md
references/ref-456.md
references/ref-457.md
references/ref-458.md
references/ref-459.md
references/ref-460.md
references/ref-461.md
references/ref-462.md
references/ref-463.md
references/ref-464.md
references/ref-465.md
references/ref-466.md
references/ref-467.md
references/ref-468.md
references/ref-469.md
references/ref-470.md
references/ref-471.md
references/ref-472.md
references/ref-473.md
references/ref-474.md
references/ref-475.md
references/ref-476.md
references/ref-477.md
references/ref-478.md
references/ref-479.md
references/ref-480.md
references/ref-481.md
references/ref-482.md
references/ref-483.md
references/ref-484.md
references/ref-485.md
references/ref-486.md
references/ref-487.md
references/ref-488.md
references/ref-489.md
references/ref-490.md
references/ref-491.md
references/ref-492.md
references/ref-493.md
references/ref-494.md
references/ref-495.md
references/ref-496.md
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-500.md
references/ref-501.md
references/ref-502.md
references/ref-503.md
references/ref-504.md
references/ref-505.md
references/ref-506.md
references/ref-507.md
references/ref-508.md
references/ref-509.md
references/ref-510.md
references/ref-511.md
references/ref-512.md
references/ref-513.md
references/ref-514.md
references/ref-515.md
references/ref-516.md
references/ref-517.md
references/ref-518.md
references/ref-519.md
references/ref-520.md
references/ref-521.md
references/ref-522.md
references/ref-523.md
references/ref-524.md
references/ref-525.md
references/ref-526.md
references/ref-527.md
references/ref-528.md
references/ref-529.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
references/ref-539.md
references/ref-540.md
references/ref-541.md
references/ref-542.md
references/ref-543.md
references/ref-544.md
references/ref-545.md
references/ref-546.md
references/ref-547.md
references/ref-548.md
references/ref-549.md
references/ref-550.md
references/ref-551.md
references/ref-552.md
references/ref-553.md
references/ref-554.md
references/ref-555.md
references/ref-556.md
references/ref-557.md
references/ref-558.md
references/ref-559.md
references/ref-560.md
references/ref-561.md
references/ref-562.md
references/ref-563.md
references/ref-564.md
references/ref-565.md
references/ref-566.md
references/ref-567.md
references/ref-568.md
references/ref-569.md
references/ref-570.md
references/ref-571.md
references/ref-572.md
references/ref-573.md
references/ref-574.md
references/ref-575.md
references/ref-576.md
references/ref-577.md
references/ref-578.md
references/ref-579.md
references/ref-580.md
references/ref-581.md
references/ref-582.md
references/ref-583.md
references/ref-584.md
references/ref-585.md
references/ref-586.md
references/ref-587.md
references/ref-588.md
references/ref-589.md
references/ref-590.md
references/ref-591.md
references/ref-592.md
references/ref-593.md
references/ref-594.md
references/ref-595.md
references/ref-596.md
references/ref-597.md
references/ref-598.md
references/ref-599.md
references/ref-600.md
references/ref-601.md
references/ref-602.md
references/ref-603.md
references/ref-604.md
references/ref-605.md
references/ref-606.md
references/ref-607.md
references/ref-608.md
references/ref-609.md
references/ref-610.md
references/ref-611.md
references/ref-612.md
references/ref-613.md
references/ref-614.md
references/ref-615.md
references/ref-616.md
references/ref-617.md
references/ref-618.md
references/ref-619.md
references/ref-620.md
references/ref-621.md
references/ref-622.md
references/ref-623.md
references/ref-624.md
references/ref-625.md
references/ref-626.md
references/ref-627.md
references/ref-628.md
references/ref-629.md
references/ref-630.md
references/ref-631.md
references/ref-632.md
references/ref-633.md
references/ref-634.md
references/ref-635.md
references/ref-636.md
references/ref-637.md
references/ref-638.md
references/ref-639.md
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
references/ref-644.md
references/ref-645.md
references/ref-646.md
references/ref-647.md
references/ref-648.md
references/ref-649.md
references/ref-650.md
references/ref-651.md
references/ref-652.md
references/ref-653.md
references/ref-654.md
references/ref-655.md
references/ref-656.md
references/ref-657.md
references/ref-658.md
references/ref-659.md
references/ref-660.md
references/ref-661.md
references/ref-662.md
references/ref-663.md
references/ref-664.md
references/ref-665.md
references/ref-666.md
references/ref-667.md
references/ref-668.md
references/ref-669.md
references/ref-670.md
references/ref-671.md
references/ref-672.md
references/ref-673.md
references/ref-674.md
references/ref-675.md
references/ref-676.md
references/ref-677.md
references/ref-678.md
references/ref-679.md
references/ref-680.md
references/ref-681.md
references/ref-682.md
references/ref-683.md
references/ref-684.md
references/ref-685.md
references/ref-686.md
references/ref-687.md
references/ref-688.md
references/ref-689.md
references/ref-690.md
references/ref-691.md
references/ref-692.md
references/ref-693.md
references/ref-694.md
references/ref-695.md
references/ref-696.md
references/ref-697.md
references/ref-698.md
references/ref-699.md
references/ref-700.md
references/ref-701.md
references/ref-702.md
references/ref-703.md
references/ref-704.md
references/ref-705.md
references/ref-706.md
references/ref-707.md
references/ref-708.md
references/ref-709.md
references/ref-710.md
references/ref-711.md
references/ref-712.md
references/ref-713.md
references/ref-714.md
references/ref-715.md
references/ref-716.md
references/ref-717.md
references/ref-718.md
references/ref-719.md
references/ref-720.md
references/ref-721.md
references/ref-722.md
references/ref-723.md
references/ref-724.md
references/ref-725.md
references/ref-726.md
references/ref-727.md
references/ref-728.md
references/ref-729.md
references/ref-730.md
references/ref-731.md
references/ref-732.md
references/ref-733.md
references/ref-734.md
references/ref-735.md
references/ref-736.md
references/ref-737.md
references/ref-738.md
references/ref-739.md
references/ref-740.md
references/ref-741.md
references/ref-742.md
references/ref-743.md
references/ref-744.md
references/ref-745.md
references/ref-746.md
references/ref-747.md
references/ref-748.md
references/ref-749.md
references/ref-750.md
references/ref-751.md
references/ref-752.md
references/ref-753.md
references/ref-754.md
references/ref-755.md
references/ref-756.md
references/ref-757.md
references/ref-758.md
references/ref-759.md
references/ref-760.md
references/ref-761.md
references/ref-762.md
references/ref-763.md
references/ref-764.md
references/ref-765.md
references/ref-766.md
references/ref-767.md
references/ref-768.md
references/ref-769.md
references/ref-770.md
references/ref-771.md
references/ref-772.md
references/ref-773.md
references/ref-774.md
references/ref-775.md
references/ref-776.md
references/ref-777.md
references/ref-778.md
references/ref-779.md
references/ref-780.md
references/ref-781.md
references/ref-782.md
references/ref-783.md
references/ref-784.md
references/ref-785.md
references/ref-786.md
references/ref-787.md
references/ref-788.md
references/ref-789.md
references/ref-790.md
references/ref-791.md
references/ref-792.md
references/ref-793.md
references/ref-794.md
references/ref-795.md
references/ref-796.md
references/ref-797.md
references/ref-798.md
references/ref-799.md
references/ref-800.md
references/ref-801.md
references/ref-802.md
references/ref-803.md
references/ref-804.md
references/ref-805.md
references/ref-806.md
references/ref-807.md
references/ref-808.md
references/ref-809.md
references/ref-810.md
references/ref-811.md
references/ref-812.md
references/ref-813.md
references/ref-814.md
references/ref-815.md
references/ref-816.md
references/ref-817.md
references/ref-818.md
references/ref-819.md
references/ref-820.md
references/ref-821.md
references/ref-822.md
references/ref-823.md
references/ref-824.md
references/ref-825.md
references/ref-826.md
references/ref-827.md
references/ref-828.md
references/ref-829.md
references/ref-830.md
references/ref-831.md
references/ref-832.md
references/ref-833.md
references/ref-834.md
references/ref-835.md
references/ref-836.md
references/ref-837.md
references/ref-838.md
references/ref-839.md
references/ref-840.md
references/ref-841.md
references/ref-842.md
references/ref-843.md
references/ref-844.md
references/ref-845.md
references/ref-846.md
references/ref-847.md
references/ref-848.md
references/ref-849.md
references/ref-850.md
references/ref-851.md
references/ref-852.md
references/ref-853.md
references/ref-854.md
references/ref-855.md
references/ref-856.md
references/ref-857.md
references/ref-858.md
references/ref-859.md
references/ref-860.md
references/ref-861.md
references/ref-862.md
references/ref-863.md
references/ref-864.md
references/ref-865.md
references/ref-866.md
references/ref-867.md
references/ref-868.md
references/ref-869.md
references/ref-870.md
references/ref-871.md
references/ref-872.md
references/ref-873.md
references/ref-874.md
references/ref-875.md
references/ref-876.md
references/ref-877.md
references/ref-878.md
references/ref-879.md
references/ref-880.md
references/ref-881.md
references/ref-882.md
references/ref-883.md
references/ref-884.md
references/ref-885.md
references/ref-886.md
references/ref-887.md
references/ref-888.md
references/ref-889.md
references/ref-890.md
references/ref-891.md
references/ref-892.md
references/ref-893.md
references/ref-894.md
references/ref-895.md
references/ref-896.md
references/ref-897.md
references/ref-898.md
references/ref-899.md
references/ref-900.md
references/ref-901.md
references/ref-902.md
references/ref-903.md
references/ref-904.md
references/ref-905.md
references/ref-906.md
references/ref-907.md
references/ref-908.md
references/ref-909.md
references/ref-910.md
references/ref-911.md
references/ref-912.md
references/ref-913.md
references/ref-914.md
references/ref-915.md
references/ref-916.md
references/ref-917.md
references/ref-918.md
references/ref-919.md
references/ref-920.md
references/ref-921.md
references/ref-922.md
references/ref-923.md
references/ref-924.md
references/ref-925.md
references/ref-926.md
references/ref-927.md
references/ref-928.md
references/ref-929.md
references/ref-930.md
references/ref-931.md
references/ref-932.md
references/ref-933.md
references/ref-934.md
references/ref-935.md
references/ref-936.md
references/ref-937.md
references/ref-938.md
references/ref-939.md
references/ref-940.md
references/ref-941.md
references/ref-942.md
references/ref-943.md
references/ref-944.md
references/ref-945.md
references/ref-946.md
references/ref-947.md
references/ref-948.md
references/ref-949.md
references/ref-950.md
references/ref-951.md
references/ref-952.md
references/ref-953.md
references/ref-954.md
references/ref-955.md
references/ref-956.md
references/ref-957.md
references/ref-958.md
references/ref-959.md
references/ref-960.md
references/ref-961.md
references/ref-962.md
references/ref-963.md
references/ref-964.md
references/ref-965.md
references/ref-966.md
references/ref-967.md
references/ref-968.md
references/ref-969.md
references/ref-970.md
references/ref-971.md
references/ref-972.md
references/ref-973.md
references/ref-974.md
references/ref-975.md
references/ref-976.md
references/ref-977.md
references/ref-978.md
references/ref-979.md
references/ref-980.md
references/ref-981.md
references/ref-982.md
references/ref-983.md
references/ref-984.md
references/ref-985.md
references/ref-986.md
references/ref-987.md
references/ref-988.md
references/ref-989.md
references/ref-990.md
references/ref-991.md
references/ref-992.md
references/ref-993.md
references/ref-994.md
references/ref-995.md
references/ref-996.md
references/ref-997.md
references/ref-998.md
references/ref-999.md
site-matrix.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
topics/2026/2026-09-25-area18-s4.md
topics/2026/2026-09-25-area18-s6.md
topics/2026/2026-09-25-area18-s7.md
topics/2026/2026-09-25-area18-s8.md
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area20-s10.md
topics/2026/2026-09-25-area20-s11.md
topics/2026/2026-09-25-area20-s4.md
topics/2026/2026-09-25-area20-s6.md
topics/2026/2026-09-25-area20-s7.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
topics/2026/2026-09-25-area22-s10.md
topics/2026/2026-09-25-area22-s4.md
topics/2026/2026-09-25-area22-s6.md
topics/2026/2026-09-25-area22-s7.md
topics/2026/2026-09-25-area22-s8.md
topics/2026/2026-09-25-area23-s10.md
topics/2026/2026-09-25-area23-s11.md
topics/2026/2026-09-25-area23-s4.md
topics/2026/2026-09-25-area23-s6.md
topics/2026/2026-09-25-area23-s7.md
topics/2026/2026-09-25-area24-s10.md
topics/2026/2026-09-25-area24-s3.md
topics/2026/2026-09-25-area24-s4.md
topics/2026/2026-09-25-area24-s6.md
topics/2026/2026-09-25-area24-s7.md
topics/2026/2026-09-25-area25-s11.md
topics/2026/2026-09-25-area25-s3.md
topics/2026/2026-09-25-area25-s6.md
topics/2026/2026-09-25-area25-s7.md
topics/2026/2026-09-25-area25-s8.md
topics/2026/2026-09-25-area26-s10.md
topics/2026/2026-09-25-area26-s11.md
topics/2026/2026-09-25-area26-s3.md
topics/2026/2026-09-25-area26-s4.md
topics/2026/2026-09-25-area26-s6.md
topics/2026/2026-09-25-area26-s7.md
topics/2026/2026-09-25-area26-s8.md
topics/2026/2026-09-25-area27-s10.md
topics/2026/2026-09-25-area27-s4.md
topics/2026/2026-09-25-area27-s6.md
topics/2026/2026-09-25-area27-s7.md
topics/2026/2026-09-25-area27-s8.md
topics/2026/2026-09-25-area28-s11.md
topics/2026/2026-09-25-area28-s3.md
topics/2026/2026-09-25-area28-s4.md
topics/2026/2026-09-25-area28-s6.md
topics/2026/2026-09-25-area28-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/2026/2026-09-26-area04-s10.md
topics/2026/2026-09-26-area25-s7.md
topics/2026/2026-09-29-area01-s10.md
topics/2026/2026-09-29-area01-s11.md
topics/2026/2026-09-29-area01-s3.md
topics/2026/2026-09-29-area01-s4.md
topics/2026/2026-09-29-area01-s6.md
topics/2026/2026-09-29-area01-s7.md
topics/2026/2026-09-29-area01-s8.md
topics/2026/2026-09-29-area04-s10.md
topics/2026/2026-09-29-area04-s11.md
topics/2026/2026-09-29-area04-s3.md
topics/2026/2026-09-29-area04-s4.md
topics/2026/2026-09-29-area04-s6.md
topics/2026/2026-09-29-area04-s7.md
topics/2026/2026-09-29-area04-s8.md
topics/2026/2026-09-29-area06-s10.md
topics/2026/2026-09-29-area06-s11.md
topics/2026/2026-09-29-area06-s3.md
topics/2026/2026-09-29-area06-s4.md
topics/2026/2026-09-29-area06-s6.md
topics/2026/2026-09-29-area06-s7.md
topics/2026/2026-09-29-area06-s8.md
topics/2026/2026-09-29-area07-s10.md
topics/2026/2026-09-29-area07-s11.md
topics/2026/2026-09-29-area07-s3.md
topics/2026/2026-09-29-area07-s4.md
topics/2026/2026-09-29-area07-s6.md
topics/2026/2026-09-29-area07-s7.md
topics/2026/2026-09-29-area07-s8.md
topics/2026/2026-09-29-area08-s10.md
topics/2026/2026-09-29-area08-s11.md
topics/2026/2026-09-29-area08-s3.md
topics/2026/2026-09-29-area08-s4.md
topics/2026/2026-09-29-area08-s6.md
topics/2026/2026-09-29-area08-s7.md
topics/2026/2026-09-29-area08-s8.md
topics/2026/2026-09-29-area09-s10.md
topics/2026/2026-09-29-area09-s11.md
topics/2026/2026-09-29-area09-s3.md
topics/2026/2026-09-29-area09-s4.md
topics/2026/2026-09-29-area09-s6.md
topics/2026/2026-09-29-area09-s7.md
topics/2026/2026-09-29-area09-s8.md
topics/2026/2026-09-29-area10-s10.md
topics/2026/2026-09-29-area10-s11.md
topics/2026/2026-09-29-area10-s3.md
topics/2026/2026-09-29-area10-s4.md
topics/2026/2026-09-29-area10-s6.md
topics/2026/2026-09-29-area10-s7.md
topics/2026/2026-09-29-area10-s8.md
topics/2026/2026-09-29-area11-s10.md
topics/2026/2026-09-29-area11-s11.md
topics/2026/2026-09-29-area11-s3.md
topics/2026/2026-09-29-area11-s4.md
topics/2026/2026-09-29-area11-s6.md
topics/2026/2026-09-29-area11-s7.md
topics/2026/2026-09-29-area11-s8.md
topics/2026/2026-09-29-area12-s10.md
topics/2026/2026-09-29-area12-s11.md
topics/2026/2026-09-29-area12-s3.md
topics/2026/2026-09-29-area12-s4.md
topics/2026/2026-09-29-area12-s6.md
topics/2026/2026-09-29-area12-s7.md
topics/2026/2026-09-29-area12-s8.md
topics/2026/2026-09-29-area13-s10.md
topics/2026/2026-09-29-area13-s11.md
topics/2026/2026-09-29-area13-s3.md
topics/2026/2026-09-29-area13-s4.md
topics/2026/2026-09-29-area13-s6.md
topics/2026/2026-09-29-area13-s7.md
topics/2026/2026-09-29-area13-s8.md
topics/2026/2026-09-29-area61-s10.md
topics/2026/2026-09-29-area61-s11.md
topics/2026/2026-09-29-area61-s3.md
topics/2026/2026-09-29-area61-s4.md
topics/2026/2026-09-29-area61-s6.md
topics/2026/2026-09-29-area61-s7.md
topics/2026/2026-09-29-area61-s8.md
topics/2026/2026-09-29-area62-s10.md
topics/2026/2026-09-29-area62-s11.md
topics/2026/2026-09-29-area62-s3.md
topics/2026/2026-09-29-area62-s4.md
topics/2026/2026-09-29-area62-s6.md
topics/2026/2026-09-29-area62-s7.md
topics/2026/2026-09-29-area62-s8.md
topics/2026/2026-09-29-area63-s10.md
topics/2026/2026-09-29-area63-s11.md
topics/2026/2026-09-29-area63-s3.md
topics/2026/2026-09-29-area63-s4.md
topics/2026/2026-09-29-area63-s6.md
topics/2026/2026-09-29-area63-s7.md
topics/2026/2026-09-29-area63-s8.md
topics/2026/2026-09-29-area64-s10.md
topics/2026/2026-09-29-area64-s11.md
topics/2026/2026-09-29-area64-s3.md
topics/2026/2026-09-29-area64-s4.md
topics/2026/2026-09-29-area64-s6.md
topics/2026/2026-09-29-area64-s7.md
topics/2026/2026-09-29-area64-s8.md
topics/2026/2026-09-29-area65-s10.md
topics/2026/2026-09-29-area65-s11.md
topics/2026/2026-09-29-area65-s3.md
topics/2026/2026-09-29-area65-s4.md
topics/2026/2026-09-29-area65-s6.md
topics/2026/2026-09-29-area65-s7.md
topics/2026/2026-09-29-area65-s8.md
topics/2026/2026-09-30-area02-s10.md
topics/2026/2026-09-30-area02-s11.md
topics/2026/2026-09-30-area02-s3.md
topics/2026/2026-09-30-area02-s4.md
topics/2026/2026-09-30-area02-s6.md
topics/2026/2026-09-30-area02-s7.md
topics/2026/2026-09-30-area02-s8.md
topics/2026/2026-09-30-area03-s10.md
topics/2026/2026-09-30-area03-s11.md
topics/2026/2026-09-30-area03-s3.md
topics/2026/2026-09-30-area03-s4.md
topics/2026/2026-09-30-area03-s6.md
topics/2026/2026-09-30-area03-s7.md
topics/2026/2026-09-30-area03-s8.md
topics/2026/2026-09-30-area14-s10.md
topics/2026/2026-09-30-area14-s11.md
topics/2026/2026-09-30-area14-s3.md
topics/2026/2026-09-30-area14-s4.md
topics/2026/2026-09-30-area14-s6.md
topics/2026/2026-09-30-area14-s8.md
topics/2026/2026-09-30-area16-s10.md
topics/2026/2026-09-30-area16-s11.md
topics/2026/2026-09-30-area16-s4.md
topics/2026/2026-09-30-area16-s6.md
topics/2026/2026-09-30-area16-s7.md
topics/2026/2026-09-30-area16-s8.md
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
topics/2026/2026-09-30-area36-s10.md
topics/2026/2026-09-30-area36-s11.md
topics/2026/2026-09-30-area36-s3.md
topics/2026/2026-09-30-area36-s4.md
topics/2026/2026-09-30-area36-s6.md
topics/2026/2026-09-30-area36-s7.md
topics/2026/2026-09-30-area36-s8.md
topics/2026/2026-09-30-area37-s10.md
topics/2026/2026-09-30-area37-s4.md
topics/2026/2026-09-30-area37-s6.md
topics/2026/2026-09-30-area37-s8.md
topics/2026/2026-09-30-area40-s10.md
topics/2026/2026-09-30-area40-s11.md
topics/2026/2026-09-30-area40-s3.md
topics/2026/2026-09-30-area40-s4.md
topics/2026/2026-09-30-area40-s6.md
topics/2026/2026-09-30-area40-s7.md
topics/2026/2026-09-30-area40-s8.md
topics/2026/2026-09-30-area41-s10.md
topics/2026/2026-09-30-area41-s11.md
topics/2026/2026-09-30-area41-s3.md
topics/2026/2026-09-30-area41-s4.md
topics/2026/2026-09-30-area41-s6.md
topics/2026/2026-09-30-area41-s7.md
topics/2026/2026-09-30-area41-s8.md
topics/2026/2026-09-30-area43-s10.md
topics/2026/2026-09-30-area43-s11.md
topics/2026/2026-09-30-area43-s3.md
topics/2026/2026-09-30-area43-s4.md
topics/2026/2026-09-30-area43-s6.md
topics/2026/2026-09-30-area43-s7.md
topics/2026/2026-09-30-area44-s10.md
topics/2026/2026-09-30-area44-s11.md
topics/2026/2026-09-30-area44-s3.md
topics/2026/2026-09-30-area44-s4.md
topics/2026/2026-09-30-area44-s6.md
topics/2026/2026-09-30-area44-s7.md
topics/2026/2026-09-30-area44-s8.md
topics/2026/2026-09-30-area45-s10.md
topics/2026/2026-09-30-area45-s11.md
topics/2026/2026-09-30-area45-s3.md
topics/2026/2026-09-30-area45-s4.md
topics/2026/2026-09-30-area45-s6.md
topics/2026/2026-09-30-area45-s7.md
topics/2026/2026-09-30-area45-s8.md
topics/2026/2026-09-30-area46-s10.md
topics/2026/2026-09-30-area46-s11.md
topics/2026/2026-09-30-area46-s3.md
topics/2026/2026-09-30-area46-s4.md
topics/2026/2026-09-30-area46-s6.md
topics/2026/2026-09-30-area46-s7.md
topics/2026/2026-09-30-area46-s8.md
topics/2026/2026-09-30-area49-s10.md
topics/2026/2026-09-30-area49-s11.md
topics/2026/2026-09-30-area49-s3.md
topics/2026/2026-09-30-area49-s4.md
topics/2026/2026-09-30-area49-s6.md
topics/2026/2026-09-30-area49-s7.md
topics/2026/2026-09-30-area49-s8.md
topics/2026/2026-09-30-area50-s10.md
topics/2026/2026-09-30-area50-s11.md
topics/2026/2026-09-30-area50-s3.md
topics/2026/2026-09-30-area50-s4.md
topics/2026/2026-09-30-area50-s6.md
topics/2026/2026-09-30-area50-s7.md
topics/2026/2026-09-30-area50-s8.md
topics/2026/2026-09-30-area52-s10.md
topics/2026/2026-09-30-area52-s11.md
topics/2026/2026-09-30-area52-s3.md
topics/2026/2026-09-30-area52-s4.md
topics/2026/2026-09-30-area52-s6.md
topics/2026/2026-09-30-area52-s8.md
topics/2026/2026-09-30-area53-s10.md
topics/2026/2026-09-30-area53-s11.md
topics/2026/2026-09-30-area53-s3.md
topics/2026/2026-09-30-area53-s4.md
topics/2026/2026-09-30-area53-s6.md
topics/2026/2026-09-30-area53-s7.md
topics/2026/2026-09-30-area53-s8.md
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
topics/2026/2026-09-30-area67-s10.md
topics/2026/2026-09-30-area67-s11.md
topics/2026/2026-09-30-area67-s3.md
topics/2026/2026-09-30-area67-s4.md
topics/2026/2026-09-30-area67-s6.md
topics/2026/2026-09-30-area67-s7.md
topics/2026/2026-09-30-area67-s8.md
topics/index.md
tracks/chat-based-configuration-and-operation/experiments.md
tracks/chat-based-configuration-and-operation/index.md
tracks/chat-based-configuration-and-operation/log.md
tracks/chat-based-configuration-and-operation/question-backlog.md
tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md
tracks/chat-based-configuration-and-operation/stage-10-integrated-verification.md
tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md
tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md
tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md
tracks/chat-based-configuration-and-operation/stage-6-chat-map-authoring.md
tracks/chat-based-configuration-and-operation/stage-7-chat-scenario-composition.md
tracks/chat-based-configuration-and-operation/stage-8-chat-robot-configuration.md
tracks/chat-based-configuration-and-operation/stage-9-chat-real-situation-replay.md
tracks/chat-based-configuration-and-operation/task-model-draft.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
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

### runs/2026-10-09-05/pages.json

```json
{
  "run_id": "2026-10-09-05",
  "outline": [
    {
      "path": "docs/categories/field-operations-and-monitoring/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 9000,
      "summary": "J. 현장 운영·관제의 네 세부영역은 D·E·F에서 지도·현재 상태·제조사 신호를 받아 보여 주고, 판정·경보·지표를 G·H·I·K·L·M·N·P로 넘긴다. Open-RMF 상태·경보 스키마가 연결의 주된 근거다. [사실][^ref-148][^ref-448] B. 로봇 온톨로지와의 연결 근거는 없다.",
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
        "f10",
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
        "f22",
        "f23",
        "f24",
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
        "f35",
        "f36",
        "f37",
        "f38",
        "f39",
        "f40",
        "f41",
        "f42",
        "f43"
      ]
    },
    {
      "path": "docs/categories/field-operations-and-monitoring/index.md",
      "section": "참고 자료",
      "budget_chars": 100,
      "summary": "이 대분류의 핵심 포인트 원문 문단에는 [n] 표기가 없어 원문 각주가 없다. '다른 대분류와의 연결'의 각주 정의는 그 절 끝에 둔다.",
      "planned_findings": []
    }
  ],
  "pages": [
    {
      "path": "docs/categories/field-operations-and-monitoring/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 신규 작성: 15개 대분류와의 연결(요약 표 + 대분류별 근거), B. 로봇 온톨로지와 근거 없는 세부영역을 '아직 다루지 않은 연결'로 명시, 절 끝에 각주 정의 47건. 형식 검증에 따라 템플릿의 마지막 절 '참고 자료'(원문 각주 없음)를 더함",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-031",
              "ref-051",
              "ref-096",
              "ref-102",
              "ref-111",
              "ref-125",
              "ref-139",
              "ref-140",
              "ref-145",
              "ref-146",
              "ref-148",
              "ref-230",
              "ref-283",
              "ref-302",
              "ref-313",
              "ref-447",
              "ref-448",
              "ref-449",
              "ref-453",
              "ref-494",
              "ref-569",
              "ref-762",
              "ref-781",
              "ref-782",
              "ref-944",
              "ref-1093",
              "ref-1094",
              "ref-1096",
              "ref-1098",
              "ref-1099",
              "ref-1103",
              "ref-1150",
              "ref-1151",
              "ref-1152",
              "ref-1153",
              "ref-1154",
              "ref-1157",
              "ref-1199",
              "ref-1236",
              "ref-1272",
              "ref-1278",
              "ref-1359",
              "ref-1360",
              "ref-1361",
              "ref-1362",
              "ref-1363",
              "ref-1364"
            ]
          },
          "content": "J. 현장 운영·관제의 네 세부영역은 다른 대분류가 만든 지도·상태·계획·기록을 받아 운영자에게 보여 주고, 판정·경보·지표를 다시 다른 대분류로 넘긴다. 아래 연결은 게시된 세부영역 페이지(37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구)와 2026-10-09 조사·검증을 거친 주장에 기댄다. 대부분 단일 출처이거나 세부영역 페이지의 판단을 다시 인용한 것이므로, 두 영역이 이어진다고 해석한 문장은 추정 표기로 남겼다.\n\n### 한눈에 보기\n\n| 다른 대분류 | J. 현장 운영·관제 쪽 세부영역 | 상대 세부영역 |\n|---|---|---|\n| A. 기획·사업 | 39. 운영 성과 측정·개선 | 3. 경제성·조달·사업 모델 |\n| B. 로봇 온톨로지 | 근거 없음 | 아래 '아직 다루지 않은 연결' |\n| C. 채팅 기반 구성·운영 | 37. 관제 화면·실행 기록 | 11. 채팅으로 실제 상황 시뮬레이션 재현, 12. 채팅으로 업무 지시·오케스트레이션 |\n| D. 공간·지도 모델 | 37. 관제 화면·실행 기록, 40. 운영 절차·요청 창구 | 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리 |\n| E. 사물·사람·실시간 상태 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선 | 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성 |\n| F. 연동 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동 |\n| G. 계획·최적화 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 27. 다중 로봇 경로·교통 관리 — MAPF, 28. 공용 자원·충전·에너지 최적화 |\n| H. 실행·협업·예외 복구 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 29. 명령·작업 실행의 신뢰성, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성 |\n| I. 설계·시뮬레이션 | 37. 관제 화면·실행 기록, 39. 운영 성과 측정·개선 | 35. 처리능력·규모·배치 설계, 36. 가상 시운전·실제 상황 재현 |\n| K. 플랫폼 아키텍처·인프라 | 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 43. 데이터·관측성·배포 |\n| L. AI·학습 기술 | 38. 모니터링·이상 탐지·원인 분석 | 47. AI·학습·적응과 모델 운영 |\n| M. 안전 | 37. 관제 화면·실행 기록, 40. 운영 절차·요청 창구 | 50. 안전 표준·인증·사고 조사 |\n| N. 보안·개인정보 | 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터 |\n| O. 검증·도입·수명주기 | 40. 운영 절차·요청 창구 | 56. 운영 이관·확대·교육 |\n| P. 거버넌스·법규·사회 | 37. 관제 화면·실행 기록, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 59. 법·규제·보험·라이선스, 60. 노동·수용성·접근성 |\n| Q. 현장 유형별 적용 | 37. 관제 화면·실행 기록, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구 | 61. 물류창고, 62. 제조 공장, 63. 병원·의료, 64. 상업 시설 |\n\n### [A. 기획·사업](../planning-and-business/index.md)\n\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md): 39. 운영 성과 측정·개선 페이지는 투자 수익률·순현재가치·회수 기간 같은 재무 평가를 연계 대상으로 두고 ROP는 그 입력인 처리량·가동률·충전·예외 실행 데이터를 제공한다고 보므로, 운영 지표가 투자 효과 판단으로 넘어가는 지점에서 두 영역이 이어지는 것으로 보인다. [추정][^ref-148] 그 계량 데이터를 누가 재고 어떻게 합의하는지는 열린 질문 oq-268 로 남아 있다.\n\n### [B. 로봇 온톨로지](../robot-ontology/index.md)\n\n게시된 페이지에서 B. 로봇 온톨로지와 J. 현장 운영·관제를 잇는 검증된 근거를 찾지 못했다. 아래 '아직 다루지 않은 연결'에 적었다.\n\n### [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md): 11. 채팅으로 실제 상황 시뮬레이션 재현은 재현 결과를 실제 기록의 시각·위치·사건 순서와 비교해야 하며, 그 실제 기록은 37. 관제 화면·실행 기록이 정규화해 저장하는 실행 기록에서 나올 것으로 보인다. [추정][^ref-1094][^ref-1096] 이 대화 기능이 부르는 엔진은 36. 가상 시운전·실제 상황 재현이므로 아래 I. 설계·시뮬레이션 항목과 함께 읽는다.\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md): 12. 채팅으로 업무 지시·오케스트레이션이 진행 상황 질의에 실행 기록과 시각을 근거로 답할 때, Open-RMF 작업 상태 스키마의 상태 값, 시작·종료 시각, 단계 목록, 취소·강제 종료 기록이 그 답의 근거 자료가 될 것으로 보인다. [추정][^ref-111] 업무 지시가 부르는 엔진은 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링이다.\n\n### [D. 공간·지도 모델](../space-and-map-model/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md): Open-RMF rmf_visualization 은 층 평면도 위에 로봇 위치, 문·승강기, 주행 그래프, 예측 궤적을 겹쳐 표시한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1093]\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md): Open-RMF 차선 요청(LaneRequest)이 플릿 이름과 열고 닫을 차선 목록 세 필드만 두므로, 임시 통제 구역을 누가 왜 언제까지 닫았는지는 40. 운영 절차·요청 창구의 운영 기록이, 차선·구역 반영은 16. 장소 의미·지도 관리가 맡는 접점이 될 것으로 보인다. [추정][^ref-569] 통제 구역의 선언·해제 절차를 공개한 현장 사례는 열린 질문 oq-203 으로 남아 있다([차선 폐쇄](../../glossary/lane-closure.md) 참고).\n\n### [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)\n\n이 대분류와의 연결은 지금의 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이다. 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽 연결은 섞지 않고 아래 I. 설계·시뮬레이션 항목에 따로 둔다.\n\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): Open-RMF 로봇 상태가 상태 값·문제 목록과 함께 기록 시각을 담으므로, 지연 원인 구분은 18. 실시간 세계 상태·데이터 일관성이 시각과 함께 유지하는 로봇·문·작업의 현재 상태를 같은 시간축에 맞춘 데이터를 쓸 것으로 보인다. [추정][^ref-148][^ref-051][^ref-313]\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): Open-RMF 로봇 상태 스키마는 상태 값 7개(uninitialized·offline·shutdown·idle·charging·working·error), 0~1 범위의 배터리, 현재 작업 id, 문제 목록, 기록 시각을 담는다(2026-10-09 확인). [사실][^ref-148] 이 값이 가동률·충전·오류 시간 지표의 원천이 될 것으로 보인다. [추정][^ref-148] 같은 해석이 [A. 기획·사업의 '다른 대분류와의 연결'](../planning-and-business/index.md#다른-대분류와의-연결)에도 같은 각주로 실려 있다.\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)(병원): 현대차·기아와 한림대학교의료원이 안면 인식 기반 수령 인증과 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 한 협약 보도(2025-04-07, 운영 결과 미확인)를 보면, 병원의 완료·인계 단계에서 수령인 확인과 배송 이력 기록이 한 기록으로 묶일 것으로 보인다. [추정][^ref-1103]\n\n### [F. 연동](../integration/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 3.0.0 은 차량 위치·계획 경로를 시각화 시스템에 보내는 visualization 토픽을 상태(state) 토픽과 따로 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031]\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 의 오류 수준과 연결 상태(CONNECTION_BROKEN), MassRobotics 의 외부 사건 대기(waitingExternalEvent), Open-RMF 의 작업 지연·차단은 서로 다른 어휘로 보고되므로, 20. 로봇·제조사 관제 연동에서 들어온 신호를 ROP 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. [추정][^ref-051][^ref-449][^ref-230][^ref-111] 공통 매핑 표준은 확인되지 않았고 열린 질문 oq-033·oq-073 으로 남아 있다.\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 문 모드는 closed·moving·open·offline·unknown 다섯 값이고, 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다(2026-10-09 확인). [사실][^ref-313][^ref-283] 문 개폐 제어 자체는 시설·설비 제어 경계의 연계 대상이며, 이 연결에서 ROP 몫은 문 상태 확인과 작업 요청으로 한정된다.\n- 연계 대상: [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)(병원): 미국 MultiCare 계열 두 병원의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기 버튼을 스스로 누르지 못해 사람이 계속 따라다녀야 했다고 2026-06-09 보도되었다. [사실][^ref-1154] 승강기 조작은 시설·설비 제어 경계의 연계 대상이며, 40. 운영 절차·요청 창구 페이지도 승강기 연동을 이 영역 밖의 설비 연계로 둔다.\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)(물류창고): 로봇·작업 상태 기록만으로는 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표를 계산할 수 없으므로, 이 지표는 23. 업무 시스템 연동을 거쳐 WMS·ERP 주문 데이터와 이어야 계산될 것으로 보인다. [추정][^ref-140][^ref-148][^ref-111] 이를 실제로 검증한 공개 사례는 열린 질문 oq-015 로 남아 있다.\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)(병원): 미국 ChristianaCare 는 간호사가 키오스크에서 Moxi 로봇을 호출하던 방식에 더해, 로봇을 Cerner 전자의무기록과 연동해 주문이 들어오면 로봇이 물품을 가지러 가게 하는 계획을 밝혔다(2022-08-11 보도, 계획 단계이며 운영 결과 미확인). [사실][^ref-1362] 주문 취소·변경을 진행 중인 로봇 작업에 반영한 공개 사례가 있는지는 [열린 질문](../../open-questions.md)에 새로 올렸다.\n\n### [G. 계획·최적화](../planning-and-optimization/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): [설명 가능한 다중 에이전트 경로 찾기](../../glossary/explainable-mapf.md) 연구(Kottinger·Almagor·Lahijanian, ICAPS 2022)는 경로 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 문제를 다루지만 알고리즘 수준의 연구다. [사실][^ref-1098]\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md): 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터가 위치 신뢰도와 실행 행동 증거를 결합해 에이전트를 분류하는 것으로 미루어, 실행 기록으로 이상 로봇을 가려 배정 후보에서 빼는 일이 두 영역의 접점이 될 것으로 보이며 물류센터 적용은 확인되지 않았다. [추정][^ref-494] 같은 연결이 [G. 계획·최적화의 '다른 대분류와의 연결'](../planning-and-optimization/index.md#다른-대분류와의-연결)에도 같은 각주로 실려 있고, 배정 전 검증 기준은 열린 질문 oq-082 로 남아 있다.\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)(물류창고): Omega(2024) 게재 연구는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했으며, 이는 모델·시뮬레이션 조건의 저자 보고값이고 현장 실측이 아니다. [사실][^ref-146] A. 기획·사업 페이지의 연결 절에도 같은 값과 단서가 실려 있다.\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md): Open-RMF 작업 요청 스키마가 가장 이른 시작 시각과 우선순위만 두고 마감 시각 필드는 두지 않으므로, 요청 창구에서 받은 긴급도·기한을 순서 결정 입력으로 옮기는 규칙이 두 영역의 접점이 될 것으로 보인다. [추정][^ref-125]\n\n### [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 다중 로봇 인터페이스 연구(Roldán 외, Sensors 2017-07-27)는 운영자 [상황 인식](../../glossary/situation-awareness.md)을 위한 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었으며, 이 연구의 몰입·예측 실험은 실험실 조건이다. [사실][^ref-1099]\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md): Open-RMF 작업 상태 스키마는 blocked·error·failed·delayed·canceled·killed 를 포함한 12개 상태 값과 작업에 걸린 중단(interruptions)·취소·강제 종료 요청 기록, 시작·종료 시각을 담는다(2026-10-09 확인). [사실][^ref-111] 그래서 실행 결과 확인과 이상 탐지가 같은 기록을 쓰는 것으로 보인다. [추정][^ref-111]\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): Open-RMF 경보(Alert) 메시지는 심각도 등급(info 0·warning 1·error 2), 운영자가 고를 수 있는 응답 목록(responses_available), 관련 작업 id 를 담는다(2026-10-09 확인). [사실][^ref-448] 원인 판정 뒤의 운영자 선택이 이 메시지를 거쳐 복구 조치로 넘어가는 것으로 보인다. [추정][^ref-448]\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 다중 로봇 수색·구조 과제 실험(Mehrotra·Sycara·Lewis·Chien·Wang, HFES 2011)은 경보 없음, 경보 자유 표시, 최상위 경보만 보이는 의사결정 보조의 세 조건을 비교했고, 자유 표시 조건의 운영자가 고장과 피해자를 더 빨리 탐지했으며 탐색 면적과 발견한 피해자 수에는 차이가 없었다(실험실 시뮬레이션 조건). [사실][^ref-1363] 경보 관리 표준으로는 ANSI/ISA 18.2-2016 이 공정 산업 시설에서 제어 시스템을 거쳐 운영자에게 표시되는 경보 전체의 수명주기 관리 원칙과 절차를 정하지만 이는 공정 산업 표준이며, 다중 로봇 플릿에 특화된 경보 관리 표준은 2026-10-09 조사에서 찾지 못했다. [사실][^ref-1359] 로봇 운영용 경보 관리 표준이나 지침이 있는지는 [열린 질문](../../open-questions.md)에 새로 올렸다.\n\n### [I. 설계·시뮬레이션](../design-and-simulation/index.md)\n\n이 대분류와의 연결은 현재 상태 표현이 아니라 기록 재현과 가정한 미래의 설계 쪽이다.\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md): Open-RMF 작업 이벤트 로그는 작업·단계·사건의 3계층으로 나뉘고 [MCAP](../../glossary/mcap.md) 은 시각 색인을 둔 기록 형식이어서 37. 관제 화면·실행 기록이 남긴 기록은 시간축 재현의 입력이 될 수 있어 보이지만, 이 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식은 확인되지 않았다. [추정][^ref-1094][^ref-1096] 변환 규칙은 열린 질문 oq-131 로 남아 있다.\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)(물류창고): AMR 물류센터 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼으며, 이는 시뮬레이션 결과다. [사실][^ref-102]\n\n### [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md): Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하므로, 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다(2026-10-09 확인, 두 문서는 같은 프로젝트라 독립 출처가 아니다). [사실][^ref-762][^ref-302]\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md): ros2_tracing(Bédard·Lütkebohle·Dagenais, IEEE RA-L 2022)은 저부하 LTTng 추적기로 ROS 2 실행 정보를 모으며 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가가 평균 0.0033 ms 였다고 보고했는데, 이는 저자 실험값이고 독립 재현은 미확인이다. [사실][^ref-1361] 플랫폼 서비스 쪽 [분산 추적](../../glossary/distributed-tracing.md)(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모으므로, 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다. [추정][^ref-447][^ref-1361] 두 계층을 이은 공개 사례는 열린 질문 oq-210 으로 남아 있다.\n\n### [L. AI·학습 기술](../ai-and-learning/index.md)\n\n분류 원문의 교차 규칙은 장애 분석을 38. 모니터링·이상 탐지·원인 분석에 적용되는 AI 연구 방법으로 둔다.\n\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md): 대규모 언어 모델로 로봇 실패를 설명하고 수정하는 REFLECT(2023) 같은 [실패 설명](../../glossary/failure-explanation.md) 연구가 두 영역을 잇는 예가 될 것으로 보인다. [추정][^ref-453]\n\n### [M. 안전](../safety/index.md)\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md): Winfield 외(2022-05-13)의 [윤리적 블랙박스](../../glossary/ethical-black-box.md) 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록하는 장치나 소프트웨어 모듈을 제안하며, 초안 표준은 논문 부속서에 토론용 초안으로 실렸다. [사실][^ref-1360] 초록에는 플릿·플랫폼 수준 기록에 대한 언급이 없다(부속서 본문은 열람하지 않음). [사실][^ref-1360] 플랫폼 수준의 최소 기록 항목은 열린 질문 oq-252 로 남아 있다.\n- 연계 대상: [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md): 40. 운영 절차·요청 창구 페이지는 로봇 교시·정비 작업 지침(산업안전보건기준에 관한 규칙 제222조)과 ANSI/A3 R15.08-3-2026 이 사용자에게 두는 운영 요구를 사업주·제조사 책임의 연계 대상으로 두므로, ROP는 요청·권한·기록 층으로 그 이행을 받쳐 주는 쪽인 것으로 보인다. [추정][^ref-1157][^ref-1153] 누가 이를 이행하는지는 열린 질문 oq-265 로 남아 있다.\n\n### [N. 보안·개인정보](../security-and-privacy/index.md)\n\n- [38. 모니터링·이상 탐지·원인 분석](monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md): [사이버복원력법](../../glossary/cyber-resilience-act.md)은 2026-09-11부터 디지털 요소 제품의 제조자에게 실제 악용되는 취약점과 중대 보안 사고를 24시간 안에 조기 경보하게 하므로, 이상 탐지가 보안 사고를 가려내는 시점이 보고 의무와 맞물릴 가능성이 있으며 오케스트레이션 플랫폼의 제조자 해당 여부는 미확인이다. [추정][^ref-1236]\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)(물류창고): 창고 작업자 12명을 반구조화 면담한 연구(Malik·Brandão·Coopamootoo, 2026)는 로봇 운영에 따르는 데이터 감시에 대한 작업자 우려를 확인하고, 감시 활동 알림·개인정보 통제 같은 작업자 중심 요구를 제시했다. [사실][^ref-1278]\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md): Open-RMF API 서버(rmf-server)는 OpenID Connect 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정하며, 관리자는 모든 그룹에서 모든 동작을 할 수 있고 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다(2026-10-09 확인). [사실][^ref-762]\n\n### [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)\n\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [56. 운영 이관·확대·교육](../verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)(상업 시설): 중국 고급 호텔 직원 19명 면담 연구(Fu·Zheng·Wong, 2022)에서는 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼고, 근무 중 로봇 교육·동료 교육·고장 처리·고객 안내 같은 추가 업무가 직원의 사용 저항으로 이어졌다. [사실][^ref-1150] 운영 책임 조직과 교육의 연결은 열린 질문 oq-266·oq-278 로 남아 있다([역할 모호성](../../glossary/role-ambiguity.md) 참고).\n\n### [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)\n\n- 연계 대상: [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md): 국내 병원·약국은 2018-05-18 입고 내역부터 마약류 취급 내역을 마약류통합관리시스템에 전산 보고하고 종전 마약류 관리대장은 2년간 보관한다고 2018-07-13 보도되었으며, 법령 원문과 현행 여부는 미확인이다. [사실][^ref-1364] 로봇 배송 이력이 이 보고·보관 대상에 드는지는 열린 질문 oq-239 로 남아 있다.\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md): 한국 근로자참여법 제20조가 신기계·기술 도입과 사업장 내 근로자 감시 설비 설치를 노사협의회 협의 사항으로 두므로, 성과 측정이 개별 작업자의 처리량·위치까지 기록하면 도입 전 노동자 참여 절차가 필요할 가능성이 있으며 법적 해당 여부는 미확인이다. [추정][^ref-1272][^ref-1278]\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md)(병원): 병원 자율 배송 로봇(TUG) 민족지 연구(Mutlu·Forlizzi, HRI 2008)에서 내과 병동은 업무 중단에 대한 낮은 허용도, 비용과 이익의 불일치, 통행이 많은 곳의 주행 중단 때문에 직원 저항을 보였고, 산후 병동은 로봇을 업무 흐름에 통합했다. [사실][^ref-1151]\n\n### [Q. 현장 유형별 적용](../site-type-applications/index.md)\n\nQ. 현장 유형별 적용은 현장마다 다른 요구를 모으고, 모든 현장에 공통인 운영·관제 기능은 J. 현장 운영·관제에 둔다. 이번 근거는 물류창고·제조 공장·병원·상업 시설에 한정되며 가정·실외·기타 현장의 근거는 없다.\n\n- [37. 관제 화면·실행 기록](control-screen-and-execution-records.md) ↔ [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): 국내 병원 현장에서 관제 시스템과 특수 물품 배송 이력 관리를 함께 개발하기로 한 협약이 2025-04-07 보도되었고, 37. 관제 화면·실행 기록 페이지가 찾은 현장 근거는 이 병원 사례 한 건뿐이다. [사실][^ref-1103]\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [61. 물류창고](../site-type-applications/warehouse.md): 로봇 이동형 풀필먼트 시스템 대기행렬 모델(Lamballais 외, 2017)에서는 처리량이 보관 구역 둘레의 작업대 위치에 영향을 받았으며, 이는 모델 연구로 현장 실측이 아니다. [사실][^ref-096] 협업형 AMR 피킹 해석 모델(Ghelichi·Kilaru, 2021)에서는 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우했으며, 이 역시 모델 연구로 현장 실측이 아니다. [사실][^ref-145]\n- [39. 운영 성과 측정·개선](operational-performance-measurement-and-improvement.md) ↔ [62. 제조 공장](../site-type-applications/manufacturing-plant.md): ISO 22400-2:2014 는 제조 운영 관리의 핵심성과지표 정의를 다루는 현행판이다. [사실][^ref-139] 에너지 관리 KPI 를 더한 개정 1(ISO 22400-2:2014/Amd 1:2017, 2017-04)이 있다. [사실][^ref-782] 개정판 ISO/DIS 22400-2 의 발행은 2026-09-26 확인 기준으로 확인되지 않았다. [사실][^ref-781] 이동로봇 플릿에 OEE 를 적용하는 합의된 정의는 열린 질문 oq-016 으로 남아 있다.\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): 한림대학교성심병원은 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다고 보도되었으며, 이는 2024년 보도 기준이고 두 보도가 병원 발표에서 나왔을 수 있어 독립 확인으로 보지 않는다. [사실][^ref-1199][^ref-944]\n- [40. 운영 절차·요청 창구](operating-procedures-and-request-channels.md) ↔ [64. 상업 시설](../site-type-applications/commercial-facilities.md): 미국 뉴욕 알로프트 호텔에서는 투숙객이 전화로 프런트에 요청하면 사람이 주문 물건과 객실 번호를 확인해 처리했고, 배송 로봇(Savioke Relay)은 객실 앞에 도착하면 객실 전화로 자동 알림을 보냈다(2017-04-18 보도). [사실][^ref-1152]\n\n### 아직 다루지 않은 연결\n\n- [B. 로봇 온톨로지](../robot-ontology/index.md) 전체(4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 7. 온톨로지 검증·변경 관리): 게시된 페이지에 J. 현장 운영·관제와 잇는 근거가 없다.\n- 이번 근거가 없는 세부영역: 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터.\n- Q. 현장 유형별 적용 가운데 65. 가정·공동주택, 66. 실외, 67. 기타 현장과의 연결 근거는 없다.\n\n[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09\n[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09\n[^ref-096]: Lamballais, T., Roy, D., & de Koster, M. B. M., Estimating performance in a Robotic Mobile Fulfillment System, 2017, https://repub.eur.nl/pub/107376/, 접근일 2026-10-09 (원문 미열람)\n[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-10-09 (원문 미열람)\n[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-10-09\n[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-10-09\n[^ref-139]: ISO, ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 2014, https://www.iso.org/standard/54497.html, 접근일 2026-10-09 (원문 미열람)\n[^ref-140]: ASCM, SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment, 미확인, https://scor.ascm.org/performance/reliability/RL.1.1, 접근일 2026-10-09 (원문 미열람)\n[^ref-145]: Ghelichi, Z., & Kilaru, S., Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers, 2021, https://www.sciencedirect.com/science/article/pii/S0307904X20305801, 접근일 2026-10-09 (원문 미열람)\n[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-10-09 (원문 미열람)\n[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-10-09\n[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09\n[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-10-09\n[^ref-302]: Open Robotics (open-rmf), rmf-web — README, 미확인, https://github.com/open-rmf/rmf-web, 접근일 2026-10-09 (원문 미열람)\n[^ref-313]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg, 접근일 2026-10-09\n[^ref-447]: OpenTelemetry (CNCF), OpenTelemetry Specification — Overview, 미확인, https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md, 접근일 2026-10-09\n[^ref-448]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_task_msgs/msg/Alert.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg, 접근일 2026-10-09\n[^ref-449]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/connection.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema, 접근일 2026-10-09\n[^ref-453]: Liu, Z., Bahety, A., & Song, S., REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023, https://arxiv.org/abs/2306.15724, 접근일 2026-10-09 (원문 미열람)\n[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-10-09 (원문 미열람)\n[^ref-569]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg, 접근일 2026-10-09\n[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09\n[^ref-781]: ISO, ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions, 미확인, https://www.iso.org/standard/87563.html, 접근일 2026-09-26 (원문 미열람)\n[^ref-782]: ISO, ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management, 2017-04, https://www.iso.org/standard/68295.html, 접근일 2026-09-26 (원문 미열람)\n[^ref-944]: 로봇신문, 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원', 2024-04-15, http://www.irobotnews.com/news/articleView.html?idxno=34601, 접근일 2026-10-09 (원문 미열람)\n[^ref-1093]: Open Robotics (open-rmf/rmf_visualization), rmf_visualization — README, 미확인, https://github.com/open-rmf/rmf_visualization, 접근일 2026-10-09 (원문 미열람)\n[^ref-1094]: Open Robotics (open-rmf/rmf_api_msgs), rmf_api_msgs schemas — task_log.json (Task Event Log), 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json, 접근일 2026-10-09\n[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-09 (원문 미열람)\n[^ref-1098]: Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022), Conflict-Based Search for Explainable Multi-Agent Path Finding, 2022-02, https://arxiv.org/abs/2202.09930, 접근일 2026-10-09 (원문 미열람)\n[^ref-1099]: Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)), Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction, 2017-07-27, https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1103]: 아주경제, 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다, 2025-04-07, https://www.ajunews.com/view/20250407084333272, 접근일 2026-10-09 (원문 미열람)\n[^ref-1150]: Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management), The perils of hotel technology: The robot usage resistance model, 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1151]: Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008-03, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-10-09 (원문 미열람)\n[^ref-1152]: 한국일보, “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인), 2017-04-18, https://www.hankookilbo.com/news/article/201704180418820469, 접근일 2026-10-09 (원문 미열람)\n[^ref-1153]: ANSI (The ANSI Blog), ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications, 미확인, https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1154]: Proof News (Varsha Bansal), Meet the Robot That Nurses Unplugged, 2026-06-09, https://www.proofnews.org/moxi/, 접근일 2026-10-09 (원문 미열람)\n[^ref-1157]: 고용노동부 (국가법령정보센터), 산업안전보건기준에 관한 규칙 제222조(교시 등), 2025-09-01, https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202, 접근일 2026-10-09 (원문 미열람)\n[^ref-1199]: ZDNet Korea, 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인), 2024-09-19, https://zdnet.co.kr/view/?no=20240919162124, 접근일 2026-10-09 (원문 미열람)\n[^ref-1236]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-10-09 (원문 미열람)\n[^ref-1272]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-10-09 (원문 미열람)\n[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-10-09 (원문 미열람)\n[^ref-1359]: ISA (ANSI Webstore 게재), ANSI/ISA 18.2-2016 Management of Alarm Systems for the Process Industries, 2016, https://webstore.ansi.org/standards/isa/ansiisa182016, 접근일 2026-10-09\n[^ref-1360]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09\n[^ref-1361]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L 7(3), arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-10-09\n[^ref-1362]: TechTarget (Hannah Nelson, Xtelligent Healthcare Media), Hospital Looks to 'Cobot' EHR Integration to Alleviate Nurse Burnout, 2022-08-11, https://techtarget.com/searchhealthit/feature/Hospital-Looks-to-Cobot-EHR-Integration-to-Alleviate-Nurse-Burnout, 접근일 2026-10-09\n[^ref-1363]: Mehrotra, S., Sycara, K., Lewis, M., Chien, S.-Y., & Wang, H. (Proceedings of the Human Factors and Ergonomics Society), Effects of alarms on control of robot teams, 2011, https://d-scholarship.pitt.edu/12400/, 접근일 2026-10-09\n[^ref-1364]: 데일리팜 (김지은), 마약통합시스템 시행 2개월…병원·약국 다빈도 질문은, 2018-07-13, https://dailypharm.com/user/news/85066, 접근일 2026-10-09"
        },
        {
          "section": "참고 자료",
          "action": "replace",
          "content": "없음. '이 대분류의 핵심 포인트' 원문 문단에는 참고문헌 번호([n]) 표기가 없어 원문 각주가 없다. '다른 대분류와의 연결' 절에서 쓴 각주의 정의는 그 절 끝에 있다."
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | J. 현장 운영·관제 | '다른 대분류와의 연결' 절 신규 작성(15개 대분류와의 연결, B. 로봇 온톨로지 근거 없음 명시, 각주 47건, 1차 조건부 승인 수정 22건 반영), 템플릿 마지막 절 '참고 자료' 추가 | run 2026-10-09-05",
  "index_updates": {
    "home_recent": "2026-10-09 — J. 현장 운영·관제: '다른 대분류와의 연결' 절 신규 작성(15개 대분류와의 연결 정리, B. 로봇 온톨로지는 근거 미확보로 명시)",
    "category_recent": "2026-10-09 — J. 현장 운영·관제: '다른 대분류와의 연결' 절 신규 작성(37~40번 세부영역과 15개 대분류의 연결, 아직 다루지 않은 연결 목록 포함)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "alarm-management",
      "term_ko": "경보 관리",
      "term_en": "Alarm Management (ANSI/ISA 18.2)",
      "definition": "운영자에게 표시되는 경보를 정의·설계·운영·유지·변경하는 수명주기 전체를 관리하는 일로, 공정 산업에서는 ANSI/ISA 18.2-2016 이 일반 원칙과 절차를 정한다.",
      "description": "ANSI/ISA 18.2-2016 은 공정 산업 시설의 기본 공정 제어·경보판·화재·가스 패키지·안전계장 시스템 경보를 포함하는 공정 산업 표준이다. 다중 로봇 플릿에 특화된 경보 관리 표준은 2026-10-09 조사에서 찾지 못했다.",
      "related_areas": [
        38,
        31
      ],
      "sources": [
        "ref-1359"
      ]
    },
    {
      "action": "new",
      "slug": "runtime-tracing",
      "term_ko": "런타임 추적",
      "term_en": "Runtime Tracing (ros2_tracing)",
      "definition": "실행 중인 소프트웨어 내부의 콜백·메시지 전달 같은 실행 정보를 저부하 추적기로 기록하는 방법으로, ROS 2 에서는 LTTng 기반 ros2_tracing 이 이를 제공한다.",
      "description": "기존 용어 '분산 추적'이 플랫폼 서비스 사이의 요청 흐름(OpenTelemetry 등)을 다루는 것과 달리, 런타임 추적은 ROS 2 런타임 내부라는 다른 계층의 실행 정보를 모은다. 두 계층을 작업 식별자로 잇는 공개 사례는 미확인이다.",
      "related_areas": [
        38,
        43
      ],
      "sources": [
        "ref-1361",
        "ref-447"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1359",
      "org": "ISA (ANSI Webstore 게재)",
      "title": "ANSI/ISA 18.2-2016 Management of Alarm Systems for the Process Industries",
      "published": "2016",
      "url": "https://webstore.ansi.org/standards/isa/ansiisa182016",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "공정 산업 시설에서 운영자에게 표시되는 경보 시스템의 수명주기 관리 원칙·절차를 정한 표준의 판매 소개 페이지. 본문은 유료라 소개 문구만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1360",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사고·아차 사고 조사를 위해 소셜 로봇의 센서·구동기·제어 결정을 안전하게 기록하는 윤리적 블랙박스의 초안 공개 표준. 초록만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1361",
      "org": "Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L 7(3), arXiv)",
      "title": "ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2",
      "published": "2022-07",
      "url": "https://arxiv.org/abs/2201.00393",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "LTTng 기반 ROS 2 실행 정보 추적 도구와 계측. 저자 실험에서 평균 종단 지연 증가는 0.0033 ms 였다. 초록만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1362",
      "org": "TechTarget (Hannah Nelson, Xtelligent Healthcare Media)",
      "title": "Hospital Looks to 'Cobot' EHR Integration to Alleviate Nurse Burnout",
      "published": "2022-08-11",
      "url": "https://techtarget.com/searchhealthit/feature/Hospital-Looks-to-Cobot-EHR-Integration-to-Alleviate-Nurse-Burnout",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "ChristianaCare 가 키오스크로 호출하던 Moxi 로봇을 Cerner 전자의무기록과 연동해 주문으로 출동시키려는 계획을 다룬 보도.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1363",
      "org": "Mehrotra, S., Sycara, K., Lewis, M., Chien, S.-Y., & Wang, H. (Proceedings of the Human Factors and Ergonomics Society)",
      "title": "Effects of alarms on control of robot teams",
      "published": "2011",
      "url": "https://d-scholarship.pitt.edu/12400/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "다중 로봇 수색·구조 과제에서 경보 없음·자유 표시·최상위 경보만 표시 조건을 비교한 실험. 저장소의 초록을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1364",
      "org": "데일리팜 (김지은)",
      "title": "마약통합시스템 시행 2개월…병원·약국 다빈도 질문은",
      "published": "2018-07-13",
      "url": "https://dailypharm.com/user/news/85066",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "2018-05-18 시행된 마약류통합관리시스템 전산 보고와 종전 마약류 관리대장 2년 보관, 과태료 유예를 다룬 보도.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "관제–이동로봇 통신 명세(main 3.0.0). visualization·state 토픽 분리 등.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 상태 메시지 JSON 스키마(오류 수준 등).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-096",
      "org": "Lamballais, T., Roy, D., & de Koster, M. B. M.",
      "title": "Estimating performance in a Robotic Mobile Fulfillment System",
      "published": "2017",
      "url": "https://repub.eur.nl/pub/107376/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 대기행렬 모델로 작업대 위치 등이 처리량에 미치는 영향을 추정.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-102",
      "org": "Springer(FAIM 2025 발표 논문, 저자 미확인)",
      "title": "Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics",
      "published": "2025",
      "url": "https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 물류센터 AMR 플릿·충전기 규모를 시뮬레이션으로 산정한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "작업 상태 값 12개, 시작·종료 시각, 단계, 중단·취소·강제 종료 기록을 담는 Open-RMF 작업 상태 스키마. 이번 실행에서 원문을 다시 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 작업 요청 스키마(가장 이른 시작 시각·우선순위·플릿 지정).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-139",
      "org": "ISO",
      "title": "ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions",
      "published": "2014",
      "url": "https://www.iso.org/standard/54497.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 제조 운영 관리 핵심성과지표의 정의와 설명.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-140",
      "org": "ASCM",
      "title": "SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment",
      "published": null,
      "url": "https://scor.ascm.org/performance/reliability/RL.1.1",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. SCOR 완전 주문 이행률 지표 정의.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-145",
      "org": "Ghelichi, Z., & Kilaru, S.",
      "title": "Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers",
      "published": "2021",
      "url": "https://www.sciencedirect.com/science/article/pii/S0307904X20305801",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 협업형 AMR 피킹의 해석적 성과 모델.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-146",
      "org": "Omega 게재 논문(저자 미확인)",
      "title": "The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority",
      "published": "2024",
      "url": "https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RMFS 에서 동적 우선순위 규칙의 에너지·처리량 효과를 모델·시뮬레이션으로 평가.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-148",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "로봇 상태 값 7개, 배터리, 현재 작업 id, 문제 목록, 위치, 기록 시각을 담는 로봇 상태 스키마. 이번 실행에서 원문을 다시 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "MassRobotics AMR 상호운용 표준 JSON 스키마(운용 상태 waitingExternalEvent 등).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-283",
      "org": "Open Robotics",
      "title": "Doors (integration_doors) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_doors.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 문 연동과 문 어댑터의 상태 감독자 역할 설명.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-302",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 웹 대시보드·API 서버 저장소 README(기본 비영속 저장). 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-313",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "문 모드 다섯 값(closed·moving·open·offline·unknown) 정의.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-447",
      "org": "OpenTelemetry (CNCF)",
      "title": "OpenTelemetry Specification — Overview",
      "published": null,
      "url": "https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "분산 서비스의 추적·지표·로그 신호와 컨텍스트 전파를 정의하는 명세 개요.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-448",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_task_msgs/msg/Alert.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "심각도 등급(info·warning·error), 응답 목록, 관련 작업 id 를 담는 경보 메시지 정의. 이번 실행에서 원문을 다시 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-449",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/connection.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 연결 상태(ONLINE·OFFLINE·CONNECTION_BROKEN) 스키마.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-453",
      "org": "Liu, Z., Bahety, A., & Song, S.",
      "title": "REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction",
      "published": "2023",
      "url": "https://arxiv.org/abs/2306.15724",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 경험 요약과 대규모 언어 모델로 실패를 설명하고 수정하는 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-494",
      "org": "Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU)",
      "title": "Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.25690",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 위치 스푸핑 공격 모델과 신뢰 인지 모니터로 적대 에이전트를 계획에서 빼는 다중 로봇 롤아웃 계획 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-569",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "플릿 이름과 열고 닫을 차선 목록만 담는 차선 요청 메시지. 이번 실행에서 원문을 다시 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "rmf-server 의 OIDC 인증, 앱 내 역할·동작·그룹 기반 권한 판정, 기본 메모리 내 SQLite 와 지원 데이터베이스를 설명한다. 이번 실행에서 원문을 다시 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-781",
      "org": "ISO",
      "title": "ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions",
      "published": null,
      "url": "https://www.iso.org/standard/87563.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. ISO 22400-2 개정판 초안(DIS) 페이지. 2026-09-26 확인 기준 새 판 발행은 확인되지 않았다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-782",
      "org": "ISO",
      "title": "ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management",
      "published": "2017-04",
      "url": "https://www.iso.org/standard/68295.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. ISO 22400-2:2014 에 에너지 관리 KPI 를 더한 개정 1.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-944",
      "org": "로봇신문",
      "title": "국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원'",
      "published": "2024-04-15",
      "url": "http://www.irobotnews.com/news/articleView.html?idxno=34601",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "한림대학교성심병원 커맨드센터의 서비스 로봇 통합 관제·요청 경로 보도. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1093",
      "org": "Open Robotics (open-rmf/rmf_visualization)",
      "title": "rmf_visualization — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_visualization",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "층 평면도 위에 로봇·문·승강기·주행 그래프·예측 궤적을 표시하는 Open-RMF 시각화 패키지 README. 브리프 기준 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1094",
      "org": "Open Robotics (open-rmf/rmf_api_msgs)",
      "title": "rmf_api_msgs schemas — task_log.json (Task Event Log)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "작업·단계·사건 3계층 로그 구조를 정의한 작업 이벤트 로그 스키마. 이번 실행에서 원문을 다시 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1096",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "시각 색인을 둔 로봇 기록 컨테이너 형식 명세. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1098",
      "org": "Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022)",
      "title": "Conflict-Based Search for Explainable Multi-Agent Path Finding",
      "published": "2022-02",
      "url": "https://arxiv.org/abs/2202.09930",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람이 확인할 수 있게 나눠 보여 주는 설명 가능한 다중 에이전트 경로 계획 연구. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1099",
      "org": "Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8))",
      "title": "Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction",
      "published": "2017-07-27",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "다중 로봇 인터페이스의 몰입·예측이 운영자 상황 인식에 주는 영향을 실험한 연구. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1103",
      "org": "아주경제",
      "title": "현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다",
      "published": "2025-04-07",
      "url": "https://www.ajunews.com/view/20250407084333272",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "현대차·기아와 한림대학교의료원의 배송 로봇·관제·수령 인증·특수 물품 배송 이력 관리 공동 개발 협약 보도. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1150",
      "org": "Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management)",
      "title": "The perils of hotel technology: The robot usage resistance model",
      "published": "2022",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "호텔 직원 면담으로 로봇 사용 저항 요인(역할 모호성·추가 업무 등)을 정리한 연구. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1151",
      "org": "Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008-03",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "병원 자율 배송 로봇(TUG) 민족지 연구. 병동별 수용 차이를 업무 흐름·사회·환경 요인으로 설명. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1152",
      "org": "한국일보",
      "title": "“딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인)",
      "published": "2017-04-18",
      "url": "https://www.hankookilbo.com/news/article/201704180418820469",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "뉴욕 알로프트 호텔의 프런트 경유 요청과 배송 로봇(Savioke Relay) 운영 보도. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1153",
      "org": "ANSI (The ANSI Blog)",
      "title": "ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications",
      "published": null,
      "url": "https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 이동로봇 적용(사용자 측 요구) 표준 소개 글.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1154",
      "org": "Proof News (Varsha Bansal)",
      "title": "Meet the Robot That Nurses Unplugged",
      "published": "2026-06-09",
      "url": "https://www.proofnews.org/moxi/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "MultiCare 계열 병원의 Moxi 로봇 운영 문제(길 잃음, 승강기 버튼 조작 불가, 사람 동행)를 다룬 보도. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1157",
      "org": "고용노동부 (국가법령정보센터)",
      "title": "산업안전보건기준에 관한 규칙 제222조(교시 등)",
      "published": "2025-09-01",
      "url": "https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "산업용 로봇 교시 등 작업 시 작업 지침 등을 정한 조항. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1199",
      "org": "ZDNet Korea",
      "title": "로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인)",
      "published": "2024-09-19",
      "url": "https://zdnet.co.kr/view/?no=20240919162124",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "한림대학교성심병원 커맨드센터의 7종 73대 로봇 운영과 누적 사용 건수 보도. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1236",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Cyber Resilience Act - Reporting obligations",
      "published": "2026-09-11",
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "EU 사이버복원력법의 취약점·중대 사고 보고 의무(24시간 조기 경보, 72시간 통지, 최종 보고) 안내. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1272",
      "org": "대한민국 국회 (법률 제16320호, 케이스노트 게재)",
      "title": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항)",
      "published": "2019-04-16",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "노사협의회 협의 사항(신기계·기술 도입, 근로자 감시 설비 설치 등)을 정한 조항. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    },
    {
      "id": "ref-1278",
      "org": "Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics)",
      "title": "Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety",
      "published": "2026",
      "url": "https://doi.org/10.1007/s12369-026-01359-1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "창고 작업자 12명 면담으로 로봇 운영의 데이터 감시 우려와 작업자 중심 요구(수동 무시·개인정보 통제·감시 알림)를 확인한 연구. 이번 실행에서는 원문 미열람.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/field-operations-and-monitoring/index.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "다중 로봇 플릿 관제에서 경보 우선순위, 경보 홍수 기준, 경보 합리화 절차를 ANSI/ISA 18.2 처럼 정한 로봇 운영용 경보 관리 표준이나 공개 지침이 있는가?",
      "areas": [
        38,
        31
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "전자의무기록 주문이 로봇 작업 요청을 자동으로 만드는 병원 연동에서 주문 취소·변경을 진행 중인 로봇 작업에 반영하고 결과를 기록에 되돌린 공개 사례가 있는가?",
      "areas": [
        40,
        23,
        63
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [],
  "standards_updates": [
    {
      "name": "ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries)",
      "kind": "표준",
      "org": "ISA(International Society of Automation)",
      "url": "https://webstore.ansi.org/standards/isa/ansiisa182016",
      "related_areas": [
        38,
        31
      ],
      "summary": "공정 산업 시설에서 제어 시스템을 거쳐 운영자에게 표시되는 경보 전체의 수명주기 관리 원칙과 절차를 정한 표준(2009년 판 개정). 공정 산업 표준이며 다중 로봇 플릿 적용은 확인되지 않았다.",
      "ref_id": "ref-1359"
    }
  ],
  "additional_research_requests": [
    "대분류 페이지 '다른 대분류와의 연결' 절의 B. 로봇 온톨로지 항목: 4. 이기종 로봇 등록·5. 로봇 능력·작업 표현의 능력·상태 어휘가 37. 관제 화면·실행 기록의 표시나 38. 모니터링·이상 탐지·원인 분석의 원인 범주와 이어진다는 검증된 근거가 게시 페이지에 없어 '아직 다루지 않은 연결'로만 적었다. 두 대분류를 잇는 자료 조사가 필요하다.",
    "같은 절의 '아직 다루지 않은 연결'(41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 58. 다사업자 책임·계약·데이터)과 가정·실외·기타 현장 유형 근거: 다음 대분류 연결 실행에서 J. 현장 운영·관제와의 연결 근거를 찾아야 한다.",
    "f25 의 오토스토어 경제성 수치(ref-150)는 벤더 주장이라 본문에서 뺐다. A. 기획·사업 연결에 쓸 독립 출처의 투자 효과 측정 자료(oq-017)가 필요하다.",
    "다음 영역 실행 후보(브리프 제안): 38. 모니터링·이상 탐지·원인 분석 10절에 f18·f19·f21·f22 반영, 37. 관제 화면·실행 기록 11절 oq-252 에 f10, oq-239 에 f11 근거 추가. 하루 갱신 상한으로 이번 실행에서는 대분류 페이지만 고쳤다.",
    "f11 마약류 관리대장 보관 기간은 2018년 기사 기준이다. 37. 관제 화면·실행 기록 ↔ 59. 법·규제·보험·라이선스 연결을 보강하려면 현행 마약류 관리법령 원문의 보관·보고 조항 확인이 필요하다.",
    "pipeline 담당 확인 요청: 입력 대분류 페이지에 템플릿의 마지막 절 '참고 자료'가 없어 형식 검증이 실패했다. 이번 재작성에서는 '참고 자료' 절을 patches(replace)로 보냈다. 패치 적용 코드가 없는 절을 페이지 끝에 새로 만드는지 확인하고, 다른 대분류 시드 페이지에도 이 절이 빠져 있는지 점검해야 한다."
  ],
  "fixes_applied": [
    "patches 대상 절 — 페이지 H2 와 같은 번호 없는 '다른 대분류와의 연결'로 patch(action replace)를 보내 '아직 작성되지 않음(에이전트가 채운다).'를 교체했고, 다른 절과 auto 마커는 건드리지 않았다.",
    "각주 정의 — 절에서 쓴 각주 47건을 '[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일 …' 형식으로 이번 patch 절 끝에 두었다. 이번 실행 브리프 출처는 접근일 2026-10-09, 브리프에 없는 기존 각주 ref-781·ref-782 는 실제 접근일인 2026-09-26 으로 적었다.",
    "원문 미열람 표시 — 지시된 26건과 ref-781·ref-782 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 에서도 source_unopened: true 로 두었다(ref-150 은 인용하지 않아 넣지 않음).",
    "f16 — 12개 상태 값과 중단·취소·강제 종료 기록은 [사실][^ref-111], '실행 결과 확인과 이상 탐지가 같은 기록을 쓴다'는 별도 문장 [추정][^ref-111]으로 H. 실행·협업·예외 복구 항목에 썼다.",
    "f17 — Alert 메시지 필드(심각도 등급·응답 목록·관련 작업 id)는 [사실][^ref-448], '운영자 선택이 복구 조치로 넘어간다'는 별도 문장 [추정][^ref-448]으로 분리했다.",
    "f26 — 로봇 상태 스키마 필드는 [사실][^ref-148], '가동률·충전·오류 시간 지표의 원천'은 별도 문장 [추정][^ref-148]으로 분리하고 A. 기획·사업 연결 절로 링크했다.",
    "f18 — '최상위 경보 하나만 보여 준 조건보다'를 빼고 비교한 세 조건, 자유 표시 조건의 빠른 탐지, 탐색 면적·피해자 수 무차이를 [사실][^ref-1363]으로 쓰고 실험실 시뮬레이션 조건을 붙였다.",
    "f10 — '초록에는 플릿·플랫폼 수준 기록에 대한 언급이 없다(부속서 본문 미열람)'로 좁혔고, 초안 표준이 논문 부속서에 토론용 초안으로 실렸음을 밝혔으며 용어집 '윤리적 블랙박스'로 링크했다.",
    "f11 — '연계 대상:'으로 시작하는 두 문장으로 줄이고 '2018-05-18 입고 내역부터 전산 보고, 종전 관리대장 2년 보관', 기준일 2018-07-13 보도, '법령 원문·현행 여부 미확인'을 병기했으며 로봇 배송 이력 해당 여부는 oq-239 로 남겼다.",
    "f33 — 개정 1(2017-04) 진술에 [^ref-782], ISO/DIS 22400-2 미발행 진술에 [^ref-781]을 붙이고 기준일을 '2026-09-26 확인'으로 두었다.",
    "f25 — ref-150 의 오토스토어 수치와 각주를 본문에 쓰지 않았고, 문장은 [추정][^ref-148]로만 썼다.",
    "f32 — Lamballais 외(2017)와 Ghelichi·Kilaru(2021)를 문장별로 나눠 연도를 밝히고 각각 '모델 연구로 현장 실측이 아니다'를 붙였다.",
    "f28·f22·f29·f41 — 각 문장 안에 '모델·시뮬레이션 조건의 저자 보고값이고 현장 실측이 아니다', '저자 실험값이며 독립 재현은 미확인', '시뮬레이션 결과', '2024년 보도 기준이고 병원 발표에서 나왔을 수 있어 독립 확인으로 보지 않는다'를 유지했다.",
    "추정·low finding — f3·f9·f20·f23·f24·f25·f31·f38 을 '것으로 보인다'·'가능성이 있다' 형태로만 썼고, f24 에 '오케스트레이션 플랫폼의 제조자 해당 여부는 미확인', f31 에 '법적 해당 여부는 미확인'을 병기했다.",
    "범위 경계 — f11·f38·f43 항목을 '연계 대상:'으로 시작해 짧게 썼고, f15 에서 문 개폐 제어를, f43 에서 승강기 조작을 연계 대상으로 밝혀 ROP 몫을 상태 확인·요청으로 한정했으며, f19 는 공정 산업 표준이고 로봇 플릿용 경보 관리 표준은 찾지 못했다고 쓰고 새 열린 질문과 이었다.",
    "18 대 34 구분 — E. 사물·사람·실시간 상태 항목 머리에 현재 상태 표현(18. 실시간 세계 상태·데이터 일관성) 쪽임을, I. 설계·시뮬레이션 항목 머리에 기록 재현·가정한 미래 쪽임을 밝혀 f13·f26 과 f2·f29 를 따로 썼다.",
    "L. AI·학습 기술 — 교차 규칙은 [분류원문] 인용 없이 태그 없는 서술로 쓰고, f23 은 38. 모니터링·이상 탐지·원인 분석과 47. AI·학습·적응과 모델 운영 페이지 양쪽으로 링크했다.",
    "'아직 다루지 않은 연결' 소절 — B. 로봇 온톨로지 전체(4~7 세부영역 이름 포함), 지시된 9개 세부영역, Q. 현장 유형별 적용의 가정·실외·기타 근거 부재를 번호와 이름으로 적었다.",
    "중복 각주 재사용 — f26·f28 은 ref-148·ref-146, f20 은 ref-494 를 쓰고 같은 단서 표현을 유지했으며 A. 기획·사업과 G. 계획·최적화의 '다른 대분류와의 연결' 절로 링크했다.",
    "표기 — 대분류는 문자와 이름, 세부영역은 번호와 이름을 함께 썼고(요약 표 포함), 링크는 docs/categories/field-operations-and-monitoring/index.md 기준 상대 경로(.md 포함)로 썼다. Mermaid 도식은 쓰지 않았다.",
    "직접 인용 — f34·f11·f19 를 포함한 모든 출처를 재서술로만 써서 출처당 1회 이하를 지켰다.",
    "새 열린 질문 2건(경보 관리 표준 — areas 38·31, EHR 주문 연동 취소·변경 — areas 40·23·63)을 open_question_updates 로 등록하고 본문에서 열린 질문 페이지로 연결했으며, 용어 '경보 관리'와 '런타임 추적'을 glossary_updates 로 내면서 '런타임 추적' 설명에 기존 '분산 추적'과 다른 계층(ROS 2 런타임 내부)임을 밝혔다."
  ]
}
```


## 형식 검증 오류 (재작성)

직전 원고(runs/<run_id>/pages.json, pages/)가 코드 형식 검증(pipeline/validate_run.py)을 통과하지 못했다. 내용(주장·태그·각주·판정)은 바꾸지 말고 아래 형식 오류만 고친 전체 pages.json 을 다시 반환한다. 차등 갱신 실행이면 patches 로, 아니면 content 로 보낸다.

- docs/categories/field-operations-and-monitoring/index.md: 패치 대상 절을 찾지 못했다: '참고 자료'
- docs/categories/field-operations-and-monitoring/index.md: pages/ 에 파일이 없다
