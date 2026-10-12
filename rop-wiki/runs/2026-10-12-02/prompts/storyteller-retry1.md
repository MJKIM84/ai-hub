(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-02
- date: 2026-10-12
- run_type: update (갱신)
- 대상: 59. 법·규제·보험·라이선스 (P. 거버넌스·법규·사회)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 세부영역 반영 제안: 1건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-10-12-02/target.json

```json
{
  "run_id": "2026-10-12-02",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 174,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 59,
    "area_name": "59. 법·규제·보험·라이선스",
    "category": "P. 거버넌스·법규·사회",
    "category_letter": "P"
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
  "selection_rationale": "CLI 지정 run_type=update, area=59"
}
```

### runs/2026-10-12-02/research.json

```json
{
  "run_id": "2026-10-12-02",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 59,
    "area_name": "59. 법·규제·보험·라이선스",
    "category": "P. 거버넌스·법규·사회"
  },
  "gaps": [
    "섹션 3. 왜 중요한가(분리 2026-09-30-area59-s3) — EU 개정 제조물책임지침 적용 시점·소프트웨어 포함 서술이 법률사무소 해설(ref-1227, 2026-03-23) 단독 근거의 [사실]이고, 2026-05-07 관보 정오표와 비상업 FOSS 제외가 없음",
    "섹션 4. 핵심 개념과 용어(분리 2026-09-30-area59-s4) — 고영향 인공지능 항목이 정부 발표(ref-1235)만 들고 제33조 사전 검토·제35조 영향평가의 의무 강도와 조문 판이 없음, 제조물책임 EU 부분이 해설 기준",
    "섹션 5. 적용 사례 — 한국 실외 사례에 책임보험 법정 가입금액이 없고(oq-288), '개정 시점·근거 고시 … 확인하지 못했다' 문단이 낡았으며, 버지니아 보험의 단위(합산 운행)가 불명확하고 다른 관할의 보험 의무 비교가 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area59-s6) — CRA 보고 기한의 기산점이 없고, 라이선스 소절이 ROS 2 가이드·Gazebo 규칙뿐이라 Apache 2.0 재배포 의무, 비텍스트 자산 권리 정보, SPDX 표현식 검사, 모델 가중치 라이선스가 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area59-s7) — EU AI Act 행이 없고(디지털 옴니버스 2026/1744 의 적용일·기계류 Section B 이동), 기계류 규정 행에 AI 위임법령 경로가 없으며, PLD 행이 해설 기준, CRA 행에 오픈소스 스튜어드 적용일 없음, 인공지능 기본법 행에 조문 없음",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area59-s8) — 학술 연구가 거의 없고(규제 샌드박스 비교 연구 없음), EU 제조물 책임 서술의 근거가 해설",
    "섹션 9. 책임 경계 — 규제 대장(분류 경로·적용일), 보고 기한 기산 기록, 릴리스 권리 검사 같은 ROP 직접 업무가 일반 서술에 머묾",
    "섹션 11. 열린 질문(분리 2026-09-30-area59-s11) — 새 질문 다섯 건이 id 없이 '(새 질문)'으로만 표기되고 oq-288 이 미해결",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: PLD 근거 교체(날짜는 유지), 16→8 문단의 '확인하지 못했다', 버지니아 보험 단위"
  ],
  "research_questions": [
    "이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]",
    "EU AI Act 디지털 옴니버스(Regulation (EU) 2026/1744)는 고위험 AI 적용일과 기계류 로봇의 AI 요구 경로를 어떻게 바꿨는가(oq-106, oq-143)? (섹션 7 겨냥)",
    "국내 인공지능 기본법 제33·35조는 고영향 여부 검토와 영향평가를 어떤 강도의 의무로 정하며, 열람한 판과 법 최초 시행일은 어떻게 구분되는가(oq-143)? (섹션 4·7 겨냥)",
    "oq-288 한국 실외이동로봇 책임보험·공제의 최저 가입금액을 정한 조항과 금액은 무엇이며, 다른 관할(버지니아·홍콩)의 보험 의무는 어떤 단위로 정해지는가? (섹션 5 겨냥)",
    "EU 사이버복원력법 보고 기한의 기산점과 오픈소스 스튜어드·기여자의 적용 범위·시점은 무엇인가(oq-291)? (섹션 6·7 겨냥)",
    "EU 개정 제조물책임지침의 적용 시점·제품 정의·오픈소스 제외는 관보 원문과 정오표로 무엇인가(oq-289)? (섹션 3·7 겨냥)",
    "Apache 2.0 재배포 의무, 비텍스트 자산의 권리 정보, SPDX 표현식 검사, 모델 가중치 라이선스는 무엇을 요구하는가(oq-292)? (섹션 6·7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "규정 (EU) 2026/1744(Digital Omnibus on AI, 2026-07-08 채택, 관보 OJ L 2026/1744 2026-07-24 게재)은 제4조에서 관보 게재 후 셋째 날 발효한다고 정해 2026-07-27 발효했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "머리말 'of 8 July 2026', 'OJ L, 24.7.2026'; 제4조 'shall enter into force on the third day following that of its publication'. 기존 2026-10-09-area43-s10.md 44행의 로펌 글(ref-1322) 기반 서술을 1차 원문으로 보강",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "2026/1744 제1조(40)(b)로 바뀐 AI Act 제113조 셋째 문단 (c)는 제III장 제1·2·3절(제6조5항 제외)을 제6조2항·부속서 III 에 따른 고위험 AI 에는 2027-12-02 부터 적용하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제1조(40)(b), 35쪽: '(i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III', 'with the exception of Article 6(5)'. 모든 AI 의무의 유예가 아님. area43-s10 44행(ref-1322)과 같은 날짜, 근거 상향",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "같은 조항은 제6조1항·부속서 I 에 따른 고위험 AI 에는 제III장 제1·2·3절을 2028-08-02 부터 적용하게 하고, 새 (d)호로 제102~110조를 2026-07-27 부터 적용하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제1조(40)(b)(ii) '2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I'; (c) '(d) Articles 102 to 110 shall apply from 27 July 2026'. 기계류에 대한 실제 적용 범위는 f4·f5 와 함께 읽음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "2026/1744 제1조(41)은 AI Act 부속서 I Section A 1번(기계류 지침 2006/42/EC)을 삭제하고 Section B 에 21번으로 기계규정 (EU) 2023/1230 을 추가해, 기계류를 부속서 I Section A 에서 Section B 로 옮겼다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제1조(41) '(a) in Section A, point 1 is deleted; (b) in Section B, the following point is added: 21. Regulation (EU) 2023/1230'. 전문 (42) 'moving Regulation (EU) 2023/1230 from Section A to Section B of Annex I'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "2026/1744 제1조(2)(a)로 바뀐 AI Act 제2조2항은 부속서 I Section B 법령 대상 제품과 관련해 제6조1항으로 고위험이 되는 AI 에는 제6조1항, 제60a조, 제102~112조만 적용하고, 제57~59조는 그 법령에 고위험 AI 요구가 통합된 범위에서만 적용한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제1조(2)(a): 'only Article 6(1), Article 60a and Articles 102 to 112 shall apply. Articles 57, 58 and 59 shall apply only in so far as the requirements … have been integrated in that Union harmonisation legislation.'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "따라서 기계규정 대상 로봇(기계류)에 안전 구성요소로 들어가거나 그 자체가 기계류인 고위험 AI 에는 AI Act 제III장 제2절 요구(제12조 기록 등)와 제공자 의무가 2028-08-02 에 직접 적용되는 것이 아니라 기계규정 부속서 III 을 거쳐 반영되는 구조로 보이며, '기계류 등 부속서 I 제품에 내장된 경우라면 적용 시점은 2028-08-02' 라는 기존 위키 서술은 이 구조를 반영하지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f3·f4·f5·f7 조합 해석. 전문 (42) 'the application of Regulation (EU) 2024/1689 to those machines should be limited to the provisions referred to in Article 2(2)'. 기존 서술: 2026-10-09-area43-s10.md 45행, safety/index.md 149행, ai-and-learning/index.md 131행. 개별 제품의 해당성은 판단하지 않음(oq-106·oq-316)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "2026/1744 제3조(1)은 기계규정 제8조에 문단을 더해, 위원회가 제47조에 따른 위임법령으로 기계규정 부속서 III 을 개정해 AI Act 제6조1항 고위험 AI(기계규정 대상 제품의 안전 구성요소이거나 그 자체가 대상 제품인 것)의 보건·안전 요구를 추가하게 하며, 그 요구는 AI Act 제III장 제2절과 제17·19·72·73조를 반영해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제3조(1), 39쪽: 'The Commission shall adopt delegated acts … to amend Annex III to this Regulation by adding health and safety requirements … Chapter III, Section 2, and Articles 17, 19, 72 and 73 … are reflected.' 위임법령 번호는 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "같은 조항은 그 위임법령이 2028-08-02 까지 적용되도록 정하고, 제3조(3)으로 바뀐 기계규정 제47조2항은 제8조 셋째 문단의 위임 권한을 2026-07-27 부터 5년으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제3조(1), 40쪽 'Those delegated acts shall apply by 2 August 2028'; 제3조(3)(a) 'Article 8, third paragraph, … for a period of five years from 27 July 2026'. 기계규정 일반 적용일(2027-01-20)을 바꾸는 조항이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "2026/1744 제3조(2)로 기계규정 제20조에 추가된 제10항은 기계규정에 따른 AI 조화 표준·공통 사양이 나오기 전까지 AI Act 제40·41조의 조화 표준·공통 사양을 준수한 고위험 AI 를 기계규정 부속서 III 의 AI 관련 보건·안전 요구에 적합한 것으로 추정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제3조(2), 40쪽: 'Until harmonised standards or common specifications are referenced or adopted pursuant to this Article as regards high-risk AI systems, … shall be presumed to be in conformity with the essential health and safety requirements set out in Annex III'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "ROP 규제 대장은 AI Act 적용을 하나의 날짜로 묶지 말고 관할, 분류 경로(부속서 III / 부속서 I Section A / Section B), 근거 조항, 적용일을 따로 기록하고, 기계류 로봇의 AI 요구는 기계규정 제8조 위임법령 채택을 별도 추적 항목으로 둬야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2~f9 에서 도출(구축자 의견). 특정 ROP 기능의 법적 해당성은 판정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "인공지능기본법 제33조1항은 인공지능사업자가 AI 또는 이를 이용한 제품·서비스를 제공할 때 그 AI 가 고영향 인공지능에 해당하는지 사전에 검토하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제33조①: '고영향 인공지능에 해당하는지에 대하여 사전에 검토하여야 하며'. 열람한 판: 법률 제21311호. ROP 특정 기능의 해당성 판정 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "같은 항은 필요한 경우 과학기술정보통신부장관에게 고영향 해당 여부의 확인을 요청할 수 있게 하고(재량), 제2항은 요청이 있으면 장관이 해당 여부를 확인하도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제33조① '확인을 요청할 수 있다', ② '해당 여부를 확인하여야 하며'. 확인 요청은 모든 사업자의 사전 승인 의무가 아님. ③ 가이드라인, ④ 절차는 대통령령(시행령 미확인)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "인공지능기본법 제35조1항은 고영향 AI 를 이용한 제품·서비스를 제공하는 인공지능사업자가 사전에 사람의 기본권에 미치는 영향을 평가하기 위해 노력하도록 정한 노력의무이며, 제2항은 국가기관등이 영향평가를 실시한 제품·서비스를 우선 고려하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제35조① '영향을 평가(이하 \"영향평가\"라 한다)하기 위하여 노력하여야 한다', ② '우선적으로 고려하여야 한다'. 평가 실시를 보장하는 의무로 넓히지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "열람한 조문 판은 법률 제21311호(2026-01-20 일부개정, 2026-07-21 시행)이지만 제33조에는 개정 표시가 없고 제35조1항에는 '<개정 2026. 1. 20.>' 표시만 있어, 두 조의 의무는 이 개정으로 새로 생긴 것이 아니라 법 최초 시행(2026-01-22)부터 있던 것이며 '시행 2026-07-21' 은 두 조의 발효일이 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1518",
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "law.go.kr 화면 '[시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정]'. 법 시행일 2026-01-22 는 정부 발표(ref-1235). 원판 ref-620(lsiSeq=268543)은 이번에도 열지 않음. 제35조①의 개정 대상 문장은 대비표 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "ROP 운영 준비에는 고영향 해당성 사전 검토, 장관 확인 요청 여부, 영향평가 노력의 기록을 별도 업무로 두고, '사람이 최종 결정하면 고영향에서 제외' 라는 정부 설명만으로 모든 ROP 기능을 면제 처리하지 않아야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1518",
        "ref-1235"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f11~f14 와 기존 oq-143 근거(ref-1235)에서 도출(구축자 의견)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "산업통상부 공고 제2025-042호(2025-11-06) 행정예고 첨부안은 개정 이유를 인증 절차 간소화로 들고 심사결과 통보 기한 30일 이내 명시(안 제9조)와 심사항목 기준의 통·폐합에 따른 16개→8개 축소(안 별표 3)를 담았으며, 이 개정은 산업통상부고시 제2025-21호로 2025-11-24 발령·시행됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1519",
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "첨부 hwpx '심사항목 기준의 통·폐합에 따른 심사항목 축소(16개→8개)(안 별표3)', '통보 기한 명시(30일 이내)(안 제9조)'; 국가법령정보센터 '[시행 2025. 11. 24.] [산업통상부고시 제2025-21호]'. 시점·별표 대응은 기존 내용 확인(2026-10-11-area50-s7·s11, area49-s7·s11)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "현행 고시(제2025-21호) 제8조1항2호는 운행안전인증을 받은 실외이동로봇 또는 해당 관제장치의 일부를 변경해 신규 인증이나 법 제40조의2제3항의 변경인증을 받으려는 경우 인증기관장이 심사의 일부 또는 전부를 면제할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1469"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제8조①2호 '운행안전인증을 받은 실외이동로봇 또는 해당 관제장치의 일부를 변경하여 … 변경인증을 받고자 하는 경우'. 오케스트레이션 계층이 인증상 관제장치인지에 대한 해석은 없음(oq-187 부분 근거)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "지능형로봇법 시행규칙 제7조의10제1항(법 제40조의4·영 제24조의3제3항 근거)은 실외이동로봇 사고배상 책임보험·공제의 보험금 기준을 사망 1인당 1억5천만원으로 정하고, 실손해액이 2천만원 미만이면 2천만원으로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제7조의10①1호 '사망한 경우에는 1인당 1억5천만원. 다만, 실손해액이 2천만원 미만인 경우에는 2천만원으로 한다'. ① 단서: 지급 보험금은 1호 단서 외에는 실손해액을 넘을 수 없음. 현행 통합본(산업통상부령 제1호, 2025-10-01 시행)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "같은 항 제2호는 부상의 보험금 기준을 1인당 3천만원으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제7조의10①2호 '부상당한 경우에는 1인당 3천만원'. 법령 기준 금액이며 실제 보험약관·보험료 수치가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "같은 항 제3호는 치료를 마친 뒤 증상이 고정된 상태에서 부상이 원인이 된 신체 장애(후유장애)의 보험금 기준을 1인당 1억5천만원으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제7조의10①3호 '… 후유장애 … 1인당 1억5천만원'. ②는 한 사건이 사망·부상·후유장애 중 둘 이상에 해당할 때 실손해액 안에서 금액을 더하는 방식을 정함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "같은 항 제4호는 재물이 멸실되거나 훼손된 경우의 보험금 기준을 사고당 10억원으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제7조의10①4호 '재물이 멸실되거나 훼손된 경우에는 사고당 10억원'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "제7조의10은 2023-11-17 신설된 조문이며, 현행 통합본(산업통상부령 제1호, 2025-10-01 시행)에도 같은 금액과 '[본조신설 2023. 11. 17.]' 표시만 있어 신설 뒤 개정되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "현행 통합본 화면 '[시행 2025. 10. 1.] [산업통상부령 제1호, 2025. 10. 1., 타법개정]', 제7조의10 끝 '[본조신설 2023. 11. 17.]', 개정 표시 없음. 같은 시행규칙의 제7조의4·5 는 기존 ref-1470",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "ROP 의 보험 상태 관리는 법령 기준 금액(시행규칙 제7조의10)과 실제 보험 상품의 보장·면책·자기부담금·가입 기간, 협회 단체보험의 보험료를 서로 다른 지표로 기록해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18~f22 에서 도출(구축자 의견). 기존 위키의 단체보험 보험료 30만원대(ref-1232)는 가입금액과 다른 지표",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "버지니아주법 §46.2-908.1:1 E항의 최소 10만 달러 일반배상책임 보험은 운영자 통제 아래 있는 개인 배송 장치들의 합산 운행(combined operations)으로 생긴 손해를 대상으로 하며, 장치당 한도로 정하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1238"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§E: 'combined operations of personal delivery devices under a personal delivery device operator's control'. 현행 표시 조문 기준. 기존 위키 5절 버지니아 '제약' 행(s7 버지니아 행)의 보험 문장을 정밀화",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "홍콩 정부는 2026-05-20 입법회 서면 답변(LCQ20)에서 사적·상업적 목적의 지능형 로봇 사용에 제3자 책임보험 가입을 강제하는 법적 요건이 당시 홍콩에 없다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1521"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Reply: 'currently there is no statutory requirement in Hong Kong mandating the purchase of third party liability insurance for using intelligent robots for private or commercial purposes'. 질문자의 사고 주장은 사실로 채택하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "ROP 의 보험 확인 규칙은 국가 이름 하나가 아니라 관할, 운영자, 플릿(합산 운행) 단위, 적용 시점으로 구성해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1238",
        "ref-1521",
        "ref-1520"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f18·f24·f25 에서 도출(구축자 의견)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "사이버복원력법(CRA) 제14조2항 (a)(b)는 실제 악용 취약점의 조기 경보(24시간)와 취약점 통지(72시간)의 기산점을 제조자가 그 취약점을 인지한 때로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1522"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제14조②(a) 'within 24 hours of the manufacturer becoming aware of it', (b) 'within 72 hours of the manufacturer becoming aware'. 24h·72h 자체는 기존 내용(area59-s6, glossary/cyber-resilience-act.md), 이번에는 기산점만 보탬",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "같은 항 (c)는 실제 악용 취약점의 최종 보고 기한을 최초 인지가 아니라 시정·완화 조치가 이용 가능해진 뒤 14일 이내로 정한다(관련 정보가 이미 제공된 경우 제외).",
      "tag": "사실",
      "source_ids": [
        "ref-1522"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제14조②(c) 'no later than 14 days after a corrective or mitigating measure is available'",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "CRA 제14조4항 (c)는 중대한 보안 사고의 최종 보고를 (b)의 사고 통지 제출 뒤 1개월 이내로 정해, 취약점 최종 보고와 기산점이 다르다.",
      "tag": "사실",
      "source_ids": [
        "ref-1522"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제14조④(c) 'within one month after the submission of the incident notification under point (b)'. 사고 조기 경보·통지도 제조자 인지 시점 기준(④(a)(b))",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "CRA 제24조3항은 오픈소스 소프트웨어 스튜어드에게 제14조1항 보고 의무를 그 제품 개발에 관여하는 범위에서 적용하며, 제71조2항에 따라 제24조는 규정의 일반 적용일인 2027-12-11 부터 적용된다(제14조만 2026-09-11 부터). ENISA 의 단일 보고 플랫폼 가동 발표(2026-09-11)도 스튜어드 보고 의무 적용일을 2027-12-11 로 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1522",
        "ref-1523"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제24조③ 'shall apply to open-source software stewards to the extent that they are involved in the development'; 제71조② 'shall apply from 11 December 2027. However, Article 14 shall apply from 11 September 2026'. ENISA 'In accordance with Article 24(3) … This article shall apply from 11 December 2027'. 플랫폼 가동 사실은 기존 내용(area59-s4·s7)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "CRA 전문 (18)은 상업 활동 과정에서 시장에 공급되는 자유·오픈소스 소프트웨어만 이 규정의 적용 대상으로 보고, 자기 책임 아래 있지 않은 자유·오픈소스 제품에 소스 코드를 기여하는 자에게는 이 규정이 적용되지 않는다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1522"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "전문 (18) 'only free and open-source software made available on the market, and therefore supplied … in the course of a commercial activity, should fall within the scope'; 'does not apply to … persons who contribute with source code … that are not under their responsibility'. 조문 아닌 전문",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "ROP 는 취약점 인지, 사고 인지, 시정 조치 이용 가능, 사고 통지 제출 시각을 따로 기록해 기한 계산 이력을 남기고, 배포 제품·유료 서비스·직접 개발·외부 기여·스튜어드 역할을 릴리스와 계약별로 나눈 책임 대장을 둬야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1522"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f27~f31 에서 도출(구축자 의견). ROP 사업자의 제조자 해당성은 판정하지 않음(oq-291)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "Apache License 2.0 제4절 (a)는 저작물이나 파생저작물을 재배포할 때 수령자에게 이 라이선스 사본을 제공하도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1524"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4(a) 'You must give any other recipients of the Work or Derivative Works a copy of this License'. SaaS 제공만의 의무를 판정한 것이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "같은 절 (b)는 수정한 파일에 변경했다는 사실을 눈에 띄게 표시하도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1524"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4(b) 'You must cause any modified files to carry prominent notices stating that You changed the files'. 소스 공개 의무로 넓히지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "같은 절 (d)는 원 저작물에 NOTICE 파일이 있으면 배포하는 파생저작물에 관련 귀속 고지의 읽을 수 있는 사본을 NOTICE 파일, 소스·문서, 또는 통상 표시되는 화면 가운데 한 곳에 포함하도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1524"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§4(d) 'If the Work includes a \"NOTICE\" text file … must include a readable copy of the attribution notices'. 파생저작물과 무관한 고지는 제외",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "REUSE 명세 3.3(2024-11-14)은 주석을 넣을 수 없는 파일의 라이선스 정보를 같은 이름에 .license 확장자를 붙인 인접 텍스트 파일에 두도록 규정하며(MUST), REUSE.toml 로 정보를 모아 두는 방법도 함께 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1525"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Comment headers 절: 'MUST be in an adjacent text file of the same name with the additional extension .license'. 실제 로봇 3D 자산 적용 사례는 아님(oq-292 부분 근거)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "SPDX 명세 2.2.2 부록 D.4.2 는 둘 이상의 라이선스 중 하나를 고를 수 있음을 OR 연산자로 표현하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1527"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "D.4.2 Disjunctive 'OR' operator: 'choice between two or more licenses'. 문법·의미 표현이며 라이선스 호환성의 법률 판정이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "같은 부록 D.4.3 은 둘 이상의 라이선스를 동시에 준수해야 하는 경우를 AND 연산자로 표현하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1527"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "D.4.3 Conjunctive 'AND' operator: 'simultaneously comply'. 표현식에 함께 적었다고 호환성이 입증되지 않음. SPDX 개요는 기존 ref-1230(area59-s7 SPDX 행)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "reuse-tool 프로젝트 자체 변경기록(CHANGELOG, v6.1.0 태그)은 v6.0.0(2025-10-06)에서 reuse lint 에 SPDX 문법상 유효하지 않은 라이선스 표현식을 잡는 'Invalid SPDX License Expressions' 검사 항목을 추가했다고 기록한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1526"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "프로젝트 자체 변경기록: v6.0.0 Added 'A new criterion 'Invalid SPDX License Expressions' has been added to reuse lint'. 실행 재현은 하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "ROP 릴리스 파이프라인은 SPDX 표현식 문법 검사와 파일별 권리 정보(.license·REUSE.toml) 검사를 자동화하되, 권리 범위·배포 조건 검토 결과는 별도로 보존하고, 메시·텍스처 같은 시뮬레이션 자산의 권리 정보를 모델 전체 코드 LICENSE 와 분리해 추적해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1525",
        "ref-1527",
        "ref-1526"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f36~f39 에서 도출(구축자 의견). 기존 Gazebo 모델 단위 공백(area59-s6)과 연결",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "NVIDIA GR00T-N1.6-3B 모델 저장소의 고정 커밋(d0814e7) LICENSE 제3.3절은 저작물과 파생물을 비상업적(연구·평가 목적) 용도로만 쓰게 하고, NVIDIA 와 계열사는 상업적으로 쓸 수 있다고 정한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1528"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "벤더 주장: LICENSE §3.3 'only may be used or intended for use non-commercially … NVIDIA Corporation and its affiliates may use … commercially … research or evaluation purposes only'. 벤더 라이선스 문면 단독. 다른 모델판·코드 저장소·별도 계약은 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f42",
      "claim": "배포 심사에서는 모델 가중치의 커밋과 LICENSE 를 코드 라이선스와 분리해 등록해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1528"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f41 에서 도출(구축자 의견). 상업적 사용 가능성을 스스로 판정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "제조물책임지침 (EU) 2024/2853(2024-10-23 채택, 관보 2024-11-18) 원판 제2조1항은 'after 9 December 2026' 에 출시·사용 개시된 제품에 적용한다고 적었으나, 2026-05-07 정오표(OJ L 2026/90364)가 이를 'after 8 December 2026' 으로 고쳤다. 정정 후 문언은 2026-12-08 이 지난 뒤, 곧 2026-12-09 에 출시·사용 개시된 제품부터 적용된다는 뜻이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1529",
        "ref-1530"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정오표 1쪽 Art 2(1): 'for: … after 9 December 2026 … read: … after 8 December 2026'. '2026-12-08 이후'로 옮기면 12-08 이 포함돼 틀림. 전문 (63)·제21조의 'before 9 December 2026' 과 맞음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "같은 지침 제2조2항은 상업 활동 밖에서 개발되거나 공급되는 자유·오픈소스 소프트웨어에는 지침을 적용하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1529"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제2조② 'does not apply to free and open-source software that is developed or supplied outside the course of a commercial activity'. 전문 (15): 그런 소프트웨어를 제조자가 상업 활동 중 제품에 통합하면 그 제조자에게 책임을 물을 수 있음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "같은 지침 제4조1항은 '제품'을 다른 동산·부동산에 통합되거나 연결된 경우를 포함한 모든 동산으로 정의하고 전기, 디지털 제조 파일, 원재료, 소프트웨어를 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1529"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제4조(1) ''product' means all movables … it includes electricity, digital manufacturing files, raw materials and software'. 기존 s3·s4·s7 의 소프트웨어 포함 서술(ref-1227 해설)을 1차 원문으로 보강",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "기존 위키(2026-09-30-area59-s3.md 본문 둘째 문단, s7 PLD 행)의 '2026-12-09 이후 출시·사용 개시 제품' 날짜는 정정 후 의미와 같아 바꿀 필요가 없지만, 근거가 정오표(2026-05-07) 전에 나온 법률사무소 해설(ref-1227, 2026-03-23)이므로 적용 시점·소프트웨어 포함·FOSS 제외의 근거를 EUR-Lex 원문과 정오표로 바꾸고 '정오표 기준' 임을 밝혀야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1227",
        "ref-1529",
        "ref-1530"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원판 'after 9 December 2026' 은 문언상 12-10 부터라 해설과 하루 어긋남. ref-1227 의 증거 공개·결함 추정·보안 업데이트 서술(s6·s8)은 이번에 원문 대조하지 않아 해설 기준으로 둠",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f47",
      "claim": "김정욱·성현지·유성희(2025, 규제연구 34권 1호)는 싱가포르 IMDA 가 시행한 AI 샌드박스 2건이 모두 기술 개발·혁신 지원에 가까운 형태로, 한국과 달리 규제 특례를 부여하기 위한 목적이 아니라고 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1531"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "III.4 소결, 106쪽: '2건 모두 기술 개발과 혁신을 지원하는 관점에서의 샌드박스에 가까운 형태로, 한국과 달리 규제 특례를 부여하기 위한 목적으로 추진하는 것은 아니다'. 제도 비교 연구이며 로봇 실증이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f48",
      "claim": "ROP 의 규제 검증 계획은 의무·책임자·시험·증거·제출처를 연결하고, 규제 특례(샌드박스) 승인을 받은 것과 기술 검증 프로그램에 참가한 것을 구분해 기록해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1531"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f47 에서 도출(구축자 의견)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1517",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI)",
      "published": "2026-07-24",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "AI Act 디지털 옴니버스 규정(OJ L 2026/1744). 제1조(40) 고위험 적용일(2027-12-02·2028-08-02), 제1조(41) 기계규정의 부속서 I Section B 이동, 제1조(2) 제2조2항 적용 조항 한정, 제3조 기계규정 제8조 위임법령·제20조 추정, 제4조 발효를 관보 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1518",
      "org": "법제처 국가법령정보센터 (과학기술정보통신부)",
      "title": "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 [시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정] 제33조·제34조·제35조",
      "published": "2026-01-20",
      "url": "https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810895",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "인공지능기본법의 열람한 판(법률 제21311호, 2026-07-21 시행) 조문 링크. 제33조(고영향 확인)·제35조(영향평가)와 제34조①2호를 읽었다. 법 최초 시행(2026-01-22) 원판은 기존 ref-620(미열람)이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1519",
      "org": "산업통상부 기계로봇제조정책과",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정(안) 행정예고 (산업통상부 공고 제2025-042호)",
      "published": "2025-11-06",
      "url": "https://www.motir.go.kr/kor/article/ATCLa6723dc7b/458/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "2025-11-06 행정예고 공고와 첨부 개정안(hwpx). 통보 기한 30일 명시(안 제9조), 심사항목 통·폐합 16개→8개(안 별표 3)를 담는다. 최종 고시는 제2025-21호(ref-1469).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1520",
      "org": "법제처 국가법령정보센터 (산업통상부)",
      "title": "지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의10(책임보험 등의 가입금액)",
      "published": "2025-10-01",
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=278777",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "시행규칙 현행 통합본. 제7조의10 의 실외이동로봇 책임보험·공제 보험금 기준(사망·후유장애 1억5천만원, 부상 3천만원, 재물 10억원)과 '[본조신설 2023. 11. 17.]' 표시를 확인했다. 같은 시행규칙 제7조의4·5 는 기존 ref-1470.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1521",
      "org": "Hong Kong SAR Government (Innovation, Technology and Industry Bureau)",
      "title": "LCQ20: Regulating operation of intelligent robots",
      "published": "2026-05-20",
      "url": "https://www.info.gov.hk/gia/general/202605/20/P2026052000416p.htm",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "입법회 질문에 대한 정부 서면 답변(2026-05-20). 지능형 로봇 사용에 제3자 책임보험을 강제하는 법정 요건이 없다고 밝혔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1522",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act)",
      "published": "2024-11-20",
      "url": "https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "사이버복원력법 관보 원판(OJ L 2024/2847, 2024-11-20). 제14조 보고 기한의 기산점, 제24조3항 스튜어드, 제71조2항 적용일, 전문 (18) 오픈소스 범위를 Publications Office 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1523",
      "org": "European Union Agency for Cybersecurity (ENISA)",
      "title": "The CRA Single Reporting Platform is launched",
      "published": "2026-09-11",
      "url": "https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "ENISA 보도자료(2026-09-11). 단일 보고 플랫폼 초기 운영 역량 가동과, 제조자 보고 의무(2026-09-11)와 스튜어드 보고 의무(제24조3항, 2027-12-11)의 적용일 구분을 밝힌다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1524",
      "org": "Apache Software Foundation",
      "title": "Apache License, Version 2.0",
      "published": "2004-01",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Apache License 2.0 원문. 제4절 재배포 조건 (a) 라이선스 사본, (b) 수정 파일 고지, (d) NOTICE 귀속 고지를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1525",
      "org": "Free Software Foundation Europe (REUSE)",
      "title": "REUSE Specification – Version 3.3",
      "published": "2024-11-14",
      "url": "https://reuse.software/spec-3.3/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "파일별 저작권·라이선스 정보 표기 명세 3.3판. 주석을 넣을 수 없는 파일은 같은 이름 + .license 인접 파일, 또는 REUSE.toml 로 정보를 둔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1526",
      "org": "FSFE reuse-tool 기여자 (GitHub)",
      "title": "reuse-tool CHANGELOG.md (v6.1.0 태그)",
      "published": "2025-10-07",
      "url": "https://github.com/fsfe/reuse-tool/blob/v6.1.0/CHANGELOG.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "reuse-tool 프로젝트 자체 변경기록(v6.1.0, 2025-10-07). v6.0.0(2025-10-06) Added 의 'Invalid SPDX License Expressions' lint 항목을 확인했다. 기능 실행은 재현하지 않았다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/fsfe/reuse-tool/v6.1.0/CHANGELOG.md",
      "source_unopened": false
    },
    {
      "id": "ref-1527",
      "org": "SPDX Project (Linux Foundation)",
      "title": "Annex D: SPDX License Expressions - specification v2.2.2",
      "published": null,
      "url": "https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "SPDX 2.2.2 명세 부록 D. 라이선스 표현식 문법과 OR(선택)·AND(동시 준수)·WITH 연산자를 정의한다. 발행일은 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1528",
      "org": "NVIDIA (Hugging Face 모델 저장소)",
      "title": "GR00T-N1.6-3B / LICENSE (NVIDIA License)",
      "published": "2025-12-15",
      "url": "https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/LICENSE",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "로봇 기반 모델 가중치 저장소의 고정 커밋(d0814e7, 2025-12-15) 라이선스 문서. 제3.3절 비상업(연구·평가) 사용 제한과 NVIDIA·계열사 예외를 담는다. 발행일은 커밋 날짜다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1529",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC",
      "published": "2024-11-18",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "개정 제조물책임지침 관보 원판(OJ L 2024/2853). 제2조1항 적용 시점(원판 'after 9 December 2026'), 제2조2항 비상업 FOSS 제외, 제4조1항 제품 정의(소프트웨어·디지털 제조 파일 포함)를 Publications Office 원문으로 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1530",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Corrigendum to Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC",
      "published": "2026-05-07",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202690364",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "제조물책임지침 정오표(OJ L 2026/90364, 2026-05-07). 제2조1항의 'after 9 December 2026' 을 'after 8 December 2026' 으로 고친다(1쪽).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1531",
      "org": "김정욱·성현지·유성희",
      "title": "한·싱가포르 규제샌드박스 비교를 통한 AI 샌드박스 효율화 방안 제언",
      "published": "2025-06",
      "url": "https://journal.kci.go.kr/ksrs2002/archive/articlePdf?artiId=ART003225249",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "규제연구 34권 1호(DOI 10.22954/ksrs.2025.34.1.003). 한국 규제샌드박스와 싱가포르 IMDA AI 샌드박스를 비교한 제도 연구로, 로봇 실증 연구는 아니다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1238",
      "org": "Commonwealth of Virginia (Code of Virginia)",
      "title": "§ 46.2-908.1:1. Personal delivery devices",
      "published": null,
      "url": "https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "버지니아주 개인 배송 장치 조문(기존 출처). 이번 재열람에서 E항 보험이 운영자 통제 아래 장치들의 합산 운행 손해를 대상으로 함을 확인했다.",
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
      "accessed": "2026-10-12",
      "summary": "현행 운행안전인증 고시(기존 출처). 이번 재열람에서 '[시행 2025. 11. 24.]' 표시와 제8조①2호(로봇 또는 관제장치 일부 변경 시 심사 일부·전부 면제), 제9조①(30일 이내 통보)을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1227",
      "org": "Gibson Dunn",
      "title": "EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains",
      "published": "2026-03-23",
      "url": "https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "개정 제조물책임지침 법률사무소 해설(기존 출처). 정오표(2026-05-07) 전에 나온 글이며, 이번 갱신에서 적용 시점·FOSS 제외·제품 정의의 근거를 관보 원문으로 옮기는 대상이다. 이번에는 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1235",
      "org": "대한민국 정책브리핑 (과학기술정보통신부)",
      "title": "'인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무",
      "published": "2026-01-21",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958380",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "인공지능 기본법 2026-01-22 시행과 고영향 AI 판단 설명을 알린 정부 보도(기존 출처). 법 최초 시행일 근거로 쓴다. 이번에는 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3(분리 2026-09-30-area59-s3) — 본문 둘째 문단 PLD 문장: 날짜 '2026-12-09 이후'는 정오표 후 의미와 같아 유지하고, 근거를 ref-1227 해설에서 관보 원문·정오표로 교체(f43·f45·f46), '정오표(2026-05-07) 기준, 원판은 after 9 December 2026' 을 밝힘. '2026-12-08 이후'로 쓰지 않음. 비상업 FOSS 제외(f44) 추가 / 섹션 4(분리 2026-09-30-area59-s4) — 제조물책임 항목의 EU 부분을 제4조1항(f45)으로, 고영향 인공지능 항목에 제33조 사전 검토 의무·확인 요청 재량(f11·f12), 제35조 영향평가 노력의무(f13), 판 표기(열람한 판 법률 제21311호, 두 조는 2026-01-22 원법부터, f14) 추가. CRA 항목에 스튜어드 2027-12-11(f30) / 섹션 5 — 한국 사례 '제약' 칸 보험 문장 뒤에 시행규칙 제7조의10 가입금액(사망 1억5천만원·최저 2천만원, 부상 3천만원, 후유장애 1억5천만원, 재물 사고당 10억원; f18~f21), 2023-11-17 신설 후 현행 통합본(산업통상부령 제1호, 2025-10-01 시행)까지 그대로(f22) — '현행 미확인' 단서 쓰지 않음. 협회 단체보험료(ref-1232)는 가입금액과 다른 지표로 구분(f23). 16가지→8개 문단의 '개정 시점·근거 고시 … 확인하지 못했다'를 '공고 제2025-042호(2025-11-06) 행정예고의 심사항목 통·폐합(16개→8개), 고시 제2025-21호로 2025-11-24 시행'(f16)으로 짧게 정정 — '채택 미확인' 서술 금지, 별표 대응 상세는 기존 내용 확인(2026-10-11-area50-s7·s11, area49-s7·s11)으로 링크만. 버지니아 '제약' 칸 보험 문장을 합산 운행 기준으로 정밀화(f24). 해외 비교 문장에 홍콩 정부 답변(f25) 추가 / 섹션 6(분리 2026-09-30-area59-s6) — '사고·취약점 보고와 증거 기록' 소절: 24h·72h·14일·1개월 기존 서술은 그대로 두고 기산점(인지 시점·시정 조치 이용 가능 시점·사고 통지 제출 시점; f27~f29)만 보탬, PLD 서술은 해설 기준임을 유지하되 적용 시점은 원문으로(f46). '라이선스 선언·자동 검사·SBOM' 소절: Apache 2.0 §4(a)(b)(d)(f33~f35), REUSE 3.3 .license·REUSE.toml(f36), SPDX OR/AND(f37·f38), reuse lint 표현식 검사(f39, 프로젝트 자체 변경기록으로 명시), 모델 가중치 별도 라이선스(f41 [추정]·벤더 라이선스 문면); 의견 f32·f40·f42 / 섹션 7(분리 2026-09-30-area59-s7) — 새 행 'EU AI Act (Regulation (EU) 2024/1689)와 디지털 옴니버스 (EU) 2026/1744': 발효 2026-07-27(f1), 부속서 III 2027-12-02·부속서 I 2028-08-02(f2·f3), 기계규정의 Section A→B 이동과 바뀐 제2조2항(6(1)·60a·102~112조만, f4·f5), 기계류 로봇 AI 는 기계규정 경로라는 해석(f6 [추정]); 날짜 셋은 2026-10-09-area43-s10.md 44행(ref-1322)과 중복이므로 새 사실로 쓰지 않고 1차 근거로 올리는 행. 'EU 기계류 규정' 행에 제8조 위임법령(부속서 III, 제III장 2절·제17·19·72·73조 반영, 2028-08-02까지 적용, f7·f8)과 제20조10항 적합 추정(f9). 'EU 개정 제조물책임지침' 행: 출처를 Gibson Dunn 에서 관보 원문·정오표로, 날짜 표현 '2026-12-08 후(곧 2026-12-09 출시·사용 개시분부터), 2026-05-07 정오표 기준'(f43), FOSS 제외(f44), 제품 정의(f45). '인공지능 기본법' 행에 제33·35조와 판 표기(f11~f14). 'EU 사이버복원력법' 행: 기존 기한 유지 + 기산점(f27~f29), 스튜어드 제24조3항·제71조2항 2027-12-11(f30), 오픈소스 범위 전문 (18)(f31). '실외이동로봇 운행안전인증' 행 근거 고시 제2025-21호(f16). 새 행: 시행규칙 제7조의10(f18~f22), Apache License 2.0(f33~f35), REUSE 3.3(f36), SPDX 행 확장(f37~f39), NVIDIA GR00T 가중치 라이선스(f41, 벤더 라이선스 [추정]) / 섹션 8(분리 2026-09-30-area59-s8) — 김정욱 외(2025) 샌드박스 비교 연구 추가(f47, 제도 비교이며 로봇 실증 아님); Gibson Dunn 항목은 '적용 시점·FOSS 제외·제품 정의는 관보 원문(f43~f45)으로 대체, 나머지는 해설 기준'으로 고침(f46). Ogayemi(2026) 연구는 초록만 확인·LLM 에이전트 대상이라 넣지 않음; 의견 f48 / 섹션 9 — 업종별 조건 행의 'ROP가 직접 맡는 것'에 규제 대장 분류 경로·적용일 분리(f10), 고영향 검토 기록(f15), 보험 상태를 관할·운영자·플릿 단위로(f23·f26), CRA 기한 기산 시각 기록·역할 대장(f32), 릴리스 권리 검사(f40·f42) — 모두 [의견] / 섹션 11(분리 2026-09-30-area59-s11) — 새 질문 다섯 건을 실제 id 로 표기(oq-288·oq-289·oq-290·oq-291·oq-292, docs/open-questions.md 의 질문 문장과 대조). 해결 제안: oq-288(조항 시행규칙 제7조의10, 금액 f18~f21, 현행 통합본 확인 f22). 부분 답(열림 유지): oq-143(f2·f3·f5·f11~f14; 대화 기능 분류·로그 항목은 미답), oq-186(f16; 알림음·등화장치 이동은 area50 과 같은 결론으로 미답), oq-187(f17; 관제장치 해당성 해석 없음), oq-289(f43·f44; 오케스트레이션 소프트웨어 판정 없음), oq-291(f27~f31), oq-292(f36~f39; 3D 로봇 자산 SPDX 사례 없음). 다른 영역 질문 근거 연결: oq-106(f4~f8, 기계류 AI 의 적용 경로가 바뀜), oq-316·oq-338(f5·f6), oq-313(f18 법 제40조의4 근거만). 답하지 못함: oq-173, oq-231, oq-239, oq-249, oq-250, oq-262, oq-275, oq-279, oq-282, oq-290. oq-103 은 2026/1744 제3조가 기계규정 제8·20·47조만 고치고 적용일을 바꾸지 않아 변동 없음. 메모의 'Q5'는 내부 조사 번호라 쓰지 않음 / 기존 내용 확인(새로 넣지 않음): 단일 보고 플랫폼 2026-09-11 가동(area59-s4·s7), CRA 24h·72h·14일·1개월(area59-s6, glossary/cyber-resilience-act.md, glossary/actively-exploited-vulnerability.md), 운행안전인증 16→8 경위·별표 대응(2026-10-11-area50-s7·s11, area49-s7·s11, safety/human-proximity-safety.md; ref-1485·ref-1484·ref-1118·ref-1469), SPDX 개요(area59-s7, ref-1230), AI Act 적용일 셋(2026-10-09-area43-s10.md 44행, ref-1322) / 후속 정리 필요(이번 갱신 범위 밖, 다른 페이지): 2026-10-09-area43-s10.md 44행의 ref-1322 기반 날짜를 ref-1517 로 근거 교체하고 2026-10-09 일일 로그 856행 추가 조사 요청을 닫음; 같은 파일 45행 '기계류 등 부속서 I 제품에 내장된 경우라면 적용 시점은 2028-08-02', categories/safety/index.md 149행(부속서 I 기계류 고위험 서술), categories/ai-and-learning/index.md 131행을 f4~f8 구조(Section B 이동, 기계규정 위임법령 경로)로 정리. ref-620(원판, 미열람)과 ref-1518(열람한 판)의 관계, ref-1470(같은 시행규칙 제7조의4·5)과 ref-1520(제7조의10)의 관계를 참고문헌에 표기. 다음 실행 후보: 47. AI·학습·적응과 모델 운영·48. 안전·위험 관리(f4~f9, oq-106), 66. 실외(f16~f22)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "(EU) 2026/1744 로 기계규정 제8조에 근거가 생긴, 고위험 AI 의 보건·안전 요구를 기계규정 부속서 III 에 추가하는 위원회 위임법령은 채택됐는가, 채택됐다면 번호와 반영한 AI Act 요구(제III장 제2절, 제17·19·72·73조)의 범위는 무엇이며 여러 로봇을 지시하는 오케스트레이션 소프트웨어의 AI 도 그 대상에 드는가? | 관련 영역: 59. 법·규제·보험·라이선스, 48. 안전·위험 관리 | 근거: f7 | 종류: 일반",
    "국내 실외이동로봇 책임보험·공제의 실제 보험사 약관은 시행규칙 제7조의10 기준 금액 외에 관제 장애·통신 단절·사이버 사고로 생긴 손해와 제조사·관제 사업자에 대한 구상을 어떻게 다루는가? | 관련 영역: 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f18 | 종류: 일반"
  ],
  "open_questions_resolved": [
    "oq-288"
  ],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-02/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f7·f8: 기계규정 제8조 위임법령의 번호·채택 여부 미확인(검증 때 Publications Office 색인에서 2023/1230 을 고치는 법령은 2024/2748·2026/1744 둘뿐이었으나 색인 지연 가능성이 있어 미채택으로 단정하지 않음) — 새 열린 질문으로 올림",
      "f14: 원판(법 최초 시행판, ref-620 lsiSeq=268543)은 이번에도 열지 못함. 두 조가 원법부터 있었다는 판단은 열람한 판의 개정 표시와 독립 검증 결과에 기댐. 제35조①의 개정 문장(2026-01-20)은 신구 대비표 미확인. 시행령 미확인",
      "f18~f22: 실제 보험사 약관·보험료와의 대조는 하지 않음(새 열린 질문)",
      "f17: oq-187 의 핵심(오케스트레이션 계층이 인증상 관제장치인지)은 해석 자료가 없어 미답. 시행규칙 제7조의7③ 2025-10-01 개정 내용은 이번에 읽지 않음",
      "f16: 2023 별표 3 의 알림음·등화장치가 현행 별표 3 밖 다른 규정으로 옮겨졌는지는 area50 과 같이 미확인(oq-186 열림 유지)",
      "f41: GR00T 라이선스는 벤더 라이선스 문면 단독이라 [추정]·vendor_claim. 다른 모델판(N1.7 등)·별도 상업 계약은 미확인",
      "f39: reuse-tool 기능은 프로젝트 자체 변경기록으로만 확인하고 실행 재현하지 않음",
      "f46: Gibson Dunn 해설(ref-1227)의 증거 공개·결함 추정·보안 업데이트 서술은 이번에 PLD 원문과 대조하지 않음",
      "메모 F33(Ogayemi 2026, International Journal of Information Security 25:164)은 Springer 본문을 열지 못해 Crossref 초록('Using doctrinal analysis')만 확인됐고 LLM 자율 에이전트 대상이라 출처·finding 에서 뺌",
      "GPL/AGPL 원문 조건(메모 N02)은 이번 출처에 넣지 않음. PLD 두 번째 정오표(OJ L 2026/90830, 2026-09-29)는 네덜란드어판만 있어 영문 본문 영향 없음으로 보고 넣지 않음"
    ],
    "scope_violations": [
      "f4~f9: EU AI Act·기계규정의 기계류 AI 적용 구조는 47. AI·학습·적응과 모델 운영, 48. 안전·위험 관리와 겹친다. 이 영역에는 법 적용 경로·적용일 관점으로만 쓰고 다른 영역 페이지 수정은 후속 정리로 남김",
      "f16·f17: 실외이동로봇 운행안전인증은 50. 안전 표준·인증·사고 조사, 66. 실외와 겹치며, 이 영역에는 근거 고시 정정과 관제장치 변경 조항으로만 씀",
      "f27~f31: CRA 보고는 52. 통신 보호·위협 관리·감사, 57. 자산·소프트웨어 수명주기 관리와 겹치며, 이 영역에는 법적 의무의 기산점·주체로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 15
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1517~ref-1531, 예약 구간 ref-1517~ref-1546 안, 한도 도달), 재사용 4건(ref-1238·ref-1469·ref-1227·ref-1235). 출처 매핑(검증 결과 기준): 메모 n1→ref-1517, n2(유럽위원회 'AI Omnibus enters into force')는 신규 출처 한도로 빼고 발효일은 n1 제4조와 관보 게재일로 근거를 둠(검증 때 같은 2026-07-27 확인), n3(Ogayemi)은 초록만 확인·LLM 에이전트 대상이라 뺌, n4→ref-1518(열람한 판 법률 제21311호; 원판 ref-620 과 별도 id), n5→ref-1519, n6→ref-1520(2023 개정문 목록 대신 현행 통합본 lsiSeq=278777; ref-1470 은 같은 시행규칙의 제7조의4·5 제목이라 별도 id), n7→ref-1238, n8→ref-1521, n9→ref-1522('정오표 표시 포함' 표기 삭제, 2024-11-20 관보 원판), n10→ref-1523, n11(유럽위원회 CRA 오픈소스 해설)은 한도로 빼고 같은 내용을 CRA 전문 (18)·제24조로 근거를 옮김, n12→ref-1524, n13→ref-1525, n14→ref-1526, n15→ref-1527, n16→ref-1528, n17→ref-1529, n18→ref-1530, n19→ref-1531. 추가 재사용: ref-1469(최종 고시·제8조), ref-1227(근거 교체 대상, 미재열람), ref-1235(법 시행일, 미재열람). 교차 확인 0건: 모든 사실 finding 이 단일 1차 원문이거나 같은 계열(ENISA 발표는 CRA 조문을 그대로 옮긴 것이라 독립으로 세지 않음). 검증 반영(보고서 H절 Top 10): (1) PLD 'after 8 December 2026' 을 '2026-12-08 이후'가 아니라 '2026-12-08 후, 곧 2026-12-09 출시·사용 개시분부터'로(f43), s3·s7 은 날짜가 아니라 근거·표현을 고침(f46), 1차 원문으로 올림·FOSS 제외(f44); (2) 2026/1744 의 부속서 I Section B 이동과 제2조2항 한정(f4·f5), 기계류 AI 는 기계규정 제8조 위임법령 경로(f6~f9), oq-106 연결, 다른 영역 페이지는 후속 정리로만; (3) 적용일 셋은 area43-s10(ref-1322)과 중복이라 1차 근거 상향으로 표시; (4) 16→8 은 고시 제2025-21호(2025-11-24) 기준으로 짧게, '채택 미확인' 서술 없음(f16); (5) 보험은 현행 통합본으로 근거 교체, '현행 미확인' 단서 삭제, oq-288 해결 제안(f18~f22); (6) 메모의 새 질문을 oq-288·oq-289·oq-290·oq-291·oq-292 로 표기(질문 문장 대조), 'Q5' 삭제; (7) 제33·35조는 원법(2026-01-22 시행)부터, 법률 제21311호는 열람한 판(f14), ref-620 과 별도 id; (8) Apache 조항 표기 §4(a)(b)(d)(f33~f35); (9) Ogayemi 제외; (10) CRA 기존 24h/72h/14일/1개월은 유지하고 기산점(f27~f29)과 스튜어드 2027-12-11(제24조3항·제71조2항, f30)만 추가. 그 밖에 X01 GR00T 는 [추정]·벤더 라이선스 문면(f41), reuse-tool 은 프로젝트 자체 변경기록으로 명시(f39), 메모 F20(SRP 가동)은 기존 내용이라 finding 으로 넣지 않음. 열린 질문: oq-288 해결 근거 f18~f22. 부분 답 oq-143·oq-186·oq-187·oq-289·oq-291·oq-292, 근거 연결 oq-106·oq-316·oq-338·oq-313. oq-290 은 이번 자료로 답하지 못함. 메모의 '새로 생긴 열린 질문' N01(위임법령)·N03(보험 약관)을 새 질문으로 올리고 N02(GPL/AGPL)는 근거 출처가 없어 올리지 않음. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### runs/2026-10-12-02/verification.json

```json
{
  "run_id": "2026-10-12-02",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. ref-1517 EUR-Lex 원문은 이번 검증에서 열람 실패(PDF·HTML·ELI 모두 빈 본문 응답) — 원문 미열람(검증). ERTICO 기사(관보 게재 2026-07-24, 발효 2026-07-27)와 Hunton 블로그(게재 3일 뒤 2026-07-27 발효)로 날짜를 독립 확인했다. 리서치는 원문 열람(fetched true)으로 기록했다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 부속서 III 고위험 2027-12-02 는 Hunton·ERTICO·Cooley 세 해설이 일치한다. '제6조5항 제외' 세부는 검증 단계에서 원문 미열람이라 리서치의 원문 인용에 기댄다. 2026-10-09-area43-s10.md 44행(ref-1322)과 같은 날짜이므로 새 사실이 아니라 근거 상향으로만 쓴다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 부속서 I(제6조1항) 2028-08-02 는 Hunton·ERTICO·Cooley 가 일치한다. 새 (d)호(제102~110조 2026-07-27 적용)는 해설에서 찾지 못해 검증 단계 원문 미열람. 원판 AI Act 의 제102~110조가 다른 법령 개정 조항이라는 구조와는 맞는다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 기계규정의 부속서 I Section A → Section B 이동은 IBF Solutions 기술 기사('from Annex I, Part A, to Part B')와 Cooley 해설('moving the Machinery Regulation from Section A to Section B')로 독립 확인했다. 원문 조항 번호(제1조(41))는 리서치의 원문 인용에 기댄다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(요지). 제2조2항의 적용 조항 목록(6(1)·60a·102~112, 57~59 조건부)은 검증 단계에서 원문 미열람이다. Cooley 해설이 요지(Section B 제품에는 대부분 고위험 조항이 직접 적용되지 않고 기계규정 경로를 따른다)를 뒷받침하고, 원판 제2조2항 구조(6(1)·102~109·112, 57 조건부)와도 맞는다. 단일 1차 출처."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 조합 해석이며 Cooley 해설이 요지를 지지한다. 다만 같은 Cooley 글이 2028-08-02 날짜의 부속서 I 예시로 기계류를 들어 2차 자료 설명이 엇갈린다. 기존 위키 서술(area43-s10 45행, safety/index.md 149행, ai-and-learning/index.md 131행)과 충돌하므로 둘 다 제시하고 oq-106 에 연결한다(required_fixes). 개별 제품 해당성은 판단하지 않는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IBF Solutions 기사가 기계규정 제8조 위임법령(부속서 III 에 고위험 AI 보건·안전 요구 추가)을 같은 문구로 옮긴다. 제17·19·72·73조 반영 범위는 검증 단계 원문 미열람. 위임법령 번호·채택 여부 미확인(새 열린 질문)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IBF 기사가 'shall apply by 2 August 2028'과 '27 July 2026 부터 5년' 위임 기간을 옮긴다. IBF 해설은 'published by 2 August 2028'로도 적어 표현이 엇갈리므로 본문은 조문 문언('2028-08-02 까지 적용')으로만 쓴다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. IBF 기사가 기계규정 제20조 새 제10항(AI Act 제40·41조 조화 표준·공통 사양 준수 시 부속서 III 적합 추정)을 옮기고, ERTICO 기사도 기계규정상 적합성 추정을 언급한다. 단일 1차 출처."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f2~f9 에서 도출한 구축자 의견. 본문에 '(구축자 의견)'을 표시하고 특정 ROP 기능의 법적 해당성은 판정하지 않는다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. law.go.kr 조문 링크를 열었다. 법률 제21311호(2026-01-20 일부개정, 2026-07-21 시행)의 제33조①에 '고영향 인공지능에 해당하는지에 대하여 사전에 검토하여야 하며'가 있다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 같은 페이지의 제33조①(확인 요청 '할 수 있다')·②(장관 확인 의무)·③ 가이드라인·④ 대통령령을 확인했다. 제33조에는 개정 표시가 없다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 열어 본 조문 링크에는 제33조만 나와 제35조는 검증 단계에서 원문 미열람. 검색 결과(wikidocs 법령 정리)가 제35조①의 '노력하여야 한다'(노력의무)와 ②의 국가기관등 우선 고려를 같게 적는다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 리서치의 근거대로라면 제35조①에 '<개정 2026. 1. 20.>' 표시가 있다. 그러면 바뀐 제35조① 문장은 법률 제21311호 시행일(2026-07-21)부터 효력이 있을 수 있으므로 '시행 2026-07-21 은 두 조의 발효일이 아니다'와 '두 조의 의무는 원법부터 있던 것'을 단정할 수 없다. 원판(ref-620) 미열람, 신구 대비표 미확인. 제33조에 개정 표시가 없다는 점만 [사실]로 쓸 수 있다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견 표시가 필요하다. ref-1235 는 이번에 다시 열지 않았다(source_unopened true)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(간접). motir.go.kr(ref-1519)과 law.go.kr(ref-1469)은 이번 검증에서 ECONNRESET 로 여러 번 열람에 실패했고, 검색으로도 공고 원문을 찾지 못했다(원문 미열람(검증)). 다만 16개→8개 통폐합과 2025-11-24 발령·시행은 앞서 검증된 2026-10-11-06 브리프의 ref-1504(정부 보도참고)·ref-1505(산업통상부 고시 게시)와 일치한다. 같은 정부 계열이라 교차 확인으로 세지 않는다. 행정예고안 수치는 '안' 기준이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-1469 는 이미 등록된 참고문헌이지만 이번 검증에서 law.go.kr 접속이 계속 끊겨(ECONNRESET 3회) 제8조①2호 문언을 확인하지 못했고, 대조할 2차 자료도 없다. 리서치의 원문 열람 기록에만 기댄다. 오케스트레이션 계층의 관제장치 해당성(oq-187)은 판단하지 않는다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). ref-1520 현행 통합본 페이지는 열렸고 법령명과 '[시행 2025. 10. 1.] [산업통상부령 제1호, 2025. 10. 1., 타법개정]'이 일치한다. 다만 조문 본문(제7조의10)은 프레임 밖이라 검증 단계에서 원문 미열람. 2026-09-30-23 브리프 자체 점검에 기록된 검색 요약 금액(사망 1억5천만원)과 일치한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). f18 과 같다. 부상 3천만원은 2026-09-30-23 브리프의 검색 요약 금액과 일치하며, 조문 본문은 검증 단계 원문 미열람. 법령 기준 금액이고 보험 약관의 보장 한도가 아니다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). f18 과 같다. 후유장애 1억5천만원은 조문 본문 기준이며 검증 단계에서는 원문 미열람."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 재물 사고당 10억원은 2026-09-30-23 브리프의 검색 요약 금액과 일치한다. 조문 본문은 검증 단계 원문 미열람."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). 현행 통합본의 시행 표시(산업통상부령 제1호, 2025-10-01)는 일치한다. '[본조신설 2023. 11. 17.]'과 개정 표시가 없다는 점은 리서치의 원문 열람에 기댄다(검증 단계 조문 본문 미열람)."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견. 협회 단체보험 보험료(ref-1232)와 법령 기준 금액을 다른 지표로 구분하라는 제안이다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 버지니아 조문 E항을 열어 'general liability coverage of at least $100,000', 'combined operations of personal delivery devices under a personal delivery device operator's control'을 확인했다. 발행일은 미확인."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. LCQ20(2026-05-20) 답변을 열어 'there is no statutory requirement in Hong Kong mandating the purchase of third party liability insurance'를 확인했다. 같은 답변에 보험업계와 상품 제공을 협의한다는 문장도 있다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ref-1522 EUR-Lex 는 빈 본문 응답이라 원문 미열람(검증)이다. 검색 결과(여러 해설)가 24시간·72시간 기산점을 '제조자 인지'로 같게 적고, CRA 제14조2항 문언과도 맞는다. 용어는 용어집 '적극 악용 취약점'으로 통일해야 한다(required_fixes)."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 검색 결과가 최종 보고 14일을 시정·완화 조치 이용 가능 시점에서 센다고 같게 적는다. 원문은 검증 단계 미열람."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 중대 사고 최종 보고는 '사고 통지 제출 뒤 1개월'이다. 검색 결과 해설이 '72시간 통지 뒤 1개월'로 일치한다. 원문은 검증 단계 미열람."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. ENISA 보도자료(ref-1523, 2026-09-11)를 열어 제24조3항 스튜어드 보고 의무와 'This article shall apply from 11 December 2027'을 확인했다. ENISA 는 CRA 조문을 옮긴 것이라 독립 교차 확인으로 세지 않는다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. CRA 전문 (18)의 상업 활동 FOSS 한정과 기여자 제외 문언이다(원문은 검증 단계 미열람, 공개 관보 문언과 부합). 조문이 아니라 전문임을 본문에 밝힌다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견. ROP 사업자의 제조자 해당성은 판정하지 않는다(oq-291)."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. Apache License 2.0(2004-01) §4(a) 문언을 열람해 확인했다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §4(b) 'prominent notices stating that You changed the files'를 확인했다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. §4(d) NOTICE 파일 귀속 고지 조건을 확인했다(첫 문장)."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. REUSE 3.3(2024-11-14)을 열어 주석을 넣을 수 없는 파일의 '.license' 인접 파일 규정(MUST)과 REUSE.toml 방법을 확인했다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. SPDX 2.2.2 부록 D.4.2 OR 연산자를 확인했다. 발행일은 페이지에 없다(저작권 표기 2010-2022)."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. D.4.3 AND 연산자('simultaneously comply')를 확인했다. 호환성의 법률 판정이 아니다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. GitHub raw(v6.1.0 태그) CHANGELOG 에서 v6.1.0 - 2025-10-07, v6.0.0 - 2025-10-06 과 'Invalid SPDX License Expressions' 추가 항목을 확인했다. 프로젝트 자체 변경기록이며 실행 재현은 하지 않았다."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·벤더 주장 유지(vendor_claim true). Hugging Face 고정 커밋 d0814e7 의 NVIDIA License §3.3(비상업·연구·평가 목적, NVIDIA·계열사 상업 사용 예외)을 확인했다. 커밋은 '10개월 전'으로 표시되어 2025-12-15 와 맞는다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견. 상업 사용 가능성은 판정하지 않는다."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. EUR-Lex 본문은 열람 실패(검증 단계 원문 미열람). 검색 결과에서 EUR-Lex 정오표 기록(OJ L 2026/90364, 2026-05-07, Art 2(1) 'after 9 December 2026' → 'after 8 December 2026')과 통합본의 'Corrected by' 표시를 확인했다. 2026-10-12-01 브리프 f7(ref-1490)과 같은 결론이다."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 제2조2항 비상업 FOSS 제외는 공개 관보 문언과 부합하고, 2026-10-12-01 브리프 f5(ref-1490)와 같다. 검증 단계 원문 미열람."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 제4조1항 제품 정의(전기·디지털 제조 파일·원재료·소프트웨어 포함)이다. 2026-10-12-01 브리프 f5 와 같다. 검증 단계 원문 미열람."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 날짜 유지·근거 교체 판단은 정오표 확인과 맞는다. ref-1227 은 이번에 다시 열지 않았고(source_unopened true), s6·s8 의 증거 공개·결함 추정 서술은 해설 기준으로 둔다."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분). KCI 논문 상세 페이지에서 서지(규제연구 34권 1호 81~113쪽, DOI 10.22954/ksrs.2025.34.1.003, 한국개발연구원 소속 저자)와 IMDA 샌드박스 분석 초록을 확인했다. PDF 는 압축 바이너리라 106쪽 구절은 검증 단계 원문 미열람. 초록은 하향식 기술 지원 성격과 부합한다. 발행 월은 KCI 페이지에 없다(브리프 2025-06)."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 구축자 의견."
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
      "f1~f3 의 AI Act 적용일(2026-07-27 발효, 2027-12-02, 2028-08-02)은 docs/topics/2026/2026-10-09-area43-s10.md 44행(ref-1322)과 같다 — 새 사실이 아니라 1차 근거 상향으로만 쓴다",
      "f6(기계류 AI 는 기계규정 경로)은 기존 위키의 '기계류 등 부속서 I 제품에 내장되면 2028-08-02'(2026-10-09-area43-s10.md 45행, categories/safety/index.md 149행, categories/ai-and-learning/index.md 131행)과 충돌한다. Cooley 해설도 기계류를 2028 예시로 든다 — 한쪽을 고르지 않고 둘 다 제시한다",
      "ref-1529(Directive (EU) 2024/2853, CELEX PDF URL)는 같은 날 2026-10-12-01 브리프의 ref-1490(같은 지침, ELI URL)과 같은 문서다. f43~f45 는 그 브리프 f5·f7 과 같은 내용이다",
      "f16(심사항목 16→8, 고시 2025-11-24 시행)은 2026-10-11-06 브리프 f13·f14(ref-1504·ref-1505)와 area50·area49 페이지에 이미 있다. 고시 번호 표기가 '제2025-21호'(이번)와 '제2025-021호'(기존)로 다르다",
      "f27~f29 의 24시간·72시간·14일·1개월 기한은 area59-s6, glossary/cyber-resilience-act.md, glossary/actively-exploited-vulnerability.md 에 이미 있다 — 기산점만 보탠다",
      "ref-1518(법률 제21311호 판)과 ref-620(원판), ref-1520(시행규칙 제7조의10)과 ref-1470(같은 시행규칙 제7조의4·5)은 같은 법령의 다른 판·조문이다 — 별도 id 유지, 관계 표기"
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f27·f28 의 '실제 악용 취약점'은 용어집 actively-exploited-vulnerability 의 '적극 악용 취약점'과 다르다",
      "f16·f17 의 고시 번호 '제2025-21호'(국가법령정보센터 표기)와 기존 area50·area49 페이지의 '제2025-021호'(산업통상부 누리집 표기)가 다르다",
      "f11~f15 의 '인공지능기본법'(법령 약칭) 표기는 기존 페이지·용어집 high-impact-ai 의 '인공지능 기본법'과 띄어쓰기가 다르다"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f14: [사실] → [추정]으로 강등한다. 제33조에 개정 표시가 없다는 점만 사실로 쓰고, '두 조의 의무는 원법(2026-01-22)부터 있었고 2026-07-21 은 두 조의 발효일이 아니다'는 추정으로 쓰며, 제35조①에 '<개정 2026. 1. 20.>' 표시가 있어 바뀐 문장의 시행일이 2026-07-21 일 수 있다는 단서와 원판(ref-620)·신구 대비표 미확인을 함께 적는다 — 열람한 판의 개정 표시가 단정을 뒷받침하지 않는다.",
    "f17: [사실] → [추정]으로 강등한다(4·7·11절의 고시 제8조①2호 문장) — 검증 단계에서 ref-1469 원문을 확인하지 못했고 대조할 자료도 없다. oq-187 은 열림으로 유지한다.",
    "7절 새 'EU AI Act·디지털 옴니버스' 행과 9절: f6 해석을 [추정]으로 쓰면서, 기존 위키 서술('기계류 등 부속서 I 제품에 내장되면 2028-08-02')도 지우거나 고르지 말고 함께 제시하고 oq-106 에 연결한다 — 기존 검증된 주장과 충돌하며 2차 해설(Cooley)도 엇갈린다. 다른 페이지(area43-s10, safety/index.md, ai-and-learning/index.md)는 이번 실행에서 고치지 않는다.",
    "f1~f3: 7절 행에서 날짜 셋은 2026-10-09-area43-s10.md 44행과 같은 내용의 1차 근거(ref-1517)임을 밝히고 새 발견처럼 서술하지 않는다 — 중복이다.",
    "f8: 위임법령은 조문 문언대로 '2028-08-02 까지 적용(shall apply by)'으로만 쓰고 '공표 기한'으로 바꾸지 않는다 — 해설의 표현이 엇갈린다.",
    "f43: 적용 시점은 '2026-12-08 후(정오표 2026-05-07, OJ L 2026/90364 기준), 곧 2026-12-09 에 출시·사용 개시된 제품부터'로 쓰고 '2026-12-08 이후'·'2026-12-08 부터'로 쓰지 않으며, 2026-10-12-01 실행이 58영역 페이지에 쓴 표현과 맞춘다 — 하루 차이로 뜻이 바뀐다.",
    "ref-1529: reference_updates 비고에 2026-10-12-01 의 ref-1490(같은 Directive (EU) 2024/2853, ELI URL)과 같은 문서임을 적어 퍼블리셔 병합 판단에 쓰게 한다 — 같은 주장에 다른 id 가 생긴다.",
    "f27·f28: '실제 악용 취약점'을 용어집 표기 '적극 악용 취약점'으로 바꾸고 첫 등장 시 용어집 페이지(glossary/actively-exploited-vulnerability.md)로 연결한다 — 용어 충돌.",
    "f16·f17: 고시 번호는 '산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)'처럼 두 표기를 한 번 병기한 뒤 같은 표기로 통일한다 — 기존 area50·area49 페이지와 표기가 다르다.",
    "f11~f15: 본문은 기존 표기 '인공지능 기본법'을 쓰고, 법령 약칭 '인공지능기본법'은 첫 등장 시 정식 명칭과 함께 한 번만 밝힌다 — 용어 일관성.",
    "f16: 공고 제2025-042호 첨부안의 '30일 이내 통보·16개→8개'는 행정예고안 기준임을 밝히고 최종 근거는 고시(ref-1469)로 두며, 별표 항목 대응은 area50 페이지 링크로만 처리한다. 5절의 '개정 시점·근거 고시 … 확인하지 못했다' 문장은 이 내용으로 바꾸되, 알림음·등화장치의 이동 여부가 미확인이라는 단서(oq-186 열림)는 남긴다.",
    "f18~f21: 5절 한국 사례 '제약' 칸의 가입금액은 '시행규칙 제7조의10 의 법령 기준 금액'으로 쓰고, 기존 '보장 한도는 미확인'(협회 단체보험 상품의 한도) 문장과 섞지 않으며 f23 의 지표 구분을 [의견]으로 붙인다 — 법령 기준과 상품 약관은 다른 지표다.",
    "f10·f15·f23·f26·f32·f40·f42·f48: [의견] 태그와 '(구축자 의견)'을 붙이고, ROP 기능이나 사업자의 법적 해당성(고영향 AI, CRA 제조자, 상업 사용 가능성 등)을 판정하는 문장으로 쓰지 않는다 — 출처가 판정하지 않는다.",
    "f41: [추정]에 '벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)'을 병기하고 다른 모델판·별도 계약은 미확인으로 둔다.",
    "f39: reuse lint 검사 항목은 '프로젝트 자체 변경기록(CHANGELOG v6.1.0 태그) 기준, 실행 재현 안 함'으로 밝힌다.",
    "f47: 8절 항목에 '제도 비교 연구이며 로봇 실증 연구가 아님'을 적는다.",
    "f31: CRA 오픈소스 범위는 조문이 아니라 전문 (18)에 근거함을 본문에 밝힌다.",
    "ref-1227·ref-1235: 이번 실행에서 다시 열지 않았으므로 각주의 접근일을 2026-09-30 그대로 둔다. 접근일을 2026-10-12 로 바꾸면 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다.",
    "페이지 본문의 직접 인용은 출처당 1회, 짧은 구절로 제한하고 나머지(특히 ref-1517 의 여러 조항)는 요약·재서술한다 — 5.3 인용 규칙.",
    "11절: oq-288 은 해결로 처리하고(근거 f18~f22), oq-143·oq-186·oq-187·oq-289·oq-291·oq-292 는 부분 근거만 적고 열림을 유지한다. 새 질문 5건은 id(oq-288~oq-292)로 표기하고, 새 열린 질문 2건(위임법령 채택, 보험 약관)을 관련 영역 번호와 이름을 함께 써서 등록한다.",
    "세부영역 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2, 7절 학습 데이터 라이선스 사례): 이번 브리프에 근거 finding 이 없으므로 7절에 반영하지 않고 제안 상태를 유지하며, 미반영 사유를 changelog_entry 에 적는다 — 브리프 밖 내용을 넣으면 드리프트다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 46건, 미확인 2건, 교차 확인 4건(f1~f4: AI 옴니버스 발효일·적용일·기계류 Section B 이동을 ERTICO·Hunton·Cooley·IBF 해설로 독립 확인). 강등: f14 사실 → 추정(제35조① 개정 표시로 원법부터의 의무라고 단정할 수 없음), f17 사실 → 추정(고시 제8조①2호 원문 미확인). 원문 미열람 출처: ref-1227, ref-1235(리서치 미재열람). 이번 검증 단계에서도 열지 못한 출처는 ref-1517·ref-1522·ref-1529·ref-1530(EUR-Lex 빈 본문 응답), ref-1519·ref-1469(접속 끊김), ref-1520(조문 본문 프레임 밖), ref-1531(PDF 판독 불가, KCI 서지·초록만 확인)이다. 이들은 검색 결과·2차 해설·이전 검증 실행(2026-10-11-06, 2026-10-12-01)과의 일치로 확인했다. 주의: 모든 사실 주장이 단일 1차 원문에 기대므로 신뢰도는 medium 이다. 기계류 로봇의 AI 요구가 AI Act 직접 적용이 아니라 기계규정 위임법령 경로를 따른다는 해석(f6)은 추정이며, 기존 위키의 '부속서 I 기계류 2028-08-02' 서술과 2차 해설이 엇갈려 둘 다 제시한다(oq-106). 시행규칙 제7조의10 금액은 법령 기준 금액이며 실제 보험 약관 한도가 아니다. oq-288 해결 인정(f18~f22). 정정 요청 없음. 2026-10-09-26 트랙 반영 제안(학습 데이터 라이선스 사례)은 브리프 근거가 없어 이번에는 반영하지 않는다. 검색 9회를 썼다.",
  "retry_reason": null
}
```

### docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md

```markdown
---
title: "59. 법·규제·보험·라이선스"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 59
related_areas: [3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66]
tags: [실외이동로봇 운행안전인증, 책임보험, 제조물책임, 사이버복원력법, SBOM, 오픈소스 라이선스]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-991, ref-1227, ref-1228, ref-1229, ref-1230, ref-1231, ref-1232, ref-980, ref-992, ref-1233, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-1212]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 59. 법·규제·보험·라이선스

# 59. 법·규제·보험·라이선스

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]

## 3. 왜 중요한가

로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1238][^ref-1237][^ref-1235][^ref-1228][^ref-1234][^ref-1227][^ref-1236]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 왜 중요한가](../../topics/2026/2026-09-30-area59-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다. (구축자 의견) [의견][^ref-980][^ref-1227][^ref-1228][^ref-1236]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area59-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 실외

**사례:** 한국 보도에서 실외이동로봇 운행

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 운행안전인증 대상은 배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합이다. [사실][^ref-980] 운용자는 로봇을 정확히 조작하고 안전하게 운용할 의무를 진다. [사실][^ref-991] |
| 제약 | 2023-11-17부터 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하 실외이동로봇이 보행자 지위로 보도를 통행할 수 있다. [사실][^ref-991][^ref-980] 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지켜야 한다. [사실][^ref-991] 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 한다. [사실][^ref-991][^ref-1232] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있다. [사실][^ref-991] 한국로봇산업협회 발표를 전한 기사(ref-1232) 기준으로, 협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고 첫 가입 기업은 뉴빌리티·로보티즈였다. 보장 한도는 미확인이다. [추정][^ref-1232] |

정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다(2023-11-16 발표). [사실][^ref-991] 운행안전인증은 서류심사→제품심사→인증표시 순으로 진행되고 신청일부터 30일 이내에 처리되며, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다(2026-09-30 확인). [사실][^ref-980]

제정 당시의 기준은 달랐다. 2023-07 산업통상자원부가 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다(2023-07 행정예고안 기준). [사실][^ref-992] 두 자료를 비교하면 심사 체계가 16가지 안전기준에서 현재 8개 심사항목으로 재편된 것으로 보이나, 개정 시점·근거 고시와 알림음·등화장치·경사로 같은 기존 기준이 어느 항목에 흡수됐는지는 확인하지 못했다. [추정][^ref-980][^ref-992]

**현장 유형:** 실외

**사례:** 미국 버지니아주에서 개인 배송 장치를 보도로 운행 (해외 비교)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 장치에 운영자를 식별하는 표시를 단다. [사실][^ref-1238] |
| 제약 | [개인 배송 장치](../../glossary/personal-delivery-device.md)(Personal Delivery Device, PDD)는 보도·횡단보도에서 시속 10마일 이하로 운행한다. [사실][^ref-1238] 운영자는 장치 운행으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지해야 한다. [사실][^ref-1238] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 버지니아주법 §46.2-908.1:1 기준이며(2026-09-30 확인), 지방정부는 추가 안전 요건을 둘 수 있다. [사실][^ref-1238] 미국 주법이므로 한국 현장에 바로 적용되지 않으며, 한국 사례와 운행 속도·보험 요구를 비교하는 해외 비교 사례로만 둔다.

이번 조사에서 근거를 찾은 현장 유형은 실외뿐이다. 물류창고·제조 공장·병원·상업 시설·가정의 사례는 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1228][^ref-1236]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area59-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1238][^ref-1227][^ref-1212][^ref-1228][^ref-1233][^ref-1235][^ref-1234][^ref-1237][^ref-1236][^ref-1229][^ref-1230][^ref-1231]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area59-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 대표 연구와 자료](../../topics/2026/2026-09-30-area59-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 업종별 조건 | 로봇별 인증·보험 상태와 인증 조건(관제장치 조합, 속도·질량·운행 구역)을 등록 정보와 작업·경로 제약으로 반영하고, 촬영 표시 같은 규제 상태를 운영 조건으로 확인한다. [추정][^ref-980][^ref-991][^ref-1234] | 인증 취득과 법적 적합성 판단(제조사·운영자), 보험 계약과 보상(운영자·보험사·협회), 제조물 책임 판정(당사자·법원), 개인정보 처리 적법성 판단(개인정보처리자)은 연계 대상으로 보인다. [추정][^ref-980][^ref-1232][^ref-1233][^ref-1227][^ref-1234] |
| 시설·설비 제어 | 사업장 안전검사 결과를 받아 작업·경로·권한 제약으로 반영한다. [추정][^ref-1237] | 산업용 로봇 안전검사는 사업주가 맡는 연계 대상으로 보인다. [추정][^ref-1237] |

분류 원문 19장의 [범위 경계](../../about/scope-boundary.md)는 업종별 조건에서 ROP가 "해당 조건을 작업·경로·권한 제약으로 반영"한다고 정한다. 이 영역에서 ROP는 법적 판단을 내리지 않고 그 결과를 받아 반영하며 근거 기록을 제공하는 쪽인 것으로 보인다. [추정][^ref-980][^ref-1237] 그 밖에 사고·취약점 보고와 책임 판단에 필요한 실행 기록을 남기는 일과 플랫폼 배포물의 라이선스·소프트웨어 자재명세서(Software Bill of Materials, SBOM) 목록을 관리하는 일은 ROP 직접 범위로 보인다. [추정][^ref-1228][^ref-1230][^ref-1236] 오케스트레이션 계층이 운행안전인증상 관제장치에 해당하면 경계가 달라질 수 있으나, 이에 대한 기준은 확인되지 않았다(oq-187).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1234][^ref-1228][^ref-1227]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area59-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 열린 질문 12건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 열린 질문](../../topics/2026/2026-09-30-area59-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md) — 영역 심화: 3~11절 첫 작성(seed → draft), 13절 각주 16건, 프런트매터 related_areas·tags·sources·confidence·last_run 채움(2차 수정: 열린 질문 12건, 구축자 의견 표시, 7절 각주 보강, SBOM 풀어쓰기, 8절 문장 정리) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area59-s7.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정: 요약 문장 각주 보강, ROS 2 행 표현, ENISA·SBOM 풀어쓰기) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 열린 질문](../../topics/2026/2026-09-30-area59-s11.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "11. 열린 질문" 절을 옮겼다(2차 수정: 기존 열린 질문 12건, oq-275·oq-279·oq-282 추가) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area59-s4.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 수정: 구축자 의견 표시, ENISA 풀어쓰기) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area59-s6.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "6. 대표 접근법과 기술" 절을 옮겼다(2차 수정: SBOM 풀어쓰기) (실행 2026-09-30-23)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1230]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1232]: 지디넷코리아, "실외 이동로봇 필수보험 94% 저렴하게", 2024-02-08, https://zdnet.co.kr/view/?no=20240208201432, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1233]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1234]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1235]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1236]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1237]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1238]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-1229]: ROS (ros-infrastructure/rep), REP 2004 -- Package Quality Categories, 2019-12-17, https://ros.org/reps/rep-2004.html, 접근일 2026-09-30
[^ref-1231]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-1212]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30 (원문 미열람)
```

### docs/categories/governance-law-and-society/index.md

```markdown
---
title: "P. 거버넌스·법규·사회"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-004, ref-009, ref-010, ref-031, ref-051, ref-076, ref-090, ref-104, ref-111, ref-125, ref-129, ref-130, ref-138, ref-159, ref-168, ref-199, ref-210, ref-230, ref-234, ref-238, ref-239, ref-240, ref-253, ref-283, ref-284, ref-286, ref-314, ref-315, ref-316, ref-317, ref-351, ref-353, ref-399, ref-405, ref-407, ref-408, ref-417, ref-465, ref-466, ref-470, ref-472, ref-473, ref-475, ref-476, ref-494, ref-516, ref-518, ref-531, ref-539, ref-541, ref-554, ref-559, ref-561, ref-567, ref-583, ref-589, ref-606, ref-607, ref-608, ref-618, ref-623, ref-625, ref-626, ref-635, ref-711, ref-712, ref-706, ref-709, ref-710]
---

[홈](../../index.md) › P. 거버넌스·법규·사회

# P. 거버넌스·법규·사회

## 핵심 질문

여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

## 개요

여러 사업자 사이의 책임·계약·데이터·API 정책, 법·규제·보험·라이선스, 노동 영향·수용성·접근성. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **58. 다사업자 책임·계약·데이터** | 책임과 변경 승인, 데이터 소유권, API 변경 정책, 서비스 수준·감사 이력 | 제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? | [58. 다사업자 책임·계약·데이터](multi-party-responsibility-contracts-and-data.md) | published |
| **59. 법·규제·보험·라이선스** | 법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 | 이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? | [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md) | published |
| **60. 노동·수용성·접근성** | 노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 | 로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? | [60. 노동·수용성·접근성](labor-acceptance-and-accessibility.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

책임 경계는 기술보다 먼저 정해야 한다. **누가 고치고, 누가 승인하고, 누가 배상하는지**가 정해지지 않으면 여러 사업자가 함께 운영할 수 없다. [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 G. 안전·보안·지능·거버넌스 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


G. 안전·보안·지능·거버넌스의 네 세부영역은 나머지 여섯 대분류의 세부영역에 공통 제약과 관리 체계로 걸린다. 아래 연결은 게시된 세부영역 페이지(48. 안전·위험 관리, 51. 인증·권한·격리, 47. AI·학습·적응과 모델 운영, 21. 상호운용 표준·적합성)와 A~F 대분류 페이지의 연결 서술을 같은 각주로 다시 인용한 것이다(기준일 2026-09-25). 연결마다 출처가 하나이거나 발행 주체가 같은 출처여서, 교차 확인된 연결은 아직 없다.

### A. 업무·공급망 설계

- [A. 업무·공급망 설계](../planning-and-business/index.md) — [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md): ISA-95 계열 작업 지시 동사·메서드(B2MML의 CHANGE·CANCEL, OPC UA for ISA-95 Job Control)를 VDA 5050·Open-RMF 주문·작업 요청과 잇는 표준 매핑이 확인되지 않았다. 따라서 번역 규칙을 누가 소유하고 변경을 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-129][^ref-130][^ref-031][^ref-125] 표준 매핑이 없다는 것은 조사 범위 안에서 관찰한 것이며, 부재가 확인되지는 않았다([oq-020](../../open-questions.md)).
- 같은 두 영역: 상위 업무 시스템에 여는 ROP API의 판 번호와 폐기 예고 정책은 ROP 몫으로 보인다. 그 규칙의 후보로 의미적 버전 관리(Semantic Versioning, SemVer 2.0.0)와 RFC 9745 Deprecation 헤더가 있다. [추정][^ref-635][^ref-706]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md): 주문·납기 제약을 받는 배정·계획 모델의 버전과 변경 승인은 ROP 몫으로 보인다. 수요예측 모델은 분류 원문 19장의 상위 업무 시스템 경계에 따라 연계 대상으로 보인다. [추정][^ref-626][^ref-618]

### B. 공통 정보·환경 모델

- [B. 공통 정보·환경 모델](../robot-ontology/index.md) — [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md): 대규모 언어 모델(Large Language Model, LLM)로 능력 온톨로지를 생성하는 연구(2024-04)가 있다. 로봇 기술 파일(URDF)에서 로봇 온톨로지를 LLM으로 채우는 연구(2026-06)도 있다. 분류 개정 전 원문 8장 교차 규칙의 매뉴얼 해석이 이 두 대분류를 잇는다. [사실][^ref-238][^ref-239]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md): 비전 언어 모델로 평면도 지도를 해석하는 연구(2024-09)가 있다. 교차 규칙의 도면 해석이 두 대분류를 잇는다. [사실][^ref-076]
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md): 제조사와 무관하게 쓰는 정보 모델 표준으로 세 가지가 있다. 무인운반차 기술 데이터 서브모델 IDTA 02047, 서비스 로봇 모듈 공통 정보 모델 ISO 22166-201(2024-02), 국내 KS B 7321-2다. [사실][^ref-234][^ref-240][^ref-138] KS 부합화 여부는 [oq-004·oq-026](../../open-questions.md)에서 열려 있다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md): ISO 21423은 산업용 이동로봇의 통신·상호운용성을 다루는 ISO 표준이다(검색 결과상 FDIS 단계, 발행 여부 미확인). 그 공통 좌표계와 제조사 지도 식별자가 어떻게 대응하는지는 확인되지 않았다. [사실][^ref-159] 관련 질문은 [oq-027](../../open-questions.md)이다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md): Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있다. 따라서 탑승을 확정하기 전에 최신 모드를 확인하는 규칙이 안전 조건과 맞물릴 것으로 보인다. 설비 안전 제어 자체는 연계 대상이다. [추정][^ref-286]

### C. 연결·실행 기반

- [C. 연결·실행 기반](../integration/index.md) — [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): 국가기술표준원은 2021-11 KS B 7317을 제정했다. 이 표준은 이동 로봇이 엘리베이터에 탑승할 때의 안전 요구사항과 평가 방법을 정한다. Open-RMF 승강기 상태의 운영 모드에는 화재·비상이 들어 있다. [사실][^ref-314][^ref-315][^ref-286] 승강기 탑승 안전과 설비 안전 제어 자체는 분류 원문 19장 시설·설비 제어 경계의 연계 대상이다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md): VDA 5050 3.0.0 상태 메시지의 safetyState는 비상정지 종류(eStop)와 보호 필드 침범(fieldViolation)을 보고한다. 명세는 스스로 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 적용해서는 안 된다고 밝힌다. [사실][^ref-031] ROP는 로봇이 보고한 안전 상태가 해제되고 운용 모드가 자동으로 돌아온 뒤 재개를 지시하는 운영 조율을 맡는다. 정지·재개 지시를 확실히 전달하는 문제는 29. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다. [추정][^ref-031] 원격 비상정지 지시 경로가 성능 수준 요구를 받는지는 [oq-095](../../open-questions.md)에서 열려 있다.
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)·[42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): ROS 2는 DDS 보안 규격의 인증·접근통제·암호화 플러그인을 쓴다. Open-RMF는 같은 신원과 접근통제 규칙을 공유하는 SROS 2 인클레이브(enclave)로 구성요소의 권한을 나눈다. 웹 대시보드에는 TLS(Transport Layer Security)와 OpenID Connect 기반 역할 토큰을 쓴다. [사실][^ref-009][^ref-405]
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 3.0.0에는 MQTT(Message Queuing Telemetry Transport)용 TLS 자격증명을 내려받는 사전 정의 동작 updateCertificate가 있다. 명세는 내려받기도 TLS로 보호하고, 인증서를 활성화하기 전에 인증서 체인을 검증하도록 권한다. [사실][^ref-031] 명세는 보안 기구 전체를 범위 밖에 둔다. 그래서 인증서 교체가 관제 연동 경로를 거치는 보안 명령이 된다는 것은 이 위키의 해석이다. [추정][^ref-031] 교체 시점·대상 승인과 실패 시 되돌림을 누가 책임지는지는 이번 실행에서 열린 질문으로 올렸다.
- 같은 두 영역: ROS 2 위협 모델 초안(최종 수정 2021-01)은 기본 사용자명·암호가 설정된 이미지에 SSH로 접속하는 경로를 진입점으로 든다. CISA 권고(ICSA-21-280-02)는 MiR 차량과 플릿 소프트웨어의 취약점으로 로봇 제어와 서비스 거부가 가능하다고 보고했다. [사실][^ref-010][^ref-583]
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서는 어느 관제 구성요소가 어떤 설비 명령을 낼 수 있는지를 정해야 할 것으로 보인다. 그 단위는 인클레이브·권한 파일 같은 접근통제 단위이며, 공개된 구성이나 사례는 확인되지 않았다. [추정][^ref-405][^ref-283][^ref-284] 관련 질문은 [oq-043·oq-056](../../open-questions.md)이다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 3.0.0은 경로 계산·교착 해소·교통 관리를 관제 기능으로, 위치 추정과 주문 실행을 이동로봇 기능으로 나눈다. 제조사 중립 연동의 기준은 VDA 5050 말고도 MassRobotics AMR 상호운용 표준과 ISO 21423이 있다. ISO 21423은 산업용 이동로봇의 통신·상호운용성을 다루는 ISO 표준이다(검색 결과상 FDIS 단계, 발행 여부 미확인). [사실][^ref-031][^ref-253][^ref-159]
- 같은 두 영역: 확인한 VDA 5050 적합성 시험 근거는 제3자 오픈소스 도구와 벤더 발표뿐이다. 따라서 어느 시험 결과를 연동 승인 기준으로 삼고, 누가 연동 오류를 판정할지가 거버넌스 과제로 넘어갈 것으로 보인다. 공식 인증 절차가 없다는 것은 확정되지 않았다. [추정][^ref-407][^ref-408][^ref-031] OTTO는 2026-04 VDA 5050 인증을 추가했다고 발표했으나, 시험 항목은 확인되지 않았다. [추정] 벤더 주장[^ref-608] 관련 질문은 [oq-055](../../open-questions.md)다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): 국내에서는 로봇 엘리베이터 탑승 KS가 제정되었다. 대한승강기협회가 엘리베이터와 로봇 연동 단체표준을 제정했다는 기사도 있어, 설비 연동 표준이 두 대분류를 잇는 것으로 보인다. 단체표준의 원문과 발행일은 확인되지 않았다. [추정][^ref-709][^ref-316][^ref-317] 메시지 내용은 [oq-041](../../open-questions.md)에서 열려 있다.
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): 오픈소스 ROS-MCP-Server는 rosbridge를 통해 ROS 기능을 LLM에게 도구로 노출한다. 노출하는 기능은 토픽 발행·구독, 서비스·액션 호출, 파라미터 설정이다. README는 권한 기능을 앞으로 기여받을 기능으로만 언급한다(2026-09-25 확인). [사실][^ref-712]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)·[51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md): 다음 판단은 트랙 [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)의 실행 2026-09-25-71([단계 3](../../tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md))에서 이 위키가 종합한 것이다. LLM에 저수준 로봇 도구를 직접 열면 명령 상태 관리와 실행 전 검증을 우회할 수 있다. 그래서 ROP는 검증 경로로 들어가는 상위 도구(작업 요청 제출 등)만 노출해야 할 것으로 보인다. [추정][^ref-712][^ref-417] 출처는 도구 노출 방식과 실행 전 안전 게이트가 있다는 것만 뒷받침한다. 이 판단은 게시 전인 트랙 추정이다.
- 같은 두 영역: Tang 외(2026-06)는 산업용 다중 로봇을 위한 구조를 제안했다. 에이전트의 제안은 결정적 검증과 원자적 반영(atomic commit)을 거쳐야만 실행 상태·자원 잠금 기록에 받아들여진다. [사실][^ref-711] 이 연구는 산업용 다중 로봇을 대상으로 한 프리프린트이며, 물류 적용은 확인되지 않았다. 원문을 열지 못해 제안 주체가 LLM 에이전트로 한정되는지도 확인하지 않았다.
- C. 연결·실행 기반 페이지는 47. AI·학습·적응과 모델 운영과의 연결을 '근거 없음'으로 두었다. 위 세 항목은 그 페이지를 보강할 후보이며, 이번 실행에서는 C. 연결·실행 기반 페이지를 고치지 않았다.

### D. 계획·최적화

- [D. 계획·최적화](../planning-and-optimization/index.md) — [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md): 분류 개정 전 원문 8장 교차 규칙에 따라 학습 기반 배차 연구가 두 영역을 잇는다. 이종 그래프 어텐션 스케줄러, 창고 강화학습 배정 RTAW, LLM 기반 다중 로봇 작업 배정 연구가 그 예다. [사실][^ref-399][^ref-623][^ref-090][^ref-168] LLM 배정 결과 수치는 출처가 서로 달라([oq-030](../../open-questions.md)) 싣지 않는다.
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)·[28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md): 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있다. 자율 피킹 로봇의 배터리 관리에 심층 강화학습을 쓰는 연구(2026-07)도 있다. [사실][^ref-199][^ref-531] 이 연구들로 보아 학습 기반 방법이 경로·충전 계획에도 들어와 두 대분류를 잇는 것으로 보인다. 두 연구 모두 프리프린트다. [추정][^ref-199][^ref-531]
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md): 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고했다. 이 연구는 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했으며, 실험은 GPS 스푸핑 데이터와 택시 수요로 했다. [사실][^ref-494] 물류센터 적용은 확인되지 않았다. 배정 전에 보고값을 검증하는 기준은 [oq-082](../../open-questions.md)에서 열려 있다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): VDA 5050 3.0.0은 여러 구역 유형을 교통 관리 수단으로 정의한다. 진입 금지(BLOCKED)·해제(RELEASE)·속도 제한(SPEED_LIMIT)·우선(PRIORITY)·벌점(PENALTY) 같은 유형이다. 그러면서도 명세는 안전 표준으로 적용하지 말라고 밝힌다. [사실][^ref-031] Open-RMF는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004]
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md): Open-RMF 데모는 비상 경보가 켜지면 로봇들을 가장 가까운 주차 위치로 보낸다. 2025-04-04 기능 요청 이슈를 기준으로 하면, 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었다. [사실][^ref-104][^ref-567] 그 뒤 구현 여부는 확인되지 않았다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): VDA 5050은 교통 조율 전략을 명세에서 뺀다. Open-RMF에서는 시스템 통합사가 배치한 판정자가 협상 결과를 고른다. 따라서 한 현장의 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-031][^ref-004] 관련 질문은 oq-057이다.

### E. 협업·현장 운영

- [E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md) — [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md): ANSI/A3 R15.08-2-2023은 이동 플랫폼에 로봇팔을 단 모바일 매니퓰레이터를 산업용 이동로봇 유형 C로 다룬다. 이 표준은 시스템·적용 단위의 안전 요구를 정한다. [사실][^ref-210][^ref-472] 국내 대응 KS는 [oq-064](../../open-questions.md)에서 열려 있다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)·[31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 사람 감지·보호 필드·비상정지 같은 안전 기능은 제조사·통합사·설비 쪽의 연계 대상으로 보인다. ROP는 로봇이 보고한 안전 상태를 표시하고, 재개와 수동 전환 승인을 작업 흐름에 반영하는 쪽을 맡는 경계로 보인다. [추정][^ref-470][^ref-051][^ref-210]
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 국내에서는 고용노동부가 2023-07 고정식·이동식 산업용 로봇의 협동작업 안전 가이드를 배포했다. 중소벤처기업부는 2024-11 이동식 협동로봇 안전기준 산업표준을 제정했다고 발표했다. [사실][^ref-473][^ref-475][^ref-561] 제정된 KS의 번호와 내용은 [oq-070](../../open-questions.md)에서 열려 있다.
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)·[48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 관련 연구로 세 가지가 있다. LLM 계획기가 불확실할 때 사람에게 되묻는 연구(KnowNo, 2023-07), 사용자 명령의 모호성을 해소하는 연구(CLARA, 2024), 자연어 명령을 실행하기 전에 거치는 안전 게이트 연구(SafeGate, 2026-04)다. [사실][^ref-351][^ref-353][^ref-417] 세 연구의 실험 환경은 물류 현장이 아니다.
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): Das 외(2021-01)는 로봇 실패 설명을 생성해 사용자의 고장 복구 지원을 개선하는 연구를 발표했다. [사실][^ref-476] 이 연구는 분류 개정 전 원문 8장 교차 규칙의 장애 분석에 해당하며, 두 대분류를 잇는 근거로 보인다. [추정][^ref-476]
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): VDA 5050 오류 수준, MassRobotics 운용 상태, Open-RMF 작업 상태는 서로 다른 어휘이고, 셋을 잇는 공통 매핑 표준은 확인되지 않았다. 따라서 이종 플릿의 오류·원인 범주 해석 규칙을 누가 정하고 바꾸는지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-051][^ref-230][^ref-111] 관련 질문은 oq-033·oq-073이다.
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md): 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 안의 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다(해당 호 번호는 미확인). [사실][^ref-589] ROS 2 위협 모델 초안은 카메라 영상을 사적 데이터로 분류한다. [사실][^ref-010] 따라서 카메라를 단 로봇이 작업자를 촬영하는 현장에서는 영상 수집 조건이 사람–로봇 협업의 제약이 될 것으로 보인다. [추정][^ref-589][^ref-010] 어느 규정이 적용되는지는 [oq-099](../../open-questions.md)에서 열려 있다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): 비상이 해제된 뒤 어떤 작업을 어떤 순서로 재개할지, 대상 플릿을 어떻게 구분할지가 출하 마감 준수에 영향을 준다. 그래서 비상 대응 뒤의 재개는 예외 복구 과제로 넘어가는 것으로 보인다. [추정][^ref-567][^ref-004]
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): 출하 마감 중에 오류 로봇을 제조사 원격 유지보수로 복구하는 상황이 있다. 이때 대상 로봇과 진단 명령만 허용하고, 이동 명령은 막고, 세션을 감사 기록으로 남기는 권한 제약이 복구 속도와 맞물릴 것으로 보인다. [추정][^ref-010][^ref-583][^ref-405] 로봇·명령 단위 권한 매트릭스를 정한 공개 표준은 [oq-100](../../open-questions.md)에서 열려 있다.
- E. 협업·현장 운영 페이지는 51. 인증·권한·격리와의 연결을 '근거 없음'으로 두었다. 위 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성 연결 두 건은 그 페이지를 보강할 후보이며, 이번 실행에서는 E. 협업·현장 운영 페이지를 고치지 않았다.

### F. 도입·검증·유지관리

- [F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md) — 연계 대상: [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)·[54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md): ISO 3691-4:2023은 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하고, 운용 구역 준비를 부속서 A에 둔다. [사실][^ref-470] 이는 로봇 자체 안전 기능 쪽 내용이며, 세부 시험 항목은 확인되지 않았다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md): 업체(세이프틱스) 자료는 설비·작업을 바꿀 때 위험성평가를 다시 하도록 권한다. 이로 보아 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가를 촉발하는 조건이 될 수 있어 보인다. 근거는 이 업체 자료 하나뿐이며, 국내 공식 규정은 확인되지 않았다. [추정][^ref-559] 관련 질문은 [oq-092·oq-093](../../open-questions.md)이다.
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md): IEC TR 62443-2-3:2015는 산업 자동화·제어 시스템 환경의 패치 관리를 다룬다. ROS 2 위협 모델 초안은 빌드 팜과 개발자 작업 환경을 거치는 공급망 위협에 대한 완화책으로 바이너리 서명과 소스 감사를 든다. [사실][^ref-554][^ref-010]
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)·[54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md): 자연어 능력 설명에서 LLM으로 능력 온톨로지를 생성하는 방법(2024-06)이 제안되었다. ALFRED와 LoTa-Bench는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과로 자동 평가하는 공개 벤치마크다. 두 벤치마크는 물류 지시 데이터셋이 아니다. [사실][^ref-465][^ref-539][^ref-541] 분류 개정 전 원문 8장 교차 규칙의 매뉴얼 해석이 55. 현장 조사·설치·시운전에 적용되는 예다.
- [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md): 57. 자산·소프트웨어 수명주기 관리의 정의에는 모델 버전과 배포·복구가 들어 있다. 따라서 학습 배차 모델을 교체할 때 모델 레지스트리의 버전·별칭과 운영 준비도 시험 기준으로 관리하는 일이 두 대분류를 잇는 것으로 보인다. [추정][^ref-626][^ref-625] 이 연결은 아직 어느 대분류 페이지에도 없다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md): 제조용 디지털 트윈 프레임워크 ISO 23247은 국내에 KS X ISO 23247-1로 등재되어 있다. 2026년에는 디지털 트윈 결합을 다루는 Part 6이 발행되었다. 다만 이 표준은 제조를 대상으로 한다. [사실][^ref-516][^ref-518] 물류센터에 적용할 수 있는지는 [oq-085](../../open-questions.md)에서 열려 있다. 이 연결은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽이며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과는 구분한다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md): 국내에는 로봇 자체 성능 시험(KS B ISO 18646-1, 한국로봇산업진흥원 시험평가)이 있다. 소프트웨어 모듈 정보모델의 상호운용성 시험 절차(KOROS 1148-8:2025)도 있다. 로봇 성능 시험은 시험기관이 맡고, ROP는 그 결과를 연동 승인·등록 조건으로 받는 쪽으로 보인다. [추정][^ref-606][^ref-607][^ref-710][^ref-466] 관련 질문은 [oq-089·oq-111](../../open-questions.md)이다.
- [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md): 관제는 VDA 5050 헤더의 version으로 판 차이를 감지한다. 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러난다. 따라서 펌웨어·프로토콜 판을 이행할 때 호환 시험과 수정 책임을 누가 지는지가 두 대분류 사이의 과제로 보인다. [추정][^ref-031][^ref-051][^ref-635] 관련 질문은 [oq-091](../../open-questions.md)이다.

### 아직 다루지 않은 연결

다음 연결은 아직 근거를 찾지 못해 쓰지 않았다.

- 42. 분산 시스템·통신·컴퓨팅 구조 ↔ 48. 안전·위험 관리, 47. AI·학습·적응과 모델 운영
- 17. 작업 대상·자산 식별과 인계 추적 ↔ 48. 안전·위험 관리, 51. 인증·권한·격리, 47. AI·학습·적응과 모델 운영, 21. 상호운용 표준·적합성
- 26. 작업 순서·스케줄링 ↔ 48. 안전·위험 관리, 51. 인증·권한·격리, 47. AI·학습·적응과 모델 운영, 21. 상호운용 표준·적합성
- 24. 작업·워크플로 모델링, 35. 처리능력·규모·배치 설계, 39. 운영 성과 측정·개선 ↔ 48. 안전·위험 관리, 51. 인증·권한·격리

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-076]: DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps, 2024-09, https://arxiv.org/abs/2409.12842, 접근일 2026-09-25 (원문 미열람)
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25 (원문 미열람)
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-09-25 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-199]: arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-25 (원문 미열람)
[^ref-210]: ANSI / A3(Association for Advancing Automation), ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s), 2023, https://webstore.ansi.org/standards/ria/ansia3r15082023, 접근일 2026-09-25 (원문 미열람)
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25 (원문 미열람)
[^ref-234]: IDTA(Industrial Digital Twin Association), IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-09-25 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-09-25 (원문 미열람)
[^ref-240]: ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules, 2024-02, https://www.iso.org/standard/82334.html, 접근일 2026-09-25 (원문 미열람)
[^ref-253]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — README, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25 (원문 미열람)
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-314]: 국가표준인증통합정보시스템(KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2021-11, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-09-25 (원문 미열람)
[^ref-315]: 산업통상자원부 국가기술표준원(대한민국 정책브리핑), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-316]: 건설기술신문, 승강기협, 엘리베이터-로봇 연동 단체표준 제정, 미확인, https://www.ctman.kr/35296, 접근일 2026-09-25 (원문 미열람)
[^ref-317]: 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 미확인, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-353]: Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S., CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents, 2024, https://arxiv.org/abs/2306.10376, 접근일 2026-09-25 (원문 미열람)
[^ref-399]: Wang, Z., & Gombolay, M., Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints, 미확인, https://link.springer.com/article/10.1007/s10514-021-09997-2, 접근일 2026-09-25 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-465]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions, 2024-06, https://arxiv.org/abs/2406.07962, 접근일 2026-09-25 (원문 미열람)
[^ref-466]: 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’, 2026-07-24, https://www.busan.com/view/busan/view.php?code=2026072420194685883, 접근일 2026-09-25 (원문 미열람)
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-09-25 (원문 미열람)
[^ref-472]: A3(Association for Advancing Automation), ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available, 2023-10, https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available, 접근일 2026-09-25 (원문 미열람)
[^ref-473]: 고용노동부, 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포, 2023-07, https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065, 접근일 2026-09-25 (원문 미열람)
[^ref-475]: 중소벤처기업부(대한민국 정책브리핑), ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!, 2024-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517, 접근일 2026-09-25 (원문 미열람)
[^ref-476]: Das, D., Banerjee, S., & Chernova, S., Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery, 2021-01, https://arxiv.org/abs/2101.01625, 접근일 2026-09-25 (원문 미열람)
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-09-25 (원문 미열람)
[^ref-516]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010140724, 접근일 2026-09-25 (원문 미열람)
[^ref-518]: ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition, 2026, https://www.iso.org/standard/87426.html, 접근일 2026-09-25 (원문 미열람)
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-539]: askforalfred (ALFRED 공식 저장소), ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README), 미확인, https://github.com/askforalfred/alfred, 접근일 2026-09-25 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-09-25 (원문 미열람)
[^ref-554]: IEC, IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment, 2015-06, https://webstore.iec.ch/en/publication/22811, 접근일 2026-09-25 (원문 미열람)
[^ref-559]: 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드, 미확인, https://doc.safetics.io/insight-risk-assessment/, 접근일 2026-09-25 (원문 미열람)
[^ref-561]: 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어, 2024-11-03, https://www.korea.kr/news/policyNewsView.do?newsId=148935814, 접근일 2026-09-25 (원문 미열람)
[^ref-567]: Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf, 2025-04-04, https://github.com/open-rmf/rmf/issues/658, 접근일 2026-09-25 (원문 미열람)
[^ref-583]: CISA, Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02), 미확인, https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02, 접근일 2026-09-25 (원문 미열람)
[^ref-589]: 법제처 국가법령정보센터, 근로자참여 및 협력증진에 관한 법률, 미확인, https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636, 접근일 2026-09-25 (원문 미열람)
[^ref-606]: 한국표준협회 KSSN(국가표준인증종합정보센터), KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010113281, 접근일 2026-09-25 (원문 미열람)
[^ref-607]: 한국로봇산업진흥원(KIRIA), 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼, 미확인, https://kiria.org/rp/kiria/tva/inr/page.dn, 접근일 2026-09-25 (원문 미열람)
[^ref-608]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-09-25 (원문 미열람)
[^ref-618]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-623]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-09-25 (원문 미열람)
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry | MLflow AI Platform, 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)
[^ref-635]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25 (원문 미열람)
[^ref-711]: Tang, G. 외(arXiv 2606.31339), Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems, 2026-06, https://arxiv.org/abs/2606.31339, 접근일 2026-09-25 (원문 미열람)
[^ref-712]: robotmcp (ROS-MCP-Server 공식 저장소), ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README), 미확인, https://github.com/robotmcp/ros-mcp-server, 접근일 2026-09-25
[^ref-706]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-710]: 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차, 2025-06-04, http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223, 접근일 2026-09-25 (원문 미열람)

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 125건이다(논문 25건 · 기사·보고서 11건 · 업체 발표 7건 · 표준·오픈소스·기관 자료 82건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-494](../../references/ref-494.md) — Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems (발행 2026-08)
- [ref-531](../../references/ref-531.md) — arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers (발행 2026-07)
- [ref-711](../../references/ref-711.md) — Tang, G. 외(arXiv 2606.31339), Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems (발행 2026-06)
- [ref-239](../../references/ref-239.md) — Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF (발행 2026-06)
- [ref-1208](../../references/ref-1208.md) — Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong? (발행 2026-05-01)
- [ref-417](../../references/ref-417.md) — Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems (발행 2026-04)
- [ref-1226](../../references/ref-1226.md) — Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety (발행 2026)
- [ref-168](../../references/ref-168.md) — Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms (발행 2025-12)
- [ref-1488](../../references/ref-1488.md) — De Noyette, E., Ståhler, L., Margoni, T. (IIC 56(5)), Data Secrets: The Data Act's New Trade Secrets Framework (발행 2025-04-24)
- [ref-199](../../references/ref-199.md) — arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding (발행 2024-10)
- 그 밖에 15건

**기사·보고서**

- [ref-1211](../../references/ref-1211.md) — 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까 (발행 2026-09-14)
- [ref-466](../../references/ref-466.md) — 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ (발행 2026-07-24)
- [ref-1227](../../references/ref-1227.md) — Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains (발행 2026-03-23)
- [ref-1215](../../references/ref-1215.md) — 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인) (발행 2025-04-01)
- [ref-1222](../../references/ref-1222.md) — 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파 (발행 2025-01-21)
- [ref-1233](../../references/ref-1233.md) — 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점 (발행 2024-07-05)
- [ref-1232](../../references/ref-1232.md) — 지디넷코리아, "실외 이동로봇 필수보험 94% 저렴하게" (발행 2024-02-08)
- [ref-992](../../references/ref-992.md) — 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (발행 2023-07-28)
- [ref-1193](../../references/ref-1193.md) — 지디넷코리아, 산업데이터 만든 자에게 사용·수익권 부여 (발행 2022-03-15)
- [ref-317](../../references/ref-317.md) — 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 (발행 미확인)
- 그 밖에 1건

**업체 발표**

- [ref-1496](../../references/ref-1496.md) — Formant, General Terms (발행 2026-04-16)
- [ref-608](../../references/ref-608.md) — OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments (발행 2026-04)
- [ref-1493](../../references/ref-1493.md) — 1X Technologies, Inc., Pre-Order Terms (발행 2025-10-28)
- [ref-1491](../../references/ref-1491.md) — Relay Robotics, Terms of Service (Exhibit A: Service Level Agreement) (발행 2023-03-01)
- [ref-1492](../../references/ref-1492.md) — Amazon Web Services, AWS IoT RoboRunner Service Level Agreement (발행 2022-11-28)
- [ref-559](../../references/ref-559.md) — 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드 (발행 미확인)
- [ref-1487](../../references/ref-1487.md) — Best Epoch Technology Co., Ltd. (AIRROBO), EU DATA ACT Notice (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-1228](../../references/ref-1228.md) — European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations (발행 2026-09-11)
- [ref-1495](../../references/ref-1495.md) — SingHealth / Changi General Hospital CHART, RoMi-H Empanelment Programme 2026 (발행 2026-05-06)
- [ref-1217](../../references/ref-1217.md) — 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행 (발행 2026-01-28)
- [ref-1235](../../references/ref-1235.md) — 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무 (발행 2026-01-21)
- [ref-518](../../references/ref-518.md) — ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition (발행 2026)
- [ref-1191](../../references/ref-1191.md) — European Commission (Shaping Europe's digital future), Data Act explained (발행 2025-12-15)
- [ref-1489](../../references/ref-1489.md) — European Commission, ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final (발행 2025-11-19)
- [ref-1192](../../references/ref-1192.md) — European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (발행 2025-11-19)
- [ref-1213](../../references/ref-1213.md) — George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk (발행 2025-08-26)
- [ref-710](../../references/ref-710.md) — 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 (발행 2025-06-04)
- 그 밖에 72건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-12 · 갱신 · [58. 다사업자 책임·계약·데이터](multi-party-responsibility-contracts-and-data.md) — 차등 갱신: 4절 데이터 보유자 정의를 데이터법 원문(제4조(13)·제2조(17))으로 바로잡고 2026-09-30 분리 페이지 연결 복구, 5절 병원 사례의 '연 2회'를 원어와 두 해석으로 고치고 2025·2026 등재를 연차별로 나눔, 가정 청소 로봇 데이터 공유 사례 추가, 6절 데이터법 적용 시점·SCC 면책(추정)·제조물책임지침 조문·공개 약관 비교(벤더 주장)·영상 위탁 관리 보강과 2026-09-30 분리 페이지 연결, 7절 요약 문장에 제조물책임지침·RFC 9745 추가와 표 3행, 8절 논문 1건, 11절 실행별 질문 건수 정정·부분 근거·새 질문 3건, 13절 각주 갱신(ref-872 원문 열람, ref-1488 원문 미열람) (실행 2026-10-12-01)
- 2026-10-12 · 생성 · [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area58-s6.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "6. 대표 접근법과 기술" 절(4,483자)을 옮겼다 (실행 2026-10-12-01)
- 2026-10-12 · 생성 · [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-10-12-area58-s11.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "11. 열린 질문" 절(1,186자)을 옮겼다 (실행 2026-10-12-01)
- 2026-10-12 · 생성 · [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area58-s7.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,029자)을 옮겼다 (실행 2026-10-12-01)
- 2026-10-12 · 생성 · [58. 다사업자 책임·계약·데이터 — 대표 연구와 자료](../../topics/2026/2026-10-12-area58-s8.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "8. 대표 연구와 자료" 절(774자)을 옮겼다 (실행 2026-10-12-01)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24
```

### data/area_reflection_proposals.json (대상 영역 59. 법·규제·보험·라이선스 에 대한 트랙 반영 제안 1건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-10-09-26",
      "date": "2026-10-09",
      "track": "floorplan-recognition",
      "stage": 2,
      "area_no": 59,
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "summary": "공공 AI 학습 데이터(AI허브) 원 이용정책과 다른 데이터셋 페이지 2차 기술의 차이, CC BY-NC-SA 4.0 평면도 데이터셋의 상용 이용 제약을 학습 데이터 라이선스 사례로(f4, f5, f6, f7). 법적 판단 아님.",
      "status": "제안"
    }
  ]
}
```

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "17. 작업 대상·자산 식별과 인계 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
area_no: {{area_no}}                        # 1~67 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [18, 29, 30]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개. 예: [EPCIS, 인계 확인, 자산 추적]. 시드면 []
status: {{status}}                          # seed | draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여. 시드면 이 줄을 뺀다
created: {{created}}                        # YYYY-MM-DD. 페이지를 처음 만든 날
updated: {{updated}}                        # YYYY-MM-DD. 마지막으로 내용을 바꾼 날
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id. 예: [ref-003, ref-021]. 없으면 []
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜 YYYY-MM-DD. 시드면 이 줄을 뺀다
version: {{version}}                        # 정수. 시드 1, 갱신마다 +1
---
<!--
[템플릿] 세부 연구영역 페이지 (type: area)
경로: docs/categories/<대분류 slug>/<영역 slug>.md  (아래 경로 규약 표. 2026-09-28 개정부터 폴더·파일 이름에 대분류 문자·영역 번호를 붙이지 않는다)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석, C. 채팅 기반 구성·운영의 엔진 짝 주석), 1절 아래 "이 영역이 다루는 일(2026-09-28 리스트업 기준)" 목록(data/area_items.json)과 옛 영역에서 이어받은 경우의 계보 안내(data/area_lineage.json)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

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

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/<트랙 slug>/index.md(예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition) 이다.
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
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 67페이지(예: docs/categories/robot-ontology/robot-capability-and-task-representation.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 로봇 온톨로지):
!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 67페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]

{{area_items_block}}
<!--
첫 내용 줄: 분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않는다. 원문 주석(현재 원문)은 이 절이 아니라 2절의 인용 블록에 둔다.
{{area_items_block}}: 시드가 넣은 위키 문구를 그대로 둔다(pipeline/scaffold.py area_items_block). (1) "이 영역이 다루는 일(2026-09-28 리스트업 기준):" 과 그 아래 "- **일 이름**: 정의" 목록(data/area_items.json), (2) 옛 영역에서 일부를 이어받은 영역이면 계보 안내 문장(data/area_lineage.json), (3) 옛 영역 본문을 이어받은 영역이면 옛 영역 안내 문장과 옛 정의·질문·주석 인용 블록("> 옛 정의: … [옛 분류원문]", "> 옛 질문: … [옛 분류원문]", "> 옛 원문 주석: … [옛 분류원문]"). 옛 인용 블록은 보관한 옛 원문(_source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)과 글자 단위로 같아야 하며(protect_source.py check_tagged_lines), 이력 기록이므로 에이전트가 고치거나 새 문장을 [옛 분류원문] 으로 태그하지 않는다. 해당 내용이 없는 영역은 이 자리 표시 줄을 지운다.
이 절의 원문 문장과 옛 원문 인용은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. 핵심 질문

{{core_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 세부영역 표의 "핵심 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]". 수정 금지. (대분류 페이지의 핵심 질문과 다른 문장이다. 소속 대분류의 핵심 질문은 H1 아래 admonition 에 둔다.)
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 해당 영역(2026-09-28 원문 기준): 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 36. 가상 시운전·실제 상황 재현, 38. 모니터링·이상 탐지·원인 분석, 55. 현장 조사·설치·시운전. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14~16번의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석("매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번"), C. 채팅 기반 구성·운영의 엔진 짝 주석("맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번").
굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다. 문단이 여럿인 영역(예: 14. 도면·BIM에서 지도 만들기는 셋, 15. 지도·공간·위치 모델과 25. 작업 배정 — MRTA는 둘)은 인용 블록도 원문 순서대로 그 수만큼 둔다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다. 정확한 목록은 pipeline/lib/source.py 의 area_notes(번호)가 정한다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 ROP를 구현·운영할 때 무엇이 막히는지, 로봇 개별 성능과 업무 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 핵심 질문에서 출발한다. 특정 현장 유형(예: 물류창고)에만 해당하는 이야기로 좁히지 말고, 현장 유형에 따라 달라지는 점이 있으면 어느 현장 유형인지 밝힌다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "VDA 5050(독일자동차산업협회 무인운반차 인터페이스)", "WMS(Warehouse Management System, 창고 관리 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** {{site_types}}
<!-- 이 사례가 놓이는 현장 유형을 분류 원문 21장의 일곱 가지(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 가운데 하나로 명시한다. 예: "병원". 물류창고는 일곱 현장 유형 가운데 하나일 뿐이므로 기본값으로 쓰지 않고, 브리프 근거가 있는 현장 유형을 고른다. 물류창고 사례라면 입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 중 어느 단계인지를 사례 제목이나 서술에 덧붙일 수 있다. -->

**사례:** {{case_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "병원에서 검체를 검사실로 운반", "제조 공장에서 공정 사이 부품 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
여섯 항목은 분류 원문 21장의 정의를 따른다. 시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가? / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가? / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가? / 제약: 시간·공간·적재량·설비·권한·안전 제약은 무엇인가? / 완료·인계: 무엇이 확인돼야 일이 끝났다고 인정하는가? / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?
표 아래에 1~3단락으로 사례를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 실제 도입 사례는 출처 각주와 함께 쓰고, 설명용 가상 사례이면 첫 문장에 밝힌다(예: "다음은 설명을 위한 가상의 사례이다."). 지어낸 현장 수치는 쓰지 않는다.
사례가 여럿이면 "**현장 유형:** … / **사례:** … / 여섯 항목 표 / 서술" 묶음을 사례마다 반복한다(서로 다른 현장 유형의 사례를 우선한다). 2026-09-28 개정 전에 쓴 물류창고 시나리오는 "현장 유형: 물류창고" 사례로 유지한다.
다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 함께 낸다(항목마다 site_type·item·link·title. 대분류는 퍼블리셔가 link 에서 정한다). 현장 유형 매트릭스 페이지: ../../site-matrix.md
-->

## 6. 대표 접근법과 기술

{{approaches}}
<!--
소제목(###)별로 접근법을 2~5개 정리한다. 각 접근법: 무엇을 해결하는가, 어떻게 동작하는가, 한계는 무엇인가. 주장마다 태그·각주.
벤더 제품의 기능·성능은 [추정]에 "벤더 주장"을 병기한다. 표·그림은 복제하지 않고 필요하면 mermaid 로 직접 그린다.
-->

## 7. 관련 표준·프레임워크·오픈소스

{{standards}}
<!--
표 형식: | 이름 | 유형(표준 / 오픈소스 / 평가 프로그램 / 프레임워크) | 이 영역과의 관계 | 출처 |. 각 행의 출처 칸에 각주.
표준·규격은 발행 기관의 공식 자료를 근거로 하고, 원문을 못 열었으면 "원문 미열람"을 표기한다. 대체·개정된 표준은 현재 버전을 확인해 기준일을 쓴다. 표준 목록 페이지(../../standards/index.md)와 용어집 링크를 함께 둔다.
-->

## 8. 대표 연구와 자료

{{key_research}}
<!--
목록 형식: "- 저자 또는 기관, 제목(연도) — 한두 문장 요약과 이 영역에서의 의미. [태그][^ref]". 3~8건. 학술 논문·표준·정부·연구기관 보고서를 우선하고 기사·벤더 문서는 보조로 둔다.
-->

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 현장 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 19장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장"(같은 대분류 E. 사물·사람·실시간 상태 안의 예). 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 L. AI·학습 기술의 해당 영역(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)을 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 영역이면 짝이 되는 엔진 영역(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 연결한다. 현장 유형별 요구·도입 사례는 Q. 현장 유형별 적용의 해당 영역(61. 물류창고 ~ 67. 기타 현장)을 연결한다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/<트랙 slug>/index.md. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/<트랙 slug>/question-backlog.md)로 링크만 둔다.
출처가 충돌한 주장, 확인하지 못한 수치, "분류 확장 제안"은 여기에 질문으로 올린다.
-->

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:area-recent:end -->
<!-- 퍼블리셔가 이 영역을 다룬 실행과 주제 페이지를 최신순으로 넣는다(날짜 | 실행 id | 변경 요약 | 페이지 링크). 스토리텔러는 마커 사이를 건드리지 않는다. -->

## 13. 참고 자료 (각주)

{{footnotes}}
<!--
각주 정의만 둔다. 형식: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"(공통 규칙 9). 본문에서 쓴 각주는 모두 여기에 정의하고, 정의만 있고 본문에 없는 각주는 지운다. 프런트매터 sources 와 일치시킨다.
시드 페이지는 2절 원문 주석의 [n] 에 대응하는 각주 정의만 둔다(없으면 "아직 작성되지 않음"). 각주 정의는 이 절에만 두고 [분류원문] 이 붙은 줄에는 붙이지 않는다.
-->
```

### templates/topic.md

```markdown
---
title: "{{title}}"                          # 주제 제목. 질문형 또는 명사구. 예: "로봇 도착과 작업 대상 인계 확인은 어떻게 다른가"
type: topic
category: "{{category}}"                    # 주 연구영역이 속한 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
primary_area_no: {{primary_area_no}}        # 주 연구영역 번호(1~67). 반드시 하나
track: {{track_slug}}                       # 트랙 실행에서 나온 주제 페이지만. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition. 아니면 이 줄을 뺀다
related_areas: [{{related_areas}}]          # 관련 영역 번호 0개 이상. 예: [18, 29]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개
status: {{status}}                          # draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜
version: {{version}}                        # 정수. 신규 1, 갱신마다 +1
---
<!--
[템플릿] 주제 페이지 (type: topic)
경로: docs/topics/YYYY/YYYY-MM-DD-slug.md  (YYYY-MM-DD 는 생성한 실행 날짜, slug 는 영문 소문자·하이픈)
쓰임: 파이프라인 2주기부터의 주제 조사 실행, 세부영역 페이지가 4,000자를 넘어 분리한 글, 트랙 실행에서 하나의 질문을 깊게 다룬 글. 하루 신규 주제 페이지 상한은 daily_budget.new_topic_pages 를 따른다.
필수: 주 연구영역 하나(primary_area_no)와 0개 이상의 관련 영역. 트랙 실행에서 나온 페이지는 프런트매터에 track 을 넣고, 해당 트랙 단계 페이지의 3절(조사 결과)에서 이 페이지를 링크한다.
분량: 1~7절 텍스트 합계(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외) 1,500~2,500자.
서사 골격: 왜 중요한가 → 현장에서 무슨 일이 벌어지는가(현장 유형을 밝힌 적용 사례) → 무엇이 알려져 있는가(검증된 사실) → ROP는 무엇을 맡고 무엇을 연계하는가 → 다른 영역과 어떻게 이어지는가 → 아직 모르는 것.
브리프의 발견 사항(finding)만 쓴다. 새 사실을 더하지 않는다. 필요한 사실이 브리프에 없으면 본문에 넣지 않고 pages.json 의 additional_research_requests 에 기록한다.

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

[경로 규약] 이 페이지에서 홈은 ../../index.md, 주제 목록은 ../index.md, 세부영역 페이지는 ../../categories/<대분류 slug>/<파일>, 대분류 페이지는 ../../categories/<대분류 slug>/index.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 트랙은 ../../tracks/<트랙 slug>/<파일>.md 이다.
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
[홈](../../index.md) › [주제](../index.md) › {{title}}

# {{title}}

**주 연구영역:** [{{primary_area_no}}. {{primary_area_name}}](../../categories/{{category_slug}}/{{area_file}}.md) · **관련 영역:** {{related_area_links_or_없음}} · **실행:** {{run_id}}
<!-- 관련 영역 링크는 "[18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)" 형식으로 쉼표 구분. 트랙 페이지면 "· **트랙:** [트랙 이름](../../tracks/<트랙 slug>/index.md) 단계 n" 을 덧붙인다(예: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)). -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 새 페이지에는 빈 마커 두 줄만 둔다. -->

## 1. 세 줄 요약

- {{summary_line_1}}
- {{summary_line_2}}
- {{summary_line_3}}
<!-- 정확히 세 줄. 각 줄은 한 문장. 첫 줄은 무엇을 밝혔는가, 둘째 줄은 ROP 운영에 무엇을 뜻하는가, 셋째 줄은 무엇이 아직 확인되지 않았는가. 요약에도 핵심 주장에는 태그를 붙인다. -->

## 2. 배경

{{background}}
<!--
어느 연구영역의 어떤 질문에서 출발했는지 쓴다. 주 연구영역의 원문 "핵심 질문"을 인용하면 그대로 옮기고 [분류원문] 을 붙인다. 출발점이 열린 질문(oq-NNN)이나 트랙 백로그 질문(q1-01), 정정 요청, priority.yaml 의 우선 주제이면 그 id 와 링크를 적는다. 1~2단락.
-->

## 3. 본문

### {{subheading_1}}

{{body_1}}

### {{subheading_2}}

{{body_2}}
<!--
소제목은 자유(2~5개). 주장마다 태그·각주. 검증된 발견 사항만 쓰고 순서는 서사 골격을 따른다. 출처가 충돌하면 둘 다 제시하고 7절 열린 질문에 올린다.
표·그림 복제 금지. 도식이 필요하면 mermaid 로 그리고 도식 안에서도 이름을 쓴다. 벤더 주장은 [추정]에 "벤더 주장" 병기. 조건부 승인의 수정 목록을 모두 반영하고 pages.json 의 fixes_applied 에 표시한다.
-->

## 4. 현장 시나리오

**현장 유형:** {{site_types}}

**사례:** {{case_title}}

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
절 제목 "4. 현장 시나리오"는 파이프라인(pipeline/lib/validate.py)이 쓰는 고정 문자열이므로 바꾸지 않는다. 내용은 분류 원문 21장의 방법대로 쓴다: 현장 유형(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 하나를 명시하고, 여섯 항목(시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가 / 수행 자원 / 제약 / 완료·인계 / 예외·성과)을 채운다. 물류창고는 일곱 현장 유형 가운데 하나이므로 기본값으로 쓰지 않는다. 이 주제와 직접 관련 없는 항목은 "해당 없음"으로 둔다. 실제 사례는 출처 각주와 함께, 설명용 가상 사례이면 첫 문장에 밝히고 지어낸 수치는 쓰지 않는다. 다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 낸다.
-->

## 5. ROP 관점의 시사점

**직접 범위:**
{{direct_scope_implications}}

**연계 범위:**
{{external_scope_implications}}
<!-- 분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 경계를 기준으로 ROP가 직접 맡는 것과 외부와 연계하는 것을 나누어 쓴다. 각 항목은 목록으로, 주장마다 태그·각주. 외부 연계 영역을 ROP 직접 범위처럼 쓰지 않는다. -->

## 6. 연결되는 연구영역

{{connected_areas}}
<!-- 목록 형식: "- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 연결 이유 한 문장". 주 연구영역을 첫 줄에, 관련 영역을 그 아래에. 번호와 이름을 함께 쓴다. 여기 적은 번호는 프런트매터 primary_area_no·related_areas 와 일치시킨다. AI를 다루면 27. AI·학습·적응과 모델 운영을 함께 연결한다. -->

## 7. 열린 질문

{{open_questions}}
<!-- 목록 형식: "- **oq-012** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 이 글에서 새로 생긴 질문과 답한(해결한) 질문을 나누어 적고, 해결한 질문에는 답이 있는 절을 표시한다. 트랙 질문(q1-01)은 트랙 백로그 링크만 둔다. pages.json 의 open_question_updates 로도 낸다. 없으면 "없음"과 이유. -->

## 8. 출처

{{footnotes}}
<!-- 각주 정의만 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". 본문의 각주와 프런트매터 sources 를 일치시킨다. 새 출처는 pages.json 의 reference_updates 로도 낸다. -->

## 9. 검증 노트

- 판정: 1차 {{first_verdict}} / 2차 {{second_verdict}}
- 확인·미확인: 확인 {{confirmed_count}}건 · 미확인 {{unconfirmed_count}}건 · 교차 확인 {{cross_checked_count}}건
- 강등된 주장: {{downgraded_claims_or_없음}}
- 검증자 주의: {{verification_note}}
- 신뢰도: {{confidence}}
<!-- 내용 검증 에이전트의 verification.json 에서 옮긴다. 판정 값: 1차 = 승인 | 조건부 승인 | 반려, 2차 = 통과 | 수정 후 재검증 | 불통과. 강등된 주장은 finding id 와 "사실 → 추정" 같은 변경을 적는다. "검증자 주의"는 verification_note 문구를 그대로 쓴다. 스토리텔러는 여기에 자기 의견을 넣지 않는다. -->

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| {{date}} | {{run_id}} | {{change_summary}} | {{version}} |
<!-- 신규 작성은 "신규 작성". 갱신마다 한 행을 위에 추가하고 프런트매터 version 을 올린다. 정정 요청을 반영했으면 corr-NNN id 를 적는다. -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1496건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 2026-09-30 | 예 |
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 | 2023-11-16 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 2026-09-30 | 예 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 | 2023-07-28 | https://zdnet.co.kr/view/?no=20230728173101 | 2026-09-30 | 예 |
| ref-1212 | European Agency for Safety and Health at Work (EU-OSHA) | Regulation 2023/1230/EU - machinery | 미확인 | https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery | 2026-09-30 | 예 |
| ref-1227 | Gibson Dunn | EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains | 2026-03-23 | https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/ | 2026-09-30 | 예 |
| ref-1228 | European Commission (Shaping Europe's digital future) | Cyber Resilience Act - Reporting obligations | 2026-09-11 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 2026-09-30 | 예 |
| ref-1229 | ROS (ros-infrastructure/rep) | REP 2004 -- Package Quality Categories | 2019-12-17 | https://ros.org/reps/rep-2004.html | 2026-09-30 | 예 |
| ref-1230 | SPDX Project (Linux Foundation) | SPDX Overview | 미확인 | https://spdx.dev/about/overview/ | 2026-09-30 | 예 |
| ref-1231 | Open Robotics (Gazebo Classic) | Gazebo : Tutorial : Model structure and requirements | 미확인 | https://classic.gazebosim.org/tutorials?tut=model_structure | 2026-09-30 | 예 |
| ref-1232 | 지디넷코리아 | "실외 이동로봇 필수보험 94% 저렴하게" | 2024-02-08 | https://zdnet.co.kr/view/?no=20240208201432 | 2026-09-30 | 예 |
| ref-1233 | 김·장 법률사무소 | 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점 | 2024-07-05 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930 | 2026-09-30 | 예 |
| ref-1234 | 법제처 찾기쉬운 생활법령정보 | 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인) | 미확인 | https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3 | 2026-09-30 | 예 |
| ref-1235 | 대한민국 정책브리핑 (과학기술정보통신부) | '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무 | 2026-01-21 | https://www.korea.kr/news/policyNewsView.do?newsId=148958380 | 2026-09-30 | 예 |
| ref-1236 | Open Robotics (ROS 2 Documentation) | ROS 2 developer guide | 미확인 | https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html | 2026-09-30 | 예 |
| ref-1237 | 고용노동부 | 산업용 로봇과 컨베이어도 안전검사 필수 | 2017-10-26 | https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135 | 2026-09-30 | 예 |
| ref-1238 | Commonwealth of Virginia (Code of Virginia) | § 46.2-908.1:1. Personal delivery devices | 미확인 | https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/ | 2026-09-30 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [59] 에 걸린 25건 / 전체 396건)

```markdown
- oq-143 [열림] ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? (영역 13, 59, 53)
- oq-173 [열림] 국가기술표준원이 2021년 제정을 발표한 로봇의 승강기 탑승 안전 요구사항 KS 와 실내 배송 로봇 KS 의 표준 번호·조항은 무엇이며, 그 요구(속도 제어·보호 정지·높낮이차·틈새)가 승강기 연동 계층에 어떤 정보를 요구하는가? (영역 63, 22, 59)
- oq-186 [열림] 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시는 무엇이며, 경사로·알림음·등화장치 같은 기존 항목은 어느 항목에 흡수됐는가? (영역 66, 50, 59)
- oq-187 [열림] 운행안전인증 대상이 로봇과 관제장치의 조합인데, 제조사가 다른 실외 로봇을 하나의 오케스트레이션 계층에서 지시할 때 그 계층이 인증상 관제장치에 해당하는지, 재인증이 필요한지에 관한 기준이나 해석이 있는가? (영역 66, 20, 59)
- oq-231 [열림] 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? (영역 49, 59)
- oq-239 [열림] 병원의 특수 물품(마약류·검체 등) 로봇 배송 이력처럼 보관 의무가 걸릴 수 있는 실행 기록의 보관 기간과 무결성 요건을 국내 법령·지침이 정하고 있는가? (영역 37, 59)
- oq-249 [열림] EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? (영역 52, 59, 58)
- oq-250 [열림] KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가? (영역 52, 59)
- oq-262 [열림] 유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가? (영역 53, 59)
- oq-275 [열림] 서비스 로봇(서빙·배송·조리 로봇)을 운영하는 인력에게 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육이 실제로 어떻게 적용되며, 고용노동부 지침이나 사례가 있는가? (영역 56, 59, 50)
- oq-279 [열림] 여러 제조사 로봇의 운영 데이터를 모으는 오케스트레이션 플랫폼 사업자는 EU 데이터법상 데이터 보유자인가, 사용자가 지정한 제3자 데이터 수령자인가, 그리고 그에 따라 제조사에게 데이터 제공을 요구할 수 있는 범위는 어디까지인가? (영역 58, 59)
- oq-282 [열림] 오케스트레이션 플랫폼에서 경로망·속도 제한·작업 규칙 같은 설정을 바꾸는 일이 EU 기계류 규정의 실질적 변경에 해당해 플랫폼 운영자나 통합자가 제조자 의무를 지는 경우가 있는가? (영역 58, 59, 48)
- oq-284 [열림] 서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가? (영역 60, 59, 64)
- oq-285 [열림] 오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가? (영역 60, 53, 59)
- oq-288 [열림] 한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가? (영역 59, 66)
- oq-289 [열림] EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가? (영역 59, 58)
- oq-290 [열림] 국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가? (영역 59, 58)
- oq-291 [열림] 로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가? (영역 59, 52, 57)
- oq-292 [열림] 시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가? (영역 59, 36, 57)
- oq-313 [열림] 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? (영역 59, 58, 66)
- oq-333 [열림] 국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? 평가 항목 수가 바이라인네트워크 보도(16개 항목)와 한국로봇산업진흥원 안내(관제장치를 포함한 8개 심사 항목)에서 다르게 표현되므로 현행 기준도 함께 확인해야 한다. (영역 37, 59, 66)
- oq-338 [열림] 로봇 플랫폼 사업자와 현장 운영자가 각각 EU AI Act 의 제공자·배포자가 될 때 실행 기록의 통제권과 6개월 이상 보관 책임을 계약으로 나눈 공개 사례나 지침이 있는가? (영역 43, 58, 59)
- oq-344 [열림] 국내에서 판매·설치되는 산업용 로봇·이동로봇의 사용설명서를 한국어로 제공해야 한다는 규정이 자율안전확인 고시나 다른 법령에 있으며, 원본과 한국어 번역판의 판이 다를 때 어느 쪽을 근거로 삼는가? (영역 59, 4)
- oq-347 [열림] AI허브 원 이용정책은 이용자가 학습시킨 모델의 배포·상업적 이용을 직접 말하지 않고 '학습용으로만'과 '영리·비영리 연구개발 활용'을 함께 적는데, 건축 도면 데이터로 학습한 도면 인식 모델을 상용 서비스로 배포하는 것이 허용되는지와 데이터셋별 별도 조건이 있는지를 운영기관 확인으로 정할 수 있는가? (영역 14, 59)
- oq-393 [열림] EN ISO 10218-1/-2:2025 참조는 기계 규정 (EU) 2023/1230 의 조화 표준으로 언제 게재되며, 지침 2006/42/EC 기반 목록(시행결정 2023/1586)이 2027-01-20 폐지된 뒤 적합성 추정은 어떻게 이어지는가? (영역 50, 59)
```

### docs/standards/index.md (요약: 361개 — 이름 · 종류 · 발행 기관)

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
- ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries) · ISA(International Society of Automation) · 표준
- IDTA 02005 Provision of Simulation Models (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- autoware_rosbag2_anonymizer · Autoware Foundation · 오픈소스
- Gazebo Fuel Tools (gz-fuel-tools) · Open Robotics · 오픈소스
- ISO/AWI 26159-2 로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항 (초안) · ISO (ISO/TC 299 Robotics) · 표준
- ISO/CD TS 8100-11 승강기와 다른 시스템의 상호운용 (위원회 초안) · ISO (ISO/TC 178 Lifts, escalators and moving walks) · 표준
- 싱가포르 Technical Reference 93 (TR 93) 로봇–건물 설비 데이터 교환 · 싱가포르 (CGH 보도자료 기준, 발행 기관명 미확인) · 표준
- Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_obstacle (사람 검출·lane_blocker) · Open Robotics (open-rmf) · 오픈소스
- Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리) · Pasch, F. 외 (Intel Labs 외) · 오픈소스
- RoboVAST (출처 기록 기반 시뮬레이션 시험 틀) · Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. · 프레임워크
- ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열 · ISO · 표준
- IEEE 7001-2021 자율 시스템 투명성 표준 · IEEE Standards Association · 표준
- W3C Trace Context (traceparent·tracestate, 권고안 2021-11-23) · W3C · 표준
- EU AI Act 제19조 자동 생성 로그 (Article 19) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- EU 기계류 지침 2006/42/EC 부속서 I 1.7.4.1 (설명서 언어·원본·번역 표기) · European Parliament and Council (legislation.gov.uk 게재본) · 프레임워크
- MMLongBench-Doc (긴 문서 이해 벤치마크) · Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- NVIDIA Isaac Mission Dispatch · NVIDIA (nvidia-isaac) · 오픈소스
- NVIDIA Isaac Mission Control · NVIDIA (nvidia-isaac) · 오픈소스
- PlanSys2 (ROS 2 Planning System) · PlanSys2 프로젝트 · 오픈소스
- crossflow · Open Robotics (open-rmf) · 오픈소스
- Open BIM Object standard (OBOS) V1.0 · Construction Information Limited (Masterspec, 뉴질랜드) · 표준
- W3C SKOS (Simple Knowledge Organization System) Reference · W3C · 표준
- BPMN 2.0.2 (OMG formal/13-12-09) · OMG(Object Management Group) · 표준
- Open-RMF 입찰 제안 메시지(rmf_internal_msgs의 rmf_task_msgs BidProposal) · Open Robotics (open-rmf) · 오픈소스
- KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 (대한승강기협회 단체표준) · 대한승강기협회(KOLA) · 표준
- KONE RMF Lift Adapter (kone-ros-api) · CHART (KABAM-Robotics 보존 저장소) · 오픈소스
- door_adapter_dormakaba (Open-RMF Dormakaba 문 어댑터) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 배정·취소 응답 스키마(rmf_api_msgs dispatch_task_response·cancel_task_response·simple_response) · Open Robotics (open-rmf) · 오픈소스
- KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항 · 국가기술표준원(한국표준협회 KSSN) · 표준
- KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템 · 국가기술표준원(한국표준협회 KSSN) · 표준
- 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호) · 고용노동부 · 프레임워크
- STPA Handbook · MIT Partnership for Systems Approaches to Safety and Security · 프레임워크
- KS B 8252 실내 이동로봇의 보호정지 시험방법 · 국가기술표준원 (e-나라표준인증) · 표준
- 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 별표 3 · 산업통상부 · 평가 프로그램
- human_detection_fusion (YOLO·UWB 사람 위치 융합 ROS 2 패키지) · ATHENA RC (EU ARISE 'KIRO' 실험) · 오픈소스
- UL 3100 Automated Mobile Platforms (AMPs) · UL Standards & Engagement · 표준
- UL 3300 (SCIEE 로봇 표준, Simbe Tally 인증 발표) · UL Solutions · 표준
- ISO/DIS 3691-4 (제3판) 무인 산업용 트럭과 그 시스템 안전 요구·검증 개정안 · ISO · 표준
- KS B ISO 10218-1 산업용 로봇의 안전에 관한 요구사항 — 제1부: 로봇 · 국가기술표준원 · 표준
- 산업용 로봇 자율안전확인 · 안전보건공단 산업안전보건인증원 · 평가 프로그램
- 위원회 시행결정 (EU) 2026/2015 (기계류 지침 조화 표준 목록 개정·폐지) · European Commission · 프레임워크
```

### runs/2026-10-12-02/docs_tree.txt

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
glossary/4d-scene-graph.md
glossary/a-b-update.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/abstract-and-concrete-scenario.md
glossary/action-dependency-graph.md
glossary/action-status.md
glossary/actively-exploited-vulnerability.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alarm-management.md
glossary/alert-tier.md
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
glossary/automatic-recording-of-events.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/average-displacement-error.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
glossary/building-element-proxy.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/buildingsmart-data-dictionary.md
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
glossary/connection-state.md
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
glossary/data-provenance.md
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
glossary/domain-shift.md
glossary/door-to-door-robot-delivery.md
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
glossary/generalized-voronoi-graph.md
glossary/giai.md
glossary/gln-extension-component.md
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
glossary/integrity-risk.md
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
glossary/lease-expiry.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic-on-finite-traces.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/localization-score.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/makespan.md
glossary/managed-node.md
glossary/management-of-change.md
glossary/map-alignment.md
glossary/map-distribution.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/minimum-cost-flow.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt-last-will.md
glossary/mqtt-quality-of-service-level.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/oauth2-client-credentials-grant.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/online-simulation.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry-genai-semantic-conventions.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/operational-state.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/original-instructions.md
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
glossary/persistence-filter.md
glossary/personal-delivery-device.md
glossary/phased-rollout.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/precision-time-protocol.md
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
glossary/remote-attestation.md
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
glossary/runtime-tracing.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/safety-guardrail.md
glossary/safety-state-report.md
glossary/saga.md
glossary/satisfiability-modulo-theories.md
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
glossary/skos.md
glossary/slot-filling.md
glossary/slotcar.md
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
glossary/state-script.md
glossary/stpa.md
glossary/strict-schema.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/surrogate-model.md
glossary/synchronization-loss.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/task-dependency-graph.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/trace-context.md
glossary/transparency-level-ieee-7001.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-defined-property-set.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050-hibernation.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
glossary/wireless-safety-rated-emergency-stop.md
glossary/workflow-diagram.md
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
logs/daily/2026-10-09.md
logs/daily/2026-10-10.md
logs/daily/2026-10-11.md
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
references/ref-1239.md
references/ref-124.md
references/ref-1240.md
references/ref-1241.md
references/ref-1242.md
references/ref-1243.md
references/ref-1244.md
references/ref-1245.md
references/ref-1246.md
references/ref-1247.md
references/ref-1248.md
references/ref-1249.md
references/ref-125.md
references/ref-1250.md
references/ref-1251.md
references/ref-1252.md
references/ref-1253.md
references/ref-1254.md
references/ref-1255.md
references/ref-1256.md
references/ref-1257.md
references/ref-1258.md
references/ref-1259.md
references/ref-126.md
references/ref-1260.md
references/ref-1261.md
references/ref-1262.md
references/ref-1263.md
references/ref-1264.md
references/ref-1265.md
references/ref-1266.md
references/ref-1267.md
references/ref-1268.md
references/ref-1269.md
references/ref-127.md
references/ref-1270.md
references/ref-1271.md
references/ref-1272.md
references/ref-1273.md
references/ref-1274.md
references/ref-1275.md
references/ref-1276.md
references/ref-1277.md
references/ref-1278.md
references/ref-1279.md
references/ref-128.md
references/ref-1280.md
references/ref-1281.md
references/ref-1282.md
references/ref-1283.md
references/ref-1284.md
references/ref-1285.md
references/ref-1286.md
references/ref-1287.md
references/ref-1288.md
references/ref-1289.md
references/ref-129.md
references/ref-1290.md
references/ref-1291.md
references/ref-1292.md
references/ref-1293.md
references/ref-1294.md
references/ref-1295.md
references/ref-1296.md
references/ref-1297.md
references/ref-1298.md
references/ref-1299.md
references/ref-130.md
references/ref-1300.md
references/ref-1301.md
references/ref-1302.md
references/ref-1303.md
references/ref-1304.md
references/ref-1305.md
references/ref-1306.md
references/ref-1307.md
references/ref-1308.md
references/ref-1309.md
references/ref-131.md
references/ref-1310.md
references/ref-1311.md
references/ref-1312.md
references/ref-1313.md
references/ref-1314.md
references/ref-1315.md
references/ref-1316.md
references/ref-1317.md
references/ref-1318.md
references/ref-1319.md
references/ref-132.md
references/ref-1320.md
references/ref-1321.md
references/ref-1322.md
references/ref-1323.md
references/ref-1324.md
references/ref-1325.md
references/ref-1326.md
references/ref-1327.md
references/ref-1328.md
references/ref-1329.md
references/ref-133.md
references/ref-1330.md
references/ref-1331.md
references/ref-1332.md
references/ref-1333.md
references/ref-1334.md
references/ref-1335.md
references/ref-1336.md
references/ref-1337.md
references/ref-1338.md
references/ref-1339.md
references/ref-134.md
references/ref-1340.md
references/ref-1341.md
references/ref-1342.md
references/ref-1343.md
references/ref-1344.md
references/ref-1345.md
references/ref-1346.md
references/ref-1347.md
references/ref-1348.md
references/ref-1349.md
references/ref-135.md
references/ref-1350.md
references/ref-1351.md
references/ref-1352.md
references/ref-1353.md
references/ref-1354.md
references/ref-1355.md
references/ref-1356.md
references/ref-1357.md
references/ref-1358.md
references/ref-1359.md
references/ref-136.md
references/ref-1360.md
references/ref-1361.md
references/ref-1362.md
references/ref-1363.md
references/ref-1364.md
references/ref-1365.md
references/ref-1366.md
references/ref-1367.md
references/ref-1368.md
references/ref-1369.md
references/ref-137.md
references/ref-1370.md
references/ref-1371.md
references/ref-1372.md
references/ref-1373.md
references/ref-1374.md
references/ref-1375.md
references/ref-1376.md
references/ref-1377.md
references/ref-1378.md
references/ref-1379.md
references/ref-138.md
references/ref-1380.md
references/ref-1381.md
references/ref-1382.md
references/ref-1383.md
references/ref-1384.md
references/ref-1385.md
references/ref-1386.md
references/ref-1387.md
references/ref-1388.md
references/ref-1389.md
references/ref-139.md
references/ref-1390.md
references/ref-1391.md
references/ref-1392.md
references/ref-1393.md
references/ref-1394.md
references/ref-1395.md
references/ref-1396.md
references/ref-1397.md
references/ref-1398.md
references/ref-1399.md
references/ref-140.md
references/ref-1400.md
references/ref-1401.md
references/ref-1402.md
references/ref-1403.md
references/ref-1404.md
references/ref-1405.md
references/ref-1406.md
references/ref-1407.md
references/ref-1408.md
references/ref-1409.md
references/ref-141.md
references/ref-1410.md
references/ref-1411.md
references/ref-1412.md
references/ref-1413.md
references/ref-1414.md
references/ref-1415.md
references/ref-1416.md
references/ref-1417.md
references/ref-1418.md
references/ref-1419.md
references/ref-142.md
references/ref-1420.md
references/ref-1421.md
references/ref-1422.md
references/ref-1423.md
references/ref-1424.md
references/ref-1425.md
references/ref-1426.md
references/ref-1427.md
references/ref-1428.md
references/ref-1429.md
references/ref-143.md
references/ref-1430.md
references/ref-1431.md
references/ref-1432.md
references/ref-1433.md
references/ref-1434.md
references/ref-1435.md
references/ref-1436.md
references/ref-1437.md
references/ref-1438.md
references/ref-1439.md
references/ref-144.md
references/ref-1440.md
references/ref-1441.md
references/ref-1442.md
references/ref-1443.md
references/ref-1444.md
references/ref-1445.md
references/ref-1446.md
references/ref-1447.md
references/ref-1448.md
references/ref-1449.md
references/ref-145.md
references/ref-1450.md
references/ref-1451.md
references/ref-1452.md
references/ref-1453.md
references/ref-1454.md
references/ref-1455.md
references/ref-1456.md
references/ref-1457.md
references/ref-1458.md
references/ref-1459.md
references/ref-146.md
references/ref-1460.md
references/ref-1461.md
references/ref-1462.md
references/ref-1463.md
references/ref-1464.md
references/ref-1465.md
references/ref-1466.md
references/ref-1467.md
references/ref-1468.md
references/ref-1469.md
references/ref-147.md
references/ref-1470.md
references/ref-1471.md
references/ref-1472.md
references/ref-1473.md
references/ref-1474.md
references/ref-1475.md
references/ref-1476.md
references/ref-1477.md
references/ref-1478.md
references/ref-1479.md
references/ref-148.md
references/ref-1480.md
references/ref-1481.md
references/ref-1482.md
references/ref-1483.md
references/ref-1484.md
references/ref-1485.md
references/ref-1486.md
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
topics/2026/2026-10-09-area18-s10.md
topics/2026/2026-10-09-area18-s11.md
topics/2026/2026-10-09-area18-s6.md
topics/2026/2026-10-09-area18-s7.md
topics/2026/2026-10-09-area18-s8.md
topics/2026/2026-10-09-area19-s10.md
topics/2026/2026-10-09-area19-s11.md
topics/2026/2026-10-09-area19-s6.md
topics/2026/2026-10-09-area19-s7.md
topics/2026/2026-10-09-area19-s8.md
topics/2026/2026-10-09-area33-s10.md
topics/2026/2026-10-09-area33-s11.md
topics/2026/2026-10-09-area33-s3.md
topics/2026/2026-10-09-area33-s6.md
topics/2026/2026-10-09-area33-s7.md
topics/2026/2026-10-09-area33-s8.md
topics/2026/2026-10-09-area37-s11.md
topics/2026/2026-10-09-area37-s3.md
topics/2026/2026-10-09-area37-s7.md
topics/2026/2026-10-09-area38-s10.md
topics/2026/2026-10-09-area38-s11.md
topics/2026/2026-10-09-area38-s3.md
topics/2026/2026-10-09-area38-s7.md
topics/2026/2026-10-09-area41-s11.md
topics/2026/2026-10-09-area41-s6.md
topics/2026/2026-10-09-area41-s7.md
topics/2026/2026-10-09-area42-s10.md
topics/2026/2026-10-09-area42-s11.md
topics/2026/2026-10-09-area42-s3.md
topics/2026/2026-10-09-area42-s7.md
topics/2026/2026-10-09-area43-s10.md
topics/2026/2026-10-09-area43-s11.md
topics/2026/2026-10-09-area43-s6.md
topics/2026/2026-10-09-area43-s7.md
topics/2026/2026-10-09-area43-s8.md
topics/2026/2026-10-10-area20-s10.md
topics/2026/2026-10-10-area20-s11.md
topics/2026/2026-10-10-area20-s3.md
topics/2026/2026-10-10-area20-s6.md
topics/2026/2026-10-10-area20-s7.md
topics/2026/2026-10-10-area20-s8.md
topics/2026/2026-10-10-area24-s11.md
topics/2026/2026-10-10-area24-s3.md
topics/2026/2026-10-10-area24-s6.md
topics/2026/2026-10-10-area24-s7.md
topics/2026/2026-10-10-area24-s8.md
topics/2026/2026-10-10-area25-s10.md
topics/2026/2026-10-10-area25-s11.md
topics/2026/2026-10-10-area25-s3.md
topics/2026/2026-10-10-area25-s6.md
topics/2026/2026-10-10-area25-s7.md
topics/2026/2026-10-10-area25-s8.md
topics/2026/2026-10-10-area26-s10.md
topics/2026/2026-10-10-area26-s11.md
topics/2026/2026-10-10-area26-s3.md
topics/2026/2026-10-10-area26-s7.md
topics/2026/2026-10-10-area26-s8.md
topics/2026/2026-10-10-area27-s10.md
topics/2026/2026-10-10-area27-s11.md
topics/2026/2026-10-10-area27-s6.md
topics/2026/2026-10-10-area27-s7.md
topics/2026/2026-10-10-area27-s8.md
topics/2026/2026-10-10-area28-s10.md
topics/2026/2026-10-10-area28-s11.md
topics/2026/2026-10-10-area28-s3.md
topics/2026/2026-10-10-area28-s6.md
topics/2026/2026-10-10-area28-s7.md
topics/2026/2026-10-10-area28-s8.md
topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md
topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md
topics/2026/2026-10-11-area21-s10.md
topics/2026/2026-10-11-area21-s11.md
topics/2026/2026-10-11-area21-s6.md
topics/2026/2026-10-11-area21-s7.md
topics/2026/2026-10-11-area21-s8.md
topics/2026/2026-10-11-area22-s10.md
topics/2026/2026-10-11-area22-s11.md
topics/2026/2026-10-11-area22-s3.md
topics/2026/2026-10-11-area22-s6.md
topics/2026/2026-10-11-area22-s7.md
topics/2026/2026-10-11-area22-s8.md
topics/2026/2026-10-11-area23-s10.md
topics/2026/2026-10-11-area23-s11.md
topics/2026/2026-10-11-area23-s3.md
topics/2026/2026-10-11-area23-s4.md
topics/2026/2026-10-11-area23-s6.md
topics/2026/2026-10-11-area23-s7.md
topics/2026/2026-10-11-area23-s8.md
topics/2026/2026-10-11-area48-s10.md
topics/2026/2026-10-11-area48-s11.md
topics/2026/2026-10-11-area48-s3.md
topics/2026/2026-10-11-area48-s4.md
topics/2026/2026-10-11-area48-s6.md
topics/2026/2026-10-11-area48-s7.md
topics/2026/2026-10-11-area48-s8.md
topics/2026/2026-10-11-area49-s11.md
topics/2026/2026-10-11-area49-s4.md
topics/2026/2026-10-11-area49-s6.md
topics/2026/2026-10-11-area49-s7.md
topics/2026/2026-10-11-area49-s8.md
topics/2026/2026-10-11-area50-s10.md
topics/2026/2026-10-11-area50-s11.md
topics/2026/2026-10-11-area50-s4.md
topics/2026/2026-10-11-area50-s6.md
topics/2026/2026-10-11-area50-s7.md
topics/2026/2026-10-11-area50-s8.md
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

### runs/2026-10-12-02/pages.json

```json
{
  "run_id": "2026-10-12-02",
  "outline": [
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 550,
      "summary": "EU 개정 제조물책임지침은 정오표 기준 2026-12-08 후, 곧 2026-12-09 출시·사용 개시 제품부터 적용되고 소프트웨어를 포함하며 비상업 FOSS 를 뺀다. [사실][^ref-1529][^ref-1530]",
      "planned_findings": [
        "f43",
        "f44",
        "f45",
        "f46"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1500,
      "summary": "인공지능 기본법 제33조는 고영향 해당성 사전 검토 의무, 제35조는 영향평가 노력의무를 정한다. [사실][^ref-1518]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f14",
        "f17",
        "f30",
        "f44",
        "f45"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2900,
      "summary": "한국 실외이동로봇 책임보험의 법령 기준 금액은 시행규칙 제7조의10 이 정한다. [사실][^ref-1520]",
      "planned_findings": [
        "f16",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24",
        "f25"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1500,
      "summary": "CRA 보고 기한은 인지 시점·시정 조치 이용 가능 시점·사고 통지 제출 시점으로 기산점이 다르다. [사실][^ref-1522]",
      "planned_findings": [
        "f27",
        "f28",
        "f29",
        "f33",
        "f34",
        "f35",
        "f36",
        "f37",
        "f38",
        "f39",
        "f41",
        "f46"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2600,
      "summary": "AI Act 디지털 옴니버스 (EU) 2026/1744 는 기계규정을 부속서 I Section B 로 옮겼다. [사실][^ref-1517]",
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
        "f16",
        "f17",
        "f31",
        "f43"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 550,
      "summary": "한·싱가포르 AI 샌드박스 비교 연구는 싱가포르 샌드박스가 규제 특례 목적이 아니라고 구분한다. [사실][^ref-1531]",
      "planned_findings": [
        "f47",
        "f46"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1200,
      "summary": "규제 대장·고영향 검토 기록·보험 상태·보고 기산 기록·릴리스 권리 검사를 ROP 기록 업무로 두자는 구축자 의견. [의견][^ref-1517]",
      "planned_findings": [
        "f10",
        "f15",
        "f26",
        "f32",
        "f40",
        "f42",
        "f48"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 350,
      "summary": "48. 안전·위험 관리와 44. 로봇 기반 모델·언어 모델 계획과의 연결을 더한다. [사실][^ref-1517]",
      "planned_findings": [
        "f7",
        "f41",
        "f42"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "section": "11. 열린 질문",
      "budget_chars": 1200,
      "summary": "oq-288 해결, oq-143·oq-186·oq-187·oq-289·oq-291·oq-292 부분 근거, 새 질문 2건. [사실][^ref-1520]",
      "planned_findings": [
        "f18",
        "f17"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 5절 교체(책임보험 법령 기준 금액, 16개→8개 근거 고시 정정, 버지니아 합산 운행 보험 단위, 홍콩 비교), 3·4·6·7·8·9·10·11절에 2026-10-12 보강 소절 추가(AI 옴니버스·기계규정 위임법령, PLD 정오표, 인공지능 기본법 제33·35조, CRA 기산점·스튜어드, 라이선스 검사, oq-288 해결), 프런트매터 sources·related_areas 갱신",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "append",
          "frontmatter": {
            "sources": [
              "ref-991",
              "ref-1227",
              "ref-1228",
              "ref-1229",
              "ref-1230",
              "ref-1231",
              "ref-1232",
              "ref-980",
              "ref-992",
              "ref-1233",
              "ref-1234",
              "ref-1235",
              "ref-1236",
              "ref-1237",
              "ref-1238",
              "ref-1212",
              "ref-1469",
              "ref-1517",
              "ref-1518",
              "ref-1519",
              "ref-1520",
              "ref-1521",
              "ref-1522",
              "ref-1523",
              "ref-1524",
              "ref-1525",
              "ref-1526",
              "ref-1527",
              "ref-1528",
              "ref-1529",
              "ref-1530",
              "ref-1531"
            ],
            "related_areas": [
              3,
              4,
              13,
              16,
              36,
              44,
              47,
              48,
              50,
              52,
              53,
              57,
              58,
              66
            ],
            "last_run": "2026-10-12"
          },
          "content": "\n### 2026-10-12 보강: 개정 제조물책임지침의 적용 시점 근거\n\nEU 개정 제조물책임지침 (EU) 2024/2853은 2026-12-08 후(정오표 2026-05-07, OJ L 2026/90364 기준), 곧 2026-12-09에 출시·사용 개시된 제품부터 적용된다. [사실][^ref-1529][^ref-1530] 이 지침은 소프트웨어를 제품에 포함하고, 상업 활동 밖에서 개발·공급되는 자유·오픈소스 소프트웨어(Free and Open-Source Software, FOSS)는 적용에서 뺀다. [사실][^ref-1529] 주제 페이지 둘째 문단의 '2026-12-09 이후 출시·사용 개시 제품'이라는 날짜는 정오표 기준의 뜻과 같아 그대로 두지만, 근거였던 법률사무소 해설은 정오표 전에 나온 자료이므로 적용 시점·소프트웨어 포함·FOSS 제외의 근거는 관보 원문과 정오표로 읽는다. [추정][^ref-1227][^ref-1529][^ref-1530]\n"
        },
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "content": "\n### 2026-10-12 보강\n\n- **고영향 인공지능(High-impact AI)** — 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」(법령 약칭 인공지능기본법, 이하 인공지능 기본법) 제33조1항은 인공지능사업자가 AI나 이를 이용한 제품·서비스를 제공할 때 그 AI가 [고영향 인공지능](../../glossary/high-impact-ai.md)에 해당하는지 사전에 검토하도록 한다. [사실][^ref-1518] 같은 항은 필요하면 과학기술정보통신부장관에게 해당 여부 확인을 요청할 수 있게 하고(재량), 제2항은 요청이 있으면 장관이 해당 여부를 확인하도록 한다. [사실][^ref-1518] 제35조1항은 고영향 AI 제품·서비스를 제공하는 사업자가 사전에 사람의 기본권에 미치는 영향을 평가하도록 노력하게 하는 노력의무이고, 제2항은 국가기관등이 영향평가를 실시한 제품·서비스를 우선 고려하게 한다. [사실][^ref-1518]\n- **인공지능 기본법 조문 판 표기** — 이번에 열람한 판은 법률 제21311호(2026-01-20 일부개정, 2026-07-21 시행)이며, 이 판의 제33조에는 개정 표시가 없다. [사실][^ref-1518] 두 조의 의무는 법 최초 시행(2026-01-22)부터 있었고 2026-07-21은 두 조의 발효일이 아닌 것으로 보인다. [추정][^ref-1518][^ref-1235] 다만 제35조1항에는 ‘개정 2026. 1. 20.’ 표시가 있어 바뀐 문장의 시행일이 2026-07-21일 수 있으며, 원판([ref-620](../../references/ref-620.md))과 신구 대비표는 확인하지 못했다. [추정][^ref-1518]\n- **[제조물책임](../../glossary/product-liability.md)(Product Liability, EU 정의)** — 개정 제조물책임지침 제4조1항은 '제품'을 다른 동산·부동산에 통합되거나 연결된 경우를 포함한 모든 동산으로 정의하고, 전기·디지털 제조 파일·원재료·소프트웨어를 포함한다. [사실][^ref-1529] 제2조2항은 상업 활동 밖에서 개발·공급되는 FOSS에는 지침을 적용하지 않는다. [사실][^ref-1529]\n- **오픈소스 소프트웨어 스튜어드(Open-source Software Steward)** — [사이버복원력법](../../glossary/cyber-resilience-act.md)(Cyber Resilience Act, CRA) 제24조3항은 스튜어드에게 제14조1항 보고 의무를 그 제품 개발에 관여하는 범위에서 적용한다. [사실][^ref-1522] 제71조2항에 따라 제24조는 일반 적용일인 2027-12-11부터 적용되고(제14조만 2026-09-11부터), 유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA)의 단일 보고 플랫폼 가동 발표(2026-09-11)도 스튜어드 보고 의무의 적용일을 2027-12-11로 구분한다. [사실][^ref-1522][^ref-1523]\n- **운행안전인증의 관제장치 변경** — [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md)의 현행 근거 고시는 산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)이며, 이 페이지에서는 이후 제2025-21호로 적는다. [사실][^ref-1469] 이 고시 제8조1항2호는 인증받은 실외이동로봇 또는 해당 관제장치의 일부를 변경해 신규 인증이나 변경인증을 받으려는 경우 인증기관장이 심사의 일부 또는 전부를 면제할 수 있게 한 것으로 보인다(리서치 단계 원문 열람 기준, 검증 단계 미확인). [추정][^ref-1469] 오케스트레이션 계층이 인증상 관제장치인지에 대한 해석은 확인되지 않았다(oq-187).\n"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "**현장 유형:** 실외\n\n**사례:** 한국 보도에서 실외이동로봇 운행\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 해당 없음 |\n| 작업 대상 | 해당 없음 |\n| 수행 자원 | 운행안전인증 대상은 배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합이다. [사실][^ref-980] 운용자는 로봇을 정확히 조작하고 안전하게 운용할 의무를 진다. [사실][^ref-991] |\n| 제약 | 2023-11-17부터 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하 실외이동로봇이 보행자 지위로 보도를 통행할 수 있다. [사실][^ref-991][^ref-980] 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지켜야 한다. [사실][^ref-991] 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 한다. [사실][^ref-991][^ref-1232] 그 보험금 기준은 지능형로봇법 시행규칙 제7조의10의 법령 기준 금액으로, 사망 1인당 1억5천만원(실손해액이 2천만원 미만이면 2천만원), 부상 1인당 3천만원, 후유장애 1인당 1억5천만원, 재물 사고당 10억원이다. [사실][^ref-1520] 이 조문은 2023-11-17 신설된 뒤 현행 통합본(산업통상부령 제1호, 2025-10-01 시행)까지 개정되지 않았다. [사실][^ref-1520] |\n| 완료·인계 | 해당 없음 |\n| 예외·성과 | 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있다. [사실][^ref-991] 한국로봇산업협회 발표를 전한 기사(ref-1232) 기준으로, 협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고 첫 가입 기업은 뉴빌리티·로보티즈였다. 이 단체보험 상품의 보장 한도는 미확인이다. [추정][^ref-1232] |\n\n시행규칙 제7조의10의 금액은 법령이 정한 보험금 기준이며, 실제 보험 상품의 보장·면책·자기부담금·가입 기간이나 협회 단체보험의 보험료와는 다른 지표이므로 서로 다른 항목으로 기록해야 한다고 본다(구축자 의견). [의견][^ref-1520]\n\n정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다(2023-11-16 발표). [사실][^ref-991] 운행안전인증은 서류심사→제품심사→인증표시 순으로 진행되고 신청일부터 30일 이내에 처리되며, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다(2026-09-30 확인). [사실][^ref-980]\n\n제정 당시의 기준은 달랐다. 2023-07 산업통상자원부가 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다(2023-07 행정예고안 기준). [사실][^ref-992] 심사항목을 줄인 근거는 산업통상부 공고 제2025-042호(2025-11-06)의 행정예고다. 행정예고안은 인증 절차 간소화를 개정 이유로 들고, 심사결과 통보 기한 30일 이내 명시(안 제9조)와 심사항목 기준 통·폐합에 따른 16개→8개 축소(안 별표 3)를 담았다(행정예고안 기준). [사실][^ref-1519] 최종 근거는 이 개정을 반영해 2025-11-24 발령·시행된 고시 제2025-21호다. [사실][^ref-1469] 별표 항목이 어떻게 대응하는지는 [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md)에 정리돼 있다. 다만 2023 행정예고안의 알림음·등화장치 기준이 현행 별표 3 밖의 다른 규정으로 옮겨졌는지는 확인되지 않았다(oq-186 열림).\n\n**현장 유형:** 실외\n\n**사례:** 미국 버지니아주에서 개인 배송 장치를 보도로 운행 (해외 비교)\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 해당 없음 |\n| 작업 대상 | 해당 없음 |\n| 수행 자원 | 장치에 운영자를 식별하는 표시를 단다. [사실][^ref-1238] |\n| 제약 | [개인 배송 장치](../../glossary/personal-delivery-device.md)(Personal Delivery Device, PDD)는 보도·횡단보도에서 시속 10마일 이하로 운행한다. [사실][^ref-1238] 운영자는 자기 통제 아래 있는 개인 배송 장치들의 합산 운행(combined operations)으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지해야 하며, 이 금액은 장치당 한도로 정해져 있지 않다. [사실][^ref-1238] |\n| 완료·인계 | 해당 없음 |\n| 예외·성과 | 해당 없음 |\n\n이 사례는 버지니아주법 §46.2-908.1:1 기준이며(2026-09-30 확인, 보험 단위는 2026-10-12 재확인), 지방정부는 추가 안전 요건을 둘 수 있다. [사실][^ref-1238] 미국 주법이므로 한국 현장에 바로 적용되지 않으며, 한국 사례와 운행 속도·보험 요구를 비교하는 해외 비교 사례로만 둔다.\n\n비교하면, 홍콩 정부는 2026-05-20 입법회 서면 답변(LCQ20)에서 사적·상업적 목적의 지능형 로봇 사용에 제3자 책임보험 가입을 강제하는 법정 요건이 당시 홍콩에 없다고 밝혔다. [사실][^ref-1521]\n\n이번 조사에서 근거를 찾은 현장 유형은 실외뿐이다. 물류창고·제조 공장·병원·상업 시설·가정의 사례는 이번 조사에서 찾지 못했다.\n"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "\n### 2026-10-12 보강: 보고 기한의 기산점\n\nCRA 보고 기한은 기한마다 세기 시작하는 시점이 달라, 기한 길이와 함께 기산점을 기록해야 계산할 수 있다. 주제 페이지의 24시간·72시간·14일·1개월 기한 서술은 그대로 두고 기산점만 보탠다. CRA 제14조2항 (a)(b)는 [적극 악용 취약점](../../glossary/actively-exploited-vulnerability.md)의 조기 경보(24시간)와 취약점 통지(72시간)를 제조자가 그 취약점을 인지한 때부터 센다. [사실][^ref-1522] 같은 항 (c)는 최종 보고 기한을 최초 인지가 아니라 시정·완화 조치가 이용 가능해진 뒤 14일 이내로 정한다(관련 정보가 이미 제공된 경우 제외). [사실][^ref-1522] 제14조4항 (c)는 중대한 보안 사고의 최종 보고를 사고 통지 제출 뒤 1개월 이내로 정해, 취약점 최종 보고와 기산점이 다르다. [사실][^ref-1522]\n\n주제 페이지의 제조물책임 증거 공개·결함 추정·보안 업데이트 서술은 법률사무소 해설 기준이며 이번에 원문과 대조하지 않았고, 적용 시점만 관보 원문·정오표 기준(3절·7절)으로 읽는다. [추정][^ref-1227][^ref-1529][^ref-1530]\n\n### 2026-10-12 보강: 라이선스 재배포 의무와 자동 검사\n\nApache License 2.0 제4절은 저작물이나 파생저작물을 재배포할 때 (a) 수령자에게 라이선스 사본을 주고, (b) 수정한 파일에 변경 사실을 눈에 띄게 표시하며, (d) 원 저작물에 NOTICE 파일이 있으면 관련 귀속 고지의 읽을 수 있는 사본을 NOTICE 파일·소스·문서·통상 표시 화면 가운데 한 곳에 넣도록 요구한다. [사실][^ref-1524]\n\nREUSE 명세 3.3(2024-11-14)은 주석을 넣을 수 없는 파일의 라이선스 정보를 같은 이름에 .license 확장자를 붙인 인접 텍스트 파일에 두도록 규정하고, REUSE.toml로 정보를 모아 두는 방법도 정한다. [사실][^ref-1525] 이 방법을 실제 로봇 3D 자산에 적용한 사례는 확인하지 못했다(oq-292).\n\nSPDX 명세 2.2.2 부록 D는 라이선스 표현식의 문법으로, 둘 이상의 라이선스 중 하나를 고를 수 있는 경우를 OR 연산자로, 동시에 준수해야 하는 경우를 AND 연산자로 표현하게 한다(호환성의 법률 판정 규칙은 아니다). [사실][^ref-1527] reuse-tool은 프로젝트 자체 변경기록(CHANGELOG v6.1.0 태그) 기준으로 v6.0.0(2025-10-06)에서 reuse lint에 SPDX 문법상 유효하지 않은 라이선스 표현식을 잡는 검사 항목을 추가했다고 기록한다(실행 재현 안 함). [사실][^ref-1526]\n\n[로봇 기반 모델](../../glossary/robot-foundation-model.md) 가중치에는 코드와 별개의 라이선스 문서가 붙는 예가 있다. NVIDIA GR00T-N1.6-3B 모델 저장소의 LICENSE 제3.3절은 저작물과 파생물을 비상업적(연구·평가 목적) 용도로만 쓰게 하고, NVIDIA와 계열사는 상업적으로 쓸 수 있다고 정한다. [추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)[^ref-1528] 다른 모델판·코드 저장소·별도 계약의 조건은 미확인이다.\n"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "\n### 2026-10-12 보강\n\n이번 실행에서 1차 원문으로 확인한 규범을 아래 표에 더한다. 주제 페이지 표에 같은 이름의 행이 있으면 이 표의 근거와 날짜 표현을 함께 읽는다.\n\n| 이름 | 유형 | 이 영역과의 관계 | 출처 |\n|---|---|---|---|\n| EU AI Act (Regulation (EU) 2024/1689)와 디지털 옴니버스 (EU) 2026/1744 | 프레임워크 | 2026/1744는 2026-07-08 채택, 2026-07-24 관보 게재 뒤 2026-07-27 발효했다. [사실][^ref-1517] 고위험 AI 요구(제III장 제1~3절)는 부속서 III 고위험에 2027-12-02부터(제6조5항 제외), 제6조1항·부속서 I 고위험에 2028-08-02부터 적용되고, 제102~110조는 2026-07-27부터 적용된다. [사실][^ref-1517] 이 세 날짜는 [43. 데이터·관측성·배포의 다른 연구영역과의 연결 주제 페이지](../../topics/2026/2026-10-09-area43-s10.md)에 이미 있는 내용이며, 여기서는 근거를 관보 원문으로 올린 것이다. 2026/1744는 기계규정 (EU) 2023/1230을 부속서 I Section A에서 Section B로 옮겼고, 바뀐 제2조2항은 Section B 대상 제품과 관련해 고위험이 되는 AI에 제6조1항·제60a조·제102~112조만 적용한다(제57~59조는 그 법령에 고위험 AI 요구가 통합된 범위에서만). [사실][^ref-1517] 이 구조로 보면 기계류 로봇의 고위험 AI 요구는 2028-08-02에 AI Act에서 직접 적용되는 것이 아니라 기계규정 부속서 III을 거쳐 반영되는 것으로 보인다. [추정][^ref-1517] 반면 기존 위키 서술(같은 주제 페이지, [M. 안전](../safety/index.md)·[L. AI·학습 기술](../ai-and-learning/index.md) 대분류 페이지)은 '기계류 등 부속서 I 제품에 내장되면 2028-08-02'로 적고 2차 해설도 엇갈리므로, 두 서술을 함께 두고 oq-106에서 다룬다. | [^ref-1517] |\n| EU 기계류 규정 (EU) 2023/1230 — AI 위임법령 경로 | 프레임워크 | 2026/1744 제3조는 기계규정 제8조에 위임 권한을 더해, 위원회가 위임법령으로 부속서 III에 고위험 AI의 보건·안전 요구(AI Act 제III장 제2절과 제17·19·72·73조를 반영)를 추가하게 했다. [사실][^ref-1517] 그 위임법령은 조문 문언대로 2028-08-02까지 적용(shall apply by)되도록 정해졌고, 위임 권한은 2026-07-27부터 5년이다. [사실][^ref-1517] 새 제20조10항은 기계규정상 AI 조화 표준·공통 사양이 나오기 전까지 AI Act 제40·41조의 조화 표준·공통 사양을 준수한 고위험 AI를 부속서 III의 AI 관련 요구에 적합한 것으로 추정한다([적합성 추정](../../glossary/presumption-of-conformity.md)). [사실][^ref-1517] 위임법령의 번호와 채택 여부는 확인되지 않았다(새 열린 질문). | [^ref-1517] |\n| EU 개정 제조물책임지침 (Directive (EU) 2024/2853) — 근거 교체 | 프레임워크 | 원판 제2조1항은 적용 대상을 'after 9 December 2026'에 출시·사용 개시된 제품으로 적었으나, 2026-05-07 정오표(OJ L 2026/90364)가 이를 'after 8 December 2026'으로 고쳤다. [사실][^ref-1529][^ref-1530] 따라서 적용 시점은 2026-12-08 후(정오표 2026-05-07, OJ L 2026/90364 기준), 곧 2026-12-09에 출시·사용 개시된 제품부터다. [사실][^ref-1529][^ref-1530] 제2조2항은 상업 활동 밖의 FOSS를 적용에서 빼고, 제4조1항은 소프트웨어·디지털 제조 파일을 제품에 포함한다. [사실][^ref-1529] 주제 페이지 표의 같은 행은 날짜(2026-12-09 이후)는 이와 같지만 근거가 정오표 전 해설이므로, 근거는 관보 원문과 정오표로 읽는다. [추정][^ref-1227][^ref-1529][^ref-1530] | [^ref-1529][^ref-1530] |\n| 인공지능 기본법 — 제33·35조 | 프레임워크 | 제33조(고영향 해당 여부 사전 검토 의무, 장관 확인 요청은 재량)와 제35조(영향평가 노력의무)를 조문 근거로 더했다(4절). 열람한 판은 법률 제21311호다. [사실][^ref-1518] 두 조의 시행 시점은 4절의 단서와 함께 추정으로 둔다. | [^ref-1518] |\n| EU 사이버복원력법 (Regulation (EU) 2024/2847) — 기산점·오픈소스 | 프레임워크 | 기존 기한(24시간·72시간·14일·1개월)은 유지하고, 기산점(인지 시점, 시정 조치 이용 가능 시점, 사고 통지 제출 시점)을 6절에 더했다. [사실][^ref-1522] 오픈소스 스튜어드 보고 의무는 제24조3항·제71조2항에 따라 2027-12-11부터 적용된다(4절). [사실][^ref-1522][^ref-1523] CRA의 오픈소스 적용 범위는 조문이 아니라 전문 (18)에 근거하는데, 전문 (18)은 상업 활동 과정에서 공급되는 자유·오픈소스 소프트웨어만 적용 대상으로 보고, 자기 책임 아래 있지 않은 제품에 소스 코드를 기여하는 자에게는 적용되지 않는다고 적는다. [사실][^ref-1522] | [^ref-1522][^ref-1523] |\n| 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (산업통상부고시 제2025-21호) | 평가 프로그램 | 심사항목 16개→8개 통·폐합을 담은 개정 고시로 2025-11-24 발령·시행됐다(행정예고안은 공고 제2025-042호). [사실][^ref-1519][^ref-1469] 제8조1항2호의 관제장치 일부 변경 시 심사 면제 조항은 리서치 단계 원문 열람 기준으로만 확인됐다(4절). [추정][^ref-1469] | [^ref-1519][^ref-1469] |\n| 지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의10 (책임보험 등의 가입금액) | 프레임워크 | 실외이동로봇 사고배상 책임보험·공제의 법령 기준 금액을 정한다(5절). [사실][^ref-1520] 같은 시행규칙의 제7조의4·5는 [ref-1470](../../references/ref-1470.md)으로 따로 인용된다. | [^ref-1520] |\n| Apache License 2.0 | 오픈소스 | 재배포 때 라이선스 사본 제공, 수정 파일 고지, NOTICE 귀속 고지를 요구한다(6절). [사실][^ref-1524] | [^ref-1524] |\n| REUSE 명세 3.3 | 프레임워크 | 주석을 넣을 수 없는 파일의 권리 정보를 .license 인접 파일 또는 REUSE.toml로 표기한다(6절). [사실][^ref-1525] | [^ref-1525] |\n| SPDX 라이선스 표현식 (명세 2.2.2 부록 D)과 reuse lint | 표준 / 오픈소스 | OR(선택)·AND(동시 준수) 연산자로 라이선스 조합을 표현하고, reuse lint는 유효하지 않은 표현식을 검사하는 항목을 두었다고 기록한다(프로젝트 자체 변경기록 기준, 6절). [사실][^ref-1527][^ref-1526] 주제 페이지 표의 SPDX 개요 행을 보강한다. | [^ref-1527][^ref-1526] |\n| NVIDIA GR00T-N1.6-3B 가중치 라이선스 | 오픈소스(가중치 공개, 비상업 라이선스) | 가중치를 연구·평가 목적의 비상업 용도로만 쓰게 한다(6절). [추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)[^ref-1528] | [^ref-1528] |\n\n[표준 목록](../../standards/index.md)에도 새 항목을 더한다.\n"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "\n### 2026-10-12 보강\n\n- 김정욱·성현지·유성희, 한·싱가포르 규제샌드박스 비교를 통한 AI 샌드박스 효율화 방안 제언(2025, 규제연구 34권 1호) — 싱가포르 IMDA(Infocomm Media Development Authority)가 시행한 AI 샌드박스 2건이 모두 기술 개발·혁신 지원에 가까운 형태이며, 한국과 달리 규제 특례 부여를 목적으로 하지 않는다고 구분한다. [사실][^ref-1531] 제도 비교 연구이며 로봇 실증 연구가 아니다.\n- 관보 원문 자료: AI Act 디지털 옴니버스 (EU) 2026/1744, 사이버복원력법 (EU) 2024/2847, 개정 제조물책임지침 (EU) 2024/2853과 그 정오표(2026-05-07)를 1차 근거로 더했다(7절). [사실][^ref-1517][^ref-1522][^ref-1529][^ref-1530]\n- 주제 페이지의 Gibson Dunn 해설(2026-03-23) 항목은 적용 시점·FOSS 제외·제품 정의를 관보 원문과 정오표로 대체하고, 증거 공개·결함 추정 같은 나머지 서술은 해설 기준으로 둔다. [추정][^ref-1227][^ref-1529][^ref-1530]\n"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "\n### 2026-10-12 보강: ROP가 직접 맡을 기록 업무 (구축자 의견)\n\n아래는 이번 실행에서 확인한 조문으로부터 이 위키가 도출한 구축자 의견이다. 어떤 ROP 기능이나 사업자가 고영향 인공지능, CRA 제조자, 상업적 사용 허용 대상 등에 해당한다고 판정하지 않으며, 해당성 판단은 운영자·법률 검토·규제 기관 쪽의 연계 대상이다.\n\n- **규제 대장**: AI Act 적용을 하나의 날짜로 묶지 말고 관할, 분류 경로(부속서 III / 부속서 I Section A / Section B), 근거 조항, 적용일을 따로 기록하고, 기계류 로봇의 AI 요구는 기계규정 제8조 위임법령 채택을 별도 추적 항목으로 둬야 한다고 본다(구축자 의견). [의견][^ref-1517] 기계류 로봇의 AI 적용 경로는 7절의 기계규정 경로 해석(추정)과 기존 위키의 '부속서 I 기계류 2028-08-02' 서술이 함께 있으며 oq-106에서 열려 있다.\n- **고영향 검토 기록**: 운영 준비에 고영향 해당성 사전 검토, 장관 확인 요청 여부, 영향평가 노력의 기록을 별도 업무로 두고, 사람이 최종 결정하면 고영향에서 제외된다는 정부 설명만으로 모든 ROP 기능을 면제 처리하지 않아야 한다고 본다(구축자 의견). [의견][^ref-1518][^ref-1235]\n- **보험 상태**: 보험 확인 규칙은 국가 이름 하나가 아니라 관할, 운영자, 플릿(합산 운행) 단위, 적용 시점으로 구성해야 한다고 본다(구축자 의견). [의견][^ref-1238][^ref-1521][^ref-1520]\n- **보고 기한 기록과 역할 대장**: 취약점 인지, 사고 인지, 시정 조치 이용 가능, 사고 통지 제출 시각을 따로 기록해 기한 계산 이력을 남기고, 배포 제품·유료 서비스·직접 개발·외부 기여·스튜어드 역할을 릴리스와 계약별로 나눈 책임 대장을 둬야 한다고 본다(구축자 의견). [의견][^ref-1522]\n- **릴리스 권리 검사**: 릴리스 파이프라인에서 SPDX 표현식 문법 검사와 파일별 권리 정보(.license·REUSE.toml) 검사를 자동화하되 권리 범위·배포 조건 검토 결과는 따로 보존하고, 메시·텍스처 같은 시뮬레이션 자산의 권리 정보를 모델 전체 코드 LICENSE와 분리해 추적해야 한다고 본다(구축자 의견). [의견][^ref-1525][^ref-1527][^ref-1526] 배포 심사에서는 모델 가중치의 커밋과 LICENSE를 코드 라이선스와 분리해 등록해야 한다고 본다(구축자 의견). [의견][^ref-1528]\n- **규제 검증 계획**: 의무·책임자·시험·증거·제출처를 연결하고, 규제 특례(샌드박스) 승인을 받은 것과 기술 검증 프로그램에 참가한 것을 구분해 기록해야 한다고 본다(구축자 의견). [의견][^ref-1531]\n"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "\n### 2026-10-12 보강\n\n- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) — (EU) 2026/1744로 기계규정 대상 로봇의 고위험 AI 보건·안전 요구가 기계규정 제8조 위임법령(부속서 III)을 거쳐 반영되는 경로가 생겨, 기계 안전 요구와 AI 규제 적용 경로가 만난다. [사실][^ref-1517]\n- [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md) — 모델 가중치의 라이선스를 코드와 분리해 등록하자는 구축자 의견(9절)이 두 영역을 잇는다. [의견][^ref-1528] GR00T-N1.6-3B 가중치는 비상업(연구·평가) 사용으로 제한된다. [추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)[^ref-1528]\n"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "\n### 2026-10-12 갱신\n\n2026-09-30 실행에서 올린 새 질문 5건의 id는 oq-288·oq-289·oq-290·oq-291·oq-292다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.\n\n**해결**\n\n- **oq-288** (상태: 해결 · 실행 2026-10-12-02) 한국 실외이동로봇 책임보험·공제의 가입금액은 지능형로봇법 시행규칙 제7조의10이 정하며, 금액은 5절에 있다. [사실][^ref-1520]\n\n**부분 근거만 확인, 열림 유지**\n\n- **oq-143** (상태: 열림) AI Act 고위험 적용일과 Section B 제품의 적용 조항, 인공지능 기본법 제33·35조의 의무 강도를 확인했다(4·7절). 로봇 대화 기능의 분류와 대화 기록 로그 항목·보존 기간은 답하지 못했다.\n- **oq-186** (상태: 열림) 16개→8개 개정의 근거(행정예고 공고 제2025-042호, 고시 제2025-21호, 2025-11-24 시행)를 확인했다(5절). 알림음·등화장치가 어디로 옮겨졌는지는 확인되지 않았다.\n- **oq-187** (상태: 열림) 고시 제8조1항2호의 관제장치 일부 변경 시 심사 면제 조항은 리서치 단계 원문 열람 기준으로만 확인됐다. [추정][^ref-1469] 오케스트레이션 계층이 인증상 관제장치에 해당하는지에 대한 해석은 없다.\n- **oq-289** (상태: 열림) 개정 제조물책임지침의 적용 시점과 비상업 FOSS 제외를 확인했으나(3·7절), 오케스트레이션 소프트웨어를 어떻게 다루는지에 대한 판정 자료는 없다.\n- **oq-291** (상태: 열림) CRA 보고 기한의 기산점과 오픈소스 스튜어드의 적용 범위·시점을 확인했으나(4·6·7절), 오케스트레이션 플랫폼 사업자의 제조자 해당성은 답하지 못했다.\n- **oq-292** (상태: 열림) REUSE 3.3의 .license 인접 파일·REUSE.toml 방법과 SPDX 표현식 검사를 확인했으나(6절), 3D 로봇 자산의 라이선스를 SPDX로 기술한 사례는 찾지 못했다.\n\n**다른 영역 질문과의 연결**\n\n- oq-106: 기계류 로봇 AI의 적용 경로가 (EU) 2026/1744로 바뀌었고(7절), 이 위키의 기존 서술과 엇갈린다.\n- oq-316·oq-338: 바뀐 AI Act 제2조2항의 적용 조항 한정(7절)이 근거가 된다.\n- oq-313: 시행규칙 제7조의10이 지능형로봇법 제40조의4에 근거한다는 점만 확인했다. [사실][^ref-1520]\n\n**이번에 답하지 못한 질문**: oq-173, oq-231, oq-239, oq-249, oq-250, oq-262, oq-275, oq-279, oq-282, oq-290.\n\n**새 질문**(id는 게시 때 부여)\n\n- (EU) 2026/1744로 기계규정 제8조에 근거가 생긴, 고위험 AI의 보건·안전 요구를 기계규정 부속서 III에 추가하는 위원회 위임법령은 채택됐는가? 채택됐다면 번호와 반영한 AI Act 요구(제III장 제2절, 제17·19·72·73조)의 범위는 무엇이며, 여러 로봇을 지시하는 오케스트레이션 소프트웨어의 AI도 그 대상에 드는가? (관련: 59. 법·규제·보험·라이선스, 48. 안전·위험 관리)\n- 국내 실외이동로봇 책임보험·공제의 실제 보험사 약관은 시행규칙 제7조의10 기준 금액 외에 관제 장애·통신 단절·사이버 사고로 생긴 손해와 제조사·관제 사업자에 대한 구상을 어떻게 다루는가? (관련: 59. 법·규제·보험·라이선스, 66. 실외)\n"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(3,306자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"11. 열린 질문\" 절(1,771자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"4. 핵심 개념과 용어\" 절(1,656자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"6. 대표 접근법과 기술\" 절(1,484자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"3. 왜 중요한가\" 절(586자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"8. 대표 연구와 자료\" 절(579자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area59-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 59. 법·규제·보험·라이선스 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(408자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-12 | 59. 법·규제·보험·라이선스 | 차등 갱신: AI Act 디지털 옴니버스·기계규정 위임법령 경로, 제조물책임지침 정오표 기준 적용 시점, 인공지능 기본법 제33·35조, CRA 보고 기산점·스튜어드, 실외이동로봇 책임보험 법령 기준 금액(oq-288 해결), 16개→8개 근거 고시 정정, 라이선스 검사 근거 보강. 트랙 반영 제안(2026-10-09-26 건축 도면 자동 인식 단계 2, 학습 데이터 라이선스 사례)은 이번 브리프에 근거 finding 이 없어 7절에 반영하지 않고 제안 상태 유지 | run 2026-10-12-02",
  "index_updates": {
    "home_recent": "2026-10-12 — 59. 법·규제·보험·라이선스: EU AI Act 디지털 옴니버스·제조물책임지침 정오표·CRA 보고 기산점·실외이동로봇 책임보험 법령 기준 금액·라이선스 검사 근거를 관보·법령 원문으로 보강(oq-288 해결)",
    "category_recent": "2026-10-12 — 59. 법·규제·보험·라이선스: 기계류 로봇 AI 요구의 기계규정 위임법령 경로, 제조물책임지침 적용 시점(2026-12-08 후, 정오표 기준), 인공지능 기본법 제33·35조, 책임보험 가입금액, Apache·REUSE·SPDX 라이선스 검사 보강",
    "area_recent": "2026-10-12 — 59. 법·규제·보험·라이선스: 5절 교체(책임보험 법령 기준 금액, 16개→8개 근거 고시, 버지니아 보험 단위, 홍콩 비교), 3·4·6·7·8·9·10·11절 보강 소절 추가, oq-288 해결"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1517",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI)",
      "published": "2026-07-24",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "AI Act 디지털 옴니버스 규정(OJ L 2026/1744). 고위험 적용일(2027-12-02·2028-08-02), 기계규정의 부속서 I Section B 이동, 제2조2항 적용 조항 한정, 기계규정 제8조 위임법령·제20조 적합 추정, 2026-07-27 발효를 담는다. 적용일 셋은 기존 ref-1322 기반 서술의 1차 근거다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1518",
      "org": "법제처 국가법령정보센터 (과학기술정보통신부)",
      "title": "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 [시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정] 제33조·제34조·제35조",
      "published": "2026-01-20",
      "url": "https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810895",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "인공지능 기본법의 열람한 판(법률 제21311호, 2026-07-21 시행) 조문. 제33조 고영향 사전 검토·확인 요청, 제35조 영향평가 노력의무. 법 최초 시행판(원판)은 별도 id ref-620(미열람)이다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1519",
      "org": "산업통상부 기계로봇제조정책과",
      "title": "실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정(안) 행정예고 (산업통상부 공고 제2025-042호)",
      "published": "2025-11-06",
      "url": "https://www.motir.go.kr/kor/article/ATCLa6723dc7b/458/view",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "2025-11-06 행정예고 공고와 첨부 개정안. 통보 기한 30일 명시(안 제9조), 심사항목 통·폐합 16개→8개(안 별표 3)를 담는다(행정예고안 기준). 최종 고시는 제2025-21호(ref-1469).",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1520",
      "org": "법제처 국가법령정보센터 (산업통상부)",
      "title": "지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의10(책임보험 등의 가입금액)",
      "published": "2025-10-01",
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=278777",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "시행규칙 현행 통합본. 제7조의10 실외이동로봇 책임보험·공제 보험금 기준(사망·후유장애 1억5천만원, 부상 3천만원, 재물 사고당 10억원)과 2023-11-17 신설 표시. 같은 시행규칙 제7조의4·5 는 별도 id ref-1470 이다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1521",
      "org": "Hong Kong SAR Government (Innovation, Technology and Industry Bureau)",
      "title": "LCQ20: Regulating operation of intelligent robots",
      "published": "2026-05-20",
      "url": "https://www.info.gov.hk/gia/general/202605/20/P2026052000416p.htm",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "입법회 질문에 대한 정부 서면 답변(2026-05-20). 지능형 로봇 사용에 제3자 책임보험을 강제하는 법정 요건이 없다고 밝혔다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1522",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act)",
      "published": "2024-11-20",
      "url": "https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "사이버복원력법 관보 원판. 제14조 보고 기한의 기산점, 제24조3항 오픈소스 스튜어드, 제71조2항 적용일, 전문 (18) 오픈소스 범위를 담는다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1523",
      "org": "European Union Agency for Cybersecurity (ENISA)",
      "title": "The CRA Single Reporting Platform is launched",
      "published": "2026-09-11",
      "url": "https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "ENISA 보도자료(2026-09-11). 단일 보고 플랫폼 가동과, 제조자 보고 의무(2026-09-11)와 스튜어드 보고 의무(제24조3항, 2027-12-11)의 적용일 구분을 밝힌다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1524",
      "org": "Apache Software Foundation",
      "title": "Apache License, Version 2.0",
      "published": "2004-01",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "Apache License 2.0 원문. 제4절 재배포 조건 (a) 라이선스 사본, (b) 수정 파일 고지, (d) NOTICE 귀속 고지.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1525",
      "org": "Free Software Foundation Europe (REUSE)",
      "title": "REUSE Specification – Version 3.3",
      "published": "2024-11-14",
      "url": "https://reuse.software/spec-3.3/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "파일별 저작권·라이선스 정보 표기 명세 3.3판. 주석을 넣을 수 없는 파일은 같은 이름 + .license 인접 파일, 또는 REUSE.toml 로 정보를 둔다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1526",
      "org": "FSFE reuse-tool 기여자 (GitHub)",
      "title": "reuse-tool CHANGELOG.md (v6.1.0 태그)",
      "published": "2025-10-07",
      "url": "https://github.com/fsfe/reuse-tool/blob/v6.1.0/CHANGELOG.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "reuse-tool 프로젝트 자체 변경기록(v6.1.0). v6.0.0(2025-10-06)에서 'Invalid SPDX License Expressions' lint 항목을 추가했다고 기록한다. 실행 재현은 하지 않았다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1527",
      "org": "SPDX Project (Linux Foundation)",
      "title": "Annex D: SPDX License Expressions - specification v2.2.2",
      "published": null,
      "url": "https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "SPDX 2.2.2 명세 부록 D. 라이선스 표현식 문법과 OR(선택)·AND(동시 준수)·WITH 연산자를 정의한다. 발행일 미확인.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1528",
      "org": "NVIDIA (Hugging Face 모델 저장소)",
      "title": "GR00T-N1.6-3B / LICENSE (NVIDIA License)",
      "published": "2025-12-15",
      "url": "https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/LICENSE",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "로봇 기반 모델 가중치 저장소의 고정 커밋(d0814e7) 라이선스 문서. 제3.3절 비상업(연구·평가) 사용 제한과 NVIDIA·계열사 예외. 벤더 라이선스 문면이며 발행일은 커밋 날짜다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1529",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC",
      "published": "2024-11-18",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "개정 제조물책임지침 관보 원판. 제2조1항 적용 시점(원판 'after 9 December 2026'), 제2조2항 비상업 FOSS 제외, 제4조1항 제품 정의. 비고: 2026-10-12-01 실행의 ref-1490(같은 Directive (EU) 2024/2853, ELI URL)과 같은 문서이므로 퍼블리셔 병합 판단에 쓴다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1530",
      "org": "European Parliament and Council of the European Union (Official Journal of the European Union)",
      "title": "Corrigendum to Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC",
      "published": "2026-05-07",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202690364",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "제조물책임지침 정오표(OJ L 2026/90364, 2026-05-07). 제2조1항의 'after 9 December 2026' 을 'after 8 December 2026' 으로 고친다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1531",
      "org": "김정욱·성현지·유성희",
      "title": "한·싱가포르 규제샌드박스 비교를 통한 AI 샌드박스 효율화 방안 제언",
      "published": "2025-06",
      "url": "https://journal.kci.go.kr/ksrs2002/archive/articlePdf?artiId=ART003225249",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "규제연구 34권 1호(DOI 10.22954/ksrs.2025.34.1.003). 한국 규제샌드박스와 싱가포르 IMDA AI 샌드박스를 비교한 제도 연구로, 로봇 실증 연구는 아니다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1238",
      "org": "Commonwealth of Virginia (Code of Virginia)",
      "title": "§ 46.2-908.1:1. Personal delivery devices",
      "published": null,
      "url": "https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "버지니아주 개인 배송 장치 조문(기존 출처). 재열람에서 E항 보험이 운영자 통제 아래 장치들의 합산 운행 손해를 대상으로 함을 확인했다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
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
      "accessed": "2026-10-12",
      "summary": "현행 운행안전인증 고시(기존 출처, 산업통상부 누리집 표기 제2025-021호). 2025-11-24 시행 표시, 제8조①2호(관제장치 일부 변경 시 심사 면제, 검증 단계 미확인), 제9조①(30일 이내 통보).",
      "cited_by": [
        "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-288",
      "question": "한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가?",
      "areas": [
        59,
        66
      ],
      "status": "해결",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시"
    },
    {
      "action": "new",
      "question": "(EU) 2026/1744 로 기계규정 제8조에 근거가 생긴, 고위험 AI 의 보건·안전 요구를 기계규정 부속서 III 에 추가하는 위원회 위임법령은 채택됐는가, 채택됐다면 번호와 반영한 AI Act 요구(제III장 제2절, 제17·19·72·73조)의 범위는 무엇이며 여러 로봇을 지시하는 오케스트레이션 소프트웨어의 AI 도 그 대상에 드는가?",
      "areas": [
        59,
        48
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 실외이동로봇 책임보험·공제의 실제 보험사 약관은 시행규칙 제7조의10 기준 금액 외에 관제 장애·통신 단절·사이버 사고로 생긴 손해와 제조사·관제 사업자에 대한 구상을 어떻게 다루는가?",
      "areas": [
        59,
        66
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시",
      "title": "59. 법·규제·보험·라이선스"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시",
      "title": "59. 법·규제·보험·라이선스"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#5-적용-사례-현장-유형-명시",
      "title": "59. 법·규제·보험·라이선스"
    }
  ],
  "standards_updates": [
    {
      "name": "EU AI Act 디지털 옴니버스 (Regulation (EU) 2026/1744)",
      "kind": "프레임워크",
      "org": "European Parliament and Council of the European Union",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744",
      "related_areas": [
        59,
        47,
        48
      ],
      "summary": "AI Act 고위험 적용일(부속서 III 2027-12-02, 부속서 I 2028-08-02)을 정하고 기계규정을 부속서 I Section B 로 옮기며, 기계규정 제8조 위임법령으로 고위험 AI 요구를 부속서 III 에 더하는 경로를 둔다. 2026-07-27 발효.",
      "ref_id": "ref-1517"
    },
    {
      "name": "지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의10 (실외이동로봇 책임보험 등의 가입금액)",
      "kind": "프레임워크",
      "org": "산업통상부",
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=278777",
      "related_areas": [
        59,
        66
      ],
      "summary": "실외이동로봇 사고배상 책임보험·공제의 법령 기준 금액(사망·후유장애 1인당 1억5천만원, 부상 1인당 3천만원, 재물 사고당 10억원)을 정한다. 2023-11-17 신설.",
      "ref_id": "ref-1520"
    },
    {
      "name": "Apache License 2.0",
      "kind": "오픈소스",
      "org": "Apache Software Foundation",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
      "related_areas": [
        59,
        57
      ],
      "summary": "재배포 때 라이선스 사본 제공, 수정 파일 변경 고지, NOTICE 귀속 고지 포함을 요구하는 오픈소스 라이선스.",
      "ref_id": "ref-1524"
    },
    {
      "name": "REUSE Specification 3.3",
      "kind": "프레임워크",
      "org": "Free Software Foundation Europe (REUSE)",
      "url": "https://reuse.software/spec-3.3/",
      "related_areas": [
        59,
        36,
        57
      ],
      "summary": "파일별 저작권·라이선스 정보 표기 명세. 주석을 넣을 수 없는 파일은 .license 인접 파일이나 REUSE.toml 로 권리 정보를 둔다.",
      "ref_id": "ref-1525"
    },
    {
      "name": "reuse-tool (reuse lint)",
      "kind": "오픈소스",
      "org": "FSFE reuse-tool 기여자",
      "url": "https://github.com/fsfe/reuse-tool/blob/v6.1.0/CHANGELOG.md",
      "related_areas": [
        59,
        57
      ],
      "summary": "REUSE 명세 준수를 검사하는 도구. 프로젝트 자체 변경기록 기준 v6.0.0(2025-10-06)에서 유효하지 않은 SPDX 라이선스 표현식 검사 항목을 추가했다.",
      "ref_id": "ref-1526"
    }
  ],
  "additional_research_requests": [
    "분리된 주제 페이지(2026-09-30-area59-s3·s4·s6·s7·s8·s11)의 본문이 이번 입력에 없어 그 안의 PLD 행·Gibson Dunn 근거 문장·'새 질문 5건' 표기를 직접 교체하지 못하고 세부영역 페이지 각 절에 '2026-10-12 보강' 소절로 덧붙였다. 다음 갱신 실행에서 해당 주제 페이지 본문을 입력으로 넣어 근거 교체(ref-1227 → ref-1529·ref-1530)를 마무리해야 한다.",
    "7절·9절: (EU) 2026/1744 에 따른 기계규정 제8조 위임법령의 채택 여부·번호와 반영 범위(새 열린 질문). 기계류 로봇 AI 적용 경로의 두 서술(기계규정 경로 vs 부속서 I 2028-08-02)을 가를 독립 1차·공식 해설이 필요하다(oq-106).",
    "4절: 인공지능 기본법 원판(ref-620)과 법률 제21311호 신구 대비표로 제35조1항의 개정 문장과 시행일을 확인해야 [추정]을 해소할 수 있다. 시행령(제33조④ 절차)도 미확인.",
    "4·7·11절: 고시 제2025-21호 제8조1항2호 문언은 검증 단계에서 열지 못해 [추정]으로 두었다. 국가법령정보센터 원문 재확인 또는 독립 자료가 필요하다(oq-187).",
    "5절: 2023 행정예고안의 알림음·등화장치 기준이 현행 별표 3 밖 어디로 옮겨졌는지(oq-186), 실제 보험사 약관의 보장 범위(새 열린 질문)가 필요하다.",
    "7절: 트랙 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2 — AI허브 원 이용정책과 CC BY-NC-SA 4.0 평면도 데이터셋의 상용 이용 제약)은 이번 브리프에 근거 finding 이 없어 반영하지 못했다. 다음 59. 법·규제·보험·라이선스 실행에서 그 finding(f4~f7, 실행 2026-10-09-26)의 출처를 브리프에 넣어야 한다.",
    "후속 정리(이번 갱신 범위 밖 페이지): 2026-10-09-area43-s10.md 44행의 ref-1322 기반 AI Act 날짜를 ref-1517 로 근거 교체, 같은 파일 45행과 categories/safety/index.md 149행·categories/ai-and-learning/index.md 131행의 '부속서 I 기계류 2028-08-02' 서술을 Section B 이동·기계규정 위임법령 경로와 함께 정리하는 실행이 필요하다(47. AI·학습·적응과 모델 운영, 48. 안전·위험 관리).",
    "이번 실행은 기존 페이지 갱신 1건만 사용했다(예산 2건 중)."
  ],
  "fixes_applied": [
    "f14 강등 — 4절 '인공지능 기본법 조문 판 표기' 항목에서 제33조에 개정 표시가 없다는 점만 [사실]로 두고, 원법부터의 의무·2026-07-21 이 발효일이 아니라는 판단은 [추정]으로 썼으며 제35조1항의 ‘개정 2026. 1. 20.’ 표시로 시행일이 2026-07-21 일 수 있다는 단서와 원판(ref-620)·신구 대비표 미확인을 함께 적었다.",
    "f17 강등 — 4·7·11절의 고시 제8조1항2호 문장을 모두 [추정]으로 쓰고 '리서치 단계 원문 열람 기준, 검증 단계 미확인'을 밝혔으며 oq-187 은 열림으로 유지했다.",
    "f6 와 기존 서술 병기 — 7절 새 AI Act·디지털 옴니버스 행에서 기계규정 경로 해석을 [추정]으로 쓰고 기존 위키 서술('기계류 등 부속서 I 제품에 내장되면 2028-08-02', 43 주제 페이지·M. 안전·L. AI·학습 기술 대분류 페이지)을 링크와 함께 제시해 oq-106 에 연결했고, 9절 규제 대장 항목에도 두 서술이 함께 있음을 적었다. 다른 페이지는 고치지 않았다.",
    "f1~f3 중복 표시 — 7절 행에서 날짜 셋이 2026-10-09-area43-s10 주제 페이지에 이미 있는 내용이며 근거를 관보 원문(ref-1517)으로 올린 것임을 밝혔다.",
    "f8 — 7절 기계류 규정 행에서 위임법령을 조문 문언대로 '2028-08-02 까지 적용(shall apply by)'으로만 쓰고 공표 기한 표현을 쓰지 않았다.",
    "f43 — 3절·7절에서 적용 시점을 '2026-12-08 후(정오표 2026-05-07, OJ L 2026/90364 기준), 곧 2026-12-09 에 출시·사용 개시된 제품부터'로 쓰고 '2026-12-08 이후'·'2026-12-08 부터' 표현을 쓰지 않았다.",
    "ref-1529 — reference_updates 의 summary 끝에 2026-10-12-01 실행의 ref-1490(같은 Directive (EU) 2024/2853, ELI URL)과 같은 문서라는 비고를 넣었다.",
    "f27·f28 용어 — 6절에서 '적극 악용 취약점'으로 쓰고 첫 등장에 glossary/actively-exploited-vulnerability.md 링크를 걸었다.",
    "f16·f17 고시 번호 — 4절 첫 등장에 '산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)'로 병기한 뒤 5·7·11절은 제2025-21호로 통일했다.",
    "f11~f15 표기 — 4절 첫 등장에 정식 명칭과 법령 약칭 '인공지능기본법'을 한 번 밝히고 이후 본문은 '인공지능 기본법'으로 썼다.",
    "f16 — 5절에서 공고 제2025-042호의 30일 통보·16개→8개를 '행정예고안 기준'으로 밝히고 최종 근거를 고시 제2025-21호(ref-1469)로 두었으며 별표 대응은 50. 안전 표준·인증·사고 조사 페이지 링크로만 처리했다. '개정 시점·근거 고시 … 확인하지 못했다' 문장을 이 내용으로 바꾸고 알림음·등화장치 이동 미확인(oq-186 열림) 단서는 남겼다.",
    "f18~f21 — 5절 한국 사례 '제약' 칸에 '지능형로봇법 시행규칙 제7조의10 의 법령 기준 금액'으로 쓰고, '예외·성과' 칸의 기존 미확인 문장은 '이 단체보험 상품의 보장 한도는 미확인이다'로 구분했으며, 표 아래에 f23 지표 구분을 [의견](구축자 의견)으로 붙였다.",
    "의견 표시 — f10·f15·f26·f32·f40·f42·f48 은 9절, f23 은 5절에 모두 [의견]과 '(구축자 의견)'으로 쓰고, 9절 머리에 어떤 ROP 기능·사업자의 법적 해당성도 판정하지 않는다고 밝혔다.",
    "f41 — 6절·10절에서 '[추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)'을 병기하고 다른 모델판·코드 저장소·별도 계약은 미확인으로 두었다.",
    "f39 — 6절에서 reuse lint 검사 항목을 '프로젝트 자체 변경기록(CHANGELOG v6.1.0 태그) 기준', '실행 재현 안 함'으로 밝혔다.",
    "f47 — 8절 항목에 '제도 비교 연구이며 로봇 실증 연구가 아니다'를 적었다.",
    "f31 — 7절 CRA 행에서 오픈소스 적용 범위가 조문이 아니라 전문 (18)에 근거함을 밝혔다.",
    "ref-1227·ref-1235 — 기존 각주 정의(접근일 2026-09-30)를 고치지 않았고 reference_updates 에도 넣지 않았다.",
    "인용 제한 — 직접 인용은 ref-1529('after 9 December 2026')·ref-1530('after 8 December 2026')·ref-1517('shall apply by')·ref-1238('combined operations')·ref-1518(‘개정 2026. 1. 20.’) 각 1회의 짧은 구절로 제한하고 나머지 조항은 재서술했다.",
    "11절 — oq-288 을 해결(근거 시행규칙 제7조의10)로 처리하고 open_question_updates 에 update 로 냈으며, oq-143·oq-186·oq-187·oq-289·oq-291·oq-292 는 부분 근거만 적고 열림을 유지했다. 지난 실행의 새 질문 5건을 oq-288~oq-292 로 표기하고, 새 열린 질문 2건(위임법령 채택, 보험 약관)을 관련 영역 번호와 이름을 함께 써서 등록했다.",
    "트랙 반영 제안(2026-10-09-26) — 브리프 근거가 없어 7절에 반영하지 않았고 미반영 사유를 changelog_entry 에 적었다.",
    "docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md: 각주 정의 16개를 참고문헌에서 만들어 붙임: ref-1469, ref-1517, ref-1518, ref-1519, ref-1520, ref-1521, ref-1522, ref-1523, ref-1524, ref-1525, ref-1526, ref-1527, ref-1528, ref-1529, ref-1530, ref-1531",
    "분량 초과 자동 분리: 59. 법·규제·보험·라이선스 본문 14,035자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,335자"
  ]
}
```

### runs/2026-10-12-02/pages/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md

```markdown
---
title: "59. 법·규제·보험·라이선스"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [실외이동로봇 운행안전인증, 책임보험, 제조물책임, 사이버복원력법, SBOM, 오픈소스 라이선스]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-12
sources: [ref-991, ref-1227, ref-1228, ref-1229, ref-1230, ref-1231, ref-1232, ref-980, ref-992, ref-1233, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-1212, ref-1469, ref-1517, ref-1518, ref-1519, ref-1520, ref-1521, ref-1522, ref-1523, ref-1524, ref-1525, ref-1526, ref-1527, ref-1528, ref-1529, ref-1530, ref-1531]
last_run: 2026-10-12
version: 3
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 59. 법·규제·보험·라이선스

# 59. 법·규제·보험·라이선스

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **법·규제 대응**: 기계류 규정·AI 규제·로봇 관련 법·개인정보 법·실외 로봇 운행 규정을 파악하고 대응한다
- **보험·사고 책임**: 사고 책임의 배분과 보험을 정한다
- **오픈소스·라이선스 관리**: 오픈소스·SDK·3D 자산의 라이선스를 지킨다

## 2. 핵심 질문

이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]

## 3. 왜 중요한가

로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1238][^ref-1237][^ref-1235][^ref-1228][^ref-1234][^ref-1227][^ref-1236]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 왜 중요한가](../../topics/2026/2026-10-12-area59-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 핵심 개념과 용어](../../topics/2026/2026-10-12-area59-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 실외

**사례:** 한국 보도에서 실외이동로봇 운행

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 운행안전인증 대상은 배송 등을 위해 자율주행(원격제어 포함)으로 운행하는 지능형 로봇과 그 운행에 필요한 관제장치의 조합이다. [사실][^ref-980] 운용자는 로봇을 정확히 조작하고 안전하게 운용할 의무를 진다. [사실][^ref-991] |
| 제약 | 2023-11-17부터 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하 실외이동로봇이 보행자 지위로 보도를 통행할 수 있다. [사실][^ref-991][^ref-980] 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지켜야 한다. [사실][^ref-991] 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 한다. [사실][^ref-991][^ref-1232] 그 보험금 기준은 지능형로봇법 시행규칙 제7조의10의 법령 기준 금액으로, 사망 1인당 1억5천만원(실손해액이 2천만원 미만이면 2천만원), 부상 1인당 3천만원, 후유장애 1인당 1억5천만원, 재물 사고당 10억원이다. [사실][^ref-1520] 이 조문은 2023-11-17 신설된 뒤 현행 통합본(산업통상부령 제1호, 2025-10-01 시행)까지 개정되지 않았다. [사실][^ref-1520] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있다. [사실][^ref-991] 한국로봇산업협회 발표를 전한 기사(ref-1232) 기준으로, 협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고 첫 가입 기업은 뉴빌리티·로보티즈였다. 이 단체보험 상품의 보장 한도는 미확인이다. [추정][^ref-1232] |

시행규칙 제7조의10의 금액은 법령이 정한 보험금 기준이며, 실제 보험 상품의 보장·면책·자기부담금·가입 기간이나 협회 단체보험의 보험료와는 다른 지표이므로 서로 다른 항목으로 기록해야 한다고 본다(구축자 의견). [의견][^ref-1520]

정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다(2023-11-16 발표). [사실][^ref-991] 운행안전인증은 서류심사→제품심사→인증표시 순으로 진행되고 신청일부터 30일 이내에 처리되며, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다(2026-09-30 확인). [사실][^ref-980]

제정 당시의 기준은 달랐다. 2023-07 산업통상자원부가 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다(2023-07 행정예고안 기준). [사실][^ref-992] 심사항목을 줄인 근거는 산업통상부 공고 제2025-042호(2025-11-06)의 행정예고다. 행정예고안은 인증 절차 간소화를 개정 이유로 들고, 심사결과 통보 기한 30일 이내 명시(안 제9조)와 심사항목 기준 통·폐합에 따른 16개→8개 축소(안 별표 3)를 담았다(행정예고안 기준). [사실][^ref-1519] 최종 근거는 이 개정을 반영해 2025-11-24 발령·시행된 고시 제2025-21호다. [사실][^ref-1469] 별표 항목이 어떻게 대응하는지는 [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md)에 정리돼 있다. 다만 2023 행정예고안의 알림음·등화장치 기준이 현행 별표 3 밖의 다른 규정으로 옮겨졌는지는 확인되지 않았다(oq-186 열림).

**현장 유형:** 실외

**사례:** 미국 버지니아주에서 개인 배송 장치를 보도로 운행 (해외 비교)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 장치에 운영자를 식별하는 표시를 단다. [사실][^ref-1238] |
| 제약 | [개인 배송 장치](../../glossary/personal-delivery-device.md)(Personal Delivery Device, PDD)는 보도·횡단보도에서 시속 10마일 이하로 운행한다. [사실][^ref-1238] 운영자는 자기 통제 아래 있는 개인 배송 장치들의 합산 운행(combined operations)으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지해야 하며, 이 금액은 장치당 한도로 정해져 있지 않다. [사실][^ref-1238] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 버지니아주법 §46.2-908.1:1 기준이며(2026-09-30 확인, 보험 단위는 2026-10-12 재확인), 지방정부는 추가 안전 요건을 둘 수 있다. [사실][^ref-1238] 미국 주법이므로 한국 현장에 바로 적용되지 않으며, 한국 사례와 운행 속도·보험 요구를 비교하는 해외 비교 사례로만 둔다.

비교하면, 홍콩 정부는 2026-05-20 입법회 서면 답변(LCQ20)에서 사적·상업적 목적의 지능형 로봇 사용에 제3자 책임보험 가입을 강제하는 법정 요건이 당시 홍콩에 없다고 밝혔다. [사실][^ref-1521]

이번 조사에서 근거를 찾은 현장 유형은 실외뿐이다. 물류창고·제조 공장·병원·상업 시설·가정의 사례는 이번 조사에서 찾지 못했다.

## 6. 대표 접근법과 기술

확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1228][^ref-1236]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area59-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1238][^ref-1227][^ref-1212][^ref-1228][^ref-1233][^ref-1235][^ref-1234][^ref-1237][^ref-1236][^ref-1229][^ref-1230][^ref-1231]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area59-s7.md)에 있다.

## 8. 대표 연구와 자료

이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 대표 연구와 자료](../../topics/2026/2026-10-12-area59-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 업종별 조건 | 로봇별 인증·보험 상태와 인증 조건(관제장치 조합, 속도·질량·운행 구역)을 등록 정보와 작업·경로 제약으로 반영하고, 촬영 표시 같은 규제 상태를 운영 조건으로 확인한다. [추정][^ref-980][^ref-991][^ref-1234] | 인증 취득과 법적 적합성 판단(제조사·운영자), 보험 계약과 보상(운영자·보험사·협회), 제조물 책임 판정(당사자·법원), 개인정보 처리 적법성 판단(개인정보처리자)은 연계 대상으로 보인다. [추정][^ref-980][^ref-1232][^ref-1233][^ref-1227][^ref-1234] |
| 시설·설비 제어 | 사업장 안전검사 결과를 받아 작업·경로·권한 제약으로 반영한다. [추정][^ref-1237] | 산업용 로봇 안전검사는 사업주가 맡는 연계 대상으로 보인다. [추정][^ref-1237] |

분류 원문 19장의 [범위 경계](../../about/scope-boundary.md)는 업종별 조건에서 ROP가 "해당 조건을 작업·경로·권한 제약으로 반영"한다고 정한다. 이 영역에서 ROP는 법적 판단을 내리지 않고 그 결과를 받아 반영하며 근거 기록을 제공하는 쪽인 것으로 보인다. [추정][^ref-980][^ref-1237] 그 밖에 사고·취약점 보고와 책임 판단에 필요한 실행 기록을 남기는 일과 플랫폼 배포물의 라이선스·소프트웨어 자재명세서(Software Bill of Materials, SBOM) 목록을 관리하는 일은 ROP 직접 범위로 보인다. [추정][^ref-1228][^ref-1230][^ref-1236] 오케스트레이션 계층이 운행안전인증상 관제장치에 해당하면 경계가 달라질 수 있으나, 이에 대한 기준은 확인되지 않았다(oq-187).

### 2026-10-12 보강: ROP가 직접 맡을 기록 업무 (구축자 의견)

아래는 이번 실행에서 확인한 조문으로부터 이 위키가 도출한 구축자 의견이다. 어떤 ROP 기능이나 사업자가 고영향 인공지능, CRA 제조자, 상업적 사용 허용 대상 등에 해당한다고 판정하지 않으며, 해당성 판단은 운영자·법률 검토·규제 기관 쪽의 연계 대상이다.

- **규제 대장**: AI Act 적용을 하나의 날짜로 묶지 말고 관할, 분류 경로(부속서 III / 부속서 I Section A / Section B), 근거 조항, 적용일을 따로 기록하고, 기계류 로봇의 AI 요구는 기계규정 제8조 위임법령 채택을 별도 추적 항목으로 둬야 한다고 본다(구축자 의견). [의견][^ref-1517] 기계류 로봇의 AI 적용 경로는 7절의 기계규정 경로 해석(추정)과 기존 위키의 '부속서 I 기계류 2028-08-02' 서술이 함께 있으며 oq-106에서 열려 있다.
- **고영향 검토 기록**: 운영 준비에 고영향 해당성 사전 검토, 장관 확인 요청 여부, 영향평가 노력의 기록을 별도 업무로 두고, 사람이 최종 결정하면 고영향에서 제외된다는 정부 설명만으로 모든 ROP 기능을 면제 처리하지 않아야 한다고 본다(구축자 의견). [의견][^ref-1518][^ref-1235]
- **보험 상태**: 보험 확인 규칙은 국가 이름 하나가 아니라 관할, 운영자, 플릿(합산 운행) 단위, 적용 시점으로 구성해야 한다고 본다(구축자 의견). [의견][^ref-1238][^ref-1521][^ref-1520]
- **보고 기한 기록과 역할 대장**: 취약점 인지, 사고 인지, 시정 조치 이용 가능, 사고 통지 제출 시각을 따로 기록해 기한 계산 이력을 남기고, 배포 제품·유료 서비스·직접 개발·외부 기여·스튜어드 역할을 릴리스와 계약별로 나눈 책임 대장을 둬야 한다고 본다(구축자 의견). [의견][^ref-1522]
- **릴리스 권리 검사**: 릴리스 파이프라인에서 SPDX 표현식 문법 검사와 파일별 권리 정보(.license·REUSE.toml) 검사를 자동화하되 권리 범위·배포 조건 검토 결과는 따로 보존하고, 메시·텍스처 같은 시뮬레이션 자산의 권리 정보를 모델 전체 코드 LICENSE와 분리해 추적해야 한다고 본다(구축자 의견). [의견][^ref-1525][^ref-1527][^ref-1526] 배포 심사에서는 모델 가중치의 커밋과 LICENSE를 코드 라이선스와 분리해 등록해야 한다고 본다(구축자 의견). [의견][^ref-1528]
- **규제 검증 계획**: 의무·책임자·시험·증거·제출처를 연결하고, 규제 특례(샌드박스) 승인을 받은 것과 기술 검증 프로그램에 참가한 것을 구분해 기록해야 한다고 본다(구축자 의견). [의견][^ref-1531]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1234][^ref-1228][^ref-1227]

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결](../../topics/2026/2026-10-12-area59-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 열린 질문 12건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [59. 법·규제·보험·라이선스 — 열린 질문](../../topics/2026/2026-10-12-area59-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md) — 영역 심화: 3~11절 첫 작성(seed → draft), 13절 각주 16건, 프런트매터 related_areas·tags·sources·confidence·last_run 채움(2차 수정: 열린 질문 12건, 구축자 의견 표시, 7절 각주 보강, SBOM 풀어쓰기, 8절 문장 정리) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area59-s7.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다(2차 수정: 요약 문장 각주 보강, ROS 2 행 표현, ENISA·SBOM 풀어쓰기) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 열린 질문](../../topics/2026/2026-09-30-area59-s11.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "11. 열린 질문" 절을 옮겼다(2차 수정: 기존 열린 질문 12건, oq-275·oq-279·oq-282 추가) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area59-s4.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 수정: 구축자 의견 표시, ENISA 풀어쓰기) (실행 2026-09-30-23)
- 2026-09-30 · 생성 · [59. 법·규제·보험·라이선스 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area59-s6.md) — 자동 분리: 59. 법·규제·보험·라이선스 의 "6. 대표 접근법과 기술" 절을 옮겼다(2차 수정: SBOM 풀어쓰기) (실행 2026-09-30-23)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30
[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1230]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1232]: 지디넷코리아, "실외 이동로봇 필수보험 94% 저렴하게", 2024-02-08, https://zdnet.co.kr/view/?no=20240208201432, 접근일 2026-09-30
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-992]: 지디넷코리아, 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 심사, 2023-07-28, https://zdnet.co.kr/view/?no=20230728173101, 접근일 2026-09-30
[^ref-1233]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1234]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1235]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1236]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1237]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1238]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-1229]: ROS (ros-infrastructure/rep), REP 2004 -- Package Quality Categories, 2019-12-17, https://ros.org/reps/rep-2004.html, 접근일 2026-09-30
[^ref-1231]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-1212]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30 (원문 미열람)

[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-12
[^ref-1517]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI), 2026-07-24, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744, 접근일 2026-10-12
[^ref-1518]: 법제처 국가법령정보센터 (과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 [시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정] 제33조·제34조·제35조, 2026-01-20, https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810895, 접근일 2026-10-12
[^ref-1519]: 산업통상부 기계로봇제조정책과, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정(안) 행정예고 (산업통상부 공고 제2025-042호), 2025-11-06, https://www.motir.go.kr/kor/article/ATCLa6723dc7b/458/view, 접근일 2026-10-12
[^ref-1520]: 법제처 국가법령정보센터 (산업통상부), 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의10(책임보험 등의 가입금액), 2025-10-01, https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=278777, 접근일 2026-10-12
[^ref-1521]: Hong Kong SAR Government (Innovation, Technology and Industry Bureau), LCQ20: Regulating operation of intelligent robots, 2026-05-20, https://www.info.gov.hk/gia/general/202605/20/P2026052000416p.htm, 접근일 2026-10-12
[^ref-1522]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act), 2024-11-20, https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng, 접근일 2026-10-12
[^ref-1525]: Free Software Foundation Europe (REUSE), REUSE Specification – Version 3.3, 2024-11-14, https://reuse.software/spec-3.3/, 접근일 2026-10-12
[^ref-1526]: FSFE reuse-tool 기여자 (GitHub), reuse-tool CHANGELOG.md (v6.1.0 태그), 2025-10-07, https://github.com/fsfe/reuse-tool/blob/v6.1.0/CHANGELOG.md, 접근일 2026-10-12
[^ref-1527]: SPDX Project (Linux Foundation), Annex D: SPDX License Expressions - specification v2.2.2, 미확인, https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/, 접근일 2026-10-12
[^ref-1528]: NVIDIA (Hugging Face 모델 저장소), GR00T-N1.6-3B / LICENSE (NVIDIA License), 2025-12-15, https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/LICENSE, 접근일 2026-10-12
[^ref-1531]: 김정욱·성현지·유성희, 한·싱가포르 규제샌드박스 비교를 통한 AI 샌드박스 효율화 방안 제언, 2025-06, https://journal.kci.go.kr/ksrs2002/archive/articlePdf?artiId=ART003225249, 접근일 2026-10-12
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s7.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1212, ref-1227, ref-1228, ref-1229, ref-1230, ref-1231, ref-1233, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-1469, ref-1517, ref-1518, ref-1519, ref-1520, ref-1522, ref-1523, ref-1524, ref-1525, ref-1526, ref-1527, ref-1528, ref-1529, ref-1530, ref-980, ref-991]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#7
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스

# 59. 법·규제·보험·라이선스 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1238][^ref-1227][^ref-1212][^ref-1228][^ref-1233][^ref-1235][^ref-1234][^ref-1237][^ref-1236][^ref-1229][^ref-1230][^ref-1231]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사로 확인한 규범은 한국 실외 로봇 법령과 운행안전인증, 해외 실외 배송 로봇 주법, EU의 제조물 책임·기계·사이버보안 규범, 한국의 제조물책임·AI·개인정보·산업안전 법령, ROS 2·SPDX·Gazebo의 라이선스 규칙이다. [사실][^ref-991][^ref-980][^ref-1238][^ref-1227][^ref-1212][^ref-1228][^ref-1233][^ref-1235][^ref-1234][^ref-1237][^ref-1236][^ref-1229][^ref-1230][^ref-1231]


### 2026-10-12 보강

이번 실행에서 1차 원문으로 확인한 규범을 아래 표에 더한다. 주제 페이지 표에 같은 이름의 행이 있으면 이 표의 근거와 날짜 표현을 함께 읽는다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| EU AI Act (Regulation (EU) 2024/1689)와 디지털 옴니버스 (EU) 2026/1744 | 프레임워크 | 2026/1744는 2026-07-08 채택, 2026-07-24 관보 게재 뒤 2026-07-27 발효했다. [사실][^ref-1517] 고위험 AI 요구(제III장 제1~3절)는 부속서 III 고위험에 2027-12-02부터(제6조5항 제외), 제6조1항·부속서 I 고위험에 2028-08-02부터 적용되고, 제102~110조는 2026-07-27부터 적용된다. [사실][^ref-1517] 이 세 날짜는 [43. 데이터·관측성·배포의 다른 연구영역과의 연결 주제 페이지](2026-10-09-area43-s10.md)에 이미 있는 내용이며, 여기서는 근거를 관보 원문으로 올린 것이다. 2026/1744는 기계규정 (EU) 2023/1230을 부속서 I Section A에서 Section B로 옮겼고, 바뀐 제2조2항은 Section B 대상 제품과 관련해 고위험이 되는 AI에 제6조1항·제60a조·제102~112조만 적용한다(제57~59조는 그 법령에 고위험 AI 요구가 통합된 범위에서만). [사실][^ref-1517] 이 구조로 보면 기계류 로봇의 고위험 AI 요구는 2028-08-02에 AI Act에서 직접 적용되는 것이 아니라 기계규정 부속서 III을 거쳐 반영되는 것으로 보인다. [추정][^ref-1517] 반면 기존 위키 서술(같은 주제 페이지, [M. 안전](../../categories/safety/index.md)·[L. AI·학습 기술](../../categories/ai-and-learning/index.md) 대분류 페이지)은 '기계류 등 부속서 I 제품에 내장되면 2028-08-02'로 적고 2차 해설도 엇갈리므로, 두 서술을 함께 두고 oq-106에서 다룬다. | [^ref-1517] |
| EU 기계류 규정 (EU) 2023/1230 — AI 위임법령 경로 | 프레임워크 | 2026/1744 제3조는 기계규정 제8조에 위임 권한을 더해, 위원회가 위임법령으로 부속서 III에 고위험 AI의 보건·안전 요구(AI Act 제III장 제2절과 제17·19·72·73조를 반영)를 추가하게 했다. [사실][^ref-1517] 그 위임법령은 조문 문언대로 2028-08-02까지 적용(shall apply by)되도록 정해졌고, 위임 권한은 2026-07-27부터 5년이다. [사실][^ref-1517] 새 제20조10항은 기계규정상 AI 조화 표준·공통 사양이 나오기 전까지 AI Act 제40·41조의 조화 표준·공통 사양을 준수한 고위험 AI를 부속서 III의 AI 관련 요구에 적합한 것으로 추정한다([적합성 추정](../../glossary/presumption-of-conformity.md)). [사실][^ref-1517] 위임법령의 번호와 채택 여부는 확인되지 않았다(새 열린 질문). | [^ref-1517] |
| EU 개정 제조물책임지침 (Directive (EU) 2024/2853) — 근거 교체 | 프레임워크 | 원판 제2조1항은 적용 대상을 'after 9 December 2026'에 출시·사용 개시된 제품으로 적었으나, 2026-05-07 정오표(OJ L 2026/90364)가 이를 'after 8 December 2026'으로 고쳤다. [사실][^ref-1529][^ref-1530] 따라서 적용 시점은 2026-12-08 후(정오표 2026-05-07, OJ L 2026/90364 기준), 곧 2026-12-09에 출시·사용 개시된 제품부터다. [사실][^ref-1529][^ref-1530] 제2조2항은 상업 활동 밖의 FOSS를 적용에서 빼고, 제4조1항은 소프트웨어·디지털 제조 파일을 제품에 포함한다. [사실][^ref-1529] 주제 페이지 표의 같은 행은 날짜(2026-12-09 이후)는 이와 같지만 근거가 정오표 전 해설이므로, 근거는 관보 원문과 정오표로 읽는다. [추정][^ref-1227][^ref-1529][^ref-1530] | [^ref-1529][^ref-1530] |
| 인공지능 기본법 — 제33·35조 | 프레임워크 | 제33조(고영향 해당 여부 사전 검토 의무, 장관 확인 요청은 재량)와 제35조(영향평가 노력의무)를 조문 근거로 더했다(4절). 열람한 판은 법률 제21311호다. [사실][^ref-1518] 두 조의 시행 시점은 4절의 단서와 함께 추정으로 둔다. | [^ref-1518] |
| EU 사이버복원력법 (Regulation (EU) 2024/2847) — 기산점·오픈소스 | 프레임워크 | 기존 기한(24시간·72시간·14일·1개월)은 유지하고, 기산점(인지 시점, 시정 조치 이용 가능 시점, 사고 통지 제출 시점)을 6절에 더했다. [사실][^ref-1522] 오픈소스 스튜어드 보고 의무는 제24조3항·제71조2항에 따라 2027-12-11부터 적용된다(4절). [사실][^ref-1522][^ref-1523] CRA의 오픈소스 적용 범위는 조문이 아니라 전문 (18)에 근거하는데, 전문 (18)은 상업 활동 과정에서 공급되는 자유·오픈소스 소프트웨어만 적용 대상으로 보고, 자기 책임 아래 있지 않은 제품에 소스 코드를 기여하는 자에게는 적용되지 않는다고 적는다. [사실][^ref-1522] | [^ref-1522][^ref-1523] |
| 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (산업통상부고시 제2025-21호) | 평가 프로그램 | 심사항목 16개→8개 통·폐합을 담은 개정 고시로 2025-11-24 발령·시행됐다(행정예고안은 공고 제2025-042호). [사실][^ref-1519][^ref-1469] 제8조1항2호의 관제장치 일부 변경 시 심사 면제 조항은 리서치 단계 원문 열람 기준으로만 확인됐다(4절). [추정][^ref-1469] | [^ref-1519][^ref-1469] |
| 지능형 로봇 개발 및 보급 촉진법 시행규칙 제7조의10 (책임보험 등의 가입금액) | 프레임워크 | 실외이동로봇 사고배상 책임보험·공제의 법령 기준 금액을 정한다(5절). [사실][^ref-1520] 같은 시행규칙의 제7조의4·5는 [ref-1470](../../references/ref-1470.md)으로 따로 인용된다. | [^ref-1520] |
| Apache License 2.0 | 오픈소스 | 재배포 때 라이선스 사본 제공, 수정 파일 고지, NOTICE 귀속 고지를 요구한다(6절). [사실][^ref-1524] | [^ref-1524] |
| REUSE 명세 3.3 | 프레임워크 | 주석을 넣을 수 없는 파일의 권리 정보를 .license 인접 파일 또는 REUSE.toml로 표기한다(6절). [사실][^ref-1525] | [^ref-1525] |
| SPDX 라이선스 표현식 (명세 2.2.2 부록 D)과 reuse lint | 표준 / 오픈소스 | OR(선택)·AND(동시 준수) 연산자로 라이선스 조합을 표현하고, reuse lint는 유효하지 않은 표현식을 검사하는 항목을 두었다고 기록한다(프로젝트 자체 변경기록 기준, 6절). [사실][^ref-1527][^ref-1526] 주제 페이지 표의 SPDX 개요 행을 보강한다. | [^ref-1527][^ref-1526] |
| NVIDIA GR00T-N1.6-3B 가중치 라이선스 | 오픈소스(가중치 공개, 비상업 라이선스) | 가중치를 연구·평가 목적의 비상업 용도로만 쓰게 한다(6절). [추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)[^ref-1528] | [^ref-1528] |

[표준 목록](../../standards/index.md)에도 새 항목을 더한다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1212]: European Agency for Safety and Health at Work (EU-OSHA), Regulation 2023/1230/EU - machinery, 미확인, https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery, 접근일 2026-09-30 (원문 미열람)
[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1229]: ROS (ros-infrastructure/rep), REP 2004 -- Package Quality Categories, 2019-12-17, https://ros.org/reps/rep-2004.html, 접근일 2026-09-30
[^ref-1230]: SPDX Project (Linux Foundation), SPDX Overview, 미확인, https://spdx.dev/about/overview/, 접근일 2026-09-30
[^ref-1231]: Open Robotics (Gazebo Classic), Gazebo : Tutorial : Model structure and requirements, 미확인, https://classic.gazebosim.org/tutorials?tut=model_structure, 접근일 2026-09-30
[^ref-1233]: 김·장 법률사무소, 인공지능, 소프트웨어 결함으로 인한 제조물책임의 주요 쟁점 및 시사점, 2024-07-05, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930, 접근일 2026-09-30
[^ref-1234]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1235]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1236]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1237]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1238]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-12
[^ref-1517]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI), 2026-07-24, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744, 접근일 2026-10-12
[^ref-1518]: 법제처 국가법령정보센터 (과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 [시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정] 제33조·제34조·제35조, 2026-01-20, https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810895, 접근일 2026-10-12
[^ref-1519]: 산업통상부 기계로봇제조정책과, 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정(안) 행정예고 (산업통상부 공고 제2025-042호), 2025-11-06, https://www.motir.go.kr/kor/article/ATCLa6723dc7b/458/view, 접근일 2026-10-12
[^ref-1520]: 법제처 국가법령정보센터 (산업통상부), 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의10(책임보험 등의 가입금액), 2025-10-01, https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=278777, 접근일 2026-10-12
[^ref-1522]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act), 2024-11-20, https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng, 접근일 2026-10-12
[^ref-1523]: European Union Agency for Cybersecurity (ENISA), The CRA Single Reporting Platform is launched, 2026-09-11, https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched, 접근일 2026-10-12
[^ref-1524]: Apache Software Foundation, Apache License, Version 2.0, 2004-01, https://www.apache.org/licenses/LICENSE-2.0.html, 접근일 2026-10-12
[^ref-1525]: Free Software Foundation Europe (REUSE), REUSE Specification – Version 3.3, 2024-11-14, https://reuse.software/spec-3.3/, 접근일 2026-10-12
[^ref-1526]: FSFE reuse-tool 기여자 (GitHub), reuse-tool CHANGELOG.md (v6.1.0 태그), 2025-10-07, https://github.com/fsfe/reuse-tool/blob/v6.1.0/CHANGELOG.md, 접근일 2026-10-12
[^ref-1527]: SPDX Project (Linux Foundation), Annex D: SPDX License Expressions - specification v2.2.2, 미확인, https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/, 접근일 2026-10-12
[^ref-1528]: NVIDIA (Hugging Face 모델 저장소), GR00T-N1.6-3B / LICENSE (NVIDIA License), 2025-12-15, https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/LICENSE, 접근일 2026-10-12
[^ref-1529]: European Parliament and Council of the European Union (Official Journal of the European Union), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853, 접근일 2026-10-12
[^ref-1530]: European Parliament and Council of the European Union (Official Journal of the European Union), Corrigendum to Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2026-05-07, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202690364, 접근일 2026-10-12
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s11.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 열린 질문"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1469, ref-1520]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#11
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 열린 질문

# 59. 법·규제·보험·라이선스 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 기존 열린 질문 12건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 기존 열린 질문 12건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.


### 2026-10-12 갱신

2026-09-30 실행에서 올린 새 질문 5건의 id는 oq-288·oq-289·oq-290·oq-291·oq-292다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

**해결**

- **oq-288** (상태: 해결 · 실행 2026-10-12-02) 한국 실외이동로봇 책임보험·공제의 가입금액은 지능형로봇법 시행규칙 제7조의10이 정하며, 금액은 5절에 있다. [사실][^ref-1520]

**부분 근거만 확인, 열림 유지**

- **oq-143** (상태: 열림) AI Act 고위험 적용일과 Section B 제품의 적용 조항, 인공지능 기본법 제33·35조의 의무 강도를 확인했다(4·7절). 로봇 대화 기능의 분류와 대화 기록 로그 항목·보존 기간은 답하지 못했다.
- **oq-186** (상태: 열림) 16개→8개 개정의 근거(행정예고 공고 제2025-042호, 고시 제2025-21호, 2025-11-24 시행)를 확인했다(5절). 알림음·등화장치가 어디로 옮겨졌는지는 확인되지 않았다.
- **oq-187** (상태: 열림) 고시 제8조1항2호의 관제장치 일부 변경 시 심사 면제 조항은 리서치 단계 원문 열람 기준으로만 확인됐다. [추정][^ref-1469] 오케스트레이션 계층이 인증상 관제장치에 해당하는지에 대한 해석은 없다.
- **oq-289** (상태: 열림) 개정 제조물책임지침의 적용 시점과 비상업 FOSS 제외를 확인했으나(3·7절), 오케스트레이션 소프트웨어를 어떻게 다루는지에 대한 판정 자료는 없다.
- **oq-291** (상태: 열림) CRA 보고 기한의 기산점과 오픈소스 스튜어드의 적용 범위·시점을 확인했으나(4·6·7절), 오케스트레이션 플랫폼 사업자의 제조자 해당성은 답하지 못했다.
- **oq-292** (상태: 열림) REUSE 3.3의 .license 인접 파일·REUSE.toml 방법과 SPDX 표현식 검사를 확인했으나(6절), 3D 로봇 자산의 라이선스를 SPDX로 기술한 사례는 찾지 못했다.

**다른 영역 질문과의 연결**

- oq-106: 기계류 로봇 AI의 적용 경로가 (EU) 2026/1744로 바뀌었고(7절), 이 위키의 기존 서술과 엇갈린다.
- oq-316·oq-338: 바뀐 AI Act 제2조2항의 적용 조항 한정(7절)이 근거가 된다.
- oq-313: 시행규칙 제7조의10이 지능형로봇법 제40조의4에 근거한다는 점만 확인했다. [사실][^ref-1520]

**이번에 답하지 못한 질문**: oq-173, oq-231, oq-239, oq-249, oq-250, oq-262, oq-275, oq-279, oq-282, oq-290.

**새 질문**(id는 게시 때 부여)

- (EU) 2026/1744로 기계규정 제8조에 근거가 생긴, 고위험 AI의 보건·안전 요구를 기계규정 부속서 III에 추가하는 위원회 위임법령은 채택됐는가? 채택됐다면 번호와 반영한 AI Act 요구(제III장 제2절, 제17·19·72·73조)의 범위는 무엇이며, 여러 로봇을 지시하는 오케스트레이션 소프트웨어의 AI도 그 대상에 드는가? (관련: 59. 법·규제·보험·라이선스, 48. 안전·위험 관리)
- 국내 실외이동로봇 책임보험·공제의 실제 보험사 약관은 시행규칙 제7조의10 기준 금액 외에 관제 장애·통신 단절·사이버 사고로 생긴 손해와 제조사·관제 사업자에 대한 구상을 어떻게 다루는가? (관련: 59. 법·규제·보험·라이선스, 66. 실외)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-12
[^ref-1520]: 법제처 국가법령정보센터 (산업통상부), 지능형 로봇 개발 및 보급 촉진법 시행규칙(산업통상부령 제1호, 2025-10-01 시행) 제7조의10(책임보험 등의 가입금액), 2025-10-01, https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=278777, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s4.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 핵심 개념과 용어"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1227, ref-1228, ref-1235, ref-1236, ref-1469, ref-1518, ref-1522, ref-1523, ref-1529, ref-980]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#4
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 핵심 개념과 용어

# 59. 법·규제·보험·라이선스 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다.
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 운행 조건을 정하는 인증·보험, 사고 뒤 책임을 정하는 제조물책임·실질적 변경, 운영 중 의무를 정하는 AI·보안 규제, 배포물의 권리를 정하는 라이선스 선언으로 나눠 볼 수 있다. (구축자 의견) [의견][^ref-980][^ref-1227][^ref-1228][^ref-1236]


### 2026-10-12 보강

- **고영향 인공지능(High-impact AI)** — 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」(법령 약칭 인공지능기본법, 이하 인공지능 기본법) 제33조1항은 인공지능사업자가 AI나 이를 이용한 제품·서비스를 제공할 때 그 AI가 [고영향 인공지능](../../glossary/high-impact-ai.md)에 해당하는지 사전에 검토하도록 한다. [사실][^ref-1518] 같은 항은 필요하면 과학기술정보통신부장관에게 해당 여부 확인을 요청할 수 있게 하고(재량), 제2항은 요청이 있으면 장관이 해당 여부를 확인하도록 한다. [사실][^ref-1518] 제35조1항은 고영향 AI 제품·서비스를 제공하는 사업자가 사전에 사람의 기본권에 미치는 영향을 평가하도록 노력하게 하는 노력의무이고, 제2항은 국가기관등이 영향평가를 실시한 제품·서비스를 우선 고려하게 한다. [사실][^ref-1518]
- **인공지능 기본법 조문 판 표기** — 이번에 열람한 판은 법률 제21311호(2026-01-20 일부개정, 2026-07-21 시행)이며, 이 판의 제33조에는 개정 표시가 없다. [사실][^ref-1518] 두 조의 의무는 법 최초 시행(2026-01-22)부터 있었고 2026-07-21은 두 조의 발효일이 아닌 것으로 보인다. [추정][^ref-1518][^ref-1235] 다만 제35조1항에는 ‘개정 2026. 1. 20.’ 표시가 있어 바뀐 문장의 시행일이 2026-07-21일 수 있으며, 원판([ref-620](../../references/ref-620.md))과 신구 대비표는 확인하지 못했다. [추정][^ref-1518]
- **[제조물책임](../../glossary/product-liability.md)(Product Liability, EU 정의)** — 개정 제조물책임지침 제4조1항은 '제품'을 다른 동산·부동산에 통합되거나 연결된 경우를 포함한 모든 동산으로 정의하고, 전기·디지털 제조 파일·원재료·소프트웨어를 포함한다. [사실][^ref-1529] 제2조2항은 상업 활동 밖에서 개발·공급되는 FOSS에는 지침을 적용하지 않는다. [사실][^ref-1529]
- **오픈소스 소프트웨어 스튜어드(Open-source Software Steward)** — [사이버복원력법](../../glossary/cyber-resilience-act.md)(Cyber Resilience Act, CRA) 제24조3항은 스튜어드에게 제14조1항 보고 의무를 그 제품 개발에 관여하는 범위에서 적용한다. [사실][^ref-1522] 제71조2항에 따라 제24조는 일반 적용일인 2027-12-11부터 적용되고(제14조만 2026-09-11부터), 유럽연합 사이버보안청(European Union Agency for Cybersecurity, ENISA)의 단일 보고 플랫폼 가동 발표(2026-09-11)도 스튜어드 보고 의무의 적용일을 2027-12-11로 구분한다. [사실][^ref-1522][^ref-1523]
- **운행안전인증의 관제장치 변경** — [실외이동로봇 운행안전인증](../../glossary/outdoor-mobile-robot-operational-safety-certification.md)의 현행 근거 고시는 산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)이며, 이 페이지에서는 이후 제2025-21호로 적는다. [사실][^ref-1469] 이 고시 제8조1항2호는 인증받은 실외이동로봇 또는 해당 관제장치의 일부를 변경해 신규 인증이나 변경인증을 받으려는 경우 인증기관장이 심사의 일부 또는 전부를 면제할 수 있게 한 것으로 보인다(리서치 단계 원문 열람 기준, 검증 단계 미확인). [추정][^ref-1469] 오케스트레이션 계층이 인증상 관제장치인지에 대한 해석은 확인되지 않았다(oq-187).

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1235]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1236]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1469]: 산업통상부 (국가법령정보센터 행정규칙), 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 및 별표 3 실외이동로봇 운행안전인증 기준, 2025-11-24, https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000269426, 접근일 2026-10-12
[^ref-1518]: 법제처 국가법령정보센터 (과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 [시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정] 제33조·제34조·제35조, 2026-01-20, https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810895, 접근일 2026-10-12
[^ref-1522]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act), 2024-11-20, https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng, 접근일 2026-10-12
[^ref-1523]: European Union Agency for Cybersecurity (ENISA), The CRA Single Reporting Platform is launched, 2026-09-11, https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched, 접근일 2026-10-12
[^ref-1529]: European Parliament and Council of the European Union (Official Journal of the European Union), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853, 접근일 2026-10-12
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s6.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 대표 접근법과 기술"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1227, ref-1228, ref-1236, ref-1522, ref-1524, ref-1525, ref-1526, ref-1527, ref-1528, ref-1529, ref-1530, ref-980]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#6
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 대표 접근법과 기술

# 59. 법·규제·보험·라이선스 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1228][^ref-1236]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

확인한 자료로 보면 이 영역의 대응 수단은 인증·보험 조건을 운영 제약으로 반영하는 것, 사고·취약점 보고와 증거 기록을 갖추는 것, 라이선스를 선언하고 자동으로 검사하는 것의 세 갈래로 보인다. [추정][^ref-980][^ref-1228][^ref-1236]


### 2026-10-12 보강: 보고 기한의 기산점

CRA 보고 기한은 기한마다 세기 시작하는 시점이 달라, 기한 길이와 함께 기산점을 기록해야 계산할 수 있다. 주제 페이지의 24시간·72시간·14일·1개월 기한 서술은 그대로 두고 기산점만 보탠다. CRA 제14조2항 (a)(b)는 [적극 악용 취약점](../../glossary/actively-exploited-vulnerability.md)의 조기 경보(24시간)와 취약점 통지(72시간)를 제조자가 그 취약점을 인지한 때부터 센다. [사실][^ref-1522] 같은 항 (c)는 최종 보고 기한을 최초 인지가 아니라 시정·완화 조치가 이용 가능해진 뒤 14일 이내로 정한다(관련 정보가 이미 제공된 경우 제외). [사실][^ref-1522] 제14조4항 (c)는 중대한 보안 사고의 최종 보고를 사고 통지 제출 뒤 1개월 이내로 정해, 취약점 최종 보고와 기산점이 다르다. [사실][^ref-1522]

주제 페이지의 제조물책임 증거 공개·결함 추정·보안 업데이트 서술은 법률사무소 해설 기준이며 이번에 원문과 대조하지 않았고, 적용 시점만 관보 원문·정오표 기준(3절·7절)으로 읽는다. [추정][^ref-1227][^ref-1529][^ref-1530]

### 2026-10-12 보강: 라이선스 재배포 의무와 자동 검사

Apache License 2.0 제4절은 저작물이나 파생저작물을 재배포할 때 (a) 수령자에게 라이선스 사본을 주고, (b) 수정한 파일에 변경 사실을 눈에 띄게 표시하며, (d) 원 저작물에 NOTICE 파일이 있으면 관련 귀속 고지의 읽을 수 있는 사본을 NOTICE 파일·소스·문서·통상 표시 화면 가운데 한 곳에 넣도록 요구한다. [사실][^ref-1524]

REUSE 명세 3.3(2024-11-14)은 주석을 넣을 수 없는 파일의 라이선스 정보를 같은 이름에 .license 확장자를 붙인 인접 텍스트 파일에 두도록 규정하고, REUSE.toml로 정보를 모아 두는 방법도 정한다. [사실][^ref-1525] 이 방법을 실제 로봇 3D 자산에 적용한 사례는 확인하지 못했다(oq-292).

SPDX 명세 2.2.2 부록 D는 라이선스 표현식의 문법으로, 둘 이상의 라이선스 중 하나를 고를 수 있는 경우를 OR 연산자로, 동시에 준수해야 하는 경우를 AND 연산자로 표현하게 한다(호환성의 법률 판정 규칙은 아니다). [사실][^ref-1527] reuse-tool은 프로젝트 자체 변경기록(CHANGELOG v6.1.0 태그) 기준으로 v6.0.0(2025-10-06)에서 reuse lint에 SPDX 문법상 유효하지 않은 라이선스 표현식을 잡는 검사 항목을 추가했다고 기록한다(실행 재현 안 함). [사실][^ref-1526]

[로봇 기반 모델](../../glossary/robot-foundation-model.md) 가중치에는 코드와 별개의 라이선스 문서가 붙는 예가 있다. NVIDIA GR00T-N1.6-3B 모델 저장소의 LICENSE 제3.3절은 저작물과 파생물을 비상업적(연구·평가 목적) 용도로만 쓰게 하고, NVIDIA와 계열사는 상업적으로 쓸 수 있다고 정한다. [추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)[^ref-1528] 다른 모델판·코드 저장소·별도 계약의 조건은 미확인이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1236]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1522]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act), 2024-11-20, https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng, 접근일 2026-10-12
[^ref-1524]: Apache Software Foundation, Apache License, Version 2.0, 2004-01, https://www.apache.org/licenses/LICENSE-2.0.html, 접근일 2026-10-12
[^ref-1525]: Free Software Foundation Europe (REUSE), REUSE Specification – Version 3.3, 2024-11-14, https://reuse.software/spec-3.3/, 접근일 2026-10-12
[^ref-1526]: FSFE reuse-tool 기여자 (GitHub), reuse-tool CHANGELOG.md (v6.1.0 태그), 2025-10-07, https://github.com/fsfe/reuse-tool/blob/v6.1.0/CHANGELOG.md, 접근일 2026-10-12
[^ref-1527]: SPDX Project (Linux Foundation), Annex D: SPDX License Expressions - specification v2.2.2, 미확인, https://spdx.github.io/spdx-spec/v2.2.2/SPDX-license-expressions/, 접근일 2026-10-12
[^ref-1528]: NVIDIA (Hugging Face 모델 저장소), GR00T-N1.6-3B / LICENSE (NVIDIA License), 2025-12-15, https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/LICENSE, 접근일 2026-10-12
[^ref-1529]: European Parliament and Council of the European Union (Official Journal of the European Union), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853, 접근일 2026-10-12
[^ref-1530]: European Parliament and Council of the European Union (Official Journal of the European Union), Corrigendum to Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2026-05-07, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202690364, 접근일 2026-10-12
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s3.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 왜 중요한가"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1227, ref-1228, ref-1234, ref-1235, ref-1236, ref-1237, ref-1238, ref-1529, ref-1530, ref-980, ref-991]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#3
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 왜 중요한가

# 59. 법·규제·보험·라이선스 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1238][^ref-1237][^ref-1235][^ref-1228][^ref-1234][^ref-1227][^ref-1236]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇을 운영할 때 지켜야 할 법·규제·보험·라이선스는 현장마다 달라 보이며, 이번 조사 범위에서는 실외의 운행 규정·운행안전인증·운용자 의무·의무 보험, 산업 사업장의 기계 안전 규제, 모든 현장에 걸치는 AI·사이버보안·개인정보 규제와 사고 책임 법제, 오픈소스·3D 자산 라이선스가 겹치는 구조로 보인다. [추정][^ref-991][^ref-980][^ref-1238][^ref-1237][^ref-1235][^ref-1228][^ref-1234][^ref-1227][^ref-1236]


### 2026-10-12 보강: 개정 제조물책임지침의 적용 시점 근거

EU 개정 제조물책임지침 (EU) 2024/2853은 2026-12-08 후(정오표 2026-05-07, OJ L 2026/90364 기준), 곧 2026-12-09에 출시·사용 개시된 제품부터 적용된다. [사실][^ref-1529][^ref-1530] 이 지침은 소프트웨어를 제품에 포함하고, 상업 활동 밖에서 개발·공급되는 자유·오픈소스 소프트웨어(Free and Open-Source Software, FOSS)는 적용에서 뺀다. [사실][^ref-1529] 주제 페이지 둘째 문단의 '2026-12-09 이후 출시·사용 개시 제품'이라는 날짜는 정오표 기준의 뜻과 같아 그대로 두지만, 근거였던 법률사무소 해설은 정오표 전에 나온 자료이므로 적용 시점·소프트웨어 포함·FOSS 제외의 근거는 관보 원문과 정오표로 읽는다. [추정][^ref-1227][^ref-1529][^ref-1530]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1234]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1235]: 대한민국 정책브리핑 (과학기술정보통신부), '인공지능기본법' 22일 시행…생성형 AI 결과물 '워터마크' 표시 의무, 2026-01-21, https://www.korea.kr/news/policyNewsView.do?newsId=148958380, 접근일 2026-09-30
[^ref-1236]: Open Robotics (ROS 2 Documentation), ROS 2 developer guide, 미확인, https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html, 접근일 2026-09-30
[^ref-1237]: 고용노동부, 산업용 로봇과 컨베이어도 안전검사 필수, 2017-10-26, https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135, 접근일 2026-09-30
[^ref-1238]: Commonwealth of Virginia (Code of Virginia), § 46.2-908.1:1. Personal delivery devices, 미확인, https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/, 접근일 2026-09-30
[^ref-1529]: European Parliament and Council of the European Union (Official Journal of the European Union), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853, 접근일 2026-10-12
[^ref-1530]: European Parliament and Council of the European Union (Official Journal of the European Union), Corrigendum to Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2026-05-07, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202690364, 접근일 2026-10-12
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30
[^ref-991]: 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 로봇 허용, 2023-11-16, https://www.korea.kr/news/policyNewsView.do?newsId=148922726, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s8.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 대표 연구와 자료"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1227, ref-1517, ref-1522, ref-1529, ref-1530, ref-1531]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#8
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 대표 연구와 자료

# 59. 법·규제·보험·라이선스 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 모은 자료는 학술 논문보다 정부·집행기관의 1차 자료와 법률사무소 해설이 중심이다.


### 2026-10-12 보강

- 김정욱·성현지·유성희, 한·싱가포르 규제샌드박스 비교를 통한 AI 샌드박스 효율화 방안 제언(2025, 규제연구 34권 1호) — 싱가포르 IMDA(Infocomm Media Development Authority)가 시행한 AI 샌드박스 2건이 모두 기술 개발·혁신 지원에 가까운 형태이며, 한국과 달리 규제 특례 부여를 목적으로 하지 않는다고 구분한다. [사실][^ref-1531] 제도 비교 연구이며 로봇 실증 연구가 아니다.
- 관보 원문 자료: AI Act 디지털 옴니버스 (EU) 2026/1744, 사이버복원력법 (EU) 2024/2847, 개정 제조물책임지침 (EU) 2024/2853과 그 정오표(2026-05-07)를 1차 근거로 더했다(7절). [사실][^ref-1517][^ref-1522][^ref-1529][^ref-1530]
- 주제 페이지의 Gibson Dunn 해설(2026-03-23) 항목은 적용 시점·FOSS 제외·제품 정의를 관보 원문과 정오표로 대체하고, 증거 공개·결함 추정 같은 나머지 서술은 해설 기준으로 둔다. [추정][^ref-1227][^ref-1529][^ref-1530]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1517]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI), 2026-07-24, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744, 접근일 2026-10-12
[^ref-1522]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act), 2024-11-20, https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng, 접근일 2026-10-12
[^ref-1529]: European Parliament and Council of the European Union (Official Journal of the European Union), Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2024-11-18, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024L2853, 접근일 2026-10-12
[^ref-1530]: European Parliament and Council of the European Union (Official Journal of the European Union), Corrigendum to Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC, 2026-05-07, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202690364, 접근일 2026-10-12
[^ref-1531]: 김정욱·성현지·유성희, 한·싱가포르 규제샌드박스 비교를 통한 AI 샌드박스 효율화 방안 제언, 2025-06, https://journal.kci.go.kr/ksrs2002/archive/articlePdf?artiId=ART003225249, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-12-02/pages/topics/2026/2026-10-12-area59-s10.md

```markdown
---
title: "59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 59
related_areas: [3, 4, 13, 16, 36, 44, 47, 48, 50, 52, 53, 57, 58, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1227, ref-1228, ref-1234, ref-1517, ref-1528, ref-980]
last_run: 2026-10-12
version: 1
split_from: docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md#10
---

[홈](../../index.md) › [주제](../index.md) › 59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결

# 59. 법·규제·보험·라이선스 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1234][^ref-1228][^ref-1227]
- 이 페이지는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 안전 인증, 개인정보·보안, 수명주기, 다사업자 책임, 실외 현장 영역과 두루 이어지는 것으로 보인다. [추정][^ref-980][^ref-1234][^ref-1228][^ref-1227]


### 2026-10-12 보강

- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — (EU) 2026/1744로 기계규정 대상 로봇의 고위험 AI 보건·안전 요구가 기계규정 제8조 위임법령(부속서 III)을 거쳐 반영되는 경로가 생겨, 기계 안전 요구와 AI 규제 적용 경로가 만난다. [사실][^ref-1517]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 모델 가중치의 라이선스를 코드와 분리해 등록하자는 구축자 의견(9절)이 두 영역을 잇는다. [의견][^ref-1528] GR00T-N1.6-3B 가중치는 비상업(연구·평가) 사용으로 제한된다. [추정] 벤더 주장(NVIDIA 라이선스 문면, 커밋 d0814e7 기준)[^ref-1528]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1227]: Gibson Dunn, EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains, 2026-03-23, https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/, 접근일 2026-09-30
[^ref-1228]: European Commission (Shaping Europe's digital future), Cyber Resilience Act - Reporting obligations, 2026-09-11, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-09-30
[^ref-1234]: 법제처 찾기쉬운 생활법령정보, 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인), 미확인, https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3, 접근일 2026-09-30
[^ref-1517]: European Parliament and Council of the European Union (Official Journal of the European Union), Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI), 2026-07-24, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32026R1744, 접근일 2026-10-12
[^ref-1528]: NVIDIA (Hugging Face 모델 저장소), GR00T-N1.6-3B / LICENSE (NVIDIA License), 2025-12-15, https://huggingface.co/nvidia/GR00T-N1.6-3B/blob/d0814e7ecb19202e7c8468b46098b0b7ef3a6d61/LICENSE, 접근일 2026-10-12
[^ref-980]: 한국로봇산업진흥원, 실외이동로봇 운행안전인증, 미확인, https://www.kiria.org/portal/cert/portalCertEstiSafe.do, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-02 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-02 | 59. 법·규제·보험·라이선스 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-12-02/verification2.json

```json
{
  "run_id": "2026-10-12-02",
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
    "overlaps": []
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "세부영역 페이지 5절은 '고시 제2025-21호'가 이 페이지에서 처음 나오는데 '산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)' 병기가 없다. 병기는 분리된 2026-10-12-area59-s4 에만 있다",
      "세부영역 페이지 9절에 'CRA'가 이 페이지에서 처음 나오는데 풀어 쓰지 않았다(사이버복원력법(Cyber Resilience Act, CRA))"
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "11절(세부영역 페이지 11절 첫 문단, docs/topics/2026/2026-10-12-area59-s11.md 의 세 줄 요약 첫 줄과 3절 첫 문단): '기존 열린 질문 12건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다'는 2026-09-30 실행 기준 문장이다. 이번 실행의 oq-288 해결과 새 질문 2건 등록과 맞지 않는다. 11절 패치를 replace 로 보내 첫 문단을 이번 실행 기준(2026-09-30에 올린 질문 5건의 id 는 oq-288~oq-292, oq-288 해결, oq-143·oq-186·oq-187·oq-289·oq-291·oq-292 는 부분 근거만 있어 열림 유지, 새 질문 2건 등록)으로 고친다. 2026-09-30 질문 목록 페이지(docs/topics/2026/2026-09-30-area59-s11.md) 링크는 남긴다. 같은 페이지 안에서 상태가 서로 모순된다.",
    "4절 요약 문장(세부영역 페이지 4절, 2026-10-12-area59-s4 의 세 줄 요약 첫 줄): '이 영역의 용어는 … 나눠 볼 수 있다.' 뒤에 기존 페이지에 있던 '(구축자 의견) [의견][^ref-980][^ref-1227][^ref-1228][^ref-1236]'을 되살린다. 갱신 중에 기존의 검증된 문장에서 태그와 각주가 빠졌다.",
    "3·4·6·7·8·10·11절 보강 블록: 재분리 과정에서 세부영역 페이지가 가리키던 2026-09-30 주제 페이지(2026-09-30-area59-s3·s4·s6·s7·s8·s10·s11)로 가는 링크가 사라졌다. 그래서 '주제 페이지 둘째 문단'(s3), '주제 페이지 표에 같은 이름의 행'·'주제 페이지 표의 같은 행'·'SPDX 개요 행'(s7), '주제 페이지의 24시간·72시간·14일·1개월 기한 서술'·'주제 페이지의 제조물책임 증거 공개 … 서술'(s6), '주제 페이지의 Gibson Dunn 해설 항목'(s8)이 무엇을 가리키는지 알 수 없다. 각 블록에서 '주제 페이지'를 해당 2026-09-30-area59-sN.md 링크로 밝힌다. 각 절에는 '이전 상세 내용: [59. 법·규제·보험·라이선스 — <절 이름> (2026-09-30)](…)' 링크 한 줄을 남긴다. 이전 실행에서 검증된 상세 내용에 위키 안에서 다시 닿을 수 있어야 한다.",
    "5절 둘째 문단: 태그 없는 문장 '심사항목을 줄인 근거는 산업통상부 공고 제2025-042호(2025-11-06)의 행정예고다.'는 바로 뒤의 '최종 근거는 … 고시 제2025-21호다'와 충돌한다. 이 문장을 지우거나, '심사항목 축소는 산업통상부 공고 제2025-042호(2025-11-06) 행정예고로 예고됐다.'처럼 고치고 [사실][^ref-1519]를 붙인다. 이것은 f16 의 처분(행정예고안 기준, 최종 근거는 고시)에 맞추는 것이다.",
    "5절: 이 페이지에서 처음 나오는 '고시 제2025-21호'를 '산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)'로 한 번 병기한다. '지능형로봇법 시행규칙'도 처음 나올 때 정식 명칭 '지능형 로봇 개발 및 보급 촉진법 시행규칙'을 함께 쓴다. 1차 용어 지시는 페이지마다 첫 등장에 적용된다.",
    "7절(2026-10-12-area59-s7) NVIDIA GR00T-N1.6-3B 행: 유형 칸의 '오픈소스(가중치 공개, 비상업 라이선스)'를 '벤더 라이선스(모델 가중치)'처럼 고친다. 브리프(f41)는 이 라이선스를 오픈소스로 규정하지 않는다. 또 비상업 제한 라이선스를 오픈소스로 부르는 것은 브리프 밖 성격 규정이다.",
    "9절 보강 소절: 이 페이지에서 처음 나오는 'CRA'를 '사이버복원력법(Cyber Resilience Act, CRA)'으로 풀어 쓴다. 약어는 첫 등장 때 풀어 쓴다는 문체 규칙에 따른 것이다.",
    "ref-1238 각주(세부영역 페이지 13절, 2026-10-12-area59-s3·s7 출처 절): 이번 실행에서 다시 열었고 reference_updates 의 접근일이 2026-10-12 이므로 각주 정의의 접근일도 2026-10-12 로 맞춘다. ref-1469 는 이미 맞춰져 있다. 각주와 참고문헌 갱신 값이 어긋나면 안 된다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 46건, 미확인 2건, 교차 확인 4건(f1~f4: AI 옴니버스 발효일·적용일·기계류 Section B 이동을 ERTICO·Hunton·Cooley·IBF 해설로 독립 확인). 강등: f14 사실 → 추정(제35조① 개정 표시가 있어 원법부터의 의무라고 단정할 수 없음), f17 사실 → 추정(고시 제8조①2호 원문 미확인). 원문 미열람 출처: ref-1227, ref-1235(리서치에서 다시 열지 않음). 검증 단계에서도 열지 못한 출처는 ref-1517·ref-1522·ref-1529·ref-1530·ref-1519·ref-1469·ref-1520·ref-1531이며, 검색 결과·2차 해설·이전 검증 실행과 일치하는지로 확인했다. 주의: 모든 사실 주장이 단일 1차 원문에 기대므로 신뢰도는 medium 이다. 기계류 로봇의 AI 요구가 기계규정 위임법령 경로를 따른다는 해석(f6)은 추정이다. 이 해석은 기존 위키의 '부속서 I 기계류 2028-08-02' 서술과 함께 제시했다(oq-106). 시행규칙 제7조의10 금액은 법령 기준 금액이며 실제 보험 약관의 한도가 아니다. oq-288 해결 인정(f18~f22). 정정 요청 없음. 2026-10-09-26 트랙 반영 제안은 이번에 반영하지 않았다. / 2차 수정 후 재검증. 드리프트 1건 처리: NVIDIA 가중치 라이선스를 '오픈소스'로 분류한 것을 수정하도록 지시했다. 그 밖에 브리프 밖 사실·수치는 없다. 1차 수정 지시 21건은 이행됐다. 다만 11절 첫 문단이 oq-288 해결과 모순되고, 4절 요약 문장에서 [의견] 태그가 빠졌으며, 5절에 태그 없는 문장이 하나 있다. [분류원문] 보존, 섹션 순서 준수. 링크는 유효하나, 재분리 과정에서 2026-09-30 주제 페이지로 가는 연결이 사라져 보강 블록의 '주제 페이지' 지시가 가리키는 대상이 불분명하다(분리 코드가 기존 '자세한 내용은' 링크 줄을 옮기지 않는 것으로 보여 pipeline 담당의 확인이 필요하다).",
  "retry_reason": null
}
```


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 11절(세부영역 페이지 11절 첫 문단, docs/topics/2026/2026-10-12-area59-s11.md 의 세 줄 요약 첫 줄과 3절 첫 문단): '기존 열린 질문 12건은 이번 실행에서 해결되지 않아 모두 열림으로 두고, 새 질문 5건을 올린다'는 2026-09-30 실행 기준 문장이다. 이번 실행의 oq-288 해결과 새 질문 2건 등록과 맞지 않는다. 11절 패치를 replace 로 보내 첫 문단을 이번 실행 기준(2026-09-30에 올린 질문 5건의 id 는 oq-288~oq-292, oq-288 해결, oq-143·oq-186·oq-187·oq-289·oq-291·oq-292 는 부분 근거만 있어 열림 유지, 새 질문 2건 등록)으로 고친다. 2026-09-30 질문 목록 페이지(docs/topics/2026/2026-09-30-area59-s11.md) 링크는 남긴다. 같은 페이지 안에서 상태가 서로 모순된다.
    - 4절 요약 문장(세부영역 페이지 4절, 2026-10-12-area59-s4 의 세 줄 요약 첫 줄): '이 영역의 용어는 … 나눠 볼 수 있다.' 뒤에 기존 페이지에 있던 '(구축자 의견) [의견][^ref-980][^ref-1227][^ref-1228][^ref-1236]'을 되살린다. 갱신 중에 기존의 검증된 문장에서 태그와 각주가 빠졌다.
    - 3·4·6·7·8·10·11절 보강 블록: 재분리 과정에서 세부영역 페이지가 가리키던 2026-09-30 주제 페이지(2026-09-30-area59-s3·s4·s6·s7·s8·s10·s11)로 가는 링크가 사라졌다. 그래서 '주제 페이지 둘째 문단'(s3), '주제 페이지 표에 같은 이름의 행'·'주제 페이지 표의 같은 행'·'SPDX 개요 행'(s7), '주제 페이지의 24시간·72시간·14일·1개월 기한 서술'·'주제 페이지의 제조물책임 증거 공개 … 서술'(s6), '주제 페이지의 Gibson Dunn 해설 항목'(s8)이 무엇을 가리키는지 알 수 없다. 각 블록에서 '주제 페이지'를 해당 2026-09-30-area59-sN.md 링크로 밝힌다. 각 절에는 '이전 상세 내용: [59. 법·규제·보험·라이선스 — <절 이름> (2026-09-30)](…)' 링크 한 줄을 남긴다. 이전 실행에서 검증된 상세 내용에 위키 안에서 다시 닿을 수 있어야 한다.
    - 5절 둘째 문단: 태그 없는 문장 '심사항목을 줄인 근거는 산업통상부 공고 제2025-042호(2025-11-06)의 행정예고다.'는 바로 뒤의 '최종 근거는 … 고시 제2025-21호다'와 충돌한다. 이 문장을 지우거나, '심사항목 축소는 산업통상부 공고 제2025-042호(2025-11-06) 행정예고로 예고됐다.'처럼 고치고 [사실][^ref-1519]를 붙인다. 이것은 f16 의 처분(행정예고안 기준, 최종 근거는 고시)에 맞추는 것이다.
    - 5절: 이 페이지에서 처음 나오는 '고시 제2025-21호'를 '산업통상부고시 제2025-21호(산업통상부 누리집 표기 제2025-021호)'로 한 번 병기한다. '지능형로봇법 시행규칙'도 처음 나올 때 정식 명칭 '지능형 로봇 개발 및 보급 촉진법 시행규칙'을 함께 쓴다. 1차 용어 지시는 페이지마다 첫 등장에 적용된다.
    - 7절(2026-10-12-area59-s7) NVIDIA GR00T-N1.6-3B 행: 유형 칸의 '오픈소스(가중치 공개, 비상업 라이선스)'를 '벤더 라이선스(모델 가중치)'처럼 고친다. 브리프(f41)는 이 라이선스를 오픈소스로 규정하지 않는다. 또 비상업 제한 라이선스를 오픈소스로 부르는 것은 브리프 밖 성격 규정이다.
    - 9절 보강 소절: 이 페이지에서 처음 나오는 'CRA'를 '사이버복원력법(Cyber Resilience Act, CRA)'으로 풀어 쓴다. 약어는 첫 등장 때 풀어 쓴다는 문체 규칙에 따른 것이다.
    - ref-1238 각주(세부영역 페이지 13절, 2026-10-12-area59-s3·s7 출처 절): 이번 실행에서 다시 열었고 reference_updates 의 접근일이 2026-10-12 이므로 각주 정의의 접근일도 2026-10-12 로 맞춘다. ref-1469 는 이미 맞춰져 있다. 각주와 참고문헌 갱신 값이 어긋나면 안 된다.
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 46건, 미확인 2건, 교차 확인 4건(f1~f4: AI 옴니버스 발효일·적용일·기계류 Section B 이동을 ERTICO·Hunton·Cooley·IBF 해설로 독립 확인). 강등: f14 사실 → 추정(제35조① 개정 표시가 있어 원법부터의 의무라고 단정할 수 없음), f17 사실 → 추정(고시 제8조①2호 원문 미확인). 원문 미열람 출처: ref-1227, ref-1235(리서치에서 다시 열지 않음). 검증 단계에서도 열지 못한 출처는 ref-1517·ref-1522·ref-1529·ref-1530·ref-1519·ref-1469·ref-1520·ref-1531이며, 검색 결과·2차 해설·이전 검증 실행과 일치하는지로 확인했다. 주의: 모든 사실 주장이 단일 1차 원문에 기대므로 신뢰도는 medium 이다. 기계류 로봇의 AI 요구가 기계규정 위임법령 경로를 따른다는 해석(f6)은 추정이다. 이 해석은 기존 위키의 '부속서 I 기계류 2028-08-02' 서술과 함께 제시했다(oq-106). 시행규칙 제7조의10 금액은 법령 기준 금액이며 실제 보험 약관의 한도가 아니다. oq-288 해결 인정(f18~f22). 정정 요청 없음. 2026-10-09-26 트랙 반영 제안은 이번에 반영하지 않았다. / 2차 수정 후 재검증. 드리프트 1건 처리: NVIDIA 가중치 라이선스를 '오픈소스'로 분류한 것을 수정하도록 지시했다. 그 밖에 브리프 밖 사실·수치는 없다. 1차 수정 지시 21건은 이행됐다. 다만 11절 첫 문단이 oq-288 해결과 모순되고, 4절 요약 문장에서 [의견] 태그가 빠졌으며, 5절에 태그 없는 문장이 하나 있다. [분류원문] 보존, 섹션 순서 준수. 링크는 유효하나, 재분리 과정에서 2026-09-30 주제 페이지로 가는 연결이 사라져 보강 블록의 '주제 페이지' 지시가 가리키는 대상이 불분명하다(분리 코드가 기존 '자세한 내용은' 링크 줄을 옮기지 않는 것으로 보여 pipeline 담당의 확인이 필요하다).

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
