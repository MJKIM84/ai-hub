(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
| **59. 법·규제·보험·라이선스** | 법·규제 대응, 보험·사고 책임, 오픈소스·라이선스 | 이 현장에서 로봇을 운영하려면 어떤 법·규제·보험·라이선스를 지켜야 하는가? | [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md) | seed |
| **60. 노동·수용성·접근성** | 노동 영향·사회적 수용성, 고령자·장애인·어린이 접근성 | 로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? | [60. 노동·수용성·접근성](labor-acceptance-and-accessibility.md) | seed |

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
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 84건이다(논문 18건 · 기사·보고서 5건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 59건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-494](../../references/ref-494.md) — Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems (발행 2026-08)
- [ref-531](../../references/ref-531.md) — arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers (발행 2026-07)
- [ref-711](../../references/ref-711.md) — Tang, G. 외(arXiv 2606.31339), Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems (발행 2026-06)
- [ref-239](../../references/ref-239.md) — Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF (발행 2026-06)
- [ref-1208](../../references/ref-1208.md) — Shaik, A. S. (SSRN), Liability Allocation in Autonomous Industrial Systems: Who Pays when the AI is Wrong? (발행 2026-05-01)
- [ref-417](../../references/ref-417.md) — Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems (발행 2026-04)
- [ref-168](../../references/ref-168.md) — Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms (발행 2025-12)
- [ref-199](../../references/ref-199.md) — arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding (발행 2024-10)
- [ref-076](../../references/ref-076.md) — DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps (발행 2024-09)
- [ref-465](../../references/ref-465.md) — Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., Toward a Method to Generate Capability Ontologies from Natural Language Descriptions (발행 2024-06)
- 그 밖에 8건

**기사·보고서**

- [ref-1211](../../references/ref-1211.md) — 한국아파트신문 (사설), 공동주택에 밀려오는 로봇, 또 다른 관리책임은 없을까 (발행 2026-09-14)
- [ref-466](../../references/ref-466.md) — 부산일보, KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ (발행 2026-07-24)
- [ref-1193](../../references/ref-1193.md) — 지디넷코리아, 산업데이터 만든 자에게 사용·수익권 부여 (발행 2022-03-15)
- [ref-317](../../references/ref-317.md) — 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 (발행 미확인)
- [ref-316](../../references/ref-316.md) — 건설기술신문, 승강기협, 엘리베이터-로봇 연동 단체표준 제정 (발행 미확인)

**업체 발표**

- [ref-608](../../references/ref-608.md) — OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments (발행 2026-04)
- [ref-559](../../references/ref-559.md) — 세이프틱스(Safetics), 로봇 시스템 위험성평가 가이드 (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-518](../../references/ref-518.md) — ISO, ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition (발행 2026)
- [ref-1191](../../references/ref-1191.md) — European Commission (Shaping Europe's digital future), Data Act explained (발행 2025-12-15)
- [ref-1192](../../references/ref-1192.md) — European Commission (Shaping Europe's digital future), Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (발행 2025-11-19)
- [ref-710](../../references/ref-710.md) — 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 (발행 2025-06-04)
- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-567](../../references/ref-567.md) — Open-RMF (open-rmf/rmf GitHub), [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf (발행 2025-04-04)
- [ref-561](../../references/ref-561.md) — 대한민국 정책브리핑(중소벤처기업부), 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 (발행 2024-11-03)
- [ref-475](../../references/ref-475.md) — 중소벤처기업부(대한민국 정책브리핑), ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! (발행 2024-11)
- [ref-240](../../references/ref-240.md) — ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules (발행 2024-02)
- [ref-130](../../references/ref-130.md) — OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) (발행 2024-01-31)
- 그 밖에 49건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [58. 다사업자 책임·계약·데이터](multi-party-responsibility-contracts-and-data.md) — 영역 심화: 3~11절 첫 작성(병원·가정 적용 사례, 데이터 계약·버전·폐기 규칙·SLA·감사 이력, 책임 경계, 연결 14건, 열린 질문 8건+새 질문 5건), 13절 각주, 1차 조건부 승인 수정 17건 반영, 2차 수정: 9절 표 셋째 행 경계 칸을 '원문 19장 다섯 경계 밖'으로 고침 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area58-s6.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "6. 대표 접근법과 기술" 절(2,613자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 열린 질문](../../topics/2026/2026-09-30-area58-s11.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "11. 열린 질문" 절(1,824자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area58-s7.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,269자)을 옮겼다 (실행 2026-09-30-22)
- 2026-09-30 · 생성 · [58. 다사업자 책임·계약·데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area58-s10.md) — 자동 분리: 58. 다사업자 책임·계약·데이터 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,155자)을 옮겼다 (실행 2026-09-30-22)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24
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

### docs/standards/index.md (요약: 303개 — 이름 · 종류 · 발행 기관)

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
```

### runs/2026-09-30-24/docs_tree.txt

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
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
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
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
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
references/ref-118.md
references/ref-119.md
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
references/ref-121.md
references/ref-122.md
references/ref-123.md
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
      "summary": "물류창고(부상 재분배·데이터 감시), 병원(미국 TUG 민족지, 한국 병원 자체 설문), 실외(보도 로봇과 휠체어 이용자) 사례를 여섯 항목으로 정리했다. 제조 공장·상업 시설·가정 사례는 찾지 못했다.",
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
      "summary": "수용성 측정 모델(알메러 모델, Q방법론), 참여 설계, 직무 설계, 노동자 참여 절차가 대표 접근법이다. 작업자 데이터 기록 기능이 노동자 참여 절차 대상일 가능성은 법적으로 확인되지 않았다. [추정][^ref-1278][^ref-1272][^ref-1271]",
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
      "budget_chars": 700,
      "summary": "ISO/IEC Guide 71:2014, 무인정보단말기 접근성 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조가 이 영역의 기준이다. [사실][^ref-1276][^ref-1268][^ref-1272][^ref-1271]",
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
      "budget_chars": 900,
      "summary": "이 영역은 작업 분담·속도, 부상, 작업자 데이터, 보행 약자와 대기 위치, 목표량 지표, 교육, 화면 접근성, 법 의무, 효과 추정, 적용 현장을 통해 15개 세부영역과 이어지는 것으로 보인다. [추정][^ref-1264][^ref-1265]",
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
      "diff_summary": "영역 심화: 3~11절 첫 작성(물류창고·병원·실외 적용 사례 4건, 수용성 모델·노동자 참여 절차·접근성 의무, 책임 경계, 연결 15개 영역, 열린 질문 8건), 각주 15건, 프런트매터 related_areas·tags·sources·confidence 채움"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"8. 대표 연구와 자료\" 절(1,290자)을 옮겼다"
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
      "path": "docs/topics/2026/2026-09-30-area60-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(847자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"3. 왜 중요한가\" 절(762자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"6. 대표 접근법과 기술\" 절(737자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area60-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 60. 노동·수용성·접근성 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(643자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 60. 노동·수용성·접근성 | 영역 심화: 3~11절 첫 작성(물류창고·병원·실외 적용 사례, 수용성 모델·노동자 참여 절차·접근성 의무, 책임 경계), 출처 15건, 강등 2건·삭제 1건 반영 | run 2026-09-30-24",
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
    "3·5절 물류창고 부상 수치(f3): ILR Review 논문 원문과 데이터 출처를 열어 대학 발표 기준을 논문 기준으로 바꾸고, 검증 노트가 언급한 같은 대학의 2026-08 후속 보도(로봇 창고 표지판·부상)를 확인해야 한다.",
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
    "분량 초과 자동 분리: 60. 노동·수용성·접근성 본문 9,108자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,155자"
  ]
}
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
| 수행 자원 | 로봇 센터에서는 작업자가 로봇과 함께 피킹을 맡는다. [사실][^ref-1264] 작업자는 더 주체적인 협업을 요구했다. [사실][^ref-1278] |
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

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1269] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1273] 두 연구는 돌봄·고령자 맥락이어서 물류창고·병원 운영 인력의 수용성에 그대로 옮길 수 있을지는 따로 확인해야 한다. [의견][^ref-1269][^ref-1273]

자세한 내용은 주제 페이지 [60. 노동·수용성·접근성 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area60-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

위 항목은 법적 적합성 판단의 근거가 아니라 이 영역이 참고하는 규정 목록이다. 법 적용 판단은 [59. 법·규제·보험·라이선스](law-regulation-insurance-and-licensing.md)와 이어진다.

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

아래 연결은 이번 조사의 발견 사항에서 도출한 추정이다.

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
[^ref-1277]: European Agency for Safety and Health at Work (EU-OSHA), Advanced robotics and automation: implications for occupational safety and health, 2022-06-16, https://osha.europa.eu/en/publications/advanced-robotics-and-automation-implications-occupational-safety-and-health, 접근일 2026-09-30
[^ref-1278]: Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics), Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety, 2026, https://doi.org/10.1007/s12369-026-01359-1, 접근일 2026-09-30
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
sources: [ref-1264, ref-1265, ref-1266, ref-1267, ref-1269, ref-1151, ref-1275, ref-1277, ref-1278]
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

[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1267]: 한국노동연구원 (국회 정책정보 포털 NABIS 게재), 기술 혁신과 노동시장 변화, 2024-12, https://www.nabis.go.kr/issuReportDetailView.do?menucd=130&gbnCode=P52&refCode=10&poIdx=16861, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
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

- 위 항목은 법적 적합성 판단의 근거가 아니라 이 영역이 참고하는 규정 목록이다. 법 적용 판단은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)와 이어진다.
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

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
sources: [ref-1264, ref-1265, ref-1266, ref-1268, ref-1269, ref-1151, ref-1273, ref-1274, ref-1275, ref-1278]
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

[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1269]: Heerink, M., Kröse, B., Evers, V., Wielinga, B. (International Journal of Social Robotics), Assessing acceptance of assistive social agent technology by older adults: the Almere model, 2010, https://doi.org/10.1007/s12369-010-0068-5, 접근일 2026-09-30
[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
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

- 알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1269] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1273] 두 연구는 돌봄·고령자 맥락이어서 물류창고·병원 운영 인력의 수용성에 그대로 옮길 수 있을지는 따로 확인해야 한다. [의견][^ref-1269][^ref-1273]
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

### 수용성 측정 모델

알메러 모델은 요양시설과 가정에서 세 가지 소셜 에이전트로 시험해 사용 의도 분산의 59~79%, 실제 사용 분산의 49~59%를 설명했다(2010). [사실][^ref-1269] 국내에서는 Q방법론으로 노인 이용자·가족·돌봄 종사자의 돌봄로봇 인식을 네 유형으로 나눴고, '불가피한 대체재' 유형의 설명력이 가장 컸다(2023). [사실][^ref-1273] 두 연구는 돌봄·고령자 맥락이어서 물류창고·병원 운영 인력의 수용성에 그대로 옮길 수 있을지는 따로 확인해야 한다. [의견][^ref-1269][^ref-1273]

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
sources: [ref-1264, ref-1265, ref-1266, ref-1268, ref-1151, ref-1271, ref-1272, ref-1274, ref-1275, ref-1278]
last_run: 2026-09-30
version: 1
split_from: docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md#10
---

[홈](../../index.md) › [주제](../index.md) › 60. 노동·수용성·접근성 — 다른 연구영역과의 연결

# 60. 노동·수용성·접근성 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 연결은 이번 조사의 발견 사항에서 도출한 추정이다.
- 이 페이지는 [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 연결은 이번 조사의 발견 사항에서 도출한 추정이다.

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

[^ref-1264]: George Mason University Costello College of Business, Warehouse automation hasn't made workers safer — it's just reshuffled risk, 2025-08-26, https://business.gmu.edu/news/2025-08/warehouse-automation-hasnt-made-workers-safer-its-just-reshuffled-risk, 접근일 2026-09-30
[^ref-1265]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-09-30
[^ref-1266]: 한국경제, 로봇이 제조업 일자리 뺏는다? 청년·고숙련 … (제목 일부만 확인), 2025-04-01, https://www.hankyung.com/article/2025040138391, 접근일 2026-09-30
[^ref-1268]: 대한민국 정책브리핑 (보건복지부), 장애인 접근성 갖춘 무인정보단말기 설치 의무화 전면 시행, 2026-01-28, https://www.korea.kr/news/policyNewsView.do?newsId=148958690, 접근일 2026-09-30
[^ref-1151]: Mutlu, B., Forlizzi, J. (HRI 2008), Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction, 2008, https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf, 접근일 2026-09-30
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


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 6절 수용성 측정 모델 단락: '두 연구는 돌봄·고령자 맥락이어서 물류창고·병원 운영 인력의 수용성에 그대로 옮길 수 있을지는 따로 확인해야 한다. [의견][^ref-1269][^ref-1273]' 문장에 의견 주체를 '구축자 의견'으로 밝히고, 각주는 f10·f11이 뒷받침하는 사실 부분('돌봄·고령자 맥락')에만 걸리게 한다. 주체를 밝히지 않을 거라면 문장을 삭제한다. 이유: 이 판단은 브리프의 어느 finding에도 없고, [의견] 태그에는 누구의 의견인지 적어야 한다(1차에서 f4에 같은 지시를 냈다). 지금 각주대로라면 Heerink 외와 김소라 논문이 그렇게 주장한 것처럼 읽힌다. 같은 문장이 분리 페이지 2026-09-30-area60-s6.md의 세 줄 요약과 본문에 복사돼 있으므로 원래 절을 고쳐 다시 분리되게 한다.
    - 5절 물류창고 표의 수행 자원 칸: '로봇 센터에서는 작업자가 로봇과 함께 피킹을 맡는다. [사실][^ref-1264]'에서 '로봇과 함께'가 가리키는 작업 분담 서술을 빼고, f3이 말하는 범위(로봇 센터 작업자에게 부과되는 피킹 목표량)만 남긴다. 그러면 칸이 비게 되는 경우 f5의 '작업자는 더 주체적인 협업을 요구했다' 문장만 둔다. 이유: f3과 ref-1264는 로봇 센터 작업자의 피킹 목표량과 부상만 다룬다. 로봇과 사람이 어떻게 일을 나누는지는 브리프에 없으므로 [사실]로 쓸 수 없다(드리프트).
    - 7절 관련 표준·프레임워크·오픈소스: 표 앞에 이 절이 다루는 규정 네 가지(ISO/IEC Guide 71:2014, 무인정보단말기 접근성 의무, 근로자참여법 제20조, 독일 사업장조직법 제87조)를 밝히는 도입 문장을 둔다. 내용은 outline 7절 요약과 같게 하고 태그·각주를 붙이며, ref-1276 각주의 원문 미열람 표기는 유지한다. 이유: 자동 분리 뒤 원래 페이지 7절과 분리 페이지의 세 줄 요약에 '위 항목은 …' 문장만 남았는데, 가리키는 표가 없다. 도입 문장이 있으면 분리 뒤에도 원래 페이지에서 뜻이 통한다.
    - 10절 다른 연구영역과의 연결: 첫 문장을 연결되는 세부영역을 번호와 이름으로 요약하는 문장으로 바꾼다. 수준은 outline 10절 요약과 같게 하고, f22의 [추정] 태그와 각주를 붙인다. 이유: 자동 분리 뒤 원래 페이지 10절에는 '아래 연결은 이번 조사의 발견 사항에서 도출한 추정이다.'만 남아, 절 제목이 요구하는 번호·이름 표기 연결이 원래 페이지에서 하나도 보이지 않는다.
- 검증 노트: 판정: 조건부 승인. 확인 21건, 미확인 1건, 교차 확인 0건. 강등: f7 사실 → 추정(보고서 수치가 기사 한 곳 기준), f9 사실 → 추정(병원 자체 조사를 전한 단일 기사). 삭제: f2(EU-OSHA 게시 페이지가 위험 목록·참여 권고를 뒷받침하지 않음). 원문 미열람 출처: ref-1276(ISO/IEC Guide 71, 검색 결과로만 확인). 주의: 물류창고 부상 수치(f3)는 논문 원문이 아니라 저자 소속 대학 발표 기준이다. 병원 만족도(f9)는 기관 자체 설문이다. 노사협의·공동결정 조문이 로봇 오케스트레이션의 작업자 데이터 기록에 적용되는지(f18), 화면 접근성 의무가 로봇 화면에 적용되는지는 법적으로 판단되지 않았다. 제조 공장·상업 시설·가정 사례는 확인하지 못했다. ref-1264는 이번 검증에서 직접 열리지 않아(307) 같은 보도문의 재게재와 검색 결과로 확인했다. 같은 대학의 후속 보도(2026-08, 로봇 창고 표지판·부상 관련)가 검색됐으나 열지 못해 반영하지 않았으며, 다음 갱신 실행에서 확인한다. 기존 열린 질문 oq-146·oq-188·oq-266은 해결로 인정하지 않는다(해결 제안 없음). 정정 요청 없음. 검증 검색 3회(리서치 20회와 합쳐 23/30). / 2차 수정 후 재검증. 1차 수정 지시 11건은 모두 페이지에 반영됐다(f2 삭제, f3·f16 기준 명시, f4 의견 주체, f7·f9 강등과 병기, f13·f15 문구 수정, ref-1276 원문 미열람 표기, f22 연결 근거, 5절 현장 유형 구성). 드리프트 1건: 5절 물류창고 수행 자원 칸의 로봇–작업자 분담 서술. 의견 주체 누락 1건: 6절 돌봄 연구 전용 가능성 문장. 자동 분리 뒤 가리키는 대상이 사라진 문장 2건: 7절 '위 항목은', 10절 '아래 연결은'. [분류원문] 보존(소속 대분류 블록, 1·2절, 9절 원문 19장 문장), 섹션 순서 준수, 링크 유효(형식 검증 통과), auto 마커 내용 유지. 적용 사례 표와 site_matrix_updates(물류창고·병원·실외 × 작업 대상·수행 자원·제약·예외·성과), 열린 질문 갱신 4건, 참고문헌·용어집·표준 갱신이 서로 일치한다. 2차 검색 0회. 참고: 자동 분리 요약이 표 뒤 문장을 고르면 참조어가 남는 문제는 pipeline 분리 담당에게도 알린다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
