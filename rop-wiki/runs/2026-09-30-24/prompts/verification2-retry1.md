(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-24
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 60. 노동·수용성·접근성 (P. 거버넌스·법규·사회)
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

### runs/2026-09-30-24/target.json

```json
{
  "run_id": "2026-09-30-24",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 133,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 60,
    "area_name": "60. 노동·수용성·접근성",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=60"
}
```

### runs/2026-09-30-24/research.json

```json
{
  "run_id": "2026-09-30-24",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 60,
    "area_name": "60. 노동·수용성·접근성",
    "category": "P. 거버넌스·법규·사회"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 기술 수용 모델(UTAUT·Almere 모델), 노사협의·공동결정, 근로자 감시 설비, 무인정보단말기 접근성, 연석 경사로 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고(부상·감시 우려), 병원(작업 흐름 적합성·종사자·환자 만족도), 실외(휠체어 이용자와 보도 로봇) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 수용성 측정 모델, 참여 설계(co-design), 직무 설계, 노동자 참여 절차 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO/IEC Guide 71, 장애인차별금지법 무인정보단말기 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 로봇의 고용·임금 효과(미국·한국), 창고 로봇과 부상, 병원 로봇 민족지 연구 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-146, oq-188, oq-266 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]",
    "로봇 도입은 고용·임금과 일하는 방식(작업 속도·부상·직무 내용)을 어떻게 바꾸는가(미국·한국 실증 연구, 물류창고 부상 자료)? (섹션 3·5·8 겨냥)",
    "일하는 사람과 이용하는 사람의 로봇 수용성은 어떤 모델로 측정하고, 어떤 요인(작업 흐름 적합성, 감시·데이터, 사회적 상호작용)이 좌우하는가(병원·돌봄·물류창고 사례)? (섹션 4·5·6 겨냥)",
    "고령자·장애인·어린이가 로봇 서비스를 안전하게 쓰고 피할 수 있게 하는 표준·법 의무(ISO/IEC Guide 71, 장애인차별금지법 무인정보단말기 접근성)는 무엇인가? (섹션 7 겨냥, 한국 자료 우선)",
    "보도 로봇이 휠체어 이용자 등 보행 약자의 통행을 막지 않게 하는 설계·운영 기준이나 사례가 있는가? (섹션 5·6 겨냥, oq-188 관련)",
    "로봇 도입과 작업자 데이터 수집에 노동자 참여·협의를 요구하는 법 절차(한국 근로자참여법, 독일 사업장조직법)는 무엇인가? (섹션 6·7 겨냥, oq-266 관련)",
    "노동·수용성·접근성에서 ROP가 직접 맡을 것과 사용자·노사·제조사·법무에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "EU-OSHA(유럽 산업안전보건청)는 2022-06-16 보고서 'Advanced robotics and automation: implications for occupational safety and health'에서 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다뤘다.",
      "tag": "사실",
      "source_ids": [
        "ref-1277"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EU-OSHA 게시 페이지: 'The specific focus is how increasing use of robotic systems that could also collaborate with humans, impacts workers' (2022-06-16 게시).",
      "as_of": "2022-06-16",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "EU-OSHA 게시 페이지 요약은 첨단 로봇의 심리사회적 위험으로 고용 불안, 작업 강도 증가, 의사결정 자율성 감소, 탈숙련, 로봇에 대한 신뢰 문제를 들고, 도입 결정에 노동자 참여·인간 중심 설계·교육을 권고하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1277"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "게시 페이지 요약 기준이며 보고서 PDF 본문은 열리지 않아(인코딩 오류) 위험 목록과 권고 문구를 원문에서 확인하지 못했다.",
      "as_of": "2022-06-16",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f3",
      "claim": "물류창고 사례(미국 아마존 풀필먼트 센터): Burtch·Greenwood·Ravindran(ILR Review, 2025)은 로봇 풀필먼트 센터에서 기존 센터보다 중대 부상이 40% 줄고 비중대 부상이 77% 늘었다고 보고했고, 작업자 온라인 게시글에서는 로봇 센터의 피킹 목표량이 2~3배 높다는 진술이 나왔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1264"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "GMU 뉴스(2025-08-26): 로봇 센터 중대 부상 40% 감소, 비중대 부상 77% 증가, 작업자 게시글 수천 건 분석. 논문 DOI 10.1177/00197939251333754(원문 403으로 미열람).",
      "as_of": "2025-08-26",
      "site_type": "물류창고",
      "flow_item": "예외·성과"
    },
    {
      "id": "f4",
      "claim": "같은 연구진은 창고 자동화가 위험 작업을 없애는 대신 남은 작업의 다양성을 줄이고 작업 속도를 높여 반복성 긴장 손상 같은 비중대 부상을 늘리므로, 위험이 사라지기보다 재분배되며 직무 설계로 대응해야 한다고 해석한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1264"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "GMU 뉴스 제목 'Warehouse automation hasn't made workers safer — it's just reshuffled risk'; 빠른 작업 속도와 단조로운 작업이 새로운 건강 위험을 만든다는 저자 해석.",
      "as_of": "2025-08-26",
      "site_type": "물류창고",
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "물류창고 사례: Malik·Brandão·Coopamootoo(International Journal of Social Robotics, 2026)는 창고 작업자 12명 반구조화 면담에서 로봇 운영에 딸린 데이터 감시에 대한 우려와 더 주체적인 협업에 대한 요구를 확인하고, 수동 무시(override)·개인정보 통제·감시 활동 알림 같은 작업자 중심 요구를 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1278"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 요약: 작업자 12명 면담, 'data surveillance' 우려, 'a spectrum of worker-centered requirements and visions'(수동 무시·개인정보 통제·감시 알림).",
      "as_of": "2026",
      "site_type": "물류창고",
      "flow_item": "제약"
    },
    {
      "id": "f6",
      "claim": "Acemoglu·Restrepo(NBER 작업논문 w23285, 2017-03; Journal of Political Economy 2020 게재)는 1990~2007년 미국 통근권역 자료로 노동자 1천 명당 로봇 1대가 늘면 고용률이 약 0.18~0.34%p, 임금이 0.25~0.5% 낮아진다고 추정했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1275"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NBER 초록: 'one more robot per thousand workers reduces the employment to population ratio by about 0.18-0.34 percentage points and wages by 0.25-0.5 percent'(1990-2007, 산업용 로봇).",
      "as_of": "2017-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "한국노동연구원 보고서 '기술 혁신과 노동시장 변화'(2024-12)를 전한 보도에 따르면, 노동자 1천 명당 로봇 6.6대 증가(로봇 노출도 한 단계)마다 고숙련 제조업 노동자의 임금은 2.5%, 고용률은 0.55%p 올랐으나 저숙련 제조업 노동자 임금은 4.5~4.9% 줄었고 45~54세 고용률은 0.37%p 낮아졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1266",
        "ref-1267"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "수치는 한국경제 보도(2025-04-01) 기준. 보고서의 존재·발행기관·발행월(2024-12)은 국회 정책정보 페이지로 확인했으나 수치는 보고서 원문에서 확인하지 못함.",
      "as_of": "2025-04-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "병원 사례(미국): Mutlu·Forlizzi(HRI 2008)의 자율 배송 로봇 TUG 민족지 연구에서 내과 병동은 방해에 대한 낮은 허용도, 인식된 비용과 이득의 불일치, 붐비는 통로의 운행 중단 때문에 로봇이 작업 흐름을 해치고 직원 저항을 불렀지만 산후 병동은 로봇을 작업 흐름과 사회적 맥락에 통합했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1151"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "논문 PDF 일부와 초록 기준: 작업 환경과 방해 가능성(interruptability)이 서비스 로봇 평가를 좌우하는 요인이라는 결론.",
      "as_of": "2008",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f9",
      "claim": "병원 사례(한국): 한림대성심병원은 2022-08~2024-12 의료서비스로봇 11종 77대를 도입해 51,092건을 사용했고, 2023년 하반기 간호사 109명 조사에서 90% 이상이 단순업무 경감, 94%가 계속 사용을 희망했으며, 입원환자 147명 중 93.9%가 영상 안내가 도움이 됐고 99%가 로봇에 거부감이 없다고 답했다고 보도됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1274"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "의협신문(2025-01-21) 보도 기준. 병원 자체 만족도 조사이며 조사 방법은 공개되지 않음. 다른 보도는 병동 간호사 99명 중 91.9%로 적어 표본 구분 미확인.",
      "as_of": "2025-01-21",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "Heerink 외(International Journal of Social Robotics 2(4), 2010)의 Almere 모델은 통합 기술 수용 이론(UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하며, 요양시설과 가정에서 세 가지 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1269"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'accounting for 59-79% of the variance in usage intentions and 49-59% of the variance in actual use'(요양시설·가정, 세 소셜 에이전트).",
      "as_of": "2010",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "김소라(주관성 연구 63, 2023)는 Q방법론으로 노인 이용자·가족·돌봄서비스 종사자의 돌봄로봇 인식을 '불가피한 대체재', '상호보완적 동반자', '열등한 보조재', '불완전한 경쟁자'의 네 유형으로 나눴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1273"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KCI 초록 기준: 네 인식 유형 가운데 '불가피한 대체재 인식 유형'의 설명력이 가장 크다.",
      "as_of": "2023",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "실외 사례(미국): Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명 면담, 4회의 공동설계 워크숍으로 보도 로봇이 들어오면 이동장애인이 보도 공간을 두고 경쟁한다고 느끼고, 실무자는 기업이 문제가 생긴 뒤에야 접근성을 다룬다고 인정했으며, 두 집단 모두 처음부터 접근성을 통합해야 한다고 보았음을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1265"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2404.05050(CHI '24): 'feel they have to compete for space on the sidewalk when robots are introduced'.",
      "as_of": "2024-04-07",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "같은 연구가 출발점으로 삼은 사례에서 배송 로봇이 연석 경사로에 멈춰 휠체어 이용자의 횡단 후 통행을 막았고 이용자가 이를 공개하자 업체가 로봇 운행을 잠시 중단했으며, 참여자들은 연석 경사로로 다가오는 사람을 감지하면 로봇이 자동으로 경로를 다시 계획하고 스스로 비켜 주차하는 기능을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1265"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "논문 본문: 로봇이 연석 경사로(curb cut)에서 정지해 통행을 막은 사건, 업체의 일시 운행 중단, 'automatically replan when detecting people approaching curb cuts' 제안.",
      "as_of": "2024-04-07",
      "site_type": "실외",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "ISO/IEC Guide 71:2014(2판, 2014-12)는 사람이 쓰는 제품·서비스·건축 환경을 다루는 표준에 접근성 요구를 넣도록 표준 개발자에게 지침을 주며 장애인·어린이·고령자의 접근성 요구를 주로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1276"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 소개 요약(검색 결과): 표준 개발자 대상 지침, 'persons with disabilities, children and older persons'. 원문·ISO 페이지 403으로 미열람.",
      "as_of": "2014-12",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "한국에서는 2026-01-28부터 무인정보단말기를 설치·운영하는 모든 사업자가 디지털 접근성 지침의 검증 기준을 충족하는 장애인 접근 가능 기기를 제공해야 하며, 바닥면적 50㎡ 미만 시설·소상공인·테이블 주문형 기기는 보조기기·보조 인력·호출벨 등으로 대신할 수 있고, 위반은 장애인 차별에 해당한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1268"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보건복지부 정책브리핑(2026-01-28): 접근성 갖춘 무인정보단말기 설치 의무 전면 시행, 소규모 시설 대체 수단 허용.",
      "as_of": "2026-01-28",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "한국 근로자참여 및 협력증진에 관한 법률 제20조 제1항은 노사협의회가 협의할 사항으로 근로자의 채용·배치 및 교육훈련(제2호), 신기계·기술의 도입 또는 작업 공정의 개선(제9호), 사업장 내 근로자 감시 설비의 설치(제14호)를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1272"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제20조 제1항 제9호 '신기계·기술의 도입 또는 작업 공정의 개선', 제14호 '사업장 내 근로자 감시 설비의 설치'(법률 제16320호, 2019-07-17 시행).",
      "as_of": "2019-07-17",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f17",
      "claim": "독일 사업장조직법(BetrVG) 제87조 제1항 제6호는 법률·단체협약 규정이 없는 한 노동자의 행동이나 성과를 감시하도록 정해진 기술 장치의 도입과 적용에 사업장협의회의 공동결정권을 두고, 합의가 안 되면 중재위원회(Einigungsstelle)가 결정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1271"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§87 Abs.1 Nr.6: 'Einführung und Anwendung von technischen Einrichtungen, die dazu bestimmt sind, das Verhalten oder die Leistung der Arbeitnehmer zu überwachen'.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "시작 조건"
    },
    {
      "id": "f18",
      "claim": "f5·f16·f17을 종합하면 로봇 작업과 연결해 개별 작업자의 처리량·위치·행동 데이터를 남기는 오케스트레이션 기능은 한국에서는 노사협의회 협의 사항(신기계 도입, 근로자 감시 설비), 독일에서는 공동결정 대상 감시 장치로 다뤄질 수 있어 도입 전에 노동자 참여 절차가 필요할 가능성이 있으나, 해당 여부는 법적 판단으로 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1278",
        "ref-1272",
        "ref-1271"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "조문과 작업자 면담 결과를 결합한 추론이며 로봇·플랫폼 로그에 적용한 판례·행정해석은 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "확인한 자료를 종합하면 핵심 질문(로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가)의 답은 한 가지가 아니며, 일하는 사람 쪽은 작업 흐름 적합성(f8)·작업 속도와 직무 설계(f3·f4)·데이터 감시(f5)·고용과 숙련 효과(f6·f7)가, 이용하는 사람 쪽은 사회적 상호작용 요인(f10·f11)과 보행 약자의 공간·접근성(f12·f13·f15)이 수용 여부를 가르는 것으로 보이고, 기관 자체 설문은 높은 만족도를 보고한다(f9).",
      "tag": "추정",
      "source_ids": [
        "ref-1151",
        "ref-1264",
        "ref-1278",
        "ref-1275",
        "ref-1266",
        "ref-1269",
        "ref-1273",
        "ref-1265",
        "ref-1268",
        "ref-1274"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "여러 현장(물류창고·병원·실외·돌봄)의 개별 연구를 종합한 판단이며 같은 현장에서 노동자와 이용자 수용성을 함께 측정한 연구는 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 60. 노동·수용성·접근성에서 ROP가 직접 맡을 범위는 로봇과 사람의 작업 분담·작업 속도(목표량) 설정을 드러내고 조정할 수 있게 하는 것, 작업자 데이터 수집 범위 표시·감시 알림·수동 무시 같은 작업자 통제 수단을 제공하는 것, 연석 경사로·통로에서 보행 약자에게 양보하고 멈추지 않는 대기 위치 규칙을 경로·작업 제약으로 반영하는 것, 운영자·이용자 화면의 접근성을 갖추는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1264",
        "ref-1278",
        "ref-1265",
        "ref-1268"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3·f5·f13·f15 에서 나온 요구를 분류 원문 19장 경계에 맞춰 플랫폼 기능으로 옮긴 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f21",
      "claim": "연계 대상: 분류 원문 19장 기준으로 고용·임금·재교육 정책, 노사협의·공동결정 절차와 근로자 감시 설비의 적법성 판단(사업주·노동자 대표·법무), 장애인차별금지법 등 접근성 법적 적합성 판단(운영자·법무), 로봇 본체의 물리적 접근성 설계(높이·음성 조작 등 제조사)는 외부가 맡고, ROP는 그 결정을 작업·경로·권한 제약과 화면 설계로 받아 반영하고 근거 기록을 제공하는 쪽인 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1272",
        "ref-1271",
        "ref-1268",
        "ref-1265",
        "ref-1266"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "법 조문(f16·f17)·접근성 의무(f15)·공동설계 제안(f13)의 주체를 기준으로 나눈 추론.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f22",
      "claim": "이 영역은 작업 분담·속도의 31. 사람–로봇 협업과 25. 작업 배정 — MRTA(f3·f4), 부상의 49. 사람 근접 안전(f3), 작업자 데이터 감시의 53. 개인정보·영상 데이터(f5·f18), 보행 약자와 대기 위치의 19. 사람·보행자 모델과 16. 장소 의미·지도 관리(f12·f13), 목표량 지표의 39. 운영 성과 측정·개선(f3), 교육·도입 절차의 56. 운영 이관·확대·교육(f2·f8), 화면 접근성의 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반(f15), 법 의무의 59. 법·규제·보험·라이선스(f15·f16·f17), 효과 추정의 3. 경제성·조달·사업 모델(f6·f7), 적용 현장인 61. 물류창고·63. 병원·의료·66. 실외(f3·f5·f8·f9·f12)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1264",
        "ref-1278",
        "ref-1265",
        "ref-1277",
        "ref-1151",
        "ref-1268",
        "ref-1272",
        "ref-1271",
        "ref-1275",
        "ref-1266",
        "ref-1274"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결은 괄호 안 finding 의 주제에서 도출한 추론이다.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1264",
      "org": "George Mason University Costello College of Business",
      "title": "Warehouse automation hasn't made workers safer — it's just reshuffled risk",
      "published": "2025-08-26",
      "url": "https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Burtch·Greenwood·Ravindran 의 ILR Review 논문(Lucy and the Chocolate Factory, DOI 10.1177/00197939251333754)을 소개하는 대학 뉴스. 아마존 로봇 센터의 중대 부상 40% 감소·비중대 부상 77% 증가를 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1265",
      "org": "Han, H. Z. 외 (Carnegie Mellon University) — CHI '24",
      "title": "Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations",
      "published": "2024-04-07",
      "url": "https://arxiv.org/abs/2404.05050",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "이동장애인 15명·로봇 실무자 8명 면담과 공동설계 워크숍 4회로 보도 로봇의 접근성 문제와 설계안을 도출한 CHI 2024 논문.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2404.05050v1",
      "source_unopened": false
    },
    {
      "id": "ref-1266",
      "org": "한국경제",
      "title": "로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인)",
      "published": "2025-04-01",
      "url": "https://www.hankyung.com/article/2025040138391",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국노동연구원 '기술 혁신과 노동시장 변화' 보고서의 로봇 노출도별 임금·고용 효과 수치를 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1267",
      "org": "한국노동연구원 (국회 정책정보 포털 NABIS 게재)",
      "title": "기술 혁신과 노동시장 변화",
      "published": "2024-12",
      "url": "https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자동화·로봇 도입·AI 가 지역 고용과 인적자본에 주는 영향을 분석한 한국노동연구원 보고서(2024-12)의 소개 페이지. 세부 수치는 페이지에 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1268",
      "org": "대한민국 정책브리핑 (보건복지부)",
      "title": "장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행",
      "published": "2026-01-28",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958690",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2026-01-28부터 모든 무인정보단말기 설치·운영 사업자에게 장애인 접근성 기기 제공을 의무화하고 소규모 시설의 대체 수단을 허용한 조치를 알린 보도자료.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1269",
      "org": "Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics)",
      "title": "Assessing acceptance of assistive social agent technology by older adults: the Almere model",
      "published": "2010",
      "url": "https://doi.org/10.1007/s12369-010-0068-5",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "UTAUT 에 사회적 상호작용 변수를 더한 고령자용 보조 소셜 에이전트 수용성 모델(Almere 모델)을 제안·검증한 논문. 암스테르담대 저장소 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://dare.uva.nl/search?identifier=d2099065-f734-4cc1-bf00-46333c2c77c1",
      "source_unopened": false
    },
    {
      "id": "ref-1151",
      "org": "Mutlu, B., Forlizzi, J. (HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "병원 자율 배송 로봇 TUG 도입을 민족지로 조사해 병동별 작업 흐름·방해 허용도·환경이 수용과 저항을 가른다는 점을 보인 논문. PDF 는 일부만 읽혔다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1271",
      "org": "Bundesministerium der Justiz (gesetze-im-internet.de)",
      "title": "Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte",
      "published": null,
      "url": "https://www.gesetze-im-internet.de/betrvg/__87.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "독일 사업장조직법 제87조. 노동자 행동·성과 감시용 기술 장치의 도입·적용에 대한 사업장협의회 공동결정권(제1항 제6호)과 중재위원회 결정(제2항)을 정한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1272",
      "org": "대한민국 국회 (법률 제16320호, 케이스노트 게재)",
      "title": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항)",
      "published": "2019-04-16",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "노사협의회 협의 사항(채용·배치·교육훈련, 신기계·기술 도입, 근로자 감시 설비 설치 등 17개 호)을 정한 조문. 국가법령정보센터 본문이 열리지 않아 법령 게재 사이트로 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1273",
      "org": "김소라 (주관성 연구, 한국주관성연구학회)",
      "title": "돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구",
      "published": "2023",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 분류한 국내 논문. KCI 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1274",
      "org": "의협신문",
      "title": "\"로봇이 병원을 돌아다닌다\"…의료서비스로봇 5만건 돌파",
      "published": "2025-01-21",
      "url": "https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원의 의료서비스로봇 11종 77대 도입·사용 5만 건과 간호사·입원환자 만족도 조사 결과를 전한 기사(병원 발표 기반).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1275",
      "org": "Acemoglu, D., Restrepo, P. (NBER)",
      "title": "Robots and Jobs: Evidence from US Labor Markets",
      "published": "2017-03",
      "url": "https://www.nber.org/papers/w23285",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "1990~2007년 미국 통근권역 자료로 산업용 로봇이 고용과 임금을 낮춘다고 추정한 NBER 작업논문(2020년 Journal of Political Economy 게재).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1276",
      "org": "ISO/IEC",
      "title": "ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards",
      "published": "2014-12",
      "url": "https://www.iso.org/standard/57385.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 표준 개발자가 장애인·어린이·고령자의 접근성 요구를 표준에 반영하도록 돕는 지침(2판). ISO 페이지 403 으로 검색 결과 요약만 확인.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1277",
      "org": "European Agency for Safety and Health at Work (EU-OSHA)",
      "title": "Advanced robotics and automation: implications for occupational safety and health",
      "published": "2022-06-16",
      "url": "https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "협업 가능한 로봇 시스템의 확산이 노동자의 안전·건강·웰빙에 주는 영향을 다룬 EU-OSHA 보고서의 게시 페이지. 보고서 PDF 는 읽히지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1278",
      "org": "Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics)",
      "title": "Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety",
      "published": "2026",
      "url": "https://doi.org/10.1007/s12369-026-01359-1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "창고 작업자 12명 면담으로 로봇 운영의 데이터 감시 우려와 작업자 중심 요구(수동 무시·개인정보 통제·감시 알림)를 정리한 논문. 학술 색인(OUCI)의 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://ouci.dntb.gov.ua/en/works/lRrprVOa/",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
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
      "rationale": "섹션 3: f19(핵심 질문 답, 추정), f3·f4(위험 재분배), f6·f7(고용·임금 효과), f12(보행 약자 공간 경쟁) / 섹션 4: 기술 수용 모델 UTAUT·Almere 모델 f10, 돌봄로봇 인식 유형 f11, 노사협의 협의 사항·근로자 감시 설비 f16, 공동결정 f17, 무인정보단말기 접근성 f15, 연석 경사로 f13, 접근성 대상 집단 f14 / 섹션 5: 물류창고 — f3(예외·성과), f4·f5(제약), 병원 — f8(예외·성과, 미국), f9(예외·성과, 한국), 실외 — f12(제약)·f13(예외·성과). 제조 공장·상업 시설·가정 사례는 찾지 못했음을 명시(f7 은 현장 사례가 아니라 산업 통계) / 섹션 6: 수용성 측정 모델 f10·f11, 참여 설계 f12·f13, 직무 설계 f4, 노동자 참여 절차 f2·f16·f17·f18 / 섹션 7: ISO/IEC Guide 71 f14(원문 미열람), 장애인차별금지법 무인정보단말기 의무 f15, 근로자참여법 제20조 f16, 독일 사업장조직법 제87조 f17 / 섹션 8: f1·f3·f6·f7·f8·f10·f12 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66 / 섹션 11: 기존 oq-146·oq-188·oq-266(모두 미해결 유지; oq-188 은 f13 이 해외 사례만 제공, oq-266 은 f8 이 병동 단위 차이만 제공)과 open_questions_new 4건. 다음 실행 후보: 61. 물류창고 페이지에 f3·f5, 66. 실외 페이지에 f12·f13, 63. 병원·의료 페이지에 f8·f9 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "통합 기술 수용 이론",
      "term_en": "Unified Theory of Acceptance and Use of Technology (UTAUT)",
      "definition": "성과 기대·노력 기대·사회적 영향·촉진 조건으로 기술 사용 의도와 실제 사용을 설명하는 기술 수용 모델로, 로봇 수용성 연구의 출발점으로 널리 쓰인다."
    },
    {
      "term_ko": "알메러 모델",
      "term_en": "Almere Model",
      "definition": "UTAUT 에 사회적 존재감·신뢰 같은 사회적 상호작용 변수를 더해 고령자의 보조 소셜 로봇·에이전트 수용성을 측정하도록 만든 모델이다(Heerink 외, 2010)."
    },
    {
      "term_ko": "무인정보단말기 접근성",
      "term_en": "Kiosk Accessibility (Unmanned Information Terminal Accessibility)",
      "definition": "키오스크 같은 무인정보단말기를 시각·이동 등 장애가 있는 사람도 동등하게 쓸 수 있게 하는 요건으로, 한국은 장애인차별금지법에 따라 2026-01-28부터 모든 설치 사업자에게 의무화했다."
    },
    {
      "term_ko": "연석 경사로",
      "term_en": "Curb Cut (Curb Ramp)",
      "definition": "보도와 차도 사이 턱을 경사로로 낮춘 부분으로, 휠체어·유모차 이용자가 횡단할 때 반드시 지나야 하므로 로봇이 이곳에 멈추면 통행을 막는다."
    }
  ],
  "open_questions_new": [
    "서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가? | 관련 영역: 60. 노동·수용성·접근성, 59. 법·규제·보험·라이선스, 64. 상업 시설 | 근거: f15 | 종류: 일반",
    "오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가? | 관련 영역: 60. 노동·수용성·접근성, 53. 개인정보·영상 데이터, 59. 법·규제·보험·라이선스 | 근거: f18 | 종류: 일반",
    "로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 31. 사람–로봇 협업, 25. 작업 배정 — MRTA | 근거: f3 | 종류: 일반",
    "국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 63. 병원·의료, 61. 물류창고 | 근거: f9 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "f2 EU-OSHA 보고서 PDF 본문이 읽히지 않아 심리사회적 위험 목록과 권고를 원문에서 확인하지 못함(게시 페이지 요약 기준, 추정·low)",
      "f3 ILR Review 논문 원문(SAGE·SSRN 403) 미열람 — 대학 뉴스 기준이며 데이터 출처(OSHA 사업장 부상 보고 2016~2020)는 검색 요약에만 있어 claim 에서 뺌",
      "f6 JPE 게재본 수치(고용률 0.2%p·임금 0.42%)는 검색 요약에만 있어 NBER 작업논문 범위값으로 적음",
      "f7 한국노동연구원 보고서 수치는 보도 기준이며 보고서 원문 미열람. 저자 한글 이름 미확인",
      "f9 간호사 조사 표본이 보도마다 다름(109명 90% 이상 / 병동 99명 91.9%) — 두 보도가 같은 병원 발표에서 나와 독립 교차 확인 불가",
      "f14 ISO/IEC Guide 71 원문·ISO 페이지 403 으로 미열람",
      "f16 국가법령정보센터 본문이 열리지 않아 법령 게재 사이트로 확인",
      "시각장애인과 공원 청소 로봇 현장 연구(ACM 2026, 10.1145/3776734.3794493)는 ACM 403 과 출처 상한으로 넣지 않음",
      "oq-146(국내 음성 지시 인식률)·oq-188(국내 대기 위치·점자블록 기준)·oq-266(운영 책임 조직 비교) 근거를 찾지 못함",
      "제조 공장·상업 시설·가정 현장의 노동·수용성·접근성 사례 미확인"
    ],
    "scope_violations": [
      "f6·f7: 로봇의 고용·임금 효과는 노동시장 정책 영역이므로 배경 근거로만 쓰고 ROP 직접 범위로 서술하지 않음(f21 연계 대상)",
      "f16·f17·f18: 노사협의·공동결정 절차와 감시 설비 적법성 판단은 사업주·노동자 대표·법무의 몫이며 59. 법·규제·보험·라이선스와 겹치므로 규칙 목록으로만 제안",
      "f15: 접근성 법 의무 적합성 판단은 운영자·법무 몫이며 로봇에 적용되는지는 열린 질문으로 보냄",
      "f13: 로봇 본체의 물리적 접근성 설계(높이 조절·음성 조작)는 제조사 영역이므로 ROP 몫은 경로·대기 위치 제약으로 한정(f20·f21)"
    ],
    "budget_used": {
      "queries": 20,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 20회/30, 신규 출처 15건/15(ref-1264~ref-1278, 예약 구간 안)로 신규 출처 상한에 도달해 시각장애인·공공 로봇 현장 연구, 제조 공장 사례 추가 조사를 하지 못했다. 재사용 출처 없음(참고문헌 목록 요약에 이 영역 인용 0건). 원문 열람: 15건 중 14건을 webfetch 로 열었고 ISO/IEC Guide 71(ref-1276)만 403 으로 미열람이다. 다만 ref-1269·ref-1273·ref-1278 은 초록만, ref-1151 은 PDF 일부만, ref-1277 은 게시 페이지만 읽었다. 교차 확인 0건(한림대성심병원 수치는 같은 병원 발표에서 나온 두 보도라 독립 아님). 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '한 가지 답은 없고, 일하는 사람 쪽은 작업 흐름 적합성·작업 속도·데이터 감시·고용 효과가, 이용하는 사람 쪽은 사회적 상호작용과 보행 약자 접근성이 수용을 가르며 기관 자체 설문은 높은 만족을 보고한다'는 추정이다. 현장 유형 사례는 물류창고(f3·f4·f5, 미국·영국계 연구), 병원(f8 미국, f9 한국), 실외(f12·f13 미국)이고 돌봄(f10·f11)은 출처가 현장 유형을 하나로 밝히지 않아 null 로 두었다. 제조 공장·상업 시설·가정 사례는 찾지 못했다. 국내 자료는 한국경제·국회 정책정보(한국노동연구원 보고서)·정책브리핑·근로자참여법·KCI 논문·의협신문이다. 기존 열린 질문 oq-146·oq-188·oq-266 은 해결하지 못했다(oq-188 은 f13 이 해외 연석 경사로 사례만, oq-266 은 f8 이 병동 단위 수용 차이만 제공). L. AI·학습 기술 관련 finding 은 없고, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. 용어집에 이미 있는 역할 모호성·자동화 편향·공공 영역 이동로봇·서비스 삼자 관계·이동형 영상정보처리기기는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-24/verification.json

```json
{
  "run_id": "2026-09-30-24",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: EU-OSHA 게시 페이지를 열어 제목·게시일(2022-06-16)·요약 문구(협업 로봇 시스템이 노동자와 일자리에 주는 영향)를 확인했다. 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "삭제",
      "note": "게시 페이지를 다시 열었지만 고용 불안·작업 강도 증가·자율성 감소·탈숙련·신뢰 같은 심리사회적 위험 목록과 노동자 참여·인간 중심 설계 권고는 없다. 페이지에서 확인되는 권고는 최종 사용자 교육의 중요성뿐이다. 보고서 PDF는 리서치 단계에서 열리지 않았으므로 출처가 뒷받침하지 않는 주장으로 보고 삭제한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: GMU 뉴스(2025-08-26)는 WebFetch로 열리지 않았다(307 리다이렉트). 대신 같은 보도문을 다시 실은 TechXplore와 검색 결과에서 중대 부상 40% 감소, 비중대 부상 77% 증가, 작업자 게시글의 '피킹 목표량 2~3배' 진술, ILR Review 게재를 확인했고 SSRN 원고 목록도 확인했다. TechXplore는 같은 보도문을 다시 실은 것이라 독립 교차 확인으로 보지 않는다. 논문 원문은 미열람이다. [사실]을 유지하되 '논문 원문이 아니라 저자 소속 대학의 발표 기준'이라고 밝히는 조건이다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 보도문이 위험 재분배, 빠른 작업 속도와 단조로운 작업, 직무 설계·작업 순환·달성 가능한 목표량의 필요를 저자(Greenwood) 해석으로 싣고 있다. [의견] 태그가 맞으며 누구의 의견인지(연구진) 밝혀야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OUCI 색인에서 제목·저자·학술지(IJSR 2026)·DOI, 작업자 12명 반구조화 면담, 데이터 감시 우려, 수동 무시·구역별 개인정보 통제·감시 알림 요구를 확인했다. 초록 기준이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: NBER 초록(2017-03)의 수치 범위(고용률 0.18~0.34%p, 임금 0.25~0.5%)와 1990~2007 기간, 2020년 JPE 게재가 일치한다. 수치는 NBER 작업논문 기준이며 게재본 수치와 다를 수 있다(브리프 self_check)."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 한국경제(2025-04-01) 기사에서 수치(1천 명당 6.6대, 고숙련 임금 +2.5%·고용률 +0.55%p, 저숙련 임금 −4.5~4.9%, 45~54세 고용률 −0.37%p)를 확인했다. 국회 정책정보 페이지에서는 보고서의 존재(한국노동연구원, 2024-12)를 확인했으나 수치는 없다. 핵심 수치가 기사 한 곳에만 있고 보고서 원문은 미열람이므로 강등한다. 저자 한글 이름은 미확인이다. NABIS 페이지에는 로마자 표기만 있다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 논문 PDF에서 내과 병동의 낮은 방해 허용도, 비용·이득 불일치, 붐비는 통로와 산후 병동의 통합을 확인했다(HRI 2008)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 의협신문(2025-01-21)에서 11종 77대, 누적 5만 1092건, 간호사 109명 가운데 90% 이상 단순업무 경감·94% 계속 사용 희망, 환자 147명 가운데 93.9% 도움·99% 거부감 없음을 확인했다. 병원이 직접 한 만족도 조사를 전한 기사 한 곳뿐이고 다른 보도와 표본이 달라 강등한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 암스테르담대 저장소 초록에서 UTAUT 확장, 사회적 상호작용 변수, 요양시설·가정, 설명력 59~79%와 49~59%를 확인했다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: KCI 초록에서 김소라, 주관성 연구 63호(2023), 노인 이용자·가족·돌봄 종사자, 네 유형과 '불가피한 대체재' 유형의 설명력이 가장 큰 점을 확인했다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록에서 이동장애인 15명·실무자 8명·공동설계 워크숍 4회, 보도 공간 경쟁, 기업이 문제가 생긴 뒤에야 접근성을 다룬다는 점, 처음부터 통합해야 한다는 점을 확인했다(CHI '24)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "핵심 확인: 논문 본문(arXiv HTML v1)에서 로봇이 연석 경사로에 멈춰 휠체어 이용자의 통행을 막은 사건과 업체의 일시 운행 중단을 확인했다. 사건은 Bennett 외(2021) 공저자가 겪은 것이다. 다만 '자동으로 경로를 다시 계획' 제안은 로봇 실무자 참여자 한 명(R3)의 제안이고, '스스로 비켜 주차' 부분은 원문에서 확인하지 못했다. 이 구절을 삭제하고 제안 주체를 바로잡는 조건으로 유지한다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(ISO 페이지 403, universaldesign.ie PDF 본문 추출 실패). 검색 결과(ISO·CSA·BSI 목록)에서 2판·2014-12-01 발행, 표준 개발자 대상 지침, 장애인·어린이·고령자 대상을 확인했다. 발행 기관 소개 자료 수준의 근거이므로 신뢰도는 medium 이하다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 정책브리핑(보건복지부, 2026-01-28)에서 전면 시행, 모든 설치·운영 사업자, 50㎡ 미만·소상공인·테이블 주문형의 대체 수단(호환 보조기기·소프트웨어, 보조 인력, 호출벨)을 확인했다. 표현 두 곳은 원문대로 고쳐야 한다. 검증 기준의 근거는 '디지털취약계층의 정보 접근 및 이용 편의 증진을 위한 고시'다. 위반 효과는 '차별행위로 인정되면 시정권고, 3천만 원 이하 과태료'다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 케이스노트 조문에서 제2호·제9호·제14호와 법률 제16320호(2019-07-17 시행)를 확인했다. 국가법령정보센터에서 현행 조문인지는 확인하지 못했으므로 기준 법률 번호·시행일을 명시한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: gesetze-im-internet.de에서 제87조 제1항 본문(법률·단체협약 규정이 없는 한), 제6호 원문, 제2항 중재위원회 결정을 확인했다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정 태그가 맞다. 조문(f16·f17)과 면담 결과(f5)를 결합한 추론이며, 법적 판단을 확인하지 못했다는 한계를 적었다. 법적 판단은 연계 대상으로 둔다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 핵심 질문에 대한 종합 추정이다. 근거 finding 가운데 f7·f9는 강등됐으므로 본문에서도 추정 근거로만 인용한다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f3·f5·f13·f15에서 이끈 추정이며 분류 원문 19장 경계 안의 기능(제약 반영·화면·통제 수단)으로 한정했다. 화면 접근성 의무가 적용되는지는 열린 질문으로 남긴다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 연계 대상 추정이며 19장의 '상위 업무 시스템'·'업종별 조건' 경계와 맞는다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 연결 추정이다. 56. 운영 이관·확대·교육 연결의 근거에서 삭제된 f2를 빼고 f8만 남긴다."
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
      "f16·f17(노사협의·공동결정 조문)과 f15(무인정보단말기 접근성 의무)는 59. 법·규제·보험·라이선스와 주제가 겹친다. 이번 59 브리프(2026-09-30-23)에는 이 조문들이 없어 충돌하지 않지만, 이 영역에서는 노동·접근성 관점으로만 쓰고 법적 적합성 판단은 59로 연결한다."
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
    "f2: 본문(3·6·8절)과 연결 근거에서 삭제한다 — 출처 ref-1277 게시 페이지에는 심리사회적 위험 목록과 노동자 참여·인간 중심 설계 권고가 없고 확인되는 권고는 최종 사용자 교육뿐이다. 6절 '노동자 참여 절차'의 근거는 f16·f17·f18로만 쓴다.",
    "f3: [사실]을 유지하되 문장이나 각주 설명에 '논문 원문이 아니라 저자 소속 대학(GMU) 발표 기준'이라고 밝힌다 — 논문 원문이 미열람이고 TechXplore 재게재는 독립 출처가 아니다.",
    "f4: [의견] 문장에 의견 주체를 'Burtch·Greenwood·Ravindran 연구진의 해석'으로 명시한다 — 의견 태그는 누구의 의견인지 밝혀야 한다.",
    "f7: [사실] → [추정]으로 강등하고 '한국경제 보도(2025-04-01) 기준, 보고서 원문 미확인'을 병기한다 — 핵심 수치가 기사 한 곳뿐이다. 보고서의 존재와 발행(한국노동연구원, 2024-12)은 ref-1267로 [사실] 서술할 수 있다.",
    "f9: [사실] → [추정]으로 강등하고 '병원 자체 만족도 조사, 의협신문 보도 기준, 다른 보도와 표본(간호사 109명 / 병동 간호사 99명)이 다름'을 밝힌다 — 단일 기사이고 조사 방법이 공개되지 않았다.",
    "f13: '스스로 비켜 주차하는 기능' 구절을 삭제하고, 경로 재계획 제안의 주체를 '참여자들'이 아니라 '로봇 실무자 참여자 한 명'으로 고친다 — 원문에서는 R3 한 명의 제안만 확인되고 주차 부분은 확인되지 않았다.",
    "f15: 검증 기준의 근거를 '디지털취약계층의 정보 접근 및 이용 편의 증진을 위한 고시'로 적고, '위반은 장애인 차별에 해당한다'를 '차별행위로 인정되면 시정권고와 3천만 원 이하 과태료 대상이 된다'로 고친다 — 정책브리핑 원문 표현과 맞춘다. 용어 후보 '무인정보단말기 접근성'의 정의에도 소규모 시설의 대체 수단 허용을 덧붙여 같은 기준으로 맞춘다.",
    "f16: 조문 인용에 기준(법률 제16320호, 2019-07-17 시행)을 명시한다 — 현행 조문 여부는 국가법령정보센터에서 확인하지 못했다.",
    "f14: 13절 각주 정의에서 ref-1276의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-1276 항목에 source_unopened: true 를 넣는다 — ISO 페이지 403으로 검색 결과 요약만 확인했다.",
    "f22: 10절에서 56. 운영 이관·확대·교육 연결의 근거를 f8 하나로 적는다 — f2가 삭제됐다.",
    "5절 적용 사례: 현장 유형을 물류창고(f3·f4·f5), 병원(f8 미국, f9 한국), 실외(f12·f13)로 나눠 쓴다. f10·f11(돌봄)은 출처가 현장 유형을 하나로 밝히지 않으므로 5절 사례로 세우지 말고 4·6절(수용성 측정 모델)에 둔다. 제조 공장·상업 시설·가정 사례는 찾지 못했다고 명시한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 21건, 미확인 1건, 교차 확인 0건. 강등: f7 사실 → 추정(보고서 수치가 기사 한 곳 기준), f9 사실 → 추정(병원 자체 조사를 전한 단일 기사). 삭제: f2(EU-OSHA 게시 페이지가 위험 목록·참여 권고를 뒷받침하지 않음). 원문 미열람 출처: ref-1276(ISO/IEC Guide 71, 검색 결과로만 확인). 주의: 물류창고 부상 수치(f3)는 논문 원문이 아니라 저자 소속 대학 발표 기준이다. 병원 만족도(f9)는 기관 자체 설문이다. 노사협의·공동결정 조문이 로봇 오케스트레이션의 작업자 데이터 기록에 적용되는지(f18), 화면 접근성 의무가 로봇 화면에 적용되는지는 법적으로 판단되지 않았다. 제조 공장·상업 시설·가정 사례는 확인하지 못했다. ref-1264는 이번 검증에서 직접 열리지 않아(307) 같은 보도문의 재게재와 검색 결과로 확인했다. 같은 대학의 후속 보도(2026-08, 로봇 창고 표지판·부상 관련)가 검색되었으나 열지 못해 반영하지 않았으며, 다음 갱신 실행의 확인 대상이다. 기존 열린 질문 oq-146·oq-188·oq-266은 해결로 인정하지 않는다(해결 제안 없음). 정정 요청 없음. 검증 검색 3회(리서치 20회와 합쳐 23/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-24/pages.json

```json
{
  "run_id": "2026-09-30-24",
  "outline": [
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1100,
      "summary": "로봇 도입의 수용에는 한 가지 답이 없고, 일하는 사람 쪽은 작업 흐름 적합성·작업 속도·데이터 감시·고용 효과가, 이용하는 사람 쪽은 사회적 상호작용과 보행 약자의 공간·접근성이 수용을 가르는 것으로 보인다. [추정][^ref-1151][^ref-1264][^ref-1278][^ref-1275][^ref-1266]",
      "planned_findings": [
        "f19",
        "f3",
        "f6",
        "f7",
        "f9",
        "f12",
        "f20"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "알메러 모델은 UTAUT에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명한다. [사실][^ref-1269] 노사협의회 협의 사항·감시 장치 공동결정·무인정보단말기 접근성·연석 경사로가 이 영역의 핵심 용어다.",
      "planned_findings": [
        "f10",
        "f11",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1600,
      "summary": "물류창고(부상 재분배·데이터 감시), 병원(미국 TUG 민족지, 한국 병원 자체 설문), 실외(보도 로봇과 휠체어 이용자) 사례를 여섯 항목으로 정리했다. 물류창고 수행 자원 칸은 작업자의 협업 요구(f5)만 둔다. 제조 공장·상업 시설·가정 사례는 찾지 못했다.",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f8",
        "f9",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 900,
      "summary": "수용성 측정 모델(알메러 모델, Q방법론), 참여 설계, 직무 설계, 노동자 참여 절차가 대표 접근법이다. 돌봄 연구의 전용 가능성 판단은 구축자 의견으로 밝히고 각주는 사실 부분에만 건다. [사실][^ref-1269][^ref-1273]",
      "planned_findings": [
        "f10",
        "f11",
        "f12",
        "f4",
        "f16",
        "f17",
        "f18"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "이 영역과 관련된 규정으로 ISO/IEC Guide 71:2014, 무인정보단말기 접근성 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조를 확인했다. [사실][^ref-1276][^ref-1268][^ref-1272][^ref-1271]",
      "planned_findings": [
        "f14",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "EU-OSHA 보고서, 창고 부상 연구, 창고 작업자 면담, 미국·한국 로봇 고용 효과 연구, 병원 로봇 민족지, 알메러 모델, 보도 로봇 공동설계 연구가 대표 자료다. [사실][^ref-1277][^ref-1264][^ref-1275]",
      "planned_findings": [
        "f1",
        "f3",
        "f5",
        "f6",
        "f7",
        "f8",
        "f10",
        "f12"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 800,
      "summary": "ROP는 작업 분담·속도 조정, 작업자 통제 수단, 보행 약자 양보 대기 규칙, 화면 접근성을 맡고, 고용 정책·노사 절차·법적 적합성 판단·로봇 본체 설계는 외부와 연계하는 것으로 보인다. [추정][^ref-1264][^ref-1278][^ref-1265][^ref-1268]",
      "planned_findings": [
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1000,
      "summary": "이 영역은 작업 분담·속도로 25. 작업 배정 — MRTA와 31. 사람–로봇 협업, 부상으로 49. 사람 근접 안전, 작업자 데이터로 53. 개인정보·영상 데이터 등 15개 세부영역과 이어지는 것으로 보인다. [추정][^ref-1264][^ref-1265]",
      "planned_findings": [
        "f22"
      ]
    },
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "section": "11. 열린 질문",
      "budget_chars": 900,
      "summary": "기존 열린 질문 네 건(oq-146·oq-188·oq-266·oq-278)은 열림으로 두고, 로봇 화면의 접근성 의무, 작업자 데이터 기록의 노사협의 대상 여부, 속도 정책의 부상 완화, 국내 독립 수용성 연구에 관한 새 질문 네 건을 올렸다.",
      "planned_findings": [
        "f15",
        "f18",
        "f3",
        "f9"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "영역 심화: 3~11절 첫 작성(물류창고·병원·실외 적용 사례 4건, 수용성 모델·노동자 참여 절차·접근성 의무, 책임 경계, 연결 15개 영역, 열린 질문 8건), 각주 15건. 2차 수정: 6절 의견 주체 명시, 5절 물류창고 수행 자원 칸 드리프트 제거, 7절 도입 문장, 10절 요약 첫 문장"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"8. 대표 연구와 자료\" 절(1,290자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,060자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"11. 열린 질문\" 절(1,002자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"4. 핵심 개념과 용어\" 절(985자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(980자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"6. 대표 접근법과 기술\" 절(778자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"3. 왜 중요한가\" 절(762자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 60. 노동·수용성·접근성 | 영역 심화: 3~11절 첫 작성(물류창고·병원·실외 적용 사례, 수용성 모델·노동자 참여 절차·접근성 의무, 책임 경계), 출처 15건, 강등 2건·삭제 1건 반영, 2차 수정 4건 반영 | run 2026-09-30-24",
  "index_updates": {
    "home_recent": "2026-09-30 — 60. 노동·수용성·접근성: 3~11절 첫 작성(물류창고 부상 재분배·데이터 감시, 병원 로봇 수용, 보도 로봇과 휠체어 이용자 사례, 노사협의·공동결정·무인정보단말기 접근성 규정, 새 열린 질문 4건)",
    "category_recent": "2026-09-30 — 60. 노동·수용성·접근성: 영역 심화로 3~11절 첫 작성(적용 사례 4건, 관련 규정 4건, 책임 경계, 연결 15개 영역)",
    "area_recent": "2026-09-30 — 60. 노동·수용성·접근성: 3~11절 첫 작성, 출처 15건, 신뢰도 medium"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "utaut",
      "term_ko": "통합 기술 수용 이론",
      "term_en": "Unified Theory of Acceptance and Use of Technology (UTAUT)",
      "definition": "성과 기대·노력 기대·사회적 영향·촉진 조건으로 기술 사용 의도와 실제 사용을 설명하는 기술 수용 모델로, 로봇 수용성 연구의 출발점으로 쓰인다.",
      "description": "알메러 모델은 이 이론에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명한다(Heerink 외, 2010).",
      "related_areas": [
        60
      ],
      "sources": [
        "ref-1269"
      ]
    },
    {
      "action": "new",
      "slug": "almere-model",
      "term_ko": "알메러 모델",
      "term_en": "Almere Model",
      "definition": "UTAUT에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 로봇·에이전트 수용성을 측정하도록 만든 모델이다(Heerink 외, 2010).",
      "description": "요양시설과 가정에서 세 가지 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다.",
      "related_areas": [
        60,
        65
      ],
      "sources": [
        "ref-1269"
      ]
    },
    {
      "action": "new",
      "slug": "kiosk-accessibility",
      "term_ko": "무인정보단말기 접근성",
      "term_en": "Kiosk Accessibility (Unmanned Information Terminal Accessibility)",
      "definition": "키오스크 같은 무인정보단말기를 장애가 있는 사람도 동등하게 쓸 수 있게 하는 요건으로, 한국은 2026-01-28부터 모든 설치·운영 사업자에게 접근 가능한 기기 제공을 의무화했고 바닥면적 50㎡ 미만 시설·소상공인·테이블 주문형 기기에는 보조기기·보조 인력·호출벨 같은 대체 수단을 허용한다.",
      "description": "검증 기준은 '디지털취약계층의 정보 접근 및 이용 편의 증진을 위한 고시'를 따르며, 차별행위로 인정되면 시정권고와 3천만 원 이하 과태료 대상이 된다.",
      "related_areas": [
        60,
        59,
        37
      ],
      "sources": [
        "ref-1268"
      ]
    },
    {
      "action": "new",
      "slug": "curb-cut",
      "term_ko": "연석 경사로",
      "term_en": "Curb Cut (Curb Ramp)",
      "definition": "보도와 차도 사이 턱을 경사로로 낮춘 부분으로, 휠체어·유모차 이용자가 횡단할 때 지나야 하므로 로봇이 이곳에 멈추면 통행을 막는다.",
      "description": "배송 로봇이 연석 경사로에 멈춰 휠체어 이용자의 통행을 막은 사건이 보도 로봇 접근성 공동설계 연구(CHI 2024)의 출발점이었다.",
      "related_areas": [
        60,
        66,
        16,
        19
      ],
      "sources": [
        "ref-1265"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1264",
      "org": "George Mason University Costello College of Business",
      "title": "Warehouse automation hasn't made workers safer — it's just reshuffled risk",
      "published": "2025-08-26",
      "url": "https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Burtch·Greenwood·Ravindran 의 ILR Review 논문(DOI 10.1177/00197939251333754)을 소개하는 대학 발표. 아마존 로봇 센터의 중대 부상 40% 감소·비중대 부상 77% 증가를 전한다. 논문 원문은 미열람.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1265",
      "org": "Han, H. Z. 외 (Carnegie Mellon University) — CHI '24",
      "title": "Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations",
      "published": "2024-04-07",
      "url": "https://arxiv.org/abs/2404.05050",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "이동장애인 15명·로봇 실무자 8명 면담과 공동설계 워크숍 4회로 보도 로봇의 접근성 문제와 설계안을 도출한 CHI 2024 논문.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1266",
      "org": "한국경제",
      "title": "로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인)",
      "published": "2025-04-01",
      "url": "https://www.hankyung.com/article/2025040138391",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국노동연구원 '기술 혁신과 노동시장 변화' 보고서의 로봇 노출도별 임금·고용 효과 수치를 전한 기사.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1267",
      "org": "한국노동연구원 (국회 정책정보 포털 NABIS 게재)",
      "title": "기술 혁신과 노동시장 변화",
      "published": "2024-12",
      "url": "https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자동화·로봇 도입·AI 가 지역 고용과 인적자본에 주는 영향을 분석한 한국노동연구원 보고서(2024-12)의 소개 페이지. 세부 수치는 페이지에 없다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1268",
      "org": "대한민국 정책브리핑 (보건복지부)",
      "title": "장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행",
      "published": "2026-01-28",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958690",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "2026-01-28부터 모든 무인정보단말기 설치·운영 사업자에게 장애인 접근성 기기 제공을 의무화하고 소규모 시설의 대체 수단을 허용한 조치를 알린 보도자료.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1269",
      "org": "Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics)",
      "title": "Assessing acceptance of assistive social agent technology by older adults: the Almere model",
      "published": "2010",
      "url": "https://doi.org/10.1007/s12369-010-0068-5",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "UTAUT 에 사회적 상호작용 변수를 더한 고령자용 보조 소셜 에이전트 수용성 모델(Almere 모델)을 제안·검증한 논문. 초록 기준.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1151",
      "org": "Mutlu, B., Forlizzi, J. (HRI 2008)",
      "title": "Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction",
      "published": "2008",
      "url": "https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "병원 자율 배송 로봇 TUG 도입을 민족지로 조사해 병동별 작업 흐름·방해 허용도·환경이 수용과 저항을 가른다는 점을 보인 논문.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1271",
      "org": "Bundesministerium der Justiz (gesetze-im-internet.de)",
      "title": "Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte",
      "published": null,
      "url": "https://www.gesetze-im-internet.de/betrvg/__87.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "독일 사업장조직법 제87조. 노동자 행동·성과 감시용 기술 장치의 도입·적용에 대한 사업장협의회 공동결정권(제1항 제6호)과 중재위원회 결정(제2항)을 정한다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1272",
      "org": "대한민국 국회 (법률 제16320호, 케이스노트 게재)",
      "title": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항)",
      "published": "2019-04-16",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "노사협의회 협의 사항(채용·배치·교육훈련, 신기계·기술 도입, 근로자 감시 설비 설치 등)을 정한 조문. 법률 제16320호(2019-07-17 시행) 기준이며 현행 조문 여부는 국가법령정보센터에서 확인하지 못했다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1273",
      "org": "김소라 (주관성 연구, 한국주관성연구학회)",
      "title": "돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구",
      "published": "2023",
      "url": "https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 분류한 국내 논문. KCI 초록 기준.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1274",
      "org": "의협신문",
      "title": "\"로봇이 병원을 돌아다닌다\"…의료서비스로봇 5만건 돌파",
      "published": "2025-01-21",
      "url": "https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한림대성심병원의 의료서비스로봇 11종 77대 도입·사용 5만 건과 간호사·입원환자 만족도 조사 결과를 전한 기사(병원 자체 조사 기반).",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1275",
      "org": "Acemoglu, D., Restrepo, P. (NBER)",
      "title": "Robots and Jobs: Evidence from US Labor Markets",
      "published": "2017-03",
      "url": "https://www.nber.org/papers/w23285",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "1990~2007년 미국 통근권역 자료로 산업용 로봇이 고용과 임금을 낮춘다고 추정한 NBER 작업논문(2020년 Journal of Political Economy 게재).",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1276",
      "org": "ISO/IEC",
      "title": "ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards",
      "published": "2014-12",
      "url": "https://www.iso.org/standard/57385.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 표준 개발자가 장애인·어린이·고령자의 접근성 요구를 표준에 반영하도록 돕는 지침(2판). ISO 페이지 403 으로 검색 결과 요약만 확인.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1277",
      "org": "European Agency for Safety and Health at Work (EU-OSHA)",
      "title": "Advanced robotics and automation: implications for occupational safety and health",
      "published": "2022-06-16",
      "url": "https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "협업 가능한 로봇 시스템의 확산이 노동자의 안전·건강·웰빙에 주는 영향을 다룬 EU-OSHA 보고서의 게시 페이지. 보고서 PDF 본문은 읽히지 않았다.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1278",
      "org": "Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics)",
      "title": "Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety",
      "published": "2026",
      "url": "https://doi.org/10.1007/s12369-026-01359-1",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "창고 작업자 12명 면담으로 로봇 운영의 데이터 감시 우려와 작업자 중심 요구(수동 무시·개인정보 통제·감시 알림)를 정리한 논문. 초록 기준.",
      "cited_by": [
        "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가?",
      "areas": [
        60,
        59,
        64
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가?",
      "areas": [
        60,
        53,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가?",
      "areas": [
        60,
        31,
        25
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가?",
      "areas": [
        60,
        63,
        61
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#5-적용-사례-현장-유형-명시",
      "title": "60. 노동·수용성·접근성"
    }
  ],
  "standards_updates": [
    {
      "name": "ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판)",
      "kind": "표준",
      "org": "ISO/IEC",
      "url": "https://www.iso.org/standard/57385.html",
      "related_areas": [
        60
      ],
      "summary": "사람이 쓰는 제품·서비스·건축 환경을 다루는 표준에 접근성 요구를 넣도록 표준 개발자에게 지침을 주며 장애인·어린이·고령자의 접근성 요구를 주로 다룬다(원문 미열람).",
      "ref_id": "ref-1276"
    },
    {
      "name": "장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행)",
      "kind": "프레임워크",
      "org": "보건복지부",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148958690",
      "related_areas": [
        60,
        59,
        37
      ],
      "summary": "모든 무인정보단말기 설치·운영 사업자에게 '디지털취약계층의 정보 접근 및 이용 편의 증진을 위한 고시'의 검증 기준을 충족하는 장애인 접근 가능 기기 제공을 의무화하고, 소규모 시설에는 대체 수단을 허용한다.",
      "ref_id": "ref-1268"
    },
    {
      "name": "근로자참여 및 협력증진에 관한 법률 제20조(협의 사항)",
      "kind": "프레임워크",
      "org": "대한민국 국회",
      "url": "https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0",
      "related_areas": [
        60,
        53,
        59
      ],
      "summary": "신기계·기술 도입과 사업장 내 근로자 감시 설비 설치 등을 노사협의회 협의 사항으로 둔다(법률 제16320호, 2019-07-17 시행 기준).",
      "ref_id": "ref-1272"
    },
    {
      "name": "독일 사업장조직법(BetrVG) 제87조 공동결정권",
      "kind": "프레임워크",
      "org": "Bundesministerium der Justiz",
      "url": "https://www.gesetze-im-internet.de/betrvg/__87.html",
      "related_areas": [
        60,
        53,
        59
      ],
      "summary": "노동자의 행동·성과 감시용 기술 장치의 도입·적용에 사업장협의회 공동결정권을 두고, 합의가 안 되면 중재위원회가 결정한다.",
      "ref_id": "ref-1271"
    }
  ],
  "additional_research_requests": [
    "5. 적용 사례: 제조 공장·상업 시설·가정 현장의 노동 영향·수용성·접근성 사례가 없다. 현장 유형 균형을 위해 이 세 현장 유형의 근거를 조사해야 한다.",
    "5절 물류창고 수행 자원 칸: 로봇 센터에서 로봇과 작업자가 작업을 어떻게 나누는지(상품-대-사람 방식 등)는 브리프에 없어 2차 지시로 뺐다. 분담 구조를 밝힌 출처를 조사해야 한다.",
    "3·5절 물류창고 부상 수치(f3): ILR Review 논문 원문과 데이터 출처를 열어 대학 발표 기준을 논문 기준으로 바꾸고, 검증 노트가 언급한 같은 대학의 2026-08 후속 보도(로봇 창고 표지판·부상)를 확인해야 한다.",
    "6절: 돌봄·고령자 대상 수용성 모델(알메러 모델 등)을 물류창고·병원 종사자 수용성에 적용·검증한 연구가 있는지 조사해야 구축자 의견을 근거 있는 서술로 바꿀 수 있다.",
    "8절: 한국노동연구원 '기술 혁신과 노동시장 변화' 보고서 원문에서 로봇 노출도별 임금·고용 수치와 저자를 확인해야 [추정]을 [사실]로 올릴 수 있다.",
    "3·6절: 삭제된 f2를 대신할 근거로 EU-OSHA 보고서 PDF 본문의 심리사회적 위험과 권고 내용을 원문에서 확인해야 한다.",
    "4·7절: 근로자참여법 제20조가 현행 조문과 같은지 국가법령정보센터에서 확인해야 한다.",
    "5·6절과 oq-188: 국내 보도 배송·순찰 로봇의 대기 위치·점자블록 기준과, 시각장애인과 공공 로봇 현장 연구(ACM 2026, DOI 10.1145/3776734.3794493)를 조사해야 한다.",
    "7절: ISO/IEC Guide 71:2014 원문을 열어 로봇 서비스에 적용할 수 있는 요구 항목을 확인해야 한다."
  ],
  "fixes_applied": [
    "f2 삭제 — 3·6·8절과 10절 연결 근거 어디에도 f2를 쓰지 않았고, 6절 '노동자 참여 절차'는 f16·f17·f18(ref-1272·ref-1271·ref-1278)로만 썼다.",
    "f3 출처 기준 명시 — 3절과 5절 물류창고 표(제약·예외·성과 칸)에 '논문 원문이 아니라 저자 소속 대학(GMU) 발표 기준'을 넣고 8절에도 '저자 소속 대학 발표 기준'을 밝혔다.",
    "f4 의견 주체 명시 — 5절 물류창고 서술에 'Burtch·Greenwood·Ravindran 연구진의 해석으로는 …'으로 [의견] 문장의 주체를 밝혔고, 6절 직무 설계에서도 '물류창고 부상 연구진은 … 해석한다'로 썼다.",
    "f7 강등 — 3절과 8절의 한국 수치 문장을 [추정]으로 쓰고 '한국경제 보도 2025-04-01 기준, 보고서 원문 미확인'을 병기했으며, 보고서의 존재·발행(한국노동연구원, 2024-12)만 ref-1267로 [사실] 서술했다.",
    "f9 강등 — 5절 병원(한국) 사례의 표 칸을 모두 [추정]으로 쓰고 표 아래에 '병원 자체 만족도 조사, 의협신문 보도(2025-01-21) 기준, 조사 방법 비공개, 다른 보도는 병동 간호사 99명(91.9%)으로 표본이 다름'을 밝혔다.",
    "f13 수정 — '스스로 비켜 주차' 구절을 넣지 않았고, 5절 실외 서술에서 경로 재계획 제안의 주체를 '로봇 실무자 참여자 한 명'으로 썼다.",
    "f15 수정 — 7절 표에 검증 기준 근거 '디지털취약계층의 정보 접근 및 이용 편의 증진을 위한 고시'와 '차별행위로 인정되면 시정권고와 3천만 원 이하 과태료 대상'을 썼고, 용어집 '무인정보단말기 접근성' 정의에 소규모 시설의 대체 수단 허용을 덧붙였다.",
    "f16 기준 명시 — 4·6·7절의 조문 서술에 '법률 제16320호, 2019-07-17 시행 기준'을 넣고 7절에는 현행 조문 여부 미확인을 밝혔다.",
    "f14 미열람 표시 — 13절 ref-1276 각주의 접근일 뒤에 ' (원문 미열람)'을 붙이고 7절 표 출처 칸에도 원문 미열람을 적었으며, reference_updates 의 ref-1276 항목에 source_unopened: true 를 넣었다.",
    "f22 수정 — 10절에서 56. 운영 이관·확대·교육 연결의 근거를 f8(ref-1151) 하나로만 적었다.",
    "5절 구성 — 현장 유형을 물류창고(f3·f4·f5), 병원(f8 미국, f9 한국), 실외(f12·f13)로 나눠 썼고, f10·f11(돌봄)은 4·6절 수용성 측정 모델에만 두었으며, 5절 첫머리에 제조 공장·상업 시설·가정 사례를 찾지 못했다고 명시했다.",
    "2차: 6절 돌봄 연구 전용 가능성 문장 — 사실 부분('두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다')을 따로 떼어 [사실][^ref-1269][^ref-1273]을 걸고, 전용 가능성 판단은 '이 위키 구축자의 의견'으로 주체를 밝혀 각주 없이 [의견]만 붙였다(원래 절을 고쳤으므로 재분리 시 분리 페이지에도 반영된다).",
    "2차: 5절 물류창고 수행 자원 칸 — '작업자가 로봇과 함께 피킹을 맡는다' 작업 분담 서술(ref-1264)을 빼고, 피킹 목표량은 이미 제약 칸에 있으므로 f5의 '창고 작업자는 로봇 운영에서 더 주체적인 협업을 요구했다. [사실][^ref-1278]'만 두었다.",
    "2차: 7절 — 표 앞에 ISO/IEC Guide 71:2014, 무인정보단말기 접근성 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조 네 규정을 밝히는 도입 문장을 [사실][^ref-1276][^ref-1268][^ref-1272][^ref-1271]로 두고, ISO/IEC Guide 71:2014를 원문 미열람으로 확인했다는 문장을 덧붙였다(ref-1276 각주의 원문 미열람 표기 유지).",
    "2차: 10절 — 첫 문장을 연결되는 세부영역 15개를 번호와 이름으로 요약하는 문장으로 바꾸고 f22의 [추정] 태그와 각주(ref-1264·ref-1278·ref-1265·ref-1151·ref-1268·ref-1272·ref-1271·ref-1275·ref-1266·ref-1274, 삭제된 f2의 ref-1277 제외)를 붙였으며, 기존 '아래 연결은 … 추정이다' 문장은 둘째 문장으로 옮겼다.",
    "분량 초과 자동 분리: 60. 노동·수용성·접근성 본문 9,680자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,542자"
  ]
}
```

### runs/2026-09-30-24/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area60-s8.md (1,290자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area60-s7.md (1,060자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area60-s11.md (1,002자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area60-s4.md (985자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area60-s10.md (980자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area60-s6.md (778자)
    - docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area60-s3.md (762자)
```

### runs/2026-09-30-24/pages/categories/governance-law-and-society/labor-acceptance-and-accessibility.md

```markdown
---
title: "60. 노동·수용성·접근성"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [기술 수용 모델, 노동자 참여, 근로자 감시 설비, 무인정보단말기 접근성, 연석 경사로]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1264, ref-1265, ref-1266, ref-1267, ref-1268, ref-1269, ref-1151, ref-1271, ref-1272, ref-1273, ref-1274, ref-1275, ref-1276, ref-1277, ref-1278]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 60. 노동·수용성·접근성

# 60. 노동·수용성·접근성

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]

## 3. 왜 중요한가

로봇 도입이 받아들여지는지에는 한 가지 답이 없으며, 일하는 사람 쪽에서는 작업 흐름 적합성, 작업 속도와 직무 설계, 데이터 감시, 고용과 숙련 효과가 수용 여부를 가르는 것으로 보인다. [추정][^ref-1151][^ref-1264][^ref-1278][^ref-1275][^ref-1266] 이용하는 사람 쪽에서는 사회적 상호작용 요인과 보행 약자의 공간·접근성이 같은 역할을 하는 것으로 보인다. [추정][^ref-1269][^ref-1273][^ref-1265][^ref-1268]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 왜 중요한가](../../topics/2026/2026-09-30-area60-s3.md)에 있다.

## 4. 핵심 개념과 용어

**알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1269]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area60-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 근거를 찾은 현장 유형은 물류창고·병원·실외다. 제조 공장·상업 시설·가정 현장의 노동·수용성·접근성 사례는 찾지 못했다. 돌봄 로봇 수용성 연구(4·6절)는 출처가 현장 유형을 하나로 밝히지 않아 사례로 세우지 않았다.

**현장 유형:** 물류창고

**사례:** 로봇을 도입한 물류창고의 피킹 작업(흐름 단계: 피킹)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇 운영에 딸려 수집되는 작업자 데이터가 작업자의 데이터 감시 우려 대상이 된다. [사실][^ref-1278] |
| 수행 자원 | 창고 작업자는 로봇 운영에서 더 주체적인 협업을 요구했다. [사실][^ref-1278] |
| 제약 | 작업자 온라인 게시글에서는 로봇 센터의 피킹 목표량이 2~3배 높다는 진술이 나왔다(GMU 발표 기준). [사실][^ref-1264] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 로봇 센터는 기존 센터보다 중대 부상이 40% 적고 비중대 부상이 77% 많았다(논문 원문이 아니라 GMU 발표 기준). [사실][^ref-1264] |

이 사례는 서로 다른 두 연구를 묶었다. Burtch·Greenwood·Ravindran 연구진의 해석으로는 자동화가 위험 작업을 없애는 대신 남은 작업의 다양성을 줄이고 작업 속도를 높여 반복성 긴장 손상 같은 비중대 부상을 늘리므로, 위험이 사라지기보다 재분배되며 직무 설계로 대응해야 한다. [의견][^ref-1264] 창고 작업자 12명 반구조화 면담 연구는 수동 무시(override)·개인정보 통제·감시 활동 알림 같은 작업자 중심 요구를 제시했다(2026). [사실][^ref-1278]

**현장 유형:** 병원

**사례:** 병동에 물품을 배송하는 자율 배송 로봇 TUG 도입(미국, 2008 연구)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 자율 배송 로봇이 병동으로 배송하는 물품 [사실][^ref-1151] |
| 수행 자원 | 자율 배송 로봇 TUG와 병동 직원 [사실][^ref-1151] |
| 제약 | 내과 병동은 방해에 대한 허용도가 낮았고 붐비는 통로에서 로봇 운행이 멈췄다. [사실][^ref-1151] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 내과 병동에서는 로봇이 작업 흐름을 해치고 직원 저항을 불렀지만, 산후 병동은 로봇을 작업 흐름과 사회적 맥락에 통합했다. [사실][^ref-1151] |

같은 로봇이라도 병동의 작업 흐름, 방해 허용도, 인식된 비용과 이득의 불일치, 통로 환경에 따라 수용과 저항이 갈렸다. [사실][^ref-1151]

**현장 유형:** 병원

**사례:** 병동 의료서비스로봇 운영(한국 한림대성심병원, 2022-08~2024-12)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 간호사의 단순업무와 입원환자 대상 영상 안내 [추정][^ref-1274] |
| 수행 자원 | 의료서비스로봇 11종 77대와 간호사 [추정][^ref-1274] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 누적 51,092건을 사용했고, 간호사 109명 가운데 90% 이상이 단순업무 경감, 94%가 계속 사용 희망, 입원환자 147명 가운데 93.9%가 영상 안내가 도움이 됐고 99%가 로봇에 거부감이 없다고 답했다. [추정][^ref-1274] |

이 수치는 병원 자체 만족도 조사이며 의협신문 보도(2025-01-21) 기준이다. 조사 방법은 공개되지 않았고, 다른 보도는 표본을 병동 간호사 99명(91.9%)으로 적어 간호사 109명 표본과 다르다. [추정][^ref-1274]

**현장 유형:** 실외

**사례:** 보도에서 운행하는 배송 로봇과 휠체어 이용자의 통행(미국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇과 보행 약자가 함께 쓰는 보도 공간 [사실][^ref-1265] |
| 수행 자원 | 보도 배송 로봇과 그 운영 업체 [사실][^ref-1265] |
| 제약 | 이동장애인은 로봇이 들어오면 보도 공간을 두고 경쟁해야 한다고 느꼈다. [사실][^ref-1265] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 배송 로봇이 연석 경사로에 멈춰 횡단한 휠체어 이용자의 통행을 막았고, 이용자가 이를 공개하자 업체가 로봇 운행을 잠시 중단했다. [사실][^ref-1265] |

이동장애인 15명과 로봇 실무자 8명 면담, 공동설계 워크숍 4회로 진행한 연구(CHI 2024)에서 로봇 실무자 참여자 한 명은 연석 경사로로 다가오는 사람을 감지하면 로봇이 자동으로 경로를 다시 계획하는 기능을 제안했다. [사실][^ref-1265] 국내에서 같은 문제를 다루는 대기 위치 기준은 확인되지 않았다([oq-188](../../open-questions.md)).

## 6. 대표 접근법과 기술

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1269] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1273] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1269][^ref-1273]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area60-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1276][^ref-1268][^ref-1272][^ref-1271] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area60-s7.md)에 있다.

## 8. 대표 연구와 자료

EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1277]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 연구와 자료](../../topics/2026/2026-09-30-area60-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 로봇과 사람의 작업 분담과 작업 속도(목표량) 설정을 드러내고 조정할 수 있게 하고, 작업자 데이터 수집 범위 표시·감시 알림·수동 무시 같은 작업자 통제 수단을 제공하는 것으로 보인다. [추정][^ref-1264][^ref-1278] | 고용·임금·재교육 정책, 노사협의·공동결정 절차와 근로자 감시 설비의 적법성 판단(사업주·노동자 대표·법무)이 연계 대상으로 보인다. [추정][^ref-1272][^ref-1271][^ref-1266] |
| 업종별 조건 | 연석 경사로·통로에서 보행 약자에게 양보하고 멈추지 않는 대기 위치 규칙을 경로·작업 제약으로 반영하고, 운영자·이용자 화면의 접근성을 갖추는 것으로 보인다. [추정][^ref-1265][^ref-1268] | 장애인차별금지법 등 접근성 법적 적합성 판단(운영자·법무)이 연계 대상으로 보인다. [추정][^ref-1268] |
| 로봇 자체 지능·제어 | 제조사 설계를 전제로 대기·양보 조건을 작업·경로 제약으로 로봇에 전달하는 것으로 보인다. [추정][^ref-1265] | 로봇 본체의 물리적 접근성 설계(높이·음성 조작 등)는 제조사의 몫으로 보인다. [추정][^ref-1265] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

이 영역에서 ROP는 법적 판단을 하지 않고, 외부에서 정한 결정을 작업·경로·권한 제약과 화면 설계로 받아 반영하며 그 근거 기록을 제공하는 쪽으로 보인다. [추정][^ref-1272][^ref-1271][^ref-1268][^ref-1265][^ref-1266] 경계 전체는 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 작업 분담·속도로 25. 작업 배정 — MRTA와 31. 사람–로봇 협업, 부상으로 49. 사람 근접 안전, 작업자 데이터 감시로 53. 개인정보·영상 데이터, 보행 약자와 대기 위치로 19. 사람·보행자 모델과 16. 장소 의미·지도 관리, 목표량 지표로 39. 운영 성과 측정·개선, 도입 절차로 56. 운영 이관·확대·교육, 화면 접근성으로 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반, 법 의무로 59. 법·규제·보험·라이선스, 효과 추정으로 3. 경제성·조달·사업 모델, 적용 현장으로 61. 물류창고·63. 병원·의료·66. 실외와 이어지는 것으로 보인다. [추정][^ref-1264][^ref-1278][^ref-1265][^ref-1151][^ref-1268][^ref-1272][^ref-1271][^ref-1275][^ref-1266][^ref-1274]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area60-s10.md)에 있다.

## 11. 열린 질문

**oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 열린 질문](../../topics/2026/2026-09-30-area60-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
[^ref-1271]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1272]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1273]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1274]: 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파, 2025-01-21, https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208, 접근일 2026-09-30
[^ref-1275]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1276]: ISO/IEC, ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards, 2014-12, https://www.iso.org/standard/57385.html, 접근일 2026-09-30 (원문 미열람)
[^ref-1277]: European Agency for Safety and Health at Work (EU-OSHA), Advanced robotics and automation: implications for occupational safety and health, 2022-06-16, https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health, 접근일 2026-09-30
[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30
```

### docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md

```markdown
---
title: "60. 노동·수용성·접근성"
type: area
category: "P. 거버넌스·법규·사회"
area_no: 60
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [P. 거버넌스·법규·사회](index.md) › 60. 노동·수용성·접근성

# 60. 노동·수용성·접근성

!!! info "소속 대분류"
    [P. 거버넌스·법규·사회](index.md) — 핵심 질문:
    여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **노동 영향·사회적 수용성**: 일자리와 일하는 방식의 변화, 로봇에 대한 사회적 수용성을 다룬다
- **접근성·포용**: 고령자·장애인·어린이도 로봇 서비스를 안전하게 쓰고 피할 수 있게 한다

## 2. 핵심 질문

로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]

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

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s8.md

```markdown
---
title: "60. 노동·수용성·접근성 — 대표 연구와 자료"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1151, ref-1264, ref-1265, ref-1266, ref-1267, ref-1269, ref-1275, ref-1277, ref-1278]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#8
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 대표 연구와 자료

# 60. 노동·수용성·접근성 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1277]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- EU-OSHA(유럽 산업안전보건청), Advanced robotics and automation: implications for occupational safety and health(2022-06-16) — 사람과 협업할 수 있는 로봇 시스템의 확산이 노동자의 안전·건강·웰빙과 고용 조건에 주는 영향을 다룬 보고서다. [사실][^ref-1277]
- Burtch·Greenwood·Ravindran, ILR Review(2025) — 로봇 풀필먼트 센터의 부상 구성 변화를 분석했다(5절 물류창고 사례, 저자 소속 대학 발표 기준). [사실][^ref-1264]
- Malik·Brandão·Coopamootoo, Towards Worker-Centered Warehouse Robots(International Journal of Social Robotics, 2026) — 창고 작업자 면담으로 데이터 감시 우려와 작업자 중심 요구를 정리했다. [사실][^ref-1278]
- Acemoglu·Restrepo, Robots and Jobs(NBER 작업논문 w23285, 2017-03; Journal of Political Economy 2020 게재) — 1990~2007년 미국 통근권역 자료로 노동자 1천 명당 로봇 1대가 늘면 고용률이 약 0.18~0.34%p, 임금이 0.25~0.5% 낮아진다고 추정했다. [사실][^ref-1275]
- 한국노동연구원, 기술 혁신과 노동시장 변화(2024-12) — 자동화·로봇 도입·AI가 지역 고용과 인적자본에 주는 영향을 분석한 보고서다. [사실][^ref-1267] 이 보고서를 전한 보도에 따르면 노동자 1천 명당 로봇 6.6대 증가(로봇 노출도 한 단계)마다 고숙련 제조업 노동자 임금은 2.5%, 고용률은 0.55%p 올랐고, 저숙련 제조업 노동자 임금은 4.5~4.9% 줄었으며 45~54세 고용률은 0.37%p 낮아졌다(한국경제 보도 2025-04-01 기준, 보고서 원문 미확인). [추정][^ref-1266]
- Mutlu·Forlizzi, Robots in Organizations(HRI 2008) — 병원 자율 배송 로봇의 수용과 저항이 병동의 작업 흐름·사회적·환경 요인에 따라 갈린다는 민족지 연구다(5절 병원 사례). [사실][^ref-1151]
- Heerink 외, Assessing acceptance of assistive social agent technology by older adults: the Almere model(2010) — 고령자용 수용성 측정 모델을 제안·검증했다(4·6절). [사실][^ref-1269]
- Han 외, Co-design Accessible Public Robots(CHI 2024) — 이동장애인과 로봇 실무자의 공동설계로 보도 로봇의 접근성 문제와 설계안을 도출했다(5절 실외 사례). [사실][^ref-1265]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1267]: 한국노동연구원 (국회 정책정보 포털 NABIS 게재), 기술 혁신과 노동시장 변화, 2024-12, https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1275]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1277]: European Agency for Safety and Health at Work (EU-OSHA), Advanced robotics and automation: implications for occupational safety and health, 2022-06-16, https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health, 접근일 2026-09-30
[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s7.md

```markdown
---
title: "60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1268, ref-1271, ref-1272, ref-1276]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#7
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스

# 60. 노동·수용성·접근성 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1276][^ref-1268][^ref-1272][^ref-1271] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역과 관련된 규정으로 접근성 지침 ISO/IEC Guide 71:2014, 장애인차별금지법에 따른 무인정보단말기 접근성 의무, 노사협의회 협의 사항을 정한 근로자참여 및 협력증진에 관한 법률 제20조, 감시 장치 공동결정을 정한 독일 사업장조직법 제87조의 네 가지를 확인했다. [사실][^ref-1276][^ref-1268][^ref-1272][^ref-1271] 이 가운데 ISO/IEC Guide 71:2014는 원문을 열지 못하고 검색 결과로만 확인했다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ISO/IEC Guide 71:2014 (2판, 2014-12) | 표준 | 사람이 쓰는 제품·서비스·건축 환경을 다루는 표준에 접근성 요구를 넣도록 표준 개발자에게 지침을 주며, 장애인·어린이·고령자의 접근성 요구를 주로 다룬다. [사실][^ref-1276] | ISO/IEC (원문 미열람) |
| 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) | 프레임워크 | 설치·운영 사업자는 '디지털취약계층의 정보 접근 및 이용 편의 증진을 위한 고시'의 검증 기준을 충족하는 장애인 접근 가능 기기를 제공해야 하고, 바닥면적 50㎡ 미만 시설·소상공인·테이블 주문형 기기는 호환 보조기기·소프트웨어, 보조 인력, 호출벨 같은 대체 수단을 쓸 수 있다. 차별행위로 인정되면 시정권고와 3천만 원 이하 과태료 대상이 된다. [사실][^ref-1268] | 보건복지부(정책브리핑) |
| 근로자참여 및 협력증진에 관한 법률 제20조 | 프레임워크 | 채용·배치 및 교육훈련, 신기계·기술 도입, 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다(법률 제16320호, 2019-07-17 시행 기준, 현행 조문 여부 미확인). [사실][^ref-1272] | 법령 게재 사이트 |
| 독일 사업장조직법 제87조 | 프레임워크 | 노동자 행동·성과 감시용 기술 장치의 도입·적용을 사업장협의회의 공동결정 대상으로 두고, 합의가 안 되면 중재위원회가 결정한다. [사실][^ref-1271] | 독일 연방법무부 법령 사이트 |

위 항목은 법적 적합성 판단의 근거가 아니라 이 영역이 참고하는 규정 목록이다. 법 적용 판단은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)와 이어진다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1271]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1272]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1276]: ISO/IEC, ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards, 2014-12, https://www.iso.org/standard/57385.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s11.md

```markdown
---
title: "60. 노동·수용성·접근성 — 열린 질문"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#11
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 열린 질문

# 60. 노동·수용성·접근성 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **oq-146** (상태: 열림) 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가? 이번 조사에서도 근거를 찾지 못했다.
- **oq-188** (상태: 열림) 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? 이번 조사는 해외 연석 경사로 사례(5절 실외)만 찾았다.
- **oq-266** (상태: 열림) 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? 이번 조사는 병동 단위의 수용 차이(5절 병원)만 찾았다.
- **oq-278** (상태: 열림) 로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가?
- (신규, 상태: 열림 · 실행 2026-09-30-24) 서비스 로봇 본체에 달린 터치스크린·주문 화면이나 운영자·이용자용 채팅 화면이 장애인차별금지법상 무인정보단말기에 해당해 접근성 의무를 지는가?
- (신규, 상태: 열림 · 실행 2026-09-30-24) 오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가?
- (신규, 상태: 열림 · 실행 2026-09-30-24) 로봇 도입 뒤 늘어난 작업 속도(피킹 목표량)와 비중대 부상 증가를 오케스트레이션의 작업 배정·속도 정책(휴식·작업 순환 반영)으로 줄인 사례나 연구가 있는가?
- (신규, 상태: 열림 · 실행 2026-09-30-24) 국내 병원·물류창고에서 로봇 도입 뒤 종사자 수용성과 직무 변화를 기관 자체 설문이 아닌 독립 연구로 조사한 자료가 있는가?

전체 목록은 [열린 질문](../../open-questions.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s4.md

```markdown
---
title: "60. 노동·수용성·접근성 — 핵심 개념과 용어"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1265, ref-1268, ref-1269, ref-1271, ref-1272, ref-1273, ref-1276]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#4
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 핵심 개념과 용어

# 60. 노동·수용성·접근성 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- **알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1269]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

- **알메러 모델(Almere Model)** — 통합 기술 수용 이론(Unified Theory of Acceptance and Use of Technology, UTAUT)에 사회적 상호작용 변수를 더해 고령자의 보조 소셜 에이전트 수용성을 설명하는 모델이다(Heerink 외, 2010). [사실][^ref-1269]
- **돌봄로봇 인식 유형** — Q방법론 연구는 노인 이용자·가족·돌봄서비스 종사자의 돌봄로봇 인식을 '불가피한 대체재', '상호보완적 동반자', '열등한 보조재', '불완전한 경쟁자'의 네 유형으로 나눴다(2023). [사실][^ref-1273]
- **노사협의회 협의 사항** — 한국 근로자참여 및 협력증진에 관한 법률 제20조 제1항은 근로자의 채용·배치 및 교육훈련(제2호), 신기계·기술의 도입 또는 작업 공정의 개선(제9호), 사업장 내 근로자 감시 설비의 설치(제14호)를 협의 사항으로 둔다(법률 제16320호, 2019-07-17 시행 기준). [사실][^ref-1272]
- **감시 장치 공동결정(Mitbestimmung)** — 독일 사업장조직법(Betriebsverfassungsgesetz, BetrVG) 제87조 제1항 제6호는 법률·단체협약 규정이 없는 한 노동자의 행동이나 성과를 감시하도록 정해진 기술 장치의 도입과 적용에 사업장협의회의 공동결정권을 두고, 합의가 안 되면 중재위원회(Einigungsstelle)가 결정하게 한다(2026-09-30 확인). [사실][^ref-1271]
- **무인정보단말기 접근성(Kiosk Accessibility)** — 한국에서는 2026-01-28부터 무인정보단말기를 설치·운영하는 모든 사업자가 장애인이 접근할 수 있는 기기를 제공해야 한다(세부 내용은 7절). [사실][^ref-1268]
- **연석 경사로(Curb Cut)** — 배송 로봇이 연석 경사로에 멈춰 휠체어 이용자의 통행을 막은 사건이 보도 로봇 접근성 공동설계 연구의 출발점이었다(2024). [사실][^ref-1265]
- **접근성 대상 집단** — ISO/IEC Guide 71:2014는 장애인·어린이·고령자의 접근성 요구를 주로 다룬다. [사실][^ref-1276]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1271]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1272]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1273]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1276]: ISO/IEC, ISO/IEC Guide 71:2014 Guide for addressing accessibility in standards, 2014-12, https://www.iso.org/standard/57385.html, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s10.md

```markdown
---
title: "60. 노동·수용성·접근성 — 다른 연구영역과의 연결"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1151, ref-1264, ref-1265, ref-1266, ref-1268, ref-1271, ref-1272, ref-1274, ref-1275, ref-1278]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#10
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 다른 연구영역과의 연결

# 60. 노동·수용성·접근성 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 작업 분담·속도로 25. 작업 배정 — MRTA와 31. 사람–로봇 협업, 부상으로 49. 사람 근접 안전, 작업자 데이터 감시로 53. 개인정보·영상 데이터, 보행 약자와 대기 위치로 19. 사람·보행자 모델과 16. 장소 의미·지도 관리, 목표량 지표로 39. 운영 성과 측정·개선, 도입 절차로 56. 운영 이관·확대·교육, 화면 접근성으로 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반, 법 의무로 59. 법·규제·보험·라이선스, 효과 추정으로 3. 경제성·조달·사업 모델, 적용 현장으로 61. 물류창고·63. 병원·의료·66. 실외와 이어지는 것으로 보인다. [추정][^ref-1264][^ref-1278][^ref-1265][^ref-1151][^ref-1268][^ref-1272][^ref-1271][^ref-1275][^ref-1266][^ref-1274]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 작업 분담·속도로 25. 작업 배정 — MRTA와 31. 사람–로봇 협업, 부상으로 49. 사람 근접 안전, 작업자 데이터 감시로 53. 개인정보·영상 데이터, 보행 약자와 대기 위치로 19. 사람·보행자 모델과 16. 장소 의미·지도 관리, 목표량 지표로 39. 운영 성과 측정·개선, 도입 절차로 56. 운영 이관·확대·교육, 화면 접근성으로 37. 관제 화면·실행 기록과 13. 대화형 기능의 신뢰·기반, 법 의무로 59. 법·규제·보험·라이선스, 효과 추정으로 3. 경제성·조달·사업 모델, 적용 현장으로 61. 물류창고·63. 병원·의료·66. 실외와 이어지는 것으로 보인다. [추정][^ref-1264][^ref-1278][^ref-1265][^ref-1151][^ref-1268][^ref-1272][^ref-1271][^ref-1275][^ref-1266][^ref-1274] 아래 연결은 모두 이번 조사의 발견 사항에서 도출한 추정이다.

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)·[31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 로봇과 사람의 작업 분담과 작업 속도가 부상과 수용을 좌우한다. [추정][^ref-1264]
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — 로봇 도입 뒤 부상 구성이 바뀐다. [추정][^ref-1264]
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 피킹 목표량 같은 성과 지표가 작업 강도와 이어진다. [추정][^ref-1264]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 작업자 데이터 감시 우려와 노동자 참여 절차가 걸린다. [추정][^ref-1278][^ref-1272][^ref-1271]
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)·[16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 보행 약자와 연석 경사로 같은 장소의 대기 위치 규칙이 필요하다. [추정][^ref-1265]
- [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) — 병동마다 작업 흐름 통합 정도가 달라 도입 절차가 수용에 영향을 준다. [추정][^ref-1151]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md)·[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 운영자·이용자 화면의 접근성 의무 적용 여부가 걸린다. [추정][^ref-1268]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 접근성 의무와 노사협의·공동결정 조문의 법 적용 판단이 이어진다. [추정][^ref-1268][^ref-1272][^ref-1271]
- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 로봇의 고용·임금 효과 추정이 도입 효과 평가의 배경이 된다. [추정][^ref-1275][^ref-1266]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md)·[63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)·[66. 실외](../../categories/site-type-applications/outdoor.md) — 5절 적용 사례가 놓인 현장 유형이다. [추정][^ref-1264][^ref-1278][^ref-1151][^ref-1274][^ref-1265]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1271]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1272]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1274]: 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파, 2025-01-21, https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208, 접근일 2026-09-30
[^ref-1275]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s6.md

```markdown
---
title: "60. 노동·수용성·접근성 — 대표 접근법과 기술"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1264, ref-1265, ref-1269, ref-1271, ref-1272, ref-1273, ref-1278]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#6
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 대표 접근법과 기술

# 60. 노동·수용성·접근성 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1269] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1273] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1269][^ref-1273]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 수용성 측정 모델

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1269] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1273] 두 연구는 요양시설·가정의 고령자와 돌봄 맥락에서 수행되었다. [사실][^ref-1269][^ref-1273] 그 결과를 물류창고·병원 운영 인력의 수용성에 그대로 옮길 수 있을지는 따로 확인해야 한다는 것이 이 위키 구축자의 의견이다. [의견]

### 참여 설계(co-design)

보도 로봇 연구는 이동장애인과 로봇 실무자가 함께 설계안을 도출하는 공동설계 워크숍을 썼다. [사실][^ref-1265] 실무자는 기업이 문제가 생긴 뒤에야 접근성을 다룬다고 인정했고, 두 집단 모두 처음부터 접근성을 통합해야 한다고 보았다(2024). [사실][^ref-1265]

### 직무 설계

물류창고 부상 연구진은 로봇 도입 뒤 남은 작업의 단조로움과 빠른 속도가 새 건강 위험을 만들므로 직무 설계로 대응해야 한다고 해석한다(5절 물류창고 사례). [의견][^ref-1264]

### 노동자 참여 절차

한국은 신기계·기술 도입과 근로자 감시 설비 설치를 노사협의회 협의 사항으로 두고(법률 제16320호, 2019-07-17 시행 기준), 독일은 노동자 감시용 기술 장치의 도입·적용을 사업장협의회의 공동결정 대상으로 둔다. [사실][^ref-1272][^ref-1271] 로봇 작업과 연결해 개별 작업자의 처리량·위치·행동 데이터를 남기는 오케스트레이션 기능은 이 절차의 대상으로 다뤄질 수 있어 도입 전에 노동자 참여 절차가 필요할 가능성이 있다. [추정][^ref-1278][^ref-1272][^ref-1271] 다만 해당 여부는 법적 판단으로 확인하지 못했고, 로봇·플랫폼 로그에 적용한 판례·행정해석도 찾지 못했다. [추정][^ref-1272][^ref-1271]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1271]: Bundesministerium der Justiz (gesetze-im-internet.de), Betriebsverfassungsgesetz § 87 Mitbestimmungsrechte, 미확인, https://www.gesetze-im-internet.de/betrvg/__87.html, 접근일 2026-09-30
[^ref-1272]: 대한민국 국회 (법률 제16320호, 케이스노트 게재), 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항), 2019-04-16, https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0, 접근일 2026-09-30
[^ref-1273]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-24/pages/topics/2026/2026-09-30-area60-s3.md

```markdown
---
title: "60. 노동·수용성·접근성 — 왜 중요한가"
type: topic
category: "P. 거버넌스·법규·사회"
primary_area_no: 60
related_areas: [3, 13, 16, 19, 25, 31, 37, 39, 49, 53, 56, 59, 61, 63, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1151, ref-1264, ref-1265, ref-1266, ref-1268, ref-1269, ref-1273, ref-1274, ref-1275, ref-1278]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#3
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 왜 중요한가

# 60. 노동·수용성·접근성 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 도입이 받아들여지는지에는 한 가지 답이 없으며, 일하는 사람 쪽에서는 작업 흐름 적합성, 작업 속도와 직무 설계, 데이터 감시, 고용과 숙련 효과가 수용 여부를 가르는 것으로 보인다. [추정][^ref-1151][^ref-1264][^ref-1278][^ref-1275][^ref-1266] 이용하는 사람 쪽에서는 사회적 상호작용 요인과 보행 약자의 공간·접근성이 같은 역할을 하는 것으로 보인다. [추정][^ref-1269][^ref-1273][^ref-1265][^ref-1268]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 도입이 받아들여지는지에는 한 가지 답이 없으며, 일하는 사람 쪽에서는 작업 흐름 적합성, 작업 속도와 직무 설계, 데이터 감시, 고용과 숙련 효과가 수용 여부를 가르는 것으로 보인다. [추정][^ref-1151][^ref-1264][^ref-1278][^ref-1275][^ref-1266] 이용하는 사람 쪽에서는 사회적 상호작용 요인과 보행 약자의 공간·접근성이 같은 역할을 하는 것으로 보인다. [추정][^ref-1269][^ref-1273][^ref-1265][^ref-1268] 기관이 직접 한 설문은 높은 만족도를 보고하지만, 같은 현장에서 노동자와 이용자의 수용성을 함께 측정한 연구는 이번 조사에서 찾지 못했다. [추정][^ref-1274]

로봇이 위험 작업을 맡아도 위험이 사라지지 않을 수 있다. 논문 원문이 아니라 저자 소속 대학(George Mason University)의 2025-08-26 발표 기준으로, 미국 아마존의 로봇 풀필먼트 센터는 기존 센터보다 중대 부상이 40% 적고 비중대 부상이 77% 많았다. [사실][^ref-1264]

고용 효과도 사람마다 다르게 나타난다. 미국 1990~2007년 자료로는 노동자 1천 명당 로봇 1대가 늘 때 고용률과 임금이 낮아진다는 추정이 있다(2017-03 작업논문). [사실][^ref-1275] 한국에서는 고숙련 제조업 노동자의 임금·고용은 오르고 저숙련 노동자의 임금은 줄었다는 보고서 내용이 보도되었다(한국경제 보도 2025-04-01 기준, 보고서 원문 미확인). [추정][^ref-1266]

이용하는 사람 쪽에서는 보도 로봇이 들어오면 이동장애인이 보도 공간을 두고 경쟁한다고 느낀다는 연구가 있다(2024). [사실][^ref-1265] ROP는 로봇과 사람의 작업 분담·속도, 작업자 데이터 기록, 로봇의 대기 위치를 정하는 자리에 있으므로 이 영역의 요구가 플랫폼 설계 요구로 돌아오는 것으로 보인다. [추정][^ref-1264][^ref-1278][^ref-1265][^ref-1268]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [56. 운영 이관·확대·교육](../../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1273]: 김소라 (주관성 연구, 한국주관성연구학회), 돌봄로봇에 대한 돌봄서비스 종사자와 사용자의 인식 유형 연구, 2023, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002970146, 접근일 2026-09-30
[^ref-1274]: 의협신문, "로봇이 병원을 돌아다닌다"…의료서비스로봇 5만건 돌파, 2025-01-21, https://www.doctorsnews.co.kr/news/articleView.html?idxno=158208, 접근일 2026-09-30
[^ref-1275]: Acemoglu, D., Restrepo, P. (NBER), Robots and Jobs: Evidence from US Labor Markets, 2017-03, https://www.nber.org/papers/w23285, 접근일 2026-09-30
[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-24 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-24 | 60. 노동·수용성·접근성 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1212건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 339개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [60] 에 걸린 4건 / 전체 283건)

```markdown
- oq-146 [열림] 국내 물류창고·병원·제조 공장에서 로봇 소음과 한국어 조건의 음성 지시 인식률과 오인식 시 확인 절차를 보고한 자료가 있는가(이번 조사에서 확인된 현장 사례는 네덜란드 슈퍼마켓 연구뿐이다)? (영역 13, 60, 61)
- oq-188 [열림] 국내 보도에서 배송·순찰 로봇이 횡단 대기 중 연석 경사로·점자블록을 막지 않도록 하는 대기 위치 규칙이나 접근성 기준(인증 항목·지침)이 있는가? (영역 66, 60, 16)
- oq-266 [열림] 로봇 운영 책임을 전담 운영 조직(커맨드센터), 사용 부서, 시설·IT 부서 가운데 어디에 두는 것이 역할 모호성과 사용 저항을 줄이는지 비교한 연구가 있는가? (영역 40, 56, 60)
- oq-278 [열림] 로봇 관제 요원·운영 인력의 직무 역량과 교육 과정을 정한 국가직무능력표준(NCS)이나 공개 교육 표준이 있는가? (영역 56, 40, 60)
```

### runs/2026-09-30-24/verification2.json

```json
{
  "run_id": "2026-09-30-24",
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
      "1차에서 지적한 59. 법·규제·보험·라이선스와의 주제 겹침(노사협의·공동결정 조문, 무인정보단말기 접근성 의무)은 7절(분리 페이지 2026-09-30-area60-s7.md)과 10절이 법 적용 판단을 59. 법·규제·보험·라이선스로 연결하는 방식으로 처리됐다. 새 충돌은 없다."
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
    "6절 수용성 측정 모델 단락: '두 연구는 돌봄·고령자 맥락이어서 물류창고·병원 운영 인력의 수용성에 그대로 옮길 수 있을지는 따로 확인해야 한다. [의견][^ref-1269][^ref-1273]' 문장에 의견 주체를 '구축자 의견'으로 밝히고, 각주는 f10·f11이 뒷받침하는 사실 부분('돌봄·고령자 맥락')에만 걸리게 한다. 주체를 밝히지 않을 거라면 문장을 삭제한다. 이유: 이 판단은 브리프의 어느 finding에도 없고, [의견] 태그에는 누구의 의견인지 적어야 한다(1차에서 f4에 같은 지시를 냈다). 지금 각주대로라면 Heerink 외와 김소라 논문이 그렇게 주장한 것처럼 읽힌다. 같은 문장이 분리 페이지 2026-09-30-area60-s6.md의 세 줄 요약과 본문에 복사돼 있으므로 원래 절을 고쳐 다시 분리되게 한다.",
    "5절 물류창고 표의 수행 자원 칸: '로봇 센터에서는 작업자가 로봇과 함께 피킹을 맡는다. [사실][^ref-1264]'에서 '로봇과 함께'가 가리키는 작업 분담 서술을 빼고, f3이 말하는 범위(로봇 센터 작업자에게 부과되는 피킹 목표량)만 남긴다. 그러면 칸이 비게 되는 경우 f5의 '작업자는 더 주체적인 협업을 요구했다' 문장만 둔다. 이유: f3과 ref-1264는 로봇 센터 작업자의 피킹 목표량과 부상만 다룬다. 로봇과 사람이 어떻게 일을 나누는지는 브리프에 없으므로 [사실]로 쓸 수 없다(드리프트).",
    "7절 관련 표준·프레임워크·오픈소스: 표 앞에 이 절이 다루는 규정 네 가지(ISO/IEC Guide 71:2014, 무인정보단말기 접근성 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조)를 밝히는 도입 문장을 둔다. 내용은 outline 7절 요약과 같게 하고 태그·각주를 붙이며, ref-1276 각주의 원문 미열람 표기는 유지한다. 이유: 자동 분리 뒤 원래 페이지 7절과 분리 페이지의 세 줄 요약에 '위 항목은 …' 문장만 남았는데, 가리키는 표가 없다. 도입 문장이 있으면 분리 뒤에도 원래 페이지에서 뜻이 통한다.",
    "10절 다른 연구영역과의 연결: 첫 문장을 연결되는 세부영역을 번호와 이름으로 요약하는 문장으로 바꾼다. 수준은 outline 10절 요약과 같게 하고, f22의 [추정] 태그와 각주를 붙인다. 이유: 자동 분리 뒤 원래 페이지 10절에는 '아래 연결은 이번 조사의 발견 사항에서 도출한 추정이다.'만 남아, 절 제목이 요구하는 번호·이름 표기 연결이 원래 페이지에서 하나도 보이지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 21건, 미확인 1건, 교차 확인 0건. 강등: f7 사실 → 추정(보고서 수치가 기사 한 곳 기준), f9 사실 → 추정(병원 자체 조사를 전한 단일 기사). 삭제: f2(EU-OSHA 게시 페이지가 위험 목록·참여 권고를 뒷받침하지 않음). 원문 미열람 출처: ref-1276(ISO/IEC Guide 71, 검색 결과로만 확인). 주의: 물류창고 부상 수치(f3)는 논문 원문이 아니라 저자 소속 대학 발표 기준이다. 병원 만족도(f9)는 기관 자체 설문이다. 노사협의·공동결정 조문이 로봇 오케스트레이션의 작업자 데이터 기록에 적용되는지(f18), 화면 접근성 의무가 로봇 화면에 적용되는지는 법적으로 판단되지 않았다. 제조 공장·상업 시설·가정 사례는 확인하지 못했다. ref-1264는 이번 검증에서 직접 열리지 않아(307) 같은 보도문의 재게재와 검색 결과로 확인했다. 같은 대학의 후속 보도(2026-08, 로봇 창고 표지판·부상 관련)가 검색됐으나 열지 못해 반영하지 않았으며, 다음 갱신 실행에서 확인한다. 기존 열린 질문 oq-146·oq-188·oq-266은 해결로 인정하지 않는다(해결 제안 없음). 정정 요청 없음. 검증 검색 3회(리서치 20회와 합쳐 23/30). / 2차 수정 후 재검증. 1차 수정 지시 11건은 모두 페이지에 반영됐다(f2 삭제, f3·f16 기준 명시, f4 의견 주체, f7·f9 강등과 병기, f13·f15 문구 수정, ref-1276 원문 미열람 표기, f22 연결 근거, 5절 현장 유형 구성). 드리프트 1건: 5절 물류창고 수행 자원 칸의 로봇–작업자 분담 서술. 의견 주체 누락 1건: 6절 돌봄 연구 전용 가능성 문장. 자동 분리 뒤 가리키는 대상이 사라진 문장 2건: 7절 '위 항목은', 10절 '아래 연결은'. [분류원문] 보존(소속 대분류 블록, 1·2절, 9절 원문 19장 문장), 섹션 순서 준수, 링크 유효(형식 검증 통과), auto 마커 내용 유지. 적용 사례 표와 site_matrix_updates(물류창고·병원·실외 × 작업 대상·수행 자원·제약·예외·성과), 열린 질문 갱신 4건, 참고문헌·용어집·표준 갱신이 서로 일치한다. 2차 검색 0회. 참고: 자동 분리 요약이 표 뒤 문장을 고르면 참조어가 남는 문제는 pipeline 분리 담당에게도 알린다.",
  "retry_reason": null
}
```
