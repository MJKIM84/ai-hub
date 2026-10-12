(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-06
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 50. 안전 표준·인증·사고 조사 (M. 안전)
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

### runs/2026-10-11-06/target.json

```json
{
  "run_id": "2026-10-11-06",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 172,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 50,
    "area_name": "50. 안전 표준·인증·사고 조사",
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
  "selection_rationale": "CLI 지정 run_type=update, area=50"
}
```

### runs/2026-10-11-06/research.json

```json
{
  "run_id": "2026-10-11-06",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 50,
    "area_name": "50. 안전 표준·인증·사고 조사",
    "category": "M. 안전"
  },
  "gaps": [
    "섹션 5. 적용 사례 — 실외 사례 표·본문(98·100·104·106행)이 고시 제2023-211호를 현행 근거로 두고 심사항목 8개·16가지를 '어느 쪽도 고르지 않고' 병기하며, 행정예고 기준값을 '확정 고시 별표 원문 미확인'으로 둠. 제조 공장·물류창고 사고 사례는 수사·조사 중 기사 두 건뿐이고 공식 재해사례 자료가 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area50-s6) — '사고 기록 장치' 소절의 '기록할 데이터 형식과 보존 기간 … 미확인'(45행), 조직·제어 책임까지 보는 사고 분석 방법(CAST) 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area50-s7) — EN ISO 10218 EU 조화 게재 행(42행)이 IBF 해설 단독 근거로 [사실], 실외이동로봇 행(45행)의 '고시 제2023-211호가 정한다'가 낡음, R15.08-3·ISO 3691-4 차기판·KS 부합판·UL 3100·국내 자율안전확인·EU 기계 규정 기록 요구·rosbag2/MCAP 기록 계약 없음",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area50-s8) — Sanders 외의 관측 기간·관할 범위 미기재, 미국 보상 청구 자료(Suresh 외 2026) 없음, Webb 외 역할극의 수행 조건·한계 미기재",
    "섹션 4. 핵심 개념과 용어(분리 2026-09-30-area50-s4) — '적합성 추정' 항목(41행)이 해설 기준이고 2027-01-20 목록 폐지 미반영, '중상 보고' 항목(45행)의 기간이 연 단위",
    "섹션 9. 책임 경계 — 실외 인증이 요구하는 관제장치 기능(실시간 상태·원격 정지)과 인증 정보의 관제장치 모델 단위 미반영",
    "섹션 11. 열린 질문(분리 2026-09-30-area50-s11) — oq-186·oq-230 이 별표 원문 미확인 상태, oq-384(ISO 3691-4 차기판 단계 충돌) 미해소",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 고시 근거(제2025-021호), 16/8 항목 경위, EU 게재 서술 강등, ref-789 제목, 'KS B ISO 10218-2 2017 확인'"
  ],
  "research_questions": [
    "어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]",
    "oq-186·oq-230 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시와 항목 대응은 무엇인가? (섹션 5·7·11 겨냥)",
    "EN ISO 10218-1/-2:2025 의 EU 조화 게재는 어떤 법령에 대한 것이며 언제까지 효력이 있는가, ISO 3691-4 차기판·국내 KS 부합판의 현재 상태는 무엇인가(oq-384, oq-251)? (섹션 4·7 겨냥)",
    "oq-252 사고 조사에 필요한 기록 항목·형식·보존을 정한 공개 규약(EBB 초안, EU 기계 규정, rosbag2·MCAP)은 무엇을 정하고 무엇을 비워 두는가? (섹션 6·7 겨냥)",
    "로봇 사고 통계(OSHA SIR, Ohio 보상 청구, 국내 공식 재해사례)는 어떤 관할·기간·집계 단위·한계를 가지는가? (섹션 5·8 겨냥)",
    "사고 원인을 개인 과실이 아니라 제어 구조·조직 정책까지 조사하는 방법(CAST·역할극 증언)은 무엇을 요구하고 어떤 한계가 있는가? (섹션 6·8 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "위원회 시행결정 (EU) 2026/2015(2026-09-04 채택, 2026-09-07 관보 L 시리즈 게재)의 부속서는 시행결정 (EU) 2023/1586 부속서 I 에 EN ISO 10218-1:2025(223a)와 EN ISO 10218-2:2025(224a)의 참조를 추가한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "부속서 (2)(a): \"223a. EN ISO 10218-1:2025 Robotics – Safety requirements – Part 1: Industrial robots\" / \"224a. EN ISO 10218-2:2025 … Part 2: Industrial robot applications and robot cells\". 머리말 \"OJ L 2026/2015, 7.9.2026\", \"of 4 September 2026\", 제3조 관보 게재일 발효. 기존 위키(2026-09-30-area50-s7.md 42행, s4.md 41행, safety/index.md 177행)의 IBF 해설 기반 게재 사실·날짜를 1차 원문으로 보강",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "이 결정이 참조를 추가한 목록(2023/1586 부속서 I)은 기계류 지침 2006/42/EC 에 대한 적합성 추정을 주는 조화 표준 목록이며, 같은 결정 제2조는 2023/1586 을 2027-01-20 부로 폐지한다. 전문 (14)는 그 이유를 지침 2006/42/EC 가 규정 (EU) 2023/1230 으로 같은 날 폐지되기 때문이라고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "전문 (11): \"references of harmonised standards conferring a presumption of conformity with Directive 2006/42/EC\". 제2조: \"Implementing Decision (EU) 2023/1586 is repealed with effect from 20 January 2027.\" 전문 (14) 같은 취지. 2023/1230 에 따른 새 조화 표준 게재로 읽지 않음(이 결정은 지침 기반)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "기존 위키(2026-09-30-area50-s7.md 42행)의 'PL d·범주 3 일률 요구 대신 표의 기본 성능 수준 또는 위험성평가 근거 선택 허용, 운전 정지용 정상 정지 기능 신설' 서술은 컨설팅사 IBF Solutions 해설만 근거로 [사실]로 실려 있다. 관보 원문으로 확인되는 것은 참조 게재 사실·날짜·법적 기반뿐이므로 이 서술은 [추정]·벤더 해설로 낮추는 것이 맞다.",
      "tag": "추정",
      "source_ids": [
        "ref-1116",
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: IBF Solutions 해설(ref-1116, 2026-09-18)만 PL d·범주 3 대체와 정상 정지 요구를 전한다. (EU) 2026/2015 본문·부속서에는 참조 목록만 있고 ISO 10218 조항 내용은 없음. ISO 10218:2025 원문 미열람이라 해설 내용 자체의 옳고 그름은 판단하지 않음. 같은 서술이 s4.md 41행·safety/index.md 177행과 이어짐",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f4",
      "claim": "ANSI/A3 R15.08-3-2026(Part 3: Use of IMR Applications)은 A3 판매 페이지 기준 2026-04-23 발행으로 표시되며, 이 사실은 위키에 이미 있다. 이 영역 7절 표에는 R15.08-2 만 있어 Part 3 행을 더할 근거로만 쓴다.",
      "tag": "추정",
      "source_ids": [
        "ref-1255"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기존 내용 확인: ref-1255(2026-10-09 원문 열람, \"Published April 23, 2026\"), docs/categories/safety/index.md 53·137·169행. 이번 재열람은 Cloudflare 차단으로 실패해 [추정]. 사용자 의무 세부(oq-265)는 답하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "ISO 3691-4 차기판 프로젝트는 ISO 위원회 페이지에서 'ISO/DIS 3691-4, Edition 3, Under development'이며 단계 40.60(투표 종료, 2026-09-10)으로 표시되고 ISO 3691-4:2023 을 대체할 예정이다. 발행된 개정판이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-789"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "committee.iso.org/standard/88615: \"ISO/DIS 3691-4 / Edition 3 / Under development / Stage: Close of voting [40.60]\", 이력 \"40.60 2026-09-10\", \"Will replace ISO 3691-4:2023\". 위키 ref-789 의 2026-09-26 'ISO/CD' 기록과의 충돌(oq-384)을 해소. ref-789 제목을 'ISO/DIS 3691-4 (제3판)'으로 갱신 제안. 개정안 본문 미열람",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "국가표준 목록에서 KS B ISO 10218-1(산업용 로봇의 안전 요구사항 제1부: 로봇)의 대응 국제표준은 ISO 10218-1:2011(IDT, 일치)이고 최종개정확인일은 2021-11-26 이다(제정 2008-01-17).",
      "tag": "사실",
      "source_ids": [
        "ref-1497"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "standard.go.kr 상세: 대응국제표준 \"ISO 10218-1:2011 / IDT 일치\", 제정일 2008-01-17, 최종개정확인일 2021-11-26. 최종개정확인일은 다른 표준과 연계된 확인 개정일로 보이며, ISO 10218-1:2025 부합화 KS 는 이 목록에서 확인되지 않음(부재 증명 아님)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "같은 목록에서 KS B ISO 10218-2(제2부: 로봇 시스템 및 통합)의 대응 국제표준은 ISO 10218-2:2011(IDT)이고 최종개정확인일은 2022-10-12(고시 제2022-0433호)다. 위키의 'KS B ISO 10218-2 2017 확인' 표현은 낡았다.",
      "tag": "사실",
      "source_ids": [
        "ref-211"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "standard.go.kr 상세: \"ISO 10218-2:2011 / IDT 일치\", 제정일 2012-03-29, 최종개정확인일 2022-10-12, 이력 고시번호 2022-0433. 2017 확인 표현 위치: docs/topics/2026/2026-09-26-area25-s7.md 45행과 ref-814 제목(48. 안전·위험 관리 쪽 분리 페이지라 후속 정리)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "EU 기계 규정 (EU) 2023/1230 부속서 III 1.2.1(f)는 제어 시스템을, 개입과 관련해 생성된 데이터와 출시·사용 개시 뒤 업로드한 안전 소프트웨어 판의 추적 기록이 업로드 뒤 5년간 활성화되도록 설계·제작해야 한다고 정한다. 목적은 관할 국가기관의 이유 있는 요청에 따른 적합성 입증에 한정된다.",
      "tag": "사실",
      "source_ids": [
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2026-07-27 통합본 부속서 III 1.2.1 (f): \"the tracing log of the data generated in relation to an intervention and of the versions of safety software uploaded … is enabled for five years after such upload, exclusively to demonstrate the conformity … further to a reasoned request from a competent national authority\". 영역 52 의 IES 해설(ref-1109, 2026-09-30-area52-s3.md 43행) 기반 문장을 1차 원문으로 보강. 일반 작업 로그 보관 의무로 확대하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "같은 절 둘째 목록 (b)는 행동·논리가 전부 또는 일부 자체 진화하며 여러 자율성 수준으로 작동하도록 설계된 기계의 제어 시스템에 대해, 안전 기능을 보장하는 소프트웨어 기반 안전 시스템의 안전 관련 의사결정 데이터를 기록하고 수집 뒤 1년간 보존하도록 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "부속서 III 1.2.1 둘째 목록: \"Control systems of machinery … with fully or partially self-evolving behaviour or logic …\" (b) \"recording of data on the safety related decision-making process … retained for one year after its collection, exclusively to demonstrate the conformity\". 대상은 자체 진화 제어 시스템에 한정. 통합본은 M1 2024/2748·M2 2026/1744 반영",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "UL 3100(Automated Mobile Platforms, AMPs) 공식 목록은 제1판의 최초 발행일을 2021-05-26, 최근 개정일과 ANSI 승인일을 2026-06-10 으로 표시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1498"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "UL 표준 목록: \"Edition 1 (Active)\", \"Published Date: May 26, 2021 / Last Revision: June 10, 2026 / ANSI Approved: June 10, 2026\". 개정 조항 전체·시험 수치는 미열람",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "UL 3100 의 공개 적용 범위 1.4 는 산업용 로봇 자체의 요구사항은 포함하지 않으며(UL 1740·CSA Z434 가 다룸), 그 표준에 맞는 로봇 매니퓰레이터는 통합 시스템의 탑재물로 쓸 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1498"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Scope 1.4: \"This Standard does not include requirements for industrial robots, which are covered under … UL 1740 and … CSA Z434. A robotic manipulator that is in compliance with these standards may be used as the payload for the integrated system.\" 결합 시스템 인증 범위는 인증서로 따로 확인 필요",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "UL Solutions 는 2026-03-11 보도자료에서 Simbe 의 매장용 자율이동로봇 Tally 가 UL 3300(SCIEE 로봇 표준) 인증을 받았으며, 로봇과 충전 도크가 화재·감전 위험과 안전한 자율 이동 시험을 거쳤다고 발표했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1499"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 인증기관 자체 상업 발표 \"Tally earned certification to UL 3300 …\", \"The robot and its charging dock underwent extensive evaluation\". 인증서·시험보고서 미열람. 이종 플릿 전체의 안전 입증으로 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f13",
      "claim": "정부의 2025-11-27 보도참고자료(신산업 규제합리화 1호 로드맵, AI 분야)는 실외이동로봇 운행안전인증의 심사 평가항목을 16개에서 8개로 통폐합하고 심사기간을 60일에서 30일로 줄였다고('25.11 시행) 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1504"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도참고 본문 과제 표: \"(실외이동로봇)운행안전인증 심사 평가항목 통폐합 (16→8개) 및 심사기간 단축 (60→30일) ('25.11 시행)\". 메모가 근거로 든 kmcc.go.kr 로드맵 파일은 열지 못해 같은 날 정부 보도참고(fsc.go.kr 게재)로 출처를 바꿈. 쪽 번호는 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "산업통상부 고시 제2025-021호(실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정)는 2025-11-24 발령되었고 부칙에서 '발령한 날부터 시행'하므로 2025-11-24 부터 시행이다. 현행 절차·기준의 근거는 제2023-211호가 아니라 이 개정 고시다.",
      "tag": "사실",
      "source_ids": [
        "ref-1505"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "산업통상부 고시 게시물(등록일 2025-11-24) 첨부 고시문: \"산업통상부 고시 제2025-021호 … 2025년 11월 24일\", 부칙 제1조 \"이 고시는 발령한 날부터 시행한다.\" 기존 위키 '절차·기준은 고시 제2023-211호(2023-11-17)가 정한다'(2026-09-30-area50-s7.md 45행, 본 페이지 104행)의 정정 근거",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "고시 제2023-211호는 2023-11-17 발령(제정)되었다. 시행일은 원 고시 첨부 부칙이 '2023년 11월 17일부터 시행', 제2025-021호 첨부 본문에 실린 구 부칙(<제2023-211호, 2023.11.17.>)이 '2023년 11월 21일부터 시행'으로 서로 달라 확정하지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1118",
        "ref-1505"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ref-1118 첨부 HWP 부칙: \"이 고시는 2023년 11월 17일부터 시행한다.\" / ref-1505 첨부 본문: \"부칙 <제2023-211호, 2023.11.17.> 이 고시는 2023년 11월 21일부터 시행한다.\" 같은 부처의 두 원문이 다름. 독립 검증 보고는 2023-11-21 로 적었으나 원 고시 첨부와 충돌해 [추정]으로 둠",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "고시 제2025-021호 제9조①은 운행안전인증기관이 인증신청서를 접수한 날부터 30일 이내에 심사 결과를 통보하도록 정한다. 제2023-211호 제9조①에는 이 기한이 없고 심사 종료 뒤 통보만 정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1505",
        "ref-1118"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2025-021 제9조①: \"인증신청서를 접수한 날로부터 30일 이내에 신청인에게 심사 결과를 통보해야 한다.\" 2023-211 제9조①: \"심사가 종료되면 신청인에게 심사 결과를 통보해야 한다.\" 진흥원 안내 '신청일로부터 30일 이내'(ref-980, 본 페이지 98행)와 일치. 서류 보완 기간(제7조② 30일 이내)의 산입 여부는 미확인",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "고시 제2023-211호 별표 3(운행안전인증 기준)은 질량 및 폭 제한, 운행 속도, 겉모양, 동적 안정성, 비상정지, 운행구역 준수, 속도 제어, 장애물 감지, 알림음, 등화장치, 방수 성능, 물리적 보안, 횡단보도 통행, 관제장치, 통신장애 대응, 원격조작의 16개 항목을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1118"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ref-1118 첨부 HWP [별표 3] 실외이동로봇 운행안전인증 기준(제4조 관련) 항목 1~16 원문 대조. 2023-07 행정예고 보도(ref-992)의 '16가지'와 수가 일치",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "현행 고시 제2025-021호 별표 3 은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 항목을 두며, 한국로봇산업진흥원 안내의 8개 심사항목과 이름이 같다.",
      "tag": "사실",
      "source_ids": [
        "ref-1505",
        "ref-980"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ref-1505 첨부 【별표 3】 항목 1~8 원문 대조. 진흥원 페이지(재열람): \"규격 및 운행속도, 겉모양, 동적 특성 등 총 8개 심사항목\". 진흥원은 고시를 집행하는 인증기관이라 독립 교차 확인으로 세지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "두 별표를 조문으로 대조하면 구 질량·폭 제한과 운행 속도는 '규격 및 운행속도'로, 동적 안정성(5° 경사·30 mm 턱)과 속도 제어(±10 %)는 '동적 특성'으로, 운행구역 준수와 장애물 감지는 '주변 인식'으로, 관제장치와 원격조작(원격 정지·영상 확인 원격 수동조작)은 '관제장치'로 합쳐졌다. 알림음(55~73 dB(A)), 등화장치(표면 60℃ 이하), 물리적 보안(통신포트·저장장치 단자 보호)은 새 별표에 없고, 통신장애 대응(운행계획서 시나리오)은 횡단보도 통행 중 통신 단절 시 정차 조항으로만 남았다. 빠진 항목이 다른 규정으로 옮겨졌는지는 확인하지 못했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1118",
        "ref-1505"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 HWP 의 별표 3 세부 문구가 대부분 그대로 옮겨짐(예: 구 7.가 '정확도 ± 10 % 이내' = 신 3.다). 신 7.나 \"횡단보도 통행 중 통신 단절이 발생한 경우 … 안전한 곳에 정차\", 신 8.라 \"원격에서 정지할 수 있는 수단\". 알림음·등화장치·물리적 보안 문구는 신 별표 3 에 없음. 이동 여부(세부운영지침 등)는 미확인",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "본 페이지 5절이 '2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인'으로 둔 기준 예시(질량별 속도 230 kg 초과 5 km/h·100 kg 초과 10 km/h, 폭 800 mm·보도 2,500 mm 이상이면 1,200 mm, 5° 경사, 알림음 55~73 dB, 등화장치 60℃, IPX4)는 확정 고시 제2023-211호 별표 3 에 그대로 있다. 현행 제2025-021호에는 질량·폭·속도·5° 경사·IPX4 는 남고 알림음·등화장치 기준은 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1118",
        "ref-1505"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2023-211 별표 3 항목 1·2·4·9·10·11 수치 원문 대조, 2025-021 별표 3 항목 1·3·6 대조. 두 판 모두 어린이·노인·장애인 보호구역 최대 5 km/h 확인 조항 있음. 정정 대상: 본 페이지 106행",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "현행 별표 3 의 관제장치 항목은 관제장치가 운용 중인 모든 로봇을 식별하고, 모든 로봇의 위치·속력, 주행가능 거리 또는 배터리 잔량, 로봇–관제장치 통신 신호 감도, 상태(주행·대기·비상정지·오류)를 실시간으로 확인할 수 있어야 하며, 통행 불가 시 관제장치 알림과 관리자 조치, 원격 정지 수단, 영상장치로 주변을 확인하는 원격 수동조작을 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1505"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2025-021 【별표 3】 8. 관제장치 가~마. 고시 본문·별표 3 에는 관제장치의 운행 기록 저장·보관 요구 문구가 없음(oq-333 부분 근거). 이 요구를 이기종 오케스트레이션 계층이 충족하는지(oq-187)는 판단하지 않음",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "고시 제2025-021호 제10조②는 인증기관이 인증번호, 회사명, 실외이동로봇 제품명·모델명과 함께 관제장치 제품명·모델명, 소재지 등의 정보를 보관하도록 정해, 인증 정보가 로봇 모델과 관제장치 모델의 조합으로 관리됨을 보여 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-1505"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제10조②: \"인증번호, 회사명, 실외이동로봇 제품명ㆍ모델명, 관제장치 제품명ㆍ모델명, 소재지 등에 대한 정보를 별도로 보관해야 한다.\" 인증 대상이 로봇과 관제장치 조합이라는 기존 위키 내용(ref-980, 2026-09-30-area59-s6.md 41행)과 일치",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f23",
      "claim": "안전보건공단 산업안전보건인증원의 자율안전확인 대상 안내는 산업용 로봇을 직교좌표로봇을 포함해 3축 이상의 매니퓰레이터(액추에이터·교시 펜던트·제어기·통신 인터페이스 포함)를 갖추고 전용 제어기로 프로그램·자동제어가 가능한 고정식 로봇으로 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1500"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자율안전확인 대상품 안내 산업용 로봇 행: \"3축 이상의 메니퓰레이터(엑츄에이터, 교시 펜던터, 제어기 및 통신 인터페이스를 포함)를 구비하고 전용의 제어기를 이용하여 프로그램 및 자동제어가 가능한 고정식 로봇\". AMR·AGV 전체를 같은 대상으로 보지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Sanders 외(2024)가 분석한 OSHA 중상 보고(SIR)의 기간은 2015-01-01 부터 2022-04-30 까지다.",
      "tag": "사실",
      "source_ids": [
        "ref-1122"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "저자 공개 원고(White Rose) p.5 137–138행: \"January 1, 2015 through April 30, 2022\". 2024 발표를 2024년까지의 집계로 읽지 않음. 기존 위키(s4.md 45행, s8.md 42행)의 '2015~2022년' 보강",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "같은 연구는 SIR 이 연방 OSHA 관할 사업장의 보고만 담고 자체 주 계획(State Plan)을 운영하는 22개 주의 사업장은 포함하지 않는다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1122"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원고 133–136행(연방 OSHA 관할, 주 계획 22개 주 제외). 메모의 'OSHA 대시보드는 업무상 사망을 포함하지 않는다'(OSHA 페이지)는 403 으로 확인하지 못해 넣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "같은 연구에서 분석한 사고 서술의 단어 수 중앙값은 36 단어였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1122"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원고 p.13 332행: \"median word count was 36\". 선별된 77건 보고의 서술 길이이며 원인 정밀도나 발생률을 뜻하지 않음. 기존 '서술이 더 구조화되고 상세해야 한다'(s3.md 41행) 결론의 근거 수치",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "Suresh 외(American Journal of Industrial Medicine 69(5), 2026)는 Ohio 산재보상국(OHBWC) 자료에서 2001~2020년 로봇 관련 산재보상 청구 1,076건을 키워드 검색으로 찾았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1501"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 Results: \"From 2001 to 2020, 1076 robot-related claims were identified\". Methods: OHBWC 데이터베이스 키워드 검색. 서지 69(5):345–357, 인쇄 2026-05, 온라인 2026-03-03(Crossref). 로봇 노출 노동자당 발생률이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "초록 기준으로 이 청구의 85% 가 의료비만 청구(의료 처치만 또는 휴업 7일 이하)였고, 청구의 75.7% 가 공유 작업공간에서 협동 적용 로봇 팔을 다루는 작업과 관련됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1501"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: \"85% medical-only claims (medical care only and/or ≤ 7 days away from work)\", \"Most claims involved working with robotic arms for collaborative applications (75.7%) in a shared workspace\". 메모의 'n = 917(85.2%)'과 '발생률을 계산하지 못함(§4.1)'은 본문 미열람으로 확인하지 못해 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "안전보건공단 공개 재해사례(광주 광산구 사업장)는 로봇 용접기의 용접 팁 교체 작업자가 작동 중인 로봇 팔과 지그 사이에 흉부가 끼어 숨진 사고의 원인을 두 가지로 든다: 일시중지(muting) 기능 사용으로 감응식 방호장치가 작동하지 않은 것, 로봇 운전을 정지하지 않고 안전 조치가 없는 재료 투입구로 셀에 들어간 것.",
      "tag": "사실",
      "source_ids": [
        "ref-1502"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "재해발생원인: \"일시중지(muting) 기능 사용으로 방호장치 미작동\", \"로봇을 정지시키지 않은 상태에서 안전 조치가 구축되지 않은 재료 투입구 공간을 통해 셀 내부로 들어가 작업\". 발생일 미기재. 고성·오뚜기 사건과 다른 사건",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f30",
      "claim": "같은 사례의 재발방지대책은 출입 시 감응식 방호장치가 작동하도록 하고 muting 사용 시 다른 수단으로 안전이 유지되도록 관리하며, 수리·점검 같은 비정형 작업은 로봇 운전을 정지한 뒤 출입문으로 들어가 하라고 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1502"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "재발방지대책: \"일시중지(muting) 사용시 다른 수단에 의하여 안전이 유지되도록 관리\", \"수리·점검 등 비정형적 작업을 하는 경우에는 해당 로봇의 운전을 반드시 정지한 후, 출입문으로 진입\". 사례 대책 표현이며 muting 구현 인증 지침은 아님",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": "제약"
    },
    {
      "id": "f31",
      "claim": "Leveson 의 MIT OCW 강의 자료(16.863J System Safety, 2016년 봄 학기) 'CAST 분석'은 SO2 탱크 넘침 사례에서 안전 핵심 장비가 오랫동안 작동하지 않은 이유, 그런 상태로 공장을 운전하는 정책과 위험성평가 여부, 점검·정비 정책을 조사 질문으로 던진다.",
      "tag": "사실",
      "source_ids": [
        "ref-1506"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "슬라이드 6 Questions: \"What types of policy existent about operating plant with non-functioning safety equipment? Is risk assessment done when this occurs?\", \"What is maintenance policy? Why was safety-critical equipment non-operational …\". '2016'은 강의 학기이며 사고 연도가 아님. 로봇 적용 실증 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "같은 강의는 운전원 수준 분석 항목으로 맥락·시스템 요인과 정신 모형의 결함을 두고, 사후 판단 편향(hindsight bias)을 경계한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1506"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "슬라이드 10: \"Contextual and systemic factors\", \"Mental model flaws\"; 슬라이드 7 제목 \"Hindsight Bias at Operator Level\"",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "Webb 외(2021)는 2020년 11월 같은 연구자 한 명이 Zoom 으로 가상 목격자 증언(VWT) 역할극 면담 22회를 진행했으며, 실제 사고가 아닌 삽화 시나리오를 보여 주는 방식이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1121"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Results 도입: \"In November 2020 we conducted a first set of 22 VWT role-play interviews … conducted over an online teleconferencing platform (Zoom)\". 실제 사고·실제 고령자 목격자 조사가 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "연구진은 정지 이미지를 써서 시나리오의 동적인 부분을 효과적으로 전달하지 못했다고 한계를 밝혔다(예: 로봇이 거주자 다리와 부딪혔을 가능성을 시사하는 움직임).",
      "tag": "사실",
      "source_ids": [
        "ref-1121"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Discussion: \"the use of static images meant we could not convey the more dynamic parts of the scenario effectively\". 면담에서 충돌 언급이 적은 것을 실제 충돌 부재의 증거로 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "윤리적 블랙박스 초안(ICRES 2022 게재본 부록, RFC Draft 0.1)은 날짜 필드 ebbD 의 길이를 표에서는 10자, MD 기록 주석 2 에서는 12 ASCII 문자로 다르게 적고, 시각 필드도 표와 주석이 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-1503"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "게재본 Table 3 \"ebbD EBB date record written 10 chars\" vs MD note 2 \"The EBB date field ebbD is 12 ASCII characters\"(시각 필드는 Table 2 12자 vs note 3 10자). 초안 내부 표기 충돌이며 규범 값을 정하지 않음. 기존 위키 '기록할 데이터 형식 … 미확인'(2026-09-30-area50-s6.md 45행) 보강",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "같은 초안의 체크섬 표기는 표 2 의 4 문자, 표 3 의 8자리 16진수, 주석 4 의 '64비트 비암호학적 해시(추후 결정)'로 서로 맞지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1503"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Table 2 \"Checksum 4 chars ASCII\", Table 3 \"chkS checksum for complete record 8 hexadecimal chars\", note 4 \"64-bit … hash function, to be determined\". 변조 방지 보장 근거로 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "초안은 로봇 결정 코드의 숫자값 정의를 표준 범위 밖으로 두고 로봇 제조사나 운영자에게 맡긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1503"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RD note 8: \"outside the scope of this standard, and left to the robot's manufacturer or operator\". 제조사 간 결정 의미를 통일한 규약이 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "초안의 로봇 데이터(RD) 기록은 저장 한도에 이르면 가장 오래된 RD 기록부터 덮어쓰는 순환 구조이며, 고정 보존 기간을 정하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1503"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "부록 A.4: \"write the next RD record overwriting RD record 1, and write subsequent RDs …\". 보존 기간 조항 없음. 사고 시 보존 잠금은 초안에 없음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "rosbag2 0.35.0 README 의 --repeat-transient-local 옵션은 지정 토픽의 최근 N개(기본 1개) 메시지를 보관했다가 분할로 새 파일이 시작되거나 스냅샷을 쓸 때 앞에 다시 넣는다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "태그 0.35.0 README: \"tells the recorder to retain the last N messages for specified topics and prepend them when a new bag file starts (on split) or when a snapshot is written\", \"If omitted, the default depth is 1\". 0.35.0 CHANGELOG 날짜 2026-09-12. 정적 TF·지도 보존은 depth 설정에 종속",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "같은 판의 스냅샷 모드는 메시지를 바로 디스크에 쓰지 않고 --max-cache-size(바이트)와 선택적 --max-cache-duration(초)로 제한한 메모리 순환 버퍼에 두었다가 요청 시(~/snapshot 서비스) 디스크에 저장한다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README Snapshot mode: \"keeps an in-memory circular buffer bounded by --max-cache-size (bytes) and optionally --max-cache-duration (seconds). The entire buffer can be dumped to disk on request\". 사고 전 기록 길이는 설정·유입량에 종속, 무제한 보존 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "rosbag2 의 유실 메시지 통계는 증분 방식이라 유실이 0인 토픽은 이벤트에 들어가지 않고, 내부 카운터는 이벤트를 발행할 때마다 0으로 재설정된다.",
      "tag": "사실",
      "source_ids": [
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README Statistics about lost messages: \"the statistics are incremental, and message lost event doesn't include topics with zero number of lost messages … inner counters reset to zero after each event has been published\". 이벤트 미수신을 유실 0 으로 단정할 수 없음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "MCAP 명세는 Message 레코드의 publish_time 을 '발행 시각, 알 수 없으면 log_time 으로 설정해야 한다(must)'고 정한다. 따라서 publish_time 이 log_time 과 같으면 실제 발행 시각인지 대체값인지 포맷만으로 구분되지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1096"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "고정 커밋 f7069e6 명세 Message: \"publish_time … Time at which the message was published. If not available, must be set to the log time.\" log_time·publish_time 구분 자체는 기존 위키(design-and-simulation/index.md 100행). 새 내용은 대체 규칙",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "MCAP 명세는 Chunk 의 uncompressed_crc 와 여러 레코드의 crc 값이 0 이면 'CRC 검증을 수행하지 않아야 한다(should not)'는 뜻으로 정한다. CRC 는 오류 검출용이며 서명이나 증거 인계를 보장하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1096"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 Chunk: \"uncompressed_crc … A value of zero indicates that CRC validation should not be performed.\" 다른 레코드 crc 필드에도 같은 문구. 강도는 must 가 아닌 should",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "표준 레지스트리는 발행판(ISO 3691-4:2023)과 개발 중 프로젝트(ISO/DIS 3691-4 제3판), 국내 부합판(KS B ISO 10218-1·-2, ISO 10218:2011 IDT)과 국제 최신판(ISO 10218:2025), EU 조화 게재(지침 2006/42/EC 기반, 2027-01-20 폐지 예정 목록)를 별도 속성으로 두고, 배포 설정에는 현장 승인된 판을 고정해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-789",
        "ref-1497",
        "ref-211",
        "ref-1496"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2·f5~f7 에서 도출. 국제판 개정만으로 현장 인용판을 자동 치환하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "실외이동로봇 인증 정보는 고시 번호·시행일(제2025-021호, 2025-11-24)과 별표 판(16항목/8항목)을 함께 기록하고, 구 별표로 받은 인증과 현행 별표 기준을 구분해야 한다. 현행 관제장치 항목의 실시간 상태(위치·속력·배터리·통신 감도·상태)와 원격 정지는 ROP 가 이종 로봇 상태 모델로 받아야 할 최소 항목으로 쓸 수 있다.",
      "tag": "의견",
      "source_ids": [
        "ref-1505",
        "ref-1118"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f14·f17~f22 에서 도출. ROP 계층이 인증상 관제장치인지(oq-187)는 판단하지 않음",
      "as_of": "2026-10-11",
      "site_type": "실외",
      "flow_item": "수행 자원"
    },
    {
      "id": "f46",
      "claim": "EU 부속서 III 1.2.1 의 5년·1년 기록 의무는 안전 소프트웨어 개입·판 이력과 자체 진화 제어의 안전 결정 데이터에 한정되므로, ROP 는 인증 증거용 이력과 일반 작업 로그를 나눠 보존 정책을 정하고 플릿 전체 데이터를 일률적으로 5년 또는 1년 보관해야 한다고 해석하지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-555"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8·f9 에서 도출. 적용 여부는 제품·제어 시스템별 검토 필요",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f47",
      "claim": "사고 자료 레코드에는 출처별 관할(연방 OSHA 관할만 등), 관측 기간, 집계 단위(보고 건수·부상 수·보상 청구), 중증도 정의, 노출 분모 유무를 필드로 두어 OSHA SIR 과 Ohio 보상 청구 같은 서로 다른 모집단을 합산·비교하지 않게 해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1122",
        "ref-1501"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f24~f28 에서 도출",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f48",
      "claim": "EBB 초안을 공통 기록 스키마로 쓰기 전에 날짜·시각·체크섬 표기 충돌을 해소하고, ROP 쪽에서 제조사 원본 결정 코드·공통 사건 유형·코드표 판·시각 기준·사고 시 보존 잠금을 따로 정의해야 한다. 기록기 쪽에서는 사고 트리거 스냅샷, 정적 토픽 재삽입 depth, 유실 이벤트 수신 여부, MCAP publish_time 대체 여부와 원본 해시·추출 이력을 증거 메타데이터로 함께 남겨야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1503",
        "ref-1120",
        "ref-831",
        "ref-1096"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f35~f43 에서 도출. 현장 재현 시험(기록기 장애·캐시 소진·이벤트 누락)은 이번에 하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f49",
      "claim": "CAST 의 조사 질문을 플릿 사고에 옮기면, 사건 시간선 뒤에 제조사·통합자·현장 운영자·관제자 각각의 제어 책임, 당시 관측 가능했던 정보, 방호장치 우회(muting)와 정비·승인 정책을 따로 조사하고, '교육 부족' 같은 결론을 증거 없이 먼저 정하지 않는 절차가 필요하다.",
      "tag": "의견",
      "source_ids": [
        "ref-1506",
        "ref-1502"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f29~f32 에서 도출. 로봇 사고에 CAST 를 적용한 실증은 이번에 확인하지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1496",
      "org": "European Commission (Official Journal of the European Union)",
      "title": "Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC",
      "published": "2026-09-07",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "EN ISO 10218-1/-2:2025 참조를 기계류 지침 2006/42/EC 조화 표준 목록(2023/1586 부속서 I)에 추가한 시행결정(OJ L 2026/2015). 제2조로 2023/1586 을 2027-01-20 부로 폐지한다. Publications Office 공식 원문으로 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1497",
      "org": "국가기술표준원 (국가표준인증 통합정보시스템)",
      "title": "KS B ISO 10218-1 로봇 및 로봇장치 ─ 산업용 로봇의 안전에 관한 요구사항 ─ 제1부: 로봇",
      "published": "2021-11-26",
      "url": "https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS 상세 목록. 대응 국제표준 ISO 10218-1:2011(IDT), 제정 2008-01-17, 최종개정확인일 2021-11-26. 표준 본문은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1498",
      "org": "UL Standards & Engagement",
      "title": "UL 3100 Automated Mobile Platforms (AMPs)",
      "published": "2026-06-10",
      "url": "https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=39063",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "UL 3100 공식 목록. 제1판(2021-05-26 발행)의 최근 개정·ANSI 승인 2026-06-10, 적용 범위 1.1·1.4(산업용 로봇 제외, 매니퓰레이터 탑재 가능)를 공개한다. 개정 조항 전체는 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1499",
      "org": "UL Solutions",
      "title": "UL Solutions Grants Its First Global Certification for a Public-Facing Robot to Simbe's Tally Autonomous Mobile Robot",
      "published": "2026-03-11",
      "url": "https://www.ul.com/news/ul-solutions-grants-its-first-global-certification-public-facing-robot-simbes-tally-autonomous",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "인증기관의 상업 보도자료. Simbe Tally 로봇·충전 도크의 UL 3300 인증 취득을 발표한다. 인증서·시험보고서는 공개되지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1500",
      "org": "안전보건공단 산업안전보건인증원",
      "title": "자율안전확인 대상품 (자율안전확인신고 대상 및 적용범위)",
      "published": null,
      "url": "https://miis.kosha.or.kr/oshci/busi/viewMiisJayulMerchandiseInfo.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "자율안전확인 대상 기계·기구 안내. 산업용 로봇을 3축 이상 매니퓰레이터와 전용 제어기를 갖춘 고정식 로봇으로 정의한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1501",
      "org": "Suresh, V., Konda, S., Haney, J. M. 외 (American Journal of Industrial Medicine 69(5))",
      "title": "Robot-Related Workers' Compensation Claims in Ohio, 2001–2020",
      "published": "2026-05",
      "url": "https://stacks.cdc.gov/view/cdc/258698",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "NIOSH 연구진의 Ohio 산재보상 청구 분석(pp.345–357, 온라인 2026-03-03, DOI 10.1002/ajim.70067). 이번에는 CDC Stacks 서지·초록만 확인했고 본문 PDF 는 열지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1502",
      "org": "안전보건공단",
      "title": "산업용 로봇 팔과 지그 사이에 끼임 (재해사례)",
      "published": null,
      "url": "https://oshri.kosha.or.kr/kosha/data/machine.do?articleNo=411924&attachNo=233368&mode=download",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공개 재해사례 1쪽. 용접 팁 교체 중 끼임 사망의 원인(muting 사용으로 방호장치 미작동, 운전 정지 없이 셀 진입)과 재발방지대책을 적는다. 발생일은 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1503",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본)",
      "published": "2022-07",
      "url": "https://doi.org/10.13180/icres.2022.18-19.07.019",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "윤리적 블랙박스 공개 표준 초안의 학회 게재본(pp.99–110, 부록 RFC Draft 0.1 포함). 같은 연구의 arXiv 판은 ref-1120. 필드 표·주석과 RD 덮어쓰기 구조를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.clawar.org/icres2022/wp-content/uploads/2022/07/ICRES2022-Proceedings-manuscript.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1504",
      "org": "관계부처 합동 (금융위원회 누리집 게재 보도참고자료)",
      "title": "규제의 벽은 허물고 AI의 길은 넓힌다 — 신산업 규제합리화 1호 로드맵(AI 분야) 발표",
      "published": "2025-11-27",
      "url": "https://www.fsc.go.kr/no010101/85753",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "정부의 AI 분야 규제합리화 로드맵 보도참고자료. 실외이동로봇 운행안전인증 심사 평가항목 16→8개 통폐합과 심사기간 60→30일 단축('25.11 시행)을 적는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1505",
      "org": "산업통상부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정)",
      "published": "2025-11-24",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "2025-11-24 발령·시행된 일부개정 고시. 첨부 본문에서 제9조① 30일 통보 기한, 제10조② 관제장치 모델 정보 보관, 별표 3 의 8개 인증 기준 항목을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1506",
      "org": "Leveson, N. (MIT OpenCourseWare, 16.863J System Safety)",
      "title": "System Safety: CAST Analysis (강의 자료)",
      "published": "2016",
      "url": "https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/7dc4344ef259e4bde4acc1bb2d578a95_MIT16_863JS16_LecNotes3-2.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "2016년 봄 학기 강의 슬라이드. SO2 탱크 넘침 사례로 CAST 조사 질문(정비 정책·안전 장비 비가동 운전)과 운전원 분석 항목(맥락·시스템 요인, 정신 모형 결함)을 보여 준다. 2016 은 강의 학기다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1255",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications",
      "published": "2026-04-23",
      "url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "R15.08 Part 3 판매 페이지(기존 출처). 이번 재열람은 Cloudflare 차단으로 실패했고 발행일은 2026-10-09 열람 기록 기준이다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-789",
      "org": "ISO",
      "title": "ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": null,
      "url": "https://www.iso.org/standard/88615.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 3691-4 차기판(제3판) 프로젝트 페이지. 2026-10-11 위원회 페이지 기준 ISO/DIS, 단계 40.60(2026-09-10 투표 종료), ISO 3691-4:2023 대체 예정. 기존 'ISO/CD' 제목을 갱신한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://committee.iso.org/standard/88615.html",
      "source_unopened": false
    },
    {
      "id": "ref-211",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합",
      "published": "2022-10-12",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010083660",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B ISO 10218-2 목록(기존 출처). 이번에 국가표준인증 통합정보시스템 상세에서 ISO 10218-2:2011 IDT, 최종개정확인일 2022-10-12(고시 2022-0433)를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-2&menuId=919&reformNo=&tmprKsNo=KSBISO10218-2&topMenuId=502&upperMenuId=503",
      "source_unopened": false
    },
    {
      "id": "ref-555",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery",
      "published": "2023-06",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "EU 기계 규정. 이번에 2026-07-27 통합본(M1 2024/2748, M2 2026/1744 반영)에서 부속서 III 1.2.1(f) 5년 추적 기록과 둘째 목록 (b) 1년 보존, 제54조 적용일을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02023R1230-20260727",
      "source_unopened": false
    },
    {
      "id": "ref-1122",
      "org": "Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121)",
      "title": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports",
      "published": "2024",
      "url": "https://eprints.whiterose.ac.uk/id/eprint/217393/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OSHA 중상 보고 로봇 관련 사고 분석(기존 출처). 이번에 저자 공개 원고에서 분석 기간(2015-01-01~2022-04-30), 연방 관할 범위, 서술 단어 수 중앙값 36 을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eprints.whiterose.ac.uk/id/eprint/217393/1/Robot-Related%20Injuries.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1120",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "윤리적 블랙박스 초안의 arXiv 판(기존 출처). 이번에는 다시 열지 않았고, 필드 세부는 학회 게재본(ref-1503)으로 확인했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1121",
      "org": "Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI)",
      "title": "Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions",
      "published": "2021-06-29",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "역할극 증언 면담 연구(기존 출처). 이번에 2020-11 Zoom 면담 22회와 정지 이미지 한계를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (ros2/rosbag2 GitHub)",
      "title": "rosbag2 — README (Recording and playback of ROS 2 communications)",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rosbag2 README(기존 출처). 이번에 태그 0.35.0 판(rosbag2_transport CHANGELOG 0.35.0 = 2026-09-12)에서 repeat-transient-local, 스냅샷 모드 순환 버퍼, 유실 메시지 통계를 확인했다. 태그 커밋 날짜는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/rosbag2/0.35.0/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1096",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "MCAP 포맷 명세(기존 출처). 이번에 커밋 f7069e6 고정판에서 publish_time 대체 규칙과 CRC 0 의미를 확인했다. 고정 커밋 날짜는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/foxglove/mcap/f7069e637d66460b138bde275cefcd9021e64a78/website/docs/spec/index.md",
      "source_unopened": false
    },
    {
      "id": "ref-1118",
      "org": "산업통상자원부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시",
      "published": "2023-11-17",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "고시 제2023-211호(2023-11-17 제정, 기존 출처). 이번에 첨부 HWP 에서 별표 3 의 16개 기준 항목과 제9조, 부칙('2023년 11월 17일부터 시행')을 확인했다. 현행은 제2025-021호(ref-1505)로 개정됐다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1116",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "EN ISO 10218:2025 조화 게재를 해설한 컨설팅사 글(기존 출처). PL d·범주 3 대체와 정상 정지 요구 서술의 단독 근거다. 이번에는 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "인증기관 안내 페이지(기존 출처). 이번 재열람에서 8개 심사항목과 '인증 신청일로부터 30일 이내' 처리기간을 다시 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "sections": [
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 4(분리 2026-09-30-area50-s4) — '적합성 추정' 항목(41행)을 IBF 해설 대신 관보 원문으로 보강(f1)하고 지침 2006/42/EC 기반 목록이 2027-01-20 폐지됨을 덧붙임(f2). '중상 보고' 항목(45행)의 기간을 2015-01-01~2022-04-30 로(f24), 연방 관할 한정(f25) / 섹션 5 — 실외 사례: 104행 '고시 제2023-211호(2023-11-17)로 정해졌고'를 현행 제2025-021호(2025-11-24 발령·시행, f14)로 정정하고 제2023-211호 시행일은 두 원문이 달라 확정하지 않음(f15 [추정], 독립 검증 보고의 2023-11-21 과도 다름); 100행 제약 칸과 106행 W19 문장('8개와 16가지로 달라 어느 쪽도 고르지 않고')을 '구 고시 별표 3 16개(f17) → 현행 별표 3 8개(f18), 2025-11 통폐합(f13)'으로 정정하고 항목 대응·빠진 항목(알림음·등화장치·물리적 보안, 다른 규정 이동 여부 미확인)을 f19 로; 106행 '확정 고시 별표 원문 미확인' 기준값은 2023-211 별표 3 에 있음과 현행 잔존 여부(f20); 98행 30일 처리기간에 제9조① 근거(f16)·60→30일 경위(f13). 제조 공장: 공식 재해사례(용접 팁 교체 끼임, muting 우회·운전 정지 미실시, f29·f30)를 사례로 추가하되 고성·오뚜기 기사 사건과 연결하지 않음; 의견 f45·f49 / 섹션 6(분리 2026-09-30-area50-s6) — '사고 기록 장치' 소절 45행 '형식과 보존 기간 … 미확인'을 EBB 초안 게재본 내용으로 보강: 날짜·시각 필드 충돌(f35), 체크섬 충돌(f36), 결정 코드 제조사 위임(f37), RD 순환 덮어쓰기·보존 기간 없음(f38). 조직·제어 분석 방법 CAST 소절 추가(f31·f32, 2016 은 강의 학기이며 사고 연도 아님); 의견 f48·f49 / 섹션 7(분리 2026-09-30-area50-s7) — 42행 EN ISO 10218 EU 조화 게재 행: 게재 사실·날짜·법적 기반은 관보 원문(f1·f2)으로, PL d·범주 3 대체·정상 정지 서술은 IBF 단독 근거라 [사실]→[추정]·벤더 해설로 강등(f3). 45행 실외이동로봇 행 '절차·기준은 고시 제2023-211호(2023-11-17)가 정한다'→ 제2023-211호를 제2025-021호가 2025-11-24 개정·시행(f14), 심사항목 구판 16·현행 8(f17·f18). R15.08-3 행 추가(f4 [추정], 발행 사실은 기존 내용 확인 — safety/index.md 53행, 재추가 아님). ISO/DIS 3691-4 제3판 40.60(2026-09-10) 행(f5) — ref-789 제목을 'ISO/DIS 3691-4 (제3판)'으로 갱신. KS 부합판 ISO 10218-1/-2:2011 IDT(f6·f7). EU 기계 규정 부속서 III 1.2.1(f) 5년 추적 기록(f8: 영역 52 의 IES 해설 기반 문장 2026-09-30-area52-s3.md 43행을 1차 원문으로 보강)과 자체 진화 제어 1년 보존(f9). UL 3100 판·범위(f10·f11), UL 3300 Tally 인증은 벤더 주장(f12 [추정]). 자율안전확인 대상 정의(f23). rosbag2 0.35.0 repeat-transient-local·스냅샷·유실 통계(f39~f41, 기능 일반은 ref-831 기존 내용), MCAP publish_time 대체 규칙·CRC 0(f42·f43, log_time/publish_time 구분 자체는 design-and-simulation/index.md 100행 기존 내용); 의견 f44·f46 기존 내용 확인(새로 넣지 않음): EU 기계 규정 일반 적용일 2027-01-20(2026-09-25-area26-s7.md 55행, 2026-09-30-area52-s3.md 43행), 제54조 (b) 제50조(1) 2026-10-20(safety-and-risk-management.md 142행, 2026-10-11 게시), R15.08-3 발행일(safety/index.md 53행) / 섹션 8(분리 2026-09-30-area50-s8) — Sanders 외 항목(42행)에 기간(f24)·연방 관할 한정(f25)·서술 단어 수 중앙값 36(f26). Suresh 외 2026 AJIM 69(5):345–357 추가(f27·f28: 85% 는 초록 수치, n=917·발생률 미산출 서술은 미확인이라 쓰지 않음). Webb 외 항목(41행)에 2020-11 Zoom 22회(f33)와 정지 이미지 한계(f34); 의견 f47 / 섹션 9 — 업종별 조건 행: 실외 인증의 관제장치 요구(실시간 상태·원격 정지, f21)와 인증 정보의 관제장치 모델 단위(f22)를 인증 상태 등록 근거로; 의견 f45 / 섹션 11(분리 2026-09-30-area50-s11) — 해결 제안: oq-230(구판 16·현행 8 이 모두 항목 단위이며 세부 목록 확인, f17·f18·f19), oq-384(ISO/DIS 3691-4 제3판 40.60, f5). 부분 답: oq-186(시점·근거 고시 f13·f14, 경사로→동적 특성, 알림음·등화장치는 새 별표에 없음 f19; 다른 규정 이동 여부가 남아 열린 채 둠), oq-251·oq-123(KS 는 여전히 2011 IDT, f6·f7), oq-252(f8·f9·f35~f43), oq-333(관제장치 항목에 기록 보관 요구 문구 없음, f21), oq-187(관련 근거 f22). 답하지 못함: oq-170, oq-253, oq-254, oq-265. 메모의 '새 질문' 4건은 문구 대조로 기존 oq-251~oq-254 와 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 중 '별표 구·신 대응표'는 f19 로 대부분 답해져 만들지 않고 남은 부분은 oq-186 에 둠; EBB·스냅샷 검증·MCAP 증거 표시 3건과 제2023-211호 시행일 출처 충돌, 2023/1230 조화 게재 시점 질문을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/topics/2026/2026-09-26-area25-s7.md 45행 'KS B ISO 10218-2 … 2017 확인' → 2022-10-12 확인(f7)과 ref-814 제목, docs/categories/safety/index.md 177행(IBF 단독 근거 [사실]·'산업통상자원부 고시(2023-11-17)로 정해졌다')을 f1·f2·f14 로 정리, 2026-09-30-area52-s3.md 43행에 f8 1차 근거 연결. 다음 실행 후보: 66. 실외(f17~f22), 59. 법·규제·보험·라이선스(f2·f8·f9·f14), 37. 관제 화면·실행 기록(f21·f39~f43)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "윤리적 블랙박스 초안의 날짜·시각·체크섬 표기 충돌을 해소한 후속 판이 있는가, 서로 다른 제조사의 로봇 결정 코드를 공통 사건 유형으로 옮기는 공개 매핑이 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 37. 관제 화면·실행 기록 | 근거: f35 | 종류: 일반",
    "rosbag2 스냅샷·repeat-transient-local·유실 통계를 쓴 사고 전후 기록을 현장 설정(스냅샷 트리거 지연, 전원 상실, 정적 토픽 depth, 유실 이벤트 누락)에서 시험해 보존 길이와 누락을 검증한 사례가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 43. 데이터·관측성·배포 | 근거: f40 | 종류: 일반",
    "MCAP 의 publish_time 이 log_time 으로 대체된 경우와 원본 추출·해시·서명 이력을 사고 증거 묶음에 어떻게 표시하고 검증할 것인가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 38. 모니터링·이상 탐지·원인 분석 | 근거: f42 | 종류: 일반",
    "출처 충돌: 실외이동로봇 운행안전인증 고시 제2023-211호의 시행일은 원 고시 첨부 부칙(2023-11-17)과 제2025-021호 첨부 본문에 실린 구 부칙(2023-11-21) 가운데 어느 쪽인가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 66. 실외 | 근거: f15 | 종류: 출처 충돌",
    "EN ISO 10218-1/-2:2025 참조는 기계 규정 (EU) 2023/1230 의 조화 표준으로 언제 게재되며, 지침 2006/42/EC 기반 목록(시행결정 2023/1586)이 2027-01-20 폐지된 뒤 적합성 추정은 어떻게 이어지는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스 | 근거: f2 | 종류: 일반"
  ],
  "open_questions_resolved": [
    "oq-230",
    "oq-384"
  ],
  "self_check": {
    "source_count": 23,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-06/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f4: A3 R15.08-3 판매 페이지 재열람 실패(Cloudflare) — 발행일은 기존 ref-1255(2026-10-09 열람) 기준이라 [추정]",
      "f15: 고시 제2023-211호 시행일 — 원 고시 첨부 HWP 부칙 '2023년 11월 17일부터 시행'과 제2025-021호 첨부 본문의 구 부칙 '2023년 11월 21일부터 시행'이 충돌. 독립 검증 보고(2023-11-21)와도 달라 확정하지 않음",
      "f19: 2023-211 별표 3 의 알림음·등화장치·물리적 보안과 통신장애 대응(운행계획서 시나리오)이 세부운영지침 등 다른 규정으로 옮겨졌는지 미확인",
      "f13: 메모가 든 kmcc.go.kr 로드맵 파일(인쇄 p.50)은 열지 못해 같은 날 정부 보도참고(fsc.go.kr, ref-1504)로 출처를 바꾸고 쪽 번호를 삭제",
      "f27·f28: Suresh 외는 CDC Stacks 초록·Crossref 서지만 확인(본문 PDF 열람 실패). 메모의 'n = 917(85.2%)'·'발생률 미산출(§4.1)'은 미확인이라 쓰지 않음",
      "메모 F19(OSHA SIR 대시보드는 업무상 사망 제외)는 osha.gov 403 으로 확인하지 못해 넣지 않음(연방 관할 한정은 Sanders 원고로 f25)",
      "f10·f11: UL 3100 은 공식 목록의 판·범위만 확인, 2026 개정 조항 전체·시험 수치 미확인. f12: Tally UL 3300 인증서·시험보고서 미확인(벤더 주장)",
      "f3: ISO 10218:2025 원문 미열람이라 IBF 해설의 PL d·범주 3·정상 정지 서술이 틀렸다고 판단한 것이 아니라 근거 수준만 낮춤",
      "f39~f43: rosbag2 0.35.0 태그 대상 커밋 날짜와 MCAP 고정 커밋(f7069e6) 날짜는 확인하지 못해 published null. 현장 무유실 성능은 시험하지 않음",
      "f6·f7: KS 목록에서 ISO 10218:2025 부합 KS 를 찾지 못했으나 후속 고시 전수 부재를 증명한 것은 아님(oq-251 부분 답)",
      "oq-170(ISO 3691-4:2023 원문 플릿 정보 요구), oq-253(국내 고정형·이동형 분리 재해 통계), oq-254(ISO/FDIS 13482 플릿 요구), oq-265(R15.08-3 사용자 의무)는 이번 메모가 답하지 못함",
      "메모가 2026-10-11 기준 위키 진단에 쓴 고정 커밋과 배포 페이지의 동일성, 오뚜기·고성 사고의 공식 최종 원인, 국내 실외운행인증 최신 누계는 확인하지 못함"
    ],
    "scope_violations": [
      "f8·f9·f2: EU 기계 규정·조화 표준의 법적 효력 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 개별 제품의 적용 여부는 판단하지 않음",
      "f39~f43: rosbag2·MCAP 기록 기능은 37. 관제 화면·실행 기록, 43. 데이터·관측성·배포와 겹치며, 이 영역에는 사고 조사 증거 보존 관점으로만 씀",
      "f17~f22: 실외이동로봇 인증 기준은 66. 실외와 겹치며, 이 영역에는 인증 근거·항목 변화와 ROP 가 받는 관제장치 요구로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 11
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 11건/15(ref-1496~ref-1506, 예약 구간 ref-1496~ref-1525 안), 재사용 12건(ref-1255·ref-789·ref-211·ref-555·ref-1122·ref-1120·ref-1121·ref-831·ref-1096·ref-1118·ref-1116·ref-980). 출처 매핑(검증 결과 기준): 메모 n1→ref-1496, n2→ref-1255(미열람), n3→ref-1497, n4→ref-211(standard.go.kr 상세로 열람; ref-814 는 '2017 확인' 제목이라 쓰지 않음), n5→ref-789(제목 ISO/DIS 3691-4 (제3판)으로 갱신), n6→ref-555(2026-07-27 통합본), n7→ref-1498, n8→ref-1499(벤더 문서), n9→ref-1500, n10→ref-1122(White Rose 원고), n11→ref-1501(초록만), n12(OSHA SIR 페이지)는 403 이라 출처에서 뺌, n13→ref-1502, n14→ref-1503(ICRES 게재본, DOI 10.13180/icres.2022.18-19.07.019; arXiv 판 ref-1120 은 미재열람), n15→ref-1121, n16→ref-831(0.35.0 태그 raw), n17→ref-1096(고정 커밋 raw), n18→ref-1504(kmcc.go.kr 대신 fsc.go.kr 보도참고 85753), n19→ref-1505(첨부 본문·별표 3 열람), n20→ref-1506. 추가 재사용: ref-1118(2023-211 첨부 HWP 별표 3·부칙), ref-1116(강등 대상 해설, 미재열람), ref-980(진흥원 8개 항목 재열람). fetched: false 는 ref-1255·ref-1120·ref-1116. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: 고시·진흥원·로드맵은 정부 계열, EBB·Webb 은 RoboTIPS 계열) — 신뢰도 medium 이하. 중복 제거: 메모 F07(일반 적용일)·F08(제50조(1) 2026-10-20, 2026-10-11 게시된 safety-and-risk-management.md 142행)·F03(R15.08-3 발행일)은 기존 위키에 있어 rationale 에 위치만 적고 F03 만 7절 행 근거로 [추정] f4 에 남김. 메모 F19·F22 는 확인 불가로 넣지 않음. 검증 반영: F13 출처 교체·쪽 번호 삭제, F15 시행일 2025-11-24·고시 번호 제2025-021호, 별표 3 원문(구 16·신 8)으로 W19·W82 정정, F02 에 2023/1586 2027-01-20 폐지 보완, W78 강등(f3), F04 로 oq-384 해소·ref-789 제목 갱신, F17 행 번호 137–138, F23 원인 2개·장소, F25 '2016'=강의 학기, F37 should 강도, F21 은 초록 85% 만, X01 벤더 주장 [추정]. 검증 보고와 다르게 둔 것: 제2023-211호 시행일(검증 보고 2023-11-21)은 원 고시 첨부 부칙(2023-11-17)과 충돌해 f15 [추정]과 출처 충돌 질문으로 남김. 열린 질문: 해결 제안 oq-230·oq-384, 부분 답 oq-186·oq-251·oq-123·oq-252·oq-333·oq-187. 메모의 새 질문 4건은 기존 oq-251~oq-254 와 같아 새로 만들지 않음. 새 질문 5건. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-11-06/verification.json

```json
{
  "run_id": "2026-10-11-06",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: EUR-Lex 원문을 열어 (EU) 2026/2015 의 채택일 2026-09-04, 관보 게재일 2026-09-07(OJ L 2026/2015), 부속서 223a·224a 의 EN ISO 10218-1/-2:2025 추가를 대조했다. 단일 1차 출처다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 원문에서 제2조의 2023/1586 폐지(2027-01-20 발효)와 전문 (14)의 '지침 2006/42/EC 가 규정 2023/1230 으로 폐지됨'을 대조했다. 목록은 지침 기반이며 규정 2023/1230 의 조화 게재로 읽지 않는다는 한정을 유지해야 한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 관보 결정에는 참조 목록·날짜·법적 기반만 있고 ISO 10218 의 조항 내용은 없음을 원문으로 확인했다. 따라서 PL d·범주 3·정상 정지 서술은 IBF(컨설팅사) 단독 근거다. 기존 페이지 서술을 [사실]에서 [추정]·벤더 해설로 강등하는 근거로 유지한다. ref-1116 은 이번에 다시 열지 않았다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람: ref-1255 는 재열람에 실패했고 2026-10-09 열람 기록에 기댄다. [추정] 유지. 각주에 (원문 미열람)을 표시해야 한다. oq-265(사용자 의무)에는 답하지 않는다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: committee.iso.org/standard/88615 를 열어 ISO/DIS 3691-4, 제3판, 40.60(투표 종료, 2026-09-10), 'Will replace ISO 3691-4:2023', 개발 중임을 대조했다. oq-384 의 충돌은 이 원문으로 해소된다. 개정안 본문은 열지 않았다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증자 재열람 실패(standard.go.kr ECONNRESET). 리서치 열람 기록에 기댄다. 같은 시스템의 KS B ISO 10218-2 상세(f7)가 같은 형식(2011 IDT)임을 확인했다. ISO 10218:2025 부합 KS 가 없다는 것은 부재 증명이 아니다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: standard.go.kr 상세에서 ISO 10218-2:2011 IDT, 제정 2012-03-29, 최종 확인 2022-10-12 를 대조했다. 이력에는 2017 확인도 있으므로 '2017 확인'은 틀린 것이 아니라 최신 확인이 아니다. 해당 문장은 이번 대상 페이지 밖에 있다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증자는 통합본 HTML 열람이 실패해(본문이 비어 있음) 리서치의 2026-07-27 통합본 열람 기록에 기댄다. 부속서 III 1.2.1(f) 의 5년 추적 기록 요건은 기존 위키(ref-1109 해설)와 내용이 맞는다. 적용 대상은 안전 소프트웨어 개입·판 이력으로 한정되며 목적은 당국 요청 시 적합성 입증뿐이다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다(통합본 재열람 실패). 대상은 자체 진화 행동·논리를 가진 기계의 제어 시스템에 한정된다는 서술을 유지해야 한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: UL Standards & Engagement 목록에서 제1판(Active), 발행 2021-05-26, 최근 개정·ANSI 승인 2026-06-10 을 대조했다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 공개 적용 범위 1.4 에서 산업용 로봇 제외(UL 1740·CSA Z434)와 매니퓰레이터의 탑재물 사용 가능 문구를 대조했다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: UL Solutions 보도자료(2026-03-11)에서 Tally 의 UL 3300 인증, 로봇·충전 도크의 화재·감전·자율 이동 평가를 대조했다. 인증기관의 상업 발표이므로 [추정]·'벤더 주장' 유지. 인증서는 공개되지 않았다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: fsc.go.kr 보도참고(2025-11-27) 본문에서 '(실외이동로봇)운행안전인증 심사 평가항목 통폐합(16→8개) 및 심사기간 단축(60→30일)('25.11 시행)'을 대조했다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증자 재열람 실패(motir.go.kr·law.go.kr ECONNRESET). 리서치 열람 기록에 기댄다. 같은 날 실행 2026-10-11-05 브리프의 ref-1469(국가법령정보센터, 같은 고시, 2025-11-24 일부개정, 발령일 시행)와 f13 의 '25.11 시행'이 일치한다. 같은 정부 계열이므로 독립 교차 확인으로 세지 않는다. 고시 번호 표기는 '제2025-021호'(이 브리프)와 '제2025-21호'(ref-1469)로 다르다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "두 원문(ref-1118 첨부 부칙, ref-1505 첨부의 구 부칙)이 서로 다르다. 한쪽을 고르지 않는 [추정] 처리와 출처 충돌 열린 질문을 유지한다. 검증자는 첨부를 다시 열지 못했다(ECONNRESET). 발령일 2023-11-17 만 확정적으로 쓴다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다(고시 첨부 재열람 실패). 진흥원 안내 '30일 이내'(ref-980)와 정부 보도참고의 '60→30일'(f13)과 일치한다. 서류 보완 기간이 산입되는지는 미확인으로 남긴다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록(ref-1118 첨부 HWP 별표 3)에 기댄다. 항목 수 16 은 ref-992 의 '16가지'와 맞고, 검색 결과 해설의 '총 16개 항목'과도 맞는다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인: 8개 항목 이름은 실행 2026-10-11-05 의 ref-1469(국가법령정보센터 별표 3)와 ref-980 에 같은 순서로 있다. 모두 같은 인증 체계 계열이라 교차 확인은 false 로 둔다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치가 두 별표를 조문으로 대조한 결과에 기댄다. 신 별표의 '규격 및 운행속도', 1.라 보호구역, 7.나 통신 단절 정차, 8.다·라 는 ref-1469 기록과 맞는다. 빠진 항목이 다른 규정으로 옮겨졌는지 미확인이라는 한정을 반드시 유지해야 한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다. 질량별 속도 구간은 ref-1469(실행 2026-10-11-05 f29)와 일치한다. 폭 800 mm·1,200 mm 는 검색 결과 해설과도 맞는다. 기존 106행의 '확정 고시 별표 원문 미확인'을 정정하는 근거다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다. 8.다(보행자 밀집 시 관제장치 알림·관리자 조치)는 ref-1469 기록과 맞는다. 실외 업종별 조건이므로 '연계 대상'으로 쓰고, ROP 가 인증상 관제장치라고 쓰지 않는다(oq-187)."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록(제10조②)에 기댄다. 검증자 재열람은 실패했다. 인증이 로봇과 관제장치의 조합이라는 기존 위키 내용(ref-980)과 맞는다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 산업안전보건인증원 자율안전확인 대상품 페이지에서 산업용 로봇 정의 문구를 대조했다. AMR·AGV 전체로 확대하지 않는다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인: White Rose 저장소 소개 페이지는 2015–2022 와 77건을 보여 준다. 일 단위 기간(2015-01-01~2022-04-30)은 원고 PDF 를 검증자가 열지 못해(크기 초과) 리서치 열람 기록에 기댄다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치의 원고 열람 기록에 기댄다. 소개 페이지 초록에는 관할 범위가 없다. '연방 OSHA 관할만, 주 계획 22개 주 제외'는 원고 본문 기준으로 쓴다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치의 원고 열람 기록에 기댄다. 77건 서술의 길이 지표일 뿐 원인 정밀도나 발생률로 쓰지 않는다는 한정을 유지한다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CDC Stacks 에서 제목, 저자, 2001~2020 년 1,076건, OHBWC 자료를 대조했다. CDC Stacks 는 '2026-03-03 Epub ahead of print'로 표시하고 권호·쪽이 없다. 69(5):345–357 은 Crossref 기준이라는 브리프 기록만 있다. 노출 인원당 발생률이 아니다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록에서 85% medical-only(의료 처치만 또는 휴업 7일 이하)와 공유 작업공간 협동 적용 로봇 팔 75.7% 를 대조했다. n=917 과 발생률 미산출은 쓰지 않는다는 처리를 유지한다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "출처 실재: KOSHA 다운로드 PDF(251KB)가 열렸으나 이미지·압축 PDF 라 검증자가 본문을 추출하지 못했다. 공단 이슈리포트 목록에 '로봇용접기 용접팁 교체 중 끼임, 사망 1명(2020-05)' 사례가 있어 사건이 실재함은 뒷받침된다. muting 세부는 리서치 열람 기록에 기댄다. 발생일은 출처에 없으므로 미확인으로 쓴다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다(PDF 본문 추출 실패). 사례의 재발방지대책 표현이며 muting 구현 인증 지침이 아니라는 한정을 유지한다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "출처 실재: OCW 강의 목록에 'System Safety: CAST Analysis'(pdf, 245 kB, 3회차 2부)가 있고, 열린 PDF 크기(244.8KB)와 일치한다. 슬라이드 본문은 압축 PDF 라 추출하지 못해 리서치 열람 기록에 기댄다. 화학 공장(SO2 탱크) 사례이며 로봇 적용 실증이 아니다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다. 같은 강좌 과제에 사후 판단 편향 찾기가 있다는 검색 결과와 맞는다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Frontiers 원문에서 2020-11, 같은 연구자, Zoom, 역할극 면담 22회를 대조했다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'the use of static images meant we could not convey the more dynamic parts of the scenario effectively' 를 대조했다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "출처 실재: DOI 10.13180/icres.2022.18-19.07.019 가 ICRES 2022 paper 19 PDF 로 연결된다. 검증자 열람에서는 본문 추출이 신뢰할 수 없어(압축 PDF) 필드 길이 충돌은 리서치 열람 기록에 기댄다. 초안 내부 표기 충돌로만 쓰고 규범 값으로 쓰지 않는다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다(같은 PDF). 변조 방지 보장 근거로 쓰지 않는다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다(같은 PDF)."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "리서치 열람 기록에 기댄다(같은 PDF). '보존 기간 조항 없음'은 초안 부록 범위에서의 진술로 쓴다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rosbag2 0.35.0 태그 README(raw)에서 --repeat-transient-local 의 최근 N개 보관, 분할·스냅샷 시 재삽입, 기본 depth 1 을 대조했다. 태그 커밋 날짜는 미확인이다."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 README 에서 스냅샷 모드의 메모리 순환 버퍼(--max-cache-size 바이트, 선택적 --max-cache-duration 초)와 요청 시 저장을 대조했다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 유실 통계가 증분 방식이고, 유실 0 인 토픽은 빠지며, 이벤트 발행 뒤 카운터가 0 으로 재설정됨을 대조했다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: MCAP 고정 커밋 명세의 publish_time 'If not available, must be set to the log time.' 을 대조했다. '포맷만으로 구분되지 않는다'는 이 규칙에서 바로 따라오는 결론이다."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Chunk uncompressed_crc 0 이 'CRC validation should not be performed' 임을 대조했다. 강도는 should 다."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f1·f2·f5~f7 에서 도출했다. 페이지에서는 '구축자 의견'으로 출처를 밝혀야 한다."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 실외 인증 관제장치 요구는 연계 대상(업종별 조건)이다. ROP 가 인증상 관제장치인지(oq-187)는 판단하지 않는다는 한정을 함께 쓴다. '구축자 의견' 표시가 필요하다."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f8·f9 에서 도출했다. 법적 적용 여부의 판단은 59. 법·규제·보험·라이선스 로 연결하고, 이 페이지에서는 보존 정책 구분 의견으로만 쓴다. '구축자 의견' 표시가 필요하다."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f24~f28 에서 도출했다. '구축자 의견' 표시가 필요하다."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f35~f43 에서 도출했다. 근거 목록에 ref-1120(이번 미재열람)이 있으므로 해당 각주는 기존 줄을 그대로 쓴다. '구축자 의견' 표시가 필요하다."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f29~f32 에서 도출했다. 로봇 사고에 CAST 를 적용한 실증이 없다는 한정을 함께 쓴다. '구축자 의견' 표시가 필요하다."
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
      "f14·f18~f22(ref-1505, 고시 '제2025-021호')는 같은 날 실행 2026-10-11-05 의 ref-1469(국가법령정보센터, 같은 고시 '제2025-21호')·f27~f33 과 같은 고시·별표 3 을 다룬다. 다른 URL 이라 ref id 는 따로지만 고시 번호 표기가 서로 다르다.",
      "f1·f2 는 분리 페이지 2026-09-30-area50-s7.md 42행·2026-09-30-area50-s4.md 41행·docs/categories/safety/index.md 177행의 IBF 해설 기반 서술과 겹친다(safety/index.md 는 이번 갱신 범위 밖).",
      "f8 은 2026-09-30-area52-s3.md 43행의 IES 해설(ref-1109) 기반 5년 기록 문장과 겹친다(범위 밖, 후속 연결).",
      "f7 은 2026-09-26-area25-s7.md 45행·ref-814 제목의 'KS B ISO 10218-2 2017 확인'과 겹친다(범위 밖). 국가표준 목록 이력에 2017 확인도 있으므로 모순이 아니라 최신 확인일의 보강이다.",
      "ref-1503(ICRES 2022 게재본)과 ref-1120(arXiv 판)은 같은 연구의 서로 다른 판이다.",
      "f4(R15.08-3 발행일)는 docs/categories/safety/index.md 53행의 기존 내용 확인이며 재추가가 아니다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "고시 번호 표기: ref-1505·f14 '산업통상부 고시 제2025-021호' 와 같은 날 49. 사람 근접 안전 브리프(ref-1469) '산업통상부고시 제2025-21호' 가 같은 고시를 다르게 적는다. 위키 안에서 하나로 통일해야 한다.",
      "부처명: 2023년 고시(ref-1118)는 '산업통상자원부', 2025년 개정 고시(ref-1505)는 '산업통상부'로, 시기에 따라 이름이 다르다. 서술에서 혼동하지 않게 각 고시의 발령 당시 이름을 쓴다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f3: 7절(분리 페이지 2026-09-30-area50-s7 42행)과 4절(분리 2026-09-30-area50-s4 41행)에서 PL d·범주 3 대체와 정상 정지 기능 신설 서술을 [사실]에서 [추정]으로 강등한다. 'IBF Solutions(컨설팅사) 해설, 벤더 주장'을 병기하고 각주는 [^ref-1116] 만 단다. 이유: 관보 원문(ref-1496)에는 참조 목록만 있고 조항 내용이 없다.",
    "f1·f2: 7절·4절의 EU 조화 게재 서술은 ref-1496 근거 [사실]로 고친다. 결정 (EU) 2026/2015 는 2026-09-04 채택, 2026-09-07 게재이며, 부속서는 시행결정 2023/1586 부속서 I 에 223a·224a 를 추가한다. 이 적합성 추정은 기계류 지침 2006/42/EC 에 대한 것이고, 그 목록(2023/1586)은 2027-01-20 폐지된다고 함께 적는다. 이유: 규정 (EU) 2023/1230 의 조화 게재로 읽히지 않게 하기 위해서다. 규정 쪽 게재 시점은 새 열린 질문으로만 둔다.",
    "고시 번호 표기: 같은 고시가 ref-1505 에서는 '제2025-021호', 같은 날 49. 사람 근접 안전 실행의 ref-1469 에서는 '제2025-21호'로 적혀 있다. 이 페이지에서는 첫 등장에 '산업통상부 고시 제2025-21호(첨부 고시문 표기 제2025-021호, 2025-11-24 발령·시행)'로 적고 이후에는 '제2025-21호'로 통일한다. 이유: 용어 일관성과 다른 페이지와의 대조를 위해서다.",
    "f14·f15: 5절 104행 '고시 제2023-211호(2023-11-17)로 정해졌고' 와 7절(분리 s7 45행) '절차·기준은 고시 제2023-211호가 정한다' 를 고친다. '제2023-211호(2023-11-17 발령)를 제2025-21호가 2025-11-24 개정했고 발령일부터 시행한다'로 쓴다 [사실][^ref-1505]. 제2023-211호의 시행일은 원 고시 부칙(2023-11-17)과 개정 고시에 실린 구 부칙(2023-11-21)을 둘 다 [추정]으로 제시하고 하나를 고르지 않는다. 이유: 두 원문이 충돌하고, 출처 충돌 열린 질문이 브리프에 있다.",
    "f13·f17~f20: 5절 실외 사례 표의 제약 칸(100행)과 106행 문단을 다시 쓴다. 구 고시 별표 3 은 16개 항목(f17), 현행 별표 3 은 8개 항목(f18)이고, 2025-11 통폐합이 있었다(f13). 항목 대응과 새 별표에 없는 항목(알림음·등화장치·물리적 보안)은 f19 로 적는다. '8개와 16가지로 달라 어느 쪽도 고르지 않고 함께 둔다'는 문구는 삭제한다. '확정 고시 별표 원문 미확인' 기준값 문장은 ref-992 단독 근거에서 ref-1118(확정 고시 별표 3) 근거로 바꾸고, 현행 잔존 여부(f20)를 덧붙인다. 빠진 항목이 다른 규정으로 옮겨졌는지는 '미확인'으로 명시한다. 이유: oq-230 해소 근거가 원문으로 확인됐다.",
    "f16: 5절 실외 사례의 시작 조건 칸(98행)에 30일 처리기간의 근거로 고시 제9조①(f16)과 60→30일 경위(f13)를 더한다. 서류 보완 기간이 산입되는지는 '미확인'으로 적는다.",
    "f21·f22·f45: 9절 업종별 조건 행에 실외 인증의 관제장치 요구(실시간 위치·속력·배터리·통신 감도·상태, 원격 정지)와 인증 정보의 관제장치 모델 단위 보관을 넣을 때는 '연계 대상: '으로 시작한다. ROP 가 인증상 관제장치라거나 이 요구를 충족한다고 쓰지 않는다(oq-187 은 열린 채 둔다). 이유: 원문 19장 업종별 조건(실외 차량)은 연계 영역이다.",
    "f4/ref-1255: 7절 R15.08-3 행은 [추정]으로 둔다. 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1255 에 source_unopened: true 를 넣는다. 이유: 이번 재열람에 실패했다.",
    "f5/ref-789: 7절에 ISO/DIS 3691-4 제3판 행을 더한다(40.60, 2026-09-10, ISO 3691-4:2023 대체 예정, 발행된 개정판이 아님). reference_updates 로 ref-789 제목을 'ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems' 로 갱신한다. 이유: 위원회 페이지 원문으로 확인했다.",
    "f7: 7절의 KS 부합판 서술은 'KS B ISO 10218-2 의 최종 확인일은 2022-10-12(ISO 10218-2:2011 IDT)'로 쓴다. 2017 확인이 틀렸다고 쓰지 않는다. 2026-09-26-area25-s7.md 45행과 ref-814 제목은 이번 pages 에서 고치지 않고 후속 정리 대상으로 changelog_entry 에만 적는다. 이유: 국가표준 목록 이력에 2017 확인도 있고, 해당 문장이 대상 페이지 밖에 있다.",
    "f12: 7절의 UL 3300 Tally 인증 문장을 [추정]으로 쓰고 '벤더 주장(인증기관 UL Solutions 의 상업 보도자료)'을 병기한다. 이종 플릿 전체의 안전 입증으로 확장하지 않는다. 이유: 인증서·시험보고서가 공개되지 않은 단일 상업 발표다.",
    "f8·f9·f46: 7절의 EU 기계 규정 기록 의무를 쓸 때 대상을 그대로 한정한다. 5년은 안전 소프트웨어 개입 데이터와 업로드한 판의 추적 기록, 1년은 자체 진화 제어 시스템의 안전 관련 결정 데이터이며, 목적은 관할 당국의 이유 있는 요청에 따른 적합성 입증뿐이다. 일반 작업 로그나 플릿 전체 데이터의 보관 의무로 쓰지 않는다. 제품별 적용 여부는 59. 법·규제·보험·라이선스 로 연결한다.",
    "f27·f28/ref-1501: 8절 Suresh 외 항목의 각주 발행일을 '2026-03-03(온라인 선공개)'로 쓴다. 권호·쪽 69(5):345–357 은 'Crossref 기준'으로 표시한다. 85% 와 75.7% 는 초록 수치임을 밝히고, 노출 인원당 발생률이 아니라고 적는다. 이유: CDC Stacks 는 Epub ahead of print 로만 표시한다.",
    "f24~f26: 8절 Sanders 외 항목과 4절 '중상 보고' 항목의 기간을 2015-01-01~2022-04-30 으로 고친다. 연방 OSHA 관할만 포함되고 주 계획 22개 주는 빠진다는 점을 적는다. 서술 단어 수 중앙값 36 은 77건 보고의 서술 길이 지표일 뿐 원인 정밀도·발생률이 아니라고 함께 쓴다.",
    "f29·f30: 5절 제조 공장에 공단 공개 재해사례(용접 팁 교체 중 로봇 팔과 지그 사이 끼임 사망)를 별도 사례로 추가한다. 발생일은 '미확인'으로 적는다. 오뚜기·고성 기사 사건과 연결하거나 같은 사건으로 쓰지 않는다. 여섯 항목 가운데 근거가 없는 칸은 '해당 없음'으로 둔다. 이유: 출처에 발생일이 없고 다른 사건이다.",
    "f31·f32·f49: 6절의 CAST 소절에서 출처를 '2016년 봄 학기 MIT OCW 강의 자료'로 쓰고, 예시는 화학 공장 SO2 탱크 넘침 사례이며 로봇 사고에 적용한 실증은 확인하지 않았다고 밝힌다. 이유: 2016 은 강의 학기이고 적용 대상이 다르다.",
    "f35~f38: 6절 '사고 기록 장치' 소절은 EBB 초안 내부의 표기 충돌(날짜·시각·체크섬), 결정 코드의 제조사·운영자 위임, RD 순환 덮어쓰기와 고정 보존 기간 부재로만 쓴다. 특정 길이·형식을 규범 값으로 제시하지 않는다. ref-1503(ICRES 2022 게재본)과 ref-1120(arXiv 판)이 같은 연구의 다른 판임을 밝힌다.",
    "f39~f43: 7절의 rosbag2·MCAP 내용은 사고 증거 보존 관점으로만 짧게 쓴다. 기준판(rosbag2 0.35.0 태그, MCAP 고정 커밋 f7069e6)과 기준일 2026-10-11 을 명시하고, 37. 관제 화면·실행 기록, 43. 데이터·관측성·배포 로 연결한다. 이유: 기록 기능 자체는 해당 영역의 내용이다.",
    "f44~f49: [의견] 문장마다 '구축자 의견'임을 밝힌다. 근거 finding 의 출처 각주는 브리프에 적힌 것만 단다.",
    "11절(분리 2026-09-30-area50-s11): oq-230 과 oq-384 는 해결로 바꾼다(근거 f17·f18·f19, f5). oq-186 은 부분 답(시점·근거 고시 f13·f14, 흡수·누락 항목 f19)만 적고 열림을 유지한다. 이유: 빠진 항목이 다른 규정으로 옮겨졌는지가 남아 있다. oq-251·oq-123·oq-252·oq-333·oq-187 은 부분 근거만 덧붙이고 해결로 바꾸지 않는다. 브리프의 새 열린 질문 5건은 등록한다.",
    "범위 밖 페이지(docs/categories/safety/index.md 177행의 IBF 단독 [사실]과 '산업통상자원부 고시(2023-11-17)' 서술, 2026-09-26-area25-s7.md 45행, 2026-09-30-area52-s3.md 43행)는 이번 pages 에 넣지 않는다. 후속 정리 대상으로 changelog_entry 에만 기록한다. 이유: 하루 갱신 예산과 이번 갱신 범위 밖이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 49건, 미확인 0건, 교차 확인 0건. 확인 49건의 내역은 다음과 같다. 검증자가 원문을 직접 대조한 것이 19건(f1~f3, f5, f7, f10~f13, f23, f27, f28, f33, f34, f39~f43), 부분 대조한 것이 2건(f18, f24)이다. 검증자의 재열람이 연결 오류나 압축 PDF 로 실패해 리서치 열람 기록에 기댄 것이 21건(f6, f8, f9, f14~f17, f19~f22, f25, f26, f29~f32, f35~f38)이다. 원문 미열람 기록에 기댄 것이 1건(f4), 의견이 6건(f44~f49)이다. 강등: 이번 브리프 finding 의 강등은 없다. 기존 페이지 7절·4절의 PL d·범주 3·정상 정지 서술은 f3 에 따라 사실에서 추정(IBF 해설, 벤더 주장)으로 강등한다. 원문 미열람 출처: ref-1255(이번 실행). ref-1116 과 ref-1120 은 이번에 다시 열지 않았다. 열린 질문: oq-230 해결 인정(f17·f18·f19), oq-384 해결 인정(f5). oq-186 은 부분 답만 있어 열림을 유지한다. 정정 요청 없음. 주의: 실외이동로봇 고시 두 판(제2023-211호, 제2025-21호)과 KOSHA 재해사례·EBB 게재본·MIT 강의 PDF 는 검증 시점에 본문을 다시 열지 못했다. 같은 날 49. 사람 근접 안전 실행의 국가법령정보센터 고시 기록(ref-1469)과 정부 보도참고(ref-1504)로 일부만 맞춰 보았다. 고시 관련 출처는 모두 같은 정부 계열이라 독립 교차 확인으로 세지 않았다. 제2023-211호의 시행일은 출처끼리 충돌해 확정하지 않는다. EU 조화 게재는 기계류 지침 2006/42/EC 기반 목록에 대한 것이며 2027-01-20 폐지된다. 검증 검색 4회.",
  "retry_reason": null
}
```

### runs/2026-10-11-06/pages.json

```json
{
  "run_id": "2026-10-11-06",
  "outline": [
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "'적합성 추정'은 EU 관보 원문으로 다시 확인했다. (EU) 2026/2015 는 기계류 지침 2006/42/EC 기반 목록에 EN ISO 10218:2025 를 추가했고, 그 목록은 2027-01-20 폐지된다. [사실][^ref-1496] '중상 보고'에는 기간 2015-01-01~2022-04-30 과 연방 관할 한정을 적었다. [사실][^ref-1122]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3600,
      "summary": "실외 인증 사례를 현행 고시 제2025-21호(2025-11-24 시행)와 별표 3 의 16개→8개 항목 대응으로 고쳐 썼다. [사실][^ref-1505][^ref-1118] 제조 공장에는 안전보건공단 공개 재해사례(muting 우회, 운전 정지 미실시)를 더했다. [사실][^ref-1502]",
      "planned_findings": [
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
        "f29",
        "f30"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "윤리적 블랙박스 초안 안에서 날짜·시각·체크섬 표기가 서로 맞지 않고, RD 기록은 순환 덮어쓰기 방식이며 보존 기간을 정하지 않는다. [사실][^ref-1503] CAST 강의 자료는 조사 질문을 정비 정책과 안전 장비 비가동 운전까지 넓힌다. [사실][^ref-1506]",
      "planned_findings": [
        "f31",
        "f32",
        "f35",
        "f36",
        "f37",
        "f38",
        "f49"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 3200,
      "summary": "EN ISO 10218:2025 EU 게재는 지침 기반 목록에 실린 것으로 원문 확인했고, PL d 해설은 추정으로 낮췄다. [사실][^ref-1496] 이 밖에 실외 고시 개정, ISO/DIS 3691-4, KS 부합판, EU 기계 규정 기록 의무, UL 3100·3300, 자율안전확인, rosbag2·MCAP 행을 더했다.",
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
        "f14",
        "f23",
        "f39",
        "f40",
        "f41",
        "f42",
        "f43",
        "f44",
        "f46",
        "f48"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1200,
      "summary": "연방 OSHA 중상 보고(2015-01-01~2022-04-30)와 Ohio 산재보상 청구(2001~2020, 1,076건)는 관할·기간·집계 단위가 다르다. [사실][^ref-1122][^ref-1501]",
      "planned_findings": [
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f33",
        "f34",
        "f47"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1700,
      "summary": "업종별 조건 행에 실외 인증이 요구하는 관제장치 기능(실시간 상태 확인, 원격 정지)과 관제장치 모델 단위 보관을 연계 대상으로 더했다. [사실][^ref-1505]",
      "planned_findings": [
        "f21",
        "f22",
        "f45"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 500,
      "summary": "이전 판 연결 목록 링크를 두고, 43. 데이터·관측성·배포(기록기 설정과 증거 보존), 59. 법·규제·보험·라이선스(EU 게재·기록 의무의 법적 해석) 연결을 덧붙였다. [추정][^ref-831][^ref-1496]",
      "planned_findings": [
        "f2",
        "f8",
        "f39",
        "f42"
      ]
    },
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "section": "11. 열린 질문",
      "budget_chars": 1700,
      "summary": "oq-230·oq-384 를 원문 근거로 해결했다. oq-186 을 비롯한 질문들은 부분 근거만 더해 열어 두고, 새 질문 5건을 올렸다. [사실][^ref-1118][^ref-1505][^ref-789]",
      "planned_findings": [
        "f5",
        "f6",
        "f7",
        "f8",
        "f13",
        "f14",
        "f15",
        "f17",
        "f18",
        "f19",
        "f21",
        "f22",
        "f35",
        "f40",
        "f42"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "4·5·6·7·8·9·11·13절 차등 갱신, 10절 덧붙임: 실외 인증 근거를 고시 제2025-21호로 정정하고 별표 3 의 16개→8개 항목 대응을 원문으로 정리, EN ISO 10218 EU 게재를 관보 원문으로 확인하고 IBF 해설을 추정으로 강등, 제조 공장 공식 재해사례, EBB 초안 형식 충돌·CAST, UL 3100·3300·ISO/DIS 3691-4·KS 부합판·EU 기록 의무·rosbag2·MCAP, 사고 자료 범위, oq-230·oq-384 해결. 2차: 10절 이전 판 연결 목록 링크 복원·59 영역 호칭 수정, 6절·5절 개수 단정 문장 수정, 프런트매터 sources 를 원 페이지 각주와 일치",
      "patches": [
        {
          "section": "4. 핵심 개념과 용어",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)",
          "frontmatter": {
            "related_areas": [
              4,
              22,
              37,
              38,
              43,
              48,
              49,
              51,
              52,
              55,
              57,
              58,
              59,
              61,
              62,
              65,
              66,
              67
            ],
            "tags": [
              "ISO 10218",
              "EU 조화 표준",
              "실외이동로봇 운행안전인증",
              "윤리적 블랙박스",
              "사고 조사",
              "잠금·표지"
            ],
            "confidence": "medium",
            "last_run": "2026-10-11",
            "sources": [
              "ref-1084",
              "ref-991",
              "ref-1115",
              "ref-1116",
              "ref-1117",
              "ref-980",
              "ref-1118",
              "ref-945",
              "ref-1120",
              "ref-1121",
              "ref-1122",
              "ref-1124",
              "ref-1125",
              "ref-563",
              "ref-1496",
              "ref-1501",
              "ref-1502",
              "ref-1503",
              "ref-1504",
              "ref-1505",
              "ref-1506",
              "ref-789"
            ]
          }
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-11-area50-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(4,831자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area50-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"11. 열린 질문\" 절(2,163자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area50-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"6. 대표 접근법과 기술\" 절(1,504자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area50-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"8. 대표 연구와 자료\" 절(1,484자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area50-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"4. 핵심 개념과 용어\" 절(878자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area50-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 50. 안전 표준·인증·사고 조사 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(606자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-11 | 50. 안전 표준·인증·사고 조사 | 4~11·13절 차등 갱신: 실외이동로봇 인증 근거를 고시 제2025-21호(2025-11-24 시행)로 정정하고 별표 3 의 16개→8개 항목 대응을 원문으로 정리(oq-230 해결), EN ISO 10218 EU 조화 게재를 관보 원문(지침 기반, 2027-01-20 폐지 목록)으로 확인하고 IBF 해설을 추정·벤더 주장으로 강등, ISO/DIS 3691-4 제3판 40.60(oq-384 해결)·KS 부합판·UL 3100·UL 3300(벤더 주장)·자율안전확인·EU 기계 규정 기록 의무·rosbag2·MCAP 추가, 제조 공장 공식 재해사례·EBB 초안 형식 충돌·CAST·사고 자료 범위 보강, 새 열린 질문 5건. 2차: 10절 이전 판 연결 목록 링크 복원, 개수 단정 문장 2건 수정, 프런트매터 sources 정리. 후속 정리 필요(이번 범위 밖): docs/categories/safety/index.md 177행(IBF 단독 사실 표기와 '산업통상자원부 고시(2023-11-17)' 서술), docs/topics/2026/2026-09-26-area25-s7.md 45행과 ref-814 제목(KS B ISO 10218-2 최종 확인일 2022-10-12 보강), docs/topics/2026/2026-09-30-area52-s3.md 43행(EU 기계 규정 5년 기록의 1차 근거 ref-555 연결), 이전 판 주제 페이지 docs/topics/2026/2026-09-30-area50-s4.md 41행·2026-09-30-area50-s7.md 42·45행(IBF 서술 강등과 고시 근거 정정은 이번 판 4·7절로 대체됨) | run 2026-10-11-06",
  "index_updates": {
    "home_recent": "2026-10-11 — 50. 안전 표준·인증·사고 조사: 실외이동로봇 인증 고시 현행 근거(제2025-21호)와 별표 16개→8개 항목 대응, EN ISO 10218 EU 조화 게재 원문 확인과 해설 강등, 사고 기록 규약·사고 자료 범위 보강",
    "category_recent": "2026-10-11 — 50. 안전 표준·인증·사고 조사: 4~11절 차등 갱신(실외 인증 고시 정정, EU 조화 게재 원문 확인, ISO/DIS 3691-4·KS·UL 3100·EU 기록 의무·rosbag2·MCAP, 제조 공장 공식 재해사례, EBB·CAST, oq-230·oq-384 해결)",
    "area_recent": "2026-10-11 — 50. 안전 표준·인증·사고 조사: 실외이동로봇 운행안전인증 근거를 고시 제2025-21호로 정정하고 구·신 별표 3 대응 정리, EN ISO 10218 EU 게재(지침 기반, 2027-01-20 폐지 목록)와 IBF 해설 강등, 표준·오픈소스 행 추가, 사고 자료·조사 방법 보강, 새 열린 질문 5건"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1496",
      "org": "European Commission (Official Journal of the European Union)",
      "title": "Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC",
      "published": "2026-09-07",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "EN ISO 10218-1/-2:2025 참조를 기계류 지침 2006/42/EC 조화 표준 목록(2023/1586 부속서 I)에 추가한 시행결정(OJ L 2026/2015). 제2조로 2023/1586 을 2027-01-20 부로 폐지한다. Publications Office 공식 원문으로 열람.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1497",
      "org": "국가기술표준원 (국가표준인증 통합정보시스템)",
      "title": "KS B ISO 10218-1 로봇 및 로봇장치 ─ 산업용 로봇의 안전에 관한 요구사항 ─ 제1부: 로봇",
      "published": "2021-11-26",
      "url": "https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS 상세 목록. 대응 국제표준 ISO 10218-1:2011(IDT), 제정 2008-01-17, 최종개정확인일 2021-11-26. 표준 본문은 열지 않았다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1498",
      "org": "UL Standards & Engagement",
      "title": "UL 3100 Automated Mobile Platforms (AMPs)",
      "published": "2026-06-10",
      "url": "https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=39063",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "UL 3100 공식 목록. 제1판(2021-05-26 발행)의 최근 개정·ANSI 승인 2026-06-10, 적용 범위 1.1·1.4(산업용 로봇 제외, 매니퓰레이터 탑재 가능)를 공개한다. 개정 조항 전체는 열지 않았다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1499",
      "org": "UL Solutions",
      "title": "UL Solutions Grants Its First Global Certification for a Public-Facing Robot to Simbe's Tally Autonomous Mobile Robot",
      "published": "2026-03-11",
      "url": "https://www.ul.com/news/ul-solutions-grants-its-first-global-certification-public-facing-robot-simbes-tally-autonomous",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "인증기관의 상업 보도자료. Simbe Tally 로봇·충전 도크의 UL 3300 인증 취득을 발표한다. 인증서·시험보고서는 공개되지 않았다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1500",
      "org": "안전보건공단 산업안전보건인증원",
      "title": "자율안전확인 대상품 (자율안전확인신고 대상 및 적용범위)",
      "published": null,
      "url": "https://miis.kosha.or.kr/oshci/busi/viewMiisJayulMerchandiseInfo.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "자율안전확인 대상 기계·기구 안내. 산업용 로봇을 3축 이상 매니퓰레이터와 전용 제어기를 갖춘 고정식 로봇으로 정의한다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1501",
      "org": "Suresh, V., Konda, S., Haney, J. M. 외 (American Journal of Industrial Medicine 69(5))",
      "title": "Robot-Related Workers' Compensation Claims in Ohio, 2001–2020",
      "published": "2026-03-03",
      "url": "https://stacks.cdc.gov/view/cdc/258698",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "NIOSH 연구진의 Ohio 산재보상 청구 분석(DOI 10.1002/ajim.70067). CDC Stacks 는 2026-03-03 온라인 선공개(Epub ahead of print)로 표시하며, 권호·쪽 69(5):345–357(인쇄 2026-05)은 Crossref 기준이다. 이번에는 서지·초록만 확인했고 본문 PDF 는 열지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1502",
      "org": "안전보건공단",
      "title": "산업용 로봇 팔과 지그 사이에 끼임 (재해사례)",
      "published": null,
      "url": "https://oshri.kosha.or.kr/kosha/data/machine.do?articleNo=411924&attachNo=233368&mode=download",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공개 재해사례 1쪽. 용접 팁 교체 중 끼임 사망의 원인(muting 사용으로 방호장치 미작동, 운전 정지 없이 셀 진입)과 재발방지대책을 적는다. 발생일은 없다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1503",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본)",
      "published": "2022-07",
      "url": "https://doi.org/10.13180/icres.2022.18-19.07.019",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "윤리적 블랙박스 공개 표준 초안의 학회 게재본(pp.99–110, 부록 RFC Draft 0.1 포함). 같은 연구의 arXiv 판은 ref-1120. 필드 표·주석과 RD 덮어쓰기 구조를 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1504",
      "org": "관계부처 합동 (금융위원회 누리집 게재 보도참고자료)",
      "title": "규제의 벽은 허물고 AI의 길은 넓힌다 — 신산업 규제합리화 1호 로드맵(AI 분야) 발표",
      "published": "2025-11-27",
      "url": "https://www.fsc.go.kr/no010101/85753",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "정부의 AI 분야 규제합리화 로드맵 보도참고자료. 실외이동로봇 운행안전인증 심사 평가항목 16→8개 통폐합과 심사기간 60→30일 단축('25.11 시행)을 적는다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1505",
      "org": "산업통상부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정)",
      "published": "2025-11-24",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "2025-11-24 발령·시행된 일부개정 고시(위키 본문 표기 제2025-21호, 첨부 고시문 표기 제2025-021호). 첨부 본문에서 제9조① 30일 통보 기한, 제10조② 관제장치 모델 정보 보관, 별표 3 의 8개 인증 기준 항목을 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1506",
      "org": "Leveson, N. (MIT OpenCourseWare, 16.863J System Safety)",
      "title": "System Safety: CAST Analysis (강의 자료)",
      "published": "2016",
      "url": "https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/7dc4344ef259e4bde4acc1bb2d578a95_MIT16_863JS16_LecNotes3-2.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "2016년 봄 학기 강의 슬라이드. SO2 탱크 넘침 사례로 CAST 조사 질문(정비 정책·안전 장비 비가동 운전)과 운전원 분석 항목(맥락·시스템 요인, 정신 모형 결함)을 보여 준다. 2016 은 강의 학기다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1255",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications",
      "published": "2026-04-23",
      "url": "https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "원문 미열람. R15.08 Part 3 판매 페이지(기존 출처). 이번 재열람은 Cloudflare 차단으로 실패했고 발행일은 2026-10-09 열람 기록 기준이다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-789",
      "org": "ISO",
      "title": "ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": null,
      "url": "https://www.iso.org/standard/88615.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "ISO 3691-4 차기판(제3판) 프로젝트 페이지. 2026-10-11 위원회 페이지 기준 ISO/DIS, 단계 40.60(2026-09-10 투표 종료), ISO 3691-4:2023 대체 예정. 기존 'ISO/CD' 제목을 갱신한다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-211",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합",
      "published": "2022-10-12",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010083660",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B ISO 10218-2 목록(기존 출처). 이번에 국가표준인증 통합정보시스템 상세에서 ISO 10218-2:2011 IDT, 최종개정확인일 2022-10-12(고시 2022-0433)를 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-555",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery",
      "published": "2023-06",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "EU 기계 규정. 이번에 2026-07-27 통합본(M1 2024/2748, M2 2026/1744 반영)에서 부속서 III 1.2.1(f) 5년 추적 기록과 둘째 목록 (b) 1년 보존, 제54조 적용일을 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1122",
      "org": "Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121)",
      "title": "Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports",
      "published": "2024",
      "url": "https://eprints.whiterose.ac.uk/id/eprint/217393/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OSHA 중상 보고 로봇 관련 사고 분석(기존 출처). 이번에 저자 공개 원고에서 분석 기간(2015-01-01~2022-04-30), 연방 관할 범위, 서술 단어 수 중앙값 36 을 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1121",
      "org": "Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI)",
      "title": "Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions",
      "published": "2021-06-29",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "역할극 증언 면담 연구(기존 출처). 이번에 2020-11 Zoom 면담 22회와 정지 이미지 한계를 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (ros2/rosbag2 GitHub)",
      "title": "rosbag2 — README (Recording and playback of ROS 2 communications)",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "rosbag2 README(기존 출처). 이번에 태그 0.35.0 판(rosbag2_transport CHANGELOG 0.35.0 = 2026-09-12)에서 repeat-transient-local, 스냅샷 모드 순환 버퍼, 유실 메시지 통계를 확인했다. 태그 커밋 날짜는 확인하지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1096",
      "org": "MCAP 프로젝트 (Foxglove)",
      "title": "MCAP Format Specification",
      "published": null,
      "url": "https://mcap.dev/spec",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "MCAP 포맷 명세(기존 출처). 이번에 커밋 f7069e6 고정판에서 publish_time 대체 규칙과 CRC 0 의미를 확인했다. 고정 커밋 날짜는 확인하지 못했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-1118",
      "org": "산업통상자원부",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시",
      "published": "2023-11-17",
      "url": "https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "고시 제2023-211호(2023-11-17 제정, 기존 출처). 이번에 첨부 HWP 에서 별표 3 의 16개 기준 항목과 제9조, 부칙('2023년 11월 17일부터 시행')을 확인했다. 현행은 제2025-21호(ref-1505)로 개정됐다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    },
    {
      "id": "ref-980",
      "org": "한국로봇산업진흥원",
      "title": "실외이동로봇 운행안전인증",
      "published": null,
      "url": "https://www.kiria.org/portal/cert/portalCertEstiSafe.do",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "인증기관 안내 페이지(기존 출처). 이번 재열람에서 8개 심사항목과 '인증 신청일로부터 30일 이내' 처리기간을 다시 확인했다.",
      "cited_by": [
        "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-230",
      "question": "출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가?",
      "areas": [
        49,
        50
      ],
      "status": "해결",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시"
    },
    {
      "action": "update",
      "id": "oq-384",
      "question": "출처 충돌: ISO 3691-4 차기판 프로젝트의 현재 단계는 위키 기록(2026-09-26, ISO/CD 3691-4)과 외부 조사 메모(ISO/DIS 3691-4 제3판, 2026-09-10 단계 40.60) 가운데 어느 쪽인가? (관련 기존 질문 oq-170)",
      "areas": [
        48,
        50
      ],
      "status": "해결",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md"
    },
    {
      "action": "new",
      "question": "윤리적 블랙박스 초안의 날짜·시각·체크섬 표기 충돌을 해소한 후속 판이 있는가, 서로 다른 제조사의 로봇 결정 코드를 공통 사건 유형으로 옮기는 공개 매핑이 있는가?",
      "areas": [
        50,
        37
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "rosbag2 스냅샷·repeat-transient-local·유실 통계를 쓴 사고 전후 기록을 현장 설정(스냅샷 트리거 지연, 전원 상실, 정적 토픽 depth, 유실 이벤트 누락)에서 시험해 보존 길이와 누락을 검증한 사례가 있는가?",
      "areas": [
        50,
        43
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "MCAP 의 publish_time 이 log_time 으로 대체된 경우와 원본 추출·해시·서명 이력을 사고 증거 묶음에 어떻게 표시하고 검증할 것인가?",
      "areas": [
        50,
        38
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: 실외이동로봇 운행안전인증 고시 제2023-211호의 시행일은 원 고시 첨부 부칙(2023-11-17)과 제2025-21호 첨부 본문에 실린 구 부칙(2023-11-21) 가운데 어느 쪽인가?",
      "areas": [
        50,
        66
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EN ISO 10218-1/-2:2025 참조는 기계 규정 (EU) 2023/1230 의 조화 표준으로 언제 게재되며, 지침 2006/42/EC 기반 목록(시행결정 2023/1586)이 2027-01-20 폐지된 뒤 적합성 추정은 어떻게 이어지는가?",
      "areas": [
        50,
        59
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "제조 공장",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "제약",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/safety/safety-standards-certification-and-incident-investigation.md#5-적용-사례-현장-유형-명시",
      "title": "50. 안전 표준·인증·사고 조사"
    }
  ],
  "additional_research_requests": [
    "4·7절 후속: 이전 판 주제 페이지 docs/topics/2026/2026-09-30-area50-s4.md(41행 '적합성 추정')와 docs/topics/2026/2026-09-30-area50-s7.md(42행 EN ISO 10218 IBF 해설 단독 사실 표기, 45행 '절차·기준은 고시 제2023-211호가 정한다')의 본문이 이번 입력에 없어 해당 줄을 직접 고치지 못했다. 이번 판 4·7절이 같은 서술을 대체한다고 밝혀 두었다. 다음 갱신 실행에 두 페이지를 입력으로 넣어 강등과 고시 근거 정정을 그 페이지에도 반영해야 한다.",
    "6절: CAST 의 원어 풀이(강의 자료 원문 기준)와, 로봇·플릿 사고에 CAST 를 적용한 실증 사례가 필요하다. 약어를 처음 쓸 때 원어를 함께 적는 규칙을 지키고, 지금 의견으로 둔 플릿 적용 절차를 사실로 뒷받침하기 위해서다.",
    "5절 실외 사례: 구 별표 3 의 알림음·등화장치·물리적 보안·통신장애 대응 기준이 세부운영지침 같은 다른 규정으로 옮겨졌는지 확인해야 한다. oq-186 을 닫는 데 필요하다.",
    "5절: 병원·상업 시설의 안전 인증·사고 조사 사례가 필요하다. 현재 이 두 현장 유형에는 사례가 없다.",
    "8절: Suresh 외(2026) 본문을 확인해야 한다. 85% 의 분모(n)와 발생률을 계산하지 않았는지를 본문으로 확인하기 위해서다. 이번에는 초록까지만 확인했다."
  ],
  "fixes_applied": [
    "f3 강등 — 4절 '적합성 추정' 항목과 7절 'EN ISO 10218:2025 요구 변경 해설' 행에서 PL d·범주 3 대체와 정상 정지 기능 신설 서술을 추정으로 쓰고, 'IBF Solutions(컨설팅사) 해설, 벤더 주장'을 함께 적었으며 각주는 [^ref-1116] 하나만 달았다. 분리 페이지 2026-09-30-area50-s4·s7 은 본문이 입력에 없어 해당 줄을 직접 고치지 못했다. 그래서 4·7절 머리에 이번 판이 이전 판의 같은 항목·행을 대체한다고 적고, changelog_entry 와 additional_research_requests 에 후속 정정을 남겼다.",
    "f1·f2 — 4절과 7절의 EU 조화 게재 서술을 [^ref-1496] 근거의 사실로 고쳐 썼다. 2026-09-04 채택, 2026-09-07 게재, 2023/1586 부속서 I 에 223a·224a 추가, 기계류 지침 2006/42/EC 에 대한 적합성 추정, 2027-01-20 목록 폐지를 적고, 규정 (EU) 2023/1230 에 따른 게재가 아니라고 밝혔다. 규정 쪽 게재 시점은 11절과 open_question_updates 에 새 열린 질문으로만 두었다.",
    "고시 번호 표기 — 페이지에서 처음 나오는 5절 실외 사례의 시작 조건 칸에 '산업통상부 고시 제2025-21호(첨부 고시문 표기 제2025-021호, 2025-11-24 발령·시행)'로 쓰고, 그 뒤 본문은 모두 '제2025-21호'로 통일했다. 각주와 reference_updates 의 출처 제목 문자열만 원문 제목(제2025-021호)을 유지했다.",
    "f14·f15 — 5절 실외 사례 서술과 7절 '실외이동로봇 운행안전인증 고시' 행을 '제2023-211호(2023-11-17 발령)를 제2025-21호가 2025-11-24 개정했고 발령일부터 시행한다'로 고쳤다(사실, [^ref-1505]). 제2023-211호의 시행일은 원 고시 부칙(2023-11-17)과 개정 고시에 실린 구 부칙(2023-11-21)을 둘 다 추정으로 제시하고 어느 쪽도 고르지 않았으며, 출처 충돌 질문을 11절에 두었다.",
    "f13·f17~f20 — 5절 실외 사례의 제약 칸을 구 별표 3 의 16개 항목(ref-1118), 현행 별표 3 의 8개 항목(ref-1505·ref-980), 2025-11 통폐합(ref-1504)으로 다시 썼다. 항목 대응과 새 별표에 없는 항목(알림음·등화장치·물리적 보안)은 서술과 Mermaid 도식으로 적었다. '어느 쪽도 고르지 않고 함께 둔다' 문구는 지웠다. 기준값 문장은 ref-992 대신 ref-1118(확정 고시 별표 3) 근거로 바꾸고, 현행 판에 어떤 기준이 남았는지를 덧붙였다. 다른 규정으로 옮겨졌는지는 '미확인'으로 밝혔다.",
    "f16 — 5절 실외 사례의 시작 조건 칸에 30일 처리기간의 근거로 고시 제9조①을, 경위로 60일에서 30일로 줄인 일을 더했다. 서류 보완 기간이 들어가는지는 '미확인'으로 적었다.",
    "f21·f22·f45 — 9절 업종별 조건 행의 외부 연계 칸에 관제장치 요구(실시간 위치·속력·배터리·통신 감도·상태, 원격 정지)와 관제장치 모델 단위 보관을 각각 '연계 대상: '으로 시작해 넣었다. 표 아래의 구축자 의견에서 ROP 계층이 인증상 관제장치인지는 판단하지 않고 oq-187 로 남겼다.",
    "f4/ref-1255 — 7절 R15.08-3 행을 추정으로 두었다. 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙였고, reference_updates 의 ref-1255 에 source_unopened: true 를 넣었다.",
    "f5/ref-789 — 7절에 ISO/DIS 3691-4 제3판 행(40.60, 2026-09-10, ISO 3691-4:2023 대체 예정, 아직 발행된 개정판 아님)을 더했다. reference_updates 와 각주에서 ref-789 제목을 'ISO/DIS 3691-4 (제3판) - …'으로 바꿨다.",
    "f7 — 7절 KS 행에 'KS B ISO 10218-2 의 최종 확인일은 2022-10-12(ISO 10218-2:2011 IDT)'로 적고, 2017 확인이 틀렸다는 표현은 쓰지 않았다. 2026-09-26-area25-s7.md 45행과 ref-814 제목은 pages 에 넣지 않고 changelog_entry 에만 후속 정리 대상으로 적었다.",
    "f12 — 7절 UL 3300 행을 추정으로 쓰고 '벤더 주장: 인증기관 UL Solutions 의 상업 보도자료'를 함께 적었다. 이종 플릿 전체의 안전 입증으로 읽지 않는다고도 밝혔다.",
    "f8·f9·f46 — 7절 EU 기계 규정 행에서 5년 기록은 안전 소프트웨어 개입 데이터와 업로드한 판의 추적 기록, 1년 보존은 스스로 진화하는 제어 시스템의 안전 결정 데이터로 한정하고, 목적은 관할 당국이 이유를 들어 요청할 때의 적합성 입증뿐이라고 적었다. 일반 작업 로그나 플릿 전체 보관 의무로 읽지 않는다고 밝히고 59. 법·규제·보험·라이선스로 연결했다.",
    "f27·f28/ref-1501 — 8절 Suresh 외 항목과 각주의 발행일을 '2026-03-03(온라인 선공개)'로 쓰고, 69(5):345–357 은 'Crossref 기준'으로 표시했다. 85%·75.7% 는 초록 수치이며 노출 인원당 발생률이 아니라고 적었다. reference_updates 의 published 도 2026-03-03 으로 맞췄다.",
    "f24~f26 — 8절 Sanders 외 항목과 4절 '중상 보고' 항목의 기간을 2015-01-01~2022-04-30 으로 고치고, 연방 OSHA 관할만 들어 있고 주 계획 22개 주는 빠진다는 점을 적었다. 서술 단어 수 중앙값 36 은 77건 보고의 서술 길이 지표일 뿐 원인 정밀도나 발생률이 아니라고 함께 썼다.",
    "f29·f30 — 5절 제조 공장에 공단 공개 재해사례(용접 팁 교체 중 로봇 팔과 지그 사이 끼임 사망)를 별도 사례로 더했다. 발생일은 '미확인'으로 적고, 오뚜기·고성 기사 사건과는 연결하지 않고 별개로 다룬다고 밝혔다. 근거가 없는 완료·인계 칸은 '해당 없음'으로 두었다.",
    "f31·f32·f49 — 6절 CAST 소절에 출처를 '2016년 봄 학기 MIT OCW 강의 자료'로 쓰고, 예시가 화학 공장 SO2 탱크 넘침 사례이며 로봇 사고에 적용한 실증은 확인하지 않았다고 밝혔다.",
    "f35~f38 — 6절 '사고 기록 장치' 소절은 EBB 초안 안의 표기 충돌(날짜·시각·체크섬), 결정 코드를 제조사·운영자에게 맡긴 점, RD 순환 덮어쓰기와 고정 보존 기간이 없다는 점으로만 썼다. 특정 길이·형식을 규범 값으로 제시하지 않았고, ref-1503(ICRES 2022 게재본)과 ref-1120(arXiv 판)이 같은 연구의 다른 판임을 밝혔다.",
    "f39~f43 — 7절 rosbag2·MCAP 행을 사고 증거 보존 관점으로만 짧게 썼다. 기준판(rosbag2 0.35.0 태그, MCAP 커밋 f7069e6)과 확인일 2026-10-11 을 밝히고, 37. 관제 화면·실행 기록과 43. 데이터·관측성·배포로 연결했다.",
    "f44~f49 — 의견 문장(7절 f44·f46·f48, 8절 f47, 9절 f45, 6절 f49)은 모두 '구축자 의견:'으로 시작하게 했고, 각주는 브리프의 source_ids 에 적힌 출처만 달았다.",
    "11절 — oq-230(근거 ref-1118·ref-1505)과 oq-384(근거 ref-789)를 해결로 바꾸고 open_question_updates 에 update 로 냈다. oq-186 은 부분 답(시점·근거 고시, 흡수·누락 항목)만 적고 열림을 유지했다. oq-251·oq-123·oq-252·oq-333·oq-187 에는 부분 근거만 덧붙였다. 브리프의 새 열린 질문 5건은 11절과 open_question_updates(new)로 등록했다.",
    "범위 밖 페이지(docs/categories/safety/index.md 177행, 2026-09-26-area25-s7.md 45행, 2026-09-30-area52-s3.md 43행)는 pages 에 넣지 않고 changelog_entry 에만 후속 정리 대상으로 적었다.",
    "2차: 10절 이전 판 링크 — append 패치의 추가 내용 맨 앞에 '이전 판(2026-09-30)의 연결 목록은 [50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area50-s10.md)에 있다.' 문장을 원 페이지 기준 상대 경로로 넣었다.",
    "2차: 10절 59 항목 — '법적 효력 해석은 59번 영역으로 넘긴다'를 '법적 효력 해석은 59. 법·규제·보험·라이선스 로 넘긴다'로 고쳤다.",
    "2차: 6절 CAST 소절 — '조사 질문은 세 가지다.'를 '강의 자료는 다음을 조사 질문으로 던진다.'로 고쳐 질문 개수를 단정하지 않게 했다.",
    "2차: 5절 용접 팁 교체 사례 제약 칸 — '공단의 재발방지대책은 세 가지다.'를 '공단의 재발방지대책은 다음을 제시한다.'로 고쳤다.",
    "2차: 프런트매터 sources — 4절 패치의 frontmatter sources 에서 분리 페이지에서만 인용되는 ref-1497·ref-1498·ref-1499·ref-1500·ref-1255·ref-211·ref-555·ref-831·ref-1096 을 빼고, 원 페이지 본문과 13절에 남는 22건(ref-1084, ref-991, ref-1115, ref-1116, ref-1117, ref-980, ref-1118, ref-945, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-563, ref-1496, ref-1501, ref-1502, ref-1503, ref-1504, ref-1505, ref-1506, ref-789)으로 맞췄다. 재분리 결과가 달라지면 원 페이지에 남은 각주 기준으로 맞춘다.",
    "분량 초과 자동 분리: 50. 안전 표준·인증·사고 조사 본문 17,990자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 7,554자"
  ],
  "standards_updates": [
    {
      "name": "UL 3100 Automated Mobile Platforms (AMPs)",
      "kind": "표준",
      "org": "UL Standards & Engagement",
      "url": "https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=39063",
      "related_areas": [
        50
      ],
      "summary": "자동 이동 플랫폼 안전 표준. 제1판 2021-05-26 발행, 최근 개정·ANSI 승인 2026-06-10. 적용 범위에서 산업용 로봇 자체(UL 1740·CSA Z434)는 제외하고 해당 표준에 맞는 매니퓰레이터의 탑재를 허용한다.",
      "ref_id": "ref-1498"
    },
    {
      "name": "UL 3300 (SCIEE 로봇 표준, Simbe Tally 인증 발표)",
      "kind": "표준",
      "org": "UL Solutions",
      "url": "https://www.ul.com/news/ul-solutions-grants-its-first-global-certification-public-facing-robot-simbes-tally-autonomous",
      "related_areas": [
        50,
        64
      ],
      "summary": "UL Solutions 가 2026-03-11 매장용 자율이동로봇 Tally 의 UL 3300 인증을 발표했다(벤더 주장, 인증기관 상업 보도자료 기준, 인증서 미공개).",
      "ref_id": "ref-1499"
    },
    {
      "name": "ISO/DIS 3691-4 (제3판) 무인 산업용 트럭과 그 시스템 안전 요구·검증 개정안",
      "kind": "표준",
      "org": "ISO",
      "url": "https://www.iso.org/standard/88615.html",
      "related_areas": [
        50,
        48
      ],
      "summary": "ISO 3691-4:2023 을 대체할 개정 프로젝트. 2026-10-11 기준 단계 40.60(투표 종료 2026-09-10)이며 아직 발행되지 않았다.",
      "ref_id": "ref-789"
    },
    {
      "name": "KS B ISO 10218-1 산업용 로봇의 안전에 관한 요구사항 — 제1부: 로봇",
      "kind": "표준",
      "org": "국가기술표준원",
      "url": "https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503",
      "related_areas": [
        50,
        62
      ],
      "summary": "ISO 10218-1:2011 과 일치(IDT)하는 국가표준. 최종개정확인일 2021-11-26. ISO 10218-1:2025 부합판은 2026-10-11 목록에서 확인되지 않았다.",
      "ref_id": "ref-1497"
    },
    {
      "name": "산업용 로봇 자율안전확인",
      "kind": "평가 프로그램",
      "org": "안전보건공단 산업안전보건인증원",
      "url": "https://miis.kosha.or.kr/oshci/busi/viewMiisJayulMerchandiseInfo.do",
      "related_areas": [
        50,
        62
      ],
      "summary": "자율안전확인 대상 산업용 로봇을 3축 이상 매니퓰레이터와 전용 제어기를 갖추고 프로그램·자동제어가 가능한 고정식 로봇으로 정의한다.",
      "ref_id": "ref-1500"
    },
    {
      "name": "위원회 시행결정 (EU) 2026/2015 (기계류 지침 조화 표준 목록 개정·폐지)",
      "kind": "프레임워크",
      "org": "European Commission",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015",
      "related_areas": [
        50,
        59
      ],
      "summary": "EN ISO 10218-1/-2:2025 참조를 기계류 지침 2006/42/EC 조화 표준 목록(2023/1586 부속서 I)에 추가했다(2026-09-07 관보 게재). 이 목록은 2027-01-20 부로 폐지된다.",
      "ref_id": "ref-1496"
    }
  ]
}
```

### runs/2026-10-11-06/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md (9개 절)
- 분량 초과 자동 분리:
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-11-area50-s7.md (4,831자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "11. 열린 질문" → docs/topics/2026/2026-10-11-area50-s11.md (2,163자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-11-area50-s6.md (1,504자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-11-area50-s8.md (1,484자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-11-area50-s4.md (878자)
    - docs/categories/safety/safety-standards-certification-and-incident-investigation.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-11-area50-s10.md (606자)
```

### runs/2026-10-11-06/pages/categories/safety/safety-standards-certification-and-incident-investigation.md

````markdown
---
title: "50. 안전 표준·인증·사고 조사"
type: area
category: "M. 안전"
area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [ISO 10218, EU 조화 표준, 실외이동로봇 운행안전인증, 윤리적 블랙박스, 사고 조사, 잠금·표지]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-11
sources: [ref-1084, ref-991, ref-1115, ref-1116, ref-1117, ref-980, ref-1118, ref-945, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-563, ref-1496, ref-1501, ref-1502, ref-1503, ref-1504, ref-1505, ref-1506, ref-789]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [M. 안전](index.md) › 50. 안전 표준·인증·사고 조사

# 50. 안전 표준·인증·사고 조사

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]

## 3. 왜 중요한가

따를 안전 표준과 인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년에 개정 중이어서, 여러 제조사 로봇을 함께 운영하는 ROP는 적용 기준을 한 번 정하고 끝낼 수 없는 것으로 보인다. [추정][^ref-1115][^ref-1117][^ref-980][^ref-945]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 왜 중요한가](../../topics/2026/2026-09-30-area50-s3.md)에 있다.

## 4. 핵심 개념과 용어

표준 개정과 사고 자료를 읽으려면 다음 용어를 알아야 한다. 이번 갱신에서 '적합성 추정'은 EU 관보 원문으로, '중상 보고'는 연구 원고로 다시 확인했다. [사실][^ref-1496][^ref-1122]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-10-11-area50-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 사례는 네 가지다. 제조 공장·물류창고의 사고(보도 2건, 안전보건공단 공개 재해사례 1건), 실외 로봇의 법정 인증, 가정의 모의 사고 조사, 건설 현장의 위험성평가다. 병원·상업 시설의 안전 인증·사고 조사 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 제조 공장

**사례:** 식품 제조 공장에서 멈춘 적재 로봇을 점검하던 노동자의 끼임 사망 사고(2026-09)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 2026-09-21 제품 적재용 로봇이 멈춰 노동자가 점검에 나섰다. [사실][^ref-1125] |
| 작업 대상 | 멈춘 제품 적재용 로봇과 그 로봇을 점검하던 노동자 [사실][^ref-1125] |
| 수행 자원 | 점검 노동자와 적재 로봇 [사실][^ref-1125] |
| 제약 | 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다. [사실][^ref-1125] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 노동자가 끼여 2026-09-25 숨졌다. 노동부 통영지청은 산업안전보건법·중대재해처벌법 위반을 조사하고 있다. [사실][^ref-1125] |

재가동 경위는 조사 쟁점이다. 경찰은 다른 노동자가 작업 중임을 확인하지 않고 재가동했는지, 기계 오작동인지를 수사 중이며, 원인은 확정되지 않았다(원인 미확정, 2026-09-29 보도 기준). [사실][^ref-1125] 이 사례에서 이 영역은 예외·성과 항목, 곧 사고 뒤 누가 무엇을 조사하는가에 관여한다.

**현장 유형:** 제조 공장

**사례:** 로봇 용접기의 용접 팁을 교체하다 로봇 팔과 지그 사이에 끼인 사망 사고(안전보건공단 공개 재해사례, 발생일 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇 용접기의 용접 팁을 교체하는 작업이었다. [사실][^ref-1502] |
| 작업 대상 | 로봇 용접기의 로봇 팔·지그와 셀 안에 들어간 작업자 [사실][^ref-1502] |
| 수행 자원 | 용접 팁을 교체하던 작업자와 작동 중이던 로봇 팔 [사실][^ref-1502] |
| 제약 | 공단의 재발방지대책은 다음을 제시한다. 출입할 때 감응식 방호장치가 작동하게 하고, 일시중지(muting) 기능을 쓸 때는 다른 수단으로 안전을 유지하며, 수리·점검 같은 비정형 작업은 로봇 운전을 정지한 뒤 출입문으로 들어가 한다. [사실][^ref-1502] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 작업자가 작동 중인 로봇 팔과 지그 사이에 가슴이 끼여 숨졌다(광주 광산구 사업장, 발생일 미확인). [사실][^ref-1502] |

공단은 원인을 두 가지로 든다. 일시중지(muting) 기능을 써서 감응식 방호장치가 작동하지 않았다. 또 작업자가 로봇 운전을 정지하지 않은 채, 안전 조치가 없는 재료 투입구를 통해 셀에 들어갔다. [사실][^ref-1502] 이 사례는 위아래의 보도 사례와는 별개로 다룬다. 이 사례에서 이 영역은 예외·성과 항목에 관여한다. 곧 공식 재해 조사가 원인을 방호장치 우회와 정지 절차 누락으로 정리하는 방식이다(조사 방법은 6절).

**현장 유형:** 물류창고

**사례:** 농산물유통센터에서 상자를 선별해 팔레트로 옮기는 로봇의 점검 중 압착 사망 사고(2023-11)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하는 작업이었다. [사실][^ref-1124] |
| 작업 대상 | 파프리카 상자를 선별해 팔레트로 옮기는 산업용 로봇 [사실][^ref-1124] |
| 수행 자원 | 산업용 로봇과 점검 작업자 [사실][^ref-1124] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 2023-11-07 작업자가 로봇에 압착되어 숨졌다. 경찰은 로봇이 사람을 상자로 인식한 것으로 보고 안전관리 책임자의 과실 여부를 수사했다(2023-11-08 보도 기준). [사실][^ref-1124] |

두 사고 모두 정상 운전이 아니라 점검과 작동 확인 같은 비정상 작업 중에 일어났다. [사실][^ref-1124][^ref-1125]

**현장 유형:** 실외

**사례:** 연계 대상: 보도를 운행하는 실외이동로봇의 운행안전인증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 연계 대상: 인증을 신청하면 심사가 시작된다. 산업통상부 고시 제2025-21호(첨부 고시문 표기 제2025-021호, 2025-11-24 발령·시행) 제9조①은 인증기관이 인증신청서를 받은 날부터 30일 안에 심사 결과를 알리도록 정한다. 한국로봇산업진흥원도 처리기간을 신청일부터 30일 이내로 안내한다(확인일 2026-10-11). [사실][^ref-1505][^ref-980] 정부 보도참고자료(2025-11-27)는 심사기간을 60일에서 30일로 줄였다고('25.11 시행) 적는다. 구 고시 제2023-211호 제9조①에는 이런 기한이 없었다. [사실][^ref-1504][^ref-1118] 서류 보완 기간이 30일에 들어가는지는 미확인이다. |
| 작업 대상 | 최대 질량 500kg·최고 속도 15km/h 이하 실외이동로봇 [사실][^ref-980] |
| 수행 자원 | 지능형로봇법 제40조의2 에 근거한 인증을 한국로봇산업진흥원이 맡는다. [사실][^ref-980] 인증기관은 로봇 제품명·모델명과 함께 관제장치 제품명·모델명을 보관한다(제10조②). 현행 별표 3 은 관제장치가 운용 중인 모든 로봇의 위치·속력, 주행가능 거리 또는 배터리 잔량, 통신 신호 감도, 상태를 실시간으로 확인하고 로봇을 원격으로 정지할 수 있어야 한다고 정한다. [사실][^ref-1505] |
| 제약 | 구 고시 제2023-211호 별표 3 의 기준 항목은 16개였다. 질량 및 폭 제한, 운행 속도, 겉모양, 동적 안정성, 비상정지, 운행구역 준수, 속도 제어, 장애물 감지, 알림음, 등화장치, 방수 성능, 물리적 보안, 횡단보도 통행, 관제장치, 통신장애 대응, 원격조작이다. [사실][^ref-1118] 현행 제2025-21호 별표 3 의 항목은 8개다. 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치이며, 진흥원이 안내하는 8개 심사항목과 이름이 같다. [사실][^ref-1505][^ref-980] 정부는 2025-11 심사 평가항목을 16개에서 8개로 합쳤다고 밝혔다. [사실][^ref-1504] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

연계 대상: 인증 절차와 기준은 산업통상자원부 고시 제2023-211호(2023-11-17 발령)로 처음 정해졌다. 이 고시는 지능형로봇법(법률 제19412호) 개정 시행에 따라 만들어졌고, 별표에서 로봇 모델 구분, 최고속도, 최대폭, 최대질량, 운행안전성 기준을 다뤘다. [사실][^ref-1118] 제2025-21호가 2025-11-24 제2023-211호(2023-11-17 발령)를 개정했고, 발령일부터 시행한다. [사실][^ref-1505] 제2023-211호의 시행일은 원 고시 첨부 부칙에 2023-11-17, 제2025-21호 첨부 본문에 실린 구 부칙에 2023-11-21 로 서로 다르게 적혀 있다. 그래서 어느 쪽으로도 확정하지 않는다(11절의 출처 충돌 질문). [추정][^ref-1118][^ref-1505]

두 별표를 조문끼리 맞춰 보면 구 별표의 항목이 다음처럼 합쳐졌다. 질량·폭 제한과 운행 속도는 '규격 및 운행속도'로, 동적 안정성(5° 경사·30mm 턱)과 속도 제어(정확도 ±10%)는 '동적 특성'으로 들어갔다. 운행구역 준수와 장애물 감지는 '주변 인식'으로, 관제장치와 원격조작(원격 정지, 영상으로 주변을 확인하는 원격 수동조작)은 '관제장치'로 합쳐졌다. [사실][^ref-1118][^ref-1505] 알림음(55~73dB(A)), 등화장치(표면 60℃ 이하), 물리적 보안(통신포트·저장장치 단자 보호)은 새 별표에 없다. 통신장애 대응(운행계획서 시나리오)은 '횡단보도 통행 중 통신이 끊기면 안전한 곳에 정차한다'는 조항으로만 남았다. [사실][^ref-1118][^ref-1505] 빠진 항목이 세부운영지침 같은 다른 규정으로 옮겨졌는지는 미확인이다. 아래 도식은 이 대조를 보여 준다. 점선은 이름이 같은 항목, 또는 일부 조항만 남은 항목이다.

```mermaid
flowchart LR
  subgraph OLD["구 고시 제2023-211호 별표 3 (16개 항목)"]
    o1["질량 및 폭 제한"]
    o2["운행 속도"]
    o3["겉모양"]
    o4["동적 안정성"]
    o5["비상정지"]
    o6["운행구역 준수"]
    o7["속도 제어"]
    o8["장애물 감지"]
    o9["알림음"]
    o10["등화장치"]
    o11["방수 성능"]
    o12["물리적 보안"]
    o13["횡단보도 통행"]
    o14["관제장치"]
    o15["통신장애 대응"]
    o16["원격조작"]
  end
  subgraph NEW["현행 고시 제2025-21호 별표 3 (8개 항목)"]
    n1["규격 및 운행속도"]
    n2["겉모양"]
    n3["동적 특성"]
    n4["주변 인식"]
    n5["비상정지"]
    n6["방수 성능"]
    n7["횡단보도 통행"]
    n8["관제장치"]
  end
  GONE["새 별표에 없음 (다른 규정 이동 여부 미확인)"]
  o1 --> n1
  o2 --> n1
  o3 -. 같은 이름 .-> n2
  o4 --> n3
  o7 --> n3
  o6 --> n4
  o8 --> n4
  o5 -. 같은 이름 .-> n5
  o11 -. 같은 이름 .-> n6
  o13 -. 같은 이름 .-> n7
  o15 -. 통신 단절 시 정차 조항만 .-> n7
  o14 --> n8
  o16 --> n8
  o9 --> GONE
  o10 --> GONE
  o12 --> GONE
```

이전 판은 일부 기준값을 '2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인'으로 두었다. 질량별 속도 제한(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 800mm 이하(보도 폭 2,500mm 이상이면 1,200mm), 5° 경사, 알림음 55~73dB, 등화장치 표면 온도 60℃ 이하, 방수 IPX4 다. 이 값들은 확정 고시 제2023-211호 별표 3 에 그대로 있다. [사실][^ref-1118] 현행 제2025-21호 별표 3 에는 질량·폭·속도·5° 경사·IPX4 기준이 남았고, 알림음·등화장치 기준은 없다. 두 판 모두 어린이·노인·장애인 보호구역에서 최대 5km/h 를 지키는지 확인하는 조항을 둔다. [사실][^ref-1118][^ref-1505] ROP 는 인증 자체를 맡지 않는다. 인증이 허용한 운행 조건을 작업·경로 제약으로 받아들이는 쪽에서 이 사례에 관여한다(9절). [추정][^ref-980]

**현장 유형:** 가정

**사례:** 실제 사고가 아닌 역할극 모의 사고(노인 지원 주거 공동체 시나리오) — 넘어진 거주자 곁 보조 로봇의 알림 실패 조사

| 항목 | 내용 |
|---|---|
| 시작 조건 | 지원 주거 아파트에서 거주자가 넘어졌다(모의). [사실][^ref-1121] |
| 작업 대상 | 넘어진 거주자와 그 사실을 직원에게 알리는 정보(모의) [사실][^ref-1121] |
| 수행 자원 | 보조 로봇과 직원, 그리고 사고를 조사하는 조사자(모의) [사실][^ref-1121] |
| 제약 | 로봇이 인터넷에 연결되지 않은 상태였다(모의 조건). [사실][^ref-1121] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 보조 로봇이 오작동해 직원에게 알리지 못했다(모의). 조사는 목격자 증언, 윤리적 블랙박스 기록, 환경·로봇 전문가 분석, 기술·조직 권고로 구성되었다. [사실][^ref-1121] |

Webb 외(2021)는 이 모의 사고를 역할극 증언 면담으로 조사해 조사 방법을 시험했다. 실제 사고 자료가 아니므로 방법의 시험 사례로만 읽는다. [사실][^ref-1121]

**현장 유형:** 기타

**사례:** 건설 현장에 이동로봇을 배치하기 전의 위험성평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 건설 현장에 이동로봇을 배치하기 전 위험성평가 틀이 필요한 상황이다. [사실][^ref-563] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 해당 없음 |
| 제약 | ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 다양한 배치 상황에 적용할 수 있는 표준이 없고 이동 플랫폼의 위험성평가 문헌도 제한적이었다. [사실][^ref-563] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

Belzile 외(2025)는 이 공백을 메우려고 건설 현장 이동로봇 배치용 위험성평가 틀을 제안했다(프리프린트). [사실][^ref-563]

## 6. 대표 접근법과 기술

사고 기록에 관한 공개 규약 초안은 아직 필드 형식과 보존 기간을 정하지 않았다. 사고 원인을 제어 구조와 조직 정책까지 넓혀 묻는 분석 방법은 이번 조사에서 강의 자료 수준으로만 확인했다. [추정][^ref-1503][^ref-1506]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area50-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

EN ISO 10218-1/-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015(2026-09-07 관보 게재)로 기계류 지침 2006/42/EC 의 조화 표준 목록에 실렸다. 실외이동로봇 운행안전인증 기준은 2025-11-24 개정 고시로 8개 항목이 되었다. [사실][^ref-1496][^ref-1505]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area50-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 판은 미국 연방 OSHA 중상 보고 분석(2015-01-01~2022-04-30)과 Ohio 산재보상 청구 분석(2001~2020)을 다룬다. 두 자료는 관할·기간·집계 단위가 다르다. [사실][^ref-1122][^ref-1501]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 대표 연구와 자료](../../topics/2026/2026-10-11-area50-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 범위는 인증 상태·적용 표준과 판·허용 운행 조건을 등록해 배정·경로 제약에 반영하고, 사고 조사에 쓸 플릿 수준 실행 기록을 보존하는 일로 보인다. [추정][^ref-980][^ref-1116][^ref-1120][^ref-1122]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇·적용마다 인증 상태와 적용 표준·판을 등록 정보로 관리하고, 정지·재가동·정비 모드 전환 명령과 로봇 상태 보고를 사고 조사에 쓸 수 있게 보존한다. [추정][^ref-1116][^ref-1120] | 연계 대상: 로봇 본체의 표준 적합성과 제품 인증은 제조사와 인증기관이, 로봇 셀·이동로봇 적용의 위험성평가와 사용 정보는 통합자가 맡는다. [추정][^ref-1115][^ref-1084] |
| 업종별 조건 | 인증이 허용한 운행 조건(질량·속도·구역)을 배정·경로 제약에 반영하고 표준 판 개정을 추적한다. [추정][^ref-980][^ref-1116] | 연계 대상: 실외 운행 인증과 보험은 운영자와 한국로봇산업진흥원의 일이다. [추정][^ref-980][^ref-991] 연계 대상: 현행 고시 제2025-21호 별표 3 은 관제장치에 다음을 요구한다. 운용 중인 모든 로봇을 식별하고, 위치·속력, 주행가능 거리 또는 배터리 잔량, 로봇–관제장치 통신 신호 감도, 상태(주행·대기·비상정지·오류)를 실시간으로 확인한다. 통행할 수 없으면 관제장치에 알리고 관리자가 조치하며, 원격 정지 수단과 영상장치로 주변을 보며 조작하는 원격 수동조작을 갖춘다. [사실][^ref-1505] 연계 대상: 같은 고시 제10조②는 인증기관이 인증번호·회사명·로봇 제품명·모델명과 함께 관제장치 제품명·모델명을 보관하게 한다. 따라서 인증 정보는 로봇 모델과 관제장치 모델의 조합으로 관리된다. [사실][^ref-1505] |
| 시설·설비 제어 | 사고 조사에 필요한 실행 기록을 외부 주체와 주고받는 인터페이스를 둔다. [추정][^ref-1125] | 연계 대상: 교육·작업 절차·잠금·표지는 사용자 사업장이, 법정 사고 조사는 고용노동부·경찰이 맡는다. [추정][^ref-1084][^ref-1125] |

실외이동로봇 운행안전인증처럼 인증 자체는 운영자·진흥원의 일이고, ROP는 그 결과를 받아 작업·경로 제약으로 반영하는 쪽이다. [추정][^ref-980] 이 경계는 제품 전략에 따라 옮겨질 수 있으며 기준은 [범위 경계](../../about/scope-boundary.md)에 있다. 이종 제조사를 연결하는 ROP는 각 주체의 인증·평가 결과와 조사에 필요한 실행 기록을 주고받는 인터페이스를 맡는 것으로 보인다. [추정][^ref-1115][^ref-1084][^ref-1125]

구축자 의견: 실외이동로봇 인증 정보에는 고시 번호·시행일(제2025-21호, 2025-11-24)과 별표 판(구 16개 항목, 현행 8개 항목)을 함께 기록해야 한다. 그래야 구 별표로 받은 인증과 현행 별표 기준을 구분할 수 있다. 현행 관제장치 항목이 요구하는 실시간 상태(위치·속력·배터리·통신 감도·상태)와 원격 정지는, ROP 가 이기종 로봇 상태 모델로 받아야 할 최소 항목으로 쓸 수 있다. [의견][^ref-1505][^ref-1118] 다만 ROP 계층이 인증에서 말하는 관제장치에 해당하는지, 이 요구를 충족하는지는 판단하지 않는다. 이 문제는 열린 질문 oq-187 로 남긴다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1120]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area50-s10.md)에 있다.

## 11. 열린 질문

실외이동로봇 인증 심사 항목 수의 충돌(oq-230)과 ISO 3691-4 차기판 단계의 충돌(oq-384)은 원문을 확인해 해결했다. 실외 별표 개정의 세부(oq-186)와 플랫폼 수준 사고 기록 항목(oq-252)은 부분 근거만 더하고 열어 둔다. [사실][^ref-1118][^ref-1505][^ref-789]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-10-11-area50-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) — seed → draft: 3~11절 첫 작성(표준·인증 개정 현황, 제조 공장·물류창고·실외·가정·기타 사례, 사고 기록·조사 방법, 책임 경계, 연결 17건, 열린 질문 7건). 2차 수정: 7절 머리 문장을 f1·f3 의 구체 사실로 교체, 프런트매터 sources 를 각주 정의와 일치 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 머리 문장을 f1·f3 의 구체 사실로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "4. 핵심 개념과 용어" 절(1,007자)을 옮겼다 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area50-s6.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 역할별 표준 적합성 경로의 브리프 밖 한계 문장을 f16 사실 문장으로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-09-30-area50-s11.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "11. 열린 질문" 절(978자)을 옮겼다 (실행 2026-09-30-15)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30 (원문 미열람)
[^ref-1115]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1117]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-10-11
[^ref-1118]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-10-11
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-30
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1121]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-10-11
[^ref-1122]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-10-11
[^ref-1124]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-09-30
[^ref-1125]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-09-30
[^ref-563]: Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv), From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02-28, https://arxiv.org/abs/2502.20693, 접근일 2026-09-30
[^ref-1496]: European Commission (Official Journal of the European Union), Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC, 2026-09-07, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015, 접근일 2026-10-11
[^ref-789]: ISO, ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 미확인, https://www.iso.org/standard/88615.html, 접근일 2026-10-11
[^ref-1501]: Suresh, V., Konda, S., Haney, J. M. 외 (American Journal of Industrial Medicine 69(5):345–357, 권호·쪽은 Crossref 기준), Robot-Related Workers' Compensation Claims in Ohio, 2001–2020, 2026-03-03(온라인 선공개), https://stacks.cdc.gov/view/cdc/258698, 접근일 2026-10-11
[^ref-1502]: 안전보건공단, 산업용 로봇 팔과 지그 사이에 끼임 (재해사례), 미확인, https://oshri.kosha.or.kr/kosha/data/machine.do?articleNo=411924&attachNo=233368&mode=download, 접근일 2026-10-11
[^ref-1503]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR), An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본), 2022-07, https://doi.org/10.13180/icres.2022.18-19.07.019, 접근일 2026-10-11
[^ref-1504]: 관계부처 합동 (금융위원회 누리집 게재 보도참고자료), 규제의 벽은 허물고 AI의 길은 넓힌다 — 신산업 규제합리화 1호 로드맵(AI 분야) 발표, 2025-11-27, https://www.fsc.go.kr/no010101/85753, 접근일 2026-10-11
[^ref-1505]: 산업통상부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정), 2025-11-24, https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view, 접근일 2026-10-11
[^ref-1506]: Leveson, N. (MIT OpenCourseWare, 16.863J System Safety), System Safety: CAST Analysis (강의 자료), 2016, https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/7dc4344ef259e4bde4acc1bb2d578a95_MIT16_863JS16_LecNotes3-2.pdf, 접근일 2026-10-11
````

### docs/categories/safety/safety-standards-certification-and-incident-investigation.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사"
type: area
category: "M. 안전"
area_no: 50
related_areas: [4, 22, 37, 38, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [ISO 10218, 실외이동로봇 운행안전인증, 윤리적 블랙박스, 사고 조사, 잠금·표지]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1084, ref-991, ref-1115, ref-1116, ref-1117, ref-980, ref-992, ref-1118, ref-945, ref-1120, ref-1121, ref-1122, ref-1124, ref-1125, ref-563]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [M. 안전](index.md) › 50. 안전 표준·인증·사고 조사

# 50. 안전 표준·인증·사고 조사

!!! info "소속 대분류"
    [M. 안전](index.md) — 핵심 질문:
    여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]

## 3. 왜 중요한가

따를 안전 표준과 인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년에 개정 중이어서, 여러 제조사 로봇을 함께 운영하는 ROP는 적용 기준을 한 번 정하고 끝낼 수 없는 것으로 보인다. [추정][^ref-1115][^ref-1117][^ref-980][^ref-945]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 왜 중요한가](../../topics/2026/2026-09-30-area50-s3.md)에 있다.

## 4. 핵심 개념과 용어

표준 개정과 사고 자료를 읽으려면 다음 용어가 필요하다. 표준 관련 용어의 설명은 ISO·ANSI 원문이 아니라 전문지·컨설팅사 해설에 기댄다. [사실][^ref-1115][^ref-1116]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 사례는 제조 공장·물류창고의 사고, 실외 로봇의 법정 인증, 가정의 모의 사고 조사, 건설 현장의 위험성평가다. 병원·상업 시설의 안전 인증·사고 조사 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 제조 공장

**사례:** 식품 제조 공장에서 멈춘 적재 로봇을 점검하던 노동자의 끼임 사망 사고(2026-09)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 2026-09-21 제품 적재용 로봇이 멈춰 노동자가 점검에 나섰다. [사실][^ref-1125] |
| 작업 대상 | 멈춘 제품 적재용 로봇과 그 로봇을 점검하던 노동자 [사실][^ref-1125] |
| 수행 자원 | 점검 노동자와 적재 로봇 [사실][^ref-1125] |
| 제약 | 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다. [사실][^ref-1125] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 노동자가 끼여 2026-09-25 숨졌다. 노동부 통영지청은 산업안전보건법·중대재해처벌법 위반을 조사하고 있다. [사실][^ref-1125] |

재가동 경위는 조사 쟁점이다. 경찰은 다른 노동자가 작업 중임을 확인하지 않고 재가동했는지, 기계 오작동인지를 수사 중이며, 원인은 확정되지 않았다(원인 미확정, 2026-09-29 보도 기준). [사실][^ref-1125] 이 사례에서 이 영역은 예외·성과 항목, 곧 사고 뒤 누가 무엇을 조사하는가에 관여한다.

**현장 유형:** 물류창고

**사례:** 농산물유통센터에서 상자를 선별해 팔레트로 옮기는 로봇의 점검 중 압착 사망 사고(2023-11)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하는 작업이었다. [사실][^ref-1124] |
| 작업 대상 | 파프리카 상자를 선별해 팔레트로 옮기는 산업용 로봇 [사실][^ref-1124] |
| 수행 자원 | 산업용 로봇과 점검 작업자 [사실][^ref-1124] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 2023-11-07 작업자가 로봇에 압착되어 숨졌다. 경찰은 로봇이 사람을 상자로 인식한 것으로 보고 안전관리 책임자의 과실 여부를 수사했다(2023-11-08 보도 기준). [사실][^ref-1124] |

두 사고 모두 정상 운전이 아니라 점검과 작동 확인 같은 비정상 작업 중에 일어났다. [사실][^ref-1124][^ref-1125]

**현장 유형:** 실외

**사례:** 연계 대상: 보도를 운행하는 실외이동로봇의 운행안전인증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 연계 대상: 인증 신청이 심사를 발생시키며, 한국로봇산업진흥원은 처리기간을 신청일로부터 30일 이내로 안내한다(확인일 2026-09-30). [사실][^ref-980] |
| 작업 대상 | 최대 질량 500kg·최고 속도 15km/h 이하 실외이동로봇 [사실][^ref-980] |
| 수행 자원 | 지능형로봇법 제40조의2 에 근거한 인증을 한국로봇산업진흥원이 맡는다. [사실][^ref-980] |
| 제약 | 진흥원 페이지는 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 심사항목을 둔다. [사실][^ref-980] 행정예고 보도와 정책브리핑은 16가지 기준·시험항목을 전한다. [사실][^ref-992][^ref-991] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

연계 대상: 인증 절차와 기준은 산업통상자원부 고시 제2023-211호(2023-11-17)로 정해졌고, 이 고시는 지능형로봇법(법률 제19412호) 개정 시행에 따라 제정되었으며 별표에서 로봇 모델 구분, 최고속도, 최대폭, 최대질량, 운행안전성 기준을 다룬다. [사실][^ref-1118]

2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인인 기준 예시는 질량별 속도 제한(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 80cm 이하(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정 주행, 비상정지, 장애물 회피, 알림음 55~73dB, 등화장치 표면 온도 60도 이하, 방수 IPX4 이상이다. 현행 기준으로 확인된 값이 아니다. [사실][^ref-992] 심사항목 수가 8개와 16가지로 달라 어느 쪽도 고르지 않고 함께 두며, 11절의 oq-186·oq-230 으로 남긴다. ROP는 인증 자체가 아니라 인증이 허용한 운행 조건을 작업·경로 제약으로 받는 쪽에서 이 사례에 관여한다(9절). [추정][^ref-980]

**현장 유형:** 가정

**사례:** 실제 사고가 아닌 역할극 모의 사고(노인 지원 주거 공동체 시나리오) — 넘어진 거주자 곁 보조 로봇의 알림 실패 조사

| 항목 | 내용 |
|---|---|
| 시작 조건 | 지원 주거 아파트에서 거주자가 넘어졌다(모의). [사실][^ref-1121] |
| 작업 대상 | 넘어진 거주자와 그 사실을 직원에게 알리는 정보(모의) [사실][^ref-1121] |
| 수행 자원 | 보조 로봇과 직원, 그리고 사고를 조사하는 조사자(모의) [사실][^ref-1121] |
| 제약 | 로봇이 인터넷에 연결되지 않은 상태였다(모의 조건). [사실][^ref-1121] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 보조 로봇이 오작동해 직원에게 알리지 못했다(모의). 조사는 목격자 증언, 윤리적 블랙박스 기록, 환경·로봇 전문가 분석, 기술·조직 권고로 구성되었다. [사실][^ref-1121] |

Webb 외(2021)는 이 모의 사고를 역할극 증언 면담으로 조사해 조사 방법을 시험했다. 실제 사고 자료가 아니므로 방법의 시험 사례로만 읽는다. [사실][^ref-1121]

**현장 유형:** 기타

**사례:** 건설 현장에 이동로봇을 배치하기 전의 위험성평가

| 항목 | 내용 |
|---|---|
| 시작 조건 | 건설 현장에 이동로봇을 배치하기 전 위험성평가 틀이 필요한 상황이다. [사실][^ref-563] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 해당 없음 |
| 제약 | ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 다양한 배치 상황에 적용할 수 있는 표준이 없고 이동 플랫폼의 위험성평가 문헌도 제한적이었다. [사실][^ref-563] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

Belzile 외(2025)는 이 공백을 메우려고 건설 현장 이동로봇 배치용 위험성평가 틀을 제안했다(프리프린트). [사실][^ref-563]

## 6. 대표 접근법과 기술

표준 적합성은 제조사·통합자·사용자가 역할을 나눠 맞추는 구조이고, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계로 제안되어 있다. [추정][^ref-1115][^ref-1084][^ref-1121]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area50-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

6절의 역할별 경로는 아래 표준·인증으로 구체화된다. ISO 10218-1/-2 는 2025-02 에 개정판이 발행되었다. [사실][^ref-1115] ISO 13482 개정판은 2026-09-15 기준 FDIS 투표 단계(50.20)로 발행 전이다. [사실][^ref-1117] 표준 서술은 ISO·ANSI 원문이 아니라 전문지·컨설팅사·국가 표준기관의 해설과 프로젝트 정보에 기댄다.

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md)에 있다.

## 8. 대표 연구와 자료

사고 기록·조사 연구는 사회적 로봇을 중심으로 방법을 제안하는 단계이고, 산업 현장 자료는 보고 서술의 구조화 부족을 드러낸다. [추정][^ref-1120][^ref-1122]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 대표 연구와 자료](../../topics/2026/2026-09-30-area50-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 범위는 인증 상태·적용 표준과 판·허용 운행 조건을 등록해 배정·경로 제약에 반영하고, 사고 조사에 쓸 플릿 수준 실행 기록을 보존하는 일로 보인다. [추정][^ref-980][^ref-1116][^ref-1120][^ref-1122]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇·적용마다 인증 상태와 적용 표준·판을 등록 정보로 관리하고, 정지·재가동·정비 모드 전환 명령과 로봇 상태 보고를 사고 조사에 쓸 수 있게 보존한다. [추정][^ref-1116][^ref-1120] | 연계 대상: 로봇 본체의 표준 적합성과 제품 인증은 제조사와 인증기관이, 로봇 셀·이동로봇 적용의 위험성평가와 사용 정보는 통합자가 맡는다. [추정][^ref-1115][^ref-1084] |
| 업종별 조건 | 인증이 허용한 운행 조건(질량·속도·구역)을 배정·경로 제약에 반영하고 표준 판 개정을 추적한다. [추정][^ref-980][^ref-1116] | 연계 대상: 실외 운행 인증과 보험은 운영자와 한국로봇산업진흥원의 일이다. [추정][^ref-980][^ref-991] |
| 시설·설비 제어 | 사고 조사에 필요한 실행 기록을 외부 주체와 주고받는 인터페이스를 둔다. [추정][^ref-1125] | 연계 대상: 교육·작업 절차·잠금·표지는 사용자 사업장이, 법정 사고 조사는 고용노동부·경찰이 맡는다. [추정][^ref-1084][^ref-1125] |

실외이동로봇 운행안전인증처럼 인증 자체는 운영자·진흥원의 일이고, ROP는 그 결과를 받아 작업·경로 제약으로 반영하는 쪽이다. [추정][^ref-980] 이 경계는 제품 전략에 따라 옮겨질 수 있으며 기준은 [범위 경계](../../about/scope-boundary.md)에 있다. 이종 제조사를 연결하는 ROP는 각 주체의 인증·평가 결과와 조사에 필요한 실행 기록을 주고받는 인터페이스를 맡는 것으로 보인다. [추정][^ref-1115][^ref-1084][^ref-1125]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1120]

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area50-s10.md)에 있다.

## 11. 열린 질문

표준 원문을 열지 못한 부분과 출처가 충돌한 부분은 질문으로 남긴다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-09-30-area50-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [50. 안전 표준·인증·사고 조사](safety-standards-certification-and-incident-investigation.md) — seed → draft: 3~11절 첫 작성(표준·인증 개정 현황, 제조 공장·물류창고·실외·가정·기타 사례, 사고 기록·조사 방법, 책임 경계, 연결 17건, 열린 질문 7건). 2차 수정: 7절 머리 문장을 f1·f3 의 구체 사실로 교체, 프런트매터 sources 를 각주 정의와 일치 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area50-s7.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 1절·3절 머리 문장을 f1·f3 의 구체 사실로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area50-s4.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "4. 핵심 개념과 용어" 절(1,007자)을 옮겼다 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area50-s6.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 역할별 표준 적합성 경로의 브리프 밖 한계 문장을 f16 사실 문장으로 교체 (실행 2026-09-30-15)
- 2026-09-30 · 생성 · [50. 안전 표준·인증·사고 조사 — 열린 질문](../../topics/2026/2026-09-30-area50-s11.md) — 자동 분리: 50. 안전 표준·인증·사고 조사 의 "11. 열린 질문" 절(978자)을 옮겼다 (실행 2026-09-30-15)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-991]: 산업통상자원부·경찰청 (대한민국 정책브리핑), ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인), 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30 (원문 미열람)
[^ref-1115]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1117]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: ZDNet Korea, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1118]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-09-30
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-30
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1121]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-09-30
[^ref-1122]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-09-30
[^ref-1124]: 경향신문, ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망, 2023-11-08, https://www.khan.co.kr/article/202311081103001, 접근일 2026-09-30
[^ref-1125]: 경남도민일보, 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다, 2026-09-29, https://www.idomin.com/news/articleView.html?idxno=2015923, 접근일 2026-09-30
[^ref-563]: Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv), From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, 2025-02-28, https://arxiv.org/abs/2502.20693, 접근일 2026-09-30
```

### runs/2026-10-11-06/pages/topics/2026/2026-10-11-area50-s7.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1096, ref-1115, ref-1116, ref-1117, ref-1118, ref-1120, ref-1255, ref-1496, ref-1497, ref-1498, ref-1499, ref-1500, ref-1503, ref-1505, ref-211, ref-555, ref-789, ref-831]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#7
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스

# 50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- EN ISO 10218-1/-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015(2026-09-07 관보 게재)로 기계류 지침 2006/42/EC 의 조화 표준 목록에 실렸다. 실외이동로봇 운행안전인증 기준은 2025-11-24 개정 고시로 8개 항목이 되었다. [사실][^ref-1496][^ref-1505]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

EN ISO 10218-1/-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015(2026-09-07 관보 게재)로 기계류 지침 2006/42/EC 의 조화 표준 목록에 실렸다. 실외이동로봇 운행안전인증 기준은 2025-11-24 개정 고시로 8개 항목이 되었다. [사실][^ref-1496][^ref-1505] 이전 판(2026-09-30)의 표는 [50. 안전 표준·인증·사고 조사 — 관련 표준·프레임워크·오픈소스](2026-09-30-area50-s7.md)에 있다. 이번 판의 행은 이전 판의 'EN ISO 10218 EU 조화 게재' 행과 '실외이동로봇 운행안전인증' 행을 대체하고, 새 행을 더한다.

ISO 10218-1/-2 는 2025-02 에 개정판이 발행되었다. [사실][^ref-1115] ISO 13482 개정판은 2026-09-15 기준 FDIS 투표 단계(50.20)로 아직 발행 전이다. [사실][^ref-1117] 이전 판은 2025 판의 요구 변경 설명을 컨설팅사 해설만으로 사실 표기했다. 이번 판은 관보 원문에 그 내용이 없어 추정으로 낮췄다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| EN ISO 10218-1:2025·-2:2025 의 EU 조화 게재 | 표준 | 위원회 시행결정 (EU) 2026/2015(2026-09-04 채택, 2026-09-07 관보 L 시리즈 게재)의 부속서는 시행결정 2023/1586 부속서 I 에 EN ISO 10218-1:2025(223a)와 -2:2025(224a)의 참조를 추가했다. [사실][^ref-1496] 이 목록은 기계류 지침 2006/42/EC 에 대해 적합성 추정을 주는 조화 표준 목록이다. 같은 결정 제2조에 따라 2027-01-20 부로 폐지되는데, 지침이 같은 날 기계 규정 (EU) 2023/1230 으로 폐지되기 때문이다. [사실][^ref-1496] 따라서 이 게재는 규정 (EU) 2023/1230 에 따른 조화 게재가 아니다. [사실][^ref-1496] 규정 쪽 게재 시점은 미확인이다(11절). | EU 관보 원문(열람) |
| EN ISO 10218:2025 요구 변경 해설 | 표준 | 컨설팅사 IBF Solutions 는 2025 판이 PL d·범주 3 을 일률로 요구하지 않고 표의 기본 성능 수준이나 위험성평가 근거 가운데 고를 수 있게 했으며, 운전을 멈추는 정상 정지 기능을 새로 두었다고 해설한다. 이 해설은 벤더 주장이다. [추정][^ref-1116] (EU) 2026/2015 의 본문과 부속서에는 참조 목록만 있고 ISO 10218 의 조항 내용은 없다. [추정][^ref-1496] | 컨설팅사 해설(2026-09-30 열람), 표준 원문 미열람 |
| ANSI/A3 R15.08-3-2026 (Part 3: Use of IMR Applications) | 표준 | 산업용 이동로봇(IMR) 적용의 사용을 다루는 3부다. A3 판매 페이지에 2026-04-23 발행으로 표시된다(2026-10-09 열람 기록 기준, 이번 재열람 실패). [추정][^ref-1255] 사용자 의무의 세부는 열린 질문 oq-265 로 남긴다. | 판매 페이지(이번 원문 미열람) |
| ISO/DIS 3691-4 (제3판) | 표준 | ISO 위원회 페이지에 개발 중(단계 40.60, 투표 종료 2026-09-10)으로 표시되며, ISO 3691-4:2023 을 대체할 예정이다. 아직 발행된 개정판이 아니다(확인일 2026-10-11). [사실][^ref-789] | ISO 위원회 페이지(열람), 개정안 본문 미열람 |
| KS B ISO 10218-1·-2 | 표준 | KS B ISO 10218-1 의 대응 국제표준은 ISO 10218-1:2011(IDT, 일치)이고, 최종개정확인일은 2021-11-26 이다. [사실][^ref-1497] KS B ISO 10218-2 의 최종 확인일은 2022-10-12(ISO 10218-2:2011 IDT, 고시 제2022-0433호)다. [사실][^ref-211] 2026-10-11 목록에서 ISO 10218:2025 에 부합하는 KS 는 확인되지 않았다. 다만 없다는 것을 증명한 것은 아니다. [사실][^ref-1497][^ref-211] | 국가표준 목록(열람) |
| 실외이동로봇 운행안전인증 고시 | 평가 프로그램 | 절차와 기준을 정한 산업통상자원부 고시 제2023-211호(2023-11-17 발령)를 산업통상부 고시 제2025-21호가 2025-11-24 개정했고, 발령일부터 시행한다. [사실][^ref-1505] 인증 기준(별표 3)은 구판 16개 항목에서 현행 8개 항목으로 바뀌었다(5절). [사실][^ref-1118][^ref-1505] | 고시 첨부 원문(열람) |
| EU 기계 규정 (EU) 2023/1230 부속서 III 1.2.1 | 프레임워크 | 제어 시스템은 두 가지 추적 기록이 업로드 뒤 5년간 켜져 있도록 설계·제작해야 한다. 개입과 관련해 생성된 데이터, 그리고 출시·사용 개시 뒤 업로드한 안전 소프트웨어 판의 기록이다. 목적은 관할 국가기관이 이유를 들어 요청할 때 적합성을 입증하는 것으로 한정된다. [사실][^ref-555] 행동·논리가 전부 또는 일부 스스로 진화하는 기계의 제어 시스템은, 소프트웨어 기반 안전 시스템의 안전 관련 의사결정 데이터를 기록해 수집 뒤 1년간 보존해야 한다. [사실][^ref-555] 이 페이지는 이를 일반 작업 로그나 플릿 전체 데이터의 보관 의무로 읽지 않는다. 제품별 적용 여부는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)에서 다룬다(2026-07-27 통합본 기준). | EUR-Lex 통합본(리서치 열람) |
| UL 3100 Automated Mobile Platforms (AMPs) | 표준 | 공식 목록은 제1판의 최초 발행일을 2021-05-26, 최근 개정일과 ANSI 승인일을 2026-06-10 으로 표시한다. [사실][^ref-1498] 공개된 적용 범위 1.4 는 산업용 로봇 자체의 요구사항은 포함하지 않는다고 적는다(UL 1740·CSA Z434 가 다룸). 그 표준에 맞는 로봇 매니퓰레이터는 통합 시스템의 탑재물로 쓸 수 있다. [사실][^ref-1498] | UL 표준 목록(열람), 개정 조항 미열람 |
| UL 3300 (Simbe Tally 인증 발표) | 표준 | UL Solutions 는 2026-03-11 Simbe 의 매장용 자율이동로봇 Tally 가 UL 3300(SCIEE 로봇 표준) 인증을 받았다고 발표했다. 로봇과 충전 도크가 화재·감전 위험과 안전한 자율 이동 시험을 거쳤다는 내용이다(벤더 주장: 인증기관 UL Solutions 의 상업 보도자료, 인증서·시험보고서 미공개). [추정][^ref-1499] 이 페이지는 이 발표를 이종 플릿 전체의 안전 입증으로 읽지 않는다. | 인증기관 보도자료 |
| 산업용 로봇 자율안전확인 | 평가 프로그램 | 안전보건공단 산업안전보건인증원은 자율안전확인 대상인 산업용 로봇을 이렇게 정의한다. 직교좌표로봇을 포함해 3축 이상의 매니퓰레이터(액추에이터·교시 펜던트·제어기·통신 인터페이스 포함)를 갖추고, 전용 제어기로 프로그램·자동제어가 가능한 고정식 로봇이다. [사실][^ref-1500] | 인증원 안내(열람) |
| rosbag2 (0.35.0 태그) | 오픈소스 | `--repeat-transient-local` 옵션은 지정한 토픽의 최근 N개(기본 1개) 메시지를 보관해 두었다가, 분할로 새 파일이 시작되거나 스냅샷을 쓸 때 맨 앞에 다시 넣는다. [사실][^ref-831] 스냅샷 모드는 메시지를 바로 디스크에 쓰지 않는다. `--max-cache-size`(바이트)와 선택적 `--max-cache-duration`(초)으로 제한한 메모리 순환 버퍼에 두었다가, 요청이 오면(`~/snapshot` 서비스) 디스크에 저장한다. [사실][^ref-831] 유실 메시지 통계는 증분 방식이어서 유실이 0인 토픽은 이벤트에 들어가지 않고, 내부 카운터는 이벤트를 발행할 때마다 0으로 돌아간다. [사실][^ref-831] | GitHub 원문 README(열람, 확인일 2026-10-11) |
| MCAP (커밋 f7069e6 명세) | 오픈소스 | Message 레코드의 publish_time 은 발행 시각이며, 알 수 없으면 log_time 으로 설정해야 한다(must). 그래서 두 값이 같을 때 실제 발행 시각인지 대체값인지를 포맷만으로는 구분할 수 없다. [사실][^ref-1096] Chunk 의 uncompressed_crc 와 여러 레코드의 crc 값이 0이면 CRC 검증을 하지 않아야 한다(should not)는 뜻이다. CRC 는 오류 검출용이며 서명이나 증거 인계를 보장하지 않는다. [사실][^ref-1096] | GitHub 원문 명세(열람, 확인일 2026-10-11) |

rosbag2 와 MCAP 의 기록 기능 자체는 [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)과 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)에서 다룬다. 이 영역에서는 사고 증거를 보존하는 관점으로만 본다. 위 두 행은 rosbag2 0.35.0 태그(CHANGELOG 2026-09-12)와 MCAP 커밋 f7069e6 판을 기준으로 하며, 확인일은 2026-10-11 이다. 전체 목록은 [표준·프레임워크](../../standards/index.md)에 있다.

구축자 의견: 표준 레지스트리는 다음 판들을 서로 다른 속성으로 나눠 두어야 한다. 발행판(ISO 3691-4:2023)과 개발 중 프로젝트(ISO/DIS 3691-4 제3판), 국내 부합판(KS B ISO 10218-1·-2, ISO 10218:2011 IDT)과 국제 최신판(ISO 10218:2025), 그리고 EU 조화 게재(지침 2006/42/EC 기반, 2027-01-20 폐지 예정 목록)다. 배포 설정에는 현장에서 승인한 판을 고정해야 한다. [의견][^ref-789][^ref-1497][^ref-211][^ref-1496]

구축자 의견: EU 기계 규정 부속서 III 1.2.1 의 5년·1년 기록 의무는 안전 소프트웨어의 개입·판 이력과, 스스로 진화하는 제어의 안전 결정 데이터에만 걸린다. 따라서 ROP 는 인증 증거용 이력과 일반 작업 로그의 보존 정책을 나눠 정해야 한다. 플릿 전체 데이터를 일률적으로 5년이나 1년 보관해야 한다고 해석하지 않는 것이 맞다. [의견][^ref-555]

구축자 의견: 윤리적 블랙박스 초안을 공통 기록 스키마로 쓰려면 먼저 날짜·시각·체크섬 표기 충돌을 풀어야 한다. ROP 쪽에서는 제조사 원본 결정 코드, 공통 사건 유형, 코드표 판, 시각 기준, 사고 시 보존 잠금을 따로 정의해야 한다. 기록기 쪽에서는 다음을 증거 메타데이터로 함께 남겨야 한다. 사고 트리거 스냅샷, 정적 토픽 재삽입 깊이, 유실 이벤트 수신 여부, MCAP publish_time 대체 여부, 원본 해시와 추출 이력이다. [의견][^ref-1503][^ref-1120][^ref-831][^ref-1096]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-11
[^ref-1115]: The Robot Report, ISO 10218 industrial robot safety standard receives major overhaul, 2025-02, https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/, 접근일 2026-09-30
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1117]: Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보, ISO/FDIS 13482 Robotics — Safety requirements for service robots, 미확인, https://iss.rs/en/project/show/iso:proj:83498, 접근일 2026-09-30
[^ref-1118]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-10-11
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1255]: A3(Association for Advancing Automation), ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications, 2026-04-23, https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download, 접근일 2026-10-11 (원문 미열람)
[^ref-1496]: European Commission (Official Journal of the European Union), Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC, 2026-09-07, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015, 접근일 2026-10-11
[^ref-1497]: 국가기술표준원 (국가표준인증 통합정보시스템), KS B ISO 10218-1 로봇 및 로봇장치 ─ 산업용 로봇의 안전에 관한 요구사항 ─ 제1부: 로봇, 2021-11-26, https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503, 접근일 2026-10-11
[^ref-1498]: UL Standards & Engagement, UL 3100 Automated Mobile Platforms (AMPs), 2026-06-10, https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=39063, 접근일 2026-10-11
[^ref-1499]: UL Solutions, UL Solutions Grants Its First Global Certification for a Public-Facing Robot to Simbe's Tally Autonomous Mobile Robot, 2026-03-11, https://www.ul.com/news/ul-solutions-grants-its-first-global-certification-public-facing-robot-simbes-tally-autonomous, 접근일 2026-10-11
[^ref-1500]: 안전보건공단 산업안전보건인증원, 자율안전확인 대상품 (자율안전확인신고 대상 및 적용범위), 미확인, https://miis.kosha.or.kr/oshci/busi/viewMiisJayulMerchandiseInfo.do, 접근일 2026-10-11
[^ref-1503]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR), An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본), 2022-07, https://doi.org/10.13180/icres.2022.18-19.07.019, 접근일 2026-10-11
[^ref-1505]: 산업통상부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정), 2025-11-24, https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view, 접근일 2026-10-11
[^ref-211]: 국가표준인증통합정보시스템(KSSN), KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합, 2022-10-12, https://www.kssn.net/search/stddetail.do?itemNo=K001010083660, 접근일 2026-10-11
[^ref-555]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-10-11
[^ref-789]: ISO, ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 미확인, https://www.iso.org/standard/88615.html, 접근일 2026-10-11
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-06 | 50. 안전 표준·인증·사고 조사 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-11-06/pages/topics/2026/2026-10-11-area50-s11.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 열린 질문"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1096, ref-1118, ref-1497, ref-1503, ref-1504, ref-1505, ref-211, ref-555, ref-789, ref-831]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#11
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 열린 질문

# 50. 안전 표준·인증·사고 조사 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 실외이동로봇 인증 심사 항목 수의 충돌(oq-230)과 ISO 3691-4 차기판 단계의 충돌(oq-384)은 원문을 확인해 해결했다. 실외 별표 개정의 세부(oq-186)와 플랫폼 수준 사고 기록 항목(oq-252)은 부분 근거만 더하고 열어 둔다. [사실][^ref-1118][^ref-1505][^ref-789]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

실외이동로봇 인증 심사 항목 수의 충돌(oq-230)과 ISO 3691-4 차기판 단계의 충돌(oq-384)은 원문을 확인해 해결했다. 실외 별표 개정의 세부(oq-186)와 플랫폼 수준 사고 기록 항목(oq-252)은 부분 근거만 더하고 열어 둔다. [사실][^ref-1118][^ref-1505][^ref-789] 전체 목록은 [열린 질문](../../open-questions.md)에 있고, 이전 판의 질문 정리는 [50. 안전 표준·인증·사고 조사 — 열린 질문](2026-09-30-area50-s11.md)에 있다.

### 해결

- **oq-230** (상태: 해결 · 실행 2026-10-11-06) 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? — 답: 둘 다 항목 단위다. 16개는 구 고시 제2023-211호 별표 3, 8개는 현행 제2025-21호 별표 3 의 인증 기준 항목이다. 세부 목록과 항목 대응은 5절에 있다. [사실][^ref-1118][^ref-1505]
- **oq-384** (상태: 해결 · 실행 2026-10-11-06) 출처 충돌: ISO 3691-4 차기판 프로젝트의 현재 단계는 위키 기록(2026-09-26, ISO/CD 3691-4)과 외부 조사 메모(ISO/DIS 3691-4 제3판, 2026-09-10 단계 40.60) 가운데 어느 쪽인가? — 답: ISO 위원회 페이지 기준으로 ISO/DIS 3691-4 제3판, 단계 40.60(투표 종료 2026-09-10)이다. 아직 발행된 개정판이 아니다(확인일 2026-10-11, 7절). [사실][^ref-789]

### 부분 근거를 더하고 열어 둔 질문

- **oq-186** (상태: 열림) 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시와 흡수된 항목 — 정부는 2025-11 심사 평가항목을 16개에서 8개로 합쳤다. [사실][^ref-1504] 근거 고시는 2025-11-24 발령·시행된 제2025-21호다. [사실][^ref-1505] 경사로 안정성(5°)은 '동적 특성'에 흡수됐고, 알림음·등화장치는 새 별표에 없다. [사실][^ref-1118][^ref-1505] 빠진 항목이 다른 규정으로 옮겨졌는지가 아직 확인되지 않아 열어 둔다.
- **oq-251** (상태: 열림) 국내 KS B ISO 10218-1·-2 의 ISO 10218:2025 부합화 시점 — 2026-10-11 목록 기준으로 두 KS 는 여전히 ISO 10218-1·-2:2011 IDT 다. [사실][^ref-1497][^ref-211] 같은 부분 근거를 oq-123 에도 더한다.
- **oq-252** (상태: 열림) 플랫폼 수준의 사고·아차 사고 조사용 최소 기록 항목 — 이번에 세 가지 부분 근거를 더했다. EU 기계 규정 부속서 III 1.2.1 의 5년·1년 기록 의무(대상 한정), 윤리적 블랙박스 초안의 형식 충돌과 순환 덮어쓰기, rosbag2·MCAP 의 기록 규칙이다(6·7절). [사실][^ref-555][^ref-1503][^ref-831][^ref-1096] 여러 제조사 로봇을 지휘하는 플랫폼의 최소 기록 항목을 정한 표준은 여전히 확인하지 못했다.
- **oq-333** (부분 근거 추가) 현행 고시 본문과 별표 3 에는 관제장치의 운행 기록을 저장·보관하라는 문구가 없다. [사실][^ref-1505]
- **oq-187** (부분 근거 추가) 인증 정보는 로봇 모델과 관제장치 모델의 조합으로 보관된다(제10조②). [사실][^ref-1505] 이기종 오케스트레이션 계층이 인증상 관제장치에 해당하는지는 판단하지 않는다.
- 이번 조사로 답하지 못해 그대로 열린 질문: oq-170, oq-253, oq-254, oq-265.

### 새 질문 (id 는 등록할 때 부여한다)

- 윤리적 블랙박스 초안의 날짜·시각·체크섬 표기 충돌을 해소한 후속 판이 있는가, 서로 다른 제조사의 로봇 결정 코드를 공통 사건 유형으로 옮기는 공개 매핑이 있는가?
- rosbag2 스냅샷·repeat-transient-local·유실 통계를 쓴 사고 전후 기록을 현장 설정(스냅샷 트리거 지연, 전원 상실, 정적 토픽 depth, 유실 이벤트 누락)에서 시험해 보존 길이와 누락을 검증한 사례가 있는가?
- MCAP 의 publish_time 이 log_time 으로 대체된 경우와 원본 추출·해시·서명 이력을 사고 증거 묶음에 어떻게 표시하고 검증할 것인가?
- 출처 충돌: 실외이동로봇 운행안전인증 고시 제2023-211호의 시행일은 원 고시 첨부 부칙(2023-11-17)과 개정 고시 첨부 본문에 실린 구 부칙(2023-11-21) 가운데 어느 쪽인가?
- EN ISO 10218-1/-2:2025 참조는 기계 규정 (EU) 2023/1230 의 조화 표준으로 언제 게재되며, 지침 2006/42/EC 기반 목록(시행결정 2023/1586)이 2027-01-20 폐지된 뒤 적합성 추정은 어떻게 이어지는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-11
[^ref-1118]: 산업통상자원부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시, 2023-11-17, https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view, 접근일 2026-10-11
[^ref-1497]: 국가기술표준원 (국가표준인증 통합정보시스템), KS B ISO 10218-1 로봇 및 로봇장치 ─ 산업용 로봇의 안전에 관한 요구사항 ─ 제1부: 로봇, 2021-11-26, https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503, 접근일 2026-10-11
[^ref-1503]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR), An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본), 2022-07, https://doi.org/10.13180/icres.2022.18-19.07.019, 접근일 2026-10-11
[^ref-1504]: 관계부처 합동 (금융위원회 누리집 게재 보도참고자료), 규제의 벽은 허물고 AI의 길은 넓힌다 — 신산업 규제합리화 1호 로드맵(AI 분야) 발표, 2025-11-27, https://www.fsc.go.kr/no010101/85753, 접근일 2026-10-11
[^ref-1505]: 산업통상부, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정), 2025-11-24, https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view, 접근일 2026-10-11
[^ref-211]: 국가표준인증통합정보시스템(KSSN), KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합, 2022-10-12, https://www.kssn.net/search/stddetail.do?itemNo=K001010083660, 접근일 2026-10-11
[^ref-555]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-10-11
[^ref-789]: ISO, ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 미확인, https://www.iso.org/standard/88615.html, 접근일 2026-10-11
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-06 | 50. 안전 표준·인증·사고 조사 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-11-06/pages/topics/2026/2026-10-11-area50-s6.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1120, ref-1502, ref-1503, ref-1506]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#6
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술

# 50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사고 기록에 관한 공개 규약 초안은 아직 필드 형식과 보존 기간을 정하지 않았다. 사고 원인을 제어 구조와 조직 정책까지 넓혀 묻는 분석 방법은 이번 조사에서 강의 자료 수준으로만 확인했다. [추정][^ref-1503][^ref-1506]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사고 기록에 관한 공개 규약 초안은 아직 필드 형식과 보존 기간을 정하지 않았다. 사고 원인을 제어 구조와 조직 정책까지 넓혀 묻는 분석 방법은 이번 조사에서 강의 자료 수준으로만 확인했다. [추정][^ref-1503][^ref-1506] 이전 판(2026-09-30)의 접근법 정리는 [50. 안전 표준·인증·사고 조사 — 대표 접근법과 기술](2026-09-30-area50-s6.md)에 있다. 이번 판의 두 소절은 이전 판 '사고 기록 장치' 소절에 남아 있던 '기록할 데이터 형식과 보존 기간 미확인'을 보강하고, 조직·제어 분석 방법을 더한다.

### 사고 기록 장치 — 윤리적 블랙박스 초안의 형식

[윤리적 블랙박스](../../glossary/ethical-black-box.md)(Ethical Black Box, EBB) 공개 표준 초안은 같은 연구의 두 판으로 나와 있다. arXiv 판(2022-05-13)과, 부록에 RFC Draft 0.1 을 실은 ICRES 2022 학회 게재본이다. 아래 필드 내용은 게재본으로 확인했다. [사실][^ref-1120][^ref-1503]

- 날짜 필드 ebbD 의 길이가 표에서는 10자, 기록 주석에서는 12 ASCII 문자로 서로 다르다. 시각 필드도 표와 주석이 다르게 적혀 있다. [사실][^ref-1503]
- 체크섬 표기도 서로 맞지 않는다. 표 2 는 4문자, 표 3 은 8자리 16진수이고, 주석은 '64비트 비암호학적 해시(추후 결정)'로 적는다. [사실][^ref-1503]
- 로봇 결정 코드의 숫자값 정의는 표준 범위 밖으로 두고 로봇 제조사나 운영자에게 맡긴다. 그래서 제조사마다 다른 결정 코드의 의미를 통일하는 규약이 아니다. [사실][^ref-1503]
- 로봇 데이터(RD) 기록은 저장 한도에 이르면 가장 오래된 RD 기록부터 덮어쓰는 순환 구조다. 초안 부록에는 고정 보존 기간 조항이 없다. [사실][^ref-1503]

이 값들은 초안 안에서 서로 어긋나는 표기다. 그래서 특정 필드 길이나 형식을 규범 값으로 쓸 수 없고, 체크섬도 변조를 막는다는 근거가 되지 않는 것으로 보인다. [추정][^ref-1503]

### 조직·제어 구조까지 보는 사고 분석 — CAST

Leveson 의 MIT OpenCourseWare 강의 자료 'CAST 분석'(16.863J System Safety, 2016년 봄 학기)은 화학 공장의 SO2 탱크 넘침 사례를 다룬다. 강의 자료는 다음을 조사 질문으로 던진다. 안전 핵심 장비가 왜 오랫동안 작동하지 않았는가, 안전 장비가 작동하지 않는 상태로 공장을 운전하는 정책이 있었고 그때 위험성평가를 했는가, 점검·정비 정책은 무엇이었는가. [사실][^ref-1506] 같은 강의는 운전원 수준의 분석 항목으로 맥락·시스템 요인과 정신 모형의 결함을 두고, 사후 판단 편향(hindsight bias)을 경계한다. [사실][^ref-1506] 2016 은 사고 연도가 아니라 강의 학기다. 예시도 로봇이 아닌 화학 공장 사고이며, 로봇 사고에 CAST 를 적용한 실증은 이번 조사에서 확인하지 않았다.

구축자 의견: CAST 의 조사 질문을 플릿 사고에 옮기려면 사건 시간선을 정리한 뒤 다음을 따로 조사하는 절차가 필요하다. 제조사·통합자·현장 운영자·관제자 각각의 제어 책임, 사고 당시 관측할 수 있었던 정보, 방호장치 우회(muting)와 정비·승인 정책이다. '교육 부족' 같은 결론을 증거 없이 먼저 정하지 않아야 한다. 5절의 용접 팁 교체 사례처럼 공식 조사가 방호장치 우회와 정지 절차 누락을 원인으로 든 경우가 이런 질문의 출발점이 될 수 있다. [의견][^ref-1506][^ref-1502]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1502]: 안전보건공단, 산업용 로봇 팔과 지그 사이에 끼임 (재해사례), 미확인, https://oshri.kosha.or.kr/kosha/data/machine.do?articleNo=411924&attachNo=233368&mode=download, 접근일 2026-10-11
[^ref-1503]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR), An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본), 2022-07, https://doi.org/10.13180/icres.2022.18-19.07.019, 접근일 2026-10-11
[^ref-1506]: Leveson, N. (MIT OpenCourseWare, 16.863J System Safety), System Safety: CAST Analysis (강의 자료), 2016, https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/7dc4344ef259e4bde4acc1bb2d578a95_MIT16_863JS16_LecNotes3-2.pdf, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-06 | 50. 안전 표준·인증·사고 조사 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-11-06/pages/topics/2026/2026-10-11-area50-s8.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 대표 연구와 자료"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1121, ref-1122, ref-1501]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#8
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 대표 연구와 자료

# 50. 안전 표준·인증·사고 조사 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 판은 미국 연방 OSHA 중상 보고 분석(2015-01-01~2022-04-30)과 Ohio 산재보상 청구 분석(2001~2020)을 다룬다. 두 자료는 관할·기간·집계 단위가 다르다. [사실][^ref-1122][^ref-1501]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 판은 미국 연방 OSHA 중상 보고 분석(2015-01-01~2022-04-30)과 Ohio 산재보상 청구 분석(2001~2020)을 다룬다. 두 자료는 관할·기간·집계 단위가 다르다. [사실][^ref-1122][^ref-1501] 이전 판(2026-09-30)의 자료 목록은 [50. 안전 표준·인증·사고 조사 — 대표 연구와 자료](2026-09-30-area50-s8.md)에 있다. 이번 판의 Sanders 외·Webb 외 항목은 이전 판의 같은 항목을 보강한다.

- Sanders, N. E., Sener, E., & Chen, K. B., Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports(Applied Ergonomics, 2024) — 분석한 중상 보고(SIR)는 2015-01-01부터 2022-04-30까지의 자료다. 2024 는 발표 연도이지 집계가 끝난 연도가 아니다. [사실][^ref-1122] SIR 에는 연방 OSHA 관할 사업장의 보고만 들어 있고, 자체 주 계획을 운영하는 22개 주의 사업장은 빠진다. [사실][^ref-1122] 분석한 사고 서술의 단어 수 중앙값은 36 단어였다. 이는 선별된 77건 보고의 서술 길이를 보여 주는 지표일 뿐, 원인을 얼마나 정확히 적었는지나 발생률을 뜻하지 않는다. [사실][^ref-1122]
- Suresh, V., Konda, S., Haney, J. M. 외, Robot-Related Workers' Compensation Claims in Ohio, 2001–2020(American Journal of Industrial Medicine, 2026-03-03 온라인 선공개. 권호·쪽 69(5):345–357 은 Crossref 기준) — Ohio 산재보상국(OHBWC) 자료를 키워드로 검색해 2001~2020년 로봇 관련 산재보상 청구 1,076건을 찾았다. [사실][^ref-1501] 초록에 따르면 청구의 85% 는 의료비만 청구한 건(의료 처치만 받았거나 휴업 7일 이하)이었다. 75.7% 는 공유 작업공간에서 협동 적용 로봇 팔을 다루는 작업과 관련됐다. 모두 청구 건수 기준이므로 로봇에 노출된 인원당 발생률이 아니다. [사실][^ref-1501] 이번 확인은 서지와 초록까지다.
- Webb, H. 외, Role-Play as Responsible Robotics(Frontiers in Robotics and AI, 2021) — 2020년 11월 같은 연구자 한 명이 Zoom 으로 가상 목격자 증언(VWT) 역할극 면담을 22회 진행했다. 실제 사고가 아니라 삽화로 된 시나리오를 보여 주는 방식이었다. [사실][^ref-1121] 연구진은 정지 이미지를 썼기 때문에 시나리오의 동적인 부분을 제대로 전달하지 못했다고 한계를 밝혔다. 로봇이 거주자의 다리와 부딪혔을 수 있음을 보여 주는 움직임이 그 예다. [사실][^ref-1121]

구축자 의견: 사고 자료 레코드에는 출처별 관할(예: 연방 OSHA 관할만), 관측 기간, 집계 단위(보고 건수·부상 수·보상 청구), 중증도 정의, 노출 분모가 있는지를 필드로 두어야 한다. 그래야 OSHA SIR 과 Ohio 보상 청구처럼 모집단이 다른 자료를 합치거나 비교하지 않게 된다. [의견][^ref-1122][^ref-1501]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1121]: Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI), Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions, 2021-06-29, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full, 접근일 2026-10-11
[^ref-1122]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-10-11
[^ref-1501]: Suresh, V., Konda, S., Haney, J. M. 외 (American Journal of Industrial Medicine 69(5):345–357, 권호·쪽은 Crossref 기준), Robot-Related Workers' Compensation Claims in Ohio, 2001–2020, 2026-03-03(온라인 선공개), https://stacks.cdc.gov/view/cdc/258698, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-06 | 50. 안전 표준·인증·사고 조사 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-11-06/pages/topics/2026/2026-10-11-area50-s4.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1116, ref-1122, ref-1496]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#4
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어

# 50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 표준 개정과 사고 자료를 읽으려면 다음 용어를 알아야 한다. 이번 갱신에서 '적합성 추정'은 EU 관보 원문으로, '중상 보고'는 연구 원고로 다시 확인했다. [사실][^ref-1496][^ref-1122]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

표준 개정과 사고 자료를 읽으려면 다음 용어를 알아야 한다. 이번 갱신에서 '적합성 추정'은 EU 관보 원문으로, '중상 보고'는 연구 원고로 다시 확인했다. [사실][^ref-1496][^ref-1122] 이전 판(2026-09-30) 용어 목록은 [50. 안전 표준·인증·사고 조사 — 핵심 개념과 용어](2026-09-30-area50-s4.md)에 있다. 이번 판의 두 항목은 이전 판의 같은 항목을 대체한다.

- **[적합성 추정](../../glossary/presumption-of-conformity.md)(Presumption of Conformity)** — 위원회 시행결정 (EU) 2026/2015(2026-09-04 채택, 2026-09-07 관보 게재)는 기계류 지침 2006/42/EC 에 대해 적합성 추정을 주는 조화 표준 목록(시행결정 2023/1586 부속서 I)에 EN ISO 10218-1:2025 와 -2:2025 의 참조를 추가했다. [사실][^ref-1496] 같은 결정은 이 목록을 2027-01-20 부로 폐지한다. 지침 2006/42/EC 가 같은 날 기계 규정 (EU) 2023/1230 으로 폐지되기 때문이라고 적는다. [사실][^ref-1496] 따라서 이 게재는 지침에 따른 것이며 규정 (EU) 2023/1230 에 따른 조화 게재가 아니다. [사실][^ref-1496] 컨설팅사 IBF Solutions 는 2025 판이 PL d·범주 3 을 일률로 요구하지 않고 표의 기본 성능 수준이나 위험성평가 근거 가운데 고를 수 있게 했으며, 운전을 멈추는 정상 정지 기능을 새로 두었다고 해설한다. 이 해설은 벤더 주장이다. [추정][^ref-1116]
- **중상 보고(Severe Injury Reports, SIR)** — Sanders 외(2024)가 분석한 미국 산업안전보건청(OSHA) 중상 보고는 2015-01-01부터 2022-04-30까지의 자료다. [사실][^ref-1122] SIR 에는 연방 OSHA 관할 사업장의 보고만 들어 있다. 자체 주 계획(State Plan)을 운영하는 22개 주의 사업장은 빠진다. [사실][^ref-1122]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-09-30
[^ref-1122]: Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121), Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports, 2024, https://eprints.whiterose.ac.uk/id/eprint/217393/, 접근일 2026-10-11
[^ref-1496]: European Commission (Official Journal of the European Union), Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC, 2026-09-07, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-06 | 50. 안전 표준·인증·사고 조사 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-10-11-06/pages/topics/2026/2026-10-11-area50-s10.md

```markdown
---
title: "50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결"
type: topic
category: "M. 안전"
primary_area_no: 50
related_areas: [4, 22, 37, 38, 43, 48, 49, 51, 52, 55, 57, 58, 59, 61, 62, 65, 66, 67]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1084, ref-1096, ref-1120, ref-1496, ref-555, ref-831]
last_run: 2026-10-11
version: 1
split_from: docs/categories/safety/safety-standards-certification-and-incident-investigation.md#10
---

[홈](../../index.md) › [주제](../index.md) › 50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결

# 50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1120]
- 이 페이지는 [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 위험성평가·정지 절차, 인증 속성 등록, 사고 조사용 기록, 법정 인증·책임 분담을 매개로 여러 영역과 이어진다. 아래 연결은 이번 조사 결과를 세부영역 정의와 대조한 제안이다. [추정][^ref-1084][^ref-1120]


이전 판(2026-09-30)의 연결 목록은 [50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결](2026-09-30-area50-s10.md)에 있다. 이번 갱신(2026-10-11)에서는 그 목록에 아래 두 연결을 더했다.

- [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) — 사고 증거로 쓰는 기록을 얼마나 보존하고 어떻게 해석할지는 기록기 설정과 포맷 규칙에 따라 달라진다. rosbag2 의 스냅샷 버퍼 크기·정적 토픽 재삽입 깊이·유실 통계, MCAP 의 시각·CRC 규칙이 그 예다(7절). [추정][^ref-831][^ref-1096]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 이 영역은 두 가지 사실까지만 확인하고, 법적 효력 해석은 59. 법·규제·보험·라이선스 로 넘긴다. EN ISO 10218 의 EU 조화 게재가 2027-01-20 폐지되는 기계류 지침 기반 목록에 대한 것이라는 점, 기계 규정 부속서 III 의 기록 의무는 대상이 한정된다는 점이다(4·7절). [추정][^ref-1496][^ref-555]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md)
- 관련 영역: [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md), [67. 기타 현장](../../categories/site-type-applications/other-sites.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/safety/safety-standards-certification-and-incident-investigation.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1084]: The Robot Report, New AMR safety standard available with release of ANSI/A3 R15.08-2, 2023-10-26, https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/, 접근일 2026-09-30 (원문 미열람)
[^ref-1096]: MCAP 프로젝트 (Foxglove), MCAP Format Specification, 미확인, https://mcap.dev/spec, 접근일 2026-10-11
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-09-30
[^ref-1496]: European Commission (Official Journal of the European Union), Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC, 2026-09-07, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015, 접근일 2026-10-11
[^ref-555]: European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery, 2023-06, https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng, 접근일 2026-10-11
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-06 | 50. 안전 표준·인증·사고 조사 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1465건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | https://arxiv.org/abs/2502.20693 | 2026-09-25 | 아니오 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 2026-09-29 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 2026-09-30 | 예 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 2026-09-30 | 예 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | https://zdnet.co.kr/view/?no=20230728173101 | 2026-09-30 | 예 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 2026-09-30 | 예 |
| ref-1115 | The Robot Report | ISO 10218 industrial robot safety standard receives major overhaul | 2025-02 | https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/ | 2026-09-30 | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 2026-09-30 | 예 |
| ref-1117 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | https://iss.rs/en/project/show/iso:proj:83498 | 2026-09-30 | 예 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 2026-09-30 | 예 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | https://arxiv.org/abs/2205.06564 | 2026-09-30 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 2026-09-30 | 예 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 2026-09-30 | 예 |
| ref-1124 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | https://www.khan.co.kr/article/202311081103001 | 2026-09-30 | 예 |
| ref-1125 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 2026-09-30 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [50] 에 걸린 14건 / 전체 384건)

```markdown
- oq-170 [열림] ISO 3691-4:2023 의 운용 구역 분류와 사람 감지 요구가 이기종 플릿 관제 계층에 어떤 정보(구역·속도 제한·모드)를 요구하는지 표준 원문으로 확인할 수 있는가(이번 조사는 인증 기관 설명만 확인했다)? (영역 62, 50)
- oq-186 [열림] 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? (영역 66, 50, 59)
- oq-230 [열림] 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (영역 49, 50)
- oq-251 [열림] 국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가? (영역 50, 62)
- oq-252 [열림] 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? (영역 50, 37, 38)
- oq-253 [열림] 2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가? (영역 50, 48)
- oq-254 [열림] ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가? (영역 50, 64, 63)
- oq-265 [열림] ANSI/A3 R15.08-3-2026 이 사용자에게 요구하는 운영 절차·교육·변경 관리 항목은 무엇이며, 여러 제조사 로봇을 함께 쓰는 현장에서 누가 이를 이행하는가? (영역 40, 50, 58)
- oq-275 [열림] 서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가? (영역 56, 59, 50)
- oq-309 [열림] 이동로봇 안전 표준(ISO 3691-4 등)이나 국내 인증 기관이 시뮬레이션·가상 시운전 결과를 안전 확인 근거로 인정하는 조건과 절차가 있는가? (영역 50, 36, 54)
- oq-311 [열림] ISO/DIS 13482:2024 부속서 H 의 승강기 협동 로봇 요구가 국내 KS B 7317 과 어떻게 대응하는가? (영역 50, 22)
- oq-372 [열림] KS B 7317 의 2022-12-09 개정과 2025-05-09 개정은 각각 어떤 조항(요구사항·평가 방법)을 바꿨으며, 그 변경이 승강기 연동 계층이 확인해야 할 항목에 영향을 주는가? (관련 기존 질문: oq-098, oq-173, oq-311) (영역 22, 50)
- oq-383 [열림] 여러 제조사 로봇이 섞인 현장에서 STPA 제어 구조 분석, 변경 이력(수시 위험성평가), 근로자 아차사고 제보를 하나의 위험등록부로 연결해 운영한 공개 실증 사례가 있는가? (영역 48, 50)
- oq-384 [열림] 출처 충돌: ISO 3691-4 차기판 프로젝트의 현재 단계는 위키 기록(2026-09-26, ISO/CD 3691-4)과 외부 조사 메모(ISO/DIS 3691-4 제3판, 2026-09-10 단계 40.60) 가운데 어느 쪽인가? (관련 기존 질문 oq-170) (영역 48, 50)
```

### runs/2026-10-11-06/verification2.json

```json
{
  "run_id": "2026-10-11-06",
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
    "ok": true,
    "overlaps": [
      "이전 판 분리 페이지 docs/topics/2026/2026-09-30-area50-s4.md 41행과 2026-09-30-area50-s7.md 42·45행에는 IBF 해설만 근거로 한 [사실] 표기와 '절차·기준은 고시 제2023-211호가 정한다'는 서술이 그대로 남아 있다. 이번 판 4·7절 분리 페이지는 이 페이지들을 '이전 판'으로 링크하고, 같은 항목·행을 대체한다고 밝힌다. 두 페이지는 이번 입력에 없어 고칠 수 없었다. changelog_entry 와 additional_research_requests 에 후속 정정 대상으로 적혀 있으므로 이번 판정의 수정 지시 대상으로 삼지 않는다.",
      "docs/categories/safety/index.md 177행, docs/topics/2026/2026-09-26-area25-s7.md 45행, docs/topics/2026/2026-09-30-area52-s3.md 43행은 1차 지시대로 pages 에 넣지 않았다. changelog_entry 에 후속 정리 대상으로만 남겼다."
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
    "10절(patch action append. 코드 분리 결과는 docs/topics/2026/2026-10-11-area50-s10.md 3절): 추가 내용 앞에 이전 판 연결 목록으로 가는 문장을 넣는다. 예: '이전 판(2026-09-30)의 연결 목록은 [50. 안전 표준·인증·사고 조사 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area50-s10.md)에 있다.' 경로는 원 페이지 기준 상대 경로로 쓴다. 이유: 기존 원 페이지 10절에 있던 이전 분리 페이지 링크가 이번 재분리에서 빠졌다. 그 결과 실행 2026-09-30-15 에서 검증된 기존 연결 목록이 원 페이지에서도 새 분리 페이지에서도 링크되지 않는다. 4·6·7·8·11절 분리 페이지는 이전 판 링크를 두고 있으므로 10절도 같게 맞춘다.",
    "10절 추가 내용의 59 항목: '법적 효력 해석은 59번 영역으로 넘긴다'를 '법적 효력 해석은 59. 법·규제·보험·라이선스 로 넘긴다'로 고친다. 이유: 세부영역을 번호만으로 부르는 표기는 금지다(공통 규칙 6절).",
    "6절 CAST 소절(분리 결과 2026-10-11-area50-s6 3절): '조사 질문은 세 가지다.'를 개수를 단정하지 않는 문장으로 고친다. 예: '강의 자료는 다음을 조사 질문으로 던진다.' 이유: f31 은 강의 자료가 이 질문들을 던진다고만 적는다. 질문이 세 개뿐이라는 근거는 브리프에 없다.",
    "5절 제조 공장 '용접 팁 교체' 사례 표의 제약 칸: '공단의 재발방지대책은 세 가지다.'를 '공단의 재발방지대책은 다음을 제시한다.'로 고친다. 이유: f30 은 대책의 내용만 전하고 항목 수는 전하지 않는다.",
    "프런트매터 sources(4절 patch 의 frontmatter): 원 페이지 본문과 13절 각주 정의에 실제로 남는 출처와 일치시킨다. ref-1497·ref-1498·ref-1499·ref-1500·ref-1255·ref-211·ref-555·ref-831·ref-1096 은 분리된 7·10·11절 주제 페이지에서만 인용된다. 원 페이지 본문과 13절에는 없으므로 원 페이지 sources 에서 뺀다. 분리 페이지는 각자 sources 를 가진다. 재분리 결과가 이번과 달라지면 그 결과에서 원 페이지에 남은 각주를 기준으로 맞춘다. 이유: 실행 2026-09-30-15 의 2차 수정(프런트매터 sources 를 각주 정의와 일치)과 같은 기준이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 49건, 미확인 0건, 교차 확인 0건. 확인 49건 가운데 검증자가 원문을 직접 대조한 것이 19건, 부분 대조한 것이 2건이다. 리서치 열람 기록에 기댄 것이 21건, 원문 미열람 기록에 기댄 것이 1건(f4), 의견이 6건이다. 강등: 이번 브리프 finding 의 강등은 없다. 기존 4·7절의 PL d·범주 3·정상 정지 서술은 사실에서 추정(IBF 해설, 벤더 주장)으로 강등했고, 이번 판에 반영됐다. 원문 미열람 출처: ref-1255(이번 실행). ref-1116·ref-1120 은 이번에 다시 열지 않았다. 열린 질문: oq-230 해결 인정(f17·f18·f19), oq-384 해결 인정(f5). oq-186 은 부분 답만 있어 열림을 유지한다. 정정 요청 없음. 주의: 실외이동로봇 고시 두 판과 KOSHA 재해사례·EBB 게재본·MIT 강의 PDF 는 검증 시점에 본문을 다시 열지 못했다. 고시 관련 출처는 같은 정부 계열이라 독립 교차 확인으로 세지 않았다. 제2023-211호 시행일은 출처끼리 충돌해 확정하지 않는다. EU 조화 게재는 기계류 지침 2006/42/EC 기반 목록에 대한 것이며, 이 목록은 2027-01-20 폐지된다. 이전 판 분리 페이지(2026-09-30-area50-s4·s7)에는 강등 전 [사실] 표기와 낡은 고시 근거가 남아 있어 후속 정정이 필요하다. CAST 약어의 원어 병기는 출처 미확인으로 추가 조사 요청에 남아 있다. / 2차 수정 후 재검증. 드리프트 2건 처리(CAST 조사 질문·재발방지대책의 개수 단정). [분류원문] 보존, 섹션 순서 준수. 1차 수정 지시 21건은 이행됐다(범위 밖 이전 판 분리 페이지는 입력이 없어 후속 정리로 남김). 링크: 10절 재분리에서 이전 판 연결 목록 링크가 빠졌고, '59번 영역' 번호 단독 표기가 있다. 프런트매터 sources 와 원 페이지 각주가 맞지 않는다. 2차 검증에서 검색·열람 도구는 쓰지 않았다.",
  "retry_reason": null
}
```
