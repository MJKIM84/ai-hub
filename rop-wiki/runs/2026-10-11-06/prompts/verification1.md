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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### docs/categories/safety/human-proximity-safety.md (요약)

```markdown
# 49. 사람 근접 안전

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
```

### docs/categories/robot-ontology/heterogeneous-robot-registration.md (요약)

```markdown
# 4. 이기종 로봇 등록

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

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

### docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md (요약)

```markdown
# 37. 관제 화면·실행 기록

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

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

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

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

### docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md (요약)

```markdown
# 52. 통신 보호·위협 관리·감사

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **통신 보호**: 로봇·플랫폼·설비 사이 통신을 암호화하고 무결성을 지킨다(ROS 2 보안 등)
- **보안 위협 모델·취약점 관리**: 위협 모델을 세우고 취약점을 찾아 고친다(ROS 2 위협 모델, IEC 62443 등)
- **문서·대화 입력 보안**: 문서나 대화에 숨은 지시를 명령으로 실행하지 않게 막는다(프롬프트 주입 방지)
- **명령·승인 감사 기록**: 누가 언제 무엇을 지시·승인·변경했는지 지울 수 없게 기록한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md (요약)

```markdown
# 55. 현장 조사·설치·시운전

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 조사, 설치·설정, 교정, 시운전, 인수 시험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 설치·설정**: 로봇·충전기·네트워크·설비를 설치하고 설정하며, 반복되는 설치 절차를 자동화한다
- **교정**: 센서·좌표·지도를 현장에 맞게 교정한다
- **현장 시운전**: 연동과 작업을 현장에서 시험 운전하며 문제를 잡는다
- **현장 조사**: 설치 전에 현장 치수·네트워크·설비·동선을 조사한다
- **인수 시험**: 합의한 수용 기준으로 인수 여부를 판정한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 21번 영역 ‘온보딩·설정·현장 시운전’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [옛 분류원문]

> 옛 질문: 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

새 현장에 설치하고 시운전할 때 반복 작업을 얼마나 줄일 수 있는가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md (요약)

```markdown
# 58. 다사업자 책임·계약·데이터

소속 대분류: P. 거버넌스·법규·사회 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

책임과 변경 승인, 데이터 소유권, API 변경 정책, 서비스 수준·감사 이력 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다사업자 책임·변경 승인**: 연동 오류를 누가 고치고 변경을 누가 승인할지 정한다
- **데이터 소유권**: 운영 데이터를 누가 갖고 어디까지 쓸 수 있는지 정한다
- **API 변경 정책**: 제조사와 플랫폼의 API가 바뀔 때 호환성과 공지 방식을 정한다
- **서비스 수준·감사 이력**: 서비스 수준 약속과 감사 이력을 정하고 지킨다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’에서 왔다. 그 본문은 [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
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

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/home-and-apartment.md (요약)

```markdown
# 65. 가정·공동주택

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]
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

### docs/categories/site-type-applications/other-sites.md (요약)

```markdown
# 67. 기타 현장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

점검·순찰(플랜트·데이터센터·빌딩), 건설, 농업, 공공시설, 오피스, 연구실 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **점검·순찰 적용**: 플랜트·데이터센터·건물의 순찰·점검 로봇 운영을 다룬다
- **기타 현장 적용**: 건설 현장·농업·공항과 역 같은 공공시설·오피스 빌딩·연구실의 로봇 운영을 다룬다

## 2. 핵심 질문

점검·건설·농업·공공시설 같은 다른 현장은 무엇이 다른가? [분류원문]
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

### runs/2026-10-11-05/research.md

```markdown
# 리서치 브리프 2026-10-11-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-05 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 49. 사람 근접 안전 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area49-s4) — NIST SSM 논문 연도를 '2016' 으로 적어 학술지 게재 연도(2017)와 다름
- 섹션 5. 적용 사례 — 병원 사례를 '시뮬레이션 평가' 로 잘못 분류(89행), 창고 연구(74행)는 '정량 결과 미확인', 아마존 글 '발행일 미확인'(72행), 실외 사례 제약 칸(100행)이 2023 기사의 '당시 개정안' 수치에만 기대고 현행 고시 원문 근거가 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area49-s6) — 구역 지원 신고·적재 외곽 기준 진입, Nav2·RMF 의 0 값 의미 차이, 감지 응답시간 보정 요인이 없고, Farrell(55행)·Jafari(61행) 문장이 실험 조건을 '미확인' 으로 둠
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area49-s7) — 실외 인증 행이 인증기관 페이지·기사 근거뿐이고 시행규칙·고시 원조문이 없음. ISO 13482:2014·ISO 10218-1:2025 범위·국내 실내 KS(KS B 8252) 행 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area49-s8) — Farrell·HATA·Jafari 서지가 프리프린트 기준이고 Rondoni 제목·환경 표현 부정확, HATA 평가가 시뮬레이션이라는 점과 실패율 정의 없음
- 섹션 9. 책임 경계 — 사람 위치를 플릿에 전달하는 공개 구현과 그 한계(좌표계·변환 실패), 실외 인증의 운행계획서·보행자 밀집 알림 요구 미반영
- 섹션 11. 열린 질문 — oq-229·oq-230·oq-231·oq-232 부분 근거 미반영
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정 5건(f1·f14·f20·f24·f49)

## 조사 질문

1. 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
2. oq-229 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? (섹션 6·9·11 겨냥)
3. oq-230 출처 충돌: 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? (섹션 5·7·11 겨냥)
4. oq-231 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (섹션 7·11 겨냥)
5. oq-232 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (섹션 9·11 겨냥)
6. 바뀐 출처: 병원·창고·편안함 연구의 실험 조건과 출판 서지, 현행 실외 인증 고시 별표의 실제 기준은 무엇인가? (섹션 5·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Marvel·Norcross(NIST)의 SSM 논문 학술지판은 Robotics and Computer-Integrated Manufacturing 44권(2017) 144–155쪽에 실렸고, 2015-03-04 접수·2016-08-01 승인됐다. 위키 4절·8절과 분리 페이지의 '2016년 논문' 표기는 승인 연도 기준이라 게재 연도(2017)와 다르다. | ref-1075 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [추정] | SICK 의 기술 블로그는 안전 레이저 스캐너에서 감시 케이스(보호 필드 집합) 사이를 전환하면 시스템 응답시간이 늘어나고, 다중 샘플링 값을 올리면 물체가 연속으로 더 여러 번 감지돼야 출력이 꺼지므로 응답시간 보정분이 더해진다고 설명한다. | ref-1466 | 아니오 | low | 2026-10-11 | 제약 | 벤더 주장 |
| f3 | [사실] | VDA 5050 3.0.0 은 로봇마다 처리할 수 있는 구역 유형이 다르므로, 모든 이동 로봇이 이해할 수 있는 구역 이름을 factsheet 의 typeSpecifications.supportedZones 배열로 플릿 관제에 보고하도록 요구한다(shall). | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f4 | [사실] | 같은 명세의 외곽 기준 구역(contour-based zones)에서는 적재물을 포함한 로봇 외곽이 구역 진입·이탈을 정하며, 외곽의 어느 부분이라도 구역에 들어가면 진입이고 외곽이 모두 빠져나가야 이탈이다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f5 | [의견] | ROP 가 구역 속도 제한을 등록할 때는 로봇별 supportedZones 신고를 먼저 확인하고, 적재물로 커진 외곽이 진입 경계에 닿기 전에 감속을 마치도록 감속 시작 지점을 경계 앞에 두며, 실제 감속을 통합 시험으로 확인하는 절차가 필요하다. | ref-031 | 아니오 | low | 2026-10-11 | 제약 | — |
| f6 | [사실] | Nav2(Jazzy) Collision Monitor 문서는 source_timeout(기본 2.0초) 안에 새 센서 데이터가 오지 않으면 로봇을 정지시키며, source_timeout 을 0.0 으로 두면 이 차단 동작이 꺼진다고 설명한다. | ref-1467 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | Nav2(Jazzy) Speed Filter 에서 speed_limit 메시지 값 0 은 정지가 아니라 '속도 제한 없음'을 뜻하며, 이는 백분율·절댓값 설정과 관계없다. | ref-1468 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | Open-RMF rmf_fleet_adapter 2.14.0 의 차선 속도 제한(limit_lane_speeds) 처리는 요청 속도가 0 이하이거나 차선 번호가 그래프 범위를 벗어나면 경고만 남기고 그 요청을 무시하며, 경고문은 차선을 닫으려면 close_lanes API 를 쓰라고 안내한다. | ref-1464 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | 같은 코드에서 유효한 속도 제한은 계획 그래프의 차선 속성(speed_limit)에 기록된 뒤 새 Planner 를 만들어 작업 파라미터에 넘기고 차선 상태를 발행하는 데서 끝나며, 차량이 실제로 감속을 마쳤는지 확인하는 경로는 이 함수에 없다. | ref-1464 | 아니오 | medium | 2026-10-11 | — | — |
| f10 | [추정] | Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 모두 '정지'를 뜻하지 않으므로, 이종 플릿 어댑터가 '0' 을 정지 명령으로 그대로 옮기면 의도와 반대로 제한이 풀리거나 무시될 수 있는 것으로 보인다. | ref-1467, ref-1468, ref-1464 | 아니오 | low | 2026-10-11 | 제약 | — |
| f11 | [의견] | ROP 어댑터 계약은 '제한 없음', '양수 속도 제한', '통로 폐쇄', '보호 정지'를 서로 다른 명령으로 표현하고, 구역 전송·활성화·계획 반영·차량 감속 관측을 별개 상태로 기록해 계획 상태 갱신만으로 감속 완료를 보고하지 않도록 해야 한다. | ref-1464, ref-1468, ref-031 | 아니오 | low | 2026-10-11 | 제약 | — |
| f12 | [사실] | Farrell 외의 창고 연구는 Freight·Jackal·Megarover 실물 로봇으로 실험했고, 로봇과 보행자 위치는 OptiTrack 모션 캡처로 측정했다. 정적·동적 장애물 회피 단위 실험은 설정마다 10회 수행했다. | ref-1082 | 아니오 | medium | 2026-10-11 | 물류창고 / 수행 자원 | — |
| f13 | [사실] | 같은 연구의 Open-RMF 플릿 실험(Table IV)은 로봇 4대·최고 1.0 m/s 또는 2대·1.5 m/s 설정에서 보행자 0·1·2명 조건을 비교했고, 표의 값은 Open-RMF 상위 계획기가 로봇을 일부러 세워 둔 시간을 뺀 것이다. | ref-1082 | 아니오 | medium | 2026-10-11 | 물류창고 / 예외·성과 | — |
| f14 | [추정] | 정정 제안: 49영역 본문 74행('정량 결과는 미확인')·2026-09-30-area49-s6.md 55행('정량 결과 미확인')·2026-09-30-area49-s8.md 42행('2025-03, 프리프린트 … 정량 결과 미확인')은 실물 실험 조건(f12)과 Table IV 조건·분모(f13)를 적고, 서지를 2025 IEEE CASE(pp.548–555, 2025-08-17) 게재로 고치는 것이 맞아 보인다. 현장 배치 사례가 아니라 연구 평가라는 기존 구분은 유지한다. | ref-1082 | 아니오 | medium | 2026-10-11 | 물류창고 / 예외·성과 | — |
| f15 | [사실] | HATA(Kazemi Eskeri 외) 논문의 5·10·15대 플릿 평가는 실제 기록된 사람 궤적을 재생하는 시뮬레이션 환경에서 수행됐다. | ref-1083 | 아니오 | medium | 2026-10-11 | — | — |
| f16 | [사실] | 같은 논문의 실패율은 교착 또는 10분 제한시간 초과로 완료하지 못한 과제의 비율로, 사고율이나 사람과의 충돌률이 아니다. | ref-1083 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | Tartu 병원 현장 시험 논문은 TIAGo·Clearpath Jackal 이종 로봇을 RMF 로 관리하는 능력을 '시험 환경'에서 검증했고, 병원 안에서 여러 배송 로봇을 운용하는 것은 아직 하지 않은 향후 과제로 적었다. | ref-869 | 아니오 | medium | 2026-10-11 | 병원 / 수행 자원 | — |
| f18 | [사실] | Rondoni 외(Scientific Reports, 2024-08-07)의 병원 주행 벤치마크는 컴퓨터 시뮬레이션이 아니라, 병상·복도·대기 공간·가구 등 실제 병원의 물리적 배치를 재현한 모의 병원 공간에서 HOSBOT·TIAGo 실물 로봇으로 수행됐고 Vicon 카메라 8대로 위치를 측정했다. | ref-1081 | 아니오 | medium | 2026-10-11 | 병원 / 작업 대상 | — |
| f19 | [사실] | 같은 연구의 이동 장애물은 사람이 아니라 정해진 경로를 고정 선속도·각속도로 원격조종해 움직인 두 번째 시험용 이동 로봇 베이스였다. | ref-1081 | 아니오 | medium | 2026-10-11 | 병원 / 제약 | — |
| f20 | [추정] | 정정 제안: 49영역 본문 89행 '이 사례는 실제 병원이 아닌 모의 병원 환경에서 수행한 시뮬레이션 평가다' 는 '실제 병원 구조를 재현한 모의 병원 공간에서 실물 로봇으로 수행한 실험 평가(이동 장애물은 원격조종 로봇)' 로 고치는 것이 맞아 보인다. 2026-09-30-area49-s8.md 41행의 논문 제목도 원문대로 단수 'hospital environment' 로 맞춘다. | ref-1081 | 아니오 | medium | 2026-10-11 | 병원 / 작업 대상 | — |
| f21 | [사실] | Jafari·Nguyen·Liu 의 보행자 편안함 실험 참가자는 23~41세 자원자 32명(남 22·여 10)이었고, 폭 3.2 m 복도에서 원격조종 로봇이 1.4·2.8 m/s 로 움직였으며, 160회 시행 중 데이터 수집이 완전히 실패한 2회를 뺐다(측면 거리 관련 분석은 13회를 더 뺐다). | ref-1085 | 아니오 | medium | 2026-10-11 | 작업 대상 | — |
| f22 | [사실] | 같은 연구의 복합 예측기는 분석에 쓴 데이터와 같은 데이터로 평가돼, 독립 시험 집합에서의 성능은 아니다. | ref-1085 | 아니오 | medium | 2026-10-11 | — | — |
| f23 | [사실] | 논문의 오즈비 3.67 은 복합 예측기가 '편안함'으로 예측했을 때 실제로 편안했을 오즈가 그렇지 않게 예측했을 때보다 3.67배라는 뜻으로, 사고 감소 확률이나 안전 거리 기준이 아니다. | ref-1085 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [추정] | 정정 제안: 2026-09-30-area49-s6.md 61행의 '(실험 장소·참가자 수 미확인)' 은 참가자 32명·3.2 m 복도·원격조종 로봇·1.4/2.8 m/s 조건(f21)과 같은 데이터 평가 한계(f22)로 바꾸고, 2026-09-30-area49-s8.md 40행의 '(2026-04, 프리프린트)' 는 'ICRA 2026 채택(arXiv 저자판)' 으로 고치는 것이 맞아 보인다. | ref-1085 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | 지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의4제1항은 운행안전인증 기준으로 로봇의 최대 질량(적재물 포함) 500 kg 이하(1호)와 최대 속도 시속 15 km 이하(2호)를 정하고, 제2항은 그 밖의 세부사항을 산업통상부장관 고시로 위임한다. | ref-1470 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f26 | [사실] | 같은 시행규칙 제7조의5제1항은 운행안전인증 신청서에 횡단보도 통행방식, 통신장애 대응 시나리오, 사고발생 대응 시나리오, 혼잡상황 대응 시나리오 등을 담은 운행계획서를 첨부해 제출하도록 한다(4호). | ref-1470 | 아니오 | medium | 2026-10-11 | 실외 / 시작 조건 | — |
| f27 | [사실] | 현행 「실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시」는 산업통상부고시 제2025-21호(2025-11-24 일부개정)이며 부칙에 따라 발령한 날부터 시행하고, 제4조는 운행안전인증 기준을 별표 3 으로 정한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 | — |
| f28 | [사실] | 고시 제2025-21호 별표 3(실외이동로봇 운행안전인증 기준)의 상위 항목은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개이며, 한국로봇산업진흥원 인증 안내 페이지의 '총 8개 심사항목' 이름과 같다. | ref-1469, ref-980 | 아니오 | medium | 2026-10-11 | 실외 | — |
| f29 | [사실] | 별표 3 의 1.규격 및 운행속도는 로봇과 적재물 질량 합계 500 kg 초과를 금지하고, 최대 운행 속도를 질량 230 kg 초과 500 kg 이하 5 km/h, 100 kg 초과 230 kg 이하 10 km/h, 100 kg 이하 15 km/h 로 정한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f30 | [사실] | 별표 3 1.라는 도로교통법상 어린이 보호구역·노인 보호구역·장애인 보호구역에서 로봇이 최대 운행 속도 5 km/h 를 지키는지 확인하도록 한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f31 | [사실] | 별표 3 4.주변 인식은 로봇이 지정된 운행구역을 지키고 제한된 금지구역에 들어가지 않을 것(가), 사람이나 장애물을 감지해 안전하게 감속·정지 또는 회피할 것(다)을 요구하며, 다목의 평가 방법은 KS B 7320 의 5.6절(장애물 감지와 회피)을 따른다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f32 | [사실] | 별표 3 7.횡단보도 통행은 대기 장소에 도착했을 때 보행 신호가 이미 켜져 있으면 정지 상태로 기다렸다가 다음 보행 신호에 횡단하도록 하고(가.3), 횡단 중 통신이 끊기면 횡단을 마친 뒤 안전한 곳에 정차하도록 한다(나). | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f33 | [사실] | 별표 3 8.관제장치 다목은 주행 경로가 보행자 밀집 등으로 통행할 수 없으면 로봇이 관제장치에 알리고 관리자가 조치할 수 있어야 한다고 정한다. | ref-1469 | 아니오 | medium | 2026-10-11 | 실외 / 예외·성과 | — |
| f34 | [추정] | 49영역 본문 5절 실외 사례 제약 칸(100행)이 2023-07-28 기사의 '당시 개정안'으로 전한 질량별 속도 구간(230·100 kg 경계, 5·10·15 km/h)과 횡단보도 대기 규칙은 현행 고시 제2025-21호 별표 3 의 값과 같으므로, 현행 고시 원문을 근거로 바꿔 쓰고 보호구역 5 km/h 를 덧붙일 수 있어 보인다. | ref-1469, ref-992 | 아니오 | medium | 2026-10-11 | 실외 / 제약 | — |
| f35 | [의견] | ROP 가 실외 로봇의 관제 역할을 맡으면, 운행계획서의 통신장애·혼잡 대응 시나리오와 별표 3 8.다의 보행자 밀집 알림·관리자 조치, 보호구역 5 km/h 를 구역별 속도 제한 정책과 알림 흐름으로 연결해 두는 것이 필요하다. | ref-1469, ref-1470 | 아니오 | low | 2026-10-11 | 실외 / 예외·성과 | — |
| f36 | [사실] | ISS(세르비아 표준원)가 제공하는 ISO 프로젝트 정보에서 ISO 13482:2014 는 2014-02-03 발행, 현재 단계 90.92(개정 예정)의 발행 표준(Published)으로 표시된다. | ref-1471 | 아니오 | medium | 2026-10-11 | — | — |
| f37 | [사실] | ISS 가 제공하는 ISO 10218-1:2025(2025-02-05 발행) 적용 범위는 로봇·매니퓰레이터가 무인 산업용 트럭이나 이동 플랫폼에 고정되거나 그 일부일 때의 이동성(mobility) 관련 위험을 이 문서가 다루지 않는다고 적는다. | ref-1472 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [사실] | 국가표준 KS B 8252 '실내 이동로봇의 보호정지 시험방법'은 안전한 실내 공간에서 이동 로봇이 자율 주행할 때 정적 장애물에 대한 보호정지를 평가하는 시험방법 표준으로 ISO 13482 를 기반으로 하며, 2020-02-26 제정(고시 2020-0026)·2025-09-05 확인(고시 2025-0241, 5년 도래 확인)됐다. | ref-1473 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [추정] | 확인한 국내 실내 이동로봇 KS(KS B 8252)는 정적 장애물에 대한 보호정지 시험방법이어서, 움직이는 사람과의 속도·거리 기준값이나 병원·상업 시설·공동주택 실내 운행을 강제하는 기준은 이번에도 확인되지 않았다(oq-231 부분 근거). | ref-1473, ref-1471 | 아니오 | low | 2026-10-11 | — | — |
| f40 | [사실] | 공개 ROS 2 패키지 human_detection_fusion 은 YOLO 검출과 UWB 위치를 합쳐 사람 식별자별 위치를 '/humans/persons/<id>/position' 토픽에 ROS4HRI 의 hri_msgs/PointOfInterest3DStamped 형식으로 발행한다. | ref-1474 | 아니오 | medium | 2026-10-11 | 수행 자원 | — |
| f41 | [사실] | 같은 코드의 transformUWBPosition 함수는 UWB 좌표를 계획 좌표계로 바꾸다 TF 변환 예외가 나면 경고 로그를 남기고 입력 좌표를 그대로 돌려준다. | ref-1474 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [추정] | 호출부는 반환된 좌표에 header.frame_id 를 TARGET_FRAME(계획 좌표계)으로 붙여 발행하므로, 변환이 실패하면 UWB 좌표계 값이 계획 좌표계 값으로 표시돼 나갈 수 있어 보인다. 실제 운용에서 오류가 났는지, 상위 계층이 이를 보정하는지는 확인하지 못했다. | ref-1474 | 아니오 | low | 2026-10-11 | 제약 | — |
| f43 | [사실] | 이 저장소의 'KIRO' 는 EU ARISE 1차 공개 모집의 실험 이름으로, 한국로봇융합연구원(KIRO)과는 다른 것이며, 저작권자는 그리스 연구기관 ATHENA RC 이고 라이선스는 AGPL-3.0 이다. | ref-1474 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 사람 위치를 받아 플릿 감속·정지에 쓰는 ROP 연계에는 측정 시각, 좌표계, 변환 성공 여부, 만료 시각을 메시지에 명시하게 하고, 위치 수신과 차량의 실제 감속 확인을 별도 단계로 시험해야 한다. | ref-1474, ref-1080 | 아니오 | low | 2026-10-11 | 제약 | — |
| f45 | [추정] | 확인한 자료 범위에서 사람 위치를 여러 제조사 플릿에 동시에 전달해 감속·정지시키는 공통 안전 인터페이스는 없고, 기업 단독 사례(아마존 조끼, 벤더 주장)와 사람 위치 발행 형식만 정한 공개 구현(ROS4HRI 기반 human_detection_fusion)이 따로 있는 것으로 보인다(oq-232 부분 근거). | ref-1080, ref-1474 | 아니오 | low | 2026-10-11 | — | — |
| f46 | [사실] | NavWareSet 프로젝트는 통제된 실내 수집 실험에 참가자 총 17명이 참여했고 5명씩 2개 그룹과 5개 쌍으로 나뉘었다고 설명한다. | ref-1475 | 아니오 | medium | 2026-10-11 | 작업 대상 | — |
| f47 | [사실] | NavWareSet 의 시나리오에는 시야가 가려진 모퉁이에서 로봇과 사람이 마주치는 'BLIND CORNER' 가 포함된다. | ref-1475 | 아니오 | medium | 2026-10-11 | — | — |
| f48 | [의견] | 사람 근접 감속·정지 정책의 재생 시험에는 가려진 모퉁이·통로 점유·혼잡 장면을 넣고, 아동·보행 보조기·휠체어 사용자처럼 감지 특성이 다른 보행자를 따로 평가해야 하며, 기존 데이터셋만으로 취약 보행자 범위가 충족됐다고 보면 안 된다. | ref-1475, ref-1085 | 아니오 | low | 2026-10-11 | — | — |
| f49 | [추정] | 아마존의 로보틱스 테크 조끼 설명 글은 페이지 메타데이터 기준 2019-04-06 에 발행됐다. 49영역 본문 72행과 2026-09-30-area49-s6.md 55행의 '발행일 미확인' 을 이 날짜로 고칠 수 있다. | ref-1080 | 아니오 | low | 2026-10-11 | 물류창고 | 벤더 주장 |
| f50 | [추정] | 확인한 명세·코드는 구역 제한의 지원 신고(supportedZones)·적재 외곽 기준 진입 판정·계획 계층 속도 반영까지만 다루고, 플릿 구역 제한을 위험성 평가의 위험 감소 조치로 인정하는 조건이나 로봇 보호 필드 설정과의 정합을 누가 검증하는지는 다루지 않는다(oq-229 부분 근거). | ref-031, ref-1464, ref-1467 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1466 | SICK (Martin Kidman) | The perfect size of the protective field on an industrial autonomous vehicle | 2021-02-09 | 벤더 문서 | medium | 2026-10-11 | https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle | 아니오 |
| ref-1467 | Open Navigation (Nav2 documentation, Jazzy) | Collision Monitor Node — Nav2 Docs (Jazzy) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/ | 아니오 |
| ref-1468 | Open Navigation (Nav2 documentation, Jazzy) | Speed Filter Parameters — Nav2 Docs (Jazzy) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/ | 아니오 |
| ref-1469 | 산업통상부 (국가법령정보센터 행정규칙) | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준 | 2025-11-24 | 정부·연구기관 | high | 2026-10-11 | https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426 | 아니오 |
| ref-1470 | 법제처 국가법령정보센터 | 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의4·제7조의5 | 2025-10-01 | 정부·연구기관 | high | 2026-10-11 | https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075 | 아니오 |
| ref-1471 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots | 2014-02-03 | 표준 | medium | 2026-10-11 | https://iss.rs/en/project/show/iso:proj:53820 | 아니오 |
| ref-1472 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO 10218-1:2025 Robotics — Safety requirements — Part 1: Industrial robots | 2025-02-05 | 표준 | medium | 2026-10-11 | https://iss.rs/en/project/show/iso:proj:73933 | 아니오 |
| ref-1473 | 국가기술표준원 (e-나라표준인증) | KS B 8252 실내 이동로봇의 보호정지 시험방법 | 2020-02-26 | 표준 | high | 2026-10-11 | https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB8252&menuId=919&reformNo=&tmprKsNo=KSB8252&topMenuId=502&upperMenuId=503 | 아니오 |
| ref-1474 | ATHENA RC (유지관리 Andreas Vatistas, Nikolaos Lappas) — EU ARISE 'KIRO' 실험 | human_detection_fusion — src/yolo_uwb_fusion_node.cpp 및 README (커밋 934ca8387a205aaac894da22451970a203777e18) | 2026-06-29 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp | 아니오 |
| ref-1475 | Brayan, J., Deng, S., Alves Neto, A., Okunevich, I., Krajnik, T., Bremond, F., & Yan, Z. (NavWare 프로젝트) | NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation (프로젝트 사이트) | 2026-05-24 | 논문 | medium | 2026-10-11 | https://anr-navware.github.io/navwareset/ | 아니오 |
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2017 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1464 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter 2.14.0 소스 — FleetUpdateHandle.cpp(handle_target_emergency)·Node.cpp(비상 신호 구독) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp | 아니오 |
| ref-1082 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv; 2025 IEEE CASE) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2503.21141 | 아니오 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-869 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 2022-08-23 | 논문 | high | 2026-10-11 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full | 아니오 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environment | 2024-08-07 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 아니오 |
| ref-1085 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv; IEEE ICRA 2026 채택) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2604.13677 | 아니오 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 2019-04-06 | 벤더 문서 | low | 2026-10-11 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 아니오 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-11 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | 기사 | low | 2026-10-11 | https://zdnet.co.kr/view/?no=20230728173101 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/human-proximity-safety.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area49-s4) — NIST 논문 서지 정정: 학술지판 RCIM 44(2017), 2016-08-01 승인(f1). 본문 53행·s4 28·37행·s8 37행의 '2016' 표기를 '2017(2016 승인)'으로. ZR·ZS 위치 불확실성(메모 H02)은 기존 내용 확인(2026-09-30-area49-s4.md 38행) / 섹션 5 — 물류창고: 아마존 글 발행일 2019-04-06(f49, 벤더 주장 [추정]; 본문 72행·s6 55행 '발행일 미확인' 정정), Farrell 연구 문단(본문 74행)의 '정량 결과는 미확인' 정정 — 실물 로봇·OptiTrack·설정별 10회(f12), Table IV 4대·1.0 m/s/2대·1.5 m/s·보행자 0~2명·정지 구간 제외(f13), CASE 2025 서지(f14). 병원: 89행 '시뮬레이션 평가' 정정 — 실제 병원 배치를 재현한 모의 병원의 실물 실험·Vicon 8대(f18), 이동 장애물은 원격조종 로봇(f19), 정정 제안 f20. 같은 오류가 docs/categories/safety/index.md 125행·187행에도 있으나 이번 실행 범위 밖이라 후속 정리 필요. Tartu: 이종 다로봇은 시험 환경·병원 내 복수 배송 로봇은 향후 과제(f17), 혈액 운반 시연(메모 H19)은 기존 내용 확인(ref-869). 실외: 제약 칸(100행)의 질량별 속도·횡단 대기를 2023 기사 '당시 개정안'에서 현행 고시 제2025-21호 별표 3 근거로 바꾸고(f27·f29·f32·f34), 보호구역 5 km/h(f30), 감속·정지·회피(f31), 보행자 밀집 알림(f33)을 더함; 시행규칙 원조문(f25, 수치는 기존·근거만 새), 운행계획서 시나리오(f26), 의견 f35 / 섹션 6(분리 2026-09-30-area49-s6) — 보호 분리 거리: SICK 케이스 전환·다중 샘플링 응답시간(f2, 벤더 주장 [추정]); NIST 0.113 s(메모 H01)는 기존 내용 확인(s6 41행). 플릿 구역: supportedZones 보고 의무(f3), 적재 외곽 기준 진입(f4), 의견 f5; maximumSpeed m/s·진입 시 이미 제한 속도 도달(메모 H06·H07)은 기존 내용 확인(docs/categories/safety/index.md 77행), zoneSetId 변경·DISABLED 후 enableZoneSet(메모 H08·H09)은 기존 내용 확인(2026-09-30-area16-s6.md 49행, 2026-09-30-area16-s4.md 40행). 로봇 측: source_timeout 0.0 차단 해제(f6), speed_limit 0 = 제한 없음(f7), RMF 0 이하 무시·close_lanes(f8)·계획 반영까지만(f9), 0 값 의미 차이 [추정](f10), 의견 f11; Nav2 하드 실시간 인증 미제공(메모 H10)은 기존 내용 확인(s6 47행, ref-1077). s6 55행 Farrell 문장 정정(f12·f13), s6 57행 HATA 는 시뮬레이션·실패율 정의(f15·f16) 보강. s6 61행 Jafari '(실험 장소·참가자 수 미확인)' 정정 — 32명·3.2 m 복도·1.4/2.8 m/s·원격조종(f21), 같은 데이터 평가(f22), 오즈비 의미(f23), 정정 제안 f24. 데이터셋: NavWareSet 17명(f46)·BLIND CORNER(f47), 의견 f48 / 섹션 7(분리 2026-09-30-area49-s7) — 실외이동로봇 운행안전인증 행(44행): 시행규칙 제7조의4·제7조의5 원조문(f25·f26), 현행 고시 제2025-21호(f27)·별표 3 상위 8개 항목과 인증기관 8개 항목 일치(f28), 질량별 속도(f29). 새 행: ISO 13482:2014 발행·90.92(f36; ISO/FDIS 13482 50.20·2026-09-15(메모 H30)은 기존 내용 확인 — ref-1117), ISO 10218-1:2025 범위의 이동성 위험 제외(f37, 판 번호는 쓰지 않음), KS B 8252 정적 장애물 보호정지 시험방법(f38)과 한계(f39). Nav2 Collision Monitor 행에 source_timeout(f6), Speed Filter 0 값(f7) 추가 / 섹션 8(분리 2026-09-30-area49-s8) — Farrell 항목(42행) 서지를 CASE 2025(pp.548–555, 2025-08-17)로·'정량 결과 미확인' 삭제(f14), Rondoni 항목(41행) 제목 단수 'environment'·'모의 병원 환경' → 실물 모의 병원 실험(f20), Jafari 항목(40행) ICRA 2026 채택·32명(f24), HATA 항목(43행) IROS 2025 pp.12697–12703·시뮬레이션 평가·실패율 정의(f15·f16), NIST 항목 연도(f1), NavWareSet 새 항목(f46·f47) / 섹션 9 — 로봇 자체 지능·제어 행: 0 값 계약 차이와 어댑터 명령 구분(f10·f11), 사람 위치 연계 공개 구현 human_detection_fusion 의 ROS4HRI 발행(f40)·변환 실패 시 원좌표 반환(f41)·좌표계 표기 문제 [추정](f42)·'KIRO' 는 EU ARISE 실험 이름(f43, 한국로봇융합연구원 아님), 의견 f44; 업종별 조건 행: 운행계획서·보행자 밀집 알림(f26·f33·f35). 아마존 조끼(메모 H34)는 기존 내용 확인(본문 65~72행), 발행일만 f49 / 섹션 11 — 해결 제안 없음, 부분 근거만: oq-229(f50, 바탕 f3·f4·f8·f9), oq-230(f28 — 현행 별표 3 상위 8개 항목과 인증기관 8개 항목은 일치하나 기사 16가지와의 대응은 미확인; 오늘 50번 영역에서도 다루므로 부분 답변으로 둠), oq-231(f38·f39), oq-232(f40·f45). 관련 기존 질문: oq-186(16→8 개정 시점, 이번 미확인), oq-333(관제장치 항목 — 별표 3 8.가~라 f33 근거가 부분 관련). 메모의 새 질문 대조: U01→oq-229 하위, U08→f29·f32 로 답해 질문으로 올리지 않음, U09→oq-230·oq-186, U10→oq-064, U11→oq-254, U12→oq-231 하위, U13→oq-232, U14→oq-272 와 같아 새로 만들지 않음. U04(Farrell 독립 재현)·U06(Jafari 표 VI·VII 정밀도·재현율 산술)·U07(Tartu 장기 운영)은 이번 검증 범위 밖이라 올리지 않음. 새 질문 4건(U02·U03·U05·U15) / 다음 실행 후보: 50. 안전 표준·인증·사고 조사(f25~f29·f36~f38), 66. 실외(f29~f35), 63. 병원·의료(f17~f20), 20. 로봇·제조사 관제 연동(f8~f11), 19. 사람·보행자 모델(f40~f47). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 로봇별 반응 시간·제동 거리·적재 하중·센서 오차가 펌웨어 변경이나 운용 조건 변화로 바뀌었을 때, 로봇 측 보호 필드와 ROP 의 구역 속도 제한·감속 시작 지점을 함께 다시 검증하는 절차나 공개 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 57. 자산·소프트웨어 수명주기 관리 | 근거: f2 | 종류: 일반
- Nav2 의 speed_limit 0(제한 없음)·source_timeout 0.0(차단 해제)과 Open-RMF 의 0 이하 속도 제한(무시) 같은 서로 다른 '0' 의미를 이종 플릿 어댑터가 올바르게 변환하는지 실행 시험으로 확인한 공개 자료나 적합성 시험 항목이 있는가? | 관련 영역: 49. 사람 근접 안전, 20. 로봇·제조사 관제 연동 | 근거: f10 | 종류: 일반
- HATA 의 임무 완료 시간 최대 26%·19% 단축을 다시 계산할 수 있도록 실험별 분모, 교착·타임아웃 실패 시행의 처리 방식, 고정된 실행 코드가 공개돼 있는가? | 관련 영역: 49. 사람 근접 안전, 25. 작업 배정 — MRTA | 근거: f16 | 종류: 일반
- 아동·휠체어 사용자·보행 보조기 사용자·시각장애인이 가려진 모퉁이나 통로 점유 상황에서 로봇을 만날 때의 감지 누락·양보 결과를 독립적으로 측정한 데이터셋이나 시험 결과가 있는가? | 관련 영역: 49. 사람 근접 안전, 60. 노동·수용성·접근성 | 근거: f47 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 10건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-05/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f2: SICK 블로그는 원문 대조로 문장을 확인했으나 저장소 규칙(6.2 항목 13)에 따라 벤더 문서만 근거라 vendor_claim: true·[추정]으로 둔다. 특정 센서·하중 조건의 응답시간 실측값은 없음
    - f49: 아마존 글 발행일(2019-04-06)은 페이지 메타데이터 기준이며 벤더 문서만 근거라 [추정]. 조끼 신호의 거리·지연·안전 등급은 여전히 미확인
    - f14: Farrell 의 CASE 2025 쪽수(pp.548–555)·날짜(2025-08-17)는 UC eScholarship 기준이며 IEEE Xplore 원문은 열지 않음. Table IV 개별 수치는 옮기지 않음
    - f15: HATA 출판판 쪽수(pp.12697–12703)는 검증 결과 기준이며 IEEE Xplore 원문은 열지 않음
    - f24: Jafari 의 ICRA 2026 발표 쪽수·DOI 미확인(arXiv 저자판 표지의 채택 표기만 확인). 메모가 부록에서 제기한 Table VI·VII 정밀도·재현율 산술 불일치(U06)는 이번 검증 범위 밖이라 확인 못 함
    - f28·f34(oq-230·oq-186): 현행 별표 3 상위 8개 항목과 인증기관 8개 항목의 일치는 확인했으나, 2023-07-28 기사의 '16가지' 가 어느 판·계층(세부 항목)에 대응하는지와 16→8 개정 시점은 이번에 확인하지 못함. ref-992 는 다시 열지 않음
    - f36·f37: ISO 목록은 iso.org 403 이라 ISS(세르비아 표준원) 미러로 확인. ISO 10218-1:2025 의 판 번호는 쓰지 않음. 표준 본문 미열람
    - f38·f39: KS B 8252 본문 미열람(목록·적용범위만). kssn.net 은 502 로 열리지 않아 e-나라표준인증 상세로 확인. 국내 병원·상업·공동주택 실내의 사람 근접 속도·거리 강제 기준은 여전히 미확인(oq-231)
    - f42: human_detection_fusion 의 변환 실패 시 좌표계 표기 문제는 코드 경로 해석이며 실제 운용 오류·상위 보정 여부는 미확인. README 의 'Standard ROS4HRI output' 은 프로젝트 자기 서술
    - f46: NavWareSet 연결 논문(IJRR 2026)의 권호는 임시(0(0))라 확정 서지로 쓰지 않음
    - 메모의 VDA 5050 '2026-03' 날짜는 명세 안에 근거가 없어 쓰지 않음(ref-031 published null 유지)
    - oq-229(위험 감소 조치 인정 조건·검증 주체)·oq-232(이종 플릿 공통 감속·정지 인터페이스)는 부분 근거만 있고 답을 찾지 못함
- 범위 경계 위반 의심:
    - f2·f6·f7: 안전 레이저 스캐너 응답시간과 Nav2 Collision Monitor·Speed Filter 는 로봇 측 안전·로컬 회피 기능(연계 대상)이며, ROP 몫은 그 의미를 어댑터 계약에 반영하는 데로 한정
    - f25~f35: 실외이동로봇 운행안전인증 법령·고시는 59. 법·규제·보험·라이선스, 50. 안전 표준·인증·사고 조사, 66. 실외와 겹치므로 이 영역에는 사람 근접 감속·정지·속도 기준 근거로만 씀
    - f36~f39: 표준 목록 정보는 50. 안전 표준·인증·사고 조사 쪽 내용이며, 이 영역에는 사람 근접 요구의 적용 범위 확인용으로만 씀
    - f40~f43: 사람 검출·추적 모듈은 19. 사람·보행자 모델 쪽 기술이며, 이 영역에는 사람 위치를 감속·정지로 연결하는 인터페이스 근거로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1466~ref-1475, 예약 구간 ref-1466~ref-1495 안), 재사용 11건(ref-1075·ref-031·ref-1464·ref-1082·ref-1083·ref-869·ref-1081·ref-1085·ref-1080·ref-980·ref-992). 출처 매핑(검증 결과 기준): 메모 n1→ref-1075(NIST 공개 PDF 로 열람), n2→ref-1466(벤더), n3→ref-031(3.0.0 태그), n4→ref-1467(Collision Monitor 문서 페이지; H10 은 기존 ref-1077 내용이라 이번 출처에서 뺌), n5→ref-1468, n6→ref-1464(오늘 48번 영역에서 등록), n7→ref-1082, n8→ref-1083, n9→ref-869, n10→ref-1081, n11→ref-1085, n12→ref-1469(산업통상부 게시글 대신 국가법령정보센터 고시 본문·별표 3), n13→ref-1470, n14→ref-1117(H30 기존 내용 확인만, finding 없어 sources 에서 뺌), n15→ref-1471, n16→ref-1473(standard.go.kr), n17→ref-1080, n18→ref-1474, n19→ref-1475, n20→ref-1472. 추가 재사용: ref-980(8개 항목 대조), ref-992(2023 기사 수치 비교, 이번 미열람). 교차 확인 0건 — 모든 [사실] finding 이 단일 출처이거나 같은 제도·프로젝트 계열(고시·시행규칙·인증기관은 같은 운행안전인증 체계, 코드·README 는 같은 저장소). 중복 제거: 메모 H01(NIST 0.113 s)·H02(ZR·ZS)·H06·H07(maximumSpeed m/s·진입 시 도달)·H08·H09(zoneSetId·enableZoneSet)·H10(Nav2 인증 미제공)·H19(Tartu 혈액 운반)·H30(ISO/FDIS 13482 50.20)·H34(아마존 조끼 동작)는 기존 위키에 있어 새 finding 으로 넣지 않고 위치만 rationale 에 적었다. 검증 반영: H03·H34 벤더 주장 [추정] 유지, H21·H22 로 본문 89행 정정(f20), Farrell 정량 미확인 문장 정정(f14), Jafari 참가자 정정(f24), 아마존 발행일(f49), NIST 연도(f1), 고시 표기 '제2025-21호' 통일, 메모가 '별표 미열람'으로 남긴 질량별 속도·횡단 조건은 별표 3 원문으로 확인(f29~f33), H36 의 좌표계 문제는 [추정] 시사점(f42), n18 'KIRO' 는 EU ARISE 실험명(f43), ISO 목록은 ISS 근거로 판 번호 없이(f36·f37). 현장 유형: 물류창고(f12~f14·f49), 병원(f17~f20), 실외(f25~f35). 국내 자료: 시행규칙(ref-1470)·고시(ref-1469)·KS(ref-1473)·인증기관(ref-980). 열린 질문 해결 제안 없음 — 부분 근거만: oq-229(f50), oq-230(f28, 오늘 50번 영역에서도 다룸), oq-231(f38·f39), oq-232(f40·f45). 메모의 새 질문 중 U01·U08~U14 는 기존 oq 와 같거나 이번 finding 으로 답해 새로 만들지 않았고, U02·U03·U05·U15 는 docs/open-questions.md 에 같은 질문이 없어 새로 올린다(U04·U06·U07 은 검증 범위 밖이라 보류). 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 원문 절·조항과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
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

### runs/2026-09-30-15/research.md

```markdown
# 리서치 브리프 2026-09-30-15

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-15 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 50. 안전 표준·인증·사고 조사 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 조화 표준·적합성 추정, 협동 적용, 로봇 분류(ISO 10218:2025), 윤리적 블랙박스, 잠금·표지(LOTO), 중상 보고(SIR) 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 제조 공장·물류창고 사고 사례, 실외 법정 인증, 가정 모의 사고 조사 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 표준 적합성 경로(제조사·통합자·사용자), 사고 기록 장치, 증언·기록 결합 조사 절차 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218-1/-2:2025, ISO/FDIS 13482, ANSI/A3 R15.08, 실외이동로봇 운행안전인증 고시, KS B 7317 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-170, oq-186, oq-230 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
2. 산업용·이동·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482, ANSI/A3 R15.08)은 최근 어떻게 개정되었고 제조사·통합자·사용자에게 무엇을 요구하는가? (섹션 4·7 겨냥, oq-170)
3. 한국에서 로봇에 적용되는 법정 인증·KS 표준(실외이동로봇 운행안전인증, 협동로봇 관련 기준, 이동로봇 승강기 탑승 KS)은 무엇이며 심사 항목은 무엇인가? (섹션 5·7 겨냥, oq-186, oq-230, 한국 자료 우선)
4. 로봇 사고·아차 사고를 기록하고 원인을 조사하는 방법(사고 기록 장치, 조사 절차)에 관한 연구는 무엇을 제안하는가? (섹션 6·8 겨냥)
5. 실제 로봇 사고 통계와 사례는 어떤 작업·상황에서 사고가 나는지, 조사 자료에 어떤 한계가 있는지 보여 주는가? (섹션 3·5 겨냥, 제조 공장·물류창고·가정·실외·기타)
6. 안전 표준·인증·사고 조사에서 ROP가 직접 맡을 것과 제조사·통합자·인증기관·조사 기관에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ISO 10218-1:2025(산업용 로봇 설계·제조, 제조사 대상)와 ISO 10218-2:2025(로봇 적용·로봇 셀 설계·통합, 통합자 대상)는 2025년 2월 발행된 2011년판 이후 첫 개정으로, 별도 기술 사양이던 ISO/TS 15066 의 협동 적용 요구와 수동 적재·하역 및 말단 장치 관련 기술 보고서 내용을 본문에 합치고, 기능 안전 요구를 명시화하며, 새 로봇 분류와 사이버보안 요구를 더했다. | ref-1225, ref-1226 | 예 | medium | 2025-02 | — | — |
| f2 | [사실] | EN ISO 10218-1/-2:2025 의 참조가 2026-09-07 EU 관보에 (EU) 2026/2015 시행 결정으로 게재되어 기계류 지침 2006/42/EC 의 필수 안전보건 요구에 대한 적합성 추정을 주게 되었고, 개정판은 안전 관련 제어 기능에 일률적으로 요구하던 PL d·범주 3 대신 표의 기본 성능 수준 적용 또는 위험성평가 근거 선택을 허용하며, 교대 종료 같은 운전 정지용 정상 정지 기능을 새로 요구한다. | ref-1226 | 아니오 | medium | 2026-09-18 | — | — |
| f3 | [사실] | 서비스 로봇 안전 표준 ISO 13482 는 개정판 ISO/FDIS 13482 가 2026-09-15 기준 단계 50.20(FDIS 투표 개시)에 있어 ISO 13482:2014 를 대체할 예정이며, 개인·전문(상업) 용도 서비스 로봇의 물리적 접촉 위험과 기능 안전을 다루고 산업용·의료용 로봇은 적용 범위에서 제외한다. | ref-1227 | 아니오 | medium | 2026-09-15 | — | — |
| f4 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동로봇 시스템을 특정 적용·현장에 배치할 때 위험성평가는 통합자가 하고, 제조사와 통합자는 사용자에게 사용 정보를 주며, 교육과 안전 작업 절차는 사용자 책임이고, 사용자가 시스템을 개조하면 제조사·통합자 역할을 떠맡는다고 정한다. | ref-1084 | 아니오 | medium | 2023-10-26 | 수행 자원 | 원문 미열람 |
| f5 | [사실] | 연계 대상: 한국로봇산업진흥원이 맡는 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2 에 근거한 인증으로, 최대 질량 500kg·최고 속도 15km/h 이하 로봇을 대상으로 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 심사항목을 두고 인증 처리기간을 신청일로부터 30일 이내로 안내한다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | — |
| f6 | [사실] | 연계 대상: 실외이동로봇 운행안전인증의 절차와 기준은 산업통상자원부 고시 제2023-211호 '실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시'(2023-11-17)로 정해졌고, 이 고시는 지능형로봇법(법률 제19412호) 개정 시행에 따라 제정되었으며 별표에서 로봇 모델 구분, 최고속도, 최대폭, 최대질량, 운행안전성 기준을 다룬다. | ref-1230 | 아니오 | medium | 2023-11-17 | 실외 / 제약 | — |
| f7 | [사실] | 연계 대상: 고시 행정예고 단계의 보도(ZDNet Korea 2023-07-28)는 운행안전 기준을 16가지로 전하며, 질량별 속도 제한(230kg 초과 5km/h, 100kg 초과 10km/h), 폭 80cm 이하(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정 주행, 비상정지, 장애물 회피, 알림음 55~73dB, 등화장치 표면 온도 60도 이하, 방수 IPX4 이상을 예로 들어, 진흥원 페이지의 8개 심사항목(f5)과 항목 수가 다르다. | ref-992, ref-991 | 아니오 | low | 2023-07-28 | 실외 / 제약 | — |
| f8 | [사실] | 국가기술표준원은 2021-11-11 행정안전부와 협력해 실내 배송 로봇처럼 층간 이동에 승강기를 타는 로봇을 위한 KS B 7317 '이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법'을 제정했고, 이 표준은 속도 제어, 위험 상황의 보호 정지, 높낮이 차·틈새 극복, 추락·넘어짐 방지를 다룬다. | ref-945 | 아니오 | medium | 2021-11-11 | 제약 | — |
| f9 | [의견] | Winfield 외(2020)는 산업용 로봇과 달리 사람 사이에서 움직이는 사회적 로봇의 사고는 항공·철도 사고 조사와 같은 엄격함으로 조사되어야 하며, 사고 조사 없는 사회적 로봇 개발은 항공 사고 조사 없는 항공만큼 무책임하다고 주장했다. | ref-1232 | 아니오 | medium | 2020-05 | — | — |
| f10 | [사실] | Winfield·van Maris·Salvini·Jirotka(2022)는 사회적 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고·아차 사고 조사를 돕는 장치 또는 소프트웨어 모듈인 윤리적 블랙박스(EBB)의 공개 표준 초안을 항공기 비행기록장치를 본떠 제안했고, 이를 논의용 첫 초안으로 내놓았다. | ref-1233 | 아니오 | medium | 2022-05-13 | 예외·성과 | — |
| f11 | [사실] | 가정 사례(모의): Webb 외(2021)는 사고 조사를 목격자 증언, 윤리적 블랙박스 기록, 해당 환경·로봇 전문가 분석, 기술·조직 권고로 구성하고, 지원 주거 아파트에서 넘어진 거주자 곁의 보조 로봇이 오작동해 직원에게 알리지 못하고 인터넷에도 연결되지 않은 모의 사고를 역할극 증언 면담으로 조사해 방법을 시험했다. | ref-1234 | 아니오 | medium | 2021-06-29 | 가정 / 예외·성과 | — |
| f12 | [사실] | Sanders·Sener·Chen(Applied Ergonomics 121, 2024)은 미국 OSHA 중상 보고(SIR)에서 2015~2022년 로봇 관련 사고 77건을 찾아, 고정형 로봇 54건(부상 66건, 주로 손가락 절단과 머리·몸통 골절)과 이동로봇 23건(부상 27건, 주로 다리·발 골절)으로 나누었고, 보고서 서술이 더 구조화되고 상세해야 한다고 결론지었다. | ref-1235 | 아니오 | medium | 2024 | 예외·성과 | — |
| f13 | [사실] | 제조 공장 사례: 서울신문(2017-04-07)이 보도한 안전보건공단 산업안전보건연구원 조사에 따르면 2011~2015년 국내 산업용 로봇 재해자는 207명(사망 15명)이고, 그중 134명(64.7%)이 수리·점검·준비·설치 작업 중에, 90.7%가 방책 안에서 다쳤으며, 평균 근로손실일수는 707.5일로 제조업 평균 351.7일의 약 두 배였다. | ref-1236 | 아니오 | low | 2017-04-07 | 제조 공장 / 예외·성과 | — |
| f14 | [사실] | 물류창고 사례: 2023-11-07 경남 고성의 농산물유통센터에서 파프리카 상자를 선별해 팔레트로 옮기는(출하 단계) 산업용 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌고, 경찰은 로봇이 사람을 상자로 인식한 것으로 보고 안전관리 책임자의 과실 여부를 수사했다. | ref-1237 | 아니오 | low | 2023-11-08 | 물류창고 / 예외·성과 | — |
| f15 | [사실] | 제조 공장 사례: 2026-09-21 경남 고성의 식품 제조 공장에서 멈춘 제품 적재용 로봇을 점검하던 노동자가 끼여 2026-09-25 숨졌으며, 보도에 따르면 전원 차단·기동스위치 잠금·표지(LOTO)와 재가동 전 안전 확인 절차가 없었고, 고용노동부 통영지청은 산업안전보건법·중대재해처벌법 위반을, 경찰은 임의 재가동·기계 오작동 여부를 조사 중이다. | ref-1238 | 아니오 | low | 2026-09-29 | 제조 공장 / 예외·성과 | — |
| f16 | [사실] | 기타(건설 현장) 사례: Belzile 외(2025)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토하고 이동로봇 전용이면서 다양한 배치 상황에 적용할 수 있는 표준은 없으며 이동 플랫폼의 위험성평가 문헌도 제한적이라고 보고, 건설 현장 이동로봇 배치용 위험성평가 틀을 제안했다. | ref-563 | 아니오 | medium | 2025-02-28 | 기타 / 제약 | — |
| f17 | [추정] | 확인한 자료를 종합하면 핵심 질문(어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가)에 대해, 따를 표준·인증은 로봇 유형(산업용 ISO 10218, 이동 R15.08, 서비스 ISO 13482)과 현장·국가 조건(한국 실외 보도 운행 법정 인증, 승강기 탑승 KS B 7317)에 따라 갈리고 주요 표준이 2025~2026년 개정 중이며, 사고 원인 규명은 비행기록장치식 기록과 증언을 결합하는 방법이 연구 단계로 제안되었지만 현행 보고 자료는 서술이 구조화되지 않아 원인 분석에 한계가 있는 것으로 보인다. | ref-1225, ref-1226, ref-1227, ref-1084, ref-980, ref-945, ref-1233, ref-1234, ref-1235 | 아니오 | low | 2026-09-30 | — | — |
| f18 | [추정] | 확인한 사고 자료(f12~f15)는 로봇 관련 중대 사고가 정상 운전보다 점검·수리·프로그램 수정·재가동 같은 비정상 작업 중에, 방책 안에서, 재가동 확인 절차가 없을 때 주로 일어났음을 보여 주므로, 여러 로봇을 지휘하는 플랫폼에서는 정비·점검 상태와 재가동 명령의 권한·확인 이력을 남기는 것이 예방과 사후 조사 모두에 필요할 것으로 보인다. | ref-1236, ref-1237, ref-1238, ref-1235 | 아니오 | low | 2026-09-30 | 예외·성과 | — |
| f19 | [추정] | 확인한 자료를 종합하면 50. 안전 표준·인증·사고 조사에서 ROP가 직접 맡을 범위는 로봇·적용마다 인증 상태, 적용 표준과 판, 인증이 허용한 운행 조건(질량·속도·구역)을 등록 정보로 관리해 배정·경로 제약에 반영하는 일, 정지·재가동·정비 모드 전환 명령과 로봇 상태 보고를 사고 조사에 쓸 수 있게 보존하는 플릿 수준 실행 기록, 표준 판 개정을 추적하는 일로 보인다. | ref-980, ref-1226, ref-1233, ref-1235 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 본체의 표준 적합성과 제품 인증은 제조사와 인증기관이, 로봇 셀·이동로봇 적용의 위험성평가와 사용 정보는 통합자가, 교육·작업 절차·잠금·표지는 사용자 사업장이, 실외 운행 인증과 보험은 운영자와 진흥원이, 법정 사고 조사는 고용노동부·경찰이 맡으므로, ROP는 그 결과와 조사에 필요한 실행 기록을 주고받는 인터페이스를 맡는 것으로 보인다. | ref-1225, ref-1084, ref-980, ref-991, ref-1238 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f21 | [추정] | 이 영역은 위험성평가·정지 절차의 48. 안전·위험 관리(f4·f15), 협동 적용·분리 거리의 49. 사람 근접 안전(f1), 인증 속성을 등록하는 4. 이기종 로봇 등록(f5), 승강기 탑승 기준의 22. 설비·건물 시스템 연동(f8), 사고 조사용 기록의 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석(f10~f12), 재가동 권한의 51. 인증·권한·격리(f15), 사이버보안 요구의 52. 통신 보호·위협 관리·감사(f1), 시험·인증 절차의 54. 시험·형식 검증·벤치마크, 현장 위험성평가의 55. 현장 조사·설치·시운전(f16), 표준 판 추적의 57. 자산·소프트웨어 수명주기 관리(f2·f3), 책임 분담의 58. 다사업자 책임·계약·데이터(f4), 법정 인증·보험·조사의 59. 법·규제·보험·라이선스(f5~f7·f15), 적용 현장인 61. 물류창고(f14)·62. 제조 공장(f13·f15)·65. 가정·공동주택(f11)·66. 실외(f5~f7)·67. 기타 현장(f16)과 이어진다. | ref-1084, ref-1238, ref-1225, ref-980, ref-945, ref-1233, ref-1234, ref-1235, ref-563, ref-1226, ref-1227, ref-1230, ref-992, ref-1237, ref-1236 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1225 | The Robot Report | ISO 10218 industrial robot safety standard receives major overhaul | 2025-02 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/iso-10218-industrial-robot-safety-standard-receives-major-overhaul/ | 아니오 |
| ref-1226 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-09-30 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 아니오 |
| ref-1227 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | 표준 | medium | 2026-09-30 | https://iss.rs/en/project/show/iso:proj:83498 | 아니오 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-992 | ZDNet Korea | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사 | 2023-07-28 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1230 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | high | 2026-09-30 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 아니오 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-30 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 아니오 |
| ref-1232 | Winfield, A. F. T., Winkle, K., Webb, H., Lyngs, U., Jirotka, M., & Macrae, C. (arXiv) | Robot Accident Investigation: a case study in Responsible Robotics | 2020-05 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2005.07474 | 아니오 |
| ref-1233 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2205.06564 | 아니오 |
| ref-1234 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 아니오 |
| ref-1235 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-09-30 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 아니오 |
| ref-1236 | 서울신문 | [단독] 산업용 로봇 재해 위험 제조업보다 두 배 ... (제목 일부만 확인) | 2017-04-07 | 기사 | low | 2026-09-30 | https://www.seoul.co.kr/news/society/2017/04/07/20170407011011 | 아니오 |
| ref-1237 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | 기사 | low | 2026-09-30 | https://www.khan.co.kr/article/202311081103001 | 아니오 |
| ref-1238 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | 기사 | low | 2026-09-30 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 아니오 |
| ref-563 | Belzile, B., Wanang-Siyapdjie, T., Karimi, S., Braga, R. G., Iordanova, I., & St-Onge, D. (arXiv) | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02-28 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2502.20693 | 아니오 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | medium | 2026-09-30 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 예 |
| ref-991 | 산업통상자원부·경찰청 (대한민국 정책브리핑) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·... (제목 일부만 확인) | 2023-11-16 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/safety-standards-certification-and-incident-investigation.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f13·f12(사고가 점검·재가동 중, 방책 안에서 나고 손실이 큼), f17(핵심 질문 답, 추정) / 섹션 4: ISO 10218:2025 제조사·통합자 구분과 로봇 분류 f1, 조화 표준·적합성 추정 f2, 윤리적 블랙박스 f10, 잠금·표지(LOTO) f15, 중상 보고 f12 / 섹션 5: 제조 공장 — f13(예외·성과: 재해 통계)·f15(예외·성과: 적재 로봇 점검 중 사고, 조사 중임 명시), 물류창고 — f14(출하 단계 선별·팔레트 적재 로봇 사고), 실외 — f5·f6·f7(제약: 운행안전인증, 항목 수 출처 충돌 병기), 가정 — f11(모의 사고 조사임 명시), 기타 — f16(건설 현장). 병원·상업 시설 사례는 찾지 못함을 명시 / 섹션 6: 역할별 적합성 경로 f1·f4, 기록 장치와 증언 결합 조사 f10·f11, 비정상 작업 관리 f18(추정) / 섹션 7: ISO 10218-1/-2:2025 f1·f2, ISO/FDIS 13482 f3, ANSI/A3 R15.08-2 f4, 실외이동로봇 운행안전인증·고시 제2023-211호 f5~f7, KS B 7317 f8, EBB 초안 f10 / 섹션 8: f9~f12·f16 / 섹션 9: f19(직접 범위), f20(연계 대상) / 섹션 10: f21 — 4, 22, 37, 38, 48, 49, 51, 52, 54, 55, 57, 58, 59, 61, 62, 65, 66, 67 / 섹션 11: 기존 oq-170·oq-186·oq-230(미해결 유지, f5~f7 로 부분 근거)과 open_questions_new 4건. 다음 실행 후보: 66. 실외 페이지에 f5~f7, 22. 설비·건물 시스템 연동 페이지에 f8 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 윤리적 블랙박스 | Ethical Black Box (EBB) | 로봇의 센서·구동기·제어 결정 데이터를 안전하게 계속 기록해 사고나 아차 사고 뒤 원인 조사에 쓰도록 항공기 비행기록장치를 본떠 제안된 장치 또는 소프트웨어 모듈이다. |
| 잠금·표지 | Lockout/Tagout (LOTO) | 점검·수리 전에 설비의 동력을 차단하고 기동 장치를 잠근 뒤 다른 사람이 가동하지 못하도록 표지를 다는 작업 안전 절차다. |
| 적합성 추정 | Presumption of Conformity | EU 관보에 참조가 게재된 조화 표준을 적용한 제품은 해당 법령(예: 기계류 지침)의 필수 안전보건 요구를 충족한 것으로 추정되는 효력이다. |

## 열린 질문

새로 생긴 질문:

- 국내 KS B ISO 10218-1·-2 는 ISO 10218:2025 판을 언제 부합화하며, 산업안전보건기준에 관한 규칙의 협동로봇 방책 면제 인정 기준과 협동로봇 설치 작업장 안전인증은 새 판(로봇 분류·기능 안전 요구 변경)을 기준으로 바뀌는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 62. 제조 공장 | 근거: f1 | 종류: 일반
- 여러 제조사 로봇을 지휘하는 플랫폼 수준에서 사고·아차 사고 조사에 필요한 최소 기록 항목(명령·정지·재가동·정비 모드 전환·상태 보고)을 정한 표준이나 공개 규약이 있는가, 윤리적 블랙박스 초안을 플릿 기록에 적용한 사례가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석 | 근거: f10 | 종류: 일반
- 2016년 이후 국내 로봇 관련 산업재해 통계를 고정형 산업용 로봇과 이동로봇(AMR·AGV)으로 나누어 집계한 공식 자료가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 48. 안전·위험 관리 | 근거: f13 | 종류: 일반
- ISO/FDIS 13482 개정판은 여러 대가 함께 운영되는 서비스 로봇의 플릿 관제·승강기 연동·소프트웨어 갱신에 관한 안전 요구를 포함하는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 64. 상업 시설, 63. 병원·의료 | 근거: f3 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 1
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - oq-170 미해결: ISO 3691-4:2023 원문·ISO 페이지·iTeh 카탈로그가 열리지 않거나 본문이 없어 운용 구역 요구를 표준 원문으로 확인하지 못함(검색 요약의 제3자 블로그 설명은 넣지 않음)
    - oq-186·oq-230 미해결: 진흥원 페이지는 8개 심사항목, 행정예고 보도와 정책브리핑은 16가지 항목으로 전하며, 8개가 16개를 묶은 상위 항목인지 개정인지 고시 별표 원문으로 확인하지 못함. 근거 고시는 제2023-211호로 확인(f6)
    - f5 인증 처리기간: 진흥원 페이지는 30일 이내, 검색 요약 한 곳은 60일로 달라 페이지 값만 기재
    - f10 EBB 초안의 데이터 항목·형식·보존 기간: arXiv PDF 본문 추출 실패로 초록 범위만 기재
    - f12 OSHA SIR 분석: 출판사 페이지 403, 기관 저장소의 초록만 확인
    - f13 산업안전보건연구원 보고서 원문 미확인(기사 재인용), 끼임·부딪힘 비율은 기사에 없어 넣지 않음
    - f15 2026-09 고성 사고는 조사 진행 중이며 원인 확정 아님
    - ISO 10218:2025 의 '협동 적용' 용어 전환과 ANSI/A3 R15.06-2025·R15.08-3-2026 발간은 검색 요약에만 있어 넣지 않음(A3·ANSI 블로그 403)
    - 산업안전보건기준에 관한 규칙 제223조 단서와 협동로봇 설치 작업장 안전인증 기관: 법제처 원문이 열리지 않았고 인증기관을 한국로봇사용자협회로 적은 자료와 한국로봇산업진흥원으로 적은 기사가 달라 넣지 않음
    - KS B 7317 2025-05-09 개정 여부는 검색 요약에만 있어 넣지 않음
    - EU 기계류 규정 2023/1230 전환과 ISO 10218:2025 의 관계는 조사하지 못함
    - 병원·상업 시설의 안전 인증·사고 조사 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f5·f6·f7: 실외 보도 운행 법정 인증은 원문 19장 '업종별 조건'(실외 차량 등)의 연계 대상이므로 claim 을 '연계 대상: '으로 시작함
    - f20: 로봇 본체 인증(제조사·인증기관), 적용 위험성평가(통합자), 법정 사고 조사(노동부·경찰)는 ROP 밖 주체의 일로 '연계 대상: '으로 구분함
    - f13~f15: 산업용 로봇 셀의 방호장치·LOTO 는 원문 19장 '시설·설비 제어'·설비 안전 제어에 가까우므로 사고 조사 근거로만 쓰고 ROP 직접 범위(f19)는 기록·권한 쪽으로 한정함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1225~ref-563, 예약 구간 안)로 신규 출처 상한에 도달해 ZDNet 2023-11-30(운행안전인증 심사 시작), ZDNet 2025-05-14(KS B 7317 평가 통과 사례), 한국로봇사용자협회·기사(협동로봇 설치 작업장 안전인증), CAST 핸드북(연결 끊김)을 출처로 넣지 못했다. 재사용 2건(ref-1084, ref-991): 참고문헌 전체 목록이 입력에 없어 값은 이전 브리프 2026-09-30-14 출처 표를 따랐고 이번에 다시 열지 않아 fetched: false 로 적었다. 원문 열람: 신규 15건 모두 WebFetch 로 열었으나 ref-1232·ref-1233·ref-1235 는 초록만 읽었다. ISO(10218·13482·3691-4), A3, ANSI 블로그, ScienceDirect 는 403 이었다. 교차 확인 1건(f1: The Robot Report·IBF 두 곳). 기사 근거 finding(f7·f13·f14·f15)은 low. 벤더 기능 주장 없음. 분류 원문 핵심 질문에는 f17 로 답했고 결론은 '따를 표준은 로봇 유형·현장·국가 조건에 따라 갈리고 주요 표준이 개정 중이며, 사고 원인 규명은 기록 장치와 증언을 결합하는 방법이 연구 단계이고 현행 보고 자료는 구조화가 부족하다'는 추정이다. 현장 유형 사례는 제조 공장(f13·f15)·물류창고(f14)·실외(f5~f7)·가정(f11, 모의)·기타(f16, 건설 현장)이며 병원·상업 시설은 찾지 못했다. 국내 자료는 진흥원·산업통상자원부 고시·국가기술표준원·정책브리핑(재사용)과 기사 4건이다. 기존 열린 질문 oq-170·oq-186·oq-230 은 원문 확인 실패로 해결 제안하지 않았다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding 없음(f14 의 인식 오류는 사고 사례로만 다룸). 용어집에 이미 있는 위험성평가·STPA·근본 원인 분석·운용 구역·실외이동로봇 운행안전인증·협동 적용·동력·힘 제한·속도·분리 감시는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```
