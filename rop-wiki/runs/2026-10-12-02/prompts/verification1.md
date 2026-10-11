(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
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

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
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

### docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md (요약)

```markdown
# 36. 가상 시운전·실제 상황 재현

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실행 전 계획 검증**: 선언한 초기 조건에서 경로·자원·능력을 실제로 실행하지 않고 정적으로 검사한다
- **가상 시운전**: 실제 설치 전에 연동과 운영 정책을 가상 환경에서 시험한다
- **운영 기록 기반 재현**: 실제 운영 기록으로 시뮬레이션의 초기 상태와 사건을 다시 구성한다
- **시뮬레이션–현실 차이 관리**: 시뮬레이션 결과를 현실에 적용할 때 생기는 차이를 측정하고 보정한다
- **디지털 트윈 동기화**: 실시간 상태를 가상 모델에 계속 반영해 현재 상태 표현과 미래 실험을 잇는다

## 2. 핵심 질문

설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
```

### docs/categories/safety/safety-standards-certification-and-incident-investigation.md (요약)

```markdown
# 50. 안전 표준·인증·사고 조사

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

안전 표준 적합성·인증, 사고 기록과 사후 조사 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **안전 표준·인증**: 산업용 로봇·이동 로봇·서비스 로봇 안전 표준(ISO 10218, ISO 3691-4, ISO 13482 등)과 인증에 맞춘다
- **사고 기록·사후 조사**: 사고와 아차 사고를 기록하고 원인을 조사해 재발을 막는다

## 2. 핵심 질문

어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
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

### docs/categories/security-and-privacy/privacy-and-video-data.md (요약)

```markdown
# 53. 개인정보·영상 데이터

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1486건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [59] 에 걸린 25건 / 전체 393건)

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

### runs/2026-10-12-01/research.md

```markdown
# 리서치 브리프 2026-10-12-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-01 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 58. 다사업자 책임·계약·데이터 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area58-s4) — '데이터 보유자' 항목(40행)이 '사용자 동의 없이 비개인 데이터를 이용할 수 없다'로 데이터법 제4조(13)의 '사용자와의 계약을 근거로만'과 다르고, 근거가 해설 페이지(ref-1191)뿐
- 섹션 5. 적용 사례 — 병원 사례가 2025 공고 하나(ref-872, 각주에 '원문 미열람')에 기대며 '연 2회 평가·인증'(71행 표 '수행 자원', 76행 본문)을 원어 'bi-annual' 의 한 해석으로 단정, 2026 공고(연례·AutoveX 2026-09-01부터 2년) 미반영. 상업·물류 현장의 실제 공개 계약 문안(지원 응답·시설 장애·책임 상한) 사례 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area58-s6) — 데이터 계약 소절(51·53행)에 '쉽게 이용 가능한 데이터' 범위·제3조(1) 설계 의무의 별도 적용일·MCT/SCC 의 제3자 면책 공백 없음. 변경 주체 책임 소절에 EU 제조물책임지침(소프트웨어 포함·실질적 변경자·업무용 재산 제외·증거 공개 비례성) 없음. 서비스 수준 소절(65행)이 ISO/IEC 19086-1(원문 미열람) 일반론뿐이라 응답·복구 시계, 시설 장애 예외, API 가용성 측정식 같은 실제 조항 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area58-s7) — 표에 EU 제조물책임지침과 RFC 9745(폐기 예고·종료 시각) 행이 없고, 데이터법 행(41행)이 일반 적용일만 적음
- 섹션 8. 대표 연구와 자료 — 세 건뿐이며 데이터 접근 거절(영업비밀) 관할별 관행을 다룬 동료심사 연구 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area58-s11) — oq-241·oq-268·oq-279·oq-280·oq-259·oq-185 에 붙일 공개 원문 근거 없음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s4.md 40행 데이터 보유자 정의, 본 페이지 71·76행 '연 2회', ref-872·ref-706 의 '원문 미열람' 표시

## 조사 질문

1. 제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
2. EU 데이터법에서 데이터 보유자의 비개인 데이터 이용 근거와 사용자에게 제공할 데이터 범위, 설계 의무의 적용 시점은 원문상 무엇인가(oq-279·oq-320)? (섹션 4·6·7 겨냥)
3. 공개된 모델 계약 조항·표준 계약 조항과 EU 개정 제조물책임지침은 제3자 청구·소프트웨어 결함·실질적 변경·증거 공개를 다사업자 사이에서 어떻게 다루는가(oq-241·oq-289)? (섹션 6·7 겨냥)
4. 로봇 서비스·관제 플랫폼의 공개 약관은 지원 응답 시간·시설 장애 예외·책임 상한·과금 단위·가용성 측정을 어떻게 정하는가(oq-112·oq-268)? (섹션 5·6 겨냥)
5. API 폐기 예고와 종료 시각의 관계를 정한 표준은 무엇을 정하고 무엇을 계약에 남기는가(oq-280)? (섹션 7 겨냥)
6. 통합자 사전 자격(RoMi-H 등재)의 주기·유효기간과, 영상 처리 위탁·데이터 접근 거절의 관리 기준은 공개 원문상 무엇인가(oq-149·oq-259)? (섹션 5·6·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU 데이터법(Regulation (EU) 2023/2854) 제4조(13)은 데이터 보유자가 쉽게 이용 가능한 데이터 가운데 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있다고 정하고, 그 데이터로 사용자의 경제 상황·자산·생산 방식을 추론해 사용자의 시장 지위를 해치는 이용을 금지한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | 데이터법 제4조(1)은 사용자가 연결 제품·관련 서비스에서 데이터에 직접 접근할 수 없을 때 데이터 보유자가 '쉽게 이용 가능한 데이터'와 그 해석·이용에 필요한 관련 메타데이터를 지체 없이 무료로 제공하도록 하며, 제2조(17)은 '쉽게 이용 가능한 데이터'를 데이터 보유자가 과도한 노력 없이 연결 제품·관련 서비스에서 적법하게 얻거나 얻을 수 있는 제품 데이터·관련 서비스 데이터로 정의한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | 데이터법 제50조는 이 규정을 2025-09-12부터 적용한다고 하면서, 제3조(1)의 설계 의무(연결 제품·관련 서비스를 데이터에 직접 접근 가능하게 설계·제조할 의무)는 2026-09-12 후에 시장에 출시되는 연결 제품과 관련 서비스에 적용한다고 따로 정한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | 집행위원회 권고 초안 부속서(C(2025) 7750 final ANNEX, 2025-11-19)의 클라우드 표준 계약 조항(SCC) 중 책임 조항 설명(Annex X)은 '이 SCC 는 면책(indemnification) 조항을 포함하지 않는다'고 적고, 한 당사자의 중대한 의무 위반으로 생긴 제3자 청구에 대해 면책·보호 조항이 필요한지와 그 범위를 당사자가 검토하도록 권한다. | ref-1489, ref-1192 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | EU 개정 제조물책임지침(Directive (EU) 2024/2853) 제4조(1)은 '제품'에 소프트웨어를 포함하고, 제2조(2)는 상업 활동 밖에서 개발·공급된 자유·오픈소스 소프트웨어에는 지침을 적용하지 않는다고 정한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | 같은 지침 제8조(2)는 제조자의 통제 밖에서 제품을 실질적으로 변경한 뒤 시장에 내놓거나 사용에 투입한 자연인·법인을 그 제품의 제조자로 본다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | 지침 제2조(1)의 적용 대상은 2026-05-07 정오표(OJ L 2026/90364)로 '2026-12-09 후'에서 '2026-12-08 후(after 8 December 2026)' 시장에 출시되거나 사용에 투입된 제품으로 고쳐졌으며, 따라서 2026-12-09 당일부터 출시·투입되는 제품에 적용된다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | 지침 제22조(1)은 회원국이 지침 이행 법령을 2026-12-09까지 시행하도록 정하고, 제21조는 구 제조물책임지침 85/374/EEC 를 2026-12-09 부로 폐지하되 그 전에 출시·사용 투입된 제품에는 계속 적용한다고 정한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | 지침 제6조(1)(b)(iii)은 전적으로 업무 목적으로만 쓰는 재산의 손해를 이 지침의 보상 대상 손해에서 제외한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | 지침 제9조(3)은 같은 조 제1·2항에 따른 증거 공개를 필요하고 비례적인 범위로 제한하도록 회원국에 요구하고, 제9조(4)는 그 판단에서 제3자를 포함한 모든 당사자의 정당한 이익, 특히 기밀·영업비밀 보호를 고려하게 한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | 창이종합병원 CHART 의 2025년 RoMi-H 등재 공고는 프로그램을 'a bi-annual RoMi-H Empanelment Program'으로 적고, 같은 공고에서 등재 통합자 5개사(HOPE Technik, Medisys Innovation, Panasonic Asia Pacific, QuikBot Technologies, Techfox)의 등재가 2025-05-01부터 2년간 유효하다고 게시한다. | ref-872 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [추정] | 2025년 공고의 'bi-annual'은 '연 2회'로도 '2년마다'로도 읽힐 수 있고 같은 공고가 등재 유효기간을 2년으로 적고 있어, 위키 5절의 '연 2회 평가·인증'(본문 76행, 표 '수행 자원' 행)은 원어 인용과 두 해석을 함께 적거나 [추정]으로 낮춰야 한다. | ref-872, ref-1495 | 아니오 | low | 2026-10-12 | — | — |
| f13 | [사실] | SingHealth/CHART 의 2026년 RoMi-H 등재 공고(2026-05-06 게시, 2026-08-24 갱신)는 CHART 가 연례(annual) 등재 프로그램을 운영해 통합자의 RoMi-H 배치 역량을 평가·재평가한다고 적고, 등재 통합자는 CHART 웹사이트에 공개되어 공공 의료기관이 제안요청(RFP/RFI) 참여를 위해 연락할 수 있다고 적는다. | ref-1495 | 아니오 | medium | 2026-10-12 | 병원 / 수행 자원 | — |
| f14 | [사실] | 2026년 공고의 등재 명단은 AutoveX Pte Ltd 1개사이며 등재는 2026-09-01부터 2년간 유효하다. | ref-1495 | 아니오 | medium | 2026-10-12 | 병원 / 수행 자원 | — |
| f15 | [사실] | 개인정보보호위원회는 「이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서」 발표 보도자료(2024-10-14 게시)에서 외부업체 위수탁으로 개인영상정보를 처리하는 경우 보호책임자 지정과 주기적인 점검ㆍ교육 등으로 안전하게 관리할 것을 당부했다. | ref-1494 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | RFC 9745(2025-03, Standards Track) §5 는 자원을 폐기 예정(deprecated)으로 표시하는 행위가 자원의 동작을 바꾸지 않으며, 클라이언트는 폐기 표시 전과 같은 방식으로 자원을 계속 쓸 수 있다고 정한다. | ref-706 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | RFC 9745 §4 는 Sunset 헤더(RFC 8594)로 자원이 응답하지 않게 될 시각을 함께 알릴 수 있게 하고, Sunset 시각이 Deprecation 시각보다 빨라서는 안 된다(MUST NOT)고 정하며, 두 시각 사이의 최소 간격은 정하지 않는다. | ref-706 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | De Noyette·Stähler·Margoni(IIC 56(5):984–1014, 2025)는 데이터법의 영업비밀 체계를 분석하며, 회원국 관할 당국마다 영업비밀 관련 행정 관행이 달라져 더 파편화될 위험이 있다고 지적한다. | ref-1488 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [추정] | Relay Robotics 공개 약관의 서비스 수준 부속서(Exhibit A)에 따르면 Tier 1(24시간 콜센터)은 서비스 개시일 이후 이메일 지원 요청을 받은 뒤 60분 안에 응답하도록 '상업적으로 합리적인 노력'을 기울이는 조건이며, 복구 완료 시각을 보장하는 문구는 아니다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f20 | [추정] | Relay 약관의 같은 부속서 예외 조항에 따르면 고객의 네트워크나 시설(예: 승강기 고장)에서 생긴 문제는 고객이 고칠 때까지 지원 기한이 연장되고, Relay 는 고객 네트워크·시설 문제의 수리 책임을 지지 않는다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f21 | [추정] | Relay 약관 §12 에 따르면 면책 의무, 고객의 라이선스 위반, 양측의 비밀유지 위반을 제외한 각 당사자의 책임은 청구 발생 전 18개월 동안 고객이 지급했거나 지급할 요금 총액을 넘지 않으며, 약관 준거법은 미국 캘리포니아주법이다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f22 | [추정] | Relay 약관 §5.2 에 따르면 당사자 사이에서 고객이 Relay 와 공유하기로 한 개인정보는 고객 소유이며, Relay 는 서비스 제공 목적에만 쓴다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f23 | [추정] | Formant 일반 약관(2026-04-16 갱신)에 따르면 고객이 지정한 통합자('Development Consultant')는 고객의 지시로만 일하며 고객이 그 통합자의 작위·부작위에 책임을 진다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f24 | [추정] | Formant 약관의 'Device' 정의에 따르면 하나의 장치에 가상 환경(PLC, Jetson, 가상 머신 등)이 둘 이상 있으면 가상 환경마다 별도 Device 로 센다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f25 | [추정] | Formant 약관의 Formant AI 추가 조건에 따르면 고객은 AI 출력에 의존하거나 그 출력으로 명령을 실행하기 전에 출력을 검증하는 사람의 검토 절차를 사용 과정에 두어야 한다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f26 | [추정] | AIRROBO(Best Epoch Technology)의 EU 데이터법 고지 §4(b)에 따르면 사용자는 앱에서 데이터를 내보내 한 번에 공유하거나, 승인된 QR 코드로 제3자와 지속 공유할 수 있으며 지속 공유를 받으려는 제3자는 Tuya 클라우드 플랫폼에 등록해야 한다. | ref-1487 | 아니오 | low | 2026-10-12 | 가정 / 작업 대상 | 벤더 주장 |
| f27 | [추정] | AWS IoT RoboRunner 서비스 수준 협약(2022-11-28 갱신)에 따르면 'Error'는 500 또는 503 오류 코드를 돌려준 요청이고, 가용성은 5분 구간마다 오류 없이 처리된 요청 비율로 계산한다. | ref-1492 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f28 | [추정] | 같은 SLA 는 요청이 하나도 없던 5분 구간을 가용성 100%로 간주한다. | ref-1492 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f29 | [추정] | 1X Technologies 의 사전예약 약관(2025-10-28 갱신) §2.4 에 따르면 주문 초대를 받아 로봇을 받으려는 사람은 구매 시점에 제시되는 별도 판매약관(Terms of Sale)에 동의해야 하며, 취소·배송·보증 세부는 주문 초대나 판매약관에 둔다. | ref-1493 | 아니오 | low | 2026-10-12 | 가정 | 벤더 주장 |
| f30 | [의견] | ROP 의 데이터 자산 대장은 데이터 항목마다 데이터법상 역할(사용자·데이터 보유자·제3자), 이용 근거(사용자와의 계약), 요청 가능 범위(쉽게 이용 가능한 데이터·메타데이터), 연결 제품의 출시일(2026-09-12 후 출시 여부)을 따로 기록하고, 개인정보 처리 근거는 별도로 심사하는 편이 좋다. | ref-636 | 아니오 | low | 2026-10-12 | — | — |
| f31 | [의견] | 다사업자 계약은 클라우드 SCC 의 책임 조항을 그대로 옮기지 말고, 로봇 제조사·통합자·시설 관리주체·플랫폼 사이의 제3자 청구 면책을 따로 정해야 하며, 제조물책임지침이 업무 전용 재산 손해를 보상 대상에서 빼므로 사업장 설비·재고 손해는 계약 조항으로 다룰 필요가 커 보인다. | ref-1489, ref-1490 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [의견] | ROP 는 사고 뒤 증거 공개가 법원 판단으로 필요·비례 범위에 한정된다는 점을 전제로, 로그 보관 기간·사고 후 동결·내보내기 형식·영업비밀 분리 절차를 계약 부속서에 미리 정해 두는 편이 좋다. | ref-1490 | 아니오 | low | 2026-10-12 | — | — |
| f33 | [의견] | 서비스 수준 부속서는 응답 시각·원인 분석·복구 완료 시각을 나누고, 시설 장애로 지원 기한이 멈추는 구간의 시작·종료와 확인 주체를 기록하며, API 오류율과 별도로 작업 성공률·지연·시설 대기 시간을 지표로 합의하는 편이 좋다. | ref-1491, ref-1492 | 아니오 | low | 2026-10-12 | — | — |
| f34 | [의견] | 플랫폼 약관과 고객–통합자 계약을 함께 대조해 통합자 행위의 책임 귀속, 과금 수량 단위(로봇 대수·가상 환경·설치 인스턴스)의 대응표와 계량 이의 절차, AI 출력으로 명령을 실행할 때의 검토자·승인 기록을 정하는 편이 좋다. | ref-1496, ref-1491 | 아니오 | low | 2026-10-12 | — | — |
| f35 | [의견] | 제조사의 데이터법 고지가 안내하는 내보내기·제3자 지속 공유 경로는 ROP 온보딩 때 제3자 등록·필드 목록·지연·승인 철회를 직접 시험해 확인하는 편이 좋다. | ref-1487 | 아니오 | low | 2026-10-12 | — | — |
| f36 | [의견] | 통합자 등재(사전 자격)는 연동 역량 평가일 뿐이므로, 등재 사실과 별도로 인수 기준·장애 복구 책임·등재 유효기간 만료 시 처리를 계약에 적는 편이 좋다. | ref-872, ref-1495 | 아니오 | low | 2026-10-12 | 병원 / 완료·인계 | — |
| f37 | [의견] | ROP 어댑터는 제조사 API 의 폐기 예고 시각·종료(Sunset) 시각·전환 문서 링크를 따로 저장하고, 두 시각 사이의 최소 통지 기간은 RFC 가 정하지 않으므로 계약에서 따로 확인하는 편이 좋다. | ref-706 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [의견] | 영상 처리를 다른 사업자에게 맡길 때는 위탁 범위·보호책임자·교육·주기 점검 증빙을 계약 부속서로 관리하고, 데이터 접근 거절(영업비밀) 사유와 이의 경로는 관할별로 기록하되 법학 논문의 제안을 검증된 운영 성과로 표시하지 않는 편이 좋다. | ref-1494, ref-1488 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-636 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 아니오 |
| ref-1192 | European Commission (Shaping Europe's digital future) | Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts | 2025-11-19 | 정부·연구기관 | high | 2026-10-12 | https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding | 아니오 |
| ref-872 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | 정부·연구기관 | medium | 2026-10-12 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 2025-03 | 표준 | high | 2026-10-12 | https://www.rfc-editor.org/info/rfc9745/ | 아니오 |
| ref-1487 | Best Epoch Technology Co., Ltd. (AIRROBO) | EU DATA ACT Notice | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://owebsite-cdn.ubtrobot.com/resources/file/2025/12/25/755762357268549.pdf | 아니오 |
| ref-1488 | De Noyette, E., Stähler, L., Margoni, T. (IIC 56(5)) | Data Secrets: The Data Act's New Trade Secrets Framework | 2025-04-24 | 논문 | medium | 2026-10-12 | https://link.springer.com/article/10.1007/s40319-025-01601-9 | 아니오 |
| ref-1489 | European Commission | ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final | 2025-11-19 | 정부·연구기관 | high | 2026-10-12 | https://ec.europa.eu/newsroom/dae/redirection/document/121719 | 아니오 |
| ref-1490 | European Union (EUR-Lex) | Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC | 2024-11-18 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng | 아니오 |
| ref-1491 | Relay Robotics | Terms of Service (Exhibit A: Service Level Agreement) | 2023-03-01 | 벤더 문서 | medium | 2026-10-12 | https://relayrobotics.com/tos | 아니오 |
| ref-1492 | Amazon Web Services | AWS IoT RoboRunner Service Level Agreement | 2022-11-28 | 벤더 문서 | medium | 2026-10-12 | https://aws.amazon.com/roborunner/sla/ | 아니오 |
| ref-1493 | 1X Technologies, Inc. | Pre-Order Terms | 2025-10-28 | 벤더 문서 | medium | 2026-10-12 | https://www.1x.tech/legal | 아니오 |
| ref-1494 | 개인정보보호위원회 | 자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다 | 2024-10-14 | 정부·연구기관 | high | 2026-10-12 | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678 | 아니오 |
| ref-1495 | SingHealth / Changi General Hospital CHART | RoMi-H Empanelment Programme 2026 | 2026-05-06 | 정부·연구기관 | medium | 2026-10-12 | https://www.singhealth.com.sg/news/robotics/romi-h-empanelment-programme-2026 | 아니오 |
| ref-1496 | Formant | General Terms | 2026-04-16 | 벤더 문서 | medium | 2026-10-12 | https://www.formant.ai/terms_of_use | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md | 4, 5, 6, 7, 8, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area58-s4) — 40행 '데이터 보유자' 항목 정정: '사용자와 계약을 맺어야 하고 사용자 동의 없이 비개인 데이터를 이용할 수 없다'[사실][^ref-1191] → '쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고, 사용자의 시장 지위를 해치는 추론에 쓸 수 없다'(f1, 근거 ref-636 원문). '쉽게 이용 가능한 데이터' 범위(f2)를 같은 항목이나 새 줄로 / 섹션 5 — 병원 사례: 71행 표 '수행 자원'과 76행 본문의 '연 2회'를 원어 'bi-annual'(2025 공고) 인용과 두 해석(연 2회/2년마다) 병기 또는 [추정]으로 정정(f11·f12), 2025 등재 5개사·2년 유효(f11), 2026 공고의 연례 표현·RFP/RFI 연락 경로(f13)와 AutoveX 2026-09-01부터 2년(f14)을 추가하고 '(2025-05 기준)'을 연차별로 나눔. ref-872 각주의 '(원문 미열람)' 해소. 의견 f36. 새 사례 블록(배송 로봇 서비스 계약; 약관이 현장 유형을 특정하지 않아 '병원·호텔 배송 로봇 업체의 공개 약관'으로만 표기): Relay 약관의 Tier 1 60분 응답 노력(f19), 시설 장애(승강기 고장) 시 지원 기한 연장(f20)을 '단일 업체 약관에 따르면' [추정]·벤더 주장으로, 완료·인계/예외·성과는 미확인. 가정 사례에 AIRROBO 고지의 QR 지속 공유 경로(f26)와 1X 사전예약 약관의 판매약관 위임(f29)을 [추정]·벤더 주장으로 짧게; 의견 f35 / 섹션 6(분리 2026-09-30-area58-s6) — 데이터 접근·공유 계약 소절: 일반 적용일(기존 51행) 뒤에 제3조(1) 설계 의무는 2026-09-12 후 출시 제품에만 적용(f3), 제4조(1)·(13) 범위와 계약 근거(f1·f2); MCT/SCC 문단(53행) 뒤에 부속서 X 의 면책 조항 부재와 제3자 청구 검토 권고(f4); 의견 f30·f31. 변경 주체 책임 소절: EU 개정 제조물책임지침의 다사업자 책임 관점 핵심만 — 소프트웨어 포함·비상업 FOSS 제외(f5), 실질적 변경자=제조자(f6), 적용 대상 '2026-12-08 후' 출시·투입 = 2026-12-09부터(f7, 정오표 2026-05-07; '2026-12-08부터'로 쓰지 말 것), 이행 기한 2026-12-09·구 지침 폐지(f8), 업무 전용 재산 손해 제외(f9), 증거 공개 필요·비례성과 영업비밀 고려(f10); 의견 f31·f32. 서비스 수준 약속과 감사 이력 소절: 공개 약관 비교 — Relay 책임 상한 18개월 요금·예외 3가지·캘리포니아 준거법(f21), 개인정보 고객 귀속(f22), Formant 통합자 책임 고객 귀속(f23)·가상 환경별 Device 계수(f24)·AI 출력 사람 검토(f25), AWS RoboRunner Error=500/503·5분 가용성·요청 없는 구간 100%(f27·f28) — 모두 [추정]·벤더 주장, 문장에 'OO사 약관에 따르면', 단일 업체 사례로 한정하고 업체 간 교차 확인으로 세지 않음; 의견 f33·f34. 영상 위탁 관리: 개인정보위 보도자료의 위수탁 시 보호책임자·주기 점검·교육 당부(f15)를 한두 문장으로만 넣고 53영역으로 연결; 의견 f38 / 섹션 7(분리 2026-09-30-area58-s7) — 데이터법 행(41행)에 '제3조(1)은 2026-09-12 후 출시 제품' 추가(f3). 행 추가: EU 개정 제조물책임지침(Directive (EU) 2024/2853, 소프트웨어 포함·실질적 변경자·적용 2026-12-09부터·이행 기한 2026-12-09, f5~f8), RFC 9745(폐기 표시는 동작 불변, Sunset≥Deprecation, 최소 간격 미규정, f16·f17); 의견 f37 / 섹션 8 — 연구 항목 추가: De Noyette·Stähler·Margoni(IIC 2025) 데이터법 영업비밀 체계와 관할별 행정 관행 파편화 위험(f18); 기존 MCT 항목(109행)은 기존 내용 확인(부속서 X 면책 공백은 6절로) / 섹션 11(분리 2026-09-30-area58-s11) — 해결 없음. 부분 근거: oq-241(f19~f25, 네 당사자 공통 분담표는 여전히 없음), oq-268(f24·f27·f28·f20; 메모의 'Formant 가상 환경 수량 공동 검증 주문서' 질문은 oq-268 의 하위 질문이라 새로 만들지 않음), oq-279·oq-320(f1·f2, 특정 ROP 지위 미판정), oq-280·oq-207(f16·f17, 로봇 계약상 최소 통지 일수 미확인), oq-259(f15), oq-185(f29, 원격 조작자 책임 미확인), oq-249(f10 은 법원 증거 공개 범위일 뿐 기계 규정 로그 의무의 플랫폼 적용은 미판정), oq-289(f5·f6 원문 조문만, 오케스트레이션 SW 해당 여부 미판정), oq-149(f13·f14, 국내 사례 없음), oq-110(f1~f3·f26). 답하지 못함: oq-145, oq-265, oq-281(가이드 본문 미열람), oq-282, oq-283, oq-290. 새 질문 3건 / 기존 내용 확인(새로 넣지 않음): MCT·SCC 사용이 자발적이라는 점(메모 F04) — s6.md 53행·s7.md 42행·본 페이지 109행·용어집 model-contractual-terms; 데이터법 일반 적용일 2025-09-12 — s6.md 51행·s7.md 41행; RFC 9745 Sunset≥Deprecation — 2026-09-25-area28-s4.md 40행(원문 미열람 근거였음); 증거 공개 제도 자체 — 2026-09-30-area59-s6.md 45행; 영상 위탁 점검 — privacy-and-video-data.md 108행(기사 ref-1136 근거) / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/glossary/data-holder.md 정의가 '연결 제품' 정의처럼 잘못 쓰임, docs/categories/security-and-privacy/index.md 169행의 비슷한 서술(ref-1274, ref-1191 과 같은 EC 해설 페이지), docs/topics/2026/2026-09-25-area28-s3.md 41행 '주요 조항의 적용 개시일은 미확인'(f3 로 해소 가능), docs/topics/2026/2026-09-30-area03-s7.md 44행·2026-09-30-area56-s7.md 46행 '연 2회'(f12), 59영역(2026-09-30-area59-s3·s4·s6·s7·s8, glossary/product-liability.md, standards/index.md 342행)의 제조물책임지침 서술 근거를 Gibson Dunn 해설(ref-1227)에서 원문(ref-1490)으로, 53영역 108행 근거를 1차 보도자료(ref-1494)로, ref-706 서지(발행 2025-03, 원문 열람). EU AI법 제25·26조 서술(s6.md 43·65행)은 개정 여부 점검 필요(미확인). 다음 실행 후보: 59. 법·규제·보험·라이선스(f5~f10), 63. 병원·의료(f11~f14), 3. 경제성·조달·사업 모델(f24·f27·f28) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 여러 사업자가 얽힌 장애·사고에서 서비스 수준 협약의 지원 기한을 멈추는 사유(시설 장애 등)와 재개 시점을 누가 확인·승인하며, 각 계약의 로그를 어떤 공통 식별자로 연결하는가? (관련: oq-112) | 관련 영역: 58. 다사업자 책임·계약·데이터, 32. 예외 복구·재계획·업무 연속성 | 근거: f20 | 종류: 일반
- 제조사의 데이터법 고지가 안내하는 제3자 지속 공유 경로(승인 QR 코드·외부 플랫폼 등록 등)는 실제로 어떤 필드를 어떤 지연으로 제공하며, 사용자가 승인을 철회하면 언제 공유가 끊기는가? (관련: oq-110, oq-279) | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동 | 근거: f26 | 종류: 일반
- RoMi-H 통합자 등재 프로그램의 실제 운영 주기는 무엇인가(2025 공고 'bi-annual', 2026 공고 'annual', 등재 유효 2년), 그리고 유효기간이 끝난 등재 통합자가 맡은 연동의 유지·장애 복구 책임은 어떻게 이어지는가? (관련: oq-149) | 관련 영역: 58. 다사업자 책임·계약·데이터, 63. 병원·의료 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 10건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-01/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f4: C(2025) 7750 final 의 권고가 최종 채택(관보 게재)되었는지와 다국어본 공개 상태는 확인하지 못함(EC 페이지는 2026-03-03 갱신에도 Draft 표기). 합리적 보상 지침의 후속 발표 여부도 미확인
    - f5~f10: 회원국별 제조물책임지침 이행 법령과 국내 제조물책임법의 소프트웨어 포함 개정 여부(oq-290)는 확인하지 못함. 오케스트레이션 소프트웨어가 제품·관련 서비스에 해당하는지(oq-289)는 판단하지 않음
    - f11·f12: 2025 공고 'bi-annual'의 의도(연 2회/2년마다)는 공고 원문만으로 확정할 수 없음
    - f15: 개인정보위 보도자료는 독립 검증 보고의 원문 대조 기준이며, 안내서 본문(ref-1135)과 개인정보 보호법 조문은 이번에 다시 열지 않음
    - f18: 논문 §4.1.4 구절은 독립 검증 보고의 원문 대조 기준(로컬 저장본은 접근 차단 페이지), 서지는 Crossref 로 확인
    - f19~f29: 벤더 약관은 공개 웹 문안이며 개별 체결본·주문서·단가·이행 실적은 미확인. AWS IoT RoboRunner 의 조사일 현재 신규 제공·지원 상태 미확인(지원 종료 공지는 찾지 못함). AIRROBO 고지의 발행일 미확인(PDF 작성 2025-12-23)
    - 검증 보고의 2차 자료 언급: 데이터법 개정안(Digital Omnibus, COM(2025) 837)이 협상 중으로 보이고 EU AI법이 개정되었다는 점은 원문으로 확인하지 않아 finding 으로 넣지 않음 — s6.md 의 AI법 제25·26조 서술 영향은 후속 점검
    - oq-145(모델 대체·라우팅 희석 계약), oq-265(R15.08-3 사용자 의무), oq-281(산업데이터 계약 가이드 432쪽 본문), oq-282(기계 규정 실질적 변경과 플랫폼 설정 변경), oq-283(로봇-승강기 연동 표준 결과물)은 이번 메모가 답하지 못함
- 범위 경계 위반 의심:
    - f5~f10: EU 제조물책임지침의 법적 효력·적용 판단은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 다사업자 책임 관점 핵심만 씀
    - f15: 영상 위탁 관리는 53. 개인정보·영상 데이터와 겹치며, 이 영역에는 계약 부속서 관리 관점의 짧은 연결로만 씀
    - f11~f14: RoMi-H 등재는 63. 병원·의료와 겹치며, 이 영역에는 통합자 사전 자격과 책임 주체 관점으로만 씀
    - f16·f17: RFC 9745 는 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성과 겹치며, 이 영역에는 제조사 API 폐기 통지의 계약 관점으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1487~ref-1496, 예약 구간 ref-1487~ref-1516 안), 재사용 4건(ref-636·ref-1192·ref-872·ref-706). 출처 매핑(검증 결과 기준): 메모 n1→ref-636, n2→ref-1487(UBTech CDN), n3→ref-1488, n4→ref-1192, n5→ref-1489(미러 dirittobancario.it 대신 공식 EC URL), n6→ref-1490(EUR-Lex 원문; ref-1227 은 해설이라 쓰지 않음), n7→ref-1491(약관 표기 2023-03-01), n8→ref-1492, n9→ref-1493, n10→ref-1494(안내서 ref-1135·기사 ref-1136 과 별개 1차 보도자료), n11→ref-1495, n12→ref-872, n13→ref-706(원문 열람), n14→ref-1496. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: EC 발표·부속서, CHART 2025·2026 공고) — 신뢰도 medium 이하. 벤더 약관 11건(Relay·Formant·AIRROBO·AWS·1X)은 모두 [추정]·vendor_claim, 서로 다른 업체의 다른 조건이라 교차 확인으로 세지 않음. 검증 반영: A01 정정 위치를 6절이 아니라 s4.md 40행(4절)으로, 근거 ref-1191→ref-636(f1); F03 제3조(1) 적용 대상(2026-09-12 후 출시)과 일반 적용일(2025-09-12) 구분(f3); F04 는 기존 내용이라 제외; F05 출처를 공식 EC URL 로(f4, 면책 조항 없음); 제조물책임지침은 다사업자 책임 관점 핵심만(f5~f10) 넣고 정오표 표기 '2026-12-08 후'=2026-12-09부터로 명시(f7), 제8조(2) 실질적 변경자 추가(f6); F13 'bi-annual' 원어 인용과 두 해석으로 정정(f11 사실·f12 추정); F14 는 53영역 중복이라 짧게(f15); RFC 9745 는 원문 열람으로 보강(f16·f17); 벤더 약관 X01~X11 은 '○○사 약관에 따르면'·단일 업체 사례로 한정(f19~f29), Formant 는 정의 번호 대신 용어 이름으로 인용. 열린 질문: 해결 없음. 부분 근거 oq-241·oq-268·oq-279·oq-320·oq-280·oq-207·oq-259·oq-185·oq-249·oq-289·oq-149·oq-110. 메모의 '답한 열린 질문' 가운데 '새 질문' 5건은 문구 대조로 기존 oq-279~oq-283 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 3건 중 지원 기한 정지·제3자 공유 실동작 2건을 새로 올리고 Formant 수량 검증 건은 oq-268 에 묶음; RoMi-H 주기 질문 1건 추가. 메모의 '.research-work' 로컬 경로·행 번호(L…)는 쓰지 않고 원문 조·절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-10-11-06/research.md

```markdown
# 리서치 브리프 2026-10-11-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-06 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 50. 안전 표준·인증·사고 조사 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 실외 사례 표·본문(98·100·104·106행)이 고시 제2023-211호를 현행 근거로 두고 심사항목 8개·16가지를 '어느 쪽도 고르지 않고' 병기하며, 행정예고 기준값을 '확정 고시 별표 원문 미확인'으로 둠. 제조 공장·물류창고 사고 사례는 수사·조사 중 기사 두 건뿐이고 공식 재해사례 자료가 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area50-s6) — '사고 기록 장치' 소절의 '기록할 데이터 형식과 보존 기간 … 미확인'(45행), 조직·제어 책임까지 보는 사고 분석 방법(CAST) 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area50-s7) — EN ISO 10218 EU 조화 게재 행(42행)이 IBF 해설 단독 근거로 [사실], 실외이동로봇 행(45행)의 '고시 제2023-211호가 정한다'가 낡음, R15.08-3·ISO 3691-4 차기판·KS 부합판·UL 3100·국내 자율안전확인·EU 기계 규정 기록 요구·rosbag2/MCAP 기록 계약 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area50-s8) — Sanders 외의 관측 기간·관할 범위 미기재, 미국 보상 청구 자료(Suresh 외 2026) 없음, Webb 외 역할극의 수행 조건·한계 미기재
- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area50-s4) — '적합성 추정' 항목(41행)이 해설 기준이고 2027-01-20 목록 폐지 미반영, '중상 보고' 항목(45행)의 기간이 연 단위
- 섹션 9. 책임 경계 — 실외 인증이 요구하는 관제장치 기능(실시간 상태·원격 정지)과 인증 정보의 관제장치 모델 단위 미반영
- 섹션 11. 열린 질문(분리 2026-09-30-area50-s11) — oq-186·oq-230 이 별표 원문 미확인 상태, oq-384(ISO 3691-4 차기판 단계 충돌) 미해소
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 고시 근거(제2025-021호), 16/8 항목 경위, EU 게재 서술 강등, ref-789 제목, 'KS B ISO 10218-2 2017 확인'

## 조사 질문

1. 어떤 안전 표준과 인증을 따라야 하며, 사고가 나면 원인을 어떻게 밝힐 것인가? [분류원문]
2. oq-186·oq-230 실외이동로봇 운행안전인증 심사항목이 16개에서 8개로 바뀐 개정의 시점·근거 고시와 항목 대응은 무엇인가? (섹션 5·7·11 겨냥)
3. EN ISO 10218-1/-2:2025 의 EU 조화 게재는 어떤 법령에 대한 것이며 언제까지 효력이 있는가, ISO 3691-4 차기판·국내 KS 부합판의 현재 상태는 무엇인가(oq-384, oq-251)? (섹션 4·7 겨냥)
4. oq-252 사고 조사에 필요한 기록 항목·형식·보존을 정한 공개 규약(EBB 초안, EU 기계 규정, rosbag2·MCAP)은 무엇을 정하고 무엇을 비워 두는가? (섹션 6·7 겨냥)
5. 로봇 사고 통계(OSHA SIR, Ohio 보상 청구, 국내 공식 재해사례)는 어떤 관할·기간·집계 단위·한계를 가지는가? (섹션 5·8 겨냥)
6. 사고 원인을 개인 과실이 아니라 제어 구조·조직 정책까지 조사하는 방법(CAST·역할극 증언)은 무엇을 요구하고 어떤 한계가 있는가? (섹션 6·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 위원회 시행결정 (EU) 2026/2015(2026-09-04 채택, 2026-09-07 관보 L 시리즈 게재)의 부속서는 시행결정 (EU) 2023/1586 부속서 I 에 EN ISO 10218-1:2025(223a)와 EN ISO 10218-2:2025(224a)의 참조를 추가한다. | ref-1496 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [사실] | 이 결정이 참조를 추가한 목록(2023/1586 부속서 I)은 기계류 지침 2006/42/EC 에 대한 적합성 추정을 주는 조화 표준 목록이며, 같은 결정 제2조는 2023/1586 을 2027-01-20 부로 폐지한다. 전문 (14)는 그 이유를 지침 2006/42/EC 가 규정 (EU) 2023/1230 으로 같은 날 폐지되기 때문이라고 적는다. | ref-1496 | 아니오 | medium | 2026-10-11 | — | — |
| f3 | [추정] | 기존 위키(2026-09-30-area50-s7.md 42행)의 'PL d·범주 3 일률 요구 대신 표의 기본 성능 수준 또는 위험성평가 근거 선택 허용, 운전 정지용 정상 정지 기능 신설' 서술은 컨설팅사 IBF Solutions 해설만 근거로 [사실]로 실려 있다. 관보 원문으로 확인되는 것은 참조 게재 사실·날짜·법적 기반뿐이므로 이 서술은 [추정]·벤더 해설로 낮추는 것이 맞다. | ref-1116, ref-1496 | 아니오 | low | 2026-10-11 | — | 벤더 주장 |
| f4 | [추정] | ANSI/A3 R15.08-3-2026(Part 3: Use of IMR Applications)은 A3 판매 페이지 기준 2026-04-23 발행으로 표시되며, 이 사실은 위키에 이미 있다. 이 영역 7절 표에는 R15.08-2 만 있어 Part 3 행을 더할 근거로만 쓴다. | ref-1255 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f5 | [사실] | ISO 3691-4 차기판 프로젝트는 ISO 위원회 페이지에서 'ISO/DIS 3691-4, Edition 3, Under development'이며 단계 40.60(투표 종료, 2026-09-10)으로 표시되고 ISO 3691-4:2023 을 대체할 예정이다. 발행된 개정판이 아니다. | ref-789 | 아니오 | medium | 2026-10-11 | — | — |
| f6 | [사실] | 국가표준 목록에서 KS B ISO 10218-1(산업용 로봇의 안전 요구사항 제1부: 로봇)의 대응 국제표준은 ISO 10218-1:2011(IDT, 일치)이고 최종개정확인일은 2021-11-26 이다(제정 2008-01-17). | ref-1497 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | 같은 목록에서 KS B ISO 10218-2(제2부: 로봇 시스템 및 통합)의 대응 국제표준은 ISO 10218-2:2011(IDT)이고 최종개정확인일은 2022-10-12(고시 제2022-0433호)다. 위키의 'KS B ISO 10218-2 2017 확인' 표현은 낡았다. | ref-211 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | EU 기계 규정 (EU) 2023/1230 부속서 III 1.2.1(f)는 제어 시스템을, 개입과 관련해 생성된 데이터와 출시·사용 개시 뒤 업로드한 안전 소프트웨어 판의 추적 기록이 업로드 뒤 5년간 활성화되도록 설계·제작해야 한다고 정한다. 목적은 관할 국가기관의 이유 있는 요청에 따른 적합성 입증에 한정된다. | ref-555 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | 같은 절 둘째 목록 (b)는 행동·논리가 전부 또는 일부 자체 진화하며 여러 자율성 수준으로 작동하도록 설계된 기계의 제어 시스템에 대해, 안전 기능을 보장하는 소프트웨어 기반 안전 시스템의 안전 관련 의사결정 데이터를 기록하고 수집 뒤 1년간 보존하도록 정한다. | ref-555 | 아니오 | medium | 2026-10-11 | — | — |
| f10 | [사실] | UL 3100(Automated Mobile Platforms, AMPs) 공식 목록은 제1판의 최초 발행일을 2021-05-26, 최근 개정일과 ANSI 승인일을 2026-06-10 으로 표시한다. | ref-1498 | 아니오 | medium | 2026-10-11 | — | — |
| f11 | [사실] | UL 3100 의 공개 적용 범위 1.4 는 산업용 로봇 자체의 요구사항은 포함하지 않으며(UL 1740·CSA Z434 가 다룸), 그 표준에 맞는 로봇 매니퓰레이터는 통합 시스템의 탑재물로 쓸 수 있다고 적는다. | ref-1498 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [추정] | UL Solutions 는 2026-03-11 보도자료에서 Simbe 의 매장용 자율이동로봇 Tally 가 UL 3300(SCIEE 로봇 표준) 인증을 받았으며, 로봇과 충전 도크가 화재·감전 위험과 안전한 자율 이동 시험을 거쳤다고 발표했다. | ref-1499 | 아니오 | low | 2026-10-11 | — | 벤더 주장 |
| f13 | [사실] | 정부의 2025-11-27 보도참고자료(신산업 규제합리화 1호 로드맵, AI 분야)는 실외이동로봇 운행안전인증의 심사 평가항목을 16개에서 8개로 통폐합하고 심사기간을 60일에서 30일로 줄였다고('25.11 시행) 적는다. | ref-1504 | 아니오 | medium | 2026-10-11 | — | — |
| f14 | [사실] | 산업통상부 고시 제2025-021호(실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부개정)는 2025-11-24 발령되었고 부칙에서 '발령한 날부터 시행'하므로 2025-11-24 부터 시행이다. 현행 절차·기준의 근거는 제2023-211호가 아니라 이 개정 고시다. | ref-1505 | 아니오 | medium | 2026-10-11 | — | — |
| f15 | [추정] | 고시 제2023-211호는 2023-11-17 발령(제정)되었다. 시행일은 원 고시 첨부 부칙이 '2023년 11월 17일부터 시행', 제2025-021호 첨부 본문에 실린 구 부칙(<제2023-211호, 2023.11.17.>)이 '2023년 11월 21일부터 시행'으로 서로 달라 확정하지 않는다. | ref-1118, ref-1505 | 아니오 | low | 2026-10-11 | — | — |
| f16 | [사실] | 고시 제2025-021호 제9조①은 운행안전인증기관이 인증신청서를 접수한 날부터 30일 이내에 심사 결과를 통보하도록 정한다. 제2023-211호 제9조①에는 이 기한이 없고 심사 종료 뒤 통보만 정했다. | ref-1505, ref-1118 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | 고시 제2023-211호 별표 3(운행안전인증 기준)은 질량 및 폭 제한, 운행 속도, 겉모양, 동적 안정성, 비상정지, 운행구역 준수, 속도 제어, 장애물 감지, 알림음, 등화장치, 방수 성능, 물리적 보안, 횡단보도 통행, 관제장치, 통신장애 대응, 원격조작의 16개 항목을 둔다. | ref-1118 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [사실] | 현행 고시 제2025-021호 별표 3 은 규격 및 운행속도, 겉모양, 동적 특성, 주변 인식, 비상정지, 방수 성능, 횡단보도 통행, 관제장치의 8개 항목을 두며, 한국로봇산업진흥원 안내의 8개 심사항목과 이름이 같다. | ref-1505, ref-980 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | 두 별표를 조문으로 대조하면 구 질량·폭 제한과 운행 속도는 '규격 및 운행속도'로, 동적 안정성(5° 경사·30 mm 턱)과 속도 제어(±10 %)는 '동적 특성'으로, 운행구역 준수와 장애물 감지는 '주변 인식'으로, 관제장치와 원격조작(원격 정지·영상 확인 원격 수동조작)은 '관제장치'로 합쳐졌다. 알림음(55~73 dB(A)), 등화장치(표면 60℃ 이하), 물리적 보안(통신포트·저장장치 단자 보호)은 새 별표에 없고, 통신장애 대응(운행계획서 시나리오)은 횡단보도 통행 중 통신 단절 시 정차 조항으로만 남았다. 빠진 항목이 다른 규정으로 옮겨졌는지는 확인하지 못했다. | ref-1118, ref-1505 | 아니오 | medium | 2026-10-11 | — | — |
| f20 | [사실] | 본 페이지 5절이 '2023-07 행정예고안 보도 기준, 확정 고시 별표 원문 미확인'으로 둔 기준 예시(질량별 속도 230 kg 초과 5 km/h·100 kg 초과 10 km/h, 폭 800 mm·보도 2,500 mm 이상이면 1,200 mm, 5° 경사, 알림음 55~73 dB, 등화장치 60℃, IPX4)는 확정 고시 제2023-211호 별표 3 에 그대로 있다. 현행 제2025-021호에는 질량·폭·속도·5° 경사·IPX4 는 남고 알림음·등화장치 기준은 없다. | ref-1118, ref-1505 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [사실] | 현행 별표 3 의 관제장치 항목은 관제장치가 운용 중인 모든 로봇을 식별하고, 모든 로봇의 위치·속력, 주행가능 거리 또는 배터리 잔량, 로봇–관제장치 통신 신호 감도, 상태(주행·대기·비상정지·오류)를 실시간으로 확인할 수 있어야 하며, 통행 불가 시 관제장치 알림과 관리자 조치, 원격 정지 수단, 영상장치로 주변을 확인하는 원격 수동조작을 요구한다. | ref-1505 | 아니오 | medium | 2026-10-11 | 실외 / 수행 자원 | — |
| f22 | [사실] | 고시 제2025-021호 제10조②는 인증기관이 인증번호, 회사명, 실외이동로봇 제품명·모델명과 함께 관제장치 제품명·모델명, 소재지 등의 정보를 보관하도록 정해, 인증 정보가 로봇 모델과 관제장치 모델의 조합으로 관리됨을 보여 준다. | ref-1505 | 아니오 | medium | 2026-10-11 | 실외 / 수행 자원 | — |
| f23 | [사실] | 안전보건공단 산업안전보건인증원의 자율안전확인 대상 안내는 산업용 로봇을 직교좌표로봇을 포함해 3축 이상의 매니퓰레이터(액추에이터·교시 펜던트·제어기·통신 인터페이스 포함)를 갖추고 전용 제어기로 프로그램·자동제어가 가능한 고정식 로봇으로 정의한다. | ref-1500 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [사실] | Sanders 외(2024)가 분석한 OSHA 중상 보고(SIR)의 기간은 2015-01-01 부터 2022-04-30 까지다. | ref-1122 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | 같은 연구는 SIR 이 연방 OSHA 관할 사업장의 보고만 담고 자체 주 계획(State Plan)을 운영하는 22개 주의 사업장은 포함하지 않는다고 밝힌다. | ref-1122 | 아니오 | medium | 2026-10-11 | — | — |
| f26 | [사실] | 같은 연구에서 분석한 사고 서술의 단어 수 중앙값은 36 단어였다. | ref-1122 | 아니오 | medium | 2026-10-11 | — | — |
| f27 | [사실] | Suresh 외(American Journal of Industrial Medicine 69(5), 2026)는 Ohio 산재보상국(OHBWC) 자료에서 2001~2020년 로봇 관련 산재보상 청구 1,076건을 키워드 검색으로 찾았다. | ref-1501 | 아니오 | medium | 2026-10-11 | — | — |
| f28 | [사실] | 초록 기준으로 이 청구의 85% 가 의료비만 청구(의료 처치만 또는 휴업 7일 이하)였고, 청구의 75.7% 가 공유 작업공간에서 협동 적용 로봇 팔을 다루는 작업과 관련됐다. | ref-1501 | 아니오 | medium | 2026-10-11 | — | — |
| f29 | [사실] | 안전보건공단 공개 재해사례(광주 광산구 사업장)는 로봇 용접기의 용접 팁 교체 작업자가 작동 중인 로봇 팔과 지그 사이에 흉부가 끼어 숨진 사고의 원인을 두 가지로 든다: 일시중지(muting) 기능 사용으로 감응식 방호장치가 작동하지 않은 것, 로봇 운전을 정지하지 않고 안전 조치가 없는 재료 투입구로 셀에 들어간 것. | ref-1502 | 아니오 | medium | 2026-10-11 | 제조 공장 / 예외·성과 | — |
| f30 | [사실] | 같은 사례의 재발방지대책은 출입 시 감응식 방호장치가 작동하도록 하고 muting 사용 시 다른 수단으로 안전이 유지되도록 관리하며, 수리·점검 같은 비정형 작업은 로봇 운전을 정지한 뒤 출입문으로 들어가 하라고 제시한다. | ref-1502 | 아니오 | medium | 2026-10-11 | 제조 공장 / 제약 | — |
| f31 | [사실] | Leveson 의 MIT OCW 강의 자료(16.863J System Safety, 2016년 봄 학기) 'CAST 분석'은 SO2 탱크 넘침 사례에서 안전 핵심 장비가 오랫동안 작동하지 않은 이유, 그런 상태로 공장을 운전하는 정책과 위험성평가 여부, 점검·정비 정책을 조사 질문으로 던진다. | ref-1506 | 아니오 | medium | 2026-10-11 | — | — |
| f32 | [사실] | 같은 강의는 운전원 수준 분석 항목으로 맥락·시스템 요인과 정신 모형의 결함을 두고, 사후 판단 편향(hindsight bias)을 경계한다. | ref-1506 | 아니오 | medium | 2026-10-11 | — | — |
| f33 | [사실] | Webb 외(2021)는 2020년 11월 같은 연구자 한 명이 Zoom 으로 가상 목격자 증언(VWT) 역할극 면담 22회를 진행했으며, 실제 사고가 아닌 삽화 시나리오를 보여 주는 방식이었다. | ref-1121 | 아니오 | medium | 2026-10-11 | — | — |
| f34 | [사실] | 연구진은 정지 이미지를 써서 시나리오의 동적인 부분을 효과적으로 전달하지 못했다고 한계를 밝혔다(예: 로봇이 거주자 다리와 부딪혔을 가능성을 시사하는 움직임). | ref-1121 | 아니오 | medium | 2026-10-11 | — | — |
| f35 | [사실] | 윤리적 블랙박스 초안(ICRES 2022 게재본 부록, RFC Draft 0.1)은 날짜 필드 ebbD 의 길이를 표에서는 10자, MD 기록 주석 2 에서는 12 ASCII 문자로 다르게 적고, 시각 필드도 표와 주석이 다르다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f36 | [사실] | 같은 초안의 체크섬 표기는 표 2 의 4 문자, 표 3 의 8자리 16진수, 주석 4 의 '64비트 비암호학적 해시(추후 결정)'로 서로 맞지 않는다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f37 | [사실] | 초안은 로봇 결정 코드의 숫자값 정의를 표준 범위 밖으로 두고 로봇 제조사나 운영자에게 맡긴다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [사실] | 초안의 로봇 데이터(RD) 기록은 저장 한도에 이르면 가장 오래된 RD 기록부터 덮어쓰는 순환 구조이며, 고정 보존 기간을 정하지 않는다. | ref-1503 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [사실] | rosbag2 0.35.0 README 의 --repeat-transient-local 옵션은 지정 토픽의 최근 N개(기본 1개) 메시지를 보관했다가 분할로 새 파일이 시작되거나 스냅샷을 쓸 때 앞에 다시 넣는다. | ref-831 | 아니오 | medium | 2026-10-11 | — | — |
| f40 | [사실] | 같은 판의 스냅샷 모드는 메시지를 바로 디스크에 쓰지 않고 --max-cache-size(바이트)와 선택적 --max-cache-duration(초)로 제한한 메모리 순환 버퍼에 두었다가 요청 시(~/snapshot 서비스) 디스크에 저장한다. | ref-831 | 아니오 | medium | 2026-10-11 | — | — |
| f41 | [사실] | rosbag2 의 유실 메시지 통계는 증분 방식이라 유실이 0인 토픽은 이벤트에 들어가지 않고, 내부 카운터는 이벤트를 발행할 때마다 0으로 재설정된다. | ref-831 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [사실] | MCAP 명세는 Message 레코드의 publish_time 을 '발행 시각, 알 수 없으면 log_time 으로 설정해야 한다(must)'고 정한다. 따라서 publish_time 이 log_time 과 같으면 실제 발행 시각인지 대체값인지 포맷만으로 구분되지 않는다. | ref-1096 | 아니오 | medium | 2026-10-11 | — | — |
| f43 | [사실] | MCAP 명세는 Chunk 의 uncompressed_crc 와 여러 레코드의 crc 값이 0 이면 'CRC 검증을 수행하지 않아야 한다(should not)'는 뜻으로 정한다. CRC 는 오류 검출용이며 서명이나 증거 인계를 보장하지 않는다. | ref-1096 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 표준 레지스트리는 발행판(ISO 3691-4:2023)과 개발 중 프로젝트(ISO/DIS 3691-4 제3판), 국내 부합판(KS B ISO 10218-1·-2, ISO 10218:2011 IDT)과 국제 최신판(ISO 10218:2025), EU 조화 게재(지침 2006/42/EC 기반, 2027-01-20 폐지 예정 목록)를 별도 속성으로 두고, 배포 설정에는 현장 승인된 판을 고정해야 한다. | ref-789, ref-1497, ref-211, ref-1496 | 아니오 | low | 2026-10-11 | — | — |
| f45 | [의견] | 실외이동로봇 인증 정보는 고시 번호·시행일(제2025-021호, 2025-11-24)과 별표 판(16항목/8항목)을 함께 기록하고, 구 별표로 받은 인증과 현행 별표 기준을 구분해야 한다. 현행 관제장치 항목의 실시간 상태(위치·속력·배터리·통신 감도·상태)와 원격 정지는 ROP 가 이종 로봇 상태 모델로 받아야 할 최소 항목으로 쓸 수 있다. | ref-1505, ref-1118 | 아니오 | low | 2026-10-11 | 실외 / 수행 자원 | — |
| f46 | [의견] | EU 부속서 III 1.2.1 의 5년·1년 기록 의무는 안전 소프트웨어 개입·판 이력과 자체 진화 제어의 안전 결정 데이터에 한정되므로, ROP 는 인증 증거용 이력과 일반 작업 로그를 나눠 보존 정책을 정하고 플릿 전체 데이터를 일률적으로 5년 또는 1년 보관해야 한다고 해석하지 않는 것이 맞다. | ref-555 | 아니오 | low | 2026-10-11 | — | — |
| f47 | [의견] | 사고 자료 레코드에는 출처별 관할(연방 OSHA 관할만 등), 관측 기간, 집계 단위(보고 건수·부상 수·보상 청구), 중증도 정의, 노출 분모 유무를 필드로 두어 OSHA SIR 과 Ohio 보상 청구 같은 서로 다른 모집단을 합산·비교하지 않게 해야 한다. | ref-1122, ref-1501 | 아니오 | low | 2026-10-11 | — | — |
| f48 | [의견] | EBB 초안을 공통 기록 스키마로 쓰기 전에 날짜·시각·체크섬 표기 충돌을 해소하고, ROP 쪽에서 제조사 원본 결정 코드·공통 사건 유형·코드표 판·시각 기준·사고 시 보존 잠금을 따로 정의해야 한다. 기록기 쪽에서는 사고 트리거 스냅샷, 정적 토픽 재삽입 depth, 유실 이벤트 수신 여부, MCAP publish_time 대체 여부와 원본 해시·추출 이력을 증거 메타데이터로 함께 남겨야 한다. | ref-1503, ref-1120, ref-831, ref-1096 | 아니오 | low | 2026-10-11 | — | — |
| f49 | [의견] | CAST 의 조사 질문을 플릿 사고에 옮기면, 사건 시간선 뒤에 제조사·통합자·현장 운영자·관제자 각각의 제어 책임, 당시 관측 가능했던 정보, 방호장치 우회(muting)와 정비·승인 정책을 따로 조사하고, '교육 부족' 같은 결론을 증거 없이 먼저 정하지 않는 절차가 필요하다. | ref-1506, ref-1502 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1496 | European Commission (Official Journal of the European Union) | Commission Implementing Decision (EU) 2026/2015 of 4 September 2026 amending and repealing Implementing Decision (EU) 2023/1586 as regards harmonised standards for machinery drafted in support of Directive 2006/42/EC | 2026-09-07 | 정부·연구기관 | high | 2026-10-11 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D2015 | 아니오 |
| ref-1497 | 국가기술표준원 (국가표준인증 통합정보시스템) | KS B ISO 10218-1 로봇 및 로봇장치 ─ 산업용 로봇의 안전에 관한 요구사항 ─ 제1부: 로봇 | 2021-11-26 | 표준 | medium | 2026-10-11 | https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSBISO10218-1&menuId=919&reformNo=05&tmprKsNo=KSBISO10218-1&topMenuId=502&upperMenuId=503 | 아니오 |
| ref-1498 | UL Standards & Engagement | UL 3100 Automated Mobile Platforms (AMPs) | 2026-06-10 | 표준 | medium | 2026-10-11 | https://www.shopulstandards.com/ProductDetail.aspx?UniqueKey=39063 | 아니오 |
| ref-1499 | UL Solutions | UL Solutions Grants Its First Global Certification for a Public-Facing Robot to Simbe's Tally Autonomous Mobile Robot | 2026-03-11 | 벤더 문서 | medium | 2026-10-11 | https://www.ul.com/news/ul-solutions-grants-its-first-global-certification-public-facing-robot-simbes-tally-autonomous | 아니오 |
| ref-1500 | 안전보건공단 산업안전보건인증원 | 자율안전확인 대상품 (자율안전확인신고 대상 및 적용범위) | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://miis.kosha.or.kr/oshci/busi/viewMiisJayulMerchandiseInfo.do | 아니오 |
| ref-1501 | Suresh, V., Konda, S., Haney, J. M. 외 (American Journal of Industrial Medicine 69(5)) | Robot-Related Workers' Compensation Claims in Ohio, 2001–2020 | 2026-05 | 논문 | medium | 2026-10-11 | https://stacks.cdc.gov/view/cdc/258698 | 아니오 |
| ref-1502 | 안전보건공단 | 산업용 로봇 팔과 지그 사이에 끼임 (재해사례) | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://oshri.kosha.or.kr/kosha/data/machine.do?articleNo=411924&attachNo=233368&mode=download | 아니오 |
| ref-1503 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (ICRES 2022 Proceedings, CLAWAR) | An Ethical Black Box for Social Robots: a draft Open Standard (ICRES 2022 게재본) | 2022-07 | 논문 | medium | 2026-10-11 | https://doi.org/10.13180/icres.2022.18-19.07.019 | 아니오 |
| ref-1504 | 관계부처 합동 (금융위원회 누리집 게재 보도참고자료) | 규제의 벽은 허물고 AI의 길은 넓힌다 — 신산업 규제합리화 1호 로드맵(AI 분야) 발표 | 2025-11-27 | 정부·연구기관 | high | 2026-10-11 | https://www.fsc.go.kr/no010101/85753 | 아니오 |
| ref-1505 | 산업통상부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 (고시 제2025-021호, 일부개정) | 2025-11-24 | 정부·연구기관 | high | 2026-10-11 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view | 아니오 |
| ref-1506 | Leveson, N. (MIT OpenCourseWare, 16.863J System Safety) | System Safety: CAST Analysis (강의 자료) | 2016 | 정부·연구기관 | medium | 2026-10-11 | https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/7dc4344ef259e4bde4acc1bb2d578a95_MIT16_863JS16_LecNotes3-2.pdf | 아니오 |
| ref-1255 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 2026-04-23 | 표준 | medium | 2026-10-11 | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download | 예 |
| ref-789 | ISO | ISO/DIS 3691-4 (제3판) - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 미확인 | 표준 | medium | 2026-10-11 | https://www.iso.org/standard/88615.html | 아니오 |
| ref-211 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 2022-10-12 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | high | 2026-10-11 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 아니오 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-10-11 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 아니오 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-11 | https://arxiv.org/abs/2205.06564 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | high | 2026-10-11 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 아니오 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/ros2/rosbag2 | 아니오 |
| ref-1096 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://mcap.dev/spec | 아니오 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | high | 2026-10-11 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 아니오 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-11 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/safety-standards-certification-and-incident-investigation.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area50-s4) — '적합성 추정' 항목(41행)을 IBF 해설 대신 관보 원문으로 보강(f1)하고 지침 2006/42/EC 기반 목록이 2027-01-20 폐지됨을 덧붙임(f2). '중상 보고' 항목(45행)의 기간을 2015-01-01~2022-04-30 로(f24), 연방 관할 한정(f25) / 섹션 5 — 실외 사례: 104행 '고시 제2023-211호(2023-11-17)로 정해졌고'를 현행 제2025-021호(2025-11-24 발령·시행, f14)로 정정하고 제2023-211호 시행일은 두 원문이 달라 확정하지 않음(f15 [추정], 독립 검증 보고의 2023-11-21 과도 다름); 100행 제약 칸과 106행 W19 문장('8개와 16가지로 달라 어느 쪽도 고르지 않고')을 '구 고시 별표 3 16개(f17) → 현행 별표 3 8개(f18), 2025-11 통폐합(f13)'으로 정정하고 항목 대응·빠진 항목(알림음·등화장치·물리적 보안, 다른 규정 이동 여부 미확인)을 f19 로; 106행 '확정 고시 별표 원문 미확인' 기준값은 2023-211 별표 3 에 있음과 현행 잔존 여부(f20); 98행 30일 처리기간에 제9조① 근거(f16)·60→30일 경위(f13). 제조 공장: 공식 재해사례(용접 팁 교체 끼임, muting 우회·운전 정지 미실시, f29·f30)를 사례로 추가하되 고성·오뚜기 기사 사건과 연결하지 않음; 의견 f45·f49 / 섹션 6(분리 2026-09-30-area50-s6) — '사고 기록 장치' 소절 45행 '형식과 보존 기간 … 미확인'을 EBB 초안 게재본 내용으로 보강: 날짜·시각 필드 충돌(f35), 체크섬 충돌(f36), 결정 코드 제조사 위임(f37), RD 순환 덮어쓰기·보존 기간 없음(f38). 조직·제어 분석 방법 CAST 소절 추가(f31·f32, 2016 은 강의 학기이며 사고 연도 아님); 의견 f48·f49 / 섹션 7(분리 2026-09-30-area50-s7) — 42행 EN ISO 10218 EU 조화 게재 행: 게재 사실·날짜·법적 기반은 관보 원문(f1·f2)으로, PL d·범주 3 대체·정상 정지 서술은 IBF 단독 근거라 [사실]→[추정]·벤더 해설로 강등(f3). 45행 실외이동로봇 행 '절차·기준은 고시 제2023-211호(2023-11-17)가 정한다'→ 제2023-211호를 제2025-021호가 2025-11-24 개정·시행(f14), 심사항목 구판 16·현행 8(f17·f18). R15.08-3 행 추가(f4 [추정], 발행 사실은 기존 내용 확인 — safety/index.md 53행, 재추가 아님). ISO/DIS 3691-4 제3판 40.60(2026-09-10) 행(f5) — ref-789 제목을 'ISO/DIS 3691-4 (제3판)'으로 갱신. KS 부합판 ISO 10218-1/-2:2011 IDT(f6·f7). EU 기계 규정 부속서 III 1.2.1(f) 5년 추적 기록(f8: 영역 52 의 IES 해설 기반 문장 2026-09-30-area52-s3.md 43행을 1차 원문으로 보강)과 자체 진화 제어 1년 보존(f9). UL 3100 판·범위(f10·f11), UL 3300 Tally 인증은 벤더 주장(f12 [추정]). 자율안전확인 대상 정의(f23). rosbag2 0.35.0 repeat-transient-local·스냅샷·유실 통계(f39~f41, 기능 일반은 ref-831 기존 내용), MCAP publish_time 대체 규칙·CRC 0(f42·f43, log_time/publish_time 구분 자체는 design-and-simulation/index.md 100행 기존 내용); 의견 f44·f46 기존 내용 확인(새로 넣지 않음): EU 기계 규정 일반 적용일 2027-01-20(2026-09-25-area26-s7.md 55행, 2026-09-30-area52-s3.md 43행), 제54조 (b) 제50조(1) 2026-10-20(safety-and-risk-management.md 142행, 2026-10-11 게시), R15.08-3 발행일(safety/index.md 53행) / 섹션 8(분리 2026-09-30-area50-s8) — Sanders 외 항목(42행)에 기간(f24)·연방 관할 한정(f25)·서술 단어 수 중앙값 36(f26). Suresh 외 2026 AJIM 69(5):345–357 추가(f27·f28: 85% 는 초록 수치, n=917·발생률 미산출 서술은 미확인이라 쓰지 않음). Webb 외 항목(41행)에 2020-11 Zoom 22회(f33)와 정지 이미지 한계(f34); 의견 f47 / 섹션 9 — 업종별 조건 행: 실외 인증의 관제장치 요구(실시간 상태·원격 정지, f21)와 인증 정보의 관제장치 모델 단위(f22)를 인증 상태 등록 근거로; 의견 f45 / 섹션 11(분리 2026-09-30-area50-s11) — 해결 제안: oq-230(구판 16·현행 8 이 모두 항목 단위이며 세부 목록 확인, f17·f18·f19), oq-384(ISO/DIS 3691-4 제3판 40.60, f5). 부분 답: oq-186(시점·근거 고시 f13·f14, 경사로→동적 특성, 알림음·등화장치는 새 별표에 없음 f19; 다른 규정 이동 여부가 남아 열린 채 둠), oq-251·oq-123(KS 는 여전히 2011 IDT, f6·f7), oq-252(f8·f9·f35~f43), oq-333(관제장치 항목에 기록 보관 요구 문구 없음, f21), oq-187(관련 근거 f22). 답하지 못함: oq-170, oq-253, oq-254, oq-265. 메모의 '새 질문' 4건은 문구 대조로 기존 oq-251~oq-254 와 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 중 '별표 구·신 대응표'는 f19 로 대부분 답해져 만들지 않고 남은 부분은 oq-186 에 둠; EBB·스냅샷 검증·MCAP 증거 표시 3건과 제2023-211호 시행일 출처 충돌, 2023/1230 조화 게재 시점 질문을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/topics/2026/2026-09-26-area25-s7.md 45행 'KS B ISO 10218-2 … 2017 확인' → 2022-10-12 확인(f7)과 ref-814 제목, docs/categories/safety/index.md 177행(IBF 단독 근거 [사실]·'산업통상자원부 고시(2023-11-17)로 정해졌다')을 f1·f2·f14 로 정리, 2026-09-30-area52-s3.md 43행에 f8 1차 근거 연결. 다음 실행 후보: 66. 실외(f17~f22), 59. 법·규제·보험·라이선스(f2·f8·f9·f14), 37. 관제 화면·실행 기록(f21·f39~f43) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 윤리적 블랙박스 초안의 날짜·시각·체크섬 표기 충돌을 해소한 후속 판이 있는가, 서로 다른 제조사의 로봇 결정 코드를 공통 사건 유형으로 옮기는 공개 매핑이 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 37. 관제 화면·실행 기록 | 근거: f35 | 종류: 일반
- rosbag2 스냅샷·repeat-transient-local·유실 통계를 쓴 사고 전후 기록을 현장 설정(스냅샷 트리거 지연, 전원 상실, 정적 토픽 depth, 유실 이벤트 누락)에서 시험해 보존 길이와 누락을 검증한 사례가 있는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 43. 데이터·관측성·배포 | 근거: f40 | 종류: 일반
- MCAP 의 publish_time 이 log_time 으로 대체된 경우와 원본 추출·해시·서명 이력을 사고 증거 묶음에 어떻게 표시하고 검증할 것인가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 38. 모니터링·이상 탐지·원인 분석 | 근거: f42 | 종류: 일반
- 출처 충돌: 실외이동로봇 운행안전인증 고시 제2023-211호의 시행일은 원 고시 첨부 부칙(2023-11-17)과 제2025-021호 첨부 본문에 실린 구 부칙(2023-11-21) 가운데 어느 쪽인가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 66. 실외 | 근거: f15 | 종류: 출처 충돌
- EN ISO 10218-1/-2:2025 참조는 기계 규정 (EU) 2023/1230 의 조화 표준으로 언제 게재되며, 지침 2006/42/EC 기반 목록(시행결정 2023/1586)이 2027-01-20 폐지된 뒤 적합성 추정은 어떻게 이어지는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스 | 근거: f2 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- oq-230
- oq-384

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 11건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-06/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f4: A3 R15.08-3 판매 페이지 재열람 실패(Cloudflare) — 발행일은 기존 ref-1255(2026-10-09 열람) 기준이라 [추정]
    - f15: 고시 제2023-211호 시행일 — 원 고시 첨부 HWP 부칙 '2023년 11월 17일부터 시행'과 제2025-021호 첨부 본문의 구 부칙 '2023년 11월 21일부터 시행'이 충돌. 독립 검증 보고(2023-11-21)와도 달라 확정하지 않음
    - f19: 2023-211 별표 3 의 알림음·등화장치·물리적 보안과 통신장애 대응(운행계획서 시나리오)이 세부운영지침 등 다른 규정으로 옮겨졌는지 미확인
    - f13: 메모가 든 kmcc.go.kr 로드맵 파일(인쇄 p.50)은 열지 못해 같은 날 정부 보도참고(fsc.go.kr, ref-1504)로 출처를 바꾸고 쪽 번호를 삭제
    - f27·f28: Suresh 외는 CDC Stacks 초록·Crossref 서지만 확인(본문 PDF 열람 실패). 메모의 'n = 917(85.2%)'·'발생률 미산출(§4.1)'은 미확인이라 쓰지 않음
    - 메모 F19(OSHA SIR 대시보드는 업무상 사망 제외)는 osha.gov 403 으로 확인하지 못해 넣지 않음(연방 관할 한정은 Sanders 원고로 f25)
    - f10·f11: UL 3100 은 공식 목록의 판·범위만 확인, 2026 개정 조항 전체·시험 수치 미확인. f12: Tally UL 3300 인증서·시험보고서 미확인(벤더 주장)
    - f3: ISO 10218:2025 원문 미열람이라 IBF 해설의 PL d·범주 3·정상 정지 서술이 틀렸다고 판단한 것이 아니라 근거 수준만 낮춤
    - f39~f43: rosbag2 0.35.0 태그 대상 커밋 날짜와 MCAP 고정 커밋(f7069e6) 날짜는 확인하지 못해 published null. 현장 무유실 성능은 시험하지 않음
    - f6·f7: KS 목록에서 ISO 10218:2025 부합 KS 를 찾지 못했으나 후속 고시 전수 부재를 증명한 것은 아님(oq-251 부분 답)
    - oq-170(ISO 3691-4:2023 원문 플릿 정보 요구), oq-253(국내 고정형·이동형 분리 재해 통계), oq-254(ISO/FDIS 13482 플릿 요구), oq-265(R15.08-3 사용자 의무)는 이번 메모가 답하지 못함
    - 메모가 2026-10-11 기준 위키 진단에 쓴 고정 커밋과 배포 페이지의 동일성, 오뚜기·고성 사고의 공식 최종 원인, 국내 실외운행인증 최신 누계는 확인하지 못함
- 범위 경계 위반 의심:
    - f8·f9·f2: EU 기계 규정·조화 표준의 법적 효력 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 개별 제품의 적용 여부는 판단하지 않음
    - f39~f43: rosbag2·MCAP 기록 기능은 37. 관제 화면·실행 기록, 43. 데이터·관측성·배포와 겹치며, 이 영역에는 사고 조사 증거 보존 관점으로만 씀
    - f17~f22: 실외이동로봇 인증 기준은 66. 실외와 겹치며, 이 영역에는 인증 근거·항목 변화와 ROP 가 받는 관제장치 요구로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 11건/15(ref-1496~ref-1506, 예약 구간 ref-1496~ref-1525 안), 재사용 12건(ref-1255·ref-789·ref-211·ref-555·ref-1122·ref-1120·ref-1121·ref-831·ref-1096·ref-1118·ref-1116·ref-980). 출처 매핑(검증 결과 기준): 메모 n1→ref-1496, n2→ref-1255(미열람), n3→ref-1497, n4→ref-211(standard.go.kr 상세로 열람; ref-814 는 '2017 확인' 제목이라 쓰지 않음), n5→ref-789(제목 ISO/DIS 3691-4 (제3판)으로 갱신), n6→ref-555(2026-07-27 통합본), n7→ref-1498, n8→ref-1499(벤더 문서), n9→ref-1500, n10→ref-1122(White Rose 원고), n11→ref-1501(초록만), n12(OSHA SIR 페이지)는 403 이라 출처에서 뺌, n13→ref-1502, n14→ref-1503(ICRES 게재본, DOI 10.13180/icres.2022.18-19.07.019; arXiv 판 ref-1120 은 미재열람), n15→ref-1121, n16→ref-831(0.35.0 태그 raw), n17→ref-1096(고정 커밋 raw), n18→ref-1504(kmcc.go.kr 대신 fsc.go.kr 보도참고 85753), n19→ref-1505(첨부 본문·별표 3 열람), n20→ref-1506. 추가 재사용: ref-1118(2023-211 첨부 HWP 별표 3·부칙), ref-1116(강등 대상 해설, 미재열람), ref-980(진흥원 8개 항목 재열람). fetched: false 는 ref-1255·ref-1120·ref-1116. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: 고시·진흥원·로드맵은 정부 계열, EBB·Webb 은 RoboTIPS 계열) — 신뢰도 medium 이하. 중복 제거: 메모 F07(일반 적용일)·F08(제50조(1) 2026-10-20, 2026-10-11 게시된 safety-and-risk-management.md 142행)·F03(R15.08-3 발행일)은 기존 위키에 있어 rationale 에 위치만 적고 F03 만 7절 행 근거로 [추정] f4 에 남김. 메모 F19·F22 는 확인 불가로 넣지 않음. 검증 반영: F13 출처 교체·쪽 번호 삭제, F15 시행일 2025-11-24·고시 번호 제2025-021호, 별표 3 원문(구 16·신 8)으로 W19·W82 정정, F02 에 2023/1586 2027-01-20 폐지 보완, W78 강등(f3), F04 로 oq-384 해소·ref-789 제목 갱신, F17 행 번호 137–138, F23 원인 2개·장소, F25 '2016'=강의 학기, F37 should 강도, F21 은 초록 85% 만, X01 벤더 주장 [추정]. 검증 보고와 다르게 둔 것: 제2023-211호 시행일(검증 보고 2023-11-21)은 원 고시 첨부 부칙(2023-11-17)과 충돌해 f15 [추정]과 출처 충돌 질문으로 남김. 열린 질문: 해결 제안 oq-230·oq-384, 부분 답 oq-186·oq-251·oq-123·oq-252·oq-333·oq-187. 메모의 새 질문 4건은 기존 oq-251~oq-254 와 같아 새로 만들지 않음. 새 질문 5건. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-23/research.md

```markdown
# 리서치 브리프 2026-09-30-23

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-23 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 59. 법·규제·보험·라이선스 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 운행안전인증, 운용자, 책임보험·공제, 제조물(소프트웨어 포함 여부), 사이버복원력법 보고 의무, SBOM·SPDX, 패키지 라이선스 선언 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 실외(한국 보도 통행 로봇, 미국 주법 개인 배송 장치)·산업 사업장(산업용 로봇 안전검사) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 인증·보험 조건의 운영 제약 반영, 사고·취약점 보고 체계, 라이선스 선언·SBOM 관리 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 지능형로봇법·도로교통법, 산업안전보건법 안전검사, EU 기계류 규정, EU 제조물책임지침, 한국 제조물책임법, 인공지능 기본법, EU 사이버복원력법, 개인정보보호법 제25조의2, ROS 2 REP 2004, SPDX(ISO/IEC 5962) 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-143, oq-173, oq-186, oq-187, oq-231, oq-239, oq-249, oq-250, oq-262 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? [분류원문]
2. 실외에서 로봇을 운행할 때 한국(지능형로봇법·도로교통법의 운행안전인증·운용자 의무·보험)과 해외(미국 주법의 개인 배송 장치)는 무엇을 요구하며, 운행안전인증의 심사항목과 인증 대상은 어떻게 정해져 있는가? (섹션 5·7 겨냥, oq-186·oq-187 관련, 한국 자료 우선)
3. 로봇 사고의 책임을 정하는 제조물 책임 법제는 소프트웨어·AI를 어떻게 다루는가(EU 개정 제조물책임지침, 한국 제조물책임법)? (섹션 4·6·7 겨냥)
4. AI 규제와 사이버보안 규제(한국 인공지능 기본법, EU 사이버복원력법)는 로봇 운영 사업자에게 어떤 의무와 시행 일정을 두는가? (섹션 7 겨냥, oq-143 관련)
5. 산업 사업장에서 로봇을 쓸 때 적용되는 기계·안전 규제(산업안전보건법 안전검사, EU 기계류 규정)는 무엇인가? (섹션 5·7 겨냥)
6. 오픈소스·SDK·3D 자산의 라이선스를 지키기 위한 선언·목록화 수단(ROS 2 패키지 라이선스 규칙, SPDX·SBOM, 시뮬레이션 모델 데이터베이스의 라이선스 표기)은 무엇인가? (섹션 6·7 겨냥)
7. 법·규제·보험·라이선스에서 ROP가 직접 맡을 것과 제조사·운영자·보험사·법무에 맡길 것의 경계는 어디이며 어느 영역(개인정보 법 포함, oq-262 관련)과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | 한국에서는 개정 지능형로봇법과 도로교통법이 2023-11-17부터 시행되어, 운행안전인증을 받은 질량 500kg 이하·최고속도 15km/h 이하의 실외이동로봇이 보행자 지위로 보도를 통행할 수 있게 되었다. | ref-991, ref-980 | 예 | high | 2023-11-16 | 실외 / 제약 | — |
| f2 | [사실] | 개정 도로교통법은 실외이동로봇을 조작·관리하는 운용자에게 정확한 조작과 안전한 운용 의무를 두고, 로봇도 신호위반·무단횡단 금지 같은 보행자 교통규칙을 지키게 하며, 안전운용의무 위반에는 범칙금(3만원)을 부과할 수 있게 했다. | ref-991 | 아니오 | medium | 2023-11-16 | 실외 / 수행 자원 | — |
| f3 | [사실] | 한국에서 운행안전인증을 받은 실외이동로봇을 보도에서 운영하는 자는 인적·물적 손해 배상을 위한 보험 또는 공제에 가입해야 하며, 정부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정했다. | ref-991, ref-1240 | 예 | medium | 2023-11-16 | 실외 / 제약 | — |
| f4 | [사실] | 실외 사례(한국): 한국로봇산업협회는 2024-02 실외이동로봇 손해배상책임 단체보험을 내놓아 로봇 1대당 약 500만원 수준이던 보험료를 30만원대로 낮췄다고 밝혔고, 첫 가입 기업은 뉴빌리티·로보티즈였다. | ref-1240 | 아니오 | low | 2024-02-08 | 실외 / 예외·성과 | — |
| f5 | [사실] | 한국로봇산업진흥원 안내에 따르면 실외이동로봇 운행안전인증은 지능형로봇법 제40조의2에 근거하며, 인증 대상은 실외이동로봇과 그 운행에 필요한 관제장치 조합의 일체이고, 현재 심사항목은 규격 및 운행속도·겉모양·동적 특성·주변 인식·비상정지·방수 성능·횡단보도 통행·관제장치의 8개다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 수행 자원 | — |
| f6 | [사실] | 2023-07 한국로봇산업진흥원이 행정예고한 실외이동로봇 운행 안전기준은 16가지 항목으로, 질량별 속도 제한, 폭 80cm(보도 폭 250cm 이상이면 120cm), 5도 경사로 안정성, 비상정지, 장애물 회피, 횡단보도 신호 준수, 알림음 55~73dB, 등화장치 온도 60도 이하, 방수 IPX4 이상 등을 담았다. | ref-992 | 아니오 | low | 2023-07-28 | 실외 / 제약 | — |
| f7 | [추정] | f5와 f6을 비교하면 실외이동로봇 운행안전인증의 심사 체계가 제정 당시 16가지 안전기준에서 현재 8개 심사항목으로 재편된 것으로 보이나, 개정 시점·근거 고시와 알림음·등화장치·경사로 같은 기존 기준이 어느 항목에 흡수됐는지는 확인하지 못했다. | ref-980, ref-992 | 아니오 | low | 2026-09-30 | 실외 / 제약 | — |
| f8 | [사실] | 실외 사례(미국): 버지니아주법 §46.2-908.1:1은 개인 배송 장치(PDD)가 보도·횡단보도에서 시속 10마일 이하로 운행하고 운영자를 식별하는 표시를 달게 하며, 운영자에게 장치 운행으로 생긴 손해에 대해 최소 10만 달러의 일반배상책임 보험을 유지하게 한다. | ref-1248 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | — |
| f9 | [사실] | EU 개정 제조물책임지침(Directive (EU) 2024/2853)은 2026-12-09 이후 시장에 출시되거나 사용이 개시된 제품에 적용되며, 독립형 소프트웨어·디지털 제조 파일·통합 디지털 요소를 제품에 포함하고, 출시 뒤 제품을 실질적으로 변경한 자를 제조자로 볼 수 있게 한다. | ref-1235 | 아니오 | medium | 2026-03-23 | 예외·성과 | — |
| f10 | [사실] | 같은 지침에서는 결함 있는 소프트웨어나 필요한 보안 업데이트 미제공도 책임 원인이 될 수 있고, 청구인이 그럴듯한 청구를 하면 피고에게 증거 공개를 명할 수 있으며, 공개 의무 불이행 등의 경우 결함이 추정된다. | ref-1235 | 아니오 | medium | 2026-03-23 | 예외·성과 | — |
| f11 | [사실] | 한국 제조물책임법은 제조물을 제조되거나 가공된 동산으로 정의해 소프트웨어를 명시적으로 포함하지 않으므로, 사람의 개입 없이 동작한 자율 시스템 사고에서 소프트웨어 개발자가 제조물 책임을 지는지가 쟁점으로 남아 있다. | ref-1243 | 아니오 | medium | 2024-07 | 예외·성과 | — |
| f12 | [사실] | EU 기계류 규정(Regulation (EU) 2023/1230)은 2027-01-20부터 적용되며, 출시된 기계에 실질적 변경을 한 자를 제조자로 보아 제조자 의무를 지게 한다. | ref-1212, ref-555 | 아니오 | medium | 2023-06-14 | 제약 | 원문 미열람 |
| f13 | [사실] | 한국 인공지능 기본법은 2026-01-22 시행되었고, 정부는 최종 의사결정 권한을 사람이 가지는 경우 고영향 인공지능 분류에서 제외된다고 설명하며, 과태료 등 규제를 최소 1년 이상 유예하고 지원데스크를 운영한다고 밝혔다. | ref-1245 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f14 | [사실] | EU 사이버복원력법(CRA)에 따라 2026-09-11부터 디지털 요소 제품의 제조자는 실제 악용되는 취약점과 중대한 보안 사고를 ENISA 단일 보고 플랫폼을 통해 24시간 안에 조기 경보, 72시간 안에 통지, 이후 최종 보고(취약점은 수정 조치 후 14일, 중대 사고는 1개월)해야 한다. | ref-1236 | 아니오 | medium | 2026-09-11 | 예외·성과 | — |
| f15 | [사실] | 한국 개인정보보호법 제25조의2는 착용형·휴대형·부착·거치형 이동형 영상정보처리기기로 공개된 장소에서 사람을 촬영할 때 불빛·소리·안내판·안내방송 등으로 촬영 사실을 표시하게 하고, 표시했는데 거부 의사가 없는 경우 등에 한해 촬영을 허용한다. | ref-1244 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f16 | [사실] | 고용노동부는 2017-10-29부터 산업용 로봇과 컨베이어를 산업안전보건법상 안전검사 대상에 추가해, 이미 쓰던 설비는 2018-12-31까지 최초 안전검사를 받게 했고, 그 근거로 최근 5년간 산업용 로봇 재해자 221명을 들었다. | ref-1247 | 아니오 | medium | 2017-10-26 | 제약 | — |
| f17 | [사실] | ROS 2 개발자 가이드는 각 패키지에 LICENSE 파일(대개 Apache 2.0, 기존 허용형 라이선스가 있으면 예외)을 두고 모든 소스 파일에 라이선스·저작권 문구를 넣어 자동 린터(ament_copyright)로 검사하게 한다. | ref-1246 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f18 | [사실] | ROS 2 패키지 품질 등급을 정한 REP 2004(2019-12-17 작성, Active)는 품질 수준 1~4 패키지에 선언된 라이선스와 프로젝트 안의 저작권 명시·모든 저자 표기를 요구하고, 수준 5에는 권장만 한다. | ref-1237 | 아니오 | medium | 2019-12-17 | 작업 대상 | — |
| f19 | [사실] | SPDX는 소프트웨어 자재명세서(SBOM)의 출처·라이선스·보안 정보를 교환하는 개방 표준으로 ISO/IEC 5962:2021로 인정되었고, SPDX 라이선스 목록은 라이선스 식별자·예외·라이선스 표현식 문법을 제공한다. | ref-1238 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f20 | [사실] | Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 데이터베이스 안 모델의 라이선스를 지정하고 CC BY 3.0 Unported를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다. | ref-1239 | 아니오 | medium | 2026-09-30 | 작업 대상 | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가)의 답은 현장마다 다르며, 실외는 운행 규정·운행안전인증·운용자 의무·의무 보험(한국 f1~f5, 미국 버지니아 f8), 산업 사업장은 기계 안전 규제(한국 안전검사 f16, EU 기계류 규정 f12), 공통으로 AI·사이버보안·개인정보 규제(f13·f14·f15), 사고 책임 법제(f9~f11), 오픈소스·3D 자산 라이선스(f17~f20)가 겹치는 구조로 보이고, 병원·상업 시설·가정 실내 로봇에 특화된 운행 규정은 이번 조사에서 확인하지 못했다. | ref-991, ref-980, ref-1248, ref-1247, ref-1212, ref-1245, ref-1236, ref-1244, ref-1235, ref-1243, ref-1246, ref-1238, ref-1239 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 59. 법·규제·보험·라이선스에서 ROP가 직접 맡을 범위는 로봇별 인증·보험 상태와 인증 조건(관제장치 조합, 속도·질량·운행 구역)을 등록 정보와 작업·경로 제약으로 반영하고, 사고·취약점 보고와 책임 판단에 필요한 실행 기록을 남기며, 촬영 표시 같은 규제 상태를 운영 조건으로 확인하고, 플랫폼 배포물의 라이선스·SBOM 목록을 관리하는 일로 보인다. | ref-980, ref-991, ref-1236, ref-1244, ref-1238, ref-1246 | 아니오 | low | 2026-09-30 | 제약 | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장의 업종별 조건 경계에 따라 인증 취득과 법적 적합성 판단(제조사·운영자), 보험 계약과 보상(운영자·보험사·협회), 제조물 책임 판정(당사자·법원), 개인정보 처리 적법성 판단(개인정보처리자), 사업장 안전검사(사업주)는 외부가 맡고, ROP는 그 결과를 작업·경로·권한 제약으로 받아 반영하고 근거 기록을 제공하는 쪽인 것으로 보인다. | ref-980, ref-1240, ref-1243, ref-1235, ref-1244, ref-1247 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f24 | [추정] | 이 영역은 인증·안전검사의 50. 안전 표준·인증·사고 조사(f5·f16), 실외 운행 규정의 66. 실외(f1~f8), 촬영 표시의 53. 개인정보·영상 데이터(f15), 실질적 변경·책임 배분의 58. 다사업자 책임·계약·데이터(f9·f12), AI 규제의 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영(f13), 취약점 보고의 52. 통신 보호·위협 관리·감사(f14), 라이선스·SBOM·보안 업데이트의 57. 자산·소프트웨어 수명주기 관리(f10·f17~f19), 인증 정보 등록의 4. 이기종 로봇 등록(f5), 운행 구역 규정의 16. 장소 의미·지도 관리(f6), 3D 자산 라이선스의 36. 가상 시운전·실제 상황 재현(f20), 보험료 부담의 3. 경제성·조달·사업 모델(f4)과 이어진다. | ref-980, ref-1247, ref-991, ref-1244, ref-1235, ref-1212, ref-1245, ref-1236, ref-1246, ref-1237, ref-1238, ref-992, ref-1239, ref-1240 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-991 | 대한민국 정책브리핑 (산업통상자원부·경찰청) | ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 (제목 일부만 확인) | 2023-11-16 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148922726 | 아니오 |
| ref-1235 | Gibson Dunn | EU Product Liability Directive: Responding to Software, AI and Complex Supply Chains | 2026-03-23 | 업계 보고서 | medium | 2026-09-30 | https://www.gibsondunn.com/eu-product-liability-directive-responding-to-software-ai-and-complex-supply-chains/ | 아니오 |
| ref-1236 | European Commission (Shaping Europe's digital future) | Cyber Resilience Act - Reporting obligations | 2026-09-11 | 정부·연구기관 | high | 2026-09-30 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 아니오 |
| ref-1237 | ROS (ros-infrastructure/rep) | REP 2004 -- Package Quality Categories | 2019-12-17 | 오픈소스 문서 | high | 2026-09-30 | https://ros.org/reps/rep-2004.html | 아니오 |
| ref-1238 | SPDX Project (Linux Foundation) | SPDX Overview | 미확인 | 표준 | high | 2026-09-30 | https://spdx.dev/about/overview/ | 아니오 |
| ref-1239 | Open Robotics (Gazebo Classic) | Gazebo : Tutorial : Model structure and requirements | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://classic.gazebosim.org/tutorials?tut=model_structure | 아니오 |
| ref-1240 | 지디넷코리아 | "실외 이동로봇 필수보험 94% 저렴하게" | 2024-02-08 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240208201432 | 아니오 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-992 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부만 확인) | 2023-07-28 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1243 | 김·장 법률사무소 | 인공지능, 소프트웨어 결함으로 인한 제조물책임의 … (제목 일부만 확인) | 2024-07 | 업계 보고서 | medium | 2026-09-30 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=29930 | 아니오 |
| ref-1244 | 법제처 찾기쉬운 생활법령정보 | 개인정보보호 > 개인정보의 처리단계별 보호방안 (이동형 영상정보처리기기) (제목 일부만 확인) | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1257&ccfNo=2&cciNo=3&cnpClsNo=3 | 아니오 |
| ref-1245 | 대한민국 정책브리핑 (과학기술정보통신부) | '인공지능기본법' 22일 시행…생성형 AI 결과물 … (제목 일부만 확인) | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148958380 | 아니오 |
| ref-1246 | Open Robotics (ROS 2 Documentation) | ROS 2 developer guide | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://docs.ros.org/en/rolling/The-ROS2-Project/Contributing/Developer-Guide.html | 아니오 |
| ref-1247 | 고용노동부 | 산업용 로봇과 컨베이어도 안전검사 필수 | 2017-10-26 | 정부·연구기관 | medium | 2026-09-30 | https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=8135 | 아니오 |
| ref-1248 | Commonwealth of Virginia (Code of Virginia) | § 46.2-908.1:1. Personal delivery devices | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://law.lis.virginia.gov/vacode/title46.2/chapter8/section46.2-908.1:1/ | 아니오 |
| ref-555 | European Parliament and Council of the European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council of 14 June 2023 on machinery | 2023-06-14 | 정부·연구기관 | medium | 2026-09-30 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-1212 | European Agency for Safety and Health at Work (EU-OSHA) | Regulation 2023/1230/EU - machinery | 미확인 | 정부·연구기관 | medium | 2026-09-30 | https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/law-regulation-insurance-and-licensing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(핵심 질문 답, 추정), f9·f11(소프트웨어 사고 책임의 법적 공백·변화), f14(보고 기한) / 섹션 4: 운행안전인증·관제장치 조합 f1·f5, 운용자 f2, 책임보험·공제 f3, 제조물(소프트웨어 포함 여부) f9·f11, 실질적 변경 f9·f12, 사이버복원력법 보고 f14, 이동형 영상정보처리기기 f15, 라이선스 선언·SBOM f17~f19 / 섹션 5: 실외 — f1·f5(제약·수행 자원, 한국)·f2(수행 자원)·f3(제약)·f4(예외·성과)·f6·f7(제약), f8(제약, 미국 버지니아). 산업 사업장 안전검사 f16 은 출처가 현장 유형을 밝히지 않아 현장 유형 미명시로 서술. 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했음을 명시 / 섹션 6: 인증·보험 조건의 운영 제약 반영 f5·f3·f8, 사고·취약점 보고 체계 f14·f10, 라이선스 선언·자동 검사·SBOM f17~f20 / 섹션 7: 지능형로봇법·도로교통법 f1~f7, 버지니아 PDD 주법 f8, EU 제조물책임지침 f9·f10, 한국 제조물책임법 f11, EU 기계류 규정 f12, 인공지능 기본법 f13, EU 사이버복원력법 f14, 개인정보보호법 제25조의2 f15, 산업안전보건법 안전검사 f16, ROS 2 개발자 가이드·REP 2004 f17·f18, SPDX(ISO/IEC 5962) f19, Gazebo 모델 라이선스 f20 / 섹션 8: f9·f11·f14 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 3, 4, 13, 16, 36, 47, 50, 52, 53, 57, 58, 66 / 섹션 11: 기존 oq-143·oq-173·oq-186·oq-187·oq-231·oq-239·oq-249·oq-250·oq-262(모두 미해결 유지; oq-186 은 f5·f6·f7 로 현재 8개 항목만 확인, oq-143 은 f13 으로 부분 근거)와 open_questions_new 5건. 다음 실행 후보: 66. 실외 페이지에 f1~f8, 57. 자산·소프트웨어 수명주기 관리 페이지에 f17~f19 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 제조물책임 | Product Liability | 제조물의 결함으로 생명·신체·재산에 손해가 생겼을 때 제조업자 등이 과실과 관계없이 배상 책임을 지는 제도로, 한국은 제조물책임법, EU는 개정 제조물책임지침(2024/2853)이 정하며 EU 지침은 소프트웨어를 제품에 포함한다. |
| 사이버복원력법 | Cyber Resilience Act (CRA) | 디지털 요소를 가진 제품의 사이버보안 요구사항과 제조자의 취약점·중대 사고 보고 의무(2026-09-11부터)를 정한 EU 규정이다. |
| 소프트웨어 자재명세서 | Software Bill of Materials (SBOM) | 소프트웨어를 이루는 구성 요소와 그 출처·버전·라이선스·보안 정보를 기계가 읽을 수 있게 나열한 목록으로, SPDX(ISO/IEC 5962:2021) 같은 형식으로 교환한다. |
| 오픈소스 소프트웨어 스튜어드 | Open-source Software Steward | EU 사이버복원력법에서 상업 활동에 쓰이는 자유·오픈소스 소프트웨어의 개발을 체계적·지속적으로 지원하는 법인으로, 제조자보다 가벼운 사이버보안·보고 의무를 진다. |

## 열린 질문

새로 생긴 질문:

- 한국 실외이동로봇 책임보험·공제의 최저 가입금액(사망·부상·재물 한도)을 정한 산업통상자원부령 조항과 금액은 무엇인가? | 관련 영역: 59. 법·규제·보험·라이선스, 66. 실외 | 근거: f3 | 종류: 일반
- EU 개정 제조물책임지침에서 여러 제조사 로봇에 명령을 내리는 오케스트레이션 소프트웨어는 결함 제품이나 관련 서비스로 다뤄지는가, 그 소프트웨어의 설정·기능 변경이 실질적 변경에 해당해 플랫폼 사업자가 제조자로 간주될 수 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f9 | 종류: 일반
- 국내 제조물책임법에 소프트웨어를 제조물로 포함하는 개정안이 발의되거나 통과되었는가, 그리고 로봇 관제·오케스트레이션 소프트웨어의 결함 사고에 관한 국내 판례가 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f11 | 종류: 일반
- 로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가? | 관련 영역: 59. 법·규제·보험·라이선스, 52. 통신 보호·위협 관리·감사, 57. 자산·소프트웨어 수명주기 관리 | 근거: f14 | 종류: 일반
- 시뮬레이션·가상 시운전에 쓰는 3D 자산(로봇 모델·건물 모델)의 라이선스와 저작자 표기를 자산 단위로 추적하는 표준 방법이 있으며, SPDX 로 3D 자산의 라이선스를 기술한 사례가 있는가? | 관련 영역: 59. 법·규제·보험·라이선스, 36. 가상 시운전·실제 상황 재현, 57. 자산·소프트웨어 수명주기 관리 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 2
- 예산 사용량: 검색 17회 · 신규 출처 15건
- 미확인 항목:
    - f3 실외이동로봇 책임보험 가입금액(사망 1억5천만원·부상 3천만원·재물 10억원)은 검색 요약에만 있고 시행규칙 원문을 열지 못해 finding 에서 뺌
    - f4 단체보험 보장 한도 미확인
    - f7 운행안전인증 심사항목이 16가지에서 8개로 바뀐 개정 시점·근거 고시 미확인(oq-186). 검색 요약에 '다시 16개로 재정의'라는 서술이 있었으나 인증기관 페이지(2026-09-30 확인)는 8개를 나열해 확인되지 않은 요약은 쓰지 않음
    - f9·f10 EU 제조물책임지침은 EUR-Lex 원문·PDF 본문이 비어 열지 못해 법률사무소 해설 기준. 오픈소스 예외 조항 미확인
    - f11 김·장 뉴스레터 PDF 본문 미열람, 웹 요약 기준
    - f13 고영향 인공지능의 법정 영역 목록과 사업자 책무 조문은 시행령·가이드라인 원문을 열지 못해 미확인(신·김 뉴스레터 403)
    - f14 오픈소스 스튜어드 보고 의무 시점(2027-12-11)은 집행위원회 페이지 한 곳 기준이며, 제조자 보고 의무 시점과 같다고 적은 다른 요약과 교차 확인하지 못함
    - f15 개인정보보호법 제25조의2 시행일은 출처 요약이 2023-09-15(검색 요약)와 2024-12-03(생활법령 페이지 요약)으로 달라 finding 에 넣지 않음
    - f16 산업용 로봇 정기 안전검사 주기(최초 3년 이내, 이후 2년)는 검색 요약에만 있고 안전보건공단 페이지가 비어 확인하지 못함
    - Open-RMF 저장소 라이선스는 GitHub 페이지 403·raw 경로 404 로 확인하지 못해 넣지 않음
    - 일본 원격조작형 소형차 신고제(2023-04 시행)는 1차 출처를 열지 않아 넣지 않음
    - 병원·상업 시설·가정 실내 로봇의 운행 규정, 승강기 탑승 KS(oq-173), 실내 사람 근접 기준(oq-231)은 이번에 조사하지 못함
- 범위 경계 위반 의심:
    - f16: 산업용 로봇 안전검사는 사업주의 설비 안전 의무이고 원문 19장 '시설·설비 제어'·'업종별 조건' 쪽이므로 규제 사례로만 쓰고 ROP 직접 범위로 서술하지 않음(f23 연계 대상)
    - f9·f10·f11: 제조물 책임의 법적 판정은 당사자·법원 몫이므로 ROP 가 제공할 기록의 근거로만 쓰고 f23 에서 연계 대상으로 둠
    - f15: 영상 촬영 적법성 판단은 53. 개인정보·영상 데이터와 겹치므로 이 영역에서는 규제 목록으로만 다룸
    - f8: 미국 주법은 한국 현장에 바로 적용되지 않으므로 해외 비교 사례로만 제안
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 15건/15(ref-991~ref-1248, 예약 구간 안)로 신규 출처 상한에 도달했다. 재사용 2건: ref-555·ref-1212(EU 기계류 규정, 이전 브리프 2026-09-30-22 출처 표 값 사용, 이번에 다시 열지 않아 fetched false). 참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요. 원문 열람: 신규 15건 모두 열었다(webfetch 13, github_raw 2). ros.org(봇 차단)는 ros-infrastructure/rep, docs.ros.org 는 ros2/ros2_documentation 공식 저장소 원본을 열었다. EUR-Lex(본문 비어 있음)·신·김 뉴스레터(403)·안전보건공단 포털(본문 비어 있음)·Open-RMF GitHub(403)는 열지 못해 출처로 쓰지 않았다. 교차 확인 2건(f1: 정책브리핑·한국로봇산업진흥원, f3: 정책브리핑·지디넷코리아). 벤더 주장 없음. 분류 원문 핵심 질문에는 f21 로 답했고 결론은 '현장마다 다르며 실외는 운행 규정·인증·운용자 의무·의무 보험, 산업 사업장은 기계 안전 규제, 공통으로 AI·사이버보안·개인정보 규제, 제조물 책임, 오픈소스·3D 자산 라이선스가 겹친다'는 추정이다. 현장 유형 사례는 실외(f1~f7 한국, f8 미국)뿐이고 f16(산업용 로봇 안전검사)은 출처가 현장 유형을 밝히지 않아 null 로 두었다. 물류창고·제조 공장·병원·상업 시설·가정 사례는 찾지 못했다. 국내 자료는 정책브리핑(ref-991·ref-1245)·한국로봇산업진흥원(ref-980)·고용노동부(ref-1247)·법제처 생활법령(ref-1244)·김·장(ref-1243)·지디넷코리아(ref-1240·ref-992)다. 기존 열린 질문 9건은 해결하지 못했다(oq-186 은 현재 8개 심사항목만 확인, 개정 시점·흡수 관계 미확인; oq-187 은 인증 대상이 로봇과 관제장치 조합이라는 전제만 재확인; oq-143 은 f13 이 사람의 최종 결정 권한 시 고영향 제외라는 정부 설명만 제공해 부분 근거). L. AI·학습 기술 관련은 f13(인공지능 기본법)을 13. 대화형 기능의 신뢰·기반과 47. AI·학습·적응과 모델 운영에 연결 제안했다(f24). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 고영향 인공지능·실외이동로봇 운행안전인증·개인 배송 장치·이동형 영상정보처리기기·원격 조작형 소형차·위험성평가는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```
